"""
S87 W11-meta methodology-class wave landing script (orchestrator-direct-write).

Lands 3 methodology gates in one atomic pass per the S87 W11-meta plan-block at
`sessions/session-plan/session-87-plan-w11-meta.md`:

- METH-1: cross-pillar-bridge-anatomy.md K-counter advancement K=1->2 (W11-5 = FWD-C3 instance #2)
- METH-2: math-scripts.md plan-authorship lesson on D_K block-diagonality (W11-2 + W11-3 dual calibration)
- METH-3: epistemic-discipline.md PRU Class 8.2 corpus closure (W11-1 V_4 supersession event)

Per `.claude/rules/wave-classification.md` §"Dispatch consequences", METHODOLOGY-class
waves are orchestrator-direct-write; this script encapsulates the 3 rule-file edits
+ allowlist appends + verdict-line emissions for atomicity (matching the
W11-2/3/5 one-shot writer pattern from epistemic-discipline.md §"Registry-Write
Hygiene under Parallel-Writer Race").

Run: phonon-exflation-sim/.venv312/Scripts/python.exe computations/_shared/_s87_w11_meta_methodology_landing.py
"""

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------- Helpers ------------------------------------------------------------

def sha256_hex(data: bytes | str) -> str:
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()

def file_sha256(path: Path) -> str:
    return sha256_hex(path.read_bytes())

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")

# ---------- Step 1: extract gate-blocks from plan + compute sha256_of_plan_block

PLAN_BLOCK_PATH = ROOT / "sessions" / "session-plan" / "session-87-plan-w11-meta.md"
plan_text = read_text(PLAN_BLOCK_PATH)

def extract_gate_block(plan: str, anchor: str) -> str:
    """Extract the §METH-N gate-block as the substring from `## §<anchor>.` up to
    the next `## §` header or `---` separator (whichever first).
    """
    start_re = re.compile(rf"^## §{re.escape(anchor)}\.", re.MULTILINE)
    m_start = start_re.search(plan)
    if not m_start:
        raise RuntimeError(f"plan-block anchor §{anchor} not found")
    rest = plan[m_start.start():]
    # next §-header or trailing horizontal rule (---) followed by §-header or end
    next_header = re.compile(r"^## §METH-", re.MULTILINE).search(rest, pos=1)
    end = len(rest) if next_header is None else next_header.start()
    block = rest[:end].rstrip() + "\n"
    return block

GATES = ["METH-1", "METH-2", "METH-3"]
gate_blocks = {g: extract_gate_block(plan_text, g) for g in GATES}
plan_block_sha = {g: sha256_hex(gate_blocks[g]) for g in GATES}

print("=" * 70)
print("STEP 1: sha256_of_plan_block per gate-block")
print("=" * 70)
for g in GATES:
    print(f"  {g}: {plan_block_sha[g]}  (block bytes: {len(gate_blocks[g].encode('utf-8'))})")

# ---------- Step 2: METH-1 cross-pillar-bridge-anatomy.md edit ----------------

CPB_PATH = ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
cpb_pre = read_text(CPB_PATH)
cpb_pre_sha = sha256_hex(cpb_pre)

# Idempotency: if METH-1 edits already landed (from prior aborted run), reuse
# the original pre-SHA for the input-pin map and skip the in-script edits.
CPB_ORIGINAL_PRE_SHA = "8f12e22c8b5b72afed1fedca196fef808d926b801a821a88a1a1646d2675b8cc"
CPB_EXPECTED_POST_SHA = "17eff567d8cf7fc02e23f9584e69675bf58b0e040d459879fef89bbf975f810b"
if cpb_pre_sha == CPB_EXPECTED_POST_SHA:
    print("[METH-1] already landed (post-SHA matches); reusing prior edits idempotently.")
    cpb_post = cpb_pre
    cpb_pre_sha = CPB_ORIGINAL_PRE_SHA  # restore the original pre-SHA for audit reproducibility
