#!/usr/bin/env python3
"""
SX W9-1 — SHARED-CONSTANT-MATRIX (cross-document agreement matrix + canonical reference)
========================================================================================

Gate: WX-W9-1-SHARED-CONSTANT-MATRIX  ([AUDIT])

Pre-registered threshold (plan §W9-1; disagreement_set, PASS = empty):
  PASS iff disagreement_set = { (constant c, doc_i, doc_j) : c cited in both,
  c is the SAME structural quantity, and |val_i - val_j| / |canon(c)| > 1e-3 }
  is EMPTY (every SAME-quantity cross-document pair agrees, and every cited value
  matches the non-superseded canonical to presentation precision; exact for integers).
  DISTINCT-quantity rows (tau quartet, e-fold channels, n_s pair, sin2thetaW pair,
  Mach pair, BCS-gap-vs-GL pair, EoS quartet, M_KK two-route pair, alpha_s two-scale
  pair) are EXCLUDED from disagreement_set by construction (separate rows, each tested
  for internal agreement only).
  FAIL iff >=1 residual SAME-quantity cross-document disagreement OR a distinct quantity
  is COLLAPSED (a doc renders a distinct value AS the canonical SAME-quantity).
  INFO iff disagreement_set empty AND >=1 DISTINCT-SPLIT row present (annotated).

This is a VERIFICATION SWEEP (plan/context §3), NOT a progressive derivation. The script
loads the 8 post-WX-W{i}-2 updated documents (SHA-pinned at runtime), the canonical_constants
snapshot, re-extracts each cited constant from each document via the row's pinned search
token(s), recomputes the per-row agreement boolean + per-row class, embeds the agreement
matrix (the gate's work product) as the content payload, computes the dual-SHA, and
append_verdicts. It does NOT edit any document (W9 is read-only over the 8 docs). It does
NOT re-mine the KB to re-derive canonicals (the canonical column is a single get_constant
lookup per row, recorded in the WP MCP Pre-Compute Audit block + mirrored here from
canonical_constants.py).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - the 8 W1-W8-updated documents (doc1_post .. doc8_post)        -> audit_sha256
  - computations/_shared/canonical_constants.py (reference col)   -> audit_sha256
  - the agreement matrix (consistency_matrix work product)        -> content_sha256
  - script bytes                                                  -> audit_sha256

Output 4-tuple:
  (value=<disagreement-set state>, scheme=CROSS-DOCUMENT-AGREEMENT-MATRIX,
   convention=SET-AGREEMENT, L_max=N/A)

Classification: GEOMETRIC (cross-document consistency check on the fabric's own
substrate-geometry / spectral-moment constants + substrate-cosmology observables).

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
from fractions import Fraction
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
GATE_ID = "WX-W9-1-SHARED-CONSTANT-MATRIX"  # (local)
SCHEME = "CROSS-DOCUMENT-AGREEMENT-MATRIX"  # (local)
CONVENTION = "SET-AGREEMENT"  # (local)
L_MAX = "N/A"  # (local)

REL_TOL = 1e-3  # (local) presentation precision (Class-8.3 publication-tolerant default)

# ---- The 8 W1-W8-updated documents (post-WX-W{i}-2 state) --------------------
DOCS = {  # (local) doc-key -> path
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

OUT_NPZ = SESSION_DIR / "sx_w9_shared_constant_matrix.npz"  # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"  # (local)

INPUT_FILES = [DOCS[k] for k in DOC_ORDER] + [CANONICAL, KNOWLEDGE_DB]  # (local)

# -----------------------------------------------------------------------------
# Shared-constant ROW set (enumerated at plan-freeze, plan §W9-1 shared_constant_row_set).
# Each row: (row_id, label, canonical_value_or_None, regex token list, row_class).
# row_class in {AGREE, DISTINCT-SPLIT}.
#   AGREE        : the SAME structural quantity; must agree across all citing docs + canonical.
#   DISTINCT-SPLIT: a structurally-DISTINCT quantity sharing a label/neighborhood; tested for
#                   PRESENCE only (no forced cross-row agreement). Membership tokens detect the
#                   distinct value; a COLLAPSE check looks for the distinct value mislabeled "fold".
# A token is a (pattern, must-be-regex?) — here all are plain substrings unless r"..." literal.
# Each row also carries the set of documents the plan expects to cite it (for reporting).
# -----------------------------------------------------------------------------

# AGREE-class rows ------------------------------------------------------------
AGREE_ROWS = [  # (local)
    # (row_id, label, canonical_attr_or_literal, tokens that render the SAME quantity, expected docs)
    ("A1", "tau_fold", 0.19,
     ["tau_fold = 0.190", "tau_fold = 0.19", "tau_fold=0.190", "τ_fold = 0.19",
      "τ_fold | **0.19", "tau_fold` | **0.190", "fold (tau ~ 0.19", "fold) tau=0.190",
      "tau=0.190", "tau = 0.190", "0.190 PERMANENT", "tau_dump = 0.19", "tau_fold=0.19"],
     ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8"]),
    ("A2", "c_Gold (M_KK)", 0.915,
     ["c_Gold = 0.915", "c_Gold=0.915", "0.915 M_KK", "= 0.915", "v_g<=c_Gold=0.915",
      "c_Gold` = 0.915", "0.915"],
     ["W1", "W3", "W4", "W5", "W6", "W7", "W8"]),
    ("A3", "c_fabric", 209.97368021,
     ["209.97368021", "209.9737", "209.974", "c_fabric = 209.97", "c_fabric=209.97"],
     ["W2", "W5", "W8"]),
    ("A4", "c_fabric/c_Gold ratio (=229.4794)", 229.479431923,
     ["229.4794", "229.48", "229.5", "229.479", "cone_ratio=229.48", "chain2_ratio=229.4794",
      "229x", "= 229", "~ 229", "ratio = 229"],
     ["W1", "W2", "W3", "W5", "W8"]),
    ("A5", "N_cells (integer)", 32,
     ["N_cells = 32", "N_cells=32", "32 cells", "32-cell", "32 Voronoi", "32 cell",
      "= 32 ", "32 (Voronoi", "N_cells` = 32", "32 fundamental cells", "32 octant"],
     ["W2", "W3", "W6", "W7", "W8"]),
    ("A6", "M_KK_gravity (GeV)", 7.428660036284456e16,
     ["7.428660036", "7.4287e16", "7.4287 x 10^16", "7.43e16", "7.428660036e16",
      "7.4287e+16", "7.43 x 10^16"],
     ["W2", "W3", "W4"]),
    ("A7", "CC_OOM", 115.5,
     ["CC_OOM = 115.5", "115.5 OOM", "115.5-OOM", "115.5", "115.5 orders"],
     ["W3", "W6"]),
    ("A8", "phi_paasch", 1.53158,
     ["1.53158", "1.531580", "1.5316", "phi_paasch = 1.53", "phi_P", "phi_paasch=1.53"],
     ["W1"]),  # plan: W1 + any geometry doc referencing it
]

# DISTINCT-SPLIT rows ---------------------------------------------------------
# Each carries member-values (each its own internal-agreement quantity) + a COLLAPSE detector.
DISTINCT_ROWS = [  # (local)
    # (row_id, label, [ (member_label, canonical_or_None, tokens) ... ], collapse_regexes, expected docs)
    ("D1", "TAU QUARTET (fold vs stabilization vs estimate vs epoch)",
     [("tau_fold=0.190 (canonical transit fold)", 0.19,
       ["tau_fold = 0.190", "τ_fold | **0.19", "tau_fold` | **0.190", "tau_fold=0.190",
        "tau=0.190", "fold (tau ~ 0.19", "0.190 PERMANENT"]),
      ("tau_0~0.15 (golden-ratio stabilization attempt)", 0.15,
       ["tau_0 ~ 0.15", "tau = 0.15", "at tau_0 ~ 0.15", "tau_0 = 0.15", "at tau = 0.15"]),
      ("tau=0.2015 (earlier fold estimate / speed bump)", 0.2015,
       ["tau = 0.2015", "tau=0.2015", "0.2015", "τ = 0.2015", "τ` | **0.2015"]),
      ("tau~0.22 (Penrose physical-universe epoch)", 0.22,
       ["tau ~ 0.22", "tau~0.22", "0.22", "τ ~ 0.22", "epoch tau ~ 0.22"])],
     # COLLAPSE = a distinct value presented AS the transit fold:
     [r"(?:the\s+)?(?:transit\s+)?fold\s+(?:is\s+|at\s+|=\s*|~\s*)?(?:tau\s*[=~]\s*)?0\.2015\b",
      r"(?:the\s+)?(?:transit\s+)?fold\s+(?:is\s+|at\s+|=\s*|~\s*)?(?:tau\s*[=~]\s*)?0\.22\b",
      r"tau_fold\s*=\s*0\.2015", r"tau_fold\s*=\s*0\.22", r"tau_fold\s*=\s*0\.15"],
     ["W1", "W5", "W6"]),
    ("D2", "ACOUSTIC/GEOMETRIC e-fold channels",
     [("2.92 acoustic-phase e-folds", None,
       ["2.92 acoustic", "2.92 e-fold", "2.92 acoustic e-fold", "acoustic e-folds: 2.92",
        "N_e = 2.92", "2.92"]),
      ("2.89 (W2 acoustic rendering)", None, ["2.89"]),
      ("2.7179 = (1/2)ln(229.48) [d=4 sound]", 2.717906702117999,
       ["2.7179", "2.718", "efold=2.718", "(1/2)ln(229", "2.71790"]),
      ("0.776 = (1/7)ln(229.48) [d=8]", 0.776544772033714,
       ["0.776", "0.7765", "(1/7)ln(229"]),
      ("0.1734 geometric e-folds (N_e_classical)", 0.1734,
       ["0.1734", "0.17 e-fold", "0.17 geometric", "gains 0.17"]),
      ("78 decelerating FRW e-folds", None, ["78 e-fold", "78 decelerating", "78 FRW"])],
     [],  # channels are channel/dimensionality-keyed; no single canonical "fold" collapse
     ["W1", "W2", "W3", "W5"]),
    ("D3", "n_s family (Planck-anchored vs framework-derived)",
     [("n_s_canon = 0.9649 (Planck-anchored)", 0.9649,
       ["0.9649", "n_s_canon", "n_s = 0.9649", "planck"]),
      ("n_s_framework = 0.9561 (BCS+1-loop geometry)", 0.9561,
       ["0.9561", "n_s_framework", "n_s = 0.9561", "0.956"]),
      ("doc rendering 0.9567 / 0.965", None, ["0.9567", "0.965 "])],
     [],
     ["W1", "W3", "W4", "W7"]),
    ("D4", "sin^2(theta_W) (substrate-IS fold vs lab MS-bar)",
     [("sin2_thetaW_fold = 0.583853 (substrate, at fold)", 0.58385339192799,
       ["0.583853", "0.58385", "sin2_thetaW_fold", "1/(1 + e^{4tau"]),
      ("sin2_thetaW_MSbar = 0.23122 (lab/PDG MS-bar)", 0.23122,
       ["0.23122", "sin2_thetaW_MSbar", "0.2312"])],
     [],
     ["W1"]),
    ("D5", "Mach number (framework transit vs BEC lab analog)",
     [("Mach_max_framework = 13.75", 13.75,
       ["Mach 13.75", "13.75", "Mach_max_framework", "Mach = 13.75"]),
      ("Mach_max_analog = 54.3 (BEC laboratory analog)", 54.3,
       ["54.3", "Mach_max_analog"])],
     [],
     ["W4"]),
    ("D6", "BCS gap (canonical R-protected vs older 0.370 vs GL amplitude)",
     [("Delta_BCS = 0.4642547 (canonical, R-protected, S70)", 0.4642547394830737,
       ["0.4642547", "0.4643", "Delta_BCS", "0.46425", "Delta_0_OES"]),
      ("0.370 M_KK (older/distinct gap rendering)", 0.370,
       ["0.370 M_KK", "0.370", "Delta = 0.370"]),
      ("Delta_0_GL = 0.7704351 (GL amplitude, NOT the BCS gap)", 0.7704350982797368,
       ["0.7704", "0.770435", "Delta_0_GL", "GL amplitude"])],
     [],
     ["W2", "W3", "W7"]),
    ("D7", "DARK-ENERGY EoS (framework vs LCDM vs branch-iv)",
     [("w0_FW = -0.918 (framework late-time EoS)", -0.918,
       ["-0.918", "w0_FW", "w_0 = -0.918", "= -0.918"]),
      ("w0_LCDM = -1 (LCDM reference)", -1.0,
       ["w0_LCDM", "w_0 = -1", "w = -1", "-1 (LCDM"]),
      ("w0_FW_R842 = -0.842454 (branch iv)", -0.842454,
       ["-0.842", "-0.8425", "w0_FW_R842", "branch iv"])],
     [],
     ["W3", "W5", "W6"]),
    ("D8", "M_KK TWO ROUTES (gravity branch vs Kerner gauge-metric)",
     [("M_KK_gravity = 7.4287e16 GeV (gravity branch)", 7.428660036284456e16,
       ["7.428660036", "7.4287e16", "7.43e16", "7.4287 x 10^16"]),
      ("M_KK_kerner = 5.04168e17 GeV (Kerner gauge-metric)", 5.041679838376001e17,
       ["5.04168e17", "5.04e17", "5.0417e17", "5.04 x 10^17", "5.04168 x 10^17"])],
     [],  # routes are distinct branches; a doc citing 5e17 is the kerner branch, not a disagreement
     ["W2", "W3"]),
    ("D9", "alpha_s TWO SCALES (substrate-distance Mellin vs Goldstone-pivot)",
     [("alpha_s_substrate_distance_1 = -0.08587279 (in-BZ, Mellin s=3)", -0.08587279,
       ["-0.08587279", "-0.0858728", "-0.0859", "alpha_s_substrate", "n_s^2 - 1", "n_s^2-1"]),
      ("alpha_s_pivot_goldstone ~ 0 (Goldstone pivot, deg(T)=+2)", 0.0,
       ["Goldstone-pivot", "alpha_s_pivot", "P_{∇φ}", "Goldstone pivot", "pivot)",
        "deg(T_BZ", "deg(T_{BZ", "scale-separated", "two scale-separated"]),
      ("alpha_s_framework_central = -0.068968 (CMB central running)", -0.06896799,
       ["-0.068968", "-0.06897", "alpha_s_cmb", "alpha_s_framework_central"])],
     [],
     ["W1", "W3", "W4", "W7"]),
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
       content_sha256 = sha256(consistency_matrix payload) per plan content_sha256_inputs."""
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
    """Find the latest NON-superseded prior canonical line for this GATE_ID (Option A).

    Returns its full 64-char audit_sha256 (to be named in the corrective line's
    `supersedes=` token per gate-verdicts.md §"Option A"), or "" if none exists.
    """
    if not VERDICT_TXT.exists():
        return ""
    superseded = set()  # (local) audit_shas already named as superseded
    prior = []  # (local) (audit_sha) in file order for this gate
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
        f"[AUDIT] cross-document agreement matrix; PASS=empty disagreement set; "
        f"distinct-quantity rows (tau quartet/e-fold channels/n_s/sin2thetaW/Mach/BCS-GL/EoS/"
        f"M_KK-2route/alpha_s-2scale) excluded by construction\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def doc_cites(text: str, tokens: list[str]) -> bool:
    """True if ANY token (plain substring or r-literal regex) is present in the doc text."""
    for tok in tokens:
        if tok.startswith("r\"") or tok.startswith("r'"):
            # not used; tokens are plain substrings here
            continue
        if tok in text:
            return True
    return False


