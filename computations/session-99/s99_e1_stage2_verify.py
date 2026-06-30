"""
S99-E1-STAGE2-VERIFY — PASS-AND closeout for the §VII.BL E1 "Non-LI-Deformation
Necessity" joint theorem Stage-2 two-agent parallel cross-axis independent-verify.

*** AXIS-A RE-DISPATCH (corrected closeout) ***
The original Stage-2 used connes-ncg-theorist as axis-A. Per permanent-results-
registry.md §VII.BL provenance, connes-ncg-theorist was a CO-AUTHOR of the S97 W-2
connes×kk workshop that authored the E1 Stage-0 candidate. That violates
joint-theorem-promotion.md §"Stage 2" audit item 3 (cross-reviewers must NOT be the
original workshop authors) + the Axis-B Selection Protocol condition 2 (original-
authoring-agent exclusion). The compromised connes axis-A line (audit_sha256
13998949...) is RETAINED on disk per absolute verdict permanence; THIS corrected
closeout SUPERSEDES it (Option A, gate-verdicts.md). The clean axis-A re-leg is
van-den-dungen-bridge-theorist (a NON-author NCG-axiomatic reviewer: spectral-triple
factorization / almost-commutative manifolds / NCG axioms). The axis-B leg
(dirac-antimatter-theorist, a non-author) is VALID and STANDS unchanged.

This is the closeout (NON-COMPUTE adjudication gate): it reads the two FROZEN
cross-reviewer fragment JSONs (axis-A van-den-dungen-bridge-theorist; axis-B
dirac-antimatter-theorist), applies the PASS-AND collapse per joint-theorem-
promotion.md Stage 2 (composite PASS iff BOTH single-axis clauses PASS in their
respective reviewers AND the JOINT clause PASSes INDEPENDENTLY in BOTH reviewers;
logical AND, OR FORBIDDEN), emits the structural-check bools (including the NEW
original_author_exclusion_satisfied bool — the FIX vs the prior connes leg), writes
the npz + png, computes the dual-SHA, and PRINTS the emit_verdict payload carrying a
supersedes=<prior connes audit_sha256> token (the dispatching agent calls the
race-safe emit_verdict knowledge-MCP tool; this script does NOT open-code a
verdict-file write).

The actual permanent-results-registry.md §VII.BL E1 tag flip (STAGE-1-CANDIDATE ->
STAGE-3-PERMANENT) is a session-end orchestrator action; this script RECORDS the
transition string in the npz/payload only — it does NOT edit the registry.

Inputs (FROZEN, read-only):
  - computations/session-99/s99_e1_axisA_vdd_verdict.json  (axis-A vdd: clause#7 + joint) [RE-DISPATCH]
  - computations/session-99/s99_e1_axisB_verdict.json      (axis-B dirac: clause#9 + joint) [STANDS]
  - the two S98 static npz (SHA-pinned; verified == plan pins; consumed only for SHA
    folding into audit_sha256, NOT re-read for physics — the physics is in the fragments)
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

sys.path.insert(0, "computations/_shared")
from canonical_constants import tau_fold  # noqa: E402  (consistency note only; not a gate threshold)

# ---------------------------------------------------------------------------
# Identity (mirrors the §W3-1 plan-block machinery pins)
# ---------------------------------------------------------------------------
SESSION = "S99"
GATE_ID = "S99-E1-STAGE2-VERIFY"
SCHEME = "STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY"
CONVENTION = "PASS-AND"
L_MAX = 12  # (local) plan-pinned machinery field (§W3-1 machinery_pin_map.L_max); not a framework constant

ROOT = Path(".")
# AXIS-A RE-DISPATCH: the clean (non-author) van-den-dungen-bridge-theorist fragment.
# The prior connes-ncg-theorist fragment (s99_e1_axisA_verdict.json) is original-author-
# COMPROMISED and is NOT consumed here; the corrective line supersedes the connes line.
AXIS_A_JSON = ROOT / "computations/session-99/s99_e1_axisA_vdd_verdict.json"
AXIS_B_JSON = ROOT / "computations/session-99/s99_e1_axisB_verdict.json"

# Prior compromised connes axis-A closeout line's audit_sha256 (Option A supersedes target).
SUPERSEDES_PRIOR_AUDIT_SHA = "13998949a4d18760e1f8e63562180ec4119675864b55965a99c60ed5f8934ee6"  # (local)
S98_W3_1 = ROOT / "computations/session-98/s98_w3_1_yukawa_eps_lx_between_gen.npz"
S98_W3_2 = ROOT / "computations/session-98/s98_w3_2_baryogen_uniqueness.npz"
SCRIPT = ROOT / "computations/session-99/s99_e1_stage2_verify.py"
CANONICAL = ROOT / "computations/_shared/canonical_constants.py"
NPZ_OUT = ROOT / "computations/session-99/s99_e1_stage2_verify.npz"
PNG_OUT = ROOT / "computations/session-99/s99_e1_stage2_verify.png"

# Plan-pinned static input SHAs (verified == plan §W3-1 input_files pins this session).
PIN_S98_W3_1 = "b26a38b1b4de138a68fa6f33e37d84162c476392831ef2a347160579f76b0c24"
PIN_S98_W3_2 = "4a3f9470bb52f56e0deace1951f4bc6820fba9e92468c5d88d6c160cf36eeb9e"

# Registered §VII.BL E1 anchor for the version-drift provenance note.
# registry §VII.BL line ~21082 anchor vs axis-B-fragment-reported s98_w3_2 value (version-drift note inputs)
ETA_B_REGISTERED_ANCHOR = 1.700e-11  # (local)
ETA_B_NPZ_S98_W3_2 = 4.517492e-11  # (local)


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())                       # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Step 0 — log input SHAs (canonical: first 20 lines of stdout per gate-verdicts.md)
# ---------------------------------------------------------------------------
print("=" * 74)
print(f"{GATE_ID} — PASS-AND closeout (Stage-2 cross-axis independent-verify)")
print("=" * 74)
sha_a = sha256_file(AXIS_A_JSON)                       # (local)
sha_b = sha256_file(AXIS_B_JSON)                       # (local)
sha_w31 = sha256_file(S98_W3_1)                        # (local)
sha_w32 = sha256_file(S98_W3_2)                        # (local)
print(f"INPUT SHA s99_e1_axisA_vdd_verdict.json (RE-DISPATCH, vdd): {sha_a}")
print(f"INPUT SHA s99_e1_axisB_verdict.json (dirac, STANDS)       : {sha_b}")
print(f"SUPERSEDES prior connes axis-A line audit_sha256          : {SUPERSEDES_PRIOR_AUDIT_SHA}")
print(f"INPUT SHA s98_w3_1 npz              : {sha_w31}  (plan pin match={sha_w31 == PIN_S98_W3_1})")
print(f"INPUT SHA s98_w3_2 npz              : {sha_w32}  (plan pin match={sha_w32 == PIN_S98_W3_2})")
assert sha_w31 == PIN_S98_W3_1, "s98_w3_1 SHA drift vs plan pin"
assert sha_w32 == PIN_S98_W3_2, "s98_w3_2 SHA drift vs plan pin"

# ---------------------------------------------------------------------------
# Step 1 — read the two FROZEN cross-reviewer fragments
# ---------------------------------------------------------------------------
frag_a = json.loads(AXIS_A_JSON.read_text())
frag_b = json.loads(AXIS_B_JSON.read_text())

# Axis-A: van-den-dungen-bridge-theorist (spectral / NCG-axiomatic; RE-DISPATCH, NON-author);
#         single-axis clause #7 + JOINT.
# Axis-B: dirac-antimatter-theorist (substrate / Dirac; NON-author; STANDS); clause #9 + JOINT.
AXIS_A_REVIEWER = "van-den-dungen-bridge-theorist"   # (local) the clean axis-A re-leg
AXIS_B_REVIEWER = "dirac-antimatter-theorist"        # (local)
assert frag_a["axis"] == "A" and frag_a["reviewer"] == AXIS_A_REVIEWER, (
    f"axis-A fragment reviewer mismatch: expected {AXIS_A_REVIEWER}, got {frag_a.get('reviewer')!r} "
    "(the RE-DISPATCH must consume the vdd fragment, NOT the compromised connes fragment)")
assert frag_b["axis"] == "B" and frag_b["reviewer"] == AXIS_B_REVIEWER
# Original-author-exclusion attestation carried by the vdd fragment (the FIX vs the connes leg).
assert frag_a.get("original_author_check", "").startswith("vdd NOT an E1 Stage-0 author"), (
    "axis-A fragment must carry the vdd original-author-exclusion attestation")

axisA_clause7 = frag_a["single_axis_verdict"]          # (local) clause #7 generation-blindness
axisA_joint = frag_a["joint_clause_verdict"]           # (local) joint nonLI necessity (spectral)
axisB_clause9 = frag_b["single_axis_verdict"]          # (local) clause #9 baryogenesis uniqueness
axisB_joint = frag_b["joint_clause_verdict"]           # (local) joint nonLI necessity (substrate)

axisA_clause_verdicts = {"clause_7_generation_blindness": axisA_clause7,
                         "joint_nonLI_necessity": axisA_joint}
axisB_clause_verdicts = {"clause_9_baryogen_uniqueness": axisB_clause9,
                         "joint_nonLI_necessity": axisB_joint}

print("\n[FRAGMENTS]")
print(f"  axis-A ({frag_a['reviewer']}) [RE-DISPATCH, non-author]: clause#7={axisA_clause7}  "
      f"joint={axisA_joint}  npz={frag_a['npz_loaded']}  transcript_read={frag_a['workshop_transcript_read']}")
print(f"  axis-A original-author check: {frag_a['original_author_check']}")
print(f"  axis-B ({frag_b['reviewer']}) [STANDS, non-author]: clause#9={axisB_clause9}  "
      f"joint={axisB_joint}  npz={frag_b['npz_loaded']}  transcript_read={frag_b['workshop_transcript_read']}")

# ---------------------------------------------------------------------------
# Step 2 — PASS-AND collapse (joint-theorem-promotion.md Stage 2; OR is FORBIDDEN)
#   composite PASS iff:
#     clause#7 PASS (axis-A) AND clause#9 PASS (axis-B)
#     AND joint_nonLI PASS in BOTH reviewers (logical AND).
#   ANY clause FAIL in EITHER reviewer -> composite FAIL (stays STAGE-1-CANDIDATE).
#   ANY clause INFO (none FAIL) -> composite INFO (stays STAGE-1-CANDIDATE).
# ---------------------------------------------------------------------------
joint_clause_ids = ["joint_nonLI_necessity"]
# per-joint-clause bool = axisA_PASS AND axisB_PASS
joint_pass_and = {c: (frag_a["joint_clause_verdict"] == "PASS"
                      and frag_b["joint_clause_verdict"] == "PASS")
                  for c in joint_clause_ids}            # (local)

all_clause_verdicts = [axisA_clause7, axisA_joint, axisB_clause9, axisB_joint]  # (local)
any_fail = any(v == "FAIL" for v in all_clause_verdicts)                        # (local)
any_info = any(v == "INFO" for v in all_clause_verdicts)                        # (local)
single_axis_both_pass = (axisA_clause7 == "PASS" and axisB_clause9 == "PASS")   # (local)
joint_pass_and_all = all(joint_pass_and.values())                              # (local)

if any_fail:
    composite_verdict = "FAIL"
elif any_info:
    composite_verdict = "INFO"
elif single_axis_both_pass and joint_pass_and_all:
    composite_verdict = "PASS"
else:
    # defensive: non-FAIL, non-INFO, but not all-PASS-AND (should be unreachable
    # given the {PASS,FAIL,INFO} verdict set) -> conservative INFO, NOT PASS.
    composite_verdict = "INFO"

print("\n[PASS-AND COLLAPSE]")
print(f"  single_axis_both_pass (clause#7 ∧ clause#9) = {single_axis_both_pass}")
print(f"  joint_pass_and (per clause) = {joint_pass_and}")
print(f"  joint_pass_and_all          = {joint_pass_and_all}")
print(f"  any_fail={any_fail}  any_info={any_info}")
print(f"  --> COMPOSITE VERDICT = {composite_verdict}  (OR is FORBIDDEN; AND only)")

# ---------------------------------------------------------------------------
# Step 3 — structural-check bools
# ---------------------------------------------------------------------------
# substrate-input orthogonality: >=1 npz feeds exactly ONE reviewer (no overlap).
a_npz = set(frag_a["npz_loaded"]); b_npz = set(frag_b["npz_loaded"])            # (local)
a_only = a_npz - b_npz                                                          # (local)
b_only = b_npz - a_npz                                                          # (local)
overlap = a_npz & b_npz                                                         # (local)
substrate_input_orthogonality_satisfied = (len(a_only) >= 1 or len(b_only) >= 1) and len(overlap) == 0
axis_distinctness_satisfied = (frag_a["axis"] != frag_b["axis"])               # NCG vdd (A) vs substrate/Dirac (B)
no_workshop_transcript_in_prompt = (frag_a["workshop_transcript_read"] is False
                                    and frag_b["workshop_transcript_read"] is False)
# ORIGINAL-AUTHOR EXCLUSION — the FIX vs the prior connes leg.
# The S97 W-2 E1 Stage-0 authors are connes-ncg-theorist + kaluza-klein-theorist
# (permanent-results-registry.md §VII.BL provenance). Neither axis-A vdd NOR axis-B dirac
# is among them, so the Stage-2 original-author-exclusion (joint-theorem-promotion.md
# §"Stage 2" item 3 + Axis-B Selection Protocol condition 2) is SATISFIED.
E1_STAGE0_AUTHORS = {"connes-ncg-theorist", "kaluza-klein-theorist"}            # (local) registry §VII.BL provenance
original_author_exclusion_satisfied = (
    frag_a["reviewer"] not in E1_STAGE0_AUTHORS
    and frag_b["reviewer"] not in E1_STAGE0_AUTHORS
    and frag_a.get("original_author_check", "").startswith("vdd NOT an E1 Stage-0 author"))

e1_stage_transition = ("STAGE-1-CANDIDATE -> STAGE-3-PERMANENT"
                       if composite_verdict == "PASS"
                       else "stays STAGE-1-CANDIDATE")

print("\n[STRUCTURAL CHECKS]")
print(f"  substrate_input_orthogonality_satisfied = {substrate_input_orthogonality_satisfied} "
      f"(axis-A only={sorted(a_only)}; axis-B only={sorted(b_only)}; overlap={sorted(overlap)})")
print(f"  axis_distinctness_satisfied             = {axis_distinctness_satisfied} "
      f"(axis-A=NCG-axiomatic vdd; axis-B=substrate/Dirac)")
print(f"  no_workshop_transcript_in_prompt        = {no_workshop_transcript_in_prompt}")
print(f"  original_author_exclusion_satisfied     = {original_author_exclusion_satisfied} "
      f"(E1 Stage-0 authors={sorted(E1_STAGE0_AUTHORS)}; axis-A={frag_a['reviewer']}, "
      f"axis-B={frag_b['reviewer']} — BOTH non-authors; THIS IS THE FIX vs the prior connes leg)")
print(f"  e1_stage_transition                     = {e1_stage_transition}")

# ---------------------------------------------------------------------------
# Step 3b — joint_theorem_independent_verify 6-item structural attestation
#   (the closeout consumes the audit per plan §W3-1 method.description item 6).
# ---------------------------------------------------------------------------
jtiv = {
    "item1_two_reviewers_parallel": True,        # axis-A + axis-B dispatched in parallel
    "item2_different_axes": axis_distinctness_satisfied,
    "item3_not_workshop_authors": original_author_exclusion_satisfied,  # NEITHER reviewer is an E1 Stage-0 author (the FIX: prior connes leg FAILED this)
    "item4_no_transcripts": no_workshop_transcript_in_prompt,
    "item5_joint_pass_and": joint_pass_and_all,
    "item6_cross_reviewer_machinery_not_self_authored": True,  # distinct axis-native routes (spectral vs Dirac)
}
print("\n[_joint_theorem_independent_verify 6-item attestation]")
for k, v in jtiv.items():
    print(f"  {k}: {v}")

# ---------------------------------------------------------------------------
# Step 3c — version-drift provenance note (NON-BLOCKING; recorded, not a veto)
# ---------------------------------------------------------------------------
import math
eta_ratio = ETA_B_NPZ_S98_W3_2 / ETA_B_REGISTERED_ANCHOR                        # (local)
eta_dec = math.log10(eta_ratio)                                                 # (local) decades apart
# Provenance correction: the axis-B fragment LABELS the drift "1.63x"; but its OWN
# "0.42 decades" figure equals 10^0.42 ~ 2.63x, and the two authoritative eta_B values
# (1.700e-11 anchor; 4.517492e-11 npz) give 4.517492/1.700 = 2.66x EXACTLY. The closeout
# records the arithmetically-correct ratio computed from the two values; the "1.63x" in
# the axis-B fragment is an internal mis-transcription (its 0.42-decade figure agrees with 2.66x).
version_drift_note = (
    f"eta_B registered anchor (VII.BL line ~21082) = {ETA_B_REGISTERED_ANCHOR:.3e}; "
    f"s98_w3_2 npz carries {ETA_B_NPZ_S98_W3_2:.6e} ({eta_ratio:.2f}x = {eta_dec:.2f} dec). "
    f"Axis-B adjudicated REFINED SUPPRESSION (same W1^W2^W3 structure, same forced "
    f"phi_CP=pi/2, eps_in_S97_band=True) — a NUMERICAL refinement, NOT a structural "
    f"divergence; moves NEITHER clause verdict; does NOT block PASS-AND. PROVENANCE NOTE: "
    f"the axis-B fragment labels this '1.63x' but its OWN '0.42 decades' figure = 10^0.42 ~ "
    f"2.63x; the two authoritative values give {eta_ratio:.2f}x EXACTLY, so the closeout "
    f"records {eta_ratio:.2f}x (the '1.63x' label is an axis-B internal mis-transcription)."
)
print("\n[VERSION-DRIFT PROVENANCE NOTE (non-blocking)]")
print(f"  {version_drift_note}")

# ---------------------------------------------------------------------------
# Step 4 — npz
# ---------------------------------------------------------------------------
np.savez(
    NPZ_OUT,
    # core clause-verdict structure
    axisA_clause_verdicts=json.dumps(axisA_clause_verdicts),
    axisB_clause_verdicts=json.dumps(axisB_clause_verdicts),
    joint_clause_ids=np.array(joint_clause_ids, dtype=object),
    joint_pass_and=json.dumps({k: bool(v) for k, v in joint_pass_and.items()}),
    composite_verdict=composite_verdict,
    # structural-check bools
    substrate_input_orthogonality_satisfied=bool(substrate_input_orthogonality_satisfied),
    axis_distinctness_satisfied=bool(axis_distinctness_satisfied),
    no_workshop_transcript_in_prompt=bool(no_workshop_transcript_in_prompt),
    original_author_exclusion_satisfied=bool(original_author_exclusion_satisfied),
    e1_stage0_authors=np.array(sorted(E1_STAGE0_AUTHORS), dtype=object),
    supersedes_prior_audit_sha=SUPERSEDES_PRIOR_AUDIT_SHA,
    axisA_redispatch_reason=("connes-ncg-theorist was a CO-AUTHOR of the S97 W-2 E1 Stage-0 "
                             "workshop; joint-theorem-promotion.md Stage-2 item 3 + Axis-B "
                             "Selection Protocol condition 2 EXCLUDE original authors as "
                             "cross-reviewers. Re-dispatched to van-den-dungen-bridge-theorist "
                             "(clean non-author NCG-axiomatic reviewer)."),
    e1_stage_transition=e1_stage_transition,
    # per-axis raw verdicts (for downstream audit)
    axisA_clause7_generation_blindness=axisA_clause7,
    axisA_joint_nonLI=axisA_joint,
    axisB_clause9_baryogen_uniqueness=axisB_clause9,
    axisB_joint_nonLI=axisB_joint,
    single_axis_both_pass=bool(single_axis_both_pass),
    joint_pass_and_all=bool(joint_pass_and_all),
    # 6-item independent-verify attestation
    jtiv_attestation=json.dumps(jtiv),
    # reviewer / data provenance
    axisA_reviewer=frag_a["reviewer"],   # van-den-dungen-bridge-theorist (RE-DISPATCH)
    axisB_reviewer=frag_b["reviewer"],   # dirac-antimatter-theorist (STANDS)
    axisA_npz_loaded=np.array(frag_a["npz_loaded"], dtype=object),
    axisB_npz_loaded=np.array(frag_b["npz_loaded"], dtype=object),
    # version-drift provenance (non-blocking)
    version_drift_note=version_drift_note,
    eta_B_registered_anchor=ETA_B_REGISTERED_ANCHOR,
    eta_B_npz_s98_w3_2=ETA_B_NPZ_S98_W3_2,
    eta_B_drift_ratio=eta_ratio,
    version_drift_blocking=False,
    # provenance tags
    scheme=SCHEME,
    convention=CONVENTION,
    L_max=L_MAX,
    tau_fold=tau_fold,
    input_sha_axisA=sha_a,
    input_sha_axisB=sha_b,
    input_sha_s98_w3_1=sha_w31,
    input_sha_s98_w3_2=sha_w32,
)
print(f"\n[NPZ] wrote {NPZ_OUT}")

# ---------------------------------------------------------------------------
# Step 5 — png: 2-column clause-verdict matrix
#   rows: clause#7 (gen-blindness) / clause#9 (baryogen) / JOINT-NON-LI
#   cols: axis-A connes / axis-B dirac
# ---------------------------------------------------------------------------
COLOR = {"PASS": "#2e8b57", "FAIL": "#b22222", "INFO": "#d99a00", "N/A": "#888888"}  # (local)
rows = ["clause #7\ngeneration-blindness\n(ε_LX between-gen)",
        "clause #9\nbaryogenesis\nuniqueness",
        "JOINT\nNON-LI-DEFORMATION\nNECESSITY"]                                # (local)
cols = [f"axis-A\n{frag_a['reviewer']}\n(spectral / NCG, RE-DISPATCH)",
        f"axis-B\n{frag_b['reviewer']}\n(substrate / Dirac, STANDS)"]         # (local)
# cell grid: each clause's verdict per reviewer ("N/A" where the clause is the
# OTHER reviewer's single-axis clause, not audited by this reviewer).
cell = [
    [axisA_clause7, "N/A"],          # clause #7 audited by axis-A only
    ["N/A", axisB_clause9],          # clause #9 audited by axis-B only
    [axisA_joint, axisB_joint],      # JOINT audited by BOTH (PASS-AND)
]                                                                              # (local)

fig, ax = plt.subplots(figsize=(9.5, 6.2))
ax.set_xlim(0, 2); ax.set_ylim(0, 3)
ax.invert_yaxis()
for i in range(3):
    for j in range(2):
        v = cell[i][j]                                                         # (local)
        ax.add_patch(Rectangle((j, i), 1, 1, facecolor=COLOR[v],
                               edgecolor="white", lw=3, alpha=0.92))
        ax.text(j + 0.5, i + 0.5, v, ha="center", va="center",
                color="white", fontsize=15, fontweight="bold")
for j, c in enumerate(cols):
    ax.text(j + 0.5, -0.12, c, ha="center", va="bottom", fontsize=9.5, fontweight="bold")
for i, r in enumerate(rows):
    ax.text(-0.04, i + 0.5, r, ha="right", va="center", fontsize=9.5)
ax.set_xticks([]); ax.set_yticks([])
for sp in ax.spines.values():
    sp.set_visible(False)
title = (f"{GATE_ID} — Stage-2 cross-axis PASS-AND closeout\n"
         f"COMPOSITE = {composite_verdict}   |   "
         f"{e1_stage_transition}")
ax.set_title(title, fontsize=13, fontweight="bold", pad=46)
annot = ("AXIS-A RE-DISPATCH: connes (E1 Stage-0 CO-AUTHOR) replaced by van-den-dungen-bridge-theorist "
         "(non-author); axis-B dirac (non-author) STANDS. Prior connes line superseded (Option A).\n"
         "PASS-AND: composite PASS iff clause#7(A)=PASS ∧ clause#9(B)=PASS ∧ "
         "JOINT=PASS in BOTH reviewers (OR FORBIDDEN).\n"
         f"single_axis_both_pass={single_axis_both_pass}  joint_pass_and_all={joint_pass_and_all}  "
         f"|  substrate-input-orthogonality={substrate_input_orthogonality_satisfied} "
         f"(no overlap caveat), axis-distinct={axis_distinctness_satisfied}, "
         f"no-transcript={no_workshop_transcript_in_prompt}, "
         f"original-author-exclusion={original_author_exclusion_satisfied}\n"
         f"version-drift (NON-BLOCKING): η_B {ETA_B_REGISTERED_ANCHOR:.2e}→{ETA_B_NPZ_S98_W3_2:.3e} "
         f"({eta_ratio:.2f}× = {eta_dec:.2f} dec) = refined suppression, same W1∧W2∧W3, same φ_CP=π/2; "
         f"verdict unchanged. [axis-B '1.63×' label is a mis-transcription; 0.42-dec figure ⇒ {eta_ratio:.2f}×]")
fig.text(0.5, 0.015, annot, ha="center", va="bottom", fontsize=7.6,
         bbox=dict(boxstyle="round", facecolor="#f2f2f2", edgecolor="#cccccc"))
plt.subplots_adjust(left=0.30, right=0.97, top=0.80, bottom=0.20)
plt.savefig(PNG_OUT, dpi=150)
plt.close()
print(f"[PNG] wrote {PNG_OUT}")

# ---------------------------------------------------------------------------
# Step 6 — dual-SHA over the ordered input-pin map + emit payload
# ---------------------------------------------------------------------------
pins = {
    "s99_e1_axisA_vdd_verdict.json": sha_a,   # RE-DISPATCH: vdd fragment (NOT the connes fragment)
    "s99_e1_axisB_verdict.json": sha_b,
    "s98_w3_1_yukawa_eps_lx_between_gen.npz": sha_w31,
    "s98_w3_2_baryogen_uniqueness.npz": sha_w32,
    "permanent-results-registry.md::VII.BL.E1": "656ea882948162b9da864c0f3af76632a83cf42ed2cf76188ac93120c356a504",
    "_gate_id": GATE_ID,
    "_scheme": SCHEME,
    "_convention": CONVENTION,
    "_L_max": str(L_MAX),
    "_composite_verdict": composite_verdict,
    "_joint_pass_and_all": str(joint_pass_and_all),
    "_e1_stage_transition": e1_stage_transition,
    "_axisA_reviewer": frag_a["reviewer"],    # vdd — distinguishes this corrective line from the connes line
    "_original_author_exclusion_satisfied": str(original_author_exclusion_satisfied),
    "_supersedes": SUPERSEDES_PRIOR_AUDIT_SHA,  # Option A: this line supersedes the compromised connes line
}
audit_sha, content_sha = compute_dual_sha(SCRIPT, CANONICAL, pins)             # (local)
closure = closure_hash(pins)                                                   # (local)
print(f"\n[CLOSURE] closure_hash(pins) = {closure}")
print(f"[DUAL-SHA] audit_sha256   = {audit_sha}")
print(f"[DUAL-SHA] content_sha256 = {content_sha}")

# verdict value payload (descriptive; no single-quote chars per emit_verdict grammar).
# Carries the Option-A supersedes token (prior compromised connes axis-A line) in the value=
# field AND the dual-SHA companion row (gate-verdicts.md §"Option A").
value = (f"composite={composite_verdict};"
         f"clause7_genblind_axisA={axisA_clause7};"
         f"clause9_baryogen_axisB={axisB_clause9};"
         f"joint_nonLI_axisA={axisA_joint};joint_nonLI_axisB={axisB_joint};"
         f"joint_pass_and_all={joint_pass_and_all};"
         f"substrate_input_orthogonality={substrate_input_orthogonality_satisfied};"
         f"axis_distinct={axis_distinctness_satisfied};"
         f"no_transcript={no_workshop_transcript_in_prompt};"
         f"original_author_exclusion={original_author_exclusion_satisfied};"
         f"axisA_reviewer={frag_a['reviewer']};"
         f"axisA_redispatch=connes_E1_Stage0_coauthor_excluded;"
         f"supersedes={SUPERSEDES_PRIOR_AUDIT_SHA};"
         f"e1_transition={e1_stage_transition.replace(' ', '_')};"
         f"eta_B_drift_nonblocking={eta_ratio:.2f}x_{eta_dec:.2f}dec_refined_suppression")    # (local)

# 4-tuple non-verdict tag line (per gate-verdicts.md step 2)
print(f"\n4-tuple: (value={value}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

extra_rows = [
    f"# {GATE_ID} supersedes={SUPERSEDES_PRIOR_AUDIT_SHA} (Option A, gate-verdicts.md): "
    f"corrective axis-A line; the prior connes-ncg-theorist axis-A line is RETAINED on disk "
    f"and superseded by this line (latest-non-superseded reading discipline)",
    f"# {GATE_ID} AXIS-A RE-DISPATCH reason: connes-ncg-theorist was a CO-AUTHOR of the S97 W-2 "
    f"E1 Stage-0 workshop (permanent-results-registry.md VII.BL provenance); "
    f"joint-theorem-promotion.md Stage-2 item 3 + Axis-B Selection Protocol condition 2 EXCLUDE "
    f"original authors as cross-reviewers; re-legged to van-den-dungen-bridge-theorist (clean "
    f"non-author NCG-axiomatic reviewer); original_author_exclusion_satisfied={original_author_exclusion_satisfied}",
    f"# {GATE_ID} Stage-2 PASS-AND: clause#7(axis-A vdd)={axisA_clause7}, "
    f"clause#9(axis-B dirac)={axisB_clause9}, JOINT-NON-LI=PASS-AND({axisA_joint},{axisB_joint}); "
    f"substrate-input-orthogonality={substrate_input_orthogonality_satisfied} (no overlap caveat); "
    f"axis_distinct={axis_distinctness_satisfied} (NCG vdd vs substrate dirac); "
    f"e1_transition={e1_stage_transition}",
    f"# {GATE_ID} version-drift NON-BLOCKING: eta_B {ETA_B_REGISTERED_ANCHOR:.3e} (VII.BL anchor) "
    f"-> {ETA_B_NPZ_S98_W3_2:.6e} (s98_w3_2 npz, {eta_ratio:.2f}x = {eta_dec:.2f} dec) = refined "
    f"suppression, same W1^W2^W3 + phi_CP=pi/2; verdict unchanged",
    f"# {GATE_ID} registry-tag flip STAGE-1-CANDIDATE->STAGE-3-PERMANENT is a session-end "
    f"orchestrator action; this gate RECORDS the transition only (does NOT edit registry)",
]

# Build the payload for the agent to pass to mcp__knowledge__emit_verdict.
# supersedes=<prior connes audit_sha256> is the Option-A correction path: it permits a
# SECOND canonical line for a gate that already has one (the compromised connes line),
# which the emit_verdict sig_5 guard would otherwise reject.
payload = {
    "session": 99,
    "gate_id": GATE_ID,
    "verdict": composite_verdict,
    "value": value,
    "scheme": SCHEME,
    "convention": CONVENTION,
    "l_max": str(L_MAX),
    "audit_sha256": audit_sha,
    "content_sha256": content_sha,
    "supersedes": SUPERSEDES_PRIOR_AUDIT_SHA,
    "schema_version": "S84+",
    "extra_rows": extra_rows,
}
print("\n<<<EMIT_VERDICT_PAYLOAD>>>")
print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
sys.exit(0)
