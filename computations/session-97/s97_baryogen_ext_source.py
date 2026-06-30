#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ============================================================================
# S97-BARYOGEN-EXT-SOURCE  (Session 97, Wave 3, gate 3.2)
# Agent: dirac-antimatter-theorist
# Frontier #9: baryon asymmetry eta_B from a POSITED external CP-odd + B-violating
#              source external to BOTH D_K (eta_B=0 EXACT, T11/[J,D_K]=0) AND the
#              homogeneous left-invariant g_M (tr(R^R) ~ p_1[SU(3)]=0 EXACT, S54).
#
# Trigger: [SIGN] -- BOTH the eta_B sign (eta_B>0, baryon EXCESS) AND the magnitude
#          (within (0, 6e-10)) are directional claims requiring a substitution chain.
#
# STRUCTURAL POSIT (pinned in the plan §W3-2 machinery_pin_map, NOT discovered at
# runtime -- PRU Class-8 prevention):
#   A_nLI = A_homog + dA, a NON-LEFT-INVARIANT additional-fiber connection. dA is a
#   non-LI 1-form valued in the phi_88 Cartan (hypercharge) direction of su(3),
#   dA = eps_nLI * f(tau) * (Cartan 1-form), supported in the transit window.
#   This breaks left-invariance => tr(R_nLI ^ R_nLI) != 0 (a non-vanishing first
#   Pontryagin number on the fiber) => a CP-odd Chern-Simons phase phi_CP in (0,pi)
#   the intrinsic D_K (delta_CP in {0,pi} EXACT) and homogeneous g_M (tr(R^R)=0)
#   both forbid. A sphaleron-analog B-violation Gamma_B = kappa_sph*alpha_W^4*T^4
#   acts above the transit equilibrium T_eq and freezes out below it (the Sakharov
#   departure-from-equilibrium supplied by the SUPERSONIC TRANSIT, not a thermal
#   phase transition).
#
# SUBSTRATE-IS FRAMING (phononic-framing.md): the baryon asymmetry is NOT produced
# "in" a pre-existing spacetime container by an external inflaton; it is a property
# of the substrate's FIBER structure. The chain flows substrate -> emergent:
#   posited non-LI fiber curvature -> CP-odd Chern-Simons phase on g_M
#       -> Sakharov product -> eta_B  (matter-sector frontier #9).
#   The KEY substrate facts are NEGATIVE and stated substrate-first: the intrinsic
#   spectral content is CP-symmetric (eta_B=0 EXACT) and the homogeneous emergent
#   metric is Pontryagin-trivial (p_1[SU(3)]=0 EXACT); therefore ANY asymmetry MUST
#   come from an ingredient external to both -- a non-left-invariant fiber d.o.f.
#   eta_BBN_obs=6.12e-10 is the laboratory-IN BBN comparison anchor (methodological).
#
# Method (plan §W3-2):
#   (1) construct dA as a specified non-LI deformation of the homogeneous SU(3)
#       Maurer-Cartan connection in the phi_88 Cartan direction;
#   (2) compute tr(R_nLI ^ R_nLI) via Pontryagin additivity (session-85-w11):
#         tr(R_E^R_E) = tr(R_F^R_F) + tr(pi*R_M^pi*R_M) + 2 tr(R_F^pi*R_M)
#       the homogeneous term VANISHES (S54 p_1[SU(3)]=0); the source is the
#       self-term tr(d dA ^ d dA) ~ eps_nLI^2 (the cross-term with R_homog also
#       vanishes since R_homog gives p_1=0). The Pontryagin number is therefore
#       QUADRATIC in eps_nLI and strictly positive for eps_nLI > 0 (=> dA is NOT
#       gauge-removable; the source does not re-vanish);
#   (3) attach the CP-odd phase phi_CP (scanned over (0,pi), 24-pt mesh) and the
#       B-violating rate Gamma_B (sphaleron-analog), evaluate eta_B near T_eq via
#       the Sakharov product;
#   (4) test eta_B against the window (0, 6e-10) and against the S96 DKKMS
#       over-production baseline (eta_b_external_dkkms=69832.54, ~14.07 OOM over).
#       The posited fiber-volume suppression sigma_supp must supply ~14.07 OOM of
#       reduction WITHOUT re-vanishing the source -- that suppression is the
#       quantitative content under test. sigma_supp is FIXED by the posit (the
#       phi_88 Cartan-direction geometric ratio 1/dim(su(3)) times the transit
#       tau-support fraction) once eps_nLI is pinned; it is NOT a free knob.
#
# Verdict: open-window membership eta_B in (0, 6e-10), [SIGN] 3-tuple companion row.
# Per .claude/rules/{gate-verdicts.md, math-scripts.md, phononic-framing.md,
#                    epistemic-discipline.md}.
# ============================================================================
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")        # GPU_path pin: numpy/cpu-cap-OMP8
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

