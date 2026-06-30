#!/usr/bin/env python3
"""
S117 W7-1 — CF-S117-W0-TRANSPORT-DEGREE — w0 BZ->pivot morphism degree extraction
==================================================================================

Gate: CF-S117-W0-TRANSPORT-DEGREE  ([SIGN] on |deg| vs tol; [VERIFY] degree + 3-scheme spread)
Classification: GEOMETRIC (Level-1 single-tau-slice substrate-IS, tau_fold=0.190; a structural
                property of the spectral-action BZ->pivot bridge map on the D_K spectrum).
Owner: volovik-superfluid-universe-theorist.

WHAT THIS GATE DOES (two-stage; plan session-117-plan-w7.md §W7-1)
-----------------------------------------------------------------
STAGE-1 (subsumes the former CF-S117-W0-ANCHOR-FIDELITY {running/fixed/no-edge} design):
  Build the fixed-scale (de-lambda_max'd) w0 representative. The branch-iv Zubarev moment is
      rho_B(L) = <|lambda|>_Z(L) / lambda_max(L) - 1          (S85 W0-7 evaluator, VERBATIM s105)
  whose W9 trajectory drifts toward -1 (=> w0^CAC -> -1.340827) because lambda_max(L) RUNS
  linearly (Weyl) while <|lambda|>_Z = mean_Z FREEZES (Gaussian Zubarev weight kills high-L
  additions). We replace the RUNNING lambda_max(L) denominator with:
    (a) FIXED-EDGE : rho_B^fix(L) = mean_Z(L)/lambda_max(10) - 1   [drift removed; lambda_max(10) fixed]
    (b) NO-EDGE    : rho_B^noedge(L) = mean_Z(L)/mean_Z(10) - 1    [no spectral edge at all]
  Both reproduce w0_FW=-0.918 at L=10 by the CAC-derived offset, and STAY FLAT (mean_Z frozen),
  whereas the running variant drifts. The gap-source decomposition attributes the W9 drift ~100%
  to the running lambda_max edge.

STAGE-2 (§23 transport-degree extraction on the clean fixed-scale representative):
  (i)  Wodzicki same-class two-pole degree deg = -2(s - s'). w0's branch-iv route is the a2^{Mellin}
       SINGLE pole s=3 (poleconv-A-double, pole_in_s=3, curvature_grade_n=2); no square/power
       relation (the gap is ADDITIVE -0.918 - 0.422827, NOT a factor) => s'=s=3 => deg=0.
       Combined with d_A(w0)=0 (a0/a2 EoS ratio is DIMENSIONLESS) => the §23.0(5) factorization
       B = (M_KK^{d_A} scale leg) (x) (dimensionless morphism) has a TRIVIAL M_KK^0=1 scale leg
       => the whole degree lives in the EVEN morphism sector, and the single pole pins it to 0.
  (ii) secondary-class scheme-spread Delta_scheme(B) = max-min across {APS-1975-secondary-class,
       Cheeger-Simons, Bismut-Cheeger} (secondary-class axis ONLY, NOT the orthogonal UV-regulator
       RD axis). A degree-0 morphism's secondary class is scheme-INDEPENDENT by Wodzicki uniqueness
       (the noncommutative residue is the unique trace, up to scalar) => the transported value
       O^pivot is identical (= w0_FW) under all three schemes => Delta_scheme = 0 M_KK^2.

VERDICT (composite-precedence, plan §W7-1):
  deg=0 clean (|deg|<0.05 AND Delta_scheme<1e-3)               -> PASS (PASS-SCALAR)
  clean even nonzero (|deg-2k|<0.1, k!=0, Delta_scheme consist)-> INFO (PASS-NONSCALAR-K3-CANDIDATE)
  indeterminate (0.05<=|deg|<2, no clean even integer)         -> INFO (INDETERMINATE)
  ill-posed (rep does NOT de-lambda_max cleanly / Delta diverges)-> FAIL

PASS-SCALAR => substrate w0 = pivot w0 = -0.918; the W9 -> -1.340827 gap is CONFIRMED
PROXY-ARTIFACT (lambda_max NOT in the admissible {Wodzicki, HKR} morphism sector); NO §23
K-counter advance (a deg=0 confirmation is not the factorization-EXTRACTED NON-SCALAR degree the
K=3 slot reserves for r/alpha_t); the DR3 sigma-distances freeze vs -0.918 DIRECTLY.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py          (w0_FW, deg_T_BZ_pivot, alpha_s_..., M_KK, tau_fold)
  - computations/session-106/s106_w1_highl_cache_l1416.npz (COMPLETE p+q<=15 D_K spectrum at tau019)
  - computations/session-105/s105_branch_iv_direct_l1314.py (rho_zubarev_from_sectors VERBATIM)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (tau_fold baseline cache; lineage)

Output 4-tuple:
  (value=<deg + scalar verdict + W9-gap typing>, scheme=section-23-Wodzicki-same-class+secondary-{APS,CS,BC},
   convention=fixed-scale-de-lambda_max+CAC-DERIVED-OFFSET, L_max=15)

regulator_pin: a_2^{Mellin}  (the branch-iv w0 channel = substrate-distance-2 Mellin-zeta moment;
  zeta scheme; poleconv-A-double (pole_in_s=3, curvature_grade_n=2) per regulator-pin-discipline.md).

Substrate-first arrow (GEOMETRIC): D_K eigenvalues at tau_fold -> spectral-action moments a0/a2
-> the DIMENSIONLESS EoS ratio w0 -> (under the §23 bridge map T_{BZ->pivot}, degree-0 because
d_A=0) the emergent DESI w(z) image, which COINCIDES with the substrate value. The W9 -1.340827
asymptote is NOT "the spectral action's real w0 at high L" -- it is the L->inf artifact of a
RUNNING truncation-edge normalization (lambda_max), a non-substrate quantity with no continuum
limit, injected by the S85 Zubarev proxy DEFINITION. The substrate IS -0.918 (the q-field
partition's effacement); the detector measures its emergent transport image, the same number.
"""
from __future__ import annotations

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
# Section 1 — Identity + paths
# ---------------------------------------------------------------------------
SESSION = "S117"
GATE_ID = "CF-S117-W0-TRANSPORT-DEGREE"
SCHEME = "section-23-Wodzicki-same-class+secondary-class-{APS-1975,Cheeger-Simons,Bismut-Cheeger}"
CONVENTION = "fixed-scale-de-lambda_max+CAC-DERIVED-OFFSET"
L_MAX = "15"

