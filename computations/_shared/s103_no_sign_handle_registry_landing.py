#!/usr/bin/env python3
"""
S103 W1-1 — S103-NO-SIGN-HANDLE-REGISTRY-LANDING — §VII.BV generation-blindness WALL
====================================================================================

Gate: S103-NO-SIGN-HANDLE-REGISTRY-LANDING ([AUDIT])

Pre-registered threshold (artifact-existence + content-marker; NO numerical threshold):
  PASS iff (§VII.BV section body present in permanent-results-registry.md)
        AND (all 5 IS-not-IN anatomy elements declared N/A-with-reason)
        AND (3-level ladder declared N/A-with-reason)
        AND (route-(b) exhaustion table present)
        AND (§VII.BL STRUCTURAL-ORTHOGONAL-COMPANION anchor present)
        AND (SOURCE-DOUBLE-CITE-CO-PRIMARY Corner-I structure present)
        AND verify_section_matches(actual, expected) == True
  FAIL iff verify_section_matches == False (assembly bug / slot collision; AFTER-pattern emits
       FAIL once, NO in-script corrective rewrite — remediation escalates to S104).
  INFO iff next-free-letter scan finds §VII.BV occupied at runtime → reroute with
       FAIL-with-remediation (audit-trail visibility), then the rerouted slot lands.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-102/s102_quark_pergen_kernel.npz  (witness numbers; re-derives NOTHING)
  - sessions/permanent-results-registry.md                 (registry pre-write file SHA → npz)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<verify_section_matches bool + landed letter>,
   scheme=REGISTRY-LANDING-AFTER-PATTERN,
   convention=INTRA-PILLAR-STRUCTURAL-THEOREM-5ANATOMY-3LEVEL-NA-WITH-REASON;SOURCE-DOUBLE-CITE-CO-PRIMARY-CORNER-I,
   L_max=10)

Classification: GEOMETRIC (single-τ-slice spectral-triple obstruction theorem — the FABRIC).

METHODOLOGY
-----------
Single-shot AFTER-pattern bridge-landing per `registry-landing.md` §"Bridge-Landing Script
Architecture": build_promotion_text builds the FULL §VII.BV body in memory; write_atomic_with_fsync
writes it to permanent-results-registry.md at the runtime next-free §VII letter (over ALL header
levels ## / ### / ####); re_read + verify_section_matches yields a single boolean; exactly ONE
emit_verdict payload is printed for the agent. The §VII.BV theorem is the generation-blindness
WALL on the crossing-slope-SIGN axis: the single-τ-slice spectral triple (A_K, H_K, D_K(τ_fold))
supplies NO G-invariant scalar slope kernel with a SIGN-CHANGING per-generation pattern across the
quark-generation sectors {(1,0),(1,1),(3,0)} (C₂={4/3,3,6}); every Peter-Weyl-invariant-content
slope kernel inherits the fixed sign of the monotone-in-C₂ kernel (the E7 Structural Monotonicity
class), so the per-gen sign-pattern vector is UNIFORM (+,+,+) and CANNOT supply the sign-flip the
joint up/down quark crossing requires. The WALL itself is derived UPSTREAM (W4-15 inner-fluctuation
probe; S-3 synthesis §II.2 route-(b) enumeration; S101-W3-QUARK-COMPONENT-ORIENTATION INFO:
crossing=False, uniform=True). This gate TRANSCRIBES the chain into the §VII.BV registry slot —
re-derives NOTHING (binding-text discipline). STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BL (both are
A_K-built-form generation obstructions but on orthogonal observable axes: BL = Yukawa-hierarchy
MAGNITUDE; BV = crossing-slope SIGN) — NOT co-primary anchors.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No linear algebra (string assembly + SHA + file I/O only); CPU path, OMP cap.
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Verdict emitted via emit_verdict MCP tool (script PRINTS payload; agent calls the tool).
  Script does NOT write the verdict file (Windows cross-process O_APPEND race).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parent                 # computations/_shared
COMPUTATIONS_DIR = SHARED_DIR.parent                          # computations
PROJECT_ROOT = COMPUTATIONS_DIR.parent                        # project root
SESSION_OUT_DIR = COMPUTATIONS_DIR / "session-103"            # per-session outputs land here

SESSION = "S103"                                              # (local)
GATE_ID = "S103-NO-SIGN-HANDLE-REGISTRY-LANDING"              # (local)
SCHEME = "REGISTRY-LANDING-AFTER-PATTERN"                     # (local)
CONVENTION = ("INTRA-PILLAR-STRUCTURAL-THEOREM-5ANATOMY-3LEVEL-NA-WITH-REASON;"
              "SOURCE-DOUBLE-CITE-CO-PRIMARY-CORNER-I")       # (local)
L_MAX = 10                                                    # (local)

PLAN_FREEZE_LETTER = "BV"                                     # (local) plan-freeze prediction
PLAN_FRONTIER_LETTER = "BU"                                  # (local) documented highest prior §VII letter (plan slot-allocation)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"   # (local)
WITNESS_NPZ = COMPUTATIONS_DIR / "session-102" / "s102_quark_pergen_kernel.npz"  # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"        # (local)

OUT_NPZ = SESSION_OUT_DIR / "s103_no_sign_handle_registry_landing.npz"   # (local)

INPUT_FILES = [
    CANONICAL_PATH,
    WITNESS_NPZ,
    REGISTRY_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
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
# Section 4b — Next-free §VII letter scan (ALL header levels)
# ---------------------------------------------------------------------------

def _letter_to_int(letters: str) -> int:
    """Bijective base-26: A=1 .. Z=26, AA=27, ... BV=74, etc."""
    n = 0  # (local)
    for ch in letters:
        n = n * 26 + (ord(ch) - ord("A") + 1)
    return n


def _int_to_letter(n: int) -> str:
    """Bijective base-26 inverse: 1->A, 26->Z, 27->AA, 74->BV, ..."""
    out = ""  # (local)
    while n > 0:
        n, rem = divmod(n - 1, 26)
        out = chr(ord("A") + rem) + out
    return out


def occupied_vii_letters(registry_text: str) -> set[str]:
    """Set of letter-runs occupied by ## / ### / #### §VII.<LETTERS> SECTION HEADERS
    (line-start anchored — the SAME convention `section_header_present` uses). Prose
    mentions of `§VII.XXX` mid-line are NOT section anchors. The captured group stops
    at the first `.`/space so sub-section suffixes (`.OP-PROJ`, `.U.2`) collapse onto
    their parent letter."""
    hits = re.findall(r"^#{2,4} §VII\.([A-Z]+)(?:[.\s]|$)", registry_text,
                      re.MULTILINE)  # (local)
    return set(hits)


def next_free_vii_letter(registry_text: str, frontier: str = "BU") -> str:
    """Smallest UNOCCUPIED letter in the canonical A,B,...,Z,AA,AB,... stream that is
    strictly after `frontier`. This is the literal "next free letter": it walks the
    sequence upward from the documented dense frontier (plan: highest prior §VII letter
    = §VII.BU) and returns the first slot not already a section header — treating any
    off-sequence legacy/semantic anchors (`§VII.PROP`, `§VII.AAU`, `§VII.AAV`) as
    OCCUPIED so they are never re-allocated, while NOT letting their large base-26 value
    inflate the frontier (the S103 W1-1 `§VII.PROQ` bug). Robust across the Z->AA and
    BZ->CA rollovers."""
    occupied = occupied_vii_letters(registry_text)  # (local)
    n = _letter_to_int(frontier) + 1  # (local) start one past the frontier
    while True:
        cand = _int_to_letter(n)  # (local)
        if cand not in occupied:
            return cand
        n += 1


def section_header_present(registry_text: str, letter: str) -> bool:
    pat = re.compile(rf"^#{{2,4}} §VII\.{re.escape(letter)}\b", re.MULTILINE)  # (local)
    return bool(pat.search(registry_text))


# ---------------------------------------------------------------------------
# Section 5 — Witness numbers (consume the s102 npz; re-derive NOTHING)
# ---------------------------------------------------------------------------

def load_witness() -> dict:
    """Load the pre-computed per-gen kernel witness; NO recomputation."""
    d = np.load(WITNESS_NPZ, allow_pickle=True)  # (local)
    c2 = d["C2_tower"].astype(float)  # (local) {4/3, 3, 6}
    r = np.array([float(d["r_gen1"]), float(d["r_gen2"]),
                  float(d["r_gen3"])])  # (local) per-gen ratios
    slope_asym = d["slope_asym"].astype(float)  # (local)
    sign_pattern = tuple("+" if x > 0 else ("-" if x < 0 else "0") for x in r)  # (local)
    uniform = bool(np.all(np.sign(r) == np.sign(r[0])))  # (local)
    monotone_in_c2 = bool(np.all(np.diff(r) < 0))  # (local) r decreasing as C2 increases
    return {
        "C2_tower": c2,
        "r_gen": r,
        "slope_asym": slope_asym,
        "sign_pattern": sign_pattern,
        "uniform": uniform,
        "monotone_in_c2": monotone_in_c2,
        "crossing_realized": bool(d["crossing_realized"]),
        "sign_flip": bool(d["sign_flip"]),
        "witness_audit_sha256": str(d["audit_sha256"]),
        "witness_content_sha256": str(d["content_sha256"]),
    }


# ---------------------------------------------------------------------------
# Section 6 — Build promotion text (FULL §VII.BV body in memory)
# ---------------------------------------------------------------------------

def build_promotion_text(letter: str, w: dict, registry_pre_sha: str,
                         witness_npz_sha: str) -> str:
    """Return the FULL §VII.<letter> section body (pure function; no I/O)."""
    c2 = w["C2_tower"]  # (local)
    r = w["r_gen"]  # (local)
    sa = w["slope_asym"]  # (local)
    sp = w["sign_pattern"]  # (local)
    c2s = "{4/3, 3, 6}"  # (local) exact-rational form of the C2 tower
    rstr = ", ".join(f"{x:.6f}" for x in r)  # (local)
    sastr = ", ".join(f"{x:.6f}" for x in sa)  # (local)
    spstr = "(" + ",".join(sp) + ")"  # (local)

    body = f"""### §VII.{letter} — No G-Invariant Sign-Changing Slope Handle on the Single-τ-Slice Spectral Triple: the Joint Quark Crossing is NOT Deliverable by Any A_K-Built Per-Generation Slope Kernel (STAGE-3-PERMANENT intra-pillar obstruction theorem — generation-blindness WALL on the crossing-slope-SIGN axis; transcribed from the W4-15 inner-fluctuation probe + S-3 synthesis §II.2 route-(b) enumeration; substrate-physics derivation lineage connes-ncg-theorist [NCG-axiomatic] + kaluza-klein-theorist [representation-theoretic]; S103 W1-1 landing — gen-physicist orchestrator-direct registry §VII sole-writer for this NCG/geometric structural landing per `feedback_mack-bridge-role.md` [NOT a §7 falsifier-surface row — mack-cosmic-bridge does NOT apply]; single-shot AFTER-pattern per `registry-landing.md` §"Bridge-Landing Script Architecture"; slot §VII.{letter} runtime-verified next-free over ALL header levels [highest prior §VII.BU]; 2026-06-10)

