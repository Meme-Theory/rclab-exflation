# Session 30B: The Decisive Grid — U(2)-Invariant Minimum and Frozen-State Observables

**Date**: TBD
**Author**: Baptista (baptista-spacetime-analyst), reviewed by QA (quantum-acoustics-theorist)
**Depends on**: Session 29B complete. B-29d FIRED (Jensen saddle, 2/4 eigenvalues negative). The true BCS minimum lives in the U(2)-invariant family, not on the 1D Jensen curve.
**Prerequisite**: None beyond existing Session 29 data. All inputs in current `.npz` files.
**Input data**:
- `tier0-computation/tier1_dirac_spectrum.py` (core Dirac code)
- `tier0-computation/s29b_jensen_transverse.npz` (Jensen saddle verdict, B-29d)
- `tier0-computation/s29b_3sector_fbcs.npz` (3-sector free energy, B-29a)
- `tier0-computation/s29b_bogoliubov_bcs.npz` (Bogoliubov BCS gap)
- `tier0-computation/s29b_josephson_coupling.npz` (Josephson J_perp)
- `tier0-computation/s29b_pmns_extraction.npz` (PMNS tridiagonal extraction)
- Baptista Paper 15 eq 3.58-3.68: U(2)-invariant metric parameterization on SU(3)
- Baptista Paper 15 eq 3.79-3.80: Scalar curvature and V_eff on the moduli space
- Baptista Paper 17 eq 1.3-1.4: $[D_K, \mathcal{L}_X]$ formula for gauge boson masses
- Baptista Paper 18 eq 7.5: Dimensional reduction D_F = mass matrix from KK geometry

## Motivation

**The single most important computation for observational contact.** The entire predictive content of the frozen-state program reduces to one question: what are the values of SM parameters at the off-Jensen BCS minimum?

Session 29Bb established that the Jensen curve is a saddle (B-29d FIRES, eigenvalues $E_1 = -511{,}430$, $E_2 = -16{,}083$). Both unstable directions are U(2)-invariant. The true BCS minimum lives in the 3D U(2)-invariant family $g(\lambda_1, \lambda_2, \lambda_3)$, parametrized by the three scale factors on the decomposition

$$\mathfrak{su}(3) = \mathfrak{u}(1) \oplus \mathfrak{su}(2) \oplus \mathbb{C}^2$$

(Baptista Paper 15, eq 3.58). The Jensen subfamily is the 1D curve $(\lambda_1, \lambda_2, \lambda_3) = (e^{2\tau}, e^{-2\tau}, e^{\tau})$, which preserves the total volume $\lambda_1 \lambda_2^3 \lambda_3^4 = 1$. The instability directions (T1 breathing, T2 cross-block) move the modulus off this curve within the U(2)-invariant subspace.

The grid search locates the true minimum of $V_{\text{total}}(\lambda_1, \lambda_2, \lambda_3) = S_{\text{spectral}} + F_{\text{BCS}}^{3\text{-sector}}$ in this 3D space. At that minimum, every SM parameter is determined with zero adjustable parameters:

- $\sin^2(\theta_W)$ from $\lambda_2 / (\lambda_1 + \lambda_2)$ (off-Jensen generalization of $e^{-2\tau}$)
- $g_1/g_2$ from $\sqrt{\lambda_2/\lambda_1}$ (gauge coupling ratio at KK scale)
- $m_{(3,0)} / m_{(0,0)}$ eigenvalue ratio from the Dirac spectrum (tests P-30phi at S12 value 1.5316 and P-30golden at $\phi = 1.618$)
- PMNS mixing angles from the tridiagonal Kosmann kernel at the minimum
- RGE-A: SM one-loop running of $g_1/g_2$ from $M_{\text{KK}}$ to $M_Z$

These are zero-parameter derivations. They either match the Standard Model or they do not. There is no fitting.

### Why This Is Session 30B (Not 30A)

Session 30A is the D_total Pfaffian computation (deferred since Session 18) -- the highest-ceiling topological test. Session 30B is the highest-impact quantitative test: it converts the entire frozen-state prediction program from "in principle derivable" to "derived numbers versus measurement." The Pfaffian test (30A) can produce a Level 4 topological prediction; the grid search (30B) tests whether the framework produces the Standard Model at all.

These sessions are independent. 30A requires its own prerequisite (off-Jensen minimum location) which 30B delivers as a byproduct. Running 30B first provides the minimum location needed by 30A.

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
| 2 | 3-sector BCS free energy on grid + locate minimum | phonon-sim | ~1-2 hr | PENDING |
| 3 | Full Dirac spectrum at minimum ($N_{\max} = 6$) | phonon-sim | ~5-10 min | PENDING |
| 4 | RGE running + NCG-KK tension check | phonon-sim / einstein | analytic | PENDING |
| 5 | Diagnostics at minimum (level stats, AZ, DOS) | phonon-sim | ~0 | PENDING |
| 5b | Order-one condition at minimum (contingent on P-30w) | phonon-sim | ~5-10 min | PENDING |
| 6 | Grid extension to T1 direction (contingent) | phonon-sim | ~30-60 min | PENDING |

## Gate Verdicts — Existential

