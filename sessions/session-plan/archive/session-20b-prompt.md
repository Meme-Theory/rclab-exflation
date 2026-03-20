# Session 20b: Lichnerowicz TT 2-Tensor Eigenvalue Sweep + V_total Minimum Search

## Session Type: New Code + Computation (2-3 DAYS)
## Agents: phonon-exflation-sim + kaluza-klein-theorist
## Session Goal: Compute the Lichnerowicz operator eigenvalues on TT 2-tensors on (SU(3), g_Jensen) across 21 tau-values. Assemble E_total(tau) from all four towers (scalar + vector + TT + Dirac). Determine whether V_total has a minimum. THIS IS THE DECISIVE COMPUTATION.

---

# I. CONTEXT

Sessions 18 and 19d established that V_eff(tau) is monotonically decreasing when computed from scalar (1 DOF), vector (8 DOF), and Dirac (16 DOF) modes only. The fermion/boson ratio is 8.36:1 — no spectral functional can overcome this.

Session 19d's self-audit discovered 741,636 missing bosonic DOF: the **TT 2-tensor modes** from Sym^2_0(T*K), with fiber dimension 27. Including them flips F/B to **0.44:1** (boson-dominated). The Lichnerowicz operator on TT 2-tensors couples to the **full Riemann tensor** R_{acbd}, giving qualitatively different tau-dependence from all previously computed spectra.

Session 20a built the Riemann tensor R_{abcd}(tau) infrastructure and tested the Seeley-DeWitt shortcut (da_2/dtau vs da_4/dtau). This session consumes R_{abcd} from 20a to construct the full Lichnerowicz eigenvalues.

**Why these agents**: phonon-exflation-sim owns the Peter-Weyl decomposition infrastructure (`tier1_dirac_spectrum.py`), the bosonic Laplacian code (`b6_scalar_vector_laplacian.py`), and will build the Lichnerowicz matrix. kaluza-klein-theorist provides the Duff-Nilsson-Pope stability framework, validates the TT projection, and interprets results in the KK context.

**Dependencies**: Consumes `r20a_riemann_tensor.npz` and `compute_riemann_tensor_ON(s)` from Session 20a (R-1). Also uses existing `kk1_bosonic_tower.py`, `b6_scalar_vector_laplacian.py`, and `tier1_dirac_spectrum.py`.

---

# II. REQUIRED READING

## For phonon-exflation-sim:

1. **Session 20a Riemann tensor**: `tier0-computation/r20a_riemann_tensor.py` — The R_{abcd}(tau) function and saved data from 20a R-1. This is your primary input.

2. **Session 19d synthesis**: `sessions/session-19/session-19d-synthesis.md` — Section IV (Lichnerowicz curvature coupling is the key differentiator). Section II (computation pipeline: R_{abcd} -> Lichnerowicz -> E_total -> band structure).

3. **Existing Laplacian infrastructure**: `tier0-computation/b6_scalar_vector_laplacian.py` — `compute_connection_ON()`, `ricci_tensor_ON()`, scalar and vector Laplacian assembly. Your code extends this.

4. **Peter-Weyl infrastructure**: `tier0-computation/tier1_dirac_spectrum.py` — `get_irrep(p,q)`, `jensen_metric(s)`, Gell-Mann structure constants. Sector dimensions and Casimir eigenvalues.

5. **Session 19d master collaboration**: `sessions/session-19/session-19d-master-collab.md` — Section II (Session 20 pipeline), Section III-B (Lichnerowicz curvature coupling), Baptista's subtlety about deformed TT projection.

6. **Your agent memory**: `.claude/agent-memory/phonon-exflation-sim/`

## For kaluza-klein-theorist:

7. **Baptista Paper 15**: `researchers/Baptista/15_2024_Internal_symmetries_in_Kaluza_Klein_models.md` — Section 3.3 (TT fluctuations), eqs 3.14-3.19 (Riemann tensor on Lie groups), eq 3.87 (4D mass formula: m^2_n = mu_n - R_{gK}/4).

