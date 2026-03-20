# Session 30Aa: D_F Construction — Lie Derivative + Commutator Assembly

**Date**: TBD
**Author**: Team-lead (promoted from 29B-7; originally Session 29Bc)
**Depends on**: Session 29B complete. B-29d FIRED (Jensen saddle, 2/4 eigenvalues negative). The Pfaffian must be computed at the true U(2)-invariant minimum, not on the 1D Jensen curve.
**Prerequisite**: REVISED — Session 30 Thread 1 (2D U(2)-invariant grid search) must first locate the off-Jensen minimum. Then the D_F construction runs at that geometry. The original Jensen-stability prerequisite is replaced by off-Jensen minimum availability.
**Input data**:
- `tier0-computation/tier1_dirac_spectrum.py` (core Dirac code — to be modified for eigenvector return)
- `tier0-computation/branching_computation_32dim.py` (Xi, G5, gamma_F, particle identification)
- `tier0-computation/s23a_kosmann_singlet.py` (Kosmann operator K_a construction, corrected antisymmetric formula)
- `tier0-computation/s29b_jensen_transverse.npz` (Jensen 5D stability verdict — FROM 29Bb)
- Baptista Paper 17 eq 1.4: $[D_K, \mathcal{L}_X]$ formula
- Baptista Paper 18 Appendix E: SU(3) example

## Motivation

**The single highest-ceiling computation in the entire project.** Deferred for 13 sessions since Session 18, when it was first marked HIGHEST PRIORITY.

The existing D_K Pfaffian computation (Session 17c, `d2_pfaffian_computation.py`) returned Z_2 = +1 (trivial) for all tau in [0, 2.5]. But D_K is only the Kaluza-Klein part. The full Dirac operator on the NCG spectral triple (A, H, D) for M^4 x K is:

$$D_{\text{total}} = D_K \otimes \mathbf{1}_F + \gamma_5^{(K)} \otimes D_F$$

where $D_F$ is the **finite Dirac operator** encoding Yukawa couplings and Majorana mass terms, acting on $H_F = \mathbb{C}^{32}$.

Session 30Aa builds the D_F(tau) matrix from first principles using the Baptista KK-geometric construction. This is the prerequisite for the Pfaffian scan in Session 30Ab.

### Two Approaches to D_F

#### Approach A: Connes-Chamseddine-Marcolli (NCG from finite geometry)

$D_F$ contains Yukawa coupling matrices ($Y_\nu, Y_e, Y_u, Y_d$) and Majorana mass matrix $M_R$. These are ~20 FREE PARAMETERS per generation. The Pfaffian test would use KNOWN experimental Yukawa couplings — interesting but not a zero-parameter prediction.

#### Approach B: Baptista (D_F derived from KK geometry)

$D_F$ is NOT an independent input. It emerges from the dimensional reduction of the higher-dimensional Dirac operator via the Kosmann-Lichnerowicz derivative. $D_F(\tau)$ is a FUNCTION of tau derived entirely from the geometry of (SU(3), g_tau). **Zero external parameters.**

**However**: The order-one condition (NCG Axiom 5) FAILS at O(1) for the SU(3) spectral triple (Session 28c, C-6: norm = 4.000). This has two interpretations:
- **(i)** The order-one condition is too restrictive for KK (Baptista framework uses full Diff(K))
- **(ii)** The framework is incomplete (SU(3) spectral triple is not a valid NCG spectral triple)

**This computation empirically distinguishes these interpretations.** If D_total has a Pfaffian sign change at a geometrically natural tau_c, interpretation (i) is strongly supported.

### What D_F Actually Is (Baptista Construction)

$D_F(\tau)$ is the matrix (per sector) given by:

$$[D_F]_{\alpha\beta} = \sum_{a \in \mathbb{C}^2} \langle \psi_\alpha | [D_K, \mathcal{L}_{e_a}] | \psi_\beta \rangle$$

where $\{e_a\}_{a=3,4,5,6}$ are the 4 non-Killing frame vectors. The commutator formula (Paper 17 eq 1.4):

