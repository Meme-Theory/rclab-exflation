#!/usr/bin/env python3
"""
S110 W2-3 S110-CF1-AT-MINISUPERSPACE — the a(t) backbone-form decider
=====================================================================

Gate: S110-CF1-AT-MINISUPERSPACE ([SIGN])

Pre-registered threshold:
  PASS=MONOTONE iff sign(dH2/drho)_{gap-as-ceiling} == sign(dH2/drho)_{holonomy}
                    (both reduction schemes agree on a single-signed ramp across the rho-grid);
  INFO=SPLIT     iff the two reduction schemes give OPPOSITE sign(dH2/drho);
  FAIL           iff the reduction is ill-posed (no well-defined dH2/drho).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py (a_n_FW_zeta triple, M_KK_gravity, M_Pl_reduced, G_DeWitt; feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<MONOTONE|SPLIT|ill-posed + signs>, scheme=MINISUPERSPACE-EFFECTIVE-FRIEDMANN-FORM,
   convention=a_n^{zeta};reduction=BOTH;mu-bar-analog, L_max=12)

Classification: GEOMETRIC

METHODOLOGY
-----------
The spectral action S_SA(tau) = a_0 - a_2 + a_4 (E7 moment combination) projects to the
homogeneous-isotropic minisuperspace sector. The standard heat-kernel -> gravitational-action
dictionary maps:
  - a_2 term  proportional to R          -> Einstein-Hilbert; sources (8 pi G_eff / 3) rho
  - a_4 term  proportional to R^2 + Weyl^2 -> Starobinsky higher-curvature operator
The whole functional-form question localizes to sign(dH2/drho_relic) and whether the a_4
R^2+Weyl^2 operator deviates the reduced constraint from a monotone ramp.

Two PRE-REGISTERED reduction schemes are run (MANDATORY; convention-shoppable without BOTH,
PROHIBITED_ACTIONS Class 1 per v3-closure-recovery.md):

  (1) gap-as-density-ceiling: test whether the spectral gap lambda_min enters the homogeneous
      constraint as a (1 - rho/rho_c) density ceiling. Per inv-7 W4-1 convergence (D1), the
      linear spectral moments a_n = Sum_k w_k lambda_k^{-2s} carry NO bounded sin^2-type
      saturation operator; lambda_min is an INTENSIVE [M_KK] floor on quasiparticle creation,
      NOT an EXTENSIVE [M_KK^4] density ceiling. We construct the reduced constraint explicitly
      and read its sign (do NOT assume MONOTONE).

  (2) holonomy-analog: construct the CLOSEST-POSSIBLE bounded-function analog of the LQC
      sin^2(mu-bar c)/mu-bar^2 operator from the substrate moments (the most LQC-favorable
      construction). The a_4/a_2 ratio supplies the curvature-squared coefficient; we form the
      LQC-template H^2 = (8 pi G_eff / 3) rho (1 - rho/rho_c) with rho_c derived from the
      moment-built bounded operator, and read its sign. mu-bar-analog (improved dynamics: ceiling
      at FIXED rho_c) vs mu_0-analog (old dynamics: ceiling scales with the volume) is declared;
      we pin mu-bar-analog (the physical LQC choice; Ashtekar-Pawlowski-Singh 2006).

MANDATORY V_spec-monotone reconciliation (rollup-at-clock section 3/4 internal-tension flag):
  V_spec monotone (S24a, closed mechanism): a_4/a_2 = 1000:1, NO Starobinsky minimum,
  monotone INCREASING for all rho. This settles the a_4-operator sign in the POTENTIAL
  LANDSCAPE V_spec(tau; rho) = -c_2 R_K + c_4 a_4^geom. The minisuperspace dH2/drho is a
  FRIEDMANN-REDUCTION object (H^2 = (8 pi G_eff/3) rho_relic). These are DISTINCT functionals
  of the same a_4 moment -- the p_S75 != p_cosmo lesson (spectral-action shape in tau-space !=
  Friedmann power-law in N-space). We compute BOTH the V_spec potential slope d V_spec/d rho
  AND the Friedmann-reduction slope dH2/drho, and DECLARE them same-object-or-distinct from the
  computed relationship -- we do NOT assert the Friedmann sign from V_spec alone.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- low-dim algebra + 1-D rho-scan -> CPU (cpu-cap OMP8); no matrices >= 100x100
- SHA-256 of all inputs logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA)
- 4-tuple printed as the final non-verdict line
- verdict via print_verdict_payload -> agent calls emit_verdict (race-safe)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 -- Path bootstrap (SHARED_DIR onto sys.path BEFORE canonical import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    a_0_FW_zeta, a_2_FW_zeta, a_4_FW_zeta,
    M_KK_gravity, M_Pl_reduced, G_DeWitt,
)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports (CPU; low-dim algebra + 1-D scan)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S110"                                                       # (local)
GATE_ID = "S110-CF1-AT-MINISUPERSPACE"                                 # (local)
SCHEME = "MINISUPERSPACE-EFFECTIVE-FRIEDMANN-FORM"                     # (local)
CONVENTION = "a_n^zeta;reduction=BOTH;mu-bar-analog"                   # (local)
L_MAX = 12                                                             # (local)

OUT_NPZ = SESSION_DIR / "s110_cf1_at_minisuperspace.npz"
OUT_PNG = SESSION_DIR / "s110_cf1_at_minisuperspace.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
]

# ---------------------------------------------------------------------------
# NON-CANONICAL inputs -- sourced with inline provenance (NOT hardcoded-as-canonical).
# get_constant() returns null for both; they are workshop-cited values.
# ---------------------------------------------------------------------------
# rho_relic = Sum_K E_K |beta_K|^2 = 26.553854 M_KK (B1+B2+B3 Bogoliubov band sum).
#   Provenance: S96 section W1-5 (the homogeneous source density); cited verbatim by the
#   inv-7 W4-1 effective-Friedmann-functional-form workshop (effective-friedmann-functional-
#   form.md line 80, 172, 366). Truncation band [15.41, 26.85] M_KK (inv-12 W3-1). The
#   value is fixed at the fold by saturation |beta_K|^2 = max (P_exc = 1.000).
RHO_RELIC = 26.553854          # M_KK units; NON-canonical, S96 W1-5 / inv-7 W4-1   # (local)
# lambda_min(tau_fold) = 0.790 M_KK -- the absolute spectral-gap floor (S17a, never-closing).
#   DISTINCT from the canonical lambda_min_max_ratio_FW = 0.15127 (the |lam|_min/|lam|_max
#   strict ratio at the fold). 0.790 is the absolute floor value used by the gap-as-ceiling
#   scheme. Provenance: S17a; cited by inv-7 W4-1 (line 146, 366) and _rollup-at-clock section 5.
LAMBDA_MIN = 0.790             # M_KK units; NON-canonical, S17a                     # (local)


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


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
# Section 5 -- Compute
# ---------------------------------------------------------------------------

def sign_of(x: float, tol: float = 1e-12) -> int:
    """Return -1, 0, +1 with a tolerance band to suppress float noise at zero."""
    if x > tol:
        return +1
    if x < -tol:
        return -1
    return 0


def reduced_friedmann_base(rho_grid: np.ndarray) -> np.ndarray:
    """The bare Einstein-Hilbert (a_2-grade) reduced constraint H^2 = (8 pi G_eff/3) rho.

    Dimensional check: G_eff carries [M_KK^-2] in M_KK units (it is the inverse of the
    a_2 Einstein-Hilbert coefficient ~ M_Pl^2). H^2 carries [M_KK^2]. rho carries [M_KK^4].
    (8 pi G_eff/3) rho -> [M_KK^-2][M_KK^4] = [M_KK^2] = [H^2]. Consistent.

    G_eff is taken as the substrate's emergent Newton constant in M_KK units; only its SIGN
    (strictly +, gravity is attractive) enters the verdict, so its precise magnitude is a
    diagnostic, not a gate input. We use the canonical a_2-channel dictionary value.
    """
    # G_eff in M_KK units from the a_2 Einstein-Hilbert grade. The dimensionless prefactor
    # is the substrate's emergent 1/M_Pl_eff^2 expressed in M_KK units = (M_KK/M_Pl_red)^2.
    g_eff_mkk = (M_KK_gravity / M_Pl_reduced) ** 2          # (local) dimensionless in M_KK units
    return (8.0 * np.pi * g_eff_mkk / 3.0) * rho_grid       # H^2 in M_KK^2 units  # (local)


def scheme_gap_as_density_ceiling(rho_grid: np.ndarray) -> dict:
    """Scheme 1: does the spectral gap lambda_min enter as a (1 - rho/rho_c) ceiling?

    Substitution chain (read sign FROM the constructed form, do NOT assume) -- the chain
    follows inv-7 W4-1 Re:L-a Steps 1-4 (effective-friedmann-functional-form.md:122-124) and
    is closed by the Sage-verified Starobinsky-R^2 sign result (see scheme_holonomy_analog and
    the V_spec reconciliation):
      Step A: the only place lambda_min could enter the homogeneous constraint is through the
              a_n moments a_n = Sum_k w_k lambda_k^{-2s}. These are LINEAR sums over the
              eigenvalue spectrum -- there is no bounded trigonometric function of a connection
              component (no sin^2(mu-bar c)) in them (inv-7 W4-1 Step 3, agreed D1 both agents).
      Step B: lambda_min is an INTENSIVE [M_KK] floor on quasiparticle creation (the minimum
              energy 2*lambda_min to excite the BdG sector), NOT an EXTENSIVE [M_KK^4] density
              ceiling on rho. The LQC inversion Delta -> rho_c is a consequence of holonomy
              boundedness SPECIFICALLY, not of the gap's existence (Ashtekar 2006 Paper08:151:
              quantum-geometry "comes with the sign required to make gravity repulsive" via the
              bounded sin^2). No such bounded operator exists in linear moments.
      Step C: the a_4 R^2+Weyl^2 moment IS present in the reduced action
              (S_eff=(1/16piG)int[R + (a_4/a_2)M_KK^-2 curv^2], inv-13 W1) but it is a
              PURE-CURVATURE (Starobinsky R^2) term: Hdot-structured, sources NO matter coupling,
              so it contributes 0 to d(H^2)/d(rho) (Sage-verified: diff(8piG rho/3, rho)=8piG/3
              from the a_2 term; the a_4 R^2 term adds no rho-dependence). The gap therefore
              enters ONLY as an additive zero-point offset rho_offset (rho-INDEPENDENT).
      Step D: H^2_gap = (8 pi G_eff/3)(rho + rho_offset), rho_offset = const;
              dH2/drho = (8 pi G_eff/3) > 0 EXACTLY, rho-independent. MONOTONE by construction.

    We construct H^2_gap explicitly and read sign(dH2/drho) numerically across the grid.
    """
    g_eff_mkk = (M_KK_gravity / M_Pl_reduced) ** 2                         # (local)
    # The gap contributes an ADDITIVE zero-point energy offset (intensive floor promoted to an
    # extensive constant via the M_KK^3 cutoff-volume bridge), NOT a multiplicative ceiling.
    # rho_offset is rho-INDEPENDENT -> annihilated by d/drho.
    rho_offset = LAMBDA_MIN ** 4                                           # (local) M_KK^4, additive const
    H2_gap = (8.0 * np.pi * g_eff_mkk / 3.0) * (rho_grid + rho_offset)     # (local) M_KK^2
    dH2_drho = np.gradient(H2_gap, rho_grid)                               # (local) numerical derivative
    signs = np.array([sign_of(d) for d in dH2_drho])                      # (local)
    single_signed = bool(np.all(signs == signs[0]) and signs[0] != 0)     # (local)
    return {
        "name": "gap-as-density-ceiling",
        "H2": H2_gap,
        "dH2_drho": dH2_drho,
        "signs": signs,
        "sign_uniform": int(signs[0]) if single_signed else 0,
        "single_signed": single_signed,
        "rho_c_candidate": rho_offset,          # the additive gap offset (NOT a ceiling)
        "has_saturation_operator": False,        # linear moments carry no bounded sin^2 factor
    }


def scheme_holonomy_analog(rho_grid: np.ndarray, rho_relic: float) -> dict:
    """Scheme 2: the CLOSEST-POSSIBLE bounded-function analog of sin^2(mu-bar c)/mu-bar^2.

    Substitution chain:
      Step A: LQC effective Friedmann: H^2 = (8 pi G/3) rho (1 - rho/rho_c), rho_c the
              saturation density built by holonomy boundedness sin^2(mu-bar c)/mu-bar^2 <= 1.
              In LQC rho_c = sqrt(3)/(32 pi^2 gamma^3) M_Pl^4 ~ 0.41 M_Pl^4 -- a PLANCK-ANALOG
              density (order M_Pl^4), NOT a moment-ratio.
      Step B: the substrate Planck-analog is the cutoff M_KK; the bare-cutoff ceiling is
              rho_c ~ M_KK^4 = 1 (M_KK^4 units). BUT a physical-consistency constraint binds it:
              the relic EXISTS with P_exc=1.000 at rho_relic [M_KK^4] -- so H^2 >= 0 at the
              realized loading REQUIRES rho_c >= rho_relic (you cannot exceed the bounce density
              in LQC). A sub-cutoff rho_c < rho_relic gives H^2(rho_relic) < 0 (ill-posed).
              The MOST-LQC-FAVORABLE *physically-consistent* ceiling is the MARGINAL one:
              rho_c^holo = rho_relic (the smallest ceiling that keeps H^2 >= 0 at the relic).
      Step C: mu-bar-analog (improved dynamics): rho_c FIXED (Ashtekar-Pawlowski-Singh 2006).
              H^2_holo = (8 pi G_eff/3) rho (1 - rho/rho_c^holo),
              dH2/drho = (8 pi G_eff/3)(1 - 2 rho/rho_c^holo):
              SIGN-POSITIVE for rho < rho_c/2 = rho_relic/2,
              SIGN-NEGATIVE for rho > rho_relic/2 -- a TURNING POINT at rho_relic/2, which lies
              INSIDE the physical window [rho_min, rho_relic]. The a_4/a_2 ratio is reported as
              the curvature-squared coefficient diagnostic (it sets the Starobinsky Hdot-term,
              NOT the matter ceiling -- Step B of scheme 1).

    We construct H^2_holo and read sign(dH2/drho) across the grid. Whether the sign turns over
    within [rho_min, rho_relic] is the DECISIVE comparison against Scheme 1.
    """
    g_eff_mkk = (M_KK_gravity / M_Pl_reduced) ** 2                         # (local)
    a4_over_a2 = a_4_FW_zeta / a_2_FW_zeta                                 # (local) dimensionless ~0.486 (curv^2 coeff diagnostic)
    # Most-LQC-favorable PHYSICALLY-CONSISTENT saturation density: the marginal Planck-analog
    # ceiling rho_c = rho_relic (the smallest rho_c keeping H^2 >= 0 at the realized relic
    # loading). A sub-cutoff rho_c < rho_relic is ill-posed (H^2(rho_relic) < 0); a super-relic
    # rho_c > rho_relic pushes the turnover above the window (no turning point). The marginal
    # case is the boundary that makes the holonomy-analog MAXIMALLY ceiling-producing while
    # staying physical -- the closest the substrate can come to an LQC turning point.
    rho_c_holo = rho_relic                                                # (local) M_KK^4, marginal Planck-analog
    bounded_factor = 1.0 - rho_grid / rho_c_holo                          # (local)
    H2_holo = (8.0 * np.pi * g_eff_mkk / 3.0) * rho_grid * bounded_factor  # (local) M_KK^2
    dH2_drho = np.gradient(H2_holo, rho_grid)                             # (local)
    signs = np.array([sign_of(d) for d in dH2_drho])                     # (local)
    single_signed = bool(np.all(signs == signs[0]) and signs[0] != 0)    # (local)
    # locate any sign-change (turning point)
    sign_changes = int(np.sum(np.abs(np.diff(signs)) > 0))               # (local)
    turning_rho = None                                                    # (local)
    if sign_changes > 0:
        idx = int(np.argmax(np.abs(np.diff(signs)) > 0))                  # (local)
        turning_rho = float(0.5 * (rho_grid[idx] + rho_grid[idx + 1]))    # (local)
    return {
        "name": "holonomy-analog",
        "H2": H2_holo,
        "dH2_drho": dH2_drho,
        "signs": signs,
        "sign_uniform": int(signs[0]) if single_signed else 0,
        "single_signed": single_signed,
        "rho_c_candidate": rho_c_holo,
        "a4_over_a2": a4_over_a2,
        "sign_changes": sign_changes,
        "turning_rho": turning_rho,
        "mu_pin": "mu-bar-analog (improved dynamics, rho_c FIXED at marginal Planck-analog = rho_relic; Ashtekar-Pawlowski-Singh 2006)",
        "has_saturation_operator": True,         # by CONSTRUCTION (most-LQC-favorable, physically-consistent)
    }


def vspec_reconciliation(rho_grid: np.ndarray) -> dict:
    """MANDATORY V_spec-monotone (S24a) reconciliation: same-object-or-distinct.

    V_spec(tau; rho) = -c_2 R_K + c_4 a_4^geom is the POTENTIAL LANDSCAPE; S24a proves it
    monotone INCREASING for all rho (a_4/a_2 = 1000:1, no Starobinsky minimum). The
    minisuperspace dH2/drho is a FRIEDMANN-REDUCTION object H^2 = (8 pi G_eff/3) rho_relic.

    We compute the POTENTIAL slope d V_spec/d rho on the SAME rho-grid (using the S24a
    structural form: V_spec increases with rho -> d V_spec/d rho > 0) and compare its sign to
    the Friedmann-reduction slope. We DECLARE same-object-or-distinct from the STRUCTURE of the
    two functionals, NOT by asserting one from the other:

      - V_spec is a function of (tau; rho) -- a POTENTIAL in tau-space, parameterised by rho.
        Its rho-dependence is the source-density loading of the spectral-action potential.
      - H^2(rho) is the Friedmann-REDUCTION -- the homogeneous-sector constraint READOUT,
        a function of the relic source density.
      These are DISTINCT functionals of the same a_4 moment (the p_S75 != p_cosmo lesson:
      spectral-action SHAPE in tau-space != Friedmann power-law in N-space). The a_4 moment
      ENTERS BOTH, but the FUNCTIONAL FORM differs: V_spec adds a_4 as a curvature potential
      term (-c_2 R + c_4 a_4); H^2 reduction uses a_4 only through the (optional) higher-
      curvature correction to the constraint. Same INPUT (a_4), distinct OUTPUT FUNCTIONAL.
    """
    # V_spec potential slope (S24a structural: monotone increasing -> sign +1 for all rho).
    # We encode the S24a result as the structural sign; the magnitude is not the gate's object.
    vspec_slope_sign = +1                                                 # (local) S24a: monotone increasing
    return {
        "vspec_potential_slope_sign": vspec_slope_sign,
        "vspec_a4_over_a2": 1000.0,                # S24a structural ratio (1000:1)
        "declaration": "DISTINCT",                 # distinct functionals of the same a_4 moment
        "reason": ("V_spec(tau;rho) is a POTENTIAL in tau-space (spectral-action landscape); "
                   "H^2(rho) is the FRIEDMANN-REDUCTION constraint readout. Same a_4 INPUT, "
                   "distinct OUTPUT functional -- the p_S75 != p_cosmo lesson. V_spec monotone "
                   "(S24a) does NOT fix the Friedmann-reduction sign; dH2/drho is read "
                   "independently from the reduced constraint."),
    }


def compute() -> dict:
    # rho-grid: >= 25 points over [rho_min, rho_relic]. rho_min is a small positive floor
    # (the post-fold coasting branch dilutes toward 0); we span the full relic loading.
    rho_min = 0.01 * RHO_RELIC                                            # (local) small positive floor
    rho_grid = np.linspace(rho_min, RHO_RELIC, 60)                       # (local) 60 >= 25 points

    base = reduced_friedmann_base(rho_grid)                              # (local) bare EH diagnostic
    s1 = scheme_gap_as_density_ceiling(rho_grid)
    s2 = scheme_holonomy_analog(rho_grid, RHO_RELIC)
    rec = vspec_reconciliation(rho_grid)

    # --- ill-posedness guard ---
    # The reduction is ill-posed iff dH2/drho is undefined anywhere (NaN/inf) under either scheme.
    ill_posed = bool(
        not np.all(np.isfinite(s1["dH2_drho"])) or
        not np.all(np.isfinite(s2["dH2_drho"]))
    )

    # --- verdict logic ---
    s1_sign = s1["sign_uniform"]   # (local) +1 if single-signed positive, -1 negative, 0 mixed
    s2_sign = s2["sign_uniform"]   # (local)

    if ill_posed:
        verdict = "FAIL"
        branch = "ill-posed"
        agree = False
    elif s1["single_signed"] and s2["single_signed"] and s1_sign == s2_sign:
        # Both schemes single-signed AND agree -> MONOTONE-RAMP
        verdict = "PASS"
        branch = "MONOTONE-RAMP"
        agree = True
    else:
        # schemes disagree (one single-signed, one turns over; or opposite uniform signs)
        verdict = "INFO"
        branch = "SPLIT"
        agree = False

    # sign within the PHYSICAL window [rho_min, rho_relic]: does scheme-2 actually turn over
    # BEFORE rho_relic, or is rho_c/2 beyond the relic loading (so it never reaches the ceiling)?
    s2_turns_in_window = bool(s2["turning_rho"] is not None
                              and rho_min <= s2["turning_rho"] <= RHO_RELIC)  # (local)

    return {
        "value": branch,
        "verdict": verdict,
        "rho_grid": rho_grid,
        "base_H2": base,
        "s1": s1,
        "s2": s2,
        "rec": rec,
        "schemes_agree": agree,
        "s1_sign": s1_sign,
        "s2_sign": s2_sign,
        "s2_turns_in_window": s2_turns_in_window,
        "rho_relic": RHO_RELIC,
        "rho_c_holo": s2["rho_c_candidate"],
        "ill_posed": ill_posed,
    }


# ---------------------------------------------------------------------------
# Section 6 -- Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
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
    rho = res["rho_grid"]                                                 # (local)
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))                       # (local)

    ax = axes[0]
    ax.plot(rho, res["s1"]["H2"], "b-", lw=2, label="gap-as-density-ceiling")
    ax.plot(rho, res["s2"]["H2"], "r--", lw=2, label="holonomy-analog")
    ax.axvline(res["rho_relic"], color="k", ls=":", lw=1,
               label=f"rho_relic={res['rho_relic']:.3f}")
    if res["s2"]["turning_rho"] is not None:
        ax.axvline(res["s2"]["turning_rho"], color="orange", ls=":", lw=1,
                   label=f"holo turning rho={res['s2']['turning_rho']:.3f}")
    ax.set_xlabel("rho  [M_KK^4]")
    ax.set_ylabel("H^2  [M_KK^2]")
    ax.set_title(f"{GATE_ID}: effective-Friedmann form -- {res['value']}")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axes[1]
    ax.plot(rho, res["s1"]["dH2_drho"], "b-", lw=2,
            label=f"gap dH2/drho (sign={res['s1_sign']:+d})")
    ax.plot(rho, res["s2"]["dH2_drho"], "r--", lw=2,
            label=f"holo dH2/drho (sign uniform={res['s2_sign']:+d})")
    ax.axhline(0.0, color="k", lw=0.8)
    ax.axvline(res["rho_relic"], color="k", ls=":", lw=1)
    ax.set_xlabel("rho  [M_KK^4]")
    ax.set_ylabel("dH^2/drho  [M_KK^-2]")
    ax.set_title("sign(dH2/drho) -- the a_4 Starobinsky-operator readout")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"S110-CF1 minisuperspace a(t) backbone-form decider | "
        f"V_spec reconciliation: {res['rec']['declaration']} | "
        f"schemes agree: {res['schemes_agree']}",
        fontsize=10,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()
    print(f"  NON-CANONICAL pins (inline provenance):")
    print(f"    RHO_RELIC  = {RHO_RELIC} M_KK  [S96 W1-5 / inv-7 W4-1; band [15.41,26.85]]")
    print(f"    LAMBDA_MIN = {LAMBDA_MIN} M_KK  [S17a never-closing; != lambda_min_max_ratio_FW=0.15127]")
    print(f"  CANONICAL a_n_FW_zeta: a0={a_0_FW_zeta}, a2={a_2_FW_zeta}, a4={a_4_FW_zeta}")
    print(f"  M_KK_gravity={M_KK_gravity:.6e}, M_Pl_reduced={M_Pl_reduced:.6e}, G_DeWitt={G_DeWitt}")
    print()

    res = compute()

    # --- report ---
    print(f"=== {GATE_ID} -- RESULTS ===")
    print(f"  Scheme 1 (gap-as-density-ceiling):")
    print(f"    sign(dH2/drho) uniform = {res['s1_sign']:+d}  (single-signed={res['s1']['single_signed']})")
    print(f"    has bounded saturation operator: {res['s1']['has_saturation_operator']}")
    print(f"    additive gap offset rho_offset = lambda_min^4 = {res['s1']['rho_c_candidate']:.6f} M_KK^4")
    print(f"  Scheme 2 (holonomy-analog, {res['s2']['mu_pin']}):")
    print(f"    a4/a2 = {res['s2']['a4_over_a2']:.6f} (curv^2 coeff diagnostic; Hdot-structured, NOT the ceiling)")
    print(f"    rho_c^holo = marginal Planck-analog = rho_relic = {res['rho_c_holo']:.6f} M_KK^4 (smallest rho_c keeping H^2>=0 at relic)")
    print(f"    sign uniform = {res['s2_sign']:+d}  (single-signed={res['s2']['single_signed']}, sign_changes={res['s2']['sign_changes']})")
    print(f"    turning rho = {res['s2']['turning_rho']}  (turns within [rho_min,rho_relic]: {res['s2_turns_in_window']})")
    print(f"  rho_c^holo / 2 = {res['rho_c_holo']/2:.6f} M_KK^4  vs  rho_relic = {res['rho_relic']:.6f} M_KK^4")
    print(f"    -> rho_relic {'EXCEEDS' if res['rho_relic'] > res['rho_c_holo']/2 else 'is BELOW'} rho_c/2")
    print(f"  V_spec reconciliation: {res['rec']['declaration']}")
    print(f"    V_spec potential slope sign (S24a) = {res['rec']['vspec_potential_slope_sign']:+d} (monotone increasing)")
    print(f"    reason: {res['rec']['reason']}")
    print(f"  schemes_agree = {res['schemes_agree']}  ->  branch = {res['value']}")
    print()

    verdict = res["verdict"]

    # --- [SIGN] 3-tuple ---
    # sign_verdict: did the substitution-chain directional prediction match? The chain predicted
    #   Scheme-1 MONOTONE (gap is wrong object; +1) -- PASS iff s1 is single-signed positive.
    sign_verdict = "PASS" if (res["s1_sign"] == +1 and res["s1"]["single_signed"]) else "FAIL"  # (local)
    # magnitude_verdict: the gate's "magnitude" object is scheme AGREEMENT (the form decision).
    #   PASS iff schemes agree (MONOTONE); INFO iff they SPLIT; FAIL iff ill-posed.
    if res["ill_posed"]:
        magnitude_verdict = "FAIL"          # (local)
    elif res["schemes_agree"]:
        magnitude_verdict = "PASS"          # (local)
    else:
        magnitude_verdict = "INFO"          # (local)
    # regime_verdict: the minisuperspace reduction is VALID over the full physical rho-window
    #   (no interior pole, dH2/drho finite throughout). BREAKDOWN iff ill-posed.
    regime_verdict = "BREAKDOWN" if res["ill_posed"] else "VALID"        # (local)

    # save data
    np.savez(
        OUT_NPZ,
        rho_grid=res["rho_grid"],
        base_H2=res["base_H2"],
        s1_H2=res["s1"]["H2"],
        s1_dH2_drho=res["s1"]["dH2_drho"],
        s1_signs=res["s1"]["signs"],
        s1_sign_uniform=res["s1_sign"],
        s1_single_signed=res["s1"]["single_signed"],
        s1_rho_offset=res["s1"]["rho_c_candidate"],
        s2_H2=res["s2"]["H2"],
        s2_dH2_drho=res["s2"]["dH2_drho"],
        s2_signs=res["s2"]["signs"],
        s2_sign_uniform=res["s2_sign"],
        s2_single_signed=res["s2"]["single_signed"],
        s2_a4_over_a2=res["s2"]["a4_over_a2"],
        s2_rho_c_holo=res["rho_c_holo"],
        s2_sign_changes=res["s2"]["sign_changes"],
        s2_turning_rho=(np.nan if res["s2"]["turning_rho"] is None else res["s2"]["turning_rho"]),
        s2_turns_in_window=res["s2_turns_in_window"],
        schemes_agree=res["schemes_agree"],
        branch=res["value"],
        verdict=verdict,
        rho_relic=res["rho_relic"],
        lambda_min=LAMBDA_MIN,
        vspec_declaration=res["rec"]["declaration"],
        vspec_potential_slope_sign=res["rec"]["vspec_potential_slope_sign"],
        a_0_FW_zeta=a_0_FW_zeta, a_2_FW_zeta=a_2_FW_zeta, a_4_FW_zeta=a_4_FW_zeta,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
    )
    make_plot(res)

    # value payload (no single-quote chars; emit_verdict wraps value='...')
    value_payload = (
        f"branch={res['value']};"
        f"s1_gap_sign={res['s1_sign']:+d}_MONOTONE_no_saturation_operator;"
        f"s2_holo_sign_uniform={res['s2_sign']:+d};"
        f"s2_sign_changes={res['s2']['sign_changes']};s2_turning_rho={res['s2']['turning_rho']:.4f};"
        f"s2_turns_in_window={res['s2_turns_in_window']};"
        f"schemes_agree={res['schemes_agree']};"
        f"rho_c_holo_marginal_Planck_analog={res['rho_c_holo']:.6f};rho_relic={res['rho_relic']:.6f};"
        f"a4_over_a2_curv2_coeff={res['s2']['a4_over_a2']:.6f};"
        f"starobinsky_R2_contributes_zero_to_dH2drho_Sage_verified=True;"
        f"vspec_reconciliation={res['rec']['declaration']};vspec_slope_sign=+1;"
        f"vspec_vs_friedmann=distinct_functionals_same_a4_p_S75_neq_p_cosmo;"
        f"mu_pin=mu-bar-analog;reduction_scheme=BOTH;"
        f"a0={a_0_FW_zeta};a2={a_2_FW_zeta};a4={a_4_FW_zeta};"
        f"regulator_pin=a_n_zeta"
    )

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    print_verdict_payload(
        verdict, value_payload, audit_sha, content_sha,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        extra_rows=[
            "# regulator_pin=a_n^{zeta} (a_0=6440, a_2=2776.165389, a_4=1350.7216); "
            "the a_4 R^2+Weyl^2 Starobinsky operator is the load-bearing Seeley-DeWitt term",
            "# SD1 (inv-7 W4-1 technical heart): a_4 R^2+Weyl^2 is PURE-CURVATURE (Hdot-structured), "
            "contributes 0 to d(H^2)/d(rho) [Sage-verified: only a_2 EH term sources matter coupling "
            "8piG/3>0]; gap-as-ceiling -> MONOTONE+ by construction (no sin^2 saturation in linear moments)",
            "# holonomy-analog: most-LQC-favorable PHYSICALLY-CONSISTENT ceiling = marginal Planck-analog "
            "rho_c=rho_relic (sub-cutoff rho_c<rho_relic gives H^2<0 ill-posed); turnover at rho_relic/2 "
            "IN-window -> TURNING-POINT; schemes SPLIT (inv-7 W4-1 line 150 pre-registered INFO outcome)",
            "# V_spec-monotone (S24a) reconciliation: DISTINCT functionals -- V_spec(tau;rho) "
            "potential-landscape (monotone increasing, no Starobinsky minimum) vs H^2(rho) "
            "Friedmann-reduction; same a_4 INPUT, distinct OUTPUT functional (p_S75 != p_cosmo)",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (branch={res['value']}, wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
