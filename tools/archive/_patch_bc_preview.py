"""Preview Patches B + C against the audited 500 equations.

Patch B: in-loop denylist (active prefixes only — exclude entries Patch C's
regex already kills via short-RHS) + section-header-colon-suffix filter.

Patch C: LHS regex with `(` and `[` preserved as openers, `\\s` removed from
the inner character class, BUT balanced `{...}` and `(...)` groups admitted
explicitly so LaTeX subscripts like `T_{mu nu}` continue to match.

Goal: measure (a) what fraction of structural NOISE these two close on the
audited population, (b) what fraction of structural VALID they kill (false
positives). Report per-table and overall.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from collections import Counter

# Live extractor's current regex (for baseline comparison)
RE_OLD = re.compile(
    r'^[ ]{0,8}('
    r'[A-Za-z_\(\[][\w_{}\(\)\[\]\\,\s\^\']*'
    r'\s*[=≡≈]\s*'
    r'[^\n|]{5,}'
    r')$',
    re.MULTILINE,
)

# Patch C: LHS shape tightened. Removed `\s` from inner class; explicitly allow
# balanced {} and () groups (where internal whitespace is OK) as token alternatives.
# First char includes `(` and `[` so `[V_KK] = ...` and `(iii) chi = ...` openers parse.
RE_NEW = re.compile(
    r'^[ ]{0,8}('
    r'[A-Za-z_\(\[]'                          # first char
    r'(?:'
    r'    \{[^{}\n]{0,80}\}'                  # balanced { } group (whitespace OK inside)
    r'    | \([^()\n]{0,80}\)'                # balanced ( ) group (whitespace OK inside)
    r'    | [\w_{}\(\)\[\]\\,\^\']'           # any safe single char (NO \s, no `;` etc.)
    r')*'
    r'\s*[=≡≈]\s*'
    r'[^\n|]{5,}'
    r')$',
    re.MULTILINE | re.VERBOSE,
)

# Patch B: in-loop denylist of pin tokens that produce NOISE with long RHS.
# Earlier sister-Opus reasoning said `value=` was dead code under Patch C, but
# empirical preview showed `value='quoted-pin-with-internal=signs'` slips through
# because Patch C's RHS accepts quoted-string content. Reinstated.
VERDICT_PIN_PREFIXES = (
    'audit_sha256', 'content_sha256', 'closure_sha256', 'sha256',
    'convention', 'scheme', 'tier_pin', 'supersedes', 'value',
    # Still excluding OMP_NUM_THREADS, MKL_NUM_THREADS, K=, schema_version=
    # — these have short RHS that Patch C's regex rejects.
)

# Patch B sub-filter: last-word truncation. Lines ending in an auxiliary verb,
# preposition, or article (after stripping trailing punctuation) are mid-clause
# truncations of a prose paragraph that happens to contain an `=`. Closes the
# `N_C = ... is NOT an emergent algebraic relation between two independent`
# class.
PROSE_TAIL_STOPWORDS = frozenset([
    'is', 'was', 'are', 'were', 'has', 'have', 'had', 'be', 'been', 'being',
    'will', 'would', 'could', 'should', 'must', 'may', 'might',
    'the', 'a', 'an', 'of', 'in', 'at', 'to', 'from', 'on', 'by',
    'with', 'as', 'for', 'and', 'or', 'but',
])


def patch_b_kills(line: str) -> bool:
    """Returns True if Patch B rejects this line as verdict-metadata, section
    header, or mid-clause prose truncation."""
    stripped = line.rstrip()
    # Section-header colon suffix
    if stripped.endswith(':'):
        return True
    # Pin-prefix denylist
    first_tok = line.split('=', 1)[0].strip().split()[0] if '=' in line else ''
    if any(first_tok == p or first_tok.startswith(p + '=') for p in VERDICT_PIN_PREFIXES):
        return True
    # Last-word stopword (mid-clause truncation indicator)
    tail_clean = re.sub(r'[.,;:]+$', '', stripped)
    last_tok = tail_clean.split()[-1].lower() if tail_clean.split() else ''
    if last_tok in PROSE_TAIL_STOPWORDS:
        return True
    return False


def main():
    audit = json.loads(Path('tools/_anchor_validation_results.json').read_text())
    idx = json.loads(Path('tools/knowledge-index.json').read_text(encoding='utf-8'))
    eq_index = {e['id']: e for e in idx['equations']}

    # Build the structural-audited population
    structural_audited = []
    for aid, av in audit['equations'].items():
        e = eq_index[aid]
        if e['type'] != 'structural':
            continue
        structural_audited.append((aid, av['verdict'], e['raw']))

    n_noise = sum(1 for _, v, _ in structural_audited if v == 'NOISE')
    n_valid = sum(1 for _, v, _ in structural_audited if v == 'VALID')

    # Simulate Patches B + C in pipeline
    # An entry is KEPT iff: matches new regex AND not rejected by patch B
    # An entry is DROPPED iff: doesn't match new regex OR rejected by patch B
    breakdown = Counter()
    examples_valid_dropped = []
    examples_noise_kept = []

    for aid, verdict, raw in structural_audited:
        # Apply Patch C: regex match
        # We use raw (full captured text) — but the live extractor matches against
        # the SOURCE TEXT not the captured raw. Approximation: apply RE_NEW to raw.
        # Multi-line `raw` entries: try first line only since RE is MULTILINE.
        first_line = raw.split('\n', 1)[0]
        regex_match = bool(RE_NEW.match(first_line))
        patchb_kill = patch_b_kills(first_line)
        kept = regex_match and not patchb_kill

        if verdict == 'NOISE':
            if not kept:
                breakdown['noise_killed'] += 1
            else:
                breakdown['noise_kept'] += 1
                if len(examples_noise_kept) < 8:
                    examples_noise_kept.append((aid, raw[:90]))
        elif verdict == 'VALID':
            if not kept:
                breakdown['valid_killed'] += 1
                if len(examples_valid_dropped) < 12:
                    examples_valid_dropped.append((aid, raw[:90]))
            else:
                breakdown['valid_kept'] += 1

    nk, nkept = breakdown['noise_killed'], breakdown['noise_kept']
    vk, vkept = breakdown['valid_killed'], breakdown['valid_kept']

    print(f'Structural audited population: {len(structural_audited)} (NOISE={n_noise}, VALID={n_valid})')
    print()
    print(f'{"":24s} {"NOISE":>8s} {"VALID":>8s}')
    print(f'{"killed by patches":24s} {nk:>8d} {vk:>8d}')
    print(f'{"kept (still in index)":24s} {nkept:>8d} {vkept:>8d}')
    print()
    print(f'NOISE-kill rate:  {100*nk/n_noise:.1f}% ({nk}/{n_noise})')
    print(f'VALID-kill rate:  {100*vk/n_valid:.1f}% ({vk}/{n_valid})')
    print(f'Net audit-value:  killed={nk} NOISE - {vk} VALID = {nk-vk:+d}')
    print()
    print('=== VALID entries killed (false positives) — first 12 ===')
    for aid, raw in examples_valid_dropped:
        print(f'  [{aid}] {raw!r}')
    print()
    print('=== NOISE entries NOT killed (residual) — first 8 ===')
    for aid, raw in examples_noise_kept:
        print(f'  [{aid}] {raw!r}')


if __name__ == '__main__':
    main()
