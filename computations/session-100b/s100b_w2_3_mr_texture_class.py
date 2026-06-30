#!/usr/bin/env python3
"""
S100b W2-3 — S100b-MR-TEXTURE-CLASS — M_R two-zero texture classification (Ma/Xu/Zhao Eq. 8)
=============================================================================================

Gate: S100b-MR-TEXTURE-CLASS ([VERIFY])   Classification: PARTICLE
Plan: sessions/session-plan/session-100b-plan-w2.md §W2-3 (R3 gate block)

Pre-registered operator (set-membership over a discrete phase grid AND phase-region
consistency):
  match(g) = the unique survivor class whose zero-position set EQUALS
             {(i,j) : z_ij(g) < eps_texture} for phase grid point g in {0,pi}^3.
  PASS iff exists g with match(g) = exactly one class in {A1, A2, B3, B4, B6}
           AND the matched class's paper-08 3-sigma phase region contains g.
  INFO iff exists g with a unique class match but NO matched class admits a
           {0,pi}^3 point in its 3-sigma phase region (phase conflict).
  FAIL iff no grid point yields any survivor-class zero pattern at eps = 1e-10.

Construction (s60-pinned Majorana congruence; route-(a) scope — all PMNS mixing
carried by the heavy sector, m_D diagonal per the s99 npz, m_D[0] = 0 exactly
(S62 rank-1 Yukawa, m_1 = 0 EXACT)):
  M_R^flavor = U^T . diag(M_R_GeV) . U          (congruence, NOT conjugation)
  U = R_23(th23) . R_13(th13, delta) . R_12(th12) . P(rho, sigma),
  P = diag(1, e^{i rho}, e^{i sigma})           (PDG PMNS parameterization)

SECTOR-CONFLATION GUARD (MANDATORY, dirac G3 flag): the substrate PMNS Dirac-phase
set is {0, pi} (canonical delta_CP_PMNS_substrate sector; S99-W3-SEESAW-SUMMNU
verdict delta_CP=[0,pi]). The K_7 transit phase pi/2 (phi_CP_K7_transit) is the
BARYOGENESIS-sector phase (S98-W3-2 CLOSED-SOURCED-UNIQUE) and MUST NOT enter the
grid; it is asserted absent below. The numerical coincidence d(1.5pi, {0,pi}) =
pi/2 = phi_CP_K7_transit is NOT imported as a leptonic-phase match.

Inputs (SHA-256 dual-pinned; plan-freeze static pins asserted at runtime):
  - computations/session-99/s99_w3_seesaw_summnu.npz                (M_R fold energies)
  - downloads/research-sweep-s99/neutrino-mass-seesaw/08_Ma-Xu-Zhao_*.pdf  (Eq. 8 patterns)
  - downloads/research-sweep-s99/neutrino-mass-seesaw/01_Esteban_NuFit-6.0*.pdf (angles)
  - computations/_shared/canonical_constants.py  (delta_CP_PMNS_substrate,
    phi_CP_K7_transit, dm2_21_NuFit, dm2_31_NuFit)

Output 4-tuple:
  (value=<membership result>, scheme=MXZ-Eq8-two-zero,
   convention=UT-MR-U-congruence-PDG-PMNS-NuFit60, L_max=<inherited from s99 npz>)

METHODOLOGY
-----------
The M_3(C)-derived heavy Majorana matrix M_R (substrate-IS: B-branch D_K fold
energies, S99 seesaw PASS) is rotated to the Ma/Xu/Zhao classification basis over
the exhaustive discrete CP grid (delta, rho, sigma) in {0,pi}^3 (8 points; Majorana
phases inherit {0,pi} from the CP-conserving constraint, dirac G3 litrev II.5).
Texture zeros are tested at the pre-registered machine-epsilon-class threshold
z_ij < 1e-10 on the normalized modulus, and the resulting zero-position sets are
compared (exact set equality) against the five MXZ Eq.-8 survivor classes
{A1, A2, B3, B4, B6}, with the class patterns EXTRACTED FROM THE SHA-PINNED PDF AT
RUNTIME (training-knowledge texture labels FORBIDDEN — labeling conventions differ
across the literature). Diagnostics (NOT gate-bearing): near-zero scan at
eps in {1e-6, 1e-3, 3e-2}; NuFIT-5.2 vintage-robustness re-run at the
paper-08-stated Table-1 inputs; m_1 = 0 EXACT annotation against the matched
class's implied lightest mass; per-class phase-region distances.

STRUCTURAL LEMMAS (verified numerically below; the Dirac-methodology content)
------------------------------------------------------------------------------
L1 (Majorana-phase transparency of modulus textures): with U = R(theta, delta) P,
   P diagonal unimodular, (U^T D U)_ij = P_ii (R^T D R)_ij P_jj, so
   |M_R^flavor,ij| = |(R^T D R)_ij| — INDEPENDENT of (rho, sigma) for ALL values,
   and independent of the Majorana-phase-matrix convention (PDG diag(1,e^ir,e^is)
   vs paper-08 diag(e^ir,e^is,1) — they differ by an overall rephasing that the
   modulus kills). The pattern axis sees only (theta_ij, delta).
L2 (CP-conserving diagonal-zero obstruction): at (delta,rho,sigma) in {0,pi}^3, U
   is REAL ORTHOGONAL, so (M_R^flavor)_ii = sum_k M_k U_ki^2 with U_ki^2 >= 0,
   sum_k U_ki^2 = 1: a CONVEX COMBINATION of the fold energies, bounded in
   [M_1, M_3]. Hence z_ii >= M_1 / M_3 (since max|M_kl| <= M_3 by Cauchy-Schwarz).
   ALL FIVE survivor classes carry at least one DIAGONAL zero, so no class can
   match at ANY CP-conserving point for ANY positive heavy spectrum: the FAIL is
   analytically forced, not merely generic. (Diagonal zeros require complex
   cancellation — exactly why the MXZ B-classes live at delta ~ 1.5pi,
   rho ~ sigma ~ pi/2: the phase-grid restriction and the texture obstruction are
   the same algebraic fact viewed twice.)

DISCIPLINE
----------
- `from canonical_constants import *`; intermediates tagged `# (local)`
- cpu-cap-OMP8 (3x3 complex algebra x 8 grid points; GPU pointless at this size)
- SHA-256 of all inputs logged in first 20 lines of stdout; S84+ dual-SHA emitted
- Verdict via the race-safe `emit_verdict` knowledge-MCP tool: this script PRINTS
  the payload (print_verdict_payload) and NEVER open("a")'s the verdict file.
- Exit code reflects script health ONLY (PASS/FAIL/INFO are data).
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (plan pin: cpu-cap-OMP8) -------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
# consumed: delta_CP_PMNS_substrate, phi_CP_K7_transit, dm2_21_NuFit, dm2_31_NuFit

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import itertools
import json
import re
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pypdf import PdfReader

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration (ALL pins fixed BEFORE compute)
# ---------------------------------------------------------------------------
SESSION = "100b"
GATE_ID = "S100b-MR-TEXTURE-CLASS"
SCHEME = "MXZ-Eq8-two-zero"
CONVENTION = "UT-MR-U-congruence-PDG-PMNS-NuFit60"
TRIGGER = "[VERIFY]"

# Pre-registered thresholds (plan §W2-3 items (1)/(2)/(5); plan-pinned per-gate
# values — the plan block is the pre-registration authority, tags are audit-scope)
EPS_TEXTURE = 1e-10                  # (local) plan-pinned gate-bearing texture-zero threshold on z_ij
EPS_DIAGNOSTIC = (1e-6, 1e-3, 3e-2)  # diagnostic near-zero rails (NOT gate-bearing)
UNITARITY_TOL = 1e-12                # (local) plan-pinned ||U^dag U - 1||_max per congruence
CONSISTENCY_TOL = 1e-12              # (local) plan-pinned npz delta_CP_allowed vs canonical sector set
DRIFT_BOUND = 0.02                   # (local) plan-pinned NuFit-6.0 angle drift detector (abs, per angle)
TOL_REGION = np.pi / 4               # encoded reading of paper-08 "close to/around";
#   raw phase distances are reported so the containment conclusion is
#   tolerance-independent for any tol < pi/2 (see Chain 2).
SURVIVOR_SET = {"A1", "A2", "B3", "B4", "B6"}  # plan-pinned survivor-class names

# Plan-freeze provisional NuFit-6.0 floats — drift detector ONLY (plan §W2-3 nufit_pins)
PROVISIONAL_NUFIT60 = {"s2_12": 0.308, "s2_13": 0.02215, "s2_23": 0.470}

# Plan-freeze static input SHA pins (Input-SHA Ledger, session-100b-plan-w2.md)
SHA_PIN_S99_NPZ = "48e53bc69868272cdc012d76c8127349c31f611ea08c7d233d5ed973fe83f711"
SHA_PIN_PAPER08 = "3229fffbf7c13ebe165f17be38784f51ef20eba4374ae7d2677d0367b36ccb6a"
SHA_PIN_NUFIT60 = "66ff020fea48d04fe703e99559d625ed3d0bacfc36cbf619b8df16652d54194f"

P_S99_NPZ = PROJECT_ROOT / "computations/session-99/s99_w3_seesaw_summnu.npz"
P_PAPER08 = PROJECT_ROOT / ("downloads/research-sweep-s99/neutrino-mass-seesaw/"
                            "08_Ma-Xu-Zhao_Two-Zero-Majorana-MR-Textures-Leptogenesis.pdf")
P_NUFIT60 = PROJECT_ROOT / ("downloads/research-sweep-s99/neutrino-mass-seesaw/"
                            "01_Esteban_NuFit-6.0-Global-Oscillation-Fit.pdf")
P_CANON = SHARED_DIR / "canonical_constants.py"

OUT_NPZ = SESSION_DIR / "s100b_w2_3_mr_texture_class.npz"
OUT_PNG = SESSION_DIR / "s100b_w2_3_mr_texture_class.png"

INPUT_FILES = [P_CANON, P_S99_NPZ, P_PAPER08, P_NUFIT60]

# Methodology pinmap — feeds audit_sha256 (plan audit_discriminators: "pinmap
# (construction, phase grid, eps_texture, nufit_pins, scope_pin)")
METHODOLOGY_PINMAP = {
    "construction": "M_R^flavor = U^T . diag(M_R_GeV) . U (s60 congruence pin; NOT conjugation)",
    "pmns_parameterization": "PDG: U = R_23(th23) R_13(th13,delta) R_12(th12) . diag(1, e^{i rho}, e^{i sigma})",
    "phase_grid": "(delta, rho, sigma) in {0, pi}^3 exhaustive 8 points; delta set = delta_CP_PMNS_substrate sector {0,pi}; phi_CP_K7_transit=pi/2 EXCLUDED (baryogenesis sector)",
    "eps_texture": EPS_TEXTURE,
    "eps_diagnostic": list(EPS_DIAGNOSTIC),
    "nufit_pins": "angles AS PRINTED in SHA-pinned NuFit-6.0 PDF, IC24-with-SK-atm NO best-fit column; provisional floats (0.308, 0.02215, 0.470) drift detector at 0.02; dm2 from canonical_constants (dm2_21_NuFit, dm2_31_NuFit, NuFit-6.0 vintage)",
    "scope_pin": "route-(a) ONLY: all PMNS mixing in M_R; m_D diagonal per s99 npz (m_D[0]=0 exact, S62 rank-1 Yukawa); m_D-carried mixing OUT OF SCOPE -> S100a-MD-NORMALIZATION",
    "pattern_source": "paper-08 Eq. 8 zero-position sets extracted from SHA-pinned PDF at runtime; training-knowledge labels FORBIDDEN",
    "survivor_set": sorted(SURVIVOR_SET),
    "unitarity_tol": UNITARITY_TOL,
    "consistency_tol": CONSISTENCY_TOL,
    "tol_region": "pi/4 (raw distances reported; conclusion tol-independent for tol < pi/2)",
}


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """S84+ dual-SHA: audit = sha256(script || canonical || pinmap_json);
    content = sha256(script). pinmap_json covers input-file SHAs AND the
    methodology pinmap (construction / phase grid / eps / nufit / scope)."""
    script_bytes = script_path.read_bytes()      # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    full_pins = dict(pins)  # (local)
    full_pins["PINMAP::methodology"] = hashlib.sha256(
        json.dumps(METHODOLOGY_PINMAP, separators=(",", ":"), sort_keys=True).encode()
    ).hexdigest()
    pinmap_json = json.dumps(dict(sorted(full_pins.items())),
                             separators=(",", ":"), sort_keys=True).encode()  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Runtime PDF extraction (SHA-pinned sources ONLY)
# ---------------------------------------------------------------------------

def pdf_text(path: Path) -> str:
    r = PdfReader(str(path))  # (local)
    txt = "\n".join(pg.extract_text() for pg in r.pages)  # (local)
    return txt.replace("−", "-")  # normalize unicode minus


def extract_eq8_patterns(text: str) -> dict:
    """Extract the five MXZ Eq.-8 two-zero M_R survivor patterns from paper-08.

    Returns {class_name: frozenset of 1-based upper-triangle (i,j) zero positions}.
    Consistency checks: exactly 5 classes; names == SURVIVOR_SET; each pattern
    symmetric with exactly 2 independent zeros; patterns pairwise distinct.
    """
    m = re.search(r"correspond to the following two-zero textures of\s*M\s*R\s*:(.*?)\.\s*\(8\)",
                  text, re.S)
    if m is None:
        raise RuntimeError("paper-08 Eq. 8 block not found — extraction anchor missing")
    block = m.group(1)  # (local)
    labels = list(re.finditer(r"([AB])\s*([0-9])\s*:\s*M\s*R\s*=", block))  # (local)
    patterns = {}  # (local)
    cross_chars = {"×", "*"}  # (local) — pypdf renders the paper's entry-cross as U+00D7
    for k, lm in enumerate(labels):
        name = lm.group(1) + lm.group(2)  # (local)
        seg = block[lm.end(): labels[k + 1].start() if k + 1 < len(labels) else len(block)]  # (local)
        syms = [ch for ch in seg if ch in cross_chars or ch == "0"]  # (local)
        if len(syms) != 9:
            raise RuntimeError(f"class {name}: expected 9 matrix symbols, got {len(syms)}: {syms}")
        zeros = set()  # (local)
        for idx, ch in enumerate(syms):
            r_, c_ = divmod(idx, 3)  # (local)
            if ch == "0":
                zeros.add((r_ + 1, c_ + 1))
        # symmetry of the full zero set
        if any((j, i) not in zeros for (i, j) in zeros):
            raise RuntimeError(f"class {name}: extracted zero set not symmetric: {sorted(zeros)}")
        indep = frozenset((i, j) for (i, j) in zeros if i <= j)  # (local)
        if len(indep) != 2:
            raise RuntimeError(f"class {name}: expected 2 independent zeros, got {sorted(indep)}")
        patterns[name] = indep
    if set(patterns) != SURVIVOR_SET:
        raise RuntimeError(f"extracted classes {sorted(patterns)} != survivor set {sorted(SURVIVOR_SET)}")
    if len({p for p in patterns.values()}) != 5:
        raise RuntimeError("survivor patterns not pairwise distinct")
    return patterns


def extract_paper08_table1_NO(text: str) -> dict:
    """Paper-08 Table 1, Normal-Ordering best-fit column (the paper's stated
    global-fit inputs — NuFIT-5.2 era; used ONLY for the vintage-robustness
    diagnostic re-run)."""
    out = {}  # (local)
    out["s2_12"] = float(re.search(r"sin2\s*θ\s*12\s*([0-9]+\.[0-9]+)", text).group(1))
    out["s2_23"] = float(re.search(r"sin2\s*θ\s*23\s*([0-9]+\.[0-9]+)", text).group(1))
    out["s2_13"] = float(re.search(r"sin2\s*θ\s*13\s*([0-9]+\.[0-9]+)", text).group(1))
    out["dm2_21"] = float(re.search(r"m2\s*21/\(10-5\s*eV2\)\s*([0-9]+\.[0-9]+)", text).group(1)) * 1e-5
    out["dm2_3l"] = float(re.search(r"m2\s*3ℓ/\(10-3\s*eV2\)\s*([0-9]+\.[0-9]+)", text).group(1)) * 1e-3
    return out


def extract_paper08_class_predictions(text: str) -> dict:
    """Phrase-anchored extraction of the per-class 3-sigma-preferred phase/mass
    predictions from paper-08 §2 (the Figure-1/Figure-2 region statements).
    Every numeric is pulled from the matched phrase — never from training
    knowledge."""
    t = re.sub(r"\s+", " ", text)  # (local) normalize whitespace
    mA = re.search(r"m\s*1 is predicted to be around ([0-9.]+) eV,\s*while\s*δ\s*is allowed to span a wide range from\s*π\s*to (\d)π", t)
    mB = re.search(r"the lightest neutrino mass is predicted to be close to ([0-9.]+) eV,\s*while\s*δ\s*is close to ([0-9.]+)π", t)
    mAr = re.search(r"ρ\s*and\s*σ\s*satisfy the relations\s*ρ\s*∼\s*σ\s*\+\s*π/2 or\s*σ\s*∼\s*ρ\s*\+\s*π/2", t)
    mBr = re.search(r"ρ\s*and\s*σ\s*are both predicted to be around\s*π/2", t)
    if not (mA and mB and mAr and mBr):
        raise RuntimeError("paper-08 per-class phase/mass prediction phrases not found "
                           f"(A:{bool(mA)} B:{bool(mB)} Arel:{bool(mAr)} Brel:{bool(mBr)})")
    return {
        "A_m_lightest_eV": float(mA.group(1)),               # ~0.005
        "A_delta_range": (np.pi, float(mA.group(2)) * np.pi),  # [pi, 2pi]
        "A_majorana_rel_offset": np.pi / 2,                   # rho ~ sigma +- pi/2
        "B_m_lightest_eV": float(mB.group(1)),                # ~0.1
        "B_delta_pref": float(mB.group(2)) * np.pi,           # 1.5*pi
        "B_rho_sigma_pref": np.pi / 2,                        # rho, sigma ~ pi/2
    }


def extract_nufit60_NO(text: str) -> dict:
    """NuFit-6.0 Table 1, 'IC24 with SK atmospheric data' variant, Normal-Ordering
    (best fit) column — the gate-bearing mixing angles AS PRINTED in the
    SHA-pinned PDF. dm2 rows extracted for canonical-constant vintage assert."""
    idx = text.find("IC24 with SK atmospheric data")  # (local)
    if idx < 0:
        raise RuntimeError("NuFit-6.0 'IC24 with SK atmospheric data' anchor not found")
    sl = text[idx: idx + 3000]  # (local)
    if "Normal Ordering (best fit)" not in sl[:200]:
        raise RuntimeError("NuFit-6.0 IC24-with-SK NO-best-fit header not where expected")
    out = {}  # (local)
    out["s2_12"] = float(re.search(r"sin2\s*θ\s*12\s*([0-9]+\.[0-9]+)", sl).group(1))
    out["s2_23"] = float(re.search(r"sin2\s*θ\s*23\s*([0-9]+\.[0-9]+)", sl).group(1))
    out["s2_13"] = float(re.search(r"sin2\s*θ\s*13\s*([0-9]+\.[0-9]+)", sl).group(1))
    out["dm2_21"] = float(re.search(r"m2\s*21\s*10-5\s*eV2\s*([0-9]+\.[0-9]+)", sl).group(1)) * 1e-5
    out["dm2_3l"] = float(re.search(r"m2\s*3ℓ\s*10-3\s*eV2\s*\+?([0-9]+\.[0-9]+)", sl).group(1)) * 1e-3
    return out


# ---------------------------------------------------------------------------
# Section 6 — PMNS construction + classification machinery
# ---------------------------------------------------------------------------

def build_U(s2_12: float, s2_13: float, s2_23: float,
            delta: float, rho: float, sigma: float,
            majorana_convention: str = "PDG") -> np.ndarray:
    """PDG PMNS: U = R_23(th23) . R_13(th13, delta) . R_12(th12) . P.
    majorana_convention 'PDG'   : P = diag(1, e^{i rho}, e^{i sigma})   (plan pin)
    majorana_convention 'MXZ'   : P = diag(e^{i rho}, e^{i sigma}, 1)   (paper-08 Eq. 1;
                                   cross-check only — lemma L1 makes z identical)
    """
    th12, th13, th23 = (np.arcsin(np.sqrt(s2_12)), np.arcsin(np.sqrt(s2_13)),
                        np.arcsin(np.sqrt(s2_23)))  # (local)
    c12, s12 = np.cos(th12), np.sin(th12)  # (local)
    c13, s13 = np.cos(th13), np.sin(th13)  # (local)
    c23, s23 = np.cos(th23), np.sin(th23)  # (local)
    R23 = np.array([[1, 0, 0], [0, c23, s23], [0, -s23, c23]], dtype=complex)  # (local)
    R13 = np.array([[c13, 0, s13 * np.exp(-1j * delta)], [0, 1, 0],
                    [-s13 * np.exp(1j * delta), 0, c13]], dtype=complex)  # (local)
    R12 = np.array([[c12, s12, 0], [-s12, c12, 0], [0, 0, 1]], dtype=complex)  # (local)
    if majorana_convention == "PDG":
        P = np.diag([1.0, np.exp(1j * rho), np.exp(1j * sigma)]).astype(complex)  # (local)
    elif majorana_convention == "MXZ":
        P = np.diag([np.exp(1j * rho), np.exp(1j * sigma), 1.0]).astype(complex)  # (local)
    else:
        raise ValueError(majorana_convention)
    return R23 @ R13 @ R12 @ P


def congruence_z(U: np.ndarray, M_diag: np.ndarray):
    """M_R^flavor = U^T diag(M) U (s60 congruence pin); returns (M_fl, z) with
    z = |M_fl| / max|M_fl|."""
    M_fl = U.T @ np.diag(M_diag.astype(complex)) @ U  # (local)
    absM = np.abs(M_fl)  # (local)
    return M_fl, absM / absM.max()


def zero_set(z: np.ndarray, eps: float) -> frozenset:
    """Independent (upper-triangle, 1-based) texture-zero positions at threshold eps."""
    return frozenset((i + 1, j + 1) for i in range(3) for j in range(i, 3)
                     if z[i, j] < eps)


def circ_dist(a: float, b: float, period: float = 2 * np.pi) -> float:
    d = abs((a - b) % period)  # (local)
    return min(d, period - d)


def sig4(x: float) -> str:
    """Exactly 4 significant figures with trailing zeros (Class-8.3 publication pin)."""
    return np.format_float_positional(float(x), precision=4, unique=False,
                                      fractional=False, trim="k")


def classify_grid(s2_12, s2_13, s2_23, delta_set, M_diag, patterns):
    """Run the 8-point exhaustive {0,pi}^3 classification. Returns per-point
    records + per-class proximity diagnostics."""
    grid = list(itertools.product(sorted(delta_set), (0.0, np.pi), (0.0, np.pi)))  # (local)
    recs = []  # (local)
    for (d_, r_, s_) in grid:
        U = build_U(s2_12, s2_13, s2_23, d_, r_, s_, "PDG")  # (local)
        uni = np.abs(U.conj().T @ U - np.eye(3)).max()  # (local)
        if uni >= UNITARITY_TOL:
            raise RuntimeError(f"unitarity violated at {(d_, r_, s_)}: {uni:.3e}")
        im_max = np.abs(U.imag).max()  # (local) CP-conserving point => U real
        M_fl, z = congruence_z(U, M_diag)  # (local)
        # Lemma L1 cross-checks: (a) MXZ Majorana-convention z identical;
        # (b) z independent of (rho, sigma) — compare against (delta, 0, 0).
        U_mxz = build_U(s2_12, s2_13, s2_23, d_, r_, s_, "MXZ")  # (local)
        _, z_mxz = congruence_z(U_mxz, M_diag)  # (local)
        U_00 = build_U(s2_12, s2_13, s2_23, d_, 0.0, 0.0, "PDG")  # (local)
        _, z_00 = congruence_z(U_00, M_diag)  # (local)
        zs = zero_set(z, EPS_TEXTURE)  # (local)
        matched = [nm for nm, pat in sorted(patterns.items()) if pat == zs]  # (local)
        recs.append({
            "phases": (d_, r_, s_),
            "U_real_residual": float(im_max),
            "unitarity_residual": float(uni),
            "z": z,
            "M_fl_diag_GeV": np.real(np.diag(M_fl)).copy(),
            "zero_set": zs,
            "match": matched[0] if len(matched) == 1 else (matched if matched else None),
            "lemma_L1_mxz_dev": float(np.abs(z - z_mxz).max()),
            "lemma_L1_rs_dev": float(np.abs(z - z_00).max()),
            "diag_min_z": float(np.diag(z).min()),
            "offdiag_max_z": float(max(z[0, 1], z[0, 2], z[1, 2])),
            "offdiag_min_z": float(min(z[0, 1], z[0, 2], z[1, 2])),
        })
    # per-class proximity: min over grid of (max z over the class's required positions)
    min_z = {}  # (local)
    for nm, pat in patterns.items():
        vals = [max(rec["z"][i - 1, j - 1] for (i, j) in pat) for rec in recs]  # (local)
        min_z[nm] = float(min(vals))
    return grid, recs, min_z


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload printer (script PRINTS; agent calls emit_verdict)
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha, l_max,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    payload = {
        "session": SESSION,            # "100b" — letter-suffixed sub-session
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(l_max),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }  # (local)
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

    # 1. Input pins + plan-freeze SHA asserts (audit chain)
    pins = log_input_pins(INPUT_FILES)  # (local)
    rel_npz = str(P_S99_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/")    # (local)
    rel_p08 = str(P_PAPER08.relative_to(PROJECT_ROOT)).replace("\\", "/")    # (local)
    rel_nf6 = str(P_NUFIT60.relative_to(PROJECT_ROOT)).replace("\\", "/")    # (local)
    for rel, pin in ((rel_npz, SHA_PIN_S99_NPZ), (rel_p08, SHA_PIN_PAPER08),
                     (rel_nf6, SHA_PIN_NUFIT60)):
        if pins[rel] != pin:
            raise RuntimeError(f"SHA mismatch vs plan-freeze pin: {rel}")
    print("  [OK] all 3 static input SHAs match the plan-freeze Input-SHA Ledger")
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), P_CANON, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # 2. Load s99 seesaw npz (route-(a) substrate inputs)
    d99 = np.load(P_S99_NPZ, allow_pickle=True)  # (local)
    M_R_GeV = d99["M_R_GeV"]          # (local) B-branch D_K fold energies, GeV
    M_R_MKK = d99["M_R_MKK"]          # (local) cross-check, M_KK units
    m_D_GeV = d99["m_D_GeV"]          # (local) diagonal m_D (route-(a) basis condition)
    m_nu_npz = d99["m_nu_eV"]         # (local)
    delta_CP_allowed = d99["delta_CP_allowed"]  # (local)
    L_MAX = int(d99["L_max"])         # (local) inherited verbatim into the verdict line
    print(f"M_R_GeV = {M_R_GeV}")
    print(f"m_D_GeV = {m_D_GeV} (diagonal; m_D[0] = {m_D_GeV[0]} — route-(a) basis condition)")
    print(f"delta_CP_allowed (npz) = {delta_CP_allowed};  L_max (inherited) = {L_MAX}")
    assert m_D_GeV[0] == 0.0, "route-(a) scope pin: m_D[0] must be exactly 0 (S62 rank-1 Yukawa)"
    assert np.all(np.diff(M_R_GeV) > 0) and np.all(M_R_GeV > 0), "M_R must be positive ascending"

    # 3. SECTOR-CONFLATION GUARD + delta_CP consistency asserts
    #    canonical sector set = {delta_CP_PMNS_substrate, delta_CP_PMNS_substrate + pi}
    delta_set = np.array(sorted([float(delta_CP_PMNS_substrate),
                                 float(delta_CP_PMNS_substrate) + np.pi]))  # (local)
    dev_allowed = np.abs(np.sort(delta_CP_allowed) - delta_set).max()  # (local)
    assert dev_allowed < CONSISTENCY_TOL, \
        f"npz delta_CP_allowed vs canonical sector set: dev {dev_allowed:.3e} >= 1e-12"
    print(f"[GUARD] npz delta_CP_allowed == canonical PMNS sector set {{0, pi}} (dev {dev_allowed:.1e})")
    guard_min_dist = min(abs(dv - float(phi_CP_K7_transit)) for dv in delta_set)  # (local)
    assert guard_min_dist > 1.0, "phi_CP_K7_transit leaked into the PMNS delta grid"
    print(f"[GUARD] phi_CP_K7_transit = pi/2 (BARYOGENESIS sector, S98-W3-2) is EXCLUDED from the")
    print(f"        PMNS grid: min distance to delta set = {guard_min_dist:.10f} rad = pi/2. The")
    print(f"        d(1.5pi, {{0,pi}}) = pi/2 coincidence below is NOT a leptonic-phase match.")
    print()

    # 4. Runtime PDF extraction (SHA-pinned sources only)
    txt08 = pdf_text(P_PAPER08)   # (local)
    txt60 = pdf_text(P_NUFIT60)   # (local)
    patterns = extract_eq8_patterns(txt08)  # (local)
    print("paper-08 Eq. 8 survivor patterns (1-based upper-triangle zero positions):")
    diag_zero_classes = []  # (local)
    for nm in sorted(patterns):
        pat = sorted(patterns[nm])  # (local)
        has_diag = any(i == j for (i, j) in pat)  # (local)
        if has_diag:
            diag_zero_classes.append(nm)
        print(f"  {nm}: zeros at {pat}  (diagonal zero: {has_diag})")
    assert len(diag_zero_classes) == 5, "L2 premise: every survivor class carries a diagonal zero"
    preds = extract_paper08_class_predictions(txt08)  # (local)
    print(f"paper-08 class predictions: A: m_l ~ {preds['A_m_lightest_eV']} eV, delta in "
          f"[pi, {preds['A_delta_range'][1]/np.pi:.0f}pi], rho ~ sigma +- pi/2; "
          f"B: m_l ~ {preds['B_m_lightest_eV']} eV, delta ~ {preds['B_delta_pref']/np.pi:.2f}pi, "
          f"rho, sigma ~ pi/2")
    t1_52 = extract_paper08_table1_NO(txt08)  # (local) paper-stated NuFIT-5.2-era inputs
    print(f"paper-08 Table 1 (NO, NuFIT-5.2 era): {t1_52}")
    nf60 = extract_nufit60_NO(txt60)  # (local)
    print(f"NuFit-6.0 Table 1 (IC24+SK-atm, NO best fit): {nf60}")

    # 4b. Drift detector + canonical dm2 vintage asserts
    drift = {k: abs(nf60[k] - PROVISIONAL_NUFIT60[k]) for k in PROVISIONAL_NUFIT60}  # (local)
    drift_flag = any(v > DRIFT_BOUND for v in drift.values())  # (local)
    print(f"NuFit-6.0 angle drift vs plan-freeze provisional floats: {drift} "
          f"-> {'FLAGGED' if drift_flag else 'no drift (all <= 0.02)'}")
    assert abs(nf60["dm2_21"] - float(dm2_21_NuFit)) < 1e-12, "canonical dm2_21_NuFit vintage mismatch"
    assert abs(nf60["dm2_3l"] - float(dm2_31_NuFit)) < 1e-12, "canonical dm2_31_NuFit vintage mismatch"
    print("[OK] canonical dm2_21_NuFit / dm2_31_NuFit == NuFit-6.0 PDF as-printed (vintage confirmed)")
    print()

    # 5. Classification on the exhaustive {0,pi}^3 grid — NuFit-6.0 angles (gate-bearing)
    grid, recs, min_z = classify_grid(nf60["s2_12"], nf60["s2_13"], nf60["s2_23"],
                                      delta_set, M_R_GeV, patterns)  # (local)
    # cross-check: M_KK-unit input gives identical z (scale invariance of the congruence)
    _, recs_mkk, _ = classify_grid(nf60["s2_12"], nf60["s2_13"], nf60["s2_23"],
                                   delta_set, M_R_MKK, patterns)  # (local)
    z_unit_dev = max(np.abs(a["z"] - b["z"]).max() for a, b in zip(recs, recs_mkk))  # (local)
    assert z_unit_dev < 1e-12, "GeV vs M_KK unit z-matrices differ"
    print(f"[OK] GeV vs M_KK z-matrix scale invariance: max dev {z_unit_dev:.2e}")
    print(f"[OK] lemma L1 (Majorana-phase transparency): max dev z(PDG) vs z(MXZ convention) = "
          f"{max(r['lemma_L1_mxz_dev'] for r in recs):.2e}; max dev z(rho,sigma) vs z(0,0) = "
          f"{max(r['lemma_L1_rs_dev'] for r in recs):.2e}")
    print(f"[OK] U real at all CP-conserving points: max |Im U| = "
          f"{max(r['U_real_residual'] for r in recs):.2e}; max unitarity residual = "
          f"{max(r['unitarity_residual'] for r in recs):.2e}")

    # 5b. Lemma L2 — diagonal convex-combination bound (structural FAIL forcing)
    M1, M3 = float(M_R_GeV[0]), float(M_R_GeV[2])  # (local)
    z_diag_bound = M1 / M3  # (local) z_ii >= M_1/M_3 for real-orthogonal congruence
    diag_in_range = all(M1 * (1 - 1e-9) <= v <= M3 * (1 + 1e-9)
                        for r in recs for v in r["M_fl_diag_GeV"])  # (local)
    emp_min_diag_z = min(r["diag_min_z"] for r in recs)  # (local)
    assert diag_in_range, "L2 violated: a diagonal entry left [M_1, M_3]"
    assert emp_min_diag_z >= z_diag_bound - 1e-12, "L2 bound violated numerically"
    print(f"[L2] diagonal entries of M_R^flavor in [M_1, M_3] at every grid point: {diag_in_range}")
    print(f"[L2] z_ii lower bound M_1/M_3 = {z_diag_bound:.6f}; empirical min z_ii = {emp_min_diag_z:.6f}")
    print(f"[L2] all 5 survivor classes carry a diagonal zero => no class can match at ANY")
    print(f"     CP-conserving point for ANY positive heavy spectrum (FAIL analytically forced;")
    print(f"     z_ii >= {z_diag_bound:.4f} is {np.log10(z_diag_bound / EPS_TEXTURE):.2f} OOM above eps = 1e-10)")
    print()

    # 6. Membership results (gate-bearing, eps = 1e-10) + diagnostic near-zero scan
    print("Per-grid-point classification (NuFit-6.0 angles, eps = 1e-10):")
    any_match = False  # (local)
    for rec in recs:
        d_, r_, s_ = rec["phases"]  # (local)
        zs = sorted(rec["zero_set"])  # (local)
        print(f"  (delta, rho, sigma) = ({d_/np.pi:.0f}, {r_/np.pi:.0f}, {s_/np.pi:.0f})*pi : "
              f"zero set {zs if zs else '{}'} -> match: {rec['match']}")
        if rec["match"]:
            any_match = True
    diag_scan = {}  # (local) eps -> per-point matches under exact set equality
    for eps in EPS_DIAGNOSTIC:
        hits = []  # (local)
        for rec in recs:
            zs_e = zero_set(rec["z"], eps)  # (local)
            mt = [nm for nm, pat in sorted(patterns.items()) if pat == zs_e]  # (local)
            if mt:
                hits.append((rec["phases"], mt))
        diag_scan[eps] = hits
        print(f"  diagnostic eps = {eps:g}: matches = {hits if hits else 'none'}")
    print("Per-class proximity min_z (min over grid of max z over the class's required zeros):")
    for nm in sorted(min_z):
        print(f"  min_z[{nm}] = {sig4(min_z[nm])}   (>= L2 bound {z_diag_bound:.4f} since "
              f"{nm} requires a diagonal zero)")

    # 6b. Phase-region containment analysis (per the consistency clause; the raw
    #     distances make the conclusion tolerance-independent for tol < pi/2)
    region_rows = []  # (local)
    for (d_, r_, s_) in grid:
        dB = max(circ_dist(d_, preds["B_delta_pref"]), circ_dist(r_, preds["B_rho_sigma_pref"]),
                 circ_dist(s_, preds["B_rho_sigma_pref"]))  # (local)
        dn = (d_ % (2 * np.pi))  # (local)
        in_int = preds["A_delta_range"][0] <= dn <= preds["A_delta_range"][1]  # (local)
        dA_delta = 0.0 if in_int else min(circ_dist(d_, preds["A_delta_range"][0]),
                                          circ_dist(d_, preds["A_delta_range"][1]))  # (local)
        if not in_int and circ_dist(d_, 0.0) == 0.0:
            dA_delta = 0.0  # (local) delta = 0 == 2pi is the closed-interval boundary
        dA_maj = min(circ_dist(r_ - s_, preds["A_majorana_rel_offset"]),
                     circ_dist(r_ - s_, -preds["A_majorana_rel_offset"]))  # (local)
        dA = max(dA_delta, dA_maj)  # (local)
        region_rows.append({"phases": (d_, r_, s_), "d_A": dA, "d_B": dB,
                            "in_A": dA <= TOL_REGION, "in_B": dB <= TOL_REGION})
    min_dA = min(rw["d_A"] for rw in region_rows)  # (local)
    min_dB = min(rw["d_B"] for rw in region_rows)  # (local)
    any_in_region = any(rw["in_A"] or rw["in_B"] for rw in region_rows)  # (local)
    print(f"Phase-region distances over the grid: min d_A = {min_dA/np.pi:.3f}*pi "
          f"(A-class Majorana relation rho ~ sigma +- pi/2), min d_B = {min_dB/np.pi:.3f}*pi "
          f"(B-class delta ~ 1.5pi, rho/sigma ~ pi/2); any grid point inside any class "
          f"region (tol pi/4): {any_in_region}")
    print("  -> Chain 2 realized: every {0,pi}^3 point sits at the MAXIMAL CP-odd distance pi/2")
    print("     from the B-class preference on every phase axis, and at pi/2 from the A-class")
    print("     Majorana relation. Containment fails for ANY tolerance < pi/2 — not a band choice.")

    # 6c. Vintage-robustness diagnostic re-run (paper-08-stated NuFIT-5.2 inputs)
    _, recs52, min_z52 = classify_grid(t1_52["s2_12"], t1_52["s2_13"], t1_52["s2_23"],
                                       delta_set, M_R_GeV, patterns)  # (local)
    any_match_52 = any(r["match"] for r in recs52)  # (local)
    vintage_robust = (any_match == any_match_52)  # (local)
    print(f"Vintage-robustness (NuFIT-5.2 re-run): any_match = {any_match_52}; "
          f"min_z = {[f'{nm}:{sig4(min_z52[nm])}' for nm in sorted(min_z52)]}; "
          f"class verdict vintage-robust: {vintage_robust}")

    # 6d. m_1 = 0 EXACT annotation + spectrum cross-check (diagnostic)
    m_nu_nf60 = np.array([0.0, np.sqrt(float(dm2_21_NuFit)), np.sqrt(float(dm2_31_NuFit))])  # (local)
    reldiff_m = np.zeros(3)  # (local)
    reldiff_m[1:] = (m_nu_npz[1:] - m_nu_nf60[1:]) / m_nu_nf60[1:]
    print(f"m_1 = 0 EXACT cross-check: m_nu(NuFit-6.0, m_1=0) = {m_nu_nf60} eV vs npz "
          f"{m_nu_npz} eV; reldiff (m2, m3) = ({reldiff_m[1]:+.4%}, {reldiff_m[2]:+.4%}) "
          f"[npz spectrum is PDG-vintage (7.53e-5, 2.453e-3); diagnostic only]")
    print(f"Matched-class lightest-mass annotation: substrate m_1 = 0 EXACT (S62 rank-1 Yukawa),")
    print(f"  Sigma_mnu = {float(d99['Sigma_mnu_eV']):.4f} eV. Paper-08 A-class implies "
          f"m_l ~ {preds['A_m_lightest_eV']} eV (near-floor, NOT exactly 0); B-class implies "
          f"m_l ~ {preds['B_m_lightest_eV']} eV => Sigma >~ 0.3 eV, excluded by the substrate")
    print(f"  Sigma and by DESI {float(d99['bound_DESI']):.3f} eV — both axes cohere with FAIL.")
    print()

    # 7. Verdict per the pre-registered operator
    match_points = [rec for rec in recs if rec["match"] and isinstance(rec["match"], str)]  # (local)
    if not any_match:
        verdict = "FAIL"  # (local) no grid point yields any survivor-class pattern
    else:
        pass_pts = []  # (local)
        for rec in match_points:
            cls = rec["match"]  # (local)
            rw = next(rw for rw in region_rows if rw["phases"] == rec["phases"])  # (local)
            inside = rw["in_A"] if cls.startswith("A") else rw["in_B"]  # (local)
            if inside:
                pass_pts.append(rec)
        verdict = "PASS" if pass_pts else "INFO"

    # Pre-registered 3-tuple mapping (directional content of Chains 1-2, fixed
    # BEFORE the membership outcome is read):
    #   sign      = PASS iff Chain-1 direction (generic off-diagonals >> eps;
    #               operationalized min over grid of offdiag_max_z > 1e-6) AND
    #               Chain-2 direction (B-class delta distance == pi/2 within 1e-12)
    #               both verify numerically; else FAIL.
    #   magnitude = the membership outcome itself (FAIL / INFO / PASS as above).
    #   regime    = VALID (exact finite arithmetic; unitarity + consistency
    #               asserts all enforced above — any breach raises, exiting nonzero).
    chain1_dir = min(r["offdiag_max_z"] for r in recs) > 1e-6  # (local)
    chain2_dir = abs(min_dB - np.pi / 2) < 1e-12  # (local)
    sign_verdict = "PASS" if (chain1_dir and chain2_dir) else "FAIL"  # (local)
    magnitude_verdict = verdict  # (local)
    regime_verdict = "VALID"  # (local)
    # composite collapse cross-check (gate-verdicts.md schema-v2): with sign=PASS,
    # regime=VALID the composite equals magnitude — verify:
    composite = ("FAIL" if regime_verdict == "BREAKDOWN" else
                 "FAIL" if sign_verdict == "FAIL" else
                 "FAIL" if (magnitude_verdict == "FAIL" and regime_verdict == "VALID") else
                 "INFO" if (magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL") else
                 "INFO" if magnitude_verdict == "INFO" else "PASS")  # (local)
    assert composite == verdict, "composite collapse rule inconsistency"

    gen_offdiag_max = max(r["offdiag_max_z"] for r in recs)  # (local)
    gen_offdiag_min = min(r["offdiag_min_z"] for r in recs)  # (local)
    value = (f"no_survivor_class_match_at_eps1e-10_on_full_grid_{{0,pi}}^3_x8; "
             if verdict == "FAIL" else f"match={[(r['phases'], r['match']) for r in match_points]}; ") + (
        f"min_z A1={sig4(min_z['A1'])} A2={sig4(min_z['A2'])} B3={sig4(min_z['B3'])} "
        f"B4={sig4(min_z['B4'])} B6={sig4(min_z['B6'])}; structural: all 5 survivors carry a "
        f"diagonal zero and real-orthogonal congruence forces z_ii >= M1/M3 = {z_diag_bound:.4f} "
        f"({np.log10(z_diag_bound/EPS_TEXTURE):.1f} OOM above eps); offdiag z range "
        f"[{gen_offdiag_min:.3g}, {gen_offdiag_max:.3g}] (Chain-1 generic scale); "
        f"d_B = pi/2 maximal (Chain-2 realized); route-(a) scope; "
        f"vintage-robust(NuFIT-5.2)={vintage_robust}; drift={'FLAGGED' if drift_flag else '0.000'}")  # (local)

    # 8. Save npz
    np.savez(
        OUT_NPZ,
        M_R_GeV=M_R_GeV, M_R_MKK=M_R_MKK, m_D_GeV=m_D_GeV,
        m_nu_npz_eV=m_nu_npz, m_nu_nf60_eV=m_nu_nf60, m_nu_reldiff=reldiff_m,
        Sigma_mnu_eV=float(d99["Sigma_mnu_eV"]),
        delta_CP_allowed=delta_CP_allowed, delta_set=delta_set,
        phi_CP_K7_transit_excluded=float(phi_CP_K7_transit),
        guard_min_dist=guard_min_dist,
        grid_phases=np.array(grid),
        z_matrices=np.stack([r["z"] for r in recs]),
        M_fl_diag_GeV=np.stack([r["M_fl_diag_GeV"] for r in recs]),
        zero_sets_json=json.dumps([sorted(r["zero_set"]) for r in recs]),
        matches_json=json.dumps([r["match"] for r in recs]),
        patterns_json=json.dumps({nm: sorted(p) for nm, p in patterns.items()}),
        diag_zero_classes_json=json.dumps(sorted(diag_zero_classes)),
        eps_texture=EPS_TEXTURE, eps_diagnostic=np.array(EPS_DIAGNOSTIC),
        diag_scan_json=json.dumps({str(k): [(list(p), m) for p, m in v]
                                   for k, v in diag_scan.items()}),
        min_z_json=json.dumps(min_z), min_z_52_json=json.dumps(min_z52),
        z_diag_bound=z_diag_bound, emp_min_diag_z=emp_min_diag_z,
        lemma_L1_max_dev=max(max(r["lemma_L1_mxz_dev"], r["lemma_L1_rs_dev"]) for r in recs),
        unitarity_max=max(r["unitarity_residual"] for r in recs),
        U_real_residual_max=max(r["U_real_residual"] for r in recs),
        nufit60_json=json.dumps(nf60), nufit52_json=json.dumps(t1_52),
        provisional_json=json.dumps(PROVISIONAL_NUFIT60), drift_json=json.dumps(drift),
        drift_flag=bool(drift_flag), vintage_robust=bool(vintage_robust),
        class_predictions_json=json.dumps({k: (list(v) if isinstance(v, tuple) else v)
                                           for k, v in preds.items()}),
        region_rows_json=json.dumps([{"phases": list(rw["phases"]), "d_A": rw["d_A"],
                                      "d_B": rw["d_B"], "in_A": bool(rw["in_A"]),
                                      "in_B": bool(rw["in_B"])} for rw in region_rows]),
        min_dA=min_dA, min_dB=min_dB, any_in_region=bool(any_in_region),
        verdict=verdict, sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        value=value, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        audit_sha256=audit_sha, content_sha256=content_sha,
        input_pins_json=json.dumps(pins),
        methodology_pinmap_json=json.dumps(METHODOLOGY_PINMAP),
    )
    print(f"[saved] {OUT_NPZ.name}")

    # 9. Plot: 8 z-matrix heat maps + per-class proximity bars with eps rails
    fig = plt.figure(figsize=(16, 11))  # (local)
    gs = fig.add_gridspec(3, 4, height_ratios=[1, 1, 1.15], hspace=0.45, wspace=0.30)  # (local)
    labels3 = ["e", "mu", "tau"]  # (local)
    for k, rec in enumerate(recs):
        ax = fig.add_subplot(gs[k // 4, k % 4])  # (local)
        logz = np.log10(rec["z"])  # (local)
        im = ax.imshow(logz, cmap="viridis", vmin=-3, vmax=0)  # (local)
        d_, r_, s_ = rec["phases"]  # (local)
        ax.set_title(f"$(\\delta,\\rho,\\sigma)=({d_/np.pi:.0f},{r_/np.pi:.0f},{s_/np.pi:.0f})\\pi$"
                     + (f"  match: {rec['match']}" if rec["match"] else "  no match"),
                     fontsize=9)
        ax.set_xticks(range(3), labels3); ax.set_yticks(range(3), labels3)
        for i in range(3):
            for j in range(3):
                ax.text(j, i, f"{rec['z'][i, j]:.3f}", ha="center", va="center",
                        fontsize=8, color="w")
        if k == 3:
            fig.colorbar(im, ax=ax, fraction=0.046, label="log10 z")
    axb = fig.add_subplot(gs[2, :])  # (local)
    names = sorted(min_z)  # (local)
    vals = [min_z[nm] for nm in names]  # (local)
    xpos = np.arange(len(names))  # (local)
    axb.bar(xpos - 0.18, vals, color="#3b6ea5", width=0.36,
            label="min_z (NuFit-6.0, gate-bearing)")
    axb.bar(xpos + 0.18, [min_z52[nm] for nm in names], color="#9ec9e8",
            width=0.36, label="min_z (NuFIT-5.2 diagnostic)")
    axb.set_xticks(xpos, names)
    axb.set_yscale("log"); axb.set_ylim(1e-12, 3.0); axb.set_xlim(-0.6, 4.6)
    for eps, lab, col in ((EPS_TEXTURE, "eps gate 1e-10", "crimson"),
                          (1e-6, "diag 1e-6", "darkorange"),
                          (1e-3, "diag 1e-3", "goldenrod"),
                          (3e-2, "diag 3e-2 (generic off-diag scale)", "olive")):
        axb.axhline(eps, color=col, ls="--", lw=1.2)
        axb.text(3.95, eps * 1.4, lab, fontsize=8, color=col)
    axb.axhline(z_diag_bound, color="k", ls=":", lw=1.5)
    axb.text(-0.5, z_diag_bound * 0.45, f"L2 structural bound M1/M3 = {z_diag_bound:.4f}",
             fontsize=9)
    for x, v in zip(xpos - 0.18, vals):
        axb.text(x, v * 1.25, sig4(v), ha="center", fontsize=9)
    axb.set_ylabel("min over grid of max z over class zeros")
    axb.set_title(f"{GATE_ID}: per-class proximity vs eps rails — verdict {verdict} "
                  f"(all 5 survivors need a diagonal zero; real-orthogonal congruence "
                  f"forces z_ii >= M1/M3)", fontsize=10)
    axb.legend(loc="center right", fontsize=8)
    fig.suptitle("S100b-MR-TEXTURE-CLASS — M_R^flavor = U^T diag(M_R) U over (delta,rho,sigma) in {0,pi}^3 "
                 "(z = |M|/max|M|; Majorana phases provably inert in z — lemma L1)", fontsize=11)
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"[saved] {OUT_PNG.name}")
    print()

    # 10. 4-tuple + verdict payload
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    extra_rows = [
        (f"# SECTOR-GUARD: phi_CP_K7_transit=pi/2 is the BARYOGENESIS-sector phase "
         f"(S98-W3-2 CLOSED-SOURCED-UNIQUE), EXCLUDED from the PMNS grid; the "
         f"d(1.5pi,{{0,pi}})=pi/2 coincidence is NOT a leptonic-phase match "
         f"# {GATE_ID} sector-conflation guard"),
        (f"# STRUCTURAL-L2: all 5 MXZ survivors carry a DIAGONAL zero; "
         f"(U^T D U)_ii = sum_k M_k U_ki^2 in [M1,M3] for real-orthogonal U => "
         f"z_ii >= M1/M3 = {z_diag_bound:.6f} >> eps=1e-10; FAIL analytically forced "
         f"at CP-conserving phases for ANY positive heavy spectrum # {GATE_ID}"),
        (f"# CHAIN-2: B-class delta_pref=1.5pi, d(1.5pi,{{0,pi}})=pi/2 MAXIMAL; "
         f"A-class Majorana relation rho~sigma+-pi/2 also pi/2 from grid; "
         f"phase-containment fails for any tol<pi/2 # {GATE_ID}"),
    ]  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha, L_MAX,
                          sign_verdict=sign_verdict,
                          magnitude_verdict=magnitude_verdict,
                          regime_verdict=regime_verdict,
                          companion_note=("route-(a) scope; m_D diagonal per s99; "
                                          "patterns extracted from SHA-pinned paper-08 Eq. 8 at runtime"),
                          extra_rows=extra_rows)

    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0  # exit code reflects script health only (math-scripts.md)


if __name__ == "__main__":
    sys.exit(main())