| ID | Condition | Status |
|:---|:----------|:-------|
| **P-30w** | $\sin^2(\theta_W) \in [0.20, 0.25]$ at minimum | PENDING |
| **P-30phi** | $m_{(3,0)}/m_{(0,0)} \in [1.52, 1.54]$ at minimum | PENDING |
| **RGE-A** | $g_1/g_2$ runs to $\tan(\theta_W) = 0.553$ at $M_Z$ | PENDING |

## Gate Verdicts — Hard Closes

| ID | Condition | Status |
|:---|:----------|:-------|
| B-30w | $\sin^2(\theta_W)$ outside $[0.15, 0.30]$ everywhere on grid | PENDING |
| B-30phi | Ratio outside $[1.45, 1.65]$ everywhere on grid | PENDING |
| B-30min | $V_{\text{total}}$ has no minimum in 2D grid | PENDING |
| B-30rge | RGE incompatible for all $M_{\text{KK}} \in [10^{10}, 10^{18}]$ GeV | PENDING |
| B-30nck | NCG-KK coupling irreconcilable ($\Lambda_{\text{SA}}/M_{\text{KK}} \notin [10^{-3}, 10^3]$) | PENDING |

## Gate Verdicts — Positive Signals

| ID | Condition | Status |
|:---|:----------|:-------|
| P-30a | P-30w + P-30phi both PASS (Scenario A) | PENDING |
| P-30b | P-30w + RGE-A both PASS | PENDING |
| P-30pmns | PMNS angles match NuFIT ($\theta_{13}$, $\theta_{23}$) | PENDING |
| P-30conv | SDW shortcut matches full spectrum $< 5\%$ | PENDING |
| P-30golden | Ratio $\in [1.610, 1.626]$ (golden ratio $\phi$) | PENDING |

## Gate Verdicts — Diagnostics

| ID | Condition | Status |
|:---|:----------|:-------|
| DOS-1 | DOS at minimum $>$ DOS at Jensen ($\tau = 0.35$) | PENDING |
| AZ-1 | AZ class = BDI (unchanged from Jensen) | PENDING |
| HM-1 | Anderson-Higgs mode $m_H^2 > 0$ at minimum | PENDING |
| OO-1 | Order-one violation at minimum (contingent on P-30w) | PENDING |

## Deliverables

| Output | Step | Status |
|:-------|:-----|:-------|
| `s30b_sdw_grid.npz` / `.py` | 1 | PENDING |
| `s30b_grid_bcs.npz` / `.py` | 2-3 | PENDING |
| `s30b_minimum_spectrum.npz` | 3 | PENDING |
| `s30b_5d_stability.npz` | 2 | PENDING |
| `s30b_rge_running.npz` / `.py` | 4 | PENDING |
| `s30b_landscape.png` | 2 | PENDING |
| `s30b_weinberg_contour.png` | 1-2 | PENDING |
| `s30b_phi_contour.png` | 3 | PENDING |
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
| einstein-theorist | Connes Papers 07, 10 (spectral action coefficients, GUT-scale coupling relations). Session 29 Connes Excursion. Assess NCG-KK coupling tension (XS-2) at the off-Jensen minimum. |
| baptista-spacetime-analyst | `researchers/Baptista/` -- Paper 15 Section 3.5-3.7 (U(2)-invariant moduli space, scalar curvature, Lagrangian), Paper 17 eq 1.3-1.4 ($[D_K, \mathcal{L}_X]$), Paper 18 Section 6-7 (mass mixing, CKM/PMNS). Validate the off-Jensen Dirac spectrum against Baptista's geometric expectations. |
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

These are zero-parameter predictions at the minimum. The RGE gate (Part A) tests whether the ratio at $M_{\text{KK}}$ runs to the correct value at $M_Z$ under standard one-loop SM beta functions.

### Topological Classification Off-Jensen

On the Jensen curve, the BCS condensate on SU(3) is in Altland-Zirnbauer symmetry class **BDI** with $T^2 = +1$ (Session 17c). The classification depends on three discrete symmetries:

- **Time-reversal** $T$: implemented by the real structure $J$ with $J^2 = +1$ (KO-dim 6). $[J, D_K(\tau)] = 0$ is an algebraic theorem for all $\tau$, for ANY left-invariant metric (Session 17a). **This survives off-Jensen.**
- **Particle-hole** $C$: implemented by the charge conjugation operator. **Also survives off-Jensen** (algebraic, not metric-dependent).
- **Chiral** $S = TC$: survives if both $T$ and $C$ survive.

The AZ class is determined by $T^2$ and $C^2$, both of which are algebraic (representation-theoretic) and independent of the metric. **Therefore BDI should persist off-Jensen for any U(2)-invariant metric.** However, the Pfaffian invariant depends not just on the symmetry class but on the specific representation content, which does change off-Jensen (sector multiplicities shift). Step 5 (AZ-1 gate) verifies this explicitly.

---

# II-b. OBSERVATIONS OF OPPORTUNITY (OoO)

**OoO** = **Observations of Opportunity**. These are "nice to have" diagnostics, cross-checks, and data pulls embedded within computation steps. They are NOT required for gate verdicts and do NOT block session progress. OoOs provide supplementary context — condensed matter analogs, PDG comparisons, convergence checks — that enrich interpretation but are strictly optional.

