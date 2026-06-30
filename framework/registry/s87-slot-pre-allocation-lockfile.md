# S87 §VII Slot Pre-Allocation Lockfile

**Status**: NEEDS-DECISION (UD-8) → **SPEC INSTALLED** 2026-04-27 (S86 Level-10 housekeeping T10-1).
**Reservation status**: PENDING-SLOT-AVAILABILITY-SCAN. Slot identities below are provisional; orchestrator at S87-W0 plan-freeze MUST run an availability scan against `sessions/permanent-results-registry.md` (using the scan-ALL-header-levels protocol from `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race") before promoting reservations to LOCKED.
**Source**: S86 W-1 workshop `_housekeeping-extract-w1.md` OF-1 (lines 114-119) + REG-1 through REG-5 + S87-SLOT-PRE-ALLOCATION-LOCKFILE-DRAFT block (workshop lines 2197-2201).
**Recommending agent**: gen-physicist (extract); connes + lizzi (workshop sponsors).
**Cross-session purpose**: persists beyond S87. The lockfile is a coordination artifact — its function is to prevent slot collisions across sessions when multiple §VII landings are queued by different workshops.

---

## §1 — Reserved-for-Workshop-86-W-1 slot table

The following six §VII slots are **RESERVED-FOR-WORKSHOP-86-W-1** for the S87 landing program. Each reservation pins the originating workshop, the carry-forward gate ID, the substrate-physical theorem statement, and the SHA-anchor source.

| Slot | Reservation | Theorem class | Originating gate | SHA-anchor |
|:-----|:------------|:--------------|:------------------|:------------|
| **§VII.U** | RESERVED (lizzi anchor) | FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY (ALGEBRAIC × AXIOM); **OR** W1b-T5 LANDING (Mellin-Strip / Convergence-Cone Theorem; INFINITE-VECTOR class) | `S87-FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY-LANDING` (CF-4) **OR** `S87-W1B-T5-LANDING` (CF-1) | C10 verdict line `s86_gate_verdicts.txt:91` `sha256=279da9646d421b60bb39711057be7722226f7bc4e6336bae2baa4aebdbb70698` (CF-4); C11 verdict `s86_gate_verdicts.txt:91`-pinned audit_sha256 (CF-1) |
| **§VII.V** | RESERVED (connes anchor) | CM-1995-INADMISSIBILITY-AT-FINITE-L with WEYL-NON-ASYMP-F_4-MB-NO-GO Corollary A (AXIOM × SPECTRAL); **OR** W1b-T5 LANDING (alternative slot identity per L-CN-4) | `S87-MELLIN-CONE-NO-GO-THEOREM-LANDING` (CF-2) | C9 verdict line `s86_gate_verdicts.txt:95-96` `audit_sha256=1559e559208db268580961556082122cc4d97d73bb01a98c056cdde404155544`, `content_sha256=ed4ee766ad00f31f71f475b476b511806cbbf8d5ed2ddf5567db9b40854482f7` |
| **§VII.W** | RESERVED (joint anchor) | A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE (SPECTRAL × CROSS-PROGRAM); biconditional theorem | `S87-A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE-LANDING` (CF-5) | S77 R-protection-universal claim (`project_s77_synthesis`, `permanent-theorems.md` line 71); C9 audit_sha256 (above) |
| **§VII.X** | RESERVED (joint anchor) | M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL (necessity-only meta-theorem; AXIOM × META) | `S87-M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL-LANDING` (CF-6) | Six full-64-char SHAs from S46 / S64-split / S64-finite-L / S77 / S82-W2-5 / C9 verdict-line records (S87 closure script must harvest) |
| **§VII.PROP** | RESERVED (joint anchor; routing-layer principle (a)) | P_MB / P_CM un-bundling principle | `S87-VII-PROP-LANDING` (CF-7) part (a) | connes C1 axiom decomposition (workshop lines 730-820); lizzi E-γ proposal (workshop lines 1135-1141) |
| **§VII.PROP+1** | RESERVED (joint anchor; routing-layer principle (b)) | Lens-mediated-vs-Prescription-mediated distinction | `S87-VII-PROP-LANDING` (CF-7) part (b) | connes C-EN-1 (workshop R3-final round, lines 1963-2017) |

**Slot-allocation policy**: per Q-OPEN-8 + UD-10, the orchestrator at S87-W0 plan-freeze must adjudicate one of:

- **Option (a) — single §VII.PROP with two sub-headers** (`§VII.PROP.a` + `§VII.PROP.b`): both routing-layer principles share one §-anchor, with sub-headers distinguishing P_MB/P_CM un-bundling vs Lens/Prescription distinction
- **Option (b) — two adjacent §-anchors** (`§VII.PROP` and `§VII.PROP+1`): each principle gets its own slot identity (lizzi preference, see Q-OPEN-8)

Per Q-OPEN-8 + UD-10, lizzi prefers Option (b); the lockfile reserves both slots until the orchestrator commits to one of the options.

---

## §2 — Slot-allocation collision-resolution policy (per UD-9)

If at S87-W0 plan-freeze any of the six reserved slots is found OCCUPIED (by a parallel-landed §VII row from another workshop), the orchestrator applies the precedent of S84 W2a-11 §VII.M→§VII.N rerouting (see `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race" rule (3)):

1. **Reroute to next free letter** following the alphabetical order `§VII.U → §VII.V → §VII.W → §VII.X → §VII.Y → §VII.Z → §VII.AA → ...` skipping any occupied slot.
2. **Emit FAIL-with-remediation in the producing script's verdict line**, NOT PASS, so the rerouting is visible in the verdict-file audit trail.
3. **Update this lockfile** (next session) with the LOCKED reservation column for every successfully landed slot, and the FAIL-with-remediation reroute column for any slot that hit a collision.

**Three-way collision resolution at §VII.W** (UD-18, S86 W-1 vs W-5 vs Slot-1a-S7-CN): the user-decided canonical assignment to §VII.W (one of: W-1 REG-3 A0-R-PROTECTION-FAILURE-IS-M2-AXIOM, W-5 REG-1 Pillar III↔IV Bridge, Slot-1a-S7-CN Parity-Grading per lizzi Corollary E, or merge under common §VII.W parent) governs the §VII.W reservation here. Until UD-18 is decided by the user, the §VII.W reservation here is provisional with W-1 REG-3 as the OF-1 originating workshop's claim — but the orchestrator's S87-W0 adjudication binds.

---

## §3 — Append-only writer protocol

Per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race" rules (1)-(2), every S87 landing script for the six reserved slots MUST:

1. **Use append-only Python writers** (open in `"a"` mode, append the new entry, close) — NOT Edit-tool round-trips. Multiple parallel landings into `permanent-results-registry.md` cause Edit-tool mtime conflicts.
2. **Scan ALL header levels** (`## Header #N` + `### Header #N` + `#### Header #N`) before slot allocation. A scan limited to one hash level under-counts existing slots.
3. **Use the S82 W1 template helper pattern** `computations/script-template.py append_verdict()` as the canonical analog. An equivalent registry-append helper for `permanent-results-registry.md` should follow the same protocol.

**Lockfile-write discipline**: this lockfile itself is updated next session with LOCKED reservations or FAIL-with-remediation reroutes. Append-only Python writer applies to the lockfile too; do NOT use Edit-tool round-trips for next-session lockfile updates.

---

## §4 — Cross-reference template for §VII registry entries

Each §VII registry entry landing into a reserved slot MUST include the following cross-reference fields:

```
## §VII.<letter> <THEOREM-NAME>

**Provenance**: 
  - Workshop: S86 W-<N> `<workshop-file>.md` (lines L1-L2)
  - Originating gate: <S87-CARRY-FORWARD-ID>
  - Lockfile reservation: `sessions/framework/registry/s87-slot-pre-allocation-lockfile.md` §1 row (...)

**Sponsors**: <agent-1> [+ <agent-2> if joint anchor]

**Anchor List** (full-64-char SHA pins):
  - <sha-1> -- <source-1>
  - <sha-2> -- <source-2>
  - ...

**Theorem statement**: <verbatim from this lockfile §1>

**Theorem class**: <one of: ALGEBRAIC × AXIOM, AXIOM × SPECTRAL, SPECTRAL × CROSS-PROGRAM, AXIOM × META, ROUTING-LAYER, INFINITE-VECTOR, FINITE-VECTOR>

**Preconditions**: <if any structural footnote, e.g., μ_CCM continuity prerequisite for §VII.V>

**Cross-references**:
  - Parent registry slots: <list of upstream §VII.* slots cited>
  - Downstream consumer slots: <list of §VII.* slots that cite this one>
  - Framework note anchors: <list of `sessions/framework/*.md` anchor files>

**Future-Work Flags**: <if any OPEN-QUESTION items, e.g., S87-PAIRED-SLOT-RATIO-INTERPRETATION for §VII.X>
```

---

## §5 — Slot-letter availability scan protocol

The S87-W0 orchestrator MUST run the following scan BEFORE promoting any reservation in §1 to LOCKED:

```python
import re

# Open registry in read mode
registry_path = "sessions/permanent-results-registry.md"
with open(registry_path, "r", encoding="utf-8") as f:
    content = f.read()

# Scan ALL header levels for §VII.<letter> patterns
# Match ## §VII.X, ### §VII.X, #### §VII.X — letters A-Z, AA-ZZ, AAA-ZZZ, etc.
pattern = re.compile(r"^#+\s+(?:§VII|VII|Section\s+VII)\.([A-Z]+)\b", re.MULTILINE)
occupied_slots = set(pattern.findall(content))

# Lockfile reservation set (six slots from §1)
lockfile_reserved = {"U", "V", "W", "X", "PROP", "PROP+1"}

# Detect collision
collisions = occupied_slots & lockfile_reserved
if collisions:
    print(f"COLLISION DETECTED: slots {collisions} already occupied; reroute per §2")
else:
    print(f"NO COLLISION: lockfile reservations may be promoted to LOCKED")
```

The scan MUST cover three header levels (`##`, `###`, `####`) per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race" rule (1) — a scan limited to one hash level (the S86 W1c BULLETIN failure mode) under-counts existing slots and produces collision under parallel writers.

---

## §6 — Reservation life-cycle states

Each slot in §1 transits through five states:

1. **RESERVED-PENDING-SCAN** — current state at S86 close (this lockfile install). Slot identity is provisional; orchestrator scan at S87-W0 promotes to LOCKED or REROUTED.
2. **LOCKED** — orchestrator scan at S87-W0 confirmed slot is free; reservation is binding. Any further parallel landing into this slot from another workshop must check the lockfile FIRST.
3. **REROUTED** — orchestrator scan at S87-W0 found collision; reservation is rerouted to next-free-letter per §2 protocol; FAIL-with-remediation verdict line emitted; this lockfile is updated with the rerouted slot identity.
4. **LANDED** — registry entry has been appended to `permanent-results-registry.md` at the LOCKED or REROUTED slot identity; Anchor List SHAs are pinned.
5. **CLOSED** — landing-anchor SHAs are validated at S87 closure; ladder audit confirms no Class-1-7 execution failures; reservation entry in this lockfile may be archived to a closed-slot registry at S88+.

---

## §7 — Cross-references

- **Source workshop**: `sessions/archive/session-86/_housekeeping-extract-w1.md` OF-1 (lines 114-119), REG-1 through REG-5 (lines 7-58), CF-1 through CF-7 (lines 133-173).
- **S87 carry-forward gates** (full 4-field specs in W-1 extract): `S87-W1B-T5-LANDING` (CF-1, 4-6h); `S87-MELLIN-CONE-NO-GO-THEOREM-LANDING` (CF-2, 6-8h); `S87-FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY-LANDING` (CF-4, 2-3h); `S87-A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE-LANDING` (CF-5, 4-6h); `S87-M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL-LANDING` (CF-6, 6-8h); `S87-VII-PROP-LANDING` (CF-7, 3-4h).
- **Append-only writer protocol**: `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race" rules (1)-(3).
- **S82 W1 template helper** (canonical pattern for append-only verdict-write): `computations/script-template.py` `append_verdict()`.
- **S84 W2a-11 §VII.M→§VII.N rerouting precedent**: `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race" rule (3) calibration corpus.
- **Three-way collision resolution at §VII.W** (UD-18): `sessions/archive/session-86/_housekeeping-install-queue.md` lines 484-492 (NEEDS-USER-DECISION items).
- **Single §VII.PROP vs adjacent §VII.PROP/§VII.PROP+1** (UD-10): `sessions/archive/session-86/_housekeeping-install-queue.md` lines 484-492.
- **Framework note anchor for §VII.U FINITE-VECTOR class**: `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md` §1-§2 (per OF-2 cross-reference).
- **Framework note anchor for W1b-T5 INFINITE-VECTOR class**: `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md` §3 (per CF-1 cross-reference).
- **Mellin-cone live infrastructure (W2 C9/C10)**: `sessions/archive/session-86/session-86-w2-workingpaper.md` lines 218-272 (5-point sweep machine-ε agreement).
- **Mellin-cone factorization reading** (L-EN-2 STRUCTURAL FACTORIZATION): `sessions/framework/registry/baseline-findings-s66.md` (T10-3 install) — `F_4 ∘ MB ∘ SD-subtraction = LENS_kernel ∘ PRESCRIPTION_subtraction ∘ LENS_substrate`.

---

## §8 — Open user decisions (BLOCKERS)

Until the user resolves the following, slot promotion remains in **RESERVED-PENDING-SCAN** state:

- **UD-8**: Synchronization-lockfile content drafting — orchestrator-confirmed §VII slot availability scan first (Option a) vs draft with placeholder slots (Option b)?
- **UD-9**: Slot allocation collisions — resolution policy: reroute to next free letter (Option i, S84 §VII.M→§VII.N precedent), merge under common §VII.W parent (Option ii), or defer all to S87 plan-author (Option iii)?
- **UD-10**: §VII.PROP — single slot with sub-headers (Option a) vs two adjacent slots (Option b)?
- **UD-18**: Three-way collision at §VII.W — which workshop's claim is canonical: Slot 1a-S7 (Parity-Grading; lizzi Corollary E), W-1 REG-3 (A0-R-PROTECTION-FAILURE-IS-M2-AXIOM), W-5 REG-1 (Pillar III↔IV Bridge), or merge under common §VII.W parent with sub-blocks?

These four decisions cannot be made by the orchestrator alone; they are filed in `sessions/archive/session-86/_housekeeping-install-queue.md` §"NEEDS-USER-DECISION items" for user adjudication. Once decided, this lockfile is amended in S87-W0 to record the bindings.

---

## §9 — Closing

This lockfile is the coordination artifact for the S87-W0 §VII registry-landing program. Its function is structural: prevent slot collisions across sessions, document the originating-workshop provenance, pin Anchor List SHAs forward, and provide the verbatim cross-reference template for landing scripts. The lockfile itself does NOT land §VII rows; it reserves the slot identities and provides the audit-trail spec for S87 landings to follow. It persists beyond S87 as a permanent registry-allocation record.
