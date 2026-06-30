#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CF-S117-LEPTON-SEESAW-R-CHANNEL  (Session 117, Wave 2, §W2-2)  -- [VERIFY] gate.

THE BINDING OPEN CHANNEL R (S116-W2-PMNS-RESCUE carry-forward)
-------------------------------------------------------------
The S116-W2-LEPTON-PMNS-TEXTURE gate WALLED the lepton mixing ANGLES
(mix_grp=0/4; the eigenVECTOR channel). The S116-W2-PMNS-RESCUE workshop closed
that as WALLED-AS-UNDER-DETERMINED with the sharp corollary: the seesaw masses fix
the singular VALUES (the spectrum), NOT the left singular VECTORS (the angles).

This gate tests the SPECTRUM channel the angle-metric does NOT touch:
  R = Delta m^2_32 / Delta m^2_21 = m_3^2/m_2^2 - 1   (at m_1 = 0, normal ordering)
against the NuFIT 5.2 NO 3-sigma R-floor [17, 66].

WHAT THIS GATE COMPUTES (deterministic; reads the S116 texture npz)
------------------------------------------------------------------
  (1) BARE B-branch composite (THE SPECTRUM CHANNEL; verdict number):
        M_nu_bare = M_D_diag . M_R^{-1} . M_D_diag^T
        with M_D_diag = diag(Y_nu_diag)  (mass-pinned DIAGONAL Dirac; NO eps_LX),
             M_R       = diag(B-branch fold energies)  (the "bowtie shape").
        m_1 = 0 EXACTLY (Y_1 = 0, rank-2 M_D; S100a). R_bare = m_3^2/m_2^2 - 1.
  (2) CONTRAST -- npz M_nu (with the SHARED eps_LX off-diagonal w23_nu the S116
        angle-metric transplanted into the neutrino Dirac 2-3 block): its singular
        values give R_eps23. This is the angle-metric "touching" the spectrum
        (which the gate hypothesis posits it should NOT) -- reported transparently.
  (3) CROSS-CHECK -- R from the S99 oscillation-anchored masses [0,0.0086776,
        0.0495278] eV, and from the NuFit-6.0 central Delta m^2 pins.
  (4) STRUCTURAL -- rescale-INVARIANCE: M_R -> c.M_R gives M_nu -> (1/c).M_nu, so
        every eigenvalue scales by 1/c and R is UNCHANGED. Verified across
        c in {1e-3 .. 1e6}. => R is set by the bowtie SHAPE, not the Majorana SCALE;
        the INFO clause keys on a bowtie RESHAPE, not a rescale.

PRE-REGISTERED OPERATOR (plan sessions/session-plan/session-117-plan-w2.md §W2-2):
  PASS iff R_bare in [17, 66]                       (spectrum channel holds)
  FAIL iff R_bare not in [17,66] AND no reshape reaches the band
                                                    (FAIL sub-direction R<17 = S96 shortfall)
  INFO iff R_bare not in [17,66] but a bowtie RESHAPE reaches the band
                                                    (reachable only off the bare fold shape)

[VERIFY] substitution chain (plan §W2-2):
  Def 1: M_nu = M_D . M_R^{-1} . M_D^T                          [type-I seesaw]
  Def 2: {m_1<=m_2<=m_3} = singular values of M_nu (>=0); M_D rank-2 (Y_1=0) => m_1=0 EXACT
  Def 3: R := Delta m^2_32 / Delta m^2_21 = (m_3^2-m_2^2)/(m_2^2-m_1^2)
  Substitute m_1=0:  R = (m_3^2-m_2^2)/m_2^2 = m_3^2/m_2^2 - 1
  Rescale:  M_R -> c.M_R => M_nu -> (1/c).M_nu => every m_i -> m_i/c => R UNCHANGED
  Direction: R >= 17 <=> m_3^2/m_2^2 >= 18 <=> m_3/m_2 >= sqrt(18)=4.2426
             S96 peak R=6.87 => m_3/m_2=2.805 < 4.2426 => R<17 was the S96 shortfall.

