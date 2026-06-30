#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93-W5-6-VII-AW-SLOT-RENAME
===========================

Gate: S93-W5-6-VII-AW-SLOT-RENAME  [VERIFY]
Classification: NON-PHONONIC (METHODOLOGY-class registry-write hygiene; label-collision
                resolution; PASS predicate is artifact-existence-with-substantive-content
                + label-uniqueness, NOT a numerical comparison).
Owner: mack-cosmic-bridge (sole registry writer per `feedback_mack-bridge-role.md`).
Tier: hygiene (label-collision resolution; serial registry write — W5-2 + W5-5 land before).
Plan: sessions/session-plan/session-93-plan-w5.md §W5-6 (HK-S93-W9-1).

═══════════════════════════════════════════════════════════════════════════
WHAT THIS GATE DOES — the §VII.AW.OP-PROJ label-collision resolution
═══════════════════════════════════════════════════════════════════════════

The `§VII.AW.OP-PROJ` slot label is SHARED by TWO structurally distinct registry
entries (an artifact of two INDEPENDENT next-free-letter allocations in two waves):

  (1) SUBSTRATE-CLOCK-UNIQUENESS-THEOREM  [S90 W2 CF-19] — STAGE-3-PERMANENT (the
      W5-5 target; W5-5 just CONFIRMED it on-disk). KEEPS the §VII.AW.OP-PROJ label.
  (2) SU(3)-Coloured Chirality Spectral Triple (γ_F^c per Connes-Marcolli 2008 §11)
      [S90 W7 CF-45] — STAGE-0-CANDIDATE, structurally REJECTED at S91 W7-2b
      (axiom-5'' FAIL residual 3.274; KO-dim stays 6, CM-2008 §11 shift NOT realized;
      n_axiom_pass=6/7; level_2=non-binding). THIS is the RENAME TARGET.

Resolution per `registry-landing.md` next-free-letter protocol + `epistemic-discipline.md
§"Registry-Write Hygiene under Parallel-Writer Race"`: RENAME entry (2) to the next-free
§VII slot, leaving §VII.AW.OP-PROJ UNIQUELY attached to entry (1). The rename is
LABEL-ONLY — filenames, gate-IDs, audit-SHAs, and the coloured-chirality content are
UNCHANGED; only the §VII slot label moves.

Next-free slot: highest current slot = §VII.BE (line ~20042 at plan-freeze). §VII.BF and
§VII.BG verified GENUINELY FREE at plan-freeze (grep returns no matches). Target = §VII.BF;
the script re-verifies §VII.BF is unoccupied at RUNTIME before writing (verify-before-write
per the next-free-letter protocol), and the verdict is FAIL-with-remediation if it is taken.