else:
    # Edit 1a: header K=1 -> K=2 (line 100)
    cpb_post = cpb_pre.replace(
        "### Status: SUGGESTION (NOT MANDATORY) at K=1",
        "### Status: SUGGESTION (NOT MANDATORY) at K=2",
        1,
    )
    assert cpb_post != cpb_pre, "METH-1 edit 1a failed: K=1 header not found"

    # Edit 1b: row 2 of corpus table (line 107)
    old_row2 = "| 2 | — | — | (awaits future high-density workshop) |"
    new_row2 = (
        "| 2 | S87 W11-5 (volovik PRIMARY) "
        "| Pillar IV ↔ Pillar V (substrate spectral-excess ↔ 3He-B BdG-undoubled excess at polycritical pressure) "
        "| REGISTRY-FAIL §VII.AJ NOT eligible per §\"Registry-PASS criterion\" "
        "(Level-3 1.029 violates Level-2 0.05 by ~21×); calibration corpus K=1→2 |"
    )
    assert old_row2 in cpb_post, "METH-1 edit 1b failed: row 2 placeholder not found"
    cpb_post = cpb_post.replace(old_row2, new_row2, 1)

    # Edit 1c: narrative line 110 K=1 -> K=2
    old_narr = "K = 1  <  K_promotion = 3  ⇒  status = **SUGGESTION** (NOT MANDATORY).  Promotion event triggers when a 2nd and 3rd calibration instance land"
    new_narr = "K = 2  <  K_promotion = 3  ⇒  status = **SUGGESTION** (NOT MANDATORY).  Promotion event triggers when a 3rd calibration instance lands"
    assert old_narr in cpb_post, "METH-1 edit 1c failed: narrative not found"
    cpb_post = cpb_post.replace(old_narr, new_narr, 1)

    # Edit 1d: calibration-corpus tracking instance #2 line 159
    old_inst2 = "- instance #2: SUGGESTED candidate from {FWD-C1, FWD-C2, FWD-C3} (whichever lands first at S88+)."
    new_inst2 = (
        "- instance #2: S87 W11-5 (volovik PRIMARY) — FWD-C3 = Pillar IV ↔ Pillar V "
        "(substrate cocycle-derived spectral excess ↔ 3He-B BdG-undoubled excess at polycritical pressure P_pc≈21.22 bar, T_pc≈2.273 mK). "
        "REGISTRY-FAIL: Level-3 ratio_mismatch=1.029 violates Level-2 envelope 0.05 by ~21×; "
        "structural cause = M_3(C) Cartan-zone weight non-negligible at L_max=10 in multiplicity-weighted Mellin scheme. "
        "Inheritance theorem at S86 W1b-T8 PRESERVED (FAIL is observable-construction-specific, not bridge-map-defective). "
        "Carry-forward: S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY (M_3(C) Cartan-zone pre-projection)."
    )
    assert old_inst2 in cpb_post, "METH-1 edit 1d failed: instance #2 placeholder not found"
    cpb_post = cpb_post.replace(old_inst2, new_inst2, 1)

    write_text(CPB_PATH, cpb_post)

cpb_post_sha = sha256_hex(cpb_post)

# Compute METH-1 dual-SHA
# audit_sha256 = SHA over input-pin map (canonicalized JSON of pin name -> pin SHA)
meth1_input_pin_map = {
    "cross-pillar-bridge-anatomy.md_pre_edit": cpb_pre_sha,
    "s87_gate_verdicts.txt_W11-5_audit_sha256": "e1aef7ce0deaed2d85d8031fce1d009384ed0842ffb25585e880a5f475efd9aa",
    "session-87-results-workingpaper.md_W11-5_section_anchor": "lines_9090_to_9275",
    "plan_block_W11-meta_METH-1_sha": plan_block_sha["METH-1"],
}
meth1_audit_sha = sha256_hex(json.dumps(meth1_input_pin_map, sort_keys=True))

# content_sha256 = SHA over rule-file diff (full post-edit content for METHODOLOGY-class)
meth1_content_sha = cpb_post_sha

