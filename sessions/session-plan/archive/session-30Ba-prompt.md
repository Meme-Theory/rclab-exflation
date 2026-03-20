# Session 30Ba: U(2)-Invariant Grid Search — Minimum Location

**Date**: TBD
**Author**: Baptista (baptista-spacetime-analyst), reviewed by QA (quantum-acoustics-theorist)
**Depends on**: Session 29B complete. B-29d FIRED (Jensen saddle, 2/4 eigenvalues negative). The true BCS minimum lives in the U(2)-invariant family, not on the 1D Jensen curve.
**Prerequisite**: None beyond existing Session 29 data. All inputs in current `.npz` files.
**Delivers to**: Session 30Bb (minimum location, grid eigenvalue data), Session 30A (minimum location for Pfaffian scan)
**Input data**:
- `tier0-computation/tier1_dirac_spectrum.py` (core Dirac code)
- `tier0-computation/s29b_jensen_transverse.npz` (Jensen saddle verdict, B-29d)
- `tier0-computation/s29b_3sector_fbcs.npz` (3-sector free energy, B-29a)
- `tier0-computation/s29b_bogoliubov_bcs.npz` (Bogoliubov BCS gap)
- `tier0-computation/s29b_josephson_coupling.npz` (Josephson J_perp)
- Baptista Paper 15 eq 3.58-3.68: U(2)-invariant metric parameterization on SU(3)
- Baptista Paper 15 eq 3.79-3.80: Scalar curvature and V_eff on the moduli space

## Motivation

**The computational foundation for all frozen-state predictions.** The entire predictive content of the frozen-state program reduces to one question: what are the values of SM parameters at the off-Jensen BCS minimum? Before we can answer that question, we must find the minimum.

Session 29Bb established that the Jensen curve is a saddle (B-29d FIRES, eigenvalues $E_1 = -511{,}430$, $E_2 = -16{,}083$). Both unstable directions are U(2)-invariant. The true BCS minimum lives in the 3D U(2)-invariant family $g(\lambda_1, \lambda_2, \lambda_3)$, parametrized by the three scale factors on the decomposition

$$\mathfrak{su}(3) = \mathfrak{u}(1) \oplus \mathfrak{su}(2) \oplus \mathbb{C}^2$$

(Baptista Paper 15, eq 3.58). The Jensen subfamily is the 1D curve $(\lambda_1, \lambda_2, \lambda_3) = (e^{2\tau}, e^{-2\tau}, e^{\tau})$, which preserves the total volume $\lambda_1 \lambda_2^3 \lambda_3^4 = 1$. The instability directions (T1 breathing, T2 cross-block) move the modulus off this curve within the U(2)-invariant subspace.

Session 30Ba locates the true minimum of $V_{\text{total}}(\lambda_1, \lambda_2, \lambda_3) = S_{\text{spectral}} + F_{\text{BCS}}^{3\text{-sector}}$ on the 2D volume-preserving surface, confirms it with a Hessian check and 5D transverse stability, and delivers the minimum coordinates to 30Bb (SM parameter extraction) and 30A (Pfaffian computation).

---

# SESSION DASHBOARD

## Prerequisites

| ID | Requirement | Source | Status |
|:---|:-----------|:-------|:-------|
| PRE-1 | Session 29B complete, B-29d FIRED (Jensen saddle) | `s29b_gate_verdicts.txt` | CONFIRMED |
| PRE-2 | T1/T2 eigenvectors available | `s29b_jensen_transverse.npz` | CONFIRMED |
| PRE-3 | Dirac code generalized to $(\lambda_1, \lambda_2, \lambda_3)$ | Step 0 output | PENDING |

## Computation Steps

| Step | Description | Agent | ~Cost | Status |
|:-----|:-----------|:------|:------|:-------|
| 0 | Generalize Dirac code to U(2)-invariant metrics | phonon-sim | ~20 lines | PENDING |
| 1 | Seeley-DeWitt shortcut on 2D grid (441 pts) | phonon-sim | ~20 sec | PENDING |
| 2 | 3-sector BCS free energy on grid + locate minimum + 5D stability | phonon-sim | ~1-2 hr | PENDING |

## Gate Verdicts

