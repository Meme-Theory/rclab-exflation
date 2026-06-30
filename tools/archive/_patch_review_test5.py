"""Resolve the handoff/Haiku disagreement on 'In d = n+1 spacetime dimensions'."""
import json
from pathlib import Path

ROOT = Path('C:/sandbox/Ainulindale Exflation')
idx = json.loads((ROOT / 'tools/knowledge-index.json').read_text(encoding='utf-8'))
audit = json.loads((ROOT / 'tools/_anchor_validation_results.json').read_text())

for e in idx['equations']:
    if 'In d = n+1 spacetime dimensions' in e['raw']:
        verdict = audit['equations'].get(e['id'], {}).get('verdict', '?')
        comment = audit['equations'].get(e['id'], {}).get('comment', '')
        print(f"[{e['id']}] verdict={verdict} type={e['type']}")
        print(f"  src: {e['source_file']}:{e['line']}")
        print(f"  raw: {e['raw']!r}")
        print(f"  comment: {comment}")
        # Read context from source file
        src_path = ROOT / e['source_file'].replace('\\', '/')
        try:
            src_text = src_path.read_text(encoding='utf-8', errors='replace')
            lines = src_text.split('\n')
            ln = e['line']
            print('--- source context (±5 lines) ---')
            for i in range(max(0, ln - 6), min(len(lines), ln + 6)):
                marker = '*' if i + 1 == ln else ' '
                print(f"  {marker} {i+1:5d}: {lines[i][:160]}")
        except Exception as ex:
            print(f"  (could not read source: {ex})")
        print()
