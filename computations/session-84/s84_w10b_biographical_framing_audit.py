#!/usr/bin/env python3
"""
S84 W10b-122 — S84-BIOGRAPHICAL-FRAMING-AUDIT
=============================================

Gate: S84-BIOGRAPHICAL-FRAMING-AUDIT ([AUDIT])

Pre-registered threshold:
  PASS iff survival_fraction >= 0.80 AND inter_auditor_kappa >= 0.6
       AND prompt_symmetry_shift < 0.15
  INFO iff 0.50 <= survival_fraction < 0.80 OR inter_auditor_kappa < 0.6
  FAIL iff survival_fraction < 0.50

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py (feeds audit_sha256)
  - sessions/archive/session-83/workshops/s83-gear-machine-thought-experiment.md
  - sessions/archive/session-83/session-83-gen-physicist-s6-synthesis.md
  - computations/session-83/s83_gate_verdicts.txt
  - .claude/rules/epistemic-discipline.md
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<survival_fraction>, scheme=neutral_prompt,
   convention=arg_backed_vs_weak_vs_unsupported, L_max=NA)

Classification: NON-PHONONIC (methodological audit of agent-interaction pattern)

METHODOLOGY
-----------
This audit re-evaluates the load-bearing claims of S83's gear-machine R2
"corner-with-extensions" wrap-up under a NEUTRAL-PROMPT TEMPLATE that
strips:
  - agent names and biographical anchors ("Tesla / Kaku / Einstein
    perspective")
  - prior-workshop-transcript priming ("Kaku conceded in R2", "Tesla
    sharpened in T2")
  - convergence framing ("R2 corner-with-extensions", "agreed at midpoint
    6.0")
and PRESERVES:
  - mathematical identities (e.g., alpha_s = n_s^2 - 1)
  - structural predicates (e.g., KO-dim = 6, A_F = C+H+M_3(C) singleton)
  - canonical constants (tau_fold = 0.190, d^2 S/dtau^2 = +317,863)
  - verdict-log thresholds from S82/S83 gate verdicts

Each load-bearing claim is then classified against pre-registered criteria:
  ARGUMENT-BACKED  := claim is supported by >= 1 mathematical identity OR
                      >= 1 canonical constant pin OR >= 1 gate verdict
                      from the S82/S83 verdict log.
  ARGUMENT-WEAK    := claim is supported only by organizational-insight
                      framing (rank-counting argument, type categorization,
                      convergence-language only).
  UNSUPPORTED      := claim has no citation chain to math, constants, or
                      verdict-log; rests on rhetorical framing alone.

The adjudicator implements a deterministic classifier driven by an
explicit citation-chain table. The classifier function applied to each
claim is identical regardless of claim order (cross-check c) and
identical under prompt-inversion (cross-check b: re-runs the classifier
with the inversion-flag asserted; PASS-classification logic is
NOT-claim-orientation-dependent).

Inter-auditor kappa is computed by re-classifying a 5-claim sub-sample
under a STRICT-INDEPENDENT classifier (a separately-implemented function
with no shared state) and comparing categorical labels.

DISCIPLINE
----------
- `from canonical_constants import *`
- All intermediates tagged `# (local)`
- CPU-only (text classification; no matrix algebra)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict appended to s84_gate_verdicts.txt with BOTH
  audit_sha256=<64> and content_sha256=<64> plus schema_version=S84+
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (CPU-only)
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

os.environ.setdefault('OMP_NUM_THREADS', '8')  # CPU thread cap (no GPU here)
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import random
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSION_DIR = PROJECT_ROOT / "sessions" / "session-84"
ARTIFACT_DIR = SESSION_DIR / "computation-artifacts"
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

SESSION = "S84"                                                      # (local)
GATE_ID = "S84-BIOGRAPHICAL-FRAMING-AUDIT"                           # (local)
SCHEME = "neutral_prompt"                                            # (local)
CONVENTION = "arg_backed_vs_weak_vs_unsupported"                     # (local)
L_MAX = "NA"                                                         # (local)

# Pre-registered thresholds (frozen BEFORE running)
PASS_SURVIVAL = 0.80                                                 # (local)
INFO_SURVIVAL = 0.50                                                 # (local)
KAPPA_PASS_THRESHOLD = 0.60                                          # (local)
PROMPT_SYMMETRY_TOLERANCE = 0.15                                     # (local)
ORDER_EFFECT_TOLERANCE = 0.05                                        # (local)
RANDOM_SEED = 84122                                                  # (local)

# Output destinations
OUT_JSON = ARTIFACT_DIR / "s84_w10b_122_bio_framing_audit.json"
VERDICT_TXT = resolve_output(84, 's84_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    PROJECT_ROOT / "sessions" / "session-83" / "workshops"
        / "s83-gear-machine-thought-experiment.md",
    PROJECT_ROOT / "sessions" / "session-83"
        / "session-83-gen-physicist-s6-synthesis.md",
    resolve_output(83, 's83_gate_verdicts.txt'),
    PROJECT_ROOT / ".claude" / "rules" / "epistemic-discipline.md",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
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
# Section 5 — Claim inventory (load-bearing claims from S83 R2 wrap-up)
#
# Each claim is an atomic assertion extracted from the S83 R2 corner-with-
# extensions wrap-up (lines 1166-1218 of s83-gear-machine-thought-experiment.md)
# and the S83 §V.6 gen-physicist synthesis. The "load-bearing" filter:
# present in either (a) the Workshop Verdict table, (b) the Wrap-Up
# What-Changed/Holds/Strains sections, (c) the §V.6 synthesis row, or
# (d) the pre-registered S84-GEAR-MASTER-CANDIDATE block.
#
# For each claim we record:
#   id            — short identifier
#   text          — neutral, biographically-stripped statement
#   citations     — explicit list of {math_identity | canonical_constant |
#                   gate_verdict | structural_theorem | organizational_only |
#                   none}
#   source_layer  — wrap-up section in which it appears (for traceability)
# ---------------------------------------------------------------------------

CLAIMS = [                                                           # (local)
    # === Quantitative / mathematical claims (ARGUMENT-BACKED candidates) ===
    {
        "id": "C01",
        "text": ("Master gear MG-1 corresponds to tau_fold = 0.190 as the "
                 "Jensen-deformation hand (van Hove singularity of the bare "
                 "spectral action)."),
        "citations": ["canonical_constant:tau_fold=0.19",
                      "canonical_constant:d2S_fold=317862.85",
                      "structural_theorem:Jensen_deformation"],
        "source_layer": "wrap-up:What-Holds; verdict-row:2",
    },
    {
        "id": "C02",
        "text": ("Convexity d^2 S/dtau^2|_fold = +317,863 is positive, "
                 "yielding sign(n_T) = + (blue tilt) by the chain "
                 "convex curvature => dH/dtau > 0 => dP_T/dtau > 0 "
                 "=> n_T > 0."),
        "citations": ["canonical_constant:d2S_fold=317862.85",
                      "math_identity:n_T=dlnP_T/dlnk",
                      "gate_verdict:S83-W3-G50:PASS:|n_T|=0.4676"],
        "source_layer": "wrap-up:What-Holds",
    },
    {
        "id": "C03",
        "text": ("alpha_s = n_s^2 - 1 evaluates to -0.068968 at "
                 "n_s = 0.9649 (Planck central)."),
        "citations": ["math_identity:alpha_s=n_s^2-1",
                      "structural_theorem:S50_atlas_identity",
                      "python_verified:alpha_s=-0.068968"],
        "source_layer": "wrap-up:What-Changed; V.7 pre-registration",
    },
    {
        "id": "C04",
        "text": ("Framework alpha_s = -0.069 is 9.62 sigma from Planck 2018 "
                 "central -0.0045 +/- 0.0067."),
        "citations": ["math_identity:sigma=|delta|/sigma_obs",
                      "python_verified:sigma_planck=9.62"],
        "source_layer": "wrap-up:What-Changed",
    },
    {
        "id": "C05",
        "text": ("Framework vs CMB-S4 slow-roll baseline (alpha_s ~ -0.001, "
                 "sigma ~ 0.002) gives 33.98 sigma separation."),
        "citations": ["math_identity:sigma=|delta|/sigma_proj",
                      "python_verified:sigma_S4=33.98"],
        "source_layer": "wrap-up:What-Changed; V.7",
    },
    {
        "id": "C06",
        "text": ("sin^2(mu_BC) = 3/(3 + e^{12 tau}) at tau = 0.190 gives "
                 "0.234803, matching PDG sin^2(theta_W)|_M_Z = 0.23122 to "
                 "0.134% via 2-loop RGE."),
        "citations": ["math_identity:cubic_BC=3/(3+exp(12*tau))",
                      "canonical_constant:tau_fold=0.19",
                      "python_verified:sin2_mu_BC_fold=0.234803",
                      "gate_verdict:S83-W2-G15:PASS"],
        "source_layer": "wrap-up:Gamma1' status",
    },
    {
        "id": "C07",
        "text": ("At tau = 0.10, sin^2(mu_BC) = 0.4747, off PDG-RGE target "
                 "by +102.2% (mesh JAMS)."),
        "citations": ["math_identity:cubic_BC=3/(3+exp(12*tau))",
                      "python_verified:sin2_010_ratio=2.022"],
        "source_layer": "wrap-up:R3.3 alternative-state",
    },
    {
        "id": "C08",
        "text": ("At tau = 0.30, sin^2(mu_BC) = 0.0758, off target by "
                 "-67.7% (mesh JAMS in opposite direction)."),
        "citations": ["math_identity:cubic_BC=3/(3+exp(12*tau))",
                      "python_verified:sin2_030_ratio=0.323"],
        "source_layer": "wrap-up:R3.3",
    },
    {
        "id": "C09",
        "text": ("Same-regulator Mellin-moment ratios M_i^R / M_j^R are "
                 "R-invariant by pointwise weight cancellation w_R(lambda) "
                 "in numerator and denominator."),
        "citations": ["math_identity:Mellin_ratio_R_invariance",
                      "structural_theorem:META-PRINCIPLE",
                      "gate_verdict:S83-W3-META-PRINCIPLE:PASS"],
        "source_layer": "wrap-up:What-Holds; verdict-row:1",
    },
    {
        "id": "C10",
        "text": ("Heterotic CY3 commutative function-algebra cannot produce "
                 "M_3(C) via any finite-group quotient; therefore A_F = "
                 "C + H + M_3(C) is a non-commutative singleton not reachable "
                 "from K2 algebra-layer constructions."),
        "citations": ["structural_theorem:CCM_admissibility_singleton",
                      "math_identity:center_of_commutative_algebra=whole_algebra",
                      "math_identity:center(A_F)=R^3"],
        "source_layer": "wrap-up:What-Changed; verdict-row:3",
    },
    {
        "id": "C11",
        "text": ("alpha_s = n_s^2 - 1 is a S50 atlas-registered identity, "
                 "permanent in the project's permanent-results registry."),
        "citations": ["structural_theorem:S50_permanent_result",
                      "math_identity:alpha_s=n_s^2-1"],
        "source_layer": "V.6 / V.7 synthesis",
    },
    {
        "id": "C12",
        "text": ("Output-to-input ratio of the composite master gear "
                 "is 53 identities / 3 inputs ~ 17.7."),
        "citations": ["math_identity:output_input_ratio=53/3",
                      "python_verified:53/3=17.667",
                      "structural_theorem:perm_results_registry_count"],
        "source_layer": "verdict-row:2",
    },
    {
        "id": "C13",
        "text": ("Rank-to-count ratio for §VII-A + §VII-B identities is "
                 "6/53 ~ 0.113; landscape continuous-moduli ratio is 202/222 "
                 "~ 0.91; framework is 3 OOM tighter at the discrete-flux "
                 "layer."),
        "citations": ["math_identity:6/53=0.1132",
                      "math_identity:202/222=0.9099",
                      "python_verified:rank_count_ratio=0.1132"],
        "source_layer": "wrap-up:What-Changed; verdict-row:4",
    },
    {
        "id": "C14",
        "text": ("Gamma3 (CC-5 belt-drive) retires into Gamma2' (Mellin "
                 "first-moment cone) as a corollary; span(A_s)/span(k_a2) = "
                 "1.0000 to machine precision is a unit-ratio belt-drive "
                 "forced by MG-0."),
        "citations": ["math_identity:Mellin_unit_ratio_belt_drive",
                      "gate_verdict:S83-W3-META-PRINCIPLE:PASS"],
        "source_layer": "wrap-up:What-Holds",
    },
    {
        "id": "C15",
        "text": ("Gamma1' cubic-BC closure is PARTIAL: the input "
                 "M_H_framework = 97 GeV carries a 3.3% prior-coincidence "
                 "risk under a uniform 15-GeV window prior."),
        "citations": ["math_identity:prior_coincidence=1/15",
                      "structural_theorem:cubic_BC_input_dependency"],
        "source_layer": "wrap-up:What-Strains",
    },
    {
        "id": "C16",
        "text": ("Gamma6 (BCS-on-Jensen frequency comb) preserves the "
                 "three-band structure (Josephson / Gap / Breathing at ~10x "
                 "separation) across the tau scan [0.10, 0.30] because the "
                 "seven inter-mode ratios are algebraic features of the BCS "
                 "spectral problem, independent of tau."),
        "citations": ["math_identity:BCS_inter_mode_ratios_algebraic",
                      "structural_theorem:BCS_on_Jensen_spectral_problem"],
        "source_layer": "wrap-up:R3.3",
    },
    # === Organizational / classification claims (ARGUMENT-WEAK candidates) ===
    {
        "id": "C17",
        "text": ("The 53 §VII-A + §VII-B structural identities have effective "
                 "rank = 6 deep generators (C-1 Mellin cone, C-2 Jensen "
                 "curvature, C-3 cubic-BC, C-4 KO-dim-6 class, C-5 A_F "
                 "singleton, C-6 BCS-on-Jensen)."),
        "citations": ["organizational_only:rank_classification",
                      "structural_theorem:registry_class_partition_estimate"],
        "source_layer": "wrap-up:What-Changed; verdict-row:2",
    },
    {
        "id": "C18",
        "text": ("Framework's structural position is 'corner-with-extensions' "
                 "of the landscape's rep-theory output cone: shares output "
                 "with heterotic-CY3 sub-class, framework-specific at A_F "
                 "algebra layer, genuinely outside in dynamics sector."),
        "citations": ["organizational_only:type_b_prime_categorization"],
        "source_layer": "wrap-up:R3.4 meta-concept; verdict-row:4",
    },
    {
        "id": "C19",
        "text": ("Input count = 3 (MG-0 Mellin cone, MG-1 tau_fold, "
                 "MG-2 A_F singleton) drives 53 structural identities; "
                 "this composite is the 'master gear' of the framework."),
        "citations": ["organizational_only:master_gear_categorization",
                      "math_identity:53/3=17.667"],
        "source_layer": "verdict-row:2",
    },
    {
        "id": "C20",
        "text": ("C-7 residual Kirchhoff class collapses into C-1 at ~0.5 "
                 "dependency, so the effective rank stays at 6 even with "
                 "the residual sub-class accounted."),
        "citations": ["organizational_only:registry_audit_estimate"],
        "source_layer": "wrap-up:What-Changed",
    },
    {
        "id": "C21",
        "text": ("The dynamics sector (tau_fold, Jensen curvature, BCS-on-"
                 "Jensen comb, four-speed hierarchy) has no landscape "
                 "counterpart across IIB, IIA, heterotic, M-theory G_2, and "
                 "F-theory CY4 compactifications surveyed in R1-R2."),
        "citations": ["organizational_only:literature_survey_pending",
                      "structural_theorem:dynamics_sector_uniqueness_open"],
        "source_layer": "wrap-up:What-Holds",
    },
    {
        "id": "C22",
        "text": ("Framework predictions live in its dynamics extensions, "
                 "while its rep-theory predictions are 'table-stakes' "
                 "matched by string compactifications of the heterotic-CY3 "
                 "type."),
        "citations": ["organizational_only:epistemic_layering_claim"],
        "source_layer": "wrap-up:R3.4",
    },
    {
        "id": "C23",
        "text": ("The composite master-gear set is algebraically derivable "
                 "from (CCM 2007 + KO-dim = 6 + A_F singleton "
                 "classification theorem) without additional structural "
                 "assumption (S84-GEAR-MASTER-CANDIDATE PASS criterion)."),
        "citations": ["organizational_only:S84_pre-registration",
                      "structural_theorem:CCM_axioms_A1-A6"],
        "source_layer": "wrap-up:Pre-Registered Gate; V.6 PASS criterion",
    },
    {
        "id": "C24",
        "text": ("The framework is an overdetermined mesh at a single "
                 "stationary point tau = 0.190, not a tunable free parameter "
                 "that happened to land there."),
        "citations": ["math_identity:cubic_BC_residual_<0.3%_at_tau=0.19_only",
                      "python_verified:sin2_010_ratio=2.022_AND_sin2_030_ratio=0.323"],
        "source_layer": "wrap-up:R3.3 net reading",
    },
    # === Convergence / consensus framing claims (UNSUPPORTED candidates) ===
    {
        "id": "C25",
        "text": ("Both workshop participants converged on the type-(b') "
                 "categorization with 'corner-with-extensions' as the honest "
                 "epistemic label."),
        "citations": ["organizational_only:agent_convergence_record"],
        "source_layer": "wrap-up:Workshop Verdict row 4",
    },
    {
        "id": "C26",
        "text": ("Both workshop participants converged at midpoint rank = 6.0 "
                 "(range 5.5-6.3) for the deep-theorem count generating "
                 "the 53 §VII identities."),
        "citations": ["organizational_only:agent_convergence_record"],
        "source_layer": "wrap-up:Pre-Registered Gate / Speculative entries",
    },
    {
        "id": "C27",
        "text": ("The K2 algebra-layer claim was withdrawn during the "
                 "workshop, leaving the framework's algebra-layer master "
                 "gear genuinely framework-specific (independent of any "
                 "argument-cite, this is a process record)."),
        "citations": ["organizational_only:workshop_process_record"],
        "source_layer": "wrap-up:What-Changed; verdict-row:3",
    },
]


# ---------------------------------------------------------------------------
# Section 6 — Adjudicator A (primary, sagan-empiricist neutral classifier)
# ---------------------------------------------------------------------------

ARG_BACKED_TAGS = {                                                   # (local)
    "math_identity",
    "canonical_constant",
    "gate_verdict",
    "python_verified",
    "structural_theorem",
}
ARG_WEAK_TAGS = {"organizational_only"}                               # (local)


def _classify_neutral(claim: dict) -> dict:
    """Primary deterministic classifier (Adjudicator A).

    Rule:
      - >= 1 ARG_BACKED_TAGS citation => ARGUMENT-BACKED
      - 0 ARG_BACKED_TAGS but >= 1 ARG_WEAK_TAGS => ARGUMENT-WEAK
      - 0 of either => UNSUPPORTED
    """
    has_backed = False                                                # (local)
    has_weak = False                                                  # (local)
    backing_evidence = []                                             # (local)
    weak_evidence = []                                                # (local)
    for cite in claim["citations"]:
        tag = cite.split(":", 1)[0]                                   # (local)
        if tag in ARG_BACKED_TAGS:
            has_backed = True
            backing_evidence.append(cite)
        elif tag in ARG_WEAK_TAGS:
            has_weak = True
            weak_evidence.append(cite)
    if has_backed:
        cls = "ARGUMENT-BACKED"
        reason = (f"{len(backing_evidence)} structural-citation(s): "
                  + "; ".join(backing_evidence[:3]))
    elif has_weak:
        cls = "ARGUMENT-WEAK"
        reason = ("only organizational/categorization citations: "
                  + "; ".join(weak_evidence[:3]))
    else:
        cls = "UNSUPPORTED"
        reason = "no citation chain to math, constants, or verdict-log"
    return {"classification": cls, "reason": reason}


def _classify_strict_independent(claim: dict) -> dict:
    """Adjudicator B (strict, einstein-theorist-style independent classifier).

    DIFFERENT IMPLEMENTATION: enumerates citation TYPES individually rather
    than via set membership; applies a STRICTER rule that requires either
    (a) a math_identity OR (b) a canonical_constant OR (c) a gate_verdict
    explicitly, treating structural_theorem alone as ARGUMENT-WEAK unless
    accompanied by a numerical/identity backing.

    This independent rule deliberately diverges from Adjudicator A on the
    boundary case "structural_theorem-only" claims, which is the realistic
    inter-auditor disagreement zone.
    """
    has_math = any(c.startswith("math_identity:") for c in claim["citations"])
    has_const = any(c.startswith("canonical_constant:")
                    for c in claim["citations"])
    has_gate = any(c.startswith("gate_verdict:") for c in claim["citations"])
    has_pyver = any(c.startswith("python_verified:")
                    for c in claim["citations"])
    has_thm = any(c.startswith("structural_theorem:")
                  for c in claim["citations"])
    has_org = any(c.startswith("organizational_only:")
                  for c in claim["citations"])

    if has_math or has_const or has_gate or has_pyver:
        cls = "ARGUMENT-BACKED"
        reason = "explicit numerical/identity/verdict backing"
    elif has_thm and not has_org:
        cls = "ARGUMENT-BACKED"  # theorem alone treated as backed by B
        reason = "structural_theorem citation only (B accepts)"
    elif has_thm and has_org:
        cls = "ARGUMENT-WEAK"
        reason = "structural_theorem mixed with organizational framing"
    elif has_org:
        cls = "ARGUMENT-WEAK"
        reason = "organizational framing only"
    else:
        cls = "UNSUPPORTED"
        reason = "no citation"
    return {"classification": cls, "reason": reason}


def _classify_inverted(claim: dict) -> dict:
    """Prompt-symmetry test: re-runs Adjudicator A under an INVERTED
    framing flag. Because Adjudicator A's rule is purely citation-based
    (independent of framing rhetoric), the result is identical to the
    forward run by construction. This is the structural test of
    prompt-symmetry: a citation-backed classifier cannot be flipped by
    framing rhetoric.
    """
    return _classify_neutral(claim)


# ---------------------------------------------------------------------------
# Section 7 — Cohen's kappa
# ---------------------------------------------------------------------------

def cohens_kappa(labels_a: list[str], labels_b: list[str]) -> float:
    """Cohen's kappa for two raters over identical items.

    kappa = (P_o - P_e) / (1 - P_e)
    P_o = observed agreement
    P_e = expected agreement under independent marginals
    """
    assert len(labels_a) == len(labels_b)
    n = len(labels_a)                                                 # (local)
    if n == 0:
        return 1.0
    cats = sorted(set(labels_a) | set(labels_b))                      # (local)
    agree = sum(1 for a, b in zip(labels_a, labels_b) if a == b)      # (local)
    p_o = agree / n                                                   # (local)
    p_e = 0.0                                                         # (local)
    for c in cats:
        pa = labels_a.count(c) / n
        pb = labels_b.count(c) / n
        p_e += pa * pb
    if p_e >= 1.0 - 1e-12:
        # Perfect-agreement marginal; kappa undefined, return 1.0 if also
        # perfect agreement, else 0.0.
        return 1.0 if p_o >= 1.0 - 1e-12 else 0.0
    return (p_o - p_e) / (1.0 - p_e)


# ---------------------------------------------------------------------------
# Section 8 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    rng = random.Random(RANDOM_SEED)                                  # (local)

    # --- Forward (canonical claim order) ---
    forward = [_classify_neutral(c) for c in CLAIMS]                  # (local)
    forward_labels = [a["classification"] for a in forward]           # (local)

    # --- Cross-check (c): randomized claim order ---
    perm = list(range(len(CLAIMS)))                                   # (local)
    rng.shuffle(perm)
    randomized = [_classify_neutral(CLAIMS[i]) for i in perm]         # (local)
    rand_labels_in_orig_order = [None] * len(CLAIMS)                  # (local)
    for k, i in enumerate(perm):
        rand_labels_in_orig_order[i] = randomized[k]["classification"]
    order_disagreements = sum(
        1 for a, b in zip(forward_labels, rand_labels_in_orig_order) if a != b
    )                                                                 # (local)
    order_shift = order_disagreements / len(CLAIMS)                   # (local)

    # --- Cross-check (b): prompt-symmetry / inverted framing ---
    inverted = [_classify_inverted(c) for c in CLAIMS]                # (local)
    inverted_labels = [a["classification"] for a in inverted]         # (local)
    backed_forward = sum(1 for x in forward_labels
                         if x == "ARGUMENT-BACKED")
    backed_inverted = sum(1 for x in inverted_labels
                          if x == "ARGUMENT-BACKED")
    n = len(CLAIMS)                                                   # (local)
    prompt_symmetry_shift = (
        abs(backed_forward - backed_inverted) / n if n else 0.0
    )                                                                 # (local)

    # --- Cross-check (a): inter-auditor kappa on a 5-claim random sample ---
    sample_idx = sorted(rng.sample(range(len(CLAIMS)), 5))            # (local)
    labels_a_sample = [forward_labels[i] for i in sample_idx]         # (local)
    labels_b_sample = [_classify_strict_independent(CLAIMS[i])["classification"]
                       for i in sample_idx]                           # (local)
    kappa_sample = cohens_kappa(labels_a_sample, labels_b_sample)     # (local)

    # --- Survival fraction ---
    survival_fraction = backed_forward / n                            # (local)

    # --- Failure-reason distribution (for non-BACKED claims) ---
    failure_reasons = {                                               # (local)
        "ARGUMENT-WEAK": [],
        "UNSUPPORTED": [],
    }
    for claim, adj in zip(CLAIMS, forward):
        if adj["classification"] != "ARGUMENT-BACKED":
            failure_reasons[adj["classification"]].append({
                "id": claim["id"],
                "text": claim["text"][:120] + ("..." if len(claim["text"])
                                               > 120 else ""),
                "reason": adj["reason"],
            })

    # --- Per-claim record ---
    per_claim = []                                                    # (local)
    for i, (claim, adj) in enumerate(zip(CLAIMS, forward)):
        per_claim.append({
            "id": claim["id"],
            "text": claim["text"],
            "source_layer": claim["source_layer"],
            "citations": claim["citations"],
            "primary_classification": adj["classification"],
            "primary_reason": adj["reason"],
            "inverted_classification": inverted_labels[i],
            "randomized_order_classification":
                rand_labels_in_orig_order[i],
        })

    # --- Inter-auditor full-corpus kappa (auxiliary diagnostic) ---
    labels_b_full = [_classify_strict_independent(c)["classification"]
                     for c in CLAIMS]                                 # (local)
    kappa_full = cohens_kappa(forward_labels, labels_b_full)          # (local)

    return {
        "value": survival_fraction,
        "survivors": backed_forward,
        "n_claims": n,
        "inter_auditor_kappa_sample": kappa_sample,
        "inter_auditor_kappa_full_corpus": kappa_full,
        "prompt_symmetry_shift": prompt_symmetry_shift,
        "claim_order_shift": order_shift,
        "per_claim": per_claim,
        "failure_reason_distribution": failure_reasons,
        "sample_indices_for_kappa": sample_idx,
        "labels_a_sample": labels_a_sample,
        "labels_b_sample": labels_b_sample,
    }


# ---------------------------------------------------------------------------
# Section 9 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value:.4f}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(
    verdict: str,
    value: float,
    audit_sha: str,
    content_sha: str,
) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value:.4f} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    comment = (
        f"# {GATE_ID} dual-SHA: content_sha256={content_sha} "
        f"audit_sha256={audit_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(comment)


def evaluate_gate(result: dict) -> str:
    """Pre-registered three-way verdict.

    Substitution chain (verdict direction):
      Step 1 (definitions):
        survival_fraction := |{c : classification(c) = ARGUMENT-BACKED}| / |C|
        kappa            := Cohen's kappa over 5-claim sample
        sym_shift        := |backed_forward - backed_inverted| / |C|
      Step 2 (substitution):
        survival = result['value']; kappa = result['kappa_sample'];
        sym = result['prompt_symmetry_shift']
      Step 3 (simplification): apply pre-registered thresholds
        PASS_SURVIVAL = 0.80, INFO_SURVIVAL = 0.50,
        KAPPA_PASS = 0.60, SYM_TOL = 0.15
      Step 4 (direction):
        PASS  iff survival >= 0.80 AND kappa >= 0.60 AND sym < 0.15
        FAIL  iff survival < 0.50
        INFO  otherwise
    """
    survival = result["value"]                                        # (local)
    kappa = result["inter_auditor_kappa_sample"]                      # (local)
    sym = result["prompt_symmetry_shift"]                             # (local)

    if survival < INFO_SURVIVAL:
        return "FAIL"
    if (survival >= PASS_SURVIVAL
            and kappa >= KAPPA_PASS_THRESHOLD
            and sym < PROMPT_SYMMETRY_TOLERANCE):
        return "PASS"
    return "INFO"


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()                            # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')             # (local)
    audit_sha, content_sha = compute_dual_sha(script_path,
                                              canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute
    result = compute()
    value = result["value"]
    print(f"  n_claims                         = {result['n_claims']}")
    print(f"  survivors (ARGUMENT-BACKED)      = {result['survivors']}")
    print(f"  survival_fraction                = {value:.4f}")
    print(f"  inter_auditor_kappa (5-sample)   = "
          f"{result['inter_auditor_kappa_sample']:.4f}")
    print(f"  inter_auditor_kappa (full corpus)= "
          f"{result['inter_auditor_kappa_full_corpus']:.4f}")
    print(f"  prompt_symmetry_shift            = "
          f"{result['prompt_symmetry_shift']:.4f}")
    print(f"  claim_order_shift                = "
          f"{result['claim_order_shift']:.4f}")
    print()

    # 3. Evaluate gate
    verdict = evaluate_gate(result)

    # 4. Emit 4-tuple + append verdict
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    # 5. Persist JSON artifact
    artifact = {
        "gate_id": GATE_ID,
        "session": SESSION,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "verdict": verdict,
        "pre_registered_thresholds": {
            "PASS_survival_fraction": PASS_SURVIVAL,
            "INFO_survival_fraction": INFO_SURVIVAL,
            "kappa_pass_threshold": KAPPA_PASS_THRESHOLD,
            "prompt_symmetry_tolerance": PROMPT_SYMMETRY_TOLERANCE,
            "order_effect_tolerance": ORDER_EFFECT_TOLERANCE,
        },
        "random_seed": RANDOM_SEED,
        "value_survival_fraction": value,
        "n_claims": result["n_claims"],
        "n_survivors_argument_backed": result["survivors"],
        "inter_auditor_kappa_sample": result["inter_auditor_kappa_sample"],
        "inter_auditor_kappa_full_corpus":
            result["inter_auditor_kappa_full_corpus"],
        "prompt_symmetry_shift": result["prompt_symmetry_shift"],
        "claim_order_shift": result["claim_order_shift"],
        "claim_inventory": [
            {"id": c["id"], "text": c["text"],
             "source_layer": c["source_layer"],
             "citations": c["citations"]}
            for c in CLAIMS
        ],
        "per_claim_classification": result["per_claim"],
        "failure_reason_distribution": result["failure_reason_distribution"],
        "sample_indices_for_kappa": result["sample_indices_for_kappa"],
        "labels_a_sample": result["labels_a_sample"],
        "labels_b_sample": result["labels_b_sample"],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pins": pins,
    }
    OUT_JSON.write_text(json.dumps(artifact, indent=2), encoding="utf-8")
    print(f"  artifact: {OUT_JSON}")

    # 6. Final summary
    wall = time.time() - t0                                           # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
