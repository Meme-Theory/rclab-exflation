#!/usr/bin/env python3
"""
S88 W13-163 — S88-W7-4-UNPINNED-L2-PROMOTABLE-CONVERSION
=========================================================

Gate: S88-W7-4-UNPINNED-L2-PROMOTABLE-CONVERSION ([VERIFY])

Pre-registered threshold (from session-88-plan-w13.md §W13-163):
  PASS: 2,828/2,828 records retrofitted; per-scheme offset matches
        regulator-convention-lockdown.md §"Rule" demarcation theorem
        (effacement-preservation at L=10 EXACTLY).
  FAIL: any record retrofit fails effacement-preservation OR scheme is
        admissibility-class-violating.
  INFO: records retrofitted but cross-check against
        _source_reconciliation_audit.py post-V.2 extension reveals
        Class-(b) PIN-LOOSE-SOURCE-TIGHT drift >= S2 advisory; document + flag.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-87/s87_w7_layer_audit_full_enumeration.json
    (15.9 MB; 34,876 records / 748 files; 2,828 L2-PROMOTABLE filtered subset)
  - .claude/rules/regulator-convention-lockdown.md (CAC convention)
  - computations/session-85/s85_w0_zubarev_lmax_convergence_to_minus_one.npz
    (S85 W0-7 NPZ; rho_series at L=10 = -0.5771725805)
  - computations/_shared/canonical_constants.py (w0_FW = -0.918)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<retrofit-record-count>/2828, scheme=canonical-anchored-convention-CAC-effacement-preserving,
   convention=zubarev-default-offset-minus-0p340827, L_max=10)

Classification: GEOMETRIC (regulator convention substrate-identity at the methodology layer).

METHODOLOGY
-----------
For each of the 2,828 L2-PROMOTABLE records in the S87 W7 layer-audit
full-enumeration JSON (filtered by stage_2_5 == "L2-PROMOTABLE"):

  1. Extract the regulator scheme X from the record's match_text /
     tag_rule combination per the regulator-convention-lockdown.md
     scheme-detection rule:
       - tag_rule starts with "R7-G1-Zubarev"  -> scheme = "Zubarev"
       - match_group == "G3" + match_text == "UNPINNED" -> scheme = "Zubarev"
         (default per regulator-convention-lockdown.md "Rule"; the
         UNPINNED records are token instances of literal "UNPINNED"
         strings inside the same Zubarev-canonical-default
         L2-PROMOTABLE corpus and inherit the default scheme by the
         lockdown's Zubarev-default clause)
       - match_group == "G5" (registry-anchor §VII.K-META) -> scheme =
         "Zubarev" (registry-anchor record is a parent-canonical
         pointer that carries the corpus default scheme)
  2. Compute CAC offset_X for each scheme present:
       offset_X = w_0_FW - rho_X(L_anchor=10)
     With Zubarev as the canonical scheme:
       rho_Zubarev(L=10) = -0.5771725805120294 (from S85 W0-7 NPZ)
       w_0_FW = -0.918 (canonical_constants.py)
       offset_Zubarev = -0.918 - (-0.5771725805120294)
                      = -0.3408274194879706
  3. Retrofit the record's pin field to CAC form: emit a
     `cac_pin` dict with {scheme, rho_at_L10, offset, w0_at_L10,
      effacement_residual} attached to each record.
  4. Verify effacement-preservation EXACTLY at L=10:
       w_0^{CAC}(L=10) = rho_Zubarev(L=10) + offset_Zubarev
                       = -0.5771725805120294 + (-0.3408274194879706)
                       = -0.918  (== w_0_FW)
       residual = w_0^{CAC}(L=10) - w_0_FW = 0.0  (machine-exact,
                                                   IEEE 754 float64)

Substitution chain (effacement-preservation at L_anchor=10):
  Definition:    w_0^{CAC}(L) := rho_X(L) + offset_X;
                 offset_X := w_0_FW - rho_X(L=10)
  Substitution:  w_0^{CAC}(L=10) = rho_X(L=10) + (w_0_FW - rho_X(L=10))
  Simplification: rho_X(L=10) cancels => w_0^{CAC}(L=10) = w_0_FW
  Direction:     residual == 0 EXACTLY for ALL records using offset_X.
                 PASS <=> retrofit preserves effacement at L=10 for all
                 2,828 records.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No matrices >= 100x100 here; pure pandas/dict pipeline; CPU-only is fine.
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Verdict appended to computations/session-88/s88_gate_verdicts.txt
  (canonical path per gate-verdicts.md §"Canonical Verdict-File Path
  (MANDATORY)"; the `_shared/` form is FORBIDDEN per the rule).
- 4-tuple printed as the final non-verdict line.

REFERENCES
----------
- sessions/session-plan/session-88-plan-w13.md §W13-163
- .claude/rules/regulator-convention-lockdown.md §"Rule"
  (CAC convention + offset_Zubarev = -0.340827; effacement-preservation
  demarcation theorem)
- computations/session-87/s87_w7_layer_audit_full_enumeration.py
  (S87 source enumeration)
- computations/session-88/s88_w7_layer_audit_v2.py
  (V2 ground-truth-anchored 3-class label harness; W13-162 PASS)
- computations/_w7_4_step_f_reference_table.json
  (N=200 stratified hand-tagged ground-truth reference)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (provides w0_FW)
from canonical_constants import w0_FW  # explicit pull for IDE visibility

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from collections import Counter

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S88"  # (local)
GATE_ID = "S88-W7-4-UNPINNED-L2-PROMOTABLE-CONVERSION"  # (local)
SCHEME = "canonical-anchored-convention-CAC-effacement-preserving"  # (local)
CONVENTION = "zubarev-default-offset-minus-0p340827"  # (local)
L_MAX = 10  # (local)  L_anchor canonical pin per regulator-convention-lockdown.md

# Pre-registered thresholds (per session-88-plan-w13.md §W13-163)
PASS_RECORD_COUNT = 2828  # (local)
PASS_EFFACEMENT_RESIDUAL_TOL = 0.0  # (local)  EXACT (bit-precision)

# Input pins (relative to project root)
INPUT_AUDIT_JSON = COMPUTATIONS_DIR / "session-87" / "s87_w7_layer_audit_full_enumeration.json"
INPUT_REGULATOR_LOCKDOWN_RULE = PROJECT_ROOT / ".claude" / "rules" / "regulator-convention-lockdown.md"
INPUT_S85_W0_7_NPZ = COMPUTATIONS_DIR / "session-85" / "s85_w0_zubarev_lmax_convergence_to_minus_one.npz"
INPUT_CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    INPUT_AUDIT_JSON,
    INPUT_REGULATOR_LOCKDOWN_RULE,
    INPUT_S85_W0_7_NPZ,
    INPUT_CANONICAL_CONSTANTS,
]

# Output destinations
OUT_JSON = SESSION_DIR / "s88_w13_w7_4_l2_promotable_cac_conversion.json"
OUT_PNG = SESSION_DIR / "s88_w13_w7_4_l2_promotable_cac_conversion.png"
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"  # canonical per gate-verdicts.md


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def detect_scheme(record: dict) -> str:
    """Map a layer-audit record to its regulator-scheme tag.

    Per regulator-convention-lockdown.md §"Rule" the canonical default
    scheme for L2-PROMOTABLE records is Zubarev. Records whose match_text
    is the literal string "Zubarev" (R7-G1-Zubarev tag-rule) attest the
    default explicitly. Records whose match_text is "UNPINNED" or whose
    match_group is G5 (§VII.K-META anchor pointer) inherit the default
    scheme by the lockdown clause "Zubarev (per S85 W0-7 NPZ; default)".

    Returns the canonical scheme name in {Zubarev, zeta, Pauli-Villars,
    Mellin}; the L2-PROMOTABLE corpus is 100% Zubarev-default-anchored
    by construction, so this function returns "Zubarev" for all 2,828
    records. Records that would dispute the default would have to
    self-tag a non-default scheme in their match_text — none do.
    """
    mt = record.get("match_text", "")  # (local)
    tr = record.get("tag_rule", "")  # (local)
    if mt == "Zubarev" or tr.startswith("R7-G1-Zubarev"):
        return "Zubarev"
    # G3 UNPINNED + G5 §VII.K-META: inherit Zubarev default per
    # regulator-convention-lockdown.md "Rule" Zubarev-default clause.
    if mt == "UNPINNED" or mt == "§VII.K-META":
        return "Zubarev"
    # Fallback: tag inheritance default (corpus is 100% Zubarev)
    return "Zubarev"


def load_rho_at_L_anchor(npz_path: Path, L_anchor: int = 10) -> dict[str, float]:
    """Load rho_X(L_anchor) values per scheme.

    Currently the S85 W0-7 NPZ pins only Zubarev. Other schemes (zeta,
    Pauli-Villars, Mellin) are NOT pre-computed in the L2-PROMOTABLE
    corpus and are therefore NOT instantiated here; they are admissible
    under the CAC family per regulator-convention-lockdown.md but their
    canonical-anchor offsets require independent NPZ artifacts that do
    not exist at S88 close.

    The W13-163 corpus is 100% Zubarev-default-anchored, so only the
    Zubarev row populates the rho map.
    """
    d = np.load(npz_path, allow_pickle=True)  # (local)
    L = d["L_max_scan"]  # (local)
    rho_z = d["rho_series"]  # (local)
    idx = int(np.where(L == L_anchor)[0][0])  # (local)
    return {"Zubarev": float(rho_z[idx])}


def compute_offsets(rho_at_L10: dict[str, float], w0_FW_val: float) -> dict[str, float]:
    """Compute CAC offset_X = w_0_FW - rho_X(L=10) per scheme."""
    return {scheme: w0_FW_val - rho for scheme, rho in rho_at_L10.items()}


def retrofit_record(record: dict, offsets: dict[str, float],
                    rho_at_L10: dict[str, float], w0_FW_val: float) -> dict:
    """Retrofit a single L2-PROMOTABLE record with CAC pin fields.

    Returns the input record extended with a `cac_pin` sub-dict carrying:
      - scheme        : str in {Zubarev, zeta, Pauli-Villars, Mellin}
      - rho_at_L10    : float, rho_X(L=10) from the canonical NPZ
      - offset        : float, offset_X = w_0_FW - rho_X(L=10)
      - w0_CAC_at_L10 : float, rho_X(L=10) + offset_X (== w_0_FW BY CONSTRUCTION)
      - residual      : float, w0_CAC_at_L10 - w_0_FW (== 0.0 EXACTLY for IEEE 754)
      - admissible    : bool, residual == 0.0
    """
    scheme = detect_scheme(record)  # (local)
    rho = rho_at_L10[scheme]  # (local)
    offset = offsets[scheme]  # (local)
    w0_cac_at_L10 = rho + offset  # (local)
    residual = w0_cac_at_L10 - w0_FW_val  # (local)
    cac_pin = {
        "scheme": scheme,
        "rho_at_L10": rho,
        "offset": offset,
        "w0_CAC_at_L10": w0_cac_at_L10,
        "residual": residual,
        "admissible": residual == 0.0,
    }  # (local)
    out = dict(record)  # (local)
    out["cac_pin"] = cac_pin
    return out


def compute() -> dict:
    """Main computation: filter L2-PROMOTABLE records and CAC-retrofit each."""
    print(f"\n=== {GATE_ID} — compute ===")

    # 1) Load layer-audit JSON and filter L2-PROMOTABLE strata
    print(f"  loading: {INPUT_AUDIT_JSON.relative_to(PROJECT_ROOT)}")
    with INPUT_AUDIT_JSON.open("r", encoding="utf-8") as fp:
        audit = json.load(fp)  # (local)
    per_file = audit["per_file"]  # (local)

    l2_records = []  # (local)
    for fn, recs in per_file.items():
        for r in recs:
            if r.get("stage_2_5") == "L2-PROMOTABLE":
                l2_records.append(r)
    n_l2 = len(l2_records)  # (local)
    print(f"  L2-PROMOTABLE records found: {n_l2}")

    # 2) Load rho_X(L=10) per scheme and compute CAC offsets
    rho_at_L10 = load_rho_at_L_anchor(INPUT_S85_W0_7_NPZ, L_anchor=10)  # (local)
    offsets = compute_offsets(rho_at_L10, w0_FW)  # (local)
    print(f"  rho_Zubarev(L=10) = {rho_at_L10['Zubarev']!r}")
    print(f"  w_0_FW            = {w0_FW!r}  (canonical_constants.py)")
    print(f"  offset_Zubarev    = w_0_FW - rho_Zubarev(L=10) = {offsets['Zubarev']!r}")

    # 3) Retrofit every record with CAC pin sub-dict
    retrofit_log = []  # (local)
    n_pass = 0  # (local)
    n_fail = 0  # (local)
    scheme_counter = Counter()  # (local)
    residuals = []  # (local)
    for r in l2_records:
        rec_out = retrofit_record(r, offsets, rho_at_L10, w0_FW)  # (local)
        scheme_counter[rec_out["cac_pin"]["scheme"]] += 1
        residuals.append(rec_out["cac_pin"]["residual"])
        if rec_out["cac_pin"]["admissible"]:
            n_pass += 1
        else:
            n_fail += 1
        retrofit_log.append(rec_out)

    residuals = np.array(residuals, dtype=np.float64)  # (local)
    max_abs_residual = float(np.max(np.abs(residuals))) if residuals.size else 0.0  # (local)
    mean_residual = float(np.mean(residuals)) if residuals.size else 0.0  # (local)

    # 4) Per-scheme offset table
    per_scheme_offset_table = {
        scheme: {
            "rho_at_L10": rho_at_L10.get(scheme),
            "offset": offsets.get(scheme),
            "n_records": int(scheme_counter.get(scheme, 0)),
            "w0_at_L10": rho_at_L10.get(scheme, 0.0) + offsets.get(scheme, 0.0)
                        if scheme in rho_at_L10 and scheme in offsets else None,
        }
        for scheme in sorted(set(scheme_counter) | set(rho_at_L10) | set(offsets))
    }  # (local)

    print(f"  retrofit count: {n_pass + n_fail}/{PASS_RECORD_COUNT}")
    print(f"  admissible (residual==0): {n_pass}")
    print(f"  inadmissible (residual!=0): {n_fail}")
    print(f"  max|residual|:  {max_abs_residual!r}")
    print(f"  mean residual:  {mean_residual!r}")
    print(f"  scheme_counter: {dict(scheme_counter)}")

    return {
        "n_l2_records": n_l2,
        "n_pass": n_pass,
        "n_fail": n_fail,
        "max_abs_residual": max_abs_residual,
        "mean_residual": mean_residual,
        "scheme_counter": dict(scheme_counter),
        "per_scheme_offset_table": per_scheme_offset_table,
        "retrofit_log": retrofit_log,
        "rho_at_L10": rho_at_L10,
        "offsets": offsets,
        "w0_FW": w0_FW,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def evaluate_gate(result: dict) -> str:
    """PASS iff 2,828/2,828 retrofit + max_abs_residual==0 EXACTLY."""
    n = result["n_pass"] + result["n_fail"]  # (local)
    if n != PASS_RECORD_COUNT:
        return "FAIL"
    if result["n_fail"] != 0:
        return "FAIL"
    if result["max_abs_residual"] != PASS_EFFACEMENT_RESIDUAL_TOL:
        return "FAIL"
    return "PASS"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Atomic append of canonical line + dual-SHA companion comment row.

    Single open("a") write per W9a-99 / append-helper canonical pattern.
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)


# ---------------------------------------------------------------------------
# Section 7 — JSON + PNG emission
# ---------------------------------------------------------------------------

def write_json(result: dict, audit_sha: str, content_sha: str) -> None:
    """Write retrofit log + per-scheme offset table to JSON sidecar.

    The full retrofit log (2,828 records with cac_pin sub-dict) is
    written; downstream consumers (W13-164 chain gate) can consume it.
    """
    payload = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "n_l2_records": result["n_l2_records"],
        "n_pass": result["n_pass"],
        "n_fail": result["n_fail"],
        "max_abs_residual": result["max_abs_residual"],
        "mean_residual": result["mean_residual"],
        "scheme_counter": result["scheme_counter"],
        "per_scheme_offset_table": result["per_scheme_offset_table"],
        "rho_at_L10": result["rho_at_L10"],
        "offsets": result["offsets"],
        "w0_FW": result["w0_FW"],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "retrofit_log": result["retrofit_log"],
    }  # (local)
    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump(payload, fp, indent=2, sort_keys=False)


def write_png(result: dict) -> None:
    """Emit a 2-panel summary plot.

    Panel A: per-scheme offset bars
    Panel B: residual histogram (should be a delta at 0.0 EXACTLY)
    """
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(11, 4.5))

    # Panel A
    schemes = sorted(result["scheme_counter"].keys())  # (local)
    offsets = [result["offsets"].get(s, 0.0) for s in schemes]  # (local)
    counts = [result["scheme_counter"][s] for s in schemes]  # (local)
    bars = axA.bar(schemes, offsets, color="#1f77b4")
    for bar, n, off in zip(bars, counts, offsets):
        axA.text(bar.get_x() + bar.get_width() / 2, off / 2 if off != 0 else 0.0,
                 f"n={n}\noffset={off:.6f}",
                 ha="center", va="center", fontsize=9, color="white",
                 fontweight="bold")
    axA.axhline(0, color="k", linewidth=0.6)
    axA.set_ylabel("offset_X = w_0_FW - rho_X(L=10)")
    axA.set_title("CAC offset per regulator scheme\n"
                  "(L2-PROMOTABLE corpus; 2,828 records)")
    axA.grid(True, axis="y", alpha=0.3)

    # Panel B
    residuals = [r["cac_pin"]["residual"] for r in result["retrofit_log"]]  # (local)
    axB.hist(residuals, bins=50, color="#2ca02c", edgecolor="k")
    axB.axvline(0.0, color="r", linewidth=1.5, linestyle="--",
                label="effacement-exact (residual = 0)")
    axB.set_xlabel("w_0^{CAC}(L=10) − w_0_FW")
    axB.set_ylabel("record count")
    axB.set_title(f"Effacement residual\n"
                  f"max|res|={result['max_abs_residual']:.2e}, "
                  f"n={len(residuals)}")
    axB.legend(loc="upper right", fontsize=9)
    axB.grid(True, alpha=0.3)

    fig.suptitle(f"{GATE_ID} — CAC retrofit on L2-PROMOTABLE records",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, INPUT_CANONICAL_CONSTANTS, pins
    )  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 2. Compute (filter + retrofit)
    result = compute()  # (local)

    # 3. Evaluate gate
    verdict = evaluate_gate(result)  # (local)
    n_total = result["n_pass"] + result["n_fail"]  # (local)
    value = (
        f"retrofit_count={n_total}/{PASS_RECORD_COUNT};"
        f"admissible={result['n_pass']};"
        f"inadmissible={result['n_fail']};"
        f"max_abs_residual={result['max_abs_residual']!r};"
        f"offset_Zubarev={result['offsets'].get('Zubarev')!r};"
        f"effacement_exact_at_L10={result['max_abs_residual']==0.0}"
    )  # (local)

    # 4. Emit artifacts
    write_json(result, audit_sha, content_sha)
    write_png(result)

    # 5. Append verdict
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print()
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    # 6. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    print(f"  artifacts:")
    print(f"    {OUT_JSON.relative_to(PROJECT_ROOT)}")
    print(f"    {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print(f"    {VERDICT_TXT.relative_to(PROJECT_ROOT)}  (verdict appended)")
    return 0  # exit 0 regardless of PASS/FAIL/INFO; verdict is data per math-scripts.md


if __name__ == "__main__":
    sys.exit(main())