8. **Duff-Nilsson-Pope stability**: The DNP criterion lambda_L >= 3m^2 for KK stability. Jensen-deformed SU(3) becomes "product-like" at large s — a TT mode crossing the DNP threshold signals geometric instability and a natural vacuum selection point.

9. **Session 19d KK collaboration**: `sessions/session-19/session-19d-kk-collab.md` (if exists) or the KK sections of `sessions/session-19/session-19d-master-collab.md`.

10. **Your agent memory**: `.claude/agent-memory/kaluza-klein-theorist/`

## Key Equations

**Lichnerowicz operator on symmetric 2-tensors:**
```
Delta_L h_{ab} = -nabla^2 h_{ab} - 2 R_{acbd} h^{cd} + 2 R_{(a}^c h_{b)c}
```
On a compact Lie group with left-invariant metric, the covariant Laplacian nabla^2 decomposes via Peter-Weyl. The Riemann coupling term R_{acbd} acts algebraically on the fiber Sym^2_0(R^8).

**TT projection:**
```
h in Sym^2_0(T*K)  with  div_g h = 0  (transverse)  and  tr_g h = 0  (traceless)
```
At tau=0 (bi-invariant): Sym^2_0(8) = 1 + 8 + 27 under adjoint SU(3). The 27 = (2,2) irrep is automatically TT.
At tau != 0 (Jensen): The TT condition uses the DEFORMED connection. Work with full Sym^2_0 (35 dim) and project onto div-free kernel within each Peter-Weyl sector.

**Peter-Weyl block structure:**
```
Each (p,q) sector has spatial dimension dim(p,q)^2.
Fiber: Sym^2_0(R^8) = 35 dimensions.
Full block: 35 * dim(p,q)^2.
Largest: (3,3) with dim=64, block = 35 * 64 = 2240. Tractable.
After TT projection: reduced to ~27 * dim(p,q)^2 (exact at s=0).
```

**E_total assembly:**
```
E_total(tau) = E_scalar(tau) + E_vector(tau) + E_TT(tau) - E_Dirac(tau)

Each: E_X(tau) = (1/2) Sum_n mult_n * |lambda_n(tau)|    [Casimir, linear weight]
  or: E_X(tau) = Sum_n mult_n * lambda_n^4 * log(lambda_n^2/mu^2)    [CW, quartic weight]
```
Compute BOTH weightings. The Casimir (linear) is the physical energy. The CW (quartic) is the 1-loop correction.

---

# III. CALCULATION ASSIGNMENTS

## Agent Allocation

| Assignment | Primary | Secondary | Rationale |
|:-----------|:--------|:----------|:----------|
| L-1: Lichnerowicz matrix assembly | phonon-sim | kk (validation) | Extends existing Peter-Weyl infrastructure |
| L-2: TT eigenvalue sweep | phonon-sim | kk (DNP check) | Computation + physics interpretation |
| L-3: V_total assembly + minimum search | phonon-sim | kk (closure/proceed) | Assembly of all four towers |

**Workflow**: L-1 -> L-2 -> L-3 (sequential). kk validates at each stage.

---

### Assignment L-1: Lichnerowicz Matrix Assembly (1-2 DAYS)

**Agent**: phonon-exflation-sim

#### Computation Steps

1. **Load R_{abcd}(tau)** from 20a (`r20a_riemann_tensor.py` or `.npz`).

2. **Construct Sym^2_0(R^8) basis**: The 35-dimensional space of traceless symmetric 2-tensors on R^8. Basis elements E_{ab}^{(I)} for I = 1..35.

3. **Compute the Riemann curvature endomorphism on Sym^2_0**:
   ```
   [R_endo]_{IJ}(tau) = -2 R_{acbd}(tau) [contracted with E^I and E^J]
   ```
   This is a 35x35 matrix at each tau — the "curvature mass matrix" for shape fluctuations.

4. **Assemble the full Lichnerowicz operator in the Peter-Weyl basis** for each sector (p,q):
   ```
   [Delta_L]_{(p,q)} = [nabla^2]_{(p,q)} tensor I_35 + I_{dim^2} tensor [R_endo(tau)]
   + [Ricci coupling term]
   ```
   Block size: 35 * dim(p,q)^2. Largest block at max_pq=6: sector (3,3) with dim=64 -> 2240 x 2240.

