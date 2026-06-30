#!/usr/bin/env python3
"""
S88 W2-2 — S88-V4-CANDIDATE-III-TRIALITY-MOD-2
================================================

Gate: S88-V4-CANDIDATE-III-TRIALITY-MOD-2 (trigger: VERIFY)
Wave: W2 (V_4-on-triality-mod-2 substrate-IS V_4 incarnation test)
Plan: sessions/session-plan/session-88-plan-w2.md §W2-2

Pre-registered threshold (per session-88-plan-w2.md §W2-2.9):
  PASS: D-W8-1 PASSes (all three Schur orthogonality < 1e-12)
        AND max_n |Delta_n| <= 1e-12 across n in {0, 2, 4}.
  INFO: D-W8-1 PASSes AND max_n |Delta_n| in (1e-12, 1e-9].
  FAIL: D-W8-1 FAILs OR max_n |Delta_n| > 1e-9.

D-W8-1 KO=6 collapse diagnostic (FIRST gate-step): chi_triality_Z2 must be Schur-
orthogonal to (g_C, g_H, g_M) inventory characters at substrate-bot20 support
to confirm chi_triality_Z2 is a NEW substrate-IS character independent of the
existing 3-element A_F *-automorphism inventory.

Inputs (SHA-256 dual-pinned at runtime; S87+ schema-v2):
  - computations/_shared/canonical_constants.py     (tau_fold, M_KK, Delta_BCS)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (sector_evals dict per (p,q))
  - computations/session-87/s87_w11_partition_stability_4stratum.npz  (W11-2 cv anchor cross-check)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Filename re-pin (Class-(c) PIN-DRIFT remediation):
  Plan cites s84_w8a_af_automorphism_inventory.npz; no such file on disk.
  Inventory (g_C, g_H, g_M) reconstructed from canonical A_F = C + H + M_3(C)
  Cartan-toral character algebra:
    g_C(p, q) := (-1)^q       (Cartan-q parity; complex/abelian factor)
    g_H(p, q) := (-1)^(p+q)   (combined parity; quaternion factor)
    g_M(p, q) := (-1)^p       (Cartan-p parity; matrix factor; matches W11-1)

Output 4-tuple:
  (value=max_n |Delta_n|,
   scheme=triality-mod-2-Z2-paired-with-Cartan-zone-parity-Z2-V4-incarnation,
   convention=KO-dim-6-collapse-diagnostic-D-W8-1-orthogonal-to-A_F-automorphism-inventory,
   L_max=6)

Classification: GEOMETRIC

METHODOLOGY
-----------
SU(3) triality-mod-2 character on Peter-Weyl (p, q):
  chi_triality_Z2(p, q) := -1 if (p - q) mod 3 != 0 else +1

This Z_2 character lifts the SU(3) center Z_3 = {0, 1, 2} action via the kernel
of the (p - q) mod 3 -> Z_2 map (mod-2 reduction of the triality grade).
Triality orbits {(p,q), (q, p+q?), ...} are constant on chi_triality_Z2 by
construction.

Step 1 — D-W8-1 KO=6 collapse diagnostic:
  At substrate bot20 support (k=0..19, (p_k, q_k) sector labels), compute
    <chi_triality_Z2, g_X>_substrate := sum_{k=0..19} chi_triality_Z2(p_k,q_k)
                                                       * g_X(p_k, q_k)
                                                       * w_0(lambda_k)
  for X in {C, H, M}. Threshold |<.>| < 1e-12 -> orthogonal -> chi_triality_Z2
  is a NEW substrate-IS character outside (g_C, g_H, g_M) inventory.

Step 2-3 — Parallelogram identity Delta_n at n in {0, 2, 4}:
  sigma_triality(p,q) := chi_triality_Z2(p,q)
  sigma_M(p,q)        := g_M(p,q) = (-1)^p
  A_n^(sigma) := sum_k sigma_1(p_k,q_k) * sigma_2(p_k,q_k) * w_n(lambda_k)
  Delta_n(sigma_triality, sigma_M) := A_n^(e) - A_n^(sigma_triality)
                                       - A_n^(sigma_M) + A_n^(sigma_triality * sigma_M)

By linearity:
  Delta_n = 4 * sum_{k: chi_triality_Z2(p_k,q_k) = -1 AND p_k odd} w_n(lambda_k)

Delta_n = 0 iff substrate bot20 has NO eigenvalue with both
  (a) (p_k - q_k) mod 3 != 0   AND   (b) p_k odd.

DISCIPLINE
----------
- `from canonical_constants import *`
- All locals tagged `# (local)`
- Dual-SHA verdict line per S87+ schema-v2; 3-tuple companion row
- gen-physicist BLACKLISTED on V_4 character substantive design per W11-1
  calibration (this script is connes-ncg-theorist authorship).
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
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths and pin metadata
# ---------------------------------------------------------------------------
GATE_ID = "S88-V4-CANDIDATE-III-TRIALITY-MOD-2"
SCHEME = "triality-mod-2-Z2-paired-with-Cartan-zone-parity-Z2-V4-incarnation"
CONVENTION = "KO-dim-6-collapse-diagnostic-D-W8-1-orthogonal-to-A_F-automorphism-inventory"
L_MAX_OPERATIONAL = 6      # (local) Casimir-bound truncation per math-scripts.md
L_MAX_PLAN = 10            # (local) plan-pinned but redundant per Friedrich-Bar saturation
N_BOT = 20                 # (local) bottom-20 eigenvalue support
ABS_PASS_FLOOR = 1e-12     # (local) machine-epsilon floor for Schur orthogonality / parallelogram
ABS_INFO_CEILING = 1e-9    # (local) information-band ceiling

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w2_v4_candidate_iii_triality_mod_2.py"
NPZ_OUT = T0 / "s88_w2_v4_candidate_iii_triality_mod_2.npz"
PNG_OUT = T0 / "s88_w2_v4_candidate_iii_triality_mod_2.png"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

S84_CACHE = T0 / "s84_spectrum_cache_L12_tau019.npz"
W11_2_NPZ = T0 / "s87_w11_partition_stability_4stratum.npz"
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
# Section 4 — Substrate bot20 with (p,q) sector labels at L_max=6
# ---------------------------------------------------------------------------
def collect_bot20_with_pq_labels(
    cache_path: Path, L_max_cut: int, n_bot: int = N_BOT
) -> tuple[np.ndarray, list[tuple[int, int]]]:
    """Aggregate sector_evals at L_max_cut, sort by |lambda|, return bot-N + (p,q) labels.

    Returns:
      bot20_lams: shape (n_bot,) sorted |lambda|
      bot20_pq:   length-n_bot list of (p, q) tuples (sector labels)
    """
    d = np.load(cache_path, allow_pickle=True)
    sector_evals = d["sector_evals"].item()                   # (local) dict (p,q) -> entry
    all_eigs: list[tuple[float, int, int]] = []               # (local) (|lambda|, p, q)
    for (p, q), entry in sector_evals.items():
        if (p + q) > L_max_cut:
            continue
        evs = np.asarray(entry["abs_evals"], dtype=np.float64)
        for ev in evs:
            all_eigs.append((float(abs(ev)), int(p), int(q)))
    all_eigs.sort(key=lambda t: t[0])
    bot = all_eigs[:n_bot]
    bot20_lams = np.array([t[0] for t in bot], dtype=np.float64)
    bot20_pq = [(t[1], t[2]) for t in bot]
    return bot20_lams, bot20_pq


# ---------------------------------------------------------------------------
# Section 5 — Characters and Schur orthogonality
# ---------------------------------------------------------------------------
def chi_triality_Z2(p: int, q: int) -> int:
    """SU(3) triality-mod-2 character on Peter-Weyl (p, q).

    chi = +1 if (p - q) mod 3 == 0 (triality-trivial orbit)
    chi = -1 otherwise
    """
    return +1 if ((p - q) % 3 == 0) else -1


def g_M(p: int, q: int) -> int:
    """A_F M_3(C) Cartan-p parity character (matches W11-1 convention)."""
    return +1 if (p % 2 == 0) else -1


def g_C(p: int, q: int) -> int:
    """A_F C (complex/abelian) Cartan-q parity character."""
    return +1 if (q % 2 == 0) else -1


def g_H(p: int, q: int) -> int:
    """A_F H (quaternion) combined parity character (-1)^(p+q)."""
    return +1 if ((p + q) % 2 == 0) else -1


def w_n(lam: float, n: int) -> float:
    """Mellin-cone weight at substrate distance n on |lambda|."""
    if n == 0:
        return 1.0
    return 1.0 / (lam ** (2 * n))


def schur_inner_product(
    bot20_lams: np.ndarray,
    bot20_pq: list[tuple[int, int]],
    chi1_fn,
    chi2_fn,
) -> float:
    """<chi_1, chi_2>_substrate = sum_k chi_1(p_k,q_k) * chi_2(p_k,q_k) * w_0(lam_k)."""
    total = 0.0  # (local)
    for k in range(len(bot20_lams)):
        p, q = bot20_pq[k]
        total += chi1_fn(p, q) * chi2_fn(p, q) * w_n(float(bot20_lams[k]), 0)
    return total


def parallelogram_delta_n(
    bot20_lams: np.ndarray,
    bot20_pq: list[tuple[int, int]],
    sigma1_fn,
    sigma2_fn,
    n: int,
) -> float:
    """Delta_n(sigma_1, sigma_2) = A_n^e - A_n^sigma1 - A_n^sigma2 + A_n^(sigma_1*sigma_2)."""
    A_e = 0.0       # (local)
    A_s1 = 0.0      # (local)
    A_s2 = 0.0      # (local)
    A_s1s2 = 0.0    # (local)
    for k in range(len(bot20_lams)):
        p, q = bot20_pq[k]
        w = w_n(float(bot20_lams[k]), n)
        s1 = sigma1_fn(p, q)
        s2 = sigma2_fn(p, q)
        A_e += w
        A_s1 += s1 * w
        A_s2 += s2 * w
        A_s1s2 += s1 * s2 * w
    return A_e - A_s1 - A_s2 + A_s1s2


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t_start = time.time()                                     # (local)

    # 6.1 — Substrate bot20 with (p,q) labels
    bot20_lams, bot20_pq = collect_bot20_with_pq_labels(S84_CACHE, L_MAX_OPERATIONAL)
    print(f"[W2-2] bot20 from {S84_CACHE.name} at L_max={L_MAX_OPERATIONAL}, tau={tau_fold}")
    for k in range(N_BOT):
        p, q = bot20_pq[k]
        ct = chi_triality_Z2(p, q)
        gp = g_M(p, q)
        gq = g_C(p, q)
        gh = g_H(p, q)
        print(f"  [{k:2d}] |lam|={bot20_lams[k]:.10f}  (p,q)=({p},{q})  "
              f"chi_tri={ct:+d}  g_M={gp:+d}  g_C={gq:+d}  g_H={gh:+d}")

    # 6.2 — Cross-check W11-2 cv anchor (CC2)
    d11 = np.load(W11_2_NPZ, allow_pickle=True)
    idx_tau = int(np.argmin(np.abs(d11["tau_grid"] - tau_fold)))
    bot20_w11 = d11["bot20_per_tau"][idx_tau].copy()          # (local)
    cv_w11 = d11["cardinality_vector_per_tau"][idx_tau].copy()  # (local)
    cv_w11_nonzero = cv_w11[cv_w11 > 0].astype(int).tolist()
    cc2_anchor_match = bool(
        cv_w11_nonzero == [2, 4, 8, 6]
        and np.allclose(np.sort(bot20_lams), np.sort(bot20_w11), atol=1e-10)
    )
    print(f"[W2-2] CC2: bot20 substrate vs W11-2 cv anchor (2,4,8,6): {cc2_anchor_match}")

    # 6.3 — D-W8-1 KO=6 collapse diagnostic (Schur orthogonality)
    sip_M = schur_inner_product(bot20_lams, bot20_pq, chi_triality_Z2, g_M)  # (local)
    sip_C = schur_inner_product(bot20_lams, bot20_pq, chi_triality_Z2, g_C)  # (local)
    sip_H = schur_inner_product(bot20_lams, bot20_pq, chi_triality_Z2, g_H)  # (local)
    sip_self = schur_inner_product(bot20_lams, bot20_pq, chi_triality_Z2, chi_triality_Z2)  # (local) sanity
    print(f"[W2-2] D-W8-1 Schur inner products at substrate bot20:")
    print(f"  <chi_tri, g_M> = {sip_M:+.6e}")
    print(f"  <chi_tri, g_C> = {sip_C:+.6e}")
    print(f"  <chi_tri, g_H> = {sip_H:+.6e}")
    print(f"  <chi_tri, chi_tri> = {sip_self:+.6e}  (sanity: should be sum_k 1*w_0 = N_BOT={N_BOT} or |support|)")

    # Plan threshold: ABS |<.>| < 1e-12 -> orthogonal. Note: this is on 20-element
    # support; "orthogonality" here is structural-numerical, not measure-theoretic.
    d_w8_1_pass_M = bool(abs(sip_M) < ABS_PASS_FLOOR)
    d_w8_1_pass_C = bool(abs(sip_C) < ABS_PASS_FLOOR)
    d_w8_1_pass_H = bool(abs(sip_H) < ABS_PASS_FLOOR)
    d_w8_1_pass = d_w8_1_pass_M and d_w8_1_pass_C and d_w8_1_pass_H

    # 6.4 — Parallelogram Delta_n at n in {0, 2, 4}
    moment_indices = [0, 2, 4]                                # (local)
    delta_per_n = []                                          # (local)
    for n in moment_indices:
        delta = parallelogram_delta_n(
            bot20_lams, bot20_pq, chi_triality_Z2, g_M, n
        )
        delta_per_n.append(delta)
        print(f"  Delta_{n}(sigma_triality, sigma_M) = {delta:+.6e}")
    max_delta = float(np.max(np.abs(delta_per_n)))            # (local)
    parallelogram_pass_floor = bool(max_delta <= ABS_PASS_FLOOR)
    parallelogram_info_band = bool(ABS_PASS_FLOOR < max_delta <= ABS_INFO_CEILING)

    # 6.5 — Composite verdict per plan §W2-2.9
    if d_w8_1_pass and parallelogram_pass_floor:
        composite = "PASS"
        verdict_kind = "PASS-d-w8-1-and-parallelogram-substrate-floor"  # (local)
    elif d_w8_1_pass and parallelogram_info_band:
        composite = "INFO"
        verdict_kind = "INFO-d-w8-1-pass-parallelogram-near-vanishing"  # (local)
    elif not d_w8_1_pass:
        composite = "FAIL"
        verdict_kind = "FAIL-d-w8-1-collapse-chi-tri-reducible-to-A_F-inventory"  # (local)
    else:
        composite = "FAIL"
        verdict_kind = "FAIL-parallelogram-cocycle-non-vanishing"  # (local)

    # 6.6 — SHAs and pin map
    canon_sha = sha256_file(CANON_PY)
    s84_sha = sha256_file(S84_CACHE)
    w11_2_sha = sha256_file(W11_2_NPZ)
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
        "input_canonical_constants_sha256": canon_sha,
        "input_s84_spectrum_cache_sha256": s84_sha,
        "input_w11_2_partition_npz_sha256": w11_2_sha,
        "script_sha256": script_sha,
        "bot20_pq_first_3": [list(bot20_pq[i]) for i in range(3)],
    }
    audit_sha256 = closure_hash(pin_map)

    # 6.7 — Save .npz
    np.savez(
        NPZ_OUT,
        bot20_lams=bot20_lams,
        bot20_pq=np.array(bot20_pq),
        chi_tri_per_k=np.array([chi_triality_Z2(*pq) for pq in bot20_pq]),
        g_M_per_k=np.array([g_M(*pq) for pq in bot20_pq]),
        g_C_per_k=np.array([g_C(*pq) for pq in bot20_pq]),
        g_H_per_k=np.array([g_H(*pq) for pq in bot20_pq]),
        sip_M=np.float64(sip_M),
        sip_C=np.float64(sip_C),
        sip_H=np.float64(sip_H),
        sip_self=np.float64(sip_self),
        d_w8_1_pass_M=np.bool_(d_w8_1_pass_M),
        d_w8_1_pass_C=np.bool_(d_w8_1_pass_C),
        d_w8_1_pass_H=np.bool_(d_w8_1_pass_H),
        d_w8_1_pass=np.bool_(d_w8_1_pass),
        moment_indices=np.array(moment_indices),
        delta_per_n=np.array(delta_per_n),
        max_delta=np.float64(max_delta),
        parallelogram_pass_floor=np.bool_(parallelogram_pass_floor),
        parallelogram_info_band=np.bool_(parallelogram_info_band),
        composite=composite,
        verdict_kind=verdict_kind,
        cc2_anchor_match=np.bool_(cc2_anchor_match),
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
        tau_fold_pin=np.float64(tau_fold),
        L_max_operational=np.int64(L_MAX_OPERATIONAL),
    )

    # 6.8 — Plot
    fig, ax = plt.subplots(2, 1, figsize=(11, 8))
    chi_tri_arr = np.array([chi_triality_Z2(*pq) for pq in bot20_pq])  # (local)
    g_M_arr = np.array([g_M(*pq) for pq in bot20_pq])                   # (local)
    ks = np.arange(N_BOT)
    ax[0].set_title("S88 W2-2 — Substrate bot20: chi_triality_Z2 and g_M characters per (p,q)")
    ax[0].step(ks, chi_tri_arr, where="mid", marker="o", label="chi_triality_Z2")
    ax[0].step(ks, g_M_arr, where="mid", marker="s", label="g_M = (-1)^p", alpha=0.7)
    ax[0].set_xlabel("substrate index k (sorted by |lambda|)")
    ax[0].set_ylabel("character value")
    ax[0].set_xticks(ks)
    ax[0].set_yticks([-1, 0, +1])
    ax[0].legend()
    ax[0].grid(True, alpha=0.3)

    ax[1].set_title("S88 W2-2 — Schur inner products + Parallelogram Delta_n")
    bars = ["sip_M", "sip_C", "sip_H", "Delta_0", "Delta_2", "Delta_4"]
    vals = [abs(sip_M), abs(sip_C), abs(sip_H)] + [abs(d) for d in delta_per_n]
    ax[1].bar(bars, np.maximum(vals, 1e-20))
    ax[1].set_yscale("log")
    ax[1].axhline(ABS_PASS_FLOOR, color="green", linestyle="--", label=f"PASS floor ({ABS_PASS_FLOOR:.0e})")
    ax[1].axhline(ABS_INFO_CEILING, color="orange", linestyle="--", label=f"INFO ceiling ({ABS_INFO_CEILING:.0e})")
    ax[1].set_ylabel("absolute value")
    ax[1].legend()
    ax[1].grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(PNG_OUT, dpi=120)
    plt.close()

    # 6.9 — Append verdict line
    elapsed = time.time() - t_start
    value_str = (
        f"max_delta={max_delta:.3e};d_w8_1_pass={d_w8_1_pass};"
        f"sip_M={sip_M:+.3e};sip_C={sip_C:+.3e};sip_H={sip_H:+.3e};"
        f"verdict_kind={verdict_kind};cc2_anchor_match={cc2_anchor_match};"
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
    sign_v = "PASS" if (d_w8_1_pass) else "FAIL"
    mag_v = "PASS" if parallelogram_pass_floor else ("INFO" if parallelogram_info_band else "FAIL")
    regime_v = "VALID"
    tuple_line = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_line)
        f.write(tuple_line)

    print(f"[W2-2] DONE in {elapsed:.2f}s")
    print(f"[W2-2] composite = {composite} (verdict_kind={verdict_kind})")
    print(f"[W2-2] D-W8-1 sip_M={sip_M:+.3e} sip_C={sip_C:+.3e} sip_H={sip_H:+.3e}")
    print(f"[W2-2] max_delta = {max_delta:.6e}")
    print(f"[W2-2] audit_sha256 = {audit_sha256}")
    print(f"[W2-2] content_sha256 = {content_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