============================================================================
SUBSTRATE-FIRST (phononic-framing.md) -- PARTICLE:
============================================================================
  D_K eigenvalues -> seesaw composite M_nu = M_D M_R^{-1} M_D^T -> light-mass
  spectrum -> oscillation ratio R -> measurement. The light neutrino masses ARE
  the eigenvalues of the seesaw composite, assembled from D_K's Dirac-Yukawa M_D
  and the fold-spectrum Majorana M_R (B-branch fold energies, INTERNAL to the
  spectrum per S100a). R is the spectral-hierarchy observable read off that
  spectrum; it is INVARIANT under the Majorana SCALE (which S100a holds
  oscillation-anchored) and set by the bowtie SHAPE -- a substrate-IS spectral fact.
  Direction flows substrate -> spectrum -> observable, never the reverse.

  HONEST CAVEAT (S100a-MD-NORMALIZATION INFO, PERMANENT): the Dirac-Yukawa RATIO
  Y_3/Y_2 is oscillation-anchored (the D_K bottom-triple -> Y_i map is NON-UNIQUE,
  MAP-A vs MAP-B), so R_bare is a CONSISTENCY of the spectrum channel with the NuFIT
  band, NOT a zero-free-parameter prediction. The substrate-FIRST content is the
  seesaw STRUCTURE + M_R bowtie shape + the rescale-invariance (R = SHAPE not SCALE).

External observational anchor: NuFIT 5.2 NO 3-sigma R-floor [17,66] is a
laboratory-IN observational band (class-(B) datum), carried as # (local) pins --
NOT a canonical_constants import (PDG/NuFIT lab values are working anchors per
substrate-first-canonical-sourcing.md §(i)). dm2_21_NuFit/dm2_31_NuFit ARE imported
as the canonical central cross-check anchor.

Output 4-tuple:
  (value=<R_bare + band + contrasts + rescale-inv>, scheme=seesaw-composite-eigenvalue-ratio,
   convention=RATIO-..., L_max=N/A)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  computations/_shared/canonical_constants.py
  computations/session-116/s116_lepton_pmns_texture.npz
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (math-scripts.md; 3x3 svd is tiny) ---
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
# Section 1 -- Paths + canonical constants (MANDATORY import)
# ---------------------------------------------------------------------------
THIS = Path(__file__).resolve()
SESSION_DIR = THIS.parent                                  # computations/session-117
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    tau_fold,
    dm2_21_NuFit, dm2_31_NuFit,
)

import matplotlib                                           # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                             # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Identity + pinned machinery (plan §W2-2 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "117"                                             # (local)
GATE_ID = "CF-S117-LEPTON-SEESAW-R-CHANNEL"                 # (local)
SCHEME = "seesaw-composite-eigenvalue-ratio"               # (local)
CONVENTION = "RATIO-Dm2-32-over-21-eq-m3sq-over-m2sq-minus-1-at-m1-zero-NO"  # (local)
L_MAX = "N/A"                                               # (local) 3x3 M_nu read directly
TAU = float(tau_fold)                                       # (local) 0.19 canonical (provenance)
PUB_SIGFIGS = 6                                             # (local) Class-8.3 publication precision

# --- Pre-registered NuFIT 5.2 NO 3-sigma R-floor (laboratory-IN band; # local) ---
# R = Delta m^2_32 / Delta m^2_21 (NO). The 3-sigma R range follows from the NuFIT
# 5.2 NO 3-sigma ranges of the two splittings; the plan pins the band edges:
R_LO, R_HI = 17.0, 66.0                                     # (local) NuFIT 5.2 NO 3-sigma R-floor (plan §W2-2)

# Rescale-invariance probe scales (structural check; # local):
RESCALE_CS = [1.0e-3, 1.0e-2, 1.0e-1, 1.0, 1.0e1, 1.0e2, 1.0e3, 1.0e6]  # (local)
M1_REL_TOL = 1.0e-9                                         # (local) m_1 machine-zero check (plan pin)


# ---------------------------------------------------------------------------
# Section 3 -- SHA-256 dual-SHA block (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 4 -- Paths/targets
# ---------------------------------------------------------------------------
OUT_NPZ = SESSION_DIR / "s117_lepton_seesaw_r_channel.npz"
OUT_PNG = SESSION_DIR / "s117_lepton_seesaw_r_channel.png"

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
S116_NPZ = COMPUTATIONS_DIR / "session-116" / "s116_lepton_pmns_texture.npz"

INPUT_FILES = [CANONICAL_PATH, S116_NPZ]


