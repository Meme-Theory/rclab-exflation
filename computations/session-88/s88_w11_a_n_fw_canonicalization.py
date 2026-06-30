#!/usr/bin/env python3
"""
S88 W11-124 — S88-A-N-FW-CANONICALIZATION (METHODOLOGY)
========================================================

Plan §W11-124: canonical-write-order Step 2 promotion of {a_0_FW, a_2_FW}
under regulator-pin-discipline.md MANDATORY (S86 W0c-7).

This script:
  1. Verifies that `a_0_FW_zeta` and `a_2_FW_zeta` are importable from
     canonical_constants.py (Step-2 closure check).
  2. Confirms the substrate-first canonical values:
       a_0_FW_zeta = 6440.0          (S64; CCM 2007 mode count)
       a_2_FW_zeta = 2776.165389     (S42 / S46 a_2 split)
  3. Documents the Pauli-Villars and Mellin regulator-tagged variants
     as carry-forward (no substrate-first source identified at this query
     depth; promotion BLOCKED by `substrate-first-canonical-sourcing.md`
     §(v) Class-(f) PIN-PLACEHOLDER discipline).
  4. Builds dual-SHA, emits verdict line + companions to canonical
     verdict file. METHODOLOGY-class artifact-existence PASS predicate
     per `wave-classification.md §M1`.

Substitution chain (carried in WP §W11-124):
  Step 1 — Definition. a_n^X = n-th Seeley-DeWitt coefficient under
    regulator X; a_n^X = Res[Tr(D_K^{−2s}); s = (d−n)/2] · m_n
    (Connes-Moscovici 1995 §III.4).
  Step 2 — Substitution. Substrate-first canonical values from MCP
    knowledge graph + S64/S46 source records:
      a_0_FW_zeta := 6440.0         (S64, dimensionless mode count)
      a_2_FW_zeta := 2776.165389    (S42 spectral zeta sum / S46 split)
    Pauli-Villars and Mellin variants: NO substrate-first source at
    this query depth → carry-forward (S89).
  Step 3 — Simplify. count_of_promoted = 2 (single regulator each: ζ for
    both a_0 and a_2). Plan threshold PASS iff count ∈ {2, 6}.
  Step 4 — Direction. count = 2 ⇒ PASS (single-regulator-each branch
    of plan threshold).
"""

import os
import sys
import json
import hashlib
import time
from pathlib import Path

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'computations' / '_shared'))

GATE_ID = "S88-A-N-FW-CANONICALIZATION"  # (local)
SCHEME = "canonical_write_order_step2"  # (local)
CONVENTION = "mcp-knowledge-MCP-query-substrate-first"  # (local)
L_MAX = 10  # (local) plan pin (zeta-regulator at L=10 baseline)
WP_ID = "W11-124"  # (local)
SCHEMA_VERSION = "S87+"  # (local)
VERDICT_FILE = ROOT / 'computations' / 'session-88' / 's88_gate_verdicts.txt'

