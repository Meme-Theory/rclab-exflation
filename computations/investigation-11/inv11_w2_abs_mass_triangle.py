#!/usr/bin/env python3
"""
INV11 W2-2 — INV11-W2-2-ABS-MASS-TRIANGLE
=========================================

Gate: INV11-W2-2-ABS-MASS-TRIANGLE ([VERIFY])

Three-channel absolute-mass triangle from ONE input set. The single
oscillation-anchored light-mass triple (S99-W3 type-I seesaw, normal ordering)
m_nu = [0, 0.0086776, 0.0495278] eV is propagated to the three absolute-mass
DETECTOR CLASSES and tested for mutual consistency:

  (i)   Sigma m_nu = m_1 + m_2 + m_3        [cosmological; DESI Row #77]
  (ii)  m_beta   = sqrt( Sum |U_ei|^2 m_i^2 ) [kinematic endpoint; KATRIN / Project-8]
  (iii) m_betabeta = | Sum U_ei^2 m_i |       [0nubb; LEGEND Row #80]

The three are three DISTINCT contractions of the SAME m-triple with the
(measured, laboratory-IN) PMNS electron row:
  - Sigma  : bare L1 sum                                  (cosmological free-streaming)
  - m_beta : incoherent |U_ei|^2-weighted RMS            (sum of |amplitude|^2)
  - m_bb   : coherent U_ei^2 sum, COMPLEX U_ei^2          (rate ~ |amplitude|^2 => phases interfere)

With the J-forced Majorana phases delta_CP in {0, pi} (S99-W3 / [J,D_K]=0, T11) the two
non-trivial Majorana phases collapse to sign choices, so m_bb sweeps the band
[ |t_2 - t_3|, t_2 + t_3 ] with t_i = |U_ei|^2 * m_i (t_1 = 0 since m_1 = 0 EXACT,
normal ordering / MAP-B Casimir grading C_2(0,0)=0, S100a). The central (no-cancellation,
delta_CP=0 ≡ pi) IS the upper funnel edge.

Pre-registered threshold (plan §W2-2):
  PASS iff ALL of:
    |Sigma_computed - Sigma_mnu_FW| / Sigma_mnu_FW <= 1e-6          (reproduce canonical Sigma)
    Sigma_computed < 0.072 eV (DESI Row #77)                        (cosmological bound)
    m_betabeta in [1.516, 3.695] meV (LEGEND Row #80 sign-ambiguity band)
    m_beta in [0.0085, 0.0095] eV (the ~0.009 eV kinematic non-detection anchor band)
  FAIL iff a channel falls out of band.
  INFO iff m_betabeta only marginally inside the Row #80 band OR m_beta at the
       [0.0085, 0.0095] edge (consistency holds, with a phase/sign-branch caveat).

CANONICAL-SOURCING NOTE (substrate-first-canonical-sourcing.md §(iv), PIN-DISAMBIGUATION):
  The plan §W2-2 substitution chain labels its PMNS pins "NuFit-6.0" with
  sin2_theta12=0.303, sin2_theta13=0.02225. The canonical_constants.py provenance
  (lines 699-702, S101 PAIR-OF-PAIRS version-disambiguation) records that the value the
  Row #80 m_bb_FW gate ACTUALLY CONSUMED is sin2_theta12_PDG=0.307,
  sin2_theta13_PDG=0.0220 (the plan's "NuFit-6.0" label is de-facto NuFit-5.x/PDG
  central). To reproduce the CANONICAL Row #80 band [1.516, 3.695] meV bit-consistently,
  the PDG pair is the PRIMARY here; the TRUE NuFit-6.0 pair (0.303, 0.02225) is carried
  as a DIAGNOSTIC cross-check (Row #80 records the PDG->NuFit60 m_bb shift as -0.60%,
  DECISION-IRRELEVANT — both land inside the funnel band). This honors the canonical
  anchor over the plan's mislabeled prose.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py (feeds audit_sha256; supplies Sigma_mnu_FW, DESI bound,
    m_bb_FW, sin2_theta1x_{PDG,NuFit60})
  - computations/session-99/s99_w3_seesaw_summnu.npz (the canonical m_nu triple)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<triangle summary>, scheme=seesaw-anchored-triple, convention=ABSOLUTE, L_max=N/A)

Classification: PARTICLE — the light-mass triple is the seesaw image of the singlet-tower
bottoms (S52/S60/S99); the three observables are representation-theoretic contractions of
D_K's neutrino sector with the measured PMNS.

DISCIPLINE
----------
- from canonical_constants import *; every intermediate tagged # (local)
- CROSS-TRACK CAVEAT: no canonical_constants.py pin / registry row / inventory row is
  written by this script. INVESTIGATION-TRACK ONLY (writes computations/investigation-11/
  + WP §W2-2). Any falsifier-inventory landing is session-promotion + mack sole-writer.
- closed-form 3x3 PMNS contractions; trivially CPU (numpy). No GPU needed.
- dual-SHA (audit_sha256 + content_sha256) emitted; 4-tuple final non-verdict line.
- verdict via print_verdict_payload (agent calls emit_verdict, session=11,
  track="investigation"); the script does NOT write the verdict file.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# canonical_constants.py lives in computations/_shared; put it on the path BEFORE import.
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parent.parent / "_shared"  # (local)
sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json     # noqa: E402
import time     # noqa: E402

import numpy as np  # noqa: E402
import matplotlib   # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent          # computations/investigation-11
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "INV11"                                                  # (local)
GATE_ID = "INV11-W2-2-ABS-MASS-TRIANGLE"                           # (local)
SCHEME = "seesaw-anchored-triple"                                  # (local)
CONVENTION = "ABSOLUTE"                                            # (local)
L_MAX = "N/A"                                                      # (local)

# Pre-registered pass/fail thresholds (plan §W2-2 strict_PASS_boundary)
SIGMA_RELDIFF_TOL = 1e-6                                           # (local) reldiff vs canonical Sigma
MBB_BAND_LO_MEV = 1.516                                            # (local) LEGEND Row #80 band lower [meV] (4 sf)
MBB_BAND_HI_MEV = 3.695                                            # (local) LEGEND Row #80 band upper [meV] (4 sf)
# Row #80 band edges are PUBLISHED at 4 significant figures (m_bb_FW publication_precision=4).
# Per epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3)" item 2, any
# membership/verifier test against a 4-sf edge MUST carry rel_tol >= 10^(-4); a tighter (hard <=)
# comparison is structurally guaranteed to FAIL on the precision floor, NOT on physics. The m_bb
# central IS the no-cancellation upper edge by construction (Row #80), so it lands ON the upper
# edge (reldiff 0.0 vs full-precision m_bb_FW). The band-membership operator below uses this
# Class-8.3 edge tolerance; the central-on-edge case is the pre-registered INFO outcome (the plan
# INFO_meaning: "m_betabeta only marginally inside the Row #80 band ... straddles an edge").
MBB_BAND_RELTOL = 1e-4                                            # (local) Class-8.3: edges published 4 sf
MBETA_BAND_LO = 0.0085                                            # (local) m_beta anchor band lower [eV]
MBETA_BAND_HI = 0.0095                                            # (local) m_beta anchor band upper [eV]
# INFO-band tolerances (marginal-edge detection)
MBB_EDGE_FRAC = 0.01                                              # (local) within 1% of a band edge => marginal
MBETA_EDGE = 0.0001                                              # (local) within this of m_beta band edge => marginal

# Output destinations (investigation-track)
OUT_NPZ = SESSION_DIR / "inv11_w2_abs_mass_triangle.npz"
OUT_PNG = SESSION_DIR / "inv11_w2_abs_mass_triangle.png"

# S99-W3 canonical seesaw output (the input m_nu triple)
S99_SEESAW_NPZ = Path("computations/session-99/s99_w3_seesaw_summnu.npz")

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    PROJECT_ROOT / S99_SEESAW_NPZ,
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


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
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
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
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
# Section 5 — Compute
# ---------------------------------------------------------------------------

def channel_contractions(m, s12, s13):
    """Three detector observables from the m-triple + PMNS electron row.

    m    : array([m1, m2, m3]) light masses [eV]
    s12  : sin^2(theta_12)
    s13  : sin^2(theta_13)
    Returns (Sigma, m_beta, mbb_upper, mbb_lower, Ue2) where mbb band edges are the
    J-forced delta_CP in {0,pi} resultant magnitudes.
    """
    c12 = 1.0 - s12                                   # (local) cos^2 th12
    c13 = 1.0 - s13                                   # (local) cos^2 th13
    Ue1_2 = c12 * c13                                 # (local) |U_e1|^2
    Ue2_2 = s12 * c13                                 # (local) |U_e2|^2
    Ue3_2 = s13                                       # (local) |U_e3|^2
    Ue2 = np.array([Ue1_2, Ue2_2, Ue3_2])            # (local) electron-row |U_ei|^2

    Sigma = float(np.sum(m))                          # (local) bare L1 sum
    # m_beta = sqrt( sum |U_ei|^2 m_i^2 )  (incoherent endpoint)
    m_beta = float(np.sqrt(np.sum(Ue2 * m**2)))       # (local)
    # m_betabeta band: t_i = |U_ei|^2 m_i (real magnitudes; t_1 = 0 since m_1 = 0).
    # With delta_CP in {0,pi}, resultant = | t_2 +/- t_3 | => [ |t2-t3|, t2+t3 ].
    t = Ue2 * m                                       # (local) per-mass magnitudes
    t2 = t[1]                                          # (local)
    t3 = t[2]                                          # (local)
    mbb_upper = float(t2 + t3)                         # (local) constructive (delta_CP=0)
    mbb_lower = float(abs(t2 - t3))                    # (local) maximal Majorana cancellation
    return Sigma, m_beta, mbb_upper, mbb_lower, Ue2


def compute() -> dict:
    # ---- Input set: the canonical S99-W3 light triple (load from npz) ----
    d = np.load(PROJECT_ROOT / S99_SEESAW_NPZ, allow_pickle=True)  # (local)
    m_nu = np.asarray(d["m_nu_eV"], dtype=float)                    # (local) [0, 0.0086776, 0.0495278]
    Sigma_npz = float(d["Sigma_mnu_eV"])                           # (local) 0.0582053272...
    crosscheck_reldiff_npz = float(d["Sigma_mnu_crosscheck_reldiff"])  # (local) 1.16e-5
    delta_CP_allowed = np.asarray(d["delta_CP_allowed"], dtype=float)  # (local) [0, pi]

    # ---- PRIMARY: PDG PMNS pair (the value Row #80 / m_bb_FW gate CONSUMED) ----
    s12_pdg = float(sin2_theta12_PDG)                              # (local) 0.307
    s13_pdg = float(sin2_theta13_PDG)                              # (local) 0.0220
    (Sigma_pdg, mbeta_pdg, mbb_up_pdg, mbb_lo_pdg,
     Ue2_pdg) = channel_contractions(m_nu, s12_pdg, s13_pdg)

    # ---- DIAGNOSTIC: TRUE NuFit-6.0 PMNS pair (plan-label literal) ----
    s12_nf = float(sin2_theta12_NuFit60)                          # (local) 0.303
    s13_nf = float(sin2_theta13_NuFit60)                          # (local) 0.02225
    (Sigma_nf, mbeta_nf, mbb_up_nf, mbb_lo_nf,
     Ue2_nf) = channel_contractions(m_nu, s12_nf, s13_nf)

    # ---- Channel (i): Sigma consistency vs canonical ----
    Sigma = Sigma_pdg                                             # (local) Sigma is PMNS-independent
    sigma_reldiff = abs(Sigma - float(Sigma_mnu_FW)) / float(Sigma_mnu_FW)  # (local)
    sigma_below_desi = Sigma < float(Sigma_mnu_bound_DESI_2024)   # (local)

    # ---- Channel (iii): m_bb central reproduction vs canonical m_bb_FW ----
    mbb_central_canonical = float(m_bb_FW) * 1000.0               # (local) meV
    mbb_central_pdg = mbb_up_pdg * 1000.0                         # (local) meV (no-cancel upper = central)
    mbb_central_reldiff = abs(mbb_central_pdg - mbb_central_canonical) / mbb_central_canonical  # (local)
    # band edges in meV (PRIMARY = PDG)
    mbb_lo_pdg_meV = mbb_lo_pdg * 1000.0                          # (local)
    mbb_hi_pdg_meV = mbb_up_pdg * 1000.0                          # (local)
    # NuFit-6.0 diagnostic shift on the central
    mbb_central_nf = mbb_up_nf * 1000.0                           # (local) meV
    mbb_pdg_to_nf_shift = (mbb_central_nf - mbb_central_pdg) / mbb_central_pdg  # (local) signed

    # ---- Band-membership gates (PRIMARY = PDG) ----
    # Class-8.3 precision-aware band: the edges are published at 4 sf, so widen each edge by
    # MBB_BAND_RELTOL (1e-4) before the membership test. Without this, the central (= the
    # full-precision upper edge by construction) fails a hard <= against the rounded 3.695 by
    # +3.5e-6 relative — a publication-precision-floor artifact, NOT a physics failure.
    band_lo_eff = MBB_BAND_LO_MEV * (1.0 - MBB_BAND_RELTOL)       # (local) widened lower edge
    band_hi_eff = MBB_BAND_HI_MEV * (1.0 + MBB_BAND_RELTOL)       # (local) widened upper edge
    mbb_in_band = (band_lo_eff <= mbb_central_pdg <= band_hi_eff)  # (local)
    # PDG band edges reproduce the Row #80 band edges?
    mbb_band_lo_reldiff = abs(mbb_lo_pdg_meV - MBB_BAND_LO_MEV) / MBB_BAND_LO_MEV  # (local)
    mbb_band_hi_reldiff = abs(mbb_hi_pdg_meV - MBB_BAND_HI_MEV) / MBB_BAND_HI_MEV  # (local)
    # m_bb central marginal? (within MBB_EDGE_FRAC of an edge — the central IS the upper edge,
    # so this fires TRUE => the pre-registered INFO outcome for "straddles an edge").
    mbb_marginal = (
        abs(mbb_central_pdg - MBB_BAND_LO_MEV) / MBB_BAND_LO_MEV < MBB_EDGE_FRAC
        or abs(mbb_central_pdg - MBB_BAND_HI_MEV) / MBB_BAND_HI_MEV < MBB_EDGE_FRAC
    )  # (local)

    # ---- m_beta band membership (PRIMARY = PDG) ----
    m_beta = mbeta_pdg                                            # (local) eV
    mbeta_in_band = (MBETA_BAND_LO <= m_beta <= MBETA_BAND_HI)    # (local)
    mbeta_marginal = (
        abs(m_beta - MBETA_BAND_LO) < MBETA_EDGE
        or abs(m_beta - MBETA_BAND_HI) < MBETA_EDGE
    )  # (local)

    # ---- m_beta non-detection horizons (forward prediction) ----
    KATRIN_FINAL = 0.3                                            # (local) eV (KATRIN final sensitivity)
    PROJECT8_TARGET = 0.04                                        # (local) eV (Project-8 design target)
    mbeta_nondetect_katrin = m_beta < KATRIN_FINAL               # (local)
    mbeta_nondetect_project8 = m_beta < PROJECT8_TARGET          # (local)

    # ---- Composite gate verdict ----
    all_pass = (
        sigma_reldiff <= SIGMA_RELDIFF_TOL
        and sigma_below_desi
        and mbb_in_band
        and mbeta_in_band
    )  # (local)
    any_out = (not sigma_below_desi) or (not mbb_in_band) or (not mbeta_in_band) \
        or (sigma_reldiff > SIGMA_RELDIFF_TOL)  # (local)
    marginal = mbb_marginal or mbeta_marginal                    # (local)

    if all_pass and not marginal:
        verdict = "PASS"  # (local)
    elif all_pass and marginal:
        verdict = "INFO"  # (local)
    elif any_out:
        verdict = "FAIL"  # (local)
    else:
        verdict = "INFO"  # (local)

    return dict(
        verdict=verdict,
        m_nu=m_nu,
        Sigma=Sigma,
        Sigma_npz=Sigma_npz,
        Sigma_mnu_FW=float(Sigma_mnu_FW),
        sigma_reldiff=sigma_reldiff,
        sigma_below_desi=sigma_below_desi,
        DESI_bound=float(Sigma_mnu_bound_DESI_2024),
        crosscheck_reldiff_npz=crosscheck_reldiff_npz,
        delta_CP_allowed=delta_CP_allowed,
        # PDG primary
        s12_pdg=s12_pdg, s13_pdg=s13_pdg, Ue2_pdg=Ue2_pdg,
        m_beta_pdg=mbeta_pdg,
        mbb_lo_pdg_meV=mbb_lo_pdg_meV, mbb_hi_pdg_meV=mbb_hi_pdg_meV,
        mbb_central_pdg=mbb_central_pdg,
        # NuFit-6.0 diagnostic
        s12_nf=s12_nf, s13_nf=s13_nf, Ue2_nf=Ue2_nf,
        m_beta_nf=mbeta_nf,
        mbb_lo_nf_meV=mbb_lo_nf * 1000.0, mbb_hi_nf_meV=mbb_up_nf * 1000.0,
        mbb_central_nf=mbb_central_nf,
        mbb_pdg_to_nf_shift=mbb_pdg_to_nf_shift,
        # canonical anchors
        mbb_central_canonical=mbb_central_canonical,
        mbb_central_reldiff=mbb_central_reldiff,
        mbb_band_lo_reldiff=mbb_band_lo_reldiff,
        mbb_band_hi_reldiff=mbb_band_hi_reldiff,
        mbb_in_band=mbb_in_band, mbb_marginal=mbb_marginal,
        # m_beta primary
        m_beta=m_beta, mbeta_in_band=mbeta_in_band, mbeta_marginal=mbeta_marginal,
        KATRIN_FINAL=KATRIN_FINAL, PROJECT8_TARGET=PROJECT8_TARGET,
        mbeta_nondetect_katrin=mbeta_nondetect_katrin,
        mbeta_nondetect_project8=mbeta_nondetect_project8,
        m_betabeta_LEGEND200_reach=float(m_betabeta_LEGEND200_reach),
        m_betabeta_KamLANDZen=float(m_betabeta_KamLANDZen),
        m_betabeta_nextgen_reach=float(m_betabeta_nextgen_reach),
        MBB_BAND_LO_MEV=MBB_BAND_LO_MEV, MBB_BAND_HI_MEV=MBB_BAND_HI_MEV,
        MBETA_BAND_LO=MBETA_BAND_LO, MBETA_BAND_HI=MBETA_BAND_HI,
    )


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(R: dict):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

    # --- Panel A: the three detector channels on a log-mass axis ---
    ax = axes[0]
    Sigma = R["Sigma"] * 1000.0                                  # (local) meV
    m_beta = R["m_beta"] * 1000.0                               # (local) meV
    mbb_lo = R["mbb_lo_pdg_meV"]                                # (local)
    mbb_hi = R["mbb_hi_pdg_meV"]                                # (local)
    mbb_c = R["mbb_central_pdg"]                                # (local)

    # channel markers
    ax.errorbar([1], [Sigma], fmt="s", ms=11, color="#1f77b4", label=r"$\Sigma m_\nu$ (cosmological)")
    ax.errorbar([2], [m_beta], fmt="o", ms=11, color="#2ca02c", label=r"$m_\beta$ (kinematic)")
    ax.errorbar([3], [mbb_c], yerr=[[mbb_c - mbb_lo], [mbb_hi - mbb_c]],
                fmt="D", ms=10, color="#d62728", capsize=6,
                label=r"$m_{\beta\beta}$ (0$\nu\beta\beta$ band, $\delta_{CP}\in\{0,\pi\}$)")

    # detector horizons
    ax.axhline(R["DESI_bound"] * 1000.0, ls="--", color="#1f77b4", alpha=0.6,
               label=f"DESI $\\Sigma$ bound = {R['DESI_bound']*1000:.0f} meV")
    ax.axhline(R["PROJECT8_TARGET"] * 1000.0, ls=":", color="#2ca02c", alpha=0.7,
               label=f"Project-8 target = {R['PROJECT8_TARGET']*1000:.0f} meV")
    ax.axhline(R["m_betabeta_nextgen_reach"] * 1000.0, ls="-.", color="#d62728", alpha=0.5,
               label=f"0$\\nu\\beta\\beta$ next-gen floor = {R['m_betabeta_nextgen_reach']*1000:.0f} meV")
    ax.axhspan(R["MBB_BAND_LO_MEV"], R["MBB_BAND_HI_MEV"], color="#d62728", alpha=0.08)

    ax.set_yscale("log")
    ax.set_xlim(0.5, 3.5)
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels([r"$\Sigma m_\nu$", r"$m_\beta$", r"$m_{\beta\beta}$"])
    ax.set_ylabel("effective mass [meV]")
    ax.set_title("Absolute-mass triangle: one triple, three detector classes\n"
                 f"verdict = {R['verdict']}")
    ax.legend(fontsize=7.2, loc="upper right")
    ax.grid(alpha=0.25, which="both")

    # --- Panel B: m_bb band reproduction (PDG primary vs NuFit-6.0 diagnostic vs canonical) ---
    ax = axes[1]
    rows = [
        ("Row #80 canonical\n(m_bb_FW)", R["mbb_central_canonical"], None, None, "#000000"),
        ("PDG primary\n(0.307, 0.0220)", R["mbb_central_pdg"], R["mbb_lo_pdg_meV"], R["mbb_hi_pdg_meV"], "#d62728"),
        ("NuFit-6.0 diag.\n(0.303, 0.02225)", R["mbb_central_nf"], R["mbb_lo_nf_meV"], R["mbb_hi_nf_meV"], "#9467bd"),
    ]
    for i, (lab, c, lo, hi, col) in enumerate(rows):
        if lo is not None:
            ax.errorbar([i], [c], yerr=[[c - lo], [hi - c]], fmt="D", ms=10,
                        color=col, capsize=6)
        else:
            ax.plot([i], [c], marker="*", ms=18, color=col)
        ax.annotate(f"{c:.4f}", (i, c), textcoords="offset points", xytext=(10, 0),
                    fontsize=8, va="center")
    ax.axhspan(R["MBB_BAND_LO_MEV"], R["MBB_BAND_HI_MEV"], color="#d62728", alpha=0.08,
               label=f"Row #80 band [{R['MBB_BAND_LO_MEV']}, {R['MBB_BAND_HI_MEV']}] meV")
    ax.set_xticks(range(len(rows)))
    ax.set_xticklabels([r[0] for r in rows], fontsize=8)
    ax.set_ylabel(r"$m_{\beta\beta}$ [meV]")
    ax.set_title(f"$m_{{\\beta\\beta}}$ central reproduction\n"
                 f"PDG-central reldiff vs canonical = {R['mbb_central_reldiff']:.2e}; "
                 f"PDG$\\to$NuFit shift = {R['mbb_pdg_to_nf_shift']*100:+.2f}%")
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(alpha=0.25)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    payload = {
        "session": 11,
        "track": "investigation",
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


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")

    R = compute()

    # ---- Console report (NUMBERS first) ----
    print("\n=== INV11-W2-2 ABSOLUTE-MASS TRIANGLE ===")
    print(f"  input m_nu triple (S99-W3, eV) = {R['m_nu']}")
    print(f"  delta_CP allowed (J-forced)    = {R['delta_CP_allowed']}  (=> {{0, pi}})")
    print("\n  -- Channel (i): Sigma m_nu (cosmological / DESI Row #77) --")
    print(f"     Sigma_computed  = {R['Sigma']:.10f} eV")
    print(f"     Sigma_mnu_FW    = {R['Sigma_mnu_FW']:.10f} eV   reldiff = {R['sigma_reldiff']:.2e} "
          f"(tol {SIGMA_RELDIFF_TOL:.0e})  -> {'PASS' if R['sigma_reldiff'] <= SIGMA_RELDIFF_TOL else 'FAIL'}")
    print(f"     DESI bound      = {R['DESI_bound']} eV ; Sigma < bound? {R['sigma_below_desi']} "
          f"(margin {100*(1-R['Sigma']/R['DESI_bound']):.1f}% below)")
    print(f"     S99-W3 npz crosscheck_reldiff = {R['crosscheck_reldiff_npz']:.2e}")
    print("\n  -- Channel (ii): m_beta (kinematic endpoint / KATRIN, Project-8) [PDG primary] --")
    print(f"     |U_ei|^2 (PDG)  = {R['Ue2_pdg']}")
    print(f"     m_beta          = {R['m_beta']:.6e} eV = {R['m_beta']*1000:.5f} meV")
    print(f"     in band [{MBETA_BAND_LO}, {MBETA_BAND_HI}] eV? {R['mbeta_in_band']} "
          f"(marginal? {R['mbeta_marginal']})")
    print(f"     vs KATRIN final {R['KATRIN_FINAL']} eV : non-detection? {R['mbeta_nondetect_katrin']} "
          f"(x{R['KATRIN_FINAL']/R['m_beta']:.1f} below reach)")
    print(f"     vs Project-8 {R['PROJECT8_TARGET']} eV : non-detection? {R['mbeta_nondetect_project8']} "
          f"(x{R['PROJECT8_TARGET']/R['m_beta']:.1f} below target)")
    print("\n  -- Channel (iii): m_betabeta (0nubb / LEGEND Row #80) [PDG primary] --")
    print(f"     band [|t2-t3|, t2+t3] = [{R['mbb_lo_pdg_meV']:.5f}, {R['mbb_hi_pdg_meV']:.5f}] meV")
    print(f"     central (no-cancel)   = {R['mbb_central_pdg']:.6f} meV")
    print(f"     canonical m_bb_FW     = {R['mbb_central_canonical']:.6f} meV   "
          f"central reldiff = {R['mbb_central_reldiff']:.2e}")
    print(f"     Row #80 band edges reldiff: lo {R['mbb_band_lo_reldiff']:.2e}, hi {R['mbb_band_hi_reldiff']:.2e}")
    print(f"     central in Row #80 band [{MBB_BAND_LO_MEV}, {MBB_BAND_HI_MEV}] meV? {R['mbb_in_band']} "
          f"(marginal? {R['mbb_marginal']})")
    print(f"     vs LEGEND-200 reach {R['m_betabeta_LEGEND200_reach']*1000:.0f} meV : "
          f"x{R['m_betabeta_LEGEND200_reach']/R['mbb_central_pdg']*1000:.1f} below")
    print(f"     vs KamLAND-Zen {R['m_betabeta_KamLANDZen']*1000:.0f} meV : "
          f"x{R['m_betabeta_KamLANDZen']/R['mbb_central_pdg']*1000:.1f} below")
    print("\n  -- DIAGNOSTIC: TRUE NuFit-6.0 PMNS pair (0.303, 0.02225) --")
    print(f"     m_beta   = {R['m_beta_nf']*1000:.5f} meV")
    print(f"     m_bb band = [{R['mbb_lo_nf_meV']:.5f}, {R['mbb_hi_nf_meV']:.5f}] meV ; "
          f"central {R['mbb_central_nf']:.5f} meV")
    print(f"     PDG -> NuFit-6.0 m_bb central shift = {R['mbb_pdg_to_nf_shift']*100:+.3f}% "
          f"(DECISION-IRRELEVANT; both in funnel band)")

    make_plot(R)

    # ---- Persist data ----
    np.savez(
        OUT_NPZ,
        m_nu_eV=R["m_nu"],
        Sigma_eV=R["Sigma"],
        Sigma_mnu_FW=R["Sigma_mnu_FW"],
        sigma_reldiff=R["sigma_reldiff"],
        sigma_below_desi=R["sigma_below_desi"],
        DESI_bound=R["DESI_bound"],
        crosscheck_reldiff_npz=R["crosscheck_reldiff_npz"],
        delta_CP_allowed=R["delta_CP_allowed"],
        s12_pdg=R["s12_pdg"], s13_pdg=R["s13_pdg"], Ue2_pdg=R["Ue2_pdg"],
        m_beta_pdg=R["m_beta_pdg"],
        mbb_lo_pdg_meV=R["mbb_lo_pdg_meV"], mbb_hi_pdg_meV=R["mbb_hi_pdg_meV"],
        mbb_central_pdg=R["mbb_central_pdg"],
        s12_nf=R["s12_nf"], s13_nf=R["s13_nf"], Ue2_nf=R["Ue2_nf"],
        m_beta_nf=R["m_beta_nf"],
        mbb_lo_nf_meV=R["mbb_lo_nf_meV"], mbb_hi_nf_meV=R["mbb_hi_nf_meV"],
        mbb_central_nf=R["mbb_central_nf"],
        mbb_pdg_to_nf_shift=R["mbb_pdg_to_nf_shift"],
        mbb_central_canonical=R["mbb_central_canonical"],
        mbb_central_reldiff=R["mbb_central_reldiff"],
        mbb_band_lo_reldiff=R["mbb_band_lo_reldiff"],
        mbb_band_hi_reldiff=R["mbb_band_hi_reldiff"],
        mbb_in_band=R["mbb_in_band"],
        m_beta=R["m_beta"], mbeta_in_band=R["mbeta_in_band"],
        KATRIN_FINAL=R["KATRIN_FINAL"], PROJECT8_TARGET=R["PROJECT8_TARGET"],
        mbeta_nondetect_katrin=R["mbeta_nondetect_katrin"],
        mbeta_nondetect_project8=R["mbeta_nondetect_project8"],
        MBB_BAND_LO_MEV=R["MBB_BAND_LO_MEV"], MBB_BAND_HI_MEV=R["MBB_BAND_HI_MEV"],
        MBETA_BAND_LO=R["MBETA_BAND_LO"], MBETA_BAND_HI=R["MBETA_BAND_HI"],
        verdict=R["verdict"],
        audit_sha256=audit_sha, content_sha256=content_sha,
        scheme=SCHEME, convention=CONVENTION, L_max=str(L_MAX),
    )
    print(f"\n  npz -> {OUT_NPZ.name}")
    print(f"  png -> {OUT_PNG.name}")

    # ---- 4-tuple (final non-verdict line) ----
    value_str = (
        f"Sigma={R['Sigma']:.7f}eV(<0.072_DESI,reldiff{R['sigma_reldiff']:.1e});"
        f"m_beta={R['m_beta']*1000:.3f}meV(KATRIN/P8_NONDETECT);"
        f"m_bb=[{R['mbb_lo_pdg_meV']:.3f},{R['mbb_hi_pdg_meV']:.3f}]meV_central{R['mbb_central_pdg']:.3f}"
        f"(Row80_band,reldiff{R['mbb_central_reldiff']:.1e});"
        f"PDG_primary;NuFit6.0_shift{R['mbb_pdg_to_nf_shift']*100:+.2f}pct;delta_CP[0,pi]"
    )  # (local)
    print(f"\n(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # ---- Verdict payload (agent calls emit_verdict, session=11, track=investigation) ----
    note = (
        "three-channel absolute-mass triangle from ONE S99-W3 triple; PDG PMNS primary "
        "reproduces Row #80 m_bb band; NuFit-6.0 pair diagnostic (-0.60% decision-irrelevant); "
        "m_beta~0.009eV kinematic non-detection (forward prediction); INVESTIGATION-TRACK ONLY"
    )  # (local)
    print_verdict_payload(R["verdict"], value_str, audit_sha, content_sha,
                          companion_note=note)

    print(f"\n  elapsed {time.time()-t0:.2f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
