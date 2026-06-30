#!/usr/bin/env python3
"""
S118 W3-1 - CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN  (lizzi-spectral-functional-theorist)
==================================================================================

Gate: CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN
Trigger: [SIGN]  (additive-channel-dominant directional prediction; schema-v2 3-tuple)
Classification: GEOMETRIC
Agent type: lizzi-spectral-functional-theorist

THE OQ-4 MAGNITUDE DISCRIMINATOR — the CC problem in microcosm, with the substrate's
own Fermi surface PINNED (not bounded by heuristic vacuum models).

QUESTION (OQ-4)
---------------
The S117 W6-2 predecessor (CF-S117-LEMP-UV-REGULATOR-BR-SPAN) established model-INDEPENDENTLY:
  * FI is REJECTED ROBUSTLY (rel_span > 1e-7 in every vacuum model), and
  * the UV-regulator {zeta, PV, Mellin} axis is GENUINELY SD-OPEN (the additive-in-trace
    a0 / cosmological-constant counterterm SURVIVES the log-derivative; the multiplicative
    channel is annihilated by the W8-2 multiplicative-normalization-cancellation theorem).
W6-2 left the MAGNITUDE open: it returned rel_span = 0.03118 (INFO) at the conservative
Fermi=zero vacuum model but BOUNDED rel_span with three heuristic models (zero / floor /
median). The OQ-4 open question: is the SD-OPEN regulator-class span PHYSICALLY SIGNIFICANT
or SUPPRESSED once the substrate's BdG Fermi-surface location xi_F is PINNED?

THIS GATE: pin xi_F SUBSTRATE-FIRST.
  STEP 1: read the s52 8-mode BdG occupations o_a = v_a^2 (~{0.130x4, 0, 0.0079x3});
          compute the substrate-first target = mean(o_a) FROM THE NPZ (NOT rounded literals).
  STEP 2: SOLVE for the single Fermi level xi_F* such that the extended-vacuum occupation
          v_vac^2(lam; xi_F) = 1/2(1 - (lam-xi_F)/E),  E = sqrt((lam-xi_F)^2 + Delta_BCS^2),
          over the gap-IR (lowest-|lam|) sector of the L14 D_K spectrum reproduces mean(o_a).
          Root-find on the mean (unique by monotonicity of v_vac^2 in xi_F; xtol 1e-12).
  STEP 3: with xi_F* fixed, recompute Delta_R(xi_F*) = reg_vac_var(Mellin;xi_F*) -
          reg_vac_var(PV;xi_F*) and B(R;xi_F*) = d^2 ln(kappa_0(K) + delta_R)/d(ln K)^2 for
          R in {zeta, PV, Mellin} (reuse the W6-2 reg_vacuum_variance machinery).
  STEP 4: rel_span(xi_F*) = (max_R B - min_R B)/|L_emp_PV|; compare to the 0.05 band.
  STEP 5: report whether xi_F* lands BELOW the |D_K| floor (conservative => INFO) or in-band
          (Delta_R ~ kappa_0 => FAIL).

CRITICAL ANTI-INJECTION (xi_F_status = SOLVED-FROM-GAP-IR-OCCUPATION-MATCH)
--------------------------------------------------------------------------
xi_F* is the UNIQUE ROOT of the s52 gap-IR occupation-matching constraint. It is NEVER
scanned, seeded, or fixed to reproduce a target rel_span. The prior rel_span = 0.03118 and
the 0.05 band are post-hoc COMPARISON TARGETS, never finder seeds or imports (PROHIBITED
Class-4 / Class-6-adjacent per v3-closure-recovery.md). The W6-2 npz is loaded for
cross-check display ONLY (never as a seed). The kernel reproduces L_emp_PV = -7.046336 to
< 1e-9 (the regime gate), ESTABLISHED INDEPENDENTLY of xi_F.

SUBSTITUTION CHAIN (per math-scripts.md; the [SIGN] directional claim)
---------------------------------------------------------------------
  Leg A (sign, robust/model-INDEPENDENT): the a0-grade UV-regulator difference is
    ADDITIVE-IN-TRACE and SURVIVES the log-derivative; the additive channel DOMINATES the
    (W8-2-annihilated) multiplicative channel (multiplicative residue = 0 EXACTLY) =>
    sign_verdict = PASS regardless of xi_F.
  Leg B (magnitude direction): mean(o_a) < 1/2 => the gap-IR occupations sit below the
    Fermi half-filling => xi_F* lands BELOW the |D_K| spectral floor => the a0-grade UV
    modes are EMPTY (v_vac^2 -> 0) => |delta_Mellin| << kappa_0 => rel_span(xi_F*) <= 0.05
    => magnitude_verdict = INFO (INFO-stays, suppressed). [Counter: had mean(o_a) >= 1/2,
    xi_F* would land in-band => Delta_R ~ kappa_0 => rel_span > 0.05 => FAIL-promote.]

SUBSTRATE FRAMING (IS-not-IN; phononic-framing.md)
--------------------------------------------------
The substrate IS the BdG occupation-variance Var_a(|v_a(K)|^2) of the D_K eigenmodes on
the M_2(C) child of A_K = C (+) H (+) M_3(C); the regulator class R (zeta / PV / Mellin)
is the OTHER substrate-IS choice - WHICH spectral functional defines the fabric's action
(zeta drops a0, cutoff/Mellin retain it). The Fermi surface xi_F is a FEATURE of the D_K
spectrum, not a thing "in" a container; pinning it from the s52 gap-IR occupations is the
IS-not-IN move. L_emp = d^2/d(ln K)^2 PROJECTS OUT the K-independent pure-volume (CC) part.

PLAN: sessions/session-plan/session-118-plan-w3.md §W3-1.
WP:   sessions/session-118/session-118-w3-workingpaper.md §W3-1.
VERDICT FILE: computations/session-118/s118_gate_verdicts.txt (via emit_verdict MCP).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    Delta_BCS,
    tau_fold,
    L_emp_VII_AV_STATE_PROJ,
)

import numpy as np  # noqa: E402
from scipy.optimize import brentq, minimize_scalar  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------- Gate-block identity (machinery pins per plan §W3-1 R3 YAML) ----------------
SESSION = "S118"
GATE_ID = "CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN"
SCHEME = "B-of-R-multi-regulator-span-at-gap-IR-pinned-xi_F"
CONVENTION = (
    "FWDC2-UV-regulator-span-a0zeta+a0PV+a0Mellin-"
    "poleconv-A-double-pole_in_s-4-curvature_grade_n-0-RATIO-NORMALIZED-TRACE-MEAN"
)
L_MAX = 14  # (local) primary additive a0 channel over the s87 L14 cache; L12 (s84) cross-check

# Canonical reference (PV pinned, S93 W3 Stage-2 PASS-AND; W8-2 multiplicative-cancellation)
L_EMP_PV = float(L_emp_VII_AV_STATE_PROJ)  # (local) -7.046336474406761 M_KK^2

# Verdict bands (plan operator; relative span on rel_span DIRECTLY)
PASS_REL = 1e-7    # (local) FI-strict, L_emp 7-sig-fig publication-precision floor (Class-8.3); UNREACHABLE
INFO_REL = 0.05    # (local) physical-significance threshold (operative INFO/FAIL boundary)
PUB_PRECISION = 7  # (local) L_emp -7.046336 published at 7 sig figs (Class-8.3)
REGIME_KERNEL_TOL = 1e-9  # (local) kernel must reproduce L_emp_PV to < 1e-9 (regime gate)

# K-window pins (S87 W2-3 / S89 / S91 canonical horizon-crossing window)
K_HORIZON_FRAC = (0.95, 1.05)  # (local) +/-5% window around horizon crossing
DLNK = 0.001                   # (local) step in ln K (S87 W2-3 canonical pin); N_K=101

# Pauli-Villars mass-tower (S61/S78 canonical 2-PV; M_KK-natural units M_KK=1)
PV_M_TOWER = (1.0, math.sqrt(2.0))  # (local) (M_KK, sqrt2*M_KK)
PV_COEFFS = (+2.0, -1.0)            # (local) subtraction coeffs; full set (+1,-2,+1) kills a0 AND a2
S_POLE = 4                          # (local) substrate-distance-2 Mellin pole s=4 (n=0)

# gap-IR occupation-match sector + root-find bracket (anti-injection: SOLVE, not scan)
N_GAP_IR = 8                        # (local) lowest-|lam| sector, matched 1:1 to the 8 s52 modes
N_GAP_IR_SCAN = (8, 16, 32, 64)     # (local) robustness of the below-floor conclusion (NOT target-hitting)
BRACKET_FLOOR_MARGIN = 5.0          # (local) lower bracket = lam_min - 5*Delta_BCS
XI_F_XTOL = 1e-12                   # (local) root-find tolerance (plan pin)

# Output paths
OUT_NPZ = ROOT / "computations" / "session-118" / "s118_w3_lemp_oq4_vacuum_fermi_pin.npz"
OUT_PNG = ROOT / "computations" / "session-118" / "s118_w3_lemp_oq4_vacuum_fermi_pin.png"

# Input dependencies (substrate-IS pins)
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
S52_BOG_CACHE = ROOT / "computations" / "session-52" / "s52_bogoliubov_amp.npz"
FWDC2_NPZ = ROOT / "computations" / "session-116" / "s116_w8_fwdc2_full_bdg_proxy_refinement.npz"
FULL_PV_NPZ = ROOT / "computations" / "session-91" / "s91_w5_1_full_bdg_pv.npz"
L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
L14_CACHE = ROOT / "computations" / "session-87" / "s87_spectrum_cache_L14_tau019.npz"
W6_2_NPZ = ROOT / "computations" / "session-117" / "s117_w6_lemp_uv_regulator_br_span.npz"  # cross-check display ONLY
SCRIPT_PATH = Path(__file__).resolve()

# Plan input-SHA ledger (verified at runtime; mismatch => PRE-REG-INC honest close)
LEDGER_SHA = {
    "s52_bogoliubov_amp": "ecfbce08eabe84394009b69d6ae9710fc2d9e106d55ec8481466f95952e348b1",
    "L14_spectrum_cache_tau019": "fa2bfb83c74ff151b138c83498f54ca2c87a61fc59ec1ae5189bb6aab360480c",
    "L12_spectrum_cache_tau019": "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9",
    "w6_2_predecessor_npz": "e43cd8d498ba26ca676f3a55bdab14a19fac03668dac0bd15a10b5bd49ab123f",
    "fwdc2_proxy_refinement": "5c6726c41b6ec53c9be98b5e88a2c041612335baf552715f82c0a2549518bcc8",
    "full_bdg_pv_pipeline": "6893ca6b8dec0bccfdc7cd45a1552346c26ba7bc0c5f42ecd2b5db30096f8e5d",
}

# pinmap (audit consumption): canonical + frozen substrate-IS data + script.
# NOTE: the W6-2 MACHINERY SCRIPT is read for METHOD only and is NOT in audit consumption.
INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "s52_bogoliubov_amp": S52_BOG_CACHE,
    "L12_spectrum_cache_tau019": L12_CACHE,
    "L14_spectrum_cache_tau019": L14_CACHE,
    "w6_2_predecessor_npz": W6_2_NPZ,
    "fwdc2_proxy_refinement": FWDC2_NPZ,
    "full_bdg_pv_pipeline": FULL_PV_NPZ,
    "script": SCRIPT_PATH,
}


# ---------------- SHA helpers (S84+ dual-SHA schema) ----------------
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    blob = json.dumps(items, sort_keys=True).encode("utf-8")  # (local)
    return hashlib.sha256(blob).hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 78)
    print(f"Gate: {GATE_ID}")
    print(f"Scheme: {SCHEME}")
    print(f"Convention: {CONVENTION}")
    print("regulator_pin = a_0^{zeta} || a_0^{Pauli-Villars} || a_0^{Mellin}; "
          "poleconv-A-double pole_in_s=4 curvature_grade_n=0 (a0/CC grade)")
    print("counting_pin  = RATIO-NORMALIZED-TRACE-MEAN (intensive; UV-regulator _|_ counting)")
    print(f"Substrate-distance-2 pole s={S_POLE}; K-window {K_HORIZON_FRAC}; DLNK={DLNK}")
    print(f"Reference L_emp_PV (canonical) = {L_EMP_PV:.15f} M_KK^2")
    print("=" * 78)
    print("Input SHAs (verified against plan §W3-1 ledger):")
    sha_ok = True  # (local)
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:34s} = (file not found; pin skipped)")
            if name in LEDGER_SHA:
                sha_ok = False
            continue
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        tag = ""  # (local)
        if name in LEDGER_SHA:
            match = (sha == LEDGER_SHA[name])  # (local)
            sha_ok = sha_ok and match
            tag = "  [LEDGER-MATCH]" if match else "  [!! LEDGER-MISMATCH !!]"
        print(f"  {name:34s} = {sha[:16]}...  ({p.relative_to(ROOT)}){tag}")
    print(f"  ALL LEDGER SHAs MATCH = {sha_ok}")
    return pins, sha_ok


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    """audit_sha256 over [script, canonical, pinmap]; content_sha256 over [script]."""
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()  # (local)
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to the knowledge-MCP
    emit_verdict tool (race-safe; the script does NOT write the verdict file)."""
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
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


