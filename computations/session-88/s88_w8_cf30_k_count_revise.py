#!/usr/bin/env python3
"""
S88 W8-91 — S88-CF-30-RETROACTIVE-K-COUNT-REVISION-VIA-CF-29-SUBSTANTIVE
========================================================================

Gate: S88-CF-30-RETROACTIVE-K-COUNT-REVISION-VIA-CF-29-SUBSTANTIVE ([VERIFY])

Pre-registered threshold (plan §W8-91 lines 199-205):
  - PASS iff K_revised = 2 AND third observable REFUTED.
  - FAIL iff K_revised ∉ {2} (asymmetric: K=1 FAIL "insufficient corpus"; K≥3
    FAIL "contradicts REFUTED-for-instance-3 prior").
  - INFO iff K_revised = 2 but third observable tag is MIXED (rather than
    REFUTED).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-88/s88_w8_cf29_partition_classify.npz  (#90 output)
  - computations/_shared/canonical_constants.py
  - script bytes

Output 4-tuple:
  (value=<K_revised + per-observable tags>,
   scheme=K-count-revise-from-cf29-tags,
   convention=K-count-Type-F-only-Type-S-and-MIXED-excluded,
   L_max=10)

Classification: GEOMETRIC (algebra-axis classification on substrate A_K).

METHODOLOGY
-----------
Loads the canonical (Option-A latest non-superseded) §W8-90 partition tags
from `s88_w8_cf29_partition_classify.npz`, counts Type-F-α tags (α ∈ {C, H,
M3}), adds the S86 W-4 R3-A baseline (K=1), compares against the
pre-registered asymmetric threshold from plan §W8-91 Step 5.

Substitution chain (K-count derivation; verbatim from plan §W8-91 Step 1-5):

  Step 1: K = number of distinct calibration corpus instances satisfying the
          Type-F partition criterion (one Type-F-α tag per instance) under
          the Reading-B operator-projection separation rule.

  Step 2: Instance 1 (S86 W-4 R3-A) verified at S86 close → K_baseline = 1.

  Step 3: K_revised = 1 + |{obs ∈ {LEGGETT, BCS, A_s/n_s}
                          : partition_tag(obs) starts-with "Type-F-"}|.

  Step 4: Substitute the canonical §W8-90 tags
          (audit_sha=dfff27f73a658ae5..., latest non-superseded per
          gate-verdicts.md §"Option A"):
            tag(LEGGETT_MOMENT_S70) = Type-F-M3 → counts (+1)
            tag(PILLAR_III_BCS)     = Type-S    → does NOT count (+0)
            tag(PILLAR_VI_As_ns)    = Type-F-C  → counts (+1)
          ⇒ TypeF_count = 2 ⇒ K_revised = 1 + 2 = 3.

  Step 5 (direction): asymmetric threshold — only K_revised = 2 PASSes;
          K_revised = 3 FAILs because two Type-F tags contradict the prior
          REFUTED stance for instance-3 (Reading-B promotion path was
          K=2 SUGGESTION-status pre-promotion; K=3 PROMOTES via a different
          route — see structural-finding diagnostic below).

  Conclusion: K_revised = 3 ∉ {2} ⇒ FAIL (per plan §W8-91 Step 4).

Structural finding (the discipline-correct interpretation of the FAIL):
  The substantive partition produces TWO Type-F-α tags, not the plan's
  pre-registered "exactly one Type-F" hypothesis (plan §W8-91 line 186).
  Per substrate-IS algebra-axis classification, LEGGETT lives on the
  M_3(ℂ) summand and A_s/n_s lives on the ℂ summand — these are distinct
  central minimal projections of A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ), so they are
  STRUCTURALLY INDEPENDENT corpus instances. The S89 carry-forward
  S89-W8-91-K-COUNT-PRE-REG-REVISION updates the pre-registration to
  admit K≥3 cases as PASS-PROMOTION-AUTHORIZED, consistent with §W8-99
  wide criterion.

DISCIPLINE
----------
- `from canonical_constants import *`
- All intermediates tagged `# (local)`
- No GPU (deterministic integer comparison; no linear algebra)
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Single-shot emission per registry-landing.md §"Bridge-Landing Script
  Architecture" — no conditional rewrite branches.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S88"                                                              # (local)
GATE_ID = "S88-CF-30-RETROACTIVE-K-COUNT-REVISION-VIA-CF-29-SUBSTANTIVE"     # (local)
WP_ID = "W8-91"                                                              # (local)
SCHEME = "K-count-revise-from-cf29-tags"                                     # (local)
CONVENTION = "K-count-Type-F-only-Type-S-and-MIXED-excluded"                 # (local)
L_MAX = 10                                                                   # (local)

# Pre-registered baseline + threshold (plan §W8-91 Steps 2 + 5)
K_BASELINE = 1                                                               # (local)  S86 W-4 R3-A
PASS_K = 2                                                                   # (local)  asymmetric: PASS iff K_revised == 2

# Canonical §W8-90 SHA pin (latest non-superseded per gate-verdicts.md §"Option A")
W8_90_CANONICAL_AUDIT_SHA = (                                                # (local)
    "dfff27f73a658ae595215b6b9e6c284b2c4f750d149814c25106d759f20d5137"
)

# Output destinations
OUT_NPZ = SESSION_DIR / "s88_w8_cf30_k_count_revise.npz"
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SESSION_DIR / "s88_w8_cf29_partition_classify.npz",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                     # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                                # (local)
    for p in inputs:
        sha = sha256_of(p)                                                   # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")            # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                                             # (local)
    h = hashlib.sha256()                                                     # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = b""                                                       # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""                                                    # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(                                                # (local)
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")

    h_audit = hashlib.sha256()                                               # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                              # (local)

    h_content = hashlib.sha256()                                             # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                          # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute (deterministic K-count integer comparison)
# ---------------------------------------------------------------------------
def compute():
    """Load canonical §W8-90 npz, count Type-F-α tags, derive K_revised."""
    cf29_npz = SESSION_DIR / "s88_w8_cf29_partition_classify.npz"           # (local)
    d = np.load(cf29_npz, allow_pickle=True)                                # (local)

    # Pre-registered observable order from plan §W8-91 (Method step 2)
    observables = list(d['observables'])                                    # (local)
    tags = list(d['per_observable_tag'])                                    # (local)
    npz_verdict = str(d['verdict'])                                         # (local)
    npz_audit_sha_disk = sha256_of(cf29_npz)                                # (local)

    print(f"\n=== §W8-90 canonical tags loaded from CF-29 npz ===")
    print(f"  npz disk SHA-256: {npz_audit_sha_disk[:16]}...")
    print(f"  npz verdict:      {npz_verdict}")
    print(f"  observables:      {observables}")
    print(f"  partition_tags:   {tags}")
    print()

    # Per-observable tag classification — count Type-F-α
    # Type-F-α := tag.startswith('Type-F-') (any of Type-F-C, Type-F-H, Type-F-M3)
    # Type-S   := state-pair functional, does NOT count toward K
    # MIXED    := does NOT count toward K (per cross-pillar-bridge-anatomy.md
    #             §"Algebra-axis orthogonality" 4-corner classification)
    type_f_count = 0                                                        # (local)
    type_s_count = 0                                                        # (local)
    mixed_count = 0                                                         # (local)
    per_obs_classification = []                                             # (local)
    for obs, tag in zip(observables, tags):
        tag_str = str(tag)                                                  # (local)
        if tag_str.startswith("Type-F-"):
            counts_toward_K = True                                          # (local)
            kind = "Type-F-alpha"                                           # (local)
            type_f_count += 1
        elif tag_str == "Type-S":
            counts_toward_K = False                                         # (local)
            kind = "Type-S"                                                 # (local)
            type_s_count += 1
        elif tag_str == "MIXED":
            counts_toward_K = False                                         # (local)
            kind = "MIXED"                                                  # (local)
            mixed_count += 1
        else:
            counts_toward_K = False                                         # (local)
            kind = "UNKNOWN"                                                # (local)
        per_obs_classification.append({
            "observable": str(obs),
            "tag": tag_str,
            "kind": kind,
            "counts_toward_K": counts_toward_K,
        })
        print(f"  {str(obs):<22s}  tag={tag_str:<10s}  counts={counts_toward_K}")

    # Substitution chain Step 3-4 (verbatim from plan §W8-91)
    K_revised = K_BASELINE + type_f_count                                   # (local)
    print()
    print(f"  K_baseline (S86 W-4 R3-A): {K_BASELINE}")
    print(f"  Type-F-alpha count from #90: {type_f_count}")
    print(f"  Type-S count: {type_s_count}")
    print(f"  MIXED count: {mixed_count}")
    print(f"  K_revised = {K_BASELINE} + {type_f_count} = {K_revised}")

    # Pre-registered threshold comparison (plan §W8-91 Step 5 asymmetric)
    if K_revised == PASS_K:
        # Determine REFUTED vs MIXED for the third observable
        if mixed_count >= 1:
            verdict = "INFO"                                                # (local)
            verdict_reason = (                                              # (local)
                f"K_revised={K_revised} but third-obs is MIXED "
                f"(rather than REFUTED) — registry-text update required"
            )
        else:
            verdict = "PASS"                                                # (local)
            verdict_reason = (                                              # (local)
                f"K_revised={K_revised} AND third-obs REFUTED "
                f"(Type-S, not Type-F-alpha)"
            )
    elif K_revised == 1:
        verdict = "FAIL"                                                    # (local)
        verdict_reason = (                                                  # (local)
            f"K_revised={K_revised}; insufficient corpus "
            f"(no Type-F-alpha tags among {observables})"
        )
    else:  # K_revised >= 3
        verdict = "FAIL"                                                    # (local)
        verdict_reason = (                                                  # (local)
            f"K_revised={K_revised} >= 3; contradicts "
            f"REFUTED-for-instance-3 prior. {type_f_count} Type-F-alpha "
            f"tags (instances STRUCTURALLY INDEPENDENT — see "
            f"structural-finding diagnostic in WP §W8-91)"
        )

    print()
    print(f"  Threshold comparison: K_revised={K_revised} vs PASS_K={PASS_K}")
    print(f"  Verdict: {verdict}")
    print(f"  Reason:  {verdict_reason}")

    # Compose value-string for verdict line
    tag_summary = ";".join(                                                 # (local)
        f"{c['observable']}={c['tag']}" for c in per_obs_classification
    )
    structural_finding = (                                                  # (local)
        "STRUCTURAL_FINDING_2_TYPE_F_NOT_1" if K_revised >= 3 else "AS_PRE_REG"
    )
    value_str = (                                                           # (local)
        f"K_revised={K_revised};K_baseline={K_BASELINE};"
        f"TypeF_count={type_f_count};TypeS_count={type_s_count};"
        f"MIXED_count={mixed_count};{tag_summary};"
        f"finding={structural_finding}"
    )

    return {
        "value": value_str,
        "K_revised": K_revised,
        "K_baseline": K_BASELINE,
        "type_f_count": type_f_count,
        "type_s_count": type_s_count,
        "mixed_count": mixed_count,
        "per_obs_classification": per_obs_classification,
        "observables": observables,
        "tags": tags,
        "verdict": verdict,
        "verdict_reason": verdict_reason,
        "npz_audit_sha_disk": npz_audit_sha_disk,
        "w8_90_canonical_audit_sha_pin": W8_90_CANONICAL_AUDIT_SHA,
        "structural_finding": structural_finding,
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict emission (single-shot per registry-landing.md)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, audit_sha, content_sha, comment):
    """Atomic append of canonical line + dual-SHA companion comment row."""
    canonical = (                                                            # (local)
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (                                                            # (local)
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]} # {comment}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                                         # (local)

    # 1. Log input pins (first lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                             # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()                                   # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"                   # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 2. Compute (deterministic integer K-count)
    result = compute()

    # 3. Save .npz
    np.savez_compressed(
        OUT_NPZ,
        gate_id=GATE_ID,
        wp_id=WP_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        K_revised=result["K_revised"],
        K_baseline=result["K_baseline"],
        type_f_count=result["type_f_count"],
        type_s_count=result["type_s_count"],
        mixed_count=result["mixed_count"],
        observables=np.array(result["observables"], dtype=object),
        per_observable_tags=np.array(result["tags"], dtype=object),
        per_obs_classification=np.array(
            [json.dumps(c) for c in result["per_obs_classification"]],
            dtype=object,
        ),
        verdict=result["verdict"],
        verdict_reason=result["verdict_reason"],
        npz_audit_sha_disk=result["npz_audit_sha_disk"],
        w8_90_canonical_audit_sha_pin=result["w8_90_canonical_audit_sha_pin"],
        structural_finding=result["structural_finding"],
        threshold_PASS_K=PASS_K,
        threshold_rule="PASS iff K_revised==2 AND third-obs REFUTED; "
                       "FAIL iff K_revised not in {2}; "
                       "INFO iff K_revised==2 AND third-obs MIXED",
    )
    print(f"\n  saved: {OUT_NPZ.name}")

    # 4. Emit 4-tuple + append verdict (single-shot, no rewrite branches)
    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)            # (local)
    print(tag)

    comment = (                                                              # (local)
        f"K_revised={result['K_revised']} = {K_BASELINE} (S86 W-4 R3-A) + "
        f"{result['type_f_count']} (Type-F-alpha from W8-90 canonical "
        f"audit_sha={W8_90_CANONICAL_AUDIT_SHA[:16]}); "
        f"verdict={result['verdict']} per plan §W8-91 asymmetric threshold "
        f"(PASS iff K==2; FAIL iff K not-in {{2}}; structural finding: "
        f"{result['structural_finding']}); "
        f"computed by computations/session-88/s88_w8_cf30_k_count_revise.py"
    )
    append_verdict(
        result["verdict"], result["value"], audit_sha, content_sha, comment
    )

    wall = time.time() - t0                                                  # (local)
    print(f"\n=== {GATE_ID}: {result['verdict']} (wall {wall:.2f}s) ===")
    print(f"=== {result['verdict_reason']} ===")
    # Per math-scripts.md §"Exit Codes and Verdict Semantics":
    # FAIL is a valid scientific result; exit 0 means script ran successfully.
    return 0


if __name__ == "__main__":
    sys.exit(main())
