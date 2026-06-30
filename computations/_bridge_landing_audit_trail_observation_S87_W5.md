# Bridge-Landing Audit-Trail Observation — S87 W5

> **Provenance**: S88 W3c-30 (`S88-BRIDGE-LANDING-SCRIPT-ARCHITECTURE-REFINEMENT`).
> METHODOLOGY-class deliverable per `.claude/rules/wave-classification.md` M1∧M2∧M3∧M4.
> Source: empirical inspection of `computations/session-87/s87_gate_verdicts.txt`
> lines 149–178 (S87 wave W5 verdict block; gates §W5-1..§W5-5).

## 1. Observation summary

The S87 W5 wave dispatched 5 bridge-landing gates owned by
`volovik-superfluid-universe-theorist`. Empirically, **4 of 5** of these
gates emitted a corrective FAIL/INFO → PASS double-trio in the verdict
file, producing two distinct dual-SHA verdict-line records per gate
instead of the canonical single-shot dual-SHA record.

The S86 W1c-5 all-3-lines-retained discipline (per
`.claude/rules/epistemic-discipline.md` §"Verifier-Rubric Pre-Registration"
Class 8.2) correctly preserves the audit provenance of both the FAIL/INFO
emission and the corrective PASS — both verdict trios remain in the file
and are NOT deleted post-remediation. The structural defect addressed by
W3c-30 is upstream of W1c-5: the script architecture
(`write → re-read → verify → conditionally re-write/append`) emits the
intermediate FAIL/INFO line BEFORE the corrective rewrite, producing the
dual-trio. The `_bridge_landing_script_template.py` single-shot pattern
(`write_promotion → fsync → re-read → verify → emit`) eliminates the
intermediate emission by construction.

## 2. Empirical 4-of-5 dual-trio enumeration

| W-N | Gate ID | Initial verdict (line) | Corrective verdict (line) | Initial audit_sha256 | Corrective audit_sha256 |
|:----|:--------|:----------------------|:--------------------------|:---------------------|:------------------------|
| W5-1 | `S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND` | FAIL (149) | PASS (152) | `adbc3d68fbab8b9fe9e9a74f4098581a5484a84aaa1421cd7071b94273f5edcf` | `5775770d2e01617ee5efeec96413508bb3a66f97616466b36bf1fd1c9b24b0eb` |
| W5-2 | `S87-W11-C5-LAB-FALSIFIER` | INFO (170) | PASS (176) | `08846ab3989ea5042d254e668f2b538b125a5035a5cb52ca7abf6d96bc8f96bd` | `d40a8d26588a0d207ddb6adaad1f26149512e940c659ade32766054d33031a8b` |
| W5-4 | `S87-VII-P-V2-HP1-CONTENT-DISTINCT-RECAST` | FAIL (161) | PASS (164) | `c65129ef7ae77bb3920f0f4f16ea0937bb1922df1ee4c24635f23915e3e42de1` | `42befa89b93c91d470c759dcc0e128b9fff849a1ed58ef7773fa170e5f0022a2` |
| W5-5 | `S87-CROSS-PILLAR-FORWARD-CANDIDATES` | FAIL (158) | PASS (173) | `5e5bba154d480970f8f9c1313504d3d47ea48f68c5ee06eeb122ffb98e5813d4` | `6cd3bfd86d0bac2dd86ba78e64c30988cd954abd5935f0788cc7d34205adf274` |

The W5-4 corrective PASS record at line 164 carries the explicit
post-remediation cross-pin annotation
`post_remediation_of_pre_FAIL_audit_sha256_short=c65129ef7ae77bb3` in the
canonical line — a useful audit-pointer pattern but not a substitute for
the structural fix (single-shot emission would have made the cross-pin
unnecessary).

## 3. The 5th W5 gate — empirical PASS→PASS double (NOT a FAIL→PASS trio)

| W-N | Gate ID | First verdict (line) | Second verdict (line) | First audit_sha256 | Second audit_sha256 |
|:----|:--------|:---------------------|:----------------------|:-------------------|:--------------------|
| W5-3 | `S87-W11-C6-MUSR-FALSIFIER` | PASS (155) | PASS (167) | `0f1ec34899ffffd3b9c64b568e33166440cff54682c9759eaee178f6006939b8` | `3e8a066e1652c0c86eafa3b983e8ef99935c79c3ff8962c08017f86b6aa7c44b` |

Strictly speaking, W5-3 ALSO emitted a duplicate verdict (the script ran
twice and emitted PASS both times), but it is NOT a corrective FAIL → PASS
double-trio — the underlying value differs slightly between the two
emissions (`chi_A=2.266180` vs `chi_A=1.500000`) which suggests the second
emission was a script-rerun rather than a re-verify-then-rewrite. This
falls outside the W3c-30 scope (which targets the corrective-rewrite
defect specifically); the W5-3 case is captured here for completeness.

## 4. Plan-text correction (honest disclosure)

`sessions/session-plan/session-88-plan-w3c.md` §W3c-30 lines 187–189
identified the dual-trio subset as `W5-1 + W5-3 + W5-4 + W5-5`. The
empirical subset (table §2 above) is `W5-1 + W5-2 + W5-4 + W5-5` — the
plan's `W5-3` reference should empirically be `W5-2` (W11-C5-LAB-FALSIFIER,
INFO→PASS) instead. The structural claim "4 of 5 W5 dispatch gates emitted
FAIL/INFO → PASS double-trios" is empirically true; the literal subset
list was off-by-one. This document records the correction without
revising the plan (plan freeze is preserved per
`.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 3 — no
post-hoc plan editing).

## 5. Cross-references

- **AFTER-pattern template**: `computations/_bridge_landing_script_template.py`
  (single-shot `write_promotion → fsync → re-read → verify → emit`).
- **Registry-landing rule extension**: `.claude/rules/registry-landing.md`
  §"Bridge-Landing Script Architecture (single-shot pattern)" — the
  rule-file edit landed by §W3c-30 deliverable (a).
- **All-3-lines-retained rule (S86 W1c-5)**:
  `.claude/rules/epistemic-discipline.md` §"Verifier-Rubric
  Pre-Registration" Class 8.2 — the upstream rubric that keeps both
  verdict trios in the file post-remediation; W3c-30 is the script-side
  fix that prevents the trio from existing in the first place.
- **PROHIBITED_ACTIONS Class 6 ("iterate-until-PASS")**:
  `.claude/rules/v3-closure-recovery.md` — the BEFORE pattern's
  conditional rewrite is Class-6-adjacent; the AFTER pattern eliminates
  the adjacency by construction.
- **Methodology-wave-allowlist row**: `.claude/rules/methodology-wave-allowlist.md`
  §"Allowlist Rows" — appended row for `S88-BRIDGE-LANDING-SCRIPT-ARCHITECTURE-REFINEMENT`
  per `.claude/rules/wave-classification.md` M4 substrate.

## 6. Source authority

This observation is empirical inspection only. No new derivation; the
M3 substrate per `.claude/rules/wave-classification.md` §M3 is verbatim
sub-diff from the S87 W5 dispatch trace in `s87_gate_verdicts.txt`
(lines 149–178). The 8 dual-SHAs in §2 + the 2 dual-SHAs in §3 are
copied verbatim from that file.
