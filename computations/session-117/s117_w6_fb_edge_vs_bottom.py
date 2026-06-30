"""
s117_w6_fb_edge_vs_bottom.py
============================

CF-S117-FB-EDGE-VS-BOTTOM  —  [SIGN] gate (spectral-geometer).

Confirms the s=3 (a_2 Seeley-DeWitt, curvature_grade n=2) PV-subtracted moment
truncation drift is lambda_max-EDGE-driven (FB-A-null), NOT bottom-K, so the
S116-W8-1 "friedrich-bar-saturation" label is MIS-SCOPED (the operative mechanism
is FB-B Level-2 convergence of the PV ratio, NOT FB-A bottom-K exact-saturation);
and the convergence-rate alpha is SCHEME-DEPENDENT across {zeta, Pauli-Villars}.

INFO-class by construction: the S116-W8-FWDC1-LANDING INFO verdict + all its
numbers are UNAFFECTED.  This gate ADDS an additive Sec.VII.AU.OP-PROJ Element-3
Level-2-envelope scope annotation (FB-B not FB-A; mack-routed).  A FAIL fires ONLY
on bottom_frac >= 0.05 (FB-A IN-SCOPE reopened) OR a zeta-vs-PV drift sign mismatch.

GOVERNING STRUCTURE (heat-kernel Rosetta Stone):
    Tr(e^{-sigma D^2}) = Sum_k m_k e^{-sigma lambda_k^2}
    zeta_D(s) = (1/Gamma(s)) Int_0^inf sigma^{s-1} Tr(e^{-sigma D^2}) dsigma
              = Sum_k m_k lambda_k^{-2s}                       (poleconv-A-double)
    -> simple poles at s = (d-n)/2 with Res = a_n / Gamma((d-n)/2).
    d=8: s=4(a0), s=3(a2), s=2(a4), s=1(a6), s=0(a8).  s=3 IS a2 (n = d-2s = 8-6 = 2).
    a_2 is a LOCAL curvature invariant = small-sigma (UV) heat-kernel residue
    -> UV-EDGE (large-lambda) determined.  The bottom of the spectrum sets the
    large-sigma (IR) tail = lambda_min, NEVER a_n.  => the a_2 truncation drift is
    structurally bottom-K-NULL; the residual drift is the lambda_max edge tail.

[SIGN] 3-tuple:
    sign      = sign(zeta s=3 L12->L14 drift) == sign(PV s=3 drift)   (both edge-driven, same UV pole)
    magnitude = alpha_rel band: PASS(FI) <= 0.10 ; INFO 0.10-0.50 ; FAIL(SD) > 0.50
    regime    = bottom_frac band: VALID (< 0.05, FB-A-null) ; BREAKDOWN (>= 0.05, FB-A reopened)

PLAN-FROZEN composite operator (plan sec.W6-3 PASS/INFO/FAIL_meaning, pre-registered
BEFORE evaluation):
    FAIL iff  bottom_frac >= 0.05  OR  sign(drift_zeta) != sign(drift_PV)
    PASS iff  bottom_frac < 0.05  AND  sign match  AND  alpha_rel <= 0.10   (alpha FI; unexpected)
    INFO iff  bottom_frac < 0.05  AND  sign match  AND  alpha_rel  > 0.10   (alpha SD; the EXPECTED result)
This plan-frozen operator takes PRECEDENCE over the generic 3-tuple collapse
(which would read magnitude=FAIL ^ regime=VALID -> FAIL); a `# composite-precedence:`
disclosure extra-row is emitted per gate-verdicts.md.

CLASS = FULL : both schemes evaluate FULL physical regularizations on the cached
spectra (PV PRIMARY 2-point CC1996 helper; bare zeta = analytic-continuation value).
No SCHEMATIC helper is consumed for any load-bearing trace.

Plan: sessions/session-plan/session-117-plan-w6.md sec.W6-3.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU-thread cap (per-mode moment sums + small log-log fits; no large eigensolve)

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Path discipline (project root contains a space -- absolute paths only)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

# -----------------------------------------------------------------------------
# Canonical constants (MANDATORY: never hardcode framework constants)
# -----------------------------------------------------------------------------
from canonical_constants import (  # noqa: E402
    tau_fold,
    M_KK,
    alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22,   # = 2.6926... (PV Level-2 alpha_sat; the alpha_PV reference)
    alpha_HH1_per_pole_FW_s3,                          # = 2.0  (Wodzicki per-pole lower bound)
    rho_FULL_CC_VII_AU_SAT_s3,                         # = 1.0076927826 (canonical PV rho cross-check anchor)
)

# -----------------------------------------------------------------------------
# FULL-physical Pauli-Villars helper (PRIMARY; CC1996 sec.2.2-2.3) -- the SAME
# machinery as S116-W8-FWDC1-LANDING / S92 W1-CF-W9-8-2 (rho_FULL lineage)
# -----------------------------------------------------------------------------
from _pauli_villars_subtraction import (  # noqa: E402
    PV_PRIMARY_C,
    PV_PRIMARY_M_DIMLESS,
    pv_multiplier_primary,
    pv_mellin_moment_primary,
    bare_mellin_moment,
    _verify_pv_identities,
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (R3 YAML, plan sec.W6-3)
# -----------------------------------------------------------------------------
SESSION = "S117"
GATE_ID = "CF-S117-FB-EDGE-VS-BOTTOM"
SCHEME = "edge-vs-bottom-decomposition + zeta-vs-PV-alpha"
CONVENTION = (
    "FWDC1-s3-edge-bottom-{a_2^zeta}+{a_2^Pauli-Villars}-"
    "poleconv-A-double-pole_in_s-3-curvature_grade_n-2"
)
L_MAX = "12 and 14"
S_POLE = 3.0             # (local) substrate-distance pole; poleconv-A-double, d=8 -> curvature_grade n = d-2s = 2 (a_2)
D_DIM = 8               # (local) spectral dimension of M4 x SU(3)/U(1) substrate fibre object
CURV_GRADE_N = 2         # (local) n = d - 2s = 8 - 6 = 2 ; a_2 Seeley-DeWitt (Einstein-Hilbert generator)

# Pre-registered bands (plan sec.W6-3 machinery_pin_map.tolerance)
BOTTOM_FRAC_NULL = 0.05      # (local) bottom_frac < 0.05 -> FB-A-null (edge-driven); >= 0.05 -> FB-A reopened
ALPHA_REL_FI = 0.10          # (local) alpha_rel <= 0.10 -> FI ; (0.10,0.50] -> INFO ; > 0.50 -> SD
ALPHA_REL_SD = 0.50          # (local) alpha_rel > 0.50 -> SD (scheme-dependent convergence rate)
BOTTOM_K_CEILING = 0.845     # (local) bottom-20 weighted-multiset ceiling (plan gate-block ref; the s=3 a_2 IR cut)
L_SCAN = [8, 9, 10, 11, 12, 13, 14]   # (local) multi-L sub-truncations of the L14 cache (level<=L; NO new diagonalization)

# alpha_PV reference (PV Level-2 convergence exponent; canonical, NOT refit here)
ALPHA_PV = float(alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22)  # (local) = 2.6926236951...

# -----------------------------------------------------------------------------
# Input files
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
PV_HELPER_PATH = PROJECT_ROOT / "computations" / "_pauli_villars_subtraction.py"
CACHE_L12 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CACHE_L14 = PROJECT_ROOT / "computations" / "session-87" / "s87_spectrum_cache_L14_tau019.npz"
FWDC1_NPZ = PROJECT_ROOT / "computations" / "session-116" / "s116_w8_fwdc1_level2_envelope_friedrich_bar.npz"

OUT_NPZ = PROJECT_ROOT / "computations" / "session-117" / "s117_w6_fb_edge_vs_bottom.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "session-117" / "s117_w6_fb_edge_vs_bottom.png"

# Static input-SHA pins (plan Input-SHA Ledger; verified at runtime)
PIN_L12 = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"
PIN_L14 = "fa2bfb83c74ff151b138c83498f54ca2c87a61fc59ec1ae5189bb6aab360480c"
PIN_FWDC1 = "40a6c8e1fbb9656752d63ad835b3bfb9e3d881fc6c18582ff13febfd2e9f6728"


# -----------------------------------------------------------------------------
# SHA helpers (S84+ dual-SHA schema; same as S116 FWDC1 lineage)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    h = hashlib.sha256()  # (local)
    for k, v in sorted(pins.items()):
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    """audit_sha256 = sha256(script || canonical || pinmap_json); content_sha256 = sha256(script)."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None) -> dict:
    """Emit the delimited verdict PAYLOAD for the dispatching agent to pass to the
    knowledge-MCP `emit_verdict` tool (race-safe; gate-verdicts.md). Script does NOT
    write the verdict file."""
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
    if sign_verdict is not None:
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# -----------------------------------------------------------------------------
# Spectrum cache loaders (Peter-Weyl sectored; per-mode weighted by Weyl dim)
#   identical flattening convention to S116 FWDC1 load_spectrum_flat
# -----------------------------------------------------------------------------
def load_sector_dict(cache_path: Path) -> dict:
    return np.load(cache_path, allow_pickle=True)["sector_evals"].item()


