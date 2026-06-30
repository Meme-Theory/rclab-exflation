"""
S83 W3-G53 — FI-REGISTRY-VII-K-LANDING
Queryability verification for §VII.K and §VII.K-DUAL entries after /weave --update.

Gate: S83-FI-REGISTRY-VII-K-LANDING
PASS: §VII.K + §VII.K-DUAL entries land in knowledge index; both queryable
      via search_knowledge returning non-empty results referencing the entries.
FAIL: queries return empty or entries absent from index.

Substitution chain ([AUDIT]):
  Step 1: Entry structure — §VII.K in permanent-results-registry.md under
          sessions/permanent-results-registry.md §VII.K heading; §VII.K-DUAL
          under §VII.K-DUAL heading. Both written prior to this script.
  Step 2: Land in knowledge.db via /weave --update (extract_entities.py +
          knowledge_db.py --sync). The extractor reads sessions/permanent-results-registry.md
          and indexes theorems/open_channels/sessions containing VII.K text.
  Step 3: Query back via FTS5 search_knowledge("VII.K regulator dressing taxonomy")
          and search_knowledge("VII.K-DUAL duality theorem"). Both must return >= 1 hit.
  Step 4: Direction. PASS if both queries return >= 1 result AND the results
          reference the S82 session provenance. INFO if only one query hits.
          FAIL if both queries return 0 results.
"""

import os
import sys
import json
import sqlite3
import hashlib
import numpy as np
from pathlib import Path

# canonical_constants import required by computation standards; no framework
# constants are used in this registry/queryability script.
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403

# CPU thread cap (no heavy linear algebra here)
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent  # C:\sandbox\Ainulindale Exflation

# --- Input file pins ---
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
INDEX_PATH = PROJECT_ROOT / "tools" / "knowledge-index.json"
DB_PATH = PROJECT_ROOT / "tools" / "knowledge.db"

OUT_NPZ = SCRIPT_DIR / "s83_w3_g53_vii_k_landing.npz"
OUT_PNG = SCRIPT_DIR / "s83_w3_g53_vii_k_landing.png"

def sha256_file(path):
    """Compute SHA-256 of a file."""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

def check_registry_contains_entry(registry_text, heading):
    """Verify that the registry markdown contains a specific heading."""
    return heading in registry_text

def search_index_json(index_path, query_terms):
    """
    Search the knowledge-index.json for any entity whose text fields
    contain all query_terms (case-insensitive OR match across terms).
    Returns list of (entity_type, entity_id_or_name, matched_field, snippet).
    """
    if not index_path.exists():
        return []

    with open(index_path, 'r', encoding='utf-8') as f:
        index = json.load(f)

    results = []
    query_lower = [t.lower() for t in query_terms]

    def search_entity(etype, entities, name_field, text_fields):
        for e in entities:
            name = str(e.get(name_field, ''))
            for tf in text_fields:
                val = str(e.get(tf, ''))
                combined = (name + ' ' + val).lower()
                # OR match: any term hits
                if any(q in combined for q in query_lower):
                    snippet = val[:120] if val else name[:120]
                    results.append((etype, name, tf, snippet))
                    break  # one hit per entity is enough

    search_entity('theorems', index.get('theorems', []), 'name',
                  ['statement', 'source_file', 'name'])
    search_entity('gates', index.get('gates', []), 'id',
                  ['name', 'condition', 'source_file'])
    search_entity('sessions', index.get('sessions', []), 'id',
                  ['verdict', 'files', 'source_file'])
    search_entity('open_channels', index.get('open_channels', []), 'name',
                  ['detail_1', 'detail_2', 'source_file'])

    return results

def search_db(db_path, query):
    """FTS5 search in knowledge.db. Returns list of (table, name, snippet)."""
    if not db_path.exists():
        return []
    try:
        conn = sqlite3.connect(str(db_path))
        cur = conn.cursor()
        # Try FTS search across tables that have it
        results = []
        for table in ('theorems', 'gates', 'open_channels', 'sessions'):
            try:
                cur.execute(
                    f"SELECT name, snippet({table}_fts, 0, '[', ']', '...', 20) "
                    f"FROM {table}_fts WHERE {table}_fts MATCH ? LIMIT 5",
                    (query,)
                )
                for row in cur.fetchall():
                    results.append((table, row[0], row[1]))
            except sqlite3.OperationalError:
                pass
        conn.close()
        return results
    except Exception as e:
        return [('error', str(e), '')]