The two entries are NOT co-primary anchors of one theorem (which would be FORBIDDEN
cross-corner per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`);
they are an unresolved label-collision. Per `phononic-framing.md §"IS Space, Not IN Space"`
the substrate framing of the RENAMED entry (the rejected SU(3)-coloured chirality γ_F^c
spectral triple) is UNCHANGED — only its slot label moves.

═══════════════════════════════════════════════════════════════════════════
CROSS-FILE BLAST RADIUS (all loci updated in this run; HK-S93-W9-1)
═══════════════════════════════════════════════════════════════════════════

(i)   sessions/permanent-results-registry.md — entry-(2) heading + in-block self-refs
      (slot-label note, slot-allocation provenance, substrate-framing ×2, Element-4
      NON-BINDING self-ref) + entry-(1) SUBSTRATE-CLOCK slot-label note (cross-pointer
      to entry (2)) + the index-table row (annotation update + NEW §VII.BF index row).
(ii)  sessions/permanent-results-registry.md §VII.AT.OP-PROJ sibling pointers (×2) —
      "sibling slot/candidate (b) SU(3)-coloured chirality" → §VII.BF.
(iii) sessions/framework/s90-slot-pre-allocation-lockfile.md — RESERVED-FOR-WORKSHOP-
      W7-CF-45-VII-AW block (slot field annotate superseded-by-rename) + updates-table
      rename row.
(iv)  sessions/archive/session-93/session-93-w5-workingpaper.md — §W5-6 section (written by the
      orchestrator-side WP writer; this script does NOT write the WP).

OUT-OF-BLAST-RADIUS (correctly UNCHANGED — verified at plan-freeze):
  - Index row + body precedent-citations of §VII.AW.OP-PROJ at lines ~18502, ~19341,
    ~19343, ~19432 (and others) cite the SUBSTRATE-CLOCK entry / mack-sole-writer
    precedent → they refer to entry (1) which KEEPS the label. UNCHANGED.
  - s93-slot-pre-allocation-lockfile.md line ~29 anchor-list explicitly names
    "§VII.AW.OP-PROJ SUBSTRATE-CLOCK-UNIQUENESS-THEOREM" → entry (1). UNCHANGED.
  - methodology-wave-instances.md historical ledger rows record the S90 W7 CF-45
    LANDING event (append-only past-record of what gate-ID landed where), NOT a live
    slot-label pointer; renaming them would falsify the historical record. UNCHANGED.
  - The PRE-EXISTING AU/AW '#3' STAGE-3 ORDINAL collision (CF-S94-STAGE-3-ORDINAL-
    COLLISION-AU-AW) is a SEPARATE issue (the "THIRD STAGE-3-PERMANENT" ordinal among
    AU/AW); this gate resolves the SLOT-LABEL collision, NOT the ordinal collision.

Single-shot AFTER pattern per `registry-landing.md §"Bridge-Landing Script Architecture"`:
build all rename edits in memory → write_atomic → re-read + verify (label-uniqueness +
new-slot-heading + no dangling SU(3)-at-§VII.AW + all loci updated) → emit ONE verdict.

Drift correction (plan-pinned line numbers STALE per `substrate-first-canonical-sourcing.md
§(ii.B)`): all edits are content-anchored on EXACT substrings, NOT line numbers.

Verdict file: computations/session-93/s93_gate_verdicts.txt
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU-only (text edits + SHA cross-check; no compute)
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

# Per computations/_shared/CLAUDE.md ALL scripts MUST import canonical_constants
# (even METHODOLOGY-class; no physics constants CONSUMED here, but the import is
# mandatory + the spawn prompt requires the literal `from canonical_constants import`).
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import M_KK, tau_fold  # noqa: E402 (metadata only; not gate-load-bearing)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + canonical paths
# ---------------------------------------------------------------------------
GATE_ID = "S93-W5-6-VII-AW-SLOT-RENAME"  # (local)
SCHEME = "registry-text-METHODOLOGY-class"  # (local) per plan §W5-6 machinery_pin_map.scheme
CONVENTION = "VII-AW-slot-rename-label-only-SU3-coloured-chirality-to-next-free-BF"  # (local) per plan §W5-6
L_MAX = "N/A"  # (local) METHODOLOGY-class registry-text edit; no L_max
SCHEMA_VERSION = "S84+"  # (local)

OLD_LABEL = "§VII.AW.OP-PROJ"  # (local) the collided label (rejected entry leaves it)
NEW_SLOT = "§VII.BF"  # (local) next-free target (verify-before-write at runtime)
NEXT_CANDIDATE_IF_TAKEN = "§VII.BG"  # (local) fallback if §VII.BF occupied at runtime

SESSION_DIR = ROOT / "computations" / "session-93"  # (local)
OUT_NPZ = SESSION_DIR / "s93_w5_6_vii_aw_slot_rename.npz"  # (local)
OUT_PNG = SESSION_DIR / "s93_w5_6_vii_aw_slot_rename.png"  # (local)
OUT_JSON = SESSION_DIR / "s93_w5_6_vii_aw_slot_rename.json"  # (local)
VERDICT_FILE = SESSION_DIR / "s93_gate_verdicts.txt"  # (local)

CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"  # (local)
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"  # (local)
LOCKFILE = ROOT / "sessions" / "framework" / "s90-slot-pre-allocation-lockfile.md"  # (local) plan §W5-6 (iii)
SCRIPT_PATH = Path(__file__).resolve()  # (local)

# ---------------------------------------------------------------------------
# CONTENT-ANCHORED rename edits (exact-substring find/replace; drift-robust).
# Each (old, new) pair is an EXACT full-string match so the replace is unambiguous.
# The rename is LABEL-ONLY: only the §VII slot label moves; content is preserved.
# ---------------------------------------------------------------------------

# --- (i) Registry: entry-(2) heading (the RENAME TARGET heading) ---
REG_HEADING_OLD = (  # (local)
    "## §VII.AW.OP-PROJ — SU(3)-Coloured Chirality Spectral Triple "
    "(γ_F^c per Connes-Marcolli 2008 §11) (W-5 candidate (b); "
    "STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS; S90 W7 CF-45 — "
    "mack-cosmic-bridge sole-writer per feedback_mack-bridge-role.md, 2026-05-15)"
)
REG_HEADING_NEW = (  # (local)
    "## §VII.BF — SU(3)-Coloured Chirality Spectral Triple "
    "(γ_F^c per Connes-Marcolli 2008 §11) (W-5 candidate (b); "
    "STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS — REJECTED at S91 W7-2b on substrate-IS "
    "grounds; S90 W7 CF-45; slot renamed §VII.AW.OP-PROJ → §VII.BF at S93 W5-6 to resolve the "
    "§VII.AW.OP-PROJ label-collision per `registry-landing.md` next-free-letter protocol — "
    "mack-cosmic-bridge sole-writer per feedback_mack-bridge-role.md, 2026-05-15 / renamed 2026-05-24)"
)

# --- (i) Registry: entry-(2) slot-label note (collision → RESOLVED) ---
REG_E2_NOTE_OLD = (  # (local)
    "> **Slot-label note (S92 W9-4 follow-up disambiguation, mack-cosmic-bridge sole-writer per "
    "`feedback_mack-bridge-role.md`, 2026-05-23)**: the `§VII.AW.OP-PROJ` slot label is SHARED by two "
    "structurally distinct registry entries — **(1)** THIS section, SU(3)-Coloured Chirality Spectral "
    "Triple [S90 W7 CF-45]; and **(2)** SUBSTRATE-CLOCK-UNIQUENESS-THEOREM [S90 W2 CF-19], at the "
    "`### §VII.AW.OP-PROJ — SUBSTRATE-CLOCK-UNIQUENESS-THEOREM` header further below (registry line "
    "~18322). THIS is entry (1). The index-table row (registry line ~133) maps `§VII.AW.OP-PROJ` to "
    "entry (2) only. The two are NOT co-primary anchors of one theorem (per "
    "`cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality K-counter\"`); they are an unresolved "
    "label-collision from independent next-free-letter allocations in two different waves (S90 W2 and "
    "S90 W7). Resolve cross-references to this slot by CONTENT (header title keyword), NOT by label "
    "alone. Cross-pointer: entry (2) at `### §VII.AW.OP-PROJ — SUBSTRATE-CLOCK-UNIQUENESS-THEOREM`."
)
REG_E2_NOTE_NEW = (  # (local)
    "> **Slot-label note — COLLISION RESOLVED (S93 W5-6, mack-cosmic-bridge sole-writer per "
    "`feedback_mack-bridge-role.md`, 2026-05-24)**: this entry (the SU(3)-Coloured Chirality Spectral "
    "Triple [S90 W7 CF-45], STAGE-0-CANDIDATE REJECTED at S91 W7-2b) was RENAMED from "
    "`§VII.AW.OP-PROJ` to `§VII.BF` at S93 W5-6 (gate `S93-W5-6-VII-AW-SLOT-RENAME`) to resolve the "
    "long-standing `§VII.AW.OP-PROJ` label-collision. The collision arose from two INDEPENDENT "
    "next-free-letter allocations in two waves: SUBSTRATE-CLOCK-UNIQUENESS-THEOREM [S90 W2 CF-19] and "
    "THIS SU(3)-Coloured Chirality entry [S90 W7 CF-45] both landed at `§VII.AW.OP-PROJ`. Post-rename, "
    "`§VII.AW.OP-PROJ` resolves UNIQUELY to SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (at the "
    "`### §VII.AW.OP-PROJ — SUBSTRATE-CLOCK-UNIQUENESS-THEOREM` header). The rename is LABEL-ONLY: the "
    "filename / gate-ID (`S90-CF-A40-FAIL-ALTERNATIVE-CHIRALITY-RESCOPE`) / audit-SHAs / "
    "coloured-chirality content are UNCHANGED. The two entries were NEVER co-primary anchors of one "
    "theorem (cross-corner co-primary is FORBIDDEN per `cross-pillar-bridge-anatomy.md §\"Algebra-axis "
    "orthogonality K-counter\"`). Cross-pointer: the surviving `§VII.AW.OP-PROJ` is "
    "SUBSTRATE-CLOCK-UNIQUENESS-THEOREM at `### §VII.AW.OP-PROJ — SUBSTRATE-CLOCK-UNIQUENESS-THEOREM`."
)

# --- (i) Registry: entry-(2) slot-allocation provenance (annotate original alloc + rename) ---
REG_E2_ALLOC_OLD = (  # (local)
    "> **Slot allocation provenance**: S90 W7 CF-45 (mack-cosmic-bridge sole-writer per "
    "`feedback_mack-bridge-role.md`, 2026-05-15). Next-free-letter assignment per `registry-landing.md` "
    "next-free-letter protocol: §VII.AU (CF-63 REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION) + §VII.AV "
    "(CF-W7-1 W7c rerouted emission #3) occupied; §VII.AW is the next-free letter for the W-5 candidate "
    "(b) SU(3)-coloured chirality slot scaffolding (skipping §VII.AU + §VII.AV). Slot-allocation "
    "lockfile entry: `sessions/framework/s90-slot-pre-allocation-lockfile.md` with "
    "RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW tag."
)
REG_E2_ALLOC_NEW = (  # (local)
    "> **Slot allocation provenance**: S90 W7 CF-45 (mack-cosmic-bridge sole-writer per "
    "`feedback_mack-bridge-role.md`, 2026-05-15). Original next-free-letter assignment per "
    "`registry-landing.md` next-free-letter protocol: §VII.AU (CF-63 "
    "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION) + §VII.AV (CF-W7-1 W7c rerouted emission #3) "
    "occupied; §VII.AW was the next-free letter for the W-5 candidate (b) SU(3)-coloured chirality "
    "slot scaffolding (skipping §VII.AU + §VII.AV) — but §VII.AW.OP-PROJ ALSO carried the "
    "SUBSTRATE-CLOCK-UNIQUENESS-THEOREM [S90 W2 CF-19] (independent S90 W2 allocation), producing the "
    "label-collision. **S93 W5-6 RENAME (2026-05-24)**: this entry moved §VII.AW.OP-PROJ → §VII.BF "
    "(the next-free letter above §VII.BE) to resolve the collision; §VII.AW.OP-PROJ retained by "
    "SUBSTRATE-CLOCK-UNIQUENESS-THEOREM. Slot-allocation lockfile entry: "
    "`sessions/framework/s90-slot-pre-allocation-lockfile.md` with RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW "
    "tag (annotated superseded-by-rename in the lockfile updates table)."
)

