"""
Session 61 BAP-5: PW Data Audit — (1,2) Irrep Contamination Scanner
====================================================================

Scans computations/_shared/ and computations/_shared/ for scripts that reference
s44_dos_tau.npz eigenvalue data and classifies each as SAFE or
CONTAMINATED based on whether it uses cross-sector PW sums that are
missing the (1,2) irrep contribution.

Background:
    s44_dos_tau.py builds its sector list from s27_multisector_bcs.py,
    which uses 9 sectors with p+q <= 3:
        (0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1)

    The (1,2) irrep (dim=15, dim^2=225, CPT-conjugate of (2,1)) is
    MISSING. s27 documents this explicitly and defines MULT_21_EFFECTIVE=450
    for its internal F_total computation. But s44_dos_tau.py does NOT
    propagate this doubling — it stores dim2=225 for (2,1) modes.

    Impact: 54,000 physical modes missing out of correct total 155,984
    (fraction = 54000/101984 = 52.95% undercount).

Contamination classification:
    CONTAMINATED: Script uses s44 dim2 weights in cross-sector sums
        (spectral action coefficients, total particle number, weighted
        averages, DOS histograms, etc.)
    SAFE: Script uses only raw eigenvalues, per-sector calculations,
        eigenvalue positions (gaps, maxima), or dim2 only as sector labels.
    UTILITY: Inspection/debug scripts with no physics output.

Gate: PW-AUDIT-61 (INFO)

Author: baptista-spacetime-analyst (Session 61, Wave 1)
Date: 2026-03-28
"""

import os
import re
import sys
from collections import defaultdict
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


# ================================================================
# 1. CONFIGURATION
# ================================================================

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# X2-removed: alias 'SHARED_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SHARED_DIR = os.path.join(PROJECT_ROOT, "computations", "_shared")

# Patterns that indicate s44 data usage
S44_PATTERNS = [
    r's44_dos_tau',
    r's44.*eigenval',
    r's27_multisector_bcs',
    r's36_sfull_tau_stabilization',
    r's43_phonon_dos',
]

# Patterns indicating cross-sector PW weighted sums (CONTAMINATED)
CONTAMINATED_PATTERNS = [
    r'np\.sum\(.*dim2',
    r'np\.average\(.*dim2',
    r'weights\s*=\s*dim2',
    r'weights\s*=\s*all_dim2',
    r'dim2\s*\*\s*',     # dim2 used as multiplicative weight
    r'\*\s*dim2',
    r'\+=\s*d2',         # accumulation via d2 (e.g., sectors[d2_int]['a0'] += d2)
    r'\+=\s*d2\s*\*',    # accumulation with d2 weight (e.g., a2 += d2 * w)
    r'sum\(.*dim2',
    r'rho_w',            # pre-weighted DOS histogram from s44
    r'rho_smooth',       # smoothed weighted DOS from s44
    r'hist_w',           # weighted histogram from s44
    r'N_cum_w',          # cumulative weighted count
    r'mean_omega_vs_tau',  # weighted mean from s44
    r'std_omega_vs_tau',   # weighted std from s44
    r'omega_rms_vs_tau',   # weighted rms from s44
    r'omega_log_vs_tau',   # weighted log-mean from s44
    r'n_physical',         # total physical mode count (101984 vs 155984)
    r'vh_rho',             # van Hove peak heights (weighted)
    r'dim2\.sum\(\)',
    r'dim2_fold\.sum',
    r'dim2_i\.sum',
]

# Patterns indicating SAFE usage (per-sector, positional, or label-only)
SAFE_PATTERNS = [
    r'omega_gap_vs_tau',     # min eigenvalue position (unweighted)
    r'omega_max_vs_tau',     # max eigenvalue position (unweighted)
    r'total_bw_vs_tau',      # bandwidth = max - min (unweighted)
    r'omin_.*_vs_tau',       # per-sector min
    r'omax_.*_vs_tau',       # per-sector max
    r'bw_.*_vs_tau',         # per-sector bandwidth
    r'vh_omega',             # van Hove positions (unweighted)
    r'vh_type',              # van Hove type labels
    r'dim2\s*==\s*\d+',     # using dim2 as sector label/mask
    r'all_omega',            # raw eigenvalue array (if not weighted)
    r'bin_centers',          # grid metadata
    r'tau_values',           # metadata
]

# Utility script patterns
UTILITY_PATTERNS = [
    r'^_inspect',
    r'^_test',
    r'^check_',
    r'^inspect_',
    r'^debug_',
]

# ================================================================
# 2. SCAN FUNCTIONS
# ================================================================

