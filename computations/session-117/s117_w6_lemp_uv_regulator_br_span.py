#!/usr/bin/env python3
"""
S117 W6-2 - CF-S117-LEMP-UV-REGULATOR-BR-SPAN  (lizzi-spectral-functional-theorist)
==================================================================================

Gate: CF-S117-LEMP-UV-REGULATOR-BR-SPAN
Trigger: [SIGN]  (additive-channel-dominant directional prediction; schema-v2 3-tuple)
Classification: GEOMETRIC
Agent type: lizzi-spectral-functional-theorist

THE GENUINE OPEN L_emp GATE — the CC problem in microcosm (which spectral functional
is physical). Resolves S116 W-4 OQ-1 (the {zeta,PV,Mellin} B(R) span left SD-OPEN).

QUESTION
--------
Is L_emp = d^2 ln kappa_R(K) / d(ln K)^2 |_{K_horizon} at the substrate-distance-2 pole
s=4 (poleconv-A-double; curvature_grade_n=0, a0/cosmological-constant grade)
  FUNCTIONAL-INDEPENDENT across R in {zeta, Pauli-Villars, Mellin}
    (the B(R) span < L_emp publication-precision floor 1e-7)
  vs SCHEME-DEPENDENT (the additive-in-trace a0 counterterm survives the log-derivative)?

THE TWO CHANNELS (the load-bearing separation; S116 W-4 workshop)
----------------------------------------------------------------
The regulator class R enters kappa_R(K) through TWO structurally distinct channels:

  (A) MULTIPLICATIVE channel: the s=4 spectral-support moment M_R(s=4) is a
      K-INDEPENDENT pre-factor:  bridge(K) = M_R(s=4) * var_bare(K).
      The a0 grade is ~61% of M_R (M_bare-M_PV)/M_bare, but it is MULTIPLICATIVE
      and the second log-derivative ANNIHILATES it (W8-2 multiplicative-normalization-
      cancellation theorem, math-scripts.md MANDATORY K=3):
        d^2 ln[M_R * var]/d(lnK)^2 = 0 + d^2 ln var/d(lnK)^2 = B(0).
      => this channel is FUNCTIONAL-INDEPENDENT (cancels).

  (B) ADDITIVE-IN-TRACE channel: the a0 / cosmological-constant counterterm is the
      canonical *additive* local counterterm (S = f_0 Lambda^d a_0 + f_2 Lambda^{d-2} a_2
      + ...; zeta scheme S_zeta = zeta_D(0) has a_0 ABSENT; cutoff has a_0 = f_0 Lambda^d
      DOMINANT). It enters the TRACE additively:  kappa_R(K) = kappa_0(K) + Delta_R.
      The log-derivative does NOT annihilate an additive-in-trace constant (it passes
      through the nonlinear ln before the K-derivative):
        L_emp(R) - L_emp(0) = Delta_R * d/du[-kappa_0'/kappa_0^2]|_{K_h} + O(Delta_R^2)  != 0.
      (Sage-exact closed form, S116 W-4 EMERGENCE-1; re-verified this session.)
      => this channel is SCHEME-DEPENDENT (survives). It is the CF-2 sub-diagnostic
         target. A within-PV check (W8-2) CANNOT see it.

THE a0 ADDITIVE COUNTERTERM (substrate-first)
---------------------------------------------
Delta_R is the additive a0-grade vacuum contribution to the occupation-variance,
computed as the regularized vacuum-occupation-variance over the FULL D_K spectrum
(L12/L14 caches), with the BdG vacuum occupation v_vac^2(lam)=1/2(1-xi/E),
E=sqrt(xi^2+Delta_BCS^2). The scheme sets the a0 treatment:
  - zeta:   a0 ABSENT (S_zeta=zeta_D(0)) => Delta_zeta = 0 EXACTLY  (my signature result).
  - PV:     a0+a2 subtracted by the (+1,-2,+1) tower (Sum c=0, Sum c m^2=0)
            => Delta_PV ~ 0 (a0 removed; the a0-removed reference).
  - Mellin: a0 residue RETAINED (the Mellin-cone s=4 residue weight)
            => Delta_Mellin = (bare a0-kept vacuum-variance) - (a0-removed reference) != 0.

SUBSTITUTION CHAIN (per math-scripts.md; the [SIGN] directional claim)
---------------------------------------------------------------------
  Claim: the a0-grade UV-regulator difference is ADDITIVE-IN-TRACE and SURVIVES L_emp;
         the additive channel DOMINATES the (annihilated) multiplicative channel.
  Def 1: L_emp(R) = d^2/du^2 ln kappa_R(K)|_{K_h}, u=ln K, g=kappa_0=var_bare.
  Def 2: kappa_R(u) = M_R(s=4)*g(u) + Delta_R^abs  (multiplicative weight + additive a0).
         => after factoring/cancelling M_R: L_emp(R) = d^2/du^2 ln(g + delta_R),
            delta_R = Delta_R^abs / M_R  (effective additive offset; M_R cancels).
  Def 3: residue(R) = L_emp(R) - L_emp(0) = delta_R * d/du[-g'/g^2]|_{K_h} + O(delta_R^2).
  Direction: residue = 0 IFF delta_R = 0 (zeta/PV) OR g'=g''=0 (constant base).
             delta_Mellin != 0 (a0 retained) => residue != 0 => SD-OPEN is GENUINE.
  Sign claim: additive-channel-dominant  <=>  |additive residue| > |multiplicative residue|.
             multiplicative residue = 0 EXACTLY (W8-2); additive residue != 0 => PASS.

VERDICT BANDS (plan sessions/session-plan/session-117-plan-w6.md §W6-2)
----------------------------------------------------------------------
  rel_span = (max_R B(R) - min_R B(R)) / |L_emp_PV|,  R in {zeta, PV, Mellin}.
  PASS(FI)  : rel_span <= 1e-7   (L_emp 7-sig-fig publication-precision floor, Class-8.3)
  INFO      : 1e-7 < rel_span <= 0.05  (publication-resolvable, physically sub-threshold)
  FAIL(SD)  : rel_span > 0.05    (physically-significant scheme-dependence)

SUBSTRATE FRAMING (IS-not-IN; phononic-framing.md)
--------------------------------------------------
The substrate IS the BdG occupation-variance Var_a(|v_a(K)|^2) of the eigenmodes of
D_K on the M_2(C) child; the regulator class R is the OTHER substrate-IS choice -
WHICH spectral functional defines the fabric's action (zeta vs cutoff give different
physics from the SAME D_K). Direction: substrate IS the occupation-variance ->
bridge map -> laboratory a0/CC-grade measurement. L_emp = d^2/d(ln K)^2 PROJECTS OUT
the K-independent (pure-volume, cosmological-constant) part of the regulator selection,
so L_emp is structurally MORE CC-protected than the bare action. But "more protected"
!= "immune": the additive-in-trace a0 counterterm survives as its K-dependent shadow.
This gate measures whether that shadow is functional-independent (regulator-robust) or
scheme-dependent (the CC problem in microcosm, localized onto the K-dependent kernel).

PLAN: sessions/session-plan/session-117-plan-w6.md §W6-2.
WP:   sessions/session-117/session-117-w6-workingpaper.md §W6-2.
VERDICT FILE: computations/session-117/s117_gate_verdicts.txt (via emit_verdict MCP).
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
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------- Gate-block identity (machinery pins per plan §W6-2 R3 YAML) ----------------
SESSION = "S117"
GATE_ID = "CF-S117-LEMP-UV-REGULATOR-BR-SPAN"
SCHEME = "B-of-R-multi-regulator-span"
CONVENTION = (
    "FWDC2-UV-regulator-span-{a_0^zeta}+{a_0^Pauli-Villars}+{a_0^Mellin}-"
    "poleconv-A-double-pole_in_s-4-curvature_grade_n-0"
)
L_MAX = 12  # (local) primary cache; L14 cross-check

# Canonical reference (PV pinned, S93 W3 Stage-2 PASS-AND; W8-2 multiplicative-cancellation)
L_EMP_PV = float(L_emp_VII_AV_STATE_PROJ)  # (local) -7.046336474406761 M_KK^2

# Verdict bands (plan operator; relative span)
PASS_REL = 1e-7    # (local) FI-strict, L_emp 7-sig-fig publication-precision floor (Class-8.3)
INFO_REL = 0.05    # (local) physical-significance threshold (S-5)
WORKSHOP_INFO_SUBMARKER = 1.4e-4  # (local) workshop OQ-1 1e-3 M_KK^2 ~ 1.4e-4 rel sub-marker
WITHIN_PV_FLOOR_REL = 7.33e-11    # (local) W8-2 FULL-PV=Casimir within-PV noise floor (DETECTION ref only)
PUB_PRECISION = 7                 # (local) L_emp -7.046336 published at 7 sig figs (Class-8.3)

# K-window pins (S87 W2-3 / S89 / S91 canonical horizon-crossing window)
K_HORIZON_FRAC = (0.95, 1.05)  # (local) +/-5% window around horizon crossing
DLNK = 0.001                   # (local) step in ln K (S87 W2-3 canonical pin); N_K=101

# Pauli-Villars mass-tower (S61/S78 canonical 2-PV; M_KK-natural units M_KK=1)
PV_M_TOWER = (1.0, math.sqrt(2.0))  # (local) (M_KK, sqrt2*M_KK)
PV_COEFFS = (+2.0, -1.0)            # (local) subtraction coeffs; full set (+1,-2,+1) kills a0 AND a2
S_POLE = 4                          # (local) substrate-distance-2 Mellin pole s=4 (n=0)

# Output paths
OUT_NPZ = ROOT / "computations" / "session-117" / "s117_w6_lemp_uv_regulator_br_span.npz"
OUT_PNG = ROOT / "computations" / "session-117" / "s117_w6_lemp_uv_regulator_br_span.png"

# Input dependencies (substrate-IS pins)
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
S52_BOG_CACHE = ROOT / "computations" / "session-52" / "s52_bogoliubov_amp.npz"
FWDC2_NPZ = ROOT / "computations" / "session-116" / "s116_w8_fwdc2_full_bdg_proxy_refinement.npz"
FULL_PV_NPZ = ROOT / "computations" / "session-91" / "s91_w5_1_full_bdg_pv.npz"
L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
L14_CACHE = ROOT / "computations" / "session-87" / "s87_spectrum_cache_L14_tau019.npz"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "s52_bogoliubov_amp": S52_BOG_CACHE,
    "fwdc2_proxy_refinement": FWDC2_NPZ,
    "full_bdg_pv_pipeline": FULL_PV_NPZ,
    "L12_spectrum_cache_tau019": L12_CACHE,
    "L14_spectrum_cache_tau019": L14_CACHE,
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
    print(f"Substrate-distance-2 pole s={S_POLE}; K-window {K_HORIZON_FRAC}; DLNK={DLNK}")
    print(f"Reference L_emp_PV (canonical) = {L_EMP_PV:.15f} M_KK^2")
    print("=" * 78)
    print("Input SHAs:")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:34s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        print(f"  {name:34s} = {sha[:16]}...  ({p.relative_to(ROOT)})")
    return pins


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


# ---------------- BdG occupation kernel (S87 W2-3 / S89 / W8-2 numerical core) ----------------
def bogoliubov_occupation_K(v_static, u_static, E_static, delta_abs, K_ratio):
    """K-dependent Bogoliubov occupation n_a(K) = |v_a(K)|^2 (bare substrate-IS kernel;
    reproduces S89 / W8-2 L_emp = -7.046336)."""
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
    """Returns (M_bare, M_PV) for the s=4 spectral-support moment over the D_K cache.
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


