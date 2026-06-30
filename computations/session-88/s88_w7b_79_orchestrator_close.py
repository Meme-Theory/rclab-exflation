#!/usr/bin/env python3
"""
S88 W7b-79 — S88-VII-AK-STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE
============================================================================

Gate: S88-VII-AK-STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE (trigger: AUDIT)
Wave: W7b (METHODOLOGY-class registry-landing)
Plan: sessions/session-plan/session-88-plan-w7b.md §W7b-79

Pre-registered threshold (per session-88-plan-w7b.md §W7b-79 Field "Thresholds"):
  PASS: All 4 grep-cross-checks pass (Step 3 of plan §W7b-79 Method) AND
        audit_sha256 unique in s88_gate_verdicts.txt AND sha256_of_plan_block
        computed and appended to methodology-wave-allowlist.md AND landed slot
        equals planned slot §VII.AK.
  INFO: §VII.AK slot pre-occupied by parallel writer → reroute to next-free
        per S84 W2a-11 §VII.M→§VII.N precedent (math content preserved).
        Plan §135 INFO clause.
  FAIL: Any of plan §134 (a)-(e) FAIL conditions surface, OR any registry-
        landing structural defect (anatomy / level / structure-tag missing).

Per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under
Parallel-Writer Race" item 3 (binding rule, outranks per-session plan per
`CLAUDE.md §"No Technical Debt"`): when planned slot is occupied at runtime,
rerouting to next-free-letter is permitted, BUT the verdict line MUST emit
FAIL-with-remediation (not PASS, not INFO) so the rerouting is visible in
the audit trail. This script implements that binding semantics: when
slot_label != "AK", composite=FAIL with value field documenting the reroute.

Per `.claude/rules/registry-landing.md §"Bridge-Landing Script Architecture
(single-shot pattern)"` AFTER-pattern (W3c-30):

  build_promotion → fsync → re-read → verify → emit (exactly one verdict line)

This is METHODOLOGY-class per `wave-classification.md` M1-M4: artifact-
existence-with-substantive-content predicate (M1); Edit on registry +
Python append-only writer + grep cross-checks (M2); verbatim from S86 W-11
BULLETIN-S4/4A/W0W5 trio + S87 W7 LF closures + S86 W-13 REG-1/REG-2
anchor-structure precedent (M3); gate-ID W7b-79 allowlisted in
`.claude/rules/methodology-wave-allowlist.md` line 146 with
sha256_of_plan_block = 9395ab115bebf3e07e3d2db5445c49043083120e3dd0d7c147e5f990379ab1fe (M4).

Audit-trail observation cross-link: this is the second registry-landing
gate to use the W3c-30 single-shot AFTER-pattern (after W5a-37). It tests
the AFTER-pattern under the slot-collision-with-reroute case.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - sessions/permanent-results-registry.md (registry edit target)
  - .claude/rules/methodology-wave-allowlist.md (allowlist row already appended)
  - .claude/rules/registry-landing.md (SOURCE-DOUBLE-CITE-CO-PRIMARY schema)
  - .claude/rules/cross-pillar-bridge-anatomy.md (5 IS-not-IN anatomy + 3-level ladder)
  - .claude/rules/regulator-pin-discipline.md (W-11 RULE-2 STRENGTHENED parity-blindness)
  - .claude/rules/joint-theorem-promotion.md (STAGE-1-CANDIDATE 4-stage pathway)
  - sessions/session-plan/session-88-plan-w7b.md (plan source; §W7b-79 block)
  - computations/session-86/s86_gate_verdicts.txt (W-11 BULLETIN-S4/4A/W0W5 verdicts)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (spectrum cache pin)
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

# Ensure _shared is importable for canonical_constants
T0 = Path(__file__).resolve().parent
PROJECT_ROOT = T0.parent.parent
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# Pin metadata
GATE_ID = "S88-VII-AK-STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE"
SCHEME = "registry-landing"
CONVENTION = "source-double-cite-co-primary"  # (overridden in value-string when reroute)
L_MAX = "10"  # (local) plan-pinned canonical anchor; identity is L-independent
LINE_THRESHOLD_PASS = 18  # (local) plan-pinned ≥18-line registry-body criterion
PLANNED_SLOT = "AK"  # (local) plan §51 / line 76 target

# W-11 STRENGTHENED parity-blindness pin values (per plan §W7b-79 PRDR + canonical_constants.py)
GV_CANONICAL_DIFFERENCE = -40579.1500479506  # (local) S87 W8-8 promoted; gv_canonical_difference_FW
GV_SPREAD_PUBLICATION_FLOOR = 6.257e-10  # (local) publication-precision floor; PRU Class 8.3
MAX_PAIR_RATIO_A_5 = 9.240438549812e-01  # (local) S87 W8-2 promoted; max_pair_ratio_A_5_FW
M_KK_GEV = 7.4287e+16  # (local) canonical_constants.py:M_KK
A_5_EXTENDED = ("ζ", "Zubarev", "SDW", "anomaly", "cutoff_sqrt")  # (local) atlas pin

# Allowlist row sha256_of_plan_block pin (computed externally; see docstring M4)
SHA256_OF_PLAN_BLOCK = "9395ab115bebf3e07e3d2db5445c49043083120e3dd0d7c147e5f990379ab1fe"

# Files
SCRIPT_PATH = T0 / "s88_w7b_79_orchestrator_close.py"
NPZ_OUT = T0 / "s88_w7b_79_orchestrator_close.npz"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
ALLOWLIST_PATH = PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
RULE_REGISTRY_LANDING = PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"
RULE_BRIDGE_ANATOMY = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
RULE_REGULATOR_PIN = PROJECT_ROOT / ".claude" / "rules" / "regulator-pin-discipline.md"
RULE_JOINT_THEOREM = PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
PLAN_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w7b.md"
CANON_PY = SHARED_DIR / "canonical_constants.py"
S86_VERDICTS = PROJECT_ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"
SPECTRUM_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"


# ──────────────────────────────────────────────────────────────────────
# Helpers (mirror s88_w5a_cf20_source_double_cite_alpha_s.py pattern)
# ──────────────────────────────────────────────────────────────────────

def sha256_file(path: Path) -> str:
    if not path.exists():
        return "FILE-NOT-FOUND"
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def count_section_lines(file_path: Path, start_anchor: str, end_anchor: str) -> int:
    text = file_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    in_section = False
    count = 0  # (local) line counter
    for line in lines:
        if start_anchor in line:
            in_section = True
            continue
        if in_section and end_anchor in line:
            break
        if in_section:
            count += 1
    return count


def scan_next_free_letter(registry_text: str) -> str:
    """
    Scan ALL header levels (## §, ### §, #### §) per
    epistemic-discipline.md §"Registry-Write Hygiene" item 1.
    Find next-free letter X under §VII.A<X> double-letter allocation namespace.
    Returns "A<X>" where <X> is the lowest-ordered free letter A..Z.
    """
    pattern = re.compile(r"§VII\.A([A-Z])(?:[\.\s—\-]|$)")
    used_letters = set()  # (local)
    for m in pattern.finditer(registry_text):
        used_letters.add(m.group(1))
    for code in range(ord("A"), ord("Z") + 1):
        letter = chr(code)
        if letter not in used_letters:
            return f"A{letter}"
    raise RuntimeError("No free letter under §VII.A* — extend to §VII.B*")


def build_promotion_text(slot_label: str, planned_slot: str, audit_sha_placeholder: str = "PENDING") -> str:
    """
    Pure function: builds the §VII.<slot_label> promotion text in memory from
    pre-registered schema (no I/O before write). Per registry-landing.md
    AFTER-pattern. Embeds the slot-reroute remediation paragraph if
    slot_label != planned_slot.
    """
    rerouted = (slot_label != planned_slot)
    if rerouted:
        reroute_paragraph = (
            f"**Slot reroute remediation** (per `epistemic-discipline.md` §\"Registry-Write Hygiene under Parallel-Writer Race\" item 3 + S84 W2a-11 §VII.M→§VII.N precedent): "
            f"Plan §W7b-79 originally targeted §VII.{planned_slot} based on the S87 W-7 lockfile pre-allocation `RESERVED-FOR-W7-S88`. "
            f"At dispatch time §VII.{planned_slot} was occupied by S86 W-13 REG-1 (Basis-Completeness Theorem 2, 2026-04-27); §VII.AL by S86 W-13 REG-2; §VII.AM by S88 W1b2-65 (Universal Lock Condition); §VII.AN/AO/AP by S88 W5a-37/42/43 (α_s registry trio). "
            f"Next-free letter §VII.{slot_label} assigned per the registry-write-hygiene rule. "
            f"Math content preserved INTACT at §VII.{slot_label}; only the slot label diverged from plan. "
            f"Verdict line emits FAIL-with-remediation per the binding rule item 3 so the reroute is visible in the audit trail. "
            f"Source-Reconciliation Class-(c) PIN-DRIFT-FROM-STALE-SOURCE: lockfile not refreshed after intervening S86 W-13 / S88 W1b2 / S88 W5a landings.\n\n"
        )
    else:
        reroute_paragraph = ""

    block = f"""
## §VII.{slot_label} — STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE (S88 W7b-79 — orchestrator-direct write per wave-classification.md METHODOLOGY-class; mack-cosmic-bridge designated writer per feedback_mack-bridge-role.md, 2026-05-05)

{reroute_paragraph}ANCHOR-1 (V_input, axiomatic chain): connes-ncg KO-dim 6 + Pf=−1 BDI(J, γ_9) + Connes 1996 reconstruction theorem (axioms 1-7 + chirality + reality);
  algebraic premise: η-invariant and ALL even-grading regulator-weighted Mellin moments
  M_w(D_K) = Σ_n w_n Tr(D_K^{{-2n}}) with w_2k ≠ 0, w_2k+1 = 0 (Mellin-cone weight w_n = 2n)
  satisfy η(C_H · D_K · C_H^†) = η(C_epsH · D_K · C_epsH^†) = η(D_K) by axiom-level identity.
ANCHOR-2 (C_output, scope-locality): lizzi-spectral 4-corner classification §VII.U.2 (Corner I = even-grading spectrum-only family) + Mellin-cone weight w_n=2n;
  structural theorem CONDITIONAL on the V_input axiom-level identity acting BEFORE regulator-weight assignment;
  regulator-INDEPENDENT across A_5_extended atlas {{ζ, Zubarev, SDW, anomaly, cutoff_sqrt}}.
STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY (per `.claude/rules/registry-landing.md`
  §"SOURCE-DOUBLE-CITE-CO-PRIMARY"; calibration corpus instance #2 — instance #1 = S86 W-3 R3 Convergence #2 §VII.AC.4-class; V_input + C_output sequential chain
  with non-fungible roles: V_input alone supplies the axiom-layer premise but does not
  fix the conclusion; C_output alone is conditional on the algebra-choice premise from V_input;
  together they fix the conclusion uniquely).
Derivation chain: V_input (KO-dim 6 NCG-axiomatic chain on (A_K, H_K, D_K)) → A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) state-pair specification
  → C_output (functional-class assignment + Mellin-cone weight w_n=2n) → conclusion (even-grading
  parity-blindness across A_5_extended at L_max=10).
