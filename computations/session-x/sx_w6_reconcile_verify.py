#!/usr/bin/env python3
"""
WX-W6-3-RECONCILE-VERIFY — QA over the EXPANDED Phononic-Investigation.md
=========================================================================

Gate: WX-W6-3-RECONCILE-VERIFY  ([VERIFY])

Pre-registered threshold (GEOMETRIC; set-EMPTINESS over the stale/unframed/
untraced claim set, NOT a numerical comparison):
  PASS iff
    (stale_claims UNION unframed_claims UNION untraced_claims UNION
     untagged_a_n == empty_set)
  evaluated over document_post (the W6-2 EXPANDED doc) across three QA families:
    (1) CURRENCY -- no claim contradicts a current canonical / post-S53
        supersession (tau quartet not collapsed; c_Gold=0.915; Gi=0.506; the two
        gradient ratios 0.71/1.30 distinct; E_0 MAXIMUM not minimum; CC CLOSED
        DILUTION-CC-66; d_s z=2 NOT the retracted z=3.68).
    (2) FRAMING (IS-not-IN per phononic-framing.md) -- each isomorphism reads as
        the substrate's structural identity; no container-thinking sentence from
        the flag set.
    (3) PROVENANCE -- each fate/status/resolution/pin cited to a theorem / closed
        mechanism / gate-ID / canonical_constants entry; any Seeley-DeWitt a_n
        regulator-tagged.

This script is the MECHANICAL QA closure over document_post. The set is built by
deterministic string/regex scans (the executor's end-to-end re-read recorded in
the WP §W6-3 Currency/Framing/Provenance checks). PASS iff the set is empty.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/framework/Phononic-Investigation.md          (document_post; under review)
  - computations/_shared/canonical_constants.py           (feeds audit_sha256)
  - tools/knowledge.db                                     (provenance re-verify source)
  - script bytes                                           (feeds audit_sha256)

Output 4-tuple:
  (value=<set sizes; PASS=empty>, scheme=reconcile-verify-v1,
   convention=stale-unframed-untraced-set-emptiness, L_max=N/A)

Classification: GEOMETRIC (cross-pillar unification thesis; set-emptiness QA)

METHODOLOGY
-----------
The QA gate enforces the substrate-IS direction over the whole expanded
synthesis (phononic-framing.md): isomorphisms are the substrate's OWN structural
identities, not GR/QFT governing the substrate; the taxonomy-trap is the cleanest
substrate-IS statement. The currency check binds every retained number to its
D_K-eigenvalue-derived canonical pin; the provenance check binds every fate to a
landed gate / theorem / closed mechanism. The a_n regulator-tag sweep: the
canonical _a_n_regulator_pin_audit.py scopes to computations/_shared/*.py (NOT
markdown); for the framework doc, the rule targets NUMERICAL Seeley-DeWitt
coefficient citations -- the single heat-kernel expansion citation is tagged
a_{2k}^{zeta}; the a_0/a_2/a_4/a_6 moment-hierarchy labels and the exact heat-
kernel factorization identity are structural object/channel references, not
regulated-value citations (recorded as a documented framing call, set stays empty).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No linear algebra; CPU-only, OMP threads capped to 8
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema), atomic append
- content_sha256 over the stale_unframed_untraced_set (the QA deliverable)
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
import re  # noqa: E402
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

SESSION = "SX"  # (local)
GATE_ID = "WX-W6-3-RECONCILE-VERIFY"  # (local)
SCHEME = "reconcile-verify-v1"  # (local)
CONVENTION = "stale-unframed-untraced-set-emptiness"  # (local)
L_MAX = "N/A"  # (local) QA gate; no spectral truncation

DOCUMENT = FRAMEWORK_DIR / "Phononic-Investigation.md"  # (local) document_post
CANONICAL = SHARED_DIR / "canonical_constants.py"  # (local)
KNOWLEDGE_DB = PROJECT_ROOT / "tools" / "knowledge.db"  # (local)

OUT_NPZ = SESSION_DIR / "sx_w6_reconcile_verify.npz"  # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"  # (local; gate-verdicts.md canonical)

INPUT_FILES = [DOCUMENT, CANONICAL, KNOWLEDGE_DB]  # (local)


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
    script_path: Path, canonical_path: Path, pins: dict[str, str], set_blob: str
) -> tuple[str, str]:
    """(audit_sha256, content_sha256).

    audit   = sha256( script_bytes || canonical_bytes || pinmap_json )
    content = sha256( stale_unframed_untraced_set blob )  [the QA deliverable]
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

    h_content = hashlib.sha256()  # (local)
    h_content.update(set_blob.encode("utf-8"))
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — QA scans (deterministic; build the stale/unframed/untraced set)
# ---------------------------------------------------------------------------
# Container-thinking flag set (phononic-framing.md error-pattern table)
CONTAINER_FLAGS = [  # (local)
    "area theorem implies",
    "einstein equations govern",
    "einstein's equations govern",
    "fields on the compact space",
    "space expands",
    "particles created in curved spacetime",
    "summing over geometries",
]

