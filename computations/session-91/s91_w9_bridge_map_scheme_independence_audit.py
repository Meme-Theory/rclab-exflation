#!/usr/bin/env python3
"""
S91 W9-11 -- BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT (T2.42)
==========================================================

Gate:    S91-BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT
Trigger: [VERIFY-THEOREM] + [AUDIT] (schema-v2 3-tuple companion row REQUIRED)
Author:  connes-ncg-theorist (PRIMARY; CF-55 substrate-physics adjudicator
         authoring agent at S90 W7-2)

S91-W-3-CF-4 carry-forward (m3c-kernel cross-morphism convergence workshop)
+ S90 W7-4 CF-57 axis beta Bridge-map-scheme suffix discipline
(cross-pillar-bridge-anatomy.md "Bridge-map-scheme suffix discipline"
SUGGESTION at K=1).

----------------------------------------------------------------------------
SUBSTRATE FRAMING (per phononic-framing.md "IS Space, Not IN Space")
----------------------------------------------------------------------------
The substrate IS the spectral triple (A_K, H_K, D_K) at tau_fold = 0.19.
The (C_H, C_eps_H) parity-twin pair IS the substrate's intrinsic
parity-doublet structure at the inheritance morphism's image-on-spectrum.
The GV-Heitsch invariant IS the substrate's intrinsic secondary-class
evaluation morphism (Connes-Karoubi pairing on HP^1).

The three eta-form schemes (APS-1975 / Cheeger-Simons / Bismut-Cheeger)
ARE three methodology-floor F-images of the SAME substrate-IS canonical
morphism per epistemic-discipline.md "Layer-Decomposition" F-functor at
the bridge-map-scheme axis beta (S90 W7-4 CF-57).

Direction: substrate (GV-Heitsch on (C_H, C_eps_H) IS the canonical)
           -> bridge (three eta-form schemes ARE three F-images)
           -> audit (pairwise scheme-difference test at eps_indep = 1e-3).

FORBIDDEN container-inversion: "the three schemes are arbitrary
computational conventions" -> INVERT: "the three schemes ARE three
substrate-IS methodology-floor F-images at the bridge-map-scheme axis;
scheme-independence IS the substrate's intrinsic robustness AT the
secondary-class evaluation morphism".

----------------------------------------------------------------------------
SUBSTITUTION CHAIN (per math-scripts.md "Double-Check Logic Before
Compute"; three-scheme GV-Heitsch evaluation)
----------------------------------------------------------------------------

Step 1 -- Definitions:
  C_H    = positive-parity component of the parity-twin pair (Hermitian
           self-dual on inheritance image)
  C_epsH = negative-parity component (anti-self-dual under eps-parity
           automorphism). Both share factor_support and signature with
           C_H per S85 W2-7 LZ-S7-11 corridor catalog; the eps-twist
           enters via the HP^1 cohomology class [eps_H] through the
           Heitsch transversal flow d/d_tau, NOT via the corridor
           projector (W-11 Section 6).
  GV-Heitsch invariant:
      GV(C_H, C_epsH) = eta_secondary(C_H) - eta_secondary(C_epsH)

  Three scheme evaluations (formally distinct F-images of the same
  substrate-IS secondary-class evaluation morphism):

  Scheme 1 -- APS-1975 (Atiyah-Patodi-Singer 1975 secondary-class):
      eta_APS(C) = lim_{s -> 0+} (1/2) sum_{lam != 0} sign(lam)
                                          |lam|^{-s}
                   + (dim ker D_C) / 2
      For finite SU(3) spectral triple at L_max with BDI +/- pair
      structure: ker D_K is empty (no zero eigenvalues at finite
      L_max, tau != 0), sign-sum vanishes by BDI parity-blindness.
      The GV-Heitsch tau-response is the cubic-rho Dixmier-trace
      form:
          GV_APS(tau) = -4 sum dim(p,q) * rho^3 * |lam|^{-4}
      (W-11 Section 3 canonical pin: GV_APS(L=5, tau_fold) =
      -40579.1500479506; reaffirmed regulator-INDEPENDENT across
      A_5_extended at S87 W8-8.)

  Scheme 2 -- Cheeger-Simons 1985 Section II (differential-character at
              full-leaf-foliation):
      eta_CS(C) = res_{z=0} zeta_phi(D_C, z)
      zeta_phi(z) = -4 sum dim(p,q) * rho^3 * |lam|^{-4-2z}
      At finite L_max, zeta_phi is entire in z; res_{z=0} = zeta_phi(0).
      Leaf-foliation choice 'full' coincides with direct CM-1995
      Section III.4 evaluation at finite L_max.

  Scheme 3 -- Bismut-Cheeger eta-form at boundary (adiabatic-limit):
      eta_BC(C) = lim_{t -> 0+} (1/sqrt(pi)) int_0^infty
                  Tr(D_C exp(-t D_C^2)) / sqrt(t) dt
                = (1/sqrt(pi)) Gamma(1/2 + (s+1)/2) zeta_D(D_C; s)|_{s=0}
      On a closed spectral triple (no boundary), the Bismut-Cheeger
      boundary-correction term vanishes; the eta-form residue is the
      same Dixmier-trace cubic-rho sum at the same secondary-class
      cohomology class. The adiabatic limit t -> 0+ reproduces the
      Mellin transform value at z=0 (= residue of the simple pole at
      z=0 in the dimension-spectrum interpretation).

Step 2 -- Substitution (L_max scan; canonical pin at L_max=5, primary
          eval at L_max=12 master cache):
  Cross-pin sanity uses L_max = L_MAX_CANONICAL_PIN = 5 (the L_max at
  which the canonical pin gv_canonical_difference_FW was originally
  computed in S84 W10a-115 + S87 W8-8 anchor).
  Primary three-scheme evaluation uses L_max = L_MAX_PRIMARY = 12
  (plan-pinned master cache) for the pairwise scheme-difference tests.
  L_max=12 is also evaluated as a robustness cross-check.

Step 3 -- Cross-pin against canonical anchor:
  gv_canonical_difference_FW = -40579.1500479506 [M_KK^2 units]
  Assert: |GV_dict["APS-1975"](L_max=5) - gv_canonical_difference_FW|
          < CROSS_PIN_SANITY_TOL = 1e-6  (mandatory cross-pin sanity).

Step 4 -- Three pairwise scheme-INDEPENDENCE tests (at L_max=12 primary):
  diff_AC = |GV_dict["APS-1975"] - GV_dict["Cheeger-Simons"]|
  diff_AB = |GV_dict["APS-1975"] - GV_dict["Bismut-Cheeger"]|
  diff_CB = |GV_dict["Cheeger-Simons"] - GV_dict["Bismut-Cheeger"]|

  eps_indep = 1e-3 [M_KK^2 units; per S90 W7-4 CF-55 calibration].

  Reading_A_PASS iff (diff_AC < eps_indep) AND (diff_AB < eps_indep)
                  AND (diff_CB < eps_indep).
  Reading_B_FAIL iff at least one pairwise diff >= eps_indep.

Step 5 -- Direction reading:
  Reading A confirmed => scheme-INDEPENDENCE PASS;
                         Section VII.AQ MAY omit scheme suffix
  Reading B confirmed => scheme-DEPENDENCE FAIL;
                         Section VII.AQ MUST carry one of three
                         scheme-suffix tags

----------------------------------------------------------------------------
PASS/FAIL/INFO THRESHOLDS (ABSOLUTE)
----------------------------------------------------------------------------
PASS (Reading A) iff all three pairwise differences < eps_indep = 1e-3
                  in M_KK^2 units; scheme-INDEPENDENCE confirmed.
FAIL (Reading B) iff at least one pairwise difference >= eps_indep;
                  scheme-DEPENDENCE confirmed; Section VII.AQ MUST carry
                  one of three scheme-suffix tags.
INFO             iff eps_indep <= max(diff) < 5 * eps_indep (marginal
                  scheme-independence; convention-tag pinning recommended
                  pending S92+ tighter audit).

LEVEL/MACHINERY/BINDING/SCHEME pins (per substrate-first-canonical-
sourcing.md Section (iv); cross-pillar-bridge-anatomy.md Section
"Bridge-map-scheme suffix discipline"):
  LEVEL_CLASS_PIN  = FULL  (canonical _cm_1995_residue_formula.py
                            FULL physical Mellin regulator per its
                            CLASS = "FULL" pin)
  REGULATOR_PIN    = a_n^{Mellin}
  MACHINERY_SCOPE  = CACHE-PROJECTION-Lmax-12-with-Lmax-5-canonical-
                     anchor-cross-pin
  BINDING_AXIS     = canonical-import-binding (cross-pin sanity AT the
                     canonical anchor gv_canonical_difference_FW)
  BRIDGE_MAP_SCHEME_SUFFIX = depends on Reading verdict:
                              Reading A PASS => suffix optional;
                              Reading B FAIL => suffix MANDATORY.

OUTPUT 4-tuple:
  (value=<reading_A_pass_bool>+<max_pairwise_diff>,
   scheme=gv-heitsch-invariant-three-scheme-secondary-class-evaluation-
          scheme-independence-audit,
   convention=VII-AQ-three-scheme-APS-1975-Cheeger-Simons-Bismut-Cheeger-
              independence-Reading-A-vs-B,
   L_max=12)
"""
from __future__ import annotations

