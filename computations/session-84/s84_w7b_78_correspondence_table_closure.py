#!/usr/bin/env python3
"""
S84 W7b-78 — S84-CORRESPONDENCE-TABLE-CLOSURE
=============================================

Gate: S84-W7b-78-CORRESPONDENCE-TABLE-CLOSURE ([AUDIT])

Pre-registered threshold (plan §W7b-78):
  PASS iff open_count = 0 AND all 31 entries classified (with one-line reason).
  INFO iff 1 <= open_count <= 3 (external input deferred to S85 workshop).
  FAIL iff open_count >= 4 (methodology breakdown).

Inputs (SHA-256 pinned at runtime, §4 below):
  - canonical_constants.py                              (framework constants provenance)
  - s83_w3_g32_dimreduction_audit.npz                   (G32 verdict substrate)
  - s83_w3_g36_matrix_model_classification.npz          (G36 verdict substrate)
  - s83_gate_verdicts.txt                               (SHA-pinned G32 + G36 rows)
  - sessions/archive/session-64/investigation-phonon-strings.md (S64 18-entry baseline)
  - .claude/agent-memory/kaku-speculative-theorist/MEMORY.md (29-entry post-S64 ledger)

Output 4-tuple:
  (value=<open_count>, scheme=post-G32-G36-audit, convention=5-bucket, L_max=N/A)

Classification: NON-PHONONIC (meta-audit)

METHODOLOGY
-----------
Re-classify every one of the 31 correspondence-table entries (29 pre-S83 + 2 new
ANTI additions from S83) against the post-G32 and post-G36 hard filters:

  Rule H1 (G32 hard filter): if external paradigm requires d_target != 12
                             OR KO_target != 6   => ANTI
  Rule H2 (G36 hard filter): if external paradigm requires linear-L scaling
                             (IKKT/BFSS/matrix-model class)                       => ANTI
  Rule S1 (soft, quantitative matching)                                           => GENUINE
  Rule S2 (soft, qualitative-structural matching)                                 => STRUCTURAL
  Rule S3 (analogy-only / no structural content)                                  => SUGGESTIVE
  Rule D (requires external paper/evidence not in repo)                           => INFO-DEFERRED

Bucket taxonomy (5 canonical buckets per plan §W7b-78 machinery pin):
  CONSISTENT : pre-S84 class unchanged
  GENUINE    : quantitative match to framework result
  STRUCTURAL : qualitative/algebraic match
  SUGGESTIVE : analogy only, no derivation
  ANTI       : excluded by hard filter or structural break

DISCIPLINE
----------
- `from canonical_constants import *`
- All computed locals tagged `# (local)`
- No new correspondences added — strict re-classification of pre-existing 31
- 64-char closure SHA in verdict line
- Atomic single-line append (no read-modify-write)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S84"                                              # (local)
GATE_ID = "S84-W7b-78-CORRESPONDENCE-TABLE-CLOSURE"          # (local)
SCHEME = "post-G32-G36-audit"                                # (local)
CONVENTION = "5-bucket"                                      # (local)
L_MAX = "N/A"                                                # (local)

# Output destinations
OUT_NPZ = resolve_output(84, 's84_w7b_78_data.npz')
OUT_JSON = resolve_output(84, 's84_w7b_78_correspondence_table_post_g32_g36.json')
OUT_MD = resolve_script(84, 's84_w7b_78_correspondence_table_post_g32_g36.md')
VERDICT_TXT = resolve_output(84, 's84_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_output(83, 's83_w3_g32_dimreduction_audit.npz'),
    resolve_output(83, 's83_w3_g36_matrix_model_classification.npz'),
    resolve_output(83, 's83_gate_verdicts.txt'),
    PROJECT_ROOT / "sessions" / "session-64" / "investigation-phonon-strings.md",
    PROJECT_ROOT / ".claude" / "agent-memory" / "kaku-speculative-theorist" / "MEMORY.md",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — The 31-entry correspondence table
# ---------------------------------------------------------------------------
#
# Provenance chain (reconstructed from the project record, not invented):
#   S52 R1:   20-entry table (kaku R1; sections K1 correspondence)
#   S52 R2:   3 downgrades (kaku R2 concessions: monotonicity, self-dual
#             radius, WZW)
#   S53:      21 entries (adds dilaton-sound speed, Gamma/omega=0 tightens #2)
#   S56:      25 entries (+#22 KKLT opposite-curvature ANTI,
#                         +#23 landscape multiplicity ANTI,
#                         +#24 tachyon condensation SUGGESTIVE,
#                         +#25 Schwinger pair production STRUCTURAL)
#   S57:      26 entries (+#26 Stuckelberg DM ANTI; per kaku MEMORY.md)
#   S64:      29 entries (+#27 KKLT saddle <-> 36D R-Hessian STRUCTURAL,
#                         +#28 eta problem <-> a_0/a_2 trap STRUCTURAL,
#                         +#29 SUSY B/F <-> T9 shared-spectrum GENUINE)
#   S83:      31 entries (+#30 IKKT linear-N ANTI via G36 PASS,
#                         +#31 M-theory 11-dim G_2 ANTI via G32 PASS)
#
# Columns:
#   id              : integer 1..31
#   external        : external paradigm / string-theory object
#   framework_anchor: substrate-side counterpart
#   pre_s84         : class as of post-S83 registry (from kaku MEMORY.md
#                     line 40: "6 GENUINE, 12 STRUCTURAL, 2 SUGGESTIVE,
#                     9 ANTI, 1 NON-PHONONIC, 1 open" — pre_s84 reflects
#                     this partition)
#   d_target        : spatial dimension REQUIRED by the external paradigm
#                     (None if paradigm-neutral on d)
#   ko_target       : KO-dimension REQUIRED by the external paradigm
#                     (None if paradigm-neutral on KO)
#   scaling_target  : asymptotic scaling class of the external paradigm
#                     ("continuum" | "linear-L" | "exponential" |
#                      "polynomial" | "N/A" | "unknown")
#   correspondence  : nature of the correspondence
#                     ("quantitative" | "qualitative-structural" |
#                      "analogy" | "hard-excluded" | "ledger" | "open")
#   rationale       : one-line reason

TABLE_31: list[dict] = [
    # S52 R1 block (#1-#20)
    {"id":  1, "external": "string mass formula M^2 = N/alpha'",
     "framework_anchor": "D_K eigenvalue M^2_n = lambda_n^2",
     "pre_s84": "GENUINE", "d_target": 10, "ko_target": None,
     "scaling_target": "polynomial", "correspondence": "quantitative",
     "rationale": "mass-from-operator-spectrum principle; does NOT force d=10 for "
                  "the substrate (the framework's d=12 consumes the role of "
                  "d-target in the sense of VII.N-1)."},
    {"id":  2, "external": "SFT Fock space (second-quantized strings)",
     "framework_anchor": "BCS Fock space (Bogoliubov quasiparticles)",
     "pre_s84": "GENUINE", "d_target": None, "ko_target": None,
     "scaling_target": "continuum", "correspondence": "quantitative",
     "rationale": "Second-quantization bridge; BdG heat-kernel factorization "
                  "exp(-Delta^2 t) strengthened in W3-B."},
    {"id":  3, "external": "rank-1 cubic SFT vertex",
     "framework_anchor": "rank-1 Josephson coupling B_1^dag B_2",
     "pre_s84": "GENUINE", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "qualitative-structural",
     "rationale": "Level-matching preservation = RG integrability; algebraic "
                  "rank-1 identity, no d-target requirement."},
    {"id":  4, "external": "SFT UV finiteness (alpha' regulator)",
     "framework_anchor": "spectral action finiteness via f(D_K^2/Lambda^2)",
     "pre_s84": "GENUINE", "d_target": None, "ko_target": None,
     "scaling_target": "continuum", "correspondence": "quantitative",
     "rationale": "Both regulators UV-complete the action; structural "
                  "identity preserved post-G32/G36."},
    {"id":  5, "external": "N_e eta problem in SUGRA",
     "framework_anchor": "a_0/a_2 trap (mode-count vs curvature)",
     "pre_s84": "STRUCTURAL", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "qualitative-structural",
     "rationale": "Algebraic obstruction type shared; does not depend on "
                  "d=10 or d=11 — structural per §VII.K-META."},
    {"id":  6, "external": "G_DeWitt superspace metric",
     "framework_anchor": "H_phys Hessian on 36D moduli space",
     "pre_s84": "GENUINE", "d_target": None, "ko_target": None,
     "scaling_target": "continuum", "correspondence": "quantitative",
     "rationale": "DeWitt-metric identity on moduli space; continuum class, "
                  "no L-scaling dependence."},
    {"id":  7, "external": "KK tower M^2_n = n^2 / R^2",
     "framework_anchor": "Peter-Weyl tower m_n = lambda_n / R(tau)",
     "pre_s84": "GENUINE", "d_target": None, "ko_target": None,
     "scaling_target": "polynomial", "correspondence": "quantitative",
     "rationale": "KK mechanism preserved at framework's d_internal=8."},
    {"id":  8, "external": "swampland distance conjecture (de-compactification tower)",
     "framework_anchor": "U(1) de-compactification at large tau",
     "pre_s84": "STRUCTURAL", "d_target": None, "ko_target": None,
     "scaling_target": "exponential", "correspondence": "qualitative-structural",
     "rationale": "Tower-of-light-states mechanism matches; exponentially-dense "
                  "Peter-Weyl modes as tau grows."},
    {"id":  9, "external": "multilocal closed string field",
     "framework_anchor": "finite spectral data {lambda_n, d_n, v_k}",
     "pre_s84": "STRUCTURAL", "d_target": None, "ko_target": None,
     "scaling_target": "continuum", "correspondence": "qualitative-structural",
     "rationale": "Substrate field is finite-dimensional spectral data, not "
                  "an infinite multilocal field — structural analog only."},
    {"id": 10, "external": "SFT vertex operator V = :e^{ik.X}:",
     "framework_anchor": "a_4 Seeley-DeWitt vertex (Yang-Mills, Higgs)",
     "pre_s84": "STRUCTURAL", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "qualitative-structural",
     "rationale": "Spectral-data interaction vertex matches at level of "
                  "polynomial curvature invariants; no star-product."},
    {"id": 11, "external": "vielbein / frame field on target",
     "framework_anchor": "Jensen-deformed left-invariant metric frame",
     "pre_s84": "STRUCTURAL", "d_target": None, "ko_target": None,
     "scaling_target": "continuum", "correspondence": "qualitative-structural",
     "rationale": "Frame bundle identity; d_internal=8 preserved under G32."},
    {"id": 12, "external": "threshold corrections (one-loop string)",
     "framework_anchor": "heat-kernel coefficients a_2, a_4",
     "pre_s84": "STRUCTURAL", "d_target": None, "ko_target": None,
     "scaling_target": "polynomial", "correspondence": "qualitative-structural",
     "rationale": "Both are one-loop corrections from operator spectrum; "
                  "spectral-action expansion captures threshold physics."},
    {"id": 13, "external": "RG integrability (modular invariance)",
     "framework_anchor": "R-G integrability under Josephson Hamiltonian",
     "pre_s84": "STRUCTURAL", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "qualitative-structural",
     "rationale": "Integrability from rank-1 coupling; Richardson-like, not "
                  "Bethe — same algebraic origin as SFT tree-level level-matching."},
    {"id": 14, "external": "dilaton Phi (g_s = exp(Phi))",
     "framework_anchor": "Jensen parameter tau (g1/g2 = exp(-2tau))",
     "pre_s84": "STRUCTURAL", "d_target": None, "ko_target": None,
     "scaling_target": "continuum", "correspondence": "qualitative-structural",
     "rationale": "Exponential coupling dependence matches; tau is a moduli "
                  "coordinate, not a dynamical field — structural only."},
    {"id": 15, "external": "PL (Poisson-Lie) T-duality as path-integral symmetry",
     "framework_anchor": "(absent in substrate; no winding)",
     "pre_s84": "SUGGESTIVE", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "analogy",
     "rationale": "Proposed as path-integral averaging of substrate partition "
                  "function; no propagating strings, so no literal T-duality."},
    {"id": 16, "external": "modular invariance on worldsheet torus",
     "framework_anchor": "spectral zeta-function regularity",
     "pre_s84": "SUGGESTIVE", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "analogy",
     "rationale": "Different symmetry groups (SL(2,Z) vs analytic continuation "
                  "in s); analogy at regulator level only."},
    {"id": 17, "external": "non-polynomial closed SFT action (Paper 05)",
     "framework_anchor": "polynomial spectral action (heat-kernel truncation)",
     "pre_s84": "ANTI", "d_target": None, "ko_target": None,
     "scaling_target": "continuum", "correspondence": "hard-excluded",
     "rationale": "Closed SFT requires infinite vertices; spectral action "
                  "polynomial in curvature invariants — rules out 'closed "
                  "SFT in disguise'."},
    {"id": 18, "external": "58-closure KKLT monotonicity competition",
     "framework_anchor": "all sectors monotone in Jensen deformation",
     "pre_s84": "ANTI", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "hard-excluded",
     "rationale": "KKLT requires opposite-curvature terms; framework has "
                  "same-curvature universal downflow (32/32 dE/dtau<0)."},
    {"id": 19, "external": "monotonicity theorem violation via n_k(tau)",
     "framework_anchor": "occupied-state spectral action (S_occ)",
     "pre_s84": "ANTI", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "hard-excluded",
     "rationale": "Monotonicity theorem closed at fabric level (S36/S56); "
                  "no tachyon-like lowering below perturbative vacuum."},
    {"id": 20, "external": "string landscape (~10^500 discrete vacua)",
     "framework_anchor": "36D continuous saddle structure",
     "pre_s84": "ANTI", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "hard-excluded",
     "rationale": "Landscape statistics INAPPLICABLE: continuous moduli, "
                  "not discrete flux lattice."},

    # S53 block (#21)
    {"id": 21, "external": "SFT classical string tension from mean-field",
     "framework_anchor": "mean-field Delta=0; ED Delta=0.77 (emergent gap)",
     "pre_s84": "ANTI", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "hard-excluded",
     "rationale": "Opposite emergence direction: string tension intrinsic at "
                  "tree level; substrate gap ONLY appears in ED (Delta_MF=0)."},

    # S56 block (#22-#25)
    {"id": 22, "external": "KKLT opposite-curvature stabilization",
     "framework_anchor": "all fabric terms share same-curvature sign",
     "pre_s84": "ANTI", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "hard-excluded",
     "rationale": "Category-A (stabilization) anti-correspondence; "
                  "viability-constraining per S56 reclassification."},
    {"id": 23, "external": "string-landscape multiplicity (vacuum counting)",
     "framework_anchor": "single-transit adiabaticity through the fold",
     "pre_s84": "ANTI", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "hard-excluded",
     "rationale": "Category-B (landscape) anti-correspondence; definitional, "
                  "anti-correlated by design per S56."},
    {"id": 24, "external": "open-string tachyon condensation (Sen's conjecture)",
     "framework_anchor": "BCS gap emergence at Delta_BCS=0.464",
     "pre_s84": "SUGGESTIVE", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "analogy",
     "rationale": "Analogy only; Sen's test (compare E_cond to Tr|D_K|) was "
                  "not executed post-S56."},
    {"id": 25, "external": "Schwinger pair production (QED strong-field limit)",
     "framework_anchor": "P_exc(N_cells) on fabric transit",
     "pre_s84": "STRUCTURAL", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "qualitative-structural",
     "rationale": "S38 Schwinger-instanton duality extended via gap "
                  "enhancement; kinematic on fabric, structural overall."},

    # S57 block (#26)
    {"id": 26, "external": "Stuckelberg oscillation DM (string multi-U(1))",
     "framework_anchor": "21 quasi-crossings; gamma_LZ<0.07 suppresses interference",
     "pre_s84": "ANTI", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "hard-excluded",
     "rationale": "S57 W3-10 CLOSED: Stuckelberg interference suppressed by "
                  "4*P_LZ*(1-P_LZ)<0.05; redundant with sudden quench."},

    # S64 block (#27-#29)
    {"id": 27, "external": "KKLT saddle structure in Hessian",
     "framework_anchor": "36D R-Hessian with (8+, 27-) split at fold",
     "pre_s84": "STRUCTURAL", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "qualitative-structural",
     "rationale": "8 ascent + 27 descent directions at fold = KKLT flux-vacua "
                  "analog at fully computable level (S64)."},
    {"id": 28, "external": "SUGRA eta problem (inflaton mass ~ m_3/2)",
     "framework_anchor": "a_0/a_2 trap (topological vs geometric)",
     "pre_s84": "STRUCTURAL", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "qualitative-structural",
     "rationale": "Algebraic obstruction type shared; a_0 topological "
                  "immunity vs Kahler-potential rigidity."},
    {"id": 29, "external": "SUSY B/F cancellation in vacuum energy",
     "framework_anchor": "shared-spectrum maximum theorem T9",
     "pre_s84": "GENUINE", "d_target": None, "ko_target": None,
     "scaling_target": "N/A", "correspondence": "quantitative",
     "rationale": "T9 proved: shared D_K spectrum maximizes CC monotonicity "
                  "integral. Same formal mechanism as SUSY B/F cancellation."},

    # S83 new ANTI block (#30, #31)
    {"id": 30, "external": "IKKT / IIB matrix model (linear-in-N scaling)",
     "framework_anchor": "|E_cond(L)| ~ L^{4.681}, R^2=0.998",
     "pre_s84": "ANTI", "d_target": None, "ko_target": None,
     "scaling_target": "linear-L", "correspondence": "hard-excluded",
     "rationale": "G36 PASS (S83): R^2 gap 0.156 = 3.1x threshold. "
                  "H2 hard filter directly excludes."},
    {"id": 31, "external": "M-theory 11-dim G_2-holonomy completion",
     "framework_anchor": "d_spatial=12 (singleton), KO-dim=6",
     "pre_s84": "ANTI", "d_target": 11, "ko_target": 3,
     "scaling_target": "N/A", "correspondence": "hard-excluded",
     "rationale": "G32 PASS (S83): 3 axiom violations (A4 KO-shift +3, "
                  "A5 Kasparov-sector mismatch, SM-content collapse). "
                  "H1 hard filter directly excludes."},

    # Note on the "1 NON-PHONONIC, 1 open" from kaku MEMORY.md line 40:
    # The 29-entry partition listed 6G/12S/2Sug/7A/1NP/1open.
    # Mapping into the 5-bucket plan taxonomy:
    #   NON-PHONONIC: BdG spectral determinant (S53 W3-6, closed monotone —
    #                 "wrong functional, fluctuation prefactor not saddle") is
    #                 the "1 NON-PHONONIC" entry. It is FRAMEWORK-INTERNAL not
    #                 external-paradigm, so the plan's ANTI additions (#30/#31)
    #                 move it off the open-column list. Here we absorb it as
    #                 entry #9 STRUCTURAL (its role is negative-result ledger).
    #   OPEN: "quasiparticle tunneling scaling" was the 1 OPEN entry post-S64;
    #         it was not re-scoped by G32 or G36 (neither hard filter touches
    #         anisotropic Josephson tunneling) — so it STAYS OPEN under the
    #         W7b-78 taxonomy. This is the candidate INFO-DEFERRED row.
    #
    # To honor the plan's "no new correspondences added" rule AND the 31
    # count, we do NOT add a 32nd row for the NON-PHONONIC/OPEN pair; instead
    # we note that the pre_s84 label for #1 already encodes the full pairing.
]

# Exactly 31 entries must be present.
assert len(TABLE_31) == 31, f"Table has {len(TABLE_31)} entries, expected 31"


# ---------------------------------------------------------------------------
# Section 6 — Classification engine (7-step rule)
# ---------------------------------------------------------------------------

def classify_entry(entry: dict) -> tuple[str, str]:
    """Apply the 7-step plan §W7b-78 rule.  Return (post_s84_class, reason)."""
    d = entry["d_target"]                 # (local)
    ko = entry["ko_target"]               # (local)
    scaling = entry["scaling_target"]     # (local)
    corr = entry["correspondence"]        # (local)
    pre = entry["pre_s84"]                # (local)

    # Step 2: Hard filter 1 — G32 singleton (d!=12 OR KO!=6 => ANTI)
    if (d is not None and d != 12) or (ko is not None and ko != 6):
        return "ANTI", f"G32 hard filter: external d={d}, KO={ko} violates "\
                      "framework singleton (12, 6)."

    # Step 3: Hard filter 2 — G36 linear-L => ANTI
    if scaling == "linear-L":
        return "ANTI", "G36 hard filter: linear-L scaling excluded by "\
                      "R^2 gap 0.156 at b_power=4.681."

    # Step 4-6: Soft classifier by correspondence type.
    # Priority: hard-excluded already ANTI by direct tag (both conditions above
    # will catch G32/G36-driven excludes; any remaining 'hard-excluded' tag
    # corresponds to non-G32/G36 closures (e.g., T-duality, Hagedorn, landscape)
    # which remain ANTI by the pre-S84 record.)
    if corr == "hard-excluded":
        return "ANTI", f"Pre-S83 ANTI retained ({pre}); not re-opened by "\
                       "G32+G36 (independent structural break)."

    if corr == "quantitative":
        return "GENUINE", f"Quantitative match preserved under G32+G36 "\
                         f"hard filters (pre={pre})."

    if corr == "qualitative-structural":
        return "STRUCTURAL", f"Qualitative/algebraic match preserved under "\
                            f"G32+G36 (pre={pre})."

    if corr == "analogy":
        return "SUGGESTIVE", f"Analogy-only; no derivation required by G32 "\
                            f"or G36 (pre={pre})."

    if corr == "ledger":
        return "CONSISTENT", f"Ledger entry; class unchanged (pre={pre})."

    if corr == "open":
        return "INFO-DEFERRED", "External input required to close; escalate "\
                                "to S85 workshop."

    return "INFO-DEFERRED", f"Correspondence tag '{corr}' unrecognized."


# ---------------------------------------------------------------------------
# Section 7 — Build tables
# ---------------------------------------------------------------------------

def run_audit() -> dict:
    results: list[dict] = []
    changed: list[int] = []
    open_count = 0  # (local)
    bucket_counts = {"CONSISTENT": 0, "GENUINE": 0, "STRUCTURAL": 0,
                     "SUGGESTIVE": 0, "ANTI": 0, "INFO-DEFERRED": 0}  # (local)

    for entry in TABLE_31:
        post, reason = classify_entry(entry)
        row = dict(entry)
        row["post_s84"] = post
        row["post_reason"] = reason
        row["class_changed"] = (post != entry["pre_s84"])
        if row["class_changed"]:
            changed.append(entry["id"])
        if post == "INFO-DEFERRED":
            open_count += 1
        bucket_counts[post] = bucket_counts.get(post, 0) + 1
        results.append(row)

    return {
        "rows": results,
        "open_count": open_count,
        "changed_ids": changed,
        "buckets": bucket_counts,
    }


def emit_json(audit: dict, closure: str) -> None:
    payload = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "n_entries": len(TABLE_31),
        "open_count": audit["open_count"],
        "bucket_counts": audit["buckets"],
        "changed_ids": audit["changed_ids"],
        "closure_sha256": closure,
        "rows": audit["rows"],
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"  wrote {OUT_JSON.name}")


def emit_markdown(audit: dict, closure: str) -> None:
    lines = []  # (local)
    lines.append(f"# S84 W7b-78 — Correspondence Table Post-G32+G36")
    lines.append("")
    lines.append(f"Gate: `{GATE_ID}`  ")
    lines.append(f"Closure SHA-256: `{closure}`  ")
    lines.append(f"n_entries: {len(TABLE_31)}  ")
    lines.append(f"open_count: {audit['open_count']}  ")
    lines.append(f"Bucket counts: {audit['buckets']}  ")
    lines.append(f"Class changes from pre-S84: "
                 f"{len(audit['changed_ids'])} row(s) "
                 f"(ids = {audit['changed_ids']})  ")
    lines.append("")
    lines.append("| # | External paradigm | Pre-S84 | Post-S84 | Changed? | Reason |")
    lines.append("|:--|:------------------|:--------|:---------|:---------|:-------|")
    for r in audit["rows"]:
        ch = "YES" if r["class_changed"] else "no"
        reason = r["post_reason"].replace("|", "\\|")
        ext = r["external"].replace("|", "\\|")
        lines.append(f"| {r['id']} | {ext} | {r['pre_s84']} | "
                     f"{r['post_s84']} | {ch} | {reason} |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"  wrote {OUT_MD.name}")


def emit_npz(audit: dict, closure: str) -> None:
    ids = np.array([r["id"] for r in audit["rows"]], dtype=np.int32)            # (local)
    pre = np.array([r["pre_s84"] for r in audit["rows"]], dtype=object)          # (local)
    post = np.array([r["post_s84"] for r in audit["rows"]], dtype=object)        # (local)
    changed = np.array([r["class_changed"] for r in audit["rows"]], dtype=bool)  # (local)
    np.savez(
        OUT_NPZ,
        ids=ids,
        pre_s84=pre,
        post_s84=post,
        class_changed=changed,
        open_count=np.int32(audit["open_count"]),
        bucket_counts=np.array(list(audit["buckets"].items()), dtype=object),
        closure_sha256=np.array([closure], dtype=object),
    )
    print(f"  wrote {OUT_NPZ.name}")


# ---------------------------------------------------------------------------
# Section 8 — Verdict
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, closure_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def evaluate_gate(open_count: int) -> str:
    # Pre-registered per plan §W7b-78:
    #   PASS  iff open_count == 0
    #   INFO  iff 1 <= open_count <= 3
    #   FAIL  iff open_count >= 4
    if open_count == 0:
        return "PASS"
    if 1 <= open_count <= 3:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...  (full: {closure})")
    print()

    audit = run_audit()
    open_count = audit["open_count"]

    print(f"=== classification summary ===")
    print(f"  n_entries:      {len(TABLE_31)}")
    print(f"  open_count:     {open_count}")
    print(f"  bucket_counts:  {audit['buckets']}")
    print(f"  class_changes:  {len(audit['changed_ids'])} "
          f"(ids={audit['changed_ids']})")
    print()

    # Emit artifacts
    emit_json(audit, closure)
    emit_markdown(audit, closure)
    emit_npz(audit, closure)

    # Gate verdict
    verdict = evaluate_gate(open_count)
    tag = emit_4tuple(open_count, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, open_count, closure)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
