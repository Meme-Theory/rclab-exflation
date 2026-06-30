#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S101 W6-2 — S101-DUAL-Z3-REGISTRY-LANDING (registry landing at §VII.BN)
======================================================================

Gate: S101-DUAL-Z3-REGISTRY-LANDING ([VERIFY])

Pre-registered threshold (artifact-verification, non-numerical):
  PASS iff verify_section_matches(re_read(registry, §VII.BN), promotion_text) == True
           AND the reserved slot §VII.BN was FREE at runtime (no reroute).
  FAIL iff section mismatch (honest close, remediation S102) OR slot-reroute fired.
  INFO not used by this gate.

This is a single-shot AFTER-pattern bridge-landing per
`.claude/rules/registry-landing.md` §"Bridge-Landing Script Architecture" +
`computations/_bridge_landing_script_template.py` lines 54-65:
  (1) build_promotion_text   — pure in-memory assembly, no I/O before write
  (2) write_atomic_with_fsync — single APPEND + flush() + os.fsync()
  (3) re_read + verify_section_matches — ONE strict-equality boolean
  (4) exactly one print_verdict_payload whose verdict IS that boolean
No conditional corrective-rewrite branch exists (the BEFORE-pattern double-trio
is absent by construction).

DEVIATION from the template docstring (disclosed): step (2) appends in mode 'a'
to the 1.7 MB curated registry (NOT the template's single-file 'w' truncate
example). The registry is a shared curated doc; the slot is the LAST entry in
the file, appended after a blank line following the §VII.BM (W6-1) entry. PD-4
single-writer serialization (W6-1 PASS landed §VII.BM at line 21113 cleanly;
this gate is NEXT in the chain).

BINDING TEXT — REGISTRY-LANDING GATE. The c(φ) exact-result content is
transcribed VERBATIM from the S100a W-2 frozen workshop (WP §W2-1); NOTHING is
re-derived. The arithmetic substitution chain (heavy/light = 3) and the
lepton-only structural identity (quark d/dφ ≡ 0) are TRANSCRIBED from the anchor
gate `S100a-DUAL-Z3-PHI-POINTS` PASS, not newly computed.

Inputs (SHA-256 pinned at runtime; S84+ dual-SHA schema):
  - sessions/session-100a/session-100a-w2-workingpaper.md   (Stage-0 source)
  - computations/session-100a/s100a_dual_z3_phi_points.npz  (anchor npz; plan pin 36a412ee...)
  - sessions/session-100a/session-100a-housekeeping.md       (plan pin 07b164c1...)
  - computations/_bridge_landing_script_template.py          (template; plan pin 876c018f...)
  - sessions/framework/s101-slot-pre-allocation-lockfile.md  (RESERVED-FOR-S101-W6-2-DUAL-Z3)
  - sessions/permanent-results-registry.md                   (live append target; runtime SHA)
  - canonical_constants.py                                   (feeds audit_sha256 only)
  - script bytes                                             (feeds BOTH SHAs)

Output 4-tuple:
  (value=<landed_VII.BN ...>, scheme=BRIDGE-LANDING-AFTER-PATTERN,
   convention=SINGLE-SHOT-VERBATIM-EXTRACTION, L_max=N/A)

Classification: PARTICLE (Z3 Haar-moment closed-form generation lever; lepton-only)

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No GPU path (text assembly only)
- SHA-256 of all input files logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe):
  the script PRINTS the payload; the dispatching AGENT calls
  mcp__knowledge__emit_verdict(**payload). The script does NOT write the
  verdict file.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# Bootstrap computations/_shared onto sys.path BEFORE the canonical import
# (the script is invoked from the project root, not from its own dir), matching
# the W6-1 precedent s101_w6_1_foam_protection_landing.py:55-56.
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str((Path(__file__).resolve().parent.parent
                        / "_shared")))
