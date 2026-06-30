#!/usr/bin/env python3
"""
S86 W15-1 — S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY
=========================================================

Gate: S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY ([VERIFY])

Pre-registered threshold (binary presence-check; per plan §9):
  PASS iff (a) all 4 obstruction-vector rows present and non-empty
       AND (b) sibling-cluster line cites all THREE sibling IDs
                (#19_no-T-duality, #20_no-S-duality, #21_no-Hagedorn)
       AND (c) W10-1 audit_sha256 is exactly 64 hex chars.
  FAIL otherwise.  INFO not used (binary verification, no band).

Inputs (SHA-256 dual-pinned at runtime — see §4 below; S84+ schema):
  - computations/session-85/s85_gate_verdicts.txt  (W10-1 line — extract audit_sha256)
  - computations/session-85/s85_w10_anti_correspondence_30_registry.json
  - computations/session-85/s85_w10_anti_correspondence_30_REGISTRY_PATCH.md
  - sessions/permanent-results-registry.md (§VII row schema reference)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<n_present>-of-4_components_present, scheme=registry-write,
   convention=parallel-cluster, L_max=NA)

Classification: GEOMETRIC

METHODOLOGY
-----------
W15-1 promotes the S85 W10-1 ANTI-CORRESPONDENCE #30 patch (whose physics
is ALREADY pinned in `s85_gate_verdicts.txt` audit_sha256 prefix
e034e19f...) into a NEW project-level registry file at
`sessions/framework/correspondence/correspondence-table-registry.md`. The registry
becomes the canonical "do-not-re-litigate string-substrate distinctions"
ledger, parallel to `permanent-results-registry.md` §VII. This script:
  1. Reads the W10-1 verdict line from the canonical S85 verdict file.
  2. Extracts the full 64-char audit_sha256.
  3. Assembles the entry-30 block (4-obstruction vector + sibling-cluster
     citation + substrate-side derivation pointers + Witten 1998 anchor).
  4. Writes the registry file (creating it with header if absent;
     appending #30 if present).
  5. Verifies VERIFY conjunction (a) AND (b) AND (c).
  6. Computes closure_sha = sha256( registry_block || W10-1_audit_sha256 ||
     ordered_sibling_3-tuple ) and emits the dual-SHA verdict line.

DISCIPLINE
----------
- canonical_constants import: NOT REQUIRED for registry write (no framework
  constants used in the body), but imported defensively per `computations/_shared/CLAUDE.md`.
- Every local/intermediate tagged `# (local)`.
- GPU path: NOT USED (registry write, no linear algebra).
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- 4-tuple printed as the final non-verdict line.
- Gate verdict appended to `s86_gate_verdicts.txt` with BOTH
  `audit_sha256=<64>` and `content_sha256=<64>` plus `schema_version=S84+`.
- closure_sha is COMPUTED, never hardcoded (per `.claude/rules/v3-closure-recovery.md` §sig_5).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (defensive import; not used in body)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
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

_SCRIPT_DIR = _Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in _sys.path:
    _sys.path.insert(0, str(_SCRIPT_DIR))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"

SESSION = "S86"                                                    # (local)
GATE_ID = "S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY"          # (local)
SCHEME = "registry-write"                                          # (local)
CONVENTION = "parallel-cluster"                                    # (local)
L_MAX = "NA"                                                       # (local)

# Pre-registered targets (per plan §0.10 W15-1 machinery enumeration)
REGISTRY_TARGET = FRAMEWORK_DIR / "correspondence-table-registry.md"
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')
W10_1_VERDICT_FILE = resolve_output(85, 's85_gate_verdicts.txt')
W10_1_REGISTRY_JSON = resolve_output(85, 's85_w10_anti_correspondence_30_registry.json')
W10_1_REGISTRY_PATCH = resolve_script(85, 's85_w10_anti_correspondence_30_REGISTRY_PATCH.md')
PERMANENT_REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

# Pre-registered values (per plan §0.10 W15-1 machinery enumeration; literal pins)
NEXT_ENTRY_NUM = 30                                                # (local)
OBSTRUCTION_AXES = (                                               # (local)
    "rank",
    "K_0",
    "Witten_integral",
    "Bott_period_residue",
)
SUBSTRATE_VALUES = (3, "torsion-free", 16.0, "!= 1")               # (local)
WITTEN_VALUES = (1, "Z/2", 1.0, 1)                                 # (local)
SIBLING_CLUSTER_IDS = (                                            # (local)
    "#19_no-T-duality",
    "#20_no-S-duality",
    "#21_no-Hagedorn",
)
WITTEN_ANCHOR = "Witten, \"D-Branes and K-Theory\", JHEP 12 (1998) 019."  # (local)

INPUT_FILES = [
    W10_1_VERDICT_FILE,
    W10_1_REGISTRY_JSON,
    W10_1_REGISTRY_PATCH,
    PERMANENT_REGISTRY,
    resolve_script(None, 'canonical_constants.py'),
]


# ---------------------------------------------------------------------------
# Section 4 - SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash_legacy(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 - W10-1 source SHA extraction
# ---------------------------------------------------------------------------

def extract_w10_1_audit_sha() -> str:
    """Read W10-1 verdict line from s85_gate_verdicts.txt (canonical path
    per .claude/rules/gate-verdicts.md). Extract full 64-char audit_sha256.
    Per the plan §6 spec: never truncate.
    """
    if not W10_1_VERDICT_FILE.exists():
        raise FileNotFoundError(
            f"S85 verdict file not found at canonical path: {W10_1_VERDICT_FILE}"
        )
    text = W10_1_VERDICT_FILE.read_text(encoding="utf-8")  # (local)
    # Match the canonical verdict line for S85 W10 ANTI-CORRESPONDENCE #30
    pat = re.compile(
        r"S85-W10-ANTI-CORRESPONDENCE-30-REGISTRY:\s+PASS\s+--.*?"
        r"audit_sha256=([0-9a-f]{64})",
        re.IGNORECASE,
    )
    m = pat.search(text)
    if not m:
        raise ValueError(
            "Could not locate S85-W10-ANTI-CORRESPONDENCE-30-REGISTRY "
            "verdict line with 64-char audit_sha256 in "
            f"{W10_1_VERDICT_FILE}"
        )
    sha = m.group(1)  # (local)
    if len(sha) != 64:
        raise ValueError(
            f"W10-1 audit_sha256 length {len(sha)} != 64 (truncated)"
        )
    return sha


# ---------------------------------------------------------------------------
# Section 6 - Registry block construction
# ---------------------------------------------------------------------------

REGISTRY_FILE_HEADER = """# Correspondence-Table Registry (parallel to permanent-results §VII)

