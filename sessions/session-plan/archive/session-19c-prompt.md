# Session 19c: Eigenvector Infrastructure + Synthesis + Session 20 Gate

## Session Type: Code Infrastructure + Results Synthesis (1-2 DAYS)
## Agents: phonon-exflation-sim + connes-ncg-theorist
## Session Goal: (1) Modify collect_spectrum() to return eigenvectors — the dual-purpose gate for Session 20. (2) Synthesize 19a + 19b results into a convergence assessment. (3) Plan Session 20 (D_total Pfaffian OR spectral back-reaction simulation, depending on 19a/19b outcomes).

---

# I. CONTEXT

Sessions 19a and 19b tested two independent hypotheses about the monotonic V_eff:

**Path A (19a)**: Spectral complexity diagnostics — level statistics q(tau), spectral dimension d_s(tau, sigma), entropy production dS/dtau, heat capacity C(tau), complexity functional Omega(tau). Agents: phonon-exflation-sim + tesla-resonance.

**Path B (19b)**: Rolling modulus cosmology — coupled (sigma, tau) FRW dynamics, gauge coupling drift, w(z) vs DESI. Agents: baptista-spacetime-analyst + einstein-theorist.

**This session** builds the infrastructure that BOTH surviving paths need going forward, synthesizes all results, and plans Session 20.

**Why these agents**: phonon-exflation-sim owns the eigenvalue code (tier1_dirac_spectrum.py) and will modify collect_spectrum() for eigenvector extraction. connes-ncg-theorist brings NCG spectral triple expertise essential for the D_total Pfaffian route — understanding how D_F(s) is constructed from D_K eigenvectors, how the order-one condition works, and what the Pfaffian sign change physically means in the NCG framework.

---

# II. REQUIRED READING

## For phonon-exflation-sim:

1. **tier1_dirac_spectrum.py**: `tier0-computation/tier1_dirac_spectrum.py` — The main eigenvalue infrastructure. Focus on collect_spectrum() — currently calls np.linalg.eigh and DISCARDS eigenvectors. Your task is to make eigenvector return optional.

2. **Session 18 wrapup, Section XI**: `sessions/session-18/session-18-wrapup.md` (lines 401-416) — Einstein's recommendation for Session 19: eigenvector extraction, Yukawa integrals, D_F(s) assembly, Pfaffian phase diagram.

3. **Session 19 primer, Section VI item 6**: `sessions/session-19/session-19-primer.md` — Eigenvector extraction identified as dual-purpose gate.

4. **Session 19a results**: Check `tier0-computation/s19a_*.py` output — what did the spectral diagnostics find?

5. **Your agent memory**: `.claude/agent-memory/phonon-exflation-sim/`

## For connes-ncg-theorist:

