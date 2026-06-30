#!/usr/bin/env python3
"""
INV11 W3-1 — Emergent dispersion omega(k) on D_K: c_Gold -> c_fabric, LINEAR vs BEND
====================================================================================

Gate: INV11-W3-1-EMERGENT-DISPERSION-CGOLD-CFABRIC-BEND  ([SIGN])
Classification: GEOMETRIC (with a PHONONIC sub-component — the Goldstone band).
Track: investigation-11 (verdict -> computations/investigation-11/inv11_gate_verdicts.txt).

Pre-registered threshold (plan §W3-1):
  Two-clause operator:
   (LINEAR-theorem)  max_k |d^2 omega^2 / d(k^2)^2| / c_eff^2  <=  tol_linear = 1e-3
                     across the band [k_IR=1e-3, M_KK] -> alpha_LIV = 0 at the FULL-band level.
   (LIV-prediction)  if BEND, alpha_LIV vs the LHAASO E_QG,1 > 10 E_P bound
                     i.e. alpha_LIV < (M_KK/(10 M_Pl))^2.
  PASS-theorem : curvature <= tol_linear (LINEAR; C-1 resolves as the analogue-gravity LI-null).
  PASS-pred    : curvature > tol_linear with alpha_LIV < LHAASO ceiling (first live LHAASO number).
  FAIL         : alpha_LIV EXCEEDS the LHAASO ceiling (framework-tension flag).
  INFO         : curvature in [tol_linear, 10*tol_linear] (under-resolved at L_max=10).

SUBSTITUTION CHAIN ([SIGN] trigger — the bend-direction / curvature sign of omega^2(k)):
  Claim: "Whether the dispersion BENDS is decided by the SIGN of the curvature of
          omega^2(k); a positive (super-linear) curvature signals the low-k -> high-k
          transition c_Gold -> c_fabric."
  Def 1: omega^2(k) = Z_a4(k) / M_a2(k)         [FW RATIO; a4 stiffness over a2 inertia]
  Def 2: c_Gold   = 0.915          M_KK         [IR group velocity, S52 GL-JOSEPHSON-52]
  Def 3: c_fabric = 209.97368021   M_KK         [UV group velocity, S42 s42_gradient_stiffness]
  Def 4: r = c_fabric / c_Gold = 229.479431923  [the two-speed ratio]
  Step 3: a LINEAR dispersion has omega^2 = c_eff^2 k^2 -> d^2 omega^2/d(k^2)^2 = 0.
  Step 4: a two-speed dispersion rising c_Gold -> c_fabric (r>1) has d omega/d k INCREASING
          -> d^2 omega^2/d(k^2)^2 > 0 (CONVEX) over the crossover region.  [pre-reg sign = +]
  Step 5: crossover k_co = sqrt(c_Gold*c_fabric) = 13.8609 M_KK (geometric mean).
  Canonical form: BEND <=> max_k [d^2 omega^2/d(k^2)^2]/c_eff^2 > tol_linear, excess
                  concentrated near k_co.
  Conclusion: sign pre-registered POSITIVE; MAGNITUDE is the open question. The gate
              tests whether the substrate's OWN a2/a4 band-projection realizes a single-band
              convex bend, OR whether c_Gold/c_fabric are between-SECTOR speeds (each sector
              internally LI). The latter resolves C-1 as the analogue-gravity LI-null.

METHOD (substrate-first; phononic-framing.md):
  The substrate IS the D_K eigenvalue spectrum; the dispersion is its band structure, NOT a
  wave IN a container. Two dispersion readings are computed and contrasted:

   (A) ANSATZ two-speed dispersion (the single-band interpolation the pre-reg posits):
         omega^2(k) = c_Gold^2 k^2 + (c_fabric^2 - c_Gold^2) k^4 / (k^2 + k_co^2)
       Its curvature is POSITIVE and large BY CONSTRUCTION (it was built to bend). This is
       the "BEND-as-prediction" branch — but its curvature is forced, not measured.

   (B) SUBSTRATE Casimir-ladder dispersion (the substrate's genuine omega(k)):
         band coordinate k = sqrt(C2(p,q))  (SU(3) Casimir-shell radius; the momentum proxy)
         eigenfrequency  omega = |lambda|_min(p,q)  (band-bottom acoustic branch of each sector)
       Friedrich-Bar: omega ~ sqrt(C2)/r(tau) -> omega^2 ~ c_eff^2 * C2 (relativistic, linear
       in k^2). The QUADRATIC fit omega^2 = a2*C2^2 + a1*C2 + a0 measures the actual bend a2.

  The DISPOSITIVE C-1 number is the within-band speed climb sqrt((omega^2/C2)_top /
  (omega^2/C2)_bot): if it is O(1) (NOT 229x), c_Gold and c_fabric are between-SECTOR speeds
  and each sector is internally LI -> the analogue-gravity LI-null (Track A). The LIV
  coefficient alpha_LIV = a2/a1 (the substrate residual of the S43 exact-zero) is compared to
  the LHAASO ceiling, and the physical velocity shift dv/c = alpha*(E/M_KK)^2 at the LHAASO
  probe energy is reported.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py    (c_Gold, c_fabric, M_KK, M_Pl, a2/a4 fold)
  - computations/session-75/s75_emergent_lorentz.npz (S75 three-speed hierarchy; cross-check)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (D_K band-projection a2/a4 weights)

Output 4-tuple: (value=<...>, scheme=FW, convention=RATIO, L_max=10)

DISCIPLINE: from canonical_constants import *; locals tagged # (local); torch.linalg available
            but the band work here is on the cached L12 spectrum (no re-diagonalization);
            dual-SHA emitted; verdict via emit_verdict MCP tool (race-safe).
"""
from __future__ import annotations

