#!/usr/bin/env python3
"""
S83 W3-G59 -- SHA-COLLISION-AUDIT
================================================================
Gate: S83-SHA-COLLISION-AUDIT ([AUDIT], NON-PHONONIC)

HYPOTHESIS: The S82 verdict SHAs for W1-1-TD, W2-13, W3-7 are unique AND
auditable (no duplicate signifying copy-paste).

  PASS: all 3 SHAs distinct AND each recomputes correctly from the
        independently-reconstructed input-pin map of its producing script.
  FAIL: any duplicate SHA (copy-paste signature) OR any mismatch between
        recorded SHA and the SHA recomputed from the input-pin map.

INPUTS:
  - computations/session-82/s82_gate_verdicts.txt  (recorded SHAs)
  - computations/session-82/s82_w1_1_h_tilde_td.py (W1-1-TD producing script)
  - computations/session-82/s82_w2_13_f0_convention_audit.py (W2-13 producing script)
  - computations/session-82/s82_w3_7_ej_convention_audit.py (W3-7 producing script)
  - computations/_shared/canonical_constants.py (shared input dependency)

4-tuple output:
  (value=<distinct_count>/3, scheme=S82-verdict-SHAs,
   convention=sha256-input-pin-map, L_max=N/A)

Classification: NON-PHONONIC (computation-audit hygiene)

METHODOLOGY
-----------
The S81+ gate-verdict discipline requires every verdict line to carry a
SHA-256 closure hash:

    closure = sha256( concat( sorted{ f"{relpath}={sha256_of(file)}\n" } ) )

where the set iterates the `INPUT_FILES` list inside the producing script.
The closure therefore encodes:
  (a) which files were INPUTS to the computation, and
  (b) the content of each input at the moment the script ran.

A SHA collision between TWO DIFFERENT GATES implies that both producing
scripts declared the same INPUT_FILES list and read identical byte content
at run time. This is NOT a cryptographic anomaly -- SHA-256 does not
spontaneously collide at 2^128 work factor -- it is a STRUCTURAL PROPERTY
of the scripts: identical input-pin maps by construction.

This is EXPECTED and HARMLESS when the scripts genuinely share the same
input dependency (e.g., all three read only canonical_constants.py), but
it breaks the AUDITABILITY goal of the closure SHA: a reader cannot
distinguish which verdict came from which gate by SHA alone.

THE DISTINCTION THAT MATTERS for this audit:

  (1) "Copy-paste signature" = the verdict line's SHA was HARDCODED into
      the script text (not computed from the input-pin map at runtime).
      Detection: the recorded SHA does NOT recompute from the declared
      INPUT_FILES list.

  (2) "Input-map coincidence" = two gates legitimately share the same
      input-pin map because they depend on exactly the same files.
      Detection: the recorded SHA DOES recompute from the declared
      INPUT_FILES list, AND the INPUT_FILES lists are identical across
      the gates in question.

Pre-registered rule:
  - If any of the three SHAs FAIL to recompute from the declared input
    map -> FAIL (copy-paste signature, audit-integrity broken).
  - If all three SHAs recompute correctly but COLLIDE because all three
    scripts declared identical INPUT_FILES -> INFO (audit discipline
    weak: single-input gates cannot be distinguished by closure SHA;
    recommend pinning the producing-script SHA itself into INPUT_FILES
    going forward).
  - If all three SHAs recompute correctly AND are distinct -> PASS.

DISCIPLINE
----------
- `from canonical_constants import *` (imports PI; unused constants fine)
- Every local/intermediate tagged `# (local)`
- CPU-only (audit logic is pure Python; no linear algebra)
- SHA-256 of all input files logged in first 20 lines of stdout
- Gate verdict appended to s83_gate_verdicts.txt with 64-char SHA pin
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY per CLAUDE.md)
# ---------------------------------------------------------------------------
import os
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
from computation_root import resolve_script, resolve_output, resolve_glob, resolve_dynamic, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault('OMP_NUM_THREADS', '8')     # (local) CPU cap
os.environ.setdefault('MKL_NUM_THREADS', '8')     # (local)

import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import re
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths and pre-registration pins
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S83"                                               # (local)
GATE_ID = "S83-SHA-COLLISION-AUDIT"                           # (local)
SCHEME = "S82-verdict-SHAs"                                   # (local)
CONVENTION = "sha256-input-pin-map"                           # (local)
L_MAX = "N/A"                                                 # (local)

# Pre-registered gate
# PASS : all 3 recompute AND distinct
# INFO : all 3 recompute but share identical input-pin map (legit collision)
# FAIL : any recomputation mismatch (copy-paste signature)
# (per S81+ audit protocol, gate-verdicts.md rules)

# Input/output paths
OUT_NPZ = resolve_output(83, 's83_w3_g59_sha_collision_audit.npz')
OUT_PNG = resolve_output(83, 's83_w3_g59_sha_collision_audit.png')
VERDICT_TXT = resolve_output(83, 's83_gate_verdicts.txt')
S82_VERDICTS = resolve_output(82, 's82_gate_verdicts.txt')

# The three triplet gates + their producing scripts (S82)
TRIPLET = [                                                   # (local)
    {
        "label": "W1-1-TD",
        "gate_id_s82": "S82-H-TILDE-EPOCH-TD",
        "script": resolve_script(82, 's82_w1_1_h_tilde_td.py'),
    },
    {
        "label": "W2-13",
        "gate_id_s82": "S82-F0-CONVENTION-AUDIT",
        "script": resolve_script(82, 's82_w2_13_f0_convention_audit.py'),
    },
    {
        "label": "W3-7",
        "gate_id_s82": "S82-EJ-CONVENTION-AUDIT",
        "script": resolve_script(82, 's82_w3_7_ej_convention_audit.py'),
    },
]

INPUT_FILES = [                                               # (local)
    S82_VERDICTS,
    resolve_script(82, 's82_w1_1_h_tilde_td.py'),
    resolve_script(82, 's82_w2_13_f0_convention_audit.py'),
    resolve_script(82, 's82_w3_7_ej_convention_audit.py'),
    resolve_script(None, 'canonical_constants.py'),
]

# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (own closure for this audit script)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file; empty string on missing."""
    h = hashlib.sha256()                                      # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    """Print SHA-256 of each input; return dict {relpath: sha} for closure."""
    print(f"=== {GATE_ID} -- input SHA-256 pins (S81-hardened) ===")
    pins = {}                                                 # (local)
    for p in inputs:
        sha = sha256_of(p)                                    # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins) -> str:
    """Stable hash over ordered input SHAs -- full 64-char hexdigest."""
    items = sorted(pins.items())                              # (local)
    h = hashlib.sha256()                                      # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Replicate the canonical closure-hash algorithm from S82 scripts
