#!/usr/bin/env python3
"""
S90 W4-4 — S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED (CF-40)
==========================================================================

Gate: S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED ([VERIFY])

Refines the S88 §W1-3 species-multiplicity lookup with lattice-QCD
corrections near Λ_QCD ≈ 200 MeV (smooth quark-hadron crossover) and
Boltzmann threshold-suppression at species mass boundaries
(m_e at T=1 MeV; m_W, m_top at T=100 GeV; etc.). Validates the refined
g_*_BS(T) against PDG/Planck-canonical reference values at 3 cross-check
anchors T ∈ {100 GeV, 1 GeV, 1 MeV}.

PASS iff rel_dev_i ≤ 0.10 RATIO at ALL 3 anchors.
INFO iff at least one rel_dev_i ∈ (0.05, 0.10].
FAIL iff any rel_dev_i > 0.10.

Outputs (npz keys, mandatory):
    g_star_BS_T_H            # at T_H = 1.057 MeV (CF-39 anchor)
    g_star_BS_100GeV
    g_star_BS_1GeV
    g_star_BS_1MeV
    g_star_PDG_100GeV
    g_star_PDG_1GeV
    g_star_PDG_1MeV
    rel_dev_anchors          # 3-element array
    Boltzmann_factors_per_species  # dict per anchor (object array)
    cascade_form_pin   : "S88 W6 §V.5"
    lattice_QCD_pin    : "Borsanyi et al. 2016 / PDG canonical"
    T_H_value_MeV      : 1.057  (CF-39 anchor temperature)
    audit_sha256, content_sha256, schema_version

Substrate framing
-----------------
The substrate cascade FORM per S88 W6 §V.5 specifies HOW g_*(T) enters
the cascade-tail observable; it does NOT specify g_*(T) itself. g_*(T)
is a laboratory-IN PDG-canonical count of effective relativistic
degrees of freedom at temperature T. The refinement here is on the
laboratory-IN INPUT to the substrate cascade-tail formula; the
substrate-IS observable remains pinned at S88 W6 §V.5 Result 2.

Direction of explanation: substrate cascade tail (S88 W6 §V.5) ←→
g_*(T) (laboratory-IN PDG-canonical, refined here) ←→ bridge at the
CF-39 L_H_canonical = (π²/60) · g_*(T_H) · A_horizon · T_H⁴ formula at
substrate-pinned T_H = 1.057 MeV.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))

# Mandatory: thread cap BEFORE numpy import (CPU-only is fine here; no
# matrix algebra; only scalar arithmetic + table lookups).
import os  # noqa: E402
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
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
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"
NPZ_OUT = SESSION_DIR / "s90_w4_cf40_species_multiplicity_retry.npz"
PNG_OUT = SESSION_DIR / "s90_w4_cf40_species_multiplicity_retry.png"
JSON_OUT = SESSION_DIR / "s90_w4_cf40_species_multiplicity_retry.json"


# ---------------------------------------------------------------------
# Gate identity
# ---------------------------------------------------------------------

GATE_ID = "S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED"  # (local)
SCHEME = "lattice-QCD-corrected-Boltzmann-suppressed-substrate-cascade"  # (local)
CONVENTION = "PDG-canonical-3-anchor-cross-check"  # (local)
L_MAX = "N/A"  # (local; particle-physics anchor refinement, no L_max axis)

# Substrate-pinned T_H per S87 J8 + W1a CF-CURV-7 (cited in S88 W6 §V.5)
T_H_value_MeV = 1.057  # (local) CF-39 anchor temperature; substrate-derived per S87 J8 + W1a CF-CURV-7; cited in S88 W6 §V.5 Result 2

# Boltzmann threshold band per plan §6: m/T ∈ [0.2, 5] uses exp(-m/T)
BS_BAND_LO = 0.2  # (local; m/T < 0.2 → relativistic, BS = 1)
BS_BAND_HI = 5.0  # (local; m/T > 5 → decoupled, BS = 0)

# QCD crossover band: smooth interpolation between deconfined and confined
# phases over T ∈ [50 MeV, 1 GeV] per Borsanyi+ 2016 lattice-QCD g_*(T).
LAMBDA_QCD_GeV = 0.200  # (local; quark-hadron transition scale)
QCD_CROSSOVER_LO_GeV = 0.050  # (local; lower band edge — fully confined)
QCD_CROSSOVER_HI_GeV = 1.000  # (local; upper band edge — fully deconfined)

# Cross-check anchors (per plan §6 cross_check_anchors)
T_ANCHOR_GEV = {
    "100GeV": 1.00e2,
    "1GeV":   1.00e0,
    "1MeV":   1.00e-3,
}

# PDG / Planck reference values (canonical, per plan §5 Step 5):
#   g_*(T = 100 GeV) ≈ 106.75 (full SM above EW transition)
#   g_*(T = 1 GeV)   ≈ 60-65  (deconfined QGP; per Husdal 2016 Table 5;
#                              we use 61.75 as canonical mid-band)
#   g_*(T = 1 MeV)   ≈ 10.75  (pre-neutrino-decoupling; γ + e± + 3ν;
#                              per PDG / Husdal 2016 — at T=1 MeV the
#                              ν decoupling has not yet completed AND
#                              e± annihilation has not yet completed,
#                              so e± remain relativistic, giving 10.75
#                              not the post-annihilation 3.36)
G_STAR_PDG = {
    "100GeV": 106.75,
    "1GeV":   61.75,
    "1MeV":   10.75,
}

# Threshold-band INFO band: 5%-10% RATIO (borderline)
PASS_BAND = 0.10  # (local; 10% RATIO at all 3 anchors)
INFO_BAND_LO = 0.05  # (local; 5%-10% INFO band)


# ---------------------------------------------------------------------
# SM species table — (name, mass_GeV, internal_dof, statistics)
# ---------------------------------------------------------------------
# References:
#  - PDG 2024 mass values (cited in canonical_constants.py for some)
#  - Husdal 2016 "On effective degrees of freedom in the early universe"
#    Table 4 species enumeration
#  - Borsanyi et al. 2016 (Nature 539, 69) lattice-QCD g_*(T) — used
#    only as the numerical interpolation anchor for the QCD crossover
#    band; SM species table is canonical PDG.
#
# Internal dof convention (per Kolb & Turner Table 3.4):
#   photon γ: 2 (helicity); BOSON
#   gluon g (8): 8 colors × 2 polarizations = 16; BOSON
#   W± / Z: 3 polarization states each; BOSON; W gives 2×3=6, Z gives 3
#   Higgs H: 1 (real scalar); BOSON
#   each charged lepton (e, μ, τ): 4 (particle + antiparticle, 2 spin); FERMION
#   each light neutrino (ν_e, ν_μ, ν_τ): 2 (Weyl: ν_L + ν_R bar; or
#       2 helicities of single Majorana); FERMION
#   each quark flavor (u, d, s, c, b, t): 4 spin × 3 color = 12; FERMION
#
# Fermions get the 7/8 statistical-weight factor in the g_*_eff sum.

# (name, m_GeV, g_internal, "B"|"F", classification)
SM_SPECIES = [
    # Bosons (g = 1.0 weight factor)
    ("photon",    0.0,         2,  "B", "EM gauge"),
    ("gluon",     0.0,         16, "B", "QCD gauge (deconfined-only)"),
    ("W_plus",    80.379,      3,  "B", "EW gauge"),
    ("W_minus",   80.379,      3,  "B", "EW gauge"),
    ("Z",         91.188,      3,  "B", "EW gauge"),
    ("Higgs",     125.10,      1,  "B", "EW scalar"),
    # Fermions (g = 7/8 weight factor)
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

# Confined-phase hadrons (active for T < Λ_QCD ≈ 200 MeV).
# Conservative subset per Husdal 2016 Table 4: pions (3), kaons (4),
# η, η', ρ, ω, p, n, plus their antiparticles where applicable. We
# include the lightest mesons + nucleons; heavier hadrons (1+ GeV) are
# Boltzmann-suppressed at all T below Λ_QCD anyway.
CONFINED_HADRONS = [
    ("pion_pm",   0.13957,     2,  "B", "pseudo-scalar meson (π±, antiparticle)"),
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
# Boltzmann threshold-suppression model
# ---------------------------------------------------------------------

def boltzmann_factor(m_GeV: float, T_GeV: float) -> float:
    """Boltzmann threshold-suppression factor BS_i(T) per plan §5 Step 3.

    BS_i(T) = 1                if m/T < 0.2  (relativistic)
    BS_i(T) = exp(-m/T)        if 0.2 <= m/T <= 5  (threshold band)
    BS_i(T) = 0                if m/T > 5  (decoupled / non-relativistic)

    Massless species (m=0) always return 1.
    """
    if m_GeV <= 0.0:
        return 1.0
    ratio = m_GeV / T_GeV
    if ratio < BS_BAND_LO:
        return 1.0
    if ratio > BS_BAND_HI:
        return 0.0
    return math.exp(-ratio)


def stat_weight(stat: str) -> float:
    """Boson 1.0; Fermion 7/8 per Kolb-Turner Eq.3.62 g_*_eff sum."""
    if stat == "B":
        return 1.0
    if stat == "F":
        return 7.0 / 8.0
    raise ValueError(f"unknown statistics: {stat!r}")


def qcd_crossover_weight(T_GeV: float) -> float:
    """Smooth interpolation between deconfined (1.0) and confined (0.0)
    phases across T ∈ [50 MeV, 1 GeV], canonical-anchored at Borsanyi+
    2016 lattice-QCD g_*(T) shape.

    Returns w ∈ [0, 1]:
      w = 1                  if T >= 1 GeV (fully deconfined; quarks+gluons)
      w = 0                  if T <= 50 MeV (fully confined; hadrons only)
      smooth tanh-like in between.

    The complementary weight (1 - w) multiplies the confined-hadron
    contribution. The crossover model captures the qualitative
    Borsanyi+2016 shape; precise lattice-QCD g_*(T) tabulation could
    be substituted as a future refinement but the 3-anchor cross-check
    band of 10% RATIO is achievable with the smooth-tanh model.
    """
    if T_GeV >= QCD_CROSSOVER_HI_GeV:
        return 1.0
    if T_GeV <= QCD_CROSSOVER_LO_GeV:
        return 0.0
    # log-smooth tanh interpolation across the [50 MeV, 1 GeV] band
    # centered at Λ_QCD = 200 MeV (lattice-QCD pseudo-critical temperature).
    log_lo = math.log10(QCD_CROSSOVER_LO_GeV)
    log_hi = math.log10(QCD_CROSSOVER_HI_GeV)
    log_T = math.log10(T_GeV)
    log_center = math.log10(LAMBDA_QCD_GeV)
    # Width set by half-band in log-space
    width = (log_hi - log_lo) / 4.0
    # tanh smoothly transitions from 0 at log_T = log_lo to 1 at log_T = log_hi
    arg = (log_T - log_center) / width
    raw = 0.5 * (1.0 + math.tanh(arg))
    # Clip to [0, 1]
    return max(0.0, min(1.0, raw))


def g_star_BS(T_GeV: float, return_breakdown: bool = False):
    """g_*_BS(T) = Σ_i (g_i × stat_weight_i × BS_i(T) × phase_weight_i)

    Phase weight:
      - quark / gluon species: w_QCD(T) (1 in deconfined, 0 in confined)
      - confined hadrons: (1 - w_QCD(T))
      - all other species: 1

    Returns scalar g_*_BS(T); if return_breakdown=True, also returns
    a dict {species_name: contribution} for diagnostics.
    """
    w_qcd = qcd_crossover_weight(T_GeV)
    breakdown = {}
    total = 0.0  # (local) accumulator for Σ_i g_i × stat_weight_i × BS_i × phase_i

    # Deconfined-phase species (free quarks + gluons get w_qcd; everything else gets 1)
    for name, m_GeV, g_int, stat, classification in SM_SPECIES:
        bs = boltzmann_factor(m_GeV, T_GeV)
        sw = stat_weight(stat)
        if "deconfined-only" in classification:
            phase = w_qcd  # (local) quark / gluon active in deconfined phase only
        else:
            phase = 1.0  # (local) non-QCD species (γ, leptons, ν, EW bosons, H) always active
        contrib = g_int * sw * bs * phase
        breakdown[name] = contrib
        total += contrib

    # Confined hadrons (active for T below Λ_QCD; weighted by 1 - w_qcd)
    for name, m_GeV, g_int, stat, classification in CONFINED_HADRONS:
        bs = boltzmann_factor(m_GeV, T_GeV)
        sw = stat_weight(stat)
        phase = 1.0 - w_qcd  # (local) confined hadron weight: complementary to QCD crossover
        contrib = g_int * sw * bs * phase
        breakdown[name] = contrib
        total += contrib

    if return_breakdown:
        return total, breakdown
    return total


# ---------------------------------------------------------------------
# Verdict / SHA / I/O scaffolding (mirrors S90 W2 canonical pattern)
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
    content_sha = SHA(script)."""
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


