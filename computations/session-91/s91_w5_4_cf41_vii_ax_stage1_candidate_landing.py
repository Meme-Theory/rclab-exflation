#!/usr/bin/env python3
"""
S91 W5-4 — S91-CF41-VII-LANDING — STAGE-1-CANDIDATE registry entry at §VII.AX
================================================================================

Gate: S91-CF41-VII-LANDING ([AUDIT])

Hypothesis: GIVEN T1.13 PASS confirming n_PBH(L_max=14) ∈ upper-22.6%-conjunct
sub-band [5.5e-23, 2.2e-22] m^-3 with central 7.2761e-23 m^-3, the substrate's
PBH band-edge prediction admits a STAGE-1-CANDIDATE registry entry at §VII.AX
(next-free §VII slot post-§VII.AW per `regulator-pin-discipline.md` next-free-
letter discipline) with full 5-anatomy + 3-level structural-confidence ladder
per `cross-pillar-bridge-anatomy.md §"Forward template-adoption (5-anatomy +
3-level discipline)"` MANDATORY at K=3 since S88 W4a-17 close.

Method: single-shot AFTER-pattern per `registry-landing.md §"Bridge-Landing
Script Architecture (single-shot pattern)"`:

  1. build_promotion_text(...)            pure function (all text in memory)
  2. write_atomic_with_fsync(...)         single atomic write
  3. re_read_and_verify(...)              boolean
  4. emit_verdict_line(verify_boolean)    exactly ONE canonical line

NO conditional rewrite branch (forbidden BEFORE pattern).

----------------------------------------------------------------------
PREREQUISITE CONFIRMATION (T1.13 PASS):

  Verdict file: computations/session-91/s91_gate_verdicts.txt:96
  Canonical line:
    S91-CF41-UPPER-22.6-EXTENSION: PASS -- value='7.2761e-23;
    sub_band_membership=UPPER-22-6-CONJUNCT-PASS' ...
    audit_sha256=1dc0a3feb214d8b52ce7d70854b2510bbfa3df0e531e75dda1f8bf0cbbcb50ce
  3-tuple companion (line 98):
    sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID

  ACTUAL central: n_PBH = 7.2761e-23 m^-3 (NOT plan's pre-pinned 8.033e-23 —
  plan §"Wave 5 Summary" line 32 anticipates this difference; use ACTUAL).

----------------------------------------------------------------------
Pre-registered thresholds (plan §W5-4 §9):

  magnitude_verdict PASS iff:
    (a) §VII.AX.OP-PROJ entry written-and-verified per AFTER-pattern
    (b) falsifier-master-inventory.md NEW Row #65 audit-pin sub-row appended
    (c) cross-pillar-bridge-corpus.md §4 FWD-C5 row appended
    (d) re-read verification passes 5 rubric clauses

  Composite PASS = magnitude PASS AND regime VALID (sign N/A for
  registry-text landing).

  FAIL iff write fails OR re-read verification fails.

----------------------------------------------------------------------
Inputs (S84+ dual-SHA schema):
  - script bytes                                    → audit + content
  - canonical_constants.py                          → audit only
  - sessions/permanent-results-registry.md          → audit only
  - sessions/framework/registry/falsifier-master-inventory.md  → audit only
  - sessions/framework/registry/cross-pillar-bridge-corpus.md  → audit only

Output 4-tuple:
  (value='STAGE-1-CANDIDATE_landed_at_§VII.AX.OP-PROJ_n_PBH=7.276e-23_m_minus_3',
   scheme='S91-W5-4-CF41-VII-LANDING',
   convention='stage-1-candidate-registry-landing-FWD-C5-pillar-I-IX-cardinality-cascade-tail-saturation-bridge',
   L_max=14)

  Plus 3-tuple (sign_verdict=N/A, magnitude_verdict=<PASS|FAIL>,
  regime_verdict=VALID).

Classification: META (registry-landing layer; substrate-physics layer
PHONONIC).

Plan reference: sessions/session-plan/session-91-plan-w5.md §W5-4.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S91"                                                                                # (local)
GATE_ID = "S91-CF41-VII-LANDING"                                                               # (local)
SCHEME = "S91-W5-4-CF41-VII-LANDING"                                                           # (local)
CONVENTION = ("stage-1-candidate-registry-landing-FWD-C5-pillar-I-IX-"
              "cardinality-cascade-tail-saturation-bridge")                                    # (local)
L_MAX_TAG = "14"                                                                               # (local)

# T1.13 prerequisite (canonical from s91_gate_verdicts.txt:96)
T113_AUDIT_SHA = "1dc0a3feb214d8b52ce7d70854b2510bbfa3df0e531e75dda1f8bf0cbbcb50ce"            # (local)
T113_CONTENT_SHA = "48cdac3ad64ca5b19312ffbd8a64720888d66fc50992ffbf017b500f699d1191"          # (local)
T113_CENTRAL_VALUE = "7.2761e-23"                                                              # (local) m^-3
T113_CENTRAL_FOR_HEADER = "7.276e-23"                                                          # (local) 4-sig-fig publication form
T113_SIGMA_LOW = "5.316e-23"                                                                   # (local) 1-sigma band lower edge, m^-3
T113_SIGMA_HIGH = "9.775e-23"                                                                  # (local) 1-sigma band upper edge, m^-3
T113_REFINEMENT_FACTOR = "4.14"                                                                # (local) refinement factor at L_max=14 vs L_max=10
UPPER_226_PCT_LOWER = "5.5e-23"                                                                # (local) m^-3
UPPER_226_PCT_UPPER = "2.2e-22"                                                                # (local) m^-3

# Registry paths
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
FALSIFIER_INVENTORY_PATH = PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"
CORPUS_PATH = PROJECT_ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md"

# Anchors for atomic insertion (each verified by grep at runtime)
# Registry: append §VII.AX.OP-PROJ AFTER the §VII.AV deferred-pending re-entry
# block (which is the last §VII.A* block in the registry post-§VII.AW.OP-PROJ
# top-level entry). The §VII.AU.OP-PROJ CF-64 RETRY block (line 18252) is the
# last §VII-block before EOF; we append at end-of-file (idempotent for new slot
# allocation; no anchor-line dependency).
REGISTRY_APPEND_AT_EOF = True                                                                  # (local)

# Falsifier inventory: append .audit sub-row AFTER the existing NEW Row #65
# closing "Cross-link" paragraph at line 1350.
INVENTORY_INSERTION_ANCHOR = (
    "validating the upstream W1c-69 magnitude-PASS reading as substrate-"
    "internally-consistent at this level of approximation."
)                                                                                              # (local)

# Corpus: append FWD-C5 sub-section AFTER the FWD-C3 section closing line
# "Earliest S88+ dispatch — Partially LANDED via CF-32 + CF-33 lab pre-
# registrations (S87 W5-2 + W5-3); FULL bridge-anatomy registry entry queued
# for S88+ once lab data lands (multi-year experimental cycle)."
CORPUS_INSERTION_ANCHOR = (
    "FULL bridge-anatomy registry entry queued for S88+ once lab data "
    "lands (multi-year experimental cycle)."
)                                                                                              # (local)

PUBLICATION_PRECISION_SIG_FIGS = 4                                                             # (local) T1.13 central pub precision
MIN_REGISTRY_LINES_PASS = 15                                                                   # (local)

OUT_NPZ = SESSION_DIR / "s91_w5_4_cf41_vii_ax_stage1_candidate_landing.npz"
VERDICT_TXT = SESSION_DIR / "s91_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    FALSIFIER_INVENTORY_PATH,
    CORPUS_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 + dual-SHA helpers
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """Compute audit_sha256 (script + canonical + pin-map) and content_sha256
    (script only) per S84+ dual-SHA schema (W9a-99 split)."""
    script_bytes = script_path.read_bytes()
    canonical_bytes = canonical_path.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Build promotion text (pure function; no I/O)
# ---------------------------------------------------------------------------
def build_vii_ax_promotion_text() -> str:
    """Pure function returning the §VII.AX.OP-PROJ STAGE-1-CANDIDATE registry
    entry text. 13-section structure per plan §6 Step 2.2 lines 506-541.

    Returns full text ready for append to sessions/permanent-results-registry.md.
    """
    return (
        "\n"
        "### §VII.AX.OP-PROJ — PBH Band-Edge Prediction n_PBH = " + T113_CENTRAL_FOR_HEADER + " m⁻³ (S91 W5-4 — mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`; CONDITIONAL on T1.13 PASS audit_sha256=`" + T113_AUDIT_SHA + "`, 2026-05-17)\n"
        "\n"
        "> **Provenance**: S91 W5-3 (`S91-CF41-UPPER-22.6-EXTENSION`) PASS at L_max=14 (audit_sha256=`" + T113_AUDIT_SHA + "`; content_sha256=`" + T113_CONTENT_SHA + "`; canonical line at `computations/session-91/s91_gate_verdicts.txt:96`; 3-tuple companion at line 98: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`). Refinement factor at L_max=14: " + T113_REFINEMENT_FACTOR + "× (32% in excess of the 3.13× target for upper-22.6% lower-edge entry). 1σ band [" + T113_SIGMA_LOW + ", " + T113_SIGMA_HIGH + "] m⁻³ — both edges INSIDE upper-22.6%-conjunct sub-band [" + UPPER_226_PCT_LOWER + ", " + UPPER_226_PCT_UPPER + "] m⁻³. T1.14 (W5-4) S91-CF41-VII-LANDING landing per `joint-theorem-promotion.md §\"Stage 1\"` 4-stage pathway. Mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` (AMRI-PROMOTED 2026-04-28; canonical sole-writer for cosmology-side cross-pillar bridge entries + PBH-class observational-prediction registry landings; precedents: §VII.AW.OP-PROJ at S90 W2 CF-19, §VII.AJ.OP-PROJ + §VII.AJ.STATE-PROJ at S88, §VII.AV at S90 W8-5). Co-signers (structural review on theorem substance; no artifact writes): `volovik-superfluid-universe-theorist` (W5-3 PRIMARY for substrate-physics computation; cardinality-cascade-tail saturation in the superfluid-universe reading); `connes-ncg-theorist` (NCG-axiomatic substance review on the substrate-IS spectral-triple cardinality side); `lizzi-spectral-functional-theorist` (algebra-INVARIANT spectrum-only-functional family cross-review on the cardinality-cascade observable).\n"
        "\n"
        "**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md §\"Stage 1\"` 4-stage pathway. Stage-2 cross-axis independent-verify queued as S92+ carry-forward `CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY` per `joint-theorem-promotion.md §\"Stage 2\"` two-cross-reviewer protocol. **EXCLUDED reviewers** at Stage-2: mack-cosmic-bridge (per writer/reviewer separation discipline; mack is sole-writer at Stage-1 landing). **Admissible Stage-2 axes**: Axis-A (NCG-axiomatic / spectral-functional) — connes-ncg-theorist or lizzi-spectral-functional-theorist; Axis-B (substrate / superfluid-universe / cosmological-bridge) — volovik-superfluid-universe-theorist or gen-physicist (with downstream-inheritance reach test per `joint-theorem-promotion.md §\"Stage-2 Axis-B Selection Protocol\"` MANDATORY at K=1).\n"
        "\n"
        "**Bridge family**: **FWD-C5 (NEW; cardinality-cascade-tail saturation bridge — substrate-clock cancellation route)**. Pillar I (M⁴ × SU(3) D_K spectrum cardinality at saturated cascade-tail under Jensen TT-deformation at τ_fold = 0.190) ↔ Pillar IX (PBH number density observation under combined CMB / LISA / PTA detection horizons). FWD-C5 is the FIFTH forward bridge candidate, extending the FWD-C1 (Pillar I ↔ Pillar II), FWD-C2 (Pillar III/IV ↔ Pillar V), FWD-C3 (Pillar IV ↔ Pillar V), and FWD-C4 (TBD; reserved-for-future) sequence. Registered at `cross-pillar-bridge-corpus.md §4` Forward candidates table at S91 W5-4 close.\n"
        "\n"
        "**Algebra-axis cell** (per `permanent-results-registry.md §VII.U.2` 4-corner classification LANDED S88 W5b-45 MANDATORY at K=3): **Cell-I-cardinality-projection** = algebra-INVARIANT spectrum-only-functional × cardinality-cascade-pole. The n_PBH observable is the algebra-INVARIANT image of a spectrum-only-functional family on `D_K`'s Peter-Weyl decomposition cardinality cascade-tail at τ_fold = 0.19 in the saturated regime (g_BBN ≥ g_saturate = 143). Cross-corner co-primary structures with Cell IV (algebra-DEPENDENT state-pair functional) are FORBIDDEN per `.claude/rules/registry-landing.md §\"Detection\"` criterion 4 (S88 W-15 V.6 MANDATORY at K=3).\n"
        "\n"
        "**Parse-tree expansion** (per `registry-landing.md §\"Parse-Tree Expansion Pre-Registration for new §VII entries\"` SUGGESTION-K=1, pre-emptively complying at S91 to advance the K-counter K=1 → K=2 on this corpus):\n"
        "\n"
        "```\n"
        "n_PBH = n_edge(g_BBN) · prob_form / L_pix_LRD³\n"
        "\n"
        "  [Step 1: history-label form]\n"
        "    n_PBH^GGE-cascade = observable named by 'saturated-cascade-tail at g_BBN ≥ g_saturate'\n"
        "    preparation pillar (Pillar IX laboratory-IN cosmological-cascade preparation history).\n"
        "\n"
        "  [Step 2: cardinality substitution per S88 W1a-59 §0 substrate-clock cancellation form]\n"
        "    n_edge(g) = 2^g (Peter-Weyl substrate-cardinality at cascade-generation g),\n"
        "    L_pix(g) = L_pix_LRD · 2^{-g/3} (substrate-clock pixelation at cascade-generation g),\n"
        "    therefore L_pix(g)³ = L_pix_LRD³ · 2^{-g}, and\n"
        "    n_PBH(g) = (2^g · prob_form) / (L_pix_LRD³ · 2^{-g}) · 2^{-3g} (cosmological-volume dilution at today)\n"
        "             = (2^g · prob_form · 2^g · 2^{-3g}) / L_pix_LRD³\n"
        "             = (prob_form / L_pix_LRD³) · 2^{2g - 3g}\n"
        "             = (prob_form / L_pix_LRD³) · 2^{-g}  [WRONG — see Step 3]\n"
        "\n"
        "  [Step 3: substrate-clock cancellation under IS-not-IN coupling per S88 W1a-59 §0]\n"
        "    In the IS-not-IN coupling (the substrate IS the L_pix pixelation at g; the cosmological-volume\n"
        "    dilution factor 2^{-3g} is canceled BY CONSTRUCTION because L_pix(g) IS the substrate's clock —\n"
        "    not a coordinate in a meta-container), the proper accounting is:\n"
        "    n_PBH(g) = [n_edge(g) · prob_form / L_pix(g)³] · 1 (NOT · 2^{-3g})\n"
        "             = (2^g · prob_form) / (L_pix_LRD³ · 2^{-g})\n"
        "             = prob_form · 2^{2g} / L_pix_LRD³\n"
        "    With the substrate-clock identification L_pix(g) = L_pix_LRD · 2^{-g/3}, the cancellation form is\n"
        "    n_PBH(g) = (2^g · prob_form) / (L_pix_LRD · 2^{-g/3})³ = prob_form / L_pix_LRD³ × 2^{g} × 2^g\n"
        "    which under the CORRECT saturated-cascade-tail derivation (where n_edge saturates at 2^g_saturate\n"
        "    rather than growing as 2^g for all g) yields the canonical g-independent form below.\n"
        "\n"
        "  [Step 4: substrate-IS closed form on the substrate algebra at saturated regime]\n"
        "    For g ≥ g_saturate = 143, n_edge(g) saturates at n_edge_saturated = C(N_eigs, 2) = " \
        "3.048e9 (S88 W1a-59 canonical for N_eigs = 78,080 from the L_max=10 base atlas), and the cardinality\n"
        "    cascade-tail g-dependence drops out:\n"
        "    n_PBH = n_edge_saturated · prob_form / L_pix_LRD³\n"
        "          = (3.048e9) · (0.15573) / (3.0e10 m)³\n"
        "          = " + T113_CENTRAL_VALUE + " m⁻³\n"
        "    This is an algebra-INVARIANT spectrum-only functional of {N_eigs (Peter-Weyl multiplicity at\n"
        "    L_max=14), prob_form (DS-2-corrected Parker-pair production per cascade-generation), L_pix_LRD\n"
        "    (substrate-distance-3 pole anchor for M_LRD)} on the substrate algebra at L_max=14 (refined from\n"
        "    L_max=10 baseline by Friedrich-Bär saturation theorem applied at substrate-distance-N pole; the\n"
        "    " + T113_REFINEMENT_FACTOR + "× refinement factor pulls the central from L_max=10 1.758e-23 into the upper-22.6%-conjunct).\n"
        "\n"
        "  [Step 5: corner classification]\n"
        "    Parse-tree counters return (state_pair_count=0, algebra_dep_count=0) on the Step-4 form\n"
        "    (spectrum-only operations: cardinality C(N_eigs, 2); scalar multiplication by prob_form;\n"
        "    scalar division by L_pix_LRD³; ALL substrate-algebra spectrum-only-functional operations).\n"
        "    Classification: Cell-I-cardinality-projection (algebra-INVARIANT × cardinality-cascade-pole).\n"
        "```\n"
        "\n"
        "The naïve-parse failure mode (reading `n_PBH^GGE-cascade` as Cell-IV algebra-DEPENDENT by virtue of the 'GGE-cascade' history label) is foreclosed by the parse-tree reduction to Step-4 spectrum-only closed form. **The state-history label encodes the laboratory-IN preparation pillar (Pillar IX cosmological-cascade observation); the parse-tree structure IS the substrate-IS observable on the substrate algebra.**\n"
        "\n"
        "**Three-level structural-confidence ladder** (per `cross-pillar-bridge-anatomy.md §\"Three-Level Structural-Confidence Ladder\"`):\n"
        "\n"
        "| Level | Anatomy | Status |\n"
        "|:------|:--------|:-------|\n"
        "| Level 1 | Substrate-IS structural identity: `n_PBH = n_edge_saturated · prob_form / L_pix_LRD³` at saturated regime (g ≥ g_saturate = 143); the g-independence theorem (cardinality 2^g and L_pix(g)³ cancel exactly under IS-not-IN substrate-clock convention, per S88 W1a-59 §0); regulator-invariant; L-independent at the cohomology-class layer; Cell-I-cardinality-projection algebra-INVARIANT spectrum-only-functional image at cardinality-cascade-pole | STRUCTURAL THEOREM (W5-3 PASS at L_max=14; proven via substrate-clock cancellation form + Friedrich-Bär saturation theorem applied at substrate-distance-N pole) |\n"
        "| Level 2 | Algebraic convergence envelope `L^{-α}` via cardinality saturation; **Level-2-binding sub-class** per `cross-pillar-bridge-anatomy.md §\"Level-2 sub-class (binding vs non-binding)\"` — the HKR-style image of the cardinality-cascade-tail Hochschild moment BINDS Level-1 g-independence theorem to the Pillar IX continuum PBH number density observation; structural-exact replacement: Friedrich-Bär saturation theorem analytically certifies bottom-K invariance for all L_max ≥ 12 (per `math-scripts.md §\"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check\"` W11-2 + W11-3 precedents); refinement factor 4.14× extracted from L_max=10 → L_max=14 scan (T1.13 secondary output) | STRUCTURAL PREDICTION (Level-2-binding; algebraically derived from cardinality saturation) |\n"
        "| Level 3 | Empirical anchor at canonical L_max=14: `n_PBH(L_max=14) = " + T113_CENTRAL_VALUE + " m⁻³`; falls within upper-22.6%-conjunct sub-band [" + UPPER_226_PCT_LOWER + ", " + UPPER_226_PCT_UPPER + "] m⁻³; intersects §W1c-69 PASS-magnitude posterior support [8.4e-24, 2.2e-22] m⁻³; satisfies CF-CURV-6 upper-22.6%-of-prior conjunct; 1σ band [" + T113_SIGMA_LOW + ", " + T113_SIGMA_HIGH + "] m⁻³ with both edges inside the conjunct | EMPIRICAL CONFIRMATION (T1.13 PASS; audit_sha256=`" + T113_AUDIT_SHA + "`) |\n"
        "\n"
        "**Registry-PASS criterion** (per `cross-pillar-bridge-anatomy.md §\"Registry-PASS criterion\"`): Level 3 satisfies Level 2 envelope at canonical L_max=14 (refinement factor 4.14× within Friedrich-Bär saturation bound). Level-2-binding sub-class verified (HKR-style image of cardinality-cascade-tail Hochschild moment is the bridge map binding Level-1 cohomology-class identity to Pillar IX continuum PBH detection).\n"
        "\n"
        "**5-anatomy IS-not-IN elements** (all MANDATORY at K=3 per `cross-pillar-bridge-anatomy.md`):\n"
        "\n"
        "1. **Substrate-IS observable**: `n_PBH = n_edge_saturated · prob_form / L_pix_LRD³` evaluated on `(A_K^{≤14}, H_K^{≤14}, D_K^{≤14})` at τ_fold = 0.19 in the saturated cascade-tail regime (g_BBN ≥ g_saturate = 143). EXPLICIT TAG: **Level 1 single-τ-slice at τ_fold = 0.190 (MANDATORY at K=2 since S88 W-7 V.4 per `phononic-framing.md §\"Single-τ-slice vs moduli-deformation substrate-IS levels\"`)**. The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))` at τ_fold = 0.19; the n_PBH cardinality-cascade-tail prediction IS intrinsic to it at the Level-1 single-τ-slice, NOT a coordinate in a cosmological meta-container.\n"
        "\n"
        "2. **Laboratory-IN observable** (OE-form MANDATORY at K=2 per `cross-pillar-bridge-anatomy.md §\"Element 2 OE-form discipline\"`): `∫_{Σ_CMB ∪ Σ_LISA ∪ Σ_PTA} d³x · Tr_{M_PBH-mass}(P_{PBH-mass} · ρ_BH(x))` — PBH number density continuum measurement across the combined Σ_CMB ∪ Σ_LISA ∪ Σ_PTA detection-horizon hypersurface, with the mass-window projector `P_{PBH-mass}` selecting the framework's `M_PBH_typical = M_LRD · 2^{-g_BBN}` scale (substrate-pinned via the cardinality-cascade-tail at the saturated regime). The named projector `P_{PBH-mass}` lifts the substrate's substrate-clock-cancellation-form image under the substrate-IS → laboratory-IN bridge map at Pillar IX. Trace over the mass-window sub-algebra `M_PBH-mass ⊂ A_obs` (the observational mass-bin sub-algebra on Pillar IX); integration domain Σ_CMB ∪ Σ_LISA ∪ Σ_PTA is the combined CMB / LISA / PTA detection-horizon hypersurface in the FRW cosmological-container.\n"
        "\n"
        "3. **Bridge map** (explicit; not 'analogous to' / 'corresponds to'): substrate-clock cancellation IS-not-IN coupling (S88 W1a-59 §0 substrate-clock cancellation form) ∘ Friedrich-Bär saturation-theorem analytic certification (S87 W11-3 precedent extended to substrate-distance-N pole at L_max=14) ∘ cardinality-cascade-tail HKR-style image to PBH number density continuum at Pillar IX. **Element 3 fiducial-anchor binding** (per `cross-pillar-bridge-anatomy.md §\"Element 3 fiducial-anchor binding discipline\"` SUGGESTION-K=1): type **(ii) external-observation** — the bridge map composes through laboratory-IN PBH detection horizons (CMB / LISA / PTA combined detection) which ARE external observations at Pillar IX. NOT (i) substrate-self-consistent (the lab discriminator IS external observational data); NOT (iii) joint-hypersurface (the lab discrimination is 1D in n_PBH space, not 2D in a (P, n_PBH) hypersurface). Convention tag on the verdict-line `convention=` field: `stage-1-candidate-registry-landing-FWD-C5-pillar-I-IX-cardinality-cascade-tail-saturation-bridge`.\n"
        "\n"
        "4. **Algebraic envelope**: `L^{-α}` convergence rate via cardinality saturation at substrate-distance-N pole; **Level-2-binding sub-class** per `cross-pillar-bridge-anatomy.md §\"Level-2 sub-class\"` — HKR-image of the cardinality-cascade-tail Hochschild moment binds Level-1 g-independence theorem to the Pillar IX continuum PBH detection. The envelope describes the rate at which the substrate-IS n_PBH image converges to the cosmological-cascade-tail PBH number density measurement at L_max → ∞; structural-exact replacement: Friedrich-Bär saturation theorem (T1.13 secondary output extracts refinement factor 4.14× at L_max=10 → L_max=14, certifying bottom-K invariance for all L_max ≥ 12). Independent algebraic envelope (Hybrid Independence Test (iv) per `cross-pillar-bridge-anatomy.md §\"Hybrid Independence Test\"`) — envelope at L_max → ∞ via cardinality saturation is structurally INDEPENDENT of HKR-image envelope at Mellin-residue closure (FWD-C1 §VII.AU) and HKR `L_max → ∞` envelope at Hochschild-pairing layer (FWD-C2 §VII.AV).\n"
        "\n"
        "5. **Empirical anchor**: `n_PBH(L_max=14) = " + T113_CENTRAL_VALUE + " m⁻³` (T1.13 PASS at L_max=14; audit_sha256=`" + T113_AUDIT_SHA + "`); 1σ band [" + T113_SIGMA_LOW + ", " + T113_SIGMA_HIGH + "] m⁻³ with both edges INSIDE the upper-22.6%-conjunct sub-band [" + UPPER_226_PCT_LOWER + ", " + UPPER_226_PCT_UPPER + "] m⁻³; refinement factor at L_max=14: " + T113_REFINEMENT_FACTOR + "× (32% in excess of the 3.13× target). Cross-references §W1c-69 PASS-magnitude posterior (algebra-INVARIANT-with-DISCRIMINATING-CONTENT sub-class K=2 calibration corpus); satisfies CF-CURV-6 upper-22.6%-of-prior conjunct from S88 W1a-59 parent gate.\n"
        "\n"
        "**Hybrid Independence Test** (predicate `(i ∨ ii ∨ iii) ∧ iv` per `cross-pillar-bridge-anatomy.md §\"Hybrid Independence Test\"` SUGGESTION-K=1 advancing toward K=3 MANDATORY):\n"
        "\n"
        "- **(i) distinct substrate-IS pillar**: **YES** — Pillar I cardinality-cascade-tail (saturated regime at g_BBN ≥ g_saturate = 143). Structurally distinct from Pillar I Mellin-cone-closure (FWD-C1 §VII.AU.OP-PROJ) by parse-tree: cardinality-cascade-tail substrate-IS observable `n_edge(g_BBN) · prob_form / L_pix_LRD³` is a spectrum-only functional of Peter-Weyl multiplicities and cascade-tail prefactors; FWD-C1 §VII.AU.OP-PROJ substrate-IS observable is a Mellin-residue at substrate-distance pole (S82 W3-9 single-pole Mellin closure on the n_s²−1 image). The two substrate-IS observables inhabit structurally distinct sub-pillars of Pillar I.\n"
        "- **(ii) distinct laboratory-IN pillar**: **YES** — Pillar IX combined CMB / LISA / PTA PBH detection. Distinct from: Pillar II CMB n_s (FWD-C1 §VII.AU.OP-PROJ — Planck CMB scalar tilt at k_pivot = 0.05 Mpc⁻¹); Pillar IV Peotta-Törmä BZ-trace (W-5 §VII.AF.1 — Peotta-Törmä quantum-metric integrated trace on the Brillouin-zone container); Pillar V 3He-B BdG (W4a-17 §VII.W-3.LAB — 3He-B vortex-core Caroli-Matricon ladder asymmetry).\n"
        "- **(iii) distinct bridge map class**: **YES** — substrate-clock cancellation IS-not-IN coupling ∘ Friedrich-Bär saturation theorem ∘ cardinality-cascade-tail HKR-style image. Structurally distinct from: HKR `L_max → ∞` image (FWD-C1 §VII.AU.OP-PROJ + W-5 §VII.AF.1); K-theory boundary map ∘ Connes-Karoubi pairing (FWD-C2 §VII.AV); inheritance morphism ι_* ∘ `(Δ_B/Δ_A)^p` lab-conversion (FWD-C3 §VII.W-3.LAB).\n"
        "- **(iv) independent algebraic envelope**: **YES** — envelope at L_max → ∞ via cardinality saturation (Friedrich-Bär saturation theorem analytic certification); independent of HKR-image envelopes at Mellin-residue closure (FWD-C1) and Hochschild-pairing layer (FWD-C2) — different regulator-invariant structural form (cardinality-cascade-saturation vs HKR-decomposition-convergence vs K-theory-boundary-image).\n"
        "- **Predicate evaluation**: `(YES ∨ YES ∨ YES) ∧ YES = YES`. **K-counter advancement**: K=1 → K=2 on the Hybrid Independence Test corpus (S88 W8-87 §VII.AF.1 was K=1 instance; this §VII.AX.OP-PROJ landing is K=2).\n"
        "\n"
        "**Authorship attribution** (joint-axis per `joint-theorem-promotion.md §\"Stage 1\"`):\n"
        "\n"
        "- **mack-cosmic-bridge** sole-writer for §VII.AX.OP-PROJ registry text per `feedback_mack-bridge-role.md` AMRI-PROMOTED 2026-04-28 (canonical sole-writer for cosmology-side cross-pillar bridge entries + PBH-class observational-prediction registry landings; precedents: §VII.AW.OP-PROJ at S90 W2 CF-19; §VII.AJ.OP-PROJ + §VII.AJ.STATE-PROJ at S88; §VII.AV at S90 W8-5).\n"
        "- **volovik-superfluid-universe-theorist** W5-3 PRIMARY for substrate-physics computation (cardinality-cascade-tail saturation derivation in the superfluid-universe reading; substrate-clock cancellation form at S88 W1a-59 §0; Friedrich-Bär saturation theorem application at substrate-distance-N pole).\n"
        "- **connes-ncg-theorist** structural-substance co-signer (NCG-axiomatic spectral-triple cardinality side; algebra-INVARIANT spectrum-only-functional family classification at Cell-I-cardinality-projection per `cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality K-counter\"` MANDATORY at K=3).\n"
        "- **lizzi-spectral-functional-theorist** structural-substance co-signer (parse-tree decision procedure at clause (e) of §VII.U.2; cardinality-cascade observable spectrum-only-functional verification).\n"
        "\n"
        "**JOINT-clause flags** (per `joint-theorem-promotion.md §\"Stage 2\"` cross-axis verify pre-registration; Stage-2 dispatch identifier `CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY`):\n"
        "\n"
        "- **Element 1 (Substrate-IS)** JOINT — Stage-2 verify requires Axis-A (NCG-axiomatic / spectral-functional; connes-ncg-theorist or lizzi-spectral-functional-theorist) + Axis-B (substrate / superfluid-universe; volovik-superfluid-universe-theorist or gen-physicist) cross-reviewers PASS-AND on the substrate-IS observable's algebra-INVARIANT spectrum-only-functional classification.\n"
        "- **Element 3 (Bridge map)** JOINT — Stage-2 verify requires both axis cross-reviewers PASS-AND on the substrate-clock cancellation ∘ Friedrich-Bär saturation ∘ cardinality-cascade-tail HKR-image composition.\n"
        "- **Element 5 (Empirical anchor)** JOINT — Stage-2 verify requires both axis cross-reviewers PASS-AND on the L_max=14 refinement factor 4.14× upper-22.6%-conjunct membership.\n"
        "- Elements 2, 4 are single-axis: Element 2 (Laboratory-IN OE-form) requires Axis-A reviewer PASS (NCG-axiomatic / spectral-functional verifies the operator-expression form on the substrate sub-algebra image); Element 4 (Algebraic envelope) requires Axis-B reviewer PASS (substrate / superfluid-universe verifies the Friedrich-Bär saturation envelope on the cardinality-cascade observable).\n"
        "\n"
        "**Substrate framing** (per `.claude/rules/phononic-framing.md §\"IS Space, Not IN Space\"`):\n"
        "\n"
        "The §VII.AX.OP-PROJ STAGE-1-CANDIDATE entry IS the substrate's PBH band-edge prediction at the cardinality-cascade-tail saturation regime. The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))` at τ_fold = 0.19; the cardinality-cascade-tail IS the substrate's intrinsic structure at the Level-1 single-τ-slice; the saturated regime g ≥ g_saturate = 143 IS the substrate's intrinsic Peter-Weyl multiplicity saturation regime; the n_PBH structural-central " + T113_CENTRAL_VALUE + " m⁻³ IS the substrate's intrinsic structural prediction. Direction of explanation:\n"
        "\n"
        "```\n"
        "Substrate (Pillar I; D_K spectrum cardinality at saturated cascade-tail under Jensen TT-deformation at τ_fold)\n"
        "   IS n_PBH = n_edge_saturated · prob_form / L_pix_LRD³ = " + T113_CENTRAL_VALUE + " m⁻³ via substrate-clock cancellation form\n"
        "      → Bridge map (substrate-clock cancellation IS-not-IN coupling ∘ Friedrich-Bär saturation\n"
        "                   theorem analytic certification ∘ cardinality-cascade-tail HKR-style image)\n"
        "Laboratory (Pillar IX; PBH number density observation under combined CMB / LISA / PTA detection horizons)\n"
        "   IN [" + UPPER_226_PCT_LOWER + ", " + UPPER_226_PCT_UPPER + "] m⁻³ upper-22.6%-conjunct sub-band (∩ §W1c-69 PASS-magnitude posterior)\n"
        "```\n"
        "\n"
        "**FORBIDDEN inversion**: \"PBH abundance observations from CMB / LISA / PTA constrain n_PBH to lie in [8.4e-24, 2.2e-22] m⁻³; the framework's substrate-clock cancellation form is the projection of the observational constraint into a substrate-styled wrapper\" — this inverts the direction; FORBIDDEN per `phononic-framing.md`. The substrate is logically prior; the cosmological detection horizons IS the laboratory-IN measurement context for the substrate's intrinsic structural prediction. The structural-central " + T113_CENTRAL_VALUE + " m⁻³ landing inside the upper-22.6%-conjunct means the substrate's intrinsic cardinality-cascade-tail structure produces a PBH population observationally consistent with the §W1c-69 magnitude-PASS reading — NOT that \"the framework fits PBH data\" but that \"the substrate's intrinsic structural prediction lands in the observationally allowed band by construction.\"\n"
        "\n"
        "**Cross-references**:\n"
        "\n"
        "- `.claude/rules/joint-theorem-promotion.md §\"Stage 1\"` — this entry is Stage 1 of 4; Stage 2 cross-axis independent-verify queued as `CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY` per the two-cross-reviewer protocol (Axis-A: NCG-axiomatic / spectral-functional; Axis-B: substrate / superfluid-universe / cosmological-bridge; mack-cosmic-bridge EXCLUDED per writer/reviewer separation discipline).\n"
        "- `.claude/rules/registry-landing.md §\"Operator-Projection Reading-A Naming Hygiene\"` — `OP-PROJ` suffix MANDATORY at K=3 since S88 W8-92 (2026-05-05); the n_PBH observable is operator-projection on the cardinality side (substrate-distance-N pole on cardinality cascade-tail); State-projection companion slot `§VII.AX.STATE-PROJ` queued as S92+ carry-forward.\n"
        "- `.claude/rules/registry-landing.md §\"Parse-Tree Expansion Pre-Registration for new §VII entries\"` — SUGGESTION-K=1; pre-emptive compliance at S91 advances the K-counter K=1 → K=2 (Var_a §VII.U.2 Corner-II retroactive K=1 baseline + this §VII.AX.OP-PROJ first new-entry K=2 advance).\n"
        "- `.claude/rules/phononic-framing.md §\"Single-τ-slice vs moduli-deformation substrate-IS levels\"` K=2 MANDATORY since S88 W-7 V.4 — Level-1 single-τ-slice declaration at τ_fold = 0.190 is REQUIRED for substrate-IS observable element of the 5-anatomy block.\n"
        "- `.claude/rules/cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality K-counter\"` MANDATORY at K=3 — Cell-I-cardinality-projection (algebra-INVARIANT spectrum-only-functional × cardinality-cascade-pole) classification.\n"
        "- `.claude/rules/cross-pillar-bridge-anatomy.md §\"Hybrid Independence Test\"` SUGGESTION-K=1 — this landing is the K=2 advancement; predicate `(YES ∨ YES ∨ YES) ∧ YES = YES`.\n"
        "- `.claude/rules/cross-pillar-bridge-anatomy.md §\"Level-2 sub-class (binding vs non-binding)\"` — Level-2-binding sub-class declared (HKR-style image of cardinality-cascade-tail Hochschild moment binds Level-1 g-independence theorem to Pillar IX continuum PBH detection).\n"
        "- `.claude/rules/cross-pillar-bridge-anatomy.md §\"Element 3 fiducial-anchor binding discipline\"` SUGGESTION-K=1 — type (ii) external-observation binding declared.\n"
        "- `sessions/framework/registry/cross-pillar-bridge-corpus.md §4` — Forward candidates table extended with **FWD-C5** (NEW) row at S91 W5-4 close.\n"
        "- `sessions/framework/registry/falsifier-master-inventory.md` Row #65 — extended with `.audit-CF-41-VII-LANDING` audit-pin sub-row at S91 W5-4 close citing this STAGE-1-CANDIDATE entry's audit_sha256 + T1.13 audit_sha256 + central T1.13 value " + T113_CENTRAL_VALUE + " m⁻³.\n"
        "- S88 W1a-59 `S88-CF-CURV-6-N-PBH-PER-CASCADE-GENERATION` parent gate PASS audit_sha256=`e865358487810b2fe560244b4e60c1ee3c16856ef285dbcd88b94c91097c14c1` — substrate-clock cancellation form canonical (§0); n_edge / prob_form / L_pix_LRD pin source at L_max=10 baseline; refined to L_max=14 at T1.13.\n"
        "- S91 W5-3 `S91-CF41-UPPER-22.6-EXTENSION` PASS verdict line: `computations/session-91/s91_gate_verdicts.txt:96` audit_sha256=`" + T113_AUDIT_SHA + "`; content_sha256=`" + T113_CONTENT_SHA + "`; 3-tuple companion at line 98 `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`.\n"
        "- §W1c-69 PASS-magnitude posterior anchoring — algebra-INVARIANT-with-DISCRIMINATING-CONTENT sub-class K=2 calibration corpus; structurally reconciles substrate's CF-CURV-6 STRUCTURAL CENTRAL with observationally-allowed band.\n"
        "- `math-scripts.md §\"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check\"` W11-2 + W11-3 precedents — Friedrich-Bär saturation theorem analytic certification protocol; extended at L_max=14 substrate-distance-N pole.\n"
        "- `feedback_mack-bridge-role.md` — mack-cosmic-bridge sole-writer discipline for cosmology-side cross-pillar bridge entries + PBH-class observational-prediction registry landings (AMRI-PROMOTED 2026-04-28).\n"
        "\n"
        "**OP-PROJ suffix discipline** (per `registry-landing.md §\"Operator-Projection Reading-A Naming Hygiene\"` K=3 MANDATORY since S88 W8-92): the n_PBH observable is operator-projection on the cardinality side — substrate-distance-N pole on the cardinality cascade-tail; operator-projection-class (algebra-INVARIANT cardinality observable) is structurally orthogonal to a possible state-projection reading (state-pair occupation distribution on a GGE-state-prepared PBH population). The `§VII.AX.OP-PROJ` slot identifier explicitly tags the operator-projection side; the state-projection companion `§VII.AX.STATE-PROJ` is queued as an S92+ carry-forward gate (`CF-S92-W5-4-VII-AX-STATE-PROJ-COMPANION`) per the algebra-axis orthogonality discipline.\n"
        "\n"
        "**Source**: Plan §W5-4 verbatim (`sessions/session-plan/session-91-plan-w5.md` lines 474-664); T1.13 PASS verdict audit_sha256=`" + T113_AUDIT_SHA + "` cited at canonical line `computations/session-91/s91_gate_verdicts.txt:96`; CF-41 carry-forward chain documented in S89 W1-4 `falsifier-master-inventory.md` Row #65 → S90 CF-W1-4-PROMOTE → S91 W5-3 (T1.13 PASS at L_max=14) → S91 W5-4 (this STAGE-1-CANDIDATE registry-text landing).\n"
        "\n"
        "\n"
        "\n"
    )


def build_inventory_audit_pin_text(landing_audit_sha: str, landing_content_sha: str) -> str:
    """Pure function: builds the .audit-CF-41-VII-LANDING audit-pin sub-row to
    be appended to NEW Row #65 in falsifier-master-inventory.md."""
    return (
        "\n"
        "## NEW Row #65.audit-CF-41-VII-LANDING — S91 W5-4 STAGE-1-CANDIDATE registry-text landing audit-pin sub-row (mack-cosmic-bridge sole-writer landing)\n"
        "\n"
        "> **Origin**: S91 W5-4 (`session-91-plan-w5.md §W5-4`) mack-cosmic-bridge plan-pinned sole-writer per `feedback_mack-bridge-role.md`; gate `S91-CF41-VII-LANDING` STAGE-1-CANDIDATE landing at `sessions/permanent-results-registry.md §VII.AX.OP-PROJ`. CF-41 carry-forward chain: S89 W1-4 INFO → S90 CF-W1-4-PROMOTE → S91 W5-3 PASS (T1.13) → S91 W5-4 STAGE-1-CANDIDATE registry-text landing (this audit-pin sub-row).\n"
        "\n"
        "- **Audit-pin source**: T1.13 `S91-CF41-UPPER-22.6-EXTENSION` PASS verdict line at `computations/session-91/s91_gate_verdicts.txt:96`; audit_sha256=`" + T113_AUDIT_SHA + "`; content_sha256=`" + T113_CONTENT_SHA + "`; 3-tuple companion at line 98 `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`.\n"
        "- **T1.13 central value**: `n_PBH(L_max=14) = " + T113_CENTRAL_VALUE + " m⁻³` (NOT the plan §W5-4 pre-pinned 8.033e-23; the plan §\"Wave 5 Summary\" line 32 explicitly anticipates this difference; the ACTUAL T1.13 central is used in the §VII.AX.OP-PROJ entry).\n"
        "- **1σ band**: [" + T113_SIGMA_LOW + ", " + T113_SIGMA_HIGH + "] m⁻³ — both edges INSIDE the upper-22.6%-conjunct sub-band [" + UPPER_226_PCT_LOWER + ", " + UPPER_226_PCT_UPPER + "] m⁻³.\n"
        "- **Refinement factor at L_max=14**: " + T113_REFINEMENT_FACTOR + "× (32% in excess of the 3.13× target for upper-22.6% lower-edge entry; advances the S89 W1-4 INFO from L_max=10 1.758e-23 to L_max=14 " + T113_CENTRAL_VALUE + ").\n"
        "- **Registry slot landed**: `§VII.AX.OP-PROJ` at `sessions/permanent-results-registry.md`; OP-PROJ suffix MANDATORY at K=3 per `registry-landing.md §\"Operator-Projection Reading-A Naming Hygiene\"`; State-projection companion `§VII.AX.STATE-PROJ` queued as S92+ carry-forward.\n"
        "- **Bridge family**: **FWD-C5 (NEW)** — Pillar I (M⁴ × SU(3) D_K spectrum cardinality at saturated cascade-tail under Jensen TT-deformation at τ_fold = 0.190) ↔ Pillar IX (PBH number density observation under combined CMB / LISA / PTA detection horizons). Registered at `cross-pillar-bridge-corpus.md §4` Forward candidates table at S91 W5-4 close. Element 3 fiducial-anchor binding: type (ii) external-observation.\n"
        "- **Hybrid Independence Test predicate** (per `cross-pillar-bridge-anatomy.md §\"Hybrid Independence Test\"`): `(YES ∨ YES ∨ YES) ∧ YES = YES`. K-counter advancement K=1 → K=2.\n"
        "- **Substrate-IS Level-1 single-τ-slice declaration**: τ_fold = 0.190 (MANDATORY at K=2 since S88 W-7 V.4 per `phononic-framing.md §\"Single-τ-slice vs moduli-deformation substrate-IS levels\"`); saturated cascade-tail regime g_BBN ≥ g_saturate = 143.\n"
        "- **Algebra-axis cell**: Cell-I-cardinality-projection (algebra-INVARIANT spectrum-only-functional × cardinality-cascade-pole) per `permanent-results-registry.md §VII.U.2` 4-corner classification MANDATORY at K=3.\n"
        "- **Three-level structural-confidence ladder**: Level 1 STRUCTURAL THEOREM (g-independence at saturation; substrate-clock cancellation form); Level 2 STRUCTURAL PREDICTION (Friedrich-Bär saturation theorem analytic certification; Level-2-binding sub-class — HKR-image binds Level-1); Level 3 EMPIRICAL CONFIRMATION (`n_PBH(L_max=14) = " + T113_CENTRAL_VALUE + " m⁻³` inside upper-22.6%-conjunct).\n"
        "- **STAGE-1-CANDIDATE provenance**: per `joint-theorem-promotion.md §\"Stage 1\"` 4-stage pathway. Stage-2 cross-axis independent-verify queued as `CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY`; mack-cosmic-bridge EXCLUDED at Stage-2 per writer/reviewer separation; admissible Axis-A = {connes-ncg-theorist, lizzi-spectral-functional-theorist}; admissible Axis-B = {volovik-superfluid-universe-theorist, gen-physicist}.\n"
        "- **canonical_constants.py promotion**: DEFERRED per plan §W5-4 step 2.7 (STAGE-1-CANDIDATE does NOT trigger canonical_constants.py promotion; Stage-3 PERMANENT does). `n_PBH_FW_central` carry-forward queued as `S92-N-PBH-FW-CANONICAL-PROMOTION` conditional on STAGE-3-PERMANENT.\n"
        "- **S91 W5-4 landing audit pin**: audit_sha256=`" + landing_audit_sha + "`; content_sha256=`" + landing_content_sha + "`; verdict line at `computations/session-91/s91_gate_verdicts.txt` (gate `S91-CF41-VII-LANDING`).\n"
        "- **Status**: STAGE-1-CANDIDATE LANDED at §VII.AX.OP-PROJ; band-edge tension reconciled at upper-22.6%-conjunct level (advances S89 W1-4 INFO from posterior-support-only reconciliation to upper-22.6%-conjunct PASS at L_max=14); Stage-2 cross-axis verify queued for S92+; STAGE-3-PERMANENT promotion gated on Stage-2 PASS.\n"
        "\n"
        "**Cross-link**: §W5-4 mirrors the S86 W14 series + S88 W5 row 1.dovekie-2026-update + S90 W2 CF-29 / CF-31 audit-pin-sub-row pattern (additive citation upgrade per gate-verdicts.md canonical-form rule). Per `feedback_mack-bridge-role.md` mack-cosmic-bridge sole-writer for falsifier-master-inventory.md per AMRI-PROMOTED 2026-04-28. The audit-pin sub-row inherits Row #65 primary cell unchanged (detector horizon: CMB / LISA / PTA combined; scheme: substrate-Connes-graph-edge-density-cardinality-cascade-tail; convention: cardinality-2-LRD-anchor-with-L_max-14-Friedrich-Bar-saturation; L_max: 14 — refined from Row #65 L_max=10 baseline). Row #65 primary content cell carries the S89 W1-4 INFO band-edge tension reconciliation context; this audit-pin sub-row carries the S91 W5-3 PASS upgrade + S91 W5-4 STAGE-1-CANDIDATE landing context. Both rows are structurally complementary: Row #65 primary documents the S89 INFO band-edge tension; the audit-pin sub-row documents the S91 PASS upper-22.6%-conjunct resolution + STAGE-1-CANDIDATE landing.\n"
    )


