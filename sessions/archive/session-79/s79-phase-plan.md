# Session 79 Phase Plan — S78 Oddities Workshop Series

**Date**: 2026-04-16
**Trigger**: S78 post-hoc analysis surfaced 13 oddities requiring deeper investigation. EVOI update moved to final workshop so it ingests all prior outcomes.
**Total workshops**: 13, organized in 5 phases with a remediation layer between Phase 1 and Phase 2.
**Format per workshop**: 2-agent iterative, 2 rounds, no TeamCreate (per team-lessons 2-agent workshop pattern).

---

## Execution Status

### Phase 1 — Record-state cleanup (LAUNCHED 2026-04-16)

| # | ID | Title | Agents | Status |
|:-:|:---|:------|:-------|:-------|
| 1 | P1-1 | S78 §VI table + §VII synthesis completion | qa × gen-physicist | **CLOSED** (906 lines; 5 Converged, 1 Partial, 1 Emerged; transcription to S78 pending user auth) |
| 2 | P1-2 | Wave 2 holes (W2-B, W2-E, W2-G) | landau × transit | **R1-A IN PROGRESS** (landau running BCS compute) |
| 3 | P1-3 | W1-B 7× iteration audit | nazarewicz × gen-physicist | **CLOSED** (1637 lines; W1-B WARRANT-INVALID, W2-C WARRANT-INVALID) |

**Key Phase 1 outcomes**:
- P1-3 issued WARRANT-INVALID on W1-B and W2-C → remediation layer required before those gates' results are cited downstream.
- P1-3 proposed **PRU as 8th integrity failure class** (Pre-Registration Underspecification).
- P1-3 proposed §0.10 four-way split: (a) numerical-iteration, (b) verdict-log-iteration, (c) script-provenance, (d) plan-self-consistency/PRDR.
- P1-1 consensus: S78-MASTER verdict is **FAIL-composed** (not INCOMPUTABLE) at A_s composed ≈ 1.96e-6, +2.97 OOM from Planck.
- P1-1 identified **fold |β|²~10⁴ as unified root cause of 5 S78 failures**.

### Remediation Layer (P1-3-driven, not a workshop phase)

| R# | Gate | Action | Pre-registrations required before re-run |
|:--:|:-----|:-------|:-----------------------------------------|
| R1 | W1-B | Single clean re-run of s78_norm_indep_verify.py | N_eval=3 (pinned); Hankel-formula-order=2^(2ν-3); ε-scan in pre-reg; SHA-256 content-hash at verdict stamp; import-closure hash; plan §W1-B addendum |
| R2 | W2-C | Single clean re-run of s78_zeta_josephson.py | Frozen quantity-definition (Type I vs Type II distinction); 5-pt stencil h-range pre-reg; per-branch drift threshold; same content-hash pins |

**Remediation is a user decision**: execute before Phase 2, or proceed with explicit caveats. **Plan default**: Phase 2 proceeds with agents instructed to flag W1-B/W2-C-dependent claims as WARRANT-INVALID-UPSTREAM.

### Phase 2 — A_s chain-level tensions (LAUNCHING 2026-04-16)

| # | ID | Title | Agents | Oddity # (from S78 summary) |
|:-:|:---|:------|:-------|:---------------------------:|
| 4 | P2-A | W1-A PASS vs composed-chain dissonance | lizzi × transit | 5 |
| 5 | P2-B | W3-E PBH wrong-sign (same root as W1-E) | mack × transit | 8 |
| 6 | P2-C | W3-G DESI mechanism PASS / prediction 23σ FAIL | einstein × mack | 7 |

**Dependencies**:
- P2-A references W1-A ledger (convention-pinning is warranted; the +3 OOM composition is the question).
- P2-B and P2-C both use Mack — P2-B runs Mack as R1-A opener; P2-C's Mack appears as R1-B responder to Einstein. Parallel-safe for R1-A launches.
- Transit is R1-B in both P2-A and P2-B — sequential by necessity.

### Phase 3 — Structural reinterpretation (QUEUED)

