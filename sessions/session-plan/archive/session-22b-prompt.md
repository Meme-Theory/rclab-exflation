# Session 22b: Coupled Diagonalization — The Decisive Computation (P1-2)

## Session Type: COMPUTATION (hours — eigenvector extraction required)
## Agents: phonon-exflation-sim + baptista-spacetime-analyst + coordinator
## Session Goal: Execute the coupled V_IR computation (P1-2): extract eigenvectors of D_K, compute Kosmann-Lichnerowicz off-diagonal matrix elements, diagonalize in the coupled basis, and compute delta_T in the coupled basis. This is the single most important computation remaining in the perturbative program.

---

# 0. OPERATIONAL RULES — READ BEFORE ANYTHING ELSE

## DEPENDENCY: DO NOT START UNTIL SESSION 22a IS COMPLETE

This session depends on knowing the slow-roll epsilon(tau) result from Session 22a (computation SP-1). If epsilon < 1 in the physical window, the coupled computation is the last perturbative handle. If epsilon > 1 throughout, the coupled computation still runs but the interpretation changes — a coupled zero-crossing would then be the ONLY surviving perturbative mechanism.

Read `sessions/session-22/session-22a-synthesis.md` before beginning.

## TWO-PHASE STRUCTURE

**Phase A**: Eigenvector extraction and matrix element computation (phonon-exflation-sim primary).
**Phase B**: Coupled V_IR assembly, coupled delta_T, and interpretation (baptista primary, with phonon-exflation-sim support).

**COMPLETION SIGNAL**: Session ends ONLY when coordinator sends: "SESSION 22b COMPLETE — all agents confirm."

## MESSAGE PROTOCOL

**Work step, then inbox, work step, then inbox.** This session involves heavy computation. Check messages every 15-20 minutes during long runs — do not wait for a 4-hour job to complete before checking.

## COMPUTATION ENVIRONMENT

**Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**GPU**: AMD RX 9070 XT, 17 GB VRAM, ROCm 7.2. USE IT for eigenvector extraction.
**Output directory**: `tier0-computation/`
**Script prefix**: `s22b_`
**Expected total runtime**: 2-8 hours depending on eigenvector extraction method.

---

# I. CONTEXT: WHY THIS COMPUTATION IS DECISIVE

## The Block-Diagonal Approximation Error

All spectral computations in Sessions 7-21c used block-diagonal Peter-Weyl treatment: each (p,q) sector is an independent block of D_K. This approximation is valid in the UV (Weyl regime) but is known to fail at the gap edge for tau > 0:

From Session 21b/21c:
- |coupling|/|gap| = 4-5x for lowest modes at tau = 0.15-0.30
- CG coefficients are O(1) by Wigner-Eckart (no 1/sqrt(dim) suppression)
- The neutrino avoided crossing at tau=1.58 (gap = 8e-6) is DIRECT COMPUTATIONAL PROOF that the coupling produces real avoided crossings

This means:
- V_IR(tau) at N=50 is unreliable at O(100%) — the minimum might be real or artifact
- delta_T(tau) = +1081 at tau=0.30 is reliable for the UV contribution (89% UV) but could be qualitatively wrong for the IR gap-edge contribution (11%)
- The coupled computation is the only way to resolve these questions

## What the Coupled Computation Tests

**Pre-registered gate (ALL 15 R2 reviewers)**:

| Outcome | Trigger | Posterior |
|:--------|:--------|:----------|
| Coupled delta_T zero crossing in [0.15, 0.35] | T(tau_coupled) = tau_coupled at tau_0 in physical window | 50-58% |
| Coupled V_IR non-monotonic | V_IR minimum in coupled basis | +8-12 pp on top of current state |
| Both crossing + non-monotonic | | ~60-70% |
| Coupled delta_T also monotonic | No fixed point even with full coupling | 30-35% |
| Coupled V_IR still monotonic | Block-diagonal treatment was correct | V_IR route definitively closed |

