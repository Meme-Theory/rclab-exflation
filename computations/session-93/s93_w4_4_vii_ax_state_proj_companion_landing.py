#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93-W4-4-VII-AX-STATE-PROJ-COMPANION-LANDING
============================================

Lands a NEW §VII.AX.STATE-PROJ section in
`sessions/permanent-results-registry.md` as a STRUCTURAL-ORTHOGONAL-COMPANION
to §VII.AX.OP-PROJ (the PBH band-edge prediction n_PBH = 7.2761e-23 m⁻³).

  - §VII.AX.OP-PROJ    (Cell I  ; algebra-INVARIANT spectrum-only cardinality
                        functional n_PBH = n_edge_saturated · prob_form / L_pix_LRD³;
                        operator-projection on the cardinality-cascade-tail;
                        EXISTING entry; STAGE-3-PERMANENT-ELIGIBLE this wave)
  - §VII.AX.STATE-PROJ (Cell IV ; algebra-DEPENDENT state-pair occupation
                        functional ⟨ψ_GGE-PBH|n_a^PBH|ψ_GGE-PBH⟩ on a
                        GGE-state-prepared PBH population at τ_fold=0.190
                        saturated cascade-tail; Leggett-channel inter-band
                        coherence; THIS landing)

declared STRUCTURAL-ORTHOGONAL-COMPANION (NOT SOURCE-DOUBLE-CITE-CO-PRIMARY:
cross-corner co-primary is STRUCTURALLY FORBIDDEN per the algebra-axis
orthogonality K=3 MANDATORY clause — the two sub-slots live on ORTHOGONAL
algebra-axis cells, Cell I ≠ Cell IV, and CANNOT be co-primary anchors of one
theorem; `registry-landing.md §"Detection"` criterion (4) requires both
co-primary anchors on the SAME algebra-axis cell).

CHAIN PREREQUISITE — §VII.AX.OP-PROJ STAGE-3-PERMANENT ELIGIBILITY
-----------------------------------------------------------------
This is a CHAINED gate. Eligibility = (a) ∧ (b) ∧ (c):
  (a) S93 W4-1 Axis-A E2 verdict-artifact re-emission PASS
      (axis_a_composite=PASS; `computations/session-93/s93_gate_verdicts.txt:67`
       audit_sha256=2ab8bb1ecccb1bb7da8f85250b92ba4b25f2d7476253a4f5b2cb9703d79d29e8).
  (b) S92 W-4 JE5 PASS at central-value (Axis-B; the prior Axis-B FAIL
      RETIRED-NOT-OVERTURNED via Option-A; JE5 flips PASS once Eq.(2′) lands).
  (c) Eq.(2′) registry-text correction LANDED on §VII.AX.OP-PROJ (the
      internally-inconsistent conjunctive band-containment Level-3 statement
      corrected to the central-value PASS reading + Friedrich-Bär
      truncation-resolution annotation; per `cross-pillar-bridge-anatomy.md
      §"Registry-PASS criterion"` Level-3 annotation discipline §20).

The script CONFIRMS all three conjuncts on disk before landing the companion:
  (a) grep the W4-1 PASS line in s93_gate_verdicts.txt (non-superseded);
  (b) grep the S92 W-4 JE5 CONVERGED verdict in session-92-mack-synthesis.md
      (the workshop-verdict record);
  (c) re-run the Class-(i) detector predicate on the §VII.AX.OP-PROJ block —
      Eq.(2′) is landed IFF the block no longer fires
      INTERNALLY-INCONSISTENT-LEVEL-3-BAND-STATEMENT.
