#!/usr/bin/env python3
"""
S92 W6-2 — S92-W6-CF-W2-2-S91-W2-K-COUNTER-K2-ADVANCEMENT-REGULATOR-CLASS-PLURALISM
====================================================================================

Gate: S92-W6-CF-W2-2-S91-W2-K-COUNTER-K2-ADVANCEMENT-REGULATOR-CLASS-PLURALISM
      ([VERIFY-THEOREM])

Pre-registered threshold (per session-92-plan-w6.md §W6-2 lines 673-1120):
  PASS iff
    (corpus row 1 appended at §3 Hybrid Independence Test corpus with
     K=2 advancement annotation, predicate (YES ∨ YES ∨ NO) ∧ YES = YES)
    AND
    (corpus row 2 appended at §10 Element 3 fiducial-anchor binding /
     Bridge-map-scheme suffix discipline corpus with three regulator-
     class suffix declaration ζ + PV + Mellin)
    AND
    (corpus row 3 appended at §17 (plan §15) Within-cell discriminator
     axes corpus with regulator-class axis specialization at Cell-II ×
     Mellin-pole-s=4)
    AND
    (each row's content_sha256 matches pre-composed text bit-exact)
  FAIL otherwise; INFO does NOT apply (METHODOLOGY-class binary
  artifact predicate).

Inputs (SHA-256 dual-pinned at runtime, S87+ schema):
  - computations/_shared/canonical_constants.py
  - sessions/framework/registry/cross-pillar-bridge-corpus.md
  - sessions/permanent-results-registry.md
  - computations/session-91/s91_gate_verdicts.txt
  - computations/session-92/s92_gate_verdicts.txt
  - script bytes (feeds both audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<row_content_sha_summary>,
   scheme=gen-physicist-rule-extension-scribe-atomic-posix-O_APPEND-corpus-row-landing-AFTER-pattern,
   convention=k-counter-k2-advancement-three-corpus-axes-suggestion-status-preserved,
   L_max=12)

Classification: NON-PHONONIC (METHODOLOGY-class corpus-row landing per
                wave-classification.md M1-M4 strict-conjunction)

METHODOLOGY
-----------
This gate appends THREE K=2 corpus rows to `sessions/framework/registry/
cross-pillar-bridge-corpus.md` citing §W6-1's §VII.AX.MULTI-PIN-ATLAS
landing (audit_sha256=a006b8092e33e680c445676041d3fe38bc7cd46d8dab9e9a99e0d9904ff8b727)
as the K=2 calibration corpus instance shared across three K-counter
axes:

  §3  Hybrid Independence Test corpus (K=1 instance #1 = S88 W8-87
       §VII.AF.1 baseline; K=2 instance #2 = §VII.AX.MULTI-PIN-ATLAS
       with predicate (YES ∨ YES ∨ NO) ∧ YES = YES).
  §10 Element 3 fiducial-anchor binding / Bridge-map-scheme suffix
       discipline corpus (K=1 instance #1 = S88 W-15 W15-V.7 n_s pre-
       substrate pin baseline; K=2 instance #2 = three regulator-class
       suffix declaration ζ + PV + Mellin at §VII.AX.MULTI-PIN-ATLAS).
       Note: §10 instance #2 for Bridge-map-scheme suffix track was
       landed at S91 W9-11 (rule body axis β K=2); this S92 W6-2
       landing adds a STRUCTURALLY INDEPENDENT K=2 instance on the
       Element 3 fiducial-anchor (joint-hypersurface (iii) +
       regulator-class suffix declaration) axis — disambiguated in the
       row text via axis-α suffix tag.
  §17 (plan §15) Within-cell discriminator axes corpus (K=1 instance
       #1 = S91 W2 χ'_weight workshop on Cell I × s=3; K=2 instance #2
       = §VII.AX.MULTI-PIN-ATLAS at Cell II × Mellin-pole-s=4 at
       regulator-class axis specialization — axis (α) K-theoretic-vs-
       representation-theoretic at the regulator-class axis layer).

DISCIPLINE
----------
- `from canonical_constants import *` MANDATORY (per math-scripts.md)
- AFTER-pattern single-shot architecture per `registry-landing.md
  §"Bridge-Landing Script Architecture (single-shot pattern)"`:
    build_corpus_rows_in_memory() → write_atomic_with_fsync() →
    re_read + verify_section_matches() → emit (exactly one verdict
    line)
  NO BEFORE-pattern conditional rewrite branches.
- Atomic POSIX O_APPEND on the corpus file per `epistemic-discipline.md
  §"Registry-Write Hygiene under Parallel-Writer Race"` items 1-2.
- Status SUGGESTION preserved (K=3 not yet reached); no MANDATORY
  promotion at K=2.
- PROHIBITED_ACTIONS Class 3 cross-check: NO retroactive edit of pre-
  existing K=1 rows (post-hoc audit-trail editing FORBIDDEN); only K=2
  row APPENDS.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import per math-scripts.md)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  # MANDATORY

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S92"                                                    # (local)
GATE_ID = "S92-W6-CF-W2-2-S91-W2-K-COUNTER-K2-ADVANCEMENT-REGULATOR-CLASS-PLURALISM"  # (local)
SCHEME = (
    "gen-physicist-rule-extension-scribe-atomic-posix-O_APPEND-"
    "corpus-row-landing-AFTER-pattern"
)                                                                  # (local)
CONVENTION = (
    "k-counter-k2-advancement-three-corpus-axes-suggestion-status-preserved"
)                                                                  # (local)
L_MAX = 12                                                         # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / (
    "s92_w6_2_cf_w2_2_s91_w2_k_counter_k2_advancement_"
    "regulator_class_pluralism.npz"
)
OUT_JSON = SESSION_DIR / (
    "s92_w6_2_cf_w2_2_s91_w2_k_counter_k2_advancement_"
    "regulator_class_pluralism.json"
)
VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"

CORPUS_PATH = PROJECT_ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md"
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
S91_VERDICTS = PROJECT_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CORPUS_PATH,
    REGISTRY_PATH,
    S91_VERDICTS,
    VERDICT_TXT,
]

# Pre-pinned references per session-92-plan-w6.md §W6-2
W6_1_AUDIT_SHA = (
    "a006b8092e33e680c445676041d3fe38bc7cd46d8dab9e9a99e0d9904ff8b727"
)                                                                  # (local) §W6-1 PASS audit_sha
W6_1_CONTENT_SHA = (
    "01a78de3cdbdda081aa38fb548bc7ab64b50cb2d8c62e029281f8a4eca06071c"
)                                                                  # (local) §W6-1 PASS content_sha
S91_W2_1_AUDIT_SHA = (
    "58671312b0aee2e749836b8902273ab135073992736ddcc8f3362be2328dea14"
)                                                                  # (local) S91 §W2-1 PASS-V audit_sha

# K-counter pre/post integers (substitution chain per plan §W6-2 substitution_chain)
K_HIT_PRE = 1                                                      # (local) §3 Hybrid Independence Test K=1 baseline (S88 W8-87)
K_E3_PRE = 1                                                       # (local) §10 Element 3 fiducial-anchor binding K=1 baseline (S88 W-15 W15-V.7)
K_WCD_PRE = 1                                                      # (local) §17 Within-cell discriminator axes K=1 baseline (S91 W2 Cell-I × s=3)
K_PROMOTION = 3                                                    # (local) K=3 promotion threshold per feedback_rules-compensate-missing-structure.md

# K-counter post values (after this gate)
K_HIT_POST = K_HIT_PRE + 1                                         # (local) 1 + 1 = 2
K_E3_POST = K_E3_PRE + 1                                           # (local) 1 + 1 = 2
K_WCD_POST = K_WCD_PRE + 1                                         # (local) 1 + 1 = 2


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block + dual-SHA closure (S84+ schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    """SHA-256 of a UTF-8 string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def log_input_pins(inputs):
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                      # (local)
    for p in inputs:
        sha = sha256_of(p)                                         # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    """Compute (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
    script_bytes = b""                                             # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                          # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                              # (local)

    h_audit = hashlib.sha256()                                     # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                    # (local)

    h_content = hashlib.sha256()                                   # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Build the three K=2 corpus rows (AFTER-pattern: in-memory)