Closure SHA pin: audit_sha256 = {audit_sha_placeholder}
  (S88 W7b-79 verdict per `computations/session-88/s88_gate_verdicts.txt`).

**Level 1 (substrate-IS structural identity)**: η(C_H · D_K · C_H^†) = η(C_epsH · D_K · C_epsH^†) = η(D_K) AND
  M_w(C_H · D_K · C_H^†) = M_w(C_epsH · D_K · C_epsH^†) = M_w(D_K) for ALL even-weight w; regulator-INVARIANT
  across A_5_extended atlas; L-independent (holds at every L_max). Status: STRUCTURAL THEOREM.

**Level 2 (algebraic envelope)**: NOT APPLICABLE — structural-exact form replaces L^{{-α}} envelope.
  The identity holds AT EVERY L_max because it acts at the KO-dim 6 axiom level BEFORE regulator-weight
  assignment, not at the calculational layer. Contrast with W-5 cancellation theorem (which acts at the
  calculational layer via common-exponent (Δ_B/Δ_A)^p): W-11 STRENGTHENED is STRUCTURALLY STRONGER because
  axiom-level identity precedes regulator-weight assignment ⟹ holds for every R ∈ A_5_extended by
  construction, not by calculational cancellation. Status: STRUCTURAL PREDICTION (replaces convergence envelope).

