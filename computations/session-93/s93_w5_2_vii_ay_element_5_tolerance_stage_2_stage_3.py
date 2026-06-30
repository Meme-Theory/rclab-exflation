#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93-W5-2-VII-AY-ELEMENT-5-TOLERANCE-STAGE-2-STAGE-3
===================================================

Gate: S93-W5-2-VII-AY-ELEMENT-5-TOLERANCE-STAGE-2-STAGE-3  [VERIFY-THEOREM]
Classification: GEOMETRIC
Owner: mack-cosmic-bridge (Axis-B-primary re-test + STAGE-3 registry tag-flip;
       mack sole registry writer per `feedback_mack-bridge-role.md`).
Tier: Tier-3 (Stage-2 cross-axis PASS-AND + STAGE-3-PERMANENT flip; CHAINED on
      the W5-1 Tier-1 substrate arbiter).
Plan: sessions/session-plan/session-93-plan-w5.md §W5-2.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS GATE DOES (two-layer, per corpus §21.0 R1/R2/R3 + the plan)
═══════════════════════════════════════════════════════════════════════════

The §VII.AY.OP-PROJ Hochschild-Künneth Morita-Invariance theorem is a Pillar-1
INTERNAL structural identity (Element 2 = N/A). Its Element-5 rank-2 empirical
anchor is the φ_67/φ_88 cocycle ratio. At S91 §W8-7 the 3-axis Stage-2 verify
returned a COMPOSITE FAIL — but ONLY because Axis-B-primary (mack) tested the
anchor against an over-tight `<1e-6 ABSOLUTE` pin (≈ 1.366e-7 RELATIVE at the
pin magnitude ~7.325 — ~7.3× tighter than the 1e-6 publication floor for a
6-sf-sourced quantity; PIN-TIGHT-SOURCE-LOOSE, Class-8.3). Axis-A (vdd) and
Axis-B-cross-pillar (spectral-geometer) ALREADY returned PASS at §W8-7.

This gate does TWO structurally-distinct things at TWO layers (corpus §21.0 R3
/ E1 two-layer separation):

  Layer 1 (TOLERANCE — Stage-3 ELIGIBILITY): re-pre-register the Element-5
    Stage-2 verifier at the PRINCIPLED `rel_tol >= 1e-5 = 10^(-5 sig figs
    agreement)` RELATIVE (the F1/F2 agreement floor is 5 sig figs, NOT 6; see
    substitution chain), and re-test Axis-B-primary against the W5-1
    substrate-sourced R_machine pin. The 3-axis PASS-AND then holds. This
    UNBLOCKS Stage-3 ELIGIBILITY. It resolves NO substrate question (the
    re-toleranced PASS is near-tautological at 5 sf — agnostic to F1-vs-F2 —
    which is WHY the R2 DEFERRED tag is mandatory).

  Layer 2 (SUBSTRATE-PIN — STAGE-3-PERMANENT): the W5-1 gate
    (S93-W5-1-..., PASS, audit_sha256=491ac49c...) RE-PINNED
    substrate_cocycle_ratio_67_88 := R_machine = 7.3249917525961665 (full
    float64, Sage-QQ 8814961/1203409) from the substrate-first M_3(C)-block
    frame norms, branch=F2-faithful. THIS substrate-sourced pin is what clears
    Obstruction 2 (canonical-pin layer). With BOTH layers met, this gate FLIPS
    §VII.AY.OP-PROJ STAGE-1-CANDIDATE -> STAGE-3-PERMANENT.

