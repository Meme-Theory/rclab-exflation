#!/usr/bin/env python3
"""
S91 W9-5 — S91-W6-CF-W7-2-CF-50-52-LOCKED-NORM-L_k-1-PRE-NORMALIZATION
======================================================================

Gate: S91-W6-CF-W7-2-CF-50-52-LOCKED-NORM-L_k-1-PRE-NORMALIZATION ([VERIFY] + [AUDIT])
  Alias: S91-W9-5; CF-50 + CF-52
  Schema: R3 ; S87+ schema-v2 3-tuple companion row REQUIRED

REQUIRED LAYER DECLARATION (per substrate-first-canonical-sourcing.md §(ii.A)):
  - consumption layer:  cache-moment (operates on s84_spectrum_cache_L12_tau019.npz)
  - target identity:    atlas-row F_traj = (k+1)/2
  - bridge machinery:   locked-norm L_k=1 pre-normalization
  (Layer declaration regex r"consumption layer:|target identity:|bridge machinery:"
   present in this docstring per §(ii.A) discipline; missing declaration would
   route to SOURCE-RECONCILIATION advisory S2.)

Pre-registered threshold (plan §W9-5 Field 9; ABSOLUTE):
  PASS iff max_err < 1e-10 AND layer declaration present in docstring
  FAIL iff max_err >= 1e-6 OR layer declaration absent
  INFO iff 1e-10 <= max_err < 1e-6

Inputs (SHA-256 dual-pinned per S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only)
  - .claude/rules/substrate-first-canonical-sourcing.md (§(ii.A) rule)
  - sessions/permanent-results-registry.md (§VII.AF.1.OP-PROJ canonical)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<max_bridge_error>,
   scheme=zeta-regularization-locked-norm-pre-normalization-atlas-row-bridge,
   convention=cache-moment-to-atlas-row-bridge-via-locked-norm-L_k-1-BdG-restricted,
   L_max=12)

Classification: PHONONIC x GEOMETRIC

METHODOLOGY
-----------
The substrate IS the spectral triple (A_K, H_K, D_K) at tau_fold = 0.19.
At the atlas-row layer the substrate's canonical first-spectrum-only-
functional moment satisfies F_traj(k) = (k+1)/2 (locked-norm L_k=1
identity; substrate-IS algebraic identity, regulator-invariant, L-
independent). At the cache-moment layer the same canonical quantity
admits a numerical evaluation M_k_cache(k) = Sigma_{alpha in BdG} m_alpha
|lambda_alpha|^k on the L_max=12 BdG-restricted Peter-Weyl cache. The
two layers are STRUCTURALLY ORTHOGONAL evaluation conventions per
substrate-first-canonical-sourcing.md §(ii.A); the pre-normalization
machinery N_k_locked_norm(k; L_k=1) IS the operational bridge.

This script (i) loads s84_spectrum_cache_L12_tau019.npz; (ii) filters
to the BdG sub-algebra image (M_2(C) ⊂ A_K = C ⊕ H ⊕ M_3(C); the
filter restricts to Peter-Weyl level == 1, corresponding to the
fundamental block image in A_K); (iii) computes F_traj_atlas(k) and
M_k_cache(k) for k ∈ [0, K_MAX=8]; (iv) evaluates the plan-prescribed
substrate-natural closed form xi_k(zeta-window) = Γ(k+1) / Γ(1+k/2)^2
and the corresponding N_k_locked_norm(k); (v) verifies the bridge
identity |F_traj_atlas(k) - M_k_cache(k)/N_k_locked_norm(k)| < 1e-10.

DISCIPLINE
----------
- `from canonical_constants import *` (tau_fold, M_KK, Delta_BCS)
- All local intermediates tagged `# (local)`
- numpy float64 + OMP_NUM_THREADS=8 cap (no GPU; cache moments are
  pure aggregations on a few thousand eigenvalues)
- SHA-256 of every input emitted in first ~20 lines of stdout
- Dual-SHA (audit_sha256 + content_sha256) per S84+
- 3-tuple companion row per S87+ schema-v2 (this gate carries [VERIFY] +
  [AUDIT] triggers; a 3-tuple is REQUIRED)

SUBSTITUTION CHAIN (for sign/direction; required by math-scripts.md
§"Double-Check Logic Before Compute")
------------------------------------------------------------------
Step 1 — Definitions:
  F_traj_atlas(k) = (k+1)/2                              [substrate-IS atlas-row]
  M_k_cache(k)    = Σ_{α∈BdG} m_α · |λ_α|^k              [L_max=12 cache-moment]
  xi_k(zeta)      = Γ(k+1) / Γ(1+k/2)^2                  [plan-prescribed §W9-5 line 869]
  N_k_locked_norm = M_k_cache(k) · xi_k(zeta) / L_k      [plan-prescribed line 870; L_k=1]

Step 2 — Substitution (cache-moment normalized at L_k=1):
  M_k_norm(k) := M_k_cache(k) / N_k_locked_norm(k)
              = M_k_cache(k) / (M_k_cache(k) · xi_k / 1.0)
              = 1 / xi_k
              = Γ(1+k/2)^2 / Γ(k+1)

Step 3 — Bridge error at k=0 (canonical first cross-check):
  F_traj_atlas(0) = 0.5
  M_0_norm        = Γ(1)^2 / Γ(1) = 1.0
  |F_traj_atlas(0) − M_0_norm| = 0.5

Step 4 — Direction:
  The bridge identity F_traj_atlas(k) ≡ M_k_norm(k) requires
    (k+1)/2 = Γ(1+k/2)^2 / Γ(k+1)  for all k ∈ [0, K_MAX].
  Evaluating at k=0,1,2 shows the LHS sequence is (0.5, 1.0, 1.5)
  while the RHS sequence is (1.0, π/4, 0.5). The two sequences do
  NOT agree; max_err ≥ 0.5 is set by k=0 already. Result: FAIL.

Step 5 — Conclusion (substrate-physics reading; per Field 11):
  FAIL means "Bridge machinery defective. Either the locked-norm
  factor N_k_locked_norm is misidentified (substrate-natural xi_k
  closed-form is wrong) OR the cache-moment/atlas-row layers are
  structurally non-bridgeable at L_max=12". The plan-prescribed
  xi_k = Γ(k+1)/Γ(1+k/2)^2 does not produce the (k+1)/2 atlas-row
  identity under pre-normalization at L_k=1; the operational diagnostic
  here surfaces the substrate-natural ξ_k closed-form mismatch as the
  carry-forward target for S92 refinement.

Honest disclosure (per agent-standards.md §"Completion Verification"):
  the substitution chain is computed exactly as written in plan §W9-5
  Field 6. No convention-shopping, no threshold-loosening. The
  diagnostic emitted by this script — max_err = 0.5 set by k=0 —
  IS the substrate-physics finding the plan's Field 11 anticipates
  as a FAIL-classification outcome.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — CPU thread cap (set BEFORE numpy import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 2 — Canonical constants (MANDATORY first import after env cap)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import tau_fold, M_KK, Delta_BCS  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
import numpy as np  # noqa: E402
from scipy.special import gamma  # noqa: E402

# ---------------------------------------------------------------------------
# Section 4 — Paths + pre-registration constants
# ---------------------------------------------------------------------------
SESSION = "S91"  # (local)
GATE_ID = "S91-W6-CF-W7-2-CF-50-52-LOCKED-NORM-L_k-1-PRE-NORMALIZATION"  # (local)
SCHEME = "zeta-regularization-locked-norm-pre-normalization-atlas-row-bridge"  # (local)
CONVENTION = "cache-moment-to-atlas-row-bridge-via-locked-norm-L_k-1-BdG-restricted"  # (local)
L_MAX = 12  # (local) plan-pinned

# Plan-pinned PRDR (§W9-5 Field 7)
P_BDG_BLOCK_IDX = 1     # (local) Peter-Weyl level index for BdG image M_2(C) ⊂ A_K
K_MAX = 8               # (local) substrate-distance-1 pole exhaustion scan range
BRIDGE_TOL = 1e-10      # (local) PASS threshold (ABSOLUTE; machine epsilon)
INFO_CEILING = 1e-6     # (local) INFO band ceiling
L_K = 1.0               # (local) locked-norm L_k=1 canonical pre-normalization

# Inputs
CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
RULE_SUBSTRATE_FIRST_PATH = PROJECT_ROOT / ".claude" / "rules" / "substrate-first-canonical-sourcing.md"
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

# Outputs
OUT_NPZ = SESSION_DIR / "s91_w9_cf50_52_locked_norm_lk1_pre_normalization.npz"
VERDICT_TXT = SESSION_DIR / "s91_gate_verdicts.txt"

INPUT_FILES = [
    CACHE_PATH,
    CANONICAL_PATH,
    RULE_SUBSTRATE_FIRST_PATH,
    REGISTRY_PATH,
]

# ---------------------------------------------------------------------------
# Section 5 — SHA-256 dual-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema."""
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 6 — Cache loader + BdG sub-algebra filter
# ---------------------------------------------------------------------------

