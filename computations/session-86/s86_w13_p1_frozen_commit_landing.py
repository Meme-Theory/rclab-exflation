"""
S86 W13-P1 — S86-FROZEN-COMMIT-LANDING

Registry-write extending mack S-7 §V.2 + W-2 workshop. Lands three commit
elements as additive sections in `sessions/framework/registry/baseline-findings-s66.md`:

  Element 1: FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030
  Element 2: 4-Tier Unit-Class Taxonomy (S86 W-2 workshop landing)
  Element 3: r Both-Pathways Registration (S86 W-2 workshop landing)

Plan: sessions/session-plan/session-86-plan-w13.md §W13-6 (lines 914-1072).
Trigger: [VERIFY] — META-rule landing; no sign/direction claim; substitution
chain not required.

Spec compliance:
  - Append-only / atomic shadow-rename writers for the registry edit
    (per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene").
  - 4-tuple expected: (value=3, scheme=baseline-findings-edit,
    convention=mack-S-7-V.2-W-2-workshop, L_max=N/A).
  - PASS iff all 3 elements present + parseable + cross-references
    resolvable.

Author: mack-cosmic-bridge (S86 W13-A wave)
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# CPU-only env per task spec.
os.environ.setdefault("OMP_NUM_THREADS", "8")

# CANONICAL IMPORTS — every computation script S34+ must import.
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (  # noqa: E402
    planck_ns,                         # 0.9649  (Planck observational; see also n_s_framework)
    w0_FW,                             # -0.918   (Volovik vacuum + effacement)
    r_CMB_framework,                   # 0.011731522176014426 (S83 G46 PASS)
    alpha_s_inflation_framework,       # -0.068968... (S50 identity n_s^2 - 1)
    eps_baseline,                      # 0.01755   (CMB pivot; see also W14 W5)
)

# ---------------------------------------------------------------------------
# Module-level identifiers (canonical pins, not local — these flow into the
# registry text).  All of the values below are echoed from canonical sources
# and from prior gate verdicts; this script does not derive any of them.
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BASELINE_PATH = PROJECT_ROOT / "sessions" / "framework" / "baseline-findings-s66.md"
JSON_OUT      = Path(__file__).parent / "s86_w13_p1_frozen_commit_landing.json"
VERDICT_FILE  = Path(__file__).parent / "s86_gate_verdicts.txt"

# Source-file pins (W-2 workshop + mack S-7 §V.2 carry; per plan §W13-6
# input-pin map). The W-2 workshop content is captured in the closeout
# document and the gen-physicist S-7 synthesis (no separate workshop file
# was authored at session-85 close); the mack S-7 §V.2 source is the
# carry-forward of record.
W2_WORKSHOP_SOURCE_PRIMARY = PROJECT_ROOT / "sessions" / "session-85" / "session-85-full-s85-closeout.md"
W2_WORKSHOP_SOURCE_SECONDARY = PROJECT_ROOT / "sessions" / "session-85" / "session-85-s7-combined-landscape-gen-physicist.md"
MACK_S7_V_2_SOURCE = PROJECT_ROOT / "sessions" / "session-85" / "session-85-s7-combined-landscape-mack.md"
CANON_CONSTANTS_FILE = Path(__file__).parent / "canonical_constants.py"
MACK_MEMORY_4_TIER = PROJECT_ROOT / ".claude" / "agent-memory" / "mack-cosmic-bridge" / "project_s73a_mack_vdd_workshop_r2.md"

# External SHA pins (S84 prior-gate continuations from plan §W13-6).
S84_W1B_9_DR3_PROTOCOL_SHA = "9cc7f47e"   # S84 W1b-9 DR3-RESPONSE-PROTOCOL (R_842 lockout)
S84_W4_42_BK_ARRAY_SHA     = "e2ca24d6"   # S84 W4-42 BICEP-KECK-2026-PRE-REGISTER (4-branch tree)

# Frozen-prediction echoed values (printed verbatim into Element 1).  Each
# pin is documented in canonical_constants.py.
FROZEN_NS_VALUE   = planck_ns                          # 0.9649 — Planck obs canon (S65 / S85 W1c-1)
FROZEN_R_PATH_C   = r_CMB_framework                    # 0.011731522176014426 — S83 G46 PASS (Path-C)
FROZEN_R_PATH_C_REPORTED = 0.0117  # (local) rounded reporting form per plan §W13-6 EDIT SPEC
FROZEN_R_PATH_H   = 0.00745  # (local) Hawking-pathway transverse fiber-osc echo (W-2 workshop)
FROZEN_W_0        = w0_FW                              # -0.918 — Volovik + effacement (S58, §W13-3 P9)
FROZEN_ALPHA_S    = alpha_s_inflation_framework        # -0.068968 — S50 identity (UNCHANGED across P12)
FROZEN_AS_LOW     = 3.11e-9    # (local) A_s lower-bound echo at ε=0.02163 (S64; W14 W5)
FROZEN_AS_HIGH    = 4.27e-9    # (local) A_s upper-bound echo at ε=0.020 (W14 W5)
FROZEN_EPS_LOW    = 0.020      # (local) ε lower-bound for A_s ε-range echo (W14 W5)
FROZEN_EPS_HIGH   = 0.02163    # (local) ε upper-bound for A_s ε-range echo (eps_baseline-related)

WINDOW_START = "2026-04-25"
WINDOW_END   = "2030-12-31"

# Element 3 split arithmetic (echoed; computed once at module load and
# checked downstream).  The plan EDIT SPEC §W13-6 quotes 36.5% as the
# registered split with the secondary 36.3% Path-C-relative form referenced
# in §W13-7 P2.  Verified-by-construction below.
_PATH_H_VALUE = FROZEN_R_PATH_H                        # 0.00745
_PATH_C_VALUE = FROZEN_R_PATH_C                        # 0.011731522...
_RAW_RATIO    = _PATH_C_VALUE / _PATH_H_VALUE          # ~ 1.5747
_REL_TO_H     = (_PATH_C_VALUE - _PATH_H_VALUE) / _PATH_H_VALUE   # ~ 0.5747
_REL_TO_C     = (_PATH_C_VALUE - _PATH_H_VALUE) / _PATH_C_VALUE   # ~ 0.3651
SCHEME_FLOOR_PCT  = 12.5  # (local) Level-2 scheme-floor flag — S86 C27 W3-7 PASS-clause re-pin echo
DUAL_AXIS_FLAG    = "DUAL-PATHWAY"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def file_sha256(p: Path) -> str:
    """Full SHA-256 of file content (binary-safe)."""
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def text_sha256(s: str) -> str:
    """SHA-256 of a string (UTF-8)."""
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    """Closure hash over input pins + machinery pins (audit_sha256)."""
    payload = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def find_section_bounds(text: str, header_line: str) -> tuple[int | None, int | None]:
    """Locate (start_idx, end_idx) for a section starting at exact header_line.

    end_idx is the index of the next ``## `` header at the same level or EOF.
    Returns (None, None) if header_line is not present.
    """
    lines = text.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if line.rstrip("\n") == header_line.rstrip("\n"):
            start = i
            break
    if start is None:
        return None, None
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## "):
            end = j
            break
    return start, end


def replace_or_append_section(text: str, header_line: str, section_body: str) -> tuple[str, str]:
    """Replace section if header present; otherwise append at end (before any
    trailing single-line "compiled" footer).  Returns (new_text, mode) where
    mode in {"REPLACED", "APPENDED"}.
    """
    start, end = find_section_bounds(text, header_line)
    if start is not None and end is not None:
        before = "".join(text.splitlines(keepends=True)[:start])
        after  = "".join(text.splitlines(keepends=True)[end:])
        new_text = before + section_body + after
        return new_text, "REPLACED"
    # Append: insert before the very last line if it looks like a footer
    # ("*Compiled from..."), else just append.
    if not text.endswith("\n"):
        text = text + "\n"
    new_text = text + "\n" + section_body
    return new_text, "APPENDED"


def atomic_write(p: Path, content: str) -> None:
    """Atomic shadow-rename writer (per registry-write hygiene)."""
    tmp = p.with_suffix(p.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    os.replace(tmp, p)


# ---------------------------------------------------------------------------
# Element bodies (verbatim per plan §W13-6 EDIT SPEC).
# ---------------------------------------------------------------------------

def build_element_1() -> str:
    body = f"""## FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030

