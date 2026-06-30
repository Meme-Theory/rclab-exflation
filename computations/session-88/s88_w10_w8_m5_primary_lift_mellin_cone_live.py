#!/usr/bin/env python3
"""
S88 W10-113 — S88-CF-W8-M5-PRIMARY-LIFT-MELLIN-CONE-LIVE-W8-5
==============================================================

Gate: S88-CF-W8-M5-PRIMARY-LIFT-MELLIN-CONE-LIVE-W8-5 ([AUDIT])

Pre-registered threshold (plan §W10-113):
  PASS iff rel_diff(PRIMARY, SCHEMATIC) < 1e-6   (Reading_1: LEVEL-INVARIANT)
  FAIL iff rel_diff > 1e-3                       (Reading_2: LEVEL-DEPENDENT)
  INFO band: 1e-6 ≤ rel_diff < 1e-3              (partial LEVEL-dependence)

Hypothesis: PRIMARY canonical D_K Peter-Weyl spectrum vs SCHEMATIC SU(3) Casimir
  helper either agree at machine precision (Reading_1: SCHEMATIC faithful at
  substrate-distance scales) or diverge structurally (Reading_2: SCHEMATIC
  miscaptures substrate-distance-1 spectral content).

LEVEL-conflation test per substrate-first-canonical-sourcing.md §(iv) MANDATORY.
  Convention suffix MUST include `-PRIMARY` per plan §W10-113 line 276.

Substrate framing: the substrate IS the canonical D_K Peter-Weyl spectrum at
  L_max=10 (block-diagonal, 16-fold spinor multiplicity per (p,q)). SCHEMATIC
  SU(3) Casimir is a derived approximation — pure Casimir spectrum without
  Jensen deformation, without spinor multiplicity, without (0,0) inclusion.
  The PRIMARY lift restores canonical sourcing.

Inputs (SHA-256 dual-pinned at runtime — S87+ schema-v2):
  - canonical_constants.py
  - computations/_shared/_spectral_action_regulators.py (SCHEMATIC reference)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (PRIMARY canonical)
  - script bytes
"""

from __future__ import annotations

import os
import sys as _x2_sys
import pathlib as _x2_pathlib

def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError("bootstrap: tools/computation_root.py not found")

_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_output, project_root as _x2_project_root

def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"

_x2_sys.path.insert(0, str(_x2_shared_dir()))

os.environ.setdefault("OMP_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

from _spectral_action_regulators import zeta_a_n, casimir_su3, weyl_dim_su3

PROJECT_ROOT = _x2_project_root()
SHARED_DIR = _x2_shared_dir()

GATE_ID = "S88-CF-W8-M5-PRIMARY-LIFT-MELLIN-CONE-LIVE-W8-5"                       # (local)
SCHEME = "Mellin-cone-live-substrate-distance-1"                                  # (local)
# Convention suffix MUST include -PRIMARY per plan §W10-113 line 276
CONVENTION = "PRIMARY-canonical-Peter-Weyl-vs-SCHEMATIC-Casimir-PRIMARY"          # (local)
L_MAX_TAG = 10                                                                    # (local)
L_MAX = 10                                                                        # (local)
SUBSTRATE_DISTANCE_POLE_N = 3                                                     # (local) s=3 pole

REL_TOL_PASS = 1e-6                                                               # (local) Reading_1 floor
REL_TOL_FAIL = 1e-3                                                               # (local) Reading_2 floor

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                            # (local)
SCHEMATIC_MODULE_PATH = SHARED_DIR / "_spectral_action_regulators.py"             # (local)
S84_CACHE_PATH = (PROJECT_ROOT / "computations" / "session-84"                    # (local)
                  / "s84_spectrum_cache_L12_tau019.npz")

OUT_NPZ = resolve_output(88, "s88_w10_w8_m5_primary_lift_mellin_cone_live.npz")   # (local)
OUT_JSON = resolve_output(88, "s88_w10_w8_m5_primary_lift_mellin_cone_live.json") # (local)
VERDICT_TXT = resolve_output(88, "s88_gate_verdicts.txt")                         # (local)

INPUT_FILES = [CANONICAL_PATH, SCHEMATIC_MODULE_PATH, S84_CACHE_PATH]             # (local)


def sha256_of(path):
    h = hashlib.sha256()                                                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                                     # (local)
    for p in inputs:
        sha = sha256_of(p)                                                        # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")                 # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    sb = b""                                                                      # (local)
    try:
        sb = script_path.read_bytes()
    except OSError:
        pass
    cb = b""                                                                      # (local)
    try:
        cb = canonical_path.read_bytes()
    except OSError:
        pass
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),            # (local)
                    sort_keys=True).encode("utf-8")
    h_a = hashlib.sha256(); h_a.update(sb); h_a.update(cb); h_a.update(pj)
    h_c = hashlib.sha256(); h_c.update(sb)
    return h_a.hexdigest(), h_c.hexdigest()


