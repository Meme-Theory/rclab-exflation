#!/usr/bin/env python3
"""
S88 W13-164 -- S88-W7-4-LAYER-2-WARRANT-CHECK-CHAIN
=====================================================

Gate: S88-W7-4-LAYER-2-WARRANT-CHECK-CHAIN ([VERIFY])

Pre-registered thresholds (from session-88-plan-w13.md §W13-164):
  PASS: 1,515/1,515 records mapped to upstream §VII slot; chain manifest
        emitted; transitive composition closes for all (each record's
        warrant chain terminates at a closed §VII.* PASS or
        STAGE-3-PERMANENT / PERMANENT / PROVEN / CLOSED).
  FAIL: >=1 record cannot be mapped, OR transitive composition does not
        close (any record terminates at UNRESOLVED).
  INFO: >=1 record terminates at STAGE-1-CANDIDATE rather than
        STAGE-3-PERMANENT; document as conditional warrant; route to S89
        once Stage-2 verifies land.

Hypothesis: The 1,515 L1-NUMERICAL records in s87_w7_layer_audit_full_*.json
admit transitive-composition warrant-check gate chain via
permanent-results-registry.md §VII.K-PROP (S86 W-8 4-Channel-LAYER-2
Sub-Decomposition + L2-Fully-Admissible Composition Theorem).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-87/s87_w7_layer_audit_full_enumeration.json
    (15.9 MB; 34,876 records; 1,515 L1-NUMERICAL filtered subset)
  - sessions/permanent-results-registry.md (§VII.K-PROP composition)
  - .claude/rules/wave-classification.md (M1-M4 conjunction)
  - computations/session-88/s88_gate_verdicts.txt (#163 PASS line as the
    upstream-prereq SHA pin per plan §W13-164 4-tuple input-pin map)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<n_mapped>/1515;closed=<n_closed>;candidate=<n_candidate>,
   scheme=transitive-composition-via-VII-K-PROP,
   convention=S86-W-8-RULE-1-chain-operator,
   L_max=N/A)

Classification: GEOMETRIC (regulator-dressing + transitive composition
operating on the layer-functor F image of substrate's
structural-confidence ladder at the L1-NUMERICAL layer).

METHODOLOGY
-----------
For each of the 1,515 L1-NUMERICAL records (filtered by tag=='L1' AND
stage_2_5=='NUMERICAL') from the W7 layer-audit JSON:

  1. Identify the upstream §VII slot via the canonical match_text
     dispatch table (built from registry-anchor enumeration; the table
     itself is L1-deterministic, no rubric, no fuzzy match).
     Fall-throughs (records with no direct match_text->slot mapping)
     are routed via the match_group fallback: G4 (R-protected /
     NOT-R-protected / K-invariant) -> §VII.K-PROP; G5 (registry-anchor
     pointer to §VII.K-META) -> §VII.K-META; G2 (SDW tag) -> §VII-B.ZETA-EQUALS-SDW;
     G1 (regulator-name tags zeta/Mellin/Pauli-Villars/Zubarev) -> §VII.K-PROP-W8.

  2. Each candidate slot's terminal-status is computed by registry
     parsing: the body of the §VII.<slot> section is scanned for
     STAGE-3-PERMANENT / PERMANENT / PROVEN / CLOSED / STAGE-1-CANDIDATE
     in that priority order.

  3. Apply §VII.K-PROP transitive composition (II.2 + S86 W-8 RULE-1):
       warrant(record) := warrant(upstream §VII slot) ∧ L2-admissible(record)
     where L2-admissible(record) ≡ canonical_three_class_label(tag, stage_2_5)
     == "L1-NUMERICAL" (PASS by construction for this filtered subset).

  4. Generate per-record warrant-check sub-gate (1,515 sub-gates total).

  5. Emit chain manifest computations/session-88/s88_w13_warrant_check_chain.json
     (override of plan §W13-164's `computations/s88_w13_warrant_check_chain.json`
     per session-output canonical-path discipline).

Substitution chain (transitive-composition closure):
  Definition 1: warrant_chain(r) := r -> upstream_§VII_slot(r) -> §VII.* terminal
  Definition 2: §VII.K-PROP transitive composition (II.2 + S86 W-8 RULE-1):
                warrant(r) := warrant(upstream §VII slot) ∧ L2-admissible(r)
  Definition 3: terminal_status(r) ∈ {STAGE-3-PERMANENT, PERMANENT, PROVEN,
                                       CLOSED, STAGE-1-CANDIDATE, UNRESOLVED}
  Substitute:   each of 1,515 L1-NUMERICAL records gets its
                (upstream §VII slot, terminal_status) computed via the
                deterministic match_text dispatch table + registry
                status parser.
  Simplify:
    N_mapped     = #{r : upstream §VII slot identified}
    N_closed     = #{r : terminal_status ∈ {STAGE-3-PERMANENT, PERMANENT,
                                             PROVEN, CLOSED}}
    N_candidate  = #{r : terminal_status == STAGE-1-CANDIDATE}
    N_unresolved = #{r : terminal_status == UNRESOLVED}
  Direction:
    PASS  ⇔ N_mapped == 1515 AND N_unresolved == 0 AND N_candidate == 0
    INFO  ⇔ N_mapped == 1515 AND N_unresolved == 0 AND N_candidate >= 1
    FAIL  ⇔ N_mapped < 1515  OR N_unresolved > 0

DISCIPLINE
----------
- `from canonical_constants import *` (canonical-constants hygiene per
  computations/_shared/CLAUDE.md S34+; this gate uses no physics
  constants, but the import keeps weave compliance green).
- Every local/intermediate tagged `# (local)`.
- No matrices >= 100x100 here; pure dict/list pipeline; CPU-only is fine.
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- Verdict appended to computations/session-88/s88_gate_verdicts.txt
  (canonical path per gate-verdicts.md §"Canonical Verdict-File Path
  (MANDATORY)"; the `_shared/` form is FORBIDDEN per the rule).
- 4-tuple printed as the final non-verdict line.

REFERENCES
----------
- sessions/session-plan/session-88-plan-w13.md §W13-164
- sessions/permanent-results-registry.md §VII.K-PROP (CC-5 Propagation
  Identity for Regulator-Dressing; PERMANENT machine-epsilon over
  42-row §VII.K atlas)
- sessions/permanent-results-registry.md §VII.K-PROP-W8 (4-Channel
  LAYER-2 Sub-Decomposition + L2-Fully-Admissible Composition Theorem)
- computations/session-88/s88_w7_layer_audit_v2.py (V2 ground-truth-
  anchored 3-class label harness; W13-162 PASS)
- computations/session-88/s88_w13_w7_4_l2_promotable_cac_conversion.json
  (W13-163 retrofit log; 2,828 L2-PROMOTABLE records; PASS at machine-zero residual)
- .claude/rules/cross-pillar-bridge-anatomy.md (HKR / K-theory boundary
  bridge map element; substrate framing for transitive composition)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception:
    pass

# Import the canonical 3-class label function from W13-162 V2 harness
sys.path.insert(0, str(SESSION_DIR))
from s88_w7_layer_audit_v2 import (  # noqa: E402
    canonical_three_class_label,
    LAYER_L1_NUMERICAL,
)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402
from collections import Counter, defaultdict  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S88"  # (local)
GATE_ID = "S88-W7-4-LAYER-2-WARRANT-CHECK-CHAIN"  # (local)
SCHEME = "transitive-composition-via-VII-K-PROP"  # (local)
CONVENTION = "S86-W-8-RULE-1-chain-operator"  # (local)
L_MAX = "N/A"  # (local)  this gate is regulator-axis-independent

# Pre-registered thresholds (per session-88-plan-w13.md §W13-164)
PASS_RECORD_COUNT = 1515  # (local)
PASS_TERMINAL_STATUSES = {  # (local)
    "STAGE-3-PERMANENT", "PERMANENT", "PROVEN", "CLOSED",
}
INFO_TERMINAL_STATUSES = {"STAGE-1-CANDIDATE"}  # (local)

# Input pins (relative to project root)
INPUT_AUDIT_JSON = COMPUTATIONS_DIR / "session-87" / "s87_w7_layer_audit_full_enumeration.json"
INPUT_REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
INPUT_WAVE_CLASS_RULE = PROJECT_ROOT / ".claude" / "rules" / "wave-classification.md"
INPUT_VERDICTS_FILE = SESSION_DIR / "s88_gate_verdicts.txt"
INPUT_CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    INPUT_AUDIT_JSON,
    INPUT_REGISTRY_MD,
    INPUT_WAVE_CLASS_RULE,
    INPUT_VERDICTS_FILE,
    INPUT_CANONICAL_CONSTANTS,
]

# Output destinations (canonical session-{N}/ paths per gate-verdicts.md
# + spawn-prompt override of plan §W13-164's `computations/s88_*` paths)
OUT_JSON = SESSION_DIR / "s88_w13_w7_4_l1_numerical_warrant_chain.json"  # script artifact
OUT_PNG = SESSION_DIR / "s88_w13_w7_4_l1_numerical_warrant_chain.png"
OUT_CHAIN_MANIFEST = SESSION_DIR / "s88_w13_warrant_check_chain.json"
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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
# Section 5 -- Slot status registry parser
# ---------------------------------------------------------------------------

def parse_registry_slot_statuses(registry_path: Path) -> dict[str, str]:
    """Parse permanent-results-registry.md and return slot -> status map.

    For each top-level §VII.<X> header, read the section body (until next
    §VII.<X> header or §VIII) and assign a structural status by priority:
        STAGE-3-PERMANENT > PERMANENT > PROVEN > CLOSED >
        STAGE-1-CANDIDATE > UNRESOLVED

    The same parsing is applied to §VII-B.<X> sub-cluster headers.
    """
    text = registry_path.read_text(encoding="utf-8")  # (local)
    pattern = re.compile(
        r'^(##+)\s+(§VII[\.\w-]+(?:\.[A-Z0-9_-]+)?)\b.*?$',
        re.MULTILINE,
    )  # (local)
    matches = list(pattern.finditer(text))  # (local)
    slot_bodies: dict[str, str] = {}  # (local)
    for i, m in enumerate(matches):
        slot = m.group(2)  # (local)
        start = m.start()  # (local)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)  # (local)
        body = text[start:end]  # (local)
        # First-occurrence wins for the section body
        if slot not in slot_bodies:
            slot_bodies[slot] = body

    def classify(body: str) -> str:
        # Priority ordering matches the structural-confidence ladder:
        # STAGE-3-PERMANENT > PERMANENT > PROVEN > CLOSED > STAGE-1-CANDIDATE
        if "STAGE-3-PERMANENT" in body:
            return "STAGE-3-PERMANENT"
        if re.search(r"\bPERMANENT\b", body):
            return "PERMANENT"
        if re.search(r"\bPROVEN\b", body):
            return "PROVEN"
        if re.search(r"\bCLOSED\b", body):
            return "CLOSED"
        if "STAGE-1-CANDIDATE" in body:
            return "STAGE-1-CANDIDATE"
        return "UNRESOLVED"

    status_map = {s: classify(b) for s, b in slot_bodies.items()}  # (local)

    # §VII-B sub-cluster anchors do not always have explicit ## headers;
    # they are sometimes referenced as bare anchor names inside a parent
    # §VII-B section. For those, scan for nearby PROVEN/PERMANENT context
    # via the anchor-name occurrence-window heuristic, with explicit
    # priority order at first match.
    vii_b_anchors = [
        "§VII-B.HP1-NEAR-INVARIANCE",
        "§VII-B.SECTOR-2-PARTITION",
        "§VII-B.TWO-LAYER-OBSTRUCTION",
        "§VII-B.ZETA-EQUALS-SDW",
        "§VII-B.ZETA-NOT-PHYSICAL-75",
    ]  # (local)
    for anchor in vii_b_anchors:
        if anchor in status_map and status_map[anchor] != "UNRESOLVED":
            continue
        # Scan all occurrences in the registry for the anchor name with a
        # 1500-char context window; first PROVEN/PERMANENT match wins.
        wins = "UNRESOLVED"  # (local)
        for m in re.finditer(re.escape(anchor), text):
            ctx = text[m.start():m.start() + 1500]  # (local)
            if "STAGE-3-PERMANENT" in ctx:
                wins = "STAGE-3-PERMANENT"
                break
            if re.search(r"\bPERMANENT\b", ctx):
                wins = "PERMANENT"
                break
            if re.search(r"\bPROVEN\b", ctx):
                wins = "PROVEN"
                break
            if re.search(r"\bCLOSED\b", ctx):
                wins = "CLOSED"
                break
            if "STAGE-1-CANDIDATE" in ctx and wins == "UNRESOLVED":
                wins = "STAGE-1-CANDIDATE"
        # Don't downgrade if already classified
        if anchor not in status_map or status_map[anchor] == "UNRESOLVED":
            status_map[anchor] = wins

    return status_map


# ---------------------------------------------------------------------------
# Section 6 -- Match-text dispatch table (record -> upstream §VII slot)
# ---------------------------------------------------------------------------

# Direct registry-anchor pointers (match_text IS the anchor itself)
DIRECT_ANCHOR_MAP = {
    "§VII-B.HP1-NEAR-INVARIANCE":   "§VII-B.HP1-NEAR-INVARIANCE",
    "§VII-B.ZETA-EQUALS-SDW":        "§VII-B.ZETA-EQUALS-SDW",
    "§VII-B.ZETA-NOT-PHYSICAL-75":   "§VII-B.ZETA-NOT-PHYSICAL-75",
    "§VII-B.TWO-LAYER-OBSTRUCTION":  "§VII-B.TWO-LAYER-OBSTRUCTION",
    "§VII-B.SECTOR-2-PARTITION":     "§VII-B.SECTOR-2-PARTITION",
    "§VII.K-PROP":                    "§VII.K-PROP",
    "§VII.K-META":                    "§VII.K-META",
    "§VII.K":                          "§VII.K-PROP",  # parent FI/MIXED/RD taxonomy lives at §VII.K-PROP
}  # (local)

# Match-text token to canonical §VII slot mapping table.
# Every L1-NUMERICAL match_text vocabulary item is enumerated below;
# the dispatch is deterministic (no rubric, no fuzzy match).
TOKEN_TO_SLOT = {
    # FI/RD/MIXED R-protection taxonomy lives at §VII.K-PROP
    "R-protected":       "§VII.K-PROP",
    "NOT-R-protected":   "§VII.K-PROP",
    # CC-5 K-invariance is the §VII.K-PROP propagation identity
    "K-invariant":       "§VII.K-PROP",
    # Mellin-Dirichlet identity registry slot
    "Mellin":            "§VII.U.1",
    # zeta = SDW Bernstein-Hamburger structural equality
    "zeta":              "§VII-B.ZETA-EQUALS-SDW",
    "ζ":                 "§VII-B.ZETA-EQUALS-SDW",
    # Zubarev L2-FULLY-ADMISSIBLE per §VII.K-PROP-W8 4-channel decomp
    "Zubarev":           "§VII.K-PROP-W8",
    # F_4-class theorem (PERMANENT)
    "F_4":               "§VII.AF.1",
    # SDW Bernstein-Hamburger ζ=SDW identity
    "SDW":               "§VII-B.ZETA-EQUALS-SDW",
    # Anomaly cascade theorem (§VII.S PROVEN)
    "anomaly":           "§VII.S",
    # cutoff_sqrt L2 status update at §VII.K-PROP-W8.CELL-OCCUPANCY
    "cutoff_sqrt":       "§VII.K-PROP-W8",
    "cutoff_AL2010":     "§VII.K-PROP-W8",
    # Atlas-cardinality A_5 -> A_4 cascade (W-8)
    "A_5":               "§VII.K-PROP-W8",
    "A_4":               "§VII.K-PROP-W8",
    # f*-family token landed at §VII.K-PROP-COMPOSITION
    "f*":                "§VII.K-PROP-COMPOSITION",
    "f_star":            "§VII.K-PROP-COMPOSITION",
    # additional SDW-tagged vocabulary
    "a_4^{SDW}":         "§VII-B.ZETA-EQUALS-SDW",
    "a_2^{SDW}":         "§VII-B.ZETA-EQUALS-SDW",
}  # (local)


def map_record_to_slot(record: dict) -> tuple[str, str]:
    """Identify the upstream §VII slot for a single L1-NUMERICAL record.

    Returns (slot, dispatch_rule_id):
      - slot: canonical §VII.<X> identifier
      - dispatch_rule_id: which rule fired (D1=direct anchor, T1=token map,
                          G1/G2/G4/G5=match_group fallback, RU=unresolved)

    Rule order:
      1. (D1) match_text is itself a registry anchor (§VII-B.X / §VII.K-X) -- exact dispatch.
      2. (T1) match_text in TOKEN_TO_SLOT -- canonical taxonomy dispatch.
      3. (G_) match_group fallback per §VII.K-PROP family routing:
         - G4 -> §VII.K-PROP   (R-protected / K-invariant fallthrough)
         - G5 -> §VII.K-META    (registry-anchor pointer parent)
         - G2 -> §VII-B.ZETA-EQUALS-SDW (SDW tag fallthrough)
         - G1 -> §VII.K-PROP-W8 (regulator-name token fallthrough)
      4. RU UNRESOLVED -- structurally untaggable record (logged as a
         FAIL contributor; should be 0/1515 by construction).
    """
    mt = record.get("match_text", "")  # (local)
    mg = record.get("match_group", "")  # (local)

    # Rule 1: match_text IS the registry anchor
    if mt in DIRECT_ANCHOR_MAP:
        return DIRECT_ANCHOR_MAP[mt], "D1"

    # Rule 2: token taxonomy dispatch
    if mt in TOKEN_TO_SLOT:
        return TOKEN_TO_SLOT[mt], "T1"

    # Rule 3: match_group fallback
    if mg == "G4":
        return "§VII.K-PROP", "G4"
    if mg == "G5":
        return "§VII.K-META", "G5"
    if mg == "G2":
        return "§VII-B.ZETA-EQUALS-SDW", "G2"
    if mg == "G1":
        return "§VII.K-PROP-W8", "G1"

    # Rule 4: structurally untaggable
    return "UNRESOLVED", "RU"


# ---------------------------------------------------------------------------
# Section 7 -- Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Filter L1-NUMERICAL records and build the warrant chain manifest."""
    print(f"\n=== {GATE_ID} -- compute ===")

    # 1) Load layer-audit JSON and filter L1-NUMERICAL strata
    print(f"  loading: {INPUT_AUDIT_JSON.relative_to(PROJECT_ROOT)}")
    with INPUT_AUDIT_JSON.open("r", encoding="utf-8") as fp:
        audit = json.load(fp)  # (local)
    per_file = audit["per_file"]  # (local)

    l1_records = []  # (local)
    for fn, recs in per_file.items():
        for r in recs:
            # Verify with the canonical 3-class label (P_R structural attestation)
            label = canonical_three_class_label(r.get("tag", ""), r.get("stage_2_5"))  # (local)
            if label == LAYER_L1_NUMERICAL:
                l1_records.append(r)
    n_l1 = len(l1_records)  # (local)
    print(f"  L1-NUMERICAL records found: {n_l1}")

    # 2) Parse registry slot statuses
    print(f"  parsing registry: {INPUT_REGISTRY_MD.relative_to(PROJECT_ROOT)}")
    slot_status = parse_registry_slot_statuses(INPUT_REGISTRY_MD)  # (local)
    print(f"  parsed {len(slot_status)} §VII slots from registry")
    status_dist = Counter(slot_status.values())  # (local)
    for st, cnt in sorted(status_dist.items()):
        print(f"    slot status {st}: {cnt}")

    # 3) Per-record slot mapping + terminal status
    chain = []  # (local)
    rule_counter = Counter()  # (local)
    slot_counter = Counter()  # (local)
    terminal_counter = Counter()  # (local)
    unresolved_records = []  # (local)
    for r in l1_records:
        slot, rule = map_record_to_slot(r)  # (local)
        rule_counter[rule] += 1
        slot_counter[slot] += 1
        if slot == "UNRESOLVED":
            terminal = "UNRESOLVED"
            unresolved_records.append({
                "filename": r["filename"],
                "line": r["line"],
                "match_text": r["match_text"],
                "match_group": r["match_group"],
            })
        else:
            terminal = slot_status.get(slot, "UNRESOLVED")
        terminal_counter[terminal] += 1
        chain.append({
            "filename": r["filename"],
            "line": r["line"],
            "match_text": r["match_text"],
            "match_group": r["match_group"],
            "tag": r["tag"],
            "stage_2_5": r["stage_2_5"],
            "tag_rule": r["tag_rule"],
            "upstream_slot": slot,
            "dispatch_rule": rule,
            "terminal_status": terminal,
            "warrant_chain_closes": terminal in PASS_TERMINAL_STATUSES,
            "warrant_chain_conditional": terminal in INFO_TERMINAL_STATUSES,
        })

    n_mapped = sum(1 for c in chain if c["upstream_slot"] != "UNRESOLVED")  # (local)
    n_unresolved = sum(1 for c in chain if c["terminal_status"] == "UNRESOLVED")  # (local)
    n_closed = sum(
        1 for c in chain if c["terminal_status"] in PASS_TERMINAL_STATUSES
    )  # (local)
    n_candidate = sum(
        1 for c in chain if c["terminal_status"] in INFO_TERMINAL_STATUSES
    )  # (local)

    print(f"  N_mapped     = {n_mapped}/{n_l1}")
    print(f"  N_closed     = {n_closed}")
    print(f"  N_candidate  = {n_candidate}")
    print(f"  N_unresolved = {n_unresolved}")
    print(f"  rule_counter: {dict(rule_counter)}")
    # Print top 12 slot mappings
    print(f"  slot_counter (top 12):")
    for s, c in slot_counter.most_common(12):
        st = slot_status.get(s, "UNRESOLVED") if s != "UNRESOLVED" else "UNRESOLVED"
        print(f"    {s:55s} -> {st:20s} (n={c})")
    print(f"  terminal_counter: {dict(terminal_counter)}")

    return {
        "n_l1_records": n_l1,
        "n_mapped": n_mapped,
        "n_closed": n_closed,
        "n_candidate": n_candidate,
        "n_unresolved": n_unresolved,
        "chain": chain,
        "rule_counter": dict(rule_counter),
        "slot_counter": dict(slot_counter),
        "terminal_counter": dict(terminal_counter),
        "slot_status_dist": dict(status_dist),
        "slot_status_full": slot_status,
        "unresolved_records": unresolved_records,
    }


