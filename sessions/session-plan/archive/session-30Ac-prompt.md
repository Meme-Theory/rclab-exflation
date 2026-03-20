# Session 30Ac: Pfaffian Refinement + N_max=3 Confirmation

**Date**: TBD
**Author**: Team-lead (promoted from 29B-7; originally Session 29Bc)
**Depends on**: Session 30Ab (Pfaffian scan at N_max = 2 complete — either P-30a or B-30a fired)
**Prerequisite**: 30Ab must complete. Both outcomes (sign change found OR no sign change) lead to this sub-session, but with different execution paths.
**Input data**:
- `tier0-computation/s30a_dtotal_pfaffian.npz` (N_max=2 Pfaffian scan results) — FROM 30Ab
- `tier0-computation/s30a_df_construction.npz` (D_F(tau) matrices) — FROM 30Aa
- `tier0-computation/s30a_gate_verdicts.txt` (B-30a / P-30a verdicts) — FROM 30Ab
- `tier0-computation/d2_pfaffian_computation.py` (Parlett-Reid Pfaffian algorithm)
- `tier0-computation/tier1_dirac_spectrum.py` (D_K eigenvalues per sector)

## Motivation

Session 30Ab delivered the N_max = 2 Pfaffian verdict. Session 30Ac provides the definitive confirmation.

**If P-30a fired (sign change found):** Two tasks:
1. **Bisection** (Step 6): Refine tau_c to $10^{-6}$ precision. Identify the zero-crossing mode and sector. Extract the critical exponent.
2. **N_max = 3 confirmation** (Step 7): Verify the sign change persists at higher truncation. This eliminates the possibility that the sign change is a truncation artifact.

**If B-30a fired (no sign change):** One task:
1. **N_max = 3 extension** (Step 7): Check whether a sign change appears at higher truncation that was missed at N_max = 2. If still no sign change, the topological route is definitively exhausted.

---

# SESSION DASHBOARD

## Prerequisites

| ID | Requirement | Source | Status |
|:---|:-----------|:-------|:-------|
| PRE-5 | 30Ab Pfaffian scan complete (P-30a or B-30a fired) | `s30a_gate_verdicts.txt` | BLOCKED (awaiting 30Ab) |

## Computation Steps (this sub-session)

| Step | Description | ~Lines | ~Cost | Status | Condition |
|:-----|:-----------|:-------|:------|:-------|:----------|
| 6 | Bisect to locate $\tau_c$ with $10^{-6}$ precision | reuse | minutes | PENDING | P-30a only |
| 7 | $N_{\max} = 3$ confirmation (3328-dim Pfaffian) | reuse | ~25-30 min | PENDING | Always |

## Gate Verdicts (this sub-session)

| ID | Type | Short Description | Status |
|:---|:-----|:-----------------|:-------|
| B-30a-final | Hard Close | Pf constant — no sign change at BOTH $N_{\max} = 2$ AND $N_{\max} = 3$ | PENDING |
| P-30a-confirmed | Positive | Pf sign change confirmed at $N_{\max} = 3$ | PENDING |
| P-30b | Positive | $\tau_c$ coincides with $\tau_{\text{cross}}$ (BCS) within 10% | PENDING |

## Deliverables

| Output | Description | Status |
|:-------|:-----------|:-------|
| `s30a_pfaffian_nmax3.py` | Steps 6-7 computation script | PENDING |
| `s30a_pfaffian_nmax3.npz` | N_max=3 Pfaffian scan, bisection results (if applicable), tau_c refined location | PENDING |
| `s30a_gate_verdicts.txt` | Final gate verdicts (B-30a-final / P-30a-confirmed / P-30b appended) | PENDING |

---

# 0. OPERATIONAL RULES

## COMPUTATION DISCIPLINE

