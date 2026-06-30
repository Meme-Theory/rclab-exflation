#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S116-W7-STATEPROJ-BCS — substrate-IS STATE-PROJ observable R_STATE = (a-b)/(a+b)
from the 3He-B BdG BCS condensation-energy state-pair functional, with the
LOAD-BEARING Track-A/B provenance discriminator on the controlling gap ratio.

SUBSTRATE FRAMING (phononic-framing.md; 3HeB-inheritance-canonical.md):
  The substrate IS the BdG BCS ground state on (A_K, H_K, D_K). The 3He-B cell
  is NOT a container the substrate lives in but a CONTROLLED REALIZATION of the
  same BDI universality class via the parent->child inheritance morphism
  iota : C (+) H (+) M3(C) -> M2(C) (NOT analogy). Direction of explanation:
    D_K eigenvalues
      -> BdG occupation v_k^2 in the BCS state
      -> condensation-energy state-pair functional  a = rho_BCS(P_A . H_pair),
                                                     b = rho_BCS(P_B . H_pair)
      -> R_STATE = (a - b)/(a + b)
      -> the lab MEASURES R_3HeB_lit = (Delta_A^2 - Delta_B^2)/(Delta_A^2 + Delta_B^2)
         IN the cryostat at the polycritical point (P_pc, T_pc).
  STATE-PROJ is algebra-DEPENDENT (a state-pair functional weighting rho_BCS
  against the sector central projections P_A, P_B), structurally distinct from
  the algebra-INVARIANT OP-PROJ spectrum-only count F({lambda_k, m_k}).

PRIMARY DELIVERABLE: NOT the numerical reproduction of +0.03536 (which the form
  reproduces by construction to machine epsilon) but the PROVENANCE of the
  controlling gap ratio Delta_B/Delta_A:
    Track A = substrate-first q-theory strong-coupling prediction (genuine 0-param)
    Track B = the 3He lab strong-coupling ratio SC_corr_B/SC_corr_A re-expressed
              (a near-tautology, a consistency-check, NOT a prediction).

  composite = PASS iff (3-tuple PASS AND Track A)
  composite = INFO iff (3-tuple PASS AND Track B)
  composite = FAIL iff magnitude FAIL
  (plan-frozen operator precedence, gate-verdicts.md; OVERRIDES generic collapse.)

Gate: S116-W7-STATEPROJ-BCS  | [SIGN] trigger | classification PHONONIC
Plan: sessions/session-plan/session-116-plan-w7.md  S W7-1
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")     # cpu-cap-OMP8 (GPU_path pin)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
# Section 1 — Paths + canonical imports (NEVER hardcode framework constants)
# --------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (          # noqa: E402
    SC_corr_A,            # 3He-A strong-coupling gap enhancement (LAB; Serene-Rainer/Greywall)
    SC_corr_B,            # 3He-B strong-coupling gap enhancement (LAB)
    delta_A_over_kBTc,    # 3He-A reduced gap Delta_A/(k_B T_c) at P_pc (LAB)
    delta_B_over_kBTc,    # 3He-B reduced gap Delta_B/(k_B T_c) at P_pc (LAB)
    P_pc,                 # polycritical pressure (bar) (LAB)
    T_pc,                 # polycritical temperature (K) (LAB)
    R_3HeB_lit,           # lab A/B gap-square asymmetry target (LAB)
    Delta_BCS,            # canonical substrate BCS gap (M_KK units; R-protected)
)

# --------------------------------------------------------------------------
# Section 2 — Gate identity + machinery pins (from plan W7-1 PRDR block)
# --------------------------------------------------------------------------
GATE_ID = "S116-W7-STATEPROJ-BCS"
SESSION = "S116"
SCHEME = "STATE-PROJ-BCS-condensation-energy-state-pair"
CONVENTION = "(a-b)/(a+b)-A-B-coexistence-condensation-energy + STATE-PROJ"
L_MAX = 10                                  # (local) canonical substrate truncation (plan pin)
EULER_GAMMA = 0.5772156649015329            # (local) Euler-Mascheroni (universal math const)
TOL_REL = 5e-2                              # (local) secondary numerical band (plan pin)