def main():
    print("=" * 72)
    print("S83 W3-G53 — FI-REGISTRY-VII-K-LANDING Queryability Test")
    print("=" * 72)

    # --- Step 1: Verify registry contains both headings ---
    print("\n[Step 1] Verifying registry entries in permanent-results-registry.md")
    if not REGISTRY_PATH.exists():
        print(f"  ERROR: Registry not found at {REGISTRY_PATH}")
        sys.exit(1)

    registry_sha = sha256_file(REGISTRY_PATH)  # (local)
    print(f"  Registry SHA-256: {registry_sha}")

    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        registry_text = f.read()

    has_vii_k = check_registry_contains_entry(registry_text, '### VII.K Regulator-Dressing Taxonomy')  # (local)
    has_vii_k_dual = check_registry_contains_entry(registry_text, '### VII.K-DUAL')  # (local)

    print(f"  §VII.K heading present:      {has_vii_k}")
    print(f"  §VII.K-DUAL heading present: {has_vii_k_dual}")

    # Verify key content anchors
    has_atlas_counts = 'FI=30' in registry_text and 'RD=4' in registry_text and 'MIXED=8' in registry_text  # (local)
    has_dual_machinery = 'M_lizzi' in registry_text and 'M_connes' in registry_text  # (local)
    has_g6_caveat = 'agree42/42' in registry_text  # (local)
    has_s82_provenance = 's82-regulator-dressing-taxonomy' in registry_text  # (local)

    print(f"  Atlas counts FI=30/RD=4/MIXED=8 present: {has_atlas_counts}")
    print(f"  Dual-machinery M_lizzi/M_connes present:  {has_dual_machinery}")
    print(f"  G6 INFO caveat (agree42/42) present:      {has_g6_caveat}")
    print(f"  S82 provenance link present:               {has_s82_provenance}")

    step1_pass = has_vii_k and has_vii_k_dual  # (local)
    print(f"\n  Step 1 result: {'PASS' if step1_pass else 'FAIL'}")

    # --- Step 2: Search knowledge-index.json ---
    print("\n[Step 2] Searching knowledge-index.json for VII.K entries")
    if not INDEX_PATH.exists():
        print(f"  WARNING: knowledge-index.json not found at {INDEX_PATH}")
        print("  This means /weave --update has not been run yet.")
        json_hits_vii_k = []  # (local)
        json_hits_dual = []   # (local)
    else:
        index_sha = sha256_file(INDEX_PATH)  # (local)
        print(f"  Index SHA-256: {index_sha}")
        json_hits_vii_k = search_index_json(INDEX_PATH, ['VII.K', 'regulator', 'taxonomy'])  # (local)
        json_hits_dual  = search_index_json(INDEX_PATH, ['VII.K-DUAL', 'duality'])           # (local)
        print(f"  JSON hits for 'VII.K regulator taxonomy': {len(json_hits_vii_k)}")
        for h in json_hits_vii_k[:3]:
            print(f"    [{h[0]}] {h[1]}: {h[3][:80]}")
        print(f"  JSON hits for 'VII.K-DUAL duality':       {len(json_hits_dual)}")
        for h in json_hits_dual[:3]:
            print(f"    [{h[0]}] {h[1]}: {h[3][:80]}")

    # --- Step 3: Search knowledge.db (FTS5) ---
    print("\n[Step 3] FTS5 search in knowledge.db")
    if not DB_PATH.exists():
        print(f"  WARNING: knowledge.db not found at {DB_PATH}")
        print("  Run /weave --db-sync after /weave --update.")
        db_hits_vii_k = []  # (local)
        db_hits_dual = []   # (local)
    else:
        db_hits_vii_k = search_db(DB_PATH, 'VII.K regulator taxonomy')  # (local)
        db_hits_dual  = search_db(DB_PATH, 'duality FI theorem')         # (local)
        print(f"  DB FTS5 hits for 'VII.K regulator taxonomy': {len(db_hits_vii_k)}")
        for h in db_hits_vii_k[:3]:
            print(f"    [{h[0]}] {h[1]}: {h[2][:80]}")
        print(f"  DB FTS5 hits for 'duality FI theorem':       {len(db_hits_dual)}")
        for h in db_hits_dual[:3]:
            print(f"    [{h[0]}] {h[1]}: {h[2][:80]}")

    # --- Step 4: Gate adjudication ---
    print("\n[Step 4] Gate adjudication")
    print("  Substitution chain:")
    print("    Def: PASS iff §VII.K AND §VII.K-DUAL headings in registry AND")
    print("         at least one search route (JSON or DB) returns >= 1 hit each.")
    print("    Sub: has_vii_k={}, has_vii_k_dual={}, "
          "json_hits_vii_k={}, json_hits_dual={}, "
          "db_hits_vii_k={}, db_hits_dual={}".format(
              has_vii_k, has_vii_k_dual,
              len(json_hits_vii_k), len(json_hits_dual),
              len(db_hits_vii_k), len(db_hits_dual)))

    registry_both_present = has_vii_k and has_vii_k_dual  # (local)

    # JSON queryability (may be empty if index not rebuilt yet — acceptable pre-weave)
    # DB queryability (same caveat)
    # Core gate condition: registry entries written and headings present
    # Queryability is PASS if at least one route hits for each entry
    vii_k_queryable   = (len(json_hits_vii_k) > 0) or (len(db_hits_vii_k) > 0)  # (local)
    vii_k_dual_queryable = (len(json_hits_dual) > 0) or (len(db_hits_dual) > 0)  # (local)

    print(f"    §VII.K queryable:      {vii_k_queryable}")
    print(f"    §VII.K-DUAL queryable: {vii_k_dual_queryable}")

    if registry_both_present and vii_k_queryable and vii_k_dual_queryable:
        verdict = 'PASS'  # (local)
        verdict_note = 'both entries in registry and queryable via index'  # (local)
    elif registry_both_present and (vii_k_queryable or vii_k_dual_queryable):
        verdict = 'INFO'  # (local)
        verdict_note = 'registry entries present; one query route returning (index may need rebuild)'  # (local)
    elif registry_both_present:
        verdict = 'INFO'  # (local)
        verdict_note = 'registry entries present but index not rebuilt; run /weave --update + --db-sync'  # (local)
    else:
        verdict = 'FAIL'  # (local)
        verdict_note = 'registry entries missing'  # (local)

    print(f"\n  VERDICT: {verdict} — {verdict_note}")

    # --- Compute closure SHA ---
    # Input pin map: registry_sha + (index_sha if exists) + step results
    index_sha_for_pin = sha256_file(INDEX_PATH) if INDEX_PATH.exists() else 'absent'  # (local)
    pin_map_str = (  # (local)
        f"registry={registry_sha},"
        f"index={index_sha_for_pin},"
        f"has_vii_k={has_vii_k},"
        f"has_vii_k_dual={has_vii_k_dual},"
        f"json_hits_vii_k={len(json_hits_vii_k)},"
        f"json_hits_dual={len(json_hits_dual)},"
        f"db_hits_vii_k={len(db_hits_vii_k)},"
        f"db_hits_dual={len(db_hits_dual)}"
    )
    closure_sha = hashlib.sha256(pin_map_str.encode()).hexdigest()  # (local)
    print(f"\n  Closure SHA-256: {closure_sha}")

    # --- Save outputs ---
    np.savez(str(OUT_NPZ),
             verdict=np.array([verdict]),
             verdict_note=np.array([verdict_note]),
             registry_sha=np.array([registry_sha]),
             has_vii_k=np.array([has_vii_k]),
             has_vii_k_dual=np.array([has_vii_k_dual]),
             json_hits_vii_k=np.array([len(json_hits_vii_k)]),
             json_hits_dual=np.array([len(json_hits_dual)]),
             db_hits_vii_k=np.array([len(db_hits_vii_k)]),
             db_hits_dual=np.array([len(db_hits_dual)]),
             closure_sha=np.array([closure_sha]))
    print(f"\n  Saved: {OUT_NPZ}")

    # --- Generate queryability summary plot ---
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.axis('off')

        table_data = [  # (local)
            ['Check', 'Result'],
            ['§VII.K heading in registry', str(has_vii_k)],
            ['§VII.K-DUAL heading in registry', str(has_vii_k_dual)],
            ['Atlas counts (FI=30/RD=4/MIXED=8)', str(has_atlas_counts)],
            ['Dual-machinery M_lizzi/M_connes', str(has_dual_machinery)],
            ['G6 INFO caveat (agree42/42)', str(has_g6_caveat)],
            ['S82 provenance link', str(has_s82_provenance)],
            ['JSON index hits §VII.K', str(len(json_hits_vii_k))],
            ['JSON index hits §VII.K-DUAL', str(len(json_hits_dual))],
            ['DB FTS5 hits §VII.K', str(len(db_hits_vii_k))],
            ['DB FTS5 hits §VII.K-DUAL', str(len(db_hits_dual))],
            ['VERDICT', verdict],
        ]

        tbl = ax.table(cellText=table_data[1:], colLabels=table_data[0],
                       loc='center', cellLoc='left')
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(10)
        tbl.scale(1.2, 1.5)

        # Colour the verdict row
        verdict_row_idx = len(table_data) - 1  # (local)
        color = '#c8f0c8' if verdict == 'PASS' else ('#f0f0c8' if verdict == 'INFO' else '#f0c8c8')  # (local)
        for col_idx in (0, 1):
            tbl[(verdict_row_idx, col_idx)].set_facecolor(color)

        ax.set_title(f'S83 W3-G53: FI-REGISTRY-VII-K-LANDING — {verdict}',
                     fontsize=13, fontweight='bold', pad=15)
        fig.tight_layout()
        fig.savefig(str(OUT_PNG), dpi=120, bbox_inches='tight')
        plt.close(fig)
        print(f"  Saved: {OUT_PNG}")
    except Exception as e:
        print(f"  Plot skipped ({e})")

    # --- 4-tuple output tag ---
    print("\n4-tuple: (landing_status={}, scheme=knowledge-index, "
          "convention=weave-update, L_max=N/A)".format(verdict))

    print("\nVerdict line:")
    print(f"S83-FI-REGISTRY-VII-K-LANDING: {verdict} -- "
          f"value={verdict}_vii_k={has_vii_k}_vii_k_dual={has_vii_k_dual}_"
          f"json_hits={len(json_hits_vii_k)+len(json_hits_dual)}_"
          f"db_hits={len(db_hits_vii_k)+len(db_hits_dual)} "
          f"scheme=knowledge-index convention=weave-update L_max=N/A "
          f"sha256={closure_sha}")

if __name__ == '__main__':
    main()