| ID | Type | Condition | Status |
|:---|:-----|:----------|:-------|
| B-30min | Hard Close | $V_{\text{total}}$ has no minimum in 2D grid | PENDING |
| B-30w | Hard Close | $\sin^2(\theta_W)$ outside $[0.15, 0.30]$ everywhere on grid | PENDING |
| B-30phi | Hard Close | $m_{(3,0)}/m_{(0,0)}$ outside $[1.45, 1.65]$ everywhere on grid (preliminary, $N_{\max} = 3$) | PENDING |
| P-30w | Existential | $\sin^2(\theta_W) \in [0.20, 0.25]$ at minimum (from metric: $\lambda_2/(\lambda_1 + \lambda_2)$) | PENDING |
| P-30conv | Positive | SDW minimum location matches $V_{\text{total}}$ minimum $< 5\%$ | PENDING |
| DOS-1 | Diagnostic | $N(E_F)$ at minimum $>$ $N(E_F)$ at Jensen ($\tau = 0.35$) | PENDING |
| HM-1 | Diagnostic | Anderson-Higgs mode $m_H^2 > 0$ at minimum | PENDING |

## Deliverables

| Output | Step | Status |
|:-------|:-----|:-------|
| `s30b_sdw_grid.npz` / `.py` | 1 | PENDING |
| `s30b_grid_bcs.npz` / `.py` | 2 | PENDING |
| `s30b_5d_stability.npz` | 2 | PENDING |
| `s30b_landscape.png` | 2 | PENDING |
| `s30b_weinberg_contour.png` | 1-2 | PENDING |
| `s30b_phi_contour.png` | 2 | PENDING |
| `s30b_fbcs_landscape.png` | 2 | PENDING |
| `s30b_dos_landscape.png` | 2 | PENDING |
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
1. Read `tier0-computation/s29b_gate_verdicts.txt` -- confirm B-29d FIRED (Jensen saddle)
2. Read `tier0-computation/s29b_jensen_transverse.npz` -- confirm eigenvalues and eigenvectors available for T1, T2 directions
3. Confirm existing Dirac spectrum code (`tier1_dirac_spectrum.py`) can accept general U(2)-invariant metric parameters $(\lambda_1, \lambda_2, \lambda_3)$, not just Jensen $\tau$
4. If the Dirac code only accepts Jensen $\tau$, the FIRST computation is modifying it to accept general U(2)-invariant metrics (Step 0 below)

## COMPLETION SIGNAL

Session ends ONLY when user approves shutdown explicitly. Idle agents are not finished agents.

---

# I. REQUIRED READING

## ALL agents (MANDATORY):

1. **Session 29 Fusion Synthesis Section IX**: `sessions/session-29/session-29-fusion-synthesis.md` -- Priority Stack, Scenario Tree (A/B/C), Master Equation chain
2. **Session 29Bb Synthesis**: `sessions/session-29/session-29Bb-synthesis.md` -- Jensen saddle analysis, T1/T2 eigenvectors, U(2)-invariant parametrization
3. **Session 29Ba Synthesis**: `sessions/session-29/session-29ba-synthesis.md` -- 3-sector F_BCS, PMNS extraction, gradient balance
4. **Session 29 Wrapup**: `sessions/session-29/session-29-wrapup.md` -- Consolidated gate verdicts, physical picture, probability assessment
5. **Session 28 Fusion Synthesis Section I**: `sessions/session-28/session-28-fusion-synthesis.md` -- Four structural walls, BCS as the sole surviving mechanism
6. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## Agent-specific required reading:

| Agent | Additional Reading |
|:------|:-------------------|
| phonon-exflation-sim | `tier0-computation/tier1_dirac_spectrum.py` (Dirac code to generalize), `tier0-computation/s29b_3sector_fbcs.py` (3-sector F_BCS computation to extend), `tier0-computation/s29b_jensen_transverse.py` (transverse Hessian code with T1/T2 parametrization) |
| baptista-spacetime-analyst | `researchers/Baptista/` -- Paper 15 Section 3.5-3.7 (U(2)-invariant moduli space, scalar curvature, Lagrangian), Paper 17 eq 1.3-1.4 ($[D_K, \mathcal{L}_X]$). Validate the off-Jensen metric parameterization and scalar curvature formula. |
| coordinator | This prompt Section IV (gate conditions). Memorize ALL thresholds before first computation completes. |

---

# II. THEORETICAL CONTEXT

## The U(2)-Invariant Metric Family