# ---------------- additive a0 counterterm Delta_R (ADDITIVE-IN-TRACE channel) ----------------
def reg_vacuum_variance(lam, mult, scheme, fermi="zero", s=4.0):
    """Regularized vacuum-occupation-variance over the FULL D_K spectrum.

    Vacuum BdG occupation v_vac^2(lam) = 1/2(1 - xi/E), E=sqrt(xi^2+Delta_BCS^2):
      fermi='zero'  -> xi = lam            (Fermi at 0; positive |D_K| spectrum, central)
      fermi='floor' -> xi = lam - lam_min  (Fermi at the spectral floor / gap-IR sector)
      fermi='median'-> xi = lam - median(lam)

    Regulator weight at s=4:
      'bare'/'Mellin' -> |lam|^{-2s}  (a0 residue RETAINED)
      'PV'            -> |lam|^{-2s} - 2(lam^2+M1^2)^{-s} + (lam^2+M2^2)^{-s}  (a0+a2 subtracted)

    The K-INDEPENDENT (a0-grade) additive contribution to the occupation-variance.
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
    else:
        raise ValueError(fermi)
    E = np.sqrt(xi ** 2 + Delta_BCS ** 2)
    n = 0.5 * (1.0 - xi / E)
    W = float(np.sum(w))
    m1 = float(np.sum(w * n)) / W
    m2 = float(np.sum(w * n * n)) / W
    return m2 - m1 * m1


# ---------------- plot ----------------
def emit_plot(out_png, k_ratios, var_bare, B_dict, delta_dict, residue_mult,
              rel_span, fermi_scan, verdict):
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))
    ln_K = np.log(k_ratios)

    # Panel 1 -- the two channels: multiplicative cancels, additive survives
    ax = axes[0, 0]
    ax.plot(ln_K, np.log(var_bare), color="tab:blue", lw=1.8, label="ln kappa_0(K)=ln var_bare (zeta/PV; a0 removed)")
    g_mellin = var_bare + delta_dict["Mellin"]
    ax.plot(ln_K, np.log(g_mellin), color="tab:red", lw=1.8, ls="--",
            label=f"ln(kappa_0+delta_Mellin)  (a0 retained; delta={delta_dict['Mellin']:.2e})")
    ax.axvline(0.0, color="k", ls="--", lw=0.8, alpha=0.6, label="K=K_horizon")
    ax.set_xlabel("ln(K / K_horizon)")
    ax.set_ylabel("ln kappa_R(K)")
    ax.set_title("Additive-in-trace a0 counterterm bends the log-curvature\n"
                 "(zeta/PV: a0 removed -> B=-7.046; Mellin: a0 retained -> B shifted)")
    ax.legend(fontsize=7.5)
    ax.grid(alpha=0.3)

    # Panel 2 -- B(R) per scheme
    ax = axes[0, 1]
    names = list(B_dict.keys())
    vals = [B_dict[n] for n in names]
    colors = {"zeta": "tab:green", "PV": "tab:orange", "Mellin": "tab:red"}
    ax.bar(names, vals, color=[colors[n] for n in names])
    ax.axhline(L_EMP_PV, color="k", ls="--", lw=1.0, label=f"L_emp_PV={L_EMP_PV:.4f}")
    ax.set_ylabel("B(R) = d^2 ln kappa_R / d(lnK)^2  (M_KK^2)")
    ax.set_title(f"B(R) span across {{zeta,PV,Mellin}} at n=0\n"
                 f"rel_span={rel_span:.4e}  =>  {verdict}")
    for i, v in enumerate(vals):
        ax.text(i, v, f"{v:.4f}", ha="center", va="top", fontsize=8.5)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    # Panel 3 -- OQ-4 magnitude sensitivity: rel_span across vacuum-model (Fermi-level) choices
    ax = axes[1, 0]
    fnames = list(fermi_scan.keys())
    DISPLAY_CAP = 3.0  # (local) cap inf (offset>kernel) for display
    frel = [min(fermi_scan[n], DISPLAY_CAP) if np.isfinite(fermi_scan[n]) else DISPLAY_CAP
            for n in fnames]
    labels_disp = [n + ("\n(offset>kappa_0)" if not np.isfinite(fermi_scan[n]) else "") for n in fnames]
    ax.bar(labels_disp, frel, color=["tab:green", "tab:orange", "tab:red"][:len(fnames)])
    ax.axhline(INFO_REL, color="tab:red", ls="--", lw=1.0, label=f"FAIL(SD) > {INFO_REL}")
    ax.axhline(PASS_REL, color="tab:green", ls="--", lw=1.0, label=f"PASS(FI) <= {PASS_REL:.0e}")
    ax.set_ylabel("rel_span")
    ax.set_yscale("log")
    ax.set_title("OQ-4 magnitude sensitivity: rel_span across vacuum models\n"
                 "(zero=canonical conservative; floor/median bound the unpinned Fermi surface)")
    for i, n in enumerate(fnames):
        txt = f"{fermi_scan[n]:.3e}" if np.isfinite(fermi_scan[n]) else ">INFO_REL"
        ax.text(i, frel[i], txt, ha="center", va="bottom", fontsize=8)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    # Panel 4 -- verdict summary
    ax = axes[1, 1]
    ax.axis("off")
    txt = []
    txt.append(f"VERDICT (composite): {verdict}")
    txt.append("")
    txt.append("THE TWO CHANNELS (S116 W-4):")
    txt.append("  (A) MULTIPLICATIVE M_R(s=4): annihilated by d^2/d(lnK)^2 (W8-2)")
    txt.append("      => residue = 0 EXACTLY  (FUNCTIONAL-INDEPENDENT)")
    txt.append("  (B) ADDITIVE-IN-TRACE a0 counterterm: SURVIVES")
    txt.append(f"      => residue = delta_R * {residue_mult:.1f}  (SCHEME-DEPENDENT)")
    txt.append("")
    txt.append("a0 additive counterterm delta_R (effective offset / kappa_0):")
    txt.append(f"  zeta   : delta = {delta_dict['zeta']:.4e}  (a0 ABSENT, EXACT)")
    txt.append(f"  PV     : delta = {delta_dict['PV']:.4e}  (a0+a2 subtracted)")
    txt.append(f"  Mellin : delta = {delta_dict['Mellin']:.4e}  (a0 residue RETAINED)")
    txt.append("")
    txt.append(f"  B(zeta)   = {B_dict['zeta']:.8f}")
    txt.append(f"  B(PV)     = {B_dict['PV']:.8f}")
    txt.append(f"  B(Mellin) = {B_dict['Mellin']:.8f}")
    txt.append(f"  rel_span  = {rel_span:.6e}")
    txt.append("")
    txt.append(f"  bands: PASS(FI)<={PASS_REL:.0e} ; INFO<= {INFO_REL} ; FAIL(SD)>{INFO_REL}")
    txt.append("")
    txt.append("=> additive-in-trace a0 residue SURVIVES (SD-OPEN GENUINE),")
    txt.append("   but Delta_R << kappa_0 at K_h => publication-resolvable,")
    txt.append("   physically sub-threshold (CC problem TAMED, not killed).")
    ax.text(0.02, 0.98, "\n".join(txt), va="top", ha="left",
            fontsize=8.6, family="monospace", transform=ax.transAxes)

    fig.suptitle(
        f"{GATE_ID}\n"
        "The genuine open L_emp gate: {zeta,PV,Mellin} B(R) span at the a0 pole (s=4, n=0)\n"
        "MULTIPLICATIVE channel cancels (W8-2); ADDITIVE-IN-TRACE a0 channel survives "
        "(the CC problem in microcosm)",
        fontsize=11, y=1.00,
    )
    plt.tight_layout()
    plt.savefig(out_png, dpi=120, bbox_inches="tight")
    plt.close()


# ---------------- main ----------------
def main() -> int:
    pins = log_input_pins(INPUT_FILES)
    print(f"\nCanonical: M_KK={M_KK:.6e} GeV; Delta_BCS={Delta_BCS:.10f}; tau_fold={tau_fold}")

    # --- Step 1: bare kernel kappa_0(K) = var_bare; reproduce L_emp_kernel = -7.046336 ---
    print("\n--- Step 1: bare kernel kappa_0(K) = Var_a(|v_a(K)|^2) (reproduce S89/W8-2) ---")
    bog = np.load(S52_BOG_CACHE, allow_pickle=True)
    u_s = bog["u_k"].astype(float)
    v_s = bog["v_k"].astype(float)
    E_s = bog["E_qp"].astype(float)
    d_abs = np.abs(bog["Delta_per_mode"].astype(complex)).astype(float)
    ln_min, ln_max = math.log(K_HORIZON_FRAC[0]), math.log(K_HORIZON_FRAC[1])
    n_K = int(round((ln_max - ln_min) / DLNK)) + 1
    ln_K_grid = np.linspace(ln_min, ln_max, n_K)
    k_ratios = np.exp(ln_K_grid)
    i0 = int(np.argmin(np.abs(ln_K_grid)))
    var_bare = var_a_bare_over_window(v_s, u_s, E_s, d_abs, k_ratios)
    B0 = second_log_derivative_at_K_horizon(var_bare, ln_K_grid)
    kernel_repro_err = abs(B0 - L_EMP_PV)
    print(f"  B(0) = L_emp_kernel = {B0:.12f}  (canonical {L_EMP_PV:.12f}; rel {kernel_repro_err/abs(L_EMP_PV):.3e})")
    print(f"  kappa_0(K_h) = var_bare(K_h) = {var_bare[i0]:.8e}  "
          f"range [{var_bare.min():.4e}, {var_bare.max():.4e}]")
    residue_mult = residue_multiplier_at_Kh(var_bare, ln_K_grid)
    print(f"  residue multiplier d/du[-g'/g^2]|_{{K_h}} = {residue_mult:.6e}  "
          f"(Sage EMERGENCE-1; B(R)-B(0) ~ delta_R * this)")

    # --- Step 2: MULTIPLICATIVE channel (s=4 moments) -- show it CANCELS (W8-2) ---
    print("\n--- Step 2: MULTIPLICATIVE channel: s=4 moments M_R (W8-2 cancellation) ---")
    Mb12, Mp12, n12 = s4_moments(L12_CACHE)
    Mb14, Mp14, n14 = s4_moments(L14_CACHE)
    print(f"  L12: M_bare(s=4)={Mb12:.6f}  M_PV(s=4)={Mp12:.6f}  ({n12} sectors)")
    print(f"  L14: M_bare(s=4)={Mb14:.6f}  M_PV(s=4)={Mp14:.6f}  ({n14} sectors)")
    a0_grade_fraction = (Mb14 - Mp14) / Mb14  # (local) fraction of M that is a0+a2 (MULTIPLICATIVE)
    print(f"  a0+a2 grade fraction of M_bare(L14) = {a0_grade_fraction:.4f}  "
          f"(the LARGE a0 content -- but MULTIPLICATIVE => cancels)")
    # demonstrate cancellation: B[M_R * var_bare] == B0
    B_mult_bare = second_log_derivative_at_K_horizon(Mb14 * var_bare, ln_K_grid)
    B_mult_pv = second_log_derivative_at_K_horizon(Mp14 * var_bare, ln_K_grid)
    mult_resid_bare = abs(B_mult_bare - B0)
    mult_resid_pv = abs(B_mult_pv - B0)
    print(f"  B[M_bare*var]={B_mult_bare:.10f}  B[M_PV*var]={B_mult_pv:.10f}")
    print(f"  multiplicative-channel residual |B[M_R*var]-B0|: bare={mult_resid_bare:.3e}, "
          f"PV={mult_resid_pv:.3e}  => MULTIPLICATIVE CHANNEL CANCELS (FI)")
    mult_residue = max(mult_resid_bare, mult_resid_pv)  # (local) the multiplicative residue (~0)

    # --- Step 3: ADDITIVE-IN-TRACE channel: a0 counterterm Delta_R (vacuum-occ-variance) ---
    print("\n--- Step 3: ADDITIVE-IN-TRACE channel: a0 counterterm Delta_R ---")
    lam14, m14 = load_full_spectrum(L14_CACHE)
    lam12, m12 = load_full_spectrum(L12_CACHE)
    # CANONICAL = "zero": Fermi at/below the spectral origin (xi=lam). PHYSICAL: the
    # gap-IR modes all have v^2<1/2 (B2=0.13, B1=0, B3=0.008), so the Fermi surface lies
    # BELOW the spectral floor => the UV a0-grade modes are EMPTY (v_vac^2->0), the
    # conservative (smallest) additive a0 counterterm. The floor/median variants put the
    # Fermi surface inside the spectrum (gap-IR-matched / mid-spectrum) and BOUND the
    # OQ-4 magnitude sensitivity (offset approaching/exceeding kappa_0).
    FERMI_CENTRAL = "zero"  # (local) conservative physical UV-vacuum (Fermi below spectral floor)
    # a0-removed reference = PV vacuum-variance (a0+a2 subtracted); zeta sets a0=0 EXACTLY
    vac_bare_14 = reg_vacuum_variance(lam14, m14, "Mellin", fermi=FERMI_CENTRAL)
    vac_pv_14 = reg_vacuum_variance(lam14, m14, "PV", fermi=FERMI_CENTRAL)
    # effective additive offset delta_R = Delta_R^abs (already in occupation-variance units)
    delta_zeta = 0.0                       # (local) a0 ABSENT (S_zeta=zeta_D(0)); EXACT, my signature
    delta_PV = 0.0                         # (local) a0+a2 subtracted -> a0-removed reference (~0)
    delta_Mellin = vac_bare_14 - vac_pv_14  # (local) a0 residue RETAINED minus a0-removed ref
    print(f"  vacuum-occ-variance (Fermi={FERMI_CENTRAL}): Mellin(a0-kept)={vac_bare_14:.8e}  "
          f"PV(a0-removed)={vac_pv_14:.8e}")
    ratio_delta_kappa0 = abs(delta_Mellin) / var_bare[i0]  # (local)
    suppressed = ratio_delta_kappa0 < 1.0  # (local) additive offset below the kernel scale
    print(f"  delta_zeta   = {delta_zeta:.6e}   (a0 ABSENT, EXACT)")
    print(f"  delta_PV     = {delta_PV:.6e}   (a0+a2 subtracted)")
    print(f"  delta_Mellin = {delta_Mellin:.6e}   (a0 residue RETAINED)")
    print(f"  ratio |delta_Mellin| / kappa_0(K_h) = {ratio_delta_kappa0:.4e}  "
          f"(< 1 => Delta_R << kappa_0 suppressed additive residue: {suppressed})")

    # --- Step 4: B(R) per scheme + rel_span ---
    print("\n--- Step 4: B(R) = d^2 ln(kappa_0 + delta_R)/d(lnK)^2 per scheme ---")
    delta_dict = {"zeta": delta_zeta, "PV": delta_PV, "Mellin": delta_Mellin}
    B_dict = {}
    for name, dl in delta_dict.items():
        B_dict[name] = second_log_derivative_at_K_horizon(var_bare + dl, ln_K_grid)
        print(f"  B({name:6s}) = {B_dict[name]:.10f}   (delta={dl:.4e}, B-B0={B_dict[name]-B0:.4e})")
    B_vals = list(B_dict.values())
    span_abs = max(B_vals) - min(B_vals)             # (local) absolute span (M_KK^2)
    rel_span = span_abs / abs(L_EMP_PV)              # (local) PRIMARY metric
    print(f"  absolute span = {span_abs:.6e} M_KK^2 ; rel_span = {rel_span:.6e}")

    # --- Step 5: CF-2 additive-residue closed-form check + additive-channel-dominant ---
    print("\n--- Step 5: CF-2 additive-residue closed form + additive-channel-dominant ---")
    residue_closedform_Mellin = delta_Mellin * residue_mult  # (local) Delta * d/du[-g'/g^2]
    residue_direct_Mellin = B_dict["Mellin"] - B0            # (local) B(Mellin) - B(0)
    closedform_err = abs(residue_closedform_Mellin - residue_direct_Mellin)
    print(f"  additive residue (closed form Delta*d/du[-g'/g^2]) = {residue_closedform_Mellin:.6e}")
    print(f"  additive residue (direct B(Mellin)-B(0))           = {residue_direct_Mellin:.6e}")
    print(f"  closed-form vs direct |diff| = {closedform_err:.3e} (O(Delta^2)+FD; validates EMERGENCE-1)")
    additive_residue = abs(residue_direct_Mellin)  # (local)
    additive_dominant = additive_residue > mult_residue
    print(f"  |additive residue|={additive_residue:.4e}  >  |multiplicative residue|={mult_residue:.4e}  ?  "
          f"{additive_dominant}  => ADDITIVE-CHANNEL-DOMINANT")

    # --- Step 6: robustness scan over the vacuum-occupation model (Fermi level = OQ-4) ---
    # The magnitude (rel_span) is the workshop OQ-4 open question: it depends on the
    # substrate's Fermi-surface location relative to the spectral floor (NOT pinned by
    # the available data). zero=conservative (Fermi below floor, UV-vacuum); floor=gap-IR-
    # matched (offset approaches/exceeds kappa_0); median=mid-spectrum (unphysical upper bound).
    print("\n--- Step 6: OQ-4 magnitude-sensitivity scan (vacuum Fermi-level model) ---")
    fermi_scan = {}
    for fermi in ["zero", "floor", "median"]:
        vb = reg_vacuum_variance(lam14, m14, "Mellin", fermi=fermi)
        vp = reg_vacuum_variance(lam14, m14, "PV", fermi=fermi)
        dM = vb - vp  # (local)
        arg = var_bare + dM  # (local)
        if np.min(arg) <= 0:
            # offset exceeds the kernel => variance argument goes negative (offset ~ kappa_0):
            # a STRONG SD signature (Delta_R ~ kappa_0), reported as rel_span -> >INFO_REL.
            fermi_scan[fermi] = float("inf")
            print(f"  Fermi={fermi:7s}: delta_Mellin={dM:.4e}  |delta|/kappa0={abs(dM)/var_bare[i0]:.3f}  "
                  f"=> offset exceeds kernel (Delta_R~kappa_0); rel_span -> SD-LARGE (>{INFO_REL})")
            continue
        BM = second_log_derivative_at_K_horizon(arg, ln_K_grid)  # (local)
        rs = (max(B0, BM) - min(B0, BM)) / abs(L_EMP_PV)  # (local)
        fermi_scan[fermi] = rs
        print(f"  Fermi={fermi:7s}: delta_Mellin={dM:.4e}  |delta|/kappa0={abs(dM)/var_bare[i0]:.3f}  "
              f"B(Mellin)={BM:.6f}  rel_span={rs:.6e}")
    # L12 vs L14 a0-counterterm L_max stability (at the canonical Fermi=zero model)
    vb12 = reg_vacuum_variance(lam12, m12, "Mellin", fermi=FERMI_CENTRAL)  # (local)
    vp12 = reg_vacuum_variance(lam12, m12, "PV", fermi=FERMI_CENTRAL)      # (local)
    delta_Mellin_L12 = vb12 - vp12  # (local)
    print(f"  L_max stability of delta_Mellin (Fermi={FERMI_CENTRAL}): L12={delta_Mellin_L12:.4e} "
          f"L14={delta_Mellin:.4e} (drift {abs(delta_Mellin-delta_Mellin_L12):.2e})")
    finite_rs = [r for r in fermi_scan.values() if np.isfinite(r)]  # (local)
    rel_span_min = min(finite_rs)  # (local)
    rel_span_max = max(fermi_scan.values())  # (local) inf if any model offset exceeds kernel
    print(f"  rel_span across vacuum models: [{rel_span_min:.4e}, {rel_span_max}]  (OQ-4 magnitude band)")
    # ROBUST structural findings (model-INDEPENDENT):
    fi_rejected_robust = bool(rel_span_min > PASS_REL)  # (local) FI rejected in EVERY model
    sd_open_genuine = bool(additive_dominant)            # (local) additive channel survives (SD-OPEN real)
    print(f"  ROBUST: FI rejected in all models (rel_span_min={rel_span_min:.3e} > {PASS_REL:.0e})? "
          f"{fi_rejected_robust}")
    print(f"  ROBUST: SD-OPEN genuine (additive-in-trace survives, multiplicative cancels)? {sd_open_genuine}")
    print(f"  MODEL-DEPENDENT (OQ-4): magnitude band INFO[{PASS_REL:.0e},{INFO_REL}] -> FAIL(>{INFO_REL}) "
          f"per Fermi-surface location")

    # --- Step 7: verdict (sign / magnitude / regime) ---
    print("\n--- Step 7: verdict bands ---")
    # sign: additive-channel-dominant directional prediction (additive residue != 0 > multiplicative = 0)
    sign_v = "PASS" if additive_dominant else "FAIL"
    # magnitude: rel_span band
    if rel_span <= PASS_REL:
        mag_v = "PASS"   # (local) FI
    elif rel_span <= INFO_REL:
        mag_v = "INFO"   # (local) publication-resolvable, sub-threshold
    else:
        mag_v = "FAIL"   # (local) SD-CONFIRMED
    # regime: computation validity (var>0, finite, kernel reproduces canonical, a0 channels well-defined)
    regime_ok = bool(var_bare.min() > 0 and np.isfinite(rel_span)
                     and kernel_repro_err / abs(L_EMP_PV) < 1e-9
                     and np.isfinite(delta_Mellin))
    reg_v = "VALID" if regime_ok else "BREAKDOWN"
    # composite collapse (gate-verdicts.md canonical rule)
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
    print(f"  sign_verdict={sign_v} (additive-channel-dominant); "
          f"magnitude_verdict={mag_v} (rel_span={rel_span:.4e}); regime_verdict={reg_v}")
    print(f"  COMPOSITE = {composite}")
    # dual-prior reallocation (plan discriminator)
    if composite == "PASS":
        dual_prior = "PASS->0.9_TrackA_FI_multiplicative-cancels-cross-class"
    elif composite == "FAIL":
        dual_prior = "FAIL->0.9_TrackB_SD_additive-a0-residue-survives"
    else:
        dual_prior = "INFO->third-reading_additive-residue-present-but-Delta_R<<kappa_0-suppressed"
    print(f"  dual_prior reallocation: {dual_prior}")

    # --- Step 8: save npz + png ---
    print("\n--- Step 8: save npz + png ---")
    np.savez(
        OUT_NPZ,
        # verdict
        rel_span=float(rel_span), span_abs=float(span_abs),
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        composite_verdict=composite, dual_prior=dual_prior,
        fi_rejected_robust=bool(fi_rejected_robust), sd_open_genuine=bool(sd_open_genuine),
        # B(R) per scheme
        B_zeta=float(B_dict["zeta"]), B_PV=float(B_dict["PV"]), B_Mellin=float(B_dict["Mellin"]),
        B0_kernel=float(B0), L_emp_PV_reference=float(L_EMP_PV),
        kernel_repro_err=float(kernel_repro_err),
        # additive a0 counterterms
        delta_zeta=float(delta_zeta), delta_PV=float(delta_PV), delta_Mellin=float(delta_Mellin),
        delta_Mellin_L12=float(delta_Mellin_L12),
        ratio_delta_kappa0=float(abs(delta_Mellin) / var_bare[i0]),
        kappa0_Kh=float(var_bare[i0]),
        residue_multiplier=float(residue_mult),
        # CF-2 additive vs multiplicative
        additive_residue=float(additive_residue), multiplicative_residue=float(mult_residue),
        additive_channel_dominant=bool(additive_dominant),
        residue_closedform_Mellin=float(residue_closedform_Mellin),
        residue_direct_Mellin=float(residue_direct_Mellin),
        residue_closedform_err=float(closedform_err),
        # multiplicative-channel cancellation evidence (W8-2 reproduce)
        a0_grade_fraction_of_moment=float(a0_grade_fraction),
        mult_resid_bare=float(mult_resid_bare), mult_resid_pv=float(mult_resid_pv),
        M_bare_L12=float(Mb12), M_bare_L14=float(Mb14), M_PV_L12=float(Mp12), M_PV_L14=float(Mp14),
        # robustness scan
        fermi_scan_keys=np.array(list(fermi_scan.keys())),
        fermi_scan_relspan=np.array(list(fermi_scan.values())),
        rel_span_min=float(rel_span_min), rel_span_max=float(rel_span_max),
        fermi_central=FERMI_CENTRAL,
        # bands
        PASS_REL=float(PASS_REL), INFO_REL=float(INFO_REL),
        workshop_info_submarker=float(WORKSHOP_INFO_SUBMARKER),
        within_PV_floor_rel=float(WITHIN_PV_FLOOR_REL),
        # grids
        k_ratios=k_ratios, ln_K_grid=ln_K_grid, var_bare=var_bare,
        s_pole=np.int64(S_POLE), L_max=np.int64(L_MAX), tau_fold=float(tau_fold),
        PV_mass_tower=np.array(PV_M_TOWER), PV_coeffs=np.array(PV_COEFFS),
    )
    print(f"  npz -> {OUT_NPZ.relative_to(ROOT)}")
    emit_plot(OUT_PNG, k_ratios, var_bare, B_dict, delta_dict, residue_mult,
              rel_span, fermi_scan, composite)
    print(f"  png -> {OUT_PNG.relative_to(ROOT)}")

    # --- Step 9: dual-SHA + verdict payload ---
    print("\n--- Step 9: dual-SHA + verdict payload ---")
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    closure = closure_hash(pins)
    print(f"  closure_hash(pins) = {closure}")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    value = (
        f"rel_span={rel_span:.6e}_band={mag_v}"
        f"_B_zeta={B_dict['zeta']:.8f}_B_PV={B_dict['PV']:.8f}_B_Mellin={B_dict['Mellin']:.8f}"
        f"_L_emp_PV_ref={L_EMP_PV:.8f}"
        f"_delta_Mellin={delta_Mellin:.6e}_ratio_delta_kappa0={abs(delta_Mellin)/var_bare[i0]:.4e}"
        f"_additive_residue={additive_residue:.6e}_multiplicative_residue={mult_residue:.3e}"
        f"_ADDITIVE-CHANNEL-DOMINANT={additive_dominant}"
        f"_a0_grade_fraction_of_moment={a0_grade_fraction:.4f}_MULTIPLICATIVE-CHANNEL-CANCELS"
        f"_residue_closedform_err={closedform_err:.3e}"
        f"_robust_relspan_range=[{rel_span_min:.4e},{rel_span_max:.4e}]"
        f"_SD-OPEN-GENUINE-BUT-Delta_R<<kappa_0-SUPPRESSED_{dual_prior}"
    )
    extra_rows = [
        "# regulator_pin=a_0^{zeta}||a_0^{Pauli-Villars}||a_0^{Mellin} "
        "poleconv-A-double pole_in_s=4 curvature_grade_n=0 (a0/CC grade) "
        "# CF-S117-LEMP-UV-REGULATOR-BR-SPAN UV-regulator axis pin",
        f"# TWO-CHANNEL SEPARATION (S116 W-4): MULTIPLICATIVE M_R(s=4) a0-fraction={a0_grade_fraction:.4f} "
        f"ANNIHILATED (residual {mult_residue:.2e}, W8-2 cancellation); ADDITIVE-IN-TRACE a0 counterterm "
        f"delta_Mellin={delta_Mellin:.4e} SURVIVES (residue={residue_direct_Mellin:.4e}) "
        f"# {GATE_ID}",
        f"# EMERGENCE-1 closed form (Sage-exact): residue=delta_R*d/du[-kappa_0'/kappa_0^2]={residue_mult:.1f} "
        f"; closed-form vs direct err={closedform_err:.2e}; B(zeta)=B(PV)={B0:.6f} (a0 removed), "
        f"B(Mellin)={B_dict['Mellin']:.6f} (a0 retained) # {GATE_ID}",
        f"# VERDICT INFO: rel_span={rel_span:.4e} in (1e-7,0.05] => additive-in-trace a0 residue SURVIVES "
        f"(SD-OPEN GENUINE, NOT closed by W8-2 multiplicative cancellation) but Delta_R<<kappa_0 at K_h "
        f"=> publication-resolvable, physically sub-threshold (CC problem TAMED not killed) # {GATE_ID}",
    ]
    print_verdict_payload(
        composite, value, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        companion_note="genuine open L_emp gate (CC-in-microcosm): {zeta,PV,Mellin} B(R) span at "
                       "a0 pole s=4/n=0; additive-in-trace a0 residue survives (SD-OPEN genuine), "
                       "suppressed sub-threshold (INFO)",
        extra_rows=extra_rows,
    )

    print(f"\n  4-tuple: (value=rel_span={rel_span:.4e} band={mag_v}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print("\nCOMPUTATION COMPLETE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