# Canonical values from MCP queries
EXPECTED = {  # (local) (name → (value, session, source))
    "a_0_FW_zeta": (6440.0, "S64", "session-64-results-workingpaper.md + lizzi-signature-observable.md"),
    "a_2_FW_zeta": (2776.165389, "S42", "s61_heat_kernel_a2_log.txt + s86-mellin-cone-repair-or-no-go.md"),
}


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def closure_hash_dict(d: dict) -> str:
    return hashlib.sha256(json.dumps(d, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def main():
    t0 = time.time()  # (local)
    print(f"[{GATE_ID}] METHODOLOGY canonical-write-order Step 2 verification")

    # Step 1: import canonical_constants and check the new entries
    import importlib
    import canonical_constants
    importlib.reload(canonical_constants)  # ensure latest disk state

    promoted = {}  # (local)
    missing = []  # (local)
    for name, (expected_v, sess, src) in EXPECTED.items():
        if hasattr(canonical_constants, name):
            actual_v = getattr(canonical_constants, name)
            promoted[name] = {
                "actual_value": actual_v,
                "expected_value": expected_v,
                "match": abs(actual_v - expected_v) < 1e-9,
                "session": sess,
                "source": src,
            }
            print(f"  ✓ from canonical_constants import {name}: {actual_v} (expected {expected_v}, match={promoted[name]['match']})")
        else:
            missing.append(name)
            print(f"  ✗ MISSING: {name}")

    count_promoted = len(promoted)  # (local)
    all_match = all(v["match"] for v in promoted.values())  # (local)

    # Step 2: document Pauli-Villars / Mellin carry-forward
    cf_set = []  # (local)
    for n in ["a_0", "a_2"]:
        for r in ["Pauli-Villars", "Mellin"]:
            cf_set.append(f"{n}_FW_{r}")
    print(f"\n  Carry-forward (no substrate-first source at this depth):")
    for c in cf_set:
        print(f"    - {c}: substrate-first computation pending S89")

    # Step 3: verdict
    if count_promoted == 2 and all_match and not missing:
        verdict = "PASS"
        reason = "count=2 promoted (single-regulator-each branch); both ζ-tagged values match canonical at <1e-9; PV/Mellin variants carry-forward to S89"
    elif count_promoted >= 1 and all_match:
        verdict = "INFO"
        reason = f"partial promotion {count_promoted}/2; remaining: {missing}"
    else:
        verdict = "FAIL"
        reason = f"value mismatch or missing constants; missing={missing}, all_match={all_match}"

    canonical_consts_path = ROOT / 'computations' / '_shared' / 'canonical_constants.py'
    canonical_consts_sha = file_sha256(canonical_consts_path)  # (local)

    # Build pinmap + dual-SHA
    pinmap = {  # (local)
        "_gate_id": GATE_ID,
        "_wp_id": WP_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": L_MAX,
        "promoted_count": count_promoted,
        "all_match": all_match,
        "missing": missing,
        "expected_a_0_FW_zeta": EXPECTED["a_0_FW_zeta"][0],
        "expected_a_2_FW_zeta": EXPECTED["a_2_FW_zeta"][0],
        "carry_forward_set": cf_set,
        "canonical_constants_sha": canonical_consts_sha,
    }
    audit_sha256 = closure_hash_dict(pinmap)  # (local)

    val_str = (
        f"count_of_promoted_constants={count_promoted};"
        f"a_0_FW_zeta={promoted.get('a_0_FW_zeta', {}).get('actual_value', 'MISSING')};"
        f"a_2_FW_zeta={promoted.get('a_2_FW_zeta', {}).get('actual_value', 'MISSING')};"
        f"carry_forward={'+'.join(cf_set)};reason={reason}"
    )  # (local)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{val_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={{CONTENT_SHA}} schema_version={SCHEMA_VERSION}"
    )  # (local)
    content_sha256 = hashlib.sha256(
        canonical_line.replace("{CONTENT_SHA}", "PLACEHOLDER").encode("utf-8")
    ).hexdigest()  # (local)
    canonical_line = canonical_line.replace("{CONTENT_SHA}", content_sha256)

    short_a = audit_sha256[:16]  # (local)
    short_c = content_sha256[:16]  # (local)
    companion_dualsha = (
        f"# audit_sha256_short={short_a} content_sha256_short={short_c} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"plan §W11-124 canonical-write-order Step 2; promoted "
        f"{count_promoted}/2 ζ-tagged constants; PV/Mellin variants carry-forward S89"
    )  # (local)

    sign_v = "PASS" if verdict == "PASS" else ("FAIL" if verdict == "FAIL" else "N/A")  # (local)
    mag_v = "PASS" if verdict == "PASS" else ("FAIL" if verdict == "FAIL" else "INFO")  # (local)
    regime_v = "VALID"  # (local) artifact-existence predicate is direct
    companion_3tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); "
        f"METHODOLOGY-M1-artifact-existence orchestrator-direct-write per "
        f"wave-classification.md §Dispatch consequences; allowlist append herewith"
    )  # (local)
    companion_methodology = (
        f"# methodology_class=METHODOLOGY-M1-artifact-existence "
        f"# {GATE_ID} canonical-write-order Step 2 promotion; "
        f"a_0_FW_zeta=6440.0 (S64) + a_2_FW_zeta=2776.165389 (S42/S46) added to "
        f"canonical_constants.py SECTION E with PROVENANCE entries; "
        f"rationale prose at sessions/framework/registry/methodology-wave-instances.md"
    )  # (local)

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line + "\n")
        f.write(companion_dualsha + "\n")
        f.write(companion_3tuple + "\n")
        f.write(companion_methodology + "\n")
    print(f"\n  Verdict appended to {VERDICT_FILE}")
    print(f"  audit_sha256 = {audit_sha256}")
    print(f"  content_sha256 = {content_sha256}")

    elapsed = time.time() - t0  # (local)
    print(f"  Total wall: {elapsed:.1f}s")
    print(f"  Verdict: {verdict} — {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
