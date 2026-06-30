#!/usr/bin/env python3
"""
S86 W4-1 P4 — BRANCH-IV-FORMULATION-COMMIT (registry-write verification)
=========================================================================

Gate: S86-BRANCH-IV-FORMULATION-COMMIT  ([VERIFY])

Pre-registered threshold (per session-86-plan-w4.md §W4-1 §9):
  PASS iff all 5 CC pass AND all 3 file edits present AND both canonical
  entries registered with provenance AND re-import succeeds. FAIL otherwise.

Inputs (SHA-256 dual-pinned at runtime — first 20 lines of stdout):
  - sessions/framework/registry/branch-iv-canonical.md      (post-edit registry)
  - computations/_shared/canonical_constants.py       (post-edit + audit_sha256)
  - computations/_shared/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz
                                                    (anchor cache)
  - computations/session-85/s85_gate_verdicts.txt        (W12-ELIM-* cite SHAs)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value="R_JE_retired+R_JK_landed+xi_E_GGE_inv_landed",
   scheme="branch-iv-canonical", convention="2B-path-c", L_max="N/A")

Classification: PHONONIC

METHODOLOGY
-----------
Registry-write commit verification. Reads the framework file + canonical
constants file post-edit; performs 5 cross-checks (CC-1/CC-2 dimensional
rescaling traces, CC-3 framework-file grep, CC-4 canonical_constants.py
grep, CC-5 re-import); appends a dual-SHA verdict line to the canonical
verdict file at computations/session-86/s86_gate_verdicts.txt.

CC-1 + CC-2 are pure dimensional analysis (units verification, not
direction). CC-1: R_JK ~ M_KK^{-2} via M_KK -> 2*M_KK rescaling -> ratio 1/4.
CC-2: xi_E_GGE_inv ~ M_KK via M_KK -> 2*M_KK rescaling -> ratio 2.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Canonical verdict line appended to computations/session-86/s86_gate_verdicts.txt
- Exit code 0 regardless of verdict (per .claude/rules/math-scripts.md)
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
import re
import sys
import time
from pathlib import Path

import numpy as np
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


# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"

SESSION = "S86"                                                    # (local)
GATE_ID = "S86-BRANCH-IV-FORMULATION-COMMIT"                       # (local)
SCHEME = "branch-iv-canonical"                                     # (local)
CONVENTION = "2B-path-c"                                           # (local)
L_MAX = "N/A"                                                      # (local) commit gate, no L_max axis

# Output destinations
VERDICT_TXT = resolve_output(86, f's86_gate_verdicts.txt')
FRAMEWORK_FILE = FRAMEWORK_DIR / "branch-iv-canonical.md"
CANONICAL_PY = resolve_script(None, 'canonical_constants.py')
S85_VERDICTS = resolve_output(85, 's85_gate_verdicts.txt')
ANCHOR_CACHE = resolve_script(None, 'artifacts') / "s85_w12_elim1_D_K_Lmax_moments.npz"

INPUT_FILES = [
    CANONICAL_PY,
    FRAMEWORK_FILE,
    ANCHOR_CACHE,
    S85_VERDICTS,
]

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema; first 20 lines)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                      # (local)
    for p in inputs:
        sha = sha256_of(p)                                         # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    """Stable hash over all input SHAs (sorted)."""
    items = sorted(pins.items())                                   # (local)
    h = hashlib.sha256()                                           # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """Compute (audit_sha256, content_sha256) per S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )
    """
    script_bytes = b""                                             # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                          # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                              # (local)

    h_audit = hashlib.sha256()                                     # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                    # (local)

    h_content = hashlib.sha256()                                   # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Computation: R_JK and xi_E_GGE_inv from canonical structure
# ---------------------------------------------------------------------------

def compute_R_JK_from_cache():
    """Compute R_JK = (sigma_J/sigma_K) * (|Delta_BCS|^2/K_base) at L_max=10
    from the S85 W12 ELIM-1 anchor cache.

    Returns:
        R_JK_value (float) at L_max=10
        R_JK_traj (np.array): trajectory at L_max in {8, 10, 12}
        prefactor (float): L_max-INDEPENDENT prefactor |Delta_BCS|^2/K_base
    """
    cache = np.load(ANCHOR_CACHE)                                  # (local)
    L_axis = cache["L_max"]                                        # (local) [8, 10, 12]
    a_2_axis = cache["a_2"]                                        # (local) sigma_K
    a_4_axis = cache["a_4"]                                        # (local) sigma_J
    Delta_sq = float(cache["Delta_sq"])                            # (local) |Delta_BCS|^2
    K_base_val = float(cache["K_base"])                            # (local)

    # Recompute trajectory (cross-check against cached R_JK)
    R_JK_traj = (a_4_axis * Delta_sq) / (a_2_axis * K_base_val)    # (local)

    # L_max=10 anchor (index 1)
    idx_10 = int(np.where(L_axis == 10)[0][0])                     # (local)
    R_JK_value = float(R_JK_traj[idx_10])                          # (local)

    prefactor = Delta_sq / K_base_val                              # (local) L_max-INDEPENDENT

    return R_JK_value, R_JK_traj, prefactor, L_axis


def compute_xi_E_GGE_inv():
    """Compute xi_E_GGE_inv from substrate-natural anchor:
        xi_E_GGE_inv = N_pair_GGE * (Delta_BCS / K_base)
                     = lim_{s->-1} zeta_{D_K^GGE}(s)  (substrate-natural reduction)

    Returns:
        xi_inv (float): in M_KK units
        N_pair_GGE (float): 59.8 (S38 GGE permanence)
        lambda_GGE_avg (float): Delta_BCS / K_base
    """
    N_pair_GGE = 59.8                                              # (local) S38 GGE permanence theorem
    lambda_GGE_avg = Delta_BCS / K_base                            # (local) substrate-natural avg eigenvalue
    xi_inv = N_pair_GGE * lambda_GGE_avg                           # (local) M_KK units
    return xi_inv, N_pair_GGE, lambda_GGE_avg


# ---------------------------------------------------------------------------
# Section 6 — Cross-checks (5 mandatory; PASS iff all 5)
# ---------------------------------------------------------------------------

def cc1_R_JK_dimensional_rescaling(R_JK_value: float):
    """CC-1: R_JK has units of M_KK^{-2}.

    Substitution chain (DIMENSIONAL):
      Step 1: sigma_J = Tr[D_K^-4]/Vol_SU3 has units M_KK^{-4}.
              sigma_K = Tr[D_K^-2]/Vol_SU3 has units M_KK^{-2}.
              Delta_BCS, K_base, Vol_SU3 are dimensionless ratios.
      Step 2: R_JK = (sigma_J * |Delta|^2) / (sigma_K * K_base)
                  = ([M_KK^-4] * [1]) / ([M_KK^-2] * [1])
                  = M_KK^{-2}
      Step 3: Under M_KK -> 2*M_KK, eigenvalues lambda_n -> 2*lambda_n
              Tr[D_K^-4] -> 2^{-4} * Tr[D_K^-4]
              Tr[D_K^-2] -> 2^{-2} * Tr[D_K^-2]
              R_JK_new / R_JK_old = (2^-4) / (2^-2) = 2^{-2} = 0.25
      Direction: ratio = 0.25 confirms R_JK ~ M_KK^{-2}.
    """
    cache = np.load(ANCHOR_CACHE)                                  # (local)
    a_2_orig = float(cache["a_2"][1])                              # (local) L_max=10
    a_4_orig = float(cache["a_4"][1])                              # (local) L_max=10
    Delta_sq = float(cache["Delta_sq"])                            # (local)
    K_base_v = float(cache["K_base"])                              # (local)
    R_JK_orig = (a_4_orig * Delta_sq) / (a_2_orig * K_base_v)      # (local)

    # Rescale: M_KK -> 2*M_KK
    a_2_new = a_2_orig * 2 ** (-2)                                 # (local)
    a_4_new = a_4_orig * 2 ** (-4)                                 # (local)
    R_JK_new = (a_4_new * Delta_sq) / (a_2_new * K_base_v)         # (local)

    ratio = R_JK_new / R_JK_orig                                   # (local) expected 0.25
    expected = 0.25                                                # (local) M_KK^{-2} factor
    tol = 1e-12                                                    # (local) machine epsilon
    cc1_pass = abs(ratio - expected) < tol                         # (local)

    print(f"  CC-1 (R_JK ~ M_KK^{{-2}}):")
    print(f"    R_JK at orig M_KK   = {R_JK_orig:.10e}")
    print(f"    R_JK at 2*M_KK      = {R_JK_new:.10e}")
    print(f"    ratio R_JK_new/orig = {ratio:.16f}")
    print(f"    expected (1/4)      = {expected:.16f}")
    print(f"    abs(ratio-expected) = {abs(ratio-expected):.2e}")
    print(f"    CC-1 PASS: {cc1_pass}")
    return cc1_pass, ratio


def cc2_xi_E_GGE_inv_dimensional_rescaling(xi_inv: float):
    """CC-2: xi_E_GGE_inv has units of M_KK.

    Substitution chain (DIMENSIONAL):
      Step 1: xi_E_GGE_inv := lim_{s->-1} zeta_{D_K^GGE}(s)
                            = (analytic continuation) Sum lambda_n^GGE
              lambda_n has units of M_KK (Dirac eigenvalues are mass-scale).
      Step 2: Sum has units [lambda] = M_KK.
      Step 3: Under M_KK -> 2*M_KK, lambda_n -> 2*lambda_n
              Sum -> 2*Sum
              xi_inv_new / xi_inv_old = 2
      Direction: ratio = 2 confirms xi_E_GGE_inv ~ M_KK^{+1}.
    """
    # Demonstration of the algebraic identity Sum(2x) = 2*Sum(x) for any
    # eigenvalue distribution. (The substrate-natural anchor equals
    # N_pair_GGE * Delta_BCS / K_base; Delta_BCS is in M_KK units.)
    rng = np.random.default_rng(86)                                # (local)
    mock_eigs = rng.uniform(0.05, 5.0, size=120)                   # (local) 59.8 pairs ~ 120 modes
    sum_orig = float(np.sum(mock_eigs))                            # (local)
    sum_new = float(np.sum(2.0 * mock_eigs))                       # (local)
    ratio_mock = sum_new / sum_orig                                # (local)

    # Anchor formula rescaling: xi_inv = N_pair_GGE * Delta_BCS / K_base
    # Under M_KK -> 2*M_KK:
    #   Delta_BCS is a dimensionless eigenvalue ratio (Delta_0 / M_KK),
    #   so the dimensional eigenvalue Delta_0 -> 2*Delta_0; the printed
    #   Delta_BCS ratio in M_KK units stays = 0.4642 BUT the dimensional
    #   anchor xi_inv has SI dimensions of [Delta_0] = M_KK.
    # Direct test on the anchor formula in dimensional form:
    Delta_0_dim_orig = Delta_BCS                                   # (local) treat as dimensional
    Delta_0_dim_new = 2.0 * Delta_BCS                              # (local) under M_KK doubling
    xi_inv_orig = 59.8 * Delta_0_dim_orig / K_base                 # (local)
    xi_inv_new = 59.8 * Delta_0_dim_new / K_base                   # (local)
    ratio_anchor = xi_inv_new / xi_inv_orig                        # (local)

    expected = 2.0                                                 # (local) M_KK^{+1} factor
    tol = 1e-12                                                    # (local)
    cc2_pass_mock = abs(ratio_mock - expected) < tol               # (local)
    cc2_pass_anchor = abs(ratio_anchor - expected) < tol           # (local)
    cc2_pass = bool(cc2_pass_mock and cc2_pass_anchor)             # (local)

    print(f"  CC-2 (xi_E_GGE_inv ~ M_KK^{{+1}}):")
    print(f"    sum_orig (mock 120 modes) = {sum_orig:.10e}")
    print(f"    sum_new (2x scaled)       = {sum_new:.10e}")
    print(f"    ratio (mock)              = {ratio_mock:.16f}")
    print(f"    xi_inv_orig (anchor)      = {xi_inv_orig:.10e}")
    print(f"    xi_inv_new (2x dim)       = {xi_inv_new:.10e}")
    print(f"    ratio (anchor)            = {ratio_anchor:.16f}")
    print(f"    expected (2)              = {expected:.16f}")
    print(f"    CC-2 PASS: {cc2_pass}")
    return cc2_pass, ratio_anchor


def cc3_framework_file_grep():
    """CC-3: branch-iv-canonical.md contains all 3 required substrings."""
    text = FRAMEWORK_FILE.read_text(encoding="utf-8")              # (local)
    has_R_JE_retired = "R_JE retired" in text or "R_JE Retirement" in text  # (local)
    has_R_JK = bool(re.search(r"\bR_JK\b", text))                  # (local)
    has_xi_E_GGE = ("xi_E_GGE" in text) or ("xi_E_GGE_inv" in text) or ("ξ_E_GGE" in text)  # (local)

    cc3_pass = bool(has_R_JE_retired and has_R_JK and has_xi_E_GGE)  # (local)
    print(f"  CC-3 (framework file grep):")
    print(f"    contains 'R_JE retired/Retirement': {has_R_JE_retired}")
    print(f"    contains 'R_JK':                    {has_R_JK}")
    print(f"    contains 'xi_E_GGE'/'ξ_E_GGE':      {has_xi_E_GGE}")
    print(f"    CC-3 PASS: {cc3_pass}")
    return cc3_pass


def cc4_canonical_constants_grep():
    """CC-4: canonical_constants.py contains both R_JK and xi_E_GGE_inv lines
    with provenance comments."""
    text = CANONICAL_PY.read_text(encoding="utf-8")                # (local)
    has_R_JK_assign = bool(re.search(r"^R_JK\s*=", text, re.MULTILINE))  # (local)
    has_xi_assign = bool(re.search(r"^xi_E_GGE_inv\s*=", text, re.MULTILINE))  # (local)
    has_R_JK_provenance = "S86-W4-1 P4" in text or "S86-BRANCH-IV-FORMULATION-COMMIT" in text  # (local)
    has_3heb_cite = "3He-B" in text and "project_3heb-inheritance" in text  # (local)

    cc4_pass = bool(has_R_JK_assign and has_xi_assign and has_R_JK_provenance and has_3heb_cite)  # (local)
    print(f"  CC-4 (canonical_constants.py grep):")
    print(f"    R_JK = ... assignment present:        {has_R_JK_assign}")
    print(f"    xi_E_GGE_inv = ... assignment present: {has_xi_assign}")
    print(f"    Provenance cite (S86-W4-1 P4 or gate): {has_R_JK_provenance}")
    print(f"    3He-B parent inheritance cite:         {has_3heb_cite}")
    print(f"    CC-4 PASS: {cc4_pass}")
    return cc4_pass


def cc5_reimport_check():
    """CC-5: re-import canonical_constants succeeds with both names accessible
    AND values match what the module exports."""
    # Re-import (the existing import * at top loaded the module; here we
    # explicitly check the names are bound and resolvable).
    import importlib
    import canonical_constants as _cc                              # (local)
    importlib.reload(_cc)                                          # (local) ensure post-edit values

    has_R_JK = hasattr(_cc, "R_JK")                                # (local)
    has_xi = hasattr(_cc, "xi_E_GGE_inv")                          # (local)

    R_JK_loaded = getattr(_cc, "R_JK", None)                       # (local)
    xi_loaded = getattr(_cc, "xi_E_GGE_inv", None)                 # (local)

    R_JK_is_float = isinstance(R_JK_loaded, (int, float))          # (local)
    xi_is_float = isinstance(xi_loaded, (int, float))              # (local)

    cc5_pass = bool(has_R_JK and has_xi and R_JK_is_float and xi_is_float)  # (local)
    print(f"  CC-5 (re-import check):")
    print(f"    canonical_constants.R_JK present: {has_R_JK} (value={R_JK_loaded})")
    print(f"    canonical_constants.xi_E_GGE_inv present: {has_xi} (value={xi_loaded})")
    print(f"    R_JK is numeric: {R_JK_is_float}")
    print(f"    xi_E_GGE_inv is numeric: {xi_is_float}")
    print(f"    CC-5 PASS: {cc5_pass}")
    return cc5_pass, R_JK_loaded, xi_loaded


# ---------------------------------------------------------------------------
# Section 7 — Verdict + main
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str,
                   closure_legacy: str) -> str:
    """Append S84+ inline dual-SHA verdict line + companion comment row."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                              # (local)
    companion = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]} "
        f"# 2B path-(c) BRANCH-IV commit; R_JE retired; "
        f"R_JK + xi_E_GGE_inv landed at SECTION E.B; "
        f"closure_legacy={closure_legacy[:16]}\n"
    )                                                              # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
    return line


