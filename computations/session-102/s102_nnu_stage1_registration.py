#!/usr/bin/env python3
"""
S102 W1-1 — Normalization-Non-Universality rank-1 theorem-tag Stage-1 registration
==================================================================================

Gate: S102-NNU-STAGE1-REGISTRATION ([VERIFY])

Pre-registered threshold (set-membership, NON-numerical):
  PASS iff  verify_section_matches(on_disk_section, expected_promotion_text) == True
            AND "STAGE-1-CANDIDATE" in the tag-line
            AND every clause row {(a),(b),(c),(d),(e),(f),(g)} present
            AND JOINT-flag on {(a),(c),(e)}
            AND both falsifier statements {(i),(ii)} present
            AND the odd-floor rider present.
  FAIL iff section mismatch OR a required structural marker absent OR slot-reroute occurred.
  INFO reserved for the degenerate next-free-slot-ambiguity case (parallel-writer race).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/session-101/workshops/s101-normalization-non-universality-workshop.md  (frozen Stage-0 source; spans byte-extracted)
  - sessions/permanent-results-registry.md  (write target; pre-write SHA captured for the audit trail)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<section_match_bool + slot>, scheme=REGISTRY-LANDING-AFTER-PATTERN,
   convention=STAGE-1-CANDIDATE-JOINT-CROSS-AXIS, L_max=N/A)

Classification: GEOMETRIC  (the spectral-triple structure / emergent-metric
  normalization — the FABRIC itself, not its excitations).

METHODOLOGY
-----------
AFTER-pattern single-shot registry landing per `registry-landing.md §"Bridge-Landing
Script Architecture"`: build_promotion_text builds the FULL §VII.BS STAGE-1-CANDIDATE
entry in memory (theorem-tag text + clause-attribution table byte-EXTRACTED VERBATIM
from the SHA-pinned frozen Stage-0 source by literal-substring anchors, with HARD span
SHA + length asserts so any transcription drift halts the run) -> write_atomic_with_fsync
appends to permanent-results-registry.md at the next-free §VII slot (next-free-LETTER
scan over ## / ### / #### header levels per `epistemic-discipline.md §"Registry-Write
Hygiene"`; binary 'ab' append, NO CRLF flatten) -> re_read + verify_section_matches
(the on-disk §VII.BS section byte-matches the expected promotion text AND carries the
STAGE-1-CANDIDATE tag AND all seven clause rows AND the JOINT flags on (a)/(c)/(e) AND
both falsifier statements AND the odd-floor rider) -> emit exactly one verdict line whose
verdict is that boolean. NO conditional rewrite branch (forbidden BEFORE-pattern).

This is a JOINT-THEOREM Stage-1 registration per `joint-theorem-promotion.md §"Stage 1"`,
NOT a cross-pillar BRIDGE entry: the 5 IS-not-IN anatomy elements of
`cross-pillar-bridge-anatomy.md` are declared N/A-with-reason (no substrate-IS-pillar ->
laboratory-IN-pillar bridge map; the theorem scopes the substrate's own normalization
structure). The 3-stage joint-theorem pathway applies: this gate is Stage 1 (register as
CANDIDATE); Stage 2 is item 4 (S102-NNU-STAGE2-VERIFY); Stage 3 (PERMANENT) is the
session-end orchestrator-direct tag flip on item-4 PASS-AND.

The registration is a TRANSCRIPTION, not a re-derivation: the direction of explanation
(D_K eigenvalues -> spectral moments -> dimensionless dynamical shapes -> measurement; the
single dimensional second imported via the external cutoff M_KK, N_3=0) is preserved
VERBATIM from the frozen Stage-0 text. No sign/direction/threshold claim is made by this
gate (the theorem-tag's OWN directional claims are the subjects of items 3 and 4).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- File I/O only (no linear algebra) -> no GPU path
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe; the script
  PRINTS the payload via print_verdict_payload, the AGENT calls emit_verdict). The script
  does NOT write s102_gate_verdicts.txt. The registry-file write here uses the single-shot
  open('ab')-append-with-fsync pattern (single-writer registry; distinct from the verdict
  file).
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

# Put computations/_shared on the path so canonical_constants imports when this
# script is run from computations/session-102/ (sibling-script pattern, e.g.
# computations/session-101/s101_w6_6_schur_rigidity_stage1_registration.py:76-78).
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
import os
import re
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

SESSION = "S102"                                                  # (local)
GATE_ID = "S102-NNU-STAGE1-REGISTRATION"                          # (local)
SCHEME = "REGISTRY-LANDING-AFTER-PATTERN"                         # (local)
CONVENTION = "STAGE-1-CANDIDATE-JOINT-CROSS-AXIS"                 # (local)
L_MAX = "N/A"                                                     # (local)

# Inputs
FROZEN_SRC = (PROJECT_ROOT / "sessions" / "session-101" / "workshops"
              / "s101-normalization-non-universality-workshop.md")          # (local)
REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"      # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"                           # (local)

# Pinned input SHAs (plan §W1-1 input_files block; static files)
FROZEN_SRC_SHA_PIN = "082cf60e8ba31d79b1d989dcf9b4c3c5dbd1ebcdab4493e83a4936196110e087"   # (local)
CANONICAL_SHA_PIN = "9f2fe9983ecbbb76a2ba1b3e951cf9275deda8d7f2241576ef23b7f728ba1047"     # (local)

# Pinned byte-extracted span SHAs + lengths (HARD asserts; transcription-drift halt)
THEOREM_SPAN_SHA_PIN = "e669ccd2daa5aa5be7396499"   # (local) head-24 of the theorem-tag span
THEOREM_SPAN_LEN_PIN = 2514                          # (local)
TABLE_SPAN_SHA_PIN = "7f53159eaf6b5eb02abe9fe7"     # (local) head-24 of the clause-table span
TABLE_SPAN_LEN_PIN = 1219                            # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s102_nnu_stage1_registration.npz"
OUT_PNG = SESSION_DIR / "s102_nnu_stage1_registration.png"

INPUT_FILES = [CANONICAL, FROZEN_SRC, REGISTRY]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block + dual-SHA
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
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


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """audit_sha256 = sha256(script || canonical || pinmap_json); content_sha256 = sha256(script)."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Verbatim span extraction (HARD-asserted) + promotion-text build
# ---------------------------------------------------------------------------
def extract_verbatim_spans() -> tuple[str, str]:
    """Byte-EXTRACT the theorem-tag text + clause-attribution table from the frozen
    Stage-0 source by literal-substring anchors; HARD-assert span SHA + length.
    A transcription-drift mismatch raises -> non-zero exit (script breakage, not a verdict)."""
    src = FROZEN_SRC.read_text(encoding="utf-8")  # (local)

    a1_start = "> **Normalization Non-Universality (N₃=0 corollary, rank-1).**"  # (local)
    a1_end = "PROVEN-corollary pending the R1 kill-criterion gate."                   # (local)
    i1 = src.find(a1_start)  # (local)
    j1 = src.find(a1_end)    # (local)
    if i1 < 0 or j1 < 0:
        raise RuntimeError("theorem-tag anchor substrings not found in frozen source")
    theorem_span = src[i1: j1 + len(a1_end)]  # (local)

    a2_start = "| Clause | Content | Axis attribution |"  # (local)
    a2_end = ("| (g) | moment-decoupling caveat (rank-1 covariance ≠ single-compute "
              "closure; F₋₁ vs F₊₁) | **phonon-first-side** "
              "(Re:V2/Q-PF3; volovik DISSENT confirmed) |")  # (local)
    i2 = src.find(a2_start)  # (local)
    j2 = src.find(a2_end)    # (local)
    if i2 < 0 or j2 < 0:
        raise RuntimeError("clause-attribution-table anchor substrings not found in frozen source")
    table_span = src[i2: j2 + len(a2_end)]  # (local)

    # HARD asserts — transcription-drift halt
    th_sha = hashlib.sha256(theorem_span.encode("utf-8")).hexdigest()  # (local)
    tb_sha = hashlib.sha256(table_span.encode("utf-8")).hexdigest()    # (local)
    assert len(theorem_span) == THEOREM_SPAN_LEN_PIN, \
        f"theorem-span length drift: {len(theorem_span)} != {THEOREM_SPAN_LEN_PIN}"
    assert th_sha.startswith(THEOREM_SPAN_SHA_PIN), \
        f"theorem-span SHA drift: {th_sha[:24]} != {THEOREM_SPAN_SHA_PIN}"
    assert len(table_span) == TABLE_SPAN_LEN_PIN, \
        f"table-span length drift: {len(table_span)} != {TABLE_SPAN_LEN_PIN}"
    assert tb_sha.startswith(TABLE_SPAN_SHA_PIN), \
        f"table-span SHA drift: {tb_sha[:24]} != {TABLE_SPAN_SHA_PIN}"

    print(f"  theorem_span: len={len(theorem_span)} sha={th_sha[:24]} (PINNED, verbatim)")
    print(f"  table_span:   len={len(table_span)} sha={tb_sha[:24]} (PINNED, verbatim)")
    return theorem_span, table_span


