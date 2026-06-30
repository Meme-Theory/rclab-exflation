#!/usr/bin/env python3
"""
S88 W5a-44 — S88-A_2-MELLIN-SPECTRUM-CACHE-DISCRIMINATOR
=========================================================

Gate: S88-A_2-MELLIN-SPECTRUM-CACHE-DISCRIMINATOR (trigger: VERIFY)
Wave: W5a (COMPUTE-class — substrate-IS bit-exact reproduction of α_s_canonical
       via CM-1995 §III.4 Mellin residue at L_max=12, Route-A canonical primacy
       WITHOUT invoking Route-B n_s²−1)
Plan: sessions/session-plan/session-88-plan-w5a.md §W5a-44

Pre-registered threshold (per plan §W5a-44 Field 9):
  PASS:  rel_diff ≤ 1e-12 against α_s_canonical = -8587279/100000000 via
         CM-1995 §III.4 formula evaluated on cache eigenvalues + Mellin
         moment normalization, WITHOUT n_s² invocation.
  FAIL:  rel_diff > 1e-12 — bit-exact reproduction failed; either cache
         integrity, Mellin pin drift, formula evaluation defect, or
         scheme mismatch.
  INFO:  rel_diff ∈ (1e-12, 1e-9] — publication-precision floor exceeded
         but within ~10^(-publication_sig_figs) band per Class 8.3.

Substitution chain (per plan §W5a-44 Field 10):
  Definition 1: D_K = Dirac on Jensen-deformed SU(3) at τ=0.190;
                cached spectrum {λ_k, m_k} in s84_spectrum_cache_L12_tau019.npz
                as sector_evals dict keyed by (p,q), each entry containing
                dim (irrep multiplicity) + abs_evals (16-component spinor block)
  Definition 2: Tr(D_K^{−2s}) = Σ_k m_k λ_k^{−2s} (zeta-regulated trace)
  Definition 3: a_n = Res[Tr(D_K^{−2s}); s = (d−n)/2] = Σ_k m_k λ_k^{−(d−n)}
                (Connes-Moscovici 1995 §III.4 dim-spectrum residue formula at d=4)
  Definition 4: At d=4, n=2 ⇒ exponent (d−n) = 2:
                a_2 = Σ_k m_k λ_k^{−2}
                For block-diagonal D_K with sector multiplicity dim(p,q),
                eigenvalues |λ| = abs_evals from cache, 16 per sector copy:
                a_2 = Σ_{(p,q)} dim(p,q) · Σ_{i=1..16} (abs_evals[i])^{−2}
  Definition 5: α_s_canonical_target = -8587279/100000000 = -0.08587279
                (S82 W3-9 closure, Sage-QQ exact)
  Definition 6: Mellin moment pins (S82 W3-9 normalization):
                f0 = 0.0883200; f2 = 214.97335676; f4 = 6446.63942272
                (the substrate-first canonical Mellin moments per plan
                 §W5a-44 Field 7; their algebraic role in the
                 normalization is the structural question this gate tests)

  Step 7 (substitute): compute a_2 from cache; then evaluate candidate
                normalization formulas combining a_2 with (f0, f2, f4) and
                compare to α_s_canonical_target.

  Step 8 (Route-B exclusion): the script MUST NOT import n_s for the
                bit-exact test path. n_s reading is permitted ONLY in the
                Discussion §"cross-reference" output for narrative.

  Step 9 (direction): PASS iff at least one substrate-first normalization
                reproduces α_s_canonical_target with rel_diff ≤ 1e-12.

Plan-authorship caveat (logged honestly):
  The plan §W5a-44 Field 6 step 3 says "Substitute Mellin moment pins
  (f0, f2, f4) per S82 W3-9 normalization; evaluate the substrate-distance-1
  single-pole residue in the project's canonical pole convention" but does
  NOT give an explicit closed-form normalization formula. S82 W3-9
  s82_w3_9_as_adjacent_obs.py treats α_s as the SCHEME-IDENTITY n_s²−1 (Route B),
  not a Mellin residue. This script tries several plausible Route-A
  normalizations and reports rel_diff for each. If none reaches 1e-12, the
  gate FAILs honestly with a structural diagnostic — this would surface the
  hypothesis that the S82 W3-9 "single-pole Mellin closure" framing in
  plan §W5a-37 / §W5a-44 is a re-rationalization rather than an
  independently derivable Route A.

Inputs:
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
    (sector_evals dict, 90 sectors, p+q ≤ 12; SHA pinned in pin_map)
  - computations/_shared/canonical_constants.py
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from fractions import Fraction
from pathlib import Path

T0 = Path(__file__).resolve().parent
PROJECT_ROOT = T0.parent.parent
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))

# Note: we DELIBERATELY do NOT import n_s from canonical_constants for the
# bit-exact path; importing tau_fold + tau_pivot is fine (substrate slice).
from canonical_constants import tau_fold, tau_pivot  # noqa: E402

# Pin metadata
GATE_ID = "S88-A_2-MELLIN-SPECTRUM-CACHE-DISCRIMINATOR"
SCHEME = "mellin-residue-substrate-distance-1-pole"
CONVENTION = "connes-moscovici-1995-III-4-substrate-first-route-A"
L_MAX = "12"  # (local) cache L_max
PUBLICATION_PRECISION_FLOOR = 1e-12  # (local) PASS threshold
INFO_FLOOR = 1e-9  # (local) INFO band ceiling per Class 8.3

# α_s canonical Sage-QQ exact (target)
TARGET_NUM = -8587279  # (local)
TARGET_DEN = 100000000  # (local)
TARGET_VALUE = TARGET_NUM / TARGET_DEN  # (local) = -0.08587279

# Mellin moment pins (per plan §W5a-44 Field 7)
MELLIN_F0 = 0.0883200  # (local)
MELLIN_F2 = 214.97335676  # (local)
MELLIN_F4 = 6446.63942272  # (local)

# Files
SCRIPT_PATH = T0 / "s88_w5a_a2_mellin_spectrum_cache_discriminator.py"
NPZ_OUT = T0 / "s88_w5a_a2_mellin_spectrum_cache_discriminator.npz"
PNG_OUT = T0 / "s88_w5a_a2_mellin_spectrum_cache_discriminator.png"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

CACHE_PATH = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANON_PY = SHARED_DIR / "canonical_constants.py"
PLAN_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w5a.md"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def main() -> int:
    t_start = time.time()
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # ──────────────────────────────────────────────────────────────────
    # 1 — Cache integrity verification
    # ──────────────────────────────────────────────────────────────────
    cache_sha = sha256_file(CACHE_PATH)
    expected_sha_prefix = "9e6d9cf7fd6a6949"  # (local) per plan §W5a-44 Field 7
    cc_cache_sha = cache_sha.startswith(expected_sha_prefix)
    print(f"[W5a-44] Cache SHA-256: {cache_sha}")
    print(f"[W5a-44] CC1 cache SHA prefix matches '{expected_sha_prefix}': {cc_cache_sha}")

    # ──────────────────────────────────────────────────────────────────
    # 2 — Load cache + structural verification
    # ──────────────────────────────────────────────────────────────────
    d = np.load(CACHE_PATH, allow_pickle=True)
    sector_evals = d["sector_evals"].item()
    n_sectors = len(sector_evals)
    print(f"[W5a-44] Loaded cache: {n_sectors} sectors")

    # Verify p+q range covers L_max=12
    pq_max = max(p + q for (p, q) in sector_evals.keys())
    cc_lmax = (pq_max == 12)
    print(f"[W5a-44] CC2 max(p+q) = {pq_max} (expected 12): {cc_lmax}")

    # Total D_K eigenvalue count: Σ_{(p,q)} dim(p,q) · 16
    total_eigs_with_mult = 0  # (local)
    total_distinct_eigs = 0  # (local)
    for (p, q), v in sector_evals.items():
        dim = v["dim"]
        evals = v["abs_evals"]
        total_eigs_with_mult += dim * len(evals)
        total_distinct_eigs += len(evals)
    print(f"[W5a-44] Total eigenvalues (multiplicity-weighted): {total_eigs_with_mult}")
    print(f"[W5a-44] Total distinct |eigenvalues| in cache:     {total_distinct_eigs}")

    # ──────────────────────────────────────────────────────────────────
    # 3 — Compute a_2 = Σ m_k λ_k^{−2} (CM-1995 §III.4 at d=4, n=2)
    # ──────────────────────────────────────────────────────────────────
    a_2_raw = 0.0  # (local)
    for (p, q), v in sector_evals.items():
        dim = v["dim"]
        abs_evals = v["abs_evals"]
        # Defensive: skip any zero-eigenvalue entries (would cause inf)
        nonzero = abs_evals[abs_evals > 1e-15]
        sector_contribution = dim * float(np.sum(nonzero ** -2))
        a_2_raw += sector_contribution
    print(f"[W5a-44] a_2 (raw, CM-1995 §III.4 at d=4, n=2): {a_2_raw:.10f}")

    # Also compute Σ m_k λ_k^{−4} (a_4 analog) and Σ m_k λ_k^{0} = trace count
    a_4_raw = 0.0  # (local)
    a_0_raw = 0.0  # (local)
    for (p, q), v in sector_evals.items():
        dim = v["dim"]
        abs_evals = v["abs_evals"]
        nonzero = abs_evals[abs_evals > 1e-15]
        a_4_raw += dim * float(np.sum(nonzero ** -4))
        a_0_raw += dim * len(nonzero)
    print(f"[W5a-44] a_4 (raw, n=4 analog): {a_4_raw:.6f}")
    print(f"[W5a-44] a_0 (eigenvalue count, multiplicity-weighted): {a_0_raw:.0f}")

    # ──────────────────────────────────────────────────────────────────
    # 4 — Try multiple Route-A normalization formulas; tabulate rel_diff
    # ──────────────────────────────────────────────────────────────────
    # The plan does not specify the formula explicitly. Try plausible forms:
    candidates = []  # (label, value, formula_description)

    # Try the negative of (a_2 / a_0) — a normalized moment ratio
    cand_v = -(a_2_raw / a_0_raw) if a_0_raw != 0 else float("nan")
    candidates.append(("- a_2 / a_0", cand_v, "negative ratio of 2nd to 0th raw moment"))

    # Try (a_2 - f2) / f4
    cand_v = (a_2_raw - MELLIN_F2) / MELLIN_F4 if MELLIN_F4 != 0 else float("nan")
    candidates.append(("(a_2 - f2)/f4", cand_v, "shifted by f2, normalized by f4"))

    # Try -a_2 × f0 / f4
    cand_v = -(a_2_raw * MELLIN_F0 / MELLIN_F4) if MELLIN_F4 != 0 else float("nan")
    candidates.append(("-a_2·f0/f4", cand_v, "Mellin moment ratio"))

    # Try -f0 (Mellin moment alone — sanity)
    candidates.append(("-f0", -MELLIN_F0, "negation of f0 alone"))

    # Try (f0 - 1)
    candidates.append(("f0 - 1", MELLIN_F0 - 1.0, "shift convention"))

    # Try -(f2 / a_2_raw) factor of canonical
    if a_2_raw != 0:
        cand_v = -(MELLIN_F2 / a_2_raw) * MELLIN_F0
        candidates.append(("-(f2/a_2)·f0", cand_v, "alternate Mellin pole-residue"))

    # Try a_2 / (some normalization power of the ground-state eigenvalue)
    # ground-state: sector (0,0), abs_evals[0] = 0.97140762
    lambda_0 = sector_evals[(0, 0)]["abs_evals"][0]
    cand_v = -(a_2_raw / a_0_raw) * (lambda_0 ** 2)
    candidates.append(("-(a_2/a_0)·λ_0²", cand_v, "ground-state eigenvalue normalization"))

    # Try the n_s² − 1 SCHEME identity using λ_0 as a stand-in (NOT importing n_s)
    # This is just a sanity diagnostic: if n_s ≈ λ_0, then n_s² − 1 ≈ λ_0² − 1
    cand_v = lambda_0 ** 2 - 1.0
    candidates.append(("λ_0² − 1 (diag)", cand_v, "ground-state-eigenvalue scheme analog (NOT Route A)"))

    print(f"\n[W5a-44] Route-A normalization candidates:")
    print(f"[W5a-44]   target α_s_canonical = {TARGET_VALUE:+.10f}")
    print(f"[W5a-44]   {'label':<22s} {'value':>18s} {'rel_diff':>14s} {'description':s}")
    best_rel_diff = float("inf")
    best_candidate = None  # (local)
    for label, val, desc in candidates:
        if math.isnan(val) or math.isinf(val):
            continue
        rel_diff = abs(val - TARGET_VALUE) / abs(TARGET_VALUE)
        marker = "  <-- BEST" if rel_diff < best_rel_diff else ""
        if rel_diff < best_rel_diff:
            best_rel_diff = rel_diff
            best_candidate = (label, val, desc)
        print(f"[W5a-44]   {label:<22s} {val:>+18.10f} {rel_diff:>14.6e} {desc}{marker}")

    print(f"\n[W5a-44] Best candidate: '{best_candidate[0]}' = {best_candidate[1]:+.10f}")
    print(f"[W5a-44] Best rel_diff: {best_rel_diff:.6e} (PASS iff ≤ {PUBLICATION_PRECISION_FLOOR:.0e})")

    # ──────────────────────────────────────────────────────────────────
    # 5 — Composite verdict (Route-A bit-exact reproduction test)
    # ──────────────────────────────────────────────────────────────────
    if not cc_cache_sha:
        composite = "FAIL"
        verdict_kind = "FAIL-cache-sha-mismatch"
    elif not cc_lmax:
        composite = "FAIL"
        verdict_kind = "FAIL-cache-lmax-mismatch"
    elif best_rel_diff <= PUBLICATION_PRECISION_FLOOR:
        composite = "PASS"
        verdict_kind = f"PASS-route-A-bit-exact-via-{best_candidate[0].replace(' ', '_')}"
    elif best_rel_diff <= INFO_FLOOR:
        composite = "INFO"
        verdict_kind = f"INFO-route-A-publication-precision-floor-{best_rel_diff:.2e}-best={best_candidate[0]}"
    else:
        composite = "FAIL"
        verdict_kind = (
            f"FAIL-no-route-A-normalization-reproduces-target-best={best_candidate[0]}-"
            f"rel_diff={best_rel_diff:.2e}-suggests-S82-W3-9-framing-is-route-B-rationalization"
        )

    print(f"\n[W5a-44] composite = {composite}")
    print(f"[W5a-44] verdict_kind = {verdict_kind}")

    # ──────────────────────────────────────────────────────────────────
    # 6 — Plot a_2 contributions per sector (diagnostic)
    # ──────────────────────────────────────────────────────────────────
    sector_contribs = []
    for (p, q), v in sector_evals.items():
        dim = v["dim"]
        abs_evals = v["abs_evals"]
        nonzero = abs_evals[abs_evals > 1e-15]
        c = dim * float(np.sum(nonzero ** -2))
        sector_contribs.append(((p, q), c))
    sector_contribs.sort(key=lambda x: -x[1])
    top10 = sector_contribs[:10]
    fig, ax = plt.subplots(figsize=(9, 4.5))
    labels = [f"({p},{q})" for (p, q), _ in top10]
    values = [c for _, c in top10]
    ax.bar(range(len(labels)), values, edgecolor="black", color="#4477AA")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels)
    ax.set_xlabel("sector (p,q)")
    ax.set_ylabel("contribution to a_2 = dim · Σ |λ|^{-2}")
    ax.set_title(f"S88 W5a-44: top-10 sector contributions to a_2 (cache L_max=12, τ={tau_fold})")
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(PNG_OUT, dpi=120)
    plt.close(fig)
    print(f"[W5a-44] PNG saved: {PNG_OUT.name}")

    # ──────────────────────────────────────────────────────────────────
    # 7 — Compute SHAs
    # ──────────────────────────────────────────────────────────────────
    canon_sha = sha256_file(CANON_PY)
    plan_sha = sha256_file(PLAN_PATH)
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha
    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "cache_sha256": cache_sha,
        "n_sectors": n_sectors,
        "total_eigs_with_mult": total_eigs_with_mult,
        "a_2_raw": a_2_raw,
        "a_4_raw": a_4_raw,
        "a_0_raw": a_0_raw,
        "MELLIN_F0": MELLIN_F0,
        "MELLIN_F2": MELLIN_F2,
        "MELLIN_F4": MELLIN_F4,
        "TARGET_NUM": TARGET_NUM,
        "TARGET_DEN": TARGET_DEN,
        "best_candidate_label": best_candidate[0] if best_candidate else None,
        "best_candidate_value": best_candidate[1] if best_candidate else None,
        "best_rel_diff": best_rel_diff,
        "PUBLICATION_PRECISION_FLOOR": PUBLICATION_PRECISION_FLOOR,
        "INFO_FLOOR": INFO_FLOOR,
        "input_canonical_constants_sha256": canon_sha,
        "input_plan_sha256": plan_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    # ──────────────────────────────────────────────────────────────────
    # 8 — Save .npz
    # ──────────────────────────────────────────────────────────────────
    np.savez(
        NPZ_OUT,
        cache_sha256=cache_sha,
        n_sectors=np.int64(n_sectors),
        total_eigs_with_mult=np.int64(total_eigs_with_mult),
        a_2_raw=np.float64(a_2_raw),
        a_4_raw=np.float64(a_4_raw),
        a_0_raw=np.float64(a_0_raw),
        target_value=np.float64(TARGET_VALUE),
        candidate_labels=np.array([c[0] for c in candidates], dtype=object),
        candidate_values=np.array([c[1] for c in candidates], dtype=np.float64),
        best_label=best_candidate[0] if best_candidate else "none",
        best_value=np.float64(best_candidate[1]) if best_candidate else np.float64(0.0),
        best_rel_diff=np.float64(best_rel_diff),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )

    # ──────────────────────────────────────────────────────────────────
    # 9 — Append verdict trio
    # ──────────────────────────────────────────────────────────────────
    elapsed = time.time() - t_start
    value_str = (
        f"a_2_raw={a_2_raw:.6f};a_4_raw={a_4_raw:.4f};a_0={a_0_raw:.0f};"
        f"target={TARGET_VALUE};best_label={best_candidate[0] if best_candidate else 'none'};"
        f"best_value={best_candidate[1] if best_candidate else 0.0:.10f};"
        f"best_rel_diff={best_rel_diff:.4e};verdict_kind={verdict_kind}"
    )
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
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

    print(f"[W5a-44] DONE in {elapsed:.2f}s")
    print(f"[W5a-44] audit_sha256   = {audit_sha256}")
    print(f"[W5a-44] content_sha256 = {content_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
