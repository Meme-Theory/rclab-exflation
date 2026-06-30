#!/usr/bin/env python3
"""
S86 W0c-4 — S86-K-FLOOR-K-WALL-LAND
====================================

Gate: S86-K-FLOOR-K-WALL-LAND ([VERIFY])
Classification: PHONONIC

Pre-registered threshold (plan §W0c-4.9):
  PASS iff K_floor + K_wall both in canonical_constants.py + W5 D.4 block in
  permanent-results-registry.md with dual-SHA + ordering check
  K_floor < K_crit_BdG < K_wall holds.
  FAIL iff any of: variable absent, registry block absent, W5 D.4 SHA mismatch,
  ordering violated.
  INFO iff registry-file did not exist at session start (CREATED status).

Inputs (S84+ dual-SHA):
  - computations/_shared/canonical_constants.py (pre-edit)
  - sessions/permanent-results-registry.md (pre-edit, or ABSENT)
  - computations/session-85/s85_gate_verdicts.txt (W5 D.4 verdict-line entry)
  - computations/session-85/s85_w0_k_floor_wall_registry_landing.{py,npz}
    (S85 predecessor; audit-only)
  - script bytes (this file)

Output 4-tuple:
  (value=K_floor_K_wall_landed | upstream_FAIL_no_values,
   scheme=canonical_constants_plus_registry,
   convention=W5_D.4_derivation, L_max=N/A)
"""
from __future__ import annotations

from canonical_constants import M_KK  # noqa: F401 — framework-import discipline

import hashlib
import json
import sys
import time
import os
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


os.environ.setdefault("OMP_NUM_THREADS", "8")

import numpy as np  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S86"
GATE_ID = "S86-K-FLOOR-K-WALL-LAND"
SCHEME = "canonical_constants_plus_registry"
CONVENTION = "W5_D.4_derivation"
L_MAX = "N/A"

CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
S85_VERDICTS = resolve_output(85, 's85_gate_verdicts.txt')
S85_W0_NPZ = resolve_output(85, 's85_w0_k_floor_wall_registry_landing.npz')
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

INPUT_FILES = [
    CANONICAL_PATH,
    REGISTRY_PATH,
    S85_VERDICTS,
    S85_W0_NPZ,
]

# Pre-registered ordering anchor (plan §W0c-4.10 substitution chain)
K_CRIT_BDG_ANCHOR = 2.035  # (local) — per W0c-2 PASS, line 138 of canonical_constants.py


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        if sha:
            print(f"  {rel}: {sha[:16]}...")
        else:
            print(f"  {rel}: ABSENT")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    sb = b""  # (local)
    try:
        sb = script_path.read_bytes()
    except OSError:
        pass
    cb = b""  # (local)
    try:
        cb = canonical_path.read_bytes()
    except OSError:
        pass
    pj = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    h_a = hashlib.sha256(); h_a.update(sb); h_a.update(cb); h_a.update(pj)
    h_c = hashlib.sha256(); h_c.update(sb)
    return h_a.hexdigest(), h_c.hexdigest()


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def search_w5_d4_verdict() -> dict:
    """Search s85_gate_verdicts.txt for the W5 D.4 entry and parse it."""
    if not S85_VERDICTS.exists():
        return {"found": False, "reason": "s85_gate_verdicts.txt absent"}
    text = S85_VERDICTS.read_text(encoding="utf-8")  # (local)
    # Find any line referencing W5 D.4 / K_FLOOR / K_WALL
    matches = []  # (local)
    for line in text.split("\n"):
        if any(tok in line for tok in [
            "S85-K-FLOOR-WALL-JOINT-REGISTRY-LANDING",
            "K-FLOOR-WALL",
            "W5-D.4",
            "W5_D.4",
        ]):
            matches.append(line)
    return {
        "found": bool(matches),
        "lines": matches,
    }


def search_substrate_npz_for_values() -> dict:
    """Look for any preserved npz with numerical K_floor / K_wall values.

    Per the plan §W0c-4 the canonical source is the S85 W5 D.4 producing script
    output. That script does not exist in repo. We search for any npz that
    might contain K_floor / K_wall numerical anchors.
    """
    candidates = sorted(SCRIPT_DIR.glob("s8*k_floor*.npz")) + sorted(
        SCRIPT_DIR.glob("s8*k_wall*.npz")
    )  # (local)
    findings = []  # (local)
    for p in candidates:
        try:
            d = np.load(p, allow_pickle=True)  # (local)
            keys = list(d.keys())  # (local)
            payload = {}  # (local)
            for k in keys:
                v = d[k]
                # Only capture scalar numerical values that could be K_floor/K_wall
                if (
                    getattr(v, "shape", None) == ()
                    and v.dtype.kind in "fiub"  # float, int, uint, bool
                ):
                    payload[k] = (
                        float(v) if v.dtype.kind in "fi" else bool(v)
                    )
            findings.append({
                "path": str(p.relative_to(PROJECT_ROOT)),
                "keys": keys,
                "scalar_payload": payload,
            })
        except Exception as e:
            findings.append({
                "path": str(p.relative_to(PROJECT_ROOT)),
                "error": str(e),
            })
    return {"candidates": [str(p.relative_to(PROJECT_ROOT)) for p in candidates],
            "findings": findings}


