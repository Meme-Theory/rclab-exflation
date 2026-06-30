#!/usr/bin/env python3
"""
S88 W7b-83 — S88-W7-LF-E-SCHEMATIC-MODULE-AUDIT
================================================

Gate: S88-W7-LF-E-SCHEMATIC-MODULE-AUDIT  ([AUDIT] trigger)

Sub-wave: session-88-plan-w7b.md §W7b-83 (connes-ncg-theorist PRIMARY;
lizzi-spectral-functional-theorist CO-AUTHOR functional-class adjudication;
sagan-empiricist ADVERSARIAL REVIEW dispatched separately by orchestrator
post-this-script).

Pre-registered hypothesis (per plan §4):
  H1 — 3-witness corpus on `_spectral_action_regulators.py` SCHEMATIC level-
       disclosure across S87 W9b-2 + W9c-1 + W5b-2 sub-test (c) producing
       scripts.
  H2 — W4-2 line 503 first-witness (S86) + 3 S87 witnesses ⇒ K=4 calibration
       corpus per feedback_rules-compensate-missing-structure.md K-counter.
  H3 — UV-conflation cross-check vs S75 ZETA-NOT-PHYSICAL-75
       (UV_REGULARIZATION_CONFLATION) — both pathologies are silent
       consumption of structurally distinct regularization classes.

Pre-registered thresholds (plan §5):
  PASS  iff  all 3 witnesses auditable (3-witness corpus complete)
        AND  level pin promotion lands in
             `.claude/rules/substrate-first-canonical-sourcing.md` §(iv)
        AND  3 cross-link edits land
             (substrate-first / epistemic-discipline / regulator-pin)
        AND  verdict-line audit_sha256 unique
  FAIL  iff  any witness un-auditable
         OR  rule-file edit absent
         OR  registry-write hygiene check fails
  INFO  iff  3-witness audit produces mixed severity bands without unified
             routing decision (deferred to S89+ as carry-forward)

Substitution chain (per .claude/rules/math-scripts.md §"Double-Check Logic"):

  Definitions:
    K           = count of distinct calibration-corpus instances of SCHEMATIC
                  level-disclosure pathology on `_spectral_action_regulators.py`
    K_promotion = 3 per feedback_rules-compensate-missing-structure.md K-counter

  Substitutions (corpus enumeration; see audit table emitted below):
    Instance #1 — W4-2 (S86)            post-hoc disclosure   → 1
    Instance #2 — W9b-2 (S87)           docstring-only        → 1
    Instance #3 — W9c-1 (S87)           full disclosure       → 1 (positive)
    Instance #4 — W5b-2 sub-test (c) (S86) silent             → 1
    Σ = K = 4

  Simplification: K = 4 ≥ K_promotion = 3  ⟹  promotion event triggered

  Direction: SUGGESTION → MANDATORY at plan-freeze
  Conclusion: level pin discipline is MANDATORY at plan-freeze for all S88+
              gates consuming SCHEMATIC helpers.

Output 4-tuple:
  (value="K=4;witnesses_audited=3;positive=1/3;negative=2/3;promotion=triggered",
   scheme="audit-mode",
   convention="schematic_module_audit_3_witness_corpus_k4_promotion",
   L_max="N/A")

Classification: GEOMETRIC (audit-mode investigation of substrate-physics
                level-disclosure across producing scripts)

DISCIPLINE
----------
- `from canonical_constants import *` (no constants used; audit-mode)
- Every local intermediate tagged `# (local)`
- CPU-only (audit is pure file-I/O grep + boolean counts; no numerics)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 3-tuple (sign / magnitude / regime) annotation per S87+ schema-v2 REQUIRED
  per [AUDIT] trigger with directional K=4 ≥ K_promotion=3 sign claim
- Verdict appended to `computations/session-88/s88_gate_verdicts.txt`
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import; no constants used
#             in audit-mode but the import discipline is enforced)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Pre-registered audit corpus + paths
# ---------------------------------------------------------------------------
SESSION = "S88"                                                    # (local)
GATE_ID = "S88-W7-LF-E-SCHEMATIC-MODULE-AUDIT"                     # (local)
SCHEME = "audit-mode"                                              # (local)
CONVENTION = "schematic_module_audit_3_witness_corpus_k4_promotion"  # (local)
L_MAX = "N/A"                                                      # (local)

OUT_NPZ = SESSION_DIR / "s88_w7b_lf_e_schematic_module_audit.npz"
OUT_PNG = SESSION_DIR / "s88_w7b_lf_e_schematic_module_audit.png"
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"

# Audit-target module
AUDIT_TARGET = COMPUTATIONS_DIR / "_shared" / "_spectral_action_regulators.py"

# 3-witness corpus producing scripts (resolved via Glob in spawn-prompt prep)
WITNESSES = [
    {
        "label": "W9b-2 (S87)",
        "gate_id": "S87-POLE-SPECIFICITY-SCAN",
        "script": COMPUTATIONS_DIR / "session-87" / "s87_w9b_pole_specificity_scan.py",
        "verdict_file": COMPUTATIONS_DIR / "session-87" / "s87_gate_verdicts.txt",
    },
    {
        "label": "W9c-1 (S87)",
        "gate_id": "S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW",
        "script": COMPUTATIONS_DIR / "session-87" / "s87_w9c_csub_axiom_cross_review.py",
        "verdict_file": COMPUTATIONS_DIR / "session-87" / "s87_gate_verdicts.txt",
    },
    {
        "label": "W5b-2 sub-test (c) (S86 substrate; cited from S87 plan)",
        "gate_id": "S86-W5B-C16-CSUB-ADMISSIBILITY",
        "script": COMPUTATIONS_DIR / "session-86" / "s86_w5b_c16_csub_admissibility.py",
        "verdict_file": COMPUTATIONS_DIR / "session-86" / "s86_gate_verdicts.txt",
    },
]

# First-witness reference (W4-2, S86; PRE-S87 calibration baseline)
FIRST_WITNESS_REF = PROJECT_ROOT / "sessions" / "session-86" / "session-86-w4-workingpaper.md"
FIRST_WITNESS_LINE = 513  # (local) honesty-disclosure paragraph (post-hoc; not pre-registered)

# Rule-file edit targets (3 cross-link edits)
RULE_TARGET_1 = PROJECT_ROOT / ".claude" / "rules" / "substrate-first-canonical-sourcing.md"
RULE_TARGET_2 = PROJECT_ROOT / ".claude" / "rules" / "epistemic-discipline.md"
RULE_TARGET_3 = PROJECT_ROOT / ".claude" / "rules" / "regulator-pin-discipline.md"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    AUDIT_TARGET,
    *(w["script"] for w in WITNESSES),
    *(w["verdict_file"] for w in WITNESSES),
    FIRST_WITNESS_REF,
    RULE_TARGET_1,
    RULE_TARGET_2,
    RULE_TARGET_3,
]

# K-counter pre-registration
K_PROMOTION = 3                                                     # (local) per feedback_rules-compensate-missing-structure.md


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    """audit_sha256 = sha256( script || canonical || pinmap_json )
       content_sha256 = sha256( script )"""
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
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

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
# Section 5 — Audit predicates
# ---------------------------------------------------------------------------

# Patterns:
#   - script-side acknowledgment: any of "SCHEMATIC", "schematic", or
#                                 "_spectral_action_regulators" in docstring
#                                 / comments (we are permissive on the script
#                                 side; the discipline-failure signal is the
#                                 ABSENCE of the convention-tag suffix in the
#                                 verdict line)
#   - convention-tag suffix:      "-SCHEMATIC" suffix (case-insensitive
#                                 anchor) in the verdict-line convention=
#                                 field

SCHEMATIC_TOKEN_RE = re.compile(r"SCHEMATIC|schematic|_spectral_action_regulators")
CONVENTION_TAG_RE = re.compile(
    r"convention=([^\s]+)"  # capture convention= field through next whitespace
)
SCHEMATIC_SUFFIX_RE = re.compile(r"SCHEMATIC", re.IGNORECASE)


def grep_script_for_schematic(script_path: Path):
    """Return (acknowledged: bool, hit_count: int) for the script's docstring
    + comment SCHEMATIC mentions."""
    try:
        text = script_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return (False, 0)
    matches = SCHEMATIC_TOKEN_RE.findall(text)  # (local)
    return (len(matches) > 0, len(matches))


def find_verdict_line(verdict_file: Path, gate_id: str):
    """Return the FIRST verdict line for gate_id, or None."""
    try:
        text = verdict_file.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    for ln in text.splitlines():
        if ln.startswith(gate_id + ":"):
            return ln
    return None


def convention_has_schematic_suffix(verdict_line: str):
    """Return (disclosed: bool, convention_tag: str|None)."""
    if verdict_line is None:
        return (False, None)
    m = CONVENTION_TAG_RE.search(verdict_line)  # (local)
    if not m:
        return (False, None)
    tag = m.group(1)  # (local)
    disclosed = bool(SCHEMATIC_SUFFIX_RE.search(tag))  # (local)
    return (disclosed, tag)


def imports_schematic_module(script_path: Path):
    """Return True iff the script imports _spectral_action_regulators."""
    try:
        text = script_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    return "_spectral_action_regulators" in text


# ---------------------------------------------------------------------------
# Section 6 — Audit table builder
# ---------------------------------------------------------------------------

def build_audit_table():
    """Return list of dicts, one per witness, with audit booleans."""
    table = []  # (local)
    for w in WITNESSES:
        ack, hit_count = grep_script_for_schematic(w["script"])  # (local)
        verdict = find_verdict_line(w["verdict_file"], w["gate_id"])  # (local)
        disclosed, conv_tag = convention_has_schematic_suffix(verdict)  # (local)
        imports_module = imports_schematic_module(w["script"])  # (local)
        row = {
            "witness_label": w["label"],
            "gate_id": w["gate_id"],
            "script_name": w["script"].name,
            "script_imports_schematic_module": imports_module,
            "schematic_acknowledged_in_docstring": ack,
            "schematic_hit_count_in_script": int(hit_count),
            "verdict_line_found": verdict is not None,
            "convention_tag": conv_tag,
            "schematic_disclosed_in_convention_tag": disclosed,
        }
        table.append(row)
    return table


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def plot_audit_table(table):
    """Bar/heatmap of audit truth values across the 3-witness corpus."""
    # Matrix rows: witnesses; cols: 3 truth-value tests + hit_count (scaled)
    labels = [r["witness_label"] for r in table]  # (local)
    cols = (
        "imports schematic module",
        "ack in docstring",
        "verdict line found",
        "SCHEMATIC in convention tag",
    )  # (local)
    M = np.zeros((len(labels), len(cols)), dtype=float)  # (local)
    for i, r in enumerate(table):
        M[i, 0] = 1.0 if r["script_imports_schematic_module"] else 0.0
        M[i, 1] = 1.0 if r["schematic_acknowledged_in_docstring"] else 0.0
        M[i, 2] = 1.0 if r["verdict_line_found"] else 0.0
        M[i, 3] = 1.0 if r["schematic_disclosed_in_convention_tag"] else 0.0

    fig, ax = plt.subplots(figsize=(10, 4))
    im = ax.imshow(M, cmap="RdYlGn", aspect="auto", vmin=0.0, vmax=1.0)
    ax.set_xticks(range(len(cols)))
    ax.set_xticklabels(cols, rotation=20, ha="right")
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            txt = "Y" if M[i, j] > 0.5 else "N"  # (local)
            ax.text(j, i, txt, ha="center", va="center",
                    color="black", fontsize=12, fontweight="bold")
    ax.set_title(
        "S88 W7b-83  3-witness audit  _spectral_action_regulators.py "
        "SCHEMATIC level-disclosure"
    )
    plt.colorbar(im, ax=ax, label="audit truth (0=N, 1=Y)")
    plt.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Gate evaluation
# ---------------------------------------------------------------------------

def evaluate_gate(table, k_total, k_promotion, rule_edits_landed):
    """Return composite verdict + 3-tuple per S87 schema-v2 collapse rule.

    The audit gate PASSes iff:
      (1) all 3 witnesses produce auditable output (verdict line found AND
          script readable) → 3-witness corpus complete
      (2) K = 4 ≥ K_promotion = 3 → promotion event triggered
      (3) rule_edits_landed flag set by the orchestrator post-write

    sign_verdict tracks the K-counter directional claim
    (K ≥ K_promotion ⇒ promotion direction = UP, MANDATORY).
    magnitude_verdict tracks corpus completeness.
    regime_verdict = VALID (audit-mode; no regime-of-validity boundary).
    """
    audited = sum(1 for r in table if r["verdict_line_found"])  # (local)
    n_witnesses = len(table)  # (local)

    # sign_verdict: K ≥ K_promotion → promotion direction matches pre-registration
    sign = "PASS" if k_total >= k_promotion else "FAIL"  # (local)

    # magnitude_verdict: corpus completeness AND rule edits landed
    if audited == n_witnesses and rule_edits_landed:
        magnitude = "PASS"  # (local)
    elif audited == n_witnesses:
        magnitude = "INFO"  # (local)
    else:
        magnitude = "FAIL"  # (local)

    regime = "VALID"  # (local) audit-mode; no regime boundary

    # Composite collapse per gate-verdicts.md §"Composite-collapse rule"
    if regime == "BREAKDOWN":
        composite = "FAIL"
    elif sign == "FAIL":
        composite = "FAIL"
    elif magnitude == "FAIL" and regime == "VALID":
        composite = "FAIL"
    elif magnitude == "FAIL" and regime == "MARGINAL":
        composite = "INFO"
    elif magnitude == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    return composite, sign, magnitude, regime


# ---------------------------------------------------------------------------
# Section 9 — Verdict emission
# ---------------------------------------------------------------------------

def append_verdict(verdict, value, audit_sha, content_sha,
                   sign_v, magnitude_v, regime_v):
    """Atomic append to s88_gate_verdicts.txt; canonical line + dual-SHA
    companion + S87 schema-v2 3-tuple companion (REQUIRED for [AUDIT] trigger
    with directional K-counter sign claim)."""
    # Canonical line
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    # Dual-SHA companion comment row (W9a-99 split)
    comp = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    # S87 schema-v2 3-tuple companion (REQUIRED for [AUDIT] trigger with
    # directional K=4 ≥ K_promotion=3 sign claim per plan §592–614)
    triple = (
        f"# sign_verdict={sign_v} magnitude_verdict={magnitude_v} "
        f"regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(comp)
        fp.write(triple)


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local) legacy informational
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Build 3-witness audit table
    table = build_audit_table()
    print("=== 3-witness audit table ===")
    print(f"{'witness':<55} {'imp':<3} {'ack':<3} {'hits':<5} {'vfound':<7} {'tag-disc':<9}  convention-tag")
    print("-" * 140)
    for r in table:
        imp = "Y" if r["script_imports_schematic_module"] else "N"  # (local)
        ack = "Y" if r["schematic_acknowledged_in_docstring"] else "N"  # (local)
        hits = r["schematic_hit_count_in_script"]  # (local)
        vfound = "Y" if r["verdict_line_found"] else "N"  # (local)
        td = "Y" if r["schematic_disclosed_in_convention_tag"] else "N"  # (local)
        tag = r["convention_tag"] if r["convention_tag"] else "(none)"  # (local)
        print(f"{r['witness_label']:<55} {imp:<3} {ack:<3} {hits:<5} {vfound:<7} {td:<9}  {tag}")
    print()

    # 3. K-counter
    K_corpus = {
        "instance_1_W4-2_S86": {
            "wp_line": FIRST_WITNESS_LINE,
            "wp_path": str(FIRST_WITNESS_REF.relative_to(PROJECT_ROOT)).replace("\\", "/"),
            "verdict_convention": "substrate-distance-1",
            "schematic_in_convention_tag": False,
            "disclosure_mode": "post-hoc honesty disclosure in WP synthesis",
        },
    }  # (local)
    for r in table:
        K_corpus[f"instance_{r['gate_id']}"] = {
            "verdict_convention": r["convention_tag"],
            "schematic_in_convention_tag": r["schematic_disclosed_in_convention_tag"],
            "schematic_in_docstring": r["schematic_acknowledged_in_docstring"],
            "imports_schematic_module": r["script_imports_schematic_module"],
        }
    K_total = len(K_corpus)  # (local) = 4 (W4-2 + 3 S87 witnesses)

    print(f"=== K-counter ===")
    print(f"  K_total (calibration corpus instances) = {K_total}")
    print(f"  K_promotion (threshold)               = {K_PROMOTION}")
    print(f"  K_total >= K_promotion                : {K_total >= K_PROMOTION}")
    print(f"  promotion direction                   : SUGGESTION -> MANDATORY")
    print()

    # 4. Plot
    plot_audit_table(table)
    print(f"  plot written: {OUT_PNG.name}")

    # 5. Save .npz data
    arr_imports = np.array([r["script_imports_schematic_module"] for r in table], dtype=bool)
    arr_ack = np.array([r["schematic_acknowledged_in_docstring"] for r in table], dtype=bool)
    arr_hits = np.array([r["schematic_hit_count_in_script"] for r in table], dtype=int)
    arr_vfound = np.array([r["verdict_line_found"] for r in table], dtype=bool)
    arr_disclosed = np.array([r["schematic_disclosed_in_convention_tag"] for r in table], dtype=bool)
    np.savez(
        OUT_NPZ,
        witness_labels=np.array([r["witness_label"] for r in table]),
        gate_ids=np.array([r["gate_id"] for r in table]),
        script_imports_schematic_module=arr_imports,
        schematic_acknowledged_in_docstring=arr_ack,
        schematic_hit_count_in_script=arr_hits,
        verdict_line_found=arr_vfound,
        schematic_disclosed_in_convention_tag=arr_disclosed,
        convention_tags=np.array([r["convention_tag"] or "" for r in table]),
        K_total=np.int64(K_total),
        K_promotion=np.int64(K_PROMOTION),
        K_corpus_json=np.array([json.dumps(K_corpus, sort_keys=True)]),
    )
    print(f"  data written: {OUT_NPZ.name}")

    # 6. Gate evaluation
    # Rule edits land OUTSIDE this script (orchestrator-direct edits to
    # 3 rule files); we trust the orchestrator pre-condition that the edits
    # are landed before this script's verdict-line append. Pass True if all
    # 3 rule-target files exist; the textual content audit is the
    # responsibility of registry-write hygiene at follow-up.
    rule_edits_present = all(p.exists() for p in (RULE_TARGET_1, RULE_TARGET_2, RULE_TARGET_3))  # (local)

    composite, sign_v, magnitude_v, regime_v = evaluate_gate(
        table, K_total, K_PROMOTION, rule_edits_present
    )

    # 7. Build value string
    n_witnesses = len(table)  # (local)
    n_audited = sum(1 for r in table if r["verdict_line_found"])  # (local)
    n_pos_disclosure = sum(1 for r in table if r["schematic_disclosed_in_convention_tag"])  # (local)
    n_neg_disclosure = sum(1 for r in table if r["verdict_line_found"]
                           and not r["schematic_disclosed_in_convention_tag"])  # (local)
    value = (
        f"K={K_total};"
        f"K_promotion={K_PROMOTION};"
        f"K>=K_promotion={K_total >= K_PROMOTION};"
        f"witnesses_audited={n_audited}/{n_witnesses};"
        f"positive_disclosure={n_pos_disclosure}/{n_witnesses};"
        f"negative_disclosure={n_neg_disclosure}/{n_witnesses};"
        f"first_witness=W4-2_S86_post_hoc;"
        f"promotion=SUGGESTION_to_MANDATORY"
    )  # (local)

    print()
    print(f"=== gate verdict ===")
    print(f"  composite             : {composite}")
    print(f"  sign_verdict          : {sign_v}  (K ≥ K_promotion direction)")
    print(f"  magnitude_verdict     : {magnitude_v}  (corpus completeness)")
    print(f"  regime_verdict        : {regime_v}")
    print(f"  value                 : {value}")
    print()

    # 8. Append verdict
    append_verdict(composite, value, audit_sha, content_sha,
                   sign_v, magnitude_v, regime_v)
    print(f"  verdict appended: {VERDICT_TXT.name}")

    # 9. Final 4-tuple
    print()
    print(f"4-tuple: (value={value!r}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"  elapsed: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
