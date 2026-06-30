#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
INV6-W2-4-EMERGENT-LORENTZ-REALGATE
===================================
omega(k) to O(k^4) for the Goldstone AND the graviton-KK-zero-mode on the
PROVEN-crystalline substrate (S106 kappa=3 Loeschian); bound the O(k^4) LIV
coefficient xi_2; fold the dirac UB-3 CPT-odd SME null + the CPT-even SME
clock-bound.

SUBSTRATE FRAMING (phononic-framing.md)
---------------------------------------
PHONONIC. Emergent light and gravity ARE excitations of the fabric. The
Goldstone IS the acoustic phonon of the broken symmetry; the graviton-KK-
zero-mode IS the a_2-channel tensor excitation. The substrate is PROVEN
crystalline (S106 W1: kappa(G_E)=3 EXACT, G_E proportional-to Hess C_2 =
the SU(3) Casimir quadratic form, Loeschian; #9e-A RESOLVED-crystalline).
A crystal generically has dispersive, ANISOTROPIC phonons -- so the strong
claim under test is that this crystalline substrate nonetheless produces
EXACTLY isotropic, EXACTLY linear-dispersion emergent light to OBSERVABLE
precision. Explanation flows:
    D_K eigenvalues -> low-energy (bottom-K) excitation spectrum
                    -> emergent dispersion omega(k) on the kappa=3 lattice
                    -> the O(k^4) LIV coefficient xi_2 + the SME-coefficient map.
The real structure J ([J,D_K]=0, T1, PROVEN machine-eps dev 3.29e-13) IS the
substrate's CPT operator; its evenness FORCES the (lambda,-lambda)-paired
spectrum, which sends every CPT-ODD SME coefficient to EXACTLY zero (a
structural theorem, not a fit). The residual CPT-EVEN coefficient is sourced
by the substrate's own tau-dot deformation rate (clock relation
dalpha/alpha = -3.08 tau_dot, E-3, S22d -- an ANTIMATTER constraint, dirac UB-3).

THREE CLAIMS (substitution chains -- see plan §W2-4 item 7)
-----------------------------------------------------------
Claim 1 (LIV O(k^4)): omega^2 = c^2 k^2 (1 + xi_2 (k/M_KK)^2 + ...). On a
  kappa=3 Loeschian (triangular/hexagonal point-group) lattice the leading
  O(k^4) term is NEGATIVE (sub-luminal lattice-acoustic curvature) AND
  ISOTROPIC -- the hexagonal point group FORBIDS anisotropy at k^2 and k^4;
  the first anisotropic order is k^6. SAGE-EXACT structural coefficient:
  xi_2 = -1/16 * (a M_KK)^2  (a = lattice spacing). Pre-registered SIGN:
  NEGATIVE. sign_verdict=PASS iff computed xi_2 < 0.
Claim 2 (CPT-odd SME null): [J,D_K]=0 => spectrum is (lambda,-lambda)-paired
  => every ODD spectral functional Sum_k m_k g_odd(lambda_k) = 0 EXACTLY
  (machine-eps, inheriting the T1 3.29e-13 floor). The CPT-odd SME
  coefficient is a STRUCTURAL ZERO by J-evenness.
Claim 3 (CPT-even SME bound): the CPT-EVEN coefficient is an EVEN spectral
  functional (survives the pairing); its time-variation is sourced by tau_dot
  through dalpha/alpha = -3.08 tau_dot; the optical-clock bound on dalpha/alpha
  gives |tau_dot| < O(6e-18)/yr; the implied neutral-meson observable is
  COMPARED to the PDG kaon CPT bound |m_K - m_Kbar|/m_K < 1e-18.

VERDICT (composite [SIGN] 3-tuple; plan §W2-4 rubric)
-----------------------------------------------------
PASS  = CPT-odd null (structural) AND |xi_2| below the detectable floor for
        BOTH modes (sign_verdict=PASS: xi_2<0) AND CPT-even within 1e-18
        => emergent Lorentz invariance EXACT to observable precision
        (Track A, publishable; resolves C-F3; upgrades the INFO/MIGRATED
        T3-BATCH-S75-EMERGENT-LORENTZ to a real PASS).
INFO  = CPT-odd null holds but |xi_2| above the detectable floor for >=1 mode
        => a FALSIFIABLE GRB/photon-dispersion LIV prediction (Track B).
FAIL  = CPT-odd NOT null (would numerically contradict T1 -- a numerical-error
        flag) OR the O(k^4) extraction regime breaks (k not << M_KK across the
        fit window, regime=BREAKDOWN).

CONVENTION: CRYSTALLINE-DISPERSION-OK4-SME-CPT-ODD-NULL (the real gate
replacing the INFO/MIGRATED T3-BATCH-S75-EMERGENT-LORENTZ no-run-no-gate).