The Lie algebra $\mathfrak{su}(3)$ decomposes under the adjoint action of U(2) as (Paper 15, eq 3.58):

$$\mathfrak{su}(3) = \mathfrak{u}(1) \oplus \mathfrak{su}(2) \oplus \mathbb{C}^2$$

with dimensions $1 + 3 + 4 = 8$. The most general U(2)-invariant metric on SU(3) is (Paper 15, eq 3.60-3.62):

$$g^{\wedge} = \lambda_1 \, g_0|_{\mathfrak{u}(1)} + \lambda_2 \, g_0|_{\mathfrak{su}(2)} + \lambda_3 \, g_0|_{\mathbb{C}^2}$$

This is a 3-parameter family. In the Gell-Mann basis $\{T_a\}_{a=1}^8$ with $\text{tr}(T_a T_b) = \frac{1}{2}\delta_{ab}$:

- $\lambda_1$ scales the $\mathfrak{u}(1)$ direction ($T_8$)
- $\lambda_2$ scales the $\mathfrak{su}(2)$ directions ($T_1, T_2, T_3$)
- $\lambda_3$ scales the $\mathbb{C}^2$ directions ($T_4, T_5, T_6, T_7$)

The metric is diagonal in the Gell-Mann basis: $g_{ab} = \lambda_{I(a)} \delta_{ab}$ where $I(a) \in \{1, 2, 3\}$ maps index $a$ to its subalgebra.

### Jensen Subfamily

The Jensen curve is the 1D subfamily (Paper 15, eq 3.68):

$$\lambda_1 = e^{2\tau}, \quad \lambda_2 = e^{-2\tau}, \quad \lambda_3 = e^{\tau}$$

This satisfies volume-preservation: $\lambda_1 \cdot \lambda_2^3 \cdot \lambda_3^4 = 1$. The volume-preserving constraint is a 2D surface within the 3D family.

### Off-Jensen Directions (from Session 29Bb)

The Session 29Bb transverse Hessian identified two U(2)-invariant transverse directions:

- **T1 (breathing)**: $\mathbf{t}_1 = (7, 11, 8)$ in $(\log\lambda_1, \log\lambda_2, \log\lambda_3)$ coordinates. Breaks volume-preservation. Eigenvalue $E_1 = -16{,}083$.
- **T2 (cross-block)**: $\mathbf{t}_2 = (-11, -7, 8)$ in log-$\lambda$ coordinates. Volume-preserving AND orthogonal to Jensen. Eigenvalue $E_2 = -511{,}430$.

T2 is the dominant instability. It increases $\lambda_3$ (C$^2$ directions) while decreasing $\lambda_1, \lambda_2$, pushing the gap-edge eigenvalues lower and deepening the BCS condensation energy.

**Weinberg angle convergence (from Session 29Bb)**: Moving along T2 changes $\log(\lambda_1/\lambda_2)$ at rate $-4\epsilon$, which shifts $\sin^2(\theta_W) = \lambda_2/(\lambda_1 + \lambda_2)$ toward the SM value 0.231 from the Jensen value 0.198 at $\tau = 0.35$. The required displacement is $\epsilon_{\text{T2}} \approx 0.049$ (small). BCS instability and electroweak mixing angle improvement align along T2.

### Scalar Curvature on the U(2)-Invariant Family

The scalar curvature is (Paper 15, eq 3.65):

$$R(\lambda_1, \lambda_2, \lambda_3) = \frac{1}{2\lambda_2} + \frac{1}{\lambda_3} - \frac{\lambda_2}{4\lambda_3^2} - \frac{\lambda_1}{2\lambda_3^2}$$

This is computable analytically at every grid point. The spectral action leading term $a_2 \propto R$ is therefore available without running the Dirac spectrum.

### Gauge Coupling Ratios Off-Jensen

From dimensional reduction of the higher-dimensional gauge field (Paper 15, Sections 3.6-3.7; Session 29Bb result):

$$\frac{g_1}{g_2} = \sqrt{\frac{\lambda_2}{\lambda_1}}, \qquad \sin^2(\theta_W) = \frac{\lambda_2}{\lambda_1 + \lambda_2}$$

These are zero-parameter predictions at the minimum. The RGE gate (Session 30Bb, Step 4) tests whether the ratio at $M_{\text{KK}}$ runs to the correct value at $M_Z$ under standard one-loop SM beta functions.