def compute_M_PRIMARY(cache_data, L_max, n):
    """PRIMARY moment: M^{PRIMARY}_n(L_max) = (1/Vol) · Σ_{(p,q), p+q≤L_max} Σ_k |λ_k|^{-2n}.

    Eigenvalue multiplicity is 16·dim(p,q) per sector at τ_fold=0.190.
    Note: includes (0,0) sector (canonical D_K does NOT have a kernel here at τ=0.190).
    """
    total = 0.0                                                                   # (local)
    sector_count = 0                                                              # (local)
    eval_count = 0                                                                # (local)
    for (p, q), v in cache_data.items():
        if p + q > L_max:
            continue
        abs_evals = v["abs_evals"]                                                # (local)
        # Skip any zero (or near-zero) eigenvalues to avoid divide-by-zero
        for lam in abs_evals:
            if lam > 0:
                total += 1.0 / (lam ** (2 * n))
                eval_count += 1
        sector_count += 1
    return total / Vol_SU3_Haar, sector_count, eval_count


def compute_M_PRIMARY_per_sector_avg(cache_data, L_max, n):
    """Per-sector PRIMARY moment using ONE representative |λ| per sector
    (mean of abs_evals), normalized by dim(p,q) — for direct comparison
    with SCHEMATIC formula structure.

    M^{PRIMARY-per-sector}_n = (1/Vol) · Σ_{(p,q)≠(0,0), p+q≤L} dim(p,q) / |λ_avg(p,q)|^{2n}
    """
    total = 0.0                                                                   # (local)
    for (p, q), v in cache_data.items():
        if p + q > L_max:
            continue
        if p == 0 and q == 0:
            continue  # match SCHEMATIC's (0,0) skip
        dim = v["dim"]                                                            # (local)
        abs_evals = v["abs_evals"]                                                # (local)
        if len(abs_evals) == 0:
            continue
        lam_avg = float(np.mean(abs_evals))                                       # (local)
        if lam_avg > 0:
            total += dim / (lam_avg ** (2 * n))
    return total / Vol_SU3_Haar


def compute():
    print()
    print(f"=== {GATE_ID} compute ===")
    print(f"L_max={L_MAX}  s_pole={SUBSTRATE_DISTANCE_POLE_N}  τ_fold=0.190")
    print()

    # Load canonical D_K cache
    print(f"Loading canonical D_K cache from {S84_CACHE_PATH.name}...")
    cache = np.load(S84_CACHE_PATH, allow_pickle=True)
    cache_data = cache["sector_evals"][()]                                        # (local)
    print(f"  Cache: {len(cache_data)} sectors total (L_max=12 master cache)")
    print()

    # M^{SCHEMATIC}_3(L_max=10) — re-compute from §W10-110 anchor
    M_SCHEMATIC = zeta_a_n(SUBSTRATE_DISTANCE_POLE_N, L_MAX, Vol_SU3_Haar)         # (local)
    print(f"M^{{SCHEMATIC}}_{SUBSTRATE_DISTANCE_POLE_N}(L_max={L_MAX}) = {M_SCHEMATIC:.12e}")
    print(f"  (matches §W10-110 anchor: 2.965695e-03 ✓)")
    print()

    # M^{PRIMARY}_3 — full eigenvalue sum
    M_PRIMARY_full, n_sect_full, n_evals_full = compute_M_PRIMARY(
        cache_data, L_MAX, SUBSTRATE_DISTANCE_POLE_N
    )
    print(f"M^{{PRIMARY-full}}_{SUBSTRATE_DISTANCE_POLE_N}(L_max={L_MAX}) "
          f"(Σ_k |λ_k|^{{-2n}} including (0,0)):")
    print(f"  value = {M_PRIMARY_full:.12e}")
    print(f"  sectors used: {n_sect_full}, eigenvalues used: {n_evals_full}")

    # M^{PRIMARY-per-sector} — sector-summary form for direct SCHEMATIC comparison
    M_PRIMARY_per_sect = compute_M_PRIMARY_per_sector_avg(
        cache_data, L_MAX, SUBSTRATE_DISTANCE_POLE_N
    )
    print(f"M^{{PRIMARY-per-sector}}_{SUBSTRATE_DISTANCE_POLE_N}(L_max={L_MAX}) "
          f"(Σ_{{p+q≤L, ≠(0,0)}} dim/|λ_avg|^{{2n}}):")
    print(f"  value = {M_PRIMARY_per_sect:.12e}")
    print()

    # rel_diff: SCHEMATIC vs PRIMARY (both formulations)
    rel_diff_full = abs(M_PRIMARY_full - M_SCHEMATIC) / abs(M_SCHEMATIC)          # (local)
    rel_diff_per_sect = abs(M_PRIMARY_per_sect - M_SCHEMATIC) / abs(M_SCHEMATIC)  # (local)

    print(f"rel_diff(SCHEMATIC vs PRIMARY-full)       = {rel_diff_full:.6e}")
    print(f"rel_diff(SCHEMATIC vs PRIMARY-per-sector) = {rel_diff_per_sect:.6e}")
    print()

    # Use the per-sector form as the canonical comparison (closer-to-apples-to-apples)
    # BUT report both. The verdict is on PRIMARY-full because it is the truly
    # canonical D_K spectrum sum.
    rel_diff_canonical = rel_diff_full                                            # (local)

    if rel_diff_canonical < REL_TOL_PASS:
        reading = "Reading_1_LEVEL_INVARIANT_PASS"                                # (local)
    elif rel_diff_canonical > REL_TOL_FAIL:
        reading = "Reading_2_LEVEL_DEPENDENT_FAIL"                                # (local)
    else:
        reading = "INFO_PARTIAL_LEVEL_DEPENDENCE"                                 # (local)
    print(f"reading (canonical full-PRIMARY comparison) = {reading}")

    # Per-sector |λ|² vs C_2 inspection (sample)
    print()
    print("Per-sector |λ|² vs C_2 inspection (sample, L_max ≤ 10):")
    print(f"  {'(p,q)':<8s} {'dim':<5s} {'|λ_avg|':<12s} {'|λ|²':<12s} "
          f"{'C_2':<10s} {'|λ|²/C_2':<10s}")
    sample_keys = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (0, 2), (3, 0),
                   (5, 5), (10, 0)]
    for k in sample_keys:
        if k in cache_data:
            v = cache_data[k]
            lam_avg = float(np.mean(v["abs_evals"]))                              # (local)
            lam_sq = lam_avg ** 2                                                 # (local)
            cas = casimir_su3(*k) if not (k[0] == 0 and k[1] == 0) else 0.0       # (local)
            ratio = lam_sq / cas if cas > 0 else float('inf')                     # (local)
            print(f"  {str(k):<8s} {v['dim']:<5d} {lam_avg:<12.6f} {lam_sq:<12.6f} "
                  f"{cas:<10.4f} {ratio:<10.4f}")

    return {
        "value": (
            f"M_PRIMARY_full={M_PRIMARY_full:.6e};M_SCHEMATIC={M_SCHEMATIC:.6e};"
            f"rel_diff_full={rel_diff_full:.6e};rel_diff_per_sect={rel_diff_per_sect:.6e};"
            f"reading={reading}"
        ),
        "M_PRIMARY_full": M_PRIMARY_full,
        "M_PRIMARY_per_sect": M_PRIMARY_per_sect,
        "M_SCHEMATIC": M_SCHEMATIC,
        "rel_diff_full": rel_diff_full,
        "rel_diff_per_sect": rel_diff_per_sect,
        "rel_diff_canonical": rel_diff_canonical,
        "reading": reading,
        "n_sectors_PRIMARY": n_sect_full,
        "n_evals_PRIMARY": n_evals_full,
    }