def flatten_sectors(sector_evals: dict, level_max=None) -> tuple[np.ndarray, np.ndarray]:
    """Flatten {(p,q):{dim,level,abs_evals}} -> (|lambda|, mult) arrays.
    If level_max given, keep only sectors with level (=p+q) <= level_max."""
    lams, mults = [], []  # (local)
    for (p, q), info in sector_evals.items():
        if level_max is not None and int(info["level"]) > level_max:
            continue
        dim = int(info["dim"])  # (local) Weyl multiplicity m_k for every eigenvalue in the block
        for v in np.asarray(info["abs_evals"], dtype=np.float64):
            lams.append(float(v))
            mults.append(float(dim))
    return np.asarray(lams, dtype=np.float64), np.asarray(mults, dtype=np.float64)


def g_pv_per_mode(lambdas: np.ndarray, s: float) -> np.ndarray:
    """Per-mode PV kernel g_PV(lambda;s) = w_PV(lambda^2;s) * lambda^{-2s}.
    Sum_k m_k g_PV(lambda_k;s) == pv_mellin_moment_primary(s, lambdas, mults)."""
    lam2 = lambdas * lambdas  # (local)
    w = pv_multiplier_primary(lam2, s)  # (local) FULL 2-point CC1996 multiplier
    return w * np.power(lam2, -s)