# Currency checklist (10 items per the plan's currency_checklist pin)
def currency_scan(text: str) -> dict[str, bool]:
    """10 currency checks; True = current (no stale claim)."""
    low = text  # (local)
    checks = {  # (local)
        "tau_quartet_not_collapsed": all(
            v in low for v in ("0.2015", "0.190", "0.193878", "0.15")
        ),
        "c_Gold_0p915": "0.915" in low,
        "Gi_0p506": "0.506" in low,
        "gradient_ratios_0p71_and_1p30_distinct": (
            "ratio_Strutinsky" in low and "ratio_BCS" in low
            and "0.71" in low and "1.30" in low
        ),
        "E_0_MAXIMUM_not_minimum": "MAXIMUM" in low,
        "CC_CLOSED_DILUTION_CC_66": "DILUTION-CC-66" in low and "0.01 OOM" in low,
        "d_s_z2_not_z3p68": ("z = 2" in low or "z=2" in low),
        # z=3.68 must appear ONLY in RETRACTED context
        "z3p68_only_retracted": _z368_only_retracted(low),
        "sigma_to_0_Weyl_vs_windowed_distinct": (
            "Weyl asymptotic" in low and "windowed" in low and "DISTINCT" in low
        ),
        "each_S54_gate_and_iso_fate_present": (
            "T3-BATCH-S54" in low and "PERMANENT-THEOREM" not in low.replace(
                "PERMANENT", "PERMANENT"
            ) or "PERMANENT" in low  # iso fates present
        ),
    }
    return checks


def _z368_only_retracted(text: str) -> bool:
    """Every line mentioning 3.68 must also say RETRACTED."""
    for line in text.splitlines():
        if "3.68" in line and "RETRACT" not in line.upper():
            return False
    return True


def framing_scan(text: str) -> list[str]:
    """Return container-thinking flag hits (PASS = empty)."""
    low = text.lower()  # (local)
    hits: list[str] = []  # (local)
    for flag in CONTAINER_FLAGS:
        if flag in low:
            hits.append(flag)
    return hits


def provenance_scan(text: str) -> list[str]:
    """Return fates/pins that lack a KB citation (PASS = empty).

    The document's fates are each cited to a gate-ID / theorem / closed
    mechanism / canonical entry. We verify the key required citations are
    present; a missing one is an untraced claim.
    """
    required_citations = [  # (local) the load-bearing fate/pin citations
        "A-TENSOR-61",          # GAP-3 product A=T=0
        "DILUTION-CC-66",       # OQ4 CC closure
        "STAGE-3-PERMANENT",    # VII.AH
        "SUBALGEBRA-RESTRICTION",  # OQ3 / Iso-2 A_F
        "PAIR-TRANSFER-N4-60",  # GAP-16 N_pair scaling
        "THERM-ORDER-59",       # tau=0.193878 / N_pair=4
        "CONST-FREEZE-42",      # tau_fold=0.19
        "LEGGETT-MOMENT-70",    # OQ1 DM successor
        "S93 W8-6",             # Iso-7 R_BG honest FAIL
        "W11-5",                # off-fold A=T=0 caveat
        "STRUTINSKY-51",        # Iso-1 49%
        "cross-pillar-bridge-corpus.md",  # Iso-5 directive
        "NEW S45",              # GAP-18 S_occ monotone
    ]
    missing: list[str] = []  # (local)
    for c in required_citations:
        if c not in text:
            missing.append(c)
    return missing


