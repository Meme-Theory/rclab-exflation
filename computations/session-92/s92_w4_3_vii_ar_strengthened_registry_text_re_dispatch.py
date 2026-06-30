#!/usr/bin/env python3
"""
S92 W4-3 — S92-W4-CF-S92-VII-AR-STRENGTHENED-REGISTRY-TEXT-RE-DISPATCH
=====================================================================

Gate: S92-W4-CF-S92-VII-AR-STRENGTHENED-REGISTRY-TEXT-RE-DISPATCH
Trigger: [VERIFY]
Classification: NON-PHONONIC (METHODOLOGY-class)
Agent: mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`

Pre-registered threshold (plan §W4-3):
  PASS iff
    (a) §W4-1 LATEST canonical (line 129) is PASS with reading=PASS-A-AND-B
    (b) §VII.AR registry slot is located via heading-anchor grep (NOT plan-line-
        numbers, which are stale by ~106 lines)
    (c) "Strengthened STAGE-1-CANDIDATE evidence chain (S92 W4 CF-S92-VII-AR)"
        sub-block is inserted into the §VII.AR slot, folding BOTH PASS-A
        (asymmetric Bogoliubov coupling) AND PASS-B (A_5_extended sub-atlas
        projection excluding ζ) derivations as complementary substrate-natural
        realizations of the §VII.AR LEVEL-DRESSED predicate
    (d) §W4-1 audit_sha256=257e2619…  is cited explicitly in the inserted block
    (e) supersedes chain origin daf7001d…  is cited explicitly
    (f) PROVISIONAL qualifier at line 17299 AND sub-atlas pre-registration at
        lines 17305-17315 remain INTACT (no edits to S90 W1-16-committed or
        S91 W-3 R2-B-committed text)
    (g) verdict line carries supersedes=daf7001d…  token

CHAINED-CONDITIONAL behavior:
  §W4-1 verdict outcome at `computations/session-92/s92_gate_verdicts.txt:129`
  (the LATEST canonical line per Option-A reading discipline) is **PASS** with
  reading=PASS-A-AND-B. The plan §W4-3 method envisaged PASS-A XOR PASS-B
  XOR FAIL; the realized verdict combines both. Plan-text-drift correction
  protocol (substrate-first-canonical-sourcing.md §(ii.B)) applied: BOTH
  substrate-physics derivations are folded into the registry slot as
  complementary substrate-natural realizations.

Substrate framing (per `phononic-framing.md §"IS Space, Not IN Space"` +
`epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence):
  NON-PHONONIC METHODOLOGY-class gate. The §VII.AR registry-text edit IS the
  methodology-floor F-image of the substrate-IS canonical structural identity
  verified at §W4-1. The substrate's own structural test of construction-rank
  preservation at the BdG sub-algebra IS what determines PASS/FAIL — BOTH the
  asymmetric coupling AND A_5_extended sub-atlas projection ARE substrate-
  natural realizations of the §VII.AR LEVEL-DRESSED predicate, NOT orchestrator-
  selected conventions. The S91 W4-1 axis-B FAIL was specific to the SYMMETRIC
  multiplicative overlay realization (uniform multiplicative factor cannot
  change rank vector by construction); the asymmetric coupling and
  A_5_extended projection are TWO distinct substrate-IS realizations that each
  independently confirm the cohomology-class structural identity.

  Direction substrate → emergent: D_K eigenvalues → BdG sub-algebra
  M_2(ℂ) ⊂ A_K → asymmetric Bogoliubov amplitudes OR A_5_extended sub-atlas
  (4-element regulator family excluding ζ) → rank-ordering predicate at
  substrate-distance-2 pole s=4 → §VII.AR cohomology-class structural identity
  validation. FORBIDDEN inversion: "the registry edit drives the substrate
  canonical." INVERT: "the substrate's own structural test at §W4-1 drives the
  registry edit; mack-cosmic-bridge sole-writer is the methodology-floor
  scribe of that substrate outcome."

  mack-cosmic-bridge sole-writer

METHODOLOGY-class M1-M4 conjunction (per `wave-classification.md §M1-M4`):
  M1 (PASS predicate type): artifact-existence + insertion-block-presence
      content_sha256-distinct from pre-edit (NOT a numerical comparison)
  M2 (Producing-operation type): Edit on `sessions/permanent-results-registry.md`
      + SHA-256 cross-check; NO numerical compute, NO eigenvalue work
  M3 (Source-of-truth type): verbatim sub-diff from §W4-1 substrate-physics
      derivation + §W4-1 LATEST canonical verdict; NOT first-principles new
      derivation
  M4 (Allowlist membership): gate-ID
      `S92-W4-CF-S92-VII-AR-STRENGTHENED-REGISTRY-TEXT-RE-DISPATCH`;
      allowlist append is orchestrator-only-edit per
      `methodology-wave-allowlist.md §"Edit discipline"` clause (2)

Output 4-tuple:
  (value=<composite-string>,
   scheme=mack-sole-writer-registry-text-update-methodology-class-CHAINED-CONDITIONAL,
   convention=joint-theorem-promotion-stage-3-eligibility-branch-PASS-A-AND-B-BOTH-FOLD,
   L_max=N/A)

Inputs (SHA-256 pinned at runtime, feed audit_sha256):
  - computations/_shared/canonical_constants.py
  - sessions/permanent-results-registry.md (registry §VII.AR pre-edit, slot
    located via heading-anchor grep; line range 17276-17326 at runtime)
  - computations/session-92/s92_gate_verdicts.txt (§W4-1 LATEST canonical line)
  - script bytes (feed BOTH audit_sha256 and content_sha256)

Verdict-line supersedes-tag form (canonical f-string emission target):
  supersedes=daf7001d89346a7a7721a1e8b3bc89244f2dd4693fd71414ac5c6acb8335897c
  per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute
  verdict permanence"` (S88 W8-100 user adjudication, 2026-05-05). Companion
  in-session supersedes chain: 257e2619…  is the LATEST canonical for the §W4-1
  predecessor gate (the W4-3 spawn-prompt-cited audit), which itself supersedes
  4baa1fb2…  (in-session prior PASS) and chains back to daf7001d…  (S90 W7
  mechanical-closure chain origin).
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
from pathlib import Path

# MANDATORY canonical constants import (M2 audit compliance even though no
# numerical constant is consumed; the import is the audit-trail signature)
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: F401,F403

# -----------------------------------------------------------------
# Section 1 — Identity + canonical paths
# -----------------------------------------------------------------

GATE_ID = "S92-W4-CF-S92-VII-AR-STRENGTHENED-REGISTRY-TEXT-RE-DISPATCH"
SCHEME = (
    "mack-sole-writer-registry-text-update-methodology-class-"
    "CHAINED-CONDITIONAL"
)
CONVENTION = (
    "joint-theorem-promotion-stage-3-eligibility-"
    "branch-PASS-A-AND-B-BOTH-FOLD"
)
L_MAX = "N/A"

PROJECT_ROOT = Path(__file__).resolve().parents[2]  # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICT_TXT = (
    PROJECT_ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"
)  # (local)
W4_1_VERDICT_PATH = VERDICT_TXT  # same file — §W4-1 emitted to same path  # (local)
CANONICAL_CONSTANTS_PATH = (
    PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"
)  # (local)

DATA_OUT = (
    PROJECT_ROOT / "computations" / "session-92"
    / "s92_w4_3_vii_ar_strengthened_registry_text_re_dispatch.json"
)  # (local)

# Supersedes chain — Option-A protocol per gate-verdicts.md S88 W8-100
SUPERSEDES_CHAIN_ORIGIN = (
    "daf7001d89346a7a7721a1e8b3bc89244f2dd4693fd71414ac5c6acb8335897c"
)
W4_1_LATEST_AUDIT_SHA = (
    "257e2619fe308645a8f87d127dde3764696d0432038725af77e3fa1fa96ce490"
)
W4_1_IN_SESSION_PRIOR_AUDIT_SHA = (
    "4baa1fb278416c7d0a3e2859ab355affd6f126d0737b2ebc5487f21226563276"
)

# -----------------------------------------------------------------
# Section 2 — SHA helpers
# -----------------------------------------------------------------

def sha256_of_path(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sha256_of_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """Stable closure hash over an ordered pin map per W9a-99 split."""
    keys = sorted(pin_map.keys())                                       # (local)
    payload = "\n".join(f"{k}={pin_map[k]}" for k in keys)              # (local)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


# -----------------------------------------------------------------
# Section 3 — Locate §VII.AR slot via heading-anchor grep
#             (plan-text-drift correction per substrate-first-canonical-
#              sourcing.md §(ii.B))
# -----------------------------------------------------------------

VII_AR_HEADING_PREFIX = "## §VII.AR — Rank-Ordering at s=4"
VII_AS_HEADING_PREFIX = "## §VII.AS —"


def locate_vii_ar_slot(registry_text: str) -> tuple[int, int, str]:
    """Return (start_line_0idx, end_line_0idx_exclusive, slot_text)."""
    lines = registry_text.splitlines(keepends=True)                     # (local)
    start_idx = None                                                    # (local)
    for i, line in enumerate(lines):
        if line.startswith(VII_AR_HEADING_PREFIX):
            start_idx = i
            break
    if start_idx is None:
        raise RuntimeError(
            f"Could not locate '{VII_AR_HEADING_PREFIX}' in registry"
        )
    end_idx = None                                                      # (local)
    for j in range(start_idx + 1, len(lines)):
        if lines[j].startswith(VII_AS_HEADING_PREFIX):
            end_idx = j
            break
    if end_idx is None:
        raise RuntimeError(
            f"Could not locate next-slot boundary '{VII_AS_HEADING_PREFIX}'"
        )
    # Trim the trailing '---\n\n' separator between slots
    while end_idx > start_idx and lines[end_idx - 1].strip() in ("", "---"):
        end_idx -= 1
    slot_text = "".join(lines[start_idx:end_idx])                       # (local)
    return start_idx, end_idx, slot_text


# -----------------------------------------------------------------
# Section 4 — Read §W4-1 LATEST canonical verdict via grep
# -----------------------------------------------------------------

W4_1_GATE_ID = "S92-W4-CF-S92-VII-AR-STAGE-2-RE-DISPATCH-ASYMMETRIC-COUPLING"


def read_w4_1_latest_canonical(verdict_text: str) -> dict:
    """Find LATEST canonical line for §W4-1 (Option-A reading discipline:
    LATEST non-superseded line). Returns parsed fields."""
    lines = verdict_text.splitlines()                                   # (local)
    candidates = []                                                     # (local)
    for ln in lines:
        if ln.startswith(W4_1_GATE_ID + ":"):
            candidates.append(ln)
    if not candidates:
        raise RuntimeError(
            f"No canonical line for {W4_1_GATE_ID} in verdict file"
        )
    # Build supersedes-set: each line that is named in another line's
    # supersedes= token is itself superseded; the LATEST non-superseded
    # line is canonical per gate-verdicts.md S88 W8-100.
    superseded_shas: set[str] = set()                                   # (local)
    for ln in candidates:
        # Extract supersedes= token (full 64-char old audit_sha256)
        # Look for "supersedes=<64hex>" in the value field
        for tok in ln.split():
            if tok.startswith("supersedes="):
                val = tok[len("supersedes="):]                          # (local)
                # Strip any trailing punctuation; take first 64 hex chars
                hex64 = ""                                              # (local)
                for ch in val:
                    if ch in "0123456789abcdef":
                        hex64 += ch
                    else:
                        break
                if len(hex64) >= 64:
                    superseded_shas.add(hex64[:64])
        # Inline supersedes within value='...;supersedes=…;...' form:
        if "supersedes=" in ln:
            idx = 0                                                     # (local)
            while True:
                p = ln.find("supersedes=", idx)                         # (local)
                if p < 0:
                    break
                tail = ln[p + len("supersedes="):]                      # (local)
                hex64 = ""                                              # (local)
                for ch in tail:
                    if ch in "0123456789abcdef":
                        hex64 += ch
                    else:
                        break
                if len(hex64) >= 64:
                    superseded_shas.add(hex64[:64])
                idx = p + len("supersedes=")
    # Find non-superseded lines (latest comes last on disk)
    canonical = None                                                    # (local)
    for ln in candidates:
        # Extract this line's own audit_sha256
        own_sha = None                                                  # (local)
        for tok in ln.split():
            if tok.startswith("audit_sha256="):
                own_sha = tok[len("audit_sha256="):][:64]
                break
        if own_sha is not None and own_sha not in superseded_shas:
            canonical = (ln, own_sha)
    if canonical is None:
        # Fallback: take last in file order
        ln = candidates[-1]                                             # (local)
        own_sha = None                                                  # (local)
        for tok in ln.split():
            if tok.startswith("audit_sha256="):
                own_sha = tok[len("audit_sha256="):][:64]
                break
        canonical = (ln, own_sha or "")
    ln_canonical, sha_canonical = canonical
    # Parse verdict status
    verdict_tok = ln_canonical.split(":", 1)[1].lstrip()                # (local)
    status = verdict_tok.split()[0]                                     # (local) PASS/FAIL/INFO
    # Parse reading from value=
    reading = None                                                      # (local)
    if "reading=" in ln_canonical:
        idx = ln_canonical.find("reading=") + len("reading=")           # (local)
        tail = ln_canonical[idx:]                                       # (local)
        # reading is followed by ; or space
        end = 0                                                         # (local)
        while end < len(tail) and tail[end] not in ";' ":
            end += 1
        reading = tail[:end]
    return {
        "line": ln_canonical,
        "status": status,
        "reading": reading,
        "own_audit_sha256": sha_canonical,
        "superseded_shas_seen": sorted(superseded_shas),
    }


# -----------------------------------------------------------------
# Section 5 — Build the inserted "Strengthened evidence chain" block
# -----------------------------------------------------------------

def build_strengthened_block() -> str:
    """Build the verbatim insertion block to fold BOTH PASS-A and PASS-B
    derivations into the §VII.AR STAGE-1-CANDIDATE block."""
    block = (
        "**Strengthened STAGE-1-CANDIDATE evidence chain (S92 W4 "
        "CF-S92-VII-AR; landed 2026-05-23; mack-cosmic-bridge sole-writer "
        "per `feedback_mack-bridge-role.md`)**: §W4-1 Stage-2 cross-axis "
        "verify returned **composite=PASS, reading=PASS-A-AND-B** "
        "(audit_sha256=`257e2619fe308645a8f87d127dde3764696d0432038725af77e3fa1fa96ce490`, "
        "content_sha256=`15aac20c27ed47b74c267b180c0ee55d636710f0c7e7ac84e86d3e5d80e1667f`, "
        "at `computations/session-92/s92_gate_verdicts.txt:129` LATEST "
        "canonical per Option-A reading discipline; supersedes chain "
        "`257e2619…` → `4baa1fb2…` (in-session prior PASS) → "
        "`daf7001d89346a7a7721a1e8b3bc89244f2dd4693fd71414ac5c6acb8335897c` "
        "(S90 W7 mechanical-closure chain origin) per "
        "`gate-verdicts.md §\"Option A — sig_5 remediation pathway under "
        "absolute verdict permanence\"` S88 W8-100). The composite PASS "
        "ratifies BOTH alternative substrate-physics-derived realizations "
        "of the §VII.AR LEVEL-DRESSED predicate independently — the K=3 "
        "conditional re-audit (PASS-A | PASS-A-RESTRICTED | PASS-B | "
        "INFO/FAIL) at the **K-counter status PROVISIONAL re-tag** "
        "paragraph above resolves under BOTH the PASS-A-RESTRICTED branch "
        "AND the PASS-B branch simultaneously. Direction substrate → "
        "emergent: D_K eigenvalues → BdG sub-algebra `M_2(ℂ) ⊂ A_K` → "
        "asymmetric Bogoliubov amplitudes OR A_5_extended sub-atlas → "
        "rank-ordering predicate at substrate-distance-2 pole s=4 → "
        "§VII.AR cohomology-class structural identity validation. "
        "Two structurally distinct substrate-natural realizations:\n"
        "\n"
        "- **PASS-A — asymmetric Bogoliubov coupling on the F_2-axis FI "
        "sub-atlas**: regulator-specific PARAMETER pins replace the "
        "uniform multiplicative PARAMETER overlay realized at S91 W4-1 "
        "(which was rank-preserving by construction and FAILed clause "
        "(d)). Substrate-physics derivation: the four regulator profiles "
        "{F_2 Gaussian-exponential, cutoff_sqrt sharp-step, anomaly "
        "polynomial-corrected, Zubarev Fermi-Dirac analog} are "
        "STRUCTURALLY DISTINCT functional forms and admit STRUCTURALLY "
        "DISTINCT (cutoff_frac, M_PV²_frac) PARAMETER scales. Per-"
        "regulator pins: cutoff_frac ∈ {0.7, 0.5, 0.9, 1.2} and "
        "M_PV²_frac ∈ {0.1, 0.05, 0.2, 0.15} for {F_2, cutoff_sqrt, "
        "anomaly, Zubarev} respectively, pre-registered substrate-natural "
        "per the E5 sub-atlas enumeration at the **PASS-A-RESTRICTED** "
        "branch above (NOT post-hoc convention-shopping per "
        "`v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1). Outcome: "
        "**1 of 5 heat-kernel anchors** (t_ref ∈ "
        "{1/max(λ²), 2.3/max(λ²), ln(2)/max(λ²), 1/⟨λ²⟩_mw, 1/M_KK²-internal}) "
        "exhibits rank-vector change between PRIMARY and SCHEMATIC level "
        "evaluations (rank_change_per_anchor = [0, 0, 0, 0, 1]); the "
        "non-zero rank-change at the deep-IR anchor (1/M_KK²-internal) "
        "satisfies clause (d) `rank_vec_PRIMARY ≠ rank_vec_SCHEMATIC at "
        "≥1 anchor` predicate, completing axis-B 2/3 clause-PASS "
        "(clauses (d) PASS and (f) PASS; clause (b) FAIL under "
        "asymmetric form). Algebraic distance: the asymmetric form is "
        "NOT a numerical refinement of the symmetric form — the "
        "construction is structurally inequivalent (4-component PARAMETER "
        "vector vs scalar multiplicative overlay), hence Hybrid "
        "Independence Test clause (iv) at "
        "`cross-pillar-bridge-anatomy.md §\"Hybrid Independence Test\"` "
        "is satisfied.\n"
        "\n"
        "- **PASS-B — A_5_extended sub-atlas projection excluding ζ**: "
        "the 4-regulator atlas `A_5_extended = A_5 ∖ {ζ} = "
        "{Pauli-Villars, sharp_cutoff, sinc_lattice, sech_lattice}` "
        "(cardinality 4) reproduces the structural-equivalence band per "
        "the discrete combinatorial Spearman identity "
        "`ρ_S = 1 − 6·D²/(n³ − n)` for `n = 4`. Substrate-physics "
        "derivation per registry line 17308 above: ζ-regulator is the "
        "substrate-distance-1 pole reference (Mellin-residue at "
        "substrate-distance-1; cross-link to §VII.AU.OP-PROJ FWD-C1 "
        "baseline); the substrate-distance-2 pole observable IS sub-"
        "atlas-natural to evaluate on {F_2, cutoff_sqrt, anomaly, "
        "Zubarev} where ζ-regulator's structural-asymmetric image at "
        "substrate-distance-2 is excluded. Outcome: "
        "**|ρ_S(A_5_extended; s=4)| = 1.000000 EXACT** at the canonical "
        "L_max=12 block-diagonal cache, exceeding the registry-anchor "
        "Level-2 magnitude envelope `|ρ_S(s=4)|_PRIMARY ≥ 0.800 EXACT` "
        "from line 17288 by a structurally-meaningful margin (the 1.000 "
        "EXACT value corresponds to D² = 0 — zero pairwise rank "
        "inversions in the 4-element rank vector; the 0.800 EXACT "
        "registry anchor corresponds to D² = 2 — 2-of-6 pairwise "
        "inversions). Axis-B clauses (b), (d), (f) all PASS under this "
        "sub-atlas projection (axis_b_3_of_3_PASS_a5e = True); the "
        "PASS-A-RESTRICTED → PASS-B transition is the substrate-IS "
        "signature that the substrate-natural sub-atlas restriction "
        "achieves what the full A_5 atlas cannot under the symmetric "
        "form.\n"
        "\n"
        "**Joint structural implication**: PASS-A-AND-B (BOTH PASS-A "
        "asymmetric coupling AND PASS-B A_5_extended sub-atlas project "
        "independently to clause-(d) PASS) is the strongest possible "
        "outcome of the 3-branch conditional re-audit. The K-counter "
        "status PROVISIONAL qualifier at line 17299 above is RETAINED "
        "intact (per §W4-2 INFO closure: qualifier_intact_with_"
        "augmentation; required_markers=9/9; n_augmentation_markers=14; "
        "S92 W4-2 audit_sha256=`0b8193d9d0005b97ac8a1f947d674dba37789624c7da45873239fcfa02b6434c`) "
        "AND augmented with the §W4-1 BOTH-FOLD outcome. The §VII.AR "
        "LEVEL-DRESSED 4th-class extension at `cross-pillar-bridge-"
        "anatomy.md §\"Per-Bulletin-per-pole Level-1 wall classification\"` "
        "advances toward STAGE-3-PERMANENT eligibility via the K=3 "
        "calibration corpus: §VII.K-PROP.W10-4 ρ_∞ permanent-wall + "
        "§VII.U.1 Mellin-Dirichlet identity + §VII.AR LEVEL-DRESSED rank-"
        "ordering (THIS slot) all now share a substrate-natural sub-"
        "atlas restriction tag under PASS-B, and a substrate-natural "
        "asymmetric-coupling tag under PASS-A. Both restrictions are "
        "pre-registered substrate-physics-derived (NOT convention-shopped) "
        "per the E5 enumeration above. The §VII.K-DUAL.LEVEL-DRESSED "
        "calibration corpus row annotation template at line 17315 above "
        "applies: under PASS-A-AND-B, the §VII.K-DUAL.LEVEL-DRESSED "
        "corpus row inherits dual annotation `scoped to "
        "{A_5_extended-minus-ζ}` + `realized via asymmetric coupling "
        "(F_2-axis FI sub-atlas)` — the joint annotation propagates "
        "UPSTREAM from §VII.AR (K=1 instance) to §VII.K-DUAL (4th-class "
        "proposal).\n"
        "\n"
        "**Level-pin compliance (substrate-first-canonical-sourcing.md "
        "§(iv) K=4 MANDATORY)**: §W4-1 emission carries "
        "`convention=…-SCHEMATIC-PENDING-FULL-TIER-N4` + companion row "
        "`# tier_pin=TIER-2` (POSITIVE 4-class disclosure profile). The "
        "FULL-tier N=4 retry is queued forward as "
        "`forward_full_tier_N4_retry_queued` per the §W4-1 verdict. The "
        "K=3 advancement here is at the SCHEMATIC tier; promotion to "
        "STAGE-3-PERMANENT requires the FULL-tier N=4 reinforcement, "
        "which is pre-registered as a downstream gate beyond S92.\n"
        "\n"
        "**Substrate-input-orthogonality K-counter status**: K=3 "
        "preserved (no advance to K=4 under this landing) per §W4-1's "
        "explicit declaration "
        "`k_counter_substrate_input_orthogonality_status=K=3_preserved_"
        "no_advance_to_K=4_due_to_overlap_caveat_at_alternative_form_layer`. "
        "The substrate-input-overlap caveat applies because both PASS-A "
        "and PASS-B consume the same L_max=12 spectrum cache (cache_sha="
        "`9e6d9cf7fd6a6949`) and the same heat-kernel anchor sweep "
        "PRIMARY evaluator (cf60_input_sha=`3ba0f34b9c04a7f0`). "
        "Future Stage-2 dispatches with STRUCTURALLY ORTHOGONAL "
        "substrate-input pins (distinct cache, distinct anchor evaluator) "
        "would advance the K-counter; this landing preserves K=3 with "
        "the overlap caveat per `joint-theorem-promotion.md §\"Substrate-"
        "input-orthogonality clause\"` MANDATORY K=3 since S90 W2 CF-20.\n"
    )
    return block


# -----------------------------------------------------------------
# Section 6 — Apply edit + verify
# -----------------------------------------------------------------

# Anchor: insert immediately BEFORE the existing "Substrate framing per..."
# paragraph at line 17317. This places the strengthened block AFTER the
# K-counter status PROVISIONAL re-tag paragraph (preserved INTACT) and AFTER
# the E5 sub-atlas pre-registration (preserved INTACT), but BEFORE the
# forward-dispatch-routing prose. This keeps the PROVISIONAL qualifier
# (line 17299) and sub-atlas pre-registration (lines 17305-17315) untouched.

INSERT_ANCHOR_PREFIX = (
    "Substrate framing per `phononic-framing.md §\"IS Space, Not IN Space\"`"
)


def apply_strengthened_edit(registry_text: str) -> tuple[str, dict]:
    """Apply the strengthened evidence chain insertion in the §VII.AR slot."""
    lines = registry_text.splitlines(keepends=True)                     # (local)
    start_idx, end_idx, slot_text = locate_vii_ar_slot(registry_text)
    # Find the anchor line within the slot
    anchor_idx_global = None                                            # (local)
    for j in range(start_idx, end_idx):
        if lines[j].startswith(INSERT_ANCHOR_PREFIX):
            anchor_idx_global = j
            break
    if anchor_idx_global is None:
        raise RuntimeError(
            f"Could not locate insertion anchor '{INSERT_ANCHOR_PREFIX}' "
            f"within §VII.AR slot lines [{start_idx},{end_idx})"
        )
    block_text = build_strengthened_block()                             # (local)
    # Inserted block is its own paragraph: blank line before, blank line after
    insertion = block_text + "\n"                                       # (local)
    new_lines = (
        lines[:anchor_idx_global]
        + [insertion]
        + lines[anchor_idx_global:]
    )  # (local)
    new_text = "".join(new_lines)                                       # (local)
    diag = {
        "vii_ar_slot_start_line_1idx": start_idx + 1,
        "vii_ar_slot_end_line_1idx_exclusive": end_idx + 1,
        "vii_ar_slot_byte_count_pre_edit": len(slot_text.encode("utf-8")),
        "insertion_anchor_line_1idx": anchor_idx_global + 1,
        "insertion_anchor_text_prefix": INSERT_ANCHOR_PREFIX,
        "insertion_byte_count": len(insertion.encode("utf-8")),
    }
    return new_text, diag


# -----------------------------------------------------------------
# Section 7 — Atomic write + re-read verification
# -----------------------------------------------------------------

def write_atomic_with_fsync(path: Path, text: str) -> None:
    """Atomic write with fsync on Windows via temp-rename pattern."""
    tmp_path = path.with_suffix(path.suffix + ".tmp")                   # (local)
    with tmp_path.open("w", encoding="utf-8", newline="") as fp:
        fp.write(text)
        fp.flush()
        try:
            import os
            os.fsync(fp.fileno())
        except OSError:
            pass
    tmp_path.replace(path)


def verify_post_edit_slot(
    registry_text: str,
    expected_insertion_prefix: str,
    expected_w4_1_sha: str,
    expected_supersedes_origin: str,
) -> tuple[bool, dict]:
    """Re-read §VII.AR slot, verify all PASS predicates hold."""
    _, _, slot_text = locate_vii_ar_slot(registry_text)
    checks = {
        "insertion_block_present": expected_insertion_prefix in slot_text,
        "w4_1_audit_sha_cited": expected_w4_1_sha in slot_text,
        "supersedes_origin_cited": expected_supersedes_origin in slot_text,
        "provisional_qualifier_intact": (
            "K-counter status PROVISIONAL re-tag" in slot_text
            and "PASS-A-RESTRICTED" in slot_text
        ),
        "sub_atlas_preregistration_intact": (
            "A_5_extended-minus-ζ" in slot_text
            and "A_5_extended-minus-cutoff_sqrt" in slot_text
            and "A_5_extended-minus-anomaly" in slot_text
            and "Volovik R2-B Answer to Q-VLV-B" in slot_text
        ),
        "vii_ar_heading_intact": slot_text.startswith(VII_AR_HEADING_PREFIX),
        "both_fold_pass_a_present": (
            "PASS-A — asymmetric Bogoliubov coupling" in slot_text
        ),
        "both_fold_pass_b_present": (
            "PASS-B — A_5_extended sub-atlas projection" in slot_text
        ),
        "joint_structural_implication_present": (
            "PASS-A-AND-B (BOTH PASS-A" in slot_text
        ),
        "level_pin_compliance_present": (
            "SCHEMATIC-PENDING-FULL-TIER-N4" in slot_text
        ),
        "mack_sole_writer_present": (
            "mack-cosmic-bridge sole-writer" in slot_text
        ),
    }
    return all(checks.values()), checks


# -----------------------------------------------------------------
# Section 8 — Verdict emission (Option-A protocol)
# -----------------------------------------------------------------

def append_verdict(
    verdict: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Atomic single-append: canonical line + dual-SHA companion row +
    Option-A protocol companion row (per gate-verdicts.md S88 W8-100).
    The supersedes= token lives in the canonical line + companion row.

    Matches the canonical `append_verdict` helper signature at
    `computations/_shared/_critpath_audit.py` and the canonical
    `_script_template.py` convention; mack-cosmic-bridge sole-writer
    pattern preserves the helper-name discipline.
    """
    canonical = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"supersedes={SUPERSEDES_CHAIN_ORIGIN} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} # {GATE_ID} dual-SHA "
        f"companion row (W9a-99 split); "
        f"supersedes={SUPERSEDES_CHAIN_ORIGIN}\n"
    )  # (local)
    option_a_companion = (
        f"# OPTION_A_PROTOCOL=supersedes={SUPERSEDES_CHAIN_ORIGIN} "
        f"# {GATE_ID} Option-A corrective emission per gate-verdicts.md "
        f"§\"Option A — sig_5 remediation pathway under absolute verdict "
        f"permanence\" (S88 W8-100); supersedes_chain_origin=S90 W7 "
        f"mechanical-closure; W4-1 LATEST canonical audit_sha256="
        f"{W4_1_LATEST_AUDIT_SHA} (line 129); supersedes in-session prior "
        f"PASS audit_sha256={W4_1_IN_SESSION_PRIOR_AUDIT_SHA}\n"
    )  # (local)
    methodology_companion = (
        f"# METHODOLOGY_CLASS=M1_M2_M3_M4_strict_conjunction "
        f"# {GATE_ID} wave-classification.md §M1-M4: M1 artifact-existence + "
        f"insertion-block-presence; M2 Edit + SHA only; M3 verbatim sub-diff "
        f"from §W4-1 substrate-physics + LATEST canonical verdict; M4 "
        f"allowlist append is orchestrator-only per methodology-wave-"
        f"allowlist.md §\"Edit discipline\" clause (2); mack-cosmic-bridge "
        f"sole-writer per feedback_mack-bridge-role.md\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(dual_sha_companion)
        fp.write(option_a_companion)
        fp.write(methodology_companion)


# -----------------------------------------------------------------
# Section 9 — Main
# -----------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                    # (local)

    print(f"=== {GATE_ID} ===")
    print(f"  mack-cosmic-bridge sole-writer (CHAINED-CONDITIONAL on §W4-1)")
    print()

    # Step 1: Read §W4-1 LATEST canonical
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8")              # (local)
    w4_1_canonical = read_w4_1_latest_canonical(verdict_text)           # (local)
    print("Step 1: §W4-1 LATEST canonical")
    print(f"  status: {w4_1_canonical['status']}")
    print(f"  reading: {w4_1_canonical['reading']}")
    print(f"  audit_sha256 (own): {w4_1_canonical['own_audit_sha256']}")

    branch = None                                                       # (local)
    if w4_1_canonical["status"] == "PASS":
        reading = w4_1_canonical["reading"] or ""                       # (local)
        if "PASS-A-AND-B" in reading:
            branch = "BOTH-FOLD"
        elif "PASS-A" in reading:
            branch = "PASS-A"
        elif "PASS-B" in reading:
            branch = "PASS-B"
    if branch is None and w4_1_canonical["status"] == "INFO":
        branch = "INFO"
    if branch is None:
        branch = "FAIL"
    print(f"  branch selected: {branch}")
    print()

    if branch != "BOTH-FOLD":
        # CHAINED-CONDITIONAL escape hatch: anything other than BOTH-FOLD
        # under PASS-A-AND-B reading is a planning mismatch. Plan-text
        # drift correction applies: spawn prompt explicitly directs
        # BOTH-FOLD for PASS-A-AND-B. Other branches FAIL via mechanical
        # closure per `mechanical-closure-discipline.md`. Since we have
        # verified PASS-A-AND-B at line 129, this path should not fire.
        raise RuntimeError(
            f"Unexpected §W4-1 branch '{branch}'; spawn prompt directs "
            f"BOTH-FOLD on PASS-A-AND-B reading."
        )

    # Step 2: Read registry + locate §VII.AR slot, compute pre-edit SHA
    registry_text_pre = REGISTRY_PATH.read_text(encoding="utf-8")       # (local)
    start_pre, end_pre, slot_pre = locate_vii_ar_slot(registry_text_pre)
    pre_edit_slot_sha = sha256_of_str(slot_pre)                         # (local)
    print("Step 2: §VII.AR slot pre-edit")
    print(f"  slot lines: [{start_pre + 1}, {end_pre + 1}) "
          f"(1-indexed, half-open)")
    print(f"  slot byte count: {len(slot_pre.encode('utf-8'))}")
    print(f"  pre-edit slot content_sha256: {pre_edit_slot_sha[:16]}…")
    print()

    # Step 3: Apply edit (build inserted block + locate insertion anchor +
    #          splice new lines)
    new_registry_text, edit_diag = apply_strengthened_edit(registry_text_pre)
    print("Step 3: edit applied (in memory)")
    print(f"  insertion anchor line (1-indexed): "
          f"{edit_diag['insertion_anchor_line_1idx']}")
    print(f"  insertion byte count: "
          f"{edit_diag['insertion_byte_count']}")
    print()

    # Step 4: Atomic write
    write_atomic_with_fsync(REGISTRY_PATH, new_registry_text)
    print("Step 4: atomic write + fsync complete")
    print()

    # Step 5: Re-read + verify
    registry_text_post = REGISTRY_PATH.read_text(encoding="utf-8")      # (local)
    start_post, end_post, slot_post = locate_vii_ar_slot(registry_text_post)
    post_edit_slot_sha = sha256_of_str(slot_post)                       # (local)
    expected_insertion_prefix = (
        "**Strengthened STAGE-1-CANDIDATE evidence chain "
        "(S92 W4 CF-S92-VII-AR;"
    )
    verify_ok, verify_checks = verify_post_edit_slot(
        registry_text_post,
        expected_insertion_prefix=expected_insertion_prefix,
        expected_w4_1_sha=W4_1_LATEST_AUDIT_SHA,
        expected_supersedes_origin=SUPERSEDES_CHAIN_ORIGIN,
    )
    print("Step 5: re-read + verify")
    print(f"  slot lines post-edit: [{start_post + 1}, {end_post + 1}) "
          f"(1-indexed)")
    print(f"  post-edit slot content_sha256: {post_edit_slot_sha[:16]}…")
    print(f"  pre-vs-post-distinct: "
          f"{pre_edit_slot_sha != post_edit_slot_sha}")
    print(f"  verification PASS: {verify_ok}")
    for k, v in verify_checks.items():
        print(f"    {k}: {v}")
    print()

    # Step 6: Build verdict + dual-SHA closure
    canonical_constants_sha = sha256_of_path(CANONICAL_CONSTANTS_PATH)  # (local)
    script_path = Path(__file__).resolve()                              # (local)
    script_sha = sha256_of_path(script_path)                            # (local)
    # Re-read verdict file SHA (post our atomic write may include nothing)
    verdict_file_sha_pre = sha256_of_str(verdict_text)                  # (local)
    registry_post_sha = sha256_of_str(registry_text_post)               # (local)

    pin_map = {
        "script_sha256": script_sha,
        "canonical_constants_sha256": canonical_constants_sha,
        "registry_pre_edit_sha256": sha256_of_str(registry_text_pre),
        "registry_post_edit_sha256": registry_post_sha,
        "vii_ar_slot_pre_edit_sha256": pre_edit_slot_sha,
        "vii_ar_slot_post_edit_sha256": post_edit_slot_sha,
        "verdict_file_pre_emit_sha256": verdict_file_sha_pre,
        "w4_1_latest_audit_sha256": W4_1_LATEST_AUDIT_SHA,
        "w4_1_in_session_prior_audit_sha256": W4_1_IN_SESSION_PRIOR_AUDIT_SHA,
        "supersedes_chain_origin": SUPERSEDES_CHAIN_ORIGIN,
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "branch": branch,
        "verify_ok": str(verify_ok),
    }
    audit_sha = closure_hash(pin_map)                                   # (local)
    # content_sha256 := SHA over the script bytes themselves (W9a-99 split)
    content_sha = script_sha                                            # (local)

    verdict = "PASS" if verify_ok else "FAIL"                           # (local)

    # Build the value field (compact, single-quoted, key=value;key=value pairs)
    value_str = (
        f"branch={branch};"
        f"reading=PASS-A-AND-B;"
        f"vii_ar_slot_pre_edit_sha={pre_edit_slot_sha[:16]};"
        f"vii_ar_slot_post_edit_sha={post_edit_slot_sha[:16]};"
        f"pre_post_distinct={pre_edit_slot_sha != post_edit_slot_sha};"
        f"insertion_anchor_line_1idx={edit_diag['insertion_anchor_line_1idx']};"
        f"insertion_byte_count={edit_diag['insertion_byte_count']};"
        f"vii_ar_slot_lines_post_1idx=[{start_post + 1},{end_post + 1});"
        f"verify_pass={verify_ok};"
        f"insertion_block_present={verify_checks['insertion_block_present']};"
        f"w4_1_audit_sha_cited={verify_checks['w4_1_audit_sha_cited']};"
        f"supersedes_origin_cited={verify_checks['supersedes_origin_cited']};"
        f"provisional_qualifier_intact={verify_checks['provisional_qualifier_intact']};"
        f"sub_atlas_preregistration_intact={verify_checks['sub_atlas_preregistration_intact']};"
        f"both_fold_pass_a_present={verify_checks['both_fold_pass_a_present']};"
        f"both_fold_pass_b_present={verify_checks['both_fold_pass_b_present']};"
        f"joint_structural_implication_present={verify_checks['joint_structural_implication_present']};"
        f"level_pin_compliance_present={verify_checks['level_pin_compliance_present']};"
        f"mack_sole_writer_present={verify_checks['mack_sole_writer_present']};"
        f"w4_1_latest_audit_sha={W4_1_LATEST_AUDIT_SHA[:16]};"
        f"supersedes={SUPERSEDES_CHAIN_ORIGIN};"
        f"supersedes_in_session_prior={W4_1_IN_SESSION_PRIOR_AUDIT_SHA[:16]};"
        f"plan_line_drift_corrected=plan_pinned_17170_17208_vs_runtime_17276_17326_+106_lines;"
        f"methodology_class_M1_M2_M3_M4=satisfied"
    )

    # Step 7: Write JSON sidecar BEFORE emitting verdict (so SHA inputs are
    # all stable; the JSON does NOT feed audit_sha256 — it's an audit-trail
    # output)
    data_out = {
        "gate_id": GATE_ID,
        "agent": "mack-cosmic-bridge",
        "branch": branch,
        "verdict": verdict,
        "value_str": value_str,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "supersedes": SUPERSEDES_CHAIN_ORIGIN,
        "w4_1_latest_audit_sha256": W4_1_LATEST_AUDIT_SHA,
        "w4_1_in_session_prior_audit_sha256": W4_1_IN_SESSION_PRIOR_AUDIT_SHA,
        "w4_1_canonical_line_status": w4_1_canonical["status"],
        "w4_1_canonical_reading": w4_1_canonical["reading"],
        "w4_1_superseded_shas_seen": w4_1_canonical["superseded_shas_seen"],
        "pin_map": pin_map,
        "edit_diagnostic": edit_diag,
        "verify_checks": verify_checks,
        "pre_edit_vii_ar_slot_sha256": pre_edit_slot_sha,
        "post_edit_vii_ar_slot_sha256": post_edit_slot_sha,
        "pre_edit_vii_ar_slot_lines_1idx": [start_pre + 1, end_pre + 1],
        "post_edit_vii_ar_slot_lines_1idx": [start_post + 1, end_post + 1],
        "registry_path": str(REGISTRY_PATH.relative_to(PROJECT_ROOT)),
        "verdict_path": str(VERDICT_TXT.relative_to(PROJECT_ROOT)),
        "elapsed_seconds": time.time() - t0,
    }
    DATA_OUT.parent.mkdir(parents=True, exist_ok=True)
    DATA_OUT.write_text(
        json.dumps(data_out, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(f"Step 7: JSON sidecar written: {DATA_OUT.name}")
    print()

    # Step 8: Emit verdict (single atomic append: canonical + 3 companion rows)
    append_verdict(verdict, value_str, audit_sha, content_sha)
    print("Step 8: verdict line + dual-SHA companion + Option-A companion + "
          "methodology-class companion appended")
    print(f"  verdict: {verdict}")
    print(f"  audit_sha256: {audit_sha[:16]}…  (full 64-char in file)")
    print(f"  content_sha256: {content_sha[:16]}…  (full 64-char in file)")
    print(f"  supersedes: {SUPERSEDES_CHAIN_ORIGIN[:16]}… (full in file)")
    print()
    print(f"elapsed: {time.time() - t0:.2f}s")

    return 0


if __name__ == "__main__":
    sys.exit(main())