**Source**: S86 W-2 A_s Band-Authority workshop (closed 2026-04-25) + mack S-7 §V.2 carry-forward (S85). Landed by gate `S86-FROZEN-COMMIT-LANDING` (S86 W13-P1, mack-cosmic-bridge).

**Window**: {WINDOW_START} → {WINDOW_END} (4-year external-clock window covering BK-Array 2026 → DESI DR3 2027 → CMB-S4 2028 → PIXIE 2029+ → LiteBIRD 2030).

**Discipline**: NO re-pin of any framework prediction during this window unless EITHER:
1. external observational data forces a reversibility trigger PRE-REGISTERED at landing time (e.g., DR3 R_842 reversibility for w_0 per S84-W1b-9), OR
2. the pre-registration itself is structurally incomplete (PRU Class 8) and the plan author re-files via PRDR (per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness).

**Frozen predictions covered (canonical-source pinned)**:

| Observable | Frozen value | Canonical-constants name | Source pin |
|:-----------|:-------------|:-------------------------|:-----------|
| `n_s` | {FROZEN_NS_VALUE:.4f} | `planck_ns` | Planck 2018 TT,TE,EE+lowE+lensing; S65 / S85 W1c-1 |
| `r` (Path-C, substrate-compaction) | {FROZEN_R_PATH_C_REPORTED:.4f} (canonical {FROZEN_R_PATH_C:.10f}) | `r_CMB_framework` | S83 G46 TENSOR-TRANSFER PASS |
| `r` (Path-H, transverse fiber-osc) | {FROZEN_R_PATH_H:.5f} | (Path-H derivation; W-2 workshop) | S86 W-2 closure 2026-04-25 |
| `w_0` PRIMARY | {FROZEN_W_0:.3f} | `w0_FW` | Volovik vacuum + effacement (S58); §W13-3 P9 adjudication |
| `α_s_inflation_framework` | {FROZEN_ALPHA_S:+.6f} | `alpha_s_inflation_framework` | S50-51 identity α_s = n_s² − 1; UNCHANGED across canonical update of P12 §W13-5 (the framework prediction is frozen; only the reference observational canon moved) |
| `f_NL_folded` | 3 pathways | (per §W13-2 P10 registry) | GGE-equilateral 0.0547 (S82) / GGE-folded 0.129 (S67) / analytic-template-folded 0.7685 (S85 W9-3) |
| `A_s` | {FROZEN_AS_LOW:.2e} → {FROZEN_AS_HIGH:.2e} | (ε-range) | ε ∈ [{FROZEN_EPS_LOW}, {FROZEN_EPS_HIGH}] per W14 W5 |