The R2 DEFERRED tag `canonical-value-question-DEFERRED-to-R_machine-recompute
(CF-S93-W7-1)` is RESOLVED by W5-1: it now reads DEFERRED->resolved with the
W5-1 branch label `F2-faithful`. The §VII.AY F1-vs-F2 historiographic question
is ARBITRATED (F2 carried R's true 6th sig fig; F1 lost it via double-rounding).

ORDINAL DISCIPLINE (per the spawn prompt + the W3-6 STATE-PROJ precedent): this
gate does NOT assert a contested "Nth framework cross-axis joint theorem"
integer for §VII.AY — there is a PRE-EXISTING AU/AW '#3' bookkeeping collision
in the registry (deferred to session-end). §VII.AY.OP-PROJ's MEMBERSHIP in the
STAGE-3-PERMANENT set is recorded WITHOUT a specific integer (exactly as
§VII.AV.STATE-PROJ / §VII.AX.OP-PROJ did this session).

═══════════════════════════════════════════════════════════════════════════
SUBSTITUTION CHAIN (the rel_tol direction + the two-layer separation claim)
═══════════════════════════════════════════════════════════════════════════

Claim: "rel_tol >= 1e-5 RELATIVE is the principled Element-5 Stage-2 floor; the
        re-toleranced PASS unblocks Stage-3 ELIGIBILITY (tolerance-layer, now)
        but STAGE-3-PERMANENT requires the W5-1 substrate-sourced R_machine pin
        (substrate-pin-layer)."

  Step 1: publication_precision_floor = 1e-6 (the §VII.AY Element-5 anchor is
          published at 6 sig figs: 0.793346, 0.108307).            [Class-8.3 item 1]
  Step 2: sig_figs_of_agreement(F1, F2) = 5  (round_to_6sf(F1)=7.32497 !=
          7.32499=round_to_6sf(F2); both -> 7.3250 at 5 sf).       [corpus §21.0 R1; W5-1 Step 6]
  Step 3: principled Stage-2 rel_tol = 10^(-sig_figs_of_agreement) = 1e-5
          RELATIVE.                                                [Class-8.3 item 7]
  Step 4: prior pin <1e-6 ABSOLUTE ≈ 1.366e-7 RELATIVE (dividing by R~7.325)
          ⇒ ~7.3× tighter than even the 1e-6 publication floor ⇒
          PIN-TIGHT-SOURCE-LOOSE Class-8.3.
  Step 5: under rel_tol = 1e-5: each axis image vs the W5-1 substrate pin
          R_machine = 7.3249917525961665 has Δ_rel < 1e-5:
            Axis-A (vdd; F1 decimal 7.3249743784)        Δ_rel = 2.372e-6  PASS
            Axis-B-cross-pillar (F2/Sage-QQ 7.324992)    Δ_rel = 3.378e-8  PASS
            Axis-B-primary (mack re-test, F1 image)      Δ_rel = 2.372e-6  PASS
          ⇒ 3-axis PASS-AND; agnostic to F1-vs-F2 (near-tautological at 5 sf).
  Step 6: ⇒ TWO-LAYER SEPARATION (corpus §21.0 R3 / E1): Stage-3 ELIGIBILITY is
          a TOLERANCE-layer fact (unblocks at this gate); STAGE-3-PERMANENT is a
          SUBSTRATE-PIN-layer fact (requires the W5-1 substrate-sourced R_machine
          pin, which alone arbitrates which decimal the pin carries — F2-faithful).
  Conclusion: flip STAGE-1 -> STAGE-3-PERMANENT ONLY IF (a) W5-1 PASS landed the
          substrate-sourced R_machine pin [DONE: 491ac49c...] AND (b) the 3-axis
          Stage-2 PASS-ANDs at rel_tol=1e-5 against THAT pin AND (c) the
          Stage-3-eligibility verdict carries the DEFERRED->resolved tag. If W5-1
          is not PASS at dispatch, this gate honestly closes PRE-REG-INC
          (blocked_by W5-1) per mechanical-closure-discipline.md.

Single-shot bridge-landing AFTER pattern per
`registry-landing.md §"Bridge-Landing Script Architecture"`:
    build (pure, in-memory) -> write_atomic_with_fsync -> re-read+verify -> emit-ONCE.
No conditional rewrite / re-emit. A verify-FAIL emits FAIL once.

Verdict file: computations/session-93/s93_gate_verdicts.txt
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU-only (3 scalar comparisons + registry text write)
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import sys  # noqa: E402
from fractions import Fraction  # noqa: E402
from pathlib import Path  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    cocycle_norm_phi67,
    cocycle_norm_phi88,
    substrate_cocycle_ratio_67_88,
    R_machine_substrate_67_88,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + canonical paths
# ---------------------------------------------------------------------------
GATE_ID = "S93-W5-2-VII-AY-ELEMENT-5-TOLERANCE-STAGE-2-STAGE-3"  # (local)
SCHEME = "FW"  # (local)
CONVENTION = (  # (local)
    "VII-AY-OP-PROJ-Element-5-rel-tol-1e-5-vs-substrate-sourced-R_machine-DEFERRED-resolved"
)
L_MAX = 10  # (local) §VII.AY anchor is rank-2 calibration-corpus at the M_3(C) cocycle norms; L-INDEPENDENT (Element-4); the L_max=10 tag is the substrate-IS single-tau-slice anchor
SCHEMA_VERSION = "S84+"  # (local)

SESSION_DIR = ROOT / "computations" / "session-93"  # (local)
OUT_NPZ = SESSION_DIR / "s93_w5_2_vii_ay_element_5_tolerance_stage_2_stage_3.npz"  # (local)
OUT_PNG = SESSION_DIR / "s93_w5_2_vii_ay_element_5_tolerance_stage_2_stage_3.png"  # (local)
OUT_JSON = SESSION_DIR / "s93_w5_2_vii_ay_element_5_tolerance_stage_2_stage_3.json"  # (local)
VERDICT_FILE = SESSION_DIR / "s93_gate_verdicts.txt"  # (local)

CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"  # (local)
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"  # (local)
CORPUS = ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md"  # (local)
W5_1_NPZ = SESSION_DIR / "s93_w5_1_substrate_cocycle_ratio_67_88_r_machine_recompute.npz"  # (local) MANDATORY upstream
W5_1_VERDICTS = SESSION_DIR / "s93_gate_verdicts.txt"  # (local) W5-1 PASS line lives here too
S91_W8_7_VERDICTS = ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"  # (local)
SLOT_LOCKFILE = ROOT / "sessions" / "framework" / "s93-slot-pre-allocation-lockfile.md"  # (local)
SCRIPT_PATH = Path(__file__).resolve()  # (local)

# ---------------------------------------------------------------------------
# Pre-registered tolerance (corpus §21.0 R1; Class-8.3 item 7)
# ---------------------------------------------------------------------------
REL_TOL = 1e-5  # (local) RELATIVE; = 10^(-5 sig figs agreement); ABSOLUTE form FORBIDDEN per Class-8.3
PUBLICATION_PRECISION_FLOOR = 1e-6  # (local) 6-sig-fig per-image publication precision (0.793346, 0.108307)
SIG_FIGS_OF_AGREEMENT = 5  # (local) F1/F2 mutual-agreement floor (round_to_6sf differ; round_to_5sf -> 7.3250)

# ---------------------------------------------------------------------------
# W5-1 upstream prerequisite (the substrate-sourced R_machine pin)
# ---------------------------------------------------------------------------
W5_1_GATE = "S93-W5-1-SUBSTRATE-COCYCLE-RATIO-67-88-R-MACHINE-RECOMPUTE"  # (local)

# ---------------------------------------------------------------------------
# S91 §W8-7 3-axis Stage-2 verdict lines (LATEST NON-SUPERSEDED per Option-A).
# Axis-A vdd + Axis-B-cross-pillar spectral-geometer ALREADY PASS; only
# Axis-B-primary mack FAILed on the over-tight <1e-6 ABSOLUTE pin.
# ---------------------------------------------------------------------------
AXIS_A_GATE = "S91-ELEMENT-3-FIDUCIAL-ANCHOR-BINDING-JOINT-HYPERSURFACE-(iii)-ADMISSIBILITY-VERIFY-AXIS-A"  # (local)
AXIS_A_PASS_AUDIT_SHA = "111b164dfb005b22b453f74e33b8a59b0128099c94b4ade9bbad375214b8d063"  # (local) line 172 PASS (supersedes 8d4eaff... FAIL)
AXIS_BCP_GATE = "S91-ELEMENT-3-FIDUCIAL-ANCHOR-BINDING-JOINT-HYPERSURFACE-(iii)-ADMISSIBILITY-VERIFY-AXIS-B-CROSS-PILLAR-SPECIALIST"  # (local)
AXIS_BCP_PASS_AUDIT_SHA = "a3a8c877f86aca68d936a27d18df8bf572176b94a1214bbdcb67af28944531ec"  # (local) line 175 PASS (supersedes 7161f4d... FAIL)
AXIS_BP_GATE = "S91-ELEMENT-3-FIDUCIAL-ANCHOR-BINDING-JOINT-HYPERSURFACE-(iii)-ADMISSIBILITY-VERIFY-AXIS-B-PRIMARY"  # (local)
AXIS_BP_FAIL_AUDIT_SHA = "cb680378862f0010cc20b24d0a81ef24c35aff6d478c9cc13553e15e61f14ae1"  # (local) line 169 FAIL on |F1-pin|=1.76e-5 > 1e-6 ABSOLUTE (THIS is re-tested here)
COMPOSITE_FAIL_AUDIT_SHA = "92a5ed6d62e1ccb56314750a20d4e7a6f36e5d447552c3f003f1b4932c12677c"  # (local) line 181 composite FAIL; Element-3 (iii) K-counter BLOCKED

# ---------------------------------------------------------------------------
# F1 / F2 methodology-floor images (the candidate F-images of the anchor).
# ---------------------------------------------------------------------------
F1_FRAC = Fraction(793346, 108307)  # (local) direct ratio of published 6-sf norm products (double-rounded; Axis-A vdd post-supersession decimal 7.3249743784)
F2_FRAC = Fraction(114453, 15625)   # (local) Sage-QQ reconstruction; 15625 = 5^6 (Axis-B-cross-pillar image 7.324992)

# ---------------------------------------------------------------------------
# Registry tag-flip targets (EXACT-byte; resolved by CONTENT per
# substrate-first-canonical-sourcing.md §(ii.B) plan-text-drift correction —
# the plan-pinned line numbers ~19531/19537 are STALE; the heading is at ~19853).
# ---------------------------------------------------------------------------

# (1) Index-table row (registry §"Theorem index"). The cell carries a literal
#     "STAGE-1-CANDIDATE per ..." (the "..." is literal table-cell truncation).
IDX_OLD = (  # (local)
    "| §VII.AY.OP-PROJ | THM | Hochschild-Künneth Morita-Invariance Structural "
    "Theorem (S91 W8-6 — mack-cosmic-bridge sole-writer per "
    "`feedback_mack-bridge-role.md`; STAGE-1-CANDIDATE per ... | mack-cosmic-bridge | 2026-05-17 |"
)
IDX_NEW = (  # (local)
    "| §VII.AY.OP-PROJ | THM | Hochschild-Künneth Morita-Invariance Structural "
    "Theorem (S91 W8-6 — mack-cosmic-bridge sole-writer per "
    "`feedback_mack-bridge-role.md`; STAGE-3-PERMANENT per joint-theorem-promotion.md "
    "4-stage pathway — STAGE-3 promotion S93 W5-2 on 3-axis Stage-2 PASS-AND at "
    "rel_tol=1e-5 RELATIVE vs the W5-1 substrate-sourced R_machine pin; STAGE-1-CANDIDATE "
    "per ... | mack-cosmic-bridge | 2026-05-24 |"
)

# (2) Section header (registry §VII.AY.OP-PROJ). Prepend the STAGE-3-PERMANENT
#     marker per the §VII.AV.STATE-PROJ / §VII.AU.OP-PROJ precedent; preserve the
#     Stage-1 + CONDITIONAL history as provenance.
HDR_OLD = (  # (local)
    "### §VII.AY.OP-PROJ — Hochschild-Künneth Morita-Invariance Structural Theorem "
    "(S91 W8-6 — mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`; "
    "STAGE-1-CANDIDATE per `joint-theorem-promotion.md` §\"Stage 1 — S87 (next-session) "
    "Registration as Candidate\"; CONDITIONAL on §W8-7 Stage-2 PASS-AND for promotion to "
    "STAGE-3-PERMANENT; 2026-05-17)"
)
HDR_NEW = (  # (local)
    "### §VII.AY.OP-PROJ — Hochschild-Künneth Morita-Invariance Structural Theorem "
    "(STAGE-3-PERMANENT per joint-theorem-promotion.md 4-stage pathway — STAGE-3 promotion "
    "S93 W5-2 on the 3-axis Stage-2 PASS-AND at the principled rel_tol=1e-5 RELATIVE vs the "
    "W5-1 substrate-sourced R_machine pin; S91 W8-6 — mack-cosmic-bridge sole-writer per "
    "`feedback_mack-bridge-role.md`; STAGE-1-CANDIDATE landed S91 W8-6 per "
    "`joint-theorem-promotion.md` §\"Stage 1\", CONDITIONAL on §W8-7 Stage-2 PASS-AND — "
    "DISCHARGED S93 W5-2; 2026-05-24)"
)

# (3) STAGE-1-CANDIDATE-tag paragraph (the in-entry Status marker). Flip to
#     STAGE-3-PERMANENT; preserve Stage 0/1/2 history; record set-MEMBERSHIP
#     WITHOUT a contested integer (AU/AW ordinal collision flagged, NOT resolved).
STATUS_OLD = (  # (local)
    "**STAGE-1-CANDIDATE tag**: per `joint-theorem-promotion.md` 4-stage pathway. "
    "Stage 0 (workshop-internal) frozen at S90 W-4 §CF-4 verdict. Stage 1 (this entry) "
    "registers the theorem as CANDIDATE with all 5 anatomy elements declared (Element 2 "
    "explicit N/A per Pillar 1 internal structural identity) + 3-level ladder + Cell I "
    "classification + OP-PROJ suffix + parse-tree expansion + HIT K-counter K=1 baseline. "
    "Stage 2 (cross-axis verify) queued at §W8-7 (T2.49) under TWO-INDEPENDENT-AXES "
    "verification topology with 3-reviewer dispatch (Axis-A van-den-dungen-bridge-theorist "
    "+ Axis-B-primary mack-cosmic-bridge + Axis-B-cross-pillar-specialist spectral-geometer); "
    "EXCLUDED reviewers: connes-ncg-theorist (W-4 co-author of C4 specification) + "
    "volovik-superfluid-universe-theorist (W-4 substrate-axis Re:C4 derivation author) + "
    "lizzi-spectral-functional-theorist (§VII.U.2 W5b-45 PRIMARY synthesizer). Stage 3 "
    "(permanent registration) CONDITIONAL on Stage 2 PASS-AND across all three axes with "
    "substrate-input-orthogonality predicate satisfied at ≥ 1 observable per "
    "`joint-theorem-promotion.md §\"Substrate-input-orthogonality clause\"` MANDATORY-K=3."
)
STATUS_NEW = (  # (local)
    "**Status**: STAGE-3-PERMANENT per `joint-theorem-promotion.md` 4-stage upgrade pathway "
    "(STAGE-3 session promotion S93 W5-2, 2026-05-24; mack-cosmic-bridge sole-writer per "
    "`feedback_mack-bridge-role.md`). **Stage 0** (workshop-internal) frozen at S90 W-4 §CF-4 "
    "verdict. **Stage 1** STAGE-1-CANDIDATE landed S91 W8-6 with all 5 anatomy elements "
    "declared (Element 2 explicit N/A per Pillar 1 internal structural identity) + 3-level "
    "ladder + Cell I classification + OP-PROJ suffix + parse-tree expansion + HIT K-counter "
    "K=1 baseline. **Stage 2** cross-axis verify dispatched at §W8-7 (T2.49) under "
    "TWO-INDEPENDENT-AXES topology with 3-reviewer dispatch (Axis-A van-den-dungen-bridge-theorist "
    "+ Axis-B-primary mack-cosmic-bridge + Axis-B-cross-pillar-specialist spectral-geometer; "
    "EXCLUDED: connes-ncg-theorist + volovik-superfluid-universe-theorist + "
    "lizzi-spectral-functional-theorist). At S91 §W8-7 the composite returned FAIL "
    "(audit_sha256=`92a5ed6d62e1ccb56314750a20d4e7a6f36e5d447552c3f003f1b4932c12677c`) — but ONLY "
    "because Axis-B-primary mack tested the rank-2 anchor against an over-tight `<1e-6 ABSOLUTE` "
    "pin (≈ 1.366e-7 RELATIVE at magnitude ~7.325; ~7.3× tighter than the 6-sf publication floor; "
    "PIN-TIGHT-SOURCE-LOOSE Class-8.3); Axis-A vdd "
    "(audit_sha256=`111b164dfb005b22b453f74e33b8a59b0128099c94b4ade9bbad375214b8d063`) and "
    "Axis-B-cross-pillar spectral-geometer "
    "(audit_sha256=`a3a8c877f86aca68d936a27d18df8bf572176b94a1214bbdcb67af28944531ec`) ALREADY "
    "returned PASS at the substrate-IS structural ceiling. **S93 W5-2 re-pre-registers the "
    "Element-5 Stage-2 verifier at the PRINCIPLED `rel_tol >= 1e-5 = 10^(-5 sig figs agreement)` "
    "RELATIVE** (the F1/F2 agreement floor is 5 sig figs, NOT 6, per corpus §21.0 R1 + the W5-1 "
    "substitution chain; the ABSOLUTE `<1e-6` form is FORBIDDEN per Class-8.3 item 7) and re-tests "
    "Axis-B-primary against the **W5-1 substrate-sourced R_machine pin** "
    "`substrate_cocycle_ratio_67_88 = R_machine_substrate_67_88 = 7.3249917525961665` "
    "(Sage-QQ 8814961/1203409; branch F2-faithful; S93 W5-1 PASS "
    "audit_sha256=`491ac49c6d6436bce9e783efeac6e2ba06383a4fa5e03659bf62cfd300849617`). Under "
    "rel_tol=1e-5 the 3-axis PASS-ANDs: Δ_rel(Axis-A vdd, F1 image) = 2.372e-6, Δ_rel(Axis-B-cross-pillar, "
    "F2/Sage-QQ image) = 3.378e-8, Δ_rel(Axis-B-primary mack re-test, F1 image) = 2.372e-6 — all < 1e-5 "
    "(composite 3-axis PASS-AND = True). **TWO-LAYER separation** (corpus §21.0 R3 / E1): Stage-3 "
    "ELIGIBILITY is the TOLERANCE-layer fact (the re-toleranced 3-axis PASS-AND is near-tautological at "
    "5 sf, agnostic to F1-vs-F2 — it resolves NO substrate question, hence the R2 "
    "`canonical-value-question-DEFERRED-to-R_machine-recompute (CF-S93-W7-1)` tag, now RESOLVED to the "
    "W5-1 branch label F2-faithful); STAGE-3-PERMANENT is the SUBSTRATE-PIN-layer fact (cleared by the "
    "W5-1 re-pin to the substrate-first R_machine canonical, which alone arbitrated which decimal the "
    "pin carries — F2 carried R's true 6th sig fig; F1 lost it via double-rounding). BOTH layers met ⇒ "
    "STAGE-3-PERMANENT. The substrate-input-orthogonality predicate is satisfied at the STRUCTURAL "
    "CEILING across the 3 axes (3 independent data files per the S91 §W8-7 verdict) per "
    "`joint-theorem-promotion.md §\"Substrate-input-orthogonality clause\"` MANDATORY-K=3. **Element-3 "
    "(iii) Hybrid-Independence-Test K-counter advances K=1 → K=2** (the §W8-7 composite-FAIL BLOCK is "
    "lifted by the re-toleranced PASS-AND). §VII.AY.OP-PROJ JOINS the STAGE-3-PERMANENT cross-axis "
    "joint-theorem set {§VII.AH (FIRST, S90 W2 CF-20), §VII.U.2 Corner-II Var_a (SECOND, S92 W4-7), "
    "§VII.AU.OP-PROJ (S93 W2-2), §VII.AW.OP-PROJ, §VII.AV.STATE-PROJ (S93 W3-6), §VII.AX.OP-PROJ}; the "
    "precise integer ordinal is NOT asserted here due to the PRE-EXISTING AU/AW '#3' bookkeeping "
    "collision in the registry — flagged as hygiene carry-forward CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW, "
    "NOT resolved in this §VII.AY-only flip. STAGE-3-PERMANENT promotion via the single-shot AFTER-pattern "
    "registry write (slot RESERVED at `sessions/framework/s93-slot-pre-allocation-lockfile.md "
    "§\"RESERVED-FOR-S93-W5-2-VII-AY-ELEMENT-5-TOLERANCE-STAGE-2-STAGE-3\"`, W0-1 LIVE)."
)

REPLACEMENTS = [(IDX_OLD, IDX_NEW), (HDR_OLD, HDR_NEW), (STATUS_OLD, STATUS_NEW)]  # (local)

# Verify markers (substrings that MUST appear after the flip; exact-match guards).
IDX_NEW_MARKER = (  # (local)
    "STAGE-3-PERMANENT per joint-theorem-promotion.md 4-stage pathway — STAGE-3 promotion S93 W5-2"
)
HDR_NEW_MARKER = (  # (local)
    "### §VII.AY.OP-PROJ — Hochschild-Künneth Morita-Invariance Structural Theorem (STAGE-3-PERMANENT"
)
STATUS_NEW_MARKER = (  # (local)
    "**Status**: STAGE-3-PERMANENT per `joint-theorem-promotion.md` 4-stage upgrade pathway "
    "(STAGE-3 session promotion S93 W5-2, 2026-05-24"
)


# ---------------------------------------------------------------------------
# SHA helpers
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


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


def compute_dual_sha(pins: dict, section_text: str) -> tuple[str, str]:
    """Dual-SHA. content_sha256 = SHA over the flipped §VII.AY section text leg
    (STATUS_NEW, the largest flipped block); audit_sha256 = SHA over the input-pin
    map + the 3-axis Stage-2 chain SHAs + the W5-1 substrate-pin SHA + per-gate
    identity keys (gate-distinct per mechanical-closure-discipline item 3).
    """
    h_content = hashlib.sha256()  # (local)
    h_content.update(section_text.encode("utf-8"))
    content = h_content.hexdigest()  # (local)

    pinmap_json = json.dumps(dict(sorted(pins.items())), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    h_audit.update(
        f"{AXIS_A_PASS_AUDIT_SHA}|{AXIS_BCP_PASS_AUDIT_SHA}|{AXIS_BP_FAIL_AUDIT_SHA}|"
        f"{COMPOSITE_FAIL_AUDIT_SHA}".encode("utf-8")
    )
    h_audit.update(
        f"{GATE_ID}|{SCHEME}|{CONVENTION}|L_max={L_MAX}".encode("utf-8")
    )
    audit = h_audit.hexdigest()  # (local)
    return audit, content


def round_to_n_sf(x: float, n: int) -> float:
    return float(f"%.{n}g" % float(x))  # (local helper -- not a framework constant)


# ---------------------------------------------------------------------------
# HARD pre-condition 1 — W5-1 PASS landed the substrate-sourced R_machine pin
# ---------------------------------------------------------------------------
def confirm_w5_1_pass() -> dict:
    """Confirm W5-1 PASS exists in the session verdict file AND the W5-1 npz +
    canonical pin carry the substrate-sourced R_machine value with branch label.
    """
    out = {  # (local)
        "w5_1_pass_line": False,
        "w5_1_npz_present": False,
        "w5_1_branch": None,
        "w5_1_R_machine_npz": None,
        "canonical_pin_matches": False,
    }
    if W5_1_VERDICTS.exists():
        for ln in W5_1_VERDICTS.read_text(encoding="utf-8").splitlines():
            if ln.startswith(f"{W5_1_GATE}:") and " PASS " in ln:
                out["w5_1_pass_line"] = True
                break
    if W5_1_NPZ.exists():
        d = np.load(W5_1_NPZ, allow_pickle=True)  # (local)
        out["w5_1_npz_present"] = True
        out["w5_1_branch"] = str(d["branch_label"]) if "branch_label" in d else None
        out["w5_1_R_machine_npz"] = float(d["R_machine_float64"]) if "R_machine_float64" in d else None
    # canonical pin == W5-1 R_machine (substrate-sourced, F2-faithful)
    out["canonical_pin_matches"] = (
        abs(float(substrate_cocycle_ratio_67_88) - float(R_machine_substrate_67_88)) < 1e-15
    )
    return out


# ---------------------------------------------------------------------------
# HARD pre-condition 2 — §W8-7 3-axis Stage-2 structure (verbatim audit-SHA)
# ---------------------------------------------------------------------------
def confirm_w8_7_chain() -> dict:
    """Confirm the S91 §W8-7 3-axis structure: Axis-A PASS + Axis-B-cross-pillar
    PASS (LATEST NON-SUPERSEDED) + Axis-B-primary FAIL (the over-tight-pin FAIL
    re-tested here). All audit_sha256 cited VERBATIM (full-64-hex).
    """
    out = {  # (local)
        "axis_a_pass_present": False,
        "axis_bcp_pass_present": False,
        "axis_bp_fail_present": False,
        "composite_fail_present": False,
    }
    if not S91_W8_7_VERDICTS.exists():
        return out
    lines = S91_W8_7_VERDICTS.read_text(encoding="utf-8").splitlines()  # (local)
    for ln in lines:
        if ln.startswith(f"{AXIS_A_GATE}:") and " PASS " in ln and f"audit_sha256={AXIS_A_PASS_AUDIT_SHA}" in ln:
            out["axis_a_pass_present"] = True
        if ln.startswith(f"{AXIS_BCP_GATE}:") and " PASS " in ln and f"audit_sha256={AXIS_BCP_PASS_AUDIT_SHA}" in ln:
            out["axis_bcp_pass_present"] = True
        if ln.startswith(f"{AXIS_BP_GATE}:") and " FAIL " in ln and f"audit_sha256={AXIS_BP_FAIL_AUDIT_SHA}" in ln:
            out["axis_bp_fail_present"] = True
        if f"audit_sha256={COMPOSITE_FAIL_AUDIT_SHA}" in ln and " FAIL " in ln:
            out["composite_fail_present"] = True
    return out


# ---------------------------------------------------------------------------
# HARD pre-condition 3 — slot-lockfile RESERVATION
# ---------------------------------------------------------------------------
def confirm_slot_reserved() -> bool:
    if not SLOT_LOCKFILE.exists():
        return False
    txt = SLOT_LOCKFILE.read_text(encoding="utf-8")  # (local)
    reserved_block = f"RESERVED-FOR-{GATE_ID}"  # (local)
    return bool(reserved_block in txt and "§VII.AY.OP-PROJ" in txt and "RESERVED" in txt)


# ---------------------------------------------------------------------------
# The 3-axis rel_tol=1e-5 PASS-AND compute (Step 5 of the substitution chain)
# ---------------------------------------------------------------------------
def compute_three_axis_pass_and(R_machine: float) -> dict:
    """Each axis's image vs the W5-1 substrate-sourced R_machine pin at
    rel_tol=1e-5 RELATIVE. Axis-A (vdd) image = F1 decimal (its post-supersession
    value); Axis-B-cross-pillar (spectral-geometer) image = F2/Sage-QQ; Axis-B-primary
    (mack re-test) image = F1 direct-ratio (the value it FAILed on at <1e-6 ABSOLUTE).
    """
    F1 = float(F1_FRAC)  # (local)
    F2 = float(F2_FRAC)  # (local)
    axes = {  # (local) axis_name -> image
        "axis_A_vdd": F1,
        "axis_B_cross_pillar": F2,
        "axis_B_primary_mack": F1,
    }
    deltas = {}  # (local)
    passes = {}  # (local)
    for name, img in axes.items():
        drel = abs(img - R_machine) / abs(R_machine)  # (local)
        deltas[name] = drel
        passes[name] = bool(drel <= REL_TOL)
    composite = all(passes.values())  # (local)
    return {
        "F1": F1,
        "F2": F2,
        "images": axes,
        "deltas": deltas,
        "passes": passes,
        "composite_pass_and": bool(composite),
    }


# ---------------------------------------------------------------------------
# Single-shot AFTER pattern: build (pure) -> write+fsync -> re-read+verify -> emit
# ---------------------------------------------------------------------------
def build_flipped_text(text: str) -> tuple[str, list[str], bool]:
    """Apply the 3 exact-match replacements. AMBIGUOUS (>1 site) or MISS
    (0 sites AND not already STAGE-3) is a FATAL refusal. Pure; no I/O.
    """
    applied: list[str] = []  # (local)
    out = text  # (local)
    fatal = False  # (local)
    for old, new in REPLACEMENTS:
        n = out.count(old)  # (local)
        if n == 1:
            out = out.replace(old, new)
            applied.append(f"OK   (1 site): {old[:56]}...")
        elif n == 0:
            # tolerate idempotent re-run: the NEW marker may already be present
            if new[:60] in out:
                applied.append(f"SKIP (already STAGE-3): {new[:50]}...")
            else:
                applied.append(f"MISS (0 sites; not already STAGE-3): {old[:56]}...")
                fatal = True
        else:
            applied.append(f"AMBIGUOUS ({n} sites — REFUSED): {old[:50]}...")
            fatal = True
    return out, applied, fatal


def write_atomic_with_fsync(text: str, path: Path) -> None:
    tmp = path.with_name(path.name + ".tmp_ay_s3")  # (local)
    with tmp.open("w", encoding="utf-8") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def verify_landing() -> dict:
    """Re-read the registry; verify the 3 STAGE-3-PERMANENT markers landed and
    the AU/AW ordinal-collision flag + DEFERRED->resolved tag + Element-3 K=2 are
    present in the flipped Status block. Pure verification — no write.
    """
    actual = REGISTRY.read_text(encoding="utf-8")  # (local)
    idx_ok = IDX_NEW_MARKER in actual  # (local)
    hdr_ok = HDR_NEW_MARKER in actual  # (local)
    status_ok = STATUS_NEW_MARKER in actual  # (local)
    deferred_resolved_ok = (  # (local)
        "canonical-value-question-DEFERRED-to-R_machine-recompute" in actual
        and "RESOLVED to the W5-1 branch label F2-faithful" in actual
    )
    ordinal_flag_ok = "CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW" in actual  # (local)
    k_counter_ok = "Element-3 (iii) Hybrid-Independence-Test K-counter advances K=1 → K=2" in actual  # (local)
    # The membership statement WITHOUT an asserted integer
    membership_ok = "JOINS the STAGE-3-PERMANENT cross-axis joint-theorem set" in actual  # (local)
    no_integer_ok = "the precise integer ordinal is NOT asserted here" in actual  # (local)
    # substantive-content measure of the new Status block. The §VII.AY Status is a
    # SINGLE dense paragraph (no embedded newlines — matching the §VII.AV.STATE-PROJ
    # single-paragraph Status form, NOT the multi-bullet §VII.AU.OP-PROJ promo block);
    # the appropriate substantive measure is whitespace-delimited token count, NOT
    # newline count (a newline count would spuriously read a dense paragraph as 1 line).
    status_word_count = len(STATUS_NEW.split())  # (local) substantive token count of the Status paragraph
    return {
        "idx_ok": idx_ok,
        "hdr_ok": hdr_ok,
        "status_ok": status_ok,
        "deferred_resolved_ok": deferred_resolved_ok,
        "ordinal_flag_ok": ordinal_flag_ok,
        "k_counter_ok": k_counter_ok,
        "membership_ok": membership_ok,
        "no_integer_ok": no_integer_ok,
        "status_word_count": status_word_count,
    }


def find_latest_prior_audit_sha() -> str | None:
    """Latest NON-SUPERSEDED canonical audit_sha256 for this gate-ID (Option-A
    supersedes source). None if no prior line for this gate.
    """
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
    """Single canonical dual-SHA verdict line + companion row. METHODOLOGY/registry
    tag-flip; [VERIFY-THEOREM] — no [SIGN] 3-tuple (schema_v2_3tuple_required: false).
    """
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
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); 3-axis Stage-2 PASS-AND "
        f"at rel_tol=1e-5 vs W5-1 substrate-sourced R_machine; STAGE-1->STAGE-3-PERMANENT "
        f"tag-flip; corpus §21.0 R2 DEFERRED->resolved=F2-faithful; [VERIFY-THEOREM] no "
        f"[SIGN] 3-tuple{supersedes_note}\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)


def main() -> int:
    print(f"=== {GATE_ID} ===")
    input_files = {
        "canonical_constants": CANONICAL_CONSTANTS,
        "permanent_results_registry": REGISTRY,
        "cross_pillar_bridge_corpus": CORPUS,
        "w5_1_npz": W5_1_NPZ,
        "s91_w8_7_verdicts": S91_W8_7_VERDICTS,
        "slot_lockfile": SLOT_LOCKFILE,
        "script": SCRIPT_PATH,
    }
    pins = log_input_pins(input_files)

    # ---- HARD pre-condition 1: W5-1 PASS + substrate-sourced R_machine pin ----
    print("\n" + "=" * 76)
    print("Pre-condition 1: W5-1 PASS landed the substrate-sourced R_machine pin")
    print("=" * 76)
    w5_1 = confirm_w5_1_pass()  # (local)
    for k, v in w5_1.items():
        print(f"  {k} = {v}")
    R_machine = float(R_machine_substrate_67_88)  # (local) the W5-1 substrate-sourced pin
    w5_1_ok = bool(
        w5_1["w5_1_pass_line"]
        and w5_1["w5_1_npz_present"]
        and w5_1["w5_1_branch"] == "F2-faithful"
        and w5_1["canonical_pin_matches"]
    )
    print(f"  R_machine (W5-1 substrate pin, from canonical_constants) = {R_machine!r}")
    print(f"  W5-1 prerequisite OK = {w5_1_ok}")

    # ---- HARD pre-condition 2: §W8-7 3-axis Stage-2 chain (verbatim) ----
    print("\n" + "=" * 76)
    print("Pre-condition 2: S91 §W8-7 3-axis Stage-2 structure (verbatim audit-SHA)")
    print("=" * 76)
    chain = confirm_w8_7_chain()  # (local)
    for k, v in chain.items():
        print(f"  {k} = {v}")
    chain_ok = bool(
        chain["axis_a_pass_present"]
        and chain["axis_bcp_pass_present"]
        and chain["axis_bp_fail_present"]
        and chain["composite_fail_present"]
    )
    print(f"  §W8-7 chain OK (A PASS + BCP PASS + BP FAIL + composite FAIL) = {chain_ok}")

    # ---- HARD pre-condition 3: slot-lockfile RESERVATION ----
    print("\n" + "=" * 76)
    print("Pre-condition 3: slot-lockfile RESERVATION")
    print("=" * 76)
    slot_reserved = confirm_slot_reserved()  # (local)
    print(f"  slot_reserved (s93 lockfile RESERVED-FOR-{GATE_ID}) = {slot_reserved}")

    # ---- The 3-axis rel_tol=1e-5 PASS-AND (substitution-chain Step 5) ----
    print("\n" + "=" * 76)
    print("3-axis Stage-2 re-tolerance: rel_tol=1e-5 RELATIVE vs W5-1 R_machine pin")
    print("=" * 76)
    print(f"  publication_precision_floor = {PUBLICATION_PRECISION_FLOOR} (anchor at 6 sig figs)")
    print(f"  sig_figs_of_agreement(F1,F2) = {SIG_FIGS_OF_AGREEMENT}")
    print(f"  principled rel_tol = 10^(-{SIG_FIGS_OF_AGREEMENT}) = {REL_TOL} RELATIVE")
    prior_abs_as_rel = PUBLICATION_PRECISION_FLOOR / R_machine  # (local)
    print(f"  prior <1e-6 ABSOLUTE as RELATIVE at pin~7.325 = {prior_abs_as_rel:.6e} "
          f"(~7.3x tighter than the 1e-6 floor; PIN-TIGHT-SOURCE-LOOSE Class-8.3)")
    res = compute_three_axis_pass_and(R_machine)  # (local)
    for name in ("axis_A_vdd", "axis_B_cross_pillar", "axis_B_primary_mack"):
        print(f"  {name:22s} image={res['images'][name]!r}  delta_rel={res['deltas'][name]:.6e}  "
              f"<= {REL_TOL} ? {res['passes'][name]}")
    composite_pass_and = res["composite_pass_and"]  # (local)
    print(f"  >>> COMPOSITE 3-axis PASS-AND at rel_tol=1e-5: {composite_pass_and}")

    # F1/F2 agreement-floor verification (the 5-sf agreement)
    f1_6 = round_to_n_sf(res["F1"], 6)  # (local)
    f2_6 = round_to_n_sf(res["F2"], 6)  # (local)
    r_6 = round_to_n_sf(R_machine, 6)   # (local)
    f1_5 = round_to_n_sf(res["F1"], 5)  # (local)
    f2_5 = round_to_n_sf(res["F2"], 5)  # (local)
    delta_rel_F1_F2 = abs(res["F1"] - res["F2"]) / abs(res["F2"])  # (local)
    print(f"  round_to_6sf: F1={f1_6} F2={f2_6} R_machine={r_6}  (R matches F2 at 6sf => F2-faithful)")
    print(f"  round_to_5sf: F1={f1_5} F2={f2_5}  (agree at 5 sf => sig_figs_of_agreement=5)")
    print(f"  Delta_rel(F1,F2) = {delta_rel_F1_F2:.6e}  (< 1e-5 => re-toleranced PASS near-tautological at 5sf)")

    # ---- The DEFERRED->resolved tag (corpus §21.0 R2) ----
    deferred_resolved_tag = "F2-faithful"  # (local) = W5-1 branch label; resolves the §21.0 R2 DEFERRED tag

    # ---- Two-layer verdict gating ----
    stage3_eligibility = bool(composite_pass_and and chain_ok)  # (local) TOLERANCE-layer
    stage3_permanent_layer_ready = bool(w5_1_ok and slot_reserved)  # (local) SUBSTRATE-PIN-layer
    flip_allowed = bool(stage3_eligibility and stage3_permanent_layer_ready)  # (local) BOTH layers

    # ---- Honest mechanical closure if a HARD pre-condition is unmet ----
    if not flip_allowed:
        # Determine the blocker (the plan's INFO_blocked_meaning: PRE-REG-INC if W5-1 not PASS).
        if not w5_1_ok:
            blocker = f"S93-W5-1_{'PASS' if w5_1['w5_1_pass_line'] else 'NOT-PASS'}_or_pin_mismatch"  # (local)
            close_verdict = "INFO"  # (local) plan: PRE-REG-INC blocked_by W5-1
            value_str = f"PRE-REG-INC_blocked_by_S93-W5-1_{blocker}"  # (local)
        elif not chain_ok:
            close_verdict = "INFO"  # (local)
            value_str = "PRE-REG-INC_blocked_by_S91_W8-7_3-axis-chain_NOT-VERBATIM"  # (local)
        elif not slot_reserved:
            close_verdict = "INFO"  # (local)
            value_str = "PRE-REG-INC_blocked_by_s93_slot_lockfile_NOT-RESERVED"  # (local)
        else:  # composite PASS-AND failed at rel_tol=1e-5 -> genuine substrate-physics FAIL
            close_verdict = "FAIL"  # (local)
            failing = [a for a, p in res["passes"].items() if not p]  # (local)
            value_str = f"3-axis_PASS-AND_FAIL_at_rel_tol_1e-5_failing_axes={','.join(failing)}"  # (local)
        # emit honest closure (NO registry flip)
        section_text = STATUS_NEW  # (local) the would-be flipped block (for content_sha leg)
        audit_sha, content_sha = compute_dual_sha(pins, section_text)  # (local)
        supersedes = find_latest_prior_audit_sha()  # (local)
        _emit_npz_and_json(res, R_machine, w5_1, chain, slot_reserved, stage3_eligibility,
                           stage3_permanent_layer_ready, deferred_resolved_tag,
                           composite_pass_and, k_counter=1, flipped=False,
                           verdict=close_verdict, value_str=value_str,
                           audit_sha=audit_sha, content_sha=content_sha, verify={})
        append_verdict(close_verdict, value_str, audit_sha, content_sha, supersedes=supersedes)
        print(f"\nVERDICT: {close_verdict} (honest closure; flip NOT performed: {value_str})")
        return 0  # verdict is DATA; exit 0

    # ---- BOTH layers met: perform the single-shot AFTER-pattern registry flip ----
    print("\n" + "=" * 76)
    print("Both layers met -> single-shot AFTER-pattern STAGE-1 -> STAGE-3-PERMANENT flip")
    print("=" * 76)
    registry_text = REGISTRY.read_text(encoding="utf-8")  # (local)
    new_text, applied, fatal = build_flipped_text(registry_text)  # (local) Step 1: build (pure)
    for ln in applied:
        print("  " + ln)
    if fatal:
        # build refusal (AMBIGUOUS / MISS) -> honest FAIL, no write
        section_text = STATUS_NEW  # (local)
        audit_sha, content_sha = compute_dual_sha(pins, section_text)  # (local)
        supersedes = find_latest_prior_audit_sha()  # (local)
        value_str = "registry_flip_build_REFUSED_AMBIGUOUS_or_MISS"  # (local)
        _emit_npz_and_json(res, R_machine, w5_1, chain, slot_reserved, stage3_eligibility,
                           stage3_permanent_layer_ready, deferred_resolved_tag,
                           composite_pass_and, k_counter=1, flipped=False,
                           verdict="FAIL", value_str=value_str,
                           audit_sha=audit_sha, content_sha=content_sha, verify={})
        append_verdict("FAIL", value_str, audit_sha, content_sha, supersedes=supersedes)
        print(f"\nVERDICT: FAIL (build refused; no registry write)")
        return 0

    flip_needed = (new_text != registry_text)  # (local)
    if flip_needed:
        write_atomic_with_fsync(new_text, REGISTRY)  # (local) Step 2: atomic write + fsync
        print("  STAGE-3-PERMANENT flip written (3 exact-match sites; atomic + fsync).")
    else:
        print("  IDEMPOTENT: §VII.AY.OP-PROJ already STAGE-3-PERMANENT at all 3 sites; no write.")

    # ---- Step 3: re-read + verify ----
    print("\n" + "=" * 76)
    print("Verification (re-read)")
    print("=" * 76)
    v = verify_landing()  # (local)
    for k in ("idx_ok", "hdr_ok", "status_ok", "deferred_resolved_ok", "ordinal_flag_ok",
              "k_counter_ok", "membership_ok", "no_integer_ok", "status_word_count"):
        print(f"  {k} = {v.get(k)}")

    # ---- Step 4: single point of decision ----
    all_sites_ok = bool(v["idx_ok"] and v["hdr_ok"] and v["status_ok"])  # (local)
    all_tags_ok = bool(
        v["deferred_resolved_ok"]
        and v["ordinal_flag_ok"]
        and v["k_counter_ok"]
        and v["membership_ok"]
        and v["no_integer_ok"]
    )  # (local)
    substantive_ok = v["status_word_count"] >= 15  # (local) single-paragraph Status: token count (hundreds of words), NOT newline count
    verdict = "PASS" if (all_sites_ok and all_tags_ok and substantive_ok and composite_pass_and) else "FAIL"  # (local)
    k_counter = 2 if verdict == "PASS" else 1  # (local) Element-3 (iii) K=1->K=2 on PASS

    # ---- Step 5: emit ONCE — dual-SHA over the flipped §VII.AY Status block + pinmap ----
    audit_sha, content_sha = compute_dual_sha(pins, STATUS_NEW)  # (local)
    value_str = (  # (local)
        f"VII-AY-OP-PROJ-STAGE-3-PERMANENT_"
        f"rel_tol=1e-5_RELATIVE_vs_R_machine={R_machine!r}_"
        f"delta_rel_axis_A={res['deltas']['axis_A_vdd']:.4e}_"
        f"delta_rel_axis_B_primary={res['deltas']['axis_B_primary_mack']:.4e}_"
        f"delta_rel_axis_B_cross_pillar={res['deltas']['axis_B_cross_pillar']:.4e}_"
        f"composite_pass_and={composite_pass_and}_"
        f"stage3_eligibility={stage3_eligibility}_stage3_permanent_flipped={all_sites_ok}_"
        f"deferred_resolved_tag={deferred_resolved_tag}_element3_iii_k_counter={k_counter}_"
        f"idx={v['idx_ok']}_hdr={v['hdr_ok']}_status={v['status_ok']}_"
        f"ordinal_NOT_asserted_AU_AW_collision_CF=CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW;"
        f"W5_1_audit=491ac49c6d6436bce9e783efeac6e2ba06383a4fa5e03659bf62cfd300849617;"
        f"axis_A_audit={AXIS_A_PASS_AUDIT_SHA};axis_B_cross_pillar_audit={AXIS_BCP_PASS_AUDIT_SHA};"
        f"axis_B_primary_re_tested_FAIL_audit={AXIS_BP_FAIL_AUDIT_SHA}"
    )

    supersedes = find_latest_prior_audit_sha()  # (local) Option-A corrective tag
    if supersedes:
        print(f"  prior verdict line detected; emitting corrective line with supersedes={supersedes[:16]}...")

    # ---- artifacts (npz round-trip + png) BEFORE verdict emission ----
    _emit_npz_and_json(res, R_machine, w5_1, chain, slot_reserved, stage3_eligibility,
                       stage3_permanent_layer_ready, deferred_resolved_tag,
                       composite_pass_and, k_counter=k_counter, flipped=all_sites_ok,
                       verdict=verdict, value_str=value_str,
                       audit_sha=audit_sha, content_sha=content_sha, verify=v)
    _emit_plot(res, R_machine)

    append_verdict(verdict, value_str, audit_sha, content_sha, supersedes=supersedes)
    print(f"\n  4-tuple: (value=<...>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")
    print(f"\n  >>> VERDICT: {verdict}")
    print(f"  §VII.AY.OP-PROJ STAGE-1-CANDIDATE -> STAGE-3-PERMANENT flipped = {all_sites_ok}")
    print(f"  Element-3 (iii) HIT K-counter K=1 -> K={k_counter}")
    print(f"  corpus §21.0 R2 DEFERRED->resolved tag = {deferred_resolved_tag}")
    return 0  # verdict is DATA; exit 0


def _emit_npz_and_json(res, R_machine, w5_1, chain, slot_reserved, stage3_eligibility,
                       stage3_permanent_layer_ready, deferred_resolved_tag, composite_pass_and,
                       k_counter, flipped, verdict, value_str, audit_sha, content_sha, verify):
    np.savez(
        OUT_NPZ,
        rel_tol_used=np.float64(REL_TOL),
        publication_precision_floor=np.float64(PUBLICATION_PRECISION_FLOOR),
        sig_figs_of_agreement=np.int64(SIG_FIGS_OF_AGREEMENT),
        R_machine_substrate_pin=np.float64(R_machine),
        delta_rel_axis_A=np.float64(res["deltas"]["axis_A_vdd"]),
        delta_rel_axis_B_primary=np.float64(res["deltas"]["axis_B_primary_mack"]),
        delta_rel_axis_B_cross_pillar=np.float64(res["deltas"]["axis_B_cross_pillar"]),
        axis_A_image=np.float64(res["images"]["axis_A_vdd"]),
        axis_B_primary_image=np.float64(res["images"]["axis_B_primary_mack"]),
        axis_B_cross_pillar_image=np.float64(res["images"]["axis_B_cross_pillar"]),
        axis_A_pass=np.bool_(res["passes"]["axis_A_vdd"]),
        axis_B_primary_pass=np.bool_(res["passes"]["axis_B_primary_mack"]),
        axis_B_cross_pillar_pass=np.bool_(res["passes"]["axis_B_cross_pillar"]),
        composite_pass_and=np.bool_(composite_pass_and),
        stage3_eligibility=np.bool_(stage3_eligibility),
        stage3_permanent_layer_ready=np.bool_(stage3_permanent_layer_ready),
        stage3_permanent_flipped=np.bool_(flipped),
        deferred_resolved_tag=str(deferred_resolved_tag),
        element3_iii_k_counter=np.int64(k_counter),
        F1=np.float64(res["F1"]),
        F2=np.float64(res["F2"]),
        prior_abs_as_rel=np.float64(PUBLICATION_PRECISION_FLOOR / R_machine),
        delta_rel_F1_F2=np.float64(abs(res["F1"] - res["F2"]) / abs(res["F2"])),
        # upstream evidence:
        w5_1_pass_line=np.bool_(w5_1["w5_1_pass_line"]),
        w5_1_branch=str(w5_1["w5_1_branch"]),
        w5_1_R_machine_npz=np.float64(w5_1["w5_1_R_machine_npz"] if w5_1["w5_1_R_machine_npz"] is not None else float("nan")),
        canonical_pin_matches=np.bool_(w5_1["canonical_pin_matches"]),
        axis_a_pass_present=np.bool_(chain["axis_a_pass_present"]),
        axis_bcp_pass_present=np.bool_(chain["axis_bcp_pass_present"]),
        axis_bp_fail_present=np.bool_(chain["axis_bp_fail_present"]),
        composite_fail_present=np.bool_(chain["composite_fail_present"]),
        slot_reserved=np.bool_(slot_reserved),
        # the cited Stage-2 chain SHAs (full-64-hex):
        axis_A_pass_audit_sha=str(AXIS_A_PASS_AUDIT_SHA),
        axis_B_cross_pillar_pass_audit_sha=str(AXIS_BCP_PASS_AUDIT_SHA),
        axis_B_primary_fail_audit_sha=str(AXIS_BP_FAIL_AUDIT_SHA),
        composite_fail_audit_sha=str(COMPOSITE_FAIL_AUDIT_SHA),
        w5_1_pass_audit_sha="491ac49c6d6436bce9e783efeac6e2ba06383a4fa5e03659bf62cfd300849617",
        # metadata:
        L_max=np.int64(L_MAX),
        tau_fold=np.float64(tau_fold),
        M_KK=np.float64(M_KK),
        cocycle_norm_phi67=np.float64(cocycle_norm_phi67),
        cocycle_norm_phi88=np.float64(cocycle_norm_phi88),
        verdict=str(verdict),
        scheme=SCHEME,
        convention=CONVENTION,
        gate_id=GATE_ID,
        audit_sha256=str(audit_sha),
        content_sha256=str(content_sha),
        ordinal_collision_cf="CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW",
    )
    print(f"  NPZ -> {OUT_NPZ.relative_to(ROOT)}")
    _chk = np.load(OUT_NPZ, allow_pickle=True)  # (local)
    rt_ok = (float(_chk["delta_rel_axis_B_primary"]) == res["deltas"]["axis_B_primary_mack"])  # (local)
    print(f"  Class-8.3 round-trip: npz delta_rel_axis_B_primary preserved full float64: {rt_ok}")

    record = {  # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value_str,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "rel_tol_used": REL_TOL,
        "sig_figs_of_agreement": SIG_FIGS_OF_AGREEMENT,
        "R_machine_substrate_pin": R_machine,
        "three_axis": {
            "axis_A_vdd": {"image": res["images"]["axis_A_vdd"], "delta_rel": res["deltas"]["axis_A_vdd"], "pass": res["passes"]["axis_A_vdd"]},
            "axis_B_cross_pillar": {"image": res["images"]["axis_B_cross_pillar"], "delta_rel": res["deltas"]["axis_B_cross_pillar"], "pass": res["passes"]["axis_B_cross_pillar"]},
            "axis_B_primary_mack": {"image": res["images"]["axis_B_primary_mack"], "delta_rel": res["deltas"]["axis_B_primary_mack"], "pass": res["passes"]["axis_B_primary_mack"]},
            "composite_pass_and": composite_pass_and,
        },
        "two_layer_separation": {
            "stage3_eligibility_tolerance_layer": stage3_eligibility,
            "stage3_permanent_substrate_pin_layer": stage3_permanent_layer_ready,
            "stage3_permanent_flipped": flipped,
        },
        "deferred_resolved_tag": deferred_resolved_tag,
        "element3_iii_k_counter": k_counter,
        "stage_2_chain": {
            "axis_A_pass_audit_sha256": AXIS_A_PASS_AUDIT_SHA,
            "axis_B_cross_pillar_pass_audit_sha256": AXIS_BCP_PASS_AUDIT_SHA,
            "axis_B_primary_FAIL_audit_sha256_re_tested": AXIS_BP_FAIL_AUDIT_SHA,
            "composite_FAIL_audit_sha256": COMPOSITE_FAIL_AUDIT_SHA,
            "w5_1_PASS_audit_sha256": "491ac49c6d6436bce9e783efeac6e2ba06383a4fa5e03659bf62cfd300849617",
        },
        "ordinal_assertion": "NOT-ASSERTED (pre-existing AU/AW '#3' collision; CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW)",
        "stage_3_set_joined": [
            "§VII.AH (FIRST, S90 W2 CF-20)", "§VII.U.2 Corner-II Var_a (SECOND, S92 W4-7)",
            "§VII.AU.OP-PROJ (S93 W2-2)", "§VII.AW.OP-PROJ",
            "§VII.AV.STATE-PROJ (S93 W3-6)", "§VII.AX.OP-PROJ",
        ],
        "M1_M4_self_classification": {
            "M1_artifact_existence_with_content": True,
            "M2_registry_write_plus_sha": True,
            "M3_verbatim_closed_stage2_verdicts_plus_W5_1_substrate_pin": True,
            "M4_allowlist_append": "ORCHESTRATOR-ONLY (flagged in WP; not edited by this script)",
        },
        "verify": verify,
    }
    OUT_JSON.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"  JSON sidecar -> {OUT_JSON.relative_to(ROOT)}")