---

# II-b. OBSERVATIONS OF OPPORTUNITY (OoO)

**OoO** = **Observations of Opportunity**. These are "nice to have" diagnostics, cross-checks, and data pulls embedded within computation steps. They are NOT required for gate verdicts and do NOT block session progress. OoOs provide supplementary context — condensed matter analogs, PDG comparisons, convergence checks — that enrich interpretation but are strictly optional.

**Tracking**: OoOs are statused and tracked separately from the main gate structure (Section IV). An OoO that is skipped does not affect any gate verdict. An OoO that produces a surprising result may be promoted to a gate in a future session, but within this session it remains advisory.

| OoO ID | Step | Description | Status |
|:-------|:-----|:------------|:-------|
| OoO-0b | 0 | Isotropic-to-anisotropic BCS analog (He-3 A→B, Leggett 1975); validation $< 10^{-12}$ justification | PENDING |
| OoO-1b | 1 | Overlay PDG precision contours ($\sin^2\theta_W$, $\alpha_{\text{em}}$) on $(\tau, \epsilon)$ plane via VizieR `B/pdg`; SDW-Sommerfeld breakdown check | PENDING |
| OoO-2b | 2 | Pull DESI DR1/DR2 $w_0$-$w_a$ constraints; band-edge BCS analogs (SrTiO$_3$, TBG); Anderson-Higgs mode $m_H^2 \to 0$ check | PENDING |

---

# III. COMPUTATION PLAN

## Step 0: Generalize Dirac Code to U(2)-Invariant Metrics

**Status**: The existing `tier1_dirac_spectrum.py` parameterizes the metric by a single Jensen parameter $\tau$ via $(\lambda_1, \lambda_2, \lambda_3) = (e^{2\tau}, e^{-2\tau}, e^{\tau})$. Generalize to accept $(\lambda_1, \lambda_2, \lambda_3)$ directly.

**What changes**: The metric tensor construction in `dirac_operator_on_irrep()` must replace the Jensen parametrization with direct $\lambda_a$ scaling. The structure constants and Clifford algebra are basis-dependent, not metric-dependent -- only the metric tensor $g_{ab}$ and its inverse change. The spin connection $\omega_{abc}$ is recomputed from $g_{ab}$ and the structure constants $f^c_{ab}$.

**Scope**: ~15-20 lines modified. The function signature changes from `dirac_operator_on_irrep(p, q, s)` to `dirac_operator_on_irrep(p, q, lambdas)` where `lambdas = (L1, L2, L3)`. A wrapper preserves backward compatibility: `dirac_operator_on_irrep_jensen(p, q, tau)` calls the general version with Jensen parameters.

**Validation**: At $(\lambda_1, \lambda_2, \lambda_3) = (e^{2\tau}, e^{-2\tau}, e^{\tau})$ for $\tau = 0.15, 0.35$, the generalized code must reproduce the existing eigenvalues to machine epsilon ($< 10^{-12}$).

**OoO**: Isotropic-to-anisotropic BCS analog (He-3 A→B phase, Leggett 1975): anisotropy generically deepens condensation energy, consistent with Jensen being a saddle. Validation must be $< 10^{-12}$ because BCS gap equations are exponentially sensitive to eigenvalue errors near Fermi level.

**Agent**: phonon-exflation-sim

## Step 1: Seeley-DeWitt Shortcut on 2D Grid (Fast Landscape Scan)

**Fusion Priority**: 1 (Session 29 Fusion Section IX.1)
**Cost**: ~20 seconds for 400 grid points

**What**: Evaluate the Seeley-DeWitt heat kernel coefficients $a_0, a_2, a_4$ on a 20$\times$20 grid in the volume-preserving U(2)-invariant surface. This surface is 2D (3 parameters minus 1 volume constraint).

**Parameterization**: Use the Jensen parameter $\tau$ and the T2 displacement $\epsilon$ as coordinates:

$$\lambda_1(\tau, \epsilon) = e^{2\tau - 11\epsilon/N}, \quad \lambda_2(\tau, \epsilon) = e^{-2\tau - 7\epsilon/N}, \quad \lambda_3(\tau, \epsilon) = e^{\tau + 8\epsilon/N}$$

