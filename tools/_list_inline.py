import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')
with open('tools/knowledge-index.json') as f:
    idx = json.load(f)
eqs = idx['equations']

inline = [eq for eq in eqs if not eq.get('latex') and eq.get('type') == 'inline']
inline.sort(key=lambda x: (x['source_file'], x['line']))

for eq in inline:
    sf = os.path.basename(eq['source_file'])
    print(f"{eq['id']} | {sf}:{eq['line']}")
    print(f"  raw: {eq['raw']}")
    print()