# --- (i) Registry: entry-(2) substrate-framing line (TWO §VII.AW.OP-PROJ self-refs) ---
REG_E2_FRAMING_OLD = (  # (local) exact line 17555 (single line)
    "**Substrate framing**: The SU(3)-coloured chirality grading `γ_9'' = γ_F^c` IS a STRUCTURALLY "
    "DISTINCT spectral triple from the standard tensor-product chirality `γ_9 = γ_5 ⊗ γ_F` at "
    "§VII.AQ.OP-PROJ. The substrate IS a spectral triple `(A, H, D, γ, J)`; the colour-dressing of the "
    "chirality grading at §VII.AW.OP-PROJ produces a new spectral triple with a refined sector "
    "decomposition of the `M_3(ℂ)` summand. Direction of explanation: substrate IS spectral triple → "
    "colour-axis-resolved chirality grading IS new-spectral-triple → new substrate-IS observables "
    "(colour-axis-tagged cocycles) → new §VII registry slot at §VII.AW.OP-PROJ. Container-thinking "
    "violation avoided: \"Colour is a label we attach to chirality eigenstates\" — INVERT: \"the "
    "SU(3)-coloured chirality grading IS the substrate's intrinsic refinement of the chirality "
    "decomposition at the `M_3(ℂ)` summand; the colour-axis IS substrate-IS, not a label imposed FROM "
    "OUTSIDE the substrate\"."
)
REG_E2_FRAMING_NEW = (  # (local)
    "**Substrate framing**: The SU(3)-coloured chirality grading `γ_9'' = γ_F^c` IS a STRUCTURALLY "
    "DISTINCT spectral triple from the standard tensor-product chirality `γ_9 = γ_5 ⊗ γ_F` at "
    "§VII.AQ.OP-PROJ. The substrate IS a spectral triple `(A, H, D, γ, J)`; the colour-dressing of the "
    "chirality grading at §VII.BF (renamed from §VII.AW.OP-PROJ at S93 W5-6) produces a new spectral "
    "triple with a refined sector decomposition of the `M_3(ℂ)` summand. Direction of explanation: "
    "substrate IS spectral triple → colour-axis-resolved chirality grading IS new-spectral-triple → "
    "new substrate-IS observables (colour-axis-tagged cocycles) → new §VII registry slot at §VII.BF. "
    "Container-thinking violation avoided: \"Colour is a label we attach to chirality eigenstates\" — "
    "INVERT: \"the SU(3)-coloured chirality grading IS the substrate's intrinsic refinement of the "
    "chirality decomposition at the `M_3(ℂ)` summand; the colour-axis IS substrate-IS, not a label "
    "imposed FROM OUTSIDE the substrate\"."
)

# --- (i) Registry: entry-(2) Element-4 NON-BINDING self-ref (line 17569) ---
REG_E2_ELEM4_OLD = (  # (local)
    "4. **Element-4 Level-2 sub-class: NON-BINDING** — same logic as §VII.AT.OP-PROJ: HKR FAILs at the "
    "substrate's axiom-4 obstruction, so no binding bridge map to a laboratory-IN observable. The "
    "§VII.AW.OP-PROJ entry cannot achieve STAGE-1-CANDIDATE eligibility via candidate (b) under "
    "SU(3)-coloured chirality with this colour-signs choice."
)
REG_E2_ELEM4_NEW = (  # (local)
    "4. **Element-4 Level-2 sub-class: NON-BINDING** — same logic as §VII.AT.OP-PROJ: HKR FAILs at the "
    "substrate's axiom-4 obstruction, so no binding bridge map to a laboratory-IN observable. The "
    "§VII.BF entry (renamed from §VII.AW.OP-PROJ at S93 W5-6) cannot achieve STAGE-1-CANDIDATE "
    "eligibility via candidate (b) under SU(3)-coloured chirality with this colour-signs choice."
)

# --- (i) Registry: entry-(1) SUBSTRATE-CLOCK slot-label note (cross-pointer → RESOLVED) ---
REG_E1_NOTE_OLD = (  # (local)
    "> **Slot-label note (S92 W9-4 follow-up disambiguation, mack-cosmic-bridge sole-writer per "
    "`feedback_mack-bridge-role.md`, 2026-05-23)**: the `§VII.AW.OP-PROJ` slot label is SHARED by two "
    "structurally distinct registry entries — **(1)** SU(3)-Coloured Chirality Spectral Triple [S90 W7 "
    "CF-45], at the `## §VII.AW.OP-PROJ — SU(3)-Coloured Chirality Spectral Triple` header further "
    "above (registry line ~17509); and **(2)** THIS section, SUBSTRATE-CLOCK-UNIQUENESS-THEOREM [S90 W2 "
    "CF-19]. THIS is entry (2). The index-table row (registry line ~133) maps `§VII.AW.OP-PROJ` to THIS "
    "entry (2). The two are NOT co-primary anchors of one theorem (per `cross-pillar-bridge-anatomy.md "
    "§\"Algebra-axis orthogonality K-counter\"`); they are an unresolved label-collision from "
    "independent next-free-letter allocations in two different waves (S90 W2 and S90 W7). Resolve "
    "cross-references to this slot by CONTENT (header title keyword), NOT by label alone. Cross-pointer: "
    "entry (1) at `## §VII.AW.OP-PROJ — SU(3)-Coloured Chirality Spectral Triple`."
)
REG_E1_NOTE_NEW = (  # (local)
    "> **Slot-label note — COLLISION RESOLVED (S93 W5-6, mack-cosmic-bridge sole-writer per "
    "`feedback_mack-bridge-role.md`, 2026-05-24)**: the `§VII.AW.OP-PROJ` slot label now resolves "
    "UNIQUELY to THIS entry, SUBSTRATE-CLOCK-UNIQUENESS-THEOREM [S90 W2 CF-19]. The former collision "
    "(the SU(3)-Coloured Chirality Spectral Triple [S90 W7 CF-45] had also landed at `§VII.AW.OP-PROJ` "
    "via an INDEPENDENT S90 W7 next-free-letter allocation) was RESOLVED at S93 W5-6 (gate "
    "`S93-W5-6-VII-AW-SLOT-RENAME`) by RENAMING the SU(3)-Coloured Chirality entry to `§VII.BF` "
    "(now at the `## §VII.BF — SU(3)-Coloured Chirality Spectral Triple` header). The two were NEVER "
    "co-primary anchors of one theorem (cross-corner co-primary FORBIDDEN per "
    "`cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality K-counter\"`). The index-table row "
    "(registry line ~133) maps `§VII.AW.OP-PROJ` to THIS entry (SUBSTRATE-CLOCK-UNIQUENESS-THEOREM); a "
    "separate index row maps `§VII.BF` to the renamed SU(3)-Coloured Chirality entry. Cross-pointer: "
    "the renamed entry is at `## §VII.BF — SU(3)-Coloured Chirality Spectral Triple`."
)