**Tracking**: OoOs are statused and tracked separately from the main gate structure (Section IV). An OoO that is skipped does not affect any gate verdict. An OoO that produces a surprising result may be promoted to a gate in a future session, but within this session it remains advisory.

| OoO ID | Step | Description | Status |
|:-------|:-----|:------------|:-------|
| OoO-0b | 0 | Isotropic-to-anisotropic BCS analog (He-3 A→B, Leggett 1975); validation $< 10^{-12}$ justification | PENDING |
| OoO-1b | 1 | Overlay PDG precision contours ($\sin^2\theta_W$, $\alpha_{\text{em}}$) on $(\tau, \epsilon)$ plane via VizieR `B/pdg`; SDW-Sommerfeld breakdown check | PENDING |
| OoO-2b | 2 | Pull DESI DR1/DR2 $w_0$-$w_a$ constraints; band-edge BCS analogs (SrTiO$_3$, TBG); Anderson-Higgs mode $m_H^2 \to 0$ check | PENDING |
| OoO-3b | 3 | Pull NuFIT PMNS angles, $\Delta m^2$, quark mass ratios via VizieR `B/pdg`; R-1 J-parity check; Poisson→GOE level statistics transition | PENDING |
| OoO-4b | 4 | Pull PDG $\alpha_i(M_Z)$; Super-K proton lifetime bound; NCG-KK heavy-fermion analog ($T_K \sim T_{\text{RKKY}}$) | PENDING |
| OoO-5b | 5 | AZ class algebraic survival off-Jensen; sector composition = MgB$_2$ $\sigma$/$\pi$ analog; iron pnictide $s_\pm$ precedent | PENDING |
| OoO-5b' | 5b | He-3-B emergent gauge symmetry (Volovik); Anderson's theorem analog for order-one condition | PENDING |
| OoO-6b | 6 | Pomeranchuk volume change analog (UGe$_2$/URhGe/UTe$_2$); pull $G_N$, LLR $|\dot{G}/G|$ bound via VizieR `B/pdg` | PENDING |

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

**Output**: `s30b_sdw_grid.npz` containing the 2D arrays for $R$, $\sin^2(\theta_W)$, $g_1/g_2$, $a_2$, and the $F_{\text{BCS}}^{3\text{-sector}}$ landscape from Step 3.

**OoO**: Overlay PDG precision contours on the $(\tau, \epsilon)$ plane — $\sin^2\theta_W^{\text{lept}}_{\text{eff}} = 0.23122 \pm 0.00004$, $\alpha_{\text{em}}(M_Z) = 1/127.951$ via VizieR `B/pdg`. SDW shortcut is a Sommerfeld expansion analog — known to fail near van Hove singularities where BCS is strongest. If SDW minimum disagrees with full BCS minimum (Step 2) by more than one grid spacing, the shortcut is unreliable.

**Agent**: phonon-exflation-sim

## Step 2: 3-Sector BCS Free Energy on the Same Grid

**Fusion Priority**: Integral to Priority 1 (the minimum of $V_{\text{total}} = S_{\text{spectral}} + F_{\text{BCS}}$ requires both terms)
**Cost**: ~1-2 hours at `max_pq_sum = 3` for 441 grid points. With 3 sectors only: ~8.7s per point, ~64 min total. With all 10 sectors: ~2 hours total.

**What**: At each grid point $(\tau, \epsilon)$, compute the Dirac spectrum for ALL sectors with $p+q \leq 3$ (10 sectors total: (0,0), (1,0), (0,1), (2,0), (0,2), (1,1), (3,0), (0,3), (2,1), (1,2)) using the generalized code from Step 0. **Store eigenvalues for all sectors** — they are needed for the spectral action sum $S_{\text{spectral}}$, level statistics (Step 5), and as potential input to Session 30A. The BCS free energy uses only the 3 load-bearing sectors:

$$F_{\text{BCS}}^{3\text{-sector}}(\tau, \epsilon; \mu) = \sum_{r \in \{(0,0),(3,0),(0,3)\}} \text{mult}(r) \cdot F_{\text{cond}}^{(r)}(\tau, \epsilon; \mu)$$

with multiplicities 16, 100, 100. The self-consistent chemical potential $\mu = \lambda_{\min}$ (the smallest positive eigenvalue of $D_K$ at each grid point).

**Grid reduction**: If full 441-point grid is too expensive, first run Step 1 (Seeley-DeWitt, 20 sec) to identify the region of interest, then run the full Dirac spectrum on a reduced 10$\times$10 grid centered on the Seeley-DeWitt minimum. Cost: ~15 minutes.

**What to compute at each grid point** (store eigenvalues for ALL 10 sectors with $p+q \leq 3$; the BCS free energy uses only 3, but $S_{\text{spectral}}$ and Step 5 diagnostics require the full spectrum):
1. Dirac eigenvalues for ALL sectors with $p+q \leq 3$
2. $\lambda_{\min}$ (smallest positive eigenvalue)
3. $F_{\text{BCS}}^{3\text{-sector}}$ at $\mu = \lambda_{\min}$ and $\mu = 1.2 \lambda_{\min}$
4. BCS gap $\Delta/\lambda_{\min}$ for each sector
5. Spectral action leading contribution $S_{\text{spectral}}(\tau, \epsilon)$ from eigenvalue sum
6. **DOS at band edge** $N(E_F)$: count eigenvalues within $\delta E$ of $\lambda_{\min}$ (zero-cost from eigenvalue data). Confirms whether Pomeranchuk deepening is driven by DOS enhancement or trivial gap rescaling.
7. **Anderson-Higgs mode mass$^2$**: from Gaussian fluctuation analysis at each grid point (adapted from `s29b_gaussian_correction.py`). If $m_H^2 \to 0$ at any point on the grid, mean-field BCS breaks down there (quantum critical point). This is a zero-cost diagnostic from the BCS data.