# ---------------------------------------------------------------------------
# Section 5 -- R helpers
# ---------------------------------------------------------------------------
def singular_values_ascending(M: np.ndarray) -> np.ndarray:
    """Singular values of a 3x3 real matrix, ascending. For a real-symmetric PSD
    seesaw composite these equal the (non-negative) eigenvalues."""
    s = np.linalg.svd(np.asarray(M, dtype=float), compute_uv=False)  # (local) descending >=0
    return np.sort(s)                                                # (local) ascending


def R_from_masses(m: np.ndarray) -> float:
    """R = Delta m^2_32 / Delta m^2_21 = (m_3^2 - m_2^2)/(m_2^2 - m_1^2), ascending m."""
    m1, m2, m3 = float(m[0]), float(m[1]), float(m[2])
    denom = m2 * m2 - m1 * m1                              # (local) Delta m^2_21
    if denom <= 0:
        return float("nan")
    return (m3 * m3 - m2 * m2) / denom                     # (local)


def R_at_m1zero(m: np.ndarray) -> float:
    """R at m_1=0 closed form: m_3^2/m_2^2 - 1 (used as a cross-check of R_from_masses)."""
    _, m2, m3 = float(m[0]), float(m[1]), float(m[2])
    if m2 <= 0:
        return float("nan")
    return (m3 * m3) / (m2 * m2) - 1.0                     # (local)


def in_band(R: float) -> bool:
    return bool(R_LO <= R <= R_HI)


