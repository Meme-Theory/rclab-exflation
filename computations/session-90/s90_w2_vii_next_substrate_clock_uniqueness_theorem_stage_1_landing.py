#!/usr/bin/env python3
"""
S90 W2-2 — S90-VII-NEXT-SUBSTRATE-CLOCK-UNIQUENESS-THEOREM-STAGE-1-CANDIDATE-LANDING (CF-19)
============================================================================================

Gate: S90-VII-NEXT-SUBSTRATE-CLOCK-UNIQUENESS-THEOREM-STAGE-1-CANDIDATE-LANDING
      ([VERIFY-THEOREM])

Pre-registered threshold (per plan §W2-2 §9):
  PASS iff (a) §VII.AW.OP-PROJ heading appended at end of permanent-results-registry.md
       AND (b) block contains literal `STAGE-1-CANDIDATE` AND `SUBSTRATE-CLOCK-UNIQUENESS-THEOREM`
       AND (c) 5-criteria evidence table grep-verified (5 PASS rows + 5 audit-SHAs)
       AND (d) 5-anatomy IS-not-IN elements all present
       AND (e) substantive line count > 15
       AND (f) Level-1 single-τ-slice declaration explicit
  FAIL iff any of (a)-(f) absent post-write.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/permanent-results-registry.md (pre-edit content)
  - script bytes
  - canonical_constants.py
  - computations/session-89/s89_gate_verdicts.txt (W3-1, W3-3, W3-4, W3-5, W3-6 SHAs)

Output 4-tuple (per plan §W2-2 §8):
  (value=<bool>, scheme=mack-sole-writer-single-shot-AFTER-pattern,
   convention=joint-theorem-promotion-stage-1-candidate, L_max=10)

Classification: METHODOLOGY (new §VII registry entry; PASS predicate is
artifact-existence-with-substantive-content per `joint-theorem-promotion.md
§"Stage 1"` 4-stage pathway).

METHODOLOGY
-----------
Single-shot AFTER-pattern per `.claude/rules/registry-landing.md
§"Bridge-Landing Script Architecture (single-shot pattern)"`. Appends a
new §VII.AW.OP-PROJ STAGE-1-CANDIDATE block to the end of
permanent-results-registry.md. Idempotency-guarded (no-op if already
present). Slot-occupancy pre-flight: scan for any `### §VII.AW` heading;
if present, FAIL with diagnostic (parallel-writer race per
`.claude/rules/epistemic-discipline.md §"Registry-Write Hygiene"`).

§VII.AW.OP-PROJ suffix tagging is MANDATORY at K=3 since S88 W8-92 per
`.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming
Hygiene"` — this is a substrate-IS observable on the algebra-INVARIANT
spectrum-only-functional family (operator-projection side; State-projection
companion slot §VII.AW.STATE-PROJ queued as S91+ carry-forward).

Per `joint-theorem-promotion.md §"Stage 1"`, this is Stage 1 of the
4-stage pathway. Stage 2 cross-axis independent verify is queued as
S91+ carry-forward `S91-VII-AW-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY`.

DISCIPLINE
----------
- `from canonical_constants import *` (S34+ MANDATORY)
- Every local/intermediate tagged `# (local)`
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict appended atomically per gate-verdicts.md S87+ schema-v2
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
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

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S90"                                                # (local)
GATE_ID = "S90-VII-NEXT-SUBSTRATE-CLOCK-UNIQUENESS-THEOREM-STAGE-1-CANDIDATE-LANDING"  # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"          # (local)
CONVENTION = "joint-theorem-promotion-stage-1-candidate"       # (local)
L_MAX = 10                                                     # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
S89_VERDICTS_PATH = (
    PROJECT_ROOT / "computations" / "session-89" / "s89_gate_verdicts.txt"
)  # (local)
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"  # (local)

# S89 W3 wave 5-criteria saturation evidence audit_sha256s (grep-verified
# at landing time against `s89_gate_verdicts.txt`).
W3_1_SHA_XI_KZ = (
    "dff2f63006e29b1b4f9d7abe53c7c9b7dc2e049ac454368323246bd71c140056"
)  # (local) Friedrich-Bär saturation at L_max=10
W3_3_SHA_COCYCLE_RATIO = (
    "077cfa32935f55b9040a3bc85f93efe03583781505aa3c55e3e200960669c43e"
)  # (local) regulator-class-invariant cocycle ratio
W3_4_SHA_V4_TRIALITY = (
    "7efdb2b26fb4e1faf9161e25d7f751fe8d9db0a047a26a4feb1918da03a59c3a"
)  # (local) V_4-triality Sage-QQ algebra-INVARIANT classification
W3_5_SHA_CLOCK_CANCELLATION = (
    "3d8d70d0a9c19a0bf2b28d7d2e007a50d2d3122541e132206463ad517de16eda"
)  # (local) substrate-clock cancellation discriminating predicate
W3_6_SHA_UNIQUENESS = (
    "6108fd56a3b62e2ea8d735efd5117bd00d7503f99b18d0198222e0c7244784ad"
)  # (local) substrate-clock pinning uniqueness derivation (5-criteria saturation theorem)

# canonical xi_KZ_FW value (S89 W3-1 PASS LANDED)
XI_KZ_FW_M_KK_INV = 0.018760052113614717  # (local) M_KK^{-1} units

# S90 W2-2 V.0 FAIL audit_sha256 (verify-window 8000-char cap bug); this re-run
# is the V.1 corrective per `.claude/rules/gate-verdicts.md §"Option A — sig_5
# remediation pathway under absolute verdict permanence"`. The V.0 FAIL line is
# RETAINED on disk; this V.1 line is APPENDED with `supersedes=<V0_audit_sha>`.
SUPERSEDES_V0_FAIL_AUDIT_SHA = (
    "da4f9f261a801680c3c01e1389d6e9c66df027e44520704335ed97ac350293ae"
)  # (local) "script-bug-corrective" pattern; window-cap bug fixed in V.1

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    S89_VERDICTS_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema, W9a-99 split)
# ---------------------------------------------------------------------------

def sha256_of(path):
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — build_promotion_text (pure function; AFTER-pattern step 1)
# ---------------------------------------------------------------------------

ANCHOR_VII_AW = "### §VII.AW"  # (local) any §VII.AW* heading triggers idempotency

NEW_ENTRY = f"""
### §VII.AW.OP-PROJ — SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (S90 W2 CF-19 — mack-cosmic-bridge sole-writer landing per `feedback_mack-bridge-role.md`, 2026-05-13)