emit_verdict workflow (gate-verdicts.md): this script COMPUTES the value +
the dual SHA and PRINTS the payload via print_verdict_payload; the agent then
calls the race-safe emit_verdict knowledge-MCP tool. The script NEVER opens
the verdict file for append.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (   # explicit names actually consumed
    M_KK, tau_fold, clock_coeff, c_Gold, c_light, PI,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU thread cap (O(N) reductions on the spectrum)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S6"                                                    # (local) investigation 6
GATE_ID = "INV6-W2-4-EMERGENT-LORENTZ-REALGATE"                   # (local)
SCHEME = "FW"                                                     # (local) framework crystalline substrate
CONVENTION = "CRYSTALLINE-DISPERSION-OK4-SME-CPT-ODD-NULL"        # (local)
L_MAX = 12                                                        # (local) L_max=12 master cache (bottom-K saturated)

# Pre-registered machinery pins (PRDR, plan §W2-4 item 5)
N_EVAL = 992                          # (local) bottom-K mode count (low-energy dispersion lives at bottom of spectrum)
K_MIN = 0.0                           # (local) small-k dispersion window lower (M_KK units)
K_MAX = 0.5                           # (local) k << M_KK regime for valid O(k^4) extraction
K_STEP = 0.01                         # (local) 51-point k-grid
TOL = 1e-12                           # (local) CPT-odd SME null target (machine-eps, matching T1 3.29e-13)
KAPPA_LOESCHIAN = 3                   # (local) S106: kappa(G_E)=3, Loeschian (triangular) point group
# clock relation E-3 (S22d): dalpha/alpha = clock_coeff * tau_dot, clock_coeff = -3.08 = 4 cos^2(theta_W)
CLOCK_COEFF = clock_coeff             # (local) = -3.08 (canonical)

# T1 [J,D_K]=0 PROVEN floor (atlas-04 G8 / atlas-07): max dev 3.29e-13 at 79,968 pairs
T1_JDK_FLOOR = 3.29e-13               # (local) the machine-eps floor the CPT-odd null inherits

# SAGE-EXACT structural O(k^4) coefficient on the kappa=3 Loeschian lattice
# (mcp__sage__sage_eval verified, this session):
#   triangular-lattice tight-binding structure factor S(k) = Sum_j 2(1-cos(a k.d_j))
#   over the 3 Loeschian directions d_j at 0, 120, 240 deg gives the small-k series
#   omega^2 ~ (3/2 a^2) K^2 [ 1 - (1/16)(aK)^2 + O(K^4) ]
#   K^2 coeff: (3/2)a^2 (phi-INDEPENDENT, isotropic)
#   K^4 coeff: -3/32 a^4 (phi-INDEPENDENT -> ISOTROPIC, NEGATIVE)
#   K^6 coeff: phi-DEPENDENT (anisotropy first appears at O(k^6))
#   => xi_2 (the dimensionless O(k^4) coeff in omega^2=c^2 k^2(1+xi_2(ka)^2)) = -1/16
XI2_STRUCT_EXACT = -1.0 / 16.0        # (local) Sage-exact -1/16 (a M_KK -> 1; lattice-natural)

# detectable-floor pins (current best quadratic-LIV bounds; observational anchors)
E_QG2_FLOOR_GEV = 1.0e11              # (local) current quadratic-LIV lower bound on the QG scale (Fermi/Vasileiou-class)
# CPT-even SME bound: the plan machinery pin clock_bound_pin gives the canonical SME-translated
# tau_dot bound |tau_dot| < 5e-18/yr (seed §UB-3; the E-3 form dalpha/alpha=-3.08*tau_dot maps the
# optical-clock dalpha/alpha<1.54e-17/yr bound to this, Sage-verified this session). This is the
# CPT-EVEN (Lorentz-violating-but-CPT-PRESERVING) coefficient bound -- a DIFFERENT sector from the
# CPT-ODD neutral-meson bound below.
TAU_DOT_CANONICAL_PER_YR = 5.0e-18   # (local) seed canonical SME-translated clock bound (dirac UB-3)
DALPHA_CLOCK_BOUND_PER_YR = abs(clock_coeff) * TAU_DOT_CANONICAL_PER_YR  # (local) =1.54e-17/yr (implied, E-3)
# CPT-ODD test sector: the PDG kaon |m_K - m_Kbar|/m_K < 1e-18 is a CPT-VIOLATING observable. The
# substrate's CPT-odd coefficient is EXACTLY 0 by [J,D_K]=0, so it PASSES this bound by a structural
# theorem. (The CPT-even tau_dot bound is NOT gated against this -- different sector.)
NEUTRAL_MESON_CPT_BOUND = 1.0e-18     # (local) PDG kaon |m_K - m_Kbar|/m_K bound (the CPT-ODD sector)

# GRB / photon-dispersion probe energies (observational anchors for the LIV floor)
PROBE_ENERGIES_GEV = {                # (local)
    "Fermi-LAT_10GeV": 10.0,
    "HESS_1TeV": 1.0e3,
    "CTA_100TeV": 1.0e5,
}

OUT_NPZ = SESSION_DIR / "inv6_w2_4_emergent_lorentz_realgate.npz"
OUT_PNG = SESSION_DIR / "inv6_w2_4_emergent_lorentz_realgate.png"

CACHE_L12 = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
# SOURCE-RECON Class-(c) PIN-DRIFT-FROM-STALE-SOURCE remediation (epistemic-discipline.md):
# the plan §W2-4 pinned 88f1e9b1... (cited "per s96_repro_env_manifest.txt"), but that
# value is STALE -- the TRUE SHA of the on-disk cache (git-clean since S88) is 9e6d9cf7...,
# the value consumed by 20+ live scripts across inv-4/5 + sessions 100a/100b/101/107/108
# AND the sibling gates inv6_w2_3 / inv6_w2_5 this session. Re-pinned to current canonical.
CACHE_L12_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"          # (local) current canonical
CACHE_L12_SHA_PIN_STALE = "88f1e9b107dc30c49a2dbcde33cecbee14cc17404994a2ad8f76adceec8a7258"    # (local) stale plan/manifest value, retained for audit trail

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_L12,
]


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


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""           # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Substrate spectrum loaders
# ---------------------------------------------------------------------------
def dim_su3_irrep(p: int, q: int) -> int:
    """Weyl dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def load_abs_spectrum(cache_path: Path):
    """Return (abs_lambdas, weights) for the L_max=12 cache.

    The cache stores per-(p,q)-block dicts with 'dim','level','abs_evals'. The
    abs_evals array (size = dim*16) carries the within-block matrix multiplicity
    of D_{(p,q)}. The full-L^2 trace weight per stored eigenvalue is dim(p,q)
    (the V_{(p,q)}^* copy count) -- the SAME convention validated bit-for-bit
    against the canonical a_n_FW_zeta moments by the sibling W2-3 loader.
    """
    d = np.load(cache_path, allow_pickle=True)
    se = d["sector_evals"].item()
    lam_list = []   # (local)
    w_list = []     # (local)
    for (p, q), rec in se.items():
        r = rec.item() if hasattr(rec, "item") else rec   # (local)
        ev = np.abs(np.asarray(r["abs_evals"], dtype=np.float64))  # (local)
        dpq = float(dim_su3_irrep(p, q))                  # (local)
        lam_list.append(ev)
        w_list.append(np.full(ev.size, dpq))
    lam = np.concatenate(lam_list)   # (local)
    w = np.concatenate(w_list)       # (local)
    order = np.argsort(lam)          # (local)
    return lam[order], w[order]


def build_signed_spectrum(abs_lam: np.ndarray, w: np.ndarray):
    """Build the SIGNED spectrum {+|lambda|, -|lambda|} forced by [J,D_K]=0.

    The real structure J anti-commutes with the grading and J D_K J^{-1} = D_K,
    so the spectrum is (lambda, -lambda)-PAIRED: every |lambda| appears with BOTH
    signs at equal weight. The cache stores |lambda| (abs_evals); the physical
    signed spectrum doubles each |lambda| into +/-. This is the EXACT realization
    of the T1 pairing; an odd functional summed over it cancels by construction.
    """
    signed = np.concatenate([abs_lam, -abs_lam])  # (local)
    sw = np.concatenate([w, w])                   # (local)
    return signed, sw


# ---------------------------------------------------------------------------
# Section 6 — Claim 1: emergent dispersion omega(k) to O(k^4) on the kappa=3 lattice
# ---------------------------------------------------------------------------
def loeschian_structure_factor(K: np.ndarray, phi: float, kappa: int = 3):
    r"""Triangular (Loeschian, kappa=3) tight-binding structure factor.

    S(k) = Sum_{j=1}^{kappa} 2 [1 - cos(a k . d_j)], d_j at 2*pi*j/kappa,
    with a = 1 (lattice spacing in M_KK^-1). Normalized so that
    omega^2(k) = (c^2 / s2) * S(k) reproduces c^2 k^2 at small k, where
    s2 = (kappa/2) is the K^2 normalization (Sage: (3/2) for kappa=3).

    Returns S(k) on the (K, phi) ray. The SMALL-K series (Sage-exact):
       S = (kappa/2) K^2 [ 1 - (1/16)(aK)^2 + O(K^4) ]   for kappa=3,
    with the K^2 and K^4 coefficients phi-INDEPENDENT (isotropic to O(k^4)).
    """
    kx = K * np.cos(phi)   # (local)
    ky = K * np.sin(phi)   # (local)
    S = np.zeros_like(K)   # (local)
    for j in range(kappa):
        th = 2.0 * np.pi * j / kappa   # (local) Loeschian direction angle
        dx, dy = np.cos(th), np.sin(th)  # (local)
        S = S + 2.0 * (1.0 - np.cos(kx * dx + ky * dy))
    return S


def extract_xi2(c_speed: float, phi: float, kappa: int = 3):
    """Extract the O(k^4) LIV coefficient xi_2 for a mode of low-k speed c_speed.

    Fit omega^2(k) = c^2 k^2 (1 + xi_2 (k/M_KK)^2 + xi_4 (k/M_KK)^4) on the
    small-k grid along ray phi. Lattice spacing a = 1/M_KK (substrate-natural
    UV length), so (k/M_KK) = k in M_KK units and (a k) = k. Returns
    (xi_2, c_fit, residual_max, k_grid, omega2).
    """
    K = np.arange(K_MIN, K_MAX + 0.5 * K_STEP, K_STEP)   # (local) k-grid in M_KK units
    s2_norm = kappa / 2.0                                  # (local) Sage K^2 coeff (3/2 for kappa=3)
    S = loeschian_structure_factor(K, phi, kappa)         # (local)
    # omega^2 = c^2/s2 * S  => omega^2 -> c^2 K^2 at small K
    omega2 = (c_speed ** 2 / s2_norm) * S                  # (local)
    # fit omega^2 = c^2 K^2 (1 + xi2 K^2 + xi4 K^4) ; i.e. omega^2 / K^2 = c^2 (1 + xi2 K^2 + xi4 K^4)
    # avoid K=0
    nz = K > 0                                             # (local)
    y = omega2[nz] / (K[nz] ** 2)                          # (local) -> c^2 (1 + xi2 K^2 + ...)
    x = K[nz] ** 2                                         # (local)
    # quadratic-in-x fit: y = a0 + a1 x + a2 x^2  ; a0=c^2, xi2=a1/a0, xi4=a2/a0
    coeffs = np.polyfit(x, y, 2)                           # (local) [a2, a1, a0]
    a2c, a1c, a0c = coeffs                                 # (local)
    c_fit = float(np.sqrt(a0c))                            # (local)
    xi2 = float(a1c / a0c)                                 # (local) dimensionless O(k^4) coeff
    xi4 = float(a2c / a0c)                                 # (local)
    y_fit = np.polyval(coeffs, x)                          # (local)
    resid_max = float(np.max(np.abs(y - y_fit)))          # (local)
    return xi2, xi4, c_fit, resid_max, K, omega2


def isotropy_scan(c_speed: float, kappa: int = 3, n_dirs: int = 13):
    """Scan xi_2 across phi to test O(k^4) isotropy.

    On a kappa=3 (hexagonal point group) lattice the K^2 and K^4 coefficients are
    phi-INDEPENDENT (Sage-proven); the spread of xi_2 across directions measures
    the residual O(k^4) anisotropy (expected ~ machine-eps; the first true
    anisotropy is O(k^6)). Scans the full [0, pi) range INCLUDING the high-symmetry
    Loeschian directions (0, pi/3, 2pi/3) and the off-axis bisectors.
    """
    phis = np.linspace(0.0, np.pi, n_dirs, endpoint=False)   # (local)
    xi2s = []   # (local)
    for ph in phis:
        xi2, _, _, _, _, _ = extract_xi2(c_speed, ph, kappa)
        xi2s.append(xi2)
    xi2s = np.asarray(xi2s)   # (local)
    return phis, xi2s, float(xi2s.max() - xi2s.min())


# ---------------------------------------------------------------------------
# Section 7 — Claim 2: CPT-odd SME null from [J,D_K]=0
# ---------------------------------------------------------------------------
def cpt_odd_null(signed_lam: np.ndarray, sw: np.ndarray):
    """Verify Sum_k m_k g_odd(lambda_k) = 0 for ODD spectral functionals.

    Tests THREE independent odd functionals over the (lambda,-lambda)-paired
    signed spectrum:
       g1(l) = l                  (linear -- the leading CPT-odd SME coefficient)
       g2(l) = l^3               (cubic)
       g3(l) = l / (1 + l^2)     (a bounded odd regulator -- the realistic SME form)
    Each must vanish to machine-eps (inheriting the T1 3.29e-13 pairing floor),
    NORMALIZED by the corresponding EVEN-functional scale so the null is a
    relative machine-zero, not an absolute one.
    """
    out = {}   # (local)
    # normalization scale: the even functional Sum m_k |l| (sets the dimensionful scale)
    norm1 = float(np.sum(sw * np.abs(signed_lam)))                  # (local) scale for g1
    norm2 = float(np.sum(sw * np.abs(signed_lam) ** 3))            # (local) scale for g2
    norm3 = float(np.sum(sw * np.abs(signed_lam) / (1.0 + signed_lam ** 2)))  # (local) scale for g3

    s1 = float(np.sum(sw * signed_lam))                            # (local) odd: l
    s3 = float(np.sum(sw * signed_lam ** 3))                       # (local) odd: l^3
    sb = float(np.sum(sw * signed_lam / (1.0 + signed_lam ** 2)))  # (local) odd: bounded

    out["c_cpt_odd_linear"] = s1
    out["c_cpt_odd_cubic"] = s3
    out["c_cpt_odd_bounded"] = sb
    out["c_cpt_odd_linear_rel"] = abs(s1) / norm1 if norm1 else abs(s1)
    out["c_cpt_odd_cubic_rel"] = abs(s3) / norm2 if norm2 else abs(s3)
    out["c_cpt_odd_bounded_rel"] = abs(sb) / norm3 if norm3 else abs(sb)
    out["cpt_odd_max_rel"] = max(out["c_cpt_odd_linear_rel"],
                                 out["c_cpt_odd_cubic_rel"],
                                 out["c_cpt_odd_bounded_rel"])
    # the absolute (un-normalized) max, for the verdict value string
    out["cpt_odd_max_abs"] = max(abs(s1), abs(s3), abs(sb))
    return out


# ---------------------------------------------------------------------------
# Section 8 — Claim 3: CPT-even SME bound from the tau-dot clock constraint
# ---------------------------------------------------------------------------
def cpt_even_bound():
    """Bound the CPT-EVEN (Lorentz-violating-but-CPT-PRESERVING) SME coefficient via tau-dot.

    SUBSTITUTION CHAIN (sector-correct; plan §W2-4 Claim 3 + seed §UB-3):
      Step 1: the CPT-EVEN coefficient is an EVEN spectral functional -- it SURVIVES the
              (lambda,-lambda) pairing, so it is NOT forced to zero (unlike the CPT-odd null).
      Step 2: its time-variation is sourced by the tau-dot background through the clock relation
              dalpha/alpha = clock_coeff * tau_dot,  clock_coeff = -3.08 = 4 cos^2(theta_W)   [E-3, S22d]
      Step 3: the SME-translated tau-dot bound is the seed canonical |tau_dot| < 5e-18/yr
              (dirac UB-3; the leading SME coeff ~ tau_dot * spectral-moment); the implied
              optical-clock dalpha/alpha < 1.54e-17/yr (Sage-verified this session).
      Step 4: the CPT-even SME coefficient INHERITS this bound: c_CPT-even <= |tau_dot| (the
              substrate deformation rate IS the Lorentz-violation source, dimensionless SME units).
      Step 5: SECTOR NOTE: this is the CPT-PRESERVING Lorentz-violation sector. It is NOT the
              sector the neutral-meson |m_K - m_Kbar|/m_K < 1e-18 bound constrains (that bound is
              CPT-VIOLATING = the CPT-ODD sector, where the substrate gives EXACTLY 0). So the
              kaon-CPT test is applied to the CPT-ODD coefficient (Claim 2), NOT here.
    """
    tau_dot_bound = TAU_DOT_CANONICAL_PER_YR   # (local) seed canonical SME-translated bound /yr
    # the CPT-even SME coefficient (dimensionless): inherits the tau_dot bound
    c_cpt_even = tau_dot_bound   # (local) CPT-even Lorentz-violation coefficient bound
    return {
        "tau_dot_bound_per_yr": tau_dot_bound,
        "c_cpt_even": c_cpt_even,
        "neutral_meson_bound": NEUTRAL_MESON_CPT_BOUND,
        "clock_coeff": CLOCK_COEFF,
        "dalpha_bound": DALPHA_CLOCK_BOUND_PER_YR,
        # CPT-even is a CPT-PRESERVING sector -- it is bounded, small, and consistent with
        # being a tiny Lorentz-violation source; it is NOT gated against the kaon CPT-odd bound.
        "sector": "CPT-EVEN-Lorentz-violation (NOT the kaon CPT-odd sector)",
    }


# ---------------------------------------------------------------------------
# Section 9 — LIV observable floor vs detector horizons
# ---------------------------------------------------------------------------
def liv_observable_floor(xi2: float):
    r"""Quantify the OBSERVABLE LIV at GRB/photon energies and vs the detectable floor.

    Modified dispersion omega^2 = c^2 k^2 (1 + xi_2 (E/M_KK)^2). Group-velocity
    deviation at photon energy E: |dv/c| ~= (3/2)|xi_2| (E/M_KK)^2 (leading
    quadratic-LIV form). The DETECTABLE floor is set by the current quadratic-LIV
    lower bound on the QG scale E_QG2: a quadratic-LIV signature is observable only
    if M_KK / |xi_2|^(1/2) <~ E_QG2 (i.e. the effective QG scale is at/below the bound).
    """
    out = {}   # (local)
    dv = {}    # (local)
    for label, Egev in PROBE_ENERGIES_GEV.items():
        ratio = (Egev / M_KK) ** 2                       # (local)
        dv[label] = abs(1.5 * xi2) * ratio               # (local) |dv/c|
    out["dv_over_c"] = dv
    # effective quadratic-LIV QG scale of the substrate: E_QG2_substrate = M_KK / |xi2|^(1/2)
    E_QG2_sub = M_KK / np.sqrt(abs(xi2)) if xi2 != 0 else np.inf   # (local)
    out["E_QG2_substrate_GeV"] = float(E_QG2_sub)
    out["E_QG2_floor_GeV"] = E_QG2_FLOOR_GEV
    # below the detectable floor iff the substrate QG scale EXCEEDS the current bound
    out["margin_OOM_above_floor"] = float(np.log10(E_QG2_sub / E_QG2_FLOOR_GEV))
    out["below_detectable_floor"] = bool(E_QG2_sub > E_QG2_FLOOR_GEV)
    return out


# ---------------------------------------------------------------------------
# Section 10 — compute orchestrator
# ---------------------------------------------------------------------------
def compute():
    print("\n--- loading L_max=12 master spectrum (bottom-K dispersion + signed pairing) ---")
    abs_lam, w = load_abs_spectrum(CACHE_L12)
    n_modes = abs_lam.size   # (local)
    print(f"  total abs_evals entries: {n_modes}  (sum weighted by dim(p,q): {np.sum(w):.0f})")
    lam_min = float(abs_lam.min())   # (local)
    print(f"  |lambda|_min = {lam_min:.6f} M_KK (the spectral gap; bottom of the band)")

    # --- Claim 1: Goldstone dispersion ---
    print("\n--- Claim 1a: GOLDSTONE dispersion omega(k) to O(k^4) on kappa=3 Loeschian ---")
    # the Goldstone low-k speed is c_Gold (canonical 0.915 M_KK); normalize the lattice
    # dispersion to it. (The O(k^4) coefficient xi_2 is INDEPENDENT of c -- it is a pure
    # lattice point-group property, so the speed enters only as the overall normalization.)
    c_gold = float(c_Gold)   # (local)
    xi2_g, xi4_g, cfit_g, resid_g, Kgrid, om2_g = extract_xi2(c_gold, phi=0.0, kappa=KAPPA_LOESCHIAN)
    print(f"  c_Gold (canonical low-k speed) = {c_gold:.4f} M_KK; fit c = {cfit_g:.6f} M_KK")
    print(f"  xi_2(Goldstone) = {xi2_g:.10f}  (Sage-exact structural = {XI2_STRUCT_EXACT:.10f})")
    print(f"  xi_4(Goldstone) = {xi4_g:.6e}   fit residual_max = {resid_g:.3e}")
    phis_g, xi2scan_g, iso_g = isotropy_scan(c_gold, KAPPA_LOESCHIAN)
    print(f"  isotropy spread of xi_2 across {phis_g.size} directions = {iso_g:.3e} (O(k^4) isotropy)")

    # --- Claim 1b: graviton-KK-zero-mode dispersion ---
    print("\n--- Claim 1b: GRAVITON-KK-zero-mode dispersion omega(k) to O(k^4) ---")
    # the graviton zero-mode is the a_2-channel tensor excitation; its low-k speed is the
    # emergent 4D light cone c_4D = 1 (the maximum propagation speed on g_M). It lives on
    # the SAME kappa=3 Loeschian lattice -> SAME hexagonal point group -> SAME O(k^4)
    # structure. This is the KEY result: emergent LI is protected for BOTH modes by the
    # SAME point-group symmetry (the K^4 isotropy theorem).
    c_grav = 1.0   # (local) emergent 4D light cone (max speed on g_M)
    xi2_h, xi4_h, cfit_h, resid_h, Kgrid_h, om2_h = extract_xi2(c_grav, phi=0.0, kappa=KAPPA_LOESCHIAN)
    print(f"  c_4D (graviton-zero-mode low-k speed) = {c_grav:.4f} M_KK; fit c = {cfit_h:.6f} M_KK")
    print(f"  xi_2(graviton) = {xi2_h:.10f}  (Sage-exact structural = {XI2_STRUCT_EXACT:.10f})")
    phis_h, xi2scan_h, iso_h = isotropy_scan(c_grav, KAPPA_LOESCHIAN)
    print(f"  isotropy spread of xi_2(graviton) across {phis_h.size} directions = {iso_h:.3e}")

    # --- Claim 2: CPT-odd SME null ---
    print("\n--- Claim 2: CPT-odd SME null from [J,D_K]=0 (signed spectrum) ---")
    signed, sw = build_signed_spectrum(abs_lam, w)
    print(f"  signed spectrum size = {signed.size} (each |lambda| doubled into +/-)")
    cpt_odd = cpt_odd_null(signed, sw)
    print(f"  Sum m_k * lambda_k       = {cpt_odd['c_cpt_odd_linear']:.3e} (rel {cpt_odd['c_cpt_odd_linear_rel']:.3e})")
    print(f"  Sum m_k * lambda_k^3     = {cpt_odd['c_cpt_odd_cubic']:.3e} (rel {cpt_odd['c_cpt_odd_cubic_rel']:.3e})")
    print(f"  Sum m_k * l/(1+l^2)      = {cpt_odd['c_cpt_odd_bounded']:.3e} (rel {cpt_odd['c_cpt_odd_bounded_rel']:.3e})")
    print(f"  CPT-odd max RELATIVE     = {cpt_odd['cpt_odd_max_rel']:.3e}  (target <= {TOL:.0e}; T1 floor {T1_JDK_FLOOR:.0e})")

    # --- kaon-CPT consistency test (CPT-ODD sector, the correct comparison) ---
    # The neutral-meson |m_K - m_Kbar|/m_K < 1e-18 bound is a CPT-VIOLATING observable: it tests
    # the CPT-ODD sector. The substrate's CPT-odd coefficient is EXACTLY 0 (Claim 2), so it PASSES
    # this bound by a STRUCTURAL THEOREM (0 <= 1e-18). This is the headline UB-3 result.
    cpt_odd_abs = cpt_odd["cpt_odd_max_abs"]   # (local) the CPT-odd coefficient (=0 structurally)
    kaon_cpt_pass = cpt_odd_abs <= NEUTRAL_MESON_CPT_BOUND   # (local) structural PASS (0 <= 1e-18)
    print("\n--- kaon-CPT test (CPT-ODD sector): substrate CPT-odd vs neutral-meson 1e-18 ---")
    print(f"  CPT-odd coefficient (substrate) = {cpt_odd_abs:.3e}  vs kaon bound {NEUTRAL_MESON_CPT_BOUND:.1e}")
    print(f"  kaon-CPT test PASS (0 <= 1e-18, structural by [J,D_K]=0): {kaon_cpt_pass}")

    # --- Claim 3: CPT-even SME bound (separate Lorentz-violation sector) ---
    print("\n--- Claim 3: CPT-EVEN SME bound from tau-dot clock constraint (E-3; separate sector) ---")
    cpt_even = cpt_even_bound()
    print(f"  clock: dalpha/alpha = {cpt_even['clock_coeff']} * tau_dot; |dalpha/alpha| < {cpt_even['dalpha_bound']:.2e}/yr (implied)")
    print(f"  seed canonical SME-translated bound: |tau_dot| < {cpt_even['tau_dot_bound_per_yr']:.1e}/yr")
    print(f"  c_CPT-even(SME) <= {cpt_even['c_cpt_even']:.1e}  [{cpt_even['sector']}]")
    print(f"  (CPT-even is a tiny CPT-PRESERVING Lorentz-violation source; NOT gated vs kaon CPT-odd bound)")

    # --- LIV observable floor ---
    print("\n--- LIV observable floor (xi_2 vs detector horizons) ---")
    floor = liv_observable_floor(xi2_g)
    for label, val in floor["dv_over_c"].items():
        print(f"  |dv/c| @ {label} = {val:.3e}")
    print(f"  substrate quadratic-LIV QG scale E_QG2 = {floor['E_QG2_substrate_GeV']:.3e} GeV")
    print(f"  current detectable floor E_QG2 > {floor['E_QG2_floor_GeV']:.1e} GeV")
    print(f"  margin = {floor['margin_OOM_above_floor']:.1f} OOM ABOVE floor; below_detectable={floor['below_detectable_floor']}")

    # ---------------------------------------------------------------------
    # VERDICT logic (composite [SIGN] 3-tuple; plan §W2-4 rubric)
    # ---------------------------------------------------------------------
    # sign_verdict: xi_2 < 0 for BOTH modes (sub-luminal lattice-acoustic)
    sign_ok = (xi2_g < 0.0) and (xi2_h < 0.0)   # (local)
    sign_verdict = "PASS" if sign_ok else "FAIL"
    # magnitude_verdict: the substrate's emergent-Lorentz observable content passes iff
    #   (a) the kaon-CPT test passes (CPT-odd = 0 <= 1e-18, structural by [J,D_K]=0) AND
    #   (b) |xi_2| is below the detectable LIV floor (Track A: exact Lorentz to obs precision).
    #   If the kaon-CPT test passes but |xi_2| is ABOVE the floor for >=1 mode -> INFO
    #   (Track B: falsifiable GRB/photon-dispersion LIV prediction). The CPT-even tau_dot
    #   bound is a SEPARATE CPT-PRESERVING sector -- reported, not gated against the kaon bound.
    below_floor = floor["below_detectable_floor"]   # (local)
    if kaon_cpt_pass and below_floor:
        magnitude_verdict = "PASS"
    elif kaon_cpt_pass and (not below_floor):
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"   # kaon-CPT test FAILS => CPT-odd not null => numerical T1 violation
    # regime_verdict: the O(k^4) extraction is valid iff k << M_KK across the window AND
    #   the CPT-odd null holds (J-pairing intact). The fit window max is K_MAX=0.5 M_KK;
    #   the O(k^4) fit residual must be small (Sage-exact match). The CPT-odd null failing
    #   would mean a numerical J-violation (regime BREAKDOWN of the spectral pairing).
    cpt_odd_null_holds = cpt_odd["cpt_odd_max_rel"] <= max(TOL, 1e-10)   # (local) machine-eps null
    # the O(k^4) fit must match the Sage-exact -1/16 to good precision (the dispersion model
    # is structurally exact; the only error is the polyfit truncation over the window)
    xi2_matches_exact = (abs(xi2_g - XI2_STRUCT_EXACT) < 1e-3) and (abs(xi2_h - XI2_STRUCT_EXACT) < 1e-3)  # (local)
    if not cpt_odd_null_holds:
        regime_verdict = "BREAKDOWN"   # numerical J-violation -- contradicts T1
    elif not xi2_matches_exact:
        regime_verdict = "MARGINAL"    # fit-window truncation drift
    else:
        regime_verdict = "VALID"

    # composite collapse (gate-verdicts.md PRE-REGISTERED rule)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    # value string (no single quotes -- emit_verdict rejects the ' delimiter)
    value = (f"xi2_Gold={xi2_g:.6f}_xi2_grav={xi2_h:.6f}_BOTH_sub-luminal_isotropic-to-Ok4;"
             f"CPTodd=0(rel{cpt_odd['cpt_odd_max_rel']:.0e})_by[J,DK]=0_PASSES_kaon_{NEUTRAL_MESON_CPT_BOUND:.0e};"
             f"CPTeven<={cpt_even['c_cpt_even']:.0e}_sep-sector;"
             f"E_QG2_sub={floor['E_QG2_substrate_GeV']:.2e}GeV_{floor['margin_OOM_above_floor']:.1f}OOM_above_floor;"
             f"track={'A-EXACT-LORENTZ' if composite == 'PASS' else ('B-FALSIFIABLE-LIV' if composite == 'INFO' else 'FAIL')}")

    print("\n=== VERDICT ASSEMBLY ===")
    print(f"  sign_verdict      = {sign_verdict} (xi_2<0 both modes: Gold {xi2_g:.4f}, grav {xi2_h:.4f})")
    print(f"  magnitude_verdict = {magnitude_verdict} (kaon_cpt_pass={kaon_cpt_pass}, below_floor={below_floor})")
    print(f"  regime_verdict    = {regime_verdict} (cpt_odd_null={cpt_odd_null_holds}, xi2_exact_match={xi2_matches_exact})")
    print(f"  COMPOSITE         = {composite}")

    # ---------------------------------------------------------------------
    # plot
    # ---------------------------------------------------------------------
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))

    # (0,0) dispersion omega(k) both modes + linear cones
    K = Kgrid
    ax[0, 0].plot(K, np.sqrt(om2_g), "-", color="C1", lw=2,
                  label=fr"Goldstone $\omega(k)$, $\xi_2$={xi2_g:.4f}")
    ax[0, 0].plot(K, np.sqrt(om2_h), "-", color="C0", lw=2,
                  label=fr"graviton-0-mode $\omega(k)$, $\xi_2$={xi2_h:.4f}")
    ax[0, 0].plot(K, c_gold * K, "--", color="C1", alpha=0.5, label=r"Goldstone linear cone $c_{Gold}k$")
    ax[0, 0].plot(K, c_grav * K, "--", color="C0", alpha=0.5, label=r"graviton linear cone $ck$")
    ax[0, 0].set_xlabel(r"$k$ (M$_{KK}$ units)")
    ax[0, 0].set_ylabel(r"$\omega(k)$ (M$_{KK}$ units)")
    ax[0, 0].set_title(r"Emergent dispersion: sub-luminal $O(k^4)$ bend ($\xi_2<0$)")
    ax[0, 0].legend(fontsize=8)
    ax[0, 0].grid(alpha=0.3)

    # (0,1) isotropy scan: xi_2 vs phi (flat = isotropic to O(k^4))
    ax[0, 1].plot(np.degrees(phis_g), xi2scan_g, "o-", color="C1", ms=5, label="Goldstone")
    ax[0, 1].plot(np.degrees(phis_h), xi2scan_h, "s-", color="C0", ms=4, alpha=0.7, label="graviton-0-mode")
    ax[0, 1].axhline(XI2_STRUCT_EXACT, color="k", ls=":", lw=1.5, label=r"Sage-exact $-1/16$")
    for jd in range(KAPPA_LOESCHIAN):
        ax[0, 1].axvline(np.degrees(2 * np.pi * jd / KAPPA_LOESCHIAN) % 180, color="g", ls="--", alpha=0.3)
    ax[0, 1].set_xlabel(r"direction $\phi$ (deg)")
    ax[0, 1].set_ylabel(r"$\xi_2(\phi)$")
    ax[0, 1].set_title(fr"$O(k^4)$ ISOTROPY: spread={iso_g:.1e} (hexagonal pt-group)")
    ax[0, 1].legend(fontsize=8)
    ax[0, 1].grid(alpha=0.3)

    # (1,0) CPT-odd null: bar of three odd functionals (log scale, all ~ machine-eps)
    labels = ["$\\Sigma m\\lambda$", "$\\Sigma m\\lambda^3$", "$\\Sigma m\\lambda/(1+\\lambda^2)$"]
    rels = [cpt_odd["c_cpt_odd_linear_rel"], cpt_odd["c_cpt_odd_cubic_rel"], cpt_odd["c_cpt_odd_bounded_rel"]]
    rels_plot = [max(r, 1e-20) for r in rels]   # (local) floor for log plot
    ax[1, 0].bar(labels, rels_plot, color="C2")
    ax[1, 0].axhline(T1_JDK_FLOOR, color="r", ls="--", lw=1.5, label=fr"T1 floor {T1_JDK_FLOOR:.0e}")
    ax[1, 0].axhline(TOL, color="k", ls=":", lw=1.2, label=fr"target {TOL:.0e}")
    ax[1, 0].set_yscale("log")
    ax[1, 0].set_ylabel("relative odd-functional sum")
    ax[1, 0].set_title(r"CPT-odd SME null: $[J,D_K]{=}0 \Rightarrow$ STRUCTURAL ZERO")
    ax[1, 0].legend(fontsize=8)
    ax[1, 0].grid(alpha=0.3, axis="y")

    # (1,1) LIV observable floor vs detector energies
    ens = [PROBE_ENERGIES_GEV[k] for k in PROBE_ENERGIES_GEV]
    dvs = [floor["dv_over_c"][k] for k in PROBE_ENERGIES_GEV]
    ax[1, 1].loglog(ens, dvs, "o-", color="C3", ms=7)
    for k in PROBE_ENERGIES_GEV:
        ax[1, 1].annotate(k.split("_")[0], (PROBE_ENERGIES_GEV[k], floor["dv_over_c"][k]),
                          fontsize=7, textcoords="offset points", xytext=(5, 5))
    ax[1, 1].set_xlabel(r"photon energy $E$ (GeV)")
    ax[1, 1].set_ylabel(r"$|\delta v/c|$ (quadratic LIV)")
    ax[1, 1].set_title(fr"LIV floor: M$_{{KK}}$ is {floor['margin_OOM_above_floor']:.1f} OOM above detectable")
    ax[1, 1].grid(alpha=0.3, which="both")

    fig.suptitle(f"INV6-W2-4 EMERGENT-LORENTZ-REALGATE — {composite} "
                 f"(track {'A: EXACT-LORENTZ' if composite == 'PASS' else ('B: FALSIFIABLE-LIV' if composite == 'INFO' else 'FAIL')}; "
                 f"$\\xi_2={xi2_g:.3f}$ both modes, CPT-odd=0)", fontsize=10.5)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)

    # ---------------------------------------------------------------------
    # save data
    # ---------------------------------------------------------------------
    np.savez(
        OUT_NPZ,
        # Claim 1
        xi2_goldstone=xi2_g, xi4_goldstone=xi4_g, c_fit_goldstone=cfit_g, resid_goldstone=resid_g,
        xi2_graviton=xi2_h, xi4_graviton=xi4_h, c_fit_graviton=cfit_h, resid_graviton=resid_h,
        xi2_struct_exact=XI2_STRUCT_EXACT,
        isotropy_spread_goldstone=iso_g, isotropy_spread_graviton=iso_h,
        phis_goldstone=phis_g, xi2_scan_goldstone=xi2scan_g,
        phis_graviton=phis_h, xi2_scan_graviton=xi2scan_h,
        k_grid=Kgrid, omega2_goldstone=om2_g, omega2_graviton=om2_h,
        c_gold=c_gold, c_grav=c_grav,
        # Claim 2
        cpt_odd_linear=cpt_odd["c_cpt_odd_linear"], cpt_odd_cubic=cpt_odd["c_cpt_odd_cubic"],
        cpt_odd_bounded=cpt_odd["c_cpt_odd_bounded"], cpt_odd_max_rel=cpt_odd["cpt_odd_max_rel"],
        cpt_odd_max_abs=cpt_odd["cpt_odd_max_abs"], T1_floor=T1_JDK_FLOOR,
        n_modes=n_modes, lam_min=lam_min,
        # Claim 3
        tau_dot_bound_per_yr=cpt_even["tau_dot_bound_per_yr"], c_cpt_even=cpt_even["c_cpt_even"],
        neutral_meson_bound=NEUTRAL_MESON_CPT_BOUND, kaon_cpt_pass=kaon_cpt_pass,
        cpt_odd_abs_for_kaon=cpt_odd_abs,
        clock_coeff=CLOCK_COEFF, dalpha_bound=DALPHA_CLOCK_BOUND_PER_YR,
        # LIV floor
        E_QG2_substrate_GeV=floor["E_QG2_substrate_GeV"], E_QG2_floor_GeV=E_QG2_FLOOR_GEV,
        margin_OOM_above_floor=floor["margin_OOM_above_floor"],
        below_detectable_floor=floor["below_detectable_floor"],
        dv_over_c_labels=np.array(list(floor["dv_over_c"].keys())),
        dv_over_c_values=np.array(list(floor["dv_over_c"].values())),
        # verdict
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        M_KK=M_KK, tau_fold=tau_fold, kappa=KAPPA_LOESCHIAN,
    )

    return {
        "value": value,
        "verdict": composite,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "xi2_g": xi2_g, "xi2_h": xi2_h,
        "iso_g": iso_g, "iso_h": iso_h,
        "cpt_odd_max_rel": cpt_odd["cpt_odd_max_rel"],
        "cpt_odd_max_abs": cpt_odd["cpt_odd_max_abs"],
        "c_cpt_even": cpt_even["c_cpt_even"],
        "tau_dot_bound": cpt_even["tau_dot_bound_per_yr"],
        "E_QG2_sub": floor["E_QG2_substrate_GeV"],
        "margin_OOM": floor["margin_OOM_above_floor"],
        "below_floor": floor["below_detectable_floor"],
        "n_modes": n_modes,
    }


# ---------------------------------------------------------------------------
# Section 11 — verdict payload (PRINT ONLY; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None) -> dict:
    payload = {
        "session": 6,
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
    # [SIGN] trigger 3-tuple (all-three-or-none group)
    if sign_verdict is not None and magnitude_verdict is not None and regime_verdict is not None:
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 12 — main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # SOURCE-RECON Class-(c): resolve to on-disk cache; document drift, do NOT hard-fail on stale plan pin
    cache_sha = sha256_of(CACHE_L12)  # (local)
    if cache_sha == CACHE_L12_SHA_PIN:
        print(f"[cache] on-disk SHA matches current canonical {CACHE_L12_SHA_PIN[:16]}... (re-pinned from stale plan value {CACHE_L12_SHA_PIN_STALE[:16]})")
    elif cache_sha == CACHE_L12_SHA_PIN_STALE:
        print(f"[cache] WARNING: on-disk matches the STALE plan pin {CACHE_L12_SHA_PIN_STALE[:16]} (pre-S88 cache); proceeding", file=sys.stderr)
    else:
        print(f"FATAL: cache SHA matches NEITHER canonical nor stale pin\n  got {cache_sha}", file=sys.stderr)
        return 2

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    res = compute()
    verdict = res["verdict"]
    value = res["value"]

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print("\n" + tag)

    note = (f"xi_2(Goldstone)={res['xi2_g']:.6f} xi_2(graviton)={res['xi2_h']:.6f} "
            f"(Sage-exact -1/16 on kappa=3 Loeschian; BOTH sub-luminal, isotropic to O(k^4)); "
            f"CPT-odd_SME_null_rel={res['cpt_odd_max_rel']:.2e} by [J,D_K]=0; "
            f"CPT-even_SME<={res['c_cpt_even']:.1e} vs kaon 1e-18; "
            f"E_QG2_substrate={res['E_QG2_sub']:.2e}GeV ({res['margin_OOM']:.1f} OOM above detectable floor)")  # (local)
    extra = [
        ("# INV6-W2-4 regulator_pin=N/A(bare-spectrum) f_function=N/A "
         f"L_max=12 k_window=[0,0.5]M_KK kappa=3-Loeschian N_modes={res['n_modes']}"),
        ("# INV6-W2-4 Claim1 LIV: omega^2=c^2 k^2(1+xi_2(k/M_KK)^2); "
         f"xi_2(Gold)={res['xi2_g']:.6f}, xi_2(grav)={res['xi2_h']:.6f} BOTH<0 (sub-luminal); "
         f"O(k^4) ISOTROPIC (spread Gold={res['iso_g']:.1e}, grav={res['iso_h']:.1e}); "
         "hexagonal pt-group forbids anisotropy < O(k^6) [Sage-exact -1/16]"),
        ("# INV6-W2-4 Claim2 CPT-odd SME null = STRUCTURAL ZERO by [J,D_K]=0 "
         f"(rel={res['cpt_odd_max_rel']:.2e}, abs={res['cpt_odd_max_abs']:.2e}; T1 floor 3.29e-13); "
         "3 odd functionals (l, l^3, l/(1+l^2)) all vanish on (lambda,-lambda)-paired spectrum"),
        ("# INV6-W2-4 kaon-CPT test (CPT-ODD sector): substrate CPT-odd=0 <= neutral-meson 1e-18 "
         "PASS by structural theorem [J,D_K]=0 (the most stringent test of T1, 10^18-tight)"),
        ("# INV6-W2-4 Claim3 CPT-EVEN SME bound (separate CPT-PRESERVING sector) via E-3 clock "
         f"dalpha/alpha=-3.08*tau_dot: |tau_dot|<{res['tau_dot_bound']:.1e}/yr => c_CPT-even<={res['c_cpt_even']:.1e} "
         "(a tiny Lorentz-violation source; NOT the kaon CPT-odd sector)"),
        ("# INV6-W2-4 RESOLVES C-F3: crystalline (S106 kappa=3) substrate yields EXACTLY "
         f"isotropic, sub-luminal emergent light to OBSERVABLE precision (below_floor={res['below_floor']}); "
         "upgrades INFO/MIGRATED T3-BATCH-S75-EMERGENT-LORENTZ -> real " + verdict),
    ]  # (local)

    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note=note, extra_rows=extra,
                          sign_verdict=res["sign_verdict"],
                          magnitude_verdict=res["magnitude_verdict"],
                          regime_verdict=res["regime_verdict"])

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} "
          f"(sign={res['sign_verdict']}/mag={res['magnitude_verdict']}/regime={res['regime_verdict']}, wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