If any conjunct is unmet → honest mechanical closure per
`mechanical-closure-discipline.md` (value='PRE-REG-INC_blocked_by_VII_AX_OP_PROJ
_STAGE_3_eligibility_<status>'; FAIL, NEVER forced PASS).

METHODOLOGY/PHONONIC-boundary registry-landing gate. mack-cosmic-bridge is the
SOLE registry writer per `feedback_mack-bridge-role.md`. connes-ncg-theorist is
CO-SIGNER on the Cell-IV algebra-axis classification (the parse-tree decision
procedure §VII.U.2 clause (e)). The script reads NO D_K eigenvalues — it lands a
registry section and records the Cell-IV state-pair classification.

Single-shot bridge-landing AFTER pattern per
`registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"`
+ `computations/_bridge_landing_script_template.py`:
    build_promotion_text  ->  write_atomic_with_fsync  ->
    re_read + verify_section_matches  ->  emit-ONCE
No conditional rewrite / re-emit. A verify-FAIL emits FAIL once and the gate
closes honestly per `mechanical-closure-discipline.md`.

Verdict: [VERIFY] (artifact-existence + Cell-IV classification predicate; no
[SIGN] 3-tuple — §W4-4 pre-registers no directional prediction). Dual-SHA
closure: content_sha256 over the landed §VII.AX.STATE-PROJ section text;
audit_sha256 over the input-pin map + the OP-PROJ T1.13 anchor SHA + the
W4-1 Axis-A PASS SHA + per-gate identity keys.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import re
import sys
from pathlib import Path

# --- canonical constants (mandatory per .claude/rules/math-scripts.md S34+) ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import M_KK, tau_fold  # noqa: F401, E402

# Class-(i) detector predicate is the Eq.(2′)-landed precondition oracle.
from _registry_landing_audit import (  # noqa: E402
    detect_class_i_internally_inconsistent_level_3_band,
    extract_registry_block_anylevel,
)

# ---------------------------------------------------------------------------
# Gate identity + canonical paths
# ---------------------------------------------------------------------------
GATE_ID = "S93-W4-4-VII-AX-STATE-PROJ-COMPANION-LANDING"  # (local)
SCHEME = "vii-ax-state-proj-companion-landing-cell-iv-state-pair-functional"  # (local)
CONVENTION = (  # (local)
    "single-shot-AFTER-pattern-bridge-landing-STRUCTURAL-ORTHOGONAL-COMPANION-"
    "not-cross-corner-co-primary"
)
L_MAX = "14"  # (local) STATE-PROJ Level-3 anchor inherited from OP-PROJ T1.13 at L_max=14

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICT_TXT = (  # (local) canonical per gate-verdicts.md §"Canonical Verdict-File Path"
    PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"
)
NPZ_PATH = (  # (local)
    PROJECT_ROOT / "computations" / "session-93"
    / "s93_w4_4_vii_ax_state_proj_companion_landing.npz"
)
JSON_PATH = (  # (local)
    PROJECT_ROOT / "computations" / "session-93"
    / "s93_w4_4_vii_ax_state_proj_companion_landing.json"
)
S93_VERDICT_TXT = VERDICT_TXT  # (local) W4-1 Axis-A PASS lives here
S92_MACK_SYNTHESIS = (  # (local) S92 W-4 JE5 CONVERGED workshop-verdict record
    PROJECT_ROOT / "sessions" / "session-92" / "session-92-mack-synthesis.md"
)
SLOT_LOCKFILE = (  # (local) W0-1 cross-wave lockfile
    PROJECT_ROOT / "sessions" / "framework" / "s93-slot-pre-allocation-lockfile.md"
)

# --- eligibility-conjunct SHAs (full-64-hex; cited VERBATIM) ---
W4_1_AXIS_A_AUDIT_SHA = (  # (local) S93 W4-1 Axis-A E2 re-emission PASS (conjunct a)
    "2ab8bb1ecccb1bb7da8f85250b92ba4b25f2d7476253a4f5b2cb9703d79d29e8"
)
W4_1_GATE = "S93-W4-1-VII-AX-OP-PROJ-AXIS-A-E2-VERDICT-ARTIFACT-RE-EMISSION"  # (local)
T1_13_AUDIT_SHA = (  # (local) S91 W5-3 T1.13 PASS — the OP-PROJ Level-3 anchor source
    "1dc0a3feb214d8b52ce7d70854b2510bbfa3df0e531e75dda1f8bf0cbbcb50ce"
)
T1_13_GATE = "S91-CF41-UPPER-22.6-EXTENSION"  # (local)

# --- substrate-IS anchors ---
# Element-5 anchor INHERITED from §VII.AX.OP-PROJ T1.13 via a Bogoliubov-state
# closed-form (the state-projection reading and the operator-projection reading
# AGREE on the n_PBH magnitude anchor but differ in algebra-axis identity-class).
N_PBH_FW_CENTRAL = 7.2761e-23  # (local) m^-3; OP-PROJ T1.13 central anchor (L_max=14)
CONJUNCT_LO = 5.5e-23  # (local) m^-3 upper-22.6%-conjunct floor
CONJUNCT_HI = 2.2e-22  # (local) m^-3 upper-22.6%-conjunct ceiling

# --- OP-PROJ companion slot the STATE-PROJ entry is structural-orthogonal to ---
OP_PROJ_SLOT = "§VII.AX.OP-PROJ"  # (local)
STATE_PROJ_SLOT = "§VII.AX.STATE-PROJ"  # (local)

# Insertion boundary: the NEW §VII.AX.STATE-PROJ section lands immediately AFTER
# the existing §VII.AX.OP-PROJ block (which ends at the §VII.AX.MULTI-PIN-ATLAS
# header). The MULTI-PIN-ATLAS header is the next-section marker.
OP_PROJ_HEADER_PREFIX = (  # (local) the EXISTING §VII.AX.OP-PROJ header line prefix
    "### §VII.AX.OP-PROJ — PBH Band-Edge Prediction n_PBH = 7.276e-23 m⁻³"
)
MULTI_PIN_ATLAS_HEADER_PREFIX = (  # (local) the next §VII.AX section (insertion boundary)
    "### §VII.AX.MULTI-PIN-ATLAS — Substrate-Distance-2 Pole s=4 χ' Restriction"
)
STATE_PROJ_HEADER = (  # (local) the NEW section header (exact, matched on verify)
    "### §VII.AX.STATE-PROJ — Cell-IV State-Pair PBH Occupation Functional "
    "⟨ψ_GGE-PBH|n_a^PBH|ψ_GGE-PBH⟩"
)

# Input-pin map (source documents the landing consumes; SHAs feed audit_sha256).
INPUT_FILES = [  # (local)
    REGISTRY_PATH,
    S93_VERDICT_TXT,
    S92_MACK_SYNTHESIS,
    SLOT_LOCKFILE,
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md",
    PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md",
]


# ---------------------------------------------------------------------------
# SHA helpers (canonical dual-SHA per the S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(section_text: str, pins: dict[str, str]) -> tuple[str, str]:
    """Dual-SHA per gate-verdicts.md + wave-classification.md §"Dual-SHA closure".

    content_sha256 = SHA-256 over the landed §VII.AX.STATE-PROJ section text.
    audit_sha256   = SHA-256 over the input-pin map + the OP-PROJ T1.13 anchor SHA
                     + the W4-1 Axis-A PASS SHA + the Element-5 anchor value +
                     per-gate identity keys (so audit_sha256 is gate-distinct per
                     mechanical-closure-discipline item 3).
    """
    h_content = hashlib.sha256()  # (local)
    h_content.update(section_text.encode("utf-8"))
    content = h_content.hexdigest()  # (local)

    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    # The companion landing is licensed by the eligibility chain + the inherited
    # anchor; these are part of the canonical input set.
    h_audit.update(
        f"{W4_1_AXIS_A_AUDIT_SHA}|{T1_13_AUDIT_SHA}|{N_PBH_FW_CENTRAL!r}".encode(
            "utf-8"
        )
    )
    # per-gate identity keys embedded so audit_sha256 is gate-distinct
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}|{L_MAX}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Eligibility-chain confirmation (the CHAINED prerequisite)
# ---------------------------------------------------------------------------
def _latest_nonsuperseded_line(verdict_txt: Path, gate_id: str) -> str | None:
    """Latest NON-SUPERSEDED canonical line for a gate-ID (Option-A reading)."""
    if not verdict_txt.exists():
        return None
    superseded: set[str] = set()  # (local)
    lines: list[tuple[str, str]] = []  # (local) (audit_sha, full_line)
    for ln in verdict_txt.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{gate_id}:") and "audit_sha256=" in ln:
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                lines.append((m.group(1), ln))
            sm = re.search(r"supersedes=([a-f0-9]{64})", ln)  # (local)
            if sm:
                superseded.add(sm.group(1))
    live = [(a, ln) for (a, ln) in lines if a not in superseded]  # (local)
    return live[-1][1] if live else None


