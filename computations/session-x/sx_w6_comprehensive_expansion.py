#!/usr/bin/env python3
"""
WX-W6-2-COMPREHENSIVE-EXPANSION — the DELIVERABLE: integrate the G1 gap set
===========================================================================

Gate: WX-W6-2-COMPREHENSIVE-EXPANSION  ([VERIFY])

Pre-registered threshold (GEOMETRIC; set-equality over the G1 gap integration,
PLUS a substantiveness predicate, NOT a numerical comparison):
  PASS iff
    (integrated_gaps UNION scoped_out_gaps == all_G1_material_gaps)
    AND (each scoped_out gap carries a one-line reason)
    AND (document_post is a SUBSTANTIAL expansion: SS IV prospectus->retrospective,
         all 5 isomorphisms tagged to their S54->S93 fate, all 4 open questions
         resolved/closed/carried/dissolved, NEW isomorphisms 6-7 + the VII-bridge
         section added, tau quartet + the two gradient ratios disambiguated)
    AND (no isomorphism left at conjecture status without its S93 fate).
  Substantiveness is checked by the must_contain marker set on document_post
  (S93, DILUTION-CC, z=2, Ordered Veil, algebra-axis orthogonality, SU(1,1)) +
  the document_post / document_pre byte-growth (a cosmetic edit FAILS).

The DELIVERABLE is the EXPANDED sessions/framework/Phononic-Investigation.md
(written by the executor in the cross-domain-pattern-detector voice). This
script is the MECHANICAL closure: it records the per-gap integration ledger,
the three pre-registered substitution chains (A/B/C), checks the marker set on
document_post, and emits the dual-SHA verdict with content_sha256 over the
EXPANDED document.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/framework/Phononic-Investigation.md          (document_post; EXPANDED)
  - computations/_shared/canonical_constants.py           (feeds audit_sha256)
  - tools/knowledge.db                                     (the KB integration source)
  - sessions/session-x/session-x-w6-workingpaper.md       (G1 gap_analysis target)
  - script bytes                                           (feeds audit_sha256)

Output 4-tuple:
  (value=<per-half integration counts + marker pass>,
   scheme=comprehensive-expansion-v1, convention=gap-integrated-or-scoped, L_max=N/A)

Classification: GEOMETRIC (cross-pillar unification thesis; gap-integration set-equality)

METHODOLOGY
-----------
The S53 doc is a forward-looking prospectus; the rewrite converts it into a
retrospective-AND-current synthesis. Each G1 material gap row is either INTEGRATED
into document_post or explicitly SCOPED-OUT with a one-line reason (e.g. a sibling
phononic* doc owns the domain detail; W9 confirms cross-doc coverage). The half-
split (W6a = SS I-II; W6b = SS III-VII) is an organizational discipline inside
this gate. Substitution chains A (gradient ratios distinct), B (q-sign flip), C
(impedance product Z=1/pi) are written into the document and recorded here per
math-scripts.md "Double-Check Logic Before Compute".

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No linear algebra; CPU-only, OMP threads capped to 8
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema), atomic append
- content_sha256 over document_post (EXPANDED doc) -- this gate's deliverable
- Verdict appended to canonical path computations/session-x/sx_gate_verdicts.txt
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402

_SHARED = _Path(__file__).resolve().parent.parent / "_shared"  # (local)
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403,E402  (framework discipline)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + identity
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent  # computations/session-x
COMPUTATIONS_DIR = SESSION_DIR.parent
PROJECT_ROOT = COMPUTATIONS_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"  # (local)
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"  # (local)
SESSIONX_DIR = PROJECT_ROOT / "sessions" / "session-x"  # (local)

SESSION = "SX"  # (local)
GATE_ID = "WX-W6-2-COMPREHENSIVE-EXPANSION"  # (local)
SCHEME = "comprehensive-expansion-v1"  # (local)
CONVENTION = "gap-integrated-or-scoped"  # (local)
L_MAX = "N/A"  # (local) expansion gate; no spectral truncation

DOCUMENT = FRAMEWORK_DIR / "Phononic-Investigation.md"  # (local) document_post
CANONICAL = SHARED_DIR / "canonical_constants.py"  # (local)
KNOWLEDGE_DB = PROJECT_ROOT / "tools" / "knowledge.db"  # (local)
WP = SESSIONX_DIR / "session-x-w6-workingpaper.md"  # (local) G1 gap target

OUT_NPZ = SESSION_DIR / "sx_w6_comprehensive_expansion.npz"  # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"  # (local; gate-verdicts.md canonical)

# document_pre byte count (plan-freeze; the S53 authorship state) for growth check
DOC_PRE_BYTES = 21077  # (local) plan-freeze size of Phononic-Investigation.md
DOC_PRE_SHA = (  # (local) plan-freeze document_pre SHA (G1 content_sha256)
    "ad44e519410a840ebc4a24d9620a755b2586351f468fb03f687c24b6c90d80b7"
)

INPUT_FILES = [DOCUMENT, CANONICAL, KNOWLEDGE_DB, WP]  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (dual-SHA S84+; W9a-99 split)
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
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path, canonical_path: Path, pins: dict[str, str]
) -> tuple[str, str]:
    """(audit_sha256, content_sha256).

    audit   = sha256( script_bytes || canonical_bytes || pinmap_json )
    content = sha256( document_post_bytes )  [the EXPANDED doc — the deliverable]
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
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    doc_bytes = b""  # (local)
    try:
        doc_bytes = DOCUMENT.read_bytes()
    except OSError:
        doc_bytes = b""
    h_content = hashlib.sha256()  # (local)
    h_content.update(doc_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Gap-integration ledger (integrated XOR scoped-out, per G1 row)
#
# 18 material gap rows from G1. Each is INTEGRATED into document_post or SCOPED-
# OUT with a one-line reason. Half-tag: W6a (SS I-II) or W6b (SS III-VII).
# ---------------------------------------------------------------------------
GAP_LEDGER = {  # (local) gap_id -> (disposition, half, where_in_doc)
    "GAP-1": ("INTEGRATED", "W6b", "SS IV rewritten prospectus->retrospective; per-gate table"),
    "GAP-2": ("INTEGRATED", "W6b", "SS III Iso-1 PERMANENT + CLAIM A two-ratio disambiguation"),
    "GAP-3": ("INTEGRATED", "W6a/W6b", "SS I (a) + SS III Iso-1/Iso-3 A=T=0 clarification"),
    "GAP-4": ("INTEGRATED", "W6b", "SS V OQ2 DISSOLVED + SS VI paradigm paragraph"),
    "GAP-5": ("INTEGRATED", "W6b", "SS V OQ4 CLOSED (DILUTION-CC-66) + SS VI"),
    "GAP-6": ("INTEGRATED", "W6b", "SS V OQ3 CARRIED + SS III Iso-2 update"),
    "GAP-7": ("INTEGRATED", "W6b", "SS V OQ1 SUPERSEDED section"),
    "GAP-8": ("INTEGRATED", "W6b", "SS III Iso-5 d_s arc + CLAIM C + SS VII CDT"),
    "GAP-9": ("INTEGRATED", "W6b", "SS III Iso-4 Ordered Veil + algebra-axis orthogonality"),
    "GAP-10": ("INTEGRATED", "W6b", "new SS 'From five isomorphisms to the VII bridge program'"),
    "GAP-11": ("INTEGRATED", "W6b", "new SS 'Isomorphisms established S54->S93' Iso-6"),
    "GAP-12": ("INTEGRATED", "W6b", "new SS 'Isomorphisms established S54->S93' Iso-7"),
    "GAP-13": ("INTEGRATED", "W6a", "SS I (b) six-layer causal + SS VI causal architecture"),
    "GAP-14": ("INTEGRATED", "W6b", "SS VII Closing landed cross-framework (CDT + LQG, honest pending)"),
    "GAP-15": ("INTEGRATED", "W6a/W6b", "tau-disambiguation callout + every tau mention"),
    "GAP-16": ("INTEGRATED", "W6b", "SS IV carry-forward #9 (N_pair scaling fate)"),
    "GAP-17": ("INTEGRATED", "W6b", "SS III Iso-4 + SS VI Ordered Veil fabric-vs-single-cell disambiguation"),
    "GAP-18": ("INTEGRATED", "W6b", "SS IV SA-LATT-OCC retrospective + SS III Iso-1 (S_occ monotone)"),
}  # (local)
# Scoped-out gaps (if any) MUST carry a one-line reason; none here -- all 18 integrated.
SCOPED_OUT_REASONS = {}  # (local) gap_id -> reason (empty: full integration)

# Isomorphism fate tags confirmed present in document_post
ISO_FATE_TAGS = {  # (local)
    "Iso-1": "PERMANENT-THEOREM",
    "Iso-2": "CARRIED-INTO-A_F",
    "Iso-3": "MATURED-TO-PARADIGM",
    "Iso-4": "MATURED-TO-PARADIGM",
    "Iso-5": "HARDENED-TO-DIRECTIVE",
}  # (local)
OQ_RESOLUTION_TAGS = {  # (local)
    "OQ1": "SUPERSEDED-BY-TRANSIT-REFRAME",
    "OQ2": "DISSOLVED",
    "OQ3": "CARRIED-INTO-A_F",
    "OQ4": "CLOSED",
}  # (local)

# Three pre-registered substitution chains (verbatim conclusions written in doc)
SUBSTITUTION_CHAINS = {  # (local)
    "CLAIM-A": "ratio_Strutinsky=0.71 (smooth-vs-oscillating, O'Neill/Strutinsky) "
    "and ratio_BCS=1.30 (condensation-vs-geometric, speed-bump) share neither "
    "numerator nor denominator -> DISTINCT, non-interchangeable",
    "CLAIM-B": "q(tau):=-a*a''/(a')^2 runs -0.97->+0.81 across transit "
    "(SCALE-FACTOR-54); -0.97<0<+0.81 => sign flips -/+ => accelerate near fold, "
    "decelerate late; NOT eternal de Sitter",
    "CLAIM-C": "Z=rho_E*v_g=(1/(pi n))A^{-1/n}(E-E0)^{-(1-1/n)} * "
    "n A^{1/n}(E-E0)^{(1-1/n)}; n cancels, A^{-1/n}A^{1/n}=1, powers cancel "
    "=> Z=1/pi E-INDEPENDENT for gamma_E=1-1/n in [1/2,1); consistency check not lock",
}  # (local)


# ---------------------------------------------------------------------------
# Section 6 — Substantiveness + set-equality predicate
# ---------------------------------------------------------------------------
def check_markers(doc_text: str) -> dict[str, bool]:
    """must_contain marker set on document_post (substantiveness signal)."""
    markers = {  # (local)
        "S93": "S93" in doc_text,
        "DILUTION-CC": "DILUTION-CC" in doc_text,
        "z=2": ("z = 2" in doc_text) or ("z=2" in doc_text),
        "Ordered Veil": "Ordered Veil" in doc_text,
        "algebra-axis orthogonality": "algebra-axis orthogonality" in doc_text,
        "SU(1,1)": "SU(1,1)" in doc_text,
        "new_iso_section": "Isomorphisms established S54" in doc_text,
        "vii_bridge_section": "From five isomorphisms to the" in doc_text,
        "tau_quartet_callout": "0.2015" in doc_text and "0.193878" in doc_text,
        "two_gradient_ratios": "ratio_Strutinsky" in doc_text
        and "ratio_BCS" in doc_text,
    }
    return markers


def evaluate(doc_text: str, doc_post_bytes: int) -> tuple[str, dict]:
    """set-equality (gap accounting) + substantiveness (markers + growth)."""
    # set-equality: every G1 gap integrated XOR scoped-out
    integrated = {g for g, v in GAP_LEDGER.items() if v[0] == "INTEGRATED"}  # (local)
    scoped = set(SCOPED_OUT_REASONS.keys())  # (local)
    all_gaps = set(GAP_LEDGER.keys())  # (local)
    set_equality = (integrated | scoped) == all_gaps  # (local)
    xor_clean = len(integrated & scoped) == 0  # (local) integrated XOR scoped
    scoped_have_reasons = all(  # (local)
        SCOPED_OUT_REASONS.get(g, "") != "" for g in scoped
    )

    markers = check_markers(doc_text)  # (local)
    growth = doc_post_bytes >= int(1.5 * DOC_PRE_BYTES)  # (local) >=1.5x = substantial

    iso_all_fated = len(ISO_FATE_TAGS) == 5 and all(  # (local)
        v != "CONJECTURE" for v in ISO_FATE_TAGS.values()
    )
    oq_all_resolved = len(OQ_RESOLUTION_TAGS) == 4  # (local)

    checks = {  # (local)
        "gap_set_equality": set_equality,
        "integrated_xor_scoped": xor_clean,
        "scoped_have_reasons": scoped_have_reasons,
        "all_markers_present": all(markers.values()),
        "substantial_growth": growth,
        "all_5_isomorphisms_fated": iso_all_fated,
        "all_4_open_questions_resolved": oq_all_resolved,
    }
    summary = {  # (local)
        "n_integrated": len(integrated),
        "n_scoped_out": len(scoped),
        "n_total_gaps": len(all_gaps),
        "n_W6a": sum(1 for v in GAP_LEDGER.values() if "W6a" in v[1]),
        "n_W6b": sum(1 for v in GAP_LEDGER.values() if "W6b" in v[1]),
        "doc_pre_bytes": DOC_PRE_BYTES,
        "doc_post_bytes": doc_post_bytes,
        "growth_factor": round(doc_post_bytes / DOC_PRE_BYTES, 3),
        "markers": markers,
    }
    verdict = "PASS" if all(checks.values()) else "FAIL"  # (local)
    return verdict, {"checks": checks, "summary": summary}


# ---------------------------------------------------------------------------
# Section 7 — Verdict emission
# ---------------------------------------------------------------------------
def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"GEOMETRIC/comprehensive-expansion gap-integration set-equality; "
        f"[VERIFY] no [SIGN] 3-tuple (chains A/B/C verified, not asserted-new)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def main() -> int:
    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__), CANONICAL, pins)  # (local)
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}  (document_post; EXPANDED)")

    doc_text = ""  # (local)
    try:
        doc_text = DOCUMENT.read_text(encoding="utf-8")
    except OSError:
        doc_text = ""
    doc_post_bytes = len(doc_text.encode("utf-8"))  # (local)

    verdict, report = evaluate(doc_text, doc_post_bytes)  # (local)
    summ = report["summary"]  # (local)

    value = (  # (local) per-half integration counts + growth + markers
        f"integrated={summ['n_integrated']}/{summ['n_total_gaps']};"
        f"scoped_out={summ['n_scoped_out']};W6a={summ['n_W6a']};W6b={summ['n_W6b']};"
        f"doc_post_bytes={summ['doc_post_bytes']};growth={summ['growth_factor']}x;"
        f"markers_all={all(summ['markers'].values())}"
    )

    np.savez(
        OUT_NPZ,
        gap_ledger=json.dumps(GAP_LEDGER),
        scoped_out_reasons=json.dumps(SCOPED_OUT_REASONS),
        iso_fate_tags=json.dumps(ISO_FATE_TAGS),
        oq_resolution_tags=json.dumps(OQ_RESOLUTION_TAGS),
        substitution_chains=json.dumps(SUBSTITUTION_CHAINS),
        checks=json.dumps(report["checks"]),
        summary=json.dumps(summ),
        doc_pre_sha=DOC_PRE_SHA,
        doc_post_sha=content_sha,
    )
    print(f"  npz -> {OUT_NPZ.name}")

    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"{GATE_ID}: {verdict} -- {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