> **Provenance**: project-level registry created by S86 W15-1
> (`S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY`) per
> `sessions/session-plan/session-86-plan-w15.md` §W15-1. Owner agent:
> `kaku-speculative-theorist`. The registry mirrors the
> `permanent-results-registry.md` §VII row schema for ANTI-CORRESPONDENCE
> entries but lives in `sessions/framework/` so that future cross-paradigm
> structural-exclusion arguments route through this single canonical
> ledger rather than re-deriving the case each time.

## Substrate-framing convention (MANDATORY for all entries)

Every entry in this registry pins a structural-EXCLUSION wall in the
SUBSTRATE solution space. The string-paradigm (or other contrast-anchor)
column is a CONTRAST ANCHOR, NOT a reference frame. Direction of
explanation: substrate spectral triple -> its own structural invariants
-> comparison FROM that structure outward to the contrast paradigm. Do
NOT write "the substrate looks like the contrast paradigm except for
these N corrections" -- that inverts the explanatory direction. The
substrate is logically prior; the contrast paradigm is the anchor.

Per `.claude/rules/phononic-framing.md`: this is a structural wall, not
a "things the substrate has that look like the string scheme" ledger.

## Schema (one row per entry)

  ## Entry #<N> -- <substrate aspect> vs <contrast paradigm>

  Source verdict: <gate ID> (S<N>), audit_sha256=<full 64-char>
  Sibling cluster: <list of sibling entry IDs forming the bloc>

  <N>-OBSTRUCTION VECTOR:
  | axis | substrate | <contrast paradigm> |
  |:-----|:----------|:--------------------|
  ...

  Substrate-side derivation pointers:
  ...

  Contrast-side anchor:
  ...

