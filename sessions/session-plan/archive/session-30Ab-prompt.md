# Session 30Ab: D_total Pfaffian Scan — The Topological Verdict

**Date**: TBD
**Author**: Team-lead (promoted from 29B-7; originally Session 29Bc)
**Depends on**: Session 30Aa (D_F construction must succeed — B-30b did NOT fire)
**Prerequisite**: 30Aa must complete with B-30b NOT firing. D_F(tau) matrices available in `s30a_df_construction.npz`. Chirality check documented.
**Input data**:
- `tier0-computation/s30a_df_construction.npz` (D_F(tau) matrices, eigenvectors, chirality norms) — FROM 30Aa
- `tier0-computation/d2_pfaffian_computation.py` (Parlett-Reid Pfaffian algorithm, (0,0) sector framework — to be adapted)
- `tier0-computation/branching_computation_32dim.py` (Xi, G5, gamma_F, particle identification)
- `tier0-computation/tier1_dirac_spectrum.py` (D_K eigenvalues per sector)

## Motivation

Session 30Aa delivered the D_F(tau) matrix — the finite Dirac operator derived purely from KK geometry. Session 30Ab now constructs the full $D_{\text{total}}$ and runs the Pfaffian scan. This is the decisive binary test: **does the Pfaffian of $D_{\text{total}}$ change sign as tau varies?**

A sign change produces a **topologically protected massless fermion** — a Level 4 novel prediction testable by KATRIN ($\sum m_\nu$), Planck+DESI, and Project 8. This would be the framework's single strongest observational prediction. Zero external parameters.

If $D_{\text{total}}$ has a Pfaffian sign change at some $\tau_c$, it produces:
- A zero-parameter binary prediction (sign changes or not)
- A specific critical deformation $\tau_c$ where the gap closes
- A testable fermion mass prediction

---

# SESSION DASHBOARD

## Prerequisites

| ID | Requirement | Source | Status |
|:---|:-----------|:-------|:-------|
| PRE-3 | D_F construction succeeded (B-30b did NOT fire) | `s30a_gate_verdicts.txt` | BLOCKED (awaiting 30Aa) |
| PRE-4 | D_F(tau) matrices available | `s30a_df_construction.npz` | BLOCKED (awaiting 30Aa) |

## Computation Steps (this sub-session)

| Step | Description | ~Lines | ~Cost | Status |
|:-----|:-----------|:-------|:------|:-------|
| 4 | Construct $D_{\text{total}}(\tau)$ and antisymmetric $M(\tau)$ (864-dim) | ~30 | minutes | PENDING |
| 5 | Pfaffian scan over $\tau \in [0, 2.5]$ at $N_{\max} = 2$ | ~50 | ~6-8 min | PENDING |

## Gate Verdicts (this sub-session)

| ID | Type | Short Description | Status |
|:---|:-----|:-----------------|:-------|
| B-30a | Hard Close | Pf constant — no sign change at $N_{\max} = 2$ | PENDING |
| P-30a | Positive | Pf sign change at some $\tau_c \in [0, 2.5]$ | PENDING |

## Deliverables

| Output | Description | Status |
|:-------|:-----------|:-------|
| `s30a_dtotal_pfaffian.py` | Steps 4-5 computation script | PENDING |
| `s30a_dtotal_pfaffian.npz` | Pfaffian scan: signs, gaps, D_F norms, sign-change locations | PENDING |
| `s30a_gate_verdicts.txt` | Gate verdict log (B-30a, P-30a appended) | PENDING |

---

# 0. OPERATIONAL RULES

## COMPUTATION DISCIPLINE

