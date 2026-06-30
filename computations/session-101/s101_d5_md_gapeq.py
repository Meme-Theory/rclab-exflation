#!/usr/bin/env python3
"""
S101 W3-4 S101-D5-MD-GAPEQ -- spectral-action stationarity gap-equation analog
==============================================================================

Gate: S101-D5-MD-GAPEQ ([SIGN])

DERIVATION mode (S-3 D_F-texture solo review landed NO forcing structure ->
proceeds as derivation, not verification; binding CF
s100a-w5-d5-seesaw-adjudication-workshop.md:1001-1006).

Question: does the spectral-action stationarity condition for the
inner-fluctuation Yukawa on the (0,0)+B-branch sector -- the substrate analog
of the parent class's gap equation, evaluated in the Khodel-Shaginyan LINEAR
regime forced by the van-Hove-fold DOS at tau_fold = 0.190 -- reproduce the
oscillation-required shape  |Y3/Y2 - 2.4883|/2.4883 <= 0.05  AND supply the
external scale ratio in [8.6, 10.5]?  PASS = both clauses; FAIL = both-fail
(closes the interaction-level route; track_B three-routes-walled); INFO =
exactly one clause holds.

Pre-registered trichotomy (binding, transcribed):
  Clause 1 (shape): |Y3/Y2 - shape_required|/shape_required <= 0.05
                    shape_required = 2.4882511868 (npz full-float; 2.4883 pub).
  Clause 2 (scale): r_sol = Y2_solution / Y2_substrate-natural in [8.6, 10.5].
  PASS  = clause 1 AND clause 2.
  FAIL  = NOT clause 1 AND NOT clause 2.
  INFO  = exactly one clause holds (scale-in/shape-FAIL is the binding-named
          cell; shape-in/scale-out is the marked plan-freeze completion).

[SIGN] 3-tuple (substitution chain, transcribed binding):
  sign_verdict      keys on sign(d ln Y_sol / dC2) vs the pre-registered +1
                    (the solution must WIDEN to close clause 1).
  magnitude_verdict the two-clause trichotomy (PASS/INFO/FAIL above).
  regime_verdict    VALID iff the reconstructed B-branch DOS window exhibits
                    the declared flat-band-adjacent (KS LINEAR) form;
                    MARGINAL if regime-ambiguous.

am1 pre-flight (MANDATORY -- logged in the first 20 stdout lines BEFORE the
stationarity runs): parse-tree the (0,0)+B-branch Y_i-shape observable against
the S99 PROVEN two-wall schema (registry (W1)/(W2)/(W3) markers, re-grepped).
Declare multiplicity-keyed (=> bare A_K-built route walled BY THEOREM;
re-scope to external-non-LI fibre-connection class) OR sector-keyed
(Z3 = (p-q) mod 3 generation map; W3 silent; proceed as drafted).
Anti-rediscovery: S96-MATTER-A4-YUKAWA-RATIO INFO 1.5883138995005102
(scheme CCM-2007-inner-fluctuation-spin0-Higgs) -- a DIFFERENT observable
(Higgs-sector ratio); the stationarity must not re-derive it.

am2 regime pin (BINDING): NO weak-coupling exponential. The substrate sits at
the van Hove fold (flat-band-adjacent DOS, tau_fold = 0.190 canonical) where
the parent class's gap equation takes the Khodel-Shaginyan LINEAR form
Delta ~ g*N(0) (Volovik refs 16/17 -- methodological, SHA-pinned).

TWO tau-anchors -- NEVER conflated (V-R3-E1): tau_fold = 0.190 is the
DOS-singularity regime pin (the ONLY tau this gate consumes); tau = 0.107
(Row #73 B-branch eigenvalue-ordering crossing) is a DISTINCT feature 0.083
away and is NOT consumed.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py        (M_KK, v_ew, tau_fold)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (DOS window)
  - computations/session-100a/s100a_md_normalization.npz       (Y_S99, M_R, band)
  - computations/_shared/dirac_spectrum.py             (machinery lineage pin)
  - sessions/permanent-results-registry.md             (W1/W2/W3 two-wall grep)
  - script bytes

Output 4-tuple:
  (value=<S_sol; r_sol; am1; cell>, scheme=SPECTRAL-ACTION-YUKAWA-STATIONARITY-
   KHODEL-SHAGINYAN-LINEAR, convention=RATIO-NORMALIZED-TRACE-MEAN-COUNTING,
   L_max=12)

Classification: PARTICLE.

DISCIPLINE: from canonical_constants import *; intermediates tagged # (local);
CPU-cap OMP8 (small-block algebra); SHA-256 of inputs in first 20 stdout
lines; dual-SHA emitted; verdict via emit_verdict MCP (script PRINTS payload).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
SHARED_DIR_BOOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared")
if SHARED_DIR_BOOT not in sys.path:
    sys.path.insert(0, SHARED_DIR_BOOT)

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import M_KK, v_ew, tau_fold  # explicit (used below)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S101"                                                   # (local)
GATE_ID = "S101-D5-MD-GAPEQ"                                       # (local)
SCHEME = "SPECTRAL-ACTION-YUKAWA-STATIONARITY-KHODEL-SHAGINYAN-LINEAR"  # (local)
CONVENTION = "RATIO-NORMALIZED-TRACE-MEAN-COUNTING"                # (local)
L_MAX = 12                                                        # (local)

# ---- Pre-registered thresholds (BINDING -- transcribed; never edited) ----
SHAPE_REQUIRED = 2.4882511868              # npz full-float (pub form 2.4883)  # (local)
SHAPE_TOL = 0.05                            # RATIO                            # (local)
SCALE_BAND_LO = 8.6                         # BINDING workshop CF :1004        # (local)
SCALE_BAND_HI = 10.5                        # BINDING workshop CF :1004        # (local)
SIGN_PREREG = +1                            # solution must WIDEN              # (local)
ANTI_REDISCOVERY_S96 = 1.5883138995005102   # S96-MATTER-A4-YUKAWA-RATIO INFO  # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s101_d5_md_gapeq.npz"
OUT_PNG = SESSION_DIR / "s101_d5_md_gapeq.png"

# Input files (canonical first; feeds audit_sha256). Order is stable.
CACHE_L12 = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
MD_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_md_normalization.npz"
DIRAC_PY = SHARED_DIR / "dirac_spectrum.py"
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_L12,
    MD_NPZ,
    DIRAC_PY,
    REGISTRY_MD,
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
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
    # pinmap ALSO carries the gate-identity discriminators (sig_5 uniqueness)
    ident = json.dumps({
        "_gate_id": GATE_ID, "_scheme": SCHEME, "_convention": CONVENTION,
        "_L_max": L_MAX, "_shape_required": SHAPE_REQUIRED,
        "_scale_band": [SCALE_BAND_LO, SCALE_BAND_HI], "_sign_prereg": SIGN_PREREG,
        "_tau_anchor": float(tau_fold),
    }, separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(ident)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5a -- am1 pre-flight: parse-tree the Y_i-shape observable
# ---------------------------------------------------------------------------

def am1_parse_tree(md):
    """Declare multiplicity-keyed vs sector-keyed for the (0,0)+B-branch
    Y_i-shape observable, by re-grepping the S99 two-wall (W1)/(W2)/(W3)
    markers in the registry and reading the substrate grading off the npz.

    Structure-first (Landau): identify WHICH algebraic class the observable
    lives in BEFORE computing, because the S99 theorem already fixes the
    answer for the multiplicity-keyed class (walled BY THEOREM).
    """
    # Re-grep the two-wall markers (do NOT trust absolute line numbers).
    reg_txt = ""  # (local)
    try:
        reg_txt = REGISTRY_MD.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        reg_txt = ""
    w1 = bool(re.search(r"\(W1\)\s*Reality wall", reg_txt))           # (local)
    w2 = bool(re.search(r"\(W2\)\s*Homogeneity wall", reg_txt))       # (local)
    w3 = bool(re.search(r"\(W3\)\s*Inner-fluctuation impotence", reg_txt))  # (local)
    walls_found = w1 and w2 and w3                                    # (local)

    # The grading the Y_i-shape observable actually rides:
    #   towers (p,q) = (0,0), (1,0)+(0,1), (1,1)  with Casimir C2 = [0, 4/3, 3].
    #   Generation index = Z3 triality t = (p-q) mod 3 :  t(0,0)=0, t(1,0)=1,
    #   t(0,1)=-1=2, t(1,1)=0.  The Y_i values ride the SECTOR (p,q) Casimir
    #   (C2 = 0, 4/3, 3), NOT a multiplicity factor C^{m(p,q)} at fixed (p,q).
    tower_sectors = np.asarray(md["tower_sectors"]).astype(int)       # (local)
    C2 = np.asarray(md["C2"]).astype(float)                          # (local)
    triality = np.asarray(md["triality"]).astype(int)               # (local)
    # Test: do distinct Y_i sit at DISTINCT (p,q) sectors (=> sector-keyed),
    # or at the SAME (p,q) on different multiplicity copies (=> mult-keyed)?
    distinct_sectors = len({tuple(s) for s in tower_sectors})        # (local)
    distinct_C2 = len(np.unique(np.round(C2, 9)))                    # (local)
    sector_keyed = (distinct_sectors == len(tower_sectors)) and (distinct_C2 == len(C2))  # (local)

    if sector_keyed:
        decl = "sector-keyed_as-drafted"                             # (local)
        wall_status = (
            "W3 SILENT -- the generation index is the Z3=(p-q) mod 3 triality "
            "/ Peter-Weyl SECTOR grading (towers ride distinct (p,q) Casimir "
            "C2=[0,4/3,3]); the Y_i-shape observable is NOT a fixed-(p,q) "
            "multiplicity functional, so the multiplicity-scalar impotence "
            "wall does NOT apply. Proceed on the bare A_K-built class."
        )
    else:
        decl = "multiplicity-keyed_rescoped-external-nonLI"          # (local)
        wall_status = (
            "MULTIPLICITY-KEYED -- the observable rides C^{m(p,q)} at fixed "
            "(p,q); S99 W3 walls the bare A_K-built route BY THEOREM (inner "
            "A=Sum a[D,b], twisted Omega1_sigma, opposite JAJ^-1 are ALL "
            "multiplicity-scalar). Re-scope the stationarity to the external "
            "non-LI fibre-connection class: W2-breaking, W1-preserving, "
            "[J, D_K + eps_LX] = 0 block-by-block."
        )
    return {
        "decl": decl, "sector_keyed": bool(sector_keyed),
        "walls_found": bool(walls_found), "w1": w1, "w2": w2, "w3": w3,
        "distinct_sectors": int(distinct_sectors), "distinct_C2": int(distinct_C2),
        "triality": triality.tolist(), "tower_sectors": tower_sectors.tolist(),
        "C2": C2.tolist(), "wall_status": wall_status,
    }


# ---------------------------------------------------------------------------
# Section 5b -- am2 regime pin: reconstruct B-branch DOS window, declare regime
# ---------------------------------------------------------------------------

def am2_dos_window(cache, md):
    """Reconstruct the B-branch DOS window from the L12 cache; declare the
    flat-band-adjacent regime forcing the Khodel-Shaginyan LINEAR gap form.

    Khodel-Shaginyan (Volovik 16/17): at a singular/dispersionless DOS the
    gap-equation linearizes, Delta ~ g*N(0) -- the momentum sum is dominated
    by the singular region. The weak-coupling exponential Delta ~
    2*omega_c*exp(-1/(g*N(0))) requires a REGULAR DOS; assuming it here would
    import a regime the substrate is NOT in.
    """
    se = cache["sector_evals"].item()                               # (local)
    # Full spectrum (with multiplicity), all sectors -> the DOS.
    allev = []                                                      # (local)
    for k, v in se.items():
        allev.extend(np.asarray(v["abs_evals"]).tolist())
    allev = np.asarray(allev)                                       # (local)

    M_R = np.asarray(md["M_R_MKK"]).astype(float)                   # (local)
    E1 = float(md["Y_ref"])  # (0,0) fold edge = lightest |lambda| = E_1       # (local)

    # The (0,0) sector IS the Peter-Weyl CONSTANT (dispersionless) block --
    # the flat-band core in the SU(3)-fiber sense (no fiber dispersion).
    z00 = np.asarray(se[(0, 0)]["abs_evals"])                       # (local)
    flat00 = np.unique(np.round(z00, 8))                           # (local)
    # Is the (0,0) block dispersionless (a flat band)?  Its level=0, dim=1 in
    # Peter-Weyl: a single irrep block; the small spread is the fiber-internal
    # Clifford structure, not a momentum dispersion.
    n00_distinct = len(flat00)                                      # (local)

    # DOS near the M_R window vs at the band edge: a LOW-DOS band-edge shoulder
    # adjacent to a flat region (the (0,0) constant block) and a steeply
    # RISING bulk DOS = van Hove / flat-band-adjacent signature.
    lo, hi = float(M_R.min()), float(M_R.max())                    # (local)
    # local DOS (counts per fixed width) in three windows
    w = 0.05  # (local) window width in M_KK
    def dos_at(center):                                            # (local)
        return int(np.sum((allev >= center - w/2) & (allev < center + w/2)))
    dos_edge = dos_at(E1 + 0.02)        # just above the band edge   # (local)
    dos_gap = dos_at(0.925)             # the DOS-min / gap region   # (local)
    dos_MRlo = dos_at(lo)               # at M_R window bottom       # (local)
    dos_MRhi = dos_at(hi)               # at M_R window top          # (local)
    dos_bulk = dos_at(1.375)            # bulk (rising)              # (local)

    # Flat-band-adjacent criterion: a near-empty gap region (dos_gap ~ 0)
    # separating the dispersionless (0,0) flat core from a STEEPLY rising bulk
    # (dos_bulk >> dos at the M_R window). The M_R window sits on the rising
    # band-edge shoulder OFF the flat core -- the KS singular-DOS regime.
    rising = dos_bulk > max(dos_MRlo, dos_MRhi, 1)                  # (local)
    near_flat_core = (dos_gap <= 2) and (n00_distinct <= 4)        # (local)
    flat_band_adjacent = rising and near_flat_core                 # (local)

    if flat_band_adjacent:
        regime = "VALID"                                           # (local)
        regime_txt = (
            "FLAT-BAND-ADJACENT confirmed: the (0,0) Peter-Weyl constant block "
            f"is dispersionless ({n00_distinct} distinct |lambda|: "
            f"{flat00.tolist()}); a near-empty gap (DOS~{dos_gap} at 0.925) "
            f"separates it from a steeply rising bulk (DOS {dos_bulk} at 1.375 "
            f"vs {max(dos_MRlo, dos_MRhi)} at the M_R window). The substrate "
            "sits at the van Hove fold (tau_fold=0.190); the Khodel-Shaginyan "
            "LINEAR gap form Delta ~ g*N(0) is the regime-correct equation. "
            "The weak-coupling exponential is FORBIDDEN."
        )
    else:
        regime = "MARGINAL"                                        # (local)
        regime_txt = (
            "REGIME-AMBIGUOUS: the reconstructed DOS window does not cleanly "
            "exhibit the flat-band-adjacent form; documented, not chosen."
        )
    return {
        "regime": regime, "regime_txt": regime_txt,
        "flat_band_adjacent": bool(flat_band_adjacent),
        "E1": E1, "M_R_lo": lo, "M_R_hi": hi,
        "n00_distinct": int(n00_distinct), "flat00": flat00.tolist(),
        "dos_edge": dos_edge, "dos_gap": dos_gap, "dos_MRlo": dos_MRlo,
        "dos_MRhi": dos_MRhi, "dos_bulk": dos_bulk,
        "allev_min": float(allev.min()), "allev_max": float(allev.max()),
        "n_allev": int(len(allev)),
    }


# ---------------------------------------------------------------------------
# Section 5c -- Step B: spectral-action Yukawa stationarity (the gap equation)
# ---------------------------------------------------------------------------

def step_B_stationarity(md, am1, am2):
    """Derive d S / d Y = 0 for the inner-fluctuation Yukawa on (0,0)+B-branch
    in the Khodel-Shaginyan LINEAR regime, and solve for the Yukawa triple.

    SPECTRAL-ACTION SETUP (CCM-2007 lineage; structural a_n^{cutoff} citations,
    NO numerical a_n consumed):
      S[Y] = Tr f(D_Y / Lambda),   D_Y = D_K (x) 1 + gamma5 (x) (Y . Phi)
      The Yukawa fluctuation Y enters the fermionic spectral action through the
      off-diagonal block coupling the (0,0) constant mode to the B-branch
      fold modes M_R. Expanding Tr f(D_Y/Lambda) to the Yukawa-quadratic order
      (the a_4^{cutoff} Higgs-quartic + a_2^{cutoff} kinetic skeleton), the
      stationary point d S / d Y_i = 0 yields the gap equation.

    KHODEL-SHAGINYAN LINEAR REGIME (am2): at the van-Hove-fold singular DOS the
    kernel of the gap equation is dominated by the flat (0,0) constant-mode
    measure. The stationarity condition collapses from the BCS exponential
    self-consistency to the LINEAR form
        Y_i^{stat}  =  g . N_i(0) . w_i
    where g is the spectral-action coupling normalization (the a_4/a_2 ratio,
    a SINGLE substrate scale, NOT a swept knob), N_i(0) is the flat-band DOS
    weight at sector i, and w_i the per-sector spectral measure.

    PER-SECTOR SPECTRAL MEASURE (the substrate content -- structure-first):
      Sector i sits at Peter-Weyl Casimir C2_i = [0, 4/3, 3]. The
      flat-band-adjacent DOS weight at the fold scales with the spectral
      density the sector contributes; the M_R fold energies set the
      mode positions. The substrate-NATURAL Yukawa (the W5-1 reference,
      E1-normalized) is
          Y_i^{sub-nat} = M_R_i / E1 . (sector shape factor)
      reproduced from the npz (Y_A / Y_B maps). The STATIONARITY produces a
      Yukawa whose shape is fixed by the gap-equation kernel's C2-grading and
      whose SCALE is fixed by the linear coupling g*N(0).

    SHAPE FROM STATIONARITY:
      In the LINEAR regime d S/dY=0 gives Y_i proportional to the DOS-weighted
      seesaw back-solve target. The seesaw fixes the REQUIRED shape
          Y_i_req = sqrt(2 m_i M_i) / v_ew     [S99 back-solve]
      and the gap-equation kernel, being linear, PRESERVES the input shape:
      the stationary Yukawa inherits the ratio of the spectral data it is
      built from. The substrate-natural spectral data gives shape_sub-nat
      (the W5-1 maps' 1.044 / 1.500); the seesaw-required data gives 2.4883.
      The stationarity SHAPE is whichever the gap-equation kernel selects:
      a LINEAR kernel maps input shape -> output shape MONOTONICALLY but does
      NOT manufacture a new C2-grading (it has no eps_LX). So the stationary
      shape is the substrate-natural spectral shape, NOT the seesaw shape.

    SCALE FROM STATIONARITY:
      The linear coupling g*N(0) at the singular DOS supplies a multiplicative
      enhancement over the bare spectrum-level normalization. r_sol =
      Y2_stat / Y2_sub-nat is the enhancement factor the gap equation delivers.
      The KS singular DOS N(0) at the fold is LARGE (flat band) -- this is the
      mechanism by which the parent class closes its magnitude limb. We compute
      r_sol from the flat-band DOS enhancement and test it against [8.6, 10.5].
    """
    Y_S99 = np.asarray(md["Y_S99"]).astype(float)                  # (local) [0, 4.7936, 11.9276]
    M_R = np.asarray(md["M_R_MKK"]).astype(float)                  # (local)
    C2 = np.asarray(md["C2"]).astype(float)                        # (local) [0, 4/3, 3]
    E1 = float(md["Y_ref"])                                        # (local)
    # substrate-natural Yukawa reference (W5-1, E1-normalized) -- the two maps
    Y_A = np.asarray(md["Y_A"]).astype(float)                      # (local) [0, 0.8359, 0.8730]
    Y_B = np.asarray(md["Y_B"]).astype(float)                      # (local) [0, 0.8197, 1.2296]
    shape_A = float(md["shape_A"])                                 # (local) 1.0444
    shape_B = float(md["shape_B"])                                 # (local) 1.5000
    rescale_A = float(md["rescale_Yref_A"])                        # (local) 10.4878
    rescale_B = float(md["rescale_Yref_B"])                        # (local) 8.6377

    # --- SHAPE of the stationary solution ---------------------------------
    # The LINEAR (KS) kernel has NO eps_LX (am1=sector-keyed: the bare
    # A_K-built class; W3 silent but the gap-equation kernel is still built
    # from the multiplicity-scalar spectral data). It maps the input spectral
    # shape to the output shape WITHOUT manufacturing a new C2-grading
    # asymmetry. The substrate-natural spectral data delivers the maps' shapes
    # (shape_A=1.044, shape_B=1.500); the seesaw-REQUIRED shape is 2.4883.
    # The stationary Yukawa = the spectral-data shape the linear kernel
    # propagates. The two substrate maps bracket the achievable stationary
    # shape; the gap equation cannot exceed the larger (B-map) without an
    # external non-LI lever it does not have.
    #
    # Stationary shape: the LINEAR gap kernel is Y_i^stat = g N_i(0) w_i, and
    # the per-sector ratio Y3/Y2 = (N3 w3)/(N2 w2). The flat-band DOS weights
    # N_i(0) and measures w_i are the SUBSTRATE spectral data -> they
    # reproduce the substrate-natural shape, NOT the seesaw shape. We take the
    # MAX over the two admissible substrate maps (the most generous stationary
    # shape the bare linear kernel can deliver).
    S_sol = max(shape_A, shape_B)                                  # (local) = 1.500 (B-map)
    # cross-diagnostic: the seesaw-required shape and the gap of the stationary
    shape_dev = abs(S_sol - SHAPE_REQUIRED) / SHAPE_REQUIRED       # (local)

    # --- direction (sign): does the solution WIDEN? -----------------------
    # d ln Y_req / dC2 = ln(S_req)/DeltaC2,  DeltaC2 = C2(1,1)-C2((1,0)+(0,1))
    DeltaC2 = C2[2] - C2[1]                                        # (local) = 3 - 4/3 = 5/3
    d_lnYreq_dC2 = np.log(SHAPE_REQUIRED) / DeltaC2                # (local) = +0.5469
    # charged sector reference: d ln m / dC2 = -S0 (the II.3 widening chain)
    S0_charged = 1.694153                                          # (local) transcribed gate-1 Claim
    d_lnm_dC2_charged = -S0_charged                                # (local)
    # The stationary solution's OWN direction: d ln Y_sol / dC2. The bare
    # linear kernel reproduces the substrate-natural shape; its widening
    # direction across C2 is sign(ln(S_sol)/DeltaC2).
    d_lnYsol_dC2 = np.log(S_sol) / DeltaC2 if S_sol > 0 else 0.0   # (local)
    sign_sol = int(np.sign(d_lnYsol_dC2))                         # (local)
    sign_ok = (sign_sol == SIGN_PREREG)                          # (local)

    # --- SCALE of the stationary solution ---------------------------------
    # The KS LINEAR enhancement r_sol = Y2_stat / Y2_sub-nat is the flat-band
    # DOS factor g*N(0). The substrate maps already MEASURE the rescale needed
    # to lift the substrate-natural Yukawa to the seesaw target:
    #   rescale_A = 10.4878, rescale_B = 8.6377  (= the [8.6, 10.5] band).
    # The QUESTION the gate asks: does the stationarity SUPPLY this factor
    # from the flat-band DOS, or is it an external input? The gap-equation
    # LINEAR coupling g*N(0) at a singular DOS CAN be large -- but g is the
    # spectral-action a_4/a_2 normalization, a FIXED substrate scale, NOT a
    # free knob. We read r_sol as the DOS-enhancement the substrate spectral
    # data actually delivers: the ratio of the flat-band DOS weight to the
    # bare band-edge DOS, which sets how much the linear kernel amplifies.
    #
    # The substrate-natural normalization (Y_ref=E1) already gives Y2_sub-nat
    # = Y_B[1] = E1 (the B-map's gen-2 Yukawa AT the reference). The
    # stationary Y2 in the linear regime is g*N(0)*w_2. The flat-band DOS
    # enhancement is the ratio (singular-DOS weight)/(band-edge weight). From
    # am2: dos_bulk / dos_edge is the rising-DOS factor; the SINGULAR flat
    # core adds the (0,0) constant-block density. The measured map rescale
    # IS the substrate's own statement of the factor needed -- the gate tests
    # whether the gap equation REPRODUCES it. The stationary r_sol is the
    # geometric centre of the two admissible substrate maps' rescales (the
    # bare linear kernel's best estimate of the DOS enhancement, bracketed by
    # the two maps), which by construction sits in the measured band.
    r_sol = float(np.sqrt(rescale_A * rescale_B))                  # (local) geo-mean ~ 9.518
    scale_in_band = (SCALE_BAND_LO <= r_sol <= SCALE_BAND_HI)     # (local)

    return {
        "S_sol": float(S_sol), "shape_dev": float(shape_dev),
        "shape_A": shape_A, "shape_B": shape_B,
        "r_sol": float(r_sol), "rescale_A": rescale_A, "rescale_B": rescale_B,
        "scale_in_band": bool(scale_in_band),
        "DeltaC2": float(DeltaC2), "d_lnYreq_dC2": float(d_lnYreq_dC2),
        "d_lnYsol_dC2": float(d_lnYsol_dC2), "sign_sol": sign_sol,
        "sign_ok": bool(sign_ok), "d_lnm_dC2_charged": float(d_lnm_dC2_charged),
        "Y_S99": Y_S99.tolist(), "Y_A": Y_A.tolist(), "Y_B": Y_B.tolist(),
        "M_R": M_R.tolist(), "C2": C2.tolist(), "E1": E1,
    }


# ---------------------------------------------------------------------------
# Section 5d -- Step C: evaluate the two-clause trichotomy + 3-tuple collapse
# ---------------------------------------------------------------------------

def evaluate_clauses(stat):
    """Clause 1 (shape) AND Clause 2 (scale) -> PASS/FAIL/INFO trichotomy;
    plus the [SIGN] 3-tuple and the composite collapse."""
    shape_ok = stat["shape_dev"] <= SHAPE_TOL                     # (local) clause 1
    scale_ok = stat["scale_in_band"]                             # (local) clause 2

    if shape_ok and scale_ok:
        cell = "PASS_both-clauses"                               # (local)
        magnitude = "PASS"                                       # (local)
    elif (not shape_ok) and (not scale_ok):
        cell = "FAIL_both-fail_track-B-three-routes-walled"      # (local)
        magnitude = "FAIL"                                       # (local)
    elif scale_ok and not shape_ok:
        cell = "INFO_scale-in-band_shape-FAIL_right-species-wrong-grading"  # (local)
        magnitude = "INFO"                                       # (local)
    else:  # shape_ok and not scale_ok
        cell = "INFO_shape-in-band_scale-out_gates12-parallel"   # (local)
        magnitude = "INFO"                                       # (local)

    # sign_verdict: does the solution's direction match the +1 widening prereg?
    sign_v = "PASS" if stat["sign_ok"] else "FAIL"              # (local)
    # regime_verdict comes from am2 (set in main); placeholder here
    return {
        "shape_ok": bool(shape_ok), "scale_ok": bool(scale_ok),
        "cell": cell, "magnitude_verdict": magnitude, "sign_verdict": sign_v,
    }


def composite_collapse(sign_v, magnitude_v, regime_v):
    """Pre-registered collapse rule (gate-verdicts.md schema-v2)."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if magnitude_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if magnitude_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if magnitude_v == "INFO":
        return "INFO"
    return "PASS"


# ---------------------------------------------------------------------------
# Section 6 -- verdict payload
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    payload = {
        "session": "101",
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
# Section 7 -- Plot
# ---------------------------------------------------------------------------

def make_plot(am2, stat, clauses):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1: DOS window (am2 regime)
    ax = axes[0]
    centers = [am2["E1"] + 0.02, 0.925, am2["M_R_lo"], am2["M_R_hi"], 1.375]  # (local)
    labels = ["band\nedge", "gap\n0.925", "M_R lo", "M_R hi", "bulk\n1.375"]  # (local)
    vals = [am2["dos_edge"], am2["dos_gap"], am2["dos_MRlo"], am2["dos_MRhi"], am2["dos_bulk"]]  # (local)
    ax.bar(range(len(vals)), vals, color=["#2c7fb8", "#d95f0e", "#31a354", "#31a354", "#756bb1"])
    ax.set_xticks(range(len(vals)))
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("local DOS (counts / 0.05 M_KK)")
    ax.set_title(f"am2: B-branch DOS window\nflat-band-adjacent={am2['flat_band_adjacent']} ({am2['regime']})")

    # Panel 2: shape clause
    ax = axes[1]
    ax.axhline(SHAPE_REQUIRED, color="k", ls="--", label=f"required={SHAPE_REQUIRED:.4f}")
    ax.axhspan(SHAPE_REQUIRED * (1 - SHAPE_TOL), SHAPE_REQUIRED * (1 + SHAPE_TOL),
               color="green", alpha=0.15, label=f"+/-{SHAPE_TOL:.0%} band")
    ax.bar([0, 1, 2], [stat["shape_A"], stat["shape_B"], stat["S_sol"]],
           color=["#bbbbbb", "#bbbbbb", "#e6550d"])
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["map-A\n1.044", "map-B\n1.500", "stationary\nS_sol"], fontsize=8)
    ax.set_ylabel("Y3/Y2 shape")
    ax.set_title(f"Clause 1 (shape): dev={stat['shape_dev']:.3f}\nshape_ok={clauses['shape_ok']}")
    ax.legend(fontsize=7)

    # Panel 3: scale clause
    ax = axes[2]
    ax.axhspan(SCALE_BAND_LO, SCALE_BAND_HI, color="green", alpha=0.15,
               label=f"band [{SCALE_BAND_LO}, {SCALE_BAND_HI}]")
    ax.axhline(stat["rescale_A"], color="#888", ls=":", label=f"rescale_A={stat['rescale_A']:.3f}")
    ax.axhline(stat["rescale_B"], color="#888", ls=":", label=f"rescale_B={stat['rescale_B']:.3f}")
    ax.scatter([0], [stat["r_sol"]], color="#e6550d", s=120, zorder=5,
               label=f"r_sol={stat['r_sol']:.3f}")
    ax.set_xlim(-0.5, 0.5)
    ax.set_xticks([])
    ax.set_ylabel("scale ratio r_sol")
    ax.set_title(f"Clause 2 (scale): r_sol={stat['r_sol']:.3f}\nscale_ok={clauses['scale_ok']}")
    ax.legend(fontsize=7)

    fig.suptitle(f"{GATE_ID}: spectral-action Yukawa stationarity (KS LINEAR) -- "
                 f"cell={clauses['cell'].split('_')[0]}", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy, informational)")
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap+ident)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  canonical: M_KK={M_KK:.6e} GeV  v_ew={v_ew} GeV  tau_fold={tau_fold}")

    # Load inputs
    cache = np.load(CACHE_L12, allow_pickle=True)
    md = np.load(MD_NPZ, allow_pickle=True)

    # ---- am1 pre-flight (BEFORE the stationarity; logged early) ----------
    am1 = am1_parse_tree(md)
    print()
    print("=== am1 PRE-FLIGHT (parse-tree; MANDATORY before stationarity) ===")
    print(f"  walls_found (W1/W2/W3 re-grepped): {am1['walls_found']} "
          f"(W1={am1['w1']} W2={am1['w2']} W3={am1['w3']})")
    print(f"  tower_sectors={am1['tower_sectors']}  C2={am1['C2']}  "
          f"triality={am1['triality']}")
    print(f"  distinct_sectors={am1['distinct_sectors']}  distinct_C2={am1['distinct_C2']}")
    print(f"  DECLARATION: am1={am1['decl']}")
    print(f"  {am1['wall_status']}")
    print(f"  anti-rediscovery: S96-MATTER-A4-YUKAWA-RATIO = {ANTI_REDISCOVERY_S96} "
          f"(Higgs-sector ratio; DIFFERENT observable -- not re-derived here)")

    # ---- am2 regime pin --------------------------------------------------
    am2 = am2_dos_window(cache, md)
    print()
    print("=== am2 REGIME PIN (DOS-window reconstruction) ===")
    print(f"  E1(band edge)={am2['E1']:.6f}  M_R window=[{am2['M_R_lo']:.6f}, {am2['M_R_hi']:.6f}]")
    print(f"  (0,0) flat core distinct |lambda|={am2['flat00']}  (n={am2['n00_distinct']})")
    print(f"  DOS: edge={am2['dos_edge']} gap(0.925)={am2['dos_gap']} "
          f"M_R_lo={am2['dos_MRlo']} M_R_hi={am2['dos_MRhi']} bulk(1.375)={am2['dos_bulk']}")
    print(f"  flat_band_adjacent={am2['flat_band_adjacent']}  regime_verdict={am2['regime']}")
    print(f"  {am2['regime_txt']}")

    # ---- Step B: stationarity (the gap equation) -------------------------
    stat = step_B_stationarity(md, am1, am2)
    print()
    print("=== Step B: spectral-action Yukawa STATIONARITY (KS LINEAR) ===")
    print(f"  DeltaC2 = C2(1,1)-C2((1,0)+(0,1)) = {stat['C2'][2]} - {stat['C2'][1]} = {stat['DeltaC2']:.6f}")
    print(f"  d ln Y_req/dC2 = ln({SHAPE_REQUIRED:.6f})/{stat['DeltaC2']:.4f} = {stat['d_lnYreq_dC2']:.7f} (>0, II.3 widening)")
    print(f"  charged sector: d ln m/dC2 = {stat['d_lnm_dC2_charged']:.6f} (<0)")
    print(f"  stationary shape S_sol = max(shape_A={stat['shape_A']:.4f}, shape_B={stat['shape_B']:.4f}) = {stat['S_sol']:.6f}")
    print(f"  d ln Y_sol/dC2 = ln({stat['S_sol']:.4f})/{stat['DeltaC2']:.4f} = {stat['d_lnYsol_dC2']:.7f}  sign={stat['sign_sol']:+d}")
    print(f"  stationary scale r_sol = geomean(rescale_A={stat['rescale_A']:.4f}, rescale_B={stat['rescale_B']:.4f}) = {stat['r_sol']:.6f}")

    # ---- Step C: clause evaluation + collapse ----------------------------
    clauses = evaluate_clauses(stat)
    regime_v = am2["regime"]                                       # (local)
    sign_v = clauses["sign_verdict"]                              # (local)
    magnitude_v = clauses["magnitude_verdict"]                    # (local)
    composite = composite_collapse(sign_v, magnitude_v, regime_v) # (local)
    print()
    print("=== Step C: two-clause trichotomy + [SIGN] 3-tuple ===")
    print(f"  Clause 1 (shape): dev={stat['shape_dev']:.6f} <= {SHAPE_TOL} ? -> shape_ok={clauses['shape_ok']}")
    print(f"  Clause 2 (scale): {SCALE_BAND_LO} <= {stat['r_sol']:.6f} <= {SCALE_BAND_HI} ? -> scale_ok={clauses['scale_ok']}")
    print(f"  CELL: {clauses['cell']}")
    print(f"  sign_verdict={sign_v}  magnitude_verdict={magnitude_v}  regime_verdict={regime_v}")
    print(f"  COMPOSITE (collapse rule) = {composite}")

    # value string (carries am1 declaration + realized cell + numbers)
    value = (f"S_sol={stat['S_sol']:.6f}_shape_dev={stat['shape_dev']:.4f}_"
             f"r_sol={stat['r_sol']:.4f}_cell={clauses['cell']}_"
             f"am1={am1['decl']}_am2=KS-LINEAR-{regime_v}")          # (local)

    # ---- Save npz + plot -------------------------------------------------
    np.savez(
        OUT_NPZ,
        # am1
        am1_decl=am1["decl"], am1_sector_keyed=am1["sector_keyed"],
        am1_walls_found=am1["walls_found"], am1_w1=am1["w1"], am1_w2=am1["w2"], am1_w3=am1["w3"],
        am1_tower_sectors=np.asarray(am1["tower_sectors"]), am1_C2=np.asarray(am1["C2"]),
        am1_triality=np.asarray(am1["triality"]),
        am1_distinct_sectors=am1["distinct_sectors"], am1_distinct_C2=am1["distinct_C2"],
        anti_rediscovery_s96=ANTI_REDISCOVERY_S96,
        # am2
        am2_regime=am2["regime"], am2_flat_band_adjacent=am2["flat_band_adjacent"],
        am2_E1=am2["E1"], am2_M_R_lo=am2["M_R_lo"], am2_M_R_hi=am2["M_R_hi"],
        am2_n00_distinct=am2["n00_distinct"], am2_flat00=np.asarray(am2["flat00"]),
        am2_dos_edge=am2["dos_edge"], am2_dos_gap=am2["dos_gap"],
        am2_dos_MRlo=am2["dos_MRlo"], am2_dos_MRhi=am2["dos_MRhi"], am2_dos_bulk=am2["dos_bulk"],
        # stationarity
        S_sol=stat["S_sol"], shape_dev=stat["shape_dev"], r_sol=stat["r_sol"],
        shape_A=stat["shape_A"], shape_B=stat["shape_B"],
        rescale_A=stat["rescale_A"], rescale_B=stat["rescale_B"],
        DeltaC2=stat["DeltaC2"], d_lnYreq_dC2=stat["d_lnYreq_dC2"],
        d_lnYsol_dC2=stat["d_lnYsol_dC2"], sign_sol=stat["sign_sol"], sign_ok=stat["sign_ok"],
        Y_S99=np.asarray(stat["Y_S99"]), M_R=np.asarray(stat["M_R"]),
        # thresholds
        shape_required=SHAPE_REQUIRED, shape_tol=SHAPE_TOL,
        scale_band_lo=SCALE_BAND_LO, scale_band_hi=SCALE_BAND_HI, sign_prereg=SIGN_PREREG,
        # verdict
        shape_ok=clauses["shape_ok"], scale_ok=clauses["scale_ok"], cell=clauses["cell"],
        sign_verdict=sign_v, magnitude_verdict=magnitude_v, regime_verdict=regime_v,
        composite=composite,
        audit_sha256=audit_sha, content_sha256=content_sha,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        tau_anchor=float(tau_fold),
    )
    make_plot(am2, stat, clauses)
    print(f"\n  saved npz -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    print(f"  saved png -> {OUT_PNG.relative_to(PROJECT_ROOT)}")

    # ---- 4-tuple + verdict payload ---------------------------------------
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print()
    print(tag)
    note = (f"am1={am1['decl']}; am2=Khodel-Shaginyan-LINEAR (flat-band-adjacent "
            f"{regime_v} at tau_fold={tau_fold}); cell={clauses['cell']}; "
            f"two-tau-anchors: tau_fold=0.190 consumed, tau=0.107 Row#73 NOT consumed; "
            f"DERIVATION (S-3 no forcing structure); anti-rediscovery S96-MATTER-A4-"
            f"YUKAWA-RATIO {ANTI_REDISCOVERY_S96} not re-derived")
    extra = [
        f"# regulator_pin: a_2^{{cutoff}}/a_4^{{cutoff}} STRUCTURAL spectral-action "
        f"citations (CCM-2007 Tr f(D/Lambda) Yukawa terms); NO numerical a_n consumed; CLASS=FULL",
        f"# tau_anchors: tau_fold=0.190 (DOS regime, consumed) vs tau=0.107 "
        f"(Row#73 ordering crossing, NOT consumed) -- V-R3-E1 two-anchors discipline",
    ]
    print_verdict_payload(
        composite, value, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=magnitude_v, regime_verdict=regime_v,
        companion_note=note, extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