def load_bdg_filtered_spectrum() -> tuple[np.ndarray, np.ndarray, dict]:
    """Load s84 L_max=12 cache, filter to BdG sub-algebra image (M_2(C) ⊂ A_K).

    The cache is keyed by SU(3) Young-diagram tuples (p, q) with each
    value carrying {'dim', 'level' = p+q, 'abs_evals'}. The BdG image
    M_2(C) ⊂ A_K corresponds to the level == P_BDG_BLOCK_IDX (= 1)
    Peter-Weyl restriction; this is the fundamental rep image
    that descends to the BdG sub-algebra of A_K = C ⊕ H ⊕ M_3(C).
    """
    cache = np.load(CACHE_PATH, allow_pickle=True)
    sector_dict = cache["sector_evals"].item()  # (local) dict-of-dicts

    lam_list: list[float] = []  # (local)
    mult_list: list[float] = []  # (local)
    sector_counts: dict[tuple, int] = {}  # (local) per-(p,q) count diagnostic
    for (p, q), entry in sector_dict.items():
        if entry["level"] == P_BDG_BLOCK_IDX:
            evs = np.asarray(entry["abs_evals"], dtype=np.float64)
            # Multiplicity weight m_α = dim of the Peter-Weyl block;
            # the cache stores each eigenvalue once per multiplet so
            # multiplicity = 1.0 per stored entry under the standard
            # convention used in S84+ cache builds (each row already
            # counts a single eigenvalue).
            mults = np.ones_like(evs)
            lam_list.extend(evs.tolist())
            mult_list.extend(mults.tolist())
            sector_counts[(p, q)] = int(evs.size)

    lam = np.array(lam_list, dtype=np.float64)  # (local)
    m = np.array(mult_list, dtype=np.float64)  # (local)
    return lam, m, sector_counts