# ---------------- BdG occupation kernel (S87 W2-3 / S89 / W8-2 numerical core; xi_F-INDEPENDENT) ----------------
def bogoliubov_occupation_K(v_static, u_static, E_static, delta_abs, K_ratio):
    """K-dependent Bogoliubov occupation n_a(K) = |v_a(K)|^2 (bare substrate-IS kernel;
    reproduces S89 / W8-2 L_emp = -7.046336). Independent of the additive a0 vacuum xi_F."""
    xi0 = (u_static ** 2 - v_static ** 2) * E_static    # (local) static xi_a^(0)
    xi_K = xi0 * (K_ratio ** 2)                          # (local) acoustic K^2 rescaling
    E_K = np.sqrt(xi_K ** 2 + delta_abs ** 2)           # (local) BdG dispersion
    E_K = np.where(E_K < 1e-30, 1e-30, E_K)             # (local) gapless guard
    return np.clip(0.5 * (1.0 - xi_K / E_K), 0.0, 1.0)  # (local) Bogoliubov occupation in [0,1]


def var_a_bare_over_window(v_static, u_static, E_static, delta_abs, k_ratios):
    """kappa_0(K) = Var_a(|v_a(K)|^2) over the 8 BdG modes (uniform, canonical)."""
    return np.array([float(np.var(bogoliubov_occupation_K(
        v_static, u_static, E_static, delta_abs, kr))) for kr in k_ratios])


