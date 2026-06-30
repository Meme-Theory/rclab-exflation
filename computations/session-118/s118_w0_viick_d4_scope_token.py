#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S118 W0-2 CF-S118-HK-VIICK-D4-SCOPE-TOKEN — §VII.CK D4 scope-token hygiene patch
================================================================================

Gate: CF-S118-HK-VIICK-D4-SCOPE-TOKEN ([AUDIT])
Classification: NON-PHONONIC (registry-hygiene / scope-token methodology; the §VII.CK
  theorem itself is GEOMETRIC, the GATE is the scope-inside-token patch).

GREP-VERIFIER CANONICAL-IMPORT EXEMPTION (pre-registered): this is a PURE grep-verifier;
it consumes NO canonical constant. It MUST NOT import canonical_constants.py, and
canonical_constants.py is DELIBERATELY ABSENT from input_files + the audit_sha256 pinmap.
The `.claude/hooks/python-validate.sh` Check-1 WARN ("script does not import
canonical_constants") is a pre-registered WARN-only exemption per
`feedback_grep-verifier-canonical-import-exemption.md` (S117 W0-2). Do NOT add a dead import.

Pre-registered threshold (artifact-existence grep; NOT a numerical threshold):
  Over the §VII.CK D4 surface, EXCLUDING bracketed "[PRIOR CONTESTED-STATE NARRATIVE —
  RETAINED VERBATIM FOR AUDIT-TRAIL:] … [PRIOR D4-open AUDIT-TRAIL RETAINED VERBATIM
  ABOVE.]" regions:
    PASS iff grep_count(LIVE bare `t(O)=±1[^)]{0,40}center-character selection rule`) == 0
            AND the scoped token pattern
              `t(O)=±1.{0,80}(coset-shift|generation-slot-permutation).{0,40}NOT.{0,20}(Z₃|Z3) center character`
            is present (>= 2, one per patched LIVE occurrence)
            AND every LIVE `0≠±1 (mod 3)` carries the inline coset-shift scope.

Method: carry the corrected coset-shift scope INSIDE each of the two LIVE bare `t(O)=±1`
center-character tokens — occurrence A (four-door D4 table cell "Closing fact", the
DECIDED-S114-W-2 sentence) and occurrence G (D4-disposition annotation). The coset-shift
reading (`t(O)=±1` = coset-SHIFT / generation-slot-permutation grading, NOT the Z₃ center
character) was established S116 W2-1 + S117 W2-1, both already in the live D4 surface; this
gate carries it INSIDE the bare tokens so a skim/aggregation cannot regenerate the
blind-reviewer-REJECTED center-character mis-reading. Per `regulator-pin-discipline.md
§"Channel-Scope Suffix Discipline"`: scope-inside-the-token (separable parentheticals do not
survive aggregation). EXEMPT (NOT edited): the bracketed verbatim-retained audit-trail blocks.

Single-shot AFTER-pattern (build text -> write_atomic_with_fsync -> re-read+verify -> emit
exactly one verdict line) per `.claude/rules/registry-landing.md` §"Bridge-Landing Script
Architecture". Surgical string-replacement designated-writer patch (NOT a bulk append) per
`feedback_framework-hygiene.md`.

Provenance: S118 W0-2 plan `sessions/session-plan/session-118-plan-w0.md` §W0-2.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S118"                                                # (local)
GATE_ID = "CF-S118-HK-VIICK-D4-SCOPE-TOKEN"                     # (local)
SCHEME = "REGISTRY-VIICK-D4-SCOPE-TOKEN-PATCH"                  # (local)
CONVENTION = "SCOPE-INSIDE-TOKEN-coset-shift-NOT-Z3-center-character"  # (local)
L_MAX = "N/A"                                                   # (local)

REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

# Exempt audit-trail region delimiters (everything between is verbatim-retained, NOT edited).
EXEMPT_OPEN = "[PRIOR CONTESTED-STATE NARRATIVE — RETAINED VERBATIM FOR AUDIT-TRAIL:]"
EXEMPT_CLOSE = "[PRIOR D4-open AUDIT-TRAIL RETAINED VERBATIM ABOVE.]"