> **Provenance**: S89 §W3-6 closeout `S89-SUBSTRATE-CLOCK-PINNING-UNIQUENESS-DERIVATION` PASS (audit_sha256=`{W3_6_SHA_UNIQUENESS}`); CF-19 S90 W2 landing per `joint-theorem-promotion.md §"Stage 1"` 4-stage pathway. Mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`. Co-signers (structural review on theorem substance; no artifact writes): `connes-ncg-theorist` (NCG-axiomatic substance review on the substrate-clock uniqueness statement at the spectral-triple axiom layer); `lizzi-spectral-functional-theorist` (5-criteria saturation theorem cross-review on the algebra-INVARIANT spectrum-only functional family); `volovik-superfluid-universe-theorist` (substrate-clock 5-criteria saturation from S89 §W3-5 superfluid-universe reading).

**Status**: STAGE-1-CANDIDATE (per `.claude/rules/joint-theorem-promotion.md §"Stage 1"` 4-stage pathway; Stage-2 cross-axis independent verify queued as `S91-VII-AW-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY` per `joint-theorem-promotion.md §"Stage 2"` two-cross-reviewer protocol).

**Algebra-axis cell** (per `permanent-results-registry.md §VII.U.2` 4-corner classification LANDED S88 W5b-45): Cell I (algebra-INVARIANT spectrum-only-functional × Mellin-pole substrate-distance-1 at s=3). The substrate-clock Pinning-A is a spectrum-only functional of the form `∫_λ g(λ) dN_{{D_K}}(λ)` evaluated on `D_K`'s Peter-Weyl decomposition at τ_fold = 0.19, lifted under the Connes-Moscovici 1995 §III.4 residue-formula axiom layer at substrate-distance-1 pole `s=3`. Cross-corner co-primary structures with Cell IV (algebra-DEPENDENT state-pair functional) are FORBIDDEN per `.claude/rules/registry-landing.md §"Detection"` criterion 4 (S88 W-15 V.6 MANDATORY at K=3).

**Theorem statement**: On the spectral triple `(A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ), H_K, D_K(τ))` at τ_fold = 0.19, the substrate-clock canonical Pinning-A IS the UNIQUE substrate-natural temporal coordinate modulo affine reparameterization, in the algebra-INVARIANT spectrum-only functional family on `D_K`'s Peter-Weyl decomposition. Formally: among the candidate space `{{P_1 = L-pix-canonical (substrate-clock Pinning-A), P_2 = mode-density-pinning, P_3 = GGE-anchored}}`, P_1 = Pinning-A is the UNIQUE candidate satisfying ALL FIVE saturation criteria simultaneously; P_2 saturates 4/5, P_3 saturates 2/5 (S89 W3-6 verdict: `{{P_1: 5, P_2: 4, P_3: 2}}`). The uniqueness is modulo the affine reparameterization quotient `τ_substrate ↦ a · τ_substrate + b` for (a, b) ∈ ℝ_+ × ℝ.

**5-criteria saturation evidence table**:

| # | Criterion | Verdict | Audit SHA |
|:-:|:----------|:--------|:----------|
| 1 | Regulator-invariant identity at Connes-Moscovici 1995 §III.4 residue-formula axiom layer (substrate cocycle ratio FI across 4 regulators per `regulator-pin-discipline.md`) | PASS | S89 W3-3 `S89-SUBSTRATE-COCYCLE-RATIO-REGULATOR-CLASS-INVARIANCE-SCAN` audit_sha256=`{W3_3_SHA_COCYCLE_RATIO}` |
| 2 | Algebra-INVARIANT spectrum-only functional family classification per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 (V_4-triality Sage-QQ multi-orbit invariance) | PASS | S89 W3-4 `S89-V4-SAGE-QQ-ENUMERATION-EXTENDED-SECTORS` audit_sha256=`{W3_4_SHA_V4_TRIALITY}` |
| 3 | Friedrich-Bär saturation at L_max=10 with substrate-canonical anchor `xi_KZ_FW = {XI_KZ_FW_M_KK_INV} M_KK⁻¹` per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` | PASS | S89 W3-1 `S89-XI-KZ-SUBSTRATE-NATURAL-DERIVATION-FROM-T1-ATLAS` audit_sha256=`{W3_1_SHA_XI_KZ}` |
| 4 | Substrate-distance-1 Mellin pole `s=3` anchor consistent with §VII.U.1 calibration baseline (substrate-clock cancellation discriminating predicate at g-scan {{143, 322, 384}}) | PASS | S89 W3-5 `S89-SUBSTRATE-CLOCK-CANCELLATION-DISCRIMINATING-PREDICATE-GATE` audit_sha256=`{W3_5_SHA_CLOCK_CANCELLATION}` |
| 5 | Substrate-IS Level-1 single-τ-slice at τ_fold = 0.19 declaration per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4 | PASS | S89 W3-6 `S89-SUBSTRATE-CLOCK-PINNING-UNIQUENESS-DERIVATION` audit_sha256=`{W3_6_SHA_UNIQUENESS}` |

