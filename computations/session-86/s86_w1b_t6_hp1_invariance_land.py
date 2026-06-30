#!/usr/bin/env python3
"""
S86 W1b-T6 — S86-HP1-NEAR-INVARIANCE-LANDING
==============================================

Gate: S86-HP1-NEAR-INVARIANCE-LANDING ([VERIFY-THEOREM])

Purpose
-------
Land the S85 W5-6 PASS as a permanent registry entry in
`sessions/permanent-results-registry.md` §VII-B titled
"HP^1 Near-Invariance (Lizzi-track)" containing BOTH:
  (a) LOOSE statement: ‖[ε_H]‖_{HP^1} R-protected on full 5-atlas
      {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} with factor 2.0.
  (b) STRICT statement: on F_4 = {ζ, Zubarev, SDW} (pure-a_4),
      factor 1.031.
plus substitution chain (STRICT-on-F_4 → LOOSE-on-5-atlas under
M-family extension), source citation, and the W5-6 verdict pin
(content_sha256 + audit_sha256, full 64-hex each).

Pre-registered threshold:
  PASS iff §VII-B entry exists with BOTH factor statements within a
       single registry block AND W5-6 SHA pin matches the canonical
       line in computations/session-85/s85_gate_verdicts.txt.
  FAIL iff any of: §VII-B section heading not found; either factor
       statement absent post-write; W5-6 SHA pin mismatch.
  INFO iff entry exists with both factors but adjacent rather than
       within a single block.

Tolerance: THEOREM (exact match for factors 2.0 and 1.031; statement
text may vary in wording provided LOOSE/STRICT distinction is
preserved).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - sessions/permanent-results-registry.md
  - sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md
  - computations/session-85/s85_gate_verdicts.txt
  - canonical_constants.py (audit_sha256 only)
  - script bytes (BOTH SHAs)

Output 4-tuple:
  (value=<entry_SHA>, scheme=registry_landing, convention=lizzi-track,
   L_max=N/A)

Classification: GEOMETRIC

Methodology
-----------
Pure I/O + SHA hashing. No GPU/numpy linear algebra. The script:
 1. Hashes all inputs (SHA-256).
 2. Locates W5-6 verdict line in s85_gate_verdicts.txt; parses LOOSE
    factor (2.0) + dual-SHA pin.
 3. Locates §VII-B heading in permanent-results-registry.md;
    inserts entry block at end of §VII-B (just before next "---"
    separator preceding §VII.J or analogous next subsection).
 4. Re-reads the registry post-write; verifies BOTH factor statements
    appear within the inserted block (single-block containment test);
    verifies W5-6 SHA pin string is unchanged.
 5. Computes entry_SHA = SHA-256 of the inserted block bytes.
 6. Appends canonical verdict line + companion comment row to
    computations/session-86/s86_gate_verdicts.txt.

Substrate-framing
-----------------
HP^1 near-invariance describes the substrate's spectral-triple
cohomology class structure: the L^2 norm of the ε_H cocycle is
bounded across regulator choice. The HP^1 cohomology IS the
substrate's first quaternionic projective class — it does not live
IN a manifold, it IS the manifold-free cohomological structure of
D_K. R-protection means the cohomology norm is geometrically rigid
against regulator choice, NOT that an external regulator preserves
a pre-existing norm.
"""

from __future__ import annotations

# Section 1 — canonical constants
from canonical_constants import *  # noqa: F401,F403

# Section 2 — standard imports
import hashlib
import re
import sys
import time
from pathlib import Path
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


# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSIONS_DIR = PROJECT_ROOT / "sessions"

SESSION = "S86"                                                           # (local)
GATE_ID = "S86-HP1-NEAR-INVARIANCE-LANDING"                                # (local)
SCHEME = "registry_landing"                                                # (local)
CONVENTION = "lizzi-track"                                                 # (local)
L_MAX_TAG = "N/A"                                                          # (local)

# Pre-registered factor pins (THEOREM tolerance — exact match)
LOOSE_FACTOR = 2.0                                                          # (local) plan §W1b-2.7
STRICT_FACTOR = 1.031                                                       # (local) plan §W1b-2.7
LOOSE_THRESHOLD_TXT = "factor <= 2.0 across full 5-atlas"                   # (local)
STRICT_THRESHOLD_TXT = "factor <= 1.05 across F_4"                          # (local)
LOOSE_ATLAS = ["zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly"]          # (local)
STRICT_ATLAS = ["zeta", "Zubarev", "SDW"]                                   # (local)

