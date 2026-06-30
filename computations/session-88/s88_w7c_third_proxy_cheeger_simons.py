"""S88 W7c §W7c-85 — S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS

GEOMETRIC gate: APS-1975 eta-Cheeger-Simons secondary-class third-proxy
INDEPENDENT-CROSS-CHECK at axiom-side c_sub via the band-0 projector
P_0(tau_fold) restriction; completes a 3-route INDEPENDENT-CROSS-CHECK
with tau-flow-trace (S86 W5b-2) and WZW-anomaly-isolating proxy
(S87 W9c-1).

Plan section: sessions/session-plan/session-88-plan-w7c.md  Sec W7c-85
              lines 133-218.

Mechanical-closure handler (this script):
  Per the ORCHESTRATOR OVERRIDE pinned in the dispatch prompt:
    "APS module: phonon-exflation-sim/src/aps_eta_cs.py
     (S88 prereq landing per plan Sec 0.11). If absent at dispatch-time,
     emit PRE-REG-INC per .claude/rules/mechanical-closure-discipline.md
     with value='PRE-REG-INC_blocked_by_S88-CHEEGER-SIMONS-MACHINERY_status_absent'."

  Verification at dispatch-time: phonon-exflation-sim/src/aps_eta_cs.py
  is ABSENT from the canonical path (only the GPE simulation modules
  -- backend, defect_census, diagnostics, expansion, gpe_solver,
  initial_conditions, vortex_detection -- are present in
  phonon-exflation-sim/src/). Per the override, this script emits a
  mechanical PRE-REG-INC closure following all five conditions of
  .claude/rules/mechanical-closure-discipline.md "When mechanical
  closure IS acceptable":

    (1) upstream-block topology: prereq #5 documented in plan
        Sec "Wave 7c Decision Point Prerequisites" item 5.
    (2) verdict honesty: FAIL composite + value='PRE-REG-INC_blocked_*';
        NEVER PASS.
    (3) per-gate-distinct audit_sha256: pinmap includes gate_id +
        per-gate identity keys.
    (4) audit-trail signature: descriptive value names the blocking
        prereq + companion comment row cites the closure-script.
    (5) WP update is in-script (writes Sec W7c-85 in the same run as
        the verdict-line append).

NOTE on the in-session inline precedent
---------------------------------------
S88 W7b-82 landed an APS-1975 eta-Cheeger-Simons evaluator INLINE in
`computations/session-88/s88_w7b_lf_d_cheeger_simons_odd_grading_proxy.py`
(verdict S88-W7-LF-D-CHEEGER-SIMONS-ODD-GRADING-PROXY: PASS at L_max=10
with three odd-grading proxies {CS, GV, eta_CS}). The inline precedent
demonstrates that the MACHINERY content is operational; the absence is
specifically of the canonical PUBLISHED MODULE PATH that the W7c-85
plan pinned (`phonon-exflation-sim/src/aps_eta_cs.py`) for downstream
import re-use.

The inline-vs-canonical-path distinction matters because:
  (a) the canonical path is the structural pin downstream gates would
      import from (no in-script duplication),
  (b) S89-OR-LATER consumers of the third-proxy result need a single
      pinned reference module, and
  (c) the pre-registered Cheeger-Simons module landing closes the
      machinery-feasibility-audit envelope cleanly per
      .claude/rules/math-scripts.md Sec "Machinery-Feasibility Audit".

The orchestrator-override deterministic rule fires UNCONDITIONALLY on
canonical-path-absence; inline precedents do not satisfy the override.

Carry-forward
-------------
  S89-CHEEGER-SIMONS-MACHINERY-LANDING:
    What: extract the W7b-82 inline machinery (eta-invariant +
          Cheeger-Simons + GV-Heitsch evaluators) into a canonical
          import-target module at
          phonon-exflation-sim/src/aps_eta_cs.py with full docstring,
          input-signature spec, and unit-tests against the W7b-82
          PASS values.
    Inputs: s88_w7b_lf_d_cheeger_simons_odd_grading_proxy.py
            (Sec 6 "Odd-grading proxies" -- compute_eta, compute_cs,
            compute_gv, compute_proxies functions).
    Gate: PASS iff the module imports cleanly + reproduces the
          W7b-82 verdict-line value bit-for-bit when re-run on the
          L_max=10 spectrum cache.
    Effort: 0.4 wave-equivalent.

  S89-W7c-85-RE-RUN:
    What: re-execute S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS with the
          S89 canonical APS module imported.
    Inputs: phonon-exflation-sim/src/aps_eta_cs.py (S89 landing);
            s84_spectrum_cache_L12_tau019.npz (L_max=10 truncation);
            canonical_constants.py:c_sub_baseline = 2.238.
    Gate: PASS iff |c_sub_CheegerSimons - c_sub_baseline| / 2.238 < 0.02
          (2 percent tolerance per W7c-85 pre-registration).
    Effort: 0.8 wave-equivalent (matches W7c-85 plan effort).
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Canonical constants (mandatory per .claude/rules/math-scripts.md)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_shared"))
from canonical_constants import M_KK, tau_fold  # noqa: E402

# c_sub_baseline pinned by-value (2.238 per knowledge-MCP get_constant return;
# canonical_constants.py provenance pending S86 W4-2 PROVENANCE block)
c_sub_baseline = 2.238  # (local) substrate-first canonical anchor

# ---------------------------------------------------------------------------
# Section 1 -- Identifiers, paths
# ---------------------------------------------------------------------------

GATE_ID = "S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS"
SCHEME = "eta-Cheeger-Simons-APS-1975-secondary-class-band-0-restricted"
CONVENTION = "axiom-side-CS-third-proxy-INDEPENDENT-CROSS-CHECK-PRIMARY"
L_MAX = 10  # (local) plan W7c-85 canonical truncation
SCHEMA_VERSION = "S87+"

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_PATH = REPO_ROOT / "computations" / "_shared" / "canonical_constants.py"
SPECTRUM_CACHE = REPO_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
APS_MODULE_PATH = REPO_ROOT / "phonon-exflation-sim" / "src" / "aps_eta_cs.py"
INLINE_PRECEDENT = (
    REPO_ROOT / "computations" / "session-88"
    / "s88_w7b_lf_d_cheeger_simons_odd_grading_proxy.py"
)

VERDICT_TXT = REPO_ROOT / "computations" / "session-88" / "s88_gate_verdicts.txt"
NPZ_OUT = REPO_ROOT / "computations" / "session-88" / "s88_w7c_third_proxy_cheeger_simons.npz"
PNG_OUT = REPO_ROOT / "computations" / "session-88" / "s88_w7c_third_proxy_cheeger_simons.png"
JSON_OUT = REPO_ROOT / "computations" / "session-88" / "s88_w7c_third_proxy_cheeger_simons.json"
WP_PATH = REPO_ROOT / "sessions" / "session-88" / "session-88-w7c-workingpaper.md"

# Pre-registered thresholds (plan Sec W7c-85 thresholds)
PASS_BAND = 0.02  # (local) |c_sub_CS - 2.238| / 2.238 < 0.02 PASS
INFO_BAND = 0.01  # (local) 0.01 <= ... < 0.02 INFO
ETA_FN_EPS = 1e-12  # (local) plan machinery pin eta_function_eps

PREREQ_NAME = "S88-CHEEGER-SIMONS-MACHINERY"


# ---------------------------------------------------------------------------
# Section 2 -- Dual-SHA helpers (matches .claude/templates/script-template.py)
# ---------------------------------------------------------------------------

def file_sha256(path: Path) -> str:
    """SHA-256 of a file's bytes (returns 'ABSENT' if path missing)."""
    if not path.exists():
        return "ABSENT"
    h = hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(pins: dict[str, str]) -> tuple[str, str]:
    """audit_sha256 = SHA(script_bytes || canonical_bytes || pinmap_json)
    content_sha256 = SHA(script_bytes)"""
    script_bytes = SCRIPT_PATH.read_bytes()
    canonical_bytes = CANONICAL_PATH.read_bytes()
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit_sha = h_audit.hexdigest()

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content_sha = h_content.hexdigest()
    return audit_sha, content_sha


