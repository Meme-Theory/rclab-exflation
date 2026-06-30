#!/usr/bin/env python3
"""S90 W1-10 allowlist + instances row append helper (single-shot).

Per `.claude/rules/methodology-wave-allowlist.md §"Edit discipline"` items 1-4:
- Append-only 3-column row to the allowlist
- Parallel rationale entry to `sessions/framework/registry/methodology-wave-instances.md`
- Atomic Python `open("a")` POSIX O_APPEND pattern (no Edit-tool round-trip)
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
from canonical_constants import *  # noqa: F401,F403 — canonical-constants discipline per CLAUDE.md
ALLOWLIST = ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
INSTANCES = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"

GATE_ROW = "W1-10"
SESSION = "S90"
PLAN_BLOCK_SHA = "d19afcffc483a1ace6231fb9f47c210be02783002eb53f28970504c8c6422ab4"
AUDIT_SHA = "977cc8b0c3a8db645b998ed6ac413a43ce21417a10fac2771b885d1da1758757"
CONTENT_SHA = "5f1ffde28801e6d4bf5b8f42b01b1c0326ab5889005f9c7aad38ebb260638b59"

ALLOWLIST_ROW = f"| {GATE_ROW} | {SESSION} | {PLAN_BLOCK_SHA} |\n"

INSTANCES_RATIONALE = f"""
### {GATE_ROW} ({SESSION}) — {PLAN_BLOCK_SHA}

**Provenance**: gate-ID `S90-W5-7-ANCHOR-5-UNIT-CONSISTENCY-AUDIT` (CONNES V.5);
agent `gen-physicist orchestrator-direct-write` per `wave-classification.md
§"Dispatch consequences"`; plan reference `sessions/session-plan/session-90-plan-w1.md`
§W1-10 lines 641-708; plan-block sha256 `{PLAN_BLOCK_SHA}` (6195 chars).

**Gate classification (M1∧M2∧M3∧M4 conjunction)**:
- **M1** (PASS-predicate type): artifact-existence-with-substantive-content per
  `wave-classification.md §M1`. PASS predicate per plan §W1-10 #9 is: audit-script lands
  + side-by-side 3-reading comparison produced + canonical reading identified (A/B/C) +
  WP §W5-7 §(f) amendment lands + allowlist/instances rows appended. INFO branch (the
  one fired): Reading C identified, requires `lambda_unit_canonical` pin promotion
  carried forward. None of these is a numerical comparison against a pre-registered
  threshold; all are existence-with-content predicates.
- **M2** (producing-operation type): Edit/Write on `.claude/rules/*` (allowlist row),
  `sessions/framework/registry/methodology-wave-instances.md` (rationale), AND a
  `.py` audit script that performs STATIC-STRING / DIMENSIONAL analysis (NOT a
  numerical comparison against a pre-registered threshold). The audit script reads
  the S84 spectrum cache to determine λ range empirically — this is dimensional
  analysis, not a fixture-with-hand-engineered-numerical-target (the W0a-2 trap).
- **M3** (source-of-truth type): verbatim sub-diff from prior CONNES V.5 dispatch
  (session-89-connes-synthesis.md §V.5; carried-forward as plan §W1-10). The
  3-reading taxonomy A (GeV⁻²) / B (dimensionless / M_KK²-normalized) / C
  (requires `lambda_unit_canonical` pin) is verbatim from plan §W1-10 #5
  hypothesis + #6 methodology + #10 substitution chain. No first-principles
  new derivation; all content is verbatim-extractable from prior workshop
  or rule-file.
- **M4** (allowlist membership): this row landing satisfies M4 by construction —
  the orchestrator-edit-only allowlist append is the recursion-attack-closure
  mechanism per `methodology-wave-allowlist.md §"Edit discipline"`. Subagent
  edit-denial breaks self-promotion path; allowlist additions originate only
  from orchestrator at plan-freeze (here: in-session execution under /rclab-solo
  with --tasking per user dispatch).

**Sub-clause structure landed**: The audit script implements 4 analytical steps:
(i) regex-detect anchor-5 site (1 hit at W5-7 script line 336 `"1/M_KK_sq": 1.0 / M_KK_sq`);
(ii) empirical spectrum-cache λ range from S84 L=12 cache → [0.82, 5.42] dimensionless
(M_KK-natural units; n_eigenvalues=166896);
(iii) side-by-side 3-reading comparison: Reading A REJECTED (λ not in GeV; GeV-scaled
λ would be ~7e16 not ~3), Reading B REJECTED (script's literal `1.0 / M_KK_sq` does
NOT apply the M_KK² normalization Reading B requires; literal value is 1.81e-34 not
1), Reading C ACCEPTED (the structural resolution requires `lambda_unit_canonical`
pin promotion to disambiguate λ-unit convention);
(iv) verdict INFO per plan §W1-10 #9 INFO clause "if Reading C identified".