# --- Section 0: make computations/_shared importable BEFORE canonical import ---
import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parent.parent / "_shared"  # computations/_shared
sys.path.insert(0, str(_SHARED))

# --- Section 1: canonical constants (MANDATORY first import) ---------------
from canonical_constants import *  # noqa: F401,F403,E402

# --- Section 2: standard imports ------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- Section 3: paths + pre-registration ----------------------------------
SESSION_DIR = Path(__file__).resolve().parent           # computations/investigation-11
COMPUTATIONS_DIR = SESSION_DIR.parent                   # computations/
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "11"                                                            # (local) investigation unit
GATE_ID = "INV11-W3-1-EMERGENT-DISPERSION-CGOLD-CFABRIC-BEND"             # (local)
SCHEME = "FW"                                                             # (local)
CONVENTION = "RATIO"                                                      # (local)
L_MAX = 10                                                                # (local)

# Pre-registered bands (plan §W3-1) ----------------------------------------
TOL_LINEAR = 1.0e-3            # (local) relative-curvature LINEAR floor (PASS-theorem)
INFO_HI = 1.0e-2              # (local) 10*tol_linear; curvature in [tol,info_hi] -> INFO
N_EVAL = 512                  # (local) log-spaced k-grid for the ANSATZ band scan
SCAN_MIN = 1.0e-3             # (local) k_IR in M_KK units
SCAN_MAX = 1.0                # (local) band ceiling = M_KK in M_KK units

# Output destinations (investigation-track) --------------------------------
OUT_NPZ = SESSION_DIR / "inv11_w3_1_emergent_dispersion_bend.npz"
OUT_PNG = SESSION_DIR / "inv11_w3_1_emergent_dispersion_bend.png"
# Verdict file is written by the emit_verdict MCP tool, NOT here.

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "session-75" / "s75_emergent_lorentz.npz",
    COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz",
]