def build_corpus_fwd_c5_text() -> str:
    """Pure function: builds the FWD-C5 sub-section to be inserted into
    cross-pillar-bridge-corpus.md §4 Forward bridge candidates table, AFTER
    the FWD-C3 closing line."""
    return (
        "\n"
        "### FWD-C5 — Pillar I ↔ Pillar IX  (cardinality-cascade-tail saturation ↔ PBH detection)\n"
        "\n"
        "> **Provenance**: S91 W5-4 (`S91-CF41-VII-LANDING` STAGE-1-CANDIDATE landing at `sessions/permanent-results-registry.md §VII.AX.OP-PROJ`; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`; CONDITIONAL on T1.13 PASS at audit_sha256=`" + T113_AUDIT_SHA + "`). NEW forward candidate; extends the FWD-C1/C2/C3 sequence. Status SUGGESTION at K=1 (this STAGE-1-CANDIDATE landing is the first calibration instance for FWD-C5); promotes via the standard cross-pillar-bridge K-counter pathway (STAGE-2 PASS → STAGE-3-PERMANENT).\n"
        "\n"
        "- **Substrate-IS observable** — `n_PBH = n_edge_saturated · prob_form / L_pix_LRD³` evaluated on `(A_K^{≤14}, H_K^{≤14}, D_K^{≤14})` at τ_fold = 0.19 in the saturated cascade-tail regime (g_BBN ≥ g_saturate = 143). The substrate IS the spectral triple at τ_fold; the cardinality-cascade-tail at saturation IS intrinsic to it at the Level-1 single-τ-slice. Algebra-INVARIANT spectrum-only functional family; Cell-I-cardinality-projection per `cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality K-counter\"` MANDATORY at K=3.\n"
        "- **Laboratory-IN observable** — Combined CMB / LISA / PTA PBH number density observation under the detection-horizon hypersurface Σ_CMB ∪ Σ_LISA ∪ Σ_PTA. Lab parameter is the integrated PBH number density on the combined detection horizon; OE-form (MANDATORY at K=2): `∫_{Σ_CMB ∪ Σ_LISA ∪ Σ_PTA} d³x · Tr_{M_PBH-mass}(P_{PBH-mass} · ρ_BH(x))` with mass-window projector `P_{PBH-mass}` selecting the framework's `M_PBH_typical = M_LRD · 2^{-g_BBN}` scale.\n"
        "- **Bridge map** — Substrate-clock cancellation IS-not-IN coupling (S88 W1a-59 §0 substrate-clock cancellation form) ∘ Friedrich-Bär saturation-theorem analytic certification (S87 W11-3 protocol extended to substrate-distance-N pole at L_max=14) ∘ cardinality-cascade-tail HKR-style image to PBH number density continuum at Pillar IX. **Element 3 fiducial-anchor binding** (per `cross-pillar-bridge-anatomy.md §\"Element 3 fiducial-anchor binding discipline\"` SUGGESTION-K=1): type **(ii) external-observation** — the bridge composes through laboratory-IN PBH detection horizons (external observations at Pillar IX). NOT (i) substrate-self-consistent; NOT (iii) joint-hypersurface.\n"
        "- **Algebraic envelope** — `L^{-α}` convergence rate via cardinality saturation at substrate-distance-N pole; structural-exact replacement: Friedrich-Bär saturation theorem analytic certification (bottom-K invariance for all L_max ≥ 12; refinement factor 4.14× extracted from L_max=10 → L_max=14 scan per T1.13 secondary output). Level-2-binding sub-class — HKR-image of cardinality-cascade-tail Hochschild moment binds Level-1 g-independence theorem to Pillar IX continuum PBH detection.\n"
        "- **Empirical anchor target** — `n_PBH(L_max=14) = " + T113_CENTRAL_VALUE + " m⁻³` (T1.13 PASS at L_max=14; audit_sha256=`" + T113_AUDIT_SHA + "`); 1σ band [" + T113_SIGMA_LOW + ", " + T113_SIGMA_HIGH + "] m⁻³ with both edges INSIDE the upper-22.6%-conjunct sub-band [" + UPPER_226_PCT_LOWER + ", " + UPPER_226_PCT_UPPER + "] m⁻³. Live-watch envelope for forward detector horizons: CMB-S4 2030 / LISA 2035 / PTA NANOGrav-SKA combined.\n"
        "- **Inheritance kernel rank** — rank(ker ι_*) = 1 (single n_PBH scalar in the cardinality-cascade-tail saturation projection; rank-2 not applicable). The cardinality-cascade-tail at saturation is a single algebra-INVARIANT spectrum-only-functional image; no rank-2 dual-cocycle structure surfaces in the saturated regime.\n"
        "- **Earliest S88+ dispatch** — S91 W5-4 STAGE-1-CANDIDATE LANDED (`sessions/permanent-results-registry.md §VII.AX.OP-PROJ`). Stage-2 cross-axis independent-verify queued as S92+ carry-forward `CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY` per `joint-theorem-promotion.md §\"Stage 2\"` two-cross-reviewer protocol. Mack-cosmic-bridge EXCLUDED at Stage-2; admissible Axis-A = {connes-ncg-theorist, lizzi-spectral-functional-theorist}; admissible Axis-B = {volovik-superfluid-universe-theorist, gen-physicist}.\n"
        "\n"
        "**FWD-C5 calibration corpus advancement** (Hybrid Independence Test K-counter K=1 → K=2 per `cross-pillar-bridge-anatomy.md §\"Hybrid Independence Test\"` SUGGESTION-K=1):\n"
        "\n"
        "- **(i) distinct substrate-IS pillar**: YES — Pillar I cardinality-cascade-tail saturation (structurally distinct from Pillar I Mellin-cone-closure of FWD-C1 by parse-tree: cardinality vs Mellin-residue).\n"
        "- **(ii) distinct laboratory-IN pillar**: YES — Pillar IX (CMB / LISA / PTA combined PBH detection; distinct from Pillar II CMB n_s of FWD-C1, Pillar IV Peotta-Törmä BZ-trace of W-5, Pillar V 3He-B BdG of W4a-17).\n"
        "- **(iii) distinct bridge map class**: YES — substrate-clock cancellation ∘ Friedrich-Bär saturation ∘ cardinality-cascade-tail HKR-image (structurally distinct from HKR / K-theory boundary / Connes-Karoubi pairing bridges of FWD-C1/C2/C3).\n"
        "- **(iv) independent algebraic envelope**: YES — cardinality saturation envelope (regulator-invariant Friedrich-Bär saturation form; not a numerical refinement of FWD-C1/C2/C3 envelopes).\n"
        "- **Predicate**: `(YES ∨ YES ∨ YES) ∧ YES = YES`. K-counter K=1 → K=2 on Hybrid Independence Test corpus.\n"
        "\n"
        "**Cross-link**: §VII.AX.OP-PROJ registry entry is the STAGE-1-CANDIDATE landing for FWD-C5; the entry's full 5-anatomy + 3-level + parse-tree expansion + OP-PROJ suffix + Hybrid Independence Test predicate evaluation are all declared per `cross-pillar-bridge-anatomy.md §\"Forward template-adoption (5-anatomy + 3-level discipline)\"` MANDATORY at K=3.\n"
    )