**Probability of coupled delta_T zero crossing (reviewer estimates)**:
- Sagan: 15-25%
- Hawking: ~25%
- Feynman: ~30%
- Baptista: 35-40%

This uncertainty range reflects the genuine open question. The computation answers it.

---

# II. REQUIRED READING

## ALL agents (MANDATORY):

1. **Session 21c synthesis**: `sessions/session-21/session-21c-phase0-synthesis.md`
   — Sections IV (CP-2 confirmation: CG coefficients O(1)), V (scenario classification), VIII (Phase 1 pipeline priority).

2. **Session 21b Valar plan**: `sessions/session-plan/session-21b-valar-plan.md`
   — Section XI.5 (1/sqrt(dim) correction), Section XI.6 (flux-coupling-condensate chain), Section V (B-4 off-diagonal coupling escape route).

3. **R2 master collab**: `sessions/session-21/session-21c-r2-master-collab.md`
   — Section VIII (Tier 1 priority: coupled V_IR and coupled delta_T as items 1 and by-product), Section X (conditional probability structure).

4. **Session 22a synthesis**: `sessions/session-22/session-22a-synthesis.md` (**READ FIRST — dependency**)

5. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## Agent-specific required reading:

| Agent | Additional Reading |
|:------|:------------------|
| phonon-exflation-sim | `tier0-computation/tier1_dirac_spectrum.py` — existing Dirac spectrum infrastructure. Section with `compute_dirac_matrix()` and eigenvalue solvers. `tier0-computation/s21c_kk_verify.py` — partial delta_T code (starting point). |
| baptista | `researchers/Baptista/17_2024_Non_isometric_Killing_spinors.md` Sec 4.1 — Kosmann-Lichnerowicz derivative formula. `researchers/Baptista/18_2024_Frame_bundle.md` eq 1.4 — L_tilde correction. Session 21c synthesis Section IV, CP-2, for Wigner-Eckart theorem statement. |

---

# III. PHASE A: EIGENVECTOR EXTRACTION

**Primary**: phonon-exflation-sim
**Goal**: Modify the existing Dirac spectrum code to return eigenvectors in addition to eigenvalues.

## PA-1: Infrastructure Modification

The existing `tier1_dirac_spectrum.py` computes eigenvalues of D_K at each tau. Modify it to also return eigenvectors.

**Modification specification**:

1. In the function that computes the Dirac spectrum (currently returning eigenvalues only):
   - Switch from `scipy.linalg.eigvalsh()` to `scipy.linalg.eigh()` which returns (eigenvalues, eigenvectors).
   - Store the eigenvectors V_{tau} in a structured array indexed by sector (p,q) and mode index n.
   - Due to GPU availability: use `torch.linalg.eigh()` on GPU for the diagonalization if the matrix fits in VRAM (it will — the matrix is at most ~1000x1000 per sector at max_pq_sum=6).

2. For the coupled computation, we need eigenvectors at the gap-edge sectors (p+q <= 3) with sufficient precision. Focus on:
   - (0,0) singlet: 2 Dirac modes
   - (1,0)/(0,1) fundamental: 24 Dirac modes each (48 total)
   - (1,1) adjoint: 16 Dirac modes
   - (2,0)/(0,2): 12 Dirac modes each
   - Total gap-edge sector: ~120 Dirac modes

3. Run at tau values: 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50 (8 values in the physical window, plus 0.0 for normalization).

**Script**: `tier0-computation/s22b_eigenvector_extraction.py`

**Expected runtime**: ~10-30 minutes at max_pq_sum=4-5 for gap-edge sectors. GPU should accelerate this significantly.

**Output**: `tier0-computation/s22b_eigenvectors.npz`
- Keys: `tau_values`, `eigenvalues_{i}`, `eigenvectors_{i}`, `sector_p_{i}`, `sector_q_{i}`, `multiplicities_{i}` for i=0..8 (the 9 tau values)

---

## PA-2: Kosmann-Lichnerowicz Matrix Element Computation

**Primary**: baptista-spacetime-analyst (with phonon-exflation-sim support for numerical parts)
**Runtime**: 30 minutes to code, 1-4 hours to run

