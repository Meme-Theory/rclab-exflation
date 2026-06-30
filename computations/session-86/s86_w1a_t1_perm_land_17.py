"""
S86-W0-PERM-LAND-17 producing script.

Wave: W1a-1 / Gate: S86-W0-PERM-LAND-17 / Classification: META (registry hygiene).
Owner agent (compute-time): connes-ncg-theorist.

Task: For each of 17 W0-W5 theorem-grade PASSes named in S86-W1a plan §W1a-1
table, extract the (audit_sha256, content_sha256) dual-SHA pair from
`computations/session-85/s85_gate_verdicts.txt` and append a permanent-results-registry
row at the cited §VII slot. Emit a verdict line + companion to
`computations/session-86/s86_gate_verdicts.txt`.

THEOREM tolerance rule: every SHA must be exactly 64 hex chars; every §VII
slot must pre-exist (or be created as a one-time slot allocation per the
registry's open-slot convention). Per plan §0.5 + §9, partial completion
falls to INFO; full completion is PASS.

Pre-compute audit (MCP knowledge):
  - search_knowledge("permanent-results-registry §VII W0 W2 W3 W5 land") → 4 hits
    (theorem PROVEN entries; no PRE-CLOSED gate exists for this META landing).
  - search_knowledge("S85 cluster-span Dai-Freed KO-6 two-layer obstruction PASS") →
    confirmed W5-7 PASS, S85 §VII.B draft cited but slot not yet opened.
  - list_constants("K_crit_BdG") → present (value=2.035; W0c-2 provenance).
    No INFO-band needed for W2-12 BdG row.
  - PRE-CLOSED: NO (this is a NEW META-landing).
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU-only fallback per math-scripts.md

# Canonical constants import — mandated by computations/_shared/CLAUDE.md for S34+
# scripts. This script does not USE any framework constants (file I/O only),
# but the import is required for compliance + provenance breadcrumb.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import K_crit_BdG  # noqa: F401  # cited in row 12 (W2-12 BdG band)

# ----------------------------------------------------------------------
# 1. Pin map (Section 4 of script-template.py; THEOREM tolerance class)
# ----------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
S85_VERDICTS = PROJECT_ROOT / "computations" / "session-85" / "s85_gate_verdicts.txt"
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
OUT_VERDICTS = PROJECT_ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"
OUT_JSON = PROJECT_ROOT / "computations" / "session-86" / "s86_w1a_t1_perm_land_17.json"

GATE_ID = "S86-W0-PERM-LAND-17"
SCHEME = "registry_landing"
CONVENTION = "64-char-dual-SHA"
L_MAX_TAG = "NA"
SCHEMA_VERSION = "S84+"

# 17-row mapping table: each row is (plan_stem_alias, actual_verdict_stem,
# vii_slot, one_line_theorem_statement). Plan stem-aliases are the human-
# readable labels in plan §6 §W1a-1 table; actual verdict stems are the
# strings that appear at column-1 of `s85_gate_verdicts.txt`.
ROW_TABLE: list[tuple[str, str, str, str]] = [
    # 1. CC-5 cluster-span identity (W0-3 alias W1a-3)
    ("S85-W0-3", "S85-CC-5-LMAX-ASYMPTOTIC-REFIT",
     "§VII.K-PROP",
     "CC-5 cluster-span identity span(M_0)^2 == cluster(f_conv) at machine-epsilon (2.220e-15) across L in {7,9,11}; triality-orbit-cluster scheme, multiplicative convention, L_max=12."),
    # 2. CC-4 Dai-Freed Z/2 torsion class shift = 0
    ("S85-W0-12", "S85-CC-4-DAI-FREED-TORSION",
     "§VII.K-PROP",
     "CC-4 Dai-Freed Z/2 torsion class shift = 0 for the canonical regulator; Dai-Freed-1994 scheme, eta-mod-Z convention, L_max=8."),
    # 3. HP^1 dim-CM2008 (3,3) shift
    ("S85-W0-16", "S85-HP1-DIMENSION-UNTWISTED-TWISTED",
     "§VII.B",
     "HP^1 dim-CM2008 (3,3) shift = 0; HP^1 cohomology integer-stable across regulator family; HP-cohomology scheme, CM-2008 convention, L_max=8."),
    # 4. CC-1 eta-invariant = 0 (INFO at registration; theorem-grade)
    ("S85-W0-23", "S85-CC-1-ETA-INVARIANT-FULL-TRIPLE",
     "§VII.K-PROP",
     "CC-1 eta-invariant = 0 for the spectral triple at L_max=8 (INFO-band, registered as theorem-grade structural data); APS-1975 scheme, Jensen-SU(3)-x-A_F convention."),
    # 5. W2-2 cross-session theorem family
    ("S85-W2-2", "S85-W2-CROSS-SESSION-THEOREM-FAMILY",
     "§VII.P",
     "W2-2 mother-theorem + 3 corollaries + 2 predicted instantiations (k=3 HP^3 + 4-bucket HP^even q-deformation); theorem-family-unification scheme, registry-§VII-unified convention."),
    # 6. W2-3 HP^3 disjoint corridor
    ("S85-W2-3", "S85-W2-HP3-DISJOINT-CORRIDOR-THREE-WAY",
     "§VII.P",
     "W2-3 HP^3 disjoint corridor: num_nontrivial = 0 (rank-3 Hochschild triple-intersection vanishes); hochschild-triple-intersection scheme, CM-2008 convention."),
    # 7. KO-6 Higgs sign +1 -> -1 RG flow
    ("S85-W2-4", "S85-W2-KO6-HIGGS-SIGN-DIRECTION",
     "§VII.P",
     "KO-6 Higgs sign-flow direction +1 -> -1 under RG (CCM-2007 / AC-2010 sign convention); ko6-sign-flow scheme."),
    # 8. KO-6 eta-band 3/3 = machine zero
    ("S85-W2-5", "S85-W2-PRE-CC-1-KO6-ON-ETA",
     "§VII.P",
     "KO-6 eta-band 3/3 = machine zero (eta-invariant identically vanishes on the KO-6 corridor); ko6-eta-constraint-verification scheme, APS+CCM-2007 convention."),
    # 9. Quantum disjoint corridor 4-route confluence
    ("S85-W2-6", "S85-W2-QUANTUM-DISJOINT-CORRIDOR",
     "§VII.P",
     "Quantum disjoint corridor 4-route: q-deformed HKR-SBI under CM-cyclic + Woronowicz, num_nontrivial = 0; q-deformed-HKR-SBI scheme, CM-cyclic+Woronowicz convention."),
    # 10. 3-solo SHA reproduction cf3b7443...
    ("S85-W2-10", "S85-W2-THREE-SOLO-CONVERGENCE-VERIFY",
     "§VII.K-META",
     "3-solo SHA reproduction (3 independent agents reproduce identical content_sha256 cf3b7443... for S84-W2a-11); three-solo-sha-reproduction scheme, S84-W2a-11 convention."),
    # 11. Triality-Jensen commutation
    ("S85-W2-11", "S85-W2-PRE-CC-2-TRIALITY-ON-JENSEN",
     "§VII.K-PROP",
     "Triality-Jensen commutation [tau_3, J_Jensen] = 0.00e+00 (machine-epsilon); triality-orbit-spectrum-match scheme, Spin(8)-triality convention, L_max=8."),
    # 12. BdG band CMB l_crit, T_LB at K_crit_BdG
    ("S85-W2-12", "S85-W2-BAND-DETECTOR-MAP-LEGGETT-BOG",
     "§VII.K-PROP",
     "BdG band CMB l_crit = 1424.50 (T_LB = 0.113 implicit in two-scale band-to-l mapping) at K_crit_BdG = 2.035 (canonical_constants.py); two-scale-band-to-l scheme, Mukhanov-Sasaki-recomb convention, L_max=10."),
    # 13. CF-5 PIXIE-mu K_FIRAS gamma=1 lockout
    ("S85-W3-1", "S85-W3-CF-5-PIXIE-KMFIRAS-PREREG",
     "§VII.K-PROP",
     "CF-5 PIXIE-mu x K_FIRAS gamma=1 lockout: regulator-spread = 8.69e-05 across canonical heat-kernel convention A; canonical_heat_kernel scheme, A convention, L_max=10."),
    # 14. CF-6 K-regulator functorial closure-defect
    ("S85-W3-4", "S85-W3-CF-6-K-REGULATOR-MAP-THEOREM",
     "§VII.K-PROP",
     "CF-6 K-regulator functorial closure-defect = 2.55e-16 (cross-regulator A-union-B at L_max=10); cross-regulator scheme."),
    # 15. CF-2 two-speed transfer c_S = f_B
    ("S85-W3-5", "S85-W3-CF-2-TWO-SPEED-TRANSFER-IDENTITY",
     "§VII.K-PROP",
     "CF-2 two-speed transfer identity c_S = f_B at machine-epsilon (cross-regulator convention A, L_max=10); cross-regulator scheme."),
    # 16. Ginzburg-Oz validity Gi
    ("S85-W3-9", "S85-W3-RUNNING-MASS-GINZBURG-OZ",
     "§VII.K-PROP",
     "Ginzburg-Oz validity criterion Gi = 5.50e-10 (mean-field intact over W3 regulator family); heat_kernel scheme, A convention, L_max=10."),
    # 17. Two-Layer Obstruction Theorem n_joint = 0/5
    ("S85-W5-7", "S85-W5-7-TWO-LAYER-OBSTRUCTION",
     "§VII.B",
     "Two-Layer Obstruction Theorem: n_joint = 0/5 across the 5-regulator atlas (every joint scheme-independence + epsilon_H conjunct fails individually for every regulator); 5-regulator-atlas scheme, 5pct-scheme-indep-def convention, L_max=10."),
]

assert len(ROW_TABLE) == 17, f"plan-pinned 17 rows; got {len(ROW_TABLE)}"


# ----------------------------------------------------------------------
# 2. Helpers
# ----------------------------------------------------------------------

HEX64 = re.compile(r"^[0-9a-f]{64}$")
AUDIT_RE = re.compile(r"audit_sha256=([0-9a-f]{64})")
CONTENT_RE = re.compile(r"content_sha256=([0-9a-f]{64})")


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_sha256(pin_map: dict) -> str:
    """sha256(canonical_serialize(input_pin_map)) -- per gate-verdicts.md."""
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(canon).hexdigest()


def find_canonical_pass_line(verdict_lines: list[str], stem: str) -> tuple[int, str] | None:
    """Find the FIRST canonical-form (non-comment, non-companion) verdict line
    starting with the literal stem followed by ':'. Returns (1-indexed-line-no,
    line) or None if not found.

    Skips comment rows starting with '#' and lines with the dual-SHA companion
    annotation 'companion row'.
    """
    prefix = stem + ":"
    for idx, line in enumerate(verdict_lines, start=1):
        if line.startswith("#"):
            continue
        if "companion row" in line:
            continue
        if line.startswith(prefix):
            return idx, line.rstrip()
    return None


# ----------------------------------------------------------------------
# 3. Logging input SHAs (first 20 lines of stdout per script template)
# ----------------------------------------------------------------------

print("=" * 78)
print(f"[{GATE_ID}] producing-script start at {datetime.now(timezone.utc).isoformat()}")
print("=" * 78)
print(f"[input] s85_verdicts_path  = {S85_VERDICTS}")
s85_sha = file_sha256(S85_VERDICTS)
print(f"[input] s85_verdicts_sha256= {s85_sha}")
print(f"[input] registry_path      = {REGISTRY_MD}")
registry_pre_sha = file_sha256(REGISTRY_MD)
print(f"[input] registry_pre_sha256= {registry_pre_sha}")
print(f"[input] gate_stems_count   = {len(ROW_TABLE)}")
plan_stems_serialized = "|".join(r[0] for r in ROW_TABLE)
actual_stems_serialized = "|".join(r[1] for r in ROW_TABLE)
slots_serialized = "|".join(r[2] for r in ROW_TABLE)
print(f"[input] plan_stems         = {plan_stems_serialized}")
print(f"[input] actual_stems       = {actual_stems_serialized}")
print(f"[input] vii_slots          = {slots_serialized}")
print("-" * 78)

# Compute the closure-SHA candidate (input-pin-map hash). The verdict's
# audit_sha256 MUST be this closure SHA, NOT a copy of any input file SHA.
input_pin_map = {
    "s85_verdicts_path": str(S85_VERDICTS).replace("\\", "/"),
    "s85_verdicts_content_sha256": s85_sha,
    "registry_path": str(REGISTRY_MD).replace("\\", "/"),
    "registry_pre_edit_content_sha256": registry_pre_sha,
    "plan_stems": [r[0] for r in ROW_TABLE],
    "actual_stems": [r[1] for r in ROW_TABLE],
    "vii_slots": [r[2] for r in ROW_TABLE],
    "schema_version": SCHEMA_VERSION,
    "scheme": SCHEME,
    "convention": CONVENTION,
}
audit_closure_sha = closure_sha256(input_pin_map)
print(f"[closure] audit_sha256 (input-pin-map closure) = {audit_closure_sha}")
print("-" * 78)


# ----------------------------------------------------------------------
# 4. Main extraction loop (substitution chain steps 1-3)
# ----------------------------------------------------------------------

with open(S85_VERDICTS, "r", encoding="utf-8") as f:
    verdict_lines = f.read().splitlines()

with open(REGISTRY_MD, "r", encoding="utf-8") as f:
    registry_text = f.read()

# Cross-check 2: identify which §VII slots pre-exist in the registry.
slot_existence = {}
for slot in {r[2] for r in ROW_TABLE}:
    # Header pattern: '## <slot> ' or '### <slot> ' or '## <slot> —' (em-dash variants)
    pre_exists = any(
        line.startswith(f"## {slot} ") or line.startswith(f"### {slot} ") or
        line.startswith(f"## {slot} —") or line.startswith(f"## {slot}—") or
        line.startswith(f"## {slot}\n")
        for line in registry_text.splitlines()
    )
    # Fallback: substring check for slot label in any header context
    if not pre_exists:
        # Check for '## <slot>' as the start of a header line (any trailing text).
        pre_exists = any(
            (line.startswith(f"## {slot}") or line.startswith(f"### {slot}"))
            for line in registry_text.splitlines()
        )
    slot_existence[slot] = pre_exists
    print(f"[slot-check] {slot}: pre_exists={pre_exists}")

# Per plan §0.5 + §9: a missing slot is INFO-band, NOT FAIL. The §VII.B slot
# does NOT pre-exist as a §-header in the registry. Per the cross-pair note in
# the W1a plan and the precedent of §VII.P / §VII.Q (both opened via plan-
# directive in S85 W9-1 / W9-2), a one-time slot-allocation header is created
# here as part of the registry write (NOT a recompute; just a header insert).
needs_slot_creation = [s for s, pe in slot_existence.items() if not pe]
print(f"[slot-check] slots needing creation: {needs_slot_creation}")

extraction_results: list[dict] = []
n_pass = 0  # (local)
n_fail = 0  # (local)
missing_stems: list[str] = []

for plan_stem, actual_stem, vii_slot, one_liner in ROW_TABLE:
    found = find_canonical_pass_line(verdict_lines, actual_stem)
    if found is None:
        print(f"[FAIL-EXTRACT] {plan_stem} (actual={actual_stem}): no canonical verdict line found")
        n_fail += 1
        missing_stems.append(plan_stem)
        extraction_results.append({
            "plan_stem": plan_stem,
            "actual_stem": actual_stem,
            "vii_slot": vii_slot,
            "status": "MISSING-VERDICT-LINE",
            "audit_sha256": None,
            "content_sha256": None,
            "source_line_number_in_s85_verdicts": None,
            "one_liner": one_liner,
        })
        continue
    line_no, line_text = found
    a_match = AUDIT_RE.search(line_text)
    c_match = CONTENT_RE.search(line_text)
    if a_match is None or c_match is None:
        print(f"[FAIL-EXTRACT] {plan_stem}: line {line_no} missing dual-SHA: {line_text[:120]}...")
        n_fail += 1
        missing_stems.append(plan_stem)
        extraction_results.append({
            "plan_stem": plan_stem,
            "actual_stem": actual_stem,
            "vii_slot": vii_slot,
            "status": "MISSING-DUAL-SHA",
            "audit_sha256": None,
            "content_sha256": None,
            "source_line_number_in_s85_verdicts": line_no,
            "one_liner": one_liner,
        })
        continue
    audit_sha = a_match.group(1)
    content_sha = c_match.group(1)
    # Cross-check 1: enforce 64-char hex
    if not (HEX64.match(audit_sha) and HEX64.match(content_sha)):
        print(f"[FAIL-HEX64] {plan_stem}: SHA short. a={audit_sha} c={content_sha}")
        n_fail += 1
        missing_stems.append(plan_stem)
        extraction_results.append({
            "plan_stem": plan_stem,
            "actual_stem": actual_stem,
            "vii_slot": vii_slot,
            "status": "SHA-NOT-64-HEX",
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
            "source_line_number_in_s85_verdicts": line_no,
            "one_liner": one_liner,
        })
        continue
    print(f"[PASS-EXTRACT] {plan_stem} -> {vii_slot} | line={line_no} | audit={audit_sha[:16]}... content={content_sha[:16]}...")
    n_pass += 1
    extraction_results.append({
        "plan_stem": plan_stem,
        "actual_stem": actual_stem,
        "vii_slot": vii_slot,
        "status": "EXTRACTED",
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "source_line_number_in_s85_verdicts": line_no,
        "one_liner": one_liner,
    })

# Cross-check anchor: row #17 must reproduce plan §0.11 line 740 SHA pin.
ANCHOR_AUDIT = "f8c8f56630a347192a627a0699714a03fc3c9d9d249835807f0f77c4fc235d4c"
ANCHOR_CONTENT = "2b979d69f6a57c13b38337f5dda4d52aa07debc2ccbd6857b3cb00ba9d591fec"
row17 = next(r for r in extraction_results if r["plan_stem"] == "S85-W5-7")
anchor_match = (row17["audit_sha256"] == ANCHOR_AUDIT and row17["content_sha256"] == ANCHOR_CONTENT)
print(f"[anchor-cross-check] W5-7 audit matches plan §0.11 pin: {anchor_match}")
if not anchor_match:
    print(f"[anchor-cross-check] FAIL — W5-7 audit={row17['audit_sha256']} content={row17['content_sha256']}")
    print(f"[anchor-cross-check] expected audit={ANCHOR_AUDIT} content={ANCHOR_CONTENT}")
    sys.exit(2)


# ----------------------------------------------------------------------
# 5. Registry write — append rows under each §VII slot (substitution-chain step 4)
# ----------------------------------------------------------------------

# Group rows by slot for clean append.
rows_by_slot: dict[str, list[dict]] = {}
for r in extraction_results:
    if r["status"] != "EXTRACTED":
        continue
    rows_by_slot.setdefault(r["vii_slot"], []).append(r)

# Idempotency check (cross-check 3): if a row's actual_stem already appears
# under a §VII landing block with both SHAs, skip that row's append.
n_skipped_existing = 0  # (local)
for slot, rows in list(rows_by_slot.items()):
    keep = []
    for r in rows:
        # Idempotency = grep for the actual-stem anchored in a permanent-row context
        # together with the audit_sha256 (full 64) on the same line. If both
        # appear in the registry simultaneously, treat as already landed.
        already_landed = (r["actual_stem"] in registry_text) and (r["audit_sha256"] in registry_text)
        if already_landed:
            print(f"[idempotent-skip] {r['plan_stem']} ({r['actual_stem']}) already in registry, skipping")
            n_skipped_existing += 1
            continue
        keep.append(r)
    rows_by_slot[slot] = keep


# Compose the new registry content (append at end of file, under a single
# 2026-04-26 S86-W1a-1 META landing section with per-slot sub-blocks).
date_today = "2026-04-26"
header_block = (
    f"\n---\n\n"
    f"## §VII — S86-W0-PERM-LAND-17 — 17 W0-W5 Theorem-Grade PASSes "
    f"(connes-ncg-theorist, S86 W1a-1, {date_today})\n"
    f"\n"
    f"**Gate**: `S86-W0-PERM-LAND-17` (META, registry hygiene). "
    f"**Source**: `computations/session-85/s85_gate_verdicts.txt` content_sha256 "
    f"= `{s85_sha}`. **Producing script**: `computations/session-86/s86_w1a_t1_perm_land_17.py`. "
    f"**Tolerance rule**: THEOREM (every SHA verbatim 64 hex chars). "
    f"**Substrate framing**: All 17 entries are GEOMETRIC content of the spectral "
    f"triple `(A, H, D_K)` — cluster-span identities, Dai-Freed torsions, KO-6 "
    f"sign flows, HP^k cohomology dim shifts, BdG-band CMB indices, two-layer "
    f"obstructions, fold-uniqueness propositions. None are phononic excitations; "
    f"all are walls in the regulator-class structural floor (`session-86-context.md` §1.5).\n"
    f"\n"
    f"**Slot allocation note**: Of the 4 §VII slots cited by the 17 stems, "
    f"§VII.K-PROP, §VII.K-META, and §VII.P pre-existed at S85 close. "
    f"§VII.B was an OPEN ROMAN-LETTER SLOT under the §VII alphabet "
    f"(per §VII.Ω slot-allocation note: \"§VII.P through §VII.Z as open slots\"). "
    f"Under this S86-W1a-1 META landing, §VII.B is opened by sub-section header "
    f"with the two W0-W5 rows that target it ({{HP^1 dim-CM2008 (W0-16); two-layer "
    f"obstruction n_joint=0/5 (W5-7)}}); see §VII.B sub-block below. No cascade "
    f"required.\n"
)

slot_order = ["§VII.K-PROP", "§VII.K-META", "§VII.B", "§VII.P"]
slot_blocks: list[str] = [header_block]

# Per-slot canonical row form — one table per slot.
COLUMN_HEADER = (
    "| §VII slot | Plan stem | Theorem statement (one line) | "
    "audit_sha256 (64 hex) | content_sha256 (64 hex) | session |\n"
    "|:----------|:----------|:------------------------------|:----------------------|:------------------------|:--------|\n"
)

for slot in slot_order:
    rows_here = rows_by_slot.get(slot, [])
    if not rows_here:
        continue
    if slot == "§VII.B":
        # New slot — write a sub-header with the canonical opening blurb
        # consistent with §VII.O / §VII.P / §VII.Q precedent.
        slot_blocks.append(
            f"\n### §VII.B — Two-Layer Obstruction Family + HP^1 Cohomology Stability "
            f"(opened S86 W1a-1 from S85 W0-16 + W5-7, {date_today})\n\n"
            f"**Slot-allocation note**: §VII.B opened as a one-time S86-W1a-1 META "
            f"slot allocation; previously open per §VII.Ω registry note. Two W0-W5 "
            f"PASSes land here: HP^1 dim-CM2008 integer-stability (W0-16) and the "
            f"Two-Layer Obstruction Theorem n_joint = 0/5 (W5-7). Both are walls in "
            f"the spectral-triple regulator-class structural floor.\n\n"
        )
    else:
        slot_blocks.append(
            f"\n### {slot} — S86-W1a-1 sub-block ({date_today})\n\n"
            f"The following theorem-grade PASSes land in {slot} per S86-W1a-1 "
            f"plan §6 stem -> slot mapping. Each row preserves the full 64-char "
            f"dual-SHA from `s85_gate_verdicts.txt` verbatim.\n\n"
        )
    slot_blocks.append(COLUMN_HEADER)
    for r in rows_here:
        # Escape any pipe characters in the one-liner to avoid breaking the table
        ol = r["one_liner"].replace("|", "\\|")
        slot_blocks.append(
            f"| {slot} | `{r['plan_stem']}` (= `{r['actual_stem']}`) "
            f"| {ol} | `{r['audit_sha256']}` | `{r['content_sha256']}` | session=85 |\n"
        )

# Closing footer
footer_block = (
    f"\n**Anchor SHA**: This META-landing's input-pin-map closure (script "
    f"audit_sha256 emitted to `s86_gate_verdicts.txt`):\n\n"
    f"  audit_sha256 = `{audit_closure_sha}`\n\n"
    f"**Cross-references**: §VII.K-PROP (CC-5 propagation identity, S84 W3-21); "
    f"§VII.K-META (W-3 META-PRINCIPLE, S83); §VII.P (Borel-summability floor, S85 W9-1); "
    f"§VII.B (this entry — opened); §VII.R (single-name conflation methodology, S86 W0b-2); "
    f"§VII.S (three-layer adjudication, S86 W0b-3).\n\n"
    f"**Provenance**: producing-script `computations/session-86/s86_w1a_t1_perm_land_17.py`; "
    f"JSON map `computations/session-86/s86_w1a_t1_perm_land_17.json`; verdict line "
    f"`computations/session-86/s86_gate_verdicts.txt` ({GATE_ID}); working paper "
    f"`sessions/archive/session-86/session-86-w1a-workingpaper.md` §W1a-1.\n\n"
    f"---\n"
)
slot_blocks.append(footer_block)

new_block = "".join(slot_blocks)

# Append to registry
with open(REGISTRY_MD, "a", encoding="utf-8") as f:
    f.write(new_block)

n_landed = sum(len(rows_by_slot.get(s, [])) for s in slot_order)
print(f"[registry-append] new rows appended: {n_landed}")

registry_post_sha = file_sha256(REGISTRY_MD)
print(f"[output] registry_post_sha256 = {registry_post_sha}")


# ----------------------------------------------------------------------
# 6. Write JSON map
# ----------------------------------------------------------------------

json_map = {
    r["plan_stem"]: {
        "actual_stem": r["actual_stem"],
        "audit_sha256": r["audit_sha256"],
        "content_sha256": r["content_sha256"],
        "vii_slot": r["vii_slot"],
        "source_line_number_in_s85_verdicts": r["source_line_number_in_s85_verdicts"],
        "one_liner": r["one_liner"],
        "status": r["status"],
    }
    for r in extraction_results
}
with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(
        {
            "gate_id": GATE_ID,
            "scheme": SCHEME,
            "convention": CONVENTION,
            "input_pin_map": input_pin_map,
            "audit_sha256_closure": audit_closure_sha,
            "registry_pre_sha256": registry_pre_sha,
            "registry_post_sha256": registry_post_sha,
            "n_extracted": n_pass,
            "n_failed": n_fail,
            "n_skipped_existing": n_skipped_existing,
            "n_landed": n_landed,
            "missing_stems": missing_stems,
            "rows": json_map,
            "anchor_cross_check_w5_7": {
                "expected_audit": ANCHOR_AUDIT,
                "expected_content": ANCHOR_CONTENT,
                "actual_audit": row17["audit_sha256"],
                "actual_content": row17["content_sha256"],
                "match": anchor_match,
            },
        },
        f,
        indent=2,
        sort_keys=True,
    )
print(f"[output] json_map -> {OUT_JSON}")


# ----------------------------------------------------------------------
# 7. Verdict line + companion (substitution-chain step 4)
# ----------------------------------------------------------------------

if n_pass == 17 and n_fail == 0:
    verdict = "PASS"
    value_field = f"value=17"
elif n_pass >= 1:
    verdict = "INFO"
    value_field = f"value={n_pass}/17 missing={','.join(missing_stems)}"
else:
    verdict = "FAIL"
    value_field = f"value=0/17 missing={','.join(missing_stems)}"

verdict_line = (
    f"{GATE_ID}: {verdict} -- {value_field} scheme={SCHEME} "
    f"convention={CONVENTION} L_max={L_MAX_TAG} "
    f"audit_sha256={audit_closure_sha} content_sha256={registry_post_sha} "
    f"schema_version={SCHEMA_VERSION}\n"
)
companion_line = (
    f"# audit_sha256 companion row: {GATE_ID} "
    f"audit={audit_closure_sha[:16]} content={registry_post_sha[:16]} "
    f"# canonicalized {GATE_ID}\n"
)

with open(OUT_VERDICTS, "a", encoding="utf-8") as f:
    f.write(verdict_line)
    f.write(companion_line)

print("-" * 78)
print(f"[verdict] {verdict_line.strip()}")
print(f"[companion] {companion_line.strip()}")
print("-" * 78)
print(f"[output 4-tuple] (value={n_pass}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_TAG})")
print(f"[done] {GATE_ID} -> {verdict}")

sys.exit(0)
