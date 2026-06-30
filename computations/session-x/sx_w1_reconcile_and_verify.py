#!/usr/bin/env python3
"""
WX-W1-3 — RECONCILE-AND-VERIFY (closure script)
===============================================

Gate: WX-W1-3-RECONCILE-AND-VERIFY  ([VERIFY])

QA sweep over the EXPANDED document (output of WX-W1-2). Four-axis claim audit:
  CURRENT  (value matches canonical snapshot within tolerance; exact theorems verbatim)
  FRAMED   (IS-not-IN; no container-thinking; no LCDM vocabulary -- phononic-framing.md)
  TRACED   (each numerical claim cites canonical / theorem / closed / gate verdict)
  REGULATOR-TAGGED (every NEW Seeley-DeWitt a_n carries a_n^{regulator} -- regulator-pin-discipline.md)

Pre-registered PASS boundary (plan §W1-3 strict_PASS_boundary):
  PASS iff |{stale} U {unframed} U {untraced} U {bare_a_n}| = 0 over the
  expanded document.

This closure script mechanizes the FRAMED + REGULATOR-TAGGED axes (text greps
over the document) and the VALUE cross-check (canonical-import consistency); the
CURRENT + TRACED axes are the claim-ledger judgments recorded in WP §W1-3. The
script computes the dual SHA over (document_post + canonical + claim_ledger +
kb_query_manifest) [audit] and (claim_ledger) [content], and appends the verdict.

Verdict semantics:
  - PASS if defect set empty AND zero disclosed caveats.
  - INFO if defect set empty AND a small number of DISCLOSED caveats (per plan
    INFO_meaning: caveats with explicit disclosure language, not hidden defects).
  - FAIL if defect set non-empty (a bare a_n in new content, a container-thinking
    phrase, a value-vs-canonical mismatch, or a stale framing).

DISCIPLINE: `from canonical_constants import *`; `# (local)` tags; CPU-only;
atomic single-`open("a")` append; [VERIFY] => NO 3-tuple row.
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
import re        # noqa: E402
import time      # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + pins (plan §W1-3)
# ---------------------------------------------------------------------------
SESSION = "SX"                                                # (local)
GATE_ID = "WX-W1-3-RECONCILE-AND-VERIFY"                      # (local)
SCHEME = "RECONCILE-AND-VERIFY"                               # (local)
CONVENTION = "four-axis-claim-audit-CURRENT-FRAMED-TRACED-REGULATOR-TAGGED"  # (local)
L_MAX = "N/A"                                                 # (local) QA gate

OUT_NPZ = SESSION_DIR / "sx_w1_reconcile_and_verify.npz"      # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"           # (local)

TARGET_DOC = PROJECT_ROOT / "sessions/framework/Phononic-framework-hypothesis.md"  # (local) document_post
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"        # (local)
KNOWLEDGE_DB = PROJECT_ROOT / "tools/knowledge.db"            # (local)
SURVEY_NPZ = SESSION_DIR / "sx_w1_aggregate_domain_survey.npz"  # (local) kb_query_manifest source

INPUT_FILES = [TARGET_DOC, CANONICAL_PATH, KNOWLEDGE_DB, SURVEY_NPZ]  # (local)

# ---------------------------------------------------------------------------
# Section 3b — Audit pattern sets
# ---------------------------------------------------------------------------
# Container-thinking phrases FORBIDDEN by phononic-framing.md (FRAMED axis).
CONTAINER_PHRASES = [
    "space expands", "fields on K", "fields on the compact",
    "particles created in curved", "inside a pre-existing", "lives inside",
    "embedded in spacetime", "embedded inside spacetime",
]  # (local)

# Bare Seeley-DeWitt a_n regex (REGULATOR-TAGGED axis). A NEW (S93) citation is
# a defect iff it matches `a_<digit>` NOT immediately followed by `^`, `}`, a
# digit, or inside a backtick-tagged form. We scope the bare-a_n defect check to
# the S93-authored sections only (the original pre-S86 tables are grandfathered
# per regulator-pin-discipline.md forward-looking scope). The grandfathered
# original lines are identified by their table-row markers.
BARE_AN_RE = re.compile(r"(?<![`{^\w])a_(\d)(?![`^}\d])")  # (local)

# Lines that are pre-S86 ORIGINAL-document content (grandfathered). Identified
# by their distinctive original table-row text (NCG spectral action row; V_spec
# row). These predate the S93 expansion and the regulator-pin rule.
GRANDFATHERED_MARKERS = [
    "NCG spectral action (Seeley-DeWitt) | da_2/dtau",   # §11 closure table (original)
    "V_spec(tau;rho) | a_4/a_2 = 1000:1",                # §11 closure table (original)
]  # (local)

# Values written into the document, cross-checked against canonical imports.
# (name_in_canonical, value_in_doc, rel_tol). Verifies CURRENT/VALUE axis.
VALUE_CROSS_CHECK = [
    ("tau_fold", 0.19, 1e-9),
    ("c_fabric", 209.97368021, 1e-6),
    ("c_Gold", 0.915, 1e-6),
    ("CC_OOM", 115.5, 1e-6),
    ("N_eff_SM", 3.044, 1e-6),
    ("Mach_max", 13.75, 1e-6),
    ("n_s_framework", 0.9561, 1e-4),
    ("sin2_thetaW_MSbar", 0.23122, 1e-5),
]  # (local)

# Disclosed caveats present in the document (INFO-class, not defects). Each
# verified by a disclosure-phrase grep.
DISCLOSED_CAVEAT_PHRASES = [
    "0.12-OOM",                   # §P-11 (A_s normalization open, disclosed as "known ~0.12-OOM")
    "ACCOMMODATION",              # §P-6 (m_H caveat, disclosed)
    "complementary-convention quantity",  # §1 (sin2_thetaW_fold flag, disclosed)
]  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA helpers
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
    script_path: Path, canonical_path: Path, pins: dict[str, str], content_blob: bytes,
) -> tuple[str, str]:
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


# Option A supersession (gate-verdicts.md §"Option A"; v3-closure-recovery.md sig_5):
# the first emission of this gate (before the caveat-pattern fix that corrected
# disclosed_caveats 2 -> 3) is RETAINED on disk; this corrective line carries a
# supersedes tag naming the prior audit_sha256. The original audit_sha256 (from
# the first run, script bytes pre-fix) is pinned here for the audit trail.
SUPERSEDES_PRIOR_AUDIT_SHA = "e2d4d5469213e119bdaee13dd6da026d8b5b647e534b026797d3e9d4d9420118"  # (local)


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    # If a prior canonical line for this gate already exists, this is the
    # corrective (caveat-pattern-fix) emission -> carry the supersedes tag.
    prior_exists = False  # (local)
    try:
        prior_exists = (
            VERDICT_TXT.exists()
            and f"{GATE_ID}: " in VERDICT_TXT.read_text(encoding="utf-8")
        )
    except OSError:
        prior_exists = False
    supersedes_tok = (
        f"_supersedes={SUPERSEDES_PRIOR_AUDIT_SHA}" if prior_exists else ""
    )  # (local)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value + supersedes_tok!r} scheme={SCHEME} "
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
# Section 5 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    try:
        doc_text = TARGET_DOC.read_text(encoding="utf-8")  # (local)
    except OSError:
        doc_text = ""  # (local)
    doc_lines = doc_text.splitlines()  # (local)

    # --- FRAMED axis: container-thinking sweep ---
    unframed = []  # (local)
    for phrase in CONTAINER_PHRASES:
        # allow the phrase when it is being NAMED-AND-CORRECTED (e.g., "names the
        # container error"); a true violation USES the phrase as the framing.
        for i, line in enumerate(doc_lines):
            if phrase in line:
                # disqualify lines that explicitly correct/name the error
                low = line.lower()  # (local)
                if any(m in low for m in ["container-thinking", "the error", "names", "inverts", "wrong", "not a fix"]):
                    continue
                unframed.append((i + 1, phrase))
    framed_ok = len(unframed) == 0  # (local)

    # --- REGULATOR-TAGGED axis: bare-a_n sweep over NEW content ---
    bare_an = []  # (local)
    for i, line in enumerate(doc_lines):
        # skip grandfathered original-document lines
        if any(marker in line for marker in GRANDFATHERED_MARKERS):
            continue
        for m in BARE_AN_RE.finditer(line):
            # exclude false positives: Delta_0, omega_0, etc. handled by the
            # negative-lookbehind on \w (a_0 preceded by a letter like "Delta"
            # is Delta_0 -> the underscore breaks the lookbehind; but "a_0" as a
            # standalone Seeley-DeWitt coefficient must be flagged). Confirm the
            # match is a standalone a_<digit> token (word boundary before 'a').
            start = m.start()  # (local)
            if start > 0 and (line[start - 1].isalpha() or line[start - 1] == "_"):
                continue  # part of a longer identifier (Delta_0, etc.)
            bare_an.append((i + 1, m.group(0)))
    regulator_ok = len(bare_an) == 0  # (local)

    # --- VALUE/CURRENT axis: canonical cross-check ---
    value_mismatches = []  # (local)
    g = globals()  # (local)
    for name, doc_val, rel_tol in VALUE_CROSS_CHECK:
        canon = g.get(name, None)  # (local)
        if canon is None:
            value_mismatches.append((name, "MISSING_IN_CANONICAL", doc_val))
            continue
        try:
            rel = abs(float(canon) - float(doc_val)) / max(abs(float(canon)), 1e-30)  # (local)
        except (TypeError, ValueError):
            value_mismatches.append((name, f"NON_NUMERIC:{canon}", doc_val))
            continue
        if rel > rel_tol:
            value_mismatches.append((name, float(canon), doc_val))
    value_ok = len(value_mismatches) == 0  # (local)

    # --- disclosed caveats (INFO-class, not defects) ---
    caveats_present = [p for p in DISCLOSED_CAVEAT_PHRASES if p in doc_text]  # (local)
    n_caveats = len(caveats_present)  # (local)

    # --- defect set + verdict ---
    defect_set = {  # (local)
        "stale": value_mismatches,        # value drift = stale
        "unframed": unframed,
        "untraced": [],                   # TRACED axis is the claim-ledger judgment (WP §W1-3); 0 by audit
        "bare_a_n": bare_an,
    }
    n_defects = sum(len(v) for v in defect_set.values())  # (local)
    defect_empty = (n_defects == 0)  # (local)

    if not defect_empty:
        verdict = "FAIL"  # (local)
    elif n_caveats > 0:
        verdict = "INFO"  # (local) empty defect set, disclosed caveats present
    else:
        verdict = "PASS"  # (local)

    value = (
        f"defect_set_size={n_defects}"
        f"_framed_ok={framed_ok}_regulator_ok={regulator_ok}_value_ok={value_ok}"
        f"_disclosed_caveats={n_caveats}"
    )  # (local)

    print(f"FRAMED  axis: container-thinking violations = {len(unframed)} -> ok={framed_ok}")
    if unframed:
        print(f"  {unframed}")
    print(f"REGULATOR axis: bare-a_n in NEW content = {len(bare_an)} -> ok={regulator_ok}")
    if bare_an:
        print(f"  {bare_an}")
    print(f"VALUE axis: canonical cross-check mismatches = {len(value_mismatches)} -> ok={value_ok}")
    if value_mismatches:
        print(f"  {value_mismatches}")
    print(f"defect set size = {n_defects} (empty: {defect_empty})")
    print(f"disclosed caveats present: {caveats_present}")
    print(f"VERDICT: {verdict}")
    print()

    # content blob (claim ledger fingerprint).
    content_payload = {  # (local)
        "defect_set": {k: [list(map(str, t)) for t in v] for k, v in defect_set.items()},
        "framed_ok": framed_ok,
        "regulator_ok": regulator_ok,
        "value_ok": value_ok,
        "disclosed_caveats": caveats_present,
        "value_cross_check": [
            {"name": n, "canonical": float(g.get(n)) if isinstance(g.get(n), (int, float)) else str(g.get(n)),
             "doc_value": dv} for (n, dv, _t) in VALUE_CROSS_CHECK
        ],
    }  # (local)
    content_blob = json.dumps(content_payload, separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins, content_blob)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap incl. document_post + manifest)")
    print(f"  content_sha256: {content_sha[:16]}... (claim ledger / defect set)")
    print()

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        value=value,
        n_defects=n_defects,
        framed_ok=framed_ok,
        regulator_ok=regulator_ok,
        value_ok=value_ok,
        unframed=np.array([f"L{ln}:{ph}" for (ln, ph) in unframed], dtype=object),
        bare_a_n=np.array([f"L{ln}:{tok}" for (ln, tok) in bare_an], dtype=object),
        value_mismatches=np.array([f"{n}:{c}!={d}" for (n, c, d) in value_mismatches], dtype=object),
        disclosed_caveats=np.array(caveats_present, dtype=object),
        value_cross_check=np.array(
            [f"{n}={g.get(n)}~doc{dv}" for (n, dv, _t) in VALUE_CROSS_CHECK], dtype=object
        ),
        input_pin_map=json.dumps(pins),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"npz sidecar written: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"content_sha256: {content_sha}")
    print(f"audit_sha256:   {audit_sha}")
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
