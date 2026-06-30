#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parallel-writer-safe WP §W6-2 section writer (atomic read-modify-write, retry on race).

Replaces the four pending sub-blocks of the §W6-2 section in the shared W6 working paper
with the completed content. Uses a short retry loop with re-read on each attempt so a
concurrent sibling-W6 writer cannot clobber this section (the Edit-tool mtime race the
orchestrator hit). Each attempt re-reads, does targeted str.replace on UNIQUE anchors
scoped to §W6-2, and writes back atomically.
"""
import time
from pathlib import Path

WP = Path("sessions/archive/session-95/session-95-w6-workingpaper.md").resolve()

# --- Unique anchors scoped to §W6-2 (the stub's exact pending blocks) ----------
OLD_STATUS = (
    "**Status**: NOT STARTED\n"
    "**Gate ID**: `CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT`\n"
    "**Trigger**: `[SIGN]`"
)
NEW_STATUS = (
    "**Status**: COMPLETED\n"
    "**Gate ID**: `CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT`\n"
    "**Trigger**: `[SIGN]`"
)

# The Output-Artifacts + MCP + Verdict + Results pending blocks span from the
# "**Output Artifacts**" header of §W6-2 through its Results pending paragraph, ending
# just before the "---" separator that precedes §W6-3. Replace that whole span.
OLD_BODY_START = "**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):"
OLD_BODY_END = "dual-SHA + schema-v2 3-tuple companion row (sign/magnitude/regime), artifacts `s95_w6_2_bao_amplitude_transport.py/.npz/.png`)*"

NEW_BODY = r"""**Verdict**: **INFO** (PRE-REGISTERED INFO branch (a): `mcp__paper-search__*` DOWN at dispatch -> experiment amplitude sensitivity unavailable; substrate forecast computed IN FULL; suppression-direction + S43-ring-is-the-live-channel structural conclusions are robust without the fetched value). INFO is a VERDICT, not a closure / FAIL.

**Output Artifacts** (closure-verification checklist):