print()
print("=" * 70)
print("STEP 2: METH-1 cross-pillar-bridge-anatomy.md edits")
print("=" * 70)
print(f"  pre-edit  SHA: {cpb_pre_sha}")
print(f"  post-edit SHA: {cpb_post_sha}")
print(f"  diff bytes: {len(cpb_post.encode('utf-8')) - len(cpb_pre.encode('utf-8'))}")
print(f"  audit_sha256:   {meth1_audit_sha}")
print(f"  content_sha256: {meth1_content_sha}")

# ---------- Step 3: METH-2 math-scripts.md edit ------------------------------

MS_PATH = ROOT / ".claude" / "rules" / "math-scripts.md"
ms_pre = read_text(MS_PATH)
ms_pre_sha = sha256_hex(ms_pre)

# Append new sub-section after §"### Root-count heuristic severity-1 flag" within §"Machinery-Feasibility Audit"
# The Root-count subsection ends at the start of "## Changelog v3" section.
new_subsection = """

### D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check (S87 W11 calibration)

> **Provenance**: S87 W11-2 (CF-67) `S87-PARTITION-STABILITY-4STRATUM` + W11-3 (CF-68) `S87-STRATUM3-LMAX-SCAN` joint calibration corpus (connes-ncg-theorist; 2026-04-30). Both gates surfaced the same upstream plan-authorship gap: plan machinery pin assumed irrep CONSTRUCTION at L_max ≥ 10 is feasible, but recursive Casimir-projection cost is super-polynomial in dim(p,q). Both fixed in-session via different structural arguments (W11-2: Casimir-bound + cache cross-check; W11-3: Friedrich-Bär structural-saturation theorem).

#### Lesson

D_K is **BLOCK-DIAGONAL by Peter-Weyl decomposition**: D_K = ⊕_{(p,q)} D_{(p,q)} where each block acts on V_{(p,q)} ⊗ ℂ^16. Sparse storage is **NOT NECESSARY** at any L_max — the largest single block at L_max=15 is dim 9792 (sectors (15,0)/(0,15)), dense storage 1.53 GB which fits comfortably in 17.1 GB VRAM with margin > 11×. Plan machinery pins that prescribe sparse-Lanczos at high L_max on the assumption of dense 640k×640k storage are factually incorrect.

The operative computational cost is **irrep CONSTRUCTION**, NOT diagonalization. `dirac_spectrum.get_irrep(p,q)` builds higher (p,q) recursively via Casimir projection on tensor products with the fundamental — super-polynomial in dim(p,q). Empirical measurements:
- W11-2: irrep at p+q=10 sector takes >5 minutes single-thread CPU (e.g., (5,5) of dim 216 via Casimir-projection from (1,1)×(4,4) of dim 64).
- W11-3: irrep (13,0) construction did NOT complete within 10-minute wall time; full-spectrum reconstruction at L_max ≥ 13 is therefore **empirically infeasible** within any agent timeslot.

#### Pre-check protocol (mandatory at plan-freeze for any gate scanning L_max ≥ 10)

Plan authors MUST verify recursive Casimir-projection feasibility BEFORE pinning sparse-Lanczos at high L_max via one of two structural arguments:

1. **Casimir-bound + cache cross-check** (W11-2 precedent): bound the worst-case sector (p,q) contributing to the bottom-K observable via the |λ|_min^(p,q)(τ) ≈ √(C_2(p,q)) / r(τ) Casimir scaling × Jensen-deformation-spread factor. Worst-case sector with C_2(p,q) below the observable's |λ|_max ceiling determines the required L_max truncation. Cross-validate against the L_max=12 master spectrum cache `s84_spectrum_cache_L12_tau019.npz` filtered at L_max_operational vs L_max_plan; reject the plan-pinned L_max if the operational truncation reproduces the observable bit-for-bit (`truncation_consistent = True` flag in npz output).

2. **Friedrich-Bär structural-saturation theorem** (W11-3 precedent): for each sector (p,q), define empirical Friedrich-Bär ratio η_FB(p,q) = |λ|_min(p,q) / √(C_2(p,q) + 1) on the L_max=12 master cache. Pin η_FB_lower as 8-10% safety margin below the empirical floor (W11-3: η_FB_lower = 0.40, 8.4% below empirical (1,1)-sector floor 0.4365). Then for any L_max ≥ 12, NEW-sector eigenvalues are bounded below by η_FB_lower · √(C_2(p+q=L_max)+1); if this lower bound exceeds the bottom-K observable's ceiling, the bottom-K is structurally L_max-saturated at L_max=12 and no diagonalization at higher L_max is needed.

#### Calibration corpus

| # | Gate | Mitigation strategy | Empirical result |
|:---|:-----|:-------------------|:-----------------|
| 1 | S87 W11-2 (`S87-PARTITION-STABILITY-4STRATUM`) | Casimir-bound argument: worst-case sector p+q ≤ 4 contributes to bot-20; L_max=6 = 2-level safety margin. Cross-checked against L_max=12 cache filtered at p+q ≤ 6 vs ≤ 10 (truncation_consistent = True). | INFO at pass_count=10/11; cardinality vector (2,4,8,6) bit-identical at L_max=6 + L_max=10 truncations of master cache. Plan §W11-2 §6 nominally pinned L_max=10; operational pin L_max=6 with verdict-line convention tag `4-stratum-canonical-W12-VII.K-PROP-Lmax6-Casimir-bound-truncation`. |
| 2 | S87 W11-3 (`S87-STRATUM3-LMAX-SCAN`) | Friedrich-Bär saturation theorem: η_FB_lower = 0.40 (8.4% below empirical floor 0.4365 at sector (1,1)); NEW-sector intrusion margins +2.16 to +2.56 in M_KK units above stratum-4 ceiling 0.845; analytically certifies bottom-20 invariance for ALL L_max ≥ 12. | PASS at value=4; |S_3(L_max)| = 8 invariant across L_max ∈ {12, 13, 14, 15} — extends trivially to L_max → ∞ via the saturation theorem. Verdict-line scheme `block-diagonal-cache-plus-friedrich-baer-bound`. |

#### Plan-authorship discipline

For S88+ plan authorship, the orchestrator MUST:

1. Before pinning any L_max ≥ 10 in a gate's machinery pin, verify recursive Casimir-projection feasibility per the Casimir-bound or Friedrich-Bär protocol above.
2. If the plan-pinned L_max is structurally redundant under the protocol, downgrade the operational L_max to the smallest p+q satisfying the Casimir-bound argument; record both `L_max_plan` and `L_max_operational` in the npz output keys.
3. If the plan-pinned L_max is empirically infeasible (irrep construction timeout) but the bottom-K observable is structurally saturated per Friedrich-Bär, replace sparse-Lanczos prescription with the saturation-theorem analytic argument and tag the verdict-line scheme accordingly.
4. Honest disclosure of any operational deviation from plan §6 machinery pin in the working-paper §"Methodology" subsection + verdict-line convention/scheme tag is **mandatory** per `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1 boundary (the deviation is in-session structural correction, NOT convention-shopping, IFF honestly disclosed; absent disclosure it falls under Class 1).

This pre-check closes the upstream plan-authorship gap surfaced jointly by W11-2 + W11-3.
"""