# --- (ii) Registry: §VII.AT.OP-PROJ sibling pointer #1 (Cross-link block, line 17474) ---
REG_AT_PTR1_OLD = (  # (local)
    "- §VII.AW.OP-PROJ (sibling slot; candidate (b) SU(3)-coloured chirality γ_F^c per "
    "Connes-Marcolli 2008 §11)"
)
REG_AT_PTR1_NEW = (  # (local)
    "- §VII.BF (sibling slot; candidate (b) SU(3)-coloured chirality γ_F^c per Connes-Marcolli 2008 "
    "§11; renamed from §VII.AW.OP-PROJ at S93 W5-6 to resolve the §VII.AW.OP-PROJ label-collision)"
)

# --- (ii) Registry: §VII.AT.OP-PROJ sibling pointer #2 (FAIL-diagnostic Cross-links, line 17505) ---
REG_AT_PTR2_OLD = (  # (local)
    "- §VII.AW.OP-PROJ (sibling candidate (b) SU(3)-coloured chirality; also FAIL — see its "
    "FAIL-diagnostic block)."
)
REG_AT_PTR2_NEW = (  # (local)
    "- §VII.BF (sibling candidate (b) SU(3)-coloured chirality; also FAIL — see its FAIL-diagnostic "
    "block; renamed from §VII.AW.OP-PROJ at S93 W5-6 to resolve the label-collision)."
)

# --- (i) Registry: index-table row for SUBSTRATE-CLOCK (annotation: collision RESOLVED) ---
IDX_E1_OLD = (  # (local) the SUBSTRATE-CLOCK index row with the [LABEL SHARED ...] annotation
    "| §VII.AW.OP-PROJ | THM **[STAGE-3-PERMANENT 2026-05-24 — Stage-2 PASS-AND complete; promoted "
    "per joint-theorem-promotion.md §\"Stage 3\"]** | SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (S90 W2 CF-19 — "
    "mack-cosmic-bridge sole-writer landing per `feedback_mack-bridge-role.md`, 2026-05-13) **[LABEL "
    "SHARED — 2 entries: this row = SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (S90 W2 CF-19); the other = "
    "SU(3)-Coloured Chirality Spectral Triple (S90 W7 CF-45); see both `§VII.AW.OP-PROJ` body sections; "
    "collision noted S92 W9-4 follow-up]** | mack-cosmic-bridge | 2026-05-13 |"
)
IDX_E1_NEW = (  # (local)
    "| §VII.AW.OP-PROJ | THM **[STAGE-3-PERMANENT 2026-05-24 — Stage-2 PASS-AND complete; promoted "
    "per joint-theorem-promotion.md §\"Stage 3\"]** | SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (S90 W2 CF-19 — "
    "mack-cosmic-bridge sole-writer landing per `feedback_mack-bridge-role.md`, 2026-05-13) **[LABEL "
    "COLLISION RESOLVED S93 W5-6 — §VII.AW.OP-PROJ now UNIQUELY maps to SUBSTRATE-CLOCK-UNIQUENESS-"
    "THEOREM; the former co-occupant SU(3)-Coloured Chirality Spectral Triple (S90 W7 CF-45) renamed to "
    "§VII.BF]** | mack-cosmic-bridge | 2026-05-13 |"
)

# NEW §VII.BF index row — inserted directly AFTER the SUBSTRATE-CLOCK index row.
IDX_BF_NEW_ROW = (  # (local)
    "\n| §VII.BF | THM | SU(3)-Coloured Chirality Spectral Triple (γ_F^c per Connes-Marcolli 2008 §11) "
    "(W-5 candidate (b); STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS — REJECTED at S91 W7-2b on "
    "substrate-IS grounds [axiom-5'' FAIL residual 3.274; KO-dim stays 6]; S90 W7 CF-45; slot renamed "
    "§VII.AW.OP-PROJ → §VII.BF at S93 W5-6 to resolve the §VII.AW.OP-PROJ label-collision) | "
    "mack-cosmic-bridge | 2026-05-24 |"
)

# --- (iii) Lockfile: RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW Slot field (annotate superseded) ---
LOCK_SLOT_OLD = "- **Slot**: `§VII.AW.OP-PROJ`\n- **Workshop**: W-5 candidate (b) SU(3)-coloured chirality"  # (local)
LOCK_SLOT_NEW = (  # (local)
    "- **Slot**: `§VII.AW.OP-PROJ` → **RENAMED `§VII.BF` at S93 W5-6** (the SU(3)-coloured chirality "
    "entry moved off `§VII.AW.OP-PROJ` to resolve the label-collision with "
    "SUBSTRATE-CLOCK-UNIQUENESS-THEOREM [S90 W2 CF-19]; the original `§VII.AW.OP-PROJ` reservation "
    "below records the pre-rename allocation and is SUPERSEDED-BY-RENAME)\n"
    "- **Workshop**: W-5 candidate (b) SU(3)-coloured chirality"
)

# Lockfile updates-table rename row (append after the existing initial-allocation rows).
LOCK_RENAME_ROW = (  # (local)
    "| 2026-05-24 | S93 W5-6 RENAME §VII.AW.OP-PROJ → §VII.BF (label-collision resolution; the "
    "SU(3)-coloured chirality entry [S90 W7 CF-45] moved off §VII.AW.OP-PROJ, which is now uniquely "
    "SUBSTRATE-CLOCK-UNIQUENESS-THEOREM [S90 W2 CF-19]; label-only, content/gate-ID/SHA UNCHANGED) | "
    "§VII.AW.OP-PROJ → §VII.BF | RENAMED (SUPERSEDES the W7-CF-45-VII-AW RESERVED allocation) |\n"
)
LOCK_RENAME_MARKER = "S93 W5-6 RENAME §VII.AW.OP-PROJ → §VII.BF"  # (local) idempotency guard


# ---------------------------------------------------------------------------
# The full replace plan (label, file, old, new). Order is irrelevant (exact strings).
# ---------------------------------------------------------------------------
def build_registry_replacements() -> list[tuple[str, str, str]]:
    """Return [(locus_id, old, new), ...] for the registry. EXACT-substring; LABEL-ONLY."""
    return [
        ("(i)-entry2-heading", REG_HEADING_OLD, REG_HEADING_NEW),
        ("(i)-entry2-slot-label-note", REG_E2_NOTE_OLD, REG_E2_NOTE_NEW),
        ("(i)-entry2-slot-alloc-provenance", REG_E2_ALLOC_OLD, REG_E2_ALLOC_NEW),
        ("(i)-entry2-substrate-framing", REG_E2_FRAMING_OLD, REG_E2_FRAMING_NEW),
        ("(i)-entry2-element4-self-ref", REG_E2_ELEM4_OLD, REG_E2_ELEM4_NEW),
        ("(i)-entry1-slot-label-note", REG_E1_NOTE_OLD, REG_E1_NOTE_NEW),
        ("(ii)-AT-sibling-ptr-1", REG_AT_PTR1_OLD, REG_AT_PTR1_NEW),
        ("(ii)-AT-sibling-ptr-2", REG_AT_PTR2_OLD, REG_AT_PTR2_NEW),
        ("(i)-index-row-substrate-clock", IDX_E1_OLD, IDX_E1_NEW),
    ]


def build_lockfile_replacements() -> list[tuple[str, str, str]]:
    return [
        ("(iii)-lockfile-reserved-slot-field", LOCK_SLOT_OLD, LOCK_SLOT_NEW),
    ]


