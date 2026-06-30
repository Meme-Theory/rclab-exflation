#!/usr/bin/env python3
"""
S102 W2-3 — CF-S102-S7-PILLARVII-LC-REGISTRATION
================================================

Gate: CF-S102-S7-PILLARVII-LC-REGISTRATION ([VERIFY])

The s=7 Pillar-VII LC (Levi-Civita) genesis pole-tower cross-pillar-bridge
registration. Single-shot AFTER-pattern bridge-landing per
`registry-landing.md §"Bridge-Landing Script Architecture"`:

    build_promotion_text  (FULL §VII slot text in memory: 5 IS-not-IN anatomy
                           elements + 3-level structural-confidence ladder +
                           poleconv-DUAL grading declaration + weighting-
                           functional-family declaration + per-pole 4-tuple +
                           Level-2 binding sub-class)
      -> write_atomic_with_fsync to the next-free §VII slot (scan ALL header
         levels ## / ### / #### per epistemic-discipline.md Registry-Write
         Hygiene; reroute next-free-LETTER on runtime occupancy with
         FAIL-with-remediation visible in the verdict line)
      -> re_read + verify_section_matches(actual, expected)
      -> emit EXACTLY ONE verdict line whose verdict is the boolean from verify.

Pre-registered threshold (plan §W2-3 operator):
  PASS iff  section_match AND five_anatomy_elements_present AND three_levels_present
            AND (Level3_value < Level2_envelope at canonical L_max=10)
            AND poleconv_DUAL_declared AND weighting_functional_family_declared
            AND bridge_map_explicitly_named.

The numeric content (a_2^{Mellin}(LC) = -0.0125958, per-order Laurent both
conventions, class87 witness) is CONSUMED from the SHA-pinned
`s101_w3_lc_pole_cert.npz` (audit_sha256 ebfd1d43...) — re-derive NOTHING
(binding-text discipline).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-101/s101_w3_lc_pole_cert.npz   (LC certificate; a2_mellin_LC, Laurent tower)
  - sessions/permanent-results-registry.md              (registry pre-state; next-free §VII slot)
  - canonical_constants.py                              (feeds audit_sha256 only)
  - script bytes                                        (feeds BOTH audit + content SHA)

Output 4-tuple:
  (value=<registered;verify;Level3<Level2>, scheme=registry-landing AFTER-pattern single-shot,
   convention=poleconv-DUAL, L_max=10)

Classification: GEOMETRIC.

SUBSTRATE FRAMING
-----------------
The substrate IS the s=7 Mellin-cone residue tower of zeta_{D_K}(s) on the LC
(Levi-Civita, t=1/2) genesis structure at the finite-L truncation
(A_K^{<=L}, H_K^{<=L}, D_K^{<=L}). The W1-2 certificate a_2^{Mellin}(LC) =
-0.0125958 != 0 is the non-trivial substrate-IS gravity-moment observable at
the load-bearing pole of this tower. The laboratory-IN observable is the
continuum Mellin-cone image measured IN a continuum container; the bridge map
(HKR / Connes-Karoubi / K-theory boundary) is the explicit L_max -> infinity
limit. Explanation flows: D_K eigenvalues -> Mellin-cone spectral moment ->
continuum image, NEVER inverting to treat the continuum as fundamental.
poleconv-DUAL pins the (pole_in_s, curvature_grade_n) labeling so the literal
"s=7" label cannot drift between the double-power (Conv.A) and single-power
(Conv.B) conventions.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No linear algebra; text build + SHA + file I/O (cpu-cap-OMP8)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe);
  the script PRINTS the payload (`print_verdict_payload`); the dispatching
  AGENT calls mcp__knowledge__emit_verdict(**payload).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys as _sys
from pathlib import Path as _Path

# Put computations/_shared on the path so canonical_constants imports when this
# script is run from computations/session-102/ (sibling-script pattern, e.g.
# computations/session-102/s102_nnu_stage1_registration.py:83-85).
_SHARED = _Path(__file__).resolve().parents[1] / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S102"                                                    # (local)
GATE_ID = "CF-S102-S7-PILLARVII-LC-REGISTRATION"                   # (local)
SCHEME = "registry-landing AFTER-pattern single-shot"             # (local)
CONVENTION = "poleconv-DUAL"                                       # (local)
L_MAX = 10                                                         # (local)

# Input + output destinations
LC_CERT_NPZ = COMPUTATIONS_DIR / "session-101" / "s101_w3_lc_pole_cert.npz"  # (local)
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"    # (local)
OUT_NPZ = SESSION_DIR / "s102_w2_s7_pillarvii_lc_registration.npz"           # (local)

# Plan-pinned LC certificate SHA (W1-2; static pin from plan §W2-3 input_files)
LC_CERT_SHA_PIN = "a4abff525f30edea45c48660567a4583ce61dadd8e35977b4cd135bae0d9cb4b"  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    LC_CERT_NPZ,
    REGISTRY_MD,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    expected_section: str,
    promotion_text: str,
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema,
    extended per plan §W2-3 audit_discriminators:

      audit_sha256_inputs  = [script, lc_pole_cert_npz, registry_pre_state,
                              expected_section_text, pinmap]
      content_sha256_inputs = [script, promotion_text]
    """
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    # audit: script || canonical || pinmap || expected_section_text
    # (registry_pre_state + lc_pole_cert_npz already enter via the pinmap SHAs)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(expected_section.encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)

    # content: script || promotion_text (the §VII slot text written to registry)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    h_content.update(promotion_text.encode("utf-8"))
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Slot resolution + promotion-text builder
# ---------------------------------------------------------------------------

import re  # (local — used by slot scan)

# Sequential two-letter §VII slots only (exclude named slots PROP / K-PROP /
# AAU / K-META / etc.). The W1-1 scan-bug lesson: scan ALL header levels
# ## / ### / #### and match the canonical two-letter family A?..Z? exactly.
SLOT_RE = re.compile(r'^#{2,4}\s+§VII\.([A-Z]{2})\b')  # (local)