# Insert at the end of §"### Root-count heuristic severity-1 flag" subsection,
# i.e., immediately before the next ## section header. The Root-count subsection
# is followed by "## Changelog v3" header (line 255 in source). The Root-count
# end-text is wrapped across two lines in the source ("(W13-4 site #9\n
# exemplar: ... mismatch).") so a single-line literal marker fails. Use the
# stable next-section anchor instead and insert BEFORE it.
changelog_anchor = "## Changelog v3 (S85 W-3 v2 + 5A v2 union, landed S86 W0a-1)"
MS_EXPECTED_POST_MARKER = "### D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check (S87 W11 calibration)"
if MS_EXPECTED_POST_MARKER in ms_pre:
    print("[METH-2] already landed (subsection marker present); reusing prior edit idempotently.")
    ms_post = ms_pre
else:
    assert changelog_anchor in ms_pre, "METH-2: ## Changelog v3 anchor not found in math-scripts.md"
    ms_post = ms_pre.replace(
        changelog_anchor,
        new_subsection.lstrip("\n") + "\n" + changelog_anchor,
        1,
    )
    assert ms_post != ms_pre, "METH-2 edit failed: no change made"

write_text(MS_PATH, ms_post)
ms_post_sha = sha256_hex(ms_post)

meth2_input_pin_map = {
    "math-scripts.md_pre_edit": ms_pre_sha,
    "s87_gate_verdicts.txt_W11-2_audit_sha256": "008cf3c98f28eca8a3c9b142673be4997c92e62bdcb2c1927b67db2d6e04315d",
    "s87_gate_verdicts.txt_W11-3_audit_sha256": "f19bcd5e25969374c7ab68774de92ef927cd527cffecdffbe7b0692f1ab6e5fd",
    "session-87-results-workingpaper.md_W11-2_section_anchor": "lines_8907_to_9090",
    "session-87-results-workingpaper.md_W11-3_section_anchor": "lines_8928_to_9093",
    "plan_block_W11-meta_METH-2_sha": plan_block_sha["METH-2"],
}
meth2_audit_sha = sha256_hex(json.dumps(meth2_input_pin_map, sort_keys=True))
meth2_content_sha = ms_post_sha

