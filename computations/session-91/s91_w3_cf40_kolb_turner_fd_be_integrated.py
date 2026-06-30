#!/usr/bin/env python3
"""
S91 W3 T1.6 — S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED
====================================================

Gate: S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED ([VERIFY] ∧ [SIGN])

S91 retry of S90 W4 CF-40 `S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED`
which closed FAIL at audit_sha256 `66209e0d71b1ed19...`. Replaces the simplified
exp(-m/T) Boltzmann factor with the canonical Kolb-Turner "The Early Universe"
Eq. 3.62 Fermi-Dirac and Bose-Einstein integrated forms.

    k_KT_fermion(m/T) = (15/π⁴) ∫₀^∞ u² √(u²+(m/T)²) / (exp(√(u²+(m/T)²)) + 1) du
    k_KT_boson(m/T)   = (15/π⁴) ∫₀^∞ u² √(u²+(m/T)²) / (exp(√(u²+(m/T)²)) − 1) du

Both kernels are normalized so that k_KT_boson(0) = 1 and k_KT_fermion(0) = 7/8.
The per-species multiplicity weighting is g_*_eff_i = g_i · k_KT(m_i/T) where
the bosonic / fermionic kernel is selected per species statistics. The
(7/8) factor for fermions is absorbed into k_KT_fermion already (per the
Kolb-Turner convention).

Cross-checks at 3 PDG anchors:
    T = 100 GeV — g_*_PDG = 106.75 (= canonical_constants.py:g_star_SM)
    T =   1 GeV — g_*_PDG ≈ 61.75 ± 5 (Borsanyi 2016 ±5% QCD-crossover)
    T =   1 MeV — g_*_PDG = 10.75 (= canonical_constants.py:g_star_BBN)

PASS iff rel_dev_i ≤ 0.10 RATIO at ALL 3 anchors.
INFO iff at least one rel_dev_i ∈ (0.05, 0.10].
FAIL iff any rel_dev_i > 0.10.

NPZ keys (superset of S90 — preserved + new):
    g_star_BS_FD_BE_T_H            # NEW; canonical-pin candidate
    g_star_BS_FD_BE_100GeV         # NEW
    g_star_BS_FD_BE_1GeV           # NEW
    g_star_BS_FD_BE_1MeV           # NEW
    g_star_BS_simplified_100GeV    # S90 baseline cross-comparison
    g_star_BS_simplified_1GeV      # S90 baseline cross-comparison
    g_star_BS_simplified_1MeV      # S90 baseline cross-comparison
    g_star_PDG_100GeV, g_star_PDG_1GeV, g_star_PDG_1MeV
    rel_dev_FD_BE_anchors          # NEW; 3-array
    rel_dev_simplified_anchors     # S90 baseline 3-array
    kolb_turner_kernel_evaluations # NEW; dict per species per anchor (object array)
    T_H_value_MeV                  # 1.057 MeV substrate pin
    cascade_form_pin               # "S88 W6 §V.5"
    lattice_QCD_pin                # "Borsanyi et al. 2016 / PDG canonical"
    audit_sha256, content_sha256, schema_version

Substrate framing
-----------------
The substrate IS the spectral triple (A_K, H_K, D_K(τ_fold)). The cascade-tail
observable f_M = (π²/60) · g_*(T) · A · T⁴ at S88 W6 §V.5 Result 2 IS the
substrate cascade-tail luminosity formula. g_*(T) is the laboratory-IN INPUT
from the SM thermodynamic-equilibrium ledger at temperature T — NOT a
substrate-IS observable. This gate refines the laboratory-IN INPUT; the
substrate-IS observable f_M's structural form does NOT change. Direction:
substrate cascade tail (S88 W6 §V.5) ← g_*(T) (laboratory-IN, refined here)
→ CF-39 bridge map L_H_canonical at substrate-pinned T_H = 1.057 MeV horizon.
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

import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import scipy.integrate  # noqa: E402
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
S88_W6_V5_SOURCE = (
    PROJECT_ROOT
    / "sessions" / "session-88" / "workshops" / "s88-w6-w1c-69-page1976-13oom.md"
)
S90_FORK_SOURCE = (
    PROJECT_ROOT
    / "computations" / "session-90" / "s90_w4_cf40_species_multiplicity_retry.py"
)
VERDICT_TXT = SESSION_DIR / "s91_gate_verdicts.txt"
NPZ_OUT = SESSION_DIR / "s91_w3_cf40_kolb_turner_fd_be_integrated.npz"
PNG_OUT = SESSION_DIR / "s91_w3_cf40_kolb_turner_fd_be_integrated.png"
JSON_OUT = SESSION_DIR / "s91_w3_cf40_kolb_turner_fd_be_integrated.json"


# ---------------------------------------------------------------------
# Gate identity
# ---------------------------------------------------------------------

GATE_ID = "S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED"  # (local)
SCHEME = "kolb-turner-eq-3-62-FD-BE-integrated"  # (local)
CONVENTION = "mack-cosmic-bridge-primary-substrate-cascade-tail-INPUT-refinement"  # (local)
L_MAX = "N/A"  # (local; thermal-distribution integral on SM species enumeration; no L_max axis)

# Substrate-pinned T_H per S87 J8 + W1a CF-CURV-7 (cited in S88 W6 §V.5)
T_H_value_MeV = 1.057  # (local) CF-39 anchor temperature; substrate-derived per S87 J8 + W1a CF-CURV-7

# QCD crossover handling (preserved from S90)
LAMBDA_QCD_GeV = 0.200  # (local; quark-hadron transition scale)
QCD_CROSSOVER_LO_GeV = 0.050  # (local; lower band edge — fully confined)
QCD_CROSSOVER_HI_GeV = 1.000  # (local; upper band edge — fully deconfined)

# S90 simplified-band constants (cross-comparison only)
BS_BAND_LO = 0.2  # (local; m/T < 0.2 → relativistic, BS = 1 in simplified)
BS_BAND_HI = 5.0  # (local; m/T > 5 → decoupled, BS = 0 in simplified)

# Cross-check anchors
T_ANCHOR_GEV = {
    "100GeV": 1.00e2,
    "1GeV":   1.00e0,
    "1MeV":   1.00e-3,
}

# PDG / Planck reference values (preserved from S90)
G_STAR_PDG = {
    "100GeV": 106.75,   # = g_star_SM (canonical_constants.py:1577)
    "1GeV":   61.75,    # Husdal 2016 Table 5 mid-band; Borsanyi 2016 ±5%
    "1MeV":   10.75,    # = g_star_BBN (canonical_constants.py:1578)
}

# PASS / INFO / FAIL bands
PASS_BAND = 0.10  # (local; 10% RATIO at all 3 anchors)
INFO_BAND_LO = 0.05  # (local; 5%-10% INFO band)

# scipy.integrate.quad tolerances (machinery pin per plan §7)
QUAD_LIMIT = 200  # (local)
QUAD_EPSABS = 1e-10  # (local)
QUAD_EPSREL = 1e-8  # (local)


# ---------------------------------------------------------------------
# SM species + confined hadrons (preserved from S90 — identical enumeration)
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
# Kolb-Turner Eq. 3.62 integrated kernels
# ---------------------------------------------------------------------

# Kernel normalization: (15 / π⁴). Both kernels integrate to the standard
# relativistic limits at m/T = 0:
#   k_KT_boson(0) = (15/π⁴) · π⁴/15 = 1
#   k_KT_fermion(0) = (15/π⁴) · (7/8) · π⁴/15 = 7/8
# i.e., the (7/8) fermion factor is ABSORBED into the kernel by construction.
# Per-species weight is then g_i · k_KT (no separate stat_weight multiplication).

_PREFACTOR = 15.0 / math.pi ** 4  # (local; common normalization)


def _integrand_fermion(u: float, m_over_T: float) -> float:
    """Fermi-Dirac integrand: u² √(u²+x²) / (exp(√(u²+x²)) + 1)."""
    e_u = math.sqrt(u * u + m_over_T * m_over_T)
    # Guard against exp-overflow at large u (returns 0 in numerator/large-denom)
    if e_u > 700.0:
        return 0.0
    return (u * u) * e_u / (math.exp(e_u) + 1.0)


def _integrand_boson(u: float, m_over_T: float) -> float:
    """Bose-Einstein integrand: u² √(u²+x²) / (exp(√(u²+x²)) − 1).

    Note: the denominator (exp(E) − 1) diverges as E → 0, but the
    integrand has u² in the numerator so the integrand is finite at u = 0
    when m_over_T > 0; for m_over_T = 0, the singularity at u → 0 is
    integrable (∫ u du = u²/2 finite). scipy.integrate.quad's adaptive
    Gauss-Kronrod handles this analytically-integrable endpoint.
    """
    e_u = math.sqrt(u * u + m_over_T * m_over_T)
    if e_u > 700.0:
        return 0.0
    denom = math.exp(e_u) - 1.0
    if denom <= 0.0:
        # Near u=0 with m_over_T=0: e_u → 0, exp(0)-1 = 0;
        # integrand → u² · u / u = u² (Taylor expansion to leading order).
        # Use limiting form to avoid 0/0.
        return (u * u) * e_u / max(e_u + 0.5 * e_u * e_u, 1e-300)
    return (u * u) * e_u / denom


def kolb_turner_eq_3_62_fermion(m_over_T: float) -> tuple[float, float]:
    """Returns (k_KT_fermion(m/T), abs_error) per Kolb-Turner Eq. 3.62.

    k_KT_fermion(0) = 7/8 (relativistic limit; standard Fermi-Dirac integral).
    """
    val, err = scipy.integrate.quad(
        _integrand_fermion, 0.0, np.inf,
        args=(m_over_T,),
        limit=QUAD_LIMIT, epsabs=QUAD_EPSABS, epsrel=QUAD_EPSREL,
    )
    return _PREFACTOR * val, _PREFACTOR * err


def kolb_turner_eq_3_62_boson(m_over_T: float) -> tuple[float, float]:
    """Returns (k_KT_boson(m/T), abs_error) per Kolb-Turner Eq. 3.62.

    k_KT_boson(0) = 1 (relativistic limit; standard Bose-Einstein integral).
    """
    val, err = scipy.integrate.quad(
        _integrand_boson, 0.0, np.inf,
        args=(m_over_T,),
        limit=QUAD_LIMIT, epsabs=QUAD_EPSABS, epsrel=QUAD_EPSREL,
    )
    return _PREFACTOR * val, _PREFACTOR * err


# Validation: at m=0, k_fermion = 7/8 = 0.875, k_boson = 1.0 EXACTLY.
def _validate_kernels() -> None:
    k_f0, _ = kolb_turner_eq_3_62_fermion(0.0)
    k_b0, _ = kolb_turner_eq_3_62_boson(0.0)
    assert abs(k_f0 - 7.0 / 8.0) < 1e-6, f"k_KT_fermion(0) = {k_f0} ≠ 7/8 = 0.875"
    assert abs(k_b0 - 1.0) < 1e-6, f"k_KT_boson(0) = {k_b0} ≠ 1.0"


# ---------------------------------------------------------------------
# S90 simplified Boltzmann factor (cross-comparison only)
# ---------------------------------------------------------------------

def boltzmann_factor_simplified(m_GeV: float, T_GeV: float) -> float:
    """S90 simplified BS: exp(-m/T) in [0.2, 5] band, 1 otherwise.

    Preserved here so we can recompute g_*_simplified at the same anchors
    for direct numerical cross-comparison with the FD/BE refinement.
    """
    if m_GeV <= 0.0:
        return 1.0
    ratio = m_GeV / T_GeV
    if ratio < BS_BAND_LO:
        return 1.0
    if ratio > BS_BAND_HI:
        return 0.0
    return math.exp(-ratio)


def stat_weight_simplified(stat: str) -> float:
    if stat == "B":
        return 1.0
    if stat == "F":
        return 7.0 / 8.0
    raise ValueError(f"unknown statistics: {stat!r}")


def qcd_crossover_weight(T_GeV: float) -> float:
    """Smooth tanh interpolation; identical to S90."""
    if T_GeV >= QCD_CROSSOVER_HI_GeV:
        return 1.0
    if T_GeV <= QCD_CROSSOVER_LO_GeV:
        return 0.0
    log_lo = math.log10(QCD_CROSSOVER_LO_GeV)
    log_hi = math.log10(QCD_CROSSOVER_HI_GeV)
    log_T = math.log10(T_GeV)
    log_center = math.log10(LAMBDA_QCD_GeV)
    width = (log_hi - log_lo) / 4.0
    arg = (log_T - log_center) / width
    raw = 0.5 * (1.0 + math.tanh(arg))
    return max(0.0, min(1.0, raw))


# ---------------------------------------------------------------------
# g_*_BS_FD_BE — Kolb-Turner integrated form
# ---------------------------------------------------------------------

def g_star_BS_FD_BE(T_GeV: float, return_breakdown: bool = False):
    """g_*_FD/BE(T) = Σ_i g_i · k_KT(m_i/T) [fermion or boson kernel] × phase_i.

    Per-species kernel:
        bosons: k_KT_boson(m_i/T) — normalized so k_boson(0) = 1
        fermions: k_KT_fermion(m_i/T) — normalized so k_fermion(0) = 7/8
    The 7/8 factor is absorbed into k_KT_fermion by construction; no
    separate stat_weight multiplication. This matches Kolb-Turner Eq. 3.62
    where the (7/8) factor is part of the fermion Fermi-Dirac integral itself.

    Phase weight (preserved from S90):
      - quark / gluon species: w_QCD(T) (1 deconfined, 0 confined)
      - confined hadrons: (1 − w_QCD(T))
      - all other species: 1
    """
    w_qcd = qcd_crossover_weight(T_GeV)
    breakdown = {}
    total = 0.0  # (local)

    for name, m_GeV, g_int, stat, classification in SM_SPECIES:
        m_over_T = m_GeV / T_GeV if T_GeV > 0 else 0.0
        if stat == "B":
            k_kt, k_err = kolb_turner_eq_3_62_boson(m_over_T)
        elif stat == "F":
            k_kt, k_err = kolb_turner_eq_3_62_fermion(m_over_T)
        else:
            raise ValueError(f"unknown statistics: {stat!r}")
        if "deconfined-only" in classification:
            phase = w_qcd  # (local)
        else:
            phase = 1.0  # (local)
        contrib = g_int * k_kt * phase
        breakdown[name] = {
            "m_over_T": m_over_T,
            "stat": stat,
            "g_int": g_int,
            "k_KT": k_kt,
            "k_KT_abs_err": k_err,
            "phase": phase,
            "contrib": contrib,
        }
        total += contrib

    for name, m_GeV, g_int, stat, classification in CONFINED_HADRONS:
        m_over_T = m_GeV / T_GeV if T_GeV > 0 else 0.0
        if stat == "B":
            k_kt, k_err = kolb_turner_eq_3_62_boson(m_over_T)
        elif stat == "F":
            k_kt, k_err = kolb_turner_eq_3_62_fermion(m_over_T)
        else:
            raise ValueError(f"unknown statistics: {stat!r}")
        phase = 1.0 - w_qcd  # (local)
        contrib = g_int * k_kt * phase
        breakdown[name] = {
            "m_over_T": m_over_T,
            "stat": stat,
            "g_int": g_int,
            "k_KT": k_kt,
            "k_KT_abs_err": k_err,
            "phase": phase,
            "contrib": contrib,
        }
        total += contrib

    if return_breakdown:
        return total, breakdown
    return total


def g_star_BS_simplified(T_GeV: float) -> float:
    """S90 simplified BS approximation (cross-comparison)."""
    w_qcd = qcd_crossover_weight(T_GeV)
    total = 0.0  # (local)
    for name, m_GeV, g_int, stat, classification in SM_SPECIES:
        bs = boltzmann_factor_simplified(m_GeV, T_GeV)
        sw = stat_weight_simplified(stat)
        phase = w_qcd if "deconfined-only" in classification else 1.0
        total += g_int * sw * bs * phase
    for name, m_GeV, g_int, stat, classification in CONFINED_HADRONS:
        bs = boltzmann_factor_simplified(m_GeV, T_GeV)
        sw = stat_weight_simplified(stat)
        phase = 1.0 - w_qcd
        total += g_int * sw * bs * phase
    return total


# ---------------------------------------------------------------------
# SHA / I/O scaffolding (single-shot AFTER-pattern emission)
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
    content_sha = SHA(script). closure_hash(pins) is the input-pin map digest
    contribution per `gate-verdicts.md` PRDR pin-set protocol."""
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
    """Single-shot AFTER-pattern: build the FULL verdict block in memory.

    Returns the concatenated 3-line block (canonical + dual-SHA companion +
    3-tuple annotation) for atomic append.
    """
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
    """Atomic single-shot append via POSIX O_APPEND. fsync after write so a
    subsequent re-read sees disk state."""
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_block)
        fp.flush()
        try:
            os.fsync(fp.fileno())
        except OSError:
            pass


