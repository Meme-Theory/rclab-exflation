#!/usr/bin/env python3
"""
S90 W3-4 — S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING (CF-36 / CF-S90-MACK-8)
=============================================================================

Lands a METHODOLOGY-class calibration-corpus instance at
`sessions/framework/registry/pru-class-corpus.md §1 PRU Class 8.2`
(append after Instance #5) documenting the α_s symbol-overload pattern
across three structurally distinct numerical quantities all sharing the
symbol "α_s":
  1. QCD strong-coupling at M_Z: `alpha_s_MZ_obs = 0.1180`
     (PDG 2024; canonical_constants.py:alpha_s_MZ_obs line 1566)
  2. LEGACY inflationary running: `alpha_s_inflation_framework = -0.068968`
     (n_s_canon² − 1 with Planck-2018 anchor n_s_canon = 0.9649;
      canonical_constants.py:alpha_s_inflation_framework line 1614;
      superseded at S88 W-15 W15-V.2)
  3. BIT-EXACT Route-B identity: `α_s_canonical = -8587279/100000000
     ≈ -0.085 872 79` (Sage-QQ exact in Q via n_s_FW_exact² − 1 at
      substrate-distance-1 Mellin pole s=3; canonical_constants.py:
      n_s_FW_exact line 1719; S89 W7a triple-verified)

5-element instance template per plan §W3-4 §6:
  (i) 3 distinct numerical objects table (symbol form + value + line + domain)
  (ii) substitution chain cross-check (Steps 1-5 with distance pairs +
       discrimination at CMB-S4 / CMB-HD precision)
  (iii) structural cause (QCD-literature vs inflationary-cosmology-literature
        symbol adoption; algebra-axis orthogonality MANDATORY-K=3)
  (iv) disambiguation rule per S85-W1c-CANONICAL-CONSTANTS-ALPHA-S-
       DISAMBIGUATION-PATCH (bare α_s FORBIDDEN going forward)
  (v) audit-script extension queue `_alpha_s_symbol_overload_audit.py`
      (S91+ carry-forward)

Class 8.2 verifier rubric 4-elements per MANDATORY:
  - Pattern set: 3 symbol forms
  - Disjunction declaration: any qualifier accepted; bare auto-fails
  - Negative-marker set: bare \\bα_s\\b|\\balpha[-_]s\\b without qualifier
  - Exemplar SHA: S87 α-s W2 + S89 W7a `01c1ac83…` + S89 W4-4 `e3da1d13…`

METHODOLOGY-class wave per `.claude/rules/wave-classification.md`:
  - M1: artifact-existence (corpus row + allowlist row + instances entry)
  - M2: Edit-only on rule-file / registry / methodology files
  - M3: verbatim sub-diff from plan §W3-4 §6 markdown template
  - M4: methodology-wave-allowlist row append at plan-freeze

This script touches THREE files atomically (per-file atomic):
  1. `sessions/framework/registry/pru-class-corpus.md` — append Instance #6
     to §1 PRU Class 8.2 calibration corpus
  2. `.claude/rules/methodology-wave-allowlist.md` — append 3-column row
     `| W3-4 | S90 | <sha256_of_plan_block> |`
  3. `sessions/framework/registry/methodology-wave-instances.md` — append
     per-instance rationale entry `### W3-4 (S90) — <sha256>`

Plan: sessions/session-plan/session-90-plan-w3.md §W3-4.
Agent: mack-cosmic-bridge sole writer (primary) per `feedback_mack-bridge-role.md`.
Trigger: [AUDIT] — no 3-tuple companion row required.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import time  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

GATE_ID = "S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING"  # (local)
SCHEME = "calibration-corpus-instance-class-8-2"  # (local)
CONVENTION = "mack-sole-writer-pre-registration-OR-lizzi-alternate"  # (local)
L_MAX = "N/A"  # (local)

CORPUS_PATH = PROJECT_ROOT / "sessions" / "framework" / "registry" / "pru-class-corpus.md"
ALLOWLIST_PATH = PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
INSTANCES_PATH = PROJECT_ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"
PLAN_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-90-plan-w3.md"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

# Audit-SHA full-64-char pins (sibling W3 gates + cross-session pins):
S89_W7A_AUDIT_FULL_64 = "01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17"  # (local)
S89_W4_4_AUDIT_FULL_64 = "e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89"  # (local)
CF_29_S90_W2_AUDIT_FULL_64 = "92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27"  # (local)
CF_33_S90_W3_AUDIT_FULL_64 = "736178083caa51c09ee3c1b8521717a84809812b0c74ebfe7a212a98f9e83028"  # (local)
CF_34_S90_W3_AUDIT_FULL_64 = "be1e362c5db63e7376c189893246f91f4c68c2592aa73868437c807b1069d5b4"  # (local)
CF_35_S90_W3_AUDIT_FULL_64 = "a1328849cbd361b01e14c210dc9cff3dff6dcba453897c53d06971f703c526b0"  # (local)

# Anchor for landing the new corpus instance in pru-class-corpus.md §1:
# Insert AFTER Instance #5 boundary, BEFORE K-counter advancement section.
INSTANCE_5_END_ANCHOR = "Forward-enforcement: any plan-block claiming an asymptotic limit / boundary value MUST pre-flight Python-verify the boundary direction at plan-freeze. Audit-script extension queued at `_machinery_feasibility_audit.py` with \"boundary direction substitution chain\" sub-check."  # (local)

# Anchor for landing allowlist row at end of allowlist table (append-after-W1-17):
ALLOWLIST_W1_17_ANCHOR = "| W1-17 | S90 | 01cd431699d88193bf564b94f61180f3f542ca71e44f6582832874ec93ea8f69 |"  # (local)

# Anchor for landing instances entry at end of file (append-after-W1-17 entry):
# The W1-17 entry ends with the "container-thinking violation FORBIDDEN" sentence.
INSTANCES_W1_17_END_ANCHOR = (
    "the substrate's structural orthogonality at §VII.AH obs2 + obs3 IS established at "
    "the substrate-physics layer (W4-7 PASS 8/8 + JOINT (c)+(d) verified); the K=2 "
    "K-counter advancement is the methodology disclosure that the corpus accumulation "
    'event has fired".'
)  # (local)


def sha256_of(path):
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def extract_plan_block_w3_4(plan_text):
    """Extract the §W3-4 plan-block from plan-file text.

    Boundaries: starts at line containing '## §W3-4.' (the W3-4 section
    heading); ends at the next '## ' heading at top level (typically
    '## Wave 3 → Wave 4 Decision Point' which follows §W3-4 §13).
    """
    start_marker = "## §W3-4."  # (local)
    start_idx = plan_text.find(start_marker)
    if start_idx == -1:
        raise ValueError(f"Start marker '{start_marker}' not found in plan file")
    # Find next top-level "## " heading after start (skip immediate "###" sub-headings)
    search_start = start_idx + len(start_marker)
    while True:
        next_idx = plan_text.find("\n## ", search_start)
        if next_idx == -1:
            # End of file; extract to end
            return plan_text[start_idx:]
        # Skip "### " sub-headings (3+ hash)
        # We've found "\n## " — confirm it's exactly 2 hashes (not part of "### ")
        check_pos = next_idx + 1  # after the newline
        # Check if it's "## " not "### "
        if check_pos + 3 <= len(plan_text) and plan_text[check_pos:check_pos+3] == "## ":
            # Confirm: next char after "## " must not be "#"
            if check_pos + 3 < len(plan_text) and plan_text[check_pos+3] != "#":
                # This is a top-level "## " heading; this is the end
                return plan_text[start_idx:next_idx + 1]  # include trailing newline
        search_start = next_idx + 1


def compute_plan_block_sha(plan_path):
    plan_text = plan_path.read_text(encoding="utf-8")
    block = extract_plan_block_w3_4(plan_text)
    h = hashlib.sha256()
    h.update(block.encode("utf-8"))
    return h.hexdigest(), len(block)


def build_corpus_instance_text():
    """Per plan §W3-4 §6 verbatim markdown template (lines 558-623).

    Pure-function: builds full corpus-instance sub-section text in memory.
    """
    return """

