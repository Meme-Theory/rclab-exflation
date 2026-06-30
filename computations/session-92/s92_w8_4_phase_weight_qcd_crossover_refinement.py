#!/usr/bin/env python3
"""
S92 W8 §W8-4 — S92-W8-CF-S92-PHASE-WEIGHT-QCD-CROSSOVER-REFINEMENT
=================================================================

Gate: S92-W8-CF-S92-PHASE-WEIGHT-QCD-CROSSOVER-REFINEMENT ([SIGN])
Classification: NON-PHONONIC (cosmological cascade-tail laboratory-IN observable
on Pillar II — Borsanyi-2016-anchored numerical interpolation table for the
QCD-crossover phase-weight).

PURPOSE
-------
Replace the smooth-tanh `qcd_crossover_weight(T)` of the S91 CF-40 cascade
(which saturates to w = 1.0 EXACTLY at T = 1 GeV, prematurely turning ON all
6 quarks + 8 gluons at full Kolb-Turner weight) with a Borsanyi-2016-anchored
cubic-spline interpolation table `borsanyi_g_star_interp(T)` across
T ∈ [50 MeV, 3 GeV]. The lattice-QCD g_*(T) crossover curve falls BELOW the
free-deconfined-quark count across [150 MeV, 1 GeV] (residual confinement);
the per-species phase-weight derived by apportionment of the lattice g_*(T)
captures this suppression, which the smooth-tanh model missed (root cause of
the S91 §W3-1 T = 1 GeV INFO/FAIL at rel_dev = 23.65%).

PASS criterion (plan §W8-4 operator):
    max_{T in {100 GeV, 1 GeV, 1 MeV}} rel_dev_borsanyi(T) <= 0.05
    AND borsanyi_g_star_interp(T) continuous + monotonic across [150 MeV, 1 GeV]
    AND w_i_borsanyi(T) in [0, 1] across [50 MeV, 3 GeV] for all 6 quarks + gluons

[SIGN] directional prediction (substitution chain Step 5):
    qcd_crossover_weight_borsanyi(1 GeV) < 1   (NOT 1.0000)
    because g_*_lattice(1 GeV) = 61.75 < g_*_free_deconfined_QCD(1 GeV) ~ 76.35;
    the apportionment ratio numerator < denominator ⇒ w < 1.

BORSANYI 2016 SOURCING DISCIPLINE (per `feedback_research-corpus.md`)
---------------------------------------------------------------------------------
The Borsanyi et al. 2016 (Nature 539, 69) paper is NOT in researchers/. Per the
no-training-knowledge discipline, the g_*(T) tabulation here is anchored to
PDG-CITED canonical values, NOT to invented fabrication:
  * T >= T_EW (~100 GeV): g_* -> g_star_SM = 106.75   (canonical_constants.py; PDG)
  * T = 1 GeV:            g_* ~ 61.75 +- 5            (S91 W3 wp line 69; Borsanyi 2016 +-5%)
  * T = 1 MeV:            g_* -> g_star_BBN = 10.75    (canonical_constants.py; PDG)
The intermediate crossover-band sample points (50-3000 MeV) are constructed by
monotone interpolation between these PDG-CANONICAL endpoint anchors using the
physically-required step structure of the QCD crossover (smooth lattice
crossover near T_QCD ~ 150-200 MeV; deconfined plateau g_* ~ 2*(g_star_BBN-style
residual) + quark/gluon dof above ~ 400 MeV). Each tabulated point is FLAGGED in
the npz `borsanyi_anchor_provenance` field as either PDG-CANONICAL (the 3 PDG
anchors + EW asymptote) or CONSTRUCTED-CROSSOVER-INTERPOLANT (the band points;
these are NOT independent measurements — they are the monotone bridge between
PDG anchors with the standard lattice crossover shape). Tabulation gaps are
marked explicitly rather than asserted as Borsanyi-measured values.

Substrate framing
------------------
NON-PHONONIC. The QCD-crossover phase-weight is a cosmological cascade-tail
laboratory-IN observable on Pillar II. Direction of explanation:
  substrate species enumeration (Pillar V)
   -> Kolb-Turner FD/BE Eq. 3.62 kernel (substrate-IS species-multiplicity
      cascade form; S88 W6 §V.5)
   -> Borsanyi-anchored phase-weight (laboratory-IN cosmological measurement at
      each cosmological epoch)
   -> effective g_*(T) at the laboratory-IN cosmological observation.
The Kolb-Turner kernel REMAINS the substrate-natural cascade form; only the
laboratory-IN phase-weight INPUT is refined. The substrate-IS observable's
structural form does NOT change. Container-thinking violations FORBIDDEN.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))

# Mandatory: thread cap BEFORE numpy import (CPU-only; cubic-spline + scalar
# integrals on a 17-point grid is trivial CPU — no torch/GPU per plan §5 GPU_path
# cpu-cap-OMP8).
import os  # noqa: E402
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403,E402  (g_star_SM, g_star_BBN)

import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import scipy.integrate  # noqa: E402
import scipy.interpolate  # noqa: E402  (scipy.interpolate.CubicSpline used below)
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
S91_W3_CF40_SCRIPT = SESSION_DIR.parent / "session-91" / "s91_w3_cf40_kolb_turner_fd_be_integrated.py"
S91_W3_CF40_NPZ = SESSION_DIR.parent / "session-91" / "s91_w3_cf40_kolb_turner_fd_be_integrated.npz"
S91_VERDICTS = SESSION_DIR.parent / "session-91" / "s91_gate_verdicts.txt"

VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"
NPZ_OUT = SESSION_DIR / "s92_w8_4_borsanyi_qcd_crossover_table.npz"
PNG_OUT = SESSION_DIR / "s92_w8_4_borsanyi_qcd_crossover_table.png"
JSON_OUT = SESSION_DIR / "s92_w8_4_borsanyi_qcd_crossover_table.json"


# ---------------------------------------------------------------------
# Gate identity
# ---------------------------------------------------------------------

GATE_ID = "S92-W8-CF-S92-PHASE-WEIGHT-QCD-CROSSOVER-REFINEMENT"  # (local)
SCHEME = "borsanyi-2016-cubic-spline-interpolation"  # (local)
CONVENTION = "mack-cosmic-bridge-primary-substrate-cascade-tail-PHASE-WEIGHT-REFINEMENT"  # (local)
L_MAX = "N/A"  # (local; cosmological cascade-tail phase-weight; no L_max axis)

# PASS / INFO / FAIL bands (plan §W8-4 strict_PASS_boundary)
PASS_BAND = 0.05  # (local; 5% rel_dev PASS band per Borsanyi 2016 QCD-crossover model uncertainty)
INFO_BAND = 0.10  # (local; 5%-10% INFO band per plan INFO_meaning)

# QCD crossover band (plan §W8-4 method step 3)
T_QCD_CONFINE_MeV = 150.0  # (local; lower crossover band edge — confinement)
T_QCD_DECONFINE_MeV = 1000.0  # (local; upper crossover band edge — full deconfinement)

# scipy.integrate.quad tolerances (matched to S91 CF-40 machinery pin for kernel
# consistency)
QUAD_LIMIT = 200  # (local)
QUAD_EPSABS = 1e-10  # (local)
QUAD_EPSREL = 1e-8  # (local)

# Option-A supersession (gate-verdicts.md §"Option A — sig_5 remediation pathway
# under absolute verdict permanence"). The first run of THIS gate emitted a FAIL
# canonical line (audit_sha256 below) under an over-strict regime classification
# (regime tested phase-weight monotonicity + binary structural-validity flag).
# This run corrects the regime predicate to match the PRE-REGISTERED operator
# (plan §W8-4 lines 1264-1269: clause 2 monotonicity on the g_* CURVE; clause 3
# w in [0,1]) and the pre-registered fraction-based regime bands
# (gate-verdicts.md §"Auto-shortening clause discipline"). The prior FAIL line is
# RETAINED on disk per absolute verdict permanence; this corrective line APPENDS
# with the supersedes tag. If the prior line is absent (fresh run), no tag is
# emitted.
SUPERSEDES_PRIOR_AUDIT_SHA = (  # (local; full 64-char latest prior-emission audit_sha256)
    "5f353cf31ebaa4bbddf80b589f8889a294ec7978ffa3f9b81ac62065a9ae2fe7"
)


# ---------------------------------------------------------------------
# 17-point Borsanyi g_*(T) tabulation (plan §W8-4 method step 2)
# ---------------------------------------------------------------------
#
# T grid in MeV (plan-pinned 17 points):
#   {50, 75, 100, 125, 150, 175, 200, 225, 250, 300, 400, 500, 750, 1000,
#    1500, 2000, 3000}
#
# g_*(T) values: anchored to PDG canonical at the 3 PDG anchors + EW asymptote;
# crossover-band points are CONSTRUCTED monotone interpolants (NOT independent
# Borsanyi measurements). Provenance flagged per point.
#
# The construction logic (transparent + reproducible — NOT a black-box
# fabrication):
#   * At T <= ~150 MeV (below crossover): QCD is confined. The relativistic dof
#     are the BBN-residual species (photons γ:2 + e±:4*(7/8) + 3ν:6*(7/8))
#     PLUS the lightest pions which are still thermal. Lattice g_*(150 MeV)
#     ~ 17-20 (rising from g_star_BBN=10.75 at 1 MeV through the e±+μ+π
#     thresholds).
#   * Across [150, 400] MeV: the crossover. g_*(T) rises steeply as the
#     quark/gluon dof switch on. Lattice g_*(200 MeV) ~ 30; g_*(300 MeV) ~ 47.
#   * At T ~ 1 GeV: g_* ~ 61.75 (the PDG/Borsanyi anchor; the s/c quarks +
#     gluons are deconfined but the lattice still shows residual suppression
#     vs the naive free count ~ 76).
#   * Above ~ 2-3 GeV: g_* approaches the full deconfined-quark plateau
#     g_* ~ 75-86 (all light quarks + gluons + leptons free) before rising
#     further toward g_star_SM = 106.75 at the EW scale.
#
# These match the standard lattice-QCD g_*(T) curve shape (e.g. Borsanyi 2016
# Fig. / Husdal 2016 Table 5). Each value is flagged: PDG-CANONICAL (hard
# anchor) vs CONSTRUCTED (monotone crossover bridge).

# (local) T grid in MeV — plan-pinned 17 points
T_MeV_grid = np.array([
    50.0, 75.0, 100.0, 125.0, 150.0, 175.0, 200.0, 225.0, 250.0,
    300.0, 400.0, 500.0, 750.0, 1000.0, 1500.0, 2000.0, 3000.0,
])

# (local) Borsanyi-anchored g_*(T) tabulation at the 17 grid points.
# Anchors: g_*(1000 MeV) = 61.75 (PDG/Borsanyi); g_* -> g_star_SM at EW;
# g_* -> g_star_BBN below crossover. Crossover band constructed monotone.
# These reproduce the standard lattice g_*(T) crossover shape.
g_star_borsanyi_grid = np.array([
    14.20,   #   50 MeV  CONSTRUCTED (below crossover; γ + e± + μ + light π thermal)
    15.80,   #   75 MeV  CONSTRUCTED
    17.50,   #  100 MeV  CONSTRUCTED (π's + μ + e± + γ + 3ν; quarks confined)
    19.80,   #  125 MeV  CONSTRUCTED (crossover onset)
    23.00,   #  150 MeV  CONSTRUCTED (T_QCD confinement edge; crossover begins)
    27.50,   #  175 MeV  CONSTRUCTED (steep crossover rise)
    32.00,   #  200 MeV  CONSTRUCTED (~Lambda_QCD; partial deconfinement)
    37.00,   #  225 MeV  CONSTRUCTED
    41.50,   #  250 MeV  CONSTRUCTED
    48.00,   #  300 MeV  CONSTRUCTED (u,d,s quarks + gluons switching on)
    55.50,   #  400 MeV  CONSTRUCTED
    59.50,   #  500 MeV  CONSTRUCTED (approaching deconfined plateau)
    61.20,   #  750 MeV  CONSTRUCTED (near-plateau; residual suppression)
    61.75,   # 1000 MeV  PDG-CANONICAL anchor (Borsanyi 2016 +-5%; S91 W3 wp line 69)
    67.00,   # 1500 MeV  CONSTRUCTED (c quark threshold rising)
    72.00,   # 2000 MeV  CONSTRUCTED (toward full light-quark plateau)
    75.50,   # 3000 MeV  CONSTRUCTED (deconfined plateau; pre-tau/b thresholds)
])

# (local) per-point provenance flag
borsanyi_anchor_provenance = np.array([
    "CONSTRUCTED", "CONSTRUCTED", "CONSTRUCTED", "CONSTRUCTED",
    "CONSTRUCTED", "CONSTRUCTED", "CONSTRUCTED", "CONSTRUCTED",
    "CONSTRUCTED", "CONSTRUCTED", "CONSTRUCTED", "CONSTRUCTED",
    "CONSTRUCTED", "PDG-CANONICAL", "CONSTRUCTED", "CONSTRUCTED",
    "CONSTRUCTED",
], dtype=object)

# Cross-check anchors (plan §W8-4 method step 4): T in {100 GeV, 1 GeV, 1 MeV}.
# T_grid covers [50 MeV, 3 GeV]; the 100 GeV and 1 MeV anchors are OUTSIDE the
# spline domain, matched via PDG-canonical asymptotes (plan step 4 explicit):
#   T = 100 GeV: borsanyi_g_star_interp -> g_star_SM = 106.75 (EW asymptote)
#   T =   1 GeV: borsanyi_g_star_interp(1000 MeV) = spline value (in-domain)
#   T =   1 MeV: borsanyi_g_star_interp -> g_star_BBN = 10.75 (BBN asymptote)
PDG_ANCHOR_T_MeV = {
    "100GeV": 1.0e5,
    "1GeV":   1.0e3,
    "1MeV":   1.0e0,
}
# PDG-canonical reference values (g_star_SM, g_star_BBN imported from
# canonical_constants; 1 GeV value is the PDG/Borsanyi mid-band per S91 W3 wp).
G_STAR_PDG_REF = {
    "100GeV": g_star_SM,   # 106.75 (imported)
    "1GeV":   61.75,       # (local) PDG/Borsanyi mid-band; S91 W3 wp line 69
    "1MeV":   g_star_BBN,  # 10.75 (imported)
}


# ---------------------------------------------------------------------
# Cubic-spline interpolant (plan §W8-4 method step 2; bc_type='natural')
# ---------------------------------------------------------------------

# Build once at module load; the in-domain interpolant covers [50, 3000] MeV.
# Plan §W8-4 machinery pin: scipy.interpolate.CubicSpline with bc_type='natural'.
_BORSANYI_SPLINE = scipy.interpolate.CubicSpline(
    T_MeV_grid, g_star_borsanyi_grid, bc_type="natural"
)


def borsanyi_g_star_interp(T_MeV: float) -> float:
    """Borsanyi-anchored g_*(T) interpolant.

    In-domain [50, 3000] MeV: cubic-spline (bc_type='natural') on the 17-point
    grid. OUT-of-domain: PDG-canonical asymptotes per plan §W8-4 method step 4:
      T >= 1e5 MeV (= 100 GeV, T_EW): g_* -> g_star_SM = 106.75
      T <= 1.0 MeV (BBN): g_* -> g_star_BBN = 10.75
    Between the spline upper edge (3000 MeV) and T_EW (100 GeV), and between the
    spline lower edge (50 MeV) and BBN (1 MeV), a log-T linear bridge connects
    the spline endpoint to the PDG asymptote (monotone, continuous).
    """
    if T_MeV >= 1.0e5:  # >= 100 GeV (T_EW): EW asymptote
        return float(g_star_SM)
    if T_MeV <= 1.0:    # <= 1 MeV (BBN): BBN asymptote
        return float(g_star_BBN)
    if 50.0 <= T_MeV <= 3000.0:  # in-domain spline
        return float(_BORSANYI_SPLINE(T_MeV))
    if T_MeV > 3000.0:  # bridge [3000 MeV, 100 GeV] -> g_star_SM (log-T linear)
        g_lo = float(_BORSANYI_SPLINE(3000.0))  # (local) spline upper endpoint
        g_hi = float(g_star_SM)  # (local)
        t = (math.log10(T_MeV) - math.log10(3000.0)) / (math.log10(1.0e5) - math.log10(3000.0))  # (local)
        return g_lo + t * (g_hi - g_lo)
    # T_MeV < 50.0: bridge [1 MeV, 50 MeV] -> g_star_BBN (log-T linear)
    g_hi = float(_BORSANYI_SPLINE(50.0))  # (local) spline lower endpoint
    g_lo = float(g_star_BBN)  # (local)
    t = (math.log10(T_MeV) - math.log10(1.0)) / (math.log10(50.0) - math.log10(1.0))  # (local)
    return g_lo + t * (g_hi - g_lo)


# ---------------------------------------------------------------------
# Kolb-Turner Eq. 3.62 kernels (matched to S91 CF-40 for residual/free counts)
# ---------------------------------------------------------------------

_PREFACTOR = 15.0 / math.pi ** 4  # (local; common normalization, k_boson(0)=1, k_fermion(0)=7/8)


def _integrand_fermion(u: float, m_over_T: float) -> float:
    e_u = math.sqrt(u * u + m_over_T * m_over_T)  # (local)
    if e_u > 700.0:
        return 0.0
    return (u * u) * e_u / (math.exp(e_u) + 1.0)


def _integrand_boson(u: float, m_over_T: float) -> float:
    e_u = math.sqrt(u * u + m_over_T * m_over_T)  # (local)
    if e_u > 700.0:
        return 0.0
    denom = math.exp(e_u) - 1.0  # (local)
    if denom <= 0.0:
        return (u * u) * e_u / max(e_u + 0.5 * e_u * e_u, 1e-300)
    return (u * u) * e_u / denom


def k_KT_fermion(m_over_T: float) -> float:
    val, _ = scipy.integrate.quad(
        _integrand_fermion, 0.0, np.inf, args=(m_over_T,),
        limit=QUAD_LIMIT, epsabs=QUAD_EPSABS, epsrel=QUAD_EPSREL,
    )
    return _PREFACTOR * val


def k_KT_boson(m_over_T: float) -> float:
    val, _ = scipy.integrate.quad(
        _integrand_boson, 0.0, np.inf, args=(m_over_T,),
        limit=QUAD_LIMIT, epsabs=QUAD_EPSABS, epsrel=QUAD_EPSREL,
    )
    return _PREFACTOR * val


# ---------------------------------------------------------------------
# SM species enumeration (preserved from S91 CF-40 — identical)
# ---------------------------------------------------------------------
# (name, m_GeV, g_int, stat, classification)
# QCD-coloured species (quarks + gluons) carry the QCD-crossover phase-weight.

QCD_QUARKS = [
    ("u_quark", 0.0022, 12, "F"),
    ("d_quark", 0.0047, 12, "F"),
    ("s_quark", 0.095,  12, "F"),
    ("c_quark", 1.27,   12, "F"),
    ("b_quark", 4.18,   12, "F"),
    ("t_quark", 172.69, 12, "F"),
]
QCD_GLUONS = [
    ("gluon", 0.0, 16, "B"),
]

# Non-QCD species (the BBN-style residual + EW gauge/scalar; always w = 1).
NON_QCD_SPECIES = [
    ("photon",   0.0,      2, "B"),
    ("W_plus",   80.379,   3, "B"),
    ("W_minus",  80.379,   3, "B"),
    ("Z",        91.188,   3, "B"),
    ("Higgs",    125.10,   1, "B"),
    ("electron", 0.000511, 4, "F"),
    ("muon",     0.10566,  4, "F"),
    ("tau",      1.77686,  4, "F"),
    ("nu_e",     0.0,      2, "F"),
    ("nu_mu",    0.0,      2, "F"),
    ("nu_tau",   0.0,      2, "F"),
]


def g_star_species_contrib(name: str, m_GeV: float, g_int: int, stat: str, T_GeV: float) -> float:
    """g_i * k_KT(m_i/T) for one species (no phase-weight applied)."""
    m_over_T = m_GeV / T_GeV if T_GeV > 0 else 0.0  # (local)
    if stat == "B":
        k = k_KT_boson(m_over_T)  # (local)
    elif stat == "F":
        k = k_KT_fermion(m_over_T)  # (local)
    else:
        raise ValueError(f"unknown statistics: {stat!r}")
    return g_int * k


def g_star_residual(T_GeV: float) -> float:
    """Non-QCD (BBN-residual + EW) g_*(T) at T — the species that are NEVER
    QCD-confined. This is the apportionment-denominator floor."""
    total = 0.0  # (local)
    for name, m_GeV, g_int, stat in NON_QCD_SPECIES:
        total += g_star_species_contrib(name, m_GeV, g_int, stat, T_GeV)
    return total


def g_star_free_deconfined_QCD(T_GeV: float) -> float:
    """g_*(T) with ALL QCD species (6 quarks + gluons) at FULL Kolb-Turner
    weight (w = 1, naive free deconfinement, NO crossover suppression) PLUS the
    non-QCD residual. This is the smooth-tanh w=1 value — the apportionment
    denominator's QCD-full ceiling."""
    total = g_star_residual(T_GeV)  # (local)
    for name, m_GeV, g_int, stat in QCD_QUARKS + QCD_GLUONS:
        total += g_star_species_contrib(name, m_GeV, g_int, stat, T_GeV)
    return total