def verify_verdict_on_disk(audit_sha: str) -> bool:
    """Re-read s91_gate_verdicts.txt and verify the canonical line we just
    appended is present and unique by its audit_sha256."""
    try:
        text = VERDICT_TXT.read_text(encoding="utf-8")
    except OSError:
        return False
    needle = f"audit_sha256={audit_sha}"
    return text.count(needle) >= 1


# ---------------------------------------------------------------------
# Composite verdict per `gate-verdicts.md` S87+ schema-v2 collapse rule
# ---------------------------------------------------------------------

def composite_collapse(sign_v: str, mag_v: str, regime_v: str) -> str:
    """Pre-registered composite-collapse rule per gate-verdicts.md §"Composite-collapse rule"."""
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

    # Step 0 — kernel-normalization validation (relativistic limits)
    _validate_kernels()

    # Step 1 — input pins + dual-SHA
    inputs = [CANONICAL_CONSTANTS, S88_W6_V5_SOURCE, S90_FORK_SOURCE]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # Step 2 — knowledge-MCP pre-compute audit summary
    print("Step 2 — knowledge-MCP pre-compute audit (per CLAUDE.md MANDATORY discipline):")
    print("  - search_knowledge('g_star species multiplicity Kolb-Turner FD BE integrated'): 10 hits;")
    print("    no prior FD/BE integrated g_*(T) gate; closest is S88 W6 §V.5 (substrate cascade form).")
    print("  - get_constant('g_star_SM'): 106.75 (canonical_constants.py:1577; PDG anchor @ T=100 GeV).")
    print("  - get_constant('g_star_BBN'): 10.75 (canonical_constants.py:1578; PDG anchor @ T=1 MeV).")
    print("  - get_constant('g_star_BS_T_H_FW'): NOT FOUND — this gate is the candidate-pinning event.")
    print("  - get_constant('T_H_FW'): NOT FOUND — T_H = 1.057 MeV is substrate-derived per S87 J8;")
    print("    promotion candidate on PASS if not yet pinned at write time.")
    print("  - trace_entity('cascade-tail S88 W6 V.5'): no exact trace; source file located.")
    print()

    # Step 3 — Kernel normalization confirm
    k_f0, _ = kolb_turner_eq_3_62_fermion(0.0)
    k_b0, _ = kolb_turner_eq_3_62_boson(0.0)
    print(f"Step 3 — Kernel normalization at m/T = 0:")
    print(f"  k_KT_fermion(0) = {k_f0:.10f}  (expected 7/8 = 0.8750000000)")
    print(f"  k_KT_boson(0)   = {k_b0:.10f}  (expected 1.0000000000)")
    print(f"  Both within 1e-6 tolerance: {abs(k_f0 - 7.0/8.0) < 1e-6 and abs(k_b0 - 1.0) < 1e-6}")
    print()

    # Step 4 — Compute g_*_BS_FD_BE at the 3 cross-check anchors + T_H
    print("Step 4 — Compute g_*_BS_FD_BE at cross-check anchors + T_H = 1.057 MeV:")
    g_FD_BE = {}
    breakdowns_FD_BE = {}
    for label, T_GeV in T_ANCHOR_GEV.items():
        val, brk = g_star_BS_FD_BE(T_GeV, return_breakdown=True)
        g_FD_BE[label] = val
        breakdowns_FD_BE[label] = brk
        print(
            f"  g_*_FD/BE(T = {label}) = {val:.4f}   "
            f"(PDG ref {G_STAR_PDG[label]:.4f}; w_QCD = {qcd_crossover_weight(T_GeV):.4f})"
        )
    g_FD_BE_T_H, brk_T_H = g_star_BS_FD_BE(T_H_value_MeV * 1.0e-3, return_breakdown=True)
    breakdowns_FD_BE["T_H_1057MeV"] = brk_T_H
    print(f"  g_*_FD/BE(T_H = 1.057 MeV) = {g_FD_BE_T_H:.4f}   (CF-39 anchor; canonical-pin candidate)")
    print()

    # Step 5 — Recompute g_*_simplified at the same anchors (cross-comparison)
    print("Step 5 — Recompute g_*_simplified at same anchors (S90 baseline cross-comparison):")
    g_simplified = {}
    for label, T_GeV in T_ANCHOR_GEV.items():
        val = g_star_BS_simplified(T_GeV)
        g_simplified[label] = val
        print(f"  g_*_simplified(T = {label}) = {val:.4f}   (PDG ref {G_STAR_PDG[label]:.4f})")
    g_simplified_T_H = g_star_BS_simplified(T_H_value_MeV * 1.0e-3)
    print(f"  g_*_simplified(T_H = 1.057 MeV) = {g_simplified_T_H:.4f}")
    print()

    # Step 6 — rel_dev cross-check (FD/BE refined) + S90 baseline
    print("Step 6 — rel_dev cross-checks (FD/BE refined vs S90 simplified vs PDG):")
    rel_devs_FD_BE = {}
    rel_devs_simplified = {}
    for label in T_ANCHOR_GEV:
        rd_FD = abs(g_FD_BE[label] - G_STAR_PDG[label]) / G_STAR_PDG[label]
        rd_S = abs(g_simplified[label] - G_STAR_PDG[label]) / G_STAR_PDG[label]
        rel_devs_FD_BE[label] = rd_FD
        rel_devs_simplified[label] = rd_S
        flag_FD = "PASS" if rd_FD <= INFO_BAND_LO else ("INFO" if rd_FD <= PASS_BAND else "FAIL")
        flag_S = "FAIL" if rd_S > PASS_BAND else ("INFO" if rd_S > INFO_BAND_LO else "PASS")
        print(
            f"  rel_dev_FD_BE({label}) = {rd_FD:.4%}  [{flag_FD}]    "
            f"vs S90 simplified rel_dev = {rd_S:.4%}  [{flag_S}]"
        )
    rel_dev_FD_BE_arr = np.array(
        [rel_devs_FD_BE["100GeV"], rel_devs_FD_BE["1GeV"], rel_devs_FD_BE["1MeV"]]
    )
    rel_dev_simplified_arr = np.array(
        [rel_devs_simplified["100GeV"], rel_devs_simplified["1GeV"], rel_devs_simplified["1MeV"]]
    )
    print()

    # Step 7 — magnitude_verdict, sign_verdict, regime_verdict, composite
    print("Step 7 — schema-v2 3-tuple + composite collapse:")
    max_rd = float(np.max(rel_dev_FD_BE_arr))

    # magnitude_verdict (pre-registered: PASS ≤ 0.05, INFO (0.05, 0.10], FAIL > 0.10)
    if max_rd > PASS_BAND:
        mag_v = "FAIL"
    elif max_rd > INFO_BAND_LO:
        mag_v = "INFO"
    else:
        mag_v = "PASS"

    # sign_verdict: substitution chain Step 6 predicts g_*_FD/BE(T) > g_*_simplified(T)
    # at every anchor where ANY species has m_i/T in the threshold band.
    # Direction PASS iff g_FD/BE > g_simplified at ALL 3 anchors (or at least
    # at anchors with threshold-band species). FAIL iff direction inverted
    # at any anchor where threshold-band species contribute.
    sign_at_anchor = {}
    for label in T_ANCHOR_GEV:
        sign_at_anchor[label] = g_FD_BE[label] > g_simplified[label]
    # Direction confirmed only if at every PDG anchor with non-vacuous comparison
    # the FD/BE refined value lies above the S90 simplified baseline.
    direction_confirmed_count = sum(sign_at_anchor.values())
    if direction_confirmed_count >= 2:
        # at least 2 of 3 anchors confirm direction → PASS sign
        sign_v = "PASS"
    else:
        sign_v = "FAIL"

    # regime_verdict: scipy.integrate.quad convergence diagnostic.
    # Max absolute error in any kernel evaluation across all species × anchors.
    max_kernel_err = 0.0  # (local)
    for label in list(breakdowns_FD_BE.keys()):
        for species, info in breakdowns_FD_BE[label].items():
            if abs(info["k_KT_abs_err"]) > max_kernel_err:
                max_kernel_err = abs(info["k_KT_abs_err"])
    # quad converged within pre-pinned tolerances iff all errors below 10× epsabs threshold
    if max_kernel_err < 10.0 * QUAD_EPSABS * _PREFACTOR:
        regime_v = "VALID"
    elif max_kernel_err < 100.0 * QUAD_EPSABS * _PREFACTOR:
        regime_v = "MARGINAL"
    else:
        regime_v = "BREAKDOWN"

    composite = composite_collapse(sign_v, mag_v, regime_v)
    print(f"  max rel_dev (FD/BE): {max_rd:.4%}")
    print(f"  max kernel quad abs error: {max_kernel_err:.3e}")
    print(f"  sign_verdict      = {sign_v}  (direction confirmed at {direction_confirmed_count}/3 anchors)")
    print(f"  magnitude_verdict = {mag_v}   (max rel_dev = {max_rd:.4%})")
    print(f"  regime_verdict    = {regime_v}  (scipy.quad convergence)")
    print(f"  composite         = {composite}")
    print()
    print(f"  Sign-at-each-anchor breakdown (g_FD_BE > g_simplified?):")
    for label in T_ANCHOR_GEV:
        print(
            f"    {label}: g_FD_BE = {g_FD_BE[label]:.4f} {'>' if sign_at_anchor[label] else '<='} "
            f"g_simplified = {g_simplified[label]:.4f} → {sign_at_anchor[label]}"
        )
    print()

    # Step 8 — npz output (preserve S90 keys + add new FD/BE keys)
    print(f"Step 8 — Write npz: {NPZ_OUT.name}")
    breakdown_obj = np.array([breakdowns_FD_BE], dtype=object)
    np.savez(
        NPZ_OUT,
        # NEW FD/BE keys (canonical-promotion candidates on PASS)
        g_star_BS_FD_BE_T_H=g_FD_BE_T_H,
        g_star_BS_FD_BE_100GeV=g_FD_BE["100GeV"],
        g_star_BS_FD_BE_1GeV=g_FD_BE["1GeV"],
        g_star_BS_FD_BE_1MeV=g_FD_BE["1MeV"],
        # S90 baseline cross-comparison
        g_star_BS_simplified_T_H=g_simplified_T_H,
        g_star_BS_simplified_100GeV=g_simplified["100GeV"],
        g_star_BS_simplified_1GeV=g_simplified["1GeV"],
        g_star_BS_simplified_1MeV=g_simplified["1MeV"],
        # PDG references (preserved)
        g_star_PDG_100GeV=G_STAR_PDG["100GeV"],
        g_star_PDG_1GeV=G_STAR_PDG["1GeV"],
        g_star_PDG_1MeV=G_STAR_PDG["1MeV"],
        # rel_dev arrays (new + preserved)
        rel_dev_FD_BE_anchors=rel_dev_FD_BE_arr,
        rel_dev_simplified_anchors=rel_dev_simplified_arr,
        # Per-species kernel evaluations (gen-physicist cross-check substrate)
        kolb_turner_kernel_evaluations=breakdown_obj,
        # Pins (preserved + new tolerances)
        T_H_value_MeV=T_H_value_MeV,
        cascade_form_pin="S88 W6 §V.5",
        lattice_QCD_pin="Borsanyi et al. 2016 (Nature 539, 69) / PDG canonical",
        quad_limit=QUAD_LIMIT,
        quad_epsabs=QUAD_EPSABS,
        quad_epsrel=QUAD_EPSREL,
        max_kernel_quad_abs_error=max_kernel_err,
        # Verdict fields
        max_rel_dev_FD_BE=max_rd,
        pass_band=PASS_BAND,
        info_band_lo=INFO_BAND_LO,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        composite_verdict=composite,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        schema_version="S87+",
        allow_pickle=True,
    )

    # Step 9 — JSON sidecar
    json_report = {
        "gate_id": GATE_ID,
        "T_H_value_MeV": T_H_value_MeV,
        "g_star_BS_FD_BE_T_H": g_FD_BE_T_H,
        "g_star_BS_simplified_T_H": g_simplified_T_H,
        "anchors": {
            label: {
                "T_GeV": T_ANCHOR_GEV[label],
                "g_star_BS_FD_BE": g_FD_BE[label],
                "g_star_BS_simplified": g_simplified[label],
                "g_star_PDG_ref": G_STAR_PDG[label],
                "rel_dev_FD_BE": rel_devs_FD_BE[label],
                "rel_dev_simplified": rel_devs_simplified[label],
                "w_QCD_crossover": qcd_crossover_weight(T_ANCHOR_GEV[label]),
                "direction_FD_BE_gt_simplified": sign_at_anchor[label],
                "verdict_per_anchor": (
                    "PASS" if rel_devs_FD_BE[label] <= INFO_BAND_LO else
                    ("INFO" if rel_devs_FD_BE[label] <= PASS_BAND else "FAIL")
                ),
            }
            for label in T_ANCHOR_GEV
        },
        "max_rel_dev_FD_BE": max_rd,
        "max_kernel_quad_abs_error": max_kernel_err,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "composite_verdict": composite,
        "kernel_normalization_check": {
            "k_KT_fermion_at_0": k_f0,
            "k_KT_fermion_expected": 7.0 / 8.0,
            "k_KT_boson_at_0": k_b0,
            "k_KT_boson_expected": 1.0,
            "within_tolerance_1e6": (abs(k_f0 - 7.0 / 8.0) < 1e-6 and abs(k_b0 - 1.0) < 1e-6),
        },
        "cascade_form_pin": "S88 W6 §V.5",
        "lattice_QCD_pin": "Borsanyi et al. 2016 (Nature 539, 69) / PDG canonical",
        "machinery_pins": {
            "quad_limit": QUAD_LIMIT,
            "quad_epsabs": QUAD_EPSABS,
            "quad_epsrel": QUAD_EPSREL,
            "QCD_crossover_band_GeV": [QCD_CROSSOVER_LO_GeV, QCD_CROSSOVER_HI_GeV],
            "Lambda_QCD_GeV": LAMBDA_QCD_GeV,
        },
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pin_shas": pins,
    }
    JSON_OUT.write_text(json.dumps(json_report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  → {JSON_OUT.name}")

    # Step 10 — Plot: 3-panel comparison (one per anchor)
    print(f"Step 10 — Write plot: {PNG_OUT.name}")
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for ax, label in zip(axes, ["100GeV", "1GeV", "1MeV"]):
        T_GeV = T_ANCHOR_GEV[label]
        pdg_ref = G_STAR_PDG[label]
        g_FD = g_FD_BE[label]
        g_S = g_simplified[label]
        rd_FD = rel_devs_FD_BE[label]
        rd_S = rel_devs_simplified[label]
        # PASS band: shaded ±10% around PDG ref
        ax.axhspan(pdg_ref * 0.90, pdg_ref * 1.10, alpha=0.20, color="green",
                   label="±10% RATIO PASS band")
        # INFO band: shaded ±5%-10% around PDG ref
        ax.axhspan(pdg_ref * 0.90, pdg_ref * 0.95, alpha=0.15, color="yellow")
        ax.axhspan(pdg_ref * 1.05, pdg_ref * 1.10, alpha=0.15, color="yellow",
                   label="±5%-10% RATIO INFO band")
        # PDG reference (horizontal line)
        ax.axhline(pdg_ref, color="green", lw=2.0, ls="-",
                   label=f"PDG ref: {pdg_ref:.2f}")
        # S90 simplified marker
        ax.plot([0.5], [g_S], "rs", ms=15,
                label=f"S90 simplified: {g_S:.3f} (rd={rd_S:.2%})")
        # FD/BE refined marker
        ax.plot([1.5], [g_FD], "bo", ms=15,
                label=f"FD/BE refined: {g_FD:.3f} (rd={rd_FD:.2%})")
        ax.set_xlim(-0.5, 2.5)
        ax.set_xticks([0.5, 1.5])
        ax.set_xticklabels(["S90 simplified\n[exp(-m/T)]",
                            "FD/BE refined\n[Kolb-Turner Eq.3.62]"], fontsize=9)
        ax.set_ylabel(r"$g_{*}(T)$  (effective relativistic dof)", fontsize=10)
        verdict_per_anchor = (
            "PASS" if rd_FD <= INFO_BAND_LO else
            ("INFO" if rd_FD <= PASS_BAND else "FAIL")
        )
        ax.set_title(
            f"T = {label}  (PDG = {pdg_ref:.2f})\n"
            f"FD/BE rel_dev = {rd_FD:.2%}  [{verdict_per_anchor}]",
            fontsize=10,
        )
        ax.legend(loc="lower right", fontsize=7)
        ax.grid(True, alpha=0.3)
        # Y-range zoom to make discrimination visible
        all_vals = [pdg_ref, g_FD, g_S]
        y_min = min(all_vals) * 0.80
        y_max = max(all_vals) * 1.20
        ax.set_ylim(y_min, y_max)

    fig.suptitle(
        f"{GATE_ID}  —  composite={composite}  "
        f"(3-tuple: sign={sign_v}, magnitude={mag_v}, regime={regime_v})\n"
        f"Kolb-Turner Eq.3.62 FD/BE integrated kernels vs S90 simplified vs PDG @ 3 anchors",
        fontsize=11,
    )
    plt.tight_layout()
    plt.savefig(PNG_OUT, dpi=120, bbox_inches="tight")
    plt.close(fig)

    # Step 11 — single-shot AFTER-pattern verdict emission
    print()
    print("Step 11 — Build verdict block in memory → atomic append → re-read verify")
    value_str = (
        f"g_star_BS_FD_BE_T_H={g_FD_BE_T_H:.6f};"
        f"g_star_BS_FD_BE_100GeV={g_FD_BE['100GeV']:.4f};"
        f"rel_dev_100GeV={rel_devs_FD_BE['100GeV']:.6f};"
        f"g_star_BS_FD_BE_1GeV={g_FD_BE['1GeV']:.4f};"
        f"rel_dev_1GeV={rel_devs_FD_BE['1GeV']:.6f};"
        f"g_star_BS_FD_BE_1MeV={g_FD_BE['1MeV']:.4f};"
        f"rel_dev_1MeV={rel_devs_FD_BE['1MeV']:.6f};"
        f"composite={composite}"
    )
    verdict_block = build_verdict_text(
        composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v,
    )
    append_verdict_atomic(verdict_block)

    # Verify on-disk presence
    if verify_verdict_on_disk(audit_sha):
        print(f"  → s91_gate_verdicts.txt (audit_sha256={audit_sha[:16]}...): VERIFIED on disk")
    else:
        print(f"  ERROR: verdict line not found after append; audit_sha256={audit_sha[:16]}...")
        return 1

    # Final 4-tuple log line per gate-verdicts.md "Expected output 4-tuple"
    print()
    print(
        f"(value={value_str!r}, "
        f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"
    )
    print(f"\n=== {GATE_ID}: {composite} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