def next_free_slot_letter() -> str:
    """Scan ## / ### / #### §VII.<LETTERS> header levels; return the next-free code in the
    SEQUENTIAL two-letter A..Z allocation series after the highest existing.
    Per `epistemic-discipline.md §"Registry-Write Hygiene"` item 1 (scan ALL header levels).

    The sequential allocation series is the TWO-LETTER alphabetic suffix (…BP, BQ, BR → BS):
    this matches the sibling provenance semantics ("highest prior §VII.BR"). NAMED / legacy
    slots are EXCLUDED from the max — `§VII.PROP` ("Routing-Layer Two-Principle", a word
    abbreviation), `§VII.K-PROP-*` (hyphenated legacy), and the 3-letter `§VII.AAU` (a named
    FWD-C1 candidate, not part of the sequential B-series) are NOT sequential codes. A naive
    max over ALL `[A-Z]+` captures would pick `PROP` → `PROQ`, the slot-allocation BUG this
    guard closes. The lookahead boundary rejects any token that is the head of a hyphenated
    word (so a `K-PROP` legacy header does not contribute a bare `K`)."""
    text = REGISTRY.read_text(encoding="utf-8")  # (local)
    # EXACT two-letter slot codes only: §VII.XY followed by a slot boundary (space, dot,
    # em-dash, or .OP-PROJ/.STATE-PROJ suffix). NOT a third letter (excludes AAU, PROP).
    found = re.findall(
        r"^#{2,4}\s*§VII\.([A-Z]{2})(?=[\s.—]|\.OP-PROJ|\.STATE-PROJ|$)",
        text, flags=re.MULTILINE)  # (local)

    def code_to_int(code: str) -> int:  # (local)
        n = 0
        for ch in code:
            n = n * 26 + (ord(ch) - ord("A") + 1)
        return n

    def int_to_code(n: int) -> str:  # (local)
        s = ""
        while n > 0:
            n, r = divmod(n - 1, 26)
            s = chr(ord("A") + r) + s
        return s

    max_n = max((code_to_int(c) for c in found), default=0)  # (local)
    return int_to_code(max_n + 1)


