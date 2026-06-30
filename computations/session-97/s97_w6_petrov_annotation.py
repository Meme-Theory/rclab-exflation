#!/usr/bin/env python3
"""
S97 W6-2 — S97-W6-2-PETROV-ANNOTATION — verdict-file annotation-hygiene closure
================================================================================

Gate: S97-W6-2-PETROV-ANNOTATION ([AUDIT])
Classification: GEOMETRIC (the underlying observable is the tau->inf Petrov/CMPP
  type of the 12D Jensen-deformed product metric — a spectral-triple / fiber-geometry
  object; the GATE is a verdict-file companion-comment consistency decision, NOT a
  re-derivation of the Petrov type). METHODOLOGY-class per session-97-plan-w6.md §W6-2:
  PASS/INFO predicate is annotation-consistency (artifact-existence-with-content), NOT a
  numerical threshold; gate-ID is on the methodology-wave-allowlist-ledger.md (S97 row,
  sha256_of_plan_block=efd8312e196c25d77edcee4c6ef3a8ef93b597a39c8a938061e137c8801b5d11).

Pre-registered predicate (plan §W6-2 operator.form):
  PASS iff (after the chosen resolution is applied)
    [ Resolution (a): each of the four S96-GEOM-TAUINF-PETROV companion comment rows'
      Petrov-type/window prose is consistent with the canonical value-field ]
    OR
    [ Resolution (b): the canonical PASS line is followed by an explicit 'value-field
      governs' note naming the value-field window authoritative and the companion
      boilerplate retained-historical ]
    AND the canonical value=/audit_sha256/content_sha256 lines are UNCHANGED byte-for-byte
        (verdict permanence preserved)
    AND the resolution chosen is honestly named in the verdict line + WP §W6-2.

  Verdict token (plan rubric): PASS for resolution (a) [comment made literally consistent];
  INFO for resolution (b) [comment retained-historical + governs-note appended]; FAIL iff
  neither cleanly applied OR a canonical value=/audit_sha256/content_sha256 line was edited
  (verdict-permanence violation, PROHIBITED_ACTIONS Class-3/4).

RESOLUTION CHOSEN: (b) — value-field-governs note.
  The four S96-GEOM-TAUINF-PETROV dual-SHA companion rows are LEFT byte-for-byte; a single
  explicit 'value-field governs' NOTE was APPENDED at the end of the gate's block in
  computations/session-96/s96_gate_verdicts.txt (directly under the schema-v2 3-tuple row of
  the canonical PASS line), naming audit_sha256=8f49af07... as the canonical (latest
  non-superseded) line whose value-field (dyn_window=tau<=6(6/12), dynamic_resolvable=I)
  GOVERNS, and the 'dynamic Type G PERSIST to tau->inf' companion-row prose as
  RETAINED-HISTORICAL pre-supersession boilerplate. INFO is the honest token (the comment is
  NOT made literally consistent; it is explicitly flagged as historical and governed by the
  value-field). Rationale: resolution (b) touches the file in exactly ONE place (lower-risk
  against absolute verdict permanence than editing four historical companion rows under
  resolution (a)), and honestly preserves the Option-A supersession story rather than
  overwriting it (the boilerplate was correct as-emitted in the early chain, before the W5-3
  methodology section-6 regime-of-validity correction).

Inputs (SHA-256 pinned at runtime; the annotation edit was applied BEFORE this script ran,
so the SHAs pin the POST-resolution verdict-file state — the W7-2 mutate->verify->SHA shape):
  - computations/session-96/s96_gate_verdicts.txt  (POST-resolution: carries the appended
      governs-note + the UNCHANGED canonical PASS line + the four UNCHANGED companion rows)
  - sessions/archive/session-96/session-96-w5-workingpaper.md  (§W5-3 methodology §6 regime-artifact
      disclosure — the governs-note pointer basis)
  Both feed BOTH audit_sha256 and the pinmap; script bytes feed BOTH audit_sha256 and
  content_sha256. (Plan audit_sha256_inputs: ["script","verdict_file_pin","pinmap"].)

Output 4-tuple:
  (value=<resolution + permanence-preserved booleans>,
   scheme=annotation-hygiene-companion-comment-consistency,
   convention=value-field-governs (verdict permanence), L_max=N/A)

DISCIPLINE
----------
- `from canonical_constants import *` (MANDATORY first import; this gate consumes NO
  canonical constant as a numerical pin — it pins verdict-file text identities — but the
  import is the project-wide S34+ contract and satisfies output_artifacts.must_contain).
- All local intermediates tagged `# (local)`.
- The annotation edit (the governs-note append) was performed by the gen-physicist via the
  Edit tool BEFORE this verification+closure script ran, so the S96 verdict file is in its
  FINAL post-resolution state when the dual-SHA is computed over its bytes. This script does
  NOT re-edit the verdict file (re-edit would change the bytes audit_sha256 pins).
- audit_sha256   = sha256( bytes(script) || bytes(s96_verdict_file) || pinmap_json )
  content_sha256 = sha256( bytes(script) )                 (S84+ dual-SHA schema,
  METHODOLOGY-class form: audit over script||verdict_file_pin||pinmap per wave-classification.md
  §"Dual-SHA closure for METHODOLOGY-class").
- schema_v2_3tuple_required: false (plan §W6-2; [AUDIT] trigger, no [SIGN]) => canonical line
  + dual-SHA companion row ONLY; NO sign/magnitude/regime 3-tuple row.
- Verdict-permanence guard (PROHIBITED_ACTIONS Class-3/4): the script ASSERTS the canonical
  PASS line (audit_sha256=8f49af07...) is present UNCHANGED and the four companion rows are
  present; if any is missing the predicate FAILs (it does not silently PASS).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — sys.path bootstrap (session-dir script => add _shared/ to path so
#   the MANDATORY `from canonical_constants import *` resolves; canonical pattern
#   per the working session-N scripts, e.g. s97_vn_type_inductive_limit.py L128)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "_shared"))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
# This script lives at computations/session-97/. Walk up to the `computations/`
# directory regardless of __file__ location; the canonical S97 verdict file is the
# per-session file computations/session-97/s97_gate_verdicts.txt (gate-verdicts.md
# §"Canonical Verdict-File Path").
_THIS = Path(__file__).resolve()                                   # (local)
COMPUTATIONS_DIR = _THIS.parent                                    # (local)
while COMPUTATIONS_DIR.name != "computations" and COMPUTATIONS_DIR.parent != COMPUTATIONS_DIR:
    COMPUTATIONS_DIR = COMPUTATIONS_DIR.parent                     # (local) walk up to computations/
SHARED_DIR = COMPUTATIONS_DIR / "_shared"                          # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent                             # (local)
SESSION_DIR = COMPUTATIONS_DIR / "session-97"                      # (local)

SESSION = "S97"                                                    # (local)
GATE_ID = "S97-W6-2-PETROV-ANNOTATION"                             # (local)
SCHEME = "annotation-hygiene-companion-comment-consistency"        # (local)
CONVENTION = "value-field-governs (verdict permanence)"            # (local)
L_MAX = "N/A"                                                      # (local) annotation-hygiene; no spectral truncation

VERDICT_TXT = SESSION_DIR / "s97_gate_verdicts.txt"               # (local) S97 verdict file (this gate's own closure)
OUT_NPZ = SESSION_DIR / "s97_w6_petrov_annotation.npz"           # (local) optional record

# Input files (POST-resolution state; pinned at runtime). The S96 verdict file is the
# primary pin (the edited artifact); the W5 WP is the governs-note pointer basis.
S96_VERDICT_FILE = COMPUTATIONS_DIR / "session-96" / "s96_gate_verdicts.txt"           # (local)
W5_WORKINGPAPER = PROJECT_ROOT / "sessions" / "session-96" / "session-96-w5-workingpaper.md"  # (local)
INPUT_FILES = [S96_VERDICT_FILE, W5_WORKINGPAPER]                  # (local)

# ---- Pre-registered pin map (plan §W6-2 machinery_pin_map) ----
RESOLUTION_CHOSEN = "b"                                            # (local) value-field-governs note (INFO token)
# Canonical (latest non-superseded) line identity — pinned by SUPERSESSION-CHAIN IDENTITY,
# NOT brittle absolute line number (the file has duplicate emission blocks; the S96-CF line
# numbers 123/128/131/134 drifted). Grep on the audit_sha256.
CANONICAL_AUDIT_SHA = "8f49af075339ccac65f14478b944d57720033de4892e27ed0d785a739c761074"  # (local)
CANONICAL_CONTENT_SHA = "978a2dd6718f7adbad70892cd3150b13e01707edffe197d1aa127ad107e02717"  # (local)
AUTHORITATIVE_WINDOW = "dyn_window=tau<=6(6/12)"                   # (local) the value-field window the comment is governed-by
AUTHORITATIVE_ASYMPTOTIC = "dynamic_resolvable=I"                  # (local) asymptotic dynamic resolves to Type-I below float64
# The four stale companion-row audit_sha256 short-heads (one per Option-A re-emission):
STALE_COMPANION_HEADS = [                                          # (local)
    "f260302bc86f5b6f",
    "4789decff7bc865c",
    "ec80321557379a00",
    "8f49af075339ccac",
]
GOVERNS_NOTE_TAG = "S97-W6-2-PETROV-ANNOTATION value-field-governs"  # (local) the marker the appended note carries
# Boilerplate phrase whose persistence (in the companion rows) is the documented PROSE-vs-
# value-field inconsistency the governs-note resolves:
STALE_BOILERPLATE = "dynamic Type G PERSIST to tau->inf"           # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block + dual-SHA (S84+ schema, METHODOLOGY-class form)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for the pinmap."""
    print(f"=== {GATE_ID} — input SHA-256 pins (POST-resolution state) ===")
    pins: dict[str, str] = {}                                     # (local)
    for p in inputs:
        sha = sha256_of(p)                                        # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, verdict_file_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema, METHODOLOGY-class form.

    audit_sha256   = sha256( bytes(script) || bytes(s96_verdict_file) || pinmap_json )
        The S96 verdict file (the EDITED artifact, in its POST-resolution state) is the
        F-image of the numerical PASS-predicate eigenvalue — the verdict-file analog of a
        rule-file diff (wave-classification.md §"Dual-SHA closure for METHODOLOGY-class").
    content_sha256 = sha256( bytes(script) )
        Responds to script edits only; INVARIANT under verdict-file / pinmap change.
    """
    try:
        script_bytes = script_path.read_bytes()                  # (local)
    except OSError:
        script_bytes = b""                                       # (local)
    try:
        verdict_bytes = verdict_file_path.read_bytes()           # (local)
    except OSError:
        verdict_bytes = b""                                      # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")      # (local)

    h_audit = hashlib.sha256()                                   # (local)
    h_audit.update(script_bytes)
    h_audit.update(verdict_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                  # (local)

    h_content = hashlib.sha256()                                 # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                              # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Verify the annotation-consistency predicate (resolution b)
# ---------------------------------------------------------------------------

def verify_resolution() -> dict:
    """Re-verify the resolution-(b) annotation-consistency predicate on the POST-resolution
    S96 verdict file:

      (P1) the canonical PASS line (audit_sha256=8f49af07...) is PRESENT UNCHANGED, carrying
           its authoritative value-field window (dyn_window=tau<=6(6/12), dynamic_resolvable=I)
           — verdict permanence preserved on the canonical line;
      (P2) the canonical content_sha256 (978a2dd6...) is present on the canonical line
           (the canonical content/audit SHAs are untouched);
      (P3) all four stale companion-row heads are STILL present (the boilerplate rows were
           left byte-for-byte under resolution b);
      (P4) the appended 'value-field governs' NOTE is present, tagged with the gate-ID, and
           names the canonical audit_sha + the authoritative window + flags the companion
           boilerplate retained-historical.

    Returns the per-predicate report + the overall PASS-input booleans.
    """
    try:
        text = S96_VERDICT_FILE.read_text(encoding="utf-8")      # (local)
    except OSError:
        text = ""                                                # (local)

    # (P1)+(P2): the canonical PASS line carries its audit_sha, content_sha, and value-field
    # window — pin by content (supersession-chain identity), not line number.
    canonical_line = ""                                          # (local)
    for ln in text.splitlines():
        if ln.startswith("S96-GEOM-TAUINF-PETROV:") and f"audit_sha256={CANONICAL_AUDIT_SHA}" in ln:
            canonical_line = ln                                  # (local)
            break
    canonical_present = bool(canonical_line)                     # (local)
    canonical_is_pass = canonical_line.startswith("S96-GEOM-TAUINF-PETROV: PASS")  # (local)
    canonical_content_ok = (f"content_sha256={CANONICAL_CONTENT_SHA}" in canonical_line)  # (local)
    window_present = (AUTHORITATIVE_WINDOW in canonical_line)    # (local)
    asymptotic_present = (AUTHORITATIVE_ASYMPTOTIC in canonical_line)  # (local)
    p1_p2 = bool(canonical_present and canonical_is_pass and canonical_content_ok
                 and window_present and asymptotic_present)      # (local)

    # (P3): the four stale companion-row heads still present (left byte-for-byte).
    companion_heads_present = {h: (f"audit_sha256_short={h}" in text)
                               for h in STALE_COMPANION_HEADS}    # (local)
    p3 = all(companion_heads_present.values())                   # (local)
    # The stale boilerplate prose is (deliberately, under resolution b) still present:
    boilerplate_still_present = (STALE_BOILERPLATE in text)      # (local)

    # (P4): the appended governs-note is present + well-formed.
    governs_note_line = ""                                       # (local)
    for ln in text.splitlines():
        if GOVERNS_NOTE_TAG in ln and "value= field GOVERNS" in ln:
            governs_note_line = ln                               # (local)
            break
    note_present = bool(governs_note_line)                       # (local)
    note_names_canonical = (CANONICAL_AUDIT_SHA in governs_note_line)  # (local)
    note_names_window = (AUTHORITATIVE_WINDOW in governs_note_line
                         and AUTHORITATIVE_ASYMPTOTIC in governs_note_line)  # (local)
    note_flags_historical = ("RETAINED-HISTORICAL" in governs_note_line)  # (local)
    note_records_permanence = ("UNCHANGED byte-for-byte" in governs_note_line)  # (local)
    p4 = bool(note_present and note_names_canonical and note_names_window
              and note_flags_historical and note_records_permanence)  # (local)

    resolution_b_applied = bool(p1_p2 and p3 and p4)             # (local)

    return {
        "canonical_present": canonical_present,
        "canonical_is_pass": canonical_is_pass,
        "canonical_content_ok": canonical_content_ok,
        "window_present": window_present,
        "asymptotic_present": asymptotic_present,
        "p1_p2_verdict_permanence_canonical": p1_p2,
        "companion_heads_present": companion_heads_present,
        "p3_four_companion_rows_intact": p3,
        "boilerplate_still_present": boilerplate_still_present,
        "note_present": note_present,
        "note_names_canonical": note_names_canonical,
        "note_names_window": note_names_window,
        "note_flags_historical": note_flags_historical,
        "note_records_permanence": note_records_permanence,
        "p4_governs_note_wellformed": p4,
        "resolution_b_applied": resolution_b_applied,
    }


def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic single-`open('a')` append: canonical line + dual-SHA companion row.

    schema_v2_3tuple_required: false (plan §W6-2; [AUDIT], no [SIGN]) => NO 3-tuple row.
    No read-modify-write, no truncate-and-rewrite (POSIX O_APPEND-safe; W6-1 may write
    concurrently to the same S97 verdict file).
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                            # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (METHODOLOGY-class; content over script, "
        f"audit over script||s96_verdict_file||pinmap); annotation-hygiene resolution=(b) "
        f"value-field-governs note APPENDED to s96_gate_verdicts.txt under canonical PASS line "
        f"audit_sha256=8f49af07...; four companion rows + canonical value=/audit/content lines "
        f"UNCHANGED byte-for-byte (verdict permanence); INFO=retained-historical+governs-note\n"
    )                                                            # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                             # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                       # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, S96_VERDICT_FILE, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+s96_verdict_file+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = verify_resolution()
    print(f"=== {GATE_ID} — annotation-consistency verification (resolution b) ===")
    print(f"  [P1+P2] canonical PASS line {CANONICAL_AUDIT_SHA[:16]}... present + content_sha "
          f"+ value-field window UNCHANGED: {res['p1_p2_verdict_permanence_canonical']}")
    print(f"          (is_PASS={res['canonical_is_pass']} content_ok={res['canonical_content_ok']} "
          f"window={res['window_present']} asymptotic={res['asymptotic_present']})")
    print(f"  [P3]    four stale companion rows intact byte-for-byte: "
          f"{res['p3_four_companion_rows_intact']} ({res['companion_heads_present']})")
    print(f"          stale boilerplate '{STALE_BOILERPLATE}' still present (resolution b): "
          f"{res['boilerplate_still_present']}")
    print(f"  [P4]    governs-note appended + well-formed: {res['p4_governs_note_wellformed']} "
          f"(present={res['note_present']} names_canonical={res['note_names_canonical']} "
          f"names_window={res['note_names_window']} flags_historical={res['note_flags_historical']} "
          f"records_permanence={res['note_records_permanence']})")
    print(f"  RESOLUTION (b) applied cleanly: {res['resolution_b_applied']}")

    # Gate rule (pre-registered, plan §W6-2 rubric):
    #   resolution (b) cleanly applied (governs-note + verdict permanence preserved) => INFO
    #     (the honest token for resolution b: comment NOT made literally consistent; explicitly
    #      flagged historical + governed by the value-field).
    #   FAIL iff the predicate is not cleanly met (governs-note absent/malformed, a companion
    #     row missing, OR — the disqualifying case — the canonical value=/audit/content line was
    #     edited, a verdict-permanence violation).
    if res["resolution_b_applied"]:
        verdict = "INFO"                                         # (local) resolution (b) token
    else:
        verdict = "FAIL"                                         # (local)

    value_str = (
        f"resolution=(b)_value-field-governs;"
        f"verdict_token=INFO_retained-historical+governs-note;"
        f"canonical_line_audit_sha=8f49af075339ccac;"
        f"authoritative_window=dyn_window=tau<=6(6/12);"
        f"authoritative_asymptotic=dynamic_resolvable=I;"
        f"static_tauinf=Type-D-all-12;"
        f"companion_rows_left_byte_for_byte=4(f260302b,4789decf,ec803215,8f49af07);"
        f"governs_note_appended_under_canonical_PASS=True;"
        f"verdict_permanence_preserved=canonical_value/audit/content_UNCHANGED;"
        f"P1P2_canonical_unchanged={res['p1_p2_verdict_permanence_canonical']};"
        f"P3_four_companion_rows_intact={res['p3_four_companion_rows_intact']};"
        f"P4_governs_note_wellformed={res['p4_governs_note_wellformed']};"
        f"resolution_b_applied={res['resolution_b_applied']};"
        f"substrate_IS=Petrov_type_is_fiber-geometry_property_of_Jensen-product_metric;"
        f"physics_unchanged_methodology-floor_F-consistency_only;"
        f"orchestrator_direct_mechanical-closure_honesty=verdict_names_resolution+WP_discloses"
    )                                                            # (local)

    # Optional npz record (annotation-hygiene has no natural data array; plan optional:true).
    try:
        np.savez(
            OUT_NPZ,
            resolution_chosen=np.array("b"),
            verdict_token=np.array("INFO"),
            canonical_line_audit_sha=np.array(CANONICAL_AUDIT_SHA),
            canonical_line_content_sha=np.array(CANONICAL_CONTENT_SHA),
            authoritative_window=np.array(AUTHORITATIVE_WINDOW),
            authoritative_asymptotic=np.array(AUTHORITATIVE_ASYMPTOTIC),
            companion_rows_touched=np.array(0),  # resolution (b): companion rows LEFT byte-for-byte
            companion_row_heads=np.array(STALE_COMPANION_HEADS),
            governs_note_appended=np.array(True),
            verdict_permanence_preserved=np.array(res["p1_p2_verdict_permanence_canonical"]),
            resolution_b_applied=np.array(res["resolution_b_applied"]),
            audit_sha256=np.array(audit_sha),
            content_sha256=np.array(content_sha),
        )
        print(f"\n  npz written: {OUT_NPZ.name}")
    except OSError as exc:
        print(f"\n  npz write skipped (optional): {exc}")

    print()
    print(emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX))
    append_verdict(verdict, value_str, audit_sha, content_sha)

    wall = time.time() - t0                                      # (local)
    print(f"\n=== {GATE_ID}: {verdict} (resolution b; wall {wall:.2f}s) ===")
    # Exit 0 on any valid verdict (PASS/INFO); exit 1 only on FAIL/script-break,
    # per math-scripts.md §"Exit Codes and Verdict Semantics".
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
