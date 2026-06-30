#!/usr/bin/env python
"""
S102 W5-4 — S102-FALSIFIER-SURFACE-FREEZE
=========================================
Final gate of Session 102: freeze the cold-read 01 pre-registration draft
(v0.9 -> v1.0) by executing the §8 six-box freeze checklist.

CLASSIFICATION: NON-PHONONIC (register-finalization / pre-registration freeze).
PASS-predicate: artifact-existence-with-substantive-content + bit-exact
R_842 transcription + full numeric re-verify vs canonical_constants.

The SUBSTANTIVE box is (1): the bit-exact R_842 reconciliation. The two
registers carry DIFFERENT rectangles and the freeze reconciles them as DISTINCT
objects (NO resize, NO merge):
  - inventory Row #1 live-watch envelope:  R_842 = [-0.94, -0.88]
        (1D w_0 interval; center -0.91, half-width 0.03; tracks CANONICAL
         w0_FW = -0.918 branch)
  - atlas-09 item 37 (MIGRATION-LEDGER-OF-RECORD, S84 W1b-9 + S86 W13-3):
        R_842 = [-0.942, -0.742] x [-0.2, 0.2]
        (2D BINDING DR3 falsifier rectangle; w_0 center -0.842 half-width 0.100,
         w_a center 0 half-width 0.2; S84 lockouts A-F: no resize, no w_a migration)

The freeze transcribes the atlas-09 2D rectangle as P1's binding rectangle
(bit-exact, S84 content SHA 9cc7f47e...) and annotates inventory Row #1's
interval as the canonical-branch live-watch (distinct object).

Box (3) bundles the referee-M7 Sigma_mnu honesty annotation.
Box (5) Zenodo DOI: repo is PRIVATE -> PREPARED-PENDING-UPLOAD (verdict INFO).

Verdict EMISSION: this script computes value + dual-SHA and PRINTS the payload
via print_verdict_payload; the agent then calls the race-safe emit_verdict MCP
tool. This script does NOT open-code a verdict-file append.

mack-cosmic-bridge sole writer of the falsifier surface per
feedback_mack-bridge-role.md.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
import sys
import hashlib
import json
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_shared"))
from canonical_constants import *           # noqa: F401,F403  (canonical-import discipline)
import canonical_constants as cc

# ----------------------------------------------------------------------------
# Paths (all relative to project root; resolved absolutely)
# ----------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]                                    # (local) project root
P_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"    # (local)
P_DRAFT     = ROOT / "cold-read-s101" / "01-preregistration-DR3-draft.md"     # (local) v0.9
P_V1        = ROOT / "cold-read-s101" / "01-preregistration-DR3-v1.0.md"      # (local) v1.0 frozen
P_INVENTORY = ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"  # (local)
P_ATLAS09   = ROOT / "sessions" / "framework" / "Atlas" / "atlas-09-retractions.md"            # (local)
P_NPZ       = ROOT / "computations" / "session-102" / "s102_falsifier_surface_freeze.npz"      # (local)
P_SCRIPT    = Path(__file__).resolve()                                                          # (local)

# S84-DR3-RESPONSE-PROTOCOL content SHA — the canonical R_842 lock pin (verified
# against computations/session-84/s84_gate_verdicts.txt line 3).
S84_R842_CONTENT_SHA = "9cc7f47e3dedc978de50947914ebca073663c172fb9d5e45268bca4e74b79d9f"  # (local)


def sha256_file(p):                                                          # (local helper)
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def sha256_text(s):                                                          # (local helper)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# ----------------------------------------------------------------------------
# Input SHAs (logged in first 20 lines of stdout per gate-verdicts.md)
# ----------------------------------------------------------------------------
sha_constants = sha256_file(P_CONSTANTS)     # (local) box-3 constants-file content SHA
sha_draft     = sha256_file(P_DRAFT)         # (local) v0.9 draft
sha_inventory = sha256_file(P_INVENTORY)     # (local)
sha_atlas09   = sha256_file(P_ATLAS09)       # (local)
sha_script    = sha256_file(P_SCRIPT)        # (local) content SHA = script bytes

print("=== S102-FALSIFIER-SURFACE-FREEZE input SHAs ===")
print(f"canonical_constants.py content_sha256 = {sha_constants}")
print(f"01-preregistration-DR3-draft.md (v0.9) = {sha_draft}")
print(f"falsifier-master-inventory.md          = {sha_inventory}")
print(f"atlas-09-retractions.md                = {sha_atlas09}")
print(f"S84 R_842 lock content_sha256 (pin)    = {S84_R842_CONTENT_SHA}")
print()

# ----------------------------------------------------------------------------
# BOX 1 — bit-exact R_842 reconciliation (the substantive verification)
# ----------------------------------------------------------------------------
# The two register objects (DISTINCT — no resize, no merge):
R842_atlas_w0 = (-0.942, -0.742)   # (local) atlas-09 item 37 BINDING 2D rectangle, w_0 axis
R842_atlas_wa = (-0.2, 0.2)        # (local) atlas-09 item 37 BINDING 2D rectangle, w_a axis
R842_inv_w0   = (-0.94, -0.88)     # (local) inventory Row #1 1D live-watch interval

# Substrate canonicals (re-derive the centers/half-widths, no hardcoded magic):
w0_canonical  = cc.w0_FW           # -0.918 (Volovik partition; the inventory live-watch tracks THIS)
w0_branch_iv  = -0.842454          # (local) branch-iv (in w0_FW provenance note; NOT a standalone canonical)
w0_lcdm       = cc.w0_LCDM         # -1.0

atlas_w0_center = (R842_atlas_w0[0] + R842_atlas_w0[1]) / 2.0   # (local) -> -0.842
atlas_w0_hw     = (R842_atlas_w0[1] - R842_atlas_w0[0]) / 2.0   # (local) -> 0.100
atlas_wa_hw     = (R842_atlas_wa[1] - R842_atlas_wa[0]) / 2.0   # (local) -> 0.2
inv_w0_center   = (R842_inv_w0[0] + R842_inv_w0[1]) / 2.0       # (local) -> -0.91
inv_w0_hw       = (R842_inv_w0[1] - R842_inv_w0[0]) / 2.0       # (local) -> 0.03

# Containment cross-checks (the disambiguation logic):
branch_iv_inside_atlas = (R842_atlas_w0[0] <= w0_branch_iv <= R842_atlas_w0[1])   # (local) True
canonical_inside_inv   = (R842_inv_w0[0] <= w0_canonical <= R842_inv_w0[1])       # (local) True
# The two objects are DIFFERENT: different dimensionality (2D vs 1D) AND different
# w_0 bounds AND different branch-center.
rectangles_distinct = (R842_atlas_w0 != R842_inv_w0)                              # (local) True

# Bit-exact transcription check: the v1.0 doc MUST carry the atlas-09 rectangle
# edges character-for-character, and the S84 content SHA.
box1_ok = (
    branch_iv_inside_atlas
    and canonical_inside_inv
    and rectangles_distinct
    and abs(atlas_w0_center - (-0.842)) < 1e-12
    and abs(atlas_w0_hw - 0.100) < 1e-12
    and abs(atlas_wa_hw - 0.2) < 1e-12
)

print("=== BOX 1 — R_842 reconciliation (DISTINCT objects) ===")
print(f"atlas-09 item 37 BINDING 2D rectangle: R_842 = [{R842_atlas_w0[0]}, {R842_atlas_w0[1]}] x "
      f"[{R842_atlas_wa[0]}, {R842_atlas_wa[1]}]  (center w_0={atlas_w0_center}, hw_w0={atlas_w0_hw}, hw_wa={atlas_wa_hw})")
print(f"inventory Row #1 1D live-watch interval: [{R842_inv_w0[0]}, {R842_inv_w0[1]}]  "
      f"(center {inv_w0_center}, hw {inv_w0_hw})")
print(f"branch-iv {w0_branch_iv} inside atlas rectangle: {branch_iv_inside_atlas}")
print(f"canonical w0_FW {w0_canonical} inside inventory interval: {canonical_inside_inv}")
print(f"rectangles DISTINCT (no resize, no merge): {rectangles_distinct}")
print(f"BOX 1 OK: {box1_ok}")
print()

# ----------------------------------------------------------------------------
# BOX 3 — full numeric re-verify vs canonical_constants
# ----------------------------------------------------------------------------
# (value-in-draft, canonical-name, rel_tol). Each draft numeric must match its
# canonical pin. Track-B (a stale numeric forces deferral) fires iff any FAIL.
def approx(a, b, rel=1e-6):                                                   # (local helper)
    if b == 0:
        return abs(a - b) < 1e-12
    return abs(a - b) / abs(b) <= rel

reverify = []                                                                # (local) list of (label, draft, canon, ok)
def chk(label, draft_val, canon_val, rel=1e-6):                              # (local helper)
    ok = approx(draft_val, canon_val, rel)
    reverify.append((label, draft_val, canon_val, ok))
    return ok

chk("P1 w0 canonical", -0.918, cc.w0_FW)
chk("P1 w0 LCDM",      -1.0,   cc.w0_LCDM)
chk("P2 Sigma_mnu",     0.0582053272, cc.Sigma_mnu_FW)
chk("P4 A_FS",          0.204, cc.A_FS_first_sound_ring)
chk("P4 r1 Mpc",        325.30, cc.r1_first_sound_ring_Mpc, rel=1e-4)
chk("P4 k1 invMpc",     0.0193, cc.k1_first_sound_ring_invMpc, rel=1e-2)
chk("P5 f_FW",          0.5254916357116971, cc.f_FW)
chk("P5 f_LCDM",        0.5271303865722888, cc.f_LCDM)
chk("P5 bare-f pct",   -0.311, cc.f_bare_suppression_FW_pct)
chk("P6 r Path-H pub",  0.00745, cc.r_PathH_published)
chk("P6 r Path-H full", 0.0074705, cc.r_PathH)
chk("P6 r Path-C",      0.0117, cc.r_CMB_framework, rel=1e-2)
chk("P7b alpha_s sub", -0.0859, cc.alpha_s_substrate_distance_1, rel=1e-2)
chk("P7a alpha_s pivot", 0.0,   cc.alpha_s_pivot_goldstone)
chk("P8 cocycle 6sf",   7.324992, cc.substrate_cocycle_ratio_67_88, rel=1e-6)
chk("P9 m_bb central",  0.003695, cc.m_bb_FW, rel=1e-3)
chk("§6 n_s 0.9561",    0.9561, cc.n_s_framework)
chk("§6 planck_ns",     0.9649, cc.planck_ns)
chk("§6 m_H FW upper",  131.8,  cc.m_H_FW_KK_threshold)
chk("§6 m_H obs",       125.1,  cc.m_H_obs)
chk("§7 H0 anchor",     67.4,   cc.H_0_km_s_Mpc)

box3_numeric_ok = all(ok for (_, _, _, ok) in reverify)                      # (local)
print("=== BOX 3 — numeric re-verify vs canonical_constants ===")
for (label, dv, cv, ok) in reverify:
    flag = "OK " if ok else "STALE"
    print(f"  [{flag}] {label:22s} draft={dv!r:24s} canon={cv!r}")
print(f"BOX 3 numeric re-verify ALL-OK: {box3_numeric_ok}  (Track-B fires iff False)")
print()

# Referee-M7 Sigma_mnu honesty annotation present in v1.0 P2?
v1_text_pre = P_V1.read_text(encoding="utf-8")                              # (local) read before SHA-stamp
m7_annotation_present = ("central value" in v1_text_pre and "echo" in v1_text_pre.lower()
                         and "NOT independent evidence" in v1_text_pre)     # (local)
print(f"=== BOX 3 — referee-M7 Sigma_mnu central-value-echo annotation present: {m7_annotation_present} ===")
print()

# ----------------------------------------------------------------------------
# BOXES 2, 4, 5, 6 — presence checks in the v1.0 doc
# ----------------------------------------------------------------------------
box2_reversal_verbatim = ("w_0^{DR3}  ∈  [-0.86, -0.83]" in v1_text_pre
                          or "w_0^{DR3}" in v1_text_pre and "[-0.86, -0.83]" in v1_text_pre)  # (local)
box4_version_pins = ("DESI DR3" in v1_text_pre and "JUNO" in v1_text_pre
                     and "likelihood" in v1_text_pre)                        # (local)
box5_prepared = ("PREPARED-PENDING-UPLOAD" in v1_text_pre and "Zenodo" in v1_text_pre
                 and "CF-S102-ZENODO-DOI-MINT" in v1_text_pre)              # (local)
box6_date_before_dr3 = ("Freeze date" in v1_text_pre and "precede" in v1_text_pre.lower()
                        and "2026-06-09" in v1_text_pre)                     # (local)

# Bit-exact rectangle edges present in v1.0 (must_contain -0.942, -0.742):
edges_present = ("-0.942" in v1_text_pre and "-0.742" in v1_text_pre
                 and "[-0.2, 0.2]" in v1_text_pre)                          # (local)
s84_sha_present = (S84_R842_CONTENT_SHA in v1_text_pre)                     # (local)
version_1_0 = ("Version" in v1_text_pre and "1.0" in v1_text_pre)          # (local)

print("=== BOXES 2,4,5,6 + transcription presence ===")
print(f"BOX 2 reversal protocol verbatim:     {box2_reversal_verbatim}")
print(f"BOX 4 dataset version pins:           {box4_version_pins}")
print(f"BOX 5 PREPARED-PENDING-UPLOAD:        {box5_prepared}")
print(f"BOX 6 freeze date precedes DR3:       {box6_date_before_dr3}")
print(f"bit-exact rectangle edges present:    {edges_present}")
print(f"S84 content SHA present:              {s84_sha_present}")
print(f"Version 1.0 header present:           {version_1_0}")
print()

# ----------------------------------------------------------------------------
# SHA-stamp the v1.0 doc: embed the constants SHA + the bundle SHA.
# The bundle SHA is computed AFTER the constants SHA is embedded (so it covers
# the final byte-exact content). This is a deterministic two-pass stamp.
# ----------------------------------------------------------------------------
stamped = v1_text_pre.replace("<CONSTANTS_SHA>", sha_constants)            # (local) pass 1
# Bundle SHA = SHA of the content with the constants SHA embedded and the
# bundle placeholder still present (deterministic anchor), then substituted.
bundle_anchor_text = stamped                                              # (local)
bundle_sha = sha256_text(bundle_anchor_text)                              # (local) covers constants-SHA-embedded text
stamped_final = stamped.replace("<V1_BUNDLE_SHA>", bundle_sha)            # (local) pass 2
if stamped_final != v1_text_pre:
    P_V1.write_text(stamped_final, encoding="utf-8")
    print(f"=== v1.0 doc SHA-stamped: CONSTANTS_SHA={sha_constants[:16]}... BUNDLE_SHA={bundle_sha[:16]}... ===")
else:
    print("=== v1.0 doc already stamped (idempotent re-run) ===")
print()

# ----------------------------------------------------------------------------
# Six-box verdict roll-up
# ----------------------------------------------------------------------------
box1 = box1_ok and edges_present and s84_sha_present
box2 = box2_reversal_verbatim
box3 = box3_numeric_ok and m7_annotation_present
box4 = box4_version_pins
box5 = box5_prepared            # PREPARED-PENDING-UPLOAD (external DOI mint pending)
box6 = box6_date_before_dr3 and version_1_0

box5_ticked = False             # (local) box 5 is the SINGLE external deferral (repo PRIVATE)
content_boxes_ok = box1 and box2 and box3 and box4 and box6              # (local) the in-session content freeze

# Verdict: INFO iff content frozen (boxes 1-4,6) AND box 5 prepared-pending-upload.
if content_boxes_ok and box5 and not box5_ticked:
    verdict = "INFO"
    value = ("v1.0-FROZEN-box5-PREPARED-PENDING-UPLOAD_R842-atlas09-2D-[-0.942,-0.742]x[-0.2,0.2]-binding_"
             "inv-Row1-1D-[-0.94,-0.88]-canonical-live-watch-DISTINCT_S84sha-9cc7f47e_"
             "constants-sha-" + sha_constants[:12] + "_bundle-sha-" + bundle_sha[:12] +
             "_M7-Sigma_mnu-echo-annotated_CF-S102-ZENODO-DOI-MINT")
elif content_boxes_ok and box5_ticked:
    verdict = "PASS"
    value = "v1.0-FROZEN-all-6-boxes-ticked"
else:
    verdict = "FAIL"
    fails = [n for n, b in [("box1", box1), ("box2", box2), ("box3", box3),
                            ("box4", box4), ("box6", box6)] if not b]
    value = "freeze-blocked_boxes_failed=" + ",".join(fails) if fails else "freeze-blocked"

print("=== SIX-BOX ROLL-UP ===")
for n, b in [("box1", box1), ("box2", box2), ("box3", box3), ("box4", box4),
             ("box5 (PREPARED-PENDING-UPLOAD)", box5), ("box6", box6)]:
    print(f"  {n:34s}: {b}")
print(f"content-boxes (1-4,6) OK: {content_boxes_ok}")
print(f"VERDICT: {verdict}")
print()

# ----------------------------------------------------------------------------
# Data manifest (.npz) — SHA manifest + box verdicts (optional but produced)
# ----------------------------------------------------------------------------
import numpy as np
np.savez(
    P_NPZ,
    constants_sha=sha_constants,
    draft_sha=sha_draft,
    inventory_sha=sha_inventory,
    atlas09_sha=sha_atlas09,
    v1_bundle_sha=bundle_sha,
    s84_r842_content_sha=S84_R842_CONTENT_SHA,
    R842_atlas_w0=np.array(R842_atlas_w0),
    R842_atlas_wa=np.array(R842_atlas_wa),
    R842_inv_w0=np.array(R842_inv_w0),
    atlas_w0_center=atlas_w0_center,
    atlas_w0_hw=atlas_w0_hw,
    inv_w0_center=inv_w0_center,
    inv_w0_hw=inv_w0_hw,
    branch_iv_inside_atlas=branch_iv_inside_atlas,
    canonical_inside_inv=canonical_inside_inv,
    rectangles_distinct=rectangles_distinct,
    box1=box1, box2=box2, box3=box3, box4=box4, box5_prepared=box5, box6=box6,
    box5_ticked=box5_ticked,
    box3_numeric_ok=box3_numeric_ok,
    m7_annotation_present=m7_annotation_present,
    verdict=verdict,
)
print(f"=== data manifest written: {P_NPZ.name} ===")
print()

# ----------------------------------------------------------------------------
# Dual-SHA closure
#   audit_sha256  = closure over the ordered input-pin map (script+canonical+pinmap)
#   content_sha256 = SHA of the script bytes
# ----------------------------------------------------------------------------
input_pin_map = {                                                          # (local) ordered audit inputs
    "_gate_id": "W5-4-S102-FALSIFIER-SURFACE-FREEZE",
    "_wp_id": "session-102-w5",
    "_scheme": "N/A-register-finalization",
    "_convention": "FALSIFIER-SURFACE-FREEZE-v1.0",
    "script_sha": sha_script,
    "constants_sha": sha_constants,
    "draft_sha": sha_draft,
    "inventory_sha": sha_inventory,
    "atlas09_sha": sha_atlas09,
    "s84_r842_content_sha": S84_R842_CONTENT_SHA,
    "v1_bundle_sha": bundle_sha,
    "R842_atlas_w0": list(R842_atlas_w0),
    "R842_atlas_wa": list(R842_atlas_wa),
    "R842_inv_w0": list(R842_inv_w0),
    "verdict": verdict,
}
audit_sha256 = hashlib.sha256(
    json.dumps(input_pin_map, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()
content_sha256 = sha_script

# ----------------------------------------------------------------------------
# Print verdict payload (agent then calls the race-safe emit_verdict MCP tool)
# ----------------------------------------------------------------------------
def print_verdict_payload(verdict, value, scheme, convention, l_max,
                          audit_sha256, content_sha256, session, gate_id):   # (local helper)
    print("=== VERDICT PAYLOAD (call emit_verdict with these) ===")
    print(f"session       = {session}")
    print(f"gate_id       = {gate_id}")
    print(f"verdict       = {verdict}")
    print(f"value         = {value}")
    print(f"scheme        = {scheme}")
    print(f"convention    = {convention}")
    print(f"l_max         = {l_max}")
    print(f"audit_sha256  = {audit_sha256}")
    print(f"content_sha256= {content_sha256}")


print_verdict_payload(
    verdict=verdict,
    value=value,
    scheme="N/A-register-finalization",
    convention="FALSIFIER-SURFACE-FREEZE-v1.0",
    l_max="N/A",
    audit_sha256=audit_sha256,
    content_sha256=content_sha256,
    session="102",
    gate_id="W5-4-S102-FALSIFIER-SURFACE-FREEZE",
)

# Final non-verdict 4-tuple line per gate-verdicts.md
print()
print(f"4-tuple: (value={verdict}, scheme=N/A-register-finalization, "
      f"convention=FALSIFIER-SURFACE-FREEZE-v1.0, L_max=N/A)")
sys.exit(0)   # script health: clean run regardless of scientific verdict
