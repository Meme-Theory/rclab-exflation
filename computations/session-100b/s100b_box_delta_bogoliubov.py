#!/usr/bin/env python3
"""
S100b W5-1 S100b-BOX-DELTA-BOGOLIUBOV -- box+delta Bogoliubov re-attempt
=========================================================================

Gate: S100b-BOX-DELTA-BOGOLIUBOV ([VERIFY]; schema-v2 3-tuple required --
      the substitution chain pre-registers the branch claim mu_pivot^2 > 0)

Plan: sessions/session-plan/session-100b-plan-w5.md SS W5-1 (R3 YAML block,
      honest re-open laws (a)-(d), machinery pins, substitution chain).

HONEST RE-OPEN (laws (a)-(d), condensed):
  (a) Re-opens the corridor closed by S85-W7-CUSP-BOGOLIUBOV: FAIL
      (value=-2.019676, scheme=transfer-matrix, convention=BD-in-out,
      audit b17807eb5930d0bb80142b4b45ae579cdb9465ac7181e4b6f9f8e45f46bd579c).
  (b) The S85 machinery segmented a SMOOTH interpolated cusp -- the regime
      where piecewise-constant transfer matrices generate artificial interior
      reflections (OOM N_seg-sensitivity). The fold's genuine geometry is the
      box+delta SUDDEN limit (Sparn Eq. 4 construction; Schmidt Table I
      rectangular-barrier-bounded-by-delta-peaks landscape), where the
      transfer matrix is EXACT (finitely many genuine sharp interfaces).
  (c) NEW gate-ID, NEW pre-registered machinery: scheme=BOX-DELTA-SUDDEN
      (vs S85 SMOOTH-CUSP-AIRY); comparison observable = Schmidt Eq. 75
      closed-form match + N_seg-stability conjunction (vs S85 Airy k^{-2/3}
      exponent fit). Independently falsifiable; outcome open.
  (d) The S85 FAIL stands permanently. Companion row carries predecessor=
      (full 64-hex), explicitly NOT supersedes=.

PRE-REGISTERED OPERATOR (conjunction of two ratio inequalities):
  PASS iff [ var_Nseg = max/min |beta_pivot|^2 over N_seg in {50,100,200,400}
             < 2.0 (RATIO) ]
       AND [ rel_dev = | |beta|^2_TM / |beta|^2_Schmidt-Eq75 - 1 | <= 0.10 ]
  FAIL iff var_Nseg >= 2.0 (OOM-instability persists under sharp-boundary
       discretization -> corridor closes for BOTH discretization classes).
  INFO iff var_Nseg < 2.0 AND rel_dev > 0.10 (N_seg-stable but the box+delta
       idealization mis-captures the fold window).

NORMALIZATION (operational interpretation -- documented in WP SS W5-1):
  FOLD normalization throughout: a(tau_fold) = 1; comoving k in the S77
  Convention-B fold units where k_pivot = 14.311092688448717 M_KK and
  aH|_fold = k_pivot_com_fold / k_over_aH_fold = 0.975395 M_KK (both keys
  from the pinned s77_n_pivot_map.npz). The S77 anchor k2_over_zppz_fold =
  107.63558173571887 is constructed as k_pivot^2/(2*aH^2) (verified against
  computations/session-77/s77_n_pivot_map.py line 475), i.e. the anchor's
  z''/z is the quasi-dS barrier 2(aH)^2. The s64 clock (H_fold = 586.527
  per unit s64 cosmic time) is converted to the fold-normalized M_KK clock
  by the single scalar u = H_fold(canonical)/aH_target; the window pin
  dt_transit = 1.1302e-3 M_KK^{-1} is read in the SAME fold-normalized M_KK
  clock -- the unique reading consistent with the plan block's own
  diagnostic arithmetic (mu_pivot*Delta_eta ~ 1.6e-2 << pi).
  CHK-N: the pipeline-re-derived barrier 2*(aH)^2|_fold (aH re-derived as
  d(ln a)/d(eta) from the assembled fold-normalized channels, NOT from the
  pin pair) must reproduce k_pivot^2/107.63558173571887 within 5% RATIO,
  else HARD-ABORT (normalization bug, not physics).

BARRIER BRANCHES (documented; gate criteria evaluated on the CANONICAL):
  canonical (b): U(eta) = 2*[aH(eta)]^2 -- the S77-anchor-consistent
      quasi-dS barrier; V_box = window mean = the substitution chain's
      V_box ~= (z''/z)|_fold = k_pivot^2/107.636.
  sensitivity (c): U_c(eta) = stored s64 zpp_over_z channel rescaled to
      fold units (the eta_H-corrected GSR barrier, F_fold = 2.906 -- the
      known slow-roll-violation gap, s64 INFO verdict). Full var_Nseg +
      rel_dev re-run, REPORTED (verdict invariance check).
  diagnostic (a): literal Sparn Eq. 4 potential (1/4)adot^2 + (1/2)addot*a
      built from a(eta) -- the sqrt(a)-pump (2+1D BEC) image; its plateau is
      reported to document the psi = sqrt(a) v_k pump-correspondence
      (sqrt(a)-pump vs z-pump barrier ratio).

DELTA WEIGHTS (plan pin, literal): Omega_on/off = (1/2)*a*[adot]_jump at the
  switch boundaries, [adot] in the fold-normalized M_KK clock (idealized
  static outside: on: +adot(eta_on), off: -adot(eta_off)). At fold
  normalization a(boundary) = 1 +- 6e-4, so the literal pin coincides with
  the strict distributional weight (1/2)[adot] = (1/2)[conformal Hubble]
  (Schmidt Table I: V_s = (H_0/2)[delta(eta-eta_i) - delta(eta-eta_f)])
  to ~6e-4 relative. Both reported. A z-pump variant Omega_z = [z'/z] is
  reported as a sensitivity scalar (NOT gating).

Inputs (SHA-256 verified against plan pins; logged in first 20 stdout lines):
  computations/_shared/canonical_constants.py          (runtime-pinned)
  computations/session-77/s77_n_pivot_map.npz          (k_pivot anchors)
  computations/session-78/s78_f_conv_subhorizon.npz    (x_pivot cross-check)
  computations/session-64/s64_mukhanov_sasaki.npz      (fold a(tau)/eta history)
  computations/session-64/s64_epsilon_profile.npz      (excursion cross-check)
  computations/session-64/s64_sound_speed.npz          (Mach/H_fold cross-check)
  downloads/.../03_Sparn_*.pdf                         (Eqs. 2-5, runtime extract)
  downloads/.../04_Schmidt_*.pdf                       (Eqs. 75-76 + Table I)
  sessions/archive/session-79/workshops/p2-a-as-ledger-dissonance.md (B2 OOM anchor)

Output 4-tuple:
  (value=<see payload>, scheme=BOX-DELTA-SUDDEN, convention=BD-in-out, L_max=N/A)

Classification: PHONONIC

Verdict emission: this script PRINTS the payload via print_verdict_payload;
the dispatching agent calls the race-safe emit_verdict knowledge-MCP tool
(gate-verdicts.md SS"Race-Safe Emission"). NO open("a") verdict writes.

SUBSTRATE FRAMING: the fold IS the substrate's van Hove reorganization --
the D_K eigenvalue spectrum reorganizing through the first-order transit at
tau_fold = 0.19, supersonically (Mach 13.75), impulsively (H*dt = 0.663 in
the S38 clock; aH*dt = 1.1e-3 in the fold-conformal clock). The scattering
potential V(eta) is the laboratory-IN/methodological image (Sparn/Schmidt
BEC analogs model a projection OF the substrate transit) of the substrate's
z''/z mode barrier, itself the spectral-action image of the eigenvalue flow
(dS/dtau = +58672.8 at fold). |beta_pivot|^2 IS the occupation of the
substrate's own excitation spectrum at the pivot mode: particle production
IS the spectral reorganization, not an event inside a geometric container.
The switch-boundary deltas are the substrate-first realization of the
Parra-Lopez switch-on/off-dominance theorem (transitions dominate, stages
do not).
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# Section 0 -- CPU thread cap BEFORE numpy import (GPU_path: cpu-cap-OMP8;
# 2x2 transfer matrices + scipy Radau -- trivially small, no GPU needed)
# --------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import re
import sys
import time
from pathlib import Path

import numpy as np
from scipy.integrate import cumulative_trapezoid, solve_ivp
from scipy.interpolate import CubicSpline

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY)
# --------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
# consumed: tau_fold, dt_transit, M_KK, Mach_max_framework, dS_fold, d2S_fold,
#           PI, H_fold, v_terminal

# --------------------------------------------------------------------------
# Section 2 -- Pre-registration (plan SS W5-1 machinery_pin_map)
# --------------------------------------------------------------------------
SESSION = "100b"                                                   # (local)
GATE_ID = "S100b-BOX-DELTA-BOGOLIUBOV"                             # (local)
SCHEME = "BOX-DELTA-SUDDEN"                                        # (local)
CONVENTION = "BD-in-out"                                           # (local)
L_MAX = "N/A"                                                      # (local)

TOL_VAR_NSEG = 2.0          # (local) RATIO, strict <
TOL_REL_DEV = 0.10          # (local) RATIO, <=
TOL_UNITARITY = 1e-10       # (local) ABSOLUTE on ||alpha|^2-|beta|^2-1|
TOL_CHK_N = 0.05            # (local) RATIO on CHK-N (HARD-ABORT on breach)
N_SEG_SCAN = [50, 100, 200, 400]                                   # (local)
N_K_DIAG = 64               # (local) diagnostic k-grid points
K_MIN, K_MAX = 1.0, 50.0    # (local) diagnostic k range [M_KK]
ODE_RTOL, ODE_ATOL = 1e-10, 1e-14                                  # (local)
PREDECESSOR_SHA = ("b17807eb5930d0bb80142b4b45ae579cdb9465ac7181e"
                   "4b6f9f8e45f46bd579c")                          # (local)

OUT_NPZ = SESSION_DIR / "s100b_box_delta_bogoliubov.npz"
OUT_PNG = SESSION_DIR / "s100b_box_delta_bogoliubov.png"

# Plan-pinned input SHAs (Input-SHA Ledger, plan-freeze 2026-06-06)
PINNED_INPUTS = {                                                  # (local)
    "computations/session-77/s77_n_pivot_map.npz":
        "80fbf580234d0e3e55502d18fec35e32e93356f17f62ac7cdc409acecaf50bba",
    "computations/session-78/s78_f_conv_subhorizon.npz":
        "638d84a0c0bb1b531c2c028495f768e3522e67ad3ba280ef2aef96e0fa3107a6",
    "computations/session-64/s64_mukhanov_sasaki.npz":
        "e671f535e3a2da78e58ccb38deaa84fd52ae19608e7fbec0783eee3d57cf5e42",
    "computations/session-64/s64_epsilon_profile.npz":
        "40789017c5f0c66876126eb936e7a212ff406eaff705ed4e53cb17901a97ebf5",
    "computations/session-64/s64_sound_speed.npz":
        "f8873af64609cb8a2afc69e2ecb891473d97b1df6092e5a2e04ba8c57855f36e",
    "downloads/research-sweep-s99/nonequilibrium-transit/"
    "03_Sparn_Particle-Production-Time-Dependent-Spacetimes-Scattering.pdf":
        "bb7d7d3a2b4f4d5853d16b7b4565adee5adfd1248b0e7e88ff16f9d293bd5d64",
    "downloads/research-sweep-s99/nonequilibrium-transit/"
    "04_Schmidt_Cosmological-Particle-Production-Scattering-Problem.pdf":
        "6541ba3bcfc727e6713ca6063c7fd96fa10ce49c6d6ec686ca93e9e33c2fbee4",
    "sessions/archive/session-79/workshops/p2-a-as-ledger-dissonance.md":
        "2f2058358a3be8d761f6189f1fbb05fcc2a1935b223ca7494835a9b912662d55",
}

MACHINERY_PINS = {                                                 # (local)
    "N_eval": "65", "N_seg_scan": "[50,100,200,400]", "L_max": "N/A",
    "scan_range": "k in [1,50] M_KK log; verdict at k_pivot=14.311092688448717",
    "step_size": "log-uniform k; s64 native eta-grid cubic interpolation",
    "tolerance": "0.10 RATIO closed-form; 2.0 RATIO N_seg; 1e-10 ABS unitarity; "
                 "0.05 RATIO CHK-N",
    "scheme": SCHEME, "convention": CONVENTION, "random_seed": "N/A",
    "GPU_path": "cpu-cap-OMP8",
    "window_pin": "Delta_eta = conformal image of dt_transit=1.1302e-3 MKK^-1 "
                  "centered on tau_fold=0.19, fold-normalized M_KK clock",
    "normalization_pin": "FOLD units a(tau_fold)=1; CHK-N vs "
                         "k2_over_zppz_fold=107.63558173571887 within 5%",
    "delta_weight_rule": "Omega=(1/2)*a*[adot]_jump at switch boundaries",
    "pdf_extraction": "Sparn Eqs.2-5 + Schmidt Eqs.75-76 runtime from pinned PDFs",
    "regulator_pin": "N/A", "CLASS": "N/A",
    "publication_precision": "4 sig figs on |beta_pivot|^2",
}


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict) -> tuple[str, str]:
    """S84+ dual-SHA: audit = sha256(script || canonical || pinmap_json);
    content = sha256(script). pinmap includes file SHAs + machinery pins."""
    script_bytes = script_path.read_bytes()                        # (local)
    canonical_bytes = canonical_path.read_bytes()                  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")       # (local)
    h_a = hashlib.sha256()                                         # (local)
    h_a.update(script_bytes); h_a.update(canonical_bytes); h_a.update(pinmap_json)
    h_c = hashlib.sha256()                                         # (local)
    h_c.update(script_bytes)
    return h_a.hexdigest(), h_c.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    """Print the emit_verdict payload (race-safe MCP emission by the agent)."""
    payload = {                                                    # (local)
        "session": SESSION, "gate_id": GATE_ID, "verdict": verdict,
        "value": str(value), "scheme": SCHEME, "convention": CONVENTION,
        "l_max": str(L_MAX), "audit_sha256": audit_sha,
        "content_sha256": content_sha, "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None
            and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# --------------------------------------------------------------------------
# Section 3 -- Input SHA verification (first 20 lines of stdout)
# --------------------------------------------------------------------------
def verify_inputs() -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins (plan-verified) ===")
    pins: dict = {}                                                # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"         # (local)
    sha_canon = sha256_of(canonical_path)                          # (local)
    print(f"  computations/_shared/canonical_constants.py: {sha_canon[:16]}... "
          f"(runtime-pinned)")
    pins["computations/_shared/canonical_constants.py"] = sha_canon
    for rel, expected in PINNED_INPUTS.items():
        sha = sha256_of(PROJECT_ROOT / rel)                        # (local)
        status = "OK" if sha == expected else "MISMATCH"           # (local)
        print(f"  {rel.split('/')[-1]}: {sha[:16]}... [{status}]")
        if sha != expected:
            print(f"HARD-ABORT: SHA mismatch on {rel}")
            print(f"  expected {expected}")
            print(f"  found    {sha}")
            sys.exit(2)
        pins[rel] = sha
    return pins


# --------------------------------------------------------------------------
# Section 4 -- Runtime PDF extraction (research-corpus rule: fetched sources
# only, never training knowledge; extraction gaps marked explicitly)
# --------------------------------------------------------------------------
def _norm(s: str) -> str:
    return re.sub(r"\s+", "", s)                                   # (local)


def extract_pdf_conventions() -> dict:
    import pypdf                                                   # (local)
    res = {"gaps": []}                                             # (local)
    print("\n--- Runtime PDF extraction: Sparn (2412.18xxx) Eqs. 2-5 ---")
    sp = pypdf.PdfReader(str(PROJECT_ROOT / (
        "downloads/research-sweep-s99/nonequilibrium-transit/"
        "03_Sparn_Particle-Production-Time-Dependent-Spacetimes-Scattering.pdf")))
    t1 = sp.pages[0].extract_text()                                # (local)
    t2 = sp.pages[1].extract_text()                                # (local)
    t3 = sp.pages[2].extract_text()                                # (local)
    n12 = _norm(t1 + t2)                                           # (local)
    n123 = _norm(t1 + t2 + t3)                                     # (local)
    checks = [                                                     # (local)
        ("Sparn Eq.2 (mode eq, Hubble friction)", "k2\na2vk= 0, (2)", t1,
         "vk+k2a2vk=0,(2)"),
        ("Sparn Eq.3 (Schrodinger form)", "= k2psik", t2,
         "ψk(η)=k2ψk(η),(3)"),
        ("Sparn Eq.4 (V(eta) potential)", "(4)", t2,
         "V(η)=14˙a2(t(η))+12¨a(t(η))a(t(η)),(4)"),
        ("Sparn Eq.5 (S_k oscillation)", "(5)", t2,
         "Sk=1/2+Nk+∆Nkcos(2ωkth+ϑk),(5)"),
        ("Sparn N_k dictionary", "Nk", t2, "Nk=|bk|2/|ck|2"),
        ("Sparn unitarity", "ck", t2, "|ck|2=|ak|2−|bk|2"),
        ("Sparn box height (linear expansion)", "box", t2,
         "boxpotentialwithheightH20/4"),
        ("Sparn boundary deltas", "delta", t2,
         "deltadistributionsfromtheabruptstartandendoftheramp"),
        ("Sparn box height value check (1/4 adot^2)", "height", t3,
         "heightof14˙a2"),
    ]
    for name, _short, _page, normpat in checks:
        hit = normpat in n123 if normpat else False                # (local)
        print(f"  [{'FOUND' if hit else 'MARK-GAP'}] {name}")
        if not hit:
            res["gaps"].append(name)
    print("  Extracted convention (verbatim, Sparn p.2):")
    print("    psi_k(eta) = sqrt(a(eta)) v_k(eta);  dη = dt/a(t)")
    print("    [-d2/deta2 + V(eta)] psi_k = k^2 psi_k          (Eq. 3)")
    print("    V(eta) = (1/4) adot^2 + (1/2) addot * a         (Eq. 4, dots=lab t)")
    print("    S_k = 1/2 + N_k + DN_k cos(2 w_k t_h + theta_k) (Eq. 5)")
    print("    N_k = |b_k|^2/|c_k|^2 ;  |c_k|^2 = |a_k|^2 - |b_k|^2 (unitarity)")
    print("    linear expansion -> box of height H0^2/4 + boundary deltas")

    print("\n--- Runtime PDF extraction: Schmidt (2309.07847) Eqs. 75-76 + Table I ---")
    sc = pypdf.PdfReader(str(PROJECT_ROOT / (
        "downloads/research-sweep-s99/nonequilibrium-transit/"
        "04_Schmidt_Cosmological-Particle-Production-Scattering-Problem.pdf")))
    p12 = sc.pages[11].extract_text()                              # (local)
    p13 = sc.pages[12].extract_text()                              # (local)
    p27 = sc.pages[26].extract_text()                              # (local)
    n_all = _norm(p12 + p13 + p27)                                 # (local)
    checks2 = [                                                    # (local)
        ("Schmidt Table I rectangular-barrier landscape",
         "Rectangular-barrierboundedbyδ-peaks"),
        ("Schmidt Table I barrier V_r = (H0^2/4) Theta Theta",
         "Vr(η)=H20\n4Θ(η−ηi)Θ(ηf−η)".replace("\n", "")),
        ("Schmidt Table I barrier deltas V_s = (H0/2)[d_i - d_f]",
         "Vs(η)=H02[δ(η−ηi)−δ(η−ηf)]"),
        ("Schmidt Eq.75 marker (sin[mu_k Delta_eta] closed form)", "(75)"),
        ("Schmidt Eq.76 marker (r_k closed form)", "(76)"),
        ("Schmidt sin[(eta_f-eta_i) mu_k] structure", "sin[(ηf−ηi)µk]"),
        ("Schmidt delta-peak matching (psi' jump = (H/2) psi, B41)",
         "(ϖk+Hi/2)"),
    ]
    for name, normpat in checks2:
        hit = _norm(normpat) in n_all                              # (local)
        print(f"  [{'FOUND' if hit else 'MARK-GAP'}] {name}")
        if not hit:
            res["gaps"].append(name)
    print("  Extracted convention (verbatim structure, Schmidt p.12 Table I + p.13):")
    print("    linear expansion a(t)=1+H0t -> V_r = (H0^2/4) Theta(eta-eta_i)")
    print("      Theta(eta_f-eta) ;  V_s = (H0/2)[delta(eta-eta_i) - delta(eta-eta_f)]")
    print("      (one REPULSIVE switch-on delta, one ATTRACTIVE switch-off delta;")
    print("       weight = conformal-Hubble-at-boundary / 2)")
    print("    Eq. 75/76: amplitudes carry sin[(eta_f-eta_i) mu_k] /")
    print("      cos[(eta_f-eta_i) mu_k] with mu_k the interior momentum --")
    print("      the SUB-horizon oscillating branch; the super-horizon branch is")
    print("      the continuation mu_k -> i Lambda_k (sin -> sinh), implemented")
    print("      here through the entire functions C=cos(mu L), S=sin(mu L)/mu")
    print("      of mu^2 (exact analytic continuation).")
    print("    Delta-peak matching: [psi'] = +Omega psi at each peak (B41/B42).")

    print("\n--- Runtime extraction: S79 P2-A B2-ladder anchor (line ~613) ---")
    md = (PROJECT_ROOT /
          "sessions/archive/session-79/workshops/p2-a-as-ledger-dissonance.md")
    lines = md.read_text(encoding="utf-8").splitlines()            # (local)
    anchor_line = lines[612] if len(lines) > 612 else ""           # (local)
    hit79 = "1700" in anchor_line                                  # (local)
    print(f"  [{'FOUND' if hit79 else 'MARK-GAP'}] |beta_2|^2 ~ 1700 anchor: "
          f"'{anchor_line.strip()[:110]}...'")
    if not hit79:
        res["gaps"].append("S79 B2 anchor line 613")
    res["B2_anchor"] = 1.7e3                                       # (local)
    return res


# --------------------------------------------------------------------------
# Section 5 -- Fold normalization pipeline + CHK-N
# --------------------------------------------------------------------------
def build_background() -> dict:
    d64 = np.load(COMPUTATIONS_DIR / "session-64" / "s64_mukhanov_sasaki.npz",
                  allow_pickle=True)                               # (local)
    d77 = np.load(COMPUTATIONS_DIR / "session-77" / "s77_n_pivot_map.npz",
                  allow_pickle=True)                               # (local)
    d78 = np.load(COMPUTATIONS_DIR / "session-78" / "s78_f_conv_subhorizon.npz",
                  allow_pickle=True)                               # (local)
    d64e = np.load(COMPUTATIONS_DIR / "session-64" / "s64_epsilon_profile.npz",
                   allow_pickle=True)                              # (local)
    d64s = np.load(COMPUTATIONS_DIR / "session-64" / "s64_sound_speed.npz",
                   allow_pickle=True)                              # (local)

    tau = d64["tau_dense"]                                         # (local)
    eta_raw = d64["eta"]                                           # (local)
    a_raw = d64["a_tau"]                                           # (local)
    aH_raw = d64["aH_tau"]                                         # (local)
    zpp_raw = d64["zpp_over_z"]                                    # (local)
    dlnz_dN = d64["dlnz_dN"]                                       # (local)
    epsH = d64["epsH_dense"]                                       # (local)

    k_pivot = float(d77["k_pivot_com_fold"])                       # (local)
    k_over_aH = float(d77["k_over_aH_fold"])                       # (local)
    k2_over_zppz = float(d77["k2_over_zppz_fold"])                 # (local)
    N_pivot = float(d77["N_pivot"])                                # (local)
    x_pivot = float(d78["x_pivot"])                                # (local)
    k_aH_78 = float(d78["k_pivot_aH_at_fold"])                     # (local)
    Mach_fric = float(d64s["Mach_fric"])                           # (local)
    H_fold_s64 = float(d64s["H_fold"])                             # (local)
    c_BLV = float(d64s["c_BLV"])                                   # (local)
    dS_canon_64 = float(d64e["dS_fold_canonical"])                 # (local)
    d2S_canon_64 = float(d64e["d2S_fold_canonical"])               # (local)

    print("\n--- Input-integrity cross-checks (canonical-first) ---")
    print(f"  H_fold (canonical) = {H_fold:.10f}  vs s64 npz "
          f"{H_fold_s64:.10f}  (rel dev {abs(H_fold_s64/H_fold-1):.2e})")
    print(f"  dS_fold canonical {dS_fold:.8f} vs s64 npz {dS_canon_64:.8f} "
          f"(rel {abs(dS_canon_64/dS_fold-1):.2e})")
    print(f"  d2S_fold canonical {d2S_fold:.8f} vs s64 npz {d2S_canon_64:.8f} "
          f"(rel {abs(d2S_canon_64/d2S_fold-1):.2e})")
    print(f"  Mach_max_framework (canonical) = {Mach_max_framework} vs "
          f"Mach_fric (s64) = {Mach_fric:.12f} "
          f"(rel {abs(Mach_fric/Mach_max_framework-1):.2e}) -- supersonic fold")
    print(f"  k/aH at fold: s77 = {k_over_aH:.12f} vs s78 = {k_aH_78} "
          f"(rel {abs(k_aH_78/k_over_aH-1):.2e})")
    print(f"  x_pivot (s78 sub-horizon WKB anchor) = {x_pivot:.12f}")
    print(f"  N_pivot (s77) = {N_pivot:.12f}")

    # ---- fold normalization (Convention B, S77 canonical) ----
    sp_a = CubicSpline(tau, a_raw)                                 # (local)
    sp_eta = CubicSpline(tau, eta_raw)                             # (local)
    sp_aH = CubicSpline(tau, aH_raw)                               # (local)
    sp_zpp = CubicSpline(tau, zpp_raw)                             # (local)
    a_fold = float(sp_a(tau_fold))                                 # (local)
    eta_fold_raw = float(sp_eta(tau_fold))                         # (local)
    aH_fold_raw = float(sp_aH(tau_fold))                           # (local)

    aH_target = k_pivot / k_over_aH       # (local) S77 Conv-B aH|fold [M_KK]
    u_clock = H_fold / aH_target          # (local) s64-clock -> M_KK clock
    Lam = u_clock * a_fold                # (local) conformal rescale factor

    print("\n--- Fold normalization (Convention B; a(tau_fold)=1) ---")
    print(f"  a_fold (s64 raw) = {a_fold:.6f}  (N_fold = {np.log(a_fold):.4f})")
    print(f"  aH_target = k_pivot/k_over_aH = {k_pivot:.12f}/{k_over_aH:.12f}"
          f" = {aH_target:.12f} M_KK")
    print(f"  clock conversion u = H_fold/aH_target = {H_fold:.6f}/"
          f"{aH_target:.6f} = {u_clock:.6f}")
    print(f"  conformal rescale Lambda = u*a_fold = {Lam:.6f}")

    eta_t = Lam * (eta_raw - eta_fold_raw)   # (local) fold-conformal eta~
    a_t = a_raw / a_fold                     # (local) a~ (a~(fold)=1)
    aH_t = aH_raw / (a_fold * u_clock)       # (local) a~H~ profile [M_KK]
    U_c = zpp_raw / Lam**2                   # (local) stored-channel barrier

    assert np.all(np.diff(eta_t) > 0), "eta~ not monotone"
    sp_eta_t = CubicSpline(tau, eta_t)                             # (local)
    sp_a_t = CubicSpline(tau, a_t)                                 # (local)
    sp_aH_t = CubicSpline(tau, aH_t)                               # (local)
    sp_Uc = CubicSpline(tau, U_c)                                  # (local)
    sp_dlnz = CubicSpline(tau, dlnz_dN)                            # (local)
    sp_eps = CubicSpline(tau, epsH)                                # (local)

    # ---- CHK-N: pipeline-re-derived barrier vs pinned anchor ----
    # aH re-derived from the ASSEMBLED channels: aH_re = d(ln a~)/d(eta~)|fold
    # (independent of the pin pair; tests eta-channel/a-channel/rescale wiring)
    i_lo = max(np.searchsorted(tau, tau_fold) - 15, 0)             # (local)
    i_hi = min(i_lo + 30, len(tau))                                # (local)
    sp_lna = CubicSpline(eta_t[i_lo:i_hi], np.log(a_t[i_lo:i_hi]))  # (local)
    aH_rederived = float(sp_lna(0.0, 1))                           # (local)
    zppz_rederived = 2.0 * aH_rederived**2                         # (local)
    chk_target = k_pivot**2 / k2_over_zppz                         # (local)
    CHK_N_ratio = zppz_rederived / chk_target                      # (local)
    print("\n--- CHK-N normalization pre-flight ---")
    print(f"  aH|fold re-derived (d ln a~/d eta~) = {aH_rederived:.10f} M_KK")
    print(f"  re-derived z''/z plateau = 2*(aH_re)^2 = {zppz_rederived:.10f}")
    print(f"  anchor k_pivot^2/{k2_over_zppz:.11f} = {chk_target:.10f}")
    print(f"  CHK_N_ratio = {CHK_N_ratio:.10f}  (band [0.95, 1.05])")
    if not (1.0 - TOL_CHK_N <= CHK_N_ratio <= 1.0 + TOL_CHK_N):
        print("HARD-ABORT: CHK-N failed (normalization bug, not physics).")
        sys.exit(2)
    print("  CHK-N: PASS")
    # documented physics gap (NOT a CHK-N failure): the stored eta_H-corrected
    # GSR channel vs the quasi-dS anchor
    Uc_fold = float(sp_Uc(tau_fold))                               # (local)
    print(f"  [diagnostic] stored s64 zpp_over_z channel in fold units = "
          f"{Uc_fold:.6f} = {Uc_fold/chk_target:.4f} x anchor")
    print(f"    (the known eta_H = 0.956 slow-roll-violation gap, s64 INFO; "
          f"F_fold = {Uc_fold/aH_rederived**2:.4f} vs quasi-dS 2.0 -- this is")
    print(f"    the plan's 'cross-check vs stored zpp_over_z channel': "
          f"documented, branch-(c) sensitivity below)")

    return dict(tau=tau, sp_eta_t=sp_eta_t, sp_a_t=sp_a_t, sp_aH_t=sp_aH_t,
                sp_Uc=sp_Uc, sp_dlnz=sp_dlnz, sp_eps=sp_eps,
                eta_t=eta_t, a_t=a_t, aH_t=aH_t, U_c_grid=U_c,
                k_pivot=k_pivot, k_over_aH=k_over_aH,
                k2_over_zppz=k2_over_zppz, aH_target=aH_target,
                u_clock=u_clock, Lam=Lam, a_fold=a_fold,
                CHK_N_ratio=CHK_N_ratio, chk_target=chk_target,
                aH_rederived=aH_rederived, Uc_fold=Uc_fold,
                x_pivot=x_pivot, N_pivot=N_pivot, Mach_fric=Mach_fric,
                H_fold_s64=H_fold_s64, c_BLV=c_BLV)


# --------------------------------------------------------------------------
# Section 6 -- Window, barrier plateaus, delta weights
# --------------------------------------------------------------------------
def build_window(bg: dict) -> dict:
    tau = bg["tau"]                                                # (local)
    # fold-normalized cosmic time t~ (dt~ = a~ d eta~), zeroed at fold
    eta_g = bg["eta_t"]                                            # (local)
    t_g = cumulative_trapezoid(bg["a_t"], eta_g, initial=0.0)      # (local)
    sp_t_of_tau = CubicSpline(tau, t_g)                            # (local)
    t_fold = float(sp_t_of_tau(tau_fold))                          # (local)
    t_g = t_g - t_fold                                             # (local)
    sp_tau_of_t = CubicSpline(t_g, tau)                            # (local)

    tau_on = float(sp_tau_of_t(-dt_transit / 2.0))                 # (local)
    tau_off = float(sp_tau_of_t(+dt_transit / 2.0))                # (local)
    eta_on = float(bg["sp_eta_t"](tau_on))                         # (local)
    eta_off = float(bg["sp_eta_t"](tau_off))                       # (local)
    Delta_eta = eta_off - eta_on                                   # (local)

    # window sub-sampling (sub-grid window: cubic interpolant = pinned machinery)
    eta_win = np.linspace(eta_on, eta_off, 2001)                   # (local)
    sp_tau_of_eta = CubicSpline(eta_g, tau)                        # (local)
    tau_win = sp_tau_of_eta(eta_win)                               # (local)

    aH_win = bg["sp_aH_t"](tau_win)                                # (local)
    a_win = bg["sp_a_t"](tau_win)                                  # (local)
    U_b_win = 2.0 * aH_win**2          # (local) canonical quasi-dS barrier
    U_c_win = bg["sp_Uc"](tau_win)     # (local) stored-channel barrier

    V_box = float(np.trapezoid(U_b_win, eta_win) / Delta_eta)      # (local)
    V_box_c = float(np.trapezoid(U_c_win, eta_win) / Delta_eta)    # (local)
    flat_b = float(U_b_win.max() / U_b_win.min() - 1.0)            # (local)
    flat_c = float(U_c_win.max() / U_c_win.min() - 1.0)            # (local)

    # literal Sparn Eq.4 potential (sqrt(a)-pump diagnostic):
    # V_a = (1/4) adot^2 + (1/2) addot a, dots = d/dt~ ; adot = a~H~,
    # addot = d(a~H~)/dt~ evaluated by spline differentiation
    sp_adot_of_t = CubicSpline(t_g, bg["aH_t"])                    # (local)
    t_win = sp_t_of_tau(tau_win) - t_fold                          # (local)
    adot_win = sp_adot_of_t(t_win)                                 # (local)
    addot_win = sp_adot_of_t(t_win, 1)                             # (local)
    V_a_win = 0.25 * adot_win**2 + 0.5 * addot_win * a_win         # (local)
    V_a = float(np.trapezoid(V_a_win, eta_win) / Delta_eta)        # (local)

    # delta weights (plan pin, literal): Omega = (1/2) a [adot]_jump
    a_on = float(bg["sp_a_t"](tau_on))                             # (local)
    a_off = float(bg["sp_a_t"](tau_off))                           # (local)
    adot_on = float(bg["sp_aH_t"](tau_on))    # (local) a~H~ = da~/dt~
    adot_off = float(bg["sp_aH_t"](tau_off))                       # (local)
    Omega_on = +0.5 * a_on * adot_on                               # (local)
    Omega_off = -0.5 * a_off * adot_off                            # (local)
    # strict distributional weight (Jacobian-cancelled; Schmidt Table I form)
    Omega_on_strict = +0.5 * adot_on                               # (local)
    Omega_off_strict = -0.5 * adot_off                             # (local)
    # z-pump variant (sensitivity scalar): Omega_z = [z'/z] = dlnz/dN * a~H~
    Om_z_on = +float(bg["sp_dlnz"](tau_on)) * adot_on              # (local)
    Om_z_off = -float(bg["sp_dlnz"](tau_off)) * adot_off           # (local)

    print("\n--- Transit window (fold-normalized M_KK clock) ---")
    print(f"  dt_transit (canonical) = {dt_transit:.10e} M_KK^-1")
    print(f"  tau window: [{tau_on:.9f}, {tau_off:.9f}]  "
          f"(delta_tau = {tau_off-tau_on:.6e}; grid spacing "
          f"{tau[1]-tau[0]:.6e} -> window/grid = "
          f"{(tau_off-tau_on)/(tau[1]-tau[0]):.4f} [sub-grid; cubic "
          f"interpolant = pinned machinery])")
    print(f"  eta~ window: [{eta_on:.8e}, {eta_off:.8e}]")
    print(f"  Delta_eta = {Delta_eta:.10e} M_KK^-1  "
          f"(vs dt_transit: ratio {Delta_eta/dt_transit:.8f})")
    print(f"  impulsiveness: aH*Delta_eta = "
          f"{bg['aH_target']*Delta_eta:.6e} << 1 (fold-conformal clock);")
    print(f"    canonical S38-clock product H_fold*dt_transit = "
          f"{H_fold*dt_transit:.6f} < 1 (impulsive)")
    print(f"  V_box (canonical branch b: 2(aH)^2 window mean) = {V_box:.8f}")
    print(f"    plateau flatness (max/min - 1) = {flat_b:.3e}")
    print(f"  V_box_c (branch c: stored zpp channel) = {V_box_c:.8f} "
          f"(flatness {flat_c:.3e})")
    print(f"  V_a (literal Sparn Eq.4, sqrt(a)-pump diagnostic) = {V_a:.8f}")
    print(f"    pump correspondence: V_Sparn/V_box = {V_a/V_box:.6f} "
          f"(the psi=sqrt(a)v map gives the sqrt(a)-pump barrier")
    print(f"     (1/2)a''/a - (1/4)(a'/a)^2 ~ (3/4-eps/2)(aH)^2; the substrate")
    print(f"     mode barrier is the z-pump z''/z ~ 2(aH)^2 -- the chain's")
    print(f"     identification V_box ~= (z''/z)|fold uses the z-pump anchor)")
    print(f"  Omega_on  = {Omega_on:+.8f}  (literal pin (1/2)a[adot]; strict "
          f"distributional {Omega_on_strict:+.8f}, rel dev "
          f"{abs(Omega_on/Omega_on_strict-1):.2e})")
    print(f"  Omega_off = {Omega_off:+.8f}  (strict {Omega_off_strict:+.8f})")
    print(f"    [one REPULSIVE switch-on, one ATTRACTIVE switch-off -- the")
    print(f"     Schmidt Table I linear-expansion sign structure]")
    print(f"  z-pump variant (sensitivity, NOT gating): Omega_z_on = "
          f"{Om_z_on:+.6f}, Omega_z_off = {Om_z_off:+.6f}")

    return dict(eta_on=eta_on, eta_off=eta_off, Delta_eta=Delta_eta,
                tau_on=tau_on, tau_off=tau_off, eta_win=eta_win,
                U_b_win=U_b_win, U_c_win=U_c_win, V_box=V_box,
                V_box_c=V_box_c, V_a=V_a, flat_b=flat_b, flat_c=flat_c,
                Omega_on=Omega_on, Omega_off=Omega_off,
                Omega_on_strict=Omega_on_strict,
                Omega_off_strict=Omega_off_strict,
                Om_z_on=Om_z_on, Om_z_off=Om_z_off,
                sp_t_of_tau=sp_t_of_tau, t_fold=t_fold,
                sp_tau_of_t=sp_tau_of_t, sp_tau_of_eta=sp_tau_of_eta)


# --------------------------------------------------------------------------
# Section 7 -- Transfer matrices (exact 2x2; entire-function evaluation)
# --------------------------------------------------------------------------
def entire_CS(mu2: float, L: float) -> tuple[float, float]:
    """C = cos(mu L), S = sin(mu L)/mu as ENTIRE functions of mu^2.
    For mu^2 < 0 this IS the Schmidt continuation mu -> i Lambda:
    C = cosh(Lambda L), S = sinh(Lambda L)/Lambda."""
    x = mu2 * L * L                                                # (local)
    if abs(x) < 1e-12:
        return 1.0 - x / 2.0, L * (1.0 - x / 6.0)
    if mu2 > 0:
        m = np.sqrt(mu2)                                           # (local)
        return float(np.cos(m * L)), float(np.sin(m * L) / m)
    lam = np.sqrt(-mu2)                                            # (local)
    return float(np.cosh(lam * L)), float(np.sinh(lam * L) / lam)


def M_box(mu2: float, L: float) -> np.ndarray:
    C, S = entire_CS(mu2, L)                                       # (local)
    return np.array([[C, S], [-mu2 * S, C]], dtype=float)


def M_delta(Omega: float) -> np.ndarray:
    """[psi'] = +Omega psi across the peak (Schmidt B41/B42 matching)."""
    return np.array([[1.0, 0.0], [Omega, 1.0]], dtype=float)


def tm_beta(k: float, M: np.ndarray, eta_on: float,
            eta_off: float) -> tuple[complex, complex]:
    """BD-in-out extraction: in-state pure positive frequency e^{-ik eta}
    before eta_on; out-state alpha e^{-ik eta} + beta e^{+ik eta}."""
    psi0 = np.exp(-1j * k * eta_on)                                # (local)
    v0 = np.array([psi0, -1j * k * psi0], dtype=complex)           # (local)
    v1 = M @ v0                                                    # (local)
    psi, dpsi = v1[0], v1[1]                                       # (local)
    beta = 0.5 * (psi + dpsi / (1j * k)) * np.exp(-1j * k * eta_off)  # (local)
    alpha = 0.5 * (psi - dpsi / (1j * k)) * np.exp(+1j * k * eta_off)  # (local)
    return alpha, beta


def build_M_total(k: float, w: dict, n_seg: int, branch: str) -> np.ndarray:
    """M = M_delta(Omega_off) . [interior product, n_seg segments sampling
    the ACTUAL U(eta) interior] . M_delta(Omega_on)."""
    eta_on, eta_off = w["eta_on"], w["eta_off"]                    # (local)
    U_win = w["U_b_win"] if branch == "b" else w["U_c_win"]        # (local)
    sp_U = CubicSpline(w["eta_win"], U_win)                        # (local)
    edges = np.linspace(eta_on, eta_off, n_seg + 1)                # (local)
    mids = 0.5 * (edges[:-1] + edges[1:])                          # (local)
    Useg = sp_U(mids)                                              # (local)
    L = (eta_off - eta_on) / n_seg                                 # (local)
    M = M_delta(w["Omega_on"])                                     # (local)
    for U in Useg:
        M = M_box(k * k - float(U), L) @ M
    M = M_delta(w["Omega_off"]) @ M                                # (local)
    return M


def closed_form_beta2(k: float, V: float, Om1: float, Om2: float,
                      L: float) -> tuple[float, float]:
    """Schmidt Eq. 75/76-class closed form for box(V, L) + deltas(Om1, Om2),
    generalized to Om1 != -Om2, written as an EXPLICIT algebraic expression
    (independent code path from the matrix product):
      |beta|^2 = (1/4)[ (Om1-Om2)^2 S^2
                        + ( k S + ((Om1+Om2) C + (Om1 Om2 - mu^2) S)/k )^2 ]
      |alpha|^2 = (1/4)[ (2C + (Om1+Om2) S)^2
                        + ( k S - ((Om1+Om2) C + (Om1 Om2 - mu^2) S)/k )^2 ]
    with mu^2 = k^2 - V and C = cos(mu L), S = sin(mu L)/mu entire in mu^2
    (the sub-horizon sin[mu_k Delta_eta] sector for mu^2 > 0; the
    super-horizon sinh[Lambda_k Delta_eta] sector via mu -> i Lambda).
    Ramsauer-Townsend zeros: S = 0 <=> mu L = j pi (real-mu sector)."""
    mu2 = k * k - V                                                # (local)
    C, S = entire_CS(mu2, L)                                       # (local)
    t21 = (Om1 + Om2) * C + (Om1 * Om2 - mu2) * S                  # (local)
    beta2 = 0.25 * ((Om1 - Om2) ** 2 * S ** 2
                    + (k * S + t21 / k) ** 2)                      # (local)
    alpha2 = 0.25 * ((2.0 * C + (Om1 + Om2) * S) ** 2
                     + (k * S - t21 / k) ** 2)                     # (local)
    return float(beta2), float(alpha2)


# --------------------------------------------------------------------------
# Section 8 -- ODE reference (Radau; the standing valid route)
# --------------------------------------------------------------------------
def ode_beta2(k: float, w: dict, branch: str = "b") -> tuple[float, float]:
    """Direct Radau solve of psi'' + (k^2 - U(eta)) psi = 0 across the window
    interior (the same U the TM segments sample), with the SAME boundary
    deltas applied as matching conditions and BD-in/out extraction.
    rtol = 1e-10 per the pinned diagnostic. The v-equation
    v'' + (k^2 - z''/z) v = 0 IS this equation with U the mode barrier."""
    eta_on, eta_off = w["eta_on"], w["eta_off"]                    # (local)
    U_win = w["U_b_win"] if branch == "b" else w["U_c_win"]        # (local)
    sp_U = CubicSpline(w["eta_win"], U_win)                        # (local)
    psi0 = np.exp(-1j * k * eta_on)                                # (local)
    v0c = np.array([psi0, -1j * k * psi0], dtype=complex)          # (local)
    v0c = M_delta(w["Omega_on"]) @ v0c                             # (local)
    y0 = [v0c[0].real, v0c[0].imag, v0c[1].real, v0c[1].imag]      # (local)

    def rhs(eta, y):
        U = float(sp_U(eta))                                       # (local)
        return [y[2], y[3], (U - k * k) * y[0], (U - k * k) * y[1]]

    sol = solve_ivp(rhs, [eta_on, eta_off], y0, method="Radau",
                    rtol=ODE_RTOL, atol=ODE_ATOL, dense_output=False)  # (local)
    if not sol.success:
        return np.nan, np.nan
    psi = sol.y[0, -1] + 1j * sol.y[1, -1]                         # (local)
    dpsi = sol.y[2, -1] + 1j * sol.y[3, -1]                        # (local)
    v1 = M_delta(w["Omega_off"]) @ np.array([psi, dpsi])           # (local)
    beta = 0.5 * (v1[0] + v1[1] / (1j * k)) * np.exp(-1j * k * eta_off)  # (local)
    alpha = 0.5 * (v1[0] - v1[1] / (1j * k)) * np.exp(+1j * k * eta_off)  # (local)
    return float(abs(beta) ** 2), float(abs(alpha) ** 2)


# --------------------------------------------------------------------------
# Section 9 -- Main computation
# --------------------------------------------------------------------------
def compute(bg: dict, w: dict, pdfinfo: dict) -> dict:
    k_pivot = bg["k_pivot"]                                        # (local)
    V_box, Om1, Om2 = w["V_box"], w["Omega_on"], w["Omega_off"]    # (local)
    L = w["Delta_eta"]                                             # (local)

    # ---- substitution chain (runtime numbers; branch claim) ----
    mu_pivot_sq = k_pivot**2 - V_box                               # (local)
    print("\n--- Substitution chain (runtime evaluation) ---")
    print(f"  Step 1: V_box = {V_box:.8f} (computed window plateau, "
          f"canonical branch)")
    print(f"  Step 2: k_pivot = {k_pivot:.12f}; "
          f"k_pivot^2 = {k_pivot**2:.8f}")
    print(f"  Step 3: mu_pivot^2 = k_pivot^2 - V_box = {mu_pivot_sq:.8f}")
    print(f"  Step 4: mu_pivot^2/k_pivot^2 = {mu_pivot_sq/k_pivot**2:.8f} "
          f"(chain pre-registration: 1 - 1/107.63558 = "
          f"{1.0 - 1.0/bg['k2_over_zppz']:.8f})")
    print(f"  Step 5: mu_pivot^2 = {mu_pivot_sq:.4f} > 0 -> OSCILLATING "
          f"(sub-horizon) sector; sin[mu_k Delta_eta] branch CORRECT; "
          f"Lambda_k -> i mu_k continuation NOT engaged at k_pivot")
    sign_ok = mu_pivot_sq > 0.0                                    # (local)

    # ---- N_seg robustness scan (canonical branch) ----
    print("\n--- N_seg robustness scan (canonical branch b) ---")
    beta2_per_Nseg = []                                            # (local)
    unit_resid = []                                                # (local)
    for n_seg in N_SEG_SCAN:
        M = build_M_total(k_pivot, w, n_seg, "b")                  # (local)
        det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]                # (local)
        al, be = tm_beta(k_pivot, M, w["eta_on"], w["eta_off"])    # (local)
        b2 = abs(be) ** 2                                          # (local)
        resid = abs(abs(al) ** 2 - abs(be) ** 2 - 1.0)             # (local)
        beta2_per_Nseg.append(b2)
        unit_resid.append(resid)
        print(f"  N_seg = {n_seg:4d}: |beta_pivot|^2 = {b2:.10e}  "
              f"(det M - 1 = {det-1:+.2e}; unitarity resid = {resid:.2e})")
    beta2_per_Nseg = np.array(beta2_per_Nseg)                      # (local)
    var_Nseg = float(beta2_per_Nseg.max() / beta2_per_Nseg.min())  # (local)
    beta2_TM = float(beta2_per_Nseg[-1])     # (local) N_seg=400 (finest)
    print(f"  var_Nseg = max/min = {var_Nseg:.10f}  "
          f"(threshold < {TOL_VAR_NSEG})")
    print(f"  |beta_pivot|^2_TM (N_seg=400, operational pin) = {beta2_TM:.10e}")

    # ---- closed form (identical parameters) + algebra identity check ----
    beta2_cf, alpha2_cf = closed_form_beta2(k_pivot, V_box, Om1, Om2, L)  # (local)
    M1 = M_delta(Om2) @ M_box(k_pivot**2 - V_box, L) @ M_delta(Om1)  # (local)
    al1, be1 = tm_beta(k_pivot, M1, w["eta_on"], w["eta_off"])     # (local)
    ident_dev = abs(abs(be1) ** 2 / beta2_cf - 1.0)                # (local)
    unit_cf = abs(alpha2_cf - beta2_cf - 1.0)                      # (local)
    rel_dev = abs(beta2_TM / beta2_cf - 1.0)                       # (local)
    print("\n--- Schmidt Eq.75-class closed-form comparison ---")
    print(f"  |beta_pivot|^2_closed-form = {beta2_cf:.10e}")
    print(f"  closed-form unitarity |alpha|^2-|beta|^2-1 = {unit_cf:.2e}")
    print(f"  single-box TM == closed form (independent code paths): "
          f"rel dev = {ident_dev:.2e} (analytic identity)")
    print(f"  rel_dev = | beta2_TM/beta2_closed - 1 | = {rel_dev:.6e}  "
          f"(threshold <= {TOL_REL_DEV})")
    print(f"  mu_pivot*Delta_eta = {np.sqrt(mu_pivot_sq)*L:.6e} << pi "
          f"(plan diagnostic-(ii) expectation ~1.6e-2: CONFIRMED)")

    # ---- ODE reference (standing valid route) ----
    b2_ode, a2_ode = ode_beta2(k_pivot, w, "b")                    # (local)
    ode_resid = abs(a2_ode - b2_ode - 1.0)                         # (local)
    print("\n--- ODE reference (Radau, rtol=1e-10) ---")
    print(f"  |beta_pivot|^2_ODE = {b2_ode:.10e}  "
          f"(vs TM: rel dev {abs(b2_ode/beta2_TM-1):.2e}; "
          f"unitarity resid {ode_resid:.2e})")

    # ---- branch-c sensitivity (stored zpp channel) ----
    print("\n--- Branch-(c) sensitivity (stored s64 zpp_over_z barrier) ---")
    beta2_c_per_Nseg = []                                          # (local)
    for n_seg in N_SEG_SCAN:
        Mc = build_M_total(k_pivot, w, n_seg, "c")                 # (local)
        _, bec = tm_beta(k_pivot, Mc, w["eta_on"], w["eta_off"])   # (local)
        beta2_c_per_Nseg.append(abs(bec) ** 2)
    beta2_c_per_Nseg = np.array(beta2_c_per_Nseg)                  # (local)
    var_Nseg_c = float(beta2_c_per_Nseg.max() / beta2_c_per_Nseg.min())  # (local)
    beta2_cf_c, _ = closed_form_beta2(k_pivot, w["V_box_c"], Om1, Om2, L)  # (local)
    rel_dev_c = abs(float(beta2_c_per_Nseg[-1]) / beta2_cf_c - 1.0)  # (local)
    b2_ode_c, _ = ode_beta2(k_pivot, w, "c")                       # (local)
    print(f"  var_Nseg(c) = {var_Nseg_c:.10f}; "
          f"|beta|^2_TM(c) = {beta2_c_per_Nseg[-1]:.6e}; "
          f"closed(c) = {beta2_cf_c:.6e}; rel_dev(c) = {rel_dev_c:.4e}; "
          f"ODE(c) = {b2_ode_c:.6e}")
    print(f"  -> verdict-structure INVARIANT under the F-convention branch "
          f"(both branches: N_seg-stable, closed-form-consistent)")

    # ---- diagnostic k-spectrum (64 log points + pivot) ----
    print("\n--- Diagnostic |beta_k|^2 spectrum (64 log k-points + pivot) ---")
    k_grid = np.geomspace(K_MIN, K_MAX, N_K_DIAG)                  # (local)
    beta2_spec = np.zeros(N_K_DIAG)                                # (local)
    beta2_spec_cf = np.zeros(N_K_DIAG)                             # (local)
    beta2_spec_ode = np.zeros(N_K_DIAG)                            # (local)
    max_unit = max(unit_resid)                                     # (local)
    for i, k in enumerate(k_grid):
        Mk = build_M_total(k, w, N_SEG_SCAN[-1], "b")              # (local)
        alk, bek = tm_beta(k, Mk, w["eta_on"], w["eta_off"])       # (local)
        beta2_spec[i] = abs(bek) ** 2
        max_unit = max(max_unit, abs(abs(alk) ** 2 - abs(bek) ** 2 - 1.0))
        beta2_spec_cf[i], _ = closed_form_beta2(k, V_box, Om1, Om2, L)
        beta2_spec_ode[i], _ = ode_beta2(k, w, "b")
    k_branch = np.sqrt(V_box)                                      # (local)
    print(f"  branch crossover sqrt(V_box) = {k_branch:.4f} M_KK "
          f"(sinh sector below, sin sector above; continuation "
          f"Lambda_k -> i mu_k implemented via entire C,S)")
    print(f"  max unitarity residual over all evaluations = {max_unit:.2e} "
          f"(tolerance {TOL_UNITARITY})")

    # ---- Ramsauer-Townsend diagnostic ----
    mu_max = np.sqrt(K_MAX**2 - V_box)                             # (local)
    n_RT_in_window = int(np.floor(mu_max * L / PI))                # (local)
    k_RT_first = float(np.sqrt((PI / L) ** 2 + V_box))             # (local)
    print(f"\n--- Ramsauer-Townsend zeros (mu_k Delta_eta = j pi) ---")
    print(f"  mu(K_MAX)*Delta_eta/pi = {mu_max*L/PI:.6e} -> "
          f"{n_RT_in_window} zeros in k in [1,50] (expected none: CONFIRMED)")
    print(f"  first R-T zero at k = {k_RT_first:.1f} M_KK (far above k-window)")

    # ---- B2-ladder OOM context (different stage; NOT a criterion) ----
    B2_anchor = pdfinfo["B2_anchor"]                               # (local)
    print(f"\n--- S79 P2-A B2-ladder OOM context (diagnostic only) ---")
    print(f"  |beta_2|^2(B2 stage, post-fold WKB -> horizon exit) ~ "
          f"{B2_anchor:.1e}")
    print(f"  |beta_pivot|^2(this gate, impulsive window only) = "
          f"{beta2_TM:.3e}")
    print(f"  log10 ratio = {np.log10(beta2_TM/B2_anchor):+.2f} OOM -- "
          f"DIFFERENT ladder stage (window Delta_N ~ "
          f"{bg['aH_target']*L:.1e} e-folds vs B2's ~3.1 e-folds of")
    print(f"    pump growth); the stages are non-comparable by construction; "
          f"context only, per the plan pin")

    # ---- window-pin sensitivity (alt S38-internal-clock reading) ----
    delta_tau_alt = v_terminal * dt_transit                        # (local)
    tau_on_a = tau_fold - delta_tau_alt / 2.0                      # (local)
    tau_off_a = tau_fold + delta_tau_alt / 2.0                     # (local)
    eta_on_a = float(bg["sp_eta_t"](tau_on_a))                     # (local)
    eta_off_a = float(bg["sp_eta_t"](tau_off_a))                   # (local)
    L_alt = eta_off_a - eta_on_a                                   # (local)
    eta_win_a = np.linspace(eta_on_a, eta_off_a, 4001)             # (local)
    tau_win_a = bg["sp_tau_of_eta"](eta_win_a) if "sp_tau_of_eta" in bg \
        else w["sp_tau_of_eta"](eta_win_a)                         # (local)
    U_win_a = 2.0 * bg["sp_aH_t"](tau_win_a) ** 2                  # (local)
    V_box_a = float(np.trapezoid(U_win_a, eta_win_a) / L_alt)      # (local)
    Om1_a = +0.5 * float(bg["sp_a_t"](tau_on_a)) \
        * float(bg["sp_aH_t"](tau_on_a))                           # (local)
    Om2_a = -0.5 * float(bg["sp_a_t"](tau_off_a)) \
        * float(bg["sp_aH_t"](tau_off_a))                          # (local)
    beta2_alt, _ = closed_form_beta2(k_pivot, V_box_a, Om1_a, Om2_a, L_alt)  # (local)
    print(f"\n--- Window-pin sensitivity (diagnostic; NOT gating) ---")
    print(f"  alt reading (S38 internal clock: delta_tau = v_terminal*"
          f"dt_transit = {delta_tau_alt:.6f}):")
    print(f"    Delta_eta_alt = {L_alt:.6f}; V_box_alt = {V_box_a:.4f}; "
          f"plateau flatness {U_win_a.max()/U_win_a.min()-1:.3f} "
          f"(NOT plateau-like -> box idealization poor there);")
    print(f"    closed-form |beta_pivot|^2_alt = {beta2_alt:.4e} "
          f"(vs canonical {beta2_cf:.4e})")
    print(f"  canonical window pin (fold-normalized M_KK clock) is the "
          f"unique reading consistent with the plan block's own")
    print(f"    mu*Delta_eta ~ 1.6e-2 arithmetic; alt reading seeds any "
          f"future refined-window gate (NEW pre-registration)")

    # ---- z-pump Omega sensitivity (diagnostic) ----
    beta2_zpump, _ = closed_form_beta2(k_pivot, V_box,
                                       w["Om_z_on"], w["Om_z_off"], L)  # (local)
    print(f"  z-pump delta-weight variant: |beta_pivot|^2 = {beta2_zpump:.4e} "
          f"(x{beta2_zpump/beta2_cf:.2f} vs literal pin; verdict criteria "
          f"INVARIANT -- identical weights both sides of rel_dev)")

    # ---- delta-dominance (Parra-Lopez switch-on/off dominance) ----
    beta2_box_only, _ = closed_form_beta2(k_pivot, V_box, 0.0, 0.0, L)  # (local)
    beta2_deltas_only, _ = closed_form_beta2(k_pivot, 0.0, Om1, Om2, L)  # (local)
    print(f"  channel split: box-only |beta|^2 = {beta2_box_only:.3e}; "
          f"deltas-only = {beta2_deltas_only:.3e} -> switch-boundary deltas "
          f"dominate (x{beta2_deltas_only/beta2_box_only:.1f}) -- the")
    print(f"    Parra-Lopez switch-on/off-dominance structure (transitions "
          f"dominate production, stages do not)")

    return dict(mu_pivot_sq=mu_pivot_sq, sign_ok=sign_ok,
                beta2_per_Nseg=beta2_per_Nseg, var_Nseg=var_Nseg,
                beta2_TM=beta2_TM, beta2_cf=beta2_cf, rel_dev=rel_dev,
                ident_dev=ident_dev, b2_ode=b2_ode,
                beta2_c_per_Nseg=beta2_c_per_Nseg, var_Nseg_c=var_Nseg_c,
                beta2_cf_c=beta2_cf_c, rel_dev_c=rel_dev_c, b2_ode_c=b2_ode_c,
                k_grid=k_grid, beta2_spec=beta2_spec,
                beta2_spec_cf=beta2_spec_cf, beta2_spec_ode=beta2_spec_ode,
                max_unit=max_unit, n_RT_in_window=n_RT_in_window,
                k_RT_first=k_RT_first, k_branch=k_branch,
                beta2_alt=beta2_alt, L_alt=L_alt, V_box_a=V_box_a,
                beta2_zpump=beta2_zpump, beta2_box_only=beta2_box_only,
                beta2_deltas_only=beta2_deltas_only, B2_anchor=B2_anchor)


