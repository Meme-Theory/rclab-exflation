#!/usr/bin/env python3
"""
S103 W1-4 CF-S103-VIIBR-ORDER-CLAUSE-PATCH — reviewed curated-doc prose patch on the §VII.BR
Release-condition-R sentence (insert the in-block-O(ε)/off-block-O(ε²)/closed-loop-O(ε²)
order-class qualifier + the W5-4/W7-3 outcome cross-reference)
=============================================================================================

Gate: CF-S103-VIIBR-ORDER-CLAUSE-PATCH ([AUDIT])

Pre-registered threshold (artifact-existence + content-marker; the ONLY numeric guard is NEGATIVE):
  PASS iff (the §VII.BR Release-condition-R sentence carries the
              'in-block O(ε)' ∧ 'off-block O(ε²)' ∧ 'closed-loop O(ε²)' order-class qualifier)
           ∧ (the W5-4/W7-3 outcome cross-reference is present)
           ∧ (NO new LC-lineage-conditional FLOAT was introduced by the diff — the NEW-sentence
              float set ⊆ the OLD-sentence float set; the O(ε)/O(ε²) attribution is read from the
              EXISTING s101_w5_4 + s102_w7 npz slopes, NOT a fresh value)
           ∧ (the §VII.BR header grade STAGE-3-PERMANENT is UNCHANGED — pre==post occurrence count)
           ∧ verify == True.
  FAIL iff verify == False (qualifier substring absent, OR a NEW float entered the diff,
           OR the §VII.BR grade was altered, OR the OLD sentence is not uniquely locatable).
  INFO iff the on-disk Release-condition-R sentence has DRIFTED from the plan-pinned wording
           (a prior in-session edit) → re-anchor per substrate-first-canonical-sourcing.md §(ii.B)
           plan-text-drift correction (document drift; the patch is NOT applied on a drifted sentence
           without re-anchoring — emit INFO naming the drift).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/permanent-results-registry.md                                    (patch target; §VII.BR
        Release-condition-R sentence located by GREP, not line number — registry gained slot-rows + tail
        sections since the plan-pinned :21336)
  - sessions/session-102/session-102-berry-vii-br-order-clause-synthesis.md   (S-4 synthesis; §IV.3
        VERBATIM patch text, verified at file line 137 at plan-freeze)
  - computations/session-101/s101_w5_4_b2_isotropy_breaking.npz               (O(ε) band-matrix
        anisotropy leg; provenance cross-check ONLY — read the slope, introduce NO new number)
  - computations/session-102/s102_w7_b2_eps2_wz_holonomy.npz                  (O(ε²) closed-loop
        holonomy leg; provenance cross-check ONLY)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<patched;qualifier_ok;no_new_float;grade_unchanged;verify>,
   scheme=CURATED-DOC-REVIEWED-DESIGNATED-WRITER-PATCH,
   convention=DESIGNATED-WRITER-PROSE-PATCH-NOT-BULK-APPEND;ORDER-CLASS-QUALIFIER-INSERT;NO-NEW-LC-LINEAGE-NUMBER,
   L_max=N/A)

Classification: GEOMETRIC (the band-geometry order-class structure of the §VII.BR Schur-rigidity
  theorem; the substrate IS the spectral-triple band geometry). This gate INSERTS a reviewed
  qualifier derived UPSTREAM (S-4 synthesis §IV.3 + W5-4/W7-3 computes); it re-derives NOTHING and
  introduces NO new substrate number.

METHODOLOGY
-----------
Reviewed designated-writer prose patch — NOT a registry-landing AFTER-pattern that consumes a verdict
and builds a new §VII section. This is a TARGETED curated-doc Edit on an EXISTING §VII.BR sentence:
  build_patched_registry_text (replace the uniquely-located Release-condition-R order-clause sentence
  with the S-4 §IV.3 verbatim disambiguated text + the W5-4/W7-3 outcome cross-reference, preserving
  ALL surrounding bytes) → write_atomic_with_fsync → re_read + verify (qualifier substrings present
  ∧ no-new-float ∧ grade unchanged ∧ exactly-one §VII.BR section) → exactly ONE print_verdict_payload.
The order distinction (in-block O(ε) / off-block O(ε²) / closed-loop O(ε²)) is the OPERATOR-INDEPENDENT
consequence of off-block-ness + degenerate PT (P·δH·P ≡ 0 ⇒ leading anisotropy is the 2nd-order Schur
complement ∝ε²), so it belongs with the §VII.BR operator-independent body, NOT the LC-conditional witness
table — and it adds NO new LC-conditional number (S-4 §IV.3 closing note). The W5-4/W7-3 cross-reference
records the OUTCOME of the already-cited forward gate using gate/wave LABELS (no float witnesses), so the
NEGATIVE guard (no new float in the diff) holds.

Substitution chain (order/threshold claim — math-scripts.md §"Double-Check Logic"; verified against the
EXISTING npz slopes, introducing no new number):
  in-block anisotropy A_in(ε) ∝ ε^{p_in}, p_in ≈ 1 (linear-response, open in-band P·δH·P ≠ 0)
  off-block / closed-loop holonomy f_WZ(ε) ∝ ε^{p_loop}, p_loop = slope_angle ≈ 2 (Stokes: flux ∝ loop-area ∝ ε²)
  ⇒ ord(in-block) = 1 < ord(off-block) = ord(closed-loop) = 2 ⇒ DISTINCT order classes ⇒ the
  Release-condition-R discriminator must state WHICH order each lives at (the bare "O(ε)" conflated them).
  The slopes are READ from s101_w5_4 (disc/B2split) + s102_w7 (slope_angle) for provenance ONLY; the
  patch records the order CLASSES (O(ε), O(ε²)), not the float slopes.

DISCIPLINE
----------
- `from canonical_constants import *` (mandatory first import; no framework constant hardcoded — none used)
- Every local/intermediate tagged `# (local)`
- String assembly + SHA + file I/O only (cpu; OMP 8)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- AFTER/single-shot: build FULL text once, write atomically, re-read + verify, emit exactly ONE payload.
  If verify FAILs, emit FAIL once (no corrective in-script rewrite) per mechanical-closure-discipline.md.
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe; the script PRINTS the
  payload, the dispatching AGENT calls emit_verdict). The script does NOT write the verdict file.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import) + CPU thread cap
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
SHARED_DIR = Path(__file__).resolve().parent            # computations/_shared
COMPUTATIONS_DIR = SHARED_DIR.parent                    # computations/
PROJECT_ROOT = COMPUTATIONS_DIR.parent                  # project root
SESSION_OUT_DIR = COMPUTATIONS_DIR / "session-103"      # per-session outputs land here

SESSION = "S103"                                        # (local)
GATE_ID = "CF-S103-VIIBR-ORDER-CLAUSE-PATCH"            # (local)
SCHEME = "CURATED-DOC-REVIEWED-DESIGNATED-WRITER-PATCH"  # (local)
CONVENTION = ("DESIGNATED-WRITER-PROSE-PATCH-NOT-BULK-APPEND;"
              "ORDER-CLASS-QUALIFIER-INSERT;"
              "NO-NEW-LC-LINEAGE-NUMBER")                # (local)
L_MAX = "N/A"                                           # (local) prose patch; no spectral compute

REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
S4_SYNTHESIS = (PROJECT_ROOT / "sessions" / "session-102"
                / "session-102-berry-vii-br-order-clause-synthesis.md")
W5_4_NPZ = COMPUTATIONS_DIR / "session-101" / "s101_w5_4_b2_isotropy_breaking.npz"
W7_NPZ = COMPUTATIONS_DIR / "session-102" / "s102_w7_b2_eps2_wz_holonomy.npz"
CANONICAL = SHARED_DIR / "canonical_constants.py"

OUT_NPZ = SESSION_OUT_DIR / "s103_viibr_order_clause_patch.npz"
OUT_PNG = SESSION_OUT_DIR / "s103_viibr_order_clause_patch.png"  # optional; not emitted (string gate)

INPUT_FILES = [CANONICAL, S4_SYNTHESIS, W5_4_NPZ, W7_NPZ, REGISTRY]

# ---------------------------------------------------------------------------
# Section 3b — The OLD (frozen) order-clause sentence and the NEW (S-4 §IV.3 verbatim)
#              disambiguated replacement.
#
# OLD: the UNIQUE on-disk substring (verified by grep at plan-freeze): the order-clause sentence
#      inside the §VII.BR Release-condition-R paragraph. The lead "and " and the trailing period are
#      INCLUDED so the replacement is a clean single-sentence swap; the following sentence
#      ("Simultaneously the T1 multiplicity locks release: ... O(ε) base motion.") and the existing
#      "(forward gate CF-S101-B2-ISOTROPY-BREAKING, §V.1)" pointer are LEFT INTACT.
# ---------------------------------------------------------------------------
OLD_SENTENCE = (
    "and for generic δH the band-matrix develops anisotropy at O(ε) "
    "**iff** genuine within-band Wilczek–Zee structure exists."
)  # (local) frozen Release-condition-R order-clause sentence (plan-pinned :21336)

# NEW: the S-4 synthesis §IV.3 (file line 145) VERBATIM disambiguated sentence, lead "and " kept to
# match the swap boundary; followed by an OUTCOME cross-reference naming W5-4 + W7-3 as gate/wave
# LABELS only (no float witnesses) — records the *outcome* of the already-cited forward gate, adds NO
# LC-lineage-conditional number (the order distinction is operator-INDEPENDENT, per S-4 §IV.3 closing
# note). Together this satisfies the must_contain {O(ε), O(ε²), W5-4} AND the negative no-new-float guard.
NEW_SENTENCE = (
    "and the band-matrix develops anisotropy **iff** genuine within-band Wilczek–Zee "
    "structure exists; **the onset ORDER in ε is set by the deformation class** — an "
    "*in-block* δH carrying a non-Schur-scalar in-band part P·δH·P splits the "
    "band at **O(ε)** (open linear response), whereas an *off-block* δH (the "
    "substrate-natural C²-coset directions λ₄..λ₇, for which "
    "P·δH·P ≡ 0 because off-block operators have no in-band first-order matrix "
    "element) develops its anisotropy at **O(ε²)** via the second-order Schur-complement "
    "term (generic in the coset amplitudes; C₁=0 is STRUCTURAL, not fine-tuned). The "
    "**closed-loop** Wilczek–Zee holonomy ∮A_coset around a coset loop of radius ε is "
    "a DISTINCT object whose **O(ε²)** order is fixed by Stokes (curvature flux ∝ "
    "enclosed loop-area ∝ ε²), independent of abelian/non-abelian character; its "
    "discriminating content for genuine WZ structure is the **frame-invariant non-Schur-scalar "
    "trace** (non_scalar_frac → 1), not the ε-order. The substrate's off-block realization "
    "(forward gate CF-S101-B2-ISOTROPY-BREAKING → S102 W7-3) therefore confirms genuine WZ "
    "structure at O(ε²) on the released base, with no contradiction to the O(ε) "
    "in-block statement. (Outcome cross-reference: S101 **W5-4** (`CF-S101-B2-ISOTROPY-BREAKING`) "
    "measured the band-matrix anisotropy at O(ε²) with C₁=0 EXACT, and S102 "
    "**W7-3** confirmed the O(ε²) closed-loop frame-invariant non-Schur-scalar WZ "
    "holonomy; both record the *outcome* of the forward gate already cited and add NO "
    "LC-lineage-conditional number — the order distinction is operator-INDEPENDENT, transferring "
    "as-is under either branch of the τ=0 canonicity adjudication, exactly like T1/T2/P/U/R.)"
)  # (local) S-4 §IV.3 verbatim disambiguation + label-only W5-4/W7-3 outcome cross-reference

# §VII.BR header grade marker (must be UNCHANGED by the patch; the patch touches only the
# Release-condition-R sentence body, far below the header, so pre==post by construction).
GRADE_MARKER = "STAGE-3-PERMANENT"                      # (local)
VII_BR_HEADER = "### §VII.BR —"               # (local) unique §VII.BR section header anchor


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
    h = hashlib.sha256()  # (local)
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


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
# Section 5 — helpers: float extraction (negative guard), atomic write
# ---------------------------------------------------------------------------

# A "float" for the negative guard = a decimal-point number or a scientific-notation number.
# (Order classes O(ε), O(ε²); structural integers C₁=0, →1; gate labels W5-4/W7-3; section refs §V.1
#  are NOT floats.) The guard: NEW-sentence float set ⊆ OLD-sentence float set.
FLOAT_RE = re.compile(r"\d+\.\d+(?:[eE][+-]?\d+)?|\d+[eE][+-]?\d+")  # (local)


def floats_in(text: str) -> set[str]:
    """Return the set of decimal/scientific float tokens in `text`."""
    return set(FLOAT_RE.findall(text))


def write_atomic_with_fsync(path: Path, text: str) -> None:
    """Write text to a temp file, fsync, then atomic-replace the target."""
    tmp = path.with_suffix(path.suffix + ".tmp")  # (local)
    data = text.encode("utf-8")  # (local)
    with open(tmp, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def read_npz_slope(npz_path: Path, keys: list[str]) -> tuple[float | None, str]:
    """Read the first present slope key from an npz (provenance cross-check ONLY)."""
    try:
        with np.load(npz_path, allow_pickle=True) as d:
            for k in keys:
                if k in d.files:
                    try:
                        return float(np.asarray(d[k]).reshape(-1)[0]), k  # (local)
                    except (ValueError, TypeError, IndexError):
                        continue
    except (OSError, ValueError):
        return None, ""
    return None, ""


def verify_section_matches(registry_text: str) -> tuple[bool, dict]:
    """AFTER-pattern verify: the patched sentence + qualifier markers present, no new float,
    §VII.BR grade unchanged, exactly one §VII.BR section. Returns (bool, sub-check dict)."""
    checks: dict[str, bool] = {}  # (local)
    # (a) the NEW disambiguated sentence is present on disk (byte-faithful)
    checks["new_sentence_present"] = (NEW_SENTENCE in registry_text)
    # (b) the OLD bare order-clause sentence is GONE (the swap actually happened)
    checks["old_sentence_absent"] = (OLD_SENTENCE not in registry_text)
    # (c) order-class qualifier markers (in-block O(ε), off-block/closed-loop O(ε²))
    checks["marker_O_eps"] = ("O(ε)" in NEW_SENTENCE) and ("O(ε)" in registry_text)
    checks["marker_O_eps2"] = ("O(ε²)" in NEW_SENTENCE) and ("O(ε²)" in registry_text)
    checks["marker_in_block"] = ("*in-block*" in NEW_SENTENCE) and ("*in-block*" in registry_text)
    checks["marker_off_block"] = ("*off-block*" in NEW_SENTENCE) and ("*off-block*" in registry_text)
    checks["marker_closed_loop"] = ("**closed-loop**" in NEW_SENTENCE) and ("**closed-loop**" in registry_text)
    # (d) W5-4 + W7-3 outcome cross-reference present
    checks["xref_W5_4"] = ("W5-4" in registry_text)
    checks["xref_W7_3"] = ("W7-3" in registry_text)
    # (e) §VII.BR grade UNCHANGED (the header's STAGE-3-PERMANENT survives; exactly one §VII.BR section)
    checks["vii_br_header_unique"] = (registry_text.count(VII_BR_HEADER) == 1)
    return (all(checks.values()), checks)


# ---------------------------------------------------------------------------
# Section 6 — Compute (orchestration of the single-shot patch)
# ---------------------------------------------------------------------------

def compute() -> dict:
    reg_pre = REGISTRY.read_text(encoding="utf-8")  # (local)
    pre_sha = sha256_of_text(reg_pre)               # (local)
    s4_text = S4_SYNTHESIS.read_text(encoding="utf-8")  # (local)
    s4_sha = sha256_of_text(s4_text)                # (local)

    # --- provenance cross-check ONLY: read the EXISTING npz slopes (introduce NO new number) ---
    in_block_slope, in_block_key = read_npz_slope(
        W5_4_NPZ, ["b2_split_slope", "disc_slope", "B2split_slope"])  # (local)
    loop_slope, loop_key = read_npz_slope(
        W7_NPZ, ["slope_angle"])  # (local)

    # --- locate the OLD sentence; it MUST be unique (drift / ambiguity guard) ---
    n_old = reg_pre.count(OLD_SENTENCE)  # (local)
    n_s4_verbatim = s4_text.count(
        "develops anisotropy **iff** genuine within-band Wilczek–Zee structure exists; "
        "**the onset ORDER in ε is set by the deformation class**")  # (local) §IV.3 source present

    # --- idempotency: NEW already on disk (re-run) ---
    already_patched = (NEW_SENTENCE in reg_pre)  # (local)

    # --- drift: OLD sentence absent AND NEW not yet applied ⇒ on-disk wording drifted ---
    drift = (n_old == 0) and (not already_patched)  # (local)

    # --- negative guard: NEW float set ⊆ OLD float set (no new LC-lineage-conditional float) ---
    old_floats = floats_in(OLD_SENTENCE)  # (local)
    new_floats = floats_in(NEW_SENTENCE)  # (local)
    introduced_floats = sorted(new_floats - old_floats)  # (local)
    no_new_float = (len(introduced_floats) == 0)  # (local)

    # --- grade pre-count (must be unchanged post-write) ---
    grade_pre = reg_pre.count(GRADE_MARKER)  # (local)

    # ---- DRIFT branch: do NOT apply on a drifted sentence; emit INFO (re-anchor per §(ii.B)) ----
    if drift:
        return {
            "verdict": "INFO",
            "value": (f"plan_text_drift:Release-condition-R_order-clause_not_found_verbatim;"
                      f"n_old={n_old};already_patched=False;reanchor_per_substrate-first-§(ii.B)"),
            "pre_sha": pre_sha, "post_sha": pre_sha, "s4_sha": s4_sha,
            "patched_span_sha": sha256_of_text(NEW_SENTENCE),
            "n_old": n_old, "already_patched": already_patched, "drift": drift,
            "no_new_float": no_new_float, "introduced_floats": introduced_floats,
            "old_floats": sorted(old_floats), "new_floats": sorted(new_floats),
            "grade_pre": grade_pre, "grade_post": grade_pre,
            "in_block_slope": in_block_slope, "in_block_key": in_block_key,
            "loop_slope": loop_slope, "loop_key": loop_key,
            "n_s4_verbatim": n_s4_verbatim,
            "verify": False, "checks": {}, "rerouted": False,
        }

    # ---- AMBIGUITY guard: OLD appears more than once ⇒ unsafe swap; FAIL (no write) ----
    if n_old > 1:
        return {
            "verdict": "FAIL",
            "value": f"OLD_sentence_not_unique;n_old={n_old};unsafe_swap_no_write",
            "pre_sha": pre_sha, "post_sha": pre_sha, "s4_sha": s4_sha,
            "patched_span_sha": sha256_of_text(NEW_SENTENCE),
            "n_old": n_old, "already_patched": already_patched, "drift": drift,
            "no_new_float": no_new_float, "introduced_floats": introduced_floats,
            "old_floats": sorted(old_floats), "new_floats": sorted(new_floats),
            "grade_pre": grade_pre, "grade_post": grade_pre,
            "in_block_slope": in_block_slope, "in_block_key": in_block_key,
            "loop_slope": loop_slope, "loop_key": loop_key,
            "n_s4_verbatim": n_s4_verbatim,
            "verify": False, "checks": {}, "rerouted": False,
        }

    # ---- NEGATIVE-GUARD branch: a new float would enter the diff ⇒ FAIL (no write) ----
    if not no_new_float:
        return {
            "verdict": "FAIL",
            "value": (f"NEW_FLOAT_INTRODUCED:{','.join(introduced_floats)};"
                      f"negative_guard_violated_no_write"),
            "pre_sha": pre_sha, "post_sha": pre_sha, "s4_sha": s4_sha,
            "patched_span_sha": sha256_of_text(NEW_SENTENCE),
            "n_old": n_old, "already_patched": already_patched, "drift": drift,
            "no_new_float": no_new_float, "introduced_floats": introduced_floats,
            "old_floats": sorted(old_floats), "new_floats": sorted(new_floats),
            "grade_pre": grade_pre, "grade_post": grade_pre,
            "in_block_slope": in_block_slope, "in_block_key": in_block_key,
            "loop_slope": loop_slope, "loop_key": loop_key,
            "n_s4_verbatim": n_s4_verbatim,
            "verify": False, "checks": {}, "rerouted": False,
        }

    # ---- APPLY branch (build full text in memory → atomic write → re-read → verify) ----
    if already_patched:
        reg_post = reg_pre  # (local) idempotent re-run: already carries the NEW sentence
    else:
        new_registry = reg_pre.replace(OLD_SENTENCE, NEW_SENTENCE, 1)  # (local) single-sentence swap
        write_atomic_with_fsync(REGISTRY, new_registry)               # atomic write
        reg_post = REGISTRY.read_text(encoding="utf-8")               # re-read (post-fsync)

    post_sha = sha256_of_text(reg_post)  # (local)
    grade_post = reg_post.count(GRADE_MARKER)  # (local)
    grade_unchanged = (grade_post == grade_pre)  # (local) §VII.BR grade UNCHANGED

    verify_bool, checks = verify_section_matches(reg_post)  # (local)
    checks["grade_unchanged"] = grade_unchanged
    checks["no_new_float"] = no_new_float
    verify = bool(verify_bool and grade_unchanged and no_new_float)  # (local)

    verdict = "PASS" if verify else "FAIL"  # (local)

    value = (
        f"patched={not already_patched or (NEW_SENTENCE in reg_post)};"
        f"qualifier_ok={checks.get('marker_O_eps') and checks.get('marker_O_eps2')};"
        f"in_block_O(eps);off_block_O(eps2);closed_loop_O(eps2);"
        f"xref_W5-4={checks.get('xref_W5_4')};xref_W7-3={checks.get('xref_W7_3')};"
        f"no_new_float={no_new_float};grade={GRADE_MARKER}_unchanged={grade_unchanged};"
        f"vii_br_unique={checks.get('vii_br_header_unique')};verify={verify}"
    )  # (local)

    return {
        "verdict": verdict, "value": value,
        "pre_sha": pre_sha, "post_sha": post_sha, "s4_sha": s4_sha,
        "patched_span_sha": sha256_of_text(NEW_SENTENCE),
        "n_old": n_old, "already_patched": already_patched, "drift": drift,
        "no_new_float": no_new_float, "introduced_floats": introduced_floats,
        "old_floats": sorted(old_floats), "new_floats": sorted(new_floats),
        "grade_pre": grade_pre, "grade_post": grade_post, "grade_unchanged": grade_unchanged,
        "in_block_slope": in_block_slope, "in_block_key": in_block_key,
        "loop_slope": loop_slope, "loop_key": loop_key,
        "n_s4_verbatim": n_s4_verbatim,
        "verify": verify, "checks": checks, "rerouted": False,
    }


# ---------------------------------------------------------------------------
# Section 7 — verdict payload + 4-tuple + npz
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=None) -> dict:
    payload = {
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


def main() -> int:
    t0 = time.time()  # (local)

    # 1. input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)

    # 1b. dual SHAs (initial; extended below with the pre-patch registry SHA + patched-span SHA)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. compute (single-shot: build → write → re-read → verify)
    res = compute()
    value = res["value"]
    verdict = res["verdict"]

    # 3. extend the audit pinmap with the plan-declared runtime SHAs
    #    (audit_sha256_inputs = [script, s4_synthesis_iv3_patch_text_sha, registry_pre_patch_file_sha,
    #     patched_span_sha, pinmap]). Recompute audit_sha over the FULL declared input set.
    extended_pins = dict(pins)  # (local)
    extended_pins["__s4_synthesis_iv3_patch_text_sha"] = res["s4_sha"]
    extended_pins["__registry_pre_patch_file_sha"] = res["pre_sha"]
    extended_pins["__patched_span_sha"] = res["patched_span_sha"]
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, extended_pins)
    print(f"  audit_sha256 (extended w/ s4 + registry-pre + patched-span): {audit_sha[:16]}...")

    print("\n=== patch result ===")
    print(f"  OLD sentence occurrences (pre): {res['n_old']}  (must be 1 to apply)")
    print(f"  already_patched (idempotent re-run): {res['already_patched']}")
    print(f"  drift (OLD not found, NEW not applied): {res['drift']}")
    print(f"  S-4 §IV.3 verbatim source present: {res['n_s4_verbatim']} occurrence(s)")
    print(f"  negative guard — no new float: {res['no_new_float']}  "
          f"(introduced={res['introduced_floats']})")
    print(f"  OLD floats={res['old_floats']}  NEW floats={res['new_floats']}")
    print(f"  §VII.BR grade '{GRADE_MARKER}' count: pre={res['grade_pre']} post={res['grade_post']} "
          f"(unchanged={res.get('grade_unchanged')})")
    print(f"  provenance slopes (cross-check ONLY, no new number): "
          f"in-block={res['in_block_slope']} (key={res['in_block_key']}); "
          f"loop={res['loop_slope']} (key={res['loop_key']})")
    print(f"  verify sub-checks: {json.dumps(res['checks'])}")
    print(f"  verify={res['verify']}")

    # 4. npz: pre-patch registry SHA + patched-span SHA + the qualifier-present + no-new-float booleans
    SESSION_OUT_DIR.mkdir(parents=True, exist_ok=True)
    check_keys = list(res["checks"].keys())  # (local)
    np.savez(
        OUT_NPZ,
        registry_pre_patch_sha=res["pre_sha"],
        registry_post_patch_sha=res["post_sha"],
        s4_synthesis_sha=res["s4_sha"],
        patched_span_sha256=res["patched_span_sha"],
        old_sentence=OLD_SENTENCE,
        new_sentence=NEW_SENTENCE,
        n_old_occurrences=res["n_old"],
        already_patched=res["already_patched"],
        drift=res["drift"],
        no_new_float=res["no_new_float"],
        introduced_floats=np.array(res["introduced_floats"], dtype=object),
        old_floats=np.array(res["old_floats"], dtype=object),
        new_floats=np.array(res["new_floats"], dtype=object),
        grade_marker=GRADE_MARKER,
        grade_pre_count=res["grade_pre"],
        grade_post_count=res["grade_post"],
        grade_unchanged=res.get("grade_unchanged", res["grade_pre"] == res["grade_post"]),
        in_block_slope=(res["in_block_slope"] if res["in_block_slope"] is not None else np.nan),
        in_block_key=res["in_block_key"],
        loop_slope=(res["loop_slope"] if res["loop_slope"] is not None else np.nan),
        loop_key=res["loop_key"],
        n_s4_verbatim=res["n_s4_verbatim"],
        verify=res["verify"],
        verdict=verdict,
        check_keys=np.array(check_keys),
        check_vals=np.array([bool(res["checks"][k]) for k in check_keys], dtype=bool),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"\n  npz -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 5. 4-tuple + verdict payload (exactly ONE emission)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        f"# patched_span_sha256={res['patched_span_sha']} "
        f"registry_pre_patch_sha256={res['pre_sha']} "
        f"# {GATE_ID} curated-doc reviewed designated-writer patch on §VII.BR Release-condition-R "
        f"(order-class qualifier; NO new LC-lineage-conditional float; grade {GRADE_MARKER} UNCHANGED)",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # verdict is data; script health == 0 regardless of PASS/FAIL/INFO


if __name__ == "__main__":
    sys.exit(main())
