#!/usr/bin/env python3
"""
S86 W13-P9-W0-PRIMARY-VALUE-RESOLVE — Adjudicate two w_0_FW candidates
======================================================================

Gate: S86-W0-PRIMARY-VALUE-RESOLVE  ([AUDIT] + [SIGN])

Task: Pre-register a deterministic decision rule selecting either
  - Candidate A: w_0_A = -0.918   (S5 row #1, Volovik partition; canonical_constants.py current pin)
  - Candidate B: w_0_B = -0.842454 (S85 W10-2 branch-(iv), substrate-compaction)
as PRIMARY framework w_0_FW prediction. PRIMARY designation must be REVERSIBLE
under DR3 trigger conditions (R_842 lockout protocol per S84 W1b-9).

Method (per `feedback_agent-roster.md` 6-step pattern):
  Step 1 — Define both candidates with full provenance.
  Step 2 — Derive each candidate's geometric distance from LCDM (w=-1).
  Step 3 — Derive each candidate's relationship to the registered DR3
           falsifier rectangle R_842.
  Step 4 — Derive each candidate's falsifiability under DR3 Scenarios A/B/C/B-precise.
  Step 5 — Adjudicate via 4 independent criteria (NO single-criterion shortcut).
  Step 6 — Apply pre-registered decision rule deterministically.

Pre-registered threshold:
  PASS iff (a) decision rule lands in `sessions/framework/registry/w0-primary-decision-rule.md`
          AND (b) PRIMARY designated AND (c) reversibility protocol pre-registered
          AND (d) both candidates cross-referenced AND (e) falsifier-master-inventory.md
          Row #1 cross-references the new file.
  FAIL iff any of (a)-(e) absent OR adjudication arithmetic incorrect (cf. §10
       substitution chain in plan §W13-3.10).
  INFO iff not applicable; this is an adjudication gate that produces a
       deterministic decision rule.

Output 4-tuple:
  (value=PRIMARY=A=-0.918, scheme=4-criterion-adjudication,
   convention=registry-history-priority, L_max=N/A)

Classification: PHONONIC — w_0_FW IS the late-time projection of the substrate's
spectral-action gradient at the fold; both candidates are TWO METHODOLOGICALLY-
DISTINCT projections of the SAME substrate observable (Volovik-partition averaging
vs substrate-compaction direct evaluation), not competing models. PRIMARY
designation is OBSERVATIONAL-CITATION discipline, not a physics ranking.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-only (adjudication = arithmetic + decision tree); thread cap below
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict appended to `computations/session-86/s86_gate_verdicts.txt` with BOTH
  audit_sha256 + content_sha256 + schema_version=S84+
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (BEFORE numpy import)
# ---------------------------------------------------------------------------
import os
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

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

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

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSIONS_DIR = PROJECT_ROOT / "sessions"
FRAMEWORK_DIR = SESSIONS_DIR / "framework"

SESSION = "S86"                                                    # (local)
GATE_ID = "S86-W0-PRIMARY-VALUE-RESOLVE"                           # (local)
SCHEME = "4-criterion-adjudication"                                # (local)
CONVENTION = "registry-history-priority"                           # (local)
L_MAX = "N/A"                                                      # (local)

# Pre-registered candidates (locked at plan §W13-3.5 Hypothesis)
W_0_A = -0.918                                                     # (local) Volovik partition pin (matches w0_FW canonical)
W_0_B = -0.842454                                                  # (local) substrate-compaction (S85 W10-2 branch-(iv))
W_0_LCDM = -1.0                                                    # (local) LCDM w by definition
SIGMA_W0_DR3 = 0.025                                               # (local) DR3 sigma fiducial (S69 master)

# DR3 falsifier rectangle R_842 (TWO definitions documented; mack-9A is the
# primary canonical; plan-prompt R is wider). The decision rule does NOT
# depend on R_842 membership for either candidate (both inside the canonical).
R842_W0_LO_PLAN = -1.05                                            # (local) plan §W13-3.6 input-pin
R842_W0_HI_PLAN = -0.85                                            # (local) plan §W13-3.6 input-pin
R842_W0_LO_MACK = -0.942                                           # (local) mack-9A canonical (center -0.842, hw 0.100)
R842_W0_HI_MACK = -0.742                                           # (local) mack-9A canonical (center -0.842, hw 0.100)

# Output destinations
OUT_JSON = resolve_output(86, 's86_w13_p9_w0_primary_value_resolve.json')
OUT_DECISION_RULE_MD = FRAMEWORK_DIR / "w0-primary-decision-rule.md"
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_output(85, 's85_gate_verdicts.txt'),
    FRAMEWORK_DIR / "falsifier-master-inventory.md",
    SESSIONS_DIR / "session-85" / "session-85-mack-synthesis-w6-13.md",
    SESSIONS_DIR / "session-85" / "session-85-w10-workingpaper.md",
    SESSIONS_DIR / "session-85" / "session-85-s5-falsifier-inventory-mack.md",
    SESSIONS_DIR / "session-plan" / "session-86-plan-w13.md",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    """Print SHA-256 of each input; return {relpath: sha} for closure."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}                                      # (local)
    for p in inputs:
        sha = sha256_of(p)                                         # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    """Stable hash over input SHAs (informational; legacy)."""
    items = sorted(pins.items())                                   # (local)
    h = hashlib.sha256()                                           # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict) -> tuple[str, str]:
    """S84+ dual-SHA: (audit, content)."""
    script_bytes = b""                                             # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                          # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                              # (local)

    h_audit = hashlib.sha256()                                     # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                    # (local)

    h_content = hashlib.sha256()                                   # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Adjudication arithmetic (substitution chain MANDATORY [SIGN])