def scan_file(filepath):
    """Scan a Python file for s44 data usage and classify it."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
            lines = content.split('\n')
    except Exception as e:
        return None

    filename = os.path.basename(filepath)

    # Check if file references s44 data
    uses_s44 = False
    s44_refs = []
    for pattern in S44_PATTERNS:
        for i, line in enumerate(lines, 1):
            if re.search(pattern, line):
                uses_s44 = True
                s44_refs.append((i, line.strip(), pattern))

    if not uses_s44:
        return None

    # Check for utility scripts
    is_utility = any(re.match(pat, filename) for pat in UTILITY_PATTERNS)

    # Check for contaminated patterns
    contaminated_lines = []
    for pattern in CONTAMINATED_PATTERNS:
        for i, line in enumerate(lines, 1):
            if re.search(pattern, line):
                # Filter out false positives: comments, string literals in docstrings
                stripped = line.strip()
                if stripped.startswith('#'):
                    continue
                if stripped.startswith('"""') or stripped.startswith("'''"):
                    continue
                # Also skip lines that use rho_smooth but not from s44
                # (e.g., s54_gutzwiller_su3.py computes its own rho_smooth)
                contaminated_lines.append((i, stripped, pattern))

    # Check for safe patterns
    safe_lines = []
    for pattern in SAFE_PATTERNS:
        for i, line in enumerate(lines, 1):
            if re.search(pattern, line):
                safe_lines.append((i, line.strip(), pattern))

    # Classification logic
    if is_utility:
        classification = 'UTILITY'
        reason = 'Inspection/debug script'
    elif len(contaminated_lines) > 0:
        # Check if contaminated usage is the PRIMARY data path
        # or if dim2 is only used as a label
        label_only = True
        for _, line, pat in contaminated_lines:
            if pat in [r'dim2\s*==\s*\d+']:
                continue  # This is label usage
            # Check if this is in a comment
            if line.lstrip().startswith('#'):
                continue
            # Check for s44-derived rho_smooth vs locally-computed rho_smooth
            if 'rho_smooth' in pat:
                # Check if the file loads rho_smooth from s44 or computes its own
                if any('rho_smooth' in ref[1] and ('d44' in ref[1] or 'dos' in ref[1] or 'data[' in ref[1])
                       for ref in s44_refs + contaminated_lines):
                    label_only = False
                    break
                # If rho_smooth is computed locally (not from s44), it might be safe
                continue
            label_only = False
            break

        if label_only:
            classification = 'SAFE'
            reason = 'Uses dim2 only as sector label, not as weight'
        else:
            classification = 'CONTAMINATED'
            reason = f'{len(contaminated_lines)} PW-weighted operations found'
    else:
        classification = 'SAFE'
        reason = 'Uses only eigenvalue positions or metadata'

    return {
        'filepath': filepath,
        'filename': filename,
        'classification': classification,
        'reason': reason,
        'is_utility': is_utility,
        's44_refs': s44_refs,
        'contaminated_lines': contaminated_lines[:5],  # Top 5
        'safe_lines': safe_lines[:5],
        'n_contaminated': len(contaminated_lines),
        'n_safe': len(safe_lines),
    }


def estimate_correction(result):
    """Estimate the fractional correction magnitude for contaminated scripts."""
    if result['classification'] != 'CONTAMINATED':
        return 'N/A'

    filename = result['filename']

    # The correction depends on what kind of weighted sum is computed.
    # For sums of the form S = sum_k dim2_k * f(omega_k):
    #   - (2,1) sector has 240 modes with dim2=225, eigenvalues identical to (1,2)
    #   - Missing (1,2) adds another 240*225 = 54,000 to any dim2-weighted sum
    #   - Current total = 101,984, corrected = 155,984
    #   - Overall fractional increase = 54,000/101,984 = 52.95%
    #
    # BUT: the correction is NOT uniformly 53% for all quantities:
    #   - For weighted averages <f> = sum(dim2*f)/sum(dim2):
    #     correction depends on whether (2,1) eigenvalues are above/below mean
    #   - For per-sector quantities: no correction (SAFE)
    #   - For total counts (n_physical): exactly 53% increase
    #   - For spectral action coefficients a_n = sum(dim2 * omega^{-n}):
    #     correction depends on (2,1) eigenvalue distribution

    # Simple estimate: 53% for total-count-like quantities
    # Smaller for averaged quantities (mean, rms)
    # Larger for quantities dominated by high-multiplicity sectors

    contam_lines = ' '.join([line for _, line, _ in result['contaminated_lines']])

    if 'n_physical' in contam_lines or 'N_phys' in contam_lines or 'dim2.sum' in contam_lines:
        return '53% (total count)'
    elif 'np.sum' in contam_lines and ('beta2' in contam_lines or 'beta_sq' in contam_lines):
        return '~53% (particle number)'
    elif 'np.average' in contam_lines or 'mean' in contam_lines:
        return '~5-15% (weighted average)'
    elif 'rho_w' in contam_lines or 'rho_smooth' in contam_lines or 'hist_w' in contam_lines:
        return '~53% in (2,1) bins (DOS)'
    elif 'a0' in contam_lines or 'a2' in contam_lines or 'a4' in contam_lines:
        return '53% for a0, ~variable for a2,a4'
    else:
        return 'up to 53%'