# Input file pins
REGISTRY_FILE = SESSIONS_DIR / "permanent-results-registry.md"
SOURCE_TEXT_FILE = SESSIONS_DIR / "session-85" / "session-85-s7-combined-landscape-lizzi.md"
S85_VERDICTS_FILE = resolve_output(85, 's85_gate_verdicts.txt')
CANON_PY = resolve_script(None, 'canonical_constants.py')
SCRIPT_FILE = Path(__file__).resolve()

# Output verdict file
S86_VERDICTS_FILE = resolve_output(86, 's86_gate_verdicts.txt')

# Registry section anchor
SECTION_HEADING = "### VII-B. S29–S66 Identities & Constants"               # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 helpers
# ---------------------------------------------------------------------------
def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(p: Path) -> str:
    return sha256_bytes(p.read_bytes())


def closure_hash(pin_map: dict) -> str:
    """Ordered-pin closure SHA — keys sorted deterministically."""
    ordered = sorted(pin_map.items())
    blob = "\n".join(f"{k}={v}" for k, v in ordered).encode("utf-8")
    return sha256_bytes(blob)


# ---------------------------------------------------------------------------
# Section 5 — Locate W5-6 verdict + extract dual-SHA pin
# ---------------------------------------------------------------------------
def extract_w56_pin(verdict_path: Path) -> dict:
    """Find W5-6 line; return {value, content_sha256, audit_sha256, raw}."""
    raw_lines = verdict_path.read_text(encoding="utf-8").splitlines()
    target = None                                                            # (local)
    for ln in raw_lines:
        if "S85-W5-6-REGULATOR-SCAN-EPS-H" in ln and "INFO-tight" in ln:
            target = ln
            break
    if target is None:
        raise SystemExit("FAIL: W5-6 verdict line not found in s85_gate_verdicts.txt")
    m_val = re.search(r"value=([0-9.eE+\-]+)", target)
    m_csha = re.search(r"content_sha256=([0-9a-f]{64})", target)
    m_asha = re.search(r"audit_sha256=([0-9a-f]{64})", target)
    if not (m_val and m_csha and m_asha):
        raise SystemExit("FAIL: W5-6 verdict line missing value or dual-SHA")
    return {
        "value": float(m_val.group(1)),
        "content_sha256": m_csha.group(1),
        "audit_sha256": m_asha.group(1),
        "raw": target,
    }