**Locate the minimum**: Find $(\tau_{\min}, \epsilon_{\min})$ that minimizes $V_{\text{total}} = S_{\text{spectral}} + F_{\text{BCS}}^{3\text{-sector}}$. Verify it is a genuine minimum by computing the 2$\times$2 Hessian $\partial^2 V_{\text{total}} / \partial x_i \partial x_j$ (where $x = (\tau, \epsilon)$) via finite differences. **Both eigenvalues must be positive.** If either is negative, the minimum lies outside the volume-preserving surface and Step 6 (T1 extension) is triggered.

**Full 5D stability check at the minimum**: Once the 2D minimum is found, check transverse stability in the U(2)-breaking directions (T3, T4). These had positive eigenvalues on Jensen ($E_3 = +219$, $E_4 = +1{,}775$) but must be reconfirmed at the off-Jensen point. Compute via finite differences: perturb $\lambda_a \to \lambda_a \cdot e^{\delta \cdot t_{3,a}}$ and $\lambda_a \to \lambda_a \cdot e^{\delta \cdot t_{4,a}}$ at the minimum and check $\delta^2 V_{\text{total}} > 0$.

**Output**: `s30b_grid_bcs.npz` containing the full 2D landscape of $V_{\text{total}}$, $F_{\text{BCS}}$, $\lambda_{\min}$, $\Delta/\lambda_{\min}$, and the minimum location.

**OoO**: Pull DESI DR1/DR2 $w_0$-$w_a$ constraints (VizieR or literature) for w = -1 null prediction check. Band-edge BCS analog: SrTiO$_3$ (dilute SC), twisted bilayer graphene. $\Delta/\lambda_{\min} > 0.5$ signals strong-coupling BEC regime — mean-field qualitatively correct but quantitatively approximate. Anderson-Higgs mode observed in NbSe$_2$ — $m_H^2 \to 0$ marks quantum critical point where mean-field fails.

**Agent**: phonon-exflation-sim

## Step 3: Full Dirac Spectrum at the Minimum

**Fusion Priority**: 2 (Session 29 Fusion Section IX.2)
**Cost**: ~5-10 minutes at `max_pq_sum = 6` for a single point

**What**: At the minimum $(\tau_{\min}, \epsilon_{\min})$ identified in Step 2, compute the full Dirac spectrum to high truncation order. This gives:

1. **$\phi_{\text{paasch}}$**: $m_{(3,0)}/m_{(0,0)}$ eigenvalue ratio (P-30phi gate)
2. **$\sin^2(\theta_W)$**: from $\lambda_2/(\lambda_1 + \lambda_2)$ at the minimum (P-30w gate -- cross-check with Seeley-DeWitt)
3. **PMNS angles**: tridiagonal Kosmann kernel extraction at the minimum (upgrade P-29b from CONDITIONAL)
4. **Full eigenvalue spectrum**: level spacing statistics (Poisson vs GUE/GOE), avoided crossing census, Berry curvature diagnostic
5. **$F_{\text{BCS}}^{3\text{-sector}}$**: high-accuracy value at the minimum for gate classification

**Validation**: The generalized code from Step 0 must work at `max_pq_sum = 6` (higher sectors include (6,0), (0,6), etc. with large representation dimensions). Verify that eigenvalue counts match expected dimensions before running the full computation.

**Key diagnostic**: Does the eigenvalue ratio $m_{(3,0)}/m_{(0,0)}$ persist at the BCS minimum? Session 12 found this ratio to be 1.531580 at $\tau = 0.15$ on the Jensen curve. The ratio varies with $\tau$ and $\epsilon$ — it is NOT a constant. P-30phi tests whether this value persists at the off-Jensen BCS minimum (structural invariance). P-30golden tests whether the ratio approaches $\phi = 1.618$ at the minimum (a stronger claim). The T-7 tension (Session 29 Fusion Section VIII) — whether P-30w and P-30phi can be satisfied simultaneously — is directly tested.

**Output**: `s30b_minimum_spectrum.npz` containing full eigenvalue list, eigenvectors, $\phi_{\text{paasch}}$, PMNS angles, level statistics.

**OoO**: Pull NuFIT PMNS angles ($\sin^2\theta_{12} = 0.303$, $\sin^2\theta_{23} = 0.572$, $\sin^2\theta_{13} = 0.02203$), $\Delta m^2$ values, quark mass ratios via VizieR `B/pdg`. R-1 neutrino ratio: J-protected Kramers degeneracy may keep R ~ 10$^{14}$ off-Jensen unless relevant eigenvalues are NOT J-paired — check J-parity subspace membership. Poisson→GOE level statistics transition would indicate V(gap,gap) = 0 selection rule may be lifted off-Jensen.