# ---- The two LIVE bare-token surgical replacements (exact, each unique file-wide) ----

# Occurrence A — four-door D4 table cell "Closing fact" (the DECIDED-S114-W-2 sentence).
A_OLD = ("outside `Ω¹_{D_K}(A_K)` by the `t(O)=±1≠0` center-character selection rule "
         "(W3-1's residual=1 is the numerical shadow).")
A_NEW = ("outside `Ω¹_{D_K}(A_K)` by the `t(O)=±1≠0` coset-shift / generation-slot-permutation "
         "grading — NOT the Z₃ center character (the coset-SHIFT reading per S116 W2-1 / S117 W2-1; "
         "the \"center-character selection rule\" phrasing is the blind-reviewer-REJECTED "
         "mis-reading; W3-1's residual=1 is the numerical shadow).")

# Occurrence G — D4-disposition annotation (the role-3 admissibility sentence).
G_OLD = ("OUTSIDE `Ω¹_{D_K}(A_K)` by the `t(O)=±1≠0` center-character selection rule "
         "(the cross-generation handle SHIFTS triality cosets, `t(O)=±1`; every `A_K` one-form "
         "is coset-preserving, `t(O)=0`; `0≠±1 (mod 3)` ⇒ group-theoretically excluded, "
         "EXACT ∀ L_max — W3-1 residual=1.000000 is the numerical shadow).")
G_NEW = ("OUTSIDE `Ω¹_{D_K}(A_K)` by the `t(O)=±1≠0` coset-shift / generation-slot-permutation "
         "grading — NOT the Z₃ center character (the coset-SHIFT reading per S116 W2-1 / S117 W2-1; "
         "the \"center-character selection rule\" phrasing is the blind-reviewer-REJECTED mis-reading) "
         "— the cross-generation handle SHIFTS triality cosets (`t(O)=±1`), every `A_K` one-form "
         "is coset-preserving (`t(O)=0`), so `0≠±1 (mod 3)` ⇒ group-theoretically excluded "
         "(the coset-SHIFT grading, NOT the Z₃ center character; EXACT ∀ L_max — "
         "W3-1 residual=1.000000 is the numerical shadow).")

REPLACEMENTS = [("A", A_OLD, A_NEW), ("G", G_OLD, G_NEW)]

SCOPED_PAT = re.compile(
    r"t\(O\)=±1.{0,80}(coset-shift|generation-slot-permutation).{0,40}NOT.{0,20}(Z₃|Z3) center character")
BARE_PAT = re.compile(r"t\(O\)=±1[^)]{0,40}center-character selection rule")
MOD_PAT = re.compile(r"0\s*≠\s*±1\s*\(mod 3\)")


# ---------------------------------------------------------------------------
# SHA + surface helpers
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def extract_viick_surface(text: str) -> str:
    m = re.search(r"### §VII\.CK", text)  # (local)
    if not m:
        raise RuntimeError("§VII.CK header not found")
    start = m.start()  # (local)
    nxt = re.search(r"\n### §VII\.(?!CK)", text[start + 10:])  # (local)
    end = start + 10 + nxt.start() if nxt else len(text)  # (local)
    return text[start:end]


def strip_exempt(s: str) -> str:
    out = []  # (local)
    i = 0  # (local)
    while True:
        a = s.find(EXEMPT_OPEN, i)
        if a < 0:
            out.append(s[i:])
            break
        b = s.find(EXEMPT_CLOSE, a)
        if b < 0:
            out.append(s[i:])
            break
        out.append(s[i:a])
        i = b + len(EXEMPT_CLOSE)
    return "".join(out)


def write_atomic_with_fsync(text: str, path: Path) -> None:
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())