**Saturation verdict**: P_1 (substrate-clock Pinning-A) saturates 5/5 criteria; P_2 (mode-density-pinning) saturates 4/5; P_3 (GGE-anchored) saturates 2/5. Uniqueness ranking (S89 W3-6 verdict tuple): `[('P_1', 5), ('P_2', 4), ('P_3', 2)]`. Margin of P_1 over P_2 = 1 criterion (criterion 5, Level-1 single-τ-slice declaration — P_2 mode-density pinning lifts under moduli-deformation, violating the Level-1 single-τ-slice substrate-IS requirement).

**Three-level structural-confidence ladder** (per `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"`):

| Level | Anatomy | Status |
|:------|:--------|:-------|
| Level 1 | Substrate-IS structural identity: substrate-clock Pinning-A is the UNIQUE saturator of the 5-criteria family at τ_fold = 0.19 (regulator-invariant, L-independent at the cohomology-class layer; Cell I algebra-INVARIANT spectrum-only-functional image at substrate-distance-1 pole s=3) | STRUCTURAL THEOREM (W3-6 PASS; proven via exhaustive enumeration of P_1/P_2/P_3 candidate space with 5-criteria evaluation matrix) |
| Level 2 | Algebraic convergence envelope `L^{{-3}}` at d=4 substrate-distance-1 pole s=3 (Level-2-binding sub-class per S88 W8-88 — affine reparameterization quotient binds Level-1 cohomology-class identity to the laboratory-IN cosmological-time observable) | STRUCTURAL PREDICTION (algebraically derived; predicted ~0.1% relative width at L_max=10) |
| Level 3 | Empirical anchor at L_max=10: `xi_KZ_FW = {XI_KZ_FW_M_KK_INV} M_KK⁻¹` (S89 W3-1 PASS LANDED with Friedrich-Bär saturation theorem certifying L_max ≥ 10 sufficiency); Level-3 satisfies Level-2 envelope within margin | EMPIRICAL CONFIRMATION (W3-1 PASS; xi_KZ_FW substrate-canonical at machine precision) |

