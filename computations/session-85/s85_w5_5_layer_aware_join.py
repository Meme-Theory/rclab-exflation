#!/usr/bin/env python3
"""
S85 W5-5 S85-W5-5-LAYER-AWARE-LATTICE-JOIN - Functoriality of layer-projection
===============================================================================

Gate: S85-W5-5-LAYER-AWARE-LATTICE-JOIN  ([VERIFY])

Pre-registered threshold (plan §W5-5):
  PASS iff total violation count = 0 across 10 pairs x 4 layers = 40 checks.
  INFO iff violations >= 1 AND all violations involve the L2-SA fringe.
  FAIL iff >=1 non-L2-SA structural violation.

Classification: GEOMETRIC (categorical/lattice-theoretic test on regulator poset).

METHODOLOGY
-----------
W10-116 (S84) not formally landed; per plan "if W10-116 not landed, reconstruct
locally from the S83 three-layer synthesis". Reconstruction:

  - Regulator = (a_n support set, layer label). Atlas:
      zeta        : ({a_4},                    L1-AX)   S83 G3 EN3 axiomatic
      Zubarev     : ({a_4},                    L2-SA)   S83 W1-G1 substrate-action
      SDW         : ({a_4},                    L3-OB)   observable-layer
      cutoff_sqrt : ({a_0, a_2, a_4, a_6},     L3-OB)   observable-layer
      anomaly     : ({a_2, a_4},               L3-OB)   observable-layer
  - Regulator join r1 v r2 = regulator with support = support(r1) U support(r2).
    If union is in the atlas, use the atlas regulator's native layer (topmost
    if ties). If union not in atlas, fall back to layer-join = max-top of
    layer(r1), layer(r2).
  - Layer lattice: L0 = top, L3 = bottom. Layer join = closer to top (smaller rank).
  - Layer-projection Pi_L maps regulator to its native layer label.

Functoriality check: for each (pair, L), is
    [Pi_L(r1 v r2) == L] == [(Pi_L(r1) v Pi_L(r2)) == L] ?

Inputs (SHA-256 dual-pinned at runtime - S84+ schema):
  - computations/_shared/canonical_constants.py
  - sessions/permanent-results-registry.md (S83 three-layer synthesis source)

Output 4-tuple:
  (value=violation_count, scheme=layer-aware-lattice,
   convention=S83-three-layer-synthesis, L_max=3)
"""

from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403

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
import itertools
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W5-5-LAYER-AWARE-LATTICE-JOIN"                # (local)
SCHEME = "layer-aware-lattice"                                # (local)
CONVENTION = "S83-three-layer-synthesis"                      # (local)
L_MAX = 3                                                     # (local) canonical a_n truncation

OUT_NPZ = resolve_output(85, 's85_w5_5_layer_aware_join.npz')
OUT_PNG = resolve_output(85, 's85_w5_5_layer_aware_join.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')
CANON_PY = resolve_script(None, 'canonical_constants.py')
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
INPUT_FILES = [CANON_PY, REGISTRY_MD]


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try: h.update(path.read_bytes())
    except OSError: return ""
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

def closure_hash(pins):
    items = sorted(pins.items()); h = hashlib.sha256()
    for k, v in items: h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()

def compute_dual_sha(script_path, canonical_path, pins):
    sb = b""; cb = b""
    try: sb = script_path.read_bytes()
    except OSError: pass
    try: cb = canonical_path.read_bytes()
    except OSError: pass
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")
    ha = hashlib.sha256(); ha.update(sb); ha.update(cb); ha.update(pj)
    hc = hashlib.sha256(); hc.update(sb)
    return ha.hexdigest(), hc.hexdigest()


# W10-116 reconstruction: regulator atlas

REG_ATLAS = {
    'zeta':        (frozenset({'a_4'}),                            'L1-AX'),
    'Zubarev':     (frozenset({'a_4'}),                            'L2-SA'),
    'SDW':         (frozenset({'a_4'}),                            'L3-OB'),
    'cutoff_sqrt': (frozenset({'a_0', 'a_2', 'a_4', 'a_6'}),       'L3-OB'),
    'anomaly':     (frozenset({'a_2', 'a_4'}),                     'L3-OB'),
}
LAYER_RANK = {'L0-INT': 0, 'L1-AX': 1, 'L2-SA': 2, 'L3-OB': 3}
LAYERS_TESTED = ['L0-INT', 'L1-AX', 'L2-SA', 'L3-OB']


def layer_join(la: str, lb: str) -> str:
    """Top (smaller rank) is the join (less-refined)."""
    return la if LAYER_RANK[la] <= LAYER_RANK[lb] else lb


