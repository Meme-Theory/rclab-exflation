#!/usr/bin/env python3
"""One-shot check: how many entities were extracted from session-plan files?"""
from canonical_constants import *  # noqa: F401,F403
import sqlite3
conn = sqlite3.connect('tools/knowledge.db')
cur = conn.cursor()

for table in ['theorems', 'closed_mechanisms', 'open_channels', 'gates']:
    cur.execute(f"SELECT source_file FROM {table}")
    files = [r[0] for r in cur.fetchall()]
    plan_hits = 0  # (local)
    for f in files:
        if not f:
            continue
        norm = f.replace('\\', '/').lower()
        if 'session-plan' in norm or 'sessions/session-plan' in norm:
            plan_hits += 1
    print(f'{table:20s}: total={len(files):5d}  from session-plan/={plan_hits:4d}')
    if plan_hits > 0:
        cur.execute(
            f"SELECT name, source_file FROM {table} "
            f"WHERE source_file LIKE '%session-plan%' "
            f"   OR source_file LIKE '%session-plan%' "
            f"LIMIT 3"
        )
        for r in cur.fetchall():
            name = (r[0] or '')[:60]
            src = (r[1] or '')[-40:]
            print(f'  sample: {name} | ...{src}')