# ---------------------------------------------------------------------------
# Section 7 — Bridge identity machinery (substrate atlas-row vs cache-moment)
# ---------------------------------------------------------------------------

def F_traj_atlas(k: int) -> float:
    """Substrate-IS atlas-row identity at locked-norm L_k=1.

    Closed form: F_traj_atlas(k) = (k+1)/2. Regulator-invariant,
    L-independent; derived from the locked-norm L_k=1 normalization
    domain of the substrate's first-spectrum-only-functional moment.
    """
    return (k + 1) / 2.0


def M_k_cache(k: int, lam: np.ndarray, m: np.ndarray) -> float:
    """Cache-moment k-th moment Σ_α m_α |λ_α|^k on BdG-restricted spectrum.

    Numerical evaluation at L_max=12 truncation of the substrate
    spectrum-only functional; algebra-INVARIANT family per
    cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality
    K-counter" MANDATORY K=3 classification.
    """
    return float(np.sum(m * lam ** k))


def xi_k_zeta_window(k: int) -> float:
    """Substrate-natural zeta-window regularization factor at locked-norm L_k=1.

    Plan-prescribed closed form (§W9-5 line 869):
        ξ_k(zeta-window) = Γ(k+1) / Γ(1+k/2)^2
    """
    return float(gamma(k + 1) / gamma(1 + k / 2.0) ** 2)


def N_k_locked_norm(k: int, lam: np.ndarray, m: np.ndarray, L_k: float = L_K) -> float:
    """Locked-norm L_k=1 pre-normalization factor (plan-prescribed line 870).

        N_k(zeta; L_k=1) = Σ_α m_α |λ_α|^k · ξ_k(zeta-window) / L_k
                        = M_k_cache(k) · ξ_k / L_k
    """
    return M_k_cache(k, lam, m) * xi_k_zeta_window(k) / L_k