def build_promotion_text(slot_letter: str, theorem_span: str, table_span: str) -> str:
    """Build the FULL §VII.<slot> STAGE-1-CANDIDATE entry in memory. The theorem-tag text +
    clause table ride VERBATIM (byte-extracted spans); the surrounding registry scaffolding
    (header, STAGE-1-CANDIDATE tag, JOINT-clause flags, both-falsifier markers, odd-floor
    rider marker, Stage-2 routing w/ author exclusion, registry-anatomy compliance,
    provenance, substrate framing) is the registration wrapper."""
    slot = f"§VII.{slot_letter}"  # (local)
    header = (
        f"### {slot} — Normalization Non-Universality (N₃=0 corollary, rank-1): the "
        f"substrate determines the conformal class + all dimensionless dynamical shapes of the "
        f"emergent cosmology, NOT the dimensional metric normalization (STAGE-1-CANDIDATE per "
        f"joint-theorem-promotion.md; S101 W-2 volovik×phonon-first workshop frozen Stage-0 "
        f"text, transcribed VERBATIM; S102 W1-1 landing — gen-physicist; Stage-0 authors "
        f"volovik-superfluid-universe-theorist + phonon-first-cosmologist, BOTH Stage-2-EXCLUDED)"
    )

    body = f"""
**STAGE-1-CANDIDATE** (4-stage joint-theorem pathway per `joint-theorem-promotion.md`; Stage-0 text = `sessions/session-101/workshops/s101-normalization-non-universality-workshop.md` §"Stage-0 frozen candidate" (the EMERGENCE-(A) endorsed text, volovik R3 + phonon-first E1; Stage-0 FROZEN); Stage-2 cross-axis verify = `S102-NNU-STAGE2-VERIFY` (item 4 this wave). Classification **GEOMETRIC**. The FROZEN Stage-0 candidate theorem-tag text below (clauses (a)–(g); JOINT = (a)/(c)/(e)) is transcribed VERBATIM (byte-extracted from the SHA-pinned workshop; theorem-tag span SHA `{THEOREM_SPAN_SHA_PIN}…`, clause-attribution-table span SHA `{TABLE_SPAN_SHA_PIN}…`, both HARD-asserted at runtime) — re-derived NOTHING. The two pre-registered falsifiers (i)/(ii) ride verbatim INSIDE the theorem-tag text; the odd-floor RIDER (S101-W1-QEQ-RELIC-ODDFLOOR, a pole not a scale, OUTSIDE `O = w·Ô`) rides verbatim as the separate-finding clause. NO post-freeze amendment applies (unlike §VII.BP): both falsifier computes (items 2/3) and the Stage-2 verify (item 4) are S102 forward gates — they FEED the session-end Stage-3 decision, they do NOT amend this frozen text.

**FROZEN STAGE-0 CANDIDATE TEXT (transcribed VERBATIM — the EMERGENCE-(A) endorsed theorem-tag, S101 W-2 workshop §"Stage-0 frozen candidate"; re-derived NOTHING):**

{theorem_span}

**CLAUSE-BY-CLAUSE AXIS ATTRIBUTION (transcribed VERBATIM — Stage-0, for the S102 Stage-2 cross-axis verify):**

{table_span}

JOINT clauses (a)/(c)/(e) require Stage-2 PASS-AND across both cross-reviewers. Sign-resolved falsifier-(ii) precision (clause within (a)): `|Corr|=1` with sign `= sign(p_i·p_j)`, NOT blanket `+1` — volovik R3, phonon-first ratified.

**JOINT-clause flags (Stage-2 PASS-AND).** Clauses **(a)** (rank-1 covariance theorem / Half A), **(c)** (`O = w·Ô` = K=3 multiplicative-normalization cancellation invariant, FRW = fourth instance), and **(e)** (n=2 tracking exponent inside the protected `Ô` content) are flagged for Stage-2 PASS-AND across BOTH axes (logical AND, not OR) per `joint-theorem-promotion.md §"Stage 2"`: both cross-reviewers must INDEPENDENTLY PASS each JOINT clause. Single-axis clauses: (b) [volovik-side, N₃=0 → BDI single-cutoff count / Half B], (d) [volovik-side, Q-PF5 dimensional unreachability through the spectral action], (f) [volovik-side, odd-floor separate rider], (g) [phonon-first-side, moment-decoupling caveat].

**TWO SYMMETRIC PRE-REGISTERED FALSIFIERS (ride verbatim in the theorem-tag text above; armed by S102 items 2/3).** **Falsifier (i)** — R1 kill criterion (S102-NNU-FALSIFIER-I-R1-SOURCECHECK, item 2): if a future gate writes `gamma_unit = Φ(D_K eigenvalues alone)` with no imported GeV/seconds scale, the theorem is FALSIFIED (rank-0). **Falsifier (ii)** — rank-1 covariance test (S102-NNU-FALSIFIER-II-RANK1-COVARIANCE, item 3): if any borrowed-H dagger-row shows `|Corr| < 1` (NOT merely `Corr ≠ +1`; the predicted sign of each pair is `sign(p_i·p_j)` of the M_KK powers) under single-H renormalization, Half B's single-cutoff count is wrong, rank ≥ 2, and the memo's R2 partial-structure branch reopens. Both falsifiers are pre-registered SYMMETRICALLY (each carries an explicit theorem-CONFIRMING branch and an explicit theorem-FALSIFYING branch) so neither is an iterate-until-PASS dispatch (`v3-closure-recovery.md` PROHIBITED_ACTIONS Class 6). The Stage-3-PERMANENT promotion criterion is item-2 FAIL (rank-1 confirmed on the SOURCE axis) + item-3 sustained `|Corr|=1` (rank-1 confirmed on the COUNT axis) + item-4 Stage-2 PASS-AND; item-2 PASS or item-3 `|Corr|<1` FALSIFIES.

**ODD-FLOOR RIDER (separate finding, NOT part of the rank-1 obstruction; rides verbatim in the theorem-tag text above).** The conformal-class-complete content is robust EXCEPT where the derived substrate clock resonates with the pair band (S101-W1-QEQ-RELIC-ODDFLOOR FAIL: `ω_q^phys = 2.0128 M_KK` inside `[1.6395, 10.8379]`, `|c_odd|/|c_even| = 2.70e-2`), introducing a relic-induced odd-in-H dynamical correction OUTSIDE `O = w·Ô` — **a pole, not a scale**. The rider is a distinct structural object from the rank-1 normalization obstruction (which is the `O = w·Ô` multiplicative factorization); it does NOT enter the rank-1 covariance count.

**MOMENT-DECOUPLING CAVEAT (clause (g); rides verbatim in the theorem-tag text above).** Rank-1 covariance does NOT imply single-compute closure — the projections land on algebraically-independent spectral moments (F₋₁ vs F₊₁), so only supplying `w` at the source (the cutoff→lab-units bridge `ℏ/M_KK c²`) closes all channels; closing any single channel's readout closes only that moment's leg.

**Anchors.** Stage-0 text = the S101 W-2 normalization-non-universality workshop §"Stage-0 frozen candidate" (`sessions/session-101/workshops/s101-normalization-non-universality-workshop.md`, file SHA `{FROZEN_SRC_SHA_PIN}`; extracted theorem-tag span SHA `{THEOREM_SPAN_SHA_PIN}…` + clause-table span SHA `{TABLE_SPAN_SHA_PIN}…`, both pinned + HARD-asserted at runtime). Half-A anchor (clause (a)) = the Sage log-Jacobian rank-1 outer-product certificate (one scale at powers `(−1,2,4)` → column rank 1, `|Corr|=1` exact with sign `= sign(p_i·p_j)`). Half-B anchor (clause (b)) = the S44 `N₃ = 0` BDI-class invariant (vacuum energy unprotected by Fermi-point topology; q-theory required). Co-shift seed = `Corr(a₀,a₂) = +1` (W7-7a / S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE, the borrowed-H residual co-shift). `O = w·Ô` = the K=3-MANDATORY multiplicative-normalization cancellation invariant (`math-scripts.md`), of which the FRW background is a fourth structurally-distinct instance. Odd-floor rider anchor = `S101-W1-QEQ-RELIC-ODDFLOOR` FAIL (`s101_gate_verdicts.txt`, audit `98a923fd0ea4a6ec5f80360468422e05651ef301a25f71645bd543e6c1ad4282`). Falsifier-arming gates (S102) = `S102-NNU-FALSIFIER-I-R1-SOURCECHECK` (item 2, SOURCE axis) + `S102-NNU-FALSIFIER-II-RANK1-COVARIANCE` (item 3, COUNT axis). Canonical scale anchors = `M_KK_inv_seconds = 8.860439881925477e-42` (S96-W1-MKK-SECONDS); `G_DeWitt = 5.0` (S42); `f₂ ≈ 92 = M_Pl/M_KK` (§8.3 dictionary).

**Authorship + Stage-2 routing (binding).** Stage-0 authors = `volovik-superfluid-universe-theorist` + `phonon-first-cosmologist` ONLY (S101 W-2 workshop; CONVERGED 3 rounds, 2026-06-09); **BOTH Stage-2-EXCLUDED** (original-authoring-agent exclusion with downstream-inheritance reach, `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` all three conditions; S99 E1 author-exclusion discipline — including successor volovik / phonon-first spawns whose memory inherits this workshop's reading path). Stage-2 gate = **S102-NNU-STAGE2-VERIFY** (item 4 this wave): **Axis-A** = spectral / NCG-axiomatic (re-derives clauses (b)/(d) + the JOINT clauses from THIS registered text alone); **Axis-B** = transit-dynamics / cosmological-bridge (re-checks clauses (f)/(g) + the JOINT clauses). JOINT clauses (a)/(c)/(e) PASS-AND'd across both verdicts. Substrate-input-orthogonality SATISFIABLE at the structural ceiling (clause (a) Sage log-Jacobian vs clause (b) S44 N₃=0 invariant — orthogonal data). `joint-theorem-promotion.md` audit item 6 (no reviewer may be sole author of the verdict-layer machinery they apply) applies to the rank-1 covariance machinery (gen-physicist owns item 3's covariance compute; the Stage-2 Axis that audits clause (a) must not be sole-authored by the same machinery).

**Registry-anatomy compliance.** (i) Entry class = **joint cross-axis theorem candidate** on the spectral-triple-normalization / induced-gravity axis pair (volovik superfluid-universe-topology + phonon-first cross-domain-pattern/covariance); **NOT a cross-pillar bridge** ⇒ the 5-anatomy IS-not-IN elements + the 3-level ladder are declared **N/A-with-reason**: there is no laboratory-IN observable and no HKR / K-theory / Connes-Karoubi bridge map is claimed (the theorem scopes what the substrate's own spectral triple DETERMINES vs IMPORTS in its emergent-metric normalization; there is no continuum-image envelope). (ii) **Corner-cell machinery: N/A-with-reason** — the theorem's central object is the `O = w·Ô` multiplicative-normalization factorization (a structural statement about the borrowed-H shift-covariance rank), NOT a single spectral-triple functional on `(A_K, H_K, D_K)`, so the 4-corner parse-tree classification of `permanent-results-registry.md §VII.U.2` does not apply (and the bare slot identifier `{slot}` is therefore admissible — no `.OP-PROJ`/`.STATE-PROJ` suffix, which only applies to operator-side-vs-state-side spectral-triple functional readings). (iii) **No state-history labels** (parse-tree N/A — no `Bogoliubov`/`GGE`/`α_s_route_N` label appears in the theorem-tag text; `GGE relic` appears only in the odd-floor rider provenance, defensively expanded: GGE relic → fold-frozen occupations → Parker pair production at the τ_fold transit → D_K(τ) eigenvalue reorganization). (iv) **Substrate-IS level tag = Level 1** (single-τ-slice at the τ_fold slice of the Jensen flow, τ_fold = 0.190) per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`: the normalization structure is read at the fold slice; the conformal-class content is the protected `Ô` kernel of the single-τ-slice spectral triple.

**Substrate framing** (`phononic-framing.md §"IS Space, Not IN Space"`; GEOMETRIC-class). The theorem-tag is a statement about the FABRIC itself — the spectral triple `(A_K, H_K, D_K)` and the normalization structure of the metric it induces. **Direction of explanation** (preserved verbatim from the frozen Stage-0 text): `D_K eigenvalues → spectral moments → dimensionless dynamical shapes (every ratio, ordering, tilt, growth shape, AND the late-time tracking exponent n=2) → measurement`. The substrate DETERMINES the entire dimensionless dynamical content of the cosmology from ZERO continuous parameters, and imports exactly ONE externally-calibrated dimensional scale — the cutoff M_KK — through the `O = w·Ô` factorization (`w = M_KK`). The eigenvalue problem is SILENT at the single terminal `× (ℏ / M_KK c²)` second BY CONSTRUCTION, because `N₃ = 0` (BDI class, S44) leaves the induced metric topologically unprotected. The re-scope of the capstone §6.3 a(t)-gap is a POSITIVE finding about what the substrate DETERMINES, not a deficit confession: what dies is the *seconds-valued* a(t), not the *shape* of a(t). FORBIDDEN inversion (container thinking): "the substrate's cosmology expands in a background spacetime whose metric normalization is set by GR" → INVERT: "the substrate IS the cosmology's dimensionless dynamical content; the emergent metric's conformal class is the protected `Ô` kernel of the spectral triple; the single dimensional second is the one externally-calibrated cutoff M_KK, NOT a pre-existing container the substrate lives in."

**Provenance.** S101 W-2 normalization-non-universality workshop (`sessions/session-101/workshops/s101-normalization-non-universality-workshop.md`, frozen §"Stage-0 frozen candidate"; file SHA `{FROZEN_SRC_SHA_PIN}`; CONVERGED 3 rounds 2026-06-09, agents volovik-superfluid-universe-theorist + phonon-first-cosmologist). Binding source = the workshop frozen Stage-0 text (extracted PROGRAMMATICALLY byte-verbatim by literal-substring anchors; no transcription drift — the theorem-tag span SHA `{THEOREM_SPAN_SHA_PIN}…` (len {THEOREM_SPAN_LEN_PIN}) and clause-table span SHA `{TABLE_SPAN_SHA_PIN}…` (len {TABLE_SPAN_LEN_PIN}) are pinned + HARD-asserted at runtime). Landed S102 W1-1 (gen-physicist), single-shot AFTER pattern per `registry-landing.md §"Bridge-Landing Script Architecture"`; slot `{slot}` runtime-verified next-free at all header levels (next-free-LETTER scan over ## / ### / #### per `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` item 1; highest prior §VII.BR); the registry pre-write file SHA + the byte-extracted span SHAs are captured in the gate npz `computations/session-102/s102_nnu_stage1_registration.npz` for the audit trail. Stage-2 cross-axis verify = item 4 this wave (volovik + phonon-first Stage-2-EXCLUDED). This is a §VII joint cross-axis STAGE-1-CANDIDATE landing, NOT a §7 falsifier-surface row — `mack-cosmic-bridge` sole-writer does NOT apply (the Normalization-Non-Universality theorem-tag is a STRUCTURAL finding about the substrate's emergent-metric normalization, not a falsifier observable with a live-watch envelope; no `falsifier-master-inventory.md` row emerges, per the joint-theorem registration norm).
"""
    # The promotion text is appended to the registry; lead with a blank line so it
    # separates cleanly from the prior entry. Trailing newline keeps the file tidy.
    return "\n" + header + "\n" + body.rstrip() + "\n"


