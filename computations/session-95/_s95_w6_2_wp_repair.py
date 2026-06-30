#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Repair the §W6-1/§W6-2 region of the W6 working paper after a parallel-writer
cross-section collision.

ROOT CAUSE: the §W6-1 and §W6-2 stubs shared identical boilerplate anchors
("**Output Artifacts** ... YAML)" + the Results-pending sentence). A prior section
writer used str.index on that NON-UNIQUE anchor and matched §W6-1's occurrence, so the
§W6-2 COMPLETED content (Verdict INFO, the BAO transport tables, etc.) landed under the
§W6-1 header, the §W6-2 header was consumed, and §W6-1's own stub body was displaced.

FIX (header-scoped, idempotent, parallel-safe retry):
  - Locate the span from the "### §W6-1." header through the "---" line that precedes the
    "### §W6-3." header. This span currently holds: the §W6-1 header + its Status/GateID/
    Trigger/Class/Agent/Hypothesis/Plan stub lines (intact) FOLLOWED BY the mis-attributed
    §W6-2 BAO body.
  - Rebuild the span as: §W6-1 stub (header + identity + RESTORED pending Output-Artifacts/
    MCP/Verdict/Results boilerplate) + "---" + §W6-2 header + Status COMPLETED + identity +
    the §W6-2 COMPLETED body (lifted verbatim from the current mis-attributed content).
  - The §W6-2 COMPLETED body is detected by its unique first line (the Verdict INFO line)
    through its unique last line (the final Output-Artifacts one-liner).
"""
import time
from pathlib import Path

WP = Path("sessions/archive/session-95/session-95-w6-workingpaper.md").resolve()

H1 = "### §W6-1. CF-S95-N-PBH-MAGNITUDE-RECOMPUTE (mack-cosmic-bridge)"
H3 = "### §W6-3. DE-JOINT-POSTERIOR-RESOURCE (mack-cosmic-bridge)"

# Unique markers bounding the §W6-2 COMPLETED body currently mis-filed under §W6-1.
BODY_FIRST = "**Verdict**: **INFO** (PRE-REGISTERED INFO branch (a):"
BODY_LAST = "**Output Artifacts**: `computations/session-95/s95_w6_2_bao_amplitude_transport.py` / `.npz` / `.png`."

# Restored §W6-1 stub body (PBH boilerplate; agent has not run -> stays NOT STARTED).
W6_1_STUB_BODY = """**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):
*(pending — for each entry in the plan's `output_artifacts:` block: confirm file exists (`ls <path>`) AND paste `grep -E '<must_contain>' <path>` output for every must_contain pattern. Entries: script `computations/session-95/s95_w6_1_n_pbh_magnitude_saturated_tail.py` [must_contain `from canonical_constants import`, `append_verdict`]; data `s95_w6_1_n_pbh_magnitude_saturated_tail.npz` (required); plot `s95_w6_1_n_pbh_magnitude_saturated_tail.png` (required); verdict_line in `computations/session-95/s95_gate_verdicts.txt` [must_contain `^CF-S95-N-PBH-MAGNITUDE-RECOMPUTE:.* audit_sha256=[a-f0-9]{64}`, companion row required, no schema-v2 3-tuple]; wp_section this §W6-1 [Status COMPLETED, Verdict PASS|FAIL|INFO, Output Artifacts, MCP Pre-Compute Audit]. Verification is purely by content presence (regex match), never by line/byte counts.)*

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending agent execution)*
"""

# §W6-1 identity stub lines (already intact in the file; we reuse them verbatim).
W6_1_IDENTITY = """**Status**: NOT STARTED
**Gate ID**: `CF-S95-N-PBH-MAGNITUDE-RECOMPUTE`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (g-axis cardinality-cascade saturated tail of the D_K spectrum; Tier-2 dimensional-re-anchorability gate)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: The §VII.AX m⁻³ Level-3 magnitude, recomputed via the g-axis cardinality-cascade saturated tail at the substrate-singled-out anchor g_saturate=143 (L_max-INDEPENDENT), either re-anchors the HELD m⁻³ row to a substrate-physical scale (PASS) or stays HELD because the truncation-invariant content is dimensionful (dimension and divergence share the same spectral slot) → registry-PASS-INELIGIBLE (INFO/FAIL).
**Plan reference**: `sessions/session-plan/session-95-plan-w6.md` §W6-1 (machinery pin, Tier-1/Tier-2 thresholds, substitution chain source)."""

# §W6-2 identity stub lines (the header + identity that were consumed).
W6_2_HEADER_IDENTITY = """### §W6-2. CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (Layer-2 acoustic excitations; BAO sub-feature is an interference pattern of post-transit GGE excitations; scale-and-channel-tagged)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: The per-gapped-branch Layer-1/Layer-2 BAO sub-feature, transported through the full effacement projection `(c_b²/c_Gold)²` (Gamma_effacement=0.99970; S43 A_FS=0.204 first-sound imprint vs the ~1e-6 effacement floor) to an OBSERVED amplitude δP/P at k~0.043 Mpc⁻¹ and the S43 first-sound ring k1=0.0193 Mpc⁻¹, is either above (PASS) or below (INFO/FAIL) a named experiment's projected amplitude sensitivity — converting the S94 position-only SENSITIVITY bound into an amplitude DETECTION forecast.
**Plan reference**: `sessions/session-plan/session-95-plan-w6.md` §W6-2 (machinery pin, transport-form derivation, substitution chain + [SIGN] 3-tuple source)."""


def attempt():
    txt = WP.read_text(encoding="utf-8")

    # Idempotency: if §W6-2 header already exists AND §W6-1 is NOT-STARTED stub, done.
    if "### §W6-2. CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT" in txt:
        return "already-repaired"

    if H1 not in txt or H3 not in txt:
        return "header-missing"
    if BODY_FIRST not in txt or BODY_LAST not in txt:
        return "body-marker-missing"

    i1 = txt.index(H1)
    i3 = txt.index(H3)
    span = txt[i1:i3]               # from §W6-1 header up to (not incl) §W6-3 header

    # Extract the §W6-2 COMPLETED body verbatim from the mis-attributed span.
    b0 = span.index(BODY_FIRST)
    b1 = span.index(BODY_LAST) + len(BODY_LAST)
    w6_2_body = span[b0:b1]

    # Rebuild the span.
    new_span = (
        H1 + "\n\n"
        + W6_1_IDENTITY + "\n\n"
        + W6_1_STUB_BODY + "\n"
        + "---\n\n"
        + W6_2_HEADER_IDENTITY + "\n\n"
        + w6_2_body + "\n\n"
        + "---\n\n"
    )

    new_txt = txt[:i1] + new_span + txt[i3:]
    WP.write_text(new_txt, encoding="utf-8")
    return "repaired"


res = "init"
for _ in range(8):
    try:
        res = attempt()
    except OSError as e:
        res = f"oserror:{e}"
    if res in ("repaired", "already-repaired"):
        break
    time.sleep(0.4)
print(res)
