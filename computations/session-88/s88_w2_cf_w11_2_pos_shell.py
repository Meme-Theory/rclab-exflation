#!/usr/bin/env python3
"""
S88 W2-5 — S88-CF-W11-2-POS-SHELL
==================================

Gate: S88-CF-W11-2-POS-SHELL (trigger: VERIFY)
Wave: W2 (positive-side asymmetry probe at delta_tau in {+0.15, +0.20, +0.25})
Plan: sessions/session-plan/session-88-plan-w2.md §W2-5

Pre-registered threshold (per session-88-plan-w2.md §W2-5.9):
  PASS: delta_tau_crit_positive characterized to +/- 0.05 grid precision OR
        confirmed absence within delta_tau <= 0.25 (cv stays (2, 4, 8, 6)).
  INFO: cardinality structure inconsistent with tau-asymmetry expectation.
  FAIL: numerical breakdown at L_max=6.

Cross-check: compare delta_tau_crit_positive vs delta_tau_crit_negative (W2-4).
The substrate's tau-asymmetric breakdown direction (W-8 R3 finding) predicts
either |delta_tau_crit_negative| < |delta_tau_crit_positive| OR positive-side
absence-of-breakdown.

Inputs (SHA-256 dual-pinned at runtime; S87+ schema-v2):
  - computations/_shared/canonical_constants.py
  - computations/_shared/dirac_spectrum.py
  - computations/session-87/s87_w11_partition_stability_4stratum.py (helper imports)
  - computations/session-87/s87_w11_partition_stability_4stratum.npz (W11-2 anchor)
  - script bytes

Output 4-tuple:
  (value=delta_tau_crit_positive_or_NONE,
   scheme=sub-delta-tau-shell-scan-positive-side,
   convention=4-stratum-W11-2-canonical-partition-rule,
   L_max=6)

Classification: GEOMETRIC

DISCIPLINE
----------
Mirrors W2-4 structure with positive delta_tau values; reuses W11-2 helpers.
"""

from __future__ import annotations

# Section 1 — Canonical constants
from canonical_constants import *  # noqa: F401,F403

# Section 2 — Standard imports
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Level-1 Dirac primitives
from dirac_spectrum import (  # noqa: E402
    su3_generators,
    compute_structure_constants,
    build_cliff8,
)

# Reuse W11-2 helpers
import importlib.util as _ilu
_w11_2_spec = _ilu.spec_from_file_location(
    "_w11_2_helpers",
    str(Path(__file__).resolve().parent / "s87_w11_partition_stability_4stratum.py")
)
_w11_2 = _ilu.module_from_spec(_w11_2_spec)
_w11_2_spec.loader.exec_module(_w11_2)
precompute_tau_independent = _w11_2.precompute_tau_independent
compute_bottom20_at_tau = _w11_2.compute_bottom20_at_tau
cardinality_vector_helper = _w11_2.cardinality_vector

# Section 3 — Pin metadata
GATE_ID = "S88-CF-W11-2-POS-SHELL"
SCHEME = "sub-delta-tau-shell-scan-positive-side"
CONVENTION = "4-stratum-W11-2-canonical-partition-rule"
L_MAX_OPERATIONAL = 6        # (local) Casimir-bound truncation
L_MAX_PLAN = 10              # (local)
N_BOT = 20                   # (local)
ULP_TOL = 1e-14              # (local) W11-2 partition equivalence tolerance
GRID_PRECISION = 0.05        # (local) plan-pinned ± 0.05 grid spacing for positive scan
DELTA_TAU_GRID = (+0.15, +0.20, +0.25)  # (local) plan-pinned positive scan
CV_ANCHOR = (2, 4, 8, 6)     # (local)

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w2_cf_w11_2_pos_shell.py"
NPZ_OUT = T0 / "s88_w2_cf_w11_2_pos_shell.npz"
PNG_OUT = T0 / "s88_w2_cf_w11_2_pos_shell.png"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

