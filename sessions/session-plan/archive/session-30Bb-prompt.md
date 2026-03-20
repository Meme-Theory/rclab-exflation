# Session 30Bb: Frozen-State Observables at the Off-Jensen Minimum

**Date**: TBD
**Author**: Baptista (baptista-spacetime-analyst), reviewed by QA (quantum-acoustics-theorist)
**Depends on**: Session 30Ba (minimum location $(\tau_{\min}, \epsilon_{\min})$ and grid eigenvalue data). Cannot proceed until 30Ba delivers `s30b_grid_bcs.npz` with confirmed minimum.
**Prerequisite**: 30Ba P-30w verdict and minimum coordinates available. If B-30min FIRED in 30Ba (no minimum), Step 6 (T1 extension) runs first.
**Input data**:
- `tier0-computation/s30b_grid_bcs.npz` (from 30Ba — minimum location, grid eigenvalues)
- `tier0-computation/s30b_sdw_grid.npz` (from 30Ba — Seeley-DeWitt landscape)
- `tier0-computation/s30b_5d_stability.npz` (from 30Ba — T3/T4 stability)
- `tier0-computation/tier1_dirac_spectrum.py` (generalized by 30Ba Step 0)
- `tier0-computation/s29b_pmns_extraction.npz` (PMNS tridiagonal extraction)
- Baptista Paper 17 eq 1.3-1.4: $[D_K, \mathcal{L}_X]$ formula for gauge boson masses
- Baptista Paper 18 eq 7.5: Dimensional reduction D_F = mass matrix from KK geometry

## Motivation

**The minimum exists. What does it predict?** Session 30Ba located the off-Jensen BCS minimum at $(\tau_{\min}, \epsilon_{\min})$ and evaluated the Weinberg angle (P-30w). Session 30Bb now extracts the full set of SM observables at that minimum — eigenvalue ratios, PMNS mixing angles, RGE running — and tests whether the framework derives the Standard Model from geometry with zero adjustable parameters.

At the minimum, every SM parameter is determined:

- $\sin^2(\theta_W)$ from $\lambda_2 / (\lambda_1 + \lambda_2)$ — **evaluated in 30Ba** (P-30w verdict available)
- $g_1/g_2$ from $\sqrt{\lambda_2/\lambda_1}$ — known from minimum coordinates
- $m_{(3,0)} / m_{(0,0)}$ eigenvalue ratio — tests P-30phi (S12 value 1.5316) and P-30golden ($\phi = 1.618$)
- PMNS mixing angles from the tridiagonal Kosmann kernel
- RGE-A: SM one-loop running of $g_1/g_2$ from $M_{\text{KK}}$ to $M_Z$

These are zero-parameter derivations. They either match the Standard Model or they do not. There is no fitting.

---

# SESSION DASHBOARD

## Prerequisites (from 30Ba)

| ID | Requirement | Source | Status |
|:---|:-----------|:-------|:-------|
| PRE-1 | Minimum location $(\tau_{\min}, \epsilon_{\min})$ available | `s30b_grid_bcs.npz` | BLOCKED (awaiting 30Ba) |
| PRE-2 | P-30w verdict available | 30Ba gate verdicts | BLOCKED (awaiting 30Ba) |
| PRE-3 | 5D stability confirmed (T3/T4 positive) | `s30b_5d_stability.npz` | BLOCKED (awaiting 30Ba) |
| PRE-4 | Generalized Dirac code working | 30Ba Step 0 | BLOCKED (awaiting 30Ba) |

## Computation Steps

| Step | Description | Agent | ~Cost | Status |
|:-----|:-----------|:------|:------|:-------|
| 3 | Full Dirac spectrum at minimum ($N_{\max} = 6$) | phonon-sim | ~5-10 min | PENDING |
| 4 | RGE running + NCG-KK tension check | phonon-sim / einstein | analytic | PENDING |
| 5 | Diagnostics at minimum (level stats, AZ, DOS, sector composition) | phonon-sim | ~0 | PENDING |
| 5b | Order-one condition at minimum (contingent on P-30w PASS) | phonon-sim | ~5-10 min | PENDING |
| 6 | Grid extension to T1 direction (contingent on B-30min or boundary minimum) | phonon-sim | ~30-60 min | PENDING |

## Gate Verdicts — Existential

| ID | Condition | Status |
|:---|:----------|:-------|
| **P-30phi** | $m_{(3,0)}/m_{(0,0)} \in [1.52, 1.54]$ at minimum (definitive, $N_{\max} = 6$) | PENDING |
| **RGE-A** | $g_1/g_2$ runs to $\tan(\theta_W) = 0.553$ at $M_Z$ for some $M_{\text{KK}}$ | PENDING |

## Gate Verdicts — Hard Closes