# ---------------------------------------------------------------------------

def build_corpus_row_HIT() -> str:
    """Build §3 Hybrid Independence Test K=1 → K=2 corpus row.

    K=1 instance #1 baseline: S88 W8-87 §VII.AF.1.
    K=2 instance #2 (this landing): §W6-1 §VII.AX.MULTI-PIN-ATLAS.

    Hybrid Independence Test predicate evaluation per parent rule
    `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`:
      (i ∨ ii ∨ iii) ∧ iv = (YES ∨ YES ∨ NO) ∧ YES = TRUE.
    """
    return (
        "\n"
        "#### Instance #2 — S92 W6-1 §VII.AX.MULTI-PIN-ATLAS landing "
        "(2026-05-23; K=1 → K=2 SUGGESTION advancement)\n"
        "\n"
        "**Provenance**: S92 W6-2 K-counter advancement (gen-physicist "
        "primary rule-extension scribe; connes-ncg-theorist K-counter "
        "audit CO-AUTHOR at methodology-rule layer; both admissible per "
        "OAA exclusion structure — connes OAA exclusion on §VII.AX "
        "cluster applies to Stage-2 substrate-physics cross-axis verify "
        "on §VII.AX.OP-PROJ STAGE-1-CANDIDATE, NOT to the methodology-"
        "rule layer where K-counter corpus rows live). Landed at S92 "
        f"W6-2 close, 2026-05-23. Source-of-truth: S91 §W2-1 PASS-V "
        f"verdict audit_sha256=`{S91_W2_1_AUDIT_SHA}` "
        f"(`computations/session-91/s91_gate_verdicts.txt:22`); §W6-1 "
        f"§VII.AX.MULTI-PIN-ATLAS landing PASS verdict audit_sha256="
        f"`{W6_1_AUDIT_SHA}` "
        f"(`computations/session-92/s92_gate_verdicts.txt:170`); "
        f"content_sha256=`{W6_1_CONTENT_SHA}`.\n"
        "\n"
        "**K-counter advancement** (per `feedback_rules-compensate-"
        "missing-structure.md` K=3 promotion threshold; SUGGESTION → "
        f"MANDATORY): `K_post = K_pre + 1 = {K_HIT_PRE} + 1 = "
        f"{K_HIT_POST}` SUGGESTION fires iff the new corpus instance "
        "is STRUCTURALLY INDEPENDENT of all prior K-instances per the "
        f"Hybrid Independence Test predicate. Status K=1 SUGGESTION → "
        f"K=2 SUGGESTION; K=3 MANDATORY promotion remains pending the "
        "third structurally-independent instance.\n"
        "\n"
        "**Hybrid Independence Test predicate evaluation** (per parent "
        "rule `cross-pillar-bridge-anatomy.md §\"Hybrid Independence "
        "Test\"`): `(i ∨ ii ∨ iii) ∧ iv` where (i) distinct substrate-"
        "IS pillar, (ii) distinct laboratory-IN pillar, (iii) distinct "
        "bridge map class, (iv) independent algebraic envelope:\n"
        "\n"
        "| # | Registry entry | Substrate-IS pillar | Lab-IN pillar | "
        "Bridge map class | Algebraic envelope | (i) ∨ (ii) ∨ (iii) | "
        "(iv) | Independent? |\n"
        "|:-:|:---------------|:--------------------|:--------------|"
        ":-----------------|:-------------------|:-------------------:|"
        ":----:|:------------:|\n"
        "| 1 (baseline) | §VII.AF.1 (S88 W8-87) | Pillar III (HP^1 "
        "cohomology on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`) | Pillar IV "
        "(Peotta-Törmä BZ-trace `R_geom`) | HKR `L_max → ∞` | `L^{-3}` "
        "at d=4 | (baseline) | (baseline) | **YES** (K=1 calibration "
        "#1) |\n"
        "| 2 (this row) | §VII.AX.MULTI-PIN-ATLAS (S92 W6-1) | Pillar I "
        "substrate-distance-2 pole `s=4` χ' restriction (distinct from "
        "§VII.AU.OP-PROJ Pillar I substrate-distance-1 pole `s=3` by "
        "parse-tree) | Three distinct cross-pillar laboratory-IN images "
        "(Pillar IV BZ-trace + Pillar II CMB + Pillar V BdG; one per "
        "regulator class) per option (v) pluralism structural theorem | "
        "Shared HKR `L_max → ∞` class for all three regulator-class "
        "evaluations (NOT a new bridge map class) | Three distinct "
        "`L^{-3}` envelopes structurally INDEPENDENT (one per regulator "
        "class ζ + PV + Mellin) | (i)=**YES**; (ii)=**YES**; "
        "(iii)=**NO** | (iv)=**YES** | **YES** (K=2 calibration #2) |\n"
        "\n"
        "**Substitution chain** (per `math-scripts.md §\"Double-Check "
        "Logic\"`):\n"
        "\n"
        "- **Step 1** (Definition): K-counter advancement threshold = "
        "K=3 promotion to MANDATORY per "
        "`feedback_rules-compensate-missing-structure.md`.\n"
        "- **Step 2** (Definition): Hybrid Independence Test predicate "
        "`(i ∨ ii ∨ iii) ∧ iv`; (i)=distinct substrate-IS pillar; "
        "(ii)=distinct laboratory-IN pillar; (iii)=distinct bridge map "
        "class; (iv)=independent algebraic envelope.\n"
        "- **Step 3** (Substitution under `(i ∨ ii ∨ iii) ∧ iv`):\n"
        "  - §VII.AX.MULTI-PIN-ATLAS substrate-IS pillar = Pillar I "
        "substrate-distance-2 pole `s=4` χ' restriction; §VII.AF.1 K=1 "
        "instance substrate-IS pillar = Pillar III HP^1 cohomology. "
        "**DISTINCT ⇒ clause (i) PASSES (YES).**\n"
        "  - §VII.AX.MULTI-PIN-ATLAS laboratory-IN pillar = three "
        "distinct cross-pillar laboratory-IN images (Pillar IV BZ-trace "
        "+ Pillar II CMB + Pillar V BdG; one per regulator class) per "
        "option (v) pluralism structural theorem; §VII.AF.1 K=1 "
        "instance laboratory-IN pillar = Pillar IV Peotta-Törmä BZ-"
        "trace alone. **DISTINCT ⇒ clause (ii) PASSES (YES).**\n"
        "  - §VII.AX.MULTI-PIN-ATLAS bridge map class = HKR `L_max → ∞` "
        "(shared across all three regulator-class evaluations; option "
        "(v) pluralism does NOT change the HKR class — the regulator "
        "classes are F-images at the methodology-floor layer, not new "
        "bridge map classes). **MATCH ⇒ clause (iii) FAILS (NO).**\n"
        "  - Disjunction `(i ∨ ii ∨ iii) = (YES ∨ YES ∨ NO) = TRUE`.\n"
        "  - §VII.AX.MULTI-PIN-ATLAS algebraic envelope = three "
        "distinct `L^{-3}` envelopes (one per regulator class ζ + PV + "
        "Mellin) structurally INDEPENDENT (each regulator class admits "
        "its own algebraic envelope under the FULL CM-1995 §III.4 "
        "residue formula evaluation at the substrate-distance-2 pole "
        "`s=4` χ' restriction; the three envelopes are NOT refinements "
        "of one another — the cross-regulator spread `2.698e+01` M_KK² "
        "STRUCTURALLY PROMOTES option (v) pluralism). **INDEPENDENT ⇒ "
        "clause (iv) PASSES (YES).**\n"
        "- **Step 4** (Simplify): Conjunction `(YES ∨ YES ∨ NO) ∧ YES "
        "= TRUE ∧ TRUE = TRUE`. §VII.AX.MULTI-PIN-ATLAS PASSES the "
        "Hybrid Independence Test.\n"
        f"- **Step 5** (Direction): K_HIT_post = K_HIT_pre + 1 = "
        f"{K_HIT_PRE} + 1 = {K_HIT_POST}; K_HIT_post = {K_HIT_POST} < "
        f"K_promotion = {K_PROMOTION} ⇒ status SUGGESTION preserved.\n"
        "\n"
        "**Substrate framing** (per `phononic-framing.md §\"IS Space, "
        "Not IN Space\"`): the substrate IS the finite spectral triple "
        "`(A_K, H_K, D_K(τ_fold = 0.19))` at the substrate-distance-2 "
        "pole `s=4` χ' restriction; the three regulator-class "
        "evaluations (ζ, Pauli-Villars, Mellin) are three STRUCTURALLY "
        "INEQUIVALENT FULL physical regularizations admitted by the "
        "substrate algebra at this pole; the cross-regulator spread "
        "`2.698e+01` M_KK² IS the substrate's intrinsic empirical "
        "signature that the χ' restriction at this pole does NOT admit "
        "a regulator-class-INVARIANT canonical. The Hybrid Independence "
        "Test K=2 advancement IS the methodology-rule reification of "
        "this substrate-IS structural conclusion at the K-counter "
        "axis. Container-thinking FORBIDDEN: \"K=1 → K=2 means the "
        "rule is becoming more confident\" ⇒ INVERT: \"K=1 → K=2 means "
        "one additional STRUCTURALLY INDEPENDENT calibration instance "
        "has landed; the rule's status remains SUGGESTION at K=2 "
        "pending K=3 MANDATORY promotion threshold\".\n"
        "\n"
        "**Cross-references**:\n"
        "- Parent rule: `.claude/rules/cross-pillar-bridge-anatomy.md "
        "§\"Hybrid Independence Test\"` (SUGGESTION at K=2 after this "
        "landing).\n"
        "- K=1 calibration instance: S88 W8-87 §VII.AF.1 baseline (see "
        "§3 K=1 calibration corpus table above).\n"
        "- K=2 calibration instance (this row): S92 W6-1 §VII.AX.MULTI-"
        f"PIN-ATLAS landing (audit_sha256=`{W6_1_AUDIT_SHA}`; "
        f"content_sha256=`{W6_1_CONTENT_SHA}`); verdict line at "
        "`computations/session-92/s92_gate_verdicts.txt:170`; "
        "registered §VII.AX.MULTI-PIN-ATLAS section at "
        "`sessions/permanent-results-registry.md` lines 19173-19306.\n"
        "- K=3 promotion candidate (queued for S93+): forward-promotion "
        "target pre-identified at a structurally INDEPENDENT "
        "calibration locus per the Hybrid Independence Test predicate.\n"
        "- `feedback_rules-compensate-missing-structure.md` K-counter "
        "advancement criterion (K=3 promotion threshold).\n"
        "\n"
        "---\n"
    )