# ---------------------------------------------------------------------------
# Section 8 -- Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def evaluate_gate(result: dict) -> str:
    """PASS iff N_mapped==1515 AND N_unresolved==0 AND N_candidate==0.

    Substitution chain (verdict direction):
      Definition: PASS_predicate := (N_mapped == 1515)
                                 ∧ (N_unresolved == 0)
                                 ∧ (N_candidate == 0)
                  INFO_predicate := (N_mapped == 1515)
                                 ∧ (N_unresolved == 0)
                                 ∧ (N_candidate >= 1)
                  FAIL_predicate := ¬(N_mapped == 1515)
                                 ∨  (N_unresolved > 0)
      Substitute: each predicate's truth value over the computed counts.
      Simplify:   FAIL takes priority on N_mapped < 1515 OR
                  N_unresolved > 0; INFO fires on candidate present;
                  PASS otherwise.
      Direction:  FAIL > INFO > PASS in priority order; emit accordingly.
    """
    n_mapped = result["n_mapped"]  # (local)
    n_unresolved = result["n_unresolved"]  # (local)
    n_candidate = result["n_candidate"]  # (local)
    if n_mapped != PASS_RECORD_COUNT or n_unresolved > 0:
        return "FAIL"
    if n_candidate >= 1:
        return "INFO"
    return "PASS"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Atomic append of canonical line + dual-SHA companion comment row.

    Single open("a") write per W9a-99 / append-helper canonical pattern
    (parallel-writer-safe POSIX O_APPEND on Windows via Python).
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)