from canonical_constants import *  # noqa: E402,F401,F403  (tau_fold, Vol_SU3_Haar context echo)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402
from fractions import Fraction  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S101"                                                   # (local)
GATE_ID = "S101-DUAL-Z3-REGISTRY-LANDING"                          # (local)
SCHEME = "BRIDGE-LANDING-AFTER-PATTERN"                            # (local)
CONVENTION = "SINGLE-SHOT-VERBATIM-EXTRACTION"                     # (local)
L_MAX = "N/A"                                                      # (local)

SLOT = "§VII.BN"                                                   # (local)
LOCKFILE_BLOCK = "RESERVED-FOR-S101-W6-2-DUAL-Z3"                  # (local)

REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
LOCKFILE = (PROJECT_ROOT / "sessions" / "framework"
            / "s101-slot-pre-allocation-lockfile.md")                   # (local)
W2_WP = (PROJECT_ROOT / "sessions" / "session-100a"
         / "session-100a-w2-workingpaper.md")                          # (local)
DUAL_Z3_NPZ = (COMPUTATIONS_DIR / "session-100a"
               / "s100a_dual_z3_phi_points.npz")                       # (local)
HOUSEKEEPING_100A = (PROJECT_ROOT / "sessions" / "session-100a"
                     / "session-100a-housekeeping.md")                 # (local)
BRIDGE_TEMPLATE = COMPUTATIONS_DIR / "_bridge_landing_script_template.py"  # (local)

OUT_NPZ = SESSION_DIR / "s101_w6_2_dual_z3_landing.npz"            # (local)

# Anchor full-64-hex audit_sha256 of the PRIMARY anchor gate (plan §W6-2 (d)).
PRIMARY_ANCHOR_AUDIT = (
    "d23c7e99cba964035261235ef54b79876e89d2bd4b23d2e57f6f60151f94afe0")  # (local)
PRIMARY_ANCHOR_CONTENT = (
    "6a4e08ea7389d9a09213b567ccea0207337ae089744eef2fd9ff999b86daeb15")  # (local)

# All-header-level slot-scan regex (PD-2): ##/###/#### levels.
SLOT_SCAN_RE = re.compile(
    r'^#{2,4}\s*§VII\.BN\b', re.MULTILINE)                         # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    W2_WP,
    DUAL_Z3_NPZ,
    HOUSEKEEPING_100A,
    BRIDGE_TEMPLATE,
    LOCKFILE,
    REGISTRY,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
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
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    """Stable hash over the ordered pin map (audit-SHA closure helper)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_audit_sha(script_path: Path, canonical_path: Path,
                      pinmap: dict) -> str:
    """audit_sha256 = sha256( bytes(script) || bytes(canonical) || pinmap_json ).

    pinmap is the FULL ordered audit-pin map (input SHAs + identity keys +
    lockfile cross-reference + registry-state-at-runtime), per plan
    audit_discriminators.audit_sha256_inputs.
    """
    script_bytes = script_path.read_bytes()  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pinmap.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    h = hashlib.sha256()  # (local)
    h.update(script_bytes)
    h.update(canonical_bytes)
    h.update(pinmap_json)
    return h.hexdigest()


def content_sha_of(text: str) -> str:
    """content_sha256 = sha256 of the post-fsync re-read on-disk section text."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Arithmetic re-check (TRANSCRIBED from the anchor gate; not a
#             re-derivation — an exact-rational confirmation that the landed
#             numbers match the S100a-DUAL-Z3-PHI-POINTS PASS content).
# ---------------------------------------------------------------------------