**Physical setup** (from Session 21b B-4 and 21c CP-2):

The Kosmann-Lichnerowicz derivative L_{e_a} on spinors (Baptista Paper 17, eq 4.1):

```
(L_{e_a} psi)_i = nabla_{e_a} psi_i + (1/4)(L_{e_a} g)^{jk} gamma_j gamma_k psi_i + (1/2)(nabla_{e_a} e^m_b) gamma^b psi_m
```

The key coupling comes from the metric Lie derivative term (L_{e_a} g)^{jk}. For the Jensen deformation, the coset C^2 directions e_a (indices 6-9 in the Gell-Mann basis) generate non-zero metric Lie derivatives because they are non-Killing for tau > 0.

From Session 21b eq XI.5.1:
- L_{e_a}: D^{(p,q)} tensor S -> D^{(p+1,q-1)} tensor S or D^{(p-1,q+1)} tensor S
- Selection rule: connects sectors differing by (1,-1) or (-1,1) in (p,q) labels
- CG coefficient: <D^{(p',q')} || L_{e_a} || D^{(p,q)}> = sqrt((p+1)(q+1)/(p+q+2)) * [SU(3) isoscalar factor]

**Coupling matrix element formula**:

```python
C_{nm}(tau) = <psi_n(tau) | (1/4) * (L_{e_a} g)^{jk} * gamma_j * gamma_k | psi_m(tau)>
```

This must be summed over the coset directions a (4 directions in C^2 subspace of su(3)).

**Protocol**:

1. From `s22b_eigenvectors.npz`: for each tau, load the eigenvectors of the (0,0), (1,0), (0,1), (1,1), (2,0), (0,2) sectors.

2. Compute the metric Lie derivative tensor at each tau:
   - (L_{e_a} g)_{bc} = nabla_b (e_a)_c + nabla_c (e_a)_b where e_a is the coset vector
   - On (SU(3), g_Jensen), this has analytic form from the Jensen metric components
   - From baptista's Session 21b result: ||L_{e_a} g||^2 = 9 * tau^2 near tau=0, and ~ e^{-2tau} at moderate tau

3. Form the gamma matrix expression: (L g)^{jk} gamma_j gamma_k in the 16-dimensional spinor space.

4. Compute C_{nm}(tau) by matrix multiplication:
   ```python
   C = eigvec_pq1.conj().T @ Kosmann_matrix @ eigvec_pq2
   ```
   where Kosmann_matrix encodes the (L g)^{jk} gamma_j gamma_k operator in the spinor basis.

5. Store C_{nm}(tau) as a sparse matrix (most off-diagonal couplings vanish by selection rules).

**NOTE on L_tilde vs L_X** (Baptista R2 collab, eq 1.4 of Paper 18): Baptista identified a correction L_tilde that differs from L_X at O(0.3) at tau=0.30. Run the computation twice: once with L_X (standard) and once with L_tilde (correct). If they differ qualitatively, the L_tilde result is the physically correct one.

**Script**: `tier0-computation/s22b_kosmann_matrix.py`
**Output**: `tier0-computation/s22b_kosmann_matrix.npz`

---

# IV. PHASE B: COUPLED V_IR AND COUPLED DELTA_T

**Primary**: phonon-exflation-sim (for diagonalization), baptista-spacetime-analyst (for interpretation)

## PB-1: Coupled Diagonalization

**Goal**: Build and diagonalize the full Kosmann-coupled Hamiltonian matrix for the gap-edge sectors.

**Setup**: The block-diagonal approximation treats each (p,q) sector independently. The coupled matrix is:

```
H_coupled = block_diag(H_{0,0}, H_{1,0}, H_{0,1}, H_{1,1}, ...) + C_offdiag
```

where C_offdiag contains the Kosmann-Lichnerowicz coupling matrix elements C_{nm} (from PA-2).

**Protocol**:

1. Assemble H_coupled at each tau by combining block-diagonal eigenvalues (on the diagonal) with off-diagonal coupling matrix elements C_{nm}.