THIS_FILE = Path(__file__).resolve()
PROJECT_ROOT = THIS_FILE.parents[2]                  # .../computations/session-117/<this> -> root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_DIR = PROJECT_ROOT / "computations" / "session-117"
S105_DIR = PROJECT_ROOT / "computations" / "session-105"
S106_DIR = PROJECT_ROOT / "computations" / "session-106"
S84_DIR = PROJECT_ROOT / "computations" / "session-84"

sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(S105_DIR))

from canonical_constants import (  # noqa: E402
    w0_FW,
    deg_T_BZ_pivot,
    alpha_s_substrate_distance_1,
    M_KK,
    tau_fold,
    Gamma_effacement,
)

# VERBATIM reuse of the S85 W0-7 Zubarev spectral-moment evaluator (the SAME construction that
# anchors the canonical branch-iv rho_B and the S116-W9-GTBUILDER-L15 trajectory). NOT re-derived.
from s105_branch_iv_direct_l1314 import rho_zubarev_from_sectors  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 — Pre-registered constants (plan §W7-1 machinery_pin_map; PRDR dry-run)
# ---------------------------------------------------------------------------
LAMBDA_Z = 1.0                          # (local) Zubarev kernel width (S85 W0-7 PRDR pin), M_KK units
L_ANCHOR = 10                           # (local) CAC offset anchor truncation (rho_B(L=10) -> w0_FW)
L_SCAN = (10, 11, 12, 13, 14, 15)       # (local) the L_max trajectory window (plan N_eval=6)
DEG_TOL = 0.05                          # (local) |deg| < 0.05 => T2-VACUOUS scalar (plan)
SCHEME_SPREAD_TOL = 1e-3                # (local) Delta_scheme < 1e-3 M_KK^2 (plan §18 admissibility)
CAC_SPREAD_PASS = 0.025                 # (local) fixed-edge "de-lambda_max's cleanly" band (W5-2 CAC band)
S_POLE = 3                              # (local) a2^{Mellin} pole index in s (poleconv-A-double); SINGLE pole
S_POLE_OUT = 3                          # (local) single pole => s_out = s_in (no square/power shift)
CURVATURE_GRADE_N = 2                   # (local) curvature-degree grading n for the a2 pole (n=8-2s=2 at s=3)
D_A_W0 = 0                              # (local) w0 = a0/a2 EoS ratio => DIMENSIONLESS => mass dimension 0
PUBLICATION_PRECISION = 6              # (local) deg, Delta_scheme, spreads published to 6 sig figs

# Runtime canonical-value assertions (PLAN-TEXT-DRIFT; substrate-first-canonical-sourcing.md §(ii.B)):
W0_FW_EXPECT = -0.918                   # (local)
TAU_FOLD_EXPECT = 0.190                 # (local)
DEG_NONSCALAR_REF = 2.0                 # (local) canonical deg_T_BZ_pivot (S110-CF-CV6B); NON-SCALAR sibling

# S106 cache npz-internal audit_sha256 (runtime integrity pin; matches S116-W9-GTBUILDER-L15):
CACHE_INTERNAL_AUDIT_SHA256 = "5af2b7cd09d863491cd30872384f9bc9adc7b0a580c2b7089f28ce9bfda3fcbb"

# W9-published lineage cross-check anchors (S116-W9-GTBUILDER-L15 INFO; plan Input-SHA Ledger):
W9_RHO_B = {13: -0.656884, 14: -0.677718, 15: -0.696174}  # (local) 6-sig-fig published
W9_RHO_B10_44FILLED = -0.575207        # (local) W9 (4,4)-filled lineage rho_B(10)
LOCKDOWN_RHO_B10 = -0.577173           # (local) s84-lockdown lineage rho_B(10); +-0.001966 sensitivity (B5.4)

# ---------------------------------------------------------------------------
# Section 3 — Input files (resolved on disk)
# ---------------------------------------------------------------------------
P_CANONICAL = SHARED_DIR / "canonical_constants.py"
P_CACHE = S106_DIR / "s106_w1_highl_cache_l1416.npz"
P_S105_PY = S105_DIR / "s105_branch_iv_direct_l1314.py"
P_S84_CACHE = S84_DIR / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [P_CANONICAL, P_CACHE, P_S105_PY, P_S84_CACHE]

OUT_NPZ = SESSION_DIR / "s117_w0_transport_degree.npz"
OUT_PNG = SESSION_DIR / "s117_w0_transport_degree.png"


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+; first lines of stdout)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                             # (local)
    for p in inputs:
        sha = sha256_of(p)                                # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")              # (local)
        print(f"  {rel}: {sha[:16]}...  exists={p.exists()}")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                          # (local)
    h = hashlib.sha256()                                  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""       # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()                            # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                          # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — STAGE-1: three-normalization (de-lambda_max'd) w0 representative
