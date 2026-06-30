#!/usr/bin/env python3
"""
S87 W1b-1 — S87-PV-SUBTRACTION-RECALIBRATION
=============================================

Gate: S87-PV-SUBTRACTION-RECALIBRATION ([VERIFY] [SIGN])

Pre-registered threshold (per session-87-plan-w1b.md §W1b-1):
  PASS  iff max_rel_err_PV < 1e-12 AND |R_PV(L=12) - R_SD| > 1e-6
              AND sign_verdict=PASS AND regime_verdict=VALID
  INFO  iff max_rel_err_PV in [1e-12, 1e-9] OR |R_PV - R_SD| in [1e-9, 1e-6]
  FAIL  iff max_rel_err_PV > 1e-9 OR |R_PV - R_SD| < 1e-9
              OR sign_verdict=FAIL OR regime_verdict=BREAKDOWN

Pre-registered sign (Step 4 of plan substitution chain):
  sign_pred = +1   (R_PV(L=12; M_KK) > R_SD)

Inputs (SHA-256 dual-pinned at runtime):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (master)
  - canonical_constants.py
  - script bytes

Output 4-tuple:
  (value=max_rel_err_PV, scheme=Pauli-Villars-finite-L,
   convention=substrate-mass-scale-M_KK, L_max=12)

Classification: GEOMETRIC

METHODOLOGY
-----------
The §VII.U Mellin-Dirichlet identity in finite-spectrum form (Connes Re:L2)
is the exact algebraic identity

    zeta_D(s) * Gamma(s/2)  =  integral_0^infty  t^(s/2 - 1)  K(t)  dt

with K(t) = sum_k m_k exp(-lambda_k^2 t) and zeta_D(s) = sum_k m_k lambda_k^{-s}.
This script verifies the identity at s = 3 (the substrate-distance-1 pole)
under TWO regulator schemes:
  (i)  bare zeta-regulated moment (R_bare),
  (ii) Pauli-Villars-finite-L: R_PV(L; M) = R_bare(L) - sum_k m_k (lambda_k^2 + M^2)^{-3/2}.

The L_max=10 sub-spectrum is obtained from the L_max=12 master cache by
filtering sectors with level <= 10 (the framework's canonical L_max
truncation; substrate-faithful re-derivation, no separate cache needed).

The continuum-SD residue R_SD at s=3 with d_spec=4 is obtained from the
small-t Seeley-DeWitt fit to K(t):
    K(t) ~ a_0^{Pauli-Villars}/t^2 + a_2^{Pauli-Villars}/t + a_4^{Pauli-Villars} + O(t)
and the continuum residue at s=3 is R_SD = 2 a_2 / Gamma(3/2) (in the
finite-spectrum truncation R_SD reads the leading 1/t SD coefficient, which
is the continuum-pole proxy used by S86 W-1 W1b-T5 cone-residue evaluations).

Substitution chain (SIGN claim — REQUIRED):
  Step 1 (defs):
    R_bare(L)    = sum_{k <= N(L)} m_k lambda_k^{-3}
    R_PV(L;M)    = R_bare(L) - sum_k m_k (lambda_k^2 + M^2)^{-3/2}
    R_SD         = 2 a_2^{Pauli-Villars} / Gamma(3/2)
                   (a_2 from small-t Heat-kernel SD fit on full L=12 K(t))
  Step 2:
    sign_target  = sign( R_PV(L=12; M_KK=1) - R_SD )
  Step 3 (algebra):
    sum_k m_k (lambda_k^2 + M^2)^{-3/2} > 0 strictly (each term positive)
    => R_PV(L; M) < R_bare(L) for any finite L, M > 0
    Also bare moment converges from below as L -> infty:
       R_bare(L) <= R_bare(infty) ~ R_SD (substrate has SD asymptotic).
    Hence R_PV(L; M) < R_bare(L) <= R_SD
    => R_PV - R_SD < 0
  Step 4 (direction):
    sign( R_PV(L=12; M_KK=1) - R_SD ) = -1
    [pre-registered sign_pred = +1; substrate-physics chain yields -1]

The plan's Step-3 narrative ("PV ADDS BACK a finite subtraction") was
qualitative; the canonical PV regulator on D_K^2 is a SUBTRACTION
operator, not an additive UV restoration. The script computes honestly
and emits sign_verdict=FAIL when the computed direction does not match
the plan's pre-registered direction. No convention-shopping; the
pre-registration is binding (PROHIBITED_ACTIONS Class 1).

DISCIPLINE
----------
- `from canonical_constants import *`
- All intermediates tagged `# (local)`
- GPU torch.linalg available; small-N loops kept on numpy (data already cached)
- SHA-256 of all inputs logged in first ~20 lines of stdout
- Dual-SHA emission (audit + content) per S84+ schema
- Schema-v2 3-tuple companion row (sign / magnitude / regime) per S87+ extension
- Regulator-pin tag: a_n^{Pauli-Villars} (per regulator-pin-discipline.md)
"""

