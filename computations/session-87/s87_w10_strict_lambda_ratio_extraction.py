#!/usr/bin/env python3
"""
S87 W10-4 — S87-STRICT-LAMBDA-RATIO-EXTRACTION
================================================================

Gate: S87-STRICT-LAMBDA-RATIO-EXTRACTION ([VERIFY])

Pre-registered threshold (sessions/session-plan/session-87-plan-w10.md §W10-4 lines 358-360):
  PASS iff bit-exact extraction completes; ratio is finite positive float64;
       cache content_sha256 matches input pin bit-exactly.
  FAIL iff cache content_sha256 mismatch OR ratio non-finite OR
       zero_mode_exclusion logic raised an exception.
  INFO iff ratio is finite positive but lies outside the diagnostic band
       [1e-12, 1e+0].

Pre-registered substitution chain (lines 346-354):
  Step 1: lambda_array := loaded eigenvalues from
          computations/session-84/s84_spectrum_cache_L12_tau019.npz
  Step 2: |lambda| := numpy.abs(lambda_array)
          [STRUCTURAL NOTE: cache stores per-sector 'abs_evals' arrays,
           which are already |lambda|. numpy.abs is idempotent on
           non-negative finite floats: numpy.abs(x) == x bit-identically
           for x >= 0 by IEEE 754, so Step 2 is a no-op consistency seal.]
  Step 3: |lambda|_min := numpy.min(|lambda|[|lambda| > 0])
          (zero modes excluded from the min via strict-positive mask)
  Step 4: |lambda|_max := numpy.max(|lambda|)
  Step 5: ratio := |lambda|_min / |lambda|_max
  Step 6: PASS iff bit-exact extraction completes (no float epsilon allowed)

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
      Pre-flight pin (registry permanent-results §line 12866 / 15033 / 15764):
      content_sha256 = 9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<ratio>+<zero_mode_count>, scheme=direct-numpy-extract,
   convention=bit-exact-float64, L_max=12)

Classification: GEOMETRIC (substrate-spectral invariant of D_K(tau_fold);
                no derivation, no regulator choice — direct cache extraction).

METHODOLOGY
-----------
The L_max=12 spectrum cache was produced by S84 (predecessor of all
substrate-spectral computations at tau_fold=0.190). Its structure is:
{(p, q): {'dim': irrep_dim, 'level': L = p+q, 'abs_evals': |lambda|_array}}
keyed over Cartan-weight tuples (p,q) with 0 <= p+q <= 12.

This gate concatenates abs_evals across ALL 90 sectors (no level
truncation; full L_max=12 cache as plan-pinned), then extracts:

  N_eval        = total count of eigenvalue entries in the concatenated array
  zero_mode_cnt = count of EXACTLY zero entries (|lambda| == 0.0 bit-exact)
  |lambda|_min  = min over the strictly-positive subset
  |lambda|_max  = max over the full array
  ratio         = |lambda|_min / |lambda|_max

The ratio is a substrate-spectral invariant of D_K(tau_fold) at the cache
truncation L_max=12 — anchor for any future condition-number argument.
No physical interpretation is performed at this gate (per plan line 393).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-only path (plan line 373: numpy.abs/min/max are O(N) trivial)
- Bit-exact tolerance = 0; no float epsilon (plan line 369)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Cache content_sha256 cross-checked against pre-flight pin from
  permanent-results-registry; mismatch -> FAIL with class-(c) PIN-DRIFT
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import tau_fold, M_KK  # explicit pin echo

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
import matplotlib
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

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S87"                                                    # (local)
GATE_ID = "S87-STRICT-LAMBDA-RATIO-EXTRACTION"                     # (local)
SCHEME = "direct-numpy-extract"                                    # (local)
CONVENTION = "bit-exact-float64"                                   # (local)
L_MAX = 12                                                         # (local)

# Pre-registered diagnostic band (plan line 360)
INFO_BAND_LO = 1.0e-12                                             # (local)
INFO_BAND_HI = 1.0e+0                                              # (local)

# Pre-flight pin: cache content_sha256 from permanent-results-registry
# (registry lines 12866 / 15033 / 15764, all consistent).
PRE_FLIGHT_CACHE_SHA = (
    "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"
)                                                                  # (local)

# Output destinations
OUT_NPZ = resolve_output(87, 's87_w10_strict_lambda_ratio_extraction.npz')
OUT_PNG = resolve_output(87, 's87_w10_strict_lambda_ratio_extraction.png')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

CACHE_PATH = resolve_output(84, 's84_spectrum_cache_L12_tau019.npz')
CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = [
    CANONICAL_PATH,
    CACHE_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                           # (local)
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
        print(f"  {rel}: {sha}")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()                        # (local)
    canonical_bytes = canonical_path.read_bytes()                  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                              # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                    # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute (substitution chain Steps 1-5)
# ---------------------------------------------------------------------------

def extract_strict_ratio(cache_path: Path) -> dict:
    """Bit-exact |lambda|_min/|lambda|_max extraction from L_max=12 cache.

    Returns a dict with all intermediate counts and the final ratio.
    Raises only on cache structural defects (missing 'sector_evals' key,
    missing 'abs_evals' inner key, empty array, or all-zero spectrum).
    """
    npz = np.load(cache_path, allow_pickle=True)                   # (local)
    if "sector_evals" not in npz.files:
        raise KeyError(
            f"cache missing 'sector_evals' key; available={list(npz.files)}"
        )
    sector_evals = npz["sector_evals"].item()                      # (local)
    if not isinstance(sector_evals, dict):
        raise TypeError(
            f"sector_evals expected dict, got {type(sector_evals).__name__}"
        )
    n_sectors = len(sector_evals)                                  # (local)

    # ---- Step 1: assemble lambda_array (concatenate per-sector 'abs_evals')
    arrays: list[np.ndarray] = []                                  # (local)
    levels_present: set[int] = set()                               # (local)
    sector_count_per_level: dict[int, int] = {}                    # (local)
    eval_count_per_level: dict[int, int] = {}                      # (local)
    multiplicity_weighted_total: int = 0                           # (local)
    for (p, q), data in sector_evals.items():
        if "abs_evals" not in data:
            raise KeyError(
                f"sector ({p},{q}) missing 'abs_evals'; "
                f"keys={list(data.keys())}"
            )
        arr = np.asarray(data["abs_evals"], dtype=np.float64)      # (local)
        arrays.append(arr)
        L = int(data.get("level", p + q))                          # (local)
        levels_present.add(L)
        sector_count_per_level[L] = sector_count_per_level.get(L, 0) + 1
        eval_count_per_level[L] = eval_count_per_level.get(L, 0) + len(arr)
        d = int(data.get("dim", 1))                                # (local)
        multiplicity_weighted_total += len(arr) * d

    lambda_array = np.concatenate(arrays)                          # (local)
    N_eval_raw = int(lambda_array.size)                            # (local)

    # ---- Step 2: |lambda| := numpy.abs(lambda_array)
    # The cache field is named 'abs_evals' so values are already |lambda|.
    # numpy.abs is the idempotent consistency seal (Step 2's role is to make
    # the substitution chain explicit; bit-identical output for x >= 0).
    abs_lambda = np.abs(lambda_array)                              # (local)
    # Idempotency sanity: cache values must be non-negative as advertised.
    n_negative = int(np.sum(lambda_array < 0.0))                   # (local)
    bit_identity_step2 = bool(np.array_equal(abs_lambda, lambda_array))  # (local)

    # ---- Step 3: |lambda|_min := numpy.min(|lambda|[|lambda| > 0])
    positive_mask = abs_lambda > 0.0                               # (local)
    zero_mode_count = int(np.sum(~positive_mask))                  # (local)
    n_positive = int(np.sum(positive_mask))                        # (local)
    if n_positive == 0:
        raise ValueError(
            "all eigenvalues are zero (no positive entries to take min over)"
        )
    abs_lambda_min = float(np.min(abs_lambda[positive_mask]))      # (local)

    # ---- Step 4: |lambda|_max := numpy.max(|lambda|)
    abs_lambda_max = float(np.max(abs_lambda))                     # (local)

    # ---- Step 5: ratio
    if abs_lambda_max == 0.0:
        raise ValueError(
            "|lambda|_max == 0; cannot form ratio (denominator zero)"
        )
    ratio = abs_lambda_min / abs_lambda_max                        # (local)

    # Per-level cumulative counts (for cross-check / WP §Results table)
    levels_sorted = sorted(levels_present)                         # (local)
    cum_count_at_level: dict[int, int] = {}                        # (local)
    cum = 0                                                        # (local)
    for L in levels_sorted:
        cum += eval_count_per_level[L]
        cum_count_at_level[L] = cum

    return {
        "n_sectors": n_sectors,
        "levels_present": levels_sorted,
        "L_max_in_cache": max(levels_sorted),
        "sector_count_per_level": sector_count_per_level,
        "eval_count_per_level": eval_count_per_level,
        "cum_count_at_level": cum_count_at_level,
        "N_eval_raw": N_eval_raw,
        "multiplicity_weighted_total": multiplicity_weighted_total,
        "n_negative_in_cache": n_negative,
        "bit_identity_step2": bit_identity_step2,
        "n_positive": n_positive,
        "zero_mode_count": zero_mode_count,
        "abs_lambda_min": abs_lambda_min,
        "abs_lambda_max": abs_lambda_max,
        "ratio": ratio,
        "abs_lambda_full": abs_lambda,  # used for plot only; not persisted as raw
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(result: dict, png_path: Path) -> None:
    abs_lambda = result["abs_lambda_full"]
    pos = abs_lambda[abs_lambda > 0.0]                             # (local)
    lam_min = result["abs_lambda_min"]                             # (local)
    lam_max = result["abs_lambda_max"]                             # (local)
    ratio = result["ratio"]                                        # (local)
    zmc = result["zero_mode_count"]                                # (local)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))                # (local)

    # Left: log-spaced histogram of |lambda| (positive subset)
    ax = axes[0]
    ax.hist(np.log10(pos), bins=120, color="#2c7fb8",
            alpha=0.85, edgecolor="white", linewidth=0.3)
    ax.axvline(np.log10(lam_min), color="#d62728", linestyle="--",
               linewidth=1.4, label=f"|lambda|_min = {lam_min:.6e}")
    ax.axvline(np.log10(lam_max), color="#2ca02c", linestyle="--",
               linewidth=1.4, label=f"|lambda|_max = {lam_max:.6e}")
    ax.set_xlabel(r"$\log_{10}\,|\lambda|$ (cache units; $D_K$ at $\tau_{\rm fold}$)")
    ax.set_ylabel("count (raw eigenvalue entries)")
    ax.set_title(
        r"L_max=12 spectrum: $|\lambda|$ histogram"
        f"  (N={result['N_eval_raw']}, zero modes={zmc})"
    )
    ax.legend(loc="upper left", fontsize=9, frameon=False)
    ax.grid(alpha=0.3, linestyle=":")

    # Right: log-log spectral density (sorted |lambda| vs index)
    ax2 = axes[1]
    sorted_pos = np.sort(pos)                                      # (local)
    idx = np.arange(1, len(sorted_pos) + 1)                        # (local)
    ax2.loglog(idx, sorted_pos, color="#2c7fb8", linewidth=0.7,
               label="sorted |lambda| (positive subset)")
    ax2.axhline(lam_min, color="#d62728", linestyle="--",
                linewidth=1.4, alpha=0.85,
                label=f"|lambda|_min")
    ax2.axhline(lam_max, color="#2ca02c", linestyle="--",
                linewidth=1.4, alpha=0.85,
                label=f"|lambda|_max")
    ax2.set_xlabel("rank (sorted ascending)")
    ax2.set_ylabel(r"$|\lambda|$")
    title_ratio = (
        r"ratio $|\lambda|_{\min}/|\lambda|_{\max}$"
        f" = {ratio:.6e}"
    )
    ax2.set_title(title_ratio)
    ax2.legend(loc="lower right", fontsize=9, frameon=False)
    ax2.grid(alpha=0.3, linestyle=":", which="both")

    fig.suptitle(
        f"S87-STRICT-LAMBDA-RATIO-EXTRACTION: bit-exact |lambda| extrema "
        f"from L_max=12 D_K cache at tau_fold=0.190",
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(png_path, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max: int) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def evaluate_gate(
    ratio: float,
    cache_sha: str,
    cache_sha_pre_flight: str,
) -> tuple[str, str]:
    """Return (verdict, value_string) per plan §W10-4 threshold.

    PASS  iff cache SHA matches AND ratio finite positive AND in band.
    INFO  iff cache SHA matches AND ratio finite positive AND out-of-band.
    FAIL  iff cache SHA mismatch OR ratio non-finite OR ratio <= 0.
    """
    if cache_sha != cache_sha_pre_flight:
        return ("FAIL",
                f"cache_content_sha256_mismatch_{cache_sha[:16]}")
    if not (math.isfinite(ratio) and ratio > 0.0):
        return ("FAIL",
                f"ratio_non_finite_or_nonpositive_{ratio!r}")
    if INFO_BAND_LO <= ratio <= INFO_BAND_HI:
        return ("PASS", f"{ratio:.17e}")
    # finite positive, out of [1e-12, 1e0]
    return ("INFO", f"{ratio:.17e}_out_of_band[{INFO_BAND_LO},{INFO_BAND_HI}]")


def append_verdict(
    verdict: str,
    value_string: str,
    zero_mode_count: int,
    audit_sha: str,
    content_sha: str,
) -> str:
    """Append canonical verdict line + dual-SHA companion comment row.

    The `value=` field encodes BOTH ratio and zero_mode_count per plan
    expected-output 4-tuple line 385:
        (value=<|lambda|_min/|lambda|_max ratio bit-exact + zero-mode-count>, ...)
    """
    full_value = (
        f"ratio={value_string};zero_mode_count={zero_mode_count}"
    )                                                              # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value={full_value!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=R3\n"
    )                                                              # (local)
    short_audit = audit_sha[:16]                                   # (local)
    short_content = content_sha[:16]                               # (local)
    companion = (
        f"# audit_sha256_short={short_audit} "
        f"content_sha256_short={short_content} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )                                                              # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
    return line


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    # ---- Pre-flight: input pins (must print in first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)                             # (local)
    closure = closure_hash(pins)                                   # (local)
    print(f"  closure_hash: {closure}")
    print(f"  pre_flight_cache_sha (registry pin): {PRE_FLIGHT_CACHE_SHA}")
    cache_sha_runtime = pins.get(
        "computations/session-84/s84_spectrum_cache_L12_tau019.npz", ""
    )                                                              # (local)
    sha_match = (cache_sha_runtime == PRE_FLIGHT_CACHE_SHA)        # (local)
    print(f"  cache_sha_runtime_match_pre_flight: {sha_match}")
    print(f"=== {GATE_ID} — substitution chain Steps 1-5 ===")

    # ---- Compute (extraction)
    extraction_error: str = ""                                     # (local)
    try:
        result = extract_strict_ratio(CACHE_PATH)                  # (local)
    except Exception as exc:
        # Step 6 FAIL clause: zero_mode_exclusion or cache structure exception
        extraction_error = f"{type(exc).__name__}: {exc}"
        print(f"  EXTRACTION_EXCEPTION: {extraction_error}")
        # Compute SHAs anyway for verdict emission honesty
        audit_sha, content_sha = compute_dual_sha(
            SCRIPT_PATH, CANONICAL_PATH, pins
        )
        line = append_verdict(
            "FAIL",
            f"extraction_exception_{type(exc).__name__}",
            -1,
            audit_sha,
            content_sha,
        )
        print(f"  audit_sha256:   {audit_sha}")
        print(f"  content_sha256: {content_sha}")
        print(f"  verdict-line:   {line.rstrip()}")
        return 0  # script ran successfully; verdict is data (FAIL is a result)

    # ---- Print extraction summary
    print(f"  n_sectors:                 {result['n_sectors']}")
    print(f"  L_max_in_cache:            {result['L_max_in_cache']}")
    print(f"  N_eval_raw (entries):      {result['N_eval_raw']}")
    print(f"  multiplicity_weighted:     {result['multiplicity_weighted_total']}")
    print(f"  n_negative_in_cache:       {result['n_negative_in_cache']}")
    print(f"  bit_identity_step2:        {result['bit_identity_step2']}")
    print(f"  n_positive:                {result['n_positive']}")
    print(f"  zero_mode_count:           {result['zero_mode_count']}")
    print(f"  |lambda|_min:              {result['abs_lambda_min']!r}")
    print(f"  |lambda|_max:              {result['abs_lambda_max']!r}")
    print(f"  ratio = lmin / lmax:       {result['ratio']!r}")

    # ---- Plot
    make_plot(result, OUT_PNG)
    print(f"  plot_written:              {OUT_PNG.name}")

    # ---- Persist data (.npz)
    np.savez(
        OUT_NPZ,
        # Bit-exact extracted scalars
        abs_lambda_min=np.float64(result["abs_lambda_min"]),
        abs_lambda_max=np.float64(result["abs_lambda_max"]),
        ratio=np.float64(result["ratio"]),
        # Counts
        zero_mode_count=np.int64(result["zero_mode_count"]),
        n_eval_raw=np.int64(result["N_eval_raw"]),
        n_positive=np.int64(result["n_positive"]),
        n_negative_in_cache=np.int64(result["n_negative_in_cache"]),
        multiplicity_weighted_total=np.int64(
            result["multiplicity_weighted_total"]
        ),
        n_sectors=np.int64(result["n_sectors"]),
        l_max_in_cache=np.int64(result["L_max_in_cache"]),
        bit_identity_step2=np.bool_(result["bit_identity_step2"]),
        # Per-level counts (object array of (L, count) tuples for round-trip)
        levels_present=np.asarray(result["levels_present"], dtype=np.int64),
        sector_count_per_level=np.asarray(
            [(L, result["sector_count_per_level"][L])
             for L in result["levels_present"]],
            dtype=np.int64,
        ),
        eval_count_per_level=np.asarray(
            [(L, result["eval_count_per_level"][L])
             for L in result["levels_present"]],
            dtype=np.int64,
        ),
        cum_count_at_level=np.asarray(
            [(L, result["cum_count_at_level"][L])
             for L in result["levels_present"]],
            dtype=np.int64,
        ),
        # Pin map (full)
        pin_canonical_constants=np.bytes_(pins.get(
            "computations/_shared/canonical_constants.py", "")),
        pin_cache_sha=np.bytes_(cache_sha_runtime),
        pre_flight_cache_sha=np.bytes_(PRE_FLIGHT_CACHE_SHA),
        cache_sha_match_pre_flight=np.bool_(sha_match),
        closure_hash=np.bytes_(closure),
        # Canonical pins echo
        tau_fold_pin=np.float64(tau_fold),
        m_kk_pin=np.float64(M_KK),
        # Pre-registered band
        info_band_lo=np.float64(INFO_BAND_LO),
        info_band_hi=np.float64(INFO_BAND_HI),
        # Identity strings
        gate_id=np.bytes_(GATE_ID),
        scheme=np.bytes_(SCHEME),
        convention=np.bytes_(CONVENTION),
    )
    print(f"  data_written:              {OUT_NPZ.name}")

    # ---- Dual-SHA closure
    audit_sha, content_sha = compute_dual_sha(
        SCRIPT_PATH, CANONICAL_PATH, pins
    )
    print(f"  audit_sha256:              {audit_sha}")
    print(f"  content_sha256:            {content_sha}")

    # ---- Verdict
    verdict, value_string = evaluate_gate(
        result["ratio"], cache_sha_runtime, PRE_FLIGHT_CACHE_SHA
    )
    line = append_verdict(
        verdict,
        value_string,
        result["zero_mode_count"],
        audit_sha,
        content_sha,
    )

    # ---- 4-tuple final line
    four_tuple = emit_4tuple(
        f"ratio={result['ratio']!r};zero_mode_count={result['zero_mode_count']}",
        SCHEME, CONVENTION, L_MAX,
    )                                                              # (local)
    print(f"  4-tuple:                   {four_tuple}")
    print(f"  verdict-line:              {line.rstrip()}")
    print(f"  VERDICT: {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
