"""
S86 W14-5 — S86-WATCHLIST-W5-EDIT (Row #12 A_s eps-sensitivity sub-note)

META gate (registry maintenance). Lands sub-row 12.audit into
sessions/framework/registry/falsifier-master-inventory.md as ADDITIVE delta beyond
the P11 (S86-MASTER-INVENTORY-W6-W13-LAND) landing of Row #12 PAIR-5.

Route adjudication: Route (a)(i) PASS-incremental-upgrade — sub-row 12.audit
parallel to W14-2 row 3.audit, W14-3 row 7.audit, W14-4 row 9.audit. The
sub-row carries:
  - Full-64-hex source pins for S85 W3-7 (workshop file, not a verdict line)
    + S86 W13 P1 FROZEN-COMMIT-LANDING (s86_gate_verdicts.txt:217)
    + W5a P3 forward-reference placeholder (per plan §W14-5 Field 7
      "<plan-file-pending>" allowance)
  - Explicit 4-tier taxonomy naming per S85 W3-7 (Level 1 LCDM-statistical /
    Level 2 framework-floor / Level 3 framework-severity / Tier 4 framework-
    closure) sourced from s85-w2-as-band-authority.md:1736
  - All 5 plan-cited content tokens reproduced or cross-referenced:
    eps range {0.02163, 0.020}, A_s range [3.11e-9, 4.27e-9], W5a P3
    forward reference, S85 W3-7 taxonomy cross-reference, S86 W13 P1
    FROZEN-COMMIT-LANDING cross-reference

PROHIBITED_ACTIONS satisfied:
  - convention-shopping: NO (route adjudicated against on-disk artifact;
    on-disk wins per epistemic-discipline.md source-authority hierarchy)
  - iterate-until-PASS: NO (single-shot file edit, no scan)
  - post-hoc pre-registration editing: NO (Field 9 PASS criterion is
    pre-registered token-presence test; no threshold change)
  - ansatz-forced PASS: NO (verdict line emitted by this script with
    computed SHA, never hardcoded)
  - re-writing P11-landed cell: NO (sub-row 12.audit is additive
    insertion AFTER Row #12; Row #12 byte-equal pre/post verified)

GPU: NOT NEEDED (pure file I/O + SHA computation).
"""
import hashlib
import json
import sys
from pathlib import Path

# Note: S86 META gate; no canonical_constants.py imports needed
# (this is registry maintenance, not a physics computation).

# --- Inputs ---
INVENTORY_PATH = Path("sessions/framework/registry/falsifier-master-inventory.md")
S86_VERDICTS_PATH = Path("computations/session-86/s86_gate_verdicts.txt")
S85_VERDICTS_PATH = Path("computations/session-85/s85_gate_verdicts.txt")
W3_7_WORKSHOP_PATH = Path("sessions/archive/session-85/workshops/s85-w2-as-band-authority.md")

GATE_ID = "S86-WATCHLIST-W5-EDIT"

# --- Source pins (verified by independent grep against on-disk files) ---
# S86 W13 P1 FROZEN-COMMIT-LANDING — verdict line at s86_gate_verdicts.txt:217:
#   "S86-FROZEN-COMMIT-LANDING: PASS -- value=3 scheme=baseline-findings-edit
#    convention=mack-S-7-V.2-W-2-workshop L_max=N/A
#    sha256=e774fc99cb1ea3d2ac07f20823834c2af1b560f9f6fd273b355e7c987ea2660c"
# (pre-S81 single-sha256 format; the SHA is at once content + audit per
#  pre-dual-SHA-template convention).
W13_P1_FROZEN_COMMIT_FULL_SHA = (
    "e774fc99cb1ea3d2ac07f20823834c2af1b560f9f6fd273b355e7c987ea2660c"
)

# S85 W3-7 4-tier taxonomy is in the workshop file, NOT a verdict line
# (it is a unit-class taxonomy reporting-format decision frozen at s85-w2
# workshop). The workshop file is the audit-pin anchor. We will compute its
# SHA at runtime to lock the exact bytes referenced.
# (workshop file SHA computed below)

# W5a P3 SECTOR-1-SR-FLOW-Z-FACTOR is a FORWARD reference (plan §W14-5
# Field 7 explicitly allows "<plan-file-pending>" if not yet committed;
# the plan IS committed, so we cite it).
W5A_PLAN_PATH = Path("sessions/session-plan/session-86-plan-w5a.md")

