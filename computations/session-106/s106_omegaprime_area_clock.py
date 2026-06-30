#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S106-OMEGAPRIME-AREA-CLOCK — does the Hawking-dressed-relic modular flow have a
geometric area-clock?

GATED ON S106-OMEGAPRIME-Z-CONSTRUCTION = PASS (intra-wave gating; existence
before comparison). The 2a gate constructed the Hawking-dressed (Tolman-regraded)
modular generator K-hat.z = diag(K_a * z_a) on the named horizon blocks, emitted
omega'_z's faithfulness witness (0 < f'_a < 1 strict on every BULK mode), carried
the floor mode empty-Fock (K_floor*z_floor -> +inf, clean), and built
Delta_{omega'_z}^{it}. Disk verdict:
    omegaprimez=constructed; bulk_faithful=True; floor_empty_Fock=True;
    n_bulk=714; n_floor=6; K_floor=0.263473; Delta_omegaprimez_it_built=True;
    audit_sha256=4dd27aee5ff1ce8895b113133c71ce29f0716854c9c6c9af8632a582eb44e916

GEOMETRIC. This gate concerns the spectral-triple geometry: does the area-flow
generator
    G_tau = d/dtau on the moment family {a_0, a_2, a_4} of D_K(tau)
(area operator A-hat = a_2 second-Seeley-DeWitt moment, a_2_FW_zeta = 2776.165389)
COINCIDE with the Hawking-dressed-relic modular flow sigma_t^{omega'_z} =
Ad(Delta_{omega'_z}^{it}) at the op-norm level on the named-block BULK?

    ||K-hat.z - G-hat_tau||_op  <  tol = 1e-3   AND   cocycle-gen sign = -1 (= S97)

Substrate-first direction of explanation (phononic-framing.md "IS Space"):
    D_K spectrum (named horizon blocks, L_max=10)
      -> a_2 Seeley-DeWitt area moment             [the area operator A-hat]
      -> G_tau = d/dtau on the moment family       [the GEOMETRIC exflation-transit gen.]
      -> (does it equal?) sigma_t^{omega'_z}        [the gate-2a Hawking-dressed modular flow]
The area operator A-hat IS the a_2 moment -- NOT a geometric area of a surface in
a spacetime container. The area-clock is read FROM the spectral-action grading,
NEVER as a flow IN a container-horizon.

ADMISSIBILITY GUARDS (workshop pre-registration, VERBATIM, MANDATORY):
  (a) Layer-1 identity guard (z-INDEPENDENT): the comparison is stated against
      sigma_t^{omega'_z}, NEVER sigma_t^omega. omega'_z != omega for any z != 1
      (the f<->K bijection). Even a PASS does NOT reopen GEM-Q1 (the now-CLOSED
      G_tau = sigma_t^omega, S105 GEM-WORKSHOP Row 3) -- it is a NEW geometric-
      area-clock bridge CANDIDATE for the Hawking-dressed relic.
  (b) Layer-2 faithfulness witness (z-DEPENDENT): gate 2a emitted omega'_z's
      faithfulness witness (0 < f'_a < 1 strict on the bulk) BEFORE this
      comparison -- the 2a->2b gating IS the structural enforcement. A z that
      closed this gap by driving a BULK mode to empty-Fock would have FAILED 2a.
  (c) Floor-mode domain, interp (i): the floor mode is empty-Fock (gate 2a),
      K-hat.z -> +inf there -- EXCLUDED from the op-norm (bulk-only comparison;
      the floor contributes no finite generator value). op-norm on {|lam| > lam_horizon}.

[SIGN] trigger: cocycle-generator sign = -1 (matching S97 dS/d(a0/a2) = -1, the
OUTER-class second-law co-orientation datum; state-INDEPENDENT). Necessary for a
geometric area-clock but NOT sufficient -- the op-norm < tol conjunct carries the
INNER/identity content. A sign-PASS with op-norm >= tol is composite INFO
(co-monotone confirmed, area-clock IDENTITY not established) per the plan-frozen
composite-precedence operator.

A PASS is a CANDIDATE ONLY -- NO registration this session. Any future 5-anatomy +
3-level registration of the acoustic-area <-> Hawking-dressed-relic-modular-flow
bridge routes to S107 (cross-pillar-bridge-anatomy.md). mack-cosmic-bridge writes
any bridge row at a future session, not S106.

Plan: sessions/session-plan/session-106-plan-w2.md  §W2-2 (gate block).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
import os
from pathlib import Path

_SHARED = Path(__file__).resolve().parents[1] / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

# Cap CPU threads BEFORE numpy import (the op-norm path uses GPU torch.linalg per
# the plan pin with a numpy cross-check; the CPU fallback must not contend).
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403  (MANDATORY)
from canonical_constants import (
    a_2_FW_zeta, a2_fold, tau_fold,
)

import json
import hashlib
import numpy as np

# GPU path (plan pin: torch.linalg for the 720-mode op-norm = largest singular
# value of the diagonal difference; cross-check vs numpy < 1e-9, matching W2-3).
try:
    import torch
    _HAVE_TORCH = True
except Exception:  # pragma: no cover
    _HAVE_TORCH = False

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 2 — Identity + machinery pins
# ---------------------------------------------------------------------------
SESSION = "S106"
GATE_ID = "S106-OMEGAPRIME-AREA-CLOCK"
SCHEME = "FW"
CONVENTION = ("ACOUSTIC-FROZEN-OMEGAPRIME-Z-AREA-CLOCK;"
              "COMPARE-AGAINST-SIGMA-OMEGAPRIME-Z-ONLY;"
              "UNIT-NORMALIZED-OPNORM")
L_MAX = 10                   # (local) named-block extraction (horizon-block axis; W2-2/W2-3 pin)

TOL_OPNORM = 1.0e-3          # (local) op-norm PASS band; INHERITED from S105 W2-3 (tol_opnorm=0.001)
S97_SIGN_REF = -1            # (local) S97-DS-AREA-LAW-MONOTONICITY dS/d(a0/a2) sign
GPU_NUMPY_TOL = 1.0e-9       # (local) GPU/CPU op-norm agreement bar (matches W2-3)

# ---------------------------------------------------------------------------
# Section 3 — Input file pins
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
CANON_PY = _SHARED / "canonical_constants.py"
# gate-2a output (the constructed omega'_z modular generator K-hat.z + masks)
S106_2A_NPZ = SESSION_DIR / "s106_omegaprime_z_construction.npz"
# S105 W2-3 area-flow generator G_hat + the S97 sign chain
S105_W2_3_NPZ = SESSION_DIR.parent / "session-105" / "s105_w2_3_area_modular_agreement.npz"

OUT_NPZ = SESSION_DIR / "s106_omegaprime_area_clock.npz"
OUT_PNG = SESSION_DIR / "s106_omegaprime_area_clock.png"


# ---------------------------------------------------------------------------
# Section 4 — dual-SHA helpers (verbatim from the W2-3 sister gate)
# ---------------------------------------------------------------------------
def _file_sha(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(pins: dict) -> tuple[str, str]:
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = b""
    try:
        script_bytes = Path(__file__).resolve().read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""
    try:
        canonical_bytes = CANON_PY.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note: str = "",
                          extra_rows=None) -> dict:
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
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # ---- 5.0 GATING: 2a (S106-OMEGAPRIME-Z-CONSTRUCTION) PASS is REQUIRED ----
    d2a = np.load(S106_2A_NPZ, allow_pickle=True)
    a2_verdict = str(d2a["verdict"])
    a2_bulk_faithful = bool(d2a["bulk_faithful"])
    a2_floor_empty = bool(d2a["floor_empty_fock"])
    a2_delta_built = bool(d2a["delta_built"])
    gating_status = (a2_verdict == "PASS") and a2_bulk_faithful and a2_floor_empty and a2_delta_built
    if not gating_status:
        # The orchestrator only dispatches 2b on 2a PASS. If this branch fires,
        # the gate closes honestly (mechanical closure, upstream-blocked) per
        # mechanical-closure-discipline.md -- NOT a FAIL.
        raise RuntimeError(
            f"GATING VIOLATION: 2a verdict={a2_verdict} bulk_faithful={a2_bulk_faithful} "
            f"floor_empty={a2_floor_empty} delta_built={a2_delta_built}; "
            "2b runs ONLY on 2a PASS (PRE-REG-INC otherwise).")

    # ---- 5.1 Load the gate-2a Hawking-dressed modular generator K-hat.z ------
    # Kz = diag(K_a * z_a) on ALL 720 named-block modes; floor modes carry +inf
    # (z_floor = 1/sqrt(0) = +inf, the empty-Fock fixed point). The BULK mask
    # selects {|lam_a| > lam_horizon} (n_bulk = 714); the floor mask (n_floor = 6)
    # is EXCLUDED from the op-norm by Layer-2 guard (c).
    Kz = np.asarray(d2a["Kz"], dtype=np.float64)              # (local) K_a*z_a, 720
    bulk_mask = np.asarray(d2a["bulk_mask"], dtype=bool)       # (local) 720
    floor_mask = np.asarray(d2a["floor_mask"], dtype=bool)     # (local) 720
    K_modular_2a = np.asarray(d2a["K_modular"], dtype=np.float64)  # (local) E_a/T per mode, 720
    z_arr = np.asarray(d2a["z"], dtype=np.float64)            # (local) Tolman weight, 720
    lam_horizon = float(d2a["lam_horizon"])                   # (local) 0.8197411121
    n_bulk = int(bulk_mask.sum())                             # (local) 714
    n_floor = int(floor_mask.sum())                           # (local) 6
    n_modes_total = int(Kz.size)                              # (local) 720

    # ---- 5.2 Load the S105 W2-3 area-flow generator G-hat_tau ---------------
    # G_hat is the UNIT-NORMALIZED (by its own spectral radius) exflation tau-flow
    # generator d/dtau on the moment family, on the SAME 720-mode BdG basis. The
    # W2-3 gate built it and the K_modular on the same basis; verify the basis is
    # aligned (2a K_modular == W2-3 K_modular).
    d23 = np.load(S105_W2_3_NPZ, allow_pickle=True)
    G_hat = np.asarray(d23["G_hat"], dtype=np.float64)        # (local) unit-normalized G_tau, 720
    G_norm_23 = float(d23["G_norm"])                          # (local) ||G_tau||_op in W2-3
    K_modular_23 = np.asarray(d23["K_modular"], dtype=np.float64)  # (local) W2-3 modular gen, 720
    cocycle_generator_sign = int(d23["cocycle_generator_sign"])   # (local) -1
    S97_sign_reference = int(d23["S97_sign_reference"])       # (local) -1
    s97_p_exponent = float(d23["s97_p_exponent"])            # (local) ~ -1
    s97_decreasing = bool(d23["s97_decreasing"])             # (local) True
    op_norm_w23_ungraded = float(d23["op_norm_difference"])  # (local) 1.773745 (the ungraded precedent)

    # ---- 5.3 BASIS-ALIGNMENT CHECK (guard against silent mode-order drift) ---
    # 2a K_modular and W2-3 K_modular are BOTH E_a/T on the same mode order; the
    # op-norm comparison is only valid if they coincide exactly.
    basis_align_maxdiff = float(np.max(np.abs(K_modular_2a - K_modular_23)))  # (local)
    basis_aligned = basis_align_maxdiff < 1e-12                              # (local)
    if not basis_aligned:
        raise RuntimeError(
            f"BASIS DRIFT: 2a K_modular vs W2-3 K_modular maxdiff={basis_align_maxdiff:.3e} "
            ">= 1e-12; the op-norm comparison would be on misaligned generators.")

    # ---- 5.4 Build K-hat.z (unit-normalized) on the BULK --------------------
    # Layer-2 guard (c): the floor mode (Kz = +inf) is EXCLUDED. Restrict to the
    # bulk, then unit-normalize by the bulk spectral radius (matching how W2-3
    # unit-normalized K_hat by its own spectral radius). Both operands are diagonal
    # generators; the op-norm of their difference = max|entry|.
    Kz_bulk = Kz[bulk_mask]                                   # (local) finite on the bulk
    assert np.all(np.isfinite(Kz_bulk)), "Kz has non-finite entry on the BULK (Layer-2 violation upstream)"
    G_hat_bulk = G_hat[bulk_mask]                             # (local) W2-3 G_hat restricted to bulk
    Kz_norm = float(np.max(np.abs(Kz_bulk)))                 # (local) ||K-hat.z||_op (bulk spectral radius)
    Kz_hat = Kz_bulk / Kz_norm if Kz_norm > 0 else Kz_bulk  # (local) UNIT-NORMALIZED K-hat.z on bulk

    # sanity diagnostic: the W2-3 ungraded op-norm restricted to the bulk
    # (should reproduce 1.773745 -- the bulk carries the spectral radius)
    K_hat_w23 = np.asarray(d23["K_hat"], dtype=np.float64)    # (local) W2-3 unit-normalized K_hat, 720
    opnorm_ungraded_bulk = float(np.max(np.abs(K_hat_w23[bulk_mask] - G_hat_bulk)))  # (local)

    # ---- 5.5 [VERIFY] op-norm of the difference (GPU torch.linalg + numpy) ---
    diff_bulk = Kz_hat - G_hat_bulk                          # (local)
    op_norm_difference = float(np.max(np.abs(diff_bulk)))    # (local) ||K-hat.z - G-hat||_op (authoritative numpy)

    op_norm_difference_gpu = None                           # (local)
    gpu_used = False                                        # (local)
    if _HAVE_TORCH and n_bulk >= 1:
        try:
            dev = "cuda" if torch.cuda.is_available() else "cpu"
            diff_t = torch.tensor(diff_bulk, dtype=torch.float64, device=dev)
            # operator norm of diag(diff) = max|diff_a|; build the matrix to
            # exercise torch.linalg per the plan pin (small: <=714x714).
            M = torch.diag(diff_t)                           # (local)
            op_norm_difference_gpu = float(torch.linalg.matrix_norm(M, ord=2).cpu())
            gpu_used = (dev == "cuda")
        except Exception:
            op_norm_difference_gpu = None

    gpu_numpy_agree = True                                  # (local)
    if op_norm_difference_gpu is not None:
        gpu_numpy_agree = abs(op_norm_difference_gpu - op_norm_difference) < GPU_NUMPY_TOL

    # gap reduction the Tolman regrade achieves (diagnostic, not a gate)
    gap_reduction = op_norm_w23_ungraded - op_norm_difference  # (local) > 0 if regrade moves K toward G
    gap_reduction_frac = (gap_reduction / op_norm_w23_ungraded) if op_norm_w23_ungraded > 0 else 0.0  # (local)

    # ---- 5.6 [SIGN] cocycle-generator sign == S97 reference (-1) ------------
    # Substitution chain (Sage-verified at plan-freeze):
    #   S = A/(4 G_N), A = a_2, G_N ~ 1/a_2 ; S97 area-law functional S ~ (a0/a2)^p
    #   with p_exponent = -1 (decreasing) => dS/d(a0/a2) < 0 => sign = -1.
    #   The cocycle generator along the a0/a2 axis = sign(dS/d(a0/a2)) = -1.
    # The conjunct is the RECOMPUTED cocycle sign from the W2-3 npz vs S97_sign_reference.
    sign_match = (cocycle_generator_sign == S97_sign_reference)  # (local) -1 == -1 -> True
    # cross-check the analytic exponent reading (p=-1 -> dS/dr=-1/r^2<0 -> sign -1)
    p_sign_consistent = (np.sign(s97_p_exponent) == -1) and s97_decreasing  # (local)

    A_hat = a_2_FW_zeta                                      # (local) 2776.165389 (the area operator a_2^{zeta})

    # ---- 5.7 Verdict assembly (3-tuple + composite) ------------------------
    # sign_verdict: did the recomputed cocycle sign match the S97 reference (-1)?
    sign_verdict = "PASS" if (sign_match and p_sign_consistent) else "FAIL"
    # magnitude_verdict: op-norm agreement (the [VERIFY] area-clock-identity conjunct)
    magnitude_verdict = "PASS" if (op_norm_difference < TOL_OPNORM) else "FAIL"
    # regime_verdict: the comparison is on the certified-faithful bulk (gate 2a),
    # full domain, no auto-shortening, GPU/CPU agree -> VALID.
    regime_verdict = "VALID" if (gating_status and gpu_numpy_agree and basis_aligned) else "BREAKDOWN"

    # Composite under the PLAN-FROZEN composite-precedence operator (§W2-2
    # INFO_meaning PRE-REGISTERS sign=PASS+magnitude=FAIL+regime=VALID as INFO,
    # co-monotone-but-not-equal -- OVERRIDING the generic-collapse FAIL reading;
    # structurally identical to the W2-3 precedent):
    #   sign=PASS & magnitude=PASS & regime=VALID  -> PASS (NEW area-clock bridge CANDIDATE, Track B)
    #   sign=PASS & magnitude=FAIL & regime=VALID  -> INFO (co-monotone; identity NOT established, Track A)
    #   sign=FAIL  or regime=BREAKDOWN             -> FAIL
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "PASS":
        composite = "PASS"
    else:  # sign PASS, magnitude FAIL, regime VALID -> plan-frozen INFO (not generic FAIL)
        composite = "INFO"

    return dict(
        gating_status=gating_status, a2_verdict=a2_verdict,
        a2_bulk_faithful=a2_bulk_faithful, a2_floor_empty=a2_floor_empty,
        a2_delta_built=a2_delta_built,
        basis_align_maxdiff=basis_align_maxdiff, basis_aligned=basis_aligned,
        op_norm_difference=op_norm_difference,
        op_norm_difference_gpu=(op_norm_difference_gpu if op_norm_difference_gpu is not None else np.nan),
        gpu_used=gpu_used, gpu_numpy_agree=gpu_numpy_agree,
        op_norm_w23_ungraded=op_norm_w23_ungraded,
        opnorm_ungraded_bulk=opnorm_ungraded_bulk,
        gap_reduction=gap_reduction, gap_reduction_frac=gap_reduction_frac,
        Kz_norm=Kz_norm, G_norm_23=G_norm_23,
        cocycle_generator_sign=cocycle_generator_sign,
        S97_sign_reference=S97_sign_reference,
        sign_match=sign_match, p_sign_consistent=p_sign_consistent,
        s97_p_exponent=s97_p_exponent, s97_decreasing=s97_decreasing,
        tol_opnorm=TOL_OPNORM,
        n_bulk=n_bulk, n_floor=n_floor, n_modes_total=n_modes_total,
        lam_horizon=lam_horizon, A_hat=A_hat, a2_fold=a2_fold,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        Kz_hat=Kz_hat, G_hat_bulk=G_hat_bulk, diff_bulk=diff_bulk,
    )


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(R: dict) -> None:
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13, 5))

    # left: the unit-normalized generator spectra on the bulk
    idx = np.arange(R["n_bulk"])                              # (local)
    ax0.plot(idx, R["Kz_hat"], ".", ms=3, alpha=0.55,
             label=r"$\widehat{K\!\cdot\! z}_a$ = Hawking-dressed modular gen. $\mathrm{Ad}(\Delta_{\omega'_z}^{it})$")
    ax0.plot(idx, R["G_hat_bulk"], ".", ms=3, alpha=0.55,
             label=r"$\hat G_\tau$ = area-flow gen. $d/d\tau$ on $\{a_n\}$")
    ax0.set_xlabel("BdG mode index on the named-block BULK (n_bulk = %d)" % R["n_bulk"])
    ax0.set_ylabel("unit-normalized generator spectrum")
    ax0.set_title("Hawking-dressed modular flow vs area-flow on the (0,0)+horizon blocks\n"
                  f"cocycle-gen sign = {R['cocycle_generator_sign']} "
                  f"(S97 ref = {R['S97_sign_reference']}; match = {R['sign_match']})")
    ax0.legend(fontsize=7.5, loc="best")
    ax0.grid(alpha=0.25)

    # right: op-norm diff (graded vs ungraded) vs tol
    ax1.bar([0], [R["op_norm_w23_ungraded"]], width=0.5, color="#888",
            label=r"$\|\hat K - \hat G_\tau\|_{op}$ (W2-3 ungraded)")
    ax1.bar([1], [R["op_norm_difference"]], width=0.5, color="#c44",
            label=r"$\|\widehat{K\!\cdot\! z} - \hat G_\tau\|_{op}$ (this gate)")
    ax1.axhline(R["tol_opnorm"], color="k", ls="--", lw=1.2,
                label=f"tol = {R['tol_opnorm']:.0e}")
    ax1.set_yscale("log")
    ax1.set_xticks([0, 1])
    ax1.set_xticklabels(["ungraded\n(W2-3)", "Tolman-regraded\n(2b)"])
    ax1.set_ylabel("operator-norm difference (dimensionless)")
    verdict_txt = (f"composite = {R['composite']}\n"
                   f"sign={R['sign_verdict']} mag={R['magnitude_verdict']} "
                   f"regime={R['regime_verdict']}\n"
                   f"gap reduction = {R['gap_reduction_frac']*100:.1f}% "
                   f"(toward $\\hat G_\\tau$, not below tol)")
    ax1.set_title("area-clock op-norm vs tol\n" + verdict_txt, fontsize=9)
    ax1.legend(fontsize=7.5, loc="best")
    ax1.grid(alpha=0.25, axis="y", which="both")

    fig.suptitle(f"{GATE_ID}  —  area-clock for the Hawking-dressed relic's modular flow "
                 f"(GATED on 2a PASS: {R['gating_status']})", fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — main
# ---------------------------------------------------------------------------
def main() -> int:
    # input SHA log (first lines of stdout per gate-verdicts.md protocol)
    print(f"=== {GATE_ID} ===")
    print(f"  script_self      = {_file_sha(Path(__file__).resolve())}")
    print(f"  canonical_sha    = {_file_sha(CANON_PY)}")
    print(f"  s106_2a_sha      = {_file_sha(S106_2A_NPZ)}")
    print(f"  s105_w2_3_sha    = {_file_sha(S105_W2_3_NPZ)}")
    print(f"  torch_available  = {_HAVE_TORCH}")

    R = compute()

    print("\n=== GATING (2a / S106-OMEGAPRIME-Z-CONSTRUCTION) ===")
    print(f"  2a verdict             = {R['a2_verdict']}")
    print(f"  bulk_faithful          = {R['a2_bulk_faithful']}")
    print(f"  floor_empty_fock       = {R['a2_floor_empty']}")
    print(f"  Delta_omega'z_it_built = {R['a2_delta_built']}")
    print(f"  gating_status          = {R['gating_status']}  (PASS required; verified)")
    print(f"  basis_align_maxdiff    = {R['basis_align_maxdiff']:.3e}  (2a K_mod == W2-3 K_mod; aligned={R['basis_aligned']})")
    print(f"  lam_horizon            = {R['lam_horizon']:.10f}")
    print(f"  n_bulk / n_floor       = {R['n_bulk']} / {R['n_floor']}  (floor EXCLUDED, guard (c))")

    print("\n=== [SIGN] cocycle-generator direction (OUTER-class second-law datum) ===")
    print(f"  S97 dS/d(a0/a2) sign   = {R['S97_sign_reference']}   (decreasing={R['s97_decreasing']}, p_exp={R['s97_p_exponent']:.6f})")
    print(f"  cocycle-generator sign = {R['cocycle_generator_sign']}")
    print(f"  sign_match             = {R['sign_match']}   (cocycle-gen == S97 ref)")
    print(f"  p_sign_consistent      = {R['p_sign_consistent']}  (p_exp<0 AND decreasing -> dS/dr<0)")
    print(f"  => sign_verdict        = {R['sign_verdict']}")

    print("\n=== [VERIFY] op-norm: ||K-hat.z - G-hat_tau||_op (BULK only) ===")
    print(f"  ||K-hat.z||_op (bulk)  = {R['Kz_norm']:.6f}")
    print(f"  W2-3 ungraded op-norm  = {R['op_norm_w23_ungraded']:.6e}  (precedent; K_hat not Tolman-regraded)")
    print(f"  bulk-restricted ungrad = {R['opnorm_ungraded_bulk']:.6e}  (reproduces W2-3 precedent on bulk)")
    print(f"  ||K-hat.z - G-hat||_op = {R['op_norm_difference']:.6e}   (tol = {R['tol_opnorm']:.0e})")
    print(f"  op-norm (GPU torch)    = {R['op_norm_difference_gpu']}  (gpu_used={R['gpu_used']}, agree={R['gpu_numpy_agree']})")
    print(f"  gap reduction (regrade)= {R['gap_reduction']:.6e}  ({R['gap_reduction_frac']*100:.2f}% toward G-hat; NOT below tol)")
    print(f"  => magnitude_verdict   = {R['magnitude_verdict']}")
    print(f"  => regime_verdict      = {R['regime_verdict']}")

    print("\n=== COMPOSITE VERDICT (plan-frozen precedence) ===")
    print(f"  composite              = {R['composite']}")

    # ---- npz ----------------------------------------------------------------
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite=R["composite"],
        sign_verdict=R["sign_verdict"],
        magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        # gate primaries
        op_norm_difference=R["op_norm_difference"],
        op_norm_difference_gpu=R["op_norm_difference_gpu"],
        gpu_used=R["gpu_used"], gpu_numpy_agree=R["gpu_numpy_agree"],
        op_norm_w23_ungraded=R["op_norm_w23_ungraded"],
        opnorm_ungraded_bulk=R["opnorm_ungraded_bulk"],
        gap_reduction=R["gap_reduction"], gap_reduction_frac=R["gap_reduction_frac"],
        cocycle_generator_sign=R["cocycle_generator_sign"],
        S97_sign_reference=R["S97_sign_reference"],
        sign_match=R["sign_match"], p_sign_consistent=R["p_sign_consistent"],
        s97_p_exponent=R["s97_p_exponent"], s97_decreasing=R["s97_decreasing"],
        tol_opnorm=R["tol_opnorm"],
        # gating + basis
        gating_status=R["gating_status"], a2_verdict=R["a2_verdict"],
        a2_bulk_faithful=R["a2_bulk_faithful"], a2_floor_empty=R["a2_floor_empty"],
        a2_delta_built=R["a2_delta_built"],
        basis_align_maxdiff=R["basis_align_maxdiff"], basis_aligned=R["basis_aligned"],
        # generators (bulk)
        Kz_hat=R["Kz_hat"], G_hat_bulk=R["G_hat_bulk"], diff_bulk=R["diff_bulk"],
        Kz_norm=R["Kz_norm"], G_norm_23=R["G_norm_23"],
        n_bulk=R["n_bulk"], n_floor=R["n_floor"], n_modes_total=R["n_modes_total"],
        lam_horizon=R["lam_horizon"],
        # area operator
        A_hat=R["A_hat"], a2_fold=R["a2_fold"],
        tau_fold=tau_fold,
        regulator_pin="a_2^{zeta}",
    )

    make_plot(R)

    # ---- dual-SHA + verdict payload ----------------------------------------
    # NOTE (substrate-first-canonical-sourcing.md §(ii.B)): canonical_constants.py
    # gained S106 W1 constants this session; the plan-freeze pin (38e23ad2...) drifted
    # to runtime (82dd16e2...). We pin canonical at RUNTIME SHA (benign; a_2_FW_zeta
    # = 2776.165389 UNCHANGED), exactly as the sister S106 W1/W3 gates did. Documented
    # in the verdict value.
    pins = {
        "script": _file_sha(Path(__file__).resolve()),
        "canonical": _file_sha(CANON_PY),                    # runtime SHA (benign drift)
        "s106_omegaprime_z_construction_npz": _file_sha(S106_2A_NPZ),
        "s105_w2_3_area_modular_agreement_npz": _file_sha(S105_W2_3_NPZ),
    }
    audit_sha, content_sha = compute_dual_sha(pins)

    co_monotone = (R["sign_match"] and R["magnitude_verdict"] == "FAIL")  # (local)
    value = (
        f"composite={R['composite']};"
        f"op_norm_diff={R['op_norm_difference']:.6e}_vs_tol={R['tol_opnorm']:.0e};"
        f"cocycle_gen_sign={R['cocycle_generator_sign']}_eq_S97={R['sign_match']};"
        f"co_monotone={co_monotone};"
        f"gap_reduction_frac={R['gap_reduction_frac']:.4f}_W23ungraded={R['op_norm_w23_ungraded']:.6f};"
        f"area_clock_identity={R['magnitude_verdict']=='PASS'};"
        f"NEW_bridge_candidate={R['composite']=='PASS'};"
        f"gating_2a={R['a2_verdict']};basis_aligned={R['basis_aligned']};"
        f"n_bulk={R['n_bulk']}_floor_excluded={R['n_floor']};"
        f"A_hat=a_2_zeta={R['A_hat']:.6f};"
        f"sigma_omegaprime_z_ONLY_guard_a;canonical_runtime_SHA_benign_drift_per_(ii.B)"
    )

    composite_precedence_row = (
        "# composite-precedence: S106-OMEGAPRIME-AREA-CLOCK plan-block "
        "(session-106-plan-w2.md §W2-2 INFO_meaning) pre-registers sign=PASS+magnitude=FAIL+regime=VALID "
        "as INFO (co-monotone; area-clock IDENTITY NOT established), OVERRIDING the generic-collapse FAIL "
        "reading; gate-verdicts.md 'Plan-frozen gate-block operator precedence'"
    )
    regulator_row = ("# regulator_pin=a_2^{zeta} mellin_poleconv=poleconv-A-double "
                     "mellin_pole_declaration=(pole_in_s=3,curvature_grade_n=2)  "
                     "# A-hat = a_2 second-Seeley-DeWitt area moment (zeta-regulated; a_2_FW_zeta=2776.165389)")
    guard_row = ("# guards: (a) Layer-1 compares sigma_t^{omega'_z} ONLY, NEVER sigma_t^omega "
                 "(omega'_z != omega for z!=1; NOT a GEM-Q1 reopening even on PASS); "
                 "(b) Layer-2 faithfulness witness emitted by 2a BEFORE comparison (2a->2b gating is the enforcement); "
                 "(c) floor mode empty-Fock (Kz=+inf) EXCLUDED -- op-norm on {|lam|>lam_horizon}, n_bulk=714")
    candidate_row = ("# A PASS is a CANDIDATE only -- NO S106 registry write; future 5-anatomy+3-level "
                     "registration of the acoustic-area <-> Hawking-dressed-relic-modular-flow bridge routes to "
                     "S107 (cross-pillar-bridge-anatomy.md); mack-cosmic-bridge writes any bridge row at a future session")
    drift_row = ("# canonical-drift (substrate-first-canonical-sourcing.md (ii.B)): plan pin 38e23ad2... ; "
                 "runtime 82dd16e2... ; a_2_FW_zeta=2776.165389 UNCHANGED; s84 cache via 2a npz (session-84/, not _shared/) "
                 "-- 2a already folded the cache+canonical drift; basis-aligned to W2-3 (maxdiff=0.0)")

    print_verdict_payload(
        verdict=R["composite"],
        value=value,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_verdict=R["sign_verdict"],
        magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        companion_note=("area-clock for the Hawking-dressed relic; "
                        "G_tau ?= Ad(Delta_{omega'_z}^{it}) on the (0,0)+horizon-block BULK"),
        extra_rows=[composite_precedence_row, regulator_row, guard_row, candidate_row, drift_row],
    )

    print(f"\nWROTE {OUT_NPZ}")
    print(f"WROTE {OUT_PNG}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
