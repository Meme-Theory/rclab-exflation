#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S101-FOAM-PROTECTION-REGISTRY-LANDING  (S101 Wave-6, gate W6-1)
==============================================================

Single-shot bridge-landing of the W4-14 quantum-foam-protection exact operator
identity into `sessions/permanent-results-registry.md` at slot §VII.BM.

AFTER pattern per `.claude/rules/registry-landing.md` §"Bridge-Landing Script
Architecture" + template `computations/_bridge_landing_script_template.py`
(SHA 876c018fafea84742d06934a2061eb765ef41a042cb87ba0f4138caffbe9a68c):

  (1) build_promotion_text(...)  — PURE in-memory assembly of the §VII.BM entry
                                   (no I/O before write); the W-3 SCOPE (FINAL)
                                   blockquote + the W-2 B6(iii) ordering caveat
                                   are extracted VERBATIM (byte-equality of the
                                   anchored span) from the SHA-pinned workshop
                                   files — no paraphrase.
  (2) write_atomic_with_fsync(...) — APPEND the section to the registry, flush+fsync.
                                   (APPEND, not truncate: the registry is a
                                   1.7 MB curated doc; the template's docstring
                                   'w' example is for a single-section file.)
  (3) re_read + verify_section_matches(...) — strict-equality boolean.
  (4) the boolean IS the verdict; print_verdict_payload ONCE; the agent calls
      emit_verdict EXACTLY ONCE. No conditional corrective-rewrite branch exists.