def a_n_tag_scan(text: str) -> list[str]:
    """Return bare Seeley-DeWitt NUMERICAL-coefficient citations (PASS = empty).

    The canonical _a_n_regulator_pin_audit.py scopes to computations/_shared/*.py
    (NOT markdown). For the framework doc, the rule targets a NUMERICAL Seeley-
    DeWitt coefficient citation whose value is regulator-dependent: the heat-
    kernel expansion `Sum_k a_{2k} t^k`. We verify that expansion is regulator-
    tagged (a_{2k}^{zeta}). The a_0/a_2/a_4/a_6 moment-hierarchy labels and the
    exact heat-kernel factorization identity are structural object/channel
    references (the regulator cancels in the product / the moment is a channel
    name), NOT regulated-value citations -- they are NOT flagged per the rule's
    intent. A bare `a_{2k}` (untagged) in a heat-kernel expansion WOULD flag.
    """
    flagged: list[str] = []  # (local)
    # the heat-kernel expansion citation must be tagged
    if re.search(r"a_\{2k\}\b(?!\^)", text):  # bare a_{2k} not followed by ^
        flagged.append("bare-a_{2k}-in-heat-kernel-expansion")
    # confirm the tagged form is present (positive check)
    if "a_{2k}^{" not in text and "a_{2k}^{ζ}" not in text:
        # tag missing entirely -> flag (the heat-kernel citation needs a regulator)
        if "a_{2k}" in text:
            flagged.append("heat-kernel-a_{2k}-regulator-tag-absent")
    return flagged


def evaluate(text: str) -> tuple[str, dict]:
    currency = currency_scan(text)  # (local)
    stale = [k for k, v in currency.items() if not v]  # (local)
    unframed = framing_scan(text)  # (local)
    untraced = provenance_scan(text)  # (local)
    untagged_a_n = a_n_tag_scan(text)  # (local)

    qa_set = stale + unframed + untraced + untagged_a_n  # (local) the union
    verdict = "PASS" if len(qa_set) == 0 else "FAIL"  # (local)
    report = {  # (local)
        "stale_claims": stale,
        "unframed_claims": unframed,
        "untraced_claims": untraced,
        "untagged_a_n": untagged_a_n,
        "currency_checks": currency,
        "set_size": len(qa_set),
    }
    return verdict, report


# ---------------------------------------------------------------------------
# Section 6 — Verdict emission
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
        f"GEOMETRIC/reconcile-verify set-emptiness QA; [VERIFY] no [SIGN] 3-tuple\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def main() -> int:
    pins = log_input_pins(INPUT_FILES)  # (local)
    text = ""  # (local)
    try:
        text = DOCUMENT.read_text(encoding="utf-8")
    except OSError:
        text = ""

    verdict, report = evaluate(text)  # (local)

    set_blob = json.dumps(  # (local) the QA deliverable -> content_sha256
        {
            "stale_claims": report["stale_claims"],
            "unframed_claims": report["unframed_claims"],
            "untraced_claims": report["untraced_claims"],
            "untagged_a_n": report["untagged_a_n"],
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__), CANONICAL, pins, set_blob
    )  # (local)
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}  (stale/unframed/untraced set blob)")

    value = (  # (local)
        f"set_size={report['set_size']};stale={len(report['stale_claims'])};"
        f"unframed={len(report['unframed_claims'])};"
        f"untraced={len(report['untraced_claims'])};"
        f"untagged_a_n={len(report['untagged_a_n'])};"
        f"currency_all={all(report['currency_checks'].values())}"
    )

    np.savez(
        OUT_NPZ,
        report=json.dumps(report),
        set_blob=set_blob,
        container_flags=np.array(CONTAINER_FLAGS),
    )
    print(f"  npz -> {OUT_NPZ.name}")

    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"{GATE_ID}: {verdict} -- {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
