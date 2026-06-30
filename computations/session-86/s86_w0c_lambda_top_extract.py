#!/usr/bin/env python3
"""
S86 W0c-1 — S86-LAMBDA-TOP-DIRECT-EXTRACTION
============================================

Gate: S86-LAMBDA-TOP-DIRECT-EXTRACTION ([VERIFY])
Classification: GEOMETRIC

Pre-registered threshold (plan §W0c-1.9):
  PASS iff all 6 sub-criteria PASS (cache-integrity, count==155984,
  hermiticity, magnitude band [4.5,6.5]·M_KK, asymptotic-consistency
  L=10/L=12 ∈ [0.85,1.0], 6-sig-fig stability).
  FAIL iff any 1+ sub-criterion FAILs.
  INFO iff cache file ABSENT.

Inputs (S84+ dual-SHA):
  - computations/_shared/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz
  - computations/_shared/canonical_constants.py
  - script bytes (this file)

Output 4-tuple:
  (value=<lambda_max_to_6sigfig | sentinel>, scheme=spectral_cache_direct,
   convention=L_max=10_native, L_max=10)
"""
from __future__ import annotations

from canonical_constants import M_KK, c_fabric, J_C2  # noqa: F401

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
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S86"
GATE_ID = "S86-LAMBDA-TOP-DIRECT-EXTRACTION"
SCHEME = "spectral_cache_direct"
CONVENTION = "L_max=10_native"
L_MAX = 10  # (local) — pre-registered truncation level (plan §W0c-1.7)

CACHE_PATH = resolve_script(None, 'artifacts') / "s85_w12_elim1_D_K_Lmax_moments.npz"
DIAGNOSIS_PATH = resolve_output(86, 's86_w0c_1_failure_diagnosis.json')
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

INPUT_FILES = [
    CACHE_PATH,
    resolve_script(None, 'canonical_constants.py'),
]

# Pre-registered band parameters (plan §W0c-1.7)
EXPECTED_COUNT = 155984       # (local) — plan-asserted full L=10 multiplet count
MAGNITUDE_BAND_LO = 4.5       # (local) — plan-asserted lower band, × M_KK
MAGNITUDE_BAND_HI = 6.5       # (local) — plan-asserted upper band, × M_KK
ASYMPTOTIC_RATIO_LO = 0.85    # (local) — plan-asserted L=10/L=12 ratio LO
ASYMPTOTIC_RATIO_HI = 1.0     # (local) — plan-asserted L=10/L=12 ratio HI
HERMITICITY_TOL = 1e-10       # (local) — plan-asserted max(|imag|) tolerance


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()
    return audit, content


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def evaluate_six_subcriteria(cache_data, cache_sha: str) -> dict:
    """Run the 6 PASS sub-criteria from plan §W0c-1.6(f).

    Returns a dict with per-sub-criterion verdict + diagnostics.
    """
    results = {}  # (local)

    # Sub-criterion 1: cache-integrity (SHA self-pin: cache exists + readable)
    results["sub1_cache_integrity"] = {
        "verdict": "PASS" if cache_sha and len(cache_sha) == 64 else "FAIL",
        "cache_sha256": cache_sha,
        "note": "self-pin (no orchestrator-supplied SHA pin); PASS iff readable",
    }

    # Sub-criterion 2: count
    keys = list(cache_data.keys())  # (local)
    has_eigvals = "eigvals" in keys or "eigenvalues" in keys  # (local)
    if has_eigvals:
        eigval_key = "eigvals" if "eigvals" in keys else "eigenvalues"  # (local)
        eigvals = cache_data[eigval_key]  # (local)
        count = int(eigvals.shape[0])  # (local)
    else:
        # The cache stores per-L moment summaries, not raw eigenvalue arrays.
        eigvals = None
        n_eig_arr = cache_data.get("n_eigenvalues")  # (local)
        L_arr = cache_data.get("L_max")  # (local)
        if n_eig_arr is not None and L_arr is not None:
            try:
                idx = list(L_arr.tolist()).index(L_MAX)  # (local)
                count = int(n_eig_arr[idx])  # (local)
            except ValueError:
                count = -1  # (local) — sentinel: L=10 not in cache grid
        else:
            count = -1  # (local) — sentinel: cache lacks n_eigenvalues key

    results["sub2_count"] = {
        "verdict": "PASS" if count == EXPECTED_COUNT else "FAIL",
        "expected": EXPECTED_COUNT,
        "observed": count,
        "has_eigvals_array": has_eigvals,
        "available_keys": keys,
    }

    # Sub-criterion 3: hermiticity (requires eigval array)
    if has_eigvals:
        max_imag = float(np.max(np.abs(np.asarray(eigvals).imag)))  # (local)
        results["sub3_hermiticity"] = {
            "verdict": "PASS" if max_imag < HERMITICITY_TOL else "FAIL",
            "max_abs_imag": max_imag,
            "tolerance": HERMITICITY_TOL,
        }
    else:
        results["sub3_hermiticity"] = {
            "verdict": "FAIL",
            "reason": "cache has no raw eigenvalue array; hermiticity un-evaluable",
        }

    # Sub-criterion 4: magnitude band [4.5, 6.5] · M_KK
    if has_eigvals:
        eig_arr = np.asarray(eigvals)  # (local)
        lambda_max_abs = float(np.max(np.abs(eig_arr)))  # (local)
        ratio = lambda_max_abs / M_KK  # (local)
        in_band = (MAGNITUDE_BAND_LO <= ratio <= MAGNITUDE_BAND_HI)  # (local)
        results["sub4_magnitude"] = {
            "verdict": "PASS" if in_band else "FAIL",
            "lambda_max": lambda_max_abs,
            "ratio_to_M_KK": ratio,
            "band_lo": MAGNITUDE_BAND_LO,
            "band_hi": MAGNITUDE_BAND_HI,
        }
    else:
        results["sub4_magnitude"] = {
            "verdict": "FAIL",
            "reason": "no eigval array; lambda_max not extractable from moments alone",
        }

    # Sub-criterion 5: asymptotic-consistency L=10 vs L=12 (requires eigval arrays at both L)
    results["sub5_asymptotic"] = {
        "verdict": "FAIL",
        "reason": "cache holds moments not eigval arrays; cannot compute L=10/L=12 ratio",
    }

    # Sub-criterion 6: 6-sig-fig stability (re-load and compare)
    if has_eigvals:
        try:
            cache2 = np.load(CACHE_PATH, allow_pickle=True)  # (local)
            eig2 = np.asarray(cache2[eigval_key])  # (local)
            lambda_max_2 = float(np.max(np.abs(eig2)))  # (local)
            same = (
                f"{float(np.max(np.abs(eig_arr))):.5e}"
                == f"{lambda_max_2:.5e}"
            )  # (local)
            results["sub6_stability"] = {
                "verdict": "PASS" if same else "FAIL",
                "first_extraction": f"{float(np.max(np.abs(eig_arr))):.5e}",
                "second_extraction": f"{lambda_max_2:.5e}",
            }
        except Exception as e:
            results["sub6_stability"] = {
                "verdict": "FAIL",
                "reason": f"reload failed: {e}",
            }
    else:
        results["sub6_stability"] = {
            "verdict": "FAIL",
            "reason": "no eigval array to re-extract for stability check",
        }

    return results


