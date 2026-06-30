#!/usr/bin/env python3
"""
S83 Wave 2 Gate G10 -- AS-LEDGER-META
======================================

Gate: S83-AS-LEDGER-META  [AUDIT][CHAIN]
Classification: META (read-only classifier over G7/G8/G9)
Owner: transit-dynamics-theorist

Purpose:
  Classify the coherence of the CC7 sub-gate verdict TRIPLE
  (G7=CC7-DYNAMICAL, G8=CC7-LSZ-THOULESS, G9=CC7-UV-DECAY). The META
  gate DOES NOT recompute the underlying physics; it READS the latest
  verdict entries from s83_gate_verdicts.txt and applies the four-
  branch classifier {co-PASS, co-FAIL, MIXED, INFO}.

Phononic framing:
  The three sub-gates interrogate three independent axes of the
  UNIFIED-AS-79 A_s ledger:
     G7: dynamical backbone  (Mukhanov v_k eq. vs F_amp_canonical)
     G8: LSZ-Thouless residue (spectral weight of CMB-pivot mode)
     G9: UV-decay spectral exponent (3PI NLO pump attenuation)
  Each is a distinct structural wall on the substrate phonon ledger.
  Coherence across the triple means the A_s PASS-F2 result rests on
  THREE independent, mutually-consistent checks -- a structural
  epistemic promotion, not a numerical strengthening.

Substitution chain [AUDIT][CHAIN]:
  Step 1 (definitions):
    Let V_i in {PASS, FAIL, INFO} be the LATEST verdict entry for
    sub-gate i in {G7, G8, G9} under the dual-entry permanence rule
    (.claude/rules/gate-verdicts.md: last-appended wins).
    Let Triple T = (V_G7, V_G8, V_G9).
    Classifier C(T):
      co-PASS  <=>  for all i: V_i = PASS
      co-FAIL  <=>  for all i: V_i = FAIL
      MIXED    <=>  (exists i: V_i = PASS) AND (exists j: V_j = FAIL)
      INFO     <=>  (exists i: V_i = INFO) AND (no FAIL)   [fallback]

  Step 2 (substitution):
    Parse computations/session-83/s83_gate_verdicts.txt. For each sub-gate
    prefix, collect all lines beginning with "{gate_id}:", order by
    file-appearance (ascending), retain the LAST element.

  Step 3 (simplification):
    Convert each retained line to the first whitespace-separated
    token after "{gate_id}:" -- this token is the verdict symbol.

  Step 4 (direction):
    Apply classifier C(T). Emit meta-verdict symbol.
    META-PASS  iff  C(T) = co-PASS
    META-FAIL  iff  C(T) = co-FAIL
    META-MIXED iff  C(T) = MIXED
    META-INFO  iff  C(T) = INFO

Decision-Point-2 dispatch:
  co-PASS  -> Branch 1: A_s PASS-F2 unconditional; Wave 3 observational
              falsifiers run under PASS-F2 envelope.
  co-FAIL  -> Branch 2: A_s RETRACTED; Wave 3 Tier 6 recalibrates
              against null; VII.K-DUAL withdrawn.
  MIXED    -> Branch 3: A_s MIXED-verdict-FI-via-pinning; W-3
              META-PRINCIPLE applies; MIXED-PASS-F2 downgrade across
              A_s-contingent observables.
  INFO     -> Branch 1-degraded: PASS-F2 retained but downgrade all
              A_s-contingent observables to INFO pending re-measure.

Inputs (read-only):
  computations/session-83/s83_gate_verdicts.txt              (triple source)
  computations/session-83/s83_w2_g7_cc7_dynamical.npz        (G7 data)
  computations/session-83/s83_w2_g8_cc7_lsz_thouless.npz     (G8 data)
  computations/session-83/s83_w2_g9_cc7_uv_decay.npz         (G9 data)

Output 4-tuple:
  (value=<meta_verdict>, scheme=triple-classifier,
   convention=latest-entry-wins, L_max=N/A)
"""

import os
import sys
import hashlib
import numpy as np

# CPU-only, thread-capped: this is a pure string classifier -- no heavy LA.
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# Mandatory: canonical constants import (even though this is a META gate;
# enforces project convention per computations/_shared/CLAUDE.md).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401,F403

# -----------------------------------------------------------------
# 1. Path setup
# -----------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))                    # (local)
VERDICT_PATH = os.path.join(SCRIPT_DIR, "s83_gate_verdicts.txt")           # (local)
G7_DATA = os.path.join(SCRIPT_DIR, "s83_w2_g7_cc7_dynamical.npz")          # (local)
G8_DATA = os.path.join(SCRIPT_DIR, "s83_w2_g8_cc7_lsz_thouless.npz")       # (local)
G9_DATA = os.path.join(SCRIPT_DIR, "s83_w2_g9_cc7_uv_decay.npz")           # (local)
OUT_NPZ = os.path.join(SCRIPT_DIR, "s83_w2_g10_as_ledger_meta.npz")        # (local)

SUB_GATES = [                                                               # (local)
    ("G7", "S83-CC7-DYNAMICAL"),
    ("G8", "S83-CC7-LSZ-THOULESS"),
    ("G9", "S83-CC7-UV-DECAY"),
]

# -----------------------------------------------------------------
# 2. Input SHA pin (closure hash from ordered input-pin map)
# -----------------------------------------------------------------
def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


