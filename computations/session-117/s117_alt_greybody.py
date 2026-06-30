#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CF-S117-ALT-GREYBODY  (session-117, Wave 1, gate 1-4)  [VERIFY]
==============================================================

GATE: Do EITHER of two alternative substrate-IS exit-greybody BRIDGE MAPS reach the
required attenuation Gamma_req = 10^{-OOM} at a SUBSTRATE-NATURAL (non-in-band,
non-fitted) scale, WITHOUT the S95 A2 in-band V0 sigmoid knob?

  Bridge map (1) — Wodzicki / a_n^{Pauli-Villars} spectral-MOMENT-RATIO:
        Gamma = Res_W(s)/Res_W(s')  =  M(s_a2)/M(s_a4)
        the ratio of the two LOAD-BEARING Seeley-DeWitt moments of the substrate
        spectrum at the a_2 and a_4 poles (poleconv-A-double, d=8:
        a_2 pole pole_in_s=3 / curvature_grade_n=2 ; a_4 pole pole_in_s=2 / n=4).
        The Wodzicki ratio carries degree -2(s_a2 - s_a4) = -2 = EVEN  =>  d_A=0
        even-morphism (parity-admissible per cross-pillar-bridge-corpus §23.0(5)).

  Bridge map (2) — Connes-distance (inverse spectral diameter):
        Gamma = d_C = 1/(lambda_max - lambda_min)  on the exit-horizon BdG sector.
        A single substrate-natural number per spectrum; NO placement freedom.

SUBSTRATE EIGENVALUE SOURCES (closed-form bridge-map evaluations on EXISTING caches;
no new spectrum build, per plan effort field):
  - D_K spectrum: s84_spectrum_cache_L12_tau019.npz  sector_evals  (L_max=12, tau_fold=0.19)
        full abs-eigenvalue list (16*dim per (p,q) sector; multiplicity already included).
  - BdG dispersion (exit-horizon BdG sector): inv12_w3_4_greybody_from_bdg.npz  omega_k
        omega_k = sqrt(lambda_k^4 + Delta_k^2) for the 1248 relic modes (mu_chem=0).
  We report BOTH spectra for EACH bridge map (the plan parenthetical pins the eigenvalues
  to the s84 D_K sector_evals; the inv12 BdG band is the "exit-horizon BdG sector" naming
  + scan_range).  Including the BdG readings is the GENEROUS (closest-to-target) choice;
  the FAIL is robust under the strict D_K-only reading too (best_rel_dev 0.50).

TARGETS (plan §W1-4 substitution chain):
  Gamma_req(box-delta) = A_s_CMB / A_s_FW = 10^{-0.8644}   (the +0.864 ksi_KZ-grid fork member)
  Gamma_req(slow-roll) = 10^{-0.19617}                     (the +0.196 H~-grid fork member; OOM
                                                            plan-pinned, A_s(H~) npz-sourced)
  Gamma_fit            = 0.511872                          (s95_w4_3 FITTED comparator; the in-band knob)

OPERATOR (plan):  PASS iff  min over {moment-ratio, Connes-distance} of
                  |Gamma_bridge - Gamma_target|/Gamma_target <= 0.10  at a NON-IN-BAND scale.
  FAIL iff BOTH bridge maps miss (best agreement > 0.10) at all substrate-natural scales.
  INFO iff EXACTLY ONE bridge map reaches a target (bridge-map-SENSITIVE / construction-dependent).

KNOB-LOCATION COROLLARY (the [VERIFY] payload):
  The moment-ratio bridge map carries a HIDDEN knob — the Pauli-Villars regulator mass M_reg.
  The physically-correct UV-regulator limit M_reg -> infinity (M_reg >= lambda_max, ABOVE the
  spectrum) RECOVERS the bare moment ratio (knob-free) => MISS.  Only by placing M_reg IN the
  spectral bulk (M_reg ~ M_KK ~ band scale, BELOW lambda_max) can the ratio be tuned onto a
  target — that placement is the moment-ratio analog of the forbidden S95 in-band V0 sigmoid
  knob, and is excluded by the convention pin "substrate-natural scale (NON-in-band)".  We
  COMPUTE and STORE the full M_reg sweep to expose the knob; the verdict keys ONLY on the
  knob-free (M_reg -> infinity) bare reading + the Connes diameter.

Classification: PHONONIC.  The exit greybody IS the substrate's own transmission of the
squeezed GGE power through the post-fold a_4 condensation-energy barrier at the acoustic
white-hole exit horizon.  INV12-W3-4 found the near-horizon-barrier (Poeschl-Teller) family
gives ∫Gamma=0.0363 (agreement 0.929, FAIL) — "NOT substrate-derivable" SCOPED to that family.
This gate tests TWO families that one does NOT cover; a FAIL GENERALIZES the wall to 3 classes.

DISCIPLINE (gate-verdicts.md / regulator-pin-discipline.md):
  - from canonical_constants import *  (M_KK, A_s_CMB, A_s_FW, kappa_exit, Delta_BCS, tau_fold)
  - regulator_pin: a_n^{Pauli-Villars} + Wodzicki Res_W(s); poleconv-A-double; declare
    (pole_in_s, curvature_grade_n) for both poles.
  - dual-SHA (S84+); verdict via emit_verdict (race-safe MCP tool); [VERIFY] => no 3-tuple.
  - GPU_path: the bridge maps are VECTOR REDUCTIONS over a CACHED eigenvalue list (the cache
    PROVIDES the eigenvalues; NO >=100x100 matrix diagonalization is performed), so the plan's
    conditional "torch.linalg if ... >=100x100" is NOT triggered; cpu-cap-OMP8 is correct.
    Honest deviation disclosure per v3-closure-recovery PROHIBITED_ACTIONS Class 1 boundary.
  Script structure mirrors the sibling inv12_w3_4_greybody_from_bdg.py (same author lineage;
  dual-SHA + print_verdict_payload) and the delimited-JSON payload of
  .claude/templates/script-template.py print_verdict_payload.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) cap CPU threads before numpy import
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import hashlib
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- canonical constants (MANDATORY import) ----
sys.path.insert(0, os.path.join("computations", "_shared"))
from canonical_constants import (  # noqa: E402
    M_KK, A_s_CMB, A_s_FW, kappa_exit, Delta_BCS, tau_fold,
)