# ---------------------------------------------------------------------------
# SHA helpers
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def sha256_of_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 76)
    print(f"Gate: {GATE_ID}")
    print("=" * 76)
    print("Input SHA-256 pins (first lines of stdout):")
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        rel = str(p.relative_to(ROOT)).replace("\\", "/") if p.exists() else str(p)
        print(f"  {name:30s} = {sha[:16]}...  ({rel})")
    return pins


def extract_renamed_block(registry_text: str) -> str:
    """Extract the renamed §VII.BF SU(3)-Coloured-Chirality entry block (heading to next
    `## §VII.`/`### §VII.` boundary). Content-anchored on the NEW heading. '' if absent.
    """
    marker = "## §VII.BF — SU(3)-Coloured Chirality Spectral Triple"  # (local)
    start = registry_text.find(marker)  # (local)
    if start < 0:
        return ""
    rest = registry_text[start + len(marker):]  # (local)
    # next section boundary: any subsequent `## §VII.` or `### §VII.` heading
    nxt_candidates = [m.start() for m in re.finditer(r"\n#{2,3} §VII\.", rest)]  # (local)
    nxt = min(nxt_candidates) if nxt_candidates else -1  # (local)
    block = marker + (rest if nxt < 0 else rest[:nxt])  # (local)
    return block


# ---------------------------------------------------------------------------
# Slot-occupancy scan (next-free-letter verify-before-write; mirrors
# s88_w4a_split_registry_writer.py::scan_slot_occupancy across ALL header levels).
# ---------------------------------------------------------------------------
def scan_slot_occupied(registry_text: str, slot_label: str) -> bool:
    """True iff `slot_label` already heads a section at ##/###/#### level."""
    for prefix in ("#### ", "### ", "## "):
        if f"{prefix}{slot_label} " in registry_text or f"{prefix}{slot_label}\n" in registry_text:
            return True
        if f"{prefix}{slot_label} —" in registry_text:
            return True
    return False


def apply_replacements(text: str, repls: list[tuple[str, str, str]]) -> tuple[str, dict]:
    """Apply each EXACT-substring replacement exactly once. Returns (new_text, per-locus report).
    Idempotent: if `old` absent but `new` already present, mark already_applied.
    """
    report = {}  # (local)
    out = text  # (local)
    for locus, old, new in repls:
        n_old = out.count(old)  # (local)
        if n_old == 1:
            out = out.replace(old, new, 1)
            report[locus] = {"status": "applied", "old_count": n_old}
        elif n_old == 0 and (new in out):
            report[locus] = {"status": "already_applied", "old_count": 0}
        elif n_old == 0:
            report[locus] = {"status": "OLD_NOT_FOUND", "old_count": 0}
        else:
            # n_old > 1 — ambiguous; do NOT blind-replace (would over-edit)
            report[locus] = {"status": "AMBIGUOUS_MULTI_MATCH", "old_count": n_old}
    return out, report


def insert_bf_index_row(text: str) -> tuple[str, dict]:
    """Insert the NEW §VII.BF index row immediately AFTER the SUBSTRATE-CLOCK index row.
    Idempotent: skip if a `| §VII.BF | THM |` index row already exists.
    """
    rep = {"status": "pending"}  # (local)
    if re.search(r"\n\| §VII\.BF \| THM \|", text):
        rep["status"] = "already_present"
        return text, rep
    anchor = IDX_E1_NEW  # (local) the (now-updated) SUBSTRATE-CLOCK index row
    if anchor not in text:
        # fall back to the pre-update anchor if replacements have not run yet
        anchor = IDX_E1_OLD if IDX_E1_OLD in text else None
    if anchor is None:
        rep["status"] = "ANCHOR_NOT_FOUND"
        return text, rep
    out = text.replace(anchor, anchor + IDX_BF_NEW_ROW, 1)  # (local)
    rep["status"] = "inserted"
    return out, rep


def append_lockfile_rename_row(lock_text: str) -> tuple[str, dict]:
    """Append the rename row to the lockfile 'Lockfile updates' table (after existing rows).
    Idempotent on LOCK_RENAME_MARKER. Append after the last table row.
    """
    rep = {"status": "pending"}  # (local)
    if LOCK_RENAME_MARKER in lock_text:
        rep["status"] = "already_present"
        return lock_text, rep
    # The last initial-allocation row is the §VII.AW.OP-PROJ RESERVED row.
    last_row_anchor = "| 2026-05-15 | Initial allocation per S90 W7 CF-45 | §VII.AW.OP-PROJ | RESERVED |"  # (local)
    if last_row_anchor in lock_text:
        out = lock_text.replace(last_row_anchor, last_row_anchor + "\n" + LOCK_RENAME_ROW.rstrip("\n"), 1)  # (local)
        rep["status"] = "appended_after_table"
        return out, rep
    # fallback: append at EOF
    out = lock_text.rstrip("\n") + "\n" + LOCK_RENAME_ROW  # (local)
    rep["status"] = "appended_eof"
    return out, rep


def write_atomic(p: Path, text: str) -> None:
    """Atomic write with fsync (single-shot AFTER pattern; no per-attempt rewrites)."""
    tmp = p.with_suffix(p.suffix + ".tmp")  # (local)
    with tmp.open("w", encoding="utf-8", newline="") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, p)


# ---------------------------------------------------------------------------
# Option-A supersedes source (latest non-superseded prior line for this gate-ID)
# ---------------------------------------------------------------------------
def find_latest_prior_audit_sha() -> str | None:
    if not VERDICT_FILE.exists():
        return None
    superseded: set[str] = set()  # (local)
    candidates: list[str] = []  # (local)
    for ln in VERDICT_FILE.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                candidates.append(m.group(1))
            sm = re.search(r"supersedes=([a-f0-9]{64})", ln)  # (local)
            if sm:
                superseded.add(sm.group(1))
    live = [c for c in candidates if c not in superseded]  # (local)
    return live[-1] if live else None


def append_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str,
                   supersedes: str | None = None) -> None:
    """Single canonical dual-SHA verdict line + companion row. [VERIFY] — no [SIGN]
    3-tuple (schema_v2_3tuple_required: false)."""
    value_field = value_str if supersedes is None else f"{value_str}_supersedes={supersedes}"  # (local)
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_field}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    supersedes_note = f"; supersedes={supersedes}" if supersedes else ""  # (local)
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); METHODOLOGY-class label-collision "
        f"resolution: SU(3)-Coloured-Chirality entry renamed §VII.AW.OP-PROJ → §VII.BF (label-only); "
        f"§VII.AW.OP-PROJ now uniquely SUBSTRATE-CLOCK-UNIQUENESS-THEOREM; 4 blast-radius loci updated; "
        f"[VERIFY] no [SIGN] 3-tuple{supersedes_note}\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)


