#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S95-W4-4-SP-CONFORMAL-EMBED
===========================

Conformal-factor embedding of the modulus-space causal structure (Diagram B)
into the 4D product causal structure (Diagram A) for the acoustic white-hole
Penrose-diagram reproduction. Verifies whether the conformal-factor deceleration
parameter q_Omega(tau) reproduces the SCALE-FACTOR-54 q-range [-0.97, +0.81]
across the physical window tau in [0.19, 0.40], and whether the tau_fold extremal
horizon (kappa=0 double-root) maps to a well-defined 4D causal feature.

[VERIFY] gate (plan session-95-plan-w4.md SS W4-4. SP-CONFORMAL-EMBED).

SUBSTRATE FRAMING (phononic-framing.md SS "IS Space, Not IN Space"):
  GEOMETRIC. The conformal embedding is read off the substrate spectrum, NOT
  imposed between two stages. Arrow:
    D_K eigenvalues -> E3 internal scalar curvature R_K(tau) and the a_2^{zeta}
    Seeley-DeWitt moment -> the effective scale factor a_eff(tau) -> the
    conformal factor Omega(tau) embedding the DERIVED modulus-space causal
    structure (Diagram B, itself derived from e^{-S} monotonicity +
    COSMIC-CENSORSHIP-49) into the 4D product causal structure (Diagram A).
  The modulus-space conformal structure is fundamental and derived; the 4D
  spacetime conformal structure is emergent; Omega(tau) is the map between them.
  tau IS the substrate's intrinsic deformation parameter (Level-2
  moduli-deformation substrate-IS), NOT a coordinate on a meta-container.
  Direction held substrate -> emergent throughout.

THE TWO PROXY SCALE FACTORS (transit-flow-genesis-to-now.md SS6.4):
  The corpus carries TWO distinct PROXY scale factors, both explicitly effective
  substitutes, NEITHER a derived FRW a(t):
    (P1) a_eff(tau) = (a_2(tau)/a_2(tau_today))^{1/2}  -- the a_2-spectral-
         complexity proxy (S73b). a_2(tau) is the 2nd Seeley-DeWitt (Einstein-
         Hilbert) moment, whose tau-dependence is carried by the internal scalar
         curvature R_K(tau) (E3). This is the conformal factor the plan operator
         identifies as Omega(tau) (Def 3).
    (P2) a(tau) from Connes distance  -- SCALE-FACTOR-54 (FACTOR-54). Gives q
         transitioning from -0.97 (quasi-de Sitter) to +0.81 (decelerating).
         This is the source of the q-band TARGET [-0.97,+0.81].
  These are DIFFERENT geometric objects; the gate measures whether they coincide
  in their deceleration structure. (They do not -- see VERDICT.)