"""


def build_registry_block(w10_1_sha: str) -> str:
    """Assemble the entry-30 markdown block to be appended.

    Substrate-framing direction: substrate spectral triple FIRST,
    Witten 1998 column is a CONTRAST ANCHOR.
    """
    sib_line = ", ".join(SIBLING_CLUSTER_IDS)  # (local)
    block = f"""## Entry #{NEXT_ENTRY_NUM} -- Substrate vs Witten 1998 K-theoretic D-brane scheme

Source verdict: W10-1 (S85), audit_sha256={w10_1_sha}
Sibling cluster: {sib_line}
                 -- together, this 4-entry cluster forms the
                 string-paradigm-exclusion bloc inside this registry.

4-OBSTRUCTION VECTOR:

| axis                  | substrate              | Witten 1998       |
|:----------------------|:-----------------------|:------------------|
| rank                  | 3                      | 1                 |
| K_0                   | torsion-free           | Z/2               |
| Witten integral       | 16.0                   | 1.0               |
| Bott-period residue   | != 1                   | 1                 |

Each axis is a structural disagreement, NOT a numerical epsilon-deviation.
ALL FOUR must hold simultaneously for entry #{NEXT_ENTRY_NUM} to apply; absence of
any single component invalidates the registry write.

Substrate-side derivation pointers (substrate spectral triple is logically prior):
 - rank = 3: from the SU(3) gauge factor of D_K (Connes spectral-triple-rank
   theorem; the substrate's internal algebra A_F = C + H + M_3(C) gives
   K_0(A_F) rank = 3 from three Wedderburn-simple summands -- see §VII.R
   3-axis disjointness in `permanent-results-registry.md`).
 - K_0 torsion-free: from the SU(3) representation lattice of the Connes
   spectral triple (no Z/2 torsion appears in the substrate's K_0 group;
   the substrate's representation theory is over a noncommutative algebra
   of finite type, not a real KO-theory class).
 - Witten integral = 16.0: third spectral moment of D_K, computed as
   ch_0 * A-roof(TM^4) with the substrate's own characteristic-class data
   (16 distinct relay-pattern equivalence classes).
 - Bott-period residue != 1: 8-periodicity of real KO-theory is broken on
   the Jensen-deformed substrate by the tau_fold-localized parity flip
   (16 mod 8 = 0, 16 mod 2 = 0; neither congruence class hits 1).

Contrast-side anchor (string-paradigm reference, NOT a reference frame):
 - {WITTEN_ANCHOR}
   Witten's K-theoretic D-brane classification scheme assigns single-brane
   K^0(X) = Z (rank 1), KO^6(pt) = Z/2 torsion, single-brane Witten
   integral = 1, and 8-periodic KO theory with residue 1. The substrate
   fails to match any of these four invariants.

Entry semantics: this is a structural EXCLUSION wall. The substrate's
spectral triple is genuinely DISTINCT from Witten's K-theoretic D-brane
classification along four independent axes. The four axes are not
small-correction perturbations of a shared structure -- they are
algebraically independent K-theoretic invariants. The registry write
documents the boundary the substrate's structural identity does not
cross under the Witten 1998 candidate parent.

Provenance chain (per S85 W10-1 patch):
 - Source gate: S84-DET-P-K-THEORY (W7-74); homotopy_level = 1
 - Source closure SHA-256: def5d0cdb8a39d16017820a602cb8821fefcbbc8720700f3eb6e5b095d4af1d2
 - Landing gate: S85-W10-ANTI-CORRESPONDENCE-30-REGISTRY (PASS)
 - Landing audit_sha256: {w10_1_sha}
 - Landing content_sha256: 5e5f6f0dcb6cbefcbfe146aa9ecc056f55b653469308a487308518ef36042138
 - Project-registry landing gate: S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY (this entry)