pin_map = []                                                                # (local)
for p in [VERDICT_PATH, G7_DATA, G8_DATA, G9_DATA]:
    sha = sha256_of_file(p)
    pin_map.append((os.path.basename(p), sha))
    print(f"INPUT PIN: {os.path.basename(p)}  sha256={sha}")

# closure SHA = SHA-256 of the concatenated ordered pin strings
closure_material = "\n".join(f"{name}::{sha}" for name, sha in pin_map)     # (local)
closure_sha = hashlib.sha256(closure_material.encode("utf-8")).hexdigest()  # (local)
print(f"CLOSURE INPUT PINS: {len(pin_map)}")
print(f"CLOSURE SHA: {closure_sha}")

# -----------------------------------------------------------------
# 3. Latest-verdict parser (dual-entry permanence: last wins)
# -----------------------------------------------------------------
def read_latest_verdict(gate_id, path):
    """Return the symbol of the LATEST matching verdict line, or MISSING."""
    matches = []                                                            # (local)
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line_stripped = line.strip()                                    # (local)
            if line_stripped.startswith(f"{gate_id}:"):
                matches.append(line_stripped)
    if not matches:
        return "MISSING", None
    latest = matches[-1]                                                    # (local) last-appended wins
    # Canonical line form: "GATE: SYMBOL -- value=... scheme=... ..."
    after_colon = latest.split(":", 1)[1].strip()                           # (local)
    before_dashes = after_colon.split("--")[0].strip()                      # (local)
    symbol = before_dashes.split()[0] if before_dashes else "UNKNOWN"       # (local)
    return symbol, latest


# -----------------------------------------------------------------
# 4. Extract triple
# -----------------------------------------------------------------
print()
print("=" * 78)
print("S83 W2 G10 META-CLASSIFIER -- CC7 sub-gate triple")
print("=" * 78)

triple_symbols = []                                                         # (local)
triple_lines = []                                                           # (local)
for short, gate_id in SUB_GATES:
    sym, raw = read_latest_verdict(gate_id, VERDICT_PATH)
    triple_symbols.append(sym)
    triple_lines.append(raw if raw is not None else "")
    print(f"[{short}] {gate_id} -> LATEST verdict = {sym}")
    if raw:
        print(f"      raw line: {raw}")

v_g7, v_g8, v_g9 = triple_symbols                                           # (local)
print()
print(f"Triple: G7={v_g7}, G8={v_g8}, G9={v_g9}")

# -----------------------------------------------------------------
# 5. Classifier
# -----------------------------------------------------------------
def classify_triple(triple):
    """Apply the 4-branch classifier (co-PASS / co-FAIL / MIXED / INFO)."""
    s = set(triple)                                                         # (local)
    if triple == ["PASS", "PASS", "PASS"]:
        return "PASS", "co-PASS"
    if triple == ["FAIL", "FAIL", "FAIL"]:
        return "FAIL", "co-FAIL"
    if "PASS" in s and "FAIL" in s:
        return "MIXED", "MIXED"
    if "INFO" in s and "FAIL" not in s:
        return "INFO", "INFO"
    # Fallback: at least one MISSING/UNKNOWN or a pure INFO-with-PASS triple
    return "INFO", "INFO-fallback"


verdict_symbol, verdict_class = classify_triple(triple_symbols)             # (local)
print(f"Meta-verdict: {verdict_symbol}  (class: {verdict_class})")

# Direction-readoff for Decision Point 2
decision_branch_map = {                                                     # (local)
    "co-PASS": "Branch 1: A_s PASS-F2 unconditional; Wave 3 observational falsifiers run under PASS-F2 envelope.",
    "co-FAIL": "Branch 2: A_s RETRACTED; Wave 3 Tier 6 recalibrates against null; VII.K-DUAL withdrawn.",
    "MIXED":   "Branch 3: A_s MIXED-verdict-FI-via-pinning; W-3 META-PRINCIPLE applies; MIXED-PASS-F2 downgrade across A_s-contingent observables.",
    "INFO":    "Branch 1-degraded: PASS-F2 retained but A_s-contingent observables downgraded to INFO pending re-measure.",
    "INFO-fallback": "Branch 1-degraded (fallback): MISSING/UNKNOWN sub-verdict; reviewer attention required.",
}
branch_note = decision_branch_map.get(verdict_class, "UNMAPPED")            # (local)
print(f"Decision Point 2 dispatch: {branch_note}")

# -----------------------------------------------------------------
# 6. Save NPZ (triple + classification + closure provenance)
# -----------------------------------------------------------------
np.savez(
    OUT_NPZ,
    triple_gates=np.array([g for _, g in SUB_GATES]),
    triple_short=np.array([s for s, _ in SUB_GATES]),
    triple_symbols=np.array(triple_symbols),
    triple_raw_lines=np.array(triple_lines),
    meta_verdict_symbol=np.array([verdict_symbol]),
    meta_verdict_class=np.array([verdict_class]),
    decision_branch=np.array([branch_note]),
    input_pin_names=np.array([n for n, _ in pin_map]),
    input_pin_shas=np.array([s for _, s in pin_map]),
    closure_sha=np.array([closure_sha]),
)
print(f"Saved: {OUT_NPZ}")

# -----------------------------------------------------------------
# 7. Final 4-tuple tag (canonical output line for verdict append)
# -----------------------------------------------------------------
print()
print("-" * 78)
print(f"OUTPUT 4-TUPLE: value={verdict_class} scheme=triple-classifier "
      f"convention=latest-entry-wins L_max=N/A sha256={closure_sha}")