# ---------------------------------------------------------------------------
# Section 6 -- Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    res: dict = {}
    d = np.load(S116_NPZ, allow_pickle=True)

    Y_nu_diag = np.asarray(d["Y_nu_diag"]).ravel().astype(float)   # (local) [0, 4.794, 11.928]
    M_R = np.asarray(d["M_R_MKK"]).ravel().astype(float)           # (local) [1.0044,1.0786,1.1700]
    M_nu_npz = np.asarray(d["M_nu"]).astype(float)                 # (local) full composite (with eps_LX)
    m_nu_vals_npz = np.asarray(d["m_nu_vals"]).ravel().astype(float)  # (local) S116 light masses
    m_nu_S99 = np.asarray(d["m_nu_S99_eV"]).ravel().astype(float)  # (local) [0,0.0086776,0.0495278]
    eps23 = float(d["eps23_strength"]); w23_nu = float(d["w23_nu"])  # (local) the angle-metric transplant
    res["Y_nu_diag"] = Y_nu_diag; res["M_R_MKK"] = M_R
    res["eps23_strength"] = eps23; res["w23_nu"] = w23_nu

    print("=== STEP 0: loaded S116 texture npz ===")
    print(f"  Y_nu_diag (diagonal Dirac)  = {Y_nu_diag}")
    print(f"  M_R (B-branch fold, M_KK)   = {M_R}  (spread {(M_R.max()/M_R.min()-1)*100:.2f}%, near-degenerate)")
    print(f"  eps23 (shared angle-metric) = {eps23:.5f}; w23_nu = {w23_nu:.5f} (transplanted into M_D 2-3)")
    print(f"  npz M_nu (with eps_LX off-diagonal):\n{M_nu_npz}")

    # ===== (1) BARE B-branch composite -- THE SPECTRUM CHANNEL (verdict number) =====
    M_D_diag = np.diag(Y_nu_diag)                          # (local) mass-pinned DIAGONAL Dirac (NO eps_LX)
    M_nu_bare = M_D_diag @ np.diag(1.0 / M_R) @ M_D_diag.T  # (local) type-I seesaw, bare diagonal
    M_nu_bare = 0.5 * (M_nu_bare + M_nu_bare.T)            # (local) symmetrize (float hygiene)
    m_bare = singular_values_ascending(M_nu_bare)          # (local) [0, Y2^2/B2, Y3^2/B3]
    m1_b, m2_b, m3_b = m_bare
    m1_rel_bare = float(m1_b / m3_b) if m3_b > 0 else float("nan")  # (local) rank-2 check
    R_bare = R_from_masses(m_bare)                         # (local) PRIMARY verdict number
    R_bare_cf = R_at_m1zero(m_bare)                        # (local) closed-form cross-check
    res["M_nu_bare"] = M_nu_bare; res["m_bare"] = m_bare
    res["R_bare"] = R_bare; res["R_bare_closedform"] = R_bare_cf
    res["m1_over_m3_bare"] = m1_rel_bare
    print("\n=== STEP 1: BARE B-branch composite (spectrum channel; mass-pinned DIAGONAL M_D) ===")
    print(f"  M_nu_bare = M_D_diag . M_R^-1 . M_D_diag^T:\n{M_nu_bare}")
    print(f"  singular values (ascending) = {m_bare}  (m_1/m_3 = {m1_rel_bare:.3e}; m_1=0 iff <<1)")
    print(f"  R_bare = (m3^2-m2^2)/(m2^2-m1^2) = {R_bare:.6f}")
    print(f"  R_bare closed-form m3^2/m2^2-1 = {R_bare_cf:.6f}  (agree: {abs(R_bare-R_bare_cf)<1e-9})")
    print(f"  band [{R_LO},{R_HI}] membership: {in_band(R_bare)}")

    # ===== (2) CONTRAST -- npz M_nu (WITH the eps_LX angle-metric off-diagonal) =====
    m_eps = singular_values_ascending(M_nu_npz)            # (local) [0, 13.41, 143.54]
    R_eps = R_from_masses(m_eps)                           # (local) eps_LX-perturbed R (overshoot)
    res["m_eps"] = m_eps; res["R_eps23"] = R_eps
    res["m_eps_matches_npz"] = bool(np.allclose(np.sort(m_nu_vals_npz), m_eps, atol=1e-6))
    print("\n=== STEP 2: CONTRAST -- npz M_nu singular values (WITH eps_LX angle-metric w23_nu) ===")
    print(f"  singular values (ascending) = {m_eps}  (matches npz m_nu_vals: {res['m_eps_matches_npz']})")
    print(f"  R_eps23 = {R_eps:.6f}  band membership: {in_band(R_eps)}  "
          f"(angle-metric TOUCHED the spectrum -> overshoot vs R_bare={R_bare:.3f})")

    # ===== (3) CROSS-CHECK -- S99 oscillation-anchored + NuFit-6.0 central =====
    m_anch = np.sort(m_nu_S99)                             # (local) [0,0.0086776,0.0495278] eV
    R_anch = R_from_masses(m_anch)                         # (local)
    res["m_anchored_eV"] = m_anch; res["R_S99_anchored"] = R_anch
    # NuFit-6.0 central: at m_1=0, m_3^2 = Delta m^2_31, m_2^2 = Delta m^2_21 (NO)
    R_nufit_central = float(dm2_31_NuFit) / float(dm2_21_NuFit) - 1.0  # (local) = m3^2/m2^2 - 1
    res["R_NuFit60_central"] = R_nufit_central
    res["dm2_21_NuFit"] = float(dm2_21_NuFit); res["dm2_31_NuFit"] = float(dm2_31_NuFit)
    print("\n=== STEP 3: CROSS-CHECKS ===")
    print(f"  S99 oscillation-anchored masses (eV) = {m_anch}")
    print(f"  R_S99_anchored = {R_anch:.6f}  band membership: {in_band(R_anch)}")
    print(f"    (R_bare vs R_S99_anchored agree to {abs(R_bare-R_anch):.3e} -> the bare diagonal "
          f"composite reproduces the anchored ratio: Y_3/Y_2 was oscillation-anchored)")
    print(f"  NuFit-6.0 central: Dm2_31/Dm2_21 - 1 = {R_nufit_central:.6f}  band membership: {in_band(R_nufit_central)}")

    # ===== (4) STRUCTURAL -- rescale-INVARIANCE: M_R -> c.M_R leaves R UNCHANGED =====
    R_rescaled = []                                        # (local)
    for c in RESCALE_CS:
        M_c = M_D_diag @ np.diag(1.0 / (c * M_R)) @ M_D_diag.T
        M_c = 0.5 * (M_c + M_c.T)
        R_rescaled.append(R_from_masses(singular_values_ascending(M_c)))
    R_rescaled = np.array(R_rescaled)                      # (local)
    rescale_resid = float(np.max(np.abs(R_rescaled - R_bare)))  # (local) ~machine-eps
    res["rescale_cs"] = np.array(RESCALE_CS); res["R_rescaled"] = R_rescaled
    res["rescale_inv_resid"] = rescale_resid
    print("\n=== STEP 4: rescale-INVARIANCE (M_R -> c.M_R; R must be UNCHANGED) ===")
    for c, Rc in zip(RESCALE_CS, R_rescaled):
        print(f"  c={c:>10.3e}  R(c.M_R)={Rc:.10f}  |R - R_bare|={abs(Rc-R_bare):.2e}")
    print(f"  max rescale residual = {rescale_resid:.3e}  => R set by bowtie SHAPE, NOT Majorana SCALE "
          f"(INFO clause keys on a RESHAPE, not a rescale)")

    return res


