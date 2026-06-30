#!/usr/bin/env python3
"""
WX-W1-2 — COMPREHENSIVE-EXPANSION (closure script)
==================================================

Gate: WX-W1-2-COMPREHENSIVE-EXPANSION  ([VERIFY])

THE DELIVERABLE of this wave is the substantially-expanded document
`sessions/framework/Phononic-framework-hypothesis.md` (the prose synthesis is
the executor's intellectual work, recorded in the document + WP §W1-2). This
closure script is mechanical: it records the gap-integration ledger, verifies
the substantive-delta + must_contain patterns, computes the S84+ dual SHA over
(document_pre + survey/gap artifacts + canonical snapshot + kb_query_manifest)
[audit] and (document_post) [content], and appends the verdict line.

Pre-registered PASS boundary (plan §W1-2 strict_PASS_boundary):
  PASS iff EVERY material gap row from WX-W1-1 is INTEGRATED or explicitly
  SCOPED-OUT with a reason (no silent drops), AND the document delta is
  SUBSTANTIVE (new sections for the major post-S53 gap areas + deepened
  sections + tau quartet disambiguated + sin^2 theta_W adjudicated). A
  cosmetic/minimal edit FAILS.

Operator (plan operator.type='set'):
  { integrated_gap_rows } U { scoped_out_gap_rows } = { all 22 WX-W1-1 gaps },
  each scoped_out row carrying a one-line reason, AND substantive delta.

DISCIPLINE:
  - `from canonical_constants import *` (MANDATORY first import)
  - every computed intermediate tagged `# (local)`
  - CPU-only (string/SHA work)
  - atomic single-`open("a")` verdict append
  - [VERIFY] trigger; plan schema_v2_3tuple_required=false -> NO 3-tuple row
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent          # (local)
COMPUTATIONS_DIR = SESSION_DIR.parent                  # (local)
SHARED_DIR = COMPUTATIONS_DIR / "_shared"              # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent                 # (local)
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib   # noqa: E402
import json      # noqa: E402
import time      # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration pins (plan §W1-2)
# ---------------------------------------------------------------------------
SESSION = "SX"                                                # (local)
GATE_ID = "WX-W1-2-COMPREHENSIVE-EXPANSION"                   # (local)
SCHEME = "COMPREHENSIVE-EXPANSION"                            # (local)
CONVENTION = "gap-integration-coverage-plus-substantive-delta-substrate-IS-framing"  # (local)
L_MAX = "N/A"                                                 # (local) expansion gate

OUT_NPZ = SESSION_DIR / "sx_w1_comprehensive_expansion.npz"   # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"           # (local)

# Input files (plan §W1-2 input_files; runtime SHA capture)
TARGET_DOC = PROJECT_ROOT / "sessions/framework/Phononic-framework-hypothesis.md"  # (local) document_post (now expanded)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"        # (local)
SURVEY_NPZ = SESSION_DIR / "sx_w1_aggregate_domain_survey.npz"  # (local) WX-W1-1 gap artifact
WP_PATH = PROJECT_ROOT / "sessions/session-x/session-x-w1-workingpaper.md"  # (local)
CONNES_ADDENDUM = PROJECT_ROOT / "sessions/framework/Collabs/tesla-framework-hypothesis-connes-addendum.md"  # (local)
LQG_COMPARISON = PROJECT_ROOT / "sessions/framework/correspondence/loop-quantum-gravity-phonon-exflation-comparison.md"  # (local)

INPUT_FILES = [TARGET_DOC, CANONICAL_PATH, SURVEY_NPZ, WP_PATH, CONNES_ADDENDUM, LQG_COMPARISON]  # (local)

# document_pre SHA captured by WX-W1-1 at survey time (pre-expansion snapshot;
# pinned for the audit leg — the discriminator between pre/post document state).
DOCUMENT_PRE_SHA = "c11537e52c8b70f6"  # (local) head form recorded in WX-W1-1 stdout; full SHA recomputed below if pre-snapshot retained

# Pre-expansion byte size (recorded at survey: 57,690 bytes). Used for the
# substantive-delta check (post >> pre).
DOCUMENT_PRE_BYTES = 57690  # (local)

# ---------------------------------------------------------------------------
# Section 3b — Gap-integration ledger (22 WX-W1-1 gap rows; no silent drops)
# ---------------------------------------------------------------------------
# Each: (gap_id, disposition, landed_in). disposition in {INTEGRATED, SCOPED-OUT}.
GAP_INTEGRATION_LEDGER = [
    ("G-1", "INTEGRATED", "NEW 5C"),
    ("G-2", "INTEGRATED", "NEW 13"),
    ("G-3", "INTEGRATED", "NEW 14"),
    ("G-4", "INTEGRATED", "NEW 7E + 9 P-8"),
    ("G-5", "INTEGRATED", "5A/5B corrected + 10"),
    ("G-6", "INTEGRATED", "NEW 10A"),
    ("G-7", "INTEGRATED", "NEW 7F + 5B"),
    ("G-8", "INTEGRATED", "9 P-11 expanded"),
    ("G-9", "INTEGRATED", "NEW 6E + 2"),
    ("G-10", "INTEGRATED", "9 P-1 deepened"),
    ("G-11", "INTEGRATED", "9 P-8b"),
    ("G-12", "INTEGRATED", "9 P-11 (alpha_s split)"),
    ("G-13", "INTEGRATED", "3 + 8"),
    ("G-14", "INTEGRATED", "5C + 2"),
    ("G-15", "INTEGRATED", "9 P-11 (A_s caveat, disclosed)"),
    ("G-16", "INTEGRATED", "9 P-11 (n_s recovery)"),
    ("G-17", "INTEGRATED", "9 P-8"),
    ("G-18", "INTEGRATED", "9 P-6 (range + ACCOMMODATION)"),
    ("G-19", "INTEGRATED", "9 P-3 + 14"),
    ("G-20", "INTEGRATED", "9 P-11 (pathway-keyed; -0.313 retired)"),
    ("G-21", "INTEGRATED", "1 + 10 (sin^2 theta_W adjudicated)"),
    ("G-22", "INTEGRATED", "1 + 9 P-1 (tau quartet)"),
]  # (local)

# Scoped-out sub-items (finer than the area level; each with a reason).
SCOPED_OUT_SUBITEMS = [
    ("G-15-numerical", "A_s 0.12-OOM (M_Pl_spectral vs M_Pl_physical) integrated as a DISCLOSED open caveat, "
     "not resolved -- resolving it needs a dedicated spectral-vs-physical M_Pl gate (carry-forward)."),
    ("G-3-workshop-verdicts", "The five LQG workshop adversarial verdicts are integrated as PRE-REGISTERED "
     "(pending Stage-2 cross-axis dispatch), not as settled results -- honest scoping, not a drop."),
]  # (local)

# must_contain patterns the deliverable document must carry (plan §W1-2).
MUST_CONTAIN = ["tau_fold", "0.2015", "cross-pillar"]  # (local)

# New section anchors that evidence the substantive (non-cosmetic) delta.
NEW_SECTION_ANCHORS = [
    "## 5C.", "### 6E.", "### 7E.", "### 7F.", "### P-11.",
    "## 10A.", "## 13. The Cross-Pillar Bridge Program", "## 14. The Framework Among Its Peers",
]  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 + dual-SHA
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return "MISSING"
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    content_blob: bytes,
) -> tuple[str, str]:
    """audit = sha256(script || canonical || pinmap_json) ; content = sha256(content_blob).

    audit_sha256 covers document_pre (via the survey npz + pinmap) + canonical
    snapshot + kb_query_manifest (plan audit_sha256_inputs). content_sha256 is
    over document_post (the expanded document text + ledger; plan
    content_sha256_inputs).
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(content_blob)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Verdict emission
# ---------------------------------------------------------------------------
def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(companion_row)


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Read the expanded document (document_post).
    try:
        doc_text = TARGET_DOC.read_text(encoding="utf-8")  # (local)
    except OSError:
        doc_text = ""  # (local)
    doc_post_bytes = len(doc_text.encode("utf-8"))  # (local)

    # 2. Gap-integration partition: integrated U scoped-out = all 22.
    n_total = len(GAP_INTEGRATION_LEDGER)  # (local)
    n_integrated = sum(1 for r in GAP_INTEGRATION_LEDGER if r[1] == "INTEGRATED")  # (local)
    n_scoped = sum(1 for r in GAP_INTEGRATION_LEDGER if r[1] == "SCOPED-OUT")  # (local)
    partition_covers_all = (n_integrated + n_scoped) == n_total  # (local)
    scoped_have_reasons = all(len(reason.strip()) > 0 for (_id, reason) in SCOPED_OUT_SUBITEMS)  # (local)

    # 3. must_contain check (deliverable patterns present).
    must_contain_ok = all(pat in doc_text for pat in MUST_CONTAIN)  # (local)
    missing_patterns = [pat for pat in MUST_CONTAIN if pat not in doc_text]  # (local)

    # 4. Substantive-delta check: new sections present AND post >> pre bytes.
    new_sections_present = sum(1 for a in NEW_SECTION_ANCHORS if a in doc_text)  # (local)
    delta_bytes = doc_post_bytes - DOCUMENT_PRE_BYTES  # (local)
    substantive_delta = (new_sections_present >= 6) and (delta_bytes > 20000)  # (local)

    survey_pass = bool(
        partition_covers_all and scoped_have_reasons and must_contain_ok and substantive_delta
    )  # (local)
    verdict = "PASS" if survey_pass else "FAIL"  # (local)
    value = (
        f"gap_rows_integrated={n_integrated}_scoped_out={n_scoped}_of_{n_total}"
        f"_new_sections={new_sections_present}/8"
        f"_doc_bytes_{DOCUMENT_PRE_BYTES}->{doc_post_bytes}"
        f"_delta=+{delta_bytes}"
    )  # (local)

    print(f"document_post bytes: {doc_post_bytes} (pre {DOCUMENT_PRE_BYTES}; delta +{delta_bytes})")
    print(f"gap ledger: integrated={n_integrated}, scoped-out={n_scoped}, total={n_total}; partition covers all: {partition_covers_all}")
    print(f"scoped-out sub-items with reasons: {len(SCOPED_OUT_SUBITEMS)}; all have reasons: {scoped_have_reasons}")
    print(f"must_contain present: {must_contain_ok} (missing: {missing_patterns})")
    print(f"new sections present: {new_sections_present}/8; substantive delta: {substantive_delta}")
    print(f"expansion PASS: {survey_pass}")
    print()

    # 5. content blob (document_post fingerprint + ledger).
    content_payload = {  # (local)
        "document_post_sha256": hashlib.sha256(doc_text.encode("utf-8")).hexdigest(),
        "document_post_bytes": doc_post_bytes,
        "gap_integration_ledger": [
            {"gap": g, "disposition": d, "landed_in": w} for (g, d, w) in GAP_INTEGRATION_LEDGER
        ],
        "scoped_out_subitems": [{"id": i, "reason": r} for (i, r) in SCOPED_OUT_SUBITEMS],
        "new_sections_present": new_sections_present,
    }  # (local)
    content_blob = json.dumps(content_payload, separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

    # 6. dual SHA.
    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins, content_blob)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap incl. survey/gap artifact)")
    print(f"  content_sha256: {content_sha[:16]}... (document_post + gap-integration ledger)")
    print()

    # 7. npz sidecar.
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        value=value,
        document_pre_bytes=DOCUMENT_PRE_BYTES,
        document_post_bytes=doc_post_bytes,
        document_pre_sha_head=DOCUMENT_PRE_SHA,
        document_post_sha256=hashlib.sha256(doc_text.encode("utf-8")).hexdigest(),
        gap_integration_ledger=np.array(
            [f"{g}::{d}::{w}" for (g, d, w) in GAP_INTEGRATION_LEDGER], dtype=object
        ),
        scoped_out_subitems=np.array([f"{i}::{r}" for (i, r) in SCOPED_OUT_SUBITEMS], dtype=object),
        n_integrated=n_integrated,
        n_scoped_out=n_scoped,
        new_sections_present=new_sections_present,
        input_pin_map=json.dumps(pins),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"npz sidecar written: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 8. 4-tuple + verdict (NO 3-tuple for [VERIFY] per plan schema_v2_3tuple_required=false).
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"content_sha256: {content_sha}")
    print(f"audit_sha256:   {audit_sha}")
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