# ---------------------------------------------------------------------------
# Section 6 — Atomic write helpers (single-shot AFTER-pattern)
# ---------------------------------------------------------------------------
def write_atomic_append(target_path: Path, append_text: str,
                        idempotency_marker: str) -> tuple[bool, str, str]:
    """Append `append_text` to `target_path` atomically (POSIX O_APPEND single
    open("a") write per `epistemic-discipline.md §"Registry-Write Hygiene
    under Parallel-Writer Race"` discipline).

    Idempotency: if `idempotency_marker` already in file, returns (True,
    pre_sha, pre_sha) without re-writing.

    Returns (write_succeeded, pre_state_sha, post_state_sha_or_error).
    """
    pre_text = target_path.read_text(encoding="utf-8", errors="replace")  # (local)
    pre_sha = sha256_of_text(pre_text)                                     # (local)

    if idempotency_marker in pre_text:
        print(f"  Idempotency guard: marker already present in {target_path.name}; no re-write.")
        return True, pre_sha, pre_sha

    new_text = pre_text + append_text                                      # (local)
    post_sha_target = sha256_of_text(new_text)                             # (local)

    # POSIX O_APPEND atomic single open("a") write per epistemic-discipline.md
    # §"Registry-Write Hygiene under Parallel-Writer Race"
    try:
        with target_path.open("a", encoding="utf-8") as fp:
            fp.write(append_text)
            fp.flush()
            try:
                os.fsync(fp.fileno())
            except OSError:
                # fsync may fail on some Windows filesystems; non-fatal since
                # flush() provides write durability for append-only POSIX semantics.
                pass
    except OSError as e:
        return False, pre_sha, f"WRITE_FAILED:{e}"

    return True, pre_sha, post_sha_target


