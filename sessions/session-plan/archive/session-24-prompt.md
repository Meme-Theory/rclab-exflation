# Session 24: V_spec, Selection Rules, and the Curvature-Squared Potential — The 20-Line Verdict

## Session Type: COMPUTATION SPRINT + PANEL REVIEW (binary gate battery on 7 cheap computations)
## Session Goal: Compute all seven cheap computations from the Session 23 collab review's unanimous agenda. Every gate fires or doesn't in 24a. Interpret in 24b. Branch in 24c based on which world fired. A 20-line Python script determines whether the framework lives or dies.

---

## Session Structure

Session 24 is a three-phase pipeline with conditional branching after 24a:

| Phase | Type | Agents | Dependencies | Duration | Question answered |
|:------|:-----|:-------|:-------------|:---------|:-----------------|
| 24a | Computation sprint | phonon-exflation-sim + coordinator | Existing 23a/23c data | Hours | What do V_spec, Berry, R, A/C, and Euclidean action gates show? |
| 24b | Panel review | sagan-empiricist + einstein-theorist + coordinator | Requires 24a output | ~1 day | What does the gate pattern mean? Combined BF. Branch assignment. |
| 24c | CONDITIONAL (two branches) | See below | Requires 24b verdict | ~1 day | Deep dive on whichever world 24a selected |

**Branching logic**:
- If V_spec has minimum in [0.20, 0.40] AND at least one secondary gate passes: Session 24 = 24a + 24b + 24c(Starobinsky). Framework → 20-40%. Session 25: Landau d_eff=1 fluctuation analysis + thermal disruption.
- If V_spec is monotonic for all rho: Session 24 = 24a + 24b + 24c(Endgame). Framework → ~5%. Only remaining question: permanent NCG result write-up.
- If V_spec is ambiguous (minimum outside [0.20, 0.40] or only for extreme rho): Session 24 = 24a + 24b + 24c(rho-constraint). Question shifts to whether NCG constrains rho.

---

# 0. OPERATIONAL RULES — READ BEFORE ANYTHING ELSE

## COMPUTATION FIRST, INTERPRET SECOND

Phase 24a runs ALL seven cheap computations before any interpretation begins. Do not begin interpretation in 24a. 24a outputs numbers + gate classifications only. Interpretation is Phase 24b's job.

## COMPUTATION DISCIPLINE