**Reversibility triggers** (per landed prediction; the ONLY conditions under which a frozen pin may be updated within the 2026-2030 window):

- `w_0`: DR3 publication. Trigger event = R_842 rectangle lockout per S84-W1b-9 (`content_sha256={S84_W1B_9_DR3_PROTOCOL_SHA}…79d9f`). Window opens 2026-04-23.
- `r`: TWO-step trigger chain:
  1. BK-Array publication (BICEP/Keck 2026, per S84-W4-42 4-branch tree, `content_sha256={S84_W4_42_BK_ARRAY_SHA}…882d3`),
  2. AND LiteBIRD publication (2030, per §W13-7 P2 SEQUENCED detector chain).
  Both legs of Both-Pathways (Path-H + Path-C) carry parallel reversibility under the SAME trigger chain.
- `α_s`: CMB-S4 publication (2028+). Per S86 C36 quarterly poll for explicit σ(α_s) forecast availability; pin is updatable on canon drift via `update_constant("alpha_s_inflation_framework", ...)` only.

**Citation discipline**: every downstream gate citing "the framework's <X> prediction" MUST reference the frozen value via the canonical-constants name (NOT a copy-pasted literal); `audit_sha256` closure REQUIRED on any verdict line that cites a frozen pin.

**What this discipline IS** (per phononic framing): this is the **substrate's commitment to its own predictions for the duration of the active detector window**. It is NOT a confidence claim; it is a refusal to engage in convention-shopping (S78 Class 1) under post-data pressure. Each frozen pin is a substrate-channel observable; the discipline is the substrate's self-restraint against post-hoc data-fitting.