print()
print("=" * 70)
print("STEP 3: METH-2 math-scripts.md edits")
print("=" * 70)
print(f"  pre-edit  SHA: {ms_pre_sha}")
print(f"  post-edit SHA: {ms_post_sha}")
print(f"  diff bytes: {len(ms_post.encode('utf-8')) - len(ms_pre.encode('utf-8'))}")
print(f"  audit_sha256:   {meth2_audit_sha}")
print(f"  content_sha256: {meth2_content_sha}")

# ---------- Step 4: METH-3 epistemic-discipline.md edit ----------------------

ED_PATH = ROOT / ".claude" / "rules" / "epistemic-discipline.md"
ed_pre = read_text(ED_PATH)
ed_pre_sha = sha256_hex(ed_pre)

# Append closure bullet to existing Class 8.2 calibration corpus.
# Find the existing "**Class 8.2 calibration corpus**" entry.
old_class82 = '**Class 8.2 calibration corpus**: S86 W-12 "Z_4 or similar" admitted Klein-four V_4 as "similar" via cardinality match despite structural distinction via element orders (V_4 = [1,2,2,2] vs Z_4 = [1,2,4,4]). The pre-registered criterion was "PASS-monodromy = sweep returns to identity after 4 sheets (Z_4 or similar)"; the "or similar" token was unintentionally permissive — the workshop\'s actual finding (V_4) satisfied the literal rubric reading despite structurally falsifying Z_4.'
assert old_class82 in ed_pre, "METH-3: Class 8.2 calibration corpus anchor not found"

new_class82_addendum = (
    "\n\n**Class 8.2 calibration corpus — instance #1 closure (S87 W11-1, 2026-04-30)**: "
    "S87 W11-1 (`S87-MONODROMY-V_4-EXPLICIT`, connes-ncg-theorist) provides the empirical confirmation of W-12's diagnosis. "
    "The substrate-level V_4 PARALLELOGRAM IDENTITY `A_n^(e) − A_n^(a) − A_n^(b) + A_n^(ab) = 0` was tested at τ_fold=0.190, L_max=10 under the natural Cartan-toral V_4 character (σ_M=(-1)^p, σ_C=(-1)^q on SU(3) Peter-Weyl indices) — FAIL composite at max_dev=1.16 (per-n rel_dev: 1.16 / 0.86 / 0.21 for n ∈ {0,2,4}, all 9-11 OOM above the 1e-9 FAIL ceiling; Pathway-2 substrate-IS cross-check at 78,064 cached eigvals at L_max=10 confirms FAIL at same OOM). "
    "The Z_4 alternative is **independently falsified** by structural element-order mismatch (V_4 = [1,2,2,2] vs Z_4 = [1,2,4,4]; CC2 in W11-1 §W11-1 confirmed Sage-symbolic). "
    "The supersession-event marker `supersedes=S87-MONODROMY-Z4-LANDING_per_PRU_Class_8_2` is encoded in the W11-1 verdict-line `value=` field per HIGH-DENSITY WORKSHOP TEMPLATE T2-5 (see `agent-standards.md` §\"HIGH-DENSITY WORKSHOP TEMPLATE T2-5\" multi-output decomposition slot 1: literal pre-reg verdict slot). "
    "**Instance #1 closes**: W-12 was the diagnosis (\"Z_4 or similar\" rubric admits V_4 via cardinality match); W11-1 is the empirical confirmation that BOTH V_4 (under Cartan-toral character) AND Z_4 fail at substrate level. "
    "W11-1 leaves 3 surviving V_4 candidate incarnations (regulator-coset map [also FAILed at n=2], V_4-on-strata [structurally supported by W11-2 INFO + W11-3 PASS], V_4-on-triality-mod-2 [open]); the Class 8.2 lesson stands: rubric tokens like \"or similar\" / \"or equivalent\" / \"any of [...]\" are unintentionally permissive on cardinality-only matches that admit structurally distinct groups via element-order signature. "
    "Class 8.2 K-counter: 1 instance closed; promotion to MANDATORY at K=3 still requires 2 more substrate-level Class-8.2 manifestations."
)