where $N = \sqrt{11^2 + 7^2 + 8^2} = \sqrt{234}$ normalizes T2. Volume constraint: $\lambda_1 \lambda_2^3 \lambda_3^4 = e^{(1 \cdot (-11) + 3 \cdot (-7) + 4 \cdot 8)\epsilon/N} = e^{0} = 1$ (exactly preserved, since $\mathbf{t}_2 \cdot \mathbf{n}_V = 0$ where $\mathbf{n}_V = (1, 3, 4)$ is the volume normal).

**Grid**: $\tau \in [0.0, 0.60]$ (21 points), $\epsilon \in [-0.15, 0.15]$ (21 points). Total: 441 points.

**At each grid point, compute**:
1. $R(\lambda_1, \lambda_2, \lambda_3)$ -- scalar curvature (analytic, eq 3.65)
2. $a_2 \propto R \cdot \text{Vol}$ -- leading spectral action term
3. $\sin^2(\theta_W) = \lambda_2/(\lambda_1 + \lambda_2)$ -- Weinberg angle
4. $g_1/g_2 = \sqrt{\lambda_2/\lambda_1}$ -- gauge coupling ratio
5. Volume $V = \lambda_1^{1/2} \lambda_2^{3/2} \lambda_3^2$ (should be $\approx 1$ on the constraint surface)

**Why this works**: The Seeley-DeWitt coefficients are polynomial in the curvature invariants of the metric. On a homogeneous space with left-invariant metric, these invariants are computable from the structure constants and $\lambda_a$ alone -- no eigenvalue computation needed. This gives a rapid landscape scan.

**Limitation**: The shortcut gives $a_0, a_2$ analytically but $a_4$ requires computing the Riemann tensor components and their contractions (Gilkey formula). For the U(2)-invariant family on SU(3), this is still analytic but involves more terms. The shortcut does NOT give individual eigenvalues, BCS gap, or PMNS angles -- those require Step 2.

**Output**: `s30b_sdw_grid.npz` containing the 2D arrays for $R$, $\sin^2(\theta_W)$, $g_1/g_2$, $a_2$, and the SDW-only minimum location.

**OoO**: Overlay PDG precision contours on the $(\tau, \epsilon)$ plane — $\sin^2\theta_W^{\text{lept}}_{\text{eff}} = 0.23122 \pm 0.00004$, $\alpha_{\text{em}}(M_Z) = 1/127.951$ via VizieR `B/pdg`. SDW shortcut is a Sommerfeld expansion analog — known to fail near van Hove singularities where BCS is strongest. If SDW minimum disagrees with full BCS minimum (Step 2) by more than one grid spacing, the shortcut is unreliable.

**Agent**: phonon-exflation-sim

## Step 2: 3-Sector BCS Free Energy on the Same Grid

**Fusion Priority**: Integral to Priority 1 (the minimum of $V_{\text{total}} = S_{\text{spectral}} + F_{\text{BCS}}$ requires both terms)
**Cost**: ~1-2 hours at `max_pq_sum = 3` for 441 grid points. With 3 sectors only: ~8.7s per point, ~64 min total. With all 10 sectors: ~2 hours total.

**What**: At each grid point $(\tau, \epsilon)$, compute the Dirac spectrum for ALL sectors with $p+q \leq 3$ (10 sectors total: (0,0), (1,0), (0,1), (2,0), (0,2), (1,1), (3,0), (0,3), (2,1), (1,2)) using the generalized code from Step 0. **Store eigenvalues for all sectors** — they are needed for the spectral action sum $S_{\text{spectral}}$, level statistics (30Bb Step 5), and as potential input to Session 30A. The BCS free energy uses only the 3 load-bearing sectors:

$$F_{\text{BCS}}^{3\text{-sector}}(\tau, \epsilon; \mu) = \sum_{r \in \{(0,0),(3,0),(0,3)\}} \text{mult}(r) \cdot F_{\text{cond}}^{(r)}(\tau, \epsilon; \mu)$$

with multiplicities 16, 100, 100. The self-consistent chemical potential $\mu = \lambda_{\min}$ (the smallest positive eigenvalue of $D_K$ at each grid point).

**Grid reduction**: If full 441-point grid is too expensive, first run Step 1 (Seeley-DeWitt, 20 sec) to identify the region of interest, then run the full Dirac spectrum on a reduced 10$\times$10 grid centered on the Seeley-DeWitt minimum. Cost: ~15 minutes.