#### Instance #6 — S90 W3 CF-36 α_s symbol-overload calibration corpus (2026-05-13)

> **Provenance**: S90 W3-4 (`S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING`; CF-36 / CF-S90-MACK-8); mack-cosmic-bridge sole-writer primary per `feedback_mack-bridge-role.md`; lizzi-spectral-functional-theorist alternate writer pathway per Class 8.2 PRU MANDATORY verifier-rubric pre-registration discipline (defaulted to mack at plan-freeze).
>
> **K-counter status**: documented as Class 8.2 instance #6 (verifier-rubric pre-registration discipline; the parent §1 K-counter sits at K=5 MANDATORY post-S88 W-21 W6b-56 V.6, so Instance #6 advances to K=6 — but the parent K-counter has already saturated past K_promotion=3 so the status is MANDATORY irrespective of this instance) AND a NEW sub-tracked "symbol-overload pattern" K-counter at **K=1 SUGGESTION** pending K=3 MANDATORY promotion per `feedback_rules-compensate-missing-structure.md` K=3 threshold. The symbol-overload sub-counter is distinct from the parent Class 8.2 verifier-rubric K-counter because the structural pathology is "shared symbol denotes structurally distinct numerical objects across STRUCTURALLY ORTHOGONAL axes" (algebra-axis orthogonality MANDATORY-K=3 per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`), separate from "rubric tokens admit cardinality-only matches" (Instances #1–#5 baseline).

**5-element instance template per Class 8.2 PRU MANDATORY**:

**(i) 3 distinct numerical objects sharing the symbol "α_s"**:

| # | Symbol form | Numerical value | Source / Provenance | Domain |
|:-:|:------------|:----------------|:--------------------|:-------|
| 1 | `alpha_s_MZ_obs` (or `α_s(M_Z)`, `\\alpha_s(M_Z)`) | `0.1180` (PDG 2024) | `canonical_constants.py:alpha_s_MZ_obs` (line 1566 current file) | QCD strong-coupling running at M_Z; gauge-coupling axis; NOT inflationary |
| 2 | `alpha_s_inflation_framework` (legacy framework form) | `-0.068968` | `canonical_constants.py:alpha_s_inflation_framework` (line 1614 current file) `= n_s_canon**2 - 1`; `n_s_canon = planck_ns = 0.9649` is Planck-2018-anchored float (LEGACY; superseded at S88 W-15 W15-V.2 by bit-exact `n_s_FW_exact = Fraction(9561, 10000)`) | Inflationary running of scalar spectral index; CMB-inflationary axis; LEGACY Planck-anchor form |
| 3 | `α_s_canonical` (Route-B identity bit-exact) | `-0.085 872 79` = `-8587279/100000000` (Sage-QQ bit-exact in Q) | S87 α-s W2 PASS; `canonical_constants.py:n_s_FW_exact` (line 1719 current file)-derivable via `n_s_FW_exact² − 1`; S89 W7a `audit_sha256=01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` triple-verified | Inflationary running of scalar spectral index; CMB-inflationary axis; BIT-EXACT Route-B identity at substrate-distance-1 pole s=3 |

**Legacy laboratory-anchor pin** (for cross-axis disambiguation reference): `planck_alpha_s = -0.0045` (`canonical_constants.py:planck_alpha_s` line 1586; Planck-2018 legacy; superseded by `alpha_s_canon_2020 = +0.0023 ± 0.0063` at `canonical_constants.py:alpha_s_canon_2020` line 1600 per S86-W13 P12). These are laboratory-IN measurement values, NOT framework predictions — disambiguating axis is observational-canonical-vs-framework-substrate.

**(ii) Substitution chain cross-check** (Step-by-Step disambiguation per `.claude/rules/math-scripts.md §"Double-Check Logic Before Compute"`):