ED_EXPECTED_POST_MARKER = "**Class 8.2 calibration corpus — instance #1 closure (S87 W11-1, 2026-04-30)**"
if ED_EXPECTED_POST_MARKER in ed_pre:
    print("[METH-3] already landed (closure marker present); reusing prior edit idempotently.")
    ed_post = ed_pre
else:
    ed_post = ed_pre.replace(old_class82, old_class82 + new_class82_addendum, 1)
    assert ed_post != ed_pre, "METH-3 edit failed"

write_text(ED_PATH, ed_post)
ed_post_sha = sha256_hex(ed_post)

meth3_input_pin_map = {
    "epistemic-discipline.md_pre_edit": ed_pre_sha,
    "s87_gate_verdicts.txt_W11-1_audit_sha256": "8a4419a830e0e509bad2b4e567310959756523d0aa84d9ec9d81b9f147abe15b",
    "session-87-results-workingpaper.md_W11-1_section_anchor": "lines_8768_to_8908",
    "plan_block_W11-meta_METH-3_sha": plan_block_sha["METH-3"],
}
meth3_audit_sha = sha256_hex(json.dumps(meth3_input_pin_map, sort_keys=True))
meth3_content_sha = ed_post_sha

print()
print("=" * 70)
print("STEP 4: METH-3 epistemic-discipline.md edits")
print("=" * 70)
print(f"  pre-edit  SHA: {ed_pre_sha}")
print(f"  post-edit SHA: {ed_post_sha}")
print(f"  diff bytes: {len(ed_post.encode('utf-8')) - len(ed_pre.encode('utf-8'))}")
print(f"  audit_sha256:   {meth3_audit_sha}")
print(f"  content_sha256: {meth3_content_sha}")

# ---------- Step 5: methodology-wave-allowlist.md row append -----------------

ALL_PATH = ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
all_pre = read_text(ALL_PATH)
all_pre_sha = sha256_hex(all_pre)

new_allowlist_rows = (
    f"| W11-meta-1 | S87     | S87-METH-CROSS-PILLAR-BRIDGE-K-COUNTER-UPDATE (cross-pillar-bridge-anatomy.md K-counter advancement K=1→2 from W11-5 FWD-C3 instance #2 landing; orchestrator-direct-write per wave-classification.md §\"Dispatch consequences\") | {plan_block_sha['METH-1']} |\n"
    f"| W11-meta-2 | S87     | S87-METH-D_K-BLOCK-DIAGONAL-PLAN-AUTHORSHIP-LESSON (math-scripts.md §\"Machinery-Feasibility Audit\" extension with D_K Block-Diagonality pre-check; W11-2 + W11-3 dual calibration corpus) | {plan_block_sha['METH-2']} |\n"
    f"| W11-meta-3 | S87     | S87-METH-PRU-CLASS-8-2-CORPUS-CLOSURE (epistemic-discipline.md §\"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension\" Class 8.2 corpus closure with W11-1 V_4 supersession event) | {plan_block_sha['METH-3']} |\n"
)