def confirm_eligibility() -> dict:
    """Confirm §VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility = (a) ∧ (b) ∧ (c)."""
    out = {  # (local)
        "conjunct_a_w4_1_axis_a_pass": False,
        "conjunct_a_audit_sha_match": False,
        "conjunct_b_s92_w4_je5_converged": False,
        "conjunct_c_eq2prime_landed": False,
        "class_i_diagnostic": None,
        "eligibility_achieved": False,
    }

    # (a) W4-1 Axis-A E2 re-emission PASS (latest non-superseded line, axis_a_composite=PASS).
    w4_1_line = _latest_nonsuperseded_line(S93_VERDICT_TXT, W4_1_GATE)  # (local)
    if w4_1_line is not None:
        out["conjunct_a_w4_1_axis_a_pass"] = (
            w4_1_line.startswith(f"{W4_1_GATE}: PASS")
            and "axis_a_composite=PASS" in w4_1_line
            and "emit_bug_confirmed=True" in w4_1_line
        )
        out["conjunct_a_audit_sha_match"] = W4_1_AXIS_A_AUDIT_SHA in w4_1_line

    # (b) S92 W-4 JE5 CONVERGED (the central-value-governs verdict record).
    if S92_MACK_SYNTHESIS.exists():
        syn = S92_MACK_SYNTHESIS.read_text(encoding="utf-8", errors="ignore")  # (local)
        # The mack-synthesis §V.1 / W-4 row records JE5=PASS central-value (NOT
        # literal-conjunctive); "both edges inside" = false sentence → Eq.(2′).
        out["conjunct_b_s92_w4_je5_converged"] = bool(
            re.search(r"Central-value governs", syn)
            and "JE5" in syn
            and re.search(r"Eq\.\s*\(?2['′]\)?", syn)
        )

    # (c) Eq.(2′) landed ⇔ the §VII.AX.OP-PROJ block no longer fires Class-(i).
    reg_text = REGISTRY_PATH.read_text(encoding="utf-8", errors="ignore")  # (local)
    op_block = extract_registry_block_anylevel(reg_text, OP_PROJ_SLOT)  # (local)
    if op_block:
        ci = detect_class_i_internally_inconsistent_level_3_band(op_block, OP_PROJ_SLOT)  # (local)
        out["class_i_diagnostic"] = ci["diagnostic"]
        # Eq.(2′) landed iff the block is NOT internally inconsistent. Both
        # 'no_band_containment_claim_present' and a self-consistent 'PASS' are
        # Eq.(2′)-landed states; only the INTERNALLY-INCONSISTENT flag is the
        # NOT-landed state.
        out["conjunct_c_eq2prime_landed"] = not ci["has_class_i_flag"]

    out["eligibility_achieved"] = bool(
        out["conjunct_a_w4_1_axis_a_pass"]
        and out["conjunct_a_audit_sha_match"]
        and out["conjunct_b_s92_w4_je5_converged"]
        and out["conjunct_c_eq2prime_landed"]
    )
    return out


# ---------------------------------------------------------------------------
# Slot-lockfile pre-condition (RESERVATION confirmation; advisory — not HARD)
# ---------------------------------------------------------------------------
def confirm_slot_documented() -> bool:
    """Confirm the S93 slot lockfile DOCUMENTS the §VII.AX.STATE-PROJ companion.

    §VII.AX.STATE-PROJ is a NEW suffix-named Cell-IV companion (NOT a next-free
    LETTER allocation, so it does not collide with the 7 pre-reserved colliding
    STAGE-3-flip letter-slots). The lockfile's §VII.AX RESERVED-FOR block
    (RESERVED-FOR-S93-W4-2-VII-AX-MULTI-PIN-ATLAS-...) explicitly documents that
    "A SEPARATE W4-4 lands a NEW §VII.AX.STATE-PROJ companion (Cell IV) ... those
    are distinct slots." Confirm that documentation is present.
    """
    if not SLOT_LOCKFILE.exists():
        return False
    txt = SLOT_LOCKFILE.read_text(encoding="utf-8")  # (local)
    return bool(
        "§VII.AX.STATE-PROJ" in txt
        and "W4-4" in txt
        and "distinct slots" in txt
    )


