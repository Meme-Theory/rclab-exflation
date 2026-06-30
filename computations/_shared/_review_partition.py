#!/usr/bin/env python3
"""
Review Partitioner — splits narrow_live_set into 7 topic clusters.

Reads _canonical_audit_report.json; classifies each narrow-set script
by topic keyword on basename + docstring; writes per-cluster list to
_review_partition.json.

Clusters (mapped to physics-domain agents per the script-review plan):
  spectral   -> lizzi-spectral-functional-theorist
  bcs        -> landau-condensed-matter-theorist
  ncg        -> connes-ncg-theorist
  kk         -> baptista-spacetime-analyst
  transit    -> transit-dynamics-theorist
  cosmo      -> mack-cosmic-bridge
  generalist -> gen-physicist
"""

from __future__ import annotations

# Imports required for discipline; unused at module scope (audit script).
from canonical_constants import *  # noqa: F401,F403

import json
import re
from collections import Counter
from pathlib import Path
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


PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'COMPUTATIONS_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
REPORT_JSON = resolve_script(None, '_canonical_audit_report.json')
OUT_JSON = resolve_script(None, '_review_partition.json')

# Topic keywords matched against basename (preferred) + docstring fallback.
# First-match wins; order matters for disambiguation.
CLUSTER_RULES: list[tuple[str, list[str]]] = [
    ("spectral", [
        "spectral", "heat_kernel", "seeley", "gilkey", "zeta",
        "sdw_", "_sdw", "a_2", "a_4", "a2_", "a4_",
        "chamseddine", "lizzi", "dilaton",
    ]),
    ("bcs", [
        "bcs", "leggett", "gap_", "_gap", "hfb", "bogoliubov",
        "pairing", "josephson", "pomeran", "condensate",
        "pair_susc", "superfluid", "coop_",
    ]),
    ("ncg", [
        "ncg", "connes", "pfaffian", "block_diag", "kasparov",
        "kosmann", "grading", "chirality", "gamma9", "axiom",
        "almost_commutative", "inner_fluct",
    ]),
    ("kk", [
        "kk_", "_kk", "fiber", "jensen", "fold", "coset",
        "petrov", "baptista", "weyl", "ricci", "scalar_curv",
        "sasaki", "aloff_wallach", "kerner", "dphys",
    ]),
    ("transit", [
        "transit", "mode_eqn", "parker", "beta_", "_beta",
        "kz_", "kibble", "relic", "reheat", "gge",
        "bogoliubov_amp", "preheat", "instanton",
        "mach", "fold_dyn",
    ]),
    ("cosmo", [
        "ns_", "_ns_", "n_s_", "cmb", "desi", "pbh",
        "tensor", "hubble", "lcdm", "planck_2018", "omega_",
        "a_s_", "amp_", "h0_", "backreact",
        "bao", "lss", "dark_energy", "w_a",
    ]),
]


def classify_script(name: str, docstring: str = "") -> str:
    """Return cluster key for a script basename."""
    lower = name.lower()
    for cluster, keywords in CLUSTER_RULES:
        for kw in keywords:
            if kw in lower:
                return cluster
    # Fallback: scan docstring if available
    if docstring:
        dlower = docstring.lower()
        for cluster, keywords in CLUSTER_RULES:
            for kw in keywords:
                if kw in dlower:
                    return cluster
    return "generalist"


def extract_docstring_first_line(script_path: Path) -> str:
    """Quick read of the first triple-quoted block's first line (for tie-break)."""
    try:
        text = script_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    m = re.search(r'"""(.*?)"""', text, re.DOTALL)
    if not m:
        m = re.search(r"'''(.*?)'''", text, re.DOTALL)
    if not m:
        return ""
    body = m.group(1).strip()
    return body.splitlines()[0] if body else ""


def main() -> int:
    print(f"Reading {REPORT_JSON.name} ...")
    data = json.loads(REPORT_JSON.read_text(encoding="utf-8"))
    narrow = data.get("narrow_live_set", [])
    print(f"  narrow_live_set entries: {len(narrow)}")

    clusters: dict[str, list[dict]] = {
        k: [] for k in ("spectral", "bcs", "ncg", "kk", "transit", "cosmo", "generalist")
    }

    for r in narrow:
        name = r["name"]
        script_path = PROJECT_ROOT / r["path"]
        docstring = extract_docstring_first_line(script_path) if script_path.exists() else ""
        cluster = classify_script(name, docstring)
        r_copy = dict(r)
        r_copy["cluster"] = cluster
        r_copy["docstring_first_line"] = docstring[:160]
        clusters[cluster].append(r_copy)

    # Sort within each cluster by priority_review desc
    for cluster in clusters:
        clusters[cluster].sort(key=lambda x: (-x.get("priority_review", 0), x["name"]))

    # Summary
    print("\n=== Cluster sizes ===")
    total = 0  # (local)
    for cluster, items in clusters.items():
        print(f"  {cluster:12s}: {len(items):4d}")
        total += len(items)
    print(f"  {'TOTAL':12s}: {total:4d}")

    # Grade roll-up per cluster
    print("\n=== Grade per cluster ===")
    for cluster, items in clusters.items():
        grades = Counter(x.get("grade", "?") for x in items)
        grade_str = " | ".join(f"{g}:{n}" for g, n in grades.most_common())
        print(f"  {cluster:12s}: {grade_str}")

    # Agent mapping
    agent_map = {
        "spectral": "lizzi-spectral-functional-theorist",
        "bcs": "landau-condensed-matter-theorist",
        "ncg": "connes-ncg-theorist",
        "kk": "baptista-spacetime-analyst",
        "transit": "transit-dynamics-theorist",
        "cosmo": "mack-cosmic-bridge",
        "generalist": "gen-physicist",
    }

    out = {
        "source": "_canonical_audit_report.json",
        "total": total,
        "agent_map": agent_map,
        "clusters": clusters,
    }
    OUT_JSON.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"\nWrote {OUT_JSON.name} ({OUT_JSON.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