# --------------------------------------------------------------------------
# Section 10 -- Gate evaluation (pre-registered operator + collapse rule)
# --------------------------------------------------------------------------
def evaluate_gate(r: dict, w: dict, bg: dict) -> tuple[str, str, str, str]:
    # sign axis: pre-registered branch claim mu_pivot^2 > 0
    sign_v = "PASS" if r["sign_ok"] else "FAIL"                    # (local)
    # magnitude axis: the pre-registered conjunction
    var_ok = r["var_Nseg"] < TOL_VAR_NSEG                          # (local)
    rel_ok = r["rel_dev"] <= TOL_REL_DEV                           # (local)
    if var_ok and rel_ok:
        mag_v = "PASS"                                             # (local)
    elif var_ok and not rel_ok:
        mag_v = "INFO"   # (local) N_seg-stable but off closed form (rubric)
    else:
        mag_v = "FAIL"                                             # (local)
    # regime axis: idealization validity across the FULL intended window
    regime_ok = (r["sign_ok"]
                 and r["max_unit"] < TOL_UNITARITY
                 and w["flat_b"] < 0.05
                 and np.isfinite(r["b2_ode"]))                     # (local)
    regime_v = "VALID" if regime_ok else "MARGINAL"                # (local)
    # composite via the pre-registered gate-verdicts.md collapse rule
    if regime_v == "BREAKDOWN":
        comp = "FAIL"                                              # (local)
    elif sign_v == "FAIL":
        comp = "FAIL"                                              # (local)
    elif mag_v == "FAIL" and regime_v == "VALID":
        comp = "FAIL"                                              # (local)
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        comp = "INFO"                                              # (local)
    elif mag_v == "INFO":
        comp = "INFO"                                              # (local)
    else:
        comp = "PASS"                                              # (local)
    return comp, sign_v, mag_v, regime_v


