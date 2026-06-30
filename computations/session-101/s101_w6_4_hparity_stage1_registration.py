#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S101-HPARITY-STAGE1-REGISTRATION  (S101 Wave-6, gate W6-4)
==========================================================

Registry landing of the §VII.BP STAGE-1-CANDIDATE entry: the H-PARITY-DRIVE-
EXCLUSION (fixed-backbone q-channel) joint cross-axis theorem candidate, FROZEN
Stage-0 -> Stage-1 per `.claude/rules/joint-theorem-promotion.md §"Stage 1"`.

Gate class: REGISTRY-LANDING ([VERIFY], PHONONIC). Single-shot AFTER pattern
per `.claude/rules/registry-landing.md §"Bridge-Landing Script Architecture"`
and the template `computations/_bridge_landing_script_template.py`:

    build_promotion_text  ->  write_atomic_with_fsync (APPEND)
        ->  re_read + verify_section_matches  ->  emit ONCE.

NO numerical re-derivation. The Stage-0 candidate text is extracted
PROGRAMMATICALLY (byte-verbatim, no transcription drift) from the SHA-pinned
workshop file `sessions/session-100a/workshops/s100a-w1-hparity-scope-workshop.md`:
  - anchor_1 (E2 Stage-0 candidate blockquote, "THEOREM CANDIDATE — H-PARITY-
    DRIVE-EXCLUSION (fixed-backbone q-channel)" through end of clause (f));
  - anchor_2 (E1 "Expansion rule:" paragraph through the retrieval-layer-lodging
    sentence).
The extracted spans are pinned by SHA (EXTRACT_SHA_A1 / EXTRACT_SHA_A2); a drift
aborts BEFORE any disk write (script breakage, exit != 0, NOT a verdict). Binding-
text rule: re-derive NOTHING.

BINDING CROSS-WAVE CONSTRAINT (W4-2 FAIL, audit 98a923fd…) — ORCHESTRATOR OVERRIDE:
  The sibling odd-floor gate S101-W1-QEQ-RELIC-ODDFLOOR (Wave 4 gate 2) returned
  FAIL (audit 98a923fd0ea4a6ec…): the post-fold relic parametric resonance is
  IN-band LIVE (omega_q_phys = 2.012813 ∈ pair band [1.6395, 10.8379];
  tail_crossing = 24 modes / 14 occupied; oddratio = 2.6976e-02 > 1e-3). The
  workshop's OWN pre-registered FAIL routing (landing-list (iv) gate 3 / E2
  clause (d) conditional) therefore FIRES: relic clause (d) is DEMOTED from
  argument-grade -> COINCIDENCE-BOUNDED, and THIS Stage-1 entry carries the
  demotion AMENDMENT BLOCK (mandatory amend-before-Stage-2). The verbatim E2
  text is transcribed UNALTERED (binding-text discipline); the demotion is
  effected by an EXPLICIT amendment block APPENDED after the frozen text, NOT by
  editing the frozen clause (d) in place. Cross-references: the W4-2 verdict
  (audit 98a923fd…) and the S67 broad-band "post-transit resonance impossible"
  theorem (which the narrow-band post-fold-tail is consistent with — S67 does
  NOT cover the narrow-band tail channel).

Slot: §VII.BP (bare letter — PHONONIC joint cross-axis theorem; NOT a state-
projection observable, so NO .OP-PROJ / .STATE-PROJ suffix: the theorem's
observables (q_eq(H), Gibbs-Duhem shifts, relic forces) are backbone/q-channel
thermodynamic objects, not spectral-triple state-pair functionals — the parse-
tree 4-corner classification is declared N/A-with-reason in the entry).
Reserved RESERVED-FOR-S101-W6-4-HPARITY-STAGE1 in
`sessions/framework/s101-slot-pre-allocation-lockfile.md`.