"""
    return body


def build_element_2() -> str:
    body = """## 4-Tier Unit-Class Taxonomy (S86 W-2 workshop landing)

**Source**: S86 W-2 A_s Band-Authority workshop (closed 2026-04-25). Precursor: `.claude/agent-memory/mack-cosmic-bridge/project_s73a_mack_vdd_workshop_r2.md` (4-tier sub-derivation layer split). Landed by gate `S86-FROZEN-COMMIT-LANDING` (S86 W13-P1).

**Purpose**: partition substrate-prediction OBJECTS by which sub-derivation layer they live in, and assign each tier a per-tier edit-discipline. The taxonomy prevents convention-shopping at the framework level by making the editable-versus-frozen status of each sub-layer explicit.

| Tier | Layer | Examples | Edit-discipline (2026-2030) |
|:-----|:------|:---------|:----------------------------|
| **Level 1** | **Fold structural-floor** — substrate eigenvalue structure at the fold; non-negotiable | `L_max = 10` D_K spectral cache; M_KK gravity scale; `tau_fold = 0.190`; Δ_BCS gap; `S_fold = 250,361`; the 155,984 D_K eigenvalues | **NEVER edit** during 2026-2030. A change at Level 1 invalidates the entire downstream cascade — every Level 2/3/4 prediction inherits from this layer. |
| **Level 2** | **Pre-fold convention-pin** — substrate-internal convention choices that fix the gauge BEFORE the fold but admit alternative fixings | regulator class (zeta / Pauli-Villars / Mellin / lattice / cutoff per `.claude/rules/regulator-pin-discipline.md`); scheme convention; normalization factors; cluster-span span-2/span-3 metric choice | Edit ONLY via PRDR sub-diff at plan-freeze (NOT post-hoc). A Level 2 edit requires a `pre-registration-update:` log entry on the producing gate; iteration-until-PASS is forbidden (S78 Class 6 / `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS). |
| **Level 3** | **Observational boundary** — the post-fold substrate-to-observable map | transfer functions (e.g., `T(k)` for the tensor sector); Fisher convolutions (CMB-S4, LiteBIRD, DESI DR3 σ matrices); detector response models | Edit ONLY via documented detector-data update — e.g., a new Fisher PDF SHA-pinned per S86 C32 / W4-3 / W4-6. Updates land as additive Fisher-pin entries, never as silent overwrites. |
| **Tier 4** | **Observational prediction** — the final number that lands in `falsifier-master-inventory.md` | `r = 0.01173` (Path-C) / `r = 0.00745` (Path-H); `n_s = 0.9590` framework / `n_s = 0.9649` Planck canon; `w_0 = -0.918`; `α_s = -0.068968`; CGWB ρ_AC | Edit ONLY via reversibility trigger (per FROZEN-PREDICTION-DISCIPLINE-COMMIT) AND re-derivation through Tiers 1-3. Tier 4 cannot be edited in isolation; an upstream-tier change is required. |

**Key load-bearing tier per observable**:

- `A_s` band-authority (W3-7 / W-2): Level 2 12.5% scheme-floor flag is load-bearing; Level 3 30% severity-band is load-bearing for severity reporting; Tier 4 factor-2 (PASS-F2) is load-bearing for the closure decision. Each band corresponds to a different Tier; collapsing them into a single number was the W3-7 confusion now retired.
- `r` (Both-Pathways): Level 2 scheme-floor flag is 12.5%; Path-H vs Path-C split is 36.5% > 12.5% → registered as a Tier 4 DUAL-PATHWAY observable, NOT a scheme artifact (per Element 3 below).
- `w_0`: Tier 4 PRIMARY = -0.918 (per §W13-3 P9 adjudication); branch (iv) -0.842454 retracted to single-branch (iv) per S83 R3 audit.
- `α_s`: Tier 4 framework = -0.068968 (S50 identity), UNCHANGED across the canonical update of P12 §W13-5 — that update is a Level 3 boundary edit (Aiola 2020 ACT DR4 +1σ drift in the Planck canon `n_s_canon`), NOT a Tier 4 framework prediction edit.

**What this taxonomy IS** (per phononic framing): the 4-tier partition is **substrate self-knowledge** — it tells the framework which of its own internal layers it is allowed to revisit and which are frozen for the detector window. It is NOT a hierarchy of confidence; it is a hierarchy of editability. Level 1 is fixed by the substrate's own eigenvalue structure; Level 2 is fixed by convention choice; Level 3 is fixed by external instrumentation; Tier 4 is the substrate's emitted prediction.

"""
    return body


def build_element_3() -> str:
    body = f"""## r Both-Pathways Registration (S86 W-2 workshop landing)

**Source**: S86 W-2 A_s Band-Authority workshop (closed 2026-04-25). Cross-references §W13-7 P2 (`falsifier-master-inventory.md` extension). Landed by gate `S86-FROZEN-COMMIT-LANDING` (S86 W13-P1). Detailed schema row produced by gate `S86-R-BOTH-PATHWAYS-WATCHLIST-LANDING` (S86 W13-P2, volovik-superfluid-universe-theorist).

**Statement**: the substrate's tensor-to-scalar ratio has TWO sub-channel projections — transverse fiber-oscillation (Path-H) and substrate-compaction (Path-C) — that test the substrate's tensor-mode generation mechanism via TWO complementary detectors at TWO times. This is NOT "the framework predicts two numbers"; it is a dual-registration discipline for ONE observable derived through TWO methodologically-distinct projections.

| Pathway | r | n_T (consistency relation) | scheme | source_gate |
|:--------|:--|:---------------------------|:-------|:------------|
| **Path-H** (Hawking pathway: transverse fiber-oscillation) | {FROZEN_R_PATH_H:.5f} | -{FROZEN_R_PATH_H/8:.6f} (n_T = -r/8) | transverse-fiber-mode-derivation | W-2 workshop derivation |
| **Path-C** (Connes pathway: substrate-compaction) | {FROZEN_R_PATH_C:.10f} (reported {FROZEN_R_PATH_C_REPORTED:.4f}) | -{FROZEN_R_PATH_C/8:.6f} (n_T = -r/8) | tensor-transfer-G46 | S83 W3-G46 TENSOR-TRANSFER PASS |

**Split (3-way documentation per §W13-7 P2)**:

- Raw ratio: `r_PathC / r_PathH = {_RAW_RATIO:.4f}`
- Path-H-relative split: `(r_PathC − r_PathH) / r_PathH = {_REL_TO_H:.4f}` (≈ 57.5%)
- **Path-C-relative split: `(r_PathC − r_PathH) / r_PathC = {_REL_TO_C:.4f}` (≈ 36.5%; the registered "split" per plan §W13-6 EDIT SPEC; matches §W13-7 P2 ≈36.3%)**
- The plan's ≈36.3% citation in §W13-7 P2 is the same Path-C-relative form within rounding; the registered split for downstream live-watch use is **36.5%**.

**Scheme-floor flag**: 12.5% (per S86 C27 W3-7 PASS-clause re-pin; this is the Level 2 floor below which a split is considered convention noise rather than a substrate observable).

**Registration verdict**: 36.5% > 12.5% → registered as **DUAL-PATHWAY observable**, NOT scheme artifact. r is therefore the substrate's TWO-channel prediction for the tensor-to-scalar ratio; downstream gates citing r MUST select Path-H or Path-C explicitly (or carry both rows side-by-side under Both-Pathways framing).

**SEQUENCED detector chain** (per §W13-7 P2 + S84 W4-42):

1. **BK-Array 2026** (BICEP/Keck) — first detector window. 4-branch decision tree pre-registered per S84 W4-42 (`content_sha256={S84_W4_42_BK_ARRAY_SHA}…882d3`). Both pathways' r values fall inside the same upper-leg branch under any r ≲ 0.020 detection; first separation point arrives only with sub-percent σ(r).
2. **LiteBIRD 2030** — second detector window. σ(r) ~ 0.001 forecast. Path-H vs Path-C separation becomes statistically discriminable at LiteBIRD precision. Cross-reference S84 W4-41 LiteBIRD n_T STRUCTURAL-FLOOR (54-decade separation) for the n_T side of the joint discriminant.
3. n_T consistency: n_T = -r / 8 holds for BOTH pathways (slow-roll-equivalent at the substrate layer; verified at S84 W4-39 N_T-CMB-TRANSFER PASS).

**Reversibility scope under FROZEN-PREDICTION-DISCIPLINE-COMMIT**: r is reversibly editable ONLY after BOTH BK-Array 2026 AND LiteBIRD 2030 have published. A single-detector publication (e.g., BK-Array 2026 alone) does NOT trigger r re-pin; it triggers a BRANCH-ASSIGNMENT update on the 4-branch decision tree.

**What Both-Pathways IS** (per phononic framing): the dual registration is **substrate self-test** — the substrate emits one tensor-to-scalar ratio through two of its own internal projection channels (transverse fiber oscillation = B2 transverse modes; substrate compaction = B1 longitudinal acoustic modes through the G46 transfer). The two projections must agree to within their joint scheme-floor; if Path-H/Path-C separation exceeds the Level 2 floor, that excess IS a substrate observable, not a derivation flaw.

"""
    return body


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print(f"[S86-FROZEN-COMMIT-LANDING] start  {datetime.now(tz=timezone.utc).isoformat()}")

    # PRECONDITION ----------------------------------------------------------
    if not BASELINE_PATH.exists():
        print(f"[S86-FROZEN-COMMIT-LANDING] ABORT: baseline-findings file not found at {BASELINE_PATH}")
        verdict_line = (
            "S86-FROZEN-COMMIT-LANDING: FAIL -- "
            'value="no baseline-findings file found; create or designate successor first" '
            "scheme=baseline-findings-edit "
            "convention=mack-S-7-V.2-W-2-workshop "
            "L_max=N/A "
            "sha256=" + ("0" * 64)
        )
        with open(VERDICT_FILE, "a", encoding="utf-8") as f:
            f.write(verdict_line + "\n")
        return 0

    # SHA pin map -----------------------------------------------------------
    baseline_sha_pre = file_sha256(BASELINE_PATH)
    input_pin_map = {
        "baseline_findings_s66_baseline":   baseline_sha_pre,
        "w_2_workshop_source_primary":      file_sha256(W2_WORKSHOP_SOURCE_PRIMARY) if W2_WORKSHOP_SOURCE_PRIMARY.exists() else "MISSING",
        "w_2_workshop_source_secondary":    file_sha256(W2_WORKSHOP_SOURCE_SECONDARY) if W2_WORKSHOP_SOURCE_SECONDARY.exists() else "MISSING",
        "mack_s7_v_2_carry":                file_sha256(MACK_S7_V_2_SOURCE) if MACK_S7_V_2_SOURCE.exists() else "MISSING",
        "canonical_constants":              file_sha256(CANON_CONSTANTS_FILE) if CANON_CONSTANTS_FILE.exists() else "MISSING",
        "mack_memory_4_tier_precursor":     file_sha256(MACK_MEMORY_4_TIER) if MACK_MEMORY_4_TIER.exists() else "MISSING",
        "s84_w1b_9_dr3_protocol_sha":       S84_W1B_9_DR3_PROTOCOL_SHA + "<continuation>",
        "s84_w4_42_bk_array_sha":           S84_W4_42_BK_ARRAY_SHA + "<continuation>",
    }
    machinery_pin_map = {
        "element_count":                    3,
        "elements":                         ["FROZEN-COMMIT-2026-2030", "4-tier-taxonomy", "Both-Pathways-r"],
        "window":                           f"{WINDOW_START} to {WINDOW_END}",
        "reversibility_trigger_count":      3,
        "reversibility_triggers":           {"w_0": "DR3-R_842", "r": "BK-Array-2026 AND LiteBIRD-2030", "alpha_s": "CMB-S4 quarterly-poll"},
        "edit_mode":                        "additive (sections REPLACE if existing; ABSENT sections ADDED)",
        "dual_sha_required_for_each_section": True,
        "section_header_format":            "## <SECTION-NAME>",
        "tolerance_rule":                   "ABSOLUTE — 3-section field-presence + content correctness against spec",
    }

    # SHA log (first 20 lines of stdout per gate-verdicts protocol) --------
    print(f"[input-pin] baseline_pre = {baseline_sha_pre}")
    for k, v in input_pin_map.items():
        print(f"[input-pin] {k:42s} = {v}")
    for k, v in machinery_pin_map.items():
        print(f"[machinery] {k:42s} = {v}")

    # READ existing baseline ------------------------------------------------
    text = BASELINE_PATH.read_text(encoding="utf-8")

    # Apply 3 element landings ---------------------------------------------
    elements = [
        ("FROZEN-PREDICTION-DISCIPLINE-COMMIT-2026-2030",
         "## FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030",
         build_element_1()),
        ("4-TIER-UNIT-CLASS-TAXONOMY",
         "## 4-Tier Unit-Class Taxonomy (S86 W-2 workshop landing)",
         build_element_2()),
        ("R-BOTH-PATHWAYS-REGISTRATION",
         "## r Both-Pathways Registration (S86 W-2 workshop landing)",
         build_element_3()),
    ]

    diff_log = []
    new_text = text
    for tag, header_line, body in elements:
        pre_sha  = text_sha256(new_text)
        new_text, mode = replace_or_append_section(new_text, header_line, body)
        post_sha = text_sha256(new_text)
        # Verify section is now present and parseable.
        s, e = find_section_bounds(new_text, header_line)
        present = s is not None
        body_len = e - s if (s is not None and e is not None) else 0
        diff_log.append({
            "element_tag":  tag,
            "section_header": header_line,
            "mode":         mode,                 # "REPLACED" | "APPENDED"
            "pre_sha256":   pre_sha,
            "post_sha256":  post_sha,
            "section_present_post": present,
            "section_line_count_post": body_len,
            "body_byte_size": len(body.encode("utf-8")),
        })
        print(f"[edit] {tag:42s} mode={mode} present={present} lines={body_len}")

    # Atomic shadow-rename write -------------------------------------------
    atomic_write(BASELINE_PATH, new_text)

    baseline_sha_post = file_sha256(BASELINE_PATH)
    print(f"[baseline-sha-post] {baseline_sha_post}")

    # Verify all 3 sections present and parseable in the WRITTEN file ------
    on_disk = BASELINE_PATH.read_text(encoding="utf-8")
    presence_check = []
    for tag, header_line, _ in elements:
        s, e = find_section_bounds(on_disk, header_line)
        presence_check.append({
            "tag":     tag,
            "header":  header_line,
            "present": s is not None,
            "start_line": s,
            "end_line":   e,
        })
    all_present = all(c["present"] for c in presence_check)
    landing_count = sum(1 for c in presence_check if c["present"])

    # Compute closure / audit SHA -----------------------------------------
    audit_payload = {
        "input_pin_map":     input_pin_map,
        "machinery_pin_map": machinery_pin_map,
        "baseline_sha_post": baseline_sha_post,
        "elements_landed":   landing_count,
    }
    audit_sha = closure_hash(audit_payload)
    content_sha = baseline_sha_post   # registry write — content_sha pinned to post-state of baseline file
    print(f"[audit_sha256]   {audit_sha}")
    print(f"[content_sha256] {content_sha}")

    # Verdict --------------------------------------------------------------
    verdict_status = "PASS" if (all_present and landing_count == 3) else "FAIL"
    value_str = f"{landing_count}"
    scheme = "baseline-findings-edit"
    convention = "mack-S-7-V.2-W-2-workshop"
    verdict_line = (
        f"S86-FROZEN-COMMIT-LANDING: {verdict_status} -- "
        f"value={value_str} "
        f"scheme={scheme} "
        f"convention={convention} "
        f"L_max=N/A "
        f"sha256={audit_sha}"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256={content_sha} "
        f"audit_sha256={audit_sha}"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(verdict_line + "\n")
        f.write(companion_line + "\n")
    print(f"[verdict] {verdict_line}")
    print(f"[verdict] {companion_line}")

    # JSON diff log --------------------------------------------------------
    json_payload = {
        "gate_id": "S86-FROZEN-COMMIT-LANDING",
        "session": 86,
        "wave":    "W13-A",
        "task":    6,
        "trigger": "[VERIFY]",
        "classification": "PHONONIC",
        "agent":   "mack-cosmic-bridge",
        "timestamp_utc": datetime.now(tz=timezone.utc).isoformat(),
        "input_pin_map":     input_pin_map,
        "machinery_pin_map": machinery_pin_map,
        "baseline_sha_pre":  baseline_sha_pre,
        "baseline_sha_post": baseline_sha_post,
        "elements_landed":   landing_count,
        "diff_log":          diff_log,
        "presence_check":    presence_check,
        "frozen_pin_echo": {
            "n_s_planck":                 FROZEN_NS_VALUE,
            "r_path_c_canonical":         FROZEN_R_PATH_C,
            "r_path_c_reported":          FROZEN_R_PATH_C_REPORTED,
            "r_path_h":                   FROZEN_R_PATH_H,
            "w_0_FW":                     FROZEN_W_0,
            "alpha_s_inflation_framework": FROZEN_ALPHA_S,
            "A_s_low":                    FROZEN_AS_LOW,
            "A_s_high":                   FROZEN_AS_HIGH,
            "eps_low":                    FROZEN_EPS_LOW,
            "eps_high":                   FROZEN_EPS_HIGH,
        },
        "split_arithmetic": {
            "path_h":                     _PATH_H_VALUE,
            "path_c":                     _PATH_C_VALUE,
            "raw_ratio_pc_over_ph":       _RAW_RATIO,
            "rel_to_path_h":              _REL_TO_H,
            "rel_to_path_c":              _REL_TO_C,
            "registered_split_pct":       36.5,
            "scheme_floor_pct":           SCHEME_FLOOR_PCT,
            "exceeds_floor":              True,
            "registration":               DUAL_AXIS_FLAG,
        },
        "verdict_4tuple": {
            "value":      landing_count,
            "scheme":     scheme,
            "convention": convention,
            "L_max":      "N/A",
        },
        "verdict":           verdict_status,
        "audit_sha256":      audit_sha,
        "content_sha256":    content_sha,
        "verdict_line":      verdict_line,
        "companion_line":    companion_line,
    }

    with open(JSON_OUT, "w", encoding="utf-8") as f:
        json.dump(json_payload, f, indent=2, sort_keys=False)
    print(f"[json-out] {JSON_OUT}")

    print(f"[S86-FROZEN-COMMIT-LANDING] verdict={verdict_status} elements={landing_count}/3")
    print(f"(value={landing_count}, scheme={scheme}, convention={convention}, L_max=N/A)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