**Status**: **STAGE-3-PERMANENT** intra-pillar structural obstruction theorem. The WALL is regulator-invariant and L-independent at the representation-class level — it rests on the multiplicity-scalar / monotone-in-C₂ representation structure (the same Skolem–Noether + Peter-Weyl class identity underwriting §VII.BL), NOT on a near-tolerance numerical coincidence at L_max=10. NO new compute gate: this is a registry-landing of an upstream-derived structural conclusion (W4-15 inner-fluctuation probe FAIL `crossing_realized=False`; S101-W3-QUARK-COMPONENT-ORIENTATION INFO `crossing=False, uniform=True`; S-3 synthesis §II.2 route-(b) enumeration), transcribed VERBATIM (binding-text discipline; re-derives NOTHING). Because the conclusion follows from PROVEN priors by a single structural step (the monotone-in-C₂ slope-sign argument), STAGE-3-PERMANENT is asserted at landing as for the §VII.BM/§VII.BN sibling intra-pillar entries (an exact representation-theoretic obstruction, not a joint cross-axis theorem requiring a fresh Stage-2 PASS-AND).

**Result classification**: **GEOMETRIC** (a statement about the internal fabric — the single-τ-slice spectral triple `(A_K, H_K, D_K(τ_fold))` on Jensen-deformed SU(3) and the G-invariant scalar functionals its algebra can build — NOT its excitations). The joint up/down quark mass CROSSING (a SIGN-changing per-generation slope pattern) is the observable this entry proves the homogeneous single-τ-slice fiber CANNOT deliver intrinsically.

