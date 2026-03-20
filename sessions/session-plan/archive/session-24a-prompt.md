# Session 24a: The Computation Sprint — V_spec, Berry, Neutrino R, A/C, Euclidean Action

## Session Type: COMPUTATION (7 cheap computations, all gates fire in one session)
## Agents: phonon-exflation-sim + coordinator
## Session Goal: Run all seven cheap computations from the Session 23 collab review's unanimous agenda. Every gate is classified in real time by coordinator as phonon-sim produces numbers. This session produces numbers and gate classifications only — no interpretation. Twenty lines of Python determine the framework's future.

---

# 0. OPERATIONAL RULES — READ BEFORE ANYTHING ELSE

## NO DEPENDENCIES — RUNS FIRST

All inputs exist from Sessions 20a, 23a, and 23c:
- `tier0-computation/s23c_fiber_integrals.npz` (V_spec inputs: R_K, |Ric|^2, K at 21 tau)
- `tier0-computation/r20a_riemann_tensor.npz` (Riemann tensor cross-check)
- `tier0-computation/s23a_kosmann_singlet.npz` (V_nm matrix, eigenvalues for Berry + neutrino R)
- `tier0-computation/s23a_eigenvectors_extended.npz` (eigenvalues for eigenvalue ratio map)

## NO INTERPRETATION IN 24a

Phonon-sim reports numbers. Coordinator classifies gates. Neither agent interprets. Interpretation is Phase 24b's job. If phonon-sim begins explaining what a result means, coordinator redirects: "Number reported. Gate classified. Proceed to next computation."

## GATE CLASSIFICATION IS COORDINATOR'S PRIMARY RESPONSIBILITY

Coordinator must classify each result against its pre-registered threshold the MOMENT phonon-sim reports the number. Do not wait until all computations are done. Classify as PASS / CLOSED / INCONCLUSIVE immediately. Pre-registered thresholds are in Section IV of this document — memorize them before computation begins.

## COMPUTATION DISCIPLINE