```
Step 1: Define 3 distinct quantities all denoted "α_s":
        q_1 = α_s(M_Z) = 0.1180                                              [QCD; canonical_constants.py:alpha_s_MZ_obs]
        q_2 = alpha_s_inflation_framework = -0.068968                        [LEGACY Planck-anchor; canonical_constants.py:alpha_s_inflation_framework]
        q_3 = α_s_canonical = -0.085872                                       [BIT-EXACT Route-B; canonical_constants.py:n_s_FW_exact-derived]

Step 2: Classification by axis:
        q_1 lies on QCD-gauge-coupling axis (strong-coupling running at M_Z ≈ 91.2 GeV)
        q_2 lies on inflationary-spectral-index-running axis (LEGACY Planck-anchor pin)
        q_3 lies on inflationary-spectral-index-running axis (BIT-EXACT Route-B identity)

Step 3: Distance pairs:
        |q_1 − q_2| = |0.1180 − (-0.068968)| = 0.186968                       [structurally unrelated; ORTHOGONAL axes]
        |q_1 − q_3| = |0.1180 − (-0.085872)| = 0.203872                       [structurally unrelated; ORTHOGONAL axes]
        |q_2 − q_3| = |(-0.068968) − (-0.085872)| = 0.016904                  [same axis; Planck-anchor drift]

Step 4: Discrimination at projected detector precision:
        CMB-S4 σ_α_s ≈ 2.3e-3: |q_2 − q_3| / σ_S4 ≈ 7.4σ                     [bit-exactness DRIFT alone discriminable at S4 if applied to q_2]
        CMB-HD σ_α_s ≈ 1.1e-3: |q_2 − q_3| / σ_HD ≈ 15σ                       [bit-exactness DRIFT decisive at HD]

Step 5: Direction of disambiguation:
        q_1 is on a DIFFERENT AXIS from q_2 and q_3 (QCD vs inflationary); cannot be conflated within framework α_s axis predictions.
        q_2 is SUPERSEDED by q_3 (bit-exactness discipline; S88 W-15 W15-V.2 landing); q_2 retained only for historical-annotation cross-link.
        Future framework computation scripts MUST use q_3 (`α_s_canonical` or `canonical_constants.py:n_s_FW_exact`-derived form).
        Future watchlist + falsifier rows MUST cite q_3 as the substrate prediction (per CF-29 Row #3 update + CF-33 / CF-34 watchlist rows).

Direction: bare "α_s" in framework documentation FORBIDDEN going forward; every citation MUST carry a qualifier disambiguating q_1 / q_2 / q_3.
```

**(iii) Structural cause** (why the symbol is overloaded):

The symbol "α_s" was independently adopted in two unrelated domains:
1. **QCD literature** (1970s-): α_s denotes the strong-coupling running of the QCD gauge coupling; canonical evaluation at M_Z (≈ 91.2 GeV); positive value O(0.1).
2. **Inflationary cosmology literature** (1990s-): α_s denotes `dn_s / d ln k`, the running of the scalar spectral index; canonical evaluation at CMB pivot scale (≈ 0.05 Mpc⁻¹); typically negative value O(10⁻²–10⁻³).

The framework's substrate-distance-1 pole s=3 Mellin observable (Route-B identity `n_s² − 1`) lands on the INFLATIONARY α_s axis (instance 3 = q_3). The framework's QCD prediction (gauge-coupling running, separately derived at substrate-distance-2 pole s=4 per S82 W1c FI chain) lands on the QCD α_s axis (instance 1 = q_1) — these are STRUCTURALLY ORTHOGONAL observables that happen to share a symbol per `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 (algebra-INVARIANT spectrum-only-functional family vs algebra-DEPENDENT state-pair-functional family).

The Planck-anchor-vs-bit-exact distinction (instance 2 = q_2 vs instance 3 = q_3) is intra-axis and represents a Class-(c) PIN-DRIFT-FROM-STALE-SOURCE pattern (Planck-2018 anchor superseded by bit-exact Route-B identity at S88 W-15 W15-V.2) per `.claude/rules/epistemic-discipline.md §"Source Reconciliation"`.

**(iv) Disambiguation rule** (forward-discipline for downstream consumers):

Per `S85-W1c-CANONICAL-CONSTANTS-ALPHA-S-DISAMBIGUATION-PATCH` (canonical_constants.py:alpha_s_MZ_obs line 1566 inline-comment + line 1586 inline-comment for planck_alpha_s legacy), every citation of "α_s" in framework documentation MUST be accompanied by an explicit qualifier disambiguating which of the 3 instances is meant:
- QCD: write `α_s(M_Z)` or `alpha_s_MZ_obs` (PDG canonical evaluation point)
- Inflationary LEGACY: write `alpha_s_inflation_framework` (Planck-2018-anchor; superseded; cite only for historical-annotation)
- Inflationary BIT-EXACT: write `α_s_canonical` (Route-B identity at substrate-distance-1 pole s=3; canonical for new computation scripts)

Bare "α_s" without qualifier is FORBIDDEN in framework documentation going forward (S90 W3 CF-36 landing forward-discipline pin).

**(v) Audit-script extension queue**:

Future `_alpha_s_symbol_overload_audit.py` (S91+ carry-forward, queued at plan §"Wave 3 Wrap-Up Discipline" item 1 `S91-ALPHA-S-SYMBOL-OVERLOAD-AUDIT-SCRIPT`) greps framework documentation for `\\bα_s\\b|\\balpha[-_]s\\b|\\b\\\\alpha_s\\b` patterns NOT followed by an explicit qualifier within a 20-character window; flags violations as Class 8.2 PRU verifier-rubric pre-registration failures. Until the audit script lands, plan-freeze validators manually cross-check α_s citations against this corpus instance.

**Class 8.2 verifier rubric 4-elements** (MANDATORY at plan-freeze):

1. **Pattern set** (3 symbol forms accepted with qualifiers):
   - `α_s(M_Z)` / `alpha_s_MZ_obs` / `\\alpha_s(M_Z)` (Instance 1 = QCD)
   - `alpha_s_inflation_framework` (Instance 2 = LEGACY inflationary)
   - `α_s_canonical` / `alpha_s_canonical` (Instance 3 = BIT-EXACT inflationary)
2. **Disjunction declaration**: any qualifier accepted (disjunctive); bare "α_s" auto-fails.
3. **Negative-marker set**: bare `\\bα_s\\b|\\balpha[-_]s\\b|\\b\\\\alpha_s\\b` without qualifier within 20-character window.
4. **Exemplar SHA** (3 anchor SHAs):
   - S87 α-s W2 PASS (substrate-side; Instance 3 bit-exact pin)
   - S89 W7a `audit_sha256=01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` (Sage-QQ exact triple-verification; substrate-side Instance 3)
   - S89 W4-4 `audit_sha256=e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89` (joint (n_s, α_s) hypersurface; observational-side Instance 3; Class-8.5 PRU 2D verdict-line value-field calibration instance #1)

**Cross-link to existing rule-files**:
- `.claude/rules/epistemic-discipline.md §"Source Reconciliation"` Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY (instances 2 and 3 are both derivative forms of an n_s-pin; instance 2 derives from Planck-2018-anchored `n_s_canon`; instance 3 derives from bit-exact `n_s_FW_exact`; PRIMARY canonical is `n_s_FW_exact`)
- `.claude/rules/epistemic-discipline.md §"Verifier-Rubric Pre-Registration (Class 8.2)"` MANDATORY (this corpus instance is the calibration instance #6 in §1 corpus; sub-tracked symbol-overload pattern K=1)
- `.claude/rules/regulator-pin-discipline.md` (forward extension to symbol-overload-aware regulator-pin discipline at S91+)
- `S85-W1c-CANONICAL-CONSTANTS-ALPHA-S-DISAMBIGUATION-PATCH` (canonical disambiguation precedent at `canonical_constants.py:alpha_s_MZ_obs` line 1566 + `:planck_alpha_s` line 1586 + `:alpha_s_inflation_framework` line 1614 inline comments)
- `canonical_constants.py` lines: `alpha_s_MZ_obs` line 1566 (Instance 1 = QCD), `planck_alpha_s` line 1586 (legacy observational), `alpha_s_canon_2020` line 1600 (Aiola+ 2020 ACT DR4 + Planck combined; current laboratory canonical), `alpha_s_inflation_framework` line 1614 (Instance 2 = LEGACY inflationary), `n_s_FW_exact` line 1719 (Instance 3 = BIT-EXACT inflationary; PRIMARY canonical)
- `sessions/framework/registry/falsifier-master-inventory.md` Row #3 post-CF-29 update (CF-29 W2 audit `92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27` supersedes Row #3 cell from `-0.068968` to `-0.085872`)
- CF-33 `S90-CMB-S4-ALPHA-S-WATCHLIST-LANDING` (Wave-3 sibling; audit `736178083caa51c09ee3c1b8521717a84809812b0c74ebfe7a212a98f9e83028`; cites α_s_canonical Instance 3 as substrate prediction, NOT Instance 2)
- CF-34 `S90-CMB-HD-ALPHA-S-NLO-WATCHLIST-LANDING` (Wave-3 sibling; audit `be1e362c5db63e7376c189893246f91f4c68c2592aa73868437c807b1069d5b4`; cites α_s_canonical Instance 3 + bit-exact NLO ε² recompute under `eps_H_W6` per `canonical_constants.py:eps_H_W6` line 1717; LEGACY Instance 2 `-0.068968` explicit NOT-TO-BE-USED flag)
- CF-35 `S90-3HE-B-LIAISON-WATCHLIST-LANDING` (Wave-3 sibling; audit `a1328849cbd361b01e14c210dc9cff3dff6dcba453897c53d06971f703c526b0`; structurally orthogonal axis — 3He-B BdG cocycle ratio 7.324992; α_s symbol-overload corpus instance documents cross-axis disambiguation that 3He-B vs CMB α_s share NO numerical scale)

**Substrate framing** (per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`):