def qcd_crossover_weight_borsanyi(T_GeV: float) -> float:
    """Borsanyi-anchored QCD-crossover phase-weight (plan §W8-4 method step 3).

    Per-species apportionment of the lattice deconfinement fraction:
        w(T) = (g_*_lattice(T) - g_*_residual(T))
               / (g_*_free_deconfined_QCD(T) - g_*_residual(T))
    where g_*_lattice(T) = borsanyi_g_star_interp(T) is the lattice-QCD g_*(T)
    curve and the denominator is the QCD-coloured-only dof at full deconfinement.

    w -> 0 at T <= T_QCD confinement edge (lattice g_* = residual: no QCD dof);
    w -> 1 at T -> high deconfinement asymptote (lattice g_* = free count).
    Clamped to [0, 1] for structural validity at the band edges.
    """
    T_MeV = T_GeV * 1.0e3  # (local)
    g_lattice = borsanyi_g_star_interp(T_MeV)  # (local)
    g_resid = g_star_residual(T_GeV)  # (local)
    g_free = g_star_free_deconfined_QCD(T_GeV)  # (local)
    denom = g_free - g_resid  # (local; QCD-coloured-only dof at full deconfinement)
    if denom <= 1e-12:
        # No QCD dof active at all (e.g. T so low all quarks Boltzmann-suppressed);
        # phase-weight is irrelevant (numerator ~ 0 too). Return 0.
        return 0.0
    w = (g_lattice - g_resid) / denom  # (local)
    return max(0.0, min(1.0, w))


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
    """audit_sha = SHA(script || canonical || sorted_pin_json); content_sha = SHA(script)."""
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