$$[D_K, \mathcal{L}_X]\psi = \frac{1}{2}\sum_{i,j} (\mathcal{L}_X g_K)(v_i, v_j)\, v_i \cdot v_j \cdot \psi + \text{connection correction terms}$$

This is nonzero only for non-Killing $X$ (vanishes when $\mathcal{L}_X g_K = 0$). For Jensen deformation at tau > 0, the 4 C^2 directions are non-Killing.

### Why NOW (All Prerequisites Met)

- **Kosmann machinery** for $[D_K, \mathcal{L}_X]$: developed Session 23a
- **Eigenvector infrastructure**: built Session 12 (but eigenvectors were discarded — need ~5-line modification)
- **Order-one condition status** (C-6, Axiom 5 fails with norm 4.000): determined Session 28c
- **Jensen transverse stability** (29B-4): computed in 29Bb — B-29d FIRED (saddle). Computation redirected to off-Jensen minimum.
- **Off-Jensen minimum** (Session 30 Thread 1): 2D U(2)-invariant grid search locates the true minimum. **NEW PREREQUISITE.**

All prerequisites exist except Thread 1 (off-Jensen minimum). Compute that first, then run D_F construction at the true geometry.

---

# SESSION DASHBOARD

## Prerequisites

| ID | Requirement | Source | Status |
|:---|:-----------|:-------|:-------|
| PRE-1 | Session 29B complete, B-29d FIRED (Jensen saddle) | `s29b_gate_verdicts.txt` | CONFIRMED |
| PRE-2 | Off-Jensen minimum location from 30B Step 2 | 30B output | BLOCKED |

## Computation Steps (this sub-session)

| Step | Description | ~Lines | ~Cost | Status |
|:-----|:-----------|:-------|:------|:-------|
| 0 | Eigenvector extraction (`eigvals` → `eigh`) | ~5 | trivial | PENDING |
| 1 | Lie derivative $\mathcal{L}_{e_a} g_\tau$ for non-Killing directions | ~30 | trivial | PENDING |
| 2 | $[D_K, \mathcal{L}_{e_a}]$ commutator matrix in eigenbasis | ~80 | minutes | PENDING |
| 3 | Assemble $D_F(\tau)$ on truncated Hilbert space (432-dim) | ~40 | minutes | PENDING |

## Gate Verdicts (this sub-session)

| ID | Type | Short Description | Status |
|:---|:-----|:-----------------|:-------|
| B-30b | Hard Close | $D_F$ construction fails (numerically unstable) | PENDING |

## Deliverables

| Output | Description | Status |
|:-------|:-----------|:-------|
| `s30a_df_construction.npz` | D_F(tau) matrices, eigenvectors, Lie derivatives, chirality check norms | PENDING |
| `s30a_df_construction.py` | Steps 0-3 computation script | PENDING |
| `s30a_gate_verdicts.txt` | Gate verdict log (B-30b) | PENDING |

---

# 0. OPERATIONAL RULES

## COMPUTATION DISCIPLINE

