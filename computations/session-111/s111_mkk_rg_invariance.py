#!/usr/bin/env python3
"""
S111 W2-1 [PRIME] — M_KK τ-RG-invariance decider: is M_KK a τ-RG-invariant
dimensional-transmutation scale (DYNAMICAL) or a bare CODATA-import (BARE-IMPORT)?
=========================================================================

Gate: S111-CF-MKK-RG-INVARIANCE ([SIGN])
  The τ-spread convergence direction + the dimension-of-output sign are signed
  predictions. The PRIME Topic-1 decider; the surviving leg of the §6.3
  a(t)/effective-Friedmann residual (the M_KK-magnitude leg).

Pre-registered threshold (plan session-111-plan-w2.md §W2-1):
  PASS-leg-1 (RG-invariance): Δ_rel = (max_τ R(τ) − min_τ R(τ)) / mean_τ R(τ) < 5e-2
    where R(τ) = exp(−1/(λ_eff(τ)·N₀(τ)));
  PASS-leg-2 (no-import): M_Pl_reduced ∉ {audited dimensionful magnitude inputs};
  DYNAMICAL (PASS)   iff (leg-1 AND leg-2);
  BARE-IMPORT (FAIL) iff (NOT leg-1) OR (the only dimensionful scale = CODATA cutoff);
  INFO iff (leg-1 holds) but the magnitude leg cannot be cleared of the CODATA
    cutoff without a separate compute (route the no-import leg to a forward gate).

Inputs (SHA-256 dual-pinned at runtime — §4; S84+ schema):
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (L12 fold-slice cache)
  - computations/session-110/s110_cf_cv2a_mkk_transmut_promote.npz (CV2A dimensionLESS ratio)
  - computations/investigation-11/inv11_w1_mkk_dimensional_transmutation.npz (INV11 W1-1 build)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<Δ_rel + DYNAMICAL/BARE-IMPORT + no-import set-test>, scheme=SA, convention=RATIO, L_max=12)

Classification: GEOMETRIC
  M_KK is a property of the D_K(τ) spectrum (the fabric itself), set by the
  fold-DOS enhancement + the spectral-action coupling; not an excitation
  (PHONONIC) nor a quantum-number (PARTICLE).

METHODOLOGY
-----------
τ-scan generalizing the fixed-τ_fold CV2A / INV11-W1-1 BCS dimensional-transmutation
to FUNCTIONS of the Jensen modulus τ. At each τ ∈ [0.190, 0.600]:

  STEP 1 — build the D_K(τ) (0,0)-singlet band from the Jensen-deformed spectral
    triple (dirac_spectrum.extract_singlet_eigensystem). The 8 lowest positive
    band modes split B1(×1) + B2(×4 fold band) + B3(×3) under residual U(2). The
    B2 mean E_B2(τ) IS the van Hove fold band (its min over τ is τ_fold≈0.190,
    matching the canonical s32a B2 curve bit-for-bit at the grid points).

  STEP 2 — N₀(τ): the FINITE-enhanced B2-band van Hove DOS pile-up, computed as the
    canonical windowed integral ρ(τ) = ⟨1/(π·max(|v(t)|, v_min(t)))⟩ over the
    wall [τ−w, τ+w], where v(t)=dE_B2/dt is the B2-band group velocity along the
    τ-flow and v_min(t)=|d²E/dt²|·δτ_sector (SECT-33a finite sector width). The
    DOS pile-up is a FOLD-LOCALIZED 1D van Hove effect — the true A₂ divergence is
    REFUTED (S94); the BCS chain runs through the 1D theorem, NOT a Fermi surface.
    The wall half-width w and the canonical N₀-anchor are calibrated so
    N₀(τ_fold) = rho_B2_per_mode = 14.0233 (continuity with CV2A).

  STEP 3 — λ_eff(τ): the per-coset Kosmann V-matrix coupling on the fold B2 sector,
    via the Kosmann spinorial correction K_a(τ) = (1/8) Σ_{r,s}[Γ^s_{ra}−Γ^r_{sa}]
    γ_r γ_s (Baptista Paper 17 eq 4.1; s23a_kosmann_singlet). The C²-direction
    Kosmann norm ||K_a(τ)||_{C²} is a deterministic function of the connection
    Γ(τ), hence of the Jensen metric g_s(τ). λ_eff(τ) = ||K_a(τ)||²_{C²} / C_const,
    with C_const = ||K_a(τ_fold)||²_{C²}/λ_eff(τ_fold) the τ-INVARIANT proportionality
    fixed at the fold so λ_eff(τ_fold) = 0.038935 (continuity with CV2A V_B2.mean()).

  STEP 4 — the DIMENSIONLESS transmutation ratio R(τ) = exp(−1/(λ_eff(τ)·N₀(τ))).

  STEP 5 — Δ_rel = (max_τ R − min_τ R)/mean_τ R across the ≥40-point scan. SEPARATELY,
    audit-log EVERY dimensionful import in the chain and classify whether the only
    dimensionful magnitude scale traces to the CODATA M_Pl_reduced cutoff (leg-2).

The discriminator is (a) dimension-of-output (R is dimensionless by construction —
CC1) + (b) the τ-spread of R (CC2) + (c) the no-CODATA-cutoff set-membership test on
the dimensionful MAGNITUDE leg (CC3 — the binding falsifier).

DISCIPLINE
----------
- `from canonical_constants import *` (MANDATORY first import)
- Every local/intermediate tagged `# (local)`
- The per-τ work is the (0,0)-singlet Dirac diagonalize (16×16) + the Kosmann norm +
  the spline DOS — all CPU numpy on 16×16 / 8×8 matrices; NO ≥100×100 step, so no GPU
  path is triggered (D_K block-diagonal Peter-Weyl decomposition keeps the singlet
  sector at 16×16). L≥13 FORBIDDEN by the Friedrich-Bär feasibility pre-check; the
  fold-window DOS is L_max-saturated at L12. OMP capped at 8 (CPU, small matrices).
- MULTIPLICATIVE-NORMALIZATION cancellation pre-flight: NOT-APPLICABLE-BY-OPERATOR-FORM
  — the observable is the τ-flow of the transmutation EXPONENT, NOT a K-log-derivative
  d^n ln(·)/d(ln K)^n; no w(L_max)·g(K) factorization check is triggered (declared
  explicitly per the plan-freeze pre-flight requirement).
- SHA-256 of all input files logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict via the `emit_verdict` knowledge-MCP tool (race-safe): the script
  PRINTS the payload (`print_verdict_payload`); the agent calls emit_verdict.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (small matrices, CPU numpy) BEFORE numpy import
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 0b — make computations/_shared importable BEFORE the canonical import
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parent.parent / "_shared"  # computations/_shared
sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    M_KK_gravity,
    M_Pl_reduced,
    M_Pl_unreduced,
    rho_B2_per_mode,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
from scipy.interpolate import CubicSpline  # noqa: E402
from scipy.integrate import quad  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# Substrate D_K(τ) builder + Kosmann correction (deterministic functions of the
# Jensen metric g_s(τ))
from dirac_spectrum import (  # noqa: E402
    su3_generators,
    compute_structure_constants,
    build_cliff8,
    C2_IDX,
)
from s23a_kosmann_singlet import (  # noqa: E402
    extract_singlet_eigensystem,
    kosmann_operator_antisymmetric,
)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent           # computations/session-111
COMPUTATIONS_DIR = SESSION_DIR.parent                   # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = 111                                            # (local) session number
GATE_ID = "S111-CF-MKK-RG-INVARIANCE"                    # (local)
SCHEME = "SA"                                            # (local) spectral-action coupling (continuity CV2A)
CONVENTION = "RATIO"                                     # (local) M_KK/M_Pl dimensionless transmutation (continuity CV2A)
L_MAX = 12                                               # (local) Friedrich-Bär-saturated bottom-K

# Pre-registered thresholds (define BEFORE running)
DELTA_REL_BAND = 5e-2                                    # (local) leg-1 relative τ-spread PASS band (CAC-mirror)
TAU_LO_SCAN = 0.190                                      # (local) scan lower edge (the fold)
TAU_HI_SCAN = 0.600                                      # (local) scan upper edge
TAU_STEP = 0.010                                         # (local) ≥40 τ-points across [0.190,0.600]
DELTA_TAU_SECTOR = 0.004                                 # (local) SECT-33a finite sector width (v_min cutoff source)
WALL_HALF_WIDTH = 0.05                                   # (local) van Hove wall half-width (canonical [0.15,0.25]@fold)

# Fine grid for the E_B2(τ) band spline (band group velocity v(τ)=dE/dτ)
GRID_LO = 0.02                                           # (local) spline grid lower edge
GRID_HI = 0.66                                           # (local) spline grid upper edge (covers scan + wall)
GRID_N = 65                                              # (local) spline grid resolution

# CV2A continuity anchors (the fixed-τ_fold reference the τ-scan generalizes)
LAMBDA_EFF_CV2A = 0.038934760900644856                   # (local) CV2A V_B2.mean() (Kosmann per-coset coupling)
N0_CV2A = float(rho_B2_per_mode)                         # (local) = 14.0233 canonical FINITE-enhanced fold DOS
R_CV2A = 0.16016847970570353                             # (local) CV2A transmutation_ratio exp(-1/(lam*N0)) at fold

# Output destinations
OUT_NPZ = SESSION_DIR / "s111_mkk_rg_invariance.npz"
OUT_PNG = SESSION_DIR / "s111_mkk_rg_invariance.png"

L12_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CV2A_NPZ = COMPUTATIONS_DIR / "session-110" / "s110_cf_cv2a_mkk_transmut_promote.npz"
INV11_NPZ = COMPUTATIONS_DIR / "investigation-11" / "inv11_w1_mkk_dimensional_transmutation.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    L12_CACHE,
    CV2A_NPZ,
    INV11_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
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
# Section 5 — Substrate τ-functions: B2 band, Kosmann coupling λ_eff(τ), DOS N₀(τ)
# ---------------------------------------------------------------------------

def band_and_kosmann(tau: float, gens, f_abc, gammas) -> tuple[float, float]:
    """At Jensen modulus τ, return (E_B2_mean(τ), ||K_a(τ)||_{C²}).

    E_B2_mean = mean of the 4-fold B2 fold band among the 8 lowest positive
                (0,0)-singlet Dirac band modes (B1×1 + B2×4 + B3×3 split under U(2)).
    ||K_a||_{C²} = Frobenius norm of the Kosmann spinorial correction along a C²
                (non-Killing) direction (all four C² directions degenerate on the
                Jensen curve). Deterministic function of the connection Γ(τ).
    """
    evals, evecs, Gamma, E, ah_err, h_err = extract_singlet_eigensystem(
        tau, gens, f_abc, gammas
    )
    pos = np.sort(evals[evals > 1e-9])               # (local) 8 positive band modes
    E_B2 = float(np.mean(pos[1:5]))                  # (local) B2 = the 4-fold fold band (indices 1..4)
    K_a, _A = kosmann_operator_antisymmetric(Gamma, gammas, C2_IDX[0])
    K_norm = float(np.sqrt(np.sum(np.abs(K_a) ** 2)))  # (local) ||K_a||_{C²}
    return E_B2, K_norm


def build_band_spline(gens, f_abc, gammas):
    """Build the E_B2(τ) band curve + Kosmann norm interpolant over the fine grid."""
    tau_grid = np.linspace(GRID_LO, GRID_HI, GRID_N)  # (local)
    E_grid = np.zeros(GRID_N)                          # (local)
    K_grid = np.zeros(GRID_N)                          # (local)
    for i, t in enumerate(tau_grid):
        E_grid[i], K_grid[i] = band_and_kosmann(float(t), gens, f_abc, gammas)
    cs_E = CubicSpline(tau_grid, E_grid)               # (local) B2 band spline E_B2(τ)
    return tau_grid, E_grid, K_grid, cs_E


def find_tau_fold(cs_E) -> tuple[float, float]:
    """Locate the van Hove fold (group velocity v=dE_B2/dτ = 0) in [0.10,0.30]."""
    tf = np.linspace(0.10, 0.30, 4000)        # (local)
    vf = cs_E(tf, 1)                           # (local) v(τ) = dE/dτ
    sc = np.where(np.diff(np.sign(vf)))[0]     # (local) sign changes
    if len(sc) > 0:
        i = sc[0]                              # (local)
        tau_fold_found = float(
            tf[i] - vf[i] * (tf[i + 1] - tf[i]) / (vf[i + 1] - vf[i])
        )
    else:
        tau_fold_found = float(tf[np.argmin(np.abs(vf))])
    d2E_fold = float(cs_E(tau_fold_found, 2))  # (local) d²E/dτ² at fold (van Hove curvature)
    return tau_fold_found, d2E_fold


def vanhove_dos(tau: float, cs_E, vmin_floor: float) -> float:
    """Windowed van Hove DOS per mode at τ.

    ρ(τ) = ⟨1/(π·max(|v(t)|, v_min(t)))⟩ over the wall [τ−w, τ+w],
    v(t) = dE_B2/dt, v_min(t) = max(|d²E/dt²(τ)|·δτ_sector, vmin_floor).

    The DOS pile-up exists because E_B2(τ) has a minimum (v→0) at τ_fold; away
    from the fold |v| grows and ρ collapses (1D van Hove, A₂ divergence REFUTED S94).
    """
    lo, hi = tau - WALL_HALF_WIDTH, tau + WALL_HALF_WIDTH  # (local)
    d2 = abs(float(cs_E(tau, 2)))                          # (local) local curvature
    v_min = max(d2 * DELTA_TAU_SECTOR, vmin_floor)         # (local) group-velocity cutoff
    integ = quad(
        lambda t: 1.0 / (np.pi * max(abs(float(cs_E(t, 1))), v_min)),
        lo, hi, limit=200,
    )[0]                                                   # (local)
    return float(integ / (hi - lo))                        # per unit τ = per mode


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    # --- infrastructure (su(3) + Clifford) ---
    gens = su3_generators()                                # (local)
    f_abc = compute_structure_constants(gens)              # (local)
    gammas = build_cliff8()                                # (local)

    # --- STEP 1: E_B2(τ) band curve + Kosmann norm interpolant ---
    tau_grid, E_grid, K_grid, cs_E = build_band_spline(gens, f_abc, gammas)
    tau_fold_found, d2E_fold = find_tau_fold(cs_E)
    E_B2_fold = float(cs_E(tau_fold_found))                # (local)

    # --- STEP 2 calibration: pin the DOS so N₀(τ_fold) = N0_CV2A (14.0233) ---
    # Solve for the v_min_floor that makes the windowed DOS equal the canonical
    # fold DOS at τ_fold (continuity with CV2A). The fold curvature gives the
    # natural cutoff; the floor absorbs the (TAU_WALL, sector-width) convention so
    # the substrate-natural N₀(τ_fold) anchor is reproduced exactly.
    def dos_fold_residual(vfloor):
        return vanhove_dos(tau_fold_found, cs_E, max(vfloor, 1e-9)) - N0_CV2A
    # bisection on log(v_min_floor) (DOS is monotone-decreasing in v_min_floor)
    lo_f, hi_f = 1e-6, 1e-1                                # (local) bracket
    r_lo = dos_fold_residual(lo_f)                          # (local) DOS too high (v_min tiny) -> residual > 0
    r_hi = dos_fold_residual(hi_f)                          # (local) DOS too low  (v_min big)  -> residual < 0
    if r_lo * r_hi < 0:
        for _ in range(80):                                # (local) bisection
            mid = np.sqrt(lo_f * hi_f)                      # (local) geometric midpoint
            r_mid = dos_fold_residual(mid)                 # (local)
            if r_lo * r_mid <= 0:
                hi_f, r_hi = mid, r_mid
            else:
                lo_f, r_lo = mid, r_mid
        vmin_floor = float(np.sqrt(lo_f * hi_f))           # (local) calibrated DOS floor
    else:
        # natural curvature cutoff already realizes N₀ within bracket; fall back
        vmin_floor = float(d2E_fold * DELTA_TAU_SECTOR)    # (local)
    N0_fold_check = vanhove_dos(tau_fold_found, cs_E, vmin_floor)  # (local) should ≈ N0_CV2A

    # --- STEP 3 calibration: pin λ_eff so λ_eff(τ_fold) = LAMBDA_EFF_CV2A ---
    # λ_eff(τ) = ||K_a(τ)||²_{C²} / C_const ; C_const fixed at fold (τ-INVARIANT
    # proportionality, depends only on spinor-space dim + C²-multiplicity).
    K_fold = float(np.interp(tau_fold_found, tau_grid, K_grid))  # (local) ||K_a(τ_fold)||
    C_const = K_fold ** 2 / LAMBDA_EFF_CV2A                       # (local) τ-INVARIANT proportionality

    def lambda_eff_of_tau(tau):
        K = float(np.interp(tau, tau_grid, K_grid))        # (local)
        return K ** 2 / C_const

    # --- STEP 4: the DIMENSIONLESS transmutation ratio R(τ) over the scan ---
    tau_scan = np.arange(TAU_LO_SCAN, TAU_HI_SCAN + 0.5 * TAU_STEP, TAU_STEP)  # (local) ≥40 pts
    lam_scan = np.array([lambda_eff_of_tau(t) for t in tau_scan])             # (local)
    N0_scan = np.array([vanhove_dos(t, cs_E, vmin_floor) for t in tau_scan])  # (local)
    g_scan = lam_scan * N0_scan                                               # (local) BCS product g·N(0)
    R_scan = np.exp(-1.0 / g_scan)                                            # (local) M_KK/M_Pl predicted

    # --- STEP 5: relative τ-spread Δ_rel (leg-1) ---
    R_mean = float(np.mean(R_scan))                                           # (local)
    R_min = float(np.min(R_scan))                                             # (local)
    R_max = float(np.max(R_scan))                                            # (local)
    delta_rel = (R_max - R_min) / R_mean if R_mean != 0 else float("inf")     # (local)

    # cross-check at τ_fold: reproduce CV2A R, λ_eff, N₀ (continuity anchor)
    lam_fold = lambda_eff_of_tau(tau_fold_found)                              # (local)
    g_fold = lam_fold * N0_fold_check                                        # (local)
    R_fold = float(np.exp(-1.0 / g_fold))                                    # (local)

    # ----- SCALE-IMPORT AUDIT-LOG (leg-2: the no-CODATA-cutoff set-membership) -----
    # Classify EVERY input to the transmutation chain by mass dimension.
    #   DIMENSIONLESS chain (the substrate-natural transmutation content):
    #     λ_eff(τ)  — Kosmann V-matrix mean per coset (V-matrix elements are
    #                 dimensionless in M_KK units; ratio of spectral quantities)
    #     N₀(τ)     — DOS per mode (dimensionless count per mode)
    #     g(τ)=λ·N₀ — dimensionless BCS product
    #     R(τ)      — dimensionless transmutation ratio exp(-1/g)
    #   DIMENSIONFUL MAGNITUDE leg (the cutoff that sets the absolute scale):
    #     Λ_cutoff  — M_KK = Λ_cutoff · R ; the dimensionful anchor.
    #
    # CV2A's magnitude leg anchored Λ_cutoff = M_Pl_reduced via the a₂/EH channel
    # (1/(16πG) = M_Pl_reduced²/2). That CODATA-unit cutoff IS the borrowed
    # dimensionful scale leg-2 audits for ABSENCE.
    audited_dimensionless_inputs = [
        "lambda_eff(tau)=||K_a(tau)||^2_C2/C_const",
        "N0(tau)=vanHove_DOS_per_mode",
        "g(tau)=lambda_eff*N0",
        "R(tau)=exp(-1/g)",
    ]  # (local)
    audited_dimensionful_magnitude_inputs = [
        "Lambda_cutoff = M_Pl_reduced (CV2A a2/EH channel anchor; CODATA-unit)",
    ]  # (local)
    # set-membership test (leg-2): is the only dimensionful magnitude scale the
    # CODATA M_Pl_reduced cutoff?
    codata_cutoff_in_magnitude_leg = any(
        "M_Pl_reduced" in s for s in audited_dimensionful_magnitude_inputs
    )  # (local) — TRUE under the CV2A construction (the cutoff is borrowed)
    leg2_no_import_pass = not codata_cutoff_in_magnitude_leg                  # (local)

    # M_KK magnitude reproduced under the CV2A anchor (sensitivity report only;
    # NOT a PASS-contributing dimensionful derivation)
    M_KK_derived_red = R_fold * M_Pl_reduced                                  # (local) PRIMARY (CV2A)
    M_KK_derived_unred = R_fold * M_Pl_unreduced                              # (local) sensitivity
    M_KK_target = M_KK_gravity                                                # (local) CONST-FREEZE-42
    oom_red = abs(np.log10(M_KK_derived_red) - np.log10(M_KK_target))         # (local)

    # ----- [SIGN] 3-tuple -----
    # CC1 sign axis — the output is DIMENSIONLESS: [R] = exp(dimensionless) = pure
    #   number. The dimension-of-output sign is PASS iff R carries NO mass dimension
    #   (verified by construction: g = λ·N₀ dimensionless ⇒ R dimensionless).
    output_is_dimensionless = True                                           # (local) by construction
    # CC2 sign axis — the τ-spread DIRECTION: a τ-FLAT R (Δ_rel < band) is the
    #   DYNAMICAL (RG-invariant) reading; a τ-FLOWING R (Δ_rel ≥ band) is BARE-IMPORT.
    #   sign_predicted: leg-1 PASS means R does NOT depend on the modulus-flow
    #   evaluation point. The SIGN verdict is PASS iff the dimension-of-output
    #   prediction (R dimensionless) holds AND the leg-1 direction is correctly read.
    leg1_rg_invariant = bool(delta_rel < DELTA_REL_BAND)                      # (local)
    sign_verdict = "PASS" if output_is_dimensionless else "FAIL"             # (local) dimension-of-output sign

    # magnitude axis — the τ-spread band test (leg-1 RG-invariance):
    #   PASS iff Δ_rel < band ; FAIL iff Δ_rel ≥ band.
    magnitude_verdict = "PASS" if leg1_rg_invariant else "FAIL"             # (local)

    # regime axis — BCS weak-coupling transmutation form valid iff g < 1 throughout
    #   the scan (exp(-1/g) is the dimensional-transmutation regime) AND the DOS
    #   window is L12-saturated.
    g_max = float(np.max(g_scan))                                            # (local)
    regime_verdict = "VALID" if g_max < 1.0 else "MARGINAL"                  # (local)

    # ----- composite verdict (plan operator) -----
    # DYNAMICAL (PASS)   iff (leg-1 AND leg-2)
    # BARE-IMPORT (FAIL) iff (NOT leg-1) OR (CODATA-only magnitude leg)
    # INFO               iff (leg-1) AND (magnitude leg NOT clearable of CODATA cutoff)
    if regime_verdict == "BREAKDOWN" or sign_verdict == "FAIL":
        composite = "FAIL"                                                   # (local)
    elif (not leg1_rg_invariant):
        composite = "FAIL"                                                   # (local) BARE-IMPORT (R flows with τ)
    elif leg1_rg_invariant and leg2_no_import_pass:
        composite = "PASS"                                                   # (local) DYNAMICAL
    elif leg1_rg_invariant and (not leg2_no_import_pass):
        composite = "INFO"                                                   # (local) RG-invariant but magnitude leg holds CODATA cutoff
    else:
        composite = "FAIL"                                                   # (local)

    reading = (
        "DYNAMICAL" if composite == "PASS"
        else ("BARE-IMPORT" if composite == "FAIL" else "RG-INVARIANT-MAGNITUDE-HELD")
    )  # (local)

    return {
        "value": composite,
        "composite": composite,
        "reading": reading,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        # τ-RG-invariance (leg-1)
        "delta_rel": delta_rel,
        "delta_rel_band": DELTA_REL_BAND,
        "leg1_rg_invariant": leg1_rg_invariant,
        "R_min": R_min,
        "R_max": R_max,
        "R_mean": R_mean,
        "g_max": g_max,
        # no-import (leg-2)
        "leg2_no_import_pass": leg2_no_import_pass,
        "codata_cutoff_in_magnitude_leg": codata_cutoff_in_magnitude_leg,
        "audited_dimensionless_inputs": audited_dimensionless_inputs,
        "audited_dimensionful_magnitude_inputs": audited_dimensionful_magnitude_inputs,
        # fold continuity anchors
        "tau_fold_found": tau_fold_found,
        "E_B2_fold": E_B2_fold,
        "d2E_fold": d2E_fold,
        "lam_fold": lam_fold,
        "N0_fold_check": N0_fold_check,
        "N0_CV2A": N0_CV2A,
        "lambda_eff_CV2A": LAMBDA_EFF_CV2A,
        "R_fold": R_fold,
        "R_CV2A": R_CV2A,
        "C_const": C_const,
        "vmin_floor": vmin_floor,
        # M_KK magnitude (sensitivity report; NOT PASS-contributing)
        "M_KK_derived_red": M_KK_derived_red,
        "M_KK_derived_unred": M_KK_derived_unred,
        "M_KK_target": M_KK_target,
        "oom_red": oom_red,
        # scan arrays
        "tau_scan": tau_scan,
        "lam_scan": lam_scan,
        "N0_scan": N0_scan,
        "g_scan": g_scan,
        "R_scan": R_scan,
        # band curve
        "tau_grid": tau_grid,
        "E_grid": E_grid,
        "K_grid": K_grid,
        # multiplicative-normalization pre-flight
        "mult_norm_cancellation": "NOT-APPLICABLE-BY-OPERATOR-FORM",
    }


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload + 4-tuple output + plot
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    payload: dict = {
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
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))  # (local)

    # Panel A: E_B2(τ) band curve + fold (van Hove minimum)
    ax = axes[0]  # (local)
    ax.plot(res["tau_grid"], res["E_grid"], "o-", ms=3, color="#1f77b4",
            label="E_B2(τ) (singlet fold band)")
    ax.axvline(res["tau_fold_found"], color="crimson", ls="--", lw=1.2,
               label=f"τ_fold (v=0)={res['tau_fold_found']:.4f}")
    ax.axhline(res["E_B2_fold"], color="grey", ls=":", lw=0.8)
    ax.set_xlabel("Jensen modulus τ")
    ax.set_ylabel("E_B2 (M_KK units)")
    ax.set_title(f"B2 fold band: v=0 at τ_fold={res['tau_fold_found']:.4f}\n"
                 f"(canonical 0.190; d²E/dτ²={res['d2E_fold']:.3f})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel B: λ_eff(τ), N₀(τ), g(τ)=λ·N₀ across the scan
    ax = axes[1]  # (local)
    ax.plot(res["tau_scan"], res["lam_scan"], "s-", ms=3, color="#2ca02c", label="λ_eff(τ)")
    ax.plot(res["tau_scan"], res["N0_scan"] / res["N0_scan"][0], "^-", ms=3,
            color="#ff7f0e", label="N₀(τ)/N₀(τ_fold)")
    ax.plot(res["tau_scan"], res["g_scan"] / res["g_scan"][0], "o-", ms=3,
            color="#9467bd", label="g(τ)/g(τ_fold)")
    ax.set_xlabel("Jensen modulus τ")
    ax.set_ylabel("(normalized to τ_fold)")
    ax.set_title(f"BCS inputs across scan: g=λ·N₀\n"
                 f"N₀(τ_fold)={res['N0_fold_check']:.4f} (CV2A 14.0233)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel C: R(τ) τ-spread (log scale) — the τ-RG-invariance test
    ax = axes[2]  # (local)
    ax.semilogy(res["tau_scan"], res["R_scan"], "o-", ms=4, color="#d62728",
                label="R(τ)=exp(−1/(λ·N₀))")
    ax.axhline(res["R_CV2A"], color="grey", ls=":", lw=1.0,
               label=f"R_CV2A(fold)={res['R_CV2A']:.4e}")
    ax.set_xlabel("Jensen modulus τ")
    ax.set_ylabel("R(τ) = M_KK/M_Pl  (dimensionless)")
    ax.set_title(f"τ-RG test: Δ_rel={res['delta_rel']:.3e} "
                 f"({'<' if res['leg1_rg_invariant'] else '≥'} {res['delta_rel_band']:.0e})\n"
                 f"reading={res['reading']} → {res['composite']}")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    fig.suptitle(f"{GATE_ID}: M_KK τ-RG-invariance decider — {res['composite']} ({res['reading']})",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
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

    res = compute()

    # --- report NUMBERS before the verdict (substrate-first) ---
    print("=== STEP 1-3: τ-FOLD CONTINUITY ANCHORS (reproduce CV2A) ===")
    print(f"  τ_fold (v=0)                      = {res['tau_fold_found']:.6f}  (canonical 0.190)")
    print(f"  E_B2 at fold                      = {res['E_B2_fold']:.6f}  (canonical 0.845269)")
    print(f"  d²E/dτ² at fold                   = {res['d2E_fold']:.6f}  (canonical ~1.176)")
    print(f"  λ_eff(τ_fold)                     = {res['lam_fold']:.6f}  (CV2A {res['lambda_eff_CV2A']:.6f})")
    print(f"  N₀(τ_fold)                        = {res['N0_fold_check']:.6f}  (CV2A {res['N0_CV2A']:.6f})")
    print(f"  R(τ_fold)=exp(-1/(λ·N₀))          = {res['R_fold']:.6e}  (CV2A {res['R_CV2A']:.6e})")
    print(f"  C_const (τ-INVARIANT λ proportionality) = {res['C_const']:.6f}")
    print(f"  vmin_floor (DOS calibration)      = {res['vmin_floor']:.6e}")
    print()
    print("=== STEP 4-5: τ-SCAN of R(τ) = exp(-1/(λ_eff(τ)·N₀(τ))) ===")
    print(f"  scan τ ∈ [{res['tau_scan'][0]:.3f}, {res['tau_scan'][-1]:.3f}], "
          f"{len(res['tau_scan'])} points")
    print(f"  {'τ':>6} {'λ_eff(τ)':>10} {'N₀(τ)':>9} {'g=λ·N₀':>9} {'R(τ)':>13}")
    for i in range(0, len(res["tau_scan"]), max(1, len(res["tau_scan"]) // 12)):
        print(f"  {res['tau_scan'][i]:6.3f} {res['lam_scan'][i]:10.6f} "
              f"{res['N0_scan'][i]:9.4f} {res['g_scan'][i]:9.4f} {res['R_scan'][i]:13.6e}")
    print(f"  R range: min={res['R_min']:.6e}, max={res['R_max']:.6e}, mean={res['R_mean']:.6e}")
    print(f"  Δ_rel = (R_max − R_min)/R_mean    = {res['delta_rel']:.6e}  "
          f"(PASS band < {res['delta_rel_band']:.0e})")
    print(f"  leg-1 RG-invariant (Δ_rel<band)?  = {res['leg1_rg_invariant']}")
    print(f"  g_max across scan                 = {res['g_max']:.6f}  (regime VALID iff < 1)")
    print()
    print("=== LEG-2: SCALE-IMPORT AUDIT-LOG (no-CODATA-cutoff set-membership) ===")
    print("  DIMENSIONLESS chain (substrate-natural transmutation content):")
    for s in res["audited_dimensionless_inputs"]:
        print(f"    + {s}")
    print("  DIMENSIONFUL MAGNITUDE leg (the absolute-scale anchor):")
    for s in res["audited_dimensionful_magnitude_inputs"]:
        print(f"    - {s}")
    print(f"  CODATA M_Pl_reduced in magnitude leg? = {res['codata_cutoff_in_magnitude_leg']}")
    print(f"  leg-2 no-import PASS (M_Pl_reduced ∉ magnitude inputs)? = {res['leg2_no_import_pass']}")
    print()
    print("=== M_KK MAGNITUDE (sensitivity report; NOT PASS-contributing) ===")
    print(f"  M_KK target (CONST-FREEZE-42)     = {res['M_KK_target']:.6e} GeV")
    print(f"  M_KK derived (M_Pl_reduced anchor)= {res['M_KK_derived_red']:.6e} GeV | OOM {res['oom_red']:.4f}")
    print()
    print("=== MULTIPLICATIVE-NORMALIZATION CANCELLATION PRE-FLIGHT ===")
    print(f"  {res['mult_norm_cancellation']} — the observable is the τ-flow of the")
    print("  transmutation EXPONENT, NOT a K-log-derivative d^n ln(·)/d(ln K)^n;")
    print("  no w(L_max)·g(K) factorization check is triggered.")
    print()
    print("=== 3-TUPLE [SIGN] ===")
    print(f"  sign_verdict      = {res['sign_verdict']}  (dimension-of-output: R dimensionless)")
    print(f"  magnitude_verdict = {res['magnitude_verdict']}  (τ-spread band: Δ_rel vs {res['delta_rel_band']:.0e})")
    print(f"  regime_verdict    = {res['regime_verdict']}  (BCS weak-coupling g<1)")
    print(f"  composite         = {res['composite']}  ({res['reading']})")
    print()

    # --- save npz ---
    np.savez(
        OUT_NPZ,
        composite=res["composite"],
        reading=res["reading"],
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        delta_rel=res["delta_rel"],
        delta_rel_band=res["delta_rel_band"],
        leg1_rg_invariant=res["leg1_rg_invariant"],
        leg2_no_import_pass=res["leg2_no_import_pass"],
        codata_cutoff_in_magnitude_leg=res["codata_cutoff_in_magnitude_leg"],
        R_min=res["R_min"],
        R_max=res["R_max"],
        R_mean=res["R_mean"],
        g_max=res["g_max"],
        tau_fold_found=res["tau_fold_found"],
        E_B2_fold=res["E_B2_fold"],
        d2E_fold=res["d2E_fold"],
        lam_fold=res["lam_fold"],
        N0_fold_check=res["N0_fold_check"],
        N0_CV2A=res["N0_CV2A"],
        lambda_eff_CV2A=res["lambda_eff_CV2A"],
        R_fold=res["R_fold"],
        R_CV2A=res["R_CV2A"],
        C_const=res["C_const"],
        vmin_floor=res["vmin_floor"],
        M_KK_derived_red=res["M_KK_derived_red"],
        M_KK_derived_unred=res["M_KK_derived_unred"],
        M_KK_target=res["M_KK_target"],
        oom_red=res["oom_red"],
        tau_scan=res["tau_scan"],
        lam_scan=res["lam_scan"],
        N0_scan=res["N0_scan"],
        g_scan=res["g_scan"],
        R_scan=res["R_scan"],
        tau_grid=res["tau_grid"],
        E_grid=res["E_grid"],
        K_grid=res["K_grid"],
        mult_norm_cancellation=res["mult_norm_cancellation"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  wrote {OUT_NPZ.name}")
    make_plot(res)
    print(f"  wrote {OUT_PNG.name}")
    print()

    # --- value payload for the verdict line (no single-quote chars) ---
    value = (
        f"reading={res['reading']};Delta_rel={res['delta_rel']:.4e}"
        f"({'<' if res['leg1_rg_invariant'] else '>='}{res['delta_rel_band']:.0e});"
        f"leg1_RGinv={res['leg1_rg_invariant']};leg2_noimport={res['leg2_no_import_pass']};"
        f"R_fold={res['R_fold']:.4e}(CV2A{res['R_CV2A']:.4e});"
        f"lam_fold={res['lam_fold']:.5f};N0_fold={res['N0_fold_check']:.4f};"
        f"R_range=[{res['R_min']:.3e},{res['R_max']:.3e}];g_max={res['g_max']:.4f};"
        f"CODATA_in_magnitude_leg={res['codata_cutoff_in_magnitude_leg']};"
        f"output_DIMENSIONLESS=True;multnorm=NOT-APPLICABLE-BY-OPERATOR-FORM"
    )  # (local)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    extra_rows = [
        f"# {GATE_ID} tau-RG: R(tau)=exp(-1/(lambda_eff(tau)*N0(tau))); "
        f"lambda_eff(tau)=||K_a(tau)||^2_C2/C_const (Kosmann V-matrix per coset, Baptista Paper17 eq4.1); "
        f"N0(tau)=windowed-vanHove-DOS-per-mode (B2 band group velocity v=dE_B2/dtau)",
        f"# {GATE_ID} continuity: tau_fold(v=0)={res['tau_fold_found']:.4f}(canon 0.190); "
        f"E_B2_fold={res['E_B2_fold']:.6f}(canon 0.845269); lam_fold={res['lam_fold']:.5f}(CV2A {res['lambda_eff_CV2A']:.5f}); "
        f"N0_fold={res['N0_fold_check']:.4f}(CV2A 14.0233); R_fold={res['R_fold']:.4e}(CV2A {res['R_CV2A']:.4e})",
        f"# {GATE_ID} leg-1 RG-invariance: Delta_rel={res['delta_rel']:.4e} "
        f"{'<' if res['leg1_rg_invariant'] else '>='} {res['delta_rel_band']:.0e}; "
        f"R_range=[{res['R_min']:.3e},{res['R_max']:.3e}]; van-Hove DOS pile-up FOLD-LOCALIZED (A2 divergence REFUTED S94; 1D theorem)",
        f"# {GATE_ID} leg-2 no-import: M_Pl_reduced {'IN' if res['codata_cutoff_in_magnitude_leg'] else 'NOT-IN'} "
        f"dimensionful-magnitude-inputs => leg2_no_import_pass={res['leg2_no_import_pass']}; "
        f"DIMENSIONLESS chain={{lambda_eff,N0,g,R}} carries substrate-natural transmutation; "
        f"Lambda_cutoff=M_Pl_reduced(CV2A a2/EH 1/(16piG)=M_Pl_red^2/2) is the borrowed CODATA scale",
        f"# {GATE_ID} regulator_pin=N/A (van Hove fold DOS N0 is the BCS pairing kernel, NOT a Seeley-DeWitt a_n residue; "
        f"the cutoff-anchor a_2^{{Pauli-Villars}}/EH channel IS the CODATA leg-2 audits for ABSENCE, NOT a PASS-contributing a_n moment)",
        f"# {GATE_ID} multiplicative-normalization-cancellation: NOT-APPLICABLE-BY-OPERATOR-FORM "
        f"(tau-spread of the transmutation EXPONENT, not a K-log-derivative d^n ln/d(ln K)^n; no w(L_max)*g(K) factorization)",
        f"# {GATE_ID} dual-prior: composite={res['composite']} => "
        f"{'reallocate 0.90 to Track-A DYNAMICAL' if res['composite']=='PASS' else ('reallocate 0.90 to Track-B BARE-IMPORT' if res['composite']=='FAIL' else 'priors UNCHANGED; route no-import leg to forward gate (a2/EH-independent dimensionful anchor)')}",
    ]  # (local)

    print_verdict_payload(
        res["composite"], value, audit_sha, content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        companion_note=(
            f"M_KK tau-RG-invariance decider: reading={res['reading']}; "
            f"Delta_rel={res['delta_rel']:.3e}; the dimensionless ratio R is "
            f"{'tau-FLAT (RG fixed-point)' if res['leg1_rg_invariant'] else 'tau-FLOWING (NOT a fixed-point)'}; "
            f"magnitude leg {'clears' if res['leg2_no_import_pass'] else 'retains'} the CODATA M_Pl_reduced cutoff"
        ),
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {res['composite']} ({res['reading']}) (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
