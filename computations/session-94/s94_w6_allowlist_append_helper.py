#!/usr/bin/env python3
"""S94 W6 methodology-wave allowlist append helper (orchestrator-only).

Appends the 5 S94-W6 METHODOLOGY-class gate-IDs to the allowlist ledger
(3-column rows ONLY, per methodology-wave-allowlist.md Edit-discipline item 4)
AND the parallel rationale-prose entries to methodology-wave-instances.md.

Block-SHA method (validated against the W6-18 agent's reported 3c758838...):
  block = '## §W6-N.' header -> line before next '## ' header; (rstrip()+'\n');
  raw UTF-8 bytes; plain hashlib.sha256.  Single open('a') O_APPEND per file
  (parallel-writer-safe).  IDEMPOTENT: re-running skips gate-IDs already present
  (no double-append).
"""
import sys
import pathlib

# computations/_shared/CLAUDE.md convention: all computations/*.py import
# canonical_constants. This is a pure-IO orchestrator append-helper that uses no
# framework constant; the import satisfies the convention (python-validate check 1).
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "_shared"))
from canonical_constants import *  # noqa: F401,F403

LEDGER = pathlib.Path("sessions/framework/registry/methodology-wave-allowlist-ledger.md")
INSTANCES = pathlib.Path("sessions/framework/registry/methodology-wave-instances.md")
PLAN = "sessions/session-plan/session-94-plan-w6.md"