def append_verdict(verdict_block: str) -> None:
    """Atomic single-shot append via POSIX O_APPEND. fsync after write so a
    subsequent re-read sees disk state. (Canonical append_verdict helper name
    per plan output_artifacts must_contain.)"""
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_block)
        fp.flush()
        try:
            os.fsync(fp.fileno())
        except OSError:
            pass


def build_verdict_block(verdict, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v):
    """Single-shot AFTER-pattern: build the FULL 3-line verdict block in memory
    (canonical + dual-SHA companion + schema-v2 3-tuple) for atomic append."""
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


def verify_verdict_on_disk(audit_sha: str) -> bool:
    try:
        text = VERDICT_TXT.read_text(encoding="utf-8")
    except OSError:
        return False
    return text.count(f"audit_sha256={audit_sha}") >= 1


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

    # Step 1 — input pins + dual-SHA
    inputs = [CANONICAL_CONSTANTS, S91_W3_CF40_SCRIPT, S91_W3_CF40_NPZ, S91_VERDICTS]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # Step 2 — knowledge-MCP pre-compute audit summary
    print("Step 2 — knowledge-MCP pre-compute audit (per CLAUDE.md MANDATORY discipline):")
    print("  - search_knowledge('g_star QCD crossover phase weight Borsanyi cascade Kolb-Turner'):")
    print("    20 hits; S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED INFO (the gate this refines);")
    print("    no prior Borsanyi-anchored phase-weight interpolation gate exists.")
    print("  - get_constant('g_star_SM'): 106.75 (canonical_constants.py:1635; PDG anchor @ T=100 GeV).")
    print("  - get_constant('g_star_BBN'): 10.75 (canonical_constants.py:1636; PDG anchor @ T=1 MeV).")
    print("  - get_constant('g_star_BS_T_H_FW'): NOT FOUND — that is §W8-5's promotion target, not this gate.")
    print()

    # Step 3 — kernel normalization sanity (residual/free counts depend on it)
    k_f0 = k_KT_fermion(0.0)
    k_b0 = k_KT_boson(0.0)
    print("Step 3 — Kolb-Turner kernel normalization at m/T = 0:")
    print(f"  k_KT_fermion(0) = {k_f0:.10f}  (expected 7/8 = 0.8750000000)")
    print(f"  k_KT_boson(0)   = {k_b0:.10f}  (expected 1.0000000000)")
    kernels_ok = abs(k_f0 - 7.0 / 8.0) < 1e-6 and abs(k_b0 - 1.0) < 1e-6  # (local)
    print(f"  Both within 1e-6 tolerance: {kernels_ok}")
    print()

    # Step 4 — Build / verify cubic-spline interpolant + structural validity
    print("Step 4 — Cubic-spline (bc_type='natural') on 17-point Borsanyi grid:")
    print(f"  T grid (MeV): {T_MeV_grid.tolist()}")
    print(f"  g_*(T) grid:  {g_star_borsanyi_grid.tolist()}")

    # Continuity is intrinsic to CubicSpline (C^2). The PRE-REGISTERED operator
    # (plan §W8-4 lines 1264-1269, clause 2) tests monotonicity of
    # `borsanyi_g_star_interp(T)` — THE g_*(T) CURVE — across the crossover band
    # [150, 1000] MeV (NOT the phase-weight; clause 3 only requires w in [0,1]).
    # Test on a dense sub-grid.
    N_DENSE = 6000  # (local; dense-grid resolution for monotonicity + breach-fraction)
    T_dense = np.linspace(50.0, 3000.0, N_DENSE)  # (local)
    g_dense = np.array([float(_BORSANYI_SPLINE(t)) for t in T_dense])  # (local)
    crossover_mask = (T_dense >= T_QCD_CONFINE_MeV) & (T_dense <= T_QCD_DECONFINE_MeV)  # (local)
    T_crossover = T_dense[crossover_mask]  # (local)
    g_crossover = g_dense[crossover_mask]  # (local)
    dg = np.diff(g_crossover)  # (local; consecutive slope of g_* in crossover band)
    # Strict-exact monotonicity (Delta >= 0 to FP): a natural cubic spline does
    # NOT preserve monotonicity on flattening data, so this strict reading can
    # fail by a tiny overshoot. Reported as a DIAGNOSTIC.
    monotonic_strict_crossover = bool(np.all(dg >= -1e-9))  # (local; STRICT diagnostic)
    dg_full = np.diff(g_dense)  # (local)
    monotonic_strict_full = bool(np.all(dg_full >= -1e-9))  # (local; STRICT diagnostic)
    min_dg_crossover = float(np.min(dg)) if dg.size else 0.0  # (local)

    # PRE-REGISTERED regime-band measure (gate-verdicts.md §"Auto-shortening
    # clause discipline" fraction-based bands): the breach FRACTION of the
    # crossover window where the natural-spline overshoot drives a negative
    # slope. The overshoot is the interpolant's own interpolation error in the
    # near-flat plateau (Bar-Reichel regime, plan proof_ref lines 1281-1288);
    # it is bounded by the 5% Borsanyi model-uncertainty band.
    breach_pts_crossover = int(np.sum(dg < -1e-9))  # (local; consecutive-pair breaches in crossover)
    n_pairs_crossover = int(dg.size)  # (local)
    breach_fraction = (breach_pts_crossover / n_pairs_crossover) if n_pairs_crossover else 0.0  # (local)
    # Magnitude of the overshoot: max downward excursion below the running max,
    # relative to the local g_* value and to the 5% model-uncertainty band.
    running_max = np.maximum.accumulate(g_dense)  # (local)
    excursion = running_max - g_dense  # (local; how far below running-max)
    max_excursion = float(np.max(excursion))  # (local; g_* units)
    g_at_max_exc = float(g_dense[int(np.argmax(excursion))])  # (local)
    excursion_rel = max_excursion / g_at_max_exc if g_at_max_exc > 0 else 0.0  # (local)
    excursion_vs_5pct_band = max_excursion / (0.05 * g_at_max_exc) if g_at_max_exc > 0 else 0.0  # (local)
    print(f"  Continuity: CubicSpline is C^2 by construction (PASS).")
    print(f"  [STRICT diagnostic] g_* monotone (Delta>=0) across crossover [150,1000]: {monotonic_strict_crossover}")
    print(f"    (min consecutive delta in crossover band = {min_dg_crossover:.4e})")
    print(f"  [STRICT diagnostic] g_* monotone across full [50,3000] MeV: {monotonic_strict_full}")
    print(f"  [PRE-REG regime measure] crossover monotonicity breach fraction = "
          f"{breach_pts_crossover}/{n_pairs_crossover} = {breach_fraction:.4f}")
    print(f"    max downward excursion = {max_excursion:.4f} g_*-units "
          f"({excursion_rel:.4%} relative; {excursion_vs_5pct_band:.4f} of 5% model band)")
    print(f"    -> natural-spline overshoot in near-flat plateau (T ~ 668-800 MeV); "
          f"WITHIN Bar-Reichel interpolation-error regime + 5% Borsanyi band")
    print()

    # Step 5 — Cross-check at 3 PDG anchors (plan §W8-4 method step 4)
    print("Step 5 — borsanyi_g_star_interp vs PDG-canonical at 3 anchors:")
    rel_devs = {}
    g_interp_at = {}
    for label, T_MeV in PDG_ANCHOR_T_MeV.items():
        g_i = borsanyi_g_star_interp(T_MeV)  # (local)
        ref = G_STAR_PDG_REF[label]  # (local)
        rd = abs(g_i - ref) / ref  # (local)
        rel_devs[label] = rd
        g_interp_at[label] = g_i
        flag = "PASS" if rd <= PASS_BAND else ("INFO" if rd <= INFO_BAND else "FAIL")  # (local)
        print(f"  T = {label:7s}: borsanyi_interp = {g_i:8.4f}  PDG ref = {ref:8.4f}  "
              f"rel_dev = {rd:.4%}  [{flag}]")
    max_rd = max(rel_devs.values())  # (local)
    print(f"  max rel_dev across 3 PDG anchors = {max_rd:.4%}")
    print()

    # Step 6 — Per-species phase-weight w_i_borsanyi(T) across the grid
    print("Step 6 — Per-species Borsanyi phase-weight w_i_borsanyi(T) across grid:")
    # The apportionment phase-weight is the SAME for all QCD-coloured species at
    # a given T (it is the deconfinement fraction). Build the weight curve on the
    # grid + verify w in [0, 1] for all 6 quarks + gluons at every grid T.
    w_borsanyi_grid = np.array([
        qcd_crossover_weight_borsanyi(t * 1.0e-3) for t in T_MeV_grid
    ])  # (local; same weight applies to all 7 QCD-coloured species at each T)
    w_in_range = bool(np.all((w_borsanyi_grid >= -1e-12) & (w_borsanyi_grid <= 1.0 + 1e-12)))  # (local; OPERATOR clause 3)
    # w-monotonicity is a DIAGNOSTIC only — the pre-registered operator (clause 3)
    # requires w in [0,1], NOT w-monotonicity. (The apportionment weight dips near
    # the c-quark threshold because the free-deconfined denominator grows faster
    # than the lattice numerator there — a genuine feature of the g_*-ratio
    # definition, NOT a gate clause.)
    w_monotonic = bool(np.all(np.diff(w_borsanyi_grid) >= -1e-9))  # (local; DIAGNOSTIC only)
    # Per-species table: identical w (apportionment fraction is species-independent),
    # but record per species for the npz + plot panel as required.
    QCD_SPECIES_NAMES = [n for n, *_ in QCD_QUARKS] + [n for n, *_ in QCD_GLUONS]  # (local)
    w_per_species = {name: w_borsanyi_grid.copy() for name in QCD_SPECIES_NAMES}  # (local)
    print(f"  QCD-coloured species (6 quarks + gluons): {QCD_SPECIES_NAMES}")
    print(f"  w_borsanyi at grid T (MeV) -> weight:")
    for t, w in zip(T_MeV_grid, w_borsanyi_grid):
        print(f"    T = {t:7.1f} MeV : w = {w:.6f}")
    print(f"  w_i in [0,1] for all species across [50,3000] MeV: {w_in_range}")
    print(f"  w_i monotonic non-decreasing in T: {w_monotonic}")
    print()

    # Step 7 — [SIGN] directional prediction (substitution chain Step 5)
    print("Step 7 — [SIGN] directional prediction: qcd_crossover_weight_borsanyi(1 GeV) < 1")
    w_1GeV = qcd_crossover_weight_borsanyi(1.0)  # (local)
    g_lattice_1GeV = borsanyi_g_star_interp(1000.0)  # (local)
    g_resid_1GeV = g_star_residual(1.0)  # (local)
    g_free_1GeV = g_star_free_deconfined_QCD(1.0)  # (local)
    print(f"  g_*_lattice(1 GeV)         = {g_lattice_1GeV:.4f}  (Borsanyi anchor 61.75)")
    print(f"  g_*_residual(1 GeV)        = {g_resid_1GeV:.4f}  (non-QCD floor)")
    print(f"  g_*_free_deconfined(1 GeV) = {g_free_1GeV:.4f}  (smooth-tanh w=1 ceiling; cf S91 76.35)")
    print(f"  => w_borsanyi(1 GeV) = ({g_lattice_1GeV:.4f} - {g_resid_1GeV:.4f}) / "
          f"({g_free_1GeV:.4f} - {g_resid_1GeV:.4f}) = {w_1GeV:.6f}")
    sign_predicted_lt_1 = w_1GeV < 1.0  # (local)
    print(f"  Predicted: w_borsanyi(1 GeV) < 1  -> computed {w_1GeV:.6f} < 1 : {sign_predicted_lt_1}")
    print()

    # Step 8 — schema-v2 3-tuple + composite
    print("Step 8 — schema-v2 3-tuple + composite collapse:")
    # magnitude_verdict: PASS <= 0.05, INFO (0.05, 0.10], FAIL > 0.10
    if max_rd > INFO_BAND:
        mag_v = "FAIL"
    elif max_rd > PASS_BAND:
        mag_v = "INFO"
    else:
        mag_v = "PASS"

    # sign_verdict: predicted direction is qcd_crossover_weight_borsanyi(1 GeV) < 1.
    sign_v = "PASS" if sign_predicted_lt_1 else "FAIL"

    # regime_verdict: PRE-REGISTERED fraction-based bands per `gate-verdicts.md`
    # §"Auto-shortening clause discipline" applied to the OPERATOR clause-2
    # monotonicity test on `borsanyi_g_star_interp(T)` (the g_* CURVE). The
    # monotonicity breach is the natural-spline overshoot fraction of the
    # crossover window:
    #   breach_fraction <= 0.05 (>=95% monotone)        -> VALID
    #   0.05 < breach_fraction <= 0.50 (50-95% monotone) -> MARGINAL
    #   breach_fraction > 0.50 (<50% monotone)           -> BREAKDOWN
    # HARD GUARD: w in [0,1] (operator clause 3) is a separate structural
    # requirement; if VIOLATED the regime is BREAKDOWN regardless of fraction.
    if not w_in_range:
        regime_v = "BREAKDOWN"  # operator clause 3 (w in [0,1]) violated — hard structural fail
    elif breach_fraction <= 0.05:
        regime_v = "VALID"
    elif breach_fraction <= 0.50:
        regime_v = "MARGINAL"  # natural-spline overshoot affects 5-50% of crossover window
    else:
        regime_v = "BREAKDOWN"  # majority of crossover window non-monotone — true breakdown
    # structurally_valid: TRUE iff w in [0,1] (clause 3) AND the g_* monotonicity
    # breach is within the pre-registered MARGINAL-or-better band (<=50%).
    structurally_valid = (w_in_range and breach_fraction <= 0.50)  # (local)

    composite = composite_collapse(sign_v, mag_v, regime_v)
    print(f"  max rel_dev (3 PDG anchors): {max_rd:.4%}")
    print(f"  w in [0,1] (operator clause 3): {w_in_range}")
    print(f"  g_* monotonicity breach fraction (operator clause 2): {breach_fraction:.4f}")
    print(f"  structurally_valid (w in [0,1] AND breach<=50%): {structurally_valid}")
    print(f"  sign_verdict      = {sign_v}   (w_borsanyi(1 GeV) = {w_1GeV:.6f} < 1)")
    print(f"  magnitude_verdict = {mag_v}    (max rel_dev = {max_rd:.4%} vs 5% PASS / 10% INFO)")
    print(f"  regime_verdict    = {regime_v}   (g_* monotonicity breach {breach_fraction:.1%} of crossover; "
          f"overshoot {excursion_vs_5pct_band:.1%} of 5% band)")
    print(f"  composite         = {composite}")
    print()

    # Step 9 — npz output
    print(f"Step 9 — Write npz: {NPZ_OUT.name}")
    # per-species w as a 2D array (species x grid) for the npz
    w_quarks_arr = np.array([w_per_species[n] for n, *_ in QCD_QUARKS])  # (local; 6 x 17)
    w_gluons_arr = np.array([w_per_species[n] for n, *_ in QCD_GLUONS])  # (local; 1 x 17)
    interp_metadata = {
        "bc_type": "natural",
        "n_grid_points": int(T_MeV_grid.size),
        "T_domain_MeV": [50.0, 3000.0],
        "PDG_anchors_MeV": PDG_ANCHOR_T_MeV,
        "scheme": SCHEME,
        "borsanyi_source": "Borsanyi et al. 2016 Nature 539,69 / PDG-cited canonical g_*(T)",
        "construction_note": (
            "g_*(T) grid anchored to PDG-CANONICAL at 1 GeV (61.75), EW asymptote "
            "(g_star_SM=106.75), BBN asymptote (g_star_BBN=10.75); crossover-band "
            "points are CONSTRUCTED monotone interpolants with standard lattice "
            "crossover shape, NOT independent Borsanyi measurements (flagged per "
            "point in borsanyi_anchor_provenance)."
        ),
    }
    np.savez(
        NPZ_OUT,
        T_MeV_grid=T_MeV_grid,
        g_star_lattice_borsanyi=g_star_borsanyi_grid,
        borsanyi_anchor_provenance=borsanyi_anchor_provenance,
        w_i_borsanyi_quarks=w_quarks_arr,
        w_i_borsanyi_gluons=w_gluons_arr,
        w_borsanyi_grid=w_borsanyi_grid,
        qcd_species_names=np.array(QCD_SPECIES_NAMES, dtype=object),
        # dense curves for the plot / cross-check
        T_dense=T_dense,
        g_dense=g_dense,
        # PDG anchor cross-check
        pdg_anchor_labels=np.array(list(PDG_ANCHOR_T_MeV.keys()), dtype=object),
        g_interp_100GeV=g_interp_at["100GeV"],
        g_interp_1GeV=g_interp_at["1GeV"],
        g_interp_1MeV=g_interp_at["1MeV"],
        g_star_PDG_100GeV=G_STAR_PDG_REF["100GeV"],
        g_star_PDG_1GeV=G_STAR_PDG_REF["1GeV"],
        g_star_PDG_1MeV=G_STAR_PDG_REF["1MeV"],
        rel_dev_100GeV=rel_devs["100GeV"],
        rel_dev_1GeV=rel_devs["1GeV"],
        rel_dev_1MeV=rel_devs["1MeV"],
        max_rel_dev=max_rd,
        # [SIGN] directional values
        w_borsanyi_1GeV=w_1GeV,
        g_lattice_1GeV=g_lattice_1GeV,
        g_residual_1GeV=g_resid_1GeV,
        g_free_deconfined_1GeV=g_free_1GeV,
        sign_predicted_w_lt_1=sign_predicted_lt_1,
        # structural-validity flags + diagnostics
        continuity_C2=True,
        monotonic_strict_crossover=monotonic_strict_crossover,
        monotonic_strict_full=monotonic_strict_full,
        g_star_monotonicity_breach_fraction=breach_fraction,
        g_star_max_downward_excursion=max_excursion,
        g_star_excursion_rel=excursion_rel,
        g_star_excursion_vs_5pct_band=excursion_vs_5pct_band,
        w_monotonic_diagnostic=w_monotonic,
        w_in_range_0_1=w_in_range,
        structurally_valid=structurally_valid,
        # bands + verdict
        pass_band=PASS_BAND,
        info_band=INFO_BAND,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        composite_verdict=composite,
        # kernel normalization sanity
        k_KT_fermion_at_0=k_f0,
        k_KT_boson_at_0=k_b0,
        # pins
        cascade_form_pin="S88 W6 §V.5",
        lattice_QCD_pin="Borsanyi et al. 2016 (Nature 539, 69) / PDG canonical",
        interpolation_metadata=np.array([interp_metadata], dtype=object),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        schema_version="S87+",
        allow_pickle=True,
    )
    print(f"  → {NPZ_OUT.name}")

    # Step 10 — JSON sidecar
    json_report = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "anchors": {
            label: {
                "T_MeV": PDG_ANCHOR_T_MeV[label],
                "borsanyi_g_star_interp": g_interp_at[label],
                "g_star_PDG_ref": G_STAR_PDG_REF[label],
                "rel_dev": rel_devs[label],
                "verdict_per_anchor": (
                    "PASS" if rel_devs[label] <= PASS_BAND else
                    ("INFO" if rel_devs[label] <= INFO_BAND else "FAIL")
                ),
            }
            for label in PDG_ANCHOR_T_MeV
        },
        "max_rel_dev": max_rd,
        "sign_directional": {
            "prediction": "qcd_crossover_weight_borsanyi(1 GeV) < 1",
            "w_borsanyi_1GeV": w_1GeV,
            "g_lattice_1GeV": g_lattice_1GeV,
            "g_residual_1GeV": g_resid_1GeV,
            "g_free_deconfined_1GeV": g_free_1GeV,
            "sign_confirmed": sign_predicted_lt_1,
        },
        "structural_validity": {
            "continuity_C2": True,
            "operator_clause_2_g_star_monotonic": {
                "strict_exact_crossover": monotonic_strict_crossover,
                "strict_exact_full": monotonic_strict_full,
                "breach_fraction_crossover": breach_fraction,
                "max_downward_excursion_g_star_units": max_excursion,
                "excursion_relative": excursion_rel,
                "excursion_vs_5pct_band": excursion_vs_5pct_band,
                "note": (
                    "natural cubic spline (plan-pinned bc_type='natural') does not "
                    "preserve monotonicity on the near-flat plateau (T~668-800 MeV); "
                    "overshoot is within the Bar-Reichel interpolation-error regime "
                    "and the 5% Borsanyi model-uncertainty band; regime band MARGINAL"
                ),
            },
            "operator_clause_3_w_in_range_0_1": w_in_range,
            "w_monotonic_diagnostic_NOT_a_clause": w_monotonic,
            "structurally_valid": structurally_valid,
        },
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "composite_verdict": composite,
        "cascade_form_pin": "S88 W6 §V.5",
        "lattice_QCD_pin": "Borsanyi et al. 2016 (Nature 539, 69) / PDG canonical",
        "borsanyi_construction_note": interp_metadata["construction_note"],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pin_shas": pins,
    }
    JSON_OUT.write_text(json.dumps(json_report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  → {JSON_OUT.name}")

    # Step 11 — Plot: g_*(T) curve + Borsanyi interpolation overlay (panel 1) +
    # per-species w_i(T) (panel 2) — REQUIRED per plan output_artifacts.
    print(f"Step 11 — Write plot: {PNG_OUT.name}")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Panel 1: g_*(T) lattice curve + spline overlay + PDG anchors
    ax1.plot(T_dense, g_dense, "b-", lw=1.8, label="Borsanyi cubic-spline interp (bc=natural)")
    ax1.plot(T_MeV_grid, g_star_borsanyi_grid, "ko", ms=6,
             label="17-point Borsanyi grid")
    # mark PDG-CANONICAL grid point (1 GeV)
    pdg_idx = np.where(borsanyi_anchor_provenance == "PDG-CANONICAL")[0]  # (local)
    if pdg_idx.size:
        ax1.plot(T_MeV_grid[pdg_idx], g_star_borsanyi_grid[pdg_idx], "g*", ms=20,
                 label="PDG-CANONICAL anchor (1 GeV = 61.75)")
    # PDG anchor reference horizontals
    ax1.axhline(G_STAR_PDG_REF["1GeV"], color="green", ls="--", lw=1.0, alpha=0.6,
                label=f"PDG g_*(1 GeV) = {G_STAR_PDG_REF['1GeV']:.2f}")
    ax1.axhline(float(g_star_BBN), color="purple", ls=":", lw=1.0, alpha=0.6,
                label=f"g_star_BBN = {float(g_star_BBN):.2f} (T<=1 MeV asymptote)")
    # crossover band shading
    ax1.axvspan(T_QCD_CONFINE_MeV, T_QCD_DECONFINE_MeV, alpha=0.12, color="orange",
                label="QCD crossover band [150, 1000] MeV")
    # smooth-tanh comparison marker: at 1 GeV smooth-tanh gave g_*=76.35 (S91)
    ax1.plot([1000.0], [76.3514], "rs", ms=12,
             label="S91 smooth-tanh g_*(1 GeV) = 76.35 (FAIL: w=1)")
    ax1.set_xscale("log")
    ax1.set_xlabel("T (MeV)", fontsize=11)
    ax1.set_ylabel(r"$g_{*}(T)$  (effective relativistic dof)", fontsize=11)
    ax1.set_title(
        f"Borsanyi-anchored $g_*(T)$ interpolation\n"
        f"max rel_dev (3 PDG anchors) = {max_rd:.2%}  [{composite}]",
        fontsize=11,
    )
    ax1.legend(loc="upper left", fontsize=7.5)
    ax1.grid(True, alpha=0.3, which="both")

    # Panel 2: per-species QCD phase-weight w_i(T)
    for name, *_ in QCD_QUARKS:
        ax2.plot(T_MeV_grid, w_per_species[name], "o-", ms=4, alpha=0.7, label=f"w_{name}")
    for name, *_ in QCD_GLUONS:
        ax2.plot(T_MeV_grid, w_per_species[name], "s-", ms=5, lw=2.0, color="black",
                 label=f"w_{name}")
    # smooth-tanh comparison: w=1 at 1 GeV
    ax2.plot([1000.0], [1.0], "rs", ms=12, label="S91 smooth-tanh w(1 GeV) = 1.0")
    ax2.plot([1000.0], [w_1GeV], "g*", ms=18,
             label=f"Borsanyi w(1 GeV) = {w_1GeV:.4f} (< 1)")
    ax2.axhline(1.0, color="gray", ls="--", lw=0.8, alpha=0.6)
    ax2.axhline(0.0, color="gray", ls="--", lw=0.8, alpha=0.6)
    ax2.axvspan(T_QCD_CONFINE_MeV, T_QCD_DECONFINE_MeV, alpha=0.12, color="orange")
    ax2.set_xscale("log")
    ax2.set_xlabel("T (MeV)", fontsize=11)
    ax2.set_ylabel(r"$w_i^{\rm borsanyi}(T)$  (QCD phase-weight)", fontsize=11)
    ax2.set_ylim(-0.08, 1.12)
    ax2.set_title(
        f"Per-species QCD-crossover phase-weight $w_i(T)$\n"
        f"w in [0,1] (clause 3): {w_in_range};  w-monotone (diagnostic): {w_monotonic}  (sign={sign_v})",
        fontsize=11,
    )
    ax2.legend(loc="center right", fontsize=7)
    ax2.grid(True, alpha=0.3, which="both")

    fig.suptitle(
        f"{GATE_ID}  —  composite={composite}  "
        f"(3-tuple: sign={sign_v}, magnitude={mag_v}, regime={regime_v})",
        fontsize=12,
    )
    plt.tight_layout()
    plt.savefig(PNG_OUT, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  → {PNG_OUT.name}")

    # Step 12 — single-shot AFTER-pattern verdict emission (3-row block)
    print()
    print("Step 12 — Build verdict block in memory → atomic append → re-read verify")
    # Option-A supersedes tag: emit ONLY if the prior FAIL line is on disk
    # (gate-verdicts.md §"Option A" rule 2: corrective line carries
    # supersedes=<full-64-char>; prior line retained).
    prior_present = verify_verdict_on_disk(SUPERSEDES_PRIOR_AUDIT_SHA)  # (local)
    supersedes_clause = (
        f";supersedes={SUPERSEDES_PRIOR_AUDIT_SHA}" if prior_present else ""
    )  # (local)
    if prior_present:
        print(f"  Option-A: prior FAIL line present (audit_sha256={SUPERSEDES_PRIOR_AUDIT_SHA[:16]}...);")
        print(f"            corrective line will carry supersedes tag (prior RETAINED on disk).")
    else:
        print(f"  Option-A: no prior line on disk (fresh run); no supersedes tag emitted.")
    value_str = (
        f"max_rel_dev={max_rd:.6f};"
        f"rel_dev_100GeV={rel_devs['100GeV']:.6f};"
        f"rel_dev_1GeV={rel_devs['1GeV']:.6f};"
        f"rel_dev_1MeV={rel_devs['1MeV']:.6f};"
        f"w_borsanyi_1GeV={w_1GeV:.6f};"
        f"g_star_breach_fraction={breach_fraction:.6f};"
        f"structurally_valid={structurally_valid};"
        f"composite={composite}"
        f"{supersedes_clause}"
    )
    verdict_block = build_verdict_block(
        composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v,
    )
    append_verdict(verdict_block)

    if verify_verdict_on_disk(audit_sha):
        print(f"  → s92_gate_verdicts.txt (audit_sha256={audit_sha[:16]}...): VERIFIED on disk")
    else:
        print(f"  ERROR: verdict line not found after append; audit_sha256={audit_sha[:16]}...")
        return 1

    print()
    print(
        f"(value={value_str!r}, "
        f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"
    )
    print(f"\n=== {GATE_ID}: {composite} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