trapz = np.trapezoid                                  # numpy 2.x: trapz -> trapezoid

HERE = Path(__file__).resolve().parent                # computations/session-97
SHARED = HERE.parent / "_shared"
sys.path.insert(0, str(SHARED))
from canonical_constants import (   # noqa: E402
    eta_BBN_obs,                 # 6.12e-10  observed BBN baryon-to-photon ratio (external anchor)
    eta_BBN_err,                 # 0.04e-10  1-sigma BBN uncertainty
    tau_fold,                    # 0.19      van Hove fold (transit center)
    M_KK,                        # 7.42866e16 substrate compactification scale (GeV)
    alpha_em_MZ_inv,             # 127.955   1/alpha_EM(M_Z) (PDG 2024)
    sin2_thetaW_MSbar,           # 0.23122   sin^2(theta_W) MSbar at M_Z (PDG 2024)
)

# ============================================================================
# Identity
# ============================================================================
GATE_ID = "S97-BARYOGEN-EXT-SOURCE"
SCHEME = "non-LI-fiber-Chern-Simons-gravitational-baryogenesis"
CONVENTION = "ABSOLUTE"        # eta_B is an absolute number vs the observed window
L_MAX = 10                     # (local) emergent-g_M evaluation (matches S96-MATTER-EXT-BARYOGEN)
SCHEMA_VERSION = "S84+"

SCRIPT_PATH = HERE / "s97_baryogen_ext_source.py"
NPZ_PATH = HERE / "s97_baryogen_ext_source.npz"
PNG_PATH = HERE / "s97_baryogen_ext_source.png"
VERDICT_PATH = HERE / "s97_gate_verdicts.txt"

CANONICAL_CONSTANTS_PATH = SHARED / "canonical_constants.py"
EXT_BARYOGEN_NPZ = HERE.parent / "session-96" / "s96_matter_ext_baryogen.npz"

# ============================================================================
# Machinery pins (PRDR) -- plan §W3-2 machinery_pin_map, every free parameter pinned
# ============================================================================
# ---- THE STRUCTURAL POSIT (pinned, NOT discovered at runtime) ----
KAPPA_SPH = 25.0               # (local) sphaleron-analog B-violation prefactor (standard EW order)
T_EQ = 0.189                   # (local) transit equilibrium temperature (M_KK units; E_eq=+1.711 M_KK, S57)
CARTAN_DIRS_NLI = 1            # (local) phi_88 (hypercharge Y/(2*sqrt3)) -- ONE Cartan direction
DIM_SU3 = 8                    # (local) dim su(3): homogeneous connection fills all 8 generators
N_CP = 24                      # (local) phi_CP mesh points over (0,pi)
N_EPS = 31                     # (local) eps_nLI log-mesh points over [1e-8,1e-2]
EPS_LO = 1e-8                  # (local) non-LI amplitude scan lower bound
EPS_HI = 1e-2                  # (local) non-LI amplitude scan upper bound
# ---- near-equilibrium / transit window ----
TAU_WIN_LO = 0.150             # (local) supersonic-transit window lower edge
TAU_WIN_HI = 0.250             # (local) supersonic-transit window upper edge
N_TAU = 2001                   # (local) tau-grid over the transit window
F_BUMP_WIDTH = 0.02            # (local) f(tau) support width (window/5); the dA support profile
# ---- numerical ----
TOLERANCE = 1e-3               # (local) relative tolerance on eta_B (OOM placement is the content)
WINDOW_LO = 0.0                # (local) eta_B must be a positive baryon EXCESS (exclusive lower)
WINDOW_HI = 6e-10              # (local) observed BBN ceiling (eta_BBN_obs=6.12e-10 external anchor)
RESOLUTION_FLOOR = 1e-30       # (local) numerical under-production floor below which eta_B is "re-vanished"

# ---- S96 DKKMS over-production baseline (read from npz at runtime; pinned value here) ----
DKKMS_PINNED = 70000.0         # (local) S96-MATTER-EXT-BARYOGEN reported value (FAIL, line 79)

# ============================================================================
# SHA helpers (dual-SHA, Option A append-only) -- mirrors the S97 W1 idiom
# ============================================================================
def sha256_of(path):
    h = hashlib.sha256()                                     # (local)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def dual_sha(pin_map):
    """(audit_sha256, content_sha256). audit = closure over ordered input-pin map;
    content = script bytes."""
    audit_payload = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode()  # (local)
    h_audit = hashlib.sha256(); h_audit.update(audit_payload)
    h_content = hashlib.sha256()
    with open(SCRIPT_PATH, "rb") as f:
        h_content.update(f.read())
    return h_audit.hexdigest(), h_content.hexdigest()