def M_k_cache_normalized(k: int, lam: np.ndarray, m: np.ndarray) -> float:
    """Cache-moment normalized at locked-norm L_k=1 (Step 2 of substitution chain).

    Algebraic reduction: M_k_norm = M_k_cache / N_k = L_k / ξ_k.
    """
    Mk = M_k_cache(k, lam, m)  # (local)
    Nk = N_k_locked_norm(k, lam, m)  # (local)
    return Mk / Nk


# ---------------------------------------------------------------------------
# Section 8 — Layer-declaration self-audit (per §(ii.A) discipline)
# ---------------------------------------------------------------------------

def verify_layer_declaration() -> tuple[bool, dict[str, bool]]:
    """Verify producing-script docstring carries the §(ii.A) layer markers.

    Patterns (per plan §W9-5 line 824 + Field 6 Cross-checks line 890):
      r"consumption layer:|target identity:|bridge machinery:"
    Each pattern must appear at least once in this script's docstring.
    """
    import re
    script_text = Path(__file__).read_text(encoding="utf-8")  # (local)
    # Restrict to the module-level docstring (first triple-quoted block)
    m = re.match(r'^(?:.*?\n)?"""(.*?)"""', script_text, re.DOTALL)  # (local)
    docstring = m.group(1) if m else ""  # (local)
    markers = {  # (local)
        "consumption layer": "consumption layer:" in docstring,
        "target identity": "target identity:" in docstring,
        "bridge machinery": "bridge machinery:" in docstring,
    }
    all_present = all(markers.values())
    return all_present, markers


# ---------------------------------------------------------------------------
# Section 9 — Gate verdict + 4-tuple emission
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def evaluate_gate(max_err: float, layer_declared: bool) -> str:
    """Apply plan §W9-5 Field 9 PASS/FAIL/INFO bands.

    PASS  iff max_err < 1e-10 AND layer_declared
    FAIL  iff max_err >= 1e-6 OR not layer_declared
    INFO  iff 1e-10 <= max_err < 1e-6 AND layer_declared
    """
    if not layer_declared:
        return "FAIL"
    if max_err < BRIDGE_TOL:
        return "PASS"
    if max_err >= INFO_CEILING:
        return "FAIL"
    return "INFO"


def composite_3tuple(
    max_err: float, layer_declared: bool, regime_valid: bool
) -> tuple[str, str, str, str]:
    """Compute (composite, sign, magnitude, regime) per gate-verdicts.md §S87+.

    sign_verdict      = N/A (this gate has no signed-delta pre-registration;
                        the threshold compares an absolute |F − M_norm|)
    magnitude_verdict = PASS  if max_err < BRIDGE_TOL
                        INFO  if BRIDGE_TOL <= max_err < INFO_CEILING
                        FAIL  otherwise OR layer-declaration absent
    regime_verdict    = VALID (cache moments aggregate Σ over a finite,
                        fully populated BdG-restricted spectrum; no
                        small-parameter expansion is invoked; the
                        gate's numerical method is exact)

    composite collapses per the pre-registered rule at gate-verdicts.md
    §"Composite-collapse rule".
    """
    sign = "N/A"  # (local)
    if not layer_declared:
        magnitude = "FAIL"
    elif max_err < BRIDGE_TOL:
        magnitude = "PASS"
    elif max_err < INFO_CEILING:
        magnitude = "INFO"
    else:
        magnitude = "FAIL"
    regime = "VALID" if regime_valid else "BREAKDOWN"  # (local)
    # Collapse rule:
    if regime == "BREAKDOWN":
        composite = "FAIL"
    elif sign == "FAIL":
        composite = "FAIL"
    elif magnitude == "FAIL" and regime == "VALID":
        composite = "FAIL"
    elif magnitude == "FAIL" and regime == "MARGINAL":
        composite = "INFO"
    elif magnitude == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign, magnitude, regime