**Level 3 (empirical anchor)**: per-regulator deviation = ZERO across A_5_extended atlas at L_max = 10.
  Anchor: `gv_canonical_difference_FW = -40579.1500479506` (S87 W8-8 promoted constant).
  Publication-precision floor: `gv_spread_FW = 6.257e-10` (relative-spread-normalized; per-regulator
  deviation = ZERO at full float64 precision; the 6.257e-10 figure is the publication-precision floor only,
  per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness — Publication-Precision Pre-Registration"
  PRU Class 8.3 MANDATORY at K=4). Status: EMPIRICAL CONFIRMATION at canonical L_max.

**IS-not-IN anatomy** (per `.claude/rules/cross-pillar-bridge-anatomy.md` 5 mandatory elements):
1. Substrate-IS observable: η(D_K) on (A_K^≤10, H_K^≤10, D_K^≤10) under chirality γ_9 + reality J
   satisfying KO-dim 6. The substrate IS this observable; η is NOT defined IN any container.
2. Laboratory-IN observable: APS-style η-invariant `R_eta_lab = ∫_BZ d^3 k Tr_{{M_2(C)}}(P_{{eta-positive}}(k) - P_{{eta-negative}}(k))`
   in laboratory BdG / 3He-B (η=0 prediction; (η=0, GV≠0) joint signature is the operational
   discrimination test). OE-form per `cross-pillar-bridge-anatomy.md` §"Element 2 OE-form discipline" S88 W7a-73 hardening.
