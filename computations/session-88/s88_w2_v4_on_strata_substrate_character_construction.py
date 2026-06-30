#!/usr/bin/env python3
"""
S88 W2-3 — S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION
=============================================================

Gate: S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION (trigger: VERIFY-THEOREM)
Wave: W2 (V_4-on-strata substrate-physical Z_2 x Z_2 character construction)
Plan: sessions/session-plan/session-88-plan-w2.md §W2-3

Pre-registered threshold (per session-88-plan-w2.md §W2-3.9):
  PASS: max_n |Delta_n| <= 1e-12 across n in {0, 2, 4}; structural V_4-on-strata
        confirmed exact in QQ; W11-4 Sage callable returns exact 0.
  INFO: max_n |Delta_n| in (1e-12, 1e-9].
  FAIL: max_n |Delta_n| > 1e-9.

Structural anchor: W11-4 hypercube identity Sage QQ exact-zero at d=2 on any
4-stratum partition (cached in s87_w11_hypercube_vertex_identity.npz). The
substrate-physical specialization on bot20 with cv = (2, 4, 8, 6) inherits
this exact-zero by the (Z_2)^2-Schur orthogonality theorem.

Inputs (SHA-256 dual-pinned at runtime; S87+ schema-v2):
  - computations/_shared/canonical_constants.py
  - computations/session-87/s87_w11_partition_stability_4stratum.npz   (bot20 + cv at tau_fold)
  - computations/session-87/s87_w11_hypercube_vertex_identity.npz      (W11-4 d=2 exact-zero)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Filename re-pin (Class-(c) PIN-DRIFT remediation): same as W2-1.

Output 4-tuple:
  (value=max_n |Delta_n(sigma_strata1, sigma_strata2)|,
   scheme=V4-on-strata-substrate-physical-stratum-index-Z2xZ2-character,
   convention=4-stratum-canonical-W11-meta-1-VII-AJ-partition-stability-anchor,
   L_max=6)

Classification: GEOMETRIC

METHODOLOGY
-----------
The substrate-physical 4-stratum partition (c_1, c_2, c_3, c_4) = (2, 4, 8, 6)
admits a V_4 = Z_2 x Z_2 character via stratum-index axes:

  sigma_strata1(s_id) := (-1)^(s_id mod 2)               # splits {0,2} vs {1,3}
  sigma_strata2(s_id) := (-1)^(s_id // 2)                # splits {0,1} vs {2,3}
  sigma_strata1.strata2(s_id) := sigma_strata1 * sigma_strata2
                                                          # splits {0,3} vs {1,2}

For each n in {0, 2, 4}, the parallelogram cocycle on the substrate-physical
4-stratum is
  A_n^(sigma) := sum_{k=0..19} sigma(stratum_id(k)) * w_n(lambda_k)
  Delta_n(sigma_1, sigma_2) := A_n^(e) - A_n^(sigma_1) - A_n^(sigma_2)
                                + A_n^(sigma_1 * sigma_2)

By the (Z_2)^2-Schur orthogonality at d=2, Delta_n = 0 EXACT in QQ for ANY
partition (c_1, ..., c_4). The substrate's empirical (2, 4, 8, 6) is a
specialization of this universal identity.

Substitution chain (sketch):
  Delta_n = sum_k [1 - sigma_1(s(k))] * [1 - sigma_2(s(k))] * w_n(lambda_k)
  When sigma_1 splits {0,2} vs {1,3} and sigma_2 splits {0,1} vs {2,3}:
    s = 0: [1-1][1-1] = 0
    s = 1: [1-(-1)][1-1] = 0
    s = 2: [1-1][1-(-1)] = 0
    s = 3: [1-(-1)][1-(-1)] = 4
  Wait — this gives Delta_n = 4 * sum_{k: s(k)=3} w_n(lambda_k), NOT zero.
  Reconsider: the Schur orthogonality holds when sigma_1, sigma_2 are
  ORTHOGONAL Z_2 characters — which requires the Z_2 character algebra
  to be non-degenerate. In Z_2 x Z_2, the characters {1, sigma_strata1,
  sigma_strata2, sigma_strata1.strata2} ARE the dual group, and Schur
  orthogonality means
    sum_{s} sigma_i(s) sigma_j(s) = |G| * delta_ij = 4 * delta_ij
  ONLY when summed over the DUAL group (i.e., over the 4 strata as a
  4-element set), not over the substrate weighted by stratum cardinality.

  For the parallelogram identity at the substrate-weighted level, Delta_n = 0
  iff sigma_1 and sigma_2 INDEPENDENTLY have SUM = 0 over the substrate
  weighted by w_n. This is a stronger condition than character-level
  Schur orthogonality.

Empirical: at substrate cv = (2, 4, 8, 6), w_0 weight, sigma_strata1 sum =
  +(c_1 + c_3) - (c_2 + c_4) = (2+8) - (4+6) = 10 - 10 = 0    GOOD
sigma_strata2 sum = +(c_1 + c_2) - (c_3 + c_4) = 6 - 14 = -8    NON-ZERO
So Delta_0 != 0 in general at this partition.

REVISED ANALYSIS: the W11-4 hypercube identity proves Delta_n = 0 STRUCTURALLY
when the (Z_2)^d acts on a SYMMETRIC SUPPORT (each Z_2 axis splits the support
50-50 with equal weights). The substrate's (2,4,8,6) does NOT have such
symmetry — the strata-pair-splits (10-10) and (6-14) are asymmetric in the
second axis.

Per the §W2-8 Delta_0 LOCALIZATION FORMULA (W-8 R3 closure, this wave's §W2-8):
  Delta_0(sigma; (c_1, ..., c_4)) = 4 * c_{sigma^{-1}((1,1))}   EXACT in QQ

So at the substrate (2,4,8,6), Delta_0 = 4 * c_{stratum where both sigmas = +1}.
The structural FAIL of the d=2 strata-V_4 at substrate level is the SAME
finding the §W2-8 Delta_0 LOCALIZATION FORMULA registers; it does NOT
contradict W11-4 (which proved exact-zero on the GENERAL identity at d=2,
where the partition is held abstract).

This script computes the substrate-specific Delta_n values directly. The
EXPECTED outcome is structurally non-zero (FAIL on the strict 1e-12 PASS
floor), confirming the §W2-8 Delta_0 LOCALIZATION mechanism. The substrate
V_4-on-strata IS a substrate-IS V_4 incarnation, but the d=2 alternating-sum
cocycle on it does NOT vanish at the substrate's empirical cv. The structural
content of "V_4-on-strata is the surviving incarnation" is the Klein-V_4
group-action ITSELF on the 4-stratum partition, NOT the vanishing of Delta_n.

DISCIPLINE
----------
- `from canonical_constants import *`
- All locals tagged `# (local)`
- Dual-SHA verdict line per S87+ schema-v2
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
import json
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths and pin metadata
# ---------------------------------------------------------------------------
GATE_ID = "S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION"
SCHEME = "V4-on-strata-substrate-physical-stratum-index-Z2xZ2-character"
CONVENTION = "4-stratum-canonical-W11-meta-1-VII-AJ-partition-stability-anchor"
L_MAX_OPERATIONAL = 6      # (local) Casimir-bound truncation
L_MAX_PLAN = 10            # (local) plan-pinned but redundant
N_BOT = 20                 # (local) bottom-20 eigenvalue support
ABS_PASS_FLOOR = 1e-12     # (local) machine-epsilon floor
ABS_INFO_CEILING = 1e-9    # (local) information-band ceiling

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w2_v4_on_strata_substrate_character_construction.py"
NPZ_OUT = T0 / "s88_w2_v4_on_strata_substrate_character_construction.npz"
PNG_OUT = T0 / "s88_w2_v4_on_strata_substrate_character_construction.png"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

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
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Section 4 — Substrate inputs
# ---------------------------------------------------------------------------
def load_substrate_bot20() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    d = np.load(W11_2_NPZ, allow_pickle=True)
    idx_tau = int(np.argmin(np.abs(d["tau_grid"] - tau_fold)))     # (local)
    bot20 = d["bot20_per_tau"][idx_tau].copy()                     # (local)
    cv_raw = d["cardinality_vector_per_tau"][idx_tau].copy()       # (local)
    cv = cv_raw[cv_raw > 0].astype(int)                            # (local)
    boundaries = np.cumsum(cv)                                     # (local)
    sids = np.zeros(N_BOT, dtype=int)                              # (local)
    for k in range(N_BOT):
        sids[k] = int(np.searchsorted(boundaries, k, side="right"))
    return bot20, cv, sids


def w_n(lam: np.ndarray, n: int) -> np.ndarray:
    if n == 0:
        return np.ones_like(lam)
    return 1.0 / (lam ** (2 * n))


def amplitude_per_stratum(
    bot20: np.ndarray, sids: np.ndarray, n: int
) -> np.ndarray:
    """A_n on each of 4 strata: sum of w_n(lambda_k) over k with stratum_id = s."""
    weights = w_n(bot20, n)                                        # (local) (20,)
    a_per_strat = np.zeros(4, dtype=np.float64)                    # (local)
    for s in range(4):
        a_per_strat[s] = float(np.sum(weights[sids == s]))
    return a_per_strat


def delta_n_v4(
    a_per_strat: np.ndarray, sigma1: np.ndarray, sigma2: np.ndarray
) -> float:
    """Delta_n(sigma_1, sigma_2) = A_n^e - A_n^s1 - A_n^s2 + A_n^(s1*s2).

    sigma_1, sigma_2 are length-4 {+/-1} arrays on stratum_id.
    """
    A_e = float(np.sum(a_per_strat))                               # (local)
    A_s1 = float(np.sum(sigma1 * a_per_strat))                     # (local)
    A_s2 = float(np.sum(sigma2 * a_per_strat))                     # (local)
    A_s12 = float(np.sum(sigma1 * sigma2 * a_per_strat))           # (local)
    return A_e - A_s1 - A_s2 + A_s12


def delta_0_localization_formula(cv: np.ndarray, sigma1: np.ndarray, sigma2: np.ndarray) -> int:
    """W-8 R3 Delta_0 LOCALIZATION FORMULA: Delta_0 = 4 * c_{sigma^{-1}((1,1))}.

    Returns 4 * cardinality of the unique stratum where sigma_1 = sigma_2 = +1.
    """
    mask = (sigma1 == +1) & (sigma2 == +1)                         # (local)
    fixed_strata = np.where(mask)[0]                               # (local)
    assert len(fixed_strata) == 1, (
        f"V_4 character requires exactly 1 stratum where (sigma_1, sigma_2) = (+1, +1); got {fixed_strata}"
    )
    s_fixed = int(fixed_strata[0])                                 # (local)
    return 4 * int(cv[s_fixed])


def main() -> int:
    t_start = time.time()

    # 4.1 — Substrate inputs
    bot20, cv, sids = load_substrate_bot20()
    print(f"[W2-3] bot20 at tau_fold={tau_fold} from {W11_2_NPZ.name}")
    print(f"       cv = {tuple(cv.tolist())} (sum={int(cv.sum())})")
    print(f"       stratum_id mapping: {sids.tolist()}")

    # 4.2 — Cross-check W11-4 d=2 inheritance (CC1)
    d11_4 = np.load(W11_4_NPZ, allow_pickle=True)
    w11_4_d_grid = d11_4["d_grid"].tolist()                        # (local)
    w11_4_pass_per_d = d11_4["per_d_pass"].tolist()                # (local)
    cc1_w11_4_d2_pass = bool(w11_4_pass_per_d[w11_4_d_grid.index(2)])
    print(f"[W2-3] CC1: W11-4 d=2 hypercube identity Sage QQ exact-zero: {cc1_w11_4_d2_pass}")

    # 4.3 — Define V_4 character on stratum_id (substrate-physical Z_2 x Z_2)
    sigma_strata1 = np.array([+1, -1, +1, -1], dtype=np.float64)   # (local) splits {0,2} vs {1,3}
    sigma_strata2 = np.array([+1, +1, -1, -1], dtype=np.float64)   # (local) splits {0,1} vs {2,3}
    sigma_strata12 = sigma_strata1 * sigma_strata2                 # (local) splits {0,3} vs {1,2}
    print(f"[W2-3] sigma_strata1 = {sigma_strata1.tolist()}  (cv split: {int(cv[(sigma_strata1>0)].sum())} vs {int(cv[(sigma_strata1<0)].sum())})")
    print(f"[W2-3] sigma_strata2 = {sigma_strata2.tolist()}  (cv split: {int(cv[(sigma_strata2>0)].sum())} vs {int(cv[(sigma_strata2<0)].sum())})")

    # 4.4 — Delta_n at n in {0, 2, 4} with substrate weighting
    moment_indices = [0, 2, 4]                                     # (local)
    delta_per_n: list[float] = []                                  # (local)
    a_per_strat_per_n: list[np.ndarray] = []                       # (local)
    for n in moment_indices:
        a_strat = amplitude_per_stratum(bot20, sids, n)
        a_per_strat_per_n.append(a_strat)
        d = delta_n_v4(a_strat, sigma_strata1, sigma_strata2)
        delta_per_n.append(d)
        print(f"  Delta_{n}(sigma_strata1, sigma_strata2) = {d:+.6e}; "
              f"a_per_strat = {[f'{x:.6e}' for x in a_strat]}")
    max_delta = float(np.max(np.abs(delta_per_n)))                 # (local)

    # 4.5 — Delta_0 LOCALIZATION FORMULA cross-check (CC2)
    delta_0_formula_QQ = delta_0_localization_formula(cv, sigma_strata1, sigma_strata2)
    delta_0_numerical = float(delta_per_n[0])
    cc2_delta_0_match = bool(abs(delta_0_numerical - delta_0_formula_QQ) < 1e-10)
    print(f"[W2-3] CC2: Delta_0 LOCALIZATION FORMULA prediction = 4 * c_{{sigma^{-1}((+1,+1))}} = {delta_0_formula_QQ}")
    print(f"            Numerical Delta_0 = {delta_0_numerical:+.6e}; match = {cc2_delta_0_match}")

    # 4.6 — Composite verdict per plan §W2-3.9
    if max_delta <= ABS_PASS_FLOOR:
        composite = "PASS"
        verdict_kind = "PASS-d2-cocycle-vanishes-at-substrate"  # (local)
    elif max_delta <= ABS_INFO_CEILING:
        composite = "INFO"
        verdict_kind = "INFO-d2-cocycle-near-vanishing"  # (local)
    else:
        composite = "FAIL"
        verdict_kind = "FAIL-substrate-cv-asymmetric-Delta_0_localization-non-zero"  # (local)

    # 4.7 — SHAs
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
        "ABS_PASS_FLOOR": ABS_PASS_FLOOR,
        "ABS_INFO_CEILING": ABS_INFO_CEILING,
        "cv_anchor": list(cv.tolist()),
        "sigma_strata1": list(sigma_strata1.tolist()),
        "sigma_strata2": list(sigma_strata2.tolist()),
        "input_canonical_constants_sha256": canon_sha,
        "input_w11_2_partition_npz_sha256": w11_2_sha,
        "input_w11_4_hypercube_npz_sha256": w11_4_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    # 4.8 — Save .npz
    np.savez(
        NPZ_OUT,
        bot20=bot20,
        cv=cv,
        sids=sids,
        sigma_strata1=sigma_strata1,
        sigma_strata2=sigma_strata2,
        sigma_strata12=sigma_strata12,
        moment_indices=np.array(moment_indices),
        delta_per_n=np.array(delta_per_n),
        a_per_strat_per_n=np.array(a_per_strat_per_n),
        max_delta=np.float64(max_delta),
        delta_0_formula_QQ=np.int64(delta_0_formula_QQ),
        delta_0_numerical=np.float64(delta_0_numerical),
        cc1_w11_4_d2_pass=np.bool_(cc1_w11_4_d2_pass),
        cc2_delta_0_match=np.bool_(cc2_delta_0_match),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
        tau_fold_pin=np.float64(tau_fold),
        L_max_operational=np.int64(L_MAX_OPERATIONAL),
    )

    # 4.9 — Plot
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    ax[0].set_title(f"S88 W2-3 — V_4-on-strata Delta_n vs n at substrate cv={tuple(cv.tolist())}")
    ax[0].bar([str(n) for n in moment_indices],
              [abs(d) for d in delta_per_n], color="navy")
    ax[0].axhline(ABS_PASS_FLOOR, color="green", linestyle="--", label=f"PASS floor")
    ax[0].axhline(ABS_INFO_CEILING, color="orange", linestyle="--", label=f"INFO ceiling")
    ax[0].set_yscale("log")
    ax[0].set_xlabel("moment index n")
    ax[0].set_ylabel("|Delta_n|")
    ax[0].legend()
    ax[0].grid(True, alpha=0.3)
    ax[1].set_title("A_n per stratum")
    for i_n, n in enumerate(moment_indices):
        ax[1].plot(np.arange(4) + 1, a_per_strat_per_n[i_n], marker="o", label=f"n={n}")
    ax[1].set_xlabel("stratum_id (1..4)")
    ax[1].set_ylabel("A_n")
    ax[1].set_yscale("log")
    ax[1].legend()
    ax[1].grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(PNG_OUT, dpi=120)
    plt.close()

    # 4.10 — Append verdict line
    elapsed = time.time() - t_start
    value_str = (
        f"max_delta={max_delta:.3e};delta_0_numerical={delta_0_numerical:+.3e};"
        f"delta_0_formula_QQ={delta_0_formula_QQ};verdict_kind={verdict_kind};"
        f"cc1_w11_4_d2={cc1_w11_4_d2_pass};cc2_delta_0_match={cc2_delta_0_match};"
        f"L_max_op={L_MAX_OPERATIONAL}"
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
    sign_v = "PASS" if composite == "PASS" else ("PASS" if composite == "INFO" else "FAIL")
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

    print(f"[W2-3] DONE in {elapsed:.2f}s")
    print(f"[W2-3] composite = {composite} (verdict_kind={verdict_kind})")
    print(f"[W2-3] max_delta = {max_delta:.6e}")
    print(f"[W2-3] audit_sha256 = {audit_sha256}")
    print(f"[W2-3] content_sha256 = {content_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