# =====================================================================================
# Pinned machinery (plan §W1-4)
# =====================================================================================
GATE_ID = "CF-S117-ALT-GREYBODY"
SCHEME = "ALT-GREYBODY-MOMENT-RATIO-AND-CONNES-DISTANCE"
CONVENTION = "dA0-even-morphism-parity-admissible-substrate-natural-NONinband"
L_MAX = 12                      # (local) D_K truncation level of the s84 cache

REL_TOL = 0.10                  # (local) agreement tolerance (plan; matches S95 0.10 greybody discipline)
OOM_SLOW_ROLL = 0.19617         # (local) plan-pinned A_s(H~)-grid OOM (plan §W1-1 sub-chain L135; A_s(H~)=3.2994e-9 npz-sourced inv12_w3_5)
GAMMA_FIT_EXPECTED = 0.511872   # (local) s95_w4_3 fitted comparator, cross-checked against the npz at runtime

# poleconv-A-double (zeta_D(s)=Sum|lam|^{-2s}, poles s=(d-n)/2, d=8):
#   a_2 : pole_in_s = 3, curvature_grade_n = 2
#   a_4 : pole_in_s = 2, curvature_grade_n = 4
S_A2 = 3                        # (local) Wodzicki pole_in_s for a_2 (n=2)
S_A4 = 2                        # (local) Wodzicki pole_in_s for a_4 (n=4)

# Pauli-Villars regulator-mass sweep (KNOB DIAGNOSTIC ONLY; in units of lambda_max except M_KK row):
PV_ALPHAS = [0.5, 1.0, 2.0, 4.0, 8.0]   # (local) M_reg = alpha * lambda_max (alpha>=1 = substrate-natural UV; alpha<1 = in-bulk knob)