def regulator_join(r1: str, r2: str) -> tuple[frozenset, str]:
    """Reconstruction of W10-116 join: support union + atlas-native layer.

    If union support is present in the atlas, assign its layer (topmost candidate,
    preferring in-pair candidates). If union not in atlas, fall back to layer-join
    of the two regulators.
    """
    s1, l1 = REG_ATLAS[r1]
    s2, l2 = REG_ATLAS[r2]
    sup = s1 | s2
    candidates = [(name, lay) for name, (s, lay) in REG_ATLAS.items() if s == sup]
    if candidates:
        candidates.sort(key=lambda x: LAYER_RANK[x[1]])
        for name, lay in candidates:
            if name in (r1, r2):
                return (sup, lay)
        return (sup, candidates[0][1])
    return (sup, layer_join(l1, l2))


def compute() -> dict:
    pair_results = []
    violations = []
    for r1, r2 in itertools.combinations(REG_ATLAS.keys(), 2):
        jsup, jlayer_LHS = regulator_join(r1, r2)
        lay1 = REG_ATLAS[r1][1]
        lay2 = REG_ATLAS[r2][1]
        jlayer_RHS = layer_join(lay1, lay2)

        pair_violations = 0  # (local) per-pair counter
        for L in LAYERS_TESTED:
            lhs_eq = (jlayer_LHS == L)
            rhs_eq = (jlayer_RHS == L)
            if lhs_eq != rhs_eq:
                pair_violations += 1
                violations.append({
                    'pair': (r1, r2),
                    'layer': L,
                    'LHS': jlayer_LHS,
                    'RHS': jlayer_RHS,
                })
        pair_results.append({
            'pair': (r1, r2),
            'LHS_layer': jlayer_LHS,
            'RHS_layer': jlayer_RHS,
            'violations': pair_violations,
        })

    total_violations = sum(p['violations'] for p in pair_results)
    all_involve_L2 = all(
        v['LHS'] == 'L2-SA' or v['RHS'] == 'L2-SA' for v in violations
    ) if violations else True

    return {
        'value': total_violations,
        'pair_results': pair_results,
        'violations': violations,
        'total_violations': total_violations,
        'all_involve_L2': all_involve_L2,
    }


def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")

def append_verdict(verdict, value, audit, content):
    line = (f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
            f"convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit} content_sha256={content} "
            f"schema_version=S84+\n")
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)

def evaluate_gate(result):
    if result['total_violations'] == 0:
        return "PASS"
    if result['all_involve_L2']:
        return "INFO"
    return "FAIL"


def main() -> int:
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")
    audit, content = compute_dual_sha(Path(__file__).resolve(), CANON_PY, pins)
    print(f"  audit_sha256:   {audit[:16]}...")
    print(f"  content_sha256: {content[:16]}...")
    print()

    result = compute()
    verdict = evaluate_gate(result)

    # Persist
    pair_names = [",".join(p['pair']) for p in result['pair_results']]
    lhs_layers = [p['LHS_layer'] for p in result['pair_results']]
    rhs_layers = [p['RHS_layer'] for p in result['pair_results']]
    pair_viol = [p['violations'] for p in result['pair_results']]
    viol_table = np.array(
        [[v['pair'][0], v['pair'][1], v['layer'], v['LHS'], v['RHS']] for v in result['violations']],
        dtype=object,
    ) if result['violations'] else np.array([['NONE'] * 5], dtype=object)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        pair_names=np.array(pair_names),
        LHS_layers=np.array(lhs_layers),
        RHS_layers=np.array(rhs_layers),
        pair_violations=np.array(pair_viol),
        total_violations=result['total_violations'],
        all_involve_L2=result['all_involve_L2'],
        violation_table=viol_table,
    )
    print(f"  saved: {OUT_NPZ.name}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(12, 5))
        x = range(len(pair_names))
        colors = ['tab:green' if v == 0 else 'tab:red' for v in pair_viol]
        ax.bar(x, pair_viol, color=colors, edgecolor='k')
        ax.set_xticks(list(x))
        ax.set_xticklabels(pair_names, rotation=45, ha='right')
        ax.set_ylabel('violations (out of 4 layer-checks per pair)')
        ax.set_ylim(0, 4.5)
        ax.set_title(f"{GATE_ID}: total={result['total_violations']}/40, verdict={verdict}")
        ax.grid(True, axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(OUT_PNG, dpi=100)
        plt.close(fig)
        print(f"  saved: {OUT_PNG.name}")
    except Exception as e:
        print(f"  plot skipped: {type(e).__name__}: {e}")

    tag = emit_4tuple(result['total_violations'], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, result['total_violations'], audit, content)

    wall = time.time() - t0
    print()
    print(f"=== {GATE_ID} 10-pair functoriality results ===")
    for p in result['pair_results']:
        r1, r2 = p['pair']
        print(f"  ({r1:12s}, {r2:12s})  LHS={p['LHS_layer']:6s}  RHS={p['RHS_layer']:6s}  viol={p['violations']}/4")
    print(f"  total violations: {result['total_violations']}/40")
    print(f"  all_involve_L2: {result['all_involve_L2']}")
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