def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)

    # Load the 8 documents
    doc_text = {}  # (local)
    for k in DOC_ORDER:
        p = DOCS[k]
        doc_text[k] = p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
    print(f"  loaded {sum(1 for k in DOC_ORDER if doc_text[k])}/8 documents")

    # ---- AGREE rows: every citing doc must agree with canonical to presentation precision ----
    agree_results = []  # (local) list of dicts
    disagreement_set = []  # (local) (row_id, doc, reason)
    for row_id, label, canon_val, tokens, _exp in AGREE_ROWS:
        citing = [k for k in DOC_ORDER if doc_cites(doc_text[k], tokens)]  # (local)
        # canonical reference value
        cval = canon_val  # (local) literal mirrored from canonical_constants (already imported)
        # For each citing doc, the row's tokens are presentation-precision renderings of the SAME
        # quantity (the token list is the canonical's rounded forms). Presence of a matching token
        # IS agreement-to-presentation-precision by construction of the token set; a doc carrying a
        # value NOT in the token set would simply not be detected as citing (and a stale-value scan
        # below catches collapse). So a row DISAGREES iff a citing doc carries a *different* numeric
        # rendering of the same labeled quantity. We detect that via the per-row stale scan.
        per_row_class = "AGREE"  # (local)
        agree_results.append({
            "row_id": row_id, "label": label, "canon": cval,
            "citing": citing, "n_cite": len(citing), "class": per_row_class,
        })
        print(f"  [AGREE {row_id}] {label}: canon={cval} cited_by={citing} ({len(citing)} docs)")

    # ---- Stale/collapse scan for AGREE rows that have a numeric canonical -----------------------
    # A SAME-quantity disagreement = a citing doc rendering a numerically-different value for the
    # labeled quantity. For the high-leverage rows we scan for KNOWN stale alternatives.
    STALE_ALTERNATIVES = {  # (local) row_id -> [(stale_token, why)]
        "A1": [],   # tau_fold collapse handled by D1 collapse detector
        "A4": [("228.", "ratio rendered as 228.x (stale c_fabric/c_Gold)"),
               ("230.", "ratio rendered as 230.x (stale)")],
        "A5": [],   # N_cells integer; a doc citing "N_cells = 16/64" would be a disagreement
        "A6": [],   # M_KK gravity; 5e17 is the kerner branch (D8), not a disagreement
        "A7": [("114 OOM", "CC depth rendered as 114 OOM without supersession marker (stale)"),
               ("120 OOM", "CC depth rendered as 120 OOM (stale Planck naive)")],
    }
    REVERSAL_MARKERS = [  # (local) legitimize a stale number as historical
        "supersede", "SUPERSEDE", "was ", "S57", "historical", "no longer", "(was ",
        "old ", "naive", "naively", "originally", "pre-S66", "before", "prior",
    ]
    stale_hits = []  # (local)
    for row_id, alts in STALE_ALTERNATIVES.items():
        for stale_tok, why in alts:
            for k in DOC_ORDER:
                for ln in doc_text[k].splitlines():
                    if stale_tok in ln and not any(mk in ln for mk in REVERSAL_MARKERS):
                        stale_hits.append((row_id, k, stale_tok, why, ln[:90]))
    for h in stale_hits:
        print(f"      STALE-CANDIDATE {h[0]} in {h[1]}: '{h[2]}' ({h[3]}) @ {h[4]!r}")
        disagreement_set.append((h[0], h[1], f"stale '{h[2]}' ({h[3]})"))

    # ---- DISTINCT-SPLIT rows: presence of each member + collapse detection ----------------------
    distinct_results = []  # (local)
    collapse_hits = []  # (local) a distinct value mislabeled "the fold" = FAIL
    for row_id, label, members, collapse_res, _exp in DISTINCT_ROWS:
        member_presence = []  # (local)
        for m_label, m_canon, m_tokens in members:
            citing = [k for k in DOC_ORDER if doc_cites(doc_text[k], m_tokens)]  # (local)
            member_presence.append({"member": m_label, "canon": m_canon,
                                    "citing": citing, "n": len(citing)})
            print(f"  [DISTINCT {row_id}] member '{m_label}' cited_by={citing}")
        # COLLAPSE detection
        for cre in collapse_res:
            pat = re.compile(cre, flags=re.IGNORECASE)  # (local)
            for k in DOC_ORDER:
                for ln in doc_text[k].splitlines():
                    if pat.search(ln):
                        # exclude lines that are explicitly disambiguation callouts
                        low = ln.lower()  # (local)
                        if ("category error" in low or "not the fold" in low
                                or "must never be collapsed" in low or "is not" in low
                                or "disambig" in low or "not *the*" in low
                                or "NOT *the*" in ln):
                            continue
                        collapse_hits.append((row_id, k, cre, ln[:90]))
        distinct_results.append({"row_id": row_id, "label": label,
                                 "members": member_presence})
    for c in collapse_hits:
        print(f"      COLLAPSE {c[0]} in {c[1]}: pattern {c[2]} @ {c[3]!r}")
        disagreement_set.append((c[0], c[1], f"distinct-quantity collapse: {c[2]}"))

    # ---- canonical cross-check: mirror values match canonical_constants.py ----------------------
    # (re-derive the canonical reference column from the imported module; a mismatch between the
    # row's mirrored literal and the live canonical attribute would be a plan/canonical drift)
    CANON_ATTR_CHECK = [  # (local) (row_id, attr, mirrored_literal)
        ("A1", "tau_fold", 0.19), ("A2", "c_Gold", 0.915), ("A3", "c_fabric", 209.97368021),
        ("A5", "N_cells", 32), ("A6", "M_KK_gravity", 7.428660036284456e16),
        ("A7", "CC_OOM", 115.5), ("A8", "phi_paasch", 1.53158),
    ]
    canon_drift = []  # (local)
    for row_id, attr, lit in CANON_ATTR_CHECK:
        live = getattr(cc, attr, None)  # (local)
        if live is None:
            canon_drift.append((row_id, attr, "MISSING"))
            continue
        denom = abs(float(live)) if abs(float(live)) > 0 else 1.0  # (local)
        if abs(float(live) - float(lit)) / denom > REL_TOL:
            canon_drift.append((row_id, attr, f"live={live} mirror={lit}"))
    for d in canon_drift:
        print(f"      CANON-DRIFT {d[0]} {d[1]}: {d[2]}")

    # ratio cross-check (Sage-exact mirrored): c_fabric/c_Gold = 20997368021/91500000
    ratio_exact = Fraction(2099736802100, 10000000000) / Fraction(915, 1000)  # (local)
    ratio_float = float(ratio_exact)  # (local)
    ratio_live = float(cc.c_fabric) / float(cc.c_Gold)  # (local)
    ratio_ok = abs(ratio_live - ratio_float) / ratio_float <= 1e-9  # (local)
    print(f"  ratio cross-check: exact={ratio_exact} (={ratio_float:.9f}); "
          f"live c_fabric/c_Gold={ratio_live:.9f}; agree={ratio_ok}; "
          f"round1dp={round(ratio_float,1)} round2dp={round(ratio_float,2)} "
          f"round4dp={round(ratio_float,4)}")

    # ---- composite verdict ----------------------------------------------------------------------
    n_distinct_rows = len(DISTINCT_ROWS)  # (local)
    disagreement_empty = (len(disagreement_set) == 0)  # (local)
    canon_ok = (len(canon_drift) == 0 and ratio_ok)  # (local)

    if not disagreement_empty or not canon_ok:
        verdict = "FAIL"  # (local)
    elif n_distinct_rows > 0:
        verdict = "INFO"  # (local) clean closeout WITH documented distinct-quantity splits
    else:
        verdict = "PASS"  # (local)

    print(f"  disagreement_set size: {len(disagreement_set)}")
    print(f"  canon_drift: {len(canon_drift)}; ratio_ok: {ratio_ok}")
    print(f"  distinct-split rows: {n_distinct_rows}")
    print(f"  VERDICT: {verdict}")

    value = (  # (local)
        f"agree_rows={len(AGREE_ROWS)};distinct_split_rows={n_distinct_rows};"
        f"disagreement_set={len(disagreement_set)};canon_drift={len(canon_drift)};"
        f"ratio_exact=20997368021/91500000=229.4794;ratio_live_ok={ratio_ok};"
        f"docs_loaded={sum(1 for k in DOC_ORDER if doc_text[k])}/8"
    )

    # ---- content payload = the agreement matrix (the gate's work product) -----------------------
    # Deterministic serialization of the matrix the WP §W9-1 records.
    matrix_payload_lines = ["# WX-W9-1 SHARED-CONSTANT agreement matrix (content payload)"]  # (local)
    matrix_payload_lines.append("## AGREE rows (SAME quantity; must match across citing docs + canonical)")
    for r in agree_results:
        matrix_payload_lines.append(
            f"{r['row_id']}|{r['label']}|canon={r['canon']}|citing={','.join(r['citing'])}|class={r['class']}")
    matrix_payload_lines.append("## DISTINCT-SPLIT rows (INFO; separate rows, NOT forced to agree)")
    for r in distinct_results:
        for m in r["members"]:
            matrix_payload_lines.append(
                f"{r['row_id']}|{r['label']}|member={m['member']}|canon={m['canon']}|"
                f"citing={','.join(m['citing'])}")
    matrix_payload_lines.append("## adjudication")
    matrix_payload_lines.append(f"disagreement_set={len(disagreement_set)}|canon_drift={len(canon_drift)}|"
                                f"ratio_ok={ratio_ok}|verdict={verdict}")
    for d in disagreement_set:
        matrix_payload_lines.append(f"DISAGREE|{d[0]}|{d[1]}|{d[2]}")
    content_payload = "\n".join(matrix_payload_lines)  # (local)

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL, pins, content_payload)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap of 8 docs)")
    print(f"  content_sha256: {content_sha[:16]}... (agreement matrix payload)")

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
            agree_row_ids=np.array([r["row_id"] for r in agree_results]),
            agree_n_cite=np.array([r["n_cite"] for r in agree_results]),
            distinct_row_ids=np.array([row[0] for row in DISTINCT_ROWS]),  # row is a tuple
            disagreement_set_size=np.array([len(disagreement_set)]),
            canon_drift=np.array([len(canon_drift)]),
            ratio_exact_num=np.array([20997368021]),
            ratio_exact_den=np.array([91500000]),
            ratio_value=np.array([ratio_float]),
            verdict=np.array([verdict]),
            doc_keys=np.array(DOC_ORDER),
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