| ID | Condition | Status |
|:---|:----------|:-------|
| B-30rge | RGE-A gives $\sin^2(\theta_W)(M_Z) < 0.15$ or $> 0.30$ for ALL $M_{\text{KK}} \in [10^{10}, 10^{18}]$ GeV | PENDING |
| B-30nck | NCG relation ($g_1 = g_2$ at $\Lambda_{\text{SA}}$) and KK relation ($g_1/g_2 = \sqrt{\lambda_2/\lambda_1}$) irreconcilable: $\Lambda_{\text{SA}}/M_{\text{KK}} \notin [10^{-3}, 10^3]$ | PENDING |

## Gate Verdicts — Positive Signals

| ID | Condition | Status |
|:---|:----------|:-------|
| P-30a | P-30w (from 30Ba) + P-30phi both PASS (Scenario A) | PENDING |
| P-30b | P-30w (from 30Ba) + RGE-A both PASS | PENDING |
| P-30pmns | $\sin^2(\theta_{13}) \in [0.015, 0.030]$ AND $\theta_{23} \in [40^\circ, 55^\circ]$ at minimum | PENDING |
| P-30golden | $m_{(3,0)}/m_{(0,0)} \in [1.610, 1.626]$ (golden ratio $\phi$) | PENDING |

## Gate Verdicts — Diagnostics

| ID | Condition | Status |
|:---|:----------|:-------|
| AZ-1 | AZ class = BDI (unchanged from Jensen) | PENDING |
| AZ-1' | AZ class $\neq$ BDI → Pfaffian invariant changes, **flag to 30A** | PENDING |
| OO-1 | Order-one violation at minimum (contingent on P-30w PASS) | PENDING |
| DOS-1 | DOS at minimum $>$ DOS at Jensen (final, from $N_{\max} = 6$ data) | PENDING |

## Deliverables

| Output | Step | Status |
|:-------|:-----|:-------|
| `s30b_minimum_spectrum.npz` | 3 | PENDING |
| `s30b_rge_running.npz` / `.py` | 4 | PENDING |
| `s30b_3d_grid.npz` (contingent) | 6 | PENDING |
| `s30b_gate_verdicts.txt` | all | PENDING |

---

# 0. OPERATIONAL RULES

## COMPUTATION DISCIPLINE

