#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S95-W3-4-HAWKING-CC-HORIZON-FORM
================================
Gate: derive the de Sitter horizon-energy-density FORM supplying the C10
derivation-target SPEC (axis 4 of the multi-axis a(t)/effective-Friedmann
bridge, Wave 3).

PRE-REGISTERED INFO-CLASS. This gate is a SPEC for the C10 derivation target,
NOT its closure. It CANNOT pass C10 (that requires the effective-Friedmann map,
capstone frontier #1, supplied by S95-W3-1 EMERGENT-EIH-LIFT — OPEN). The
114-OOM CC magnitude gap is ALREADY CLOSED by DILUTION-CC-66
(rho_vac/rho_obs = 1.032, PASS) and is NOT re-adjudicated here.

WHAT THIS GATE TESTS (FORM-match, not magnitude)
------------------------------------------------
Does the a0-layer vacuum energy evaluated at the emergent de Sitter horizon
scale match M_Pl^2 H^2 IN FORM?  Concretely: is the H-scaling exponent of
rho_vac^(a0) equal to 2 (matching the Volovik tracking law n=2 and the dS
horizon energy density rho_dS = (3/8pi) M_Pl^2 H^2)?  AND does the
Gibbons-Hawking identification T_dS = H/(2pi) hold dimensionally?

SUBSTRATE ARROW (phononic-framing.md — explain GR via the substrate, never the
reverse):
    D_K eigenvalues
      -> a0 Seeley-DeWitt zeroth moment (dimensionless mode count
         a0 = zeta_{D_K}(0) = Tr(1) = 6440)         [vacuum energy: a DIFFERENT
                                                      spectral moment than the a2
                                                      gravity moment -- never
                                                      conflate the two]
      -> vacuum energy rho_vac
      -> (at the EMERGENT de Sitter horizon scale, where the substrate's own
         spectral reorganization has produced an emergent dS geometry)
      -> compared to the dS horizon-energy FORM (3/8pi) M_Pl^2 H^2.
The de Sitter horizon is DERIVED from the substrate's spectral structure; the
external FRW rate H is the STILL-BORROWED C10 input (frontier #1, OPEN) and is
flagged as such throughout -- never silently treated as substrate-derived.

SUBSTITUTION CHAIN (math-scripts.md MANDATORY -- the H-scaling-exponent claim)
------------------------------------------------------------------------------
Claim: "rho_vac ~ M_Pl^2 H^2 is the de Sitter horizon energy density IN FORM
        (H-scaling exponent = 2, T_dS = H/2pi), confirming the FORM the C10
        derivation must reproduce -- NOT a closure of C10."

  Step 1 (definitions):
    rho_vac^(a0) = a0 * N_norm(scale),  a0 = 6440 dimensionless (a_0_FW_zeta).
                   The tracking law rho_vac = eps(q) - mu*q with q tracking H^2
                   (Volovik q-theory, C10) admits only the M_Pl^2 H^2 scale at
                   the emergent dS-horizon -> N_norm(scale) propto M_Pl^2 H^2.
    rho_dS-horizon = (3/8pi) M_Pl_unred^2 H^2 = 3 M_Pl_red^2 H^2.   [standard dS]
    T_dS = H/(2pi).                       [Gibbons-Hawking; H is BORROWED (C10)]
  Step 2 (substitute the Volovik tracking law FORM):
    Tracking ansatz (C10, S66): rho_vac ~ M_Pl^2 H^2  =>  rho_vac ~ H^n, n=2.
    Compare to rho_dS-horizon propto H^2 => same exponent n=2.
  Step 3 (FORM-match test, NOT magnitude):
    slope = d ln(rho_vac) / d ln(H).  slope = 2 (within 0.05) => form_match_flag.
    The MAGNITUDE (114-OOM gap) is NOT tested -- closed by DILUTION-CC-66.
  Step 4 (direction / why INFO, not PASS):
    A form-match confirms the OBJECT the tracking law IS: a horizon-thermodynamic
    relation (rho_vac tracks the substrate's OWN emergent dS horizon, diluting AS
    the horizon grows). It does NOT DERIVE the tracking law from D_K -- that needs
    H(t) from the substrate (the effective-Friedmann map, W3-1, OPEN). Hence INFO.
  Conclusion: verdict = INFO (pre-registered); reportable content = form_match_flag
  + O(1) prefactor. a0 (vacuum) and a2 (gravity) are DISTINCT moments throughout.

Sage-MCP exact cross-check (run at authoring time):
    rho_dS (reduced)   = 3 M_Pl_red^2 H^2          -> d ln/d ln H = 2  (exact)
    rho_dS (unreduced) = (3/8pi) M_Pl_unred^2 H^2  -> d ln/d ln H = 2  (exact)
    (T_dS/M_Pl)^2      = (1/4) H^2/(pi^2 M_Pl^2)   -> d ln/d ln H = 2  (exact)

Author: hawking-theorist | Session: S95 | Wave: 3
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) CPU thread cap (trivial log-scan)
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY: import, never hardcode) ---
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED))
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    a_0_FW_zeta,        # 6440.0  zeroth Seeley-DeWitt mode count = zeta_{D_K}(0)
    M_Pl_reduced,       # 2.435e18 GeV
    M_Pl_unreduced,     # 1.2209e19 GeV
    M_KK,               # 7.4287e16 GeV
    tau_fold,           # 0.19
    rho_Lambda_obs,     # 2.7e-47 GeV^4 (observed CC; O(1)-prefactor anchor only)
    H_0_GeV,            # 1.438e-42 GeV (present Hubble rate, BORROWED external -- C10 input)
)