# ---------------------------------------------------------------------------
# Step (1) — build_promotion_text  (pure function; no I/O)
# ---------------------------------------------------------------------------
def build_promotion_text() -> str:
    """The NEW §VII.AX.STATE-PROJ companion section. Pure; no I/O.

    5 IS-not-IN anatomy elements + 3-level ladder + parse-tree expansion + Cell-IV
    classification + STRUCTURAL-ORTHOGONAL-COMPANION declaration (NOT cross-corner
    co-primary). Element 5 INHERITED from §VII.AX.OP-PROJ T1.13 via a
    Bogoliubov-state closed-form. Direction: substrate-IS → bridge → laboratory-IN
    per phononic-framing.md.
    """
    return f"""{STATE_PROJ_HEADER} (S93 W4-4 — STRUCTURAL-ORTHOGONAL-COMPANION to §VII.AX.OP-PROJ; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`; connes-ncg-theorist CO-SIGNER on the Cell-IV algebra-axis classification, 2026-05-24)

> **Provenance**: S93 W4-4 `{GATE_ID}` (mack-cosmic-bridge sole registry writer per `feedback_mack-bridge-role.md` AMRI-PROMOTED 2026-04-28; connes-ncg-theorist CO-SIGNER on the Cell-IV parse-tree classification per `permanent-results-registry.md §VII.U.2` clause (e)). This is the **state-projection companion** to §VII.AX.OP-PROJ (the operator-projection PBH band-edge prediction n_PBH = 7.2761e-23 m⁻³). CHAINED on §VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility = (a) S93 W4-1 Axis-A E2 re-emission PASS (audit_sha256=`{W4_1_AXIS_A_AUDIT_SHA}`) ∧ (b) S92 W-4 JE5 PASS at central-value (Axis-B) ∧ (c) Eq.(2′) registry-text correction LANDED (the central-value PASS reading; internally-inconsistent conjunctive band-containment statement corrected). Single-shot AFTER-pattern per `registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"`.

**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md §"Stage 1"` 4-stage pathway (this companion-landing names the Cell-IV state-projection reading; its own Stage-2 cross-axis independent-verify is an S94+ carry-forward `CF-S94-W4-STAGE-2-VII-AX-STATE-PROJ-CROSS-AXIS-VERIFY`). The §VII.AX.OP-PROJ operator-projection companion is STAGE-3-PERMANENT-ELIGIBLE this wave; this STATE-PROJ entry is its algebra-axis-orthogonal companion at Cell IV. **EXCLUDED reviewers** at Stage-2: mack-cosmic-bridge (sole-writer at this landing).

**Naming-hygiene suffix** (per `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 since S88 W8-92): this slot carries the `.STATE-PROJ` suffix because it is a **state-projection** observable — a state-pair occupation functional on a GGE-state-prepared PBH population (the algebra-DEPENDENT family). Its operator-projection companion §VII.AX.OP-PROJ carries the `.OP-PROJ` suffix (the algebra-INVARIANT cardinality observable). Bare `§VII.AX` (no suffix) is FORBIDDEN now that both projection-side readings are independently registry-eligible.

**Corner-cell**: **Cell IV** (algebra-DEPENDENT state-pair functional × cardinality-cascade-pole) per `permanent-results-registry.md §VII.U.2` 4-corner classification (LANDED S88 W5b-45 MANDATORY at K=3). The PBH occupation functional `⟨ψ_GGE-PBH|n_a^PBH|ψ_GGE-PBH⟩` is a state-pair expectation value on a Leggett-channel GGE-state-prepared PBH population; it is NOT fixed by the algebra alone (it depends on the prepared state `|ψ_GGE-PBH⟩`), so its parse-tree terminus is a state-pair expectation `⟨ψ|·|ψ⟩`, which FORCES the Cell-IV classification per `cross-pillar-bridge-anatomy.md §"Observable-Naming-History vs Parse-Tree-Structure"`. This is STRUCTURALLY ORTHOGONAL to the §VII.AX.OP-PROJ Cell-I cardinality observable `n_edge_saturated · prob_form / L_pix_LRD³` (whose parse-tree terminus is the spectrum-only cardinality `C(N_eigs, 2)` — a `Tr`/count, NOT a state-pair functional).

**Parse-tree expansion** (per `registry-landing.md §"Parse-Tree Expansion Pre-Registration for new §VII entries"` SUGGESTION-K=1):

```
n_a^PBH = ⟨ψ_GGE-PBH | n_a^PBH | ψ_GGE-PBH⟩

  [Step 1: history-label form]
    n_a^PBH-GGE = observable named by 'Leggett-channel occupation of the
    saturated-cascade-tail PBH population prepared in the GGE state |ψ_GGE-PBH⟩'
    (Pillar IX laboratory-IN cosmological-cascade preparation history).

  [Step 2: Bogoliubov-state substitution on the BdG sub-algebra M_2(ℂ) ⊂ A_K]
    n_a^PBH = ⟨ψ_GGE-PBH | b_a^† b_a | ψ_GGE-PBH⟩ = |v_a|²
    where (u_a, v_a) is the canonical S52 8-mode Bogoliubov amplitude pair on
    the BdG sub-algebra M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ), and |ψ_GGE-PBH⟩ is the
    GGE-state-prepared occupation at τ_fold = 0.190 in the saturated regime
    (g_BBN ≥ g_saturate = 143). The expectation value is a STATE-PAIR functional
    on A (it carries the prepared-state index a; it is NOT a spectrum-only
    functional of {{λ_k, m_k}}).

  [Step 3: aggregation to the population number density]
    n_PBH^STATE = (Σ_a |v_a|²) · prob_form / L_pix_LRD³
    Aggregating the per-mode occupations |v_a|² over the saturated cascade-tail
    GGE state recovers the SAME magnitude anchor as the OP-PROJ cardinality
    reading (n_PBH = 7.2761e-23 m⁻³ at L_max=14) — the two readings AGREE on the
    n_PBH magnitude but differ in algebra-axis IDENTITY-CLASS (Cell IV state-pair
    vs Cell I spectrum-only). This is the Element-5 INHERITANCE from §VII.AX.OP-PROJ
    T1.13 via a Bogoliubov-state closed-form.

  [Step 4: corner classification]
    Parse-tree counters return (state_pair_count = 1, algebra_dep_count = 1) on
    the Step-2 form (the ⟨ψ|·|ψ⟩ expectation carries the prepared-state index a;
    it is a state-pair expectation, NOT a spectrum-only Tr).
    Classification: Cell IV (algebra-DEPENDENT state-pair functional ×
    cardinality-cascade-pole).
```

The naïve-parse failure mode (reading the SHARED magnitude anchor 7.2761e-23 as forcing a SHARED algebra-axis cell with OP-PROJ) is foreclosed by the parse-tree reduction: the OP-PROJ reading terminates in a spectrum-only cardinality `C(N_eigs, 2)` (Cell I), the STATE-PROJ reading terminates in a state-pair expectation `⟨ψ|n_a^PBH|ψ⟩ = |v_a|²` (Cell IV). **Magnitude agreement does NOT imply algebra-axis identity** — the two readings are STRUCTURAL-ORTHOGONAL-COMPANIONS, not co-primary anchors of one theorem.

**Three-level structural-confidence ladder** (per `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"`):

| Level | Anatomy | Status |
|:------|:--------|:-------|
| Level 1 | Single-τ-slice substrate-IS state-pair identity at τ_fold = 0.190: the PBH occupation functional `⟨ψ_GGE-PBH|n_a^PBH|ψ_GGE-PBH⟩ = |v_a|²` on the BdG sub-algebra `M_2(ℂ) ⊂ A_K`, at the saturated cascade-tail (g_BBN ≥ g_saturate = 143). Regulator-INVARIANT (IR-self-regularized by the BdG gap `|Δ_a|` per `cross-pillar-bridge-corpus.md §22` regulator-behavior sibling discriminator — the algebra-DEPENDENT state-pair family is regulator-INVARIANT, in contrast to the OP-PROJ algebra-INVARIANT spectrum-only family which is regulator-DEPENDENT). | STRUCTURAL THEOREM (state-pair occupation closed-form on the canonical S52 8-mode Bogoliubov amplitudes) |
| Level 2 | Algebraic convergence envelope `L^{{-α}}` via the Bogoliubov-state closed-form; **Level-2-binding sub-class** per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"` — the HKR-style image of the state-pair occupation functional BINDS Level-1 to the Pillar IX continuum PBH population observation. Structural-exact replacement: Friedrich-Bär saturation theorem certifies the bottom-K Bogoliubov amplitudes for all L_max ≥ 12 (the state-pair occupation is a bottom-K-supported observable, distinct from the OP-PROJ N_eigs total-count channel — see the §VII.AX.OP-PROJ canonical-truncation note). | STRUCTURAL PREDICTION (Level-2-binding; bottom-K Bogoliubov-amplitude saturation) |
| Level 3 | Empirical anchor at canonical L_max=14: `n_PBH^STATE(L_max=14) = 7.2761e-23 m⁻³` — INHERITED from §VII.AX.OP-PROJ T1.13 via the Bogoliubov-state closed-form (`Σ_a |v_a|² · prob_form / L_pix_LRD³`); the central SINGLE-VALUE anchor lands INSIDE the upper-22.6%-conjunct sub-band [{CONJUNCT_LO:.1e}, {CONJUNCT_HI:.1e}] m⁻³ (the Registry-PASS criterion per `cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`). rel_tol ≥ 1e-4 against the OP-PROJ T1.13 anchor (publication-precision floor, 5 sig figs). | EMPIRICAL CONFIRMATION (inherited from OP-PROJ T1.13 PASS; audit_sha256=`{T1_13_AUDIT_SHA}`) |

**Registry-PASS criterion** (per `cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`): the Level-3 central SINGLE-VALUE anchor `n_PBH^STATE = 7.2761e-23 m⁻³` satisfies the Level-2 envelope at canonical L_max=14 (it lands inside the upper-22.6%-conjunct, the SAME central-value criterion the OP-PROJ companion satisfies under Eq.(2′)). Level-2-binding sub-class verified (HKR-style image of the state-pair occupation functional binds Level-1 to Pillar IX). No band-containment gate is asserted (per the §20 Level-3 annotation discipline — descriptive 1σ-band statements are non-load-bearing annotations).

**IS-not-IN anatomy** (5 elements; MANDATORY at K=3 per `cross-pillar-bridge-anatomy.md §"Forward template-adoption"`):

1. **Substrate-IS observable**: the PBH occupation functional `n_a^PBH = ⟨ψ_GGE-PBH|n_a^PBH|ψ_GGE-PBH⟩ = |v_a|²` on the BdG sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`, evaluated on the finite spectral triple `(A_K^{{≤14}}, H_K^{{≤14}}, D_K^{{≤14}})` at τ_fold = 0.190 in the saturated cascade-tail regime (g_BBN ≥ g_saturate = 143). **EXPLICIT TAG: Level 1 single-τ-slice at τ_fold = 0.190** (MANDATORY per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`). Algebra-DEPENDENT (state-pair functional; carries the prepared-state index a).
2. **Laboratory-IN observable** (OE-form MANDATORY at K=2 per `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"`): `∫_{{Σ_CMB ∪ Σ_LISA ∪ Σ_PTA}} d³x · Tr_{{M_2(ℂ)}}(P_BdG · ρ_BH-occ(x))` — PBH population occupation-density continuum measurement across the combined CMB / LISA / PTA detection-horizon hypersurface, with the BdG-sector projector `P_BdG` selecting the Leggett-channel occupation on `M_2(ℂ) ⊂ A_obs`; trace over the BdG sub-algebra `M_2(ℂ)`; integration over the combined detection-horizon hypersurface in the FRW container. Lab measures this occupation density IN the continuum container.
3. **Bridge map** (explicit; not 'analogous to'): Bogoliubov-state closed-form ∘ HKR (Hochschild-Kostant-Rosenberg) `L_max → ∞` image at the BdG sub-algebra `M_2(ℂ) ⊂ A_K`; Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on `M_2(ℂ)`. **Element 3 fiducial-anchor binding** (per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` SUGGESTION-K=1): type **(ii) external-observation** — the bridge map composes through laboratory-IN PBH detection horizons (CMB / LISA / PTA combined) which ARE external observations at Pillar IX (same binding type as the OP-PROJ companion). **substrate-natural-binding** (per `regulator-pin-discipline.md §"four-axis orthogonality"` Binding axis) — the occupation `|v_a|²` is computed directly on the substrate's BdG sub-algebra, NOT canonical-import.
4. **Algebraic envelope**: `L^{{-α}}` convergence rate via the Bogoliubov-state closed-form at the BdG sub-algebra; **Level-2-binding sub-class** — the HKR-image of the state-pair occupation functional binds Level-1 to the Pillar IX continuum PBH population. Independent algebraic envelope: the state-pair-occupation envelope (bottom-K Bogoliubov-amplitude saturation) is structurally INDEPENDENT of the OP-PROJ cardinality-cascade-saturation envelope (the OP-PROJ N_eigs total-count channel vs this bottom-K state-pair channel — STRUCTURALLY ORTHOGONAL observables per the §VII.AX.OP-PROJ canonical-truncation analysis). **Regulator-INVARIANT** (IR-self-regularized by the BdG gap; the algebra-DEPENDENT state-pair signature per `cross-pillar-bridge-corpus.md §22`).
5. **Empirical anchor**: `n_PBH^STATE(L_max=14) = 7.2761e-23 m⁻³`, INHERITED from §VII.AX.OP-PROJ T1.13 (audit_sha256=`{T1_13_AUDIT_SHA}`) via the Bogoliubov-state closed-form `Σ_a |v_a|² · prob_form / L_pix_LRD³`. The state-projection and operator-projection readings AGREE on the n_PBH magnitude anchor (rel_tol ≥ 1e-4, publication-precision floor of 5 sig figs) but differ in algebra-axis identity-class (Cell IV state-pair vs Cell I spectrum-only). Lands inside the upper-22.6%-conjunct [{CONJUNCT_LO:.1e}, {CONJUNCT_HI:.1e}] m⁻³.

**STRUCTURAL-ORTHOGONAL-COMPANION declaration** (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 + `registry-landing.md §"Detection"` criterion (4)): §VII.AX.STATE-PROJ (Cell IV) and §VII.AX.OP-PROJ (Cell I) are **STRUCTURAL-ORTHOGONAL-COMPANIONS, NOT SOURCE-DOUBLE-CITE-CO-PRIMARY**. Cross-corner co-primary is STRUCTURALLY FORBIDDEN: criterion (4) requires both co-primary anchors to be on the SAME algebra-axis cell, but `corner_cell(STATE-PROJ) = Cell IV ≠ Cell I = corner_cell(OP-PROJ)`. Cell IV (algebra-DEPENDENT state-pair) and Cell I (algebra-INVARIANT spectrum-only) live on ORTHOGONAL algebra-axes; when both projection-side readings are independently registry-eligible the correct anchor structure is structural-orthogonal-companion. The two readings share the n_PBH MAGNITUDE anchor (7.2761e-23 m⁻³) but are STRUCTURALLY DISTINCT observables on orthogonal algebra-axis cells, period. Cross-corner magnitude comparison of the STATE-PROJ occupation functional (Cell IV) against the OP-PROJ cardinality functional (Cell I) is STRUCTURALLY FORBIDDEN AS A GATE per the parent rule (permitted in narrative ONLY with explicit `[CROSS-CORNER COMPARISON; STRUCTURALLY FORBIDDEN AS GATE]` declaration).

**connes-ncg-theorist CO-SIGNER cross-check** (Cell-IV algebra-axis classification per `permanent-results-registry.md §VII.U.2` clause (e) parse-tree decision procedure): the parse-tree terminus of `⟨ψ_GGE-PBH|n_a^PBH|ψ_GGE-PBH⟩` is a state-pair expectation `⟨ψ|·|ψ⟩` carrying the prepared-state index a — `state_pair_count = 1`, `algebra_dep_count = 1` ⇒ Cell IV. This is STRUCTURALLY DISTINCT from the OP-PROJ spectrum-only cardinality terminus (`Tr`/count, `state_pair_count = 0`). CO-SIGNER PASS: the Cell-IV classification is forced by the parse-tree structure, NOT by the state-history label 'GGE-PBH' (the label encodes the Pillar IX preparation history; the parse-tree structure IS the substrate-IS observable's algebra-axis identity).

**Eligibility chain** (the CHAINED prerequisite this landing depends on): §VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility = **(a)** S93 W4-1 Axis-A E2 verdict-artifact re-emission PASS (gate `{W4_1_GATE}`, audit_sha256=`{W4_1_AXIS_A_AUDIT_SHA}`; `axis_a_composite=PASS`, `emit_bug_confirmed=True`; Option-A supersedes the S92 Axis-A FAIL `19662dc1…`) **∧ (b)** S92 W-4 JE5 PASS at central-value (Axis-B; the prior Axis-B FAIL RETIRED-NOT-OVERTURNED via Option-A) **∧ (c)** Eq.(2′) registry-text correction LANDED on §VII.AX.OP-PROJ (S93 W4-4; the central-value PASS reading; the internally-inconsistent conjunctive band-containment statement corrected). All three conjuncts confirmed on disk at this landing.

**Substrate framing** (per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`): PHONONIC (state-pair occupation functional on the BdG sub-algebra — a Leggett-channel inter-band coherence / occupation observable). The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))` at τ_fold = 0.190; the PBH occupation functional `⟨ψ_GGE-PBH|n_a^PBH|ψ_GGE-PBH⟩ = |v_a|²` IS the substrate's intrinsic state-pair occupation on the GGE-state-prepared PBH population at the Level-1 single-τ-slice. Direction of explanation:

```
Substrate (D_K spectrum → GGE-state occupation n_a^PBH on the BdG sub-algebra M_2(ℂ) ⊂ A_K at τ_fold)
   IS ⟨ψ_GGE-PBH|n_a^PBH|ψ_GGE-PBH⟩ = |v_a|²  (state-pair functional; aggregates to 7.2761e-23 m⁻³)
      → Bridge map (Bogoliubov-state closed-form ∘ HKR L_max → ∞ at the BdG sub-algebra)
Laboratory (Pillar IX; PBH population occupation-density observation under combined CMB / LISA / PTA detection horizons)
   IN the continuum occupation-density measurement (∩ §W1c-69 PASS-magnitude posterior)
```

**FORBIDDEN inversion**: treating the cosmological PBH-population occupation measurement as the canonical observable and the substrate's GGE-state occupation functional as its "analog" inverts the direction — container-thinking violation per `phononic-framing.md`. The substrate's BdG-sector occupation functional IS canonical; the CMB / LISA / PTA detection horizons ARE the laboratory-IN measurement context.

**Cross-references**:

- `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 — the `.STATE-PROJ` suffix discipline; the OP-PROJ/STATE-PROJ naming-hygiene K-counter advances with this companion landing.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 — Cell IV (algebra-DEPENDENT state-pair) classification + cross-corner co-primary FORBIDDEN.
- `.claude/rules/cross-pillar-bridge-corpus.md §22` — regulator-behavior sibling discriminator (the algebra-DEPENDENT state-pair family is regulator-INVARIANT, IR-self-regularized by the gap; vs the OP-PROJ algebra-INVARIANT spectrum-only family which is regulator-DEPENDENT).
- §VII.AX.OP-PROJ (the operator-projection companion; Cell I; STAGE-3-PERMANENT-ELIGIBLE this wave) — the structural-orthogonal-companion; shares the n_PBH MAGNITUDE anchor (7.2761e-23 m⁻³) but on the orthogonal Cell-I algebra-axis.
- §VII.AX.OP-PROJ Eq.(2′) central-value PASS correction (S93 W4-4) — the eligibility-chain conjunct (c).
- S93 W4-1 Axis-A E2 re-emission gate `{W4_1_GATE}` audit_sha256=`{W4_1_AXIS_A_AUDIT_SHA}` — eligibility-chain conjunct (a).
- S91 W5-3 T1.13 gate `{T1_13_GATE}` audit_sha256=`{T1_13_AUDIT_SHA}` — the Element-5 anchor (inherited via Bogoliubov-state closed-form).
- Precedent: §VII.AJ.OP-PROJ + §VII.AJ.STATE-PROJ (S88 W7+W10) and §VII.AV.OP-PROJ + §VII.AV.STATE-PROJ (S93 W3-1) STRUCTURAL-ORTHOGONAL-COMPANION splits — the canonical algebra-axis OP-PROJ/STATE-PROJ companion template.
- `feedback_mack-bridge-role.md` — mack-cosmic-bridge sole-writer discipline (AMRI-PROMOTED 2026-04-28).

**Audit pin**: S93 W4-4 single-shot AFTER-pattern gate `{GATE_ID}` (`computations/session-93/s93_w4_4_vii_ax_state_proj_companion_landing.py`); single-shot AFTER-pattern per `registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"`. Companion slot documented at `sessions/framework/s93-slot-pre-allocation-lockfile.md §"RESERVED-FOR-S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY"` ("A SEPARATE W4-4 lands a NEW §VII.AX.STATE-PROJ companion (Cell IV) ... those are distinct slots").

"""