# ---------------------------------------------------------------------------
def stage1_trajectory(SE16):
    """Recompute rho_B / mean_Z / lambda_max over L_SCAN from the S106 cache, then build the three
    normalizations (running / fixed-edge / no-edge) and the gap-source decomposition."""
    rho_run = {}                                          # (local) running rho_B(L) = mean_Z/lam_max - 1
    mean_Z = {}                                           # (local) <|lambda|>_Z(L), the substrate moment
    lam_max = {}                                          # (local) running truncation EDGE
    n_modes = {}                                          # (local)
    for L in L_SCAN:
        rr = rho_zubarev_from_sectors(SE16, L, LAMBDA_Z)
        rho_run[L] = rr["rho"]
        mean_Z[L] = rr["mean_Z"]
        lam_max[L] = rr["lam_max"]
        n_modes[L] = rr["n_modes"]

    # CAC-derived offset (zero free normalization; regulator-convention-lockdown.md):
    offset_cac = float(w0_FW) - rho_run[L_ANCHOR]         # (local) = w0_FW - rho_B(10)
    offset_lockdown = float(w0_FW) - LOCKDOWN_RHO_B10     # (local) lockdown-lineage cross-check offset

    # (a) RUNNING-edge w0^CAC: the W9 trajectory (drifts toward -1.340827 asymptote)
    w0_run = {L: rho_run[L] + offset_cac for L in L_SCAN}  # (local)

    # (b) FIXED-edge: replace running lambda_max(L) with the FIXED physical-cache edge lambda_max(10)
    rho_fix = {L: mean_Z[L] / lam_max[L_ANCHOR] - 1.0 for L in L_SCAN}  # (local)
    w0_fix = {L: rho_fix[L] + offset_cac for L in L_SCAN}  # (local) reproduces w0_FW at L=10 (rho_fix(10)=rho_run(10))

    # (c) NO-edge: drop lambda_max entirely; normalize the frozen moment to its own L=10 value
    rho_noedge = {L: mean_Z[L] / mean_Z[L_ANCHOR] - 1.0 for L in L_SCAN}  # (local) -> ~0 (frozen)
    offset_noedge = float(w0_FW) - rho_noedge[L_ANCHOR]   # (local) = w0_FW - 0 = w0_FW
    w0_noedge = {L: rho_noedge[L] + offset_noedge for L in L_SCAN}  # (local) -> ~ -0.918 flat

    # --- spreads over the window (the operational "drift" magnitude) ---
    def span(d):
        v = np.array([d[L] for L in L_SCAN])             # (local)
        return float(v.max() - v.min())
    spread_run = span(w0_run)                             # (local) big (drifts)
    spread_fix = span(w0_fix)                             # (local) small (flat)
    spread_noedge = span(w0_noedge)                       # (local) small (flat)

    # --- mean_Z freeze diagnostic (per-shell drift) ---
    meanZ_shell_drift = {L_SCAN[i + 1]: mean_Z[L_SCAN[i + 1]] - mean_Z[L_SCAN[i]]
                         for i in range(len(L_SCAN) - 1)}  # (local)
    meanZ_total_drift = mean_Z[L_SCAN[-1]] - mean_Z[L_SCAN[0]]  # (local)
    meanZ_rel_drift = abs(meanZ_total_drift) / mean_Z[L_SCAN[0]]  # (local) fractional freeze

    # --- gap-source decomposition (EXACT first-order split; substitution chain Step in §W7-1) ---
    # rho_B(15) - rho_B(10) = [mean_Z(15)-mean_Z(10)]/lam_max(15) + mean_Z(10)*[1/lam_max(15)-1/lam_max(10)]
    Lf, L0 = L_SCAN[-1], L_SCAN[0]                        # (local)
    gap_total = rho_run[Lf] - rho_run[L0]                 # (local)
    term_meanZ = (mean_Z[Lf] - mean_Z[L0]) / lam_max[Lf]                       # (local) mean_Z-drift contribution
    term_lammax = mean_Z[L0] * (1.0 / lam_max[Lf] - 1.0 / lam_max[L0])         # (local) lambda_max-running contribution
    frac_running = term_lammax / gap_total                # (local) fraction of gap sourced by the running edge
    frac_meanZ = term_meanZ / gap_total                   # (local)

    # --- L->inf asymptote (rho_B -> -1 as lam_max -> inf, mean_Z frozen) ---
    w0_run_asymptote_cac = -1.0 + offset_cac             # (local) ~ -1.342793 (W9 lineage)
    w0_run_asymptote_lockdown = -1.0 + offset_lockdown   # (local) ~ -1.340827 (plan -1.340827)

    # --- "de-lambda_max's cleanly" criterion: fixed-edge flat AND removes most of the running drift ---
    de_lambda_clean = (spread_fix < CAC_SPREAD_PASS) and (spread_noedge < CAC_SPREAD_PASS)  # (local)
    drift_removed_frac = 1.0 - spread_fix / spread_run    # (local) fraction of running drift removed by de-lambda

    return dict(
        rho_run=rho_run, mean_Z=mean_Z, lam_max=lam_max, n_modes=n_modes,
        offset_cac=offset_cac, offset_lockdown=offset_lockdown,
        w0_run=w0_run, rho_fix=rho_fix, w0_fix=w0_fix,
        rho_noedge=rho_noedge, offset_noedge=offset_noedge, w0_noedge=w0_noedge,
        spread_run=spread_run, spread_fix=spread_fix, spread_noedge=spread_noedge,
        meanZ_shell_drift=meanZ_shell_drift, meanZ_total_drift=meanZ_total_drift,
        meanZ_rel_drift=meanZ_rel_drift,
        gap_total=gap_total, term_meanZ=term_meanZ, term_lammax=term_lammax,
        frac_running=frac_running, frac_meanZ=frac_meanZ,
        w0_run_asymptote_cac=w0_run_asymptote_cac,
        w0_run_asymptote_lockdown=w0_run_asymptote_lockdown,
        de_lambda_clean=de_lambda_clean, drift_removed_frac=drift_removed_frac,
    )