5. **Impose TT condition**: Project onto the kernel of the divergence operator div_g within each sector. At tau=0, this selects the 27 = (2,2) components of Sym^2_0(8). At tau != 0, compute the div kernel numerically via SVD of the divergence matrix.

6. **Validation at tau=0**: Bi-invariant Lichnerowicz eigenvalues must match the Casimir formula: lambda_L = C_2(p,q)/36 + [constant from Riemann endomorphism on (2,2)]. Cross-check with Ikeda-Taniguchi tables or Milnor's formulas.

#### Deliverable
- Function `lichnerowicz_TT_eigenvalues(s, max_pq_sum=6)` returning eigenvalue arrays per sector
- 35x35 curvature endomorphism R_endo(tau) validated against Kretschner scalar
- TT projection validated at tau=0 (must recover 27-dim subspace)

---

### Assignment L-2: TT Eigenvalue Sweep (HOURS after L-1)

**Agent**: phonon-exflation-sim

#### Computation Steps

1. **Sweep tau in [0.0, 0.1, ..., 2.0]** (21 values, matching existing grids).

2. **At each tau**: Compute Lichnerowicz TT eigenvalues for all sectors with p+q <= 6.

3. **Record per-sector**:
   - Eigenvalues lambda_L^{(n)}(tau)
   - Multiplicities (dim(p,q)^2 for each sector, times number of TT eigenvalues per sector)
   - Total TT DOF count at each tau (should be ~741,636 at max_pq=6)

4. **Phonon band structure plot**: omega vs C_2(p,q) for TT modes at tau=0, 0.5, 1.0, 1.5, 2.0. Overlay scalar, vector, and Dirac modes from existing data. This is the key visualization.

5. **DNP stability check (kk-theorist)**: For each TT mode, check lambda_L against the DNP threshold 3m^2 where m^2 = R_{gK}/4. Identify any modes that cross from stable to unstable as tau increases.

#### Deliverable
- TT eigenvalue data at 21 tau-values, saved to `l20b_lichnerowicz_data.npz`
- Phonon band structure plot (4 mode types, 5 tau values)
- DNP crossing analysis: which modes cross, at what tau

---

### Assignment L-3: V_total Assembly + Minimum Search (HOURS after L-2)

**Agent**: phonon-exflation-sim

#### Computation Steps

1. **Load all four towers** at each tau:
   - Scalar bosonic: from `kk1_bosonic_tower.py` (existing, corrected DOF)
   - Vector bosonic: from `b6_scalar_vector_laplacian.py` (existing; extend to max_pq=6 if needed)
   - TT bosonic: from L-2 (new)
   - Fermionic (Dirac): from `tier1_dirac_spectrum.py` (existing)

2. **Compute E_total(tau)** with BOTH weightings:
   ```
   E_Casimir(tau) = (1/2) [Sum_boson |lam| - Sum_fermion |lam|]    [LINEAR]
   V_CW(tau) = Sum_boson lam^4 log(lam^2) - Sum_fermion lam^4 log(lam^2)  [QUARTIC]
   ```

3. **Check for sign change in E_total(tau)**. If E_total changes sign at some tau_c, there is a Casimir-stabilized minimum.

4. **If minimum exists**:
   - Locate tau_0 by interpolation
   - Compute gauge coupling ratio g_1/g_2 = e^{-2*tau_0} at that tau_0
   - Compare to sin^2(theta_W) = 0.2312 -> tau_0 = 0.2994
   - Extract m_{(3,0)}/m_{(0,0)} Dirac eigenvalue ratio at tau_0 -> compare to phi = 1.53158
   - Apply Sagan's three-tier thresholds

5. **If NO minimum**: Record monotonicity direction, curvature at tau=0, and asymptotic behavior.

#### Closure / Proceed Criteria (pre-registered from Sagan, Session 19d)