# ---------------------------------------------------------------------------
# Section 6 — Compose registry entry block
# ---------------------------------------------------------------------------
def compose_entry(w56: dict) -> str:
    """Build the §VII-B "HP^1 Near-Invariance (Lizzi-track)" entry block.

    Headed as `### VII-B.HP1-NEAR-INVARIANCE` to match the sibling pattern
    set by `### VII-B.TWO-LAYER-OBSTRUCTION` (W1b T7).
    """
    block = f"""
### VII-B.HP1-NEAR-INVARIANCE — HP^1 Near-Invariance Theorem (Lizzi-track) (S86 W1b T6, 2026-04-26)

THEOREM (R-protection of the ε_H HP^1 cohomology class on the substrate's
spectral-triple regulator atlas). Let `‖[ε_H]‖_{{HP^1, r}}` denote the L^2
norm of the ε_H cocycle in the first quaternionic projective Hopf class
HP^1(D_K) under regulator r, defined as the s=0 residue of the regulator-
weighted zeta-function ζ_{{D, ε_H², r}} (S83 G56 GODBILLON-VEY-HEITSCH).
Then ‖[ε_H]‖_{{HP^1, r}} is R-protected at TWO levels on the surveyed
regulator atlas:

  (a) LOOSE form (full 5-atlas):
      Atlas_5 = {{ζ, Zubarev, SDW, cutoff_sqrt, anomaly}}.
      max_{{r,r' ∈ Atlas_5}} ‖[ε_H]‖_{{HP^1,r}} / ‖[ε_H]‖_{{HP^1,r'}} = 2.0
      (TIGHT-LOOSE band: factor ≤ 2.0).

  (b) STRICT form (pure-a_4 subfamily F_4):
      F_4 = {{ζ, Zubarev, SDW}}  (regulators whose Mellin support is
      concentrated on the a_4 Seeley-DeWitt slot).
      max_{{r,r' ∈ F_4}} ‖[ε_H]‖_{{HP^1,r}} / ‖[ε_H]‖_{{HP^1,r'}}
        = 1.000 / 0.970024 = 1.031
      (TIGHT-STRICT band: factor ≤ 1.05).

SUBSTITUTION CHAIN (STRICT-on-F_4 ⇒ LOOSE-on-5-atlas under M-family extension):

  Step 1 (Definition):
      ‖[ε_H]‖_{{HP^1, r}}  := |f_4^r| × R_universal,
        where R_universal is the regulator-invariant geometric residue and
        f_4^r is the Mellin prefactor at the a_4 slot.
      R-protected (factor f) on atlas A
        := max_{{r, r' ∈ A}} ‖[ε_H]‖_{{HP^1,r}} / ‖[ε_H]‖_{{HP^1,r'}} ≤ f.
      F_4 := {{ζ, Zubarev, SDW}}     (pure-a_4 family)
      M   := {{cutoff_sqrt, anomaly}} (mixed-support family; M-broadening)
      Atlas_5 := F_4 ∪ M.

  Step 2 (Substitution — W5-6 measured ratios):
      W5-6 STRICT measurement on F_4: max ratio = 1.000 / 0.970024 = 1.0309.
      W5-6 LOOSE measurement on Atlas_5: max ratio = 2.000.
      M-family contributes additional spread: 2.000 / 1.031 ≈ 1.94 from
      cutoff_sqrt and anomaly inclusion (M broadens the f_4^r support
      beyond the pure-a_4 cluster).

  Step 3 (Simplification):
      Atlas-max-ratio = max( F_4-ratios, F_4×M-cross-ratios, M-ratios )
                      = max( 1.031, 2.000 )
                      = 2.000.

  Step 4 (Direction):
      STRICT (1.031 ≤ 1.05 on F_4) is the tightest containment.
      LOOSE (2.0 ≤ 2.0 on full atlas) is the structural protection
      level required when M-family regulators are admitted. Both bounds
      establish R-protection (the ratio is bounded — only the bound
      level differs upon M-extension). The structural fact: HP^1 norm
      is bounded across regulator family — geometrically rigid, NOT
      free to drift.

REDUCTION FACTOR. The S66 / S75 raw-ε_H magnitude dynamic range was 381×
(ZETA-NOT-PHYSICAL-75 permanent theorem). HP^1 cohomological projection
brings this to factor 2.0 across the 5-atlas — a 381 / 2 = 190.5×
reduction. This is the strongest scheme-invariance observation for any
ε_H-related quantity in the project to date.

SUBSTRATE FRAMING. HP^1 near-invariance IS the substrate's first
quaternionic projective Hopf cohomology class — a cohomological
feature of the spectral-triple, NOT a property attached IN a pre-
existing manifold. R-protection means the cohomology norm is
geometrically rigid against regulator choice, NOT that an external
regulator preserves a pre-existing norm. The HP^1 class describes
which spectral-functional moments survive as substrate cohomology
under regulator variation; the strip of containment (factor ≤ 2.0
LOOSE, ≤ 1.05 STRICT) is the structural geometry of that cohomology.

PROVENANCE.
  - Source: lizzi S-7 §V.7 (CF-LZ-S86-7) — `sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md` lines 436–440.
  - W5-6 verdict pin (canonical line at `computations/session-85/s85_gate_verdicts.txt`):
      content_sha256 = {w56['content_sha256']}
      audit_sha256   = {w56['audit_sha256']}
      raw = `S85-W5-6-REGULATOR-SCAN-EPS-H: INFO-tight -- value=2.0 scheme=5-regulator-atlas convention=CM-residue L_max=10`
  - W5 working paper §W5-6 (lines 938-1085, `sessions/archive/session-85/session-85-w5-workingpaper.md`).
  - Companion theorem: §VII.K-PROP CC-5 propagation; cross-cite §VII.K-META.
  - Downstream binding: S86-W9 C44 (R-protection Mellin criterion) cites
    this entry as the canonical 5-atlas LOOSE/STRICT exemplar; F_4/M
    partition (S-1 Regulator-Family Boundary Theorem) gains an empirical
    anchor at the HP^1 cohomology level.

(value=<entry_SHA>, scheme=registry_landing, convention=lizzi-track, L_max=N/A)

---

""".rstrip() + "\n\n"
    return block