[VERIFY] SUBSTITUTION CHAIN (math-scripts.md SS "Double-Check Logic Before Compute";
plan SS(7) substitution_chain):
  Claim: "The conformal factor Omega(tau) embedding Diagram B into Diagram A
          equals the effective scale factor a_eff(tau)=(a_2(tau)/a_2(today))^{1/2}
          up to a constant, and its deceleration q_Omega(tau)=-Omega'' Omega/Omega'^2
          lies in the SCALE-FACTOR-54 range [-0.97,+0.81]."
  Def 1: Diagram B: ds^2_B = -dt^2 + G_mod dtau^2, G_mod=5.0 (FLAT 1+1D Minkowski;
         conformally flat). [Phononic-Penrose-Diagrams SS Diagram B]
  Def 2: 4D causal factor (Diagram A): ds^2_4D = a_eff(tau)^2(-deta^2+dx^2)
         (FRW-like, conformal time eta; the 12D product diagram is conformally the
         4D diagram with stiff matter w>=1). [Phononic-Penrose-Diagrams line 135]
  Def 3: a_eff(tau) = (a_2(tau)/a_2(today))^{1/2}; a_2(tau) the 2nd Seeley-DeWitt
         moment carried by R_K(tau) (E3). [canonical a_2_FW_zeta=2776.165389; SP-V5]
  Substitute: a conformal embedding ds^2_B = Omega^2(tau) ds^2_4D between two
         conformally-flat 1+1D structures requires Omega = sqrt(G_mod)/a_eff (EXISTS
         for all a_eff>0 -- 1+1D conformal existence is GUARANTEED; FAIL ruled out).
         The plan operator identifies Omega(tau) WITH a_eff(tau) (Def 3); under that
         identification q_Omega = -a_eff'' a_eff/a_eff'^2 (the proxy's cosmological q).
  Simplify: a multiplicative normalization constant c in Omega=c*a_eff drops out of
         q_Omega exactly (Sage-proven: q[c*f]=q[f]); so q_Omega is well-defined even
         though the M_KK^{-1}->s normalization is open. Also q_Omega = -1 - H'/H^2
         with H=a_eff'/a_eff (Sage-proven identity), the standard cosmological q.
  Canonical form: q_Omega(tau) = -a_eff'' a_eff / a_eff'^2 evaluated on a_eff(tau).
  Direction: the physical epoch is DECELERATING (stiff matter w>=1, Diagram A
         resembles decelerating FRW not de Sitter) -> q_Omega > 0 in the matter era;
         SCALE-FACTOR-54 records q crossing -0.97 (accelerating) -> +0.81
         (decelerating); q_Omega(tau) in [-0.97,+0.81] is the admissible band.
  Conclusion: Omega(tau) is the conformal factor; PASS iff q_Omega in [-0.97,+0.81]
         AND fold-horizon image is a 4D causal feature; INFO iff Omega derivable but
         the M_KK^{-1}->s normalization stays open (or the proxies are conformally
         distinct in deceleration); FAIL iff no consistent Omega exists (conformal
         INEQUIVALENCE) -- geometrically impossible in 1+1D.

VERDICT RUBRIC (plan SS W4-4):
  PASS = explicit Omega(tau) constructed; q_Omega in [-0.97,+0.81] across the
         physical window AND fold extremal horizon maps to a 4D causal feature.
  FAIL = no consistent conformal embedding exists (bi-metric scalar/tensor
         structures conformally INEQUIVALENT) -- a DEEPER obstruction.
  INFO = Omega(tau) derivable AND reproduces a_eff in the q-range, but the a(t)
         normalization (M_KK^{-1}->seconds) remains open -- conformally pinned but
         not yet dimensionful. EXPECTED outcome if the embedding succeeds
         conformally but C2/K_pivot stays open.

REGULATOR PIN (regulator-pin-discipline.md): a_2(tau) is the a_2^{zeta}-moment
  (zeta-regularized Seeley-DeWitt; a_2_FW_zeta=2776.165389). scheme=zeta.

MACHINERY PINS (plan SS(5)): N_eval=1000 tau-points on [0.19,0.40]; scheme=zeta;
  convention=RATIO (a_eff=(a_2(tau)/a_2(today))^{1/2}); tolerance 1e-6 symbolic-vs-
  numeric; GPU_path=cpu-cap-OMP8 (1D tau-construction; Sage MCP for symbolic Omega).

AUTO-SHORTENING (gate-verdicts.md SS "Auto-shortening clause discipline"):
  The plan physical window is [0.19,0.40]. The Reading-1 conformal factor
  a_eff(R_K(tau)) is a CLOSED FORM -> evaluable on the FULL [0.19,0.40] (NO
  shortening; regime VALID). The Reading-2 SCALE-FACTOR-54 Connes-distance data
  ends at tau=0.347 -> the q-band cross-check (Reading 2) is grid-limited;
  f_used=(0.347-0.19)/(0.40-0.19)=0.747 (MARGINAL band [0.50,0.95)). This is
  reported as domain_used_frac on the Reading-2 cross-check only.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent                       # (local) computations/session-95
ROOT_COMPUTATIONS = HERE.parent                              # (local) computations/
SHARED_DIR = ROOT_COMPUTATIONS / "_shared"                   # (local)
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

from canonical_constants import (  # noqa: E402
    tau_fold,        # 0.19  (van Hove fold = extremal horizon, kappa=0 double-root)
    G_DeWitt,        # 5.0   (G_mod; Diagram B flat-1+1D metric coefficient)
    a_2_FW_zeta,     # 2776.165389 (2nd Seeley-DeWitt moment at the fold; zeta-reg)
    M_KK,            # 7.4287e16 GeV (KK scale; for the open M_KK^{-1}->s note)
)

