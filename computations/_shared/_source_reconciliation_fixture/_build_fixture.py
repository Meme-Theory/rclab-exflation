#!/usr/bin/env python
"""
_build_fixture.py
==================

Deterministic builder for the 13-site SOURCE-RECONCILIATION retrospective fixture.

Each site contains 4 files:
    pin_declared.sha256       (declared SHA-256 of the plan-pin, OR sentinel)
    on_disk.sha256            (SHA-256 of the on-disk file at audit time, OR sentinel)
    expected_class.txt        (one of S86 5-class taxonomy: A/B/C/D/E)
    expected_distance.float   (d_i in log10 OOM units, per K3/K4 of s85-5a-pin-drift-taxonomy.md)

The d_i values are sourced from:
    s85-5a-pin-drift-taxonomy.md K3 §183-197 (per-site classification + severity)
    s85-5a-pin-drift-taxonomy.md K4 §286-292 (Lyapunov-style d_i floats)

D_max = 5.6726 (site #10 GPU L=12) is the dominating site by L-infinity norm.
Threshold direction (substitution chain in plan §10):
    PASS iff abs(D_max_replayed - 5.6726) <= 1e-10  =>  monotone-decreasing in abs_error.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

FIXTURE_DIR = Path(__file__).resolve().parent

# 13 sites. Each tuple: (site_id, pin_declared, on_disk, expected_class, d_i_oom)
# - "REAL_SHA_<tag>" placeholders are replaced by sha256_of_text("<tag>") — deterministic.
# - "UNPINNED" / "MULTIPLE" / "MISSING" are sentinels classified directly.
SITES = [
    # site_id, K3-narrative, S86_class,         d_i,       pin_token,   ondisk_token
    ( 1, "W7-1 H-tilde TD anchor",       "A_PINNED_AND_MATCHED",        0.0979, "TOK_S1",       "TOK_S1"      ),
    ( 2, "W7-1 H-tilde LI anchor",       "B_PINNED_BUT_DRIFTED",        4.5393, "TOK_S2_PIN",   "TOK_S2_DISK" ),
    ( 3, "W7-2 CC-6 single-channel",     "D_PINNED_BUT_MISSING",        0.0000, "TOK_S3_PIN",   "MISSING"     ),
    ( 4, "W11-1 L_max=10 vs 5 anchor",   "B_PINNED_BUT_DRIFTED",        0.6021, "TOK_S4_PIN",   "TOK_S4_DISK" ),
    ( 5, "W11-1 FAIL floor 1e-4 vs 4",   "B_PINNED_BUT_DRIFTED",        4.6021, "TOK_S5_PIN",   "TOK_S5_DISK" ),
    ( 6, "W11-2 sig_2 SHA-cross scope",  "B_PINNED_BUT_DRIFTED",        0.3010, "TOK_S6_PIN",   "TOK_S6_DISK" ),
    ( 7, "W11-4 schedule label drift",   "E_PINNED_MULTIPLE_DIVERGENT", 0.0000, "MULTIPLE",     "TOK_S7_DISK" ),
    ( 8, "W13-1 epsilon_pivot 0.020",    "B_PINNED_BUT_DRIFTED",        0.0340, "TOK_S8_PIN",   "TOK_S8_DISK" ),
    ( 9, "W13-4 R1-RANK beta heuristic", "B_PINNED_BUT_DRIFTED",        2.3088, "TOK_S9_PIN",   "TOK_S9_DISK" ),
    (10, "W10-4 GPU-mandatory at L=12",  "B_PINNED_BUT_DRIFTED",        5.6726, "TOK_S10_PIN",  "TOK_S10_DISK"),  # D_max
    (11, "W9-1 Borel floor pin->canon",  "A_PINNED_AND_MATCHED",        0.0000, "TOK_S11",      "TOK_S11"     ),
    (12, "W12-2 PRDR bare-K keyword",    "C_UNPINNED_BUT_REFERENCED",   0.7782, "UNPINNED",     "TOK_S12_DISK"),
    (13, "W7-2 CC-6 k_cusp placement",   "B_PINNED_BUT_DRIFTED",        1.1556, "TOK_S13_PIN",  "TOK_S13_DISK"),
]


def sha256_of_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def resolve_token(token: str) -> str:
    """Sentinels pass through; otherwise hash the token deterministically."""
    if token in ("MISSING", "UNPINNED", "MULTIPLE"):
        return token
    return sha256_of_text(token)


def write_site(site_id: int, narrative: str, expected_class: str, d_i: float,
               pin_token: str, ondisk_token: str) -> None:
    site_dir = FIXTURE_DIR / f"site_{site_id}"
    site_dir.mkdir(exist_ok=True)
    (site_dir / "pin_declared.sha256").write_text(resolve_token(pin_token) + "\n")
    (site_dir / "on_disk.sha256").write_text(resolve_token(ondisk_token) + "\n")
    (site_dir / "expected_class.txt").write_text(expected_class + "\n")
    (site_dir / "expected_distance.float").write_text(f"{d_i:.10f}\n")
    # Narrative comment file (informational only; audit script ignores)
    (site_dir / "_narrative.txt").write_text(
        f"site_{site_id}: {narrative}\n"
        f"S86_class: {expected_class}\n"
        f"d_i (log10 OOM): {d_i:.4f}\n"
        f"source: sessions/archive/session-85/workshops/s85-5a-pin-drift-taxonomy.md K3+K4\n"
    )


def main() -> None:
    print(f"Building 13-site SOURCE-RECONCILIATION fixture at {FIXTURE_DIR}")
    distances = []
    class_dist = {}
    for (sid, nar, cls, d, pt, ot) in SITES:
        write_site(sid, nar, cls, d, pt, ot)
        distances.append(d)
        class_dist[cls] = class_dist.get(cls, 0) + 1
        print(f"  site_{sid:>2}: class={cls:<32} d_i={d:.4f}")
    D_max = max(distances)
    D_sum = sum(distances)
    D_L2 = (sum(d * d for d in distances)) ** 0.5
    print(f"\nDistribution: {class_dist}")
    print(f"D_max = {D_max:.10f}")
    print(f"D_sum = {D_sum:.10f}")
    print(f"D_L2  = {D_L2:.10f}")
    print(f"D_max - 5.6726 = {D_max - 5.6726:.3e}")
    assert abs(D_max - 5.6726) <= 1e-10, f"D_max mismatch: {D_max} vs 5.6726"
    print("\nFixture build complete; D_max == 5.6726 to 1e-10.")


if __name__ == "__main__":
    main()