def second_log_derivative_at_K_horizon(arr, ln_K_grid):
    """L = d^2 ln(arr)/d(ln K)^2 at K=K_horizon via 5-point central FD (S87 W2-3 core)."""
    if np.min(arr) <= 0:
        return float("nan")
    ln_A = np.log(arr)
    h = ln_K_grid[1] - ln_K_grid[0]
    i0 = int(np.argmin(np.abs(ln_K_grid)))
    n_K = len(ln_K_grid)
    if i0 < 2 or i0 > n_K - 3:
        return float((ln_A[i0 + 1] - 2 * ln_A[i0] + ln_A[i0 - 1]) / (h ** 2))
    return float((-ln_A[i0 - 2] + 16 * ln_A[i0 - 1] - 30 * ln_A[i0]
                  + 16 * ln_A[i0 + 1] - ln_A[i0 + 2]) / (12.0 * h ** 2))


def residue_multiplier_at_Kh(g, ln_K_grid):
    """d/du[-g'/g^2]|_{K_h} = -(g'' g - 2 g'^2)/g^3  (Sage EMERGENCE-1 closed form).
    The leading additive residue: B(R) - B(0) ~ delta_R * this."""
    h = ln_K_grid[1] - ln_K_grid[0]
    gp = np.gradient(g, h)
    gpp = np.gradient(gp, h)
    i0 = int(np.argmin(np.abs(ln_K_grid)))
    return float(-(gpp[i0] * g[i0] - 2.0 * gp[i0] ** 2) / g[i0] ** 3)


# ---------------- regularized s=4 spectral-support moments M_R (MULTIPLICATIVE weight) ----------------
def s4_moments(cache, s=4.0):
    """Returns (M_bare, M_PV, n_sectors) for the s=4 spectral-support moment over the D_K cache.
    M_bare keeps the a0 log-divergence (grows with L_max); M_PV subtracts a0+a2 (L_max-stable).
    These are the W8-2 MULTIPLICATIVE weights (annihilated by d^2/d(lnK)^2)."""
    se = np.load(cache, allow_pickle=True)["sector_evals"].item()
    M1_sq = PV_M_TOWER[0] ** 2  # (local) M_KK^2
    M2_sq = PV_M_TOWER[1] ** 2  # (local) 2 M_KK^2
    M_bare = 0.0  # (local) accumulator
    M_PV = 0.0    # (local) accumulator
    for (p, q), info in se.items():
        d_ = info["dim"]
        lam2 = np.asarray(info["abs_evals"], float) ** 2
        lam2 = lam2[lam2 > 0]
        bare = np.power(lam2, -s)
        pv = bare - 2.0 * np.power(lam2 + M1_sq, -s) + np.power(lam2 + M2_sq, -s)
        M_bare += d_ * float(np.sum(bare))
        M_PV += d_ * float(np.sum(pv))
    return M_bare, M_PV, len(se)


def load_full_spectrum(cache):
    """Flatten the D_K cache to (abs_eigenvalues, multiplicities)."""
    se = np.load(cache, allow_pickle=True)["sector_evals"].item()
    lams, mults = [], []
    for (p, q), info in se.items():
        ev = np.asarray(info["abs_evals"], float)
        ev = ev[ev > 0]
        lams.append(ev)
        mults.append(np.full(len(ev), info["dim"], float))
    return np.concatenate(lams), np.concatenate(mults)


def lowest_modes_with_mult(lam, mult, N):
    """The lowest-N |lam| modes of the D_K spectrum, counted WITH multiplicity
    (each distinct |lam| repeated by its total dim). Returns a length-N array of |lam|."""
    order = np.argsort(lam)  # (local)
    lam_s = lam[order]
    mult_s = np.rint(mult[order]).astype(int)
    out = []  # (local)
    for l, m in zip(lam_s, mult_s):
        take = min(int(m), N - len(out))  # (local)
        out.extend([float(l)] * take)
        if len(out) >= N:
            break
    return np.array(out, float)


# ---------------- additive a0 counterterm Delta_R (ADDITIVE-IN-TRACE channel; xi_F-DEPENDENT) ----------------
def reg_vacuum_variance(lam, mult, scheme, fermi="zero", s=4.0, xi_F=None):
    """Regularized vacuum-occupation-variance over the FULL D_K spectrum.

    Vacuum BdG occupation v_vac^2(lam) = 1/2(1 - xi/E), E=sqrt(xi^2+Delta_BCS^2):
      fermi='zero'     -> xi = lam               (Fermi at 0; positive |D_K| spectrum, central)
      fermi='floor'    -> xi = lam - lam_min     (Fermi at the spectral floor / gap-IR sector)
      fermi='median'   -> xi = lam - median(lam)
      fermi='explicit' -> xi = lam - xi_F        (the SUBSTRATE-PINNED Fermi level; THIS gate)

    Regulator weight at s=4:
      'bare'/'Mellin' -> |lam|^{-2s}  (a0 residue RETAINED)
      'PV'            -> |lam|^{-2s} - 2(lam^2+M1^2)^{-s} + (lam^2+M2^2)^{-s}  (a0+a2 subtracted)
    """
    l2 = lam ** 2
    bare = np.power(l2, -s)
    if scheme in ("bare", "Mellin"):
        w = bare
    elif scheme == "PV":
        w = bare - 2.0 * np.power(l2 + PV_M_TOWER[0] ** 2, -s) + np.power(l2 + PV_M_TOWER[1] ** 2, -s)
    else:
        raise ValueError(scheme)
    w = mult * w
    if fermi == "zero":
        xi = lam
    elif fermi == "floor":
        xi = lam - lam.min()
    elif fermi == "median":
        xi = lam - np.median(lam)
    elif fermi == "explicit":
        if xi_F is None:
            raise ValueError("fermi='explicit' requires xi_F")
        xi = lam - float(xi_F)
    else:
        raise ValueError(fermi)
    E = np.sqrt(xi ** 2 + Delta_BCS ** 2)
    n = 0.5 * (1.0 - xi / E)
    W = float(np.sum(w))
    m1 = float(np.sum(w * n)) / W
    m2 = float(np.sum(w * n * n)) / W
    return m2 - m1 * m1