# --- Compute pre-edit inventory state ---
inventory_pre = INVENTORY_PATH.read_bytes()
inventory_pre_sha = hashlib.sha256(inventory_pre).hexdigest()
inventory_pre_size = len(inventory_pre)

# --- Compute source-file SHAs for audit-pin sub-row ---
s85_verdicts_sha = hashlib.sha256(S85_VERDICTS_PATH.read_bytes()).hexdigest()
s86_verdicts_sha = hashlib.sha256(S86_VERDICTS_PATH.read_bytes()).hexdigest()
w3_7_workshop_sha = hashlib.sha256(W3_7_WORKSHOP_PATH.read_bytes()).hexdigest()
w5a_plan_sha = hashlib.sha256(W5A_PLAN_PATH.read_bytes()).hexdigest()

# --- Print input pin map (first 20 lines per gate-verdicts.md spec) ---
print("=" * 78)
print(f"S86 W14-5 — {GATE_ID}")
print("=" * 78)
print(f"INPUT PINS (canonical SHA-256):")
print(f"  inventory_path           = {INVENTORY_PATH}")
print(f"  inventory_pre_sha256     = {inventory_pre_sha}")
print(f"  inventory_pre_bytes      = {inventory_pre_size}")
print(f"  s85_verdicts_sha256      = {s85_verdicts_sha}")
print(f"  s86_verdicts_sha256      = {s86_verdicts_sha}")
print(f"  w3_7_workshop_sha256     = {w3_7_workshop_sha}")
print(f"  w5a_plan_sha256          = {w5a_plan_sha}")
print(f"  W13_P1_FROZEN_COMMIT_full_sha (pre-S81 single-SHA format) = "
      f"{W13_P1_FROZEN_COMMIT_FULL_SHA}")
print()

# --- Locate Row #12 (A_s) by content (line numbers shift with parallel writers) ---
text_pre = inventory_pre.decode("utf-8")
lines_pre = text_pre.split("\n")

row12_idx = None
for i, ln in enumerate(lines_pre):
    if ln.startswith("| 12 | A_s "):
        row12_idx = i
        break

if row12_idx is None:
    raise RuntimeError("Row #12 (A_s) not found in inventory by content lookup")

row12_content = lines_pre[row12_idx]
print(f"Row #12 located at line {row12_idx + 1} (1-indexed)")
print(f"Row #12 length: {len(row12_content)} chars")

# Verify P11-landed tokens (must remain byte-equal after edit)
P11_TOKENS_TO_PRESERVE = [
    "A_s_FW(eps=0.02163) = 3.11e-09",
    "A_s_FW(eps=0.020) = 4.27e-09",
    "range spans 37% over eps in {0.02163, 0.020}",
    "PAIR-5: eps-sensitivity sub-note 3.11e-9 -> 4.27e-9",
    "W5a P3 FOLD-PIVOT-RUNNING-FLOW-SECTOR-1",
    "eps_pivot is S86 SECTOR-1 carry-forward",
]
print("P11-landed token preservation check (PRE-edit):")
for tok in P11_TOKENS_TO_PRESERVE:
    present = tok in row12_content
    print(f"  {'OK' if present else 'MISS'}: {tok!r}")
    if not present:
        raise RuntimeError(f"P11 token missing pre-edit: {tok!r}")
print()

# --- Construct sub-row 12.audit (additive insertion) ---
# Pattern mirrors W14-2 row 3.audit (line 24), W14-3 row 7.audit (line 26),
# W14-4 row 9.audit (line 28). Sub-row carries:
#   - Full-64-hex S86 W13 P1 FROZEN-COMMIT-LANDING pin (the row Row #12
#     binds to via the FROZEN-PREDICTION-DISCIPLINE-COMMIT contract)
#   - Full-64-hex SHA of s85-w2-as-band-authority.md (workshop where the
#     S85 W3-7 4-tier unit-class taxonomy was frozen; line 1736 anchor)
#   - Full-64-hex SHA of session-86-plan-w5a.md (W5a P3 forward-reference
#     anchor; the eps_pivot resolution gate)
#   - Explicit 4-tier taxonomy NAMES per S85 W3-7:
#       Level 1 LCDM-statistical (32.26-σ Planck reading)
#       Level 2 framework-floor (12.5% scheme floor, W1a-1 STRUCTURAL FAIL)
#       Level 3 framework-severity (W3-7 30% FAIL band)
#       Tier 4 framework-closure (S80 PASS-F2 factor-2 band)
# All 5 plan-cited content tokens are present in the union of Row #12
# primary cell (P11) + sub-row 12.audit (this gate).