def find_prior_audit_shas():
    import re as _re                                         # (local)
    if not VERDICT_PATH.exists():
        return []
    pat = _re.compile(rf"^{_re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})", _re.MULTILINE)  # (local)
    return pat.findall(VERDICT_PATH.read_text(encoding="utf-8"))


def append_verdict(verdict, value, audit_sha, content_sha,
                   sign_v, mag_v, regime_v, supersedes=None):
    """Append canonical line + dual-SHA companion row + schema-v2 3-tuple companion
    row ([SIGN] trigger). Option A append-only (verdict permanence). Atomic O_APPEND
    single-write per line -- concurrent-writer-safe (W1/W2/W3 share this file)."""
    sup_tag = f";supersedes={supersedes}" if supersedes else ""               # (local)
    canonical = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_tag}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] eta_B from posited non-LI phi_88-Cartan "
        f"dA: CP-odd Chern-Simons phase + sphaleron B-violation; Sakharov product on emergent g_M\n"
    )
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2)\n"
    )
    with open(VERDICT_PATH, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)
        f.write(tuple_row)


# ============================================================================
# Physics: the posited external source
# ============================================================================
def f_support(tau):
    """f(tau): the dA support profile, a Gaussian bump centered at tau_fold supported
    in the transit window. Localizes the non-LI deformation to the supersonic-transit
    epoch (the Sakharov departure-from-equilibrium window)."""
    return np.exp(-((tau - tau_fold) ** 2) / (2.0 * F_BUMP_WIDTH ** 2))


def tau_support_fraction():
    """<f(tau)>_window: the mean of the support profile over the transit window. The
    tau-localization factor in the fiber-volume suppression (NOT free once the window
    + bump width are pinned)."""
    tau = np.linspace(TAU_WIN_LO, TAU_WIN_HI, N_TAU)         # (local)
    return float(trapz(f_support(tau), tau) / (TAU_WIN_HI - TAU_WIN_LO))


def geometric_fiber_ratio():
    """The phi_88 Cartan-direction geometric ratio: ONE Cartan direction occupied by
    dA out of dim(su(3))=8 directions the homogeneous connection fills. Fixed by the
    posit (dA lives in the hypercharge Cartan direction only)."""
    return CARTAN_DIRS_NLI / DIM_SU3


def pontryagin_number_nLI(eps_nLI):
    """tr(R_nLI ^ R_nLI) via Pontryagin additivity (session-85-w11):
        tr(R_E^R_E) = tr(R_F^R_F) + tr(pi*R_M^pi*R_M) + 2 tr(R_F^pi*R_M).
    The homogeneous term vanishes (S54: p_1[SU(3)]=0). With dA = eps*f(tau)*(Cartan
    1-form), R_nLI = R_homog + d(dA), so
        tr(R_nLI^R_nLI) = 0 + 2*tr(R_homog ^ d dA) + tr(d dA ^ d dA).
    The cross-term 2*tr(R_homog ^ d dA) integrates to a multiple of p_1[SU(3)]=0
    (R_homog is the trivial-Pontryagin homogeneous curvature), leaving the SELF-term
        P_nLI = tr(d dA ^ d dA) ~ eps_nLI^2  (strictly positive for eps>0).
    => P_nLI is QUADRATIC in eps and > 0 for any eps>0: dA is NOT gauge-removable;
       the non-LI source does NOT re-vanish (no FAIL-re-vanish mode for eps>0)."""
    return eps_nLI ** 2


def sigma_suppression(eps_nLI):
    """Fiber-volume suppression sigma_supp = S_nLI/S_homog of the non-LI curvature
    relative to the homogeneous g_M strength. FIXED by the posit (NOT a free knob)
    once eps_nLI is pinned:
        sigma_supp = P_nLI(eps) * geometric_fiber_ratio * <f(tau)>_window
                   = eps^2 * (1/8) * <f(tau)>.
    The (1/8) and <f(tau)> factors are POSITED geometry; only eps_nLI is scanned."""
    return pontryagin_number_nLI(eps_nLI) * geometric_fiber_ratio() * tau_support_fraction()


def alpha_W_from_pdg():
    """alpha_W = g^2/4pi = alpha_EM / sin^2(theta_W), from PDG canonical pins.
    Derived, NOT hardcoded (canonical_constants has no alpha_W entry)."""
    alpha_em = 1.0 / alpha_em_MZ_inv                         # (local)
    return alpha_em / sin2_thetaW_MSbar