**Agent**: phonon-exflation-sim

## Step 4: RGE Running from the Minimum

**Fusion Priority**: 3 (Session 29 Fusion Section IX.2)
**Cost**: Zero (analytic, ~50 lines)

**What**: Take $g_1/g_2$ at the off-Jensen minimum (from Steps 1-3) and run it down to $M_Z$ using standard one-loop SM beta functions:

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
6. **DOS at band edge** $N(\lambda_{\min})$: Compare with Jensen-curve value. Quantifies the Pomeranchuk DOS enhancement (DOS-1 gate).

**Output**: Diagnostics appended to `s30b_minimum_spectrum.npz`.

**OoO**: AZ class is algebraically determined ($T^2$, $C^2$ representation-theoretic) — BDI expected to survive, but topological invariant VALUE can change via gap closings. Sector composition near gap edge = orbital character analog (MgB$_2$ $\sigma$/$\pi$ bands). Avoided crossings between sectors = inter-band scattering — if gap $< 0.01\lambda_{\min}$, may affect BCS pairing symmetry (iron pnictide $s_\pm \to s_{++}$ precedent).

**Agent**: phonon-exflation-sim

## Step 5b (Contingent): Order-One Condition at the Minimum (OO-1)

**Fusion Priority**: 7 (Session 29 Fusion Section IX.2, Tier 3)
**Cost**: ~5-10 minutes at a single point
**Condition**: Runs after Step 3 delivers the minimum spectrum. Triggers if P-30w PASSES (otherwise the gauge sector is already wrong and OO-1 is moot).

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
**Condition**: Only if the 2D $(\tau, \epsilon)$ grid shows the minimum lies at the boundary of the $\epsilon$ range, suggesting the true minimum requires the T1 (breathing) direction as well.

**What**: Extend to a 3D grid search including T1 displacement. T1 breaks volume-preservation, so this probes whether the physical minimum is volume-preserving or not.

**Significance**: If the minimum is NOT volume-preserving, this is a new structural finding -- the physical vacuum selects a non-Einstein metric on the internal space. Volume-preservation was an assumption in the Jensen family (Paper 15, eq 3.68), not a dynamical requirement.

**Output**: `s30b_3d_grid.npz` if needed.

**OoO**: Pomeranchuk volume change analog — magnetostriction in UGe$_2$/URhGe/UTe$_2$, He-3 solid-liquid transition. If non-volume-preserving, pull $G_N = 6.674 \times 10^{-11}$ and LLR bound $|\dot{G}/G| < 1.4 \times 10^{-13}$ yr$^{-1}$ via VizieR `B/pdg` for consistency check.

---

# IV. CONSTRAINT CONDITIONS AND GATE STRUCTURE

## Existential Gates (framework viability at stake)

| ID | Condition | Consequence |
|:---|:----------|:------------|
| **P-30w** | $\sin^2(\theta_W) \in [0.20, 0.25]$ at the off-Jensen minimum | Weinberg angle in the ballpark. Framework can produce correct electroweak mixing. |
| **P-30phi** | $m_{(3,0)}/m_{(0,0)} \in [1.52, 1.54]$ at the off-Jensen minimum | Eigenvalue ratio matches Session 12 value (1.531580) at the physical point. **Note**: This tests structural stability of the S12 ratio, NOT the golden ratio $\phi = 1.618$. The S12 value is 5.3% below $\phi$. See P-30phi discussion below. |
| **RGE-A** | $g_1/g_2$ at $M_{\text{KK}}$ runs to $\tan(\theta_W) = 0.553$ at $M_Z$ for some $M_{\text{KK}}$ | The KK-derived coupling ratio is consistent with SM running. Zero parameters. |

## Hard Closes

| ID | Condition | Consequence |
|:---|:----------|:------------|
| B-30w | $\sin^2(\theta_W) < 0.15$ or $> 0.30$ at ALL $(\tau, \epsilon)$ in the grid | Electroweak mixing cannot be reproduced. Gauge sector fails. |
| B-30phi | $m_{(3,0)}/m_{(0,0)} < 1.45$ or $> 1.65$ at ALL $(\tau, \epsilon)$ in the grid | Eigenvalue ratio does not pass through the S12 value (1.5316) or the golden ratio (1.618) anywhere on the U(2)-invariant surface. Neither geometric target is accessible. |
| B-30min | $V_{\text{total}}$ has NO minimum in the 2D grid (monotonic in both directions) | No BCS stabilization in U(2)-invariant family. Must search full 5D. |
| B-30rge | RGE-A gives $\sin^2(\theta_W)(M_Z) < 0.15$ or $> 0.30$ for ALL $M_{\text{KK}} \in [10^{10}, 10^{18}]$ GeV | KK coupling ratio incompatible with SM under any running. |
| B-30nck | NCG relation ($g_1 = g_2$ at $\Lambda_{\text{SA}}$) and KK relation ($g_1/g_2 = \sqrt{\lambda_2/\lambda_1}$) are irreconcilable: no $\Lambda_{\text{SA}}/M_{\text{KK}}$ ratio in $[10^{-3}, 10^3]$ makes both consistent | Internal inconsistency between NCG spectral action and KK dimensional reduction. Framework has contradictory gauge coupling derivations. This is the T-3 tension (Session 29 Fusion Section VIII) promoted to a hard close. |