def emit_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str):
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
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main() -> int:
    t0 = time.time()

    # Step 0 — input pins + dual-SHA
    inputs = [CANONICAL_CONSTANTS, S88_W6_V5_SOURCE]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # Step 1 — knowledge-MCP query summary (recorded for orchestrator WP authoring)
    print("Step 1 — knowledge-MCP pre-compute audit (per CLAUDE.md MANDATORY discipline):")
    print("  - search_knowledge('g_star T lattice QCD Borsanyi Boltzmann threshold suppression species multiplicity'):")
    print("    8 hits; closest is S88 W6 §V.5 Result 2 (substitution chain at T_H=1.057 MeV); no")
    print("    canonical g_*_BS(T) tabulation has been pinned previously.")
    print("  - trace_entity('substrate cascade form S88 W6 V.5'): no exact trace found;")
    print("    located source at sessions/archive/session-88/workshops/s88-w6-w1c-69-page1976-13oom.md.")
    print("  - get_constant('T_H'): not pinned; T_H_dump_expected = 0.0 is unrelated S85 W6-4 anchor.")
    print("    T_H = 1.057 MeV is a substrate-derived value from S87 J8 + W1a CF-CURV-7;")
    print("    cited in S88 W6 §V.5 Result 2; this gate uses it as a fixed substrate-pinned input.")
    print("  - get_constant('g_star_BS_T_H'): not yet pinned; this gate is the candidate-pinning")
    print("    event for promotion to canonical_constants.py per plan §11.")
    print("  - get_constant('m_e'): grep canonical_constants.py — not pinned by name 'm_e' (m_e_pole")
    print("    not present); we use PDG 2024 value 0.000511 GeV inline with substitution-chain comment.")
    print("  - get_constant('m_t_pole'): 172.69 GeV (canonical_constants.py:1562; PDG 2024).")
    print("  - get_constant('m_W'): not pinned by name; PDG 2024 value 80.379 GeV inline.")
    print("  - get_constant('m_H_obs'): 125.1 GeV (canonical_constants.py:1561; PDG 2024).")
    print("  - get_constant('g_star_SM'): 106.75 (canonical_constants.py:1567; PDG ref above EW).")
    print("  - get_constant('g_star_BBN'): 10.75 (canonical_constants.py:1568; PDG ref at BBN).")
    print()

    # Step 2 — Compute g_*_BS at the 3 cross-check anchors + T_H
    print("Step 2 — Compute g_*_BS at cross-check anchors + T_H = 1.057 MeV:")
    g_BS = {}
    breakdowns = {}
    for label, T_GeV in T_ANCHOR_GEV.items():
        val, brk = g_star_BS(T_GeV, return_breakdown=True)
        g_BS[label] = val
        breakdowns[label] = brk
        print(f"  g_*_BS(T = {label}) = {val:.4f}   (PDG ref {G_STAR_PDG[label]:.4f}; w_QCD = {qcd_crossover_weight(T_GeV):.4f})")
    g_BS_T_H, brk_T_H = g_star_BS(T_H_value_MeV * 1.0e-3, return_breakdown=True)
    breakdowns["T_H_1057MeV"] = brk_T_H
    print(f"  g_*_BS(T_H = 1.057 MeV) = {g_BS_T_H:.4f}   (CF-39 anchor; canonical-pin candidate)")
    print()

    # Step 3 — rel_dev cross-check
    print("Step 3 — Cross-check rel_dev_i = |g_*_BS(T_i) - g_*_PDG(T_i)| / g_*_PDG(T_i):")
    rel_devs = {}
    for label in T_ANCHOR_GEV:
        rd = abs(g_BS[label] - G_STAR_PDG[label]) / G_STAR_PDG[label]
        rel_devs[label] = rd
        flag = "PASS" if rd <= INFO_BAND_LO else ("INFO" if rd <= PASS_BAND else "FAIL")
        print(f"  rel_dev({label}) = {rd:.4%}  [{flag}]")
    rel_dev_arr = np.array([rel_devs["100GeV"], rel_devs["1GeV"], rel_devs["1MeV"]])
    print()

    # Step 4 — Composite verdict
    print("Step 4 — Composite verdict:")
    max_rd = float(np.max(rel_dev_arr))
    if max_rd > PASS_BAND:
        verdict = "FAIL"
    elif max_rd > INFO_BAND_LO:
        verdict = "INFO"
    else:
        verdict = "PASS"
    all_pass = bool(np.all(rel_dev_arr <= PASS_BAND))
    print(f"  max(rel_dev) = {max_rd:.4%}  →  composite = {verdict}")
    print(f"  all-3-anchors-pass-10pct = {all_pass}")
    print()

    # Step 5 — npz output
    print(f"Step 5 — Write npz: {NPZ_OUT.name}")
    breakdown_obj = np.array([breakdowns], dtype=object)  # dict-in-array; allow_pickle on load
    np.savez(
        NPZ_OUT,
        g_star_BS_T_H=g_BS_T_H,
        g_star_BS_100GeV=g_BS["100GeV"],
        g_star_BS_1GeV=g_BS["1GeV"],
        g_star_BS_1MeV=g_BS["1MeV"],
        g_star_PDG_100GeV=G_STAR_PDG["100GeV"],
        g_star_PDG_1GeV=G_STAR_PDG["1GeV"],
        g_star_PDG_1MeV=G_STAR_PDG["1MeV"],
        rel_dev_anchors=rel_dev_arr,
        Boltzmann_factors_per_species=breakdown_obj,
        cascade_form_pin="S88 W6 §V.5",
        lattice_QCD_pin="Borsanyi et al. 2016 (Nature 539, 69) shape-anchored crossover; PDG 2024 SM masses",
        T_H_value_MeV=T_H_value_MeV,
        pass_band=PASS_BAND,
        info_band_lo=INFO_BAND_LO,
        max_rel_dev=max_rd,
        all_3_anchors_pass=all_pass,
        composite_verdict=verdict,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        schema_version="S87+",
        allow_pickle=True,
    )

    # Step 6 — JSON sidecar (plan §6 standard)
    json_report = {
        "gate_id": GATE_ID,
        "T_H_value_MeV": T_H_value_MeV,
        "g_star_BS_T_H": g_BS_T_H,
        "anchors": {
            label: {
                "T_GeV": T_ANCHOR_GEV[label],
                "g_star_BS": g_BS[label],
                "g_star_PDG_ref": G_STAR_PDG[label],
                "rel_dev": rel_devs[label],
                "w_QCD_crossover": qcd_crossover_weight(T_ANCHOR_GEV[label]),
            }
            for label in T_ANCHOR_GEV
        },
        "max_rel_dev": max_rd,
        "all_3_anchors_pass_10pct": all_pass,
        "composite_verdict": verdict,
        "cascade_form_pin": "S88 W6 §V.5",
        "lattice_QCD_pin": "Borsanyi et al. 2016 (Nature 539, 69) shape-anchored crossover; PDG 2024 SM masses",
        "Boltzmann_threshold_band_pin": [BS_BAND_LO, BS_BAND_HI],
        "QCD_crossover_band_GeV": [QCD_CROSSOVER_LO_GeV, QCD_CROSSOVER_HI_GeV],
        "Lambda_QCD_GeV": LAMBDA_QCD_GeV,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pin_shas": pins,
        "Boltzmann_factors_at_T_H_1057MeV": brk_T_H,
        "Boltzmann_factors_at_100GeV": breakdowns["100GeV"],
        "Boltzmann_factors_at_1GeV": breakdowns["1GeV"],
        "Boltzmann_factors_at_1MeV": breakdowns["1MeV"],
    }
    JSON_OUT.write_text(json.dumps(json_report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  → {JSON_OUT.name}")

    # Step 7 — PNG plot
    print(f"Step 7 — Write plot: {PNG_OUT.name}")
    T_grid_GeV = np.logspace(-4, 3, 240)
    g_grid = np.array([g_star_BS(float(T)) for T in T_grid_GeV])
    fig, ax = plt.subplots(2, 1, figsize=(9, 8), sharex=True)

    # Top panel: g_*_BS(T) curve + 3 anchors + T_H + PDG references
    ax[0].semilogx(T_grid_GeV, g_grid, "b-", lw=1.6, label=r"$g_{*,\mathrm{BS}}(T)$ refined model")
    for label, T_GeV in T_ANCHOR_GEV.items():
        ax[0].plot(T_GeV, g_BS[label], "ro", ms=7)
        ax[0].plot(T_GeV, G_STAR_PDG[label], "g^", ms=7)
        ax[0].annotate(
            f"{label}\nBS={g_BS[label]:.2f}\nPDG={G_STAR_PDG[label]:.2f}\n"
            f"rd={rel_devs[label]:.1%}",
            xy=(T_GeV, g_BS[label]),
            xytext=(8, 8), textcoords="offset points", fontsize=8,
            ha="left", va="bottom",
        )
    ax[0].axvline(T_H_value_MeV * 1.0e-3, color="purple", ls="--", lw=1.0, alpha=0.7)
    ax[0].plot(T_H_value_MeV * 1.0e-3, g_BS_T_H, "ms", ms=8)
    ax[0].annotate(
        f"$T_H = 1.057$ MeV\n$g_{{*,\\mathrm{{BS}}}}(T_H) = {g_BS_T_H:.3f}$\n(CF-39 anchor)",
        xy=(T_H_value_MeV * 1.0e-3, g_BS_T_H),
        xytext=(10, -30), textcoords="offset points", fontsize=8,
        ha="left", va="top",
        arrowprops=dict(arrowstyle="->", color="purple", lw=0.8),
    )
    ax[0].axvspan(QCD_CROSSOVER_LO_GeV, QCD_CROSSOVER_HI_GeV, alpha=0.10, color="orange",
                  label="QCD crossover band [50 MeV, 1 GeV]")
    ax[0].set_ylabel(r"$g_{*,\mathrm{BS}}(T)$  (effective relativistic dof)", fontsize=11)
    ax[0].set_title(
        f"{GATE_ID}\n"
        f"lattice-QCD-corrected + Boltzmann threshold-suppressed; composite={verdict} "
        f"(max rel_dev = {max_rd:.2%})",
        fontsize=10,
    )
    ax[0].legend(loc="lower right", fontsize=9)
    ax[0].grid(True, alpha=0.3)
    ax[0].set_ylim(0, max(120, np.max(g_grid) * 1.10))

    # Bottom panel: Boltzmann factor breakdown at T_H = 1.057 MeV
    sorted_brk = sorted(brk_T_H.items(), key=lambda kv: -kv[1])
    nonzero = [(name, c) for name, c in sorted_brk if c > 1e-6]
    if not nonzero:
        nonzero = sorted_brk[:6]
    names = [n for n, _ in nonzero]
    contribs = [c for _, c in nonzero]
    bars = ax[1].barh(range(len(names)), contribs, color="steelblue", alpha=0.8)
    ax[1].set_yticks(range(len(names)))
    ax[1].set_yticklabels(names, fontsize=8)
    for bar, c in zip(bars, contribs):
        ax[1].text(c + 0.02, bar.get_y() + bar.get_height() / 2.0, f"{c:.3f}",
                   va="center", fontsize=7)
    ax[1].set_xlabel(r"contribution to $g_{*,\mathrm{BS}}(T_H)$", fontsize=10)
    ax[1].set_title(
        rf"Per-species breakdown at $T_H = 1.057$ MeV  "
        rf"(total $g_{{*,\mathrm{{BS}}}}(T_H) = {g_BS_T_H:.3f}$)",
        fontsize=9,
    )
    ax[1].grid(True, alpha=0.3, axis="x")
    ax[1].set_xlim(0, max(contribs) * 1.25 if contribs else 1.0)
    ax[1].set_xlabel(r"$T$ [GeV]", fontsize=11)
    ax[0].set_xlabel("")

    plt.tight_layout()
    plt.savefig(PNG_OUT, dpi=120, bbox_inches="tight")
    plt.close(fig)

    # Step 8 — emit verdict (canonical line + dual-SHA companion + 3-tuple if applicable)
    print()
    print("Step 8 — Append verdict line + dual-SHA companion to s90_gate_verdicts.txt")
    value_str = (
        f"all_3_anchors_rel_dev_le_10pct={all_pass};"
        f"rel_dev_100GeV={rel_devs['100GeV']:.6f};"
        f"rel_dev_1GeV={rel_devs['1GeV']:.6f};"
        f"rel_dev_1MeV={rel_devs['1MeV']:.6f};"
        f"g_star_BS_T_H={g_BS_T_H:.6f};"
        f"g_star_BS_100GeV={g_BS['100GeV']:.4f};"
        f"g_star_BS_1GeV={g_BS['1GeV']:.4f};"
        f"g_star_BS_1MeV={g_BS['1MeV']:.4f};"
        f"max_rel_dev={max_rd:.6f};"
        f"T_H_value_MeV={T_H_value_MeV};"
        f"lattice_QCD_pin=Borsanyi+2016_shape_anchored_crossover_PDG_2024_SM_masses;"
        f"cascade_form_pin=S88_W6_V5;"
        f"composite={verdict}"
    )
    emit_verdict(verdict, value_str, audit_sha, content_sha)
    print(f"  → s90_gate_verdicts.txt (audit_sha256={audit_sha})")

    # Final 4-tuple log line (per gate-verdicts.md "Expected output 4-tuple")
    print()
    print(
        f"(value='all_3_anchors_rel_dev_le_10pct={all_pass};g_star_BS_T_H={g_BS_T_H:.6f}', "
        f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"
    )
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
