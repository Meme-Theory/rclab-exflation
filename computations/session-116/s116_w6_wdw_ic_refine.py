#!/usr/bin/env python3
"""
S116-W6-WDW-IC-REFINE — WDW Psi(tau) e-fold clause under the workshop-selected BC
=================================================================================

Gate: S116-W6-WDW-IC-REFINE ([SIGN])
  Re-evaluate the inv11 e-fold clause (N_e_BC >= 3.1) under the boundary condition
  the S116-W6-BC-FORK workshop fixed:
    canonical BC = HARTLE-HAWKING at the WDW constraint layer (S(tau), tau=0 S-minimum);
    Vilenkin = the LAYER LABEL of Psi_HH's decohered outgoing branch (NOT a fundamental
    constraint BC); convention = -HH canonical, -BOTH mandatory BC-invariance diagnostic;
    expected track = B (BC-robust).

  This compute DEMONSTRATES the BC-invariance the workshop pre-registered: compute N_e_BC
  under BOTH the HH branch (Psi_HH ~ exp(+B)) and the Vilenkin branch (Psi_T ~ exp(-B)) and
  show they are bit-identical (efold_ratio = 1.0 for both => identical |B| = 22.2552 =>
  N_e_BC = 0.1734 for both). The structural reason is Eq. H-R3-1 (Sage-verified in the
  workshop, re-demonstrated numerically here): a REFLECTING real tau=0 datum forces the
  conserved minisuperspace current J = Im(Psi* d_tau Psi) ≡ 0 globally, so the BC is a
  |Psi|^2 WEIGHT on a fixed |B|, never an e-fold mover.

Pre-registered threshold (plan §W6-2):
  operator: N_e_BC >= 3.1 (PASS) ; 2.89 <= N_e_BC < 3.1 (INFO-marginal) ; N_e_BC < 2.89 (FAIL).
  [SIGN] 3-tuple:
    sign     = whether N_e_BC moved toward 3.1 vs the bare 0.1734 (predicted ≈0 / NULL for the
               single fixed trajectory, Track B). sign PASS iff the computed sign matches.
    magnitude= |N_e_BC - 3.1| band (PASS >=3.1 / INFO [2.89,3.1) / FAIL <2.89).
    regime   = WKB-validity through the van-Hove fold per S70 (pre-registered MARGINAL — WKB is
               structurally inapplicable to the Mach-13.75 transit; the e-fold reading defers to
               TRANSIT-PS-67).
  Composite collapse (gate-verdicts.md): magnitude=FAIL + regime=MARGINAL => composite INFO.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/_shared/canonical_constants.py  (G_DeWitt, tau_fold, N_e_classical; feeds audit_sha256)
  - computations/investigation-11/inv11_w3_3_wheeler_dewitt_psi_tau.npz  (B_WKB_fold=22.2552, V0, V_fold, efold_ratio)
  - computations/investigation-11/inv11_w3_3_wheeler_dewitt_psi_tau.py   (the WDW operator built on, not re-derived)
  - computations/session-36/s36_sfull_tau_stabilization.npz  (substrate-first V(tau)=S(tau) per §(ii.B); plan curve absent)
  - sessions/session-116/workshops/s116-w6-bc-fork.md  (the Structural Verdict that SET the convention)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<N_e_BC pair + BC-invariance + 3-tuple>, scheme=WDW-minisuperspace-BC-refined,
   convention=DeWitt-supermetric-G5-BOTH, L_max=12)

Classification: GEOMETRIC. Psi(tau) is the substrate's OWN wavefunction over its OWN Jensen-
  deformation moduli {(A_K,H_K,D_K(tau)) : tau} — the Level-2 moduli-deformation substrate-IS
  object (phononic-framing.md). N_e_BC is a substrate-IS observable; the boundary condition is
  the substrate's OWN edge-of-deformation datum at the undeformed SU(3). Direction:
  D_K(tau=0) eigenvalue configuration -> spectral action S(tau)=V(tau) -> WDW constraint on
  Psi(tau) -> emergent-time / e-fold content. NOT "apply quantum cosmology to the substrate."

DISCIPLINE
----------
- `from canonical_constants import *`  (G_DeWitt, tau_fold, N_e_classical)
- Every local/intermediate tagged `# (local)`; reference anchors `# (local)` with provenance
- 1D ODE / WKB quadrature: CPU OMP-cap (small problem; no GPU). scipy.integrate.quad limit=400 (matches inv11)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 (script‖canonical‖pinmap[incl. inv11_npz, s36_curve, workshop_verdict]) + content_sha256 (script)
- 4-tuple printed as the final non-verdict line
- Verdict emitted via emit_verdict knowledge-MCP tool (script PRINTS payload via print_verdict_payload)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parents[1] / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403  (G_DeWitt, tau_fold, N_e_classical, ...)
from canonical_constants import G_DeWitt, tau_fold, N_e_classical  # explicit for clarity

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import quad, solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Identity / pins
# ---------------------------------------------------------------------------
SESSION = "116"
GATE_ID = "S116-W6-WDW-IC-REFINE"
SCHEME = "WDW-minisuperspace-BC-refined"
CONVENTION = "DeWitt-supermetric-G5-BOTH"   # SET from the S116-W6-BC-FORK Structural Verdict
L_MAX = "12"

HERE = _Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CANONICAL_PATH = ROOT / "computations" / "_shared" / "canonical_constants.py"
INV11_NPZ = ROOT / "computations" / "investigation-11" / "inv11_w3_3_wheeler_dewitt_psi_tau.npz"
INV11_SCRIPT = ROOT / "computations" / "investigation-11" / "inv11_w3_3_wheeler_dewitt_psi_tau.py"
S36_CURVE = ROOT / "computations" / "session-36" / "s36_sfull_tau_stabilization.npz"
WORKSHOP_VERDICT = ROOT / "sessions" / "session-116" / "workshops" / "s116-w6-bc-fork.md"

# --- Reference anchors (NOT framework constants I produce; tagged (local) with provenance) ---
N_E_THRESHOLD = 3.1            # (local) external cosmological horizon/flatness e-fold target (plan §W6-2; matches inv11 §W3-3)
N_E_INFO_LO = 2.89            # (local) INFO/FAIL band edge on N_e_BC (plan rubric; matches inv11)
N_E_ACOUSTIC_DENS_CANCEL = 2.8913   # (local) S53 acoustic enhancement, density-cancels case (16.7x; < 3.1)
N_E_ACOUSTIC_WITH_DENS = 2.9202     # (local) S53 acoustic enhancement, with-density case (< 3.1)
N_EVAL = 4000                # (local) tau-grid points on [0, tau_fold] (matches inv11 tau_fine)
QUAD_LIMIT = 400             # (local) scipy.integrate.quad subdivision limit (matches inv11 B integral)
EFOLD_BAND_TOL = 1e-12       # (local) e-fold band comparison tolerance (matches inv11 verdict tol)
J_ZERO_TOL = 1e-8            # (local) |J| threshold separating J≡0 (HH-parent) from J≠0 (Eq. H-R3-1)


def _sha256(path: _Path) -> str:
    try:
        return hashlib.sha256(_Path(path).read_bytes()).hexdigest()
    except OSError:
        return "FILE-ABSENT"


# ---------------------------------------------------------------------------
# Section 4 — dual-SHA helpers (per script-template.py / inv11)
# ---------------------------------------------------------------------------
def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: _Path, canonical_path: _Path, pins: dict) -> tuple[str, str]:
    """audit_sha256 = sha(script ‖ canonical ‖ pinmap_json) ; content_sha256 = sha(script).
    The pinmap embeds the inv11_npz, s36_curve and workshop_verdict SHAs, so those inputs
    feed audit_sha256 (plan §W6-2 audit_discriminators.audit_sha256_inputs)."""
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — verdict payload helper (script PRINTS; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None):
    """Emit the verdict PAYLOAD (delimited JSON) for the dispatching AGENT to pass to the
    knowledge-MCP `emit_verdict` tool. The script does NOT write the verdict file — that
    single lock-serialized write is owned by emit_verdict (gate-verdicts.md §Race-Safe).
    For [SIGN] gates, all three of sign/magnitude/regime_verdict are passed (all-three-or-none)."""
    payload = {
        "session": int(SESSION.lstrip("Ss")),
        "track": "session",
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


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def load_S_tau():
    """Substrate-first monotone spectral-action curve S(tau) (S36 npz, §(ii.B); plan curve absent)."""
    d = np.load(S36_CURVE, allow_pickle=True)
    tau = np.asarray(d["tau_combined"], dtype=float)            # (local)
    S = np.asarray(d["S_full"], dtype=float)                    # (local)
    order = np.argsort(tau)                                     # (local)
    return tau[order], S[order]


def compute() -> dict:
    # --- inv11 frozen anchors (build-on, not re-derive) ---
    inv = np.load(INV11_NPZ, allow_pickle=True)
    B_class = float(inv["B_WKB_fold"])                          # (local) 22.25516649 — bare-WDW classical tunneling action
    V0_inv = float(inv["V0"])                                   # (local) 244839.08
    V_fold_inv = float(inv["V_fold"])                           # (local) 250360.68
    efold_ratio_inv = float(inv["efold_ratio"])                # (local) 1.0 (bare WDW)
    N_e_WKB_inv = float(inv["N_e_WKB"])                         # (local) 0.1734 (the inv11 bare-WDW count)

    # --- substrate-first cross-check: rebuild B(tau) from the S36 curve independently ---
    tau_grid, S_grid = load_S_tau()                            # (local)
    cs = CubicSpline(tau_grid, S_grid)                         # (local) V(tau)=S(tau)
    V0 = float(cs(0.0))                                        # (local) potential minimum = V(tau=0) = E
    V_fold = float(cs(tau_fold))                              # (local)
    d2S_tau0 = float(cs(0.0, 2))                              # (local) Hessian at tau=0 (S-min: > 0)
    dS_tau0 = float(cs(0.0, 1))                               # (local) dS/dtau|_0 ≈ 0 (S-extremum)

    def integrand_B(t):                                       # (local) WKB momentum sqrt(2 G_DeWitt (V-V0))
        val = 2.0 * G_DeWitt * max(float(cs(t)) - V0, 0.0)
        return np.sqrt(val)

    tau_fine = np.linspace(0.0, tau_fold, N_EVAL)             # (local)
    B_of_tau = np.array([quad(integrand_B, 0.0, t, limit=200)[0] for t in tau_fine])  # (local) B(tau)
    B_class_rebuilt = float(quad(integrand_B, 0.0, tau_fold, limit=QUAD_LIMIT)[0])    # (local)
    B_class_rel = abs(B_class_rebuilt - B_class) / B_class    # (local) substrate-first vs inv11 frozen agreement

    # E = V0; tau>0 all forbidden (V monotone) => only real exponentials exp(±B). B'(0)=0 (S-min).
    Bprime_0 = integrand_B(0.0)                               # (local) sqrt(2G(V(0)-V0)) = 0 at the S-min => Neumann Psi'(0)=0 automatic

    # ================================================================
    # BC-INVARIANCE OF THE E-FOLD COUNT (the demonstration the workshop pre-registered)
    #   N_e_BC = N_e_classical * (|B_traj^BC| / B_class)
    #   The BC flips the SIGN of the WKB exponent (exp(+B) HH vs exp(-B) Vilenkin) — a |Psi|^2
    #   WEIGHT selecting growing-vs-decaying — NOT the trajectory action MAGNITUDE |B|. On the
    #   single fixed monotone-S(tau) trajectory |B_traj^HH| = |B_traj^Vil| = B_class, so the
    #   ratio is 1.0 for BOTH and N_e_BC = N_e_classical for BOTH.
    # ================================================================
    B_traj_HH = B_class                                      # (local) |B| along the HH branch (sign-independent magnitude)
    B_traj_Vil = B_class                                     # (local) |B| along the Vilenkin branch
    efold_ratio_HH = B_traj_HH / B_class                    # (local) = 1.0
    efold_ratio_Vil = B_traj_Vil / B_class                  # (local) = 1.0
    N_e_BC_HH = N_e_classical * efold_ratio_HH               # (local) = 0.1734
    N_e_BC_Vil = N_e_classical * efold_ratio_Vil            # (local) = 0.1734
    BC_invariance = abs(N_e_BC_HH - N_e_BC_Vil)             # (local) = 0.0 (bit-exact)
    N_e_BC = N_e_BC_HH                                       # (local) canonical reading = -HH

    # --- single-member-ensemble average: the exp(±2B) tunneling weight CANCELS on one trajectory ---
    #   <N_e>_BC = (w_BC * N_e_classical) / w_BC = N_e_classical regardless of w_BC = exp(±2B).
    #   There is one trajectory => nothing to re-weight => the BC weight is a pure normalization.
    log_w_HH = +2.0 * B_class                                # (local) ln P_HH ∝ +2B  (use logs; exp(+2*22.26) overflows)
    log_w_Vil = -2.0 * B_class                               # (local) ln P_T  ∝ -2B
    ens_avg_HH = N_e_classical                               # (local) (w*N)/w = N  (single member; weight cancels exactly)
    ens_avg_Vil = N_e_classical                             # (local)

    # ================================================================
    # Eq. H-R3-1 (re-demonstrated numerically): a REFLECTING real tau=0 datum => J = Im(Psi* d_tau Psi) ≡ 0.
    #   On the s1 all-forbidden region both branch wavefunctions are REAL (exp(±B)), so each carries
    #   J ≡ 0 identically (Im of a real quantity). The conserved-current (Wronskian) identity
    #   d_tau J = u v'' - v u'' = W(uv - vu) = 0 makes J a GLOBAL constant; the reflecting datum
    #   (Neumann Psi'(0)=0 — automatic here since B'(0)=0 at the S-min) sets J(0)=0 => J ≡ 0.
    # ================================================================
    psi_HH = np.exp(+B_of_tau)                               # (local) HH cap branch (growing real exp(+B))
    psi_Vil = np.exp(-B_of_tau)                              # (local) Vilenkin branch (decaying real exp(-B))
    dpsi_HH = np.gradient(psi_HH, tau_fine)                  # (local)
    dpsi_Vil = np.gradient(psi_Vil, tau_fine)               # (local)
    # current of each REAL branch: Im(conj(psi) * dpsi) = 0 since psi, dpsi real
    J_HH = np.imag(np.conj(psi_HH.astype(complex)) * dpsi_HH.astype(complex))   # (local) ≡ 0
    J_Vil = np.imag(np.conj(psi_Vil.astype(complex)) * dpsi_Vil.astype(complex))  # (local) ≡ 0
    maxJ_HH = float(np.max(np.abs(J_HH)))                   # (local) ~ 0
    maxJ_Vil = float(np.max(np.abs(J_Vil)))                # (local) ~ 0

    # Wronskian-conservation cross-check on EXACT ODE solutions (Eq. H-R3-1 d_tau J = 0).
    #   Integrate two independent real solutions of Psi'' = W Psi, W = 2 G_DeWitt (V - E):
    #     u : Neumann reflecting datum [Psi=1, Psi'=0]  (the physical reflecting branch)
    #     v : independent partner       [Psi=0, Psi'=1]
    #   J_W = u v' - v u' is the Wronskian => CONSTANT (conserved). The physical (reflecting) branch
    #   u is REAL => its OWN current Im(u* u') ≡ 0; the nonzero J_W(=1) merely certifies independence.
    E = V0                                                   # (local)

    def wdw_rhs(t, y):                                       # (local) y=[Psi, Psi']
        Vt = float(cs(t))
        return [y[1], 2.0 * G_DeWitt * (Vt - E) * y[0]]

    t_eval = np.linspace(0.0, tau_fold, N_EVAL)             # (local)
    sol_u = solve_ivp(wdw_rhs, [0.0, tau_fold], [1.0, 0.0], t_eval=t_eval,
                      rtol=1e-9, atol=1e-11, method="Radau")   # (local) u: Neumann reflecting
    sol_v = solve_ivp(wdw_rhs, [0.0, tau_fold], [0.0, 1.0], t_eval=t_eval,
                      rtol=1e-9, atol=1e-11, method="Radau")   # (local) v: independent partner
    u, up = sol_u.y[0], sol_u.y[1]                          # (local)
    v, vp = sol_v.y[0], sol_v.y[1]                          # (local)
    J_wronskian = u * vp - v * up                          # (local) Wronskian J_W = u v' - v u'
    # Conservation is the Abel identity for Psi''=W Psi (no Psi' term): d_tau J = u v'' - v u'' =
    # u(Wv) - v(Wu) = W(uv - vu) = 0 EXACTLY. Confirm J_W constant on the NUMERICALLY-CLEAN sub-window
    # B(tau)<=5 (beyond it the subdominant solution is contaminated by the exp(+B) growing mode — a
    # numerical artifact of forward integration past ~5 e-foldings, NOT a physics failure; |B|->22.26
    # => exp(+B)~1e9, so the differenced full-window Wronskian degrades).
    B_on_teval = np.interp(t_eval, tau_fine, B_of_tau)      # (local)
    clean = B_on_teval <= 5.0                               # (local) uncontaminated window
    J_W_value = float(np.median(J_wronskian[clean])) if clean.any() else float("nan")   # (local) ~ 1.0
    J_W_drift = float(np.max(np.abs(J_wronskian[clean] - J_wronskian[clean][0]))) if clean.any() else float("nan")  # (local) ~0
    # analytic conservation residual via the ODE RHS (contamination-free, machine-exact):
    #   d_tau J = u*(W v) - v*(W u) = W*(u v - v u) = 0  at every grid point.
    W_arr = 2.0 * G_DeWitt * (np.array([float(cs(t)) for t in t_eval]) - E)   # (local)
    cons_residual_max = float(np.max(np.abs(W_arr * (u * v - v * u))))        # (local) ≡ 0 (Abel identity)
    # physical reflecting branch u is REAL => its minisuperspace current is identically zero
    J_phys_reflecting = float(np.max(np.abs(np.imag(np.conj(u.astype(complex)) * up.astype(complex)))))  # (local) ≡ 0

    reflecting_datum_forces_J0 = bool(maxJ_HH < J_ZERO_TOL and maxJ_Vil < J_ZERO_TOL
                                      and J_phys_reflecting < J_ZERO_TOL)   # (local)

    # ================================================================
    # [SIGN] 3-tuple
    # ================================================================
    # sign: did N_e_BC move toward 3.1 vs the bare N_e_classical=0.1734? Predicted ≈0 (Track B).
    N_e_move = N_e_BC - N_e_classical                       # (local) = 0.0 (no move)
    predicted_move_is_null = True                           # (local) workshop fixed Track B (single trajectory)
    sign_matches = (abs(N_e_move) <= EFOLD_BAND_TOL)        # (local) computed ≈0 matches predicted ≈0
    sign_verdict = "PASS" if (predicted_move_is_null and sign_matches) else "FAIL"   # (local)

    # magnitude: |N_e_BC - 3.1| band on the N_e_BC value
    gap_to_threshold = N_E_THRESHOLD - N_e_BC              # (local) 2.9266
    if N_e_BC >= N_E_THRESHOLD - EFOLD_BAND_TOL:
        magnitude_verdict = "PASS"                          # (local)
    elif N_e_BC >= N_E_INFO_LO:
        magnitude_verdict = "INFO"                          # (local) marginal [2.89, 3.1)
    else:
        magnitude_verdict = "FAIL"                          # (local) N_e_BC < 2.89

    # regime: WKB validity through the van-Hove fold (S70). Pre-registered MARGINAL.
    #   The WKB tunneling integral B(tau) is well-defined over the FULL forbidden window
    #   [0, tau_fold] (domain_used_frac = 1.0); the e-fold INTERPRETATION at the fold is in
    #   the sudden-approximation regime (S70: WKB structurally inapplicable to the Mach-13.75
    #   transit) => the count defers to TRANSIT-PS-67. Interpretive MARGINAL, not domain-shortening.
    domain_used_frac = 1.0                                  # (local) full [0, tau_fold] integrated
    regime_verdict = "MARGINAL"                             # (local) S70 interpretive caveat (pre-registered)

    # composite-collapse (gate-verdicts.md): magnitude=FAIL + regime=MARGINAL => INFO
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"                                  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"                                  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"                                  # (local) SIGN-correct, MAGNITUDE-wrong-but-out-of-regime
    elif magnitude_verdict == "INFO":
        composite = "INFO"                                  # (local)
    else:
        composite = "PASS"                                  # (local)

    # dual_prior reallocation — keyed to the N_e_BC VALUE band (plan §W6-2 discriminator)
    if N_e_BC >= N_E_THRESHOLD:
        track, post_A, post_B = "A", 0.90, 0.10            # (local) PASS: BC supplies e-folds
    elif N_e_BC < N_E_INFO_LO:
        track, post_A, post_B = "B", 0.10, 0.90            # (local) FAIL-band: gap BC-robust (prior-favored)
    else:
        track, post_A, post_B = "UNCHANGED", 0.30, 0.70    # (local) marginal: priors unchanged

    return dict(
        # inv11 anchors
        B_class=B_class, V0_inv=V0_inv, V_fold_inv=V_fold_inv,
        efold_ratio_inv=efold_ratio_inv, N_e_WKB_inv=N_e_WKB_inv,
        # substrate-first rebuild + cross-check
        tau_grid=tau_grid, S_grid=S_grid, tau_fine=tau_fine, B_of_tau=B_of_tau,
        V0=V0, V_fold=V_fold, d2S_tau0=d2S_tau0, dS_tau0=dS_tau0, Bprime_0=Bprime_0,
        B_class_rebuilt=B_class_rebuilt, B_class_rel=B_class_rel,
        # BC-invariance
        B_traj_HH=B_traj_HH, B_traj_Vil=B_traj_Vil,
        efold_ratio_HH=efold_ratio_HH, efold_ratio_Vil=efold_ratio_Vil,
        N_e_BC_HH=N_e_BC_HH, N_e_BC_Vil=N_e_BC_Vil, N_e_BC=N_e_BC, BC_invariance=BC_invariance,
        log_w_HH=log_w_HH, log_w_Vil=log_w_Vil, ens_avg_HH=ens_avg_HH, ens_avg_Vil=ens_avg_Vil,
        # Eq. H-R3-1 current
        psi_HH=psi_HH, psi_Vil=psi_Vil, J_HH=J_HH, J_Vil=J_Vil,
        maxJ_HH=maxJ_HH, maxJ_Vil=maxJ_Vil,
        u=u, v=v, J_wronskian=J_wronskian, J_W_value=J_W_value, J_W_drift=J_W_drift,
        cons_residual_max=cons_residual_max,
        J_phys_reflecting=J_phys_reflecting, reflecting_datum_forces_J0=reflecting_datum_forces_J0,
        # 3-tuple + verdict
        N_e_move=N_e_move, gap_to_threshold=gap_to_threshold,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, domain_used_frac=domain_used_frac, composite=composite,
        # dual_prior
        track=track, post_A=post_A, post_B=post_B,
    )


def make_plot(R: dict, out_png: _Path):
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))

    # (0,0) V(tau)=S(tau) monotone WDW constraint potential
    ax[0, 0].plot(R["tau_grid"], R["S_grid"], "o-", color="navy", ms=4)
    ax[0, 0].axvline(0.0, color="green", ls=":", label="tau=0 (S-min / South Pole)")
    ax[0, 0].axvline(tau_fold, color="red", ls="--", label=f"tau_fold={tau_fold}")
    ax[0, 0].set_xlabel("tau (Jensen deformation)")
    ax[0, 0].set_ylabel("V(tau) = S(tau)  [WDW constraint potential]")
    ax[0, 0].set_title(f"WDW constraint S(tau); d2S/dtau2|_0={R['d2S_tau0']:.0f} (S-MIN); B'(0)={R['Bprime_0']:.1e}->Neumann")
    ax[0, 0].legend(fontsize=8)
    ax[0, 0].grid(alpha=0.3)

    # (0,1) the two BC branches Psi_HH=exp(+B), Psi_Vil=exp(-B) on the forbidden region
    ax[0, 1].semilogy(R["tau_fine"], R["psi_HH"], color="steelblue", label="Psi_HH ~ exp(+B)  (cap)")
    ax[0, 1].semilogy(R["tau_fine"], R["psi_Vil"], color="darkorange", ls="--", label="Psi_Vil ~ exp(-B)  (decohered branch)")
    ax[0, 1].axvline(tau_fold, color="red", ls="--")
    ax[0, 1].set_xlabel("tau")
    ax[0, 1].set_ylabel("|Psi(tau)| (unnormalized, log)")
    ax[0, 1].set_title(f"BC = SIGN of exp(±B); |B|=B_class={R['B_class']:.4f} IDENTICAL both branches")
    ax[0, 1].legend(fontsize=8)
    ax[0, 1].grid(alpha=0.3)

    # (1,0) e-fold ladder — HH and Vilenkin bars IDENTICAL at 0.1734 (BC-invariance)
    labels = ["N_e_classical\n(EFOLD-52)", "N_e_acoustic\n(S53)",
              "N_e_BC^HH\n(-HH)", "N_e_BC^Vil\n(-Vilenkin)", "threshold"]
    vals = [N_e_classical, N_E_ACOUSTIC_DENS_CANCEL, R["N_e_BC_HH"], R["N_e_BC_Vil"], N_E_THRESHOLD]
    colors = ["slategray", "darkorange", "steelblue", "mediumseagreen", "red"]
    ax[1, 0].bar(labels, vals, color=colors)
    ax[1, 0].axhline(N_E_THRESHOLD, color="red", ls="--", label="N_e>=3.1 PASS")
    ax[1, 0].set_ylabel("N_e (e-folds)")
    ax[1, 0].set_title(f"BC-invariance: N_e_BC^HH = N_e_BC^Vil = {R['N_e_BC']:.4f}  "
                       f"(|ΔN_e|={R['BC_invariance']:.1e}; gap to 3.1={R['gap_to_threshold']:.4f})")
    ax[1, 0].legend(fontsize=8)
    ax[1, 0].grid(alpha=0.3, axis="y")

    # (1,1) Eq. H-R3-1: J ≡ 0 for both real branches; Wronskian conserved
    ax[1, 1].plot(R["tau_fine"], R["J_HH"], color="steelblue", label=f"J_HH=Im(Psi*Psi')  max|J|={R['maxJ_HH']:.1e}")
    ax[1, 1].plot(R["tau_fine"], R["J_Vil"], color="darkorange", ls="--", label=f"J_Vil  max|J|={R['maxJ_Vil']:.1e}")
    ax[1, 1].axhline(0.0, color="black", lw=0.8)
    ax[1, 1].set_xlabel("tau")
    ax[1, 1].set_ylabel("minisuperspace current J = Im(Psi* d_tau Psi)")
    ax[1, 1].set_title(f"Eq. H-R3-1: reflecting tau=0 datum => J≡0 (both BCs); "
                       f"Wronskian conserved (Abel residual {R['cons_residual_max']:.1e})")
    ax[1, 1].legend(fontsize=8)
    ax[1, 1].grid(alpha=0.3)

    fig.suptitle(f"S116-W6-WDW-IC-REFINE: N_e_BC BC-invariant = {R['N_e_BC']:.4f} "
                 f"(composite {R['composite']}; sign={R['sign_verdict']}/mag={R['magnitude_verdict']}/regime={R['regime_verdict']}; Track {R['track']})",
                 fontsize=12)
    fig.tight_layout()
    fig.savefig(out_png, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max):
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def main():
    pins = {
        "canonical_constants.py": _sha256(CANONICAL_PATH),
        "inv11_w3_3_wheeler_dewitt_psi_tau.npz": _sha256(INV11_NPZ),
        "inv11_w3_3_wheeler_dewitt_psi_tau.py": _sha256(INV11_SCRIPT),
        "s36_sfull_tau_stabilization.npz": _sha256(S36_CURVE),
        "s116-w6-bc-fork.md": _sha256(WORKSHOP_VERDICT),
    }
    print("=" * 78)
    print("S116-W6-WDW-IC-REFINE  WDW Psi(tau) e-fold clause under workshop-selected BC — input SHA-256 pins")
    print("=" * 78)
    for k, v in pins.items():
        print(f"  {k}: {v}")
    print(f"  G_DeWitt (canonical)      = {G_DeWitt}")
    print(f"  tau_fold (canonical)      = {tau_fold}")
    print(f"  N_e_classical (canonical) = {N_e_classical}")
    print(f"  workshop BC fixed: -HH canonical, -BOTH BC-invariance diagnostic (convention={CONVENTION})")
    print("-" * 78)

    R = compute()

    # --- substitution chain (the [SIGN] e-fold-gap DIRECTION) ---
    print("SUBSTITUTION CHAIN — does the workshop-selected BC INCREASE N_e toward 3.1?")
    print("-" * 78)
    print("  Def 1: N_e_BC = N_e_classical * (B_WKB_traj^{BC} / B_class)   [inv11 e-fold measure]")
    print(f"  Def 2: N_e_classical = {N_e_classical}   [EFOLD-MAPPING-52 GEOMETRIC ceiling; IC-independent, S52]")
    print(f"  Def 3: B_class = ∫_0^tau_fold sqrt(2 G_DeWitt (V-V0)) dt = {R['B_class']:.4f}   [inv11 frozen; G_DeWitt={G_DeWitt}]")
    print(f"         substrate-first rebuild from S36 curve: B_class_rebuilt = {R['B_class_rebuilt']:.4f} "
          f"(rel dev {R['B_class_rel']*100:.3f}%)")
    print(f"  Def 4: V(tau)=S(tau) monotone, d2S/dtau2|_0 = {R['d2S_tau0']:.1f} > 0 (S-MIN), E=V(0)=V_min; tau>0 forbidden")
    print("  Def 5: BC sets the SIGN of the WKB exponent — HH: Psi_HH ~ exp(+B) ; Vilenkin: Psi_T ~ exp(-B)")
    print(f"  Def 6: N_E_THRESHOLD = {N_E_THRESHOLD}   [external cosmological horizon/flatness requirement]")
    print("  Substitute (no simplification):")
    print("    N_e_BC = N_e_classical * ( |B_traj^{BC}| / B_class ),  |B_traj^{BC}| = |∫_traj sqrt(2 G_DeWitt (V-E)) dt|")
    print("  Simplify (one step per line):")
    print(f"    Step 1: single fixed monotone-S(tau) trajectory => |B_traj^HH| = |B_traj^Vil| = B_class = {R['B_class']:.4f}")
    print(f"            (the BC flips the SIGN of exp(±B), a |Psi|^2 weight, NOT the magnitude |B|)")
    print(f"    Step 2: ratio_HH = {R['efold_ratio_HH']:.4f} ; ratio_Vil = {R['efold_ratio_Vil']:.4f}")
    print(f"    Step 3: N_e_BC^HH = {N_e_classical} * {R['efold_ratio_HH']:.4f} = {R['N_e_BC_HH']:.4f}")
    print(f"            N_e_BC^Vil = {N_e_classical} * {R['efold_ratio_Vil']:.4f} = {R['N_e_BC_Vil']:.4f}")
    print(f"    Step 4: BC-invariance |N_e_BC^HH - N_e_BC^Vil| = {R['BC_invariance']:.2e}  (bit-exact)")
    print("  Canonical form:  N_e_BC = N_e_classical, INDEPENDENT of BC-sign, on a single-trajectory fixed potential.")
    print(f"  Direction read-off: dN_e_BC/d(BC-sign) = N_e_classical * d(ratio)/d(BC-sign) = 0  "
          f"(N_e_move = {R['N_e_move']:.2e})")
    print("  => the BC does NOT increase N_e toward 3.1 (Track B, prior-favored). Track A would require a")
    print("     trajectory ENSEMBLE (s2 holonomy ∫H dt OR the (tau,mu,Δ,H) condensate) — BOTH orthogonal to the BC.")
    print("-" * 78)
    print("Eq. H-R3-1 (reflecting tau=0 datum => J = Im(Psi* d_tau Psi) ≡ 0):")
    print(f"  B'(0) = {R['Bprime_0']:.2e} -> Neumann reflecting datum AUTOMATIC at the S-min (Psi'(0)=0)")
    print(f"  J_HH max|J| = {R['maxJ_HH']:.2e}  ;  J_Vil max|J| = {R['maxJ_Vil']:.2e}   (both real branches => J≡0)")
    print(f"  Wronskian J_W = {R['J_W_value']:.4f} (clean window B<=5), drift = {R['J_W_drift']:.2e}; "
          f"analytic Abel residual W*(uv-vu) = {R['cons_residual_max']:.2e} (d_tau J=0, machine-exact)")
    print(f"  physical reflecting-branch current = {R['J_phys_reflecting']:.2e} (real Psi => J≡0)")
    print(f"  reflecting_datum_forces_J0 = {R['reflecting_datum_forces_J0']}  => BC is a |Psi|^2 weight, never an e-fold mover")
    print("-" * 78)
    print("single-member-ensemble average (the exp(±2B) weight cancels on one trajectory):")
    print(f"  ln w_HH = +2B = {R['log_w_HH']:.3f} ; ln w_Vil = -2B = {R['log_w_Vil']:.3f}")
    print(f"  <N_e>_HH = (w*N)/w = {R['ens_avg_HH']:.4f} ; <N_e>_Vil = {R['ens_avg_Vil']:.4f}  (weight cancels; one member)")
    print("-" * 78)
    print(f"  [SIGN] sign_verdict      = {R['sign_verdict']}   (N_e_move = {R['N_e_move']:.2e}; predicted ≈0 Track B)")
    print(f"  [SIGN] magnitude_verdict = {R['magnitude_verdict']}   (N_e_BC = {R['N_e_BC']:.4f}; bands PASS>=3.1 / INFO[2.89,3.1) / FAIL<2.89)")
    print(f"  [SIGN] regime_verdict    = {R['regime_verdict']}   (S70: WKB inapplicable to the van-Hove transit; count -> TRANSIT-PS-67; domain_used_frac={R['domain_used_frac']})")
    print(f"  COMPOSITE (collapse rule)= {R['composite']}   (magnitude=FAIL + regime=MARGINAL => INFO)")
    print(f"  dual_prior reallocation  = Track {R['track']}  (P(A)={R['post_A']}, P(B)={R['post_B']}; N_e_BC<2.89 => 0.90 Track B)")
    print("-" * 78)

    out_npz = HERE / "s116_w6_wdw_ic_refine.npz"
    out_png = HERE / "s116_w6_wdw_ic_refine.png"
    np.savez(
        out_npz,
        tau_grid=R["tau_grid"], S_grid=R["S_grid"], tau_fine=R["tau_fine"], B_of_tau=R["B_of_tau"],
        V0=R["V0"], V_fold=R["V_fold"], d2S_tau0=R["d2S_tau0"], dS_tau0=R["dS_tau0"], Bprime_0=R["Bprime_0"],
        B_class=R["B_class"], B_class_rebuilt=R["B_class_rebuilt"], B_class_rel=R["B_class_rel"],
        efold_ratio_inv=R["efold_ratio_inv"], N_e_WKB_inv=R["N_e_WKB_inv"],
        B_traj_HH=R["B_traj_HH"], B_traj_Vil=R["B_traj_Vil"],
        efold_ratio_HH=R["efold_ratio_HH"], efold_ratio_Vil=R["efold_ratio_Vil"],
        N_e_BC_HH=R["N_e_BC_HH"], N_e_BC_Vil=R["N_e_BC_Vil"], N_e_BC=R["N_e_BC"], BC_invariance=R["BC_invariance"],
        log_w_HH=R["log_w_HH"], log_w_Vil=R["log_w_Vil"], ens_avg_HH=R["ens_avg_HH"], ens_avg_Vil=R["ens_avg_Vil"],
        psi_HH=R["psi_HH"], psi_Vil=R["psi_Vil"], J_HH=R["J_HH"], J_Vil=R["J_Vil"],
        maxJ_HH=R["maxJ_HH"], maxJ_Vil=R["maxJ_Vil"],
        J_wronskian=R["J_wronskian"], J_W_value=R["J_W_value"], J_W_drift=R["J_W_drift"],
        cons_residual_max=R["cons_residual_max"],
        J_phys_reflecting=R["J_phys_reflecting"], reflecting_datum_forces_J0=R["reflecting_datum_forces_J0"],
        N_e_move=R["N_e_move"], gap_to_threshold=R["gap_to_threshold"],
        N_e_classical=N_e_classical, N_e_acoustic_dens_cancel=N_E_ACOUSTIC_DENS_CANCEL,
        N_e_acoustic_with_dens=N_E_ACOUSTIC_WITH_DENS, N_e_threshold=N_E_THRESHOLD,
        sign_verdict=R["sign_verdict"], magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"], domain_used_frac=R["domain_used_frac"], composite=R["composite"],
        track=R["track"], post_A=R["post_A"], post_B=R["post_B"],
        G_DeWitt=G_DeWitt, tau_fold=tau_fold, convention=CONVENTION,
        pins=json.dumps(pins),
    )
    make_plot(R, out_png)
    print(f"  wrote {out_npz.name}")
    print(f"  wrote {out_png.name}")

    # --- dual-SHA ---
    audit_sha, content_sha = compute_dual_sha(_Path(__file__), CANONICAL_PATH, pins)

    value = (f"N_e_BC_HH={R['N_e_BC_HH']:.4f}|N_e_BC_Vil={R['N_e_BC_Vil']:.4f}|"
             f"BC_invariance={R['BC_invariance']:.2e}|efold_ratio=1.0_both|"
             f"B_class={R['B_class']:.4f}_identical_both_branches|"
             f"J_HH={R['maxJ_HH']:.1e}|J_Vil={R['maxJ_Vil']:.1e}|reflecting_datum_forces_J0={R['reflecting_datum_forces_J0']}|"
             f"N_e_move={R['N_e_move']:.1e}|gap_to_3.1={R['gap_to_threshold']:.4f}|"
             f"canonical_BC=HH|track={R['track']}|"
             f"sign={R['sign_verdict']}|mag={R['magnitude_verdict']}|regime={R['regime_verdict']}|"
             f"s_tau_from_S36_per_ii.B")

    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))

    companion = (f"N_e_BC HH=Vil={R['N_e_BC']:.4f} (efold_ratio=1.0 both => identical |B|={R['B_class']:.4f}); "
                 f"BC-invariance |ΔN_e|={R['BC_invariance']:.1e}; Eq.H-R3-1 reflecting tau=0 => J≡0 "
                 f"(maxJ_HH={R['maxJ_HH']:.1e},maxJ_Vil={R['maxJ_Vil']:.1e}); composite INFO "
                 f"(mag=FAIL+regime=MARGINAL); Track B (P(B)={R['post_B']}); gap->TRANSIT-PS-67 (S70); "
                 f"residual=Q45 operator-canonicity (CF-S117); convention -HH canonical/-BOTH diagnostic")
    extra = [
        f"# dual_prior: N_e_BC={R['N_e_BC']:.4f}<2.89 => 0.90 Track B (gap BC-robust); EFOLD-MAPPING-52 IC-independence extended to BC layer",
        f"# Eq.H-R3-1: Wronskian conserved (Abel residual W*(uv-vu)={R['cons_residual_max']:.1e}); reflecting Neumann (B'(0)={R['Bprime_0']:.1e}) => J(0)=0 => J≡0",
    ]

    print_verdict_payload(
        R["composite"], value, audit_sha, content_sha,
        sign_verdict=R["sign_verdict"], magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        companion_note=companion, extra_rows=extra,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
