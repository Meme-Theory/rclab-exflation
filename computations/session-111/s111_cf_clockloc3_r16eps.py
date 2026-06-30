#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S111 W1-4 S111-CF-CLOCKLOC3-R16EPS — r=16ε layer-obstruction STAGE-1-CANDIDATE landing
=======================================================================================

Gate: S111-CF-CLOCKLOC3-R16EPS ([VERIFY-THEOREM])
Classification: GEOMETRIC

Pre-registered threshold (registration / registry-landing gate — NO numerical scan):
  PASS iff the STAGE-1-CANDIDATE registry entry is written at the runtime-verified
       next-free §VII slot with ALL of:
         (a) clause (a) — Level-2-clock typing
         (b) clause (b) — ε[φ] Level-1-field requirement
         (c) clause (c) — layer-obstruction no-go
         + explicit Level-1 / Level-2 typing
         + the load-bearing distinctness declaration (6th-INDEPENDENT vs structural-ROOT)
         + the STAGE-1-CANDIDATE tag on the theorem-name line
       AND the master-index table row + the section body both re-read-verify True.
  FAIL iff the entry cannot be written / verified, OR the slot collides and reroutes
       (FAIL-with-remediation per registry-landing.md / regulator-pin-discipline.md
       next-free-letter).
  INFO iff registered as STAGE-1-CANDIDATE but the distinctness declaration is left
       OPEN-pending-Stage-2 (deferred 6th-vs-ROOT adjudication).

This gate's PASS is set-membership (clause + typing + distinctness presence), NOT a
numerical comparison. There is no eigenvalue / scan / random-seed.

Single-shot AFTER-pattern (registry-landing.md §"Bridge-Landing Script Architecture",
computations/_bridge_landing_script_template.py):
  build_promotion_text  ->  write_atomic_with_fsync  ->  re_read + verify_section_matches
  ->  emit ONE verdict payload.
The promotion text (table row + section body) is FULLY built in memory before any disk
write; the post-fsync re-read is the FINAL verification step; the verify outcome IS the
verdict; emission is exactly one payload. No conditional rewrite branch (that BEFORE
pattern is what produced the S87 W5 double-trios).