**What to compute at each grid point** (store eigenvalues for ALL 10 sectors with $p+q \leq 3$; the BCS free energy uses only 3, but $S_{\text{spectral}}$ and 30Bb diagnostics require the full spectrum):
1. Dirac eigenvalues for ALL sectors with $p+q \leq 3$
2. $\lambda_{\min}$ (smallest positive eigenvalue)
3. $F_{\text{BCS}}^{3\text{-sector}}$ at $\mu = \lambda_{\min}$ and $\mu = 1.2 \lambda_{\min}$
4. BCS gap $\Delta/\lambda_{\min}$ for each sector
5. Spectral action leading contribution $S_{\text{spectral}}(\tau, \epsilon)$ from eigenvalue sum
6. **DOS at band edge** $N(E_F)$: count eigenvalues within $\delta E$ of $\lambda_{\min}$ (zero-cost from eigenvalue data). Confirms whether Pomeranchuk deepening is driven by DOS enhancement or trivial gap rescaling.
7. **Anderson-Higgs mode mass$^2$**: from Gaussian fluctuation analysis at each grid point (adapted from `s29b_gaussian_correction.py`). If $m_H^2 \to 0$ at any point on the grid, mean-field BCS breaks down there (quantum critical point). This is a zero-cost diagnostic from the BCS data.

**Locate the minimum**: Find $(\tau_{\min}, \epsilon_{\min})$ that minimizes $V_{\text{total}} = S_{\text{spectral}} + F_{\text{BCS}}^{3\text{-sector}}$. Verify it is a genuine minimum by computing the 2$\times$2 Hessian $\partial^2 V_{\text{total}} / \partial x_i \partial x_j$ (where $x = (\tau, \epsilon)$) via finite differences. **Both eigenvalues must be positive.** If either is negative, the minimum lies outside the volume-preserving surface and 30Bb Step 6 (T1 extension) is triggered.

**Full 5D stability check at the minimum**: Once the 2D minimum is found, check transverse stability in the U(2)-breaking directions (T3, T4). These had positive eigenvalues on Jensen ($E_3 = +219$, $E_4 = +1{,}775$) but must be reconfirmed at the off-Jensen point. Compute via finite differences: perturb $\lambda_a \to \lambda_a \cdot e^{\delta \cdot t_{3,a}}$ and $\lambda_a \to \lambda_a \cdot e^{\delta \cdot t_{4,a}}$ at the minimum and check $\delta^2 V_{\text{total}} > 0$.

**Output**: `s30b_grid_bcs.npz` containing the full 2D landscape of $V_{\text{total}}$, $F_{\text{BCS}}$, $\lambda_{\min}$, $\Delta/\lambda_{\min}$, $N(E_F)$, $m_H^2$, and the minimum location. `s30b_5d_stability.npz` containing T3/T4 transverse Hessian eigenvalues.

**OoO**: Pull DESI DR1/DR2 $w_0$-$w_a$ constraints (VizieR or literature) for w = -1 null prediction check. Band-edge BCS analog: SrTiO$_3$ (dilute SC), twisted bilayer graphene. $\Delta/\lambda_{\min} > 0.5$ signals strong-coupling BEC regime — mean-field qualitatively correct but quantitatively approximate. Anderson-Higgs mode observed in NbSe$_2$ — $m_H^2 \to 0$ marks quantum critical point where mean-field fails.

**Agent**: phonon-exflation-sim

---

# IV. CONSTRAINT CONDITIONS AND GATE STRUCTURE

## Hard Closes

| ID | Condition | Consequence |
|:---|:----------|:------------|
| B-30min | $V_{\text{total}}$ has NO minimum in the 2D grid (monotonic in both directions) | No BCS stabilization in U(2)-invariant family. Must search full 5D. Triggers 30Bb Step 6 (T1 extension). |
| B-30w | $\sin^2(\theta_W) < 0.15$ or $> 0.30$ at ALL $(\tau, \epsilon)$ in the grid | Electroweak mixing cannot be reproduced. Gauge sector fails. |
| B-30phi | $m_{(3,0)}/m_{(0,0)} < 1.45$ or $> 1.65$ at ALL $(\tau, \epsilon)$ in the grid | Eigenvalue ratio does not pass through the S12 value (1.5316) or the golden ratio (1.618) anywhere on the U(2)-invariant surface. Neither geometric target is accessible. **Preliminary** from $N_{\max} = 3$; definitive verdict from 30Bb Step 3 at $N_{\max} = 6$. |