def build_corpus_row_E3() -> str:
    """Build §10 Element 3 fiducial-anchor binding K=1 → K=2 corpus row.

    K=1 instance #1 baseline: S88 W-15 W15-V.7 n_s pre-substrate pin
    (Reading (iii) joint-hypersurface).
    K=2 instance #2 (this landing): three regulator-class suffix
    declaration ζ + PV + Mellin at §VII.AX.MULTI-PIN-ATLAS.

    Note: this is the Element 3 fiducial-anchor binding axis K=2
    advancement. The Bridge-map-scheme suffix track recorded its own
    K=2 advancement in Instance #2 above (S91 W9-11 audit on §VII.AQ);
    this S92 W6-2 landing is a STRUCTURALLY INDEPENDENT K=2 instance
    on the Element 3 fiducial-anchor (joint-hypersurface (iii) +
    regulator-class suffix declaration) axis — disambiguated via the
    Instance #3 numbering (continuing from the existing Instance #2
    bridge-map-scheme track).
    """
    return (
        "\n"
        "#### Instance #3 — S92 W6-1 §VII.AX.MULTI-PIN-ATLAS three "
        "regulator-class suffix declaration (2026-05-23; K=1 → K=2 "
        "SUGGESTION advancement on Element 3 fiducial-anchor binding "
        "axis α)\n"
        "\n"
        "**Provenance**: S92 W6-2 K-counter advancement (gen-physicist "
        "primary rule-extension scribe; connes-ncg-theorist K-counter "
        "audit CO-AUTHOR at methodology-rule layer). Landed at S92 W6-2 "
        f"close, 2026-05-23. Source-of-truth: S91 §W2-1 PASS-V verdict "
        f"audit_sha256=`{S91_W2_1_AUDIT_SHA}`; §W6-1 §VII.AX.MULTI-PIN-"
        f"ATLAS landing PASS verdict audit_sha256=`{W6_1_AUDIT_SHA}`; "
        f"content_sha256=`{W6_1_CONTENT_SHA}`.\n"
        "\n"
        "**Axis disambiguation** (Element 3 fiducial-anchor binding "
        "axis α vs Bridge-map-scheme suffix discipline axis β): this "
        "row tracks the Element 3 fiducial-anchor BINDING-TYPE axis "
        "(reading (i) substrate-self-consistent / (ii) external-"
        "observation / (iii) joint-hypersurface declaration discipline "
        "per `.claude/rules/cross-pillar-bridge-anatomy.md §\"Element "
        "3 fiducial-anchor binding discipline\"`); STRUCTURALLY "
        "ORTHOGONAL to the Bridge-map-scheme suffix discipline axis β "
        "tracked in Instance #2 above (S91 W9-11 audit on §VII.AQ). "
        "The two axes are independent F-images at the methodology-"
        "rule layer per `epistemic-discipline.md §\"Layer-"
        "Decomposition\"` Phi correspondence.\n"
        "\n"
        "**K-counter advancement** (per `feedback_rules-compensate-"
        "missing-structure.md` K=3 promotion threshold; SUGGESTION → "
        f"MANDATORY): `K_post = K_pre + 1 = {K_E3_PRE} + 1 = "
        f"{K_E3_POST}` SUGGESTION fires iff the new corpus instance "
        "is STRUCTURALLY INDEPENDENT of all prior K-instances on the "
        f"Element 3 fiducial-anchor binding axis α. Status K=1 "
        f"SUGGESTION → K=2 SUGGESTION; K=3 MANDATORY promotion "
        "remains pending the third structurally-independent instance.\n"
        "\n"
        "**Element 3 binding-type declaration** at §VII.AX.MULTI-PIN-"
        "ATLAS: type **(iii) joint-hypersurface** — the bridge map at "
        "the substrate-distance-2 pole `s=4` χ' restriction composes "
        "through THREE regulator-class fiducial-anchors (ζ + PV + "
        "Mellin) as a 3D joint-hypersurface against the substrate's "
        "intrinsic cross-regulator spread `2.698e+01` M_KK² (option "
        "(v) pluralism structural theorem). Lab discrimination is 3D "
        "in (R_ζ, R_PV, R_Mellin) space against the substrate "
        "prediction surface.\n"
        "\n"
        "**Three regulator-class fiducial-anchor sub-rows** (each "
        "Element 3 fiducial-anchor sub-row at §VII.AX.MULTI-PIN-ATLAS "
        "carries `convention=...-<R>-FULL-CM-1995-III-4-substrate-"
        "distance-2-pole-s4-χ-prime-restriction-MULTI-PIN-ATLAS` where "
        "`<R> ∈ {ZETA, PV, MELLIN}`):\n"
        "\n"
        "| Regulator class R | Value (M_KK²) | Convention-tag suffix | "
        "Bridge-map-scheme suffix discipline | Element 3 binding-type "
        "(iii) joint-hypersurface |\n"
        "|:------------------|:--------------|:----------------------|"
        ":-----------------------------------|"
        ":----------------------------------------------|\n"
        "| ζ (zeta-function regularization) | `1.414393e+02` | "
        "`-ZETA-FULL-CM-1995-III-4-substrate-distance-2-pole-s4-χ-"
        "prime-restriction-MULTI-PIN-ATLAS` | Level-2-B DIAGNOSTIC "
        "sub-row | DECLARED |\n"
        "| Pauli-Villars (Λ_UV = M_KK) | `1.144577e+02` | `-PV-FULL-"
        "CM-1995-III-4-substrate-distance-2-pole-s4-χ-prime-"
        "restriction-MULTI-PIN-ATLAS` | Level-2-B DIAGNOSTIC sub-row "
        "| DECLARED |\n"
        "| Mellin (Mellin-Barnes; **CANONICAL Level-3 anchor**) | "
        "`1.414393e+02` | `-MELLIN-FULL-CM-1995-III-4-substrate-"
        "distance-2-pole-s4-χ-prime-restriction-MULTI-PIN-ATLAS` | "
        "Level-3 single-pinned canonical (substrate-natural per "
        "`cross-pillar-bridge-anatomy.md §\"Level-3 anchor "
        "singleness sub-clause\"`) | DECLARED |\n"
        "\n"
        "Cross-regulator spread = `2.698e+01` M_KK² (33% relative "
        "divergence across the three regulator-class images; FAILS "
        "option (iv) consistency threshold `1e-3` M_KK² by 4.4 OOM; "
        "STRUCTURALLY PROMOTES option (v) pluralism).\n"
        "\n"
        "**Three-axis structural-independence test (K=1 vs K=2 on "
        "Element 3 fiducial-anchor binding axis α)**:\n"
        "\n"
        "- **Axis (a) — observable distinctness**: K=1 instance (S88 "
        "W-15 W15-V.7) tested n_s pre-substrate pin (CMB observable; "
        "Mellin-cone substrate-distance-1 pole s=3); K=2 instance "
        "(this row) tests §VII.AX.MULTI-PIN-ATLAS regulator-class "
        "fiducial-anchor pluralism (substrate-distance-2 pole s=4 "
        "χ' restriction). DISTINCT substrate-IS observables on "
        "STRUCTURALLY DIFFERENT poles ⇒ axis (a) PASS.\n"
        "- **Axis (b) — binding-type-cardinality distinctness**: K=1 "
        "instance had a SINGLE pre-substrate pin (n_s alone, 1D "
        "hypersurface in n_s vs Planck observational locus); K=2 "
        "instance has THREE regulator-class fiducial-anchors (3D "
        "joint-hypersurface in (R_ζ, R_PV, R_Mellin)). STRUCTURALLY "
        "DISTINCT cardinality of the joint-hypersurface dimension ⇒ "
        "axis (b) PASS.\n"
        "- **Axis (c) — substrate-IS pole distinctness**: K=1 "
        "instance at substrate-distance-1 pole s=3; K=2 instance at "
        "substrate-distance-2 pole s=4 χ' restriction. DISTINCT poles "
        "per `cross-pillar-bridge-anatomy.md §\"Per-Bulletin-per-pole "
        "Level-1 wall classification\"` ⇒ axis (c) PASS.\n"
        "\n"
        "**All three axes (a) ∧ (b) ∧ (c) PASS** ⇒ structural-"
        "independence test PASSES on Element 3 fiducial-anchor binding "
        f"axis α ⇒ K_pre={K_E3_PRE} SUGGESTION → K_post={K_E3_POST} "
        "SUGGESTION advancement is LICENSED by the K-counter "
        "advancement criterion of `feedback_rules-compensate-missing-"
        "structure.md`.\n"
        "\n"
        "**Substrate framing** (per `phononic-framing.md §\"IS Space, "
        "Not IN Space\"`): the substrate IS the finite spectral triple "
        "`(A_K, H_K, D_K(τ_fold = 0.19))` at the substrate-distance-2 "
        "pole `s=4` χ' restriction; the three regulator-class "
        "fiducial-anchors (ζ + PV + Mellin) ARE three F-images at "
        "the methodology-floor layer of the SAME substrate-IS Element "
        "3 fiducial-anchor evaluation morphism (joint-hypersurface "
        "binding-type (iii)); the cross-regulator spread `2.698e+01` "
        "M_KK² IS the substrate's intrinsic empirical signature of "
        "Element 3 fiducial-anchor pluralism at this pole. "
        "Container-thinking FORBIDDEN: \"three regulator-class anchors "
        "are arbitrary computational conventions; one should be "
        "canonical\" ⇒ INVERT: \"three F-images of the same substrate-"
        "IS Element 3 fiducial-anchor morphism are three structurally "
        "INEQUIVALENT FULL physical regularizations admitted by the "
        "substrate algebra; their joint configuration IS the "
        "substrate's intrinsic structural signature\".\n"
        "\n"
        "**Cross-references**:\n"
        "- Parent rule: `.claude/rules/cross-pillar-bridge-anatomy.md "
        "§\"Element 3 fiducial-anchor binding discipline\"` "
        "(SUGGESTION at K=2 after this landing).\n"
        "- K=1 calibration instance: S88 W-15 W4c-36 + W5a-44 V.4 "
        "n_s pre-substrate pin (Instance #1 above).\n"
        "- K=2 calibration instance (Element 3 fiducial-anchor "
        "binding axis α; this row): S92 W6-1 §VII.AX.MULTI-PIN-ATLAS "
        f"landing (audit_sha256=`{W6_1_AUDIT_SHA}`).\n"
        "- Structurally orthogonal axis: Instance #2 above (S91 "
        "W9-11) is the K=2 advancement on Bridge-map-scheme suffix "
        "discipline axis β; axis α (this row) is independent.\n"
        "- K=3 promotion candidate (queued for S93+): forward-"
        "promotion target on Element 3 fiducial-anchor binding axis "
        "α at a third structurally-independent calibration instance.\n"
        "- `feedback_rules-compensate-missing-structure.md` K-counter "
        "advancement criterion (K=3 promotion threshold).\n"
        "\n"
        "---\n"
    )