## Positive Signals

| ID | Condition | Consequence |
|:---|:----------|:------------|
| P-30a | P-30w PASSES AND P-30phi PASSES | Both mass and mixing angle predictions work at the physical point. Scenario A from Session 29 Fusion. |
| P-30b | P-30w PASSES AND RGE-A PASSES | Framework derives the correct electroweak sector from geometry alone. |
| P-30pmns | $\sin^2(\theta_{13}) \in [0.015, 0.030]$ AND $\theta_{23} \in [40^\circ, 55^\circ]$ at the minimum | Full PMNS fit (upgrades P-29b from CONDITIONAL to PASS) |
| P-30conv | Seeley-DeWitt $\sin^2(\theta_W)$ agrees with full-spectrum $\sin^2(\theta_W)$ to $< 5\%$ | Spectral shortcut validated. Enables rapid future scans. |
| P-30golden | $m_{(3,0)}/m_{(0,0)} \in [1.610, 1.626]$ at the off-Jensen minimum | Eigenvalue ratio matches the golden ratio $\phi = 1.618$ at the physical point. Stronger than P-30phi (S12 value), would be a zero-parameter prediction. |

### P-30phi Clarification

Session 12 found $m_{(3,0)}/m_{(0,0)} = 1.531580$ at $\tau = 0.15$ on the Jensen curve. This value is 5.3% below the golden ratio $\phi = 1.618034$. The ratio varies with $\tau$: it is NOT a constant. Whether it approaches $\phi$ at the off-Jensen minimum is an open question.

**P-30phi** (the existential gate) tests whether the S12 value (1.5316) is structurally stable — does it survive at the physical minimum, or is it an accident of $\tau = 0.15$? The window $[1.52, 1.54]$ is a 1.3% band around the S12 value.

**P-30golden** (a positive signal) tests whether the ratio matches $\phi$ itself. This is a stronger claim — it would mean the BCS minimum selects a geometry where the mass ratio is exactly the golden ratio. The window $[1.610, 1.626]$ is a 1% band around $\phi$.

These test different physical hypotheses. Both are reported. Neither is conflated with the other.

## Diagnostic Gates (Informative, Not Existential)

| ID | Condition | Consequence |
|:---|:----------|:------------|
| DOS-1 | $N(E_F)$ at off-Jensen minimum $>$ $N(E_F)$ at Jensen ($\tau = 0.35$, $\epsilon = 0$) | Confirms Pomeranchuk DOS mechanism: BCS deepening is physical (more states at gap edge), not just a trivial rescaling of $\lambda_{\min}$. |
| AZ-1 | AZ symmetry class at off-Jensen minimum = BDI (unchanged from Jensen) | Pfaffian invariant remains $\mathbb{Z}$. Session 30A interpretation unchanged. |
| AZ-1' | AZ symmetry class at off-Jensen minimum $\neq$ BDI (e.g., DIII) | Pfaffian invariant changes to $\mathbb{Z}_2$. Session 30A must account for modified topological classification. **Flag to 30A before Pfaffian scan runs.** |
| HM-1 | Anderson-Higgs mode $m_H^2 > 0$ at the minimum | Mean-field BCS valid at the physical point. No quantum critical point. |
| HM-1' | $m_H^2 \leq 0$ at or near the minimum | Quantum critical point. Mean-field breaks down. BCS results at the minimum are unreliable. |

## Diagnostic Outputs (Regardless of Gate Verdicts)

**Note on trapping marginality (T-2)**: The 20% sensitivity window on the energy multiplier $E_{\text{mult}}$ (Session 29 Fusion, T-2) is a dynamical question that 30B does not resolve. The grid search determines the STATIC landscape; the trapping dynamics depend on the modulus velocity at the BCS transition boundary, which requires the DNP launch energy distribution (deferred to 30C/beyond). 30B's results are valid regardless of trapping margin — if the minimum exists and has the correct SM parameters, the framework is viable. Whether the modulus REACHES that minimum is a separate question.

Even if all existential gates fail, the grid search produces:

1. **Full $V_{\text{total}}$ landscape** on the U(2)-invariant surface -- first-ever map of this 2D energy surface
2. **Off-Jensen minimum location** -- input to Session 30A (Pfaffian computation)
3. **Spectral gap variation** across the moduli space -- structural mathematics (JGP level)
4. **Level statistics transition** -- Poisson-to-GOE as function of symmetry breaking
5. **Weinberg angle contour map** -- where in moduli space does $\sin^2(\theta_W) = 0.231$?

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
| Full spectrum at minimum + diagnostics | ~50 | High-order Dirac, level stats, AZ class, avoided crossings |
| Order-one condition at minimum (OO-1, contingent) | ~40 | $\|[[D_K, a], b^o]\|$ for each factor pair at $(\tau_{\min}, \epsilon_{\min})$ |
| RGE running + NCG-KK tension check | ~60 | One-loop SM beta functions, ratio test, $\Lambda_{\text{SA}}/M_{\text{KK}}$ analysis |
| Plotting (landscape, contours, gate diagnostics) | ~60 | Heatmaps of $V_{\text{total}}$, $\sin^2(\theta_W)$, $\phi_{\text{paasch}}$, DOS |
| **Total new code** | **~455** | Core Dirac solver reused; grid scan, diagnostics, OO-1, and NCG-KK analysis are new |