## Existential Gate (Evaluated at Minimum)

| ID | Condition | Consequence |
|:---|:----------|:------------|
| **P-30w** | $\sin^2(\theta_W) \in [0.20, 0.25]$ at the off-Jensen minimum | Weinberg angle in the ballpark. Framework can produce correct electroweak mixing. **Evaluated from metric directly**: $\sin^2(\theta_W) = \lambda_2 / (\lambda_1 + \lambda_2)$ at $(\tau_{\min}, \epsilon_{\min})$. No Dirac spectrum needed. |

## Positive Signal

| ID | Condition | Consequence |
|:---|:----------|:------------|
| P-30conv | Seeley-DeWitt minimum location (Step 1) agrees with $V_{\text{total}}$ minimum location (Step 2) to $< 5\%$ in $(\tau, \epsilon)$ | Spectral shortcut validated. Enables rapid future scans. |

## Diagnostic Gates

| ID | Condition | Consequence |
|:---|:----------|:------------|
| DOS-1 | $N(E_F)$ at off-Jensen minimum $>$ $N(E_F)$ at Jensen ($\tau = 0.35$, $\epsilon = 0$) | Confirms Pomeranchuk DOS mechanism: BCS deepening is physical (more states at gap edge), not just trivial rescaling of $\lambda_{\min}$. |
| HM-1 | Anderson-Higgs mode $m_H^2 > 0$ at the minimum | Mean-field BCS valid at the physical point. No quantum critical point. |
| HM-1' | $m_H^2 \leq 0$ at or near the minimum | Quantum critical point. Mean-field breaks down. BCS results at the minimum are unreliable. |

## Handoff to 30Bb

Upon Step 2 completion, deliver to Session 30Bb:
1. **Minimum location** $(\tau_{\min}, \epsilon_{\min})$ and corresponding $(\lambda_1, \lambda_2, \lambda_3)$
2. **P-30w verdict** (sin²θ_W at minimum)
3. **Grid eigenvalue data** (`s30b_grid_bcs.npz`) for 30Bb diagnostic use
4. **5D stability verdict** (T3/T4 eigenvalues at minimum)
5. **B-30min, B-30w, B-30phi (preliminary)** verdicts

If **B-30min FIRES** (no minimum), 30Bb Step 6 (T1 extension) is triggered before Steps 3-5.

---

# V. NEW CODE INVENTORY

| Component | Lines | Description |
|:----------|:------|:------------|
| U(2)-invariant metric generalization in `dirac_operator_on_irrep()` | ~20 | Replace Jensen $\tau$ with $(\lambda_1, \lambda_2, \lambda_3)$ |
| Jensen backward-compatibility wrapper | ~5 | `dirac_operator_on_irrep_jensen(p, q, tau)` |
| Seeley-DeWitt shortcut: $R(\lambda_1, \lambda_2, \lambda_3)$ | ~30 | Analytic scalar curvature on U(2)-invariant family |
| 2D grid scan driver | ~80 | Loop over $(\tau, \epsilon)$, compute $R$, $\sin^2(\theta_W)$, $g_1/g_2$ |
| 3-sector BCS on grid (extending s29b_3sector_fbcs.py) | ~80 | F_BCS + DOS + Higgs mode at each grid point, locate minimum |
| Full 5D stability check at minimum | ~30 | T3/T4 transverse Hessian at off-Jensen point |
| Plotting (landscape, contours) | ~60 | Heatmaps of $V_{\text{total}}$, $\sin^2(\theta_W)$, $\phi_{\text{paasch}}$, DOS, F_BCS |
| **Total new code** | **~305** | Core Dirac solver reused; grid scan and visualization are new |

---

# VI. OUTPUT FILES

