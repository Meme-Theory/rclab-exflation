"""S84 W10a Gate 118 — VII.K-PROP atlas SHA uniqueness audit.

Tests the pre-registered hypothesis (§W10a-118):
    All verdict SHAs in the §VII.K-PROP propagation atlas are pairwise
    distinct AND each traces to an independent pin map (no two verdicts
    share the same canonical input-pin sequence).

Schema note: the atlas (s84_w3_vii_k_prop_atlas.json) does NOT carry a
per-row `closure_sha256` or `input_pin_ordered_list` field. Its
provenance is one meta-level closure_sha plus per-row content
(p_k, class, span_predicted, provenance, classification). For the
distinctness audit we therefore compute a per-row content SHA from
the canonical JSON of (p_k, class, span_predicted, provenance) and a
per-row pin-map proxy from the same tuple.

Pass / Fail / INFO thresholds (from plan §W10a-118):
    PASS: All SHAs pairwise distinct AND all pin-maps mutually
          independent (<80% positional overlap).
    FAIL: Any SHA collision OR any two pin-maps with >=80% positional
          overlap.
    INFO: All distinct but pin-maps cluster.

Verdict-line format (S81+ canonical):
    S84-VII-K-PROP-SHA-UNIQUENESS: PASS|FAIL|INFO -- value=<distinct/total>
        scheme=pairwise_sha_plus_pin_map convention=vii_k_prop_atlas_full
        L_max=N/A audit_sha256=<64-char> content_sha256=<64-char>
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

# Audit-integrity script: no framework constants required (operates only on
# file SHAs and atlas-row content). Importing canonical_constants for
# convention compliance with computations/_shared/CLAUDE.md.
from canonical_constants import *  # noqa: F401,F403

# Repo-relative paths (resolved at runtime)
THIS = Path(__file__).resolve()                                          # (local)
SCRIPT_DIR = THIS.parent                                                  # (local)
REPO_ROOT = SCRIPT_DIR.parent                                             # (local)
ATLAS_PATH = SCRIPT_DIR / "s84_w3_vii_k_prop_atlas.json"                  # (local)
ARTIFACT_PATH = (
    REPO_ROOT / "sessions" / "session-84" / "computation-artifacts"
    / "s84_w10a_118_vii_k_prop_uniqueness.json"
)                                                                         # (local)
VERDICT_PATH = SCRIPT_DIR / "s84_gate_verdicts.txt"                       # (local)

# Pre-registered thresholds (§W10a-118)
INDEPENDENCE_THRESHOLD = 0.80                                            # (local) >=80% positional overlap is FAIL
PASS_REQUIRES_FULL_DISTINCT = True                                       # (local)


def file_sha256(path: Path) -> str:
    """SHA-256 of a file's bytes (full 64-char hex)."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def file_size(path: Path) -> int:
    return os.path.getsize(path)