Every result classified against its pre-registered gate BEFORE any interpretation. Report the number first. Classify second. Interpret third.

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s30a_`

## PRE-SESSION GATE CHECK (MANDATORY FIRST ACTION)

Before any computation, verify:
1. Read `tier0-computation/s30a_gate_verdicts.txt` — determine whether P-30a or B-30a fired
2. Load `s30a_dtotal_pfaffian.npz` — review the N_max=2 scan results
3. **Branch execution path**:
   - If P-30a fired → execute Steps 6 AND 7
   - If B-30a fired → execute Step 7 ONLY

## COMPLETION SIGNAL

Session ends ONLY when user approves shutdown explicitly. Idle agents are not finished agents.

---

# I. REQUIRED READING

## ALL agents (MANDATORY):

1. **Session 30Ab output**: `tier0-computation/s30a_dtotal_pfaffian.npz` and `s30a_gate_verdicts.txt` — N_max=2 Pfaffian results and P-30a/B-30a verdict.
2. **Session 30Aa output**: `tier0-computation/s30a_df_construction.npz` — D_F(tau) matrices for re-computation at N_max=3.
3. **Session 17c results**: `sessions/session-17/session-17c-results.md` — Original D_K Pfaffian for comparison.
4. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

---

# II. COMPUTATION STEPS

## Step 6: If Sign Change Found (P-30a), Bisect to Locate $\tau_c$

**Executes only if P-30a fired.**

Refine to $|\tau_c - \tau_{\text{grid}}| < 10^{-6}$ using bisection. Determine which eigenvalue of $D_{\text{total}}$ crosses zero. Identify the sector and mode.

**OoO-6a**: Near-zero mode mass scales as $m \sim |\tau_{\text{frozen}} - \tau_c|^{\nu}$ with $\nu = 1$ for mean-field BDI — report this exponent. FFLO/Pauli-limited superconductor analog (CeCoIn$_5$).

**P-30b check**: Compare $\tau_c$ to $\tau_{\text{cross}}$ (BCS transition from Session 29Ab). If $|\tau_c - \tau_{\text{cross}}|/\tau_{\text{cross}} < 0.10$, P-30b fires — topological and dynamical stabilization AGREE.

## Step 7: $N_{\max} = 3$ Confirmation

**Executes in all cases.**

Extend the computation to $N_{\max} = 3$. The truncated Hilbert space grows:

$$\dim(\mathcal{H}_{\text{trunc}}^{N=3}) = (1 + 3 + 3 + 6 + 6 + 8 + 10 + 10 + 15 + 15 + 24 + 3) \times 16 = 1664$$

The antisymmetric matrix for the Pfaffian is $3328 \times 3328$. **~25-30 min total runtime.**

Steps required for N_max = 3:
1. Rerun Steps 0-3 (from 30Aa) with $N_{\max} = 3$ sectors: add (3,0), (0,3), (2,1), (1,2), (3,1)*, (1,3)*, etc. up to p+q=3
2. Rerun Steps 4-5 (from 30Ab) with the larger D_F and D_total matrices
3. Compare Pfaffian signs at N_max = 2 and N_max = 3

**Verdict logic:**

| N_max = 2 | N_max = 3 | Final Verdict |
|:----------|:----------|:-------------|
| Sign change (P-30a) | Sign change at same tau_c ± 10% | **P-30a-confirmed** — topological prediction robust |
| Sign change (P-30a) | No sign change | **AMBIGUOUS** — truncation artifact. Report but no probability update. |
| No sign change (B-30a) | Sign change | **P-30a-confirmed** — sign change was below N_max=2 resolution |
| No sign change (B-30a) | No sign change | **B-30a-final** — topological route fully exhausted |

**OoO-7a**: Finite-size scaling check — does $\lambda_{\min}$ at $\tau_c^{(N=2)}$ decrease with $N_{\max}$? Decreasing confirms convergence. If sign change found and zero-crossing mode identified, pull that fermion's mass measurement from VizieR `B/pdg`.

---

# III. CONSTRAINT CONDITIONS AND GATE STRUCTURE

## Final Hard Close

| ID | Condition | Consequence |
|:---|:----------|:------------|
| B-30a-final | Pf(J * D_total) constant for all tau (no sign change) at BOTH N_max = 2 AND N_max = 3 | Topological route fully exhausted. No Level 4 prediction from topology. No probability change (topological route was already "open" status). |

## Final Positive Signals

| ID | Condition | Consequence |
|:---|:----------|:------------|
| P-30a-confirmed | Pf(J * D_total) sign change confirmed at N_max = 3 | Level 4 topological prediction. Zero-parameter binary test. Massless fermion at tau_c. Testable by KATRIN, Planck+DESI, Project 8. **Framework probability jumps to 20-40%.** |
| P-30b | tau_c coincides with tau_cross (BCS transition from 29Ab) within 10% | Topological and dynamical stabilization AGREE. Dramatically strengthens framework. |

---

# IV. OUTPUT FILES

| Output | Contents |
|:-------|:---------|
| `s30a_pfaffian_nmax3.npz` | `tau_values_n3` (N_max=3 scan grid), `pf_values_n3`, `pf_signs_n3`, `min_gap_n3`, `tau_c_refined` (bisection result, if applicable), `critical_exponent_nu` (if applicable), `tau_c_vs_tau_cross` (P-30b comparison, if applicable) |
| `s30a_pfaffian_nmax3.py` | Complete Steps 6-7 script |

Gate verdicts appended to: `tier0-computation/s30a_gate_verdicts.txt`

---

# V. AGENT ASSIGNMENTS

| Agent | Role |
|:------|:-----|
| **phonon-exflation-sim** | Primary computation: bisection, N_max=3 extension, finite-size scaling |
| **coordinator** | Gate tracking, final synthesis |

**Recommended team**: 2 agents. Computational work dominates — theoretical oversight was provided in 30Aa.

**Blast-first spawn workflow applies** (CLAUDE.md mandatory).

---

# VI. SUCCESS CRITERIA

Session 30Ac is successful if it produces:

1. **A definitive D_total Pfaffian verdict** — sign change confirmed or definitively absent at N_max = 3
2. **If sign change confirmed**: tau_c refined to $10^{-6}$, P-30b comparison to tau_cross, zero-crossing mode identification, critical exponent
3. **If no sign change at either N_max**: spectral gap diagnostic (how close does D_total come to closing?), finite-size scaling analysis
4. **Final probability assessment** incorporating all 30A sub-session results

### Possible Outcomes and Probability Impact

| Outcome | Probability Impact |
|:--------|:------------------|
| P-30a-confirmed + P-30b (sign change at tau_cross) | **20-40%** — Level 4 topological prediction, zero parameters |
| P-30a-confirmed only (sign change, not at tau_cross) | **15-25%** — topological prediction exists but no dynamical coincidence |
| B-30a-final (no sign change, N_max = 2 and 3) | **No change** — topological route was already "open" status |

Combined with 29A and 29Ba/29Bb, this completes the Session 28 Fusion Synthesis's full 8-priority list PLUS the long-deferred topological test from Session 18.

---

*Steps 6-7 of the D_total Pfaffian computation. Bisection refinement (if sign change found) + N_max=3 confirmation (always). ~25-30 min runtime for N_max=3 (3328-dim Pfaffian). Delivers the FINAL topological verdict: P-30a-confirmed (20-40% probability) or B-30a-final (topological route exhausted). The crown jewel computation, deferred since Session 18.*