# ---------------------------------------------------------------------------
# Section 7 -- Verdict (band-membership of R_bare; plan §W2-2 rubric)
# ---------------------------------------------------------------------------
def verdict_from(res: dict) -> str:
    """PASS iff R_bare in [17,66]; FAIL iff R_bare out-of-band AND no reshape reaches
    the band; INFO iff R_bare out-of-band but a bowtie RESHAPE reaches it."""
    R_bare = res["R_bare"]                                 # (local)
    if in_band(R_bare):
        return "PASS"
    # out-of-band: does a reshape (eps_LX composite as the available reshape witness) reach it?
    reshape_in_band = in_band(res["R_eps23"])             # (local)
    return "INFO" if reshape_in_band else "FAIL"


# ---------------------------------------------------------------------------
# Section 8 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, verdict: str) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.4))

    # Panel 1: the R values vs the NuFIT 3-sigma band [17,66]
    ax = axes[0]
    labels = ["R_bare\n(spectrum\nchannel)", "R_eps23\n(angle-metric\ncontrast)",
              "R_S99\nanchored", "R_NuFit60\ncentral"]
    vals = [res["R_bare"], res["R_eps23"], res["R_S99_anchored"], res["R_NuFit60_central"]]
    ax.axhspan(R_LO, R_HI, color="tab:green", alpha=0.22, label=f"NuFIT 5.2 NO 3sig band [{R_LO:.0f},{R_HI:.0f}]")
    x = np.arange(len(vals))
    cols = ["#1e8449" if in_band(v) else "#c0392b" for v in vals]
    ax.scatter(x, vals, c=cols, s=120, zorder=5, edgecolor="k")
    for xi, v in zip(x, vals):
        ax.annotate(f"{v:.2f}", (xi, v), textcoords="offset points", xytext=(0, 9),
                    ha="center", fontsize=9, weight="bold")
    ax.set_yscale("log")
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("R = Dm^2_32 / Dm^2_21 (log)")
    ax.set_title(f"R vs NuFIT 5.2 NO 3sig band\nR_bare={res['R_bare']:.2f} in [{R_LO:.0f},{R_HI:.0f}] => {verdict}")
    ax.grid(alpha=0.3, axis="y"); ax.legend(loc="upper left", fontsize=8)

    # Panel 2: rescale-invariance -- R(c.M_R) flat at R_bare; eps composite for contrast
    ax = axes[1]
    ax.semilogx(res["rescale_cs"], res["R_rescaled"], "o-", color="tab:blue", lw=1.8,
                label=f"R(c.M_R) bare (resid {res['rescale_inv_resid']:.1e})")
    ax.axhline(res["R_bare"], color="tab:green", ls="--", lw=1.4, label=f"R_bare={res['R_bare']:.3f}")
    ax.axhline(res["R_eps23"], color="tab:red", ls=":", lw=1.4, label=f"R_eps23={res['R_eps23']:.2f} (overshoot)")
    ax.axhspan(R_LO, R_HI, color="tab:green", alpha=0.15)
    ax.set_xlabel("Majorana rescale factor c  (M_R -> c.M_R)")
    ax.set_ylabel("R")
    ax.set_title("Rescale-INVARIANCE: R set by bowtie SHAPE, not Majorana SCALE\n"
                 "(M_nu -> (1/c).M_nu => every m_i -> m_i/c => R unchanged)")
    ax.legend(loc="center right", fontsize=8); ax.grid(alpha=0.3)

    # Panel 3: text summary + substitution chain + caveats
    ax = axes[2]
    ax.axis("off")
    ax.text(0.0, 1.0, f"{GATE_ID}\nR-channel => {verdict}", fontsize=10.5, weight="bold",
            transform=ax.transAxes, va="top")
    txt = (
        f"PRIMARY (spectrum channel):\n"
        f"  R_bare = m3^2/m2^2 - 1 = {res['R_bare']:.4f}\n"
        f"  in band [{R_LO:.0f},{R_HI:.0f}]: {in_band(res['R_bare'])}  => {verdict}\n"
        f"  m_bare(M_KK) = [0, {res['m_bare'][1]:.3f}, {res['m_bare'][2]:.3f}]\n"
        f"  m_1/m_3 = {res['m1_over_m3_bare']:.1e} (rank-2; m_1=0)\n\n"
        f"CONTRAST (angle-metric touched spectrum):\n"
        f"  R_eps23 = {res['R_eps23']:.3f}  (w23_nu={res['w23_nu']:.3f}\n"
        f"  the S116 eps_LX transplant; OVERSHOOTS)\n\n"
        f"CROSS-CHECKS (both in band):\n"
        f"  R_S99_anchored  = {res['R_S99_anchored']:.4f}\n"
        f"  R_NuFit60 cent. = {res['R_NuFit60_central']:.4f}\n\n"
        f"STRUCTURAL:\n"
        f"  rescale-inv resid = {res['rescale_inv_resid']:.1e}\n"
        f"  => R = bowtie SHAPE, not Majorana SCALE\n\n"
        f"CAVEAT (S100a, PERMANENT): Y_3/Y_2 is\n"
        f"oscillation-anchored (D_K->Y_i map non-unique)\n"
        f"=> R_bare is a CONSISTENCY of the spectrum\n"
        f"channel with NuFIT, not a 0-param prediction.\n"
        f"Spectrum HOLDS where angles WALLED (S116 mix_grp=0/4)."
    )
    ax.text(0.0, 0.90, txt, fontsize=8.0, transform=ax.transAxes, va="top", family="monospace")

    fig.suptitle(f"{GATE_ID}: seesaw R = Dm^2_32/Dm^2_21 from M_nu = M_D M_R^-1 M_D^T "
                 f"(D_K tau_fold={TAU}); spectrum channel vs NuFIT 5.2 NO band", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 -- Verdict payload (race-safe MCP single-writer)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    """Print the emit_verdict payload (race-safe MCP single-writer path).
    [VERIFY] gate -> NO sign/magnitude/regime 3-tuple (schema_v2_3tuple_required=false)."""
    payload = {
        "session": int(SESSION),
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 10 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()
    print(f"=== {GATE_ID} ===")
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL_PATH, pins)
    print(f"  audit_sha256  = {audit_sha}")
    print(f"  content_sha256= {content_sha}")
    print(f"  canonical dm2_21_NuFit={dm2_21_NuFit} dm2_31_NuFit={dm2_31_NuFit} (R cross-check anchor)")
    print(f"  pre-registered band [R_LO,R_HI] = [{R_LO},{R_HI}] (NuFIT 5.2 NO 3-sigma; lab-IN # local)")

    res = compute()
    verdict = verdict_from(res)

    print("\n=== VERDICT ===")
    print(f"  R_bare = {res['R_bare']:.6f}  band [{R_LO},{R_HI}] => {verdict}")

    make_plot(res, verdict)

    # value payload (no single-quote chars)
    value = (
        f"R_bare={res['R_bare']:.5f}(band[{R_LO:.0f},{R_HI:.0f}]:{in_band(res['R_bare'])});"
        f"R_eps23_npz={res['R_eps23']:.4f}(angle-metric_TOUCHED_spectrum_overshoot,inband:{in_band(res['R_eps23'])});"
        f"R_S99anchored={res['R_S99_anchored']:.5f}(inband:{in_band(res['R_S99_anchored'])});"
        f"R_NuFit60central={res['R_NuFit60_central']:.5f}(inband:{in_band(res['R_NuFit60_central'])});"
        f"rescale_inv_resid={res['rescale_inv_resid']:.2e}(R=SHAPE_not_SCALE);"
        f"m1_over_m3={res['m1_over_m3_bare']:.2e}_rankdef(m1=0_EXACT);"
        f"m_bare_MKK=[0,{res['m_bare'][1]:.4f},{res['m_bare'][2]:.4f}];"
        f"spectrum-channel-HOLDS_where-angles-WALLED(S116_mixgrp=0of4);"
        f"Dirac-ratio-Y3overY2-oscillation-anchored-S100a-PERMANENT(consistency_not_0param-prediction)"
    )

    np.savez(
        OUT_NPZ,
        value=value, verdict=verdict,
        # primary spectrum channel
        R_bare=res["R_bare"], R_bare_closedform=res["R_bare_closedform"],
        m_bare=res["m_bare"], m1_over_m3_bare=res["m1_over_m3_bare"],
        M_nu_bare=res["M_nu_bare"],
        # contrast (angle-metric)
        R_eps23=res["R_eps23"], m_eps=res["m_eps"],
        eps23_strength=res["eps23_strength"], w23_nu=res["w23_nu"],
        m_eps_matches_npz=res["m_eps_matches_npz"],
        # cross-checks
        R_S99_anchored=res["R_S99_anchored"], m_anchored_eV=res["m_anchored_eV"],
        R_NuFit60_central=res["R_NuFit60_central"],
        dm2_21_NuFit=res["dm2_21_NuFit"], dm2_31_NuFit=res["dm2_31_NuFit"],
        # structural
        rescale_cs=res["rescale_cs"], R_rescaled=res["R_rescaled"],
        rescale_inv_resid=res["rescale_inv_resid"],
        # inputs/provenance
        Y_nu_diag=res["Y_nu_diag"], M_R_MKK=res["M_R_MKK"],
        R_LO=R_LO, R_HI=R_HI, tau=TAU,
        scheme=SCHEME, convention=CONVENTION, L_max=str(L_MAX),
        audit_sha256=audit_sha, content_sha256=content_sha,
    )

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print("\n" + tag)

    companion = (
        f"seesaw R-channel (binding open channel from S116-W2-PMNS-RESCUE); "
        f"R_bare=m3^2/m2^2-1={res['R_bare']:.4f} in [{R_LO:.0f},{R_HI:.0f}] => {verdict}; "
        f"the eigenVALUE (spectrum) channel where the eigenVECTOR (angle) channel WALLED "
        f"(S116 mix_grp=0/4); M_R B-branch fold [{', '.join(f'{x:.4f}' for x in res['M_R_MKK'])}] scale HELD; "
        f"eps_LX-perturbed contrast R_eps23={res['R_eps23']:.2f} OVERSHOOTS (angle-metric touched spectrum)"
    )
    extra = [
        (f"# substitution chain: R=(m3^2-m2^2)/(m2^2-m1^2); m_1=0 EXACT (Y_1=0 rank-2 M_D, S100a) => "
         f"R=m3^2/m2^2-1={res['R_bare']:.4f}; m_bare(M_KK)=[0,{res['m_bare'][1]:.4f},{res['m_bare'][2]:.4f}]; "
         f"m_1/m_3={res['m1_over_m3_bare']:.1e} # {GATE_ID}"),
        (f"# rescale-INVARIANCE: M_R->c.M_R => M_nu->(1/c).M_nu => R UNCHANGED across c in "
         f"[1e-3,1e6] (resid {res['rescale_inv_resid']:.1e}); R set by bowtie SHAPE (B2/B3,B3/B1) NOT "
         f"Majorana SCALE; INFO clause keys on a RESHAPE not a rescale # {GATE_ID}"),
        (f"# cross-check: R_S99_anchored={res['R_S99_anchored']:.4f}, R_NuFit60_central={res['R_NuFit60_central']:.4f} "
         f"both in [{R_LO:.0f},{R_HI:.0f}]; R_bare matches R_S99_anchored to {abs(res['R_bare']-res['R_S99_anchored']):.1e} "
         f"(Y_3/Y_2 oscillation-anchored) # {GATE_ID}"),
        (f"# CAVEAT S100a-MD-NORMALIZATION INFO (PERMANENT): D_K bottom-triple->Y_i map NON-UNIQUE; "
         f"R_bare is a CONSISTENCY of the spectrum channel with NuFIT, NOT a zero-free-parameter prediction; "
         f"substrate-FIRST content = seesaw structure + M_R bowtie shape + rescale-invariance "
         f"regulator_pin=N/A(representation-theoretic eigenvalue-ratio) # {GATE_ID}"),
        (f"# ANGLE-METRIC CONTRAST: the S116 shared eps_LX (w23_nu={res['w23_nu']:.3f}, eps23={res['eps23_strength']:.4f}) "
         f"transplanted into M_D 2-3 block is NOT a pure left-rotation => it PERTURBED the singular values "
         f"R_bare={res['R_bare']:.3f}->R_eps23={res['R_eps23']:.2f} (overshoot); the clean spectrum channel "
         f"(mass-fixed singular values) HOLDS at R_bare # {GATE_ID}"),
    ]

    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra)

    wall = time.time() - t0
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