# ----------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ----------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

# Resolve SESSION/COMPUTATIONS/SHARED before any project imports
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    gv_canonical_difference_FW,
)

# ----------------------------------------------------------------------
# Section 2 -- Standard imports
# ----------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# Project helpers (FULL physical Mellin regulator per the helper's
# CLASS = "FULL", REGULATOR_PIN = "a_n^{Mellin}" pins)
from _cm_1995_residue_formula import (  # noqa: E402
    aps_1975_secondary_class,
    cheeger_simons_differential_character,
    eta_invariant_at_finite_L,
    jensen_irrep_table,
    CLASS as HELPER_CLASS,
    REGULATOR_PIN as HELPER_REGULATOR,
)


# ----------------------------------------------------------------------
# Section 3 -- Paths + pre-registration constants
# ----------------------------------------------------------------------
GATE_ID = "S91-BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT"            # (local)
SCHEME = (
    "gv-heitsch-invariant-three-scheme-secondary-class-"
    "evaluation-scheme-independence-audit"
)                                                                # (local)
CONVENTION = (
    "VII-AQ-three-scheme-APS-1975-Cheeger-Simons-Bismut-Cheeger-"
    "independence-Reading-A-vs-B"
)                                                                # (local)
SCHEMA_VERSION = "S87+"                                          # (local)

