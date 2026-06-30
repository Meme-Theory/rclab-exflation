---
name: conditional-gate-and-qgge-dormancy
description: CONDITIONAL-gate trigger-first discipline + the W5-5 Q-GGE-PRECISION dormancy cross-link rule (inventory-annotation gates don't register ⟨Q⟩_GGE precision needs)
metadata:
  type: project
---

## CONDITIONAL-gate discipline (S95 W6-5 LEGGETT-GRAV-DECAY-CONDITIONAL)

A gate pre-registered as CONDITIONAL evaluates its pre-registered TRIGGER **first** (NUMBERS/trigger before gate before interpretation). Two outcomes:
- **Trigger FIRES** → run the gate computation in full → PASS/FAIL/INFO.
- **Trigger ABSENT** → emit the documented **CONDITIONAL-SKIP / PRE-REG-INC-by-design** verdict (carried as **INFO**, NOT a FAIL, NOT a PRU defect — the skip IS the expected default).

W6-5 trigger = "LEGGETT-GRAV-DECAY-67 CRITICAL gate confirmed PASS (Γ_grav<H_0) in KB AND S67/S73a audit_sha256 locatable." It FIRED (theorem proven_1967 CRITICAL; gate PASS; LEGGETT-GRAV-DECAY-73a τ_DM/t_univ=1.13e+65). The two existing Leggett-gate audit SHAs are carried by the **S81 batch-migration lines** (`T3-BATCH-S67-LEGGETT-GRAV-DECAY` `ceb8746c…`; `T3-BATCH-S73A-LEGGETT-GRAV-DECAY` `93b275ba…`) — the original session-67/73 verdict files do NOT exist at `computations/session-67|73/`; the batch-migration line IS the audit-traceable carrier (knowledge graph returns it for these gates).

## W5-5 Q-GGE-PRECISION dormancy cross-link (re-usable rule)

S95 W5-5 (`Q-GGE-PRECISION`) CONDITIONAL-SKIPped (T1=F, T2=F; T2 = `no_W6_Leggett-channel_DM_gate_present`). Its caveat re-activates (requeue S96) **IFF a Leggett-channel DM AMPLITUDE gate registers a ≥2-sig-fig ⟨Q⟩_GGE precision need.**

**Determination rule**: a falsifier-inventory **conditional-annotation / inventory** gate (like W6-5) is NOT a DM amplitude gate. It consumes the relic abundance (Ω_DM h²=0.120), the lifetime (τ_DM/t_univ), and the bound (Γ_grav<H_0) — none of which require the GGE projected charge ⟨Q⟩_GGE. So it does NOT register a ⟨Q⟩_GGE precision need → **W5-5 caveat stays DORMANT; Q-GGE-PRECISION CF does NOT re-activate.** The caveat only fires if a gate actually COMPUTES a Leggett DM amplitude/cross-section needing ⟨Q⟩_GGE to ≥2 sig figs.

## Conditional-PASS = SECOND DM-sector delicacy

Ω_DM h²=0.120 (Leggett-only, 0.70σ vs Planck 0.1186±0.0020) is a **conditional PASS**: PASS *given* Γ_grav<H_0. The bound is satisfied by ~65 OOM (Γ_grav/H_0 ~ 8.85e-66 = 1/(τ_DM/t_univ); Z_2 parity P_L from J-evenness of the condensate). This is the **SECOND** DM-sector delicacy; the FIRST is the 260σ full-DM over-closure that forces the Leggett-only channel. Both belong next to the Ω_DM h² row. Surfacing the conditional (NOT re-adjudicating the PASS) is the nazarewicz-collab §R2 fidelity fix — the doc must not present 0.120 as an unconditional clean PASS.

See also [[project_substrate-not-c-limited]] (Leggett DM = inter-band coherence mode is substrate dynamics). Falsifier-inventory Row #68 data lives in `sessions/framework/registry/falsifier-master-inventory.md` (NOT memory — AMRI).