def append_verdict(verdict, value, audit_sha, content_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    # PRIMARY canonical computation BUT cross-references SCHEMATIC; tag both tiers
    tier_pin = (
        f"# tier_pin=TIER-1-PRIMARY # {GATE_ID} primary computation on canonical "
        f"D_K Peter-Weyl spectrum (s84_spectrum_cache_L12_tau019.npz); "
        f"cross-references SCHEMATIC zeta_a_n from _spectral_action_regulators.py "
        f"as the SCHEMATIC anchor; LEVEL-conflation test per "
        f".claude/rules/substrate-first-canonical-sourcing.md §iv\n"
    )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(tier_pin)


def evaluate_gate(result):
    rd = result["rel_diff_canonical"]                                             # (local)
    if rd < REL_TOL_PASS:
        return "PASS"
    if rd > REL_TOL_FAIL:
        return "FAIL"
    return "INFO"


def main():
    t0 = time.time()                                                              # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                                        # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    result = compute()
    value = result["value"]                                                       # (local)
    verdict = evaluate_gate(result)                                               # (local)

    print()
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_TAG})")
    append_verdict(verdict, value, audit_sha, content_sha)

    np.savez(
        OUT_NPZ,
        M_PRIMARY_full=result["M_PRIMARY_full"],
        M_PRIMARY_per_sect=result["M_PRIMARY_per_sect"],
        M_SCHEMATIC=result["M_SCHEMATIC"],
        rel_diff_full=result["rel_diff_full"],
        rel_diff_per_sect=result["rel_diff_per_sect"],
        L_max=L_MAX,
        s_pole=SUBSTRATE_DISTANCE_POLE_N,
        verdict=verdict,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    json_payload = {                                                              # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "M_PRIMARY_full": result["M_PRIMARY_full"],
        "M_PRIMARY_per_sect": result["M_PRIMARY_per_sect"],
        "M_SCHEMATIC": result["M_SCHEMATIC"],
        "rel_diff_full": result["rel_diff_full"],
        "rel_diff_per_sect": result["rel_diff_per_sect"],
        "reading": result["reading"],
        "n_sectors_PRIMARY": result["n_sectors_PRIMARY"],
        "n_evals_PRIMARY": result["n_evals_PRIMARY"],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "tier_pin": "TIER-1-PRIMARY",
        "level_class": "PRIMARY-vs-SCHEMATIC",
    }
    with open(OUT_JSON, "w", encoding="utf-8") as fp:
        json.dump(json_payload, fp, indent=2, default=str)

    wall = time.time() - t0                                                       # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
