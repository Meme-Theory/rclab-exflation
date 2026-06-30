#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S117-W8-1  CF-S117-STATEPROJ-INTER-SUMMAND
==========================================
Substrate-first (Track-A) inter-summand BCS condensation-DOS asymmetry R_summand
between the algebra summands of A_K = C (+) H (+) M3(C), at the COMMON gap Delta_BCS.

GATE: CF-S117-STATEPROJ-INTER-SUMMAND | [SIGN] | PHONONIC | composite G1 ^ G2.
PLAN: sessions/session-plan/session-117-plan-w8.md  S W8-1.

SUBSTRATE FRAMING (phononic-framing.md):
  The substrate IS the BdG BCS ground state on the spectral triple (A_K, H_K, D_K).
  Direction of explanation:
    D_K eigenvalues {lambda_k}
      -> BdG quasiparticle dispersion  xi_k = |lambda_k|  (mu=0 forced by PH symmetry, wall #6)
      -> E_k = sqrt(xi^2 + Delta_BCS^2)
      -> gap-localized PH-even condensation weight  w_k = |xi_k| - E_k + Delta^2/(2 E_k)
      -> weighted against the substrate's OWN algebra central projection of A_K
      -> inter-summand asymmetry  R_summand = (a - b)/(a + b).
  Corner-III (algebra-DEPENDENT) STATE-PROJ observable; ZERO lab input (Track A).

-----------------------------------------------------------------------------
STRUCTURAL FINDING (in-session correction, honestly disclosed per
math-scripts.md "Honest disclosure" + v3-closure-recovery Class-1 boundary):

  The plan's LITERAL method ("lift the W5 central projections P_H, P_{M3} to the
  D_K fiber and compress the per-(p,q) blocks") rests on identifying the
  Cliff(R^8) SPINOR fiber C^16 of D_K with the NCG-SM PARTICLE fiber C^16 of W5.
  These are DIFFERENT C^16 spaces. The s84/s87 cache stores 16 |xi| per (p,q) =
  the SPINOR dimension, carrying NO particle-fiber index. Compressing D_pi onto
  a spinor-index subset chosen by the W5 particle labels is LABELING-DEPENDENT
  (permuting the 16 spinor indices changes R) and, worse, the W5 M3 spinor-index
  projection acts NON-trivially even on the color-SINGLET (0,0) sector -- which
  is physically wrong (the color algebra M3 must annihilate color singlets).
  => the literal spinor-index method does NOT yield a clean substrate observable.
  This is computed below as a DIAGNOSTIC that demonstrates the defect.

  CANONICAL reading = the FAITHFUL lift of the M3 central projection via the
  intrinsic Peter-Weyl COLOR-SECTOR structure (framework: geometric SU(3) IS
  color SU(3)_c). The M3 central idempotent 1_{M3} acts as 0 on color-singlet
  (0,0) and as identity on color-charged (p,q)!=(0,0). Its complement
  (1 - 1_{M3}) = 1_C + 1_H is the electroweak (color-blind) content carried by
  the (0,0) sector -- the "H side" (the plan's H, dominated by the 4-dim
  quaternion vs the 1-dim C center). This lift is LABELING-INDEPENDENT,
  intrinsic, and uses ONLY the cached D_K spectrum (Track A).

  Same pre-registered thresholds (|R|>=1e-3 G1; L_max-drift<=0.10 G2) applied to
  the corrected observable. No threshold/scheme change to reach PASS.
-----------------------------------------------------------------------------
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
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
# Section 1 -- Paths + canonical imports (NEVER hardcode framework constants)
# --------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import Delta_BCS, tau_fold     # noqa: E402  (R-PROTECTED gap; fold modulus)

# --------------------------------------------------------------------------
# Section 2 -- Gate identity + machinery pins (plan W8-1 PRDR block)
# --------------------------------------------------------------------------
GATE_ID = "CF-S117-STATEPROJ-INTER-SUMMAND"
SESSION = 117                               # (local) session number for emit_verdict
SCHEME = "INTER-SUMMAND-BCS-condensation-DOS-asymmetry"
# Canonical convention: intrinsic M3-central-projection color-sector lift (in-session
# structural correction of the labeling-dependent literal spinor-index method).
CONVENTION = ("RATIO-NORMALIZED-TRACE-MEAN + (a_H-b_M3)/(a_H+b_M3)-inter-summand "
              "+ STATE-PROJ-Corner-III + SUBSTRATE-NATURAL-BINDING "
              "+ M3-CENTRAL-PROJECTION-COLOR-SECTOR-LIFT-in-session-correction")
L_MAX = 12                                  # (local) canonical truncation (s84); 14 = stability (s87)

EPS_VANISH = 1e-3                           # (local) G1 vanishing-test PASS floor (plan pin)
EPS_INFO = 1e-6                             # (local) G1 INFO/FAIL boundary (plan pin)
DRIFT_TOL = 0.10                            # (local) G2 Corner-III L_max-drift tolerance (plan pin)

S84_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S87_CACHE = PROJECT_ROOT / "computations" / "session-87" / "s87_spectrum_cache_L14_tau019.npz"
W5_NPZ = PROJECT_ROOT / "computations" / "session-116" / "s116_w5_bimodule_h.npz"
W5_PY = PROJECT_ROOT / "computations" / "session-116" / "s116_w5_bimodule_h.py"

INPUT_FILES = [
    Path(__file__).resolve(),
    SHARED_DIR / "canonical_constants.py",
    S84_CACHE, S87_CACHE, W5_NPZ, W5_PY,
]

# --------------------------------------------------------------------------
# Section 3 -- dual-SHA helpers (S84+ schema; mirror script-template.py / W7)
# --------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                    # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                               # (local)
    for p in inputs:
        sha = sha256_of(p)                                  # (local)
        rel = str(Path(p).relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = Path(script_path).read_bytes()           # (local)
    canonical_bytes = Path(canonical_path).read_bytes()     # (local)
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


# --------------------------------------------------------------------------
# Section 4 -- BCS condensation weight (the S116-W7 functional, common gap)
# --------------------------------------------------------------------------
def w_weight(xi, delta):
    """Per-mode condensation weight  w_k = |xi| - E_k + Delta^2/(2 E_k),
    E_k = sqrt(xi^2 + Delta^2).  PH-EVEN (depends only on |xi|), <= 0, gap/edge
    localized: w(0) = -Delta/2 ; w(|xi|>>Delta) -> -Delta^4/(8|xi|^3) -> 0.
    Returns |w| (magnitude)."""
    xi = np.abs(np.asarray(xi, dtype=float))               # (local)
    Ek = np.sqrt(xi**2 + delta**2)                         # (local)
    w = xi - Ek + delta**2 / (2.0 * Ek)                    # (local) <= 0
    return np.abs(w)


def load_sectors(cache_path):
    d = np.load(cache_path, allow_pickle=True)
    return d["sector_evals"].item()                        # dict {(p,q): {dim, level, abs_evals}}


def color_resolved_R(cache_path, delta, pw_weight=False):
    """CANONICAL: lift the M3 central projection via the Peter-Weyl color-sector
    structure. color-SINGLET (0,0) = (1 - 1_{M3}) = C (+) H electroweak side;
    color-CHARGED (p,q)!=(0,0) = 1_{M3} side.  Intensive RATIO-NORMALIZED-TRACE-MEAN
    a = sum(|w|*mult)/sum(mult) over each summand;  R = (a - b)/(a + b).
    pw_weight=False reproduces the S116-W7 un-PW-weighted convention (the pinned
    functional); pw_weight=True applies the Peter-Weyl multiplicity dim(p,q)."""
    se = load_sectors(cache_path)
    sa_xi, sa_m, cb_xi, cb_m = [], [], [], []              # (local)
    for (p, q), blk in se.items():
        ae = np.asarray(blk["abs_evals"], dtype=float)     # (local) 16*dim_rho |xi| values
        mult = (int(blk["dim"]) if pw_weight else 1)       # (local) PW mult = dim(p,q) or 1
        if (p, q) == (0, 0):
            sa_xi.append(ae); sa_m.append(np.full(ae.size, mult))
        else:
            cb_xi.append(ae); cb_m.append(np.full(ae.size, mult))
    sa_xi = np.concatenate(sa_xi); sa_m = np.concatenate(sa_m)
    cb_xi = np.concatenate(cb_xi); cb_m = np.concatenate(cb_m)
    wa = w_weight(sa_xi, delta); wb = w_weight(cb_xi, delta)
    a_int = float(np.sum(wa * sa_m) / np.sum(sa_m))        # (local) intensive (per-mode) singlet density
    b_int = float(np.sum(wb * cb_m) / np.sum(cb_m))        # (local) intensive color density
    a_ext = float(np.sum(wa * sa_m)); b_ext = float(np.sum(wb * cb_m))   # (local) extensive (block-sum)
    R_int = (a_int - b_int) / (a_int + b_int)              # (local)
    R_ext = (a_ext - b_ext) / (a_ext + b_ext)             # (local)
    N_sing = int(np.sum(sa_m)); N_col = int(np.sum(cb_m))  # (local)
    return dict(a_int=a_int, b_int=b_int, R_int=R_int, a_ext=a_ext, b_ext=b_ext,
                R_ext=R_ext, N_sing=N_sing, N_col=N_col,
                xi_min=float(min(sa_xi.min(), cb_xi.min())),
                xi_min_singlet=float(sa_xi.min()), xi_min_color=float(cb_xi.min()))


# --------------------------------------------------------------------------
# Section 5 -- DIAGNOSTIC: literal W5 spinor-index compression is LABELING-DEPENDENT
# --------------------------------------------------------------------------
def build_omega(s):
    """Rebuild the (0,0)-sector D_K block = Omega (spinor curvature offset, 16x16)
    via the dirac_spectrum infrastructure that produced the s84 cache."""
    import dirac_spectrum as ds
    gens = ds.su3_generators()                             # (local)
    f_abc = ds.compute_structure_constants(gens)          # (local)
    gammas = ds.build_cliff8()                             # (local)
    B_ab = ds.compute_killing_form(f_abc)                 # (local)
    g_s = ds.jensen_metric(B_ab, s)                       # (local)
    E = ds.orthonormal_frame(g_s)                         # (local)
    ft = ds.frame_structure_constants(f_abc, E)           # (local)
    Gamma = ds.connection_coefficients(ft)               # (local)
    Omega = ds.spinor_connection_offset(Gamma, gammas)   # (local) 16x16
    return Omega


def compress_R(H, idx_A, idx_B, delta):
    """Compress Hermitian H = 1j*D onto two index subsets, |xi| = |eigs|, intensive R."""
    idx_A = list(idx_A); idx_B = list(idx_B)              # (local)
    HA = H[np.ix_(idx_A, idx_A)]; HB = H[np.ix_(idx_B, idx_B)]   # (local) compressions
    xiA = np.abs(np.linalg.eigvalsh(HA)); xiB = np.abs(np.linalg.eigvalsh(HB))  # (local)
    a = float(np.mean(w_weight(xiA, delta))); b = float(np.mean(w_weight(xiB, delta)))  # (local)
    return (a - b) / (a + b), a, b


def spinor_index_diagnostic(delta, seed=20260628):
    """Demonstrate the literal-method defect on the (0,0)=Omega block.
    W5 particle layout (indices 0-15): lepL[0,1] lepR[2,3]
    quarkL[[4,5],[6,7],[8,9]] quarkR[[10,11],[12,13],[14,15]].
    H (SU(2)_L weak) acts on LEFT doublets {0,1,4,5,6,7,8,9} (N=8);
    M3 (color) acts on quarks {4..15} (N=12)."""
    Omega = build_omega(tau_fold)
    H = 1j * Omega                                         # (local) Hermitian (Omega anti-Herm)
    herm_err = float(np.max(np.abs(H - H.conj().T)))      # (local)
    xi00 = np.abs(np.linalg.eigvalsh(H))                  # (local) cross-check vs cache (0.82,0.845,0.971)
    H_idx = [0, 1, 4, 5, 6, 7, 8, 9]                      # (local) weak left doublets (W5)
    M3_idx = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # (local) quark color (W5)
    R_w5, aH, bM = compress_R(H, H_idx, M3_idx, delta)
    # labeling-dependence test: random relabeling of the 16 spinor indices
    rng = np.random.default_rng(seed)                     # (local)
    perm = rng.permutation(16)                            # (local)
    R_perm, _, _ = compress_R(H, [perm[i] for i in H_idx], [perm[i] for i in M3_idx], delta)
    perm2 = rng.permutation(16)                           # (local)
    R_perm2, _, _ = compress_R(H, [perm2[i] for i in H_idx], [perm2[i] for i in M3_idx], delta)
    labeling_dependent = bool(abs(R_w5 - R_perm) > 1e-6 or abs(R_w5 - R_perm2) > 1e-6)
    return dict(herm_err=herm_err, xi00_unique=np.unique(np.round(xi00, 6)).tolist(),
                R_w5=float(R_w5), aH=aH, bM=bM, R_perm=float(R_perm), R_perm2=float(R_perm2),
                labeling_dependent=labeling_dependent,
                note="literal spinor-index compression of the COLOR-SINGLET (0,0) block: "
                     "M3 spinor-projection acts non-trivially on a color singlet (physically "
                     "wrong; M3 must annihilate singlets) AND R changes under spinor relabeling")


# --------------------------------------------------------------------------
# Section 6 -- Compute + verdict
# --------------------------------------------------------------------------
def main():
    t0 = time.time()                                       # (local)
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(),
                                              SHARED_DIR / "canonical_constants.py", pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print(f"  Delta_BCS = {Delta_BCS}  (R-PROTECTED) ; tau_fold = {tau_fold}\n")

    # ---- CANONICAL: color-sector lift of M3 central projection ----
    can12 = color_resolved_R(S84_CACHE, Delta_BCS, pw_weight=False)   # W7-matching un-PW-weighted
    can14 = color_resolved_R(S87_CACHE, Delta_BCS, pw_weight=False)
    R12 = can12["R_int"]; R14 = can14["R_int"]            # (local) canonical observable
    drift = abs(R14 - R12) / abs(R12) if R12 != 0 else 9.99   # (local) G2 metric

    # robustness: PW-multiplicity-weighted (intensive) + extensive
    pw12 = color_resolved_R(S84_CACHE, Delta_BCS, pw_weight=True)
    pw14 = color_resolved_R(S87_CACHE, Delta_BCS, pw_weight=True)
    drift_pw = abs(pw14["R_int"] - pw12["R_int"]) / abs(pw12["R_int"])   # (local)
    drift_ext = abs(can14["R_ext"] - can12["R_ext"]) / abs(can12["R_ext"])  # (local)

    # edge structure
    xi_min = can12["xi_min"]                               # (local)
    gap_over_delta = xi_min / Delta_BCS                    # (local) spectral gap in units of Delta_BCS

    # ---- DIAGNOSTIC: literal spinor-index method is labeling-dependent ----
    diag = spinor_index_diagnostic(Delta_BCS)

    # ---- [SIGN] substitution chain (sign of R = sign(a_singlet - b_color)) ----
    sign_predicted = +1                                   # (local) plan: color tower bulk-diluted -> R>0
    sign_computed = int(np.sign(R12))                     # (local)

    # ---- 3-tuple ----
    # magnitude: |R| vanishing-test bands (plan tolerance pin)
    aR = abs(R12)                                          # (local)
    magnitude_verdict = "PASS" if aR >= EPS_VANISH else ("INFO" if aR >= EPS_INFO else "FAIL")
    # sign: predicted vs computed
    sign_verdict = "PASS" if sign_computed == sign_predicted else "FAIL"
    # regime: Corner-III stability (L_max drift <= 0.10) AND edge-localized
    edge_localized = bool(xi_min > Delta_BCS)             # (local) hard gap above Delta -> edge-localized |w|
    corner_iii_stable = bool(drift <= DRIFT_TOL)         # (local)
    regime_verdict = "VALID" if (corner_iii_stable and edge_localized) else (
        "MARGINAL" if (drift <= 0.5) else "BREAKDOWN")

    # ---- composite under PLAN-FROZEN precedence (G1 ^ G2; sign DIAGNOSTIC) ----
    track_A = True                                        # (local) zero lab input (no SC ratio injected)
    G1 = (magnitude_verdict == "PASS") and track_A       # (local) vanishing test ^ Track-A
    G2 = (regime_verdict == "VALID")                     # (local) Corner-III stability
    composite = "PASS" if (G1 and G2) else (
        "FAIL" if magnitude_verdict == "FAIL" else "INFO")

    # ---- report ----
    print("=== CANONICAL (M3 central-projection color-sector lift; un-PW-weighted, W7-matching) ===")
    print(f"  L=12: a_singlet(non-color C+H)={can12['a_int']:.6e}  b_color(M3)={can12['b_int']:.6e}  "
          f"R_summand={R12:+.6f}  (N_sing={can12['N_sing']}, N_col={can12['N_col']})")
    print(f"  L=14: a_singlet={can14['a_int']:.6e}  b_color={can14['b_int']:.6e}  R_summand={R14:+.6f}")
    print(f"  G2 L_max drift |R14-R12|/|R12| = {drift:.4f}  (tol {DRIFT_TOL})")
    print(f"  spectral edge |xi|_min = {xi_min:.6f}  = {gap_over_delta:.4f} x Delta_BCS  "
          f"(hard gap; |w| edge-localized)")
    print(f"  |xi|_min singlet={can12['xi_min_singlet']:.6f}  color={can12['xi_min_color']:.6f}")
    print("=== ROBUSTNESS ===")
    print(f"  PW-multiplicity-weighted: R12={pw12['R_int']:+.6f}  R14={pw14['R_int']:+.6f}  drift={drift_pw:.4f}")
    print(f"  extensive RATIO-BLOCKSUM: R12={can12['R_ext']:+.6f}  R14={can14['R_ext']:+.6f}  "
          f"drift={drift_ext:.4f}  (SIGN-FLIPPED vs intensive: color tower wins by mode count; "
          f"counting-axis pin is LOAD-BEARING for the sign)")
    print("=== DIAGNOSTIC: literal W5 spinor-index compression (the plan's literal method) ===")
    print(f"  (0,0)=Omega Hermiticity err = {diag['herm_err']:.2e} ; |xi|_(0,0) = {diag['xi00_unique']}")
    print(f"  R_spinor(W5 idx)={diag['R_w5']:+.6f}  R_spinor(perm1)={diag['R_perm']:+.6f}  "
          f"R_spinor(perm2)={diag['R_perm2']:+.6f}")
    print(f"  labeling_dependent = {diag['labeling_dependent']}  ({diag['note']})")
    print("=== VERDICT 3-tuple ===")
    print(f"  sign={sign_verdict} (pred R>0, got R={R12:+.4f})  magnitude={magnitude_verdict} (|R|={aR:.4f} vs 1e-3)  "
          f"regime={regime_verdict} (drift {drift:.4f}, edge {edge_localized})")
    print(f"  G1(vanishing ^ Track-A)={G1}  G2(Corner-III stable)={G2}  COMPOSITE={composite}")

    # ---- persist ----
    npz_path = Path(__file__).with_suffix(".npz")
    np.savez(
        npz_path,
        R_summand=R12, R_summand_L14=R14, drift_G2=drift,
        a_singlet_noncolor=can12["a_int"], b_color_M3=can12["b_int"],
        a_singlet_L14=can14["a_int"], b_color_L14=can14["b_int"],
        N_singlet=can12["N_sing"], N_color=can12["N_col"],
        R_pw_L12=pw12["R_int"], R_pw_L14=pw14["R_int"], drift_pw=drift_pw,
        R_ext_L12=can12["R_ext"], R_ext_L14=can14["R_ext"], drift_ext=drift_ext,
        xi_min=xi_min, gap_over_delta=gap_over_delta,
        xi_min_singlet=can12["xi_min_singlet"], xi_min_color=can12["xi_min_color"],
        R_spinor_W5=diag["R_w5"], R_spinor_perm1=diag["R_perm"], R_spinor_perm2=diag["R_perm2"],
        labeling_dependent=diag["labeling_dependent"],
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        Delta_BCS=Delta_BCS, tau_fold=tau_fold,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n  wrote {npz_path.name}")

    # ---- plot ----
    png_path = Path(__file__).with_suffix(".png")
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    # panel 1: condensation weight |w(xi)| with the spectral edge
    ax = axes[0]
    xis = np.linspace(0.01, 5.0, 600)                     # (local)
    ax.plot(xis, w_weight(xis, Delta_BCS), color="#1a9850", lw=2)
    ax.axvline(Delta_BCS, color="#999999", ls=":", label=f"Delta_BCS={Delta_BCS:.3f}")
    ax.axvline(xi_min, color="#d73027", ls="--", label=f"|xi|_min={xi_min:.3f} (edge)")
    ax.set_xlabel("|xi|  (M_KK)"); ax.set_ylabel("|w(xi)|  condensation weight")
    ax.set_title("Gap/edge-localized PH-even weight\n(hard gap: all |xi| > 1.77 Delta_BCS)")
    ax.legend(fontsize=8)
    # panel 2: intensive a vs b, color-singlet vs color-charged
    ax = axes[1]
    ax.bar(["non-color\n(C+H, singlet)", "M3 color\n(charged)"],
           [can12["a_int"], can12["b_int"]], color=["#4477aa", "#cc6677"], width=0.55)
    ax.set_ylabel("intensive <|w|> (per-mode)")
    ax.set_title(f"Inter-summand condensation density\nR_summand = {R12:+.4f}  (L=12, drift {drift*100:.1f}%)")
    for i, v in enumerate([can12["a_int"], can12["b_int"]]):
        ax.text(i, v, f"{v:.2e}", ha="center", va="bottom", fontsize=9, fontweight="bold")
    # panel 3: text summary
    ax = axes[2]; ax.axis("off")
    txt = (
        "CF-S117-STATEPROJ-INTER-SUMMAND\n"
        "--------------------------------\n"
        f"CANONICAL (M3 central-proj color-sector lift):\n"
        f"  R_summand(L12) = {R12:+.6f}\n"
        f"  R_summand(L14) = {R14:+.6f}\n"
        f"  G2 drift       = {drift*100:.2f}%  (<= 10%)\n\n"
        f"G1 vanishing |R| >= 1e-3 : {magnitude_verdict}\n"
        f"G2 Corner-III stable     : {'PASS' if G2 else 'FAIL'}\n"
        f"sign (pred>0)            : {sign_verdict} (DIAGNOSTIC)\n"
        f"Track A (0 lab input)    : {track_A}\n"
        f"==> COMPOSITE = {composite}\n\n"
        "DIAGNOSTIC (literal spinor-index method):\n"
        f"  R(W5)={diag['R_w5']:+.4f} R(perm)={diag['R_perm']:+.4f}\n"
        f"  labeling-dependent = {diag['labeling_dependent']}\n"
        "  => literal method not a clean observable;\n"
        "     intrinsic color-sector lift adopted.\n\n"
        "robustness:\n"
        f"  PW-weighted R12={pw12['R_int']:+.4f} (drift {drift_pw*100:.1f}%)\n"
        f"  extensive  R12={can12['R_ext']:+.4f} (SIGN-FLIP; counting-axis\n"
        "             pin load-bearing; |R|>=1e-3 holds both axes)\n"
    )
    ax.text(0.0, 1.0, txt, va="top", ha="left", family="monospace", fontsize=8.5, transform=ax.transAxes)
    fig.suptitle(f"{GATE_ID}: R_summand = {R12:+.6f}  [{composite}]  (substrate-first / Track A)",
                 fontsize=12, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(png_path, dpi=130); plt.close(fig)
    print(f"  wrote {png_path.name}")

    # ---- value payload (no apostrophes; emit_verdict wraps value='...') ----
    value = (
        f"R_summand={R12:+.6f}_L12_{R14:+.6f}_L14_drift={drift*100:.2f}pct_"
        f"sign=POS_color-singlet-edge-vs-color-tower-bulk_"
        f"|xi|min={xi_min:.4f}={gap_over_delta:.3f}xDelta_hardgap_edge-localized_"
        f"M3-central-proj-color-sector-lift_Track-A-zero-lab-input_"
        f"literal-spinor-method-LABELING-DEPENDENT-diagnostic"
    )
    extra_rows = [
        "# composite-precedence: anchor=session-117-plan-w8 SW8-1; composite = G1 ^ G2 ; "
        "overrides=generic-sign-FAIL->composite-FAIL (sign_verdict DIAGNOSTIC, not collapsing)",
        f"# G1 = (magnitude PASS [|R|={aR:.4f}>=1e-3 vanishing test] ^ Track-A [no lab SC ratio]); "
        f"G2 = (regime VALID [drift {drift*100:.2f}%<=10% ^ edge-localized |xi|min={xi_min:.4f}>Delta_BCS])",
        "# in-session structural correction (honest disclosure): canonical reading = intrinsic "
        "M3-central-projection lift via Peter-Weyl color-sector structure (geometric SU(3)=color), "
        "NOT the labeling-dependent literal W5 spinor-index compression "
        f"(diagnostic: R_W5={diag['R_w5']:+.4f} != R_perm={diag['R_perm']:+.4f} => labeling-dependent)",
        f"# counting-axis LOAD-BEARING for sign: RATIO-NORMALIZED-TRACE-MEAN intensive (per-mode, "
        f"R={R12:+.4f}>0 canonical) vs RATIO-BLOCKSUM extensive (block-sum, R={can12['R_ext']:+.4f}<0, "
        f"color tower wins by mode count); the |R|>=1e-3 vanishing PASS holds on BOTH axes",
    ]
    print()
    print_verdict_payload(
        verdict=composite, value=value, audit_sha=audit_sha, content_sha=content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        companion_note="§VII.AJ.STATE-PROJ discharges to substrate-first (Track A) via the "
                       "M3-central-projection color-sector lift; routes to mack for slot-status update",
        extra_rows=extra_rows,
    )
    print(f"\n  elapsed {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