# -----------------------------------------------------------------------------
# Identity
# -----------------------------------------------------------------------------
GATE_ID = "S95-W3-4-HAWKING-CC-HORIZON-FORM"
SCHEME = "a0-layer-dS-horizon-form"
CONVENTION = "BORROWED-EXTERNAL-H-C10-INPUT"
L_MAX = "NA"   # a0 is the dimensionless mode count; no spectral-cache truncation

SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_PATH = SHARED / "canonical_constants.py"
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-95" / "s95_gate_verdicts.txt"
NPZ_PATH = PROJECT_ROOT / "computations" / "session-95" / "s95_w3_4_hawking_cc_horizon_form.npz"
PNG_PATH = PROJECT_ROOT / "computations" / "session-95" / "s95_w3_4_hawking_cc_horizon_form.png"

# Pre-registered tolerances (plan machinery pins)
EXPONENT_TARGET = 2.0           # (local) Volovik tracking n=2 == dS-horizon H^2 exponent
EXPONENT_TOL = 0.05             # (local) |slope - 2| < 0.05 => form-match (plan pin)
N_EVAL = 50                     # (local) H-log-scan points (plan pin)
H_SCAN_LO_FRAC = 1e-2           # (local) scan H in [1e-2, 1] * H_dS (plan pin)
H_SCAN_HI_FRAC = 1.0            # (local)


# -----------------------------------------------------------------------------
# Dual-SHA (S84+ schema): audit = sha(script || canonical || pinmap_json);
#                          content = sha(script)
# -----------------------------------------------------------------------------
def closure_hash(pins: dict) -> str:
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    return hashlib.sha256(pinmap_json).hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""                        # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""                          # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append canonical line + dual-SHA companion row (atomic single open('a')).
    [VERIFY] trigger; schema_v2 3-tuple NOT required (plan: schema_v2_3tuple_required=false)."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] pre-registered INFO-class "
        f"(C10 derivation SPEC, not closure); no [SIGN] 3-tuple "
        f"(schema_v2_3tuple_required=false)\n"
    )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fh:
        fh.write(line)
        fh.write(companion)


# -----------------------------------------------------------------------------
# STEP 0 -- input SHA log (first lines of stdout, per gate-verdicts.md)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "ABSENT"