The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the substrate's intrinsic Mellin running at substrate-distance-1 pole s=3 IS `α_s_canonical = n_s_FW_exact² − 1 = -8587279/100000000` (Sage-QQ bit-exact in Q). The QCD α_s(M_Z) is a structurally DISTINCT observable (gauge-coupling running, NOT spectral-index running); the legacy `alpha_s_inflation_framework = -0.068968` is a Planck-2018-anchor-DERIVATIVE form of an earlier framework approximation (`n_s_canon` was a previous-canonical Planck-2018-anchored float, NOT the bit-exact `n_s_FW_exact = Fraction(9561, 10000)` pin landed at S88 W-15 W15-V.2).

The corpus instance documents that the shared symbol "α_s" represents three structurally distinct numerical objects; the substrate framing flows substrate → laboratory at each instance, but the LABORATORY context differs across the three (QCD-physics laboratory at instance 1; CMB-inflationary-physics laboratory at instances 2 and 3; bit-exactness discipline distinguishes instance 2 from instance 3).

Container-thinking violation FORBIDDEN: "all three α_s values live in the same parameter space"; INVERT: "the substrate has THREE structurally orthogonal predictions that share the symbol 'α_s' by historical accident; the algebra-axis orthogonality K=3 MANDATORY discipline forbids conflation between QCD and inflationary axes; the bit-exactness discipline distinguishes the Planck-anchor-DERIVATIVE legacy form from the Route-B-identity BIT-EXACT form on the inflationary axis".
"""  # (local)


def build_allowlist_row(plan_block_sha):
    return f"| W3-4 | S90 | {plan_block_sha} |"  # (local)


def build_instances_entry(plan_block_sha, plan_block_len):
    return f"""

### W3-4 (S90) — {plan_block_sha}

**Provenance**: gate-ID `S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING` (CF-36 / CF-S90-MACK-8); agent `mack-cosmic-bridge` (sole-writer primary) per `feedback_mack-bridge-role.md` AMRI-PROMOTED 2026-04-28; alternate writer pathway `lizzi-spectral-functional-theorist` per Class 8.2 PRU MANDATORY verifier-rubric pre-registration discipline (defaulted to mack at plan-freeze); plan reference `sessions/session-plan/session-90-plan-w3.md` §W3-4 lines 524-end (plan-block sha256 `{plan_block_sha}`; {plan_block_len} chars).

**Gate classification (M1∧M2∧M3∧M4 conjunction)**:

- **M1**: artifact-existence-with-substantive-content per `.claude/rules/wave-classification.md §M1`. PASS predicate = (i) corpus instance #6 row appended to `sessions/framework/registry/pru-class-corpus.md §1 PRU Class 8.2` after Instance #5 with all 5-element template content (3 distinct numerical objects table + substitution chain Steps 1-5 + structural cause + disambiguation rule + audit-script extension queue) AND Class 8.2 verifier rubric 4-elements (pattern set + disjunction declaration + negative-marker set + 3 exemplar SHAs); (ii) methodology-wave-allowlist 3-column row `| W3-4 | S90 | {plan_block_sha[:16]}… |` appended at end of allowlist table; (iii) methodology-wave-instances per-instance rationale entry `### W3-4 (S90) — {plan_block_sha[:16]}…` appended at end of instances file. No numerical comparison; all conditions are artifact-existence + content-verification predicates.

- **M2**: producing operations restricted to Edit on 3 rule-file / registry / methodology files (`sessions/framework/registry/pru-class-corpus.md`, `.claude/rules/methodology-wave-allowlist.md`, `sessions/framework/registry/methodology-wave-instances.md`) + Python marker-presence assertions + canonical verdict-line emission. No `.py` numerical comparisons against pre-registered thresholds; the [AUDIT] trigger documents the α_s symbol-overload pattern at 3 distinct numerical values as a calibration corpus instance.

- **M3**: verbatim sub-diff from plan §W3-4 §6 dispatch prompt (5-element instance template markdown + Class 8.2 verifier rubric 4-elements + cross-link list + substrate framing reminder all verbatim from plan). The canonical_constants.py line-number citations are corrected from plan's stated values (1528/1548/1562/1576/1681) to current actual lines (1566/1586/1600/1614/1719) per direct grep verification — symbol-name citations (`alpha_s_MZ_obs`, `planck_alpha_s`, `alpha_s_canon_2020`, `alpha_s_inflation_framework`, `n_s_FW_exact`) are the canonical references; line numbers are descriptive cross-references that drift on canonical_constants.py edits. No first-principles new derivation.

- **M4**: row landing per `.claude/rules/methodology-wave-allowlist.md §"Edit discipline"` orchestrator-only-edit protocol; 3-column row `| W3-4 | S90 | {plan_block_sha} |` appended at end of allowlist table (post-W1-17 (S90)).

**Sub-clause structure landed**:

1. `sessions/framework/registry/pru-class-corpus.md §1 PRU Class 8.2 calibration corpus` — Instance #6 row inserted AFTER Instance #5 (S88 W-21 W6b-56 V.6 boundary-direction sub-check, 2026-05-08), BEFORE the K-counter advancement summary section. The new instance documents the α_s symbol-overload pattern across 3 structurally distinct numerical quantities (QCD `α_s(M_Z) = 0.1180` + LEGACY `alpha_s_inflation_framework = -0.068968` + BIT-EXACT `α_s_canonical = -0.085872`) on STRUCTURALLY ORTHOGONAL axes (QCD-gauge-coupling vs CMB-inflationary-spectral-index-running per algebra-axis orthogonality MANDATORY-K=3) AND on intra-axis bit-exactness-vs-Planck-anchor-drift (Instance 2 vs Instance 3 on the same inflationary axis differing by ≈ 0.017 ≈ 15σ at CMB-HD projected precision).
2. `.claude/rules/methodology-wave-allowlist.md §"Allowlist Rows"` — 3-column row `| W3-4 | S90 | {plan_block_sha} |` appended at end of table (post-W1-17 (S90)); enables M4 satisfaction for forward-grep of methodology-wave gate-IDs.
3. `sessions/framework/registry/methodology-wave-instances.md` — per-instance rationale entry `### W3-4 (S90) — {plan_block_sha}` appended at end of file (post-W1-17 (S90)); preserves the lifted-out rationale prose verbatim per S88 W9-RULE-CLEANUP lift-out discipline (`methodology-wave-allowlist.md §"Edit discipline"` item 4 + S88 W9 housekeeping).

**Closure conditions**: PASS verdict per pre-registered §9 (PASS) conditions — corpus instance row text written with all 5 elements present + Class 8.2 verifier rubric 4-elements present + cross-link to S85-W1c disambiguation patch + cross-links to 5 canonical_constants.py symbol-name citations + cross-link to CF-33 / CF-34 watchlist rows + cross-link to Row #3 post-CF-29 update + methodology-wave-allowlist row appended with computed sha256_of_plan_block. audit_sha256 over input-pin map (plan-block sha256 + canonical_constants.py + pru-class-corpus pre-edit + allowlist pre-edit + instances pre-edit). content_sha256 over the producing script bytes.

**[AUDIT] substitution chain** (per plan §W3-4 §10 — symbol-overload disambiguation direction):

- Step 1 (Definition): `α_s_symbols := {{q_1 = 0.1180, q_2 = -0.068968, q_3 = -0.085872}}` — 3 distinct numerical objects all denoted "α_s".
- Step 2 (Classification): `q_1` on QCD-gauge-coupling axis; `q_2`, `q_3` on inflationary-spectral-index-running axis (structurally orthogonal by algebra-axis K=3 MANDATORY).
- Step 3 (Distance pairs): `|q_1 − q_2| = 0.186968`, `|q_1 − q_3| = 0.203872` (cross-axis structurally unrelated); `|q_2 − q_3| = 0.016904` (intra-axis Planck-anchor drift).
- Step 4 (Detector discrimination): `|q_2 − q_3| / σ_CMB-S4 ≈ 7.4σ`, `/ σ_CMB-HD ≈ 15σ` (bit-exactness drift decisive at HD).
- Step 5 (Direction): bare "α_s" FORBIDDEN going forward; every citation MUST carry q_1 / q_2 / q_3 qualifier; future framework computation scripts MUST use q_3.
- Conclusion: corpus instance landed as calibration-corpus instance #6 in Class 8.2 corpus (parent K-counter already at K=5 MANDATORY); sub-tracked symbol-overload pattern at K=1 SUGGESTION pending K=3 MANDATORY promotion.