# ---------------------------------------------------------------------------
# Section 6 — Atomic write + re-read verify
# ---------------------------------------------------------------------------
def write_atomic_with_fsync(promotion_text: str) -> None:
    """Single-shot append to the registry. Binary 'ab' append (NO CRLF flatten;
    preserves the file's existing line endings) + fsync."""
    data = promotion_text.encode("utf-8")  # (local)
    with open(REGISTRY, "ab") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())


def verify_section_matches(slot_letter: str, expected_text: str) -> tuple[bool, dict]:
    """Re-read the registry; confirm the on-disk §VII.<slot> section byte-matches the
    expected promotion text AND carries every required structural marker.
    Returns (overall_bool, marker_dict)."""
    on_disk = REGISTRY.read_text(encoding="utf-8")  # (local)
    # The expected_text begins with a leading "\n" + header; locate the header on disk.
    header_anchor = expected_text.lstrip("\n").split("\n", 1)[0]  # (local) the "### §VII.<slot> — ..." line
    idx = on_disk.find(header_anchor)  # (local)
    section_present = idx >= 0  # (local)

    # Byte-match: the on-disk slice from the header to EOF must START with the
    # expected body (this entry is the LAST one in the file, appended at the tail).
    expected_body = expected_text.lstrip("\n")  # (local) drop the separating leading newline
    byte_match = False  # (local)
    if section_present:
        on_disk_tail = on_disk[idx:]  # (local)
        byte_match = on_disk_tail.strip() == expected_body.strip()

    # Structural-marker presence (scoped to the on-disk section tail)
    sect = on_disk[idx:] if section_present else ""  # (local)
    markers: dict = {}  # (local)
    markers["stage1_candidate_tag"] = "STAGE-1-CANDIDATE" in (header_anchor + sect[:4000])
    # Seven clause rows in the verbatim clause-attribution table
    clause_rows = {c: (f"| ({c}) |" in sect) for c in ["a", "b", "c", "d", "e", "f", "g"]}  # (local)
    markers["clause_rows"] = clause_rows
    markers["all_seven_clauses"] = all(clause_rows.values())
    # JOINT flags on (a)/(c)/(e): the verbatim table rows carry "**JOINT**"; the wrapper
    # JOINT-flag paragraph names them explicitly.
    markers["joint_flag_paragraph"] = (
        "Clauses **(a)**" in sect and "**(c)**" in sect and "**(e)**" in sect
        and "Stage-2 PASS-AND" in sect)
    markers["joint_in_table"] = sect.count("**JOINT**") >= 3
    markers["joint_flags_ace"] = markers["joint_flag_paragraph"] and markers["joint_in_table"]
    # Both falsifiers present (the verbatim theorem-tag carries "(i)" + "(ii)"; the wrapper
    # names them as named gates)
    markers["falsifier_i"] = ("Falsifier (i)" in sect
                              and "S102-NNU-FALSIFIER-I-R1-SOURCECHECK" in sect)
    markers["falsifier_ii"] = ("Falsifier (ii)" in sect
                               and "S102-NNU-FALSIFIER-II-RANK1-COVARIANCE" in sect)
    markers["both_falsifiers"] = markers["falsifier_i"] and markers["falsifier_ii"]
    # Odd-floor rider present
    markers["odd_floor_rider"] = ("ODD-FLOOR RIDER" in sect
                                  and "S101-W1-QEQ-RELIC-ODDFLOOR" in sect
                                  and "a pole, not a scale" in sect)
    # Verbatim spans present (the theorem-tag opening line + the clause-table header line)
    markers["theorem_tag_verbatim"] = (
        "> **Normalization Non-Universality (N₃=0 corollary, rank-1).**" in sect)
    markers["clause_table_verbatim"] = "| Clause | Content | Axis attribution |" in sect

    overall = bool(
        section_present and byte_match and markers["stage1_candidate_tag"]
        and markers["all_seven_clauses"] and markers["joint_flags_ace"]
        and markers["both_falsifiers"] and markers["odd_floor_rider"]
        and markers["theorem_tag_verbatim"] and markers["clause_table_verbatim"])
    markers["section_present"] = section_present
    markers["byte_match"] = byte_match
    return overall, markers


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": 102,
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
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins + verify static SHA pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    frozen_sha = pins[str(FROZEN_SRC.relative_to(PROJECT_ROOT)).replace(chr(92), '/')]  # (local)
    canonical_sha = pins[str(CANONICAL.relative_to(PROJECT_ROOT)).replace(chr(92), '/')]  # (local)
    registry_pre_sha = pins[str(REGISTRY.relative_to(PROJECT_ROOT)).replace(chr(92), '/')]  # (local)
    assert frozen_sha == FROZEN_SRC_SHA_PIN, f"frozen-src SHA drift: {frozen_sha[:16]} != pin"
    assert canonical_sha == CANONICAL_SHA_PIN, f"canonical SHA drift: {canonical_sha[:16]} != pin"

    # 1b. dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Extract verbatim spans (HARD-asserted)
    theorem_span, table_span = extract_verbatim_spans()

    # 2a. CONTENT-IDENTITY idempotency: detect a PRIOR landing of THIS theorem by its
    #     unique slot-INDEPENDENT wrapper-header signature. If already landed at SOME slot,
    #     re-use that slot (NO re-append — keying on the recomputed next-free letter would
    #     duplicate the entry, since each prior landing advances the next-free letter).
    on_disk_now = REGISTRY.read_text(encoding="utf-8")  # (local)
    HEADER_SIG = ("— Normalization Non-Universality (N₃=0 corollary, rank-1): the "
                  "substrate determines the conformal class")  # (local) slot-independent
    m_existing = re.search(
        r"^#{2,4}\s*§VII\.([A-Z]{2})\s+" + re.escape(HEADER_SIG),
        on_disk_now, flags=re.MULTILINE)  # (local)
    already_landed = m_existing is not None  # (local)

    if already_landed:
        slot_letter = m_existing.group(1)  # (local) re-use the EXISTING slot
        print(f"  CONTENT-IDENTITY idempotency: theorem already landed at §VII.{slot_letter} "
              f"— no re-append (re-verify the existing entry)")
    else:
        slot_letter = next_free_slot_letter()  # (local) fresh allocation
        print(f"  next-free §VII slot letter: {slot_letter}")

    expected_text = build_promotion_text(slot_letter, theorem_span, table_span)
    expected_sha = hashlib.sha256(expected_text.encode("utf-8")).hexdigest()  # (local)
    print(f"  expected_promotion_text len={len(expected_text)} sha={expected_sha[:24]}")

    # 3. Single-shot write (AFTER-pattern: write FIRST, then verify; no conditional rewrite).
    #    Skipped on an idempotent re-run (already_landed).
    if not already_landed:
        write_atomic_with_fsync(expected_text)
        print(f"  appended §VII.{slot_letter} to {REGISTRY.relative_to(PROJECT_ROOT)}")
    else:
        print(f"  §VII.{slot_letter} already on disk — idempotent re-run, no re-append")

    # 4. Re-read + verify (the verdict IS this boolean)
    section_match, markers = verify_section_matches(slot_letter, expected_text)
    print(f"  section_match (byte + structural markers): {section_match}")
    for k in ("section_present", "byte_match", "stage1_candidate_tag", "all_seven_clauses",
              "joint_flags_ace", "both_falsifiers", "odd_floor_rider",
              "theorem_tag_verbatim", "clause_table_verbatim"):
        print(f"    {k}: {markers[k]}")

    # Slot-reroute detection: plan-pinned highest prior was §VII.BR -> expected next BS.
    # On an idempotent re-run the EXISTING slot is canonical; the byte-match on the existing
    # entry is the truth, so a re-run reproduces the original PASS (no reroute).
    slot_rerouted = (slot_letter != "BS")  # (local)
    if slot_rerouted:
        print(f"  WARNING slot-reroute: expected BS, allocated {slot_letter} "
              f"(emit FAIL-with-remediation per epistemic-discipline.md Registry-Write Hygiene item 3)")

    # 5. Verdict
    if section_match and not slot_rerouted:
        verdict = "PASS"  # (local)
        value = f"STAGE-1-CANDIDATE_landed_VII.{slot_letter}_byte-faithful_7clauses_JOINT-ace_2falsifiers_oddfloor-rider"  # (local)
    elif slot_rerouted and section_match:
        verdict = "FAIL"  # (local) section ok but slot drifted -> audit-visible reroute FAIL
        value = f"slot-reroute_to_VII.{slot_letter}_expected_BS_section-otherwise-faithful"  # (local)
    else:
        verdict = "FAIL"  # (local)
        value = f"section-mismatch_or_marker-absent_slot_VII.{slot_letter}_match={section_match}"  # (local)

    # 6. clause-presence + JOINT-flag vectors for the npz
    clause_vec = np.array([markers["clause_rows"][c] for c in
                           ["a", "b", "c", "d", "e", "f", "g"]], dtype=bool)  # (local)
    joint_vec = np.array([markers["joint_flag_paragraph"], markers["joint_in_table"],
                          markers["joint_flags_ace"]], dtype=bool)  # (local)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        frozen_text_sha=frozen_sha,
        theorem_span_sha=hashlib.sha256(theorem_span.encode("utf-8")).hexdigest(),
        theorem_span_len=len(theorem_span),
        table_span_sha=hashlib.sha256(table_span.encode("utf-8")).hexdigest(),
        table_span_len=len(table_span),
        expected_promotion_sha=expected_sha,
        expected_promotion_len=len(expected_text),
        registry_pre_write_sha=registry_pre_sha,
        allocated_slot_letter=slot_letter,
        section_match_bool=section_match,
        slot_rerouted=slot_rerouted,
        clause_presence_vector=clause_vec,            # (a)..(g)
        clause_labels=np.array(["a", "b", "c", "d", "e", "f", "g"]),
        joint_flag_vector=joint_vec,                  # [paragraph, table>=3, combined-(a)(c)(e)]
        both_falsifiers=markers["both_falsifiers"],
        odd_floor_rider=markers["odd_floor_rider"],
        verdict=verdict,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  npz -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 7. 4-tuple + verdict payload
    tag = (f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        extra_rows=[
            (f"# slot=§VII.{slot_letter} clause_presence=(a,b,c,d,e,f,g)={clause_vec.astype(int).tolist()} "
             f"joint_flags(a,c,e)={int(markers['joint_flags_ace'])} "
             f"both_falsifiers={int(markers['both_falsifiers'])} odd_floor_rider={int(markers['odd_floor_rider'])}"),
            (f"# theorem_span_sha={hashlib.sha256(theorem_span.encode('utf-8')).hexdigest()[:16]} "
             f"table_span_sha={hashlib.sha256(table_span.encode('utf-8')).hexdigest()[:16]} "
             f"verbatim-byte-extracted-HARD-asserted"),
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # verdict is data; exit 0 on a clean run regardless of PASS/FAIL


if __name__ == "__main__":
    sys.exit(main())