# ---------------------------------------------------------------------------
# Step (2) — write_atomic_with_fsync
# ---------------------------------------------------------------------------
def write_atomic_with_fsync(text: str, path: Path) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())


def insert_state_proj_block(registry_text: str, block: str) -> str:
    """Insert the NEW §VII.AX.STATE-PROJ block immediately BEFORE the
    §VII.AX.MULTI-PIN-ATLAS header (i.e. AFTER the §VII.AX.OP-PROJ block).
    Pure function; no I/O. Idempotent: callers guard on header presence.
    """
    boundary = registry_text.find(MULTI_PIN_ATLAS_HEADER_PREFIX)  # (local)
    if boundary == -1:
        raise RuntimeError(
            "§VII.AX.MULTI-PIN-ATLAS header (insertion boundary) not found: "
            f"{MULTI_PIN_ATLAS_HEADER_PREFIX[:60]!r}..."
        )
    # Confirm the OP-PROJ block precedes the boundary (sanity: we insert between).
    op_idx = registry_text.find(OP_PROJ_HEADER_PREFIX)  # (local)
    if op_idx == -1 or op_idx >= boundary:
        raise RuntimeError(
            "§VII.AX.OP-PROJ header not found before the MULTI-PIN-ATLAS boundary"
        )
    pre = registry_text[:boundary]  # (local)
    post = registry_text[boundary:]  # (local)
    return pre + block + "\n---\n\n\n" + post