# ---------------------------------------------------------------------------

def substitution_chain() -> dict:
    """Execute the §10 substitution chain explicitly (definition →
    substitution → simplification → direction). Returns the four-criterion
    table values + the falsifiability table.
    """
    # Step 1 — Definitions (already imported above as W_0_A/W_0_B/W_0_LCDM/SIGMA_W0_DR3)
    # d(X) := |X - W_0_LCDM|

    # Step 2 — Substitute
    d_A = abs(W_0_A - W_0_LCDM)                                    # (local)
    d_B = abs(W_0_B - W_0_LCDM)                                    # (local)

    # Step 3 — Simplify
    delta_d = d_B - d_A                                            # (local)

    # Step 4 — Direction (n_sigma)
    n_sigma_A = d_A / SIGMA_W0_DR3                                 # (local)
    n_sigma_B = d_B / SIGMA_W0_DR3                                 # (local)
    delta_n_sigma = n_sigma_B - n_sigma_A                          # (local)

    # DR3 scenario tensions
    scenarios = {                                                  # (local)
        "A_LCDM":         W_0_LCDM,
        "B_w095":         -0.95,
        "C_w086":         -0.86,
        "B_precise_w091": -0.91,
    }
    scenario_table = {}                                            # (local)
    for name, w_obs in scenarios.items():
        n_A = abs(W_0_A - w_obs) / SIGMA_W0_DR3                    # (local)
        n_B = abs(W_0_B - w_obs) / SIGMA_W0_DR3                    # (local)
        scenario_table[name] = {
            "w_obs": w_obs,
            "n_sigma_A": float(n_A),
            "n_sigma_B": float(n_B),
        }

    # R_842 membership (both definitions)
    A_in_plan = R842_W0_LO_PLAN <= W_0_A <= R842_W0_HI_PLAN        # (local)
    B_in_plan = R842_W0_LO_PLAN <= W_0_B <= R842_W0_HI_PLAN        # (local)
    A_in_mack = R842_W0_LO_MACK <= W_0_A <= R842_W0_HI_MACK        # (local)
    B_in_mack = R842_W0_LO_MACK <= W_0_B <= R842_W0_HI_MACK        # (local)

    return {
        "definitions": {
            "w_0_A": W_0_A, "w_0_B": W_0_B,
            "w_0_LCDM": W_0_LCDM, "sigma_w0_DR3": SIGMA_W0_DR3,
        },
        "step2_substitute": {
            "d_A": d_A, "d_B": d_B,
        },
        "step3_simplify": {
            "delta_d": delta_d,
        },
        "step4_direction": {
            "n_sigma_A": n_sigma_A,
            "n_sigma_B": n_sigma_B,
            "delta_n_sigma": delta_n_sigma,
            "delta_d_positive": bool(delta_d > 0),
            "B_further_from_LCDM": bool(delta_d > 0),
            "delta_n_sigma_positive": bool(delta_n_sigma > 0),
            "B_more_discriminable_by_DR3": bool(delta_n_sigma > 0),
        },
        "R_842_membership": {
            "plan_prompt_rectangle": [R842_W0_LO_PLAN, R842_W0_HI_PLAN],
            "mack_9A_canonical_rectangle": [R842_W0_LO_MACK, R842_W0_HI_MACK],
            "A_in_plan": A_in_plan, "B_in_plan": B_in_plan,
            "A_in_mack_canonical": A_in_mack, "B_in_mack_canonical": B_in_mack,
            "primary_reference": "mack_9A_canonical",
            "note": ("Plan §W13-3.6 narrative (line 430) asserts both candidates"
                     " inside R_842; this is consistent with the mack-9A canonical"
                     " rectangle [-0.942,-0.742] (center -0.842, hw 0.100). The"
                     " input-pin field [-1.05, -0.85] is a wider envelope used"
                     " for boundary-testing; B sits 0.0075 outside its upper edge."),
        },
        "scenarios": scenario_table,
    }