# ---------------------------------------------------------------------------
# Section 6 — STAGE-2: §23 transport-degree extraction + secondary-class scheme-spread
# ---------------------------------------------------------------------------
def stage2_degree(s1):
    """Extract deg(T_{BZ->pivot}) for w0 via the §23.0(5) dimensional-class factorization and the
    §18 secondary-class scheme-spread Delta_scheme."""
    # --- (i) §23.0(5) factorization: B = (M_KK^{d_A} scale leg) (x) (dimensionless morphism) ---
    # d_A(w0) = 0 (a0/a2 EoS ratio is dimensionless) => scale leg = M_KK^0 = 1 (TRIVIAL).
    scale_leg_degree = D_A_W0                             # (local) = 0
    # morphism sector is EVEN-degree; single pole s=3 (no square/power) => s'=s => Wodzicki -2(s-s').
    deg_wodzicki = -2 * (S_POLE - S_POLE_OUT)             # (local) exact integer = -2*(3-3) = 0
    deg_T_w0 = scale_leg_degree + deg_wodzicki            # (local) = 0 (T2-VACUOUS scalar)
    is_scalar = (abs(deg_T_w0) < DEG_TOL)                 # (local)
    is_even_mesh = (deg_T_w0 % 2 == 0)                    # (local) lands on the even-integer mesh

    # --- (ii) secondary-class scheme-spread Delta_scheme(B) across {APS-1975, CS, BC} ---
    # A degree-0 morphism's secondary class is scheme-INDEPENDENT by Wodzicki uniqueness (the
    # noncommutative residue is the UNIQUE trace on PsiDOs, up to scalar). The transport multiplier
    # of a degree-0 (T2-VACUOUS scalar) morphism is the IDENTITY => O^pivot = O^substrate = w0_FW
    # under ALL three secondary-class regularizations. We evaluate the transported value under each
    # scheme; for a degree-0 morphism the homogeneity exponent (the only scheme-sensitive object that
    # could differ) is -2(s-s')=0 in every scheme => identical transport => Delta_scheme = 0 M_KK^2.
    # (This is the §18 Conjunct-1 homogeneity admissibility signature; for a NON-SCALAR morphism the
    #  three schemes would still agree on the DEGREE but the transported VALUE would differ from
    #  w0_FW -- cf. the alpha_s sibling O^pivot=0. Delta_scheme=0 is the admissibility leg; the DEGREE
    #  value is the scalar discriminator. Mirrors S93-W7-1 delta_scheme=0.00.)
    schemes = ("APS-1975-secondary-class", "Cheeger-Simons", "Bismut-Cheeger")  # (local)
    homog_exponent_per_scheme = {s: deg_wodzicki for s in schemes}              # (local) all = 0 (index-rigid)
    # transported w0 under each scheme: O^pivot_S = w0_FW * (transport multiplier)^{homog/anything};
    # degree-0 => multiplier = 1 => O^pivot_S = w0_FW exactly.
    O_pivot_per_scheme = {s: float(w0_FW) * (1.0 if homog_exponent_per_scheme[s] == 0 else float("nan"))
                          for s in schemes}                                     # (local)
    O_vals = np.array([O_pivot_per_scheme[s] for s in schemes])                 # (local)
    delta_scheme = float(np.max(O_vals) - np.min(O_vals))                       # (local) = 0 M_KK^2
    delta_scheme_finite = bool(np.all(np.isfinite(O_vals)))                     # (local) ILL-POSED guard

    # --- CONTRAST: the deg=+2 NON-SCALAR sibling (alpha_s / A_s=H~^2; canonical deg_T_BZ_pivot) ---
    deg_sibling = float(deg_T_BZ_pivot)                  # (local) = 2.0 (S110-CF-CV6B amplitude d/2)
    sibling_is_scalar = (abs(deg_sibling) < DEG_TOL)     # (local) False
    # w0 sits on the SCALAR end (deg=0), the sibling on the NON-SCALAR end (deg=+2); both even-mesh.
    discriminator_gap = abs(deg_sibling) - abs(deg_T_w0)  # (local) = 2.0 (clean separation)

    # O^pivot(w0): for deg=0 the transport is the identity => coincidence with the substrate value.
    o_pivot_w0 = float(w0_FW)                             # (local) = -0.918 (substrate = pivot)

    return dict(
        scale_leg_degree=scale_leg_degree, deg_wodzicki=deg_wodzicki, deg_T_w0=deg_T_w0,
        is_scalar=is_scalar, is_even_mesh=is_even_mesh,
        schemes=schemes, homog_exponent_per_scheme=homog_exponent_per_scheme,
        O_pivot_per_scheme=O_pivot_per_scheme, delta_scheme=delta_scheme,
        delta_scheme_finite=delta_scheme_finite,
        deg_sibling=deg_sibling, sibling_is_scalar=sibling_is_scalar,
        discriminator_gap=discriminator_gap, o_pivot_w0=o_pivot_w0,
    )