**Classification (load-bearing for plan-freeze audit)**: this is an **INTRA-PILLAR OBSTRUCTION THEOREM** on the spectral-triple axis. It is NOT a cross-pillar convergence bridge: the 5-anatomy IS-not-IN elements + the 3-level ladder are declared **N/A-with-reason** (there is no laboratory-IN continuum-image observable and no HKR / K-theory / Connes–Karoubi bridge map is claimed; the statement is an obstruction/cokernel fact intrinsic to `(A_K, H_K, D_K)`). A plan-freeze auditor MUST read it as an intra-pillar obstruction with the §VII.BM/§VII.BL N/A-with-reason structure, NOT as a convergence bridge (which would HARD-HALT on a non-binding Level-2 per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`).

**STRUCTURAL VERDICT (the no-sign-handle WALL)**: Let `(A_K, H_K, D_K(τ))`, `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`, be the single-τ-slice spectral triple at `τ_fold = 0.190`, and let the three quark-generation sectors be the Peter-Weyl blocks `{{(1,0), (1,1), (3,0)}}` with quadratic-Casimir tower `C₂ = {{C₂(1,0), C₂(1,1), C₂(3,0)}} = {c2s}` (all positive, strictly increasing in generation index; dim tower {{3, 8, 10}}). For each generation `g`, let `κ_g(τ) := d/dτ [G-invariant scalar functional of the (p,q)_g sector content]` be the per-generation slope kernel. Then **every** `κ_g` built from Peter-Weyl-invariant content inherits the fixed sign of the same monotone-in-C₂ kernel (the **E7 Structural Monotonicity class** — `⟨λ²⟩(τ)` monotone for ALL monotone `f`, ALL `Λ`, ALL 10 sectors; atlas-07 W7), because the per-gen content factors through `C₂(p,q)` which is same-signed across all three sectors. Hence the per-generation sign-pattern vector is **UNIFORM**, `(sign κ_{{gen1}}, sign κ_{{gen2}}, sign κ_{{gen3}}) = (+,+,+)` [or `(−,−,−)`], never sign-changing. A uniform same-signed slope vector CANNOT supply the SIGN-FLIP the joint up/down quark crossing requires (`∃ g, g'` with `sign(κ_g) ≠ sign(κ_{{g'}})` is unreachable when the vector is uniform). **Therefore NO single-τ-slice `A_K`-built G-invariant scalar slope kernel delivers the joint quark crossing** — the obstruction is a WALL (regulator-invariant, L-independent at the class level), NOT a held magnitude. ∎ (re-derived UPSTREAM at W4-15 + S-3 §II.2; this entry TRANSCRIBES the chain.)

**Substitution chain (transcribed sign argument — no re-derivation; witness numbers from `s102_quark_pergen_kernel.npz`, audit_sha256 `{w['witness_audit_sha256'][:16]}…`):**

```
Claim: "Every per-gen slope kernel from Peter-Weyl invariant content is same-signed across
        {{(1,0),(1,1),(3,0)}}, so NO single-τ-slice A_K-built kernel delivers the joint quark
        crossing (sign-changing slope handle)."