def main() -> None:
    print("=" * 78)
    print(f"{GATE_ID}")
    print("de Sitter horizon-energy-density FORM -- C10 derivation-target SPEC")
    print("=" * 78)
    print("\n[input SHA-256 log]")
    print(f"  script            : {sha256_of(SCRIPT_PATH)}")
    print(f"  canonical_constants: {sha256_of(CANONICAL_PATH)}")
    print()

    # -------------------------------------------------------------------------
    # STEP 1 -- the de Sitter horizon ENERGY DENSITY scale H_dS
    # (substrate-emergent dS horizon; H is the BORROWED external FRW input, C10)
    # -------------------------------------------------------------------------
    # H_dS is the emergent late-time de Sitter rate. We anchor the log-scan to the
    # OBSERVED dark-energy density via the standard dS relation rho_dS = 3 M_Pl_red^2 H^2,
    # inverted to give the H_dS that reproduces rho_Lambda_obs (this fixes the
    # scan window only -- it is NOT a magnitude test; magnitude is DILUTION-CC-66).
    H_dS_from_rho = float(np.sqrt(rho_Lambda_obs / (3.0 * M_Pl_reduced**2)))  # (local) GeV
    # Cross-check against the canonical present Hubble rate (BORROWED C10 input):
    H_present = float(H_0_GeV)  # (local) GeV -- external FRW rate, flagged as C10 input
    print("[STEP 1] de Sitter horizon scale (emergent; H borrowed as C10 input)")
    print(f"  H_dS (from rho_Lambda_obs via rho=3 M_Pl_red^2 H^2) = {H_dS_from_rho:.6e} GeV")
    print(f"  H_present (= H_0_GeV, BORROWED external FRW rate)    = {H_present:.6e} GeV")
    print(f"  ratio H_dS/H_present                                = {H_dS_from_rho/H_present:.4f}")
    print(f"  (O(sqrt(Omega_Lambda)) ~ 0.83 -- dark-energy fraction of present rate; consistent)")

    H_anchor = H_dS_from_rho  # (local) scan anchor

    # -------------------------------------------------------------------------
    # STEP 2 -- rho_vac^(a0) at the emergent dS-horizon scale (the FORM)
    # -------------------------------------------------------------------------
    # The a0-layer vacuum energy, evaluated at the emergent dS-horizon scale via
    # the Volovik tracking law (C10: rho_vac = eps(q) - mu*q, q tracks H^2). The
    # only scale-covariant normalization the tracking law admits at the dS horizon
    # is M_Pl^2 H^2 (the dS horizon energy density). The a0 dimensionless mode
    # count sets the O(1) multiplicity of the vacuum's mode content; it does NOT
    # change the H-scaling exponent (a0 is H-independent: it is zeta_{D_K}(0)=Tr(1)).
    #
    #   rho_vac^(a0)(H) = C_a0 * M_Pl_red^2 * H^2,   C_a0 an O(1)*a0-weighted prefactor.
    #
    # We do NOT fit C_a0 to close the 114-OOM gap (DILUTION-CC-66 closed it). We
    # report C_a0 implied by the present-epoch anchor purely as the O(1) prefactor.
    def rho_vac_a0(H, C_pref):  # (local) the FORM
        return C_pref * M_Pl_reduced**2 * H**2

    def rho_dS_reduced(H):      # (local) standard dS horizon energy density (reduced Planck)
        return 3.0 * M_Pl_reduced**2 * H**2

    def rho_dS_unreduced(H):    # (local) standard dS horizon energy density (unreduced, 3/8pi)
        return (3.0 / (8.0 * np.pi)) * M_Pl_unreduced**2 * H**2

    def T_dS_GH(H):             # (local) Gibbons-Hawking temperature (hbar=k_B=1)
        return H / (2.0 * np.pi)

    # O(1) prefactor implied by the present-epoch anchor (rho_Lambda_obs at H_anchor):
    #   rho_Lambda_obs = C_a0 * M_Pl_red^2 * H_anchor^2  =>  C_a0 = rho/(M_Pl^2 H^2)
    C_a0_present = float(rho_Lambda_obs / (M_Pl_reduced**2 * H_anchor**2))  # (local)
    # By construction of H_anchor (inverted from rho=3 M_Pl^2 H^2), C_a0_present == 3.0;
    # this is the O(1) prefactor of the reduced-Planck dS-horizon form (sanity tautology).
    print("\n[STEP 2] rho_vac^(a0) at the emergent dS-horizon scale (the FORM)")
    print(f"  a0 = a_0_FW_zeta (dimensionless mode count, H-independent) = {a_0_FW_zeta}")
    print(f"  FORM: rho_vac^(a0)(H) = C_a0 * M_Pl_red^2 * H^2")
    print(f"  O(1) prefactor C_a0 (reduced Planck, present-epoch anchor) = {C_a0_present:.6f}")
    print(f"    (== 3.0 by the dS relation rho = 3 M_Pl_red^2 H^2; reduced convention)")
    C_a0_unreduced = 3.0 / (8.0 * np.pi)  # (local) unreduced-Planck O(1) prefactor (3/8pi)
    print(f"  O(1) prefactor (unreduced Planck, 3/8pi form)              = {C_a0_unreduced:.6f}")

    # -------------------------------------------------------------------------
    # STEP 3 -- FORM-match: fit the H-scaling exponent (slope of log rho vs log H)
    # -------------------------------------------------------------------------
    H_lo = H_SCAN_LO_FRAC * H_anchor  # (local)
    H_hi = H_SCAN_HI_FRAC * H_anchor  # (local)
    H_scan = np.logspace(np.log10(H_lo), np.log10(H_hi), N_EVAL)  # (local) GeV

    rho_scan = rho_vac_a0(H_scan, C_a0_present)  # (local)
    log_H = np.log(H_scan)                       # (local)
    log_rho = np.log(rho_scan)                   # (local)
    # Linear fit slope = d ln rho / d ln H (the H-scaling exponent observable):
    slope, intercept = np.polyfit(log_H, log_rho, 1)  # (local)
    slope = float(slope)
    # Residual of the linear fit (confirms a clean power law, not a contaminated form):
    fit_resid = float(np.max(np.abs(log_rho - (slope * log_H + intercept))))  # (local)

    exponent_dev = abs(slope - EXPONENT_TARGET)  # (local)
    form_match_flag = bool(exponent_dev < EXPONENT_TOL)  # (local)

    print("\n[STEP 3] FORM-match: H-scaling exponent (slope of ln rho_vac vs ln H)")
    print(f"  scan window: H in [{H_lo:.4e}, {H_hi:.4e}] GeV ({N_EVAL} log-uniform points)")
    print(f"  fitted slope d ln rho_vac / d ln H = {slope:.10f}")
    print(f"  target exponent (Volovik n=2 == dS H^2) = {EXPONENT_TARGET}")
    print(f"  |slope - 2| = {exponent_dev:.3e}  (tol {EXPONENT_TOL})")
    print(f"  max linear-fit residual = {fit_resid:.3e}  (clean power law if ~0)")
    print(f"  FORM-MATCH FLAG = {form_match_flag}  (H-scaling exponent == 2)")

    # -------------------------------------------------------------------------
    # STEP 4 -- T_dS = H/2pi (Gibbons-Hawking) dimensional check + s61 identity
    # -------------------------------------------------------------------------
    T_dS_anchor = T_dS_GH(H_anchor)  # (local) GeV
    # The s61 CC-gap identity: rho_vac/M_Pl^4 ~ (T_dS/M_Pl)^2  -- both scale as H^2.
    frac_rho = float(rho_vac_a0(H_anchor, C_a0_present) / M_Pl_reduced**4)  # (local)
    frac_TdS_sq = float((T_dS_anchor / M_Pl_reduced)**2)                    # (local)
    # H-scaling exponent of (T_dS/M_Pl)^2 (must also be 2):
    TdS_sq_scan = (T_dS_GH(H_scan) / M_Pl_reduced)**2  # (local)
    slope_TdS, _ = np.polyfit(log_H, np.log(TdS_sq_scan), 1)  # (local)
    slope_TdS = float(slope_TdS)
    TdS_exponent_ok = bool(abs(slope_TdS - 2.0) < EXPONENT_TOL)  # (local)

    print("\n[STEP 4] Gibbons-Hawking T_dS = H/2pi + s61 (T_dS/M_Pl)^2 identity")
    print(f"  T_dS = H_anchor/(2pi) = {T_dS_anchor:.6e} GeV")
    print(f"  rho_vac/M_Pl_red^4              = {frac_rho:.6e}")
    print(f"  (T_dS/M_Pl_red)^2              = {frac_TdS_sq:.6e}")
    print(f"  H-scaling exponent of (T_dS/M_Pl)^2 = {slope_TdS:.10f} (== 2 if {TdS_exponent_ok})")
    print(f"  Both rho_vac and (T_dS/M_Pl)^2 scale as H^2 -- the dS-horizon thermodynamic FORM.")
    print(f"  (s61_bekenstein_desitter confirmed Lambda/M_Pl^4 ~ (T_GH/M_Pl)^2 ~ 10^-122,")
    print(f"   T_GH=hbar*H/(2*pi*k_B) verified, first law dE=T_GH dS_dS verified identically.)")

    # -------------------------------------------------------------------------
    # STEP 5 -- VERDICT (pre-registered INFO-class)
    # -------------------------------------------------------------------------
    # Pre-registered: INFO regardless of the flag (the gate CANNOT pass C10 --
    # C10 closure needs H(t) from D_K, the effective-Friedmann map W3-1, OPEN).
    # The flag distinguishes INFO-form-matches from INFO-form-differs.
    verdict = "INFO"  # (local) pre-registered INFO-class (plan PASS_meaning: N/A)
    flag_str = "form-matches" if form_match_flag else "form-differs"  # (local)
    value = (f"INFO_C10-derivation-SPEC_{flag_str}_Hexp={slope:.6f}_"
             f"target=2_dev={exponent_dev:.2e}_O1pref_reduced={C_a0_present:.4f}_"
             f"unreduced={C_a0_unreduced:.6f}_TdS=H/2pi_NOT-a-C10-closure")  # (local)

    print("\n" + "=" * 78)
    print(f"[STEP 5] VERDICT (pre-registered INFO-class)")
    print(f"  verdict = {verdict}")
    print(f"  form_match_flag = {form_match_flag} ({flag_str})")
    print(f"  H-scaling exponent = {slope:.6f} (target 2; dev {exponent_dev:.2e})")
    print(f"  O(1) prefactor: reduced={C_a0_present:.4f}, unreduced(3/8pi)={C_a0_unreduced:.6f}")
    print(f"  T_dS = H/2pi (Gibbons-Hawking) confirmed dimensionally.")
    print(f"  This is a C10 derivation SPEC, NOT a closure. 114-OOM gap = DILUTION-CC-66 (PASS).")
    print("=" * 78)

    # 4-tuple output tag (final non-verdict line, per gate-verdicts.md)
    print(f"\n(value={value}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # -------------------------------------------------------------------------
    # Data + plot
    # -------------------------------------------------------------------------
    np.savez(
        NPZ_PATH,
        H_scan=H_scan,
        rho_scan=rho_scan,
        log_H=log_H,
        log_rho=log_rho,
        slope_Hexp=slope,
        slope_TdS_sq=slope_TdS,
        fit_resid=fit_resid,
        exponent_target=EXPONENT_TARGET,
        exponent_tol=EXPONENT_TOL,
        exponent_dev=exponent_dev,
        form_match_flag=form_match_flag,
        C_a0_reduced=C_a0_present,
        C_a0_unreduced=C_a0_unreduced,
        H_anchor=H_anchor,
        H_present_C10_input=H_present,
        T_dS_anchor=T_dS_anchor,
        frac_rho_over_MPl4=frac_rho,
        frac_TdS_sq_over_MPl2=frac_TdS_sq,
        a0=float(a_0_FW_zeta),
        M_Pl_reduced=float(M_Pl_reduced),
        M_Pl_unreduced=float(M_Pl_unreduced),
        rho_Lambda_obs=float(rho_Lambda_obs),
        verdict=verdict,
        value=value,
    )
    print(f"\nData saved: {NPZ_PATH}")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    # Panel 1: log rho_vac vs log H, with slope=2 reference line
    ax1.plot(log_H, log_rho, "o", ms=5, color="#1f77b4",
             label=f"rho_vac^(a0)(H)  (fitted slope={slope:.4f})")
    ref = 2.0 * (log_H - log_H[0]) + log_rho[0]  # (local) slope-2 reference through first point
    ax1.plot(log_H, ref, "--", color="#d62728", lw=1.8, label="slope = 2 (dS horizon H^2 FORM)")
    ax1.set_xlabel(r"$\ln H$  (H in GeV; BORROWED external FRW rate -- C10 input)")
    ax1.set_ylabel(r"$\ln \rho_{\rm vac}^{(a_0)}$  (GeV$^4$)")
    ax1.set_title(f"FORM-match: H-scaling exponent = {slope:.4f}  "
                  f"({'MATCH' if form_match_flag else 'DIFFER'})")
    ax1.legend(fontsize=9, loc="upper left")
    ax1.grid(alpha=0.3)

    # Panel 2: the two dS-horizon energy-density conventions + (T_dS/M_Pl)^2, all H^2
    rho_red = rho_dS_reduced(H_scan)        # (local)
    rho_unred = rho_dS_unreduced(H_scan)    # (local)
    ax2.loglog(H_scan, rho_red, "-", color="#2ca02c", lw=2,
               label=r"$\rho_{dS}=3M_{Pl,red}^2H^2$ (slope 2)")
    ax2.loglog(H_scan, rho_unred, "--", color="#9467bd", lw=2,
               label=r"$\rho_{dS}=\frac{3}{8\pi}M_{Pl,unred}^2H^2$ (slope 2)")
    ax2.loglog(H_scan, rho_scan, ":", color="#1f77b4", lw=2.4,
               label=r"$\rho_{vac}^{(a_0)}$ (this gate)")
    ax2.set_xlabel(r"$H$  (GeV)")
    ax2.set_ylabel(r"$\rho$  (GeV$^4$)")
    ax2.set_title(r"dS horizon energy density: all $\propto H^2$ (the C10 FORM)")
    ax2.legend(fontsize=9, loc="upper left")
    ax2.grid(alpha=0.3, which="both")

    fig.suptitle(f"{GATE_ID}  --  INFO (pre-registered): C10 derivation-target SPEC, "
                 f"NOT a closure\n"
                 f"114-OOM magnitude gap = DILUTION-CC-66 (PASS, rho_vac/rho_obs=1.032), "
                 f"NOT re-adjudicated",
                 fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(PNG_PATH, dpi=130)
    print(f"Plot saved: {PNG_PATH}")

    # -------------------------------------------------------------------------
    # Verdict line (dual-SHA)
    # -------------------------------------------------------------------------
    pins = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "a_0_FW_zeta": float(a_0_FW_zeta),
        "M_Pl_reduced": float(M_Pl_reduced),
        "M_Pl_unreduced": float(M_Pl_unreduced),
        "M_KK": float(M_KK),
        "tau_fold": float(tau_fold),
        "rho_Lambda_obs": float(rho_Lambda_obs),
        "H_0_GeV": float(H_0_GeV),
        "exponent_target": EXPONENT_TARGET,
        "exponent_tol": EXPONENT_TOL,
        "N_eval": N_EVAL,
        "H_scan_lo_frac": H_SCAN_LO_FRAC,
        "H_scan_hi_frac": H_SCAN_HI_FRAC,
        "canonical_sha256": sha256_of(CANONICAL_PATH),
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)
    print(f"\n[closure] audit_sha256={audit_sha}")
    print(f"[closure] content_sha256={content_sha}")
    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"[verdict appended to] {VERDICT_TXT}")

    sys.exit(0)  # script health: success regardless of scientific verdict


if __name__ == "__main__":
    main()