3. Bridge map: KO-dim 6 NCG-axiomatic chain ∘ Connes-Karoubi pairing on the (C_H, C_epsH) parity-twin pair.
4. Algebraic envelope: structural-exact (regulator-invariant identity; replaces L^{{-α}} convergence bound;
   level-2 envelope is the structural-exact form per the 3-level ladder).
5. Empirical anchor: per-regulator deviation = ZERO at L_max=10; `gv_canonical_difference_FW = -40579.1500479506`;
   publication-precision floor `gv_spread_FW = 6.257e-10`.

**Substrate-IS level declaration** (per `.claude/rules/phononic-framing.md` §"Single-τ-slice vs moduli-deformation substrate-IS levels"):
  LEVEL-1 (single-τ-slice substrate-IS) at τ_fold = 0.190; the η-invariant and even-grading Mellin moments
  are intrinsic spectral-triple observables at this fixed τ-slice. NOT a moduli-deformation observable.

**Forward LEVEL-2 pin**: Cheeger-Simons / GV-Heitsch ODD-grading proxy required for parity-twin discrimination
  (LOAD-BEARING for §W7b-82). The (η=0, GV≠0) signature jointly identifies the parity-twin discrimination —
  η-NULL alone is structurally guaranteed by W-11 STRENGTHENED (whole 4-corner Corner I family is η-NULL);
  GV-NON-NULL alone is generic on any spectral triple; their CONJUNCTION is operationally distinguishing.

**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway. Joint clauses
  H1 (substrate-IS structural identity) + H2 (laboratory-IN signature operational form) require Stage-2
  cross-axis independent-verify at S89+ via `S89-VII-{slot_label}-STAGE-2-INDEPENDENT-VERIFY` (forward-pinned;
  not yet queued — pre-registration of Stage-2 occurs at next `/rclab-plan` for S89).

**Substrate framing** (per `.claude/rules/phononic-framing.md`): The η-invariant IS a substrate-IS observable
  on (A_K^≤10, H_K^≤10, D_K^≤10) — it is NOT a quantity defined IN any container; rather, η is the spectral
  asymmetry that the substrate's eigenvalue distribution carries on its own. The (C_H, C_epsH) parity-twin
  pair are TWO incarnations of the substrate's discrete charge-conjugation/parity action. The W-11 STRENGTHENED
  theorem says: η cannot tell the two incarnations apart, regardless of which regulator R extracts which weight
  kernel from the substrate's KO-dim-6 structure. The lab measurement of η in 3He-B (or BdG / APS) is the
  IN-image; what the substrate IS structurally produces an IDENTICAL η for the two parity-twins. The LEVEL-2
  odd-grading proxy (W7b-82) is the route the lab uses to access the parity discrimination that IS encoded
  in odd-grading cocycles (GV / Cheeger-Simons / η-Cheeger-Simons), not in the even-grading η alone.