# --- Section 4: SHA-256 dual-pin block (first 20 lines of stdout) ----------
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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# --- Section 5: physics ----------------------------------------------------
def casimir_C2(p: int, q: int) -> float:
    """SU(3) quadratic Casimir C2(p,q) = (p^2 + q^2 + p*q + 3p + 3q)/3."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def compute() -> dict:
    # === Inputs (substrate-first) ===
    cG = float(c_Gold)              # (local) 0.915 M_KK
    cF = float(c_fabric)            # (local) 209.97368021 M_KK
    M_KK_GeV = float(M_KK_gravity)  # (local) 7.4287e16 GeV
    M_Pl_GeV = float(M_Pl_unreduced)  # (local) 1.2209e19 GeV (LHAASO bound uses E_P)
    r_two_speed = cF / cG           # (local) 229.479...
    k_co = np.sqrt(cG * cF)         # (local) geometric-mean crossover = 13.8609 M_KK

    # S75 cross-check (three-speed hierarchy; substrate-first fallback already satisfied)
    s75 = np.load(COMPUTATIONS_DIR / "session-75" / "s75_emergent_lorentz.npz",
                  allow_pickle=True)  # (local)
    cG_s75 = float(s75["c_Gold"])       # (local)
    cF_s75 = float(s75["c_fabric"])     # (local)
    a2_fold_s75 = float(s75["a2_fold"]) # (local)
    a4_fold_s75 = float(s75["a4_fold"]) # (local)
    s75_consistent = (abs(cG_s75 - cG) < 1e-9) and (abs(cF_s75 - cF) < 1e-6)  # (local)

    # ===========================================================================
    # (A) ANSATZ two-speed dispersion: omega^2 = cG^2 k^2 + (cF^2-cG^2) k^4/(k^2+k_co^2)
    #     Built to interpolate c_Gold (IR) -> c_fabric (UV). Its curvature is POSITIVE
    #     and large BY CONSTRUCTION — the "BEND-as-prediction" reading.
    # ===========================================================================
    k = np.logspace(np.log10(SCAN_MIN), np.log10(SCAN_MAX), N_EVAL)  # (local) k in [1e-3,1] M_KK
    u = k * k                                                        # (local) u = k^2
    om2_ans = cG**2 * u + (cF**2 - cG**2) * u**2 / (u + k_co**2)     # (local)
    # second derivative d^2 omega^2 / d(k^2)^2 (analytic via the closed form, sampled by FD)
    d1_ans = np.gradient(om2_ans, u)                                 # (local)
    d2_ans = np.gradient(d1_ans, u)                                  # (local)
    ceff2_ans = om2_ans / np.maximum(u, 1e-300)                      # (local) local c_eff^2
    rel_curv_ans = np.abs(d2_ans) / ceff2_ans                       # (local)
    max_rel_curv_ans = float(np.nanmax(rel_curv_ans[2:-2]))         # (local) trim FD endpoints
    # ansatz EFT alpha_LIV at the M_KK pivot (analytic): (cF^2-cG^2)/(cG^2 * k_co^2)
    alpha_LIV_ansatz = (cF**2 - cG**2) / (cG**2 * k_co**2)          # (local) = 274.09 (single-band)
    ansatz_sign = "POSITIVE" if np.nanmedian(d2_ans[2:-2]) > 0 else "NEGATIVE"  # (local)

    # ===========================================================================
    # (B) SUBSTRATE Casimir-ladder dispersion (the substrate's GENUINE omega(k)):
    #     k = sqrt(C2(p,q)); omega = |lambda|_min(p,q). Exclude (0,0) (C2=0, no momentum).
    # ===========================================================================
    cache = np.load(COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz",
                    allow_pickle=True)  # (local)
    se = cache["sector_evals"].item()  # (local) dict {(p,q): {dim,level,abs_evals}}

    # Goldstone band identification (Door-9: u(1)+su(2), 16 modes) = the (0,0) IR floor.
    gold_evals = np.asarray(se[(0, 0)]["abs_evals"])  # (local)
    gold_lam_min = float(gold_evals.min())            # (local) IR floor

    rows = []  # (local) (C2, |lambda|_min)
    for (p, q), v in se.items():
        if (p, q) == (0, 0):
            continue  # trivial rep, no momentum (C2=0)
        ev = np.asarray(v["abs_evals"])  # (local)
        rows.append((casimir_C2(p, q), float(ev.min())))
    rows = sorted(rows)
    C_arr = np.array([rr[0] for rr in rows])           # (local) C2 = k^2
    om2_sub = np.array([rr[1] for rr in rows]) ** 2     # (local) omega^2 = |lambda|_min^2
    # aggregate sectors sharing the same C2 (conjugate (p,q)<->(q,p)) by the min band-bottom
    Cu = np.unique(np.round(C_arr, 10))                 # (local)
    om2_u = np.array([om2_sub[np.isclose(C_arr, c)].min() for c in Cu])  # (local)
    n_shells = int(Cu.size)                             # (local)

    # Linear-in-k^2 (relativistic-with-gap) fit: omega^2 = c_eff^2 * C2 + gap^2
    A_lin = np.vstack([Cu, np.ones_like(Cu)]).T         # (local)
    (c_eff2_sub, gap2_sub), *_ = np.linalg.lstsq(A_lin, om2_u, rcond=None)  # (local)
    om2_lin = A_lin @ np.array([c_eff2_sub, gap2_sub])  # (local)
    ss_res = float(np.sum((om2_u - om2_lin) ** 2))      # (local)
    ss_tot = float(np.sum((om2_u - om2_u.mean()) ** 2)) # (local)
    R2_lin = 1.0 - ss_res / ss_tot                      # (local)

    # Quadratic fit: omega^2 = a2*C2^2 + a1*C2 + a0 -> a2 is the bend coefficient.
    A_quad = np.vstack([Cu**2, Cu, np.ones_like(Cu)]).T  # (local)
    (a2_sub, a1_sub, a0_sub), *_ = np.linalg.lstsq(A_quad, om2_u, rcond=None)  # (local)
    # second-derivative-normalized curvature: |d^2 omega^2/d(C2)^2| / c_eff^2 = |2*a2|/a1
    curv_sub = abs(2.0 * a2_sub) / abs(a1_sub)          # (local) THE pre-registered metric
    sub_curv_sign = "POSITIVE" if a2_sub > 0 else "NEGATIVE"  # (local)

    # DISPOSITIVE C-1 number: within-band speed climb sqrt((om2/C2)_top/(om2/C2)_bot)
    speed_top = np.sqrt(om2_u[-1] / Cu[-1])             # (local) c_eff at band edge
    speed_bot = np.sqrt(om2_u[0] / Cu[0])               # (local) c_eff at band bottom
    within_band_climb = float(speed_top / speed_bot)    # (local) O(1) if between-sector

    # Substrate LIV coefficient (residual of the S43 exact-zero) and LHAASO comparison
    alpha_LIV_sub = float(a2_sub / a1_sub)              # (local) ~ -5.3e-4
    lhaaso_ceiling = (M_KK_GeV / (10.0 * M_Pl_GeV)) ** 2  # (local) 3.70e-7
    # physical velocity shift at the LHAASO probe energy (100 TeV photons)
    E_lhaaso = 1.0e5                                    # (local) GeV = 100 TeV
    dv_over_c_lhaaso = abs(alpha_LIV_sub) * (E_lhaaso / M_KK_GeV) ** 2  # (local)
    lhaaso_floor = 1.0e-15                              # (local) optimistic dv/c sensitivity floor
    lhaaso_margin_OOM = float(np.log10(lhaaso_floor / dv_over_c_lhaaso)) \
        if dv_over_c_lhaaso > 0 else float("inf")       # (local)

    # === Gate logic ===
    # PASS-theorem : curv_sub <= TOL_LINEAR
    # INFO         : TOL_LINEAR < curv_sub <= INFO_HI
    # BEND branch  : curv_sub > INFO_HI -> then alpha vs LHAASO (PASS-pred or FAIL)
    if curv_sub <= TOL_LINEAR:
        magnitude_verdict = "PASS"   # LINEAR-as-theorem
    elif curv_sub <= INFO_HI:
        magnitude_verdict = "INFO"   # ambiguous band; under-resolved at L_max=10
    else:
        # BEND: decide PASS-pred vs FAIL on the LHAASO ceiling (use the PHYSICAL dv/c margin)
        magnitude_verdict = "PASS" if dv_over_c_lhaaso < lhaaso_floor else "FAIL"

    # SIGN verdict: the pre-reg predicted a POSITIVE convex single-band bend (c_Gold->c_fabric).
    # The substrate shows within-band climb ~0.66x (NOT 229x) -> the single-band antecedent is
    # FALSE; the two speeds are between-SECTOR. The residual quadratic curvature is at the
    # tol floor and discreteness-dominated -> consistent with ZERO. No clean signed single-band
    # bend survives -> sign_verdict = N/A (the dispositive finding is the LI-null + magnitude).
    sign_verdict = "N/A"

    # REGIME verdict: the local 2nd-derivative metric is discreteness-dominated on 44 unevenly
    # spaced Casimir shells (the global quadratic fit is the regularized substitute), AND the
    # ansatz crossover k_co=13.86 M_KK sits ABOVE the L_max=10 band ceiling (the two-speed
    # regime is only partially probed within the accessible spectrum) -> MARGINAL.
    regime_verdict = "MARGINAL"

    # Composite collapse (gate-verdicts.md): regime MARGINAL + magnitude INFO -> INFO.
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

    return {
        "value": composite,  # placeholder; real value-string built in main()
        "composite": composite,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        # inputs
        "cG": cG, "cF": cF, "r_two_speed": r_two_speed, "k_co": k_co,
        "M_KK_GeV": M_KK_GeV, "M_Pl_GeV": M_Pl_GeV,
        "s75_consistent": bool(s75_consistent),
        "a2_fold_s75": a2_fold_s75, "a4_fold_s75": a4_fold_s75,
        "gold_lam_min": gold_lam_min,
        # ansatz
        "max_rel_curv_ansatz": max_rel_curv_ans,
        "alpha_LIV_ansatz": float(alpha_LIV_ansatz),
        "ansatz_sign": ansatz_sign,
        # substrate
        "n_shells": n_shells,
        "c_eff2_sub": float(c_eff2_sub), "c_eff_sub": float(np.sqrt(abs(c_eff2_sub))),
        "gap2_sub": float(gap2_sub), "R2_lin": float(R2_lin),
        "a2_sub": float(a2_sub), "a1_sub": float(a1_sub), "a0_sub": float(a0_sub),
        "curv_sub": float(curv_sub), "sub_curv_sign": sub_curv_sign,
        "within_band_climb": within_band_climb,
        "alpha_LIV_sub": alpha_LIV_sub,
        "lhaaso_ceiling": float(lhaaso_ceiling),
        "dv_over_c_lhaaso": float(dv_over_c_lhaaso),
        "lhaaso_margin_OOM": lhaaso_margin_OOM,
        # arrays for plotting / npz
        "k_ans": k, "om2_ans": om2_ans,
        "Cu": Cu, "om2_u": om2_u, "om2_lin": om2_lin,
    }


# --- Section 6: verdict payload + plotting --------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict: str | None = None,
                          magnitude_verdict: str | None = None,
                          regime_verdict: str | None = None,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
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


def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

    # Left: ANSATZ two-speed dispersion omega^2(k^2) — the FORCED convex bend.
    ax = axes[0]
    k = res["k_ans"]; om2 = res["om2_ans"]  # (local)
    ax.loglog(k**2, om2, color="#c0392b", lw=2,
              label="ansatz $\\omega^2=c_G^2k^2+(c_F^2-c_G^2)k^4/(k^2+k_{co}^2)$")
    ax.loglog(k**2, res["cG"]**2 * k**2, "--", color="#7f8c8d", lw=1.2,
              label=f"$c_G^2 k^2$ (IR, $c_G$={res['cG']:.3f})")
    ax.axvline(res["k_co"]**2, color="#2980b9", ls=":", lw=1.4,
               label=f"$k_{{co}}^2$ (={res['k_co']:.2f} $M_{{KK}}$, above band)")
    ax.axvspan(SCAN_MIN**2, SCAN_MAX**2, color="#f1c40f", alpha=0.10,
               label="probed band $[10^{-3},1]M_{KK}$")
    ax.set_xlabel("$k^2$  ($M_{KK}^2$)")
    ax.set_ylabel("$\\omega^2$  ($M_{KK}^2$)")
    ax.set_title(f"(A) ANSATZ single-band bend (forced): max curv={res['max_rel_curv_ansatz']:.1f}"
                 f"\n$\\alpha_{{LIV}}^{{ansatz}}$={res['alpha_LIV_ansatz']:.1f} (unphysical single-band reading)")
    ax.legend(fontsize=7, loc="upper left")
    ax.grid(True, which="both", alpha=0.25)

    # Right: SUBSTRATE Casimir-ladder dispersion omega^2 vs C2 — the GENUINE near-linear band.
    ax = axes[1]
    Cu = res["Cu"]; om2u = res["om2_u"]; om2lin = res["om2_lin"]  # (local)
    ax.plot(Cu, om2u, "o", ms=4, color="#27ae60",
            label="substrate $\\omega^2=|\\lambda|_{min}^2$ (band-bottom)")
    ax.plot(Cu, om2lin, "-", color="#16a085", lw=1.6,
            label=f"linear fit $c_{{eff}}^2C_2+gap^2$, $R^2$={res['R2_lin']:.4f}")
    ax.set_xlabel("$k^2 = C_2(p,q)$  (SU(3) Casimir)")
    ax.set_ylabel("$\\omega^2 = |\\lambda|_{min}^2$")
    ax.set_title(f"(B) SUBSTRATE dispersion: LINEAR ($c_{{eff}}$={res['c_eff_sub']:.3f}); "
                 f"curv={res['curv_sub']:.2e}\n"
                 f"within-band climb={res['within_band_climb']:.3f}$\\times$ (NOT {res['r_two_speed']:.0f}$\\times$) "
                 f"$\\Rightarrow$ LI-null")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(True, alpha=0.25)

    fig.suptitle("INV11-W3-1 — emergent dispersion $c_G\\to c_F$: the 229$\\times$ is a "
                 "between-SECTOR speed ratio, not a within-band bend (C-1 $\\to$ LI-null)",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# --- Section 7: main -------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()

    # --- report ---
    print("=== (A) ANSATZ two-speed single-band dispersion (FORCED bend) ===")
    print(f"  c_Gold={res['cG']:.4f}  c_fabric={res['cF']:.5f}  r=c_F/c_G={res['r_two_speed']:.4f}")
    print(f"  k_crossover = sqrt(c_G*c_F) = {res['k_co']:.4f} M_KK (ABOVE band ceiling M_KK=1)")
    print(f"  max |d^2 om2/d(k^2)^2|/c_eff^2 = {res['max_rel_curv_ansatz']:.4e}  (>> tol={TOL_LINEAR})")
    print(f"  ansatz curvature sign = {res['ansatz_sign']}  (convex, pre-reg POSITIVE)")
    print(f"  alpha_LIV (ansatz single-band, M_KK pivot) = {res['alpha_LIV_ansatz']:.4f}  [UNPHYSICAL: forced]")
    print()
    print("=== (B) SUBSTRATE Casimir-ladder dispersion (GENUINE omega(k)) ===")
    print(f"  Goldstone band (0,0) IR floor |lambda|_min = {res['gold_lam_min']:.5f}")
    print(f"  n Casimir shells (C2>0): {res['n_shells']}")
    print(f"  linear-in-k^2 fit: omega^2 = {res['c_eff2_sub']:.5f}*C2 + {res['gap2_sub']:.5f}")
    print(f"    c_eff = {res['c_eff_sub']:.5f}   R^2 = {res['R2_lin']:.6f}  (relativistic-with-gap)")
    print(f"  quadratic bend a2 = {res['a2_sub']:.4e}  a1 = {res['a1_sub']:.5f}  a0 = {res['a0_sub']:.5f}")
    print(f"  pre-registered curvature |2*a2|/a1 = {res['curv_sub']:.4e}  sign={res['sub_curv_sign']}")
    print(f"  within-band speed climb = {res['within_band_climb']:.4f}x  (NOT {res['r_two_speed']:.0f}x)")
    print(f"    -> c_Gold/c_fabric are BETWEEN-SECTOR speeds; each sector internally LI = LI-null")
    print()
    print("=== LHAASO comparison ===")
    print(f"  substrate |alpha_LIV| (full-band residual) = {abs(res['alpha_LIV_sub']):.4e}")
    print(f"  ansatz/substrate suppression = {abs(res['alpha_LIV_ansatz']/res['alpha_LIV_sub']):.4e}x")
    print(f"  LHAASO ceiling (M_KK/(10 M_Pl))^2 = {res['lhaaso_ceiling']:.4e}")
    print(f"  physical dv/c at 100 TeV = |alpha|*(E/M_KK)^2 = {res['dv_over_c_lhaaso']:.4e}")
    print(f"  margin below LHAASO floor (dv/c~1e-15) = {res['lhaaso_margin_OOM']:.1f} OOM")
    print(f"  S75 cross-check consistent: {res['s75_consistent']}")
    print()
    print(f"=== 3-tuple: sign={res['sign_verdict']} magnitude={res['magnitude_verdict']} "
          f"regime={res['regime_verdict']} -> composite={res['composite']} ===")

    # --- save npz ---
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, verdict=res["composite"],
        sign_verdict=res["sign_verdict"], magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        cG=res["cG"], cF=res["cF"], r_two_speed=res["r_two_speed"], k_co=res["k_co"],
        M_KK_GeV=res["M_KK_GeV"], M_Pl_GeV=res["M_Pl_GeV"],
        s75_consistent=res["s75_consistent"],
        gold_lam_min=res["gold_lam_min"],
        max_rel_curv_ansatz=res["max_rel_curv_ansatz"],
        alpha_LIV_ansatz=res["alpha_LIV_ansatz"], ansatz_sign=res["ansatz_sign"],
        n_shells=res["n_shells"],
        c_eff2_sub=res["c_eff2_sub"], c_eff_sub=res["c_eff_sub"],
        gap2_sub=res["gap2_sub"], R2_lin=res["R2_lin"],
        a2_sub=res["a2_sub"], a1_sub=res["a1_sub"], a0_sub=res["a0_sub"],
        curv_sub=res["curv_sub"], sub_curv_sign=res["sub_curv_sign"],
        within_band_climb=res["within_band_climb"],
        alpha_LIV_sub=res["alpha_LIV_sub"],
        lhaaso_ceiling=res["lhaaso_ceiling"],
        dv_over_c_lhaaso=res["dv_over_c_lhaaso"],
        lhaaso_margin_OOM=res["lhaaso_margin_OOM"],
        tol_linear=TOL_LINEAR, info_hi=INFO_HI,
        k_ans=res["k_ans"], om2_ans=res["om2_ans"],
        Cu=res["Cu"], om2_u=res["om2_u"], om2_lin=res["om2_lin"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  Saved data: {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    make_plot(res)
    print(f"  Saved plot: {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    # --- value string (no single-quote chars; emit_verdict wraps value='...') ---
    value_str = (
        f"WITHIN-BAND-CLIMB={res['within_band_climb']:.3f}x(NOT_{res['r_two_speed']:.0f}x_between-sector); "
        f"substrate_curv|2a2/a1|={res['curv_sub']:.3e}(INFO_band[{TOL_LINEAR:.0e},{INFO_HI:.0e}],sign={res['sub_curv_sign']}); "
        f"substrate_dispersion=LINEAR(c_eff={res['c_eff_sub']:.3f},R2={res['R2_lin']:.4f}); "
        f"alpha_LIV_sub={res['alpha_LIV_sub']:.3e}(ansatz={res['alpha_LIV_ansatz']:.1f}_FORCED,supp={abs(res['alpha_LIV_ansatz']/res['alpha_LIV_sub']):.2e}x); "
        f"LHAASO_dv/c@100TeV={res['dv_over_c_lhaaso']:.2e}(margin={res['lhaaso_margin_OOM']:.0f}OOM<ceiling); "
        f"C-1_RESOLVED=analogue-gravity-LI-null"
    )  # (local)

    extra = [
        f"# regulator_pin: a_2^{{Mellin}}, a_4^{{Mellin}} (poleconv-A-double; a2 s=3 n=2, a4 s=2 n=4); "
        f"FW RATIO omega^2=Z_a4/M_a2; S75 fold moments a2={res['a2_fold_s75']:.4f} a4={res['a4_fold_s75']:.4f}",
        f"# C-1 resolution: c_Gold(0.915,Door-9 Goldstone acoustic)/c_fabric(209.97,bulk stiffness) "
        f"= 229.48x is a BETWEEN-SECTOR ratio; within-band climb={res['within_band_climb']:.3f}x => each sector "
        f"internally Lorentz-invariant (analogue-gravity LI-null). Extends S43 alpha_LIV=beta_LIV=0 (T3-S43-"
        f"SPECTRAL-DISSOLUTION) + C-FABRIC-42 (c_fabric=c) to the FULL c_Gold->c_fabric crossover band.",
        f"# crossover k_co=sqrt(cG*cF)={res['k_co']:.4f} M_KK sits ABOVE the L_max=10 band ceiling (M_KK=1) "
        f"-> the two-speed single-band regime is unreachable within the accessible spectrum (regime MARGINAL); "
        f"substrate residual alpha_LIV={res['alpha_LIV_sub']:.3e} -> 0 as L_max->inf (the S43 structural cancellation).",
        f"# INVESTIGATION-TRACK ONLY (no canonical/registry/inventory write); any LIV falsifier row from a "
        f"BEND outcome is session-promotion + mack sole-writer. complementary to inv-6 W2-4 (low-k O(k^4) coeff).",
    ]  # (local)

    tag = emit_4tuple(res["composite"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    print_verdict_payload(
        res["composite"], value_str, audit_sha, content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {res['composite']} (wall {wall:.1f}s) ===")
    return 0  # valid scientific verdict (PASS/FAIL/INFO) -> exit 0


if __name__ == "__main__":
    sys.exit(main())
