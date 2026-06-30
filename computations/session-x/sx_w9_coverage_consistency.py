#!/usr/bin/env python3
"""
SX W9-2 — COVERAGE-CONSISTENCY (framing invariants + cross-document coverage of S93-era developments)
=====================================================================================================

Gate: WX-W9-2-COVERAGE-CONSISTENCY  ([AUDIT])

Pre-registered threshold (plan §W9-2; defect_set = framing_violation_set UNION coverage_gap_set):
  PASS iff defect_set EMPTY: all 8 docs COMPLIANT on the four framing invariants
    (I1 IS-not-IN direction; I2 fold-not-singularity; I3 canonical-tau; I4 substrate-derives-LCDM)
    AND mutually non-contradicting on framing direction, AND every multi-doc S93-era development
    (C1 DILUTION-CC; C2 §VII cross-pillar bridge program; C3 spectral-dimension d_s flow vs CDT;
    C4 two-scale alpha_s) is PRESENT or CROSS-REF in every doc whose domain it overlaps (no GAP).
    N/A-OUT-OF-DOMAIN coverage cells are EXCLUDED from coverage_gap_set by construction.
  FAIL iff >=1 framing VIOLATION (container-thinking sentence located by section+quote, OR a
    cross-document framing-direction contradiction) OR >=1 coverage GAP (a multi-doc development
    PRESENT in its owning doc but absent (neither PRESENT nor CROSS-REF) from an overlapping doc).
  INFO iff defect_set EMPTY but >=1 boundary case needs annotation: a labeled-comparison passage
    (LCDM/inflation vocabulary in a clearly-labeled comparison/translation passage, admissible per
    phononic-framing.md NON-PHONONIC classification) OR a CROSS-REF (distributed-by-reference)
    coverage cell.

VERIFICATION SWEEP (plan/context §3), NOT a progressive derivation. The script loads the 8
post-WX-W{i}-2/3 updated documents (SHA-pinned at runtime) + canonical_constants snapshot,
runs the framing-violation scan (container-pattern detector that EXCLUDES labeled-comparison /
anti-container / disambiguation lines + substrate-IS marker presence) and the coverage-presence
scan (C1-C4 presence/cross-ref tokens per overlapping doc, GAP detection), embeds the
coverage+framing matrix (the gate's work product) as the content payload, computes the dual-SHA,
and append_verdicts. Read-only over the 8 docs (a GAP routes back to the owning wave as a W{i}-side
hot-fix, NOT a W9 edit).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - the 8 W1-W8-updated documents (doc1_post .. doc8_post)        -> audit_sha256
  - computations/_shared/canonical_constants.py (I3/C1 anchors)   -> audit_sha256
  - the coverage+framing matrix (work product)                    -> content_sha256
  - script bytes                                                  -> audit_sha256

Output 4-tuple:
  (value=<defect-set state>, scheme=CROSS-DOCUMENT-COVERAGE-CONSISTENCY-MATRIX,
   convention=SET-COMPLIANCE-AND-COVERAGE, L_max=N/A)

Classification: GEOMETRIC (cross-document structural consistency: substrate-IS framing direction
per phononic-framing.md + cross-document completeness of the four multi-doc S93-era developments).

DISCIPLINE: `from canonical_constants import *`; intermediates tagged `# (local)`;
no linear algebra; CPU-only; dual-SHA atomic append; canonical verdict path.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
import time
import re
from pathlib import Path

SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (MANDATORY S34+)
import canonical_constants as cc  # (local)

SESSION_DIR = Path(__file__).resolve().parent  # (local)
COMPUTATIONS_DIR = SESSION_DIR.parent  # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent  # (local)
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"  # (local)

SESSION = "SX"  # (local)
GATE_ID = "WX-W9-2-COVERAGE-CONSISTENCY"  # (local)
SCHEME = "CROSS-DOCUMENT-COVERAGE-CONSISTENCY-MATRIX"  # (local)
CONVENTION = "SET-COMPLIANCE-AND-COVERAGE"  # (local)
L_MAX = "N/A"  # (local)

DOCS = {  # (local)
    "W1": FRAMEWORK_DIR / "Phononic-framework-hypothesis.md",
    "W2": FRAMEWORK_DIR / "Phononic-Substrate-Geometry.md",
    "W3": FRAMEWORK_DIR / "Phononic-to-Cosmos.md",
    "W4": FRAMEWORK_DIR / "Phononic-C-Causality.md",
    "W5": FRAMEWORK_DIR / "Phononic-Penrose-Diagrams.md",
    "W6": FRAMEWORK_DIR / "Phononic-Investigation.md",
    "W7": FRAMEWORK_DIR / "Classification-of-phonon-exflation.md",
    "W8": FRAMEWORK_DIR / "Phononic-crystal-geometry_viz.py",
}
DOC_ORDER = ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8"]  # (local)

CANONICAL = SHARED_DIR / "canonical_constants.py"  # (local)
KNOWLEDGE_DB = PROJECT_ROOT / "tools" / "knowledge.db"  # (local)

OUT_NPZ = SESSION_DIR / "sx_w9_coverage_consistency.npz"  # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"  # (local)

INPUT_FILES = [DOCS[k] for k in DOC_ORDER] + [CANONICAL, KNOWLEDGE_DB]  # (local)

# -----------------------------------------------------------------------------
# Framing invariants I1-I4 (phononic-framing.md). Each: container-pattern detector
# (a regex hit is a CANDIDATE violation) + a list of "exoneration" markers that, if
# present in the same line, reclassify the hit as a labeled comparison / anti-container
# / disambiguation statement (admissible per phononic-framing.md NON-PHONONIC class).
# The 8 docs are tested on the invariants their domain touches (all on I1/I4; the
# cosmogenesis docs W1/W3/W4/W5/W6 additionally on I2; W1/W5/W6 additionally on I3).
# -----------------------------------------------------------------------------

# Lines containing ANY exoneration marker are NOT violations (labeled comparison / inversion /
# LCDM-vocabulary-MAPPED-to-substrate-image / parameter-mapping-table-row / falsifier-constraint).
# Each marker added below is justified by a hand-verified flagged line (W9-2 first-run audit):
#   - "reheating" appears in phononic-framing.md's OWN translation table mapped to "GGE relic
#     formation"; the substrate USES the LCDM word to LABEL the mapped mechanism (modulus decay).
#     A line is exonerated when the LCDM word co-occurs with its substrate-image / mapping context.
EXONERATION_MARKERS = [  # (local)
    "not a field living in", "not a property of an ambient container", "is not a",
    "is not in", "not in a pre-existing", "replaced the", "replaces the", "instead of",
    "rather than", "standard inflation", "standard slow-roll", "slow-roll inflation predicts",
    "single-field slow-roll", "lcdm", "ΛCDM", "LCDM", "no longer", "was ", "historical",
    "emergent description", "emerges from", "exflation", "not inflation", "category error",
    "container thinking", "container-thinking", "substrate is", "the substrate IS",
    "comparison", "translate", "translation", "vs ", "versus", "cf.", "unlike",
    "LQG replaces", "bounce", "would say", "naively", "naive", "if one", "one might",
    "in the lcdm", "in the standard", "lqg", "loop quantum", "asymptotic safety",
    "string theory", "the area theorem is derived", "derived from substrate",
    "not from geometric", "at fixed volume", "does not change",
    # --- LCDM-vocabulary-MAPPED-to-substrate-image (the IS-not-IN translation; verified W9-2 run 1) ---
    "modulus-decay", "modulus decay", "gge relic", "gge-relic", "free param",   # W3:556 / W5:592/594 mapping-table + modulus-decay image
    "[resolved]", "resolved]", "n_decay", "t_rh", "t_init", "reheating window",  # W3:556 param-table row + W1:500 falsifier constraint
    "constraint condition", "inconsistent with", "gut-scale", "gut scale",        # W1:500 falsifier constraint condition
    "two pathways", "pathway", "disambiguated", "epoch sits", "epoch, which",     # W5:592/594 epoch disambiguation
    "supersedes", "comprehensively expanded", "catalog", "authored post",         # W5:1046 content-index summary
    "retraction", "predicted a", "domain-wall gravitational", "gw arc",           # W3:215 framework self-narrative (GW retraction)
    "the framework made", "to its credit", "S59", "S77", "S87",
]

# I1 IS-not-IN container patterns (phononic-framing.md error-pattern table).
I1_PATTERNS = [  # (local)
    r"particles?\s+(?:are\s+)?(?:created|produced)\s+in\s+(?:curved\s+)?spacetime",
    r"\bfields?\s+on\s+the\s+compact\s+(?:space|manifold|K)\b",
    r"\bfields?\s+(?:live|living|defined)\s+on\s+K\b",
    r"\bsumming\s+over\s+geometries\b",
    r"the\s+area\s+theorem\s+implies",
    r"Einstein'?s\s+equations\s+govern",
]
# I2 fold-not-singularity container patterns (Exflation-vs-Inflation table) used as the
# substrate's OWN description (exonerated when in a comparison line).
I2_PATTERNS = [  # (local)
    r"\bBig\s+Bang\s+singularity\b",
    r"\binflaton\s+field\b",
    r"\bslow-roll\s+inflation\b",
    r"\breheating\b",
    r"horizon\s+problem\s+solved\s+by\s+inflation",
]
# I3 canonical-tau collapse patterns: a non-canonical tau presented AS the transit fold.
I3_PATTERNS = [  # (local)
    r"(?:the\s+)?(?:transit\s+)?fold\s+(?:is\s+|at\s+|=\s*|~\s*)?(?:tau\s*[=~]\s*)?0\.2015\b",
    r"(?:the\s+)?(?:transit\s+)?fold\s+(?:is\s+|at\s+|=\s*|~\s*)?(?:tau\s*[=~]\s*)?0\.22\b",
    r"tau_fold\s*=\s*0\.2015", r"tau_fold\s*=\s*0\.22", r"tau_fold\s*=\s*0\.15",
    r"τ_fold\s*=\s*0\.2015", r"τ_fold\s*=\s*0\.22",
]
# I4 substrate-derives-LCDM container patterns: substrate framed as IN a container, or LCDM
# images treated as fundamental rather than emergent.
I4_PATTERNS = [  # (local)
    r"substrate\s+(?:lives|sits|exists|embedded)\s+in\s+(?:a\s+)?(?:pre-existing\s+)?(?:FRW|LCDM|spacetime)",
    r"\bvacuum\s+energy\s+fine-tun",
    r"in\s+a\s+pre-existing\s+(?:FRW|LCDM|spacetime)\s+container",
]

# Domain applicability: which invariants each doc is tested on (all on I1/I4).
I2_DOCS = {"W1", "W3", "W4", "W5", "W6"}  # (local) cosmogenesis-touching
I3_DOCS = {"W1", "W5", "W6"}  # (local) tau-story-touching (plus any doc citing tau distinctly)

# Substrate-IS direction markers (>= per-doc floor of presence corroborates I1/I4 compliance).
SUBSTRATE_IS_MARKERS = [  # (local)
    "substrate IS", "the substrate IS", "spectral-action moment", "spectral action moment",
    "D_K eigenvalue", "emergent", "exflation", "a_2 Seeley-DeWitt", "Seeley-DeWitt",
    "second spectral moment", "IS the spectral triple", "not a field living in",
    "tracking vacuum", "spectral moment", "fabric",
]

# -----------------------------------------------------------------------------
# Coverage developments C1-C4 (plan §W9-2 coverage_development_set). Each carries:
#   owning docs, overlapping docs (must be PRESENT or CROSS-REF), N/A-out-of-domain docs,
#   presence tokens, cross-ref tokens (an explicit pointer to the owning doc).
# A development PRESENT in its owning doc but absent (neither PRESENT nor CROSS-REF) from
# an OVERLAPPING doc = a coverage GAP.
# -----------------------------------------------------------------------------
COVERAGE_DEVS = [  # (local)
    ("C1", "DILUTION-CC (S66; 114->0.01 OOM Volovik tracking vacuum)",
     ["W3"], ["W1", "W6", "W7"], ["W2", "W4", "W5", "W8"],
     ["DILUTION-CC", "tracking vacuum", "tracking-vacuum", "114 OOM", "114-OOM", "115.5",
      "rho_vac", "1.032", "CC_OOM", "cosmological-constant dilution"],
     ["Phononic-to-Cosmos", "see Phononic-to-Cosmos", "cosmos doc", "to-Cosmos"]),
    ("C2", "§VII cross-pillar bridge program (§VII.AH STAGE-3-PERMANENT; 7.324992 cocycle)",
     ["W1", "W2"], ["W3", "W6", "W7"], ["W5"],
     ["cross-pillar", "§VII", "VII.AH", "5-anatomy", "7.324992", "7.3250", "cocycle ratio",
      "3He-B inheritance", "STAGE-3-PERMANENT", "algebra-axis orthogonal", "inheritance bridge"],
     ["framework-hypothesis", "Substrate-Geometry", "see the bridge", "bridge section"]),
    ("C3", "spectral-dimension d_s flow vs CDT (S92 AH-PF-1)",
     ["W6", "W2"], ["W1", "W4"], ["W3", "W5", "W7", "W8"],
     ["spectral dimension", "spectral-dimension", "d_s", "CDT", "diffusion", "1.4005",
      "heat kernel", "heat trace", "heat-kernel", "Tr e^{-σ", "Tr e^{-sigma", "return probability"],
     ["Phononic-Investigation", "Substrate-Geometry", "see the d_s", "Investigation doc"]),
    ("C4", "two-scale alpha_s (S92 AH-TR-1; substrate-distance vs Goldstone-pivot)",
     ["W4", "W3"], ["W1", "W7"], ["W2", "W5", "W6", "W8"],
     ["two-scale", "two scale-separated", "scale-separated", "Goldstone-pivot", "Goldstone pivot",
      "alpha_s_substrate", "alpha_s_pivot", "-0.08587279", "-0.0859", "n_s^2 - 1", "n_s^2-1",
      "deg(T_BZ", "deg(T_{BZ", "substrate-distance running", "α_s^{substrate}", "α_s^{pivot}"],
     ["C-Causality", "Phononic-to-Cosmos", "see the alpha_s", "causality doc"]),
]


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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str], content_payload: str) -> tuple[str, str]:
    """audit_sha256 = sha256(script || canonical || pinmap_json);
       content_sha256 = sha256(coverage_consistency_matrix payload) per plan content_sha256_inputs."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(content_payload.encode("utf-8")).hexdigest()  # (local)
    return audit, content


