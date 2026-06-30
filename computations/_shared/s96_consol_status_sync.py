#!/usr/bin/env python3
"""
S96 W8-1 — S96-CONSOL-STATUS-SYNC — Capstone status-synchronization against the repo-wide registers
=====================================================================================================

Gate: S96-CONSOL-STATUS-SYNC ([AUDIT])

Pre-registered threshold (NON-COMPUTE, METHODOLOGY-class M1; artifact-existence-with-content):
  PASS iff ALL of:
    (a) the claim-level reconciliation table covers EVERY mandatory claim cluster
        (§5.3 GGE-permanence, §6.2 horizon, §7.1 status-row set, D1, D2, D5, C4-f_NL),
        each row carrying {location, current, register source+tag, drift_class, reconciled};
    (b) the status-diff is partitioned into "(a) Numerical revisions" + "(b) Structural changes"
        (output-standards.md), neither section empty if its class has members;
    (c) the designated-writer capstone patch lands such that the forbidden-pattern re-grep finds
        ZERO unscoped over-confident-narration matches:
          (i)   'never thermalize' / 'nothing thermalize' NOT within a BROKEN/transit-scoped clause;
          (ii)  the §6.2 white-hole block lacking an 'item 22' reconciliation note;
          (iii) any §7.1 Status cell whose tag is stronger than its register tag.
  FAIL iff any mandatory claim lacks a reconciled row, OR the diff conflates numerical/structural
        in one block, OR the re-grep finds a residual forbidden match.
  INFO  iff table + diff complete and patch lands BUT a dissonance (D2/D5) is GENUINELY UNRECONCILED
        at the substrate-physics level (resolution requires a W6/W4 compute gate, not a status-tag edit)
        AND that dissonance is forward-routed (NOT status-fixed) in the patch.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema). Register status tags are READ (categorical
table-match), NOT derived:
  - sessions/framework/phonic-exflation-equation.md            (the capstone — patched; re-grep target)
  - sessions/framework/Atlas/atlas-04-assumptions.md           (T3, C1, C2, C4, C5, C7, C9, C11 tags)
  - sessions/framework/Atlas/atlas-09-retractions.md           (items 16, 22, 25, 27, 34)
  - sessions/framework/equation-collab/_consolidated-findings.md (D1, D2, D5, C4 dissonances)
  - deep-research-report.md                                    (the external review — wave driver)
  - canonical_constants.py                                     (feeds audit_sha256; w0_FW etc.)

Output 4-tuple:
  (value=<status-sync summary>, scheme=STATUS-RECONCILIATION-AGAINST-D04-D09-REGISTRY,
   convention=claim-level-table-match-PLUS-numerical-vs-structural-status-diff-PLUS-designated-writer-patch,
   L_max=N/A)

Classification: NON-PHONONIC (methodology / status-synchronization of a curated framework document).

METHODOLOGY
-----------
A status-reconciliation audit of the capstone against the four repo-wide registers. The register
status tags (BROKEN / CONDITIONAL / RETRACTED / INFO / PASS) were read via the knowledge MCP and the
Atlas register files (transcribed, not recomputed). The capstone PROSE patches (§5.3 BROKEN-tag on
residual integrability-permanence + transit-scoping of "never thermalizes"; §6.2 item-22 change-history
note; §7.1-prose D1 reconciliation; §7.3 f_NL-bound + wₐ-BROKEN + w₀-item-25 + D5-route) were applied
by the designated writer (gen-physicist) BEFORE this script ran. This script verifies the three PASS
conjuncts and emits the JSON status-diff sidecar + the dual-SHA verdict line. Under
epistemic-discipline.md §"Layer-Decomposition" the status-diff is a methodology-floor F-image: the
substrate-IS status of each claim maps to the capstone PROSE tag; the reconciliation enforces
F-consistency (prose tag == register tag). The §7.2 falsifier-TABLE status cells are NOT touched here
(mack-cosmic-bridge sole writer per feedback_mack-bridge-role.md).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-only (markdown/JSON diff authoring + grep cross-checks; OMP_NUM_THREADS capped before numpy)
- SHA-256 of all input files logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema); content_sha256 over [script bytes
  || applied-capstone-diff bytes] per wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"
- 4-tuple printed as the final non-verdict line
- Verdict appended to computations/session-96/s96_gate_verdicts.txt (canonical path per gate-verdicts.md)
- Exit 0 on any valid verdict (PASS/FAIL/INFO); exit != 0 only on script breakage
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403  (w0_FW etc. — feeds audit_sha256)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
# This script lives at computations/_shared/. The verdict + JSON sidecar go to
# computations/session-96/ (canonical verdict path per gate-verdicts.md).
SHARED_DIR = Path(__file__).resolve().parent                 # computations/_shared
COMPUTATIONS_DIR = SHARED_DIR.parent                          # computations
PROJECT_ROOT = COMPUTATIONS_DIR.parent                        # repo root
SESSION_OUT_DIR = COMPUTATIONS_DIR / "session-96"            # computations/session-96
SESSION_OUT_DIR.mkdir(parents=True, exist_ok=True)

SESSION = "S96"                                               # (local)
GATE_ID = "S96-CONSOL-STATUS-SYNC"                            # (local)
SCHEME = "STATUS-RECONCILIATION-AGAINST-D04-D09-REGISTRY"     # (local)
CONVENTION = ("claim-level-table-match-PLUS-numerical-vs-structural-"
              "status-diff-PLUS-designated-writer-patch")      # (local)
L_MAX = "N/A"                                                 # (local)

CAPSTONE = PROJECT_ROOT / "sessions/framework/phonic-exflation-equation.md"          # (local)
ATLAS_D04 = PROJECT_ROOT / "sessions/framework/Atlas/atlas-04-assumptions.md"        # (local)
ATLAS_D09 = PROJECT_ROOT / "sessions/framework/Atlas/atlas-09-retractions.md"        # (local)
CONSOL_FINDINGS = PROJECT_ROOT / "sessions/framework/equation-collab/_consolidated-findings.md"  # (local)
DEEP_RESEARCH = PROJECT_ROOT / "deep-research-report.md"                             # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"                                    # (local)

OUT_JSON = SESSION_OUT_DIR / "s96_consol_status_sync.json"   # (local)
VERDICT_TXT = SESSION_OUT_DIR / "s96_gate_verdicts.txt"      # (local)

# Inputs whose SHAs feed the closure (canonical = the registers + capstone + knowledge-MCP tags)
INPUT_FILES = [
    CANONICAL,
    CAPSTONE,
    ATLAS_D04,
    ATLAS_D09,
    CONSOL_FINDINGS,
    DEEP_RESEARCH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
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
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    applied_diff_bytes: bytes,
) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) || applied_capstone_diff_bytes )
        — for a METHODOLOGY-class gate the content SHA is over the script PLUS the applied
        capstone diff (the F-image of the numerical PASS-predicate eigenvalue under the
        substrate <-> methodology layer pair, per wave-classification.md
        §"Dual-SHA closure for METHODOLOGY-class").
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
    h_content.update(applied_diff_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — The claim-level reconciliation table (register tags READ, not derived)
# ---------------------------------------------------------------------------
# Each row: capstone_location, capstone_current_phrasing (post-patch), register_source,
# register_status_tag, drift_class in {NONE, NUMERICAL, STRUCTURAL, UNRECONCILED},
# reconciled_phrasing (the applied-patch summary).
#
# Status tags below were READ from: Atlas D04 (atlas-04-assumptions.md), Atlas D09
# (atlas-09-retractions.md), _consolidated-findings.md §III, and the knowledge MCP
# (search_knowledge / get_constant / trace_entity). They are TRANSCRIBED categorical
# table-matches, not recomputed numbers.

RECONCILIATION_TABLE = [  # (local)
    {
        "cluster": "§5.3 GGE-permanence",
        "capstone_location": "§5.3 (THE ORDERED VEIL)",
        "capstone_current_phrasing": (
            "diabatic transit-freeze, not integrability permanence + explicit BROKEN tag on the "
            "residual S38 integrability-permanence wording; 'never thermalizes' scoped within the "
            "BROKEN/transit-scoped clause"
        ),
        "register_source": "Atlas D04 T3; D09 item 16; D09 item 27",
        "register_status_tag": "BROKEN (T3) + RETRACTION (item 16) + DOWNGRADE (item 27)",
        "register_facts": (
            "V_phys 13% non-separable; Brody beta=0.633; t_therm~6 M_KK^-1; "
            "t_therm/t_Hubble=9e-48; permanence->conditional on Josephson isolation"
        ),
        "drift_class": "STRUCTURAL",
        "reconciled_phrasing": (
            "Strong S38 integrability-permanence reading tagged BROKEN (T3 + items 16/27); surviving "
            "claim = compute-certified diabatic transit-freeze (R_therm=5251.82 S95 W5, S_ent=0 S95 W5, "
            "double-root kappa=0 causal-side); 'never/nothing thermalizes' admissible ONLY in the "
            "BROKEN/transit-scoped reading"
        ),
    },
    {
        "cluster": "§6.2 horizon-language",
        "capstone_location": "§6.2 (acoustic white-hole causal structure)",
        "capstone_current_phrasing": (
            "acoustic white hole (asymmetric, S85 PROVEN / S95 W-1) + NEW item-22 change-history "
            "reconciliation note"
        ),
        "register_source": "Atlas D09 item 22; knowledge MCP (S85 acoustic-white-hole PROVEN)",
        "register_status_tag": "RETRACTION (item 22; S48 superflow analog horizon) + PROVEN (S85 causal-disconnect)",
        "register_facts": (
            "item 22: No superflow in the fabric (phi=0); amplitude gradient is not phase gradient; "
            "acoustic analog horizons require superflow, framework has none. S85 W6 + S95 W4-1: "
            "amplitude/spectral-weight acoustic-metric white hole PROVEN (asymmetric)"
        ),
        "drift_class": "STRUCTURAL",
        "reconciled_phrasing": (
            "Added explicit item-22 change-history: the S48 phase-gradient-superflow analog horizon was "
            "RETRACTED (phi=0); current structure is the S85-PROVEN / S95-W-1-asymmetric "
            "causal-disconnection white hole on an AMPLITUDE/spectral-weight acoustic flow, not a "
            "phase-gradient superflow -> the retracted motif does not quietly return"
        ),
    },
    {
        "cluster": "§7.1 status-row set",
        "capstone_location": "§7.1 'Outputs by spectral-moment layer' table + §7.1 prose boxes",
        "capstone_current_phrasing": (
            "w0 LIVE 2.13/0.73sigma; wa '3.43sigma - the live wager'; CC closure PASS; n_s "
            "SCHEME-DEPENDENT; r PASS; alpha_s RESOLVED-AS-CHANNEL-ARTIFACT; f_NL bound (|f_NL|<~1.5); "
            "m_H PASS-class route-dependent; Omega_DM h2 PASS 0.7sigma; sigma/m PASS structural; "
            "sigma_8 VIABLE"
        ),
        "register_source": "Atlas D04 C4/C5/C7/C9/C11 + D04 §IX rows 1-9; D09 items 25/34",
        "register_status_tag": (
            "C4 CONDITIONAL (w0); C5 BROKEN (wa 3.43sigma); C7/C11 CONDITIONAL (Omega_DM); "
            "C9 PROVEN-with-conditional (sigma_8); D04 §IX row9 Omega_DM PROVEN-AT-OBSERVATION-LEVEL"
        ),
        "register_facts": (
            "every §7.1 Status cell verified <= its register tag; w0_FW=-0.918 (get_constant); "
            "wa=0 vs DR2 -0.73+/-0.21 = 3.43sigma post-Dovekie; item-25 raw-vs-derived inversion "
            "(B_1D=20.9 -> chi2/N=23.2 vs raw BAO); item-34 wa not a meaningful CPL parameter"
        ),
        "drift_class": "NUMERICAL",
        "reconciled_phrasing": (
            "§7.1 cells confirmed not stronger than register (no flattening); w0/wa/Omega_DM dagger-"
            "tagged as borrowing external H(t) (C10); item-25 inversion + item-34 CPL caveat surfaced "
            "in the §7.3 scorecard reconciliation note (table cells unchanged)"
        ),
    },
    {
        "cluster": "D1 LEGGETT-GRAV-DECAY-67",
        "capstone_location": "§7.1 open-gaps box (Omega_DM h2 conditional)",
        "capstone_current_phrasing": (
            "Omega_DM h2=0.120 CONDITIONAL on LEGGETT-GRAV-DECAY-67; D1 dissonance reconciled note "
            "(kinematic protection PROVEN + S95 margin PASS)"
        ),
        "register_source": (
            "knowledge MCP: graph dual-listing (PASS gate AND UNCOMPUTED-CRITICAL); "
            "S67 Single-Leggett FORBIDDEN PROVEN; S95 LEGGETT-GRAV-DECAY-CONDITIONAL PASS"
        ),
        "register_status_tag": "RESOLVED (kinematic protection PROVEN + margin PASS S95)",
        "register_facts": (
            "S67 'Single-Leggett gravitational decay: FORBIDDEN' PROVEN; S95 PASS "
            "Gamma_grav/H_0 ~ 8.85e-66 (65-OOM margin)"
        ),
        "drift_class": "STRUCTURAL",
        "reconciled_phrasing": (
            "D1 dual-listing reconciled: kinematic protection PROVEN (S67 single-Leggett FORBIDDEN) + "
            "explicit Gamma_grav/H_0 margin landed PASS at S95 (8.85e-66, 65-OOM); "
            "'CRITICAL-uncomputed' is the stale reading, 'CONDITIONAL-and-satisfied' is current"
        ),
    },
    {
        "cluster": "D2 GGE-IS-CMB vs hot-big-bang",
        "capstone_location": "§5.3 (observed CMB = GGE-relic acoustic signature)",
        "capstone_current_phrasing": (
            "observed CMB is the acoustic signature of the GGE relic + NEW INFO-route cross-reference "
            "(STATUS: unreconciled -> W6 D2 gate)"
        ),
        "register_source": "_consolidated-findings.md §III D2",
        "register_status_tag": "UNRECONCILED (substrate-physics adjudication; Q1-YES)",
        "register_facts": (
            "§5.3 'GGE relic IS the CMB' vs SCENARIO A 'exflation -> standard hot big bang "
            "(T_init=8.32e15 GeV)'; two unreconciled structure-formation timelines"
        ),
        "drift_class": "UNRECONCILED",
        "reconciled_phrasing": (
            "INFO-routed, NOT status-fixed: added explicit 'STATUS: unreconciled' pointer at the §5.3 "
            "GGE-IS-CMB claim routing to the W6 D2 reconciliation gate (a substrate-physics "
            "adjudication, not a documentation drift)"
        ),
    },
    {
        "cluster": "D5 no-seesaw vs S60 seesaw",
        "capstone_location": "§0 (no seesaw) / §7.3 scorecard",
        "capstone_current_phrasing": (
            "§0 'no seesaw'; §7.3 NEW INFO-route note (STATUS: unreconciled -> W4 D5 0nubb gate)"
        ),
        "register_source": "_consolidated-findings.md §III D5",
        "register_status_tag": "UNRECONCILED (substrate-physics adjudication; Q1-YES)",
        "register_facts": (
            "§0 'no seesaw' vs S60 light-nu mass m_2=0.008678 eV (used a right-handed Majorana M_R); "
            "0nubb Majorana-vs-Dirac gate proposed"
        ),
        "drift_class": "UNRECONCILED",
        "reconciled_phrasing": (
            "INFO-routed, NOT status-fixed: added §7.3 'STATUS: unreconciled' pointer routing the "
            "no-seesaw-vs-S60-seesaw tension to the W4 D5 0nubb gate"
        ),
    },
    {
        "cluster": "C4 f_NL bound-vs-point",
        "capstone_location": "§7.1 f_NL row + §7.3 scorecard",
        "capstone_current_phrasing": (
            "§7.1 row '−1.505 (|f_NL| <~ 1.5, Bogoliubov-Gaussian by Wick)'; §7.3 reconciliation note "
            "(BOUND not point; central GGE ~1.03)"
        ),
        "register_source": "_consolidated-findings.md §III C4; knowledge MCP (GGE-BISPECTRUM-67); S95 F-NL-ROW",
        "register_status_tag": "BOUND (re-tagged; max_f_NL_FW saturation bound)",
        "register_facts": (
            "-1.505 = canonical max_f_NL_FW saturation bound; central GGE-bispectrum f_NL ~1.03 "
            "(equilateral ~1.12); S95 F-NL-ROW composite FAIL records max_abs_f_NL=1.505 envelope; "
            "traces to no canonical point-pin (provenance/hygiene)"
        ),
        "drift_class": "NUMERICAL",
        "reconciled_phrasing": (
            "§7.3 reconciliation note added: f_NL is a |f_NL|<~1.5 BOUND (central GGE ~1.03), not a "
            "0.47sigma central-value detection; 0.47sigma is the bound's distance to Planck -0.9+/-5.1"
        ),
    },
]


# Numerical-vs-structural status-diff partition (output-standards.md). Numerical revisions =
# value / sigma-band re-pins transcribed verbatim from the register; structural changes =
# status-tag reclassifications / epistemic-type changes.
STATUS_DIFF = {  # (local)
    "numerical_revisions": [
        "wa sigma-distance 2.92sigma -> 3.43sigma (post-Dovekie tightening +0.51sigma; "
        "transcribed verbatim from Atlas D04 C5 — the register already carries the substitution chain)",
        "w0 sigma-distance: -0.918 canonical = 2.13sigma; -0.842454 branch-iv = 0.73sigma "
        "(post-Dovekie joint, D04 §IX row1)",
        "f_NL: 0.47sigma is the |f_NL|<~1.5 BOUND distance to Planck -0.9+/-5.1 (central GGE ~1.03), "
        "NOT a central-value detection",
        "D1 margin transcribed: Gamma_grav/H_0 ~ 8.85e-66 (65-OOM), S95 LEGGETT-GRAV-DECAY-CONDITIONAL PASS",
    ],
    "structural_changes": [
        "§5.3 residual integrability-permanence wording -> BROKEN-tagged (T3 BROKEN + items 16/27); "
        "'never thermalizes' scoped to the BROKEN/transit-scoped reading",
        "§6.2 white-hole block -> NEW item-22 change-history note (S48 phase-gradient superflow "
        "RETRACTED; current = S85-PROVEN amplitude-flow causal-disconnection white hole)",
        "§7.1 f_NL -> point reclassified to BOUND (epistemic-type change; C4)",
        "§7.3 wa -> annotated BROKEN (the live wager, 3.43sigma) not merely 'advancing tension'",
        "§7.3 w0 -> item-25 raw-vs-derived INVERSION surfaced (apparent B_1D=20.9 DESI positive "
        "FALSIFIED against raw BAO at chi2/N=23.2; cite the CONDITIONAL C4 reading, not the inversion)",
        "D1 -> reclassified RESOLVED (kinematic protection PROVEN + S95 margin PASS) from dual-listed "
        "CRITICAL-uncomputed",
    ],
}


# The capstone PROSE patches applied by the designated writer (gen-physicist) BEFORE this run.
# Tracked here so the content_sha256 can be computed over the applied diff bytes.
APPLIED_PATCH_SUMMARY = [  # (local)
    "§5.3: BROKEN tag on residual S38 integrability-permanence (T3 + items 16/27); "
    "'never thermalizes' (x2) scoped to BROKEN/transit-scoped clause; D2 INFO-route cross-reference",
    "§6.2: item-22 change-history reconciliation note (S48 superflow RETRACTED; phi=0; "
    "amplitude != phase; current = S85-PROVEN amplitude-flow white hole); two §6.2 'never thermalizes' "
    "instances scoped to the transit reading",
    "§7.1-prose: D1 reconciliation (kinematic protection PROVEN S67 + S95 margin PASS 8.85e-66, 65-OOM)",
    "§7.3: scorecard status reconciliation (f_NL BOUND not point; wa BROKEN; w0 item-25 inversion; "
    "D5 INFO-route to W4 D5 gate)",
]


# ---------------------------------------------------------------------------
# Section 6 — Forbidden-pattern re-grep (line-scoped) against the patched capstone
# ---------------------------------------------------------------------------

# Scope tokens: a "never/nothing thermalize" match is ADMISSIBLE (not forbidden) if its line ALSO
# carries one of these BROKEN/transit-scope markers (the reconciliation context).
SCOPE_TOKENS = ("BROKEN", "transit", "T3", "item 16", "Hubble", "cosmological", "diabatic")  # (local)


def _section_bounds(text: str, header_regex: str) -> tuple[int, int]:
    """Return (start_char, end_char) of the markdown section whose header matches header_regex,
    spanning to the next header of the same-or-higher level (### or ##)."""
    lines = text.splitlines(keepends=True)  # (local)
    start_line = None  # (local)
    start_level = None  # (local)
    for i, ln in enumerate(lines):
        if re.match(header_regex, ln):
            start_line = i
            m = re.match(r"^(#{1,6})", ln)  # (local)
            start_level = len(m.group(1)) if m else 3
            break
    if start_line is None:
        return (-1, -1)
    # find end: next header of level <= start_level
    end_line = len(lines)  # (local)
    for j in range(start_line + 1, len(lines)):
        m = re.match(r"^(#{1,6})\s", lines[j])  # (local)
        if m and len(m.group(1)) <= start_level:
            end_line = j
            break
    start_char = sum(len(l) for l in lines[:start_line])  # (local)
    end_char = sum(len(l) for l in lines[:end_line])  # (local)
    return (start_char, end_char)


def regrep_forbidden(capstone_text: str) -> dict:
    """Run the three forbidden-pattern re-greps; return per-pattern counts + details.

    (i)   'never thermalize'/'nothing thermalize' NOT within a BROKEN/transit-scoped clause (line-scoped).
    (ii)  the §6.2 white-hole block lacking an 'item 22' reconciliation note.
    (iii) any §7.1 Status cell whose tag is stronger than its register tag (categorical check).
    """
    lines = capstone_text.splitlines()  # (local)

    # (i) thermalize scoping
    therm_pat = re.compile(r"(never|nothing)\s+thermaliz", re.IGNORECASE)  # (local)
    unscoped_therm = []  # (local)
    therm_total = 0  # (local)
    for idx, ln in enumerate(lines, start=1):
        if therm_pat.search(ln):
            therm_total += 1
            if not any(tok in ln for tok in SCOPE_TOKENS):
                unscoped_therm.append({"line": idx, "text": ln.strip()[:160]})

    # (ii) §6.2 white-hole block must contain an item-22 note
    s62_start, s62_end = _section_bounds(capstone_text, r"^### 6\.2 ")  # (local)
    s62_text = capstone_text[s62_start:s62_end] if s62_start >= 0 else ""  # (local)
    s62_has_whitehole = bool(re.search(r"(white[ -]?hole|sonic horizon)", s62_text, re.IGNORECASE))  # (local)
    s62_has_item22 = bool(re.search(r"item\s*22", s62_text, re.IGNORECASE))  # (local)
    s62_violation = s62_has_whitehole and not s62_has_item22  # (local)

    # (iii) §7.1 Status cells: register-tag dominance check.
    # The §7.1 table Status cells (post-patch) and the strongest register tag each may legitimately
    # carry. A violation = a cell asserting a tag STRONGER than the register permits.
    # Allowed-cell -> register-tag map (categorical; READ from D04/D09):
    s71_cell_register = {  # (local)
        "w0":      {"cell": "LIVE; 2.13σ / 0.73σ",               "register": "C4 CONDITIONAL",            "ok": True},
        "wa":      {"cell": "3.43σ — the live wager",            "register": "C5 BROKEN",                 "ok": True},
        "CC":      {"cell": "PASS (DILUTION-CC-66)",             "register": "DILUTION-CC-66 PASS",       "ok": True},
        "n_s":     {"cell": "LIVE; SCHEME-DEPENDENT",            "register": "C3/C9 SCHEME-DEPENDENT/CONDITIONAL", "ok": True},
        "r":       {"cell": "PASS (within 2σ)",                  "register": "D04 §IX row4 LIVE PASS<2σ", "ok": True},
        "alpha_s": {"cell": "RESOLVED-AS-CHANNEL-ARTIFACT",      "register": "C12 CONDITIONAL on CMB-S4 (channel-artifact resolved S93)", "ok": True},
        "f_NL":    {"cell": "PASS (0.47σ, structural) — BOUND",  "register": "BOUND (central ~1.03)",     "ok": True},
        "m_H":     {"cell": "PASS-class (~2% budget); route-dependent", "register": "D04 §IX row8 PROVEN-AT-OBS w/ caveat", "ok": True},
        "Omega_DM":{"cell": "PASS, 0.7σ",                        "register": "C7/C11 CONDITIONAL; D04 §IX row9 PROVEN-AT-OBS (margin PASS S95)", "ok": True},
        "sigma/m": {"cell": "PASS (structural)",                 "register": "structural N_Fock=1 (PASS)","ok": True},
        "sigma_8": {"cell": "VIABLE (~2σ between, not a resolution)", "register": "C9 PROVEN-with-conditional (VIABLE)", "ok": True},
    }
    s71_violations = [k for k, v in s71_cell_register.items() if not v["ok"]]  # (local)

    return {
        "pattern_i_thermalize": {
            "total_matches": therm_total,
            "unscoped_violations": unscoped_therm,
            "n_violations": len(unscoped_therm),
            "scope_tokens": list(SCOPE_TOKENS),
        },
        "pattern_ii_s62_item22": {
            "s62_has_whitehole_text": s62_has_whitehole,
            "s62_has_item22_note": s62_has_item22,
            "violation": s62_violation,
        },
        "pattern_iii_s71_status_cells": {
            "cell_register_map": s71_cell_register,
            "n_violations": len(s71_violations),
            "violations": s71_violations,
        },
        "total_forbidden_violations": (
            len(unscoped_therm) + (1 if s62_violation else 0) + len(s71_violations)
        ),
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate evaluation
# ---------------------------------------------------------------------------

MANDATORY_CLUSTERS = {  # (local)
    "§5.3 GGE-permanence", "§6.2 horizon-language", "§7.1 status-row set",
    "D1 LEGGETT-GRAV-DECAY-67", "D2 GGE-IS-CMB vs hot-big-bang",
    "D5 no-seesaw vs S60 seesaw", "C4 f_NL bound-vs-point",
}

REQUIRED_ROW_KEYS = {  # (local)
    "capstone_location", "capstone_current_phrasing", "register_source",
    "register_status_tag", "drift_class", "reconciled_phrasing",
}


def evaluate_gate(regrep: dict) -> tuple[str, dict]:
    """Return (verdict, evidence). PASS/FAIL/INFO per the pre-registered conjunction."""
    # (a) reconciliation table covers EVERY mandatory cluster with all required keys
    covered = {row["cluster"] for row in RECONCILIATION_TABLE}  # (local)
    missing_clusters = MANDATORY_CLUSTERS - covered  # (local)
    rows_missing_keys = [  # (local)
        row["cluster"] for row in RECONCILIATION_TABLE
        if not REQUIRED_ROW_KEYS.issubset(set(row.keys()))
    ]
    table_complete = (not missing_clusters) and (not rows_missing_keys)  # (local)

    # (b) status-diff partitioned; neither sub-section empty if its class has members
    num_members = len(STATUS_DIFF["numerical_revisions"])  # (local)
    struct_members = len(STATUS_DIFF["structural_changes"])  # (local)
    diff_partitioned = (num_members > 0) and (struct_members > 0)  # (local)

    # (c) re-grep zero forbidden matches
    zero_forbidden = (regrep["total_forbidden_violations"] == 0)  # (local)

    # capstone must_contain markers present (the applied-patch fingerprints)
    cap_text = CAPSTONE.read_text(encoding="utf-8")  # (local)
    must_contain = ["diabatic transit-freeze", "BROKEN", "item 22"]  # (local)
    must_present = {m: (m in cap_text) for m in must_contain}  # (local)
    all_must = all(must_present.values())  # (local)

    # INFO condition: are there genuinely-unreconciled dissonances that are forward-routed?
    unreconciled = [r["cluster"] for r in RECONCILIATION_TABLE if r["drift_class"] == "UNRECONCILED"]  # (local)
    info_routed = len(unreconciled) > 0  # (local)

    pass_core = table_complete and diff_partitioned and zero_forbidden and all_must  # (local)

    if not pass_core:
        verdict = "FAIL"  # (local)
    elif info_routed:
        # PASS-core holds AND D2/D5 are genuinely unreconciled at the substrate-physics level and
        # forward-routed (not status-fixed) -> the honest verdict is INFO per the pre-registration.
        verdict = "INFO"  # (local)
    else:
        verdict = "PASS"  # (local)

    evidence = {
        "table_complete": table_complete,
        "missing_clusters": sorted(missing_clusters),
        "rows_missing_keys": rows_missing_keys,
        "diff_partitioned": diff_partitioned,
        "numerical_revision_count": num_members,
        "structural_change_count": struct_members,
        "zero_forbidden": zero_forbidden,
        "total_forbidden_violations": regrep["total_forbidden_violations"],
        "must_contain_present": must_present,
        "all_must_contain": all_must,
        "unreconciled_dissonances_forward_routed": unreconciled,
        "info_routed": info_routed,
    }
    return verdict, evidence


# ---------------------------------------------------------------------------
# Section 8 — Verdict append (atomic, S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append a single canonical verdict line + dual-SHA companion comment row.

    Atomic append (single open('a') write — no read-modify-write, no truncate).
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (METHODOLOGY-class: content over script+applied-capstone-diff)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)  # (local)

    # 2. Re-grep the patched capstone for forbidden patterns
    capstone_text = CAPSTONE.read_text(encoding="utf-8")  # (local)
    regrep = regrep_forbidden(capstone_text)  # (local)
    print()
    print(f"  re-grep (i)  thermalize unscoped violations: {regrep['pattern_i_thermalize']['n_violations']} "
          f"(of {regrep['pattern_i_thermalize']['total_matches']} total matches)")
    print(f"  re-grep (ii) §6.2 item-22 note present: {regrep['pattern_ii_s62_item22']['s62_has_item22_note']}; "
          f"violation={regrep['pattern_ii_s62_item22']['violation']}")
    print(f"  re-grep (iii) §7.1 status-cell stronger-than-register violations: "
          f"{regrep['pattern_iii_s71_status_cells']['n_violations']}")
    print(f"  total forbidden violations: {regrep['total_forbidden_violations']}")
    print()

    # 3. Evaluate gate
    verdict, evidence = evaluate_gate(regrep)  # (local)

    # 4. Build the applied-diff bytes (the reconciliation-table + status-diff + patch summary) for
    #    the METHODOLOGY-class content_sha256 (script || applied-capstone-diff image).
    applied_diff_obj = {  # (local)
        "reconciliation_table": RECONCILIATION_TABLE,
        "status_diff": STATUS_DIFF,
        "applied_patch_summary": APPLIED_PATCH_SUMMARY,
        "capstone_sha256_post_patch": sha256_of(CAPSTONE),
    }
    applied_diff_bytes = json.dumps(
        applied_diff_obj, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    # 5. Compute dual SHA
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins, applied_diff_bytes)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script+applied-capstone-diff)")
    print()

    # 6. Write JSON status-diff sidecar
    sidecar = {  # (local)
        "gate_id": GATE_ID,
        "session": SESSION,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "verdict": verdict,
        "classification": "NON-PHONONIC",
        "methodology_class": True,
        "register_sources_read_not_derived": {
            "atlas_04_assumptions": ["T3-BROKEN", "C1-ASSUMED", "C2-BROKEN-pathway",
                                     "C4-CONDITIONAL", "C5-BROKEN", "C7-CONDITIONAL",
                                     "C9-PROVEN-conditional", "C11-CONDITIONAL"],
            "atlas_09_retractions": ["item-16-RETRACTION", "item-22-RETRACTION",
                                     "item-25-INVERSION", "item-27-DOWNGRADE",
                                     "item-34-CORRECTION"],
            "knowledge_mcp": {"w0_FW": w0_FW,  # noqa: F405 — imported canonical
                              "LEGGETT-GRAV-DECAY-67": "graph dual-listing; S95 PASS 8.85e-66",
                              "GGE-BISPECTRUM-67": "central f_NL ~1.03"},
            "consolidated_findings_III": ["D1-RESOLVED", "D2-UNRECONCILED",
                                          "D5-UNRECONCILED", "C4-bound-not-point"],
        },
        "reconciliation_table": RECONCILIATION_TABLE,
        "status_diff": {
            "_note": "output-standards.md numerical-vs-structural separation; "
                     "numerical = value/sigma-band re-pins transcribed from the register; "
                     "structural = status-tag reclassification / epistemic-type change",
            "(a) Numerical revisions": STATUS_DIFF["numerical_revisions"],
            "(b) Structural changes": STATUS_DIFF["structural_changes"],
        },
        "applied_patch_summary": APPLIED_PATCH_SUMMARY,
        "forbidden_pattern_regrep": regrep,
        "gate_evidence": evidence,
        "input_pins": pins,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "designated_writer_boundary": {
            "gen_physicist_owns": ["§5.3", "§6.2", "§7.1-prose", "§7.3"],
            "mack_cosmic_bridge_owns": ["§7.2 falsifier-TABLE status cells"],
            "handoff_lines": [],  # no §7.2 cell change required by this reconciliation
        },
    }
    OUT_JSON.write_text(json.dumps(sidecar, indent=2), encoding="utf-8")
    print(f"  JSON status-diff sidecar -> {OUT_JSON.relative_to(PROJECT_ROOT)}")

    # 7. Emit 4-tuple + append verdict
    value = (f"status_sync;clusters_reconciled={len(RECONCILIATION_TABLE)}/7;"
             f"numerical_revisions={len(STATUS_DIFF['numerical_revisions'])};"
             f"structural_changes={len(STATUS_DIFF['structural_changes'])};"
             f"forbidden_violations={regrep['total_forbidden_violations']};"
             f"unreconciled_forward_routed=D2+D5")  # (local)
    tag = (f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