Every result classified against its pre-registered gate BEFORE any interpretation. Report the number first. Classify second. Interpret third.

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s24a_`

**COMPLETION SIGNAL**: Session ends ONLY when user approves shutdown explicitly; Password mechanism on team lead. Idle agents are not finished agents — or even actually idle.

---

# I. CONTEXT: THE UNANIMOUS AGENDA

Session 23 delivered a decisive BCS closure (K-1e), accidental selection rule discoveries (V(gap,gap) = 0, nearest-neighbor tight-binding), and a Sagan verdict dropping the framework to 8%/5% (panel/Sagan). The subsequent 15-agent collab review voted 15/15 to compute V_spec(tau; rho) = -R_K + rho*(500*R_K^2 - 32*|Ric|^2 - 28*K) as Priority 1. The review also identified six additional cheap computations that can run simultaneously:

| Priority | Computation | Cost | BF if passes | Data source |
|:---------|:-----------|:-----|:-------------|:------------|
| P24-1 | V_spec(tau; rho) at 5 rho values | 20 lines, <1 min | 5-15 | s23c_fiber_integrals.npz |
| P24-2 | Intra-sector Berry curvature | 10 lines, 30s | diagnostic | s23a_kosmann_singlet.npz |
| P24-3 | A/C gauge-gravity check | analytic | ~10 | s23c_AC_normalization.py |
| P24-4 | Neutrino R diagnostic | 20 lines, ms | 3-7 | s23a_kosmann_singlet.npz |
| P24-6 | Euclidean action at 3 monopoles | 5 lines, 0 | 3-5 | s24a_vspec.npz (after Step 1) |
| P24-8 | Eigenvalue ratio map | 30 lines, 30s | diagnostic | s23a_kosmann_singlet.npz |

Total runtime for ALL computations: under 5 minutes. If it takes longer, something is wrong.

**Post-Session-23 probability**: Panel 8% (range 6-10%), Sagan 5% (range 3-7%).

---

# II. REQUIRED READING

## ALL agents (MANDATORY):

1. **Session 23c synthesis**: `sessions/session-23/session-23c-synthesis.md`
   Sections VIII (A/C check formula), IX (Session 24 handoff, priority table P24-1 through P24-5).

2. **Session 23 Tesla-take master collab**: `sessions/session-23/session-23-tesla-take-master-collab.md`
   Section V (P24-1 through P24-10 priority list with formulas and data sources).

3. **Session 23a synthesis**: `sessions/session-23/session-23a-synthesis.md`
   Section III (selection rules, V_nm level structure: L1/L2/L3 definitions).

4. **Researcher index**: `researchers/index.md`
   Domain 4 (Effective Potential — V_spec as spectral action potential), Domain 7 (Spectral Statistics — Berry curvature on D_K).

5. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## Agent-specific required reading:

| Agent | Additional Reading | Researcher Index Ref |
|:------|:-------------------|:---------------------|
| phonon-exflation-sim | `tier0-computation/s23c_fiber_integrals_final.py` lines 1-50 (V_spec formula, data loading, curvature invariant definitions), `tier0-computation/s23c_fiber_integrals.npz` (load and verify keys) | Domain 4: Baptista-15 eq 3.80 (V_eff), Connes-07 (spectral action expansion), KK-10 (Freund-Rubin prototype) |
| coordinator | This prompt Section IV (pre-registered Constraint Gates). Memorize ALL thresholds before first computation completes | Domain 12: Sagan-10 (methodology), Sagan-13 (Bayesian framework) |

---

# III. COMPUTATION STEPS (strict ordering)

## Agent Allocation

| Agent | Role | Specific Responsibilities |
|:------|:-----|:-------------------------|
| phonon-exflation-sim | ALL numerical computation | Steps 1-6: V_spec, Berry, neutrino R, A/C, Euclidean action, eigenvalue ratios |
| coordinator | Gate classification + documentation | Classify EACH result in real time. Assemble 24a synthesis with gate table. |

### Step 1: V_spec(tau; rho) — THE PRIMARY COMPUTATION

**Background**: The spectral action on M^4 x (SU(3), g_Jensen) generates a modulus potential from the Gilkey a_4 heat kernel coefficient. This is structurally identical to Starobinsky R+R^2 gravity transposed to the internal space. The a_2 term contributes -R_K (destabilizing). The a_4 term contributes rho*(500*R_K^2 - 32*|Ric|^2 - 28*K) (stabilizing if rho > 0). Their competition may produce a minimum.

**Formula**:
```
V_spec(tau; rho) = -R_K(tau) + rho * [500*R_K(tau)^2 - 32*|Ric(tau)|^2 - 28*K(tau)]
```

where rho = c_4/c_2 = f_4/(60*f_2*Lambda^2).

**Data**: `s23c_fiber_integrals.npz` keys: `R_scalar`, `Ric_sq`, `K_kretschner`, `tau`.

**Procedure**:
1. Load data. Verify: R_scalar(0) = 2.000, a4_geom(0) = 1970.0 (exact: 500*4 - 32*1 - 28 = 1940... wait — verify from Gilkey formula with dim_spinor=16 trace factor. The key `a4_geom` in the npz already has the correct value — use that directly).
2. Compute V_spec at each rho in {0.001, 0.01, 0.05, 0.1, 0.5} × 21 tau values.
3. Find minimum at each rho: dV/dtau via finite differences, locate sign change.
4. Record tau_min(rho), V_spec(tau_min), V_spec''(tau_min).
5. **Secondary scan**: rho in {0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.10, 0.20, 0.50}. Plot tau_min(rho).
6. Plot V_spec(tau) for 5 primary rho values, physical window [0.20, 0.40] shaded.

**Output**: `s24a_vspec.py`, `s24a_vspec.npz`, `s24a_vspec.png`.

### Step 2: Intra-Sector Berry Curvature

**Background**: Berry curvature B_n(tau) measures eigenstate rotation rate under tau deformation. Uses SAME V_nm data as BCS but weighted by energy denominators squared. A peak near tau ~ 0.2-0.3 indicates rapid structural change at the gap edge.

**Formula**:
```
B_n(tau) = sum_{m != n} |V_nm(tau)|^2 / (E_n(tau) - E_m(tau))^2
```

**Data**: `s23a_kosmann_singlet.npz`.

**Procedure**:
1. Load V_nm(tau) and E_n(tau) for (0,0) singlet at 9 tau values.
2. Compute B_n(tau) for n = 1, 2 (gap-edge Kramers pair).
3. Plot B_1(tau), B_2(tau) vs tau.
4. Record peak magnitude and location.

**Output**: `s24a_berry.py`, `s24a_berry.npz`, `s24a_berry.png`.

### Step 3: Neutrino R Diagnostic

**Background**: Tight-binding hopping ratio (V_12/V_23)^2 ~ 25 vs measured R = 33.3. The proper computation: diagonalize H_eff and extract the 3 smallest eigenvalues.

**Formula**:
```
H_eff = diag(E_1, ..., E_16) + V_nm(tau = 0.30)
R = (m_3^2 - m_2^2) / (m_2^2 - m_1^2)
```

**Data**: `s23a_kosmann_singlet.npz`.

**Procedure**:
1. Load E_n and V_nm at tau = 0.30.
2. H_eff = diag(E) + V_nm. Diagonalize.
3. Extract 3 smallest |eigenvalues|: m_1 < m_2 < m_3.
4. R = (m_3^2 - m_2^2) / (m_2^2 - m_1^2).
5. Mixing angle: tan(2*theta_12) = 2*|H_{12}| / |H_{11} - H_{22}|.
6. Repeat at tau = 0.15, 0.20, 0.25, 0.35 for sensitivity.

**Output**: `s24a_neutrino.py`, `s24a_neutrino.txt`.

### Step 4: A/C Gauge-Gravity Consistency Check

**Background**: From spectral action a_2 dominance, tr(g_unit(tau_0)) = kappa^2 / (2*g_avg^2). BF ~ 10 if consistent within factor 2.

**Known**: tr(g_unit(0.30)) = 8.868 from `s23c_AC_normalization.py`. Formula: g_unit(tau) = diag(e^{2tau}[x3], e^{-2tau}[x3], e^{tau}[x2]).

**Procedure**:
1. tr(g_unit(tau)) = 3*e^{2tau} + 3*e^{-2tau} + 2*e^{tau}. Evaluate at tau = 0.15, 0.20, 0.25, 0.30, 0.35.
2. kappa^2/(2*g_avg^2) at Lambda = M_GUT (g^2 ~ 0.5): kappa^2/(2*0.5) = kappa^2.
3. Report consistency range.

**Output**: Inline in synthesis.

### Step 5: Euclidean Action at Three Monopoles

**Background**: I_E(tau) = -V_spec(tau) * Vol(K). If I_E at Jensen deformation < I_E at round metric, Jensen dominates path integral.

**Procedure**: Extract from Step 1 data at tau = 0.00, 0.10, 1.58 for each rho. Vol(K) = const (volume-preserving TT deformation, Session 12).

**Output**: Append to `s24a_vspec.npz`.

### Step 6: Eigenvalue Ratio Map

**Background**: Does phi_paasch = 1.53158 organize the eigenvalue ladder?

**Procedure**:
1. Extract 16 eigenvalues in (0,0) singlet at 9 tau from `s23a_kosmann_singlet.npz`.
2. r_n(tau) = |lambda_{n+1}| / |lambda_n| for n = 1,...,15.
3. Mark phi_paasch crossings (within 0.1%).
4. Heatmap plot.

**Output**: `s24a_eigenvalue_ratios.py`, `s24a_eigenvalue_ratios.npz`, `s24a_eigenvalue_ratios.png`.

### Step 7: Mandatory Gate Verdicts

Coordinator produces `tier0-computation/s24a_gate_verdicts.txt` with the full table from Section III, Step 7 of the master prompt.

Also produce `sessions/YYYY-MM-DD-session-24a-synthesis.md` with gate table and brief number-only summary. No interpretation.

---

# IV. PRE-REGISTERED Constraint GateS

## V-1: V_spec Monotone — CLOSED

**Condition**: V_spec(tau) monotonically decreasing or flat for ALL rho in [10^{-3}, 10^{3}].
**Consequence**: No spectral action minimum. Framework → ~5%/3%.
**Probability of firing**: ~40%.

## V-3: V_spec Minimum in [0.20, 0.40] — PASS

**Condition**: tau_min in [0.20, 0.40] for some rho in [10^{-3}, 10^{1}].
**Consequence**: Starobinsky on internal space works. BF ~ 5-15.

## R-1: Neutrino R in [17, 66] — PASS

**Condition**: R in [17, 66] from H_eff diagonalization.
**Consequence**: BF ~ 3-7. Gate reopens.

## AC-1: A/C Inconsistency — FAIL

**Condition**: Inconsistent by factor > 5 for all scale assumptions.
**Consequence**: BF ~ 0.5.

---

# V. OUTPUT FILES

| File | Producer | Content |
|:-----|:---------|:--------|
| `tier0-computation/s24a_vspec.py` | phonon-sim | V_spec computation |
| `tier0-computation/s24a_vspec.npz` | phonon-sim | V_spec data + Euclidean action |
| `tier0-computation/s24a_vspec.png` | phonon-sim | V_spec(tau) for 5 rho values |
| `tier0-computation/s24a_berry.py` | phonon-sim | Berry curvature |
| `tier0-computation/s24a_berry.npz` | phonon-sim | B_n(tau) data |
| `tier0-computation/s24a_berry.png` | phonon-sim | Berry curvature vs tau |
| `tier0-computation/s24a_neutrino.py` | phonon-sim | H_eff + R extraction |
| `tier0-computation/s24a_neutrino.txt` | phonon-sim | R value + gate verdict |
| `tier0-computation/s24a_eigenvalue_ratios.py` | phonon-sim | Ratio map |
| `tier0-computation/s24a_eigenvalue_ratios.npz` | phonon-sim | r_n(tau) data |
| `tier0-computation/s24a_eigenvalue_ratios.png` | phonon-sim | Heatmap with phi_paasch |
| `tier0-computation/s24a_gate_verdicts.txt` | coordinator | All gate verdicts |
| `sessions/YYYY-MM-DD-session-24a-synthesis.md` | coordinator | Number-only synthesis |

---

# VI. PRE-REGISTERED PROBABILITY SCENARIOS

All posteriors from post-Session-23 baselines: panel 8%, Sagan 5%.

| Outcome | Panel posterior | Sagan posterior | Path forward |
|:--------|:---------------|:----------------|:-------------|
| V_spec monotone (V-1 closes) | 5-7% | 2-3% | Endgame. |
| V_spec min outside [0.20, 0.40] | 6-8% | 3-5% | Marginal. |
| V_spec min in [0.20, 0.40] only | 20-30% | 8-12% | Starobinsky branch. |
| V_spec + R pass | 30-40% | 12-18% | Two structural contacts. |
| V_spec + R + A/C all pass | 35-45% | 15-20% | Three predictions. Near Level 3. |

---

# VII. WHAT THIS PHASE IS REALLY ABOUT

Twenty lines of Python. Thirty seconds of runtime. Six sessions since anyone ran a new computation on the spectral action potential. The data has been sitting in `s23c_fiber_integrals.npz` since Session 23c. The formula was identified by 15 independent reviewers as the #1 priority. Everyone agreed. Nobody computed it.

Session 24a computes it. Six additional computations ride alongside because they cost nothing — 10 lines each, existing data, seconds of runtime. The total computation time for all seven is under 5 minutes. The total information content is: which gates fire.

Run the numbers. Classify the gates. Move to 24b.

---

*Session 24a prompt split from Session 24 master prompt. Computation-only phase. All gates pre-registered in Section IV before computation begins. No interpretation until Phase 24b. Agent roster: 2 agents (CLAUDE.md maximum respected). Researcher index (researchers/index.md) Domains 4 and 7 cross-referenced for phonon-sim's required reading.*

*"Twenty lines of Python settles a range of 5-20% down to a number."*