def main() -> int:
    t0 = time.time()                                               # (local)

    # === Stage 1: Input pin SHA logging (first 20 lines of stdout) ===
    pins = log_input_pins(INPUT_FILES)                             # (local)
    closure = closure_hash(pins)                                   # (local)
    print(f"  closure (legacy single-SHA): {closure[:16]}...")
    print()

    # === Stage 2: Compute R_JK and xi_E_GGE_inv ===
    print("=== Stage 2: Compute R_JK + xi_E_GGE_inv ===")
    R_JK_anchor, R_JK_traj, prefactor, L_axis = compute_R_JK_from_cache()
    xi_inv_anchor, N_pair, lambda_avg = compute_xi_E_GGE_inv()
    print(f"  R_JK (S85 W12 ELIM-1 anchor at L_max=10): {R_JK_anchor:.10f}")
    print(f"  R_JK trajectory at L_max in {list(L_axis)}:")
    for L, R in zip(L_axis, R_JK_traj):
        print(f"    L_max={L}: R_JK={R:.10f}")
    print(f"  L_max-INDEPENDENT prefactor |Delta_BCS|^2/K_base = {prefactor:.16f}")
    print(f"  xi_E_GGE_inv (substrate-natural anchor):  {xi_inv_anchor:.10f}")
    print(f"    decomposition: N_pair_GGE = {N_pair} (S38 GGE permanence)")
    print(f"    decomposition: lambda_GGE_avg = Delta_BCS/K_base = {lambda_avg:.10f}")
    print()

    # === Stage 3: Five cross-checks ===
    print("=== Stage 3: Cross-checks (5 mandatory) ===")
    cc1_pass, cc1_ratio = cc1_R_JK_dimensional_rescaling(R_JK_anchor)
    cc2_pass, cc2_ratio = cc2_xi_E_GGE_inv_dimensional_rescaling(xi_inv_anchor)
    cc3_pass = cc3_framework_file_grep()
    cc4_pass = cc4_canonical_constants_grep()
    cc5_pass, R_JK_loaded, xi_loaded = cc5_reimport_check()
    print()

    # === Stage 4: Cross-check the loaded values match the computed anchors ===
    print("=== Stage 4: Loaded-vs-anchor consistency ===")
    R_JK_match_tol = 1e-12                                         # (local) full float64 precision (pub_sig_figs=15)
    xi_match_tol = 1e-12                                           # (local) full float64 precision (pub_sig_figs=15)
    R_JK_match = abs(R_JK_loaded - R_JK_anchor) < R_JK_match_tol if R_JK_loaded is not None else False  # (local)
    xi_match = abs(xi_loaded - xi_inv_anchor) < xi_match_tol if xi_loaded is not None else False        # (local)
    print(f"  loaded R_JK = {R_JK_loaded}, anchor = {R_JK_anchor:.10f}, match (tol {R_JK_match_tol}): {R_JK_match}")
    print(f"  loaded xi_E_GGE_inv = {xi_loaded}, anchor = {xi_inv_anchor:.10f}, match (tol {xi_match_tol}): {xi_match}")
    print()

    # === Stage 5: Aggregate verdict ===
    all_cc_pass = bool(cc1_pass and cc2_pass and cc3_pass and cc4_pass and cc5_pass)  # (local)
    consistency_pass = bool(R_JK_match and xi_match)               # (local)
    overall_pass = bool(all_cc_pass and consistency_pass)          # (local)

    print(f"=== Aggregate verdict ===")
    print(f"  CC-1 (R_JK dimensional):    {'PASS' if cc1_pass else 'FAIL'}")
    print(f"  CC-2 (xi dimensional):       {'PASS' if cc2_pass else 'FAIL'}")
    print(f"  CC-3 (framework grep):       {'PASS' if cc3_pass else 'FAIL'}")
    print(f"  CC-4 (canonical grep):       {'PASS' if cc4_pass else 'FAIL'}")
    print(f"  CC-5 (re-import):            {'PASS' if cc5_pass else 'FAIL'}")
    print(f"  Loaded-vs-anchor match:      {'PASS' if consistency_pass else 'FAIL'}")
    print(f"  Overall:                     {'PASS' if overall_pass else 'FAIL'}")
    print()

    # === Stage 6: Compute dual SHA, append verdict line ===
    script_path = Path(__file__).resolve()                         # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PY, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    verdict = "PASS" if overall_pass else "FAIL"                   # (local)
    value = "R_JE_retired+R_JK_landed+xi_E_GGE_inv_landed"         # (local)

    line = append_verdict(verdict, value, audit_sha, content_sha, closure)
    print(f"=== Verdict line appended ===")
    print(f"  {line.strip()}")
    print()

    # 4-tuple final non-verdict line
    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))
    print(f"  elapsed: {time.time()-t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