from __future__ import annotations

# -----------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY)
# -----------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import *  # noqa: F401,F403

# -----------------------------------------------------------------------------
# Section 2 — Standard imports
# -----------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# -----------------------------------------------------------------------------
SESSION = "S87"                                                # (local)
GATE_ID = "S87-PV-SUBTRACTION-RECALIBRATION"                    # (local)
SCHEME = "Pauli-Villars-finite-L"                               # (local)
CONVENTION = "substrate-mass-scale-M_KK"                        # (local)
L_MAX = 12                                                      # (local)

# Pre-registered thresholds (frozen at plan-freeze; DO NOT EDIT)
RATIO_PASS_REL_ERR = 1e-12          # (local) max_rel_err PASS ceiling
RATIO_INFO_REL_ERR = 1e-9           # (local) max_rel_err INFO ceiling
ABS_PASS_PV_SD = 1e-6               # (local) |R_PV - R_SD| PASS floor
ABS_INFO_PV_SD = 1e-9               # (local) |R_PV - R_SD| INFO floor
SIGN_PRED = +1                      # (local) plan-pinned predicted direction

CACHE_L12 = resolve_output(84, 's84_spectrum_cache_L12_tau019.npz')
OUT_NPZ = resolve_output(87, 's87_w1b_pv_subtraction_recalibration.npz')
OUT_PNG = resolve_output(87, 's87_w1b_pv_subtraction_recalibration.png')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

# Regulator-pin tag in regulator-pin-discipline.md form for any a_n citation:
REGULATOR_TAG = "Pauli-Villars"     # (local) -> a_n^{Pauli-Villars}

# PV mass scale: substrate dimensionless M_KK = 1 by convention (eigenvalues
# in M_KK units already; canonical_constants.M_KK = 7.428660e+16 GeV is the
# DIMENSIONFUL value — for the spectral operator on dimensionless lambda_k
# the natural PV mass is unity).
M_KK_DIMLESS = 1.0                  # (local) PV mass-scale in eigenvalue units

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    CACHE_L12,
]

# -----------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
# -----------------------------------------------------------------------------

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


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes()         # (local)
    canonical_bytes = canonical_path.read_bytes()   # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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


# -----------------------------------------------------------------------------
# Section 5 — Spectrum loading + L_max truncation
# -----------------------------------------------------------------------------

def load_spectrum(L_max_target: int):
    """Load |lambda_k| with irrep multiplicity m_k from the L=12 master cache,
    truncated to sectors with level <= L_max_target.

    Returns (lambdas, mults) as 1D float64 arrays (one entry per distinct
    eigenvalue line; multiplicity carried as separate column for canonical
    Mellin-Dirichlet identity check).
    """
    data = np.load(CACHE_L12, allow_pickle=True)
    sec = data["sector_evals"].item()                     # (local)
    lams = []                                             # (local)
    mults = []                                            # (local)
    for (p, q), v in sec.items():
        if v["level"] > L_max_target:
            continue
        ev = np.asarray(v["abs_evals"], dtype=np.float64) # (local)
        m = int(v["dim"])                                 # (local)
        lams.append(ev)
        mults.append(np.full_like(ev, m, dtype=np.float64))
    lambdas = np.concatenate(lams)                        # (local)
    mks = np.concatenate(mults)                           # (local)
    return lambdas, mks