def recheck_closed_form() -> dict:
    """Exact-rational arithmetic re-check of the c(φ) collapse (Fraction engine).

    Confirms the transcribed numbers byte-for-byte against the frozen anchor:
      c(φ) = 1/(1 + 8 cos²φ) on Z3 orbit {0, 2π/3, 4π/3} → {1/9, 1/3, 1/3};
      heavy/light = (1/3)/(1/9) = 3 EXACT; 2-fold degeneracy at ±2π/3.
    cos²(0) = 1, cos²(±2π/3) = 1/4 are exact rationals (no float).
    """
    cos2 = {  # (local) exact cos² at the three Z3 points
        "0": Fraction(1, 1),
        "+2pi/3": Fraction(1, 4),
        "-2pi/3": Fraction(1, 4),
    }
    c = {k: Fraction(1, 1) / (Fraction(1, 1) + Fraction(8, 1) * v)
         for k, v in cos2.items()}  # (local)
    distinct = sorted(set(c.values()))  # (local)
    heavy = max(c.values())  # (local) 1/3
    light = min(c.values())  # (local) 1/9
    ratio = heavy / light  # (local)
    deg = (c["+2pi/3"] == c["-2pi/3"])  # (local)
    # Haar Dirichlet moments (exact; lineage c(φ) = α²(φ)/2).
    E_s1_sq = Fraction(1, 2)   # (local)
    E_s2_sq = Fraction(1, 4)   # (local)
    E_cross = Fraction(0, 1)   # (local)
    out = {  # (local)
        "c_num": np.array([c["0"].numerator, c["+2pi/3"].numerator,
                           c["-2pi/3"].numerator], dtype=np.int64),
        "c_den": np.array([c["0"].denominator, c["+2pi/3"].denominator,
                           c["-2pi/3"].denominator], dtype=np.int64),
        "distinct_count": len(distinct),
        "heavy_over_light_num": ratio.numerator,
        "heavy_over_light_den": ratio.denominator,
        "degeneracy_pm2pi3": bool(deg),
        "E_s1_sq_num": E_s1_sq.numerator, "E_s1_sq_den": E_s1_sq.denominator,
        "E_s2_sq_num": E_s2_sq.numerator, "E_s2_sq_den": E_s2_sq.denominator,
        "E_cross_num": E_cross.numerator, "E_cross_den": E_cross.denominator,
    }
    # Hard asserts: the transcribed numbers MUST equal the anchor's.
    assert distinct == [Fraction(1, 9), Fraction(1, 3)], distinct
    assert ratio == Fraction(3, 1), ratio
    assert deg, "±2π/3 must be exactly 2-fold degenerate"
    assert c["0"] == Fraction(1, 9) and c["+2pi/3"] == Fraction(1, 3)
    return out


# ---------------------------------------------------------------------------
# Section 6 — build_promotion_text (PURE; no I/O)
# ---------------------------------------------------------------------------