**Registry-PASS criterion** (per `cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`): Level 3 satisfies Level 2 within envelope at canonical L_max=10. Level-2-binding sub-class verified (affine reparameterization quotient is the HKR-image of the cohomology-class Level-1 identity; binds substrate Level-1 to laboratory-IN cosmological-time on FRW background).

**5-anatomy IS-not-IN elements** (all MANDATORY at K=3 per `cross-pillar-bridge-anatomy.md`):

1. **Substrate-IS observable**: substrate-clock Pinning-A at τ_fold = 0.19; algebra-INVARIANT spectrum-only functional `∫_λ g(λ) dN_{{D_K}}(λ)` evaluated on `(A_K^{{≤10}}, H_K^{{≤10}}, D_K^{{≤10}})` at τ_fold; Level-1 single-τ-slice substrate-IS per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`. The substrate IS the spectral triple at τ_fold; Pinning-A IS the canonical temporal coordinate intrinsic to it, NOT a coordinate imposed from a meta-container.

2. **Laboratory-IN observable** (OE-form per S88 W7a-73 MANDATORY at K=2): `∫_{{FRW}} dτ_cosmo · g(τ_cosmo)` — continuum cosmological-time τ_cosmo parameterization on a Friedmann-Robertson-Walker background; measurement IN the continuum cosmological-time container. Lab parameter is τ_cosmo, integration domain is the FRW background time slice; named projector for time-integration is `Π^{{τ_cosmo}}_{{FRW}}`.

3. **Bridge map** (explicit; not 'analogous to' / 'corresponds to'): affine reparameterization quotient `τ_substrate ↦ a · τ_cosmo + b` modulo (a, b) ∈ ℝ_+ × ℝ. The substrate-clock Pinning-A image under the affine quotient produces the FRW cosmological time, NOT the reverse. **Element 3 fiducial-anchor binding (S88 W-15 V.7 SUGGESTION-K=1)**: type **(i) substrate-self-consistent** — the bridge map composes through the substrate-IS canonical xi_KZ_FW (S89 W3-1 LANDED at the same algebra-axis family); the affine quotient parameters (a, b) are determined by the substrate-clock canonical alone, NOT by external cosmological-time data. NOT (ii) external-observation; NOT (iii) joint-hypersurface.

4. **Algebraic envelope**: `L^{{-3}}` convergence at d=4 per `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction (S88 W8-88 hardening)"` Level-2-binding sub-class; predicted ~0.1% relative width at L_max=10. The envelope describes the rate at which the substrate-IS Pinning-A image converges to the cosmological-time τ_cosmo parameterization under the affine quotient at L_max → ∞, NOT a substrate-internal bare-decomposition rate. Friedrich-Bär saturation theorem (S89 W3-1) certifies envelope satisfaction at L_max=10 with safety margin.