| Level | Criterion | Bayes Factor | Framework Probability |
|:------|:----------|:-------------|:---------------------|
| **Suggestive** | Robust minimum exists at any tau_0 | BF ~ 3-5 | ~55% |
| **Compelling** | tau_0 in [0.15, 0.30] AND gauge coupling match within 20% | BF ~ 10-30 | 60-70% |
| **Decisive** | All above PLUS phi mass ratio within 1% | BF ~ 100+ | >75% |
| **CLOSED** | No minimum at any tau. E_total monotonically decreasing with TT | — | Perturbative spectral mechanisms CLOSED |

#### Deliverable
- Plot: E_total(tau) with all four towers, both weightings
- Table: E_scalar, E_vector, E_TT, E_Dirac, E_total at 21 tau-values
- VERDICT: CLOSED/Suggestive/Compelling/Decisive with Bayes factor
- If minimum: tau_0, g_1/g_2, phi-ratio, Sagan threshold met

**Write all to**: `tier0-computation/l20b_lichnerowicz_sweep.py`

---

# IV. DECISION GATE

| Result | Interpretation | Next Step |
|:-------|:--------------|:----------|
| E_total has minimum, tau_0 in [0.15, 0.30] | Framework ALIVE. Shape stabilization works. | Extract mass spectrum at tau_0 (Session 21). Gauge couplings. Paper revision. |
| E_total has minimum, tau_0 outside [0.15, 0.30] | Stabilization works but physical predictions may not match SM. | Check gauge couplings, mass ratios at actual tau_0. May still be viable. |
| E_total monotonically decreasing (CLOSED) | All perturbative spectral mechanisms exhausted. | Non-perturbative routes only: Pfaffian (topological), instantons, flux corrections, lattice SU(3). |
| E_total has minimum but only with fine-tuned cutoff | Technically OPEN but naturalness fails. | Evaluate fine-tuning severity. Likely framework-threatening. |

---

# V. SUCCESS CRITERIA

- [ ] L-1: Lichnerowicz operator assembled + validated at tau=0
- [ ] L-2: TT eigenvalues at 21 tau-values + phonon band structure plot
- [ ] L-3: E_total(tau) with all 4 towers + minimum search + Sagan verdict
- [ ] Data saved for Session 20c synthesis

**3 deliverables from 2 agents in 2-3 days.** Sequential pipeline.

All scripts in `tier0-computation/`. Environment: `phonon-exflation-sim/.venv312/Scripts/python.exe`.

---

# VI. WHAT THIS SESSION DOES NOT COVER

| Item | Session | Status |
|:-----|:--------|:-------|
| Seeley-DeWitt fast gate (analytic) | 20a | Prerequisite (provides R_{abcd}) |
| Synthesis + hanging task triage | 20c | After 20a + 20b results |
| Mass spectrum extraction at tau_0 | 21+ | After tau_0 is determined |
| D_total Pfaffian | 21+ | Needs 19c eigenvectors |
| Spectral back-reaction simulation | 21+ | Needs eigenvectors + coupling matrix |
| Neutrino mass predictions | 21+ | Needs tau_0 + lightest Dirac eigenvalues |
| Paper revision | 21+ | After all computational results |

---

# VII. RELATION TO 20a AND 20c

**From 20a**: This session consumes R_{abcd}(tau) from 20a's R-1 assignment. If 20a's SD-1 found OPEN (opposite signs in da_2/dtau and da_4/dtau), this session provides the independent numerical cross-validation. If SD-1 found CLOSED, this session is the sole remaining path.

**To 20c**: This session's verdict (Closure/Suggestive/Compelling/Decisive) drives the 20c synthesis. If CLOSED, 20c triages non-perturbative routes. If OPEN, 20c plans Session 21 (mass extraction, gauge couplings, paper revision).

---

*"SU(3) at large s becomes product-like. A TT mode stable at s=0 could cross the DNP instability threshold at finite s — that crossing point is the natural vacuum selection."* — KK-theorist (Session 19d)

*"We computed the atmospheric compression while ignoring the spherical shell. Twenty-seven drums were silent."* — Tesla-Resonance (Session 19d)