def main() -> int:
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()
    canonical_path = resolve_script(None, 'canonical_constants.py')
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    if not CACHE_PATH.exists():
        print(f"Cache absent at {CACHE_PATH}")
        verdict = "INFO"
        value = "cache_absent"
        append_verdict(verdict, value, audit_sha, content_sha)
        print(f"\n=== {GATE_ID}: {verdict} ===")
        return 0

    cache_data = np.load(CACHE_PATH, allow_pickle=True)
    cache_sha = pins.get(
        str(CACHE_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/"), ""
    )

    results = evaluate_six_subcriteria(cache_data, cache_sha)

    # Print per-sub-criterion verdicts
    sub_verdicts = []  # (local)
    for k in ["sub1_cache_integrity", "sub2_count", "sub3_hermiticity",
              "sub4_magnitude", "sub5_asymptotic", "sub6_stability"]:
        v = results[k]["verdict"]
        sub_verdicts.append(v)
        print(f"  {k}: {v}")
        for kk, vv in results[k].items():
            if kk != "verdict":
                print(f"      {kk}: {vv}")

    all_pass = all(v == "PASS" for v in sub_verdicts)  # (local)
    verdict = "PASS" if all_pass else "FAIL"

    # Determine the value to report
    sub4 = results["sub4_magnitude"]  # (local)
    if "lambda_max" in sub4:
        value = f"{sub4['lambda_max']:.5e}"
    else:
        value = "no_eigvals_in_cache"

    if not all_pass:
        # Write failure diagnosis JSON per plan §W0c-1.6(h)
        diag = {
            "gate_id": GATE_ID,
            "verdict": verdict,
            "session": SESSION,
            "wave": "W0c",
            "L_max": L_MAX,
            "scheme": SCHEME,
            "convention": CONVENTION,
            "cache_path": str(CACHE_PATH.relative_to(PROJECT_ROOT)),
            "cache_sha256": cache_sha,
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
            "sub_criteria": results,
            "structural_note": (
                "Cache file is the moments-summary npz (a_2, a_4, R_JK, "
                "n_eigenvalues, K_base, ...) — it does NOT contain raw "
                "eigenvalue arrays. Sub-criteria 2-6 require raw eigvals; "
                "FAIL is structurally inevitable with this cache. "
                "Level-3 escalation: regenerate the L=10 D_K spectral cache "
                "with raw eigenvalues stored as `eigvals` key."
            ),
        }
        DIAGNOSIS_PATH.write_text(json.dumps(diag, indent=2), encoding="utf-8")
        print(f"\nFailure diagnosis written: {DIAGNOSIS_PATH.name}")

    # 4-tuple output
    print(
        f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, "
        f"L_max={L_MAX})"
    )

    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # math-scripts.md §Exit Codes: PASS/FAIL/INFO all exit 0


if __name__ == "__main__":
    sys.exit(main())