# Insert immediately after the last existing W9a-2 row.
last_w9a2_marker = "| W9a-2   | S87     | S87-A_S-SURVIVING-ROUTE-RANK-LANDING (L3+T3 cross-domain-converged α_s ranked-route table `(iii)≻(iv)≻(i)≻(ii)` landing in falsifier-master-inventory.md; closes T7-W9-FI-4 deferred install; CF-57 / W-9 CF-4; mack-cosmic-bridge sole writer) | e5accb49994ca595b956b9347cd13055fa0529c15612dff0ca1e6b3a2e92fa06 |"
assert last_w9a2_marker in all_pre, "Allowlist W9a-2 anchor not found"
all_post = all_pre.replace(
    last_w9a2_marker,
    last_w9a2_marker + "\n" + new_allowlist_rows.rstrip(),
    1,
)
assert all_post != all_pre, "Allowlist append failed"

write_text(ALL_PATH, all_post)
all_post_sha = sha256_hex(all_post)

print()
print("=" * 70)
print("STEP 5: methodology-wave-allowlist.md append (3 rows)")
print("=" * 70)
print(f"  pre-edit  SHA: {all_pre_sha}")
print(f"  post-edit SHA: {all_post_sha}")
print(f"  diff bytes: {len(all_post.encode('utf-8')) - len(all_pre.encode('utf-8'))}")

# ---------- Step 6: append 3 verdict lines + dual-SHA companions -------------

VERDICT_PATH = ROOT / "computations" / "session-87" / "s87_gate_verdicts.txt"

verdict_entries = [
    {
        "gate_id": "S87-METH-CROSS-PILLAR-BRIDGE-K-COUNTER-UPDATE",
        "value": "K_advanced_1_to_2;instance_2=W11-5_FWD-C3_REGISTRY-FAIL_Tier3_violates_Tier2_by_21x;K_promotion_threshold=3;status_remains_SUGGESTION",
        "scheme": "orchestrator-direct-rule-file-edit",
        "convention": "cross-pillar-bridge-anatomy-K-counter-update",
        "L_max": "N/A",
        "audit_sha": meth1_audit_sha,
        "content_sha": meth1_content_sha,
    },
    {
        "gate_id": "S87-METH-D_K-BLOCK-DIAGONAL-PLAN-AUTHORSHIP-LESSON",
        "value": "subsection_appended;calibration_corpus=W11-2_Casimir-bound+W11-3_FB-saturation;target=math-scripts.md_Machinery-Feasibility-Audit",
        "scheme": "orchestrator-direct-rule-file-edit",
        "convention": "math-scripts-feasibility-pre-check-extension",
        "L_max": "N/A",
        "audit_sha": meth2_audit_sha,
        "content_sha": meth2_content_sha,
    },
    {
        "gate_id": "S87-METH-PRU-CLASS-8-2-CORPUS-CLOSURE",
        "value": "class_8_2_corpus_closure_appended;W11-1_V4_supersession_event_FAIL_max_dev=1.16;Z4_alternative_falsified_via_element_order_mismatch",
        "scheme": "orchestrator-direct-rule-file-edit",
        "convention": "epistemic-discipline-PRU-class-8-2-corpus-closure",
        "L_max": "N/A",
        "audit_sha": meth3_audit_sha,
        "content_sha": meth3_content_sha,
    },
]

verdict_lines_text = ""
for v in verdict_entries:
    canonical = (
        f"{v['gate_id']}: PASS -- "
        f"value='{v['value']}' "
        f"scheme={v['scheme']} "
        f"convention={v['convention']} "
        f"L_max={v['L_max']} "
        f"audit_sha256={v['audit_sha']} "
        f"content_sha256={v['content_sha']} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={v['audit_sha'][:16]} "
        f"content_sha256_short={v['content_sha'][:16]} # "
        f"{v['gate_id']} dual-SHA companion row (W9a-99 split; METHODOLOGY-class orchestrator-direct-write per wave-classification.md §\"Dual-SHA closure for METHODOLOGY-class\")\n"
    )
    verdict_lines_text += canonical + companion

# Append to verdict file (append mode is canonical per gate-verdicts.md)
with VERDICT_PATH.open("a", encoding="utf-8", newline="\n") as f:
    f.write(verdict_lines_text)