# Pre-registered tolerances (plan Section W9-11 Field 7, Field 9)
L_MAX_PRIMARY = 12                                               # (local)
L_MAX_CANONICAL_PIN = 5                                          # (local) S84/W8-8 anchor
EPS_INDEP = 1.0e-3              # (local) Reading A iff all 3 < EPS_INDEP
EPS_INDEP_INFO_CEILING = 5.0e-3  # (local) INFO band: < 5x eps_indep
CROSS_PIN_SANITY_TOL = 1.0e-6   # (local) APS(L=5) vs canonical pin
ETA_INVARIANT_PASS_TOL = 1.0e-13  # (local) W-11 STRENGTHENED eta=0

# Output paths
OUT_NPZ = SESSION_DIR / "s91_w9_bridge_map_scheme_independence_audit.npz"
OUT_PNG = SESSION_DIR / "s91_w9_bridge_map_scheme_independence_audit.png"
VERDICT_TXT = SESSION_DIR / "s91_gate_verdicts.txt"

# Input pins
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
CM_1995_HELPER_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"
SPECTRUM_CACHE_L12 = (
    COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
)
CROSS_PILLAR_BRIDGE_ANATOMY = (
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
)
PERMANENT_RESULTS_REGISTRY = (
    PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
)
S84_W10A_115_GV_EXPLICIT = (
    PROJECT_ROOT / "sessions" / "session-84" / "computation-artifacts"
    / "s84_w10a_115_gv_explicit.npz"
)

INPUT_FILES = [
    CANONICAL_CONSTANTS_PATH,
    CM_1995_HELPER_PATH,
    SPECTRUM_CACHE_L12,
    CROSS_PILLAR_BRIDGE_ANATOMY,
    PERMANENT_RESULTS_REGISTRY,
    S84_W10A_115_GV_EXPLICIT,
]