# ---------------------------------------------------------------------------
# Section 3 -- Prereq verification at dispatch-time
# ---------------------------------------------------------------------------

def verify_prereq_aps_module() -> tuple[bool, str]:
    """Return (present_bool, status_string).

    Per orchestrator override, the canonical APS module path is the
    structural prereq:
        phonon-exflation-sim/src/aps_eta_cs.py

    A full-fidelity check means: the path EXISTS as a regular file
    AND is non-empty. If either condition fails, prereq is absent.
    """
    if not APS_MODULE_PATH.exists():
        return False, "absent_path"
    try:
        size = APS_MODULE_PATH.stat().st_size
    except OSError:
        return False, "absent_stat_error"
    if size == 0:
        return False, "absent_zero_byte"
    if not APS_MODULE_PATH.is_file():
        return False, "absent_not_file"
    return True, "present"


# ---------------------------------------------------------------------------
# Section 4 -- WP Sec W7c-85 update (mechanical-closure-discipline item 5)
# ---------------------------------------------------------------------------

def render_wp_section(verdict_3tuple: tuple[str, str, str],
                      composite: str,
                      audit_sha: str,
                      content_sha: str,
                      pins: dict[str, str],
                      prereq_status: str) -> str:
    """Render the substantive Sec W7c-85 working-paper text.

    Per .claude/rules/mechanical-closure-discipline.md Sec "When mechanical
    closure IS acceptable" item 5, the closure script MUST update the
    working-paper Sec status, verdict, results, and substrate-framing
    blocks IN THE SAME RUN as the verdict-line append.
    """
    sign_v, mag_v, regime_v = verdict_3tuple

    return f"""### §W7c-85. S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS (lizzi-spectral-functional-theorist)

**Status**: CLOSED-PRE-REG-INC (mechanical closure per `.claude/rules/mechanical-closure-discipline.md`)
**Gate ID**: `{GATE_ID}`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (Cheeger-Simons secondary-class third-proxy INDEPENDENT-CROSS-CHECK at axiom-side c_sub via APS-1975 η-invariant)
**Agent**: `lizzi-spectral-functional-theorist` PRIMARY + `connes-ncg-theorist` CO-AUTHOR (Chern-Simons → Cheeger-Simons NCG-axiomatic lift per Connes-Moscovici 1995 §III.4 dim-spectrum residue formula; cited in this section, no separate dispatch per orchestrator override)
**Hypothesis**: η-Cheeger-Simons secondary class on the band-0 projector P_0(τ_fold) provides a third independent c_sub probe converging to c_sub_baseline = 2.238 at <2% tolerance, completing a 3-route INDEPENDENT-CROSS-CHECK with τ-flow-trace (S86 W5b-2) and WZW-anomaly-isolating proxy (S87 W9c-1).
**Plan reference**: `sessions/session-plan/session-88-plan-w7c.md` §W7c-85.

**MCP Pre-Compute Audit**:

- `mcp__knowledge__.get_constant('c_sub_baseline')` → value = 2.238 (no PROVENANCE; sourced from canonical_constants.py per S86 W4-2).
- `mcp__knowledge__.get_constant('tau_fold')` → value = 0.19 (S12/S42; gate `CONST-FREEZE-42`; substrate-first canonical anchor).
- `mcp__knowledge__.get_constant('M_KK')` → value = 7.428660036284456e+16 GeV.
- `mcp__knowledge__.trace_entity('eta invariant')` → 4 gates + 1 theorem + 5 equations: η(D_K) = 0 PROVEN structural identity by BDI ±-pair; `S85-CC-1-ETA-INVARIANT-FULL-TRIPLE` INFO at L_max=8 scheme=APS-1975; `S88-W7-LF-D-CHEEGER-SIMONS-ODD-GRADING-PROXY` PASS at L_max=10 (inline APS-1975 secondary-class machinery operational at this session).
- `mcp__knowledge__.search_knowledge('APS 1975 boundary contribution band-0 projector')` → 5 hits including `Δ S_APS = π · SF(D_K; τ_1, τ_2)` (S25), `sf(D_0, D_{{tau_fold}}) = index(d/dt + D_t)` (S61), and W3c-WP eta-invariant entry. The band-0 projector at τ_fold is gapped by Δ_B2 = 0.7704 M_KK (s86-hp1-cohomology-quantum-metric-bridge §"At τ = τ_fold").
- PRE-CLOSED status: NO. The third-proxy structural reading is novel at S88; downstream registry write to §VII.AH.2 is gated on this closure.

**Prerequisite verification at dispatch-time** (per plan §"Wave 7c Decision Point Prerequisites" item 5):

| Prereq | Canonical path | Status |
|:-------|:---------------|:------:|
| #5 APS module | `phonon-exflation-sim/src/aps_eta_cs.py` | **`{prereq_status}`** |

The orchestrator override is unambiguous: *"If absent at dispatch-time, emit PRE-REG-INC per `.claude/rules/mechanical-closure-discipline.md` with value=`'PRE-REG-INC_blocked_by_S88-CHEEGER-SIMONS-MACHINERY_status_absent'`."*

Direct check at dispatch time confirmed: `phonon-exflation-sim/src/` contains only the GPE simulation modules (`backend.py`, `defect_census.py`, `diagnostics.py`, `expansion.py`, `gpe_solver.py`, `initial_conditions.py`, `vortex_detection.py`) plus `__init__.py` and `__pycache__/`. No `aps_eta_cs.py` is present.

The mechanical closure path of `.claude/rules/mechanical-closure-discipline.md` §"When mechanical closure IS acceptable" applies because all five conditions hold:

1. **Upstream-block topology is the cause** — the W7c-85 plan §"Wave 7c Decision Point Prerequisites" item 5 explicitly anticipated this scenario ("if absent, route #85 to PRE-REG-INC blocked-by-S88-CHEEGER-SIMONS-MACHINERY"). The plan author pre-registered the deferred outcome; this is NOT post-hoc plan editing.
2. **Verdict honesty** — emit FAIL composite with value `'PRE-REG-INC_blocked_by_{PREREQ_NAME}_status_absent'`. NEVER PASS. The composite is FAIL because the prereq-block prevents the substantive computation; the magnitude/sign/regime fields are encoded as N/A-with-blocked annotation.
3. **Per-gate-distinct audit_sha256** — the input pin map embeds `_gate_id`, `_wp_id`, `_scheme`, `_convention`, `_blocked_prereq`, ensuring `audit_sha256={audit_sha[:16]}…` is unique against all prior verdict-file entries.
4. **Audit-trail signature** — the canonical verdict-line value names the blocking prereq (`{PREREQ_NAME}`) + status (`absent`); the companion comment row cites the closure-script path; the descriptive WP §W7c-85 entry below names both the canonical path and the in-session inline precedent.
5. **Working-paper update is in-script** — this WP §W7c-85 text is rendered and written by the producing script in the same run as the verdict-line append.

**Verdict**:

```
{GATE_ID}: {composite} -- value='PRE-REG-INC_blocked_by_{PREREQ_NAME}_status_absent;canonical_path=phonon-exflation-sim/src/aps_eta_cs.py;in_session_inline_precedent=computations/session-88/s88_w7b_lf_d_cheeger_simons_odd_grading_proxy.py;deferred_to_S89' scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} audit_sha256={audit_sha} content_sha256={content_sha} schema_version={SCHEMA_VERSION}
```

Composite: **{composite}** (per `.claude/rules/gate-verdicts.md` S87+ collapse rule with `regime_verdict=BREAKDOWN-PREREQ-BLOCKED` ⇒ composite = FAIL; the BREAKDOWN regime distinguishes mechanical PRE-REG-INC from a substantively FAIL'd numerical comparison).

3-tuple annotation: `sign={sign_v}` `magnitude={mag_v}` `regime={regime_v}`.

**Results**:

- **value** (4-tuple, mechanical-closure form):
  - `value` = `PRE-REG-INC_blocked_by_{PREREQ_NAME}_status_absent` (per orchestrator override + plan §"Wave 7c Decision Point Prerequisites" item 5 deterministic rule).
  - `scheme` = `{SCHEME}` (preserves the plan §W7c-85 4-tuple scheme tag for downstream cross-cite).
  - `convention` = `{CONVENTION}` (PRIMARY level; SCHEMATIC FORBIDDEN per `.claude/rules/substrate-first-canonical-sourcing.md` §(iv); the convention tag ENCODES PRIMARY for forward consumers even though the substantive numerical evaluation is deferred).
  - `L_max` = `{L_MAX}` (plan-pinned canonical L_max; W11-3 Friedrich-Bär saturation theorem applicable at this truncation).

- **CC1 — η-function analytic continuation to s=0 (eta_function_eps = 1e-12)**: NOT EVALUATED (gate blocked at prereq landing). The structural form is pre-registered:

  ```
  η_D(s) := ∑_{{λ ∈ spec(D_K) \\ {{0}}}} sign(λ) · |λ|^{{−s}}
  CS_2(D_K) := (1/2) · η_D(0) + (1/2) · dim(ker D_K)  mod ℤ
  ```

  Under the BDI ±-pair preservation theorem (proved at S60 ETA-INVARIANT-60 PASS; S86 W-11 Bulletin #2 STRENGTHENED to all even-grading regulator-weighted Mellin moments), each |λ| in the L_max=10 cache appears with equal +/− signed multiplicity ⇒ the sign-sum at s=0 is EXACTLY zero ⇒ η_D(0) = 0 EXACTLY at machine epsilon. The CS_2 evaluation therefore reduces to (1/2) · dim(ker D_K) mod ℤ. The S88 W7b-82 inline precedent verified this at L_max=10 with `eta_diff = 0.00e+00`.

- **CC2 — R/Z → R lift normalization at substrate-first canonical anchor**: NOT EVALUATED. The structural form is pre-registered:

  ```
  c_sub_CheegerSimons := lift_R(CS_2_band0; baseline = c_sub_baseline = 2.238)
  ```

  The R/Z lift is fixed by the substrate-first canonical anchor (NOT a free choice); per `.claude/rules/substrate-first-canonical-sourcing.md` the anchor IS `c_sub_baseline = 2.238` from canonical_constants.py (provenance: S86 W4-2). The lift normalizes the secondary class such that the m=0 sheet contains the substrate-derived baseline; m=±1, ±2, … sheets are unphysical extensions excluded by the canonical-anchor pin.

- **Substitution chain (mandatory per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute")** — mechanical-closure form with substituted numbers:

  ```
  Step 1 (definition):   prereq_5 := canonical-path-existence(
                            phonon-exflation-sim/src/aps_eta_cs.py)
                         override_rule := orchestrator-override({{
                            "If absent at dispatch-time, emit PRE-REG-INC..."
                         }})
  Step 2 (substitution): prereq_5(observed) = ABSENT
                            (verified Glob + ls; only GPE modules in src/)
                         override_rule(prereq_5 = ABSENT) ⟹ PRE-REG-INC
  Step 3 (simplification):
                         composite_collapse := (regime_verdict =
                            BREAKDOWN-PREREQ-BLOCKED) ⟹ composite = FAIL
                            (per .claude/rules/gate-verdicts.md S87+ schema-v2
                             composite-collapse rule)
  Step 4 (canonical form):
                         FAIL value-string  := PRE-REG-INC_blocked_by_{PREREQ_NAME}_status_absent
  Step 5 (cross-check substituted numbers):
                         L_max_pin = {L_MAX} (plan-pinned)
                         c_sub_baseline = 2.238 (mcp__knowledge__.get_constant)
                         eta_function_eps = {ETA_FN_EPS} (plan machinery pin §0.11)
                         tau_fold = 0.19 (mcp__knowledge__.get_constant)
                         M_KK = 7.428660036284456e+16 GeV (mcp__knowledge__.get_constant)
                         APS_module_status = ABSENT
                         inline_precedent_status = PRESENT (W7b-82 PASS at L_max=10)
  Step 6 (direction):    canonical-path absent ⟹ orchestrator-override fires
                         ⟹ FAIL composite + PRE-REG-INC value-string
                         ⟹ §VII.AH.2 registry-write BLOCKED at this session
                         ⟹ carry-forward to S89-CHEEGER-SIMONS-MACHINERY-LANDING
                            + S89-W7c-85-RE-RUN
  Direction: prereq absent ⟹ FAIL composite + PRE-REG-INC ⟹ defer
  Conclusion: FAIL-with-mechanical-closure; numerical c_sub_CheegerSimons
              evaluation at L_max=10 deferred to S89; inline precedent at
              W7b-82 demonstrates machinery is operational; canonical-path
              landing closes the prereq.
  ```

- **5-element IS-not-IN substrate-framing block** (per `.claude/rules/cross-pillar-bridge-anatomy.md` §"IS-not-IN Anatomy" + plan §W7c-85):
  1. **Substrate-IS observable** (deferred-to-S89): `c_sub_CheegerSimons` evaluated on `(A_K^{{≤10}}, H_K^{{≤10}}, D_K^{{≤10}})` via η-Cheeger-Simons secondary class CS_2 restricted to band-0 projector P_0(τ_fold) — the substrate IS this Mellin-secondary-class probe at the axiom-side c_sub region.
  2. **Laboratory-IN observable**: N/A (substrate-internal probe; this gate is not a cross-pillar bridge entry per plan §W7c-85 substrate framing).
  3. **Bridge map**: N/A (no cross-pillar bridge map invoked at this gate; the INDEPENDENT-CROSS-CHECK is intra-substrate across three regulator-class probes).
  4. **Algebraic envelope**: Friedrich-Bär saturation at L_max=10 per W11-3 (bottom-K observable structurally L_max-saturated; no L^{{−α}} envelope required at this truncation).
  5. **Empirical anchor**: c_sub_baseline = 2.238 from canonical_constants.py (substrate-first canonical sourcing PASS per `.claude/rules/substrate-first-canonical-sourcing.md` §(iii) W0c-3 worked-example pattern).

- **INDEPENDENT-CROSS-CHECK structure declaration** (per `.claude/rules/registry-landing.md` §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)" item 1: parallel route, NOT sequential dependency):

  The three c_sub probes form a PARALLEL-INDEPENDENT-VERIFY structure (NOT SOURCE-DOUBLE-CITE-CO-PRIMARY which would require sequential V_input → C_output dependency):

  | Route | Probe | Source | Status |
  |:------|:------|:-------|:-------|
  | (i) τ-flow-trace | `c_sub_tau_flow_trace` | S86 W5b-2 INFO (verdict at `computations/session-86/s86_gate_verdicts.txt:138`) | LANDED-INFO |
  | (ii) WZW-anomaly-isolating | `c_sub_anomaly_WZW` | S87 W9c-1 SCHEMATIC FAIL Track-A (verdict at `computations/session-87/s87_gate_verdicts.txt:262`) | LANDED-SCHEMATIC-FAIL |
  | (iii) η-Cheeger-Simons (this gate) | `c_sub_CheegerSimons` | S88 W7c-85 PRE-REG-INC | DEFERRED-S89 |

  Each route uses a structurally distinct regulator class (τ-flow-trace = curvature-flow integration; WZW-anomaly = Mellin-residue at axiom-side anomaly pole; CS = APS-1975 secondary class). Route independence is preserved by construction: no route's input is another route's output. Per `.claude/rules/registry-landing.md`: "If two anchors are independently reproducing the same conclusion via DIFFERENT routes (parallel, not sequential), use PRIMARY + INDEPENDENT-CROSS-CHECK instead. The two patterns are distinct."

  Registry-write to `permanent-results-registry.md` §VII.AH.2 (3-route convergence as structural theorem) is BLOCKED at S88 pending route (iii) substantive landing at S89.

- **Forward S89 carry-forward (4-field spec per `feedback_fix-in-session-never-defer.md`)**:

  1. **`S89-CHEEGER-SIMONS-MACHINERY-LANDING`**:
     - **What**: extract the W7b-82 inline machinery (`compute_eta`, `compute_cs`, `compute_gv`, `compute_proxies`) into the canonical import-target module `phonon-exflation-sim/src/aps_eta_cs.py` with full docstring, input-signature spec, and unit-tests against the W7b-82 PASS values.
     - **Inputs**: `computations/session-88/s88_w7b_lf_d_cheeger_simons_odd_grading_proxy.py` §6 functions; `computations/session-84/s84_spectrum_cache_L12_tau019.npz`; `canonical_constants.py:gv_canonical_difference_FW = -40579.1500479506`.
     - **Gate**: PASS iff the module imports cleanly + reproduces W7b-82 verdict-line value bit-for-bit when re-run on the L_max=10 spectrum cache.
     - **Effort**: 0.4 wave-equivalent.

  2. **`S89-W7c-85-RE-RUN`**:
     - **What**: re-execute `S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS` with the S89 canonical APS module imported; evaluate `c_sub_CheegerSimons` per plan §W7c-85 method steps 1–6.
     - **Inputs**: `phonon-exflation-sim/src/aps_eta_cs.py` (S89 landing); `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (L_max=10 truncation); `canonical_constants.py:c_sub_baseline = 2.238`.
     - **Gate**: PASS iff `|c_sub_CheegerSimons − 2.238| / 2.238 < 0.02` (2% tolerance per W7c-85 pre-registration).
     - **Effort**: 0.8 wave-equivalent (matches W7c-85 plan effort).

**Files produced**:

| Artifact | Path | Size |
|:---------|:-----|-----:|
| Producing script | `computations/session-88/s88_w7c_third_proxy_cheeger_simons.py` | <see disk> |
| NPZ data | `computations/session-88/s88_w7c_third_proxy_cheeger_simons.npz` | <see disk> |
| PNG plot | `computations/session-88/s88_w7c_third_proxy_cheeger_simons.png` | <see disk> |
| JSON metadata | `computations/session-88/s88_w7c_third_proxy_cheeger_simons.json` | <see disk> |
| Verdict line | `computations/session-88/s88_gate_verdicts.txt` (canonical S88; per `.claude/rules/gate-verdicts.md`) | append |

**Dual-SHA pin** (per `.claude/rules/gate-verdicts.md` S87+ schema-v2 + W9a-99 split):
- `audit_sha256` = `{audit_sha}` (SHA over script-bytes ‖ canonical_bytes ‖ pin-map JSON; per-gate-distinct via gate-id key).
- `content_sha256` = `{content_sha}` (SHA over script-bytes only).

**3-tuple annotation** (S87 schema-v2 second companion row):
- `sign_verdict` = `{sign_v}` (no directional pre-registration applies under PRE-REG-INC; the substantive numerical comparison is deferred to S89).
- `magnitude_verdict` = `{mag_v}` (same; magnitude-comparison `|c_sub_CS − 2.238|` is not evaluated at this session).
- `regime_verdict` = `{regime_v}` (BREAKDOWN regime distinguishes mechanical PRE-REG-INC from substantive numerical FAIL; per `.claude/rules/gate-verdicts.md` collapse rule, BREAKDOWN ⟹ composite = FAIL even when sign/magnitude are N/A).

---
"""


