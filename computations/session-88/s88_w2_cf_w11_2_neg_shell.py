#!/usr/bin/env python3
"""
S88 W2-4 — S88-CF-W11-2-NEG-SHELL
==================================

Gate: S88-CF-W11-2-NEG-SHELL (trigger: VERIFY)
Wave: W2 (sub-delta_tau negative-side shell scan to localize partition-breakdown threshold)
Plan: sessions/session-plan/session-88-plan-w2.md §W2-4

Pre-registered threshold (per session-88-plan-w2.md §W2-4.9):
  PASS: delta_tau_crit_negative localized to a single grid edge +/- 0.005 with
        cardinality consistent with W11-2 (deviation at delta_tau = -0.10;
        intact at delta_tau = -0.05).
  INFO: scan reveals cardinality structure inconsistent with W11-2.
  FAIL: scan diverges (eigenvalue computation breaks down at L_max=6).

Inputs (SHA-256 dual-pinned at runtime; S87+ schema-v2):
  - computations/_shared/canonical_constants.py
  - computations/_shared/dirac_spectrum.py    (compute_bottom20 primitives)
  - computations/session-87/s87_w11_partition_stability_4stratum.py (helper imports)
  - computations/session-87/s87_w11_partition_stability_4stratum.npz  (W11-2 anchor cv)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=delta_tau_crit_negative_estimate,
   scheme=sub-delta-tau-shell-scan-negative-side,
   convention=4-stratum-W11-2-canonical-partition-rule,
   L_max=6)

Classification: GEOMETRIC

METHODOLOGY
-----------
delta_tau scan grid: {-0.06, -0.07, -0.08, -0.09}; tau values
{0.13, 0.12, 0.11, 0.10}. At each tau, compute bot-20 D_K eigenvalues
(L_max_op=6 Casimir-bound truncation), partition into stratum equivalence
classes (ULP_TOL=1e-14), compare cardinality vector to (2,4,8,6) anchor.
delta_tau_crit_negative = largest |delta_tau| with cv == (2,4,8,6) AND
smallest |delta_tau| with cv != (2,4,8,6), reported as a 0.005-precision band.

W11-2 cache anchor: tau=0.09 (delta_tau=-0.10) has cv-flip to (4,2,8,6);
tau=0.14 (delta_tau=-0.05) has cv intact (2,4,8,6). The shell scan refines
this transition window from [-0.10, -0.05] (size 0.05) down to a sub-grid
window of size 0.01 (i.e., a single edge +/- 0.005 on the {-0.06..-0.09} grid).

DISCIPLINE
----------
- `from canonical_constants import *`
- All locals tagged `# (local)`
- Dual-SHA verdict line per S87+ schema-v2
- Reuses W11-2 primitives (precompute_tau_independent + compute_bottom20_at_tau)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Level-1 Dirac primitives (per S12 / dirac_spectrum.py)
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

# ---------------------------------------------------------------------------
# Section 3 — Pin metadata
# ---------------------------------------------------------------------------
GATE_ID = "S88-CF-W11-2-NEG-SHELL"
SCHEME = "sub-delta-tau-shell-scan-negative-side"
CONVENTION = "4-stratum-W11-2-canonical-partition-rule"
L_MAX_OPERATIONAL = 6        # (local) Casimir-bound truncation per math-scripts.md
L_MAX_PLAN = 10              # (local)
N_BOT = 20                   # (local)
ULP_TOL = 1e-14              # (local) W11-2 partition equivalence tolerance
GRID_PRECISION = 0.005       # (local) plan-pinned ± 0.005 grid spacing
DELTA_TAU_GRID = (-0.06, -0.07, -0.08, -0.09)  # (local) plan-pinned scan set
CV_ANCHOR = (2, 4, 8, 6)     # (local) W11-2 anchor cardinality at tau_fold

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w2_cf_w11_2_neg_shell.py"
NPZ_OUT = T0 / "s88_w2_cf_w11_2_neg_shell.npz"
PNG_OUT = T0 / "s88_w2_cf_w11_2_neg_shell.png"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

CANON_PY = T0 / "canonical_constants.py"
HELPER_PY = T0 / "dirac_spectrum.py"
W11_2_PY = T0 / "s87_w11_partition_stability_4stratum.py"
W11_2_NPZ = T0 / "s87_w11_partition_stability_4stratum.npz"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Section 4 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t_start = time.time()                                                  # (local)

    # 4.1 — Setup tau-independent geometric infrastructure
    print(f"[W2-4] Building SU(3) generators + Killing form + irrep table at L_max={L_MAX_OPERATIONAL} ...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    B_ab, rho_table = precompute_tau_independent(gens, f_abc, L_MAX_OPERATIONAL)
    print(f"[W2-4] rho_table has {len(rho_table)} non-trivial sectors at L_max={L_MAX_OPERATIONAL}")

    # 4.2 — Scan negative-side delta_tau values
    cv_per_dtau: dict[float, tuple[int, ...]] = {}                         # (local)
    bot20_per_dtau: dict[float, np.ndarray] = {}                           # (local)
    for delta_tau in DELTA_TAU_GRID:
        tau_eval = float(tau_fold) + float(delta_tau)                       # (local)
        print(f"[W2-4] Computing bot-20 at tau = {tau_eval:.4f} (delta_tau = {delta_tau:+.4f}) ...")
        bot20 = compute_bottom20_at_tau(
            tau_eval, gens, f_abc, gammas, L_MAX_OPERATIONAL,
            B_ab=B_ab, rho_table=rho_table,
        )
        cv = cardinality_vector_helper(bot20, ULP_TOL)
        cv_per_dtau[delta_tau] = cv
        bot20_per_dtau[delta_tau] = bot20
        print(f"       cv = {cv}; bot20[0..3] = {bot20[:4].tolist()}")

    # 4.3 — Localize delta_tau_crit_negative
    # We expect cv == CV_ANCHOR for SOME delta_tau values and cv != CV_ANCHOR
    # for OTHERS; the transition delta_tau_crit_negative localizes the boundary.
    intact_dtaus = sorted(
        [dt for dt in DELTA_TAU_GRID if cv_per_dtau[dt] == CV_ANCHOR],
        key=lambda x: -x,  # ascending |delta_tau|
    )
    broken_dtaus = sorted(
        [dt for dt in DELTA_TAU_GRID if cv_per_dtau[dt] != CV_ANCHOR],
        key=lambda x: -x,
    )

    if not intact_dtaus and not broken_dtaus:
        delta_tau_crit_negative_estimate = float("nan")                    # (local)
        composite = "FAIL"
        verdict_kind = "FAIL-empty-scan-no-data"                           # (local)
    elif intact_dtaus and broken_dtaus:
        # Largest |delta_tau| that is INTACT vs smallest |delta_tau| that is BROKEN
        max_intact_dt = min(intact_dtaus, key=lambda x: -x)                # (local) least negative
        min_broken_dt = max(broken_dtaus, key=lambda x: -x)                # (local) most negative
        # We expect intact to be at less-negative dt and broken at more-negative dt
        # (per W11-2: -0.05 intact, -0.10 broken)
        if max_intact_dt > min_broken_dt:  # i.e., max_intact > min_broken (less neg vs more neg)
            delta_tau_crit_negative_estimate = (max_intact_dt + min_broken_dt) / 2.0
            composite = "PASS"
            verdict_kind = "PASS-localized-grid-edge-pm-0p005"             # (local)
        else:
            delta_tau_crit_negative_estimate = (max_intact_dt + min_broken_dt) / 2.0
            composite = "INFO"
            verdict_kind = "INFO-non-monotonic-cv-transition"              # (local)
    elif intact_dtaus and not broken_dtaus:
        # All scan points intact → breakdown lies BELOW (more negative than) min(scan)
        delta_tau_crit_negative_estimate = float(min(DELTA_TAU_GRID)) - GRID_PRECISION
        composite = "INFO"
        verdict_kind = "INFO-all-intact-breakdown-beyond-scan-window"      # (local)
    else:  # broken_dtaus only
        # All scan points broken → breakdown lies ABOVE (less negative than) max(scan)
        delta_tau_crit_negative_estimate = float(max(DELTA_TAU_GRID)) + GRID_PRECISION
        composite = "INFO"
        verdict_kind = "INFO-all-broken-breakdown-tighter-than-scan-window"  # (local)

    print(f"[W2-4] intact dtaus: {intact_dtaus}; broken dtaus: {broken_dtaus}")
    print(f"[W2-4] delta_tau_crit_negative_estimate = {delta_tau_crit_negative_estimate:.4f}")

    # 4.4 — Cross-check W11-2 anchor (CC1: cv consistency)
    d_w11 = np.load(W11_2_NPZ, allow_pickle=True)
    cc1_w11_2_anchor_match = bool(
        tuple(d_w11["cardinality_vector_per_tau"][5][:4].tolist()) == CV_ANCHOR
    )
    cc2_w11_2_outer_breakdown = bool(
        d_w11["delta_tau_breakdown_threshold"] == 0.10
    )
    print(f"[W2-4] CC1: W11-2 cv anchor (2,4,8,6) at tau_fold: {cc1_w11_2_anchor_match}")
    print(f"[W2-4] CC2: W11-2 outer-shell breakdown at delta_tau=-0.10: {cc2_w11_2_outer_breakdown}")

    # 4.5 — SHAs and pin map
    canon_sha = sha256_file(CANON_PY)
    helper_sha = sha256_file(HELPER_PY)
    w11_2_py_sha = sha256_file(W11_2_PY)
    w11_2_npz_sha = sha256_file(W11_2_NPZ)
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
        delta_tau_crit_negative_estimate=np.float64(delta_tau_crit_negative_estimate),
        cc1_w11_2_anchor_match=np.bool_(cc1_w11_2_anchor_match),
        cc2_w11_2_outer_breakdown=np.bool_(cc2_w11_2_outer_breakdown),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
        L_max_operational=np.int64(L_MAX_OPERATIONAL),
    )

    # 4.7 — Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title(f"S88 W2-4 — Negative-side shell scan; cv-flip threshold")
    for dt in DELTA_TAU_GRID:
        bot = bot20_per_dtau[dt]
        ax.plot(np.arange(N_BOT), bot, marker="o", label=f"dt={dt:+.3f} cv={cv_per_dtau[dt]}")
    ax.set_xlabel("substrate index k (sorted by |lambda|)")
    ax.set_ylabel("|lambda_k|")
    ax.legend(loc="best", fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(PNG_OUT, dpi=120)
    plt.close()

    # 4.8 — Append verdict line
    elapsed = time.time() - t_start
    value_str = (
        f"delta_tau_crit_negative_estimate={delta_tau_crit_negative_estimate:.4f};"
        f"intact_dtaus={intact_dtaus};broken_dtaus={broken_dtaus};"
        f"cv_per_dtau={ {f'{dt:+.3f}': cv_per_dtau[dt] for dt in DELTA_TAU_GRID} };"
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
    sign_v = "N/A"
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

    print(f"[W2-4] DONE in {elapsed:.2f}s")
    print(f"[W2-4] composite = {composite} (verdict_kind={verdict_kind})")
    print(f"[W2-4] audit_sha256 = {audit_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