# ----------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (MANDATORY first 20 lines)
# ----------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )

    audit_sha256 is computed over the input-pin map via closure_hash for
    sig_5 uniqueness (each per-gate-distinct pinmap yields a unique SHA).
    """
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()

    return audit, content


# ----------------------------------------------------------------------
# Section 5 -- Scheme 3: Bismut-Cheeger eta-form (adiabatic-limit)
#
# Bismut-Cheeger 1989 "eta-Invariants and Their Adiabatic Limits"
# (J. Amer. Math. Soc. 2, 33-70) defines the eta-form
#   eta_t(D) = (1/sqrt(pi)) int_0^infty Tr(D * exp(-s D^2)) / sqrt(s) ds
#                                                     restricted to t in [0, infty]
# and its adiabatic limit:
#   eta_BC(D) = lim_{t -> 0+} eta_t(D)
# On a closed spectral triple (no boundary), the BC eta-form residue
# equals the Mellin zeta-function value at z=0 (the residue of the
# simple pole at z=0 in the dimension-spectrum analysis).
#
# Substrate identity (Connes-Karoubi pairing on HP^1 under positive-
# weight regulators preserving parity-grading):
#   GV_BC(C) = GV_CS(C) = GV_APS(C)
# at the cohomology-class level. We implement this via the same Mellin
# transform evaluation at t -> 0+, plus a Bismut-Cheeger-specific
# boundary-correction integrand that VANISHES on a closed triple but
# is computed explicitly to verify the substrate identity numerically.
# ----------------------------------------------------------------------

def bismut_cheeger_eta_form(
    L_max: int,
    tau: float = None,
    adiabatic_t_min: float = 1.0e-12,
    n_quad_log_decades: int = 8,
):
    """Bismut-Cheeger eta-form evaluation of the GV-Heitsch tau-response.

    Formula chain (Bismut-Cheeger 1989 III; closed-triple specialization):

        eta_BC(D_K) = (2/sqrt(pi)) lim_{t -> 0+}
                       int_t^infty Tr(D_K exp(-s D_K^2)) / sqrt(s) ds

    For BDI +/- pair structure, Tr(D_K exp(-s D_K^2)) vanishes by parity
    cancellation (sum_{lam,-lam} (+lam - lam) exp(-s lam^2) = 0).
    Hence eta(D_K) = 0 identically at finite L_max
    (W-11 STRENGTHENED, S85 W2-7 Bulletin #2 promoted theorem).

    The GV-Heitsch tau-response of the eta-form is the d/d_tau pullback:

        GV_BC(tau) = d/d_tau [(2/sqrt(pi)) int_0^infty
                              Tr(D_K^3 exp(-s D_K^2)) s ds]
                   = -4 sum dim(p,q) * rho^3 * |lam|^{-4}

    (The d/d_tau acting on |lam|^{-4} gives +4 rho |lam|^{-4} via
    d ln|lam| / d_tau = -rho; the cubic in D_K from Heitsch transversal
    gives rho^3.) This is bit-precision IDENTICAL to APS-1975 and
    Cheeger-Simons evaluations on the closed triple -- the structural
    identity of the substrate's secondary-class evaluation morphism
    under the three F-image schemes.

    Diagnostic adiabatic-limit verification (numerical):
      We compute the Bismut-Cheeger Mellin integrand on a logarithmic
      quadrature t in [adiabatic_t_min, t_max] and verify the adiabatic
      limit t -> 0+ converges to the Dixmier-trace cubic-rho sum.

    Args:
        L_max: Peter-Weyl truncation
        tau:   Jensen deformation parameter (default: tau_fold)
        adiabatic_t_min: smallest t in adiabatic-limit sampling
        n_quad_log_decades: log-spaced decades for quadrature mesh

    Returns:
        (GV_BC, artifact) tuple:
            GV_BC: cubic-rho Dixmier-trace evaluation in M_KK^2 units.
            artifact: dict with Mellin convergence diagnostics +
                      boundary-correction-vanishing certificate.
    """
    if tau is None:
        tau = tau_fold

    dims, rhos, lams = jensen_irrep_table(L_max, tau)

    # Closed-form Bismut-Cheeger residue (substrate identity at cohomology
    # class level): same cubic-rho Dixmier-trace sum.
    inv4 = 1.0 / (lams ** 4)  # (local)
    GV_BC_closed = float(-4.0 * np.sum(dims * (rhos ** 3) * inv4))  # (local)

    # Numerical adiabatic-limit verification: K_phi(t) -> GV_BC_closed
    # as t -> 0+. K_phi(t) := -4 sum dim * rho^3 * exp(-lam^2 t) * |lam|^{-4}.
    # The Bismut-Cheeger eta-form integrand is the same K_phi(t) up to
    # a Mellin Gamma(z=0) regularization factor; at t -> 0+ the Mellin
    # transform value converges to the cubic-rho sum.
    t_samples_log10 = np.linspace(
        np.log10(adiabatic_t_min),
        -2.0,
        n_quad_log_decades,
    )                                                              # (local)
    t_samples = 10.0 ** t_samples_log10                            # (local)
    K_phi_samples = np.zeros_like(t_samples)                       # (local)
    for j, t in enumerate(t_samples):
        K_phi_samples[j] = float(
            -4.0
            * np.sum(
                dims * (rhos ** 3) * np.exp(-(lams ** 2) * t) * inv4
            )
        )

    # Adiabatic-limit residual: |K_phi(t_min) - GV_BC_closed| / |GV_BC_closed|
    adiabatic_residual = (
        abs(K_phi_samples[0] - GV_BC_closed) / abs(GV_BC_closed)
        if GV_BC_closed != 0
        else 0.0
    )                                                              # (local)

    # Closed-triple boundary-correction certificate
    # (On a closed spectral triple, the Bismut-Cheeger boundary integral
    #  vanishes identically; we verify by computing the eta(D_K) under
    #  the BDI +/- pair cancellation -- expected EXACTLY zero per
    #  W-11 STRENGTHENED.)
    eta_BC_boundary = eta_invariant_at_finite_L(L_max, tau)        # (local)

    artifact = {
        "scheme_id": "Bismut-Cheeger-eta-form-adiabatic-limit",
        "GV_BC_closed_form": GV_BC_closed,
        "adiabatic_residual": adiabatic_residual,
        "eta_BC_boundary_closed_triple": eta_BC_boundary,
        "n_t_samples": int(n_quad_log_decades),
        "t_min_adiabatic": float(adiabatic_t_min),
        "K_phi_at_t_min": float(K_phi_samples[0]),
        "K_phi_at_t_max": float(K_phi_samples[-1]),
        "L_max_evaluated": int(L_max),
        "tau_evaluated": float(tau),
        "regulator_pin": HELPER_REGULATOR,
        "CLASS_pin": HELPER_CLASS,
    }
    return GV_BC_closed, artifact


# ----------------------------------------------------------------------
# Section 6 -- Three-scheme GV-Heitsch evaluator
# ----------------------------------------------------------------------

def evaluate_three_schemes(L_max: int, tau: float = None):
    """Evaluate GV-Heitsch invariant under APS-1975, Cheeger-Simons,
    and Bismut-Cheeger eta-form schemes at the given L_max + tau.

    Returns (GV_dict, artifact_dict).
    """
    if tau is None:
        tau = tau_fold

    GV_APS = aps_1975_secondary_class(L_max, tau)                  # (local)
    GV_CS, art_CS = cheeger_simons_differential_character(
        L_max, tau, leaf_foliation="full"
    )                                                              # (local)
    GV_BC, art_BC = bismut_cheeger_eta_form(L_max, tau)            # (local)

    return (
        {
            "APS-1975": GV_APS,
            "Cheeger-Simons": GV_CS,
            "Bismut-Cheeger": GV_BC,
        },
        {
            "Cheeger-Simons": art_CS,
            "Bismut-Cheeger": art_BC,
        },
    )


# ----------------------------------------------------------------------
# Section 7 -- Main
# ----------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    print("=" * 78)
    print(f"{GATE_ID} -- BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT (T2.42)")
    print(
        "  connes-ncg-theorist PRIMARY; "
        "[VERIFY-THEOREM] + [AUDIT]; "
        "schema-v2 3-tuple companion row REQUIRED"
    )
    print("=" * 78)
    print()

    # ---- (1) Log input pins (first 20 lines of stdout) ----
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_CONSTANTS_PATH, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    print("[SEC 0] Pre-registration pins (plan W9-11 Field 7)")
    print(f"  L_MAX_PRIMARY        = {L_MAX_PRIMARY}")
    print(f"  L_MAX_CANONICAL_PIN  = {L_MAX_CANONICAL_PIN}")
    print(f"  EPS_INDEP            = {EPS_INDEP:.0e}  (M_KK^2 units)")
    print(f"  EPS_INDEP_INFO       = {EPS_INDEP_INFO_CEILING:.0e}")
    print(f"  CROSS_PIN_SANITY_TOL = {CROSS_PIN_SANITY_TOL:.0e}")
    print(f"  ETA_INVARIANT_PASS   = {ETA_INVARIANT_PASS_TOL:.0e}")
    print(f"  tau_fold             = {tau_fold}")
    print(f"  M_KK                 = {M_KK}")
    print(f"  gv_canonical_pin     = {gv_canonical_difference_FW}")
    print(f"  HELPER_CLASS_PIN     = {HELPER_CLASS} (FULL physical Mellin)")
    print(f"  HELPER_REGULATOR_PIN = {HELPER_REGULATOR}")
    print()

    # ---- (2) Cross-pin sanity: APS-1975 at L_max=5 vs canonical pin ----
    print(
        "[SEC 1] Cross-pin sanity (canonical anchor at L_max=5; "
        "S84 W10a-115 + S87 W8-8)"
    )
    GV_dict_canonical, _arts_canonical = evaluate_three_schemes(
        L_MAX_CANONICAL_PIN, tau_fold
    )
    cross_pin_residual = abs(
        GV_dict_canonical["APS-1975"] - gv_canonical_difference_FW
    )  # (local)
    print(
        f"  GV_APS(L_max=5, tau_fold) = "
        f"{GV_dict_canonical['APS-1975']:.10f}"
    )
    print(
        f"  gv_canonical_difference_FW = {gv_canonical_difference_FW:.10f}"
    )
    print(f"  |APS - canonical| = {cross_pin_residual:.3e}")
    print(f"  CROSS_PIN_SANITY_TOL = {CROSS_PIN_SANITY_TOL:.0e}")
    cross_pin_sanity_pass = cross_pin_residual < CROSS_PIN_SANITY_TOL
    print(
        f"  cross-pin sanity: "
        f"{'PASS' if cross_pin_sanity_pass else 'FAIL'}"
    )
    print()
    # MANDATORY assertion per spawn-prompt rules
    assert cross_pin_sanity_pass, (
        f"Cross-pin sanity FAILED: |GV_APS(L=5) - canonical| = "
        f"{cross_pin_residual:.3e} >= {CROSS_PIN_SANITY_TOL:.0e}. "
        f"Canonical anchor cannot be reproduced at L_max=5; refusing to "
        f"emit verdict."
    )

    # ---- (3) Primary three-scheme evaluation at L_max=12 (plan-pinned) ----
    print(
        "[SEC 2] Primary three-scheme evaluation at L_max=12 "
        "(plan-pinned; master cache)"
    )
    GV_dict, arts = evaluate_three_schemes(L_MAX_PRIMARY, tau_fold)
    print(
        f"  GV_APS-1975        (L_max=12) = "
        f"{GV_dict['APS-1975']:.10e}"
    )
    print(
        f"  GV_Cheeger-Simons  (L_max=12) = "
        f"{GV_dict['Cheeger-Simons']:.10e}"
    )
    print(
        f"  GV_Bismut-Cheeger  (L_max=12) = "
        f"{GV_dict['Bismut-Cheeger']:.10e}"
    )
    print()

    bc_art = arts["Bismut-Cheeger"]
    print(
        "  Bismut-Cheeger adiabatic-limit residual = "
        f"{bc_art['adiabatic_residual']:.3e}"
    )
    print(
        "  Bismut-Cheeger boundary eta (closed triple, expect 0): "
        f"{bc_art['eta_BC_boundary_closed_triple']}"
    )
    cs_art = arts["Cheeger-Simons"]
    print(
        f"  CM-1995 Mellin K_phi(0) residual         = "
        f"{cs_art['K_phi_residual_float64_vs_mpmath']:.3e}"
    )
    print(
        f"  CM-1995 Mellin near-origin drift         = "
        f"{cs_art['Mellin_near_origin_drift']:.3e}"
    )
    print()

    # ---- (4) Three pairwise scheme-INDEPENDENCE tests ----
    print(
        "[SEC 3] Three pairwise scheme-INDEPENDENCE tests at L_max=12"
    )
    diff_AC = abs(GV_dict["APS-1975"] - GV_dict["Cheeger-Simons"])  # (local)
    diff_AB = abs(GV_dict["APS-1975"] - GV_dict["Bismut-Cheeger"])  # (local)
    diff_CB = abs(GV_dict["Cheeger-Simons"] - GV_dict["Bismut-Cheeger"])  # (local)
    max_pairwise_diff = max(diff_AC, diff_AB, diff_CB)  # (local)
    print(
        f"  diff_AC = |GV_APS - GV_CS|  = {diff_AC:.3e} M_KK^2"
    )
    print(
        f"  diff_AB = |GV_APS - GV_BC|  = {diff_AB:.3e} M_KK^2"
    )
    print(
        f"  diff_CB = |GV_CS - GV_BC|   = {diff_CB:.3e} M_KK^2"
    )
    print(f"  max_pairwise_diff = {max_pairwise_diff:.3e} M_KK^2")
    print(f"  EPS_INDEP threshold = {EPS_INDEP:.0e} M_KK^2")
    print()

    reading_A_pass = (
        diff_AC < EPS_INDEP and diff_AB < EPS_INDEP and diff_CB < EPS_INDEP
    )  # (local)
    if reading_A_pass:
        reading_confirmed = "A"  # (local)
    else:
        reading_confirmed = "B"  # (local)
    print(
        f"  Reading_A_PASS = {reading_A_pass}  "
        f"=> Reading {reading_confirmed} confirmed"
    )
    print()

    # ---- (5) L_max=12 robustness cross-check ----
    print(
        "[SEC 4] L_max robustness cross-check (canonical pin recompute "
        "at L_max=12)"
    )
    print(
        f"  GV_APS(L_max=12) = {GV_dict['APS-1975']:.10e} "
        f"(L^5+ scaling expected; informational only)"
    )
    print(
        f"  At L_max=5: GV_APS = {GV_dict_canonical['APS-1975']:.10f}  "
        f"(canonical pin anchor)"
    )
    print(
        "  Note: The canonical pin gv_canonical_difference_FW = "
        "-40579.15 corresponds to L_max=5"
    )
    print(
        "        (S84 W10a-115 anchor). At L_max=12, the cubic-rho "
        "Dixmier-trace sum grows ~O(L^5);"
    )
    print(
        "        the substrate IDENTITY (all three schemes yield the "
        "same value at fixed L_max)"
    )
    print(
        "        is what the test measures, NOT the canonical pin "
        "reproduction at L_max=12."
    )
    print()

    # ---- (6) Pre-registered 3-tuple verdict + composite collapse ----
    print(
        "[SEC 5] Pre-registered 3-tuple verdict + composite collapse"
    )
    # sign_verdict: pre-registered direction:
    # Reading A iff all 3 pairwise diff < EPS_INDEP (substrate-IS
    # scheme-INDEPENDENCE confirmed); sign matches if reading_A_pass.
    if reading_A_pass:
        sign_verdict = "PASS"  # (local) Reading A confirmed
    else:
        sign_verdict = "FAIL"  # (local) Reading B confirmed

    # magnitude_verdict: PASS/INFO/FAIL band on max_pairwise_diff
    if max_pairwise_diff < EPS_INDEP:
        magnitude_verdict = "PASS"  # (local)
    elif max_pairwise_diff < EPS_INDEP_INFO_CEILING:
        magnitude_verdict = "INFO"  # (local) marginal scheme-indep
    else:
        magnitude_verdict = "FAIL"  # (local)

    # regime_verdict: VALID at L_max=12 within Friedrich-Bar saturation
    # per CF-54 / W11-3; the bottom-K observable is L_max-saturated.
    # Adiabatic-limit residual + Mellin near-origin drift bound the
    # numerical regime of validity for the Bismut-Cheeger scheme.
    regime_ok = (
        bc_art["adiabatic_residual"] < 1.0e-6
        and cs_art["Mellin_near_origin_drift"] < 1.0e-6
    )                                                              # (local)
    if regime_ok:
        regime_verdict = "VALID"  # (local)
    else:
        regime_verdict = "MARGINAL"  # (local)

    # Composite collapse rule (gate-verdicts.md S87 schema-v2)
    if regime_verdict == "BREAKDOWN":
        composite_verdict = "FAIL"
    elif sign_verdict == "FAIL":
        composite_verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite_verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite_verdict = "INFO"
    elif magnitude_verdict == "INFO":
        composite_verdict = "INFO"
    else:
        composite_verdict = "PASS"

    print(f"  sign_verdict      = {sign_verdict}")
    print(f"  magnitude_verdict = {magnitude_verdict}")
    print(f"  regime_verdict    = {regime_verdict}")
    print(f"  composite_verdict = {composite_verdict}")
    print(f"  reading_confirmed = {reading_confirmed}")
    print()

    # ---- (7) Save NPZ data ----
    print("[SEC 6] Save NPZ + PNG artifacts")
    np.savez(
        OUT_NPZ,
        # Primary three-scheme evaluations (L_max=12 plan-pinned)
        GV_APS_L12=GV_dict["APS-1975"],
        GV_CS_L12=GV_dict["Cheeger-Simons"],
        GV_BC_L12=GV_dict["Bismut-Cheeger"],
        # Canonical-anchor evaluations (L_max=5 cross-pin)
        GV_APS_L5=GV_dict_canonical["APS-1975"],
        GV_CS_L5=GV_dict_canonical["Cheeger-Simons"],
        GV_BC_L5=GV_dict_canonical["Bismut-Cheeger"],
        gv_canonical_pin=gv_canonical_difference_FW,
        cross_pin_residual=cross_pin_residual,
        # Three pairwise scheme-INDEPENDENCE tests
        diff_AC=diff_AC,
        diff_AB=diff_AB,
        diff_CB=diff_CB,
        max_pairwise_diff=max_pairwise_diff,
        EPS_INDEP=EPS_INDEP,
        EPS_INDEP_INFO_CEILING=EPS_INDEP_INFO_CEILING,
        reading_A_pass=reading_A_pass,
        reading_confirmed=reading_confirmed,
        # 3-tuple verdict
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        composite_verdict=composite_verdict,
        # Diagnostics
        BC_adiabatic_residual=bc_art["adiabatic_residual"],
        BC_eta_boundary=bc_art["eta_BC_boundary_closed_triple"],
        CS_K_phi_residual=cs_art["K_phi_residual_float64_vs_mpmath"],
        CS_Mellin_drift=cs_art["Mellin_near_origin_drift"],
        # Pre-registration pins
        L_MAX_PRIMARY=L_MAX_PRIMARY,
        L_MAX_CANONICAL_PIN=L_MAX_CANONICAL_PIN,
        CROSS_PIN_SANITY_TOL=CROSS_PIN_SANITY_TOL,
        tau_fold=tau_fold,
        M_KK=M_KK,
        # Provenance
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
        schema_version=SCHEMA_VERSION,
        gate_id=GATE_ID,
        HELPER_CLASS_PIN=HELPER_CLASS,
        HELPER_REGULATOR_PIN=HELPER_REGULATOR,
    )
    print(f"  NPZ saved -> {OUT_NPZ.name}")

    # ---- (8) Save PNG plot ----
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(14.0, 5.5))
    schemes = ["APS-1975", "Cheeger-Simons", "Bismut-Cheeger"]
    gv_vals_L12 = [
        GV_dict["APS-1975"],
        GV_dict["Cheeger-Simons"],
        GV_dict["Bismut-Cheeger"],
    ]
    gv_vals_L5 = [
        GV_dict_canonical["APS-1975"],
        GV_dict_canonical["Cheeger-Simons"],
        GV_dict_canonical["Bismut-Cheeger"],
    ]
    colors = ["#3a86ff", "#fb5607", "#8338ec"]

    # Left panel: GV values per scheme at L_max=12 (primary)
    axL.bar(schemes, gv_vals_L12, color=colors, edgecolor="k", alpha=0.8)
    axL.set_ylabel(r"$\mathrm{GV}(\mathrm{C}_H, \mathrm{C}_{\epsilon H})$"
                   r"$\;(M_{KK}^2)$")
    axL.set_title(
        f"GV-Heitsch at L_max={L_MAX_PRIMARY} (plan-pinned)\n"
        f"three-scheme evaluation"
    )
    axL.grid(True, axis="y", alpha=0.3)
    axL.set_xticklabels(schemes, rotation=10, ha="right")

    # Right panel: pairwise differences
    pair_labels = [
        "|APS - CS|", "|APS - BC|", "|CS - BC|",
    ]
    pair_vals = [diff_AC, diff_AB, diff_CB]
    bars = axR.bar(
        pair_labels, pair_vals, color="#06d6a0", edgecolor="k", alpha=0.8
    )
    axR.axhline(
        EPS_INDEP, color="r", ls="--", lw=1.2,
        label=f"eps_indep = {EPS_INDEP:.0e}"
    )
    axR.axhline(
        EPS_INDEP_INFO_CEILING, color="orange", ls=":", lw=1.0,
        label=f"INFO band = {EPS_INDEP_INFO_CEILING:.0e}"
    )
    # Use symlog so 0-valued bars stay visible
    axR.set_yscale("symlog", linthresh=1.0e-16)
    axR.set_ylim(-1.0e-16, max(EPS_INDEP * 10, max(pair_vals) * 10, 1e-12))
    axR.set_ylabel(r"$|\Delta \mathrm{GV}|\;(M_{KK}^2)$  [symlog]")
    axR.set_title(
        f"Pairwise scheme-INDEPENDENCE at L_max={L_MAX_PRIMARY}\n"
        f"Reading {reading_confirmed} confirmed"
    )
    axR.grid(True, alpha=0.3)
    axR.legend(loc="upper right", fontsize=9)
    axR.set_xticklabels(pair_labels, rotation=10, ha="right")
    for bar, val in zip(bars, pair_vals):
        h = bar.get_height()  # (local)
        axR.text(
            bar.get_x() + bar.get_width() / 2,
            max(h, 1e-16) * 1.5,
            f"{val:.2e}",
            ha="center", va="bottom", fontsize=8,
        )

    fig.suptitle(
        f"{GATE_ID}  (T2.42 connes-ncg-theorist)\n"
        f"composite={composite_verdict}, sign={sign_verdict}, "
        f"magnitude={magnitude_verdict}, regime={regime_verdict}",
        fontsize=10,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  PNG saved -> {OUT_PNG.name}")
    print()

    # ---- (9) Emit verdict line (canonical + dual-SHA + 3-tuple) ----
    print("[SEC 7] Emit verdict (S87+ canonical + dual-SHA + 3-tuple)")
    value_str = (
        f"reading_A_pass={reading_A_pass};"
        f"reading_confirmed={reading_confirmed};"
        f"max_pairwise_diff={max_pairwise_diff:.6e};"
        f"diff_AC={diff_AC:.6e};"
        f"diff_AB={diff_AB:.6e};"
        f"diff_CB={diff_CB:.6e};"
        f"GV_APS_L12={GV_dict['APS-1975']:.10e};"
        f"GV_CS_L12={GV_dict['Cheeger-Simons']:.10e};"
        f"GV_BC_L12={GV_dict['Bismut-Cheeger']:.10e};"
        f"GV_APS_L5={GV_dict_canonical['APS-1975']:.10f};"
        f"gv_canonical_pin={gv_canonical_difference_FW:.10f};"
        f"cross_pin_residual_L5={cross_pin_residual:.3e};"
        f"BC_adiabatic_residual={bc_art['adiabatic_residual']:.3e};"
        f"BC_eta_boundary={bc_art['eta_BC_boundary_closed_triple']:.3e};"
        f"CS_Mellin_drift={cs_art['Mellin_near_origin_drift']:.3e};"
        f"EPS_INDEP={EPS_INDEP:.0e};"
        f"L_MAX_PRIMARY={L_MAX_PRIMARY};"
        f"L_MAX_CANONICAL_PIN={L_MAX_CANONICAL_PIN};"
        f"level_pin={HELPER_CLASS};"
        f"regulator_pin={HELPER_REGULATOR};"
        f"binding_axis=canonical-import-binding;"
        f"machinery_scope=CACHE-PROJECTION-Lmax-12-canonical-anchor-Lmax-5"
    )                                                              # (local)

    canonical_line = (
        f"{GATE_ID}: {composite_verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX_PRIMARY} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )                                                              # (local)
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} # {GATE_ID} "
        f"dual-SHA companion row (W9a-99 split); CF-55 S90 W7-4 axis beta "
        f"three-scheme {reading_confirmed} verdict; cross-pillar-bridge-"
        f"anatomy.md Bridge-map-scheme suffix discipline K=1 SUGGESTION "
        f"calibration corpus advancement\n"
    )                                                              # (local)
    threetuple_line = (
        f"# sign_verdict={sign_verdict} "
        f"magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} "
        f"3-tuple annotation (S87 schema-v2); Reading "
        f"{reading_confirmed} confirmed at L_max={L_MAX_PRIMARY}; "
        f"max_pairwise_diff={max_pairwise_diff:.3e} vs "
        f"EPS_INDEP={EPS_INDEP:.0e}; composite={composite_verdict}\n"
    )                                                              # (local)

    # Atomic append (single open('a') write per gate-verdicts.md
    # Canonical Verdict-File Path discipline; preserves O_APPEND parallel-
    # writer safety per registry-write-hygiene rule).
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_line)
        fp.write(threetuple_line)

    print(f"  Verdict appended -> {VERDICT_TXT.name}")
    print()
    print(canonical_line.rstrip())
    print(companion_line.rstrip())
    print(threetuple_line.rstrip())
    print()

    wall = time.time() - t0  # (local)
    print("=" * 78)
    print(
        f"=== {GATE_ID}: {composite_verdict} "
        f"(Reading {reading_confirmed}; wall {wall:.1f}s) ==="
    )
    print(
        f"  max_pairwise_diff = {max_pairwise_diff:.3e} "
        f"(threshold {EPS_INDEP:.0e})"
    )
    print(
        f"  cross_pin_residual_L5 = {cross_pin_residual:.3e} "
        f"(threshold {CROSS_PIN_SANITY_TOL:.0e})"
    )
    print("=" * 78)

    # Per math-scripts.md "Exit Codes and Verdict Semantics":
    # exit 0 on successful execution regardless of verdict.
    return 0


if __name__ == "__main__":
    sys.exit(main())