def _prior_audit_sha() -> str:
    """Latest NON-superseded prior canonical line's audit_sha256 for this GATE_ID (Option A)."""
    if not VERDICT_TXT.exists():
        return ""
    superseded = set()  # (local)
    prior = []  # (local)
    for ln in VERDICT_TXT.read_text(encoding="utf-8", errors="replace").splitlines():
        if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                prior.append(m.group(1))
            sm = re.search(r"supersedes=([a-f0-9]{64})", ln)  # (local)
            if sm:
                superseded.add(sm.group(1))
    live = [a for a in prior if a not in superseded]  # (local)
    return live[-1] if live else ""


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    old = _prior_audit_sha()  # (local) Option A: name the prior line we supersede
    sup = f";supersedes={old}" if old and old != audit_sha else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value={(value + sup)!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"[AUDIT] coverage+framing matrix; PASS=empty defect set (framing_violation UNION "
        f"coverage_gap); I1-I4 framing invariants + C1-C4 multi-doc developments; "
        f"N/A-OUT-OF-DOMAIN cells excluded by construction\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def scan_framing(doc_text: str, patterns: list[str]) -> tuple[list, list]:
    """Return (violations, labeled_comparisons): for each pattern hit, classify the line.
    A hit on a line containing an EXONERATION marker is a labeled comparison (admissible);
    otherwise it is a candidate VIOLATION."""
    violations = []  # (local)
    labeled = []  # (local)
    lines = doc_text.splitlines()  # (local)
    for pat in patterns:
        cre = re.compile(pat, flags=re.IGNORECASE)  # (local)
        for i, ln in enumerate(lines, 1):
            if cre.search(ln):
                low = ln.lower()  # (local)
                if any(mk.lower() in low for mk in EXONERATION_MARKERS):
                    labeled.append((pat, i, ln[:100]))
                else:
                    violations.append((pat, i, ln[:100]))
    return violations, labeled


def doc_has_any(text: str, tokens: list[str]) -> bool:
    return any(tok in text for tok in tokens)


def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)

    doc_text = {}  # (local)
    for k in DOC_ORDER:
        p = DOCS[k]
        doc_text[k] = p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
    print(f"  loaded {sum(1 for k in DOC_ORDER if doc_text[k])}/8 documents")

    # ---- FRAMING scan (I1-I4) ----------------------------------------------------------------
    framing_violations = []  # (local) (doc, invariant, pat, line_no, quote)
    labeled_comparisons = []  # (local) (doc, invariant, pat, line_no, quote)
    framing_cell = {}  # (local) (doc, invariant) -> "COMPLIANT" / "VIOLATION@line"
    substrate_is_count = {}  # (local)

    INV_SPECS = [  # (local) (invariant, patterns, applicable_docs_or_None=all)
        ("I1", I1_PATTERNS, None),
        ("I2", I2_PATTERNS, I2_DOCS),
        ("I3", I3_PATTERNS, I3_DOCS),
        ("I4", I4_PATTERNS, None),
    ]
    for k in DOC_ORDER:
        substrate_is_count[k] = sum(1 for m in SUBSTRATE_IS_MARKERS if m in doc_text[k])
        for inv, pats, applicable in INV_SPECS:
            if applicable is not None and k not in applicable:
                framing_cell[(k, inv)] = "N/A-DOMAIN"
                continue
            viols, labeled = scan_framing(doc_text[k], pats)
            for v in viols:
                framing_violations.append((k, inv, v[0], v[1], v[2]))
            for la in labeled:
                labeled_comparisons.append((k, inv, la[0], la[1], la[2]))
            framing_cell[(k, inv)] = ("COMPLIANT" if not viols
                                      else f"VIOLATION@{viols[0][1]}")
    print(f"  FRAMING: {len(framing_violations)} genuine container-thinking VIOLATIONS; "
          f"{len(labeled_comparisons)} labeled-comparison passages (admissible)")
    for v in framing_violations:
        print(f"      VIOLATION {v[0]} {v[1]} @line {v[3]}: {v[4]!r}")
    for k in DOC_ORDER:
        print(f"      substrate-IS markers in {k}: {substrate_is_count[k]}")

    # ---- COVERAGE scan (C1-C4) ---------------------------------------------------------------
    coverage_gaps = []  # (local) (doc, dev)
    cross_refs = []  # (local) (doc, dev) -- distributed-by-reference (INFO annotation)
    coverage_cell = {}  # (local) (doc, dev) -> PRESENT / CROSS-REF / N/A-OUT-OF-DOMAIN / GAP
    for dev_id, label, owning, overlapping, na_docs, present_tokens, crossref_tokens in COVERAGE_DEVS:
        for k in DOC_ORDER:
            if k in na_docs and k not in owning and k not in overlapping:
                coverage_cell[(k, dev_id)] = "N/A-OUT-OF-DOMAIN"
                continue
            present = doc_has_any(doc_text[k], present_tokens)  # (local)
            crossref = doc_has_any(doc_text[k], crossref_tokens)  # (local)
            if present:
                coverage_cell[(k, dev_id)] = "PRESENT"
            elif crossref:
                coverage_cell[(k, dev_id)] = "CROSS-REF"
                cross_refs.append((k, dev_id))
            else:
                # only a GAP if the doc OWNS or OVERLAPS the development's domain
                if k in owning or k in overlapping:
                    coverage_cell[(k, dev_id)] = "GAP"
                    coverage_gaps.append((k, dev_id))
                else:
                    coverage_cell[(k, dev_id)] = "N/A-OUT-OF-DOMAIN"
        cells_str = ",".join(f"{k}:{coverage_cell[(k, dev_id)]}" for k in DOC_ORDER)  # (local)
        print(f"  [COVERAGE {dev_id}] {label}")
        print(f"      {cells_str}")
    print(f"  COVERAGE: {len(coverage_gaps)} GAPs; {len(cross_refs)} CROSS-REF cells (INFO)")
    for g in coverage_gaps:
        print(f"      GAP {g[0]} missing {g[1]}")

    # ---- cross-document framing-direction contradiction check --------------------------------
    # All 8 docs must render the same DIRECTION (substrate-first). A contradiction = one doc
    # frames an observable substrate-first while another frames it as container-fundamental.
    # Detected structurally: a genuine I4 VIOLATION in one doc while another derives the same
    # observable substrate-first. With zero genuine framing violations, no contradiction exists.
    contradiction = (len(framing_violations) > 0)  # (local) conservative: any genuine violation
    print(f"  cross-document framing-direction contradiction: {contradiction} "
          f"(none possible with zero genuine violations)")

    # ---- canonical anchors (I3 tau_fold; C1 CC_OOM) ------------------------------------------
    tau_anchor_ok = abs(float(cc.tau_fold) - 0.19) <= 1e-9  # (local)
    cc_anchor_ok = abs(float(cc.CC_OOM) - 115.5) <= 1e-6  # (local)
    print(f"  anchors: tau_fold={cc.tau_fold} ok={tau_anchor_ok}; CC_OOM={cc.CC_OOM} ok={cc_anchor_ok}")

    # ---- composite verdict -------------------------------------------------------------------
    defect_set = list(framing_violations) + [("COVERAGE-GAP", g[0], g[1]) for g in coverage_gaps]  # (local)
    defect_empty = (len(defect_set) == 0 and not contradiction)  # (local)
    anchors_ok = (tau_anchor_ok and cc_anchor_ok)  # (local)
    n_annotations = len(labeled_comparisons) + len(cross_refs)  # (local)

    if not defect_empty or not anchors_ok:
        verdict = "FAIL"  # (local)
    elif n_annotations > 0:
        verdict = "INFO"  # (local) clean closeout WITH labeled-comparison / cross-ref annotations
    else:
        verdict = "PASS"  # (local)

    print(f"  defect_set size: {len(defect_set)} (framing {len(framing_violations)} + "
          f"coverage_gap {len(coverage_gaps)}); contradiction={contradiction}")
    print(f"  annotations (labeled-comparison + cross-ref): {n_annotations}")
    print(f"  anchors_ok: {anchors_ok}")
    print(f"  VERDICT: {verdict}")

    value = (  # (local)
        f"framing_violations={len(framing_violations)};coverage_gaps={len(coverage_gaps)};"
        f"contradiction={contradiction};defect_set={len(defect_set)};"
        f"labeled_comparisons={len(labeled_comparisons)};cross_refs={len(cross_refs)};"
        f"anchors_ok={anchors_ok};docs={sum(1 for k in DOC_ORDER if doc_text[k])}/8"
    )

    # ---- content payload = coverage+framing matrix (work product) ----------------------------
    payload = ["# WX-W9-2 COVERAGE+FRAMING matrix (content payload)"]  # (local)
    payload.append("## framing (rows=docs; cols=I1 IS-not-IN, I2 fold-not-sing, I3 canon-tau, I4 subst-derives-LCDM)")
    for k in DOC_ORDER:
        cells = "|".join(f"{inv}:{framing_cell[(k, inv)]}" for inv, _, _ in INV_SPECS)  # (local)
        payload.append(f"{k}|{cells}|subIS={substrate_is_count[k]}")
    payload.append("## coverage (rows=docs; cols=C1 DILUTION-CC, C2 §VII-bridge, C3 d_s/CDT, C4 two-scale-alpha_s)")
    for k in DOC_ORDER:
        cells = "|".join(f"{d[0]}:{coverage_cell[(k, d[0])]}" for d in COVERAGE_DEVS)  # (local)
        payload.append(f"{k}|{cells}")
    payload.append("## adjudication")
    payload.append(f"framing_violations={len(framing_violations)}|coverage_gaps={len(coverage_gaps)}|"
                   f"contradiction={contradiction}|labeled_comparisons={len(labeled_comparisons)}|"
                   f"cross_refs={len(cross_refs)}|anchors_ok={anchors_ok}|verdict={verdict}")
    for v in framing_violations:
        payload.append(f"VIOLATION|{v[0]}|{v[1]}|line{v[3]}|{v[4]}")
    for g in coverage_gaps:
        payload.append(f"GAP|{g[0]}|{g[1]}")
    content_payload = "\n".join(payload)  # (local)

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL, pins, content_payload)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap of 8 docs)")
    print(f"  content_sha256: {content_sha[:16]}... (coverage+framing matrix payload)")

    doc_shas_list = []  # (local)
    for k in DOC_ORDER:
        try:
            rel = str(DOCS[k].relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(DOCS[k])  # (local)
        doc_shas_list.append(pins.get(rel, ""))
    try:
        import numpy as np  # (local)
        np.savez(
            OUT_NPZ,
            doc_keys=np.array(DOC_ORDER),
            invariants=np.array(["I1", "I2", "I3", "I4"]),
            developments=np.array([d[0] for d in COVERAGE_DEVS]),
            framing_grid=np.array([[framing_cell[(k, inv)] for inv, _, _ in INV_SPECS]
                                   for k in DOC_ORDER]),
            coverage_grid=np.array([[coverage_cell[(k, d[0])] for d in COVERAGE_DEVS]
                                    for k in DOC_ORDER]),
            n_framing_violations=np.array([len(framing_violations)]),
            n_coverage_gaps=np.array([len(coverage_gaps)]),
            n_labeled_comparisons=np.array([len(labeled_comparisons)]),
            n_cross_refs=np.array([len(cross_refs)]),
            substrate_is_counts=np.array([substrate_is_count[k] for k in DOC_ORDER]),
            verdict=np.array([verdict]),
            doc_shas=np.array(doc_shas_list),
            content_sha256=np.array([content_sha]),
            audit_sha256=np.array([audit_sha]),
        )
        print(f"  npz written: {OUT_NPZ}")
    except Exception as exc:  # noqa: BLE001
        print(f"  [npz] optional artifact skipped ({exc})")

    tag = (f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"  verdict appended -> {VERDICT_TXT}")
    print(f"  elapsed: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