Substrate framing (GEOMETRIC): the r=16ε relation ties the tensor-to-scalar ratio to a
single inflaton field's slow-roll parameter ε=−Ḣ/H². The substrate has no such single
Level-1 field: its clock is τ, the Level-2 Jensen-modulus DEFORMATION coordinate (the
parameter the family {D_K(τ)} is indexed by, upstream of the a₀/a₂/a₄ Seeley-DeWitt
grading); its kinetic energy lives in the a₂-trace-free shear σ²=5τ̇² (a tensor mode),
its potential in V_spec (a₀/a₄). The layer-obstruction is EXACT — a Level-2 deformation
parameter cannot enter a Level-1 single-field consistency relation. Direction preserved:
the obstruction is a substrate-IS layer-type fact, NOT a statement about fields IN a
spacetime container (phononic-framing.md §"IS Space, Not IN Space" + §"Single-τ-slice vs
moduli-deformation substrate-IS levels").

Source: WS-CLOCKLOC (S110, sessions/session-110/workshops/ws-clockloc.md) EMERGENCE-2/3
+ Carry-Forward 3 (ws-clockloc.md:552-559); the 5 VdD-Hawking arguments
(sessions/archive/session-63/session-63-vdd-hawking-workshop.md, V1 / H2-V7.3 / duty-cycle
/ H3-c_s / H7.1-volume-preserving-Jensen). Stage-2 deferred to S112+ (separate gate).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path

_SHARED = _Path(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403  (framework constants; dS_fold, tau_fold, M_KK)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import os
import re
import time

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = _Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S111"                                                   # (local)
GATE_ID = "S111-CF-CLOCKLOC3-R16EPS"                              # (local)
SCHEME = "STAGE-1-CANDIDATE-registration"                         # (local)
CONVENTION = "registry-landing-single-shot-AFTER-pattern"        # (local)
L_MAX = "N/A"                                                     # (local)

REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)

# Documented frontier slot (plan-pinned); the script RE-VERIFIES next-free at write-time.
PLANNED_SLOT_LETTERS = "CG"                                       # (local)
TODAY = "2026-06-21"                                             # (local)

OUT_NPZ = SESSION_DIR / "s111_cf_clockloc3_r16eps.npz"           # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: _Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: _Path, canonical_path: _Path, pins: dict):
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
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Next-free §VII slot verification (ALL header levels)
# ---------------------------------------------------------------------------
def next_free_vii_slot(registry_text: str, start_letters: str) -> tuple[str, bool]:
    """Scan ALL header levels (master-index table rows + ### / #### section bodies)
    for occupied §VII.C? slots; return (next_free_letters, planned_is_free).

    The registry master-index table is NOT alphabetically sorted (CA-CF contiguous then
    legacy out-of-order rows), so we regex EVERY §VII.<letters> token across the whole
    file rather than trusting table position (registry-landing.md / epistemic-discipline.md
    §"Registry-Write Hygiene" item 1).
    """
    occupied = set(re.findall(r"§VII\.([A-Z]{2})\b", registry_text))  # (local) 2-letter slots
    # Walk CA, CB, ... CZ, then DA.. — find the first unoccupied 2-letter C/D slot >= start.
    def _letters_seq():
        for first in "CD":
            for second in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                yield first + second
    seq = list(_letters_seq())  # (local)
    # find first free from the documented frontier forward
    try:
        start_idx = seq.index(start_letters)  # (local)
    except ValueError:
        start_idx = 0  # (local)
    nxt = None  # (local)
    for cand in seq[start_idx:]:
        if cand not in occupied:
            nxt = cand
            break
    planned_free = start_letters not in occupied  # (local)
    return (nxt if nxt else start_letters), planned_free


# ---------------------------------------------------------------------------
# Section 6 — Build promotion text (pure function; NO I/O)
# ---------------------------------------------------------------------------
def build_master_index_row(slot: str) -> str:
    """The single master-index table row, format-matched to §VII.CF (line 168)."""
    return (
        f"| §VII.{slot} | THM | r=16ε Layer-Obstruction (no substrate ε[φ]): the LCDM "
        f"single-field consistency relation r=16ε has NO substrate image because the H-rate's "
        f"clock is the **Level-2** Jensen-modulus deformation coordinate τ (the parameter the "
        f"family {{D_K(τ)}} is indexed BY, upstream of the a₀/a₂/a₄ grading), NOT a **Level-1** "
        f"configuration-space field φ over g_M — and a Level-2 deformation parameter cannot enter "
        f"a Level-1 single-field consistency relation (the layer-type mismatch is EXACT, not "
        f"approximate); the substrate kinetic energy lives in the a₂-trace-free shear σ²=5τ̇² (a "
        f"tensor mode), the potential in V_spec (a₀/a₄), so no single Level-1 field exists whose "
        f"ε=−Ḣ/H² slaves H to its own kinetic energy; **STAGE-1-CANDIDATE** clause-structured "
        f"theorem [(a) Level-2-clock typing, (b) ε[φ] Level-1-field requirement, (c) layer-"
        f"obstruction no-go], joint-clause attribution [Axis-A causal-structure/exact-solution: "
        f"the Level-1/Level-2 typing ∧ Axis-B semiclassical-gravity: the ε=−Ḣ/H² single-field-"
        f"slaving requirement]; DISTINCT FROM the 5 VdD-Hawking r=16ε-inapplicability arguments "
        f"[V1 category-error, H2/V7.3 zero-first-order-tensor, duty-cycle N_e≈0.17, H3 sound-speed "
        f"c_s=0.485, H7.1 volume-preserving-Jensen] — distinctness declaration: structural-ROOT "
        f"(the layer separation each of the 5 PRESUPPOSES; dual-prior 6th-INDEPENDENT 0.40 / "
        f"structural-ROOT 0.60, adjudicated at Stage-2); the exact-solution statement of WHY "
        f"exflation≠inflation (transit of the deformation parameter, not slow-roll of a field); "
        f"Stage-2 two-agent NON-AUTHOR cross-axis PASS-AND queued `CF-S112-CLOCKLOC3-STAGE2` "
        f"[Axis-A causal-structure + Axis-B semiclassical-gravity, verifiers MUST NOT be "
        f"schwarzschild-penrose or hawking]; single-shot AFTER-pattern, slot runtime-verified "
        f"next-free over ALL header levels + master-index table [frontier §VII.CF]; section body "
        f"at §VII.{slot} (S111 W1-4 landing) | schwarzschild-penrose-geometer | {TODAY} |"
    )


def build_section_body(slot: str) -> str:
    """The detailed §VII section body, format-matched to §VII.CF (lines 22197-22211).

    Returns text that BEGINS with a leading blank line (so it appends cleanly after the
    prior section's trailing content at EOF).
    """
    return f"""
### §VII.{slot} — r=16ε Layer-Obstruction: the Inflationary Single-Field Consistency Relation Has No Substrate Image Because the Clock Is a Level-2 Deformation Parameter, Not a Level-1 Field (a Level-2 modulus τ cannot enter a Level-1 single-field consistency relation — the EXACT-solution statement of the 5-argument VdD-Hawking r=16ε inapplicability) (STAGE-1-CANDIDATE clause-structured structural theorem — single-axis-authored layer-obstruction with joint-clause attribution [causal-structure/exact-solution axis ∧ semiclassical-gravity axis]; S110 WS-CLOCKLOC hawking-theorist × schwarzschild-penrose-geometer workshop EMERGENCE-2/3 + Carry-Forward 3, CONVERGED 2026-06-21; S111 W1-4 schwarzschild-penrose-geometer landing; single-shot AFTER-pattern per `registry-landing.md` §"Bridge-Landing Script Architecture"; slot §VII.{slot} runtime-verified next-free over ALL header levels + master-index table [documented frontier §VII.CF]; {TODAY})

**STAGE TAG: STAGE-1-CANDIDATE** (registered S111 W1-4 from the S110 WS-CLOCKLOC workshop EMERGENCE-2/3 convergence — the FROZEN Stage-0 layer-obstruction statement; Stage-2 two-agent NON-AUTHOR cross-axis PASS-AND queued as `CF-S112-CLOCKLOC3-STAGE2` per `joint-theorem-promotion.md` 4-stage pathway — the Stage-2 verifiers MUST NOT be schwarzschild-penrose-geometer or hawking-theorist [original-author exclusion], axis-distinct per the Axis-B Selection Protocol).

**Theorem (S110 WS-CLOCKLOC EMERGENCE-2; S111 W1-4 registration).** The inflationary consistency relation r=16ε (equivalently r=−8n_T) has NO substrate image. The obstruction is a LAYER-TYPE mismatch, EXACT (not approximate): the relation requires the expansion clock to be a Level-1 field; the substrate clock is a Level-2 deformation parameter; a Level-2 parameter cannot enter a Level-1 single-field consistency relation. Formally, NO Level-1 functional ε[φ] exists with φ a configuration-space field over g_M carrying the H-rate, because the H-rate's clock is the Level-2 Jensen modulus τ (a moduli-space coordinate indexing the family {{D_K(τ)}}, not a section over g_M).

**Clause decomposition (joint-clause attribution):**
- **(a) [Axis-A, causal-structure/exact-solution] Level-2-clock typing.** The substrate clock is τ = the Jensen modulus — a **Level-2** moduli-deformation substrate-IS coordinate (the parameter the entire family of spectral triples {{D_K(τ)}} is indexed BY; one must HAVE τ before D_K(τ) and its Seeley-DeWitt grading a₀⊕a₂⊕a₄ can be written, so τ is logically upstream of the grading). This is the `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` Level-2 layer. τ is the substrate-natural clock on substrate-naturalness grounds — dS/dτ = +{dS_fold:.1f} one-signed (the intrinsic evolution coordinate), NOT a Seeley-DeWitt grade. The reparam-invariance check Λ−3H_t²=Λ(1−g'²) (WS-CLOCKLOC R3, Sage) shows H is a slicing-dependent rate while Λ is a curvature scalar — so the physical content is the RELATION among rates, carried by the Level-2 modulus, not a single-rate magnitude on any Level-1 grade.
- **(b) [Axis-B, semiclassical-gravity] ε[φ] Level-1-field requirement.** r=16ε is a single-field slow-roll identity: ε=−Ḣ/H²=(1/2)φ̇²/(3H²M_Pl²) is the slow-roll parameter of a CONFIG-SPACE field φ; r=16ε ties the tensor-to-scalar ratio to the kinetic energy of THAT SAME field (P_T=2H²/(π²M_Pl²) the de Sitter vacuum theorem; P_S=H²/(8π²εM_Pl²) the slaved scalar; their ratio = 16ε). The inflaton φ is a **Level-1** object — a section of a bundle OVER the spacetime g_M, its value at each point a single-τ-slice configuration-space coordinate. The relation REQUIRES a Level-1 clock-field whose ε slaves H to its own kinetic energy.
- **(c) [JOINT — the layer-obstruction no-go] the EXACT mismatch.** The substrate has no single Level-1 field whose ε ties H to its own kinetic energy: the substrate's kinetic energy lives in the a₂-trace-free shear σ²=5τ̇² (a tensor mode, NOT a scalar field), its potential in V_spec (a₀/a₄), and the CLOCK is one layer up — the Level-2 modulus τ. r=16ε REQUIRES a Level-1 clock-field (clause b); the substrate clock is a Level-2 modulus (clause a); a Level-2 deformation parameter cannot enter a Level-1 single-field consistency relation ⇒ no substrate ε[φ] exists ⇒ r=16ε has no substrate image. The mismatch is a LAYER-TYPE fact (moduli-space coordinate vs configuration-space field), hence EXACT — not a parametric suppression. This is the JOINT clause, PASS-AND'd at Stage-2 across both axes (both reviewers must independently PASS the layer-type-mismatch no-go).

**Distinctness declaration (the LOAD-BEARING pre-registration).** This candidate is DISTINCT FROM the 5 existing VdD-Hawking r=16ε-inapplicability arguments (session-63-vdd-hawking-workshop.md): **(1) V1** — S(τ) is the bosonic spectral action Tr f(D_K²/Λ²), not a potential V(φ); ε_geom is a shape invariant, not a kinetic/potential ratio (category error). **(2) H2 / V7.3** — first-order tensor production is ZERO for a homogeneous internal transit (Kasparov factorization U_total=1_M⊗U_K ⇒ β_T=0 EXACT in the product-metric limit A=T=0; ∧ the Weyl-curvature argument: a homogeneous transit produces zero Weyl perturbation and gravitational waves ARE propagating Weyl curvature; the breathing mode is scalar). **(3) duty-cycle / burst** — the transit is N_e≈0.17 e-folds, an impulsive POINT EVENT in the conformal diagram, no sustained quasi-de Sitter phase; CMB-window modes are a SUBSET. **(4) H3 sound-speed** — the Garriga-Mukhanov r=16εc_s with c_s=0.485 (a fiber-only quantity via the π_! shriek map). **(5) H7.1 volume-preserving Jensen** — kills the running of M_Pl (the R2 "devastating" result). DECLARATION: this layer-obstruction is the **structural ROOT** subsuming the 5, NOT (primarily) a 6th independent sibling — each of the 5 PRESUPPOSES the Level-1/Level-2 layer separation (V1's "S(τ) is not V(φ)" is the Level-1 grade-statement of it; H2's "homogeneous ⇒ no Weyl ⇒ no first-order tensor" is the trace/trace-free decomposition at fixed τ; the duty-cycle's "no Level-1 field rolling for >1 e-fold" presupposes the clock is not a Level-1 field; H3/H7.1 are fiber-projection refinements). The WS-CLOCKLOC verdict states it precisely: this is "the exact-solution statement OF the 5-argument VdD-Hawking result" (ws-clockloc.md:469, 481) — an "of" (ROOT) relation, not a sibling. **Dual-prior (the structural claim, adjudicated at Stage-2):** Track-A 6th-INDEPENDENT-argument 0.40 / Track-B structural-ROOT 0.60; the candidate REGISTERS the structural-ROOT claim with the 6th-vs-ROOT adjudication formally deferred to the Stage-2 cross-axis verify.

**5-anatomy + 3-level ladder: N/A-with-reason.** This is an intra-substrate GEOMETRIC layer-type no-go (cf. §VII.CA self-non-bridge precedent), NOT a cross-pillar bridge: there is no laboratory-IN observable and no HKR/Connes-Karoubi bridge map — the obstruction is the ABSENCE of a substrate observable (no ε[φ]), exact at every L_max (the Level-1/Level-2 distinction is a layer-type / cohomology-class-level fact, L-independent). Level-1/Level-2 typing IS the structural content: the obstruction lives at the Level-1 (single-τ-slice configuration field) ↮ Level-2 (moduli-deformation parameter) layer boundary. DISTINCT FROM §VII (S85/S86) "two-layer obstruction" V(Level-1 − Level-2) which is a spectral-action MOMENT difference (5-regulator atlas, lizzi-track) — a numerical magnitude, not the r=16ε clock-field-vs-modulus layer-type no-go.

**Source / provenance:** S110 WS-CLOCKLOC workshop `sessions/session-110/workshops/ws-clockloc.md` (CONVERGED 3 rounds, 2026-06-21) EMERGENCE-2 (ws-clockloc.md:415, 469) + EMERGENCE-3 (ws-clockloc.md:417, 471) + Workshop-Verdict row 5 (ws-clockloc.md:481) + Carry-Forward 3 (ws-clockloc.md:552-559); the 5-argument distinctness source `sessions/archive/session-63/session-63-vdd-hawking-workshop.md` (V1 §32, H2/V7.3 §367/§589, duty-cycle §239, H3 §593, H7.1 §772); the Level-1/Level-2 distinction `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`; the reparam-invariance algebra Λ−3H_t²=Λ(1−g'²) (WS-CLOCKLOC R3, Sage-verified); the one-signed action gradient dS/dτ=+{dS_fold:.1f} at τ_fold={tau_fold} (canonical_constants `dS_fold`, `tau_fold`); `joint-theorem-promotion.md` Stage-0→Stage-1 protocol. **Substrate framing:** the substrate IS the finite spectral triple `(A_K, H_K, D_K(τ))`; τ IS the substrate's intrinsic Level-2 deformation parameter (the family-indexing modulus), NOT a field living IN a spacetime container; r=16ε's clock φ is a Level-1 configuration field over g_M and the substrate simply has no such object — the absence is a substrate-IS layer-type fact, read FROM the moduli structure, not a property of fields propagating in a container (`phononic-framing.md §"IS Space, Not IN Space"`). Direction preserved: `D_K eigenvalues → a_n moments → emergent (a,τ) congruence → measurement`; the r=16ε no-go is the moduli-space-layer statement, never an inversion to fields-in-a-container. **Math-owners / workshop authors (Stage-1 registrants, EXCLUDED from Stage-2 review per the original-author-exclusion clause):** schwarzschild-penrose-geometer (Axis-A causal-structure/exact-solution: the Level-1/Level-2 typing) + hawking-theorist (Axis-B semiclassical-gravity: the ε=−Ḣ/H² single-field-slaving requirement). **Stage-2 reviewers (axis-distinct, original-author-excluded, no-workshop-context — to be dispatched as `CF-S112-CLOCKLOC3-STAGE2`):** Axis-A candidate = einstein-theorist OR kaku-speculative-theorist (causal-structure/exact-solution/GR, NON-author); Axis-B candidate = feynman-theorist OR transit-dynamics-theorist (semiclassical-gravity/perturbation-theory, NON-author). The Stage-2 PASS-AND on the JOINT clause (c) is the 6th-INDEPENDENT-vs-structural-ROOT track-allocation adjudication.
"""


# ---------------------------------------------------------------------------
# Section 7 — Atomic write (single-shot) + re-read verify
# ---------------------------------------------------------------------------
def write_atomic_with_fsync(full_text: str, path: _Path) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(full_text)
        fh.flush()
        os.fsync(fh.fileno())


def verify_clauses_present(section_text: str) -> dict:
    """Strict clause / typing / distinctness / tag presence checks on the section body."""
    checks = {  # (local)
        "clause_a_level2_clock": "(a) [Axis-A, causal-structure/exact-solution] Level-2-clock typing" in section_text,
        "clause_b_eps_level1_field": "(b) [Axis-B, semiclassical-gravity] ε[φ] Level-1-field requirement" in section_text,
        "clause_c_layer_obstruction_nogo": "(c) [JOINT — the layer-obstruction no-go]" in section_text,
        "level1_typing": "Level-1" in section_text,
        "level2_typing": "Level-2" in section_text,
        "distinctness_declaration": ("Distinctness declaration" in section_text
                                     and "structural ROOT" in section_text
                                     and "6th-INDEPENDENT" in section_text),
        "stage1_tag": "STAGE-1-CANDIDATE" in section_text,
        "distinct_keyword": "DISTINCT FROM the 5" in section_text,
        "dual_prior_present": ("0.40" in section_text and "0.60" in section_text),
        "stage2_nonauthor": ("CF-S112-CLOCKLOC3-STAGE2" in section_text
                             and "MUST NOT be schwarzschild-penrose-geometer or hawking-theorist" in section_text),
    }
    return checks


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload (printed; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, l_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={l_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=None) -> dict:
    payload = {  # (local)
        "session": 111,
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 — Main (single-shot AFTER-pattern)
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 2. Read the registry ONCE, verify next-free slot over ALL header levels.
    registry_text = REGISTRY.read_text(encoding="utf-8")  # (local)
    slot, planned_free = next_free_vii_slot(registry_text, PLANNED_SLOT_LETTERS)
    print(f"  planned slot §VII.{PLANNED_SLOT_LETTERS} free={planned_free}; runtime next-free=§VII.{slot}")

    reroute = (slot != PLANNED_SLOT_LETTERS)  # (local)

    # 3. Build promotion text FULLY in memory (pure functions; no I/O).
    index_row = build_master_index_row(slot)        # (local)
    section_body = build_section_body(slot)          # (local)

    # 3a. Insert the master-index row immediately AFTER the §VII.CF master-index table row
    #     (a unique anchor line). Append the section body at EOF.
    cf_row_marker = "| §VII.CF | THM | κ-Sign-Lock ∧ Wodzicki-Parity Joint Foreclosure"  # (local)
    lines = registry_text.split("\n")  # (local)
    cf_row_idx = None  # (local)
    for i, ln in enumerate(lines):
        if ln.startswith(cf_row_marker):
            cf_row_idx = i
            break
    if cf_row_idx is None:
        # anchor missing -> structural defect; do NOT guess. Honest FAIL.
        print("  ANCHOR-MISSING: §VII.CF master-index row not found; cannot place new row.")
        anchor_ok = False  # (local)
        new_registry_text = registry_text  # (local) unchanged
    else:
        anchor_ok = True  # (local)
        new_lines = lines[: cf_row_idx + 1] + [index_row] + lines[cf_row_idx + 1 :]  # (local)
        new_registry_text = "\n".join(new_lines)  # (local)
        # append section body at EOF (build_section_body starts with a leading newline)
        if not new_registry_text.endswith("\n"):
            new_registry_text += "\n"
        new_registry_text += section_body

    # 4. Write atomically + fsync (single write; no conditional rewrite branch).
    slot_collision_fail = reroute  # plan slot occupied at runtime -> FAIL-with-remediation
    wrote = False  # (local)
    if anchor_ok:
        write_atomic_with_fsync(new_registry_text, REGISTRY)
        wrote = True

    # 5. Re-read (FINAL verification step) + verify clause/typing/distinctness presence.
    reread = REGISTRY.read_text(encoding="utf-8")  # (local)
    # isolate the new section body for the clause checks
    sec_anchor = f"### §VII.{slot} — r=16ε Layer-Obstruction"  # (local)
    sec_idx = reread.find(sec_anchor)  # (local)
    section_text = reread[sec_idx:] if sec_idx >= 0 else ""  # (local)
    row_present = (f"| §VII.{slot} | THM | r=16ε Layer-Obstruction" in reread)  # (local)

    clause_checks = verify_clauses_present(section_text)  # (local)
    all_clauses = all(clause_checks.values())  # (local)
    section_landed = (sec_idx >= 0)  # (local)

    # 6. Verdict (the verify outcome IS the verdict; single point of decision).
    #    PASS iff: not slot-collision, anchor ok, row + section landed, all clauses present.
    #    FAIL iff: slot collision (reroute) OR anchor missing OR write/verify failed.
    if slot_collision_fail:
        verdict = "FAIL"  # (local)
        value = (f"PLAN-SLOT-COLLISION_planned_CG_occupied_rerouted_to_{slot}_"
                 f"FAIL-with-remediation_per_registry-landing")
    elif not anchor_ok:
        verdict = "FAIL"  # (local)
        value = "ANCHOR-MISSING_VII-CF-master-index-row-not-found_no-landing"
    elif row_present and section_landed and all_clauses:
        verdict = "PASS"  # (local)
        value = (f"STAGE-1-CANDIDATE_landed_§VII.{slot}_3-clauses+L1-L2-typing+"
                 f"distinctness-declaration-structural-ROOT_dual-prior-0.40-0.60_"
                 f"6th-vs-ROOT-deferred-to-Stage-2_verify-True")
    else:
        verdict = "FAIL"  # (local)
        failed = [k for k, v in clause_checks.items() if not v]  # (local)
        value = (f"VERIFY-FAIL_row_present={row_present}_section_landed={section_landed}_"
                 f"missing_clauses={','.join(failed) if failed else 'none'}")

    # 7. Persist a small npz audit record (optional artifact — clause checklist + slot record).
    try:
        import numpy as np  # (local) tiny record only
        np.savez(
            OUT_NPZ,
            gate_id=GATE_ID,
            slot=f"§VII.{slot}",
            planned_slot=f"§VII.{PLANNED_SLOT_LETTERS}",
            planned_free=planned_free,
            reroute=reroute,
            anchor_ok=anchor_ok,
            wrote=wrote,
            row_present=row_present,
            section_landed=section_landed,
            all_clauses_present=all_clauses,
            clause_checklist=json.dumps(clause_checks),
            verdict=verdict,
            distinctness_track="structural-ROOT (0.60) primary; 6th-INDEPENDENT (0.40) deferred to Stage-2",
            dS_fold=float(dS_fold),     # canonical pin echoed into the record
            tau_fold=float(tau_fold),
        )
        print(f"  npz audit record -> {OUT_NPZ.name}")
    except Exception as e:  # noqa: BLE001
        print(f"  npz record skipped ({e!r})")

    # 8. dual-SHA over (this script + canonical + pinmap). Compute AFTER the write so the
    #    content_sha256 pins the script bytes as run; audit_sha256 pins script+canonical+pins.
    script_path = _Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 9. 4-tuple + payload (single emission).
    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))
    extra = [
        f"# registry_slot=§VII.{slot} planned=§VII.{PLANNED_SLOT_LETTERS} "
        f"reroute={reroute} clauses_present={all_clauses} "
        f"# {GATE_ID} STAGE-1-CANDIDATE registry-landing companion row",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    print(f"    clause checklist: {json.dumps(clause_checks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