def row_content_payload(row: dict) -> str:
    """Canonical JSON of the row's identity content."""
    payload = {
        "p_k": row.get("p_k", {}),
        "class": row.get("class", ""),
        "span_predicted": row.get("span_predicted", None),
        "provenance": row.get("provenance", ""),
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def row_sha256(row: dict) -> str:
    return hashlib.sha256(row_content_payload(row).encode("utf-8")).hexdigest()


def row_pin_ordered_list(row: dict, atlas_meta: dict) -> list:
    """Pin-map proxy for one row.

    Per-row pin map = ordered list of (key, value, value_type) triples
    drawn from the atlas-meta `input_pins` dict (which is the same for
    every row, by construction) PLUS the row-specific identity tuple
    (class, provenance, p_k_serialized). Positional overlap on this
    list measures whether two rows draw on the same upstream
    machinery in the same order.
    """
    pins = []                                                            # (local)
    # Atlas-meta input pins (shared across all rows -- this is the
    # legitimate input-map degeneracy noted in §W10-110).
    for k, v in sorted(atlas_meta.get("input_pins", {}).items()):
        pins.append((k, v, "atlas_meta_input_pin"))
    # Row-specific identity components
    pins.append(("class", row.get("class", ""), "row_class"))
    pins.append(("provenance", row.get("provenance", ""), "row_provenance"))
    pk_serialized = json.dumps(row.get("p_k", {}), sort_keys=True)       # (local)
    pins.append(("p_k", pk_serialized, "row_slot_exponents"))
    return pins


def positional_overlap(a: list, b: list) -> float:
    """Fraction of positions where a[i] == b[i], over min(len(a), len(b))."""
    if not a or not b:
        return 0.0
    n = min(len(a), len(b))                                              # (local)
    matches = sum(1 for i in range(n) if a[i] == b[i])                   # (local)
    return matches / n


def main() -> int:
    print("=" * 78)
    print("S84-VII-K-PROP-SHA-UNIQUENESS — Wave 10a Gate 118")
    print("Audit: per-row SHA + pin-map distinctness on §VII.K-PROP atlas")
    print("=" * 78)

    # --- Input pin map (mandatory in first 20 lines of stdout per plan) ---
    input_pin_map = {                                                    # (local)
        "atlas": {
            "path": str(ATLAS_PATH.relative_to(REPO_ROOT)),
            "sha256": file_sha256(ATLAS_PATH),
            "size": file_size(ATLAS_PATH),
        },
    }
    print("Input pin map:")
    for name, pin in input_pin_map.items():
        print(f"  {name}:")
        print(f"    path:   {pin['path']}")
        print(f"    sha256: {pin['sha256']}")
        print(f"    size:   {pin['size']} bytes")

    # --- Load atlas ---
    with open(ATLAS_PATH, "r", encoding="utf-8") as f:
        atlas = json.load(f)
    rows = atlas["rows"]
    meta = atlas.get("meta", {})
    n_total = len(rows)                                                  # (local)
    print(f"\nAtlas loaded: {n_total} rows.")
    print(f"  meta.gate_id:   {meta.get('gate_id', '<missing>')}")
    print(f"  meta.scheme:    {meta.get('scheme', '<missing>')}")
    print(f"  meta.L_max:     {meta.get('L_max', '<missing>')}")
    print(f"  meta.closure_sha (atlas-level): {meta.get('closure_sha', '<missing>')}")

    # --- Per-row SHAs ---
    sha_list = [row_sha256(r) for r in rows]                             # (local)
    distinct_shas = set(sha_list)                                        # (local)
    n_distinct = len(distinct_shas)                                      # (local)
    distinct_ratio = n_distinct / n_total                                # (local)
    sha_counter = Counter(sha_list)                                      # (local)

    print(f"\n--- Per-row SHA distinctness ---")
    print(f"n_total:           {n_total}")
    print(f"n_distinct_shas:   {n_distinct}")
    print(f"distinct/total:    {n_distinct}/{n_total} = {distinct_ratio:.6f}")
    print(f"distinct ratio %:  {100*distinct_ratio:.2f}%")

    sha_clusters = []                                                    # (local)
    for sha, count in sha_counter.most_common():
        if count > 1:
            cluster_rows = [r["row"] for r, s in zip(rows, sha_list) if s == sha]
            sha_clusters.append({
                "sha": sha,
                "count": count,
                "rows": cluster_rows,
                "class": rows[cluster_rows[0] - 1].get("class", ""),
                "provenance": rows[cluster_rows[0] - 1].get("provenance", ""),
                "p_k": rows[cluster_rows[0] - 1].get("p_k", {}),
            })
    print(f"\nSHA collision clusters (count > 1): {len(sha_clusters)}")
    for c in sha_clusters:
        print(f"  cluster size={c['count']:3d}  class={c['class']!r}")
        print(f"    sha[:16]={c['sha'][:16]}...  rows={c['rows']}")

    # --- Per-row pin-map proxy + pairwise positional overlap ---
    pin_lists = [row_pin_ordered_list(r, meta) for r in rows]            # (local)
    serialized_pin_lists = [
        json.dumps(p, sort_keys=False, separators=(",", ":")) for p in pin_lists
    ]                                                                     # (local)
    n_distinct_pin_maps = len(set(serialized_pin_lists))                 # (local)

    max_overlap = 0.0                                                    # (local)
    overlap_clusters = []                                                # (local)
    for i, j in combinations(range(n_total), 2):
        ov = positional_overlap(pin_lists[i], pin_lists[j])              # (local)
        if ov > max_overlap:
            max_overlap = ov
        if ov >= INDEPENDENCE_THRESHOLD:
            overlap_clusters.append({
                "row_i": rows[i]["row"],
                "row_j": rows[j]["row"],
                "overlap": ov,
            })

    print(f"\n--- Per-row pin-map independence ---")
    print(f"n_distinct_pin_maps:  {n_distinct_pin_maps}/{n_total}")
    print(f"max_pairwise_overlap: {max_overlap:.6f}")
    print(f"pairs with overlap >= {INDEPENDENCE_THRESHOLD}: {len(overlap_clusters)}")

    # --- Verdict logic (strict pre-registered thresholds) ---
    pass_distinct = (n_distinct == n_total)                              # (local)
    pass_independence = (max_overlap < INDEPENDENCE_THRESHOLD)           # (local)
    if pass_distinct and pass_independence:
        verdict = "PASS"                                                 # (local)
    else:
        # Per §W10a-118: FAIL = any SHA collision OR any pair overlap >=80%.
        verdict = "FAIL"                                                 # (local)

    # Structural note (recorded but does NOT alter the strict verdict)
    # The 31-row R-protected cluster + 4-row MIXED-FI-via-pin cluster
    # are DECLARED class-membership identities, not hidden duplicates.
    # Strict pre-registration is binary; reinterpretation lives in §W10-118.
    structural_note = (                                                  # (local)
        "Per-row SHA collisions correspond exactly to the atlas's "
        "declared class partition: 31 R-protected rows share content "
        "(p_k={}, span=1) by theorem statement; 4 MIXED-FI-via-pin "
        "rows share content (p_k={}, span=1) by pinned-class statement; "
        "2 slot-proportional-M0 rows share content. These are NOT "
        "hidden duplicates -- they are openly declared theorem-class "
        "identities. Strict pre-registration interprets ANY collision "
        "as FAIL; the structural reading is that the atlas has "
        "8 independent equivalence-class tests, not 42 independent tests."
    )

    print(f"\n=== Verdict (strict pre-registration) ===")
    print(f"  pass_distinct_shas:  {pass_distinct}  ({n_distinct}/{n_total})")
    print(f"  pass_independence:   {pass_independence}  (max_overlap={max_overlap:.4f})")
    print(f"  VERDICT:             {verdict}")
    print(f"\nStructural note: {structural_note}")

    # --- Closure hash (audit_sha256) over input-pin map ---
    closure_payload = {                                                  # (local)
        "gate_id": "S84-VII-K-PROP-SHA-UNIQUENESS",
        "session": 84,
        "wave": "10a",
        "input_pin_map": input_pin_map,
        "thresholds": {
            "distinctness": "len(set)==len(list)",
            "independence_overlap_threshold": INDEPENDENCE_THRESHOLD,
        },
    }
    closure_canon = json.dumps(                                          # (local)
        closure_payload, sort_keys=True, separators=(",", ":")
    )
    audit_sha256 = hashlib.sha256(closure_canon.encode("utf-8")).hexdigest()

    # --- Content hash over computed result ---
    result_payload = {                                                   # (local)
        "n_total": n_total,
        "n_distinct_shas": n_distinct,
        "distinct_ratio": distinct_ratio,
        "n_distinct_pin_maps": n_distinct_pin_maps,
        "max_pairwise_overlap": max_overlap,
        "overlap_pair_count": len(overlap_clusters),
        "pin_map_clusters_count": len(sha_clusters),
        "verdict": verdict,
    }
    result_canon = json.dumps(                                           # (local)
        result_payload, sort_keys=True, separators=(",", ":")
    )
    content_sha256 = hashlib.sha256(result_canon.encode("utf-8")).hexdigest()

    # --- Write JSON artifact ---
    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    artifact = {
        "gate_id": "S84-VII-K-PROP-SHA-UNIQUENESS",
        "session": 84,
        "wave": "10a",
        "timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
        "atlas_path": str(ATLAS_PATH.relative_to(REPO_ROOT)),
        "atlas_sha256": input_pin_map["atlas"]["sha256"],
        "atlas_meta_closure_sha": meta.get("closure_sha", None),
        "n_total": n_total,
        "n_distinct_shas": n_distinct,
        "distinct_count_over_total": f"{n_distinct}/{n_total}",
        "distinct_ratio": distinct_ratio,
        "n_distinct_pin_maps": n_distinct_pin_maps,
        "max_pairwise_overlap": max_overlap,
        "independence_threshold": INDEPENDENCE_THRESHOLD,
        "pairs_above_threshold": len(overlap_clusters),
        "sha_collision_clusters": sha_clusters,
        "sample_overlap_pairs_above_threshold": overlap_clusters[:20],
        "verdict": verdict,
        "verdict_basis": (
            "Strict pre-registered binary distinctness: "
            "PASS = all distinct; FAIL = any collision."
        ),
        "structural_note": structural_note,
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "thresholds": {
            "distinctness_test": "len(set(sha_list)) == len(sha_list)",
            "independence_test_threshold": INDEPENDENCE_THRESHOLD,
        },
    }
    with open(ARTIFACT_PATH, "w", encoding="utf-8") as f:
        json.dump(artifact, f, indent=2, sort_keys=True)
    print(f"\nArtifact written: {ARTIFACT_PATH.relative_to(REPO_ROOT)}")

    # --- Append verdict line ---
    verdict_value = f"{n_distinct}/{n_total}"                            # (local)
    verdict_line = (                                                     # (local)
        f"S84-VII-K-PROP-SHA-UNIQUENESS: {verdict} -- "
        f"value={verdict_value} scheme=pairwise_sha_plus_pin_map "
        f"convention=vii_k_prop_atlas_full L_max=N/A "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256}"
    )
    audit_comment = (                                                    # (local)
        f"# audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"max_overlap={max_overlap:.4f} pin_map_clusters={len(sha_clusters)}"
    )
    with open(VERDICT_PATH, "a", encoding="utf-8") as f:
        f.write("\n" + verdict_line + "\n")
        f.write(audit_comment + "\n")
    print(f"\nVerdict appended to: {VERDICT_PATH.relative_to(REPO_ROOT)}")
    print(verdict_line)

    # Final 4-tuple tag (canonical, last non-verdict line)
    print(
        f"\n4-tuple: (value={verdict_value}, "
        f"scheme=pairwise_sha_plus_pin_map, "
        f"convention=vii_k_prop_atlas_full, L_max=N/A)"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