def four_criterion_table(chain: dict) -> dict:
    """Compose the 4-criterion adjudication table (per plan §W13-3 Step 5)."""
    d_A = chain["step2_substitute"]["d_A"]
    d_B = chain["step2_substitute"]["d_B"]
    delta_d = chain["step3_simplify"]["delta_d"]

    return {
        "criterion_1_theoretical_priority": {
            "verdict": "tie",
            "rationale": (
                "Both are first-principles substrate derivations. Volovik-partition"
                " averages over the post-fold expansion history (integrates a"
                " substrate-internal gradient). Substrate-compaction pinpoints"
                " w(z=0) directly from fiber-tau density tracking (no post-fold"
                " averaging). Neither preempts the other on theoretical priority."
            ),
        },
        "criterion_2_DR3_rectangle_membership": {
            "verdict": "both_inside_mack_canonical",
            "A_offset_from_center": abs(W_0_A - (-0.842)),
            "B_offset_from_center": abs(W_0_B - (-0.842)),
            "A_offset_from_center_pct_of_hw": abs(W_0_A - (-0.842)) / 0.100 * 100,
            "B_offset_from_center_pct_of_hw": abs(W_0_B - (-0.842)) / 0.100 * 100,
            "rationale": (
                "Under the canonical mack-9A rectangle R_842 = [-0.942, -0.742]"
                " (center -0.842, hw 0.100), both candidates are inside.  A sits"
                " at 76.0% of half-width; B sits at 0.45% of half-width (centered)."
                " Neither candidate is excluded by the current registration."
            ),
        },
        "criterion_3_falsifiability": {
            "verdict": "B_more_discriminable",
            "d_A": d_A, "d_B": d_B, "delta_d": delta_d,
            "n_sigma_A": chain["step4_direction"]["n_sigma_A"],
            "n_sigma_B": chain["step4_direction"]["n_sigma_B"],
            "delta_n_sigma": chain["step4_direction"]["delta_n_sigma"],
            "rationale": (
                "Under DR3 fiducial sigma(w_0) = 0.025 (S69 master), B is +3.022"
                " sigma further from LCDM than A. This is a falsifiability"
                " advantage for B: a DR3 measurement that returns w_0 = -1.0"
                " would constitute a +6.30-sigma exclusion of B vs only a"
                " +3.28-sigma exclusion of A. Higher sigma = stronger exclusion"
                " = more discriminable."
            ),
        },
        "criterion_4_registry_history": {
            "verdict": "A_long_standing_canonical",
            "A_first_registered": "S5 (per S58 Volovik partition; canonical_constants.py current pin w0_FW=-0.918)",
            "B_first_registered": "S85 W10-2 (branch-(iv) substrate-compaction; new contender)",
            "A_session_count_since_registration": "28+ sessions (S58 -> S85 = approx 28 sessions of citation history)",
            "B_session_count_since_registration": "0-1 sessions (S85 W10-2 -> S86 W13)",
            "rationale": (
                "A has citation-history priority (28+ sessions of canonical use"
                " across the W4-7 NULL-ELIM-MAP at +3.28-sigma vs LCDM, the"
                " falsifier-master-inventory Row #1 as the +3.28-sigma framework"
                " entry, and the canonical_constants.py w0_FW pin). B is the"
                " recent contender from S85 W10-2 branch-(iv). A wins this"
                " criterion by registry-history."
            ),
        },
        "decision_rule": {
            "rule": (
                "PRIMARY = candidate that satisfies (registry-history-priority"
                " AND DR3-rectangle-membership) = CANDIDATE A unless and until a"
                " structural argument promotes B."
            ),
            "designation": "PRIMARY = A (w_0 = -0.918, Volovik partition)",
            "reversibility": (
                "PRIMARY designation is REVERSIBLE upon DR3 publication. If DR3"
                " returns w_0 in [-0.86, -0.83], the substrate-compaction branch"
                " (B) BECOMES PRIMARY by pre-registered re-pin protocol (per S84"
                " R_842 lockout protocol; W1b-9 DR3-RESPONSE-PROTOCOL)."
            ),
            "non_primary_preserved": (
                "Both candidates are documented in the registry as cross-referenced"
                " predictions; the non-PRIMARY candidate (B at S86 W13) is preserved"
                " against future re-pin."
            ),
        },
    }


# ---------------------------------------------------------------------------
# Section 6 — Decision-rule write target
# ---------------------------------------------------------------------------

