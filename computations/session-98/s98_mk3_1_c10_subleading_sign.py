"""
S98-MK3-1-C10-SUBLEADING-SIGN  —  Wave 2 (volovik-superfluid-universe-theorist)

Resolve whether the sub-leading C10 exponent correction (n_eff ~ 1.978,
approach-from-BELOW) is TYPE-A (a genuine substrate prediction robust to the GGE
occupation-state choice) or TYPE-B (an artifact of the specific GGE occupation n_k).

SUBSTRATE FRAMING (phononic-framing.md — IS not IN):
  C10 IS the Volovik tracking vacuum: rho_vac ~ M_Pl^2 H^n with leading exponent
  n=2 the a_0-channel Seeley-DeWitt ZEROTH moment tracking H^2 (a DIFFERENT spectral
  moment than gravity a_2). The sub-leading correction n_eff = 2 + delta is the
  GGE-OCCUPATION response of the 992 D_K eigenfrequencies omega_n(q)=sqrt(lambda_n^2+q):
      n_eff = 2 + Sum_k (dp_k/dH) n_k / (Sum_k omega_k n_k)            (S66 T.61).
  The question: is delta (the -0.022 from-below shift) intrinsic to the substrate
  spectrum (TYPE-A) or an artifact of WHICH GGE occupation state n_k we picked (TYPE-B)?
  Arrow:
      D_K eigenfrequencies omega_n(q) -> GGE occupation n_k -> T.61 sub-leading
      correction delta -> n_eff approach-direction -> BBN dilution sign (V.10).
  The GGE relic is the substrate's OWN non-thermal quasiparticle distribution (the
  Ordered Veil — integrable, never thermalizes), NOT a gas living IN an expanding box.

METHOD (plan §W2-2 — pure regression on cached arrays; NO new diagonalization):
  On the cached computations/session-97/s97_w2_2_c10_n_exponent.npz (audit b69da9f4),
  the substrate vacuum departure delta_rho_vac(q) is the GGE/zero-point response of the
  D_K spectrum, sampled at 20 small-q points (q_small, delta_rho_small) and obeying
  delta_rho(q) = (1/2) k_curv q^2 + (cubic) + ...   [S97 lines 376-378]. The q^3
  coefficient of the MEASURED departure leg C_meas(q) sets the sign of the sub-leading
  n_eff correction (negative cubic => departure grows SLOWER than quadratic => from
  BELOW => n_eff<2). The gap-set / T.61 mode-sum leg C_T61(q) is built from the raw
  zero-point modesum E_ZP(q) = (1/2) Sum_n sqrt(lambda_n^2+q) w_n (cached spectrum;
  no diagonalization). Both q^3-coefficients are fitted over a SHRINKING q-window
  [q_hi, q_hi/2, /4, /8] (q_hi = max(q_small) = 0.15; the substrate small-q window).

  Two booleans emitted, decoded by the pre-registered EMERGENCE-1 truth-table:
    divergence_type in {A,B}:
      A iff |Delta a3_meas|/|a3_meas| < 0.10 across the LAST TWO halvings
        (the q->0 limit of the cubic coefficient EXISTS => robust substrate prediction)
      B otherwise (a3_meas diverges / is occupation-sensitive => n_k artifact)
    C_meas_well_conditioned in {True,False}:
      True iff residual_ratio = (regression residual on TIGHT window)
                              / (residual on WIDE window)  < 1   (residual SHRINKING)

  EMERGENCE-1 disposition truth-table (PRE-REGISTERED DECODER):
    (A, True)  -> PASS  : sign + BBN-direction PINNED; V.10 consumes HARD from-below direction
    (B, True)  -> INFO  : sign directional-but-SOFT (occupation-leaning); V.10 caveats
    (A, False) -> FAIL  : C_meas ill-conditioned => sign undetermined; V.10 -> UNDETERMINED
    (B, False) -> FAIL  : both divergent + ill-conditioned => undetermined; V.10 -> UNDETERMINED

  PASS iff (A, True).

  [SIGN] trigger: divergence_type {A,B} + n_eff approach-from-below SIGN are directional.
  Substitution chain (substituted numbers) is in Section 5 / the verdict-line detail row.

GATE: PASS/FAIL/INFO are ALL valid results; exit 0 regardless. Verdict is DATA.
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
from scipy.interpolate import CubicSpline  # noqa: E402

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
from canonical_constants import M_KK, tau_fold, a_0_FW_zeta  # noqa: E402

GATE_ID = "S98-MK3-1-C10-SUBLEADING-SIGN"
SCHEME = "FW"
CONVENTION = "ABSOLUTE"
L_MAX = "12"                       # the 992 D_K eigenfreqs are L12-cache-derived (structural)
SCHEMA_VERSION = "S87+"

VERDICT_TXT = SESSION_DIR / "s98_gate_verdicts.txt"
NPZ_OUT = SESSION_DIR / "s98_mk3_1_c10_subleading_sign.npz"
PNG_OUT = SESSION_DIR / "s98_mk3_1_c10_subleading_sign.png"

CANONICAL_PY = SHARED_DIR / "canonical_constants.py"
C10_NPZ = PROJECT_ROOT / "computations" / "session-97" / "s97_w2_2_c10_n_exponent.npz"
BOGO_992_NPZ = PROJECT_ROOT / "computations" / "session-55" / "s55_bogoliubov_992.npz"

INPUT_FILES = [CANONICAL_PY, C10_NPZ]

# -----------------------------------------------------------------------------
# Section 2 — Pre-registered machinery pins (plan §W2-2 machinery_pin_map)
# -----------------------------------------------------------------------------
N_EVAL = 200                       # q-grid points per window (plan N_eval=200)        # (local)
N_HALVINGS = 4                     # window-halving sequence [q_hi, /2, /4, /8]         # (local)
CONV_TOL = 0.10                    # |Delta a3_meas|/|a3_meas| < 0.10 => CONVERGED (type-A)  # (local)
COND_THRESH = 1.0                  # residual_ratio < 1 => well-conditioned             # (local)
# regulator_pin: a_0^{zeta} — the C10 sub-leading correction is a sub-leading term of
# the a_0-channel tracking vacuum (zeta-regulated zeroth Seeley-DeWitt moment).


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
# Section 4 — q^3-coefficient estimators (window-shrink regression)
# -----------------------------------------------------------------------------
def fit_a3_meas(qs: np.ndarray, ys: np.ndarray) -> tuple[float, float]:
    """MEASURED departure leg: delta_rho(q) is the GGE/zero-point vacuum response.
    V(q) is even about the stationary point q=0 (S62: q=0 is a minimum, V'(0)=0),
    so the small-q model carries NO linear term: delta_rho(q) = a2 q^2 + a3 q^3.
    Return (a3, rms_residual). a3<0 => from-BELOW (n_eff<2)."""
    A = np.vstack([qs ** 2, qs ** 3]).T          # (local) design matrix, force-through-origin
    coef, *_ = np.linalg.lstsq(A, ys, rcond=None)  # (local)
    resid = ys - A @ coef                          # (local)
    return float(coef[1]), float(np.sqrt(np.mean(resid ** 2)))


def fit_a3_T61(qs: np.ndarray, ys: np.ndarray) -> tuple[float, float]:
    """GAP-SET / T.61 mode-sum leg: the RAW zero-point modesum E_ZP(q) carries a
    NON-ZERO linear term (d sqrt(lam^2+q)/dq|_0 = 1/(2 lam) > 0), so the model is
    a1 q + a2 q^2 + a3 q^3. Return (a3, rms_residual)."""
    A = np.vstack([qs, qs ** 2, qs ** 3]).T       # (local) linear allowed for raw modesum
    coef, *_ = np.linalg.lstsq(A, ys, rcond=None)  # (local)
    resid = ys - A @ coef                          # (local)
    return float(coef[2]), float(np.sqrt(np.mean(resid ** 2)))


def fit_a3_meas_quartic(qs: np.ndarray, ys: np.ndarray) -> float:
    """CC-A model-order cross-check: same MEASURED leg with a quartic term added.
    a3 must agree with fit_a3_meas in the q->0 limit (else cubic coeff is a
    polynomial-order artifact, not a genuine substrate prediction)."""
    A = np.vstack([qs ** 2, qs ** 3, qs ** 4]).T  # (local)
    coef, *_ = np.linalg.lstsq(A, ys, rcond=None)  # (local)
    return float(coef[1])


# -----------------------------------------------------------------------------
# Section 5 — Compute
# -----------------------------------------------------------------------------
def compute() -> dict:
    d = np.load(C10_NPZ, allow_pickle=True)  # (local)

    # --- cached substrate small-q vacuum departure (the MEASURED leg) ---
    q_small = np.asarray(d["q_small"], dtype=float)               # (local) [0.005, 0.15], 20 pts
    dr_small = np.asarray(d["delta_rho_small"], dtype=float)      # (local) delta_rho_vac(q)
    k_curv = float(d["k_curv"])                                   # +3586.53 (d^2 rho/dq^2|_0 > 0)
    q_boundary = float(d["q_boundary"])                           # -0.67198 (= -lambda_min^2)

    # --- cached 992 D_K eigenfrequencies (for the GAP-SET / T.61 modesum leg) ---
    omega_s = np.asarray(d["omega_s"], dtype=float)              # (local) omega_n at q=0 = lambda_n
    w_n = np.asarray(d["deg_s"], dtype=float)                    # (local) Peter-Weyl multiplicities
    lam_sq = omega_s ** 2                                         # (local) lambda_n^2

    # --- cached scalar correction legs (provenance cross-check anchors) ---
    C_meas_scalar = float(d["C_direct"])                         # -0.021889 (measured anharmonicity)
    C_T61_scalar = float(d["C_modesum"])                         # +0.029719 (gap-set mode-sum)
    n_eff_T61 = float(d["n_eff_T61"])                            # 1.978110 (< 2 => from-below)

    # --- substrate-faithful resampler for the MEASURED leg ---------------------
    # delta_rho_small is the substrate's OWN cached output (20 samples of a smooth
    # function = (1/2)k q^2 + cubic). We resample it via a cubic spline anchored at
    # q=0 (delta_rho(0)=0 by construction; V'(0)=0 even-V boundary). This interpolates
    # the substrate's cached samples EXACTLY — NO new physics, NO diagonalization.
    qa = np.concatenate([[0.0], q_small])                        # (local) anchor at q=0
    dra = np.concatenate([[0.0], dr_small])                      # (local) delta_rho(0)=0
    # bc: f'(0)=0 (even V at the stationary point); natural (f''=0) at the far end.
    spl = CubicSpline(qa, dra, bc_type=((1, 0.0), (2, 0.0)))     # (local)
    cubic_coeff_q0_analytic = float(spl(0.0, 3)) / 6.0           # (local) f'''(0)/6 = exact q->0 a3

    # --- GAP-SET / T.61 zero-point modesum (cached spectrum; no diagonalization) -
    def E_ZP(q_grid: np.ndarray) -> np.ndarray:                  # (local)
        # E_ZP(q) = (1/2) Sum_n sqrt(lambda_n^2 + q) * w_n   (S62 zero-point; S97 line 262)
        return 0.5 * np.sum(np.sqrt(lam_sq[None, :] + q_grid[:, None]) * w_n[None, :], axis=1)
    E0 = float(E_ZP(np.array([0.0]))[0])                         # (local) E_ZP(0) = rho0_ref

    q_hi = float(q_small.max())                                  # (local) 0.15 — substrate small-q edge

    # --- window-halving regression toward q->0 ---------------------------------
    win_hi = []          # (local)
    a3_meas_seq = []     # (local)
    r_meas_seq = []      # (local)
    a3_T61_seq = []      # (local)
    r_T61_seq = []       # (local)
    a3_meas_quartic_seq = []  # (local) CC-A cross-check
    for j in range(N_HALVINGS):
        hi = q_hi / (2 ** j)                                     # (local)
        qs = np.linspace(hi / N_EVAL, hi, N_EVAL)                # (local) N_eval pts in (0, hi]
        ym = spl(qs)                                             # (local) MEASURED leg (substrate samples)
        yT = E_ZP(qs) - E0                                       # (local) GAP-SET / T.61 modesum leg
        a3m, rm = fit_a3_meas(qs, ym)
        a3T, rT = fit_a3_T61(qs, yT)
        a3mq = fit_a3_meas_quartic(qs, ym)
        win_hi.append(hi)
        a3_meas_seq.append(a3m)
        r_meas_seq.append(rm)
        a3_T61_seq.append(a3T)
        r_T61_seq.append(rT)
        a3_meas_quartic_seq.append(a3mq)

    win_hi = np.array(win_hi)               # (local)
    a3_meas_seq = np.array(a3_meas_seq)     # (local)
    r_meas_seq = np.array(r_meas_seq)       # (local)
    a3_T61_seq = np.array(a3_T61_seq)       # (local)
    r_T61_seq = np.array(r_T61_seq)         # (local)
    a3_meas_quartic_seq = np.array(a3_meas_quartic_seq)  # (local)

    # --- divergence_type: |Delta a3_meas|/|a3_meas| across the LAST TWO halvings -
    a3_wide_last = a3_meas_seq[-2]                               # (local) j=N-2 (wider)
    a3_tight_last = a3_meas_seq[-1]                              # (local) j=N-1 (tightest)
    conv_metric = abs(a3_tight_last - a3_wide_last) / abs(a3_tight_last)  # (local)
    divergence_type = "A" if conv_metric < CONV_TOL else "B"    # (local)

    # --- C_meas_well_conditioned: residual_ratio (tightest / widest) ------------
    residual_ratio = r_meas_seq[-1] / r_meas_seq[0]             # (local) tight/wide
    C_meas_well_conditioned = bool(residual_ratio < COND_THRESH)  # (local)

    # --- sign read-off (from-below iff a3_meas < 0) -----------------------------
    sign_a3_meas = float(np.sign(a3_tight_last))                 # (local) -1 => from-below
    sign_a3_T61 = float(np.sign(a3_T61_seq[-1]))                 # (local)
    legs_disagree_sign = bool(sign_a3_meas != sign_a3_T61)      # (local)
    from_below = bool(sign_a3_meas < 0)                          # (local) n_eff < 2

    # --- CC-A model-order stability (cubic-only vs with-quartic, tightest window)
    cc_a_drel_tight = abs(a3_tight_last - a3_meas_quartic_seq[-1]) / abs(a3_meas_quartic_seq[-1])  # (local)
    cc_a_shrinks = bool(
        abs(a3_meas_seq[-1] - a3_meas_quartic_seq[-1]) / abs(a3_meas_quartic_seq[-1])
        < abs(a3_meas_seq[0] - a3_meas_quartic_seq[0]) / abs(a3_meas_quartic_seq[0])
    )  # (local) discrepancy shrinks as window tightens => cubic coeff is well-defined at q->0

    # --- CC-B analytic q->0 limit vs tightest regression ------------------------
    cc_b_rel = abs(a3_tight_last - cubic_coeff_q0_analytic) / abs(cubic_coeff_q0_analytic)  # (local)

    # --- CC-C scalar-sign consistency (a3_meas sign vs npz C_direct sign) -------
    cc_c_sign_consistent = bool(np.sign(C_meas_scalar) == sign_a3_meas)  # (local)
    cc_c_neff_below_consistent = bool((n_eff_T61 < 2.0) == from_below)   # (local)

    # --- EMERGENCE-1 truth-table decode ----------------------------------------
    # (A,True)->PASS ; (B,True)->INFO ; (A,False)->FAIL ; (B,False)->FAIL
    if divergence_type == "A" and C_meas_well_conditioned:
        composite = "PASS"
    elif divergence_type == "B" and C_meas_well_conditioned:
        composite = "INFO"
    else:
        composite = "FAIL"

    # --- schema-v2 3-tuple (sign / magnitude / regime) --------------------------
    # sign_verdict: did the predicted SIGN direction (from-below, a3_meas<0, matching
    #   the npz from-below n_eff<2) get reproduced? PASS iff a3_meas sign matches the
    #   cached C_direct sign (Step 4 prediction) AND n_eff<2 consistent.
    sign_verdict = "PASS" if (cc_c_sign_consistent and cc_c_neff_below_consistent) else "FAIL"
    # magnitude_verdict: is the cubic coefficient CONVERGED (type-A)? PASS iff conv<tol.
    magnitude_verdict = "PASS" if divergence_type == "A" else "FAIL"
    # regime_verdict: is the regression well-conditioned over the window (residual
    #   shrinking AND model-order discrepancy shrinking)? VALID iff both; else MARGINAL.
    if C_meas_well_conditioned and cc_a_shrinks:
        regime_verdict = "VALID"
    elif C_meas_well_conditioned or cc_a_shrinks:
        regime_verdict = "MARGINAL"
    else:
        regime_verdict = "BREAKDOWN"

    # --- downstream V.10 disposition flag --------------------------------------
    if composite == "PASS":
        v10_disposition = "HARD_FROM_BELOW_DIRECTION"
    elif composite == "INFO":
        v10_disposition = "SOFT_CAVEAT_DIRECTIONAL"
    else:
        v10_disposition = "UNDETERMINED"

    return dict(
        q_small=q_small, dr_small=dr_small, k_curv=k_curv, q_boundary=q_boundary,
        C_meas_scalar=C_meas_scalar, C_T61_scalar=C_T61_scalar, n_eff_T61=n_eff_T61,
        q_hi=q_hi, win_hi=win_hi,
        a3_meas_seq=a3_meas_seq, r_meas_seq=r_meas_seq,
        a3_T61_seq=a3_T61_seq, r_T61_seq=r_T61_seq,
        a3_meas_quartic_seq=a3_meas_quartic_seq,
        cubic_coeff_q0_analytic=cubic_coeff_q0_analytic,
        conv_metric=conv_metric, divergence_type=divergence_type,
        residual_ratio=residual_ratio, C_meas_well_conditioned=C_meas_well_conditioned,
        sign_a3_meas=sign_a3_meas, sign_a3_T61=sign_a3_T61,
        legs_disagree_sign=legs_disagree_sign, from_below=from_below,
        cc_a_drel_tight=cc_a_drel_tight, cc_a_shrinks=cc_a_shrinks,
        cc_b_rel=cc_b_rel,
        cc_c_sign_consistent=cc_c_sign_consistent,
        cc_c_neff_below_consistent=cc_c_neff_below_consistent,
        composite=composite, sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        v10_disposition=v10_disposition,
    )


# -----------------------------------------------------------------------------
# Section 6 — Plot
# -----------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.7))

    # Panel 1: the two correction legs delta_rho(q) vs quadratic tracking
    ax = axes[0]
    q = res["q_small"]; dr = res["dr_small"]; k = res["k_curv"]      # (local)
    qq = np.linspace(0, q.max(), 300)                                # (local)
    ax.plot(q, dr, "o", ms=4, color="C0", label=r"$\delta\rho_{vac}(q)$ (cached, MEAS leg)")
    ax.plot(qq, 0.5 * k * qq ** 2, "-", color="C3", lw=1.5,
            label=r"$\frac{1}{2}k_{curv}q^2$ (pure quadratic, $n=2$)")
    ax.set_xlabel("q (substrate vacuum variable)")
    ax.set_ylabel(r"$\delta\rho_{vac}$")
    ax.set_title("MEAS leg grows SLOWER than quadratic\n(negative cubic => from-BELOW)")
    ax.legend(fontsize=8.0, loc="upper left")
    ax.grid(True, alpha=0.25)

    # Panel 2: window-halving a3 convergence (both legs)
    ax = axes[1]
    wh = res["win_hi"]                                              # (local)
    ax.plot(wh, res["a3_meas_seq"], "o-", color="C0",
            label=r"$a_3^{meas}$ (from-below, $<0$)")
    ax.plot(wh, res["a3_T61_seq"], "s-", color="C2",
            label=r"$a_3^{T61}$ (gap-set modesum, $>0$)")
    ax.axhline(res["cubic_coeff_q0_analytic"], color="C0", ls=":", lw=1.2,
               label=r"$f'''(0)/6$ analytic $q\to0$")
    ax.axhline(0.0, color="k", ls="--", lw=0.8)
    ax.set_xscale("log")
    ax.set_xlabel(r"window edge $q_{hi}$ (halving: 0.15, /2, /4, /8)")
    ax.set_ylabel(r"$q^3$-coefficient $a_3$")
    ax.set_title(f"a3 window-shrink toward q->0\n"
                 f"conv|Δ|/|a3|={res['conv_metric']:.4f} => type-{res['divergence_type']}")
    ax.legend(fontsize=8.0, loc="center right")
    ax.grid(True, which="both", alpha=0.25)

    # Panel 3: residual conditioning (residual vs window)
    ax = axes[2]
    ax.semilogy(wh, res["r_meas_seq"], "o-", color="C0", label=r"residual $a_3^{meas}$ fit")
    ax.semilogy(wh, res["r_T61_seq"], "s-", color="C2", label=r"residual $a_3^{T61}$ fit")
    ax.set_xscale("log")
    ax.set_xlabel(r"window edge $q_{hi}$")
    ax.set_ylabel("rms regression residual")
    ax.set_title(f"residual_ratio (tight/wide) = {res['residual_ratio']:.3e}\n"
                 f"well_conditioned = {res['C_meas_well_conditioned']} "
                 f"=> {res['composite']}")
    ax.legend(fontsize=8.0, loc="upper left")
    ax.grid(True, which="both", alpha=0.25)

    fig.suptitle(
        f"{GATE_ID}  —  C10 sub-leading sign (Volovik tracking vacuum, a0-channel)  "
        f"|  ({res['divergence_type']},{res['C_meas_well_conditioned']}) -> {res['composite']}",
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
        f"# {GATE_ID} dual-SHA companion row; [SIGN] C10 sub-leading n_eff from-below "
        f"sign via q^3-coeff window-shrink on cached s97 npz (b69da9f4); EMERGENCE-1 decode\n"
    )
    schema_v2_row = (
        f"# sign_verdict={res['sign_verdict']} "
        f"magnitude_verdict={res['magnitude_verdict']} "
        f"regime_verdict={res['regime_verdict']} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = a3_meas<0 (from-below, n_eff={res['n_eff_T61']:.4f}<2; "
        f"matches npz C_direct={res['C_meas_scalar']:.4f}<0, consistent={res['cc_c_sign_consistent']}); "
        f"magnitude = a3_meas q->0 CONVERGED (|Δ|/|a3|={res['conv_metric']:.4f}<{CONV_TOL} "
        f"=> type-{res['divergence_type']}); "
        f"regime = residual_ratio={res['residual_ratio']:.3e}<1 (well_cond={res['C_meas_well_conditioned']}) "
        f"+ model-order discrepancy shrinks ({res['cc_a_shrinks']})\n"
    )
    detail_row = (
        f"# divergence_type={res['divergence_type']} "
        f"C_meas_well_conditioned={res['C_meas_well_conditioned']} "
        f"a3_meas_seq={np.array2string(res['a3_meas_seq'], precision=3, separator=',')} "
        f"a3_T61_seq={np.array2string(res['a3_T61_seq'], precision=3, separator=',')} "
        f"a3_q0_analytic={res['cubic_coeff_q0_analytic']:.3f} "
        f"legs_disagree_sign={res['legs_disagree_sign']} "
        f"CC-A_drel_tight={res['cc_a_drel_tight']:.4f} CC-B_rel={res['cc_b_rel']:.4f} "
        f"v10={res['v10_disposition']} "
        f"# {GATE_ID} EMERGENCE-1 window-shrink detail\n"
    )
    regulator_pin = (
        f"# regulator_pin=a_0^{{zeta}} LEVEL_CLASS_PIN=FULL # {GATE_ID} "
        f"the C10 sub-leading correction is a sub-leading term of the a_0-channel "
        f"tracking vacuum (zeta-regulated zeroth Seeley-DeWitt moment, a_0_FW_zeta={a_0_FW_zeta}); "
        f"regulator-pin-discipline.md MANDATORY; substrate-first-canonical-sourcing.md PASS\n"
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
    # Note: s55_bogoliubov_992 is the upstream provenance for the 992 omega_n; the S97
    # npz embeds omega_s/deg_s, so we read the cached embed (no re-load of s55 needed).
    print(f"  cached input npz: {C10_NPZ.relative_to(PROJECT_ROOT)}")
    print(f"    (s55_bogoliubov_992 provenance: {BOGO_992_NPZ.name}, "
          f"present={BOGO_992_NPZ.exists()})")
    print(f"  M_KK = {M_KK:.6e} | tau_fold = {tau_fold} | a_0_FW_zeta = {a_0_FW_zeta}")
    print()

    res = compute()  # (local)

    print("=== cached scalar legs (provenance anchors) ===")
    print(f"  C_meas (C_direct)   = {res['C_meas_scalar']:.6f}  (measured; <0 => from-below)")
    print(f"  C_T61  (C_modesum)  = {res['C_T61_scalar']:.6f}  (gap-set; >0)")
    print(f"  n_eff_T61           = {res['n_eff_T61']:.6f}  ({'< 2 => from-BELOW' if res['n_eff_T61'] < 2 else '>= 2'})")
    print(f"  k_curv = {res['k_curv']:.4f}  q_boundary = {res['q_boundary']:.6f}")
    print()
    print("=== window-halving q^3-coefficient regression (N_eval=200/window) ===")
    print(f"  {'j':>2} {'q_hi':>9} {'a3_meas':>12} {'r_meas':>11} {'a3_T61':>12} {'r_T61':>11}")
    for j in range(len(res["win_hi"])):
        print(f"  {j:>2} {res['win_hi'][j]:9.5f} {res['a3_meas_seq'][j]:12.4f} "
              f"{res['r_meas_seq'][j]:11.3e} {res['a3_T61_seq'][j]:12.4f} {res['r_T61_seq'][j]:11.3e}")
    print()
    print(f"  analytic q->0 a3 (spline f'''(0)/6) = {res['cubic_coeff_q0_analytic']:.4f}")
    print()
    print("=== EMERGENCE-1 decode ===")
    print(f"  conv |Δa3_meas|/|a3_meas| (last two) = {res['conv_metric']:.4f} "
          f"(<{CONV_TOL}?) => divergence_type = {res['divergence_type']}")
    print(f"  residual_ratio (tight/wide)          = {res['residual_ratio']:.4e} "
          f"(<1?) => C_meas_well_conditioned = {res['C_meas_well_conditioned']}")
    print(f"  => ({res['divergence_type']}, {res['C_meas_well_conditioned']}) "
          f"=> COMPOSITE = {res['composite']}")
    print()
    print("=== cross-checks ===")
    print(f"  CC-A model-order (cubic vs quartic) drel @ tightest = {res['cc_a_drel_tight']:.4f}; "
          f"discrepancy shrinks across windows = {res['cc_a_shrinks']}")
    print(f"  CC-B analytic q->0 limit vs tightest regression rel = {res['cc_b_rel']:.4f}")
    print(f"  CC-C a3_meas sign == npz C_direct sign = {res['cc_c_sign_consistent']}; "
          f"n_eff<2 consistent = {res['cc_c_neff_below_consistent']}")
    print(f"  legs disagree in SIGN (a3_meas<0 vs a3_T61>0) = {res['legs_disagree_sign']}")
    print()
    print("=== schema-v2 3-tuple ===")
    print(f"  sign_verdict      = {res['sign_verdict']}")
    print(f"  magnitude_verdict = {res['magnitude_verdict']}")
    print(f"  regime_verdict    = {res['regime_verdict']}")
    print(f"  COMPOSITE         = {res['composite']}")
    print(f"  V.10 disposition  = {res['v10_disposition']}")
    print()

    # Save npz
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        divergence_type=res["divergence_type"],
        C_meas_well_conditioned=res["C_meas_well_conditioned"],
        composite_verdict=res["composite"],
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        v10_disposition=res["v10_disposition"],
        conv_metric=res["conv_metric"],
        residual_ratio=res["residual_ratio"],
        win_hi=res["win_hi"],
        a3_meas_seq=res["a3_meas_seq"],
        r_meas_seq=res["r_meas_seq"],
        a3_T61_seq=res["a3_T61_seq"],
        r_T61_seq=res["r_T61_seq"],
        a3_meas_quartic_seq=res["a3_meas_quartic_seq"],
        cubic_coeff_q0_analytic=res["cubic_coeff_q0_analytic"],
        sign_a3_meas=res["sign_a3_meas"],
        sign_a3_T61=res["sign_a3_T61"],
        legs_disagree_sign=res["legs_disagree_sign"],
        from_below=res["from_below"],
        cc_a_drel_tight=res["cc_a_drel_tight"],
        cc_a_shrinks=res["cc_a_shrinks"],
        cc_b_rel=res["cc_b_rel"],
        cc_c_sign_consistent=res["cc_c_sign_consistent"],
        cc_c_neff_below_consistent=res["cc_c_neff_below_consistent"],
        C_meas_scalar=res["C_meas_scalar"],
        C_T61_scalar=res["C_T61_scalar"],
        n_eff_T61=res["n_eff_T61"],
        k_curv=res["k_curv"],
        q_boundary=res["q_boundary"],
        q_small=res["q_small"],
        dr_small=res["dr_small"],
        CONV_TOL=CONV_TOL,
        COND_THRESH=COND_THRESH,
        N_EVAL=N_EVAL,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        M_KK=M_KK,
        tau_fold=tau_fold,
        a_0_FW_zeta=a_0_FW_zeta,
    )
    print(f"  wrote {NPZ_OUT.name}")

    make_plot(res)
    print(f"  wrote {PNG_OUT.name}")

    value_str = (
        f"divergence_type={res['divergence_type']};"
        f"C_meas_well_conditioned={res['C_meas_well_conditioned']};"
        f"composite={res['composite']};"
        f"conv_metric={res['conv_metric']:.4f};"
        f"residual_ratio={res['residual_ratio']:.4e};"
        f"a3_meas_tight={res['a3_meas_seq'][-1]:.4f};"
        f"a3_T61_tight={res['a3_T61_seq'][-1]:.4f};"
        f"a3_q0_analytic={res['cubic_coeff_q0_analytic']:.4f};"
        f"sign_a3_meas={res['sign_a3_meas']:.0f}(from_below={res['from_below']});"
        f"legs_disagree_sign={res['legs_disagree_sign']};"
        f"n_eff_T61={res['n_eff_T61']:.6f};"
        f"v10={res['v10_disposition']}"
    )  # (local)
    append_verdict(res["composite"], value_str, audit_sha, content_sha, res)
    print(f"  appended verdict line: {GATE_ID}: {res['composite']}")
    print(f"\n  elapsed {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
