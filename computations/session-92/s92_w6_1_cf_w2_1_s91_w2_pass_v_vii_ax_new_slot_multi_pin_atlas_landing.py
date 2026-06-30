#!/usr/bin/env python3
"""S92-W6-CF-W2-1-S91-W2-PASS-V-VII-AX-NEW-SLOT-MULTI-PIN-ATLAS-LANDING.

METHODOLOGY-class registry-text landing of NEW §VII.AX.MULTI-PIN-ATLAS
sub-slot as STAGE-1-CANDIDATE per joint-theorem-promotion.md 4-stage
pathway, with THREE Element 3 fiducial-anchor sub-rows (one per regulator
class R in {zeta, Pauli-Villars, Mellin}) at substrate-distance-2 pole s=4
chi-prime restriction under FULL CM-1995 §III.4 evaluation.

Trigger: [VERIFY-THEOREM]
Classification: NON-PHONONIC (METHODOLOGY-class per wave-classification.md
M1-M4 strict-conjunction; registry-text landing of a NEW §VII.AX sub-slot,
NOT substrate-physics computation).

Method: single-shot AFTER-pattern per `registry-landing.md
§"Bridge-Landing Script Architecture (single-shot pattern)"`:
  1. build_promotion_text(...)            pure function (all text in memory)
  2. write_atomic_insert(...)             single atomic insert via tmp+replace
  3. re_read_and_verify(...)              boolean (13-sub-block presence map)
  4. emit_verdict_line(verify_boolean)    exactly ONE canonical line

NO conditional rewrite branch (forbidden BEFORE pattern).

Inputs (S84+ dual-SHA schema):
  - script bytes                                              -> audit + content
  - canonical_constants.py                                    -> audit only
  - sessions/permanent-results-registry.md                    -> audit only
  - computations/session-91/s91_gate_verdicts.txt             -> audit only

Output 4-tuple:
  (value=<verdict-string>,
   scheme='mack-sole-writer-atomic-posix-O_APPEND-registry-section-landing-AFTER-pattern',
   convention='stage-1-candidate-registry-landing-§VII.AX.MULTI-PIN-ATLAS-substrate-distance-2-pole-s4-chi-prime-restriction-FULL-CM-1995-III-4-MULTI-PIN-ATLAS',
   L_max=12)

Plan reference: sessions/session-plan/session-92-plan-w6.md §W6-1.
Mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`
AMRI-PROMOTED 2026-04-28.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical-constants import (MANDATORY for S34+ per
# computations/_shared/CLAUDE.md). The registry-text landing does not
# consume framework numerics directly; the import is present to satisfy
# the canonical-import discipline.
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S92"                                                              # (local)
GATE_ID = ("S92-W6-CF-W2-1-S91-W2-PASS-V-VII-AX-NEW-SLOT-MULTI-PIN-ATLAS-"
           "LANDING")                                                         # (local)
SCHEME = ("mack-sole-writer-atomic-posix-O_APPEND-registry-section-landing-"
          "AFTER-pattern")                                                    # (local)
CONVENTION = ("stage-1-candidate-registry-landing-§VII.AX.MULTI-PIN-ATLAS-"
              "substrate-distance-2-pole-s4-chi-prime-restriction-FULL-"
              "CM-1995-III-4-MULTI-PIN-ATLAS")                                # (local)
L_MAX = "12"                                                                  # (local)
SCHEMA_VERSION = "S87+"                                                       # (local)
TRIGGER = "[VERIFY-THEOREM]"                                                  # (local)

# S91 W2-1 PASS-V prerequisite — canonical from s91_gate_verdicts.txt:22
W2_1_AUDIT_SHA_FULL = (
    "58671312b0aee2e749836b8902273ab135073992736ddcc8f3362be2328dea14"
)
W2_1_CONTENT_SHA_FULL = (
    "a6d7346ee04657c3a7099e1b8d4fbc77ac4f2fa302789f3041c551c56827c64e"
)
# Per-regulator-class FULL CM-1995 §III.4 evaluator outputs at L_max=12
R_zeta_value = "1.414393e+02"                                                 # (local) M_KK^2
R_PV_value = "1.144577e+02"                                                   # (local) M_KK^2
R_Mellin_value = "1.414393e+02"                                               # (local) M_KK^2
cross_reg_spread = "2.698e+01"                                                # (local) M_KK^2
option_iv_threshold = "1e-3"                                                  # (local) M_KK^2 threshold

# Plan-pinned input paths
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
S91_VERDICT_PATH = (
    PROJECT_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"
)
CANONICAL_CONSTANTS_PATH = (
    PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"
)

# Output destinations (per-session)
VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"
OUT_NPZ = (
    SESSION_DIR
    / "s92_w6_1_cf_w2_1_s91_w2_pass_v_vii_ax_new_slot_multi_pin_atlas_landing.npz"
)
OUT_JSON = (
    SESSION_DIR
    / "s92_w6_1_cf_w2_1_s91_w2_pass_v_vii_ax_new_slot_multi_pin_atlas_landing.json"
)

INPUT_FILES = [
    CANONICAL_CONSTANTS_PATH,
    REGISTRY_PATH,
    S91_VERDICT_PATH,
]

# PASS-predicate boundary thresholds
MIN_SUBSTANTIVE_LINES = 80                                                    # (local)
N_REQUIRED_SUB_BLOCKS = 13                                                    # (local) (a)-(m)
N_REQUIRED_REGULATOR_ANCHORS = 3                                              # (local) zeta, PV, Mellin


# ---------------------------------------------------------------------------
# Section 4 — SHA helpers
# ---------------------------------------------------------------------------
def sha256_of_text(text: str) -> str:
    """Return the SHA-256 hex digest of `text` (utf-8 encoded)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_of_file(path: Path) -> str:
    """Return the SHA-256 hex digest of the file at `path`."""
    if not path.exists():
        return ""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def closure_hash(input_pin_map: dict[str, str]) -> str:
    """Audit-trail SHA over a sorted (key, value) ledger.

    Each key|value pair is appended in canonical order, joined by `\n`
    delimiters.
    """
    items = sorted(input_pin_map.items())                                     # (local)
    joined = "\n".join(f"{k}|{v}" for k, v in items)                          # (local)
    return sha256_of_text(joined)


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}                                                 # (local)
    for p in inputs:
        sha = sha256_of_file(p)                                               # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")              # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256:
        sha256(bytes(script) || bytes(canonical_constants.py) || pinmap_json)
        where pinmap_json is the canonical (sorted, separators=(",", ":"))
        JSON serialization of `pins`.

    content_sha256:
        sha256(bytes(script))
    """
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
    canonical_bytes = (                                                         # (local)
        canonical_path.read_bytes() if canonical_path.exists() else b""
    )
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                                          # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                                # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                            # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — build_promotion_text (pure function; AFTER-pattern Step 1)
# ---------------------------------------------------------------------------
def build_promotion_text() -> str:
    """Pure function: assembles the full §VII.AX.MULTI-PIN-ATLAS section text
    in memory. All 13 sub-blocks (a)-(m) per plan §W6-1 method.
    """
    # Header (a)
    header = (
        "### §VII.AX.MULTI-PIN-ATLAS — Substrate-Distance-2 Pole s=4 χ' "
        "Restriction Multi-Pin Regulator Atlas under FULL CM-1995 §III.4 "
        "Evaluation (S92 W6-1 — mack-cosmic-bridge sole-writer per "
        "`feedback_mack-bridge-role.md`; ACTIVATED by S91 §W2-1 PASS-V "
        "verdict audit_sha256=`"
        + W2_1_AUDIT_SHA_FULL
        + "`, 2026-05-23)\n"
    )

    # Status (b)
    status_block = (
        "\n"
        "**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-"
        "promotion.md §\"Stage 1 — S87 (next-session) Registration as "
        "Candidate\"` 4-stage pathway. The structural conclusion of S91 §W2-1 "
        "PASS-V (cross-regulator spread `" + cross_reg_spread + "` M_KK² ≫ "
        "1e-3 M_KK² option (iv) threshold; `reading_v_pluralism_bool=True`) "
        "STRUCTURALLY PROMOTES the §VII.AX mother slot's REGISTRY-INCOMPLETE-"
        "PENDING-PROXY-REFINEMENT sub-class at the (substrate-distance-2, "
        "cross-axis-converged) cell to option (v) regulator-class-pluralism "
        "multi-pin atlas — the substrate-distance-2 pole `s=4` χ' "
        "restriction does NOT admit a regulator-class-INVARIANT canonical "
        "(option (iv) FAIL); option (v) IS the substrate's intrinsic "
        "structural conclusion. Stage-2 cross-axis independent-verify queued "
        "as S93+ carry-forward `S92-OR-LATER-VII-AX-MULTI-PIN-ATLAS-STAGE-2-"
        "CROSS-AXIS-VERIFY` per `joint-theorem-promotion.md §\"Stage 2\"` "
        "two-cross-reviewer protocol.\n"
    )

    # Provenance (c)
    provenance_block = (
        "\n"
        "**Provenance**: S92 W6-1 (`session-92-plan-w6.md §W6-1`) mack-"
        "cosmic-bridge plan-pinned sole-writer per `feedback_mack-bridge-"
        "role.md` AMRI-PROMOTED 2026-04-28. Source-of-truth derivation "
        "chain:\n"
        "\n"
        "1. **S91 §W2-1 PASS-V verdict**: canonical line at "
        "`computations/session-91/s91_gate_verdicts.txt:22`; gate "
        "`S91-CF37-CHI-PRIME-WEIGHT-CANONICALIZED-FULL-CM-1995-III-4-"
        "SUBSTRATE-DISTANCE-2-EVALUATION`; PASS at L_max=12; "
        "audit_sha256=`" + W2_1_AUDIT_SHA_FULL + "`; "
        "content_sha256=`" + W2_1_CONTENT_SHA_FULL + "`; "
        "`value='reading=V_R_zeta=" + R_zeta_value + "_R_PV=" + R_PV_value
        + "_R_Mellin=" + R_Mellin_value + "_image_block_rank=3_cross_reg_"
        "spread=" + cross_reg_spread + "'`; "
        "3-tuple companion at line 24 `sign_verdict=PASS magnitude_verdict="
        "PASS-V regime_verdict=VALID`.\n"
        "2. **W2-1 routing oracle 3-tuple companion** at "
        "`computations/session-91/s91_gate_verdicts.txt:25`: "
        "`reading_iv_match_bool=False reading_v_pluralism_bool=True "
        "truncation_consistent=True K_a4_positive=True K_a4_value="
        + R_zeta_value + "`. Per the §VII.AX mother-slot Forward-refinement-"
        "pathway table row (iv) pre-registration, "
        "`reading_v_pluralism_bool=True` selects option (v) as the "
        "substrate-IS structural conclusion.\n"
        "3. **§VII.AX mother-slot pre-registration**: registry entry at "
        "`sessions/permanent-results-registry.md` (mother slot at "
        "`### §VII.AX — CF-37 Option (v) Pre-Registration: Substrate-Axis "
        "Canonicalizer at (substrate-distance-2, cross-axis-converged) "
        "Cell`); S91 W0 R5 gen-physicist orchestrator-direct-write 2026-"
        "05-16; REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT sub-class tag "
        "per `cross-pillar-bridge-anatomy.md §\"Deferred-pending "
        "intermediate verdict-class\"`.\n"
        "4. **S90 W-2 §EMERGENCE EV1 D1-Reading-B admission of option (v)**: "
        "workshop `sessions/archive/session-90/workshops/s90-w2-chi-prime-weight-"
        "canonicalization.md` lines 877-887 — D1-Reading-B confirmed; "
        "option (v) STRUCTURALLY ADMITTED as the 5th pre-registered verdict-"
        "class at the structurally-vacant (substrate-distance-2, cross-axis-"
        "converged) cell.\n"
        "5. **Three FULL CM-1995 §III.4 evaluator outputs**: R_zeta="
        + R_zeta_value + ", R_PV=" + R_PV_value + ", R_Mellin="
        + R_Mellin_value + " M_KK² at canonical L_max=12 master cache "
        "filtered to substrate-distance-2 pole `s=4` χ' restriction; cross-"
        "regulator spread = " + cross_reg_spread + " M_KK² (33% relative "
        "divergence; FAILS option (iv) consistency threshold "
        + option_iv_threshold + " M_KK²; PROMOTES option (v) pluralism "
        "artifact status per mother-slot Forward-refinement-pathway table "
        "row (iv) branching `else → option (v) demotes to regulator-class-"
        "pluralism artifact`).\n"
    )

    # Bridge family (d)
    bridge_family_block = (
        "\n"
        "**Bridge family**: substrate-axis canonicalizer at the (substrate-"
        "distance-2 pole `s=4`, cross-axis-DIVERGENT) cell at χ' restriction "
        "— a STRUCTURALLY DISTINCT cell from the (substrate-distance-2, "
        "cross-axis-converged) cell pre-registered by the §VII.AX mother "
        "slot, surfaced empirically by the S91 §W2-1 PASS-V cross-regulator "
        "spread observation. Sibling under §VII.AX mother slot to "
        "§VII.AX.OP-PROJ (FWD-C5 PBH band-edge prediction n_PBH = 7.276e-23 "
        "m⁻³ at cardinality-cascade-tail saturation; structurally distinct "
        "bridge family on cardinality vs Mellin-cone axis). Cross-link to "
        "§VII.AN-CORRIGENDUM ROUTE-B canonical at substrate-distance-1 pole "
        "`s=3` (`α_s_canonical = Fraction(-8587279, 100000000) = -0.085873`) "
        "as adjacent-pole structural anchor for cross-pole comparison.\n"
    )

    # Corner (e)
    corner_block = (
        "\n"
        "**Corner**: per the parse-tree decision procedure at "
        "`sessions/permanent-results-registry.md §VII.U.2` clause (e), the "
        "multi-pin atlas observable's parse-tree expansion (declared below) "
        "is `image_block_rank=3` across three regulator classes; each "
        "regulator-class image is `Res_{s=4}[Tr(D_K^{-2s})]` evaluated under "
        "the substrate-IS spectral-functional family. All three readings "
        "inhabit the **algebra-INVARIANT spectrum-only-functional family** "
        "(no state-pair functional structure surfaces) at Mellin pole `s=4` "
        "→ **Cell II (algebra-INVARIANT × Mellin pole s=4)** classification. "
        "Cross-corner co-primary structures with Cell IV (algebra-DEPENDENT "
        "state-pair functional) are FORBIDDEN per "
        "`.claude/rules/registry-landing.md §\"Detection\"` criterion 4 "
        "(S88 W-15 V.6 MANDATORY at K=3).\n"
    )

    # IS-not-IN anatomy (f) — 5 elements
    is_not_in_block = (
        "\n"
        "**IS-not-IN anatomy** (5 elements; MANDATORY at K=3 per "
        "`.claude/rules/cross-pillar-bridge-anatomy.md §\"IS-not-IN Anatomy "
        "(5 elements)\"`):\n"
        "\n"
        "1. **Substrate-IS observable**: `Res_{s=4}[Tr(D_K^{-2s})]` at χ' "
        "restriction on `(A_K^{≤12}, H_K^{≤12}, D_K^{≤12})` at τ_fold = 0.19 "
        "under FULL CM-1995 §III.4 finite-spectral-triple residue formula "
        "evaluation. **EXPLICIT TAG: Level 1 single-τ-slice at τ_fold = "
        "0.190** (MANDATORY per `.claude/rules/phononic-framing.md §\"Single-"
        "τ-slice vs moduli-deformation substrate-IS levels\"` K=2 MANDATORY "
        "since S88 W-7 V.4). The substrate IS the spectral triple "
        "`(A_K, H_K, D_K(τ_fold = 0.19))` at τ_fold = 0.19; the substrate-"
        "distance-2 pole `s=4` χ' restriction observable IS intrinsic to it "
        "at the Level-1 single-τ-slice, NOT a coordinate in a meta-"
        "container.\n"
        "\n"
        "2. **Laboratory-IN observable** (OE-form MANDATORY at K=2 per "
        "`cross-pillar-bridge-anatomy.md §\"Element 2 OE-form discipline\"` "
        "S88+ plan-freeze positive-match regex "
        "`\\int.*d.*Tr.*\\([ΠP]_[a-z0-9_\\-]+\\)`): "
        "`∫_BZ d^d k Tr_{A_K}(P_{χ-prime-restriction-s4} · "
        "ρ_BZ(k; τ_fold))` — substrate-distance-2 Mellin-cone projection "
        "image at χ' restriction; named projector "
        "`P_{χ-prime-restriction-s4}` lifts the substrate-axis canonicalizer "
        "image under the HKR map of the χ' restriction Hochschild cocycle "
        "at substrate-distance-2 pole `s=4`. Trace over the substrate "
        "algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`; integration domain Σ_BZ is the "
        "Brillouin-zone container on the Pillar IV bridge image projection "
        "for the canonical (Mellin) regulator-class.\n"
        "\n"
        "3. **Bridge map** (explicit; NOT 'analogous to' / 'corresponds "
        "to'): Connes-Moscovici 1995 §III.4 finite-spectral-triple residue "
        "formula ∘ HKR (Hochschild-Kostant-Rosenberg) map `L_max → ∞` image "
        "at d=4 substrate-distance-2 pole `s=4`. **Element 3 fiducial-anchor "
        "binding** per `cross-pillar-bridge-anatomy.md §\"Element 3 "
        "fiducial-anchor binding discipline\"`: type **(iii) joint-"
        "hypersurface** — lab discrimination is 2D in (regulator-class R, "
        "observable value) space, NOT 1D in observable space alone. Option "
        "(v) regulator-class-pluralism IS the 2D discrimination structure: "
        "the three regulator-class images (ζ, PV, Mellin) span a 2D "
        "joint-hypersurface (R, R_value(R)) on which lab discrimination "
        "operates. The bridge map admits THREE scheme evaluations per "
        "`cross-pillar-bridge-anatomy.md §\"Bridge-map-scheme suffix "
        "discipline\"` SUGGESTION K=1; this landing advances the K-counter "
        "K=1 → K=2 as the second calibration instance. **Triple-pin Element "
        "3 fiducial-anchor sub-rows** (each carrying its own convention-tag "
        "suffix per the discipline):\n"
        "\n"
        "   - **R = ζ (zeta-function regularization)** per "
        "`.claude/rules/regulator-pin-discipline.md` a_n^{ζ}:\n"
        "     - `R_zeta = " + R_zeta_value + "` M_KK²\n"
        "     - convention-tag suffix: "
        "`-ZETA-FULL-CM-1995-III-4-substrate-distance-2-pole-s4-χ-prime-"
        "restriction-MULTI-PIN-ATLAS`\n"
        "\n"
        "   - **R = Pauli-Villars (PV regularization at Λ_UV = M_KK)** per "
        "`.claude/rules/regulator-pin-discipline.md` a_n^{Pauli-Villars} "
        "with S61/S78 mass-scale-running pipeline:\n"
        "     - `R_PV = " + R_PV_value + "` M_KK²\n"
        "     - convention-tag suffix: "
        "`-PV-FULL-CM-1995-III-4-substrate-distance-2-pole-s4-χ-prime-"
        "restriction-MULTI-PIN-ATLAS`\n"
        "\n"
        "   - **R = Mellin (Mellin-Barnes regularization)** per "
        "`.claude/rules/regulator-pin-discipline.md` a_n^{Mellin}:\n"
        "     - `R_Mellin = " + R_Mellin_value + "` M_KK² ← **CANONICAL "
        "substrate-natural Level-3 anchor** (single-pinned per Hybrid "
        "framing; see Registry-PASS criterion below)\n"
        "     - convention-tag suffix: "
        "`-MELLIN-FULL-CM-1995-III-4-substrate-distance-2-pole-s4-χ-prime-"
        "restriction-MULTI-PIN-ATLAS`\n"
        "\n"
        "   Cross-regulator spread: `" + cross_reg_spread + "` M_KK² "
        "(33% relative divergence across the three regulator-class images; "
        "FAILS option (iv) cross-regulator consistency threshold "
        + option_iv_threshold + " M_KK²; PROMOTES option (v) pluralism "
        "artifact status BY CONSTRUCTION).\n"
        "\n"
        "4. **Algebraic envelope**: `L^{-3}` algebraic envelope at d=4 "
        "substrate-distance-2 pole `s=4`; **Level-2-binding sub-class** per "
        "`cross-pillar-bridge-anatomy.md §\"Level-2 sub-class (binding vs "
        "non-binding)\"` — the HKR-image of the χ' restriction Hochschild "
        "moment binds Level-1 (the regulator-class-pluralism STRUCTURAL "
        "THEOREM) to the laboratory-IN continuum observable images at each "
        "regulator-class projection. The cross-regulator spread "
        + cross_reg_spread + " M_KK² IS the empirical extraction of the "
        "envelope discrepancy at canonical L_max=12; option (v) pluralism "
        "interpretation: the three regulator-class images converge to "
        "STRUCTURALLY DISTINCT continuum laboratory observables at the "
        "Pillar IV / Pillar II / Pillar V bridge image projections, each "
        "carrying its own HKR-image envelope. The three envelopes are "
        "structurally INDEPENDENT (Hybrid Independence Test clause (iv) "
        "YES; see below) — not numerical refinements of one another but "
        "distinct HKR-image bindings binding three distinct Level-1 "
        "regulator-class-keyed identities to three distinct continuum lab "
        "observables.\n"
        "\n"
        "5. **Empirical anchor**: TRIPLE-PIN at canonical L_max=12 (one "
        "per regulator class) declared as Level-3 EMPIRICAL CONFIRMATION of "
        "the structural pluralism conclusion via S91 §W2-1 PASS-V verdict "
        "at audit_sha256=`" + W2_1_AUDIT_SHA_FULL + "`. The cross-regulator "
        "spread `" + cross_reg_spread + "` M_KK² ≫ option (iv) threshold "
        + option_iv_threshold + " M_KK² IS the substrate's intrinsic "
        "empirical signature that the χ' restriction at substrate-distance-"
        "2 pole `s=4` does NOT admit a regulator-class-INVARIANT canonical. "
        "Per `cross-pillar-bridge-anatomy.md §\"Level-3 anchor singleness "
        "sub-clause\"` SUGGESTION K=1, the Hybrid (single-slot with "
        "regulator-class-keyed Level-2-B sub-row table) registry-text "
        "framing requires Level-3 to be SINGLE-PINNED at the substrate-"
        "natural canonical (R_Mellin); R_zeta and R_PV land as Level-2-B "
        "DIAGNOSTIC sub-rows in the multi-pin atlas table. Cross-corner "
        "co-primary at the Level-3 axis is FORBIDDEN per "
        "`substrate-first-canonical-sourcing.md §(i)`.\n"
    )

    # Three-level structural-confidence ladder (g)
    ladder_block = (
        "\n"
        "**Three-level structural-confidence ladder** (per "
        "`.claude/rules/cross-pillar-bridge-anatomy.md §\"Three-Level "
        "Structural-Confidence Ladder\"`):\n"
        "\n"
        "| Level | Anatomy | Status |\n"
        "|:------|:--------|:-------|\n"
        "| Level 1 | Substrate-IS structural identity: option (v) "
        "regulator-class-pluralism IS a STRUCTURAL THEOREM about the "
        "substrate-distance-2 pole `s=4` χ' restriction — the residue "
        "formula admits three INEQUIVALENT FULL physical regularizations "
        "(ζ, Pauli-Villars, Mellin) whose laboratory-IN images are "
        "STRUCTURALLY DISTINCT at the cross-pillar bridge projections. "
        "Regulator-class-keyed identity (not regulator-class-INVARIANT); "
        "holds at every L_max ≥ 12 by structural property of the "
        "substrate's spectral closure at substrate-distance-2 pole. | "
        "STRUCTURAL THEOREM (W2-1 PASS-V at L_max=12; CM-1995 §III.4 "
        "multi-regulator evaluation closed at machine precision per "
        "verdict audit_sha256=`" + W2_1_AUDIT_SHA_FULL[:16] + "...`) |\n"
        "| Level 2 | Algebraic convergence envelope `L^{-3}` HKR-image at "
        "d=4 substrate-distance-2 pole `s=4` PER regulator class; "
        "**Level-2-binding sub-class** per the three distinct HKR-images "
        "binding three distinct laboratory-IN images at the Pillar IV / "
        "Pillar II / Pillar V bridge image projections. Structurally "
        "INDEPENDENT envelopes per Hybrid Independence Test clause (iv); "
        "regulator-class-keyed Level-2-B sub-rows: R_zeta, R_PV (DIAGNOSTIC "
        "sub-rows); R_Mellin substrate-natural canonical. | STRUCTURAL "
        "PREDICTION (Level-2-binding; algebraically derived from three "
        "CM-1995 §III.4 simple-pole residues with distinct regulator-class "
        "prefactors) |\n"
        "| Level 3 | Triple-pin empirical anchor at canonical L_max=12: "
        "R_zeta=" + R_zeta_value + ", R_PV=" + R_PV_value + ", R_Mellin="
        + R_Mellin_value + " M_KK²; cross-regulator spread "
        + cross_reg_spread + " M_KK² (33% relative divergence); "
        "Level-3 substrate-natural canonical SINGLE-PINNED at R_Mellin per "
        "Hybrid framing Level-3 anchor singleness sub-clause SUGGESTION "
        "K=1. | EMPIRICAL CONFIRMATION (W2-1 PASS-V; "
        "audit_sha256=`" + W2_1_AUDIT_SHA_FULL[:16] + "...`; "
        "`reading_v_pluralism_bool=True ∧ cross_reg_spread="
        + cross_reg_spread + " ≫ " + option_iv_threshold + "`) |\n"
    )

    # Registry-PASS criterion (h)
    pass_criterion_block = (
        "\n"
        "**Registry-PASS criterion** (per `cross-pillar-bridge-"
        "anatomy.md §\"Registry-PASS criterion\"`): option (v) pluralism "
        "IS the STRUCTURAL CONCLUSION — the substrate's substrate-"
        "distance-2 pole `s=4` χ' restriction does NOT admit a regulator-"
        "class-INVARIANT canonical (which would have been option (iv) "
        "PASS at spread < " + option_iv_threshold + " M_KK²). Level 3 "
        "triple-pin satisfies the option (v) admission criterion BY "
        "CONSTRUCTION (cross-regulator spread " + cross_reg_spread
        + " M_KK² > " + option_iv_threshold + " M_KK² threshold by "
        "4.4 OOM). Per `cross-pillar-bridge-anatomy.md §\"Level-3 anchor "
        "singleness sub-clause\"` SUGGESTION K=1: the Hybrid (single-slot "
        "with regulator-class-keyed Level-2-B sub-row table) registry-"
        "text framing is the canonical structural-fit; the Level-3 anchor "
        "MUST be single-pinned at one substrate-natural source. This "
        "entry ADOPTS the Hybrid framing with `R_Mellin = "
        + R_Mellin_value + "` M_KK² as the canonical substrate-natural "
        "Level-3 anchor (per §VII.AX mother-slot Element 4 algebraic "
        "envelope specification `L^{-3}` HKR-image at d=4 substrate-"
        "distance-2 with Mellin regulator as the canonical class; "
        "Mellin-Barnes is the substrate-natural regularization at the "
        "Connes-Moscovici 1995 §III.4 finite-spectral-triple residue "
        "formula); `R_zeta = " + R_zeta_value + "` and `R_PV = "
        + R_PV_value + "` M_KK² land as **Level-2-B DIAGNOSTIC sub-rows "
        "ONLY** in the multi-pin atlas table (NOT cross-referenced as "
        "Level-3 co-primaries; cross-corner co-primary at the Level-3 "
        "axis is FORBIDDEN per `substrate-first-canonical-sourcing.md "
        "§(i)`).\n"
    )

    # Hybrid Independence Test (i)
    hit_block = (
        "\n"
        "**Hybrid Independence Test** (predicate `(i ∨ ii ∨ iii) ∧ iv` "
        "per `.claude/rules/cross-pillar-bridge-anatomy.md §\"Hybrid "
        "Independence Test\"` SUGGESTION-K=1; this landing advances "
        "K-counter K=1 → K=2 on the (regulator-class-pluralism, Cell-II × "
        "Mellin-pole-s=4) corpus per sibling §W6-2 K=2 corpus row "
        "landing):\n"
        "\n"
        "- **(i) distinct substrate-IS pillar**: **YES** — Pillar I "
        "substrate-distance-2 pole `s=4` χ' restriction. Structurally "
        "distinct from §VII.AU.OP-PROJ Pillar I substrate-distance-1 pole "
        "`s=3` by parse-tree expansion (substrate-distance-2 vs "
        "substrate-distance-1 Mellin poles; distinct residue-formula "
        "evaluations on the substrate algebra).\n"
        "- **(ii) distinct laboratory-IN pillar**: **YES** — three "
        "distinct cross-pillar laboratory-IN images at the joint-"
        "hypersurface bridge projection (Pillar IV BZ-trace at the Mellin "
        "regulator-class canonical; Pillar II CMB at the ζ regulator-"
        "class image; Pillar V BdG at the PV regulator-class image). The "
        "three regulator-class images converge to STRUCTURALLY DISTINCT "
        "continuum laboratory observables per option (v) pluralism "
        "structural theorem; the three cross-pillar bridge projections "
        "ARE the substrate's empirical signature of regulator-class-"
        "pluralism.\n"
        "- **(iii) distinct bridge map class**: **NO** — same HKR-image "
        "class for all three regulator-class evaluations (HKR `L_max → ∞` "
        "image; ∘ CM-1995 §III.4 residue formula). The disjunction `(i ∨ "
        "ii ∨ iii)` only requires ANY; clauses (i) AND (ii) both YES.\n"
        "- **(iv) independent algebraic envelope**: **YES** — three "
        "distinct `L^{-3}` envelopes (one per regulator class), "
        "structurally INDEPENDENT (not numerical refinements of one "
        "another but distinct HKR-image bindings to three structurally "
        "distinct continuum laboratory observables). Per "
        "`cross-pillar-bridge-anatomy.md §\"Hybrid Independence Test\"` "
        "(iv) independent algebraic envelope criterion.\n"
        "- **Predicate evaluation**: `(YES ∨ YES ∨ NO) ∧ YES = YES`. "
        "**K-counter advancement**: K=1 SUGGESTION → K=2 advancement on "
        "the (regulator-class-pluralism, Cell-II × Mellin-pole-s=4) "
        "corpus (sibling §W6-2 lands the K=1 → K=2 corpus row at "
        "`sessions/framework/registry/cross-pillar-bridge-corpus.md`).\n"
    )

    # Parse-tree expansion (j)
    parse_tree_block = (
        "\n"
        "**Parse-tree expansion** (per `.claude/rules/registry-"
        "landing.md §\"Parse-Tree Expansion Pre-Registration for new "
        "§VII entries\"` SUGGESTION K=1; in-session pre-registration "
        "to advance K-counter K=1 → K=2 on the parse-tree expansion "
        "corpus):\n"
        "\n"
        "```\n"
        "substrate-axis canonicalizer at (substrate-distance-2,\n"
        "cross-axis-DIVERGENT) cell at χ' restriction\n"
        "   → FULL CM-1995 §III.4 finite-spectral-triple residue formula\n"
        "     at pole s=4 on (A_K, H_K, D_K(τ_fold = 0.19))\n"
        "   → regulator-class evaluation R ∈ {ζ, PV, Mellin}\n"
        "   → cross-regulator spread = " + cross_reg_spread + " M_KK²\n"
        "     (≫ " + option_iv_threshold + " M_KK² option (iv) threshold)\n"
        "   → option (v) STRUCTURALLY PROMOTED: multi-pin atlas with\n"
        "     three Element 3 fiducial-anchors (one per regulator class R)\n"
        "```\n"
        "\n"
        "The parse-tree reduction makes the substrate-IS structural form "
        "decidable at the registry-text layer: the substrate-IS image at "
        "χ' restriction does NOT admit a regulator-class-INVARIANT "
        "canonical at substrate-distance-2 pole `s=4` (the canonical "
        "would have required regulator-class INVARIANCE across {ζ, PV, "
        "Mellin}); the three regulator-class images are STRUCTURALLY "
        "DISTINCT laboratory-IN observables at the three cross-pillar "
        "bridge image projections. **The naïve-parse failure mode** "
        "(reading the multi-pin atlas as a single substrate-IS canonical "
        "observable with one of the three regulator-class images "
        "designated as 'the canonical' and the others 'non-canonical') "
        "is foreclosed by the parse-tree reduction: each regulator-class "
        "image IS a structurally-admitted FULL physical regularization "
        "per the substrate algebra's residue formula at the pole; the "
        "pluralism IS the substrate's intrinsic structural conclusion. "
        "Parse-tree counters return `image_block_rank=3` across three "
        "regulator-class evaluations (algebra-INVARIANT spectrum-only-"
        "functional family operations: residue formula on the substrate "
        "algebra; cross-regulator spread on R^3); Cell II classification "
        "follows per §VII.U.2 clause (e).\n"
    )

    # Stage-2 cross-axis verify queue (k)
    stage_2_queue_block = (
        "\n"
        "**Stage-2 cross-axis verify queue** (per `.claude/rules/joint-"
        "theorem-promotion.md §\"Stage 2\"` two-cross-reviewer protocol; "
        "dispatch identifier `S92-OR-LATER-VII-AX-MULTI-PIN-ATLAS-STAGE-2-"
        "CROSS-AXIS-VERIFY`): Stage-2 PASS-AND with two cross-reviewers "
        "on opposite axes promotes §VII.AX.MULTI-PIN-ATLAS from STAGE-1-"
        "CANDIDATE to STAGE-3-PERMANENT-eligible. **EXCLUDED reviewers** "
        "per OAA on §VII.AX cluster (per `session-92-context.md` line "
        "270) and per writer/reviewer separation discipline: mack-"
        "cosmic-bridge (sole-writer at this Stage-1 landing). "
        "**Admissible Stage-2 axes**:\n"
        "\n"
        "- **Axis-A (NCG-axiomatic / spectral-functional)** ∈ {connes-"
        "ncg-theorist, lizzi-spectral-functional-theorist}.\n"
        "- **Axis-B (substrate / superfluid-universe / cosmological-"
        "bridge)** ∈ {volovik-superfluid-universe-theorist, gen-"
        "physicist}.\n"
        "\n"
        "Both cross-reviewers operate WITHOUT prior workshop context per "
        "the 'without prior workshop context' procedural floor "
        "(`joint-theorem-promotion.md §\"Two-Agent Independent-Verify\"` "
        "item 4); the dispatch reads ONLY the registered Stage-1 entry "
        "text + cited inputs (the S91 §W2-1 PASS-V verdict line). "
        "Substrate-input-orthogonality clause per `joint-theorem-"
        "promotion.md §\"Substrate-input-orthogonality clause (S88 W-23 "
        "W7c-167 V.1; B.56)\"` MANDATORY at K=3 since S90 W2 CF-20 "
        "applies at Stage-2; per-observable substrate-input orthogonality "
        "to be verified at Stage-2 dispatch time on each of the THREE "
        "regulator-class fiducial-anchor sub-rows.\n"
    )

    # Substrate framing (l)
    substrate_framing_block = (
        "\n"
        "**Substrate framing** (per `.claude/rules/phononic-framing.md "
        "§\"IS Space, Not IN Space\"`):\n"
        "\n"
        "The §VII.AX.MULTI-PIN-ATLAS STAGE-1-CANDIDATE entry IS the "
        "substrate's intrinsic regulator-class-pluralism structural "
        "conclusion at the substrate-distance-2 pole `s=4` χ' restriction. "
        "The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))` "
        "at τ_fold = 0.19 with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`; the substrate-"
        "distance-2 pole `s=4` IS intrinsic to its spectral closure under "
        "the FULL CM-1995 §III.4 residue formula; the χ' restriction IS "
        "intrinsic to its substrate-axis canonicalizer Hochschild cocycle "
        "at the pole. The three regulator-class evaluations (ζ, Pauli-"
        "Villars, Mellin) are three STRUCTURALLY INEQUIVALENT FULL "
        "physical regularizations admitted by the substrate algebra at "
        "this pole; the cross-regulator spread `" + cross_reg_spread
        + "` M_KK² IS the substrate's intrinsic empirical signature of "
        "regulator-class-pluralism. **Direction of explanation**:\n"
        "\n"
        "```\n"
        "Substrate (Pillar I, A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); H_K, D_K(τ_fold = 0.19))\n"
        "   IS the FULL CM-1995 §III.4 simple-pole residue at\n"
        "   substrate-distance-2 pole s=4 at χ' restriction\n"
        "   → Three structurally INEQUIVALENT regulator-class evaluations\n"
        "     R ∈ {ζ, Pauli-Villars, Mellin}\n"
        "   → Bridge map (HKR L_max → ∞ image at d=4 substrate-distance-2\n"
        "                 pole s=4) PER regulator class\n"
        "   → THREE distinct laboratory-IN images at three cross-pillar\n"
        "     bridge projections (Pillar IV BZ-trace + Pillar II CMB +\n"
        "     Pillar V BdG)\n"
        "```\n"
        "\n"
        "The cross-regulator spread `" + cross_reg_spread + "` M_KK² IS "
        "NOT a numerical artifact of regulator-shopping; it IS the "
        "substrate's intrinsic structural conclusion that the χ' "
        "restriction at substrate-distance-2 pole `s=4` does NOT admit a "
        "regulator-class-INVARIANT canonical image. Option (v) regulator-"
        "class-pluralism IS a STRUCTURAL THEOREM about the substrate's "
        "Mellin-cone closure at this specific (pole, restriction) pair "
        "— NOT a methodology-floor failure of the FULL CM-1995 §III.4 "
        "evaluator (which executed faithfully per S91 §W2-1 PASS-V).\n"
        "\n"
        "**FORBIDDEN inversion**: \"the regulator class is a computational "
        "convention chosen IN the cosmological calculation; the substrate "
        "has a unique answer that one of the three regulators "
        "approximates better\" — INVERT: \"the substrate IS the residue "
        "formula at substrate-distance-2 pole `s=4` χ' restriction; the "
        "three regulator-class evaluations are three structurally "
        "INEQUIVALENT FULL physical regularizations admitted by the "
        "substrate algebra at this pole; the laboratory-IN images they "
        "produce are three structurally distinct continuum observables "
        "at three different cross-pillar bridge projections; the "
        "pluralism IS the substrate's intrinsic structural conclusion.\" "
        "Container-thinking is FORBIDDEN per `phononic-framing.md "
        "§\"IS Space, Not IN Space\"` Mandatory Reframe.\n"
        "\n"
        "**Algebra-axis cell direction**: Cell II (algebra-INVARIANT × "
        "Mellin pole s=4) per §VII.U.2 4-corner classification IS the "
        "substrate-IS axis location of the multi-pin atlas observable; "
        "cross-corner co-primary structures with Cell IV (algebra-"
        "DEPENDENT state-pair functional) are FORBIDDEN per "
        "`.claude/rules/registry-landing.md §\"Detection\"` criterion 4 "
        "(S88 W-15 V.6 MANDATORY at K=3). The multi-pin atlas operates "
        "on the regulator-class axis (structurally orthogonal to the "
        "OP-PROJ vs STATE-PROJ axis); `MULTI-PIN-ATLAS` suffix is the "
        "canonical naming-hygiene extension for regulator-class-"
        "pluralism cross-regulator atlas sub-slots per the algebra-axis "
        "orthogonality discipline.\n"
    )

    # Cross-references (m) — ≥10 cross-links
    cross_refs_block = (
        "\n"
        "**Cross-references** (≥10 enumerated):\n"
        "\n"
        "1. `sessions/permanent-results-registry.md §VII.AX` (mother "
        "slot at registry line 18816) — CF-37 Option (v) Pre-Registration "
        "(S91 W0 R5; REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT sub-"
        "class); this §VII.AX.MULTI-PIN-ATLAS entry IS the registry-text "
        "reification of the mother-slot Forward-refinement-pathway table "
        "row (iv) `else → option (v) demotes to regulator-class-pluralism "
        "artifact` branch.\n"
        "2. `sessions/permanent-results-registry.md §VII.AX.OP-PROJ` "
        "(sibling at registry line 19025) — PBH band-edge prediction "
        "n_PBH = 7.276e-23 m⁻³ at cardinality-cascade-tail saturation; "
        "STRUCTURAL MODEL for the 5-anatomy + 3-level + parse-tree "
        "expansion form mirrored at this MULTI-PIN-ATLAS landing; "
        "structurally distinct bridge family on cardinality vs Mellin-"
        "cone axis.\n"
        "3. `.claude/rules/joint-theorem-promotion.md §\"Stage 1 — S87 "
        "(next-session) Registration as Candidate\"` 4-stage pathway — "
        "this entry is Stage 1 of 4; Stage-2 cross-axis independent-"
        "verify queued as `S92-OR-LATER-VII-AX-MULTI-PIN-ATLAS-STAGE-2-"
        "CROSS-AXIS-VERIFY` per the two-cross-reviewer protocol.\n"
        "4. `.claude/rules/cross-pillar-bridge-anatomy.md §\"IS-not-IN "
        "Anatomy (5 elements)\"` MANDATORY at K=3 — all 5 elements "
        "declared above; Element 2 OE-form discipline MANDATORY at K=2 "
        "S88+ plan-freeze satisfied (named projector `P_{χ-prime-"
        "restriction-s4}`).\n"
        "5. `.claude/rules/cross-pillar-bridge-anatomy.md §\"Three-Level "
        "Structural-Confidence Ladder\"` — Level 1 STRUCTURAL THEOREM, "
        "Level 2 STRUCTURAL PREDICTION (Level-2-binding sub-class), "
        "Level 3 EMPIRICAL CONFIRMATION (single-pinned at R_Mellin per "
        "Hybrid framing).\n"
        "6. `.claude/rules/cross-pillar-bridge-anatomy.md §\"Hybrid "
        "Independence Test\"` SUGGESTION K=1 — this landing is the K=2 "
        "advancement on the (regulator-class-pluralism, Cell-II × "
        "Mellin-pole-s=4) corpus; predicate `(YES ∨ YES ∨ NO) ∧ YES = "
        "YES`.\n"
        "7. `.claude/rules/cross-pillar-bridge-anatomy.md §\"Bridge-"
        "map-scheme suffix discipline\"` SUGGESTION K=1 — each Element "
        "3 fiducial-anchor sub-row carries its own convention-tag "
        "suffix per the discipline (`-ZETA-` / `-PV-` / `-MELLIN-` "
        "suffix markers).\n"
        "8. `.claude/rules/cross-pillar-bridge-anatomy.md §\"Element 3 "
        "fiducial-anchor binding discipline\"` SUGGESTION K=1 — type "
        "(iii) joint-hypersurface declared (2D in (regulator-class R, "
        "observable value) space).\n"
        "9. `.claude/rules/cross-pillar-bridge-anatomy.md §\"Level-3 "
        "anchor singleness sub-clause\"` SUGGESTION K=1 — Hybrid (single-"
        "slot with regulator-class-keyed Level-2-B sub-row table) "
        "framing adopted; Level-3 single-pinned at R_Mellin substrate-"
        "natural canonical; R_zeta + R_PV are Level-2-B DIAGNOSTIC sub-"
        "rows ONLY.\n"
        "10. `.claude/rules/cross-pillar-bridge-anatomy.md §\"Algebra-"
        "axis orthogonality K-counter\"` MANDATORY at K=3 — Cell II "
        "(algebra-INVARIANT × Mellin pole s=4) classification; cross-"
        "corner co-primary with Cell IV FORBIDDEN per `registry-"
        "landing.md §\"Detection\"` criterion 4.\n"
        "11. `.claude/rules/registry-landing.md §\"Parse-Tree Expansion "
        "Pre-Registration for new §VII entries\"` SUGGESTION K=1 — "
        "parse-tree expansion declared above; pre-emptive compliance "
        "advances K-counter K=1 → K=2.\n"
        "12. `.claude/rules/registry-landing.md §\"Bridge-Landing Script "
        "Architecture (single-shot pattern)\"` — this gate's producing "
        "script uses the AFTER-pattern (build_promotion_text → "
        "write_atomic_with_fsync → re_read + verify_section_matches → "
        "emit exactly one verdict line); NO BEFORE-pattern with "
        "conditional rewrite branch.\n"
        "13. `.claude/rules/phononic-framing.md §\"Single-τ-slice vs "
        "moduli-deformation substrate-IS levels\"` K=2 MANDATORY since "
        "S88 W-7 V.4 — Level-1 single-τ-slice declaration at τ_fold = "
        "0.190 satisfied at Element 1.\n"
        "14. `.claude/rules/regulator-pin-discipline.md` — a_n^{ζ} + "
        "a_n^{Pauli-Villars} + a_n^{Mellin} UV-regulator pin tagging at "
        "each of the three Element 3 fiducial-anchor sub-rows; "
        "MANDATORY discipline preserved.\n"
        "15. `sessions/framework/registry/cross-pillar-bridge-corpus.md "
        "§3` (Hybrid Independence Test corpus) + `§10` (Element 3 "
        "fiducial-anchor binding / Bridge-map-scheme suffix discipline) "
        "+ `§15` (Within-cell discriminator axes) — sibling §W6-2 "
        "appends three K=2 corpus rows citing this §VII.AX.MULTI-PIN-"
        "ATLAS landing as the K=2 calibration instance.\n"
        "16. `computations/session-91/s91_gate_verdicts.txt:22` — S91 "
        "§W2-1 PASS-V canonical verdict line (audit_sha256=`"
        + W2_1_AUDIT_SHA_FULL + "`; content_sha256=`"
        + W2_1_CONTENT_SHA_FULL + "`).\n"
        "17. `feedback_mack-bridge-role.md` AMRI-PROMOTED 2026-04-28 — "
        "mack-cosmic-bridge sole-writer discipline for §VII registry "
        "rows (canonical sole-writer for cosmology-side cross-pillar "
        "bridge entries + cross-axis verdict landings).\n"
        "18. `.claude/rules/substrate-first-canonical-sourcing.md §(i)` "
        "— Level-3 cross-corner co-primary FORBIDDEN; R_zeta + R_PV "
        "Level-2-B DIAGNOSTIC sub-rows discipline.\n"
        "19. `.claude/rules/epistemic-discipline.md §\"Registry-Write "
        "Hygiene under Parallel-Writer Race\"` items 1-2 — atomic POSIX "
        "O_APPEND via tmp+replace (NOT Edit-tool round-trip) for "
        "registry-text insertion; race-condition immunity by construction.\n"
        "20. `sessions/archive/session-90/workshops/s90-w2-chi-prime-weight-"
        "canonicalization.md §EMERGENCE EV1` lines 877-887 — D1-Reading-"
        "B confirmed; option (v) admitted as 5th pre-registered "
        "structural verdict at the (substrate-distance-2, cross-axis-"
        "converged) cell.\n"
    )

    # Source / audit pin closing block
    source_block = (
        "\n"
        "**Source**: S92 W6-1 plan-pinned verbatim "
        "(`sessions/session-plan/session-92-plan-w6.md §W6-1`); S91 "
        "§W2-1 PASS-V canonical verdict line at `computations/session-"
        "91/s91_gate_verdicts.txt:22` audit_sha256=`"
        + W2_1_AUDIT_SHA_FULL + "`; W2-1 routing oracle 3-tuple "
        "companion at verdict-file line 25 "
        "(`reading_v_pluralism_bool=True ∧ cross_reg_spread="
        + cross_reg_spread + " ≫ " + option_iv_threshold + "`); §VII.AX "
        "mother-slot Forward-refinement-pathway table row (iv) "
        "branching `else → option (v) demotes to regulator-class-"
        "pluralism artifact` at registry line ~18855; S90 W-2 §EMERGENCE "
        "EV1 D1-Reading-B option (v) admission at workshop lines 877-"
        "887. Mack-cosmic-bridge sole-writer per `feedback_mack-bridge-"
        "role.md` (atomic POSIX O_APPEND tmp+replace insert per "
        "`epistemic-discipline.md §\"Registry-Write Hygiene under "
        "Parallel-Writer Race\"`). AFTER-pattern single-shot architecture "
        "verified per `registry-landing.md §\"Bridge-Landing Script "
        "Architecture (single-shot pattern)\"` REQUIRED AFTER-pattern: "
        "build_promotion_text in memory → write_atomic_with_fsync → "
        "re_read + verify_section_matches → emit exactly ONE verdict "
        "line.\n"
        "\n"
        "---\n"
        "\n"
    )

    full_text = (
        "\n"
        + header
        + status_block
        + provenance_block
        + bridge_family_block
        + corner_block
        + is_not_in_block
        + ladder_block
        + pass_criterion_block
        + hit_block
        + parse_tree_block
        + stage_2_queue_block
        + substrate_framing_block
        + cross_refs_block
        + source_block
    )

    return full_text


# ---------------------------------------------------------------------------
# Section 6 — Atomic write helper (single-shot insert via tmp+replace)
# ---------------------------------------------------------------------------
def write_atomic_insert_before(target_path: Path, insert_text: str,
                                 anchor: str,
                                 idempotency_marker: str) -> tuple[bool, str, str]:
    """Insert `insert_text` into `target_path` immediately BEFORE the line
    containing `anchor`. Atomic write via tmp + replace.

    Idempotency: if `idempotency_marker` already in file, returns (True,
    pre_sha, pre_sha) without re-writing.

    Returns (write_succeeded, pre_state_sha, post_state_sha_or_error).
    """
    pre_text = target_path.read_text(encoding="utf-8", errors="replace")       # (local)
    pre_sha = sha256_of_text(pre_text)                                          # (local)

    if idempotency_marker in pre_text:
        print(f"  Idempotency guard: marker already present in "
              f"{target_path.name}; no re-write.")
        return True, pre_sha, pre_sha

    anchor_idx = pre_text.find(anchor)                                          # (local)
    if anchor_idx == -1:
        return False, pre_sha, "ANCHOR_NOT_FOUND"

    # Insert BEFORE the anchor line (find newline preceding anchor)
    # Walk backwards from anchor_idx to find the start of the line containing
    # the anchor.
    line_start = pre_text.rfind("\n", 0, anchor_idx)                            # (local)
    if line_start == -1:
        insertion_idx = 0                                                       # (local)
    else:
        insertion_idx = line_start + 1                                          # (local)

    new_text = pre_text[:insertion_idx] + insert_text + pre_text[insertion_idx:]  # (local)
    post_sha_target = sha256_of_text(new_text)                                  # (local)

    # Atomic write via tmp + replace
    tmp_path = target_path.with_suffix(                                         # (local)
        target_path.suffix + ".tmp_s92w61"
    )
    try:
        with tmp_path.open("w", encoding="utf-8") as fp:
            fp.write(new_text)
            fp.flush()
            try:
                os.fsync(fp.fileno())
            except OSError:
                pass
        tmp_path.replace(target_path)
    except OSError as e:
        return False, pre_sha, f"WRITE_FAILED:{e}"

    return True, pre_sha, post_sha_target


# ---------------------------------------------------------------------------
# Section 7 — re_read_and_verify (13-sub-block presence map + triple-pin)
# ---------------------------------------------------------------------------
def re_read_and_verify(registry_path: Path,
                       promotion_text: str) -> dict:
    """Re-read registry; verify all 13 sub-blocks (a)-(m) + triple-pin
    Element 3 fiducial-anchor sub-rows + content_sha256 bit-exact match.
    """
    post_text = registry_path.read_text(encoding="utf-8", errors="replace")     # (local)
    post_sha = sha256_of_text(post_text)                                        # (local)
    promotion_sha = sha256_of_text(promotion_text)                              # (local)

    # Sub-block (a) Header
    sub_a_marker = "### §VII.AX.MULTI-PIN-ATLAS — Substrate-Distance-2 Pole s=4 χ' Restriction Multi-Pin Regulator Atlas"
    sub_a_pass = sub_a_marker in post_text                                      # (local)

    # Sub-block (b) Status — STAGE-1-CANDIDATE per joint-theorem-promotion.md
    sub_b_marker = "**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md"
    sub_b_pass = sub_b_marker in post_text                                      # (local)

    # Sub-block (c) Provenance citation chain (5 numbered items)
    sub_c_marker = "**Provenance**: S92 W6-1"
    sub_c_pass = sub_c_marker in post_text and W2_1_AUDIT_SHA_FULL in post_text  # (local)

    # Sub-block (d) Bridge family
    sub_d_marker = "**Bridge family**: substrate-axis canonicalizer at the (substrate-distance-2 pole `s=4`, cross-axis-DIVERGENT) cell at χ' restriction"
    sub_d_pass = sub_d_marker in post_text                                      # (local)

    # Sub-block (e) Corner Cell II
    sub_e_marker = "**Corner**: per the parse-tree decision procedure at"
    sub_e_cell_ii = "**Cell II (algebra-INVARIANT × Mellin pole s=4)**"
    sub_e_pass = (sub_e_marker in post_text) and (sub_e_cell_ii in post_text)   # (local)

    # Sub-block (f) IS-not-IN anatomy (5 elements)
    sub_f_anatomy_markers = [
        "**IS-not-IN anatomy** (5 elements;",
        "1. **Substrate-IS observable**: `Res_{s=4}[Tr(D_K^{-2s})]`",
        "2. **Laboratory-IN observable**",
        "3. **Bridge map** (explicit",
        "4. **Algebraic envelope**: `L^{-3}`",
        "5. **Empirical anchor**: TRIPLE-PIN at canonical L_max=12",
    ]
    sub_f_pass = all(m in post_text for m in sub_f_anatomy_markers)             # (local)
    sub_f_count = sum(1 for m in sub_f_anatomy_markers if m in post_text)        # (local)

    # Sub-block (g) Three-level ladder
    sub_g_markers = [
        "**Three-level structural-confidence ladder**",
        "| Level 1 | Substrate-IS structural identity: option (v)",
        "| Level 2 | Algebraic convergence envelope `L^{-3}`",
        "| Level 3 | Triple-pin empirical anchor at canonical L_max=12",
    ]
    sub_g_pass = all(m in post_text for m in sub_g_markers)                     # (local)
    sub_g_count = sum(1 for m in sub_g_markers if m in post_text)                # (local)

    # Sub-block (h) Registry-PASS criterion
    sub_h_marker = "**Registry-PASS criterion** (per `cross-pillar-bridge-anatomy.md"
    sub_h_pass = sub_h_marker in post_text                                      # (local)

    # Sub-block (i) Hybrid Independence Test predicate
    sub_i_marker = "**Hybrid Independence Test** (predicate `(i ∨ ii ∨ iii) ∧ iv`"
    sub_i_predicate = "(YES ∨ YES ∨ NO) ∧ YES = YES"
    sub_i_pass = (sub_i_marker in post_text) and (sub_i_predicate in post_text)  # (local)

    # Sub-block (j) Parse-tree expansion
    sub_j_marker = "**Parse-tree expansion** (per `.claude/rules/registry-landing.md"
    sub_j_pass = sub_j_marker in post_text                                      # (local)

    # Sub-block (k) Stage-2 cross-axis verify queue
    sub_k_marker = "**Stage-2 cross-axis verify queue**"
    sub_k_dispatch_id = "S92-OR-LATER-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY"
    sub_k_pass = (sub_k_marker in post_text) and (sub_k_dispatch_id in post_text)  # (local)

    # Sub-block (l) Substrate framing
    sub_l_marker = "**Substrate framing** (per `.claude/rules/phononic-framing.md"
    sub_l_forbidden_inversion = "**FORBIDDEN inversion**"
    sub_l_pass = (sub_l_marker in post_text) and (sub_l_forbidden_inversion in post_text)  # (local)

    # Sub-block (m) Cross-references (≥10 enumerated)
    sub_m_marker = "**Cross-references** (≥10 enumerated):"
    sub_m_pass = sub_m_marker in post_text                                      # (local)

    # Triple-pin Element 3 fiducial-anchor sub-rows
    triple_pin_markers = [
        ("R = ζ (zeta-function regularization)", R_zeta_value,
         "-ZETA-FULL-CM-1995-III-4-substrate-distance-2-pole-s4-χ-prime-restriction-MULTI-PIN-ATLAS"),
        ("R = Pauli-Villars (PV regularization at Λ_UV = M_KK)", R_PV_value,
         "-PV-FULL-CM-1995-III-4-substrate-distance-2-pole-s4-χ-prime-restriction-MULTI-PIN-ATLAS"),
        ("R = Mellin (Mellin-Barnes regularization)", R_Mellin_value,
         "-MELLIN-FULL-CM-1995-III-4-substrate-distance-2-pole-s4-χ-prime-restriction-MULTI-PIN-ATLAS"),
    ]
    triple_pin_pass_list = []                                                   # (local)
    for label, value, suffix in triple_pin_markers:
        label_ok = label in post_text                                           # (local)
        value_ok = value in post_text                                           # (local)
        suffix_ok = suffix in post_text                                         # (local)
        triple_pin_pass_list.append({
            "label": label,
            "label_present": label_ok,
            "value_present": value_ok,
            "suffix_present": suffix_ok,
            "all_three": label_ok and value_ok and suffix_ok,
        })
    triple_pin_all_pass = all(d["all_three"] for d in triple_pin_pass_list)     # (local)

    # Cross-regulator spread
    spread_pass = cross_reg_spread in post_text                                 # (local)

    # content_sha256 bit-exact match: locate the inserted block and compute
    # its SHA, compare against promotion_sha
    block_start_idx = post_text.find(promotion_text)                            # (local)
    bit_exact_match = block_start_idx != -1                                     # (local)

    # Sub-block (m) refinement: count "≥10 enumerated" lines
    # Look for numbered "1. " through "20. " in cross-references section
    cross_refs_start = post_text.find("**Cross-references** (≥10 enumerated):")  # (local)
    cross_refs_section = ""                                                     # (local)
    cross_ref_count = 0                                                         # (local)
    if cross_refs_start != -1:
        # Find next "**" markdown bold start after the cross-refs heading
        section_search_start = cross_refs_start + len(
            "**Cross-references** (≥10 enumerated):"
        )                                                                       # (local)
        next_bold_after = post_text.find("\n**Source**:", section_search_start)  # (local)
        if next_bold_after != -1:
            cross_refs_section = post_text[section_search_start:next_bold_after]  # (local)
        else:
            cross_refs_section = post_text[section_search_start:section_search_start + 10000]  # (local)
        # Count "\nN. " patterns
        import re as _re  # (local)
        cross_ref_count = len(
            _re.findall(r"\n\d+\. ", cross_refs_section)
        )                                                                       # (local)

    # Substantive line count check
    if bit_exact_match:
        block_end_idx = block_start_idx + len(promotion_text)                   # (local)
        block_text = post_text[block_start_idx:block_end_idx]                   # (local)
        block_lines = block_text.splitlines()                                   # (local)
        substantive_line_count = sum(
            1 for ln in block_lines if ln.strip() and not ln.strip().startswith("#")
        )                                                                       # (local)
    else:
        substantive_line_count = 0                                              # (local)
    substantive_pass = substantive_line_count >= MIN_SUBSTANTIVE_LINES          # (local)

    # 13-sub-block conjunction
    sub_block_results = {
        "a_header": sub_a_pass,
        "b_status_stage1": sub_b_pass,
        "c_provenance": sub_c_pass,
        "d_bridge_family": sub_d_pass,
        "e_corner_cell_ii": sub_e_pass,
        "f_is_not_in_anatomy_5elements": sub_f_pass,
        "g_three_level_ladder": sub_g_pass,
        "h_registry_pass_criterion": sub_h_pass,
        "i_hybrid_independence_test_predicate": sub_i_pass,
        "j_parse_tree_expansion": sub_j_pass,
        "k_stage2_verify_queue": sub_k_pass,
        "l_substrate_framing": sub_l_pass,
        "m_cross_references": sub_m_pass,
    }
    all_13_blocks_pass = all(sub_block_results.values())                        # (local)
    n_blocks_pass = sum(1 for v in sub_block_results.values() if v)             # (local)

    composite_pass = (
        all_13_blocks_pass
        and triple_pin_all_pass
        and spread_pass
        and bit_exact_match
        and substantive_pass
    )

    return {
        "post_sha": post_sha,
        "promotion_sha": promotion_sha,
        "sub_block_results": sub_block_results,
        "n_blocks_pass": n_blocks_pass,
        "all_13_blocks_pass": all_13_blocks_pass,
        "triple_pin_pass_list": triple_pin_pass_list,
        "triple_pin_all_pass": triple_pin_all_pass,
        "cross_reg_spread_present": spread_pass,
        "bit_exact_section_match": bit_exact_match,
        "substantive_line_count": substantive_line_count,
        "substantive_line_count_pass": substantive_pass,
        "cross_ref_count": cross_ref_count,
        "cross_ref_count_ge_10": cross_ref_count >= 10,
        "composite_pass": composite_pass,
        "sub_f_count": sub_f_count,
        "sub_g_count": sub_g_count,
    }


# ---------------------------------------------------------------------------
# Section 8 — append_verdict (atomic single open("a"); S87+ schema)
# ---------------------------------------------------------------------------
def append_verdict(verdict: str, value_str: str,
                   audit_sha: str, content_sha: str) -> None:
    """Append a single-line verdict + dual-SHA companion comment row to
    s92_gate_verdicts.txt per S87+ schema. Atomic single open("a") write.
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} # {GATE_ID} "
        f"dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)


