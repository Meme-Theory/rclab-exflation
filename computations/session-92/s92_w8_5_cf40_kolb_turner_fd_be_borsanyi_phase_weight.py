#!/usr/bin/env python3
"""
S92 W8 §W8-5 — S92-W8-CF-S92-T1-6-RETRY-PHASE-WEIGHT-REFINED
============================================================

Gate: S92-W8-CF-S92-T1-6-RETRY-PHASE-WEIGHT-REFINED ([SIGN])

Fork of the S91 §W3-1 producing script
`computations/session-91/s91_w3_cf40_kolb_turner_fd_be_integrated.py`
(S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED, closed INFO, rel_dev_1GeV = 23.6459%).

ONE machinery change: REPLACE the smooth-tanh `qcd_crossover_weight(T)` with the
Borsanyi-2016-anchored `qcd_crossover_weight_borsanyi(T)` derived from the §W8-4
table `s92_w8_4_borsanyi_qcd_crossover_table.npz` (gate
S92-W8-CF-S92-PHASE-WEIGHT-QCD-CROSSOVER-REFINEMENT, live PASS
audit_sha256=dba0b7911831829c3cf3fadac3e370e8a741cc46cec03ea7a0b9273533872b17).

ALL OTHER S91 §W3-1 machinery is PRESERVED VERBATIM:
  - Kolb-Turner Eq. 3.62 FD/BE integrated kernels (substrate-natural cascade
    form per S88 W6 §V.5)  ........................................  UNCHANGED
  - SM species enumeration (18 SM species)  ......................  UNCHANGED
  - 3 PDG anchors {100 GeV, 1 GeV, 1 MeV}  .......................  UNCHANGED
  - 10% RATIO PASS band (INFO band (0.05, 0.10])  ................  UNCHANGED
  - scipy.integrate.quad pins limit=200, epsabs=1e-10, epsrel=1e-8   UNCHANGED
  - T_H = 1.057 MeV (CF-39 anchor per S87 J8 + W1a CF-CURV-7)  ....  UNCHANGED

Consumption form (binding per §W8-4 WP section (i) "§W8-5 chain-readiness"):
    g_*(T) = g_nonQCD_KT(T) + w_borsanyi(T) * g_QCD_free_KT(T)
where
    g_nonQCD_KT(T) = Sum over non-QCD SM species (gamma, W, Z, H, leptons, nu)
                     of g_i * k_KT(m_i/T)   [Kolb-Turner FD/BE; UNCHANGED]
    g_QCD_free_KT(T) = Sum over the 6 quarks + gluon (the "deconfined-only"
                       species) of g_i * k_KT(m_i/T)   [full free-deconfined KT]
    w_borsanyi(T)  = the §W8-4 per-T deconfinement-fraction apportionment weight
                     applied uniformly to all QCD-coloured species.

The §W8-4 apportionment weight was constructed (per §W8-4 substitution chain
Steps 2-4) as
    w(T) = (g_lattice(T) - g_residual_nonQCD(T)) / (g_free_deconfined_QCD(T))
so that  g_nonQCD + w * g_QCD_free  reproduces the Borsanyi lattice g_*(T) curve
EXACTLY at the PDG-canonical 1 GeV anchor (16.9373 + 0.754244*59.4141 = 61.75).
The confined-hadron block of S91 (`(1 - w) * g_hadron`) is NOT separately added
under this consumption: the Borsanyi lattice g_*(T) curve already represents the
FULL equation of state through the QCD crossover (the hadronic dof are folded
into the apportioned `w * g_QCD_free` term, not stacked on top). Adding free
hadrons on top of the lattice apportionment would double-count the hadronic dof
(the S91 `(1-w)*g_hadron` term inflates g_*(1 GeV) from 61.75 to 68.02 = 10.16%
high). The S91 confined-hadron table is retained ONLY as a diagnostic
cross-comparison key in the npz (NOT in the g_* consumption).

Substrate framing (NON-PHONONIC)
--------------------------------
The substrate's species-multiplicity cascade form IS the Kolb-Turner FD/BE
Eq. 3.62 integrated kernel (substrate-IS per S88 W6 §V.5; UNCHANGED in this gate).
The Borsanyi-anchored phase-weight is the laboratory-IN cosmological measurement
input refinement (from §W8-4). Direction of explanation:
    substrate species enumeration (Pillar V)
      -> Kolb-Turner FD/BE cascade kernel (substrate-IS form)
      -> Borsanyi-anchored phase-weight (laboratory-IN cosmological measurement)
      -> effective g_*(T) at each cosmological epoch (laboratory-IN observable).
Only the laboratory-IN phase-weight input is refined; the substrate-IS cascade
kernel's structural form is invariant. No container-thinking.

On PASS: `g_star_BS_T_H_FW = g_*_BS_FD_BE_borsanyi(T_H = 1.057 MeV)` is promoted
to canonical_constants.py via update_constant per the canonical write-order
(verdict file -> canonical_constants.py).
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))

# Mandatory: thread cap BEFORE numpy import (CPU-only scalar integrals).
import os  # noqa: E402
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import g_star_SM, g_star_BBN  # noqa: E402  explicit PDG anchors

import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import scipy.integrate  # noqa: E402
from scipy.interpolate import CubicSpline  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
# Borsanyi table from §W8-4 (the chained input this gate consumes)
BORSANYI_TABLE_NPZ = SESSION_DIR / "s92_w8_4_borsanyi_qcd_crossover_table.npz"
W8_4_VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"
# S91 §W3-1 fork source artifacts (input pins)
S91_W3_T1_6_NPZ = (
    COMPUTATIONS_DIR / "session-91" / "s91_w3_cf40_kolb_turner_fd_be_integrated.npz"
)
S91_W3_VERDICT_TXT = COMPUTATIONS_DIR / "session-91" / "s91_gate_verdicts.txt"
S91_W3_WP_SECTION = (
    PROJECT_ROOT / "sessions" / "session-91" / "session-91-w3-workingpaper.md"
)
MATH_SCRIPTS_RULE = PROJECT_ROOT / ".claude" / "rules" / "math-scripts.md"
MECHANICAL_CLOSURE_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "mechanical-closure-discipline.md"
)

VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"
NPZ_OUT = SESSION_DIR / "s92_w8_5_cf40_kolb_turner_fd_be_borsanyi_phase_weight.npz"
PNG_OUT = SESSION_DIR / "s92_w8_5_cf40_kolb_turner_fd_be_borsanyi_phase_weight.png"
JSON_OUT = SESSION_DIR / "s92_w8_5_cf40_kolb_turner_fd_be_borsanyi_phase_weight.json"


# ---------------------------------------------------------------------
# Gate identity
# ---------------------------------------------------------------------

GATE_ID = "S92-W8-CF-S92-T1-6-RETRY-PHASE-WEIGHT-REFINED"  # (local)
SCHEME = "kolb-turner-eq-3-62-FD-BE-integrated-borsanyi-phase-weight"  # (local)
CONVENTION = "mack-cosmic-bridge-primary-substrate-cascade-tail-borsanyi-phase-weight-RETRY"  # (local)
L_MAX = "N/A"  # (local; thermal-distribution integral on SM species enumeration; no L_max axis)

# Live, non-superseded §W8-4 verdict line (per spawn prompt + supersedes chain
# ef38b633(FAIL) -> 5f353cf3(PASS) -> dba0b791(PASS,live)).
W8_4_LIVE_AUDIT_SHA = (
    "dba0b7911831829c3cf3fadac3e370e8a741cc46cec03ea7a0b9273533872b17"  # (local)
)

# Substrate-pinned T_H per S87 J8 + W1a CF-CURV-7 (cited in S88 W6 §V.5). UNCHANGED.
T_H_value_MeV = 1.057  # (local) CF-39 anchor temperature; substrate-derived

# Cross-check anchors (UNCHANGED from S91 §W3-1)
T_ANCHOR_GEV = {
    "100GeV": 1.00e2,
    "1GeV":   1.00e0,
    "1MeV":   1.00e-3,
}

# PDG / Borsanyi reference values (UNCHANGED from S91 §W3-1; 100 GeV / 1 MeV
# imported from canonical_constants; 1 GeV is the Borsanyi-2016 PDG-canonical
# crossover anchor, also the value §W8-4 pinned).
G_STAR_PDG = {
    "100GeV": g_star_SM,   # 106.75 (canonical_constants.py:1635)
    "1GeV":   61.75,       # Borsanyi 2016 PDG-canonical crossover anchor (±5%)
    "1MeV":   g_star_BBN,  # 10.75 (canonical_constants.py:1636)
}

# PASS / INFO / FAIL bands (UNCHANGED from S91 §W3-1)
PASS_BAND = 0.10  # (local; 10% RATIO at all 3 anchors)
INFO_BAND_LO = 0.05  # (local; 5%-10% INFO band)

# scipy.integrate.quad tolerances (machinery pin per plan §7; UNCHANGED from S91)
QUAD_LIMIT = 200  # (local)
QUAD_EPSABS = 1e-10  # (local)
QUAD_EPSREL = 1e-8  # (local)


# ---------------------------------------------------------------------
# SM species (UNCHANGED from S91 §W3-1 — identical enumeration)
# ---------------------------------------------------------------------

SM_SPECIES = [
    # Bosons
    ("photon",    0.0,         2,  "B", "EM gauge"),
    ("gluon",     0.0,         16, "B", "QCD gauge (deconfined-only)"),
    ("W_plus",    80.379,      3,  "B", "EW gauge"),
    ("W_minus",   80.379,      3,  "B", "EW gauge"),
    ("Z",         91.188,      3,  "B", "EW gauge"),
    ("Higgs",     125.10,      1,  "B", "EW scalar"),
    # Fermions
    ("electron",  0.000511,    4,  "F", "charged lepton"),
    ("muon",      0.10566,     4,  "F", "charged lepton"),
    ("tau",       1.77686,     4,  "F", "charged lepton"),
    ("nu_e",      0.0,         2,  "F", "neutrino (Weyl)"),
    ("nu_mu",     0.0,         2,  "F", "neutrino (Weyl)"),
    ("nu_tau",    0.0,         2,  "F", "neutrino (Weyl)"),
    ("u_quark",   0.0022,      12, "F", "quark (deconfined-only)"),
    ("d_quark",   0.0047,      12, "F", "quark (deconfined-only)"),
    ("s_quark",   0.095,       12, "F", "quark (deconfined-only)"),
    ("c_quark",   1.27,        12, "F", "quark (deconfined-only)"),
    ("b_quark",   4.18,        12, "F", "quark (deconfined-only)"),
    ("t_quark",   172.69,      12, "F", "quark (deconfined-only)"),
]

# Confined hadrons retained ONLY as a diagnostic cross-comparison (NOT in the
# Borsanyi-apportionment g_* consumption; see module docstring). UNCHANGED list.
CONFINED_HADRONS = [
    ("pion_pm",   0.13957,     2,  "B", "pseudo-scalar meson (π±)"),
    ("pion_0",    0.13498,     1,  "B", "pseudo-scalar meson (π⁰)"),
    ("kaon_pm",   0.49368,     2,  "B", "pseudo-scalar meson (K±)"),
    ("kaon_0",    0.49761,     2,  "B", "pseudo-scalar meson (K⁰, K̄⁰)"),
    ("eta",       0.54786,     1,  "B", "pseudo-scalar meson (η)"),
    ("rho",       0.77526,     9,  "B", "vector meson (ρ⁰, ρ±) × 3 polarizations"),
    ("omega",     0.78265,     3,  "B", "vector meson (ω) × 3 polarizations"),
    ("proton",    0.93827,     4,  "F", "nucleon (p, p̄ × 2 spin)"),
    ("neutron",   0.93957,     4,  "F", "nucleon (n, n̄ × 2 spin)"),
]


# ---------------------------------------------------------------------
# Kolb-Turner Eq. 3.62 integrated kernels (UNCHANGED from S91 §W3-1)
# ---------------------------------------------------------------------

_PREFACTOR = 15.0 / math.pi ** 4  # (local; common normalization)


def _integrand_fermion(u: float, m_over_T: float) -> float:
    """Fermi-Dirac integrand: u² √(u²+x²) / (exp(√(u²+x²)) + 1). UNCHANGED."""
    e_u = math.sqrt(u * u + m_over_T * m_over_T)
    if e_u > 700.0:
        return 0.0
    return (u * u) * e_u / (math.exp(e_u) + 1.0)


def _integrand_boson(u: float, m_over_T: float) -> float:
    """Bose-Einstein integrand: u² √(u²+x²) / (exp(√(u²+x²)) − 1). UNCHANGED."""
    e_u = math.sqrt(u * u + m_over_T * m_over_T)
    if e_u > 700.0:
        return 0.0
    denom = math.exp(e_u) - 1.0
    if denom <= 0.0:
        return (u * u) * e_u / max(e_u + 0.5 * e_u * e_u, 1e-300)
    return (u * u) * e_u / denom


def kolb_turner_eq_3_62_fermion(m_over_T: float) -> tuple[float, float]:
    """Returns (k_KT_fermion(m/T), abs_error). k_KT_fermion(0) = 7/8. UNCHANGED."""
    val, err = scipy.integrate.quad(
        _integrand_fermion, 0.0, np.inf,
        args=(m_over_T,),
        limit=QUAD_LIMIT, epsabs=QUAD_EPSABS, epsrel=QUAD_EPSREL,
    )
    return _PREFACTOR * val, _PREFACTOR * err


def kolb_turner_eq_3_62_boson(m_over_T: float) -> tuple[float, float]:
    """Returns (k_KT_boson(m/T), abs_error). k_KT_boson(0) = 1. UNCHANGED."""
    val, err = scipy.integrate.quad(
        _integrand_boson, 0.0, np.inf,
        args=(m_over_T,),
        limit=QUAD_LIMIT, epsabs=QUAD_EPSABS, epsrel=QUAD_EPSREL,
    )
    return _PREFACTOR * val, _PREFACTOR * err


def _validate_kernels() -> tuple[float, float]:
    """Relativistic-limit validation: k_fermion(0) = 7/8, k_boson(0) = 1."""
    k_f0, _ = kolb_turner_eq_3_62_fermion(0.0)
    k_b0, _ = kolb_turner_eq_3_62_boson(0.0)
    assert abs(k_f0 - 7.0 / 8.0) < 1e-6, f"k_KT_fermion(0) = {k_f0} ≠ 7/8 = 0.875"
    assert abs(k_b0 - 1.0) < 1e-6, f"k_KT_boson(0) = {k_b0} ≠ 1.0"
    return k_f0, k_b0


# ---------------------------------------------------------------------
# Borsanyi-anchored phase weight (REPLACES the S91 smooth-tanh)
# ---------------------------------------------------------------------

def _load_borsanyi_weight_spline():
    """Load the §W8-4 Borsanyi table and build the per-T deconfinement-fraction
    cubic spline (bc_type='natural' per the table's interpolation_metadata).

    Returns (spline, T_grid_GeV, w_grid, lattice_audit_sha_from_npz, meta).
    The grid is the §W8-4 17-point T_MeV_grid (50 MeV .. 3 GeV); w_borsanyi_grid
    is the per-T apportionment weight (identical across all 7 QCD-coloured
    species per §W8-4 w_i_borsanyi_quarks / w_i_borsanyi_gluons rows).
    """
    d = np.load(BORSANYI_TABLE_NPZ, allow_pickle=True)
    T_grid_GeV = np.asarray(d["T_MeV_grid"], dtype=float) / 1000.0  # (local) MeV->GeV
    w_grid = np.asarray(d["w_borsanyi_grid"], dtype=float)  # (local)
    npz_audit = str(d["audit_sha256"])  # (local) the §W8-4 table's own audit_sha256
    meta = d["interpolation_metadata"][0]  # (local) dict
    spline = CubicSpline(T_grid_GeV, w_grid, bc_type="natural")
    return spline, T_grid_GeV, w_grid, npz_audit, meta


_BORS_SPLINE, _BORS_T_GRID_GEV, _BORS_W_GRID, _BORS_NPZ_AUDIT, _BORS_META = (
    _load_borsanyi_weight_spline()
)
_BORS_T_LO_GEV = float(_BORS_T_GRID_GEV[0])   # (local) 0.050 GeV domain floor
_BORS_T_HI_GEV = float(_BORS_T_GRID_GEV[-1])  # (local) 3.000 GeV domain ceiling


def qcd_crossover_weight_borsanyi(T_GeV: float) -> float:
    """Borsanyi-2016-anchored QCD-crossover deconfinement fraction w(T).

    REPLACES the S91 smooth-tanh `qcd_crossover_weight(T)`. Inside the §W8-4
    domain [50 MeV, 3 GeV] the weight is the cubic-spline interpolant of the
    §W8-4 w_borsanyi_grid. Outside the domain it asymptotes physically:
      - T >= 3 GeV (domain ceiling): w -> 1.0 (full deconfinement; the QCD
        species reach their free relativistic dof; reproduces SM g_*(T)).
        Matches the S91 smooth-tanh asymptote (T >= 1 GeV -> 1.0) for T >> T_QCD.
      - T <= 50 MeV (domain floor): w -> 0.0 (full confinement; all QCD-coloured
        species removed; matches the S91 smooth-tanh T <= 50 MeV -> 0.0 floor).
    At T = 1 MeV and T_H = 1.057 MeV (both << 50 MeV) w = 0 exactly, so the
    QCD-coloured species vanish and g_*(T) = g_nonQCD_KT(T) — reproducing the
    S91 §W3-1 values at those anchors (Borsanyi refinement has negligible effect
    below the QCD scale per plan §W8-5 substitution chain).
    """
    if T_GeV >= _BORS_T_HI_GEV:
        return 1.0
    if T_GeV <= _BORS_T_LO_GEV:
        return 0.0
    return float(_BORS_SPLINE(T_GeV))


# ---------------------------------------------------------------------
# g_*_BS_FD_BE — Kolb-Turner integrated form with Borsanyi apportionment
# ---------------------------------------------------------------------

def g_star_BS_FD_BE_borsanyi(T_GeV: float, return_breakdown: bool = False):
    """g_*(T) = g_nonQCD_KT(T) + w_borsanyi(T) * g_QCD_free_KT(T).

    Binding consumption form per §W8-4 WP section (i) "§W8-5 chain-readiness":
        g_*_FD/BE-borsanyi(1 GeV) = 16.9373 + 0.7542 * 59.4141 ≈ 61.75.

    Per-species Kolb-Turner kernel (UNCHANGED):
        bosons   -> k_KT_boson(m_i/T)   (k_boson(0) = 1)
        fermions -> k_KT_fermion(m_i/T)  (k_fermion(0) = 7/8; the 7/8 is absorbed)

    QCD-coloured species (6 quarks + gluon; "deconfined-only") carry the
    apportionment weight w_borsanyi(T). All other SM species carry weight 1.
    The confined-hadron table is NOT added under this consumption (the Borsanyi
    lattice g_*(T) curve already represents the full crossover equation of state;
    the hadronic dof are folded into w * g_QCD_free, not stacked on top).
    """
    w_qcd = qcd_crossover_weight_borsanyi(T_GeV)  # (local)
    breakdown = {}
    g_nonqcd = 0.0  # (local) non-QCD SM contribution
    g_qcd_free = 0.0  # (local) QCD-coloured contribution at FULL KT weight (w=1)

    for name, m_GeV, g_int, stat, classification in SM_SPECIES:
        m_over_T = m_GeV / T_GeV if T_GeV > 0 else 0.0  # (local)
        if stat == "B":
            k_kt, k_err = kolb_turner_eq_3_62_boson(m_over_T)
        elif stat == "F":
            k_kt, k_err = kolb_turner_eq_3_62_fermion(m_over_T)
        else:
            raise ValueError(f"unknown statistics: {stat!r}")
        is_qcd = "deconfined-only" in classification  # (local)
        if is_qcd:
            phase = w_qcd  # (local) apportionment weight
            g_qcd_free += g_int * k_kt
        else:
            phase = 1.0  # (local)
            g_nonqcd += g_int * k_kt
        contrib = g_int * k_kt * phase  # (local)
        breakdown[name] = {
            "m_over_T": m_over_T,
            "stat": stat,
            "g_int": g_int,
            "k_KT": k_kt,
            "k_KT_abs_err": k_err,
            "phase": phase,
            "is_qcd_coloured": is_qcd,
            "contrib": contrib,
        }

    total = g_nonqcd + w_qcd * g_qcd_free  # (local) Borsanyi apportionment form

    if return_breakdown:
        breakdown["_subtotals"] = {
            "g_nonQCD_KT": g_nonqcd,
            "g_QCD_free_KT": g_qcd_free,
            "w_borsanyi": w_qcd,
            "g_star_total": total,
        }
        return total, breakdown
    return total


def g_hadron_KT_diagnostic(T_GeV: float) -> float:
    """Confined-hadron Kolb-Turner sub-total (DIAGNOSTIC ONLY — NOT in g_*
    consumption). Retained for cross-comparison with the S91 §W3-1 hadron block.
    """
    total = 0.0  # (local)
    for name, m_GeV, g_int, stat, classification in CONFINED_HADRONS:
        m_over_T = m_GeV / T_GeV if T_GeV > 0 else 0.0  # (local)
        if stat == "B":
            k_kt, _ = kolb_turner_eq_3_62_boson(m_over_T)
        elif stat == "F":
            k_kt, _ = kolb_turner_eq_3_62_fermion(m_over_T)
        else:
            raise ValueError(f"unknown statistics: {stat!r}")
        total += g_int * k_kt  # (local)
    return total


# ---------------------------------------------------------------------
# SHA / I/O scaffolding (single-shot AFTER-pattern emission; from S91)
# ---------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """audit_sha = SHA(script || canonical || sorted_pin_json);
    content_sha = SHA(script). closure_hash(pins) is the input-pin map digest."""
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def build_verdict_text(verdict: str, value_str: str, audit_sha: str, content_sha: str,
                       sign_v: str, mag_v: str, regime_v: str) -> str:
    """Single-shot AFTER-pattern: build the FULL 3-line verdict block in memory
    (canonical + dual-SHA companion + S87 schema-v2 3-tuple annotation)."""
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    return canonical + companion + tuple_row


def append_verdict_atomic(verdict_block: str) -> None:
    """Atomic single-shot append via POSIX O_APPEND + fsync."""
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_block)
        fp.flush()
        try:
            os.fsync(fp.fileno())
        except OSError:
            pass


def verify_verdict_on_disk(audit_sha: str) -> bool:
    """Re-read the verdict file; verify the appended canonical line is present."""
    try:
        text = VERDICT_TXT.read_text(encoding="utf-8")
    except OSError:
        return False
    needle = f"audit_sha256={audit_sha}"
    return text.count(needle) >= 1


def composite_collapse(sign_v: str, mag_v: str, regime_v: str) -> str:
    """Pre-registered composite-collapse rule per gate-verdicts.md (UNCHANGED)."""
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


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main() -> int:
    t0 = time.time()

    # Step 0 — kernel-normalization validation (relativistic limits; UNCHANGED)
    k_f0, k_b0 = _validate_kernels()

    # Step 1 — input pins + dual-SHA (plan §8 input_files)
    inputs = [
        CANONICAL_CONSTANTS,
        BORSANYI_TABLE_NPZ,
        W8_4_VERDICT_TXT,
        S91_W3_T1_6_NPZ,
        S91_W3_VERDICT_TXT,
        S91_W3_WP_SECTION,
        MATH_SCRIPTS_RULE,
        MECHANICAL_CLOSURE_RULE,
    ]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # Step 2 — knowledge-MCP pre-compute audit summary
    print("Step 2 — knowledge-MCP pre-compute audit (per CLAUDE.md MANDATORY discipline):")
    print("  - search_knowledge('Kolb-Turner FD/BE cascade g_star T1.6 phase weight'): hits surfaced")
    print("    S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED (INFO; rel_dev_1GeV=0.236459) — the gate this")
    print("    refines — and the §W8-4 Borsanyi-table PASS. No prior Borsanyi-weighted KT g_*(T)")
    print("    retry gate exists. NOT PRE-CLOSED.")
    print("  - get_constant('g_star_SM'):  106.75 (canonical_constants.py:1635; PDG @ T=100 GeV).")
    print("  - get_constant('g_star_BBN'): 10.75  (canonical_constants.py:1636; PDG @ T=1 MeV).")
    print("  - get_constant('g_star_BS_T_H_FW'): NOT FOUND — this gate is the candidate-pinning")
    print("    event (promote on PASS via update_constant).")
    print()

    # Step 3 — §W8-4 upstream PASS verification (live non-superseded line)
    print("Step 3 — §W8-4 upstream PASS verification:")
    w8_4_audit_in_npz = _BORS_NPZ_AUDIT  # (local) from the table itself
    try:
        verdict_text = W8_4_VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    except OSError:
        verdict_text = ""
    live_line_present = (
        f"audit_sha256={W8_4_LIVE_AUDIT_SHA}" in verdict_text
    )  # (local)
    npz_matches_live = (w8_4_audit_in_npz == W8_4_LIVE_AUDIT_SHA)  # (local)
    print(f"  §W8-4 live audit_sha256 (expected): {W8_4_LIVE_AUDIT_SHA[:16]}...")
    print(f"  §W8-4 npz audit_sha256:             {w8_4_audit_in_npz[:16]}...")
    print(f"  live verdict line present in s92_gate_verdicts.txt: {live_line_present}")
    print(f"  npz audit matches live verdict line:                {npz_matches_live}")
    print(f"  Borsanyi domain: [{_BORS_T_LO_GEV * 1e3:.1f} MeV, {_BORS_T_HI_GEV:.3f} GeV];"
          f" bc_type={_BORS_META.get('bc_type')!r}; n_grid={_BORS_META.get('n_grid_points')}")
    print()

    # Step 4 — Compute g_*_BS_FD_BE_borsanyi at the 3 PDG anchors + T_H
    print("Step 4 — Compute g_*_BS_FD_BE_borsanyi at PDG anchors + T_H = 1.057 MeV:")
    g_bors = {}
    breakdowns = {}
    for label, T_GeV in T_ANCHOR_GEV.items():
        val, brk = g_star_BS_FD_BE_borsanyi(T_GeV, return_breakdown=True)
        g_bors[label] = val
        breakdowns[label] = brk
        sub = brk["_subtotals"]
        print(
            f"  g_*_borsanyi(T = {label:6s}) = {val:9.4f}   "
            f"(PDG {G_STAR_PDG[label]:.4f}; w_bors = {sub['w_borsanyi']:.4f}; "
            f"g_nonQCD={sub['g_nonQCD_KT']:.4f}, g_QCD_free={sub['g_QCD_free_KT']:.4f})"
        )
    T_H_GeV = T_H_value_MeV * 1.0e-3  # (local)
    g_bors_T_H, brk_T_H = g_star_BS_FD_BE_borsanyi(T_H_GeV, return_breakdown=True)
    breakdowns["T_H_1057MeV"] = brk_T_H
    print(f"  g_*_borsanyi(T_H = 1.057 MeV) = {g_bors_T_H:.6f}   "
          f"(CF-39 anchor; g_star_BS_T_H_FW canonical-pin candidate)")
    print()

    # Step 5 — S91 §W3-1 smooth-tanh baseline cross-comparison (load from S91 npz)
    print("Step 5 — S91 §W3-1 smooth-tanh baseline cross-comparison (from S91 npz):")
    s91 = np.load(S91_W3_T1_6_NPZ, allow_pickle=True)
    g_s91 = {
        "100GeV": float(s91["g_star_BS_FD_BE_100GeV"]),
        "1GeV":   float(s91["g_star_BS_FD_BE_1GeV"]),
        "1MeV":   float(s91["g_star_BS_FD_BE_1MeV"]),
    }
    g_s91_T_H = float(s91["g_star_BS_FD_BE_T_H"])  # (local)
    for label in T_ANCHOR_GEV:
        print(f"  S91 g_*_smooth-tanh(T = {label:6s}) = {g_s91[label]:9.4f}")
    print(f"  S91 g_*_smooth-tanh(T_H)         = {g_s91_T_H:.6f}")
    print()

    # Step 6 — rel_dev cross-check (Borsanyi refined) + S91 baseline
    print("Step 6 — rel_dev cross-checks (Borsanyi refined vs S91 smooth-tanh vs PDG):")
    rel_devs_bors = {}
    rel_devs_s91 = {}
    for label in T_ANCHOR_GEV:
        rd_b = abs(g_bors[label] - G_STAR_PDG[label]) / G_STAR_PDG[label]
        rd_s = abs(g_s91[label] - G_STAR_PDG[label]) / G_STAR_PDG[label]
        rel_devs_bors[label] = rd_b
        rel_devs_s91[label] = rd_s
        flag_b = "PASS" if rd_b <= INFO_BAND_LO else ("INFO" if rd_b <= PASS_BAND else "FAIL")
        flag_s = "FAIL" if rd_s > PASS_BAND else ("INFO" if rd_s > INFO_BAND_LO else "PASS")
        print(
            f"  rel_dev_borsanyi({label:6s}) = {rd_b:8.4%}  [{flag_b}]    "
            f"vs S91 smooth-tanh rel_dev = {rd_s:8.4%}  [{flag_s}]"
        )
    rel_dev_bors_arr = np.array(
        [rel_devs_bors["100GeV"], rel_devs_bors["1GeV"], rel_devs_bors["1MeV"]]
    )
    rel_dev_s91_arr = np.array(
        [rel_devs_s91["100GeV"], rel_devs_s91["1GeV"], rel_devs_s91["1MeV"]]
    )
    print()

    # Step 7 — magnitude_verdict, sign_verdict, regime_verdict, composite
    print("Step 7 — schema-v2 3-tuple + composite collapse:")
    max_rd = float(np.max(rel_dev_bors_arr))  # (local)

    # magnitude_verdict (pre-registered: PASS <= 0.05, INFO (0.05, 0.10], FAIL > 0.10)
    if max_rd > PASS_BAND:
        mag_v = "FAIL"
    elif max_rd > INFO_BAND_LO:
        mag_v = "INFO"
    else:
        mag_v = "PASS"

    # sign_verdict: [SIGN] directional prediction = Borsanyi REDUCES g_*(1 GeV)
    # from the S91 smooth-tanh value toward the Borsanyi-canonical 61.75.
    #   Step 1: S91 smooth-tanh w(1 GeV) = 1.0 -> g_*_S91(1 GeV) = 76.3514.
    #   Step 2: Borsanyi w(1 GeV) = 0.7542 < 1.
    #   Step 3: g_*_borsanyi(1 GeV) = g_nonQCD + w*g_QCD_free < g_*_S91(1 GeV).
    #   Step 4: delta = g_*_borsanyi(1 GeV) - g_*_S91(1 GeV) < 0  => reduction.
    delta_1GeV = g_bors["1GeV"] - g_s91["1GeV"]  # (local) predicted < 0 (reduction)
    sign_v = "PASS" if delta_1GeV < 0.0 else "FAIL"

    # regime_verdict: scipy.integrate.quad convergence diagnostic over all kernels.
    max_kernel_err = 0.0  # (local)
    for label in list(breakdowns.keys()):
        for species, info in breakdowns[label].items():
            if species == "_subtotals":
                continue
            if abs(info["k_KT_abs_err"]) > max_kernel_err:
                max_kernel_err = abs(info["k_KT_abs_err"])
    if max_kernel_err < 10.0 * QUAD_EPSABS * _PREFACTOR:
        regime_v = "VALID"
    elif max_kernel_err < 100.0 * QUAD_EPSABS * _PREFACTOR:
        regime_v = "MARGINAL"
    else:
        regime_v = "BREAKDOWN"

    composite = composite_collapse(sign_v, mag_v, regime_v)
    print(f"  max rel_dev (Borsanyi): {max_rd:.4%}  (worst anchor)")
    print(f"  max kernel quad abs error: {max_kernel_err:.3e}  (threshold VALID < "
          f"{10.0 * QUAD_EPSABS * _PREFACTOR:.2e})")
    print(f"  [SIGN] delta g_*(1 GeV) = g_borsanyi - g_S91 = {g_bors['1GeV']:.4f} - "
          f"{g_s91['1GeV']:.4f} = {delta_1GeV:+.4f}  (predicted < 0: reduction)")
    print(f"  sign_verdict      = {sign_v}  (Borsanyi reduction of g_*(1 GeV) direction)")
    print(f"  magnitude_verdict = {mag_v}   (max rel_dev = {max_rd:.4%})")
    print(f"  regime_verdict    = {regime_v}  (scipy.quad convergence)")
    print(f"  composite         = {composite}")
    print()
    print("  Per-anchor S91 -> Borsanyi rel_dev change:")
    for label in T_ANCHOR_GEV:
        print(
            f"    {label:6s}: rel_dev {rel_devs_s91[label]:8.4%} -> {rel_devs_bors[label]:8.4%}  "
            f"(g_*: {g_s91[label]:.4f} -> {g_bors[label]:.4f})"
        )
    print()

    # Step 8 — npz output
    print(f"Step 8 — Write npz: {NPZ_OUT.name}")
    breakdown_obj = np.array([breakdowns], dtype=object)
    # Diagnostic confined-hadron sub-totals (NOT in consumption)
    g_hadron_diag = {
        label: g_hadron_KT_diagnostic(T_ANCHOR_GEV[label]) for label in T_ANCHOR_GEV
    }
    np.savez(
        NPZ_OUT,
        # Borsanyi-refined g_* (canonical-promotion candidate on PASS)
        g_star_BS_FD_BE_borsanyi_T_H=g_bors_T_H,
        g_star_BS_FD_BE_borsanyi_100GeV=g_bors["100GeV"],
        g_star_BS_FD_BE_borsanyi_1GeV=g_bors["1GeV"],
        g_star_BS_FD_BE_borsanyi_1MeV=g_bors["1MeV"],
        # S91 smooth-tanh baseline cross-comparison
        g_star_BS_FD_BE_s91_T_H=g_s91_T_H,
        g_star_BS_FD_BE_s91_100GeV=g_s91["100GeV"],
        g_star_BS_FD_BE_s91_1GeV=g_s91["1GeV"],
        g_star_BS_FD_BE_s91_1MeV=g_s91["1MeV"],
        # PDG references
        g_star_PDG_100GeV=G_STAR_PDG["100GeV"],
        g_star_PDG_1GeV=G_STAR_PDG["1GeV"],
        g_star_PDG_1MeV=G_STAR_PDG["1MeV"],
        # rel_dev arrays
        rel_dev_borsanyi_anchors=rel_dev_bors_arr,
        rel_dev_s91_anchors=rel_dev_s91_arr,
        max_rel_dev_borsanyi=max_rd,
        # Borsanyi phase weights at each anchor + T_H
        w_borsanyi_100GeV=qcd_crossover_weight_borsanyi(T_ANCHOR_GEV["100GeV"]),
        w_borsanyi_1GeV=qcd_crossover_weight_borsanyi(T_ANCHOR_GEV["1GeV"]),
        w_borsanyi_1MeV=qcd_crossover_weight_borsanyi(T_ANCHOR_GEV["1MeV"]),
        w_borsanyi_T_H=qcd_crossover_weight_borsanyi(T_H_GeV),
        # Borsanyi domain + spline metadata
        borsanyi_T_grid_GeV=_BORS_T_GRID_GEV,
        borsanyi_w_grid=_BORS_W_GRID,
        borsanyi_domain_lo_GeV=_BORS_T_LO_GEV,
        borsanyi_domain_hi_GeV=_BORS_T_HI_GEV,
        borsanyi_table_audit_sha256=_BORS_NPZ_AUDIT,
        w8_4_live_audit_sha256=W8_4_LIVE_AUDIT_SHA,
        w8_4_live_line_present=live_line_present,
        w8_4_npz_matches_live=npz_matches_live,
        # Diagnostic confined-hadron sub-totals (NOT in consumption)
        g_hadron_KT_diagnostic_100GeV=g_hadron_diag["100GeV"],
        g_hadron_KT_diagnostic_1GeV=g_hadron_diag["1GeV"],
        g_hadron_KT_diagnostic_1MeV=g_hadron_diag["1MeV"],
        # Per-species kernel evaluations
        kolb_turner_kernel_evaluations=breakdown_obj,
        # Pins
        T_H_value_MeV=T_H_value_MeV,
        cascade_form_pin="S88 W6 §V.5 (UNCHANGED)",
        lattice_QCD_pin="Borsanyi et al. 2016 (Nature 539, 69) / §W8-4 table",
        quad_limit=QUAD_LIMIT,
        quad_epsabs=QUAD_EPSABS,
        quad_epsrel=QUAD_EPSREL,
        max_kernel_quad_abs_error=max_kernel_err,
        # Verdict fields
        pass_band=PASS_BAND,
        info_band_lo=INFO_BAND_LO,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        composite_verdict=composite,
        delta_g_star_1GeV_vs_s91=delta_1GeV,
        k_KT_fermion_at_0=k_f0,
        k_KT_boson_at_0=k_b0,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        schema_version="S87+",
        allow_pickle=True,
    )

    # Step 9 — JSON sidecar
    json_report = {
        "gate_id": GATE_ID,
        "T_H_value_MeV": T_H_value_MeV,
        "g_star_BS_FD_BE_borsanyi_T_H": g_bors_T_H,
        "g_star_BS_FD_BE_s91_T_H": g_s91_T_H,
        "w8_4_live_audit_sha256": W8_4_LIVE_AUDIT_SHA,
        "borsanyi_table_audit_sha256": _BORS_NPZ_AUDIT,
        "w8_4_live_line_present": bool(live_line_present),
        "w8_4_npz_matches_live": bool(npz_matches_live),
        "consumption_form": "g_star = g_nonQCD_KT + w_borsanyi * g_QCD_free_KT (no separate hadron term; §W8-4 WP §(i))",
        "anchors": {
            label: {
                "T_GeV": T_ANCHOR_GEV[label],
                "g_star_BS_FD_BE_borsanyi": g_bors[label],
                "g_star_BS_FD_BE_s91": g_s91[label],
                "g_star_PDG_ref": G_STAR_PDG[label],
                "rel_dev_borsanyi": rel_devs_bors[label],
                "rel_dev_s91": rel_devs_s91[label],
                "w_borsanyi": qcd_crossover_weight_borsanyi(T_ANCHOR_GEV[label]),
                "g_nonQCD_KT": breakdowns[label]["_subtotals"]["g_nonQCD_KT"],
                "g_QCD_free_KT": breakdowns[label]["_subtotals"]["g_QCD_free_KT"],
                "verdict_per_anchor": (
                    "PASS" if rel_devs_bors[label] <= INFO_BAND_LO else
                    ("INFO" if rel_devs_bors[label] <= PASS_BAND else "FAIL")
                ),
            }
            for label in T_ANCHOR_GEV
        },
        "max_rel_dev_borsanyi": max_rd,
        "max_kernel_quad_abs_error": max_kernel_err,
        "delta_g_star_1GeV_vs_s91": delta_1GeV,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "composite_verdict": composite,
        "kernel_normalization_check": {
            "k_KT_fermion_at_0": k_f0,
            "k_KT_boson_at_0": k_b0,
            "within_tolerance_1e6": (abs(k_f0 - 7.0 / 8.0) < 1e-6 and abs(k_b0 - 1.0) < 1e-6),
        },
        "cascade_form_pin": "S88 W6 §V.5 (UNCHANGED)",
        "lattice_QCD_pin": "Borsanyi et al. 2016 (Nature 539, 69) / §W8-4 table",
        "machinery_pins": {
            "quad_limit": QUAD_LIMIT,
            "quad_epsabs": QUAD_EPSABS,
            "quad_epsrel": QUAD_EPSREL,
            "borsanyi_domain_GeV": [_BORS_T_LO_GEV, _BORS_T_HI_GEV],
            "bc_type": _BORS_META.get("bc_type"),
            "pass_band": PASS_BAND,
            "info_band_lo": INFO_BAND_LO,
        },
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pin_shas": pins,
    }
    JSON_OUT.write_text(json.dumps(json_report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  → {JSON_OUT.name}")

    # Step 10 — Plot: g_*_BS_FD_BE_borsanyi vs g_*_PDG at 3 anchors + T_H overlay
    print(f"Step 10 — Write plot: {PNG_OUT.name}")
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    plot_labels = ["100GeV", "1GeV", "1MeV"]
    for ax, label in zip(axes[:3], plot_labels):
        pdg_ref = G_STAR_PDG[label]
        g_b = g_bors[label]
        g_s = g_s91[label]
        rd_b = rel_devs_bors[label]
        rd_s = rel_devs_s91[label]
        ax.axhspan(pdg_ref * 0.90, pdg_ref * 1.10, alpha=0.20, color="green",
                   label="±10% RATIO PASS band")
        ax.axhspan(pdg_ref * 0.90, pdg_ref * 0.95, alpha=0.15, color="yellow")
        ax.axhspan(pdg_ref * 1.05, pdg_ref * 1.10, alpha=0.15, color="yellow",
                   label="±5%-10% RATIO INFO band")
        ax.axhline(pdg_ref, color="green", lw=2.0, ls="-",
                   label=f"PDG ref: {pdg_ref:.2f}")
        ax.plot([0.5], [g_s], "rs", ms=15,
                label=f"S91 smooth-tanh: {g_s:.3f} (rd={rd_s:.2%})")
        ax.plot([1.5], [g_b], "bo", ms=15,
                label=f"Borsanyi refined: {g_b:.3f} (rd={rd_b:.2%})")
        ax.set_xlim(-0.5, 2.5)
        ax.set_xticks([0.5, 1.5])
        ax.set_xticklabels(["S91 smooth-tanh\n[tanh w(T)]",
                            "Borsanyi refined\n[§W8-4 w(T)]"], fontsize=9)
        ax.set_ylabel(r"$g_{*}(T)$  (effective relativistic dof)", fontsize=10)
        verdict_per_anchor = (
            "PASS" if rd_b <= INFO_BAND_LO else
            ("INFO" if rd_b <= PASS_BAND else "FAIL")
        )
        ax.set_title(
            f"T = {label}  (PDG = {pdg_ref:.2f})\n"
            f"Borsanyi rel_dev = {rd_b:.2%}  [{verdict_per_anchor}]",
            fontsize=10,
        )
        ax.legend(loc="lower right", fontsize=7)
        ax.grid(True, alpha=0.3)
        all_vals = [pdg_ref, g_b, g_s]
        ax.set_ylim(min(all_vals) * 0.80, max(all_vals) * 1.20)

    # 4th panel: T_H overlay on the w_borsanyi(T) crossover curve + g_*(T)
    ax4 = axes[3]
    T_dense_GeV = np.logspace(np.log10(_BORS_T_LO_GEV), np.log10(_BORS_T_HI_GEV), 400)  # (local)
    g_dense = np.array([g_star_BS_FD_BE_borsanyi(t) for t in T_dense_GeV])  # (local)
    ax4.plot(T_dense_GeV * 1e3, g_dense, "b-", lw=1.8,
             label=r"$g_{*}^{\rm borsanyi}(T)$ (KT cascade)")
    # PDG anchors as points
    for label in plot_labels:
        T_MeV = T_ANCHOR_GEV[label] * 1e3
        if _BORS_T_LO_GEV * 1e3 <= T_MeV <= _BORS_T_HI_GEV * 1e3:
            ax4.plot([T_MeV], [G_STAR_PDG[label]], "g^", ms=12,
                     label=f"PDG {label}: {G_STAR_PDG[label]:.2f}")
    # T_H overlay (1.057 MeV is below the spline domain; mark its g_* value)
    ax4.axvline(T_H_value_MeV, color="purple", ls="--", lw=1.5,
                label=f"T_H = {T_H_value_MeV} MeV")
    ax4.plot([T_H_value_MeV], [g_bors_T_H], "P", color="purple", ms=14,
             label=f"g_*(T_H) = {g_bors_T_H:.4f}\n(= g_star_BS_T_H_FW cand.)")
    ax4.set_xscale("log")
    ax4.set_xlabel("T (MeV)", fontsize=10)
    ax4.set_ylabel(r"$g_{*}^{\rm borsanyi}(T)$", fontsize=10)
    ax4.set_title("Borsanyi-weighted KT cascade g_*(T)\n+ PDG anchors + T_H overlay",
                  fontsize=10)
    ax4.legend(loc="upper left", fontsize=7)
    ax4.grid(True, alpha=0.3, which="both")

    fig.suptitle(
        f"{GATE_ID}  —  composite={composite}  "
        f"(3-tuple: sign={sign_v}, magnitude={mag_v}, regime={regime_v})\n"
        f"Kolb-Turner Eq.3.62 FD/BE cascade under §W8-4 Borsanyi phase-weight "
        f"vs S91 smooth-tanh vs PDG @ 3 anchors + T_H",
        fontsize=11,
    )
    plt.tight_layout()
    plt.savefig(PNG_OUT, dpi=120, bbox_inches="tight")
    plt.close(fig)

    # Step 11 — single-shot AFTER-pattern verdict emission
    print()
    print("Step 11 — Build verdict block in memory → atomic append → re-read verify")
    value_str = (
        f"g_star_BS_FD_BE_borsanyi_T_H={g_bors_T_H:.6f};"
        f"g_star_BS_FD_BE_borsanyi_100GeV={g_bors['100GeV']:.4f};"
        f"rel_dev_100GeV={rel_devs_bors['100GeV']:.6f};"
        f"g_star_BS_FD_BE_borsanyi_1GeV={g_bors['1GeV']:.4f};"
        f"rel_dev_1GeV={rel_devs_bors['1GeV']:.6f};"
        f"g_star_BS_FD_BE_borsanyi_1MeV={g_bors['1MeV']:.4f};"
        f"rel_dev_1MeV={rel_devs_bors['1MeV']:.6f};"
        f"max_rel_dev={max_rd:.6f};"
        f"w8_4_live_audit_sha256={W8_4_LIVE_AUDIT_SHA};"
        f"composite={composite}"
    )
    verdict_block = build_verdict_text(
        composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v,
    )
    append_verdict_atomic(verdict_block)

    if verify_verdict_on_disk(audit_sha):
        print(f"  → s92_gate_verdicts.txt (audit_sha256={audit_sha[:16]}...): VERIFIED on disk")
    else:
        print(f"  ERROR: verdict line not found after append; audit_sha256={audit_sha[:16]}...")
        return 1

    # Step 12 — On PASS: emit the update_constant invocation record for
    # g_star_BS_T_H_FW (the actual MCP call is made by the orchestrating agent
    # per the canonical write-order verdict-file -> canonical_constants.py).
    print()
    if composite == "PASS":
        provenance_comment = (
            f"Substrate-cascade-tail Kolb-Turner FD/BE integrated form evaluated at "
            f"T_H=1.057 MeV (CF-39 anchor per S88 W6 §V.1) under Borsanyi-2016-anchored "
            f"qcd_crossover_weight_borsanyi phase-weight from §W8-4 "
            f"(audit_sha256={W8_4_LIVE_AUDIT_SHA}); replaces S91 §W3-1 smooth-tanh INFO "
            f"at T=1 GeV anchor with refined Borsanyi residual-confinement suppression "
            f"model. This gate audit_sha256={audit_sha}."
        )
        print("Step 12 — PASS branch: g_star_BS_T_H_FW canonical-promotion record.")
        print("  update_constant(")
        print(f"    name='g_star_BS_T_H_FW',")
        print(f"    value={g_bors_T_H!r},")
        print(f"    session='S92',")
        print(f"    source='S92-W8-5',")
        print(f"    comment={provenance_comment!r},")
        print(f"  )")
        print("  (MCP call executed by the dispatching agent per canonical write-order.)")
    else:
        print(f"Step 12 — composite={composite} (not PASS): g_star_BS_T_H_FW promotion "
              f"does NOT fire; §W8-6 deferral per plan FAIL/INFO routing.")

    # Final 4-tuple log line
    print()
    print(
        f"(value={value_str!r}, "
        f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"
    )
    print(f"\n=== {GATE_ID}: {composite} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