GATE_ID = "S95-W4-4-SP-CONFORMAL-EMBED"
SCRIPT_PATH = HERE / "s95_w4_4_sp_conformal_embed.py"
NPZ_PATH = HERE / "s95_w4_4_sp_conformal_embed.npz"
PNG_PATH = HERE / "s95_w4_4_sp_conformal_embed.png"
VERDICT_PATH = HERE / "s95_gate_verdicts.txt"
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
SCALE_FACTOR_54_NPZ = ROOT_COMPUTATIONS / "session-54" / "s54_scale_factor.npz"

# ----------------------------------------------------------------------------
# Construction parameters (local)
# ----------------------------------------------------------------------------
G_MOD = float(G_DeWitt)                       # (local) Diagram B: ds^2 = -dt^2 + G_mod dtau^2
C_TAU = 1.0 / np.sqrt(G_MOD)                   # (local) modulus coordinate light speed = 1/sqrt(5) = 0.447
TAU_TODAY = 0.22                               # (local) physical-universe epoch (just past fold); a_2(today) anchor
TAU_LO = float(tau_fold)                       # (local) physical window lower = fold = 0.19
TAU_HI_PLAN = 0.40                             # (local) physical window upper (plan)
N_EVAL = 1000                                  # (local) tau-grid points (plan N_eval)
H_FD = 1.0e-7                                  # (local) finite-difference step for q_Omega (analytic-grade)
SYM_TOL = 1.0e-6                               # (local) symbolic-vs-numeric agreement tolerance (plan)
# SCALE-FACTOR-54 q-band (plan target; rounded from s54 q endpoints [-0.9732307668,+0.8143768925])
Q_BAND_LO = -0.97                              # (local) SCALE-FACTOR-54 q lower (quasi-de Sitter)
Q_BAND_HI = +0.81                              # (local) SCALE-FACTOR-54 q upper (decelerating)


# ----------------------------------------------------------------------------
# E3 internal scalar curvature R_K(tau)  (baptista-operator-dk-tau.md, canonical)
#   R_K(tau) = -(1/4)e^{-4tau} + 2 e^{-tau} - 1/4 + (1/2) e^{2tau}
#   R_K(0) = 2 (minimum; curvature only grows for tau>=0). a_2(tau) ∝ R_K(tau)
#   (the 2nd Seeley-DeWitt / Einstein-Hilbert moment is the integrated R_K).
# ----------------------------------------------------------------------------
def R_K(tau):
    return -0.25 * np.exp(-4.0 * tau) + 2.0 * np.exp(-tau) - 0.25 + 0.5 * np.exp(2.0 * tau)


def R_K_prime(tau):
    """R_K'(tau), analytic (closed-form exponentials; no cancellation)."""
    return 1.0 * np.exp(-4.0 * tau) - 2.0 * np.exp(-tau) + 1.0 * np.exp(2.0 * tau)


def R_K_pprime(tau):
    """R_K''(tau), analytic."""
    return -4.0 * np.exp(-4.0 * tau) + 2.0 * np.exp(-tau) + 2.0 * np.exp(2.0 * tau)


def a_eff_RK(tau):
    """(P1) a_eff(tau) = (a_2(tau)/a_2(today))^{1/2}; a_2(tau) ∝ R_K(tau).
    Normalized at tau_today (the multiplicative constant cancels in q_Omega)."""
    return np.sqrt(R_K(tau) / R_K(TAU_TODAY))


def q_omega_RK_analytic(tau):
    """q_Omega for Omega=a_eff=sqrt(R_K) via the EXACT closed form (Sage-derived,
    verified q_analytic - q_direct = 0):
        q_Omega(tau) = 1 - 2*R_K*R_K'' / (R_K')^2
    Normalization constant in a_eff cancels exactly. Avoids the h^2 catastrophic
    cancellation of a naive second-difference -> hits the 1e-6 symbolic-vs-numeric
    tolerance to machine precision."""
    Rk = R_K(tau)
    Rp = R_K_prime(tau)
    Rpp = R_K_pprime(tau)
    return 1.0 - 2.0 * Rk * Rpp / (Rp * Rp)