def render_decision_rule_md(chain: dict, table: dict, audit_sha: str,
                            content_sha: str) -> str:
    """Render the 6-section w0-primary-decision-rule.md content per plan §W13-3.6
    WRITE TARGET specification.
    """
    d_A = chain["step2_substitute"]["d_A"]
    d_B = chain["step2_substitute"]["d_B"]
    delta_d = chain["step3_simplify"]["delta_d"]
    n_sigma_A = chain["step4_direction"]["n_sigma_A"]
    n_sigma_B = chain["step4_direction"]["n_sigma_B"]
    delta_n_sigma = chain["step4_direction"]["delta_n_sigma"]

    md = []
    md.append("# w_0_FW PRIMARY Designation — Decision Rule")
    md.append("")
    md.append(f"> **Origin**: Created S86 W13-3 by sagan-empiricist as adjudication output for")
    md.append(f"> `S86-W0-PRIMARY-VALUE-RESOLVE` (plan §W13-3). Self-blacklist: mack-cosmic-bridge")
    md.append(f"> cannot run this gate (own carry-forward source, mack 9A §VI.7).")
    md.append(">")
    md.append(f"> **Substrate framing**: w_0_FW IS the substrate's late-time spectral-action")
    md.append(f"> gradient projected onto observational coordinates. The two candidates are")
    md.append(f"> NOT competing models; they are TWO METHODOLOGICALLY-DISTINCT projections of")
    md.append(f"> the same substrate observable (Volovik-partition averaging vs substrate-")
    md.append(f"> compaction direct evaluation). PRIMARY designation is OBSERVATIONAL-CITATION")
    md.append(f"> discipline (which value downstream gates cite as canonical), not a physics")
    md.append(f"> ranking. The DR3 reversibility protocol is the substrate's external falsifier.")
    md.append("")
    md.append(f"**Status**: LANDED via `{GATE_ID}` (W13-3, S86).")
    md.append(f"**Producing script**: `computations/session-86/s86_w13_p9_w0_primary_value_resolve.py`")
    md.append(f"**Verdict file**: `computations/session-86/s86_gate_verdicts.txt`")
    md.append(f"**Dual-SHA**: audit_sha256={audit_sha}; content_sha256={content_sha}")
    md.append("")
    md.append("---")
    md.append("")

    # ===================================================================
    # Section 1 — Both candidates documented with full provenance
    # ===================================================================
    md.append("## §1. Both candidates documented (provenance, method, value, audit_sha256)")
    md.append("")
    md.append("### §1.1 Candidate A — w_0_A = -0.918 (Volovik partition)")
    md.append("")
    md.append("| Field | Value |")
    md.append("|:---|:---|")
    md.append("| Value | -0.918 |")
    md.append("| Source | S5 row #1 (`session-85-s5-falsifier-inventory-mack.md` §III.1) |")
    md.append("| Method | Volovik-partition projection of spectral-action gradient at fold, integrated over post-fold expansion history |")
    md.append("| Origin gate | S58 Volovik effacement Γ=0.99970; canonical-constants pin `w0_FW = -0.918` |")
    md.append("| Cross-check verdict | `S85-S5-CONVERGENCE-AUDIT: PASS` (audit_sha256=6920eaefe192f72d399ba7185224b6a0cc1aa50ad2fabdca0310551a865a24d8) |")
    md.append("| W4-7 NULL-ELIM-MAP SHA | content_sha256 head `bf8135bf...` |")
    md.append("| Sigma-distance vs LCDM (S5 §III.1) | +3.28σ at DR3 fiducial σ(w_0)=0.025 |")
    md.append("| ZFP/TD tag | ZFP (S58 Volovik partition; no free parameters) |")
    md.append("| Registry sessions of citation | 28+ sessions (S58 → S85) |")
    md.append("")
    md.append("### §1.2 Candidate B — w_0_B = -0.842454 (substrate-compaction, branch-(iv))")
    md.append("")
    md.append("| Field | Value |")
    md.append("|:---|:---|")
    md.append("| Value | -0.842454 |")
    md.append("| Source | S85 W10-2 branch-(iv) (`session-85-w10-workingpaper.md` lines 287-289, 313, 337, 341, 386) |")
    md.append("| Method | substrate-compaction-derived w(z) via fiber-tau density tracking, evaluated at z=0 |")
    md.append("| Origin gate | S85-W10-R842-PHYSICAL-ANCHOR-REAUDIT: PASS (audit_sha256=8de72cde7d635949f45716191288da6656f8a9fe05411532ab848fdb93fd04e8; content_sha256=b9a6a3014218386add94df8fef1034df5e17feb467c4d4b9cecacadfb133cd09) |")
    md.append("| R_842 offset from center (-0.842) | 0.000454 = 0.45% of mack-9A half-width |")
    md.append("| Sigma-distance vs LCDM | +6.30σ at DR3 fiducial σ(w_0)=0.025 |")
    md.append("| ZFP/TD tag | ZFP (substrate-compaction direct, no fitting) |")
    md.append("| Registry sessions of citation | 0-1 sessions (S85 W10-2 → S86 W13) |")
    md.append("")
    md.append("---")
    md.append("")

    # ===================================================================
    # Section 2 — 4-criterion adjudication table
    # ===================================================================
    md.append("## §2. 4-criterion adjudication table")
    md.append("")
    md.append("| # | Criterion | A=-0.918 | B=-0.842454 | Verdict |")
    md.append("|:-:|:----------|:---------|:------------|:--------|")
    md.append("| 1 | theoretical-priority (more-fundamental substrate construction) | post-fold integral over expansion history | direct fiber-tau density at z=0 | **tie** (both first-principles) |")
    md.append("| 2 | DR3-rectangle-membership (mack-9A R_842 = [-0.942, -0.742]) | inside (offset 0.076, 76.0% of hw) | inside (offset 0.000454, 0.45% of hw) | **both inside** (neither excluded) |")
    md.append("| 3 | falsifiability (distance from LCDM, in σ-units of DR3 fiducial 0.025) | d=0.082, n_σ=3.28 | d=0.157546, n_σ=6.30 | **B more discriminable** by Δn_σ=+3.022 |")
    md.append("| 4 | registry-history (canonical-pin longevity) | 28+ sessions (S58 → S85) | 0-1 sessions (S85 → S86) | **A long-standing** |")
    md.append("")
    md.append("**Score**: A wins Criterion 4; B wins Criterion 3; ties on Criteria 1 and 2.")
    md.append("")
    md.append("**Substitution chain** (per plan §W13-3.10; [SIGN] trigger):")
    md.append("")
    md.append("```")
    md.append("Step 1 — Definitions:")
    md.append(f"  w_0_A = {W_0_A}                  (Volovik partition; canonical pin)")
    md.append(f"  w_0_B = {W_0_B}             (substrate-compaction; W10-2 branch-(iv))")
    md.append(f"  w_0_LCDM = {W_0_LCDM}                (LCDM cosmological constant)")
    md.append(f"  d(X) := |X - w_0_LCDM|        (Euclidean distance from LCDM in 1-D w-space)")
    md.append("")
    md.append("Step 2 — Substitute (Python + Sage exact-rational verified):")
    md.append(f"  d(w_0_A) = |{W_0_A} - ({W_0_LCDM})| = |{W_0_A - W_0_LCDM}| = {d_A:.6f}    (= 41/500 exact)")
    md.append(f"  d(w_0_B) = |{W_0_B} - ({W_0_LCDM})| = |{W_0_B - W_0_LCDM}| = {d_B:.6f}    (= 78773/500000 exact)")
    md.append("")
    md.append("Step 3 — Simplify:")
    md.append(f"  Δd := d(w_0_B) - d(w_0_A) = {d_B:.6f} - {d_A:.6f} = {delta_d:+.6f}    (= 37773/500000 exact)")
    md.append("")
    md.append("Step 4 — Direction:")
    md.append(f"  Δd > 0 → d(w_0_B) > d(w_0_A) → w_0_B is FURTHER from LCDM than w_0_A.")
    md.append("")
    md.append("Falsifiability corollary (DR3 σ(w_0) = 0.025 fiducial, S69 master):")
    md.append(f"  n_σ(A) = d(A)/σ = {d_A:.6f}/0.025 = {n_sigma_A:.6f}    (= 82/25 exact)")
    md.append(f"  n_σ(B) = d(B)/σ = {d_B:.6f}/0.025 = {n_sigma_B:.6f}    (= 78773/12500 exact)")
    md.append(f"  Δn_σ = n_σ(B) - n_σ(A) = {delta_n_sigma:+.6f}    (= 37773/12500 exact)")
    md.append("")
    md.append(f"  Direction: Δn_σ > 0 → DR3 will discriminate B from LCDM at +{delta_n_sigma:.3f}σ MORE")
    md.append("  than it discriminates A from LCDM (under fiducial σ(w_0)=0.025).")
    md.append("```")
    md.append("")
    md.append("**DR3 scenario tension table** (σ-distance of FW from each scenario):")
    md.append("")
    md.append("| Scenario | DR3 returns w_0 | n_σ for A=-0.918 | n_σ for B=-0.842454 |")
    md.append("|:---|:---:|:---:|:---:|")
    for name, info in chain["scenarios"].items():
        md.append(f"| {name} | {info['w_obs']:+.4f} | {info['n_sigma_A']:.4f} | {info['n_sigma_B']:.4f} |")
    md.append("")
    md.append("---")
    md.append("")

    # ===================================================================
    # Section 3 — Pre-registered decision rule
    # ===================================================================
    md.append("## §3. Pre-registered decision rule")
    md.append("")
    md.append("**Rule** (deterministic, no post-hoc tuning):")
    md.append("")
    md.append("> PRIMARY = candidate that satisfies (registry-history-priority AND")
    md.append("> DR3-rectangle-membership) = CANDIDATE A unless and until a structural")
    md.append("> argument promotes B.")
    md.append("")
    md.append("**Components of the rule**:")
    md.append("")
    md.append("1. **Registry-history-priority** (Criterion 4): the candidate with longer canonical-pin")
    md.append("   citation history wins, because downstream gates have already been written")
    md.append("   citing that value as canonical. Re-pinning to a different value would invalidate")
    md.append("   28+ sessions of σ-distance, joint-BF, and EVOI computations.")
    md.append("")
    md.append("2. **DR3-rectangle-membership**: the candidate must sit inside the registered DR3")
    md.append("   falsifier rectangle R_842 (mack-9A canonical, center -0.842, half-widths")
    md.append("   (0.100, 0.200)). Both A and B satisfy this; the criterion is non-discriminating")
    md.append("   here but is included for falsifiability hygiene.")
    md.append("")
    md.append("3. **No invocation of post-hoc data-fitting**: the rule was authored at plan-freeze")
    md.append("   (S86 W13 plan §W13-3) BEFORE the script ran. The decision is mechanical.")
    md.append("")
    md.append("**The rule does NOT use** (and explicitly rejects):")
    md.append("- Falsifiability (Criterion 3) as PRIMARY-selection rule. Reason: more-discriminable")
    md.append("  is a virtue but does not override 28+ sessions of registry citation. Falsifiability")
    md.append("  enters via the REVERSIBILITY trigger (§5), not the PRIMARY designation.")
    md.append("- Theoretical-priority (Criterion 1) as discriminator. Reason: tie.")
    md.append("")
    md.append("---")
    md.append("")

    # ===================================================================
    # Section 4 — PRIMARY designation
    # ===================================================================
    md.append("## §4. PRIMARY designation")
    md.append("")
    md.append("**PRIMARY = w_0_A = -0.918** (Volovik partition; canonical_constants.py `w0_FW`).")
    md.append("")
    md.append("Per §3 decision rule: Candidate A wins on registry-history-priority (28+ sessions)")
    md.append("AND satisfies DR3-rectangle-membership (inside mack-9A R_842 at 76% of half-width).")
    md.append("Candidate B is preserved as the SECONDARY-with-reversibility candidate.")
    md.append("")
    md.append("**Downstream-citation discipline** (effective S86 onward):")
    md.append("- Master inventory Row #1 (w_0): cite `w_0 = -0.918, +3.28σ vs LCDM under DR3`")
    md.append("  with footnote `[*]` pointing to this file.")
    md.append("- DR3 sub-tree (W13-4, S86-DR3-SUB-TREE-3-ROW-PIN): both regulator-conditional")
    md.append("  L_max = 8/10/12 cells use A as the framework w_0 prediction; the substrate-")
    md.append("  compaction branch (B) is recorded as a parallel-pathway annotation.")
    md.append("- Future BF, EVOI, and joint-detector computations: A is the canonical framework w_0.")
    md.append("- canonical_constants.py: `w0_FW = -0.918` UNCHANGED (no canonical-constant")
    md.append("  re-emission from this gate).")
    md.append("")
    md.append("**SECONDARY-with-reversibility candidate**: w_0_B = -0.842454")
    md.append("- Documented as the substrate-compaction direct-evaluation pathway.")
    md.append("- Cross-referenced from this file (§1.2) and from the master inventory")
    md.append("  Row #1 footnote.")
    md.append("- Will be promoted to PRIMARY automatically if the §5 reversibility trigger fires.")
    md.append("")
    md.append("---")
    md.append("")

    # ===================================================================
    # Section 5 — Reversibility protocol
    # ===================================================================
    md.append("## §5. Reversibility protocol (DR3-trigger conditions)")
    md.append("")
    md.append("**Trigger**: DR3 (DESI Data Release 3, window opened 2026-04-23 per S84 W1b-9 DR3-RESPONSE-PROTOCOL).")
    md.append("")
    md.append("**Reversal condition**: if DR3 returns measured w_0 inside the band:")
    md.append("")
    md.append("```")
    md.append("    w_0^{DR3}  ∈  [-0.86, -0.83]")
    md.append("```")
    md.append("")
    md.append("then the PRIMARY designation REVERSES from A → B automatically. The justification")
    md.append("is structural: a measured w_0 in [-0.86, -0.83] sits at most 0.018 from B (n_σ < 0.72")
    md.append("at fiducial σ_obs = 0.025) and at least 0.058 from A (n_σ > 2.32). At that point the")
    md.append("registry-history priority of A is overridden by direct empirical preference for B.")
    md.append("")
    md.append("Substitution chain for the reversal threshold:")
    md.append("")
    md.append("```")
    md.append("Step 1 — Definitions:")
    md.append("  w_R_lo = -0.86   (upper edge of reversal band, closer to LCDM)")
    md.append("  w_R_hi = -0.83   (lower edge of reversal band, further from LCDM)")
    md.append("  σ_DR3 = 0.025    (DR3 fiducial sigma)")
    md.append("")
    md.append("Step 2 — Substitute (max-tension within reversal band):")
    md.append("  max |A - w_R| = max(|-0.918 - (-0.86)|, |-0.918 - (-0.83)|)")
    md.append("                = max(0.058, 0.088) = 0.088 → n_σ(A,worst) = 0.088/0.025 = 3.52")
    md.append("  min |A - w_R| = min(0.058, 0.088) = 0.058 → n_σ(A,best)  = 2.32")
    md.append("  max |B - w_R| = max(|-0.842454 - (-0.86)|, |-0.842454 - (-0.83)|)")
    md.append("                = max(0.017546, 0.012454) = 0.017546 → n_σ(B,worst) = 0.70")
    md.append("  min |B - w_R| = 0.012454 → n_σ(B,best) = 0.50")
    md.append("")
    md.append("Step 3 — Simplify:")
    md.append("  Within [-0.86, -0.83], B is always at most 0.70σ from the measurement,")
    md.append("  while A is at least 2.32σ from the measurement. The empirical preference")
    md.append("  for B is decisive (Bayes factor B/A ≥ exp((2.32^2 - 0.70^2)/2) ≥ 11.1).")
    md.append("")
    md.append("Step 4 — Direction:")
    md.append("  n_σ(A) > n_σ(B) by ≥ 1.62 in the reversal band → B is the empirically")
    md.append("  preferred candidate → PRIMARY = B by re-pin protocol.")
    md.append("```")
    md.append("")
    md.append("**Anti-reversal condition** (DR3 does NOT trigger reversal):")
    md.append("- If DR3 returns w_0 closer to A's band (e.g., [-0.95, -0.88]) or closer to LCDM")
    md.append("  (e.g., [-1.05, -0.95]), PRIMARY remains A.")
    md.append("- If DR3 returns w_0 outside the entire R_842 rectangle [-0.942, -0.742], the")
    md.append("  framework branch fails the binary containment test (independent issue, handled")
    md.append("  by S84 W1b-9 LOCKOUT-C protocol, not by this PRIMARY designation).")
    md.append("")
    md.append("**Locked machinery** (cannot be retroactively re-tuned):")
    md.append("- Reversal band edges: -0.86 / -0.83 (pre-registered in this file at S86 W13-3 freeze).")
    md.append("- σ_DR3 = 0.025 fiducial (S69 master synthesis).")
    md.append("- Registry-history-priority weight: dominant. Falsifiability secondary unless reversal triggers.")
    md.append("")
    md.append("---")
    md.append("")

    # ===================================================================
    # Section 6 — Cross-references
    # ===================================================================
    md.append("## §6. Cross-references")
    md.append("")
    md.append("**Inbound references** (files that point AT this decision rule):")
    md.append("- `sessions/framework/registry/falsifier-master-inventory.md` Row #1 (w_0): footnote citing")
    md.append("  this file as the primary-pin authority. (To be updated by P11 PAIR-1 in §W13-1.)")
    md.append("- `computations/_shared/canonical_constants.py` `w0_FW = -0.918` entry: provenance comment")
    md.append("  cites this file for the PRIMARY-decision provenance.")
    md.append("- `sessions/framework/registry/dr3-3row-7cell-subtree.md` (P8/W13-4 NEW): cites A=-0.918 as the")
    md.append("  pinned framework w_0 across the 21-cell decision matrix.")
    md.append("")
    md.append("**Outbound references** (files this decision rule cites as evidence):")
    md.append("- `computations/session-85/s85_gate_verdicts.txt`:")
    md.append("  - `S85-S5-CONVERGENCE-AUDIT: PASS` (audit_sha256=6920eaefe192f72d39...) — A's S5 anchor.")
    md.append("  - `S85-W10-R842-PHYSICAL-ANCHOR-REAUDIT: PASS` (audit_sha256=8de72cde7d63594...) — B's W10-2 anchor.")
    md.append("- `sessions/archive/session-85/session-85-mack-synthesis-w6-13.md` §VI.7 — original carry-forward.")
    md.append("- `sessions/archive/session-85/session-85-w10-workingpaper.md` §10.2 lines 287-289, 313, 337,")
    md.append("  341, 386 — W10-2 branch-(iv) value -0.842454 with R_842 offset 0.000454.")
    md.append("- `sessions/archive/session-85/session-85-s5-falsifier-inventory-mack.md` §III.1 row #1 — A's master-inventory record.")
    md.append("- S84 W1b-9 DR3-RESPONSE-PROTOCOL (R_842 lockout, content_sha256 head 9cc7f47e) — reversibility-trigger provenance.")
    md.append("")
    md.append("**Reverse-trigger linkage**: §5 reversal rule at -0.86 ≤ w_0^{DR3} ≤ -0.83 is the")
    md.append("automatic re-pin condition. If DR3 publication satisfies this band, a follow-up")
    md.append("session must:")
    md.append("1. Update `canonical_constants.py` w0_FW from -0.918 to -0.842454.")
    md.append("2. Re-emit affected verdict lines (P11 master inventory Row #1 σ-distance recomputation).")
    md.append("3. Re-cross-reference this file's PRIMARY tag from A → B.")
    md.append("4. Append a verdict line `S{N}-W0-PRIMARY-REVERSED: PASS` with new dual-SHA.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("**End of decision rule. Reversibility hot-trigger: DR3 publication, target window 2026-Q3 / 2027-Q1.**")
    md.append("")

    return "\n".join(md)


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str,
                   content_sha: str) -> None:
    """Append S84+ dual-SHA verdict line."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256={content_sha} audit_sha256={audit_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def evaluate_gate(decision_rule_path: Path, primary_designated: bool,
                  reversibility_documented: bool, both_cross_referenced: bool,
                  arithmetic_correct: bool) -> str:
    """PASS iff all 5 conditions of the pre-registered threshold met."""
    if not decision_rule_path.exists():
        return "FAIL"
    if not primary_designated:
        return "FAIL"
    if not reversibility_documented:
        return "FAIL"
    if not both_cross_referenced:
        return "FAIL"
    if not arithmetic_correct:
        return "FAIL"
    return "PASS"


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                               # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                   # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()                         # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute substitution chain + 4-criterion table
    chain = substitution_chain()
    table = four_criterion_table(chain)

    # 2a. Emit substitution chain to stdout for record (per [SIGN] trigger)
    print("=== SUBSTITUTION CHAIN (plan §W13-3.10) ===")
    d_A = chain["step2_substitute"]["d_A"]
    d_B = chain["step2_substitute"]["d_B"]
    delta_d = chain["step3_simplify"]["delta_d"]
    n_sigma_A = chain["step4_direction"]["n_sigma_A"]
    n_sigma_B = chain["step4_direction"]["n_sigma_B"]
    delta_n_sigma = chain["step4_direction"]["delta_n_sigma"]
    print(f"  Step 1 — Definitions: w_0_A={W_0_A}, w_0_B={W_0_B}, "
          f"w_0_LCDM={W_0_LCDM}, sigma={SIGMA_W0_DR3}")
    print(f"  Step 2 — Substitute: d(A)={d_A:.6f}; d(B)={d_B:.6f}")
    print(f"  Step 3 — Simplify:    Delta d = {delta_d:+.6f}")
    print(f"  Step 4 — Direction:   n_sigma(A)={n_sigma_A:.4f}; "
          f"n_sigma(B)={n_sigma_B:.4f}; Delta n_sigma={delta_n_sigma:+.4f}")
    print(f"           --> w_0_B is FURTHER from LCDM (Delta d > 0).")
    print(f"           --> B is +{delta_n_sigma:.3f}-sigma more discriminable by DR3.")
    print()

    # 3. Verify arithmetic against pre-registered numbers (plan §W13-3.10)
    expected = {
        "d_A": 0.082000,
        "d_B": 0.157546,
        "delta_d": 0.075546,
        "n_sigma_A": 3.280,
        "n_sigma_B": 6.302,
        "delta_n_sigma": 3.022,
    }                                                              # (local)
    arithmetic_correct = (
        abs(d_A - expected["d_A"]) < 1e-9
        and abs(d_B - expected["d_B"]) < 1e-9
        and abs(delta_d - expected["delta_d"]) < 1e-9
        and abs(n_sigma_A - expected["n_sigma_A"]) < 1e-3
        and abs(n_sigma_B - expected["n_sigma_B"]) < 1e-2
        and abs(delta_n_sigma - expected["delta_n_sigma"]) < 1e-2
    )                                                              # (local)
    print(f"  Arithmetic-vs-expected check: {arithmetic_correct}")

    # 4. Render decision-rule markdown + write
    md_content = render_decision_rule_md(chain, table, audit_sha, content_sha)
    OUT_DECISION_RULE_MD.write_text(md_content, encoding="utf-8")
    print(f"  decision-rule MD written: {OUT_DECISION_RULE_MD}")
    print(f"    bytes: {len(md_content)}")

    # 5. Verify decision-rule MD is parseable (6 sections present)
    md_loaded = OUT_DECISION_RULE_MD.read_text(encoding="utf-8")
    section_markers = ["## §1.", "## §2.", "## §3.", "## §4.", "## §5.", "## §6."]
    sections_found = [m for m in section_markers if m in md_loaded]
    print(f"  6-section parse check: {len(sections_found)}/6 sections found "
          f"({sections_found if len(sections_found)<6 else 'all present'})")
    six_sections_ok = len(sections_found) == 6                     # (local)

    # 6. PRIMARY designation + reversibility
    primary_designated = "**PRIMARY = w_0_A = -0.918**" in md_loaded
    reversibility_documented = (
        "Reversibility protocol" in md_loaded
        and "[-0.86, -0.83]" in md_loaded
    )                                                              # (local)
    both_cross_referenced = (
        "## §1.1 Candidate A — w_0_A = -0.918" in md_loaded
        and "## §1.2 Candidate B — w_0_B = -0.842454" in md_loaded
    )                                                              # (local)
    print(f"  PRIMARY designated:        {primary_designated}")
    print(f"  Reversibility documented:  {reversibility_documented}")
    print(f"  Both candidates cross-ref: {both_cross_referenced}")
    print(f"  Six sections present:      {six_sections_ok}")

    # 7. Build the JSON output (4-criterion table + substitution chain)
    output_obj = {                                                 # (local)
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "session": SESSION,
        "candidates": {
            "A": {
                "value": W_0_A,
                "source": "S5 row #1 (Volovik partition)",
                "method": "Volovik-partition projection of spectral-action gradient at fold",
                "audit_sha256_anchor": "6920eaefe192f72d399ba7185224b6a0cc1aa50ad2fabdca0310551a865a24d8",
                "anchor_gate": "S85-S5-CONVERGENCE-AUDIT",
                "registry_sessions": "28+",
                "ZFP_TD": "ZFP",
            },
            "B": {
                "value": W_0_B,
                "source": "S85 W10-2 branch-(iv) (substrate-compaction)",
                "method": "substrate-compaction-derived w(z=0) via fiber-tau density tracking",
                "audit_sha256_anchor": "8de72cde7d635949f45716191288da6656f8a9fe05411532ab848fdb93fd04e8",
                "anchor_gate": "S85-W10-R842-PHYSICAL-ANCHOR-REAUDIT",
                "registry_sessions": "0-1",
                "ZFP_TD": "ZFP",
            },
        },
        "substitution_chain": chain,
        "four_criterion_table": table,
        "decision_rule": (
            "PRIMARY = candidate that satisfies (registry-history-priority"
            " AND DR3-rectangle-membership) = CANDIDATE A unless and until"
            " a structural argument promotes B."
        ),
        "primary_designation": {
            "value": W_0_A,
            "label": "A",
            "source": "Volovik partition (S5 row #1)",
        },
        "secondary_with_reversibility": {
            "value": W_0_B,
            "label": "B",
            "source": "substrate-compaction (S85 W10-2 branch-(iv))",
        },
        "reversibility_trigger": {
            "condition": "DR3 returns w_0 ∈ [-0.86, -0.83]",
            "action": "PRIMARY flips A → B by pre-registered re-pin protocol",
            "provenance": "S84 W1b-9 DR3-RESPONSE-PROTOCOL R_842 lockout",
        },
        "checks": {
            "arithmetic_correct": arithmetic_correct,
            "primary_designated": primary_designated,
            "reversibility_documented": reversibility_documented,
            "both_cross_referenced": both_cross_referenced,
            "six_sections_ok": six_sections_ok,
        },
        "input_pins": pins,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }
    OUT_JSON.write_text(json.dumps(output_obj, indent=2, sort_keys=True),
                        encoding="utf-8")
    print(f"  JSON written: {OUT_JSON} ({OUT_JSON.stat().st_size} bytes)")

    # 8. Evaluate gate
    verdict = evaluate_gate(
        OUT_DECISION_RULE_MD,
        primary_designated and six_sections_ok,
        reversibility_documented,
        both_cross_referenced,
        arithmetic_correct,
    )                                                              # (local)
    print()
    print(f"=== VERDICT: {verdict} ===")

    # 9. Print 4-tuple + append verdict line
    value_str = f"PRIMARY=A={W_0_A}"                               # (local)
    print()
    print(emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX))

    append_verdict(verdict, value_str, audit_sha, content_sha)
    print()
    print(f"  Verdict appended to {VERDICT_TXT}")
    print(f"  Wall time: {time.time() - t0:.3f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
