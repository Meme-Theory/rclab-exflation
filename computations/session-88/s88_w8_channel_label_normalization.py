#!/usr/bin/env python3
"""
S88 W8-94 — S88-CHANNEL-LABEL-NORMALIZATION (METHODOLOGY-class)
================================================================

Gate: S88-CHANNEL-LABEL-NORMALIZATION ([AUDIT])

Pre-registered threshold (METHODOLOGY-class; M1 artifact-existence):
  PASS iff (a) `CHANNEL_LABELS` dict present in canonical_constants.py with all 22
  entries (4 diagonal {C, H, M_3, M_2} + 18 off-diagonal cells indexed by
  k ∈ {1,2,3} channel × ordered (p,q) ∈ {II,III,IV}^2 off-diagonal pairs)
  AND (b) provenance comment present at the dict
  AND (c) allowlist row `W8-94 | S88 | S88-CHANNEL-LABEL-NORMALIZATION | <SHA>`
  appended to `.claude/rules/methodology-wave-allowlist.md`
  AND (d) importability cross-check `from canonical_constants import CHANNEL_LABELS`
  succeeds in a clean subprocess returning len(CHANNEL_LABELS) == 22.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py (current state; pre-edit SHA captured)
  - sessions/permanent-results-registry.md (§VII.X.W4-1 substantive block at line 13614+)
  - .claude/rules/methodology-wave-allowlist.md (current state)
  - this script

Output 4-tuple:
  (value='dict-22-entries-pinned;importable=True;allowlist-appended=True',
   scheme=METHODOLOGY-canonical-constants-pin-landing,
   convention=CHANNEL-LABELS-dict-9-cell-tensor-22-entries,
   L_max=N/A)

Classification: METHODOLOGY (per .claude/rules/wave-classification.md M1-M4 strict
conjunction; pre-allocated allowlist W8-94 row appended in this dispatch).

Substrate framing
-----------------
Channel labels are structural identifiers of the substrate algebra
A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) and the Hochschild-cocycle off-diagonal cells of the
9-cell tensor R^{(k)}_{p,q}(L_max=10) per §VII.X.W4-1. The 4 diagonal entries
are the algebra summands in their structural form (ℂ scalar-trace, ℍ
quaternionic-isospin, M_3(ℂ) Cartan-zone full sector, M_2(ℂ) BdG sector
inherited via ι_*). The 18 off-diagonal entries enumerate (channel k=1,2,3)
× (off-diagonal pillar pair (p,q) ∈ {II,III,IV}² with p ≠ q; 6 ordered
pairs), giving 3 × 6 = 18. Direction of explanation: substrate
spectral-triple algebra → cohomology-cocycle-rank channel decomposition →
canonical-constants pin (the labels are NOT labels for a pre-existing
geometric container; they ARE the substrate-IS observables under three
regulator-class restrictions per §VII.X.W4-1 line 13620).

Substitution chain — 22-entry cardinality
------------------------------------------
Definition 1: pillars = {II, III, IV}
Definition 2: off_diag_pairs = {(p, q) : p, q ∈ pillars, p ≠ q}  (ordered)
Definition 3: channels = {1, 2, 3}
Definition 4: diagonal_summands = {C, H, M_3, M_2}

Step 1 (substitute): |pillars| = 3
Step 2 (substitute): |off_diag_pairs| = 3 × 2 = 6
                     (II↔III, II↔IV, III↔II, III↔IV, IV↔II, IV↔III)
Step 3 (substitute): |channels × off_diag_pairs| = 3 × 6 = 18
Step 4 (substitute): |diagonal_summands| = 4
Step 5 (simplify):   total = 18 + 4 = 22

Direction: 22 entries matches plan §W8-94 threshold (a). ✓

DISCIPLINE
----------
- `from canonical_constants import *` (Section 1)
- METHODOLOGY-class write-only operations on canonical_constants.py + allowlist
- No numerical comparison; PASS predicate is artifact-existence
- Atomic append via `open("a")` for both the canonical_constants.py edit and
  the allowlist row (no read-modify-write race; idempotent per
  re-run-detection guard at Section 5)
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

# Make _shared importable
_SCRIPT_PATH = Path(__file__).resolve()
_SHARED = _SCRIPT_PATH.parent.parent / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import subprocess
import time

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = _SCRIPT_PATH.parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S88"                                                   # (local)
GATE_ID = "S88-CHANNEL-LABEL-NORMALIZATION"                       # (local)
SCHEME = "METHODOLOGY-canonical-constants-pin-landing"            # (local)
CONVENTION = "CHANNEL-LABELS-dict-9-cell-tensor-22-entries"       # (local)
L_MAX = "N/A"                                                     # (local)

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
ALLOWLIST_PATH = PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"
OUT_NPZ = SESSION_DIR / "s88_w8_channel_label_normalization.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    ALLOWLIST_PATH,
]

# ---------------------------------------------------------------------------
# Section 4 — CHANNEL_LABELS dict canonical specification (substrate-IS source)
#
# Source: sessions/permanent-results-registry.md §VII.X.W4-1 lines 13614-13705
#   - 4 diagonal entries: A_K = C ⊕ H ⊕ M_3(C) algebra summands plus M_2(C)
#     BdG sub-sector image of inheritance morphism ι_* (per §VII.X.W4-1 line
#     13640: "for p = III the BdG superfluid HC^k(A_K) cocycle"; cf. W-5
#     §VII.AF.1 cancellation theorem cocycle-rank inheritance through the
#     M_3(C) → M_2(C) BdG-restriction).
#   - 18 off-diagonal entries: tensor product of
#     channels {k=1,2,3} × off-diagonal ordered pillar pairs in {II,III,IV}^2.
#     Channel meaning per registry line 13721 (Corollary VII.X.W4-1.1):
#       k=1: 2-pt-separable / Wick-decomposable cocycle (rank-1)
#       k=2: pair-cumulant / W-5 calibrated (rank-2)
#       k=3: 3-pt-connected / irreducible vertex (rank-3)
#     Pillar pairs per registry line 13644:
#       (II, III), (III, II): bridge map = HKR (Hochschild-Kostant-Rosenberg)
#       (III, IV), (IV, III): bridge map = Connes-Karoubi pairing (W-5 canonical)
#       (II, IV), (IV, II):   bridge map = K-theory boundary (composition)
# ---------------------------------------------------------------------------

# Build the dict programmatically to ensure 22-entry cardinality is structural.

_DIAGONAL_LABELS = {                                              # (local)
    "M_2(C)": "channel_M2C",  # M_2(C) BdG sector image of ι_*(M_3(C))
    "M_3(C)": "channel_M3C",  # M_3(C) Cartan-zone full sector
    "H":      "channel_H",     # H quaternionic-isospin sector
    "C":      "channel_C",     # C scalar-trace sector
}

_PILLARS = ("II", "III", "IV")                                    # (local)
_CHANNELS = (1, 2, 3)                                             # (local)


def _build_off_diagonal_labels() -> dict[str, str]:
    """Enumerate 18 off-diagonal cells as channel k × ordered pillar-pair (p,q).

    Substitution chain:
      |pillars|    = 3
      |off_pairs|  = 3 × 2 = 6  (ordered, p != q)
      |channels|   = 3
      |off_diag|   = 3 × 6 = 18

    Direction: matches plan §W8-94 "18 off-diagonal cells" and registry
    §VII.X.W4-1 Step 5 line 13693 ("Of 18 off-diagonal cells").
    """
    out: dict[str, str] = {}                                      # (local)
    for k in _CHANNELS:
        for p in _PILLARS:
            for q in _PILLARS:
                if p == q:
                    continue
                key = f"k{k}_{p}_to_{q}"                          # (local)
                value = f"channel_off_diag_k{k}_{p}_to_{q}"       # (local)
                out[key] = value
    return out


def build_channel_labels_dict() -> dict[str, str]:
    """Build the canonical 22-entry CHANNEL_LABELS dict.

    Structure:
      4 diagonal:   M_2(C), M_3(C), H, C
      18 off-diagonal: k ∈ {1,2,3} × ordered (p,q) ∈ {II,III,IV}^2 \\ Δ
    """
    labels: dict[str, str] = {}                                   # (local)
    labels.update(_DIAGONAL_LABELS)
    labels.update(_build_off_diagonal_labels())
    if len(labels) != 22:
        raise AssertionError(
            f"CHANNEL_LABELS cardinality drift: {len(labels)} != 22"
        )
    return labels


# ---------------------------------------------------------------------------
# Section 5 — Edit canonical_constants.py + allowlist (idempotent)
# ---------------------------------------------------------------------------

CHANNEL_LABELS_BLOCK_HEADER = "# === S88 W8-94 — CHANNEL_LABELS canonical pin (22 entries) ==="
CHANNEL_LABELS_PROVENANCE = (
    "# CHANNEL_LABELS pinned S88 W8-94 per s87 §VII.X.W4-1 9-cell tensor "
    "channel-label drift analysis; cites operator-projection Reading-A "
    "naming hygiene (S88 W8-92).\n"
    "# Source: sessions/permanent-results-registry.md §VII.X.W4-1 lines\n"
    "# 13614-13705 (Cross-Pillar 3-Channel Bridge Theorem, 9-Cell Tensor\n"
    "# R^{(k)}_{p,q}(L_max=10); STAGE-1-CANDIDATE per joint-theorem-promotion.md).\n"
    "# Structure: 4 diagonal (algebra summands C, H, M_3, M_2) + 18 off-diagonal\n"
    "# (k in {1,2,3} channel x ordered (p,q) in {II,III,IV}^2 with p != q).\n"
    "# Substrate framing: labels are structural identifiers of A_K = C (+) H (+)\n"
    "# M_3(C) and Hochschild-cocycle off-diagonal cells; NOT labels for a\n"
    "# pre-existing geometric container.\n"
)


def _format_channel_labels_python(labels: dict[str, str]) -> str:
    """Format dict as Python source for the canonical_constants.py append."""
    lines = ["CHANNEL_LABELS = {"]                                # (local)
    # Diagonal first (4 entries)
    lines.append("    # --- 4 diagonal: A_K = C (+) H (+) M_3(C) summands + M_2(C) BdG sub-sector ---")
    for key in ("M_2(C)", "M_3(C)", "H", "C"):
        v = labels[key]
        comment = {
            "M_2(C)": "M_2(C) BdG sector (from inheritance iota_*(M_3(C)) -> M_2(C))",
            "M_3(C)": "M_3(C) Cartan-zone full sector",
            "H":      "H quaternionic-isospin sector",
            "C":      "C scalar-trace sector",
        }[key]
        lines.append(f'    {key!r:12s}: {v!r:48s},  # {comment}')
    # Off-diagonal (18 entries) grouped by channel
    for k in _CHANNELS:
        bridge_map = {1: "HKR/CK/Kth", 2: "HKR/CK/Kth", 3: "HKR/CK/Kth"}[k]
        rank_kind = {
            1: "rank-1 Wick-decomposable / 2-pt-separable",
            2: "rank-2 pair-cumulant / W-5 calibrated",
            3: "rank-3 3-pt-connected vertex / irreducible",
        }[k]
        lines.append(f"    # --- 6 off-diagonal cells at channel k={k} ({rank_kind}) ---")
        for p in _PILLARS:
            for q in _PILLARS:
                if p == q:
                    continue
                key = f"k{k}_{p}_to_{q}"
                v = labels[key]
                # Bridge-map identification per §VII.X.W4-1 line 13644
                if {p, q} == {"II", "III"}:
                    bm = "HKR"
                elif {p, q} == {"III", "IV"}:
                    bm = "Connes-Karoubi pairing (W-5 canonical)"
                elif {p, q} == {"II", "IV"}:
                    bm = "K-theory boundary (HKR o Connes-Karoubi)"
                else:
                    bm = "?"
                lines.append(f'    {key!r:14s}: {v!r:46s},  # {bm}')
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def edit_canonical_constants(labels: dict[str, str]) -> tuple[bool, str]:
    """Append CHANNEL_LABELS dict + provenance to canonical_constants.py.

    Returns (was_appended, snippet) where:
      was_appended: True if the dict was newly added; False if already present
      snippet: the appended Python source (for verdict-trail logging)
    """
    canonical_text = CANONICAL_PATH.read_text(encoding="utf-8")   # (local)
    if "CHANNEL_LABELS" in canonical_text and CHANNEL_LABELS_BLOCK_HEADER in canonical_text:
        return False, ""
    py_block = _format_channel_labels_python(labels)              # (local)
    appendix = (
        "\n\n"
        + CHANNEL_LABELS_BLOCK_HEADER
        + "\n"
        + CHANNEL_LABELS_PROVENANCE
        + py_block
    )
    with CANONICAL_PATH.open("a", encoding="utf-8") as fp:
        fp.write(appendix)
    return True, appendix


def verify_importable() -> tuple[bool, int, str]:
    """Subprocess-isolated import test of CHANNEL_LABELS.

    Spawns a fresh Python interpreter, performs `from canonical_constants
    import CHANNEL_LABELS`, and prints (len, type-name). Returns
    (importable, length, raw_output).
    """
    test_code = (
        "import sys; "
        f"sys.path.insert(0, {str(SHARED_DIR)!r}); "
        "from canonical_constants import CHANNEL_LABELS; "
        "print('len=' + str(len(CHANNEL_LABELS))); "
        "print('type=' + type(CHANNEL_LABELS).__name__); "
        "print('keys_sorted=' + ','.join(sorted(CHANNEL_LABELS.keys())))"
    )
    proc = subprocess.run(
        [sys.executable, "-c", test_code],
        capture_output=True,
        text=True,
        timeout=30,
    )
    raw = proc.stdout + ("\nSTDERR:\n" + proc.stderr if proc.stderr else "")
    if proc.returncode != 0:
        return False, 0, raw
    length = 0  # (local) length accumulator
    for line in proc.stdout.splitlines():
        if line.startswith("len="):
            length = int(line.split("=", 1)[1])
    return True, length, raw


def append_allowlist_row(audit_sha: str) -> tuple[bool, str]:
    """Append the W8-94 allowlist row to methodology-wave-allowlist.md.

    Idempotent: if a row matching the gate ID already exists, returns False.
    """
    text = ALLOWLIST_PATH.read_text(encoding="utf-8")             # (local)
    if "S88-CHANNEL-LABEL-NORMALIZATION" in text:
        return False, ""
    rationale = (
        "S88-CHANNEL-LABEL-NORMALIZATION (canonical_constants.py CHANNEL_LABELS "
        "22-entry dict pin: 4 diagonal {C, H, M_3, M_2} + 18 off-diagonal {k in "
        "{1,2,3} channel x ordered (p,q) in {II,III,IV}^2 \\ Diag} per s87 "
        "§VII.X.W4-1 9-cell tensor R^{(k)}_{p,q}(L_max=10) channel-label drift "
        "analysis; cites operator-projection Reading-A naming hygiene S88 W8-92; "
        "M1-M4 strict conjunction satisfied [M1 artifact-existence on "
        "canonical_constants.py append-only edit; M2 Edit on "
        "computations/_shared/canonical_constants.py + .claude/rules/methodology-"
        "wave-allowlist.md; M3 verbatim from §VII.X.W4-1 registry block lines "
        "13614-13705; M4 allowlist append herewith]; orchestrator-direct-write "
        "per wave-classification.md §Dispatch consequences; gen-physicist sole "
        "writer per math-scripts.md §Canonical write-order)"
    )
    row = f"| W8-94 | S88 | {rationale} | {audit_sha} |\n"
    with ALLOWLIST_PATH.open("a", encoding="utf-8") as fp:
        fp.write(row)
    return True, row


# ---------------------------------------------------------------------------
# Section 6 — SHA-256 input-pin block + dual-SHA
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
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
    script_bytes = b""                                            # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                         # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                             # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                   # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                               # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 7 — Verdict emission (atomic append)
# ---------------------------------------------------------------------------

def append_verdict(
    verdict: str,
    value: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Atomic single-line append per S84+ dual-SHA schema."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def evaluate_gate(
    appended_canonical: bool,
    canonical_now_has_dict: bool,
    importable: bool,
    n_entries: int,
    appended_allowlist: bool,
    allowlist_now_has_row: bool,
) -> str:
    """METHODOLOGY-class PASS predicate.

    PASS iff:
      (a) CHANNEL_LABELS present in canonical_constants.py with 22 entries
      (b) provenance comment present
      (c) allowlist row appended (idempotent: present is sufficient)
      (d) `from canonical_constants import CHANNEL_LABELS` succeeds with len==22

    The (a)/(c) idempotence allows re-runs to PASS without re-emitting.
    """
    if not canonical_now_has_dict:
        return "FAIL"
    if not allowlist_now_has_row:
        return "FAIL"
    if not importable:
        return "FAIL"
    if n_entries != 22:
        return "FAIL"
    return "PASS"


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                              # (local)

    # 1. Pre-edit input SHA-256 pins
    pins_pre = log_input_pins(INPUT_FILES)
    print(f"  closure (pre-edit): {closure_hash(pins_pre)[:16]}...")
    print()

    # 2. Build CHANNEL_LABELS dict (pure substrate-IS structural enumeration)
    labels = build_channel_labels_dict()
    print(f"=== Built CHANNEL_LABELS dict: {len(labels)} entries ===")
    print(f"  diagonal (4):     {sorted(_DIAGONAL_LABELS.keys())}")
    print(f"  off-diagonal (18): {len(labels) - 4} cells (k in {{1,2,3}} x 6 pairs)")
    print()

    # 3. Edit canonical_constants.py (idempotent)
    appended_canonical, snippet = edit_canonical_constants(labels)
    if appended_canonical:
        print(f"=== Appended CHANNEL_LABELS to canonical_constants.py ({len(snippet)} bytes) ===")
    else:
        print("=== CHANNEL_LABELS already present in canonical_constants.py (idempotent) ===")
    canonical_text_after = CANONICAL_PATH.read_text(encoding="utf-8")
    canonical_now_has_dict = (
        "CHANNEL_LABELS" in canonical_text_after
        and CHANNEL_LABELS_BLOCK_HEADER in canonical_text_after
    )
    print(f"  canonical_now_has_dict: {canonical_now_has_dict}")
    print()

    # 4. Importability cross-check via subprocess
    importable, n_entries_imported, raw = verify_importable()
    print(f"=== Importability cross-check ===")
    print(f"  importable: {importable}")
    print(f"  n_entries_imported: {n_entries_imported}")
    if not importable:
        print(f"  raw output:\n{raw}")
    print()

    # 5. Compute dual-SHA over post-edit state (this script + post-edit canonical + pinmap)
    script_path = Path(__file__).resolve()                        # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins_pre)
    print(f"=== Dual-SHA closure (S84+ schema) ===")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # 6. Append allowlist row (using audit_sha as the per-row SHA pin)
    appended_allowlist, row = append_allowlist_row(audit_sha)
    if appended_allowlist:
        print(f"=== Appended W8-94 row to methodology-wave-allowlist.md ===")
    else:
        print("=== W8-94 row already present in methodology-wave-allowlist.md (idempotent) ===")
    allowlist_text_after = ALLOWLIST_PATH.read_text(encoding="utf-8")
    allowlist_now_has_row = "S88-CHANNEL-LABEL-NORMALIZATION" in allowlist_text_after
    print(f"  allowlist_now_has_row: {allowlist_now_has_row}")
    print()

    # 7. Evaluate gate
    verdict = evaluate_gate(
        appended_canonical=appended_canonical,
        canonical_now_has_dict=canonical_now_has_dict,
        importable=importable,
        n_entries=n_entries_imported,
        appended_allowlist=appended_allowlist,
        allowlist_now_has_row=allowlist_now_has_row,
    )

    # 8. 4-tuple emission
    value_str = (
        f"dict-22-entries-pinned={canonical_now_has_dict};"
        f"importable={importable};"
        f"n_entries={n_entries_imported};"
        f"allowlist-appended={allowlist_now_has_row}"
    )
    print(f"(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # 9. Persist NPZ summary (substrate-IS structural artifact)
    try:
        import numpy as np  # (local) numpy used only for npz packaging
        np.savez(
            OUT_NPZ,
            n_entries=np.int64(n_entries_imported if importable else len(labels)),
            n_diagonal=np.int64(4),
            n_off_diagonal=np.int64(18),
            keys=np.array(sorted(labels.keys()), dtype=object),
            values=np.array([labels[k] for k in sorted(labels.keys())], dtype=object),
            audit_sha256=audit_sha,
            content_sha256=content_sha,
            verdict=verdict,
            allow_pickle=True,
        )
        print(f"  npz: {OUT_NPZ}")
    except Exception as exc:
        print(f"  npz emission skipped ({exc!r})")

    # 10. Append verdict line + dual-SHA companion (atomic single-write each)
    append_verdict(verdict, value_str, audit_sha, content_sha)

    wall = time.time() - t0                                       # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