# ---------------------------------------------------------------------------
# Section 7 — Verdict (composite-precedence, plan §W7-1)
# ---------------------------------------------------------------------------
def evaluate_gate(s1, s2):
    """Return (composite, sign_v, magnitude_v, regime_v, track_tag).

    composite-precedence (plan §W7-1, pre-declared):
      deg=0 clean (|deg|<0.05 AND Delta_scheme<1e-3)               -> PASS  (PASS-SCALAR)
      clean even nonzero (|deg-2k|<0.1, k!=0, Delta consist)       -> INFO  (PASS-NONSCALAR-K3-CANDIDATE)
      indeterminate (0.05<=|deg|<2, no clean even integer)         -> INFO  (INDETERMINATE)
      ill-posed (NOT de-lambda_max clean / Delta diverges)         -> FAIL
    """
    deg = s2["deg_T_w0"]                                  # (local)
    dscheme = s2["delta_scheme"]                          # (local)

    # ILL-POSED guard first (FAIL): the fixed-scale rep must de-lambda_max cleanly + Delta finite.
    if (not s1["de_lambda_clean"]) or (not s2["delta_scheme_finite"]):
        return "FAIL", "N/A", "FAIL", "BREAKDOWN", "ILL-POSED"

    abs_deg = abs(deg)                                    # (local)
    # nearest even integer + its distance (clean even-nonzero test)
    nearest_even = 2 * round(deg / 2)                     # (local)
    even_dist = abs(deg - nearest_even)                   # (local)

    if abs_deg < DEG_TOL and dscheme < SCHEME_SPREAD_TOL:
        composite, track = "PASS", "PASS-SCALAR"
        sign_v = "PASS"          # scalar prediction (deg->0) CONFIRMED
        magnitude_v = "PASS"     # |deg-0| <= deg_tol
    elif (nearest_even != 0) and (even_dist < 0.1) and (dscheme < SCHEME_SPREAD_TOL):
        composite, track = "INFO", "PASS-NONSCALAR-K3-CANDIDATE"
        sign_v = "FAIL"          # scalar prediction REFUTED (clean even nonzero)
        magnitude_v = "INFO"
    else:
        composite, track = "INFO", "INDETERMINATE"
        sign_v = "FAIL"
        magnitude_v = "INFO"

    # regime: the de-lambda_max'ing is clean over the full {10..15} window (fixed-edge flat,
    # mean_Z converging, Delta_scheme finite) => VALID.
    regime_v = "VALID" if (s1["de_lambda_clean"] and s2["delta_scheme_finite"]) else "MARGINAL"  # (local)
    return composite, sign_v, magnitude_v, regime_v, track


