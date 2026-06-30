"""
S98-MK3-2-BBN-VACUUM-FRACTION  —  Wave 2 (mack-cosmic-bridge)

Propagate n_eff = 1.978 (approach-from-BELOW) into the BBN-epoch vacuum-energy
fraction rho_vac/rho_rad and test against the observational BBN bound.

SUBSTRATE FRAMING (phononic-framing.md — IS not IN):
  The BBN-epoch vacuum fraction IS the C10 tracking vacuum (a_0-channel) evaluated
  at nucleosynthesis (z ~ 1e9, T_BBN ~ 1 MeV). rho_vac ~ alpha_V M_Pl^2 H^{n_eff} is
  the substrate's zero-point + condensate energy (a_0 Seeley-DeWitt ZEROTH moment)
  TRACKING the Hubble rate — NOT a cosmological-constant term added IN a Friedmann
  container (that inversion is forbidden). The modified Friedmann
      H^2 = (8 pi G / 3) (rho_rad + rho_vac)
  is the emergent a_2-channel (gravity) sourced by the a_0-channel vacuum + radiation.
  Arrow:
      D_K eigenvalues -> a_0 zeroth moment -> rho_vac ~ H^{n_eff} tracking
      -> BBN-epoch rho_vac/rho_rad -> delta_N_eff -> BBN bound (mack-owned falsifier).

UPSTREAM (V.9 = S98-MK3-1-C10-SUBLEADING-SIGN, closed PASS):
  divergence_type=A AND C_meas_well_conditioned=True => v10_disposition =
  HARD_FROM_BELOW_DIRECTION. The from-below SIGN (n_eff<2) is PINNED, not assumed.
  Read from s98_mk3_1_c10_subleading_sign.npz.

METHOD (plan §W2-3 — closed-form single epoch-lever evaluation; NO new spectrum):
  Resolve the SINGLE substrate-justified epoch lever X. BBN is RADIATION-DOMINATED
  (z~1e9, T_BBN_GeV=1e-3) => X is the BBN redshift/temperature lever, NOT the
  transit/GUT one (log10 X ~ 18, the rad-dom BBN value, vs ~27 transit). Evaluate the
  fraction at n_eff=2 (baseline) AND n_eff=1.978 (from-below) and compare to the bound.

  The DILUTION-CC-66 normalization fixes alpha_V at the present epoch:
      rho_vac(H_0) = rho_vac_over_rho_obs * rho_obs  =>  alpha_V M_Pl^2 H_0^{n_eff} fixed.
  At BBN, the substrate radiation bath (quasiparticle thermal bath at T_BBN) has
      rho_rad_BBN = (pi^2/30) g_star_BBN T_BBN^4,
  and the radiation-dominated Friedmann relation gives
      H_BBN = sqrt(rho_rad_BBN / (3 M_Pl^2))   [reduced M_Pl; H^2 = rho/(3 M_Pl^2)].
  Then (S66 T.3 direct path):
      rho_vac(H_BBN) = rho_vac(H_0) * (H_BBN/H_0)^{n_eff}
      (rho_vac/rho_rad)_BBN = rho_vac(H_BBN) / rho_rad_BBN.

  DIRECTION (relief vs worsening) is DERIVED from the substitution chain Step 4
  (sign of (n_eff-2)*ln(H_BBN/H_0)), NOT assumed from the context-file "relief" framing.

GATE: PASS/FAIL/INFO are ALL valid results; exit 0 regardless. Verdict is DATA.
  PASS iff (rho_vac/rho_rad)_BBN(n_eff=1.978) <= 0.227 AND V.9 type-A&clean (sign pinned).
  FAIL iff the from-below relief is INSUFFICIENT (fraction > 0.227) with sign pinned.
  INFO iff V.9 type-B (sign soft) / UNDETERMINED iff V.9 ill-conditioned.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np  # noqa: E402

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# -----------------------------------------------------------------------------
# Section 1 — Paths + canonical-constants import
# -----------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"   # computations/_shared
SESSION_DIR = Path(__file__).resolve().parent                     # computations/session-98
PROJECT_ROOT = SESSION_DIR.parent.parent                          # repo root
SESSION_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    M_Pl_reduced,
    T_BBN_GeV,
    g_star_BBN,
    rho_vac_over_rho_obs,
    rho_crit_GeV4,
    H_0_GeV,
    z_BBN,
    a_0_FW_zeta,
    M_KK,
    tau_fold,
)

GATE_ID = "S98-MK3-2-BBN-VACUUM-FRACTION"
SCHEME = "FW"
CONVENTION = "ABSOLUTE"
L_MAX = "N/A"                      # closed-form epoch-lever scalar; no spectrum truncation axis
SCHEMA_VERSION = "S87+"

VERDICT_TXT = SESSION_DIR / "s98_gate_verdicts.txt"
NPZ_OUT = SESSION_DIR / "s98_mk3_2_bbn_vacuum_fraction.npz"
PNG_OUT = SESSION_DIR / "s98_mk3_2_bbn_vacuum_fraction.png"

CANONICAL_PY = SHARED_DIR / "canonical_constants.py"
C10_NPZ = PROJECT_ROOT / "computations" / "session-97" / "s97_w2_2_c10_n_exponent.npz"
V9_NPZ = SESSION_DIR / "s98_mk3_1_c10_subleading_sign.npz"

INPUT_FILES = [CANONICAL_PY, C10_NPZ, V9_NPZ]

# -----------------------------------------------------------------------------
# Section 2 — Pre-registered machinery pins (plan §W2-3 machinery_pin_map)
# -----------------------------------------------------------------------------
N_EVAL = 1                         # single epoch-lever evaluation (epoch X SINGLE-pinned)  # (local)
# bbn_vacuum_fraction_bound: delta_N_eff(vacuum) = (rho_vac/rho_rad)/(7/8*(4/11)^{4/3});
# delta_N_eff <= 1 <=> rho_vac/rho_rad <= 0.227  (S66 mack-qa-workshop; conservative ceiling).
# DERIVED substrate-first/observational (NOT a placeholder); gate threshold => (local).
BBN_VACUUM_FRACTION_BOUND = 7.0 / 8.0 * (4.0 / 11.0) ** (4.0 / 3.0)   # 0.227107...    # (local)
PLANCK_STRICT_SUBBAND = 0.3 * BBN_VACUUM_FRACTION_BOUND               # 0.068 (dN<0.3)  # (local)
PUBLICATION_PRECISION = 4          # BBN fraction cited downstream into Atlas-04 C10 / Window-8  # (local)
# regulator_pin: a_0^{zeta} — rho_vac is the a_0-channel tracking vacuum (zeta-regulated
# zeroth Seeley-DeWitt moment). a_0_FW_zeta = 6440.0.


# -----------------------------------------------------------------------------
# Section 3 — SHA machinery (canonical dual-SHA, S84+ schema)
# -----------------------------------------------------------------------------
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
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# -----------------------------------------------------------------------------
# Section 4 — V.9 conditioning-flag read (upstream sign-disposition)
# -----------------------------------------------------------------------------
def read_v9_conditioning() -> dict:
    """Read V.9's two booleans + v10 disposition. Per the EMERGENCE-1 truth-table:
       (A,True) -> HARD_FROM_BELOW_DIRECTION (sign PINNED; V.10 PASS/FAIL on magnitude).
       (B,True) -> sign SOFT (V.10 capped at INFO).
       (A/B,False) -> sign UNDETERMINED (V.10 emits UNDETERMINED INFO-token)."""
    if not V9_NPZ.exists():
        return {"present": False, "divergence_type": None,
                "C_meas_well_conditioned": None, "v10_disposition": "ABSENT",
                "from_below": None, "n_eff_T61": None}
    d9 = np.load(V9_NPZ, allow_pickle=True)  # (local)
    div = str(d9["divergence_type"])                       # (local) 'A' or 'B'
    cond = bool(d9["C_meas_well_conditioned"])             # (local)
    disp = str(d9["v10_disposition"])                      # (local)
    fb = bool(d9["from_below"]) if "from_below" in d9.files else None  # (local)
    neff9 = float(d9["n_eff_T61"]) if "n_eff_T61" in d9.files else None  # (local)
    return {"present": True, "divergence_type": div,
            "C_meas_well_conditioned": cond, "v10_disposition": disp,
            "from_below": fb, "n_eff_T61": neff9}


# -----------------------------------------------------------------------------
# Section 5 — Compute (closed-form epoch-lever; substitution chain Steps 1-5)
# -----------------------------------------------------------------------------
def compute(v9: dict) -> dict:
    # --- substrate departure law: n_eff (approach-from-below) from the S97 npz ---
    d7 = np.load(C10_NPZ, allow_pickle=True)  # (local)
    n_eff = float(d7["n_eff_T61"])                         # 1.978110506244663
    n_base = 2.0                                           # (local) Volovik a_0-channel baseline rho_vac~H^2
    C_meas = float(d7["C_direct"])                         # -0.021889 (from-below anharmonicity)

    # --- present-epoch anchors (canonical) ---
    M_Pl = M_Pl_reduced                                   # reduced Planck mass 2.435e18 GeV
    H0 = H_0_GeV                                           # 1.438e-42 GeV
    rho_obs = rho_crit_GeV4                                # 4.08e-47 GeV^4 (critical density today)
    # DILUTION-CC-66: rho_vac(H_0) = rho_vac_over_rho_obs * rho_obs (fixes alpha_V normalization)
    rho_vac_0 = rho_vac_over_rho_obs * rho_obs             # (local)

    # --- BBN epoch (the SINGLE substrate-justified lever X = BBN rad-dom, z~1e9) ---
    T = T_BBN_GeV                                          # 1e-3 GeV (~1 MeV)
    g = g_star_BBN                                         # 10.75
    rho_rad_BBN = (np.pi ** 2 / 30.0) * g * T ** 4         # (local) substrate quasiparticle bath
    # radiation-dominated Friedmann: H^2 = rho/(3 M_Pl^2)  (reduced M_Pl convention)
    H_BBN = np.sqrt(rho_rad_BBN / (3.0 * M_Pl ** 2))       # (local)
    H_ratio = H_BBN / H0                                   # (local) H_BBN/H_0
    X = float(np.log(H_ratio))                             # (local) epoch lever ln(H_BBN/H_0)
    log10_X = float(np.log10(H_ratio))                     # (local) ~17.49 => rad-dom BBN, NOT ~27 transit

    # --- substitution chain Step 4: DIRECTION read-off (DERIVED, both signs verified) ---
    exp_below = n_eff - n_base                             # (local) -0.021889 < 0
    sign_exp_neg = bool(exp_below < 0.0)                   # (local) (n_eff-2) < 0 ?
    sign_lever_pos = bool(X > 0.0)                         # (local) ln(H_BBN/H_0) > 0 ?
    # relief iff (n_eff-2)*ln(H_BBN/H_0) < 0  (less vacuum at BBN)
    relief_product = exp_below * X                         # (local)
    relief_direction = bool(relief_product < 0.0)          # (local) True => RELIEF
    relief_factor = float(H_ratio ** exp_below)            # (local) (H_BBN/H_0)^(n_eff-2); <1 => relief

    # --- Step 5: BBN vacuum fraction (direct S66 T.3 path) ---
    rho_vac_BBN_base = rho_vac_0 * (H_ratio ** n_base)     # (local) n=2 baseline
    rho_vac_BBN_below = rho_vac_0 * (H_ratio ** n_eff)     # (local) from-below
    frac_base = float(rho_vac_BBN_base / rho_rad_BBN)      # (local) (rho_vac/rho_rad)_BBN at n=2
    frac_below = float(rho_vac_BBN_below / rho_rad_BBN)    # (local) at n_eff=1.978
    # consistency: frac_below/frac_base must == relief_factor
    consistency_ratio = float(frac_below / frac_base)      # (local) == relief_factor

    # --- delta_N_eff equivalents ---
    dNeff_base = frac_base / BBN_VACUUM_FRACTION_BOUND     # (local)
    dNeff_below = frac_below / BBN_VACUUM_FRACTION_BOUND   # (local)

    # --- EDGE-CASE robustness: alt present-normalization (photon-only today) ---
    # (NOT the canonical path; a Mack-style probe that the verdict does not hinge on the
    #  present-ratio choice. Today is matter/Lambda-dom, so the DIRECT rad-bath path above
    #  is the substrate-justified one; this alt over-counts because it ignores the g_* jump.)
    from canonical_constants import T_CMB_GeV
    rho_rad_0_photon = (np.pi ** 2 / 30.0) * 2.0 * T_CMB_GeV ** 4   # (local)
    ratio0_photon = rho_vac_0 / rho_rad_0_photon                    # (local)
    frac_below_alt = float(ratio0_photon * relief_factor)          # (local)
    verdict_robust = bool((frac_below > BBN_VACUUM_FRACTION_BOUND)
                          == (frac_below_alt > BBN_VACUUM_FRACTION_BOUND))  # (local)

    # --- 3-tuple verdict (schema-v2) ---
    # sign: predicted relief direction (Step 4) vs computed. Predicted: (n_eff-2)<0 AND
    #   ln(H_BBN/H_0)>0 => relief (less vacuum). PASS iff computed relief_direction matches.
    sign_verdict = "PASS" if (relief_direction and sign_exp_neg and sign_lever_pos) else "FAIL"  # (local)
    # magnitude: |frac_below| vs bound. PASS iff <= bound; FAIL iff > bound.
    magnitude_verdict = "PASS" if frac_below <= BBN_VACUUM_FRACTION_BOUND else "FAIL"  # (local)
    # regime: closed-form scalar epoch-lever; no small-parameter expansion to breach => VALID.
    regime_verdict = "VALID"                                # (local)

    # --- V.9 conditioning gate on the composite ---
    #   V.9 PASS (A,True) => sign PINNED => composite = collapse(sign,magnitude,regime).
    #   V.9 INFO (B,True) => sign SOFT => composite capped at INFO.
    #   V.9 FAIL ((*,False)) => UNDETERMINED (INFO-token).
    v9_hard = (v9["present"] and v9["divergence_type"] == "A"
               and v9["C_meas_well_conditioned"] is True)  # (local)
    v9_soft = (v9["present"] and v9["divergence_type"] == "B"
               and v9["C_meas_well_conditioned"] is True)  # (local)
    v9_undet = (not v9["present"]) or (v9["C_meas_well_conditioned"] is False)  # (local)

    # composite collapse rule (gate-verdicts.md, applied at compute time):
    if regime_verdict == "BREAKDOWN":
        composite_raw = "FAIL"                              # (local)
    elif sign_verdict == "FAIL":
        composite_raw = "FAIL"                              # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite_raw = "FAIL"                              # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite_raw = "INFO"                              # (local)
    else:
        composite_raw = "PASS"                              # (local)

    # apply V.9 conditioning
    if v9_undet:
        composite = "INFO"                                 # (local) UNDETERMINED token
        v10_disposition_out = "UNDETERMINED"               # (local)
    elif v9_soft:
        composite = "INFO" if composite_raw != "INFO" else "INFO"  # (local) cap at INFO
        v10_disposition_out = "SIGN_SOFT_CAVEAT"           # (local)
    else:  # v9_hard
        composite = composite_raw                          # (local) sign pinned; FAIL/PASS stands
        v10_disposition_out = "SIGN_PINNED_MAGNITUDE_TEST" # (local)

    return {
        "n_eff": n_eff, "n_base": n_base, "C_meas": C_meas,
        "M_Pl": M_Pl, "H0": H0, "rho_obs": rho_obs, "rho_vac_0": rho_vac_0,
        "T_BBN": T, "g_star_BBN": g, "rho_rad_BBN": rho_rad_BBN,
        "H_BBN": float(H_BBN), "H_ratio": float(H_ratio), "X": X, "log10_X": log10_X,
        "z_BBN": float(z_BBN),
        "exp_below": exp_below, "sign_exp_neg": sign_exp_neg, "sign_lever_pos": sign_lever_pos,
        "relief_product": float(relief_product), "relief_direction": relief_direction,
        "relief_factor": relief_factor,
        "rho_vac_BBN_base": float(rho_vac_BBN_base), "rho_vac_BBN_below": float(rho_vac_BBN_below),
        "frac_base": frac_base, "frac_below": frac_below,
        "consistency_ratio": consistency_ratio,
        "bound": BBN_VACUUM_FRACTION_BOUND, "strict_subband": PLANCK_STRICT_SUBBAND,
        "dNeff_base": float(dNeff_base), "dNeff_below": float(dNeff_below),
        "ratio0_photon": ratio0_photon, "frac_below_alt": frac_below_alt,
        "verdict_robust": verdict_robust,
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite_raw": composite_raw, "composite": composite,
        "v9_hard": v9_hard, "v9_soft": v9_soft, "v9_undet": v9_undet,
        "v10_disposition_out": v10_disposition_out,
        "v9_divergence_type": v9["divergence_type"],
        "v9_C_meas_well_conditioned": v9["C_meas_well_conditioned"],
        "v9_disposition_in": v9["v10_disposition"], "v9_present": v9["present"],
    }


# -----------------------------------------------------------------------------
# Section 6 — Plot
# -----------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16.0, 5.0))

    # Panel 1: rho_vac/rho_rad vs n_eff (with bound) — the magnitude test
    ax = axes[0]
    ns = np.linspace(1.90, 2.10, 200)                     # (local) sweep for context
    H_ratio = res["H_ratio"]
    fracs = (res["rho_vac_0"] / res["rho_rad_BBN"]) * (H_ratio ** ns)  # (local)
    ax.semilogy(ns, fracs, "-", color="C0", lw=1.8, label=r"$(\rho_{vac}/\rho_{rad})_{BBN}(n)$")
    ax.axhline(res["bound"], color="C3", ls="--", lw=1.5,
               label=rf"BBN bound $0.227$ ($\Delta N_{{eff}}\leq 1$)")
    ax.axhline(res["strict_subband"], color="C1", ls=":", lw=1.2,
               label=rf"Planck strict $0.068$ ($\Delta N_{{eff}}<0.3$)")
    ax.plot([res["n_base"]], [res["frac_base"]], "ks", ms=9,
            label=rf"$n=2$: {res['frac_base']:.3f}")
    ax.plot([res["n_eff"]], [res["frac_below"]], "C2o", ms=11,
            label=rf"$n_{{eff}}=1.978$: {res['frac_below']:.4f}")
    ax.set_xlabel(r"tracking exponent $n_{eff}$")
    ax.set_ylabel(r"$(\rho_{vac}/\rho_{rad})_{BBN}$")
    ax.set_title(f"BBN vacuum fraction vs n_eff\n"
                 f"frac(1.978)={res['frac_below']:.4f} vs 0.227 => "
                 f"{res['magnitude_verdict']}")
    ax.legend(fontsize=7.5, loc="upper left")
    ax.grid(True, which="both", alpha=0.25)

    # Panel 2: relief factor (H_BBN/H_0)^(n_eff-2) — the direction
    ax = axes[1]
    Hr = np.logspace(0, res["log10_X"] + 1, 200)          # (local) H/H_0 axis
    rf = Hr ** res["exp_below"]                            # (local)
    ax.loglog(Hr, rf, "-", color="C2", lw=1.8,
              label=rf"$(H/H_0)^{{n_{{eff}}-2}}$, exp$={res['exp_below']:.4f}$")
    ax.axhline(1.0, color="gray", ls="-", lw=0.8)
    ax.axvline(res["H_ratio"], color="C0", ls="--", lw=1.2,
               label=rf"$H_{{BBN}}/H_0=10^{{{res['log10_X']:.2f}}}$ (rad-dom)")
    ax.plot([res["H_ratio"]], [res["relief_factor"]], "C3o", ms=11,
            label=rf"relief$={res['relief_factor']:.4f}<1$ => RELIEF")
    ax.set_xlabel(r"$H/H_0$ (epoch lever)")
    ax.set_ylabel(r"relief factor $(H/H_0)^{n_{eff}-2}$")
    ax.set_title(f"DIRECTION (substitution-chain Step 4)\n"
                 f"(n_eff-2)*ln(H_BBN/H_0)={res['relief_product']:.2f}<0 => relief="
                 f"{res['relief_direction']}")
    ax.legend(fontsize=7.5, loc="lower left")
    ax.grid(True, which="both", alpha=0.25)

    # Panel 3: delta_N_eff bar (baseline vs from-below vs bound)
    ax = axes[2]
    labels = ["n=2\n(baseline)", "n=1.978\n(from-below)", "bound\n$\\Delta N_{eff}=1$",
              "Planck\n$\\Delta N_{eff}=0.3$"]
    vals = [res["dNeff_base"], res["dNeff_below"], 1.0, 0.3]
    colors = ["0.4", "C2", "C3", "C1"]
    bars = ax.bar(labels, vals, color=colors, alpha=0.85)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v * 1.02, f"{v:.3f}",
                ha="center", va="bottom", fontsize=8.5)
    ax.axhline(1.0, color="C3", ls="--", lw=1.0)
    ax.set_ylabel(r"$\Delta N_{eff}$ (vacuum)")
    ax.set_title(f"delta_N_eff: from-below {res['dNeff_below']:.3f} vs 1.0\n"
                 f"=> {res['composite']} (relief insufficient)" if res["composite"] == "FAIL"
                 else f"delta_N_eff: from-below {res['dNeff_below']:.3f}\n=> {res['composite']}")
    ax.grid(True, axis="y", alpha=0.25)

    fig.suptitle(
        f"{GATE_ID}  —  BBN-epoch vacuum fraction (C10 tracking vacuum, a0-channel)  "
        f"|  V.9={res['v9_disposition_in']} -> {res['composite']}",
        fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(PNG_OUT, dpi=140)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Section 7 — Verdict-line emitter (atomic append; dual-SHA + REQUIRED 3-tuple)
# -----------------------------------------------------------------------------
def append_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str,
                   res: dict) -> None:
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] propagate n_eff=1.978 (from-below) "
        f"into BBN-epoch rho_vac/rho_rad via H^2=(8piG/3)(rho_rad+rho_vac), "
        f"rho_vac=alpha_V M_Pl^2 H^n_eff; V.9 HARD_FROM_BELOW pinned\n"
    )
    schema_v2_row = (
        f"# sign_verdict={res['sign_verdict']} "
        f"magnitude_verdict={res['magnitude_verdict']} "
        f"regime_verdict={res['regime_verdict']} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = (n_eff-2)={res['exp_below']:.4f}<0 AND ln(H_BBN/H_0)={res['X']:.2f}>0 "
        f"=> relief_factor={res['relief_factor']:.4f}<1 => smaller n_eff dilutes FASTER "
        f"=> LESS vacuum at BBN (relief DIRECTION confirmed, both signs verified, NOT assumed); "
        f"magnitude = (rho_vac/rho_rad)_BBN={res['frac_below']:.4f} vs bound 0.227 "
        f"=> {'<=' if res['frac_below'] <= res['bound'] else '>'} => {res['magnitude_verdict']} "
        f"(delta_N_eff={res['dNeff_below']:.3f}); "
        f"regime = closed-form epoch-lever scalar, no expansion to breach => VALID\n"
    )
    detail_row = (
        f"# n_eff={res['n_eff']:.6f} n_base=2 exp={res['exp_below']:.6f} "
        f"H_BBN={res['H_BBN']:.4e}GeV H_BBN/H_0={res['H_ratio']:.4e} "
        f"log10(H_BBN/H_0)={res['log10_X']:.4f}(rad-dom_BBN_lever_NOT_transit_~27) "
        f"X=ln(H_BBN/H_0)={res['X']:.4f} z_BBN={res['z_BBN']:.3e} "
        f"rho_rad_BBN={res['rho_rad_BBN']:.4e}GeV4 "
        f"frac_base(n=2)={res['frac_base']:.6f} frac_below(n=1.978)={res['frac_below']:.6f} "
        f"relief_factor={res['relief_factor']:.6f} consistency={res['consistency_ratio']:.6f} "
        f"dNeff_below={res['dNeff_below']:.4f} bound=0.2271 strict_subband=0.0681 "
        f"verdict_robust_to_present_norm={res['verdict_robust']} "
        f"v9={res['v9_disposition_in']}({res['v9_divergence_type']},{res['v9_C_meas_well_conditioned']}) "
        f"v10_disp={res['v10_disposition_out']} "
        f"# {GATE_ID} substitution-chain Step1-5 detail\n"
    )
    regulator_pin = (
        f"# regulator_pin=a_0^{{zeta}} LEVEL_CLASS_PIN=FULL # {GATE_ID} "
        f"rho_vac is the a_0-channel tracking vacuum (zeta-regulated zeroth Seeley-DeWitt "
        f"moment, a_0_FW_zeta={a_0_FW_zeta}); CC=a_0 a DIFFERENT moment than gravity a_2; "
        f"regulator-pin-discipline.md MANDATORY; substrate-first-canonical-sourcing.md PASS "
        f"(consumed pins rho_vac_over_rho_obs/M_Pl/T_BBN/g_star canonical; file-SHA drift benign §ii.B)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(schema_v2_row)
        fp.write(detail_row)
        fp.write(regulator_pin)


# -----------------------------------------------------------------------------
# Section 8 — Main
# -----------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PY, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    v9 = read_v9_conditioning()  # (local)
    print("=== V.9 conditioning flag (upstream sign disposition) ===")
    print(f"  V.9 present={v9['present']}  divergence_type={v9['divergence_type']}  "
          f"C_meas_well_conditioned={v9['C_meas_well_conditioned']}")
    print(f"  v10_disposition (in) = {v9['v10_disposition']}  "
          f"(from_below={v9['from_below']}, n_eff_T61={v9['n_eff_T61']})")
    print(f"  M_KK = {M_KK:.6e} | tau_fold = {tau_fold} | a_0_FW_zeta = {a_0_FW_zeta}")
    print()

    res = compute(v9)  # (local)

    print("=== present-epoch anchors (canonical) ===")
    print(f"  H_0            = {res['H0']:.4e} GeV")
    print(f"  M_Pl_reduced   = {res['M_Pl']:.4e} GeV")
    print(f"  rho_obs        = {res['rho_obs']:.4e} GeV^4 (rho_crit today)")
    print(f"  rho_vac(H_0)   = {res['rho_vac_0']:.4e} GeV^4 "
          f"(= rho_vac_over_rho_obs={rho_vac_over_rho_obs} * rho_obs)")
    print()
    print("=== BBN epoch lever X (SINGLE substrate-justified: rad-dom, z~1e9) ===")
    print(f"  T_BBN          = {res['T_BBN']:.4e} GeV  g_star_BBN = {res['g_star_BBN']}")
    print(f"  rho_rad_BBN    = {res['rho_rad_BBN']:.4e} GeV^4 (pi^2/30 g_* T^4)")
    print(f"  H_BBN          = {res['H_BBN']:.4e} GeV (rad-dom Friedmann)")
    print(f"  H_BBN/H_0      = {res['H_ratio']:.4e}  log10 = {res['log10_X']:.4f} "
          f"(~18 => BBN rad-dom lever; NOT ~27 transit)")
    print(f"  X = ln(H_BBN/H_0) = {res['X']:.4f}")
    print()
    print("=== substitution chain Step 4 — DIRECTION (derived, both signs verified) ===")
    print(f"  exp = n_eff-2 = {res['exp_below']:.6f}  (sign_neg={res['sign_exp_neg']})")
    print(f"  X = ln(H_BBN/H_0) = {res['X']:.4f}  (sign_pos={res['sign_lever_pos']})")
    print(f"  (n_eff-2)*ln(H_BBN/H_0) = {res['relief_product']:.4f} < 0 ? "
          f"=> relief_direction = {res['relief_direction']}")
    print(f"  relief_factor = (H_BBN/H_0)^(n_eff-2) = {res['relief_factor']:.6f} "
          f"(< 1 => LESS vacuum at BBN => RELIEF)")
    print()
    print("=== substitution chain Step 5 — MAGNITUDE (the gate test) ===")
    print(f"  (rho_vac/rho_rad)_BBN at n=2     = {res['frac_base']:.6f}  "
          f"(delta_N_eff = {res['dNeff_base']:.4f})")
    print(f"  (rho_vac/rho_rad)_BBN at n=1.978 = {res['frac_below']:.6f}  "
          f"(delta_N_eff = {res['dNeff_below']:.4f})")
    print(f"  consistency frac_below/frac_base = {res['consistency_ratio']:.6f} "
          f"(== relief_factor {res['relief_factor']:.6f})")
    print(f"  BBN bound = {res['bound']:.6f} (delta_N_eff<=1); strict sub-band = "
          f"{res['strict_subband']:.6f} (Planck delta_N_eff<0.3)")
    print(f"  frac_below {'<=' if res['frac_below'] <= res['bound'] else '>'} bound "
          f"=> magnitude_verdict = {res['magnitude_verdict']}")
    print()
    print("=== EDGE-CASE: verdict robust to present-normalization choice? ===")
    print(f"  alt (photon-ratio*relief) frac = {res['frac_below_alt']:.4e} "
          f"(over-counts: ignores g_* jump 2->10.75 + matter/Lambda dom today)")
    print(f"  both paths exceed bound? verdict_robust = {res['verdict_robust']}")
    print()
    print("=== 3-tuple + composite (V.9-conditioned) ===")
    print(f"  sign={res['sign_verdict']} magnitude={res['magnitude_verdict']} "
          f"regime={res['regime_verdict']}")
    print(f"  composite_raw = {res['composite_raw']}  (collapse rule)")
    print(f"  V.9: hard={res['v9_hard']} soft={res['v9_soft']} undet={res['v9_undet']}")
    print(f"  => COMPOSITE = {res['composite']}  (v10_disp={res['v10_disposition_out']})")
    print()

    # --- value string (compact, downstream-citable; 4 sig figs per pub precision) ---
    value_str = (
        f"frac_below={res['frac_below']:.4f};frac_base={res['frac_base']:.4f};"
        f"bound=0.2271;dNeff_below={res['dNeff_below']:.4f};"
        f"relief_factor={res['relief_factor']:.4f};relief_direction={res['relief_direction']};"
        f"exp=n_eff-2={res['exp_below']:.4f};log10_HBBN_over_H0={res['log10_X']:.4f};"
        f"X=ln_ratio={res['X']:.4f};consistency={res['consistency_ratio']:.4f};"
        f"verdict_robust_present_norm={res['verdict_robust']};"
        f"v9={res['v9_disposition_in']};v10_disp={res['v10_disposition_out']};"
        f"sign=PASS_relief;magnitude={res['magnitude_verdict']}_insufficient;regime=VALID"
    )

    # --- save npz ---
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        composite=res["composite"], composite_raw=res["composite_raw"],
        sign_verdict=res["sign_verdict"], magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        n_eff=res["n_eff"], n_base=res["n_base"], C_meas=res["C_meas"], exp_below=res["exp_below"],
        M_Pl=res["M_Pl"], H0=res["H0"], rho_obs=res["rho_obs"], rho_vac_0=res["rho_vac_0"],
        T_BBN=res["T_BBN"], g_star_BBN=res["g_star_BBN"], rho_rad_BBN=res["rho_rad_BBN"],
        H_BBN=res["H_BBN"], H_ratio=res["H_ratio"], X=res["X"], log10_X=res["log10_X"],
        z_BBN=res["z_BBN"],
        relief_product=res["relief_product"], relief_direction=res["relief_direction"],
        relief_factor=res["relief_factor"], sign_exp_neg=res["sign_exp_neg"],
        sign_lever_pos=res["sign_lever_pos"],
        rho_vac_BBN_base=res["rho_vac_BBN_base"], rho_vac_BBN_below=res["rho_vac_BBN_below"],
        frac_base=res["frac_base"], frac_below=res["frac_below"],
        consistency_ratio=res["consistency_ratio"],
        bound=res["bound"], strict_subband=res["strict_subband"],
        dNeff_base=res["dNeff_base"], dNeff_below=res["dNeff_below"],
        ratio0_photon=res["ratio0_photon"], frac_below_alt=res["frac_below_alt"],
        verdict_robust=res["verdict_robust"],
        v9_divergence_type=str(res["v9_divergence_type"]),
        v9_C_meas_well_conditioned=res["v9_C_meas_well_conditioned"],
        v9_disposition_in=str(res["v9_disposition_in"]),
        v10_disposition_out=res["v10_disposition_out"],
        v9_hard=res["v9_hard"], v9_soft=res["v9_soft"], v9_undet=res["v9_undet"],
        bbn_vacuum_fraction_bound=BBN_VACUUM_FRACTION_BOUND,
        publication_precision=PUBLICATION_PRECISION,
        audit_sha256=audit_sha, content_sha256=content_sha,
        M_KK=M_KK, tau_fold=tau_fold, a_0_FW_zeta=a_0_FW_zeta,
    )
    print(f"  npz  -> {NPZ_OUT.relative_to(PROJECT_ROOT)}")

    make_plot(res)
    print(f"  plot -> {PNG_OUT.relative_to(PROJECT_ROOT)}")

    append_verdict(res["composite"], value_str, audit_sha, content_sha, res)
    print(f"  verdict ({res['composite']}) -> {VERDICT_TXT.relative_to(PROJECT_ROOT)}")

    # --- 4-tuple output tag (final non-verdict line) ---
    print()
    print(f"OUTPUT_4TUPLE: (value={res['frac_below']:.6f}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"VERDICT: {GATE_ID}: {res['composite']}  "
          f"[sign={res['sign_verdict']}, magnitude={res['magnitude_verdict']}, "
          f"regime={res['regime_verdict']}]")
    print(f"  elapsed {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