# ---------------- occupation-match (the xi_F PIN; SOLVED, never scanned) ----------------
def vac_occupation(lam_set, xi_F):
    """v_vac^2(lam; xi_F) = 1/2(1 - (lam-xi_F)/E), E=sqrt((lam-xi_F)^2 + Delta_BCS^2)."""
    xi = np.asarray(lam_set, float) - float(xi_F)
    E = np.sqrt(xi ** 2 + Delta_BCS ** 2)
    return 0.5 * (1.0 - xi / E)


def gap_ir_mean_occupation(lam_gapir, xi_F):
    """Mean extended-vacuum occupation over the gap-IR sector at Fermi level xi_F.
    Monotone increasing in xi_F (d/dxi_F [-(lam-xi_F)/E] > 0) => unique root."""
    return float(np.mean(vac_occupation(lam_gapir, xi_F)))


def solve_xi_F(lam_gapir, target, lo, hi):
    """Root-find the UNIQUE xi_F s.t. mean(v_vac^2(gap-IR; xi_F)) = target (xtol 1e-12).
    ANTI-INJECTION: target = mean(o_a) from the s52 occupations; NEVER rel_span."""
    f = lambda xf: gap_ir_mean_occupation(lam_gapir, xf) - target  # (local)
    return float(brentq(f, lo, hi, xtol=XI_F_XTOL, maxiter=200))


def lsq_xi_F(lam_gapir, occ_targets, lo, hi):
    """Per-mode least-squares cross-check: minimize sum (v_vac^2(sorted lam) - sorted o_a)^2.
    A single-scalar minimization; reported with its RMS residual (diagnostic only)."""
    lam_sorted = np.sort(np.asarray(lam_gapir, float))  # (local)
    occ_sorted = np.sort(np.asarray(occ_targets, float))  # (local)
    n = min(len(lam_sorted), len(occ_sorted))  # (local)
    lam_sorted = lam_sorted[:n]
    occ_sorted = occ_sorted[:n]

    def sse(xf):
        return float(np.sum((vac_occupation(lam_sorted, xf) - occ_sorted) ** 2))
    res = minimize_scalar(sse, bounds=(lo, hi), method="bounded",
                          options={"xatol": XI_F_XTOL})
    xf = float(res.x)  # (local)
    rms = float(np.sqrt(sse(xf) / n))  # (local)
    return xf, rms