# ---------------------------------------------------------------------------
# Verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "") -> dict:
    payload: dict = {
        "session": 118,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} — input SHA-256 pins (grep-verifier; NO canonical_constants) ===")
    print(f"  permanent-results-registry.md (pre): {sha256_of(REGISTRY)[:16]}...")
    print()

    original = REGISTRY.read_text(encoding="utf-8")

    # Pre-patch LIVE diagnostics
    surf0 = extract_viick_surface(original)
    live0 = strip_exempt(surf0)
    print("--- pre-patch LIVE token census (exempt audit-trail regions stripped) ---")
    print(f"  bare  t(O)=±1...center-character selection rule : {len(BARE_PAT.findall(live0))}")
    print(f"  scoped coset-shift...NOT...Z₃ center character   : {len(SCOPED_PAT.findall(live0))}")
    print(f"  0≠±1 (mod 3)                                     : {len(MOD_PAT.findall(live0))}")
    print()

    # Apply the two surgical replacements (idempotent: skip an already-scoped occurrence).
    text = original
    applied = []  # (local)
    for tag, old, new in REPLACEMENTS:
        if new in text:
            applied.append((tag, "ALREADY-SCOPED"))
            continue
        cnt = text.count(old)  # (local)
        if cnt != 1:
            raise RuntimeError(f"occurrence {tag}: anchor count={cnt} (expected 1); refusing to patch")
        text = text.replace(old, new, 1)
        applied.append((tag, "PATCHED"))
    print(f"--- replacements: {applied} ---")

    if text != original:
        write_atomic_with_fsync(text, REGISTRY)
        print("    write_atomic_with_fsync OK")
    else:
        print("    no change (idempotent no-op)")
    print()

    # Re-read (post-fsync) + verify on the LIVE surface.
    landed = REGISTRY.read_text(encoding="utf-8")
    surf = extract_viick_surface(landed)
    live = strip_exempt(surf)

    bare_count = len(BARE_PAT.findall(live))           # (local)
    scoped_count = len(SCOPED_PAT.findall(live))       # (local)
    # every LIVE 0≠±1 (mod 3) must carry the coset-shift scope within a +/-220-char window
    mod_unscoped = 0  # (local)
    for mm in MOD_PAT.finditer(live):
        w = live[max(0, mm.start() - 220): mm.end() + 220]  # (local)
        if ("coset-SHIFT" not in w) and ("coset-shift" not in w):
            mod_unscoped += 1
    # exempt blocks must be UNTOUCHED (still present, count preserved)
    exempt_open_ct = landed.count(EXEMPT_OPEN)         # (local)
    exempt_close_ct = landed.count(EXEMPT_CLOSE)       # (local)

    print("--- post-patch LIVE verify ---")
    print(f"  bare  (must be 0)                : {bare_count}")
    print(f"  scoped (must be >= 2)            : {scoped_count}")
    print(f"  0≠±1 (mod 3) unscoped (must be 0): {mod_unscoped}")
    print(f"  exempt-block markers preserved   : open={exempt_open_ct} close={exempt_close_ct} (expect 2/2)")

    all_ok = bool(
        bare_count == 0
        and scoped_count >= 2
        and mod_unscoped == 0
        and exempt_open_ct == 2
        and exempt_close_ct == 2
    )
    verdict = "PASS" if all_ok else "FAIL"
    print(f"  => verdict: {verdict}")
    print()

    # Dual-SHA: audit over (script || pinmap) — NO canonical_constants (grep-verifier).
    # content over the patched §VII.CK D4 surface text.
    script_path = Path(__file__).resolve()
    pins = {
        str(REGISTRY.relative_to(PROJECT_ROOT)).replace("\\", "/"): sha256_of(REGISTRY),
    }
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_path.read_bytes())
    h_audit.update(pinmap_json)
    audit_sha = h_audit.hexdigest()           # (local)
    content_sha = sha256_text(surf)           # (local) patched §VII.CK D4 surface text

    value = (f"LIVE_bare_tokens={bare_count}(==0); scoped_coset-shift_tokens={scoped_count}(>=2); "
             f"0!=±1(mod3)_unscoped={mod_unscoped}(==0); exempt_blocks_preserved=2/2; "
             f"occA(table-cell)+occG(D4-disposition) scope-inside-token; "
             f"coset-SHIFT grading NOT Z3 center character (S116 W2-1 / S117 W2-1)")
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print_verdict_payload(verdict, value, audit_sha, content_sha)
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time()-t0:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
