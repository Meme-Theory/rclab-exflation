# τ-flow (E7) vs q-flow (S62 #19) — Distinct-Axes Registry Note

**Landed**: S95 W5-6 (`TAU-FLOW-Q-FLOW-REGISTRY-NOTE`, METHODOLOGY-class per `.claude/rules/wave-classification.md` M1–M4; allowlist row `sha256_of_plan_block = ac0f215daefad38bc30bd9c73111b1931e9f7f9e1f84082e4be249badc723e95` in `methodology-wave-allowlist-ledger.md`). Orchestrator-direct-write (skips compute-mode). 2026-05-28.

## Statement

E7 (the τ-flow Structural Monotonicity Theorem) and the S62 CC-Monotonicity Theorem (#19, the q-flow theorem) are **two DISTINCT proven theorems on two DISTINCT axes**. They must not be conflated; in particular, the cosmological-constant layer (§7.1) rests on the **q-flow**, NOT the τ-ramp.

| Axis | Theorem | Monotone relation | Flow variable | Variable kind |
|:-----|:--------|:------------------|:--------------|:--------------|
| **τ-flow** | E7 Structural Monotonicity (W7/S37; PROVEN, 9,600/9,600 checks; permanent-results-registry structural-theorem row #13) | dS_SA/dτ > 0 (spectral action increases) | τ — the Jensen deformation parameter | **order-parameter texture** — a GEOMETRIC modulus (the Jensen TT-deformation of the internal metric); NOT conserved (it ramps and drives the transit) |
| **q-flow** | S62 CC-Monotonicity #19 (PROVEN; baseline-findings-s66 theorem #19; atlas-07 A9; permanent-results-registry structural-theorem row #19 "CC = Integrability") | dE_ZP/dq > 0 (no interior q-equilibrium) | q = N_pair — the vacuum particle number | **conserved microscopic charge** (Volovik q-theory) |

## Why they are distinct

- **τ** is a geometric modulus: it parameterizes the order-parameter texture (the internal-metric deformation). Its monotone flow `dS_SA/dτ > 0` drives the *transit* — the supersonic passage through the van Hove fold (S95 W2-3 confirmed this is one-loop-robust). τ is NOT conserved; it ramps from 0 through τ_fold = 0.190.
- **q = N_pair** is a conserved microscopic charge: the vacuum particle (Cooper-pair) number. Its monotone flow `dE_ZP/dq > 0` (no interior q-equilibrium) is what nullifies the cosmological constant at equilibrium: `ρ_Λ(equilibrium) = ε(q_eq) − q_eq·μ |_{P=0} = 0` exactly (S95 W5-3 `EQUILIBRIUM-CC-WARRANT` PASS, audit_sha256 `397cf4497d22db2bcb9c7e255a6b3209a742aa768a5f09a653fa5441ba5de762`).
- The identity `q = N_pair` is fixed: "P_vac = E_GGE − N_pair IS the q-theory formula with q = N_pair" (`s59_q_variable_results.txt`).

## The CC layer rests on the q-flow, NOT the τ-ramp

The §7.1 cosmological-constant warrant rests on the **q-flow** equilibrium/monotonicity theorem (`dE_ZP/dq > 0 ⇒ ρ_Λ(equilibrium) = 0`; W5-3). It does **NOT** rest on the τ-ramp (E7). Conflating them — e.g. treating the τ-monotonicity as if it warranted the CC nullification — would make one theorem appear to do double duty. The two are structurally orthogonal: one is a geometric-modulus flow (transit dynamics), the other a conserved-charge flow (vacuum thermodynamics). The W5-3 caveat applies to the q-flow leg only: the warrant is the *thermodynamic* (Gibbs–Duhem) one, NOT a topological protection (the substrate is 3He-B class, N₃=0, BDI).

## Provenance

- **E7 τ-flow**: E7 Structural Monotonicity Theorem, `dS_SA/dτ > 0` (knowledge MCP; `phonic-exflation-equation.md §5.1`; `permanent-results-registry.md` structural-theorem row #13 "Structural Monotonicity Theorem", S37, machine-ε).
- **S62 q-flow**: CC-Monotonicity Theorem #19, `dE_ZP/dq > 0`, no interior q-theory equilibrium (`baseline-findings-s66` theorem #19; atlas-07 A9; `permanent-results-registry.md` structural-theorem row #19 "CC = Integrability (Monotonicity Theorem)", S62, exact proof).
- **q = N_pair identity**: `computations/.../s59_q_variable_results.txt`.
- **CC warrant (downstream consumer)**: S95 W5-3 `EQUILIBRIUM-CC-WARRANT` PASS.

## Cross-references

- `phonic-exflation-equation.md §7.1` (CC layer — rests on q-flow; doc-integration `/rclab-workshop` should cite THIS note as the distinct-axes authority).
- `phonic-exflation-equation.md §5.3` (Ordered-Veil — the C2 fusion-sentence presentation defect is a SEPARATE issue, resolved by W5-1/W5-2; do not merge the two corrections).
- Plan block: `sessions/session-plan/session-95-plan-w5.md §W5-6`.
- This is the registry-hygiene realization of the volovik-collab R3 carry-forward.