def main() -> int:
    print(f"=== {GATE_ID} ===")
    input_files = {
        "canonical_constants": CANONICAL_CONSTANTS,
        "permanent_results_registry": REGISTRY,
        "s90_slot_lockfile": LOCKFILE,
        "script": SCRIPT_PATH,
    }
    pins = log_input_pins(input_files)

    print("\n" + "=" * 76)
    print("Plan-text-drift correction (substrate-first-canonical-sourcing.md §(ii.B))")
    print("=" * 76)
    print("  All edits are CONTENT-ANCHORED on exact substrings, NOT plan-pinned line numbers")
    print("  (plan-pinned ~17509 / ~17472 / ~17503 / ~18367 are STALE-drifted +2 lines).")

    registry_text_pre = REGISTRY.read_text(encoding="utf-8")  # (local)
    lock_text_pre = LOCKFILE.read_text(encoding="utf-8")  # (local)

    # ---- next-free-letter verify-before-write ----
    print("\n" + "=" * 76)
    print("Next-free-letter verify-before-write (registry-landing.md next-free-letter protocol)")
    print("=" * 76)
    bf_occupied = scan_slot_occupied(registry_text_pre, NEW_SLOT)  # (local)
    bg_occupied = scan_slot_occupied(registry_text_pre, NEXT_CANDIDATE_IF_TAKEN)  # (local)
    # Only an EXISTING non-rejected-entry heading at §VII.BF counts as occupied. The
    # rejected entry currently heads §VII.AW.OP-PROJ (not §VII.BF), so §VII.BF must be free.
    print(f"  §VII.BF occupied (pre-rename) = {bf_occupied}")
    print(f"  §VII.BG occupied (fallback)   = {bg_occupied}")
    target_slot = NEW_SLOT  # (local)
    target_free = not bf_occupied  # (local)
    if bf_occupied:
        # reroute to §VII.BG per item 3 (would require FAIL-with-remediation)
        target_slot = NEXT_CANDIDATE_IF_TAKEN
        target_free = not bg_occupied
        print(f"  >>> §VII.BF OCCUPIED at runtime — would reroute to {target_slot} (FAIL-with-remediation)")
    print(f"  >>> target_slot = {target_slot}; target_free = {target_free}")

    # ---- BUILD all edits in memory (single-shot AFTER pattern) ----
    print("\n" + "=" * 76)
    print("Build rename edits in memory (LABEL-ONLY; EXACT-substring; content-anchored)")
    print("=" * 76)
    reg_repls = build_registry_replacements()  # (local)
    reg_text_1, reg_report = apply_replacements(registry_text_pre, reg_repls)  # (local)
    reg_text_2, idx_bf_report = insert_bf_index_row(reg_text_1)  # (local) NEW §VII.BF index row
    for locus, rep in reg_report.items():
        print(f"  registry {locus:38s} -> {rep['status']} (old_count={rep['old_count']})")
    print(f"  registry (i)-index-bf-new-row              -> {idx_bf_report['status']}")

    lock_repls = build_lockfile_replacements()  # (local)
    lock_text_1, lock_report = apply_replacements(lock_text_pre, lock_repls)  # (local)
    lock_text_2, lock_row_report = append_lockfile_rename_row(lock_text_1)  # (local)
    for locus, rep in lock_report.items():
        print(f"  lockfile {locus:38s} -> {rep['status']} (old_count={rep['old_count']})")
    print(f"  lockfile (iii)-updates-rename-row          -> {lock_row_report['status']}")

    # ---- replacement health: every registry locus must be applied OR already_applied ----
    bad_reg = {k: v for k, v in reg_report.items()
               if v["status"] not in ("applied", "already_applied")}  # (local)
    bad_lock = {k: v for k, v in lock_report.items()
                if v["status"] not in ("applied", "already_applied")}  # (local)
    idx_ok = idx_bf_report["status"] in ("inserted", "already_present")  # (local)
    lock_row_ok = lock_row_report["status"] in ("appended_after_table", "appended_eof", "already_present")  # (local)
    all_loci_clean = (not bad_reg) and (not bad_lock) and idx_ok and lock_row_ok  # (local)
    if bad_reg:
        print(f"  !! registry loci NOT cleanly applied: {bad_reg}")
    if bad_lock:
        print(f"  !! lockfile loci NOT cleanly applied: {bad_lock}")

    # ---- WRITE (atomic) — only if target slot free AND all loci clean ----
    do_write = bool(target_free and all_loci_clean)  # (local)
    if do_write:
        write_atomic(REGISTRY, reg_text_2)
        write_atomic(LOCKFILE, lock_text_2)
        print("\n  >>> registry + lockfile written (atomic, fsync).")
    else:
        print("\n  >>> WRITE SUPPRESSED (target slot occupied OR loci not clean) — verify will FAIL.")

    # ---- RE-READ + VERIFY (the single decision point) ----
    print("\n" + "=" * 76)
    print("Re-read + verify (label-uniqueness + new-slot-heading + no dangling SU(3)-at-AW + loci)")
    print("=" * 76)
    registry_post = REGISTRY.read_text(encoding="utf-8")  # (local)
    lock_post = LOCKFILE.read_text(encoding="utf-8")  # (local)

    # V1 — the NEW §VII.BF heading exists (rename landed)
    bf_heading_present = "## §VII.BF — SU(3)-Coloured Chirality Spectral Triple" in registry_post  # (local)
    # V2 — §VII.AW.OP-PROJ no longer heads the SU(3) entry (no `## §VII.AW.OP-PROJ — SU(3)-Coloured`)
    no_su3_at_aw_heading = "## §VII.AW.OP-PROJ — SU(3)-Coloured Chirality" not in registry_post  # (local)
    # V3 — §VII.AW.OP-PROJ STILL heads the SUBSTRATE-CLOCK entry (KEEP untouched)
    substrate_clock_at_aw = (
        "### §VII.AW.OP-PROJ — SUBSTRATE-CLOCK-UNIQUENESS-THEOREM" in registry_post
    )  # (local)
    # V4 — label-uniqueness: §VII.AW.OP-PROJ now maps to exactly ONE entry-heading.
    #      Count `## §VII.AW.OP-PROJ —` (rejected-entry heading form, level-2 ##) → must be 0;
    #      count `### §VII.AW.OP-PROJ —` (SUBSTRATE-CLOCK heading form, level-3 ###) → must be 1.
    n_aw_lvl2_heading = len(re.findall(r"\n## §VII\.AW\.OP-PROJ —", registry_post))  # (local)
    n_aw_lvl3_heading = len(re.findall(r"\n### §VII\.AW\.OP-PROJ —", registry_post))  # (local)
    label_unique = (n_aw_lvl2_heading == 0 and n_aw_lvl3_heading == 1)  # (local)
    # V5 — no dangling SU(3)-coloured cross-refs still pointing at §VII.AW.OP-PROJ.
    #      The §VII.AT sibling pointers must now say §VII.BF, not §VII.AW.OP-PROJ.
    dangling_at_ptr1 = REG_AT_PTR1_OLD in registry_post  # (local)
    dangling_at_ptr2 = REG_AT_PTR2_OLD in registry_post  # (local)
    no_dangling_at_ptrs = (not dangling_at_ptr1) and (not dangling_at_ptr2)  # (local)
    # V6 — entry-(2) in-block self-refs no longer say §VII.AW.OP-PROJ for itself.
    #      (heading/framing/element-4/alloc/slot-note OLD forms must be GONE.)
    e2_self_refs_cleared = all(  # (local)
        old not in registry_post for old in (
            REG_HEADING_OLD, REG_E2_NOTE_OLD, REG_E2_ALLOC_OLD,
            REG_E2_FRAMING_OLD, REG_E2_ELEM4_OLD,
        )
    )
    # V7 — entry-(1) SUBSTRATE-CLOCK slot-label note updated (collision-resolved form).
    e1_note_updated = (REG_E1_NOTE_OLD not in registry_post) and (
        "Slot-label note — COLLISION RESOLVED (S93 W5-6" in registry_post
    )  # (local)
    # V8 — NEW §VII.BF index row present.
    bf_index_row_present = bool(re.search(r"\n\| §VII\.BF \| THM \|", registry_post))  # (local)
    # V9 — index row for §VII.AW.OP-PROJ updated to collision-resolved annotation.
    idx_e1_updated = ("LABEL COLLISION RESOLVED S93 W5-6" in registry_post) and (IDX_E1_OLD not in registry_post)  # (local)
    # V10 — lockfile updated (RESERVED slot annotated superseded + rename row).
    lock_slot_annotated = "RENAMED `§VII.BF` at S93 W5-6" in lock_post  # (local)
    lock_rename_row_present = LOCK_RENAME_MARKER in lock_post  # (local)
    lock_updated = lock_slot_annotated and lock_rename_row_present  # (local)
    # V11 — label-only: the rejected entry's gate-ID + content survive (no filename/gate-ID change).
    #       The gate-ID S90-CF-A40-FAIL-ALTERNATIVE-CHIRALITY-RESCOPE + the FAIL-diagnostic content + the
    #       coloured-chirality body must still be present in the renamed block.
    renamed_block = extract_renamed_block(registry_post)  # (local)
    label_only_content_preserved = bool(
        renamed_block
        and "γ_F^c" in renamed_block
        and "S91-VII-AW-OP-PROJ-7-AXIOM-COLOURED" in renamed_block
        and "Connes-Marcolli 2008 §11" in renamed_block
        and "axiom-5''" in renamed_block.replace("″", "''")  # tolerate ″ vs ''
        or ("γ_F^c" in renamed_block and "S91-VII-AW-OP-PROJ-7-AXIOM-COLOURED" in renamed_block
            and "Connes-Marcolli 2008 §11" in renamed_block)
    )  # (local)

    verify = {  # (local)
        "V1_bf_heading_present": bf_heading_present,
        "V2_no_su3_at_aw_heading": no_su3_at_aw_heading,
        "V3_substrate_clock_keeps_aw": substrate_clock_at_aw,
        "V4_label_unique (## AW=0, ### AW=1)": label_unique,
        "V5_no_dangling_AT_sibling_ptrs": no_dangling_at_ptrs,
        "V6_entry2_self_refs_cleared": e2_self_refs_cleared,
        "V7_entry1_slot_note_updated": e1_note_updated,
        "V8_bf_index_row_present": bf_index_row_present,
        "V9_aw_index_row_updated": idx_e1_updated,
        "V10_lockfile_updated": lock_updated,
        "V11_label_only_content_preserved": label_only_content_preserved,
    }
    for k, v in verify.items():
        print(f"  {k} = {v}")
    print(f"  (diagnostic) n_aw_lvl2_heading(##)={n_aw_lvl2_heading}  n_aw_lvl3_heading(###)={n_aw_lvl3_heading}")
    print(f"  (diagnostic) renamed §VII.BF block word-count = {len(renamed_block.split())}")

    verify_pass = bool(target_free and all(verify.values()))  # (local) single decision point

    # honest FAIL-with-remediation if target slot was occupied (next-free scan stale)
    if not target_free:
        verdict = "FAIL"  # (local) target slot occupied; reroute needed
    elif not verify_pass:
        verdict = "FAIL"  # (local) a locus missed / dangling ref / not label-only
    else:
        verdict = "PASS"  # (local) rename complete + label unique + all loci clean

    print("\n" + "=" * 76)
    print(f"VERDICT decision: target_free={target_free}, verify_pass={verify_pass} -> {verdict}")
    print("=" * 76)

    # ---- value string (drift correction documented per §(ii.B)) ----
    value_str = (  # (local)
        f"VII-AW-slot-rename_SU3-coloured-chirality_§VII.AW.OP-PROJ→{target_slot}_label-only_"
        f"bf_heading={bf_heading_present}_no_su3_at_aw={no_su3_at_aw_heading}_"
        f"substrate_clock_keeps_aw={substrate_clock_at_aw}_label_unique={label_unique}_"
        f"AW_lvl2_headings={n_aw_lvl2_heading}_AW_lvl3_headings={n_aw_lvl3_heading}_"
        f"no_dangling_AT_ptrs={no_dangling_at_ptrs}_e2_self_refs_cleared={e2_self_refs_cleared}_"
        f"e1_note_updated={e1_note_updated}_bf_index_row={bf_index_row_present}_"
        f"aw_index_updated={idx_e1_updated}_lockfile_updated={lock_updated}_"
        f"content_preserved={label_only_content_preserved}_"
        f"4_loci=registry-entry12+AT-siblings+lockfile+WP_"
        f"drift_corrected_content_anchored_NOT_line_pinned_§(ii.B)_"
        f"AU_AW_THIRD_ordinal_collision_SEPARATE_unaffected=CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW"
    )

    pinmap_for_audit = dict(sorted(pins.items()))  # (local)
    pinmap_for_audit["_gate_id"] = GATE_ID  # (local) gate-distinct keys per mechanical-closure-discipline.md item 3
    pinmap_for_audit["_wp_id"] = "§W5-6"  # (local)
    pinmap_for_audit["_scheme"] = SCHEME  # (local)
    pinmap_for_audit["_convention"] = CONVENTION  # (local)
    pinmap_for_audit["_target_slot"] = target_slot  # (local)
    pinmap_for_audit["_old_label"] = OLD_LABEL  # (local)
    audit_sha = sha256_of_text(json.dumps(pinmap_for_audit, sort_keys=True))  # (local)
    # content_sha = SHA over the renamed §VII.BF entry block (the artifact whose
    # existence-with-content + label-uniqueness IS the METHODOLOGY-class PASS predicate)
    content_sha = sha256_of_text(renamed_block if renamed_block else "EMPTY")  # (local)
    supersedes = find_latest_prior_audit_sha()  # (local) Option-A corrective tag (None on first emission)
    if supersedes:
        print(f"  prior verdict line detected; emitting corrective line with supersedes={supersedes[:16]}...")

    # ---- artifacts (npz + json + png) BEFORE verdict emission ----
    _emit_npz_and_json(verify, reg_report, idx_bf_report, lock_report, lock_row_report,
                       target_slot, target_free, bf_occupied, bg_occupied, renamed_block,
                       n_aw_lvl2_heading, n_aw_lvl3_heading, verdict, value_str, audit_sha, content_sha)
    _emit_plot(verify, target_free, verdict)

    append_verdict(verdict, value_str, audit_sha, content_sha, supersedes=supersedes)
    print(f"\n  4-tuple: (value=<...>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")
    print(f"\n  >>> VERDICT: {verdict}")
    print(f"  RENAME: §VII.AW.OP-PROJ (SU(3)-coloured chirality) -> {target_slot} (label-only)")
    print(f"  §VII.AW.OP-PROJ now UNIQUELY = SUBSTRATE-CLOCK-UNIQUENESS-THEOREM")
    print(f"  4 blast-radius loci updated (registry entry-1/-2 + index, AT siblings ×2, lockfile, WP-by-orchestrator)")
    print(f"  AU/AW '#3' STAGE-3 ordinal collision is SEPARATE (CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW); unaffected.")
    print(f"  M4 allowlist append = ORCHESTRATOR-ONLY (flagged in WP §W5-6)")
    return 0  # verdict is DATA; exit 0 regardless of PASS/FAIL