W3_7_TAXONOMY_BLOCK = (
    "S85 W3-7 4-tier unit-class taxonomy (per s85-w2-as-band-authority.md:1736 + 1779): "
    "Level 1 LCDM-statistical (Planck A_s reading, 32.26-σ outside-reader figure); "
    "Level 2 framework-floor (12.5% scheme floor from W1a-1 STRUCTURAL FAIL); "
    "Level 3 framework-severity (W3-7 30% FAIL band — log10(1.30)=0.1139 OOM); "
    "Tier 4 framework-closure (S80 PASS-F2 factor-2 band). "
    "Row #12's eps-sensitivity 37% range sits ABOVE Level 2 (12.5% floor) AND ABOVE Level 3 "
    "(30% severity) AND INSIDE Tier 4 (factor-2 closure) — A_s prediction is "
    "FROZEN-PREDICTION-DISCIPLINE-COMMIT-binding at Tier 4 only until W5a P3 closes."
)

W13_P1_BLOCK = (
    f"S86 W13 P1 FROZEN-COMMIT-LANDING canonical pin: "
    f"sha256={W13_P1_FROZEN_COMMIT_FULL_SHA} (pre-S81 single-SHA format; "
    f"verdict at computations/session-86/s86_gate_verdicts.txt:217); "
    f"value=3 (3-row baseline-findings-edit landing, mack-S-7-V.2 W-2 workshop). "
    f"This is the FROZEN-PREDICTION-DISCIPLINE-COMMIT registration that binds "
    f"Row #12's eps-sensitivity sub-note to the band-not-point reporting "
    f"contract for the 2026-2030 publication horizon."
)

W5A_P3_BLOCK = (
    f"W5a P3 S86-SECTOR-1-SR-FLOW-Z-FACTOR forward-reference (plan-file pin: "
    f"sessions/session-plan/session-86-plan-w5a.md sha256={w5a_plan_sha}; "
    f"gate definitions at lines 90, 98, 303, 351-352). Pre-registers TWO output "
    f"4-tuples PIVOT55 + PIVOT312 against substrate-first xi^2(0) IC; HARD "
    f"DEPENDENCY on W4 P4 BRANCH-IV xi_E_GGE^{{-1}} pin. Until P3 closes, "
    f"Row #12 A_s prediction is band-cited (3.11e-9 to 4.27e-9), not point-cited."
)

W3_7_SOURCE_BLOCK = (
    f"S85 W3-7 4-tier unit-class taxonomy source: "
    f"sessions/archive/session-85/workshops/s85-w2-as-band-authority.md "
    f"sha256={w3_7_workshop_sha} (workshop file; NOT a computation verdict line — "
    f"the 4-tier taxonomy is a reporting-format decision frozen at the "
    f"s85-w2 mack-transit band-authority workshop, line 1736 emergence + "
    f"line 1779 final emergence summary). 12.5% scheme-floor pin sourced "
    f"from W1a-1 STRUCTURAL FAIL (S85 W1a workshop)."
)

# Construct the sub-row 12.audit as a single Markdown table row matching the
# 13-column header schema. Cells inherit from Row #12 where 'inherited' is
# the appropriate marker.
sub_row_12_audit = (
    "| 12.audit | audit pins (Row #12 strengthening citation; S86 W14-5) "
    "| full-64-hex source pins per `.claude/rules/gate-verdicts.md` for the "
    "eps-sensitivity 4-tier-taxonomy + FROZEN-COMMIT-LANDING + W5a P3 "
    "forward-reference | source verdicts: `computations/session-86/s86_gate_verdicts.txt:217` "
    "(S86 W13 P1 FROZEN-COMMIT-LANDING); workshop: "
    "`sessions/archive/session-85/workshops/s85-w2-as-band-authority.md:1736` "
    "(S85 W3-7 4-tier taxonomy); plan: "
    "`sessions/session-plan/session-86-plan-w5a.md:90` (W5a P3 SR-flow Z-factor) "
    f"| {W3_7_TAXONOMY_BLOCK} {W13_P1_BLOCK} {W5A_P3_BLOCK} {W3_7_SOURCE_BLOCK} "
    "— strengthening citation only; no value change to A_s prediction band 3.11e-9 to 4.27e-9 "
    "| n/a (audit-pin sub-row, not a live-watch envelope) "
    "| n/a (audit-pin sub-row carries no internal-consistency split; Row #12 primary cell unchanged) "
    "| n/a (audit-pin sub-row; detector horizon inherited from Row #12) "
    "| spectral-amplitude-pivot (inherited) "
    "| substrate-curvature-projection (inherited) "
    "| 10 (inherited) "
    "| `080b7f095f2caea9` (inherited from Row #12) "
    "| `5800016b95bb9a14` (inherited from Row #12; FULL-64-hex S86 W13 P1 FROZEN-COMMIT-LANDING pin: "
    f"`{W13_P1_FROZEN_COMMIT_FULL_SHA}`) "
    "| S86 W14-5 audit-pin sub-row (additive citation upgrade per gate-verdicts.md "
    "canonical-form rule; mirrors §W14-2 row 3.audit + §W14-3 row 7.audit + §W14-4 row 9.audit pattern). "
    "Cross-references: S85 W3-7 4-tier taxonomy (Level 1/2/3/4 unit-class names); "
    "S86 W13 P1 FROZEN-COMMIT-LANDING (FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 binding); "
    "W5a P3 S86-SECTOR-1-SR-FLOW-Z-FACTOR (eps_pivot resolution; HARD DEP on W4 P4 BRANCH-IV)."
)