| # | ID | Title | Agents | Oddity # |
|:-:|:---|:------|:-------|:--------:|
| 7 | P3-A | W1-D τ_min at fold (not pre-fold saddle) | landau × volovik | 6 |
| 8 | P3-B | W3-O T_rh: instanton → gravity channel redefinition | einstein × feynman | 9 |

### Phase 4 — Theorem-scope + meta-pattern (QUEUED)

| # | ID | Title | Agents | Oddity # |
|:-:|:---|:------|:-------|:--------:|
| 9 | P4-A | W3-K rank-universality vs strict rank-law | lizzi × spectral-geometer | 10 |
| 10 | P4-B | W2-C u1 per-branch R-protection breakdown (needs post-remediation W2-C) | lizzi × van-den-dungen | 11 |
| 11 | P4-C | W2-D f* categorically outside {SDW, zeta, anomaly} | lizzi × spectral-geometer | 12 |
| 12 | P4-D | Scheme-invariant RATIOS vs ABSOLUTE VALUES meta-pattern | lizzi × connes | 13 |

**Phase 4 serialization**: Lizzi is A in all 4; run sequentially. P4-D depends on P4-A/P4-B/P4-C conclusions.

### Phase 5 — EVOI recalibration (FINAL; QUEUED)

| # | ID | Title | Agents | Oddity # |
|:-:|:---|:------|:-------|:--------:|
| 13 | P5-A | EVOI table update ingesting all 12 prior workshop outcomes | nazarewicz × gen-physicist | 1 |

**Rationale for EVOI-last**: P(pass) and ΔP estimates depend on what the 12 prior workshops closed, re-opened, or strengthened. Running EVOI first would produce a table obsolete before Phase 2 even starts.

---

## Oddity → Workshop Map (reverse index)

| Oddity # (S78 summary) | Topic | Workshop | Phase |
|:---------------------:|:------|:---------|:-----:|
| 1 | EVOI stale / contradicts WP | P5-A | 5 |
| 2 | §VII synthesis + §VI table empty | P1-1 | 1 (CLOSED) |
| 3 | Wave 2 holes W2-B/E/G | P1-2 | 1 (in progress) |
| 4 | W1-B 7× iteration pattern | P1-3 | 1 (CLOSED) |
| 5 | W1-A PASS vs composed chain | P2-A | 2 (launching) |
| 6 | W1-D τ_min at fold | P3-A | 3 |
| 7 | W3-G DESI PASS/FAIL split | P2-C | 2 (launching) |
| 8 | W3-E PBH dual-FAIL wrong-sign | P2-B | 2 (launching) |
| 9 | W3-O T_rh 7 OOM FAIL | P3-B | 3 |
| 10 | W3-K rank-universality PASSES / strict FAILS | P4-A | 4 |
| 11 | W2-C u1 R-protection breakdown | P4-B | 4 |
| 12 | W2-D f* categorically outside cluster | P4-C | 4 |
| 13 | Ratios survive, absolutes fail | P4-D | 4 |

---

## File Paths (canonical)

- Phase plan: `sessions/archive/session-79/s79-phase-plan.md` (this file)
- Workshop docs: `sessions/archive/session-79/workshops/<p#-x>-<slug>.md`
- Remediation scripts (if executed): `computations/s79_remediation_w1b.py`, `s79_remediation_w2c.py`
- Remediation verdicts (if executed): append to `computations/s78_gate_verdicts.txt` with `S79-REMED-` prefix (per P1-3 N4 spec)

---

## Conventions (all Phase 2-5 workshops)

- Shell skeleton: build before any agent launches (per rclab-review skill §2 Step 1)
- 2 rounds default; increase to 3 only if user authorizes
- Substrate-first framing (phononic-framing.md rule)
- 4-tuple tag on every numerical claim (value, scheme, convention, L_max)
- F_amp = POWER RATIO (linear, never squared)
- S_IC = |α+β|²
- Gate verdicts are permanent — workshops re-interpret, never re-adjudicate
- W1-B and W2-C WARRANT-INVALID — Phase 2-5 agents flag dependency if they cite W1-B/W2-C-derived quantities

---

## Change Log

- **2026-04-16**: Plan authored. Phase 1 launched (P1-1, P1-2, P1-3). P1-1 and P1-3 closed same day. EVOI deferred to Phase 5 per user instruction.