6. **Session 18 wrapup, Sections III + XI**: `sessions/session-18/session-18-wrapup.md` — Candidate 1 (Pfaffian topological pinning): D_K Pfaffian is trivial (Dirac's theorem), but D_total = D_K + D_F remains open. Section XI recommends D_total Pfaffian as highest priority.

7. **Sessions 7-10 computation notes**: `sessions/` (Sessions 8-10) — The NCG spectral triple structure: KO-dimension 6, C^32, R_{u(2)}, commutant analysis, order-one condition.

8. **Baptista Paper 17**: `researchers/Baptista/17_2025_Dirac_operators_on_compact_Lie_groups.md` — Corollary 3.4 / eq 3.8 (D_K decomposition), eq 4.1 (Kosmann-Lichnerowicz derivative). The explicit D_K is needed to construct D_F.

9. **Baptista Paper 18**: `researchers/Baptista/18_2026_Spectral_geometry_from_compact_Lie_groups.md` — Appendix E (Z_3 generations), the full spectral geometry construction.

10. **Session 19b results**: Check `tier0-computation/r19b_*.py` output — what did the rolling modulus find?

11. **Your agent memory**: `.claude/agent-memory/connes-ncg-theorist/`

---

# III. CALCULATION ASSIGNMENTS

## Agent Allocation

| Assignment | Primary | Secondary | Rationale |
|:-----------|:--------|:----------|:----------|
| E-1: Eigenvector extraction | phonon-exflation-sim | — | Owns the code |
| E-2: Eigenvector validation | phonon-exflation-sim | connes (cross-check) | Orthonormality, sector purity at tau=0 |
| E-3: D_F construction roadmap | connes-ncg-theorist | phonon-exflation-sim (feasibility) | NCG theory for Pfaffian route |
| E-4: 19a + 19b synthesis | Both | — | Joint assessment |
| E-5: Session 20 plan | Both | — | Joint planning |

---

### Assignment E-1: Eigenvector Extraction (Priority: HIGHEST — gates Session 20)

#### Background

collect_spectrum() in tier1_dirac_spectrum.py currently:
1. Builds the Dirac matrix D_{(p,q)} for each irrep sector
2. Calls eigenvalues = np.linalg.eigh(D_matrix) (or equivalent)
3. Returns eigenvalues with sector labels and multiplicities
4. **DISCARDS eigenvectors**

The eigenvectors are needed for:
- **D_total Pfaffian**: Yukawa integrals M_{alpha,beta}^a = <phi_alpha | (L_{e_a} + div/2) | phi_beta> require explicit eigenvectors phi_alpha.
- **Participation ratio**: PR_n = (Sum |c_n^{(p,q)}|^2)^2 / (Sum |c_n^{(p,q)}|^4) requires eigenspinor projections onto sectors.
- **Spectral back-reaction simulation** (Primer Section IX): Coupling matrix elements and Landau-Zener transitions need eigenvector overlaps.

#### Modification

1. Add parameter `return_eigenvectors=False` to collect_spectrum().

2. When True, np.linalg.eigh returns (eigenvalues, eigenvectors). Store both.

3. Return format:
   ```python
   if return_eigenvectors:
       return eigenvalues, sector_labels, multiplicities, eigenvectors_dict
   else:
       return eigenvalues, sector_labels, multiplicities
   ```
   where eigenvectors_dict[(p,q)] is the matrix of eigenvectors for that sector.

4. **Memory consideration**: At max_pq_sum=6, the largest matrix is 448x448 (sector (6,0)). The full eigenvector set across 28 sectors is ~20 MB. Trivial.

5. **Backward compatibility**: Default return_eigenvectors=False preserves all existing call sites.

#### Deliverable
- Modified collect_spectrum() with eigenvector return
- Modified sweep_s() to optionally propagate eigenvector return
- Script `e19c_eigenvector_test.py` that validates the modification

---

### Assignment E-2: Eigenvector Validation (Priority: HIGH)

#### Validation Tests

1. **Orthonormality**: For each sector (p,q), verify V^T V = I (or V^H V = I) to machine epsilon.

2. **Reconstruction**: D_{(p,q)} V = V Lambda (eigenvalue equation). Verify ||D V - V Lambda|| < 10^{-12}.

3. **Sector purity at tau=0**: At the bi-invariant point, eigenvectors should be block-diagonal in the su(3) Casimir basis. Each eigenvector should be localized in a single sub-block. Compute participation ratio PR at tau=0. Expected: PR ~ 1 (sector-pure).

4. **Sector mixing at tau>0**: At tau=1.0, compute participation ratio PR. Expected: PR > 1 for modes near avoided crossings.

5. **J-compatibility**: Verify that J maps eigenvector phi_n to the eigenvector with eigenvalue -lambda_n (the CPT partner). This is the eigenvector-level version of the D-1 check from Session 17a.

#### Deliverable
- Validation report: orthonormality error, reconstruction error, PR at tau=0 and tau=1.0
- J-compatibility of eigenvectors: max error

---

### Assignment E-3: D_F Construction Roadmap (Priority: MEDIUM — planning for Session 20)

connes-ncg-theorist provides the theoretical roadmap for constructing D_F(s) from the eigenvectors.

#### Questions to Answer

1. **What IS D_F in this framework?** D_total = D_K + D_F. The finite Dirac operator D_F acts on C^32 and encodes Yukawa couplings. In Connes' NCG, D_F is a 32x32 matrix (or block structure on generations). How does it relate to Baptista's coupling matrix elements M_{alpha,beta}^a from Paper 17?

2. **How does D_F depend on tau?** D_F is constructed from inter-sector coupling integrals that involve D_K eigenvectors. As tau changes, the eigenvectors rotate, so D_F(tau) inherits tau-dependence. Spell out the explicit construction:
   ```
   D_F(tau)_{alpha,beta} = Sum_a <phi_alpha(tau) | L_{e_a} + div(e_a)/2 | phi_beta(tau)>
   ```
   summed over non-Killing C^2 directions e_a (which generate Yukawa couplings).

3. **What is the Pfaffian we're computing?** sgn(Pf(J * D_total(tau))) where D_total = D_K(tau) + D_F(tau) acts on the full Hilbert space. Clarify:
   - What are the dimensions? D_K acts on L^2(K, S_K) (infinite-dimensional, truncated to ~1400 eigenvalues). D_F acts on C^32. D_total acts on L^2(K, S_K) tensor C^32 — but projected onto a FINITE subspace for computation.
   - Which finite subspace? The lowest N eigenvalues of D_K, tensorially combined with C^32. The Pfaffian is then of a 32N x 32N antisymmetric matrix.
   - How does truncation affect the Pfaffian sign? Is the sign stable as N increases?

4. **Order-one condition**: Does D_F need to satisfy [[D_F, a], b^0] = 0 for a in A_F? Sessions 7-10 showed that the order-one condition with toy D_F fails. Baptista's D_K provides the physical D_F. Does the construction in (2) automatically satisfy order-one?

5. **Estimated effort**: How many lines of new code? What are the mathematical obstacles?

#### Deliverable
- Written roadmap (1-2 pages) for D_total Pfaffian construction
- Explicit formula for D_F(tau) in terms of eigenvectors and KL derivative
- Dimension and structure of the Pfaffian matrix
- Estimated effort for Session 20
- Identified mathematical obstacles or potential failure modes

---

### Assignment E-4: 19a + 19b Synthesis (Priority: HIGH)

**Requires 19a and 19b results.**

#### Synthesis Questions

1. **Convergence check**: If 19a found tau_c and 19b found tau(t_now), do they agree?

   | Source | tau value | Session |
   |:-------|:---------|:--------|
   | Level statistics inflection tau_c | ? | 19a S-1 |
   | Spectral dimension d_s=4 crossing | ? | 19a S-2 |
   | Entropy production maximum | ? | 19a S-3 |
   | FRW solution tau(t_now) | ? | 19b R-2 |
   | Gauge coupling (Weinberg angle) | 0.2994 | 17a B-1 |
   | Mass ratio phi | 0.15 | Session 12 |

   How many independently-determined tau values agree?

2. **Compatibility**: Can Path A (spectral phase) and Path B (rolling modulus) be simultaneously true? If tau is rolling slowly near a spectral phase transition, the two pictures complement each other: the spectral transition explains WHY the universe has the particle spectrum it does, and the rolling modulus explains the dark energy.

3. **Constraint Conditions**: Which paths survived? Which are closed?

4. **Updated framework probability**: Based on all Session 19 results.

#### Deliverable
- Convergence table (all tau values from all sources)
- Compatibility assessment of Paths A and B
- Updated framework probability with rationale

---

### Assignment E-5: Session 20 Plan (Priority: MEDIUM)

Based on 19a/19b/19c results, draft the Session 20 plan.

#### Decision Tree

**If Path A (spectral complexity) succeeded AND Path B (rolling modulus) passed gauge drift**:
- Session 20: D_total Pfaffian (using E-1 eigenvectors). If sign changes, framework probability 65-80%.
- Parallel: Spectral back-reaction simulation (Primer Section IX) using eigenvectors + coupling matrix.

**If Path A succeeded BUT Path B failed (gauge drift too fast)**:
- Session 20: D_total Pfaffian (critical). Rolling modulus closed, but spectral phase transition still valid.
- The vacuum is at tau_c, selected by spectral complexity. No ongoing rolling needed.

**If Path A failed BUT Path B passed**:
- Session 20: D_total Pfaffian (sole remaining route to parameter-free vacuum selection).
- Rolling modulus provides dynamics but doesn't select tau_0 algebraically.

**If both failed**:
- Session 20: D_total Pfaffian (last resort, ~40% success probability).
- If Pfaffian also fails: framework kinematics intact, dynamics exhausted at accessible level. Non-perturbative physics (instantons, lattice) required.

#### Deliverable
- Session 20 plan: agent selection, deliverables, effort estimate
- Decision tree with probability branches

---

# IV. DECISION GATE

This session's primary output is INFRASTRUCTURE (E-1, E-2) and PLANNING (E-3, E-4, E-5). The decision gate is:

| Result | Action |
|:-------|:-------|
| Eigenvectors extracted and validated | Session 20 can proceed with D_total Pfaffian |
| Eigenvectors have numerical issues | Debug before Session 20 |
| D_F roadmap reveals fundamental obstacle | Reassess Pfaffian route |
| 19a + 19b convergence at tau ~ 0.15-0.30 | Framework probability highest. Pfaffian becomes confirmation, not rescue. |
| 19a + 19b divergent or both failed | Framework in trouble. Pfaffian is rescue mission. |

---

# V. SUCCESS CRITERIA

- [ ] E-1: collect_spectrum() modified with return_eigenvectors parameter
- [ ] E-2: Eigenvector validation (orthonormality, reconstruction, PR, J-compatibility)
- [ ] E-3: D_total Pfaffian roadmap (formula, dimensions, effort, obstacles)
- [ ] E-4: 19a + 19b convergence table + compatibility assessment + updated probability
- [ ] E-5: Session 20 plan with decision tree

**5 deliverables from 2 agents over 1-2 days.**

All scripts go in `tier0-computation/`. Naming: `e19c_eigenvector_extraction.py`, `e19c_eigenvector_validation.py`.

**Environment**: System Python (`python`). numpy + scipy. No GPU.

---

# VI. WHAT THIS SESSION DOES NOT COVER

| Item | Session | Status |
|:-----|:--------|:-------|
| D_total Pfaffian (full construction) | 20 | Needs E-1 eigenvectors from this session |
| Spectral back-reaction simulation | 20+ | Needs eigenvectors + coupling matrix code |
| Healing length vs C^2 scale | Deferred | Lower priority |
| Instanton action | Long-term | Weeks of work |
| Lattice SU(3) | Long-term | Months of work |

---

# VII. NOTHING STRANDED

Complete accounting of ALL computations from Session 18 wrapup + addendum + Session 19 primer:

| Computation | Status after 19a/b/c |
|:------------|:--------------------|
| Spectral diagnostics (S-1 through S-5) | DONE (19a) |
| V_eff fit + slow-roll (R-1) | DONE (19b) |
| Coupled FRW ODEs (Calc A) | DONE (19b) |
| Gauge coupling drift (Calc B) | DONE (19b) |
| w(z) vs DESI (Calc C) | DONE (19b) |
| Near-zero spectral density | DONE (19a S-4) |
| Eigenvector extraction | DONE (19c E-1) |
| D_total Pfaffian roadmap | DONE (19c E-3) |
| D_total Pfaffian construction | QUEUED (Session 20) |
| Spectral back-reaction simulation | QUEUED (Session 20+) |
| Healing length vs C^2 scale | DEFERRED |
| Instanton action | DEFERRED (weeks) |
| Lattice SU(3) | DEFERRED (months) |

**Every computation from both source documents is tracked and scheduled.**

---

*"The spectral action IS the phonon free energy. This is not analogy — it is identity."* — Hawking (Giants G3)

*"For KO-dim 6 + C^32, valid D_F GUARANTEED TO EXIST."* — Barrett classification (Session 11)

*"The remaining path (D_total Pfaffian) is concrete and testable but uncertain (~40%). If it works, the framework jumps to 65-75%. If it fails, the framework drops to 20-30%."* — Einstein (Session 18 Wrapup)