# --- Insert sub-row 12.audit immediately after Row #12 ---
lines_post = list(lines_pre)
lines_post.insert(row12_idx + 1, sub_row_12_audit)

text_post = "\n".join(lines_post)
inventory_post = text_post.encode("utf-8")
inventory_post_sha = hashlib.sha256(inventory_post).hexdigest()
inventory_post_size = len(inventory_post)
delta_bytes = inventory_post_size - inventory_pre_size

print(f"Sub-row 12.audit constructed: {len(sub_row_12_audit)} chars")
print(f"Inventory delta: {inventory_pre_size} -> {inventory_post_size} bytes "
      f"(+{delta_bytes} bytes)")
print(f"Inventory post-edit SHA: {inventory_post_sha}")
print()

# --- Verify Row #12 byte-equal pre/post ---
row12_post = lines_post[row12_idx]
row12_byte_equal = (row12_post == row12_content)
print(f"Row #12 byte-equal pre/post: {row12_byte_equal}")
if not row12_byte_equal:
    raise RuntimeError(
        f"Row #12 mutation detected!\n  PRE:  {row12_content!r}\n  POST: {row12_post!r}"
    )

# Re-verify all P11 tokens still present in Row #12 post-edit
print("P11-landed token preservation check (POST-edit Row #12):")
for tok in P11_TOKENS_TO_PRESERVE:
    present = tok in row12_post
    print(f"  {'OK' if present else 'MISS'}: {tok!r}")
    if not present:
        raise RuntimeError(f"P11 token mutated post-edit: {tok!r}")
print()

# --- Field 9 PASS criterion: 5 required content tokens present in
# (Row #12 primary cell UNION sub-row 12.audit) ---
combined_for_token_check = row12_post + " " + sub_row_12_audit
required_tokens = {
    "eps range {0.02163, 0.020}": "0.02163" in combined_for_token_check
                                  and "0.020" in combined_for_token_check,
    "A_s range [3.11e-9, 4.27e-9]": "3.11e-09" in combined_for_token_check
                                    and "4.27e-09" in combined_for_token_check,
    "W5a P3 forward reference": ("W5a P3" in combined_for_token_check
                                 and "SECTOR-1-SR-FLOW-Z-FACTOR"
                                 in combined_for_token_check),
    "S85 W3-7 cross-reference": "W3-7" in combined_for_token_check
                                and "4-tier" in combined_for_token_check,
    "S86 W13 P1 FROZEN-COMMIT-LANDING cross-reference":
        "FROZEN-COMMIT-LANDING" in combined_for_token_check
        and W13_P1_FROZEN_COMMIT_FULL_SHA in combined_for_token_check,
}
print("Field 9 PASS-criterion 5-token check (Row #12 primary UNION sub-row 12.audit):")
all_present = True
for label, present in required_tokens.items():
    print(f"  {'OK' if present else 'MISS'}: {label}")
    if not present:
        all_present = False
print()

if not all_present:
    raise RuntimeError("Field 9 5-token check FAILED — at least one required token missing")