# ---------------------------------------------------------------------------
# All three S82 scripts use IDENTICAL closure_hash logic:
#
#   def closure_hash(pins):
#       items = sorted(pins.items())
#       h = hashlib.sha256()
#       for k, v in items:
#           h.update(f"{k}={v}\n".encode("utf-8"))
#       return h.hexdigest()
#
# and pins is built from INPUT_FILES via:
#
#   pins[rel] = sha256_of(input_file)
#
# where rel is the POSIX-ified relative path to PROJECT_ROOT.
# We replicate that EXACTLY here.


def replicate_s82_closure(input_files_list):
    """Replicate the S82-canonical closure hash from a list of Path objects.

    Matches the algorithm in:
      - s82_w1_1_h_tilde_td.py (lines 134-162)
      - s82_w2_13_f0_convention_audit.py (lines 101-126)
      - s82_w3_7_ej_convention_audit.py (lines 114-139)

    All three scripts use identical logic. The closure SHA depends only on
    (a) the ordered relpath keys and (b) the SHA-256 of each input file's
    bytes at the time the script ran.
    """
    pins = {}                                                 # (local)
    for p in input_files_list:
        sha = sha256_of(p)                                    # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        pins[rel] = sha
    return closure_hash(pins), pins


# ---------------------------------------------------------------------------
# Section 6 -- Parse the S82 INPUT_FILES declaration from each producing script
# ---------------------------------------------------------------------------
# The three S82 producing scripts declare INPUT_FILES like:
#
#   INPUT_FILES = [
#       SCRIPT_DIR / "canonical_constants.py",
#   ]
#
# We extract this list statically (via regex) so we are testing the
# DECLARED-BY-SCRIPT input map, independently of re-running the script.

INPUT_FILES_PATTERN = re.compile(
    r"INPUT_FILES\s*=\s*\[(.*?)\]",
    re.DOTALL,
)
# Each entry in the list is `SCRIPT_DIR / "filename.py"` or similar.
ENTRY_PATTERN = re.compile(
    r'SCRIPT_DIR\s*/\s*"([^"]+)"',
)


def parse_input_files_declaration(script_path: Path):
    """Extract the list of INPUT_FILES entries declared in a script.

    Returns a list of Path objects (resolved against SCRIPT_DIR).
    Returns [] if the script has no INPUT_FILES declaration.
    """
    try:
        text = script_path.read_text(encoding="utf-8")        # (local)
    except OSError:
        return []
    m = INPUT_FILES_PATTERN.search(text)                      # (local)
    if m is None:
        return []
    body = m.group(1)                                         # (local)
    names = ENTRY_PATTERN.findall(body)                       # (local)
    return [resolve_dynamic(n) for n in names]