Reroute discipline (PD-2/PD-3): at runtime the script re-scans the registry at
ALL header levels (##/###/####) for §VII letter-slot occupancy; if §VII.BM is
occupied by an intervening landing it reroutes to the next-free §VII letter AND
emits FAIL-with-remediation (NOT PASS) so the slot drift is visible
(`epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race"
item 3). The reserved slot is RESERVED-FOR-S101-W6-1-FOAM-PROTECTION in
`sessions/framework/s101-slot-pre-allocation-lockfile.md`.

This is gate 1 of 7 in the W6 single-writer registry chain
(W6-1 → … → W6-8); the chain executes sequentially (PD-4).

Binding-text rule: every numerical/structural claim is TRANSCRIBED from the
S100a W-3/W-2 frozen workshops + the S100a-EPSLX-FOAM-SURVIVAL PASS anchor; NO
re-derivation. Audit-trail observation pointer:
`computations/_bridge_landing_audit_trail_observation_S87_W5.md`.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path

# --- canonical_constants compliance (math-scripts.md): import even though this
#     is a text-assembly landing — keeps the gate inside the audited surface. ---
sys.path.insert(0, str(Path("computations/_shared").resolve()))
from canonical_constants import *  # noqa: F401,F403  (compliance import)

# ---------------------------------------------------------------------------
# Section 0 — gate identity + path pins
# ---------------------------------------------------------------------------
SESSION = "S101"
GATE_ID = "S101-FOAM-PROTECTION-REGISTRY-LANDING"
SCHEME = "BRIDGE-LANDING-AFTER-PATTERN"
CONVENTION = "SINGLE-SHOT-VERBATIM-EXTRACTION"
L_MAX = "N/A"
RESERVED_SLOT = "§VII.BM"
LOCKFILE_RESERVED_FOR = "RESERVED-FOR-S101-W6-1-FOAM-PROTECTION"

ROOT = Path(".").resolve()
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
W3_WORKSHOP = ROOT / "sessions" / "session-100a" / "workshops" / "s100a-w3-envelope-carrier-workshop.md"
W2_WORKSHOP = ROOT / "sessions" / "session-100a" / "workshops" / "s100a-w2-mass-functional-counting-workshop.md"
FOAM_NPZ = ROOT / "computations" / "session-100a" / "s100a_epslx_foam_survival.npz"
LOCKFILE = ROOT / "sessions" / "framework" / "s101-slot-pre-allocation-lockfile.md"
BRIDGE_TEMPLATE = ROOT / "computations" / "_bridge_landing_script_template.py"
CANONICAL = ROOT / "computations" / "_shared" / "canonical_constants.py"
SCRIPT = Path(__file__).resolve()
OUT_NPZ = ROOT / "computations" / "session-101" / "s101_w6_1_foam_protection_landing.npz"

# Plan-pinned static input SHAs (input_files block, session-101-plan-w6.md §W6-1).
PINNED = {
    "w3_workshop": "851c4c4a2c78b89d0aace56d1e9d25f99d86a218fdcd9c173fb2419c5e9cf488",
    "w2_workshop": "0d805e06dd69814aca25efdabdaccf3ff81a7a2518bc876c31b9186098cca491",
    "foam_npz": "057bf02a607eb5708f8631cd14e84dc5e920629f98a766c264870e3fbf2bb7e7",
    "bridge_template": "876c018fafea84742d06934a2061eb765ef41a042cb87ba0f4138caffbe9a68c",
}

# Anchor PRIMARY (S100a-EPSLX-FOAM-SURVIVAL PASS) — full 64-hex.
FOAM_SURVIVAL_AUDIT = "c46b1f6cf67d0fb60f52cc5499a04ad8206cabc3bbb6d57d7f80d54882c32fb1"


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# Section 1 — verbatim extraction (byte-equality of the anchored span)
# ---------------------------------------------------------------------------
def extract_w3_scope_final() -> str:
    """Extract the W-3 'ε_LX SCOPE (FINAL)' blockquote VERBATIM.

    Anchor: the blockquote line beginning '> **ε_LX SCOPE (FINAL).**' through the
    closing landing-sentence quote ending '...carrier-reading-ROBUST."*' (the Q5
    WITH-clause ruling). Returns the single blockquote line stripped of the
    leading '> ' markdown blockquote marker (the landed entry re-frames it as
    body text). Byte-equality of the source span is the verbatim guarantee.
    """
    text = W3_WORKSHOP.read_text(encoding="utf-8")
    lines = text.split("\n")
    start = None
    for i, ln in enumerate(lines):
        if ln.startswith("> **ε_LX SCOPE (FINAL).**"):
            start = i
            break
    if start is None:
        raise RuntimeError("W-3 SCOPE (FINAL) anchor not found — extraction FAIL")
    span = lines[start]
    if 'carrier-reading-ROBUST."*' not in span:
        raise RuntimeError("W-3 landing-sentence terminal anchor not found in span — extraction FAIL")
    # strip the leading blockquote marker '> ' for body re-framing; the content is byte-verbatim.
    return span[2:] if span.startswith("> ") else span


def extract_w2_b6iii() -> str:
    """Extract the W-2 B6(iii) ordering-caveat binding content VERBATIM.

    Anchor: the '- [x] **3. CF-S101-HK-1 ordering-caveat disposition**' bullet,
    whose 'Binding content = B6(iii) verbatim:' clause carries the caveat text
    through 'caveat dischargeable once S101 lands under the pinned convention.'
    Returns the full bullet line (the binding-content span), byte-verbatim.
    """
    text = W2_WORKSHOP.read_text(encoding="utf-8")
    lines = text.split("\n")
    for ln in lines:
        if "CF-S101-HK-1 ordering-caveat disposition" in ln and "Binding content = B6(iii) verbatim:" in ln:
            if "caveat dischargeable once S101 lands under the pinned convention." not in ln:
                raise RuntimeError("W-2 B6(iii) terminal anchor not found in span — extraction FAIL")
            return ln
    raise RuntimeError("W-2 B6(iii) anchor not found — extraction FAIL")


# ---------------------------------------------------------------------------
# Section 2 — build_promotion_text (PURE; no I/O after extraction reads)
# ---------------------------------------------------------------------------
def build_promotion_text(slot: str, w3_scope: str, w2_b6iii: str) -> str:
    """Assemble the EXACT §VII.BM entry text. Pure function (string only).

    Content order per plan §W6-1 method.description (a)..(f).
    """
    parts: list[str] = []
    a = "\n"  # leading blank separator before the new section
    parts.append(a)
    # (a) HEADER
    parts.append(
        f"### {slot} — ε_LX Foam-Protection Exact Operator Identity: "
        "[H_foam(N), ε_LX] = 0 for all N in the Wheeler-√N class "
        "(S100a W4-14; STRUCTURAL-THEOREM entry; S101 W6-1 landing — gen-physicist)\n"
    )
    parts.append("\n")
    # (b) THEOREM STATEMENT
    parts.append(
        "**Theorem (foam-protection of the generation index).** The inter-sector mixing "
        "operator `ε_LX` on the D_K multiplicity bundle commutes EXACTLY with the entire "
        "Wheeler-√N quantum-foam Hamiltonian class: `[H_foam(N), ε_LX] = 0` at all 4 probed "
        "roughness scales N (`max_C = 0.0e+00` EXACT). The foam class is the Wheeler-√N family "
        "with S43/S53 anchors. The vanishing rests on two legs: **leg L1** = left-invariance / "
        "multiplicity-scalar (`H_foam` is built from `A_K`-left-invariant data, acting scalar on "
        "each `ℂ^{m(p,q)}`); **leg L2** = fiber-diagonal (`ε_LX` is block-diagonal across the "
        "Peter-Weyl sectors it mixes within). Consequently the generation index is a TOPOLOGICAL "
        "index of the D_K multiplicity structure (QF-71 class; `α_phys = ∞`) — quantum-geometry "
        "roughness cannot decohere it at any N. Recorded CF-discriminator diagnostics: "
        "`cf1_α = 0.501`, `cf2_α = 0.501`, `z3_pinch_survival = 0.6667`. `ε_LX` source form = "
        "ITEM6-W2FORM.\n"
    )
    parts.append("\n")
    # (c) W-3-FINALIZED LANDING SENTENCE — VERBATIM (the five-element protected-FORM class
    #     + the Q5 WITH-clause three-axis robustness ending).
    parts.append(
        "**W-3 ε_LX SCOPE (FINAL) — protected operator-FORM class (verbatim, S100a W-3 "
        "envelope-carrier workshop, Effected item 3; SHA-pinned span "
        f"`{PINNED['w3_workshop'][:16]}…`):** {w3_scope}\n"
    )
    parts.append("\n")
    parts.append(
        "The FIVE protected-FORM elements are: (1) the `[[d, w], [w*, d]]` inter-sector block "
        "structure on the multiplicity bundle; (2) the multiplicity-index topology; (3) the "
        "identically-vanishing commutator `max_C = 0.0e+00` EXACT (QF-71; W4-14 PASS audit "
        "`c46b1f6c…`; CC-7); (4) the **§VII.BL structural home** in the `A_K`-bimodule complement "
        "(STAGE-3-PERMANENT; the W2-4 first-order residual `2.0450` REPORTED-not-asserted-zero is "
        "its live witness, audit `5e24db72…`); (5) the **BDI reality constraint** "
        "`[J, D_K + ε_LX] = 0` block-by-block with `J² = +1`.\n"
    )
    parts.append("\n")
    # (d) W-2 B6(iii) ORDERING CAVEAT — binding content (verbatim span) + W2-2 d-entry source.
    parts.append(
        "**W-2 B6(iii) ordering caveat (binding; verbatim, S100a W-2 mass-functional-counting "
        f"workshop, Effected item 3; SHA-pinned span `{PINNED['w2_workshop'][:16]}…`):** "
        f"{w2_b6iii}\n"
    )
    parts.append("\n")
    parts.append(
        "Caveat anatomy: `ε_LX` OFF-diagonal payloads (`|w| = 1/√6`, `arg w ∈ {π, ±2π/3}`) are "
        "counting-INDEPENDENT; the DIAGONAL d-entries are tagged `RATIO-BLOCKSUM` (as-computed P1 "
        "class) with μ/τ orientation re-pinned to `τ = (1,0)`, `μ = (1,1)` under the now-pinned "
        "`RATIO-NORMALIZED-TRACE-MEAN` convention; the `max_C = 0.0` EXACT topological claim is "
        "orientation-ROBUST (a heavy-pair relabeling permutes basis indices and cannot un-vanish "
        "an identically-vanishing commutator). The caveat is CONDITIONAL-TAGGED — *dischargeable "
        "once `S101-W2-BLOCKTRACE-WIDENING` lands under the pinned convention* (a citation-level "
        "tag, NOT a dispatch dependency). The caveat cites the **W2-2 construction** as the "
        "d-entry source.\n"
    )
    parts.append("\n")
    # (e) ANCHORS
    parts.append(
        "**Anchors.** PRIMARY = `S100a-EPSLX-FOAM-SURVIVAL` PASS (full audit_sha256 "
        f"`{FOAM_SURVIVAL_AUDIT}`; npz `computations/session-100a/s100a_epslx_foam_survival.npz`, "
        f"SHA `{PINNED['foam_npz'][:16]}…`). STRUCTURAL COMPANION (NOT co-primary — cross-corner "
        "co-primary FORBIDDEN per `cross-pillar-bridge-anatomy.md`): **§VII.BL** (the `ε_LX` "
        "bimodule-complement home). Stage-0 scope text = the S100a W-3 workshop Effected item 3.\n"
    )
    parts.append("\n")
    # (f) REGISTRY-ANATOMY COMPLIANCE BLOCK
    parts.append(
        "**Registry-anatomy compliance.** (i) Entry class = **intra-pillar structural theorem** on "
        "the spectral-triple axis (NOT a cross-pillar bridge): the 5-anatomy IS-not-IN elements + "
        "the 3-level ladder are declared **N/A-with-reason** — there is no laboratory-IN observable "
        "and no HKR / K-theory / Connes-Karoubi bridge map is claimed; the statement is an exact "
        "operator-commutator identity intrinsic to `(A_K, H_K, D_K)`. (ii) Projection-side "
        "declaration = **SINGLE-READING, operator-side**: an exact operator-commutator identity "
        "admits no state-pair functional reading, so the bare slot identifier `§VII.BM` is "
        "admissible under `registry-landing.md` Reading-A naming hygiene PRECISELY because this "
        "explicit single-reading sentence is carried (no `.OP-PROJ`/`.STATE-PROJ` suffix is "
        "required when only one reading exists). (iii) Corner-cell note: the identity is an "
        "operator-algebra exact statement, declared at the **algebra-INVARIANT operator layer** "
        "consistent with the §VII.BL lineage. (iv) No state-history labels appear "
        "(`registry-landing.md` Class-(h) parse-tree expansion N/A). (v) Substrate-IS level tag = "
        "**Level 1** (single-τ-slice; `τ_fold = 0.190` anchors the entries, the IDENTITY holds for "
        "all N by structure) per `phononic-framing.md` §\"Single-τ-slice vs moduli-deformation\".\n"
    )
    parts.append("\n")
    # Substrate framing
    parts.append(
        "**Substrate framing** (`phononic-framing.md` §\"IS Space, Not IN Space\"): the fabric's "
        "inter-sector mixing operator `ε_LX` lives on the D_K multiplicity bundle in the complement "
        "of every `A_K`-bimodule. The Wheeler-√N foam Hamiltonian class probes whether "
        "quantum-geometry roughness can decohere the generation index. The exact identity "
        "`[H_foam(N), ε_LX] = 0` says the generation label is a TOPOLOGICAL index of the D_K "
        "multiplicity structure — foam cannot touch it (QF-71 class). **Direction**: D_K Peter-Weyl "
        "multiplicity structure → `ε_LX` block form → commutator zero by left-invariance (L1) and "
        "fiber-diagonality (L2) → generation index protected against foam at every roughness scale "
        "N. The landing freezes the FORM-class scope (five elements, three robustness axes: "
        "counting-INDEPENDENT, orientation-ROBUST, carrier-reading-ROBUST) so later ENTRY-provenance "
        "re-tags (the W-3 carrier adjudication's subject) can never orphan the theorem.\n"
    )
    parts.append("\n")
    # Provenance / closure pin
    parts.append(
        "**Provenance.** S100a W4-14 quantum-foam-protection theorem (`S100a-EPSLX-FOAM-SURVIVAL` "
        f"PASS, audit `{FOAM_SURVIVAL_AUDIT}`); the W-3 SCOPE (FINAL) five-element protected-FORM "
        "class (s100a-w3-envelope-carrier-workshop.md, Effected item 3, Q5 WITH-clause ruling) + "
        "the W-2 B6(iii) ordering caveat (s100a-w2-mass-functional-counting-workshop.md, Effected "
        "item 3) — both transcribed VERBATIM from the SHA-pinned workshop spans (binding-text rule; "
        "no re-derivation). Landed S101 W6-1 (gen-physicist), single-shot AFTER pattern per "
        "`registry-landing.md` §\"Bridge-Landing Script Architecture\"; slot `§VII.BM` reserved "
        "`RESERVED-FOR-S101-W6-1-FOAM-PROTECTION` in "
        "`sessions/framework/s101-slot-pre-allocation-lockfile.md`, runtime-verified next-free at "
        "all header levels (highest prior §VII.BL). This is a §VII NCG/geometric structural-theorem "
        "landing, NOT a §7 falsifier-surface row — mack-cosmic-bridge sole-writer does NOT apply.\n"
    )
    return "".join(parts)


# ---------------------------------------------------------------------------
# Section 3 — runtime slot scan (PD-2) + write_atomic_with_fsync + verify
# ---------------------------------------------------------------------------
SLOT_HEADER_RE = re.compile(r"^#{2,4}\s*§VII\.([A-Z]+)\b")


def scan_occupied_slots(registry_text: str) -> set[str]:
    """All §VII letter-slots occupied at ANY header level (##/###/####)."""
    occ: set[str] = set()
    for ln in registry_text.split("\n"):
        m = SLOT_HEADER_RE.match(ln)
        if m:
            occ.add(m.group(1))
    return occ


def next_free_letter(occupied: set[str], start: str) -> str:
    """Next free two-letter §VII slot at or after `start` (B?-block)."""
    # start is like 'BM'; iterate BM, BN, ... BZ within the B-block.
    assert len(start) == 2 and start[0] == "B"
    for c in range(ord(start[1]), ord("Z") + 1):
        cand = "B" + chr(c)
        if cand not in occupied:
            return cand
    raise RuntimeError("no free §VII B-block letter at/after " + start)


def write_atomic_with_fsync(section_text: str) -> None:
    """APPEND the section to the registry; flush + fsync (atomic via OS)."""
    with open(REGISTRY, "a", encoding="utf-8") as fh:
        fh.write(section_text)
        fh.flush()
        os.fsync(fh.fileno())


def re_read_appended_section(expected_len: int) -> str:
    """Re-read the tail of the registry equal in length to the appended text."""
    full = REGISTRY.read_text(encoding="utf-8")
    return full[-expected_len:]


def verify_section_matches(actual: str, expected: str) -> bool:
    """Strict byte/string equality."""
    return actual == expected


# ---------------------------------------------------------------------------
# Section 4 — dual-SHA (audit over ordered input-pin map; content over section)
# ---------------------------------------------------------------------------
def compute_audit_sha(pin_map: dict[str, str]) -> str:
    """sha256( bytes(script) || canonical JSON of the ordered input-pin map )."""
    h = hashlib.sha256()
    h.update(SCRIPT.read_bytes())
    h.update(
        json.dumps(dict(sorted(pin_map.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")
    )
    return h.hexdigest()


def main() -> None:
    # --- runtime input-SHA verification (binding-text integrity) ---
    live = {
        "w3_workshop": sha256_file(W3_WORKSHOP),
        "w2_workshop": sha256_file(W2_WORKSHOP),
        "foam_npz": sha256_file(FOAM_NPZ),
        "bridge_template": sha256_file(BRIDGE_TEMPLATE),
    }
    print("=== input SHA verification (plan-pinned vs runtime) ===")
    for k in PINNED:
        ok = live[k] == PINNED[k]
        print(f"  {k}: {'OK' if ok else 'MISMATCH'}  {live[k]}")
        if not ok:
            print(f"FATAL: {k} SHA drift from plan pin — binding-text integrity broken")
            sys.exit(2)
    canonical_sha = sha256_file(CANONICAL)
    lockfile_sha = sha256_file(LOCKFILE)
    print(f"  canonical_constants.py: {canonical_sha}")
    print(f"  s101 slot lockfile: {lockfile_sha}")

    # --- PD-2 runtime occupancy scan (registry-state-at-runtime) ---
    registry_text = REGISTRY.read_text(encoding="utf-8")
    registry_state_sha = hashlib.sha256(registry_text.encode("utf-8")).hexdigest()
    occupied = scan_occupied_slots(registry_text)
    reserved_letter = RESERVED_SLOT.replace("§VII.", "")  # 'BM'
    print(f"\n=== PD-2 all-header-level §VII slot scan ===")
    print(f"  occupied §VII letters (count={len(occupied)}); BM occupied? {'BM' in occupied}")
    # confirm lockfile reserves §VII.BM to this gate
    lock_text = LOCKFILE.read_text(encoding="utf-8")
    lock_reserves_bm = (LOCKFILE_RESERVED_FOR in lock_text) and ("§VII.BM" in lock_text)
    print(f"  lockfile {LOCKFILE_RESERVED_FOR} reserves §VII.BM? {lock_reserves_bm}")

    # --- PD-3 reroute on runtime occupancy ---
    rerouted = False
    slot_letter = reserved_letter
    if reserved_letter in occupied:
        rerouted = True
        slot_letter = next_free_letter(occupied, reserved_letter)
        print(f"  PD-3: §VII.{reserved_letter} OCCUPIED at runtime → reroute to §VII.{slot_letter} (FAIL-with-remediation)")
    slot = f"§VII.{slot_letter}"

    # --- verbatim extraction (byte-equality of anchored spans) ---
    w3_scope = extract_w3_scope_final()
    w2_b6iii = extract_w2_b6iii()
    print(f"\n=== verbatim extraction ===")
    print(f"  W-3 SCOPE (FINAL) span: {len(w3_scope)} chars; ends '...{w3_scope[-30:]}'")
    print(f"  W-2 B6(iii) span: {len(w2_b6iii)} chars; ends '...{w2_b6iii[-40:]}'")

    # --- (1) build_promotion_text (PURE) ---
    promotion_text = build_promotion_text(slot, w3_scope, w2_b6iii)

    # --- (2) write_atomic_with_fsync (APPEND) ---
    write_atomic_with_fsync(promotion_text)

    # --- (3) re_read + verify_section_matches (single boolean) ---
    actual = re_read_appended_section(len(promotion_text))
    section_match = verify_section_matches(actual, promotion_text)
    print(f"\n=== AFTER-pattern verify ===")
    print(f"  appended {len(promotion_text)} chars; post-fsync re-read byte-match: {section_match}")

    # --- (4) determine verdict (the boolean IS the verdict; reroute forces FAIL) ---
    if rerouted:
        verdict = "FAIL"
        value = f"reroute_fired_slot_drift_reserved_VII.{reserved_letter}_occupied_landed_at_{slot}_section_match_{section_match}"
    elif section_match:
        verdict = "PASS"
        value = f"landed_{slot}_section_byte_match_True_5anatomy_NA_with_reason_level1_single_reading_operator_side"
    else:
        verdict = "FAIL"
        value = f"post_fsync_re_read_MISMATCH_at_{slot}_section_defect_remediation_to_S102"

    # --- dual-SHA: audit over ordered input-pin map; content over re-read section ---
    pin_map = {
        "gate_id": GATE_ID,
        "slot": slot,
        "reserved_slot": RESERVED_SLOT,
        "lockfile_reserved_for": LOCKFILE_RESERVED_FOR,
        "w3_workshop_sha": live["w3_workshop"],
        "w2_workshop_sha": live["w2_workshop"],
        "foam_npz_sha": live["foam_npz"],
        "bridge_template_sha": live["bridge_template"],
        "canonical_constants_sha": canonical_sha,
        "slot_lockfile_sha": lockfile_sha,
        "registry_state_at_runtime_sha": registry_state_sha,
        "foam_survival_anchor_audit": FOAM_SURVIVAL_AUDIT,
        "rerouted": str(rerouted),
        "section_match": str(section_match),
    }
    audit_sha = compute_audit_sha(pin_map)
    content_sha = hashlib.sha256(actual.encode("utf-8")).hexdigest()

    # --- landing-record npz ---
    try:
        import numpy as np
        np.savez(
            OUT_NPZ,
            gate_id=GATE_ID,
            slot=slot,
            reserved_slot=RESERVED_SLOT,
            rerouted=rerouted,
            section_match=section_match,
            verdict=verdict,
            audit_sha256=audit_sha,
            content_sha256=content_sha,
            registry_state_at_runtime_sha=registry_state_sha,
            w3_workshop_sha=live["w3_workshop"],
            w2_workshop_sha=live["w2_workshop"],
            foam_npz_sha=live["foam_npz"],
            slot_lockfile_sha=lockfile_sha,
            foam_survival_anchor_audit=FOAM_SURVIVAL_AUDIT,
            promotion_text_len=len(promotion_text),
        )
        print(f"\nlanding-record npz → {OUT_NPZ}")
    except Exception as e:  # noqa: BLE001
        print(f"WARN: npz write failed: {e}")

    # --- (5) print verdict payload ONCE (agent calls emit_verdict) ---
    payload = {
        "session": "101",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "companion_note": (
            f"slot={slot}; reserved={RESERVED_SLOT} ({LOCKFILE_RESERVED_FOR}); "
            f"rerouted={rerouted}; AFTER-pattern single-shot; verbatim W-3 SCOPE(FINAL)+W-2 B6(iii); "
            f"primary anchor S100a-EPSLX-FOAM-SURVIVAL {FOAM_SURVIVAL_AUDIT[:16]}…; "
            f"structural companion §VII.BL (NOT co-primary)"
        ),
    }
    print("\n=== VERDICT_PAYLOAD_BEGIN ===")
    print(json.dumps(payload, indent=2))
    print("=== VERDICT_PAYLOAD_END ===")
    print(f"\naudit_sha256={audit_sha}")
    print(f"content_sha256={content_sha}")
    sys.exit(0)  # script health: ran successfully regardless of PASS/FAIL verdict


if __name__ == "__main__":
    main()