Every result classified against its pre-registered gate BEFORE any interpretation. Report the number first. Classify second. Interpret third.

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s30a_`

## PRE-SESSION GATE CHECK (MANDATORY FIRST ACTION)

Before any computation, verify:
1. Read `tier0-computation/s30a_gate_verdicts.txt` — B-30b must NOT have fired
2. Confirm `s30a_df_construction.npz` exists and loads correctly
3. Review chirality norms from 30Aa — document severity if $\|D_F \gamma_F + \gamma_F D_F\| > 10^{-10}$

If D_F construction failed (B-30b fired), **this session does not proceed**.

## COMPLETION SIGNAL

Session ends ONLY when user approves shutdown explicitly. Idle agents are not finished agents.

---

# I. REQUIRED READING

## ALL agents (MANDATORY):

1. **Session 30Aa output**: `tier0-computation/s30a_df_construction.npz` and `s30a_gate_verdicts.txt` — D_F construction results and B-30b verdict.
2. **Session 29B plan Section III (29B-7)**: `sessions/session-plan/session-29B-plan.md` — The full 29B-7 specification.
3. **Session 17c results**: `sessions/session-17/session-17c-results.md` — Original D_K Pfaffian computation. Z_2 = +1 for all tau. Parlett-Reid implementation.
4. **Session 22b results**: `sessions/session-22/session-22b-results.md` — D_K block-diagonality theorem.
5. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## Agent-specific required reading:

| Agent | Additional Reading |
|:------|:-------------------|
| phonon-exflation-sim | `tier0-computation/d2_pfaffian_computation.py` (Parlett-Reid algorithm to adapt for 864-dim), `tier0-computation/s30a_df_construction.py` (30Aa script for D_F loading) |
| coordinator | This prompt gate conditions (Section III). Memorize ALL thresholds before first computation completes |

---

# II. COMPUTATION STEPS

## Step 4: Construct $D_{\text{total}}(\tau)$ and Antisymmetric Matrix $M(\tau)$

$$D_{\text{total}} = D_K \otimes \mathbf{1}_{32} + \gamma_5^{(K)} \otimes D_F$$

in the full $\mathcal{H}_{\text{trunc}} \otimes \mathbb{C}^{32}$ space. Construct $M = \Xi \cdot D_{\text{total}}$ and verify antisymmetry $M + M^T = 0$. The antisymmetric matrix is $864 \times 864$. **~30 lines.**

**OoO-4a**: Report $\|D_F\|/\|D_K\|$ as a function of $\tau$ — determines weak-pairing (trivial, no sign change) vs strong-pairing (topological) regime. Kitaev chain analog: gap never closes if pairing is too weak.

## Step 5: Pfaffian Scan over $\tau \in [0, 2.5]$

Use the Parlett-Reid algorithm (already implemented in `d2_pfaffian_computation.py`) to compute $\text{Pf}(M(\tau))$ at 50-100 tau values. Track the sign. Any sign change indicates a topological phase transition. **~50 lines (adapted from existing).**

**Computational cost**: ~6-8 minutes for complete scan at $N_{\max} = 2$.

**OoO-5a**: If sign change found, pull neutrino mass bounds — KATRIN ($m_{\bar{\nu}_e} < 0.45$ eV), Planck+DESI ($\sum m_\nu < 0.072$ eV), NuFIT oscillation parameters ($\Delta m^2_{21}$, $|\Delta m^2_{31}|$) via VizieR `B/pdg`. **Critical CM diagnostic**: gap must close at the sign change ($\lambda_{\min}(D_{\text{total}}) \to 0$ at $\tau_c$) or it is a gauge artifact. Always plot $\lambda_{\min}(D_{\text{total}})$ alongside Pfaffian sign (Cu$_x$Bi$_2$Se$_3$, UTe$_2$ precedent).

---

# III. CONSTRAINT CONDITIONS AND GATE STRUCTURE

## Hard Close

| ID | Condition | Consequence |
|:---|:----------|:------------|
| B-30a | Pf(J * D_total) constant for all tau (no sign change) at $N_{\max} = 2$ | Topological route exhausted at this truncation. Extend to N_max = 3 in 30Ac for confirmation. No probability change (topological route was already "open" status). |

## Positive Signal

| ID | Condition | Consequence |
|:---|:----------|:------------|
| P-30a | Pf(J * D_total) sign change at tau_c in [0, 2.5] | Level 4 topological prediction. Zero-parameter binary test. Massless fermion at tau_c. Testable by KATRIN, Planck+DESI, Project 8. **Framework probability jumps to 20-40%.** Proceed to 30Ac for refinement. |

## Diagnostic Outputs (Even If No Sign Change)

Even B-30a (no sign change) produces valuable diagnostics:
- Spectral gap of $D_{\text{total}}(\tau)$ as a function of tau (how close does it come to closing?)
- tau-dependence of $D_F(\tau)$ (does it have a natural scale compared to $D_K$?)
- Order-one condition violation as a function of tau (does it improve at the BCS point?)
- Cross-validation of C-6 (6/7 NCG axioms) with the explicit $D_F$ construction

---

# IV. NEW CODE INVENTORY

| Component | Lines | Description |
|:----------|:------|:------------|
| $D_{\text{total}}$ tensor product construction | ~30 | Tensor product with chirality |
| Extended $\Xi_{32}$ to $\Xi_{\text{trunc}}$ | ~20 | Block-diagonal extension of existing Xi |
| Pfaffian scan driver | ~50 | Adapt from `d2_pfaffian_computation.py` |
| **Total new code** | **~100** | Core algorithms (Pfaffian, Dirac spectrum) all reused |

---

# V. OUTPUT FILES

| Output | Contents |
|:-------|:---------|
| `s30a_dtotal_pfaffian.npz` | `tau_values` (scan grid), `pf_values` (Pfaffian at each tau), `pf_signs` (sign(Re(Pf))), `min_gap_dtotal` (min eigenvalue of D_total), `D_F_norm` (Frobenius norm of D_F), `order_one_norm` (order-one violation), `sign_change_tau` (tau values where sign changes, empty if none) |
| `s30a_dtotal_pfaffian.py` | Complete script |

Gate verdicts appended to: `tier0-computation/s30a_gate_verdicts.txt`

---

# VI. AGENT ASSIGNMENTS

| Agent | Role |
|:------|:-----|
| **phonon-exflation-sim** | Primary computation: D_total construction, Pfaffian scan, sign tracking |
| **coordinator** | Gate tracking, diagnostic output coordination |

**Recommended team**: 2 agents minimum. The heavy theoretical work was done in 30Aa; this is primarily computational execution.

**Blast-first spawn workflow applies** (CLAUDE.md mandatory).

---

# VII. PASS CONDITION FOR 30Ac

30Ac proceeds if:
- **P-30a fired** (sign change found): 30Ac runs bisection refinement (Step 6) + N_max = 3 confirmation (Step 7)
- **B-30a fired** (no sign change at N_max = 2): 30Ac runs N_max = 3 extension only (Step 7) to check truncation stability

In either case, 30Ac provides the final definitive verdict.

---

*Steps 4-5 of the D_total Pfaffian computation. Constructs D_total from 30Aa's D_F(tau) and runs the Pfaffian sign scan. ~100 lines new code. ~6-8 min runtime. Binary verdict: sign change (P-30a, 20-40% probability boost) or constant (B-30a, no change). Proceed to 30Ac in either case.*