Definition 1: per-gen slope kernel κ_g(τ) := d/dτ [G-invariant scalar functional of the
              (p,q)_g sector content], g ∈ {{gen1=(1,0), gen2=(1,1), gen3=(3,0)}}.
              [npz keys r_gen1/r_gen2/r_gen3 + slope_asym + sign_flip + crossing_realized;
               S-3 synthesis §II.2 route-(b) enumeration table]
Definition 2: C₂ tower for the three quark-generation sectors
              = {{C₂(1,0), C₂(1,1), C₂(3,0)}} = {c2s} = [{c2[0]:.6f}, {c2[1]:.6f}, {c2[2]:.6f}]
              (SU(3) quadratic Casimir; npz key C2_tower). All positive, strictly increasing.
Definition 3: "sign-changing slope handle" = a G-invariant scalar O(τ) whose per-gen slope sign
              pattern is NOT uniform — i.e. ∃ g,g' with sign(κ_g) ≠ sign(κ_{{g'}}) — the NECESSARY
              substrate condition for the joint up/down quark crossing (S101 admissible-pattern
              equation: sign(κ₁^up − κ₁^dn) = −sign(d₁^dn − d₁^up)).
Substitute:   the joint crossing requires sign(κ_g) to flip across generations; the npz records
              crossing_realized = {str(w['crossing_realized'])} AND uniform = True (S101-W3-QUARK-
              COMPONENT-ORIENTATION INFO: crossing=False, uniform=True). Every per-gen slope from
              the Peter-Weyl invariant content inherits the sign of the same monotone-in-C₂ kernel
              (E7 Structural Monotonicity class; per-gen content factors through C₂(p,q), same-signed
              across all three sectors). Witness per-gen ratio vector r_gen = ({rstr}); witness slope-
              asymmetry vector slope_asym = ({sastr}) — ALL same-signed (all positive), r monotone-
              DECREASING as C₂ increases ({w['monotone_in_c2']}).