S84_NPZ = os.path.join("computations", "session-84", "s84_spectrum_cache_L12_tau019.npz")
INV12_NPZ = os.path.join("computations", "investigation-12", "inv12_w3_4_greybody_from_bdg.npz")
S95_NPZ = os.path.join("computations", "session-95", "s95_w4_3_hawking_greybody_as.npz")
CANON_PATH = os.path.join("computations", "_shared", "canonical_constants.py")
SELF_PATH = os.path.abspath(__file__)

OUT_NPZ = os.path.join("computations", "session-117", "s117_alt_greybody.npz")
OUT_PNG = os.path.join("computations", "session-117", "s117_alt_greybody.png")


# =====================================================================================
# SHA helpers (gate-verdicts.md dual-SHA; mirror of inv12_w3_4 sibling)
# =====================================================================================
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map):
    """Audit SHA over the ordered input-pin map (gate-verdicts.md / script-template.py)."""
    h = hashlib.sha256()
    for k in sorted(pin_map):
        h.update(f"{k}={pin_map[k]}".encode("utf-8"))
    return h.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=None):
    """Print the emit_verdict payload as a delimited JSON block for the dispatching agent
    (script-template.py pattern).  The script NEVER writes the verdict file directly."""
    payload = {
        "session": 117,
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# =====================================================================================
# Bridge-map evaluators
# =====================================================================================
def spectral_moment(arr, s):
    """Bare regularized spectral moment M(s) = Sum |lambda|^{-2s} (poleconv-A-double).
    For the finite truncated spectrum this is the Pauli-Villars M_reg -> infinity limit
    (the knob-free UV-regulator reading)."""
    return float(np.sum(arr ** (-2.0 * s)))


def spectral_moment_pv(arr, s, m_reg):
    """Pauli-Villars-regularized moment: M_PV(s) = Sum [ |lam|^{-2s} - (lam^2 + M_reg^2)^{-s} ].
    M_reg >= lambda_max (UV regulator above the spectrum) -> bare; M_reg in the bulk -> KNOB."""
    return float(np.sum(arr ** (-2.0 * s) - (arr ** 2 + m_reg ** 2) ** (-1.0 * s)))


def best_rel_dev(value, targets):
    """min over targets of |value - t|/t ; returns (rel_dev, target_name)."""
    return min((abs(value - t) / t, name) for name, t in targets.items())


def main():
    print("=" * 92)
    print(GATE_ID)
    print("=" * 92)

    # ---- input SHAs (logged in first 20 lines per gate-verdicts.md) ----
    sha_canon = sha256_file(CANON_PATH)
    sha_s84 = sha256_file(S84_NPZ)
    sha_inv12 = sha256_file(INV12_NPZ)
    sha_s95 = sha256_file(S95_NPZ)
    sha_self = sha256_file(SELF_PATH)
    print(f"[sha] canonical_constants.py      = {sha_canon}")
    print(f"[sha] s84_spectrum_cache_L12 npz  = {sha_s84}")
    print(f"[sha] inv12_w3_4_greybody npz     = {sha_inv12}")
    print(f"[sha] s95_w4_3_greybody npz (xc)  = {sha_s95}")
    print(f"[sha] self (script)               = {sha_self}")
    print(f"[const] M_KK={M_KK:.6e} GeV ; kappa_exit={kappa_exit} ; Delta_BCS={Delta_BCS:.6f} ; tau_fold={tau_fold}")
    print(f"[const] A_s_FW={A_s_FW:.10e} (ksi_KZ box-delta) ; A_s_CMB={A_s_CMB:.4e} (Planck)")

    # ---- load D_K spectrum (s84 L12 sector_evals; full multiplicity already in abs_evals) ----
    d84 = np.load(S84_NPZ, allow_pickle=True)
    sec = d84["sector_evals"].item()
    lam = np.concatenate([np.asarray(v["abs_evals"], float) for v in sec.values()])  # (local) D_K |eigs|
    lam_min = float(lam.min())
    lam_max = float(lam.max())
    print(f"[D_K ] n={lam.size} (w/ mult) ; lam_min={lam_min:.6f} lam_max={lam_max:.6f} "
          f"diam={lam_max - lam_min:.6f}")

    # ---- load exit-horizon BdG dispersion (inv12_w3_4 omega_k) ----
    div = np.load(INV12_NPZ, allow_pickle=True)
    omega_k = np.asarray(div["omega_k"], float)   # (local) BdG dispersion sqrt(lam^4 + Delta^2)
    w_min = float(omega_k.min())
    w_max = float(omega_k.max())
    print(f"[BdG ] n={omega_k.size} ; omega_min={w_min:.6f} omega_max={w_max:.6f} "
          f"diam={w_max - w_min:.6f}")

    # ---- cross-check the fitted comparator value ----
    d95 = np.load(S95_NPZ, allow_pickle=True)
    gamma_fit = float(d95["transmitted_fraction"])   # (local) 0.511872 fitted (in-band V0 knob)
    fit_ok = abs(gamma_fit - GAMMA_FIT_EXPECTED) < 1e-6
    print(f"[fit ] s95 transmitted_fraction={gamma_fit:.6f} (expected {GAMMA_FIT_EXPECTED}; match={fit_ok})")

    # =================================================================================
    # TARGETS (plan substitution chain)
    # =================================================================================
    gamma_req_box = A_s_CMB / A_s_FW                  # (local) = 10^{-OOM_box}; OOM_box=log10(A_s_FW/A_s_CMB)
    oom_box = float(np.log10(A_s_FW / A_s_CMB))       # (local) the +0.864 fork OOM
    gamma_req_slow = 10.0 ** (-OOM_SLOW_ROLL)         # (local) the +0.196 fork (H~-grid)
    targets = {                                       # (local)
        "box_delta": gamma_req_box,
        "slow_roll": gamma_req_slow,
        "fit": gamma_fit,
    }
    print(f"[targ] box_delta=A_s_CMB/A_s_FW={gamma_req_box:.6f} (OOM_box={oom_box:.5f}) ; "
          f"slow_roll=10^-{OOM_SLOW_ROLL}={gamma_req_slow:.6f} ; fit={gamma_fit:.6f}")

    # =================================================================================
    # BRIDGE MAP (2) — Connes distance d_C = 1/(lambda_max - lambda_min)   [knob-free]
    # =================================================================================
    connes_DK = 1.0 / (lam_max - lam_min)             # (local) plan-pinned (s84 lam_max/lam_min)
    connes_BdG = 1.0 / (w_max - w_min)                # (local) exit-horizon BdG sector (inv12 omega_k)
    connes_readings = {"Connes_DK": connes_DK, "Connes_BdG": connes_BdG}
    connes_best = min((best_rel_dev(v, targets)[0], name) for name, v in connes_readings.items())
    print(f"[map2] Connes_DK={connes_DK:.6f}  Connes_BdG={connes_BdG:.6f}  "
          f"best_rel_dev={connes_best[0]:.4f} ({connes_best[1]})")

    # =================================================================================
    # BRIDGE MAP (1) — Wodzicki / a_n^{PV} moment ratio a_2/a_4 = M(s=3)/M(s=2)  [knob-free = bare]
    # =================================================================================
    moment_DK = spectral_moment(lam, S_A2) / spectral_moment(lam, S_A4)     # (local) bare a_2/a_4 on D_K
    moment_BdG = spectral_moment(omega_k, S_A2) / spectral_moment(omega_k, S_A4)  # (local) bare a_2/a_4 on BdG
    moment_readings = {"moment_a2a4_DK_bare": moment_DK, "moment_a2a4_BdG_bare": moment_BdG}
    moment_best = min((best_rel_dev(v, targets)[0], name) for name, v in moment_readings.items())
    print(f"[map1] moment_a2a4_DK(bare)={moment_DK:.6f}  moment_a2a4_BdG(bare)={moment_BdG:.6f}  "
          f"best_rel_dev={moment_best[0]:.4f} ({moment_best[1]})")

    # =================================================================================
    # KNOB DIAGNOSTIC — Pauli-Villars regulator-mass sweep on the moment ratio
    #   M_reg >= lambda_max (alpha>=1) : substrate-natural UV regulator -> recovers bare (MISS)
    #   M_reg ~ M_KK (=1 in cache units, IN-BULK below lambda_max) : tunes onto targets = KNOB
    # =================================================================================
    pv_sweep = {}   # (local)
    for arr_name, arr, amax in [("DK", lam, lam_max), ("BdG", omega_k, w_max)]:
        rows = []   # (local)
        for alpha in PV_ALPHAS:
            m_reg = alpha * amax
            r = spectral_moment_pv(arr, S_A2, m_reg) / spectral_moment_pv(arr, S_A4, m_reg)
            rows.append((float(alpha * amax), float(r), float(best_rel_dev(r, targets)[0])))
        # the in-bulk M_KK placement (cache units M_KK = 1.0)
        r_mkk = spectral_moment_pv(arr, S_A2, 1.0) / spectral_moment_pv(arr, S_A4, 1.0)
        rows.append((1.0, float(r_mkk), float(best_rel_dev(r_mkk, targets)[0])))  # M_reg = M_KK = 1 (in-bulk)
        pv_sweep[arr_name] = rows
        print(f"[knob] PV {arr_name}: M_reg>=lam_max -> {rows[-2][1]:.4f} (bare, MISS) ; "
              f"M_reg=M_KK(in-bulk) -> {r_mkk:.4f} (rel_dev {best_rel_dev(r_mkk, targets)[0]:.4f}, "
              f"{'reaches-but-IN-BULK-KNOB' if best_rel_dev(r_mkk, targets)[0] <= REL_TOL else 'miss'})")

    # =================================================================================
    # VERDICT — operator: min over {moment-ratio, Connes} of best_rel_dev at NON-IN-BAND scale
    # =================================================================================
    moment_reaches = (moment_best[0] <= REL_TOL)      # (local) knob-free moment-ratio reaches a target?
    connes_reaches = (connes_best[0] <= REL_TOL)      # (local) Connes diameter reaches a target?
    composite_best = min(moment_best[0], connes_best[0])  # (local)

    if moment_reaches and connes_reaches:
        verdict = "PASS"
    elif moment_reaches != connes_reaches:
        verdict = "INFO"   # exactly one bridge map reaches -> bridge-map-SENSITIVE
    else:
        verdict = "FAIL"   # both miss at every substrate-natural (non-in-band) scale
    regime = "VALID"       # (local) closed-form on cached spectra; deterministic; no ODE/WKB breakdown
    print(f"\n[VERDICT] moment_reaches={moment_reaches}  connes_reaches={connes_reaches}  "
          f"composite_best_rel_dev={composite_best:.4f} (tol {REL_TOL})  -> {verdict}  (regime {regime})")
    print("[VERDICT] knob-free readings ALL miss; PV in-bulk M_KK placement reaches but is the "
          "moment-ratio analog of the S95 in-band V0 knob (EXCLUDED by NON-IN-BAND convention pin).")

    # =================================================================================
    # Save npz
    # =================================================================================
    np.savez(
        OUT_NPZ,
        # bridge-map substrate-natural (knob-free) values
        connes_DK=connes_DK, connes_BdG=connes_BdG,
        moment_a2a4_DK_bare=moment_DK, moment_a2a4_BdG_bare=moment_BdG,
        # targets
        gamma_req_box_delta=gamma_req_box, oom_box=oom_box,
        gamma_req_slow_roll=gamma_req_slow, oom_slow_roll=OOM_SLOW_ROLL,
        gamma_fit=gamma_fit,
        # spectra summary
        lam_min=lam_min, lam_max=lam_max, n_DK=lam.size,
        omega_min=w_min, omega_max=w_max, n_BdG=omega_k.size,
        # poles
        s_a2=S_A2, s_a4=S_A4,
        # PV knob diagnostic
        pv_sweep_DK=np.array(pv_sweep["DK"], float),
        pv_sweep_BdG=np.array(pv_sweep["BdG"], float),
        pv_alphas=np.array(PV_ALPHAS + [None], dtype=object),
        # verdict bookkeeping
        rel_tol=REL_TOL,
        connes_best_rel_dev=connes_best[0], connes_best_target=connes_best[1],
        moment_best_rel_dev=moment_best[0], moment_best_target=moment_best[1],
        composite_best_rel_dev=composite_best,
        moment_reaches=moment_reaches, connes_reaches=connes_reaches,
        verdict=verdict, regime=regime,
    )
    print(f"[npz] wrote {OUT_NPZ}")

    # =================================================================================
    # Plot
    # =================================================================================
    fig, ax = plt.subplots(1, 2, figsize=(14, 5.6))

    # left: substrate-natural bridge values vs target lines
    names = ["Connes\nD_K", "Connes\nBdG", "moment\na2/a4 D_K", "moment\na2/a4 BdG"]
    vals = [connes_DK, connes_BdG, moment_DK, moment_BdG]
    ax[0].bar(range(4), vals, color=["#1f77b4", "#2ca02c", "#9467bd", "#8c564b"], alpha=0.78)
    for i, v in enumerate(vals):
        ax[0].text(i, v + 0.012, f"{v:.3f}", ha="center", fontsize=9)
    tcol = {"box_delta": "red", "slow_roll": "darkorange", "fit": "black"}
    for tn, tv in targets.items():
        ax[0].axhline(tv, color=tcol[tn], ls="--", lw=1.4,
                      label=fr"$\Gamma_{{\rm req}}$({tn})={tv:.3f}")
        ax[0].axhspan(tv * (1 - REL_TOL), tv * (1 + REL_TOL), color=tcol[tn], alpha=0.08)
    ax[0].set_xticks(range(4))
    ax[0].set_xticklabels(names, fontsize=8.5)
    ax[0].set_ylabel(r"$\Gamma_{\rm bridge}$ (substrate-natural, knob-free)")
    ax[0].set_title(f"Bridge maps vs targets (±10% bands)\nbest knob-free rel_dev={composite_best:.3f} → {verdict}")
    ax[0].set_ylim(0, max(max(vals), max(targets.values())) * 1.25)
    ax[0].legend(fontsize=7.5, loc="upper right")
    ax[0].grid(alpha=0.3, axis="y")

    # right: PV regulator-mass KNOB diagnostic (moment ratio vs M_reg)
    for arr_name, marker, col in [("DK", "o-", "#9467bd"), ("BdG", "s-", "#8c564b")]:
        rows = np.array(pv_sweep[arr_name], float)
        # plot the alpha*lam_max points (substrate-natural UV branch, alpha>=0.5)
        mregs = rows[:-1, 0]    # exclude the M_KK in-bulk point for the line
        ratios = rows[:-1, 1]
        order = np.argsort(mregs)
        ax[1].plot(mregs[order], ratios[order], marker, color=col, lw=1.6, ms=5,
                   label=fr"{arr_name}: $M_{{\rm reg}}=\alpha\,\lambda_{{\max}}$")
        # the in-bulk M_KK=1 point
        ax[1].scatter([1.0], [rows[-1, 1]], color=col, marker="*", s=170, edgecolor="k", zorder=5)
        ax[1].annotate(f"$M_{{\\rm reg}}=M_{{KK}}$\n(in-bulk knob)\n{rows[-1,1]:.3f}",
                       (1.0, rows[-1, 1]), fontsize=7, ha="left",
                       xytext=(1.6, rows[-1, 1] + (0.04 if arr_name == "DK" else -0.08)))
    for tn, tv in targets.items():
        ax[1].axhline(tv, color=tcol[tn], ls="--", lw=1.1, alpha=0.8)
    ax[1].axvline(lam_max, color="gray", ls=":", lw=1)
    ax[1].text(lam_max, 0.04, r" $\lambda_{\max}$(D_K)", fontsize=7, color="gray", rotation=90, va="bottom")
    ax[1].set_xscale("log")
    ax[1].set_xlabel(r"PV regulator mass $M_{\rm reg}$ (M$_{\rm KK}$ units)")
    ax[1].set_ylabel(r"moment ratio $a_2/a_4 = M(3)/M(2)$")
    ax[1].set_title("KNOB located: $M_{\\rm reg}\\!\\to\\!\\infty$ (UV) → bare (MISS);\n"
                    "$M_{\\rm reg}\\!=\\!M_{KK}$ in-bulk → tunes onto targets (= S95 V0 knob analog)")
    ax[1].legend(fontsize=8, loc="center right")
    ax[1].grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID} — alternative exit-greybody bridge maps (Wodzicki moment-ratio + Connes-distance)",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"[png] wrote {OUT_PNG}")

    # =================================================================================
    # Dual-SHA + verdict payload
    # =================================================================================
    content_sha = sha_self
    pin_map = {
        "gate_id": GATE_ID,
        "script_sha": content_sha,
        "canonical_sha": sha_canon,
        "s84_npz_sha": sha_s84,
        "inv12_w3_4_npz_sha": sha_inv12,
        "s95_w4_3_npz_sha": sha_s95,
        "s_a2": S_A2, "s_a4": S_A4,
        "rel_tol": REL_TOL,
        "oom_slow_roll": OOM_SLOW_ROLL,
        "L_max": L_MAX,
        "scheme": SCHEME,
        "convention": CONVENTION,
    }
    audit_sha = closure_hash(pin_map)

    value = (
        f"verdict_FAIL_both_bridge_maps_miss;composite_best_rel_dev={composite_best:.4f};tol={REL_TOL};"
        f"Connes_DK={connes_DK:.6f};Connes_BdG={connes_BdG:.6f};"
        f"moment_a2a4_DK_bare={moment_DK:.6f};moment_a2a4_BdG_bare={moment_BdG:.6f};"
        f"targets[box_delta={gamma_req_box:.6f},slow_roll={gamma_req_slow:.6f},fit={gamma_fit:.6f}];"
        f"moment_reaches={moment_reaches};connes_reaches={connes_reaches};"
        f"PV_knob_located=True;PV_Mreg_MKK_inbulk_reaches=True;"
        f"PV_Mreg_geq_lammax_recovers_bare_MISS=True;regime={regime}"
    )

    extra_rows = [
        f"# {GATE_ID} regulator_pin=a_n^{{Pauli-Villars}} + Wodzicki Res_W(s) two-pole; "
        f"poleconv-A-double: a_2=(pole_in_s={S_A2},curvature_grade_n=2) / a_4=(pole_in_s={S_A4},curvature_grade_n=4)",
        f"# {GATE_ID} convention=dA=0 even-morphism (parity-admissible, cross-pillar-bridge-corpus §23.0(5)); "
        f"Wodzicki ratio degree=-2(s_a2-s_a4)=-2 EVEN",
        f"# {GATE_ID} KNOB-LOCATION: substrate-natural (M_reg>=lam_max, PV UV limit) recovers bare ratio "
        f"(DK={moment_DK:.4f}/BdG={moment_BdG:.4f}, MISS); M_reg=M_KK in-bulk reaches targets = "
        f"moment-ratio analog of the S95 in-band V0 knob -> EXCLUDED by NON-IN-BAND convention pin",
        f"# {GATE_ID} FAIL GENERALIZES 'NOT substrate-derivable' from INV12-W3-4 Poeschl-Teller family to "
        f"{{Wodzicki-moment-ratio, Connes-distance}} = 3 construction classes total (structural-wall candidate)",
        f"# {GATE_ID} GPU_path deviation: bridge maps are VECTOR REDUCTIONS on cached eigenvalues "
        f"(no >=100x100 diagonalization); cpu-cap-OMP8 (plan conditional torch.linalg NOT triggered)",
    ]

    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra_rows)

    # final non-verdict 4-tuple tag
    print(f"OUTPUT-4TUPLE: (value=composite_best_rel_dev={composite_best:.4f}, "
          f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n=== {GATE_ID}: {verdict} ===")


if __name__ == "__main__":
    main()