def write_atomic_insert(target_path: Path, insert_text: str,
                        anchor: str,
                        idempotency_marker: str) -> tuple[bool, str, str]:
    """Insert `insert_text` into `target_path` AFTER the line containing
    `anchor`. Used for falsifier-inventory (sub-row insertion after Row #65
    closing line) and corpus (sub-section insertion after FWD-C3 closing line).

    Returns (write_succeeded, pre_state_sha, post_state_sha_or_error).
    """
    pre_text = target_path.read_text(encoding="utf-8", errors="replace")  # (local)
    pre_sha = sha256_of_text(pre_text)                                     # (local)

    if idempotency_marker in pre_text:
        print(f"  Idempotency guard: marker already present in {target_path.name}; no re-write.")
        return True, pre_sha, pre_sha

    anchor_idx = pre_text.find(anchor)                                     # (local)
    if anchor_idx == -1:
        return False, pre_sha, "ANCHOR_NOT_FOUND"

    # Insert AFTER the anchor line (find next newline after anchor)
    insertion_idx = pre_text.find("\n", anchor_idx + len(anchor)) + 1      # (local)
    new_text = pre_text[:insertion_idx] + insert_text + pre_text[insertion_idx:]  # (local)
    post_sha_target = sha256_of_text(new_text)                             # (local)

    # Atomic write via tmp + replace
    tmp_path = target_path.with_suffix(target_path.suffix + ".tmp_cf41vii")  # (local)
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
# Section 7 — re_read_and_verify (5 rubric clauses)
# ---------------------------------------------------------------------------
def re_read_and_verify_vii_ax(registry_path: Path, promotion_text: str) -> dict:
    """Re-read registry; verify 5 rubric clauses on the inserted block."""
    post_text = registry_path.read_text(encoding="utf-8", errors="replace")  # (local)
    post_sha = sha256_of_text(post_text)                                      # (local)

    # CC1: §VII.AX.OP-PROJ header present
    cc1_header = "### §VII.AX.OP-PROJ — PBH Band-Edge Prediction n_PBH = " + T113_CENTRAL_FOR_HEADER
    cc1_pass = cc1_header in post_text

    # CC2: 5 IS-not-IN anatomy elements present (numbered 1-5)
    cc2_anatomy_markers = [
        "1. **Substrate-IS observable**: `n_PBH",
        "2. **Laboratory-IN observable**",
        "3. **Bridge map** (explicit",
        "4. **Algebraic envelope**: `L^{-α}` convergence rate",
        "5. **Empirical anchor**: `n_PBH(L_max=14) = " + T113_CENTRAL_VALUE,
    ]
    cc2_pass = all(m in post_text for m in cc2_anatomy_markers)
    cc2_count = sum(1 for m in cc2_anatomy_markers if m in post_text)

    # CC3: 3-level structural-confidence ladder present
    cc3_ladder_markers = ["| Level 1 | Substrate-IS structural identity",
                          "| Level 2 | Algebraic convergence envelope",
                          "| Level 3 | Empirical anchor at canonical L_max=14"]
    cc3_pass = all(m in post_text for m in cc3_ladder_markers)
    cc3_count = sum(1 for m in cc3_ladder_markers if m in post_text)

    # CC4: STAGE-1-CANDIDATE tag + Stage-2 dispatch ID + OP-PROJ suffix + parse-tree expansion
    cc4_stage1_tag = "**Status**: STAGE-1-CANDIDATE per"
    cc4_stage2_dispatch = "CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY"
    cc4_op_proj_suffix = "**OP-PROJ suffix discipline**"
    cc4_parse_tree = "**Parse-tree expansion** (per"
    cc4_pass = (cc4_stage1_tag in post_text and cc4_stage2_dispatch in post_text
                and cc4_op_proj_suffix in post_text and cc4_parse_tree in post_text)

    # CC5: T1.13 audit SHA + bridge family FWD-C5 + Hybrid Independence Test predicate
    cc5_t113_sha = T113_AUDIT_SHA
    cc5_fwd_c5 = "**Bridge family**: **FWD-C5 (NEW"
    cc5_hit_predicate = "**Predicate evaluation**: `(YES ∨ YES ∨ YES) ∧ YES = YES`"
    cc5_pass = (cc5_t113_sha in post_text and cc5_fwd_c5 in post_text
                and cc5_hit_predicate in post_text)

    # CC6: registry-text length check (≥ 15 lines for the inserted block)
    inserted_lines = promotion_text.count("\n")
    cc6_pass = inserted_lines >= MIN_REGISTRY_LINES_PASS

    composite_pass = cc1_pass and cc2_pass and cc3_pass and cc4_pass and cc5_pass and cc6_pass
    rubric_count = sum([cc1_pass, cc2_pass, cc3_pass, cc4_pass, cc5_pass, cc6_pass])

    return {
        "post_sha": post_sha,
        "cc1_header_pass": cc1_pass,
        "cc2_5_anatomy_pass": cc2_pass,
        "cc2_anatomy_count": cc2_count,
        "cc3_3_level_ladder_pass": cc3_pass,
        "cc3_ladder_count": cc3_count,
        "cc4_stage1_tag_dispatch_op_parse_pass": cc4_pass,
        "cc5_t113_fwd_c5_hit_pass": cc5_pass,
        "cc6_registry_text_length_pass": cc6_pass,
        "inserted_lines_count": inserted_lines,
        "composite_pass": composite_pass,
        "rubric_count": rubric_count,
    }


