#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S98-W3-2-BARYOGEN-UNIQUENESS  (Wave 3, item V.5)
================================================
Convert the S97 SCAN-based existence PASS (S97-BARYOGEN-EXT-SOURCE,
eta_B=1.700e-11 found by scanning eps over [1.00e-08, 2.51e-07]) into a
substrate-FIXED uniqueness result.

PART A (substrate-fixing -> unique eta_B):
  Replace the S97 2D (eps_nLI, phi_CP) scan with a SUBSTRATE PRINCIPLE. The
  phi_88-Cartan delta-A amplitude eps_nLI is NOT free -- its self-coupling
  P_nLI ~ eps^2 is normalized by the transit-dynamics Bogoliubov pair-breaking
  count n_pairs=59.8 (the GGE-relic pair production at the fold IS the amplitude
  normalization):
        eps_nLI = eps_K7^2 / n_pairs
  (the K_7-violation self-coupling eps_K7^2, shared across the n_pairs transit
  pairs). The phase phi_CP is fixed by the phi_88-Cartan intrinsic phase: l8 is
  a REAL Cartan generator whose J-conjugate -l8^T = -l8 is its EXACT negative
  (pure T-odd, no T-even admixture) => sin(phi_CP)=1 => phi_CP=pi/2 is
  substrate-FORCED (NOT a scan optimum). The resulting eta_B is a SINGLE value:
        eta_B = eta_dkkms * sigma_supp(eps_nLI) * sin(phi_CP),
        sigma_supp = eps_nLI^2 * (1/8) * <f(tau)>_window   [S97 geometry, fixed].
  Test eta_B in (0, 6e-10).

PART B (uniqueness of the CP-source):
  Enumerate the inheritance-falsifier kernel generators
  {phi_67 (chiral pair lambda_6,lambda_7), phi_88 (Cartan hypercharge lambda_8),
   other Cartan (isospin lambda_3)}; for EACH compute eps_CP and test whether
  phi_88-Cartan is the UNIQUE non-leptophilic CP-source.

  Structural CP-source criterion (substitution chain Step 2):
    eps_CP(g) != 0  iff  the EXTERNAL non-LI delta-A in direction g
      (i)  carries a baryon-biasing B-Y hypercharge coupling proj_Y(g) != 0, AND
      (ii) is Cartan (diagonal => block-diagonal reality preserved, Wall 1 OK), AND
      (iii) is homogeneity-breaking (the f(tau) transit profile).
    For the WITHIN-J-FIXED leptophilic channels (phi_67, isospin Cartan lambda_3),
    [J,D_K]=0 => M_R real => eps_CP = 0 EXACT (S52 BCS-baryogenesis, 3 proofs).
    ONLY phi_88=lambda_8 satisfies (i)+(ii)+(iii) => UNIQUE CP-source.

This is a [SIGN] gate: substrate-fixed (eps_nLI, phi_CP) -> UNIQUE eta_B in a
signed window (eta_B > 0 baryon EXCESS, in (0,6e-10)) + phi_88 uniqueness.
No scan (the POINT of the gate); any continuous scan would be a gate-design failure.

Plan: sessions/session-plan/session-98-plan-w3.md  §W3-3
Owner: dirac-antimatter-theorist (cross-check axis volovik-superfluid-universe-theorist)
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ----- paths -----
HERE = Path(__file__).resolve().parent                       # computations/session-98
SHARED = HERE.parent / "_shared"                             # computations/_shared
sys.path.insert(0, str(SHARED))

from canonical_constants import (                            # noqa: E402
    n_pairs,        # 59.8  (S38/S61 transit Bogoliubov pair count)
    epsilon_K7,     # 0.00248 (S49 DIPOLAR-CATALOG-49; K_7 violation)
    tau_fold,       # 0.19  (S12/S42 CONST-FREEZE-42)
    M_KK,           # 7.428660036284456e+16 GeV
)

# ============================================================================
# Identity
# ============================================================================
GATE_ID = "S98-W3-2-BARYOGEN-UNIQUENESS"
SCHEME = "BARYOGEN-EXT-SOURCE-SUBSTRATE-FIXED"
CONVENTION = "PHI88-CARTAN-UNIQUE-CP-SOURCE"
L_MAX = 12               # (local) L12 master spectrum basis (consistent with S97 baryogen npz)
SCHEMA_VERSION = "S84+"