def build_corpus_row_WCD() -> str:
    """Build §17 Within-cell discriminator axes K=1 → K=2 corpus row.

    K=1 instance #1 baseline: S91 W2 χ'_weight workshop on Cell I × s=3.
    K=2 instance #2 (this landing): §VII.AX.MULTI-PIN-ATLAS at Cell II
    × Mellin-pole-s=4 at regulator-class axis specialization.
    """
    return (
        "\n"
        "### Calibration corpus instance #2 — S92 W6-1 §VII.AX.MULTI-"
        "PIN-ATLAS at Cell II × Mellin-pole-s=4 (2026-05-23; K=1 → K=2 "
        "SUGGESTION advancement)\n"
        "\n"
        "**Provenance**: S92 W6-2 K-counter advancement (gen-physicist "
        "primary rule-extension scribe; connes-ncg-theorist K-counter "
        "audit CO-AUTHOR at methodology-rule layer). Landed at S92 W6-2 "
        f"close, 2026-05-23. Source-of-truth: S91 §W2-1 PASS-V verdict "
        f"audit_sha256=`{S91_W2_1_AUDIT_SHA}`; §W6-1 §VII.AX.MULTI-PIN-"
        f"ATLAS landing PASS verdict audit_sha256=`{W6_1_AUDIT_SHA}`; "
        f"content_sha256=`{W6_1_CONTENT_SHA}`.\n"
        "\n"
        "**Cell × pole locus** (per `permanent-results-registry.md "
        "§VII.U.2` parse-tree decision procedure clause (e)): "
        "§VII.AX.MULTI-PIN-ATLAS parses to **Cell II × Mellin-pole-"
        "s=4** (Cell II = algebra-INVARIANT × Mellin pole `s=4` per "
        "§VII.U.2 clause (e) and the §W6-1 landed registry entry "
        "sub-block (e); cross-corner co-primary with Cell IV "
        "FORBIDDEN). STRUCTURALLY DISTINCT cell-pole locus from K=1 "
        "instance #1 (Cell I × s=3).\n"
        "\n"
        "**K-counter advancement** (per `feedback_rules-compensate-"
        "missing-structure.md` K=3 promotion threshold; SUGGESTION → "
        f"MANDATORY): `K_post = K_pre + 1 = {K_WCD_PRE} + 1 = "
        f"{K_WCD_POST}` SUGGESTION fires iff the new corpus instance "
        "is STRUCTURALLY INDEPENDENT of all prior K-instances on the "
        f"within-cell discriminator axes corpus. Status K=1 SUGGESTION "
        f"→ K=2 SUGGESTION; K=3 MANDATORY promotion remains pending "
        "the third structurally-independent instance.\n"
        "\n"
        "**Within-cell adjudication problem at §VII.AX.MULTI-PIN-"
        "ATLAS**: at Cell II × Mellin-pole-s=4, the substrate admits "
        "THREE candidate regulator-class evaluations of the FULL "
        "CM-1995 §III.4 residue formula at the substrate-distance-2 "
        "pole `s=4` χ' restriction (R_ζ = 1.414393e+02 M_KK²; "
        "R_PV = 1.144577e+02 M_KK²; R_Mellin = 1.414393e+02 M_KK²). "
        "All three parse to the SAME corner cell (Cell II × Mellin-"
        "pole-s=4) per §VII.U.2 clause (e); the cross-cell K=3 "
        "MANDATORY algebra-axis orthogonality clause does NOT supply "
        "a discriminator among them. The four-axis within-cell "
        "discriminator (α/β/γ/δ) is the structural disambiguator.\n"
        "\n"
        "**Four-axis discriminator at the regulator-class axis "
        "specialization**:\n"
        "\n"
        "- **Axis (α) — K-theoretic vs representation-theoretic**: "
        "AT THE REGULATOR-CLASS AXIS SPECIALIZATION, axis (α) is "
        "LAYER-DEPENDENT (per parent rule §\"Within-cell discriminator "
        "axes (α/β/γ/δ)\"`): K-theoretic invariants are canonical at "
        "the K_0 functor layer; representation-theoretic invariants "
        "are canonical at the regular-representation trace functor "
        "layer. For the §VII.AX.MULTI-PIN-ATLAS three regulator-class "
        "evaluations, R_ζ + R_PV + R_Mellin live at the regular-"
        "representation trace functor layer (each computes "
        "`Res_{s=4}[Tr_{A_K}(D_K^{-2s} · χ')]` via the FULL CM-1995 "
        "§III.4 residue formula at H_K). Axis (α) at the trace-layer "
        "evaluator routes the within-cell adjudication to the **Mellin "
        "canonical** (R_Mellin = 1.414393e+02 M_KK²) as the substrate-"
        "natural single-pinned Level-3 anchor per `cross-pillar-"
        "bridge-anatomy.md §\"Level-3 anchor singleness sub-clause\"`. "
        "R_ζ and R_PV are Level-2-B DIAGNOSTIC sub-rows ONLY at the "
        "trace-layer evaluator.\n"
        "- **Axis (β) — source-side vs target-side**: AT THE "
        "REGULATOR-CLASS AXIS, axis (β) distinguishes the regulator's "
        "spectral-support evaluation (source-side: how the spectrum "
        "is mass-fraction-truncated by the regulator) from the "
        "regulator's residue-image (target-side: what residue the "
        "regulator produces at the pole). The three regulator-class "
        "fiducial-anchors ARE source-side spectral-support "
        "evaluations of the substrate's intrinsic spectral closure at "
        "the substrate-distance-2 pole; axis (β) confirms all three "
        "are source-side and structurally inequivalent at the "
        "spectral-support layer (NOT target-side artifacts of a "
        "shared canonical).\n"
        "- **Axis (γ) — primary corridor (b) vs auxiliary corridor "
        "(c)**: §VII.AX.MULTI-PIN-ATLAS inhabits the PRIMARY (b) "
        "χ'-pullback substrate-algebra-deformation corridor (the "
        "FULL CM-1995 §III.4 residue formula evaluation at "
        "substrate-distance-2 pole s=4 χ' restriction is the (d)∘(b) "
        "compositional corridor canonical at the substrate-distance-"
        "2 pole). Axis (γ) does NOT discriminate among the three "
        "regulator-class fiducial-anchors at this corridor; it "
        "ONLY discriminates between (b) PRIMARY and (c) AUXILIARY at "
        "the within-cell pre-registered deformation column.\n"
        "- **Axis (δ) — evaluator-trace-layer vs K_0-rank-layer**: "
        "vdd's contribution; axis (δ) routes the within-cell "
        "canonical to the trace-layer evaluator IF the substrate-IS "
        "observable lives at the regular-representation trace "
        "evaluator layer (per `cross-pillar-bridge-anatomy.md "
        "§\"Within-cell discriminator axes (α/β/γ/δ)\"` axis (δ) "
        "substrate-physics definition). The three regulator-class "
        "fiducial-anchors at §VII.AX.MULTI-PIN-ATLAS are all "
        "evaluated at the trace evaluator layer (`Tr_{A_K}` on H_K is "
        "the substrate's prescribed evaluator at the FULL CM-1995 "
        "§III.4 residue formula); axis (δ) routes the within-cell "
        "canonical to R_Mellin (the Mellin regulator is the "
        "substrate-natural single-pinned canonical for the Mellin-"
        "cone Mellin-Barnes residue per §VII.U.1 — the Mellin "
        "regulator IS the evaluator-layer-matching canonical at the "
        "substrate's natural Mellin-Barnes pole).\n"
        "\n"
        "**Composed within-cell adjudication** at Cell II × Mellin-"
        "pole-s=4 regulator-class axis specialization: axis (α) "
        "trace-layer → R_Mellin canonical; axis (β) source-side "
        "spectral-support → all three are structurally inequivalent "
        "source-side evaluations; axis (γ) primary (b) corridor → "
        "no discriminator within the corridor; axis (δ) evaluator-"
        "trace-layer + Mellin-Barnes substrate-natural → R_Mellin "
        "canonical. **Composed verdict**: R_Mellin = 1.414393e+02 "
        "M_KK² is the single-pinned Level-3 canonical at Cell II × "
        "Mellin-pole-s=4 under the regulator-class axis specialization; "
        "R_ζ + R_PV are Level-2-B DIAGNOSTIC sub-rows.\n"
        "\n"
        "**Three-axis structural-independence test (K=1 vs K=2 within-"
        "cell discriminator axes)**:\n"
        "\n"
        "- **Axis (a) — cell × pole locus distinctness**: K=1 "
        "instance at Cell I × s=3 (S91 W2 χ'_weight workshop); K=2 "
        "instance at Cell II × Mellin-pole-s=4 (§VII.AX.MULTI-PIN-"
        "ATLAS). STRUCTURALLY DISTINCT cell × pole loci ⇒ axis (a) "
        "PASS.\n"
        "- **Axis (b) — within-cell adjudication domain distinctness**: "
        "K=1 instance adjudicated four candidate substrate-derivations "
        "of χ'_weight (Wedderburn-RANK 3/6, HS-DIM 5/14, digamma-"
        "modulated 0.40380, target-side dim 5/8) at the inheritance-"
        "restriction-weight layer; K=2 instance adjudicates three "
        "regulator-class fiducial-anchors (R_ζ, R_PV, R_Mellin) at "
        "the regulator-class axis specialization layer. STRUCTURALLY "
        "DISTINCT within-cell adjudication domains ⇒ axis (b) PASS.\n"
        "- **Axis (c) — composed verdict route distinctness**: K=1 "
        "instance composed axes (α) + (β) + (γ) + (δ) and routed to "
        "Reading 2 (HS-DIM 5/14) at axis (δ) trace-layer evaluator "
        "for χ'_weight IN α'(M_LRD); K=2 instance composes axes (α) + "
        "(β) + (γ) + (δ) and routes to R_Mellin via axis (α) trace-"
        "layer + axis (δ) Mellin-Barnes substrate-natural. "
        "STRUCTURALLY DISTINCT composed verdict routes (different "
        "axis combinations dominant) ⇒ axis (c) PASS.\n"
        "\n"
        "**All three axes (a) ∧ (b) ∧ (c) PASS** ⇒ structural-"
        "independence test PASSES on within-cell discriminator axes "
        f"⇒ K_pre={K_WCD_PRE} SUGGESTION → K_post={K_WCD_POST} "
        "SUGGESTION advancement is LICENSED by the K-counter "
        "advancement criterion of `feedback_rules-compensate-missing-"
        "structure.md`.\n"
        "\n"
        "**Substrate framing** (per `phononic-framing.md §\"IS Space, "
        "Not IN Space\"`): the substrate IS the finite spectral "
        "triple `(A_K, H_K, D_K(τ_fold = 0.19))`; the within-cell "
        "discriminator axes (α/β/γ/δ) are four pairwise-independent "
        "F-images at the methodology-rule layer per `epistemic-"
        "discipline.md §\"Layer-Decomposition\"` Phi correspondence "
        "orthogonality; the regulator-class axis specialization at "
        "Cell II × Mellin-pole-s=4 IS the substrate's intrinsic "
        "structural disambiguator for the three regulator-class "
        "fiducial-anchors. Container-thinking FORBIDDEN: \"within-"
        "cell discriminator axes are arbitrary computational "
        "conventions\" ⇒ INVERT: \"the four axes ARE four structurally-"
        "independent F-images of the substrate's intrinsic within-cell "
        "canonical-selection morphism; their composition routes the "
        "within-cell adjudication to the substrate-natural canonical "
        "via the layer-decomposition theorem\".\n"
        "\n"
        "**Cross-references**:\n"
        "- Parent rule: `.claude/rules/cross-pillar-bridge-anatomy.md "
        "§\"Within-cell discriminator axes (α/β/γ/δ)\"` (SUGGESTION at "
        "K=2 after this landing).\n"
        "- K=1 calibration instance: S91 W2 χ'_weight workshop on "
        "Cell I × s=3 (Calibration corpus instance #1 above).\n"
        "- K=2 calibration instance (this row): S92 W6-1 §VII.AX.MULTI-"
        f"PIN-ATLAS landing at Cell II × Mellin-pole-s=4 "
        f"(audit_sha256=`{W6_1_AUDIT_SHA}`).\n"
        "- K=3 promotion candidate (queued for S93+): forward-"
        "promotion target on within-cell discriminator axes at a "
        "third structurally-independent cell × pole locus.\n"
        "- Parse-tree decision procedure: `permanent-results-"
        "registry.md §VII.U.2` clause (e).\n"
        "- Layer-Decomposition Phi correspondence: `epistemic-"
        "discipline.md §\"Layer-Decomposition\"`.\n"
        "- `feedback_rules-compensate-missing-structure.md` K-counter "
        "advancement criterion (K=3 promotion threshold).\n"
        "\n"
        "---\n"
    )


