#!/usr/bin/env python3
"""
S116 W3-2 — S116-W3-GOLDSTONE-M2 — surviving non-Imry-Ma Goldstone-mass
candidate (Cheeger / lattice-Laplacian connectivity gap) + Josephson-graph ceiling
=================================================================================

Gate: S116-W3-GOLDSTONE-M2  ([SIGN] trigger)
Classification: PHONONIC

Pre-registered threshold (plan session-116-plan-w3.md §W3-2):
  frac170 = m_G^mechanism / (170 * Delta_BCS) vs the target 1.0, against the
  Josephson-graph ceiling frac170_ceiling = J_C2/(170*Delta_BCS).
    PASS iff frac170 >= 0.5
    FAIL iff frac170 <= frac170_ceiling_family (= inv5 construction-E reload,
            = J_C2/(170*Delta_BCS) ~ 0.01182) -> structural closure
    INFO iff frac170_ceiling_family < frac170 < 0.5  -> partial survival
  [SIGN] sub-test:  sign(m_G^mechanism - m_G^ImryMa_inv5),  m_IM = 0.003185
  REGIME sub-test:  x_G = (m_G/sqrt(rho_s))/(2 Delta_BCS) < 1 (below pair-breaking edge)

SUBSTRATE FRAMING (PHONONIC)
----------------------------
The U(1)_7 phase Goldstone IS the substrate's broken-phase boson. Two PERMANENT
walls fix the structure:
  wall #5  [iK_7, D_K] = 0  -> the mode is ungaugeable (N4 BROKEN);
  wall #7  SA-mass = 0 EXACT (S48) -> the spectral action CANNOT mass it.
Therefore ANY mass is a GRAPH SPECTRAL MOMENT, not a spectral-action term -- either
the random-field pinning gap (Imry-Ma, inv5 baseline, FAILED) or the lattice-Laplacian
connectivity gap (Cheeger isoperimetric constant) of the SU(3) Josephson tessellation.
Both are built from the SAME couplings {J_C2, J_su2, J_u1}.  Flow:
  D_K (0,0)-sector eigenvalues -> Josephson couplings -> graph Laplacian lambda_1 /
  Imry-Ma pinning -> m_G -> DM structure-formation mass -> halo/LSS (measured).
The 170x "problem" is container-thinking: expecting the substrate's largest internal
coupling (J_C2 ~ 0.93 M_KK ~ 2 Delta_BCS) to supply a mass ~85x ABOVE itself.  A graph
cannot pin its own phase mode harder than its stiffest bond.

METHODOLOGY
-----------
(1) Reload the inv5 disorder bracket (constructions A..E) -> Imry-Ma baseline
    (br_A, m_IM = 0.003185) + the disorder-family ceiling (br_E, m_G = J_C2 = 0.933).
(2) Surviving mechanism = Cheeger / lattice-Laplacian connectivity gap (collab §5):
    (a) closed-form Cheeger lower bound  m_G^Ch >= h(L)/2,  h(L) = 2 J_C2/Vol(cell),
        Vol(cell)=1  =>  m_G^Ch >= J_C2 = 0.933.  The Step-6 coupling-scale ceiling
        (E <= J_C2, xi >= 1 bond) caps it from ABOVE at J_C2 -> the two bounds PINCH
        m_G = J_C2 (the Goldstone global-phase coherence rate = Cheeger bottleneck).
    (b) weighted-graph Fiedler gap lambda_1 (algebraic connectivity) of the SU(3)
        Josephson unit cell, cross-checked against the Cheeger inequality h^2/4 <= lambda_1.
(3) frac170 = m_G/(170 Delta_BCS); pair-breaking-edge x_G = (m_G/sqrt(rho_s))/(2 Delta_BCS).
(4) Ceiling frac170_ceiling = J_C2/(170 Delta_BCS); target/ceiling = (170 Delta_BCS)/J_C2.
(5) [SIGN] 3-tuple: SIGN (m_G^Ch vs m_IM), MAGNITUDE (frac170 vs target), REGIME (x_G<1).

SOURCE-RECON: the disorder length is the Larkin length xi_Larkin = 17.115 bonds, NOT
the KZ quench length -- the two are distinct; the connectivity mechanism uses xi_eff ~ 1
bond (the cell scale), the SHORT-xi reading that enlarges m_G.

DISCIPLINE
----------
- canonical_constants: J_C2, J_su2, J_u1, omega_L1, Delta_BCS  (rho_s loaded from the
  SHA-pinned s48 npz `rho_s_C2`, its producing computation -- substrate-first sourcing,
  cross-checked against the inv5 npz `rho_s`).
- Every intermediate tagged `# (local)`.
- numpy.linalg (graph Laplacians are <= 9x9; OMP capped at 8 per CPU-fallback rule).
- dual-SHA (S84+); the script PRINTS the emit_verdict payload (race-safe MCP emission).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
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
# Canonical constants (S34+ MANDATORY)
# ---------------------------------------------------------------------------
ROOT = Path("C:/sandbox/Ainulindale Exflation")
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
from canonical_constants import (  # noqa: E402
    J_C2, J_su2, J_u1, omega_L1, Delta_BCS,
)

# ---------------------------------------------------------------------------
# Identity / pins (plan W3-2 PRDR)
# ---------------------------------------------------------------------------
SESSION = 116  # (local)
WAVE = "w3"  # (local)
GATE_ID = "S116-W3-GOLDSTONE-M2"
SCHEME = "JOSEPHSON-GRAPH-CHEEGER-CONNECTIVITY-CEILING"
CONVENTION = "GOLDSTONE-MASS-FROM-LATTICE-LAPLACIAN-FIEDLER-GAP-VS-DISORDER-FAMILY-CEILING"
L_MAX = 10  # (local) plan-pinned; tau_fold=0.190 single-point

# Pre-registered rubric bands (plan W3-2 strict_PASS_boundary)
PASS_BAND_FRAC170 = 0.5          # (local) frac170 >= 0.5 -> PASS (>=50% of 170x target)
M_REQUIRED_OVER_M_LEGGETT = 170  # (local) the 170x DM-mass target factor (collab §5)
X_EDGE = 1.0                     # (local) pair-breaking edge: x_G < 1 -> below edge (VALID)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
OUT_DIR = ROOT / "computations" / f"session-{SESSION}"
OUT_DIR.mkdir(parents=True, exist_ok=True)
SCRIPT_PATH = OUT_DIR / "s116_w3_goldstone_m2_disorder_ceiling.py"
NPZ_PATH = OUT_DIR / "s116_w3_goldstone_m2_disorder_ceiling.npz"
PNG_PATH = OUT_DIR / "s116_w3_goldstone_m2_disorder_ceiling.png"

CANONICAL_CONSTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
INV5_NPZ = ROOT / "computations" / "investigation-5" / "inv5_w2_4_goldstone_mass_disorder.npz"
S48_NPZ = ROOT / "computations" / "session-48" / "s48_goldstone_mass.npz"
S29B_NPZ = ROOT / "computations" / "session-29" / "s29b_josephson_coupling.npz"

INPUT_FILES = [CANONICAL_CONSTS, INV5_NPZ, S48_NPZ, S29B_NPZ]


# ---------------------------------------------------------------------------
# SHA-256 dual-pin block (S84+; first 20 lines of stdout)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def npz_scalar(d, key):
    """Robust 0-D / 1-D scalar field access (technical-notes.md)."""
    return float(np.asarray(d[key]).flat[0])


# ---------------------------------------------------------------------------
# Graph Laplacian helpers (numpy; matrices <= 9x9)
# ---------------------------------------------------------------------------
def laplacian_spectrum(W: np.ndarray) -> np.ndarray:
    """Eigenvalues of the weighted graph Laplacian L = D - W (ascending)."""
    deg = np.sum(W, axis=1)  # (local)
    L = np.diag(deg) - W  # (local)
    ev = np.linalg.eigvalsh(L)  # (local) symmetric, real
    ev[np.abs(ev) < 1e-12] = 0.0  # (local) clean the zero mode
    return np.sort(ev)


def complete_graph_weight(n: int, w: float) -> np.ndarray:
    """Adjacency of K_n with uniform edge weight w (zero diagonal)."""
    W = w * (np.ones((n, n)) - np.eye(n))  # (local)
    return W


def su3_unit_cell_star(j_c2: float, j_su2: float, j_u1: float) -> np.ndarray:
    """The literal '8 gauge-direction bonds' cell: a central node + 8 neighbour
    images, edges weighted [4 x J_C2, 3 x J_su2, 1 x J_u1].  9x9 weighted star."""
    bond_w = [j_c2] * 4 + [j_su2] * 3 + [j_u1] * 1  # (local) 8 bonds
    n = 1 + len(bond_w)  # (local) center + 8 leaves
    W = np.zeros((n, n))  # (local)
    for i, w in enumerate(bond_w, start=1):
        W[0, i] = w
        W[i, 0] = w
    return W


# ---------------------------------------------------------------------------
# Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    res = {}  # (local)

    # --- canonical pins ---
    res["J_C2"] = float(J_C2)
    res["J_su2"] = float(J_su2)
    res["J_u1"] = float(J_u1)
    res["omega_L1"] = float(omega_L1)        # bare Leggett-1 frequency (context anchor)
    res["Delta_BCS"] = float(Delta_BCS)

    # --- (1) reload the inv5 disorder bracket (constructions A..E) ---
    inv5 = np.load(INV5_NPZ, allow_pickle=True)  # (local)
    m_IM = npz_scalar(inv5, "br_A_Larkin_weak_m_G")          # (local) Imry-Ma baseline
    xi_Larkin = npz_scalar(inv5, "xi_Larkin")                # (local) 17.115 bonds (NOT KZ)
    h_rf = npz_scalar(inv5, "h_rf")                          # (local) RF strength
    m_ceiling_brE = npz_scalar(inv5, "br_E_max_bond_J_C2_m_G")  # (local) disorder ceiling = J_C2
    xG_brE = npz_scalar(inv5, "br_E_max_bond_J_C2_x_G")      # (local) inv5 ceiling x_G
    omegaG_brE = npz_scalar(inv5, "br_E_max_bond_J_C2_omega_G")  # (local)
    # full 5-construction frac170 bracket (computed consistently as m_G/(170 Delta))
    denom = M_REQUIRED_OVER_M_LEGGETT * float(Delta_BCS)     # (local) 170*Delta_BCS
    bracket = {}  # (local)
    for tag in ["A_Larkin_weak", "B_saturated_hrf", "C_saturated_Ju1",
                "D_std_nonC2", "E_max_bond_J_C2"]:
        m_g = npz_scalar(inv5, f"br_{tag}_m_G")  # (local)
        bracket[tag] = (m_g, m_g / denom)
    frac170_ceiling_family = bracket["E_max_bond_J_C2"][1]   # (local) disorder-family max
    res["m_IM"] = m_IM
    res["xi_Larkin"] = xi_Larkin
    res["h_rf"] = h_rf
    res["denom_170Delta"] = denom
    res["frac170_ceiling_family"] = frac170_ceiling_family
    res["bracket_m_G"] = {k: v[0] for k, v in bracket.items()}
    res["bracket_frac170"] = {k: v[1] for k, v in bracket.items()}

    # --- rho_s from the SHA-pinned s48 npz (substrate-first; NOT canonical_constants) ---
    s48 = np.load(S48_NPZ, allow_pickle=True)  # (local)
    rho_s = npz_scalar(s48, "rho_s_C2")  # (local) C^2 phase stiffness 7.962
    rho_s_inv5 = npz_scalar(inv5, "rho_s")  # (local) cross-check
    m_G_BCS_floor = npz_scalar(s48, "m_G_over_MKK_BCS")  # (local) BCS floor 0.006838
    sa_mass = npz_scalar(s48, "m_G_sq_BCS_estimate")  # (local) context
    assert abs(rho_s - rho_s_inv5) < 1e-9, "rho_s s48/inv5 mismatch"
    res["rho_s"] = rho_s
    res["rho_s_inv5_crosscheck"] = rho_s_inv5
    res["m_G_BCS_floor"] = m_G_BCS_floor

    # --- s29b J-matrix Frobenius cross-check (tau_fold ~ tau3=0.2) ---
    s29b = np.load(S29B_NPZ, allow_pickle=True)  # (local)
    j_frob_fold = npz_scalar(s29b, "tau3_J_matrix_frobenius")  # (local) 0.427
    res["s29b_j_frob_fold"] = j_frob_fold

    # --- (2a) closed-form Cheeger lower bound  m_G^Ch >= h/2 = J_C2 ---
    h_cheeger = 2.0 * float(J_C2)               # (local) h(L) = 2 J_C2 / Vol(cell), Vol=1
    m_Ch = h_cheeger / 2.0                       # (local) = J_C2 = Cheeger bottleneck
    # Step-6 coupling-scale ceiling: m_G = E/xi <= J_C2/1 = J_C2  (E<=J_C2, xi>=1 bond)
    m_ceiling = float(J_C2)                      # (local) the coupling-scale wall
    # PINCH:  h/2 (lower) = J_C2 = ceiling (upper)  ->  surviving-mechanism mass = J_C2
    m_G_surviving = m_Ch                          # (local) the pre-registered surviving mass
    res["h_cheeger"] = h_cheeger
    res["m_G_Ch"] = m_Ch
    res["m_ceiling_couplingscale"] = m_ceiling
    res["m_G_surviving"] = m_G_surviving

    # --- (2b) lattice-Laplacian Fiedler gap (connectivity cross-check) ---
    # C^2-sector backbone (where the U(1)_7 Goldstone T_7 lives): complete K_4 @ J_C2.
    W_c2 = complete_graph_weight(4, float(J_C2))  # (local)
    spec_c2 = laplacian_spectrum(W_c2)            # (local) {0, 4J_C2, 4J_C2, 4J_C2}
    lam1_c2 = spec_c2[1]                           # (local) Fiedler (algebraic connectivity)
    lam_max_c2 = spec_c2[-1]                       # (local)
    m_lam1 = float(np.sqrt(lam1_c2))               # (local) m_G^lam1 = sqrt(lambda_1) (optical)
    # full 8-bond SU(3) unit cell (literal star; softest inter-block link sets Fiedler)
    W_cell = su3_unit_cell_star(float(J_C2), float(J_su2), float(J_u1))  # (local)
    spec_cell = laplacian_spectrum(W_cell)         # (local)
    lam1_cell = spec_cell[1]                        # (local) ~ J_u1 (soft / Imry-Ma-like end)
    lam_max_cell = spec_cell[-1]                    # (local)
    # Cheeger inequality cross-check:  h^2/4 <= lambda_1(C^2 backbone)
    h2_over_4 = h_cheeger ** 2 / 4.0               # (local) = J_C2^2
    cheeger_ineq_ok = bool(h2_over_4 <= lam1_c2 + 1e-12)  # (local)
    # discrete sandwich  h^2/(2 d_max) <= lambda_1 <= 2h  (Alon-Milman)
    d_max_c2 = float(np.max(np.sum(W_c2, axis=1)))  # (local) 3 J_C2
    sandwich_lo = h_cheeger ** 2 / (2.0 * d_max_c2)  # (local)
    sandwich_ok = bool(sandwich_lo <= lam1_c2 + 1e-12 and lam1_c2 <= 2.0 * h_cheeger + 1e-12)  # (local)
    res["spec_c2"] = spec_c2
    res["lam1_c2"] = float(lam1_c2)
    res["lam_max_c2"] = float(lam_max_c2)
    res["m_lam1_optical"] = m_lam1
    res["spec_cell"] = spec_cell
    res["lam1_cell"] = float(lam1_cell)
    res["lam_max_cell"] = float(lam_max_cell)
    res["h2_over_4"] = h2_over_4
    res["cheeger_ineq_ok"] = cheeger_ineq_ok
    res["d_max_c2"] = d_max_c2
    res["sandwich_ok"] = sandwich_ok

    # --- (3) frac170 + pair-breaking-edge ratio ---
    frac170 = m_G_surviving / denom                # (local) the gate's MAGNITUDE quantity
    frac170_lam1 = m_lam1 / denom                  # (local) optical-Fiedler cross-check
    omega_G = m_G_surviving / np.sqrt(rho_s)        # (local) physical Goldstone frequency
    x_G = float(omega_G / (2.0 * float(Delta_BCS)))  # (local) pair-breaking-edge ratio
    res["frac170"] = float(frac170)
    res["frac170_lam1_optical"] = float(frac170_lam1)
    res["omega_G"] = float(omega_G)
    res["x_G"] = x_G

    # --- (4) ceiling formula + structural-shortfall factor ---
    frac170_ceiling = float(J_C2) / denom          # (local) = J_C2/(170 Delta_BCS)
    target_over_ceiling = denom / float(J_C2)       # (local) ~ 84.6 (the 85x wall)
    res["frac170_ceiling"] = frac170_ceiling
    res["target_over_ceiling"] = target_over_ceiling

    # --- SIGN: connectivity mass vs Imry-Ma baseline ---
    sign_delta = m_G_surviving - m_IM               # (local) > 0 predicted
    ratio_Ch_IM = m_G_surviving / m_IM              # (local) ~ 293
    res["sign_delta"] = float(sign_delta)
    res["ratio_Ch_over_IM"] = float(ratio_Ch_IM)

    # robustness: even the absolute stiffest graph mode is far below target
    frac170_stiffest = float(np.sqrt(max(lam_max_c2, lam_max_cell))) / denom  # (local)
    res["frac170_stiffest_graph_mode"] = float(frac170_stiffest)

    res["value"] = float(frac170)
    return res


# ---------------------------------------------------------------------------
# Verdict (3-tuple + composite collapse per gate-verdicts.md)
# ---------------------------------------------------------------------------
def evaluate(res: dict) -> dict:
    frac170 = res["frac170"]                       # (local)
    ceiling_family = res["frac170_ceiling_family"]  # (local)
    # SIGN: m_G^Ch > m_IM  (direction predicted by xi_eff < xi_Larkin)
    sign_verdict = "PASS" if res["sign_delta"] > 0 else "FAIL"  # (local)
    # MAGNITUDE: PASS>=0.5 ; FAIL<=ceiling_family ; INFO between
    if frac170 >= PASS_BAND_FRAC170:
        magnitude_verdict = "PASS"
    elif frac170 <= ceiling_family + 1e-15:
        magnitude_verdict = "FAIL"
    else:
        magnitude_verdict = "INFO"
    # REGIME: below pair-breaking edge?  x_G < 1 -> VALID
    x_G = res["x_G"]  # (local)
    if x_G < X_EDGE:
        regime_verdict = "VALID"
    elif x_G < 2.0 * X_EDGE:
        regime_verdict = "MARGINAL"
    else:
        regime_verdict = "BREAKDOWN"
    # composite collapse (PRE-REGISTERED; modifications are Class-3 violations)
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
    return {"sign": sign_verdict, "magnitude": magnitude_verdict,
            "regime": regime_verdict, "composite": composite}


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, verd: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    # Panel 1 — frac170 ladder: disorder family A..E + Cheeger surviving + target
    labels = ["A Imry-Ma\n(inv5 baseline)", "B sat h_rf", "C sat J_u1",
              "D std nonC2", "E ceiling\n(=J_C2)", "Cheeger\nsurviving",
              "lam1 optical\nsqrt(4 J_C2)"]
    order = ["A_Larkin_weak", "B_saturated_hrf", "C_saturated_Ju1",
             "D_std_nonC2", "E_max_bond_J_C2"]
    vals = [res["bracket_frac170"][k] for k in order]
    vals += [res["frac170"], res["frac170_lam1_optical"]]
    colors = ["#888"] * 4 + ["#c0392b", "#2471a3", "#8e44ad"]
    x = np.arange(len(vals))
    ax1.bar(x, vals, color=colors)
    ax1.axhline(1.0, color="k", ls="--", lw=1.6, label="170x DM-mass target (frac170=1)")
    ax1.axhline(res["frac170_ceiling"], color="#c0392b", ls=":", lw=1.4,
                label=f"Josephson-graph ceiling = J_C2/(170Δ) = {res['frac170_ceiling']:.4f}")
    ax1.set_yscale("log")
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, fontsize=7.5, rotation=30, ha="right")
    ax1.set_ylabel("frac170 = m_G / (170 Δ_BCS)")
    ax1.set_title(f"S116-W3-GOLDSTONE-M2 : ~{res['target_over_ceiling']:.0f}x short of target "
                  f"({verd['composite']})", fontsize=10)
    ax1.legend(fontsize=7.5, loc="center right")
    ax1.annotate(f"SIGN+: connectivity / Imry-Ma = {res['ratio_Ch_over_IM']:.0f}x",
                 xy=(5, res["frac170"]), xytext=(1.4, 0.12),
                 fontsize=8, arrowprops=dict(arrowstyle="->", color="#c0392b"))

    # Panel 2 — graph Laplacian spectra + the J_C2 coupling-scale wall
    ax2.plot(np.arange(len(res["spec_c2"])), res["spec_c2"], "o-", color="#2471a3",
             label=f"C² K₄ @ J_C2 (lam1={res['lam1_c2']:.3f})")
    ax2.plot(np.arange(len(res["spec_cell"])), res["spec_cell"], "s--", color="#16a085",
             label=f"full 8-bond cell star (lam1={res['lam1_cell']:.3f})")
    ax2.axhline(res["h2_over_4"], color="#c0392b", ls=":", lw=1.4,
                label=f"Cheeger h²/4 = J_C2² = {res['h2_over_4']:.3f}")
    ax2.axhline(float(J_C2), color="k", ls="--", lw=1.2,
                label=f"coupling scale J_C2 = {float(J_C2):.3f} ~ 2Δ_BCS")
    ax2.set_xlabel("eigenvalue index")
    ax2.set_ylabel("graph-Laplacian eigenvalue  (M_KK)")
    ax2.set_title(f"connectivity spectrum at the J_C2 scale ; x_G={res['x_G']:.3f}<1 "
                  f"(below edge, {verd['regime']})", fontsize=10)
    ax2.legend(fontsize=7.5, loc="upper left")

    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# emit_verdict payload (race-safe MCP emission; script does NOT write the file)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          companion_note="", extra_rows=None):
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
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
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
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTS, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()
    verd = evaluate(res)

    # --- console report (NUMBERS first) ---
    print("---- inv5 disorder bracket reload (constructions A..E) ----")
    for k in ["A_Larkin_weak", "B_saturated_hrf", "C_saturated_Ju1",
              "D_std_nonC2", "E_max_bond_J_C2"]:
        print(f"  {k:18s}  m_G={res['bracket_m_G'][k]:.6f}  frac170={res['bracket_frac170'][k]:.6e}")
    print(f"  Imry-Ma baseline m_IM = {res['m_IM']:.6f}  (xi_Larkin={res['xi_Larkin']:.3f} bonds)")
    print(f"  disorder-family ceiling frac170_E = {res['frac170_ceiling_family']:.6e}")
    print()
    print("---- surviving mechanism: Cheeger / lattice-Laplacian connectivity ----")
    print(f"  h(L)=2 J_C2            = {res['h_cheeger']:.6f}")
    print(f"  m_G^Ch = h/2 = J_C2   = {res['m_G_Ch']:.6f}   (Cheeger bottleneck)")
    print(f"  coupling ceiling m<=J_C2 = {res['m_ceiling_couplingscale']:.6f}  -> PINCH m_G={res['m_G_surviving']:.6f}")
    print(f"  C^2 K_4 spectrum      = {np.round(res['spec_c2'],4).tolist()}")
    print(f"  Fiedler lam1(C^2)     = {res['lam1_c2']:.6f}   m_G^lam1=sqrt={res['m_lam1_optical']:.6f} (optical)")
    print(f"  full-cell spectrum    = {np.round(res['spec_cell'],4).tolist()}")
    print(f"  Fiedler lam1(cell)    = {res['lam1_cell']:.6f}  (soft inter-block ~ J_u1)")
    print(f"  Cheeger ineq h^2/4<=lam1 : {res['cheeger_ineq_ok']}  (h^2/4={res['h2_over_4']:.4f} <= {res['lam1_c2']:.4f})")
    print(f"  Alon-Milman sandwich ok  : {res['sandwich_ok']}")
    print(f"  s29b J-Frobenius(fold)   = {res['s29b_j_frob_fold']:.6f}  (cross-check)")
    print()
    print("---- frac170 / ceiling / 3-tuple ----")
    print(f"  170*Delta_BCS         = {res['denom_170Delta']:.6f}")
    print(f"  frac170 (surviving)   = {res['frac170']:.6e}")
    print(f"  frac170_ceiling       = {res['frac170_ceiling']:.6e}")
    print(f"  frac170 == ceiling    : {abs(res['frac170']-res['frac170_ceiling'])<1e-12}")
    print(f"  target/ceiling        = {res['target_over_ceiling']:.4f}  (~85x short)")
    print(f"  SIGN delta m_Ch-m_IM  = {res['sign_delta']:.6f}  (ratio {res['ratio_Ch_over_IM']:.1f}x)")
    print(f"  rho_s (s48/inv5)      = {res['rho_s']:.4f} / {res['rho_s_inv5_crosscheck']:.4f}")
    print(f"  omega_G               = {res['omega_G']:.6f}  (inv5 br_E=0.330652)")
    print(f"  x_G (pair-break edge) = {res['x_G']:.6f}  (<1 => below edge)")
    print(f"  stiffest-graph-mode frac170 = {res['frac170_stiffest_graph_mode']:.6e} (<< 0.5)")
    print()
    print(f"  3-tuple: SIGN={verd['sign']}  MAGNITUDE={verd['magnitude']}  REGIME={verd['regime']}")
    print(f"  COMPOSITE = {verd['composite']}")
    print()

    # --- persist npz ---
    npz_out = {k: v for k, v in res.items()
               if not isinstance(v, dict)}  # (local) flat scalars + arrays
    # flatten the bracket dicts
    for k, v in res["bracket_m_G"].items():
        npz_out[f"bracket_mG_{k}"] = v
    for k, v in res["bracket_frac170"].items():
        npz_out[f"bracket_frac170_{k}"] = v
    npz_out["sign_verdict"] = verd["sign"]
    npz_out["magnitude_verdict"] = verd["magnitude"]
    npz_out["regime_verdict"] = verd["regime"]
    npz_out["composite"] = verd["composite"]
    npz_out["gate_id"] = GATE_ID
    npz_out["scheme"] = SCHEME
    npz_out["convention"] = CONVENTION
    npz_out["audit_sha256"] = audit_sha
    npz_out["content_sha256"] = content_sha
    np.savez(NPZ_PATH, **npz_out)
    print(f"  npz -> {NPZ_PATH}")

    make_plot(res, verd)
    print(f"  png -> {PNG_PATH}")
    print()

    # --- 4-tuple + emit payload ---
    value_payload = (
        f"m_G_surv={res['m_G_surviving']:.4f}|frac170={res['frac170']:.6e}|"
        f"ceiling={res['frac170_ceiling']:.6e}|target_over_ceiling={res['target_over_ceiling']:.2f}|"
        f"ratio_Ch_IM={res['ratio_Ch_over_IM']:.1f}|x_G={res['x_G']:.4f}|"
        f"lam1_C2={res['lam1_c2']:.4f}|m_lam1={res['m_lam1_optical']:.4f}|"
        f"cheeger_ineq={res['cheeger_ineq_ok']}|frac170_lam1={res['frac170_lam1_optical']:.4e}|"
        f"composite={verd['composite']}"
    )  # (local) no single-quote chars
    print(f"(value={value_payload!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    extra = [
        f"# REGIME x_G={res['x_G']:.4f}<1 below pair-breaking edge (VALID); "
        f"omega_G={res['omega_G']:.4f}; rho_s={res['rho_s']:.3f}",
        f"# structural-closure: Cheeger surviving mass m_G=J_C2={res['m_G_surviving']:.4f} "
        f"= inv5 br_E ceiling; frac170={res['frac170']:.4e}==ceiling; "
        f"target/ceiling={res['target_over_ceiling']:.1f}x; graph-unanchored (Reading B)",
    ]
    print_verdict_payload(
        verd["composite"], value_payload, audit_sha, content_sha,
        sign_verdict=verd["sign"], magnitude_verdict=verd["magnitude"],
        regime_verdict=verd["regime"],
        companion_note=(f"surviving-mechanism={CONVENTION}; SIGN+ (293x Imry-Ma) "
                        f"MAGNITUDE FAIL (~85x short) REGIME VALID (x_G<1)"),
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verd['composite']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