Every result classified against its pre-registered gate BEFORE any interpretation. Report the number first. Classify second. Interpret third.

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s30a_`

## PRE-SESSION GATE CHECK (MANDATORY FIRST ACTION)

Before any computation, verify:
1. Session 30 Thread 1 (2D U(2)-invariant grid search) has completed
2. The off-Jensen minimum location (tau_min, eps_T2_min) is available
3. Read `tier0-computation/s29b_gate_verdicts.txt` — B-29d FIRED (Jensen saddle, confirmed). The D_F construction runs at the off-Jensen minimum geometry, NOT on the 1D Jensen curve.

If the off-Jensen minimum has not been located, **this session does not proceed**.

## COMPLETION SIGNAL

Session ends ONLY when user approves shutdown explicitly. Idle agents are not finished agents.

---

# I. REQUIRED READING

## ALL agents (MANDATORY):

1. **Session 29B plan Section III (29B-7)**: `sessions/session-plan/session-29B-plan.md` — The full 29B-7 specification with both Approach A/B analysis, re-examination of tensor product structure, and revised method.
2. **Session 17c results**: `sessions/session-17/session-17c-results.md` — Original D_K Pfaffian computation. Z_2 = +1 for all tau. Parlett-Reid implementation.
3. **Session 22b results**: `sessions/session-22/session-22b-results.md` — D_K block-diagonality theorem. Proven at 8.4e-15.
4. **Session 28c results**: `sessions/session-28/session-28c-results.md` — NCG axiom check (C-6: 6/7 pass, Axiom 5 order-one condition fails, norm = 4.000).
5. **Session 23a synthesis**: `sessions/session-23/session-23a-synthesis.md` — Kosmann operator construction, corrected antisymmetric formula, V(gap,gap) = 0 selection rule.
6. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## Agent-specific required reading:

| Agent | Additional Reading |
|:------|:-------------------|
| phonon-exflation-sim | `tier0-computation/d2_pfaffian_computation.py` (Pfaffian algorithm to reuse in 30Ab), `tier0-computation/tier1_dirac_spectrum.py` (eigenvector modification target), `tier0-computation/s23a_kosmann_singlet.py` (Kosmann operator) |
| einstein-theorist | `researchers/Einstein/index.md`. Connes Papers 09, 10, 12 — D_F structure in standard NCG. Assess whether Approach B (KK-derived D_F) is physically consistent despite order-one failure. |
| baptista-spacetime-analyst | `researchers/Baptista/` — Paper 15 (moduli space), Paper 17 eq 1.3-1.4 ($[D_K, \mathcal{L}_X]$ formula), Paper 18 Section 6-7 (mass mixing = CKM/PMNS), Appendix E (SU(3) example). Cross-validate the D_F construction against Baptista's actual equations. |
| coordinator | This prompt gate conditions. Memorize ALL thresholds before first computation completes |

---

# II. COMPUTATION STEPS

## Step 0: Eigenvector Extraction (Prerequisite Modification)

Modify `tier1_dirac_spectrum.py` function `dirac_operator_on_irrep()` to return eigenvectors alongside eigenvalues. Currently calls `np.linalg.eigvals()` (eigenvalues only). Change to `np.linalg.eigh()` (eigenvalues + eigenvectors). ~5-line modification.

$D_\pi(\tau)$ on sector $(p,q)$ is a $(\dim(p,q) \cdot 16) \times (\dim(p,q) \cdot 16)$ Hermitian matrix. Store eigenvectors $|\psi_n^{(p,q)}(\tau)\rangle$ for all sectors with $p+q \leq N_{\max}$.

## Step 1: Compute Lie Derivative $\mathcal{L}_{e_a} g_\tau$ for $a = 3,4,5,6$

The Lie derivative of the Jensen metric along the non-Killing frame vectors. An $8 \times 8$ symmetric tensor per direction, computed from:

$$(\mathcal{L}_{e_a} g)_{bc} = g_{bd} f^d_{ac} + g_{cd} f^d_{ab}$$

in the left-invariant frame (where $f^d_{ac}$ are the frame structure constants). All ingredients exist in `tier1_dirac_spectrum.py`. **~30 lines, new function.**

## Step 2: Compute $[D_K, \mathcal{L}_{e_a}]$ Matrix in Eigenbasis

Using Paper 17 eq 1.4, compute the commutator as a matrix on the spinor space. For each sector $(p,q)$, project into the $D_K$-eigenbasis:

$$[D_K, \mathcal{L}_{e_a}]_{\alpha\beta} = (m_\alpha + m_\beta) \langle \psi_\alpha | \mathcal{L}_{e_a} | \psi_\beta \rangle_{\text{chiral}}$$

(from Paper 17 eq 1.6, the mass sum formula). The matrix elements involve the Kosmann operator already computed. **~80 lines, implements Paper 17 eq 1.4.**

## Step 3: Assemble $D_F(\tau)$ on the Truncated Hilbert Space

Sum contributions from all 4 non-Killing directions. $D_F(\tau)$ is Hermitian on $\mathcal{H}_{\text{trunc}}$. Verify: $D_F$ must anticommute with $\gamma_F$ (chirality condition). **~40 lines.**

The truncated Hilbert space at $N_{\max} = 2$ (sectors (0,0), (1,0), (0,1), (2,0), (0,2), (1,1)):
$$\dim(\mathcal{H}_{\text{trunc}}) = (1 + 3 + 3 + 6 + 6 + 8) \times 16 = 432$$

**OoO-3a**: Verify $\|D_F \gamma_F + \gamma_F D_F\| < 10^{-10}$ — this chirality check is a **pass/fail prerequisite** for the Pfaffian in 30Ab. If chiral symmetry is broken, AZ class shifts BDI → AI (trivial topology in 0D), and the Pfaffian invariant is absent. Compare $D_F$ matrix element hierarchies against PDG Yukawa ratios ($m_u/m_t$, $m_d/m_b$, CKM mixing) via VizieR `B/pdg`.

---

# III. CONSTRAINT CONDITIONS AND GATE STRUCTURE

## Hard Close (this sub-session)

| ID | Condition | Consequence |
|:---|:----------|:------------|
| B-30b | D_F construction fails: Lie derivative formula ill-defined or numerically unstable | Baptista KK-geometric Yukawa approach does not yield consistent D_F. Must fall back to Approach A (experimental Yukawa inputs). |

## Pass Condition for 30Ab

30Ab proceeds if and only if:
1. B-30b did NOT fire (D_F construction succeeded)
2. D_F(tau) matrices are available in `s30a_df_construction.npz`
3. Chirality check $\|D_F \gamma_F + \gamma_F D_F\|$ is either < $10^{-10}$ (ideal) or documented with magnitude

---

# IV. NEW CODE INVENTORY

| Component | Lines | Description |
|:----------|:------|:------------|
| Eigenvector return from `dirac_operator_on_irrep()` | ~5 | Modify `eigvals` → `eigh` |
| Lie derivative $\mathcal{L}_{e_a} g_\tau$ computation | ~30 | New function using existing frame/structure constants |
| $[D_K, \mathcal{L}_{e_a}]$ commutator matrix assembly | ~80 | Implements Paper 17 eq 1.4 |
| $D_F(\tau)$ assembly on truncated Hilbert space | ~40 | Sum over non-Killing directions |
| **Total new code** | **~155** | Kosmann operator reused from s23a |

---

# V. OUTPUT FILES

| Output | Contents |
|:-------|:---------|
| `s30a_df_construction.npz` | `tau_values`, `D_F_matrices` (D_F at each tau), `eigvecs_by_sector` (eigenvectors), `lie_deriv_g` (Lie derivative tensors), `commutator_matrices`, `chirality_norms` ($\|D_F \gamma_F + \gamma_F D_F\|$), `D_F_frobenius_norms` |
| `s30a_df_construction.py` | Complete Steps 0-3 script |

Gate verdicts appended to: `tier0-computation/s30a_gate_verdicts.txt`

---

# VI. AGENT ASSIGNMENTS

| Agent | Role |
|:------|:-----|
| **phonon-exflation-sim** | Primary computation: eigenvectors, Lie derivative, commutator assembly, D_F construction |
| **einstein-theorist** | Theoretical oversight: D_F construction verification, order-one condition interpretation |
| **baptista-spacetime-analyst** | Geometry: Lie derivative formula validation against Papers 17-18, cross-sector coupling structure |
| **coordinator** | Context routing, gate tracking |

**Recommended team**: 3-4 agents. The baptista agent is essential for validating the $[D_K, \mathcal{L}_X]$ formula implementation against Papers 17-18.

**Blast-first spawn workflow applies** (CLAUDE.md mandatory).

---

*Steps 0-3 of the D_total Pfaffian computation. Builds D_F(tau) from first principles using Baptista's KK-geometric construction. ~155 lines new code. If B-30b fires (construction fails), fall back to Approach A. If construction succeeds, proceed to Session 30Ab (Pfaffian scan).*