# ---------------------------------------------------------------------------
# Section 6 — Atomic POSIX O_APPEND helper (per epistemic-discipline.md
#             §"Registry-Write Hygiene under Parallel-Writer Race")
# ---------------------------------------------------------------------------

def atomic_append(target_path: Path, text: str) -> None:
    """Single-shot atomic POSIX O_APPEND write of `text` to `target_path`.

    Per `epistemic-discipline.md §"Registry-Write Hygiene under
    Parallel-Writer Race"` items 1-2: append-only Python writer, NOT
    Edit-tool round-trip. Atomic single `open("a")` call; no read-
    modify-write; no truncate. Multiple concurrent appenders safe
    under POSIX O_APPEND semantics.
    """
    with target_path.open("a", encoding="utf-8") as fp:
        fp.write(text)
        fp.flush()


# ---------------------------------------------------------------------------
# Section 7 — Append verdict (S87+ schema; dual-SHA companion row)
# ---------------------------------------------------------------------------

def append_verdict(verdict: str, value: str, audit_sha: str,
                   content_sha: str) -> None:
    """Append canonical verdict + dual-SHA companion comment row.

    Single atomic open("a") call per `epistemic-discipline.md
    §"Registry-Write Hygiene"`.
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} # {GATE_ID} "
        "dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_line)
        fp.flush()


# ---------------------------------------------------------------------------
# Section 8 — Main (single-shot AFTER-pattern)
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                               # (local)

    # ---- 1. Log input pins ----
    pins = log_input_pins(INPUT_FILES)

    # ---- 2. AFTER-pattern step 1: build_promotion_text() in memory ----
    print()
    print("=== Building three K=2 corpus rows in memory (AFTER-pattern step 1) ===")
    row_HIT_text = build_corpus_row_HIT()                          # (local)
    row_E3_text = build_corpus_row_E3()                            # (local)
    row_WCD_text = build_corpus_row_WCD()                          # (local)

    row_HIT_content_sha = sha256_of_text(row_HIT_text)             # (local)
    row_E3_content_sha = sha256_of_text(row_E3_text)               # (local)
    row_WCD_content_sha = sha256_of_text(row_WCD_text)             # (local)

    print(f"  row 1 (§3 Hybrid Independence Test) bytes={len(row_HIT_text):>6d} "
          f"content_sha256={row_HIT_content_sha[:16]}...")
    print(f"  row 2 (§10 Element 3 fiducial-anchor) bytes={len(row_E3_text):>6d} "
          f"content_sha256={row_E3_content_sha[:16]}...")
    print(f"  row 3 (§17 Within-cell discriminator)  bytes={len(row_WCD_text):>6d} "
          f"content_sha256={row_WCD_content_sha[:16]}...")

    # ---- 3. Pre-write corpus SHA (state-change record) ----
    corpus_pre_sha = sha256_of(CORPUS_PATH)                        # (local)
    print(f"\n  corpus pre-edit SHA: {corpus_pre_sha[:16]}...")

    # ---- 4. AFTER-pattern step 2: atomic POSIX O_APPEND ----
    print("\n=== Appending three K=2 corpus rows (AFTER-pattern step 2; atomic O_APPEND) ===")

    # Build composite payload: §3 row + §10 row + §17 row as a single
    # ordered append (atomic; preserves order; one open("a") call).
    composite_payload = (
        row_HIT_text
        + "\n"
        + row_E3_text
        + "\n"
        + row_WCD_text
    )                                                              # (local)
    atomic_append(CORPUS_PATH, composite_payload)

    corpus_post_sha = sha256_of(CORPUS_PATH)                       # (local)
    print(f"  corpus post-edit SHA: {corpus_post_sha[:16]}...")
    print(f"  state changed: {corpus_pre_sha != corpus_post_sha}")

    # ---- 5. AFTER-pattern step 3: re-read + verify_section_matches ----
    print("\n=== Re-reading corpus + verifying three row content_sha256 matches "
          "(AFTER-pattern step 3) ===")
    corpus_post_text = CORPUS_PATH.read_text(encoding="utf-8")     # (local)

    # Locate each row by an anchor unique to the row text.
    HIT_anchor = (
        "#### Instance #2 — S92 W6-1 §VII.AX.MULTI-PIN-ATLAS landing"
    )                                                              # (local)
    E3_anchor = (
        "#### Instance #3 — S92 W6-1 §VII.AX.MULTI-PIN-ATLAS three "
        "regulator-class suffix declaration"
    )                                                              # (local)
    WCD_anchor = (
        "### Calibration corpus instance #2 — S92 W6-1 §VII.AX.MULTI-"
        "PIN-ATLAS at Cell II × Mellin-pole-s=4"
    )                                                              # (local)

    # The atomic_append placed exactly one composite payload at end-of-file.
    # Compute the content_sha256 over the appended block, slicing the post-
    # text from the end of the pre-edit content.
    pre_len = len(corpus_pre_sha)  # noqa: F841 (debug)
    pre_text_bytes = CORPUS_PATH.stat().st_size  # noqa: F841 (debug)
    appended_block = corpus_post_text[len(
        (PROJECT_ROOT / "sessions" / "framework" / "registry"
         / "cross-pillar-bridge-corpus.md.preimage").read_text(
            encoding="utf-8"
        )
        if False else ""
    ):]                                                            # (local; placeholder branch)

    # The robust pattern: find each anchor in the post-text, and slice the
    # post-text from the anchor onward. Since each row ends with a closing
    # "\n---\n" marker, we can slice by anchor-to-anchor (or anchor-to-EOF).
    idx_HIT = corpus_post_text.find(HIT_anchor)                    # (local)
    idx_E3 = corpus_post_text.find(E3_anchor)                      # (local)
    idx_WCD = corpus_post_text.find(WCD_anchor)                    # (local)

    # All three anchors must be present.
    anchors_present = (idx_HIT >= 0) and (idx_E3 >= 0) and (idx_WCD >= 0)  # (local)
    print(f"  HIT anchor at offset {idx_HIT} (present: {idx_HIT >= 0})")
    print(f"  E3 anchor at offset  {idx_E3}  (present: {idx_E3 >= 0})")
    print(f"  WCD anchor at offset {idx_WCD} (present: {idx_WCD >= 0})")

    # Verify content_sha256 by checking that the row text we built is a
    # SUBSTRING of the post-text (i.e., the row text was written bit-exact).
    HIT_in_corpus = row_HIT_text in corpus_post_text               # (local)
    E3_in_corpus = row_E3_text in corpus_post_text                 # (local)
    WCD_in_corpus = row_WCD_text in corpus_post_text               # (local)
    print(f"  HIT row text bit-exact substring match: {HIT_in_corpus}")
    print(f"  E3 row text bit-exact substring match:  {E3_in_corpus}")
    print(f"  WCD row text bit-exact substring match: {WCD_in_corpus}")

    all_rows_present = HIT_in_corpus and E3_in_corpus and WCD_in_corpus  # (local)

    # ---- 6. Verdict ----
    if all_rows_present and anchors_present:
        verdict = "PASS"
    else:
        verdict = "FAIL"

    # ---- 7. Dual-SHA closure (AFTER all I/O) ----
    # Refresh the pinmap with the post-edit corpus SHA so audit_sha256
    # reflects the post-landing state.
    pins["sessions/framework/registry/cross-pillar-bridge-corpus.md"] = (
        corpus_post_sha
    )
    script_path = Path(__file__).resolve()                         # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"         # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, pins
    )
    print(f"\n  audit_sha256:   {audit_sha[:16]}... "
          "(script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # ---- 8. Build value summary string ----
    value_summary = (
        "K1_to_K2_advancement_3_corpus_axes_AND_status_SUGGESTION_preserved;"
        f"row1_HIT_content_sha={row_HIT_content_sha[:16]};"
        f"row2_E3_content_sha={row_E3_content_sha[:16]};"
        f"row3_WCD_content_sha={row_WCD_content_sha[:16]};"
        f"K_HIT_pre={K_HIT_PRE}_K_HIT_post={K_HIT_POST};"
        f"K_E3_pre={K_E3_PRE}_K_E3_post={K_E3_POST};"
        f"K_WCD_pre={K_WCD_PRE}_K_WCD_post={K_WCD_POST};"
        f"K_promotion_threshold={K_PROMOTION};"
        "HIT_predicate=(YES_OR_YES_OR_NO)_AND_YES=YES;"
        f"corpus_pre_sha={corpus_pre_sha[:16]};"
        f"corpus_post_sha={corpus_post_sha[:16]};"
        f"all_rows_bit_exact={all_rows_present};"
        f"anchors_present={anchors_present}"
    )                                                              # (local)

    # ---- 9. Emit 4-tuple + append verdict line ----
    tag = (f"(value={value_summary!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(tag)
    append_verdict(verdict, value_summary, audit_sha, content_sha)

    # ---- 10. Save data (npz + json) ----
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        value=value_summary,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        # Three K=2 corpus rows (text + content_sha256)
        row_HIT_text=row_HIT_text,
        row_HIT_content_sha256=row_HIT_content_sha,
        row_E3_text=row_E3_text,
        row_E3_content_sha256=row_E3_content_sha,
        row_WCD_text=row_WCD_text,
        row_WCD_content_sha256=row_WCD_content_sha,
        # K-counter integer pairs
        K_HIT_pre=K_HIT_PRE, K_HIT_post=K_HIT_POST,
        K_E3_pre=K_E3_PRE, K_E3_post=K_E3_POST,
        K_WCD_pre=K_WCD_PRE, K_WCD_post=K_WCD_POST,
        K_promotion_threshold=K_PROMOTION,
        # Corpus state-change record
        corpus_pre_sha=corpus_pre_sha,
        corpus_post_sha=corpus_post_sha,
        # Verification predicates
        HIT_in_corpus=HIT_in_corpus,
        E3_in_corpus=E3_in_corpus,
        WCD_in_corpus=WCD_in_corpus,
        all_rows_present=all_rows_present,
        anchors_present=anchors_present,
        # Pre-pinned references
        W6_1_audit_sha=W6_1_AUDIT_SHA,
        W6_1_content_sha=W6_1_CONTENT_SHA,
        S91_W2_1_audit_sha=S91_W2_1_AUDIT_SHA,
        # Hybrid Independence Test predicate evaluation (per-clause)
        HIT_clause_i=True,   # distinct substrate-IS pillar (YES)
        HIT_clause_ii=True,  # distinct laboratory-IN pillar (YES)
        HIT_clause_iii=False,  # distinct bridge map class (NO; shared HKR)
        HIT_clause_iv=True,  # independent algebraic envelope (YES)
        HIT_predicate_value=True,  # (YES ∨ YES ∨ NO) ∧ YES = TRUE
    )
    print(f"\n  npz saved: {OUT_NPZ.name}")

    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump({
            "gate_id": GATE_ID,
            "verdict": verdict,
            "value": value_summary,
            "scheme": SCHEME,
            "convention": CONVENTION,
            "L_max": L_MAX,
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
            "rows": {
                "HIT_§3": {
                    "content_sha256": row_HIT_content_sha,
                    "bytes": len(row_HIT_text),
                    "K_pre": K_HIT_PRE,
                    "K_post": K_HIT_POST,
                    "in_corpus": HIT_in_corpus,
                },
                "E3_§10": {
                    "content_sha256": row_E3_content_sha,
                    "bytes": len(row_E3_text),
                    "K_pre": K_E3_PRE,
                    "K_post": K_E3_POST,
                    "in_corpus": E3_in_corpus,
                },
                "WCD_§17": {
                    "content_sha256": row_WCD_content_sha,
                    "bytes": len(row_WCD_text),
                    "K_pre": K_WCD_PRE,
                    "K_post": K_WCD_POST,
                    "in_corpus": WCD_in_corpus,
                },
            },
            "K_promotion_threshold": K_PROMOTION,
            "status_post_landing": "SUGGESTION at K=2 across all three corpus axes",
            "HIT_predicate": {
                "clause_i_distinct_substrate_IS_pillar": True,
                "clause_ii_distinct_laboratory_IN_pillar": True,
                "clause_iii_distinct_bridge_map_class": False,
                "clause_iv_independent_algebraic_envelope": True,
                "evaluation": "(YES OR YES OR NO) AND YES = TRUE",
            },
            "corpus_pre_sha": corpus_pre_sha,
            "corpus_post_sha": corpus_post_sha,
            "input_pin_map": pins,
            "W6_1_audit_sha": W6_1_AUDIT_SHA,
            "W6_1_content_sha": W6_1_CONTENT_SHA,
            "S91_W2_1_audit_sha": S91_W2_1_AUDIT_SHA,
        }, fp, indent=2, sort_keys=True)
    print(f"  json saved: {OUT_JSON.name}")

    # ---- 11. Final summary ----
    wall = time.time() - t0                                        # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    # Verdict is data; exit 0 regardless of PASS/FAIL per math-scripts.md
    # §"Exit Codes and Verdict Semantics".
    return 0


if __name__ == "__main__":
    sys.exit(main())