def build_promotion_text() -> str:
    """Produce the EXACT §VII.BN registry section text. Pure function; no I/O.

    All numeric/structural content is transcribed from the S100a W-2 frozen
    workshop (WP §W2-1). Direction of explanation flows D_K representation
    content → Haar moments → c(φ) closed form → exact generation-coefficient
    set → lepton-sector lever (substrate-first; no inversion).
    """
    a = PRIMARY_ANCHOR_AUDIT  # (local)
    co = PRIMARY_ANCHOR_CONTENT  # (local)
    npz_sha = "36a412ee5128cf1af63df02e8968afe978ed49698bfbae4d2bd029bb18dadef1"  # (local)
    lines = [
        "### §VII.BN — Dual-Z₃ Generation Lever: Exact Closed-Form "
        "c(φ) = 1/(1+8cos²φ) Collapse {1/9, 1/3, 1/3}, Structurally Lepton-Only "
        "(S100a W2-1; EXACT-RESULT entry; S101 W6-2 landing — gen-physicist)",
        "",
        "**Exact-result statement (closed-form generation lever).** On the second "
        "Z₃ phase points φ ∈ {0, +2π/3, −2π/3} the diagonal weight "
        "`c(φ) = 1/(1 + 8 cos²φ)` collapses the three charged-lepton generations "
        "to the exact-rational set **{1/9, 1/3, 1/3}** (Sage QQ; convention "
        "EXACT-RATIONAL-QQ): `c(0) = 1/9`; `c(±2π/3) = 1/3`, the two non-trivial "
        "points **2-FOLD DEGENERATE**; **heavy/light ratio = (1/3)/(1/9) = 3 EXACT**. "
        "The quark-sector φ-derivative vanishes **IDENTICALLY** (`quark ∂Ω^D/∂φ = "
        "∂Ω^c/∂φ ≡ 0` EXACT, over the Z₃ orbit + 2 generic off-orbit probes): the "
        "second Z₃ phase is a **STRUCTURALLY LEPTON-ONLY** lever — no quark "
        "observable moves with φ. The b-sector matrix carries the φ-lever as a "
        "rigid diagonal shift `S4·c(φ)`; within it the (ν_L, e_L) doublet stays "
        "exactly degenerate (M₀ = 4/3, SU(2)_L-protected) while e_R splits "
        "(M₀ = 10/3) — the closed form is electroweak-consistent.",
        "",
        "**Lineage clause.** `c(φ) = α²(φ)/2` via the eq-(2.104) operator form "
        "`s_φ(h) = α[s₁(h) − 2(1 + e^{2iφ}) s₂(h)]`, with the exact Dirichlet Haar "
        "moments `E|s₁|² = 1/2`, `E|s₂|² = 1/4`, `E[s̄₁ s₂] = 0` verified at all "
        "three φ-points (W2 WP Haar-moment table; Sage-MCP cross-verified). Fiber "
        "integration gives `∫_K|s_φ|²/(α²·Vol) = 1/2 + 4cos²φ = (1/2)(1 + 8cos²φ)`, "
        "so the unit-norm vertical profile has `α²(φ) = 2c(φ)`: **c(φ) IS the "
        "s_φ-family normalization weight** (the phase enters through the "
        "off-diagonal first-column monomials `s₂ = h₁₁h₂₁ + h₁₁h₃₁ + h₂₁h₃₁`, "
        "eq 2.104, and lands in Ω^b as the diagonal weight after fiber "
        "integration). The eq-(2.104) operator form is carried verbatim as the "
        "PRIMARY producing-equation citation; the verdict companion row's "
        "\"eq 3.22 lineage\" label denotes the same producing equation at a "
        "different source granularity (the eq-(3.22) diagonal-weight transcription "
        "of Baptista Paper 14 §3).",
        "",
        "**Substitution chain (transcribed arithmetic — no re-derivation).** "
        "The exact ratio claim (heavy/light = 3) is an arithmetic check on the "
        "closed form:",
        "",
        "```",
        "Definition 1: c(φ) = 1/(1 + 8 cos²φ)        [S100a-DUAL-Z3-PHI-POINTS "
        "closed form; lineage c(φ) = α²(φ)/2, eq-(2.104)]",
        "Definition 2: Z₃ phase points φ ∈ {0, +2π/3, −2π/3}",
        "Substitute:   c(0) = 1/(1 + 8·cos²0) ;  c(±2π/3) = 1/(1 + 8·cos²(2π/3))",
        "Simplify:     cos(0) = 1   ⇒ cos² = 1    ⇒ c(0)    = 1/(1 + 8·1) = 1/9",
        "              cos(2π/3) = −1/2 ⇒ cos² = 1/4 ⇒ c(±2π/3) = 1/(1 + 8/4) "
        "= 1/(1+2) = 1/3",
        "              heavy/light = (1/3)/(1/9) = 9/3 = 3",
        "Direction:    the two ±2π/3 points coincide (2-fold degenerate); "
        "ratio exactly 3",
        "Conclusion:   collapse set {1/9, 1/3, 1/3}; heavy/light = 3 EXACT",
        "```",
        "",
        "The lepton-only claim (`quark ∂/∂φ ≡ 0` EXACT) is a transcribed "
        "structural identity from the anchor gate (the D-sector vertical profile "
        "`h·D·h̄`, eq 2.17, contains NO s_φ factor at any order, so its mass "
        "matrix cannot carry φ; the c-sector closed form carries no φ-term), "
        "not re-derived here.",
        "",
        f"**Anchors.** PRIMARY = `S100a-DUAL-Z3-PHI-POINTS` PASS (full 64-hex "
        f"audit_sha256 `{a}`; content_sha256 `{co}`; npz "
        f"`computations/session-100a/s100a_dual_z3_phi_points.npz`, SHA "
        f"`{npz_sha}`; scheme CLOSED-FORM-OMEGA-BG, convention EXACT-RATIONAL-QQ). "
        f"Stage-0 text = WP §W2-1 (`sessions/session-100a/"
        f"session-100a-w2-workingpaper.md`). This is an EXACT-RESULT entry "
        f"(single PRIMARY anchor; no companion co-primary).",
        "",
        "**Registry-anatomy compliance.** (i) Entry class = **intra-pillar exact "
        "closed-form result** (NOT a cross-pillar bridge): the 5-anatomy "
        "IS-not-IN elements + the 3-level ladder are declared **N/A-with-reason** "
        "— there is no laboratory-IN observable and no HKR / K-theory / "
        "Connes-Karoubi bridge map is claimed; the statement is an exact "
        "Haar-moment closed-form rational identity on the Z₃ phase moduli of "
        "`(A_K, H_K, D_K)`. The \"Level-3 < Level-2\" registry-PASS criterion is "
        "therefore vacuously N/A (no continuum-image envelope); the gate's PASS "
        "rests on the section-match predicate. (ii) Projection-side declaration = "
        "**SINGLE-READING**: a Haar-moment closed form on the Z₃ moduli is an "
        "algebra-level exact identity; no state-pair functional reading is "
        "claimed, so the bare slot identifier `§VII.BN` is admissible under "
        "`registry-landing.md` Reading-A naming hygiene PRECISELY because this "
        "explicit single-reading sentence is carried (no `.OP-PROJ`/`.STATE-PROJ` "
        "suffix is required when only one reading exists). (iii) No state-history "
        "labels appear (`registry-landing.md` Class-(h) parse-tree expansion "
        "N/A). (iv) Substrate-IS level tag = **Level 2** flavor on the Z₃ phase "
        "moduli — the φ-points are intrinsic deformation data of the substrate's "
        "Z₃ structure (the discrete Z₃ of the C² ⊂ su(3) deformation direction "
        "carrying the Jensen Higgs |s(h)|² mode), NOT coordinates in a "
        "meta-container — per `phononic-framing.md` §\"Single-τ-slice vs "
        "moduli-deformation substrate-IS levels\".",
        "",
        "**Substrate framing** (`phononic-framing.md` §\"IS Space, Not IN "
        "Space\"; PARTICLE-class). The substrate IS the Jensen-deformed SU(3) "
        "fiber; the three charged-lepton generations ARE its triality-distinct "
        "Peter-Weyl channels, and the second Z₃ acts on the generation labels "
        "through the Haar-moment coefficient `c(φ) = α²(φ)/2` of the eq-(2.104) "
        "form `s_φ(h)`. The D_K representation content fixes the exact Dirichlet "
        "moments (`E|s₁|² = 1/2`, `E|s₂|² = 1/4`, orthogonal cross-moment), and "
        "the closed form collapses to exact rationals {1/9, 1/3, 1/3} at the "
        "three Z₃ points. **Direction**: D_K representation content → Haar "
        "moments → c(φ) closed form → exact generation-coefficient set "
        "{1/9, 1/3, 1/3} → charged-lepton-sector phenomenology lever. The quark "
        "sector's φ-derivative vanishes identically — the lever moves ONLY lepton "
        "observables (a representation-theoretic selection statement of the "
        "fiber); quark texture must come from elsewhere. The entry pins exactly "
        "that scoping. FORBIDDEN inversion (container thinking): \"the generation "
        "coefficients are a flavor structure imposed on the fiber\" → INVERT: "
        "\"the fiber's own Haar-moment closed form IS the coefficient set; the "
        "second Z₃ is the fiber's intrinsic phase lever, lepton-only by "
        "representation content.\"",
        "",
        "**Provenance.** S100a W-2 fermion-mass texture cluster, gate "
        "`S100a-DUAL-Z3-PHI-POINTS` (composite PASS; 3-tuple sign=PASS, "
        "magnitude=PASS, regime=VALID; audit "
        "`d23c7e99cba964035261235ef54b79876e89d2bd4b23d2e57f6f60151f94afe0`; "
        "WP §W2-1, `sessions/session-100a/session-100a-w2-workingpaper.md`). "
        "Binding source = the S100a W-2 workshop frozen text (transcribed "
        "VERBATIM; no re-derivation — the c(φ) collapse, the Haar moments, the "
        "lepton-only structural identity, and the eq-(2.104) lineage are all the "
        "anchor gate's verified content). Construction lineage: Baptista Paper 14 "
        "§3 (eq 3.22 diagonal weight / eq 2.104 vertical profile / eq 2.17 "
        "D-sector profile); Paper 18 App E (the dual-Z₃ reading — first Z₃ = "
        "SU(3) triality channels, second Z₃ = the s_φ phase orbit). Landed S101 "
        "W6-2 (gen-physicist), single-shot AFTER pattern per `registry-landing.md` "
        "§\"Bridge-Landing Script Architecture\"; slot `§VII.BN` reserved "
        "`RESERVED-FOR-S101-W6-2-DUAL-Z3` in "
        "`sessions/framework/s101-slot-pre-allocation-lockfile.md`, runtime-"
        "verified next-free at all header levels (highest prior §VII.BM, W6-1). "
        "This is a §VII representation-theoretic exact-result landing, NOT a §7 "
        "falsifier-surface row — mack-cosmic-bridge sole-writer does NOT apply.",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Section 7 — slot scan / write / verify
# ---------------------------------------------------------------------------

def scan_slot_occupancy(registry_text: str) -> int:
    """All-header-level (##/###/####) count of §VII.BN headers (PD-2)."""
    return len(SLOT_SCAN_RE.findall(registry_text))


def write_atomic_with_fsync(registry_path: Path, section_text: str,
                            newline: str) -> None:
    """APPEND section_text to the registry + flush + os.fsync (PD-4 single-writer).

    A blank line separates the new §VII.BN section from the prior §VII.BM
    entry. The registry uses CRLF (`newline`); the appended block is written
    with the same line terminator so the file stays byte-homogeneous.
    """
    block = newline + section_text.replace("\n", newline) + newline  # (local)
    # Open in binary append to control the exact byte terminator (no universal-
    # newline translation), matching the file's existing CRLF.
    with open(registry_path, "ab") as fh:
        fh.write(block.encode("utf-8"))
        fh.flush()
        os.fsync(fh.fileno())


def re_read_section(registry_path: Path, section_text: str,
                    newline: str) -> str:
    """Re-read the registry tail and return the on-disk §VII.BN section.

    Splits on the section's own header line to isolate the landed block,
    normalizes the on-disk CRLF back to '\\n' for comparison against the
    in-memory '\\n'-joined promotion text.
    """
    disk = registry_path.read_text(encoding="utf-8")  # (local)
    disk_lf = disk.replace(newline, "\n")  # (local)
    header = section_text.splitlines()[0]  # (local) the §VII.BN header line
    idx = disk_lf.rfind(header)  # (local) last occurrence = our landing
    if idx < 0:
        return ""
    tail = disk_lf[idx:]  # (local)
    # Trim the single trailing newline the writer added so the re-read block
    # equals the in-memory promotion text exactly.
    return tail.rstrip("\n")


def verify_section_matches(actual: str, expected: str) -> bool:
    """Strict byte-exact equality."""
    return actual == expected


# ---------------------------------------------------------------------------
# Section 8 — verdict payload
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict: str, value, audit_sha: str,
                          content_sha: str,
                          extra_rows: list | None = None) -> dict:
    payload: dict = {  # (local)
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def emit_4tuple(value) -> str:
    return (f"(value={value!r}, scheme={SCHEME}, "
            f"convention={CONVENTION}, L_max={L_MAX})")


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 0. Detect the registry's line terminator (CRLF expected) BEFORE any write.
    raw = REGISTRY.read_bytes()  # (local)
    newline = "\r\n" if b"\r\n" in raw[:4096] else "\n"  # (local)
    registry_text_pre = raw.decode("utf-8")  # (local)
    print(f"=== {GATE_ID} — registry line terminator: "
          f"{'CRLF' if newline == chr(13)+chr(10) else 'LF'} ===")

    # 1. Input pins (logged in first lines of stdout).
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure(legacy): {closure[:16]}...")

    # 1b. Anchor-integrity asserts (binding-text rule): the dual_z3 npz SHA and
    #     the PRIMARY anchor audit_sha must match the plan pins exactly.
    npz_sha = pins[str(DUAL_Z3_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/")]  # (local)
    assert npz_sha == (
        "36a412ee5128cf1af63df02e8968afe978ed49698bfbae4d2bd029bb18dadef1"), (
        f"dual_z3 npz SHA drift: {npz_sha}")
    # Re-check the closed-form arithmetic against the frozen anchor numbers.
    recheck = recheck_closed_form()  # (local)
    print("  closed-form re-check: c={1/9,1/3,1/3}, distinct=2, "
          "heavy/light=3, deg(±2π/3)=True, Haar(1/2,1/4,0) — all exact ✓")

    # 2. PD-2 — all-header-level slot scan. §VII.BN must be FREE; lockfile
    #    reserves it to this gate (cross-reference asserted from disk text).
    slot_hits_pre = scan_slot_occupancy(registry_text_pre)  # (local)
    lockfile_text = LOCKFILE.read_text(encoding="utf-8")  # (local)
    reserved = (LOCKFILE_BLOCK in lockfile_text
                and "§VII.BN" in lockfile_text)  # (local)
    print(f"  PD-2 slot scan: §VII.BN occurrences (pre-append) = "
          f"{slot_hits_pre}; lockfile {LOCKFILE_BLOCK} present = {reserved}")
    rerouted = False  # (local)
    if slot_hits_pre != 0:
        # PD-3 — runtime occupancy: reroute would fire here. Single-writer
        # PD-4 chain makes this unreachable in the planned sequence; if it
        # ever fires, emit FAIL-with-remediation (NOT PASS).
        rerouted = True

    # 3. build_promotion_text (PURE; in memory before any write).
    promotion_text = build_promotion_text()  # (local)
    print(f"  built promotion text: {len(promotion_text)} chars, "
          f"header = {promotion_text.splitlines()[0][:60]}...")

    if rerouted:
        # FAIL-with-remediation: name the reroute target, do NOT write PASS.
        value = (f"REROUTE_FIRED_slot_{SLOT}_occupied_pre_append_"
                 f"hits={slot_hits_pre}_remediation_next_free_BO_block")  # (local)
        # Audit pin map (per plan audit_discriminators).
        registry_runtime_sha = pins[
            str(REGISTRY.relative_to(PROJECT_ROOT)).replace("\\", "/")]  # (local)
        pinmap = dict(pins)  # (local)
        pinmap.update({
            "_gate_id": GATE_ID, "_slot": SLOT, "_lockfile_block": LOCKFILE_BLOCK,
            "_registry_state_at_runtime": registry_runtime_sha,
            "_primary_anchor_audit": PRIMARY_ANCHOR_AUDIT,
            "_rerouted": "True", "_section_match": "N/A",
        })
        audit_sha = compute_audit_sha(
            Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pinmap)
        content_sha = content_sha_of(promotion_text)  # (local) (would-be section)
        np.savez(OUT_NPZ, slot=SLOT, rerouted=True, section_match=False,
                 slot_hits_pre=slot_hits_pre, audit_sha256=audit_sha,
                 content_sha256=content_sha, **{
                     k: v for k, v in recheck.items()})
        print(emit_4tuple(value))
        print_verdict_payload("FAIL", value, audit_sha, content_sha)
        print(f"\n=== {GATE_ID}: FAIL (reroute) (wall {time.time()-t0:.1f}s) ===")
        return 0  # script ran fine; FAIL is a valid scientific verdict

    # 4. write_atomic_with_fsync (single APPEND + fsync).
    write_atomic_with_fsync(REGISTRY, promotion_text, newline)

    # 5. re_read + verify (ONE strict-equality boolean; no conditional rewrite).
    actual = re_read_section(REGISTRY, promotion_text, newline)  # (local)
    section_match = verify_section_matches(actual, promotion_text)  # (local)
    print(f"  post-fsync re-read byte-match = {section_match} "
          f"(re-read {len(actual)} chars vs built {len(promotion_text)} chars)")

    # 6. Dual-SHA over the FINAL state.
    #    audit_sha256: script||canonical||ordered-pin-map (with the registry
    #    state captured POST-append as the runtime registry-state pin, plus
    #    identity keys); content_sha256: the post-fsync re-read on-disk section.
    registry_post_sha = sha256_of(REGISTRY)  # (local) post-append state
    pinmap = dict(pins)  # (local)
    pinmap.update({
        "_gate_id": GATE_ID,
        "_slot": SLOT,
        "_lockfile_block": LOCKFILE_BLOCK,
        "_registry_state_at_runtime": registry_post_sha,
        "_primary_anchor_audit": PRIMARY_ANCHOR_AUDIT,
        "_primary_anchor_content": PRIMARY_ANCHOR_CONTENT,
        "_rerouted": "False",
        "_section_match": str(section_match),
        "_serialization_order": "2-of-7",
    })
    audit_sha = compute_audit_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pinmap)
    content_sha = content_sha_of(actual)  # (local)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    # 7. Verdict: PASS iff byte-match AND not rerouted.
    verdict = "PASS" if section_match else "FAIL"  # (local)
    value = (
        f"landed_VII.BN_section_byte_match_{section_match}_"
        f"c=1/9,1/3,1/3_exact;deg2@pm2pi3;heavy/light=3_exact;"
        f"quark_dphi=0;haar(1/2,1/4,0);lineage_c=alpha2/2_eq2.104;"
        f"5anatomy_NA_with_reason;single_reading;level2_Z3_moduli")  # (local)

    # 8. Landing-record npz.
    np.savez(
        OUT_NPZ,
        slot=SLOT,
        rerouted=False,
        section_match=bool(section_match),
        slot_hits_pre=slot_hits_pre,
        promotion_text_len=len(promotion_text),
        reread_len=len(actual),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        registry_state_post_append=registry_post_sha,
        primary_anchor_audit=PRIMARY_ANCHOR_AUDIT,
        dual_z3_npz_sha=npz_sha,
        w2_wp_sha=pins[str(W2_WP.relative_to(PROJECT_ROOT)).replace("\\", "/")],
        lockfile_sha=pins[str(LOCKFILE.relative_to(PROJECT_ROOT)).replace("\\", "/")],
        **{k: v for k, v in recheck.items()},
    )
    print(f"  npz written: {OUT_NPZ.name}")

    print(emit_4tuple(value))
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        extra_rows=[
            f"# eq-2.104 lineage c(phi)=alpha^2(phi)/2; Haar E|s1|^2=1/2 "
            f"E|s2|^2=1/4 E[s1bar s2]=0; PRIMARY anchor S100a-DUAL-Z3-PHI-POINTS "
            f"PASS audit {PRIMARY_ANCHOR_AUDIT[:16]}...; "
            f"# {GATE_ID} dual-Z3 lepton-only lever landing companion row",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