# (gate_id, plan_block_sha64, block_range, rationale_prose)
ROWS = [
 ("S94-CPB-AUDIT-PENDING-VS-DEFECTIVE",
  "b8b69bfd076519717111b54ed769315eca30067d69c8f7f7300e1c37d50312d4", "44-247",
  "S94-CPB-AUDIT-PENDING-VS-DEFECTIVE — METHODOLOGY-class audit-script extension ([AUDIT] trigger, NON-PHONONIC). FAIL (`audit_sha256=9ef86f4f40dd5df66e045d228a031c908ef87ac7d2a4f3ff766e621755ce34fd`; verdict line 94; sig_5 CLEAN) — the pre-registered FAIL_meaning on the LIVE (un-retrofitted) registry: 4 genuinely-defective §VII entries (§VII.AJ.partition-stability, §VII.W-2, §VII.AO, §VII.AP) NAMED and routed to mack-cosmic-bridge (sole registry writer); the audit correctly FAILs until that retrofit lands. The classifier extension itself is verified complete by the 23/23-PASS self-test (proves the audit emits `PASS-WITH-N-PENDING` with `genuinely_defective == 0` after a synthetic retrofit fixture). Extends `computations/_shared/_cross_pillar_bridge_audit.py` `run_audit()` to a status trichotomy {legitimately-pending, genuinely-defective, PASS} + a parent/sub-section anatomy-inheritance resolver over 35 §VII sections (19 PASS / 9 legitimately-pending / 4 genuinely-defective / 2 self-non-bridge / 1 superseded; partition SUM=35). M1 PASS: artifact-existence (audit-script + self-test + json) + integer count. M2 PASS: audit-script extension whose output is structural classification, NOT a numerical threshold. M3 PASS: verbatim from `cross-pillar-bridge-anatomy.md` deferred-pending/OE-form/Tier taxonomy. M4 PASS: this allowlist append (orchestrator-only per recursion-attack closure). Author: gen-physicist (compute) + orchestrator (allowlist append)."),
 ("S94-MULT-NORM-CANCELLATION-K3",
  "3c758838f4243c4dba5eeb1d28ba7047e393701219f7ef16167cf5f8ee763e8c", "248-447",
  "S94-MULT-NORM-CANCELLATION-K3 — METHODOLOGY-class K-counter advancement ([VERIFY-THEOREM] trigger, GEOMETRIC). PASS (`audit_sha256=6284d0d3ac7a85c8174f26c8d1ae8561f4ff89945ae6d86cffb4a8b8ff8fb27e`; verdict line 82; sig_5 CLEAN). Advances the `math-scripts.md §\"Multiplicative-normalization cancellation invariants\"` K-counter **K=2→K=3** and promotes the rule SUGGESTION → MANDATORY: the S93 W3-2 bottom-K Casimir-ceiling weight at fixed regulator mass m_PV is the THIRD structurally-distinct spectral-support form (DISSENT-sharpened Hybrid-Independence-Test on axis (iii) spectral-support-form: discrete Casimir-ceiling sector-count cutoff vs K=1 L_max-truncation envelope vs K=2 τ-moduli-deformation weight; control parameter differs in KIND). Re-read of the S93 W3-2 npz fingerprint (no new diagonalization): `result(C_2^max)` C_2^max-INVARIANT to the FD floor (spread 9.015e-09 ≪ |result|≈528) while the multiplicative spectral-support weight ratio sweeps 0.21→0.83 (Casimir ceiling admits 3→19 Peter-Weyl sectors). M1 PASS: categorical-distinctness + integer K-increment. M2 PASS: npz re-read (no new diagonalization, no fixture). M3 PASS: verbatim K=3-candidate row + DISSENT criterion already in math-scripts.md. M4 PASS: this allowlist append. Author: gen-physicist (compute) + orchestrator (allowlist append + math-scripts.md K=2→K=3 promotion landing)."),
 ("S94-S16-AREA-FUNCTIONAL-K-ADVANCE",
  "bba2f6f9c40945d3683062c8d4917419cdc6231a93b29e15e3a9c3ed44098580", "448-658",
  "S94-S16-AREA-FUNCTIONAL-K-ADVANCE — METHODOLOGY-class K-counter assessment ([VERIFY] trigger, GEOMETRIC). PASS (`audit_sha256=2540c6e8540a5006bb4aa27e1cdf974f59aa11042d49640fae0beb56fceb6b55`; verdict line 98; sig_5 CLEAN). Routes the S93 W8-2 (0,0)-singlet adjudication to **ENRICH-§24.2-no-advance**: it is a corpus §24 same-functional fair-comparison instance (Φ_area:(p,q)→√C_2 conflated with Φ_floor:(p,q)→min|λ|, which AGREE at (0,0): √C_2(0,0)=0=√(j(j+1))|_{j=0}, Sage-exact), NOT a §16 (algebra,projector,pole) slot-split (no discontinuous deformation scan, no regulator-class split). Hybrid Independence Test vs both prior §24 instances: the fair-comparison FAILURE-MODE axis is observable-identity — the SAME axis as W7-3 (K=2), NOT a third axis ⇒ §24 STAYS SUGGESTION at K=2 (companion enrichment, no advance); §16 STAYS K=1 (a functional-conflation is correctly not credited as a slot-split). M1 PASS: structural-routing + HIT-categorical. M2 PASS: classification output is a categorical route + HIT booleans + a Sage-exact rep-theory identity (no fixture, no eigenvalue/linalg). M3 PASS: verbatim connes synthesis §II.1/§IV + §16 discriminator + §24 directive + HIT predicate. M4 PASS: this allowlist append. Author: gen-physicist (compute) + orchestrator (allowlist append + corpus §24.2 companion landing)."),
 ("S94-NON-PROMOTION-META-TAXONOMY",
  "18496daad945abfe6945efec16450e16634d6b79a40b07c5f0c253ac0d2e14bc", "659-886",
  "S94-NON-PROMOTION-META-TAXONOMY — METHODOLOGY-class rule synthesis ([AUDIT] trigger, NON-PHONONIC; INFO-by-design). INFO, outcome=`UNIFYING-META-RULE-DRAFTED` (`audit_sha256=4ddb6c438a1a449efcbb7f347c5fb36b03482150713cf1e27439e4e5513210a2`; verdict line 100, which supersedes the first-run line-96 `4455a487...` per `gate-verdicts.md` Option A; sig_5 CLEAN among non-superseded). Unifies the Tier-2-dimensionful (corpus §25 / anatomy Tier-1/Tier-2) and §(iv-bis) surrogate sub-row (`pru-class-corpus.md §11.1`) non-promotion verdicts under a **genus + differentiae** meta-taxonomy: genus NON-PROMOTION-BY-HELD-NUMBER (P1 theorem-STRUCTURE permanent/proven ∧ P2 a NUMBER held against substrate-natural extraction ∧ P3 NOT sideways-re-pinned to a methodology-floor F-image) + a 3-way differentia (dimensionful-slot-collision / undischarged-magnitude-bound / sign-lock). Held structurally ORTHOGONAL to the deferred-pending intermediate verdict-class. Self-corrected a prose-substring-scan predicate bug (first run mis-routed ORTHOGONAL; corrective UNIFYING via typed boolean fields). M1 PASS: artifact-existence-with-substantive-content reaching a definite outcome. M2 PASS: categorical synthesis output (no eigenvalue/linalg/fixture). M3 PASS: verbatim corpus §25 + §11.1 + the two parent rules. M4 PASS: this allowlist append. Author: gen-physicist (compute) + orchestrator (allowlist append + anatomy Non-Promotion-by-Held-Number sub-section landing)."),
 ("S94-A_N-RETROFIT-C-CAUSALITY",
  "0f91d095f073274b7163f34e4064649f64f643de1c31f27e3d115213019e70e7", "887-1086",
  "S94-A_N-RETROFIT-C-CAUSALITY — METHODOLOGY-class doc retrofit + audit-script scope extension ([AUDIT] trigger, GEOMETRIC). PASS (`audit_sha256=aa04474568d92bea09ac77c5befbb80bef7213211d80c97e1aa09a2074825557`; verdict line 102; a corrective PASS line 108 `9af1d930...` supersedes a spurious idempotency-rerun FAIL `a0809dd3...` per Option A; net non-superseded A_N-RETROFIT verdicts = [PASS, PASS]; sig_5 CLEAN among non-superseded). Per-citation semantic review of all 193 bare `a_n` in `sessions/framework/Phononic-C-Causality.md` (115 a_2 + 58 a_0 + 20 a_4; NSDW set EMPTY — zero lattice-spacings/plain-vars/string-literals/generic-indices) → tagged `a_n^{zeta}` (doc-self-declared regulator, line 138); the 11 pre-existing `^{zeta}` tags preserved; 0 bare a_n remaining. Extended `computations/_shared/_a_n_regulator_pin_audit.py` with a `--target` flag + `MD_TARGETS` (and fixed a latent PROJECT_ROOT-doubling bug + cleared a pre-existing docstring SyntaxWarning per the build-clean discipline) → `n_untagged_seeley_dewitt = 0`. M1 PASS: artifact-existence + integer count (0 untagged). M2 PASS: targeted per-citation tag insertion on a curated framework doc by its author (NOT a bulk append) + audit-script integer-count output. M3 PASS: verbatim `regulator-pin-discipline.md §\"Tag Format\"` + the doc's established `^{zeta}` convention. M4 PASS: this allowlist append. Author: transit-dynamics-theorist (compute) + orchestrator (allowlist append)."),
]