INPUT_FILES = [
    Path(__file__).resolve(),
    SHARED_DIR / "canonical_constants.py",
    PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz",
    PROJECT_ROOT / "computations" / "session-87" / "s87_w11_3heb_excess_inheritance_comparison.npz",
    PROJECT_ROOT / "researchers" / "Volovik" / "03_2008_Volovik_Emergent_Physics_Fermi_Point.md",
]
S84_CACHE = INPUT_FILES[2]
S87_NPZ = INPUT_FILES[3]

# OP-PROJ companion reference (algebra-INVARIANT spectrum-only saturation;
# atlas-07 STAGE-1-CANDIDATE) — used only for the SIGN-FLIP structural note.
OP_PROJ_R_INF = -1.892  # (local) atlas-07 STAGE-1-CANDIDATE companion ref, sign-flip note only

# --------------------------------------------------------------------------
# Section 3 — dual-SHA helpers (S84+ schema; mirror script-template.py)
# --------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                    # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                               # (local)
    for p in inputs:
        sha = sha256_of(p)                                  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    h = hashlib.sha256()
    for k, v in sorted(pins.items()):
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        script_bytes = script_path.read_bytes()             # (local)
    except OSError:
        script_bytes = b""                                  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()       # (local)
    except OSError:
        canonical_bytes = b""                               # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    payload = {
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


# --------------------------------------------------------------------------
# Section 4 — substrate BdG occupation moments (state-pair functional cross-check)
# --------------------------------------------------------------------------
def load_substrate_spectrum(cache_path: Path, l_max: int):
    """Flatten the cached D_K(tau_fold) |lambda_k| spectrum over sectors p+q <= l_max."""
    d = np.load(cache_path, allow_pickle=True)
    sector_evals = d["sector_evals"].item()                 # dict {(p,q): {...}}
    xis = []                                                # (local) single-particle |xi_k|
    for (p, q), blk in sector_evals.items():
        if int(blk.get("level", p + q)) <= l_max:
            xis.append(np.asarray(blk["abs_evals"], dtype=float))
    xi = np.concatenate(xis)                                # (local)
    return xi


def bcs_condensation_energy(xi, delta):
    """Standard BCS condensation energy density on a discrete dispersion xi_k.

    E_cond(Delta) = sum_k [ |xi_k| - E_k + Delta^2/(2 E_k) ],  E_k = sqrt(xi_k^2 + Delta^2).
    Leading behavior -> (1/2) N(0) Delta^2 for a flat band near E_F; returns |E_cond|.
    This is the state-pair functional rho_BCS(P_sector . H_pair) realized on the
    substrate BdG occupation v_k^2 = (1/2)(1 - xi_k/E_k).
    """
    Ek = np.sqrt(xi**2 + delta**2)                          # (local) BdG quasiparticle energy
    e_cond = np.sum(np.abs(xi) - Ek + delta**2 / (2.0 * Ek))  # (local)
    return abs(e_cond)