**Closure conditions**: INFO verdict per pre-registered #9 threshold; substrate
physics intact (Reading-A WIN at substrate-distance-2 pole s=4 is preserved at the
W5-7 producing-script structural level — anchor 5's UV-degenerate behavior was already
pre-documented at W5-7 WP §(f) cross-check (f) "1/M_KK² gives x ≈ 5e-33 ≈ 0 → all
profiles converge to ~1"; this audit formalizes the dimensional reason).
audit_sha256=`{AUDIT_SHA}` over 12-pin input-pin map (5 file SHAs + 7 computed values:
M_KK GeV, λ_max, anchor_5 literal, x at λ_max, canonical reading, regex sites count,
detection regex string). content_sha256=`{CONTENT_SHA}` over the audit-script body.
sig_5 SHA-uniqueness verified at emission: all 15 canonical lines in
`s90_gate_verdicts.txt` (W1-1..W1-9 + Option-A chains + W1-10) carry distinct
audit_sha256 pins.

**Cross-link**: `sessions/session-plan/session-90-plan-w1.md` §W1-10 (plan reference,
6195-char block, sha256=`{PLAN_BLOCK_SHA}`); `computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py`
(W5-7 producing script, anchor-5 site at line 336); `computations/session-84/s84_spectrum_cache_L12_tau019.npz`
(empirical λ range source); `computations/_shared/canonical_constants.py` (M_KK =
7.428660036284456e+16 GeV provenance); `.claude/rules/regulator-pin-discipline.md`
(`a_n^{{regulator}}` tagging convention; this audit operates at the analogous
unit-pin axis); `sessions/archive/session-89/session-89-w5-workingpaper.md §W5-7 §(f)`
(target of separate WP amendment); `.claude/rules/wave-classification.md §"Dual-SHA
closure for METHODOLOGY-class"` (audit_sha256 over input-pin map + content_sha256
over audit-script body); `feedback_rules-compensate-missing-structure.md` (K-counter
threshold framework for any future lambda_unit_canonical-related rule promotion);
`computations/_shared/s90_w1_emit_verdict.py` (atomic dual-SHA verdict-line emitter
reused from §W1-3 onwards).

**Carry-forward (substantive)**: a `lambda_unit_canonical` canonical pin needs to
be promoted to `canonical_constants.py` in S91+. The pin declares the spectrum-
cache λ unit convention explicitly (DIMENSIONLESS / M_KK-natural, per empirical
[0.82, 5.42] λ range observed). Once promoted, future scripts citing anchor 5 =
1/M_KK² can apply the appropriate unit conversion (multiply by M_KK² if λ
dimensionless, leave as-is if λ in GeV). Forward gate ID candidate:
`S91-LAMBDA-UNIT-CANONICAL-PIN-PROMOTION` (or analogous; 0.1 we; produces a
canonical_constants.py entry + provenance documentation). This carry-forward
does NOT alter the §W5-7 substrate-physics verdict (Reading-A WIN at N=4/5
remains structurally intact; anchor 5's UV-degeneracy is a substrate-physics
feature of the heat-kernel scale hierarchy, not a dimensional inconsistency
that invalidates the rank-ordering on the other 4 anchors).

**Substrate framing**: M_KK IS the substrate's intrinsic mass scale (inverse of
the substrate-distance pole at the Kaluza-Klein threshold); anchor 5 = 1/M_KK²
IS a substrate-IS natural unit. Unit-consistency at the methodology layer is
the F-image of substrate dimensional coherence per `epistemic-discipline.md
§"Layer-Decomposition"` `F: substrate → methodology → audit`. The unit IS NOT
chosen externally — it IS substrate-natural by construction. Container-thinking
violation FORBIDDEN: "the cache stores λ in some chosen container of units" —
inverted: "λ IS the substrate's own dimensionless spectral content; M_KK IS
the substrate's natural mass scale that bridges to laboratory-IN GeV units;
the audit's `lambda_unit_canonical` pin is the methodology F-image of this
substrate-IS bridge".
"""


def main() -> None:
    # Append allowlist row (atomic O_APPEND)
    with open(ALLOWLIST, "a", encoding="utf-8") as f:
        f.write(ALLOWLIST_ROW)
    print(f"Allowlist row appended: {ALLOWLIST_ROW.strip()}")

    # Append instances rationale (atomic O_APPEND)
    with open(INSTANCES, "a", encoding="utf-8") as f:
        f.write(INSTANCES_RATIONALE)
    rationale_lines = INSTANCES_RATIONALE.count("\n")
    rationale_chars = len(INSTANCES_RATIONALE)
    print(f"Instances rationale appended: {rationale_lines} lines, {rationale_chars} chars")


if __name__ == "__main__":
    main()