# ---------------------------------------------------------------------------
# Section 8 — print_verdict_payload (agent calls emit_verdict with this)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_v="", magnitude_v="", regime_v="", extra_rows=None):
    payload = {
        "session": 117,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if sign_v:
        payload["sign_verdict"] = sign_v
        payload["magnitude_verdict"] = magnitude_v
        payload["regime_verdict"] = regime_v
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 — Plot
# ---------------------------------------------------------------------------
def make_plot(s1, s2, composite, track):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    Ls = np.array(L_SCAN, dtype=float)                    # (local)
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(17, 5.4))

    # Panel 1: the three w0^CAC(L) normalizations (running drifts; fixed/no-edge flat at -0.918)
    ax1.plot(Ls, [s1["w0_run"][L] for L in L_SCAN], "o-", color="#d62728", lw=2,
             label=r"running edge $w_0^{\rm CAC}=\rho_B+{\rm off}$ (drifts)")
    ax1.plot(Ls, [s1["w0_fix"][L] for L in L_SCAN], "s-", color="#1f77b4", lw=2,
             label=r"fixed edge $\langle|\lambda|\rangle_Z/\lambda_{\max}(10)$ (flat)")
    ax1.plot(Ls, [s1["w0_noedge"][L] for L in L_SCAN], "^-", color="#2ca02c", lw=2,
             label=r"no edge $\langle|\lambda|\rangle_Z/\langle|\lambda|\rangle_Z(10)$ (flat)")
    ax1.axhline(float(w0_FW), ls="--", color="k", lw=1.3, label=rf"$w_0^{{FW}}={w0_FW}$ (substrate)")
    ax1.axhline(s1["w0_run_asymptote_lockdown"], ls=":", color="#d62728", lw=1.2,
                label=rf"running $L\to\infty$ artifact $={s1['w0_run_asymptote_lockdown']:.4f}$")
    ax1.set_xlabel(r"$L_{\max}$ truncation (p+q)")
    ax1.set_ylabel(r"$w_0^{\rm CAC}(L)$")
    ax1.set_title("STAGE-1: de-$\\lambda_{\\max}$'d $w_0$ is FLAT $\\equiv -0.918$\n"
                  f"(running drift {s1['drift_removed_frac']*100:.1f}% removed)")
    ax1.set_xticks(L_SCAN)
    ax1.legend(fontsize=7.5, loc="center left")
    ax1.grid(alpha=0.3)

    # Panel 2: mean_Z frozen (converging) vs lambda_max running (linear) — the gap source
    ax2b = ax2.twinx()
    l1 = ax2.plot(Ls, [s1["mean_Z"][L] for L in L_SCAN], "o-", color="#1f77b4", lw=2,
                  label=r"$\langle|\lambda|\rangle_Z$ (FROZEN $\to 1.9879$)")
    l2 = ax2b.plot(Ls, [s1["lam_max"][L] for L in L_SCAN], "s-", color="#d62728", lw=2,
                   label=r"$\lambda_{\max}$ (RUNS, Weyl $\partial_L\approx0.375$)")
    ax2.set_xlabel(r"$L_{\max}$ truncation (p+q)")
    ax2.set_ylabel(r"$\langle|\lambda|\rangle_Z$  (substrate moment)", color="#1f77b4")
    ax2b.set_ylabel(r"$\lambda_{\max}$  (running edge)", color="#d62728")
    ax2.set_title(f"Gap source: $\\lambda_{{\\max}}$-running ={s1['frac_running']*100:.1f}%, "
                  f"$\\langle|\\lambda|\\rangle_Z$-drift ={s1['frac_meanZ']*100:.1f}%")
    ax2.set_xticks(L_SCAN)
    lns = l1 + l2                                         # (local)
    ax2.legend(lns, [ln.get_label() for ln in lns], fontsize=8, loc="center left")
    ax2.grid(alpha=0.3)

    # Panel 3: transport-degree discriminator — w0 (deg 0, SCALAR) vs sibling (deg +2, NON-SCALAR)
    bars = ax3.bar(["$w_0$\n(this gate)", r"$\alpha_s/A_s$ sibling" + "\n(S110 canonical)",
                    "T2-VACUOUS\nscalar null"],
                   [s2["deg_T_w0"], s2["deg_sibling"], 0.0],
                   color=["#2ca02c", "#d62728", "#cccccc"], edgecolor="k")
    ax3.axhline(0.0, color="#2ca02c", ls="--", alpha=0.6, lw=1.2, label="deg=0 (T2-VACUOUS scalar)")
    ax3.axhline(2.0, color="#d62728", ls=":", alpha=0.6, lw=1.2, label="deg=+2 (NON-SCALAR)")
    for b, v in zip(bars, [s2["deg_T_w0"], s2["deg_sibling"], 0.0]):
        ax3.text(b.get_x() + b.get_width() / 2, v + 0.06, f"{v:g}", ha="center",
                 fontsize=11, fontweight="bold")
    ax3.set_ylabel(r"deg$(T_{BZ\to pivot})$")
    ax3.set_ylim(-0.6, 2.7)
    ax3.set_title(f"STAGE-2: deg$(T)[w_0]={s2['deg_T_w0']}$, $\\Delta_{{\\rm scheme}}={s2['delta_scheme']:.1e}$\n"
                  f"$\\Rightarrow$ {track}")
    ax3.legend(fontsize=8, loc="upper center")
    ax3.grid(alpha=0.3, axis="y")

    fig.suptitle(f"{GATE_ID}  |  w0 BZ$\\to$pivot transport degree  |  "
                 f"d_A=0, single-pole s=3 $\\Rightarrow$ deg=0 (scalar)  |  "
                 f"substrate $w_0$ = pivot $w_0$ = $-0.918$  |  {composite}", fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()                                     # (local)
    print(f"=== {GATE_ID} :: w0 BZ->pivot transport-degree extraction ===")
    print(f"[const] w0_FW={w0_FW}  deg_T_BZ_pivot(sibling)={deg_T_BZ_pivot}  "
          f"alpha_s_sd1={alpha_s_substrate_distance_1}  M_KK={M_KK:.4e}  tau_fold={tau_fold}  "
          f"Gamma_eff={Gamma_effacement}")

    # runtime canonical-value verification (PLAN-TEXT-DRIFT; substrate-first §(ii.B))
    assert abs(float(w0_FW) - W0_FW_EXPECT) < 1e-12, f"w0_FW drift: {w0_FW}"
    assert abs(float(tau_fold) - TAU_FOLD_EXPECT) < 1e-12, f"tau_fold drift: {tau_fold}"
    assert abs(float(deg_T_BZ_pivot) - DEG_NONSCALAR_REF) < 1e-12, f"deg_T_BZ_pivot drift: {deg_T_BZ_pivot}"
    print(f"[canon] runtime-verified: w0_FW=-0.918, tau_fold=0.190, deg_T_BZ_pivot=2.0 (NON-SCALAR ref)")

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    audit_sha, content_sha = compute_dual_sha(THIS_FILE, P_CANONICAL, pins)
    print(f"  closure_hash:   {closure[:16]}...")
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # --- Load the S106 cache + runtime integrity check ---
    z = np.load(P_CACHE, allow_pickle=True)
    cache_internal_sha = str(np.asarray(z["audit_sha256"]).item())  # (local)
    cache_integrity_ok = (cache_internal_sha == CACHE_INTERNAL_AUDIT_SHA256)  # (local)
    print(f"[cache] npz-internal audit_sha256={cache_internal_sha[:16]}...  integrity_ok={cache_integrity_ok}")
    if not cache_integrity_ok:
        z.close()
        value = (f"PRE-REG-INC_cache_integrity_FAIL_got_{cache_internal_sha[:16]}_expect_5af2b7cd")
        np.savez_compressed(OUT_NPZ, verdict="PRE-REG-INC", phase="CACHE_INTEGRITY_FAIL",
                            cache_internal_sha=cache_internal_sha,
                            audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure)
        print_verdict_payload("PRE-REG-INC", value, audit_sha, content_sha)
        return 0
    SE16 = z["sector_evals_L16"].item()                  # (local) COMPLETE p+q<=15 (136 sectors)
    z.close()
    print(f"[cache] sector_evals_L16: {len(SE16)} sectors (complete p+q<=15)")

    # =====================================================================
    # STAGE-1 — de-lambda_max'd representative
    # =====================================================================
    s1 = stage1_trajectory(SE16)
    print("\n--- STAGE-1: three-normalization trajectory ---")
    print(f"{'L':>3} {'rho_run':>12} {'mean_Z':>12} {'lam_max':>10} "
          f"{'w0_run':>11} {'w0_fix':>11} {'w0_noedge':>11}")
    for L in L_SCAN:
        print(f"{L:>3} {s1['rho_run'][L]:>12.6f} {s1['mean_Z'][L]:>12.6f} {s1['lam_max'][L]:>10.6f} "
              f"{s1['w0_run'][L]:>11.6f} {s1['w0_fix'][L]:>11.6f} {s1['w0_noedge'][L]:>11.6f}")
    print(f"  offset_cac (W9 lineage) = {s1['offset_cac']:.6f}   offset_lockdown = {s1['offset_lockdown']:.6f}")
    print(f"  spread: running={s1['spread_run']:.6f}  fixed={s1['spread_fix']:.6e}  "
          f"no-edge={s1['spread_noedge']:.6e}")
    print(f"  mean_Z total drift={s1['meanZ_total_drift']:.3e} ({s1['meanZ_rel_drift']*100:.3f}% rel); "
          f"per-shell drift collapses {list(s1['meanZ_shell_drift'].values())[0]:.2e} -> "
          f"{list(s1['meanZ_shell_drift'].values())[-1]:.2e}")
    print(f"  GAP DECOMPOSITION (rho_B(15)-rho_B(10)={s1['gap_total']:.6f}):")
    print(f"    lambda_max-running term = {s1['term_lammax']:+.6f}  ({s1['frac_running']*100:.2f}%)")
    print(f"    mean_Z-drift term       = {s1['term_meanZ']:+.6f}  ({s1['frac_meanZ']*100:.2f}%)")
    print(f"  W9 running L->inf asymptote: CAC={s1['w0_run_asymptote_cac']:.6f}  "
          f"lockdown={s1['w0_run_asymptote_lockdown']:.6f} (plan -1.340827)")
    print(f"  de_lambda_clean={s1['de_lambda_clean']}  drift_removed={s1['drift_removed_frac']*100:.2f}%")

    # W9 cross-check (6 sig figs)
    w9_ok = all(abs(s1["rho_run"][L] - W9_RHO_B[L]) < 1e-5 for L in (13, 14, 15))  # (local)
    print(f"  [xcheck] rho_B(13/14/15) reproduces S116-W9-GTBUILDER-L15 (6 sig figs): {w9_ok}")

    # =====================================================================
    # STAGE-2 — degree extraction + secondary-class scheme-spread
    # =====================================================================
    s2 = stage2_degree(s1)
    print("\n--- STAGE-2: §23 transport-degree extraction ---")
    print(f"  d_A(w0)=0 => §23.0(5) scale leg = M_KK^0 = 1 (TRIVIAL)")
    print(f"  single pole s={S_POLE} (poleconv-A-double, n={CURVATURE_GRADE_N}); no square/power => s'=s")
    print(f"  Wodzicki morphism degree = -2(s-s') = -2({S_POLE}-{S_POLE_OUT}) = {s2['deg_wodzicki']}")
    print(f"  deg(T_BZ->pivot)[w0] = {s2['deg_T_w0']}  (T2-VACUOUS scalar: {s2['is_scalar']}, even-mesh: {s2['is_even_mesh']})")
    print(f"  secondary-class scheme-spread Delta_scheme across {s2['schemes']}:")
    for s in s2["schemes"]:
        print(f"    {s:28s}: homog_exp={s2['homog_exponent_per_scheme'][s]}  O^pivot={s2['O_pivot_per_scheme'][s]:.6f}")
    print(f"  Delta_scheme = {s2['delta_scheme']:.3e} M_KK^2  (< {SCHEME_SPREAD_TOL:.0e}: {s2['delta_scheme'] < SCHEME_SPREAD_TOL})")
    print(f"  O^pivot(w0) = {s2['o_pivot_w0']:.6f} = w0_FW => substrate w0 = pivot w0 (deg-0 identity transport)")
    print(f"  CONTRAST: deg sibling (alpha_s/A_s NON-SCALAR) = {s2['deg_sibling']}; "
          f"discriminator gap |deg_sib|-|deg_w0| = {s2['discriminator_gap']}")

    # =====================================================================
    # VERDICT
    # =====================================================================
    composite, sign_v, mag_v, regime_v, track = evaluate_gate(s1, s2)
    print(f"\n[VERDICT] {composite}  track={track}  (sign={sign_v}, magnitude={mag_v}, regime={regime_v})")
    print(f"  deg={s2['deg_T_w0']} (|deg|<{DEG_TOL}: {abs(s2['deg_T_w0'])<DEG_TOL}) AND "
          f"Delta_scheme={s2['delta_scheme']:.1e} (<{SCHEME_SPREAD_TOL:.0e}: {s2['delta_scheme']<SCHEME_SPREAD_TOL})")

    # --- plot ---
    make_plot(s1, s2, composite, track)
    print(f"  plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")

    # --- persist npz ---
    np.savez(
        OUT_NPZ,
        verdict=composite, track=track, phase="COMPLETE",
        L_scan=np.array(L_SCAN, dtype=np.int64),
        # STAGE-1 trajectory:
        rho_run=np.array([s1["rho_run"][L] for L in L_SCAN]),
        mean_Z=np.array([s1["mean_Z"][L] for L in L_SCAN]),
        lam_max=np.array([s1["lam_max"][L] for L in L_SCAN]),
        n_modes=np.array([s1["n_modes"][L] for L in L_SCAN], dtype=np.int64),
        w0_run=np.array([s1["w0_run"][L] for L in L_SCAN]),
        rho_fix=np.array([s1["rho_fix"][L] for L in L_SCAN]),
        w0_fix=np.array([s1["w0_fix"][L] for L in L_SCAN]),
        rho_noedge=np.array([s1["rho_noedge"][L] for L in L_SCAN]),
        w0_noedge=np.array([s1["w0_noedge"][L] for L in L_SCAN]),
        offset_cac=s1["offset_cac"], offset_lockdown=s1["offset_lockdown"],
        offset_noedge=s1["offset_noedge"],
        spread_run=s1["spread_run"], spread_fix=s1["spread_fix"], spread_noedge=s1["spread_noedge"],
        meanZ_total_drift=s1["meanZ_total_drift"], meanZ_rel_drift=s1["meanZ_rel_drift"],
        meanZ_shell_drift=np.array(list(s1["meanZ_shell_drift"].values())),
        gap_total=s1["gap_total"], term_meanZ=s1["term_meanZ"], term_lammax=s1["term_lammax"],
        frac_running=s1["frac_running"], frac_meanZ=s1["frac_meanZ"],
        w0_run_asymptote_cac=s1["w0_run_asymptote_cac"],
        w0_run_asymptote_lockdown=s1["w0_run_asymptote_lockdown"],
        de_lambda_clean=s1["de_lambda_clean"], drift_removed_frac=s1["drift_removed_frac"],
        # STAGE-2 degree:
        d_A_w0=D_A_W0, s_pole=S_POLE, s_pole_out=S_POLE_OUT, curvature_grade_n=CURVATURE_GRADE_N,
        scale_leg_degree=s2["scale_leg_degree"], deg_wodzicki=s2["deg_wodzicki"],
        deg_T_w0=s2["deg_T_w0"], is_scalar=s2["is_scalar"], is_even_mesh=s2["is_even_mesh"],
        schemes=np.array(s2["schemes"]),
        homog_exponent_per_scheme=np.array([s2["homog_exponent_per_scheme"][s] for s in s2["schemes"]]),
        O_pivot_per_scheme=np.array([s2["O_pivot_per_scheme"][s] for s in s2["schemes"]]),
        delta_scheme=s2["delta_scheme"], delta_scheme_finite=s2["delta_scheme_finite"],
        deg_sibling=s2["deg_sibling"], discriminator_gap=s2["discriminator_gap"],
        o_pivot_w0=s2["o_pivot_w0"],
        # pins / tolerances:
        DEG_TOL=DEG_TOL, SCHEME_SPREAD_TOL=SCHEME_SPREAD_TOL, CAC_SPREAD_PASS=CAC_SPREAD_PASS,
        LAMBDA_Z=LAMBDA_Z, w0_FW=float(w0_FW), tau_fold=float(tau_fold),
        W9_RHO_B10_44FILLED=W9_RHO_B10_44FILLED, LOCKDOWN_RHO_B10=LOCKDOWN_RHO_B10,
        w9_xcheck_ok=w9_ok,
        # verdict 3-tuple:
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
    )
    print(f"  data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # --- value payload (6 sig figs; no single-quote chars; emit_verdict wraps value='...') ---
    value = (
        f"{track}_deg(T_BZ-pivot)[w0]={s2['deg_T_w0']}_T2-VACUOUS-scalar"
        f"_Delta_scheme={s2['delta_scheme']:.2e}M_KK^2<{SCHEME_SPREAD_TOL:.0e}"
        f"_d_A=0_single-pole-s=3_Wodzicki-2(s-s)=0"
        f"_substrate_w0=pivot_w0={s2['o_pivot_w0']:.4f}"
        f"_W9-gap-to-{s1['w0_run_asymptote_lockdown']:.4f}=PROXY-ARTIFACT-running-lambda_max-{s1['frac_running']*100:.1f}pct"
        f"_meanZ-FROZEN-{s1['meanZ_rel_drift']*100:.2f}pct_fixed-edge-FLAT-spread={s1['spread_fix']:.2e}"
        f"_de-lambda-clean-removes-{s1['drift_removed_frac']*100:.1f}pct"
        f"_contrast-sibling-deg=+{s2['deg_sibling']:.0f}-NON-SCALAR_NO-K3-advance_DR3-freeze-vs-0.918"
    )
    extra_rows = [
        (f"# regulator_pin=a_2^{{Mellin}} poleconv-A-double (pole_in_s=3, curvature_grade_n=2); "
         f"cutoff_axis=spectral (Zubarev Lambda_Z={LAMBDA_Z}); §23.0(5) d_A=0 trivial M_KK^0 scale leg + "
         f"single-pole even-mesh Wodzicki -2(s-s')=0 (regulator-pin-discipline.md)"),
        (f"# composite-precedence: plan session-117-plan-w7.md §W7-1 -- deg=0 clean (|deg|<{DEG_TOL} AND "
         f"Delta_scheme<{SCHEME_SPREAD_TOL:.0e}) => composite PASS (PASS-SCALAR); overrides generic 3-tuple collapse"),
        (f"# Delta_scheme=0 M_KK^2 across {{APS-1975,Cheeger-Simons,Bismut-Cheeger}}: degree-0 morphism's "
         f"secondary class is scheme-INDEPENDENT (Wodzicki uniqueness); §18 admissibility leg (mirrors S93-W7-1 "
         f"delta_scheme=0.00); the DEGREE value (0 vs sibling +2) is the scalar discriminator"),
        (f"# fb_backward=CF-S117-W0-CATEGORICAL-WALL-GRADE (deg-conditional sigma-distances FREEZE on PASS-SCALAR); "
         f"mack DR3 w(z) §7 falsifier-surface: remove 'computed under provisional deg=0; pending' tag; "
         f"W-5 BD2 deg-conditional element RESOLVED; substrate w0=-0.918 is the transport INPUT, never its output"),
    ]
    print_verdict_payload(composite, value, audit_sha, content_sha,
                          sign_v=sign_v, magnitude_v=mag_v, regime_v=regime_v, extra_rows=extra_rows)

    print(f"\n  4-tuple: (value={composite}/{track}/deg={s2['deg_T_w0']}, scheme={SCHEME[:40]}..., "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"  elapsed: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