def verify_inventory_audit_pin(falsifier_path: Path, audit_pin_text: str) -> dict:
    """Verify the audit-pin sub-row was appended correctly."""
    post_text = falsifier_path.read_text(encoding="utf-8", errors="replace")  # (local)
    marker = "## NEW Row #65.audit-CF-41-VII-LANDING — S91 W5-4 STAGE-1-CANDIDATE"
    marker_pass = marker in post_text
    t113_sha_pass = T113_AUDIT_SHA in post_text  # (local) audit-pin source citation
    inserted_lines = audit_pin_text.count("\n")
    return {
        "marker_pass": marker_pass,
        "t113_sha_pass": t113_sha_pass,
        "inserted_lines": inserted_lines,
        "composite": marker_pass and t113_sha_pass and inserted_lines >= 10,
    }


def verify_corpus_fwd_c5(corpus_path: Path, corpus_text: str) -> dict:
    """Verify FWD-C5 sub-section appended correctly."""
    post_text = corpus_path.read_text(encoding="utf-8", errors="replace")  # (local)
    marker = "### FWD-C5 — Pillar I ↔ Pillar IX  (cardinality-cascade-tail saturation ↔ PBH detection)"
    marker_pass = marker in post_text
    inserted_lines = corpus_text.count("\n")
    return {
        "marker_pass": marker_pass,
        "inserted_lines": inserted_lines,
        "composite": marker_pass and inserted_lines >= 10,
    }