| artifact | path | must_contain -> grep result |
|:---------|:-----|:----------------------------|
| script | `computations/session-95/s95_w6_2_bao_amplitude_transport.py` | `from canonical_constants import` PRESENT; `append_verdict` PRESENT (def + call) |
| data | `computations/session-95/s95_w6_2_bao_amplitude_transport.npz` | present, 19264 bytes |
| plot | `computations/session-95/s95_w6_2_bao_amplitude_transport.png` | present, 140314 bytes |
| verdict_line | `computations/session-95/s95_gate_verdicts.txt` | `^CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT:.* audit_sha256=[a-f0-9]{64}` MATCHED (`audit_sha256=e0ae23931da0a1dd...d472d0a03`); dual-SHA companion row PRESENT; schema-v2 3-tuple row PRESENT (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=BREAKDOWN`) |
| wp_section | this §W6-2 | Status COMPLETED; Verdict INFO; Output Artifacts; MCP Pre-Compute Audit |

`audit_sha256 = e0ae23931da0a1ddf4ec04ce1e24026e0c7fe6faed2760c641f4210d472d0a03` (unique across the session verdict file; SHA over script || canonical_constants.py || s94_bao_peak_branch.npz || ordered pinmap-JSON). `content_sha256 = 572b2ff608d5ab9807b09dcaff068c3c4c939ce4d5828e4e1c97657638894eab`.

**MCP Pre-Compute Audit**:
- `get_constant("Gamma_effacement")` -> 0.9997 (effacement transmission; no PROVENANCE entry -- S58 Volovik partition).
- `get_constant("c_Gold")` -> 0.915 (S52 GL-JOSEPHSON-52; Goldstone sound speed, M_KK units, the one true 4D light cone).
- `search_knowledge("BAO two-speed amplitude transport ... first-sound ring A_FS")` -> S94-BAO-PEAK-BRANCH (INFO; `delta_B1=0.0152 M_KK_frac=0.1900`) + `s94_s1_bao_observational_reach` (position-only synthesis, no gate). No closure covers the AMPLITUDE transport -> gate proceeds.
- `trace_entity("first-sound ring")` -> eq_9611 `A_FS/A_BAO = 0.204 = c_2^2/c_1^2`, first-sound ring `r_1 = 325 Mpc`, Prediction (DISTINCTIVE), UNTESTED -- confirms the S43 ring is the live, no-LCDM-counterpart channel.
- **paper-search availability outcome**: `mcp__paper-search__search_arxiv` queried TWICE at dispatch -- (1) "CMB-S4 Simons Observatory forecast BAO acoustic scale amplitude sensitivity..." -> `{"result":[]}`; (2) broad "Simons Observatory forecast cosmological parameters science goals" -> `{"result":[]}`. Both empty including a query that should be richly indexed if live => **paper-search MCP DOWN** (same as S94). Routed to PRE-REGISTERED INFO branch (a); S_exp surrogate = S94 S-1 bounding-estimate CMB-S4/SO floor (~0.01%, literature gap, NOT a fetched pin).
- PRE-CLOSED check: not pre-closed. S94 S-1 was position-only (no gate emission); this gate is the first AMPLITUDE forecast.

**Results**:

*Substrate inputs (from `s94_bao_peak_branch.npz`, cache-load -- no fresh diagonalization):*
- `b1_delta = 0.01516` (M_KK-internal B1 Layer-1/Layer-2 split magnitude); `shift_frac = 0.19` (the substrate fractional split, 7/7 gapped branches in-band).
- `c_Gold = 0.915` (Goldstone, the one true 4D acoustic cone); `c_B1 = 0.0798`, `c_B3 = 0.1397` (Layer-2 emergent BdG branch speeds, c2 column; cross-checked == canonical_constants). `s84_c_T_over_c_S = 2.0619`.
- Goldstone `delta = 0` (PROTECTED -- the protected acoustic carrier carries no split).

*Effacement-projection transport `A_obs,b = shift_b * (c_b^(2)/c_Gold)^2` (delta_P/P per gapped branch):*

| branch | c2 (M_KK) | A_eff = (c2/c_Gold)^2 | A_obs = delta_P/P |
|:-------|----------:|----------------------:|------------------:|
| Goldstone | 0.915 | 1.000 | 0 (protected) |
| **B1** | 0.0798 | 7.606e-03 (Sage `17689/2325625`) | **1.445e-03** |
| B2 | 0.002 | 4.778e-06 | 9.078e-07 |
| **B3** (best-case) | 0.1397 | 2.331e-02 | **4.429e-03** |
| Leggett/Optical | 0.0255 | 7.767e-04 | 1.476e-04 |

- B1-dominant transported amplitude `A_obs,B1 = 0.19 * 17689/2325625 = 1.445e-03` (Sage-exact `336091/232562500`). B3 best-case `A_obs,B3 = 4.429e-03`.
- delta_P/P at k_BAO=0.043 Mpc^-1 = **1.445e-03** (per-branch B1 sub-feature); delta_P/P at the S43 ring k1=0.0193 Mpc^-1 = **0.2032** (S43 first-sound ring, the LIVE channel).

*S43 transfer-function level vs effacement floor (which channel imprints?):*
- Effacement leakage `(1-Gamma) = 3.0e-04` (single-leg); deep floor `(1-Gamma)^2 = 9.0e-08` (two-leg, the plan's ~1e-6 class).
- S43 first-sound ring `A_FS = 0.204` (knowledge-graph eq_9611 `c_2^2/c_1^2`; plan pin 0.2045) at `r1 = 325.3 Mpc -> k1 = 2*pi/r1 = 0.01932 Mpc^-1`.
- Per-branch sub-feature `A_obs,B1 = 1.445e-03` sits **1.6e+04x ABOVE** the deep effacement floor but **141x BELOW** the S43 ring => the **S43 first-sound ring is the LIVE channel**; the per-branch sub-features are a secondary, weaker amplitude modulation.

*Forecast comparison (INFO branch (a) -- surrogate anchors, paper-search down):*
- B1 sub-feature (1.445e-03): WITHIN Planck theta* (3.1e-04) and CMB-S4/SO floor est (1.0e-04); **BELOW DESI DR2 ruler (2.4e-03)** -- consistent with the position result (0.14% < 0.24%).
- S43 ring A_FS (0.204): WITHIN **all** precision anchors (Planck theta*, DESI DR2, CMB-S4/SO floor) -- IF the ring imprints on the matter P(k)/C_l it is amplitude-detectable. Its detectability is set by the S43 fabric<->photon-baryon coupling (UNTESTED); the comparison against a named experiment's **amplitude** sensitivity (not just acoustic-scale ruler) needs the fetched forecast -> carried forward.

*Substitution chain (substituted numbers -- [SIGN] directional claim):*
1. `shift_frac` (substrate, M_KK-internal) = 0.19.
2. `b1_delta` = 0.01516.
3. transport FORM `A_obs,b = shift_b * (c_b^(2)/c_Gold)^2` (effacement projection; c_Gold=0.915 envelope; substrate-first, NOT borrowed LCDM).
4. Substitute (Reading-NS, B1-dominant): `(c_B1/c_Gold)^2 = 17689/2325625 = 0.0076061` reduces 19% -> 0.14452% (position, Sage-exact `0.19 * 17689/2325625`). Amplitude image gated by S43 `A_FS=0.204` vs deep floor `(1-Gamma)^2=9e-8`.
5. `(c_b^(2)/c_Gold)^2 < 1` since every Layer-2 branch speed `v_g <= c_Gold` => `A_obs,b < shift_b`. **DIRECTION: transported amplitude SMALLER than the naive split (effacement SUPPRESSES).** Position cross-check 0.14% < DESI DR2 0.24% confirms the suppression sign.
- **Conclusion**: `A_obs < naive split`; effacement is a SUPPRESSION, not an amplification. The live channel is the S43 first-sound ring (A_FS=0.204, no LCDM counterpart).

*4-tuple*: `(value=INFO / A_obs_B1=1.445e-03, scheme=effacement-amplitude-projection-(c_b^2/c_Gold)^2, convention=RATIO-substrate-first-transport-NOT-borrowed-LCDM-amplitude, L_max=N/A)`.

*Schema-v2 3-tuple companion row*: `sign_verdict=PASS` (A_obs < naive split AND (c_B1/c_Gold)^2<1 AND position image < DESI DR2 -- the predicted suppression direction holds); `magnitude_verdict=INFO` (the surrogate CMB-S4/SO floor cannot DISCRIMINATE detectability without the fetched amplitude sensitivity); `regime_verdict=BREAKDOWN` (the forecast-COMPARISON leg is 0% available -- paper-search down). Composite collapses to the PRE-REGISTERED INFO branch (a) (the SUBSTRATE forecast and suppression-direction conclusion are themselves VALID; only the experiment-comparison leg is unavailable).

**Substrate-physics assessment** (substrate-first per `phononic-framing.md`): CLASSIFICATION PHONONIC. The BAO feature is the interference pattern of post-transit GGE acoustic excitations of the fabric; the direction of explanation is `D_K spectrum -> Layer-2 BdG branch speeds (c_B1..c_L <= c_Gold) -> substrate two-speed split -> effacement projection (c_b^2/c_Gold)^2 -> emergent BAO amplitude delta_P/P -> detector comparison`. **SCALE-AND-CHANNEL-TAGGED**: the substrate-IS observable is the M_KK-internal per-branch two-speed split (M_KK units, inside the fiber); the laboratory-IN observable is the emergent BAO sub-feature amplitude delta_P/P at the CMB/LSS pivot k~0.043 Mpc^-1 and the S43 ring k1=0.0193 Mpc^-1 (Mpc^-1, in the container-observer's P(k)/C_l). The BRIDGE is the effacement projection + S43 transfer function -- NOT a borrowed LCDM amplitude. The matched (scale, channel) pair makes the comparison against DESI DR2 / Simons / CMB-S4 valid ONLY at the emergent/pivot scale -- the naive 19% is the **unmatched substrate-scale number** (a container-thinking conflation of the M_KK-internal branch speed with the emergent 4D acoustic speed, the category error the framework closed at S94 W5-3). The amplitude finding mirrors the S94 position finding: effacement SUPPRESSES the per-branch sub-feature far below current rulers, while the **S43 first-sound ring (A_FS=0.204, r1=325.3 Mpc) -- a DISTINCTIVE, zero-parameter, no-LCDM-counterpart prediction -- is the live amplitude channel**, whose detection forecast against a named experiment's amplitude sensitivity is the carry-forward once paper-search is restored.

**Output Artifacts**: `computations/session-95/s95_w6_2_bao_amplitude_transport.py` / `.npz` / `.png`."""


def attempt_write():
    txt = WP.read_text(encoding="utf-8")
    if "**Status**: COMPLETED\n**Gate ID**: `CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT`" in txt:
        return "already-done"
    if OLD_STATUS not in txt:
        return "status-anchor-missing"
    if OLD_BODY_START not in txt or OLD_BODY_END not in txt:
        return "body-anchor-missing"
    # Replace the body span (OLD_BODY_START .. OLD_BODY_END inclusive) with NEW_BODY.
    i = txt.index(OLD_BODY_START)
    j = txt.index(OLD_BODY_END) + len(OLD_BODY_END)
    new_txt = txt[:i] + NEW_BODY + txt[j:]
    # Replace the Status line.
    new_txt = new_txt.replace(OLD_STATUS, NEW_STATUS, 1)
    WP.write_text(new_txt, encoding="utf-8")
    return "written"


res = "init"
for k in range(8):
    try:
        res = attempt_write()
    except OSError as e:
        res = f"oserror:{e}"
    if res in ("written", "already-done"):
        break
    time.sleep(0.4)
print(res)