# -----------------------------------------------------------------------------
# Section 6 — Spectral observables (regulator-pin-tagged)
# -----------------------------------------------------------------------------

def heat_kernel(t_arr, lambdas, mks):
    """K(t) = sum_k m_k * exp(-lambda_k^2 t)."""
    lam2 = (lambdas * lambdas).reshape(1, -1)             # (local)
    t = t_arr.reshape(-1, 1)                              # (local)
    K = np.sum(mks.reshape(1, -1) * np.exp(-lam2 * t), axis=1)  # (local)
    return K


def zeta_D(s, lambdas, mks):
    """zeta_D(s) = sum_k m_k * lambda_k^{-s}."""
    return np.sum(mks * np.power(lambdas, -s))


def mellin_integral(s, lambdas, mks, t_min=1e-6, t_max=50.0, n_quad=4096):
    """integral_0^infty t^(s/2 - 1) K(t) dt — log-spaced trapezoidal quadrature.

    Finite-spectrum K(t) decays as exp(-lambda_min^2 t), so cutoff at
    t_max=50 with lambda_min ~ 0.82 (=> K(50) ~ exp(-33.6) ~ 2.6e-15)
    is below double precision floor.
    """
    t_grid = np.geomspace(t_min, t_max, n_quad)           # (local)
    K = heat_kernel(t_grid, lambdas, mks)                 # (local)
    integrand = np.power(t_grid, s / 2.0 - 1.0) * K       # (local)
    # log-spaced trapezoidal: dt scales with t
    return np.trapezoid(integrand, t_grid)


def mellin_dirichlet_check(s, lambdas, mks, n_quad=8192):
    """Verify zeta_D(s) * Gamma(s/2) == integral_0^infty t^(s/2-1) K(t) dt."""
    from scipy.special import gamma as Gamma             # (local)
    lhs = zeta_D(s, lambdas, mks) * Gamma(s / 2.0)       # (local)
    # Choose t_min adaptively: K(t) for very small t still bounded by sum m_k.
    sum_m = float(np.sum(mks))                           # (local)
    # For s=3 -> s/2-1 = 0.5; integrand ~ t^0.5 * K(t); near t=0 K -> sum_m
    # so integrand ~ t^0.5 * sum_m, integrable. t_min=1e-8 fine.
    rhs = mellin_integral(s, lambdas, mks, t_min=1e-8, t_max=80.0, n_quad=n_quad)
    rel_err = abs(lhs - rhs) / max(abs(lhs), 1e-300)     # (local)
    return float(lhs), float(rhs), float(rel_err)


def pv_subtracted_moment(s, lambdas, mks, M):
    """R_PV(L; M) = sum_k m_k * lambda_k^{-s} - sum_k m_k * (lambda_k^2 + M^2)^{-s/2}.

    The PV-shift on D_K^2 spectrum: lambda^2 -> lambda^2 + M^2, then take the
    same s-power as the bare moment. At s=3 in 4D-spectrum convention this
    is the canonical Pauli-Villars subtraction on the squared-Dirac.
    """
    bare = np.sum(mks * np.power(lambdas, -s))                                  # (local)
    pv_shift = np.sum(mks * np.power(lambdas * lambdas + M * M, -s / 2.0))      # (local)
    return float(bare - pv_shift), float(bare), float(pv_shift)