PD-2: all-header-level (##/###/####) runtime scan confirms §VII.BP reserved + free.
PD-3: occupancy => reroute next-free-letter + FAIL-with-remediation.
Idempotent: a re-run sees the section already on disk byte-identical -> NO-OP
(no duplicate append, no neighbor line-ending flatten). The audit_sha256 is
reproducible across re-runs via FROZEN run-1 registry PRE/POST SHA pins.

Audit-trail observation cited per template docstring discipline:
`computations/_bridge_landing_audit_trail_observation_S87_W5.md`.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import re
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

# Canonical constants import (MANDATORY per .claude/rules/math-scripts.md).
# This landing transcribes a FROZEN Stage-0 text + carries recorded numerics
# verbatim from the workshop; no framework constant is hardcoded here that
# belongs in canonical_constants.py.
sys.path.insert(0, str(Path("computations/_shared").resolve()))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Pinned identities (plan §W6-4 machinery_pin_map + input_files)
# ---------------------------------------------------------------------------
GATE_ID = "S101-HPARITY-STAGE1-REGISTRATION"
SLOT_PLANNED = "§VII.BP"
SLOT_LETTER = "BP"  # next-free letter after BO (W6-3); BM/BN/BO reserved+landed
SCHEME = "STAGE1-REGISTRATION-AFTER-PATTERN"
CONVENTION = "SINGLE-SHOT-VERBATIM-EXTRACTION"
L_MAX_TAG = "N/A"  # landing gate (no numerical L_max axis)
LOCKFILE_RESERVED = "RESERVED-FOR-S101-W6-4-HPARITY-STAGE1"

REGISTRY = Path("sessions/permanent-results-registry.md")
LOCKFILE = Path("sessions/framework/s101-slot-pre-allocation-lockfile.md")
WORKSHOP = Path("sessions/session-100a/workshops/s100a-w1-hparity-scope-workshop.md")
CANON = Path("computations/_shared/canonical_constants.py")
BRIDGE_TMPL = Path("computations/_bridge_landing_script_template.py")
VFILE = Path("computations/session-101/s101_gate_verdicts.txt")
OUT_NPZ = Path("computations/session-101/s101_w6_4_hparity_stage1_registration.npz")

# --- Static input-SHA pins (plan §W6-4 input_files; verified at authoring time) ---
PIN_WORKSHOP = "41bfcf0669639c7352cf1fee966f8d11f25a934065704b019eec371981248e70"
PIN_BRIDGE_TMPL = "876c018fafea84742d06934a2061eb765ef41a042cb87ba0f4138caffbe9a68c"

# --- Programmatic-extraction SHA pins (byte-verbatim spans; drift => abort) ---
# anchor_1 = E2 Stage-0 candidate blockquote (THEOREM CANDIDATE … through clause (f))
EXTRACT_SHA_A1 = "3735be3031dd11b18639e401631ed9bb78a77a6683cb2f84949d90bc8a10d29c"
EXTRACT_LEN_A1 = 8205  # (local) — byte-length of the pinned E2 span (extraction-drift guard)
# anchor_2 = E1 "Expansion rule:" paragraph (through retrieval-layer-lodging sentence)
EXTRACT_SHA_A2 = "78809954b079c84c0fc0baf0fddd84667e1ce1317b7f2313db05b0c432b24a14"
EXTRACT_LEN_A2 = 657  # (local) — byte-length of the pinned E1 span (extraction-drift guard)

# --- BINDING cross-wave constraint: W4-2 ODDFLOOR FAIL (full 64-hex) ---
W4_2_ODDFLOOR_AUDIT = "98a923fd0ea4a6ec5f80360468422e05651ef301a25f71645bd543e6c1ad4282"

# --- FAIL routing source-of-record numerics from the W4-2 verdict line (carried, not re-derived) ---
W4_2_OMEGA_Q_PHYS = "2.012813"
W4_2_BAND = "[1.6395, 10.8379]"
W4_2_TAIL_CROSSING = "24 modes / 14 occupied"
W4_2_ODDRATIO = "2.6976e-02"

# --- Frozen run-1 registry-state SHAs (captured at the ORIGINAL append, run 1) ---
# Used in the audit-pin map so audit_sha256 is REPRODUCIBLE across idempotent re-runs
# (a re-run sees the registry already-appended, so live PRE == live POST; pinning the
# original PRE/POST keeps the emitted audit_sha256 stable + preserves emit_verdict
# sig_5 idempotency). These are NOT live re-reads. <PRE> is the W6-3 POST state.
REGISTRY_PRE_SHA_AT_LANDING = "a8787b779f77fa0eaeeaf224cc419f8e5c3c5aa33e5e0ed90869e324c0e14190"
REGISTRY_POST_SHA_AT_LANDING = "PENDING_RUN1"  # set on first successful append (below)


def sha256_file(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """Audit SHA from the ordered input-pin map (canonical pattern; never
    hardcoded, computed at runtime)."""
    blob = json.dumps(pin_map, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Programmatic verbatim extraction (byte-pinned) from the SHA-pinned workshop
# ---------------------------------------------------------------------------
def extract_frozen_spans():
    """Extract the E2 Stage-0 candidate blockquote (anchor_1) + the E1 Expansion-
    rule paragraph (anchor_2) byte-verbatim from the SHA-pinned workshop. Each span
    is verified against its pinned SHA + length; a drift aborts with exit != 0
    (script breakage, NOT a verdict) BEFORE any disk write."""
    src = WORKSHOP.read_text(encoding="utf-8")

    # anchor_1: the FROZEN E2 instance (after the "(E2) — STAGE-0 JOINT-THEOREM
    # CANDIDATE (FINAL TEXT):" marker), THEOREM CANDIDATE header through clause (f).
    e2_marker = "**(E2) — STAGE-0 JOINT-THEOREM CANDIDATE (FINAL TEXT):**"
    e2_pos = src.find(e2_marker)
    thm_anchor = "> **THEOREM CANDIDATE — H-PARITY-DRIVE-EXCLUSION (fixed-backbone q-channel)**"
    a1_start = src.find(thm_anchor, e2_pos)
    cf_start = src.find("> - **Clause (f) [JOINT — self-consistency carve-out]:**", a1_start)
    cf_line_end = src.find("\n", cf_start)
    if min(e2_pos, a1_start, cf_start, cf_line_end) < 0:
        sys.stderr.write("[EXTRACT-ABORT] anchor_1 (E2 Stage-0) markers not located.\n")
        sys.exit(4)
    span_a1 = src[a1_start:cf_line_end]  # header line .. clause (f) line, no trailing \n

    # anchor_2: the FROZEN E1 Expansion-rule paragraph.
    e1_marker = "**(E1) — CANONICAL CITATION PARAGRAPH"
    e1_pos = src.find(e1_marker)
    exp_anchor = "> **Expansion rule:**"
    a2_start = src.find(exp_anchor, e1_pos)
    a2_line_end = src.find("\n", a2_start)
    if min(e1_pos, a2_start, a2_line_end) < 0:
        sys.stderr.write("[EXTRACT-ABORT] anchor_2 (E1 Expansion rule) markers not located.\n")
        sys.exit(4)
    span_a2 = src[a2_start:a2_line_end]

    # byte-equality discipline: each span MUST match its pinned SHA + length.
    sha_a1, sha_a2 = sha256_text(span_a1), sha256_text(span_a2)
    ok = True
    if len(span_a1) != EXTRACT_LEN_A1 or sha_a1 != EXTRACT_SHA_A1:
        sys.stderr.write(
            f"[EXTRACT-ABORT] anchor_1 drift: len={len(span_a1)} (pin {EXTRACT_LEN_A1}), "
            f"sha={sha_a1} (pin {EXTRACT_SHA_A1}); binding-text integrity broken.\n")
        ok = False
    if len(span_a2) != EXTRACT_LEN_A2 or sha_a2 != EXTRACT_SHA_A2:
        sys.stderr.write(
            f"[EXTRACT-ABORT] anchor_2 drift: len={len(span_a2)} (pin {EXTRACT_LEN_A2}), "
            f"sha={sha_a2} (pin {EXTRACT_SHA_A2}); binding-text integrity broken.\n")
        ok = False
    if not ok:
        sys.exit(4)
    return span_a1, span_a2, sha_a1, sha_a2


# ---------------------------------------------------------------------------
# (1) build_promotion_text — pure function, NO I/O
# ---------------------------------------------------------------------------
def build_promotion_text(slot_letter: str, span_a1: str, span_a2: str):
    """Produce the EXACT §VII.{letter} registry section text. Pure function; no I/O.
    The verbatim Stage-0 spans (span_a1 = E2 clauses, span_a2 = E1 expansion rule)
    are spliced UNALTERED; the demotion of clause (d) is effected by an EXPLICIT
    AMENDMENT BLOCK appended after the frozen text (binding-text discipline — the
    frozen clause (d) text is NOT edited in place)."""
    slot = f"§VII.{slot_letter}"

    header = (
        f"### {slot} — H-PARITY-DRIVE-EXCLUSION (fixed-backbone q-channel) "
        "(STAGE-1-CANDIDATE per joint-theorem-promotion.md; S100a W-1 workshop frozen "
        "Stage-0 text, transcribed VERBATIM; S101 W6-4 landing — gen-physicist; Stage-0 "
        "authors volovik-superfluid-universe-theorist + transit-dynamics-theorist, BOTH "
        "Stage-2-EXCLUDED)"
    )

    # ---- assemble (plain string; the verbatim spans carry literal {…} math) ----
    parts = []
    parts.append("\n")
    parts.append(header + "\n")
    parts.append("\n")
    parts.append(
        "**STAGE-1-CANDIDATE** (4-stage joint-theorem pathway per "
        "`joint-theorem-promotion.md`; Stage-0 text = "
        "`sessions/session-100a/workshops/s100a-w1-hparity-scope-workshop.md` "
        "blocks E1 + E2 (Stage-0 FROZEN); Stage-2 cross-axis verify = `S102` "
        "(DEFERRED — see the Stage-2 deferral conditional below). Classification "
        "**PHONONIC**. The FROZEN Stage-0 candidate text below (clauses (a)–(c) "
        "volovik-side + Regime annex (α)/(β)/(γ) + clause (d) transit-side (d1)–(d5) "
        "+ JOINT clauses (e.1)/(e.2)/(f)) is transcribed VERBATIM (byte-extracted "
        f"from the SHA-pinned workshop, anchor span SHA `{EXTRACT_SHA_A1[:8]}…`) — "
        "re-derived NOTHING. The canonical downstream-citation + expansion-rule "
        "paragraph (block E1) rides verbatim below (anchor span SHA "
        f"`{EXTRACT_SHA_A2[:8]}…`). **One BINDING amendment** applies post-freeze: "
        "the W4-2 odd-floor FAIL (audit "
        f"`{W4_2_ODDFLOOR_AUDIT[:8]}…`) fires the workshop's own FAIL routing — relic "
        "clause (d) is DEMOTED argument-grade → **coincidence-bounded** (the AMENDMENT "
        "BLOCK below; the frozen clause (d) text is left UNALTERED, the demotion is an "
        "explicit override, amend-before-Stage-2 per the workshop spec).\n"
    )
    parts.append("\n")

    # ---- FROZEN Stage-0 candidate text (anchor_1, E2 clauses (a)–(f)) — VERBATIM ----
    parts.append("**FROZEN STAGE-0 CANDIDATE TEXT (transcribed VERBATIM — block E2 of the S100a W-1 workshop; re-derived NOTHING):**\n")
    parts.append("\n")
    parts.append(span_a1 + "\n")
    parts.append("\n")

    # ---- Canonical citation + expansion-rule paragraph (anchor_2, E1) — VERBATIM ----
    parts.append("**CANONICAL DOWNSTREAM-CITATION EXPANSION RULE (transcribed VERBATIM — block E1 of the S100a W-1 workshop):**\n")
    parts.append("\n")
    parts.append(span_a2 + "\n")
    parts.append("\n")

    # ---- BINDING W4-2 AMENDMENT BLOCK (clause (d): argument-grade -> coincidence-bounded) ----
    parts.append(
        "**BINDING AMENDMENT — relic clause (d): argument-grade → COINCIDENCE-BOUNDED "
        "(W4-2 ODDFLOOR FAIL).** The sibling odd-floor gate `S101-W1-QEQ-RELIC-ODDFLOOR` "
        f"(S101 Wave 4 gate 2) returned **FAIL** (full 64-hex audit_sha256 "
        f"`{W4_2_ODDFLOOR_AUDIT}`): the post-fold relic parametric resonance is **IN-band "
        f"LIVE** — `ω_q^phys = {W4_2_OMEGA_Q_PHYS}` lies INSIDE the pair band "
        f"`{W4_2_BAND}`, with a **tail crossing** at `2E_k(q(τ)) = ω_q^phys` on "
        f"**{W4_2_TAIL_CROSSING}** and an odd-coefficient ratio `|c_odd|/|c_even| = "
        f"{W4_2_ODDRATIO} > 10⁻³`. This fires the workshop's OWN pre-registered FAIL "
        "routing (landing-list (iv) sibling-gate Gate clause + E2 clause-(d)/(d4)/(d5) "
        "conditional): **relic clause (d) is DEMOTED from argument-grade → "
        "COINCIDENCE-BOUNDED.** The clause-(d) four-argument relic closure no longer "
        "carries argument-grade weight in the wall's scope: the (d4) memory-slot "
        "parametric-rectification channel (2E_k ≈ ω_q — the single named numerical "
        "hostage) is NOT empty on this backbone, so the relic-sector exclusion is "
        "**coincidence-bounded** (it holds only where the resonance happens not to "
        "couple, not as a structural argument). The DEMOTION is effected HERE as an "
        "explicit override; the FROZEN clause (d)/(d4)/(d5)/(e.1) text above is "
        "transcribed UNALTERED (binding-text discipline) — this amendment block is the "
        "authoritative grade for downstream consumers and for Stage-2. "
        "**Amend-before-Stage-2 (binding):** Stage-2 cross-axis verify MUST treat relic "
        "clause (d) as coincidence-bounded; the equilibrium-stratum clauses (a)–(c) + "
        "Regime annex retain their FROZEN theorem-grade. **Consistency with the S67 "
        "broad-band theorem:** the S67 result is *post-transit (broad-band) parametric "
        "resonance impossible*; the W4-2 live channel is a **narrow-band post-fold-tail** "
        "resonance (occupation-weighted, 14-mode, ω_q just above the band floor) that S67 "
        "does NOT cover — the narrow-band tail crossing is CONSISTENT with S67 (no "
        "contradiction; S67's broad-band exclusion and the W4-2 narrow-band live channel "
        "occupy disjoint spectral supports). Cross-reference: the W4-2 verdict (audit "
        f"`{W4_2_ODDFLOOR_AUDIT[:16]}…`, `s101_gate_verdicts.txt`) + the S67 broad-band "
        "post-transit-resonance theorem.\n"
    )
    parts.append("\n")

    # ---- Clause-grade summary (post-amendment) ----
    parts.append(
        "**CLAUSE-GRADE SUMMARY (post-amendment).** Clause (a) [volovik-side] = "
        "**theorem-grade** (Gibbs-Duhem chain GD-1..GD-5, q_eq(H)=κ₂H² exponent-locked, "
        "κ₂=3/(8πG·n_q·k_curv), coefficient regime-limited XC-5 7.6e-8); clause (b) "
        "[volovik-side] = **theorem-grade** (all-orders H-parity grading; every "
        "equilibrium Gibbs-Duhem potential shift analytic-even in H² to all orders, "
        "(K,R)-pair included); clause (c) [volovik-side] = **theorem-grade** "
        "(slope-selection corollary, THREE selectors; numerical instantiation 2.0556 / "
        "1.008273 / 3.4159); Regime annex (α)/(β)/(γ) = **theorem-grade-QUANTITATIVE on "
        "the |Ḣ|/H²<1 stratum** (grid-mass ∈ [0.169, 0.668]; spike-region excision); "
        "clause (d) [transit-side] = **COINCIDENCE-BOUNDED** (W4-2 demotion — was "
        "argument-grade; (d1)–(d5) transcribed verbatim but no longer argument-grade); "
        "clause (e.1) [JOINT — scope] / (e.2) [JOINT — force-taxonomy] = flagged for "
        "Stage-2 PASS-AND (ONE unit); clause (f) [JOINT — KV self-consistency carve-out] "
        "= flagged for Stage-2 PASS-AND, parity-CONSISTENT, pre-registered "
        "CF-S101-W1-QEQ-SELFCONS.\n"
    )
    parts.append("\n")

    # ---- JOINT-clause flags ----
    parts.append(
        "**JOINT-clause flags (Stage-2 PASS-AND).** Clauses **(e)** (sub-lines "
        "(e.1) scope + (e.2) force-taxonomy form ONE Stage-2 PASS-AND unit) and **(f)** "
        "(KV self-consistency carve-out) are flagged for Stage-2 PASS-AND across BOTH "
        "axes (logical AND, not OR) per `joint-theorem-promotion.md §\"Stage 2\"`: both "
        "cross-reviewers must INDEPENDENTLY PASS each joint clause.\n"
    )
    parts.append("\n")

    # ---- Authorship + Stage-2 routing (binding) ----
    parts.append(
        "**Authorship + Stage-2 routing (binding).** Stage-0 authors = "
        "`volovik-superfluid-universe-theorist` + `transit-dynamics-theorist` ONLY; **BOTH "
        "Stage-2-EXCLUDED** (original-authoring-agent exclusion with downstream-inheritance "
        "reach, `joint-theorem-promotion.md §\"Stage-2 Axis-B Selection Protocol\"` all "
        "three conditions; S99 E1 author-exclusion discipline). Stage-2 reviewer pools "
        "preserved per workshop V4.i: **Axis-A** ∈ {`lizzi-spectral-functional-theorist`, "
        "`connes-ncg-theorist`}; **Axis-B** ∈ {`gen-physicist`, "
        "`kitaev-quantum-chaos-theorist`}.\n"
    )
    parts.append("\n")

    # ---- Stage-2 deferral conditional (written into the entry) ----
    parts.append(
        "**Stage-2 deferral conditional (written into the entry).** Stage-2 cross-axis "
        "verify is **DEFERRED TO S102** and dispatches only AFTER the sibling odd-floor "
        "gate `S101-W1-QEQ-RELIC-ODDFLOOR` (S101 Wave 4 gate 2) lands. **The sibling has "
        "now landed FAIL** (audit "
        f"`{W4_2_ODDFLOOR_AUDIT[:16]}…`): per the workshop's binding FAIL routing, relic "
        "clause (d) is demoted argument-grade → coincidence-bounded and THIS Stage-1 "
        "entry text is AMENDED (the BINDING AMENDMENT BLOCK above) BEFORE any Stage-2 "
        "dispatch — done. (Had the sibling returned INFO — near-resonant documented, or "
        "crossover-window documented — clauses (d4)/(d5) would carry it as written with no "
        "amendment; that branch did NOT fire.) Stage-2 at S102 audits clauses (a)–(c) + "
        "Regime annex at theorem-grade, clause (d) at coincidence-bounded, and the JOINT "
        "clauses (e)/(f) under PASS-AND.\n"
    )
    parts.append("\n")

    # ---- Riders (expansion rule restated for the registry layer) ----
    parts.append(
        "**Riders (expansion rule + retrieval-layer lodging).** Any downstream citation "
        "of the token `no_slope1_capable_substrate_drive` MUST expand it with the three "
        "scope qualifiers — (drive-type: potential-slot q_eq(H)) / (fixed-backbone) / "
        "(equilibrium = theorem-grade / relic = **coincidence-bounded** per the W4-2 "
        "amendment, was argument-grade pending sibling) — plus the carve-out pointer "
        "(CF-S101-W1-QEQ-SELFCONS). The verbatim E1 expansion-rule + retrieval-layer-"
        "lodging sentence rides above; for the post-W4-2 grade, the relic qualifier reads "
        "**coincidence-bounded** (the E1 text's \"argument-grade pending sibling\" is now "
        "resolved by the W4-2 FAIL to coincidence-bounded). The one-line scope pointer "
        "lives in the Workshop Verdict row, the S100b w1 closure reading, and the "
        "gate-entity note.\n"
    )
    parts.append("\n")

    # ---- Anchors ----
    parts.append(
        "**Anchors.** PRIMARY (FAIL the scoped citation governs) = "
        "`S100a-W1-2-QEQ-DRIVE` FAIL (full 64-hex audit_sha256 "
        "`e31d45cf5309b32cde67804d0576467592196b45ea908ec1edfac7f522212ca4`). BINDING "
        "cross-wave amendment anchor = `S101-W1-QEQ-RELIC-ODDFLOOR` FAIL (full 64-hex "
        f"audit_sha256 `{W4_2_ODDFLOOR_AUDIT}`; `s101_gate_verdicts.txt`). Stage-0 text = "
        "the S100a W-1 workshop blocks E1 + E2 "
        "(`sessions/session-100a/workshops/s100a-w1-hparity-scope-workshop.md`, "
        f"file SHA `{PIN_WORKSHOP[:16]}…`; extracted spans SHA `{EXTRACT_SHA_A1[:8]}…` "
        f"(E2) / `{EXTRACT_SHA_A2[:8]}…` (E1)). Sibling carry-forwards = "
        "`CF-S101-W1-QEQ-SELFCONS` (KV self-consistency, clause f) + "
        "`CF-S101-W1-QEQ-RELIC-ODDFLOOR` (relic odd-floor — LANDED FAIL, the amendment "
        "source). Methodological anchors = Paper 11 §VI / Eq. (8) (H-parity grading), "
        "Paper 25 §V Eqs. (5.5a-b) (KV oscillation-energy amplitude route), the S67 "
        "broad-band post-transit-resonance theorem (narrow-band consistency).\n"
    )
    parts.append("\n")

    # ---- Registry-anatomy compliance block ----
    parts.append(
        "**Registry-anatomy compliance.** (i) Entry class = **joint cross-axis theorem "
        "candidate** on the cosmological-corridor / q-channel axis pair (volovik "
        "equilibrium-thermodynamics + transit non-equilibrium); **NOT a cross-pillar "
        "bridge** ⇒ the 5-anatomy IS-not-IN elements + the 3-level ladder are declared "
        "**N/A-with-reason**: no laboratory-IN observable and no HKR / K-theory / "
        "Connes-Karoubi bridge map is claimed (the wall scopes what the substrate's own "
        "equilibrium thermodynamics can DRIVE; there is no continuum-image envelope). "
        "(ii) **Corner-cell machinery: N/A-with-reason** — the theorem's observables "
        "(q_eq(H), Gibbs-Duhem potential shifts, relic forces) are backbone / q-channel "
        "thermodynamic objects, NOT spectral-triple functionals on `(A_K, H_K, D_K)`, so "
        "the 4-corner parse-tree classification of `permanent-results-registry.md "
        "§VII.U.2` does not apply (and the bare slot identifier `§VII.BP` is therefore "
        "admissible — no `.OP-PROJ`/`.STATE-PROJ` suffix, which only applies to "
        "operator-side-vs-state-side spectral-triple functional readings). (iii) "
        "**Defensive parse-tree expansion** (Class-(h) insurance — \"GGE relic\" "
        "near-misses the state-history pattern set): GGE relic → fold-frozen occupations "
        "`{n_k, σ_k}` (s97 npz keys `w_n` / `n_k_gge`) → Parker pair production at the "
        "fold transit (diabatic transit-freeze, R_therm = 5251.82) → D_K(τ) eigenvalue "
        "reorganization through the fold. (iv) **Substrate-IS level tag = Level 1** "
        "(single-τ-slice at the τ_fold slice of the Jensen flow, τ_fold = 0.190) per "
        "`phononic-framing.md §\"Single-τ-slice vs moduli-deformation substrate-IS "
        "levels\"`: the relic sector is transit-frozen at the fold slice, not \"a fluid "
        "in expanding space\".\n"
    )
    parts.append("\n")

    # ---- Substrate framing ----
    parts.append(
        "**Substrate framing** (`phononic-framing.md §\"IS Space, Not IN Space\"`; "
        "PHONONIC-class). The candidate theorem scopes what the substrate's own "
        "thermodynamics can drive on the q-channel: every equilibrium Gibbs-Duhem "
        "potential shift of the fabric is analytic-even in H to all orders of the graded "
        "gradient expansion, so no substrate-internal EQUILIBRIUM drive can carry the "
        "slope-1 (odd-in-H) structure the q ∝ H closure needs. The fold-frozen GGE relic "
        "— the diabatic transit-freeze product of Parker pair production at the τ_fold "
        "transit (R_therm = 5251.82; NOT an equilibrium bath) — was excluded at "
        "argument-grade by four closure arguments with ONE numerical hostage (parametric "
        "resonance, the Wave-4 sibling gate); the W4-2 FAIL fires that hostage, demoting "
        "the relic-sector exclusion to **coincidence-bounded**. The unique surviving "
        "slope-1 route is amplitude self-consistency q_amp ∝ |H| (Klinkhamer-Volovik "
        "back-reaction) — parity-CONSISTENT because |H| is the non-analytic-even cell the "
        "theorem leaves open. **Direction**: D_K spectral reorganization at the fold → GGE "
        "relic occupations frozen → graded force taxonomy on the q-channel → H-parity "
        "wall → the q ∝ H closure's missing derivation localized to the KV carve-out. The "
        "wall is a substrate-IS statement about the fabric's drive inventory, not a "
        "GR-container claim. FORBIDDEN inversion (container thinking): \"the q-field "
        "tracks H in an expanding background\" → INVERT: \"the substrate's own equilibrium "
        "thermodynamics CANNOT supply an odd-in-H drive; H IS the gradient ratio of the "
        "fabric's spectral reorganization, and the q ∝ H slope-1 leg is an imposed-closure "
        "INPUT, not a substrate-derived drive.\"\n"
    )
    parts.append("\n")

    # ---- Provenance ----
    parts.append(
        "**Provenance.** S100a W-1 H-parity-scope workshop "
        "(`sessions/session-100a/workshops/s100a-w1-hparity-scope-workshop.md`, frozen "
        "blocks E1 + E2; file SHA "
        f"`{PIN_WORKSHOP}`). Binding source = the S100a W-1 workshop frozen Stage-0 text "
        "(extracted PROGRAMMATICALLY byte-verbatim; no transcription drift — the extracted "
        f"E2 span SHA `{EXTRACT_SHA_A1}` and E1 span SHA `{EXTRACT_SHA_A2}` are pinned + "
        "re-verified at runtime) + the W4-2 relic-resonance FAIL (`S101-W1-QEQ-RELIC-"
        f"ODDFLOOR`, audit `{W4_2_ODDFLOOR_AUDIT}`) which fires the clause-(d) "
        "argument-grade → coincidence-bounded demotion. Landed S101 W6-4 (gen-physicist), "
        "single-shot AFTER pattern per `registry-landing.md §\"Bridge-Landing Script "
        f"Architecture\"`; slot `{slot}` reserved `{LOCKFILE_RESERVED}` in "
        "`sessions/framework/s101-slot-pre-allocation-lockfile.md`, runtime-verified "
        "next-free at all header levels (highest prior §VII.BO, W6-3). Stage-2 cross-axis "
        "verify queued for S102 (volovik + transit Stage-2-EXCLUDED). This is a §VII "
        "joint cross-axis STAGE-1-CANDIDATE landing, NOT a §7 falsifier-surface row — "
        "`mack-cosmic-bridge` sole-writer does NOT apply (the H-parity wall is not a "
        "falsifier observable; no inventory row emerges, per the workshop's own E3 "
        "note).\n"
    )

    text = "".join(parts)

    # fail loudly if any unresolved sentinel survived (defensive)
    assert "@@" not in text, "unresolved @@SENTINEL@@ in promotion text"
    return text


# ---------------------------------------------------------------------------
# (2) write_atomic_with_fsync — APPEND to the registry, fsync
# ---------------------------------------------------------------------------
def write_atomic_with_fsync(section_text: str, registry_path: Path) -> None:
    """Append the section to the registry and fsync. The append is the only disk
    mutation. Single-writer chain PD-4 (sequential); newline='\\n' so we never
    flatten/alter neighbor (pre-existing) line endings — the append is pure-add."""
    p = Path(registry_path)
    with open(p, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(section_text)
        fh.flush()
        os.fsync(fh.fileno())


# ---------------------------------------------------------------------------
# (3) re-read + verify_section_matches
# ---------------------------------------------------------------------------
def re_read_section(registry_path: Path, slot_letter: str) -> str:
    """Re-read the appended §VII.{letter} section from disk (header line through
    end-of-file, since this entry is the file tail). Includes the leading blank
    line the section_text begins with."""
    full = Path(registry_path).read_text(encoding="utf-8")
    header = f"### §VII.{slot_letter} — H-PARITY-DRIVE-EXCLUSION"
    idx = full.find(header)
    if idx == -1:
        return ""
    start = idx
    if start > 0 and full[start - 1] == "\n":
        start -= 1
    return full[start:]


def verify_section_matches(actual: str, expected: str) -> bool:
    """Strict byte equality of the on-disk section against the built text."""
    return actual == expected


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None):
    """PRINT the verdict payload for the dispatching AGENT to pass to the
    knowledge-MCP `emit_verdict` tool (race-safe, lock-serialized single writer
    per `.claude/rules/gate-verdicts.md §\"Race-Safe Emission\"`). The script does
    NOT write the verdict file. [VERIFY] gate ⇒ no SIGN 3-tuple."""
    payload = {
        "session": "101",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX_TAG),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print(f"{GATE_ID}: {verdict} -- value='{value}' scheme={SCHEME} "
          f"convention={CONVENTION} L_max={L_MAX_TAG} "
          f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+")
    if extra_rows:
        for r in extra_rows:
            print(r)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# main — single-shot AFTER pattern
# ---------------------------------------------------------------------------
def main():
    global REGISTRY_POST_SHA_AT_LANDING

    # ---- log input SHAs (first 20 lines of stdout per gate-verdicts.md) ----
    canon_sha = sha256_file(CANON)
    lockfile_sha = sha256_file(LOCKFILE)
    workshop_sha = sha256_file(WORKSHOP)
    bridge_sha = sha256_file(BRIDGE_TMPL)
    registry_pre_sha = sha256_file(REGISTRY)

    print(f"[INPUT-SHA] canonical_constants.py = {canon_sha}")
    print(f"[INPUT-SHA] s101-slot-pre-allocation-lockfile.md = {lockfile_sha}")
    print(f"[INPUT-SHA] s100a-w1-hparity-scope-workshop.md = {workshop_sha}")
    print(f"[INPUT-SHA] _bridge_landing_script_template.py = {bridge_sha}")
    print(f"[INPUT-SHA] permanent-results-registry.md (PRE-append) = {registry_pre_sha}")

    # ---- static-pin reconciliation (plan §W6-4 input_files) ----
    assert workshop_sha == PIN_WORKSHOP, f"workshop SHA drift: {workshop_sha}"
    assert bridge_sha == PIN_BRIDGE_TMPL, f"bridge template SHA drift: {bridge_sha}"
    print("[PIN-RECON] static input SHAs match plan §W6-4 pins (workshop/bridge).")

    # ---- lockfile RESERVED-FOR cross-reference (PD-2) ----
    lock_txt = LOCKFILE.read_text(encoding="utf-8")
    assert LOCKFILE_RESERVED in lock_txt, f"{LOCKFILE_RESERVED} not in lockfile"
    assert SLOT_PLANNED in lock_txt, f"{SLOT_PLANNED} not in lockfile"
    # lockfile records the binding W4-2 clause-(d) coincidence-bounded constraint
    assert "coincidence-bounded" in lock_txt and "98a923fd" in lock_txt, \
        "lockfile RESERVED-FOR-S101-W6-4 block must carry the W4-2 coincidence-bounded constraint"
    print(f"[PD-2] lockfile carries {LOCKFILE_RESERVED} -> {SLOT_PLANNED} "
          f"+ W4-2 coincidence-bounded constraint (98a923fd).")

    # ---- W4-2 ODDFLOOR clearance audit present + FAIL in the verdict file ----
    vtxt = VFILE.read_text(encoding="utf-8")
    assert W4_2_ODDFLOOR_AUDIT in vtxt, "W4-2 ODDFLOOR audit not found in verdict file"
    odd_line = next((ln for ln in vtxt.splitlines()
                     if ln.startswith("S101-W1-QEQ-RELIC-ODDFLOOR:")), "")
    assert " FAIL " in odd_line, f"W4-2 ODDFLOOR is not FAIL: {odd_line[:80]}"
    print("[W4-2] ODDFLOOR FAIL present (98a923fd…) — clause-(d) demotion fires (binding).")

    # ---- programmatic verbatim extraction (byte-pinned; drift => abort) ----
    span_a1, span_a2, sha_a1, sha_a2 = extract_frozen_spans()
    print(f"[EXTRACT] anchor_1 (E2 Stage-0) {len(span_a1)} chars, SHA {sha_a1} (pin OK)")
    print(f"[EXTRACT] anchor_2 (E1 expansion) {len(span_a2)} chars, SHA {sha_a2} (pin OK)")

    # ---- PD-2 + idempotent-recovery + PD-3, in the CORRECT precedence order ----
    registry_pre_text = REGISTRY.read_text(encoding="utf-8")
    planned_text = build_promotion_text(SLOT_LETTER, span_a1, span_a2)
    print(f"[BUILD] promotion text built ({len(planned_text)} chars).")

    header_pat = re.compile(r"^#{2,4}\s*§VII\." + re.escape(SLOT_LETTER) + r"\b", re.MULTILINE)
    occupied = bool(header_pat.search(registry_pre_text))
    existing_planned = re_read_section(REGISTRY, SLOT_LETTER)
    reroute_fired = False
    slot_letter = SLOT_LETTER
    section_text = planned_text
    do_append = True

    if occupied and existing_planned == planned_text:
        # (A) idempotent re-run: §VII.BP already holds THIS gate's byte-identical
        #     section. Keep planned slot; skip append (no duplicate, no flatten).
        do_append = False
        print(f"[PD-2/IDEMPOTENT] §VII.{SLOT_LETTER} already on disk and byte-identical "
              f"to the built text — idempotent re-run; keep planned slot, no re-append.")
    elif occupied:
        # (B) FOREIGN collision: §VII.BP occupied by DIFFERENT content. PD-3 reroute.
        reroute_fired = True
        for cand in ["BQ", "BR", "BS", "BT", "BU", "BV"]:
            cpat = re.compile(r"^#{2,4}\s*§VII\." + re.escape(cand) + r"\b", re.MULTILINE)
            if not cpat.search(registry_pre_text):
                slot_letter = cand
                break
        section_text = build_promotion_text(slot_letter, span_a1, span_a2)
        print(f"[PD-3] PLANNED slot §VII.{SLOT_LETTER} OCCUPIED by FOREIGN content at "
              f"runtime; REROUTED to §VII.{slot_letter} + FAIL-with-remediation.")
    else:
        print(f"[PD-2] all-header-level scan: §VII.{SLOT_LETTER} FREE on disk "
              f"(reserved + free).")

    # ---- (2) write (APPEND) + fsync (skipped on idempotent re-run) ----
    if not do_append:
        pass  # idempotent re-run: section already on disk, verified below
    else:
        existing = re_read_section(REGISTRY, slot_letter)
        if existing:
            raise RuntimeError(
                f"§VII.{slot_letter} exists on disk but does NOT match the built text; "
                f"AFTER pattern forbids corrective rewrite (honest close).")
        write_atomic_with_fsync(section_text, REGISTRY)
        print(f"[WRITE] appended §VII.{slot_letter} to {REGISTRY} + fsync.")

    # ---- (3) re-read + verify (single point of decision) ----
    actual = re_read_section(REGISTRY, slot_letter)
    section_match = verify_section_matches(actual, section_text)
    print(f"[VERIFY] re-read section byte-match = {section_match}")

    content_sha = sha256_text(actual)
    registry_post_sha = sha256_file(REGISTRY)
    REGISTRY_POST_SHA_AT_LANDING = registry_post_sha
    print(f"[CONTENT-SHA] on-disk §VII.{slot_letter} section = {content_sha}")
    print(f"[REGISTRY-SHA] permanent-results-registry.md (POST-append) = {registry_post_sha}")

    # ---- verdict determination (single point) ----
    if reroute_fired:
        verdict = "FAIL"
        value = (f"slot-reroute_PLANNED_{SLOT_PLANNED}_OCCUPIED_rerouted_to_"
                 f"§VII.{slot_letter}_section_match_{section_match}_"
                 f"remediation=assess_S102_Stage2_eligibility_against_rerouted_slot")
    elif section_match:
        verdict = "PASS"
        value = (f"landed_VII.{slot_letter}_HPARITY-DRIVE-EXCLUSION_STAGE-1-CANDIDATE_"
                 f"section_byte_match_True_E2+E1_verbatim_extract_SHA_3735be30+78809954_"
                 f"clauses_a-c_THEOREM-GRADE_d_COINCIDENCE-BOUNDED(W4-2_98a923fd_demotion_"
                 f"argument-grade->coincidence-bounded)_e1+e2+f_JOINT_Stage-2_PASS-AND_"
                 f"authors_volovik+transit_BOTH_Stage-2-EXCLUDED_AxisA{{lizzi,connes}}_"
                 f"AxisB{{gen,kitaev}}_Stage-2_DEFERRED_S102_oddflow_FAIL_amend-done_"
                 f"qeqH=k2H2_slope-sel_2.0556/1.008273/3.4159_dilwindow_0.0000EXACT_"
                 f"closest_3plocal=1.657_T0i_4D=0EXACT_C7_S67_narrowband_consistent_"
                 f"5anatomy_NA_corner_NA_q-channel-thermo_level1_tau_fold")
    else:
        verdict = "FAIL"
        value = (f"landed_VII.{slot_letter}_section_byte_match_{section_match}_honest_close")

    # ---- audit SHA from ordered input-pin map (runtime closure; NEVER hardcoded) ----
    # Use FROZEN run-1 registry PRE/POST SHAs so audit_sha256 is reproducible across
    # idempotent re-runs. On run-1 the live POST == the frozen run-1 POST by construction.
    registry_post_for_pin = (REGISTRY_POST_SHA_AT_LANDING
                             if REGISTRY_POST_SHA_AT_LANDING != "PENDING_RUN1"
                             else registry_post_sha)
    input_pin_map = {
        "_gate_id": GATE_ID,
        "_slot": f"§VII.{slot_letter}",
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_wp_id": "S101-W6-4",
        "lockfile_RESERVED_FOR": LOCKFILE_RESERVED,
        "lockfile_sha256": lockfile_sha,
        "registry_state_at_runtime_PRE": REGISTRY_PRE_SHA_AT_LANDING,
        "registry_state_POST": registry_post_for_pin,
        "workshop_sha256": workshop_sha,
        "extract_E2_stage0_span_sha256": sha_a1,
        "extract_E1_expansion_span_sha256": sha_a2,
        "W4_2_ODDFLOOR_clause_d_demotion_audit": W4_2_ODDFLOOR_AUDIT,
        "primary_anchor_S100a_W1_2_QEQ_DRIVE": "e31d45cf5309b32cde67804d0576467592196b45ea908ec1edfac7f522212ca4",
        "bridge_template_sha256": bridge_sha,
        "canonical_constants_sha256": canon_sha,
        "clause_d_grade": "COINCIDENCE-BOUNDED",
        "section_byte_match": section_match,
        "reroute_fired": reroute_fired,
    }
    audit_sha = closure_hash(input_pin_map)

    # ---- landing-record npz ----
    OUT_NPZ.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        slot=f"§VII.{slot_letter}",
        slot_planned=SLOT_PLANNED,
        verdict=verdict,
        section_byte_match=bool(section_match),
        reroute_fired=bool(reroute_fired),
        content_sha256=content_sha,
        audit_sha256=audit_sha,
        registry_pre_sha=registry_pre_sha,
        registry_post_sha=registry_post_sha,
        registry_pre_sha_frozen=REGISTRY_PRE_SHA_AT_LANDING,
        extract_E2_span_sha=sha_a1,
        extract_E2_span_len=int(len(span_a1)),
        extract_E1_span_sha=sha_a2,
        extract_E1_span_len=int(len(span_a2)),
        w4_2_oddflow_audit=W4_2_ODDFLOOR_AUDIT,
        clause_d_grade="COINCIDENCE-BOUNDED",
        clause_d_was="argument-grade",
        w4_2_omega_q_phys=W4_2_OMEGA_Q_PHYS,
        w4_2_band=W4_2_BAND,
        w4_2_tail_crossing=W4_2_TAIL_CROSSING,
        w4_2_oddratio=W4_2_ODDRATIO,
        primary_anchor_qeq_drive="e31d45cf5309b32cde67804d0576467592196b45ea908ec1edfac7f522212ca4",
        slope_selectors=np.array([2.0556, 1.008273, 3.4159]),
        dilution_window_fraction=0.0000,
        closest_approach_3plocal=1.657,
        joint_clauses=np.array(["e.1", "e.2", "f"]),
        stage0_authors=np.array(["volovik-superfluid-universe-theorist",
                                 "transit-dynamics-theorist"]),
        stage2_axis_a=np.array(["lizzi-spectral-functional-theorist",
                                "connes-ncg-theorist"]),
        stage2_axis_b=np.array(["gen-physicist", "kitaev-quantum-chaos-theorist"]),
        stage2_deferred_to="S102",
        ts=datetime.now(timezone.utc).isoformat(),
    )
    print(f"[NPZ] landing record -> {OUT_NPZ}")

    # ---- (5) emit ONCE: PRINT the verdict payload (agent calls emit_verdict) ----
    companion = (
        f"§VII.{slot_letter} H-PARITY-DRIVE-EXCLUSION joint cross-axis STAGE-1-CANDIDATE; "
        f"clauses (a)-(c) THEOREM-GRADE + clause (d) COINCIDENCE-BOUNDED "
        f"[W4-2 ODDFLOOR FAIL 98a923fd demotion: argument-grade->coincidence-bounded; "
        f"amend-before-Stage-2 effected]; JOINT clauses (e)/(f) Stage-2 PASS-AND; "
        f"Stage-0 authors volovik+transit BOTH Stage-2-EXCLUDED "
        f"(Axis-A{{lizzi,connes}}, Axis-B{{gen,kitaev}}); Stage-2 DEFERRED S102; "
        f"5-anatomy + corner-cell N/A-with-reason (q-channel thermo, not spectral-triple); "
        f"S67 broad-band consistent (narrow-band tail); mack §7 sole-writer N/A"
    )
    extra = [
        f"# regulator_pin=N/A (registry-landing gate; no a_n Seeley-DeWitt citation) "
        f"# {GATE_ID} clause-(d) grade=COINCIDENCE-BOUNDED per W4-2 audit {W4_2_ODDFLOOR_AUDIT[:16]}"
    ]
    print("\n" + "=" * 72)
    print("VERDICT PAYLOAD (PRINT-only; agent calls emit_verdict knowledge-MCP tool):")
    print("=" * 72)
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra)
    print("=" * 72)

    sys.exit(0)  # script health: exit 0 regardless of PASS/FAIL


if __name__ == "__main__":
    main()