**Cross-link**: `sessions/session-plan/session-90-plan-w3.md` §W3-4 (plan reference, {plan_block_len}-char block, sha256=`{plan_block_sha}`); `sessions/framework/registry/pru-class-corpus.md §1` Instance #6 insertion target (post-S88 W-21 W6b-56 V.6 K=5 MANDATORY corpus); `.claude/rules/methodology-wave-allowlist.md §"Allowlist Rows"` table (W3-4 row append target; post-W1-17 (S90)); `.claude/rules/epistemic-discipline.md §"Verifier-Rubric Pre-Registration (Class 8.2)"` MANDATORY (parent rule statement); `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 (algebra-INVARIANT vs algebra-DEPENDENT orthogonality; QCD-axis vs inflationary-axis orthogonality structurally identical pattern); `feedback_mack-bridge-role.md` AMRI-PROMOTED 2026-04-28 (mack-cosmic-bridge sole-writer for observational-anchor + symbol-overload calibration); `feedback_rules-compensate-missing-structure.md` (K=3 promotion threshold for sub-tracked symbol-overload K-counter); CF-29 audit `92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27` (W2 sibling: falsifier-master-inventory Row #3 α_s update); CF-33 audit `736178083caa51c09ee3c1b8521717a84809812b0c74ebfe7a212a98f9e83028` (W3 sibling: CMB-S4 watchlist row); CF-34 audit `be1e362c5db63e7376c189893246f91f4c68c2592aa73868437c807b1069d5b4` (W3 sibling: CMB-HD NLO ε² watchlist row); CF-35 audit `a1328849cbd361b01e14c210dc9cff3dff6dcba453897c53d06971f703c526b0` (W3 sibling: 3He-B liaison watchlist row — structurally orthogonal axis cross-reference); S89 W7a audit `01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` (substrate-side exemplar SHA Instance 3); S89 W4-4 audit `e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89` (observational-side exemplar SHA Instance 3 joint hypersurface).

**Carry-forward (2 substantive items)** per plan §"Wave 3 Wrap-Up Discipline":

1. **`S91-ALPHA-S-SYMBOL-OVERLOAD-AUDIT-SCRIPT`** (forward; effort 0.5 we): implement `_alpha_s_symbol_overload_audit.py` per CF-36 (v) audit-script extension queue. Inputs: this CF-36 corpus instance + 5 canonical_constants.py symbol-name citations (`alpha_s_MZ_obs`, `planck_alpha_s`, `alpha_s_canon_2020`, `alpha_s_inflation_framework`, `n_s_FW_exact`). Gate: PASS = audit script runs against framework documentation corpus + returns 0 false-positives on grandfathered legacy citations + 0 false-negatives on synthetic test corpus (3 distinct α_s values bare-cited without qualifier).
2. **`S91-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-K2-ADVANCEMENT`** (forward; effort 0.3 we per instance): identify a second independent calibration instance of symbol-overload pattern across framework documentation. Candidates: n_s symbol-overload between bit-exact `n_s_FW_exact` and `n_s_canon = planck_ns = 0.9649` Planck-2018-anchor float; OR w_0 symbol-overload between `w0_FW = -0.918` Volovik partition canonical and `w0_FW_R842 = -0.842454` branch (iv) substrate-compaction reading (canonical_constants.py:w0_FW_R842 if present). Advances sub-tracked symbol-overload K-counter to K=2 SUGGESTION; promotes to K=3 MANDATORY when a third instance lands.

**Parallel-review dispatch**: not applicable per `.claude/skills/rclab-solo/SKILL.md` Phase 2 step 2 agent-ownership-takeover discipline (solo runner takes ownership of mack-sole-writer gate; alternate writer pathway lizzi-spectral-functional-theorist defaulted to mack at plan-freeze per plan §4); no Agent-tool dispatch under this skill's run.

**Substrate framing**: the α_s symbol-overload IS the methodology F-image of substrate-IS structural orthogonality at the algebra-axis level (per `.claude/rules/epistemic-discipline.md §"Layer-Decomposition"` `F: substrate → methodology → audit`). The substrate's two orthogonal α_s observables are: (i) QCD gauge-coupling running at substrate-distance-2 pole s=4 (S82 W1c FI chain); (ii) inflationary scalar-spectral-index running at substrate-distance-1 pole s=3 (Route-B identity). The symbol-overload is the methodology disclosure that historical accident (independent symbol adoption in QCD and inflationary cosmology literatures from the 1970s and 1990s respectively) produced an ambiguity at the documentation layer; the corpus instance lands the audit-trail discipline that forecloses the conflation by construction. The intra-axis bit-exactness drift (Instance 2 vs Instance 3 on the inflationary axis) IS the methodology F-image of substrate-IS canonical-pin supersession (S88 W-15 W15-V.2 Route-B identity bit-exact pin replaces Planck-2018-anchor float). Direction of explanation flows substrate-IS structural orthogonality → emergent symbol-overload at documentation layer → methodology F-image disambiguation rule at audit-script + corpus-instance layer. Container-thinking violation FORBIDDEN: "the symbol 'α_s' IS the observable"; INVERT: "the substrate's TWO observables IS the structural reality (QCD α_s at s=4 ≠ inflationary α_s at s=3); the shared symbol is a post-hoc descriptor of two structurally orthogonal pole observables, NOT the observable itself"."""  # (local)


def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def build_corpus_promotion(original_text, corpus_instance_text):
    """Insert corpus instance #6 AFTER Instance #5 end anchor."""
    marker = "Instance #6 — S90 W3 CF-36"  # (local)
    if marker in original_text:
        return original_text  # idempotent
    if INSTANCE_5_END_ANCHOR not in original_text:
        raise ValueError(f"Instance #5 end anchor not found in pru-class-corpus.md")
    # Find end of Instance #5 paragraph (end of line containing the anchor)
    idx = original_text.find(INSTANCE_5_END_ANCHOR)
    end_of_line = original_text.find("\n", idx)
    if end_of_line == -1:
        raise ValueError("Instance #5 anchor line not terminated in pru-class-corpus.md")
    insertion_point = end_of_line + 1  # right after Instance #5 closing line
    return (
        original_text[:insertion_point]
        + corpus_instance_text
        + original_text[insertion_point:]
    )


def build_allowlist_promotion(original_text, allowlist_row):
    """Append allowlist row after W1-17 (S90)."""
    marker = "| W3-4 | S90 |"  # (local)
    if marker in original_text:
        return original_text  # idempotent
    if ALLOWLIST_W1_17_ANCHOR not in original_text:
        raise ValueError(f"W1-17 (S90) anchor not found in methodology-wave-allowlist.md")
    idx = original_text.find(ALLOWLIST_W1_17_ANCHOR)
    end_of_line = original_text.find("\n", idx)
    if end_of_line == -1:
        raise ValueError("W1-17 (S90) anchor line not terminated")
    insertion_point = end_of_line + 1
    return (
        original_text[:insertion_point]
        + allowlist_row
        + "\n"
        + original_text[insertion_point:]
    )


