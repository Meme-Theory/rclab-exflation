#!/usr/bin/env python3
"""
INV5 W2-3 — INV5-W2-3-PEKKER-VARMA-HIGGS-SELF-ENERGY
=====================================================

Gate: INV5-W2-3-PEKKER-VARMA-HIGGS-SELF-ENERGY  ([SIGN])

Pre-registered threshold (plan §W2-3, operator=equality):
  |(Re Sigma_continuum / m_H) - (-5.356%)| <= tol,
     -5.356% = -67/1251 EXACT (Sage: 67/1251 = 0.0535572 = +5.35572%); the gate
     tests the NEGATIVE (the downward self-energy shift that would cancel the
     +5.36% m_H overshoot vs PDG).
  tol      = 0.01   (1 pp absolute) -> PASS band Re Sigma/m_H in [-6.356%, -4.356%]
  tol_info = 0.03   (3 pp)          -> INFO band Re Sigma/m_H in [-8.356%, -2.356%]

  [SIGN] sub-test (LOAD-BEARING, plan Step 4-5 + the explicit plan note:
    "if the computed Re Sigma is POSITIVE the bridge B-2 is falsified regardless
     of magnitude (the gate FAILs on sign)"):
       Re Sigma_continuum < 0  (the continuum coupling SHIFTS the mode DOWN).

  PASS iff SIGN=PASS (Re Sigma<0) AND |Re Sigma/m_H - (-5.356%)| <= 1 pp.
  INFO iff SIGN=PASS AND magnitude in (1pp, 3pp].
  FAIL iff SIGN=FAIL (Re Sigma>0) OR |Re Sigma/m_H| outside the 3pp INFO band.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py        (feeds audit_sha256 only)
  - computations/session-48/s48_leggett_mode.npz       ((0,0)-sector B1/B2/B3 gaps
        Delta_fold, DOS rho_fold, inter-band Josephson J_ij at tau_fold=0.19 —
        the two-quasiparticle pair-breaking continuum is built from these)
  - computations/session-43/s43_fano_continuum.npz     (Higgs-continuum vertex
        V_B2B2=0.5892, Delta_pair=Delta_BCS; the S43-W6 Fano/self-energy machinery
        Im[Sigma_i]=pi*sum_j|V_ij|^2 rho_j(omega_i))
  - computations/session-54/s54_higgs_modulus.npz       (|S|^2-radial amplitude mode
        Hessian H_ss; cross-check on the bare-mode identity)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<Re Sigma/m_H + sign + cross-checks>, scheme=PEKKER-VARMA-CONTINUUM-SELF-ENERGY,
   convention=REAL-PART-DISPERSIVE-SHIFT-KRAMERS-KRONIG, L_max=10)

Classification: PHONONIC.

SUBSTRATE-PHYSICS
-----------------
The Higgs IS the |S|^2-radial (transverse fiber-embedding amplitude) mode of the
substrate order parameter. Its dressed mass is the bare quartic PLUS the self-energy
from decay into the substrate's OWN two-quasiparticle (B2/B3) pair-breaking continuum.
The flow is D_K (0,0)-eigenvalues -> bare quartic [the +5.36% overshoot] ->
Pekker-Varma continuum self-energy Re Sigma [the dressing] -> dressed m_H -> PDG.

The amplitude-mode self-energy (Pekker-Varma 1406.2968; the substrate's S43-W6 Fano
machinery for the IMAGINARY part):
    Sigma(omega) = sum_j |V_{Hj}|^2 * integral d_Omega rho_j(Omega) / (omega - Omega + i eps)
    Re Sigma(omega) = sum_j |V_{Hj}|^2 * P integral d_Omega rho_j(Omega) / (omega - Omega)   [Kramers-Kronig]
    Im Sigma(omega) = pi * sum_j |V_{Hj}|^2 rho_j(omega)                                       [S43-W6, existing]

The two-quasiparticle continuum channel j=(a,b) (a Cooper pair broken into one
quasiparticle in band a + one in band b) has:
    threshold  Omega_thr,j = Delta_a + Delta_b
    joint DOS  weight       proportional to rho_a * rho_b
    coupling   |V_{Hj}|^2   = Higgs-continuum vertex (V_B2B2 for the dominant B2 channel,
                              scaled by the relative joint-DOS weight per channel).

SIGN (the load-bearing directional prediction; executed, NOT assumed — math-scripts.md
"Double-Check Logic Before Compute"):
  Step 1: Re Sigma(omega) = sum_j |V_Hj|^2 P int_{thr_j}^{thr_j+W} rho_j(Omega)/(omega-Omega) dOmega
          [rho_j>=0, |V_Hj|^2>=0; canonical Pekker-Varma].
  Step 2: substrate continuum weight lives in Omega in [2 Delta_B3, 2 Delta_B2] = [0.168, 1.464]
          M_KK (dominant weight at the B2 channels: rho_B2=14.67 >> rho_B1,rho_B3).
  Step 3 (PRIMARY, omega = omega_H3 = 11.465): for EVERY continuum state Omega <= 1.464
          < 11.465 => (omega_H3 - Omega) > 0 for ALL Omega in support.
  Step 4: integrand = (rho_j>=0)/((omega-Omega)>0) = POSITIVE everywhere => P int > 0
          => Re Sigma(omega_H3) > 0  (a discrete mode FAR ABOVE a continuum is repelled
          UPWARD, away from the weight below it).
  Step 5: Re Sigma(omega_H3) > 0 => dressed mode pushed UP => SIGN POSITIVE at omega_H3,
          OPPOSITE to the plan's pre-registered Re Sigma < 0.

  The plan's "amplitude-mode softening toward 2 Delta" (Re Sigma<0) is the physics of a
  mode sitting just ABOVE the 2 Delta threshold being pulled DOWN. That is omega_H2's
  situation (omega_H2=1.410 INSIDE/near the band top 2 Delta_B2=1.464), NOT omega_H3's.
  This gate computes BOTH and reports the verdict at the pre-registered PRIMARY (omega_H3,
  the |S|^2 m_H carrier) with omega_H2 as the cross-check that localizes where the
  softening actually lives.

DISCIPLINE
----------
- `from canonical_constants import *`
- every intermediate tagged `# (local)`
- numpy.linalg per plan GPU_path (the PV-integral is a 1-D frequency-grid reduction;
  the DOS rho_2qp is built from cached (0,0)-sector eigenvalues -> no >=100x100 dense
  diagonalization; OMP capped at 8 per math-scripts.md CPU fallback)
- SHA-256 of all inputs logged in first 20 lines of stdout
- dual-SHA (audit + content) emitted (S84+)
- 4-tuple printed as final non-verdict line
- verdict via print_verdict_payload -> agent calls emit_verdict (race-safe)

Author: landau-condensed-matter-theorist (Investigation 5, Wave 2, gate W2-3)
Date: 2026-06-15
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU-fallback thread cap (math-scripts.md)
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

t0 = time.time()  # (local)

# ---------------------------------------------------------------------------
# Section 1 — canonical-constants import (MANDATORY; S34+)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path.cwd()                                # (local)
_SHARED = (PROJECT_ROOT / "computations" / "_shared").resolve()  # (local)
sys.path.insert(0, str(_SHARED))
from canonical_constants import (  # noqa: E402
    Delta_BCS,
    m_H_FW_KK_threshold,
    m_H_obs,
    omega_H2,
    omega_H3,
    rho_B2_per_mode,
    Gamma_effacement,
    M_KK,
)

# ---------------------------------------------------------------------------
# Section 2 — identity / scheme / convention pins
# ---------------------------------------------------------------------------
SESSION = "5"  # investigation number (track="investigation")
GATE_ID = "INV5-W2-3-PEKKER-VARMA-HIGGS-SELF-ENERGY"
SCHEME = "PEKKER-VARMA-CONTINUUM-SELF-ENERGY"
CONVENTION = "REAL-PART-DISPERSIVE-SHIFT-KRAMERS-KRONIG"
L_MAX = "10"
TRIGGER = "[SIGN]"

# Pre-registered gate thresholds (plan §W2-3 strict_PASS_boundary; gate-block pins
# frozen at plan-freeze, single-gate-specific — not framework constants).
TARGET_FRAC = -(67.0 / 1251.0)   # (local) -5.35572% EXACT = -(m_H_FW/m_H_obs - 1)
TOL_PASS = 0.01                  # (local) 1 pp absolute on the fractional shift
TOL_INFO = 0.03                  # (local) 3 pp INFO band

# Output destinations (investigation track)
SESSION_DIR = (PROJECT_ROOT / "computations" / "investigation-5").resolve()  # (local)
OUT_NPZ = SESSION_DIR / "inv5_w2_3_pekker_varma_higgs_self_energy.npz"
OUT_PNG = SESSION_DIR / "inv5_w2_3_pekker_varma_higgs_self_energy.png"

# Input caches
S48_LEGGETT = (PROJECT_ROOT / "computations" / "session-48" / "s48_leggett_mode.npz").resolve()      # (local)
S43_FANO = (PROJECT_ROOT / "computations" / "session-43" / "s43_fano_continuum.npz").resolve()        # (local)
S54_HIGGS = (PROJECT_ROOT / "computations" / "session-54" / "s54_higgs_modulus.npz").resolve()        # (local)

INPUT_FILES = [
    _SHARED / "canonical_constants.py",
    S48_LEGGETT,
    S43_FANO,
    S54_HIGGS,
]


# ---------------------------------------------------------------------------
# Section 3/4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def re_sigma_pv(omega, channels, Vsq_per_channel, W_band, n_grid=400001, eps_frac=5.0):
    """Kramers-Kronig REAL part of the amplitude-mode self-energy at frequency omega.

    Re Sigma(omega) = sum_j |V_Hj|^2 * P int_{thr_j}^{thr_j+W} rho_j(Omega)/(omega-Omega) dOmega

    Each channel j is a flat (constant-DOS) two-quasiparticle continuum shelf of
    bandwidth W_band above its pair-breaking threshold thr_j, normalized to unit
    integrated DOS, weighted by the joint-DOS weight w_j (carried inside
    Vsq_per_channel as |V_Hj|^2 * w_j_norm). Principal value: the pole (if omega is
    inside a shelf) is excised symmetrically over a window eps_frac*dOmega (the iε
    prescription, eps->0; symmetric excision is the standard PV regulator and gives
    a vanishing principal-value contribution at the pole by oddness).
    """
    tot = 0.0  # (local)
    per_channel = {}  # (local)
    for (name, thr), Vsq in zip(channels, Vsq_per_channel):
        Om = np.linspace(thr, thr + W_band, n_grid)  # (local)
        dOm = Om[1] - Om[0]  # (local)
        dens = np.full_like(Om, 1.0 / W_band)         # (local) normalized shelf rho_j
        denom = omega - Om                            # (local)
        integ = dens / denom                          # (local)
        bad = np.abs(denom) < eps_frac * dOm          # (local) symmetric PV excision
        integ[bad] = 0.0
        contrib = Vsq * np.trapezoid(integ, Om)       # (local) numpy 2.x: trapezoid
        per_channel[name] = contrib
        tot += contrib
    return tot, per_channel


def compute() -> dict:
    # --- load substrate caches -------------------------------------------------
    d48 = np.load(S48_LEGGETT, allow_pickle=True)  # (local)
    d43 = np.load(S43_FANO, allow_pickle=True)     # (local)
    d54 = np.load(S54_HIGGS, allow_pickle=True)    # (local)

    Delta_fold = np.asarray(d48["Delta_fold"], dtype=float)  # (local) [DB1,DB2,DB3]
    rho_fold = np.asarray(d48["rho_fold"], dtype=float)      # (local) [rB1,rB2,rB3]
    DB1, DB2, DB3 = float(Delta_fold[0]), float(Delta_fold[1]), float(Delta_fold[2])  # (local)
    rB1, rB2, rB3 = float(rho_fold[0]), float(rho_fold[1]), float(rho_fold[2])        # (local)

    V_B2B2 = float(np.asarray(d43["V_B2B2"]).ravel()[0])     # (local) Higgs-continuum vertex
    Delta_pair = float(np.asarray(d43["Delta_pair"]).ravel()[0])  # (local) = Delta_BCS
    H_ss = float(np.asarray(d54["H_ss_phys"]).ravel()[0])    # (local) |S|^2 radial Hessian

    # --- substrate-canonical anchors ------------------------------------------
    two_delta_bcs = 2.0 * Delta_BCS                          # (local) 0.92851 edge
    m_H_resid = m_H_FW_KK_threshold / m_H_obs - 1.0          # (local) +5.356% (cross-check)

    # --- build the B2/B3 two-quasiparticle pair-breaking continuum channels ----
    # Channel j=(a,b): threshold Delta_a+Delta_b, joint-DOS weight rho_a*rho_b.
    band = [("B1", DB1, rB1), ("B2", DB2, rB2), ("B3", DB3, rB3)]  # (local)
    channels = []           # (local) [(name, thr), ...]
    joint_w = []            # (local) joint-DOS weight per channel
    for i, (na, Da, ra) in enumerate(band):
        for (nb, Db, rb) in band[i:]:
            channels.append((f"{na}+{nb}", Da + Db))
            joint_w.append(ra * rb)
    joint_w = np.asarray(joint_w, dtype=float)              # (local)
    w_norm = joint_w / joint_w.sum()                        # (local) normalized weights

    # Coupling: |V_Hj|^2 = (Higgs-continuum vertex)^2 * (normalized joint-DOS weight)
    Vsq = (V_B2B2 ** 2) * w_norm                            # (local)

    # Continuum bandwidth above threshold (substrate-natural: one pair-breaking
    # gap-scale 2 Delta_BCS of spectral support above each channel edge).
    W_band = two_delta_bcs                                  # (local)

    # --- eps -> 0 extrapolation of the PV integral -----------------------------
    eps_fracs = [10.0, 5.0, 2.0]   # (local) shrinking symmetric PV excision windows
    ReS_H3_eps = []   # (local)
    ReS_H2_eps = []   # (local)
    for ef in eps_fracs:
        rs3, _ = re_sigma_pv(omega_H3, channels, Vsq, W_band, eps_frac=ef)
        rs2, _ = re_sigma_pv(omega_H2, channels, Vsq, W_band, eps_frac=ef)
        ReS_H3_eps.append(rs3)
        ReS_H2_eps.append(rs2)
    # primary values at the smallest excision (eps->0)
    ReS_H3, per_ch_H3 = re_sigma_pv(omega_H3, channels, Vsq, W_band, eps_frac=2.0)
    ReS_H2, per_ch_H2 = re_sigma_pv(omega_H2, channels, Vsq, W_band, eps_frac=2.0)

    # --- imaginary part at each mode (S43-W6 machinery, cross-check) -----------
    # Im Sigma(omega) = pi * sum_j |V_Hj|^2 rho_j(omega); rho_j(omega)=1/W if inside shelf.
    def im_sigma(omega):
        s = 0.0  # (local)
        for (name, thr), v in zip(channels, Vsq):
            if thr <= omega <= thr + W_band:
                s += v * (1.0 / W_band)
        return np.pi * s
    ImS_H3 = im_sigma(omega_H3)  # (local)
    ImS_H2 = im_sigma(omega_H2)  # (local)

    # --- fractional shifts (normalized by m_H = the |S|^2 carrier omega_H3) -----
    # The gate's deliverable: Re Sigma_continuum / m_H. m_H is the |S|^2-radial mode
    # = omega_H3 (the framework m_H carrier). Report both normalizations for clarity.
    frac_H3_over_mH = ReS_H3 / omega_H3        # (local) PRIMARY (m_H = omega_H3)
    frac_H2_over_mH = ReS_H2 / omega_H3        # (local) cross-check normalized by m_H
    frac_H2_over_own = ReS_H2 / omega_H2       # (local) cross-check normalized by own freq

    # --- PRE-REGISTERED VERDICT (primary = omega_H3, the |S|^2 m_H carrier) -----
    primary_frac = frac_H3_over_mH             # (local) Re Sigma/m_H at omega_H3

    # SIGN sub-test (load-bearing): Re Sigma < 0
    sign_predicted = "NEG"                     # (local) plan Step 5
    sign_computed = "NEG" if ReS_H3 < 0 else "POS"  # (local)
    sign_verdict = "PASS" if sign_computed == "NEG" else "FAIL"  # (local)

    # MAGNITUDE sub-test: |primary_frac - TARGET_FRAC|
    mag_dist = abs(primary_frac - TARGET_FRAC)  # (local)
    if mag_dist <= TOL_PASS:
        magnitude_verdict = "PASS"  # (local)
    elif mag_dist <= TOL_INFO:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)

    # REGIME: the PV integral is well-defined (regulator-stable across eps windows);
    # the model is the flat-shelf two-quasiparticle continuum throughout the band.
    eps_spread_H3 = max(ReS_H3_eps) - min(ReS_H3_eps)  # (local)
    regime_verdict = "VALID" if abs(eps_spread_H3) < 0.05 * max(abs(np.mean(ReS_H3_eps)), 1e-9) + 1e-3 else "MARGINAL"  # (local)

    # Composite collapse (gate-verdicts.md PRE-REGISTERED rule):
    if regime_verdict == "BREAKDOWN":
        verdict = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        verdict = "INFO"
    elif magnitude_verdict == "INFO":
        verdict = "INFO"
    else:
        verdict = "PASS"

    # --- assemble ---------------------------------------------------------------
    result = {
        "value": (
            f"ReSigma_mH(omega_H3)={primary_frac*100:.4f}%|"
            f"ReSigma_H3={ReS_H3:+.5f}|sign={sign_computed}|"
            f"target=-5.3557%|"
            f"ReSigma_H2={ReS_H2:+.5f}|frac_H2/mH={frac_H2_over_mH*100:.4f}%|"
            f"frac_H2/own={frac_H2_over_own*100:.4f}%|Gamma_eff={Gamma_effacement}"
        ),
        "verdict": verdict,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        # numeric record
        "primary_frac": primary_frac,
        "ReS_H3": ReS_H3,
        "ReS_H2": ReS_H2,
        "frac_H3_over_mH": frac_H3_over_mH,
        "frac_H2_over_mH": frac_H2_over_mH,
        "frac_H2_over_own": frac_H2_over_own,
        "ImS_H3": ImS_H3,
        "ImS_H2": ImS_H2,
        "target_frac": TARGET_FRAC,
        "mag_dist": mag_dist,
        "eps_spread_H3": eps_spread_H3,
        "channels": channels,
        "thresholds": np.asarray([thr for _, thr in channels], dtype=float),
        "joint_w_norm": w_norm,
        "Vsq": Vsq,
        "V_B2B2": V_B2B2,
        "W_band": W_band,
        "two_delta_bcs": two_delta_bcs,
        "DB": np.asarray([DB1, DB2, DB3], dtype=float),
        "rho": np.asarray([rB1, rB2, rB3], dtype=float),
        "H_ss": H_ss,
        "m_H_resid": m_H_resid,
        "per_ch_H3": per_ch_H3,
        "per_ch_H2": per_ch_H2,
        "ReS_H3_eps": np.asarray(ReS_H3_eps, dtype=float),
        "ReS_H2_eps": np.asarray(ReS_H2_eps, dtype=float),
        "eps_fracs": np.asarray(eps_fracs, dtype=float),
    }
    return result


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
def make_plot(r):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # (a) Re Sigma(omega) swept across frequency, with the continuum band + Higgs modes
    ax = axes[0]
    channels = r["channels"]  # (local)
    Vsq = r["Vsq"]            # (local)
    W = r["W_band"]           # (local)
    om_grid = np.linspace(0.02, 13.0, 1600)  # (local)
    ReS_grid = []  # (local)
    for om in om_grid:
        s = 0.0  # (local)
        for (name, thr), v in zip(channels, Vsq):
            Om = np.linspace(thr, thr + W, 4001)  # (local)
            dOm = Om[1] - Om[0]  # (local)
            integ = (1.0 / W) / (om - Om)  # (local)
            bad = np.abs(om - Om) < 3 * dOm  # (local)
            integ[bad] = 0.0
            s += v * np.trapezoid(integ, Om)
        ReS_grid.append(s)
    ReS_grid = np.asarray(ReS_grid)  # (local)
    ax.axhline(0.0, color="k", lw=0.7)
    ax.axvspan(min(t for _, t in channels), max(t for _, t in channels) + W,
               color="orange", alpha=0.12, label="2-qp continuum band")
    ax.plot(om_grid, ReS_grid, "b-", lw=1.6, label=r"$\mathrm{Re}\,\Sigma(\omega)$")
    ax.axvline(omega_H2, color="green", ls="--", lw=1.3, label=fr"$\omega_{{H2}}={omega_H2}$ (hybrid x-check)")
    ax.axvline(omega_H3, color="red", ls="--", lw=1.3, label=fr"$\omega_{{H3}}={omega_H3}$ (|S|$^2$ PRIMARY)")
    ax.plot([omega_H3], [r["ReS_H3"]], "ro", ms=8)
    ax.plot([omega_H2], [r["ReS_H2"]], "go", ms=8)
    ax.set_xlabel(r"$\omega$  (M$_{KK}$)")
    ax.set_ylabel(r"$\mathrm{Re}\,\Sigma(\omega)$  (M$_{KK}$)")
    ax.set_title("Pekker-Varma amplitude-mode self-energy (real part)")
    ax.legend(fontsize=7, loc="best")
    ax.grid(alpha=0.3)

    # (b) fractional shift vs target -5.356%, both modes + bands
    ax = axes[1]
    labels = [r"$\omega_{H3}$ (PRIMARY, /m_H)", r"$\omega_{H2}$ (/m_H)", r"$\omega_{H2}$ (/own)"]
    vals = [r["frac_H3_over_mH"] * 100, r["frac_H2_over_mH"] * 100, r["frac_H2_over_own"] * 100]
    colors = ["red", "green", "darkgreen"]
    ax.bar(range(3), vals, color=colors, alpha=0.7)
    tgt = r["target_frac"] * 100  # (local)
    ax.axhline(tgt, color="purple", ls="-", lw=1.6, label=fr"target $-5.356\%$ ($-67/1251$)")
    ax.axhspan(tgt - 1, tgt + 1, color="purple", alpha=0.15, label="PASS band (±1pp)")
    ax.axhspan(tgt - 3, tgt + 3, color="purple", alpha=0.07, label="INFO band (±3pp)")
    ax.axhline(0.0, color="k", lw=0.7)
    ax.set_xticks(range(3))
    ax.set_xticklabels(labels, fontsize=7)
    ax.set_ylabel(r"$\mathrm{Re}\,\Sigma/m_H$  (%)")
    ax.set_title("Fractional shift vs the -5.356% Higgs residual")
    ax.legend(fontsize=7, loc="best")
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"{GATE_ID}\n"
        f"PRIMARY (omega_H3=11.465): ReSigma/m_H={r['frac_H3_over_mH']*100:+.3f}%  "
        f"sign={'NEG' if r['ReS_H3']<0 else 'POS'}  ->  {r['verdict']}",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    payload = {
        "session": int(SESSION),
        "track": "investigation",
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


def emit_4tuple(value, scheme, convention, L_max):
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = _SHARED / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    # numeric report
    print("--- substrate inputs ---")
    print(f"  (0,0) gaps  Delta_B[1,2,3] = {r['DB']}  M_KK")
    print(f"  (0,0) DOS   rho_B[1,2,3]   = {r['rho']}")
    print(f"  Higgs-continuum vertex V_B2B2 = {r['V_B2B2']:.6f}  (Vsq channel-weighted)")
    print(f"  2*Delta_BCS pair-breaking edge = {r['two_delta_bcs']:.6f}  M_KK")
    print(f"  continuum bandwidth W = {r['W_band']:.6f}  M_KK")
    print(f"  channels (thr): {[(n, round(t,4)) for n,t in r['channels']]}")
    print(f"  joint-DOS norm weights: {np.round(r['joint_w_norm'],4)}")
    print("--- self-energy ---")
    print(f"  Re Sigma(omega_H3={omega_H3}) = {r['ReS_H3']:+.6f}  M_KK  (PRIMARY, |S|^2 carrier)")
    print(f"  Re Sigma(omega_H2={omega_H2}) = {r['ReS_H2']:+.6f}  M_KK  (hybrid cross-check)")
    print(f"  eps->0 spread (H3): {r['eps_spread_H3']:.3e}  (regime stability)")
    print(f"  Im Sigma(omega_H3) = {r['ImS_H3']:.6f}   Im Sigma(omega_H2) = {r['ImS_H2']:.6f}")
    print("--- fractional shifts ---")
    print(f"  Re Sigma/m_H (omega_H3, PRIMARY) = {r['frac_H3_over_mH']*100:+.4f}%")
    print(f"  Re Sigma/m_H (omega_H2)          = {r['frac_H2_over_mH']*100:+.4f}%")
    print(f"  Re Sigma/omega_H2 (own-freq)     = {r['frac_H2_over_own']*100:+.4f}%")
    print(f"  TARGET = -5.3557% (= -67/1251 exact);  m_H residual r_KK = +{r['m_H_resid']*100:.4f}%")
    print(f"  |primary - target| = {r['mag_dist']:.5f}  (PASS<= {TOL_PASS}, INFO<= {TOL_INFO})")
    print("--- 3-tuple ---")
    print(f"  sign={r['sign_verdict']}  magnitude={r['magnitude_verdict']}  regime={r['regime_verdict']}")

    # save npz
    save = {k: v for k, v in r.items()
            if k not in ("channels", "per_ch_H3", "per_ch_H2", "verdict",
                         "sign_verdict", "magnitude_verdict", "regime_verdict", "value")}
    save["channel_names"] = np.asarray([n for n, _ in r["channels"]])
    save["verdict"] = r["verdict"]
    save["sign_verdict"] = r["sign_verdict"]
    save["magnitude_verdict"] = r["magnitude_verdict"]
    save["regime_verdict"] = r["regime_verdict"]
    np.savez(OUT_NPZ, **save)
    print(f"\nsaved: {OUT_NPZ}")

    make_plot(r)
    print(f"saved: {OUT_PNG}")

    tag = emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    print_verdict_payload(
        r["verdict"], r["value"], audit_sha, content_sha,
        sign_verdict=r["sign_verdict"],
        magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['verdict']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