# ---------------------------------------------------------------------------
# Section 5 -- Plot (mechanical-closure visualization)
# ---------------------------------------------------------------------------

def make_plot(out_path: Path,
              prereq_status: str,
              audit_sha_short: str) -> None:
    """Render a 2-panel plot:
       Panel A -- 3-route INDEPENDENT-CROSS-CHECK status table
       Panel B -- mechanical-closure decision flow
    """
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.4))

    # Panel A: 3-route INDEPENDENT-CROSS-CHECK status
    ax = axes[0]
    routes = ["(i) τ-flow-trace\nS86 W5b-2", "(ii) WZW-anomaly\nS87 W9c-1", "(iii) η-Cheeger-Simons\nS88 W7c-85 (this)"]
    statuses = ["LANDED\nINFO", "LANDED\nSCHEMATIC FAIL", "DEFERRED\nS89 PRE-REG-INC"]
    colors = ["#7ab84a", "#d24a4a", "#a0a0a0"]
    bar_heights = [1.0, 1.0, 1.0]
    bars = ax.bar(routes, bar_heights, color=colors, alpha=0.85, edgecolor="black")
    for bar, status in zip(bars, statuses):
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, h * 0.5,
                status, ha="center", va="center", fontsize=10, fontweight="bold")
    ax.set_ylim(0, 1.4)
    ax.set_ylabel("Route landing status (1 = landed)")
    ax.set_title("3-route INDEPENDENT-CROSS-CHECK at axiom-side c_sub\n(target: c_sub_baseline = 2.238 ± 2%)")
    ax.set_yticks([])

    # Panel B: mechanical-closure decision flow
    ax = axes[1]
    ax.axis("off")
    flow_text = (
        "Mechanical-closure decision flow\n"
        "(per .claude/rules/mechanical-closure-discipline.md)\n\n"
        "Step 1: Verify prereq #5\n"
        "    canonical path: phonon-exflation-sim/src/aps_eta_cs.py\n"
        f"    observed status: {prereq_status}\n\n"
        "Step 2: Apply orchestrator override\n"
        "    rule: 'If absent at dispatch-time, emit PRE-REG-INC...'\n"
        "    fires UNCONDITIONALLY on canonical-path absence\n\n"
        "Step 3: Compose verdict\n"
        "    composite: FAIL (per gate-verdicts.md collapse rule:\n"
        "        regime=BREAKDOWN-PREREQ-BLOCKED ⟹ FAIL)\n"
        "    value: PRE-REG-INC_blocked_by_S88-CHEEGER-SIMONS-\n"
        "        MACHINERY_status_absent\n\n"
        "Step 4: Carry-forward\n"
        "    S89-CHEEGER-SIMONS-MACHINERY-LANDING (0.4 wave-eq)\n"
        "    S89-W7c-85-RE-RUN (0.8 wave-eq)\n\n"
        f"audit_sha256: {audit_sha_short}…"
    )
    ax.text(0.0, 0.98, flow_text, ha="left", va="top",
            family="monospace", fontsize=9.5, transform=ax.transAxes)

    fig.suptitle(
        f"§W7c-85  {GATE_ID}  L_max={L_MAX}\n"
        f"Mechanical PRE-REG-INC closure — substantive evaluation deferred to S89",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    fig.savefig(out_path, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    print(f"[{GATE_ID}] start")
    print(f"  script: {SCRIPT_PATH}")
    print(f"  canonical: {CANONICAL_PATH}")
    print(f"  spectrum cache: {SPECTRUM_CACHE} (exists: {SPECTRUM_CACHE.exists()})")
    print(f"  APS module: {APS_MODULE_PATH}")
    print(f"  inline precedent: {INLINE_PRECEDENT}")

    # --- Section 3 prereq verification
    aps_present, aps_status = verify_prereq_aps_module()
    print(f"  prereq #5 (APS module) status: {aps_status} (present={aps_present})")

    if aps_present:
        # If the canonical APS module ever lands, this script's mechanical-
        # closure path becomes inapplicable; the script should be re-routed
        # to the substantive computation. Emit a diagnostic and abort.
        print(f"  ERROR: aps_eta_cs.py is present at canonical path; this "
              f"closure script handles the absent-prereq case only. "
              f"Route to substantive S89-W7c-85-RE-RUN.")
        return 2

    # --- Section 4 prereqs are absent: enter mechanical-closure path
    composite = "FAIL"  # (local) per gate-verdicts.md S87+ collapse on regime=BREAKDOWN-PREREQ-BLOCKED
    sign_v = "N/A"  # (local) no directional pre-registration applies under PRE-REG-INC
    mag_v = "N/A"  # (local) substantive magnitude-comparison deferred
    regime_v = "BREAKDOWN-PREREQ-BLOCKED"  # (local) distinguishes mechanical from numerical FAIL

    # --- Input pin map (file SHAs)
    cache_sha = file_sha256(SPECTRUM_CACHE)
    canonical_sha = file_sha256(CANONICAL_PATH)
    aps_sha = file_sha256(APS_MODULE_PATH)  # 'ABSENT'
    inline_sha = file_sha256(INLINE_PRECEDENT)

    pins = {
        # File-SHA pins (5-class file-pin taxonomy per pru-pre-registration-template.md)
        str(SPECTRUM_CACHE.relative_to(REPO_ROOT)).replace("\\", "/"): cache_sha,
        str(CANONICAL_PATH.relative_to(REPO_ROOT)).replace("\\", "/"): canonical_sha,
        str(APS_MODULE_PATH.relative_to(REPO_ROOT)).replace("\\", "/"): aps_sha,
        str(INLINE_PRECEDENT.relative_to(REPO_ROOT)).replace("\\", "/"): inline_sha,
        # Per-gate-distinct identity keys (mechanical-closure-discipline item 3)
        "_gate_id": GATE_ID,
        "_wp_id": "session-88-w7c-workingpaper.md#W7c-85",
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_blocked_prereq": PREREQ_NAME,
        "_blocked_status": aps_status,
        # Constants pinned by-value for audit traceability
        "_const:c_sub_baseline": f"{c_sub_baseline!r}",
        "_const:tau_fold": f"{tau_fold!r}",
        "_const:M_KK": f"{M_KK!r}",
        "_const:L_max": f"{L_MAX}",
        "_const:PASS_BAND": f"{PASS_BAND!r}",
        "_const:INFO_BAND": f"{INFO_BAND!r}",
        "_const:ETA_FN_EPS": f"{ETA_FN_EPS!r}",
    }
    print(f"  cache SHA          : {cache_sha[:16]}...")
    print(f"  canonical SHA      : {canonical_sha[:16]}...")
    print(f"  APS module SHA     : {aps_sha} (ABSENT marker)")
    print(f"  inline precedent SHA: {inline_sha[:16]}...")

    # --- 4-tuple value field (mechanical-closure form)
    value_str = (
        f"PRE-REG-INC_blocked_by_{PREREQ_NAME}_status_absent;"
        f"canonical_path=phonon-exflation-sim/src/aps_eta_cs.py;"
        f"in_session_inline_precedent=computations/session-88/s88_w7b_lf_d_cheeger_simons_odd_grading_proxy.py;"
        f"deferred_to_S89"
    )
    print(f"  value: {value_str}")

    # --- Persist NPZ data (mechanical-closure metadata)
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        composite=composite,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        prereq_aps_module_status=aps_status,
        prereq_aps_module_present=int(aps_present),
        canonical_path=str(APS_MODULE_PATH),
        inline_precedent_path=str(INLINE_PRECEDENT),
        c_sub_baseline=c_sub_baseline,
        eta_function_eps=ETA_FN_EPS,
        tau_fold=tau_fold,
        M_KK=M_KK,
        pass_band=PASS_BAND,
        info_band=INFO_BAND,
    )
    print(f"  saved data: {NPZ_OUT}")

    # --- Compute dual-SHA (after NPZ written so script-bytes are stable)
    audit_sha, content_sha = compute_dual_sha(pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")

    # --- Plot (visualizes 3-route INDEPENDENT-CROSS-CHECK + decision flow)
    make_plot(PNG_OUT, aps_status, audit_sha[:16])
    print(f"  saved plot: {PNG_OUT}")

    # --- JSON metadata sidecar
    json_payload = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "composite": composite,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "prereq_aps_module_status": aps_status,
        "prereq_aps_module_path": str(APS_MODULE_PATH),
        "inline_precedent_path": str(INLINE_PRECEDENT),
        "value_str": value_str,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": SCHEMA_VERSION,
        "c_sub_baseline": c_sub_baseline,
        "thresholds": {
            "PASS_band": PASS_BAND,
            "INFO_band": INFO_BAND,
            "eta_function_eps": ETA_FN_EPS,
        },
        "carry_forward": [
            {
                "id": "S89-CHEEGER-SIMONS-MACHINERY-LANDING",
                "what": "extract W7b-82 inline machinery into canonical phonon-exflation-sim/src/aps_eta_cs.py",
                "inputs": [
                    "computations/session-88/s88_w7b_lf_d_cheeger_simons_odd_grading_proxy.py",
                    "computations/session-84/s84_spectrum_cache_L12_tau019.npz",
                    "canonical_constants.py:gv_canonical_difference_FW",
                ],
                "gate": "PASS iff module imports + reproduces W7b-82 verdict-line bit-for-bit at L_max=10",
                "effort_wave_equiv": 0.4,
            },
            {
                "id": "S89-W7c-85-RE-RUN",
                "what": "re-execute S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS with canonical APS module",
                "inputs": [
                    "phonon-exflation-sim/src/aps_eta_cs.py (S89 landing)",
                    "computations/session-84/s84_spectrum_cache_L12_tau019.npz",
                    "canonical_constants.py:c_sub_baseline",
                ],
                "gate": "PASS iff |c_sub_CheegerSimons - 2.238| / 2.238 < 0.02",
                "effort_wave_equiv": 0.8,
            },
        ],
        "independent_cross_check_routes": [
            {"route": "(i)", "probe": "tau-flow-trace", "source": "S86 W5b-2", "status": "LANDED-INFO"},
            {"route": "(ii)", "probe": "WZW-anomaly-isolating", "source": "S87 W9c-1", "status": "LANDED-SCHEMATIC-FAIL"},
            {"route": "(iii)", "probe": "eta-Cheeger-Simons", "source": "S88 W7c-85", "status": "DEFERRED-S89"},
        ],
        "input_pin_map": {k: v for k, v in sorted(pins.items())},
    }
    with JSON_OUT.open("w", encoding="utf-8") as fp:
        json.dump(json_payload, fp, indent=2, sort_keys=True)
    print(f"  saved JSON: {JSON_OUT}")

    # --- Render & write WP §W7c-85 (mechanical-closure-discipline item 5)
    wp_section_text = render_wp_section(
        verdict_3tuple=(sign_v, mag_v, regime_v),
        composite=composite,
        audit_sha=audit_sha,
        content_sha=content_sha,
        pins=pins,
        prereq_status=aps_status,
    )
    # Read entire WP and replace §W7c-85 stub block (between the ### header and the next ### header / EOF)
    wp_full = WP_PATH.read_text(encoding="utf-8")
    sec_start_marker = "### §W7c-85. S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS"
    sec_end_marker = "### §W7c-86."  # next section header
    start_idx = wp_full.find(sec_start_marker)
    end_idx = wp_full.find(sec_end_marker)
    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        raise RuntimeError(
            f"WP {WP_PATH}: cannot locate §W7c-85 stub between markers; "
            f"start_idx={start_idx} end_idx={end_idx}"
        )
    wp_new = (
        wp_full[:start_idx]
        + wp_section_text
        + wp_full[end_idx:]
    )
    WP_PATH.write_text(wp_new, encoding="utf-8")
    print(f"  updated WP §W7c-85: {WP_PATH}")

    # --- Append verdict line + dual-SHA companion + 3-tuple companion
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    triple_companion = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    # Mechanical-closure audit-trail signature comment (item 4 + item 1)
    closure_trail_comment = (
        f"# # PRE-REG-INC per session-88-plan-w7c.md §W7c-85 + "
        f"§\"Wave 7c Decision Point Prerequisites\" item 5; deferred to S89; "
        f"required prereqs: [{PREREQ_NAME} = phonon-exflation-sim/src/aps_eta_cs.py]; "
        f"closure_script=computations/session-88/s88_w7c_third_proxy_cheeger_simons.py\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_companion)
        fp.write(triple_companion)
        fp.write(closure_trail_comment)
    print(f"  appended verdict + companions to {VERDICT_TXT}")

    print(f"[{GATE_ID}] complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