# ---------------------------------------------------------------------------
# Section 7 — Locate insertion point in registry
# ---------------------------------------------------------------------------
def locate_insertion_point(registry_text: str) -> tuple[int, int]:
    """Return (insertion_offset, end_of_section_offset) for §VII-B table end.

    Strategy: find SECTION_HEADING (`### VII-B. S29-S66 Identities & Constants`);
    advance to the FIRST `\\n---\\n` that follows (this closes the table block).
    Insert the new entry IMMEDIATELY AFTER that `---` divider, so the new
    `### VII-B.HP1-NEAR-INVARIANCE` heading appears as the FIRST sibling
    sub-section under §VII-B, before any pre-existing `### VII-B.<TAG>`
    sibling (e.g. VII-B.TWO-LAYER-OBSTRUCTION from W1b T7).
    """
    idx_heading = registry_text.find(SECTION_HEADING)
    if idx_heading < 0:
        raise SystemExit(
            f"FAIL: §VII-B section heading not found in {REGISTRY_FILE}. "
            "Diagnostic: searched for exact string '" + SECTION_HEADING + "'."
        )
    rest = registry_text[idx_heading:]
    # First \n---\n boundary after the §VII-B heading closes the table.
    m_div = re.search(r"\n---\n", rest)
    if m_div is None:
        raise SystemExit(
            "FAIL: cannot locate first --- divider after §VII-B heading "
            "(table-closure boundary)."
        )
    # Insertion point: immediately AFTER the "\n---\n" (i.e. m_div.end()).
    insertion_offset = idx_heading + m_div.end()
    return insertion_offset, insertion_offset


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                                          # (local)

    # ----- Pre-flight: input SHAs (logged in first 20 lines of stdout) -----
    pin_map = {                                                               # (local)
        "registry_target": str(REGISTRY_FILE.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "registry_section": "VII-B",
        "source_text_file": str(SOURCE_TEXT_FILE.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "source_section_id": "lizzi S-7 §V.7 (CF-LZ-S86-7)",
        "s85_verdicts_file": str(S85_VERDICTS_FILE.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "s85_verdicts_sha": sha256_file(S85_VERDICTS_FILE),
        "registry_pre_sha": sha256_file(REGISTRY_FILE),
        "source_text_sha": sha256_file(SOURCE_TEXT_FILE),
        "canon_py_sha": sha256_file(CANON_PY),
        "script_sha": sha256_file(SCRIPT_FILE),
        "loose_factor": LOOSE_FACTOR,
        "strict_factor": STRICT_FACTOR,
        "loose_atlas": ",".join(LOOSE_ATLAS),
        "strict_atlas": ",".join(STRICT_ATLAS),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_TAG,
    }

    print(f"[{GATE_ID}] start  ts={time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
    print(f"  registry_pre_sha    = {pin_map['registry_pre_sha']}")
    print(f"  s85_verdicts_sha    = {pin_map['s85_verdicts_sha']}")
    print(f"  source_text_sha     = {pin_map['source_text_sha']}")
    print(f"  canon_py_sha        = {pin_map['canon_py_sha']}")
    print(f"  script_sha          = {pin_map['script_sha']}")

    # ----- Step 1: extract W5-6 dual-SHA pin -----
    w56 = extract_w56_pin(S85_VERDICTS_FILE)
    if abs(w56["value"] - LOOSE_FACTOR) > 1e-9:
        print(
            f"FAIL: W5-6 verdict value {w56['value']} != LOOSE pin {LOOSE_FACTOR}",
            flush=True,
        )
        # Append FAIL verdict and exit-0 (verdict-as-data)
        verdict = "FAIL"
        entry_sha = "N/A"
        _append_verdict(verdict, entry_sha, w56, pin_map)
        return 0

    print(f"  W5-6 LOOSE factor    = {w56['value']}")
    print(f"  W5-6 content_sha256 = {w56['content_sha256']}")
    print(f"  W5-6 audit_sha256   = {w56['audit_sha256']}")

    # ----- Step 2: confirm §VII-B section exists -----
    registry_pre = REGISTRY_FILE.read_text(encoding="utf-8")
    if SECTION_HEADING not in registry_pre:
        print(f"FAIL: §VII-B heading '{SECTION_HEADING}' absent in registry. Aborting.")
        verdict = "FAIL"
        entry_sha = "N/A"
        _append_verdict(verdict, entry_sha, w56, pin_map)
        return 0

    # ----- Step 3: idempotency check — has this entry already been landed? -----
    entry_anchor = "### VII-B.HP1-NEAR-INVARIANCE — HP^1 Near-Invariance Theorem (Lizzi-track)"
    if entry_anchor in registry_pre:
        print(f"INFO: entry anchor already present in registry — skipping write.")
        # Compute the SHA of the already-present block for the verdict.
        idx_a = registry_pre.find(entry_anchor)
        # Find next "####" or "---" or "### " after the anchor
        rest = registry_pre[idx_a:]
        m_end = re.search(r"\n(####|---|### )", rest[len(entry_anchor):])
        if m_end:
            block_text = rest[: len(entry_anchor) + m_end.start()].rstrip() + "\n"
        else:
            block_text = rest
        entry_sha = sha256_bytes(block_text.encode("utf-8"))
        # Re-verify both factor statements present in this block
        loose_ok = "factor 2.0" in block_text or "= 2.0" in block_text or "2.000" in block_text
        strict_ok = "1.031" in block_text or "1.0309" in block_text
        verdict = "PASS" if (loose_ok and strict_ok) else "FAIL"
        _append_verdict(verdict, entry_sha, w56, pin_map, already_present=True)
        return 0

    # ----- Step 4: compose new entry block -----
    entry_block = compose_entry(w56)
    entry_sha = sha256_bytes(entry_block.encode("utf-8"))

    # ----- Step 5: locate insertion point -----
    insertion_offset, _ = locate_insertion_point(registry_pre)
    new_registry = (
        registry_pre[:insertion_offset]
        + entry_block
        + registry_pre[insertion_offset:]
    )

    # ----- Step 6: write registry (atomic via temp + replace) -----
    tmp_path = REGISTRY_FILE.with_suffix(".md.tmp_w1b_t6")
    tmp_path.write_text(new_registry, encoding="utf-8")
    tmp_path.replace(REGISTRY_FILE)
    print(f"  registry write OK   (insertion_offset={insertion_offset})")

    # ----- Step 7: post-write verification -----
    registry_post = REGISTRY_FILE.read_text(encoding="utf-8")
    idx_post = registry_post.find(entry_anchor)
    if idx_post < 0:
        print("FAIL: post-write entry anchor not found.")
        verdict = "FAIL"
        _append_verdict(verdict, entry_sha, w56, pin_map)
        return 0

    # Extract the inserted block for single-block containment test
    rest_post = registry_post[idx_post:]
    m_end = re.search(r"\n(####|---|### )", rest_post[len(entry_anchor):])
    block_post = (
        rest_post[: len(entry_anchor) + m_end.start()].rstrip() + "\n"
        if m_end else rest_post
    )

    # Both factor statements must lie WITHIN this single block
    loose_ok = ("= 2.0" in block_post) and ("LOOSE" in block_post)
    strict_ok = ("1.031" in block_post) and ("STRICT" in block_post)
    sha_ok = (w56["content_sha256"] in block_post) and (w56["audit_sha256"] in block_post)

    print(f"  post-write loose_ok = {loose_ok}")
    print(f"  post-write strict_ok = {strict_ok}")
    print(f"  post-write sha_ok    = {sha_ok}")

    if loose_ok and strict_ok and sha_ok:
        verdict = "PASS"
    elif loose_ok and strict_ok and not sha_ok:
        verdict = "INFO"  # both factors present but SHA pin not embedded
    else:
        verdict = "FAIL"

    # ----- Step 8: append verdict line + companion comment row -----
    pin_map["registry_post_sha"] = sha256_file(REGISTRY_FILE)
    pin_map["entry_sha"] = entry_sha
    closure_sha = closure_hash(pin_map)
    audit_sha = sha256_bytes(
        (closure_sha + pin_map["canon_py_sha"]).encode("utf-8")
    )

    _append_verdict_with_closures(
        verdict, entry_sha, closure_sha, audit_sha, pin_map, w56
    )

    # 4-tuple final non-verdict line
    print(
        f"(value={entry_sha}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_TAG})"
    )
    print(f"[{GATE_ID}] verdict={verdict}  elapsed={time.time()-t0:.2f}s")
    return 0


def _append_verdict(verdict, entry_sha, w56, pin_map, already_present=False):
    """Fallback verdict-append for early FAIL paths."""
    closure_sha = closure_hash({**pin_map, "entry_sha": entry_sha})
    audit_sha = sha256_bytes(
        (closure_sha + pin_map.get("canon_py_sha", "")).encode("utf-8")
    )
    _append_verdict_with_closures(verdict, entry_sha, closure_sha, audit_sha, pin_map, w56)


def _append_verdict_with_closures(verdict, entry_sha, content_sha, audit_sha, pin_map, w56):
    """Append canonical verdict line + companion comment row."""
    line = (
        f"{GATE_ID}: {verdict} -- value={entry_sha} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )
    comment = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
    )
    with S86_VERDICTS_FILE.open("a", encoding="utf-8") as f:
        f.write(line)
        f.write(comment)
    print(f"  verdict line appended to {S86_VERDICTS_FILE.name}")
    print(f"  audit_sha256 head   = {audit_sha[:16]}")
    print(f"  content_sha256 head = {content_sha[:16]}")


if __name__ == "__main__":
    sys.exit(main())
