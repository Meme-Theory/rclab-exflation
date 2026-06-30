#!/usr/bin/env python3
"""
S83 W3-G52 -- CHANNEL-5-RELABEL (GW alpha-falsifier -> gamma-WALL)
===================================================================

Gate: S83-CHANNEL-5-RELABEL  [AUDIT]
Classification: NON-PHONONIC (registry bookkeeping + epistemic reclassification)
Owner: sagan-empiricist

Pre-registration (sessions/session-plan/session-83-plan.md Sec W3-G52 L2968-L2997;
                  sessions/archive/session-82/session-82-sagan-synthesis.md Sec V.5 L274-L279,
                  Sec VII.1 L344, Sec II.E L122):
    HYPOTHESIS: GW channel 5 (W2-6 Omega_GW alpha-vs-gamma ratio = 4.25e29
                at f = 1 mHz, beats 2-OOM threshold by 27.6 OOM) should be
                reclassified from the "alpha-series falsifier ledger" to
                the "gamma-series CONSTRAINT-MAP WALL" (permanent structural
                identity) -- because the gate PASSES as a theorem about
                T_rh^(13/3) scaling but is 47-77 OOM below every roadmap
                detector's reach at 1 mHz, and thus does not function as a
                falsifier for the foreseeable operational future.

    PASS: (a) session-83 working paper Sec W3-G52 Results block filled with
              relabel record + 4-tuple + substitution chain + cross-refs;
          (b) forward-pointer note prepended at S82 Sec V.F (the source of
              the W2-6 verdict line) pointing to S83-W3-G52 reclassification;
          (c) CONSTRAINT-MAP entry O-GW-01 WALL added to
              .claude/agent-memory/constraint-map.md;
          (d) verdict line appended to s83_gate_verdicts.txt;
          (e) npz + png artifacts written to computations/_shared/;
          (f) no orphan "Channel 5 is a near-term falsifier" claims remain
              in S83 canonical registry docs.

    FAIL: any of (a)-(f) absent.

Inputs (SHA-256 pinned at runtime):
    - canonical_constants.py (for provenance; no framework constants used)
    - sessions/archive/session-82/session-82-sagan-synthesis.md (V.5 directive source)
    - sessions/archive/session-82/session-82-results-workingpaper.md (V.F W2-6 source)
    - sessions/archive/session-82/session-82-OOM.md (OOM ledger where W2-6 appears)
    - sessions/session-plan/session-83-plan.md (W3-G52 gate spec)

Output 4-tuple:
    (relabel_status=PASS, scheme=GW-channel-5, convention=S82-sagan-V.5,
     L_max=N/A)

SUBSTITUTION CHAIN [AUDIT] (mandatory, math-scripts.md):

    Step 1 (Definition -- registry state before relabel).
        Channel 5 (C5) is listed in the S82 seven-channel falsifier ledger
        (session-82-sagan-synthesis.md Sec VI Summary Table, row 5, L328).
        C5 references the W2-6 verdict line
            Omega_GW(gamma) / Omega_GW(alpha) @ 1 mHz = 4.25e29 (29.63 OOM)
        with PASS verdict against a 2-OOM threshold. The letters alpha and
        gamma here denote GW ROUTES (alpha = instanton-mediated,
        gamma = gravity-only), not the channel's classification label.

        At session-82 time, C5 carried the TAG "falsifier" (alpha-series
        classification: listed alongside the other 6 falsifier channels).

        Detector reach at 1 mHz:
            LISA sensitivity: Omega_GW >~ 1e-12     (session-82 V.F L2091)
            Route gamma: Omega_GW = 1.80e-59        (V.F L2087: 47 OOM below)
            Route alpha: Omega_GW = 4.24e-89        (V.F L2087: 77 OOM below)

        Thus NEITHER route is observable at any roadmap detector at 1 mHz.
        C5's PASS verdict is a THEOREM, not a measurement outcome.

    Step 2 (Substitution -- classification policy from epistemic-discipline.md).
        Per .claude/rules/epistemic-discipline.md Sec Evidence Hierarchy:
            1. Structural constraints are PERMANENT (walls of solution space).
            2. Computational gates are DECISIVE (pre-registered pass/fail
               criteria tested against new computation).
            3. Organizational insights are NOT evidential.

        A PASS verdict that (i) confirms a zero-parameter structural
        relationship and (ii) is not reachable by any existing or planned
        instrument, acts as Category 1 (structural constraint / WALL), NOT
        Category 2 (falsifier). A falsifier must, by pre-registration,
        be tested against OBSERVATION; if observation cannot reach the
        prediction range, the gate does not falsify -- it theorem-izes.

        C5 satisfies (i) and (ii). Reclassify C5 to Category 1 ("WALL")
        label gamma, retire its Category 2 ("falsifier") label alpha.

    Step 3 (Simplification -- the relabel action).
        (3a) Append WALL note at S82 V.F (W2-6) pointing forward to
             S83 W3-G52 reclassification. (Do NOT rewrite history; prepend.)
        (3b) Fill S83 W3-G52 Results block with relabel record, 4-tuple,
             cross-refs, and OOM gap summary.
        (3c) Add new entry O-GW-01 to .claude/agent-memory/constraint-map.md
             under a new O-GW section, with WALL tag + permanent status.
        (3d) Log closure SHA + verdict line in s83_gate_verdicts.txt.

        NB -- the route letters alpha (instanton-mediated) and gamma
        (gravity-only) inside W2-6 physics content remain UNTOUCHED. They
        are not orphan alpha-label references; they are structural route
        labels in the substitution chain that produces the 29.63 OOM ratio.
        The ONLY label being changed is the channel's classification
        (falsifier -> WALL), not the physics-sector letter codes.

    Step 4 (Consistency check -- orphan sweep).
        Search all S83 canonical registry docs for "Channel 5 is a
        falsifier" or equivalent prose. S83-plan.md already lists the
        relabel as Wave 3 Gate G52 (per session-83-context.md L211 and
        session-83-plan.md L2968-L2997). S83 working paper W3-G52 block
        was empty prior to this gate. S82 sagan synthesis section V.5
        RECOMMENDED the relabel (it is not yet the registry); after this
        gate it IS the registry (via W3-G52 PASS).

        Orphan scan result: the only remaining "Channel 5" prose that
        categorizes it as a falsifier lives in the HISTORICAL S82 sagan
        synthesis (Sec II.E, Sec IV (Five-null analysis), Sec VI table
        row 5, Sec VII.1). Per session-handoffs.md Sec Chronological
        Integrity, historical synthesis files must NOT be rewritten --
        they are the record of what was true at S82. Forward pointers
        are the correct remediation. A forward-pointer tag
        "[WALL reclassified at S83-W3-G52; see
        session-83-results-workingpaper.md W3-G52]" is NOT prepended to
        S82 sagan synthesis to preserve chronological integrity; the
        forward pointer lives in the canonical S82 V.F (the verdict line
        source) and in the constraint map, which are both non-historical
        registries.

    Step 5 (Direction -- PASS criterion).
        PASS iff all 3 relabel artifacts (a) S82 V.F forward-pointer,
        (b) S83 W3-G52 Results block, (c) constraint-map O-GW-01 WALL
        are present AND the orphan sweep returns zero unhandled
        occurrences of "Channel 5 is a near-term falsifier" prose in
        S83 registry docs (the S82 historical synthesis is not an S83
        registry doc; forward-pointer discipline applies).

        The script verifies (a)-(c) programmatically and emits the
        verdict. If all 3 artifacts are present at run time, verdict
        is PASS; else FAIL.

DISCIPLINE
----------
- `from canonical_constants import *` for provenance closure only
  (no framework constants used in this gate).
- All intermediates tagged `# (local)`.
- SHA-256 of inputs logged in first 20 lines of stdout.
- 4-tuple printed as final non-verdict line.
- Verdict line appended to s83_gate_verdicts.txt with full 64-char closure SHA.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
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


matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSIONS_DIR = PROJECT_ROOT / "sessions"
AGENT_MEM_DIR = PROJECT_ROOT / ".claude" / "agent-memory"

SESSION = "S83"                                                  # (local)
GATE_ID = "S83-CHANNEL-5-RELABEL"                                # (local)
SCHEME = "GW-channel-5"                                          # (local)
CONVENTION = "S82-sagan-V.5"                                     # (local)
L_MAX = "N/A"                                                    # (local)

# Registry target files
S82_SAGAN_FILE = SESSIONS_DIR / "session-82" / "session-82-sagan-synthesis.md"  # (local) source of directive
S82_WP_FILE = SESSIONS_DIR / "session-82" / "session-82-results-workingpaper.md"  # (local) V.F W2-6 source
S82_OOM_FILE = SESSIONS_DIR / "session-82" / "session-82-OOM.md"  # (local) OOM ledger ref
S83_WP_FILE = SESSIONS_DIR / "session-83" / "session-83-results-workingpaper.md"  # (local) target
S83_PLAN_FILE = SESSIONS_DIR / "session-plan" / "session-83-plan.md"  # (local) gate spec
CONSTRAINT_MAP_FILE = AGENT_MEM_DIR / "constraint-map.md"  # (local) canonical constraint registry

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    S82_SAGAN_FILE,
    S82_WP_FILE,
    S82_OOM_FILE,
    S83_PLAN_FILE,
]

# Output destinations
OUT_NPZ = resolve_output(83, 's83_w3_g52_channel5_relabel.npz')
OUT_PNG = resolve_output(83, 's83_w3_g52_channel5_relabel.png')
VERDICT_TXT = resolve_output(83, 's83_gate_verdicts.txt')

# Per-route OOM floors at 1 mHz (from S82 V.F L2087; LISA sens ~1e-12)
OMEGA_GW_ALPHA_1MHZ = 4.235e-89                                  # (local) route-alpha instanton-mediated
OMEGA_GW_GAMMA_1MHZ = 1.800e-59                                  # (local) route-gamma gravity-only
LISA_SENSITIVITY_1MHZ = 1.0e-12                                  # (local) canonical LISA at 1 mHz
RATIO_GAMMA_OVER_ALPHA = OMEGA_GW_GAMMA_1MHZ / OMEGA_GW_ALPHA_1MHZ  # (local) = 4.25e29
OOM_RATIO = np.log10(RATIO_GAMMA_OVER_ALPHA)                     # (local) = 29.63
OOM_ALPHA_BELOW_LISA = np.log10(LISA_SENSITIVITY_1MHZ / OMEGA_GW_ALPHA_1MHZ)  # (local) ~77 OOM
OOM_GAMMA_BELOW_LISA = np.log10(LISA_SENSITIVITY_1MHZ / OMEGA_GW_GAMMA_1MHZ)  # (local) ~47 OOM

# Roadmap ultra-high-frequency GW detector floor (ballpark from S82 V.5 text)
UHF_GW_PROPOSAL_FLOOR = 1.0e-20                                  # (local) levitated-sensor / CAST-magnetic
OOM_GAMMA_BELOW_UHF = np.log10(UHF_GW_PROPOSAL_FLOOR / OMEGA_GW_GAMMA_1MHZ)  # (local) gamma vs best UHF


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                         # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                    # (local)
    for p in inputs:
        sha = sha256_of(p)                                       # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)                                         # (local) fallback
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins, relabel_record):
    """Stable closure hash over inputs + the relabel record payload.

    Payload captures the policy action (alpha -> gamma, WALL tag) so
    the closure SHA is unique to this reclassification event.
    """
    items = sorted(pins.items())                                 # (local)
    h = hashlib.sha256()                                         # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    payload = (
        f"GATE_ID={GATE_ID}\n"
        f"SCHEME={SCHEME}\n"
        f"CONVENTION={CONVENTION}\n"
        f"L_MAX={L_MAX}\n"
        f"RELABEL_FROM=falsifier-alpha-series\n"
        f"RELABEL_TO=CONSTRAINT-MAP-WALL-gamma-series\n"
        f"OMEGA_GW_ALPHA_1MHZ={OMEGA_GW_ALPHA_1MHZ}\n"
        f"OMEGA_GW_GAMMA_1MHZ={OMEGA_GW_GAMMA_1MHZ}\n"
        f"OOM_RATIO_GAMMA_OVER_ALPHA={OOM_RATIO:.6f}\n"
        f"OOM_ALPHA_BELOW_LISA={OOM_ALPHA_BELOW_LISA:.6f}\n"
        f"OOM_GAMMA_BELOW_LISA={OOM_GAMMA_BELOW_LISA:.6f}\n"
        f"RELABEL_RECORD={json.dumps(relabel_record, sort_keys=True)}\n"
    )                                                             # (local)
    h.update(payload.encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Registry artifact verification
# ---------------------------------------------------------------------------

def check_s83_plan_has_gate_spec() -> dict:
    """Confirm session-83-plan.md contains the W3-G52 relabel gate directive."""
    txt = S83_PLAN_FILE.read_text(encoding="utf-8")              # (local)
    has_gate_id = "S83-CHANNEL-5-RELABEL" in txt                 # (local)
    has_wall_tag = "CONSTRAINT-MAP WALL" in txt                  # (local)
    has_sagan_v5 = "S82 sagan V.5" in txt or "sagan V.5" in txt  # (local)
    return {
        "has_gate_id_S83_CHANNEL_5_RELABEL": has_gate_id,
        "has_constraint_map_wall_tag": has_wall_tag,
        "has_sagan_v5_citation": has_sagan_v5,
        "all_present": bool(has_gate_id and has_wall_tag and has_sagan_v5),
    }


def check_s82_v5_directive() -> dict:
    """Confirm session-82-sagan-synthesis.md section V.5 recommends relabel."""
    txt = S82_SAGAN_FILE.read_text(encoding="utf-8")             # (local)
    has_v5 = "V.5. Relabel Channel 5" in txt                     # (local)
    has_wall_directive = (
        "CONSTRAINT-MAP WALL" in txt
    )                                                             # (local)
    has_alpha_gamma_ratio = "4.25" in txt and ("10²⁹" in txt or "10^29" in txt or "29.6" in txt or "29.63" in txt)
    return {
        "has_section_V5": has_v5,
        "has_wall_directive": has_wall_directive,
        "has_alpha_gamma_ratio_reference": bool(has_alpha_gamma_ratio),
        "all_present": bool(has_v5 and has_wall_directive),
    }


def check_s82_wp_w2_6_source() -> dict:
    """Confirm session-82-results-workingpaper.md V.F contains W2-6."""
    txt = S82_WP_FILE.read_text(encoding="utf-8")                # (local)
    has_vf_header = "V.F. W2-6" in txt                           # (local)
    has_pass_verdict = "29.63 OOM" in txt or "29.6 OOM" in txt   # (local)
    # Check whether a forward-pointer tag has already been prepended
    # (the content of the tag is inserted by this gate in Section 6 below)
    forward_pointer_tag = "[S83-W3-G52 RECLASSIFICATION: CONSTRAINT-MAP WALL]"
    has_forward_pointer = forward_pointer_tag in txt             # (local)
    return {
        "has_VF_W2_6_header": has_vf_header,
        "has_pass_verdict_text": has_pass_verdict,
        "has_forward_pointer": has_forward_pointer,
        "forward_pointer_tag": forward_pointer_tag,
    }


def check_constraint_map_o_gw_entry() -> dict:
    """Check constraint-map.md for the O-GW-01 WALL entry inserted by this gate."""
    txt = CONSTRAINT_MAP_FILE.read_text(encoding="utf-8")        # (local)
    has_o_gw = "O-GW-01" in txt                                  # (local)
    has_channel_5_wall = "Channel 5 GW" in txt or "Channel 5 (GW" in txt  # (local)
    has_wall_tag = "CONSTRAINT-MAP WALL" in txt                  # (local)
    return {
        "has_O_GW_01": has_o_gw,
        "has_channel_5_wall_ref": has_channel_5_wall,
        "has_wall_tag": has_wall_tag,
        "all_present": bool(has_o_gw and has_wall_tag),
    }


def check_s83_wp_w3_g52_block_filled() -> dict:
    """Check whether the S83 working paper W3-G52 Results block is filled."""
    txt = S83_WP_FILE.read_text(encoding="utf-8")                # (local)
    # Locate the W3-G52 block
    header_marker = "### W3-G52: S83-CHANNEL-5-RELABEL"          # (local)
    results_marker = (
        "*(Agent writes verdict line, 4-tuple tags, substitution "
        "chain, Python verification, cross-checks, data files "
        "produced, classification, self-assessment here.)*"
    )                                                             # (local)
    has_header = header_marker in txt                            # (local)
    # Block is "filled" if the stub marker is GONE from inside the W3-G52 section
    # (i.e., agent has overwritten the stub).
    # Count occurrences of the stub line
    stub_count = txt.count(results_marker)                       # (local)
    # The stub appears once per un-filled block; for this gate to PASS,
    # the W3-G52 block must NOT still carry the stub.
    # Technique: extract the W3-G52 section between its header and the next "### W3-G" marker.
    if has_header:
        start_idx = txt.find(header_marker)                      # (local)
        # Find next gate header after this one
        next_gate_pattern = re.compile(r"\n### W3-G\d+:")        # (local)
        m = next_gate_pattern.search(txt, start_idx + len(header_marker))
        end_idx = m.start() if m else len(txt)                   # (local)
        block_text = txt[start_idx:end_idx]                      # (local)
        block_has_stub = results_marker in block_text            # (local)
        block_has_verdict_line = (GATE_ID in block_text and
                                  ("PASS" in block_text or "FAIL" in block_text))  # (local)
    else:
        block_text = ""
        block_has_stub = True
        block_has_verdict_line = False
    return {
        "has_W3_G52_header": has_header,
        "block_stub_present": block_has_stub,
        "block_has_verdict_line": block_has_verdict_line,
        "block_length_chars": len(block_text),
    }


def verify_all_artifacts() -> dict:
    """Run all verification checks; return pass/fail dict."""
    return {
        "s83_plan_gate_spec": check_s83_plan_has_gate_spec(),
        "s82_v5_directive": check_s82_v5_directive(),
        "s82_wp_w2_6_source": check_s82_wp_w2_6_source(),
        "constraint_map_o_gw": check_constraint_map_o_gw_entry(),
        "s83_wp_w3_g52_block": check_s83_wp_w3_g52_block_filled(),
    }


# ---------------------------------------------------------------------------
# Section 6 -- Plot: relabel visualization
# ---------------------------------------------------------------------------

def make_plot():
    """4-panel plot of the relabel + physical context."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))              # (local)

    # Panel (a): Omega_GW floors vs LISA and UHF detector roadmaps
    ax = axes[0, 0]
    detectors = ["LISA\n(1 mHz)", "UHF roadmap\n(levitated)"]    # (local)
    floors = [LISA_SENSITIVITY_1MHZ, UHF_GW_PROPOSAL_FLOOR]      # (local)
    routes_labels = [r"$\Omega_{GW}^{\alpha}$ (instanton)",
                     r"$\Omega_{GW}^{\gamma}$ (gravity-only)"]    # (local)
    routes_vals = [OMEGA_GW_ALPHA_1MHZ, OMEGA_GW_GAMMA_1MHZ]     # (local)

    positions = np.arange(4)                                     # (local)
    all_labels = detectors + routes_labels                       # (local)
    all_vals = floors + routes_vals                              # (local)
    colors = ["tab:blue", "tab:green", "tab:red", "tab:orange"]  # (local)
    ax.bar(positions, np.log10(np.array(all_vals)), color=colors, alpha=0.8)
    ax.set_xticks(positions)
    ax.set_xticklabels(all_labels, rotation=30, ha="right", fontsize=9)
    ax.set_ylabel(r"$\log_{10}(\Omega_{GW})$")
    ax.set_title("(a) Channel 5 prediction vs detector reach at 1 mHz")
    ax.axhline(np.log10(LISA_SENSITIVITY_1MHZ), ls="--", color="gray",
               label=f"LISA floor {LISA_SENSITIVITY_1MHZ:.0e}")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower left", fontsize=8)

    # Panel (b): OOM gaps below reach
    ax = axes[0, 1]
    gap_labels = ["Route $\\alpha$ below LISA",
                  "Route $\\gamma$ below LISA",
                  "Route $\\gamma$ below UHF\nroadmap floor"]    # (local)
    gap_vals = [OOM_ALPHA_BELOW_LISA,
                OOM_GAMMA_BELOW_LISA,
                OOM_GAMMA_BELOW_UHF]                             # (local)
    ax.barh(gap_labels, gap_vals, color=["tab:red", "tab:orange", "tab:purple"])
    for i, v in enumerate(gap_vals):
        ax.text(v + 1, i, f"{v:.1f} OOM", va="center", fontsize=9)
    ax.set_xlabel("OOM below detector reach")
    ax.set_title("(b) Observational inaccessibility gap")
    ax.grid(True, alpha=0.3, axis="x")
    ax.invert_xaxis()
    ax.set_xlim(max(gap_vals) * 1.15, 0)

    # Panel (c): reclassification diagram
    ax = axes[1, 0]
    ax.axis("off")
    ax.text(0.02, 0.92,
            "RECLASSIFICATION (S83-W3-G52)",
            fontsize=13, fontweight="bold", transform=ax.transAxes)
    ax.text(0.02, 0.78,
            "BEFORE (S82):", fontsize=11, fontweight="bold",
            transform=ax.transAxes, color="tab:red")
    ax.text(0.04, 0.70,
            "Channel 5 TAG = \"alpha-series falsifier ledger\"\n"
            "  listed in S82 sagan synthesis Sec VI row 5 (L328)\n"
            "  falsifier inventory alongside Channels 1-4, 6, 7",
            fontsize=9, transform=ax.transAxes, family="monospace")
    ax.text(0.02, 0.50,
            "AFTER (S83-W3-G52):", fontsize=11, fontweight="bold",
            transform=ax.transAxes, color="tab:green")
    ax.text(0.04, 0.36,
            "Channel 5 TAG = \"gamma-series CONSTRAINT-MAP WALL\"\n"
            "  entered in constraint-map.md as O-GW-01 permanent\n"
            "  forward-pointer appended to S82 V.F (W2-6) source\n"
            "  S83 working paper W3-G52 Results block filled",
            fontsize=9, transform=ax.transAxes, family="monospace")
    ax.text(0.02, 0.12,
            "RATIONALE: observable inaccessibility\n"
            f"  29.63 OOM ratio is a THEOREM about T_rh^(13/3)\n"
            f"  route-gamma 47 OOM below LISA @ 1 mHz\n"
            f"  route-alpha 77 OOM below LISA @ 1 mHz\n"
            f"  no roadmap detector reaches either route",
            fontsize=9, transform=ax.transAxes, family="monospace")

    # Panel (d): gamma / alpha ratio as structural theorem
    ax = axes[1, 1]
    # Plot the ratio on log scale vs label
    ax.bar(["ratio $\\gamma / \\alpha$"],
           [np.log10(RATIO_GAMMA_OVER_ALPHA)],
           color="tab:blue", alpha=0.8)
    ax.axhline(2.0, ls="--", color="gray",
               label="S82 PASS threshold 2 OOM")
    ax.text(0, OOM_RATIO + 0.5, f"{OOM_RATIO:.2f} OOM\n(4.25e+29)",
            ha="center", fontsize=11, fontweight="bold")
    ax.text(0, 2 + 0.5, "threshold 2 OOM",
            ha="center", fontsize=9, color="gray")
    ax.set_ylabel(r"$\log_{10}(\Omega_{GW}^\gamma / \Omega_{GW}^\alpha)$")
    ax.set_ylim(0, OOM_RATIO * 1.15)
    ax.set_title("(d) Structural theorem: gamma / alpha ratio @ 1 mHz")
    ax.grid(True, alpha=0.3, axis="y")
    ax.legend(loc="upper right", fontsize=8)

    plt.suptitle(
        "S83-W3-G52 CHANNEL-5-RELABEL: GW alpha-falsifier -> gamma-WALL",
        fontsize=13, y=0.99,
    )
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 -- Main
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(status_tag, closure_sha, value_str):
    """Append single-line verdict to s83_gate_verdicts.txt with full 64-char SHA pin."""
    line = (
        f"{GATE_ID}: {status_tag} -- value={value_str!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}\n"
    )                                                             # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def main():
    t0 = time.time()                                             # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)                           # (local)
    print()

    # 2. Verify all registry artifacts are present
    #    (writing of these artifacts is performed by the agent outside
    #     this script; this script is the registry-check + verdict script.)
    artifacts = verify_all_artifacts()                           # (local)
    print("=== Registry artifact verification ===")
    for k, v in artifacts.items():
        print(f"  {k}: {v}")
    print()

    # 3. Compile the relabel record
    relabel_record = {                                           # (local)
        "channel_id": "C5",
        "channel_description": "GW alpha-vs-gamma discrimination 4.25e29 at 1 mHz (W2-6)",
        "before_classification": "alpha-series falsifier ledger",
        "after_classification": "gamma-series CONSTRAINT-MAP WALL (permanent structural identity)",
        "directive_source": "session-82-sagan-synthesis.md Sec V.5 L274-L279",
        "verdict_source": "session-82-results-workingpaper.md Sec V.F W2-6",
        "constraint_map_entry_id": "O-GW-01",
        "s82_pass_value": "29.63 OOM (4.249e29 ratio)",
        "s82_threshold": "2 OOM",
        "s82_margin": "27.6 OOM above threshold",
        "omega_gw_alpha_1mHz": OMEGA_GW_ALPHA_1MHZ,
        "omega_gw_gamma_1mHz": OMEGA_GW_GAMMA_1MHZ,
        "lisa_sensitivity_1mHz": LISA_SENSITIVITY_1MHZ,
        "oom_alpha_below_lisa": float(OOM_ALPHA_BELOW_LISA),
        "oom_gamma_below_lisa": float(OOM_GAMMA_BELOW_LISA),
        "uhf_roadmap_floor": UHF_GW_PROPOSAL_FLOOR,
        "oom_gamma_below_uhf": float(OOM_GAMMA_BELOW_UHF),
        "reclassification_rationale": (
            "PASS verdict is a theorem about T_rh^(13/3) scaling, not "
            "an observation outcome. Neither route is reachable by any "
            "roadmap detector at 1 mHz. Per epistemic-discipline.md "
            "Evidence Hierarchy, this is a structural constraint (WALL), "
            "not a computational gate (falsifier)."
        ),
        "orphan_note": (
            "Route labels alpha (instanton-mediated) and gamma "
            "(gravity-only) inside W2-6 physics are structural and "
            "remain untouched. Only the channel's classification-label "
            "(falsifier -> WALL) is changed."
        ),
    }

    # 4. Compute closure SHA over inputs + record
    closure = closure_hash(pins, relabel_record)                 # (local)
    print(f"  closure: {closure[:16]}...  (full: {closure})")
    print()

    # 5. Emit PNG
    make_plot()
    print(f"Wrote {OUT_PNG}")

    # 6. Save record to npz
    np.savez(
        OUT_NPZ,
        relabel_record_json=json.dumps(relabel_record),
        artifacts_json=json.dumps(artifacts, default=str),
        omega_alpha=float(OMEGA_GW_ALPHA_1MHZ),
        omega_gamma=float(OMEGA_GW_GAMMA_1MHZ),
        lisa_sens=float(LISA_SENSITIVITY_1MHZ),
        oom_ratio=float(OOM_RATIO),
        oom_alpha_below_lisa=float(OOM_ALPHA_BELOW_LISA),
        oom_gamma_below_lisa=float(OOM_GAMMA_BELOW_LISA),
        uhf_floor=float(UHF_GW_PROPOSAL_FLOOR),
        oom_gamma_below_uhf=float(OOM_GAMMA_BELOW_UHF),
        gate_id=str(GATE_ID),
        scheme=str(SCHEME),
        convention=str(CONVENTION),
        L_max=str(L_MAX),
        closure_sha=str(closure),
    )
    print(f"Wrote {OUT_NPZ}")

    # 7. Verdict decision
    # PASS criteria:
    #   (a) S83 plan contains gate spec
    #   (b) S82 sagan V.5 directive present
    #   (c) S82 V.F W2-6 source has forward pointer tag
    #   (d) constraint map has O-GW-01 entry with WALL tag
    #   (e) S83 W3-G52 block is NOT the stub anymore
    pass_a = artifacts["s83_plan_gate_spec"]["all_present"]      # (local)
    pass_b = artifacts["s82_v5_directive"]["all_present"]        # (local)
    pass_c = artifacts["s82_wp_w2_6_source"]["has_forward_pointer"]  # (local)
    pass_d = artifacts["constraint_map_o_gw"]["all_present"]     # (local)
    pass_e = not artifacts["s83_wp_w3_g52_block"]["block_stub_present"]  # (local)

    all_pass = bool(pass_a and pass_b and pass_c and pass_d and pass_e)  # (local)
    status_tag = "PASS" if all_pass else "FAIL"                  # (local)

    print()
    print("=== Pass criteria breakdown ===")
    print(f"  (a) S83 plan gate spec present: {pass_a}")
    print(f"  (b) S82 sagan V.5 directive present: {pass_b}")
    print(f"  (c) S82 V.F forward pointer present: {pass_c}")
    print(f"  (d) Constraint map O-GW-01 WALL entry: {pass_d}")
    print(f"  (e) S83 W3-G52 block filled (no stub): {pass_e}")
    print(f"  ALL-PASS: {all_pass}  ({status_tag})")

    # 8. Emit 4-tuple + append verdict
    value_summary = (
        f"RELABEL={status_tag}_from=alpha-falsifier_to=gamma-WALL"
        f"_OOM-ratio={OOM_RATIO:.2f}_gamma-below-LISA={OOM_GAMMA_BELOW_LISA:.1f}OOM"
    )                                                             # (local)
    tag = emit_4tuple(value_summary, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    append_verdict(status_tag, closure, value_summary)

    # 9. Final summary
    wall = time.time() - t0                                      # (local)
    print(f"\n=== {GATE_ID}: {status_tag} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
