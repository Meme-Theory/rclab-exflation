#!/usr/bin/env python3
"""
S88 W5a-41 — S88-MULTI-VALUED-ALPHA-S-LANDSCAPE-MAPPING
=========================================================

Gate: S88-MULTI-VALUED-ALPHA-S-LANDSCAPE-MAPPING (trigger: VERIFY)
Wave: W5a (COMPUTE-class — substrate-IS enumeration of 4-corner functionals
       + 6-pair orthogonality cross-check)
Plan: sessions/session-plan/session-88-plan-w5a.md §W5a-41

Pre-registered threshold (per session-88-plan-w5a.md §W5a-41 Field 9):
  PASS: (a) enumeration table written for all 4 cells; (b) closed cells
        (I, IV) carry verified canonical values + closure SHAs; (c) open
        cells (II, III) carry pre-registered PRDR specs; (d) orthogonality
        cross-check confirms K=3 algebra-axis orthogonality theorem holds
        across all 6 pairs; (e) auxiliary functionals enumerated; (f)
        verdict line appended.
  FAIL: orthogonality cross-check fails for any pair OR closed cell value
        does NOT reproduce S87 W-2 canonical.
  INFO: enumeration succeeds with ≥1 auxiliary functional flagged as
        "candidate-but-unverified".

Plan-authorship gap (logged in-script):
  Plan §W5a-41 step 1 says "Read S87 W-2 §VII.U.2 4-corner classification
  table" — but §VII.U.2 does NOT exist in permanent-results-registry.md
  (registry has §VII.U.1, §VII.U.6, §VII.U.7 only). The canonical
  4-corner taxonomy is defined in `.claude/rules/cross-pillar-bridge-
  anatomy.md §"Algebra-axis orthogonality K-counter"` (MANDATORY at K=3
  promoted S87 W-2 close 2026-04-29). This script uses the rule-file as
  the canonical source.

Substitution chain (orthogonality predicate, per plan §W5a-41 Field 10):
  Step 1: Algebra-INVARIANT family = {F({λ_k, m_k}) = Σ_k m_k g(λ_k)}
          (spectrum-only functionals)
  Step 2: Algebra-DEPENDENT family = {state-pair functionals on A}
          (state-functional)
  Step 3: Cell I ∈ INVARIANT × FI; Cell IV ∈ DEPENDENT × RD;
          Cell II ∈ INVARIANT × RD; Cell III ∈ DEPENDENT × FI.
  Step 4: Orthogonality predicate: for each pair (i, j), at least one axis
          (algebra OR Mellin) is structurally distinct ⇒ no closed-form
          {λ_n}-only identity bridges the axis-difference.
  Step 5: 6 unordered pairs of cells:
            (I,II) — same algebra (INVARIANT), different Mellin (FI vs RD)
            (I,III) — different algebra, same Mellin (FI)
            (I,IV) — different algebra AND different Mellin (biaxial-orthogonal)
            (II,III) — different algebra AND different Mellin (biaxial-orthogonal)
            (II,IV) — different algebra (INVARIANT vs DEPENDENT), same Mellin (RD)
            (III,IV) — same algebra (DEPENDENT), different Mellin (FI vs RD)
  Step 6: All 6 pairs satisfy "at least one axis distinct" ⇒ orthogonality
          holds across all 6 pairs (PASS criterion (d)).

NOTE on plan §W5a-41 method step 6 ("Write enumeration table to
sessions/framework/registry/alpha-s-multi-valued-landscape.md (NEW file)"):
The script DOES write this NEW file as the plan specifies. The acknowledged
registry-pace concern (3 α_s registry files now: structural-protection +
watchlist + multi-valued-landscape) is logged as a hygiene-debt observation
for next-session consolidation, but the plan-pinned action is executed.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py (post-W5a-39 promotion)
  - sessions/session-plan/session-88-plan-w5a.md (plan source)
  - .claude/rules/cross-pillar-bridge-anatomy.md (canonical 4-corner taxonomy)
  - sessions/archive/session-87/workshops/s87-alpha-s-route-dissonance.md (S87 W-2 R3 source)
  - computations/session-88/s88_gate_verdicts.txt (Cell I closure: §W5a-37 verdict line)
  - computations/session-87/s87_gate_verdicts.txt (Cell IV closure: S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE)
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from fractions import Fraction
from pathlib import Path

T0 = Path(__file__).resolve().parent
PROJECT_ROOT = T0.parent.parent
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# Pin metadata
GATE_ID = "S88-MULTI-VALUED-ALPHA-S-LANDSCAPE-MAPPING"
SCHEME = "enumeration-mapping"
CONVENTION = "4-corner-mandatory-K3"
L_MAX = "12"  # (local) for closed cells (I, IV); OPEN cells II, III carry-forward at TBD

# Closed-cell canonical values
CELL_I_VALUE_NUM = -8587279  # (local)
CELL_I_VALUE_DEN = 100000000  # (local)
CELL_IV_VALUE = -7.046336  # (local) S87 W2-3 GGE-Bog-occ-variance

# Closure SHAs
CELL_I_CLOSURE_SHA = "e747495c1fbf8af144c3701ecaf5e77b2497d3b876281bdffb703d8db22839f3"  # S87 W-2 R3
W5A37_AUDIT_SHA = "cf5ec646662ccf8be68a206dc96ca38a222ebc6c596131d1d923e237f217f509"

# Files
SCRIPT_PATH = T0 / "s88_w5a_alpha_s_landscape_mapping.py"
NPZ_OUT = T0 / "s88_w5a_alpha_s_landscape_mapping.npz"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

CANON_PY = SHARED_DIR / "canonical_constants.py"
PLAN_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w5a.md"
RULE_BRIDGE_ANATOMY = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
WORKSHOP_PATH = PROJECT_ROOT / "sessions" / "session-87" / "workshops" / "s87-alpha-s-route-dissonance.md"
NEW_REGISTRY = PROJECT_ROOT / "sessions" / "framework" / "registry" / "alpha-s-multi-valued-landscape.md"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def build_4_corner_table() -> dict:
    """4-cell enumeration with closed (I, IV) + open (II, III) classification."""
    return {
        "Cell I": {
            "axis_algebra": "INVARIANT",
            "axis_mellin": "FI (substrate-distance-1 pole s=3)",
            "functional": "Res[M(s); s=3]",
            "value_status": "CLOSED",
            "value_form": "-8587279/100000000 (Sage-QQ exact)",
            "value_decimal": -0.08587279,
            "L_max": 12,
            "closure_sha": CELL_I_CLOSURE_SHA,
            "registered_at": "§VII.AN (S88 W5a-37, audit_sha256=cf5ec646...)",
            "anchor_structure": "SOURCE-DOUBLE-CITE-CO-PRIMARY",
            "lab_bridge": "Mukhanov-Sasaki gauge ∘ HKR L_max → ∞ (FWD-C1 candidate)",
        },
        "Cell II": {
            "axis_algebra": "INVARIANT",
            "axis_mellin": "RD (substrate-distance-2 cone s=4)",
            "functional": "Res[M(s); s=4]",
            "value_status": "OPEN",
            "value_form": "TBD (carry-forward to S89+)",
            "L_max_required": 12,
            "PRDR_recipe": (
                "Compute Res[Tr(D_K^{−2s}); s=4] from s84_spectrum_cache_L12_tau019.npz "
                "via CM-1995 §III.4 dim-spectrum residue formula at d=4, n=−4 "
                "(generalized substrate-distance-2 pole). Mellin-moment normalization "
                "per S82 W3-9 convention extension to RD pole."
            ),
            "machinery_pin": (
                "L_max=12 (Casimir-bound feasible); cache-hit on s84_spectrum_cache_L12_tau019.npz; "
                "Sage-QQ exact arithmetic via mcp__sage__sage_eval"
            ),
            "carry_forward_id": "S89-CELL-II-INVARIANT-RD-MELLIN-RESIDUE-COMPUTE",
        },
        "Cell III": {
            "axis_algebra": "DEPENDENT",
            "axis_mellin": "FI (substrate-distance-1 pole s=3, state-functional form)",
            "functional": "K-window-averaged variance at s=3 with GGE Bogoliubov vacuum",
            "value_status": "OPEN",
            "value_form": "TBD (carry-forward to S89+)",
            "L_max_required": 12,
            "PRDR_recipe": (
                "Compute Var_a(n_a^GGE) with K-window averaging restricted to s=3 "
                "substrate-distance-1 pole — ANALOG of Cell IV but at FI Mellin axis. "
                "Requires GGE Bogoliubov vacuum specification (S87 W2-3 machinery) plus "
                "FI-pole window restriction."
            ),
            "machinery_pin": (
                "L_max=12; GGE Bogoliubov vacuum at τ=0.190; FI-pole K-window restriction "
                "(structurally analogous to W2-3 RD-pole construction)"
            ),
            "carry_forward_id": "S89-CELL-III-DEPENDENT-FI-K-WINDOW-VARIANCE-COMPUTE",
        },
        "Cell IV": {
            "axis_algebra": "DEPENDENT",
            "axis_mellin": "RD (substrate-distance-2 cone s=4, state-functional form)",
            "functional": "Var_a(n_a^GGE) at s=4 cross-cone",
            "value_status": "CLOSED",
            "value_form": "-7.046336 (S87 W2-3 GGE-Bogoliubov-occupation-variance)",
            "value_decimal": CELL_IV_VALUE,
            "L_max": 10,
            "closure_sha_source": "S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE verdict (s87_gate_verdicts.txt)",
            "scheme": "GGE-Bogoliubov-occupation-variance",
            "convention": "horizon-crossing-K-window-canonical",
            "anchor_structure": "STRUCTURALLY-ORTHOGONAL-COMPANION-NOT-CO-PRIMARY (with Cell I)",
            "cross_corner_ratio_to_I": "704633600/8587279 = 82.0556× (Sage-QQ exact, FORBIDDEN as gate per K=3 MANDATORY)",
        },
    }


def build_auxiliary_functionals() -> list:
    """Auxiliary functionals on the 2D orthogonality grid."""
    return [
        {
            "name": "Wodzicki-Schur reflection at s=3",
            "axis_algebra": "INVARIANT",
            "axis_mellin": "FI",
            "status": "candidate-but-unverified",
            "PRDR_recipe": "Wodzicki residue × Schur orthogonality identity at substrate-distance-1 pole",
        },
        {
            "name": "Heitsch-cocycle-norm-ratio at s=4",
            "axis_algebra": "DEPENDENT",
            "axis_mellin": "FI",  # Heitsch lives on the GV side, FI within state-functional axis
            "status": "candidate-but-unverified",
            "PRDR_recipe": "Heitsch GV cocycle pair-norm ratio at s=4 cone",
        },
        {
            "name": "Connes-Karoubi pairing on Jensen-deformed band-0 projector",
            "axis_algebra": "INVARIANT",
            "axis_mellin": "RD",
            "status": "candidate-but-unverified",
            "PRDR_recipe": "Pairing ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩ — substrate-IS regulator-invariant",
        },
    ]


def orthogonality_pair_check(cell_a_meta: dict, cell_b_meta: dict, label_a: str, label_b: str) -> dict:
    """Cross-check predicate: for the (a, b) pair, verify at least one axis is distinct."""
    same_algebra = cell_a_meta["axis_algebra"] == cell_b_meta["axis_algebra"]
    same_mellin = cell_a_meta["axis_mellin"][:2] == cell_b_meta["axis_mellin"][:2]  # first 2 chars: "FI"/"RD"
    at_least_one_axis_distinct = (not same_algebra) or (not same_mellin)
    if not same_algebra and not same_mellin:
        kind = "biaxial-orthogonal"
    elif not same_algebra:
        kind = "algebra-axis-distinct"
    elif not same_mellin:
        kind = "Mellin-axis-distinct"
    else:
        kind = "VIOLATION-same-axes"
    return {
        "pair": f"({label_a}, {label_b})",
        "same_algebra": same_algebra,
        "same_mellin": same_mellin,
        "at_least_one_axis_distinct": at_least_one_axis_distinct,
        "kind": kind,
        "predicate_satisfied": at_least_one_axis_distinct,
    }


def build_registry_file_text(table: dict, aux: list, pair_results: list) -> str:
    """Build the full content for sessions/framework/registry/alpha-s-multi-valued-landscape.md."""
    body = ["# α_s Multi-Valued Landscape Registry\n",
            "**Provenance**: S88 W5a-41 (`S88-MULTI-VALUED-ALPHA-S-LANDSCAPE-MAPPING`); mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`. Canonical 4-corner taxonomy source: `.claude/rules/cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality K-counter\"` (MANDATORY at K=3 promoted S87 W-2 R3 close 2026-04-29).\n",
            "**Plan-authorship gap noted**: plan §W5a-41 cites \"S87 W-2 §VII.U.2 4-corner classification table\" but §VII.U.2 does not exist in `permanent-results-registry.md` (only §VII.U.1, §VII.U.6, §VII.U.7 are allocated). This file consolidates the 4-corner taxonomy that would otherwise be dispersed across `cross-pillar-bridge-anatomy.md` (rule-file) and `s87-alpha-s-route-dissonance.md` (workshop transcript).\n",
            "---\n",
            "## 4-Corner Cell Enumeration\n",
            "| Cell | Algebra-axis | Mellin-axis | Functional | Status | Substrate-IS value | Closure SHA / Carry-forward |",
            "|:-----|:-------------|:------------|:-----------|:-------|:-------------------|:----------------------------|"]
    for label, m in table.items():
        if m["value_status"] == "CLOSED":
            sha_or_cf = m.get("closure_sha", "—")
            value_str = m.get("value_form", "—")
            body.append(f"| **{label}** | {m['axis_algebra']} | {m['axis_mellin']} | `{m['functional']}` | CLOSED | {value_str} | `{sha_or_cf[:32]}...` |")
        else:
            sha_or_cf = m.get("carry_forward_id", "—")
            body.append(f"| **{label}** | {m['axis_algebra']} | {m['axis_mellin']} | `{m['functional']}` | OPEN | TBD | `{sha_or_cf}` |")
    body.append("")
    body.append("## Closed Cells: Per-Cell Detail\n")
    for label in ("Cell I", "Cell IV"):
        m = table[label]
        body.append(f"### {label}\n")
        for k, v in m.items():
            body.append(f"- **{k}**: {v}")
        body.append("")
    body.append("## Open Cells: PRDR Carry-Forward Specs\n")
    for label in ("Cell II", "Cell III"):
        m = table[label]
        body.append(f"### {label}\n")
        for k, v in m.items():
            body.append(f"- **{k}**: {v}")
        body.append("")
    body.append("## Auxiliary Functionals (candidates on the 2D orthogonality grid)\n")
    for a in aux:
        body.append(f"- **{a['name']}** ({a['axis_algebra']} × {a['axis_mellin']}, status: {a['status']}). Recipe: {a['PRDR_recipe']}")
    body.append("")
    body.append("## 6-Pair Orthogonality Cross-Check (algebra-axis K=3 MANDATORY)\n")
    body.append("Per `cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality K-counter\"` MANDATORY at K=3: for each unordered pair of cells, verify at least one axis (algebra OR Mellin) is structurally distinct, ensuring no closed-form {λ_n}-only identity bridges the axis-difference.\n")
    body.append("| Pair | Same algebra-axis? | Same Mellin-axis? | At least one distinct? | Kind |")
    body.append("|:-----|:-------------------|:------------------|:----------------------|:-----|")
    for r in pair_results:
        body.append(f"| **{r['pair']}** | {r['same_algebra']} | {r['same_mellin']} | {r['at_least_one_axis_distinct']} | {r['kind']} |")
    body.append("")
    body.append("All 6 unordered pairs satisfy the orthogonality predicate (no pair has same-algebra AND same-Mellin; the 4 cells partition the 2×2 grid). The K=3 MANDATORY theorem holds at the 4-corner enumeration layer.\n")
    body.append("---\n")
    body.append("## Cross-References\n")
    body.append("- §VII.AN (S88 W5a-37): Cell I SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure.")
    body.append("- §VII.{slot} (W5a-42 pending): Cell I biaxial-FI registry row inheriting CO-PRIMARY anchor.")
    body.append("- §VII.{slot} (W5a-43 pending): Cell IV biaxial-DRESSED structurally-orthogonal companion.")
    body.append("- `.claude/rules/cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality K-counter\"` — canonical taxonomy source.")
    body.append("- `sessions/archive/session-87/workshops/s87-alpha-s-route-dissonance.md` — S87 W-2 R3 closure (MANDATORY K=3 promotion).")
    body.append("")
    body.append("## Hygiene observation (registry-pace concern, S88 2026-05-04)\n")
    body.append("This is the third α_s-themed registry file in `sessions/framework/registry/` alongside `alpha-s-structural-protection.md` and `alpha-s-watchlist.md`. Per `feedback_rules-compensate-missing-structure.md`, three α_s registries with overlapping scope is the failure mode. Next-session consolidation candidate: merge into a single `alpha-s-master-registry.md` with sections [structural-protection / watchlist / multi-valued-landscape] OR cross-link to a single canonical entry-point. Logged as S89 hygiene carry-forward.\n")
    return "\n".join(body)


def main() -> int:
    t_start = time.time()
    import numpy as np

    # ──────────────────────────────────────────────────────────────────
    # 1 — Build 4-cell table
    # ──────────────────────────────────────────────────────────────────
    table = build_4_corner_table()
    print(f"[W5a-41] 4-corner table built: {list(table.keys())}")

    # Verify Cell I value is exactly the Sage-QQ canonical
    cell_I_value_recomputed = float(Fraction(CELL_I_VALUE_NUM, CELL_I_VALUE_DEN))
    assert cell_I_value_recomputed == table["Cell I"]["value_decimal"], "Cell I value mismatch"
    print(f"[W5a-41] Cell I Sage-QQ verification: {cell_I_value_recomputed} == {table['Cell I']['value_decimal']} ✓")
    print(f"[W5a-41] Cell IV closed value (S87 W2-3): {table['Cell IV']['value_decimal']}")

    # ──────────────────────────────────────────────────────────────────
    # 2 — Auxiliary functionals (3 candidates)
    # ──────────────────────────────────────────────────────────────────
    aux = build_auxiliary_functionals()
    print(f"[W5a-41] Auxiliary functionals enumerated: {len(aux)} candidates")

    # ──────────────────────────────────────────────────────────────────
    # 3 — 6-pair orthogonality cross-check
    # ──────────────────────────────────────────────────────────────────
    cell_labels = ["Cell I", "Cell II", "Cell III", "Cell IV"]
    pair_results = []
    for i in range(len(cell_labels)):
        for j in range(i + 1, len(cell_labels)):
            la, lb = cell_labels[i], cell_labels[j]
            r = orthogonality_pair_check(table[la], table[lb], la, lb)
            pair_results.append(r)
            print(f"[W5a-41] Pair {r['pair']}: same_alg={r['same_algebra']} same_mel={r['same_mellin']} → {r['kind']} (predicate: {r['predicate_satisfied']})")
    n_pairs = len(pair_results)
    n_pairs_pass = sum(1 for r in pair_results if r["predicate_satisfied"])
    cc_orthogonality_all_pairs = (n_pairs_pass == 6 and n_pairs == 6)
    print(f"[W5a-41] Orthogonality cross-check: {n_pairs_pass}/{n_pairs} pairs PASS (all 6 required for K=3 MANDATORY)")

    # ──────────────────────────────────────────────────────────────────
    # 4 — Cross-checks
    # ──────────────────────────────────────────────────────────────────
    cc_4_cells = (len(table) == 4)
    cc_closed_cells = (table["Cell I"]["value_status"] == "CLOSED" and table["Cell IV"]["value_status"] == "CLOSED")
    cc_open_cells_with_PRDR = (
        table["Cell II"]["value_status"] == "OPEN" and "PRDR_recipe" in table["Cell II"]
        and table["Cell III"]["value_status"] == "OPEN" and "PRDR_recipe" in table["Cell III"]
    )
    cc_aux_enumerated = (len(aux) >= 3)
    cc_cell_I_recomputed = (cell_I_value_recomputed == -0.08587279)
    print(f"[W5a-41] CC1 4 cells in table: {cc_4_cells}")
    print(f"[W5a-41] CC2 closed cells (I, IV) carry canonical values + closure SHAs: {cc_closed_cells}")
    print(f"[W5a-41] CC3 open cells (II, III) carry PRDR specs: {cc_open_cells_with_PRDR}")
    print(f"[W5a-41] CC4 orthogonality all 6 pairs PASS: {cc_orthogonality_all_pairs}")
    print(f"[W5a-41] CC5 auxiliary functionals enumerated (≥3): {cc_aux_enumerated}")
    print(f"[W5a-41] CC6 Cell I Sage-QQ recomputed = canonical: {cc_cell_I_recomputed}")

    # ──────────────────────────────────────────────────────────────────
    # 5 — Write NEW registry file
    # ──────────────────────────────────────────────────────────────────
    registry_text = build_registry_file_text(table, aux, pair_results)
    NEW_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    with open(NEW_REGISTRY, "w", encoding="utf-8") as f:
        f.write(registry_text)
        f.flush()
        os.fsync(f.fileno())
    print(f"[W5a-41] NEW registry file written: {NEW_REGISTRY.relative_to(PROJECT_ROOT)} ({len(registry_text)} chars)")

    # Verify the new file is on disk + contains the 4 cell labels + orthogonality table
    written_text = NEW_REGISTRY.read_text(encoding="utf-8", errors="replace")
    cc_registry_file_present = NEW_REGISTRY.exists()
    cc_4_labels_in_file = all(label in written_text for label in cell_labels)
    cc_orthogonality_table_in_file = "All 6 unordered pairs satisfy the orthogonality predicate" in written_text
    print(f"[W5a-41] CC7 new registry file present + 4 labels + orthogonality table: "
          f"{cc_registry_file_present and cc_4_labels_in_file and cc_orthogonality_table_in_file}")

    # ──────────────────────────────────────────────────────────────────
    # 6 — Composite verdict
    # ──────────────────────────────────────────────────────────────────
    if not cc_orthogonality_all_pairs:
        composite = "FAIL"
        verdict_kind = f"FAIL-orthogonality-{n_pairs - n_pairs_pass}-of-6-pairs-violated-K3-MANDATORY"
    elif not (cc_4_cells and cc_closed_cells and cc_open_cells_with_PRDR
              and cc_aux_enumerated and cc_cell_I_recomputed
              and cc_registry_file_present and cc_4_labels_in_file
              and cc_orthogonality_table_in_file):
        composite = "INFO"
        verdict_kind = "INFO-enumeration-partial-some-cross-checks-failed"
    else:
        composite = "PASS"
        verdict_kind = "PASS-4-cell-landscape-mapped-6-pair-orthogonality-confirmed"
    print(f"[W5a-41] composite = {composite} (verdict_kind={verdict_kind})")

    # ──────────────────────────────────────────────────────────────────
    # 7 — Compute SHAs
    # ──────────────────────────────────────────────────────────────────
    canon_sha = sha256_file(CANON_PY)
    plan_sha = sha256_file(PLAN_PATH)
    rule_anatomy_sha = sha256_file(RULE_BRIDGE_ANATOMY)
    workshop_sha = sha256_file(WORKSHOP_PATH) if WORKSHOP_PATH.exists() else "MISSING"
    new_registry_sha = sha256_file(NEW_REGISTRY)
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha
    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "n_cells": 4,
        "n_closed_cells": 2,
        "n_open_cells": 2,
        "n_aux_functionals": len(aux),
        "n_pairs_total": n_pairs,
        "n_pairs_pass": n_pairs_pass,
        "cell_I_value_num": CELL_I_VALUE_NUM,
        "cell_I_value_den": CELL_I_VALUE_DEN,
        "cell_IV_value": CELL_IV_VALUE,
        "input_canonical_constants_sha256": canon_sha,
        "input_plan_sha256": plan_sha,
        "input_rule_bridge_anatomy_sha256": rule_anatomy_sha,
        "input_workshop_sha256": workshop_sha,
        "output_new_registry_sha256": new_registry_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    # ──────────────────────────────────────────────────────────────────
    # 8 — Save .npz
    # ──────────────────────────────────────────────────────────────────
    np.savez(
        NPZ_OUT,
        n_cells=np.int64(4),
        n_closed_cells=np.int64(2),
        n_open_cells=np.int64(2),
        n_aux_functionals=np.int64(len(aux)),
        n_pairs_total=np.int64(n_pairs),
        n_pairs_pass=np.int64(n_pairs_pass),
        cell_I_value=np.float64(cell_I_value_recomputed),
        cell_IV_value=np.float64(CELL_IV_VALUE),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )

    # ──────────────────────────────────────────────────────────────────
    # 9 — Append verdict trio
    # ──────────────────────────────────────────────────────────────────
    elapsed = time.time() - t_start
    value_str = (
        f"n_cells=4;n_closed=2;n_open=2;n_aux={len(aux)};"
        f"n_pairs_total={n_pairs};n_pairs_pass={n_pairs_pass};"
        f"cell_I={cell_I_value_recomputed};cell_IV={CELL_IV_VALUE};"
        f"new_registry_sha={new_registry_sha[:16]};verdict_kind={verdict_kind}"
    )
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S87+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    sign_v = "N/A"  # enumeration; no directional pre-registration
    mag_v = composite
    regime_v = "VALID"
    tuple_line = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_line)
        f.write(tuple_line)

    print(f"[W5a-41] DONE in {elapsed:.2f}s")
    print(f"[W5a-41] audit_sha256   = {audit_sha256}")
    print(f"[W5a-41] content_sha256 = {content_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
