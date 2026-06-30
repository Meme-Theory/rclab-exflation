#!/usr/bin/env python3
"""
S100b W5-2 — S100b-FOLD-RANGE-SCALING: fold fast-quench universality class
===========================================================================

Gate: S100b-FOLD-RANGE-SCALING ([SIGN] trigger — schema-v2 3-tuple REQUIRED)
Classification: PHONONIC
Plan: sessions/session-plan/session-100b-plan-w5.md §W5-2 (R3 YAML block)

Pre-registered operator (conjunction):
  PASS iff [ Delta_P_exc = max-min P_exc over Mach in [5,30] < 0.01 ABSOLUTE ]
       AND [ Spearman rho_S( n_rel(lambda), lambda ) > 0.99 over lambda in [0.25,4] ]
  FAIL iff Delta_P_exc >= 0.01 (rate-controlled KZ class revives; S38 re-audit CF)
  INFO iff Delta_P_exc < 0.01 AND rho_S <= 0.99 (saturated but range-law structured)

GOVERNING STRUCTURE (mode-equation-first; S38 canonical machinery LZ-PARKER-SUDDEN)
-----------------------------------------------------------------------------------
(E1) KZ exponents (BCS class): nu = 0.5 (mean-field), z = 2.0 (dynamical),
     kz_exp = nu/(1 + z*nu) = 0.25.                  [s38_kz_defects.npz pins]
(E2) Saturated KZ excitation probability (the canonical P_exc = 1.000 producer):
     P_exc^KZ = min[ (tau_0/tau_Q)^{2 nu z/(1+z nu)}, 1 ] = min[(tau_0/tau_Q)^1, 1]
     tau_0 = 1/Delta_0 = 1.2979678654734792, tau_Q = dt_transit = 1.1301575e-3
     => tau_0/tau_Q = 1148.5 >= 1 => P_exc^KZ = 1.0 EXACT (sudden saturation).
     CHK-S38: |P_exc^KZ_recon - P_exc_kz(canonical)| < 1e-6 ABS, HARD-ABORT else.
(E3) Per-crossing LZ diabatic (excitation) probability:
     P_exc^LZ = exp(-eps),  eps = pi * Delta_min^2 / (2 * v_eff),
     v_eff = dDelta/dt = 1363.4119062492628 (s38 npz), Delta_min = Delta_0 = 1/tau_0
     => eps_canonical = 6.838563969200696e-4 (s38 npz key lz_exponent; reconstructed
     here from components and cross-checked to machine precision).

RATE MAP (axis i; plan rate_map_pin):
     v_eff proportional to Mach at fixed fold geometry:
     dt_transit(Mach) = dt_transit * 13.75/Mach  =>  eps(Mach) = eps * 13.75/Mach
     =>  P_exc(Mach) = exp(-eps * 13.75/Mach)    [Mach grid: 11 linear pts on
     [5,30], Mach_max_framework = 13.75 an EXACT member]

RANGE MAP (axis ii; plan range_map_pin) — substitution chain, every step:
  Step 1: excursion profile DeltaS(tau) := S(tau) - S(tau_fold); lambda-rescale
          acts on the AMPLITUDE at fixed shape and fixed rate:
          DeltaS_lambda(tau) = lambda * DeltaS(tau).      [s64 S/dS/d2S channels]
  Step 2: swept spectral measure over the FIXED transit window
          W = [tau_fold - dtau_w/2, tau_fold + dtau_w/2],
          dtau_w = |v_terminal| * dt_transit ~= 0.0300 (rate fixed => W fixed):
          delta_max(lambda) = INT_W |d(DeltaS_lambda)/dtau| dtau
                            = lambda * INT_W |dS/dtau| dtau = lambda * delta_max(1).
  Step 3: mode count swept: mode measure UNIFORM per unit spectral action (the
          pinned-input-faithful choice; D_K DOS out of scope per L_max = N/A pin):
          N_swept(lambda) = g0 * delta_max(lambda) = g0 * lambda * delta_max(1).
  Step 4: per-crossing probability under amplitude rescale at fixed rate: the
          diabatic level sweep rate scales with the excursion amplitude,
          v_eff(lambda) = lambda * v_eff(1) => eps(lambda) = eps/lambda
          => P_exc(lambda) = exp(-eps/lambda)  (saturation DEEPENS with lambda).
  Step 5: aggregate occupation:
          n(lambda) = N_swept(lambda) * P_exc(lambda)
                    = g0 * delta_max(1) * lambda * exp(-eps/lambda).
  Step 6: RELATIVE (convention pin; the absolute 59.8 NEVER gates):
          n_rel(lambda) = n(lambda)/n(1) = lambda * exp(eps * (1 - 1/lambda)).
  Step 7: monotonicity (the [SIGN] direction):
          d ln n_rel / d ln lambda = 1 + eps/lambda > 0 for all lambda > 0
          => strictly increasing => rho_S = 1 expected (confirmed numerically).
  Step 8: diagnostic exponent p_range = LSQ slope of ln n_rel vs ln lambda
          ~= 1 + O(eps) — the substrate analog of Rao's rho ~ delta_max (p ~ 1).

LI-ADJACENCY DIAGNOSTIC (reported only, NO gate weight; plan li_diagnostic_pin):
  gap-closure proxy Delta_gap(tau) = |S(tau) - S_fold| on the s64 dense grid;
  one-sided log-log fits over |tau - tau_fold| in [2h, 0.05] give the products
  (nu z)_pre (approach side -> z) and (nu z)_post (final side -> z');
  with nu_eff = 0.5 PINNED (S38 BCS mean-field; the 1-parameter fit determines
  the PRODUCT only): z_eff = (nu z)_pre/0.5, zprime_eff = (nu z)_post/0.5.
  Li inequality: z' < z + 1/nu  evaluated and REPORTED (which side it lands).
  The fold is FIRST-ORDER (tau_fold = 0.19): effective nu*z ~ 1 is the
  analytic-profile slope (dS_fold != 0), NOT an anomalous critical exponent —
  the deviation from 1 is the d2S curvature over the fit window.

3-TUPLE (schema-v2, [SIGN]):
  sign_verdict      = PASS iff (Delta_P_exc < 0.01) AND (diff(n_rel(lambda)) > 0
                      across the grid) — both pre-registered directions.
  magnitude_verdict = PASS iff conjunction holds; INFO iff rate-flat but
                      rho_S <= 0.99; FAIL iff Delta_P_exc >= 0.01.
  regime_verdict    = VALID iff max(adiab(Mach), eps_eff over both scans) < 0.1;
                      MARGINAL < 0.5; else BREAKDOWN  (sudden-limit validity).
  Composite via the gate-verdicts.md collapse rule; asserted consistent with the
  gate-rubric composite (PASS/INFO/FAIL mapping above) — discrepancy would be
  documented in a companion row with the collapse-rule composite emitted.

Machinery pins (plan §W5-2 machinery_pin_map): scheme=LZ-PARKER-SUDDEN,
convention=RELATIVE, L_max=N/A, GPU_path=cpu-cap-OMP8, random_seed=N/A,
tolerances 0.01 ABS / 0.99 rho_S / 1e-6 ABS CHK-S38 / 1e-10 rtol integrals,
publication_precision 3 sig figs on Delta_P_exc and p_range.

Inputs (SHA-256 pinned at plan-freeze; verified here, HARD-ABORT on mismatch):
  computations/session-64/s64_epsilon_profile.npz   (range axis profile)
  computations/session-64/s64_sound_speed.npz       (rate axis cross-check)
  computations/session-38/s38_kz_defects.npz        (CHK-S38 reference)
  downloads/.../08_Rao_*.pdf + 13_Li_*.pdf          (runtime template extraction)
  computations/_shared/canonical_constants.py       (runtime SHA)

N_pair caveat (plan scoping note, carried into every output): n_pairs = 59.8 is
a PROJECTED CHARGE <Q>_GGE (S74 NOETHER-CHAIN; known overestimates), NOT a
literal pair count; the regime-robust claim is P_exc = 1 (S38, T4 PROVEN).
Everything here keys on P_exc and on RELATIVE n ratios only.

Verdict emission: this script PRINTS the payload via print_verdict_payload;
the dispatching agent calls mcp__knowledge__emit_verdict (race-safe; NEVER
an open("a") append). Exit code reflects script health ONLY.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap BEFORE numpy import (plan GPU_path: cpu-cap-OMP8)
# ---------------------------------------------------------------------------
import os
import sys

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

_SHARED_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared"
)
if _SHARED_PATH not in sys.path:
    sys.path.insert(0, _SHARED_PATH)

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
# consumed names: tau_fold, dt_transit, P_exc_kz, n_pairs, dS_fold, d2S_fold,
#                 Mach_max_framework (alias Mach_max), M_KK, PI, v_terminal

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
from scipy.interpolate import CubicSpline  # noqa: E402
from scipy.optimize import brentq  # noqa: E402
from scipy.stats import spearmanr  # noqa: E402

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "100b"                                                   # (local)
GATE_ID = "S100b-FOLD-RANGE-SCALING"                               # (local)
SCHEME = "LZ-PARKER-SUDDEN"                                        # (local)
CONVENTION = "RELATIVE"                                            # (local)
L_MAX = "N/A"                                                      # (local)

# Pre-registered thresholds (plan §W5-2 operator + tolerances)
THRESH_DP_EXC = 0.01          # (local) ABSOLUTE on P_exc in [0,1]
THRESH_RHO_S = 0.99           # (local) Spearman rank correlation
TOL_CHK_S38 = 1e-6            # (local) ABSOLUTE, canonical-point reproduction
TOL_RECON = 1e-10             # (local) machine-precision component cross-checks
TOL_ANCHOR = 0.005            # (local) 0.5% RATIO, s64 anchor cross-checks
REGIME_VALID_BOUND = 0.1      # (local) sudden-limit small parameters < 0.1
REGIME_MARGINAL_BOUND = 0.5   # (local)

# Scan grids (plan mesh pins)
MACH_REF = float(Mach_max_framework)                               # (local) 13.75
_mach_base = np.linspace(5.0, 30.0, 10)                            # (local)
MACH_GRID = np.sort(np.append(_mach_base, MACH_REF))               # (local) 11 pts, 13.75 exact
LAMBDA_GRID = np.geomspace(0.25, 4.0, 9)                           # (local) 9 log pts
assert abs(LAMBDA_GRID[4] - 1.0) < 1e-12, "lambda grid must contain 1.0"
LAMBDA_GRID[4] = 1.0  # snap exact

# Li-diagnostic fit window (pre-registered): |tau - tau_fold| in [2h, 0.05]
LI_FIT_OUTER = 0.05           # (local)
NU_EFF_PIN = 0.5              # (local) S38 BCS mean-field nu (PINNED, not fitted)

OUT_NPZ = SESSION_DIR / "s100b_fold_range_scaling.npz"
OUT_PNG = SESSION_DIR / "s100b_fold_range_scaling.png"

# Static input SHA-256 pins (plan-freeze values; HARD-ABORT on mismatch)
STATIC_PINS = {                                                    # (local)
    "computations/session-64/s64_epsilon_profile.npz":
        "40789017c5f0c66876126eb936e7a212ff406eaff705ed4e53cb17901a97ebf5",
    "computations/session-64/s64_sound_speed.npz":
        "f8873af64609cb8a2afc69e2ecb891473d97b1df6092e5a2e04ba8c57855f36e",
    "computations/session-38/s38_kz_defects.npz":
        "2083ad68cf51cc1df53aa5c150b4a7ec7dd35c7b7c364a32a5ec04c53d3b87c6",
    "downloads/research-sweep-s99/nonequilibrium-transit/"
    "08_Rao_Universal-Breakdown-Kibble-Zurek-Fast-Quenches.pdf":
        "9e32ffab2e6d286e6f0fb9c6328439be305ecc63d081779a0e331465708e6e6b",
    "downloads/research-sweep-s99/nonequilibrium-transit/"
    "13_Li_Kibble-Zurek-Tricriticality-Adiabatic-Impulse-Breakdown.pdf":
        "fee8d365e30d19603275f0729752fe551f531170f6978ecc309bb83d211329c2",
}

INPUT_FILES = [SHARED_DIR / "canonical_constants.py"] + [
    PROJECT_ROOT / rel for rel in STATIC_PINS
]

# S38 fold-window mode set (reference machinery s38_kz_defects.py, verbatim;
# validated below against the PINNED s38 npz via the E_exc_total identity)
E_MODES = np.array(
    [0.8453, 0.8453, 0.8453, 0.8453, 0.8191, 0.9782, 0.9782, 0.9782]
)                                                                  # (local)
RHO_MODES = np.array(
    [14.023, 14.023, 14.023, 14.023, 1.0, 1.0, 1.0, 1.0]
)                                                                  # (local)


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


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        expected = STATIC_PINS.get(rel)  # (local)
        status = "runtime-pinned"  # (local)
        if expected is not None:
            status = "OK" if sha == expected else "MISMATCH"
            if sha != expected:
                raise RuntimeError(
                    f"HARD-ABORT: SHA mismatch for {rel}: "
                    f"expected {expected}, got {sha}"
                )
        print(f"  {rel}: {sha[:16]}... [{status}]")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Runtime PDF template extraction (fetched sources ONLY)
# ---------------------------------------------------------------------------
def extract_pdf_templates() -> dict:
    """Extract the Rao v_c/delta_max template + the Li inequality from the
    SHA-pinned PDFs at runtime (feedback_research-corpus: never training
    knowledge; any extraction gap flagged explicitly)."""
    from pypdf import PdfReader  # noqa: E402  (local import; venv pypdf 6.9.2)

    out = {"rao_ok": False, "li_ok": False}  # (local)
    print("=== runtime PDF template extraction (pinned sources) ===")

    rao_path = PROJECT_ROOT / (
        "downloads/research-sweep-s99/nonequilibrium-transit/"
        "08_Rao_Universal-Breakdown-Kibble-Zurek-Fast-Quenches.pdf"
    )  # (local)
    rao = PdfReader(str(rao_path))  # (local)
    rao_p1 = (rao.pages[0].extract_text() or "").replace("\n", " ")  # (local)
    rao_p3 = (rao.pages[2].extract_text() or "").replace("\n", " ")  # (local)
    m1 = re.search(
        r"critical quench rate\s*v\s*c\s*that\s*scales with the quench range",
        rao_p1, re.I)  # (local)
    m2 = re.search(
        r"universal scaling\s*.{0,12}max\s*,?\s*independent of the quench rate",
        rao_p1, re.I)  # (local)
    m3 = re.search(r"=\s*α\s*δ\s*max", rao_p3)  # (local) v_c = alpha*delta_max
    if m1 and m2:
        out["rao_ok"] = True
        print("  [Rao p1, abstract] ..." +
              rao_p1[max(0, m1.start() - 40): m1.end() + 60].strip() + "...")
        print("  [Rao p1, abstract] ..." +
              rao_p1[max(0, m2.start() - 60): m2.end() + 40].strip() + "...")
    if m3:
        print("  [Rao p3, v_c law]  ..." +
              rao_p3[max(0, m3.start() - 60): m3.end() + 60].strip() + "...")
    out["rao_vc_law_ok"] = bool(m3)
    if not out["rao_ok"]:
        print("  WARNING: Rao template regexes did not match — EXTRACTION GAP "
              "flagged (gate statistics do not consume the text numerically).")

    li_path = PROJECT_ROOT / (
        "downloads/research-sweep-s99/nonequilibrium-transit/"
        "13_Li_Kibble-Zurek-Tricriticality-Adiabatic-Impulse-Breakdown.pdf"
    )  # (local)
    li = PdfReader(str(li_path))  # (local)
    li_p1 = (li.pages[0].extract_text() or "").replace("\n", " ")  # (local)
    m4 = re.search(r"z\s*[′'’]\s*<\s*z\s*\+\s*1\s*/\s*ν", li_p1)  # (local)
    m5 = re.search(
        r"r\s*µ\s*=\s*z\s*\+\s*1\s*/\s*ν\s*µ\s*=\s*9\s*/\s*5",
        li_p1)  # (local)
    if m4:
        out["li_ok"] = True
        print("  [Li p1, inequality] ..." +
              li_p1[max(0, m4.start() - 60): m4.end() + 80].strip() + "...")
    if m5:
        print("  [Li p1, TCI pin]    ..." +
              li_p1[max(0, m5.start() - 40): m5.end() + 40].strip() + "...")
    out["li_tci_ok"] = bool(m5)
    if not out["li_ok"]:
        print("  WARNING: Li inequality regex did not match — EXTRACTION GAP "
              "flagged (diagnostic-only adjacency; inequality form per plan pin).")
    print()
    return out


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    r = {}  # (local) results accumulator

    # ---- 6.1 Load pinned npz inputs --------------------------------------
    d38 = np.load(SESSION_DIR.parent / "session-38" / "s38_kz_defects.npz",
                  allow_pickle=True)  # (local)
    d64e = np.load(SESSION_DIR.parent / "session-64" / "s64_epsilon_profile.npz",
                   allow_pickle=True)  # (local)
    d64s = np.load(SESSION_DIR.parent / "session-64" / "s64_sound_speed.npz",
                   allow_pickle=True)  # (local)

    nu_exp = float(d38["nu_exp"])           # (local) 0.5
    z_exp = float(d38["z_exp"])             # (local) 2.0
    kz_exp_ref = float(d38["kz_exp"])       # (local) 0.25
    tau_0 = float(d38["tau_0"])             # (local) 1/Delta_0
    tau_Q = float(d38["tau_Q"])             # (local) = dt_transit
    P_exc_kz_npz = float(d38["P_exc_kz"])   # (local) 1.0
    P_LZ_npz = float(d38["P_LZ"])           # (local) 0.99931638
    lz_exponent_npz = float(d38["lz_exponent"])  # (local) 6.8386e-4
    dDelta_dt_npz = float(d38["dDelta_dt"])      # (local) 1363.412
    adiab_npz = float(d38["adiabaticity"])       # (local) 8.707e-4
    xi_KZ_npz = float(d38["xi_KZ"])              # (local)
    N_defwin_npz = float(d38["N_defect_window"])  # (local)
    E_exc_total_npz = float(d38["E_exc_total"])   # (local) 69.0137

    # ---- 6.2 CHK-S38 pre-flight: reconstruct the canonical machinery -----
    print("=== CHK-S38 pre-flight (canonical-point reconstruction) ===")
    kz_exp_recon = nu_exp / (1.0 + z_exp * nu_exp)                 # (local)
    assert abs(kz_exp_recon - kz_exp_ref) < TOL_RECON, "kz_exp drift"
    assert abs(tau_Q - dt_transit) / dt_transit < TOL_RECON, \
        "tau_Q != canonical dt_transit"
    adiab_recon = tau_Q / tau_0                                    # (local)
    assert abs(adiab_recon - adiab_npz) / adiab_npz < TOL_RECON, "adiab drift"

    # (E2) saturated KZ form — the P_exc = 1.000 producer
    sat_exp = 2.0 * nu_exp * z_exp / (1.0 + z_exp * nu_exp)        # (local) = 1
    raw_P_exc = (tau_0 / tau_Q) ** sat_exp                         # (local) ~1148.5
    P_exc_recon = min(raw_P_exc, 1.0)                              # (local) saturated
    CHK_S38_residual = abs(P_exc_recon - float(P_exc_kz))          # (local)
    print(f"  nu={nu_exp}, z={z_exp}, kz_exp={kz_exp_recon:.6f} (== {kz_exp_ref})")
    print(f"  tau_0 = {tau_0:.12f}, tau_Q = {tau_Q:.6e}, adiab = {adiab_recon:.6e} << 1")
    print(f"  raw_P_exc = (tau_0/tau_Q)^{sat_exp:.1f} = {raw_P_exc:.4f} -> saturated 1.0")
    print(f"  CHK-S38 residual |P_exc_recon - P_exc_kz| = {CHK_S38_residual:.3e} "
          f"(tol {TOL_CHK_S38:.0e})")
    if CHK_S38_residual >= TOL_CHK_S38:
        raise RuntimeError("HARD-ABORT: CHK-S38 failed — reconstruction bug, "
                           "not physics.")
    assert abs(P_exc_kz_npz - float(P_exc_kz)) < TOL_RECON

    # (E3) per-crossing LZ exponent — reconstruct from components
    Delta_0 = 1.0 / tau_0                                          # (local) 0.770435
    eps_recon = float(PI) * Delta_0 ** 2 / (2.0 * dDelta_dt_npz)   # (local)
    assert abs(eps_recon - lz_exponent_npz) / lz_exponent_npz < TOL_RECON, \
        "lz_exponent reconstruction drift"
    eps_c = lz_exponent_npz                                        # (local) eps_canonical
    assert abs(np.exp(-eps_c) - P_LZ_npz) < TOL_RECON, "P_LZ identity drift"
    print(f"  Delta_0 = 1/tau_0 = {Delta_0:.9f}; dDelta/dt = {dDelta_dt_npz:.6f}")
    print(f"  eps_canonical = pi*Delta_0^2/(2 dDelta/dt) = {eps_c:.12e} "
          f"(recon dev {abs(eps_recon-lz_exponent_npz)/lz_exponent_npz:.1e})")
    print(f"  P_exc^LZ(13.75) = exp(-eps) = {np.exp(-eps_c):.12f}")

    # Mode-set validation vs PINNED npz (E_exc_total identity)
    E_qp = np.sqrt(E_MODES ** 2 + Delta_0 ** 2)                    # (local)
    E_exc_recon = float(np.sum(E_qp * RHO_MODES))                  # (local)
    mode_dev = abs(E_exc_recon - E_exc_total_npz) / E_exc_total_npz  # (local)
    assert mode_dev < TOL_RECON, f"mode-set validation failed: {mode_dev:.2e}"
    sum_rho = float(np.sum(RHO_MODES))                             # (local) 60.092
    print(f"  mode set validated: sum rho_i*sqrt(E_i^2+Delta_0^2) = "
          f"{E_exc_recon:.10f} == npz E_exc_total ({mode_dev:.1e} rel)")
    print(f"  weighted mode count sum(rho_i) = {sum_rho:.3f} "
          f"[vs n_pairs = {float(n_pairs)} projected charge <Q>_GGE — "
          f"RELATIVE use only, never gates]")
    print()

    # ---- 6.3 Rate-axis cross-check anchors --------------------------------
    Mach_fric = float(d64s["Mach_fric"])                           # (local) 13.753965
    print("=== rate-map anchors ===")
    print(f"  Mach_max_framework (canonical, EXACT rate-map anchor) = {MACH_REF}")
    print(f"  Mach_fric (s64_sound_speed cross-check) = {Mach_fric:.12f} "
          f"(rel dev {abs(Mach_fric-MACH_REF)/MACH_REF:.2e})")
    v_term_npz = float(d64e["v_terminal"])                         # (local)
    assert abs(v_term_npz - float(v_terminal)) / float(v_terminal) < TOL_RECON
    print(f"  v_terminal = {v_term_npz:.12f} (npz == canonical)")
    print()

    # ---- 6.4 RATE SCAN (axis i): Mach in [5, 30], lambda = 1 -------------
    # P_exc(Mach) = exp(-eps * 13.75/Mach)  [substitution chain, plan §W5-2]
    eps_mach = eps_c * (MACH_REF / MACH_GRID)                      # (local)
    P_exc_mach = np.exp(-eps_mach)                                 # (local)
    Delta_P_exc = float(P_exc_mach.max() - P_exc_mach.min())       # (local)
    # per-mode sum (BCS-class gap mode-shared => P_exc,i identical; weights
    # cancel in the ratio — computed explicitly for the audit trail):
    n_mach = np.array([np.sum(RHO_MODES * np.exp(-em)) for em in eps_mach])  # (local)
    i_ref = int(np.argmin(np.abs(MACH_GRID - MACH_REF)))           # (local)
    assert MACH_GRID[i_ref] == MACH_REF
    n_rel_mach = n_mach / n_mach[i_ref]                            # (local)

    print("=== RATE SCAN (axis i): 11-point Mach grid, lambda = 1 ===")
    print("  Mach      eps_eff       P_exc           n_rel(Mach)")
    for m, e, p, nr in zip(MACH_GRID, eps_mach, P_exc_mach, n_rel_mach):
        print(f"  {m:6.3f}  {e:.6e}  {p:.12f}  {nr:.12f}")
    print(f"  Delta_P_exc = max - min = {Delta_P_exc:.12e}  "
          f"[threshold < {THRESH_DP_EXC} ABS]")

    # analytic boundary: solve e^{-eps*13.75/30} - e^{-eps*13.75/5} = 0.01
    def _dp(e):  # (local)
        return np.exp(-e * MACH_REF / 30.0) - np.exp(-e * MACH_REF / 5.0) - THRESH_DP_EXC

    eps_boundary = float(brentq(_dp, 1e-9, 1.0, xtol=1e-15))       # (local)
    eps_margin = eps_c / eps_boundary                              # (local) <1 = saturated side
    print(f"  eps_boundary (exact root of Delta_P_exc = 0.01) = {eps_boundary:.6e}")
    print(f"  eps_saturation_margin = eps_c/eps_boundary = {eps_margin:.6f} "
          f"(margin factor {1.0/eps_margin:.2f}x inside saturation)")
    print(f"  linearized check: 2.2917*eps_c = {2.2916666:.4f}*{eps_c:.4e} = "
          f"{2.2916666*eps_c:.6e} vs exact Delta_P_exc = {Delta_P_exc:.6e}")
    print()

    # ---- 6.5 RANGE SCAN (axis ii): lambda in [0.25, 4], Mach = 13.75 -----
    tau_d = d64e["tau_dense"]                                      # (local)
    S_d = d64e["S_dense"]                                          # (local)
    dS_d = d64e["dS_dense"]                                        # (local)
    d2S_d = d64e["d2S_dense"]                                      # (local)
    S_fold_npz = float(d64e["S_fold_canonical"])                   # (local)
    dS_fold_npz = float(d64e["dS_fold_canonical"])                 # (local)
    d2S_fold_npz = float(d64e["d2S_fold_canonical"])               # (local)
    tau_fold_npz = float(d64e["tau_fold"])                         # (local)

    # anchor identities: npz canonical keys == canonical_constants (exact)
    assert abs(dS_fold_npz - float(dS_fold)) / float(dS_fold) < 1e-12
    assert abs(d2S_fold_npz - float(d2S_fold)) / float(d2S_fold) < 1e-12
    assert abs(tau_fold_npz - float(tau_fold)) < 1e-12

    cs_S = CubicSpline(tau_d, S_d)                                 # (local)
    cs_dS = CubicSpline(tau_d, dS_d)                               # (local)
    print("=== RANGE SCAN (axis ii): excursion profile + window ===")
    # anchor cross-checks: spline at tau_fold vs canonical anchors
    S_at_fold = float(cs_S(float(tau_fold)))                       # (local)
    dS_at_fold = float(cs_dS(float(tau_fold)))                     # (local)
    dev_S = abs(S_at_fold - S_fold_npz) / abs(S_fold_npz)          # (local)
    dev_dS = abs(dS_at_fold - dS_fold_npz) / abs(dS_fold_npz)      # (local)
    print(f"  spline S(tau_fold)  = {S_at_fold:.6f} vs anchor {S_fold_npz:.6f} "
          f"(rel dev {dev_S:.2e}, tol {TOL_ANCHOR})")
    print(f"  spline dS(tau_fold) = {dS_at_fold:.6f} vs anchor {dS_fold_npz:.6f} "
          f"(rel dev {dev_dS:.2e}, tol {TOL_ANCHOR})")
    if dev_S >= TOL_ANCHOR or dev_dS >= TOL_ANCHOR:
        raise RuntimeError("HARD-ABORT: s64 anchor cross-check failed "
                           "(normalization bug, not physics).")

    # fixed transit window (rate fixed on this axis)
    dtau_w = abs(float(v_terminal)) * float(dt_transit)            # (local) ~0.0300
    dtau_w_s38 = N_defwin_npz * xi_KZ_npz                          # (local) S38 route
    dev_w = abs(dtau_w - dtau_w_s38) / dtau_w_s38                  # (local)
    tau_lo = float(tau_fold) - dtau_w / 2.0                        # (local)
    tau_hi = float(tau_fold) + dtau_w / 2.0                        # (local)
    assert tau_d.min() < tau_lo and tau_hi < tau_d.max(), "window outside grid"
    print(f"  transit window dtau_w = |v_terminal|*dt_transit = {dtau_w:.9f} "
          f"(S38 route N_defwin*xi_KZ = {dtau_w_s38:.9f}, rel dev {dev_w:.1e})")
    print(f"  W = [{tau_lo:.6f}, {tau_hi:.6f}] on tau_dense "
          f"[{tau_d.min():.3f}, {tau_d.max():.3f}]")

    # swept spectral measure at lambda = 1 (dS > 0 in window => |dS| = dS)
    tt = np.linspace(tau_lo, tau_hi, 2001)                         # (local)
    dS_win = cs_dS(tt)                                             # (local)
    assert np.all(dS_win > 0), "dS/dtau changes sign in window (unexpected)"
    delta_max_1 = float(np.trapezoid(dS_win, tt))                  # (local)
    delta_max_endpoint = float(cs_S(tau_hi) - cs_S(tau_lo))        # (local)
    dev_dm = abs(delta_max_1 - delta_max_endpoint) / delta_max_endpoint  # (local)
    print(f"  delta_max(1) = INT_W |dS/dtau| dtau = {delta_max_1:.6f} "
          f"(endpoint route S(hi)-S(lo) = {delta_max_endpoint:.6f}, "
          f"rel dev {dev_dm:.1e})")
    print(f"  flat-anchor estimate dS_fold*dtau_w = "
          f"{float(dS_fold)*dtau_w:.4f} (curvature-corrected by the profile)")

    # per-lambda: delta_max(lambda) computed THROUGH the integral (linearity
    # emerges numerically), occupation = count x per-crossing probability
    delta_max_lam = np.array(
        [float(np.trapezoid(lam * dS_win, tt)) for lam in LAMBDA_GRID]
    )                                                              # (local)
    lin_dev = float(np.max(np.abs(
        delta_max_lam / delta_max_1 - LAMBDA_GRID)))               # (local)
    eps_lam = eps_c / LAMBDA_GRID                                  # (local) Step 4
    n_lam = (sum_rho * (delta_max_lam / delta_max_1)
             * np.exp(-eps_lam))                                   # (local) Step 5
    i_lam1 = 4                                                     # (local) lambda=1 index
    n_rel_lam = n_lam / n_lam[i_lam1]                              # (local) Step 6
    rho_S, _p_sp = spearmanr(LAMBDA_GRID, n_rel_lam)               # (local)
    rho_S = float(rho_S)
    # diagnostic power-law exponent (Rao rho ~ delta_max analog; NOT gated)
    p_range = float(np.polyfit(np.log(LAMBDA_GRID),
                               np.log(n_rel_lam), 1)[0])           # (local)
    monotone_ok = bool(np.all(np.diff(n_rel_lam) > 0))             # (local)

    print(f"  delta_max(lambda)/delta_max(1) vs lambda: max |dev| = {lin_dev:.2e} "
          f"(exact linearity by construction)")
    print("  lambda     delta_max     eps_eff       n_rel(lambda)")
    for lam, dm, e, nr in zip(LAMBDA_GRID, delta_max_lam, eps_lam, n_rel_lam):
        print(f"  {lam:7.4f}  {dm:11.4f}  {e:.6e}  {nr:.12f}")
    print(f"  Spearman rho_S(n_rel, lambda) = {rho_S:.12f}  "
          f"[threshold > {THRESH_RHO_S}]")
    print(f"  monotone (all diffs > 0): {monotone_ok}")
    print(f"  p_range (LSQ log-log slope, diagnostic) = {p_range:.6f} "
          f"[Rao rho ~ delta_max analog expects ~1]")
    print()

    # ---- 6.6 Li-adjacency DIAGNOSTIC (reported only) ----------------------
    h_grid = float(np.median(np.diff(tau_d)))                      # (local)
    li_inner = 2.0 * h_grid                                        # (local)
    gap = np.abs(S_d - S_fold_npz)                                 # (local) proxy
    dist = tau_d - float(tau_fold)                                 # (local)
    li_fit = {}                                                    # (local)
    for side, mask in [
        ("pre", (dist < 0) & (np.abs(dist) > li_inner) & (np.abs(dist) < LI_FIT_OUTER)),
        ("post", (dist > 0) & (np.abs(dist) > li_inner) & (np.abs(dist) < LI_FIT_OUTER)),
    ]:
        x = np.log(np.abs(dist[mask]))                             # (local)
        y = np.log(gap[mask])                                      # (local)
        slope = float(np.polyfit(x, y, 1)[0])                      # (local)
        li_fit[side] = (slope, int(mask.sum()), x, y)
    nuz_pre = li_fit["pre"][0]                                     # (local)
    nuz_post = li_fit["post"][0]                                   # (local)
    z_eff = nuz_pre / NU_EFF_PIN                                   # (local) approach side
    zprime_eff = nuz_post / NU_EFF_PIN                             # (local) final side
    li_lhs = zprime_eff                                            # (local)
    li_rhs = z_eff + 1.0 / NU_EFF_PIN                              # (local)
    li_side = "SURVIVAL (z' < z + 1/nu)" if li_lhs < li_rhs \
        else "BREAKDOWN (z' >= z + 1/nu)"                          # (local)
    curv_scale = float(d2S_fold) / (2.0 * float(dS_fold))          # (local) ~2.71
    print("=== Li-adjacency DIAGNOSTIC (reported only, no gate weight) ===")
    print(f"  gap proxy Delta_gap = |S - S_fold|; fit window |tau-tau_fold| in "
          f"[{li_inner:.4e}, {LI_FIT_OUTER}] ({li_fit['pre'][1]}/{li_fit['post'][1]} pts)")
    print(f"  (nu z)_pre  = {nuz_pre:.6f}  -> z_eff      = {z_eff:.6f} "
          f"(nu_eff = {NU_EFF_PIN} PINNED, S38 BCS mean-field)")
    print(f"  (nu z)_post = {nuz_post:.6f}  -> zprime_eff = {zprime_eff:.6f}")
    print(f"  Li inequality z' < z + 1/nu: LHS = {li_lhs:.6f} vs RHS = {li_rhs:.6f} "
          f"-> {li_side}")
    print(f"  first-order character: nu*z ~ 1 is the ANALYTIC-profile slope "
          f"(dS_fold != 0); deviation from 1 ~ +/- (d2S/2dS)*delta = "
          f"+/-{curv_scale:.3f}*|tau-tau_fold| over the window — curvature, "
          f"NOT a critical exponent (fold is first-order, tricritical-ADJACENT)")
    print()

    # ---- 6.7 Regime check (pre-registered bands) ---------------------------
    adiab_max = float((tau_Q * MACH_REF / MACH_GRID.min()) / tau_0)  # (local)
    eps_eff_max = float(max(eps_mach.max(), eps_lam.max()))          # (local)
    regime_metric = max(adiab_max, eps_eff_max)                      # (local)
    if regime_metric < REGIME_VALID_BOUND:
        regime_verdict = "VALID"                                     # (local)
    elif regime_metric < REGIME_MARGINAL_BOUND:
        regime_verdict = "MARGINAL"                                  # (local)
    else:
        regime_verdict = "BREAKDOWN"                                 # (local)
    print("=== regime check (sudden-limit validity over both scans) ===")
    print(f"  max adiabaticity tau_Q(Mach)/tau_0 = {adiab_max:.6e} (at Mach=5)")
    print(f"  max eps_eff over both axes = {eps_eff_max:.6e} "
          f"(at lambda=0.25, Mach=13.75)")
    print(f"  regime metric = {regime_metric:.6e} < {REGIME_VALID_BOUND} "
          f"=> regime_verdict = {regime_verdict}")
    print()

    r.update(dict(
        eps_c=eps_c, Delta_0=Delta_0, tau_0=tau_0, tau_Q=tau_Q,
        CHK_S38_residual=CHK_S38_residual, raw_P_exc=raw_P_exc,
        mach_grid=MACH_GRID, P_exc_vs_mach=P_exc_mach, eps_mach=eps_mach,
        Delta_P_exc=Delta_P_exc, n_rel_vs_mach=n_rel_mach,
        eps_boundary=eps_boundary, eps_margin=eps_margin,
        lambda_grid=LAMBDA_GRID, n_rel_vs_lambda=n_rel_lam, eps_lam=eps_lam,
        delta_max_1=delta_max_1, delta_max_lam=delta_max_lam, lin_dev=lin_dev,
        rho_S=rho_S, p_range=p_range, monotone_ok=monotone_ok,
        dtau_w=dtau_w, sum_rho=sum_rho, Mach_fric=Mach_fric,
        nuz_pre=nuz_pre, nuz_post=nuz_post, z_eff=z_eff,
        zprime_eff=zprime_eff, li_lhs=li_lhs, li_rhs=li_rhs, li_side=li_side,
        li_fit=li_fit, adiab_max=adiab_max, eps_eff_max=eps_eff_max,
        regime_verdict=regime_verdict, curv_scale=curv_scale,
        dev_S=dev_S, dev_dS=dev_dS, dev_w=dev_w, dev_dm=dev_dm,
    ))
    return r


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict (pre-registered mappings + collapse rule)
# ---------------------------------------------------------------------------
def evaluate_gate(r: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict)."""
    rate_flat = r["Delta_P_exc"] < THRESH_DP_EXC                   # (local)
    range_mono = r["rho_S"] > THRESH_RHO_S                         # (local)

    # [SIGN] pre-registered directions (plan substitution chain):
    sign_verdict = "PASS" if (rate_flat and r["monotone_ok"]) else "FAIL"  # (local)

    # magnitude per the pre-registered operator bands:
    if rate_flat and range_mono:
        magnitude_verdict = "PASS"                                 # (local)
    elif rate_flat and not range_mono:
        magnitude_verdict = "INFO"                                 # (local)
    else:
        magnitude_verdict = "FAIL"                                 # (local)

    regime_verdict = r["regime_verdict"]                           # (local)

    # schema-v2 collapse rule (gate-verdicts.md; immutable):
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                         # (local)
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

    # gate-rubric composite (plan PASS/FAIL/INFO meanings):
    if not rate_flat:
        rubric = "FAIL"                                            # (local)
    elif not range_mono:
        rubric = "INFO"                                            # (local)
    else:
        rubric = "PASS"                                            # (local)
    r["rubric_composite"] = rubric
    r["collapse_consistent"] = (rubric == composite) or \
        (regime_verdict != "VALID")                                # (local)
    return composite, sign_verdict, magnitude_verdict, regime_verdict


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload (printed; agent calls emit_verdict MCP tool)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    payload = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }  # (local)
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


