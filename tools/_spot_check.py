import json, sys, random, os
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/knowledge-index.json') as f:
    idx = json.load(f)
eqs = idx['equations']

random.seed(42)
sample = random.sample(eqs, 30)

mismatches = 0
checked = 0

for eq in sample:
    eid = eq['id']
    sf = eq['source_file'].replace('\\', '/')
    line = eq['line']
    raw = eq['raw']
    latex = eq.get('latex') or 'NONE'
    audit = eq.get('audit_status', 'NONE')

    # Try to read the source file
    if not os.path.exists(sf):
        print(f'[MISSING FILE] {eid} | {sf}')
        continue

    with open(sf, encoding='utf-8', errors='replace') as f2:
        lines = f2.readlines()

    # Check if raw appears at or near the indicated line
    found = False
    found_line = None
    raw_stripped = raw.strip()

    # Check exact line first
    if 0 < line <= len(lines):
        src_line = lines[line - 1].strip()
        if raw_stripped in src_line or src_line in raw_stripped:
            found = True
            found_line = line

    # If not found, check window of +/- 5
    if not found:
        for offset in range(-5, 6):
            check_line = line + offset - 1
            if 0 <= check_line < len(lines):
                src_line = lines[check_line].strip()
                if raw_stripped[:30] in src_line or src_line[:30] in raw_stripped:
                    found = True
                    found_line = line + offset
                    break

    # If still not found, do fuzzy token match
    if not found:
        raw_tokens = set(raw_stripped.split())
        for offset in range(-10, 11):
            check_line = line + offset - 1
            if 0 <= check_line < len(lines):
                src_tokens = set(lines[check_line].strip().split())
                if len(raw_tokens) > 0 and len(raw_tokens & src_tokens) / len(raw_tokens) > 0.6:
                    found = True
                    found_line = line + offset
                    break

    checked += 1
    status = 'OK' if found else 'MISMATCH'
    if not found:
        mismatches += 1
        # Show what the source actually has
        actual = ''
        if 0 < line <= len(lines):
            actual = lines[line - 1].rstrip()
        print(f'[{status}] {eid} | {sf}:{line} | audit={audit}')
        print(f'  raw:    {raw[:120]}')
        print(f'  source: {actual[:120]}')
        print()
    else:
        line_note = f' (found at line {found_line})' if found_line != line else ''
        print(f'[{status}] {eid} | {sf}:{line}{line_note} | audit={audit} | latex={"YES" if latex != "NONE" else "NO"}')

print(f'\n--- SUMMARY: {checked} checked, {mismatches} mismatches ---')