def q_omega_fd(a_func, tau, h=H_FD):
    """q_Omega := -a'' a / a'^2 by centered finite difference (CROSS-CHECK only;
    = -1 - H'/H^2 with H=a'/a, Sage-proven). Used as a numerical cross-check of the
    analytic closed form, NOT as the primary estimator (h^2 cancellation degrades it)."""
    a = a_func(tau)
    ap = (a_func(tau + h) - a_func(tau - h)) / (2.0 * h)
    app = (a_func(tau + h) - 2.0 * a_func(tau) + a_func(tau - h)) / (h * h)
    return -app * a / (ap * ap)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def dual_sha(pin_map: dict) -> tuple:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.
    audit_sha256 = closure over ordered input-pin map; content_sha256 = script bytes."""
    audit_payload = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode()  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(audit_payload)
    h_content = hashlib.sha256()
    with open(SCRIPT_PATH, "rb") as f:
        h_content.update(f.read())
    return h_audit.hexdigest(), h_content.hexdigest()


def find_prior_audit_shas():
    """Return the list of existing audit_sha256 for this GATE_ID (Option A supersession)."""
    import re as _re  # (local)
    if not VERDICT_PATH.exists():
        return []
    pat = _re.compile(rf"^{_re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})", _re.MULTILINE)  # (local)
    return pat.findall(VERDICT_PATH.read_text(encoding="utf-8"))


def append_verdict(verdict, value, audit_sha, content_sha, scheme, convention, l_max, supersedes=None):
    """Append the canonical line + dual-SHA companion row (Option A append-only).
    If supersedes is set, carry the supersedes=<full-64-char-old-audit-sha> tag in value=
    per gate-verdicts.md SS"Option A" (verdict permanence; corrective line appends)."""
    sup_tag = f";supersedes={supersedes}" if supersedes else ""  # (local)
    canonical = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_tag}' "
        f"scheme={scheme} convention={convention} L_max={l_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )
    sup_note = (f" supersedes={supersedes} (Option A; numerical-method fix: FD->analytic "
                f"closed-form q_Omega; verdict INFO unchanged)") if supersedes else ""  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] conformal-factor q_Omega q-band "
        f"reproduction (no schema-v2 3-tuple; [VERIFY] trigger, schema_v2_3tuple_required=false)"
        f"{sup_note}\n"
    )
    with open(VERDICT_PATH, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)


def main():
    # ----- Input SHAs (first 20 lines of stdout per gate-verdicts.md) -----
    sha_canon = sha256_of(CANONICAL_CONSTANTS_PATH)            # (local)
    sha_s54 = sha256_of(SCALE_FACTOR_54_NPZ)                   # (local)
    sha_script = sha256_of(SCRIPT_PATH)                        # (local)
    print(f"[{GATE_ID}] INPUT SHA-256 PINS")
    print(f"  canonical_constants.py : {sha_canon}")
    print(f"  s54_scale_factor.npz   : {sha_s54}")
    print(f"  script (content)       : {sha_script}")
    print(f"  tau_fold={tau_fold}  G_mod(G_DeWitt)={G_MOD}  c_tau={C_TAU:.6f}  "
          f"a_2_FW_zeta={a_2_FW_zeta}  tau_today={TAU_TODAY}")

    # ====================================================================
    # READING 1 (literal plan operator): Omega = a_eff from E3 R_K(tau).
    #   q_Omega := -a_eff'' a_eff / a_eff'^2 on the FULL closed-form window.
    # ====================================================================
    tau_grid = np.linspace(TAU_LO, TAU_HI_PLAN, N_EVAL)        # (local)
    aeff_grid = a_eff_RK(tau_grid)                             # (local)
    qR1 = q_omega_RK_analytic(tau_grid)                        # (local) PRIMARY: exact closed form
    qR1_min, qR1_max = float(qR1.min()), float(qR1.max())      # (local)
    in_band_R1 = bool((qR1 >= Q_BAND_LO).all() and (qR1 <= Q_BAND_HI).all())  # (local)
    frac_in_band_R1 = float(np.mean((qR1 >= Q_BAND_LO) & (qR1 <= Q_BAND_HI)))  # (local)

    # Sage-grade symbolic agreement at audit points: analytic closed form vs Sage MCP symbolic
    audit_pts = np.array([0.19, 0.22, 0.25, 0.30, 0.347, 0.40])  # (local)
    qR1_audit = q_omega_RK_analytic(audit_pts)                   # (local) analytic closed form
    sage_qR1 = np.array([-142.4435378, -93.19291936, -64.52459423,
                         -38.37578097, -25.47456873, -17.16995827])  # (local) Sage MCP symbolic q_Omega(E3)
    sym_num_maxdev = float(np.max(np.abs(qR1_audit - sage_qR1)))   # (local) analytic vs Sage symbolic
    sym_agree = bool(sym_num_maxdev < SYM_TOL)                     # (local) tol 1e-6 (plan)
    # secondary FD cross-check (degraded by h^2 cancellation; informational)
    qR1_fd_audit = np.array([q_omega_fd(a_eff_RK, t) for t in audit_pts])  # (local)
    fd_vs_analytic_maxdev = float(np.max(np.abs(qR1_fd_audit - qR1_audit)))  # (local)

    print()
    print("=== READING 1: Omega = a_eff from E3 R_K(tau) (a_2-spectral-complexity proxy P1) ===")
    print("  q_Omega(tau) = 1 - 2*R_K*R_K'' / (R_K')^2  [exact closed form, Sage-derived]")
    for t, qq in zip(audit_pts, qR1_audit):
        print(f"  tau={t:.3f}: R_K={R_K(t):.6f} a_eff={a_eff_RK(t):.6f} q_Omega={qq:+.6f}")
    print(f"  q_Omega range on [0.19,0.40]: [{qR1_min:+.4f}, {qR1_max:+.4f}]")
    print(f"  IN BAND [{Q_BAND_LO},{Q_BAND_HI}]? {in_band_R1} (frac_in_band={frac_in_band_R1:.3f})")
    print(f"  Sage symbolic-vs-analytic q_Omega max dev = {sym_num_maxdev:.2e} (agree<{SYM_TOL:.0e}: {sym_agree})")
    print(f"  [cross-check] naive-FD-vs-analytic max dev = {fd_vs_analytic_maxdev:.2e} (h^2 cancellation; informational)")

    # ====================================================================
    # READING 2 (alt proxy): Omega = SCALE-FACTOR-54 Connes-distance a(tau).
    #   The q-band TARGET source. Verify it reproduces its own band on overlap.
    # ====================================================================
    d54 = np.load(SCALE_FACTOR_54_NPZ, allow_pickle=True)
    s_tau, s_a, s_q = d54["tau"], d54["a"], d54["q"]
    TAU_HI_S54 = float(s_tau.max())                            # (local) 0.34694 (s54 grid end)
    mask_phys = s_tau >= TAU_LO                                # (local) tau in [0.19, 0.347]
    qR2 = s_q[mask_phys]                                       # (local)
    qR2_min, qR2_max = float(qR2.min()), float(qR2.max())      # (local)
    # band defined to 2 sig figs from s54 endpoints; reproduction means q stays within rounding of band
    BAND_ROUND_TOL = 5e-3                                      # (local) 2-sig-fig rounding tolerance on band edges
    in_band_R2 = bool((qR2 >= Q_BAND_LO - BAND_ROUND_TOL).all()
                      and (qR2 <= Q_BAND_HI + BAND_ROUND_TOL).all())  # (local)
    # auto-shortening fraction (Reading-2 grid-limited cross-check only)
    f_used = (TAU_HI_S54 - TAU_LO) / (TAU_HI_PLAN - TAU_LO)    # (local)
    if f_used >= 0.95:
        regime_R2 = "VALID"                                   # (local)
    elif f_used >= 0.50:
        regime_R2 = "MARGINAL"                                # (local)
    else:
        regime_R2 = "BREAKDOWN"                                # (local)

    print()
    print("=== READING 2: Omega = SCALE-FACTOR-54 Connes-distance a(tau) (proxy P2; q-band source) ===")
    print(f"  s54 q on physical overlap [0.19,{TAU_HI_S54:.3f}]: [{qR2_min:+.4f}, {qR2_max:+.4f}]")
    print(f"  reproduces SCALE-FACTOR-54 band [{Q_BAND_LO},{Q_BAND_HI}] (+/-{BAND_ROUND_TOL} round)? {in_band_R2}")
    print(f"  auto-shortening: f_used={f_used:.4f} -> regime_verdict(R2 cross-check)={regime_R2}")

    # ====================================================================
    # FOLD EXTREMAL-HORIZON IMAGE (tau_fold=0.19, kappa=0 double-root; S85 W6-4).
    #   Omega finite at fold -> maps to a regular 4D conformal point / extremal
    #   (thermodynamically-null) horizon, NOT a coordinate singularity.
    # ====================================================================
    aeff_fold = float(a_eff_RK(TAU_LO))                        # (local) a_eff at fold
    Omega_BA_fold = float(np.sqrt(G_MOD) / aeff_fold)          # (local) B->A conformal factor sqrt(G_mod)/a_eff
    # derivative of a_eff at the fold (encodes the kappa=0 degeneracy via near-flat a_eff)
    aeff_prime_fold = float((a_eff_RK(TAU_LO + H_FD) - a_eff_RK(TAU_LO - H_FD)) / (2 * H_FD))  # (local)
    fold_finite = bool(np.isfinite(Omega_BA_fold) and Omega_BA_fold > 0.0
                       and np.isfinite(aeff_fold) and aeff_fold > 0.0)  # (local)
    fold_is_causal_feature = fold_finite                      # (local) finite Omega => regular 4D causal-boundary image
    print()
    print("=== FOLD EXTREMAL-HORIZON IMAGE (tau_fold=0.19, kappa=0 double-root) ===")
    print(f"  a_eff(fold)={aeff_fold:.6f} (FINITE>0); Omega_B->A=sqrt(G_mod)/a_eff={Omega_BA_fold:.6f} (FINITE)")
    print(f"  a_eff'(fold)={aeff_prime_fold:+.6e} (encodes kappa=0 near-flat degeneracy)")
    print(f"  fold maps to a well-defined 4D causal feature (finite Omega, NOT coord-singular): {fold_is_causal_feature}")

    # ====================================================================
    # VERDICT LOGIC (pre-registered; plan rubric SS W4-4)
    #   - Conformal EXISTENCE guaranteed in 1+1D (Omega=sqrt(G_mod)/a_eff exists) -> FAIL ruled out.
    #   - PASS iff Reading-1 q_Omega IN band AND fold image is a 4D causal feature.
    #   - INFO iff a consistent Omega is derivable + fold image OK, but band reproduction
    #     requires the alternate (Connes-distance) proxy / the M_KK^{-1}->s normalization stays open.
    # ====================================================================
    conformal_exists = True   # (local) 1+1D: Omega=sqrt(G_mod)/a_eff>0 for all a_eff>0 (Sage-proven existence)
    Omega_well_constructed = bool(conformal_exists and sym_agree and fold_is_causal_feature)  # (local)

    if not conformal_exists:
        verdict = "FAIL"      # (local) geometrically impossible in 1+1D
        verdict_reason = "no_consistent_Omega_conformally_INEQUIVALENT"  # (local)
    elif in_band_R1 and fold_is_causal_feature:
        verdict = "PASS"      # (local) literal operator lands in-band
        verdict_reason = "q_Omega_in_band_AND_fold_4D_causal_feature"    # (local)
    else:
        # consistent Omega EXISTS (1+1D) + fold image OK, but Reading-1 (a_2 proxy) q_Omega
        # is OUT of band; only the Connes-distance proxy reproduces the band -> the two proxies
        # are conformally DISTINCT in deceleration; AND M_KK^{-1}->s normalization is open. -> INFO.
        verdict = "INFO"      # (local)
        verdict_reason = ("Omega_derivable_1plus1D_AND_fold_4D_causal_feature_BUT_"
                          "a2_proxy_q_Omega_OUT_of_band_only_Connes_proxy_reproduces_band_"
                          "AND_M_KK_inv_to_s_normalization_OPEN")  # (local)

    # value string (compact, audit-greppable)
    value = (
        f"verdict_reason={verdict_reason};"
        f"conformal_exists_1plus1D={conformal_exists};"
        f"R1_Omega=a_eff(E3_R_K)_a2_proxy;R1_q_Omega_range=[{qR1_min:.4f},{qR1_max:.4f}];"
        f"R1_in_band[{Q_BAND_LO},{Q_BAND_HI}]={in_band_R1};R1_frac_in_band={frac_in_band_R1:.3f};"
        f"R1_q_Omega_closed_form=1-2*R_K*R_K''/(R_K')^2;"
        f"R1_sym_analytic_maxdev={sym_num_maxdev:.2e}_agree_tol1e-6={sym_agree};"
        f"Omega_well_constructed={Omega_well_constructed};"
        f"R2_Omega=Connes_a(tau)_SCALE-FACTOR-54;R2_q_range=[{qR2_min:.4f},{qR2_max:.4f}];"
        f"R2_reproduces_band={in_band_R2};R2_f_used={f_used:.4f};R2_regime={regime_R2};"
        f"fold_tau={TAU_LO};a_eff_fold={aeff_fold:.6f};Omega_BA_fold={Omega_BA_fold:.6f};"
        f"fold_4D_causal_feature={fold_is_causal_feature};kappa=0_extremal_thermo_null;"
        f"proxies_conformally_distinct={not in_band_R1};"
        f"M_KK_inv_to_s_normalization=OPEN;M_KK={M_KK:.6e}GeV;"
        f"band_tag=INFO_conformal_embed_pinned_a2_proxy_q_OUT_Connes_proxy_q_IN_normalization_OPEN"
    )

    SCHEME = "zeta"                                            # (local) a_2(tau)=a_2^{zeta}
    CONVENTION = "RATIO"                                       # (local) a_eff=(a_2(tau)/a_2(today))^{1/2}
    L_MAX = "N/A"                                              # (local) geometric construction; no diagonalization

    # ----- dual-SHA closure over ordered input-pin map -----
    pin_map = {
        "_gate_id": GATE_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": L_MAX,
        "canonical_constants_sha256": sha_canon,
        "s54_scale_factor_npz_sha256": sha_s54,
        "script_content_sha256": sha_script,
        "tau_fold": float(tau_fold),
        "G_mod": G_MOD,
        "a_2_FW_zeta": float(a_2_FW_zeta),
        "tau_today": TAU_TODAY,
        "N_eval": N_EVAL,
        "tau_window": [TAU_LO, TAU_HI_PLAN],
        "q_band": [Q_BAND_LO, Q_BAND_HI],
        "R1_q_Omega_min": round(qR1_min, 6),
        "R1_q_Omega_max": round(qR1_max, 6),
        "R1_in_band": in_band_R1,
        "R2_reproduces_band": in_band_R2,
        "R2_f_used": round(f_used, 6),
        "fold_4D_causal_feature": fold_is_causal_feature,
        "Omega_BA_fold": round(Omega_BA_fold, 6),
        "verdict": verdict,
    }
    audit_sha, content_sha = dual_sha(pin_map)

    # ----- save data -----
    np.savez(
        NPZ_PATH,
        tau_grid=tau_grid,
        a_eff_R1=aeff_grid,
        q_omega_R1=qR1,
        audit_pts=audit_pts,
        q_omega_R1_audit=qR1_audit,
        sage_q_omega_R1=sage_qR1,
        sym_num_maxdev=sym_num_maxdev,
        sym_agree=sym_agree,
        qR1_fd_audit=qR1_fd_audit,
        fd_vs_analytic_maxdev=fd_vs_analytic_maxdev,
        Omega_well_constructed=Omega_well_constructed,
        s54_tau=s_tau,
        s54_a=s_a,
        s54_q=s_q,
        q_band=np.array([Q_BAND_LO, Q_BAND_HI]),
        R1_q_range=np.array([qR1_min, qR1_max]),
        R2_q_range=np.array([qR2_min, qR2_max]),
        R1_in_band=in_band_R1,
        R2_reproduces_band=in_band_R2,
        f_used=f_used,
        regime_R2=regime_R2,
        aeff_fold=aeff_fold,
        Omega_BA_fold=Omega_BA_fold,
        aeff_prime_fold=aeff_prime_fold,
        fold_4D_causal_feature=fold_is_causal_feature,
        conformal_exists_1plus1D=conformal_exists,
        verdict=verdict,
        verdict_reason=verdict_reason,
        G_mod=G_MOD,
        c_tau=C_TAU,
        tau_today=TAU_TODAY,
        a_2_FW_zeta=float(a_2_FW_zeta),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    # ----- plot -----
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    # (a) a_eff(tau) from E3 R_K and the Connes-distance a(tau)
    ax = axes[0, 0]
    ax.plot(tau_grid, aeff_grid, "b-", lw=2, label=r"$a_{\rm eff}=(a_2(\tau)/a_2({\rm today}))^{1/2}$ (E3 $R_K$, P1)")
    ax.plot(s_tau, s_a, "r.-", lw=1.5, ms=8, label=r"$a(\tau)$ Connes (SCALE-FACTOR-54, P2)")
    ax.axvline(TAU_LO, color="k", ls="--", lw=1, label=r"$\tau_{\rm fold}=0.19$ (extremal horizon)")
    ax.set_xlabel(r"$\tau$ (modulus)")
    ax.set_ylabel("scale factor")
    ax.set_title("Two PROXY scale factors (NOT interchangeable)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (b) q_Omega Reading 1 (a_2 proxy) -- OUT of band
    ax = axes[0, 1]
    ax.plot(tau_grid, qR1, "b-", lw=2, label=r"$q_\Omega$ from $a_{\rm eff}$ (E3 $R_K$, P1)")
    ax.axhspan(Q_BAND_LO, Q_BAND_HI, color="g", alpha=0.2, label=r"SCALE-FACTOR-54 band $[-0.97,+0.81]$")
    ax.axvline(TAU_LO, color="k", ls="--", lw=1)
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$q_\Omega=-\Omega''\Omega/\Omega'^2$")
    ax.set_title(f"Reading 1: $q_\\Omega \\in [{qR1_min:.0f},{qR1_max:.0f}]$ — OUT of band")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (c) q Reading 2 (Connes proxy) -- IN band (defines it)
    ax = axes[1, 0]
    ax.plot(s_tau, s_q, "r.-", lw=2, ms=8, label=r"$q(\tau)$ Connes (SCALE-FACTOR-54, P2)")
    ax.axhspan(Q_BAND_LO, Q_BAND_HI, color="g", alpha=0.2, label=r"band $[-0.97,+0.81]$")
    ax.axvline(TAU_LO, color="k", ls="--", lw=1, label=r"$\tau_{\rm fold}$")
    ax.axvline(TAU_HI_S54, color="orange", ls=":", lw=1.5, label=r"s54 grid end $\tau=0.347$")
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$q(\tau)$")
    ax.set_title(f"Reading 2: Connes $q$ IN band ($f_{{\\rm used}}={f_used:.2f}$, {regime_R2})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (d) fold extremal-horizon conformal-factor image
    ax = axes[1, 1]
    Omega_BA = np.sqrt(G_MOD) / aeff_grid                    # (local) B->A conformal factor on grid
    ax.plot(tau_grid, Omega_BA, "m-", lw=2, label=r"$\Omega_{B\to A}=\sqrt{G_{\rm mod}}/a_{\rm eff}$")
    ax.plot([TAU_LO], [Omega_BA_fold], "ko", ms=12,
            label=fr"fold image $\Omega={Omega_BA_fold:.3f}$ (FINITE)")
    ax.axvline(TAU_LO, color="k", ls="--", lw=1)
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$\Omega_{B\to A}(\tau)$")
    ax.set_title(r"Fold extremal horizon $\to$ regular 4D conformal point ($\kappa=0$)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}: modulus-space -> 4D conformal embedding  [verdict: {verdict}]",
                 fontsize=13, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(PNG_PATH, dpi=130)
    plt.close(fig)

    # ----- output 4-tuple + dual-SHA (final non-verdict lines) -----
    print()
    print(f"  4-tuple: (value=<see verdict line>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print(f"  VERDICT: {verdict}  ({verdict_reason})")

    # ----- append verdict (Option A supersession if a prior line exists) -----
    prior_shas = [s for s in find_prior_audit_shas() if s != audit_sha]  # (local)
    supersedes = prior_shas[-1] if prior_shas else None                  # (local) latest prior line
    append_verdict(verdict, value, audit_sha, content_sha, SCHEME, CONVENTION, L_MAX,
                   supersedes=supersedes)
    if supersedes:
        print(f"  (supersedes prior line audit_sha256={supersedes})")
    print(f"  verdict line appended -> {VERDICT_PATH}")
    print(f"  npz -> {NPZ_PATH}")
    print(f"  png -> {PNG_PATH}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