| Output | Contents |
|:-------|:---------|
| `s30b_sdw_grid.npz` | Seeley-DeWitt landscape: $R$, $a_2$, $\sin^2(\theta_W)$, $g_1/g_2$ over 441 grid points |
| `s30b_sdw_grid.py` | Step 1 script |
| `s30b_grid_bcs.npz` | Full $V_{\text{total}}$ landscape: $F_{\text{BCS}}^{3\text{-sector}}$, $S_{\text{spectral}}$, $\lambda_{\min}$, $\Delta/\lambda_{\min}$, $N(E_F)$, $m_H^2$, minimum location, eigenvalue ratios over grid |
| `s30b_grid_bcs.py` | Step 2 script |
| `s30b_5d_stability.npz` | T3/T4 transverse Hessian eigenvalues at the off-Jensen minimum |
| `s30b_landscape.png` | Heatmap of $V_{\text{total}}(\tau, \epsilon)$ with minimum marked |
| `s30b_weinberg_contour.png` | Contour of $\sin^2(\theta_W) = 0.231$ on the $(\tau, \epsilon)$ plane |
| `s30b_phi_contour.png` | Contours of $m_{(3,0)}/m_{(0,0)} = 1.5316$ (S12 value) and $= 1.618$ ($\phi$) on the $(\tau, \epsilon)$ plane |
| `s30b_fbcs_landscape.png` | Heatmap of $F_{\text{BCS}}^{3\text{-sector}}$ alone (without spectral action) on the $(\tau, \epsilon)$ grid |
| `s30b_dos_landscape.png` | Heatmap of $N(E_F)$ across the $(\tau, \epsilon)$ grid |

Gate verdicts appended to: `tier0-computation/s30b_gate_verdicts.txt`

---

# VII. SUCCESS CRITERIA

Session 30Ba is successful if it produces:

1. **A definitive minimum verdict** (B-30min): does $V_{\text{total}}$ have a minimum in the 2D $(\tau, \epsilon)$ grid?
2. **If minimum found**: location $(\tau_{\min}, \epsilon_{\min})$ with Hessian confirmation (both eigenvalues positive), and T3/T4 stability confirmed
3. **P-30w verdict**: $\sin^2(\theta_W)$ at the minimum, classified against $[0.20, 0.25]$
4. **Grid-wide hard close verdicts**: B-30w and B-30phi (preliminary)
5. **Full $V_{\text{total}}$ landscape** and visualization PNGs
6. **Minimum coordinates delivered to 30Bb and 30A**

---

# VIII. AGENT ASSIGNMENTS

| Agent | Role |
|:------|:-----|
| **phonon-exflation-sim** | Primary computation: code generalization (Step 0), Seeley-DeWitt grid (Step 1), BCS grid + minimum + stability (Step 2) |
| **baptista-spacetime-analyst** | Geometry validation: U(2)-invariant metric formulas against Paper 15, scalar curvature cross-check, off-Jensen gauge coupling derivation |
| **coordinator** | Context routing, gate tracking, handoff to 30Bb |

**Recommended team**: 2-3 agents. The phonon-sim agent carries the full computational load. Baptista validates the geometry. Coordinator tracks gates and manages the 30Ba → 30Bb handoff.

**Blast-first spawn workflow applies** (CLAUDE.md mandatory).

---

# IX. RELATIONSHIP TO 30Bb AND 30A

**30Ba gates 30Bb.** Session 30Bb (SM parameter extraction, RGE running, diagnostics) requires the minimum location from 30Ba Step 2. Without the minimum coordinates, 30Bb Steps 3-5 have no input geometry. This is a hard dependency.

**30Ba gates 30A.** Session 30A (D_total Pfaffian) requires the minimum location from 30Ba Step 2. Additionally, 30Bb Step 5 (AZ class verification) must complete before 30A's Pfaffian scan runs, since the AZ class determines whether the topological invariant is $\mathbb{Z}$ or $\mathbb{Z}_2$.

| | Session 30Ba | Session 30Bb | Session 30A |
|:---|:---|:---|:---|
| **Question** | Where is the minimum? | What SM parameters does it produce? | Does D_total have a Pfaffian sign change? |
| **Type** | Landscape search | Quantitative extraction | Topological (binary) |
| **Dependency** | Independent | **BLOCKED until 30Ba** | **BLOCKED until 30Ba + 30Bb AZ-1** |

---

*Session 30Ba: U(2)-Invariant Grid Search. Covers Session 29 Fusion Synthesis Priority 1 (Tier 1): locate the off-Jensen BCS minimum. ~305 lines new code. ~1-2 hours total compute time. Three hard closes (B-30min, B-30w, B-30phi), one existential gate (P-30w), one positive signal (P-30conv), two diagnostics (DOS-1, HM-1). Delivers the minimum location that gates both 30Bb and 30A.*
