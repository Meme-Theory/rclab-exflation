# External-Clock Scaffold (S86-S96)

**Created**: S86 W0c-8 (gate ID: `S86-EXTERNAL-CLOCK-SCAFFOLD`)
**Owner**: mack-cosmic-bridge (delegated to rclab-solo for S86 W0c-8 land)
**Pattern**: freeze-no-re-pin (S86 freezes the scaffold; subsequent
sessions extend or ingest, never re-pin)
**Status**: DOCUMENTATION ONLY for S86 (no compute; ingest-gates fire
at S88 + S96 on data publication)

## §1. 11-Session Scaffold Table

| Session | Date Anchor       | Action                                    | Trigger Type   | Gate ID (pre-reg)   |
|:--------|:------------------|:------------------------------------------|:---------------|:--------------------|
| S86     | 2026-04 (frozen)  | Scaffold creation; freeze 2026-2030 plan  | METHODOLOGY    | S86-W0c-8           |
| S87     | 2026-Q3           | Scaffold extend (add S97-S100 horizon)    | METHODOLOGY    | S87-EXT-EXTERNAL    |
| S88     | 2026-Q4 (target)  | BK-Array data ingest                      | OBSERVATIONAL  | S88-BK-ARRAY-INGEST |
| S89     | 2027-Q1           | Post-BK-Array consolidation               | METHODOLOGY    | S89-CONSOL          |
| S90     | 2027-Q2           | Maintain                                  | MAINTAIN       | S90-MAINT           |
| S91     | 2027-Q3           | Maintain                                  | MAINTAIN       | S91-MAINT           |
| S92     | 2027-Q4           | Maintain                                  | MAINTAIN       | S92-MAINT           |
| S93     | 2028-Q1           | Maintain                                  | MAINTAIN       | S93-MAINT           |
| S94     | 2028-Q3           | Maintain                                  | MAINTAIN       | S94-MAINT           |
| S95     | 2029-Q4           | Pre-LiteBIRD prep                         | METHODOLOGY    | S95-PREP            |
| S96     | 2030-Q1 (target)  | LiteBIRD data ingest                      | OBSERVATIONAL  | S96-LITEBIRD-INGEST |

## §2. Pre-Registered Ingest-Gates (DOCUMENTATION ONLY in S86)

### S88-BK-ARRAY-INGEST

**Trigger**: BK-Array 2026 r-tensor-to-scalar publication (Ade+ or successor).
**Action**: Re-fire S86 W11 C5/C6 lab-falsifier suite + W14 W6 inventory edits
using BK-Array measured r-band as new SI anchor.
**Owner**: mack-cosmic-bridge.
**Branches** (4-branch decision tree per W12 C31):
  - Branch 1: r ∈ [0, 0.005)     → Path-H r=0.00745 (BK-Array null, framework-Path-H consistent)
  - Branch 2: r ∈ [0.005, 0.015) → Path-H r=0.00745 (BK-Array consistent with Path-H)
  - Branch 3: r ∈ [0.015, 0.030) → Path-C r=0.0117 (BK-Array prefers Path-C)
  - Branch 4: r ≥ 0.030          → BOTH-PATHS excluded (re-derivation required)

### S96-LITEBIRD-INGEST

**Trigger**: LiteBIRD 2030 publication (Hazumi+ or successor).
**Action**: Re-fire S86 W11 C5/C6 + W14 W6 with LiteBIRD measured r-band.
**Owner**: mack-cosmic-bridge.
**Branches**: same 4-branch decision tree as S88, applied to LiteBIRD r-band.

## §3. Freeze-No-Re-Pin Discipline

The scaffold is FROZEN at S86. Subsequent sessions MAY:
  - Extend (add S97-S100 horizon at S87)
  - Ingest (S88 / S96 fire ingest gates on data publication)
  - Maintain (S89-S95 sessions touch the scaffold only for housekeeping)

Subsequent sessions MUST NOT:
  - Re-pin S86's frozen 2026-2030 plan (would violate freeze-no-re-pin)
  - Re-define ingest-gate branches without explicit user approval
  - Add new ingest-gates between S86 and the target session (would silently
    re-pin the scaffold)

## §4. Provenance

**Source plan**: `sessions/session-plan/session-86-plan-w0c.md` §W0c-8
**Created in S86 W0c-8** by `s86_w0c_external_clock_scaffold.py`
**Verdict**: PASS → `computations/s86_gate_verdicts.txt`
