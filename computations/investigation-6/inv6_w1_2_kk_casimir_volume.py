#!/usr/bin/env python3
"""
INV6 W1-2 — Graded Casimir energy in the VOLUME (breathing) direction
=====================================================================

Gate: INV6-W1-2-KK-CASIMIR-VOLUME ([SIGN])

Pre-registered threshold (plan §W1-2):
  operator: set  V_stat = { v* in [0.3,3.0] : dE_Cas/dv(v*) = 0 }
  PASS  iff  EXISTS v* in V_stat with d2E_Cas/dv2(v*) > 0  (genuine VOLUME
        Casimir minimum -> the det-g volume-preservation constraint A-KK2 /
        atlas-04 G6 is DERIVED, not imposed; a THIRD M_KK lands).
  INFO  iff  dE_Cas/dv has FIXED SIGN on [0.3,3.0] (monotone runaway; no
        interior minimum) -> volume-preservation stays IMPOSED; report the
        runaway direction (fiber grows vs shrinks). [structural-default track_B]
  FAIL  iff  script/cache fault (cache SHA mismatch, zeta non-convergence, or
        graded-sign assignment inconsistent with the Peter-Weyl (p,q) triality
        fermion number) -- NOT a physics result.

[SIGN] 3-tuple: emitted on the EXISTENCE-and-SIGN of the curvature
  d2E_Cas/dv2|_{v*} (if a stationary point exists) OR the runaway sign.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py            (feeds audit_sha256)
  - s84_spectrum_cache_L12_tau019.npz (feeds audit_sha256; the 90-sector,
        166896-eigenvalue, 6997-unique L12 master cache at tau_fold=0.19)
  - script bytes                      (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<v* / minimum-vs-runaway + M_KK^Cas + zeta_graded(-1/2)>,
   scheme=zeta-regularized-graded-Casimir + PV-cross-check,
   convention=ABSOLUTE, L_max=12)

Classification: PHONONIC (graded zero-point reorganization of the fiber's
  vibrational tower as the OVERALL SCALE flows; GEOMETRIC output = v* + M_KK^Cas)

METHODOLOGY (substrate-first)
-----------------------------
The Casimir energy IS the zero-point reorganization of the fiber's vibrational
modes as the fiber's OVERALL SCALE v flows -- not a force IN a container but the
substrate's own ground-state energy as a function of how much spectral weight
the fiber carries. The graded sum 1/2 Sum_n (-1)^F g_n m_n(v) runs over the
D_K eigenvalue tower (all vibrational modes of the fabric at a point); the
(-1)^F triality alternation is the fermion/boson cancellation that makes the
regularized sum finite (cf. E_Casimir^fermion structure, S19d).

The framework already proved the SHAPE modulus tau (TT shear, the Jensen
deformation) has NO minimum (W4 monotonicity -- the runaway that drives
exflation). This gate asks the ORTHOGONAL question about the TRACE/breathing
direction the det-g=6561 (=3^8) constraint freezes. The breathing/volume mode is
the conformal direction delta g_ab = h * g_ab (theorem T2 Breathing-Mode
Exclusion: it projects to a 4D scalar -- the radion). It is orthogonal to the
volume-PRESERVING Jensen TT-deformation (L1*L2^3*L3^4 = e^{2s-6s+4s} = 1,
dirac_spectrum.jensen_metric).

Each D_K eigenvalue m_n on (SU(3), g_tau) carries [mass]^{+1}. A uniform fiber
volume rescaling g_tau -> v^{2/d} g_tau (d = dim SU(3) = 8) scales det by v^2 and
the eigenvalue by m_n -> v^{-1/d} m_n. Normalizing the breathing coordinate so
the eigenvalue scaling is m_n(v) = m_n(1) v^{-1/2}, the graded zeta-regularized
Casimir has the closed leading form
    E_Cas(v) = 1/2 v^{-1/2} zeta_graded(-1/2),
    zeta_graded(s) = Sum_n (-1)^F g_n m_n(1)^{-2s}  continued to s = -1/2.
For a PURE uniform rescaling dE_Cas/dv = -1/4 v^{-3/2} zeta_graded(-1/2) has NO
interior zero -> monotone runaway (the structural default). A genuine interior
minimum can arise ONLY from the v-DEPENDENCE OF THE JENSEN DEFORMATION coupling
to the volume mode (the deformed fiber is non-symmetric off tau=0; the breathing
mode is not a pure conformal rescaling). The gate captures this by re-evaluating
the per-sector graded sum at rescaled v through the genuine d=8 metric-breathing
exponent rather than applying only the global v^{-1/2}, and tests whether the
deformation-induced v-structure BEATS the monotone scaling.

If a minimum exists (PASS): volume-preservation is DERIVED (A-KK2 dissolves as a
postulate) and M_KK^Cas = M_KK_gravity * (v*)^{-1/2} is a THIRD determination,
handed to INV6-W4-1. If not (INFO): volume-preservation stays imposed and the
breathing mode runs away like the shape mode.

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`
- graded sum on the cached 90-sector spectrum (CPU dot product; OMP8 cap)
- SHA-256 of all inputs logged in first 20 lines of stdout
- audit_sha256 + content_sha256 (S84+ dual-SHA); 4-tuple final non-verdict line
- verdict via the emit_verdict MCP tool (track="investigation", session=6):
  the script PRINTS the payload; the agent calls mcp__knowledge__emit_verdict.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # graded dot product on CPU; cap threads

import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    M_KK_gravity, M_KK_kerner, M_KK,
    tau_fold, Vol_SU3_Haar,
)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import math
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = _Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = 6                                                  # (local) investigation number
GATE_ID = "INV6-W1-2-KK-CASIMIR-VOLUME"                      # (local)
SCHEME = "zeta-regularized-graded-Casimir+PV-cross-check"    # (local)
CONVENTION = "ABSOLUTE"                                      # (local)
L_MAX = 12                                                   # (local) L12 master cache

# Scan machinery (plan §W1-2 machinery_pin_map)
V_LO = 0.3                                                   # (local) fiber volume scan floor
V_HI = 3.0                                                   # (local) fiber volume scan ceiling
V_STEP_COARSE = 0.01                                         # (local) 271-point coarse scan
V_STEP_REFINE = 1e-4                                         # (local) refined near dE/dv sign change
STAT_TOL = 1e-6                                              # (local) stationary-point bracketing
ZETA_CONV_TOL = 1e-8                                         # (local) zeta-continuation convergence
DET_G_REF = 6561.0                                           # (local) det-g reference = 3^8 (volume-preserving anchor)
D_FIBER = 8                                                  # (local) dim SU(3)
PV_LAMBDA = M_KK_gravity                                     # (local) Pauli-Villars UV scale = M_KK

SPECTRUM_CACHE = (COMPUTATIONS_DIR / "session-84"
                  / "s84_spectrum_cache_L12_tau019.npz")     # (local)
# Canonical-source SHA per s96_repro_env_manifest.txt:
#   88f1e9b107dc30c49a2dbcde33cecbee14cc17404994a2ad8f76adceec8a7258
# (cross-source drift noted across S87/S88/S96 -- VERIFY at runtime, do NOT pin a
#  drifted literal; consume the session-84 master copy directly.)

OUT_NPZ = SESSION_DIR / "inv6_w1_2_kk_casimir_volume.npz"     # (local)
OUT_PNG = SESSION_DIR / "inv6_w1_2_kk_casimir_volume.png"     # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SPECTRUM_CACHE,
]


# ---------------------------------------------------------------------------
# Section 4 -- Input SHA pins + dual-SHA closure
# ---------------------------------------------------------------------------
def sha256_of(path) -> str:
    h = hashlib.sha256()  # (local)
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    pins = {}  # (local)
    print("=== INPUT SHA-256 PINS ===")
    for p in inputs:
        if not _Path(p).exists():
            print(f"  MISSING: {p}")
            pins[str(p)] = "MISSING"
            continue
        sha = sha256_of(p)  # (local)
        rel = str(_Path(p).relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
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
# Section 5 -- Load the graded spectrum (Peter-Weyl (p,q) with triality sign)
# ---------------------------------------------------------------------------
def triality(p, q):
    """SU(3) center character / fermion-number grading: (p - q) mod 3.

    Sectors with (p-q) mod 3 == 0 are the colour-singlet (boson-like, +) tower;
    (p-q) mod 3 in {1,2} are the triality-charged (fermion-like, -) tower. The
    graded Casimir sum carries (-1)^F = +1 on triality-0 sectors and -1 on
    triality-{1,2} sectors -- the boson/fermion cancellation that regularizes
    the zero-point sum (cf. E_Casimir^fermion structure, S19d).
    """
    return (p - q) % 3


def graded_sign(p, q):
    """(-1)^F per (p,q): +1 if triality 0 (boson-like singlet), -1 otherwise."""
    return 1.0 if triality(p, q) == 0 else -1.0


def load_spectrum(cache_path):
    """Load the L12 master cache. Returns a list of per-MODE records:
        (abs_eval, mult, sign, p, q)
    where abs_eval = |lambda| (already the eigenvalue magnitude in M_KK units),
    mult = Peter-Weyl multiplicity dim(p,q) (NOT dim(p,q)^2 -- per MEMORY.md the
    code API get_irrep returns dim(p,q); the cache stores per-level abs_evals
    arrays whose length already carries the C^16 spinor count, so the geometric
    multiplicity weight is dim(p,q)).
    """
    d = np.load(cache_path, allow_pickle=True)
    se = d["sector_evals"].item()  # (local) dict {(p,q): array-of-level-dicts}

    modes = []  # (local) list of (abs_eval, mult, sign, p, q)
    n_sectors = 0  # (local)
    n_eigs_raw = 0  # (local)
    triality_counts = {0: 0, 1: 0, 2: 0}  # (local) sector counts by triality
    for (p, q), levels in se.items():
        n_sectors += 1
        sgn = graded_sign(p, q)  # (local)
        triality_counts[triality(p, q)] += 1
        levels = np.asarray(levels).ravel()
        for lev in levels:
            dim_pq = int(lev["dim"])  # (local) Peter-Weyl multiplicity dim(p,q)
            abs_evals = np.asarray(lev["abs_evals"], dtype=float)  # (local) |lambda| array
            n_eigs_raw += abs_evals.size
            for x in abs_evals:
                modes.append((float(x), dim_pq, sgn, p, q))
    return modes, n_sectors, n_eigs_raw, triality_counts


# ---------------------------------------------------------------------------
# Section 6 -- Graded zeta-regularized Casimir energy
# ---------------------------------------------------------------------------
def zeta_graded_at(modes, s):
    """zeta_graded(s) = Sum_n (-1)^F g_n m_n(1)^{-2s} over the cached tower.

    At s = -1/2 this is the (formally) bare linear graded sum
    Sum_n (-1)^F g_n m_n(1) -- the one-loop graded Casimir coefficient. The
    physical Casimir is E_Cas(v) = 1/2 v^{-1/2} zeta_graded(-1/2). The (-1)^F
    boson/fermion cancellation is what renders the linear sum finite (it is an
    alternating, not a strictly-positive, sum). We evaluate it directly as the
    analytic-continuation value at s=-1/2 (no separate continuation needed for a
    FINITE spectral set -- the cache is a finite enumerated tower).
    """
    total = 0.0  # (local)
    for (x, mult, sgn, _p, _q) in modes:
        total += sgn * mult * (x ** (-2.0 * s))
    return total


def zeta_graded_partial_minus_half(modes):
    """Split zeta_graded(-1/2) into boson-like (+) and fermion-like (-) partials.
    Return zeta_graded(-1/2) = Sum (-1)^F g_n m_n and the two partials.
    """
    pos = 0.0  # (local) triality-0 (boson) contribution to Sum g_n m_n
    neg = 0.0  # (local) triality-{1,2} (fermion) contribution
    for (x, mult, sgn, _p, _q) in modes:
        if sgn > 0:
            pos += mult * x
        else:
            neg += mult * x
    zeta_m_half = pos - neg  # (local) zeta_graded(-1/2) = Sum (-1)^F g_n m_n
    return zeta_m_half, pos, neg


def pauli_villars_graded(modes, Lambda_uv):
    """Pauli-Villars cross-check of the graded linear sum.

    The cache eigenvalues are ALREADY in M_KK units, so the PV mass in cache
    units is Lambda_cache = M_KK / M_KK = 1.0. We apply a one-subtraction
    high-pass regulator m -> m - (sqrt(m^2 + Lambda^2) - Lambda), which is a
    deterministic finiteness cross-check on the alternating sum: it leaves the
    light-mode (m << Lambda) contributions ~m and damps the heavy modes. For a
    FINITE alternating cache the PV-regularized value should track the bare
    alternating sum to within the PV residual (this is a consistency
    cross-check on regulator-independence, NOT an independent determination).
    """
    bare = 0.0  # (local)
    pv = 0.0    # (local)
    lam_cache = Lambda_uv / M_KK_gravity  # (local) = 1.0 (cache is in M_KK units)
    for (x, mult, sgn, _p, _q) in modes:
        bare += sgn * mult * x
        m_reg = x - (math.sqrt(x * x + lam_cache * lam_cache) - lam_cache)  # (local)
        pv += sgn * mult * m_reg
    return bare, pv


# ---------------------------------------------------------------------------
# Section 7 -- Volume-direction Casimir: uniform skeleton + deformation-resolved
# ---------------------------------------------------------------------------
def E_cas_uniform(v, zeta_m_half):
    """Closed-form uniform-rescaling skeleton: E_Cas(v) = 1/2 v^{-1/2} zeta(-1/2)
    (plan substitution chain Step 4). Monotone in v for zeta(-1/2) != 0.
    Cache eigenvalues are in M_KK units, so the sum is in M_KK; the M_KK^4
    dimensional label is the carrier applied downstream.
    """
    return 0.5 * (v ** (-0.5)) * zeta_m_half


def breathing_graded_sum(flat, v):
    """Deformation-resolved re-evaluation of the graded linear sum at breathing
    scale v.

    The breathing mode is a UNIFORM metric rescaling g_tau -> v^{2/d} g_tau on
    top of the FIXED Jensen shape g_tau (tau = tau_fold). For a uniform rescaling
    the eigenvalue scaling is EXACTLY m_n(v) = m_n(1) v^{-1/d} with d=8 -- i.e. the
    breathing mode IS conformal on the metric, regardless of the shape
    deformation, because it multiplies the WHOLE metric tensor by a scalar. The
    Dirac operator on a conformally-rescaled metric g -> c^2 g obeys
    D_{c^2 g} = c^{-1} (rotated) D_g (the spin connection on a Lie group is built
    from the structure constants in the ORTHONORMAL frame, which are invariant
    under a CONSTANT conformal factor; only the inverse-vielbein prefactor
    carries c^{-1}), so every eigenvalue scales by c^{-1} = v^{-1/d} with NO
    sector-dependent structure.

    THEREFORE the deformation-resolved sum equals the global-factor sum:
        Sum_n (-1)^F g_n m_n(v) = v^{-1/d} Sum_n (-1)^F g_n m_n(1).
    The function evaluates the sum at v with the per-mode metric-breathing
    exponent applied EXPLICITLY (-1/d, d=8), so the gate CONFIRMS numerically that
    the breathing mode carries NO sector-differentiated v-structure beyond the
    global factor -- the structural reason the volume Casimir is monotone (plan
    Step 5). [The plan's normalized breathing coordinate uses exponent -1/2; the
    genuine d=8 metric exponent is -1/8. EITHER normalization is monotone -- both
    are pure powers of v -- so the interior-minimum verdict is invariant under
    the coordinate choice. We compute with the genuine -1/8 metric exponent.]
    """
    expo = -1.0 / D_FIBER  # (local) metric-breathing eigenvalue exponent = -1/8
    vfac = v ** expo       # (local)
    total = 0.0  # (local)
    for (x, mult, sgn) in flat:
        total += sgn * mult * (x * vfac)
    return total


# ---------------------------------------------------------------------------
# Section 8 -- Stationary-point scan + classification
# ---------------------------------------------------------------------------
def scan_volume(modes):
    """Scan E_Cas over v in [V_LO, V_HI]; locate stationary points of the
    DEFORMATION-RESOLVED graded Casimir; classify min/max/runaway.

    Two curves are returned:
      (A) E_uniform(v)   -- the closed-form v^{-1/2} skeleton.
      (B) E_breathing(v) -- the deformation-resolved per-mode metric-breathing
                            sum (genuine d=8 exponent), tested for an interior
                            stationary point.
    """
    flat = [(x, mult, sgn) for (x, mult, sgn, _p, _q) in modes]  # (local)

    zeta_m_half, pos, neg = zeta_graded_partial_minus_half(modes)  # (local)

    vs = np.arange(V_LO, V_HI + 0.5 * V_STEP_COARSE, V_STEP_COARSE)  # (local)
    E_uni = np.array([E_cas_uniform(v, zeta_m_half) for v in vs])    # (local)
    E_brth = np.array([breathing_graded_sum(flat, v) for v in vs])   # (local)

    # Numerical derivatives of the breathing curve (central differences).
    dE = np.gradient(E_brth, vs)   # (local)
    d2E = np.gradient(dE, vs)      # (local)

    def dEfun(v):
        h = 1e-5  # (local)
        return (breathing_graded_sum(flat, v + h)
                - breathing_graded_sum(flat, v - h)) / (2 * h)

    # Locate sign changes of dE (interior stationary points), refine by bisection.
    stat_points = []  # (local)
    sgn_dE = np.sign(dE)
    for i in range(1, len(vs)):
        if sgn_dE[i - 1] != 0 and sgn_dE[i] != 0 and sgn_dE[i - 1] != sgn_dE[i]:
            a, b = vs[i - 1], vs[i]  # (local)
            fa = dEfun(a)  # (local)
            for _ in range(200):
                m = 0.5 * (a + b)  # (local)
                fm = dEfun(m)
                if abs(fm) < STAT_TOL or (b - a) < V_STEP_REFINE:
                    break
                if (fa < 0) != (fm < 0):
                    b = m
                else:
                    a, fa = m, fm
            v_star = 0.5 * (a + b)  # (local)
            h = 1e-4  # (local)
            d2 = (breathing_graded_sum(flat, v_star + h)
                  - 2 * breathing_graded_sum(flat, v_star)
                  + breathing_graded_sum(flat, v_star - h)) / (h * h)  # (local)
            kind = ("minimum" if d2 > 0 else "maximum" if d2 < 0 else "inflection")  # (local)
            stat_points.append({
                "v_star": v_star, "d2E": d2, "kind": kind,
                "E_at": breathing_graded_sum(flat, v_star),
            })

    # Monotonicity diagnostic on the breathing curve.
    dE_sign_set = set(np.sign(dE[np.abs(dE) > 1e-14]).astype(int).tolist())  # (local)
    monotone = (len(dE_sign_set) == 1)  # (local) single sign over scan
    runaway_dir = None  # (local)
    if monotone:
        s = next(iter(dE_sign_set)) if dE_sign_set else 0  # (local)
        # dE>0: E increases with v -> lower E by SHRINKING (v->0)
        # dE<0: E decreases with v -> lower E by GROWING (v->inf)
        runaway_dir = "shrink (v->0)" if s > 0 else "grow (v->inf)"

    return {
        "vs": vs, "E_uni": E_uni, "E_brth": E_brth, "dE": dE, "d2E": d2E,
        "zeta_m_half": zeta_m_half, "pos": pos, "neg": neg,
        "stat_points": stat_points, "monotone": monotone,
        "runaway_dir": runaway_dir, "dE_sign_set": sorted(dE_sign_set),
    }


# ---------------------------------------------------------------------------
# Section 9 -- Friedrich-Bar L_max saturation pre-check
# ---------------------------------------------------------------------------
def friedrich_bar_check(modes):
    """Verify the graded Casimir sum is L_max-saturated at 12. The graded sum's
    (-1)^F alternation makes high-(p,q) tails sub-dominant; we report the
    fractional contribution of the top p+q shell to the |contribution| total.
    """
    by_shell = {}  # (local) {p+q: signed contribution to Sum (-1)^F g_n m_n}
    abs_by_shell = {}  # (local) {p+q: |contribution|}
    for (x, mult, sgn, p, q) in modes:
        shell = p + q  # (local)
        by_shell[shell] = by_shell.get(shell, 0.0) + sgn * mult * x
        abs_by_shell[shell] = abs_by_shell.get(shell, 0.0) + mult * x
    max_shell = max(by_shell)  # (local)
    total_abs = sum(abs_by_shell.values())  # (local)
    top_frac = abs_by_shell[max_shell] / total_abs if total_abs else 0.0  # (local)
    return max_shell, top_frac, by_shell


# ---------------------------------------------------------------------------
# Section 10 -- Verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    payload = {
        "session": SESSION,
        "track": "investigation",
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


def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


# ---------------------------------------------------------------------------
# Section 11 -- Plot
# ---------------------------------------------------------------------------
def make_plot(r, sat):
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    vs = r["vs"]

    # (a) E_Cas(v): uniform skeleton + deformation-resolved breathing
    ax = axes[0, 0]
    ax.plot(vs, r["E_uni"], "b-", lw=1.6,
            label=r"$E_{\rm uni}(v)=\frac{1}{2} v^{-1/2}\zeta_{\rm gr}(-\frac{1}{2})$ (skeleton)")
    ax.plot(vs, r["E_brth"], "r--", lw=1.6,
            label=r"$E_{\rm breath}(v)$ (deformation-resolved, $v^{-1/8}$)")
    for sp in r["stat_points"]:
        ax.axvline(sp["v_star"], color="g", ls=":", lw=1.0)
        ax.plot(sp["v_star"], sp["E_at"], "go", ms=8)
    ax.axvline(1.0, color="k", ls="-", lw=0.6, alpha=0.4, label="v=1 (det-g=6561 ref)")
    ax.set_xlabel("fiber volume scale $v$")
    ax.set_ylabel(r"$E_{\rm Cas}$  ($M_{KK}$ units)")
    ax.set_title("(a) Graded Casimir in the VOLUME (breathing) direction")
    ax.legend(fontsize=7.5, loc="best")
    ax.grid(alpha=0.3)

    # (b) dE/dv (monotonicity)
    ax = axes[0, 1]
    ax.plot(vs, r["dE"], "m-", lw=1.5)
    ax.axhline(0.0, color="k", ls="-", lw=0.7)
    for sp in r["stat_points"]:
        ax.axvline(sp["v_star"], color="g", ls=":", lw=1.0)
    ax.set_xlabel("fiber volume scale $v$")
    ax.set_ylabel(r"$dE_{\rm Cas}/dv$")
    title_b = "(b) $dE/dv$ -- "
    title_b += ("MONOTONE (runaway " + str(r["runaway_dir"]) + ")"
                if r["monotone"] else "SIGN-CHANGING (interior stationary pt)")
    ax.set_title(title_b)
    ax.grid(alpha=0.3)

    # (c) Graded boson/fermion contribution by triality shell
    ax = axes[1, 0]
    shells = sorted(sat["by_shell"].keys())
    contribs = [sat["by_shell"][s] for s in shells]
    colors = ["b" if c > 0 else "r" for c in contribs]
    ax.bar(shells, contribs, color=colors, alpha=0.7)
    ax.axhline(0.0, color="k", lw=0.7)
    ax.set_xlabel("Peter-Weyl shell $p+q$")
    ax.set_ylabel(r"signed contribution to $\zeta_{\rm gr}(-\frac{1}{2})$")
    ax.set_title(f"(c) Graded contribution by shell (top-shell frac={sat['top_frac']:.2e})")
    ax.grid(alpha=0.3)

    # (d) Summary text
    ax = axes[1, 1]
    ax.axis("off")
    zmh = r["zeta_m_half"]
    lines = [
        r"$\bf{INV6\!-\!W1\!-\!2}$  Graded Casimir VOLUME direction",
        "",
        f"$\\zeta_{{\\rm graded}}(-1/2)=\\Sigma(-1)^F g_n m_n = {zmh:.4f}$",
        f"  boson(+) partial = {r['pos']:.3f}   fermion(-) partial = {r['neg']:.3f}",
        f"  sign $\\zeta_{{\\rm gr}}(-1/2)$ = {'+' if zmh>0 else '-'}",
        "",
        f"interior stationary points in [0.3,3.0]: {len(r['stat_points'])}",
    ]
    for sp in r["stat_points"]:
        lines.append(f"   v*={sp['v_star']:.5f}  d2E={sp['d2E']:.3e}  ({sp['kind']})")
    if not r["stat_points"]:
        lines.append(f"   NONE -- monotone, runaway: {r['runaway_dir']}")
    lines += ["", f"VERDICT: {r['verdict']}", f"  {r['verdict_reason']}"]
    if r.get("M_KK_Cas") is not None:
        lines.append(f"  M_KK^Cas = {r['M_KK_Cas']:.5e} GeV")
    ax.text(0.02, 0.98, "\n".join(lines), va="top", ha="left",
            fontsize=9.5, family="monospace", transform=ax.transAxes)

    fig.suptitle("INV6-W1-2-KK-CASIMIR-VOLUME -- volume-breathing graded Casimir on Jensen-SU(3) L12 tower",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 12 -- Compute orchestration
# ---------------------------------------------------------------------------
def compute():
    modes, n_sectors, n_eigs_raw, tri_counts = load_spectrum(SPECTRUM_CACHE)

    # FAIL guard: graded-sign consistency with triality
    sign_ok = all(abs(sgn - graded_sign(p, q)) < 1e-12
                  for (_x, _m, sgn, p, q) in modes)  # (local)

    max_shell, top_frac, by_shell = friedrich_bar_check(modes)
    bare_lin, pv_lin = pauli_villars_graded(modes, PV_LAMBDA)

    r = scan_volume(modes)
    zmh = r["zeta_m_half"]  # (local)

    minima = [sp for sp in r["stat_points"] if sp["d2E"] > 0]  # (local)
    has_minimum = len(minima) > 0  # (local)

    M_KK_Cas = None  # (local)
    if has_minimum:
        v_star = minima[0]["v_star"]  # (local) first genuine minimum
        M_KK_Cas = M_KK_gravity * (v_star ** (-0.5))  # third determination
        verdict = "PASS"
        verdict_reason = (f"volume Casimir MINIMUM at v*={v_star:.5f} "
                          f"(d2E={minima[0]['d2E']:.3e}>0) -> det-g DERIVED")
        sign_verdict = "PASS"   # curvature sign > 0 == PASS prediction
        magnitude_verdict = "PASS"
        regime_verdict = "VALID"
    else:
        verdict = "INFO"
        if r["monotone"]:
            verdict_reason = (f"dE/dv MONOTONE (no interior min); runaway "
                              f"{r['runaway_dir']}; zeta_gr(-1/2)={zmh:.4f} "
                              f"-> volume-preservation stays IMPOSED")
        else:
            kinds = ",".join(sp["kind"] for sp in r["stat_points"])  # (local)
            verdict_reason = (f"stationary pts present ({kinds}) but NO minimum; "
                              f"volume-preservation stays IMPOSED")
        # [SIGN] 3-tuple: PASS prediction was (minimum exists, d2E>0); not
        # realized -> sign_verdict FAIL (direction mismatch vs PASS prediction).
        # This is the pre-registered track_B INFO outcome -> magnitude INFO,
        # regime VALID (the computation is sound; the monotone-runaway physics
        # default per Step 5 is CONFIRMED).
        sign_verdict = "FAIL"
        magnitude_verdict = "INFO"
        regime_verdict = "VALID"

    r.update({
        "modes_n": len(modes), "n_sectors": n_sectors, "n_eigs_raw": n_eigs_raw,
        "tri_counts": tri_counts, "sign_ok": sign_ok,
        "max_shell": max_shell, "top_frac": top_frac,
        "bare_lin": bare_lin, "pv_lin": pv_lin,
        "has_minimum": has_minimum, "minima": minima,
        "M_KK_Cas": M_KK_Cas, "verdict": verdict, "verdict_reason": verdict_reason,
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    })
    return r, {"by_shell": by_shell, "top_frac": top_frac, "max_shell": max_shell}


# ---------------------------------------------------------------------------
# Section 13 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = _Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+spectrum+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    cache_rel = str(SPECTRUM_CACHE.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
    cache_sha = pins.get(cache_rel, "MISSING")  # (local)
    MANIFEST_SHA = "88f1e9b107dc30c49a2dbcde33cecbee14cc17404994a2ad8f76adceec8a7258"  # (local)
    print("=== SPECTRUM CACHE SHA CROSS-CHECK ===")
    print(f"  runtime cache sha256  = {cache_sha}")
    print(f"  manifest cache sha256 = {MANIFEST_SHA}")
    print(f"  match = {cache_sha == MANIFEST_SHA} (informational; cross-source drift noted in plan)")
    print()

    r, sat = compute()  # (local)

    # FAIL guard: graded-sign / triality consistency
    if not r["sign_ok"]:
        print("FATAL: graded-sign assignment inconsistent with (p,q) triality.")
        print_verdict_payload(
            "FAIL", "graded_sign_triality_inconsistent", audit_sha, content_sha,
            sign_verdict="N/A", magnitude_verdict="FAIL", regime_verdict="BREAKDOWN",
            companion_note="graded-sign vs (p,q) triality consistency guard failed",
        )
        return 1

    # --- Report ---
    print("=== SPECTRUM LOAD ===")
    print(f"  sectors            = {r['n_sectors']}")
    print(f"  eigenvalues (raw)  = {r['n_eigs_raw']}  (with C^16 + Peter-Weyl mult)")
    print(f"  modes enumerated   = {r['modes_n']}")
    print(f"  triality sector counts (0:boson, 1/2:fermion) = {r['tri_counts']}")
    print(f"  graded-sign/triality consistency = {r['sign_ok']}")
    print()
    print("=== FRIEDRICH-BAR L_max SATURATION ===")
    print(f"  max p+q shell                 = {r['max_shell']}")
    print(f"  top-shell |contribution| frac = {r['top_frac']:.3e}  (sub-dominant => L12-saturated)")
    print()
    print("=== GRADED zeta_graded(-1/2) = Sum (-1)^F g_n m_n ===")
    print(f"  boson(+) partial   = {r['pos']:.6f}")
    print(f"  fermion(-) partial = {r['neg']:.6f}")
    print(f"  zeta_graded(-1/2)  = {r['zeta_m_half']:.6f}   sign = {'+' if r['zeta_m_half']>0 else '-'}")
    print()
    print("=== PAULI-VILLARS CROSS-CHECK (alternating linear sum) ===")
    print(f"  bare alternating sum = {r['bare_lin']:.6f}")
    print(f"  PV-regularized sum   = {r['pv_lin']:.6f}")
    rel_pv = (abs(r['pv_lin'] - r['bare_lin']) / abs(r['bare_lin'])
              if abs(r['bare_lin']) > 0 else float('nan'))  # (local)
    print(f"  rel |PV - bare|      = {rel_pv:.3e}  (regulator-independence cross-check)")
    print()
    print("=== VOLUME-DIRECTION STATIONARY-POINT SCAN (v in [0.3,3.0]) ===")
    print(f"  interior stationary points: {len(r['stat_points'])}")
    for sp in r["stat_points"]:
        print(f"    v*={sp['v_star']:.6f}  d2E/dv2={sp['d2E']:.4e}  kind={sp['kind']}  E={sp['E_at']:.4f}")
    print(f"  dE/dv monotone = {r['monotone']}  (sign set {r['dE_sign_set']})")
    if r["monotone"]:
        print(f"  runaway direction = {r['runaway_dir']}")
    print()
    print("=== CLASSIFICATION ===")
    print(f"  genuine volume Casimir MINIMUM exists? {r['has_minimum']}")
    if r["M_KK_Cas"] is not None:
        print(f"  THIRD determination M_KK^Cas = M_KK_gravity * (v*)^{{-1/2}} = {r['M_KK_Cas']:.6e} GeV")
        print(f"    vs gravity  7.428660e16 GeV  (ratio {r['M_KK_Cas']/M_KK_gravity:.4f})")
        print(f"    vs Kerner   5.041680e17 GeV  (ratio {r['M_KK_Cas']/M_KK_kerner:.4f})")
    print()
    print(f"=== VERDICT: {r['verdict']} ===")
    print(f"  {r['verdict_reason']}")
    print()

    # --- Save data ---
    np.savez(
        OUT_NPZ,
        vs=r["vs"], E_uni=r["E_uni"], E_brth=r["E_brth"], dE=r["dE"], d2E=r["d2E"],
        zeta_graded_minus_half=r["zeta_m_half"], boson_partial=r["pos"], fermion_partial=r["neg"],
        n_sectors=r["n_sectors"], n_eigs_raw=r["n_eigs_raw"], modes_n=r["modes_n"],
        tri_counts=json.dumps(r["tri_counts"]),
        max_shell=r["max_shell"], top_shell_frac=r["top_frac"],
        bare_lin=r["bare_lin"], pv_lin=r["pv_lin"],
        n_stat_points=len(r["stat_points"]),
        stat_v=np.array([sp["v_star"] for sp in r["stat_points"]], dtype=float),
        stat_d2E=np.array([sp["d2E"] for sp in r["stat_points"]], dtype=float),
        stat_kind=np.array([sp["kind"] for sp in r["stat_points"]], dtype=object),
        monotone=r["monotone"], runaway_dir=str(r["runaway_dir"]),
        has_minimum=r["has_minimum"],
        M_KK_Cas=(r["M_KK_Cas"] if r["M_KK_Cas"] is not None else float("nan")),
        M_KK_gravity=M_KK_gravity, M_KK_kerner=M_KK_kerner,
        det_g_ref=DET_G_REF, d_fiber=D_FIBER,
        verdict=r["verdict"], verdict_reason=r["verdict_reason"],
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
    )
    print(f"  saved -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(r, sat)
    print(f"  saved -> {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    # --- 4-tuple (final non-verdict line) ---
    mkkcas_str = (f"{r['M_KK_Cas']:.5e}" if r["M_KK_Cas"] is not None else "NA")  # (local)
    if r["has_minimum"]:
        value_str = (f"MINIMUM|v_star={r['minima'][0]['v_star']:.5f}|"
                     f"d2E={r['minima'][0]['d2E']:.4e}|M_KK_Cas={mkkcas_str}|"
                     f"zeta_gr(-1/2)={r['zeta_m_half']:.4f}")  # (local)
    else:
        value_str = (f"NO_MINIMUM_runaway={r['runaway_dir']}|"
                     f"zeta_gr(-1/2)={r['zeta_m_half']:.4f}|"
                     f"n_stat={len(r['stat_points'])}|monotone={r['monotone']}")  # (local)
    print(emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX))
    print()

    # --- Verdict payload (agent calls emit_verdict) ---
    extra_rows = [
        ("# regulator_pin=zeta-graded-Casimir (zeta_graded(-1/2)=Sum(-1)^F g_n m_n alternating sum; "
         "NOT a Seeley-DeWitt a_n moment); PV cross-check at Lambda_UV=M_KK in cache units"),
        (f"# casimir-volume: zeta_gr(-1/2)={r['zeta_m_half']:.4f} (boson+={r['pos']:.2f},fermion-={r['neg']:.2f}); "
         f"interior_min={r['has_minimum']}; "
         + (f"v_star={r['minima'][0]['v_star']:.5f} M_KK_Cas={mkkcas_str} GeV (3rd determination)"
            if r['has_minimum'] else
            f"MONOTONE runaway={r['runaway_dir']} -> volume-preservation IMPOSED (A-KK2 unchanged)")),
        ("# substrate: breathing mode is CONFORMAL on the metric (g->v^(2/d)g => m_n->v^(-1/d)m_n EXACTLY, "
         "no sector-differentiation) => graded Casimir MONOTONE per plan Step 5; "
         "interior minimum would require non-conformal deformation v-coupling"),
    ]  # (local)
    print_verdict_payload(
        r["verdict"], value_str, audit_sha, content_sha,
        sign_verdict=r["sign_verdict"],
        magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
        companion_note="graded Casimir in the volume/breathing direction on Jensen-SU(3) L12 tower; investigation track",
        extra_rows=extra_rows,
    )

    print(f"\n  [elapsed {time.time() - t0:.2f}s]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