Every result classified against its pre-registered gate BEFORE any interpretation. Report the number first. Classify second. Interpret third.

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s30b_`

## PRE-SESSION GATE CHECK (MANDATORY FIRST ACTION)

Before any computation, verify:
1. Read 30Ba gate verdicts — confirm minimum found (B-30min did NOT fire)
2. Read `tier0-computation/s30b_grid_bcs.npz` — extract $(\tau_{\min}, \epsilon_{\min})$ and corresponding $(\lambda_1, \lambda_2, \lambda_3)$
3. Read P-30w verdict from 30Ba — note $\sin^2(\theta_W)$ at minimum
4. Confirm generalized Dirac code works at $N_{\max} = 6$ (30Ba Step 0 validated at $N_{\max} = 3$; higher sectors have larger representation dimensions)

If 30Ba has not completed, **this session does not proceed**.

## COMPLETION SIGNAL

Session ends ONLY when user approves shutdown explicitly. Idle agents are not finished agents.

---

# I. REQUIRED READING

## ALL agents (MANDATORY):

1. **Session 30Ba outputs**: `tier0-computation/s30b_grid_bcs.npz`, `s30b_sdw_grid.npz`, `s30b_5d_stability.npz` — minimum location, landscape, stability
2. **Session 30Ba gate verdicts**: `tier0-computation/s30b_gate_verdicts.txt` — P-30w, B-30min, B-30w, B-30phi (preliminary)
3. **Session 29 Fusion Synthesis Section IX**: `sessions/session-29/session-29-fusion-synthesis.md` — Priority Stack, Scenario Tree (A/B/C)
4. **Session 29Bb Synthesis**: `sessions/session-29/session-29Bb-synthesis.md` — Jensen saddle analysis, T1/T2 eigenvectors
5. **Session 29Ba Synthesis**: `sessions/session-29/session-29ba-synthesis.md` — 3-sector F_BCS, PMNS extraction
6. **Session 28 Fusion Synthesis Section I**: `sessions/session-28/session-28-fusion-synthesis.md` — Four structural walls, BCS
7. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## Agent-specific required reading:

| Agent | Additional Reading |
|:------|:-------------------|
| phonon-exflation-sim | `tier0-computation/tier1_dirac_spectrum.py` (generalized code from 30Ba), `tier0-computation/s29b_pmns_extraction.py` (PMNS tridiagonal extraction to adapt) |
| einstein-theorist | Connes Papers 07, 10 (spectral action coefficients, GUT-scale coupling relations). Session 29 Connes Excursion. Assess NCG-KK coupling tension (XS-2) at the off-Jensen minimum. |
| baptista-spacetime-analyst | `researchers/Baptista/` — Paper 15 Section 3.5-3.7, Paper 17 eq 1.3-1.4, Paper 18 Section 6-7 (mass mixing, CKM/PMNS). Validate the off-Jensen Dirac spectrum against Baptista's geometric expectations. |
| coordinator | This prompt Section IV (gate conditions). Memorize ALL thresholds before first computation completes. |

---

# II. THEORETICAL CONTEXT (BRIEF RECAP)

Full theoretical context is in Session 30Ba prompt Section II. Key facts for this session:

- **U(2)-invariant metric**: $g = \lambda_1 g_0|_{\mathfrak{u}(1)} + \lambda_2 g_0|_{\mathfrak{su}(2)} + \lambda_3 g_0|_{\mathbb{C}^2}$
- **Minimum location**: $(\tau_{\min}, \epsilon_{\min})$ from 30Ba, giving specific $(\lambda_1, \lambda_2, \lambda_3)$ values
- **Gauge couplings**: $g_1/g_2 = \sqrt{\lambda_2/\lambda_1}$, $\sin^2(\theta_W) = \lambda_2/(\lambda_1 + \lambda_2)$
- **AZ class**: BDI with $T^2 = +1$ on Jensen (algebraic, should survive off-Jensen but must be verified — Step 5, AZ-1)
- **Topological classification**: BDI topology $\to$ Pfaffian invariant $\in \mathbb{Z}$ (if AZ-1 holds) or $\mathbb{Z}_2$ (if AZ-1' fires). **Must be established before 30A runs.**

### P-30phi Clarification

Session 12 found $m_{(3,0)}/m_{(0,0)} = 1.531580$ at $\tau = 0.15$ on the Jensen curve. This value is 5.3% below the golden ratio $\phi = 1.618034$. The ratio varies with $\tau$ and $\epsilon$ — it is NOT a constant. Whether it approaches $\phi$ at the off-Jensen minimum is an open question.

**P-30phi** (the existential gate) tests whether the S12 value (1.5316) is structurally stable — does it survive at the physical minimum, or is it an accident of $\tau = 0.15$? The window $[1.52, 1.54]$ is a 1.3% band around the S12 value.

**P-30golden** (a positive signal) tests whether the ratio matches $\phi$ itself. This is a stronger claim — it would mean the BCS minimum selects a geometry where the mass ratio is exactly the golden ratio. The window $[1.610, 1.626]$ is a 1% band around $\phi$.

These test different physical hypotheses. Both are reported. Neither is conflated with the other.

---

# II-b. OBSERVATIONS OF OPPORTUNITY (OoO)

**OoO** = **Observations of Opportunity**. These are "nice to have" diagnostics — NOT required for gate verdicts, do NOT block session progress. Tracked separately.

| OoO ID | Step | Description | Status |
|:-------|:-----|:------------|:-------|
| OoO-3b | 3 | Pull NuFIT PMNS angles, $\Delta m^2$, quark mass ratios via VizieR `B/pdg`; R-1 J-parity check; Poisson→GOE level statistics transition | PENDING |
| OoO-4b | 4 | Pull PDG $\alpha_i(M_Z)$; Super-K proton lifetime bound; NCG-KK heavy-fermion analog ($T_K \sim T_{\text{RKKY}}$) | PENDING |
| OoO-5b | 5 | AZ class algebraic survival off-Jensen; sector composition = MgB$_2$ $\sigma$/$\pi$ analog; iron pnictide $s_\pm$ precedent | PENDING |
| OoO-5b' | 5b | He-3-B emergent gauge symmetry (Volovik); Anderson's theorem analog for order-one condition | PENDING |
| OoO-6b | 6 | Pomeranchuk volume change analog (UGe$_2$/URhGe/UTe$_2$); pull $G_N$, LLR $|\dot{G}/G|$ bound via VizieR `B/pdg` | PENDING |

---

# III. COMPUTATION PLAN

## Step 3: Full Dirac Spectrum at the Minimum

**Fusion Priority**: 2 (Session 29 Fusion Section IX.2)
**Cost**: ~5-10 minutes at `max_pq_sum = 6` for a single point

**What**: At the minimum $(\tau_{\min}, \epsilon_{\min})$ identified in 30Ba Step 2, compute the full Dirac spectrum to high truncation order. This gives:

1. **$\phi_{\text{paasch}}$**: $m_{(3,0)}/m_{(0,0)}$ eigenvalue ratio (P-30phi gate)
2. **$\sin^2(\theta_W)$**: from $\lambda_2/(\lambda_1 + \lambda_2)$ at the minimum (P-30w cross-check with 30Ba)
3. **PMNS angles**: tridiagonal Kosmann kernel extraction at the minimum (upgrade P-29b from CONDITIONAL)
4. **Full eigenvalue spectrum**: level spacing statistics (Poisson vs GUE/GOE), avoided crossing census, Berry curvature diagnostic
5. **$F_{\text{BCS}}^{3\text{-sector}}$**: high-accuracy value at the minimum for gate classification

**Validation**: The generalized code from 30Ba Step 0 must work at `max_pq_sum = 6` (higher sectors include (6,0), (0,6), etc. with large representation dimensions). Verify that eigenvalue counts match expected dimensions before running the full computation.

**Key diagnostic**: Does the eigenvalue ratio $m_{(3,0)}/m_{(0,0)}$ persist at the BCS minimum? Session 12 found this ratio to be 1.531580 at $\tau = 0.15$ on the Jensen curve. The ratio varies with $\tau$ and $\epsilon$ — it is NOT a constant. P-30phi tests whether this value persists at the off-Jensen BCS minimum (structural invariance). P-30golden tests whether the ratio approaches $\phi = 1.618$ at the minimum (a stronger claim). The T-7 tension (Session 29 Fusion Section VIII) — whether P-30w and P-30phi can be satisfied simultaneously — is directly tested.

**Output**: `s30b_minimum_spectrum.npz` containing full eigenvalue list, eigenvectors, $\phi_{\text{paasch}}$, PMNS angles, level statistics.

**OoO**: Pull NuFIT PMNS angles ($\sin^2\theta_{12} = 0.303$, $\sin^2\theta_{23} = 0.572$, $\sin^2\theta_{13} = 0.02203$), $\Delta m^2$ values, quark mass ratios via VizieR `B/pdg`. R-1 neutrino ratio: J-protected Kramers degeneracy may keep R ~ 10$^{14}$ off-Jensen unless relevant eigenvalues are NOT J-paired — check J-parity subspace membership. Poisson→GOE level statistics transition would indicate V(gap,gap) = 0 selection rule may be lifted off-Jensen.

**Agent**: phonon-exflation-sim

## Step 4: RGE Running from the Minimum

**Fusion Priority**: 3 (Session 29 Fusion Section IX.2)
**Cost**: Zero (analytic, ~50 lines)

**What**: Take $g_1/g_2$ at the off-Jensen minimum (from 30Ba/Step 3) and run it down to $M_Z$ using standard one-loop SM beta functions:

$$\frac{1}{\alpha_i(M_Z)} = \frac{1}{\alpha_i(M_{\text{KK}})} + \frac{b_i}{2\pi} \ln\frac{M_{\text{KK}}}{M_Z}$$

with $b_1 = 41/10$, $b_2 = -19/6$, $b_3 = -7$ (SM one-loop). The ratio $\alpha_1/\alpha_2$ at $M_Z$ is measured: $\alpha_1/\alpha_2 = \sin^2(\theta_W)/\cos^2(\theta_W) = 0.2312/(1 - 0.2312) = 0.3006$.

**RGE-A (zero parameters)**: Does the KK-derived ratio $g_1/g_2 = \sqrt{\lambda_2/\lambda_1}$ at $M_{\text{KK}}$ run to the measured $\sin^2(\theta_W) = 0.2312$ at $M_Z$ for ANY choice of $M_{\text{KK}}$?

**RGE-B (one parameter, $M_{\text{KK}}$)**: Fix $M_{\text{KK}}$ such that Part A works. Do the individual couplings $g_1(M_Z)$, $g_2(M_Z)$ also match PDG values?

**NCG-KK tension check (XS-2 from Session 29 Fusion)**: Does the off-Jensen minimum reconcile the NCG relation $g_1 = g_2$ at cutoff $\Lambda_{\text{SA}}$ with the KK relation $g_1/g_2 = \sqrt{\lambda_2/\lambda_1}$? **Operational procedure**: Given $g_1/g_2$ at $M_{\text{KK}}$ from the off-Jensen minimum, run the SM one-loop beta functions UPWARD from $M_{\text{KK}}$. Find $\Lambda_{\text{SA}}$ = the scale where $\alpha_1(\Lambda_{\text{SA}}) = \alpha_2(\Lambda_{\text{SA}})$. If $g_1/g_2 < 1$ at $M_{\text{KK}}$ (as expected for $\lambda_2 < \lambda_1$), the running curves converge at some $\Lambda_{\text{SA}} > M_{\text{KK}}$. Report $\Lambda_{\text{SA}} / M_{\text{KK}}$:
- If $\Lambda_{\text{SA}} / M_{\text{KK}} \in [0.1, 10]$: tension mild (cutoff and compactification scale are of the same order)
- If $\Lambda_{\text{SA}} / M_{\text{KK}} \notin [10^{-3}, 10^3]$: B-30nck fires (irreconcilable)
- If $\Lambda_{\text{SA}}$ does not exist (running curves never cross): B-30nck fires

**Output**: `s30b_rge_running.npz` containing $\alpha_i(\mu)$ curves, $\sin^2(\theta_W)(M_Z)$ derived, $M_{\text{KK}}$ from Part B if Part A passes, $\Lambda_{\text{SA}}/M_{\text{KK}}$ ratio.

**OoO**: Pull PDG $\alpha_1(M_Z) = 0.01699$, $\alpha_2(M_Z) = 0.03376$, $\alpha_3(M_Z) = 0.1180$ via VizieR `B/pdg`. Pull Super-K proton lifetime bound $\tau_p(p \to e^+\pi^0) > 2.4 \times 10^{34}$ yr — if RGE-B determines $M_{\text{KK}}$, proton lifetime becomes a one-parameter prediction for Hyper-K (~2027). NCG-KK tension maps to two competing RG fixed points — $\Lambda_{\text{SA}}/M_{\text{KK}} \in [0.1, 10]$ is a smooth crossover (heavy-fermion $T_K \sim T_{\text{RKKY}}$ analog).

**Agent**: phonon-exflation-sim or einstein-theorist (analytic)

## Step 5: Diagnostics at the Minimum (Zero Marginal Cost)

**Fusion Priority**: 4-6 (Session 29 Fusion Section IX.2, Tier 2)
**Cost**: Zero (from Step 3 output)

From the full spectrum at the minimum, extract:

1. **Level statistics $P(s)$**: Nearest-neighbor spacing distribution. Poisson = integrable sector structure. GUE/GOE = quantum chaos. Diagnostic for off-Jensen symmetry breaking pattern.
2. **Avoided crossing census**: Count avoided crossings between eigenvalues of different sectors. If Berry curvature reappears off-Jensen (it was found to be B = 982.5 at $\tau = 0.10$ on Jensen), the frozen state may be a topological phase.
3. **Spectral gap $\lambda_{\min}(\tau_{\min}, \epsilon_{\min})$**: Is the gap at the BCS minimum larger, smaller, or equal to the Jensen-curve value? This determines the BCS depth margin.
4. **Sector composition**: Which Peter-Weyl sectors contribute the dominant eigenvalues near the gap edge? Does the sector structure change off-Jensen?
5. **AZ symmetry class off-Jensen**: On the Jensen curve, the BCS state is class BDI with $T^2 = +1$ (Session 17c). Off-Jensen, the residual symmetry is U(2), not U(1). Determine whether the symmetry class changes (e.g., BDI $\to$ DIII). If the class changes, the topological invariant shifts from $\mathbb{Z}$ to $\mathbb{Z}_2$, which directly affects the interpretation of the Session 30A Pfaffian computation. **This must be established before 30A runs.**
6. **DOS at band edge** $N(\lambda_{\min})$: Compare with Jensen-curve value. Quantifies the Pomeranchuk DOS enhancement (DOS-1 gate, final value from $N_{\max} = 6$ data).

**Output**: Diagnostics appended to `s30b_minimum_spectrum.npz`.

**OoO**: AZ class is algebraically determined ($T^2$, $C^2$ representation-theoretic) — BDI expected to survive, but topological invariant VALUE can change via gap closings. Sector composition near gap edge = orbital character analog (MgB$_2$ $\sigma$/$\pi$ bands). Avoided crossings between sectors = inter-band scattering — if gap $< 0.01\lambda_{\min}$, may affect BCS pairing symmetry (iron pnictide $s_\pm \to s_{++}$ precedent).

**Agent**: phonon-exflation-sim

## Step 5b (Contingent): Order-One Condition at the Minimum (OO-1)

**Fusion Priority**: 7 (Session 29 Fusion Section IX.2, Tier 3)
**Cost**: ~5-10 minutes at a single point
**Condition**: Runs after Step 3 delivers the minimum spectrum. Triggers if P-30w PASSES (from 30Ba) — otherwise the gauge sector is already wrong and OO-1 is moot.

**What**: Compute the order-one condition violation $\|[[D_K, a], b^o]\|$ for each factor pair $(A_i, A_j)$ at the off-Jensen minimum $(\tau_{\min}, \epsilon_{\min})$. On the Jensen curve at $\tau = 0.35$, the violations are (Session 28c, C-6):

- $(H, H)$: 4.000 (maximum)
- $(\mathbb{C}, H)$: 2.828
- $(\mathbb{C}, \mathbb{C})$: 2.000

**Gate**: If the violation DECREASES at the off-Jensen minimum (especially for the $(H,H)$ factor pair), this supports Connes' hypothesis (Session 29 Fusion VI.2) that BCS condensation improves the NCG axiom structure. If it INCREASES, the derived gauge group differs more from SM at the physical point.

**Why contingent**: The order-one condition determines whether the derived gauge group equals the SM gauge group $SU(3) \times SU(2) \times U(1)$. If it fails badly, P-30w passing is necessary but not sufficient — the correct Weinberg angle could emerge from a LARGER gauge group that happens to give the same ratio. This is the T-4 tension (Session 29 Fusion Section VIII).

**Output**: Order-one violation norms appended to `s30b_minimum_spectrum.npz`.

**OoO**: He-3-B emergent gauge symmetry (Volovik): BCS ground state can have HIGHER symmetry than single-particle Hamiltonian. If (H,H) violation decreases from 4.000, BCS is performing geometric symmetry restoration — Anderson's theorem analog.

**Agent**: phonon-exflation-sim or einstein-theorist

## Step 6 (Contingent): Grid Extension to T1 Direction

**Fusion Priority**: Extension of Priority 1
**Cost**: Medium (~30-60 minutes)
**Condition**: Only if 30Ba's 2D $(\tau, \epsilon)$ grid shows the minimum lies at the boundary of the $\epsilon$ range, or if B-30min fired (no minimum in 2D), suggesting the true minimum requires the T1 (breathing) direction as well.

**What**: Extend to a 3D grid search including T1 displacement. T1 breaks volume-preservation, so this probes whether the physical minimum is volume-preserving or not.

**Significance**: If the minimum is NOT volume-preserving, this is a new structural finding -- the physical vacuum selects a non-Einstein metric on the internal space. Volume-preservation was an assumption in the Jensen family (Paper 15, eq 3.68), not a dynamical requirement.

**Output**: `s30b_3d_grid.npz` if needed.

**OoO**: Pomeranchuk volume change analog — magnetostriction in UGe$_2$/URhGe/UTe$_2$, He-3 solid-liquid transition. If non-volume-preserving, pull $G_N = 6.674 \times 10^{-11}$ and LLR bound $|\dot{G}/G| < 1.4 \times 10^{-13}$ yr$^{-1}$ via VizieR `B/pdg` for consistency check.

---

# IV. CONSTRAINT CONDITIONS AND GATE STRUCTURE

## Existential Gates

| ID | Condition | Consequence |
|:---|:----------|:------------|
| **P-30phi** | $m_{(3,0)}/m_{(0,0)} \in [1.52, 1.54]$ at the off-Jensen minimum (definitive, $N_{\max} = 6$) | Eigenvalue ratio matches Session 12 value (1.531580) at the physical point. |
| **RGE-A** | $g_1/g_2$ at $M_{\text{KK}}$ runs to $\tan(\theta_W) = 0.553$ at $M_Z$ for some $M_{\text{KK}}$ | The KK-derived coupling ratio is consistent with SM running. Zero parameters. |

## Hard Closes

| ID | Condition | Consequence |
|:---|:----------|:------------|
| B-30rge | RGE-A gives $\sin^2(\theta_W)(M_Z) < 0.15$ or $> 0.30$ for ALL $M_{\text{KK}} \in [10^{10}, 10^{18}]$ GeV | KK coupling ratio incompatible with SM under any running. |
| B-30nck | NCG relation ($g_1 = g_2$ at $\Lambda_{\text{SA}}$) and KK relation ($g_1/g_2 = \sqrt{\lambda_2/\lambda_1}$) are irreconcilable: no $\Lambda_{\text{SA}}/M_{\text{KK}}$ ratio in $[10^{-3}, 10^3]$ makes both consistent | Internal inconsistency between NCG spectral action and KK dimensional reduction. This is the T-3 tension (Session 29 Fusion Section VIII) promoted to a hard close. |

## Positive Signals

| ID | Condition | Consequence |
|:---|:----------|:------------|
| P-30a | P-30w (from 30Ba) PASSES AND P-30phi PASSES | Both mass and mixing angle predictions work at the physical point. Scenario A from Session 29 Fusion. |
| P-30b | P-30w (from 30Ba) PASSES AND RGE-A PASSES | Framework derives the correct electroweak sector from geometry alone. |
| P-30pmns | $\sin^2(\theta_{13}) \in [0.015, 0.030]$ AND $\theta_{23} \in [40^\circ, 55^\circ]$ at the minimum | Full PMNS fit (upgrades P-29b from CONDITIONAL to PASS) |
| P-30golden | $m_{(3,0)}/m_{(0,0)} \in [1.610, 1.626]$ at the off-Jensen minimum | Eigenvalue ratio matches the golden ratio $\phi = 1.618$ at the physical point. Stronger than P-30phi (S12 value), would be a zero-parameter prediction. |

## Diagnostic Gates

| ID | Condition | Consequence |
|:---|:----------|:------------|
| AZ-1 | AZ symmetry class at off-Jensen minimum = BDI (unchanged from Jensen) | Pfaffian invariant remains $\mathbb{Z}$. Session 30A interpretation unchanged. |
| AZ-1' | AZ symmetry class at off-Jensen minimum $\neq$ BDI (e.g., DIII) | Pfaffian invariant changes to $\mathbb{Z}_2$. Session 30A must account for modified topological classification. **Flag to 30A before Pfaffian scan runs.** |
| OO-1 | Order-one violation DECREASES at minimum vs Jensen ($\tau = 0.35$) | BCS improves NCG axiom structure. Supports Connes' hypothesis. |
| DOS-1 | $N(E_F)$ at minimum $>$ $N(E_F)$ at Jensen ($\tau = 0.35$) | Confirms Pomeranchuk DOS mechanism. Final value from $N_{\max} = 6$ spectrum. |

## Diagnostic Outputs (Regardless of Gate Verdicts)

**Note on trapping marginality (T-2)**: The 20% sensitivity window on the energy multiplier $E_{\text{mult}}$ (Session 29 Fusion, T-2) is a dynamical question that 30B does not resolve. The grid search determines the STATIC landscape; the trapping dynamics depend on the modulus velocity at the BCS transition boundary, which requires the DNP launch energy distribution (deferred to 30C/beyond). 30B's results are valid regardless of trapping margin — if the minimum exists and has the correct SM parameters, the framework is viable. Whether the modulus REACHES that minimum is a separate question.

Even if all existential gates fail, the spectrum at the minimum produces:

1. **Full eigenvalue spectrum** — structural mathematics (JGP level)
2. **Level statistics transition** — Poisson-to-GOE as function of symmetry breaking
3. **Sector composition at gap edge** — which representations dominate near the band edge
4. **Berry curvature diagnostic** — topological character of the spectral flow

---

# V. NEW CODE INVENTORY

| Component | Lines | Description |
|:----------|:------|:------------|
| Full spectrum at minimum + diagnostics | ~50 | High-order Dirac, level stats, AZ class, avoided crossings |
| Order-one condition at minimum (OO-1, contingent) | ~40 | $\|[[D_K, a], b^o]\|$ for each factor pair at $(\tau_{\min}, \epsilon_{\min})$ |
| RGE running + NCG-KK tension check | ~60 | One-loop SM beta functions, ratio test, $\Lambda_{\text{SA}}/M_{\text{KK}}$ analysis |
| **Total new code** | **~150** | Core Dirac solver and grid code from 30Ba reused |

---

# VI. OUTPUT FILES

| Output | Contents |
|:-------|:---------|
| `s30b_minimum_spectrum.npz` | Full Dirac spectrum at minimum: eigenvalues, eigenvectors, $\phi_{\text{paasch}}$, PMNS, level stats, AZ class, avoided crossings, OO-1 norms |
| `s30b_rge_running.npz` | RGE curves: $\alpha_i(\mu)$ from $M_{\text{KK}}$ to $M_Z$, $\sin^2(\theta_W)(M_Z)$ derived, NCG-KK reconciliation analysis |
| `s30b_rge_running.py` | Step 4 script |
| `s30b_3d_grid.npz` | T1 extension (contingent on Step 6) |

Gate verdicts appended to: `tier0-computation/s30b_gate_verdicts.txt`

---

# VII. SUCCESS CRITERIA

Session 30Bb is successful if it produces:

1. **P-30phi verdict**: $m_{(3,0)}/m_{(0,0)}$ at the minimum, classified against $[1.52, 1.54]$ (S12 value). Also report P-30golden (against $[1.610, 1.626]$)
2. **RGE-A verdict**: Does $g_1/g_2$ at $M_{\text{KK}}$ run to the correct $\sin^2(\theta_W)$ at $M_Z$?
3. **B-30nck verdict**: Is the NCG-KK coupling tension reconcilable? $\Lambda_{\text{SA}}/M_{\text{KK}}$ ratio reported.
4. **PMNS at the minimum**: $\theta_{13}$, $\theta_{12}$, $\theta_{23}$ — does the off-Jensen minimum improve or worsen the theta_23 failure?
5. **Compound verdicts**: P-30a (P-30w + P-30phi), P-30b (P-30w + RGE-A) — scenario classification
6. **Diagnostic verdicts**: AZ-1, OO-1, DOS-1 (final) — all classified
7. **AZ class delivered to Session 30A**: Pfaffian interpretation depends on AZ class at the minimum. Must be established before 30A runs.
8. **OO-1 verdict** (contingent on P-30w PASS): Order-one violation at the minimum — better, worse, or unchanged from Jensen?

### Possible Outcomes and Probability Impact

| Outcome | Probability Impact |
|:--------|:------------------|
| **Scenario A**: P-30w (30Ba) + P-30phi + RGE-A all PASS | **30-45%** — framework derives SM from geometry. Paper preparation begins. |
| **Scenario B**: P-30w PASS, P-30phi FAIL (or vice versa) | **10-20%** — structural tension between requirements. Investigate trade-off. |
| **Scenario B'**: P-30w FAIL, P-30phi PASS | **8-15%** — gauge sector does not match. Investigate off-Jensen corrections in T1. |
| **Scenario C**: P-30w + P-30phi both FAIL | **3-5%** — structural floor (Kepler-solids). Framework closes with publishable math. |
| P-30pmns FIRES (full PMNS fit including theta_23) | Additional **+5-10%** to any scenario above |
| B-30min FIRES in 30Ba (no minimum found) | **No change below current** — must search 3D or full 5D space |

---

# VIII. AGENT ASSIGNMENTS

| Agent | Role |
|:------|:-----|
| **phonon-exflation-sim** | Primary computation: full spectrum at minimum (Step 3), diagnostics (Step 5), OO-1 (Step 5b) |
| **einstein-theorist** | RGE running (Step 4), NCG-KK coupling tension analysis, physical interpretation of Weinberg angle + phi results |
| **baptista-spacetime-analyst** | Geometry validation: off-Jensen Dirac spectrum against Papers 15/17/18, moduli space interpretation |
| **coordinator** | Context routing, gate tracking, scenario classification, handoff to 30A |

**Recommended team**: 3-4 agents. Einstein carries the RGE analysis. Phonon-sim does spectrum + diagnostics. Baptista validates geometry. Coordinator tracks gates and manages 30Bb → 30A handoff.

**Blast-first spawn workflow applies** (CLAUDE.md mandatory).

---

# IX. RELATIONSHIP TO SESSION 30A

**30Bb gates 30A.** The Pfaffian computation (30A) must run at the physical BCS minimum (coordinates from 30Ba) AND with the correct AZ class (from 30Bb Step 5). Without 30Bb's AZ-1 verdict, the Pfaffian result cannot be interpreted.

| | Session 30Ba | Session 30Bb | Session 30A |
|:---|:---|:---|:---|
| **Question** | Where is the minimum? | What SM parameters does it produce? | Does $D_{\text{total}}$ have a Pfaffian sign change? |
| **Type** | Landscape search | Quantitative extraction | Topological (binary, yes/no) |
| **Ceiling** | P-30w (Weinberg angle) | Framework viability (30-45% if Scenario A) | Level 4 prediction (20-40% if PASS) |
| **Input needed** | Session 29 data | **Minimum from 30Ba** | **Minimum from 30Ba + AZ class from 30Bb** |
| **Dependency** | Independent | Blocked until 30Ba | Blocked until 30Ba + 30Bb |

**Running order**: 30Ba → 30Bb → 30A. The 30A prerequisite steps (eigenvector extraction, Lie derivative) can proceed in parallel with 30B, but the actual Pfaffian scan (30A Step 5) requires both the minimum coordinates from 30Ba and the AZ class from 30Bb Step 5.

**Combined outcome**: If both 30A and 30Bb produce positive results (Pfaffian sign change AT the BCS minimum AND correct SM parameters), the framework probability would rise to 40-60% — the highest it has been since the project began.

---

# X. DEFERRED TO SESSION 30C (AND BEYOND)

The following computations were considered for 30B and deliberately deferred. They are valuable but not prerequisite for the existential gates.

| Item | Cost | Reason for Deferral | Source |
|:-----|:-----|:-------------------|:-------|
| Order-one condition FULL SCAN (OO-1 over full grid) | ~10 hr | Contingent single-point OO-1 is in 30Bb Step 5b. Full grid scan deferred. | Fusion VII.1 |
| D_BCS axiom verification (DBCS-1) | Medium | Requires BCS-modified Dirac operator construction. Exploratory. | Fusion VI.2 |
| Mode-dependent BCS dressing for PMNS | ~1 hr | Only relevant if P-30pmns fails (theta_23 still wrong at minimum) | Fusion VI.6 |
| Quantum metric on U(2)-invariant surface | ~1 hr | Berry curvature topological classification. Diagnostic. | Fusion VI.5 |
| Wodzicki residue for cosmological constant | Low | Theoretical development. Addresses T-6 (120-order CC discrepancy). | Fusion VI.3 |
| Spectral distance at frozen minimum | Medium | NCG-native "diameter" of internal space. | Fusion VI.4 |
| Phonon Boltzmann equation (time-resolved KC-3) | ~1 hr | Closes last gap in Constraint Chain physical story. Not urgent given KC-3 PASS. | QA S29 collab 3.4 |
| Acoustic impedance at BCS transition boundary | Medium | Trapping margin improvement. Downstream of minimum location. | QA S29 collab |
| DNP launch energy distribution | Medium | Resolves trapping margin (20% sensitivity window) | Fusion IX.4, Priority 14 |

**30C recommended scope**: OO-1 + DBCS-1 + mode-dependent PMNS dressing. These are the Tier 3 items from Fusion IX.2 that become actionable once 30Bb delivers the minimum analysis.

---

*Session 30Bb: Frozen-State Observables. Covers Session 29 Fusion Synthesis Priorities 2-3 (Tier 1) plus zero-cost Tier 2 diagnostics and contingent OO-1 from Tier 3. Depends on 30Ba minimum location. ~150 lines new code. ~15-20 min compute (Steps 3-5b). Two existential gates (P-30phi, RGE-A), two hard closes (B-30rge, B-30nck), four positive signals (P-30a, P-30b, P-30pmns, P-30golden), four diagnostics (AZ-1, OO-1, DOS-1 final). Scenario A (all PASS) → 30-45%. Scenario C (all FAIL) → 3-5%. AZ class must be established before 30A's Pfaffian scan runs.*