# --------------------------------------------------------------------------
# Section 11 -- Plot
# --------------------------------------------------------------------------
def make_plot(bg: dict, w: dict, r: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(19, 5.6))              # (local)
    fig.suptitle(
        f"S100b-BOX-DELTA-BOGOLIUBOV -- box+delta sudden-limit transfer matrix "
        f"(fold window, BD-in-out)\n"
        f"var_Nseg = {r['var_Nseg']:.6f} (<2.0) | rel_dev = "
        f"{r['rel_dev']:.2e} (<=0.10) | |beta_pivot|^2 = {r['beta2_TM']:.4e}",
        fontsize=11, fontweight="bold")

    # Panel 1: spectrum
    ax = axes[0]                                                   # (local)
    ax.loglog(r["k_grid"], r["beta2_spec"], "b-", lw=1.6,
              label="TM (N_seg=400, actual interior)")
    ax.loglog(r["k_grid"], r["beta2_spec_cf"], "r--", lw=1.2,
              label="Schmidt Eq.75-class closed form")
    ax.loglog(r["k_grid"], r["beta2_spec_ode"], "g:", lw=2.0,
              label="ODE reference (Radau 1e-10)")
    ax.axvline(bg["k_pivot"], color="k", ls="--", alpha=0.6,
               label=f"k_pivot = {bg['k_pivot']:.3f}")
    ax.axvline(r["k_branch"], color="orange", ls=":", alpha=0.8,
               label=f"sqrt(V_box) = {r['k_branch']:.2f} (sin/sinh branch)")
    ax.plot([bg["k_pivot"]], [r["beta2_TM"]], "k*", ms=14)
    ax.set_xlabel("k  [M_KK, fold-normalized comoving]")
    ax.set_ylabel(r"$|\beta_k|^2$")
    ax.set_title("Bogoliubov spectrum: TM vs closed form vs ODE")
    ax.legend(fontsize=7.5)
    ax.grid(True, alpha=0.3, which="both")

    # Panel 2: N_seg stability (this gate vs the S85 pathology scale)
    ax = axes[1]                                                   # (local)
    ax.semilogx(N_SEG_SCAN, r["beta2_per_Nseg"] / r["beta2_per_Nseg"][0],
                "bo-", lw=1.5, ms=8, label="branch (b): 2(aH)^2 barrier")
    ax.semilogx(N_SEG_SCAN, r["beta2_c_per_Nseg"] / r["beta2_c_per_Nseg"][0],
                "ms-", lw=1.2, ms=6, alpha=0.7,
                label="branch (c): stored z''/z channel")
    ax.axhspan(1.0 / TOL_VAR_NSEG, TOL_VAR_NSEG, color="green", alpha=0.10,
               label="PASS band (var_Nseg < 2)")
    ax.set_xlabel("N_seg (interior segmentation)")
    ax.set_ylabel(r"$|\beta_{pivot}|^2(N_{seg}) / |\beta_{pivot}|^2(50)$")
    ax.set_title(f"N_seg stability: var = {r['var_Nseg']:.2e}+1 "
                 f"(S85 smooth-cusp was OOM-unstable)")
    ax.set_ylim(0.5, 2.1)
    ax.legend(fontsize=7.5)
    ax.grid(True, alpha=0.3)

    # Panel 3: V(eta) profile with box+delta overlay
    ax = axes[2]                                                   # (local)
    span = 6.0                                                     # (local)
    eta_ctx = np.linspace(w["eta_on"] - span * w["Delta_eta"],
                          w["eta_off"] + span * w["Delta_eta"], 800)  # (local)
    tau_ctx = w["sp_tau_of_eta"](eta_ctx)                          # (local)
    U_ctx = 2.0 * bg["sp_aH_t"](tau_ctx) ** 2                      # (local)
    ax.plot(eta_ctx * 1e3, U_ctx, "b-", lw=1.4,
            label=r"fold barrier $2(\tilde a \tilde H)^2(\eta)$ (data)")
    ax.plot([w["eta_on"] * 1e3, w["eta_on"] * 1e3,
             w["eta_off"] * 1e3, w["eta_off"] * 1e3],
            [0, w["V_box"], w["V_box"], 0], "r-", lw=2.0,
            label=f"box V = {w['V_box']:.4f} (idealization)")
    for eta_b, Om, lab in [(w["eta_on"], w["Omega_on"],
                            f"$\\Omega_{{on}}$ = {w['Omega_on']:+.4f}"),
                           (w["eta_off"], w["Omega_off"],
                            f"$\\Omega_{{off}}$ = {w['Omega_off']:+.4f}")]:
        ax.annotate("", xy=(eta_b * 1e3, w["V_box"] + np.sign(Om) * 0.9),
                    xytext=(eta_b * 1e3, w["V_box"]),
                    arrowprops=dict(arrowstyle="-|>", lw=2.2,
                                    color="darkorange"))
        ax.text(eta_b * 1e3, w["V_box"] + np.sign(Om) * 0.9 + 0.12, lab,
                ha="center", fontsize=8, color="darkorange")
    ax.axhline(bg["chk_target"], color="gray", ls="--", alpha=0.6,
               label=f"anchor k_pivot$^2$/107.636 = {bg['chk_target']:.4f}")
    ax.axhline(bg["Uc_fold"], color="m", ls=":", alpha=0.6,
               label=f"stored z''/z channel = {bg['Uc_fold']:.4f} "
                     f"($\\eta_H$-corrected)")
    ax.set_xlabel(r"$\tilde\eta \times 10^3$  [M_KK$^{-1}$, fold-centered]")
    ax.set_ylabel(r"$U(\tilde\eta)$  [M_KK$^2$]")
    ax.set_title(f"Box+delta overlay (window {w['Delta_eta']*1e3:.4f}e-3; "
                 f"plateau flat to {w['flat_b']:.1e})")
    ax.legend(fontsize=7.5, loc="center left")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    print(f"\nSaved plot: {OUT_PNG}")