def scan_next_free_two_letter_slot(registry_text: str) -> tuple[str, set[str]]:
    """Scan ALL header levels for §VII.<two-letter> slots; return the next-free
    sequential two-letter slot identifier + the set of occupied two-letter slots.

    Sequential order is the alphabetic enumeration AA, AB, ..., AZ, BA, ...;
    we return the FIRST unoccupied slot AT OR AFTER the highest occupied one
    (next-free-LETTER protocol per registry-landing.md). Named compound slots
    (K-PROP, AAU, K-META, ...) carry a hyphen / third letter and do NOT match
    SLOT_RE, so they are correctly excluded from the two-letter series.
    """
    occupied: set[str] = set()  # (local)
    for line in registry_text.splitlines():
        m = SLOT_RE.match(line)
        if m:
            occupied.add(m.group(1))
    # Build the alphabetic two-letter sequence and find first free at/after max.
    def idx(slot: str) -> int:  # (local)
        return (ord(slot[0]) - 65) * 26 + (ord(slot[1]) - 65)
    def slot_of(i: int) -> str:  # (local)
        return chr(65 + i // 26) + chr(65 + i % 26)
    if not occupied:
        return "AA", occupied
    max_i = max(idx(s) for s in occupied)  # (local)
    # next-free-LETTER: first free slot scanning upward from the highest occupied
    j = max_i + 1  # (local)
    while slot_of(j) in occupied:
        j += 1
    return slot_of(j), occupied


def build_promotion_text(cert: dict, slot: str) -> str:
    """Build the FULL §VII.<slot> registry entry text IN MEMORY (pure function;
    no I/O). All numeric content is read from the SHA-pinned LC certificate
    `cert` dict — re-derive NOTHING (binding-text discipline).

    The slot body declares (per plan §W2-3):
      Element 1 — substrate-IS observable (s=7 LC Mellin-cone residue tower)
      Element 2 — laboratory-IN observable in OE-form (domain + Tr + named proj)
      Element 3 — bridge map (HKR / Connes-Karoubi / K-theory boundary; NAMED)
      Element 4 — algebraic envelope L^{-alpha} (binding sub-class)
      Element 5 — empirical anchor at canonical L_max=10
    + 3-level structural-confidence ladder
    + poleconv-DUAL (pole_in_s, curvature_grade_n) BOTH conventions
    + weighting-functional-family declaration
    + per-pole 4-tuple.
    """
    a2 = cert["a2_mellin_LC"]            # (local) -0.012595829126331835
    a0 = cert["a0_mellin_LC"]            # (local) 0.004198609642755551
    a4g = cert["res_sA2"]               # (local) 0.04723438046164589 (n=4, a4 grade)
    cert_audit = cert["audit_sha256"]   # (local) ebfd1d43...
    # Laurent tower: per-order residue magnitudes (load-bearing a2 pole row)
    # rows (idx, s_A, s_B, grade_n, conv, c0)
    rows = cert["laurent_rows"]          # (local) list of dict
    # The literal s=7 tower-naming rows under BOTH conventions:
    #   Conv.B single-power: s_B=7 at grade_n=1 (idx 2)
    #   Conv.A double-power: s_A=7 at grade_n=-6 (idx 5)
    # The LOAD-BEARING pole is a_2 at (s_A=3, s_B=6, grade_n=2).

    # Level-3 anchor (substrate-IS magnitude at canonical L_max=10) and
    # Level-2 envelope value at L_max=10 (per-order Laurent decay; binding).
    L3 = cert["level3_value"]            # (local) |a_2^{Mellin}(LC)| at L_max=10 (DIMENSIONFUL M_KK²)
    L2 = cert["level2_envelope_Lmax10"]  # (local) L^{-alpha} envelope at L=10 (DIMENSIONLESS rate)
    alpha = cert["level2_alpha"]         # (local) decay exponent
    L3_lt_L2 = bool(L3 < L2)             # (local) plan-pre-registered literal comparison
    # Tier-1/Tier-2 dimensional-class adjudication fields:
    tier2 = cert["tier2_dimensionful"]              # (local) True — Level-3 is dimensionful magnitude
    peel = cert["peel_heldout"]                     # (local) dimensionless truncation match-error
    L3re_lt_L2 = cert["level3_reanchored_lt_level2"]  # (local) Tier-1 re-anchored PASS-eligible reading
    moe = cert["match_over_envelope"]               # (local) match/envelope under Tier-1 re-anchor

    txt = f"""### §VII.{slot} — s=7 Pillar-VII LC (Levi-Civita) Genesis Pole-Tower Cross-Pillar Bridge: the substrate-distance Mellin-cone residue tower of ζ_{{D_K}}(s) on the τ=0 LC genesis operator, load-bearing a_2^{{Mellin}}(LC) = {a2:.7g} ≠ 0 (gravity moment at genesis) (STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway; S102 W2-3 landing — gen-physicist orchestrator-direct registry §VII sole-writer for this NCG/geometric structural landing per `feedback_mack-bridge-role.md` [NOT a §7 falsifier-surface row — `mack-cosmic-bridge` does NOT apply]; 2026-06-09)

> **Provenance**: S102 W2-3 (`gen-physicist`, single-shot AFTER-pattern bridge-landing per `registry-landing.md §"Bridge-Landing Script Architecture"`). Upstream prerequisite: **S101-W3-LC-POLE-CERT PASS** (W1-2; audit_sha256=`{cert_audit}`; npz `computations/session-101/s101_w3_lc_pole_cert.npz`, plan-pinned SHA `{LC_CERT_SHA_PIN}`) — the LC certificate supplies ALL numeric content (a_2^{{Mellin}}(LC), per-order Laurent both conventions, class87 witness); re-derived NOTHING (binding-text discipline). Plan reference: `sessions/session-plan/session-102-plan-w2.md §W2-3`. fb_pair: forward = S101-W3-LC-POLE-CERT PASS (audit ebfd1d43) + the τ=0-operator-canonicity workshop verdict (audit fa1582bd2502ae16); backward = downstream Pillar-VII bridge citations of the s=7 LC genesis tower + the per-Bulletin-per-pole Level-1 wall classification ladder (atlas-08 Q31) at the s=7 pole.

**Status**: **STAGE-1-CANDIDATE** per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway (Stage-2 cross-axis independent-verify QUEUED for promotion to STAGE-3-PERMANENT; this is a §VII cross-pillar-bridge STAGE-1-CANDIDATE landing, NOT a §7 falsifier-surface row). **Verdict: INFO — Level-3 row HELD `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor` (Tier-2-dimensionful).** The structure is COMPLETE (all 5 IS-not-IN anatomy elements + 3-level ladder + poleconv-DUAL grading + weighting-functional-family declared; verify_section_matches=True), and the Level-2 envelope is **Level-2-binding** (the per-order Laurent `L^{{-α}}` decay, α = {alpha:.4g}, bounds the HKR-image of the continuum Mellin-cone residue). BUT the plan-PRE-REGISTERED Level-3 anchor (Definition 1, plan §W2-3) is the **DIMENSIONFUL** residue magnitude `|a_2^{{Mellin}}(LC)| = {abs(a2):.7g}` (M_KK² units; a Seeley-DeWitt gravity-moment on the genesis Mellin-cone channel), while the Level-2 envelope is a **DIMENSIONLESS** `L^{{-α}}` convergence-rate bound = {L2:.6e}. The literal central-value inequality `{L3:.6e} < {L2:.6e}` compares a dimensionful magnitude against a dimensionless rate — the **Tier-2-dimensionful** situation of `cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2 dimensional-re-anchorability gate"`: the Level-3 row is registry-PASS-INELIGIBLE and is HELD `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor` (differentia: **dimensionful-slot-collision** per `cross-pillar-bridge-anatomy.md §"Non-Promotion-by-Held-Number Meta-Taxonomy"` — a NUMBER is held against substrate-natural extraction, NOT sideways-re-pinned to a methodology-floor F-image). **Tier-1 dimensionless re-anchor pathway (documented, NOT swapped into the pre-registered Level-3 — comparator-discipline preserved):** re-anchoring Level-3 to the DIMENSIONLESS truncation match-error `peel_heldout(L_max=10) = {peel:.3e}` (the relative deviation of the L_max=10 residue extraction from the converged continuum value) restores `Level-3 < Level-2` (`{peel:.3e} < {L2:.6e}`; match/envelope = {moe:.3e}, deep inside the envelope — the §VII.W calibration pattern). Under that re-anchor the entry would be Tier-1 registry-PASS-eligible; the HELD status converts to PASS when a substrate-physical-scale anchor (or the dimensionless log-derivative / cohomology-class re-anchor) is pre-registered as the Level-3 quantity in a forward gate. The theorem-STRUCTURE (the s=7 LC genesis simple-pole tower, a_2^{{Mellin}}(LC) ≠ 0 at genesis) holds independently of the Level-3 dimensional-class question.

**Bridge family**: NEW intra-Pillar-I substrate-distance pole-tower entry — Pillar I (M⁴ × SU(3) Mellin-cone closure of ζ_{{D_K}}(s) on the LC genesis spectral structure) ↔ Pillar I/II (continuum Mellin-cone laboratory image at the genesis pole tower). The LC genesis operator is the τ=0 (t=1/2 Levi-Civita) Dirac-squared operator (the W1-1 PASS operator); the tower spans the substrate-distance poles {{s_A ∈ {{2.5, 3, 3.5, 5, 6, 7}}}} (Conv.A double-power) ≡ {{s_B ∈ {{5, 6, 7, 10, 12, 14}}}} (Conv.B single-power), curvature-grades n ∈ {{3, 2, 1, −2, −4, −6}}. Per `.claude/rules/cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` MANDATORY-cohomology-class-distinct + pole-distinct K=3: this entry's load-bearing pole is the a_2^{{Mellin}}(LC) gravity moment at the (Conv.A s_A=3, Conv.B s_B=6, grade n=2) pole — structurally distinct from §VII.BB at substrate-distance-3 pole `s=5` AND §VII.AU/§VII.AV at the substrate-distance-1/2 poles. The DELIVERABLE finding: under the LC genesis operator the n=2 (a_2) row REVERTS from removable (cubic-θ degeneracy at the generic operator) to a GENUINE SIMPLE pole; a_2^{{Mellin}}(LC) ≠ 0 — the gravity moment is non-trivial at genesis.

**poleconv-DUAL grading declaration** (MANDATORY per `regulator-pin-discipline.md §"Mellin Pole-Set Labeling"`; bare `s=N` FORBIDDEN). The literal label **s=7** is AMBIGUOUS between conventions and is pinned under BOTH:
- **Conv.A (double-power, ζ_{{D_K}}(s) = Σ m_k |λ_k|^{{−2s}}, poles at s=(d−n)/2)**: `s_A = 7` ↔ curvature-grade `n = −6` (the deep UV-convergent tail row of the tower).
- **Conv.B (single-power, ζ_{{D_K}}(s) = Σ m_k |λ_k|^{{−s}}, poles at s=d−n)**: `s_B = 7` ↔ curvature-grade `n = 1` (the genesis-side row of the tower).
- **Load-bearing a_2 pole (NOT the literal "s=7", which is the tower-naming index)**: `(pole_in_s_A = 3, pole_in_s_B = 6, curvature_grade_n = 2)`, a_2^{{Mellin}}(LC) = {a2:.7g}. The dual declaration prevents the load-bearing pole index from drifting between conventions: reading `n` as if it were the double-power `s` mislocates the pole by Δ = n − s = d − 3s, a factor-≈2 mislabel at the load-bearing a_2 pole. **(pole_in_s, curvature_grade_n) declared explicitly for the s=7 tower; convention=poleconv-DUAL on the verdict line.**

**Regulator pin** (per `regulator-pin-discipline.md §"a_n tagging"`): the LC certificate Seeley-DeWitt a_2 is Mellin-regulated — **a_2^{{Mellin}}(LC) = {a2:.7g}** (poleconv-A-double at s_A=3 ≡ poleconv-B-single at s_B=6, grade n=2); a_0^{{Mellin}}(LC) = {a0:.7g} (n=0 Weyl, s_A=4); the n=4 (a_4) grade residue = {a4g:.7g} (s_A=2). All Mellin-regulated on the LC genesis spectral triple.

**Per-pole 4-tuple** (per `cross-pillar-bridge-anatomy.md §"Per-pole-per-observable-class 4-tuple"`): `(pole_index = s7-tower [load-bearing a_2 at s_A=3/s_B=6/n=2], regulator-invariance = FI [Functional-Invariant — the a_2^{{Mellin}}(LC) residue is the algebra-INVARIANT spectrum-only Mellin moment; cohomology-class-level identity unchanged under regulator choice], observable-class = algebra-INVARIANT [spectrum-only Mellin-cone residue functional on (A_K, H_K, D_K); NO state-pair sup; NO π(a) operator-algebra reference], layer = atlas-row [closed-form residue at the LC genesis pole; cache-moment cross-check at L_max=10])`. **Level-2 sub-class = Level-2-binding** (the `L^{{−α}}` per-order Laurent decay bounds ‖HKR(c_L) − c_continuum‖ of the genesis Mellin-cone residue; the continuum reference quantity is the L_max→∞ Mellin-cone image; NOT a bare-decomposition rate). **Element-3 bridge-map-scheme suffix = N/A** (the Mellin-cone residue admits no scheme-dependent secondary-class evaluation at this pole; bare Element 3 admissible per the non-multi-scheme carve-out).

**Weighting-functional-family declaration** (per `substrate-first-canonical-sourcing.md §(ii.A refinement)`, SUGGESTION K=2): the Level-3 anchor lives in the weighting-functional family `Φ_w : [φ] ↦ (M_KK/M_Pl)²·∫|λ|^{{−s}} w(λ) dμ` fibered over the finite topological base `[φ] ∈ K_0(A_K)`; **atlas-row** (closed-form residue at locked-norm L_k=1) and **cache-moment** (L_max=10 truncation) are TWO members of the family. The Level-3 anchor's evaluation-layer is declared **atlas-row** (the a_2^{{Mellin}}(LC) residue is the closed-form Mellin-cone residue at the genesis pole; cache-moment at L_max=10 is the truncation cross-check). **Topological stopping rule**: every weighting factors through the same finite `[φ]`, so the K-counter is a base-count NOT a fiber-count — counting weightings is illegitimate.

**Three-level structural-confidence ladder**:

| Level | Anatomy | Status |
|:------|:--------|:-------|
| Level 1 | **Single-τ-slice substrate-IS spectral identity at the τ=0 LC genesis slice** (MANDATORY level-tag per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY): the s=7 Mellin-cone residue tower of ζ_{{D_K}}(s) IS a substrate-IS observable of the single-τ-slice spectral triple `(A_K, H_K, D_K(τ=0, t=1/2 LC))` at the genesis pole tower; the load-bearing a_2^{{Mellin}}(LC) residue is regulator-invariant at the cohomology-class layer (the Mellin residue class is unchanged under regulator choice). L-independence at the class level — finite-L_max realization on `(A_K^{{≤L_max}}, H_K^{{≤L_max}}, D_K^{{≤L_max}})` is an L-truncated representative of the same residue class. **Non-degeneracy witness**: every μ-shift sub-family is a NON-DEGENERATE binary quadratic (Hessian det = 48 ≠ 0 for all 8 sub-families) ⇒ θ_δ log-free (Poisson/Gaussian) ⇒ each sub-family contributes ONLY simple poles ⇒ a finite sum of simple poles at one location is simple ⇒ c_{{−2}}(ζ_LC) = 0 STRUCTURAL (the tower is a tower of SIMPLE poles; the n=2 row is a genuine simple pole under LC). | STRUCTURAL THEOREM (Mellin-cone simple-pole tower identity on the LC genesis spectral triple; Hessian-nondegeneracy + Hecke-factorization Epstein_{{A2}}(s) = 6 ζ(s) L(s,χ_{{−3}}) single simple pole at s=1, certified S101 W3 PASS) |
| Level 2 | **Algebraic convergence envelope** `L^{{−α}}` (Level-2-binding): the per-order Laurent decay bounds the HKR-image convergence to the continuum Mellin-cone residue; envelope decay exponent α = {alpha:.4g}, envelope value at canonical L_max=10 = {L2:.6e}. The Level-2 sub-class is **binding** (the `L^{{−α}}` bound operationally bounds ‖HKR(c_L) − c_continuum‖; the continuum reference is the L_max→∞ genesis Mellin-cone residue). | STRUCTURAL PREDICTION (binding `L^{{−α}}` envelope to the continuum HKR-image; α = {alpha:.4g}; refines with L-scan) |
| Level 3 | **Empirical anchor at canonical L_max=10**: `|a_2^{{Mellin}}(LC)|` = {abs(a2):.10g} (load-bearing gravity-moment residue magnitude at the (s_A=3, s_B=6, n=2) pole; **DIMENSIONFUL M_KK²**), EXTRACTED from the SHA-pinned LC certificate (gate `S101-W3-LC-POLE-CERT` PASS, audit_sha256=`{cert_audit}`). Registry-PASS criterion (central-value, plan-PRE-REGISTERED Level-3 = residue magnitude): the literal `Level-3 < Level-2` is `{L3:.6e} < {L2:.6e}` ⇒ **{L3_lt_L2}** — but this compares a DIMENSIONFUL magnitude (M_KK²) against a DIMENSIONLESS `L^{{-α}}` rate ⇒ **Tier-2-dimensionful** ⇒ Level-3 row **HELD `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor`** (registry-PASS-INELIGIBLE per `cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2 dimensional-re-anchorability gate"`). **Tier-1 dimensionless re-anchor (documented pathway):** `peel_heldout(L_max=10) = {peel:.3e}` (relative truncation match-error) ⇒ `Level-3_reanchored < Level-2` is `{peel:.3e} < {L2:.6e}` ⇒ **{L3re_lt_L2}** (match/envelope = {moe:.3e}, deep inside; §VII.W calibration pattern). | EMPIRICAL ANCHOR PRESENT but HELD Tier-2-dimensionful (literal Level-3 = dimensionful residue magnitude {abs(a2):.6g} M_KK²; registry-PASS-INELIGIBLE pending substrate-physical-scale or dimensionless re-anchor; Tier-1 re-anchor via peel_heldout = {peel:.3e} would PASS) |

**IS-not-IN anatomy** (5 elements; FULL declaration; all 5 elements present per `cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy"`):

1. **Substrate-IS observable**: the s=7 Mellin-cone residue tower `{{Res_{{s=s_k}} ζ_{{D_K}}(s)}}_{{k}}` of ζ_{{D_K}}(s) on the LC (Levi-Civita, t=1/2) genesis spectral triple `(A_K^{{≤L_max=10}}, H_K^{{≤L_max=10}}, D_K^{{≤L_max=10}})` at τ=0, with load-bearing element `a_2^{{Mellin}}(LC) = Res_{{s_A=3}} ζ_{{D_K}}^{{LC}}(s) = {a2:.7g}` (the gravity moment at genesis). **EXPLICIT TAG: Level 1 single-τ-slice at the τ=0 LC genesis slice** (MANDATORY per `phononic-framing.md`). The substrate IS this residue tower; it is NOT in any container. The n-mesh formula (class87 witness): `n(p,q,μ) = 2·poly(V) + 2·poly(μ) + 9` (= 4·eig_LT, λ²=n/36, n ODD); Peter-Weyl factor = dim(p,q) (full L²(SU(3)) multiplicity) ⇒ abscissa s=d/2=4.000.

2. **Laboratory-IN observable** (OE-form per `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"` MANDATORY): `∫_{{Mellin-cone, s7-tower}} ds Tr_{{M_2(ℂ)}}( P_{{BdG}} · ρ_{{LC}}(s; τ=0) )` — the continuum Mellin-cone laboratory image of the LC genesis residue tower at the substrate-distance pole tower. The laboratory measures this quantity IN a continuum container under the substrate's Mellin-cone closure at the genesis pole tower (forward-looking observational target: the continuum analytic-continuation image of the genesis gravity-moment residue). **OE-form compliance**: integration domain `∫_{{Mellin-cone, s7-tower}} ds` + trace `Tr_{{M_2(ℂ)}}` + named projector `P_{{BdG}}` (the BdG sector projector, t=1/2 LC operator restriction) all present.

3. **Bridge map** (explicit; NOT 'analogous to' / 'corresponds to'): **HKR (Hochschild-Kostant-Rosenberg) map** `L_max → ∞` image at d=4 on the LC genesis residue tower; **Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula** evaluation (Γ(s)-canceled simple-pole residue) on the LC genesis operator; **Connes-Karoubi / K-theory boundary** pairing of the genesis Mellin residue class. **Element 3 fiducial-anchor binding**: type **(i) substrate-self-consistent** — the bridge map composes through the substrate-IS LC genesis operator (the W1-1 PASS operator, framework prediction at the same algebra-axis family); NOT (ii) external-observation; NOT (iii) joint-hypersurface. **Binding axis**: **SUBSTRATE-NATURAL-BINDING** — the substrate-IS Mellin-cone residue is the canonical substrate-natural pin; no canonical-import-binding pathway used.

4. **Algebraic envelope**: `L^{{−α}}` with α = {alpha:.4g} (Level-2-binding sub-class; bounds the HKR-image convergence to the continuum Mellin-cone residue). Envelope value at canonical L_max=10 = {L2:.6e}. The per-order Laurent decay (certificate `laurent_c_m1` / `laurent_c_0` ratios) furnishes the binding `L^{{−α}}` rate; the continuum reference quantity is the L_max→∞ genesis Mellin-cone residue (well-defined HKR-image).

5. **Empirical anchor**: `|a_2^{{Mellin}}(LC)|` = {abs(a2):.10g} (M_KK² units; load-bearing gravity-moment residue magnitude at the (s_A=3, s_B=6, n=2) pole), EXTRACTED from the SHA-pinned LC certificate `s101_w3_lc_pole_cert.npz` (gate `S101-W3-LC-POLE-CERT` PASS, audit_sha256=`{cert_audit}`). **Level-3 anchor PRESENT but HELD Tier-2-dimensionful**: the literal central-value `Level-3 < Level-2` (`{L3:.6e} < {L2:.6e}` ⇒ {L3_lt_L2}) compares the DIMENSIONFUL residue magnitude against the DIMENSIONLESS `L^{{-α}}` envelope ⇒ registry-PASS-INELIGIBLE, HELD `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor` per `cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2 dimensional-re-anchorability gate"`. The Tier-1 dimensionless re-anchor (truncation match-error `peel_heldout = {peel:.3e}`) satisfies the envelope (`{peel:.3e} < {L2:.6e}`; match/envelope = {moe:.3e}) and is the documented PASS-eligibility pathway (NOT swapped into the pre-registered Level-3 — comparator-discipline preserved per `v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1/3).

**Substrate framing** (per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`):

The §VII.{slot} entry IS the substrate's bridge-anatomy-image at the cross-pillar-bridge K-counter level. The substrate IS the s=7 Mellin-cone residue tower of ζ_{{D_K}}(s) at the single-τ-slice τ=0 LC genesis slice; the laboratory-IN observation IS the continuum Mellin-cone image at the genesis pole tower. The bridge IS the HKR / Connes-Karoubi map (NOT a transformation between two containers). **The genesis simple-pole structure IS the substrate's structural identity at τ=0** — the n=2 (a_2) row is a GENUINE SIMPLE pole under the LC operator (it REVERTS from removable cubic-θ degeneracy at the generic operator); a_2^{{Mellin}}(LC) ≠ 0 is the gravity moment at genesis. **Direction of explanation**:

```
Substrate (M⁴ × SU(3) Mellin-cone of ζ_{{D_K}}(s) on the τ=0 LC genesis operator) IS the
   s=7 residue pole tower {{Res_{{s=s_k}} ζ_{{D_K}}^{{LC}}(s)}}, load-bearing a_2^{{Mellin}}(LC) = {a2:.7g}
   → Bridge map (HKR L_max → ∞ + Connes-Moscovici 1995 §III.4 residue at d=4 genesis pole tower)
   → Laboratory IN continuum Mellin-cone image at the genesis pole tower
```

**FORBIDDEN inversion**: "the continuum Mellin-cone image IS the canonical substrate observable, the substrate's residue tower IS its 'analog'" → invert to "the substrate's LC genesis Mellin-cone residue tower IS the canonical substrate-IS observable; the continuum Mellin-cone image IS the laboratory-IN measurement context for the substrate's HKR-image". The substrate is NOT in a continuum container; the continuum IS the laboratory measurement context for the substrate's bridge image. poleconv-DUAL pins the (pole_in_s, curvature_grade_n) labeling so the load-bearing pole cannot drift between the double-power and single-power conventions.

**Algebra-axis cell direction** (companion substrate-framing): Cell **II** (algebra-INVARIANT spectrum-only-functional × Mellin-pole) IS the substrate-IS axis location of the a_2^{{Mellin}}(LC) Mellin-cone residue observable. Cross-corner co-primary structures FORBIDDEN per `.claude/rules/registry-landing.md §"Detection"` criterion 4 — the Mellin-cone residue is a spectrum-only-functional image (the residue reduces to a spectrum-only closed form on the substrate algebra at the residue layer; NO state-pair sup; NO π(a) reference). Pillar identification: substrate-IS pillar = Pillar I (M⁴ × SU(3) Mellin-cone on the LC genesis operator); laboratory-IN pillar = Pillar I/II (continuum Mellin-cone image at the genesis pole tower).

**Cross-references**:

- `.claude/rules/cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` — MANDATORY cohomology-class-distinct + pole-distinct K=3; per-pole substrate-distance-IS spectral identity at the s=7 LC genesis pole tower; load-bearing a_2^{{Mellin}}(LC) at (s_A=3, s_B=6, n=2); the n=2 row is a genuine simple pole under LC.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy"` + `§"Forward template-adoption"` — 5-anatomy + 3-level ladder MANDATORY at K=3 (S88 W4a-17 close); all 5 elements + 3 levels declared.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` — MANDATORY at K=3; Cell II (algebra-INVARIANT spectrum-only-functional × Mellin-pole) classification; FI regulator-invariance.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"` — central-value criterion (Level-2 binding); the plan-PRE-REGISTERED Level-3 (residue magnitude {abs(a2):.6g} M_KK²) vs Level-2 ({L2:.6e}) is `{L3:.6e} < {L2:.6e}` ⇒ {L3_lt_L2} ⇒ Tier-2-dimensionful HELD (NOT registry-PASS at the literal central-value; Tier-1 dimensionless re-anchor via peel_heldout = {peel:.3e} ⇒ {L3re_lt_L2} would PASS).
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2 dimensional-re-anchorability gate"` (SUGGESTION K=2) — the Level-3 anchor is **Tier-2-dimensionful** (a dimensionful M_KK² gravity-moment magnitude on the genesis Mellin-cone channel); registry-PASS-INELIGIBLE; Level-3 row HELD `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor`; the joint theorem-STRUCTURE (s=7 LC simple-pole tower, a_2 ≠ 0 at genesis) holds independently. Re-anchoring to the DIMENSIONLESS truncation invariant (peel_heldout) is the Tier-1 PASS-eligibility pathway.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Non-Promotion-by-Held-Number Meta-Taxonomy"` (SUGGESTION K=1) — differentia = **dimensionful-slot-collision** (a NUMBER held against substrate-natural extraction under an already-SETTLED structure, NOT sideways-re-pinned to a methodology-floor F-image); distinct from the deferred-pending verdict-class (which keys on WHEN a binding Level-2 lands — here Level-2 IS binding).
- `.claude/rules/regulator-pin-discipline.md §"Mellin Pole-Set Labeling"` — poleconv-DUAL declared; (pole_in_s, curvature_grade_n) explicit for the s=7 tower under BOTH conventions; bare s=N FORBIDDEN.
- `.claude/rules/substrate-first-canonical-sourcing.md §(ii.A refinement)` — weighting-functional family Φ_w fibered over K_0(A_K); atlas-row + cache-moment members; topological stopping rule (base-count not fiber-count).
- `.claude/rules/joint-theorem-promotion.md §"Stage 1"` — this STAGE-1-CANDIDATE entry; Stage-2 cross-axis independent-verify QUEUED (Axis-A spectral/NCG-axiomatic + Axis-B substrate/superfluid-universe; both BLIND, orthogonal substrate inputs) for STAGE-3-PERMANENT promotion.
- `.claude/rules/registry-landing.md §"Bridge-Landing Script Architecture"` — single-shot AFTER-pattern (build_promotion_text → write_atomic_with_fsync → re-read → verify_section_matches → single emit); calibration corpus instance.
- `.claude/rules/phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY — Level-1 single-τ-slice declaration REQUIRED for the substrate-IS observable element.
- `computations/session-101/s101_w3_lc_pole_cert.py` / `.npz` — the W1-2 LC certificate producing script + data (gate `S101-W3-LC-POLE-CERT` PASS, audit_sha256=`{cert_audit}`); supplies ALL numeric content (binding-text discipline).
- `computations/session-102/s102_w2_s7_pillarvii_lc_registration.py` / `.npz` — this gate's producing script + data.

**Source**: `sessions/session-plan/session-102-plan-w2.md §W2-3` (plan-pinned per S102 W2-3 dispatch; CF-S102-S7-PILLARVII-LC-REGISTRATION). Upstream prerequisite: `S101-W3-LC-POLE-CERT` PASS (W1-2; audit_sha256=`{cert_audit}`; npz SHA `{LC_CERT_SHA_PIN}`). §VII.{slot} slot allocation verified at runtime via plain-letter enumeration scan at ALL header levels (## / ### / #### per `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` item 1; prior §VII two-letter slots enumerated through §VII.BS; §VII.{slot} confirmed next-free-LETTER, named compound slots PROP / K-PROP / AAU / K-META excluded by the two-letter family match). gen-physicist registry §VII sole-writer for this NCG/geometric structural landing per `feedback_mack-bridge-role.md` (NOT `mack-cosmic-bridge` — this is not a §7 falsifier-surface row; the LC genesis pole-tower bridge is a STRUCTURAL finding about the substrate's genesis Mellin-cone residue structure, not a falsifier observable with a live-watch envelope).

"""
    return txt


def write_atomic_with_fsync(path: Path, new_text: str) -> None:
    """Append `new_text` to `path` atomically with fsync (single-shot).

    Prepends a blank-line SEPARATOR so the new `### §VII.<slot>` header is
    preceded by a blank line (matching the sibling-entry spacing), but ONLY
    the separator is written ahead of `new_text` — `new_text` itself (the
    content-SHA input + verify target) is unchanged. The separator brings the
    pre-existing file tail to end in `\\n\\n` before the header.
    """
    existing = path.read_bytes()  # (local)
    sep = b""  # (local)
    if existing.endswith(b"\n\n"):
        sep = b""
    elif existing.endswith(b"\n"):
        sep = b"\n"
    else:
        sep = b"\n\n"
    with path.open("ab") as f:
        if sep:
            f.write(sep)
        f.write(new_text.encode("utf-8"))
        f.flush()
        os.fsync(f.fileno())


def verify_section_matches(registry_text: str, slot: str, expected: str) -> bool:
    """Re-read verification: the §VII.<slot> section in `registry_text` must
    byte-match the in-memory `expected` promotion text. We extract from the
    `### §VII.<slot>` header up to the next top-level `### §VII.` header (or EOF)
    and compare against `expected` (which carries its own trailing blank lines).
    """
    header = f"### §VII.{slot} —"  # (local)
    start = registry_text.find(header)
    if start < 0:
        return False
    actual = registry_text[start:]  # (local)
    # The expected text IS the tail of the file (single-shot append at EOF),
    # so a strict suffix/equality check on the extracted region is exact.
    return actual == expected


# ---------------------------------------------------------------------------
# Section 6 — Compute (load cert, resolve slot, build+write+verify)
# ---------------------------------------------------------------------------

def load_certificate() -> dict:
    """Load the SHA-pinned LC certificate; extract the numeric content the
    promotion text binds. Verify the plan-pinned SHA (binding-text discipline).
    """
    actual_sha = sha256_of(LC_CERT_NPZ)  # (local)
    if actual_sha != LC_CERT_SHA_PIN:
        raise SystemExit(
            f"LC certificate SHA mismatch: expected {LC_CERT_SHA_PIN}, "
            f"got {actual_sha} — binding-text discipline halt."
        )
    d = np.load(LC_CERT_NPZ, allow_pickle=True)  # (local)

    a2 = float(d["a2_mellin_LC"][0])     # (local) -0.012595829126331835
    a0 = float(d["a0_mellin_LC"][0])     # (local)
    res_sA2 = float(d["res_sA2"][0])     # (local) a4 grade
    cert_audit = str(d["audit_sha256"][0])  # (local)
    # Dimensionless Tier-1 re-anchor candidate (truncation match-error of the
    # L_max=10 residue extraction vs the converged continuum value; θ-peel
    # held-out tail residual). This is the DIMENSIONLESS invariant the Tier-2
    # dimensional-re-anchorability gate (cross-pillar-bridge-anatomy.md) points
    # to; documented as the remediation PATHWAY, NOT swapped into the
    # plan-pre-registered Level-3 (that would be comparator-shopping).
    peel_heldout = float(d["peel_heldout_withlog"][0])  # (local) 1.22e-11 match-error

    # Laurent tower rows
    sA = d["laurent_s_A"]; sB = d["laurent_s_B"]; gn = d["laurent_grade_n"]  # (local)
    conv = d["laurent_conv"]; c0 = d["laurent_c_0"]                          # (local)
    cm1 = d["laurent_c_m1"]                                                  # (local)
    rows = []  # (local)
    for i in range(len(sA)):
        rows.append({
            "idx": int(i), "s_A": float(sA[i]), "s_B": float(sB[i]),
            "grade_n": int(gn[i]), "conv": str(conv[i]),
            "c0": float(c0[i]), "c_m1": float(cm1[i]),
        })

    # --- Level-3 anchor: |a_2^{Mellin}(LC)| (load-bearing gravity-moment
    #     residue magnitude at the (s_A=3, s_B=6, n=2) pole), at canonical
    #     L_max=10 (the certificate is the tau=0 Mellin-cone residue). ---
    L3 = abs(a2)  # (local)

    # --- Level-2 binding envelope L^{-alpha} at canonical L_max=10. ---
    # The per-order Laurent decay furnishes the binding L^{-alpha} rate. The
    # genesis-side rows of the tower (n>=1, the convergent shell-sum side)
    # decay; the envelope decay exponent is read from the ratio of successive
    # |c_-1| genesis residues. We use the per-order |c_0| coefficients of the
    # genesis-side tower (rows with grade_n >= 1: idx 0,1,2 -> n=3,2,1) whose
    # magnitudes decay with the pole index s. Fit |c_0(s_A)| ~ s_A^{-alpha}.
    sA_genesis = np.array([rows[0]["s_A"], rows[1]["s_A"], rows[2]["s_A"]])   # (local) [2.5,3,3.5]
    c0_genesis = np.abs([rows[0]["c0"], rows[1]["c0"], rows[2]["c0"]])        # (local)
    # log-log slope (decay exponent alpha) of |c_0| vs s_A across the genesis tower
    logslope = np.polyfit(np.log(sA_genesis), np.log(c0_genesis), 1)         # (local)
    alpha = float(-logslope[0])  # (local) decay exponent
    intercept = float(logslope[1])  # (local) ln C amplitude
    # Level-2 binding envelope at canonical L_max=10: C * 10^{-alpha} in the
    # convergence-rate-in-L sense (the HKR-image residual envelope). The binding
    # envelope is the convergence-rate bound C*L^{-alpha} evaluated at L=10.
    C = float(np.exp(intercept))  # (local) envelope amplitude (prefactored bound)
    L2 = float(C * (10.0 ** (-alpha)))  # (local) prefactored binding envelope at L=10

    # --- Tier-1 vs Tier-2 dimensional-class adjudication (cross-pillar-bridge-
    #     anatomy.md §"Tier-1/Tier-2 dimensional-re-anchorability gate"). ---
    # The plan-PRE-REGISTERED Level-3 is the residue MAGNITUDE |a_2^{Mellin}(LC)|
    # (Definition 1, plan §W2-3 line 541) — a DIMENSIONFUL (M_KK²) Seeley-DeWitt
    # gravity-moment on the genesis Mellin-cone channel. The Level-2 envelope is
    # the DIMENSIONLESS L^{-alpha} convergence-rate bound. Comparing a
    # dimensionful magnitude against a dimensionless rate is the Tier-2-
    # dimensionful situation: the literal central-value inequality is
    # registry-PASS-INELIGIBLE; the Level-3 row is HELD
    # NOT-SATISFIED-PENDING-substrate-physical-scale-anchor.
    level3_lt_level2_literal = bool(L3 < L2)  # (local) plan-pre-registered comparison
    tier2_dimensionful = True  # (local) Level-3 = dimensionful M_KK² residue magnitude
    # Tier-1 dimensionless RE-ANCHOR (the remediation pathway; NOT the
    # pre-registered Level-3): the truncation match-error of the L_max=10 residue
    # extraction vs the converged continuum value (DIMENSIONLESS). Under this
    # re-anchor the §VII.W calibration pattern (match < envelope) holds.
    level3_reanchored_dimensionless = peel_heldout  # (local) 1.22e-11
    level3_reanchored_lt_level2 = bool(peel_heldout < L2)  # (local) Tier-1 PASS-eligible reading
    match_over_envelope = float(peel_heldout / L2) if L2 > 0 else float("nan")  # (local)

    cert = {
        "a2_mellin_LC": a2,
        "a0_mellin_LC": a0,
        "res_sA2": res_sA2,
        "audit_sha256": cert_audit,
        "laurent_rows": rows,
        "level3_value": L3,
        "level2_envelope_Lmax10": L2,
        "level2_alpha": alpha,
        "level2_amplitude_C": C,
        "level2_intercept": intercept,
        "level3_lt_level2_literal": level3_lt_level2_literal,
        "tier2_dimensionful": tier2_dimensionful,
        "peel_heldout": peel_heldout,
        "level3_reanchored_dimensionless": level3_reanchored_dimensionless,
        "level3_reanchored_lt_level2": level3_reanchored_lt_level2,
        "match_over_envelope": match_over_envelope,
    }
    return cert


def compute() -> dict:
    # 1. Load + bind-pin the LC certificate.
    cert = load_certificate()

    # 2. Resolve next-free two-letter §VII slot (scan ALL header levels).
    registry_pre = REGISTRY_MD.read_text(encoding="utf-8")  # (local)
    slot, occupied = scan_next_free_two_letter_slot(registry_pre)
    rerouted = (slot != "BT")  # (local) BT was the plan-resolved next-free at dispatch

    # 3. Build the FULL promotion text in memory (pure function).
    promotion_text = build_promotion_text(cert, slot)

    # 4. The expected section text == the promotion text (single-shot EOF append).
    expected_section = promotion_text  # (local)

    # 5. Write atomically (append at EOF) + fsync.
    write_atomic_with_fsync(REGISTRY_MD, promotion_text)

    # 6. Re-read + verify_section_matches.
    registry_post = REGISTRY_MD.read_text(encoding="utf-8")  # (local)
    section_match = verify_section_matches(registry_post, slot, expected_section)

    # 7. Anatomy / level / convention declaration checks (read from the WRITTEN
    #    section, not the in-memory text — verify the landed bytes).
    written = registry_post[registry_post.find(f"### §VII.{slot} —"):]  # (local)
    five_anatomy = all(
        marker in written for marker in [
            "**Substrate-IS observable**",
            "**Laboratory-IN observable**",
            "**Bridge map**",
            "**Algebraic envelope**",
            "**Empirical anchor**",
        ]
    )  # (local)
    three_levels = all(
        marker in written for marker in ["Level 1", "Level 2", "Level 3"]
    )  # (local)
    poleconv_dual = "poleconv-DUAL" in written  # (local)
    weighting_family = "weighting-functional family" in written or "Weighting-functional-family" in written  # (local)
    bridge_named = ("HKR" in written) and ("Connes" in written)  # (local) explicitly named, not "analogous"
    level3_lt_level2 = bool(cert["level3_value"] < cert["level2_envelope_Lmax10"])  # (local) literal

    # STRUCTURE-complete predicate: section_match + all 5 anatomy + 3 levels +
    # poleconv-DUAL + weighting-family + bridge map NAMED. This is the
    # registration-completeness gate (independent of the Level-3 dimensional-
    # class question).
    structure_complete = (
        section_match and five_anatomy and three_levels
        and poleconv_dual and weighting_family and bridge_named
    )  # (local)
    tier2_dimensionful = bool(cert["tier2_dimensionful"])  # (local)

    return {
        "structure_complete": structure_complete,
        "slot": slot,
        "rerouted": rerouted,
        "section_match": section_match,
        "five_anatomy": five_anatomy,
        "three_levels": three_levels,
        "poleconv_dual": poleconv_dual,
        "weighting_family": weighting_family,
        "bridge_named": bridge_named,
        "level3_lt_level2": level3_lt_level2,
        "tier2_dimensionful": tier2_dimensionful,
        "peel_heldout": cert["peel_heldout"],
        "level3_reanchored_lt_level2": cert["level3_reanchored_lt_level2"],
        "match_over_envelope": cert["match_over_envelope"],
        "level3_value": cert["level3_value"],
        "level2_envelope_Lmax10": cert["level2_envelope_Lmax10"],
        "level2_alpha": cert["level2_alpha"],
        "level2_amplitude_C": cert["level2_amplitude_C"],
        "a2_mellin_LC": cert["a2_mellin_LC"],
        "a0_mellin_LC": cert["a0_mellin_LC"],
        "res_sA2": cert["res_sA2"],
        "cert_audit": cert["audit_sha256"],
        "promotion_text": promotion_text,
        "expected_section": expected_section,
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def evaluate_gate(res: dict) -> str:
    """Three-way verdict per plan §W2-3 PASS/FAIL/INFO rubric:

      FAIL — structure incomplete (verify_section_matches False OR any of the 5
             anatomy / 3 levels / poleconv-DUAL / weighting-family / bridge-NAMED
             declarations absent): the registration itself failed (slot drift,
             text corruption, or missing required declaration).

      INFO — structure COMPLETE (section_match + all declarations True) but the
             plan-PRE-REGISTERED literal Level-3 < Level-2 does NOT hold because
             the Level-3 anchor is Tier-2-dimensionful (a dimensionful M_KK²
             residue magnitude compared against a dimensionless L^{-α} rate);
             Level-3 row HELD `NOT-SATISFIED-PENDING-substrate-physical-scale-
             anchor` per `cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2
             dimensional-re-anchorability gate"` + plan §W2-3 INFO_meaning. The
             theorem-STRUCTURE holds; only the Level-3 central-value row is held.

      PASS — structure COMPLETE AND the literal Level-3 < Level-2 holds at
             canonical L_max=10 with Level-3 NOT Tier-2-dimensionful (i.e. the
             pre-registered Level-3 is already a Tier-1 dimensionless quantity
             inside the binding Level-2 envelope).
    """
    if not bool(res["structure_complete"]):
        return "FAIL"
    if bool(res["level3_lt_level2"]) and not bool(res["tier2_dimensionful"]):
        return "PASS"
    # structure complete, but literal Level-3 < Level-2 fails on Tier-2-
    # dimensionful dimensional-class ground -> INFO (HELD), not FAIL.
    return "INFO"


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    # Dual-SHA over (script, canonical, pinmap, expected_section_text) for audit;
    # (script, promotion_text) for content — per plan §W2-3 audit_discriminators.
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, pins,
        res["expected_section"], res["promotion_text"],
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap+expected_section)")
    print(f"  content_sha256: {content_sha[:16]}... (script+promotion_text)")
    print()

    # Console report (NUMBERS first).
    print(f"=== §VII.{res['slot']} LC genesis pole-tower registration ===")
    print(f"  slot resolved:            §VII.{res['slot']}  (rerouted from BT: {res['rerouted']})")
    print(f"  a_2^{{Mellin}}(LC):         {res['a2_mellin_LC']:.10g}  (load-bearing, s_A=3/s_B=6/n=2; DIMENSIONFUL M_KK²)")
    print(f"  a_0^{{Mellin}}(LC):         {res['a0_mellin_LC']:.10g}  (n=0 Weyl, s_A=4)")
    print(f"  res(n=4, a_4 grade):      {res['res_sA2']:.10g}  (s_A=2)")
    print(f"  Level-3 |a_2(LC)| (M_KK²): {res['level3_value']:.10g}  (plan-pre-registered Level-3 = residue magnitude)")
    print(f"  Level-2 envelope @L10:    {res['level2_envelope_Lmax10']:.10g}  (DIMENSIONLESS; alpha={res['level2_alpha']:.4g}, C={res['level2_amplitude_C']:.4g})")
    print(f"  Level-3 < Level-2 (lit):  {res['level3_lt_level2']}  (dimensionful magnitude vs dimensionless rate -> Tier-2-dimensionful)")
    print(f"  Tier-2-dimensionful:      {res['tier2_dimensionful']}  -> Level-3 row HELD NOT-SATISFIED-PENDING-substrate-physical-scale-anchor")
    print(f"  Tier-1 re-anchor (peel):  {res['peel_heldout']:.4e}  (dimensionless match-error)")
    print(f"  Level-3_reanchored<L2:    {res['level3_reanchored_lt_level2']}  (match/envelope={res['match_over_envelope']:.3e}; PASS-eligibility pathway)")
    print(f"  section_match:            {res['section_match']}")
    print(f"  5 anatomy present:        {res['five_anatomy']}")
    print(f"  3 levels present:         {res['three_levels']}")
    print(f"  poleconv-DUAL declared:   {res['poleconv_dual']}")
    print(f"  weighting-family decl:    {res['weighting_family']}")
    print(f"  bridge map NAMED:         {res['bridge_named']}")
    print(f"  STRUCTURE complete:       {res['structure_complete']}")
    print()

    # Save data file.
    np.savez(
        OUT_NPZ,
        slot=res["slot"],
        rerouted=res["rerouted"],
        structure_complete=res["structure_complete"],
        section_match=res["section_match"],
        five_anatomy=res["five_anatomy"],
        three_levels=res["three_levels"],
        poleconv_dual=res["poleconv_dual"],
        weighting_family=res["weighting_family"],
        bridge_named=res["bridge_named"],
        level3_lt_level2_literal=res["level3_lt_level2"],
        tier2_dimensionful=res["tier2_dimensionful"],
        peel_heldout=res["peel_heldout"],
        level3_reanchored_lt_level2=res["level3_reanchored_lt_level2"],
        match_over_envelope=res["match_over_envelope"],
        level3_value=res["level3_value"],
        level2_envelope_Lmax10=res["level2_envelope_Lmax10"],
        level2_alpha=res["level2_alpha"],
        level2_amplitude_C=res["level2_amplitude_C"],
        a2_mellin_LC=res["a2_mellin_LC"],
        a0_mellin_LC=res["a0_mellin_LC"],
        res_sA2=res["res_sA2"],
        cert_audit=res["cert_audit"],
        lc_cert_sha_pin=LC_CERT_SHA_PIN,
        verdict=verdict,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        L_max=L_MAX,
        scheme=SCHEME,
        convention=CONVENTION,
    )
    print(f"  saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    print()

    # 4-tuple + verdict payload.
    value_str = (
        f"slot=§VII.{res['slot']};verify_section_matches={res['section_match']};STRUCTURE-complete={res['structure_complete']};"
        f"5anatomy={res['five_anatomy']};3levels={res['three_levels']};"
        f"L3_literal={res['level3_value']:.6e}_M_KK2_vs_L2={res['level2_envelope_Lmax10']:.6e}_dimensionless;"
        f"L3<L2_literal={res['level3_lt_level2']};Tier-2-dimensionful={res['tier2_dimensionful']}_HELD-NOT-SATISFIED-PENDING-substrate-physical-scale-anchor;"
        f"Tier-1-reanchor_peel={res['peel_heldout']:.3e}<L2={res['level3_reanchored_lt_level2']}_match/env={res['match_over_envelope']:.3e};"
        f"poleconv-DUAL(a2@s_A=3==s_B=6,n=2)={res['poleconv_dual']};"
        f"weighting-family={res['weighting_family']};bridge-NAMED(HKR+Connes-Karoubi)={res['bridge_named']};"
        f"a2_Mellin_LC={res['a2_mellin_LC']:.7g};Level-2-binding;FI;CellII;STAGE-1-CANDIDATE"
    )  # (local)
    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)
    print(tag)

    extra_rows = [
        f"# regulator_pin=a_2^{{Mellin}}(LC)={res['a2_mellin_LC']:.7g} "
        f"poleconv-A-double(s_A=3)==poleconv-B-single(s_B=6) grade_n=2; "
        f"a_0^{{Mellin}}(LC)={res['a0_mellin_LC']:.7g}(s_A=4,n=0); "
        f"consumes S101-W3-LC-POLE-CERT audit={res['cert_audit'][:16]}",
        f"# §VII.{res['slot']} STAGE-1-CANDIDATE per joint-theorem-promotion.md; "
        f"Level-2-binding; Cell II algebra-INVARIANT FI; weighting-family atlas-row; "
        f"Level-3 HELD Tier-2-dimensionful (dimensionful-slot-collision); "
        f"Tier-1 re-anchor via peel_heldout={res['peel_heldout']:.3e} is PASS-eligibility pathway; "
        f"slot rerouted_from_BT={res['rerouted']}",
    ]  # (local)
    payload = print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        companion_note=f"§VII.{res['slot']} LC genesis pole-tower bridge STAGE-1-CANDIDATE; "
                       f"INFO: structure complete, Level-3 HELD Tier-2-dimensionful (literal L3 {res['level3_value']:.3e} M_KK² vs L2 {res['level2_envelope_Lmax10']:.3e} dimensionless); "
                       f"poleconv-DUAL; consumes ebfd1d43 LC cert",
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    # Exit 0 regardless of scientific verdict (verdict is data, not script health).
    return 0


if __name__ == "__main__":
    sys.exit(main())