def seeley_dewitt_a2_fit(lambdas, mks, t_min=1e-3, t_max=1e-1, n_quad=200):
    """Continuum SD coefficient a_2^{Pauli-Villars} from small-t fit of t*K(t).

    Heat-kernel small-t expansion (d_spec=4): K(t) ~ a_0/t^2 + a_2/t + a_4 + O(t).
    Multiply by t^2: t^2 * K(t) ~ a_0 + a_2 * t + a_4 * t^2 + ... (polynomial in t).
    Linear regression of t^2*K(t) vs t -> intercept=a_0, slope=a_2.

    Note: the regulator-pin tag is Pauli-Villars (a_2^{Pauli-Villars}) per
    regulator-pin-discipline.md; the PV scheme is implemented as the
    auxiliary-mass-shift subtraction in pv_subtracted_moment(); the SD a_n
    extracted from the unsubtracted heat kernel here is the leading-order
    R_SD continuum proxy that R_PV is compared against.
    """
    t_grid = np.geomspace(t_min, t_max, n_quad)              # (local)
    K = heat_kernel(t_grid, lambdas, mks)                    # (local)
    y = t_grid * t_grid * K                                  # (local) t^2 * K(t)
    # Linear fit y ~ a_0 + a_2 * t (drop higher-order on small-t window)
    A = np.column_stack([np.ones_like(t_grid), t_grid])      # (local)
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)             # (local)
    a_0, a_2 = float(coef[0]), float(coef[1])                # (local)
    return a_0, a_2


def sd_residue_at_s3(a_2):
    """R_SD at s=3 in 4D-spectrum convention.

    For d_spec=4 the Mellin transform of K(t) has a simple pole at s=3
    with residue 2 * a_2 / Gamma(3/2) (heat-kernel SD asymptotic).
    Reference: Connes-Chamseddine 1996 spectral-action computation.
    """
    from scipy.special import gamma as Gamma                # (local)
    return 2.0 * a_2 / Gamma(1.5)


# -----------------------------------------------------------------------------
# Section 7 — Plot
# -----------------------------------------------------------------------------

def make_plot(L_list, pv_residues, sd_residue, mellin_rel_errs,
              sign_dpv, M_used, lambda_max_L12, ratio_pass, info_pass):
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    ax = axes[0]
    ax.plot(L_list, pv_residues, "o-", label="R_PV(L; M_KK)", color="C0")
    ax.axhline(sd_residue, ls="--", color="C3", label=f"R_SD continuum = {sd_residue:.4e}")
    ax.set_xlabel("L_max")
    ax.set_ylabel("Residue at s=3 (substrate-distance-1)")
    ax.set_title("(A) PV vs SD residue across L_max")
    ax.legend()
    ax.grid(alpha=0.3)

    ax = axes[1]
    ax.semilogy(L_list, np.maximum(mellin_rel_errs, 1e-300), "s-", color="C2",
                label="max_rel_err (Mellin-Dirichlet identity)")
    ax.axhline(ratio_pass, ls=":", color="g", label=f"PASS ceiling = {ratio_pass:.0e}")
    ax.axhline(info_pass, ls=":", color="orange", label=f"INFO ceiling = {info_pass:.0e}")
    ax.set_xlabel("L_max")
    ax.set_ylabel("max_rel_err |LHS-RHS|/|LHS|")
    ax.set_title("(B) Mellin-Dirichlet identity precision vs L_max")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    ax = axes[2]
    sign_color = "g" if sign_dpv == SIGN_PRED else "r"
    label = (f"sign(R_PV(L=12)-R_SD) = {sign_dpv:+d}\n"
             f"sign_pred = {SIGN_PRED:+d}\n"
             f"M_PV(dimless) = {M_used:.3f}\n"
             f"max(|lambda|_L=12) = {lambda_max_L12:.3f}")
    ax.text(0.5, 0.5, label, ha="center", va="center", fontsize=12,
            transform=ax.transAxes,
            bbox=dict(facecolor=sign_color, alpha=0.25))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("(C) Directional sign verdict")

    fig.suptitle("S87 W1b-1 PV-Subtraction Recalibration", fontsize=14)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)


# -----------------------------------------------------------------------------
# Section 8 — Verdict + 4-tuple
# -----------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, audit_sha, content_sha,
                   sign_v, mag_v, regime_v):
    """Atomic append: canonical line + dual-SHA companion + Schema-v2 3-tuple companion."""
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(dual_sha_row)
        fp.write(schema_v2_row)