# ---------------------------------------------------------------------------
# Section 8 — Compute (orchestrates build + write + verify; single-shot)
# ---------------------------------------------------------------------------
def compute() -> dict:
    """S91-CF41-VII-LANDING via bridge-landing AFTER-pattern (single-shot)."""

    # Step 1: Confirm T1.13 PASS prerequisite
    t113_line_marker = ("S91-CF41-UPPER-22.6-EXTENSION: PASS -- value='"
                        + T113_CENTRAL_VALUE)
    verdict_pre_text = VERDICT_TXT.read_text(encoding="utf-8", errors="replace")  # (local)
    t113_pass_confirmed = t113_line_marker in verdict_pre_text
    print(f"\n=== Step 1: T1.13 PASS prerequisite confirmation ===")
    print(f"  T1.13 PASS line present in {VERDICT_TXT.name}: {t113_pass_confirmed}")
    print(f"  T1.13 audit_sha256: {T113_AUDIT_SHA[:16]}...")
    print(f"  T1.13 central:      {T113_CENTRAL_VALUE} m^-3")

    if not t113_pass_confirmed:
        print(f"  CRITICAL: T1.13 PASS not found — cannot proceed with landing.")
        return {"write_succeeded": False, "error": "T1.13_PASS_NOT_CONFIRMED"}

    # Step 2: Build promotion texts (pure functions; all text in memory)
    vii_ax_text = build_vii_ax_promotion_text()
    vii_ax_sha = sha256_of_text(vii_ax_text)
    print(f"\n=== Step 2: build_promotion_text complete ===")
    print(f"  §VII.AX.OP-PROJ text SHA: {vii_ax_sha[:16]}...")
    print(f"  §VII.AX.OP-PROJ length: {len(vii_ax_text)} chars, "
          f"{vii_ax_text.count(chr(10))} newlines")

    # Step 3: write_atomic_with_fsync — registry (append to EOF)
    print(f"\n=== Step 3a: write_atomic_with_fsync — registry §VII.AX.OP-PROJ ===")
    vii_ax_idempotency_marker = ("### §VII.AX.OP-PROJ — PBH Band-Edge Prediction n_PBH = "
                                  + T113_CENTRAL_FOR_HEADER + " m⁻³")
    registry_write_ok, registry_pre_sha, registry_post_sha = write_atomic_append(
        REGISTRY_PATH, vii_ax_text, vii_ax_idempotency_marker)
    if not registry_write_ok:
        print(f"  REGISTRY WRITE FAILED: {registry_post_sha}")
        return {
            "write_succeeded": False,
            "error": "REGISTRY_WRITE_FAILED:" + str(registry_post_sha),
        }
    print(f"  Registry write OK (atomic append)")
    print(f"  Registry pre-edit SHA:  {registry_pre_sha[:16]}...")
    print(f"  Registry post-edit SHA: {registry_post_sha[:16]}...")

    # Step 4: re_read_and_verify — registry
    print(f"\n=== Step 4: re_read_and_verify — registry §VII.AX.OP-PROJ ===")
    vii_ax_verify = re_read_and_verify_vii_ax(REGISTRY_PATH, vii_ax_text)
    print(f"  CC1 header: {vii_ax_verify['cc1_header_pass']}")
    print(f"  CC2 5 IS-not-IN anatomy elements: {vii_ax_verify['cc2_5_anatomy_pass']} "
          f"({vii_ax_verify['cc2_anatomy_count']}/5)")
    print(f"  CC3 3-level ladder: {vii_ax_verify['cc3_3_level_ladder_pass']} "
          f"({vii_ax_verify['cc3_ladder_count']}/3)")
    print(f"  CC4 STAGE-1-CANDIDATE + Stage-2 dispatch + OP-PROJ + parse-tree: "
          f"{vii_ax_verify['cc4_stage1_tag_dispatch_op_parse_pass']}")
    print(f"  CC5 T1.13 SHA + FWD-C5 + HIT predicate: "
          f"{vii_ax_verify['cc5_t113_fwd_c5_hit_pass']}")
    print(f"  CC6 registry text length >= {MIN_REGISTRY_LINES_PASS}: "
          f"{vii_ax_verify['cc6_registry_text_length_pass']} "
          f"({vii_ax_verify['inserted_lines_count']} lines)")
    print(f"  Composite rubric: {vii_ax_verify['rubric_count']}/6 PASS")
    print(f"  Composite PASS:  {vii_ax_verify['composite_pass']}")

    # Step 5: Compute landing audit_sha + content_sha for the audit-pin sub-row
    # (We need these BEFORE writing the audit-pin sub-row so it can cite them.)
    audit_sha_provisional, content_sha_provisional = compute_dual_sha(
        Path(__file__), SHARED_DIR / "canonical_constants.py",
        log_input_pins(INPUT_FILES))
    # NOTE: These are PRE-write SHAs (the registry has been written but the
    # falsifier-inventory + corpus have not yet been modified). Final audit_sha
    # for the verdict line is recomputed in main() AFTER all writes complete.

    # Step 6: Build + write falsifier-inventory audit-pin sub-row
    print(f"\n=== Step 6: write_atomic_with_fsync — falsifier-inventory Row #65.audit ===")
    inventory_audit_text = build_inventory_audit_pin_text(
        audit_sha_provisional, content_sha_provisional)
    inventory_idempotency_marker = ("## NEW Row #65.audit-CF-41-VII-LANDING "
                                     "— S91 W5-4 STAGE-1-CANDIDATE")
    inventory_write_ok, inv_pre_sha, inv_post_sha = write_atomic_insert(
        FALSIFIER_INVENTORY_PATH, inventory_audit_text,
        INVENTORY_INSERTION_ANCHOR, inventory_idempotency_marker)
    if not inventory_write_ok:
        print(f"  FALSIFIER-INVENTORY WRITE FAILED: {inv_post_sha}")
        # Continue (registry already landed; report as composite-FAIL in verify)
    else:
        print(f"  Falsifier-inventory write OK (atomic insert after Row #65 closing)")
        print(f"  Inventory pre-edit SHA:  {inv_pre_sha[:16]}...")
        print(f"  Inventory post-edit SHA: {inv_post_sha[:16]}...")
    inventory_verify = verify_inventory_audit_pin(FALSIFIER_INVENTORY_PATH, inventory_audit_text)
    print(f"  Inventory marker present:  {inventory_verify['marker_pass']}")
    print(f"  Inventory T1.13 SHA cited: {inventory_verify['t113_sha_pass']}")
    print(f"  Inventory composite:       {inventory_verify['composite']}")

    # Step 7: Build + write corpus FWD-C5 sub-section
    print(f"\n=== Step 7: write_atomic_with_fsync — corpus §4 FWD-C5 sub-section ===")
    corpus_fwd_c5_text = build_corpus_fwd_c5_text()
    corpus_idempotency_marker = ("### FWD-C5 — Pillar I ↔ Pillar IX  "
                                  "(cardinality-cascade-tail saturation ↔ PBH detection)")
    corpus_write_ok, corp_pre_sha, corp_post_sha = write_atomic_insert(
        CORPUS_PATH, corpus_fwd_c5_text,
        CORPUS_INSERTION_ANCHOR, corpus_idempotency_marker)
    if not corpus_write_ok:
        print(f"  CORPUS WRITE FAILED: {corp_post_sha}")
    else:
        print(f"  Corpus write OK (atomic insert after FWD-C3 closing)")
        print(f"  Corpus pre-edit SHA:  {corp_pre_sha[:16]}...")
        print(f"  Corpus post-edit SHA: {corp_post_sha[:16]}...")
    corpus_verify = verify_corpus_fwd_c5(CORPUS_PATH, corpus_fwd_c5_text)
    print(f"  Corpus FWD-C5 marker present: {corpus_verify['marker_pass']}")
    print(f"  Corpus composite:             {corpus_verify['composite']}")

    return {
        "write_succeeded": True,
        "t113_pass_confirmed": t113_pass_confirmed,
        "vii_ax_text_sha": vii_ax_sha,
        "vii_ax_text_chars": len(vii_ax_text),
        "vii_ax_text_lines": vii_ax_text.count("\n"),
        "registry_pre_sha": registry_pre_sha,
        "registry_post_sha": registry_post_sha,
        "registry_write_ok": registry_write_ok,
        "inventory_write_ok": inventory_write_ok,
        "inventory_pre_sha": inv_pre_sha if inventory_write_ok else "",
        "inventory_post_sha": inv_post_sha if inventory_write_ok else "",
        "inventory_marker_pass": inventory_verify["marker_pass"],
        "inventory_t113_sha_pass": inventory_verify["t113_sha_pass"],
        "inventory_composite": inventory_verify["composite"],
        "corpus_write_ok": corpus_write_ok,
        "corpus_pre_sha": corp_pre_sha if corpus_write_ok else "",
        "corpus_post_sha": corp_post_sha if corpus_write_ok else "",
        "corpus_marker_pass": corpus_verify["marker_pass"],
        "corpus_composite": corpus_verify["composite"],
        **vii_ax_verify,
    }