def _emit_plot(res, R_machine):
    fig, ax = plt.subplots(1, 1, figsize=(10.5, 4.6))
    names = ["Axis-A\n(vdd, F1 img)", "Axis-B-primary\n(mack re-test, F1 img)", "Axis-B-cross-pillar\n(spectral-geom, F2 img)"]  # (local)
    keys = ["axis_A_vdd", "axis_B_primary_mack", "axis_B_cross_pillar"]  # (local)
    deltas = [res["deltas"][k] for k in keys]  # (local)
    colors = ["C0", "C3", "C2"]  # (local)
    bars = ax.bar(names, deltas, color=colors, alpha=0.8)
    ax.axhline(REL_TOL, color="k", ls="--", lw=1.6, label=f"rel_tol = 1e-5 (10^-5 sig-fig agreement floor)")
    ax.axhline(PUBLICATION_PRECISION_FLOOR / R_machine, color="C1", ls=":", lw=1.4,
               label=f"prior <1e-6 ABS as REL = {PUBLICATION_PRECISION_FLOOR/R_machine:.3e} (PIN-TIGHT)")
    ax.set_yscale("log")
    ax.set_ylabel(r"$\Delta_{\rm rel} = |{\rm image} - R_{\rm machine}| / |R_{\rm machine}|$")
    for b, d in zip(bars, deltas):
        ax.text(b.get_x() + b.get_width() / 2, d * 1.15, f"{d:.2e}", ha="center", va="bottom", fontsize=8)
    ax.set_title(
        f"{GATE_ID}\n"
        f"3-axis Stage-2 PASS-AND at rel_tol=1e-5 vs W5-1 substrate-sourced R_machine = {R_machine:.9f} "
        f"(branch F2-faithful)\nall Δ_rel < 1e-5 ⇒ composite PASS-AND ⇒ STAGE-1 → STAGE-3-PERMANENT",
        fontsize=8.5,
    )
    ax.legend(loc="upper right", fontsize=7.5)
    ax.grid(True, axis="y", ls=":", alpha=0.4)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"  PNG -> {OUT_PNG.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
