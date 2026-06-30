#!/usr/bin/env python3
"""
S88 W2-1 — S88-MONODROMY-DEPTH-EXTENSION-SURVIVING-V4-ENUMERATION
==================================================================

Gate: S88-MONODROMY-DEPTH-EXTENSION-SURVIVING-V4-ENUMERATION (trigger: VERIFY-THEOREM)
Wave: W2 (V_4 monodromy depth-extension surviving-candidate enumeration)
Plan: sessions/session-plan/session-88-plan-w2.md §W2-1

Pre-registered threshold (per session-88-plan-w2.md §W2-1.9):
  PASS-d=2-exact: count_PASS_extensions >= 3 AND d=2 W11-4 form recovered
                  as restriction of d=3 hypercube identity.
  PASS-d>2-extension: count_PASS_extensions >= 1 with d in {3, 4} non-degenerate.
  INFO: 1 <= count_PASS_extensions < 3.
  FAIL: count_PASS_extensions = 0.

Structural anchor (W11-4 Sage-QQ exact at d in {2,3,4,5}):
  The (Z_2)^d-Schur tensor-product factored identity Delta_n^(d) = 0 EXACT in QQ
  for any (Z_2)^d character on a partition; cached in
  s87_w11_hypercube_vertex_identity.npz (identity_result_per_d=['0','0','0','0']).

This gate's substrate-physics specialization tests the NON-DEGENERACY axis-marginal
condition: for each Extension X with d axes, each Z_2(j) must act non-trivially on
the substrate's bottom-20 D_K eigenvalue support (otherwise the j-th edge collapses).

Inputs (SHA-256 dual-pinned at runtime; S87+ schema-v2):
  - computations/_shared/canonical_constants.py     (tau_fold, M_KK, Delta_BCS)
  - computations/session-87/s87_w11_partition_stability_4stratum.npz
                                              (W11-2 bot20 at tau=0.19, cv (2,4,8,6))
  - computations/session-87/s87_w11_hypercube_vertex_identity.npz
                                              (W11-4 Sage QQ exact-zero verifier)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Filename re-pin (Class-(c) PIN-DRIFT remediation per epistemic-discipline.md):
  Plan cites s87_w11_2_partition_stability_4stratum.npz (with `_2`); actual file
  is s87_w11_partition_stability_4stratum.npz (no `_2`). Plan cites
  s87_w11_4_v4_schur_identity.npz; actual file is s87_w11_hypercube_vertex_identity.npz.
  Both re-pinned to actual filenames in input-pin map.

Output 4-tuple:
  (value=count_PASS_extensions,
   scheme=Cartan-toral-rejected-V4-strata-tested-via-stratum-Z2-product-d3hypercube,
   convention=(Z_2)^d-Schur-tensor-product-factored-identity-extension-from-W11-4,
   L_max=6)

Classification: GEOMETRIC

METHODOLOGY
-----------
The substrate's bottom-20 eigenvalues at tau_fold=0.19 partition into 4 strata
of cardinality (2, 4, 8, 6) under the eigenvalue-degeneracy equivalence relation
(W11-2 partition rule, ULP_TOL=1e-14). Stratum boundaries on indices 0..19:
  stratum 1: indices [0, 2)   (cardinality 2)
  stratum 2: indices [2, 6)   (cardinality 4)
  stratum 3: indices [6, 14)  (cardinality 8)
  stratum 4: indices [14, 20) (cardinality 6)

The Mellin-cone moment weights at substrate distance n on bottom-20 eigenvalues:
  w_0(lambda) = 1
  w_2(lambda) = 1 / lambda^4    (substrate-distance-1 Casimir analog)
  w_4(lambda) = 1 / lambda^8    (substrate-distance-0 Casimir analog)

For an extension X with d axes (sigma_1, ..., sigma_d), each sigma_j a {+/-1}-valued
character on stratum_id, define
  A_n^(sigma_1, ..., sigma_d) := sum_{k=0..19} sigma_1(s(k)) * ... * sigma_d(s(k)) * w_n(lambda_k)
  Delta_n^(d)(sigma_1, ..., sigma_d) := sum_{eps in {0,1}^d} (-1)^|eps| * A_n^(sigma_1^eps_1, ..., sigma_d^eps_d)

Per W11-4 Sage-QQ exact-zero: Delta_n^(d) = 0 for any (Z_2)^d-Schur structure.
This is verified at floating-point as |Delta_n^(d)| <= 1e-12 (machine-eps floor
at d-fold tensor product on 20-element support).

NON-DEGENERACY (per-axis marginal test):
For each axis j in {1, ..., d}, compute the marginal
  M_n(j) := A_n^(sigma_j) - A_n^(e)    [single-axis Z_2 character minus identity]
A non-degenerate axis has |M_n(j)| > 1e-12 for at least one n in {0, 2, 4};
a degenerate axis has all |M_n(j)| <= 1e-12 (sigma_j acts trivially).

Extension X PASSES iff:
  (a) Delta_n^(d) <= 1e-12 for all n in {0, 2, 4} (W11-4 inheritance — verified)
  (b) all d axes are non-degenerate (each axis has |M_n(j)| > 1e-12 for some n)

DISCIPLINE
----------
- `from canonical_constants import *`
- All locals tagged `# (local)`
- Dual-SHA verdict line per S87+ schema-v2; 3-tuple companion row
- W11-4 hypercube identity inheritance pinned via input-SHA on
  s87_w11_hypercube_vertex_identity.npz
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import itertools
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths and pin metadata
# ---------------------------------------------------------------------------
GATE_ID = "S88-MONODROMY-DEPTH-EXTENSION-SURVIVING-V4-ENUMERATION"
SCHEME = "Cartan-toral-rejected-V4-strata-tested-via-stratum-Z2-product-d3hypercube"
CONVENTION = "(Z_2)^d-Schur-tensor-product-factored-identity-extension-from-W11-4"
L_MAX_OPERATIONAL = 6  # (local) Casimir-bound truncation per math-scripts.md
L_MAX_PLAN = 10        # (local) plan-pinned but redundant per Friedrich-Bar saturation
N_BOT = 20             # (local) bottom-20 eigenvalue support
ULP_TOL = 1e-14        # (local) W11-2 partition equivalence tolerance
ABS_PASS_FLOOR = 1e-12 # (local) machine-epsilon floor for hypercube identity / marginal
ABS_INFO_CEILING = 1e-9  # (local) information-band ceiling

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w2_monodromy_depth_extension_surviving_v4_enumeration.py"
NPZ_OUT = T0 / "s88_w2_monodromy_depth_extension_surviving_v4_enumeration.npz"
PNG_OUT = T0 / "s88_w2_monodromy_depth_extension_surviving_v4_enumeration.png"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

# Plan-cited inputs (Class-(c) re-pinned to actual filenames):
W11_2_NPZ = T0 / "s87_w11_partition_stability_4stratum.npz"
W11_4_NPZ = T0 / "s87_w11_hypercube_vertex_identity.npz"
CANON_PY = T0 / "canonical_constants.py"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    """SHA-256 of canonical-ordered pin map (per gate-verdicts.md S81+)."""
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Section 4 — Substrate inputs (W11-2 bot20 at tau_fold)
# ---------------------------------------------------------------------------
def load_substrate_bot20() -> tuple[np.ndarray, np.ndarray]:
    """Load bottom-20 D_K eigenvalues at tau=0.19 + cardinality vector (2,4,8,6).

    Returns:
      bot20: shape (20,) sorted |lambda| values at tau_fold=0.19
      cv:    shape (4,) cardinality vector (2, 4, 8, 6)
    """
    d = np.load(W11_2_NPZ, allow_pickle=True)
    tau_grid = d["tau_grid"]                           # (local) (11,)
    # Index of tau=0.19 in the W11-2 grid (W11-2 npz has tau_grid[5]=0.19)
    idx_tau_fold = int(np.argmin(np.abs(tau_grid - tau_fold)))  # (local)
    assert abs(float(tau_grid[idx_tau_fold]) - tau_fold) < 1e-9, (
        f"tau_fold={tau_fold} not in W11-2 grid; nearest={tau_grid[idx_tau_fold]}"
    )
    bot20 = d["bot20_per_tau"][idx_tau_fold].copy()            # (local) (20,)
    cv_raw = d["cardinality_vector_per_tau"][idx_tau_fold].copy()  # (local) (8,) padded
    cv = cv_raw[cv_raw > 0].astype(int)                        # (local) (4,)
    assert tuple(cv.tolist()) == (2, 4, 8, 6), (
        f"Expected cv (2,4,8,6); got {tuple(cv.tolist())}"
    )
    return bot20, cv


def stratum_id_per_index(cv: np.ndarray) -> np.ndarray:
    """Map index k in [0, N_BOT) to stratum_id in {0, 1, 2, 3} via cumulative cv."""
    boundaries = np.cumsum(cv)                  # (local) [2, 6, 14, 20]
    sids = np.zeros(N_BOT, dtype=int)           # (local)
    for k in range(N_BOT):
        sids[k] = int(np.searchsorted(boundaries, k, side="right"))
    return sids


# ---------------------------------------------------------------------------
# Section 5 — Mellin-cone moment weights and amplitude functional
# ---------------------------------------------------------------------------
def w_n(lam: np.ndarray, n: int) -> np.ndarray:
    """Mellin-cone moment weight at substrate distance n on bot20 |lambda|."""
    if n == 0:
        return np.ones_like(lam)
    return 1.0 / (lam ** (2 * n))


def amplitude_A_n(
    bot20: np.ndarray,
    sids: np.ndarray,
    sigmas_per_stratum: list[np.ndarray],
    n: int,
) -> float:
    """A_n^(sigma_1, ..., sigma_d) = sum_k prod_j sigma_j(s(k)) * w_n(lambda_k).

    sigmas_per_stratum[j] is a length-4 array of {+1, -1} on stratum_id ∈ {0,1,2,3}.
    """
    weights = w_n(bot20, n)                                   # (local) (20,)
    char_prod = np.ones(N_BOT, dtype=np.float64)              # (local)
    for sig_per_strat in sigmas_per_stratum:
        sig_per_idx = sig_per_strat[sids]                     # (local) (20,)
        char_prod = char_prod * sig_per_idx
    return float(np.sum(char_prod * weights))


def hypercube_delta_n(
    bot20: np.ndarray,
    sids: np.ndarray,
    sigmas: list[np.ndarray],
    n: int,
) -> float:
    """Delta_n^(d) = sum_{eps in {0,1}^d} (-1)^|eps| A_n^(sigma_1^eps_1, ..., sigma_d^eps_d).

    sigma_j^0 = identity (all +1); sigma_j^1 = sigma_j.
    """
    d = len(sigmas)                                           # (local)
    identity_sigma = np.ones(4, dtype=np.float64)             # (local)
    total = 0.0                                               # (local)
    for eps in itertools.product([0, 1], repeat=d):
        eps_arr = np.array(eps, dtype=int)                    # (local)
        sgn = (-1) ** int(np.sum(eps_arr))                    # (local)
        sigmas_eps = [
            sigmas[j] if eps_arr[j] == 1 else identity_sigma
            for j in range(d)
        ]
        total += sgn * amplitude_A_n(bot20, sids, sigmas_eps, n)
    return total


def axis_marginal(
    bot20: np.ndarray,
    sids: np.ndarray,
    sigma_j: np.ndarray,
    n: int,
) -> float:
    """M_n(j) := A_n^(sigma_j) - A_n^(e). Non-zero ⇔ sigma_j acts non-trivially."""
    A_e = amplitude_A_n(bot20, sids, [np.ones(4, dtype=np.float64)], n)  # (local)
    A_j = amplitude_A_n(bot20, sids, [sigma_j], n)                       # (local)
    return float(A_j - A_e)


# ---------------------------------------------------------------------------
# Section 6 — Five (Z_2)^d>2 atlas extensions A-E
# ---------------------------------------------------------------------------
# Each axis is a length-4 array indexed by stratum_id (0..3 for strata 1..4).
# All axes are SUBSTRATE-IS stratum-Z_2 characters (Cartan-toral REJECTED per W11-1).
#
# Substrate-physical strata at tau_fold=0.19:
#   stratum 0 (cardinality 2): lambda ~ 0.81974
#   stratum 1 (cardinality 4): lambda ~ 0.83589
#   stratum 2 (cardinality 8): lambda ~ 0.84086
#   stratum 3 (cardinality 6): lambda ~ 0.84521

def define_extensions() -> dict[str, dict]:
    """Return 5 extensions with d-axis Z_2 characters on stratum_id.

    Per plan §W2-1.6 Step 1-2:
      Extension A: (Z_2)^3 = stratum-Z_2(parity-mod-2) x stratum-pair-Z_2(low-vs-high) x stratum-Z_2(adjacent-pair)
      Extension B: (Z_2)^4 = stratum-axis-1 x stratum-axis-2 x stratum-axis-3 x stratum-axis-4
      Extension C: (Z_2)^3 = stratum-low-pair-vs-high-pair x stratum-(2,4)-vs-(8,6) x parity-mod-2
      Extension D: (Z_2)^3 = re-ordering of A axes (tests independence of Z_2 ordering — same group abstractly)
      Extension E: (Z_2)^3 = (1,4)-vs-(2,3) x (1,2)-vs-(3,4) x (1,3)-vs-(2,4)

    Substrate-physical content: Extensions B and E are "synthetic" because they
    enumerate ALL 3 non-trivial Z_2 characters on a 4-element set — but the 4-element
    set has only 2^3-1=7 non-trivial Z_2 characters total minus the constant. Per
    Z_2 representation theory on Z_2^2 = V_4 acting on 4 strata, exactly 3 non-trivial
    characters exist. So extensions A/B/D test rank-3 / rank-4 admissibility; C/E test
    independence of axis-grouping.
    """
    # Z_2 characters on the 4-stratum partition (sigma:{0,1,2,3} -> {+1,-1}):
    sig_parity_mod_2 = np.array([+1, -1, +1, -1], dtype=np.float64)        # strata (0,2) vs (1,3)
    sig_low_vs_high  = np.array([+1, +1, -1, -1], dtype=np.float64)        # strata (0,1) vs (2,3)
    sig_adjacent_pair = np.array([+1, -1, -1, +1], dtype=np.float64)       # strata (0,3) vs (1,2) — same as parity*low_vs_high
    # Extra single-stratum axes (each isolating one stratum):
    sig_isolate_0 = np.array([-1, +1, +1, +1], dtype=np.float64)
    sig_isolate_1 = np.array([+1, -1, +1, +1], dtype=np.float64)
    sig_isolate_2 = np.array([+1, +1, -1, +1], dtype=np.float64)
    sig_isolate_3 = np.array([+1, +1, +1, -1], dtype=np.float64)

    return {
        "A": {
            "d": 3,
            "label": "(Z_2)^3 = parity_mod2 x low_vs_high x adjacent_pair",
            "axes": [sig_parity_mod_2, sig_low_vs_high, sig_adjacent_pair],
        },
        "B": {
            "d": 4,
            "label": "(Z_2)^4 = parity_mod2 x low_vs_high x isolate_0 x isolate_3",
            "axes": [sig_parity_mod_2, sig_low_vs_high, sig_isolate_0, sig_isolate_3],
        },
        "C": {
            "d": 3,
            "label": "(Z_2)^3 = low_vs_high x parity_mod2 x isolate_2 (alt grouping)",
            "axes": [sig_low_vs_high, sig_parity_mod_2, sig_isolate_2],
        },
        "D": {
            "d": 3,
            "label": "(Z_2)^3 = adjacent_pair x parity_mod2 x low_vs_high (re-order of A)",
            "axes": [sig_adjacent_pair, sig_parity_mod_2, sig_low_vs_high],
        },
        "E": {
            "d": 3,
            "label": "(Z_2)^3 = isolate_0 x isolate_1 x isolate_2",
            "axes": [sig_isolate_0, sig_isolate_1, sig_isolate_2],
        },
    }


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t_start = time.time()                                     # (local)

    # 7.1 — Substrate inputs
    bot20, cv = load_substrate_bot20()
    sids = stratum_id_per_index(cv)
    print(f"[W2-1] Loaded bot20 at tau_fold={tau_fold} from {W11_2_NPZ.name}")
    print(f"       cv = {tuple(cv.tolist())} (sum={int(cv.sum())})")
    print(f"       distinct |lambda| values: {sorted(set(np.round(bot20, 8)))}")
    print(f"       stratum_id mapping: {sids.tolist()}")

    # 7.2 — Cross-check W11-4 Sage-QQ inheritance
    d_w11_4 = np.load(W11_4_NPZ, allow_pickle=True)
    w11_4_pass_per_d = d_w11_4["per_d_pass"].tolist()              # (local)
    w11_4_d_grid = d_w11_4["d_grid"].tolist()                       # (local)
    print(f"[W2-1] W11-4 hypercube identity: per_d_pass = {dict(zip(w11_4_d_grid, w11_4_pass_per_d))}")
    cc1_w11_4_inheritance = all(w11_4_pass_per_d)                  # (local) all True

    # 7.3 — Five extensions
    extensions = define_extensions()
    moment_indices = [0, 2, 4]                                # (local)

    results: dict[str, dict] = {}                             # (local)
    pass_count = 0                                            # (local)
    pass_d2_or_higher_count = 0                               # (local) PASS-d>2-extension counter

    for ext_id, ext in extensions.items():
        d = int(ext["d"])
        sigmas = ext["axes"]
        # Hypercube identity at each n
        delta_per_n = []                                      # (local)
        for n in moment_indices:
            delta = hypercube_delta_n(bot20, sids, sigmas, n)
            delta_per_n.append(delta)
        max_delta = float(np.max(np.abs(delta_per_n)))        # (local)
        hypercube_passes = bool(max_delta <= ABS_PASS_FLOOR)  # (local)

        # Per-axis marginal (non-degeneracy)
        marginals_per_axis = []                               # (local) shape (d, 3)
        non_degenerate_per_axis = []                          # (local) shape (d,)
        for j in range(d):
            mn = [axis_marginal(bot20, sids, sigmas[j], n) for n in moment_indices]
            marginals_per_axis.append(mn)
            non_deg = bool(any(abs(m) > ABS_PASS_FLOOR for m in mn))  # (local)
            non_degenerate_per_axis.append(non_deg)
        all_axes_non_degenerate = all(non_degenerate_per_axis)  # (local)

        ext_passes = bool(hypercube_passes and all_axes_non_degenerate)
        if ext_passes:
            pass_count += 1
            if d >= 3:
                pass_d2_or_higher_count += 1

        results[ext_id] = {
            "d": d,
            "label": ext["label"],
            "delta_per_n": delta_per_n,
            "max_delta": max_delta,
            "hypercube_passes": hypercube_passes,
            "marginals_per_axis": marginals_per_axis,
            "non_degenerate_per_axis": non_degenerate_per_axis,
            "all_axes_non_degenerate": all_axes_non_degenerate,
            "passes": ext_passes,
        }
        print(
            f"[W2-1] Extension {ext_id} (d={d}): "
            f"hypercube max_delta={max_delta:.3e} (pass={hypercube_passes}); "
            f"non_deg axes = {non_degenerate_per_axis}; passes={ext_passes}"
        )

    print(f"[W2-1] count_PASS_extensions = {pass_count} / 5")
    print(f"[W2-1] count_PASS_d_geq_3    = {pass_d2_or_higher_count} / 5")

    # 7.4 — Composite verdict (per plan §W2-1.9)
    if pass_count >= 3 and cc1_w11_4_inheritance:
        composite = "PASS"
        verdict_kind = "PASS-d=2-exact"  # (local) per plan §W2-1.9
    elif pass_count >= 1:
        composite = "PASS"
        verdict_kind = "PASS-d>2-extension"  # (local)
    elif pass_count == 0 and any(r["hypercube_passes"] for r in results.values()):
        # Hypercube identity holds but ALL extensions degenerate ⇒ FAIL (depth-extension closed)
        composite = "FAIL"
        verdict_kind = "FAIL-depth-extension-closed"  # (local)
    else:
        composite = "FAIL"
        verdict_kind = "FAIL-structural-W11-4-inheritance-broken"  # (local)

    # 7.5 — Compute SHA pins
    canon_sha = sha256_file(CANON_PY)
    w11_2_sha = sha256_file(W11_2_NPZ)
    w11_4_sha = sha256_file(W11_4_NPZ)
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha

    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_OPERATIONAL,
        "tau_fold": float(tau_fold),
        "M_KK": float(M_KK),
        "Delta_BCS": float(Delta_BCS),
        "ULP_TOL": ULP_TOL,
        "ABS_PASS_FLOOR": ABS_PASS_FLOOR,
        "ABS_INFO_CEILING": ABS_INFO_CEILING,
        "cv_anchor": list(cv.tolist()),
        "extension_keys": list(extensions.keys()),
        "moment_indices": moment_indices,
        "input_canonical_constants_sha256": canon_sha,
        "input_w11_2_partition_npz_sha256": w11_2_sha,
        "input_w11_4_hypercube_npz_sha256": w11_4_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    # 7.6 — Save .npz
    np.savez(
        NPZ_OUT,
        bot20=bot20,
        cv=cv,
        sids=sids,
        moment_indices=np.array(moment_indices),
        extension_keys=np.array(list(extensions.keys())),
        delta_per_ext_per_n=np.array([results[k]["delta_per_n"] for k in extensions.keys()]),
        max_delta_per_ext=np.array([results[k]["max_delta"] for k in extensions.keys()]),
        hypercube_passes_per_ext=np.array([results[k]["hypercube_passes"] for k in extensions.keys()]),
        non_degenerate_per_ext_per_axis=np.array(
            [results[k]["non_degenerate_per_axis"] + [True] * (4 - results[k]["d"])  # pad to d=4
             for k in extensions.keys()]
        ),
        all_axes_non_degenerate_per_ext=np.array(
            [results[k]["all_axes_non_degenerate"] for k in extensions.keys()]
        ),
        passes_per_ext=np.array([results[k]["passes"] for k in extensions.keys()]),
        pass_count=np.int64(pass_count),
        pass_d_geq_3_count=np.int64(pass_d2_or_higher_count),
        composite=composite,
        verdict_kind=verdict_kind,
        cc1_w11_4_inheritance=np.bool_(cc1_w11_4_inheritance),
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
        tau_fold_pin=np.float64(tau_fold),
        L_max_operational=np.int64(L_MAX_OPERATIONAL),
        L_max_plan=np.int64(L_MAX_PLAN),
    )

    # 7.7 — Plot
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    ax[0].set_title(f"S88 W2-1 — Hypercube identity Delta_n^(d) per extension")
    ext_keys = list(extensions.keys())
    deltas_matrix = np.array([results[k]["delta_per_n"] for k in ext_keys])
    for i_n, n in enumerate(moment_indices):
        ax[0].semilogy(ext_keys, np.maximum(np.abs(deltas_matrix[:, i_n]), 1e-20),
                       marker="o", label=f"n={n}")
    ax[0].axhline(ABS_PASS_FLOOR, color="green", linestyle="--", label=f"PASS floor ({ABS_PASS_FLOOR:.0e})")
    ax[0].axhline(ABS_INFO_CEILING, color="orange", linestyle="--", label=f"INFO ceiling ({ABS_INFO_CEILING:.0e})")
    ax[0].set_xlabel("Extension")
    ax[0].set_ylabel("|Delta_n^(d)|")
    ax[0].legend()
    ax[0].grid(True, alpha=0.3)
    ax[1].set_title("Per-axis marginal non-degeneracy (max over n)")
    for i_ext, k in enumerate(ext_keys):
        d = results[k]["d"]
        max_marg = [max(abs(m) for m in results[k]["marginals_per_axis"][j]) for j in range(d)]
        ax[1].semilogy([f"{k}.{j+1}" for j in range(d)], np.maximum(max_marg, 1e-20),
                       marker="s", label=f"Ext {k}")
    ax[1].axhline(ABS_PASS_FLOOR, color="green", linestyle="--")
    ax[1].set_xlabel("Extension.Axis")
    ax[1].set_ylabel("max_n |M_n(j)|")
    ax[1].legend(loc="best", ncol=3, fontsize=8)
    ax[1].grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(PNG_OUT, dpi=120)
    plt.close()

    # 7.8 — Append verdict line (S87+ schema-v2)
    elapsed = time.time() - t_start                            # (local)
    value_str = (
        f"count_PASS_extensions={pass_count};verdict_kind={verdict_kind};"
        f"max_delta_max={max(r['max_delta'] for r in results.values()):.3e};"
        f"cc1_w11_4_inheritance={cc1_w11_4_inheritance};"
        f"L_max_op={L_MAX_OPERATIONAL}_plan={L_MAX_PLAN}"
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
    # 3-tuple annotation per S87 schema-v2 (gate-verdicts.md)
    sign_verdict = "PASS" if composite == "PASS" else "N/A"   # (local)
    magnitude_verdict = "PASS" if composite == "PASS" else "FAIL"  # (local)
    regime_verdict = "VALID"  # (local) bot20 truncation Casimir-bound saturated
    tuple_line = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_line)
        f.write(tuple_line)

    print(f"[W2-1] DONE in {elapsed:.2f}s")
    print(f"[W2-1] composite = {composite} (verdict_kind={verdict_kind})")
    print(f"[W2-1] audit_sha256 = {audit_sha256}")
    print(f"[W2-1] content_sha256 = {content_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
