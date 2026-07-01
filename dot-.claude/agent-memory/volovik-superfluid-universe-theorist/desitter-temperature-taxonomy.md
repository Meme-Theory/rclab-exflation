---
name: desitter-temperature-taxonomy
description: Three de Sitter temperatures in the framework + which physical process selects each + the exact squared-Boltzmann relation (W4-4 convention audit)
metadata:
  type: reference
---

# de Sitter temperature taxonomy (INV11-W4-4 convention audit, PASS)

The framework carries THREE distinct temperatures in the de Sitter / relic context. Mis-applying one for another squares (or square-roots) every `exp(-E/T)` Boltzmann factor. Determined by which physical PROCESS the rate describes:

| T | value | governs | corpus citation |
|:--|:------|:--------|:----------------|
| **T_local** (bulk) | `H/π = 2·T_GH` | matter creation / single-particle bulk ionization / **de Sitter DECAY rate** Γ_dS | Volovik #15 (2312.02292) Eq.5 (WKB ionization), §II (single-particle), Eq.13 (triplication Γ~exp(−2m/T)); #11 (2504.05763) §II restatement; #35 §III.B |
| **T_GH** (horizon) | `H/2π` | horizon ENTROPY/AREA (`S_dS=A/4G`) + horizon FIRST LAW + two-particle Hawking co-tunneling | H-BH-6 (Paper #07); S61 §2/§5; Volovik #11 §V (horizon first law uses T_GH) |
| **T_GGE** (substrate-internal) | `0.135 M_KK` | frozen-relic pair-transfer `Γ_pair=Γ_raw·exp(−ΔE/T_GGE)` — NOT a de Sitter T at all | S59 mack-landau-workshop |

## The factor-2 / squared-Boltzmann relation (EXACT; Sage residual 0)
`T_local/T_GH = 2` (exact). `B(T)=exp(−E/T)` ⇒ **`B(T_GH) = [B(T_local)]²`**, hence `Γ_dS(T_GH) = [Γ_dS(T_local)]²`.
**Direction**: `T_local > T_GH` ⇒ `exp(−E/T_local)` is LESS suppressed (= the **square-root** of the horizon factor). Using T_GH where T_local is correct **OVER-suppresses (squares)** the rate.

## Physical origin of the factor 2 (Volovik #15 §II)
WKB ionization of an atom by the de Sitter gravitational field is a **single-particle local** process → `w~exp(−πE/H)=exp(−E/T)`, `T=H/π`. Hawking emission across the horizon is **two-particle coherent co-tunneling** → half the temperature, `T_GH=H/2π`. The factor 2 is the one-particle-vs-two-particle distinction.

## Cross-attribution (seed #15 vs S61 "Paper 11") — CONSISTENT, not contradictory
#15 Eq.5 DERIVES T_local=H/π (primary WKB derivation). #11 §II RESTATES it + uses it in local thermo + horizon first law §V. #35 §III.B concurs. S61's "Paper 11" attribution is correct for the restatement; the seed's "#15" is correct for the primary derivation. No discrepancy.

## Load-bearing consequence for future de Sitter-rate work
Any rate of the form `exp(−E/T)` for MATTER CREATION / DECAY on the substrate de Sitter state MUST use `T_local=H/π`. The de Sitter DECAY rate Γ_dS (INV11-W4-3's deliverable) inherits this: W4-3 plan pin `convention=ABSOLUTE-LOCAL-T-H-OVER-PI` is CONFIRMED CORRECT. The GGE-relic rate is unaffected (substrate-internal T_GGE; isolated-relic N_pair-change rate is structurally ZERO by energy conservation, E_GS(2)>E_GS(1)). Entropy/area + first-law correctly stay on T_GH.

Links: [[project_volovik-convergence]], [[josephson-leggett-mix-78]].