# ---------------------------------------------------------------------------
# Section 7 -- Parse the recorded SHA from the S82 verdict file
# ---------------------------------------------------------------------------

def parse_recorded_sha(gate_id: str) -> str:
    """Extract the sha256 value for a given gate ID from s82_gate_verdicts.txt.

    Returns the 64-char hex string, or empty string if not found.
    """
    try:
        text = S82_VERDICTS.read_text(encoding="utf-8")       # (local)
    except OSError:
        return ""
    # Find lines starting with gate_id:
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith(gate_id + ":") or s.startswith(gate_id + " :"):
            # Pattern: ... sha256=<hex>
            m = re.search(r"sha256=([0-9a-f]{64})", s)        # (local)
            if m:
                return m.group(1)
    return ""


# ---------------------------------------------------------------------------
# Section 8 -- Main audit logic
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                          # (local)

    # --- 8A. Input pinning for THIS script's own closure SHA ---
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure-64: {closure}")
    print()
    print(f"S83 W3-G59: SHA-COLLISION-AUDIT (S82 W1-1-TD / W2-13 / W3-7 triplet)")
    print(f"  Gate: {GATE_ID}")
    print(f"  Classification: NON-PHONONIC")
    print()

    # --- 8B. Substitution chain (pre-registered, printed for audit trail) ---
    print("=" * 78)
    print("STEP 1 -- SUBSTITUTION CHAIN (pre-registered)")
    print("=" * 78)
    print("  Definition  : SHA(i) = sha256( sorted_input_pin_map_i ) [64-char hex]")
    print("  Input map_i = { rel_path_j : sha256_of(file_j)  for j in INPUT_FILES_i }")
    print("  Closure     = sha256( concat( sorted{ f'{k}={v}\\n' : (k,v) in map } ) )")
    print("  Direction   : PASS iff all 3 recorded SHAs recompute from the")
    print("                declared INPUT_FILES of their producing script AND")
    print("                are pairwise distinct.")
    print("                INFO iff all 3 recompute but SHAs coincide because")
    print("                INPUT_FILES lists are identical across the 3 gates.")
    print("                FAIL iff any recorded SHA does NOT recompute from")
    print("                the declared INPUT_FILES (audit broken).")
    print()

    # --- 8C. Per-gate audit ---
    print("=" * 78)
    print("STEP 2 -- Per-gate SHA recomputation")
    print("=" * 78)

    records = []                                              # (local)
    for item in TRIPLET:
        label = item["label"]
        gate_s82 = item["gate_id_s82"]
        script = item["script"]

        recorded_sha = parse_recorded_sha(gate_s82)           # (local)
        declared_inputs = parse_input_files_declaration(script)  # (local)
        recomputed_sha, recomputed_pins = replicate_s82_closure(
            declared_inputs
        )                                                     # (local)
        match = (recorded_sha == recomputed_sha) and len(recorded_sha) == 64

        records.append({
            "label": label,
            "gate_s82": gate_s82,
            "script": str(script.relative_to(PROJECT_ROOT)).replace("\\", "/"),
            "declared_inputs": [
                str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
                for p in declared_inputs
            ],
            "recorded_sha": recorded_sha,
            "recomputed_sha": recomputed_sha,
            "pins": recomputed_pins,
            "match": match,
        })

        print(f"  [{label}] gate = {gate_s82}")
        print(f"    script        = {script.name}")
        print(f"    declared inp. = {[p.name for p in declared_inputs]}")
        print(f"    recorded SHA  = {recorded_sha}")
        print(f"    recomputed    = {recomputed_sha}")
        print(f"    MATCH         = {match}")
        print()

    shas_recorded = [r["recorded_sha"] for r in records]      # (local)
    shas_recomputed = [r["recomputed_sha"] for r in records]  # (local)

    distinct_count = len(set(shas_recorded))                  # (local)
    all_distinct = (distinct_count == 3)                      # (local)
    all_match = all(r["match"] for r in records)              # (local)

    # Check input-map identity (do all three declare IDENTICAL INPUT_FILES?)
    input_sets = [tuple(r["declared_inputs"]) for r in records]  # (local)
    shared_input_map = (len(set(input_sets)) == 1)            # (local)

    # --- 8D. Verdict decision ---
    print("=" * 78)
    print("STEP 3 -- Verdict decision")
    print("=" * 78)
    print(f"  Recorded SHAs: {shas_recorded}")
    print(f"  Distinct SHAs: {distinct_count}/3 ({'distinct' if all_distinct else 'COLLISION'})")
    print(f"  All recompute correctly: {all_match}")
    print(f"  All scripts share identical INPUT_FILES: {shared_input_map}")
    print()

    if not all_match:
        verdict = "FAIL"                                      # (local)
        reason = "SHA recomputation mismatch - copy-paste or corrupted closure"
    elif all_distinct:
        verdict = "PASS"                                      # (local)
        reason = "all 3 SHAs distinct AND each recomputes from its input-pin map"
    else:
        # All recompute correctly, but collision exists.
        # Distinguish legitimate input-map coincidence from copy-paste.
        if shared_input_map:
            verdict = "INFO"                                  # (local)
            reason = (
                "collision is LEGITIMATE: all 3 scripts declare identical "
                "INPUT_FILES = [canonical_constants.py], so closure SHA is "
                "forced to match by construction. NOT copy-paste. Audit-"
                "discipline recommendation: pin producing-script SHA into "
                "INPUT_FILES so single-input audits differentiate by script."
            )
        else:
            verdict = "FAIL"                                  # (local)
            reason = "SHA collision with DIFFERENT input-pin maps - cryptographic anomaly (should never happen)"

    print(f"  VERDICT: {verdict}")
    print(f"  REASON:  {reason}")
    print()

    # --- 8E. Plot: SHA histogram bars showing collision structure ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.4))

    ax1 = axes[0]
    labels_plot = [r["label"] for r in records]               # (local)
    short_shas = [s[:16] for s in shas_recorded]              # (local)
    colors = ['tab:blue', 'tab:orange', 'tab:green']           # (local)
    ax1.bar(range(3), [1, 1, 1], color=colors, alpha=0.7, edgecolor='k')
    for i, (lab, ss) in enumerate(zip(labels_plot, short_shas)):
        ax1.text(i, 0.5, f"{lab}\n{ss}...", ha='center', va='center',
                 fontsize=9, fontweight='bold', family='monospace')
    ax1.set_xticks(range(3))
    ax1.set_xticklabels(labels_plot)
    ax1.set_ylim([0, 1.2])
    ax1.set_ylabel('(dummy)')
    ax1.set_title('S82 recorded SHA-256 (first 16 chars)')
    ax1.grid(True, alpha=0.3, axis='y')

    ax2 = axes[1]
    match_vals = [1.0 if r["match"] else 0.0 for r in records]  # (local)
    ax2.bar(range(3), match_vals,
            color=['green' if m == 1 else 'red' for m in match_vals],
            edgecolor='k', alpha=0.75)
    ax2.set_xticks(range(3))
    ax2.set_xticklabels(labels_plot)
    ax2.set_ylim([0, 1.2])
    ax2.set_ylabel('SHA recompute match')
    ax2.set_title('Recorded SHA matches recomputed SHA?')
    ax2.grid(True, alpha=0.3, axis='y')
    for i, m in enumerate(match_vals):
        ax2.text(i, m + 0.05, 'MATCH' if m == 1 else 'MISMATCH',
                 ha='center', fontsize=10, fontweight='bold')

    fig.suptitle(
        f'S83 W3-G59 SHA-COLLISION-AUDIT -- verdict = {verdict}\n'
        f'distinct={distinct_count}/3, all_match={all_match}, shared_INPUT_FILES={shared_input_map}',
        fontsize=11,
    )
    plt.tight_layout()
    fig.savefig(OUT_PNG, dpi=140, bbox_inches='tight')
    plt.close(fig)

    # --- 8F. Save npz ---
    np.savez(
        OUT_NPZ,
        verdict=verdict,
        reason=reason,
        distinct_count=distinct_count,
        all_distinct=all_distinct,
        all_match=all_match,
        shared_input_map=shared_input_map,
        labels=np.array(labels_plot),
        gate_ids_s82=np.array([r["gate_s82"] for r in records]),
        scripts=np.array([r["script"] for r in records]),
        recorded_shas=np.array(shas_recorded),
        recomputed_shas=np.array(shas_recomputed),
        declared_inputs=np.array([",".join(r["declared_inputs"]) for r in records]),
        scheme=SCHEME,
        convention=CONVENTION,
        closure_sha256_full=closure,
    )

    # --- 8G. 4-tuple + verdict line (S81-canonical, 64-char SHA) ---
    four_tuple = (
        f"(value={distinct_count}/3, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX})"
    )
    print(f"\n4-tuple: {four_tuple}")
    print()

    verdict_line = (
        f"{GATE_ID}: {verdict} -- "
        f"value={distinct_count}/3 scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)

    # --- 8H. Diagnostic summary ---
    wall = time.time() - t0                                   # (local)
    print("=" * 78)
    print("OUTPUTS SAVED")
    print("=" * 78)
    print(f"  Script  : {__file__}")
    print(f"  Data    : {OUT_NPZ}")
    print(f"  Plot    : {OUT_PNG}")
    print(f"  Verdict : appended to {VERDICT_TXT}")
    print()
    print(f"VERDICT LINE (appended):")
    print(f"  {verdict_line.strip()}")
    print()
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