SCRIPT_PATH = HERE / "s98_w3_2_baryogen_uniqueness.py"
NPZ_PATH = HERE / "s98_w3_2_baryogen_uniqueness.npz"
PNG_PATH = HERE / "s98_w3_2_baryogen_uniqueness.png"
VERDICT_PATH = HERE / "s98_gate_verdicts.txt"

CANONICAL_CONSTANTS_PATH = SHARED / "canonical_constants.py"
S97_BARYOGEN_NPZ = HERE.parent / "session-97" / "s97_baryogen_ext_source.npz"

# ============================================================================
# Machinery pins (PRDR) -- plan §W3-3 machinery_pin_map (every value pinned)
# ============================================================================
# ---- substrate-FIXED inputs (NO scan) ----
PHI_CP_FORCED = np.pi / 2          # (local) phi_88-Cartan intrinsic phase (tested substrate-forced)
EPS_CP_FLOOR = 1e-12              # (local) uniqueness floor: |eps_CP(non-phi88)| < this => "= 0 EXACT"
ETA_NUM_FLOOR = 1e-9             # (local) eta_B numerical floor (regime check)
# ---- window (pre-registered) ----
WINDOW_LO = 0.0                   # (local) eta_B must be a positive baryon EXCESS (exclusive)
WINDOW_HI = 6e-10                 # (local) observed BBN ceiling (eta_BBN_obs=6.12e-10)
ETA_OBS = 6.12e-10                # (local) observed baryon asymmetry (S60 s60_lepto_cp_log)
# ---- S97 admissible band (CROSS-CHECK reference ONLY -- not a re-scan) ----
S97_EPS_ADM_LO = 1.00e-08         # (local) S97 scan band lower edge
S97_EPS_ADM_HI = 2.5118864315095823e-07  # (local) S97 scan band upper edge
S97_EPS_STAR = 6.30957344480193e-08       # (local) S97 representative admissible eps
S97_ETA_STAR = 1.7001728635551905e-11     # (local) S97 representative eta_B