CANON_PY = T0 / "canonical_constants.py"
HELPER_PY = T0 / "dirac_spectrum.py"
W11_2_PY = T0 / "s87_w11_partition_stability_4stratum.py"
W11_2_NPZ = T0 / "s87_w11_partition_stability_4stratum.npz"
W2_4_NPZ = T0 / "s88_w2_cf_w11_2_neg_shell.npz"  # cross-check vs negative-side


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def main() -> int:
    t_start = time.time()                                                  # (local)

    # 4.1 — Setup tau-independent infrastructure
    print(f"[W2-5] Building SU(3) infrastructure at L_max={L_MAX_OPERATIONAL} ...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    B_ab, rho_table = precompute_tau_independent(gens, f_abc, L_MAX_OPERATIONAL)
    print(f"[W2-5] rho_table = {len(rho_table)} non-trivial sectors")

    # 4.2 — Scan positive-side delta_tau values
    cv_per_dtau: dict[float, tuple[int, ...]] = {}
    bot20_per_dtau: dict[float, np.ndarray] = {}
    for delta_tau in DELTA_TAU_GRID:
        tau_eval = float(tau_fold) + float(delta_tau)
        print(f"[W2-5] Computing bot-20 at tau = {tau_eval:.4f} (delta_tau = {delta_tau:+.4f}) ...")
        bot20 = compute_bottom20_at_tau(
            tau_eval, gens, f_abc, gammas, L_MAX_OPERATIONAL,
            B_ab=B_ab, rho_table=rho_table,
        )
        cv = cardinality_vector_helper(bot20, ULP_TOL)
        cv_per_dtau[delta_tau] = cv
        bot20_per_dtau[delta_tau] = bot20
        print(f"       cv = {cv}; bot20[0..3] = {bot20[:4].tolist()}")

    # 4.3 — Localize delta_tau_crit_positive (or confirm absence)
    intact_dtaus = sorted([dt for dt in DELTA_TAU_GRID if cv_per_dtau[dt] == CV_ANCHOR])
    broken_dtaus = sorted([dt for dt in DELTA_TAU_GRID if cv_per_dtau[dt] != CV_ANCHOR])
    if not broken_dtaus:
        delta_tau_crit_positive_or_NONE = float("inf")  # (local) absence within scan
        composite = "PASS"
        verdict_kind = "PASS-no-breakdown-within-positive-scan-window"  # (local)
    elif intact_dtaus and broken_dtaus:
        max_intact_dt = max(intact_dtaus)
        min_broken_dt = min(broken_dtaus)
        if min_broken_dt > max_intact_dt:
            delta_tau_crit_positive_or_NONE = (max_intact_dt + min_broken_dt) / 2.0
            composite = "PASS"
            verdict_kind = "PASS-localized-positive-side-breakdown"  # (local)
        else:
            delta_tau_crit_positive_or_NONE = (max_intact_dt + min_broken_dt) / 2.0
            composite = "INFO"
            verdict_kind = "INFO-non-monotonic-positive-cv-transition"  # (local)
    else:  # all broken
        delta_tau_crit_positive_or_NONE = float(min(DELTA_TAU_GRID)) - GRID_PRECISION
        composite = "INFO"
        verdict_kind = "INFO-all-positive-broken-breakdown-tighter-than-scan-window"  # (local)

    print(f"[W2-5] intact dtaus: {intact_dtaus}; broken dtaus: {broken_dtaus}")
    print(f"[W2-5] delta_tau_crit_positive_or_NONE = {delta_tau_crit_positive_or_NONE}")

    # 4.4 — Tau-asymmetry comparison vs W2-4
    delta_tau_crit_negative = None  # (local)
    asymmetry_match = None          # (local)
    if W2_4_NPZ.exists():
        d_neg = np.load(W2_4_NPZ, allow_pickle=True)
        delta_tau_crit_negative = float(d_neg["delta_tau_crit_negative_estimate"])
        # Plan §W2-5 Step 4: substrate predicts |dt_crit_neg| < |dt_crit_pos| OR positive-absence
        if delta_tau_crit_positive_or_NONE == float("inf"):
            asymmetry_match = True  # positive-absence direction satisfied
        else:
            asymmetry_match = bool(abs(delta_tau_crit_negative) < abs(delta_tau_crit_positive_or_NONE))
        print(f"[W2-5] CC1 tau-asymmetry: |dt_neg|={abs(delta_tau_crit_negative):.4f} vs |dt_pos|={abs(delta_tau_crit_positive_or_NONE) if delta_tau_crit_positive_or_NONE != float('inf') else 'inf'}; match={asymmetry_match}")

    # 4.5 — SHAs and pin map
    canon_sha = sha256_file(CANON_PY)
    helper_sha = sha256_file(HELPER_PY)
    w11_2_py_sha = sha256_file(W11_2_PY)
    w11_2_npz_sha = sha256_file(W11_2_NPZ)
    w2_4_sha = sha256_file(W2_4_NPZ) if W2_4_NPZ.exists() else "NOT_AVAILABLE"
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha
    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_OPERATIONAL,
        "tau_fold": float(tau_fold),
        "delta_tau_grid": list(DELTA_TAU_GRID),
        "cv_anchor": list(CV_ANCHOR),
        "ULP_TOL": ULP_TOL,
        "GRID_PRECISION": GRID_PRECISION,
        "input_canonical_constants_sha256": canon_sha,
        "input_dirac_spectrum_sha256": helper_sha,
        "input_w11_2_helper_py_sha256": w11_2_py_sha,
        "input_w11_2_npz_sha256": w11_2_npz_sha,
        "input_w2_4_npz_sha256": w2_4_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    # 4.6 — Save .npz
    np.savez(
        NPZ_OUT,
        delta_tau_grid=np.array(DELTA_TAU_GRID),
        tau_eval_grid=np.array([tau_fold + dt for dt in DELTA_TAU_GRID]),
        cv_per_dtau=np.array([cv_per_dtau[dt] for dt in DELTA_TAU_GRID]),
        bot20_per_dtau=np.array([bot20_per_dtau[dt] for dt in DELTA_TAU_GRID]),
        cv_anchor=np.array(CV_ANCHOR),
        intact_dtaus=np.array(intact_dtaus, dtype=np.float64),
        broken_dtaus=np.array(broken_dtaus, dtype=np.float64),
        delta_tau_crit_positive_or_NONE=np.float64(delta_tau_crit_positive_or_NONE),
        delta_tau_crit_negative_W2_4=np.float64(delta_tau_crit_negative if delta_tau_crit_negative is not None else float("nan")),
        asymmetry_match=np.bool_(asymmetry_match) if asymmetry_match is not None else np.bool_(False),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
        L_max_operational=np.int64(L_MAX_OPERATIONAL),
    )

    # 4.7 — Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title(f"S88 W2-5 — Positive-side shell scan; tau-asymmetric probe")
    for dt in DELTA_TAU_GRID:
        ax.plot(np.arange(N_BOT), bot20_per_dtau[dt], marker="o",
                label=f"dt={dt:+.3f} cv={cv_per_dtau[dt]}")
    ax.set_xlabel("substrate index k")
    ax.set_ylabel("|lambda_k|")
    ax.legend(loc="best", fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(PNG_OUT, dpi=120)
    plt.close()

    # 4.8 — Append verdict line
    elapsed = time.time() - t_start
    pos_str = "inf" if delta_tau_crit_positive_or_NONE == float("inf") else f"{delta_tau_crit_positive_or_NONE:.4f}"
    value_str = (
        f"delta_tau_crit_positive_or_NONE={pos_str};"
        f"delta_tau_crit_negative_W2_4={delta_tau_crit_negative};"
        f"asymmetry_match={asymmetry_match};"
        f"intact_dtaus={intact_dtaus};broken_dtaus={broken_dtaus};"
        f"verdict_kind={verdict_kind};L_max_op={L_MAX_OPERATIONAL}"
    )
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_OPERATIONAL} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S87+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    sign_v = "PASS" if asymmetry_match else "N/A"
    mag_v = composite
    regime_v = "VALID"
    tuple_line = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_line)
        f.write(tuple_line)

    print(f"[W2-5] DONE in {elapsed:.2f}s")
    print(f"[W2-5] composite = {composite} (verdict_kind={verdict_kind})")
    print(f"[W2-5] audit_sha256 = {audit_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