2. Use `scipy.linalg.eigh()` or `torch.linalg.eigh()` on GPU to diagonalize H_coupled.

3. Extract the new coupled eigenvalues lambda_coupled_n(tau) for n = 1, ..., N_gap_edge.

4. **Key check**: At tau=0, coupling vanishes (all directions Killing). Coupled eigenvalues should agree with block-diagonal to machine epsilon at tau=0.

5. At tau=0.30, the block-diagonal gives: lambda_{(0,0)} ~ 0.822, coupling/gap ~ 4-5x. The coupled eigenvalue should shift by O(100%) from the block-diagonal value. **This shift is the signal**.

**Script**: `tier0-computation/s22b_coupled_diagonalization.py`
**Output**: `tier0-computation/s22b_coupled_eigenvalues.npz`

---

## PB-2: Coupled V_IR

**Goal**: Compute V_IR in the coupled basis.

**Formula**:
```
V_IR_coupled(tau) = (1/2) * [Sum_{bosonic coupled, n <= N} sqrt(lambda_n_bos) - Sum_{fermionic coupled, n <= N} sqrt(lambda_n_ferm)]
```

for N = 20, 50, 100, 200.

The key question: does the coupling CREATE or DESTROY the shallow minimum seen at N=50 in the block-diagonal treatment?

**Protocol**:

1. Load `s22b_coupled_eigenvalues.npz`.
2. Separate bosonic and fermionic coupled eigenvalues (use sector labels to classify).
3. Compute V_IR_coupled at each tau for each cutoff N.
4. Compare to block-diagonal V_IR from `s21c_V_IR.npz`.
5. Does V_IR_coupled have an interior minimum? At what tau? What depth?
6. **Connection to block-diagonal result**: The N=50 block-diagonal minimum (depth 0.8%) was classified UNCERTAIN-INTERESTING due to coupling uncertainty. After full coupling, is this minimum:
   - DEEPER (coupling enhances it) -> COMPELLING
   - UNCHANGED (block-diagonal was approximately correct at N=50) -> UNCERTAIN-INTERESTING confirmed
   - ABSENT (coupling destroys it, block-diagonal minimum was artifact) -> CLOSED
**Pre-registered Constraint Gates** (Baptista R2 collab, updated from 21b B-5 Computation 6):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| DECISIVE | Coupled V_IR minimum at tau in [0.15, 0.35], depth > 20% | 50 | +15-20 pp |
| COMPELLING | Coupled V_IR minimum at tau in [0.10, 0.45], depth > 5% | 15 | +10-12 pp |
| INTERESTING | Coupled V_IR minimum exists but at depth < 5% or tau outside [0.10, 0.45] | 4 | +3-5 pp |
| CLOSED | Coupled V_IR monotonic for all N (block-diagonal was qualitatively right) | 0.2 | -8-12 pp |

**Script**: `tier0-computation/s22b_coupled_V_IR.py`
**Output**: `tier0-computation/s22b_coupled_V_IR.npz`, `tier0-computation/s22b_coupled_V_IR.png`

---

## PB-3: Coupled delta_T

**Goal**: Compute delta_T in the coupled basis.

**Formula** (Feynman, Session 21a, extended to coupled basis):
```
delta_T_coupled(tau) = (1/(64 pi^2 e^{4tau})) * Sum_n Delta_b(sector_n) * ln(lambda_coupled_n^2(tau))
```

where sector_n is the sector label of the n-th coupled eigenstate, and Delta_b is computed from the sector label using the same branching rules as Session 21c.

**Critical subtlety** (Dirac, R2 collab): The (0,0) singlet has Delta_b = 0. Its contribution to delta_T is zero regardless of coupling. However, the coupling MIXES the (0,0) singlet with the (1,0) and (0,1) fundamental sectors. After coupling, the eigenstates are no longer pure-sector states — they are superpositions. The effective Delta_b for a mixed eigenstate is:

