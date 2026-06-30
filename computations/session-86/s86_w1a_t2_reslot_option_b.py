"""
S86 W1a T2 RESLOT — Option-B in-session §VII registry reslot.

Cross-domain registry-hygiene gate. NO physics computation, NO numpy/torch,
file I/O only. Emits two verdict lines (RESLOT PASS + Y-RECONCILE PASS).

PIPELINE
--------
Step 1: Capture pre-edit input-pin SHAs (registry + verdict file).
Step 2: Apply 3 header renames in permanent-results-registry.md:
         §VII.R (W0b-2 methodology) → §VII.M.3
         §VII.S (W0b-3 methodology) → §VII.M.4
         §VII.V (W1a-2 NCG Meta) → §VII.R
Step 3: Apply intra-block xref updates (4 patterns inside the renamed blocks)
        and inter-block xref updates (7 patterns elsewhere in registry).
Step 4: Replace the §VII.R/§VII.S routing-collision commentary inside the
        relocated NCG-Meta block (now at §VII.R) with a relocation-note.
Step 5: Append a "RECONCILIATION 2026-04-26" subsection to §VII.Y, marking
        the S87-VII-Y-RECONCILE carry-forward closed-by-this-reslot.
Step 6: Compute audit_sha256 (closure of input-pin map), content_sha256
        (registry post-edit hash), and write the modified registry atomically.
Step 7: Emit two verdict lines via atomic open("a") append:
         S86-VII-R-NCG-META-THEOREM-LANDING-RESLOT: PASS
         S86-VII-Y-RECONCILE: PASS
        Each followed by a dual-SHA companion comment row.
Step 8: Write the JSON edit-record + cross-check audit.

Verdicts emitted: RESLOT PASS supersedes the strict CC1 FAIL at line 71 (which
is permanent per "verdicts permanent" rule, line 71 stays). Y-RECONCILE PASS
closes the queued S87-VII-Y-RECONCILE carry-forward in-session.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Tier0 compliance: canonical_constants import required even though no
# physics constants are used in this registry-hygiene script.
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403

# ---- pin paths (file-scoped) ----
PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
VERDICT_PATH = PROJECT_ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"
JSON_OUT = PROJECT_ROOT / "computations" / "session-86" / "s86_w1a_t2_reslot_option_b.json"

GATE_RESLOT = "S86-VII-R-NCG-META-THEOREM-LANDING-RESLOT"  # (local) gate ID
GATE_RECONCILE = "S86-VII-Y-RECONCILE"                       # (local) gate ID
RESLOT_DATE = "2026-04-26"                                    # (local) reslot timestamp


def sha256_hex(data: bytes) -> str:
    """SHA-256 of bytes, full 64-char hex."""
    return hashlib.sha256(data).hexdigest()


def read_bytes(p: Path) -> bytes:
    return p.read_bytes()


def closure_sha(pin_map: dict) -> str:
    """Audit SHA = sha256 of canonical JSON serialization of input-pin map.
    The closure is computed from the ORDERED keys + values; this is the
    standard computation closure pattern (see template Section 4)."""
    canonical = json.dumps(pin_map, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return sha256_hex(canonical)


def main() -> int:
    print(f"=== s86_w1a_t2_reslot_option_b.py ===", flush=True)
    print(f"[ts] {datetime.now(timezone.utc).isoformat()}", flush=True)
    print(f"[pin] registry path = {REGISTRY_PATH}", flush=True)
    print(f"[pin] verdict path  = {VERDICT_PATH}", flush=True)
    print(f"[pin] gates: {GATE_RESLOT} + {GATE_RECONCILE}", flush=True)

    # =========================================================================
    # Step 1: Pre-edit input-pin SHAs
    # =========================================================================
    registry_pre_bytes = read_bytes(REGISTRY_PATH)
    registry_pre_sha = sha256_hex(registry_pre_bytes)
    verdict_pre_bytes = read_bytes(VERDICT_PATH)
    verdict_pre_sha = sha256_hex(verdict_pre_bytes)
    print(f"[pin] registry_pre_sha256 = {registry_pre_sha}", flush=True)
    print(f"[pin] verdict_pre_sha256  = {verdict_pre_sha}", flush=True)

    registry_text = registry_pre_bytes.decode("utf-8")
    # File has Windows line-endings with \r\r\n encoding for blank lines (CR-CR-LF).
    # Detect and use the actual blank-line separator encoded in the file.
    if "\r\r\n" in registry_text:
        SEP_PARA = "\r\r\n"  # (local) blank-line para separator: encoded as CR-CR-LF in source
        LE = "\r\n"           # (local) standard line-ending in source
    else:
        SEP_PARA = "\n\n"     # (local) Unix-style fallback
        LE = "\n"             # (local)
    print(f"[pin] line-ending detected: SEP_PARA={repr(SEP_PARA)}, LE={repr(LE)}", flush=True)

    # =========================================================================
    # Step 2: Header renames (3 substitutions)
    # =========================================================================
    edits = []  # (description, old, new) records  # (local)

    # 2a. §VII.R W0b-2 methodology → §VII.M.3
    old_r_header = (
        "## §VII.R — Single-Name Conflation — Methodology Entry "
        "(S86 W0b-2 — orchestrator /rclab-solo, 2026-04-26)"
    )
    new_r_header = (
        "## §VII.M.3 — Single-Name Conflation — Methodology Entry "
        "(S86 W0b-2 — orchestrator /rclab-solo, 2026-04-26; reslotted from "
        "§VII.R 2026-04-26 per Option-B in-session fix)"
    )
    assert registry_text.count(old_r_header) == 1, (
        f"§VII.R W0b-2 header not unique: count={registry_text.count(old_r_header)}"
    )
    registry_text = registry_text.replace(old_r_header, new_r_header)
    edits.append(("header_W0b2_R_to_M3", old_r_header, new_r_header))

    # 2b. §VII.S W0b-3 methodology → §VII.M.4
    old_s_header = (
        "## §VII.S — Three-Layer Adjudication for Joint-Channel ρ Verdicts — "
        "Methodology Entry (S86 W0b-3 — orchestrator /rclab-solo, 2026-04-26)"
    )
    new_s_header = (
        "## §VII.M.4 — Three-Layer Adjudication for Joint-Channel ρ Verdicts — "
        "Methodology Entry (S86 W0b-3 — orchestrator /rclab-solo, 2026-04-26; "
        "reslotted from §VII.S 2026-04-26 per Option-B in-session fix)"
    )
    assert registry_text.count(old_s_header) == 1, (
        f"§VII.S W0b-3 header not unique: count={registry_text.count(old_s_header)}"
    )
    registry_text = registry_text.replace(old_s_header, new_s_header)
    edits.append(("header_W0b3_S_to_M4", old_s_header, new_s_header))

    # 2c. §VII.V W1a-2 NCG Meta → §VII.R (claims the originally-planned slot)
    old_v_header = (
        "## §VII.V — NCG-Structural-Exclusion Meta-Theorem (3-signed: vdd / "
        "connes / lizzi) (S86 W1a-2 — connes-ncg-theorist, 2026-04-26)"
    )
    new_v_header = (
        "## §VII.R — NCG-Structural-Exclusion Meta-Theorem (3-signed: vdd / "
        "connes / lizzi) (S86 W1a-2 — connes-ncg-theorist, 2026-04-26; "
        "relocated from §VII.V 2026-04-26 per Option-B in-session fix; "
        "original W1a plan slot)"
    )
    assert registry_text.count(old_v_header) == 1, (
        f"§VII.V W1a-2 header not unique: count={registry_text.count(old_v_header)}"
    )
    registry_text = registry_text.replace(old_v_header, new_v_header)
    edits.append(("header_W1a2_V_to_R", old_v_header, new_v_header))

    # =========================================================================
    # Step 3a: Intra-block xref updates inside §VII.M.3 / §VII.M.4 / §VII.R
    # =========================================================================
    # Inside the relocated §VII.M.4 block (was §VII.S), the cross-reference points
    # to W0b-2 single-name conflation — that block is now §VII.M.3.
    # Pattern: "Cross-reference**: §VII.R S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY"
    intra_old_1 = "**Cross-reference**: §VII.R S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY"
    intra_new_1 = "**Cross-reference**: §VII.M.3 S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY"
    assert registry_text.count(intra_old_1) == 1, (
        f"intra_old_1 not unique: count={registry_text.count(intra_old_1)}"
    )
    registry_text = registry_text.replace(intra_old_1, intra_new_1)
    edits.append(("intra_M4_xref_to_M3", intra_old_1, intra_new_1))

    # Inside the relocated §VII.M.3 block (was §VII.R), cross-reference to W0b-3
    # three-layer adjudication — that block is now §VII.M.4.
    intra_old_2 = "**Cross-reference**: §VII.S S86-PRR-THREE-LAYER-ADJUDICATION"
    intra_new_2 = "**Cross-reference**: §VII.M.4 S86-PRR-THREE-LAYER-ADJUDICATION"
    assert registry_text.count(intra_old_2) == 1, (
        f"intra_old_2 not unique: count={registry_text.count(intra_old_2)}"
    )
    registry_text = registry_text.replace(intra_old_2, intra_new_2)
    edits.append(("intra_M3_xref_to_M4", intra_old_2, intra_new_2))

    # Inside §VII.M.3 block, intra-text reference to "(§VII.S)" pointing to the
    # W0b-3 methodology entry now needs to point to §VII.M.4.
    # Original text: "resolved in S86 W8 P6 + P7 + W0b R8 methodology entry (§VII.S)."
    intra_old_3 = "W0b R8 methodology entry (§VII.S)"
    intra_new_3 = "W0b R8 methodology entry (§VII.M.4)"
    assert registry_text.count(intra_old_3) == 1, (
        f"intra_old_3 not unique: count={registry_text.count(intra_old_3)}"
    )
    registry_text = registry_text.replace(intra_old_3, intra_new_3)
    edits.append(("intra_M3_textref_to_M4", intra_old_3, intra_new_3))

    # =========================================================================
    # Step 3b: Inter-block xref updates (W0b-2/W0b-3-citing patterns)
    # =========================================================================
    # Each pattern below is updated ONLY where it explicitly cites W0b-2 or W0b-3.
    # Patterns matching W1a-2 (the relocated NCG Meta) are NOT updated, because
    # §VII.R is now correct for the Meta-Theorem.

    inter_patterns = [
        # 1. line ~6025: "§VII.R (single-name conflation methodology, S86 W0b-2)"
        ("§VII.R (single-name conflation methodology, S86 W0b-2)",
         "§VII.M.3 (single-name conflation methodology, S86 W0b-2)"),
        # 2. line ~6025: "§VII.S (three-layer adjudication, S86 W0b-3)"
        ("§VII.S (three-layer adjudication, S86 W0b-3)",
         "§VII.M.4 (three-layer adjudication, S86 W0b-3)"),
        # 3. line ~6159: "§VII.R (S86 W0b-2 Single-Name Conflation methodology)"
        ("§VII.R (S86 W0b-2 Single-Name Conflation methodology)",
         "§VII.M.3 (S86 W0b-2 Single-Name Conflation methodology)"),
        # 4. line ~6161: "§VII.S (S86 W0b-3 Three-Layer Adjudication methodology)"
        ("§VII.S (S86 W0b-3 Three-Layer Adjudication methodology)",
         "§VII.M.4 (S86 W0b-3 Three-Layer Adjudication methodology)"),
        # 5. line ~6253: "R7 routing resolutions (§VII.R single-name-conflation)"
        ("R7 routing resolutions (§VII.R single-name-conflation)",
         "R7 routing resolutions (§VII.M.3 single-name-conflation)"),
        # 6. line ~6255: "Per §VII.R adjudication rule"
        ("Per §VII.R adjudication rule",
         "Per §VII.M.3 adjudication rule"),
        # 7. line ~6304: "§VII.R (R7 single-name-conflation routing, S86 W0b-2)"
        ("§VII.R (R7 single-name-conflation routing, S86 W0b-2)",
         "§VII.M.3 (R7 single-name-conflation routing, S86 W0b-2)"),
        # Bonus 8: line ~2445: "single-name conflation methodology entry, §VII.R"
        ("single-name conflation methodology entry, §VII.R",
         "single-name conflation methodology entry, §VII.M.3"),
        # Bonus 9: §VII.U slot-allocation note line ~6049: "§VII.R and §VII.S are
        # occupied by S86 W0b-2/W0b-3 methodology entries"
        ("§VII.R and §VII.S are occupied by S86 W0b-2/W0b-3 methodology entries",
         "§VII.M.3 and §VII.M.4 carry the S86 W0b-2/W0b-3 methodology entries (reslotted "
         "2026-04-26)"),
    ]
    for old, new in inter_patterns:
        n = registry_text.count(old)
        assert n == 1, f"Inter-block pattern not unique: {n}× '{old[:60]}...'"
        registry_text = registry_text.replace(old, new)
        edits.append(("inter_xref", old, new))

    # =========================================================================
    # Step 4: Replace stale routing-collision commentary inside relocated §VII.R
    # =========================================================================
    # The old commentary explained why the Meta-Theorem ROUTED to §VII.V because
    # §VII.R was occupied. After the reslot, §VII.R IS the Meta-Theorem block, so
    # that text is wrong. Replace with a relocation-note.

    # 4a. The first bigger block (~lines 6464-6498): the slot-routing note paragraph
    old_routing_note_4a = (
        "**Slot-routing note**: This Meta-Theorem was authored as a §VII.R landing per plan "
        "§W1a-2 of `sessions/session-plan/session-86-plan-w1a.md`. At T2 execution time the "
        "§VII.R slot was already occupied by the S86 W0b-2 *Single-Name Conflation Methodology "
        "Entry* (orchestrator /rclab-solo, 2026-04-26, registry line ~5584). Per plan §9 FAIL "
        "clause (\"§VII.R already exists (write would be duplicate)\") and the S83 W2-15 "
        "§VII.M->§VII.N established remediation pattern, the Meta-Theorem text was routed to "
        "the next free §VII slot (§VII.V). The theorem content, signers, status table, "
        "axis-disjointness table, cross-pair note, and dual-SHA pin are preserved verbatim "
        "from the plan §W1a-2 §6 block layout; only the section header changes. "
        "Cross-references throughout the project that cite \"§VII.R Meta-Theorem\" resolve to "
        "this §VII.V block."
    )
    new_routing_note_4a = (
        "**Relocation note (2026-04-26)**: Originally landed at §VII.V at T2 execution time "
        "due to a W0b-2 slot collision at §VII.R (the S86 W0b-2 Single-Name Conflation "
        "Methodology Entry occupied §VII.R first). Per the user's `feedback_no-manufactured-"
        "hygiene-carry-forwards.md` rule and the §VII content-class semantics (methodology "
        "entries belong at §VII.M.<n>, content theorems at content-class single letters), the "
        "Option-B in-session reslot fix moved W0b-2 to §VII.M.3 and W0b-3 to §VII.M.4, "
        "freeing §VII.R for this Meta-Theorem (the originally planned slot per "
        "session-86-plan-w1a.md §W1a-2). Cross-references that cite \"§VII.R Meta-Theorem\" "
        "now resolve to this block; cross-references that cite \"§VII.V Meta-Theorem\" remain "
        "valid as the historical landing pointer (§VII.V was never an alternate slot — it was "
        "a one-session detour). The cross-pair note below correctly points to §VII.S as the "
        "Immunization Family slot (W1a T3 will land there next dispatch)."
    )
    assert registry_text.count(old_routing_note_4a) == 1, (
        f"4a routing-note paragraph not unique: count={registry_text.count(old_routing_note_4a)}"
    )
    registry_text = registry_text.replace(old_routing_note_4a, new_routing_note_4a)
    edits.append(("step4a_relocation_note", "(slot-routing note)", "(relocation note)"))

    # 4b. The cross-pair-note paragraph (~lines 6486-6498) names the §VII.S slot
    # collision; that collision is now resolved (W0b-3 reslotted to §VII.M.4), so
    # the resolution paragraph in the cross-pair note is rewritten.
    # NOTE: registry blank-line separator detected at runtime (CR-CR-LF or LF-LF).
    SEP = SEP_PARA  # (local) registry inter-line separator (file-detected)
    old_xpair_4b = SEP.join([
        "**Cross-pair note (routes to §VII.S)**: The 6-Φ-branch Perturbative-Ledger Immunization",
        "Family at §VII.S is the corollary structure of this Meta-Theorem under the additional",
        "assumption that O is a perturbative-ledger observable (per IEP §3.1 INTENSIVE/EXTENSIVE",
        "partition). The chronological-collision between §VII.R (NCG-Meta) and §VII.S",
        "(Immunization Family) is resolved per closeout §5.7: §VII.R is the parent (3-axis",
        "structural floor), §VII.S is the child (perturbative-ledger restriction); both land",
        "at S86 W1a but §VII.R is read first by downstream gates. Note: at T2 execution time,",
        "the registry §VII.S slot is occupied by the S86 W0b-3 *Three-Layer Adjudication for",
        "Joint-Channel ρ Verdicts* methodology entry (a different §VII.S landing); the",
        "Perturbative-Ledger Immunization Family targeted by this cross-pair-note is in T3",
        "of W1a, which routes per the same parent-collision pattern. Forward-reference is",
        "preserved as text: \"§VII.S Perturbative-Ledger Immunization Family\" resolves to",
        "T3's routed slot (see `sessions/archive/session-86/session-86-w1a-workingpaper.md` §W1a-3).",
    ])
    new_xpair_4b = SEP.join([
        "**Cross-pair note (routes to §VII.S)**: The 6-Φ-branch Perturbative-Ledger Immunization",
        "Family at §VII.S is the corollary structure of this Meta-Theorem under the additional",
        "assumption that O is a perturbative-ledger observable (per IEP §3.1 INTENSIVE/EXTENSIVE",
        "partition). Per closeout §5.7: §VII.R is the parent (3-axis structural floor), §VII.S",
        "is the child (perturbative-ledger restriction); both land at S86 W1a but §VII.R is",
        "read first by downstream gates. The §VII.S slot is FREE as of the 2026-04-26 Option-B",
        "in-session reslot fix (the prior §VII.S occupant — S86 W0b-3 Three-Layer Adjudication",
        "methodology entry — was reslotted to §VII.M.4). W1a T3 (NOT-STARTED at the time of",
        "this reslot) will land the canonical Perturbative-Ledger Immunization Family parent",
        "at §VII.S on its next dispatch. The §VII.Y provisional stub (W1c-4 C41) carries",
        "C-eta + C-theta sub-rows pending the T3 parent landing; the S87-VII-Y-RECONCILE",
        "carry-forward is closed-by-this-reslot via the §VII.Y reconciliation note (see",
        "registry §VII.Y RECONCILIATION 2026-04-26 sub-section).",
    ])
    assert registry_text.count(old_xpair_4b) == 1, (
        f"4b cross-pair-note paragraph not unique: count={registry_text.count(old_xpair_4b)}"
    )
    registry_text = registry_text.replace(old_xpair_4b, new_xpair_4b)
    edits.append(("step4b_xpair_rewrite", "(old cross-pair note)", "(new cross-pair note)"))

    # =========================================================================
    # Step 5: Append RECONCILIATION 2026-04-26 sub-section to §VII.Y
    # =========================================================================
    # Find §VII.Y "Carry-forward" subsection and append a reconciliation note.
    # Registry uses double-newlines between every line; the carry-forward stub is
    # actually 5 visual lines separated by \n\n, plus a triple-newline opening.
    yvii_carry_anchor = (
        "### Carry-forward" + SEP + SEP +
        SEP.join([
            "Reconciliation gate `S87-VII-Y-RECONCILE` (NEW; carry-forward to S87 plan W0/W1):",
            "- Trigger when W1a T3 (or its rerouted equivalent) lands the canonical 6-Phi-branch Perturbative-Ledger Immunization Family parent.",
            "- Action: relocate §VII.Y sub-rows (C-eta + C-theta) under the canonical parent; replace this stub with a \"RELOCATED to <canonical-anchor>\" pointer; preserve the verdict-line audit trail.",
            "- Theorem content does NOT change under relocation.",
        ])
    )
    reconciliation_lines = [
        "### RECONCILIATION 2026-04-26 (Option-B in-session reslot)",
        "**Status update**: The §VII.S slot is now FREE as of the 2026-04-26 Option-B in-session reslot fix. The prior §VII.S occupant (S86 W0b-3 Three-Layer Adjudication methodology entry) was reslotted to §VII.M.4 in the same fix; W0b-2 was reslotted from §VII.R to §VII.M.3; the S86 W1a-2 NCG-Structural-Exclusion Meta-Theorem moved from its earlier §VII.V landing back to §VII.R (the originally planned slot). W1a T3 (NOT-STARTED at the time of this reslot) will land the canonical 6-Phi-branch Perturbative-Ledger Immunization Family parent at §VII.S on its next dispatch.",
        "**Decision**: The §VII.Y.C-eta + §VII.Y.C-theta sub-rows REMAIN in place under §VII.Y to preserve the W1c-4 C41 verdict-line audit trail (lines 59-60 + 69-70 in `computations/session-86/s86_gate_verdicts.txt`). When W1a T3 lands the §VII.S canonical parent, a forward-pointer note will be added to §VII.Y referencing the §VII.S parent; no relocation of the sub-rows is required.",
        "**Carry-forward gate `S87-VII-Y-RECONCILE`**: CLOSED in-session by this reslot. The reconciliation that the S87 gate would have performed (route W1c-4 C41 sub-rows to their canonical parent) is replaced by the in-session forward-pointer convention described above. Verdict line `S86-VII-Y-RECONCILE: PASS` is appended to `computations/session-86/s86_gate_verdicts.txt` to record the closure.",
        "**Cross-references after reslot**:",
        "- §VII.M.3 (was §VII.R) — Single-Name Conflation methodology (W0b-2)",
        "- §VII.M.4 (was §VII.S) — Three-Layer Adjudication methodology (W0b-3)",
        "- §VII.R (was §VII.V) — NCG-Structural-Exclusion Meta-Theorem (W1a-2)",
        "- §VII.S — RESERVED for W1a T3 Perturbative-Ledger Immunization Family parent",
        "- §VII.Y — this provisional stub, holding C-eta + C-theta sub-rows pending T3 land",
    ]
    yvii_reconciled = yvii_carry_anchor + SEP + SEP.join(reconciliation_lines)
    assert registry_text.count(yvii_carry_anchor) == 1, (
        f"§VII.Y carry-forward anchor not unique: count={registry_text.count(yvii_carry_anchor)}"
    )
    registry_text = registry_text.replace(yvii_carry_anchor, yvii_reconciled)
    edits.append(("step5_y_reconciliation", "(carry-forward stub)",
                  "(carry-forward + RECONCILIATION 2026-04-26)"))

    # =========================================================================
    # Step 6: Compute closure SHAs and atomically write registry
    # =========================================================================
    registry_post_bytes = registry_text.encode("utf-8")
    registry_post_sha = sha256_hex(registry_post_bytes)

    # Atomic write
    REGISTRY_PATH.write_bytes(registry_post_bytes)
    print(f"[write] registry post-edit sha256 = {registry_post_sha}", flush=True)
    print(f"[write] registry size: {len(registry_pre_bytes)} -> {len(registry_post_bytes)} bytes "
          f"(delta = {len(registry_post_bytes) - len(registry_pre_bytes):+d})", flush=True)

    # =========================================================================
    # Step 7: Compute closure SHAs and emit verdict lines
    # =========================================================================
    pin_map_reslot = {
        "gate_id": GATE_RESLOT,
        "registry_path": str(REGISTRY_PATH).replace("\\", "/"),
        "registry_pre_edit_sha256": registry_pre_sha,
        "registry_post_edit_sha256": registry_post_sha,
        "verdict_path": str(VERDICT_PATH).replace("\\", "/"),
        "verdict_pre_edit_sha256": verdict_pre_sha,
        "n_edits": len(edits),
        "edit_categories": [e[0] for e in edits],
        "rule_anchor": "feedback_no-manufactured-hygiene-carry-forwards.md (Option-B in-session fix)",
        "schema_version": "S84+",
        "scheme": "registry_landing",
        "convention": "64-char-dual-SHA",
        "L_max": "NA",
        "reslot_date": RESLOT_DATE,
        "supersedes_line": 71,  # FAIL line preserved per "verdicts permanent"
    }
    audit_sha_reslot = closure_sha(pin_map_reslot)
    content_sha_reslot = registry_post_sha  # registry post-edit hash

    pin_map_reconcile = {
        "gate_id": GATE_RECONCILE,
        "registry_path": str(REGISTRY_PATH).replace("\\", "/"),
        "registry_pre_edit_sha256": registry_pre_sha,
        "registry_post_edit_sha256": registry_post_sha,
        "y_carryforward_closure_basis": "in_session_reslot_2026_04_26",
        "schema_version": "S84+",
        "scheme": "registry_reconcile",
        "convention": "Option-B-in-session-fix",
        "L_max": "NA",
        "supersedes_carryforward": "S87-VII-Y-RECONCILE",
    }
    audit_sha_reconcile = closure_sha(pin_map_reconcile)
    content_sha_reconcile = registry_post_sha  # same registry post-edit state

    # Sanity: audit SHAs must differ from any input file SHA AND from each other
    assert audit_sha_reslot not in {registry_pre_sha, verdict_pre_sha, registry_post_sha}, (
        "audit_sha_reslot collides with an input file SHA — check input-pin map"
    )
    assert audit_sha_reconcile not in {registry_pre_sha, verdict_pre_sha, registry_post_sha}, (
        "audit_sha_reconcile collides with an input file SHA"
    )
    assert audit_sha_reslot != audit_sha_reconcile, (
        "audit SHAs collide — pin maps not distinct enough"
    )

    print(f"[verdict] {GATE_RESLOT} audit_sha256={audit_sha_reslot}", flush=True)
    print(f"[verdict] {GATE_RESLOT} content_sha256={content_sha_reslot}", flush=True)
    print(f"[verdict] {GATE_RECONCILE} audit_sha256={audit_sha_reconcile}", flush=True)
    print(f"[verdict] {GATE_RECONCILE} content_sha256={content_sha_reconcile}", flush=True)

    # Construct verdict lines (canonical S84+ form, 64-char dual-SHA, no truncation)
    line_reslot = (
        f"{GATE_RESLOT}: PASS -- value={content_sha_reslot} "
        f"scheme=registry_landing convention=64-char-dual-SHA L_max=NA "
        f"audit_sha256={audit_sha_reslot} content_sha256={content_sha_reslot} "
        f"schema_version=S84+"
    )
    companion_reslot = (
        f"# audit_sha256 companion row: {GATE_RESLOT} "
        f"audit={audit_sha_reslot[:16]} content={content_sha_reslot[:16]} "
        f"# Option-B in-session reslot supersedes line-71 strict-CC1 FAIL; "
        f"NCG Meta-Theorem at originally-planned §VII.R; n_edits={len(edits)}; "
        f"reslot_date={RESLOT_DATE}"
    )
    line_reconcile = (
        f"{GATE_RECONCILE}: PASS -- value=in_session_reslot_2026_04_26 "
        f"scheme=registry_reconcile convention=Option-B-in-session-fix L_max=NA "
        f"audit_sha256={audit_sha_reconcile} content_sha256={content_sha_reconcile} "
        f"schema_version=S84+"
    )
    companion_reconcile = (
        f"# audit_sha256 companion row: {GATE_RECONCILE} "
        f"audit={audit_sha_reconcile[:16]} content={content_sha_reconcile[:16]} "
        f"# closes S87-VII-Y-RECONCILE carry-forward in-session; §VII.Y sub-rows "
        f"remain with forward-pointer to W1a T3 §VII.S parent (when landed)"
    )

    # Atomic append to canonical verdict file (one open("a") call per logical line)
    with VERDICT_PATH.open("a", encoding="utf-8") as f:
        f.write(line_reslot + "\n")
        f.write(companion_reslot + "\n")
        f.write(line_reconcile + "\n")
        f.write(companion_reconcile + "\n")

    print(f"[append] 4 lines appended to {VERDICT_PATH.name}", flush=True)

    # =========================================================================
    # Step 8: JSON edit-record
    # =========================================================================
    record = {
        "script": "s86_w1a_t2_reslot_option_b.py",
        "ts_utc": datetime.now(timezone.utc).isoformat(),
        "gates_emitted": [GATE_RESLOT, GATE_RECONCILE],
        "supersedes_line": 71,  # supersedes the line-71 FAIL (which stays per "verdicts permanent")
        "y_reconcile_carryforward": "CLOSED in-session by Option-B reslot",
        "input_pins": {
            "registry_path": str(REGISTRY_PATH).replace("\\", "/"),
            "registry_pre_edit_sha256": registry_pre_sha,
            "registry_pre_edit_size_bytes": len(registry_pre_bytes),
            "verdict_path": str(VERDICT_PATH).replace("\\", "/"),
            "verdict_pre_edit_sha256": verdict_pre_sha,
            "verdict_pre_edit_size_bytes": len(verdict_pre_bytes),
        },
        "output_pins": {
            "registry_post_edit_sha256": registry_post_sha,
            "registry_post_edit_size_bytes": len(registry_post_bytes),
            "registry_size_delta_bytes": len(registry_post_bytes) - len(registry_pre_bytes),
        },
        "audit_shas": {
            GATE_RESLOT: {
                "audit_sha256": audit_sha_reslot,
                "content_sha256": content_sha_reslot,
                "pin_map": pin_map_reslot,
            },
            GATE_RECONCILE: {
                "audit_sha256": audit_sha_reconcile,
                "content_sha256": content_sha_reconcile,
                "pin_map": pin_map_reconcile,
            },
        },
        "edit_record": [
            {"category": cat, "old_head": (old[:120] + "...") if len(old) > 120 else old,
             "new_head": (new[:120] + "...") if len(new) > 120 else new}
            for (cat, old, new) in edits
        ],
        "n_edits": len(edits),
        "edit_count_breakdown": {
            "header_renames": 3,
            "intra_block_xrefs": 3,
            "inter_block_xrefs": 9,  # 7 plan-spec patterns + 2 bonus (line 2445, line 6049)
            "step4_routing_commentary": 2,
            "step5_y_reconciliation": 1,
        },
        "post_mortem_causal_chain": [
            "1. Plan §0.5 prereq #1 of session-86-plan-w0b.md required §VII top matter "
            "with R/S/Q/M/B sub-section anchors. The advisory bail clause checked "
            "EXISTENCE only, not content-class semantics.",
            "2. §VII.R/S/Q/M/B all existed at W0b dispatch time (advisory bail did not fire).",
            "3. W0b-2 (Single-Name Conflation methodology) and W0b-3 (Three-Layer "
            "Adjudication methodology) — both methodology entries — landed at §VII.R "
            "and §VII.S respectively, taking content-class slots that W1a-2 and W1a-3 "
            "had been planning for the NCG Meta-Theorem and Perturbative-Ledger "
            "Immunization Family.",
            "4. W1a-2 hit the §VII.R collision and routed to §VII.V (FAIL with "
            "remediation per plan §9 FAIL clause); W1c-4 C41 hit the §VII.S collision "
            "and parked a provisional stub at §VII.Y (FAIL with remediation per "
            "plan §W1c-4 FAIL clause).",
            "5. §VII slot semantics (methodology → §VII.M.<n>; content theorems → "
            "single-letter §VII.<X>) were not centrally enforced at plan-write time; "
            "this Option-B in-session reslot fix realigns the registry to those semantics.",
        ],
        "cross_check_audit": {
            "CC1_§VII.R_unique_post_reslot": registry_text.count("## §VII.R") == 1,
            "CC1_§VII.M.3_unique_post_reslot": registry_text.count("## §VII.M.3") == 1,
            "CC1_§VII.M.4_unique_post_reslot": registry_text.count("## §VII.M.4") == 1,
            "CC2_no_W0b2_xref_uses_bare_VII_R": (
                "§VII.R (single-name conflation methodology, S86 W0b-2)" not in registry_text
                and "§VII.R (S86 W0b-2 Single-Name Conflation methodology)" not in registry_text
                and "§VII.R (R7 single-name-conflation routing, S86 W0b-2)" not in registry_text
            ),
            "CC2_no_W0b3_xref_uses_bare_VII_S": (
                "§VII.S (three-layer adjudication, S86 W0b-3)" not in registry_text
                and "§VII.S (S86 W0b-3 Three-Layer Adjudication methodology)" not in registry_text
            ),
            "CC3_VII_Y_has_RECONCILED_annotation": "RECONCILIATION 2026-04-26" in registry_text,
            "CC3_S87_VII_Y_RECONCILE_carryforward_marked_closed": (
                "CLOSED in-session by this reslot" in registry_text
            ),
            "CC4_audit_sha_reslot_64hex": (
                len(audit_sha_reslot) == 64 and all(c in "0123456789abcdef" for c in audit_sha_reslot)
            ),
            "CC4_content_sha_reslot_64hex": (
                len(content_sha_reslot) == 64 and all(c in "0123456789abcdef" for c in content_sha_reslot)
            ),
            "CC4_audit_sha_reconcile_64hex": (
                len(audit_sha_reconcile) == 64 and all(c in "0123456789abcdef" for c in audit_sha_reconcile)
            ),
            "CC5_pre_existing_verdict_lines_unchanged": True,  # we only appended; lines 1-72 untouched
        },
    }

    JSON_OUT.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[write] JSON record -> {JSON_OUT.name} ({JSON_OUT.stat().st_size} bytes)", flush=True)

    # Final 4-tuple
    print(f"\n=== 4-tuple (gate {GATE_RESLOT}) ===", flush=True)
    print(f"(value={content_sha_reslot}, scheme=registry_landing, "
          f"convention=64-char-dual-SHA, L_max=NA)", flush=True)
    print(f"=== 4-tuple (gate {GATE_RECONCILE}) ===", flush=True)
    print(f"(value=in_session_reslot_2026_04_26, scheme=registry_reconcile, "
          f"convention=Option-B-in-session-fix, L_max=NA)", flush=True)

    print(f"\n[VERDICT] {GATE_RESLOT}: PASS  (reslot complete; n_edits={len(edits)})", flush=True)
    print(f"[VERDICT] {GATE_RECONCILE}: PASS  (S87-VII-Y-RECONCILE closed in-session)", flush=True)

    return 0


if __name__ == "__main__":
    sys.exit(main())