# ---------------------------------------------------------------------------
# Section slice (for content_sha + verify)
# ---------------------------------------------------------------------------
def slice_block(text: str, header: str, next_markers: list[str]) -> str:
    """Return the block from `header` to the first of `next_markers` after it."""
    start = text.find(header)  # (local)
    if start == -1:
        return ""
    end = len(text)  # (local)
    for m in next_markers:
        idx = text.find(m, start + len(header))  # (local)
        if idx != -1 and idx < end:
            end = idx
    return text[start:end]


# ---------------------------------------------------------------------------
# Step (3) — re_read + verify_section_matches
# ---------------------------------------------------------------------------
def verify_section_matches(block: str) -> dict:
    """Re-read the registry; verify the §VII.AX.STATE-PROJ block landed verbatim
    with the Cell-IV tag, naming-hygiene suffix, STRUCTURAL-ORTHOGONAL-COMPANION
    declaration, cross-corner-FORBIDDEN constraint, 5-anatomy + 3-level +
    parse-tree, Element-5 inheritance, eligibility-chain cite, and correct
    ordering (after OP-PROJ, before MULTI-PIN-ATLAS). Pure verify; no write.
    """
    actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)

    state_idx = actual.find(STATE_PROJ_HEADER)  # (local)
    op_idx = actual.find(OP_PROJ_HEADER_PREFIX)  # (local)
    atlas_idx = actual.find(MULTI_PIN_ATLAS_HEADER_PREFIX)  # (local)

    block_present = block in actual  # (local) verbatim landing

    sec = slice_block(actual, STATE_PROJ_HEADER, [MULTI_PIN_ATLAS_HEADER_PREFIX])  # (local)

    cell_iv = "**Corner-cell**: **Cell IV**" in sec  # (local)
    suffix = (  # (local) the .STATE-PROJ naming-hygiene suffix discipline
        "§VII.AX.STATE-PROJ" in sec and ".STATE-PROJ` suffix" in sec
    )
    soc = (  # (local) STRUCTURAL-ORTHOGONAL-COMPANION (NOT co-primary)
        "STRUCTURAL-ORTHOGONAL-COMPANION" in sec
        and "NOT SOURCE-DOUBLE-CITE-CO-PRIMARY" in sec
    )
    cc_forbidden = "Cross-corner co-primary is STRUCTURALLY FORBIDDEN" in sec  # (local)
    anatomy_5 = "IS-not-IN anatomy" in sec  # (local)
    ladder_3 = "Three-level structural-confidence ladder" in sec  # (local)
    parse_tree = "Parse-tree expansion" in sec  # (local)
    # Cell-IV parse-tree counter: state_pair_count >= 1
    state_pair_counter = "state_pair_count = 1" in sec  # (local)
    # Element-5 inheritance from OP-PROJ T1.13
    element5_inherit = (  # (local)
        T1_13_AUDIT_SHA in sec and "INHERITED" in sec
    )
    # eligibility-chain conjuncts cited (a)/(b)/(c)
    eligibility_cited = (  # (local)
        W4_1_AXIS_A_AUDIT_SHA in sec
        and "Eq.(2′)" in sec
        and "JE5" in sec
    )
    # connes CO-SIGNER cross-check present
    connes_cosigner = "connes-ncg-theorist CO-SIGNER" in sec  # (local)
    # direction-of-explanation (substrate IS -> bridge -> laboratory IN)
    direction_ok = (  # (local)
        "Direction of explanation" in sec and "FORBIDDEN inversion" in sec
    )
    # ordering: OP-PROJ before STATE-PROJ before MULTI-PIN-ATLAS
    ordering_ok = (  # (local)
        op_idx != -1
        and state_idx != -1
        and atlas_idx != -1
        and op_idx < state_idx < atlas_idx
    )

    n_lines = sum(1 for ln in block.splitlines() if ln.strip())  # (local)

    return {
        "block_present": block_present,
        "cell_iv": cell_iv,
        "suffix": suffix,
        "soc": soc,
        "cc_forbidden": cc_forbidden,
        "anatomy_5": anatomy_5,
        "ladder_3": ladder_3,
        "parse_tree": parse_tree,
        "state_pair_counter": state_pair_counter,
        "element5_inherit": element5_inherit,
        "eligibility_cited": eligibility_cited,
        "connes_cosigner": connes_cosigner,
        "direction_ok": direction_ok,
        "ordering_ok": ordering_ok,
        "n_lines": n_lines,
    }