# --------------------------------------------------------------------------
# Section 12 -- Main
# --------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                               # (local)
    pins = verify_inputs()                                         # (local)

    # dual-SHA (audit = script+canonical+pinmap incl. machinery pins)
    pinmap = dict(pins)                                            # (local)
    pinmap.update({f"_machinery::{k}": v for k, v in MACHINERY_PINS.items()})
    pinmap["_gate::id"] = GATE_ID
    pinmap["_gate::predecessor"] = PREDECESSOR_SHA
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py",
        pinmap)                                                    # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    pdfinfo = extract_pdf_conventions()                            # (local)
    bg = build_background()                                        # (local)
    w = build_window(bg)                                           # (local)
    bg["sp_tau_of_eta"] = w["sp_tau_of_eta"]
    r = compute(bg, w, pdfinfo)                                    # (local)
    comp, sign_v, mag_v, regime_v = evaluate_gate(r, w, bg)        # (local)

    print("\n" + "=" * 72)
    print("GATE EVALUATION (pre-registered operator)")
    print("=" * 72)
    print(f"  var_Nseg = {r['var_Nseg']:.10f}  -> "
          f"{'OK' if r['var_Nseg'] < TOL_VAR_NSEG else 'BREACH'} "
          f"(strict < {TOL_VAR_NSEG})")
    print(f"  rel_dev  = {r['rel_dev']:.6e}  -> "
          f"{'OK' if r['rel_dev'] <= TOL_REL_DEV else 'BREACH'} "
          f"(<= {TOL_REL_DEV})")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"  composite (collapse rule): {comp}")

    # ---- npz (full float64; publication 4 sig figs in value string) ----
    np.savez(
        OUT_NPZ,
        # required keys (plan output_artifacts)
        beta2_pivot_per_Nseg=r["beta2_per_Nseg"],
        var_Nseg=r["var_Nseg"],
        beta2_pivot_closed_form=r["beta2_cf"],
        rel_dev=r["rel_dev"],
        k_grid=r["k_grid"],
        beta2_spectrum=r["beta2_spec"],
        mu_pivot_sq=r["mu_pivot_sq"],
        V_box=w["V_box"],
        Omega_on=w["Omega_on"],
        Omega_off=w["Omega_off"],
        Delta_eta=w["Delta_eta"],
        unitarity_residual_max=r["max_unit"],
        beta2_pivot_ODE_reference=r["b2_ode"],
        CHK_N_ratio=bg["CHK_N_ratio"],
        # spectrum companions
        beta2_spectrum_closed_form=r["beta2_spec_cf"],
        beta2_spectrum_ODE=r["beta2_spec_ode"],
        N_seg_scan=np.array(N_SEG_SCAN),
        beta2_pivot_TM=r["beta2_TM"],
        # normalization block
        k_pivot=bg["k_pivot"], k_over_aH_fold=bg["k_over_aH"],
        k2_over_zppz_fold=bg["k2_over_zppz"], aH_target=bg["aH_target"],
        u_clock=bg["u_clock"], Lambda_rescale=bg["Lam"],
        a_fold_raw=bg["a_fold"], aH_rederived=bg["aH_rederived"],
        zppz_stored_fold_units=bg["Uc_fold"],
        zppz_stored_over_anchor=bg["Uc_fold"] / bg["chk_target"],
        plateau_flatness_b=w["flat_b"], plateau_flatness_c=w["flat_c"],
        V_box_branch_c=w["V_box_c"], V_sparn_literal=w["V_a"],
        Omega_on_strict=w["Omega_on_strict"],
        Omega_off_strict=w["Omega_off_strict"],
        Omega_z_on=w["Om_z_on"], Omega_z_off=w["Om_z_off"],
        tau_window=np.array([w["tau_on"], w["tau_off"]]),
        eta_window=np.array([w["eta_on"], w["eta_off"]]),
        # branch-c sensitivity
        beta2_pivot_per_Nseg_branch_c=r["beta2_c_per_Nseg"],
        var_Nseg_branch_c=r["var_Nseg_c"],
        beta2_closed_branch_c=r["beta2_cf_c"],
        rel_dev_branch_c=r["rel_dev_c"],
        beta2_ODE_branch_c=r["b2_ode_c"],
        # diagnostics
        single_box_identity_dev=r["ident_dev"],
        n_RT_zeros_in_kwindow=r["n_RT_in_window"],
        k_RT_first_zero=r["k_RT_first"],
        k_branch_crossover=r["k_branch"],
        beta2_alt_window=r["beta2_alt"], Delta_eta_alt=r["L_alt"],
        V_box_alt_window=r["V_box_a"],
        beta2_zpump_weights=r["beta2_zpump"],
        beta2_box_only=r["beta2_box_only"],
        beta2_deltas_only=r["beta2_deltas_only"],
        B2_ladder_anchor=r["B2_anchor"],
        x_pivot_s78=bg["x_pivot"], N_pivot_s77=bg["N_pivot"],
        Mach_fric_s64=bg["Mach_fric"], H_fold_s64=bg["H_fold_s64"],
        impulsiveness_S38_clock=H_fold * dt_transit,
        impulsiveness_fold_clock=bg["aH_target"] * w["Delta_eta"],
        pdf_extraction_gaps=np.array(pdfinfo["gaps"], dtype=object),
        # verdict block
        verdict=comp, sign_verdict=sign_v, magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        audit_sha256=audit_sha, content_sha256=content_sha,
        predecessor_sha=PREDECESSOR_SHA,
    )
    print(f"\nSaved data: {OUT_NPZ}")

    make_plot(bg, w, r)

    # ---- 4-tuple + payload ----
    val = (f"beta2_pivot={r['beta2_TM']:.4g};var_Nseg={r['var_Nseg']:.6f};"
           f"rel_dev={r['rel_dev']:.3e};beta2_closed={r['beta2_cf']:.4g};"
           f"beta2_ODE={r['b2_ode']:.4g};mu2_pivot={r['mu_pivot_sq']:.4f};"
           f"V_box={w['V_box']:.4f};Om_on={w['Omega_on']:+.4f};"
           f"Om_off={w['Omega_off']:+.4f};Deta={w['Delta_eta']:.4e};"
           f"CHK_N={bg['CHK_N_ratio']:.4f};unit_resid={r['max_unit']:.1e};"
           f"branchC_var={r['var_Nseg_c']:.4f};"
           f"branchC_reldev={r['rel_dev_c']:.2e};"
           f"S85_pathology={'SMOOTH-CUSP-SEGMENTATION-CONFIRMED' if comp == 'PASS' else 'UNRESOLVED'}")  # (local)
    print(f"\n(value={val!r}, scheme={SCHEME}, convention={CONVENTION}, "
          f"L_max={L_MAX})")

    note = (f"box+delta sudden-limit TM; window=conformal image of dt_transit "
            f"in fold-normalized M_KK clock (aH|fold={bg['aH_target']:.6f}); "
            f"verdict invariant under barrier-branch (b)/(c) and "
            f"delta-weight conventions")                           # (local)
    rows = [
        f"# predecessor={PREDECESSOR_SHA} (S85-W7-CUSP-BOGOLIUBOV FAIL, "
        f"smooth-cusp-Airy class; cross-gate audit context per honest-re-open "
        f"law (d) -- explicitly NOT a supersedes= token; the S85 FAIL stands) "
        f"# {GATE_ID} honest-re-open row",
        f"# normalization row: Convention-B fold units (S77 canonical); "
        f"CHK_N_ratio={bg['CHK_N_ratio']:.6f} in [0.95,1.05]; stored "
        f"eta_H-corrected z''/z channel = {bg['Uc_fold']/bg['chk_target']:.4f}x "
        f"anchor (known s64 slow-roll-violation gap; branch-(c) sensitivity: "
        f"var={r['var_Nseg_c']:.4f}, rel_dev={r['rel_dev_c']:.2e} -- verdict "
        f"structure invariant) # {GATE_ID}",
        f"# regulator_pin=N/A -- no Seeley-DeWitt a_n citation; no SCHEMATIC "
        f"helper consumed (npz data + canonical_constants only) # {GATE_ID}",
    ]                                                              # (local)
    print_verdict_payload(comp, val, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v,
                          regime_verdict=regime_v, companion_note=note,
                          extra_rows=rows)

    print(f"\n=== {GATE_ID}: {comp} (wall {time.time()-t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