---

# VI. OUTPUT FILES

| Output | Contents |
|:-------|:---------|
| `s30b_sdw_grid.npz` | Seeley-DeWitt landscape: $R$, $a_2$, $\sin^2(\theta_W)$, $g_1/g_2$ over 441 grid points |
| `s30b_grid_bcs.npz` | Full $V_{\text{total}}$ landscape: $F_{\text{BCS}}^{3\text{-sector}}$, $S_{\text{spectral}}$, $\lambda_{\min}$, $\Delta/\lambda_{\min}$, $N(E_F)$, $m_H^2$ over grid |
| `s30b_minimum_spectrum.npz` | Full Dirac spectrum at minimum: eigenvalues, eigenvectors, $\phi_{\text{paasch}}$, PMNS, level stats, AZ class, avoided crossings |
| `s30b_5d_stability.npz` | T3/T4 transverse Hessian eigenvalues at the off-Jensen minimum |
| `s30b_rge_running.npz` | RGE curves: $\alpha_i(\mu)$ from $M_{\text{KK}}$ to $M_Z$, $\sin^2(\theta_W)(M_Z)$ derived, NCG-KK reconciliation analysis |
| `s30b_sdw_grid.py` | Step 1 script |
| `s30b_grid_bcs.py` | Steps 2-3 script |
| `s30b_rge_running.py` | Step 4 script |
| `s30b_landscape.png` | Heatmap of $V_{\text{total}}(\tau, \epsilon)$ with minimum marked |
| `s30b_weinberg_contour.png` | Contour of $\sin^2(\theta_W) = 0.231$ on the $(\tau, \epsilon)$ plane |
| `s30b_phi_contour.png` | Contours of $m_{(3,0)}/m_{(0,0)} = 1.5316$ (S12 value) and $= 1.618$ ($\phi$) on the $(\tau, \epsilon)$ plane |
| `s30b_fbcs_landscape.png` | Heatmap of $F_{\text{BCS}}^{3\text{-sector}}$ alone (without spectral action) on the $(\tau, \epsilon)$ grid |
| `s30b_dos_landscape.png` | Heatmap of $N(E_F)$ across the $(\tau, \epsilon)$ grid |

Gate verdicts appended to: `tier0-computation/s30b_gate_verdicts.txt`

---

# VII. SUCCESS CRITERIA

Session 30B is successful if it produces:

1. **A definitive off-Jensen minimum location** -- $(\tau_{\min}, \epsilon_{\min})$ with Hessian confirmation (both eigenvalues positive in 2D, and T3/T4 stability confirmed)
2. **P-30w verdict**: $\sin^2(\theta_W)$ at the minimum, classified against [0.20, 0.25]
3. **P-30phi verdict**: $m_{(3,0)}/m_{(0,0)}$ at the minimum, classified against [1.52, 1.54] (S12 value). Also report P-30golden (against [1.610, 1.626])
4. **RGE-A verdict**: Does $g_1/g_2$ at $M_{\text{KK}}$ run to the correct $\sin^2(\theta_W)$ at $M_Z$?
5. **B-30nck verdict**: Is the NCG-KK coupling tension reconcilable? $\Lambda_{\text{SA}}/M_{\text{KK}}$ ratio reported.
6. **PMNS at the minimum**: $\theta_{13}$, $\theta_{12}$, $\theta_{23}$ -- does the off-Jensen minimum improve or worsen the theta_23 failure?
7. **OO-1 verdict** (contingent on P-30w PASS): Order-one violation at the minimum -- better, worse, or unchanged from Jensen?
8. **Diagnostic verdicts**: DOS-1, AZ-1, HM-1 -- all classified
9. **Off-Jensen minimum delivered to Session 30A**: The Pfaffian computation (30A) uses this minimum as input. AZ class established before 30A runs.

### Possible Outcomes and Probability Impact

| Outcome | Probability Impact |
|:--------|:------------------|
| **Scenario A**: P-30w + P-30phi + RGE-A all PASS | **30-45%** -- framework derives SM from geometry. Paper preparation begins. |
| **Scenario B**: P-30w PASS, P-30phi FAIL (or vice versa) | **10-20%** -- structural tension between requirements. Investigate trade-off. |
| **Scenario B'**: P-30w FAIL, P-30phi PASS | **8-15%** -- gauge sector does not match. Investigate off-Jensen corrections in T1. |
| **Scenario C**: P-30w + P-30phi both FAIL | **3-5%** -- structural floor (Kepler-solids). Framework closes with publishable math. |
| P-30pmns FIRES (full PMNS fit including theta_23) | Additional **+5-10%** to any scenario above |
| B-30min FIRES (no minimum found) | **No change below current** -- must search 3D or full 5D space |

---

# VIII. AGENT ASSIGNMENTS