LANDING = "2026-05-25"


def main() -> int:
    ledger_text = LEDGER.read_text(encoding="utf-8")
    instances_text = INSTANCES.read_text(encoding="utf-8")

    new_rows, new_entries, skipped = [], [], []
    for (g, sha, rng, prose) in ROWS:
        ledger_row = f"| {g} | S94 | {sha} |"
        if ledger_row in ledger_text:
            skipped.append(g)
            continue
        new_rows.append(ledger_row + "\n")
        gate_prefix = g.split("-")[0]  # informational; block range pins the exact span
        new_entries.append(
            f"\n### {g} (S94) — {sha[:16]}\n\n"
            f"**Full plan-block SHA**: `{sha}`\n"
            f"**Plan-file block range**: lines {rng} of `{PLAN}` "
            f"(from the `## §{g}` gate header through the line preceding the next `## ` header; "
            f"`rstrip()+'\\n'`; raw UTF-8 bytes, plain `hashlib.sha256`)\n"
            f"**Landing date**: {LANDING}\n\n"
            f"{prose}\n"
        )

    if new_rows:
        with open(LEDGER, "a", encoding="utf-8", newline="\n") as f:
            f.write("".join(new_rows))
    if new_entries:
        with open(INSTANCES, "a", encoding="utf-8", newline="\n") as f:
            f.write("".join(new_entries))

    print(f"appended {len(new_rows)} ledger rows + {len(new_entries)} instances entries; "
          f"skipped {len(skipped)} already-present: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