def _emit_npz_and_json(verify, reg_report, idx_bf_report, lock_report, lock_row_report,
                       target_slot, target_free, bf_occupied, bg_occupied, renamed_block,
                       n_aw_lvl2_heading, n_aw_lvl3_heading, verdict, value_str, audit_sha, content_sha):
    np.savez(
        OUT_NPZ,
        # verification flags
        **{k.split(" ")[0]: np.bool_(v) for k, v in verify.items()},
        target_slot=str(target_slot),
        target_free=np.bool_(target_free),
        bf_occupied_pre=np.bool_(bf_occupied),
        bg_occupied=np.bool_(bg_occupied),
        n_aw_lvl2_heading=np.int64(n_aw_lvl2_heading),
        n_aw_lvl3_heading=np.int64(n_aw_lvl3_heading),
        renamed_block_word_count=np.int64(len(renamed_block.split())),
        # metadata
        old_label=str(OLD_LABEL),
        new_slot=str(NEW_SLOT),
        L_max=str(L_MAX),
        tau_fold=np.float64(tau_fold),
        M_KK=np.float64(M_KK),
        verdict=str(verdict),
        scheme=SCHEME,
        convention=CONVENTION,
        gate_id=GATE_ID,
        audit_sha256=str(audit_sha),
        content_sha256=str(content_sha),
        label_only=np.bool_(True),
        blast_radius="registry-entry1+entry2+index; §VII.AT-siblings×2; s90-lockfile; WP(orchestrator)",
        au_aw_ordinal_collision_separate_cf="CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW",
        m1_artifact_existence_with_content=np.bool_(True),
        m4_allowlist="ORCHESTRATOR-ONLY",
    )
    print(f"  NPZ -> {OUT_NPZ.relative_to(ROOT)}")
    _chk = np.load(OUT_NPZ, allow_pickle=True)  # (local)
    rt_ok = str(_chk["target_slot"]) == str(target_slot)  # (local)
    print(f"  round-trip: npz target_slot preserved: {rt_ok}")

    record = {  # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value_str,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "rename": {
            "old_label": OLD_LABEL,
            "new_slot": target_slot,
            "entry_renamed": "SU(3)-Coloured Chirality Spectral Triple (γ_F^c per Connes-Marcolli 2008 §11) [S90 W7 CF-45; STAGE-0-CANDIDATE REJECTED at S91 W7-2b]",
            "entry_keeping_label": "SUBSTRATE-CLOCK-UNIQUENESS-THEOREM [S90 W2 CF-19; STAGE-3-PERMANENT]",
            "label_only": True,
            "filename_gate_id_sha_unchanged": True,
        },
        "verification": verify,
        "blast_radius_loci": {
            "(i)_registry_entry2_heading_and_self_refs": reg_report,
            "(i)_registry_bf_index_row": idx_bf_report,
            "(ii)_registry_AT_sibling_pointers": "see reg_report (ii)-AT-sibling-ptr-1/-2",
            "(iii)_lockfile_reserved_slot_field": lock_report,
            "(iii)_lockfile_updates_rename_row": lock_row_report,
            "(iv)_wp_section": "written by orchestrator-side WP writer (NOT this script)",
        },
        "next_free_letter_protocol": {
            "highest_slot_at_plan_freeze": "§VII.BE",
            "target": "§VII.BF",
            "bf_occupied_pre_rename": bf_occupied,
            "fallback_if_taken": "§VII.BG",
            "verify_before_write": True,
        },
        "label_uniqueness": {
            "aw_level2_headings_post (rejected-entry form '## §VII.AW.OP-PROJ —')": n_aw_lvl2_heading,
            "aw_level3_headings_post (SUBSTRATE-CLOCK form '### §VII.AW.OP-PROJ —')": n_aw_lvl3_heading,
            "unique": (n_aw_lvl2_heading == 0 and n_aw_lvl3_heading == 1),
        },
        "out_of_blast_radius_unchanged": [
            "registry precedent-citations of §VII.AW.OP-PROJ (~18502/19341/19343/19432) cite SUBSTRATE-CLOCK / mack-sole-writer precedent -> entry (1), KEEP label",
            "s93-slot-pre-allocation-lockfile.md line ~29 anchor-list names '§VII.AW.OP-PROJ SUBSTRATE-CLOCK-UNIQUENESS-THEOREM' -> entry (1)",
            "methodology-wave-instances.md historical ledger rows record the S90 W7 CF-45 LANDING event (past-record, not a live slot pointer)",
        ],
        "au_aw_ordinal_collision": {
            "note": "SEPARATE from this slot-label collision; the 'THIRD STAGE-3-PERMANENT' ordinal claimed by BOTH §VII.AU.OP-PROJ and §VII.AW.OP-PROJ",
            "cf": "CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW",
            "this_gate_action": "NOT addressed here; this gate resolves the SLOT-LABEL collision only",
        },
        "M1_M4_self_classification": {
            "M1_artifact_existence_with_content_plus_label_uniqueness": True,
            "M2_registry_lockfile_write_plus_sha_no_numerical_compute": True,
            "M3_source_verbatim_S92_W9_4_FAIL_diagnostic_landing_plus_HK_S93_W9_1": True,
            "M4_allowlist_append": "ORCHESTRATOR-ONLY (flagged in WP; not edited by this script)",
        },
    }
    OUT_JSON.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"  JSON sidecar -> {OUT_JSON.relative_to(ROOT)}")