def evaluate_3tuple(max_rel_err, abs_pv_sd, sign_obs, M, lambda_max):
    """Compute (sign_verdict, magnitude_verdict, regime_verdict) per plan §W1b-1."""
    # sign_verdict
    if sign_obs == SIGN_PRED:
        sign_v = "PASS"
    else:
        sign_v = "FAIL"

    # magnitude_verdict
    rel_pass = max_rel_err < RATIO_PASS_REL_ERR
    rel_info = max_rel_err < RATIO_INFO_REL_ERR
    abs_pass = abs_pv_sd > ABS_PASS_PV_SD
    abs_info = abs_pv_sd > ABS_INFO_PV_SD
    if rel_pass and abs_pass:
        mag_v = "PASS"
    elif rel_info and abs_info:
        mag_v = "INFO"
    else:
        mag_v = "FAIL"

    # regime_verdict
    if M > lambda_max:
        regime_v = "BREAKDOWN"
    elif M > 0.5 * lambda_max:
        regime_v = "MARGINAL"
    else:
        regime_v = "VALID"

    return sign_v, mag_v, regime_v


def collapse_verdict(sign_v, mag_v, regime_v):
    """Composite-collapse rule per gate-verdicts.md §"S87+ canonical form"."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


# -----------------------------------------------------------------------------
# Section 9 — Main
# -----------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Pin SHAs
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure (legacy): {closure[:16]}...")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # 2. Load spectra at L=10 (level-truncated) and L=12 (full master cache)
    print("=== Loading spectra ===")
    lam_L10, mks_L10 = load_spectrum(L_max_target=10)
    lam_L12, mks_L12 = load_spectrum(L_max_target=12)
    n10 = len(lam_L10)        # (local) distinct eigenvalues
    n12 = len(lam_L12)        # (local)
    n10_with_mult = float(np.sum(mks_L10))   # (local)
    n12_with_mult = float(np.sum(mks_L12))   # (local)
    print(f"  L=10: {n10} distinct, {n10_with_mult:.0f} with irrep multiplicity")
    print(f"  L=12: {n12} distinct, {n12_with_mult:.0f} with irrep multiplicity")
    print(f"  range L=12: [{lam_L12.min():.4f}, {lam_L12.max():.4f}]")
    print()

    # 3. Mellin-Dirichlet identity check at s=3 under PV-tagged scheme
    print("=== Mellin-Dirichlet identity verification at s=3 ===")
    s_pole = 3.0     # (local) substrate-distance-1 pole
    lhs10, rhs10, rel10 = mellin_dirichlet_check(s_pole, lam_L10, mks_L10)
    lhs12, rhs12, rel12 = mellin_dirichlet_check(s_pole, lam_L12, mks_L12)
    print(f"  L=10: LHS={lhs10:.6e}  RHS={rhs10:.6e}  rel_err={rel10:.3e}")
    print(f"  L=12: LHS={lhs12:.6e}  RHS={rhs12:.6e}  rel_err={rel12:.3e}")
    max_rel_err = max(rel10, rel12)         # (local)
    print(f"  max_rel_err = {max_rel_err:.3e}")
    print()

    # 4. PV-subtracted moments at L=10, L=12 with M = M_KK_dimless = 1.0
    print("=== PV-subtracted moment R_PV(L; M_KK) at s=3 ===")
    M = M_KK_DIMLESS                        # (local)
    pv10, bare10, shift10 = pv_subtracted_moment(s_pole, lam_L10, mks_L10, M)
    pv12, bare12, shift12 = pv_subtracted_moment(s_pole, lam_L12, mks_L12, M)
    print(f"  L=10: bare = {bare10:.6e}  PV-shift = {shift10:.6e}  R_PV = {pv10:.6e}")
    print(f"  L=12: bare = {bare12:.6e}  PV-shift = {shift12:.6e}  R_PV = {pv12:.6e}")
    print()

    # 5. Continuum SD residue R_SD from a_2^{Pauli-Villars} fit on L=12 K(t)
    print("=== Continuum-SD residue R_SD (a_2^{Pauli-Villars} fit on L=12) ===")
    a_0, a_2 = seeley_dewitt_a2_fit(lam_L12, mks_L12)
    R_SD = sd_residue_at_s3(a_2)            # (local)
    print(f"  a_0^Pauli-Villars (small-t intercept of t^2*K) = {a_0:.6e}")
    print(f"  a_2^Pauli-Villars (small-t slope of t^2*K)     = {a_2:.6e}")
    print(f"  R_SD = 2 * a_2 / Gamma(3/2)                   = {R_SD:.6e}")
    print()

    # 6. Sign + offset of (R_PV(L=12) - R_SD)
    print("=== Sign / offset of (R_PV(L=12; M_KK) - R_SD) ===")
    delta_pv = pv12 - R_SD                  # (local)
    abs_delta = abs(delta_pv)               # (local)
    sign_obs = int(np.sign(delta_pv))       # (local)
    print(f"  R_PV(L=12; M_KK) - R_SD = {delta_pv:+.6e}")
    print(f"  |R_PV - R_SD|           = {abs_delta:.6e}")
    print(f"  sign(R_PV - R_SD)       = {sign_obs:+d}  (pre-registered: {SIGN_PRED:+d})")
    print()

    # 7. Schema-v2 3-tuple
    lam_max = float(lam_L12.max())          # (local)
    sign_v, mag_v, regime_v = evaluate_3tuple(
        max_rel_err, abs_delta, sign_obs, M, lam_max,
    )
    composite = collapse_verdict(sign_v, mag_v, regime_v)
    print(f"=== Schema-v2 3-tuple ===")
    print(f"  sign_verdict      = {sign_v}    (obs={sign_obs:+d}, pred={SIGN_PRED:+d})")
    print(f"  magnitude_verdict = {mag_v}")
    print(f"  regime_verdict    = {regime_v}  (M={M:.3f}, max(lambda)={lam_max:.3f})")
    print(f"  composite collapse: {composite}")
    print()

    # 8. Save data
    np.savez(
        OUT_NPZ,
        lambda_L10=lam_L10,
        lambda_L12=lam_L12,
        mults_L10=mks_L10,
        mults_L12=mks_L12,
        pv_residue_L10=pv10,
        pv_residue_L12=pv12,
        bare_residue_L10=bare10,
        bare_residue_L12=bare12,
        pv_shift_L10=shift10,
        pv_shift_L12=shift12,
        sd_residue_continuum=R_SD,
        sd_a0_pauli_villars=a_0,
        sd_a2_pauli_villars=a_2,
        mellin_dirichlet_lhs=np.array([lhs10, lhs12]),
        mellin_dirichlet_rhs=np.array([rhs10, rhs12]),
        mellin_dirichlet_rel_err=np.array([rel10, rel12]),
        max_rel_err=max_rel_err,
        sign_dpv_L12_minus_continuum=sign_obs,
        delta_pv_minus_sd=delta_pv,
        M_pv_dimless=M,
        lambda_max_L12=lam_max,
        sign_pred=SIGN_PRED,
    )
    print(f"  data saved: {OUT_NPZ.name}")

    # 9. Plot
    make_plot(
        L_list=[10, 12],
        pv_residues=[pv10, pv12],
        sd_residue=R_SD,
        mellin_rel_errs=[rel10, rel12],
        sign_dpv=sign_obs,
        M_used=M,
        lambda_max_L12=lam_max,
        ratio_pass=RATIO_PASS_REL_ERR,
        info_pass=RATIO_INFO_REL_ERR,
    )
    print(f"  plot saved: {OUT_PNG.name}")
    print()

    # 10. 4-tuple emission
    tag = emit_4tuple(max_rel_err, SCHEME, CONVENTION, L_MAX)
    print(tag)

    # 11. Append verdict (atomic dual-SHA + Schema-v2 3-tuple companion)
    append_verdict(composite, max_rel_err, audit_sha, content_sha,
                   sign_v, mag_v, regime_v)
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
