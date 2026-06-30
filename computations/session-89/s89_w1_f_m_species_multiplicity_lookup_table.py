#!/usr/bin/env python3
"""
S89 W1-3 -- S89-F-M-SPECIES-MULTIPLICITY-LOOKUP-TABLE
======================================================

Gate: S89-F-M-SPECIES-MULTIPLICITY-LOOKUP-TABLE ([VERIFY])

Pre-registered thresholds (from session-89-plan-w1.md §W1-3 §9):
  PASS: ALL 3 cross-check anchors (T = 100 GeV, 1 GeV, 1 MeV) satisfy
        |f(g) - g_*_standard(T)| / g_*_standard(T) < 0.10 (10% RATIO tol)
        AND coverage_assert == True (g in {0..384} fully populated)
        AND T_H(g) is monotone decreasing.
  INFO: 2 of 3 anchors PASS (one anchor in {0.10, 0.30} band); coverage maintained.
  FAIL: <= 1 anchor PASS, OR coverage_assert == False, OR T_H(g) NOT monotone.

Hypothesis: The substrate-IS Delta_BCS cooling cascade
    T_H(g) = T_H_initial * exp(-g * Delta_BCS / K_base)
traverses the SM-particle mass-threshold structure in monotone-decreasing
sequence over g in {0..384}; the resulting f(g) = g_*(T_H(g)) lookup
table matches standard-cosmology g_*(T) at the three cross-check anchors
within 10% RATIO tolerance.

Substitution chain (Step 1 -- Step 4 per plan §W1-3 §10; MANDATORY):
  Step 1 (Definitions):
    T_H(g)  = T_H_initial * exp(-g * Delta_BCS / K_base)  (substrate-IS, S88 W6 V.5)
    g_*(T)  = sum_{bosons active} g_b + (7/8) * sum_{fermions active} g_f  (PDG)
    f(g)    = g_*(T_H(g))
  Step 2 (Substitution):
    dT_H/dg = T_H(g) * (-Delta_BCS / K_base)
    Delta_BCS / K_base = 0.4642547... / 2.035 = 0.22813500711698953
  Step 3 (Simplify):
    Delta_BCS = 0.4642547... > 0 (R-PROTECTED)
    K_base    = 2.035             > 0 (S82 W2-4)
    T_H(g)    > 0 always
    => dT_H/dg < 0 strictly for all g.
  Step 4 (Direction):
    T_H(g) is strictly monotone decreasing in g; f(g) is non-increasing
    (discrete drops at SM-particle mass thresholds).
    Pre-registered.

Substrate framing (verbatim from plan §W1-3 §13, MANDATORY):
  "Cascade generations g in {0..384} are intrinsic substrate-IS labels
  in the Delta_BCS cooling cascade (per S88 W6 §V.5 substrate-IS pinning);
  they are NOT time-coordinate values. T_H(g) is the substrate's emergent
  Hawking temperature at the substrate's intrinsic cascade-generation g;
  the cascade IS the structural substrate-physics, NOT a process happening
  IN time. Phononic excitation channel count g_*(T_H(g)) is the substrate's
  intrinsic count of accessible phononic modes at substrate-temperature
  T_H(g)."
  Single-tau-slice level: §W1-3 operates at Level 1 (cascade structure
  at fixed tau_fold = 0.190; the cascade IS the substrate's intrinsic
  generation index, NOT a moduli-deformation parameter).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py
  - sessions/archive/session-88/workshops/s88-w6-w1c-69-page1976-13oom.md (cascade form V.5)
  - sessions/framework/registry/branch-iv-canonical.md (substrate-natural anchor §3)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple (per plan §W1-3 §8):
  (value='coverage=Pass;cross_checks_passed=N/3',
   scheme=substrate-derived-T_H-g-times-PDG-SM-threshold-structure,
   convention=substrate-cascade-T_H-g-with-SM-threshold-structure-FULL,
   L_max=10)

Classification: PHONONIC + cosmological-bridge (substrate's count of
phononic excitation channels at T_H(g) traversing SM-particle
mass-threshold structure across cascade generations g in {0..384}).

DISCIPLINE
----------
- `from canonical_constants import *` (S34+; uses Delta_BCS, K_base).
- T_H_initial promoted to canonical_constants.py via update_constant on PASS.
- Every local/intermediate tagged `# (local)`.
- CPU-only; small-table arithmetic + 3-anchor cross-check; OMP_NUM_THREADS=8.
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- Verdict appended to computations/session-89/s89_gate_verdicts.txt
  (canonical path per gate-verdicts.md; the `_shared/` form is FORBIDDEN).
- Schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row REQUIRED
  (substitution chain Step 4 pre-registers monotonic-decreasing direction).

REFERENCES
----------
- sessions/session-plan/session-89-plan-w1.md §W1-3 (full block)
- sessions/archive/session-88/workshops/s88-w6-w1c-69-page1976-13oom.md V.5
- sessions/framework/registry/branch-iv-canonical.md §3
- sessions/archive/session-87/workshops/s87-pixelation-lock-hawking-transit.md
  (BBN-mass anchor: M = 1.06e13 kg, T_H = 1.057 MeV, g_form ≈ 322)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- CPU thread cap (BEFORE numpy import per computation-environment.md)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 2 -- Canonical constants (MANDATORY first import per math-scripts.md)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

# Ensure session-89 directory exists (per spawn-prompt orchestrator override)
SESSION_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403
# Explicit re-import to catch IDE refactors
from canonical_constants import Delta_BCS, K_base  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 4 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S89"  # (local)
GATE_ID = "S89-F-M-SPECIES-MULTIPLICITY-LOOKUP-TABLE"  # (local)
SCHEME = "substrate-derived-T_H-g-times-PDG-SM-threshold-structure"  # (local)
CONVENTION = "substrate-cascade-T_H-g-with-SM-threshold-structure-FULL"  # (local)
L_MAX = 10  # (local) substrate spectral-triple truncation

# Pre-registered cross-check anchors (PDG/Planck standard-cosmology values)
ANCHOR_T_GEV = {  # (local)
    "T_100GeV": 100.0,   # electroweak; standard g_* = 106.75 (full SM)
    "T_1GeV":   1.0,     # QCD-scale; standard g_* = 61.75
    "T_1MeV":   1.0e-3,  # BBN-scale; standard g_* = 10.75
}
ANCHOR_G_STAR_STANDARD = {  # (local)
    "T_100GeV": 106.75,
    "T_1GeV":   61.75,
    "T_1MeV":   10.75,
}
PASS_RATIO_TOL = 0.10  # (local) 10% relative tolerance per §9
INFO_RATIO_TOL = 0.30  # (local) {0.10, 0.30} INFO band per §9

# Cascade-generation range
G_MIN = 0     # (local)
G_MAX = 384   # (local) full cascade depth (S87 pixelation-lock cascade)
G_RANGE = G_MAX - G_MIN + 1  # (local) 385

# Substrate-IS T_H_initial anchor: pinned by back-derivation from S88 W6 V.5
# BBN-anchor (g_BBN = 322, T_H = 1.057 MeV) per S87 J8 + S88 W6 V.5.
# Cascade form: T_H(g) = T_H_initial * exp(-g * Delta_BCS / K_base)
# => T_H_initial = T_H(g_BBN) * exp(g_BBN * Delta_BCS / K_base)
G_BBN_ANCHOR = 322  # (local) S87 pixelation-lock workshop
T_H_BBN_ANCHOR_GEV = 1.057e-3  # (local) GeV (= 1.057 MeV; S88 W6 V.5 + S87 J8)
T_H_INITIAL_GEV = T_H_BBN_ANCHOR_GEV * math.exp(
    G_BBN_ANCHOR * Delta_BCS / K_base
)  # (local) substrate-pinned T_H at g=0

# Input pin paths
INPUT_CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
INPUT_S88_W6_V5 = (
    PROJECT_ROOT / "sessions" / "session-88" / "workshops"
    / "s88-w6-w1c-69-page1976-13oom.md"
)
INPUT_BRANCH_IV = (
    PROJECT_ROOT / "sessions" / "framework" / "registry"
    / "branch-iv-canonical.md"
)
INPUT_FILES = [
    INPUT_CANONICAL_CONSTANTS,
    INPUT_S88_W6_V5,
    INPUT_BRANCH_IV,
]

# Output destinations
OUT_NPZ = SESSION_DIR / "s89_w1_f_m_species_multiplicity_lookup_table.npz"
OUT_PNG = SESSION_DIR / "s89_w1_f_m_species_multiplicity_lookup_table.png"
VERDICT_TXT = SESSION_DIR / "s89_gate_verdicts.txt"


# ---------------------------------------------------------------------------
# Section 5 -- SM-particle mass threshold table (verbatim from plan §6 step 2)
# ---------------------------------------------------------------------------
# PDG values are methodological cross-checks ONLY (not substrate canonicals)
# per plan §7 SOURCE-RECONCILIATION clause.

# Each entry: (name, mass_GeV, dof_count, statistics)
# statistics: 'B' = boson (full count); 'F' = fermion (7/8 weight)
# mass = 0.0 means always relativistic / always counted
SM_PARTICLES = [  # (local)
    # Always-relativistic species (active for all g in {0..384})
    ("photon",      0.0,        2,   "B"),    # g_gamma = 2 polarizations
    ("gluon",       0.0,        16,  "B"),    # 8 colors x 2 pol = 16 (active above QCD)
    ("nu_e",        0.0,        2,   "F"),    # neutrino + antineutrino (2 dof for L-handed)
    ("nu_mu",       0.0,        2,   "F"),
    ("nu_tau",      0.0,        2,   "F"),

    # Light fermions (electron threshold)
    ("electron",    0.511e-3,   4,   "F"),    # e+/e-, 2 spins each = 4

    # Mid-mass fermions
    ("muon",        105.7e-3,   4,   "F"),    # mu+/mu-, 2 spins = 4
    ("pion_charged", 139.57e-3, 2,   "B"),    # pi+/pi-
    ("pion_neutral", 134.98e-3, 1,   "B"),    # pi0
    ("nucleon",     0.939,      8,   "F"),    # p, n, p-bar, n-bar; 2 spins each = 8

    # Heavy fermions
    ("tau",         1.777,      4,   "F"),    # tau+/tau-, 2 spins = 4
    ("charm",       1.275,      12,  "F"),    # c, c-bar; 3 colors; 2 spins = 12
    ("bottom",      4.18,       12,  "F"),    # b, b-bar; 3 colors; 2 spins = 12
    ("top",         173.0,      12,  "F"),    # t, t-bar; 3 colors; 2 spins = 12

    # Strange / up / down (active above QCD scale ~ 200 MeV)
    ("up_quark",    0.0022,     12,  "F"),    # u, u-bar; 3 colors; 2 spins (active T > Lambda_QCD)
    ("down_quark",  0.0047,     12,  "F"),    # d, d-bar
    ("strange",     0.095,      12,  "F"),    # s, s-bar

    # Heavy gauge bosons
    ("W_pm",        80.379,     6,   "B"),    # W+, W-; 3 polarizations each = 6
    ("Z_boson",     91.188,     3,   "B"),    # Z0; 3 polarizations
    ("Higgs",       125.10,     1,   "B"),    # H scalar; 1 dof
]
LAMBDA_QCD_GEV = 0.200  # (local) Lambda_QCD ~ 200 MeV (per plan §6 step 2 quark/gluon activation)


# ---------------------------------------------------------------------------
# Section 6 -- SHA-256 + closure-hash + dual-SHA helpers
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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
# Section 7 -- Cascade T_H(g) and species-counting g_*(T)
# ---------------------------------------------------------------------------

def compute_T_H_cascade(g_table: np.ndarray) -> np.ndarray:
    """Substrate-IS cascade T_H(g) = T_H_initial * exp(-g * Delta_BCS / K_base).

    Per S88 W6 V.5 substrate-natural anchor + branch-iv-canonical.md §3.
    Input g_table is array of cascade generations in {0..G_MAX}.
    Output T_H_g_table is in GeV.
    """
    rate = Delta_BCS / K_base  # (local) > 0; canonical R-PROTECTED ratio
    return T_H_INITIAL_GEV * np.exp(-g_table * rate)


def g_star_at_temperature(T_GeV: float) -> float:
    """Standard-cosmology g_*(T) summing active SM species at temperature T (GeV).

    Active = m < ~T (relativistic); near-threshold (within factor 5 of T)
    apply Boltzmann suppression exp(-m/T) per plan §6 step 3.
    Quarks/gluons activate above Lambda_QCD ~ 200 MeV per plan §6 step 2.

    Returns g_*(T) = sum_{B active} g_b + (7/8) * sum_{F active} g_f.
    """
    g_B = 0.0  # (local) accumulator for boson dof (full weight)
    g_F = 0.0  # (local) accumulator for fermion dof (7/8 weight applied at end)

    is_QCD_active = T_GeV >= LAMBDA_QCD_GEV  # (local) gluons + light quarks active
    QCD_NAMES = {"gluon", "up_quark", "down_quark", "strange", "charm",
                 "bottom", "top", "nucleon", "pion_charged", "pion_neutral"}  # (local)

    for name, mass_GeV, dof, stat in SM_PARTICLES:
        # QCD-active gating: gluons and quarks active iff T >= Lambda_QCD
        # (above the deconfinement scale, the dof are quarks+gluons; below,
        # they are pions + nucleons. The plan §6 step 2 table specifies
        # gluons "T > Lambda_QCD ~ 200 MeV"; pions "T > 134 MeV";
        # nucleons "T > 1 GeV" — we apply gluon/quark activation at QCD
        # scale and use pions/nucleons for T < QCD scale via mass thresholds.)
        is_quark_or_gluon = name in {"gluon", "up_quark", "down_quark",
                                      "strange", "charm", "bottom", "top"}  # (local)
        is_hadron = name in {"nucleon", "pion_charged", "pion_neutral"}  # (local)

        if is_quark_or_gluon and not is_QCD_active:
            continue  # below QCD scale, quarks+gluons confined into hadrons

        if is_hadron and is_QCD_active:
            continue  # above QCD scale, quark/gluon dof replace hadron dof

        # Mass-threshold activation: m < T fully active; m within factor 5
        # apply Boltzmann suppression exp(-m/T)
        if mass_GeV == 0.0:
            weight = 1.0  # (local) always-relativistic
        elif T_GeV >= 5.0 * mass_GeV:
            weight = 1.0  # (local) fully relativistic
        elif T_GeV >= mass_GeV / 5.0:
            # Near-threshold Boltzmann suppression (within factor 5 of mass)
            weight = math.exp(-mass_GeV / T_GeV)  # (local)
        else:
            weight = 0.0  # (local) frozen out (T << m / 5)

        contribution = weight * dof  # (local)
        if stat == "B":
            g_B += contribution
        elif stat == "F":
            g_F += contribution

    return g_B + (7.0 / 8.0) * g_F


def compute_f_g_lookup(T_H_g_table: np.ndarray) -> np.ndarray:
    """f(g) = g_*(T_H(g)) for each g in cascade generations table."""
    f_g_table = np.empty_like(T_H_g_table)  # (local)
    for i, T_GeV in enumerate(T_H_g_table):
        f_g_table[i] = g_star_at_temperature(float(T_GeV))
    return f_g_table


# ---------------------------------------------------------------------------
# Section 8 -- Cross-check at standard-cosmology anchors
# ---------------------------------------------------------------------------

def cross_check_at_anchor(
    T_anchor_GeV: float,
    g_star_standard: float,
    g_table: np.ndarray,
    T_H_g_table: np.ndarray,
    f_g_table: np.ndarray,
) -> dict:
    """Find g s.t. T_H(g) is closest to T_anchor; compute f(g) and rel-dev."""
    # Find closest g (in log-T space)
    log_T_anchor = np.log(T_anchor_GeV)  # (local)
    log_T_H = np.log(T_H_g_table)  # (local)
    g_closest_idx = int(np.argmin(np.abs(log_T_H - log_T_anchor)))  # (local)

    g_at_anchor = int(g_table[g_closest_idx])  # (local)
    T_H_at_anchor = float(T_H_g_table[g_closest_idx])  # (local)
    measured_f_g = float(f_g_table[g_closest_idx])  # (local)
    rel_dev = abs(measured_f_g - g_star_standard) / g_star_standard  # (local)

    return {
        "T_anchor_GeV": T_anchor_GeV,
        "g_at_anchor": g_at_anchor,
        "T_H_at_anchor_GeV": T_H_at_anchor,
        "measured_f_g": measured_f_g,
        "standard_g_star": g_star_standard,
        "rel_dev": rel_dev,
        "PASS_within_10pct": rel_dev < PASS_RATIO_TOL,
        "INFO_within_30pct": rel_dev < INFO_RATIO_TOL,
    }


# ---------------------------------------------------------------------------
# Section 9 -- Main run
# ---------------------------------------------------------------------------

def run_lookup_table_gate() -> dict:
    """Build full cascade T_H(g) + f(g) lookup table; cross-check at 3 anchors."""
    # Build cascade tables
    g_table = np.arange(G_MIN, G_MAX + 1, dtype=np.int64)  # (local) length 385
    T_H_g_table = compute_T_H_cascade(g_table)  # (local) GeV
    f_g_table = compute_f_g_lookup(T_H_g_table)  # (local) g_* at each g

    # Coverage assertion: every g in {0..384} has defined f(g)
    coverage_assert = bool(  # (local)
        len(g_table) == G_RANGE
        and len(T_H_g_table) == G_RANGE
        and len(f_g_table) == G_RANGE
        and not np.any(np.isnan(T_H_g_table))
        and not np.any(np.isnan(f_g_table))
        and not np.any(np.isinf(T_H_g_table))
        and not np.any(np.isinf(f_g_table))
    )

    # Monotonicity of T_H(g): strictly decreasing per Step 4
    dT = np.diff(T_H_g_table)  # (local) length 384
    monotonicity_T_H_assert = bool(np.all(dT < 0))  # (local) strict
    assert monotonicity_T_H_assert, (
        "FATAL: T_H(g) is NOT strictly monotone decreasing — "
        "substitution chain Step 4 violated. Check Delta_BCS, K_base signs."
    )

    # f(g) non-increasing (discrete drops at thresholds)
    df = np.diff(f_g_table)  # (local) length 384
    monotonicity_f_g_assert = bool(np.all(df <= 1e-10))  # (local) non-increasing within tol

    # Cross-check at 3 anchors
    cross_checks = {}  # (local)
    for label, T_anchor in ANCHOR_T_GEV.items():
        cross_checks[label] = cross_check_at_anchor(
            T_anchor,
            ANCHOR_G_STAR_STANDARD[label],
            g_table,
            T_H_g_table,
            f_g_table,
        )

    n_pass = sum(1 for cc in cross_checks.values() if cc["PASS_within_10pct"])  # (local)
    n_info_only = sum(1 for cc in cross_checks.values()
                      if cc["INFO_within_30pct"] and not cc["PASS_within_10pct"])  # (local)

    # Composite verdict per §9 collapse rule
    if (n_pass == 3 and coverage_assert and monotonicity_T_H_assert):
        composite_verdict = "PASS"  # (local)
    elif (n_pass == 2 and coverage_assert and monotonicity_T_H_assert):
        composite_verdict = "INFO"  # (local)
    else:
        composite_verdict = "FAIL"  # (local)

    # Compute g_eff_at_T_H_substrate at the §W1-2-relevant T_H = 1.057 MeV
    # (BBN-anchor; needed by §W1-2 L_H multi-species correction)
    T_H_substrate_GeV = T_H_BBN_ANCHOR_GEV  # (local)
    g_eff_at_T_H_substrate = g_star_at_temperature(T_H_substrate_GeV)  # (local)

    # Identify g_BBN: smallest g s.t. T_H(g) <= 1 MeV (BBN entrance)
    BBN_threshold_GeV = 1.0e-3  # (local) BBN entrance
    g_BBN_idx = int(np.argmax(T_H_g_table <= BBN_threshold_GeV))  # (local)
    g_BBN = int(g_table[g_BBN_idx])  # (local)
    f_g_BBN = float(f_g_table[g_BBN_idx])  # (local)

    # SIGN-tuple verdict (Step 4 pre-registers monotonic-decreasing direction)
    # sign_verdict = PASS iff T_H(g) is strictly monotone decreasing (Step 4)
    sign_verdict = "PASS" if monotonicity_T_H_assert else "FAIL"  # (local)
    # magnitude_verdict per the 3-anchor pass-band
    if n_pass == 3:
        magnitude_verdict = "PASS"  # (local)
    elif n_pass == 2:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)
    # regime_verdict: VALID iff coverage and full {0..384} domain tested
    if coverage_assert and len(g_table) == G_RANGE:
        regime_verdict = "VALID"  # (local)
    else:
        regime_verdict = "BREAKDOWN"  # (local)

    return {
        "g_table": g_table,
        "T_H_g_table": T_H_g_table,
        "f_g_table": f_g_table,
        "coverage_assert": coverage_assert,
        "monotonicity_T_H_assert": monotonicity_T_H_assert,
        "monotonicity_f_g_assert": monotonicity_f_g_assert,
        "cross_checks": cross_checks,
        "n_pass": n_pass,
        "n_info_only": n_info_only,
        "composite_verdict": composite_verdict,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "g_eff_at_T_H_substrate": g_eff_at_T_H_substrate,
        "T_H_substrate_GeV": T_H_substrate_GeV,
        "g_BBN": g_BBN,
        "f_g_BBN": f_g_BBN,
        "T_H_initial_GeV": T_H_INITIAL_GEV,
    }


# ---------------------------------------------------------------------------
# Section 10 -- Plot emission
# ---------------------------------------------------------------------------

def write_png(result: dict) -> None:
    """2-panel plot per plan §6 step 4.

    Panel A: T_H(g) vs g log-y (substrate exponential cascade).
    Panel B: f(g) vs g with SM-threshold annotations.
    """
    g = result["g_table"]
    T_H = result["T_H_g_table"]
    f = result["f_g_table"]

    fig, (axA, axB) = plt.subplots(1, 2, figsize=(14, 5.5))

    # Panel A: T_H(g) on log-y
    axA.semilogy(g, T_H, "b-", linewidth=1.4, label=r"$T_H(g)$ (substrate cascade)")
    axA.set_xlabel("cascade generation $g$")
    axA.set_ylabel(r"$T_H(g)$ [GeV] (log scale)")
    axA.set_title(
        r"Substrate-IS exponential cascade: "
        r"$T_H(g) = T_{H,initial} \cdot \exp(-g \cdot \Delta_{BCS}/K_{base})$"
        f"\n$T_{{H,initial}}$ = {T_H_INITIAL_GEV:.3e} GeV; "
        f"$\\Delta_{{BCS}}/K_{{base}}$ = {Delta_BCS/K_base:.6f}"
    )
    # Anchor lines
    for label, T_anc in ANCHOR_T_GEV.items():
        axA.axhline(T_anc, linestyle="--", alpha=0.45,
                    color={"T_100GeV": "red", "T_1GeV": "orange",
                           "T_1MeV": "green"}[label],
                    label=f"{label} = {T_anc:.0e} GeV")
    axA.legend(loc="lower left", fontsize=8)
    axA.grid(True, which="both", alpha=0.3)

    # Panel B: f(g) vs g
    axB.plot(g, f, "k-", linewidth=1.4, label=r"$f(g) = g_*(T_H(g))$")
    axB.set_xlabel("cascade generation $g$")
    axB.set_ylabel(r"$f(g) = g_*(T_H(g))$")
    axB.set_title(
        r"Species-multiplicity lookup: "
        r"$f(g) = g_*(T_H(g))$"
        f"\nCross-check anchors PASS = {result['n_pass']}/3; "
        f"composite verdict = {result['composite_verdict']}"
    )
    # SM threshold annotations: for each particle, mark g where T_H(g) crosses mass
    threshold_labels = [  # (local)
        ("electron", 0.511e-3),
        ("muon", 105.7e-3),
        ("pion0", 134.98e-3),
        ("nucleon", 0.939),
        ("tau", 1.777),
        ("charm", 1.275),
        ("bottom", 4.18),
        ("Higgs", 125.10),
        ("WZ", 80.379),
        ("top", 173.0),
    ]
    rate = Delta_BCS / K_base  # (local)
    for name, m_GeV in threshold_labels:
        # g_threshold s.t. T_H(g) = m_GeV
        if 0 < m_GeV < T_H_INITIAL_GEV:
            g_thr = math.log(T_H_INITIAL_GEV / m_GeV) / rate  # (local)
            if G_MIN <= g_thr <= G_MAX:
                axB.axvline(g_thr, linestyle=":", color="grey", alpha=0.55, linewidth=0.8)
                axB.text(g_thr + 1, axB.get_ylim()[1] * 0.05 if axB.get_ylim()[1] > 1 else 0.05,
                         f"{name}\n{m_GeV*1000:.2g} MeV" if m_GeV < 1 else f"{name}\n{m_GeV:.1f} GeV",
                         rotation=90, fontsize=6.5, color="grey", va="bottom")
    # Cross-check anchor markers
    for label, cc in result["cross_checks"].items():
        color = {"T_100GeV": "red", "T_1GeV": "orange", "T_1MeV": "green"}[label]
        axB.axvline(cc["g_at_anchor"], linestyle="--", color=color, alpha=0.6,
                    label=f"{label}: f={cc['measured_f_g']:.2f} "
                          f"vs std {cc['standard_g_star']:.2f} "
                          f"(rel_dev={cc['rel_dev']*100:.2f}%)")
    axB.legend(loc="upper right", fontsize=7)
    axB.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 11 -- Verdict-line emission
# ---------------------------------------------------------------------------

def append_verdict(
    composite: str, value: str, audit_sha: str, content_sha: str,
    sign_v: str, mag_v: str, reg_v: str,
) -> None:
    """Append canonical S87+ schema-v2 verdict line + dual-SHA companion
    + 3-tuple companion row to s89_gate_verdicts.txt.

    Single-shot write_promotion -> fsync -> append (registry-landing.md
    §"Bridge-Landing Script Architecture" pattern).
    """
    canonical_line = (
        f"{GATE_ID}: {composite} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    # Schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row (REQUIRED per spawn prompt;
    # substitution chain Step 4 pre-registers monotonic-decreasing direction)
    threetuple_companion = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_companion)
        fp.write(threetuple_companion)
        fp.flush()
        try:
            os.fsync(fp.fileno())
        except OSError:
            pass


# ---------------------------------------------------------------------------
# Section 12 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    print(f"=== {GATE_ID} ===")
    print(f"Session: {SESSION}; gate: {GATE_ID}")
    print(f"Pre-reg: PASS_RATIO_TOL={PASS_RATIO_TOL}; "
          f"3 anchors at T in {list(ANCHOR_T_GEV.values())} GeV")
    print(f"Substrate-pinned T_H_initial = {T_H_INITIAL_GEV:.6e} GeV "
          f"(back-derived from g_BBN={G_BBN_ANCHOR}, T_H_BBN={T_H_BBN_ANCHOR_GEV*1000:.3f} MeV)")
    print(f"Delta_BCS = {Delta_BCS:.15g} (R-PROTECTED)")
    print(f"K_base    = {K_base} (S82 W2-4)")
    print(f"Delta_BCS / K_base = {Delta_BCS/K_base:.15g}")

    # Step A: log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure_hash: {closure[:16]}...")

    # Step B: run gate
    result = run_lookup_table_gate()  # (local)
    print()
    print(f"Coverage assert:        {result['coverage_assert']}")
    print(f"Monotonicity T_H assert: {result['monotonicity_T_H_assert']}")
    print(f"Monotonicity f(g) assert: {result['monotonicity_f_g_assert']}")
    print(f"T_H(g=0)   = {result['T_H_g_table'][0]:.6e} GeV")
    print(f"T_H(g=384) = {result['T_H_g_table'][-1]:.6e} GeV")
    print()
    print(f"Cross-check anchors:")
    for label, cc in result["cross_checks"].items():
        verdict_tag = "PASS" if cc["PASS_within_10pct"] else (
            "INFO" if cc["INFO_within_30pct"] else "FAIL")
        print(f"  {label} (T_anchor={cc['T_anchor_GeV']:.3e} GeV): "
              f"g={cc['g_at_anchor']}; T_H(g)={cc['T_H_at_anchor_GeV']:.4e} GeV; "
              f"f(g)={cc['measured_f_g']:.3f} vs std {cc['standard_g_star']:.2f}; "
              f"rel_dev={cc['rel_dev']*100:.3f}% [{verdict_tag}]")
    print()
    print(f"n_pass = {result['n_pass']}/3; "
          f"composite_verdict = {result['composite_verdict']}")
    print(f"sign_verdict={result['sign_verdict']}; "
          f"magnitude_verdict={result['magnitude_verdict']}; "
          f"regime_verdict={result['regime_verdict']}")
    print()
    print(f"For §W1-2 / §W1-4 dependency:")
    print(f"  T_H_substrate = {result['T_H_substrate_GeV']*1000:.3f} MeV; "
          f"g_eff_at_T_H_substrate = {result['g_eff_at_T_H_substrate']:.3f}")
    print(f"  g_BBN = {result['g_BBN']}; f_g_BBN = {result['f_g_BBN']:.3f}")

    # Step C: Compute dual-SHA + write artifacts
    audit_sha, content_sha = compute_dual_sha(  # (local)
        Path(__file__).resolve(),
        INPUT_CANONICAL_CONSTANTS,
        pins,
    )

    # Save .npz (full lookup table + cross-check dict)
    np.savez(
        OUT_NPZ,
        g_table=result["g_table"],
        T_H_g_table=result["T_H_g_table"],
        f_g_table=result["f_g_table"],
        coverage_assert=np.array(result["coverage_assert"]),
        monotonicity_assert=np.array(result["monotonicity_T_H_assert"]),
        monotonicity_f_g_assert=np.array(result["monotonicity_f_g_assert"]),
        cross_check_at_T_100GeV=np.array(
            json.dumps(result["cross_checks"]["T_100GeV"]), dtype=object),
        cross_check_at_T_1GeV=np.array(
            json.dumps(result["cross_checks"]["T_1GeV"]), dtype=object),
        cross_check_at_T_1MeV=np.array(
            json.dumps(result["cross_checks"]["T_1MeV"]), dtype=object),
        g_eff_at_T_H_substrate=result["g_eff_at_T_H_substrate"],
        T_H_substrate_GeV=result["T_H_substrate_GeV"],
        g_BBN=result["g_BBN"],
        f_g_BBN=result["f_g_BBN"],
        T_H_initial_GeV=result["T_H_initial_GeV"],
        T_H_initial_back_derived_from_g_BBN=G_BBN_ANCHOR,
        T_H_initial_back_derived_from_T_H_BBN_GeV=T_H_BBN_ANCHOR_GEV,
        Delta_BCS=Delta_BCS,
        K_base=K_base,
        n_pass_anchors=result["n_pass"],
        composite_verdict=result["composite_verdict"],
        sign_verdict=result["sign_verdict"],
        magnitude_verdict=result["magnitude_verdict"],
        regime_verdict=result["regime_verdict"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"Wrote .npz: {OUT_NPZ}")

    # Plot
    write_png(result)
    print(f"Wrote .png: {OUT_PNG}")

    # Verdict value-string per §8
    value_str = (  # (local)
        f"coverage={'Pass' if result['coverage_assert'] else 'Fail'};"
        f"cross_checks_passed={result['n_pass']}/3"
    )

    # Step D: append verdict line
    append_verdict(
        result["composite_verdict"],
        value_str,
        audit_sha,
        content_sha,
        result["sign_verdict"],
        result["magnitude_verdict"],
        result["regime_verdict"],
    )
    print(f"Appended verdict line to {VERDICT_TXT}")
    print()
    print(f"audit_sha256:   {audit_sha}")
    print(f"content_sha256: {content_sha}")
    print()

    # Final 4-tuple line per output-standards.md (final non-verdict line)
    print(
        f"4-tuple: (value={value_str!r}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX})"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