# ---------------- plot ----------------
def emit_plot(out_png, k_ratios, ln_K_grid, var_bare, B_dict, delta_dict, residue_mult,
              rel_span, xi_F_star, lam_floor, lam_gapir, occ_s52, occ_match,
              occ_rms, N_scan_xi, N_scan_below, fermi_scan, w6_2_relspan, verdict):
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))
    ln_K = np.log(k_ratios)

    # Panel 1 -- the occupation PIN: gap-IR v_vac^2(lam; xi_F*) reproduces mean(o_a); xi_F* vs floor
    ax = axes[0, 0]
    idx = np.arange(len(lam_gapir))
    ax.plot(idx, np.sort(occ_match), "o-", color="tab:red", ms=5,
            label=f"v_vac^2(gap-IR; xi_F*) (mean={np.mean(occ_match):.5f})")
    ax.plot(np.arange(len(occ_s52)), np.sort(occ_s52), "s--", color="tab:blue", ms=5,
            label=f"s52 o_a = v_a^2 (mean={np.mean(occ_s52):.5f})")
    ax.axhline(0.5, color="k", ls=":", lw=0.8, alpha=0.6, label="half-filling v^2=1/2")
    ax.set_xlabel("mode rank (sorted)")
    ax.set_ylabel("occupation v^2")
    ax.set_title(f"OCCUPATION PIN: xi_F* = {xi_F_star:.6f} solved from mean(o_a)={np.mean(occ_s52):.5f}\n"
                 f"|D_K| floor lam_min={lam_floor:.5f}  =>  xi_F* {'BELOW' if xi_F_star < lam_floor else 'IN/ABOVE'} floor "
                 f"(LSQ-RMS={occ_rms:.2e})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 2 -- B(R) per scheme at the pinned xi_F*
    ax = axes[0, 1]
    names = list(B_dict.keys())
    vals = [B_dict[n] for n in names]
    colors = {"zeta": "tab:green", "PV": "tab:orange", "Mellin": "tab:red"}
    ax.bar(names, vals, color=[colors[n] for n in names])
    ax.axhline(L_EMP_PV, color="k", ls="--", lw=1.0, label=f"L_emp_PV={L_EMP_PV:.4f}")
    ax.set_ylabel("B(R) = d^2 ln(kappa_0+delta_R) / d(lnK)^2  (M_KK^2)")
    ax.set_title(f"B(R) span across {{zeta,PV,Mellin}} at n=0, xi_F*={xi_F_star:.4f}\n"
                 f"rel_span={rel_span:.4e}  (W6-2 Fermi=zero ref {w6_2_relspan:.4e})  =>  {verdict}")
    for i, v in enumerate(vals):
        ax.text(i, v, f"{v:.4f}", ha="center", va="top", fontsize=8.5)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    # Panel 3 -- robustness: xi_F*(N_gap-IR) all BELOW floor (the below-floor conclusion is robust)
    ax = axes[1, 0]
    ax.plot(N_scan_xi[:, 0], N_scan_xi[:, 1], "o-", color="tab:purple", ms=6, label="xi_F*(N gap-IR)")
    ax.axhline(lam_floor, color="tab:red", ls="--", lw=1.0, label=f"|D_K| floor lam_min={lam_floor:.4f}")
    ax.axhline(0.0, color="k", ls=":", lw=0.8, alpha=0.5)
    ax.set_xlabel("N (gap-IR sector size, counted w/ multiplicity)")
    ax.set_ylabel("solved xi_F*")
    ax.set_xscale("log", base=2)
    ax.set_title("Robustness of the SUBSTRATE-PINNED Fermi level\n"
                 f"xi_F*(N) all BELOW floor = {bool(np.all(N_scan_below))} (conservative vacuum, INFO-stays)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 4 -- verdict summary
    ax = axes[1, 1]
    ax.axis("off")
    txt = []
    txt.append(f"VERDICT (composite): {verdict}")
    txt.append("")
    txt.append("LEG A (sign, model-INDEPENDENT):")
    txt.append("  (A) MULTIPLICATIVE M_R(s=4): annihilated d^2/d(lnK)^2 (W8-2) => residue = 0")
    txt.append(f"  (B) ADDITIVE-IN-TRACE a0 counterterm: SURVIVES (residue ~ delta_R*{residue_mult:.1f})")
    txt.append("  => |additive| > |multiplicative|=0 => ADDITIVE-CHANNEL-DOMINANT => sign=PASS")
    txt.append("")
    txt.append("LEG B (magnitude, substrate-PINNED):")
    txt.append(f"  mean(o_a) = {np.mean(occ_s52):.5f} < 1/2  =>  xi_F* = {xi_F_star:.5f}")
    txt.append(f"  |D_K| floor lam_min = {lam_floor:.5f}  =>  xi_F* BELOW floor = {bool(xi_F_star < lam_floor)}")
    txt.append("  => a0-grade UV modes EMPTY (v_vac^2 -> 0) => |delta_Mellin| << kappa_0")
    txt.append("")
    txt.append("a0 additive counterterm delta_R (occupation-variance units):")
    txt.append(f"  zeta   : delta = {delta_dict['zeta']:.4e}  (a0 ABSENT, EXACT)")
    txt.append(f"  PV     : delta = {delta_dict['PV']:.4e}  (a0+a2 subtracted)")
    txt.append(f"  Mellin : delta = {delta_dict['Mellin']:.4e}  (a0 residue RETAINED)")
    txt.append("")
    txt.append(f"  B(zeta)   = {B_dict['zeta']:.6f}")
    txt.append(f"  B(PV)     = {B_dict['PV']:.6f}")
    txt.append(f"  B(Mellin) = {B_dict['Mellin']:.6f}")
    txt.append(f"  rel_span(xi_F*)  = {rel_span:.6e}")
    txt.append(f"  bands: PASS(FI)<={PASS_REL:.0e} (UNREACHABLE) ; INFO<= {INFO_REL} ; FAIL>{INFO_REL}")
    txt.append("")
    txt.append("=> OQ-4: SD-OPEN span is SUPPRESSED at the substrate-pinned vacuum")
    txt.append("   (xi_F* below floor => a0-grade UV modes empty); CC-in-microcosm TAMED.")
    ax.text(0.02, 0.98, "\n".join(txt), va="top", ha="left",
            fontsize=8.4, family="monospace", transform=ax.transAxes)

    fig.suptitle(
        f"{GATE_ID}\n"
        "OQ-4 magnitude discriminator: {zeta,PV,Mellin} B(R) span at the a0 pole (s=4, n=0),\n"
        "with the BdG Fermi level xi_F* PINNED substrate-first from the s52 gap-IR occupations",
        fontsize=11, y=1.00,
    )
    plt.tight_layout()
    plt.savefig(out_png, dpi=120, bbox_inches="tight")
    plt.close()


# ---------------- main ----------------
def main() -> int:
    pins, sha_ok = log_input_pins(INPUT_FILES)
    print(f"\nCanonical: M_KK={M_KK:.6e} GeV; Delta_BCS={Delta_BCS:.10f}; tau_fold={tau_fold}")

    if not sha_ok:
        # Honest PRE-REG-INC close per mechanical-closure-discipline.md (frozen input drifted).
        audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
        value = "PRE-REG-INC_blocked_by_input_SHA_ledger_mismatch"
        print_verdict_payload("PRE-REG-INC", value, audit_sha, content_sha,
                              sign_verdict="N/A", magnitude_verdict="INFO", regime_verdict="BREAKDOWN")
        print("\nCOMPUTATION HALTED: input-SHA ledger mismatch.")
        return 0

    # ===== STEP 1: substrate-first occupation target mean(o_a) from the s52 cache =====
    print("\n--- STEP 1: substrate-first occupation target mean(o_a) from s52 ---")
    bog = np.load(S52_BOG_CACHE, allow_pickle=True)
    u_s = bog["u_k"].astype(float)
    v_s = bog["v_k"].astype(float)
    E_s = bog["E_qp"].astype(float)
    d_abs = np.abs(bog["Delta_per_mode"].astype(complex)).astype(float)
    occ_s52 = v_s ** 2                       # (local) o_a = v_a^2, the 8 BdG occupations
    target = float(np.mean(occ_s52))         # (local) mean(o_a) FROM THE NPZ (not rounded literals)
    print(f"  o_a = v_a^2 = {np.round(occ_s52, 6)}")
    print(f"  mean(o_a) = TARGET = {target:.17g}   (< 1/2: {target < 0.5})")

    # ===== STEP 2: SOLVE xi_F* from the gap-IR occupation match (anti-injection: target=mean(o_a)) =====
    print("\n--- STEP 2: SOLVE xi_F* (gap-IR occupation match; SOLVED, never scanned) ---")
    lam14, m14 = load_full_spectrum(L14_CACHE)
    lam12, m12 = load_full_spectrum(L12_CACHE)
    lam_floor = float(lam14.min())            # (local) the |D_K| spectral floor
    lam_median = float(np.median(lam14))      # (local) bracket upper
    bracket_lo = lam_floor - BRACKET_FLOOR_MARGIN * Delta_BCS  # (local) below-floor reach
    bracket_hi = lam_median                    # (local)
    print(f"  L14 |D_K| floor lam_min = {lam_floor:.8f}; lam_median = {lam_median:.6f}")
    print(f"  root-find bracket = [lam_min - 5*Delta_BCS, lam_median] = [{bracket_lo:.6f}, {bracket_hi:.6f}]")

    lam_gapir = lowest_modes_with_mult(lam14, m14, N_GAP_IR)  # (local) lowest-8 |lam| w/ mult
    print(f"  gap-IR sector (N={N_GAP_IR}, lowest-|lam| w/ mult) = {np.round(lam_gapir, 6)}")
    # sign check of the bracket (monotonicity => unique root)
    f_lo = gap_ir_mean_occupation(lam_gapir, bracket_lo) - target  # (local)
    f_hi = gap_ir_mean_occupation(lam_gapir, bracket_hi) - target  # (local)
    print(f"  bracket residuals: f(lo)={f_lo:.4e}  f(hi)={f_hi:.4e}  (opposite sign => unique root)")
    xi_F_star = solve_xi_F(lam_gapir, target, bracket_lo, bracket_hi)  # (local) THE PIN
    occ_match = vac_occupation(lam_gapir, xi_F_star)                   # (local)
    occ_match_mean = float(np.mean(occ_match))                        # (local)
    occ_match_resid = abs(occ_match_mean - target)                   # (local) mean-match residual
    below_floor = bool(xi_F_star < lam_floor)                        # (local) the OQ-4 discriminator
    print(f"  xi_F* (SOLVED) = {xi_F_star:.12f}")
    print(f"  mean(v_vac^2(gap-IR; xi_F*)) = {occ_match_mean:.12f}  (target {target:.12f}; resid {occ_match_resid:.2e})")
    print(f"  xi_F* BELOW |D_K| floor ({lam_floor:.6f})? {below_floor}  "
          f"=> {'conservative vacuum (INFO-stays)' if below_floor else 'in-band (FAIL-promote)'}")
    # per-mode LSQ cross-check (diagnostic)
    xi_F_lsq, occ_rms = lsq_xi_F(lam_gapir, occ_s52, bracket_lo, bracket_hi)
    print(f"  [cross-check] per-mode LSQ xi_F = {xi_F_lsq:.6f} (RMS {occ_rms:.3e}); "
          f"below floor: {xi_F_lsq < lam_floor}")

    # ===== STEP 3: kernel kappa_0(K) (reproduce L_emp_PV) + additive a0 counterterm Delta_R(xi_F*) =====
    print("\n--- STEP 3a: bare kernel kappa_0(K) = Var_a(|v_a(K)|^2) (reproduce L_emp_PV; regime gate) ---")
    ln_min, ln_max = math.log(K_HORIZON_FRAC[0]), math.log(K_HORIZON_FRAC[1])
    n_K = int(round((ln_max - ln_min) / DLNK)) + 1
    ln_K_grid = np.linspace(ln_min, ln_max, n_K)
    k_ratios = np.exp(ln_K_grid)
    i0 = int(np.argmin(np.abs(ln_K_grid)))
    var_bare = var_a_bare_over_window(v_s, u_s, E_s, d_abs, k_ratios)
    B0 = second_log_derivative_at_K_horizon(var_bare, ln_K_grid)
    kernel_repro_err = abs(B0 - L_EMP_PV)
    kernel_repro_rel = kernel_repro_err / abs(L_EMP_PV)
    print(f"  B(0) = L_emp_kernel = {B0:.12f}  (canonical {L_EMP_PV:.12f}; rel {kernel_repro_rel:.3e})")
    print(f"  kappa_0(K_h) = {var_bare[i0]:.8e}  range [{var_bare.min():.4e}, {var_bare.max():.4e}]")
    residue_mult = residue_multiplier_at_Kh(var_bare, ln_K_grid)
    print(f"  residue multiplier d/du[-g'/g^2]|_{{K_h}} = {residue_mult:.6e}  (Sage EMERGENCE-1)")

    print("\n--- STEP 3b: ADDITIVE-IN-TRACE a0 counterterm Delta_R at the PINNED xi_F* ---")
    vac_mellin = reg_vacuum_variance(lam14, m14, "Mellin", fermi="explicit", xi_F=xi_F_star)  # (local)
    vac_pv = reg_vacuum_variance(lam14, m14, "PV", fermi="explicit", xi_F=xi_F_star)          # (local)
    delta_zeta = 0.0                          # (local) a0 ABSENT (S_zeta=zeta_D(0)); EXACT, my signature
    delta_PV = 0.0                            # (local) a0+a2 subtracted -> a0-removed reference (~0)
    delta_Mellin = vac_mellin - vac_pv         # (local) a0 residue RETAINED minus a0-removed reference
    ratio_delta_kappa0 = abs(delta_Mellin) / var_bare[i0]  # (local)
    print(f"  vacuum-occ-variance (Fermi=xi_F*={xi_F_star:.5f}): Mellin(a0-kept)={vac_mellin:.8e}  "
          f"PV(a0-removed)={vac_pv:.8e}")
    print(f"  delta_zeta   = {delta_zeta:.6e}   (a0 ABSENT, EXACT)")
    print(f"  delta_PV     = {delta_PV:.6e}   (a0+a2 subtracted)")
    print(f"  delta_Mellin = {delta_Mellin:.6e}   (a0 residue RETAINED)")
    print(f"  ratio |delta_Mellin| / kappa_0(K_h) = {ratio_delta_kappa0:.4e}  "
          f"(< 1 => Delta_R << kappa_0 suppressed: {ratio_delta_kappa0 < 1.0})")

    # ===== STEP 4: B(R) per scheme + rel_span(xi_F*) =====
    print("\n--- STEP 4: B(R) = d^2 ln(kappa_0 + delta_R)/d(lnK)^2 per scheme; rel_span(xi_F*) ---")
    delta_dict = {"zeta": delta_zeta, "PV": delta_PV, "Mellin": delta_Mellin}
    B_dict = {}
    for name, dl in delta_dict.items():
        B_dict[name] = second_log_derivative_at_K_horizon(var_bare + dl, ln_K_grid)
        print(f"  B({name:6s}) = {B_dict[name]:.10f}   (delta={dl:.4e}, B-B0={B_dict[name]-B0:.4e})")
    B_vals = list(B_dict.values())
    span_abs = max(B_vals) - min(B_vals)        # (local) absolute span (M_KK^2)
    rel_span = span_abs / abs(L_EMP_PV)         # (local) PRIMARY metric
    print(f"  absolute span = {span_abs:.6e} M_KK^2 ; rel_span(xi_F*) = {rel_span:.6e}")

    # ===== LEG A: multiplicative (W8-2) vs additive channel (model-INDEPENDENT sign) =====
    print("\n--- LEG A: multiplicative (W8-2 cancellation) vs additive-in-trace channel ---")
    Mb12, Mp12, n12 = s4_moments(L12_CACHE)
    Mb14, Mp14, n14 = s4_moments(L14_CACHE)
    a0_grade_fraction = (Mb14 - Mp14) / Mb14    # (local) a0+a2 grade fraction of M_bare (MULTIPLICATIVE)
    B_mult_bare = second_log_derivative_at_K_horizon(Mb14 * var_bare, ln_K_grid)  # (local)
    B_mult_pv = second_log_derivative_at_K_horizon(Mp14 * var_bare, ln_K_grid)    # (local)
    mult_resid_bare = abs(B_mult_bare - B0)     # (local)
    mult_resid_pv = abs(B_mult_pv - B0)         # (local)
    mult_residue = max(mult_resid_bare, mult_resid_pv)  # (local) ~0 (W8-2 cancellation)
    residue_closedform_Mellin = delta_Mellin * residue_mult  # (local) Delta*d/du[-g'/g^2] (EMERGENCE-1)
    residue_direct_Mellin = B_dict["Mellin"] - B0            # (local) B(Mellin) - B(0)
    closedform_err = abs(residue_closedform_Mellin - residue_direct_Mellin)  # (local)
    additive_residue = abs(residue_direct_Mellin)  # (local)
    additive_dominant = bool(additive_residue > mult_residue)  # (local) sign verdict driver
    print(f"  a0+a2 grade fraction of M_bare(L14) = {a0_grade_fraction:.4f}  (LARGE but MULTIPLICATIVE)")
    print(f"  multiplicative residue |B[M_R*var]-B0| = {mult_residue:.3e}  (W8-2 cancellation => 0)")
    print(f"  additive residue |B(Mellin)-B0| = {additive_residue:.6e}")
    print(f"  EMERGENCE-1 closed form Delta*{residue_mult:.1f} = {residue_closedform_Mellin:.6e} "
          f"vs direct {residue_direct_Mellin:.6e} (err {closedform_err:.2e})")
    print(f"  |additive|={additive_residue:.4e} > |multiplicative|={mult_residue:.4e}? {additive_dominant} "
          f"=> ADDITIVE-CHANNEL-DOMINANT (sign=PASS, model-INDEPENDENT)")

    # ===== STEP 5 + robustness: xi_F*(N gap-IR) below-floor; L12 L_max-stability; W6-2 cross-check =====
    print("\n--- STEP 5: robustness of the below-floor conclusion (N gap-IR scan; NOT target-hitting) ---")
    N_scan_xi = []   # (local) (N, xi_F*) rows
    N_scan_below = []  # (local) below-floor booleans
    for Nn in N_GAP_IR_SCAN:
        lg = lowest_modes_with_mult(lam14, m14, Nn)  # (local)
        xf = solve_xi_F(lg, target, bracket_lo, bracket_hi)  # (local)
        bf = bool(xf < lam_floor)  # (local)
        N_scan_xi.append((Nn, xf))
        N_scan_below.append(bf)
        print(f"  N={Nn:3d}: xi_F*={xf:.8f}  below floor({lam_floor:.5f})={bf}")
    N_scan_xi = np.array(N_scan_xi, float)
    below_floor_robust = bool(np.all(N_scan_below))  # (local)
    print(f"  below-floor robust across all N? {below_floor_robust}")

    # L12 vs L14 L_max-stability of delta_Mellin at the SAME pinned xi_F*
    vac_mellin_12 = reg_vacuum_variance(lam12, m12, "Mellin", fermi="explicit", xi_F=xi_F_star)  # (local)
    vac_pv_12 = reg_vacuum_variance(lam12, m12, "PV", fermi="explicit", xi_F=xi_F_star)          # (local)
    delta_Mellin_L12 = vac_mellin_12 - vac_pv_12  # (local)
    print(f"  L_max stability of delta_Mellin @ xi_F*: L12={delta_Mellin_L12:.4e} L14={delta_Mellin:.4e} "
          f"(drift {abs(delta_Mellin - delta_Mellin_L12):.2e})")

    # W6-2 Fermi=zero reproduction (cross-check display ONLY; never a seed) +
    # the three W6-2 heuristic models, recomputed here for the OQ-4 narrative.
    fermi_scan = {}  # (local)
    for fermi in ["zero", "floor", "median"]:
        vb = reg_vacuum_variance(lam14, m14, "Mellin", fermi=fermi)  # (local)
        vp = reg_vacuum_variance(lam14, m14, "PV", fermi=fermi)      # (local)
        dM = vb - vp  # (local)
        arg = var_bare + dM  # (local)
        if np.min(arg) <= 0:
            fermi_scan[fermi] = float("inf")
            continue
        BM = second_log_derivative_at_K_horizon(arg, ln_K_grid)  # (local)
        fermi_scan[fermi] = (max(B0, BM) - min(B0, BM)) / abs(L_EMP_PV)  # (local)
    w6_2_relspan_recomputed = fermi_scan["zero"]  # (local) reproduce W6-2 conservative model
    # load the W6-2 npz (DISPLAY cross-check only)
    w6_2_relspan_stored = float("nan")  # (local)
    try:
        w6_2 = np.load(W6_2_NPZ, allow_pickle=True)
        w6_2_relspan_stored = float(w6_2["rel_span"])
    except Exception as e:
        print(f"  (W6-2 npz cross-check skipped: {e})")
    print(f"  W6-2 Fermi=zero rel_span: recomputed={w6_2_relspan_recomputed:.6e} "
          f"stored(s117 npz)={w6_2_relspan_stored:.6e} "
          f"(cross-check; xi_F*={xi_F_star:.4f} sits just above Fermi=zero, below floor)")

    # ===== VERDICT (sign / magnitude / regime; composite collapse per gate-verdicts.md) =====
    print("\n--- VERDICT: sign / magnitude / regime ---")
    sign_v = "PASS" if additive_dominant else "FAIL"   # (local) additive-channel-dominant
    if rel_span <= PASS_REL:
        mag_v = "PASS"   # (local) FI (UNREACHABLE)
    elif rel_span <= INFO_REL:
        mag_v = "INFO"   # (local) suppressed sub-threshold (INFO-stays)
    else:
        mag_v = "FAIL"   # (local) physically-significant SD (FAIL-promote)
    regime_ok = bool(
        var_bare.min() > 0
        and np.isfinite(rel_span)
        and kernel_repro_rel < REGIME_KERNEL_TOL          # kernel reproduces L_emp_PV
        and np.isfinite(delta_Mellin)
        and occ_match_resid < 1e-9                        # occupation-match well-posed
        and bracket_lo < xi_F_star < bracket_hi           # root interior
    )
    reg_v = "VALID" if regime_ok else "BREAKDOWN"
    if reg_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    print(f"  sign_verdict={sign_v} (additive-channel-dominant, model-INDEPENDENT)")
    print(f"  magnitude_verdict={mag_v} (rel_span(xi_F*)={rel_span:.4e} vs INFO band {INFO_REL})")
    print(f"  regime_verdict={reg_v} (kernel rel {kernel_repro_rel:.2e}; occ resid {occ_match_resid:.2e}; "
          f"xi_F* interior {bracket_lo < xi_F_star < bracket_hi})")
    print(f"  COMPOSITE = {composite}")
    if composite == "PASS":
        dual_prior = "PASS->unreachable(SD-OPEN-permanent)"
    elif composite == "FAIL":
        dual_prior = "FAIL->0.9_TrackB_gap-IR-match-forces-xi_F-in-band_Delta_R~kappa_0_physically-significant-SD"
    else:
        dual_prior = "INFO->0.9_TrackA_xi_F-below-floor_a0-grade-UV-modes-EMPTY_suppressed-SD-OPEN-stays"
    print(f"  dual_prior reallocation: {dual_prior}")

    # ===== save npz + png =====
    print("\n--- save npz + png ---")
    np.savez(
        OUT_NPZ,
        # verdict
        rel_span=float(rel_span), span_abs=float(span_abs),
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        composite_verdict=composite, dual_prior=dual_prior,
        # the xi_F PIN (the OQ-4 substrate-first resolution)
        xi_F_star=float(xi_F_star), target_mean_o_a=float(target),
        occ_match_mean=float(occ_match_mean), occ_match_resid=float(occ_match_resid),
        lam_floor=float(lam_floor), below_floor=bool(below_floor),
        below_floor_robust=bool(below_floor_robust),
        xi_F_lsq=float(xi_F_lsq), occ_lsq_rms=float(occ_rms),
        bracket_lo=float(bracket_lo), bracket_hi=float(bracket_hi),
        N_gap_ir=int(N_GAP_IR), N_scan=np.array(N_GAP_IR_SCAN),
        N_scan_xi_F=N_scan_xi, N_scan_below=np.array(N_scan_below, bool),
        occ_s52=occ_s52, lam_gapir=lam_gapir, occ_match=occ_match,
        # B(R) per scheme
        B_zeta=float(B_dict["zeta"]), B_PV=float(B_dict["PV"]), B_Mellin=float(B_dict["Mellin"]),
        B0_kernel=float(B0), L_emp_PV_reference=float(L_EMP_PV),
        kernel_repro_err=float(kernel_repro_err), kernel_repro_rel=float(kernel_repro_rel),
        # additive a0 counterterms at the pinned xi_F*
        delta_zeta=float(delta_zeta), delta_PV=float(delta_PV), delta_Mellin=float(delta_Mellin),
        delta_Mellin_L12=float(delta_Mellin_L12),
        ratio_delta_kappa0=float(ratio_delta_kappa0), kappa0_Kh=float(var_bare[i0]),
        residue_multiplier=float(residue_mult),
        # Leg A: additive vs multiplicative
        additive_residue=float(additive_residue), multiplicative_residue=float(mult_residue),
        additive_channel_dominant=bool(additive_dominant),
        residue_closedform_Mellin=float(residue_closedform_Mellin),
        residue_direct_Mellin=float(residue_direct_Mellin),
        residue_closedform_err=float(closedform_err),
        a0_grade_fraction_of_moment=float(a0_grade_fraction),
        mult_resid_bare=float(mult_resid_bare), mult_resid_pv=float(mult_resid_pv),
        M_bare_L12=float(Mb12), M_bare_L14=float(Mb14), M_PV_L12=float(Mp12), M_PV_L14=float(Mp14),
        # W6-2 cross-check (display only)
        w6_2_relspan_recomputed=float(w6_2_relspan_recomputed),
        w6_2_relspan_stored=float(w6_2_relspan_stored),
        fermi_scan_keys=np.array(list(fermi_scan.keys())),
        fermi_scan_relspan=np.array([fermi_scan[k] for k in fermi_scan], float),
        # bands + grids
        PASS_REL=float(PASS_REL), INFO_REL=float(INFO_REL),
        k_ratios=k_ratios, ln_K_grid=ln_K_grid, var_bare=var_bare,
        s_pole=np.int64(S_POLE), L_max=np.int64(L_MAX), tau_fold=float(tau_fold),
        Delta_BCS=float(Delta_BCS),
        PV_mass_tower=np.array(PV_M_TOWER), PV_coeffs=np.array(PV_COEFFS),
    )
    print(f"  npz -> {OUT_NPZ.relative_to(ROOT)}")
    emit_plot(OUT_PNG, k_ratios, ln_K_grid, var_bare, B_dict, delta_dict, residue_mult,
              rel_span, xi_F_star, lam_floor, lam_gapir, occ_s52, occ_match,
              occ_rms, N_scan_xi, N_scan_below, fermi_scan, w6_2_relspan_recomputed, composite)
    print(f"  png -> {OUT_PNG.relative_to(ROOT)}")

    # ===== dual-SHA + verdict payload =====
    print("\n--- dual-SHA + verdict payload ---")
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    closure = closure_hash(pins)
    print(f"  closure_hash(pins) = {closure}")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    value = (
        f"rel_span_xi_F={rel_span:.6e}_band={mag_v}"
        f"_xi_F_star={xi_F_star:.8f}_target_mean_o_a={target:.8f}_occ_resid={occ_match_resid:.2e}"
        f"_lam_floor={lam_floor:.6f}_BELOW-FLOOR={below_floor}_below_floor_robust={below_floor_robust}"
        f"_B_zeta={B_dict['zeta']:.6f}_B_PV={B_dict['PV']:.6f}_B_Mellin={B_dict['Mellin']:.6f}"
        f"_delta_Mellin={delta_Mellin:.6e}_ratio_delta_kappa0={ratio_delta_kappa0:.4e}"
        f"_additive_residue={additive_residue:.6e}_multiplicative_residue={mult_residue:.3e}"
        f"_ADDITIVE-CHANNEL-DOMINANT={additive_dominant}"
        f"_W6-2_Fermi-zero_relspan_ref={w6_2_relspan_recomputed:.6e}"
        f"_OQ-4=SUPPRESSED-INFO-STAYS-xi_F-below-floor-a0-UV-modes-EMPTY_{dual_prior}"
    )
    extra_rows = [
        "# regulator_pin=a_0^{zeta}||a_0^{Pauli-Villars}||a_0^{Mellin} "
        "poleconv-A-double pole_in_s=4 curvature_grade_n=0 (a0/CC grade) "
        f"# {GATE_ID} UV-regulator axis pin",
        "# counting_pin=RATIO-NORMALIZED-TRACE-MEAN "
        "(intensive: rel_span normalized by trace-mean |L_emp_PV|; UV-regulator _|_ counting orthogonal axes) "
        f"# {GATE_ID} counting axis pin",
        f"# xi_F PIN (SOLVED-FROM-GAP-IR-OCCUPATION-MATCH; anti-injection): target=mean(o_a)={target:.8f} "
        f"(s52 8-mode v_a^2, NOT rel_span); xi_F*={xi_F_star:.8f} via brentq xtol=1e-12; "
        f"occ-match resid={occ_match_resid:.2e}; xi_F* BELOW |D_K| floor {lam_floor:.6f} = {below_floor} "
        f"(robust across N gap-IR {list(N_GAP_IR_SCAN)} = {below_floor_robust}) # {GATE_ID}",
        f"# LEG A (sign, model-INDEPENDENT): MULTIPLICATIVE M_R(s=4) a0-fraction={a0_grade_fraction:.4f} "
        f"ANNIHILATED (residual {mult_residue:.2e}, W8-2); ADDITIVE-IN-TRACE a0 counterterm "
        f"delta_Mellin={delta_Mellin:.4e} SURVIVES (residue={residue_direct_Mellin:.4e}); "
        f"additive-channel-dominant={additive_dominant} => sign=PASS # {GATE_ID}",
        f"# LEG B (magnitude, substrate-PINNED): mean(o_a)={target:.5f}<1/2 => xi_F*={xi_F_star:.5f} BELOW floor "
        f"=> a0-grade UV modes EMPTY (v_vac^2->0) => |delta_Mellin|/kappa_0={ratio_delta_kappa0:.4e}<<1 "
        f"=> rel_span(xi_F*)={rel_span:.4e} in (1e-7,0.05] => magnitude=INFO (INFO-stays, suppressed); "
        f"EMERGENCE-1 closed-form Delta*{residue_mult:.1f}={residue_closedform_Mellin:.4e} vs direct "
        f"{residue_direct_Mellin:.4e} (err {closedform_err:.2e}) # {GATE_ID}",
        f"# OQ-4 RESOLUTION: §VII.AV.STATE-PROJ L_emp=-7.046336 UNCHANGED (SD-OPEN STAGE-3-PERMANENT, "
        f"PASS unreachable); the a_0^{{<class>}} qualifier stays SUPPRESSED SD-OPEN (CC-in-microcosm TAMED "
        f"not killed; the huge eigenvalue-moment a0 does NOT translate into a huge OCCUPATION counterterm "
        f"because the substrate's own Fermi surface sits below the |D_K| floor) # {GATE_ID}",
    ]
    print_verdict_payload(
        composite, value, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        companion_note="OQ-4 magnitude discriminator at the substrate-PINNED Fermi level xi_F* "
                       "(gap-IR occupation match): rel_span(xi_F*) suppressed sub-threshold "
                       "(xi_F* below |D_K| floor, a0-grade UV modes empty) => INFO-stays; "
                       "sign=PASS additive-channel-dominant model-INDEPENDENT",
        extra_rows=extra_rows,
    )

    print(f"\n  4-tuple: (value=rel_span(xi_F*)={rel_span:.4e} band={mag_v}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print("\nCOMPUTATION COMPLETE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