# --------------------------------------------------------------------------
# Section 5 — Compute
# --------------------------------------------------------------------------
def compute() -> dict:
    out = {}

    # ----- weak-coupling BCS prefactor (universal; CANCELS in the ratio) -----
    pi_e_neg_gamma = np.pi * np.exp(-EULER_GAMMA)           # (local) = 1.763877...
    out["pi_e_neg_gamma"] = pi_e_neg_gamma

    # ----- the two inherited gap sectors at A-B coexistence (k_B T_c units) ---
    # Delta_sector = (pi e^-gamma) * SC_sector ; weak-coupling factor x strong-coupling correction
    Delta_A = pi_e_neg_gamma * SC_corr_A                    # (local)
    Delta_B = pi_e_neg_gamma * SC_corr_B                    # (local)
    out["Delta_A_kBTc"] = Delta_A
    out["Delta_B_kBTc"] = Delta_B
    out["gap_ratio_B_over_A"] = Delta_B / Delta_A           # = SC_corr_B/SC_corr_A

    # ----- closed-form condensation-energy state-pair functional --------------
    # a = |E_cond^A| = (1/2) N(0) Delta_A^2 ; b = (1/2) N(0) Delta_B^2 ; N(0) common -> cancels
    N0 = 1.0                                                # (local) common DOS at coexistence (cancels)
    a_closed = 0.5 * N0 * Delta_A**2                        # (local) A-sector condensation weight
    b_closed = 0.5 * N0 * Delta_B**2                        # (local) B-sector condensation weight
    R_STATE = (a_closed - b_closed) / (a_closed + b_closed)  # (local) PRIMARY observable
    out["a_closed"] = a_closed
    out["b_closed"] = b_closed
    out["R_STATE"] = R_STATE

    # Equivalent reductions (all identical algebra; the (1/2)N(0) and (pi e^-g)^2 cancel)
    R_from_SC = (SC_corr_A**2 - SC_corr_B**2) / (SC_corr_A**2 + SC_corr_B**2)   # (local)
    R_from_dkt = (delta_A_over_kBTc**2 - delta_B_over_kBTc**2) \
        / (delta_A_over_kBTc**2 + delta_B_over_kBTc**2)                          # (local)
    out["R_from_SC"] = R_from_SC
    out["R_from_dkt_4sf"] = R_from_dkt   # 4-sig-fig-rounded reduced gaps (rounding artifact)

    # ----- lab anchor cross-check (from S87 W11-5 npz + canonical) ------------
    s87 = np.load(S87_NPZ, allow_pickle=True)
    R_3HeB_lit_npz = float(s87["R_3HeB_lit"])              # (local)
    R_substrate_OP = float(s87["R_substrate"])            # (local) OP-PROJ spectral count (L=10)
    Delta_A_at_pc_npz = float(s87["Delta_A_at_pc"])       # (local)
    Delta_B_at_pc_npz = float(s87["Delta_B_at_pc"])       # (local)
    out["R_3HeB_lit_npz"] = R_3HeB_lit_npz
    out["R_3HeB_lit_canonical"] = R_3HeB_lit
    out["R_substrate_OP_L10"] = R_substrate_OP
    # confirm the S87 "lab gaps" ARE SC_corr * (pi e^-gamma) -> exposes the tautology
    out["Delta_A_at_pc_npz"] = Delta_A_at_pc_npz
    out["Delta_B_at_pc_npz"] = Delta_B_at_pc_npz
    out["gap_A_equals_SC_A_times_pieg"] = abs(Delta_A - Delta_A_at_pc_npz) / Delta_A_at_pc_npz
    out["gap_B_equals_SC_B_times_pieg"] = abs(Delta_B - Delta_B_at_pc_npz) / Delta_B_at_pc_npz

    # secondary numerical match (vs canonical lab target)
    rel_match = abs(R_STATE - R_3HeB_lit) / abs(R_3HeB_lit)  # (local)
    out["rel_match_vs_lit"] = rel_match

    # ----- substrate BdG-occupation realization (confirms state-pair form) ----
    # Confirms (a-b)/(a+b) is a GENUINE BdG occupation asymmetry on the substrate
    # spectrum, NOT a bare algebraic ratio. The OVERALL gap scale uses the
    # canonical substrate gap Delta_BCS; the A/B modulation uses SC_corr (LAB).
    xi = load_substrate_spectrum(S84_CACHE, L_MAX)        # (local) substrate |xi_k|
    Delta_A_sub = Delta_BCS * SC_corr_A                   # (local) A-sector substrate gap
    Delta_B_sub = Delta_BCS * SC_corr_B                   # (local) B-sector substrate gap
    a_bdg = bcs_condensation_energy(xi, Delta_A_sub)      # (local) rho_BCS(P_A . H_pair)
    b_bdg = bcs_condensation_energy(xi, Delta_B_sub)      # (local) rho_BCS(P_B . H_pair)
    R_BdG = (a_bdg - b_bdg) / (a_bdg + b_bdg)             # (local)
    out["N_substrate_modes"] = int(xi.size)
    out["Delta_A_sub_MKK"] = Delta_A_sub
    out["Delta_B_sub_MKK"] = Delta_B_sub
    out["a_bdg"] = a_bdg
    out["b_bdg"] = b_bdg
    out["R_BdG_occupation"] = R_BdG
    out["R_BdG_minus_R_STATE"] = R_BdG - R_STATE          # finite-DOS-curvature correction

    # ----- PROVENANCE TRACE — THE PRIMARY DELIVERABLE ------------------------
    # Trace EVERY factor in Delta_B/Delta_A.
    provenance = {
        "pi_e_neg_gamma": "UNIVERSAL weak-coupling BCS prefactor (1.763877); appears in BOTH "
                          "Delta_A and Delta_B and CANCELS in the ratio -> non-discriminating",
        "SC_corr_A": "LABORATORY-IN: 3He-A strong-coupling enhancement 1.151 = "
                     "(Delta_A/k_BT_c)/(pi e^-gamma); 3He spin-fluctuation FEEDBACK set by "
                     "3He Landau parameters (Serene-Rainer 1983 / Greywall 1986). CONTROLLING factor.",
        "SC_corr_B": "LABORATORY-IN: 3He-B strong-coupling enhancement 1.111 (Serene-Rainer/"
                     "Greywall). CONTROLLING factor.",
        "delta_B_over_delta_A": "= SC_corr_B/SC_corr_A = 1.111/1.151 = 0.96525; the index-named "
                                "'delta_B_over_delta_A_q_theory' has STRUCTURE (= 1.9597/2.0302) "
                                "= the LAB reduced-gap ratio. NAME != PROVENANCE.",
    }
    out["provenance"] = provenance

    # Is there an INDEPENDENT substrate-first prediction of SC_corr_B/SC_corr_A?
    # Substrate-physics determination (volovik authority):
    #   (i)   substrate is a single BDI object (3He-B child, N_3=0); NO intrinsic 3He-A
    #         (DIII, N_3=2) sector -> no substrate-first Delta_A.
    #   (ii)  SC corrections are 3He material properties (Fermi-liquid feedback), NOT substrate
    #         outputs; Delta_BCS=0.4642547 is a SINGLE gap, does not split into A/B with 3He feedback.
    #   (iii) Volovik q-theory governs the vacuum 4-form / CC (DILUTION-CC), NOT the superfluid
    #         gap-anisotropy strong-coupling; the 'q_theory' name is aspirational.
    substrate_first_SC_ratio_available = False
    out["substrate_first_SC_ratio_available"] = substrate_first_SC_ratio_available
    out["track"] = "A" if substrate_first_SC_ratio_available else "B"

    # ----- [SIGN] 3-tuple ----------------------------------------------------
    # sign: predicted R_STATE > 0 (SC_A > SC_B) ; computed sign
    sign_ok = (SC_corr_A > SC_corr_B) and (R_STATE > 0.0)
    out["sign_verdict"] = "PASS" if sign_ok else "FAIL"
    # magnitude: |R_STATE - R_3HeB_lit|/|R_3HeB_lit| vs 0.05 band
    out["magnitude_verdict"] = "PASS" if rel_match <= TOL_REL else (
        "INFO" if rel_match <= 0.25 else "FAIL")
    # regime: single-point polycritical (P_pc, T_pc); closed form exact at common-N(0) coexistence
    out["regime_verdict"] = "VALID"

    # ----- composite under PLAN-FROZEN precedence (dual_prior track) ----------
    three_tuple_pass = (out["sign_verdict"] == "PASS" and out["magnitude_verdict"] == "PASS")
    if out["magnitude_verdict"] == "FAIL":
        composite = "FAIL"
    elif three_tuple_pass and out["track"] == "A":
        composite = "PASS"
    elif three_tuple_pass and out["track"] == "B":
        composite = "INFO"
    else:
        composite = "INFO"
    out["composite"] = composite

    return out