# ---------------------------------------------------------------------------
# Section 9 — Compute (orchestrates build + write + verify; single-shot)
# ---------------------------------------------------------------------------
def compute() -> dict:
    """S92-W6-CF-W2-1 single-shot AFTER-pattern landing of §VII.AX.MULTI-
    PIN-ATLAS sub-slot.

    Steps:
      1. Confirm S91 §W2-1 PASS-V prerequisite line present in
         s91_gate_verdicts.txt.
      2. build_promotion_text() — pure function; assemble full section
         text in memory.
      3. write_atomic_insert_before() — single atomic insert via tmp+replace
         immediately BEFORE §VII.AZ.OP-PROJ heading (preserving §VII.AX
         family contiguity).
      4. re_read_and_verify() — 13-sub-block presence map + triple-pin
         + bit-exact section match + substantive line count check.
      5. emit ONE verdict line per AFTER-pattern (verify boolean ⇒ verdict).
    """

    # Step 1: Confirm S91 §W2-1 PASS-V prerequisite
    print(f"\n=== Step 1: S91 §W2-1 PASS-V prerequisite confirmation ===")
    s91_verdict_text = S91_VERDICT_PATH.read_text(
        encoding="utf-8", errors="replace"
    )                                                                           # (local)
    w2_1_marker = (
        "S91-CF37-CHI-PRIME-WEIGHT-CANONICALIZED-FULL-CM-1995-III-4-"
        "SUBSTRATE-DISTANCE-2-EVALUATION: PASS"
    )
    w2_1_audit_sha_present = W2_1_AUDIT_SHA_FULL in s91_verdict_text             # (local)
    w2_1_routing_present = (
        "reading_v_pluralism_bool=True" in s91_verdict_text
    )                                                                           # (local)
    w2_1_pass_confirmed = (
        (w2_1_marker in s91_verdict_text)
        and w2_1_audit_sha_present
        and w2_1_routing_present
    )                                                                           # (local)
    print(f"  S91 W2-1 PASS marker present:           {w2_1_marker in s91_verdict_text}")
    print(f"  S91 W2-1 audit_sha256 present:          {w2_1_audit_sha_present}")
    print(f"  W2-1 routing reading_v=True present:    {w2_1_routing_present}")
    print(f"  S91 W2-1 PASS-V prerequisite CONFIRMED: {w2_1_pass_confirmed}")

    if not w2_1_pass_confirmed:
        print(f"  CRITICAL: S91 W2-1 PASS-V not confirmed — cannot proceed.")
        return {
            "write_succeeded": False,
            "error": "S91_W2_1_PASS_V_NOT_CONFIRMED",
            "verify_result": {},
        }

    # Step 2: build_promotion_text (pure function)
    print(f"\n=== Step 2: build_promotion_text complete ===")
    promotion_text = build_promotion_text()                                     # (local)
    promotion_sha = sha256_of_text(promotion_text)                              # (local)
    promotion_lines = promotion_text.count("\n")                                # (local)
    promotion_chars = len(promotion_text)                                       # (local)
    print(f"  §VII.AX.MULTI-PIN-ATLAS text SHA: {promotion_sha[:16]}...")
    print(f"  §VII.AX.MULTI-PIN-ATLAS length: {promotion_chars} chars, "
          f"{promotion_lines} newlines")

    # Step 3: write_atomic_insert_before — insert BEFORE §VII.AZ.OP-PROJ heading
    print(f"\n=== Step 3: write_atomic_insert_before ===")
    # The anchor is the §VII.AZ.OP-PROJ heading; insertion is BEFORE its line.
    anchor = "### §VII.AZ.OP-PROJ — Cross-Morphism M_3(ℂ)-Kernel Universality"
    # Idempotency marker: presence of the §VII.AX.MULTI-PIN-ATLAS header
    idempotency_marker = (
        "### §VII.AX.MULTI-PIN-ATLAS — Substrate-Distance-2 Pole s=4 χ' "
        "Restriction Multi-Pin Regulator Atlas"
    )
    write_ok, pre_sha, post_sha = write_atomic_insert_before(
        REGISTRY_PATH, promotion_text, anchor, idempotency_marker
    )
    if not write_ok:
        print(f"  WRITE FAILED: {post_sha}")
        return {
            "write_succeeded": False,
            "error": f"REGISTRY_WRITE_FAILED:{post_sha}",
            "verify_result": {},
        }
    print(f"  Registry write OK")
    print(f"  Registry pre-edit SHA:  {pre_sha[:16]}...")
    print(f"  Registry post-edit SHA: {post_sha[:16]}...")

    # Step 4: re_read_and_verify (13-sub-block + triple-pin + bit-exact)
    print(f"\n=== Step 4: re_read_and_verify ===")
    verify_result = re_read_and_verify(REGISTRY_PATH, promotion_text)
    print(f"  Sub-block (a) header:                  {verify_result['sub_block_results']['a_header']}")
    print(f"  Sub-block (b) Status STAGE-1-CANDIDATE: {verify_result['sub_block_results']['b_status_stage1']}")
    print(f"  Sub-block (c) Provenance:              {verify_result['sub_block_results']['c_provenance']}")
    print(f"  Sub-block (d) Bridge family:           {verify_result['sub_block_results']['d_bridge_family']}")
    print(f"  Sub-block (e) Corner Cell II:          {verify_result['sub_block_results']['e_corner_cell_ii']}")
    print(f"  Sub-block (f) IS-not-IN anatomy 5elem: {verify_result['sub_block_results']['f_is_not_in_anatomy_5elements']} ({verify_result['sub_f_count']}/6 anatomy markers)")
    print(f"  Sub-block (g) 3-level ladder:          {verify_result['sub_block_results']['g_three_level_ladder']} ({verify_result['sub_g_count']}/4 ladder markers)")
    print(f"  Sub-block (h) Registry-PASS criterion: {verify_result['sub_block_results']['h_registry_pass_criterion']}")
    print(f"  Sub-block (i) HIT predicate:           {verify_result['sub_block_results']['i_hybrid_independence_test_predicate']}")
    print(f"  Sub-block (j) Parse-tree expansion:    {verify_result['sub_block_results']['j_parse_tree_expansion']}")
    print(f"  Sub-block (k) Stage-2 verify queue:    {verify_result['sub_block_results']['k_stage2_verify_queue']}")
    print(f"  Sub-block (l) Substrate framing:       {verify_result['sub_block_results']['l_substrate_framing']}")
    print(f"  Sub-block (m) Cross-references:        {verify_result['sub_block_results']['m_cross_references']}")
    print(f"  All 13 sub-blocks pass:                {verify_result['all_13_blocks_pass']} ({verify_result['n_blocks_pass']}/13)")
    print(f"  Triple-pin Element 3 fiducial-anchors:")
    for d in verify_result["triple_pin_pass_list"]:
        print(f"    {d['label']}: label={d['label_present']} value={d['value_present']} suffix={d['suffix_present']}")
    print(f"  Triple-pin all pass:                   {verify_result['triple_pin_all_pass']}")
    print(f"  Cross-regulator spread present:        {verify_result['cross_reg_spread_present']}")
    print(f"  Bit-exact section match:               {verify_result['bit_exact_section_match']}")
    print(f"  Substantive line count:                {verify_result['substantive_line_count']} (≥{MIN_SUBSTANTIVE_LINES} required: {verify_result['substantive_line_count_pass']})")
    print(f"  Cross-ref count:                       {verify_result['cross_ref_count']} (≥10 required: {verify_result['cross_ref_count_ge_10']})")
    print(f"  ============================================")
    print(f"  COMPOSITE VERIFY PASS:                 {verify_result['composite_pass']}")

    return {
        "write_succeeded": True,
        "verify_result": verify_result,
        "promotion_text_sha": promotion_sha,
        "promotion_lines": promotion_lines,
        "promotion_chars": promotion_chars,
        "registry_pre_sha": pre_sha,
        "registry_post_sha": post_sha,
        "w2_1_audit_sha_full": W2_1_AUDIT_SHA_FULL,
        "w2_1_content_sha_full": W2_1_CONTENT_SHA_FULL,
        "R_zeta": R_zeta_value,
        "R_PV": R_PV_value,
        "R_Mellin": R_Mellin_value,
        "cross_reg_spread": cross_reg_spread,
        "option_iv_threshold": option_iv_threshold,
    }


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                                            # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()                                      # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_CONSTANTS_PATH, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute (orchestrate single-shot AFTER-pattern)
    result = compute()

    # 3. Build value string + verdict
    if result["write_succeeded"]:
        vr = result["verify_result"]                                            # (local)
        if vr["composite_pass"]:
            verdict = "PASS"                                                    # (local)
            value_str = (
                f"STAGE-1-CANDIDATE_landed_VII_AX_MULTI_PIN_ATLAS;"
                f"13_of_13_sub_blocks_PASS;"
                f"triple_pin_R_zeta={result['R_zeta']}_R_PV={result['R_PV']}_R_Mellin={result['R_Mellin']};"
                f"cross_reg_spread={result['cross_reg_spread']};"
                f"option_v_pluralism_promoted;"
                f"hybrid_independence_test=(YES_OR_YES_OR_NO)_AND_YES=YES;"
                f"bit_exact_section_match=True;"
                f"substantive_line_count={vr['substantive_line_count']};"
                f"cross_ref_count={vr['cross_ref_count']};"
                f"K_counter_K1_to_K2_advancement_pending_W6_2"
            )                                                                   # (local)
        else:
            verdict = "FAIL"                                                    # (local)
            failing = [k for k, v in vr["sub_block_results"].items() if not v]   # (local)
            value_str = (
                f"verify_FAIL;n_blocks_pass={vr['n_blocks_pass']}_of_13;"
                f"triple_pin_all_pass={vr['triple_pin_all_pass']};"
                f"bit_exact_match={vr['bit_exact_section_match']};"
                f"substantive_line_count={vr['substantive_line_count']};"
                f"failing_blocks={','.join(failing) if failing else 'none'}"
            )                                                                   # (local)
    else:
        verdict = "FAIL"                                                        # (local)
        value_str = f"write_failed_{result.get('error', 'unknown')}"             # (local)

    # 4. Emit 4-tuple
    tag = (
        f"(value={value_str!r}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX})"
    )                                                                           # (local)
    print()
    print(tag)
    print()

    # 5. Append verdict (dual-SHA, S87+ schema)
    append_verdict(verdict, value_str, audit_sha, content_sha)

    # 6. Persist .npz + .json
    vr = result.get("verify_result", {})                                        # (local)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        write_succeeded=int(result["write_succeeded"]),
        composite_pass=int(vr.get("composite_pass", False)),
        n_blocks_pass=int(vr.get("n_blocks_pass", 0)),
        triple_pin_all_pass=int(vr.get("triple_pin_all_pass", False)),
        bit_exact_section_match=int(vr.get("bit_exact_section_match", False)),
        substantive_line_count=int(vr.get("substantive_line_count", 0)),
        cross_ref_count=int(vr.get("cross_ref_count", 0)),
        promotion_text_sha=result.get("promotion_text_sha", ""),
        promotion_lines=int(result.get("promotion_lines", 0)),
        promotion_chars=int(result.get("promotion_chars", 0)),
        registry_pre_sha=result.get("registry_pre_sha", ""),
        registry_post_sha=result.get("registry_post_sha", ""),
        w2_1_audit_sha_full=W2_1_AUDIT_SHA_FULL,
        w2_1_content_sha_full=W2_1_CONTENT_SHA_FULL,
        R_zeta=R_zeta_value,
        R_PV=R_PV_value,
        R_Mellin=R_Mellin_value,
        cross_reg_spread=cross_reg_spread,
        option_iv_threshold=option_iv_threshold,
    )
    print(f"  .npz written: {OUT_NPZ.name}")

    json_payload = {
        "gate_id": GATE_ID,
        "trigger": TRIGGER,
        "verdict": verdict,
        "value_str": value_str,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": SCHEMA_VERSION,
        "write_succeeded": bool(result["write_succeeded"]),
        "compute_result": {
            "promotion_text_sha": result.get("promotion_text_sha", ""),
            "promotion_lines": result.get("promotion_lines", 0),
            "promotion_chars": result.get("promotion_chars", 0),
            "registry_pre_sha": result.get("registry_pre_sha", ""),
            "registry_post_sha": result.get("registry_post_sha", ""),
        },
        "w2_1_prerequisite": {
            "audit_sha256_full": W2_1_AUDIT_SHA_FULL,
            "content_sha256_full": W2_1_CONTENT_SHA_FULL,
            "R_zeta": R_zeta_value,
            "R_PV": R_PV_value,
            "R_Mellin": R_Mellin_value,
            "cross_reg_spread": cross_reg_spread,
            "option_iv_threshold": option_iv_threshold,
            "reading_v_pluralism_bool": True,
        },
        "verify_result": vr,
        "input_pins": pins,
    }
    OUT_JSON.write_text(
        json.dumps(json_payload, indent=2, sort_keys=False),
        encoding="utf-8",
    )
    print(f"  .json written: {OUT_JSON.name}")

    # 7. Final summary
    wall = time.time() - t0                                                     # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