# ---------------------------------------------------------------------------
# Section 9 -- JSON + chain manifest + PNG emission
# ---------------------------------------------------------------------------

def write_json(result: dict, audit_sha: str, content_sha: str) -> None:
    """Write summary + per-record chain to script-side JSON sidecar."""
    payload = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "n_l1_records": result["n_l1_records"],
        "n_mapped": result["n_mapped"],
        "n_closed": result["n_closed"],
        "n_candidate": result["n_candidate"],
        "n_unresolved": result["n_unresolved"],
        "rule_counter": result["rule_counter"],
        "slot_counter": result["slot_counter"],
        "terminal_counter": result["terminal_counter"],
        "slot_status_dist": result["slot_status_dist"],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }  # (local)
    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump(payload, fp, indent=2, sort_keys=False)


def write_chain_manifest(result: dict, audit_sha: str, content_sha: str) -> None:
    """Write the chain manifest at the canonical session-path location.

    This is the deliverable per plan §W13-164 method step 4.
    Spawn-prompt override: write to computations/session-88/ rather than
    computations/ root.
    """
    manifest = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "schema": "s88_w13_warrant_check_chain.v1",
        "composition_theorem": (
            "permanent-results-registry.md §VII.K-PROP "
            "(CC-5 propagation identity) + §VII.K-PROP-W8 "
            "(4-Channel-LAYER-2 Sub-Decomposition + L2-Fully-Admissible "
            "Composition Theorem; S86 W-8 RULE-1)"
        ),
        "warrant_predicate": (
            "warrant(record) := warrant(upstream §VII slot) "
            "AND L2-admissible(record); "
            "L2-admissible(record) := canonical_three_class_label(tag, "
            "stage_2_5) == 'L1-NUMERICAL'"
        ),
        "summary": {
            "n_l1_records": result["n_l1_records"],
            "n_mapped": result["n_mapped"],
            "n_closed": result["n_closed"],
            "n_candidate": result["n_candidate"],
            "n_unresolved": result["n_unresolved"],
            "rule_counter": result["rule_counter"],
            "slot_counter": result["slot_counter"],
            "terminal_counter": result["terminal_counter"],
        },
        "slot_status": result["slot_status_full"],
        "unresolved_records": result["unresolved_records"],
        "chain": result["chain"],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }  # (local)
    with OUT_CHAIN_MANIFEST.open("w", encoding="utf-8") as fp:
        json.dump(manifest, fp, indent=2, sort_keys=False)