# --------------------------------------------------------------------------
# Section 6 — Plot
# --------------------------------------------------------------------------
def make_plot(out, png_path: Path):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1 — sign flip: STATE-PROJ (+) vs OP-PROJ (-)
    ax = axes[0]
    vals = [out["R_STATE"], OP_PROJ_R_INF]
    labels = ["STATE-PROJ\n(a-b)/(a+b)\nalgebra-DEPENDENT", "OP-PROJ\nR_inf\nalgebra-INVARIANT"]
    colors = ["#1a9850", "#d73027"]
    bars = ax.bar(labels, vals, color=colors, width=0.55)
    ax.axhline(0, color="k", lw=0.8)
    ax.set_ylabel("R observable")
    ax.set_title("SIGN FLIP (structural input to W7-2)\nSTATE-PROJ +0.0354  vs  OP-PROJ -1.892")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + (0.05 if v > 0 else -0.12),
                f"{v:+.4f}", ha="center", fontsize=10, fontweight="bold")
    ax.set_ylim(-2.1, 0.4)

    # Panel 2 — provenance decomposition of Delta_B/Delta_A
    ax = axes[1]
    ax.axis("off")
    txt = (
        "PROVENANCE of  Delta_B/Delta_A = SC_corr_B/SC_corr_A\n"
        "----------------------------------------------------\n"
        f"pi e^-gamma = {out['pi_e_neg_gamma']:.6f}\n"
        "   UNIVERSAL weak-coupling BCS; CANCELS in ratio\n\n"
        f"SC_corr_A = {SC_corr_A}   <-- LAB (Serene-Rainer/Greywall)\n"
        f"SC_corr_B = {SC_corr_B}   <-- LAB (Serene-Rainer/Greywall)\n"
        f"   Delta_B/Delta_A = {out['gap_ratio_B_over_A']:.6f}\n\n"
        "substrate-first SC ratio available?  NO\n"
        "  (i)   substrate = single BDI 3He-B child (N_3=0);\n"
        "        no intrinsic 3He-A (DIII, N_3=2) sector\n"
        "  (ii)  SC = 3He Fermi-liquid feedback (material);\n"
        "        Delta_BCS is ONE gap, no A/B split\n"
        "  (iii) q-theory = vacuum 4-form/CC, NOT gap anisotropy\n\n"
        f"==>  TRACK {out['track']}  (lab SC ratio re-expressed)"
    )
    ax.text(0.02, 0.98, txt, va="top", ha="left", family="monospace", fontsize=9.5,
            transform=ax.transAxes)
    ax.set_title("Track-A/B discriminator (the PRIMARY deliverable)")

    # Panel 3 — tautology: R_STATE vs R_3HeB_lit (machine-eps match)
    ax = axes[2]
    ax.axis("off")
    txt2 = (
        "NEAR-TAUTOLOGICAL numerical match\n"
        "----------------------------------\n"
        f"R_STATE          = {out['R_STATE']:+.12f}\n"
        f"R_3HeB_lit (canon)= {out['R_3HeB_lit_canonical']:+.12f}\n"
        f"R_3HeB_lit (S87)  = {out['R_3HeB_lit_npz']:+.12f}\n"
        f"rel |match|       = {out['rel_match_vs_lit']:.2e}\n\n"
        "WHY exact: BOTH are (SC_A^2-SC_B^2)/(SC_A^2+SC_B^2)\n"
        "from the SAME two lab numbers -> 0 independent bits.\n\n"
        "S87 lab gaps ARE SC_corr * pi e^-gamma:\n"
        f"  rel(Delta_A) = {out['gap_A_equals_SC_A_times_pieg']:.1e}\n"
        f"  rel(Delta_B) = {out['gap_B_equals_SC_B_times_pieg']:.1e}\n\n"
        "substrate BdG-occupation realization (form check):\n"
        f"  N_modes(p+q<=10) = {out['N_substrate_modes']}\n"
        f"  R_BdG_occupation = {out['R_BdG_occupation']:+.6f}\n"
        f"  R_BdG - R_STATE  = {out['R_BdG_minus_R_STATE']:+.2e}\n"
        "  -> (a-b)/(a+b) IS a genuine state-pair functional\n\n"
        f"COMPOSITE = {out['composite']}  "
        f"(3-tuple {out['sign_verdict']}/{out['magnitude_verdict']}/{out['regime_verdict']}, Track {out['track']})"
    )
    ax.text(0.02, 0.98, txt2, va="top", ha="left", family="monospace", fontsize=9.5,
            transform=ax.transAxes)
    ax.set_title("Tautology + BdG realization")

    fig.suptitle(
        f"{GATE_ID}: STATE-PROJ R_STATE = (a-b)/(a+b) = "
        f"{out['R_STATE']:+.6f}  [Track {out['track']} -> {out['composite']}]",
        fontsize=12, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(png_path, dpi=130)
    plt.close(fig)


# --------------------------------------------------------------------------
# Section 7 — Main
# --------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                       # (local)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    out = compute()

    print("=== RESULTS ===")
    for k in ("R_STATE", "R_from_SC", "R_from_dkt_4sf", "R_3HeB_lit_canonical",
              "R_3HeB_lit_npz", "rel_match_vs_lit", "gap_ratio_B_over_A",
              "gap_A_equals_SC_A_times_pieg", "gap_B_equals_SC_B_times_pieg",
              "R_substrate_OP_L10", "N_substrate_modes", "R_BdG_occupation",
              "R_BdG_minus_R_STATE", "substrate_first_SC_ratio_available", "track",
              "sign_verdict", "magnitude_verdict", "regime_verdict", "composite"):
        print(f"  {k:32s} = {out[k]}")
    print()
    print("  PROVENANCE TRACE (Delta_B/Delta_A factor-by-factor):")
    for k, v in out["provenance"].items():
        print(f"    - {k}: {v}")
    print()

    png_path = script_path.with_suffix(".png")
    make_plot(out, png_path)
    npz_path = script_path.with_suffix(".npz")
    np.savez(
        npz_path,
        R_STATE=out["R_STATE"],
        R_from_SC=out["R_from_SC"],
        R_from_dkt_4sf=out["R_from_dkt_4sf"],
        R_3HeB_lit_canonical=out["R_3HeB_lit_canonical"],
        R_3HeB_lit_npz=out["R_3HeB_lit_npz"],
        rel_match_vs_lit=out["rel_match_vs_lit"],
        gap_ratio_B_over_A=out["gap_ratio_B_over_A"],
        pi_e_neg_gamma=out["pi_e_neg_gamma"],
        Delta_A_kBTc=out["Delta_A_kBTc"],
        Delta_B_kBTc=out["Delta_B_kBTc"],
        gap_A_equals_SC_A_times_pieg=out["gap_A_equals_SC_A_times_pieg"],
        gap_B_equals_SC_B_times_pieg=out["gap_B_equals_SC_B_times_pieg"],
        a_closed=out["a_closed"], b_closed=out["b_closed"],
        R_substrate_OP_L10=out["R_substrate_OP_L10"],
        OP_PROJ_R_INF=OP_PROJ_R_INF,
        N_substrate_modes=out["N_substrate_modes"],
        Delta_A_sub_MKK=out["Delta_A_sub_MKK"], Delta_B_sub_MKK=out["Delta_B_sub_MKK"],
        a_bdg=out["a_bdg"], b_bdg=out["b_bdg"],
        R_BdG_occupation=out["R_BdG_occupation"],
        R_BdG_minus_R_STATE=out["R_BdG_minus_R_STATE"],
        substrate_first_SC_ratio_available=out["substrate_first_SC_ratio_available"],
        track=out["track"],
        sign_verdict=out["sign_verdict"], magnitude_verdict=out["magnitude_verdict"],
        regime_verdict=out["regime_verdict"], composite=out["composite"],
        SC_corr_A=SC_corr_A, SC_corr_B=SC_corr_B, P_pc=P_pc, T_pc=T_pc, Delta_BCS=Delta_BCS,
        audit_sha256=audit_sha, content_sha256=content_sha,
        provenance_json=json.dumps(out["provenance"]),
    )
    print(f"  wrote {npz_path.name}, {png_path.name}")
    print()

    # ----- value payload (no apostrophes; emit_verdict wraps value='...') -----
    value = (
        f"R_STATE={out['R_STATE']:+.7f}_TRACK={out['track']}_lab-SC-ratio-re-expressed_"
        f"relmatch={out['rel_match_vs_lit']:.1e}_NEAR-TAUTOLOGY_"
        f"sign=POS_vs_OP-PROJ_Rinf={OP_PROJ_R_INF}_NEG_SIGNFLIP_"
        f"substrate-first-SC-ratio_UNAVAILABLE_BDI-single-3HeB-child_no-A-sector"
    )

    extra_rows = [
        "# composite-precedence: dual_prior-track-discriminator (W7-1; "
        "generic-collapse PASS overridden to INFO under Track B)",
        f"# provenance: Delta_B/Delta_A = SC_corr_B/SC_corr_A = {out['gap_ratio_B_over_A']:.6f} "
        f"= LAB (Serene-Rainer 1983 / Greywall 1986); pi e^-gamma cancels; "
        f"substrate-first SC ratio UNAVAILABLE (single BDI 3He-B child, N_3=0, no A-sector) -> Track B",
        f"# BdG-occupation realization: R_BdG={out['R_BdG_occupation']:+.6f} on {out['N_substrate_modes']} "
        f"substrate modes (p+q<=10) confirms (a-b)/(a+b) is a genuine state-pair functional "
        f"(rho_BCS(P_sector.H_pair)); R_BdG-R_STATE={out['R_BdG_minus_R_STATE']:+.2e}",
    ]

    print_verdict_payload(
        verdict=out["composite"],
        value=value,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_verdict=out["sign_verdict"],
        magnitude_verdict=out["magnitude_verdict"],
        regime_verdict=out["regime_verdict"],
        companion_note="Track B: gap ratio is lab SC ratio re-expressed (near-tautology); "
                       "slot REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION; CF-S117-STATEPROJ-SC-FROM-SUBSTRATE",
        extra_rows=extra_rows,
    )

    print(f"\n  elapsed {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