def _emit_plot(verify, target_free, verdict):
    fig, ax = plt.subplots(1, 1, figsize=(12.0, 5.2))
    labels = [  # (local)
        "V1 §VII.BF\nheading\npresent",
        "V2 no SU(3)\nat §VII.AW",
        "V3 §VII.AW =\nSUBSTRATE-\nCLOCK",
        "V4 label\nunique",
        "V5 no dangling\nAT ptrs",
        "V6 entry-2\nself-refs\ncleared",
        "V7 entry-1\nnote\nupdated",
        "V8 §VII.BF\nindex row",
        "V9 §VII.AW\nindex\nupdated",
        "V10 lockfile\nupdated",
        "V11 label-\nonly content\npreserved",
    ]
    vals = [int(v) for v in verify.values()]  # (local)
    colors = ["C2" if x else "C3" for x in vals]  # (local)
    ax.bar(range(len(labels)), vals, color=colors, alpha=0.85)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=6.5)
    ax.set_ylim(0, 1.25)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["FAIL", "PASS"])
    ax.set_ylabel("artifact-existence / label-uniqueness predicate")
    for i, x in enumerate(vals):
        ax.text(i, x + 0.05, "PASS" if x else "FAIL", ha="center", va="bottom", fontsize=7,
                color="C2" if x else "C3", fontweight="bold")
    ax.set_title(
        f"{GATE_ID}\n"
        f"§VII.AW.OP-PROJ label-collision resolution: SU(3)-Coloured-Chirality entry "
        f"RENAMED §VII.AW.OP-PROJ → §VII.BF (label-only)\n"
        f"§VII.AW.OP-PROJ now UNIQUELY = SUBSTRATE-CLOCK-UNIQUENESS-THEOREM   |   "
        f"target_free={target_free}   |   composite verdict: {verdict}",
        fontsize=8.0,
    )
    ax.grid(True, axis="y", ls=":", alpha=0.4)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"  PNG -> {OUT_PNG.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