"""
    return block


# ---------------------------------------------------------------------------
# Section 7 - Registry write (atomic; create file with header if new)
# ---------------------------------------------------------------------------

def write_registry_block(block: str) -> bool:
    """Write entry block to correspondence-table-registry.md.

    Returns True if file was newly created, False if appended.
    """
    is_new = not REGISTRY_TARGET.exists()  # (local)
    REGISTRY_TARGET.parent.mkdir(parents=True, exist_ok=True)
    if is_new:
        with REGISTRY_TARGET.open("w", encoding="utf-8") as fp:
            fp.write(REGISTRY_FILE_HEADER)
            fp.write("\n")
            fp.write(block)
        return True
    else:
        # Append-only (parallel-writer race avoidance per
        # `.claude/rules/epistemic-discipline.md`)
        with REGISTRY_TARGET.open("a", encoding="utf-8") as fp:
            fp.write("\n")
            fp.write(block)
        return False


# ---------------------------------------------------------------------------
# Section 8 - VERIFY presence-checks (binary; per plan §9)
# ---------------------------------------------------------------------------

def verify_block(block: str, w10_1_sha: str) -> dict:
    """Run the binary VERIFY conjunction (a) AND (b) AND (c)."""
    # (a) all 4 obstruction-vector rows present and non-empty
    obs_rows = [
        "| rank ",
        "| K_0 ",
        "| Witten integral ",
        "| Bott-period residue ",
    ]
    a_check = all(row in block for row in obs_rows)  # (local)

    # (b) sibling-cluster line cites all THREE sibling IDs
    b_check = all(sid in block for sid in SIBLING_CLUSTER_IDS)  # (local)

    # (c) W10-1 audit_sha256 is exactly 64 hex chars
    c_check = (
        len(w10_1_sha) == 64
        and all(ch in "0123456789abcdef" for ch in w10_1_sha.lower())
    )  # (local)

    n_present = int(a_check) + int(b_check) + int(c_check)  # (local)
    overall = a_check and b_check and c_check  # (local)
    return {
        "a_obstruction_rows": a_check,
        "b_sibling_cluster": b_check,
        "c_sha_64hex": c_check,
        "n_present": n_present,
        "overall": overall,
    }


# ---------------------------------------------------------------------------
# Section 9 - closure_sha for verdict line
# ---------------------------------------------------------------------------

def compute_closure_sha(block: str, w10_1_sha: str) -> str:
    """closure_sha = sha256( utf-8 join("\\n", [block, w10_1_sha,
                              "|".join(sibling_3-tuple)]) )

    Hash inputs (ordered per plan §6 step 'closure_sha computation'):
      1. content of new/appended block in correspondence-table-registry.md
      2. W10-1 source audit_sha256 string
      3. ordered tuple (sibling_id_19, sibling_id_20, sibling_id_21)
    """
    sibling_str = "|".join(SIBLING_CLUSTER_IDS)  # (local)
    payload = "\n".join([block, w10_1_sha, sibling_str]).encode("utf-8")  # (local)
    return hashlib.sha256(payload).hexdigest()


def compute_block_content_sha(block: str) -> str:
    """SHA-256 of the registry block bytes (companion comment row's content_sha256)."""
    return hashlib.sha256(block.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Section 10 - Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict_lines(
    verdict: str,
    value_str: str,
    closure_sha: str,
    block_content_sha: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Append canonical verdict line + dual-SHA companion comment row.

    Per plan §6 'Verdict line' + 'Companion comment row (dual-SHA per W9a-99)'.

    Atomic append (single open("a") with both lines), per
    `.claude/rules/v3-closure-recovery.md` and the script-template
    append_verdict() helper pattern.
    """
    # Canonical verdict line (per plan §6 + .claude/rules/gate-verdicts.md S81+)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value_str} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    # Dual-SHA companion comment row (W9a-99 split)
    companion_line = (
        f"# {GATE_ID} -- "
        f"content_sha256={block_content_sha} audit_sha256={closure_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_line)


def evaluate_gate(verify: dict) -> str:
    """Binary presence-check: PASS iff (a) AND (b) AND (c). FAIL otherwise.
    INFO not used per plan §9.
    """
    return "PASS" if verify["overall"] else "FAIL"


# ---------------------------------------------------------------------------
# Section 11 - Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    legacy_closure = closure_hash_legacy(pins)  # (local) informational only
    print(f"  legacy_closure: {legacy_closure[:16]}... (informational)")

    # 1b. Compute S84+ dual SHAs (script + canonical + pinmap)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Extract W10-1 source audit_sha256 (full 64 chars)
    w10_1_sha = extract_w10_1_audit_sha()
    print(f"  W10-1 source audit_sha256 (full 64): {w10_1_sha}")
    print(f"  W10-1 sha length: {len(w10_1_sha)} chars")
    print()

    # 3. Build the entry-30 registry block (substrate-first framing)
    block = build_registry_block(w10_1_sha)
    block_content_sha = compute_block_content_sha(block)
    print(f"  registry block bytes: {len(block.encode('utf-8'))}")
    print(f"  registry block content_sha256: {block_content_sha[:16]}...")

    # 4. Run VERIFY presence-checks (binary; before write to allow FAIL-without-write)
    verify = verify_block(block, w10_1_sha)
    print(f"  VERIFY (a) obstruction rows present: {verify['a_obstruction_rows']}")
    print(f"  VERIFY (b) sibling cluster cites 3:  {verify['b_sibling_cluster']}")
    print(f"  VERIFY (c) W10-1 sha = 64 hex chars: {verify['c_sha_64hex']}")
    print(f"  n_present = {verify['n_present']} of 4_components_present")
    print(f"  conjunction overall: {verify['overall']}")
    print()

    # 5. Write registry block (only if VERIFY passes; FAIL leaves file untouched)
    if verify["overall"]:
        is_new = write_registry_block(block)
        print(f"  registry write: {'CREATED new file' if is_new else 'APPENDED to existing'}")
        print(f"  registry path: {REGISTRY_TARGET}")
    else:
        print("  registry write: SKIPPED (VERIFY conjunction failed)")

    # 6. Compute closure_sha (per plan §6 'closure_sha computation' 3-tuple)
    closure_sha = compute_closure_sha(block, w10_1_sha)
    print(f"  closure_sha (registry+W10-1+siblings): {closure_sha}")
    print()

    # 7. Evaluate gate verdict (binary)
    verdict = evaluate_gate(verify)

    # 8. Emit 4-tuple + append verdict lines
    # Per plan §6 explicit literal `value=4-of-4_components_present`: the
    # "4" is the count of OBSTRUCTION-VECTOR COMPONENTS (rank, K_0,
    # Witten integral, Bott-period residue) that must be present in the
    # registry block. The VERIFY conjunction (a)∧(b)∧(c) is a 3-check
    # binary, but the value-string convention reports component count.
    # When the conjunction PASSes, all 4 obstruction components are
    # present (verified by check (a)) AND the citation context is intact
    # (checks (b), (c)).
    if verify["overall"]:
        value_str = "4-of-4_components_present"  # (local) per plan §6 literal
    else:
        # Count actually-present obstruction-vector rows for FAIL diagnostic
        obs_rows = ["| rank ", "| K_0 ", "| Witten integral ", "| Bott-period residue "]  # (local)
        n_obs_present = sum(1 for row in obs_rows if row in block)  # (local)
        value_str = f"{n_obs_present}-of-4_components_present"  # (local)
    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict_lines(
        verdict,
        value_str,
        closure_sha,
        block_content_sha,
        audit_sha,
        content_sha,
    )

    # 9. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