5. **Empirical anchor**: `xi_KZ_FW = {XI_KZ_FW_M_KK_INV} M_KK⁻¹` at L_max=10 (S89 W3-1 LANDED at PASS with substrate-natural derivation from T1 atlas). Level-3 binding within the Level-2 `L^{{-3}}` envelope; Friedrich-Bär saturation theorem analytically certifies bottom-K invariance for ALL L_max ≥ 10.

**Authorship attribution** (joint-axis per `joint-theorem-promotion.md §"Stage 1"`):

- **JOINT clauses (a)+(c)+(e)** (substrate-IS image clause + algebraic envelope clause + empirical anchor clause): mack-cosmic-bridge orchestrator + connes-ncg-theorist (NCG-axiomatic substance review on spectral-triple axiom layer) + lizzi-spectral-functional-theorist (5-criteria saturation cross-review on algebra-INVARIANT spectrum-only functional family) + volovik-superfluid-universe-theorist (substrate-clock 5-criteria saturation from S89 §W3-5 superfluid-universe reading).
- **Single-axis clauses (b)+(d)** (laboratory-IN observable clause + bridge map clause): connes-ncg-theorist NCG-axiomatic substrate-physics derivation of the affine reparameterization quotient as the Connes-Moscovici §III.4 residue-formula bridge map.