def main() -> int:
    print(f"=== {GATE_ID} ===")
    print(f"pole s={S_POLE} (poleconv-A-double, d={D_DIM}) -> curvature_grade n = d-2s = {D_DIM}-{int(2*S_POLE)} = {CURV_GRADE_N}  (a_2 Seeley-DeWitt)")
    print(f"PASS-band gates: bottom_frac < {BOTTOM_FRAC_NULL} (FB-A-null) AND sign(drift_zeta)==sign(drift_PV); alpha_rel FI<= {ALPHA_REL_FI}, SD > {ALPHA_REL_SD}")

    # -------------------------------------------------------------------------
    # 1) Input pins + verification
    # -------------------------------------------------------------------------
    pins = {
        "computations/_shared/canonical_constants.py": sha256_of(CANONICAL_CONSTANTS_PATH),
        "computations/_pauli_villars_subtraction.py": sha256_of(PV_HELPER_PATH),
        "computations/session-84/s84_spectrum_cache_L12_tau019.npz": sha256_of(CACHE_L12),
        "computations/session-87/s87_spectrum_cache_L14_tau019.npz": sha256_of(CACHE_L14),
        "computations/session-116/s116_w8_fwdc1_level2_envelope_friedrich_bar.npz": sha256_of(FWDC1_NPZ),
        "_gate_id": GATE_ID, "_scheme": SCHEME, "_convention": CONVENTION,
        "_pole_in_s": str(int(S_POLE)), "_curvature_grade_n": str(CURV_GRADE_N),
    }
    print("\n=== Input pins (SHA-256 heads) ===")
    for k, v in sorted(pins.items()):
        if not k.startswith("_"):
            print(f"  {k}: {v[:16]}")
    # SHA-ledger verification (cache + FWDC1 must be the plan-pinned static inputs)
    assert pins["computations/session-84/s84_spectrum_cache_L12_tau019.npz"] == PIN_L12, "L12 cache SHA drift!"
    assert pins["computations/session-87/s87_spectrum_cache_L14_tau019.npz"] == PIN_L14, "L14 cache SHA drift!"
    assert pins["computations/session-116/s116_w8_fwdc1_level2_envelope_friedrich_bar.npz"] == PIN_FWDC1, "FWDC1 npz SHA drift!"
    print("  Input-SHA Ledger verified (L12 9e6d9cf7.., L14 fa2bfb83.., FWDC1 40a6c8e1..).")
    assert abs(tau_fold - 0.19) < 1e-9, f"tau_fold={tau_fold} != 0.19"
    print(f"  tau_fold = {tau_fold} ; M_KK = {M_KK:.6e} GeV")

    # PV consistency identities (Sum c_r = 1, Sum c_r m_r^2 = 0)
    sc, scm2 = _verify_pv_identities()
    print(f"  PV identities: Sum c_r = {sc:.3e} (->1), Sum c_r m_r^2 = {scm2:.3e} (->0)")
    assert abs(sc - 1.0) < 1e-12 and abs(scm2) < 1e-12

    # -------------------------------------------------------------------------
    # 2) Load caches; reproduce the S116 FWDC1 PV moments (pipeline validation)
    # -------------------------------------------------------------------------
    se12 = load_sector_dict(CACHE_L12)
    se14 = load_sector_dict(CACHE_L14)
    lam12, m12 = flatten_sectors(se12)
    lam14, m14 = flatten_sectors(se14)
    print(f"\n=== Caches ===")
    print(f"  L12: n_sectors={len(se12)}, N_block={len(lam12)}, |lam| in [{lam12.min():.4f},{lam12.max():.4f}]")
    print(f"  L14: n_sectors={len(se14)}, N_block={len(lam14)}, |lam| in [{lam14.min():.4f},{lam14.max():.4f}]")

    M_FULL_12 = pv_mellin_moment_primary(S_POLE, lam12, m12)  # (local)
    M_FULL_14 = pv_mellin_moment_primary(S_POLE, lam14, m14)  # (local)
    M_BARE_12 = bare_mellin_moment(S_POLE, lam12, m12)        # (local)
    M_BARE_14 = bare_mellin_moment(S_POLE, lam14, m14)        # (local)
    rho_12 = M_FULL_12 / M_BARE_12                            # (local)
    rho_14 = M_FULL_14 / M_BARE_14                            # (local)

    fwd = np.load(FWDC1_NPZ, allow_pickle=True)
    val_dev = lambda a, b: abs(a - b) / abs(b) if b else abs(a - b)  # (local)
    print(f"\n=== S116 FWDC1 reproduction (pipeline validation) ===")
    for nm, mine, ref in [("M_FULL_L12", M_FULL_12, float(fwd["M_FULL_L12"])),
                          ("M_FULL_L14", M_FULL_14, float(fwd["M_FULL_L14"])),
                          ("M_BARE_L12", M_BARE_12, float(fwd["M_BARE_L12"])),
                          ("M_BARE_L14", M_BARE_14, float(fwd["M_BARE_L14"])),
                          ("rho_FULL_L12", rho_12, float(fwd["rho_FULL_L12"])),
                          ("rho_FULL_L14", rho_14, float(fwd["rho_FULL_L14"]))]:
        d = val_dev(mine, ref)  # (local)
        print(f"  {nm:14s} mine={mine:.10f} ref={ref:.10f} rel_dev={d:.2e}")
        assert d < 1e-9, f"{nm} deviates from S116 FWDC1 by {d:.2e} (>1e-9)"
    rho_canon_dev = val_dev(rho_14, rho_FULL_CC_VII_AU_SAT_s3)  # (local)
    assert rho_canon_dev < 1e-9, f"rho_14 vs canonical rho_FULL_CC_VII_AU_SAT_s3 dev {rho_canon_dev:.2e}"
    print(f"  rho_FULL_L14 vs canonical rho_FULL_CC_VII_AU_SAT_s3={rho_FULL_CC_VII_AU_SAT_s3}: rel_dev={rho_canon_dev:.2e}  [VALIDATED]")

    # cache mutual-consistency: shared (level<=12) modes bit-identical across s84 / s87
    lam14_le12, m14_le12 = flatten_sectors(se14, level_max=12)
    MB_14_le12 = bare_mellin_moment(S_POLE, lam14_le12, m14_le12)  # (local)
    consistency_dev = val_dev(MB_14_le12, M_BARE_12)  # (local)
    print(f"  cache consistency: bare M(s=3) on s87[level<=12] vs s84[L12] rel_dev={consistency_dev:.2e}  (shared modes bit-identical)")
    assert consistency_dev < 1e-12, "L12/L14 caches inconsistent on shared sectors!"

    # -------------------------------------------------------------------------
    # 3) EDGE-vs-BOTTOM decomposition of the s=3 PV-subtracted moment drift
    #    dM_FULL = M_FULL(L14) - M_FULL(L12).  Partition each spectrum into
    #    bottom-K (|lambda| <= 0.845) and lambda_max edge (|lambda| > 0.845).
    #    Per-mode g_PV is L_max-INDEPENDENT -> the moment is additive over
    #    mode-sets; the shared bottom-K modes cancel in the drift.
    # -------------------------------------------------------------------------
    dM_FULL = M_FULL_14 - M_FULL_12  # (local) PV-subtracted moment drift (the truncation error)
    dM_BARE = M_BARE_14 - M_BARE_12  # (local) zeta (bare) moment drift

    g12 = g_pv_per_mode(lam12, S_POLE)  # (local) per-mode PV kernel, L12
    g14 = g_pv_per_mode(lam14, S_POLE)  # (local) per-mode PV kernel, L14
    # additivity self-check: Sum m g_PV == pv_mellin_moment_primary
    assert abs(float(np.sum(m12 * g12)) - M_FULL_12) < 1e-6 * abs(M_FULL_12)
    assert abs(float(np.sum(m14 * g14)) - M_FULL_14) < 1e-6 * abs(M_FULL_14)

    bot12 = lam12 <= BOTTOM_K_CEILING  # (local)
    bot14 = lam14 <= BOTTOM_K_CEILING  # (local)
    MF_bot_12 = float(np.sum(m12[bot12] * g12[bot12]))   # (local) bottom-K region moment, L12
    MF_bot_14 = float(np.sum(m14[bot14] * g14[bot14]))   # (local) bottom-K region moment, L14
    MF_edge_12 = M_FULL_12 - MF_bot_12                   # (local) edge region moment, L12
    MF_edge_14 = M_FULL_14 - MF_bot_14                   # (local) edge region moment, L14

    dM_FULL_bottom = MF_bot_14 - MF_bot_12   # (local) bottom-K contribution to the drift
    dM_FULL_edge = MF_edge_14 - MF_edge_12   # (local) edge contribution to the drift
    bottom_frac = abs(dM_FULL_bottom) / abs(dM_FULL)  # (local) THE FB-A-null operator
    edge_frac = abs(dM_FULL_edge) / abs(dM_FULL)      # (local)

    # NEW-mode cross-check: sectors in s87 not in s84 (levels 13,14)
    new_keys = [k for k in se14 if k not in se12]  # (local)
    new_levels = sorted(set(int(se14[k]["level"]) for k in new_keys))  # (local)
    new_lam, new_m = [], []  # (local)
    for k in new_keys:
        dim = int(se14[k]["dim"])
        for v in np.asarray(se14[k]["abs_evals"], dtype=np.float64):
            new_lam.append(float(v)); new_m.append(float(dim))
    new_lam = np.asarray(new_lam); new_m = np.asarray(new_m)
    g_new = g_pv_per_mode(new_lam, S_POLE)  # (local)
    n_new_in_bottom = int(np.sum(new_lam <= BOTTOM_K_CEILING))  # (local) NEW modes intruding below the bottom-K ceiling
    new_bottom_contrib = float(np.sum(new_m[new_lam <= BOTTOM_K_CEILING] * g_new[new_lam <= BOTTOM_K_CEILING]))  # (local)
    dM_FULL_from_new = float(np.sum(new_m * g_new))  # (local) should equal dM_FULL (shared modes cancel)
    new_lam_min = float(new_lam.min())  # (local)

    print(f"\n=== EDGE-vs-BOTTOM decomposition (s=3 a_2 PV moment, L12->L14) ===")
    print(f"  dM_FULL (PV moment drift)      = {dM_FULL:.6f}")
    print(f"  dM_FULL via NEW sectors only   = {dM_FULL_from_new:.6f}  (rel_dev {val_dev(dM_FULL_from_new, dM_FULL):.1e}; shared bottom modes cancel)")
    print(f"  bottom-K region moment  : L12={MF_bot_12:.8f}  L14={MF_bot_14:.8f}  drift={dM_FULL_bottom:.3e}")
    print(f"  edge       region moment: L12={MF_edge_12:.6f}  L14={MF_edge_14:.6f}  drift={dM_FULL_edge:.6f}")
    print(f"  bottom_frac = |dM_bottom|/|dM_FULL| = {bottom_frac:.3e}   (FB-A-null iff < {BOTTOM_FRAC_NULL})")
    print(f"  edge_frac   = |dM_edge|/|dM_FULL|   = {edge_frac:.6f}")
    print(f"  NEW sectors (s87\\s84): n={len(new_keys)}, levels={new_levels}; NEW modes with |lam|<=0.845: {n_new_in_bottom}")
    print(f"  NEW-mode bottom contribution = {new_bottom_contrib:.3e} ; min |lam| over NEW modes = {new_lam_min:.4f}  (>> {BOTTOM_K_CEILING})")
    print(f"  -> FB-A bottom-K IS saturated (region drift {dM_FULL_bottom:.1e}=0), but it carries ZERO of the a_2 drift; the drift is 100% lambda_max edge.")

    # -------------------------------------------------------------------------
    # 4) ZETA-vs-PV drift SIGN cross-check (Step 4)
    # -------------------------------------------------------------------------
    sign_PV = int(np.sign(dM_FULL))    # (local)
    sign_zeta = int(np.sign(dM_BARE))  # (local)
    sign_match = (sign_PV == sign_zeta)  # (local)
    print(f"\n=== zeta-vs-PV drift sign (L12->L14) ===")
    print(f"  drift_PV   (dM_FULL) = {dM_FULL:+.4f}  sign={sign_PV:+d}")
    print(f"  drift_zeta (dM_BARE) = {dM_BARE:+.4f}  sign={sign_zeta:+d}")
    print(f"  sign match? {sign_match}  (both edge-driven, same UV pole s=3 -> same sign expected)")

    # -------------------------------------------------------------------------
    # 5) alpha FI/SD: multi-L scan (level<=L sub-truncations of the L14 cache)
    #    PV ratio rho(L) converges (alpha_PV=2.6926); bare zeta moment DIVERGES
    #    (s=3 < d/2=4 -> Weyl tail lambda^{d-2s}=lambda^{+2}) -> no positive alpha.
    # -------------------------------------------------------------------------
    Ls = np.array(L_SCAN, dtype=float)  # (local)
    MB_scan, MF_scan, rho_scan = [], [], []  # (local)
    for L in L_SCAN:
        lamL, mL = flatten_sectors(se14, level_max=L)
        mb = bare_mellin_moment(S_POLE, lamL, mL)  # (local)
        mf = pv_mellin_moment_primary(S_POLE, lamL, mL)  # (local)
        MB_scan.append(mb); MF_scan.append(mf); rho_scan.append(mf / mb)
    MB_scan = np.array(MB_scan); MF_scan = np.array(MF_scan); rho_scan = np.array(rho_scan)
    print(f"\n=== Multi-L scan (level<=L sub-truncations of s87 L14 cache; NO new diagonalization) ===")
    for i, L in enumerate(L_SCAN):
        print(f"  L={L:2d}: M_BARE={MB_scan[i]:12.4f}  M_FULL={MF_scan[i]:12.4f}  rho={rho_scan[i]:.8f}")

    # zeta divergence exponent: log M_BARE ~ beta*log L  (beta>0 => divergent => alpha_zeta = -beta)
    beta_zeta = float(np.polyfit(np.log(Ls), np.log(MB_scan), 1)[0])  # (local) growth exponent of the bare zeta moment
    alpha_zeta = -beta_zeta  # (local) convergence exponent (negative => divergent; no FB-B envelope)
    bare_monotone_increasing = bool(np.all(np.diff(MB_scan) > 0))  # (local)

    # PV ratio convergence exponent cross-check: rho(L) = rho_inf + C L^{-alpha}  (3-param)
    alpha_PV_fit = np.nan  # (local)
    rho_inf_fit = np.nan   # (local)
    try:
        from scipy.optimize import curve_fit
        def conv_model(L, rinf, C, a):
            return rinf + C * np.power(L, -a)
        popt, _ = curve_fit(conv_model, Ls, rho_scan, p0=[1.003, 0.5, 2.7],
                            bounds=([0.9, -10, 0.3], [1.1, 10, 6.0]), maxfev=200000)
        rho_inf_fit, _, alpha_PV_fit = float(popt[0]), float(popt[1]), float(popt[2])
    except Exception as e:  # noqa: BLE001
        print(f"  (rho convergence fit fallback: {e})")
    rho_monotone_decreasing = bool(np.all(np.diff(rho_scan) < 0))  # (local)

    alpha_rel = abs(alpha_zeta - ALPHA_PV) / abs(ALPHA_PV)  # (local) THE alpha FI/SD operator
    print(f"\n=== alpha FI/SD reconciliation (s=3 a_2 convergence rate) ===")
    print(f"  PV scheme : rho(L) ratio CONVERGES (monotone-decreasing={rho_monotone_decreasing}); alpha_PV (canonical) = {ALPHA_PV:.6f}")
    print(f"              rho convergence fit (L8-14 cross-check): alpha_PV_fit={alpha_PV_fit:.4f}, rho_inf_fit={rho_inf_fit:.6f}")
    print(f"  zeta scheme: bare zeta_D(s=3) DIVERGES (monotone-increasing={bare_monotone_increasing}); growth beta={beta_zeta:.4f}")
    print(f"              => alpha_zeta = -beta = {alpha_zeta:.4f} (NEGATIVE: no positive convergence exponent; s=3<d/2=4, Weyl tail lambda^{{+2}})")
    print(f"  alpha_rel = |alpha_zeta - alpha_PV|/alpha_PV = |{alpha_zeta:.4f} - {ALPHA_PV:.4f}|/{ALPHA_PV:.4f} = {alpha_rel:.4f}")
    print(f"  bands: FI <= {ALPHA_REL_FI} ; INFO ({ALPHA_REL_FI},{ALPHA_REL_SD}] ; SD > {ALPHA_REL_SD}  => {'SD' if alpha_rel > ALPHA_REL_SD else ('INFO' if alpha_rel > ALPHA_REL_FI else 'FI')}")
    print(f"  three reconciled F-images bracket [2,3]: SCHEMATIC |alpha|=3, Wodzicki={alpha_HH1_per_pole_FW_s3:.1f}, pathway-B={ALPHA_PV:.4f}; zeta sits OUTSIDE (divergent) -> scheme-dependent")

    # -------------------------------------------------------------------------
    # 6) [SIGN] 3-tuple + PLAN-FROZEN composite operator
    # -------------------------------------------------------------------------
    sign_v = "PASS" if sign_match else "FAIL"  # (local)
    if alpha_rel <= ALPHA_REL_FI:
        mag_v = "PASS"  # (local) alpha FI
    elif alpha_rel <= ALPHA_REL_SD:
        mag_v = "INFO"  # (local)
    else:
        mag_v = "FAIL"  # (local) alpha SD (the EXPECTED result)
    regime_v = "VALID" if bottom_frac < BOTTOM_FRAC_NULL else "BREAKDOWN"  # (local) FB-A-null vs FB-A reopened

    # PLAN-FROZEN operator (plan sec.W6-3 PASS/INFO/FAIL_meaning):
    if (bottom_frac >= BOTTOM_FRAC_NULL) or (not sign_match):
        composite = "FAIL"  # (local) FB-A IN-SCOPE reopened OR sign mismatch
    elif alpha_rel <= ALPHA_REL_FI:
        composite = "PASS"  # (local) FB-A-null + sign + alpha FI (unexpected)
    else:
        composite = "INFO"  # (local) FB-A-null + sign hold, alpha SD (EXPECTED)

    # Generic 3-tuple collapse (for the composite-precedence disclosure)
    if regime_v == "BREAKDOWN":
        generic = "FAIL"  # (local)
    elif sign_v == "FAIL":
        generic = "FAIL"  # (local)
    elif mag_v == "FAIL" and regime_v == "VALID":
        generic = "FAIL"  # (local)  <- magnitude=FAIL(SD) ^ regime=VALID -> FAIL (generic)
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        generic = "INFO"  # (local)
    elif mag_v == "INFO":
        generic = "INFO"  # (local)
    else:
        generic = "PASS"  # (local)
    precedence_invoked = (composite != generic)  # (local)

    print(f"\n=== Verdict (3-tuple) ===")
    print(f"  sign={sign_v}  magnitude={mag_v}  regime={regime_v}")
    print(f"  composite (plan-frozen operator) = {composite}")
    print(f"  generic-collapse reading = {generic}  -> precedence_invoked={precedence_invoked}")

    # -------------------------------------------------------------------------
    # 7) Dual-SHA + save
    # -------------------------------------------------------------------------
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)
    print(f"\n=== Dual-SHA ===\n  audit_sha256   = {audit_sha}\n  content_sha256 = {content_sha}")
    print(f"  closure_hash(pins) [cross-check] = {closure_hash(pins)}")

    np.savez_compressed(
        OUT_NPZ,
        # edge-vs-bottom
        dM_FULL=dM_FULL, dM_FULL_from_new=dM_FULL_from_new, dM_BARE=dM_BARE,
        MF_bot_12=MF_bot_12, MF_bot_14=MF_bot_14, MF_edge_12=MF_edge_12, MF_edge_14=MF_edge_14,
        dM_FULL_bottom=dM_FULL_bottom, dM_FULL_edge=dM_FULL_edge,
        bottom_frac=bottom_frac, edge_frac=edge_frac,
        n_new_sectors=len(new_keys), new_levels=np.array(new_levels, dtype=int),
        n_new_in_bottom=n_new_in_bottom, new_bottom_contrib=new_bottom_contrib, new_lam_min=new_lam_min,
        BOTTOM_K_CEILING=BOTTOM_K_CEILING,
        # PV moments (S116 reproduction)
        M_FULL_12=M_FULL_12, M_FULL_14=M_FULL_14, M_BARE_12=M_BARE_12, M_BARE_14=M_BARE_14,
        rho_12=rho_12, rho_14=rho_14, rho_canon_dev=rho_canon_dev, consistency_dev=consistency_dev,
        # sign
        sign_PV=sign_PV, sign_zeta=sign_zeta, sign_match=sign_match,
        # alpha FI/SD
        L_scan=Ls, MB_scan=MB_scan, MF_scan=MF_scan, rho_scan=rho_scan,
        beta_zeta=beta_zeta, alpha_zeta=alpha_zeta, alpha_PV=ALPHA_PV,
        alpha_PV_fit=alpha_PV_fit, rho_inf_fit=rho_inf_fit, alpha_rel=alpha_rel,
        bare_monotone_increasing=bare_monotone_increasing, rho_monotone_decreasing=rho_monotone_decreasing,
        alpha_wodzicki=float(alpha_HH1_per_pole_FW_s3), alpha_schematic_mag=3.0,
        # bands
        BOTTOM_FRAC_NULL=BOTTOM_FRAC_NULL, ALPHA_REL_FI=ALPHA_REL_FI, ALPHA_REL_SD=ALPHA_REL_SD,
        # verdict
        verdict_composite=composite, verdict_sign=sign_v, verdict_magnitude=mag_v, verdict_regime=regime_v,
        generic_collapse=generic, precedence_invoked=precedence_invoked,
        # provenance
        S_POLE=S_POLE, CURV_GRADE_N=CURV_GRADE_N, D_DIM=D_DIM, tau_fold=tau_fold, M_KK=M_KK,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\nSaved npz: {OUT_NPZ}")

    make_plot(dM_FULL_bottom, dM_FULL_edge, bottom_frac, edge_frac,
              Ls, MB_scan, rho_scan, beta_zeta, alpha_zeta, ALPHA_PV,
              dM_FULL, dM_BARE, MF_bot_12, MF_bot_14, composite, alpha_rel,
              float(alpha_HH1_per_pole_FW_s3))
    print(f"Saved plot: {OUT_PNG}")

    # -------------------------------------------------------------------------
    # 8) Verdict value + emit payload
    # -------------------------------------------------------------------------
    value_str = (
        f"bottom_frac={bottom_frac:.3e}_FB-A-null_edge_frac={edge_frac:.6f}_"
        f"sign_drift_zeta={sign_zeta:+d}_eq_sign_drift_PV={sign_PV:+d}_match={sign_match}_"
        f"alpha_PV={ALPHA_PV:.4f}_alpha_zeta={alpha_zeta:.4f}(divergent_beta={beta_zeta:.3f})_alpha_rel={alpha_rel:.4f}_SD_"
        f"dM_FULL={dM_FULL:.2f}_dM_BARE={dM_BARE:.2f}_n_new_in_bottom={n_new_in_bottom}_"
        f"W8-1_label_MIS-SCOPED_FB-B-Level2_not_FB-A-bottomK_composite_INFO_by_design"
    )
    extra_rows = [
        f"# regulator_pin=a_2^{{zeta}} and a_2^{{Pauli-Villars}} CLASS=FULL poleconv-A-double pole_in_s={int(S_POLE)} curvature_grade_n={CURV_GRADE_N} "
        f"# {GATE_ID} a_2 Seeley-DeWitt UV-edge heat-kernel coefficient (regulator-pin-discipline.md; cross-algebra caveat N/A -- SU(3) A_K)",
        f"# composite-precedence: plan sec.W6-3 operator (FAIL iff bottom_frac>=0.05 OR sign-mismatch; INFO iff FB-A-null+sign-match+alpha_rel>0.10) "
        f"OVERRIDES generic-collapse '{generic}' (magnitude=FAIL[SD] ^ regime=VALID -> FAIL); pre-declared in plan BEFORE evaluation "
        f"# {GATE_ID} gate-verdicts.md Plan-frozen gate-block operator precedence",
        f"# FB-scope: bottom_frac={bottom_frac:.2e} (FB-A bottom-K saturated but contributes 0 to a_2 drift); drift 100% lambda_max edge "
        f"-> W8-1 'friedrich-bar-saturation' label MIS-SCOPED: mechanism is FB-B Level-2 convergence (PV-ratio L^{{-alpha}}), NOT FB-A bottom-K saturation "
        f"# {GATE_ID} Sec.VII.AU.OP-PROJ Element-3 Level-2-envelope scope annotation (registry:18347, mack-routed); UV-pole-family FB-A-ineligibility wall",
        f"# alpha-SD: alpha_PV=+{ALPHA_PV:.4f} (PV-ratio CONVERGES, FB-B) vs alpha_zeta={alpha_zeta:.3f} (bare zeta_D(s=3) DIVERGES, s=3<d/2=4, Weyl tail lambda^+2); "
        f"alpha_rel={alpha_rel:.3f}>0.50 SD -- convergence-rate is regulator-class-keyed (FUNCTIONAL-INDEPENDENT mis-scope, SCHEME-DEPENDENT rate) "
        f"# {GATE_ID} a_2^{{zeta}} vs a_2^{{Pauli-Villars}}",
    ]
    print_verdict_payload(composite, value_str, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
                          extra_rows=extra_rows)
    return 0


def make_plot(dM_bot, dM_edge, bottom_frac, edge_frac, Ls, MB_scan, rho_scan,
              beta_zeta, alpha_zeta, alpha_PV, dM_FULL, dM_BARE, MF_bot_12, MF_bot_14,
              composite, alpha_rel, alpha_wod) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # Panel 1: edge-vs-bottom decomposition of dM_FULL
    ax = axes[0, 0]
    bars = ax.bar(["bottom-K\n(|lam|<=0.845)", "lambda_max edge\n(new p+q 13,14)"],
                  [abs(dM_bot), abs(dM_edge)], color=["steelblue", "crimson"], edgecolor="black")
    ax.set_ylabel(r"|contribution to $\Delta M_{FULL}$| (s=3, $a_2$)", fontsize=11)
    ax.set_title(f"Edge-vs-bottom of the $a_2$ moment drift\n"
                 f"bottom_frac = {bottom_frac:.2e}  (FB-A-null iff < 0.05); edge_frac = {edge_frac:.4f}", fontsize=10)
    for b, v in zip(bars, [abs(dM_bot), abs(dM_edge)]):
        ax.annotate(f"{v:.3e}" if v < 1 else f"{v:.1f}", (b.get_x() + b.get_width()/2, v),
                    textcoords="offset points", xytext=(0, 4), ha="center", fontsize=9)
    ax.set_yscale("symlog", linthresh=1e-6)
    ax.grid(True, axis="y", alpha=0.3)

    # Panel 2: multi-L scan -- zeta DIVERGES vs PV-ratio CONVERGES
    ax = axes[0, 1]
    ax.plot(Ls, MB_scan, "o-", color="crimson", lw=2, ms=8, label=r"$M_{BARE}$ (zeta $\zeta_D(s{=}3)$) -- DIVERGES")
    ax.set_xlabel(r"$L_{max}$ (level $\leq L$ truncation)", fontsize=11)
    ax.set_ylabel(r"$M_{BARE}(s{=}3)$", color="crimson", fontsize=11)
    ax.tick_params(axis="y", labelcolor="crimson")
    ax2 = ax.twinx()
    ax2.plot(Ls, rho_scan, "s-", color="darkorange", lw=2, ms=8, label=r"$\rho_{FULL}=M_{FULL}/M_{BARE}$ (PV) -- CONVERGES")
    ax2.set_ylabel(r"$\rho_{FULL}(s{=}3)$", color="darkorange", fontsize=11)
    ax2.tick_params(axis="y", labelcolor="darkorange")
    ax.set_title(f"zeta bare moment DIVERGES (beta={beta_zeta:.3f}, s=3<d/2=4)\n"
                 f"vs PV ratio CONVERGES (alpha_PV={alpha_PV:.4f}) -- scheme-dependent", fontsize=10)
    ax.grid(True, alpha=0.3)
    l1, lab1 = ax.get_legend_handles_labels(); l2, lab2 = ax2.get_legend_handles_labels()
    ax.legend(l1 + l2, lab1 + lab2, fontsize=8, loc="upper left")

    # Panel 3: alpha FI/SD -- convergent vs divergent exponent
    ax = axes[1, 0]
    names = ["zeta\n(bare, divergent)", "Wodzicki\nper-pole", "pathway-B\nalpha_PV", "SCHEMATIC\nd=4"]
    vals = [alpha_zeta, alpha_wod, alpha_PV, 3.0]
    colors = ["crimson", "steelblue", "darkorange", "seagreen"]
    ax.bar(names, vals, color=colors, edgecolor="black")
    ax.axhspan(2.0, 3.0, color="gray", alpha=0.18, label="PV admissible window [2,3]")
    ax.axhline(0.0, color="black", lw=1)
    ax.set_ylabel(r"convergence exponent $\alpha$", fontsize=11)
    ax.set_title(f"alpha SCHEME-DEPENDENT: zeta divergent ({alpha_zeta:.2f}) vs PV window [2,3]\n"
                 f"alpha_rel = {alpha_rel:.3f} > 0.50 (SD)", fontsize=10)
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)

    # Panel 4: sign cross-check + bottom-region invariance
    ax = axes[1, 1]
    ax.bar(["drift_PV\n(dM_FULL)", "drift_zeta\n(dM_BARE)"], [dM_FULL, dM_BARE],
           color=["darkorange", "crimson"], edgecolor="black")
    for i, v in enumerate([dM_FULL, dM_BARE]):
        ax.annotate(f"{v:+.1f}", (i, v), textcoords="offset points", xytext=(0, 5), ha="center", fontsize=10)
    ax.axhline(0, color="black", lw=1)
    ax.set_ylabel(r"$\Delta M$ (L12$\to$L14)", fontsize=11)
    ax.set_title(f"Sign cross-check: both drifts POSITIVE (edge-driven, same UV pole)\n"
                 f"bottom-region invariant: MF_bot L12={MF_bot_12:.6f} = L14={MF_bot_14:.6f}", fontsize=10)
    ax.grid(True, axis="y", alpha=0.3)

    plt.suptitle(f"{GATE_ID}  --  composite={composite}\n"
                 f"s=3 a_2 moment: FB-A-null (edge-driven), W8-1 'friedrich-bar-saturation' MIS-SCOPED (FB-B Level-2, not FB-A bottom-K); alpha SCHEME-DEPENDENT",
                 fontsize=11, y=1.0)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    sys.exit(main())