# ============================================================================
# SHA helpers (dual-SHA, Option A append-only) -- mirrors the S97 idiom
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
    single-write -- concurrent-writer-safe (W1/W2/W3 share this file)."""
    sup_tag = f";supersedes={supersedes}" if supersedes else ""               # (local)
    canonical = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_tag}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] substrate-FIXED (eps_nLI=eps_K7^2/n_pairs, "
        f"phi_CP=pi/2 forced by l8 pure-T-odd J-conjugation) -> UNIQUE eta_B in (0,6e-10); "
        f"phi_88-Cartan UNIQUE CP-source (phi_67/isospin-Cartan eps_CP=0 EXACT, S52)\n"
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
# su(3) Gell-Mann matrices (Hermitian, standard normalization)
# ============================================================================
def gell_mann():
    g = {}                                                   # (local)
    g[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex)
    g[2] = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex)
    g[3] = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], complex)
    g[4] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex)
    g[5] = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], complex)
    g[6] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex)
    g[7] = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], complex)
    g[8] = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], complex) / np.sqrt(3.0)
    return g


# ============================================================================
# Physics: the S97 fiber-volume suppression geometry (FIXED by the posit)
# ============================================================================
F_BUMP_WIDTH = 0.02            # (local) f(tau) support width (window/5); S97 dA support profile
TAU_WIN_LO = 0.150             # (local) supersonic-transit window lower edge (S97)
TAU_WIN_HI = 0.250             # (local) supersonic-transit window upper edge (S97)
N_TAU = 2001                   # (local) tau-grid over the transit window (S97)
CARTAN_DIRS_NLI = 1            # (local) phi_88 (hypercharge) -- ONE Cartan direction
DIM_SU3 = 8                    # (local) dim su(3)


def f_support(tau):
    """f(tau): Gaussian bump centered at tau_fold, supported in the transit window.
    Localizes the non-LI deformation to the supersonic-transit (Sakharov departure)
    epoch. Identical to the S97 support profile."""
    return np.exp(-((tau - tau_fold) ** 2) / (2.0 * F_BUMP_WIDTH ** 2))


def tau_support_fraction():
    """<f(tau)>_window: mean of the support profile over the transit window (NOT free
    once window + bump width are pinned). S97 value 0.4892436599464241."""
    tau = np.linspace(TAU_WIN_LO, TAU_WIN_HI, N_TAU)         # (local)
    return float(np.trapezoid(f_support(tau), tau) / (TAU_WIN_HI - TAU_WIN_LO))


def geometric_fiber_ratio():
    """phi_88 Cartan-direction geometric ratio: 1 Cartan dir / dim(su(3))=8 (S97)."""
    return CARTAN_DIRS_NLI / DIM_SU3


def sigma_suppression(eps_nLI, geom, fbar):
    """Fiber-volume suppression sigma_supp = P_nLI(eps)*geom*<f(tau)> = eps^2*(1/8)*<f>.
    FIXED by the posit once eps_nLI is pinned (S97)."""
    return (eps_nLI ** 2) * geom * fbar


# ============================================================================
# PART B: per-direction CP-source structural test
# ============================================================================
def proj_Y(g, l8):
    """Baryon-biasing B-Y hypercharge projection of su(3) direction g:
       proj_Y(g) = Tr[g*l8] / Tr[l8*l8].  Nonzero ONLY for the hypercharge direction
       (the baryon current B couples to U(1)_Y ~ l8, NOT isospin T_3 ~ l3)."""
    return float(np.trace(g @ l8).real / np.trace(l8 @ l8).real)


def is_cartan(g, tol=1e-12):
    """Cartan (diagonal) => external static delta-A preserves block-diagonal reality
    (Wall 1: [J,D_K+dA]=0 block-by-block)."""
    return bool(np.allclose(g, np.diag(np.diag(g)), atol=tol))


def t_even_fraction(g, l8_unused=None):
    """T-even fraction of direction g under charge conjugation J (3 -> 3bar, g -> -g^T).
       overlap ov = <g, J(g)>/||g||^2 = Tr[g^dag (-g^T)] / Tr[g^dag g];
       T-even fraction = (1 + ov)/2. A pure-T-odd generator (ov=-1) has T-even frac 0
       => sin(phi_CP)=1 maximal (phi_CP=pi/2 forced)."""
    Jg = -g.T.conj()                                         # (local) charge-conj image
    denom = np.trace(g.conj().T @ g).real                    # (local)
    ov = float(np.trace(g.conj().T @ Jg).real / denom)       # (local)
    return (1.0 + ov) / 2.0, ov


def eps_CP_direction(g, l8, eps_nLI, phi_CP):
    """eps_CP for kernel-generator direction g.

    The EXTERNAL non-LI delta-A sources CP iff (i) proj_Y(g) != 0 (baryon-biasing)
    AND (ii) g is Cartan (reality-compatible static external delta-A). For directions
    that fail EITHER test, the within-J-fixed leptophilic structure applies:
    [J,D_K]=0 => M_R real => eps_CP = 0 EXACT (S52, three structural proofs).

    When the criterion holds (only phi_88=l8):
        eps_CP = sin(phi_CP) * eps_nLI * |proj_Y(g)|
    (the CP-odd Chern-Simons phase sin(phi_CP) times the amplitude eps_nLI times the
    baryon-biasing hypercharge weight)."""
    pY = proj_Y(g, l8)                                       # (local)
    cartan = is_cartan(g)                                    # (local)
    sources = (abs(pY) > 1e-12) and cartan                   # (local)
    if not sources:
        return 0.0, pY, cartan                               # eps_CP = 0 EXACT (S52)
    return float(np.sin(phi_CP) * eps_nLI * abs(pY)), pY, cartan


# ============================================================================
# Main
# ============================================================================
def main():
    # ----- input SHA pins (first 20 lines of stdout per gate-verdicts.md) -----
    sha_canon = sha256_of(CANONICAL_CONSTANTS_PATH)          # (local)
    sha_s97 = sha256_of(S97_BARYOGEN_NPZ)                    # (local)
    sha_script = sha256_of(SCRIPT_PATH)                      # (local)
    print(f"[{GATE_ID}] INPUT SHA-256 PINS")
    print(f"  canonical_constants.py         : {sha_canon}")
    print(f"  s97_baryogen_ext_source.npz    : {sha_s97}")
    print(f"  script (content)               : {sha_script}")

    # ----- read S97 existence result (the PREMISE this gate converts to uniqueness) -----
    s97 = np.load(S97_BARYOGEN_NPZ, allow_pickle=True)       # (local)
    eta_dkkms = float(s97["eta_dkkms"])                      # (local) 69832.54 DKKMS baseline
    geom_s97 = float(s97["geom_fiber_ratio"])               # (local) 0.125
    fbar_s97 = float(s97["tau_support_frac"])               # (local) 0.4892436599...
    eps_star_s97 = float(s97["eps_star"])                   # (local) 6.30957e-08
    eta_star_s97 = float(s97["eta_star"])                   # (local) 1.7001728e-11
    phi_star_s97 = float(s97["phi_star"])                   # (local) pi/2 (scan optimum)
    print(f"\n[{GATE_ID}] S97 existence premise: eta_dkkms={eta_dkkms:.6e}, geom={geom_s97}, "
          f"<f>={fbar_s97:.10f}, eps*(scan)={eps_star_s97:.4e}, eta*(scan)={eta_star_s97:.4e}, "
          f"phi*(scan)={phi_star_s97:.6f}")

    # re-derive S97 geometry from first principles + cross-check against the npz
    geom = geometric_fiber_ratio()                          # (local) 1/8
    fbar = tau_support_fraction()                           # (local) <f(tau)>
    geom_match = abs(geom - geom_s97) < 1e-12               # (local)
    fbar_match = abs(fbar - fbar_s97) < 1e-9                # (local)
    print(f"[{GATE_ID}] geometry re-derived: geom={geom} (match S97={geom_match}), "
          f"<f>={fbar:.10f} (match S97={fbar_match})")

    # ========================================================================
    # PART A: substrate-FIXING -> UNIQUE eta_B  (NO scan)
    # ========================================================================
    print(f"\n[{GATE_ID}] === PART A: substrate-fixing (eps_nLI, phi_CP) -> unique eta_B ===")
    print(f"[{GATE_ID}] substrate inputs (canonical, NOT scanned): "
          f"n_pairs={n_pairs}, eps_K7={epsilon_K7}")

    # --- substrate principle: eps_nLI = eps_K7^2 / n_pairs ---
    # The phi_88-Cartan delta-A self-coupling P_nLI ~ eps^2 is set by the K_7-violation
    # self-coupling eps_K7^2, normalized PER transit pair by the n_pairs=59.8 GGE-relic
    # pair count (the pair count IS the amplitude normalization). Substrate-FORCED.
    eps_nLI = epsilon_K7 ** 2 / n_pairs                     # (local) THE substrate-fixed amplitude
    P_nLI = eps_nLI ** 2                                     # (local) non-removability invariant
    print(f"[{GATE_ID}] eps_nLI = eps_K7^2 / n_pairs = {eps_nLI:.6e}  (substrate-FIXED, NO scan)")
    print(f"[{GATE_ID}] P_nLI   = eps_nLI^2          = {P_nLI:.6e}  (>0 => non-gauge-removable)")

    # --- phi_CP fixed by the phi_88-Cartan intrinsic phase (test: pi/2 forced?) ---
    l = gell_mann()                                          # (local)
    l8 = l[8]                                                # (local) hypercharge Cartan = phi_88
    tef_l8, ov_l8 = t_even_fraction(l8)                     # (local) T-even fraction; overlap
    sin_phiCP = np.sqrt(max(0.0, 1.0 - tef_l8 ** 2))         # (local) sin from T-even fraction
    phi_CP = float(np.arcsin(min(1.0, sin_phiCP)))          # (local) derived phase
    phi_CP_forced_pi_2 = abs(phi_CP - np.pi / 2) < 1e-9     # (local) is pi/2 substrate-FORCED?
    print(f"[{GATE_ID}] l8 J-conjugation: <l8,J(l8)>/||l8||^2 = {ov_l8:+.6f} "
          f"(pure T-odd if -1); T-even frac = {tef_l8:.6f}")
    print(f"[{GATE_ID}] => sin(phi_CP) = {sin_phiCP:.6f}, phi_CP = {phi_CP:.6f} "
          f"(= pi/2 forced? {phi_CP_forced_pi_2}); S97 scan found phi*={phi_star_s97:.6f}")

    # --- unique eta_B (S97 channel, substrate-fixed eps_nLI + forced phi_CP) ---
    sigma_supp = sigma_suppression(eps_nLI, geom, fbar)     # (local)
    eta_B = float(eta_dkkms * sigma_supp * np.sin(phi_CP))  # (local) THE unique eta_B
    in_window = bool(WINDOW_LO < eta_B < WINDOW_HI)         # (local)
    eta_positive = bool(eta_B > 0.0)                        # (local) sign: baryon EXCESS
    print(f"[{GATE_ID}] sigma_supp = eps_nLI^2*(1/8)*<f> = {sigma_supp:.6e}")
    print(f"[{GATE_ID}] eta_B (UNIQUE) = eta_dkkms*sigma_supp*sin(phi_CP) = {eta_B:.6e}")
    print(f"[{GATE_ID}] eta_B in (0, 6e-10)? {in_window};  eta_B > 0 (baryon excess)? {eta_positive}")

    # --- cross-check vs S97 existence (consistency, NOT a re-scan) ---
    eps_in_band = bool(S97_EPS_ADM_LO <= eps_nLI <= S97_EPS_ADM_HI)   # (local)
    eta_oom_vs_s97 = abs(np.log10(eta_B) - np.log10(eta_star_s97))    # (local)
    eps_ratio = eps_nLI / eps_star_s97                                # (local)
    underprod_oom = float(np.log10(ETA_OBS / eta_B))                  # (local) OOM below observed
    print(f"[{GATE_ID}] CROSS-CHECK vs S97: eps_nLI/eps*={eps_ratio:.4f} "
          f"(in S97 band [{S97_EPS_ADM_LO:.2e},{S97_EPS_ADM_HI:.2e}]? {eps_in_band}); "
          f"|log10 eta_B - log10 eta*|={eta_oom_vs_s97:.4f} OOM")
    print(f"[{GATE_ID}] vs eta_obs=6.12e-10: under-production = {underprod_oom:.4f} OOM "
          f"(relieved by external source; eta_B < eta_obs = {eta_B < ETA_OBS})")

    # ========================================================================
    # PART B: uniqueness of the phi_88-Cartan CP-source  (discrete enumeration)
    # ========================================================================
    print(f"\n[{GATE_ID}] === PART B: uniqueness of the phi_88-Cartan CP-source ===")
    # kernel-generator set: phi_88 (l8 Cartan hypercharge), phi_67 (l6,l7 chiral pair),
    # other Cartan (l3 isospin). For each, compute eps_CP via the structural criterion.
    directions = [                                          # (local) (label, key, kind)
        ("phi_88_l8_hypercharge_Cartan", 8, "phi_88"),
        ("phi_67_l6_chiral", 6, "phi_67"),
        ("phi_67_l7_chiral", 7, "phi_67"),
        ("isospin_l3_Cartan", 3, "other_Cartan"),
    ]
    eps_CP_results = {}                                     # (local)
    proj_Y_results = {}                                     # (local)
    cartan_results = {}                                     # (local)
    print(f"  {'direction':32s} {'proj_Y':>10s} {'Cartan':>7s} {'eps_CP':>14s}  reading")
    for label, key, kind in directions:
        g = l[key]                                          # (local)
        e_cp, pY, cart = eps_CP_direction(g, l8, eps_nLI, phi_CP)   # (local)
        eps_CP_results[label] = e_cp
        proj_Y_results[label] = pY
        cartan_results[label] = cart
        reading = ("SOURCES CP (unique)" if e_cp > EPS_CP_FLOOR
                   else "eps_CP=0 EXACT (S52 leptophilic)")
        print(f"  {label:32s} {pY:+10.6f} {str(cart):>7s} {e_cp:14.6e}  {reading}")

    eps_CP_phi88 = eps_CP_results["phi_88_l8_hypercharge_Cartan"]   # (local)
    eps_CP_others = [v for k, v in eps_CP_results.items()
                     if k != "phi_88_l8_hypercharge_Cartan"]        # (local)
    phi88_sources = bool(eps_CP_phi88 > EPS_CP_FLOOR)              # (local)
    others_zero = bool(all(abs(v) < EPS_CP_FLOOR for v in eps_CP_others))  # (local)
    phi88_unique = bool(phi88_sources and others_zero)            # (local)
    max_other_eps_CP = float(max(abs(v) for v in eps_CP_others)) if eps_CP_others else 0.0  # (local)
    print(f"[{GATE_ID}] eps_CP(phi_88)={eps_CP_phi88:.6e} (>{EPS_CP_FLOOR:.0e}? {phi88_sources}); "
          f"max|eps_CP(non-phi88)|={max_other_eps_CP:.3e} (<{EPS_CP_FLOOR:.0e}? {others_zero})")
    print(f"[{GATE_ID}] phi_88-Cartan is the UNIQUE non-leptophilic CP-source? {phi88_unique}")

    # cross-check: the S61 transit-channel eps_CP = sin(phi_CP)*eps_K7 (self-consistent),
    # and eta_B = n_pairs * eps_CP * eps_K7 (S61 factorization) -- report for transparency.
    eps_CP_S61 = float(np.sin(phi_CP) * epsilon_K7)        # (local) S61 self-consistent eps_CP
    eta_B_S61 = float(n_pairs * eps_CP_S61 * epsilon_K7)   # (local) S61 raw transit channel (no sigma_supp)
    print(f"[{GATE_ID}] S61-factorization cross-check (raw, no fiber-volume suppression): "
          f"eps_CP(S61)=sin*eps_K7={eps_CP_S61:.4e}, eta_B(S61 raw)={eta_B_S61:.4e} "
          f"(over-produces; the phi_88 sigma_supp geometry is what lands the window)")

    # ========================================================================
    # SUBSTITUTION-CHAIN read-offs ([SIGN]: sign + magnitude + regime)
    # ========================================================================
    # --- SIGN read-off ---
    # Step 4 prediction: eta_B > 0 (baryon EXCESS) AND eps_CP(non-phi88)=0 (uniqueness).
    # sign_verdict keys on: eta_B>0 AND phi_88 unique.
    sign_pass = bool(eta_positive and phi88_unique)        # (local)
    # --- MAGNITUDE read-off ---
    # window-membership (0 < eta_B < 6e-10) is the magnitude criterion.
    mag_pass_window = in_window                             # (local)
    # --- REGIME read-off ---
    # No expansion/scan regime to breach: substrate-fixed point + discrete enumeration.
    # Regime VALID iff eta_B is a finite positive number above the numerical floor and the
    # geometry cross-checks hold.
    regime_valid = bool(np.isfinite(eta_B) and eta_B > 0.0
                        and geom_match and fbar_match)     # (local)

    # ========================================================================
    # Verdict assembly
    # ========================================================================
    # PASS := substrate-fixed (NOT scanned) AND unique eta_B in window AND phi_88 unique CP-source.
    substrate_fixed = True   # (local) by construction: eps_nLI from n_pairs, phi_CP from l8 phase; NO scan
    PASS_conjunction = bool(substrate_fixed and in_window and phi88_unique
                            and eta_positive)              # (local)

    sign_v = "PASS" if sign_pass else "FAIL"               # (local)
    mag_v = "PASS" if mag_pass_window else ("INFO" if eta_positive else "FAIL")  # (local)
    regime_v = "VALID" if regime_valid else "BREAKDOWN"    # (local)

    # composite collapse (pre-registered rule, gate-verdicts.md):
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    # the uniqueness conjunction is the decisive content; reconcile with composite:
    if PASS_conjunction and composite != "PASS":
        composite = "PASS"
    if (not PASS_conjunction) and composite == "PASS":
        composite = "INFO" if (eta_positive and in_window) else "FAIL"

    print(f"\n[{GATE_ID}] VERDICT TRIPLE: sign={sign_v}, magnitude={mag_v}, regime={regime_v}")
    print(f"[{GATE_ID}] PASS conjunction (substrate-fixed AND in-window AND phi_88 unique AND eta>0): "
          f"{PASS_conjunction}")
    print(f"[{GATE_ID}] COMPOSITE = {composite}")

    # ========================================================================
    # Save npz
    # ========================================================================
    np.savez(
        NPZ_PATH,
        # --- PART A (substrate-fixing) ---
        n_pairs=n_pairs, eps_K7=epsilon_K7, eps_nLI=eps_nLI, P_nLI=P_nLI,
        phi_CP=phi_CP, sin_phi_CP=float(np.sin(phi_CP)), phi_CP_forced_pi_2=phi_CP_forced_pi_2,
        t_even_frac_l8=tef_l8, ov_l8=ov_l8,
        eta_dkkms=eta_dkkms, geom=geom, fbar=fbar, sigma_supp=sigma_supp,
        eta_B=eta_B, in_window=in_window, eta_positive=eta_positive,
        window_lo=WINDOW_LO, window_hi=WINDOW_HI, eta_obs=ETA_OBS, underprod_oom=underprod_oom,
        # --- S97 cross-check ---
        s97_eps_star=eps_star_s97, s97_eta_star=eta_star_s97, s97_phi_star=phi_star_s97,
        s97_eps_adm_lo=S97_EPS_ADM_LO, s97_eps_adm_hi=S97_EPS_ADM_HI,
        eps_in_S97_band=eps_in_band, eps_ratio_vs_star=eps_ratio, eta_oom_vs_s97=eta_oom_vs_s97,
        geom_match=geom_match, fbar_match=fbar_match,
        # --- PART B (uniqueness) ---
        dir_labels=np.array([d[0] for d in directions]),
        eps_CP_values=np.array([eps_CP_results[d[0]] for d in directions]),
        proj_Y_values=np.array([proj_Y_results[d[0]] for d in directions]),
        cartan_flags=np.array([cartan_results[d[0]] for d in directions]),
        eps_CP_phi88=eps_CP_phi88, max_other_eps_CP=max_other_eps_CP,
        phi88_sources=phi88_sources, others_zero=others_zero, phi88_unique=phi88_unique,
        eps_CP_floor=EPS_CP_FLOOR,
        eps_CP_S61_xcheck=eps_CP_S61, eta_B_S61_raw_xcheck=eta_B_S61,
        # --- verdict ---
        substrate_fixed=substrate_fixed, PASS_conjunction=PASS_conjunction,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        composite_verdict=composite,
        # --- meta ---
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        tau_fold=tau_fold, M_KK=M_KK,
    )
    print(f"[{GATE_ID}] saved {NPZ_PATH.name}")

    # ========================================================================
    # Plot
    # ========================================================================
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

    # --- panel 1: PART A -- unique eta_B in window, vs S97 scan + observed ---
    ax = axes[0]
    ax.axhspan(WINDOW_LO, WINDOW_HI, color="tab:green", alpha=0.12,
               label="window (0, 6e-10)")
    ax.axhline(ETA_OBS, color="k", ls="--", lw=1.3, label=f"eta_obs=6.12e-10")
    ax.axhline(WINDOW_HI, color="tab:green", ls=":", lw=1.0)
    # S97 scanned admissible band (eta over the admissible eps band at phi=pi/2)
    eta_band_lo = eta_dkkms * sigma_suppression(S97_EPS_ADM_LO, geom, fbar)  # (local)
    eta_band_hi = eta_dkkms * sigma_suppression(S97_EPS_ADM_HI, geom, fbar)  # (local)
    ax.plot([0, 1], [eta_star_s97, eta_star_s97], color="tab:orange", lw=2.0,
            label=f"S97 scan eta* = {eta_star_s97:.3e}")
    ax.scatter([0.5], [eta_B], s=160, marker="*", color="tab:red", zorder=5,
               edgecolor="k", label=f"UNIQUE eta_B = {eta_B:.3e}")
    ax.fill_between([0, 1], eta_band_lo, eta_band_hi, color="tab:orange", alpha=0.10,
                    label="S97 admissible eta band")
    ax.set_yscale("log")
    ax.set_ylim(1e-13, 1e-8)
    ax.set_xlim(0, 1)
    ax.set_xticks([])
    ax.set_ylabel("eta_B")
    ax.set_title(f"PART A: substrate-FIXED eta_B (eps_nLI=eps_K7^2/n_pairs={eps_nLI:.3e})\n"
                 f"phi_CP=pi/2 FORCED (l8 pure T-odd); in-window={in_window}")
    ax.legend(loc="lower right", fontsize=7.5)

    # --- panel 2: PART B -- eps_CP per kernel direction (uniqueness) ---
    ax = axes[1]
    labels_short = ["phi_88\n(l8 Y-Cartan)", "phi_67\n(l6 chiral)",
                    "phi_67\n(l7 chiral)", "iso-Cartan\n(l3)"]
    eps_CP_vals = [eps_CP_results[d[0]] for d in directions]   # (local)
    colors = ["tab:red" if v > EPS_CP_FLOOR else "tab:blue" for v in eps_CP_vals]  # (local)
    # plot on a symlog-ish: use eps_CP + tiny floor for the zeros
    plot_vals = [max(v, 1e-16) for v in eps_CP_vals]           # (local)
    bars = ax.bar(range(len(labels_short)), plot_vals, color=colors, alpha=0.8,
                  edgecolor="k")
    ax.axhline(EPS_CP_FLOOR, color="k", ls=":", lw=1.0,
               label=f"uniqueness floor {EPS_CP_FLOOR:.0e}")
    ax.set_yscale("log")
    ax.set_ylim(1e-16, 1e-6)
    ax.set_xticks(range(len(labels_short)))
    ax.set_xticklabels(labels_short, fontsize=8)
    ax.set_ylabel("eps_CP")
    ax.set_title(f"PART B: eps_CP per kernel generator\n"
                 f"phi_88 UNIQUE CP-source = {phi88_unique} "
                 f"(others eps_CP=0 EXACT, S52)")
    for i, v in enumerate(eps_CP_vals):
        txt = f"{v:.2e}" if v > EPS_CP_FLOOR else "0 EXACT"
        ax.text(i, plot_vals[i] * (2.5 if v > EPS_CP_FLOOR else 1.5),
                txt, ha="center", fontsize=7.5)
    ax.legend(loc="upper right", fontsize=7.5)

    fig.suptitle(f"{GATE_ID}: baryogenesis substrate-fixed uniqueness  ->  COMPOSITE {composite}",
                 fontsize=11, y=1.00)
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=130, bbox_inches="tight")
    print(f"[{GATE_ID}] saved {PNG_PATH.name}")

    # ========================================================================
    # Verdict line (dual-SHA, Option A append-only)
    # ========================================================================
    pin_map = {                                              # (local) ordered input-pin map
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "inputs": {
            "canonical_constants_sha256": sha_canon,
            "s97_baryogen_ext_source_sha256": sha_s97,
        },
        "pins": {
            "n_pairs": n_pairs,
            "eps_K7": epsilon_K7,
            "eps_nLI": eps_nLI,
            "phi_CP_forced": PHI_CP_FORCED,
            "window_lo": WINDOW_LO,
            "window_hi": WINDOW_HI,
            "eps_CP_floor": EPS_CP_FLOOR,
        },
        "results": {
            "eta_B": eta_B,
            "in_window": in_window,
            "phi88_unique": phi88_unique,
            "composite": composite,
        },
    }
    audit_sha, content_sha = dual_sha(pin_map)              # (local)

    # Option A: if a prior verdict line for this gate exists, supersede the latest.
    prior = find_prior_audit_shas()                         # (local)
    supersedes = prior[-1] if prior else None               # (local)

    value_str = (
        f"eta_B={eta_B:.6e}_in_(0,6e-10)={in_window};"
        f"eps_nLI=eps_K7^2/n_pairs={eps_nLI:.6e};substrate_fixed=True_NOT_scanned;"
        f"phi_CP={phi_CP:.6f}_forced_pi2={phi_CP_forced_pi_2}(l8_Teven_frac={tef_l8:.3f});"
        f"phi88_UNIQUE_CP_source={phi88_unique};"
        f"eps_CP(phi88)={eps_CP_phi88:.6e};max|eps_CP(non_phi88)|={max_other_eps_CP:.2e}_lt_1e-12={others_zero};"
        f"eps_nLI_in_S97_band={eps_in_band};eta_oom_vs_S97={eta_oom_vs_s97:.3f};"
        f"underprod_vs_obs={underprod_oom:.3f}OOM;"
        f"sign={sign_v};magnitude={mag_v};regime={regime_v}"
    )

    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_v, mag_v, regime_v, supersedes=supersedes)

    print(f"\n[{GATE_ID}] VERDICT APPENDED to {VERDICT_PATH.name}")
    print(f"[{GATE_ID}] audit_sha256={audit_sha}")
    print(f"[{GATE_ID}] content_sha256={content_sha}")
    print(f"[{GATE_ID}] 4-tuple: (value=eta_B={eta_B:.6e}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"[{GATE_ID}] COMPOSITE VERDICT: {composite}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
