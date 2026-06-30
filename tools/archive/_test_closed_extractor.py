"""Test harness for the new _extract_closed_from_atlas_02 parser.

Runs the new canonical-source parser on atlas-02-mechanism-lifecycle.md
alone, dumps row counts per Era and sample rows, so we can iterate
quickly without paying the full /weave --update cost each cycle.

Throwaway script; safe to delete once the cleanup is verified.
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path

# Import the new parser from extract_entities
sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_entities import (
    _extract_closed_from_atlas_02,
    _extract_closed_from_permanent_results_v,
    _extract_closed_from_closed_gw_channels,
    extract_closed_mechanisms,
    PROJECT_ROOT,
)


def banner(s: str) -> None:
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)


def main() -> int:
    src = PROJECT_ROOT / "sessions" / "framework" / "Atlas" / "atlas-02-mechanism-lifecycle.md"
    if not src.exists():
        print(f"NOT FOUND: {src}", file=sys.stderr)
        return 1
    text = src.read_text(encoding="utf-8")
    print(f"Source: {src.relative_to(PROJECT_ROOT)} ({len(text):,} chars)")

    # Call the new canonical parser directly
    rows = _extract_closed_from_atlas_02(src, text)

    banner(f"DIRECT CALL: _extract_closed_from_atlas_02")
    print(f"Total rows: {len(rows)}")

    # Breakdown by era
    by_era = Counter()
    for r in rows:
        eid = r["id"].split("_era")[1].split("_")[0] if "_era" in r["id"] else "?"
        by_era[eid] += 1
    print()
    print("Per-Era row counts:")
    era_order = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII",
                 "IX", "X", "XI", "XII"]
    for era in era_order:
        n = by_era.get(era, 0)
        print(f"  Era {era:<5s}: {n:>4} rows")

    # Sample 4 rows per era for inspection
    by_era_rows = defaultdict(list)
    for r in rows:
        eid = r["id"].split("_era")[1].split("_")[0] if "_era" in r["id"] else "?"
        by_era_rows[eid].append(r)

    banner("SAMPLE ROWS — 3 per Era (first 3 per era)")
    for era in era_order:
        if era not in by_era_rows:
            continue
        print(f"\n[Era {era}]")
        for r in by_era_rows[era][:3]:
            print(f"  id={r['id']}")
            print(f"    name      : {r.get('name','')!r}")
            print(f"    session   : {r.get('session','')!r}")
            print(f"    gate_id   : {r.get('gate_id','')!r}")
            print(f"    closed_by : {(r.get('closed_by','') or '')[:70]!r}")
            print(f"    wall      : {r.get('wall','')!r}")
            if "class" in r:
                print(f"    class     : {r.get('class','')!r}")
            if "author" in r:
                print(f"    author    : {r.get('author','')!r}")

    # Quality-check assertions
    banner("QUALITY ASSERTIONS")
    issues = []

    # Era I should have 16 closures per atlas-02 line 10
    expected_era_I = 16
    if by_era.get("I", 0) != expected_era_I:
        issues.append(f"Era I count mismatch: got {by_era.get('I', 0)}, expected {expected_era_I}")

    # Era II should have 10 per line 35
    if by_era.get("II", 0) != 10:
        issues.append(f"Era II count mismatch: got {by_era.get('II', 0)}, expected 10")

    # Era III should have 7 per line 54
    if by_era.get("III", 0) != 7:
        issues.append(f"Era III count mismatch: got {by_era.get('III', 0)}, expected 7")

    # Era IV should have 15 per line 70
    if by_era.get("IV", 0) != 15:
        issues.append(f"Era IV count mismatch: got {by_era.get('IV', 0)}, expected 15")

    # Era V should have 7 per line 94
    if by_era.get("V", 0) != 7:
        issues.append(f"Era V count mismatch: got {by_era.get('V', 0)}, expected 7")

    # Era VI should have 20 sub-numbered (56.1 - 56.20) per line 110+
    if by_era.get("VI", 0) != 20:
        issues.append(f"Era VI count mismatch: got {by_era.get('VI', 0)}, expected 20")

    # Spot check: closure #1 should be "V_tree minimum" per atlas-02:14
    first_era_I = next((r for r in rows if r["id"] == "closed_atlas02_eraI_1"), None)
    if first_era_I is None:
        issues.append("closed_atlas02_eraI_1 not found")
    elif "V_tree" not in (first_era_I.get("name") or ""):
        issues.append(f"#1 expected 'V_tree minimum', got {first_era_I.get('name')!r}")

    # Spot check: closure #5 should be "Fermion condensate (Banks-Casher)" per atlas-02:18
    fifth = next((r for r in rows if r["id"] == "closed_atlas02_eraI_5"), None)
    if fifth is None:
        issues.append("closed_atlas02_eraI_5 not found")
    elif "Banks-Casher" not in (fifth.get("name") or ""):
        issues.append(f"#5 expected name with 'Banks-Casher', got {fifth.get('name')!r}")

    # Schema-1 sessions should NOT be markdown header words
    bad_sessions = []
    forbidden_session_words = {"open", "closed", "closure", "pass", "framework",
                               "theorem", "path", "pending", "gate", "estimate",
                               "insight", "untested", "true"}
    for r in rows:
        s = (r.get("session") or "").lower().strip()
        if s in forbidden_session_words:
            bad_sessions.append(r)
    if bad_sessions:
        issues.append(f"{len(bad_sessions)} rows have markdown-header-word session field")
        for r in bad_sessions[:5]:
            print(f"  ! bad session: id={r['id']} name={r['name']!r} session={r['session']!r}")

    if not issues:
        print("ALL PASSED")
    else:
        print(f"FAILURES ({len(issues)}):")
        for i in issues:
            print(f"  - {i}")

    # ==========================================================================
    # §V parser test
    # ==========================================================================
    banner("§V parser test: permanent-results-registry.md")
    pregv = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
    if not pregv.exists():
        print(f"NOT FOUND: {pregv}", file=sys.stderr)
        return 1
    text_v = pregv.read_text(encoding="utf-8")
    print(f"Source: {pregv.relative_to(PROJECT_ROOT)} ({len(text_v):,} chars)")

    rows_v = _extract_closed_from_permanent_results_v(pregv, text_v)
    print(f"Total rows: {len(rows_v)}")

    by_era_v = Counter()
    for r in rows_v:
        eid = r["id"].split("_era")[1].split("_")[0] if "_era" in r["id"] else "?"
        by_era_v[eid] += 1
    print()
    print("Per-Era row counts (§V):")
    for era in era_order:
        n = by_era_v.get(era, 0)
        print(f"  Era {era:<5s}: {n:>4} rows")

    print()
    print("Sample rows (first 3 from each Era):")
    for era in era_order:
        era_rows = [r for r in rows_v if f"era{era}_" in r["id"]][:3]
        if not era_rows:
            continue
        print(f"\n[Era {era}]")
        for r in era_rows:
            rng = " [RANGE-ROLLUP]" if r.get("range_rollup") else ""
            print(f"  id={r['id']}{rng}")
            print(f"    name      : {r.get('name','')!r}")
            print(f"    session   : {r.get('session','')!r}")
            print(f"    gate_id   : {r.get('gate_id','')!r}")
            print(f"    closed_by : {(r.get('closed_by','') or '')[:70]!r}")
            print(f"    wall      : {r.get('wall','')!r}")

    banner("§V QUALITY ASSERTIONS")
    issues_v = []

    # §V is a HEAVILY-ROLLED-UP document past Era I. The asserts validate
    # what §V's TABLE CONTENT actually has (not what its header CLAIMS).
    # Era headers say "10 closures" but the table has 6 rows (5 individual
    # + 1 range "22-26" covering 5 closures). Range-rollup detection is the
    # canonical-gap-finding signal the user predicted.
    #
    # Expected table-row counts (verified by direct source inspection at
    # permanent-results-registry.md lines 1474-1782):
    #   Era I:   16 individual rows (no rollups; full enumeration)
    #   Era II:  5 individual + 1 range "22-26"     = 6 rows total
    #   Era III: 3 individual + 1 range "30-33"     = 4 rows total
    #   Era IV:  1 individual + 1 range "35-48"     = 2 rows total
    #   Era V:   0 individual + 1 range "49-55"     = 1 row total
    #   Era VI:  0 individual + 1 range "56-75"     = 1 row total
    #   Era VII: TBD — printed below
    expected_table_rows = {"I": 16, "II": 6, "III": 4, "IV": 2,
                            "V": 1, "VI": 1}
    for era, exp in expected_table_rows.items():
        actual = by_era_v.get(era, 0)
        if actual != exp:
            issues_v.append(f"§V Era {era} table-row count mismatch: got {actual}, expected {exp}")

    # Era VII row count: 8 was observed. No header claim to assert against
    # cleanly — record the count as a diagnostic and require it be > 5
    # (so we know we caught the multi-row Era VII tables).
    actual_vii = by_era_v.get("VII", 0)
    if actual_vii < 5:
        issues_v.append(f"§V Era VII count too low: got {actual_vii}, expected > 5")

    # No Era VIII-XII rows in §V (§V stops at Era VII)
    for era in ("VIII", "IX", "X", "XI", "XII"):
        if by_era_v.get(era, 0) > 0:
            issues_v.append(f"§V Era {era} unexpectedly present: {by_era_v.get(era)}")

    # Range-rollup detection: verify rollup rows are flagged
    rollup_rows = [r for r in rows_v if r.get("range_rollup")]
    expected_rollup_count = 5  # II 22-26 + III 30-33 + IV 35-48 + V 49-55 + VI 56-75
    if len(rollup_rows) < expected_rollup_count:
        issues_v.append(f"Range-rollup detection: got {len(rollup_rows)} flagged, expected >= {expected_rollup_count}")

    # Spot check: §V #1 V_tree minimum (already-verified working in earlier run)
    first_v = next((r for r in rows_v if r["id"] == "closed_regv_eraI_1"), None)
    if first_v is None:
        issues_v.append("closed_regv_eraI_1 not found")
    elif "V_tree" not in (first_v.get("name") or ""):
        issues_v.append(f"§V #1 wrong name: {first_v.get('name')!r}")
    elif first_v.get("session") != "17a":
        issues_v.append(f"§V #1 session wrong: got {first_v.get('session')!r}, expected '17a'")
    elif first_v.get("gate_id") != "SP-4":
        issues_v.append(f"§V #1 gate_id wrong: got {first_v.get('gate_id')!r}, expected 'SP-4'")

    # Wall suffix should be stripped: §V #1 wall = "W4" not "W4 (value=..., scheme=...)"
    if first_v is not None:
        w = first_v.get("wall", "")
        if "value=" in w or "scheme=" in w or len(w) > 10:
            issues_v.append(f"§V #1 wall suffix NOT stripped: {w!r}")

    # Spot check: §V #22-26 should be flagged as range-rollup
    range_v = next((r for r in rows_v
                    if r["id"].startswith("closed_regv_eraII_22")), None)
    if range_v is None:
        issues_v.append("Era II range row '22-26' not found")
    elif not range_v.get("range_rollup"):
        issues_v.append(f"Era II row 22-26 not flagged as range-rollup")

    if not issues_v:
        print("ALL §V PASSED")
    else:
        print(f"§V FAILURES ({len(issues_v)}):")
        for i in issues_v:
            print(f"  - {i}")

    # ==========================================================================
    # closed-gw-channels parser test
    # ==========================================================================
    banner("closed-gw-channels parser test")
    gw_path = (PROJECT_ROOT / "sessions" / "framework" /
               "registry" / "closed-gw-channels.md")
    if not gw_path.exists():
        print(f"NOT FOUND: {gw_path}", file=sys.stderr)
        return 1
    text_gw = gw_path.read_text(encoding="utf-8")
    print(f"Source: {gw_path.relative_to(PROJECT_ROOT)} ({len(text_gw):,} chars)")

    rows_gw = _extract_closed_from_closed_gw_channels(gw_path, text_gw)
    print(f"Total rows: {len(rows_gw)}")

    print()
    print("All rows:")
    for r in rows_gw:
        print(f"  id={r['id']}")
        print(f"    name        : {r.get('name','')!r}")
        print(f"    claim       : {(r.get('claim','') or '')[:90]!r}")
        print(f"    closed_by   : {(r.get('closed_by','') or '')[:90]!r}")
        print(f"    consequence : {(r.get('consequence','') or '')[:90]!r}")

    banner("closed-gw-channels QUALITY ASSERTIONS")
    issues_gw = []
    # All 7 channels expected per source lines 35-65
    expected_channels = {
        "cosmic_strings_Gmu_exclusion",
        "U(1)_7_global_Goldstone_not_GW",
        "domain_wall_GW_GUT_GHz",
        "KZ_defects_0D_quench",
        "internal_domain_walls_not_4D",
        "PBH_from_strings_light_seeds",
        "LRD_demographics_not_discriminating",
    }
    actual_names = {r["name"] for r in rows_gw}
    for ch in expected_channels:
        if ch not in actual_names:
            issues_gw.append(f"Channel '{ch}' missing from extraction")

    if len(rows_gw) != 7:
        issues_gw.append(f"Expected exactly 7 channels, got {len(rows_gw)}")

    # LRD_demographics_not_discriminating should not have trailing `---`
    lrd = next((r for r in rows_gw if r["name"] == "LRD_demographics_not_discriminating"), None)
    if lrd and ("---" in lrd.get("consequence", "")):
        issues_gw.append(f"LRD consequence has unstripped trailing markers: {lrd.get('consequence')!r}")

    # Spot check: cosmic_strings has Claim/Basis/Consequence populated
    cs = next((r for r in rows_gw if r["name"] == "cosmic_strings_Gmu_exclusion"), None)
    if cs is None:
        issues_gw.append("cosmic_strings_Gmu_exclusion not found")
    elif not cs.get("claim"):
        issues_gw.append("cosmic_strings_Gmu_exclusion has empty Claim")
    elif "Gμ" not in cs.get("claim", "") and "G\\u03bc" not in repr(cs.get("claim", "")):
        issues_gw.append(f"cosmic_strings_Gmu_exclusion claim wrong: {cs.get('claim')!r}")

    if not issues_gw:
        print("ALL closed-gw-channels PASSED")
    else:
        print(f"closed-gw-channels FAILURES ({len(issues_gw)}):")
        for i in issues_gw:
            print(f"  - {i}")

    # ==========================================================================
    # Combined canonical-source summary
    # ==========================================================================
    banner("CANONICAL-SOURCE EXTRACTION SUMMARY")
    print(f"atlas-02:                {len(rows):>4} rows  (S17-S88 enumerated)")
    print(f"§V (permanent-results):  {len(rows_v):>4} rows  (S17-S62; 6 range-rollup compressing ~70 closures)")
    print(f"closed-gw-channels:      {len(rows_gw):>4} rows  (7 GW-detection channels)")
    print(f"                         ----")
    print(f"TOTAL (pre-dedup):       {len(rows) + len(rows_v) + len(rows_gw):>4} rows")
    print()
    print("§V rollups (compressed enumeration; atlas-02 enumerates these individually):")
    for r in rollup_rows:
        era = r['id'].split('era')[1].split('_')[0]
        print(f"  - §V Era {era} range={r.get('range_raw','?')}: {r.get('name','')[:70]}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