```
Delta_b_effective(n) = Sum_sector |<n|sector>|^2 * Delta_b(sector)
```

This is where the coupled computation can qualitatively change the result: the singlet mixes gauge charge into the gap-edge modes, potentially turning the positive singlet contribution into a negative one (with sign consistent with a zero crossing).

**Protocol**:

1. For each coupled eigenstate n, compute the sector decomposition |<n|sector>|^2 from the eigenvectors.
2. Compute Delta_b_effective(n) = Sum_sector weight * Delta_b(sector).
3. Compute delta_T_coupled(tau) = (1/(64 pi^2 e^{4tau})) * Sum_n Delta_b_effective(n) * ln(lambda_coupled_n^2(tau)).
4. Check for sign change / zero crossing.
5. **Compare to block-diagonal**: At tau=0.30, block-diagonal delta_T = 1081. The coupling must produce a correction of order -1081 or more for a zero crossing. This requires the effective Delta_b to change sign for the gap-edge modes.

**Pre-registered Constraint Gates** (15/15 R2 reviewers, Section VIII Tier 1 item 1):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| DECISIVE | Coupled delta_T zero crossing in [0.15, 0.35] | 30 | +15-20 pp |
| COMPELLING | Coupled delta_T zero crossing at some tau in [0.0, 1.0] | 12 | +8-12 pp |
| INTERESTING | Coupled delta_T significantly reduced at tau=0.30 (< 200 vs 1081 uncoupled) | 4 | +2-4 pp |
| CLOSED | Coupled delta_T positive throughout [0, 2.0] with same order of magnitude as uncoupled | 0.2 | -6-10 pp |
| NEUTRAL | Coupled delta_T positive but significantly reduced (100-500 at tau=0.30) | 1 | 0 pp |

**Script**: `tier0-computation/s22b_coupled_delta_T.py`
**Output**: `tier0-computation/s22b_coupled_delta_T.npz`, `tier0-computation/s22b_coupled_delta_T.png`

---

## PB-4: Coupled Neutrino R(tau) — By-product

**Goal**: Compute R(tau) = (lambda_3^2 - lambda_2^2)/(lambda_2^2 - lambda_1^2) in the coupled basis.

The neutrino gate was INCONCLUSIVE in the block-diagonal treatment because the R=32.6 crossing at tau=1.556 was a monopole artifact with fine-tuning 1:10^5. In the coupled basis, the avoided crossing at M2 (tau~1.58) has a physical gap of 8e-6 rather than a true crossing. The coupled computation will:
1. Smooth the eigenvalue trajectories near M2 (no true crossing, only avoided)
2. Potentially produce a smooth R(tau) that crosses 32.6 at a physically meaningful tau

**Protocol**:
1. From coupled eigenvalues, extract the 3 lightest modes at each tau.
2. Compute R(tau) = (lambda_3^2 - lambda_2^2)/(lambda_2^2 - lambda_1^2).
3. Does R cross 32.6 at a smooth, non-fine-tuned tau?
4. Is this tau consistent with the physical window [0.15, 0.55]?

**Pre-registered gate** (Neutrino R2 collab):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| PASS | Smooth R = 32.6 crossing in [0.15, 0.55] (neutrino gate reopens) | 3 | +3-5 pp |
| SOFT PASS | Smooth R crossing in [0.5, 2.0] but not in physical window | 1.5 | +1 pp |
| CLOSED | R never crosses 32.6 in coupled basis | 0.3 | -4-6 pp |

**Script**: Append to `s22b_coupled_delta_T.py` or `s22b_coupled_V_IR.py` (5 lines of additional code)

---

# V. PHASE B SYNTHESIS

After all computations complete, baptista and phonon-exflation-sim conduct cross-pollination before the coordinator assembles the synthesis.

## Cross-Pollination Questions

**phonon-exflation-sim -> baptista**: "The coupled eigenvalues shifted the gap-edge spectrum by amount X. Does this shift cross the BCS threshold? Compute g_eff_coupled = coupling/(lambda_min_coupled * V_K) and compare to g_c_coupled = lambda_min_coupled."