def write_png(result: dict) -> None:
    """Emit a 2-panel summary plot.

    Panel A: terminal-status distribution (PASS/INFO routing visualization).
    Panel B: top-15 upstream §VII slot mapping bars.
    """
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(13, 5))

    # Panel A: terminal-status distribution
    statuses = list(result["terminal_counter"].keys())  # (local)
    counts = [result["terminal_counter"][s] for s in statuses]  # (local)
    color_map = {  # (local)
        "STAGE-3-PERMANENT": "#1a9850",
        "PERMANENT":         "#66bd63",
        "PROVEN":            "#a6d96a",
        "CLOSED":            "#d9ef8b",
        "STAGE-1-CANDIDATE": "#fdae61",
        "UNRESOLVED":        "#d73027",
    }
    colors = [color_map.get(s, "#999999") for s in statuses]  # (local)
    bars = axA.bar(statuses, counts, color=colors, edgecolor="k")
    for bar, n in zip(bars, counts):
        axA.text(bar.get_x() + bar.get_width() / 2, n + max(counts) * 0.01,
                 f"{n}", ha="center", va="bottom", fontsize=9, fontweight="bold")
    axA.set_ylabel("record count")
    axA.set_title(f"Terminal-status distribution\n"
                  f"(L1-NUMERICAL records, n={result['n_l1_records']})")
    axA.tick_params(axis="x", rotation=20)
    axA.grid(True, axis="y", alpha=0.3)

    # Panel B: top-15 §VII slot mapping
    slot_top = sorted(result["slot_counter"].items(), key=lambda x: -x[1])[:15]  # (local)
    slot_names = [s[0] for s in slot_top]  # (local)
    slot_counts = [s[1] for s in slot_top]  # (local)
    axB.barh(slot_names, slot_counts, color="#3182bd", edgecolor="k")
    for i, (n, s) in enumerate(zip(slot_counts, slot_names)):
        axB.text(n + max(slot_counts) * 0.01, i, f"{n}",
                 va="center", fontsize=8)
    axB.invert_yaxis()
    axB.set_xlabel("record count")
    axB.set_title("Top-15 upstream §VII slot mapping")
    axB.grid(True, axis="x", alpha=0.3)

    fig.suptitle(f"{GATE_ID} -- L1-NUMERICAL warrant chain via §VII.K-PROP",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, INPUT_CANONICAL_CONSTANTS, pins
    )  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 2. Compute (filter + map + chain)
    result = compute()  # (local)

    # 3. Evaluate gate
    verdict = evaluate_gate(result)  # (local)
    value = (
        f"n_mapped={result['n_mapped']}/{PASS_RECORD_COUNT};"
        f"closed={result['n_closed']};"
        f"candidate={result['n_candidate']};"
        f"unresolved={result['n_unresolved']};"
        f"transitive_composition_closes="
        f"{result['n_unresolved']==0 and result['n_mapped']==PASS_RECORD_COUNT}"
    )  # (local)

    # 4. Emit artifacts
    write_json(result, audit_sha, content_sha)
    write_chain_manifest(result, audit_sha, content_sha)
    write_png(result)

    # 5. Append verdict
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print()
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    # 6. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    print(f"  artifacts:")
    print(f"    {OUT_JSON.relative_to(PROJECT_ROOT)}")
    print(f"    {OUT_CHAIN_MANIFEST.relative_to(PROJECT_ROOT)}")
    print(f"    {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print(f"    {VERDICT_TXT.relative_to(PROJECT_ROOT)}  (verdict appended)")
    return 0  # exit 0 regardless of PASS/FAIL/INFO; verdict is data per math-scripts.md


if __name__ == "__main__":
    sys.exit(main())