**Cross-references**:
- §VII.AF.1 (S87 W5-1): Pillar III ↔ Pillar IV bridge theorem (W-5 calibration; first registered cross-pillar bridge)
- §VII.U.2 (S88 W5b-45): four-corner classification; this slot is the per-corner-I exemplar of even-grading parity-blindness
- §VII.AH (S86 W-9): Joint F_2-Class Path-(c) Theorem (calibration instance #1 of joint-theorem-promotion.md; STAGE-1-CANDIDATE precedent)
- §VII.AN (S88 W5a-37): SOURCE-DOUBLE-CITE-CO-PRIMARY calibration corpus instance #2 of `registry-landing.md` (this slot extends the corpus)
- `.claude/rules/regulator-pin-discipline.md` §"Class-(c) PIN-DRIFT — W-11 Calibration Corpus Extension": W-11 RULE-2 STRENGTHENED parity-blindness (substrate axiom-level identity)
- `.claude/rules/cross-pillar-bridge-anatomy.md`: 5 IS-not-IN anatomy + 3-level structural-confidence ladder
- `.claude/rules/registry-landing.md`: SOURCE-DOUBLE-CITE-CO-PRIMARY (calibration corpus instance #2 advanced here; W-3 RULE-1 precedent)
- `.claude/rules/joint-theorem-promotion.md`: STAGE-1-CANDIDATE → STAGE-3-PERMANENT 4-stage pathway

---
"""
    return block


def main() -> int:
    t_start = time.time()
    import numpy as np

    # ──────────────────────────────────────────────────────────────────
    # 1 — Canonical-constant verification (cross-check W7b-79 numerical pins)
    # ──────────────────────────────────────────────────────────────────
    try:
        cc_gv = abs(gv_canonical_difference_FW - GV_CANONICAL_DIFFERENCE) < 1e-10  # noqa: F405
    except NameError:
        cc_gv = False
    try:
        cc_max_pair = abs(max_pair_ratio_A_5_FW - MAX_PAIR_RATIO_A_5) < 1e-12  # noqa: F405
    except NameError:
        cc_max_pair = False
    try:
        cc_mkk = abs(M_KK - M_KK_GEV) / abs(M_KK_GEV) < 1e-6  # noqa: F405
    except NameError:
        cc_mkk = False
    print(f"[W7b-79] CC-A gv_canonical_difference_FW match -40579.1500479506: {cc_gv}")
    print(f"[W7b-79] CC-B max_pair_ratio_A_5_FW match 9.240438549812e-01:    {cc_max_pair}")
    print(f"[W7b-79] CC-C M_KK match 7.4287e+16 GeV:                          {cc_mkk}")

    # ──────────────────────────────────────────────────────────────────
    # 2 — Pre-write checks: registry readable; allowlist has W7b-79 row
    # ──────────────────────────────────────────────────────────────────
    registry_text_pre = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")
    allowlist_text = ALLOWLIST_PATH.read_text(encoding="utf-8", errors="replace")

    cc_allowlist_w7b79 = (
        "| W7b-79 | S88" in allowlist_text
        and SHA256_OF_PLAN_BLOCK in allowlist_text
    )
    print(f"[W7b-79] CC0 methodology-wave-allowlist W7b-79 row present: {cc_allowlist_w7b79}")

    # Idempotent re-run guard: detect this exact gate's prior landing
    already_landed = "STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE (S88 W7b-79" in registry_text_pre
    print(f"[W7b-79] Idempotent re-run check (block already landed): {already_landed}")

    # ──────────────────────────────────────────────────────────────────
    # 3 — Allocate next-free-letter slot under §VII.A* (parallel-writer rule)
    # ──────────────────────────────────────────────────────────────────
    slot_label = scan_next_free_letter(registry_text_pre)
    rerouted = (slot_label != PLANNED_SLOT)
    print(f"[W7b-79] Planned slot:    §VII.{PLANNED_SLOT}")
    print(f"[W7b-79] Next-free slot:  §VII.{slot_label}")
    print(f"[W7b-79] Slot reroute:    {rerouted} (planned={PLANNED_SLOT}; landed={slot_label})")

    # ──────────────────────────────────────────────────────────────────
    # 4 — Build promotion text (PURE, no I/O)
    # ──────────────────────────────────────────────────────────────────
    promotion_text = build_promotion_text(slot_label, PLANNED_SLOT, audit_sha_placeholder="(emitted at verdict-line append; see s88_gate_verdicts.txt)")

    # ──────────────────────────────────────────────────────────────────
    # 5 — Write append-only with fsync (single-shot AFTER pattern)
    # ──────────────────────────────────────────────────────────────────
    if not already_landed:
        with open(REGISTRY_PATH, "a", encoding="utf-8") as f:
            f.write(promotion_text)
            f.flush()
            os.fsync(f.fileno())
        print(f"[W7b-79] Appended §VII.{slot_label} block to registry ({len(promotion_text)} chars)")
    else:
        print(f"[W7b-79] Idempotent re-run — skipping registry append")

    # ──────────────────────────────────────────────────────────────────
    # 6 — Re-read + verify (final verification — boolean drives verdict)
    # ──────────────────────────────────────────────────────────────────
    registry_text_post = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")

    # Verify all mandatory fields per plan §W7b-79 Method Step 3 (4 grep cross-checks)
    cc1_anchor1 = "ANCHOR-1 (V_input, axiomatic chain): connes-ncg KO-dim 6 + Pf=−1 BDI(J, γ_9) + Connes 1996 reconstruction theorem" in registry_text_post
    cc2_anchor2 = "ANCHOR-2 (C_output, scope-locality): lizzi-spectral 4-corner classification §VII.U.2 (Corner I = even-grading spectrum-only family) + Mellin-cone weight w_n=2n" in registry_text_post
    cc3_structure = "STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY" in registry_text_post
    cc4_chain = "Derivation chain: V_input (KO-dim 6 NCG-axiomatic chain on (A_K, H_K, D_K)) → A_F" in registry_text_post

    # Plan §99-101 grep cross-checks
    section_header_count = registry_text_post.count(f"## §VII.{slot_label} — STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE")
    cc_slot_unique = (section_header_count == 1)

    # All 5 IS-not-IN anatomy elements (cc_anatomy)
    anatomy_keys = [
        "1. Substrate-IS observable: η(D_K) on (A_K^≤10, H_K^≤10, D_K^≤10)",
        "2. Laboratory-IN observable: APS-style η-invariant",
        "3. Bridge map: KO-dim 6 NCG-axiomatic chain ∘ Connes-Karoubi pairing",
        "4. Algebraic envelope: structural-exact",
        "5. Empirical anchor: per-regulator deviation = ZERO",
    ]
    cc_anatomy = all(k in registry_text_post for k in anatomy_keys)

    # All 3 level markers (cc_levels)
    level_keys = [
        "**Level 1 (substrate-IS structural identity)**:",
        "**Level 2 (algebraic envelope)**: NOT APPLICABLE",
        "**Level 3 (empirical anchor)**:",
    ]
    cc_levels = all(k in registry_text_post for k in level_keys)

    # SOURCE-DOUBLE-CITE-CO-PRIMARY tag (cc3 already covers but double-tag-check)
    cc_co_primary_calibration_2 = "calibration corpus instance #2" in registry_text_post

    # gv_canonical_difference_FW literal (Level 3 anchor)
    cc_gv_anchor = "gv_canonical_difference_FW = -40579.1500479506" in registry_text_post
    cc_gv_floor = "gv_spread_FW = 6.257e-10" in registry_text_post

    # OE-form Element 2 (per S88 W7a-73 hardening)
    cc_oe_form = "Tr_{M_2(C)}(P_" in registry_text_post

    # Substrate framing block + container-thinking guard
    cc_substrate_framing = ("Substrate framing" in registry_text_post
                             and "is NOT a quantity defined IN any container" in registry_text_post)

    # STAGE-1-CANDIDATE marker (joint-theorem-promotion.md)
    cc_stage_1_candidate = "STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md`" in registry_text_post

    print(f"[W7b-79] CC1 ANCHOR-1 (V_input KO-dim 6 + Connes 1996):       {cc1_anchor1}")
    print(f"[W7b-79] CC2 ANCHOR-2 (C_output 4-corner Corner I + w_n=2n):  {cc2_anchor2}")
    print(f"[W7b-79] CC3 STRUCTURE SOURCE-DOUBLE-CITE-CO-PRIMARY:         {cc3_structure}")
    print(f"[W7b-79] CC4 Derivation chain V_input → A_F → C_output:       {cc4_chain}")
    print(f"[W7b-79] CC5 §VII.{slot_label} unique header (not parallel-writer race): {cc_slot_unique}")
    print(f"[W7b-79] CC6 5 IS-not-IN anatomy elements present:            {cc_anatomy}")
    print(f"[W7b-79] CC7 3 level markers present (L1/L2/L3):              {cc_levels}")
    print(f"[W7b-79] CC8 calibration corpus instance #2 marker:           {cc_co_primary_calibration_2}")
    print(f"[W7b-79] CC9 gv_canonical_difference_FW = -40579.1500479506:  {cc_gv_anchor}")
    print(f"[W7b-79] CC10 gv_spread_FW = 6.257e-10 publication floor:     {cc_gv_floor}")
    print(f"[W7b-79] CC11 Element 2 OE-form Tr_{{M_2(C)}}(P_eta-...):       {cc_oe_form}")
    print(f"[W7b-79] CC12 Substrate framing + container-thinking guard:   {cc_substrate_framing}")
    print(f"[W7b-79] CC13 STAGE-1-CANDIDATE joint-theorem-promotion.md:   {cc_stage_1_candidate}")

    # Body line count
    sub_row_line_count = count_section_lines(
        REGISTRY_PATH,
        f"## §VII.{slot_label} — STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE",
        "---\n",
    )
    cc_line_count = (sub_row_line_count >= LINE_THRESHOLD_PASS)
    print(f"[W7b-79] §VII.{slot_label} body line count: {sub_row_line_count} (threshold ≥{LINE_THRESHOLD_PASS}): {cc_line_count}")

    # ──────────────────────────────────────────────────────────────────
    # 7 — Composite verdict (deterministic, pre-registered)
    # ──────────────────────────────────────────────────────────────────
    structural_pass_predicates = (
        cc1_anchor1 and cc2_anchor2 and cc3_structure and cc4_chain
        and cc_slot_unique and cc_anatomy and cc_levels
        and cc_co_primary_calibration_2
        and cc_gv_anchor and cc_gv_floor and cc_oe_form
        and cc_substrate_framing and cc_stage_1_candidate
        and cc_allowlist_w7b79
        and cc_line_count
    )

    # Per `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` item 3
    # (binding rule, outranks per-session plan): slot reroute → FAIL-with-remediation,
    # NOT PASS, NOT INFO. Composite is FAIL when rerouted, even if all structural
    # cross-checks pass at the rerouted slot. Math content is preserved at the
    # next-free-letter; the verdict line documents the reroute as the audit-trail-
    # visibility marker per S84 W2a-11 §VII.M→§VII.N precedent.
    if rerouted:
        composite = "FAIL"
        verdict_kind = (
            f"FAIL-with-remediation-vii-{PLANNED_SLOT}-rerouted-to-{slot_label}-"
            f"per-registry-write-hygiene-rule-item-3-math-content-preserved"
        )
    elif structural_pass_predicates:
        composite = "PASS"
        verdict_kind = f"PASS-vii-{slot_label}-structural-even-grading-blindness-corner-I-landed"
    elif sub_row_line_count >= 10:
        composite = "INFO"
        verdict_kind = f"INFO-vii-{slot_label}-partial-landing-cross-checks-failed"
    else:
        composite = "FAIL"
        verdict_kind = f"FAIL-vii-{slot_label}-block-incomplete"

    print(f"[W7b-79] structural_pass_predicates (all 14 CCs):  {structural_pass_predicates}")
    print(f"[W7b-79] rerouted (slot != planned):               {rerouted}")
    print(f"[W7b-79] composite verdict:                         {composite}")
    print(f"[W7b-79] verdict_kind:                              {verdict_kind}")

    # ──────────────────────────────────────────────────────────────────
    # 8 — Compute SHAs (input pin map + content_sha256 = script_sha)
    # ──────────────────────────────────────────────────────────────────
    canon_sha = sha256_file(CANON_PY)
    registry_sha_post = sha256_file(REGISTRY_PATH)
    allowlist_sha = sha256_file(ALLOWLIST_PATH)
    rule_landing_sha = sha256_file(RULE_REGISTRY_LANDING)
    rule_anatomy_sha = sha256_file(RULE_BRIDGE_ANATOMY)
    rule_regulator_sha = sha256_file(RULE_REGULATOR_PIN)
    rule_joint_sha = sha256_file(RULE_JOINT_THEOREM)
    plan_sha = sha256_file(PLAN_PATH)
    s86_verdicts_sha = sha256_file(S86_VERDICTS)
    spectrum_cache_sha = sha256_file(SPECTRUM_CACHE)
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha

    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "wp_id": "session-88-w7b-workingpaper.md",
        "planned_slot": PLANNED_SLOT,
        "landed_slot": slot_label,
        "rerouted": rerouted,
        "sha256_of_plan_block": SHA256_OF_PLAN_BLOCK,
        "gv_canonical_difference_FW": str(GV_CANONICAL_DIFFERENCE),
        "gv_spread_FW_floor": str(GV_SPREAD_PUBLICATION_FLOOR),
        "max_pair_ratio_A_5_FW": str(MAX_PAIR_RATIO_A_5),
        "M_KK_GeV": str(M_KK_GEV),
        "A_5_extended": list(A_5_EXTENDED),
        "LINE_THRESHOLD_PASS": LINE_THRESHOLD_PASS,
        "input_canonical_constants_sha256": canon_sha,
        "input_registry_sha256_post": registry_sha_post,
        "input_allowlist_sha256": allowlist_sha,
        "input_rule_registry_landing_sha256": rule_landing_sha,
        "input_rule_bridge_anatomy_sha256": rule_anatomy_sha,
        "input_rule_regulator_pin_sha256": rule_regulator_sha,
        "input_rule_joint_theorem_sha256": rule_joint_sha,
        "input_plan_sha256": plan_sha,
        "input_s86_verdicts_sha256": s86_verdicts_sha,
        "input_spectrum_cache_sha256": spectrum_cache_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    # ──────────────────────────────────────────────────────────────────
    # 9 — Save .npz
    # ──────────────────────────────────────────────────────────────────
    np.savez(
        NPZ_OUT,
        slot_label=slot_label,
        planned_slot=PLANNED_SLOT,
        rerouted=np.bool_(rerouted),
        sub_row_line_count=np.int64(sub_row_line_count),
        cc1_anchor1=np.bool_(cc1_anchor1),
        cc2_anchor2=np.bool_(cc2_anchor2),
        cc3_structure=np.bool_(cc3_structure),
        cc4_chain=np.bool_(cc4_chain),
        cc_slot_unique=np.bool_(cc_slot_unique),
        cc_anatomy=np.bool_(cc_anatomy),
        cc_levels=np.bool_(cc_levels),
        cc_co_primary_calibration_2=np.bool_(cc_co_primary_calibration_2),
        cc_gv_anchor=np.bool_(cc_gv_anchor),
        cc_gv_floor=np.bool_(cc_gv_floor),
        cc_oe_form=np.bool_(cc_oe_form),
        cc_substrate_framing=np.bool_(cc_substrate_framing),
        cc_stage_1_candidate=np.bool_(cc_stage_1_candidate),
        cc_allowlist_w7b79=np.bool_(cc_allowlist_w7b79),
        cc_line_count=np.bool_(cc_line_count),
        cc_gv=np.bool_(cc_gv),
        cc_max_pair=np.bool_(cc_max_pair),
        cc_mkk=np.bool_(cc_mkk),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )
    print(f"[W7b-79] NPZ saved: {NPZ_OUT.name}")

    # ──────────────────────────────────────────────────────────────────
    # 10 — Append verdict line (canonical + companion + 3-tuple)
    # ──────────────────────────────────────────────────────────────────
    elapsed = time.time() - t_start
    value_str = (
        f"slot=§VII.{slot_label};planned_slot=§VII.{PLANNED_SLOT};"
        f"rerouted={rerouted};"
        f"sub_row_line_count={sub_row_line_count};"
        f"cc1_anchor1={cc1_anchor1};cc2_anchor2={cc2_anchor2};"
        f"cc3_structure={cc3_structure};cc4_chain={cc4_chain};"
        f"cc_slot_unique={cc_slot_unique};cc_anatomy={cc_anatomy};"
        f"cc_levels={cc_levels};cc_co_primary_calibration_2={cc_co_primary_calibration_2};"
        f"cc_gv_anchor={cc_gv_anchor};cc_gv_floor={cc_gv_floor};"
        f"cc_oe_form={cc_oe_form};cc_substrate_framing={cc_substrate_framing};"
        f"cc_stage_1_candidate={cc_stage_1_candidate};"
        f"cc_allowlist_w7b79={cc_allowlist_w7b79};cc_line_count={cc_line_count};"
        f"verdict_kind={verdict_kind}"
    )
    convention_tag = (
        "registry-edit-rerouted-AK-to-AQ-stage-1-candidate"
        if rerouted else
        CONVENTION
    )
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={convention_tag} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S87+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    # 3-tuple: METHODOLOGY-class with directional reroute claim → sign=N/A,
    # magnitude=FAIL (slot mismatch) when rerouted, regime=VALID (registry-landing
    # operational regime is preserved; math content lands correctly at next-free)
    sign_v = "N/A"  # (local) METHODOLOGY-class — no numerical sign claim
    mag_v = "FAIL" if rerouted else composite
    regime_v = "VALID"
    tuple_line = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_line)
        f.write(tuple_line)

    print(f"[W7b-79] DONE in {elapsed:.2f}s")
    print(f"[W7b-79] composite       = {composite} (verdict_kind={verdict_kind})")
    print(f"[W7b-79] slot            = §VII.{slot_label} (planned §VII.{PLANNED_SLOT})")
    print(f"[W7b-79] audit_sha256    = {audit_sha256}")
    print(f"[W7b-79] content_sha256  = {content_sha256}")
    print(f"[W7b-79] sha256_of_plan_block (allowlist pin) = {SHA256_OF_PLAN_BLOCK}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