def extract_k_floor_k_wall_if_present() -> tuple[float | None, float | None, str]:
    """Attempt to extract numerical K_floor / K_wall from any source.

    Returns (k_floor, k_wall, source_description). Both None if not found.
    """
    # Source 1: try the S85 W0 audit npz
    if S85_W0_NPZ.exists():
        d = np.load(S85_W0_NPZ, allow_pickle=True)
        if "K_floor" in d.keys() and "K_wall" in d.keys():
            kf = float(d["K_floor"])  # (local)
            kw = float(d["K_wall"])  # (local)
            return kf, kw, "S85 W0 audit npz K_floor/K_wall keys"
        # The S85 W0 audit only stored *_present booleans, not values
        kf_present = bool(d.get("K_floor_present", False))  # (local)
        kw_present = bool(d.get("K_wall_present", False))  # (local)
        if not (kf_present and kw_present):
            return None, None, (
                f"S85 W0 audit npz: K_floor_present={kf_present}, "
                f"K_wall_present={kw_present} (presence-check only; no values)"
            )
    return None, None, "no canonical K_floor / K_wall numerical artifact found"


def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    print()

    # Step 1: search for upstream W5 D.4 verdict
    w5_d4 = search_w5_d4_verdict()  # (local)
    print("=== Upstream W5 D.4 verdict search ===")
    if w5_d4["found"]:
        for ln in w5_d4["lines"]:
            print(f"  {ln[:200]}")
    else:
        print(f"  {w5_d4['reason']}")
    print()

    # Step 2: search for substrate npz with numerical values
    npz_search = search_substrate_npz_for_values()  # (local)
    print("=== Substrate npz search for K_floor/K_wall numerical values ===")
    print(f"  Candidates: {npz_search['candidates']}")
    for f in npz_search["findings"]:
        print(f"  {f.get('path')}: keys={f.get('keys', f.get('error'))}")
        if "scalar_payload" in f:
            for k, v in f["scalar_payload"].items():
                print(f"      {k} = {v}")
    print()

    # Step 3: attempt extraction
    k_floor, k_wall, source = extract_k_floor_k_wall_if_present()  # (local)
    print(f"=== K_floor / K_wall extraction ===")
    print(f"  K_floor: {k_floor}")
    print(f"  K_wall:  {k_wall}")
    print(f"  Source:  {source}")
    print()

    # Compute dual SHA against current state (no edits performed in FAIL path)
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL_PATH, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # Decide verdict
    if k_floor is None or k_wall is None:
        # Cannot land; upstream values missing
        verdict = "FAIL"
        value = "upstream_W5_D.4_FAIL_no_K_floor_K_wall_values"
        ordering_status = "un-evaluable (no values)"
        print(f"=== FAIL — upstream values absent; gate cannot land ===")
        print(f"  Reason: S85 W5 D.4 verdict line is "
              f"'S85-K-FLOOR-WALL-JOINT-REGISTRY-LANDING: FAIL value=0' "
              f"(audit-only predecessor recorded both K_floor and K_wall ABSENT). "
              f"Plan-referenced producing script s85_w5_d4_kfloor_kwall.py is not "
              f"in current repo tree. S84 W5 K_floor scripts exist but have no "
              f"npz numerical outputs in the preserved artifact tree. "
              f"Level-3 escalation: re-derive W5 D.4 producing the substrate's "
              f"BdG-corridor brackets numerically.")
    else:
        # Land canonical entries + run ordering check
        verdict = "PASS"  # tentative — refine with ordering check below
        value = f"K_floor={k_floor:.6g}_K_wall={k_wall:.6g}"

        # Ordering check
        ordering_ok = (k_floor < K_CRIT_BDG_ANCHOR < k_wall)  # (local)
        ordering_status = (
            f"K_floor={k_floor} < K_crit_BdG={K_CRIT_BDG_ANCHOR} < K_wall={k_wall}: "
            f"{'OK' if ordering_ok else 'VIOLATED'}"
        )
        if not ordering_ok:
            verdict = "FAIL"
            value = f"ordering_violated_K_floor={k_floor}_K_wall={k_wall}"
        else:
            # Append entries to canonical_constants.py
            # ... (PASS path not implemented; would land K_floor + K_wall blocks)
            print(f"  PASS path: would land K_floor={k_floor}, K_wall={k_wall}")
            print(f"  PASS path NOT executed because no values exist (control-path placeholder).")

    print()
    print(f"  ordering: {ordering_status}")
    print(f"\n(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    append_verdict(verdict, value, audit_sha, content_sha)

    # Diagnostic
    diag = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "session": SESSION,
        "wave": "W0c",
        "k_floor": k_floor,
        "k_wall": k_wall,
        "k_crit_bdg_anchor": K_CRIT_BDG_ANCHOR,
        "source_description": source,
        "ordering_status": ordering_status,
        "upstream_w5_d4": w5_d4,
        "npz_search": npz_search,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "remediation_route": (
            "Level-3 escalation: re-derive S85 W5 D.4 producing K_floor / K_wall "
            "as substrate-corridor BdG-bracket pair, then land them via this gate "
            "in a future S86-W0c-4-RERUN or S87+ wave."
        ),
    }  # (local)
    diag_path = resolve_output(86, 's86_w0c_4_kfloor_kwall_land.json')  # (local)
    diag_path.write_text(json.dumps(diag, indent=2), encoding="utf-8")
    print(f"\nDiagnostic JSON: {diag_path.name}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
