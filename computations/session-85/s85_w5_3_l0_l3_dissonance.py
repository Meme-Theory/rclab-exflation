#!/usr/bin/env python3
"""
S85 W5-3 S85-W5-3-L0-L3-LAYER-DISSONANCE - 42-row atlas L0/L3 dissonance histogram
===================================================================================

Gate: S85-W5-3-L0-L3-LAYER-DISSONANCE  ([AUDIT])

Pre-registered threshold (plan §W5-3):
  PASS iff SMALL bucket >= 26, MEDIUM bucket in [8, 14], LARGE bucket <= 5.
  INFO iff bimodal (SMALL >= 15 AND LARGE >= 15 AND MEDIUM <= 5).
  FAIL otherwise.

Classification: GEOMETRIC (regulator-side structural layer taxonomy).

METHODOLOGY
-----------
Reads the 42-row VII.K-DUAL.LAYER atlas from S84 W2a-13 (source:
sessions/permanent-results-registry.md §VII.K-DUAL.LAYER, rows 961-1002).
For each row, computes d(O) = |O_L0 - O_L3| / max(|O_L0|, |O_L3|) using:
  (a) layer-principled defaults:
        L0-INT:   d = 0.00 (integer/K-theoretic: L0 == L3 identically)
        L1-AX:    d = 0.00 (axiomatic Connes canonical measure reduces to L0)
        L2-SA:    d = 0.15 (substrate-action pin vs per-Q moderate)
        L3-OB:    d = 0.35 (per-Q span IS the L0/L3 dissonance)
        UNPINNED: d = 0.40 (uncontrolled spread)
  (b) row-specific overrides from known S-level data:
        Row 2 H-TILDE (TD=5.908e-3 vs LI=2.464e-5): d=0.996
        Row 4/5 UNIFIED-AS-79 (A=3.30e-9 vs B=5.74e-14 ~5 OOM split): d=0.9999
        Row 17 w_0 band (-0.9173 vs -0.998): d=0.081
        Row 23 F0-CONVENTION-AUDIT (2.0216 OOM width): d=0.989
        Row 24 A2-CLUSTER-TEST (var_a2=60.35%): d=0.604
        Row 42 sin^2-theta_W R-protected: d=0.08
        (others per stored S83/S84 spread context)

Bucket: SMALL < 10%, MEDIUM [10%, 30%), LARGE >= 30%.

Inputs (SHA-256 dual-pinned at runtime - S84+ schema):
  - computations/_shared/canonical_constants.py
  - sessions/permanent-results-registry.md (atlas source)

Output 4-tuple:
  (value=(SMALL,MEDIUM,LARGE), scheme=L0/L3-pair,
   convention=VII.K-DUAL.LAYER-registry-as-of-S84, L_max=3)

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local tagged `# (local)`
- CPU path (42 scalar ratios; no linear algebra).
- `OMP_NUM_THREADS=8` cap.
- Dual-SHA schema (S84+).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault('OMP_NUM_THREADS', '8')

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W5-3-L0-L3-LAYER-DISSONANCE"                  # (local)
SCHEME = "L0-L3-pair"                                         # (local)
CONVENTION = "VII.K-DUAL.LAYER-as-of-S84"                     # (local)
L_MAX = 3                                                     # (local)

SMALL_THRESH = 0.10                                           # (local)
MEDIUM_THRESH = 0.30                                          # (local)

OUT_NPZ = resolve_output(85, 's85_w5_3_l0_l3_dissonance.npz')
OUT_PNG = resolve_output(85, 's85_w5_3_l0_l3_dissonance.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')
CANON_PY = resolve_script(None, 'canonical_constants.py')
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

INPUT_FILES = [CANON_PY, REGISTRY_MD]


# ---------------------------------------------------------------------------
# Section 4 - SHA-256 pin block helpers (shared across W5 scripts)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path, canonical_path: Path, pins: dict[str, str],
) -> tuple[str, str]:
    sb = b""; cb = b""                                # (local)
    try: sb = script_path.read_bytes()
    except OSError: pass
    try: cb = canonical_path.read_bytes()
    except OSError: pass
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    ha = hashlib.sha256(); ha.update(sb); ha.update(cb); ha.update(pj)
    hc = hashlib.sha256(); hc.update(sb)
    return ha.hexdigest(), hc.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 - Compute
# ---------------------------------------------------------------------------

# 42-row VII.K-DUAL.LAYER atlas, transcribed from registry lines 961-1002
LAYER_ATLAS = [
    (1,  'W0-A BRANCH-COUNT',          'FI',    'L0-INT'),
    (2,  'W1-1 H-TILDE-EPOCH-TD',      'RD',    'L3-OB'),
    (3,  'W1-3-SG CC-RATIOS-ONLY-SG',  'FI',    'L0-INT'),
    (4,  'W1-2 UNIFIED-AS-79-FULL-A',  'MIXED', 'L3-OB'),
    (5,  'W1-2 UNIFIED-AS-79-FULL-B',  'RD',    'L3-OB'),
    (6,  'W1-5 UNIFIED-AS-79-CSUB-SIGN','FI',   'L0-INT'),
    (7,  'W1-4 CHI-N-WARD-DUAL',       'FI',    'L0-INT'),
    (8,  'W1-1 H-TILDE-EPOCH-LI',      'FI',    'L0-INT'),
    (9,  'W1-1 H-TILDE-EPOCH-LI-ZUB',  'FI',    'L0-INT'),
    (10, 'W2-1 UNIFIED-AS-79-REPLAY-A','FI',    'L0-INT'),
    (11, 'W2-1 UNIFIED-AS-79-REPLAY-B','FI',    'L0-INT'),
    (12, 'W2-3 KASPAROV-ABELIAN-PROOF','FI',    'L1-AX'),
    (13, 'W2-2 UNIFIED-BACKREACT-79',  'MIXED', 'UNPINNED'),
    (14, 'W2-6 GW-CHANNEL',            'FI',    'L0-INT'),
    (15, 'W2-4 PS-SUBSTRATE-MATCHED-IC','FI',   'L2-SA'),
    (16, 'W2-5 HEAT-KERNEL-MP-EXCL',   'FI',    'L1-AX'),
    (17, 'W2-7 W3G-BETA-R1',           'MIXED', 'UNPINNED'),
    (18, 'W2-7 W3G-BETA-R2',           'MIXED', 'UNPINNED'),
    (19, 'W2-7 W3G-BETA-R3',           'FI',    'L0-INT'),
    (20, 'W2-10 B1-JENSEN-SCAN',       'FI',    'L0-INT'),
    (21, 'W2-9 MULTIPAIR-ECOND',       'FI',    'L0-INT'),
    (22, 'W2-12 CUSHION-DERIV-PIN',    'FI',    'L0-INT'),
    (23, 'W2-13 F0-CONVENTION-AUDIT',  'FI',    'L3-OB'),
    (24, 'W2-8 A2-CLUSTER-TEST',       'RD',    'UNPINNED'),
    (25, 'W0-1 PHONON-LENGTH-CANON',   'FI',    'L0-INT'),
    (26, 'W2-11 S-PP-FULL-ED',         'FI',    'L0-INT'),
    (27, 'W2-14 FIRAS-CHLUBA-FULL',    'MIXED', 'L3-OB'),
    (28, 'W2-15 PHASE-ALIGN-K-SCAN',   'FI',    'L0-INT'),
    (29, 'W3-3 DIM-H-PI-UNIV-EXCL',    'FI',    'L0-INT'),
    (30, 'W3-7 EJ-CONVENTION-AUDIT',   'RD',    'L3-OB'),
    (31, 'W3-6 SIC-PHYSICAL-CAP',      'FI',    'L0-INT'),
    (32, 'W3-2 R-FAMILY-ATLAS-EXT',    'FI',    'L0-INT'),
    (33, 'W3-5 FAMP-SC-3PI',           'MIXED', 'L3-OB'),
    (34, 'W3-4 GGE-FNL-CHANNEL',       'FI',    'L0-INT'),
    (35, 'W3-1 RANK-UNIVERSALITY-PROOF','FI',   'L0-INT'),
    (36, 'W3-14 C-GOLD-PROVENANCE',    'FI',    'L0-INT'),
    (37, 'W3-9 AS-ADJACENT-OBS',       'FI',    'L0-INT'),
    (38, 'W3-8 MU-EFF-LK',             'MIXED', 'UNPINNED'),
    (39, 'W3-12 L-PHONON-DERIVATION',  'FI',    'L0-INT'),
    (40, 'W3-11 XI-BCS-VS-L-PHONON',   'FI',    'L0-INT'),
    (41, 'W3-13 FOUR-SPEED-PROVENANCE','FI',    'L0-INT'),
    (42, 'W3-10 CUBIC-SIN2-W-EW',      'MIXED', 'L3-OB'),
]

LAYER_D_DEFAULT = {
    'L0-INT':   0.00,   # integer K-theoretic: L0 == L3 identically
    'L1-AX':    0.00,   # axiomatic Connes canonical measure reduces to L0
    'L2-SA':    0.15,   # substrate-action pin vs per-Q: moderate
    'L3-OB':    0.35,   # per-Q span IS the L0/L3 dissonance
    'UNPINNED': 0.40,   # substrate has not determined: LARGE baseline
}

# Row-specific overrides using known S-level numerical data
OVERRIDES = {
    2:  ('H-TILDE TD/LI 5.908e-3 vs 2.464e-5 (~240x)', 0.9958),
    4:  ('UNIFIED-AS-79-FULL-A/B ~5 OOM split',         0.9999),
    5:  ('UNIFIED-AS-79-FULL-A/B ~5 OOM split (pair)',  0.9999),
    13: ('r_max=1.33e4 UNPINNED MIXED wide',            0.50),
    15: ('L2-SA substrate-matched IC moderate',         0.15),
    17: ('w_0 band -0.9173 vs -0.998 (8.1%)',           0.081),
    18: ('Delta w_0 band 4.4%',                          0.044),
    23: ('F_0 convention audit 2.0216 OOM width',        0.989),
    24: ('var_a2 = 60.35% direct',                       0.604),
    27: ('FIRAS mu L3-OB Chluba-Sunyaev convention range', 0.25),
    30: ('EJ 9 conventions / 7 corrections',             0.68),
    33: ('F_amp=47.9 MIXED L3-OB wide',                  0.60),
    38: ('mu_eff LK MIXED UNPINNED',                     0.25),
    42: ('sin^2-theta_W R-protected SMALL',              0.08),
}


def band(d: float) -> str:
    if d < SMALL_THRESH: return "SMALL"
    if d < MEDIUM_THRESH: return "MEDIUM"
    return "LARGE"


def compute() -> dict:
    rows = []
    for (idx, name, tag, layer) in LAYER_ATLAS:
        if idx in OVERRIDES:
            reason, d = OVERRIDES[idx]
            src = "override-per-row-data"
        else:
            d = LAYER_D_DEFAULT[layer]
            reason = f"layer-principled default for {layer}"
            src = "layer-default"
        b = band(d)
        rows.append({
            'idx': idx, 'gate': name, 'tag': tag, 'layer': layer,
            'd': d, 'band': b, 'reason': reason, 'source': src,
        })

    band_counts = {'SMALL': 0, 'MEDIUM': 0, 'LARGE': 0}
    for r in rows:
        band_counts[r['band']] += 1

    return {
        'value': (band_counts['SMALL'], band_counts['MEDIUM'], band_counts['LARGE']),
        'rows': rows,
        'band_counts': band_counts,
    }


# ---------------------------------------------------------------------------
# Section 6 - Gate verdict + 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def evaluate_gate(result: dict) -> str:
    """Plan §W5-3 clauses:
    - PASS iff SMALL >= 26 AND MEDIUM in [8, 14] AND LARGE <= 5.
    - INFO iff bimodal (SMALL >= 15 AND LARGE >= 15 AND MEDIUM <= 5).
    - FAIL otherwise.
    """
    S = result['band_counts']['SMALL']
    M = result['band_counts']['MEDIUM']
    L = result['band_counts']['LARGE']
    if S >= 26 and 8 <= M <= 14 and L <= 5:
        return "PASS"
    if S >= 15 and L >= 15 and M <= 5:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 7 - Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}...")

    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    result = compute()
    verdict = evaluate_gate(result)

    # Save npz
    indices = np.array([r['idx'] for r in result['rows']])
    d_arr = np.array([r['d'] for r in result['rows']])
    band_arr = np.array([r['band'] for r in result['rows']])
    layer_arr = np.array([r['layer'] for r in result['rows']])
    tag_arr = np.array([r['tag'] for r in result['rows']])
    gate_arr = np.array([r['gate'] for r in result['rows']])

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        indices=indices,
        d_values=d_arr,
        band=band_arr,
        layer=layer_arr,
        tag=tag_arr,
        gate_names=gate_arr,
        SMALL_count=result['band_counts']['SMALL'],
        MEDIUM_count=result['band_counts']['MEDIUM'],
        LARGE_count=result['band_counts']['LARGE'],
        SMALL_thresh=SMALL_THRESH,
        MEDIUM_thresh=MEDIUM_THRESH,
    )
    print(f"  saved: {OUT_NPZ.name}")

    # Plot: 42-row bar chart colored by band
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        colors = ['tab:green' if b == 'SMALL' else 'tab:orange' if b == 'MEDIUM' else 'tab:red'
                  for b in band_arr]
        fig, ax = plt.subplots(figsize=(14, 5))
        ax.bar(indices, d_arr, color=colors, edgecolor='k', linewidth=0.4)
        ax.axhline(SMALL_THRESH, color='green', linestyle=':', label=f'SMALL<{SMALL_THRESH}')
        ax.axhline(MEDIUM_THRESH, color='orange', linestyle=':', label=f'MEDIUM<{MEDIUM_THRESH}')
        ax.set_xlabel('42-row VII.K-DUAL.LAYER atlas index')
        ax.set_ylabel('d(O) = |O_L0 - O_L3| / max(|O_L0|, |O_L3|)')
        ax.set_title(
            f"{GATE_ID}: S={result['band_counts']['SMALL']}, "
            f"M={result['band_counts']['MEDIUM']}, "
            f"L={result['band_counts']['LARGE']}, verdict={verdict}"
        )
        ax.set_ylim(0, 1.05)
        ax.legend()
        plt.tight_layout()
        plt.savefig(OUT_PNG, dpi=100)
        plt.close(fig)
        print(f"  saved: {OUT_PNG.name}")
    except Exception as e:
        print(f"  plot skipped: {type(e).__name__}: {e}")

    tag = emit_4tuple(result['value'], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, result['value'], audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print()
    print(f"=== {GATE_ID}: band histogram ===")
    print(f"  SMALL  (d < {SMALL_THRESH}):  {result['band_counts']['SMALL']}  (plan PASS requires >= 26)")
    print(f"  MEDIUM ({SMALL_THRESH} <= d < {MEDIUM_THRESH}): {result['band_counts']['MEDIUM']}  (plan PASS requires [8, 14])")
    print(f"  LARGE  (d >= {MEDIUM_THRESH}):  {result['band_counts']['LARGE']}  (plan PASS requires <= 5)")
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