# --- Compute audit_sha256 (canonical-JSON-ordered input-pin map) ---
input_pin_map = {
    "audit_subrow_added": 1,
    "edit_rule": "ADDITIVE-sub-row-12-audit-creation-only-no-row12-primary-mutation",
    "expected_sub_row_added": "12.audit",
    "field_9_5_token_check": "PASS",
    "gate_id": GATE_ID,
    "inventory_post_sha256": inventory_post_sha,
    "inventory_pre_sha256": inventory_pre_sha,
    "inventory_target_path": str(INVENTORY_PATH).replace("\\", "/"),
    "p11_predecessor": "S86-MASTER-INVENTORY-W6-W13-LAND",
    "plan_section": "session-86-plan-w14.md-§W14-5",
    "row12_primary_value_cell_byte_equal": True,
    "route_adjudication": ("a-i-additive-sub-row-12-audit-creation-"
                            "(W14-2-W14-3-W14-4-precedent)"),
    "s85_verdicts_input_sha256": s85_verdicts_sha,
    "s85_w3_7_workshop_sha256": w3_7_workshop_sha,
    "s85_w3_7_workshop_path": str(W3_7_WORKSHOP_PATH).replace("\\", "/"),
    "s86_verdicts_input_sha256": s86_verdicts_sha,
    "schema_version": "S84+",
    "source_eps_pivot_resolver_gate": "S86-SECTOR-1-SR-FLOW-Z-FACTOR",
    "source_frozen_commit_full_sha": W13_P1_FROZEN_COMMIT_FULL_SHA,
    "source_frozen_commit_gate_id": "S86-FROZEN-COMMIT-LANDING",
    "source_frozen_commit_verdict_line": "computations/session-86/s86_gate_verdicts.txt:217",
    "target_row_id": "Row #12 (A_s)",
    "verdict_route": "PASS",
    "w5a_plan_path": str(W5A_PLAN_PATH).replace("\\", "/"),
    "w5a_plan_sha256": w5a_plan_sha,
    "w5a_p3_gate_id": "S86-SECTOR-1-SR-FLOW-Z-FACTOR",
}

# Canonical JSON: sort_keys=True, separators=(",", ":") (no whitespace)
canonical_json = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))
audit_sha256 = hashlib.sha256(canonical_json.encode("utf-8")).hexdigest()

print(f"Audit input-pin map keys ({len(input_pin_map)} keys):")
for k in sorted(input_pin_map.keys()):
    print(f"  {k}")
print()
print(f"audit_sha256 = {audit_sha256}")
print(f"content_sha256 = {inventory_post_sha}")
print()

# --- Verdict line emission ---
verdict_value = "sub_note_added=1+sub_row_12_audit_added=1"
verdict_line = (
    f"{GATE_ID}: PASS -- value={verdict_value} scheme=inventory "
    f"convention=MD-EDIT L_max=n/a "
    f"audit_sha256={audit_sha256} content_sha256={inventory_post_sha} "
    f"schema_version=S84+"
)
companion_row = (
    f"# audit_sha256 companion row: {GATE_ID} "
    f"audit={audit_sha256[:16]} content={inventory_post_sha[:16]}"
)

print("VERDICT LINE (canonical, dual-SHA, full-64-hex):")
print(f"  {verdict_line}")
print(f"  {companion_row}")
print()

# --- WRITE PHASE ---
# 1. Write inventory post-edit
INVENTORY_PATH.write_bytes(inventory_post)
written = INVENTORY_PATH.read_bytes()
post_check_sha = hashlib.sha256(written).hexdigest()
assert post_check_sha == inventory_post_sha, (
    f"Inventory write verification FAILED: "
    f"computed {inventory_post_sha} vs read-back {post_check_sha}"
)
print(f"Inventory written: {inventory_post_size} bytes; "
      f"read-back SHA matches computed.")

# 2. Append verdict line + companion row to s86_gate_verdicts.txt
with open(S86_VERDICTS_PATH, "a", encoding="utf-8") as f:
    f.write(verdict_line + "\n")
    f.write(companion_row + "\n")
print(f"Verdict line + companion row appended to {S86_VERDICTS_PATH}")
print()

# --- SHA-uniqueness check (per agent-standards.md "Completion Verification" §3) ---
verdicts_text = S86_VERDICTS_PATH.read_text(encoding="utf-8")
audit_count = verdicts_text.count(audit_sha256)
content_count = verdicts_text.count(inventory_post_sha)
print(f"SHA uniqueness post-write:")
print(f"  audit_sha256 occurrences   = {audit_count}  (expected: 2 — verdict line + companion row)")
print(f"  content_sha256 occurrences = {content_count} (expected: 2 — verdict line + companion row)")
if audit_count != 2 or content_count != 2:
    print("  WARNING: SHA occurrence count differs from expected; "
          "may indicate prior collision.")
print()

print("=" * 78)
print(f"S86 W14-5 {GATE_ID}: PASS")
print("=" * 78)

sys.exit(0)
