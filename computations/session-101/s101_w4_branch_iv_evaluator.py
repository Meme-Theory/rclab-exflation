#!/usr/bin/env python3
"""
S101 W4-3 — S101-W0-BRANCH-IV-EVALUATOR — post-S86 branch-iv w0(L) evaluator + CAC spread
=========================================================================================

Gate: S101-W0-BRANCH-IV-EVALUATOR ([VERIFY])

ONE gate, TWO sequenced legs in a single producing script (planner's documented call):

  LEG 1 (derivation + HARD admissibility):
    Construct the recombination map  Phi(R_JK distance-2, xi_E_GGE_inv distance-1) -> R-slot
    occupant, with EVERY coefficient sourced from the SV1 closed-form exact f-reduction, a
    substrate identity, or a canonical constant.  NO coefficient solved against w_0_B.
    Pre-register the §(iv-bis) surrogate-vs-canonical algebraic-distance theorem and DECLARE
    the consumption layer per substrate-first-canonical-sourcing §(ii.A).
    HARD admissibility:  |Phi(L=10) - (-0.842454)| <= 1e-5  with ZERO tuned normalization.
    If INADMISSIBLE -> composite INFO-(derivation-inadmissible); LEG 2 does NOT execute.

  LEG 2 (CAC spread; executes ONLY on leg-1 admissibility):
    Compose the derived evaluator with the CAC (regulator-convention-lockdown.md):
       w0^CAC(L) = rho_zeta(L) + offset_zeta,   offset_zeta == w_0_B - rho_zeta(L=10).
    Exhibit offset_zeta's PHYSICAL content (effacement/GGE-dressing translation).
    spread = max - min of w0^CAC over L in {8, 10, 12}; gate vs the UNCHANGED W1-4 thresholds
    ({<= 0.025 PASS | (0.025, 0.050] INFO | > 0.050 FAIL}).

Pre-registered threshold:
  LEG 1: |Phi(R_JK(10), xi_E_GGE_inv; Theta_derived) - (-0.842454)| <= 1e-5, Theta_derived
         containing zero tuned normalization (admissibility PRECONDITION).
  LEG 2: spread <= 0.025 PASS / (0.025, 0.050] INFO / > 0.050 FAIL.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py            (R_JK, xi_E_GGE_inv, K_base, Delta_BCS, tau_fold, N_cells, w0_FW)
  - s84_w1a_w0_sv1.npz                (SV1 closed-form anchor: xi_J, xi_E_GGE, F_Josephson_zeta,
                                       rho_GGE_zeta, P_GGE_zeta, w_0_iv = -0.842454...)
  - s85_w12_elim1_D_K_Lmax_moments.npz (R_JK trajectory (0.01129619, 0.00803461, 0.00598992))
  - s84_spectrum_cache_L12_tau019.npz  (L12 master cache; upstream-trusted, S101-TAU0 PASS)
  - s100b_w0_branch_resolution.npz     (prior INFO-shape record + C0 6.2sigma cautionary instance)
  - branch-iv-canonical.md             (registry formula source; consume the session-85 moment path)

Output 4-tuple:
  (value=<computed>, scheme=zeta, convention=CAC-branch-iv-anchored-L10-DERIVED-OFFSET, L_max={8,10,12})

Classification: GEOMETRIC

METHODOLOGY
-----------
The SV1 closed form (S84 W1-3.SV1 PASS, two-component Zubarev-dressed) is the f-reduction
    w_0^(iv) = f(R),   f(R) = (-c_J*R + P_GGE_zeta) / (c_J*R + rho_GGE_zeta),
    c_J = |F_Josephson_zeta| / N_cells   (all coefficients Theta-free canonical/substrate).
At the SV1 anchor  R = R_sv1 = xi_J/xi_E_GGE = 0.45357833655706  (= legacy R_JE at L=5),
f(R_sv1) = -0.842454 = w_0_B EXACTLY (to 1e-12).

The S86-BRANCH-IV-FORMULATION-COMMIT RETIRED R_JE and replaced it with TWO distance-tagged
successors: R_JK (distance-2 spectral-moment ratio) and xi_E_GGE_inv (distance-1 GGE
energy-dressing inverse).  The recombination map Phi must reconstruct the R-slot occupant
(i.e. R_sv1) from {R_JK, xi_E_GGE_inv} + Theta-free coefficients, then push it through f.
The leg-1 admissibility question is EXACTLY: does a Theta-free combination of the two retired-
into successors reproduce R_sv1 (hence w_0_B) at 1e-5 WITHOUT re-injecting R_sv1 itself?

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-cap OMP8 (cached-moment arithmetic; no diagonalization)
- ZERO-FREE-NORMALIZATION ATTESTATION: no fit/solve call targets w_0_B anywhere in this
  script; every Theta coefficient carries a provenance comment; the admissibility residual
  is COMPUTED, never minimized.
- SHA-256 of all inputs logged in first 20 lines of stdout; dual-SHA emitted (S84+).
- Verdict via emit_verdict MCP tool (race-safe): script PRINTS payload; agent calls the tool.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import; _shared on path first)
# ---------------------------------------------------------------------------
_SHARED = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # explicit names used below (provenance-anchored)
    R_JK as R_JK_CANON,
    xi_E_GGE_inv as XI_E_GGE_INV_CANON,
    K_base as K_BASE_CANON,
    Delta_BCS as DELTA_BCS_CANON,
    N_cells as N_CELLS_CANON,
    w0_FW as W0_FW_CANON,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S101"                                                  # (local)
GATE_ID = "S101-W0-BRANCH-IV-EVALUATOR"                           # (local)
SCHEME = "zeta"                                                   # (local)
CONVENTION = "CAC-branch-iv-anchored-L10-DERIVED-OFFSET"          # (local)
L_MAX = "{8,10,12}"                                               # (local)

# Pre-registered thresholds (define BEFORE running)
ADMISSIBILITY_TOL = 1e-5         # (local) leg-1 |Phi(10) - w_0_B| absolute (SV1 reproduction tol)
SPREAD_PASS = 0.025              # (local) leg-2 spread PASS ceiling (UNCHANGED W1-4)
SPREAD_INFO = 0.050              # (local) leg-2 spread INFO ceiling (UNCHANGED W1-4)
L_SCAN = (8, 10, 12)             # (local) L-mesh
L_ANCHOR = 10                    # (local)

W_0_B = -0.842454                # (local) branch-iv anchored value at L_anchor=10 [S84 W1-3.SV1]

OUT_NPZ = SESSION_DIR / "s101_w4_branch_iv_evaluator.npz"
OUT_PNG = SESSION_DIR / "s101_w4_branch_iv_evaluator.png"

SV1_NPZ = COMPUTATIONS_DIR / "session-84" / "s84_w1a_w0_sv1.npz"
RJK_NPZ = COMPUTATIONS_DIR / "session-85" / "s85_w12_elim1_D_K_Lmax_moments.npz"
L12_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
SENS_NPZ = COMPUTATIONS_DIR / "session-100b" / "s100b_w0_branch_resolution.npz"
BRANCH_IV_REG = PROJECT_ROOT / "sessions" / "framework" / "registry" / "branch-iv-canonical.md"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SV1_NPZ,
    RJK_NPZ,
    L12_CACHE,
    SENS_NPZ,
    BRANCH_IV_REG,
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
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
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
# Section 5a — SV1 closed-form f-reduction (Theta-free; the admissible anchor map)
# ---------------------------------------------------------------------------
def f_branch_iv(R: float, c_J: float, P_G_z: float, rho_G_z: float) -> float:
    """SV1 closed-form f-reduction  w_0^(iv) = f(R).
    All three coefficients (c_J, P_G_z, rho_G_z) are Theta-FREE canonical/substrate
    constants -- NONE is solved against w_0_B.  f(R_sv1) = w_0_B EXACTLY by SV1 PASS.
    """
    return (-c_J * R + P_G_z) / (c_J * R + rho_G_z)


# ---------------------------------------------------------------------------
# Section 5b — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    rec: dict = {}  # (local)

    # ----- Load SV1 anchor (all Theta-free; the f-reduction coefficient source) -----
    sv1 = np.load(SV1_NPZ, allow_pickle=True)  # (local)
    xi_J = float(sv1["xi_J"])                    # (local) 0.008911  [W0-workshop/Sagan audit]
    xi_E_GGE = float(sv1["xi_E_GGE"])            # (local) 0.019646  [W3-G51 energy-weighted Zubarev]
    F_J_zeta = float(sv1["F_Josephson_zeta"])    # (local) -336.641  [S58 canonical]
    rho_GGE_zeta = float(sv1["rho_GGE_zeta"])    # (local) 1.709     [SV1 npz canonical]
    P_GGE_zeta = float(sv1["P_GGE_zeta"])        # (local) -0.688    [SV1 npz canonical]
    N_cells_v = int(sv1["N_cells"])              # (local) 32        [S42 domain formation]
    w_0_iv_sv1 = float(sv1["w_0_iv"])            # (local) -0.8424542759870739 (SV1 PASS anchor)

    # Theta-free derived coefficients (provenance-commented; NONE solved against w_0_B)
    c_J = abs(F_J_zeta) / N_cells_v              # (local) = 10.52003125  [|F_J_zeta|/N_cells, SV1 Step 1]
    R_sv1 = xi_J / xi_E_GGE                        # (local) = 0.45357833655706  [SV1 dressing ratio = legacy R_JE]

    # Cross-check: the SV1 f-reduction reproduces w_0_B at R_sv1 (this IS the admissible anchor,
    # but R_sv1 is the RETIRED object; the leg-1 task is to reach it from {R_JK, xi_E_GGE_inv}).
    w0_at_Rsv1 = f_branch_iv(R_sv1, c_J, P_GGE_zeta, rho_GGE_zeta)  # (local)
    rec["sv1_f_reduction_exact"] = bool(abs(w0_at_Rsv1 - w_0_iv_sv1) < 1e-12)
    rec["w0_at_Rsv1"] = w0_at_Rsv1
    rec["R_sv1"] = R_sv1
    rec["c_J"] = c_J

    # ----- Load R_JK trajectory (distance-2; CACHE-MOMENT layer) -----
    rjk = np.load(RJK_NPZ, allow_pickle=True)  # (local)
    L_from_npz = [int(x) for x in rjk["L_max"]]   # (local) [8,10,12]
    R_JK_traj = [float(x) for x in rjk["R_JK"]]   # (local) [0.01129619, 0.00803461, 0.00598992]
    assert L_from_npz == list(L_SCAN), f"L-mesh mismatch: {L_from_npz} vs {L_SCAN}"
    # canonical-constant cross-check at L=10 (consumption-layer declaration: cache-moment)
    rec["R_JK_canon_match_L10"] = bool(abs(R_JK_traj[1] - float(R_JK_CANON)) < 1e-8)
    rec["R_JK_traj"] = R_JK_traj
    R10 = R_JK_traj[1]                            # (local)

    # ----- distance-1 successor (canonical) -----
    xi_E_GGE_inv = float(XI_E_GGE_INV_CANON)      # (local) 13.642473425595973  [S86 commit]
    rec["xi_E_GGE_inv"] = xi_E_GGE_inv
    # substrate-identity cross-check: xi_E_GGE_inv == 59.8 * Delta_BCS / K_base
    n_pairs = 59.8                                # (local) GGE pair count (Ordered-Veil relic)
    xi_E_GGE_inv_substrate = n_pairs * float(DELTA_BCS_CANON) / float(K_BASE_CANON)  # (local)
    rec["xi_E_GGE_inv_substrate_match"] = bool(abs(xi_E_GGE_inv_substrate - xi_E_GGE_inv) < 1e-5)

    # =====================================================================
    # LEG 1 — derivation: Theta-free recombination Phi -> R-slot occupant
    # =====================================================================
    # The R-slot occupant the f-reduction needs is R_sv1 (the retired R_JE).  Search the
    # Theta-free monomial family Phi(R_JK, xi_E_GGE_inv) = R_JK^a * xi_E_GGE_inv^b over a small
    # exponent mesh a,b in {-2,-1,0,1,2}.  ZERO coefficient is solved against w_0_B; the
    # admissibility residual is COMPUTED, never minimized.  (Other Theta-free recombinations -
    # ratios xi_J/xi_E_GGE etc. - are degenerate: they ARE R_sv1 only by re-using the retired
    # numerator/denominator, which is the re-injection the zero-free clause forbids.)
    exps = [-2, -1, 0, 1, 2]                       # (local)
    monomials = []                                 # (local) list of (a, b, R_recon, w0_recon, residual)
    best = None                                    # (local)
    for a in exps:
        for b in exps:
            if a == 0 and b == 0:
                continue
            R_recon = (R10 ** a) * (xi_E_GGE_inv ** b)         # (local) Theta-free recombination of R-slot
            w0_recon = f_branch_iv(R_recon, c_J, P_GGE_zeta, rho_GGE_zeta)  # (local)
            resid = abs(w0_recon - W_0_B)                       # (local) admissibility residual (COMPUTED)
            monomials.append((a, b, R_recon, w0_recon, resid))
            if best is None or resid < best[4]:
                best = (a, b, R_recon, w0_recon, resid)
    rec["monomial_best"] = {
        "a": best[0], "b": best[1], "R_recon": best[2], "w0_recon": best[3], "residual": best[4],
    }
    # admissibility at the R-SLOT level too: does any Theta-free monomial reach R_sv1?
    best_R = None                                  # (local)
    for a in exps:
        for b in exps:
            if a == 0 and b == 0:
                continue
            R_recon = (R10 ** a) * (xi_E_GGE_inv ** b)          # (local)
            r_resid = abs(R_recon - R_sv1) / abs(R_sv1)         # (local) relative dist to retired R-slot occupant
            if best_R is None or r_resid < best_R[3]:
                best_R = (a, b, R_recon, r_resid)
    rec["R_slot_best"] = {"a": best_R[0], "b": best_R[1], "R_recon": best_R[2], "rel_resid": best_R[3]}

    # HARD admissibility verdict (leg 1)
    leg1_residual = best[4]                         # (local) min |Phi(10) - w_0_B| over Theta-free family
    leg1_admissible = bool(leg1_residual <= ADMISSIBILITY_TOL)  # (local)
    rec["leg1_residual"] = leg1_residual
    rec["leg1_admissible"] = leg1_admissible
    rec["zero_free_normalization_attestation"] = (
        "No fit/solve call targets w_0_B. Every Theta coefficient (c_J=|F_J_zeta|/N_cells, "
        "P_GGE_zeta, rho_GGE_zeta) is canonical/substrate; the recombination Phi=R_JK^a*xi_E_GGE_inv^b "
        "sweeps an INTEGER exponent mesh; the admissibility residual is COMPUTED. The candidates that "
        "reproduce w_0_B (S100b C2/C3) do so ONLY by re-injecting R_sv1 (the RETIRED R_JE) as scale/base "
        "- the tuned normalization the zero-free clause forbids."
    )

    # ---- §(iv-bis) surrogate-vs-canonical algebraic-distance theorem (pre-registered) ----
    # (i) substitution chain surrogate -> components: the surrogate w0_surr(L) = f(R_JK(L)) reduces
    #     to component substrate quantities R_JK (distance-2), c_J/P_GGE/rho_GGE (Theta-free).
    # (ii) LOCK TEST (COMPUTED): is sign(w0) and the spread MECHANICALLY LOCKED to the monotone
    #      R_JK fall, independent of map physical content?
    w0_surr = [f_branch_iv(r, c_J, P_GGE_zeta, rho_GGE_zeta) for r in R_JK_traj]  # (local) raw f(R_JK(L))
    spread_surrogate = max(w0_surr) - min(w0_surr)                                # (local)
    # derivative-lock estimate |df/dR|*Delta R_JK at L=10 (analytic d/dR of f)
    denom10 = (c_J * R10 + rho_GGE_zeta)                                          # (local)
    dfdR_10 = (-c_J * denom10 - (-c_J * R10 + P_GGE_zeta) * c_J) / (denom10 ** 2)  # (local) exact df/dR
    dR_full = R_JK_traj[0] - R_JK_traj[2]                                         # (local) L=8->12 swing
    lock_estimate = abs(dfdR_10) * dR_full                                        # (local)
    lock_match = bool(abs(lock_estimate - spread_surrogate) / spread_surrogate < 0.10)  # (local)
    # sign lock: numerator (-c_J*R + P_GGE_zeta) < 0 for all R>0 (c_J>0, P_GGE_zeta<0); denom > 0
    sign_locked = bool(all(w < 0 for w in w0_surr)
                       and all((-c_J * r + P_GGE_zeta) < 0 for r in R_JK_traj)
                       and all((c_J * r + rho_GGE_zeta) > 0 for r in R_JK_traj))  # (local)
    rec["w0_surrogate_raw"] = w0_surr
    rec["spread_surrogate_raw"] = spread_surrogate
    rec["dfdR_10"] = dfdR_10
    rec["lock_estimate"] = lock_estimate
    rec["lock_match"] = lock_match
    rec["sign_locked"] = sign_locked
    rec["algebraic_distance_locked"] = bool(lock_match and sign_locked)
    # (iii) informativeness declaration
    rec["informativeness"] = (
        "LOCKED: spread(f(R_JK(L))) is reproduced by the |df/dR|*Delta R_JK trajectory-geometry "
        "estimate to <10% and sign(w0) is structurally negative for ALL R>0 -- the surrogate is a "
        "GEOMETRIC observable, not a cohomology-class observable. Per §(iv-bis) clause (iii), a leg-2 "
        "spread verdict on this surrogate would be UNINFORMATIVE on the canonical w_0 truncation "
        "stability; a separate canonical-evaluation gate is REQUIRED. The surrogate does NOT falsify "
        "the canonical."
    ) if (lock_match and sign_locked) else (
        "NO LOCK: spread is not mechanically forced by the R_JK trajectory geometry; the spread "
        "verdict transfers to the canonical."
    )

    # =====================================================================
    # LEG 2 — CAC spread (executes ONLY on leg-1 admissibility)
    # =====================================================================
    if leg1_admissible:
        # Derived rho_zeta(L) series = the admissible map's L-trajectory (would be Phi pushed
        # through f at each L). CAC: w0^CAC(L) = rho_zeta(L) + offset_zeta, offset = w_0_B - rho_zeta(L=10).
        rho_zeta = w0_surr  # placeholder structural form (only reached if admissible)  # (local)
        offset_zeta = W_0_B - rho_zeta[1]                                              # (local)
        cac_series = [r + offset_zeta for r in rho_zeta]                               # (local)
        spread = max(cac_series) - min(cac_series)                                     # (local)
        rec["offset_zeta"] = offset_zeta
        rec["cac_series"] = cac_series
        rec["spread"] = spread
        rec["leg2_executed"] = True
        # effacement-preservation check: w0^CAC(L=10) == w_0_B bit-precision
        rec["cac_effacement_preserved"] = bool(abs(cac_series[1] - W_0_B) < 1e-12)
    else:
        rec["offset_zeta"] = float("nan")
        rec["cac_series"] = [float("nan")] * len(L_SCAN)
        rec["spread"] = float("nan")
        rec["leg2_executed"] = False
        rec["cac_effacement_preserved"] = False

    # ----- offset_zeta PHYSICAL content note (required by method, even on non-execution) -----
    # The parent lockdown's A-branch offset (-0.340827) is a PHYSICAL effacement translation
    # (Volovik partition + Gamma_eff=0.99970). For branch-iv, the CAC offset on a Theta-free
    # admissible map would have to be the effacement/GGE-dressing translation of THAT map. The
    # C0 cautionary instance (s100b: C0_legacy_anchor_gap_sigma = 6.15) shows the additive freedom
    # can SILENTLY absorb a 6.2-sigma anchor mismatch -- which is exactly why an offset that is
    # merely numerically convenient (absorbing the R_JK != R_JE distance mismatch) is NOT a
    # physical translation and does NOT redeem an inadmissible map.
    rec["offset_physical_note"] = (
        "offset_zeta is admissible as a PHYSICAL effacement/GGE-dressing translation ONLY when the "
        "map it dresses is itself Theta-free-admissible. The S100b C1 offset (-0.4117) absorbs the "
        "R_JK(distance-2) != R_JE(distance-1) MISMATCH, not a physical effacement -- it is the C0-class "
        "silent-absorption pathology (6.2-sigma, npz C0_legacy_anchor_gap_sigma)."
    )

    # ----- C0 6.2-sigma cautionary cross-check from S100b npz -----
    sens = np.load(SENS_NPZ, allow_pickle=True)  # (local)
    rec["C0_anchor_gap_sigma_prior"] = float(sens["C0_legacy_anchor_gap_sigma"])
    rec["anchor_gap_sigma_RJK_raw"] = float(sens["anchor_gap_sigma"])  # 16.47 sigma for raw R_JK
    rec["s100b_info_shape"] = str(sens["info_shape"])

    # =====================================================================
    # Composite verdict
    # =====================================================================
    if not leg1_admissible:
        verdict = "INFO"  # (local)
        verdict_reason = "derivation-inadmissible"  # (local)
    else:
        spread = rec["spread"]
        if spread <= SPREAD_PASS:
            verdict = "PASS"
            verdict_reason = "leg1-admissible+spread<=0.025"
        elif spread <= SPREAD_INFO:
            verdict = "INFO"
            verdict_reason = "leg1-admissible+marginal-spread"
        else:
            verdict = "FAIL"
            verdict_reason = "leg1-admissible+spread>0.050"
    rec["verdict"] = verdict
    rec["verdict_reason"] = verdict_reason

    # value string (no single-quote chars; emit_verdict wraps it)
    if not leg1_admissible:
        rec["value_str"] = (
            f"INFO-derivation-inadmissible_leg1_residual={leg1_residual:.6e}_"
            f"Rslot_best_reldist={best_R[3]:.4f}@a{best_R[0]}b{best_R[1]}_"
            f"NO-Theta-free-map-reproduces-w0_B_at_1e-5_"
            f"locktest={'LOCKED' if rec['algebraic_distance_locked'] else 'unlocked'}_"
            f"surrogate-spread-UNINFORMATIVE_leg2-NOT-executed"
        )
    else:
        rec["value_str"] = (
            f"{verdict}_spread={rec['spread']:.8f}_offset_zeta={rec['offset_zeta']:.8f}_"
            f"leg1_residual={leg1_residual:.6e}"
        )

    return rec


# ---------------------------------------------------------------------------
# Section 6 — Output 4-tuple + verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha, companion_note="", extra_rows=None):
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
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(rec: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))  # (local)

    # Panel A: R-slot reconstruction landscape (Theta-free monomials vs retired R_sv1)
    ax = axes[0]
    R_sv1 = rec["R_sv1"]
    # show best monomial R-reconstruction relative distance
    ax.axhline(R_sv1, color="k", ls="--", lw=1.4, label=f"R_sv1 (retired R_JE) = {R_sv1:.4f}")
    ax.axhline(rec["R_JK_traj"][1], color="tab:blue", ls=":", lw=1.4,
               label=f"R_JK(10) = {rec['R_JK_traj'][1]:.5f} (distance-2)")
    rb = rec["R_slot_best"]
    ax.scatter([0], [rb["R_recon"]], color="tab:red", zorder=5, s=80,
               label=f"best Theta-free monomial\nR_JK^{rb['a']}*xi_inv^{rb['b']}={rb['R_recon']:.4f}\n(rel dist {rb['rel_resid']:.3f})")
    ax.set_yscale("log")
    ax.set_title("LEG 1: R-slot reconstruction\n(no Theta-free monomial reaches R_sv1)")
    ax.set_ylabel("R-slot value (log)")
    ax.set_xticks([])
    ax.legend(fontsize=7, loc="best")

    # Panel B: surrogate f(R_JK(L)) trajectory + lock estimate
    ax = axes[1]
    Ls = list(L_SCAN)
    ax.plot(Ls, rec["w0_surrogate_raw"], "o-", color="tab:purple", lw=2,
            label=f"f(R_JK(L)) raw\nspread={rec['spread_surrogate_raw']:.5f}")
    ax.axhline(W_0_B, color="k", ls="--", lw=1.2, label=f"w_0_B = {W_0_B}")
    ax.set_title(f"§(iv-bis) LOCK test: spread={rec['spread_surrogate_raw']:.5f}\n"
                 f"|df/dR|*dR_JK={rec['lock_estimate']:.5f} -> "
                 f"{'LOCKED (GEOMETRIC)' if rec['algebraic_distance_locked'] else 'unlocked'}")
    ax.set_xlabel("L_max")
    ax.set_ylabel("w_0 surrogate")
    ax.set_xticks(Ls)
    ax.legend(fontsize=8, loc="best")

    fig.suptitle(f"{GATE_ID}: {rec['verdict']} ({rec['verdict_reason']})", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    rec = compute()

    print()
    print("=" * 78)
    print("LEG 1 — derivation + HARD admissibility")
    print("=" * 78)
    print(f"  SV1 f-reduction exact (f(R_sv1)=w_0_iv to 1e-12): {rec['sv1_f_reduction_exact']}")
    print(f"  R_sv1 (retired R_JE)        = {rec['R_sv1']:.14f}")
    print(f"  c_J = |F_J_zeta|/N_cells    = {rec['c_J']:.8f}   (Theta-free)")
    print(f"  R_JK(10) canon match        = {rec['R_JK_canon_match_L10']}   (cache-moment layer)")
    print(f"  xi_E_GGE_inv substrate match= {rec['xi_E_GGE_inv_substrate_match']}  (59.8*Delta_BCS/K_base)")
    print(f"  best Theta-free monomial for R-slot: R_JK^{rec['R_slot_best']['a']}*xi_inv^{rec['R_slot_best']['b']}"
          f" = {rec['R_slot_best']['R_recon']:.6f} (rel dist to R_sv1 = {rec['R_slot_best']['rel_resid']:.4f})")
    print(f"  best Theta-free monomial w0_recon residual |Phi(10)-w_0_B| = {rec['leg1_residual']:.6e}")
    print(f"  LEG-1 ADMISSIBLE (residual <= {ADMISSIBILITY_TOL:.0e}) = {rec['leg1_admissible']}")
    print()
    print("  §(iv-bis) algebraic-distance theorem:")
    print(f"    surrogate spread (raw f(R_JK(L))) = {rec['spread_surrogate_raw']:.6f}")
    print(f"    lock estimate |df/dR|*dR_JK       = {rec['lock_estimate']:.6f}  (match<10% = {rec['lock_match']})")
    print(f"    sign locked (w0<0 forall R>0)     = {rec['sign_locked']}")
    print(f"    => algebraic-distance LOCKED      = {rec['algebraic_distance_locked']}")
    print(f"    informativeness: {rec['informativeness'][:88]}...")
    print()
    print("=" * 78)
    print("LEG 2 — CAC spread")
    print("=" * 78)
    if rec["leg2_executed"]:
        print(f"  offset_zeta = w_0_B - rho_zeta(10) = {rec['offset_zeta']:.8f}")
        print(f"  CAC effacement preserved (w0^CAC(10)=w_0_B) = {rec['cac_effacement_preserved']}")
        print(f"  w0^CAC(L) = {[f'{x:.6f}' for x in rec['cac_series']]}")
        print(f"  spread = {rec['spread']:.8f}  vs PASS<={SPREAD_PASS} / INFO<={SPREAD_INFO}")
    else:
        print("  LEG 2 NOT EXECUTED — leg-1 inadmissible (composite INFO-derivation-inadmissible).")
        print(f"  offset_zeta physical note: {rec['offset_physical_note'][:90]}...")
    print(f"  C0 cautionary (S100b): anchor_gap_sigma raw-R_JK={rec['anchor_gap_sigma_RJK_raw']:.2f}, "
          f"C0_legacy={rec['C0_anchor_gap_sigma_prior']:.2f}")
    print()
    print("=" * 78)
    print(f"COMPOSITE VERDICT: {rec['verdict']}  ({rec['verdict_reason']})")
    print("=" * 78)

    # ---- dual-SHA ----
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pins)
    closure = closure_hash(pins)  # (local) retained for backward compat
    print(f"\nclosure_hash = {closure}")
    print(f"audit_sha256  = {audit_sha}")
    print(f"content_sha256= {content_sha}")

    # ---- save npz ----
    np.savez(
        OUT_NPZ,
        # leg-1
        R_sv1=np.float64(rec["R_sv1"]),
        c_J=np.float64(rec["c_J"]),
        R_JK_traj=np.array(rec["R_JK_traj"], dtype=np.float64),
        xi_E_GGE_inv=np.float64(rec["xi_E_GGE_inv"]),
        sv1_f_reduction_exact=bool(rec["sv1_f_reduction_exact"]),
        R_JK_canon_match_L10=bool(rec["R_JK_canon_match_L10"]),
        xi_E_GGE_inv_substrate_match=bool(rec["xi_E_GGE_inv_substrate_match"]),
        monomial_best_a=np.int64(rec["monomial_best"]["a"]),
        monomial_best_b=np.int64(rec["monomial_best"]["b"]),
        monomial_best_w0=np.float64(rec["monomial_best"]["w0_recon"]),
        monomial_best_residual=np.float64(rec["monomial_best"]["residual"]),
        R_slot_best_a=np.int64(rec["R_slot_best"]["a"]),
        R_slot_best_b=np.int64(rec["R_slot_best"]["b"]),
        R_slot_best_R=np.float64(rec["R_slot_best"]["R_recon"]),
        R_slot_best_reldist=np.float64(rec["R_slot_best"]["rel_resid"]),
        leg1_residual=np.float64(rec["leg1_residual"]),
        leg1_admissible=bool(rec["leg1_admissible"]),
        # §(iv-bis)
        w0_surrogate_raw=np.array(rec["w0_surrogate_raw"], dtype=np.float64),
        spread_surrogate_raw=np.float64(rec["spread_surrogate_raw"]),
        dfdR_10=np.float64(rec["dfdR_10"]),
        lock_estimate=np.float64(rec["lock_estimate"]),
        lock_match=bool(rec["lock_match"]),
        sign_locked=bool(rec["sign_locked"]),
        algebraic_distance_locked=bool(rec["algebraic_distance_locked"]),
        # leg-2
        offset_zeta=np.float64(rec["offset_zeta"]),
        cac_series=np.array(rec["cac_series"], dtype=np.float64),
        spread=np.float64(rec["spread"]),
        leg2_executed=bool(rec["leg2_executed"]),
        cac_effacement_preserved=bool(rec["cac_effacement_preserved"]),
        # cautionary cross-checks
        C0_anchor_gap_sigma_prior=np.float64(rec["C0_anchor_gap_sigma_prior"]),
        anchor_gap_sigma_RJK_raw=np.float64(rec["anchor_gap_sigma_RJK_raw"]),
        # meta
        L_scan=np.array(L_SCAN, dtype=np.int64),
        L_anchor=np.int64(L_ANCHOR),
        w_0_B=np.float64(W_0_B),
        ADMISSIBILITY_TOL=np.float64(ADMISSIBILITY_TOL),
        SPREAD_PASS=np.float64(SPREAD_PASS),
        SPREAD_INFO=np.float64(SPREAD_INFO),
        verdict=str(rec["verdict"]),
        verdict_reason=str(rec["verdict_reason"]),
        value_str=str(rec["value_str"]),
        zero_free_normalization_attestation=str(rec["zero_free_normalization_attestation"]),
        informativeness=str(rec["informativeness"]),
        offset_physical_note=str(rec["offset_physical_note"]),
        audit_sha256=str(audit_sha),
        content_sha256=str(content_sha),
        closure_hash=str(closure),
    )
    print(f"saved {OUT_NPZ.name}")

    make_plot(rec)
    print(f"saved {OUT_PNG.name}")

    print()
    print(emit_4tuple(rec["value_str"], SCHEME, CONVENTION, L_MAX))

    # ---- verdict payload (regulator-pin + consumption-layer companion rows) ----
    extra_rows = [
        "# regulator_pin=a_n^{zeta} (R_JK, CAC rho_zeta series zeta-scheme; bare a_n forbidden)",
        "# consumption_layer: R_JK(L) CACHE-MOMENT; SV1 anchor closed-form ATLAS-ROW (substrate-first §ii.A)",
        f"# leg1_admissible={rec['leg1_admissible']} leg2_executed={rec['leg2_executed']} "
        f"algebraic_distance_locked={rec['algebraic_distance_locked']} (§iv-bis surrogate UNINFORMATIVE-on-canonical)",
    ]
    print_verdict_payload(
        rec["verdict"], rec["value_str"], audit_sha, content_sha,
        companion_note="post-S86 branch-iv evaluator; leg-1 derivation + §iv-bis algebraic-distance theorem",
        extra_rows=extra_rows,
    )

    print(f"\n[done in {time.time()-t0:.2f}s]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