# ---------------------------------------------------------------------------
# Step (5) — emit ONCE
# ---------------------------------------------------------------------------
def find_latest_prior_audit_sha() -> str | None:
    """Latest NON-SUPERSEDED canonical audit_sha256 for this gate-ID (Option-A
    supersedes-tag source per gate-verdicts.md). None if no prior line.
    """
    if not VERDICT_TXT.exists():
        return None
    superseded: set[str] = set()  # (local)
    candidates: list[str] = []  # (local)
    for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                candidates.append(m.group(1))
            sm = re.search(r"supersedes=([a-f0-9]{64})", ln)  # (local)
            if sm:
                superseded.add(sm.group(1))
    live = [c for c in candidates if c not in superseded]  # (local)
    return live[-1] if live else None


def append_verdict(
    verdict: str, value, audit_sha: str, content_sha: str, supersedes: str | None = None
) -> None:
    """Append a single canonical dual-SHA verdict line + companion row.

    Atomic append (single `open("a")`). [VERIFY] trigger — no [SIGN] 3-tuple
    companion row (§W4-4 pre-registers no directional prediction). When
    `supersedes` is set, the corrective line carries the full-64-char tag per
    gate-verdicts.md Option A rule (2)/(5).
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    value_field = value if supersedes is None else f"{value}_supersedes={supersedes}"  # (local)
    line = (  # (local)
        f"{GATE_ID}: {verdict} -- value={value_field!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    supersedes_note = f"; supersedes={supersedes}" if supersedes else ""  # (local)
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"PHONONIC/registry-class §VII.AX.STATE-PROJ companion-landing artifact-existence; "
        f"[VERIFY] no [SIGN] 3-tuple{supersedes_note}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# JSON sidecar + NPZ data
# ---------------------------------------------------------------------------
def _write_json(*, verdict, value, audit_sha, content_sha, verify, eligibility,
                slot_documented, landed) -> None:
    record = {  # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "companion_entry": {
            "slot": STATE_PROJ_SLOT,
            "corner_cell": "Cell IV",
            "algebra_axis": "algebra-DEPENDENT (state-pair occupation functional on M_2(C) sub BdG)",
            "substrate_IS_observable": "<psi_GGE-PBH|n_a^PBH|psi_GGE-PBH> = |v_a|^2",
            "element_5_anchor_inherited": f"n_PBH = {N_PBH_FW_CENTRAL} m^-3 (from OP-PROJ T1.13)",
            "naming_hygiene_suffix": ".STATE-PROJ",
            "structural_orthogonal_companion_to": OP_PROJ_SLOT,
            "cross_corner_co_primary": "FORBIDDEN (Cell IV != Cell I)",
        },
        "eligibility_chain": eligibility,
        "slot_lockfile_documented": slot_documented,
        "landed": landed,
        "verify": verify,
        "constants_used": {"M_KK_GeV": float(M_KK), "tau_fold": float(tau_fold)},
    }
    JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"JSON sidecar: {JSON_PATH}")


def _write_npz(*, verdict, value, audit_sha, content_sha, verify, eligibility,
               slot_documented, landed) -> None:
    import numpy as np  # noqa: E402  (local import to keep header light)
    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        verdict=verdict,
        value=value,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        state_proj_slot=STATE_PROJ_SLOT,
        corner_cell="Cell IV",
        n_pbh_anchor_inherited=float(N_PBH_FW_CENTRAL),
        op_proj_t1_13_audit_sha=T1_13_AUDIT_SHA,
        w4_1_axis_a_audit_sha=W4_1_AXIS_A_AUDIT_SHA,
        eligibility_achieved=bool(eligibility.get("eligibility_achieved", False)),
        conjunct_a=bool(eligibility.get("conjunct_a_w4_1_axis_a_pass", False)),
        conjunct_b=bool(eligibility.get("conjunct_b_s92_w4_je5_converged", False)),
        conjunct_c=bool(eligibility.get("conjunct_c_eq2prime_landed", False)),
        class_i_diagnostic=str(eligibility.get("class_i_diagnostic")),
        slot_documented=bool(slot_documented),
        landed=bool(landed),
        verify_all_pass=bool(all(
            v for k, v in verify.items() if isinstance(v, bool)
        )) if verify else False,
        M_KK_GeV=float(M_KK),
        tau_fold=float(tau_fold),
    )
    print(f"NPZ data: {NPZ_PATH}")


# ---------------------------------------------------------------------------
# Main — single-shot AFTER pattern
# ---------------------------------------------------------------------------
def main() -> int:
    print(f"=== {GATE_ID} ===")
    print("Input-pin SHAs (first lines of stdout):")
    pins = log_input_pins(INPUT_FILES)  # (local)

    # --- CHAIN PREREQUISITE: §VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility ---
    eligibility = confirm_eligibility()  # (local)
    print("Eligibility chain (§VII.AX.OP-PROJ STAGE-3-PERMANENT = (a) ∧ (b) ∧ (c)):")
    for k, v in eligibility.items():
        print(f"  {k} = {v}")

    slot_documented = confirm_slot_documented()  # (local) advisory
    print(f"slot_documented (s93 lockfile §VII.AX.STATE-PROJ W4-4 distinct slot) = {slot_documented}")

    block = build_promotion_text()  # (local) Step (1)

    # --- Honest mechanical closure if eligibility NOT achieved (NO forced PASS) ---
    if not eligibility["eligibility_achieved"]:
        status_tokens = []  # (local)
        if not eligibility["conjunct_a_w4_1_axis_a_pass"]:
            status_tokens.append("a_axis_A_NOT-PASS")
        if not eligibility["conjunct_b_s92_w4_je5_converged"]:
            status_tokens.append("b_JE5_NOT-CONVERGED")
        if not eligibility["conjunct_c_eq2prime_landed"]:
            status_tokens.append("c_Eq2prime_NOT-LANDED")
        status = "_".join(status_tokens) if status_tokens else "unknown"  # (local)
        value = f"PRE-REG-INC_blocked_by_VII_AX_OP_PROJ_STAGE_3_eligibility_{status}"  # (local)
        # dual-SHA over the (un-landed) prospective block + pinmap (audit-trail)
        audit_sha, content_sha = compute_dual_sha(block, pins)  # (local)
        supersedes = find_latest_prior_audit_sha()  # (local)
        append_verdict("FAIL", value, audit_sha, content_sha, supersedes=supersedes)
        _write_json(
            verdict="FAIL", value=value, audit_sha=audit_sha, content_sha=content_sha,
            verify={}, eligibility=eligibility, slot_documented=slot_documented,
            landed=False,
        )
        _write_npz(
            verdict="FAIL", value=value, audit_sha=audit_sha, content_sha=content_sha,
            verify={}, eligibility=eligibility, slot_documented=slot_documented,
            landed=False,
        )
        print(f"VERDICT: FAIL (honest mechanical closure: {value})")
        return 0  # verdict is DATA; exit 0

    # --- idempotent guard (single-shot; re-runs must not duplicate the block) ---
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    header_present = STATE_PROJ_HEADER in registry_text  # (local)
    block_verbatim = block in registry_text  # (local)

    if not header_present:
        new_text = insert_state_proj_block(registry_text, block)  # (local) Step (1)
        write_atomic_with_fsync(new_text, REGISTRY_PATH)  # (local) Step (2)
        print("  §VII.AX.STATE-PROJ block inserted (after OP-PROJ, before MULTI-PIN-ATLAS).")
    elif not block_verbatim:
        # stale prior landing: strip the prior block span (header .. MULTI-PIN-ATLAS
        # header), then re-insert canonically.
        s0 = registry_text.find(STATE_PROJ_HEADER)  # (local)
        s1 = registry_text.find(MULTI_PIN_ATLAS_HEADER_PREFIX, s0)  # (local)
        if s0 != -1 and s1 != -1:
            cleaned = registry_text[:s0] + registry_text[s1:]  # (local)
        else:
            cleaned = registry_text  # (local)
        new_text = insert_state_proj_block(cleaned, block)  # (local)
        write_atomic_with_fsync(new_text, REGISTRY_PATH)  # (local)
        print("  Stale prior §VII.AX.STATE-PROJ block REPLACED with canonical build.")
    else:
        print("  §VII.AX.STATE-PROJ block already present verbatim (idempotent re-run); no write")

    # --- Step (3) re_read + verify_section_matches ---
    v = verify_section_matches(block)  # (local)
    print("Verification:")
    for k in sorted(v):
        print(f"  {k} = {v[k]}")

    # --- Step (4) determine verdict (single point of decision) ---
    predicates = bool(  # (local)
        v["block_present"]
        and v["cell_iv"]
        and v["suffix"]
        and v["soc"]
        and v["cc_forbidden"]
        and v["anatomy_5"]
        and v["ladder_3"]
        and v["parse_tree"]
        and v["state_pair_counter"]
        and v["element5_inherit"]
        and v["eligibility_cited"]
        and v["connes_cosigner"]
        and v["direction_ok"]
        and v["ordering_ok"]
    )
    substantive_ok = v["n_lines"] >= 15  # (local)
    verdict = "PASS" if (predicates and substantive_ok) else "FAIL"  # (local)

    # --- Step (5) emit ONCE — dual-SHA over the landed section + pinmap ---
    actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    state_section = slice_block(  # (local)
        actual, STATE_PROJ_HEADER, [MULTI_PIN_ATLAS_HEADER_PREFIX]
    )
    audit_sha, content_sha = compute_dual_sha(state_section, pins)  # (local)

    value = (  # (local)
        f"VII-AX-STATE-PROJ-COMPANION_"
        f"cell=Cell-IV_state_pair_functional=⟨ψ_GGE-PBH|n_a^PBH|ψ_GGE-PBH⟩_"
        f"anchor_structure=STRUCTURAL-ORTHOGONAL-COMPANION_"
        f"cross_corner_co_primary=FORBIDDEN_"
        f"companion_to=§VII.AX.OP-PROJ-Cell-I_"
        f"element5_inherited=n_PBH=7.2761e-23_from_T1.13_"
        f"eligibility_achieved={eligibility['eligibility_achieved']}_"
        f"conjunct_a_axisA={eligibility['conjunct_a_w4_1_axis_a_pass']}_"
        f"conjunct_b_JE5={eligibility['conjunct_b_s92_w4_je5_converged']}_"
        f"conjunct_c_Eq2prime={eligibility['conjunct_c_eq2prime_landed']}_"
        f"state_pair_counter={v['state_pair_counter']}_"
        f"connes_cosigner={v['connes_cosigner']}_"
        f"ordering_ok={v['ordering_ok']}_n_lines={v['n_lines']}_"
        f"slot_documented={slot_documented}"
    )

    supersedes = find_latest_prior_audit_sha()  # (local) Option-A corrective tag
    if supersedes:
        print(
            f"  prior verdict line detected; emitting corrective line with "
            f"supersedes={supersedes[:16]}..."
        )
    append_verdict(verdict, value, audit_sha, content_sha, supersedes=supersedes)
    print(
        f"4-tuple: (value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"
    )
    print(f"audit_sha256={audit_sha}")
    print(f"content_sha256={content_sha}")
    print(f"VERDICT: {verdict}")

    _write_json(
        verdict=verdict, value=value, audit_sha=audit_sha, content_sha=content_sha,
        verify=v, eligibility=eligibility, slot_documented=slot_documented, landed=True,
    )
    _write_npz(
        verdict=verdict, value=value, audit_sha=audit_sha, content_sha=content_sha,
        verify=v, eligibility=eligibility, slot_documented=slot_documented, landed=True,
    )

    # exit 0 regardless of PASS/FAIL — verdict is DATA, not script health, per
    # math-scripts.md §"Exit Codes and Verdict Semantics".
    return 0


if __name__ == "__main__":
    sys.exit(main())