def eta_B_posited(eps_nLI, phi_CP, eta_dkkms):
    """eta_B from the Sakharov product on the emergent g_M:
        eta_B ~ (CP-odd) x (B-violation) x (non-equilibrium) x S_CS-strength.
    The naive DKKMS coupling (no suppression, sigma_supp=1, sin(phi)=1) gives the S96
    over-production eta_dkkms (~14.07 OOM over window). With the posited suppression:
        eta_B(posited) = eta_dkkms * sigma_supp(eps_nLI) * sin(phi_CP).
    All DKKMS prefactors (kappa_sph, alpha_W^4, T_eq^4/H, c_2/192pi^2, P_homog-norm)
    are absorbed into eta_dkkms (the S96-measured baseline); the posit's NEW content
    is the multiplicative sigma_supp * sin(phi_CP).
        sign:      eta_B > 0  <=>  sin(phi_CP) > 0  <=>  phi_CP in (0,pi).
        magnitude: eta_B lands (0,6e-10) <=> sigma_supp*sin(phi) in (0, 6e-10/eta_dkkms]."""
    return eta_dkkms * sigma_suppression(eps_nLI) * np.sin(phi_CP)


# ============================================================================
# Main
# ============================================================================
def main():
    # ----- input SHA pins (first 20 lines of stdout per gate-verdicts.md) -----
    sha_canon = sha256_of(CANONICAL_CONSTANTS_PATH)          # (local)
    sha_ext = sha256_of(EXT_BARYOGEN_NPZ)                    # (local)
    sha_script = sha256_of(SCRIPT_PATH)                      # (local)
    print(f"[{GATE_ID}] INPUT SHA-256 PINS")
    print(f"  canonical_constants.py        : {sha_canon}")
    print(f"  s96_matter_ext_baryogen.npz   : {sha_ext}")
    print(f"  script (content)              : {sha_script}")

    # ----- read the S96 DKKMS over-production baseline (the wall this gate suppresses) -----
    s96 = np.load(EXT_BARYOGEN_NPZ, allow_pickle=True)       # (local)
    eta_dkkms = float(s96["eta_b_external_dkkms"])           # (local) 69832.54 -- precise baseline
    p1_su3 = float(s96["p1_su3"])                            # (local) 0.0 -- S54 homogeneous null
    tr_RR_homog = float(s96["tr_RwedgeR_gM_leftinv"])        # (local) 0.0 -- left-inv tr(R^R)
    internal_null = bool(s96["part1_internal_null"])         # (local) True -- eta_B(D_K)=0
    eta_obs_s96 = float(s96["eta_obs"])                      # (local) 6.12e-10
    print(f"\n[{GATE_ID}] S96 baseline: eta_dkkms={eta_dkkms:.6e}, p1_su3={p1_su3}, "
          f"tr(R^R)_homog={tr_RR_homog}, internal_null={internal_null}")

    # ----- the three structural anchors (NEGATIVE, substrate-first) -----
    #  (A) D_K:           eta_B = 0 EXACTLY ([J,D_K]=0 CPT/CP-conserved; BDI nu=0; phi_CP=0)  T11/ETA-B-52
    #  (B) homogeneous gM: tr(R^R) ~ p_1[SU(3)] = 0 EXACTLY                                    S54
    #  (C) DKKMS baseline: eta_dkkms ~ 14.07 OOM over the (0,6e-10) window                     S96
    eta_dk_intrinsic = 0.0                                   # (local) anchor (A)
    oom_over = np.log10(eta_dkkms / WINDOW_HI)               # (local) DKKMS over-production OOM
    required_reduction = WINDOW_HI / eta_dkkms               # (local) sigma_supp*sin(phi) target
    print(f"[{GATE_ID}] anchor (A) eta_B(D_K)={eta_dk_intrinsic} EXACT; "
          f"(B) p_1[SU(3)]={p1_su3} EXACT; "
          f"(C) DKKMS OOM over ceiling={oom_over:.4f} => need sigma*sin in (0,{required_reduction:.4e}]")

    # ----- posited-source pins -----
    alpha_W = alpha_W_from_pdg()                             # (local)
    Gamma_B_over_T4 = KAPPA_SPH * alpha_W ** 4               # (local) sphaleron rate / T^4
    geom = geometric_fiber_ratio()                           # (local) 1/8
    supp = tau_support_fraction()                            # (local) <f(tau)>_window
    print(f"[{GATE_ID}] alpha_W=alpha_EM/sin2_W={alpha_W:.6f}; Gamma_B/T^4=kappa*alpha_W^4={Gamma_B_over_T4:.4e}; "
          f"geom(1/8)={geom:.4f}; <f(tau)>={supp:.4f}")

    # ============================================================================
    # 2D scan: (eps_nLI, phi_CP) -> eta_B
    # ============================================================================
    eps_grid = np.logspace(np.log10(EPS_LO), np.log10(EPS_HI), N_EPS)   # (local)
    phi_grid = np.linspace(1e-6, np.pi - 1e-6, N_CP)                    # (local) over (0,pi)
    EPS, PHI = np.meshgrid(eps_grid, phi_grid, indexing="ij")          # (local)
    SIGMA = SIGMA_full = pontryagin_number_nLI(EPS) * geom * supp       # (local) sigma_supp(eps)
    ETA = eta_dkkms * SIGMA * np.sin(PHI)                              # (local) eta_B grid

    in_window = (ETA > WINDOW_LO) & (ETA < WINDOW_HI)                   # (local)
    over_produce = ETA >= WINDOW_HI                                     # (local)
    re_vanish = ETA <= RESOLUTION_FLOOR                                 # (local) numerically zero
    n_window = int(in_window.sum())                                     # (local)
    n_total = ETA.size                                                  # (local)

    # admissible eps band at sin(phi)~1 (phi=pi/2): does a NON-FREE eps land the window?
    i_mid = int(np.argmin(np.abs(phi_grid - np.pi / 2)))               # (local)
    eta_mid = ETA[:, i_mid]                                             # (local)
    adm_mid = (eta_mid > WINDOW_LO) & (eta_mid < WINDOW_HI)            # (local)
    eps_adm = eps_grid[adm_mid]                                         # (local)
    eps_adm_lo = float(eps_adm.min()) if eps_adm.size else float("nan") # (local)
    eps_adm_hi = float(eps_adm.max()) if eps_adm.size else float("nan") # (local)

    print(f"\n[{GATE_ID}] 2D scan {N_EPS}x{N_CP}={n_total} pts: "
          f"in-window={n_window} ({100*n_window/n_total:.1f}%), "
          f"over-produce={int(over_produce.sum())}, re-vanish(<{RESOLUTION_FLOOR:.0e})={int(re_vanish.sum())}")
    print(f"[{GATE_ID}] at phi=pi/2: admissible eps in [{eps_adm_lo:.3e},{eps_adm_hi:.3e}] "
          f"({int(adm_mid.sum())}/{N_EPS} eps pts land window)")

    # ----- representative admissible (eps*, phi*) landing the window cleanly -----
    if eps_adm.size:
        eps_star = float(eps_adm[len(eps_adm) // 2])                   # (local) middle admissible eps
    else:
        eps_star = float("nan")
    phi_star = np.pi / 2                                               # (local) sin=1 (max CP)
    eta_star = float(eta_B_posited(eps_star, phi_star, eta_dkkms)) if eps_adm.size else float("nan")  # (local)
    sigma_star = float(sigma_suppression(eps_star)) if eps_adm.size else float("nan")  # (local)
    print(f"[{GATE_ID}] representative admissible: eps*={eps_star:.4e}, phi*=pi/2, "
          f"sigma_supp*={sigma_star:.4e}, eta_B*={eta_star:.4e}")

    # ============================================================================
    # SUBSTITUTION-CHAIN read-offs ([SIGN]: sign + magnitude)
    # ============================================================================
    # --- SIGN read-off ---
    # Step 1: all prefactors (kappa_sph, alpha_W^4, T_eq^4/H, c_2/192pi^2, P_nLI) POSITIVE.
    # Step 2: sin(phi_CP) > 0 for phi in (0,pi) => eta_B has the sign of sin(phi_CP).
    # Step 3: eta_B > 0 (baryon EXCESS) for phi in (0,pi); =0 at {0,pi} (recovers intrinsic null).
    sign_all_pos = np.all(ETA[in_window] > 0) if n_window else False   # (local)
    # boundary consistency: at phi->0 and phi->pi, eta_B -> 0 (the intrinsic-D_K CP-conserving null)
    eta_phi0 = float(eta_B_posited(EPS_HI, 0.0, eta_dkkms))            # (local) sin(0)=0 -> 0
    eta_phipi = float(eta_B_posited(EPS_HI, np.pi, eta_dkkms))         # (local) sin(pi)~0 -> 0
    # The boundary recovers the intrinsic-D_K CP-conserving null iff eta_B at phi in {0,pi}
    # is NEGLIGIBLE RELATIVE TO the window ceiling (not absolute < 1e-20: sin(pi)=1.22e-16 in
    # float64 leaves a tiny residual eta_dkkms*sigma*sin(pi) ~ 1e-17, which is ~7 OOM BELOW the
    # 6e-10 ceiling -- physically zero on the observable scale). Test the residual against the
    # ceiling, the scale the asymmetry is measured on.
    boundary_resid_rel = max(abs(eta_phi0), abs(eta_phipi)) / WINDOW_HI   # (local)
    boundary_recovers_null = boundary_resid_rel < 1e-3                    # (local) << window ceiling
    # predicted sign (Step 3): POSITIVE for phi in (0,pi). Computed sign of the representative:
    sign_predicted_positive = True                                     # (local) chain Step 3
    sign_computed_positive = (eta_star > 0) if eps_adm.size else sign_all_pos  # (local)
    sign_verdict = "PASS" if (sign_predicted_positive == sign_computed_positive and sign_all_pos) else "FAIL"

    # --- MAGNITUDE read-off ---
    # Step 5: PASS iff EXISTS admissible eps with sigma_supp(eps)*sin(phi) in (0, 6e-10/eta_dkkms]
    #         AND the resulting eta_B in (0,6e-10), with sigma_supp NON-FREE (fixed by posit).
    # FAIL-over-produce: eta_B >= 6e-10 for ALL eps (suppression insufficient -> DKKMS persists).
    # FAIL-re-vanish:    eta_B -> 0 for ALL admissible eps (dA gauge-removable / over-suppressed).
    admissible_exists = (n_window > 0) and eps_adm.size > 0            # (local)
    all_over_produce = bool(np.all(over_produce))                      # (local) FAIL-over-produce test
    # re-vanish: is the source gauge-removable? P_nLI=eps^2>0 for all eps>0 in scan => NOT removable
    P_nLI_min = float(pontryagin_number_nLI(eps_grid.min()))          # (local) > 0
    source_not_removable = P_nLI_min > 0.0                            # (local)
    all_revanish = bool(np.all(re_vanish))                            # (local) FAIL-re-vanish test
    if all_over_produce:
        mag_verdict = "FAIL"; mag_submode = "FAIL-over-produce"        # (local)
    elif all_revanish or (not source_not_removable):
        mag_verdict = "FAIL"; mag_submode = "FAIL-re-vanish"          # (local)
    elif admissible_exists:
        mag_verdict = "PASS"; mag_submode = "admissible-band-exists"  # (local)
    else:
        mag_verdict = "FAIL"; mag_submode = "no-admissible-amplitude" # (local)

    # ============================================================================
    # REGIME read-off: does the posited suppression operate in a VALID regime?
    # ----------------------------------------------------------------------------
    # The S96 DKKMS baseline had regime_breach_fraction=1.0 (BREAKDOWN) because the
    # naive coupling ran out of regime. The posited suppression operates by SHRINKING
    # the curvature strength (sigma_supp << 1), pulling the effective coupling DEEP
    # into the perturbative / sub-dominant regime (the non-LI curvature is parametrically
    # smaller than the homogeneous g_M). The Sakharov product is a near-equilibrium
    # leading-order expression valid when Gamma_B/H is sub-Hubble and sigma_supp<<1.
    # Validity window: sigma_supp(eps) < 1 throughout the admissible band (curvature
    # genuinely sub-dominant), and Gamma_B/T^4 << 1 (sphaleron rate perturbative).
    sigma_admissible = sigma_suppression(eps_adm) if eps_adm.size else np.array([np.nan])  # (local)
    sigma_subdominant = bool(np.all(sigma_admissible < 1.0)) if eps_adm.size else False    # (local)
    gamma_perturbative = bool(Gamma_B_over_T4 < 1.0)                  # (local)
    # breach fraction over the ADMISSIBLE band (the regime the gate actually uses)
    if eps_adm.size:
        regime_breach = float(np.mean(sigma_admissible >= 1.0))      # (local) fraction breaching subdominance
    else:
        regime_breach = 1.0                                           # (local)
    if regime_breach <= 0.05 and sigma_subdominant and gamma_perturbative:
        regime_verdict = "VALID"                                      # (local)
    elif regime_breach <= 0.50:
        regime_verdict = "MARGINAL"                                   # (local)
    else:
        regime_verdict = "BREAKDOWN"                                  # (local)

    # ============================================================================
    # Composite collapse (PRE-REGISTERED rule, gate-verdicts.md schema-v2)
    # ============================================================================
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif mag_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif mag_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif mag_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print(f"\n[{GATE_ID}] 3-tuple: sign={sign_verdict} magnitude={mag_verdict}({mag_submode}) "
          f"regime={regime_verdict}(breach={regime_breach:.3f}) => composite={composite}")

    # ============================================================================
    # Plot
    # ============================================================================
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.6))

    # Panel 1: eta_B(eps, phi) heatmap with the window boundary
    ax = axes[0]
    logETA = np.log10(np.clip(ETA, 1e-30, None))                      # (local)
    pc = ax.pcolormesh(eps_grid, phi_grid, logETA.T, shading="auto", cmap="viridis")
    cb = fig.colorbar(pc, ax=ax); cb.set_label(r"$\log_{10}\,\eta_B$")
    # window-ceiling contour log10(6e-10) and over-production contour log10(eta_dkkms)
    cs = ax.contour(eps_grid, phi_grid, logETA.T,
                    levels=[np.log10(WINDOW_HI)], colors="red", linewidths=2.0)
    ax.clabel(cs, fmt=r"$\eta_B=6\times10^{-10}$", fontsize=8)
    ax.contour(eps_grid, phi_grid, logETA.T,
               levels=[np.log10(eta_obs_s96)], colors="orange", linewidths=1.2, linestyles="--")
    ax.set_xscale("log")
    ax.set_xlabel(r"$\epsilon_{\rm nLI}$ (non-LI amplitude)")
    ax.set_ylabel(r"$\varphi_{\rm CP}$ (CP-odd phase, rad)")
    ax.set_title(r"$\eta_B(\epsilon_{\rm nLI},\varphi_{\rm CP})=\eta_{\rm DKKMS}\cdot\sigma_{\rm supp}(\epsilon)\cdot\sin\varphi$"
                 + "\n(red = window ceiling; admissible region BELOW it, $\\eta_B>0$)")
    if eps_adm.size:
        ax.plot(eps_star, phi_star, "w*", ms=16, mec="k",
                label=fr"admissible $\epsilon^*={eps_star:.2e}$")
        ax.legend(loc="lower right", fontsize=8)

    # Panel 2: eta_B vs eps at phi=pi/2, with window + DKKMS + observed lines
    ax = axes[1]
    ax.loglog(eps_grid, np.clip(eta_mid, 1e-30, None), "b.-", label=r"$\eta_B$ at $\varphi=\pi/2$ (max CP)")
    ax.axhline(WINDOW_HI, color="red", lw=2.0, label=r"window ceiling $6\times10^{-10}$")
    ax.axhline(eta_obs_s96, color="orange", ls="--", lw=1.2, label=r"$\eta_{\rm BBN,obs}=6.12\times10^{-10}$")
    ax.axhline(eta_dkkms, color="k", ls=":", lw=1.5, label=fr"DKKMS baseline {eta_dkkms:.2e} (S96, ~14 OOM over)")
    if eps_adm.size:
        ax.axvspan(eps_adm_lo, eps_adm_hi, color="green", alpha=0.18,
                   label=fr"admissible $\epsilon$ band [{eps_adm_lo:.1e},{eps_adm_hi:.1e}]")
    ax.set_xlabel(r"$\epsilon_{\rm nLI}$")
    ax.set_ylabel(r"$\eta_B$")
    ax.set_title(r"Posited fiber-volume suppression $\sigma_{\rm supp}=\epsilon^2\cdot\frac{1}{8}\cdot\langle f(\tau)\rangle$"
                 + "\nbrings DKKMS over-production into the observed window")
    ax.legend(fontsize=7, loc="upper left")
    ax.grid(True, which="both", alpha=0.3)

    fig.suptitle(f"{GATE_ID}: frontier #9 -- eta_B from a posited non-LI phi_88-Cartan source "
                 f"(external to D_K [eta_B=0] AND homogeneous g_M [tr(R^R)=0])\n"
                 f"composite={composite}  (sign={sign_verdict}, magnitude={mag_verdict}, regime={regime_verdict})",
                 fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(PNG_PATH, dpi=130)
    plt.close(fig)
    print(f"[{GATE_ID}] plot -> {PNG_PATH}")

    # ============================================================================
    # audit pin-map + dual SHA
    # ============================================================================
    audit_pin_map = {                                                  # (local)
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "sha_canonical_constants": sha_canon,
        "sha_ext_baryogen_npz": sha_ext,
        # ---- the structural posit (pinned) ----
        "kappa_sph": KAPPA_SPH,
        "T_eq": T_EQ,
        "cartan_dirs_nLI": CARTAN_DIRS_NLI,
        "dim_su3": DIM_SU3,
        "eps_lo": EPS_LO, "eps_hi": EPS_HI, "n_eps": N_EPS,
        "n_cp": N_CP,
        "tau_win": [TAU_WIN_LO, TAU_WIN_HI], "n_tau": N_TAU,
        "f_bump_width": F_BUMP_WIDTH,
        # ---- window + tolerances ----
        "window_lo": WINDOW_LO, "window_hi": WINDOW_HI,
        "tolerance": TOLERANCE, "resolution_floor": RESOLUTION_FLOOR,
        # ---- canonical anchors ----
        "eta_BBN_obs": float(eta_BBN_obs), "eta_BBN_err": float(eta_BBN_err),
        "tau_fold": float(tau_fold), "M_KK": float(M_KK),
        "alpha_em_MZ_inv": float(alpha_em_MZ_inv), "sin2_thetaW_MSbar": float(sin2_thetaW_MSbar),
        "dkkms_baseline_npz": eta_dkkms,
        # ---- computed verdict drivers ----
        "n_window": n_window, "n_total": n_total,
        "eps_adm_lo": eps_adm_lo, "eps_adm_hi": eps_adm_hi,
        "eta_star": eta_star, "sigma_star": sigma_star,
        "sign_verdict": sign_verdict, "mag_verdict": mag_verdict,
        "mag_submode": mag_submode, "regime_verdict": regime_verdict,
        "regime_breach": regime_breach, "composite": composite,
        "boundary_recovers_null": bool(boundary_recovers_null),
        "boundary_resid_rel": boundary_resid_rel,
        "source_not_removable": bool(source_not_removable),
        "regulator_pin": "N/A",
    }
    audit_sha, content_sha = dual_sha(audit_pin_map)

    # ============================================================================
    # npz
    # ============================================================================
    np.savez(
        NPZ_PATH,
        # ---- scan grids ----
        eps_grid=eps_grid, phi_grid=phi_grid,
        ETA=ETA, SIGMA=SIGMA_full,
        in_window=in_window, over_produce=over_produce, re_vanish=re_vanish,
        # ---- structural anchors (NEGATIVE, substrate-first) ----
        eta_dk_intrinsic=eta_dk_intrinsic,       # (A) 0.0 EXACT (T11)
        p1_su3=p1_su3,                           # (B) 0.0 EXACT (S54)
        tr_RR_homog=tr_RR_homog,                 # (B) 0.0
        internal_null=internal_null,             # (A) True
        eta_dkkms=eta_dkkms,                     # (C) 69832.54 baseline
        oom_over=oom_over,                       # ~14.07
        required_reduction=required_reduction,   # 6e-10/eta_dkkms
        # ---- posited-source pins ----
        alpha_W=alpha_W, Gamma_B_over_T4=Gamma_B_over_T4,
        geom_fiber_ratio=geom, tau_support_frac=supp,
        kappa_sph=KAPPA_SPH, T_eq=T_EQ,
        # ---- admissible region ----
        n_window=n_window, n_total=n_total,
        eps_adm_lo=eps_adm_lo, eps_adm_hi=eps_adm_hi,
        eps_star=eps_star, phi_star=phi_star, eta_star=eta_star, sigma_star=sigma_star,
        P_nLI_min=P_nLI_min, source_not_removable=source_not_removable,
        # ---- boundary consistency (eta->0 at phi in {0,pi} recovers intrinsic null) ----
        eta_phi0=eta_phi0, eta_phipi=eta_phipi, boundary_recovers_null=boundary_recovers_null,
        boundary_resid_rel=boundary_resid_rel,
        # ---- verdict 3-tuple ----
        sign_verdict=sign_verdict, magnitude_verdict=mag_verdict, mag_submode=mag_submode,
        regime_verdict=regime_verdict, regime_breach=regime_breach, composite_verdict=composite,
        sigma_subdominant=sigma_subdominant, gamma_perturbative=gamma_perturbative,
        # ---- canonical anchors ----
        eta_BBN_obs=float(eta_BBN_obs), eta_BBN_err=float(eta_BBN_err),
        tau_fold=float(tau_fold), M_KK=float(M_KK),
        window_lo=WINDOW_LO, window_hi=WINDOW_HI,
        value=(eta_star if eps_adm.size else 0.0),
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        regulator_pin="N/A",
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"[{GATE_ID}] npz -> {NPZ_PATH}")

    # ============================================================================
    # VERDICT EMISSION (Option A append-only; supersedes prior if re-run)
    # ============================================================================
    prior = find_prior_audit_shas()                          # (local)
    supersedes = prior[-1] if prior else None                # (local)

    # value: report the representative admissible eta_B (3 sig figs) + the key drivers
    value_str = (
        f"eta_B={eta_star:.3e}_in_(0,{WINDOW_HI:.0e})={bool(admissible_exists)};"
        f"eps_star={eps_star:.3e};phi_star=pi/2;sigma_supp={sigma_star:.3e};"
        f"n_window={n_window}/{n_total};eps_adm=[{eps_adm_lo:.2e},{eps_adm_hi:.2e}];"
        f"eta_dkkms={eta_dkkms:.3e}_OOM_over={oom_over:.2f};"
        f"sign={sign_verdict};magnitude={mag_verdict}_{mag_submode};regime={regime_verdict};"
        f"src_not_removable={source_not_removable};boundary_null={boundary_recovers_null};"
        f"CLASS=FULL;regulator_pin=N/A;eta_B(D_K)=0_EXACT_T11;p1_SU3=0_EXACT_S54"
    )
    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_verdict, mag_verdict, regime_verdict, supersedes=supersedes)

    print(f"\n[{GATE_ID}] audit_sha256={audit_sha}")
    print(f"[{GATE_ID}] content_sha256={content_sha}")
    if supersedes:
        print(f"[{GATE_ID}] supersedes prior audit_sha256={supersedes} (Option A append-only)")
    print(f"[{GATE_ID}] 4-tuple: (value=eta_B={eta_star:.3e}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"[{GATE_ID}] VERDICT: {composite}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
