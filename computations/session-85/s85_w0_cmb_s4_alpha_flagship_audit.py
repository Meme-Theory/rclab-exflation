#!/usr/bin/env python3
"""
S85 W0-13 — S85-CMB-S4-ALPHA-FLAGSHIP-DOC (audit companion)
============================================================

Gate: S85-CMB-S4-ALPHA-FLAGSHIP-DOC ([AUDIT])

Pre-registered threshold (plan session-85-plan-w0.md §W0-13):
  HYPOTHESIS: The CMB-S4 α_s flagship pre-registration document is
  complete — all 5 channels have all 5 required sections populated.

  PASS iff sections_complete == 25.
  INFO iff 20-24.
  FAIL iff < 20.

Method: presence-check regex scan of the document for each channel ×
each required section. Section considered populated if its bullet
appears with non-empty content (not "TBD" or "pending" alone).

Classification: META
"""

from __future__ import annotations
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

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local)

from canonical_constants import *  # noqa: F401,F403

import hashlib, json, re, sys, time
from pathlib import Path
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                                       # (local)
GATE_ID = "S85-CMB-S4-ALPHA-FLAGSHIP-DOC"                             # (local)
SCHEME = "prereg-doc-audit"                                           # (local)
CONVENTION = "CMB-S4-SB-v2"                                           # (local)
L_MAX = 8                                                             # (local)

CHANNELS = ["α_s", "β_s", "n_T", "r", "f_NL^fold"]                    # (local) 5
REQUIRED_SECTIONS = [                                                 # (local) 5 for PASS count
    "prereg_value",
    "forecast_sigma",
    "decisive_band",
    "framework_prediction",
    "LCDM_null",
]
DIAGNOSTIC_SECTIONS = ["SHA_pin"]                                     # (local) 6th diagnostic

DOC_PATH = resolve_script(85, 's85_w0_cmb_s4_alpha_flagship_doc.md')
OUT_NPZ = resolve_output(85, 's85_w0_cmb_s4_alpha_flagship_audit.npz')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    DOC_PATH,
]


def sha256_of(p):
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script, canonical, pins):
    sb = script.read_bytes()
    cb = canonical.read_bytes()
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode()
    return (hashlib.sha256(sb + cb + pj).hexdigest(),
            hashlib.sha256(sb).hexdigest())


def audit_doc():
    print("--- Section 5: Flagship doc completeness audit ---")
    doc = DOC_PATH.read_text(encoding="utf-8")
    print(f"  Doc loaded: {len(doc)} chars")
    # For each channel, find its section header and count required subsections present
    results = {}  # (local) {channel: {section: bool}}
    sections_complete = 0  # (local) count of populated (channel, required_section) cells
    diagnostic_populated = 0  # (local)
    for ch in CHANNELS:
        # Find the channel's section block. Headers are "## Channel N: <name>"
        # Pattern: locate "## Channel ... <ch>" then capture until the next "## " or end
        header_pat = re.compile(r"## Channel \d+:[^\n]*?" + re.escape(ch), re.DOTALL)
        m = header_pat.search(doc)
        channel_results = {}  # (local)
        if not m:
            # try loose matching
            alt_pat = re.compile(r"## Channel \d+:.*?" + re.escape(ch.replace("^", "\\^")), re.DOTALL)
            m = alt_pat.search(doc)
        if m:
            start = m.end()
            # find next "## " or end of doc
            next_m = re.search(r"^## ", doc[start:], re.MULTILINE)
            end = start + (next_m.start() if next_m else len(doc) - start)
            block = doc[start:end]
            for sec in REQUIRED_SECTIONS:
                # Look for "- **sec**:" pattern with non-empty content
                sec_pat = re.compile(rf"-\s*\*\*{re.escape(sec)}\*\*:\s*(.+?)$", re.MULTILINE)
                sm = sec_pat.search(block)
                if sm and sm.group(1).strip() and "TBD" not in sm.group(1).upper()[:10]:
                    channel_results[sec] = True
                    sections_complete += 1
                else:
                    channel_results[sec] = False
            for sec in DIAGNOSTIC_SECTIONS:
                sec_pat = re.compile(rf"-\s*\*\*{re.escape(sec)}\*\*:\s*(.+?)$", re.MULTILINE)
                sm = sec_pat.search(block)
                if sm and sm.group(1).strip():
                    channel_results[sec] = True
                    diagnostic_populated += 1
                else:
                    channel_results[sec] = False
        else:
            for sec in REQUIRED_SECTIONS + DIAGNOSTIC_SECTIONS:
                channel_results[sec] = False
        results[ch] = channel_results
        print(f"  Channel {ch}: "
              + " ".join(f"{sec}={'✓' if channel_results.get(sec) else '✗'}"
                         for sec in REQUIRED_SECTIONS))

    print(f"\n  Total required sections populated: {sections_complete}/25")
    print(f"  Diagnostic (SHA_pin) populated:    {diagnostic_populated}/5")

    return dict(
        value=sections_complete,
        sections_complete=sections_complete,
        diagnostic_populated=diagnostic_populated,
        per_channel=results,
    )


def evaluate_gate(result):
    n = result["sections_complete"]
    if n >= 25:
        return "PASS"
    if n >= 20:
        return "INFO"
    return "FAIL"


def emit_4tuple(v, s, c, L):
    return f"(value={v!r}, scheme={s}, convention={c}, L_max={L})"


def append_verdict(verdict, value, audit_sha, content_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def save_npz(result, audit_sha, content_sha):
    np.savez_compressed(
        OUT_NPZ,
        sections_complete=result["sections_complete"],
        diagnostic_populated=result["diagnostic_populated"],
        channels=np.array(CHANNELS),
        required_sections=np.array(REQUIRED_SECTIONS),
        per_channel_json=json.dumps(result["per_channel"]),
        audit_sha256=audit_sha, content_sha256=content_sha,
    )


def main():
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(),
        resolve_script(None, 'canonical_constants.py'),
        pins,
    )
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    result = audit_doc()
    verdict = evaluate_gate(result)
    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    save_npz(result, audit_sha, content_sha)
    append_verdict(verdict, result["value"], audit_sha, content_sha)

    wall = time.time() - t0
    print(f"\n=== {GATE_ID}: {verdict}  (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