# ================================================================
# 3. MAIN SCAN
# ================================================================

if __name__ == '__main__':
    print("=" * 80)
    print("S61 BAP-5: PW Data Audit — (1,2) Irrep Contamination Scanner")
    print("=" * 80)

    # Collect all .py files from both directories
    all_files = []
    for dirpath in [SHARED_DIR, SHARED_DIR]:
        if os.path.isdir(dirpath):
            for fname in sorted(os.listdir(dirpath)):
                if fname.endswith('.py'):
                    all_files.append(os.path.join(dirpath, fname))

    print(f"\nScanning {len(all_files)} Python files...")

    # Scan each file
    results = []
    for fpath in all_files:
        result = scan_file(fpath)
        if result is not None:
            result['correction'] = estimate_correction(result)
            results.append(result)

    # ================================================================
    # 4. REPORT
    # ================================================================

    # Count by classification
    counts = defaultdict(int)
    for r in results:
        counts[r['classification']] += 1

    print(f"\n{'='*80}")
    print("AUDIT RESULTS")
    print(f"{'='*80}")
    print(f"\nTotal scripts referencing s44 data: {len(results)}")
    print(f"  CONTAMINATED: {counts['CONTAMINATED']}")
    print(f"  SAFE:         {counts['SAFE']}")
    print(f"  UTILITY:      {counts['UTILITY']}")

    # Print contaminated scripts
    print(f"\n{'='*80}")
    print("CONTAMINATED SCRIPTS (require recomputation with (1,2) correction)")
    print(f"{'='*80}")
    print(f"\n{'Script':<50s} {'Session':<8s} {'Correction':<30s} {'Reason'}")
    print("-" * 120)
    contaminated = [r for r in results if r['classification'] == 'CONTAMINATED']
    for r in sorted(contaminated, key=lambda x: x['filename']):
        # Extract session number from filename
        session_match = re.match(r's(\d+)', r['filename'])
        session = f"S{session_match.group(1)}" if session_match else "?"
        loc = 'comp' if 'computations' in r['filepath'] else 'arch'
        name = f"{r['filename']} ({loc})"
        print(f"  {name:<50s} {session:<8s} {r['correction']:<30s} {r['reason']}")

    # Print safe scripts
    print(f"\n{'='*80}")
    print("SAFE SCRIPTS (unaffected by (1,2) omission)")
    print(f"{'='*80}")
    safe = [r for r in results if r['classification'] == 'SAFE']
    for r in sorted(safe, key=lambda x: x['filename']):
        session_match = re.match(r's(\d+)', r['filename'])
        session = f"S{session_match.group(1)}" if session_match else "?"
        loc = 'comp' if 'computations' in r['filepath'] else 'arch'
        name = f"{r['filename']} ({loc})"
        print(f"  {name:<50s} {session:<8s} {r['reason']}")

    # Print utility scripts
    print(f"\n{'='*80}")
    print("UTILITY SCRIPTS (no physics output)")
    print(f"{'='*80}")
    utility = [r for r in results if r['classification'] == 'UTILITY']
    for r in sorted(utility, key=lambda x: x['filename']):
        loc = 'comp' if 'computations' in r['filepath'] else 'arch'
        print(f"  {r['filename']} ({loc})")

    # ================================================================
    # 5. CRITICAL CONTAMINATION ASSESSMENT
    # ================================================================
    print(f"\n{'='*80}")
    print("CRITICAL CONTAMINATION ASSESSMENT")
    print(f"{'='*80}")
    print("""
Missing irrep: (1,2) with dim=15, dim^2=225, spinor_dim=240
    - CPT-conjugate of (2,1): identical eigenvalues
    - s27_multisector_bcs.py correctly defines MULT_21_EFFECTIVE = 450
    - s44_dos_tau.py does NOT propagate this doubling
    - Stored dim2 for (2,1) modes: 225 (should be 450 for full PW weight)

Impact on stored data:
    - n_physical = 101,984 (should be 155,984, undercount by 53%)
    - rho_w, rho_smooth: (2,1) bins underweighted by factor 2
    - mean_omega, omega_rms, omega_log: biased by missing (2,1) weight
    - All spectral action coefficients a_n: undercount ~53%

Correction strategy:
    Option A: Rerun s44_dos_tau.py with (1,2) added to sectors_pq
    Option B: Post-hoc correction: double the (2,1) weight in all dim2 arrays
    Both give identical results since (1,2) eigenvalues = (2,1) eigenvalues (CPT).
    Option B is simpler and does not require recomputing upstream data.
""")

    print(f"\nGate verdict: PW-AUDIT-61 INFO")
    print(f"  {len(results)} scripts scanned, {counts['CONTAMINATED']} contaminated, "
          f"{counts['SAFE']} safe, {counts['UTILITY']} utility")