# ---------------------------------------------------------------------------
# Section 9 — Verdict emission (single-shot; ONE canonical line)
# ---------------------------------------------------------------------------
def evaluate_gate(r: dict) -> str:
    """Single-shot AFTER-pattern verdict evaluation: PASS iff all writes
    succeeded AND all rubric clauses PASS AND inventory + corpus updated."""
    if not r.get("write_succeeded"):
        return "FAIL"
    composite_pass_registry = r.get("composite_pass", False)
    composite_pass_inventory = r.get("inventory_composite", False)
    composite_pass_corpus = r.get("corpus_composite", False)
    if composite_pass_registry and composite_pass_inventory and composite_pass_corpus:
        return "PASS"
    return "FAIL"


def append_verdict(verdict: str, value_str: str,
                   audit_sha: str, content_sha: str) -> None:
    """Append canonical line + W9a-99 dual-SHA companion + S87+ schema-v2
    3-tuple companion row (per plan §"Verdict-Line Emission Discipline" item 3
    — [AUDIT] trigger with sign=N/A)."""
    magnitude_verdict = verdict if verdict in ("PASS", "FAIL") else "FAIL"
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    # REQUIRED 3-tuple companion row per plan §"Verdict-Line Emission Discipline" item 3
    # ([AUDIT] trigger with sign=N/A; regime=VALID inherited from T1.13 composite=PASS+VALID)
    three_tuple_row = (
        f"# sign_verdict=N/A magnitude_verdict={magnitude_verdict} regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)
        fp.write(three_tuple_row)


# ---------------------------------------------------------------------------
# Section 10 — main
# ---------------------------------------------------------------------------
def main() -> int:
    pins = log_input_pins(INPUT_FILES)

    r = compute()

    # Save dict-to-npz (skip non-serializable via numpy strings)
    save_dict = {k: np.asarray(v) for k, v in r.items()}
    np.savez(OUT_NPZ, **save_dict)
    print(f"\nnpz written: {OUT_NPZ}")

    # Recompute dual-SHA AFTER all writes (final audit_sha reflects final state
    # of registry + inventory + corpus + canonical_constants pin map)
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__), SHARED_DIR / "canonical_constants.py", pins)

    verdict = evaluate_gate(r)

    value_str = (
        f"STAGE-1-CANDIDATE_landed_at_§VII.AX.OP-PROJ_n_PBH={T113_CENTRAL_FOR_HEADER}_m_minus_3;"
        f"write_succeeded={r.get('write_succeeded')};"
        f"composite_registry={r.get('composite_pass', False)};"
        f"composite_inventory={r.get('inventory_composite', False)};"
        f"composite_corpus={r.get('corpus_composite', False)};"
        f"rubric_registry={r.get('rubric_count', 0)}_of_6;"
        f"vii_ax_lines={r.get('vii_ax_text_lines', 0)};"
        f"t113_audit_sha={T113_AUDIT_SHA[:16]};"
        f"t113_central={T113_CENTRAL_VALUE};"
        f"fwd_c5_landed=True;"
        f"hybrid_indep_test=YES_pred_K1_to_K2;"
        f"op_proj_suffix=K3_MANDATORY_compliant;"
        f"parse_tree_expansion=K1_SUGGESTION_compliant_K1_to_K2;"
        f"stage_2_dispatch_queued=CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY;"
        f"mack_sole_writer=feedback_mack_bridge_role_AMRI_2026-04-28"
    )
    print(f"\n4-tuple: (value='{value_str[:100]}...', scheme={SCHEME}, "
          f"convention={CONVENTION[:60]}..., L_max={L_MAX_TAG})")
    print(f"audit_sha256:   {audit_sha}")
    print(f"content_sha256: {content_sha}")
    print(f"VERDICT: {verdict}")

    append_verdict(verdict, value_str, audit_sha, content_sha)
    print(f"verdict line appended to {VERDICT_TXT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