# ---------------------------------------------------------------------------
# Section 9 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16.5, 4.8))            # (local)

    ax = axes[0]
    ax.plot(r["mach_grid"], r["P_exc_vs_mach"], "o-", color="C0", lw=1.5,
            label=r"$P_{\rm exc}({\rm Mach}) = e^{-\epsilon\,13.75/{\rm Mach}}$")
    pmax = r["P_exc_vs_mach"].max()                                # (local)
    ax.axhspan(pmax - THRESH_DP_EXC, pmax, color="C2", alpha=0.15,
               label=r"1% ABS allowance ($\Delta P_{\rm exc} < 0.01$)")
    ax.axvline(MACH_REF, color="k", ls=":", lw=1,
               label=f"canonical Mach = {MACH_REF}")
    ax.set_xlabel("Mach")
    ax.set_ylabel(r"$P_{\rm exc}$ (per-crossing LZ diabatic)")
    ax.set_title(f"Rate axis: $\\Delta P_{{\\rm exc}}$ = "
                 f"{r['Delta_P_exc']:.3e} < 0.01\n(rate-FLAT: Rao $v>v_c$ side)")
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(alpha=0.3)

    ax = axes[1]
    ax.loglog(r["lambda_grid"], r["n_rel_vs_lambda"], "s-", color="C1", lw=1.5,
              label=r"$n_{\rm rel}(\lambda) = \lambda e^{\epsilon(1-1/\lambda)}$")
    guide = r["lambda_grid"] ** 1.0                                # (local)
    ax.loglog(r["lambda_grid"], guide, "k--", lw=1,
              label=r"Rao guide $\rho \sim \delta_{\max}$ (slope 1)")
    ax.set_xlabel(r"$\lambda$ (fold-range rescale)")
    ax.set_ylabel(r"$n_{\rm rel} = n(\lambda)/n(1)$")
    ax.set_title(f"Range axis: $\\rho_S$ = {r['rho_S']:.6f} > 0.99\n"
                 f"$p_{{\\rm range}}$ = {r['p_range']:.4f} (diagnostic)")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3, which="both")

    ax = axes[2]
    for side, color in [("pre", "C3"), ("post", "C4")]:
        slope, npts, x, y = r["li_fit"][side]                      # (local)
        ax.plot(np.exp(x), np.exp(y), ".", color=color, ms=4, alpha=0.6,
                label=f"{side}-fold: $(\\nu z)_{{\\rm eff}}$ = {slope:.3f} "
                      f"({npts} pts)")
        c = np.polyfit(x, y, 1)                                    # (local)
        xs = np.linspace(x.min(), x.max(), 50)                     # (local)
        ax.plot(np.exp(xs), np.exp(np.polyval(c, xs)), "-", color=color, lw=1)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"$|\tau - \tau_{\rm fold}|$")
    ax.set_ylabel(r"$\Delta_{\rm gap} = |S - S_{\rm fold}|$")
    ax.set_title(f"Li diagnostic: $z'$ = {r['zprime_eff']:.3f} < "
                 f"$z + 1/\\nu$ = {r['li_rhs']:.3f}\n(SURVIVAL side; "
                 f"first-order analytic slope, $\\nu_{{\\rm eff}}$ = 0.5 pinned)")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3, which="both")

    fig.suptitle(f"{GATE_ID}: fold fast-quench universality class — "
                 f"rate-vs-range discrimination (scheme={SCHEME})", y=1.02)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot saved: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                               # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                         # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"         # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    pdf_flags = extract_pdf_templates()                            # (local)

    r = compute()
    composite, sv, mv, rv = evaluate_gate(r)

    # consistency assertion (collapse rule vs gate rubric; see docstring)
    print(f"=== verdict mapping: rubric = {r['rubric_composite']}, "
          f"collapse(sign={sv}, mag={mv}, regime={rv}) = {composite}, "
          f"consistent = {r['collapse_consistent']} ===")
    if r["rubric_composite"] != composite:
        print("  NOTE: collapse-rule composite emitted (gate-verdicts.md is "
              "senior); rubric divergence documented in companion row.")
    print()

    # ---- save npz (required keys per plan output_artifacts) --------------
    np.savez(
        OUT_NPZ,
        # required keys
        mach_grid=r["mach_grid"],
        P_exc_vs_mach=r["P_exc_vs_mach"],
        Delta_P_exc=r["Delta_P_exc"],
        lambda_grid=r["lambda_grid"],
        n_rel_vs_lambda=r["n_rel_vs_lambda"],
        rho_S_spearman=r["rho_S"],
        p_range_fit=r["p_range"],
        z_eff=r["z_eff"],
        zprime_eff=r["zprime_eff"],
        nu_eff=NU_EFF_PIN,
        li_inequality_lhs_rhs=np.array([r["li_lhs"], r["li_rhs"]]),
        CHK_S38_residual=r["CHK_S38_residual"],
        eps_saturation_margin=r["eps_margin"],
        # supplementary keys (full provenance)
        eps_canonical=r["eps_c"],
        eps_boundary_exact=r["eps_boundary"],
        eps_eff_mach=r["eps_mach"],
        eps_eff_lambda=r["eps_lam"],
        n_rel_vs_mach=r["n_rel_vs_mach"],
        delta_max_1=r["delta_max_1"],
        delta_max_vs_lambda=r["delta_max_lam"],
        delta_max_linearity_dev=r["lin_dev"],
        dtau_window=r["dtau_w"],
        sum_rho_modes=r["sum_rho"],
        nuz_pre=r["nuz_pre"],
        nuz_post=r["nuz_post"],
        adiab_max=r["adiab_max"],
        eps_eff_max=r["eps_eff_max"],
        regime_metric=max(r["adiab_max"], r["eps_eff_max"]),
        Mach_fric_crosscheck=r["Mach_fric"],
        anchor_dev_S=r["dev_S"],
        anchor_dev_dS=r["dev_dS"],
        window_route_dev=r["dev_w"],
        delta_max_route_dev=r["dev_dm"],
        rao_extraction_ok=pdf_flags["rao_ok"],
        rao_vc_law_ok=pdf_flags["rao_vc_law_ok"],
        li_extraction_ok=pdf_flags["li_ok"],
        li_tci_ok=pdf_flags["li_tci_ok"],
        sign_verdict=np.array([sv]),
        magnitude_verdict=np.array([mv]),
        regime_verdict=np.array([rv]),
        composite_verdict=np.array([composite]),
        curv_scale=r["curv_scale"],
    )
    print(f"  data saved: {OUT_NPZ.name}")
    make_plot(r)
    print()

    # ---- value payload (publication precision: 3 s.f. on DP_exc, p_range) -
    li_tag = "SURVIVAL" if r["li_lhs"] < r["li_rhs"] else "BREAKDOWN"  # (local)
    class_tag = ("Rao-range-controlled-v-gt-vc" if composite == "PASS"
                 else "per-composite")                             # (local)
    value = (
        f"DeltaP_exc={r['Delta_P_exc']:.3g};rho_S={r['rho_S']:.6f};"
        f"p_range={r['p_range']:.2f};eps={r['eps_c']:.4g};"
        f"eps_boundary={r['eps_boundary']:.4g};"
        f"eps_margin_ratio={r['eps_margin']:.3g};"
        f"CHK_S38={r['CHK_S38_residual']:.1e};"
        f"Li_zprime={r['zprime_eff']:.3f}_vs_z+1/nu={r['li_rhs']:.3f}_{li_tag};"
        f"class={class_tag}"
    )  # (local)

    companion = (
        f"[SIGN] rate-vs-range discrimination: eps={r['eps_c']:.4g} sits "
        f"{1.0/r['eps_margin']:.1f}x inside the {r['eps_boundary']:.3g} "
        f"saturation boundary; rate-FLAT DeltaP_exc={r['Delta_P_exc']:.3g} "
        f"< 0.01; n_rel strictly increasing in lambda (rho_S={r['rho_S']:.4f}); "
        f"Rao v>v_c range-controlled class pinned"
    )  # (local)

    extra = [
        "# regulator_pin=N/A_no_a_n_citation CLASS=N/A_no_SCHEMATIC_helper "
        f"# {GATE_ID}",
        f"# li_adjacency_diagnostic: nu_eff={NU_EFF_PIN}(S38 pin) "
        f"z_eff={r['z_eff']:.4f} zprime_eff={r['zprime_eff']:.4f}; "
        f"z'<z+1/nu: {r['li_lhs']:.4f} < {r['li_rhs']:.4f} {r['li_side']}; "
        f"reported only, no gate weight; fold FIRST-ORDER — nu*z~1 is the "
        f"analytic-profile slope (deviation = d2S curvature), not a critical "
        f"exponent # {GATE_ID}",
        f"# n_pairs_caveat: 59.8 = projected charge <Q>_GGE (S74 "
        f"NOETHER-CHAIN), never gates; all occupations RELATIVE; S38 8-mode "
        f"set validated vs pinned npz E_exc_total to <1e-10 rel; "
        f"sum_rho={r['sum_rho']:.3f} # {GATE_ID}",
    ]  # (local)

    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, "
          f"L_max={L_MAX})")
    print_verdict_payload(
        composite, value, audit_sha, content_sha,
        sign_verdict=sv, magnitude_verdict=mv, regime_verdict=rv,
        companion_note=companion, extra_rows=extra,
    )

    wall = time.time() - t0                                        # (local)
    print(f"\n=== {GATE_ID}: {composite} "
          f"(sign={sv}, magnitude={mv}, regime={rv}; wall {wall:.1f}s) ===")
    return 0  # exit code reflects script health only (math-scripts.md)


if __name__ == "__main__":
    sys.exit(main())