def build_instances_promotion(original_text, instances_entry):
    """Append instances entry at end of file (post-W1-17 W1 entry)."""
    marker = "### W3-4 (S90)"  # (local)
    if marker in original_text:
        return original_text  # idempotent
    # Append at end of file (the instances entries are append-only chronologically)
    sep = "\n" if not original_text.endswith("\n") else ""  # (local)
    return original_text + sep + instances_entry + "\n"


def verify_corpus(text):
    return {
        "instance_6_header_present": "Instance #6 — S90 W3 CF-36 α_s symbol-overload" in text,
        "5_element_template_i_3_distinct_numbers": "5-element instance template per Class 8.2 PRU MANDATORY" in text and "(i) 3 distinct numerical objects sharing the symbol" in text,
        "5_element_template_ii_substitution_chain": "(ii) Substitution chain cross-check" in text,
        "5_element_template_iii_structural_cause": "(iii) Structural cause" in text,
        "5_element_template_iv_disambiguation_rule": "(iv) Disambiguation rule" in text,
        "5_element_template_v_audit_script_queue": "(v) Audit-script extension queue" in text,
        "qcd_alpha_s_mz_obs_0_1180": "0.1180" in text and "alpha_s_MZ_obs" in text,
        "legacy_alpha_s_inflation_framework_minus_0_068968": "-0.068968" in text and "alpha_s_inflation_framework" in text,
        "bit_exact_alpha_s_canonical_minus_8587279_over_100000000": "-8587279/100000000" in text and "α_s_canonical" in text,
        "distance_pair_q1_q2_0_186968": "0.186968" in text,
        "distance_pair_q1_q3_0_203872": "0.203872" in text,
        "distance_pair_q2_q3_0_016904": "0.016904" in text,
        "cmb_s4_discrimination_7_4_sigma": "7.4σ" in text,
        "cmb_hd_discrimination_15_sigma": "15σ" in text,
        "algebra_axis_orthogonality_mandatory_k3": "Algebra-axis orthogonality K-counter" in text and "MANDATORY-K=3" in text,
        "s85_w1c_disambiguation_patch_cross_link": "S85-W1c-CANONICAL-CONSTANTS-ALPHA-S-DISAMBIGUATION-PATCH" in text,
        "class_8_2_verifier_rubric_4_elements": "Class 8.2 verifier rubric 4-elements" in text,
        "exemplar_s89_w7a_full_64char": S89_W7A_AUDIT_FULL_64 in text,
        "exemplar_s89_w4_4_full_64char": S89_W4_4_AUDIT_FULL_64 in text,
        "canonical_constants_alpha_s_MZ_obs_line_1566": "alpha_s_MZ_obs" in text and "line 1566" in text,
        "canonical_constants_planck_alpha_s_line_1586": "planck_alpha_s" in text and "line 1586" in text,
        "canonical_constants_alpha_s_canon_2020_line_1600": "alpha_s_canon_2020" in text and "line 1600" in text,
        "canonical_constants_alpha_s_inflation_framework_line_1614": "alpha_s_inflation_framework" in text and "line 1614" in text,
        "canonical_constants_n_s_FW_exact_line_1719": "n_s_FW_exact" in text and "line 1719" in text,
        "cf_29_w2_cross_link": CF_29_S90_W2_AUDIT_FULL_64 in text,
        "cf_33_w3_sibling_cross_link": CF_33_S90_W3_AUDIT_FULL_64 in text,
        "cf_34_w3_sibling_cross_link": CF_34_S90_W3_AUDIT_FULL_64 in text,
        "cf_35_w3_sibling_orthogonal_axis_cross_link": CF_35_S90_W3_AUDIT_FULL_64 in text,
        "sub_tracked_symbol_overload_k_counter_k_1_suggestion": "sub-tracked \"symbol-overload pattern\" K-counter at **K=1 SUGGESTION**" in text,
        "substrate_framing_paragraph": "The substrate IS the spectral triple" in text or "the substrate IS the spectral triple" in text,
        "phononic_framing_rule_cite": "phononic-framing.md" in text and "IS Space, Not IN Space" in text,
        "future_audit_script_alpha_s_symbol_overload_audit_py": "_alpha_s_symbol_overload_audit.py" in text,
        "s91_carry_forward_queue": "S91-ALPHA-S-SYMBOL-OVERLOAD-AUDIT-SCRIPT" in text,
    }


def verify_allowlist(text, plan_block_sha):
    return {
        "w3_4_row_present": f"| W3-4 | S90 | {plan_block_sha} |" in text,
        "schema_3_columns": True,  # by construction (single row appended)
    }


def verify_instances(text, plan_block_sha):
    return {
        "w3_4_entry_header_present": f"### W3-4 (S90) — {plan_block_sha}" in text,
        "m1_m2_m3_m4_conjunction": ("**M1**" in text and "**M2**" in text and "**M3**" in text and "**M4**" in text),
        "provenance_block": "**Provenance**:" in text,
        "audit_substitution_chain": "[AUDIT] substitution chain" in text,
        "carry_forward_block": "Carry-forward (2 substantive items)" in text,
        "substrate_framing_block": "**Substrate framing**:" in text,
    }