print()
print("=" * 70)
print("STEP 6: verdict lines appended to s87_gate_verdicts.txt")
print("=" * 70)
print(f"  6 lines (3 canonical + 3 companion) appended.")
for v in verdict_entries:
    print(f"    {v['gate_id']}: PASS")

# ---------- Step 7: SHA uniqueness verification (sig_5 ladder) ---------------

verdict_text = read_text(VERDICT_PATH)
all_audit_shas = re.findall(r"audit_sha256=([0-9a-f]{64})", verdict_text)
unique_count = len(set(all_audit_shas))
total_count = len(all_audit_shas)

print()
print("=" * 70)
print("STEP 7: SHA uniqueness check (sig_5 ladder)")
print("=" * 70)
print(f"  Total audit_sha256 occurrences in s87_gate_verdicts.txt: {total_count}")
print(f"  Unique audit_sha256 values: {unique_count}")
if total_count == unique_count:
    print(f"  ✓ SHA uniqueness PRESERVED (sig_5 ladder OK).")
else:
    print(f"  ✗ DUPLICATE audit_sha256 detected — sig_5 violation.")

# Assert the 3 new SHAs are present
for v in verdict_entries:
    assert v["audit_sha"] in verdict_text, f"verdict line for {v['gate_id']} missing"
    assert v["content_sha"] in verdict_text, f"content_sha for {v['gate_id']} missing"

# ---------- Step 8: emit JSON sidecar with full pin maps + computed SHAs ------

SIDECAR_PATH = ROOT / "computations" / "_shared" / "_s87_w11_meta_methodology_landing.json"
sidecar = {
    "session": "S87",
    "wave": "W11-meta",
    "wave_class": "METHODOLOGY",
    "gates": [
        {
            "gate_id": "S87-METH-CROSS-PILLAR-BRIDGE-K-COUNTER-UPDATE",
            "wave_id": "W11-meta-1",
            "target_file": str(CPB_PATH.relative_to(ROOT)),
            "plan_block_sha": plan_block_sha["METH-1"],
            "input_pin_map": meth1_input_pin_map,
            "audit_sha256": meth1_audit_sha,
            "content_sha256": meth1_content_sha,
            "rule_file_pre_sha": cpb_pre_sha,
            "rule_file_post_sha": cpb_post_sha,
        },
        {
            "gate_id": "S87-METH-D_K-BLOCK-DIAGONAL-PLAN-AUTHORSHIP-LESSON",
            "wave_id": "W11-meta-2",
            "target_file": str(MS_PATH.relative_to(ROOT)),
            "plan_block_sha": plan_block_sha["METH-2"],
            "input_pin_map": meth2_input_pin_map,
            "audit_sha256": meth2_audit_sha,
            "content_sha256": meth2_content_sha,
            "rule_file_pre_sha": ms_pre_sha,
            "rule_file_post_sha": ms_post_sha,
        },
        {
            "gate_id": "S87-METH-PRU-CLASS-8-2-CORPUS-CLOSURE",
            "wave_id": "W11-meta-3",
            "target_file": str(ED_PATH.relative_to(ROOT)),
            "plan_block_sha": plan_block_sha["METH-3"],
            "input_pin_map": meth3_input_pin_map,
            "audit_sha256": meth3_audit_sha,
            "content_sha256": meth3_content_sha,
            "rule_file_pre_sha": ed_pre_sha,
            "rule_file_post_sha": ed_post_sha,
        },
    ],
    "allowlist_pre_sha": all_pre_sha,
    "allowlist_post_sha": all_post_sha,
    "verdict_file_total_audit_shas": total_count,
    "verdict_file_unique_audit_shas": unique_count,
    "verdict_sha_uniqueness_preserved": (total_count == unique_count),
}
SIDECAR_PATH.write_text(json.dumps(sidecar, indent=2, sort_keys=True), encoding="utf-8")

print()
print("=" * 70)
print("DONE: 3 METHODOLOGY-class gates landed atomically.")
print("=" * 70)
print(f"  JSON sidecar: {SIDECAR_PATH.relative_to(ROOT)}")
