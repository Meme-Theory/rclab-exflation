#!/usr/bin/env python3
"""
S101 W6-7 — S101-HK-PMNS-PIN-PROMOTION (PMNS version-sub-keyed canonical promotion verify)
==========================================================================================

Gate: S101-HK-PMNS-PIN-PROMOTION ([VERIFY])

Pre-registered threshold (conjunction; any miss = FAIL):
  PASS iff ALL of:
    (A) the FOUR version-sub-keyed PMNS names import from canonical_constants with
        EXACT pinned values
          sin2_theta12_PDG     -> 0.307
          sin2_theta13_PDG     -> 0.0220
          sin2_theta12_NuFit60 -> 0.303
          sin2_theta13_NuFit60 -> 0.02225
    (B) FOUR PROVENANCE entries present (one per name) AND the W5-2 consumption
        citation present (the S100a-D5-0NUBB-MAJORANA audit a2d29b97...) in the
        canonical_constants.py text;
    (C) the line-~2119/2135 allowlist token cluster carries the
        SUPERSEDED-BY-CANONICAL annotation naming the four new constants, with the
        tokens sin2_12_pdg + sin2_13_pdg RETAINED and sin2_23_pdg untouched;
    (D) the W5-2 source script s100a_d5_0nubb_majorana.py is UNCHANGED
        (sha256 == 9ddd1ba5...966945 -- its content_sha256 is a verdict-file commitment).
  FAIL iff any conjunct misses.

This is a constants-HYGIENE promotion-of-external-pins gate. The promotion itself
(4x update_constant + the allowlist annotation Edit) was performed by the dispatching
agent BEFORE this script runs; the script COMPUTES the PASS predicate (verification-
before-verdict order, per the plan's OPERATIONAL SEQUENCE). The canonical write-order's
verdict-first clause targets NEW framework predictions; these are LABORATORY-IN
observational anchors (oscillation-fit centrals), not framework predictions -- so the
honest order is verification-first (the PASS criterion is COMPUTED, not promised).

Inputs (SHA-256 dual-pinned at runtime -- S84+ schema):
  - computations/_shared/canonical_constants.py (edit target; feeds audit_sha256)
  - computations/session-100a/s100a_d5_0nubb_majorana.py (frozen source; SHA asserted)
  - sessions/session-100a/session-100a-housekeeping.md (CF-W5-1 provenance pin)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<promo-record>, scheme=CANONICAL-PROMOTION,
   convention=VERSION-SUB-KEYED-PAIR-OF-PAIRS, L_max=N/A)

Classification: NON-PHONONIC (methodology / constants hygiene).

SUBSTRATE FRAMING
-----------------
NON-PHONONIC. The PMNS electron-row pins are laboratory-IN observational anchors
(oscillation-experiment fit centrals), NOT substrate-IS quantities. The substrate's own
neutrino content enters through the D_K bottom-triple maps (W5-1 lineage); these pins are
the external comparison surface the 0nubb funnel gates measure against. The methodology
contribution: version-honest sub-keying kills a silent class-conflation
(NuFit-5.x-values-under-a-6.0-label) at the canonical-sourcing layer, per
substrate-first-canonical-sourcing.md -- external-paper values enter as named,
version-tagged METHODOLOGICAL anchors, never as mislabeled canonical replacements.

DISCIPLINE
----------
- `from canonical_constants import *` (MANDATORY first import)
- Every local/intermediate tagged `# (local)`
- No linear algebra -> no GPU path; deterministic
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Verdict via the `emit_verdict` knowledge-MCP tool (race-safe). This script PRINTS the
  payload via print_verdict_payload; the dispatching AGENT calls emit_verdict. The script
  does NOT write s101_gate_verdicts.txt directly. Single emission; no iterate-until-PASS
  (a failed import is script/env breakage -> exit != 0; fix-and-rerun is breakage
  remediation, NOT verdict shopping).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# Explicit named imports of the FOUR promotion targets (the gate's conjunct A).
# A failed import here is environment/promotion breakage (exit != 0), the honest
# script-health signal -- NOT a verdict.
from canonical_constants import (  # noqa: F401
    sin2_theta12_PDG,
    sin2_theta13_PDG,
    sin2_theta12_NuFit60,
    sin2_theta13_NuFit60,
)

# The allowlist frozenset is a private (underscore-prefixed) name, so the star-import
# above does NOT export it; import it explicitly for the conjunct-C token-retention check.
from canonical_constants import _HARDCODE_IGNORE_NAMES  # noqa: F401

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import math
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

SESSION = "S101"                                                   # (local)
GATE_ID = "S101-HK-PMNS-PIN-PROMOTION"                             # (local)
SCHEME = "CANONICAL-PROMOTION"                                    # (local)
CONVENTION = "VERSION-SUB-KEYED-PAIR-OF-PAIRS"                     # (local)
L_MAX = "N/A"                                                     # (local)

# Publication precision: 3-4 sig fig published centrals -> rel_tol >= 1e-3 (Class 8.3).
# Values are float-literal round-trips, so exact equality is also expected; we assert
# BOTH the EXACT literal AND the rel_tol band for robustness.
REL_TOL = 1e-3                                                    # (local) Class 8.3 floor

# Pre-registered EXACT pinned values (BINDING; transcribed from housekeeping CF-W5-1).
EXPECTED = {                                                      # (local)
    "sin2_theta12_PDG": 0.307,
    "sin2_theta13_PDG": 0.0220,
    "sin2_theta12_NuFit60": 0.303,
    "sin2_theta13_NuFit60": 0.02225,
}
IMPORTED = {                                                      # (local)
    "sin2_theta12_PDG": sin2_theta12_PDG,
    "sin2_theta13_PDG": sin2_theta13_PDG,
    "sin2_theta12_NuFit60": sin2_theta12_NuFit60,
    "sin2_theta13_NuFit60": sin2_theta13_NuFit60,
}

# W5-2 consumption citation (full-64 audit_sha256 of the landed S100a-D5 verdict line 31).
W52_CONSUMPTION_AUDIT = (                                         # (local)
    "a2d29b975d8cb170dc561a35034a24c8f8d3900358ae2e0c84465e499b34bbc6"
)
# Frozen source-script SHA (its content_sha256 is a verdict-file commitment).
SOURCE_SCRIPT_SHA_EXPECTED = (                                    # (local)
    "9ddd1ba53d9c4f2fc4a1aef8f639d678e981e602f7c240cb7afa09e654966945"
)
# -0.60% decision-irrelevant m_bb shift (transcribed from W5-2 (d2); never re-derived).
MBB_SHIFT_PDG_TO_NUFIT60_PCT = -0.60                             # (local) transcribed

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"            # (local)
SOURCE_SCRIPT_PATH = (                                            # (local)
    COMPUTATIONS_DIR / "session-100a" / "s100a_d5_0nubb_majorana.py"
)
HOUSEKEEPING_PATH = (                                             # (local)
    PROJECT_ROOT / "sessions" / "session-100a" / "session-100a-housekeeping.md"
)

OUT_NPZ = SESSION_DIR / "s101_w6_7_pmns_pin_promotion.npz"

INPUT_FILES = [
    CANONICAL_PATH,
    SOURCE_SCRIPT_PATH,
    HOUSEKEEPING_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block + dual-SHA (S84+)
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


def compute_dual_sha(
    script_path: Path, canonical_path: Path, pins: dict[str, str]
) -> tuple[str, str]:
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
# Section 5 — Compute (the four conjuncts)
# ---------------------------------------------------------------------------

def compute() -> dict:
    canon_text = CANONICAL_PATH.read_text(encoding="utf-8")  # (local)

    # --- Conjunct A: four imports exact ---
    import_results = {}  # (local)
    a_all = True  # (local)
    for name, expected in EXPECTED.items():
        got = IMPORTED[name]  # (local)
        exact = (got == expected)  # (local) float-literal round-trip
        within_tol = math.isclose(got, expected, rel_tol=REL_TOL)  # (local) Class 8.3
        ok = bool(exact and within_tol)  # (local)
        import_results[name] = {
            "expected": expected, "got": float(got),
            "exact": bool(exact), "within_tol": bool(within_tol), "ok": ok,
        }
        a_all = a_all and ok
    A_pass = bool(a_all)  # (local)

    # --- Conjunct B: four PROVENANCE entries + consumption citation ---
    # update_constant lands BOTH an inline-commented assignment line AND a PROVENANCE
    # dict row per name. Require, per name: an assignment line `name = value` AND a
    # PROVENANCE dict row `"name": {...}`.
    prov_results = {}  # (local)
    b_all = True  # (local)
    for name in EXPECTED:
        assign_present = (f"\n{name} = " in canon_text)  # (local) assignment line
        prov_row_present = (f'"{name}":' in canon_text)  # (local) PROVENANCE dict row
        ok = bool(assign_present and prov_row_present)  # (local)
        prov_results[name] = {
            "assign_present": bool(assign_present),
            "prov_row_present": bool(prov_row_present),
            "ok": ok,
        }
        b_all = b_all and ok
    # consumption citation: the S100a-D5 audit appears in the new provenance text
    consumption_cite_present = bool(W52_CONSUMPTION_AUDIT in canon_text)  # (local)
    B_pass = bool(b_all and consumption_cite_present)  # (local)

    # --- Conjunct C: allowlist SUPERSEDED-BY-CANONICAL annotation + token retention ---
    annotation_present = bool(
        "SUPERSEDED-BY-CANONICAL (S101-HK-PMNS-PIN-PROMOTION)" in canon_text
    )  # (local)
    # annotation must NAME the four new constants
    annotation_names_all = all(
        name in canon_text for name in EXPECTED
    )  # (local) (trivially true via assignment lines too; explicit naming verified below)
    # tokens RETAINED in the frozenset (import-back from the live module)
    tok12_retained = ("sin2_12_pdg" in _HARDCODE_IGNORE_NAMES)  # (local)
    tok13_retained = ("sin2_13_pdg" in _HARDCODE_IGNORE_NAMES)  # (local)
    tok23_untouched = ("sin2_23_pdg" in _HARDCODE_IGNORE_NAMES)  # (local) out-of-scope
    # the annotation text itself names sin2_theta12_PDG + sin2_theta13_NuFit60 (the
    # pair-of-pairs corners) and references the retained/out-of-scope tokens
    annotation_corner_names = bool(
        "sin2_theta12_PDG=0.307" in canon_text
        and "sin2_theta13_NuFit60=0.02225" in canon_text
    )  # (local)
    annotation_token_disposition = bool(
        "RETAINED" in canon_text and "OUT OF SCOPE" in canon_text
    )  # (local)
    C_pass = bool(
        annotation_present and annotation_names_all and annotation_corner_names
        and annotation_token_disposition
        and tok12_retained and tok13_retained and tok23_untouched
    )  # (local)

    # --- Conjunct D: source script UNCHANGED ---
    source_sha = sha256_of(SOURCE_SCRIPT_PATH)  # (local)
    D_pass = bool(source_sha == SOURCE_SCRIPT_SHA_EXPECTED)  # (local)

    overall = bool(A_pass and B_pass and C_pass and D_pass)  # (local)
    n_imports_ok = sum(1 for r in import_results.values() if r["ok"])  # (local) /4 count

    return {
        "value": (
            f"PMNS-pins-promoted:PAIR-OF-PAIRS;"
            f"sin2_theta12_PDG={EXPECTED['sin2_theta12_PDG']},"
            f"sin2_theta13_PDG={EXPECTED['sin2_theta13_PDG']},"
            f"sin2_theta12_NuFit60={EXPECTED['sin2_theta12_NuFit60']},"
            f"sin2_theta13_NuFit60={EXPECTED['sin2_theta13_NuFit60']};"
            f"A_imports={n_imports_ok}/4;B_provenance+cite={int(B_pass)};"
            f"C_allowlist-annotation+tokens-retained={int(C_pass)};"
            f"D_source-script-SHA-unchanged={int(D_pass)};"
            f"mbb_shift_PDG->NuFit60={MBB_SHIFT_PDG_TO_NUFIT60_PCT}pct(decision-irrelevant);"
            f"sin2_23_pdg=OUT-OF-SCOPE-untouched"
        ),
        "A_pass": A_pass, "B_pass": B_pass, "C_pass": C_pass, "D_pass": D_pass,
        "overall": overall,
        "import_results": import_results,
        "prov_results": prov_results,
        "consumption_cite_present": consumption_cite_present,
        "annotation_present": annotation_present,
        "annotation_corner_names": annotation_corner_names,
        "annotation_token_disposition": annotation_token_disposition,
        "tok12_retained": tok12_retained,
        "tok13_retained": tok13_retained,
        "tok23_untouched": tok23_untouched,
        "source_sha": source_sha,
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str, value, audit_sha: str, content_sha: str,
    extra_rows: list[str] | None = None,
) -> dict:
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


def evaluate_gate(result: dict) -> str:
    # Conjunction: all four conjuncts must hold. Any miss = FAIL. No INFO band
    # (the gate is an artifact-existence/hygiene conjunction).
    return "PASS" if result["overall"] else "FAIL"


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    result = compute()
    verdict = evaluate_gate(result)

    # Console report (NUMBERS first)
    print("=== conjunct A: four imports exact (rel_tol>=1e-3 Class 8.3) ===")
    for name, r in result["import_results"].items():
        print(f"  {name:24s} expected={r['expected']!r:8} got={r['got']!r:8} "
              f"exact={r['exact']} within_tol={r['within_tol']} -> {r['ok']}")
    print(f"  A_pass = {result['A_pass']}")
    print("=== conjunct B: four PROVENANCE entries + W5-2 consumption citation ===")
    for name, r in result["prov_results"].items():
        print(f"  {name:24s} assign={r['assign_present']} "
              f"prov_row={r['prov_row_present']} -> {r['ok']}")
    print(f"  consumption_cite (audit a2d29b97...) present = "
          f"{result['consumption_cite_present']}")
    print(f"  B_pass = {result['B_pass']}")
    print("=== conjunct C: allowlist SUPERSEDED-BY-CANONICAL annotation + tokens ===")
    print(f"  annotation_present          = {result['annotation_present']}")
    print(f"  annotation_corner_names     = {result['annotation_corner_names']}")
    print(f"  annotation_token_disposition= {result['annotation_token_disposition']}")
    print(f"  sin2_12_pdg RETAINED        = {result['tok12_retained']}")
    print(f"  sin2_13_pdg RETAINED        = {result['tok13_retained']}")
    print(f"  sin2_23_pdg untouched (OOS) = {result['tok23_untouched']}")
    print(f"  C_pass = {result['C_pass']}")
    print("=== conjunct D: source script s100a_d5_0nubb_majorana.py UNCHANGED ===")
    print(f"  source_sha = {result['source_sha']}")
    print(f"  expected   = {SOURCE_SCRIPT_SHA_EXPECTED}")
    print(f"  D_pass = {result['D_pass']}")
    print(f"\n=== OVERALL conjunction = {result['overall']} ===")

    # Persist the promotion-record npz
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        names=np.array(list(EXPECTED.keys())),
        expected_values=np.array([EXPECTED[k] for k in EXPECTED]),
        imported_values=np.array([float(IMPORTED[k]) for k in EXPECTED]),
        A_pass=result["A_pass"], B_pass=result["B_pass"],
        C_pass=result["C_pass"], D_pass=result["D_pass"],
        overall=result["overall"],
        consumption_cite_present=result["consumption_cite_present"],
        annotation_present=result["annotation_present"],
        tok12_retained=result["tok12_retained"],
        tok13_retained=result["tok13_retained"],
        tok23_untouched=result["tok23_untouched"],
        source_sha=result["source_sha"],
        source_sha_expected=SOURCE_SCRIPT_SHA_EXPECTED,
        w52_consumption_audit=W52_CONSUMPTION_AUDIT,
        mbb_shift_PDG_to_NuFit60_pct=MBB_SHIFT_PDG_TO_NUFIT60_PCT,
        audit_sha256=audit_sha, content_sha256=content_sha,
        value=result["value"],
    )
    print(f"  wrote {OUT_NPZ.name}")

    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        ("# pmns_pin_promotion: PAIR-OF-PAIRS sin2_theta12_PDG=0.307 "
         "sin2_theta13_PDG=0.0220 sin2_theta12_NuFit60=0.303 "
         "sin2_theta13_NuFit60=0.02225 | allowlist sin2_12_pdg+sin2_13_pdg "
         "RETAINED+annotated, sin2_23_pdg OUT-OF-SCOPE | source-script "
         "s100a_d5_0nubb_majorana.py SHA 9ddd1ba5...966945 unchanged | "
         "S101-HK-PMNS-PIN-PROMOTION 3-tuple companion (schema-v2)"),
    ]  # (local)
    print_verdict_payload(verdict, result["value"], audit_sha, content_sha,
                          extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