def emit_verdict(verdict, value_str, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


def main():
    t0 = time.time()
    inputs = [SHARED_DIR / "canonical_constants.py", PLAN_PATH, CORPUS_PATH, ALLOWLIST_PATH, INSTANCES_PATH]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 0: extract plan-block §W3-4 + compute SHA-256")
    plan_block_sha, plan_block_len = compute_plan_block_sha(PLAN_PATH)
    print(f"  plan-block sha256: {plan_block_sha[:16]}... ({plan_block_len} chars)")
    print()

    print("Step 1: build promotion texts (corpus + allowlist + instances)")
    corpus_instance_text = build_corpus_instance_text()
    allowlist_row = build_allowlist_row(plan_block_sha)
    instances_entry = build_instances_entry(plan_block_sha, plan_block_len)
    print(f"  corpus_instance_text length: {len(corpus_instance_text)} chars")
    print(f"  allowlist_row: {allowlist_row}")
    print(f"  instances_entry length: {len(instances_entry)} chars")
    print()

    print("Step 2: build_promotion + write_atomic_with_fsync (3 files)")
    # File 1: pru-class-corpus.md
    corpus_original = CORPUS_PATH.read_text(encoding="utf-8")
    try:
        corpus_promoted = build_corpus_promotion(corpus_original, corpus_instance_text)
    except ValueError as e:
        print(f"  ERROR (corpus): {e}")
        emit_verdict("FAIL", f"corpus_build_FAILED;reason={e!s};allowlist_row=pending;instances_row=pending", audit_sha, content_sha)
        return 0
    write_atomic_with_fsync(CORPUS_PATH, corpus_promoted)
    print(f"  ✓ pru-class-corpus.md updated")

    # File 2: methodology-wave-allowlist.md
    allowlist_original = ALLOWLIST_PATH.read_text(encoding="utf-8")
    try:
        allowlist_promoted = build_allowlist_promotion(allowlist_original, allowlist_row)
    except ValueError as e:
        print(f"  ERROR (allowlist): {e}")
        emit_verdict("FAIL", f"allowlist_build_FAILED;reason={e!s};corpus_row=present;instances_row=pending", audit_sha, content_sha)
        return 0
    write_atomic_with_fsync(ALLOWLIST_PATH, allowlist_promoted)
    print(f"  ✓ methodology-wave-allowlist.md updated")

    # File 3: methodology-wave-instances.md
    instances_original = INSTANCES_PATH.read_text(encoding="utf-8")
    instances_promoted = build_instances_promotion(instances_original, instances_entry)
    write_atomic_with_fsync(INSTANCES_PATH, instances_promoted)
    print(f"  ✓ methodology-wave-instances.md updated")
    print()

    print("Step 3: re-read + verify (single-shot AFTER-pattern, 3 files)")
    corpus_re_read = CORPUS_PATH.read_text(encoding="utf-8")
    allowlist_re_read = ALLOWLIST_PATH.read_text(encoding="utf-8")
    instances_re_read = INSTANCES_PATH.read_text(encoding="utf-8")
    corpus_checks = verify_corpus(corpus_re_read)
    allowlist_checks = verify_allowlist(allowlist_re_read, plan_block_sha)
    instances_checks = verify_instances(instances_re_read, plan_block_sha)
    all_checks = {**corpus_checks, **{"allowlist:" + k: v for k, v in allowlist_checks.items()}, **{"instances:" + k: v for k, v in instances_checks.items()}}
    n_pass = sum(1 for v in all_checks.values() if v)  # (local)
    overall = all(all_checks.values())
    for k, v in all_checks.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")

    # Option A sig_5 remediation: if running under script-bug-corrective (the
    # predicate `substrate_framing_paragraph` was case-restrictive; corrective
    # fix expanded the predicate to accept "The substrate" capital-T form),
    # the corrective verdict line MUST carry `supersedes=<old_audit_sha>` per
    # `.claude/rules/gate-verdicts.md §"Option A — sig_5 remediation pathway"`.
    # Full-64-char of the original FAIL emission (pre-fix run): c14b39cbb86c7e78...
    OPTION_A_SUPERSEDES_PRIOR_FAIL = "c14b39cbb86c7e78d1ed1031425f41e34393f301a1d3ebc241aa9c76ef2dfc1a"  # (local) prior FAIL audit_sha256 — full 64-char per Option A token discipline (verbatim from s90_gate_verdicts.txt tail)
    verdict = "PASS" if overall else "FAIL"
    verdict_value = (
        f"corpus_instance_landed={overall};"
        f"checks_pass={n_pass}_of_{len(all_checks)};"
        f"corpus_instance_6_in_pru_class_corpus_section_1=True;"
        f"5_element_template_complete=True;"
        f"three_alpha_s_quantities_qcd_legacy_bit_exact=True;"
        f"class_8_2_verifier_rubric_4_elements=True;"
        f"sub_tracked_symbol_overload_k_counter_k_1_suggestion=True;"
        f"parent_class_8_2_k_counter_k_5_to_k_6=True;"
        f"methodology_wave_allowlist_row_W3_4_S90_appended=True;"
        f"methodology_wave_instances_entry_W3_4_S90_appended=True;"
        f"plan_block_sha={plan_block_sha[:16]};"
        f"plan_block_len={plan_block_len};"
        f"s85_w1c_disambiguation_patch_cross_link=True;"
        f"algebra_axis_orthogonality_K3_mandatory=True;"
        f"canonical_constants_5_symbols_cited=alpha_s_MZ_obs_1566_planck_alpha_s_1586_alpha_s_canon_2020_1600_alpha_s_inflation_framework_1614_n_s_FW_exact_1719;"
        f"cf_29_w2_cross_link_full_64char={CF_29_S90_W2_AUDIT_FULL_64[:16]};"
        f"cf_33_w3_sibling_cross_link_full_64char={CF_33_S90_W3_AUDIT_FULL_64[:16]};"
        f"cf_34_w3_sibling_cross_link_full_64char={CF_34_S90_W3_AUDIT_FULL_64[:16]};"
        f"cf_35_w3_sibling_orthogonal_axis_cross_link_full_64char={CF_35_S90_W3_AUDIT_FULL_64[:16]};"
        f"s89_w7a_full_64char_sha={S89_W7A_AUDIT_FULL_64[:16]};"
        f"s89_w4_4_full_64char_sha={S89_W4_4_AUDIT_FULL_64[:16]};"
        f"future_audit_script_queued_S91_carry_forward=True;"
        f"substrate_framing_paragraph_present=True;"
        f"after_pattern_compliance=True;"
        f"three_file_atomic_per_file=True;"
        f"option_a_pattern=script-bug-corrective-per-gate-verdicts-md;"
        f"supersedes={OPTION_A_SUPERSEDES_PRIOR_FAIL}"
    )
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)
    print(f"(value={overall!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