**baptista -> phonon-exflation-sim**: "The L_tilde vs L_X discrepancy at tau=0.30 — quantify it. If L_tilde changes coupled delta_T by > 10%, the L_tilde result supersedes L_X."

**Both -> coordinator**: "What is the sector decomposition of the lightest coupled mode? Is it singlet-dominated or fundamental-dominated? This determines Delta_b_effective and therefore the sign of the coupled delta_T contribution."

## Required Synthesis Content

The designated writer (coordinator) assembles:

1. **Coupled results table**: V_IR_coupled verdict, delta_T_coupled verdict, R(tau)_coupled verdict.
2. **Comparison to block-diagonal**: Which block-diagonal results were qualitatively wrong?
3. **BCS threshold assessment**: Does coupling strength after full diagonalization satisfy g_eff > g_c?
4. **Scenario determination**: Which R2 conditional scenario was realized? (Table X of R2 master collab)
5. **Updated probability**: Per-agent assessment + panel consensus.
6. **Handoff to 22c**: If coupled delta_T still monotonic, what does this mean for BCS/Pomeranchuk priority?

---

# VI. OUTPUT FILES

## Primary output:

`sessions/session-22/session-22b-synthesis.md`

## Computation output files:

| File | Content |
|:-----|:--------|
| `s22b_eigenvector_extraction.py` | Eigenvector extraction script |
| `s22b_eigenvectors.npz` | Eigenvectors at 9 tau values |
| `s22b_kosmann_matrix.py` | Coupling matrix element script |
| `s22b_kosmann_matrix.npz` | C_{nm}(tau) matrix elements |
| `s22b_coupled_diagonalization.py` | Full coupled Hamiltonian script |
| `s22b_coupled_eigenvalues.npz` | Coupled eigenvalues + sector labels |
| `s22b_coupled_V_IR.py/npz/png` | Coupled V_IR |
| `s22b_coupled_delta_T.py/npz/png` | Coupled delta_T + coupled R(tau) |

---

# VII. KNOWN FAILURE MODES AND MITIGATIONS

**Potential failure**: Eigenvector extraction hangs due to matrix size.
**Mitigation**: Restrict to sectors with p+q <= 3 (gap-edge only). Full spectrum not needed.

**Potential failure**: L_tilde correction is not implemented in Baptista's current code.
**Mitigation**: Run L_X first (Section PA-2), report result, then attempt L_tilde as a second pass. If L_tilde is unavailable in time, report L_X result clearly labeled as an approximation.

**Potential failure**: Coupling matrix elements are sparse and miss the relevant channel.
**Mitigation**: Check against the Wigner-Eckart CG coefficients analytically. For (0,0) -> (1,0) transition: CG = sqrt(1) = 1. If computed C_{nm} for this transition is << 1, there is a normalization error.

**Potential failure**: GPU computation gives NaN or Inf due to near-degenerate eigenvalues at M1/M2.
**Mitigation**: Add regularization: shift the diagonal by epsilon = 1e-8 before diagonalization. Document any regularization applied.

---

# VIII. THE SAGAN STANDARD

Pre-registered gates are recorded above. The critical meta-gate:

**If coupled delta_T is positive throughout [0, 2.0] with magnitude comparable to block-diagonal (> 100 at tau=0.30): the perturbative self-consistency route is closed at all levels of approximation.** Report this as a CLOSED. Do not reclassify as NEUTRAL because "the magnitude decreased." The pre-registered threshold is a zero crossing, not a reduction.

The panel has been clear: the threshold is the crossing. Landau's d=8 argument means mean-field is exact for the internal space — only a qualitatively new contribution (which is what full coupling could provide) changes the result.

---

*"The coupled computation is the tensor theory of gravity in the 1907-1912 analogy. The block-diagonal treatment was the scalar theory. We know the scalar theory was approximately right for weak fields but qualitatively wrong at the horizon. The question is whether the IR gap edge is strong-field territory."*
*— Einstein, R2 collab, Section II Camp 2*