def append_verdict(
    verdict: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
    sign_v: str,
    magnitude_v: str,
    regime_v: str,
    notes: str,
) -> None:
    """Append canonical line + dual-SHA companion + 3-tuple companion row.

    Atomic single open('a') write per gate-verdicts.md §"Option A" /
    POSIX O_APPEND semantics (no read-modify-write).
    """
    line1 = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    line2 = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    line3 = (
        f"# sign_verdict={sign_v} magnitude_verdict={magnitude_v} "
        f"regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); {notes}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line1)
        fp.write(line2)
        fp.write(line3)


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 10.1 SHA input-pin block (first ~20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 10.2 Layer-declaration self-audit (§(ii.A) discipline)
    layer_declared, markers = verify_layer_declaration()
    print(f"=== Layer-declaration self-audit (§(ii.A)) ===")
    for k, v in markers.items():
        print(f"  '{k}:' present in docstring: {v}")
    print(f"  ALL THREE PRESENT: {layer_declared}")
    print()

    # 10.3 Canonical constants echo
    print(f"=== Canonical constants ===")
    print(f"  tau_fold  = {tau_fold}")
    print(f"  M_KK      = {M_KK}")
    print(f"  Delta_BCS = {Delta_BCS}")
    print()

    # 10.4 BdG-filtered spectrum load
    lam, mult, sector_counts = load_bdg_filtered_spectrum()
    n_modes = len(lam)  # (local)
    print(f"=== BdG sub-algebra image filter (M_2(C) ⊂ A_K) ===")
    print(f"  Peter-Weyl filter: level == P_BDG_BLOCK_IDX (= {P_BDG_BLOCK_IDX})")
    print(f"  Sectors retained: {sorted(sector_counts.keys())}")
    print(f"  Eigenvalue counts per sector: {sector_counts}")
    print(f"  Total BdG-restricted eigenvalues: {n_modes}")
    if n_modes > 0:
        print(f"  |λ| range: [{lam.min():.6f}, {lam.max():.6f}]")
    print()

    # 10.5 Bridge identity verification table
    print(f"=== Bridge identity verification (k ∈ [0, {K_MAX}]) ===")
    print(f"  F_traj_atlas(k) = (k+1)/2  vs  M_k_cache(k)/N_k_locked_norm(k)")
    print()
    F_table: list[float] = []  # (local)
    M_table: list[float] = []  # (local)
    Mnorm_table: list[float] = []  # (local)
    Nk_table: list[float] = []  # (local)
    xi_table: list[float] = []  # (local)
    err_table: list[float] = []  # (local)
    print(f"  {'k':>3} {'F_traj_atlas':>14} {'M_k_cache':>16} "
          f"{'xi_k(zeta)':>14} {'N_k_locked':>16} "
          f"{'M_k_norm':>14} {'|err|':>14}")
    print(f"  {'-'*3:>3} {'-'*14:>14} {'-'*16:>16} {'-'*14:>14} "
          f"{'-'*16:>16} {'-'*14:>14} {'-'*14:>14}")
    for k in range(K_MAX + 1):
        f_atlas = F_traj_atlas(k)
        M_k = M_k_cache(k, lam, mult)
        xi_k = xi_k_zeta_window(k)
        N_k = N_k_locked_norm(k, lam, mult)
        M_norm = M_k_cache_normalized(k, lam, mult)
        err = abs(f_atlas - M_norm)
        F_table.append(f_atlas)
        M_table.append(M_k)
        xi_table.append(xi_k)
        Nk_table.append(N_k)
        Mnorm_table.append(M_norm)
        err_table.append(err)
        print(f"  {k:>3d} {f_atlas:>14.10f} {M_k:>16.6e} "
              f"{xi_k:>14.10f} {N_k:>16.6e} "
              f"{M_norm:>14.10f} {err:>14.6e}")
    print()
    max_err = max(err_table)  # (local)
    argmax_k = int(np.argmax(np.asarray(err_table)))  # (local)
    print(f"=== Bridge error summary ===")
    print(f"  max_err = {max_err:.10e}  (at k={argmax_k})")
    print(f"  PASS threshold: < {BRIDGE_TOL:.0e}")
    print(f"  INFO band:      [{BRIDGE_TOL:.0e}, {INFO_CEILING:.0e})")
    print(f"  FAIL threshold: >= {INFO_CEILING:.0e}")
    print()

    # 10.6 Cross-check: cache-moment ratio M_2/M_4 (plan §W9-5 line 889)
    M_2 = M_table[2]  # (local)
    M_4 = M_table[4]  # (local)
    M2_over_M4 = M_2 / M_4 if M_4 != 0 else float("inf")  # (local)
    print(f"=== Cross-check (plan line 889): M_2(zeta)/M_4(zeta) on BdG cache ===")
    print(f"  M_2 = {M_2:.10e}")
    print(f"  M_4 = {M_4:.10e}")
    print(f"  M_2/M_4 = {M2_over_M4:.10e}  (cache-moment-layer diagnostic)")
    print()

    # 10.7 Gate evaluation
    verdict = evaluate_gate(max_err, layer_declared)
    # All cache aggregations are exact within float64; no small-parameter expansion
    regime_valid = True  # (local) cache-moment aggregations are exact
    composite, sign_v, mag_v, reg_v = composite_3tuple(
        max_err, layer_declared, regime_valid
    )
    assert composite == verdict, (
        f"composite ({composite}) ≠ evaluate_gate ({verdict}); "
        f"check collapse rule consistency"
    )

    # 10.8 npz output (with layer declaration metadata in npz)
    np.savez(
        OUT_NPZ,
        # Layer declaration metadata (per §(ii.A) discipline)
        layer_consumption=np.array("cache-moment"),
        layer_target_identity=np.array("atlas-row F_traj = (k+1)/2"),
        layer_bridge_machinery=np.array("locked-norm L_k=1 pre-normalization"),
        layer_declaration_present=np.array(layer_declared),
        # PRDR pins
        L_max=np.array(L_MAX),
        P_BDG_BLOCK_IDX=np.array(P_BDG_BLOCK_IDX),
        K_MAX=np.array(K_MAX),
        BRIDGE_TOL=np.array(BRIDGE_TOL),
        L_k=np.array(L_K),
        tau_fold_pin=np.array(tau_fold),
        # Tables
        k_vals=np.arange(K_MAX + 1),
        F_traj_atlas=np.array(F_table),
        M_k_cache=np.array(M_table),
        xi_k_zeta=np.array(xi_table),
        N_k_locked_norm=np.array(Nk_table),
        M_k_cache_normalized=np.array(Mnorm_table),
        bridge_errors=np.array(err_table),
        # Summary
        max_err=np.array(max_err),
        argmax_k=np.array(argmax_k),
        n_bdg_modes=np.array(n_modes),
        M_2_over_M_4=np.array(M2_over_M4),
        # Verdicts
        verdict=np.array(verdict),
        sign_verdict=np.array(sign_v),
        magnitude_verdict=np.array(mag_v),
        regime_verdict=np.array(reg_v),
        # SHAs
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"=== Output ===")
    print(f"  {OUT_NPZ}")
    print()

    # 10.9 Emit 4-tuple + append dual-SHA + 3-tuple verdict lines
    value_str = f"max_err={max_err:.10e};argmax_k={argmax_k};layer_declared={layer_declared};M_2/M_4={M2_over_M4:.6e};n_modes={n_modes}"  # (local)
    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)
    print(tag)

    if verdict == "PASS":
        notes = (
            "bridge identity holds at machine epsilon; locked-norm L_k=1 "
            "pre-normalization operationalized; §(ii.A) layer declaration present"
        )
    elif verdict == "INFO":
        notes = (
            f"marginal bridge satisfaction (max_err={max_err:.3e} in INFO band "
            f"[{BRIDGE_TOL:.0e}, {INFO_CEILING:.0e})); §(ii.A) layer declaration present; "
            "sub-pole-class refinement queued"
        )
    else:  # FAIL
        notes = (
            f"bridge identity broken at max_err={max_err:.3e} (argmax k={argmax_k}); "
            f"plan-prescribed xi_k=Gamma(k+1)/Gamma(1+k/2)^2 yields M_k_norm=1/xi_k "
            f"= Gamma(1+k/2)^2/Gamma(k+1) which does NOT equal (k+1)/2 closed-form "
            f"atlas-row identity; substrate-natural xi_k closed form misidentified "
            f"per plan §W9-5 Field 11 FAIL semantics; carry-forward to S92 substrate-"
            f"natural xi_k canonical derivation; layer_declared={layer_declared} per §(ii.A)"
        )
    append_verdict(verdict, value_str, audit_sha, content_sha,
                   sign_v, mag_v, reg_v, notes)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # verdict is data; script-health exit unaffected


if __name__ == "__main__":
    sys.exit(main())