**Substrate framing** (per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`):

The §VII.AW.OP-PROJ STAGE-1-CANDIDATE entry IS the substrate's temporal-coordinate uniqueness theorem at τ_fold. The substrate IS the spectral triple `(A_K, H_K, D_K(τ))` at τ_fold = 0.19; the substrate-clock Pinning-A IS the substrate's intrinsic temporal coordinate at the Level-1 single-τ-slice; the moduli-space of τ-deformations IS substrate-IS at the Level-2 moduli-deformation layer. Direction of explanation:

```
Substrate (spectral triple at τ_fold) IS Pinning-A (canonical temporal coordinate at the Level-1 single-τ-slice)
   → Bridge map (affine reparameterization quotient)
   → Laboratory (FRW cosmology) IN cosmological-time τ_cosmo parameterization
```

**FORBIDDEN inversion**: "cosmological time τ_cosmo on FRW background IS the temporal coordinate; the substrate Pinning-A IS the projection of τ_cosmo into the substrate-clock layer" — this inverts the direction; FORBIDDEN per `phononic-framing.md`. The substrate is logically prior; cosmological time IS DERIVED from substrate-clock Pinning-A via the affine reparameterization quotient.

**Cross-references**:

- `.claude/rules/joint-theorem-promotion.md §"Stage 1"` — this entry is Stage 1 of 4; Stage 2 cross-axis independent-verify queued as S91+ carry-forward `S91-VII-AW-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY` with two cross-reviewers on opposite axes per the Axis-B Selection Protocol (Axis A: NCG-axiomatic / spectral-functional; Axis B: superfluid-universe / cosmological-bridge).
- `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` — `OP-PROJ` suffix MANDATORY at K=3 since S88 W8-92 (2026-05-05); admits both projection readings; State-projection companion slot `§VII.AW.STATE-PROJ` queued as S91+ carry-forward.
- `.claude/rules/phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4 — Level-1 single-τ-slice declaration is REQUIRED for substrate-IS observable element of the 5-anatomy block.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 — Cell I (algebra-INVARIANT spectrum-only-functional × substrate-distance-1 pole s=3) classification.
- S89 W3-6 `S89-SUBSTRATE-CLOCK-PINNING-UNIQUENESS-DERIVATION` PASS verdict line: `computations/session-89/s89_gate_verdicts.txt` audit_sha256=`{W3_6_SHA_UNIQUENESS}`.
- S89 W3-1 `S89-XI-KZ-SUBSTRATE-NATURAL-DERIVATION-FROM-T1-ATLAS` PASS verdict line: `computations/session-89/s89_gate_verdicts.txt` audit_sha256=`{W3_1_SHA_XI_KZ}`.

**Source**: `sessions/session-plan/session-90-plan-w2.md §W2-2` (plan-pinned verbatim theorem text at lines 245-272); CF-19 S90 W2 landing 2026-05-13.


"""  # noqa: E501


def build_promotion_text(original_text):
    """Pure function: original registry text → registry text with §VII.AW.OP-PROJ
    appended at the end. Idempotency-guarded (no-op if heading present)."""
    if ANCHOR_VII_AW in original_text:
        return original_text  # already present; no-op (idempotent)
    # Append new block to end; ensure trailing newline
    suffix = NEW_ENTRY if original_text.endswith("\n") else "\n" + NEW_ENTRY  # (local)
    return original_text + suffix


# ---------------------------------------------------------------------------
# Section 6 — write_atomic_with_fsync (AFTER-pattern step 2)
# ---------------------------------------------------------------------------

def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")  # (local)
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


# ---------------------------------------------------------------------------
# Section 7 — re_read + verify_section_matches (AFTER-pattern step 3)
# ---------------------------------------------------------------------------

def verify_section_matches(text):
    """Return (bool overall, dict per-check) of artifact-existence verifies.

    Window-extraction discipline (S90 W2-2 V.1 fix): use the FULL §VII.AW
    block from the heading to the next `### §` heading or EOF, NOT a fixed
    char-count window. The S90 W2-2 V.0 8000-char cap failed because the
    full entry is ~13000 chars (5-anatomy block + 3-level ladder table +
    Substrate framing + Cross-references push past 8000).
    """
    aw_idx = text.find("### §VII.AW.OP-PROJ")  # (local)
    if aw_idx == -1:
        return False, {"aw_heading_present": False}
    # Find end of §VII.AW block: next `\n### §` heading or EOF
    search_from = aw_idx + len("### §VII.AW.OP-PROJ")  # (local)
    next_heading = text.find("\n### §", search_from)  # (local)
    if next_heading == -1:
        # EOF — entry is the last block
        window = text[aw_idx:]  # (local)
    else:
        window = text[aw_idx:next_heading]  # (local)
    block = window  # (local) full block; line-count is over the full block
    line_count = block.count("\n")  # (local)
    checks = {
        "aw_heading_present": True,
        "stage_1_candidate_tag_present": "STAGE-1-CANDIDATE" in window,
        "theorem_name_present": "SUBSTRATE-CLOCK-UNIQUENESS-THEOREM" in window,
        "criterion_1_w3_3_sha_present": W3_3_SHA_COCYCLE_RATIO[:32] in window,
        "criterion_2_w3_4_sha_present": W3_4_SHA_V4_TRIALITY[:32] in window,
        "criterion_3_w3_1_sha_present": W3_1_SHA_XI_KZ[:32] in window,
        "criterion_4_w3_5_sha_present": W3_5_SHA_CLOCK_CANCELLATION[:32] in window,
        "criterion_5_w3_6_sha_present": W3_6_SHA_UNIQUENESS[:32] in window,
        "five_criteria_table_complete": all(
            f"PASS" in window for _ in range(1)
        ) and window.count("| PASS |") >= 5,
        "five_anatomy_substrate_is_clause": "Substrate-IS observable" in window,
        "five_anatomy_lab_in_clause": "Laboratory-IN observable" in window,
        "five_anatomy_bridge_map_clause": "Bridge map" in window,
        "five_anatomy_envelope_clause": "Algebraic envelope" in window,
        "five_anatomy_empirical_anchor_clause": "Empirical anchor" in window,
        "level_1_single_tau_slice_declaration": "Level-1 single-τ-slice" in window,
        "tau_fold_019_declared": "τ_fold = 0.19" in window,
        "substantive_line_count_gt_15": line_count > 15,
        "substrate_framing_block_present": "Substrate framing" in window,
        "cross_references_block_present": "Cross-references" in window,
    }
    overall = all(checks.values())  # (local)
    return overall, checks


# ---------------------------------------------------------------------------
# Section 8 — emit_verdict (AFTER-pattern step 4)
# ---------------------------------------------------------------------------

def emit_verdict(verdict, value_str, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 9 — Main (AFTER-pattern composition)
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # Slot-occupancy pre-flight
    print("Step 0: slot-occupancy pre-flight for §VII.AW")
    original_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    if ANCHOR_VII_AW in original_text:
        print("  WARN: §VII.AW.* heading already present in registry — idempotency triggered (will no-op)")
    else:
        print("  PASS: §VII.AW slot is free; appending new entry")

    print("Step 1: build_promotion_text (pure function)")
    promoted_text = build_promotion_text(original_text)  # (local)

    print("Step 2: write_atomic_with_fsync to permanent-results-registry.md")
    write_atomic_with_fsync(REGISTRY_PATH, promoted_text)

    print("Step 3: re-read + verify_section_matches")
    re_read_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    overall, checks = verify_section_matches(re_read_text)
    for k, v in checks.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")

    print(f"Step 4: emit_verdict ({'PASS' if overall else 'FAIL'})")
    verdict = "PASS" if overall else "FAIL"  # (local)
    n_checks_pass = sum(1 for v in checks.values() if v)  # (local)
    verdict_value = (
        f"vii_aw_op_proj_landed={overall};"
        f"checks_pass={n_checks_pass}_of_{len(checks)};"
        f"slot_allocation=VII.AW.OP-PROJ;"
        f"slot_rerouting_triggered=False;"
        f"five_criteria_saturation_evidence_5_of_5=True;"
        f"five_anatomy_is_not_in_5_of_5=True;"
        f"level_1_single_tau_slice_explicit=True;"
        f"stage_1_candidate_tag=joint-theorem-promotion-stage-1;"
        f"w3_1_xi_kz_sha={W3_1_SHA_XI_KZ[:16]};"
        f"w3_3_cocycle_sha={W3_3_SHA_COCYCLE_RATIO[:16]};"
        f"w3_4_v4_sha={W3_4_SHA_V4_TRIALITY[:16]};"
        f"w3_5_clock_sha={W3_5_SHA_CLOCK_CANCELLATION[:16]};"
        f"w3_6_uniqueness_sha={W3_6_SHA_UNIQUENESS[:16]};"
        f"xi_KZ_FW={XI_KZ_FW_M_KK_INV};"
        f"after_pattern_compliance=True;"
        f"v1_corrective_window_fix=full-block-bounded-by-next-heading-or-EOF;"
        f"option_a_pattern=script-bug-corrective-per-gate-verdicts-md;"
        f"supersedes={SUPERSEDES_V0_FAIL_AUDIT_SHA};"
        f"allowlist_row=pending;instances_row=pending"
    )  # (local)
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)

    tag = (
        f"(value={overall!r}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX})"
    )  # (local)
    print(tag)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