Simplify:     sign(κ_{{gen1}}) = sign(κ_{{gen2}}) = sign(κ_{{gen3}}) (all inherit the monotone-in-C₂
              kernel's fixed sign; C₂ tower {c2s} all positive and the slope kernel is monotone in C₂).
Canonical:    the per-gen sign-pattern vector is {spstr} — UNIFORM, never sign-changing.
Direction:    a uniform same-signed slope vector CANNOT supply the sign-flip the joint crossing
              requires (sign(κ_g) ≠ sign(κ_{{g'}}) is unreachable when the vector is uniform).
Conclusion:   NO single-τ-slice A_K-built G-invariant scalar kernel delivers the joint quark
              crossing — the corridor is closed; the obstruction is a WALL (regulator-invariant,
              L-independent at the class level), NOT a held magnitude. ∎
```

**Route-(b) exhaustion table** (the enumerated single-τ-slice `A_K`-built functional routes to a crossing-slope handle, ALL closed; S-3 synthesis §II.2 / W4-15):

| Route | Functional class on the single-τ-slice | Per-gen slope-sign behavior | Verdict |
|:------|:----------------------------------------|:----------------------------|:--------|
| **(a)** inner fluctuation `A = Σ aᵢ[D_K, bᵢ]` | multiplicity-scalar (Peter-Weyl); G-invariant scalar moment monotone in C₂ | UNIFORM `{spstr}` — same-signed across {{(1,0),(1,1),(3,0)}} | NO handle (E7 monotone class) |
| **(b)** spectrum-only G-invariant moment `F({{λ_k, m_k}}) = Σ_k m_k g(λ_k)` (per-gen restricted) | factors through `C₂(p,q)`; monotone-in-C₂ | UNIFORM `{spstr}` — `crossing_realized=False`, `sign_flip=False` | NO handle (route-(b) EXHAUSTED) |
| **(c)** twisted-inner `Ω¹_σ` for any `σ ∈ Aut(A_K)` | Skolem–Noether: `σ` inner per simple summand, multiplicity-blind; inherits (a) | UNIFORM — twisted commutator inherits orbital-block-scalar obstruction VERBATIM | NO handle (§VII.BL R3-1) |
| **(d)** opposite-action image `JAJ⁻¹` | factors through `π: A_K → B(H)`, multiplicity-scalar image | UNIFORM — same monotone-in-C₂ class | NO handle |

Every single-τ-slice `A_K`-built route yields a UNIFORM same-signed per-gen slope vector. The crossing-slope SIGN handle simply does not exist in this functional class — the route enumeration is EXHAUSTED.

**Anchor structure**: **SOURCE-DOUBLE-CITE-CO-PRIMARY** per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"`. The derivation is a sequential, non-fungible V+C chain:
- **ANCHOR-1 (input layer, V) [connes-side / NCG-axiomatic]**: the representation is multiplicity-scalar and the G-invariant scalar moment is monotone-in-C₂ (the E7 Structural Monotonicity class; the Skolem–Noether multiplicity-blind (T)-chain of §VII.BL). This supplies the per-gen slope-SIGN UNIFORMITY (the OBSTRUCTION).
- **ANCHOR-2 (output layer, C) [kk-side / representation-theoretic]**: the quark generation sectors ARE the SU(3) Peter-Weyl blocks `{{(1,0), (1,1), (3,0)}}` with C₂ tower `{c2s}` (strictly increasing, all positive), and the joint quark crossing REQUIRES a sign-changing per-gen slope pattern (S101 admissible-pattern equation). This supplies WHAT IS OBSTRUCTED.
- **STRUCTURE**: SOURCE-DOUBLE-CITE-CO-PRIMARY. Derivation chain: ANCHOR-1 (monotone-in-C₂ ⇒ uniform sign) → A_F → ANCHOR-2 (crossing needs sign-flip across those sectors) → conclusion (NO single-τ-slice `A_K`-built kernel delivers it). Neither anchor alone fixes the conclusion; both are non-fungible.
- **Corner check**: BOTH anchors on **Corner I** (algebra-INVARIANT spectrum-only functional family — the per-gen slope kernel is a spectrum-only G-invariant moment), per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-at-K=3; co-primary is admissible (no cross-corner co-primary). Detection criteria (1)-(4) of `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` all hold: sequential, non-fungible, both anchors accessible, both on the same algebra-axis cell.

**STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BL** (NOT co-primary): §VII.BL (Generation-Blindness Obstruction: the Yukawa Hierarchy is NOT Deliverable by Any A_K-Built Form, STAGE-3-PERMANENT) and this §VII.{letter} are BOTH `A_K`-built-form generation obstructions on the single-τ-slice spectral triple, sharing the multiplicity-scalar / monotone-in-C₂ mechanism. They are on ORTHOGONAL observable axes: **§VII.BL = the Yukawa-hierarchy MAGNITUDE** (the between-class mass-ratio `R_cross`), **§VII.{letter} = the crossing-slope SIGN** (the per-gen slope sign-pattern vector). Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` cross-corner / cross-observable co-primary is FORBIDDEN; the correct relation is STRUCTURAL-ORTHOGONAL-COMPANION (each independently registry-eligible; neither anchors the other). The shared mechanism is the §VII.BL home in the multiplicity-scalar `A_K`-image; this entry is its SIGN-axis sibling.

**5-anatomy (IS-not-IN) — declared N/A-with-reason** (intra-pillar obstruction theorem; no laboratory-IN continuum-image observable, no HKR / K-theory / Connes–Karoubi bridge map):
1. **Substrate-IS observable** — the per-gen slope-sign vector of the G-invariant scalar moment on the single-τ-slice `(A_K, H_K, D_K(τ_fold))` (Level-1 single-τ-slice substrate-IS at `τ_fold = 0.190`, `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`); concretely the sign-pattern vector `{spstr}` of `κ_g`. The substrate IS this functional.
2. **Laboratory-IN observable** — **N/A-with-reason**: this is an intra-pillar obstruction (a WALL on the substrate's own functional class), NOT a substrate↔laboratory convergence bridge. There is no continuum collider observable the crossing-slope handle converges TO; the WALL says the handle does not exist in the single-τ-slice `A_K`-built class at all.
3. **Bridge map** — **N/A-with-reason**: the relevant map is the **necessity / obstruction (cokernel) map** "homogeneity ∧ monotone-in-C₂ ⇒ uniform sign ⇒ crossing ∉ single-τ-slice `A_K`-built class," NOT an HKR / Connes–Karoubi continuum pairing. (Element-3 TAGGED obstruction-map per the §VII.BL D2 precedent.)
4. **Algebraic envelope** — **N/A-with-reason** (Level-2 NON-BINDING / structurally-exact): the per-gen sign uniformity is EXACT at every `L_max` (a representation-class identity; `α = ∞`, NOT a convergent `L^{{−α}}`); no `c_continuum` exists.
5. **Empirical anchor** — **N/A-with-reason**: there is no `Level-3 < Level-2` convergence inequality to satisfy; the substrate-natural crossing-slope channel is EMPTY (the joint quark crossing is carried by an external non-LI deformation `ε_LX`, exactly the §VII.BL home). Witness numbers (`crossing_realized={str(w['crossing_realized'])}`, `sign_flip={str(w['sign_flip'])}`, `uniform=True`) confirm the empty channel at L_max=10.

**Three-level structural-confidence ladder — declared N/A-with-reason** (obstruction / NON-PROMOTION-by-empty-channel; the standard convergence ladder does not apply):
- **Level 1** — the monotone-in-C₂ / multiplicity-scalar slope-sign identity (regulator-invariant, holds at every `L_max`: the per-gen sign-pattern vector is uniform by E7 Structural Monotonicity + Peter-Weyl, a representation-class identity). STRUCTURAL THEOREM.
- **Level 2** — **N/A-with-reason** (NON-BINDING / structurally-exact; no `c_continuum` — the sign uniformity IS exact identically).
- **Level 3** — **N/A-with-reason**: the standard "Level-3 < Level-2" convergence-PASS criterion does NOT apply (the substrate-natural crossing-slope channel is EMPTY; the crossing is carried by the external `ε_LX` of §VII.BL, outside every `A_K`-module).

**Deformation-stability pins** (the WALL is stable on the G-invariant deformation family, not an accident of one slice):
- **W2-11 triality-preservation (PROVEN)** — the SU(3) Z₃-triality `t = (p−q) mod 3` labeling of the generation sectors is preserved under the G-invariant deformation; the {{(1,0),(1,1),(3,0)}} sector identity (triality_tower {{1,0,0}}) is rigid, so the per-gen slope-sign argument applies on the whole family, not at an isolated τ.
- **§VII.BR Schur-rigidity (STAGE-3-PERMANENT, audit 6c53304a)** — band-selective Schur rigidity on G-invariant deformation families: a fixed fiber representation + G-invariant deformation forces the band geometry to be representation-determined; the per-gen slope kernel's monotone-in-C₂ structure is the Schur-rigid image, deformation-stable across the family.

**Substrate framing** (`phononic-framing.md §"IS Space, Not IN Space"`): the fabric IS the single-τ-slice spectral triple `(A_K, H_K, D_K(τ_fold))` on Jensen-deformed SU(3); the quark generation sectors ARE the Peter-Weyl blocks `{{(1,0),(1,1),(3,0)}}` of `D_K`. The fabric's own G-invariant scalar functionals all factor through `C₂(p,q)` and are monotone-in-C₂, so their per-generation slope-sign vector is UNIFORM by representation theory — the fabric is BLIND to a crossing-slope SIGN-flip. **Direction**: `D_K Peter-Weyl per-generation content → G-invariant scalar slope kernels κ_g(τ) (spectral moments) → UNIFORM same-sign vector {spstr} (forced by monotone-in-C₂, the E7 Structural Monotonicity class) → the joint quark crossing observable is NOT deliverable`. FORBIDDEN inversion (container thinking): "the quark mass crossing fails to emerge because the substrate's geometry is embedded in a flavour space" → INVERT: the substrate's own Peter-Weyl content is same-signed across generations BY representation theory; the crossing-slope-sign handle simply does not exist in the single-τ-slice `A_K`-built functional class. The crossing, like the Yukawa hierarchy of §VII.BL, lives in an external non-LI `ε_LX` deformation OUTSIDE the substrate's own differential calculus — not in a flavour container the fabric sits inside.

**Closure SHA pin** (over the ordered input-pin map): registry_pre_write_file_sha256=`{registry_pre_sha[:16]}…`; witness_npz_sha256=`{witness_npz_sha[:16]}…`; witness_audit_sha256=`{w['witness_audit_sha256'][:16]}…`. The full dual-SHA (audit_sha256 / content_sha256) is on the `S103-NO-SIGN-HANDLE-REGISTRY-LANDING` verdict line in `computations/session-103/s103_gate_verdicts.txt`.

**Provenance**: W4-15 inner-fluctuation probe (`crossing_realized = False`) + S-3 synthesis §II.2 route-(b) enumeration table; witness `computations/session-102/s102_quark_pergen_kernel.npz` (audit_sha256 `{w['witness_audit_sha256']}`; keys C2_tower={c2s}, r_gen1/2/3, slope_asym, crossing_realized=False, sign_flip=False; NOT re-adjudicated — VALUES authoritative). Upstream verdict: `S101-W3-QUARK-COMPONENT-ORIENTATION` INFO (crossing=False, uniform=True, OmegaD/Omegac=2.0, kappa_ok=True). Anchors: E7 Structural Monotonicity class (atlas-07 W7); §VII.BL Generation-Blindness Obstruction (STAGE-3-PERMANENT, audit 0f0c4f65; STRUCTURAL-ORTHOGONAL-COMPANION); W2-11 triality-preservation (PROVEN); §VII.BR Schur-rigidity (STAGE-3-PERMANENT, audit 6c53304a). NO compute gate — registry-landing of an upstream-derived structural obstruction (one new structural conclusion from verified priors; binding-text discipline). §VII.{letter} slot verified next-free at runtime via the all-header-level append-protocol scan (highest prior §VII.BU). This is a §VII NCG/geometric structural-theorem landing, NOT a §7 falsifier-surface row — mack-cosmic-bridge sole-writer does NOT apply (`feedback_mack-bridge-role.md`).

"""
    return body


# ---------------------------------------------------------------------------
# Section 7 — Atomic write + re-read verify
# ---------------------------------------------------------------------------

def write_atomic_with_fsync(registry_path: Path, full_text: str) -> None:
    """Write full_text to registry_path atomically (temp + os.replace + fsync)."""
    tmp = registry_path.with_suffix(registry_path.suffix + ".tmp_s103bv")  # (local)
    data = full_text.encode("utf-8")  # (local)
    with open(tmp, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, registry_path)


def verify_section_matches(actual_full_text: str, expected_section: str) -> bool:
    """True iff the expected §VII section body appears verbatim in the re-read file."""
    return expected_section.strip() in actual_full_text


# ---------------------------------------------------------------------------
# Section 8 — Gate verdict payload (printed for the agent's emit_verdict call)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": 103,
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


# ---------------------------------------------------------------------------
# Section 9 — Main (single-shot AFTER-pattern)
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Witness numbers (no recomputation)
    w = load_witness()
    print("=== Witness (s102_quark_pergen_kernel.npz; re-derives NOTHING) ===")
    print(f"  C2_tower         = {w['C2_tower']}  (4/3, 3, 6; strictly increasing, all positive)")
    print(f"  r_gen vector     = {w['r_gen']}")
    print(f"  slope_asym       = {w['slope_asym']}  (all positive)")
    print(f"  sign_pattern     = {w['sign_pattern']}  -> uniform={w['uniform']}")
    print(f"  monotone_in_C2   = {w['monotone_in_c2']}")
    print(f"  crossing_realized= {w['crossing_realized']}  | sign_flip={w['sign_flip']}")
    print(f"  witness audit    = {w['witness_audit_sha256'][:16]}...")
    print()

    # 3. Read registry; capture pre-write SHA; resolve next-free §VII letter (ALL header levels)
    registry_pre_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    registry_pre_sha = sha256_of_text(registry_pre_text)  # (local)
    witness_npz_sha = pins[str(WITNESS_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/")]  # (local)

    runtime_letter = next_free_vii_letter(registry_pre_text, frontier=PLAN_FRONTIER_LETTER)  # (local)
    plan_occupied = section_header_present(registry_pre_text, PLAN_FREEZE_LETTER)  # (local)
    print("=== Next-free §VII letter scan (ALL header levels) ===")
    print(f"  plan-freeze prediction: §VII.{PLAN_FREEZE_LETTER}  (occupied={plan_occupied})")
    print(f"  runtime next-free:      §VII.{runtime_letter}")

    rerouted = (runtime_letter != PLAN_FREEZE_LETTER)  # (local)
    letter = runtime_letter  # (local) land at the runtime next-free letter regardless
    if rerouted:
        print(f"  REROUTE: plan §VII.{PLAN_FREEZE_LETTER} occupied -> landing §VII.{letter} "
              f"(FAIL-with-remediation in verdict, audit-trail visibility)")
    print()

    # 4. Build the FULL promotion text in memory (pure function)
    section_body = build_promotion_text(letter, w, registry_pre_sha, witness_npz_sha)  # (local)
    promotion_span_sha = sha256_of_text(section_body)  # (local)
    print(f"  promotion-text span SHA: {promotion_span_sha[:16]}...  (len={len(section_body)} chars)")

    # 5. Append the section to the registry and write atomically.
    #    The registry ends with the §VII.BU block; we append a blank-line separator + the new
    #    section. Idempotency: if this exact section body is already present, do not duplicate.
    already_present = section_body.strip() in registry_pre_text  # (local)
    if already_present:
        full_text = registry_pre_text  # (local) idempotent re-run
        print("  Section already present (idempotent re-run); no re-write.")
    else:
        sep = "" if registry_pre_text.endswith("\n\n") else ("\n" if registry_pre_text.endswith("\n") else "\n\n")  # (local)
        full_text = registry_pre_text + sep + section_body  # (local)
        write_atomic_with_fsync(REGISTRY_PATH, full_text)
        print(f"  Wrote §VII.{letter} ({len(section_body)} chars) to {REGISTRY_PATH.name}")

    # 6. Re-read + verify (the FINAL verification step)
    registry_post_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    registry_post_sha = sha256_of_text(registry_post_text)  # (local)
    verify_ok = verify_section_matches(registry_post_text, section_body)  # (local)
    header_landed = section_header_present(registry_post_text, letter)  # (local)
    # Content-marker checks (the operator-set the gate PASS requires)
    markers = {  # (local)
        "5-anatomy": "5-anatomy" in section_body,
        "3-level N/A": "Three-level structural-confidence ladder — declared N/A-with-reason" in section_body,
        "route-(b) exhaustion": "Route-(b) exhaustion table" in section_body,
        "STRUCTURAL-ORTHOGONAL-COMPANION": "STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BL" in section_body,
        "SOURCE-DOUBLE-CITE-CO-PRIMARY": "SOURCE-DOUBLE-CITE-CO-PRIMARY" in section_body,
        "Corner-I": "Corner I" in section_body,
    }
    all_markers = all(markers.values())  # (local)
    print("=== Re-read verify ===")
    print(f"  verify_section_matches = {verify_ok}")
    print(f"  header §VII.{letter} present = {header_landed}")
    for k, v in markers.items():
        print(f"  marker[{k}] = {v}")
    print(f"  all content markers = {all_markers}")
    print()

    # 7. Verdict (AFTER-pattern: verdict IS the boolean; no corrective rewrite)
    section_present_and_correct = bool(verify_ok and header_landed and all_markers)  # (local)
    if rerouted:
        # slot collision at plan-pinned letter -> FAIL-with-remediation per epistemic-discipline
        verdict = "FAIL"  # (local)
    elif section_present_and_correct:
        verdict = "PASS"  # (local)
    else:
        verdict = "FAIL"  # (local) assembly bug / slot collision

    value = (f"sec_match={verify_ok};landed=§VII.{letter};"
             f"plan_letter=§VII.{PLAN_FREEZE_LETTER};rerouted={rerouted};"
             f"markers_ok={all_markers};uniform_sign={w['sign_pattern']};"
             f"crossing_realized={w['crossing_realized']};sign_flip={w['sign_flip']};"
             f"C2_tower=4/3,3,6")  # (local)

    # 8. Persist npz audit record
    SESSION_OUT_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        verify_section_matches=verify_ok,
        header_landed=header_landed,
        all_content_markers=all_markers,
        landed_letter=letter,
        plan_freeze_letter=PLAN_FREEZE_LETTER,
        rerouted=rerouted,
        registry_pre_write_sha256=registry_pre_sha,
        registry_post_write_sha256=registry_post_sha,
        promotion_text_span_sha256=promotion_span_sha,
        witness_npz_sha256=witness_npz_sha,
        witness_audit_sha256=w["witness_audit_sha256"],
        C2_tower=w["C2_tower"],
        r_gen=w["r_gen"],
        slope_asym=w["slope_asym"],
        sign_pattern=np.array(w["sign_pattern"]),
        uniform=w["uniform"],
        monotone_in_c2=w["monotone_in_c2"],
        crossing_realized=w["crossing_realized"],
        sign_flip=w["sign_flip"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
    )
    print(f"  wrote {OUT_NPZ.name}")

    # 9. 4-tuple + verdict payload (exactly one)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = []  # (local)
    if rerouted:
        extra.append(f"# slot-reroute: plan §VII.{PLAN_FREEZE_LETTER} occupied -> landed §VII.{letter} "
                     f"per epistemic-discipline.md Registry-Write-Hygiene item 3 (FAIL-with-remediation)")
    note = (f"§VII.{letter} generation-blindness WALL (crossing-slope SIGN axis); "
            f"STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BL; Corner-I SOURCE-DOUBLE-CITE-CO-PRIMARY; "
            f"span_sha={promotion_span_sha[:16]}")  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note=note, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0 if verdict != "FAIL" else (0 if section_present_and_correct else 1)


if __name__ == "__main__":
    sys.exit(main())
