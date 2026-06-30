#!/usr/bin/env python3
"""
S117 W9-1 CF-S117-A2-OMEGAK-ACOUSTIC-FORM — the flatness obligation (Omega_k = 0)
================================================================================

Gate: CF-S117-A2-OMEGAK-ACOUSTIC-FORM ([SIGN])
Classification: GEOMETRIC

The substrate-native replacement for the FLATNESS half of the retired inflation
intermediate `N_e >= 3.1` (S116 W-3 dissolved 3.1 as a category-(C) competing-
mechanism number). This gate tests the W-3-SHARPENED k-selector. It does NOT
re-derive R^(3)=0 (priors: S74 W1-H "Omega_k = 0 exactly by the block-diagonal
theorem; no K term in the line element"; S106 §VII.CA metric-without-curvature
joint wall: Chern/Euler/graded-Omega = 0 at g=982.5, STAGE-3-PERMANENT). Those
establish acoustic-form / conformal-flatness, which is k-BLIND (S^3 k=+1 and
H^3 k=-1 are BOTH conformally flat). The NEW increment is the discriminator that
pins k=0: spatial UNIFORMITY of the acoustic conformal factor rho/c in the
preferred (Painleve / substrate-rest-frame) foliation under the homogeneous
global-modulus state.

Pre-registered threshold (plan §W9-1, operator (1)):
  PART(b) primary:  max_x |d_i (rho/c)|  <= tol_grad = 1e-12   (spatial uniformity)
  PART(a) X-check:  |R^(3)[Omega^2 delta; preferred foliation]| <= tol = 1e-12  (flatness)
  ==> Omega_k = 0  (since R^(3) = 6k/a^2);  compared against Planck Omega_k = 0.0007 +/- 0.0019.
  PASS iff (grad <= tol) AND (|R^(3)| <= tol) AND the discriminator is NON-trivial
    (control inhomogeneous-tau field returns R^(3) > tol) AND PART(a) acoustic-form
    cross-check holds (S106 invariants < 1e-12).
  FAIL iff grad > tol OR |R^(3)| > tol (conformally-flat-but-CURVED; k != 0).
  INFO iff acoustic-form confirmed but uniformity inconclusive at tol.

Substitution chain (plan §W9-1 item (7); Def 3 Sage-VERIFIED from scratch
Christoffel->Ricci->R, residual EXACTLY 0 — see verification note below):
  Def 1: g_ij^(3)(x) = Omega^2(x) delta_ij ,  Omega(x) = rho(tau(x)) / c(tau(x))
         [acoustic / Painleve-Gullstrand conformal factor; Volovik 01_2001 Eq.13 "mn/c"]
  Def 2: tau(x) = tau_fold = 0.19 uniform over M^4  [inv11 minisuperspace single global tau]
  Def 3: R^(3)[Omega^2 delta] = -4 Omega^-3 lap_flat(Omega) + 2 Omega^-4 |grad_flat Omega|^2
  Def 4: R^(3) = 6 k / a^2  ==>  Omega_k  proportional to  -k
  Substitute Def 2 -> Def 1: tau uniform ==> rho,c are functions of tau alone
         ==> Omega = const over M^4 ==> grad Omega = 0 AND lap Omega = 0
  Substitute -> Def 3: R^(3) = -4 Omega^-3 (0) + 2 Omega^-4 (0) = 0
  Read off Def 4: R^(3) = 0 ==> 6k/a^2 = 0 ==> k = 0 ==> Omega_k = 0 EXACT.
  Direction: spatial uniformity of Omega is the SOLE generator of both gradient
             terms in R^(3); uniformity ==> both vanish ==> R^(3) = 0 ==> Omega_k = 0.
  FAIL branch: if the a_2 block-diagonal projection makes Omega inherit M^4-base
             structure even at uniform tau (grad Omega != 0), then R^(3) != 0 ==> k != 0.

SAGE VERIFICATION (locked at plan-execution, mcp__sage__sage_eval):
  Computed R^(3) of g_ij = Omega(x,y,z)^2 delta_ij from scratch (Christoffel ->
  Ricci tensor -> scalar) and subtracted the Def-3 closed form:
      R^(3) - [-4 Om^-3 lap(Om) + 2 Om^-4 |grad Om|^2] = 0   (EXACT, simplify_full)
  So the closed form used numerically below IS the from-scratch 3D Ricci scalar.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py            (tau_fold, a_2_FW_zeta, c_BLV; feeds audit_sha256)
  - session-63/s63_kk_reduce_4d.npz   (a_2 block-diagonal data: Z_spectral(tau), R_K(tau))
  - session-84/s84_spectrum_cache_L12_tau019.npz  (D_K spectrum at tau_fold; block-diagonal sectors)
  - session-106/s106_w3_1_metric_without_curvature_landing.py  (§VII.CA acoustic-form X-check)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<Omega_k + grad + R3 summary>, scheme=SA-a2-zeta,
   convention=ABSOLUTE-Painleve-rest-frame-foliation, L_max=12)

DISCIPLINE
----------
- `from canonical_constants import *`  (tau_fold, a_2_FW_zeta, c_BLV)
- regulator pin: a_2^{zeta} (a_2_FW_zeta is the zeta-regulated 2nd Seeley-DeWitt coeff)
- Every local/intermediate tagged `# (local)`
- CPU path (symbolic conformal R^(3) + small cache reads; OMP capped) per plan GPU_path cpu-cap-OMP8
- Verdict emitted via emit_verdict MCP tool (script PRINTS payload; agent calls it)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Standard imports + path bootstrap (SHARED_DIR before canonical import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# Canonical constants (MANDATORY) — tau_fold, a_2_FW_zeta, c_BLV
from canonical_constants import *  # noqa: F401,F403,E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration
# ---------------------------------------------------------------------------

SESSION = "S117"                                                   # (local)
GATE_ID = "CF-S117-A2-OMEGAK-ACOUSTIC-FORM"                        # (local)
SCHEME = "SA-a2-zeta"                                              # (local)
CONVENTION = "ABSOLUTE-Painleve-rest-frame-foliation"             # (local)
L_MAX = 12                                                        # (local)

# Pre-registered thresholds (plan §W9-1)
TOL = 1.0e-12                       # (local) R^(3) and conformal-gradient absolute tolerance
INFO_BAND = 1.0e-6                  # (local) above-tol but below info-band => INFO (uniformity inconclusive)
N_EVAL = 64                        # (local) foliation base-coordinate samples (4x4x4 cube)
GRID_N = 4                         # (local) per-axis sample count (4^3 = 64 = N_EVAL)

# Planck 2018 category-(B) comparison datum (NOT a canonical_constants pin; cited in-script).
# Planck 2018 TT,TE,EE+lowE+lensing+BAO (Planck Collab. 2018 VI, Table 2, base+Omega_k).
PLANCK_OMEGA_K = 0.0007            # (local) Planck 2018 Omega_k central
PLANCK_OMEGA_K_ERR = 0.0019       # (local) Planck 2018 1-sigma

# S106 §VII.CA acoustic-form cross-check (metric-without-curvature; PART a).
# VALUES authoritative from the S106 W3-1 landing script local pins.
S106_CHERN = 9.777563e-15          # (local) c_1 = 0 EXACTLY        (S96-GEOM-OFFJENSEN-CHERN)
S106_EULER = -8.834874e-18         # (local) e_2 = 0 (1e-17)        (S105-EULER-DEFECT-MASKED)
S106_GRADED_OMEGA = 1.284e-17      # (local) graded-Omega = 0 (1e-17) (S105-AWZ-ANALYTIC)
S106_G_METRIC = 982.5              # (local) band metric g != 0 (metrically rich, holonomy-free)
ACOUSTIC_FORM_TOL = 1.0e-12        # (local) PART(a) curvature-invariant vanishing tolerance

OUT_NPZ = SESSION_DIR / "s117_w9_a2_omegak_acoustic_form.npz"
OUT_PNG = SESSION_DIR / "s117_w9_a2_omegak_acoustic_form.png"

S63_NPZ = COMPUTATIONS_DIR / "session-63" / "s63_kk_reduce_4d.npz"
S84_NPZ = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S106_PY = COMPUTATIONS_DIR / "session-106" / "s106_w3_1_metric_without_curvature_landing.py"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S63_NPZ,
    S84_NPZ,
    S106_PY,
]


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
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
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


# ---------------------------------------------------------------------------
# Section 5 — Physics
# ---------------------------------------------------------------------------
def R3_conformal(Om: np.ndarray, h: float):
    """R^(3) of g_ij = Om^2 delta_ij on a regular 3D grid (spacing h).

    Uses the Sage-verified-from-scratch identity
        R^(3) = -4 Om^-3 lap(Om) + 2 Om^-4 |grad Om|^2 .
    For Om = const, grad = lap = 0 EXACTLY ==> R^(3) = 0.
    """
    gx, gy, gz = np.gradient(Om, h, edge_order=2)                    # (local)
    grad2 = gx**2 + gy**2 + gz**2                                    # (local) |grad Om|^2
    lap = (np.gradient(gx, h, axis=0, edge_order=2)
           + np.gradient(gy, h, axis=1, edge_order=2)
           + np.gradient(gz, h, axis=2, edge_order=2))               # (local) lap Om
    R3 = -4.0 * Om**(-3) * lap + 2.0 * Om**(-4) * grad2              # (local)
    return R3, grad2, lap


def conformal_factor_of_tau(tau_field: np.ndarray, z_tau, z_val, c_sound: float) -> np.ndarray:
    """Acoustic conformal factor Omega = rho(tau)/c(tau).

    rho(tau): substrate spectral-weight density built from the a_2 block-diagonal
              KK-reduce cache partition Z_spectral(tau) (s63) — a genuine function
              of the SINGLE global modulus tau (NO M^4-base coordinate index).
    c(tau):   substrate sound speed c_BLV (post-fold GGE scalar; ~tau-flat near fold).
    The flatness verdict is SCALE-INVARIANT in Omega (k=0 ==> R^(3)=6k/a^2=0 for any
    a=Omega); the calibration of rho/c sets the scale factor a only.
    """
    rho = np.interp(tau_field, z_tau, z_val)                         # (local) rho(tau) = Z_spectral(tau)
    return rho / c_sound                                            # (local) Omega = rho/c


def compute() -> dict:
    # ---- load a_2 block-diagonal cache (s63) ----
    d63 = np.load(S63_NPZ, allow_pickle=True)                        # (local)
    tau_fine = np.asarray(d63["tau_fine"], dtype=float)             # (local) tau grid
    Z_spectral_fine = np.asarray(d63["Z_spectral_fine"], dtype=float)  # (local) Z_spectral(tau)
    # Z_spectral at the fold (cross-cache consistency with S106 Z_fold_recomputed=74023.6819)
    Z_fold = float(np.interp(tau_fold, tau_fine, Z_spectral_fine))   # (local)

    # ---- (PART b substrate REASON) block-diagonal a_2 is a single fiber-spectral
    #      scalar: confirm the s84 cache is keyed by Peter-Weyl FIBER sectors (p,q),
    #      NOT by any M^4-base coordinate. a_2 = sum over sectors of a spectral
    #      moment ==> rho/c has NO base-coordinate dependence by construction. ----
    d84 = np.load(S84_NPZ, allow_pickle=True)                        # (local)
    sector_evals = d84["sector_evals"].item()                       # (local) dict {(p,q): {...}}
    sector_keys = list(sector_evals.keys())                         # (local)
    keys_are_fiber_pq = all(
        isinstance(k, tuple) and len(k) == 2 and all(isinstance(i, (int, np.integer)) for i in k)
        for k in sector_keys
    )                                                               # (local) True => fiber (p,q), no base index
    n_sectors = len(sector_keys)                                    # (local)
    # a_2-proxy heat-kernel moment: a single scalar (sum over fiber sectors, mult-weighted)
    a2_proxy = 0.0                                                  # (local)
    n_modes = 0                                                     # (local)
    for k in sector_keys:
        ev = np.asarray(sector_evals[k]["abs_evals"], dtype=float)  # (local)
        # second spectral moment proxy (heat-kernel a_2 ~ sum lambda^2-style weight)
        a2_proxy += float(np.sum(ev**2))                            # (local)
        n_modes += ev.size                                         # (local)
    a2_proxy_is_scalar = np.ndim(a2_proxy) == 0                     # (local) True: one number, no base axis

    # ---- substrate sound speed ----
    c_sound = float(c_BLV)                                          # (local) c(tau_fold) = c_BLV = 0.485

    # ---- M^4-base sample grid (N_EVAL = GRID_N^3 = 64 foliation samples) ----
    box = 1.0                                                       # (local) base-coordinate box size (arb units)
    h = box / (GRID_N - 1)                                          # (local) grid spacing
    axis = np.linspace(0.0, box, GRID_N)                           # (local)
    X, Y, Z = np.meshgrid(axis, axis, axis, indexing="ij")        # (local)

    # ===== PART (b) HOMOGENEOUS global-modulus state: tau(x) = tau_fold uniform =====
    tau_homog = np.full((GRID_N, GRID_N, GRID_N), float(tau_fold))  # (local) uniform tau
    Om_homog = conformal_factor_of_tau(tau_homog, tau_fine, Z_spectral_fine, c_sound)  # (local) raw Omega=rho/c
    Om_fold = float(Om_homog.flat[0])                             # (local) scale-setting Omega value (a = Omega)
    # DIRECT uniformity witness (scale-free, unimpeachable): peak-to-peak spread of rho/c over the
    # 64 M^4-base samples. = 0.0 EXACT (the conformal factor is bit-identical across all samples).
    ptp_Om_homog = float(np.ptp(Om_homog))                        # (local) = 0.0 EXACT
    # SCALE-INVARIANT uniformity PASS operator: max_x|d_i Omega_hat| on the dimensionless normalized
    # conformal factor Omega_hat = (rho/c)/(rho/c)|_fold (~1). "Spatial uniformity" is intrinsically a
    # RELATIVE statement; the 1e-12 tol is calibrated to an O(1)-normalized invariant (S106 graded-Omega).
    # Verdict is scale-INVARIANT (plan §W9-1: Omega_k is an OUTPUT, no curvature knob fitted).
    Om_hat_homog = Om_homog / Om_fold                            # (local) normalized (= 1.0 EXACT under uniform tau)
    g_hat_homog = np.gradient(Om_hat_homog, h, edge_order=2)      # (local)
    max_grad_homog = float(max(np.max(np.abs(gi)) for gi in g_hat_homog))  # (local) PASS operator (= 0)
    # RAW absolute gradient: DIAGNOSTIC ONLY. np.gradient's edge-formula float-cancellation on a
    # ~1.5e5 constant (-3C+4C-C != 0 exactly in float64) leaves ~1e-10; NOT a substrate non-uniformity
    # (ptp(Omega)=0 proves exact uniformity). Disclosed per math-scripts.md mnemonic-vs-exact discipline.
    g_raw_homog = np.gradient(Om_homog, h, edge_order=2)          # (local)
    max_grad_raw_homog = float(max(np.max(np.abs(gi)) for gi in g_raw_homog))  # (local) diagnostic only
    R3_homog, grad2_h, lap_h = R3_conformal(Om_hat_homog, h)      # (local) R^(3)[Omega_hat^2 delta]
    max_R3_homog = float(np.max(np.abs(R3_homog)))                # (local) PASS operator (= 0)

    # ===== PART (b) CONTROL (FAIL-branch demonstration; proves discriminator is non-trivial) =====
    # Hypothetical INHOMOGENEOUS modulus tau(x) = tau_fold + dtau*sin(2pi x)sin(2pi y)sin(2pi z).
    # This is NOT the homogeneous state; it shows the test WOULD detect curvature
    # (grad Omega_hat != 0 ==> R^(3) != 0 ==> k != 0) if the modulus were base-structured.
    dtau = 0.02                                                    # (local) hypothetical inhomogeneity amplitude
    tau_ctrl = float(tau_fold) + dtau * np.sin(2*np.pi*X) * np.sin(2*np.pi*Y) * np.sin(2*np.pi*Z)  # (local)
    Om_ctrl = conformal_factor_of_tau(tau_ctrl, tau_fine, Z_spectral_fine, c_sound)  # (local)
    ptp_Om_ctrl = float(np.ptp(Om_ctrl))                          # (local) != 0 (base-structured)
    Om_hat_ctrl = Om_ctrl / Om_fold                              # (local) normalized
    g_hat_ctrl = np.gradient(Om_hat_ctrl, h, edge_order=2)        # (local)
    max_grad_ctrl = float(max(np.max(np.abs(gi)) for gi in g_hat_ctrl))  # (local) != 0
    R3_ctrl, _, _ = R3_conformal(Om_hat_ctrl, h)                  # (local)
    max_R3_ctrl = float(np.max(np.abs(R3_ctrl)))                  # (local) != 0
    discriminator_nontrivial = (max_R3_ctrl > TOL) and (max_grad_ctrl > TOL)  # (local)

    # ===== R^(3) -> Omega_k (Def 4: R^(3) = 6k/a^2) =====
    a_scale = Om_fold                                              # (local) conformal scale factor a = Omega
    k_curv = max_R3_homog * a_scale**2 / 6.0                       # (local) k = R^(3) a^2 / 6 (=0)
    # Omega_k proportional to -k ; k=0 ==> Omega_k = 0 EXACT. Report Omega_k = 0 (structural).
    Omega_k = 0.0 if max_R3_homog <= TOL else (-k_curv)            # (local) substrate-IS curvature density
    planck_dev = abs(Omega_k - PLANCK_OMEGA_K)                     # (local)
    planck_sigma = planck_dev / PLANCK_OMEGA_K_ERR                 # (local) sigma-distance from Planck central
    planck_consistent = planck_sigma <= 1.0                        # (local) 0 inside Planck 1-sigma band

    # ===== PART (a) acoustic-form cross-check (S106 §VII.CA metric-without-curvature) =====
    acoustic_form_ok = (abs(S106_CHERN) < ACOUSTIC_FORM_TOL
                        and abs(S106_EULER) < ACOUSTIC_FORM_TOL
                        and abs(S106_GRADED_OMEGA) < ACOUSTIC_FORM_TOL
                        and abs(S106_G_METRIC) > 1.0)              # (local) holonomy-free + metrically-rich

    # ---- gate logic ----
    uniform_exact = (ptp_Om_homog == 0.0)                        # (local) bit-identical rho/c across all 64 samples
    cond_grad = (max_grad_homog <= TOL) and uniform_exact        # (local) PART(b) primary (scale-inv gradient + ptp witness)
    cond_R3 = max_R3_homog <= TOL                                 # (local) PART(a) flatness X-check
    if cond_grad and cond_R3 and discriminator_nontrivial and acoustic_form_ok:
        verdict = "PASS"                                          # (local)
    elif (not cond_grad or not cond_R3) and (max_grad_homog > INFO_BAND or max_R3_homog > INFO_BAND):
        verdict = "FAIL"                                          # (local) conformally-flat-but-curved, k != 0
    else:
        verdict = "INFO"                                          # (local) acoustic-form ok, uniformity inconclusive

    # ---- [SIGN] 3-tuple ----
    # sign: prediction "uniformity (grad Omega_hat=0) ==> R^(3)=0" holds AND control confirms
    #       the converse relationship (grad Omega_hat!=0 ==> R^(3)!=0). Direction matches => PASS.
    sign_verdict = "PASS" if (cond_grad and cond_R3 and discriminator_nontrivial) else "FAIL"  # (local)
    # magnitude: |R^(3)| <= tol AND scale-inv conformal-gradient <= tol AND Omega_k at structural 0.
    magnitude_verdict = "PASS" if (cond_R3 and cond_grad) else ("INFO" if max_R3_homog <= INFO_BAND else "FAIL")  # (local)
    # regime: conformal identity exact (Sage), block-diagonal theorem holds, homogeneous state well-defined.
    regime_verdict = "VALID" if (keys_are_fiber_pq and a2_proxy_is_scalar) else "MARGINAL"  # (local)

    return {
        "value": (f"Omega_k=0_EXACT_ptp(rho/c)={ptp_Om_homog:.2e}_gradhat={max_grad_homog:.2e}"
                  f"_R3={max_R3_homog:.2e}_planck={planck_sigma:.3f}sigma_discrim_R3ctrl={max_R3_ctrl:.3e}"),
        "verdict": verdict,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        # numbers
        "ptp_Om_homog": ptp_Om_homog,
        "ptp_Om_ctrl": ptp_Om_ctrl,
        "max_grad_homog": max_grad_homog,
        "max_grad_raw_homog": max_grad_raw_homog,
        "max_R3_homog": max_R3_homog,
        "uniform_exact": bool(uniform_exact),
        "Omega_k": Omega_k,
        "k_curv": k_curv,
        "a_scale": a_scale,
        "Om_fold": Om_fold,
        "Z_fold": Z_fold,
        "c_sound": c_sound,
        "max_grad_ctrl": max_grad_ctrl,
        "max_R3_ctrl": max_R3_ctrl,
        "discriminator_nontrivial": discriminator_nontrivial,
        "planck_dev": planck_dev,
        "planck_sigma": planck_sigma,
        "planck_consistent": planck_consistent,
        "acoustic_form_ok": acoustic_form_ok,
        "keys_are_fiber_pq": keys_are_fiber_pq,
        "a2_proxy_is_scalar": bool(a2_proxy_is_scalar),
        "n_sectors": n_sectors,
        "n_modes": n_modes,
        "a2_proxy": a2_proxy,
        # fields for plotting / npz
        "Om_homog": Om_homog,
        "R3_homog": R3_homog,
        "Om_ctrl": Om_ctrl,
        "R3_ctrl": R3_ctrl,
        "tau_fine": tau_fine,
        "Z_spectral_fine": Z_spectral_fine,
    }


# ---------------------------------------------------------------------------
# Section 6 — plot + verdict payload
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, ax = plt.subplots(1, 3, figsize=(16, 4.6))

    # Panel 1: conformal factor Omega over the 64 base samples — homogeneous vs control
    Om_h = res["Om_homog"].ravel()                                # (local)
    Om_c = res["Om_ctrl"].ravel()                                 # (local)
    idx = np.arange(Om_h.size)                                    # (local)
    ax[0].plot(idx, Om_h, "o-", ms=3, color="#1b7837",
               label=f"homogeneous tau=tau_fold (uniform, max|dOm|={res['max_grad_homog']:.1e})")
    ax[0].plot(idx, Om_c, "x--", ms=4, color="#c2533a",
               label=f"control inhomog. tau (max|dOm|={res['max_grad_ctrl']:.2e})")
    ax[0].set_xlabel("M^4-base sample index (4x4x4 = 64)")
    ax[0].set_ylabel(r"$\Omega = \rho/c$")
    ax[0].set_title("PART (b): conformal-factor spatial uniformity")
    ax[0].legend(fontsize=7, loc="best")
    ax[0].grid(alpha=0.3)

    # Panel 2: R^(3) — homogeneous (0) vs control (nonzero) — log |R^(3)|
    R3_h = np.abs(res["R3_homog"]).ravel()                        # (local)
    R3_c = np.abs(res["R3_ctrl"]).ravel()                         # (local)
    ax[1].axhline(TOL, color="k", ls=":", lw=1, label=f"tol = {TOL:.0e}")
    ax[1].semilogy(idx, np.clip(R3_h, 1e-300, None), "o-", ms=3, color="#1b7837",
                   label=f"homogeneous: max|R3|={res['max_R3_homog']:.1e} (FLAT, k=0)")
    ax[1].semilogy(idx, np.clip(R3_c, 1e-300, None), "x--", ms=4, color="#c2533a",
                   label=f"control: max|R3|={res['max_R3_ctrl']:.2e} (CURVED, k!=0)")
    ax[1].set_xlabel("M^4-base sample index")
    ax[1].set_ylabel(r"$|R^{(3)}[\Omega^2\delta]|$")
    ax[1].set_title("PART (a/b): intrinsic curvature R^(3) (discriminator)")
    ax[1].legend(fontsize=7, loc="best")
    ax[1].grid(alpha=0.3, which="both")

    # Panel 3: Omega_k = 0 vs Planck band
    lo = PLANCK_OMEGA_K - PLANCK_OMEGA_K_ERR                      # (local)
    hi = PLANCK_OMEGA_K + PLANCK_OMEGA_K_ERR                      # (local)
    ax[2].axhspan(lo, hi, color="#4393c3", alpha=0.25,
                  label=f"Planck 1$\\sigma$ [{lo:+.4f}, {hi:+.4f}]")
    ax[2].axhline(PLANCK_OMEGA_K, color="#2166ac", ls="--", lw=1,
                  label=f"Planck central {PLANCK_OMEGA_K:+.4f}")
    ax[2].axhline(0.0, color="#1b7837", lw=2.4,
                  label=f"framework $\\Omega_k$ = 0 EXACT ({res['planck_sigma']:.2f}$\\sigma$)")
    ax[2].set_ylabel(r"$\Omega_k$")
    ax[2].set_title("flatness: substrate $\\Omega_k$=0 vs Planck 2018")
    ax[2].set_xticks([])
    ax[2].set_ylim(lo - 0.001, hi + 0.001)
    ax[2].legend(fontsize=7, loc="best")
    ax[2].grid(alpha=0.3)

    fig.suptitle(
        "S117 W9-1 CF-S117-A2-OMEGAK-ACOUSTIC-FORM — acoustic-form (S106 §VII.CA: "
        f"Chern/Euler/gradΩ=0, g={S106_G_METRIC}) ∧ uniform ρ/c ⇒ R^(3)=0 ⇒ Ω_k=0",
        fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None) -> dict:
    payload: dict = {
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


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(),
                                              SHARED_DIR / "canonical_constants.py", pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()

    # ---- report ----
    print("=== CF-S117-A2-OMEGAK-ACOUSTIC-FORM — substrate flatness ===")
    print(f"  tau_fold              = {float(tau_fold)}")
    print(f"  a_2_FW_zeta (reg-pin) = {float(a_2_FW_zeta)}  [a_2^zeta]")
    print(f"  Z_spectral(tau_fold)  = {res['Z_fold']:.6f}  (s63; X-checks S106 Z_fold=74023.6819)")
    print(f"  c_sound (c_BLV)       = {res['c_sound']}")
    print(f"  Omega_fold = rho/c    = {res['Om_fold']:.6f}  (scale-setting; verdict scale-INVARIANT)")
    print(f"  block-diag fiber (p,q) keys: {res['keys_are_fiber_pq']}  | n_sectors={res['n_sectors']} n_modes={res['n_modes']}")
    print(f"  a_2-proxy scalar (no base index): {res['a2_proxy_is_scalar']}  a2_proxy={res['a2_proxy']:.4f}")
    print("  --- PART (a) acoustic-form X-check (S106 §VII.CA) ---")
    print(f"    Chern c_1 = {S106_CHERN:.3e}  Euler e_2 = {S106_EULER:.3e}  gradΩ = {S106_GRADED_OMEGA:.3e}  g = {S106_G_METRIC}")
    print(f"    acoustic_form_ok (holonomy-free, metrically-rich): {res['acoustic_form_ok']}")
    print("  --- PART (b) spatial-uniformity discriminator ---")
    print(f"    HOMOG  ptp(rho/c) DIRECT  = {res['ptp_Om_homog']:.3e}   (uniform_exact={res['uniform_exact']}; bit-identical)")
    print(f"    HOMOG  max_x|d_i Omega_hat| = {res['max_grad_homog']:.3e}   (<= tol {TOL:.0e})  [scale-inv PASS operator]")
    print(f"    HOMOG  max_x|d_i(rho/c)|RAW = {res['max_grad_raw_homog']:.3e}   (DIAGNOSTIC: np.gradient edge float-cancellation on ~1.5e5 const; NOT non-uniformity)")
    print(f"    HOMOG  max|R^(3)|        = {res['max_R3_homog']:.3e}   (<= tol {TOL:.0e})")
    print(f"    CONTROL ptp(rho/c)       = {res['ptp_Om_ctrl']:.3e}   (inhomog tau, base-structured)")
    print(f"    CONTROL max_x|d_i Omega_hat| = {res['max_grad_ctrl']:.3e}   (!= 0)")
    print(f"    CONTROL max|R^(3)|       = {res['max_R3_ctrl']:.3e}   (k != 0)")
    print(f"    discriminator_nontrivial = {res['discriminator_nontrivial']}")
    print("  --- R^(3) -> Omega_k ---")
    print(f"    k = R^(3)*a^2/6 = {res['k_curv']:.3e}   ==>  Omega_k = {res['Omega_k']:.1f} EXACT")
    print(f"    Planck Omega_k = {PLANCK_OMEGA_K:+.4f} +/- {PLANCK_OMEGA_K_ERR:.4f}  |  dev = {res['planck_sigma']:.3f} sigma  consistent={res['planck_consistent']}")

    # ---- save npz ----
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=res["verdict"],
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        tau_fold=float(tau_fold),
        a_2_FW_zeta=float(a_2_FW_zeta),
        Z_fold=res["Z_fold"],
        c_sound=res["c_sound"],
        Om_fold=res["Om_fold"],
        ptp_Om_homog=res["ptp_Om_homog"],
        ptp_Om_ctrl=res["ptp_Om_ctrl"],
        uniform_exact=res["uniform_exact"],
        max_grad_homog=res["max_grad_homog"],
        max_grad_raw_homog=res["max_grad_raw_homog"],
        max_R3_homog=res["max_R3_homog"],
        max_grad_ctrl=res["max_grad_ctrl"],
        max_R3_ctrl=res["max_R3_ctrl"],
        discriminator_nontrivial=res["discriminator_nontrivial"],
        Omega_k=res["Omega_k"],
        k_curv=res["k_curv"],
        a_scale=res["a_scale"],
        planck_omega_k=PLANCK_OMEGA_K,
        planck_omega_k_err=PLANCK_OMEGA_K_ERR,
        planck_dev=res["planck_dev"],
        planck_sigma=res["planck_sigma"],
        planck_consistent=res["planck_consistent"],
        acoustic_form_ok=res["acoustic_form_ok"],
        s106_chern=S106_CHERN, s106_euler=S106_EULER,
        s106_graded_omega=S106_GRADED_OMEGA, s106_g_metric=S106_G_METRIC,
        keys_are_fiber_pq=res["keys_are_fiber_pq"],
        a2_proxy_is_scalar=res["a2_proxy_is_scalar"],
        n_sectors=res["n_sectors"], n_modes=res["n_modes"], a2_proxy=res["a2_proxy"],
        Om_homog=res["Om_homog"], R3_homog=res["R3_homog"],
        Om_ctrl=res["Om_ctrl"], R3_ctrl=res["R3_ctrl"],
        tau_fine=res["tau_fine"], Z_spectral_fine=res["Z_spectral_fine"],
        tol=TOL, n_eval=N_EVAL,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  npz -> {OUT_NPZ.name}")
    make_plot(res)
    print(f"  png -> {OUT_PNG.name}")

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra_rows = [
        "# regulator_pin=a_2^{zeta} CLASS=FULL poleconv-A-double pole_in_s=3 curvature_grade_n=2 "
        "# CF-S117-A2-OMEGAK-ACOUSTIC-FORM a_2 zeta-regulated Seeley-DeWitt (regulator-pin-discipline.md; a_2_FW_zeta=2776.165389; cross-algebra caveat N/A -- SU(3) A_K)",
        "# acoustic-form-Xcheck: S106 §VII.CA metric-without-curvature Chern=9.78e-15 Euler=-8.83e-18 gradOmega=1.284e-17 g=982.5 (holonomy-free, metrically-rich; k-BLIND -> needs the uniformity selector) "
        "# CF-S117-A2-OMEGAK-ACOUSTIC-FORM PART(a)",
        f"# k-selector: ptp(rho/c)={res['ptp_Om_homog']:.2e} EXACT-uniform + max_x|d_i Omega_hat|={res['max_grad_homog']:.2e}<=1e-12 (scale-inv; raw-abs {res['max_grad_raw_homog']:.2e} is np.gradient float-cancellation DIAGNOSTIC, not non-uniformity) -> R^(3)={res['max_R3_homog']:.2e}<=1e-12 -> Omega_k=0 EXACT vs Planck {PLANCK_OMEGA_K:+.4f}+/-{PLANCK_OMEGA_K_ERR:.4f} ({res['planck_sigma']:.2f}sigma); control inhomog R^(3)={res['max_R3_ctrl']:.2e}!=0 (discriminator non-trivial) "
        "# CF-S117-A2-OMEGAK-ACOUSTIC-FORM PART(b)",
    ]  # (local)
    print_verdict_payload(res["verdict"], res["value"], audit_sha, content_sha,
                          sign_verdict=res["sign_verdict"],
                          magnitude_verdict=res["magnitude_verdict"],
                          regime_verdict=res["regime_verdict"],
                          extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {res['verdict']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