| Agent | Role |
|:------|:-----|
| **phonon-exflation-sim** | Primary computation: code generalization (Step 0), Seeley-DeWitt grid (Step 1), BCS grid (Step 2), full spectrum at minimum (Step 3), diagnostics (Step 5) |
| **einstein-theorist** | RGE running (Step 4), NCG-KK coupling tension analysis, physical interpretation of Weinberg angle result |
| **baptista-spacetime-analyst** | Geometry validation: U(2)-invariant metric formulas against Papers 15/17/18, scalar curvature cross-check, off-Jensen gauge coupling derivation, moduli space interpretation |
| **coordinator** | Context routing, gate tracking, scenario classification |

**Recommended team**: 3-4 agents. The phonon-sim agent carries the computational load. Einstein and Baptista provide independent theoretical validation. Coordinator tracks gates.

**Blast-first spawn workflow applies** (CLAUDE.md mandatory).

---

# IX. RELATIONSHIP TO SESSION 30A

**30B gates 30A.** The Pfaffian computation (30A) must run at the physical BCS minimum. Session 30B locates that minimum. Without 30B's output, 30A has no well-defined input geometry. This is a hard dependency, not a soft preference.

| | Session 30A (Pfaffian) | Session 30B (Grid Search) |
|:---|:---|:---|
| **Question** | Does $D_{\text{total}}$ have a Pfaffian sign change? | Does the frozen vacuum produce the Standard Model? |
| **Type** | Topological (binary, yes/no) | Quantitative (derived values vs measurement) |
| **Ceiling** | Level 4 prediction (20-40% if PASS) | Framework viability (30-45% if Scenario A) |
| **Input needed** | Off-Jensen minimum location **from 30B** | None beyond Session 29 |
| **Dependency** | **BLOCKED until 30B Step 2 delivers minimum** | Independent |

**Running order**: 30B runs first. 30A's prerequisite (Step 0: eigenvector extraction, Step 1: Lie derivative computation) can proceed in parallel with 30B, but the actual Pfaffian scan (30A Step 5) requires the minimum coordinates $(\tau_{\min}, \epsilon_{\min})$ from 30B Step 2. 30B should deliver these coordinates to 30A as soon as the grid search completes.

**AZ class dependency**: If the AZ symmetry class changes off-Jensen (AZ-1' fires in 30B Step 5), the Pfaffian invariant in 30A is $\mathbb{Z}_2$ rather than $\mathbb{Z}$. This modifies the interpretation of 30A's result. 30B must classify the AZ class BEFORE 30A's Pfaffian scan runs.

**Combined outcome**: If both 30A and 30B produce positive results (Pfaffian sign change AT the BCS minimum AND correct SM parameters), the framework probability would rise to 40-60% -- the highest it has been since the project began.

---

# X. DEFERRED TO SESSION 30C (AND BEYOND)

The following computations were considered for 30B and deliberately deferred. They are valuable but not prerequisite for the existential gates.

| Item | Cost | Reason for Deferral | Source |
|:-----|:-----|:-------------------|:-------|
| Order-one condition FULL SCAN (OO-1 over full grid) | ~10 hr | Contingent single-point OO-1 is in 30B Step 5b. Full grid scan deferred. | Fusion VII.1 |
| D_BCS axiom verification (DBCS-1) | Medium | Requires BCS-modified Dirac operator construction. Exploratory. | Fusion VI.2 |
| Mode-dependent BCS dressing for PMNS | ~1 hr | Only relevant if P-30pmns fails (theta_23 still wrong at minimum) | Fusion VI.6 |
| Quantum metric on U(2)-invariant surface | ~1 hr | Berry curvature topological classification. Diagnostic. | Fusion VI.5 |
| Wodzicki residue for cosmological constant | Low | Theoretical development. Addresses T-6 (120-order CC discrepancy). | Fusion VI.3 |
| Spectral distance at frozen minimum | Medium | NCG-native "diameter" of internal space. | Fusion VI.4 |
| Phonon Boltzmann equation (time-resolved KC-3) | ~1 hr | Closes last gap in Constraint Chain physical story. Not urgent given KC-3 PASS. | QA S29 collab 3.4 |
| Acoustic impedance at BCS transition boundary | Medium | Trapping margin improvement. Downstream of minimum location. | QA S29 collab |
| DNP launch energy distribution | Medium | Resolves trapping margin (20% sensitivity window) | Fusion IX.4, Priority 14 |

**30C recommended scope**: OO-1 + DBCS-1 + mode-dependent PMNS dressing. These are the Tier 3 items from Fusion IX.2 that become actionable once 30B delivers the minimum.

---

*Session 30B: The Decisive Grid. Covers Session 29 Fusion Synthesis Priorities 1-3 (Tier 1) plus zero-cost Tier 2 diagnostics and contingent OO-1 from Tier 3. First computation to directly test whether the off-Jensen BCS minimum produces the Standard Model. ~455 lines new code. ~2-3 hours total compute time. Three existential gates (P-30w, P-30phi, RGE-A). Five hard closes (B-30w, B-30phi, B-30min, B-30rge, B-30nck). Five positive signals (P-30a, P-30b, P-30pmns, P-30conv, P-30golden). Five diagnostic gates (DOS-1, AZ-1, HM-1, and primes). If Scenario A: framework derives SM from geometry with zero parameters. If Scenario C: framework closes with dignity and publishable structural mathematics. 30B gates 30A: the Pfaffian computation cannot proceed without the minimum location and AZ classification this session delivers.*