Every result must be classified against its pre-registered Constraint Gate BEFORE any interpretation is attempted. Report the number first. Classify second. Interpret third.

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s24a_` for Phase 24a, `s24b_` for Phase 24b

## MESSAGE PROTOCOL

**Work step, then inbox, work step, then inbox.** Never read more than 2 files or complete more than 1 computation block without checking messages. If you discover a connection to another agent's domain, message IMMEDIATELY.

**COMPLETION SIGNAL**: Session ends ONLY when user approves shutdown explicitly; Password mechanism on team lead. Idle agents are not finished agents — or even actually idle.

---

# I. CONTEXT: WHERE WE ARE

## The Post-Session-23 State

Session 23 ran three sub-phases and produced four findings that define Session 24:

**K-1e DECISIVE CLOSURE (23a)**: The Kosmann-BCS gap equation at mu = 0 yields Delta = 0 at all 9 tau values. M_max = 0.077-0.149 (needs > 1.0). Factor 6.5-12.9x below threshold. The spectral gap (2*lambda_min = 1.644) prevents BCS pairing — no Fermi surface means Cooper instability does not apply. This closure is genuine, clean, Einstein-validated, and irreversible at mu = 0. Framework drops to 8%/5% (panel/Sagan).

**Selection rules discovered (23a)**: V(gap,gap) = 0 EXACTLY (machine epsilon squared ~10^{-29}). V(L1,L3) = 0 exactly. V(L2,L2) = 0 exactly. These were not anticipated. The V_nm matrix defines a nearest-neighbor tight-binding Hamiltonian on the spectral lattice with hopping V(L1,L2) = 0.07-0.13 and V(L2,L3) = 0.01-0.03. The hopping ratio (V_12/V_23)^2 ~ 25 is within factor 1.3 of the neutrino atmospheric-solar ratio R = 33.3. First framework contact with oscillation data.

**P2a BF revised downward (23c)**: The f-dependence problem closes Scenario C and sub-scenario A3. beta/alpha CANNOT be derived with zero free parameters — the universal piece f_4/(f_8*Lambda^4) introduces one genuinely free parameter. BF drops from 50-100 to 5-15. Scenario C CLOSED: |omega_3|^2 is NOT in the Baptista submersion formula (7% residual, 5 independent numerical tests).

**V_spec discovered (23c)**: The spectral action generates a distinct modulus potential V_spec(tau; rho) = -R_K + rho*(500*R_K^2 - 32*|Ric|^2 - 28*K) from the Gilkey a_4 combination. This is structurally identical to Starobinsky R^2 gravity applied to the internal space. All data exists in `s23c_fiber_integrals.npz`. 20 lines of Python. **Nobody computed it.** The 15-agent collab review voted 15/15 to compute this before anything else. An A/C gauge-gravity consistency check (tr(g_unit(tau_0)) = kappa^2/(2*g_avg^2)) has BF ~ 10, independently of the f-dependence problem.

## Corrections From Session 23c (MUST propagate)

1. Session 21b Valar plan line 773 ("both V_FR terms come from same R_P"): **HALF-WRONG**. Only alpha*R_K comes from R_P (a_2 level). The flux term beta*|omega_3|^2 requires a_4 curvature-squared physics.
2. V_spec and V_FR are genuinely different potentials. KK-2 confirmed 7% residual: |omega_3|^2 is NOT a linear combination of the Gilkey a_4 basis {R_K^2, |Ric|^2, K}.
3. Session 22d BF=50-100 for P2a: **CLOSED**. Revised to 5-15 (geometric piece at one free parameter).

## The Key Insight From the 15-Agent Collab

The Session 23 arc closed the last energetic stabilization mechanism (BCS) but accidentally discovered the framework's most informative structural data: selection rules that produce a neutrino R ~ 25, a V_spec potential that nobody computed, and a tight-binding band structure that may predict mixing angles. The question for Session 24 is whether these structural discoveries produce numbers that match reality. The computation costs 20 lines and 30 seconds.

**As the master collab concluded**: "A 20-line Python script determines whether the framework lives or dies."

## Framework Probability

**Current (post-23c)**: Panel 8% (range 6-10%), Sagan 5% (range 3-7%).

**Conditional structure (pre-registered from Session 23 Tesla-take master synthesis)**:

| Outcome | Panel | Sagan |
|:--------|:------|:------|
| V_spec minimum in [0.20, 0.40] | 20-30% | 8-12% |
| V_spec + Berry + R all pass | 30-40% | 12-18% |
| V_spec + R + A/C all pass | 35-45% | 15-20% |
| All fail | 5-7% | 2-3% |

---

# II. REQUIRED READING

## ALL agents (MANDATORY):

1. **Session 23c synthesis**: `sessions/session-23/session-23c-synthesis.md`
   Read completely. Primary context document. Section IX (Session 24 handoff, priority-ordered questions) and Section VIII (A/C gauge-gravity consistency check).

2. **Session 23 Tesla-take master collab**: `sessions/session-23/session-23-tesla-take-master-collab.md`
   Section II (convergent themes), Section V (P24-1 through P24-10 priority list), Section VI (probability assessments). The 15/15 unanimous vote for V_spec.

3. **Session 23a synthesis**: `sessions/session-23/session-23a-synthesis.md`
   Sections II (Constraint Gate verdicts), III (selection rules). V_nm matrix structure for Berry curvature and neutrino R computations.

4. **Researcher index**: `researchers/index.md`
   Domain 4 (Effective Potential — V_spec context), Domain 7 (Spectral Statistics — Berry curvature), Domain 12 (Empirical Methodology — Sagan Standard).

5. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## Agent-specific required reading:

| Agent | Additional Reading | Researcher Index Reference |
|:------|:-------------------|:--------------------------|
| phonon-exflation-sim | `tier0-computation/s23c_fiber_integrals_final.py` (V_spec formula + data loading), `s23c_fiber_integrals.npz` (curvature invariants at 21 tau), `s23a_kosmann_singlet.npz` (V_nm for Berry + neutrino R), `s23a_eigenvectors_extended.npz` (eigenvalues) | Domain 4: Hawking-07, Landau-04, Baptista-15 (V_eff machinery). Domain 3: Baptista-17 eq 3.8 (D_K structure) |
| coordinator | `sessions/session-23/session-23b-synthesis.md` Section IV (Constraint Registry). This prompt Section IV (Constraint Gates — memorize thresholds before computation) | Domain 12: Sagan-10 (methodology), Sagan-13 (Bayesian framework) |
| sagan-empiricist (24b) | `sessions/session-23/session-23-sagan-verdict.md` (previous Sagan verdict structure), `sessions/session-23/session-23-tesla-take-sagan-collab.md` (Sagan's pre-registered gates for Tesla's computations) | Domain 12: Sagan-10, Sagan-12 (ALH84001 cautionary), Sagan-13 (Seager Bayesian), Sagan-14 (phosphine parallel) |
| einstein-theorist (24b) | `sessions/session-23/session-23-tesla-take-einstein-collab.md` (Einstein's EIH constraint, CC problem, Starobinsky connection) | Domain 8: Hawking-07 (Euclidean = spectral action), Einstein-07 (cosmological constant). Domain 4: KK-10 (Freund-Rubin), KK-11 (Lichnerowicz) |
| landau-condensed-matter-theorist (24c) | `sessions/session-23/session-23-tesla-take-landau-collab.md` (d_eff=1 fluctuation argument, Ginzburg criterion, Mermin-Wagner) | Domain 4: Landau-04 (mean-field exactness at d=8, but d_eff=1 for modulus). Domain 5: Landau-08 (GL equation) |

---

# III. PHASE 24a: THE COMPUTATION SPRINT

## Agent Allocation

| Agent | Role | Specific Responsibilities |
|:------|:-----|:-------------------------|
| phonon-exflation-sim | ALL numerical computation | Steps 1-6: V_spec, Berry, neutrino R, A/C, Euclidean action, eigenvalue ratios |
| coordinator | Gate classification + documentation | Classify EACH gate result the moment phonon-sim reports a number, BEFORE phonon-sim continues. Real-time classification. Assemble 24a synthesis. |

**Critical rule**: No interpretation in 24a. Numbers and gate verdicts only. If phonon-sim begins explaining what a result means, coordinator must redirect: "Number reported. Gate classified. Proceed to next computation."

### Step 1: V_spec(tau; rho) — THE PRIMARY COMPUTATION (P24-1)

**Background**: The spectral action on M^4 x (SU(3), g_Jensen) generates a modulus potential from the Gilkey a_4 heat kernel coefficient. The a_2 term contributes -R_K (linear curvature, destabilizing) and the a_4 term contributes rho*(500*R_K^2 - 32*|Ric|^2 - 28*K) (curvature-squared, stabilizing if rho > 0). Their competition may produce a minimum. This is structurally identical to Starobinsky R+R^2 gravity transposed to the internal space.

**Formula**:
```
V_spec(tau; rho) = -R_K(tau) + rho * [500*R_K(tau)^2 - 32*|Ric(tau)|^2 - 28*K(tau)]
```

where rho = c_4/c_2 = f_4/(60*f_2*Lambda^2) is the single free parameter.

**Data sources**:
- `tier0-computation/s23c_fiber_integrals.npz`: Keys `R_scalar`, `Ric_sq`, `K_kretschner`, `tau` at 21 points
- `tier0-computation/r20a_riemann_tensor.npz`: Cross-check source

**Procedure**:

1. Load `s23c_fiber_integrals.npz`. Verify: R_scalar(0) = 2.000, a4_geom(0) = 1970.0 (exact: 500*4 - 16*2 - 28 = 1970), tau grid covers [0, 2.0] at 21 points.

2. For each rho in {0.001, 0.01, 0.05, 0.1, 0.5}:
   - Compute V_spec(tau) at all 21 tau values
   - Find minimum (if any): dV/dtau by finite differences, locate zero crossing
   - Record: tau_min, V_spec(tau_min), V_spec''(tau_min) (second derivative)

3. Plot V_spec(tau) for all 5 rho values on one figure, physical window [0.20, 0.40] shaded.

4. **Secondary scan**: rho in {0.001, 0.002, 0.005, 0.010, 0.020, 0.050, 0.100, 0.200, 0.500}. Plot tau_min(rho) to identify the rho range where tau_min falls in [0.20, 0.40].

5. **Output**: `tier0-computation/s24a_vspec.py`, `s24a_vspec.npz` (tau, rho grid, V_spec, tau_min, V'', settling times), `s24a_vspec.png`.

**Runtime**: Under 1 minute. Under 40 lines of Python.

### Step 2: Intra-Sector Berry Curvature (P24-2)

**Background**: Berry identified (Session 23 Tesla-take, Eq. B-2) that intra-sector Berry curvature uses the SAME V_nm matrix elements as BCS but with different weighting: Berry curvature asks how sharply eigenstates rotate under tau evolution, where BCS asked about pairing strength. A peak near tau ~ 0.2-0.3 would indicate rapid structural change in the region of interest. The inter-sector Berry curvature is identically zero (from block-diagonality theorem, Session 22b).

**Formula**:
```
B_n(tau) = sum_{m != n} |V_nm(tau)|^2 / (E_n(tau) - E_m(tau))^2
```

where V_nm are Kosmann matrix elements from `s23a_kosmann_singlet.npz` and E_n are (0,0) singlet eigenvalues.

**Data**: `s23a_kosmann_singlet.npz` (V_nm, eigenvalues at 9 tau values).

**Procedure**:
1. Load V_nm(tau) and eigenvalues E_n(tau) for (0,0) singlet at all 9 tau values.
2. Compute B_n(tau) for n = 1, 2 (gap-edge modes) at all 9 tau values.
3. Plot B_1(tau), B_2(tau) vs tau on [0, 0.50].
4. Record peak magnitude and location.

**Expected**: Peak magnitude ~0.05, peak near tau ~ 0.2-0.3. Localization length ~9 sites (Berry's Anderson estimate: V~0.10, W~0.34, W/V~3.4).

**Output**: `s24a_berry.py`, `s24a_berry.npz`, `s24a_berry.png`. Under 15 lines. Under 30 seconds.

### Step 3: Neutrino R Diagnostic (P24-4)

**Background**: Neutrino (Session 23 Tesla-take) estimated R_tight-binding ~ (V_12/V_23)^2 ~ 25 from hopping amplitudes — within factor 1.3 of measured atmospheric-solar ratio R = 33.3. The proper computation requires diagonalizing H_eff = diag(eigenvalues) + V_nm and extracting the three smallest eigenvalues.

**Formula**:
```
H_eff = diag(lambda_1, ..., lambda_16) + V_nm(tau = 0.30)
```

**Procedure**:
1. Load eigenvalues E_n and V_nm at tau = 0.30 from `s23a_kosmann_singlet.npz`.
2. Construct H_eff = diag(E) + V_nm.
3. Diagonalize. Extract three smallest |eigenvalues|: m_1 < m_2 < m_3.
4. R = (m_3^2 - m_2^2) / (m_2^2 - m_1^2). Compare to 33.3.
5. Also compute: tan(2*theta_12) = 2*|H_12| / |H_11 - H_22| for lowest 2x2 block.
6. Repeat at tau = 0.15, 0.20, 0.25, 0.35 (sensitivity to tau_0 choice).

**Pre-registered gate**: R in [17, 66] = PASS (within factor 2). R outside [10, 100] = FAIL.

**Output**: `s24a_neutrino.py`, `s24a_neutrino.txt`. Under 25 lines. Milliseconds.

### Step 4: A/C Gauge-Gravity Consistency Check (P24-3)

**Background**: Session 23c (Section VIII) found that the a_2-dominated spectral action generates a zero-parameter prediction: tr(g_unit(tau_0)) = kappa^2 / (2*g_avg^2), where the (15/2) Baptista normalization cancels in the ratio. This check is independent of the f-dependence problem because f_8*Lambda^8 cancels. BF ~ 10 if passes.

**Known values**:
- tr(g_unit(0.30)) = 8.868 (from `s23c_AC_normalization.py`)
- g_unit(tau) = diag(e^{2tau}[x3], e^{-2tau}[x3], e^{tau}[x2]) — tr(g_unit(0)) = 8 = dim SU(3)
- kappa^2 = 8*pi*G_N, g_avg^2 = trace-averaged SM coupling at Lambda_KK

**Procedure**:
1. Compute tr(g_unit(tau)) at tau = 0.15, 0.20, 0.25, 0.30, 0.35.
2. Compute kappa^2/(2*g_avg^2) at two scale assumptions:
   - Lambda_KK = M_GUT = 2e16 GeV: g_3^2(M_GUT) ~ 0.5 (unified)
   - Lambda_KK = M_Pl = 1.22e19 GeV: g_3^2(M_Pl) ~ 0.4 (RGE estimated)
3. Report range of scale assumptions where check passes within factor 2.
4. Cross-check: g_1/g_2 = e^{-2tau} (Session 17a B-1 PROVEN) recovered from same formula.

**Pre-registered gate**: Consistent within factor 2 for reasonable scales = PASS (BF ~ 10). Inconsistent by factor > 5 for all scales = FAIL.

**Output**: Inline in synthesis (analytic check, no heavy computation).

### Step 5: Euclidean Action at Three Monopoles (P24-6)

**Background**: Hawking (Session 23 Tesla-take) proposed I_E(tau) = -V_spec(tau) * Vol(K) at monopoles M0 (tau=0, round), M1 (tau~0.10, first Jensen), M2 (tau~1.58, far Jensen). If I_E(M1) < I_E(M0), Jensen-deformed geometry dominates the internal-space path integral — a Hawking-Page analog for KK internal space.

**Cost**: Zero — uses V_spec data from Step 1.

**Procedure**:
1. From V_spec(tau; rho) at each rho, read off V_spec at tau = 0.00, 0.10, 1.58.
2. Compute Vol(K, tau) from the volume formula (Session 12: volume-preserving, so Vol = const).
3. I_E(tau) = -V_spec(tau) * Vol. Compare I_E(M1) vs I_E(M0) at all 5 rho values.

**Output**: Append to `s24a_vspec.npz` or inline.

### Step 6: Eigenvalue Ratio Map (P24-8)

**Background**: Paasch (Session 23 Tesla-take) proposed checking whether phi_paasch = 1.53158 organizes the eigenvalue ladder beyond the known (3,0)/(0,0) crossing at tau = 0.15.

**Procedure**:
1. Extract 16 eigenvalues of D_K in (0,0) singlet at 9 tau from `s23a_kosmann_singlet.npz`.
2. r_n(tau) = |lambda_{n+1}(tau)| / |lambda_n(tau)| for n = 1, ..., 15.
3. Mark ratios within 0.1% of phi_paasch = 1.53158.
4. Plot heatmap (n vs tau) with phi_paasch crossings highlighted.

**Output**: `s24a_eigenvalue_ratios.py`, `s24a_eigenvalue_ratios.npz`, `s24a_eigenvalue_ratios.png`. Under 30 lines.

### Step 7: Mandatory Gate Verdicts

Record ALL verdicts in `tier0-computation/s24a_gate_verdicts.txt`:

| Computation | Pre-Registered Threshold | Result | Gate Verdict |
|:------------|:-------------------------|:-------|:-------------|
| V_spec minimum location | tau_min in [0.20, 0.40] for any rho in [10^-3, 10^3] | [to fill] | PASS/CLOSED |
| V_spec monotone | No minimum for any rho | [to fill] | CLOSED if true |
| Berry curvature peak | Magnitude > 0.01, location near [0.15, 0.35] | [to fill] | diagnostic |
| Neutrino R | R in [17, 66] | [to fill] | PASS/FAIL |
| A/C consistency | Within factor 2 | [to fill] | PASS/FAIL |
| Euclidean I_E(M1) < I_E(M0) | At any rho with tau_min in [0.20, 0.40] | [to fill] | diagnostic |
| phi_paasch ratios | r_n = 1.53158 ± 0.1% at any (n, tau) | [to fill] | diagnostic |

---

# IV. PRE-REGISTERED Constraint GateS FOR P24

Classification must occur BEFORE interpretation. Report numbers first. Classify second. Interpret third.

## V-1: V_spec Monotone — CLOSED

**Condition**: V_spec(tau) monotonically decreasing or flat for ALL rho in [10^{-3}, 10^{3}] across [0, 2.0].
**Consequence**: No spectral action minimum. Curvature-squared terms cannot balance the linear term. Framework → ~5%/3% (panel/Sagan). Session 24c: Endgame branch.
**Probability of firing**: ~40% (R^2 term grows as R^2 ~ e^{4tau}; should dominate for large tau, so minimum likely exists at some rho — but whether that rho is physically motivated is the question).

## V-2: V_spec Minimum Outside Physical Window — MARGINAL

**Condition**: V_spec has minimum, but tau_min NOT in [0.20, 0.40] for any rho in [10^{-3}, 10^{1}].
**Consequence**: Stabilization exists at wrong tau. Does not reproduce Weinberg angle. BF ~ 1.
**Probability of firing**: ~25%.

## V-3: V_spec Minimum in [0.20, 0.40] — PASS

**Condition**: tau_min in [0.20, 0.40] for some rho in [10^{-3}, 10^{1}].
**Consequence**: Spectral action potential stabilizes in the physical window. Starobinsky mechanism on internal space. BF ~ 5-15 (one free parameter rho; full BF conditional on NCG constraining rho).
**Tier upgrade**: tau_min in [0.25, 0.35] AND V_spec''(tau_min) > 0 (stable): BF → 8-15.

## R-1: Neutrino R in [17, 66] — PASS (Gate Reopens)

**Condition**: R = (m_3^2 - m_2^2)/(m_2^2 - m_1^2) from H_eff diagonalization in [17, 66].
**Consequence**: Framework contacts neutrino oscillation data within factor 2. BF ~ 3-7.
**Note**: H_eff is not a literal neutrino mass matrix — it is the eigenvalue perturbation from Kosmann selection rules. BF reflects structural match, not direct derivation.

## AC-1: A/C Gauge-Gravity Inconsistency — FAIL

**Condition**: tr(g_unit(tau_0)) inconsistent with kappa^2/(2*g_avg^2) by factor > 5 for ALL reasonable scale assumptions.
**Consequence**: Gauge-gravity unification through SU(3) internal geometry fails at the consistency level. BF ~ 0.5. Not a decisive closure alone.

## Combined Gate (pre-registered from Session 23 master collab):

| Scenario | Panel posterior | Sagan posterior |
|:---------|:---------------|:----------------|
| V_spec minimum in [0.20, 0.40] | 20-30% | 8-12% |
| V_spec + R pass | 30-40% | 12-18% |
| V_spec + R + A/C all pass | 35-45% | 15-20% |
| V_spec + R + A/C + V'' > 0 stable | 40-50% | 18-25% |
| V_spec monotone (all fail) | 5-7% | 2-3% |

---

# V. PHASE 24b: PANEL REVIEW

## Triggering Condition

Phase 24b runs AFTER Phase 24a synthesis exists with all gate verdicts classified.

## Agents

| Agent | Role | Specific Responsibilities |
|:------|:-----|:-------------------------|
| sagan-empiricist | Sagan Standard verdict | Combined BF, pre-registration compliance, pattern independence, Venus Rule for V_spec |
| einstein-theorist | Physical interpretation | CC problem severity, modulus mass, settling time, EIH constraint, or permanent-result assessment if V_spec closes |
| coordinator | Synthesis writer + 24c branch assignment | Designated output writer. Receives verdicts from both. Assembles 24b synthesis. |

Only coordinator writes the final synthesis.

## Sagan's Responsibilities

1. **Pre-registration compliance**: All seven computations pre-registered before 24a. Gate thresholds in this document. No post-hoc accommodation.
2. **Venus Rule for V_spec**: V_spec was identified from 23c independently of BCS. But was it a prospective prediction or a post-hoc rescue? Sagan must state explicitly whether the V_spec gate carries the same evidential weight as the K-1e gate did.
3. **Pattern independence**: V_spec and R are largely independent (different physics). V_spec and A/C are NOT independent (same spectral geometry). Combined BF must account for correlations.
4. **Neutrino R adjudication**: Pre-registered window [17, 66] is generous. Is the H_eff construction genuine or dressed coincidence? State BF with justification.
5. **Baloney Detection Kit** (Sagan's own): If every failed mechanism is reinterpreted as confirming a new picture, the claim becomes unfalsifiable. V_spec must be tested against this concern.

## Einstein's Responsibilities

If V_spec passes:
1. **Modulus mass**: m_sigma^2 = V_spec''(tau_min). Convert to GeV using M_KK.
2. **Settling time**: T_settle = 2*pi / m_sigma. Compare to T_U ~ 4.4e17 s.
3. **CC problem severity**: V_spec(tau_min) / rho_Lambda_obs where rho_Lambda ~ 10^{-47} GeV^4. Fine-tuning ratio.
4. **EIH constraint**: Does V_spec'(tau_0) = 0 follow from 12D Bianchi identity?
5. **Landau d_eff=1 flag**: Compute Ginzburg criterion Gi ~ (T/V_barrier)^2. If Gi > 1, thermal fluctuations wash out minimum.

If V_spec closes:
1. Whether permanent results (KO-dim=6, SM quantum numbers, CPT, selection rules, R~25) constitute a publishable pure-NCG result independent of the cosmological program.
2. Minimal surviving claim set.

---

# VI. PHASE 24c (CONDITIONAL): TWO BRANCHES

## Branch A: Starobinsky Branch (V_spec minimum in [0.20, 0.40])

### Agents: landau-condensed-matter-theorist + einstein-theorist + coordinator

### Purpose
The minimum exists. Determine whether it survives d_eff=1 quantum/thermal fluctuations.

### Computation Steps

**A-1: Ginzburg Criterion (Landau)**
```
Gi = kT_KK / V_barrier
```
T_KK = M_KK / k_B (temperature at KK epoch). V_barrier = V_spec(0) - V_spec(tau_min).
Gate: Gi < 0.1 = survives. Gi > 1.0 = washed out.

**A-2: Zero-Point Fluctuation Energy**
```
E_ZPF = (1/2) * sqrt(V_spec''(tau_min))
```
If E_ZPF > V_barrier: quantum tunneling escapes minimum at T=0.

**A-3: Hubble Friction Assessment (Einstein)**
m_sigma vs H(T_KK). If m_sigma > H: modulus oscillates into minimum. If m_sigma << H: Hubble-frozen at random value.

**Output**: `sessions/YYYY-MM-DD-session-24c-starobinsky-synthesis.md`

## Branch B: Endgame Branch (V_spec monotone)

### Agents: sagan-empiricist + coordinator

### Purpose
V_spec is monotone. Starobinsky does not work. Assess whether any remaining rescue route has expected value > 1 and define the permanent achievement summary.

**Sagan**: Complete probability assessment. State the current framework probability and the maximum it could reach under any remaining rescue route. Identify whether P2b (finite-density, BF 5-15, P(success) ~ 10%) has EV > 1.

**Coordinator**: Write the permanent achievement summary: what survives K-1e + V-1. Raw material for the eventual pure-NCG publication.

**Output**: `sessions/YYYY-MM-DD-session-24c-endgame-synthesis.md`

---

# VII. OUTPUT FILES

## Phase 24a:

| File | Producer | Content |
|:-----|:---------|:--------|
| `tier0-computation/s24a_vspec.py` | phonon-sim | V_spec at 5 rho values + secondary scan |
| `tier0-computation/s24a_vspec.npz` | phonon-sim | Full V_spec data: tau, rho, V_spec, tau_min, V'', I_E |
| `tier0-computation/s24a_vspec.png` | phonon-sim | V_spec(tau) for 5 rho values with physical window shaded |
| `tier0-computation/s24a_berry.py` | phonon-sim | Intra-sector Berry curvature |
| `tier0-computation/s24a_berry.npz` | phonon-sim | B_n(tau) at 9 tau values |
| `tier0-computation/s24a_berry.png` | phonon-sim | Berry curvature vs tau |
| `tier0-computation/s24a_neutrino.py` | phonon-sim | H_eff diagonalization, R extraction |
| `tier0-computation/s24a_neutrino.txt` | phonon-sim | R value, mixing angle, gate verdict |
| `tier0-computation/s24a_eigenvalue_ratios.py` | phonon-sim | Eigenvalue ratio map |
| `tier0-computation/s24a_eigenvalue_ratios.npz` | phonon-sim | r_n(tau) at 9 tau values |
| `tier0-computation/s24a_eigenvalue_ratios.png` | phonon-sim | Ratio heatmap with phi_paasch marked |
| `tier0-computation/s24a_gate_verdicts.txt` | coordinator | All gate verdicts, classified in real time |
| `sessions/YYYY-MM-DD-session-24a-synthesis.md` | coordinator | Number-only gate summary |

## Phase 24b:

| File | Producer | Content |
|:-----|:---------|:--------|
| `sessions/YYYY-MM-DD-session-24b-synthesis.md` | coordinator | Panel synthesis with combined BF and branch assignment |
| `sessions/YYYY-MM-DD-session-24-sagan-verdict.md` | sagan | Full Sagan Standard verdict on gate battery |

## Phase 24c:

| File | Producer | Content |
|:-----|:---------|:--------|
| `sessions/YYYY-MM-DD-session-24c-[branch]-synthesis.md` | coordinator | Branch-specific synthesis + Session 25 definition |

---

# VIII. PRE-REGISTERED PROBABILITY SCENARIOS

All posteriors from post-Session-23 baselines: panel 8%, Sagan 5%.

| Outcome | Panel posterior | Sagan posterior | Path forward |
|:--------|:---------------|:----------------|:-------------|
| V_spec monotone (V-1 closes) | 5-7% | 2-3% | Endgame branch. P2b at BF 5-15 is last route. |
| V_spec minimum outside [0.20, 0.40] | 6-8% | 3-5% | Marginal. Reassess rho constraint from NCG. |
| V_spec minimum in [0.20, 0.40] only | 20-30% | 8-12% | Starobinsky branch. Ginzburg criterion is the gate. |
| V_spec in window + R passes | 30-40% | 12-18% | Two independent structural contacts. Framework alive. |
| V_spec + R + A/C all pass | 35-45% | 15-20% | Three convergent predictions. Near Level 3. |
| V_spec + R + A/C + V'' > 0 stable | 40-50% | 18-25% | Full structural suite. Session 25: thermal history. |

---

# IX. WHAT SESSION 24 IS REALLY ABOUT

The Session 23 arc closed the BCS mechanism — the last energetic stabilization route. But it also accidentally discovered something more interesting than the thing it closed: a tight-binding structure in the eigenvalue spectrum whose hopping ratios come within factor 1.3 of neutrino oscillation data, and a spectral action potential V_spec that nobody computed for 24 sessions, despite all the data existing since Session 20a.

Session 24 is about whether these accidental discoveries are genuine signals or numerical coincidences that collapse under scrutiny. The answer requires 20 lines of Python and 30 seconds of runtime for V_spec, 10 lines for Berry curvature, 20 lines for the neutrino R. If the computations take longer than 30 minutes in total, something has gone wrong.

The framework has been at 8% since K-1e. It peaked at 45-52% in Session 19d. The trajectory since has been a controlled descent with occasional plateaus. Session 24 is either the next step in that descent, or the beginning of a recovery. The probability distribution across the 15-agent review spans 5% (Sagan) to 20% (Hawking) — the widest range in the project's history — because nobody computed V_spec.

Twenty lines of Python settles a range of 5-20% down to a specific number. That is all Session 24 is.

If V_spec has a minimum near tau ~ 0.30, the Starobinsky mechanism applies to the internal space, the spectral action contains its own stabilization route, and the framework recovers to 20-40%. If V_spec is monotone, the framework is in its endgame, the mathematical achievements are permanent, and the cosmological program ends with two clean closes (BCS and Starobinsky).

Either outcome is more informative than 24 sessions of uncertainty. Run the computation. Honor the result.

---

*Session 24 master prompt drafted by gen-physicist. Pre-registered Constraint Gates and probability scenarios established from Session 23c synthesis (sessions/session-23/session-23c-synthesis.md) and Session 23 Tesla-take master collab (sessions/session-23/session-23-tesla-take-master-collab.md). All numerical values from Session 23 outputs. Agent roster respects the 2-3 agent maximum per sub-session (CLAUDE.md). Three-phase structure follows Session 23 model (computation → synthesis → conditional deep dive). Researcher index (researchers/index.md) cross-referenced for all agent-specific reading assignments.*

*"The framework has not earned the right to be believed. It has earned the right to have its potential computed."*
