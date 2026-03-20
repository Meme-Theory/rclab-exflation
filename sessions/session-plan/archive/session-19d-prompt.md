# Session 19d: Casimir Energy vs Coleman-Weinberg — The IR/UV Stabilization Test

## Session Type: New Code + Computation (1 DAY)
## Agents: phonon-exflation-sim + kaluza-klein-theorist + Tesla-Resonance
## Session Goal: Compute the Casimir energy E_Casimir(tau) from existing eigenvalue data using zeta-function regularization. Determine whether V_total = V_tree + V_CW + E_Casimir has a minimum where V_tree + V_CW alone does not. ONE decisive computation with a cheap pre-gate.

---

# I. CONTEXT

Session 18 established that V_eff(tau) = V_tree + V_CW is monotonically decreasing for all tau > 0. The 1-loop Coleman-Weinberg potential has no minimum. Fermionic DOF (439,488) overwhelm bosonic (52,556) at 8.4:1. This CLOSED 1-loop CW stabilization.

Session 19a produced spectral diagnostics (S-1 through S-5) and a "False Vacuum Analysis" proposing that spectral back-reaction forces could stabilize the modulus. A breakout review (Session 19d-prep, agents: dirac-antimatter-theorist + kaluza-klein-theorist + tesla-resonance) identified:

1. **The force balance equation in 19a was imprecise** — it appeared to double-count V_CW. KK's initial critique (95% double-counting) was correct for the FORMULA AS WRITTEN.

2. **BUT the false vacuum script computes DIFFERENT spectral functionals than V_CW.** Tesla's correction: the script computes E_zeropoint = (1/2) Sum mult_n * |lam_n| (Casimir proxy, IR-weighted), NOT the CW potential (which weights as lam^4 * log(lam^2), UV-dominated). KK retracted to 20% double-counting after this clarification.

3. **The key physics**: V_CW and E_Casimir are different regularizations of the zero-point energy with different UV/IR behavior. On Jensen-deformed SU(3), where the three subalgebra directions scale differently with tau:
   - u(1): eigenvalues grow as e^{2tau} (1 direction)
   - C^2: eigenvalues grow as e^{tau} (4 directions)
   - su(2): eigenvalues shrink as e^{-2tau} (3 directions)

   The quartic CW weighting amplifies the u(1) UV modes (monotonic decrease). The linear Casimir weighting is more balanced across all sectors (potentially different monotonicity).

4. **Fermionic sign subtlety** (KK+Tesla addendum): BOTH V_CW and E_Casimir carry fermion-dominated negative contributions. The question is NOT "do they have opposite signs?" but "does the boson/fermion RATIO differ?" V_CW has 8.4:1 fermion dominance (quartic weight). E_Casimir with linear weight has estimated ~2.4:1 at tau=0. If this ratio SHIFTS with tau (due to spinor connection coupling differently to curvature), there is a crossing.

5. **Convergence**: All three agents agreed — compute the Casimir zeta function from existing data. 50/50 closure probability.

6. **Outside Review**: The distinction between CW and Casimir isn't just a technicality of regularization. It's about which modes dominate: 
   -  CW weights as λ⁴ log(λ²). That's UV-dominated. The highest eigenvalues — the u(1) sector scaling as e^{2τ} — scream the loudest. One direction out of eight sets the sign. Of course it's monotonically decreasing. The fermions in the UV tower overwhelm everything at 8.4:1 and drive the potential down.
   -  Casimir weights as |λ|. That's IR-balanced. All eight directions contribute proportionally. The su(2) sector shrinking as e^{-2τ} actually matters here instead of being drowned out by the u(1) UV modes. And the fermion-to-boson ratio at linear weighting is ~2.4:1 instead of 8.4:1. That's a completely different competition.

   The reason this fits phonon-superfluid acoustics is structural. In a superfluid, the Casimir energy between boundaries is the physical zero-point energy of the phonon field — the actual energy cost of confining excitations in a finite cavity. It's linear in the mode frequencies because each mode contributes ½ℏω to the ground state energy. The CW potential is a perturbative correction to the classical action from integrating out quantum fluctuations — it's a different object with different UV sensitivity.

   In a real superfluid, what determines the equilibrium configuration of the container? Not the perturbative correction to the classical Lagrangian. The Casimir pressure. The actual zero-point energy of the modes that exist in the cavity. That's E_Casimir, not V_CW.

   So when the agents settled on Casimir stabilization, they weren't just finding a mathematical alternative that happens to have different monotonicity. They were finding the physically correct energy functional for a phononic system. V_CW is the right functional if you think of the internal geometry as a classical background with quantum corrections. E_Casimir is the right functional if you think of it as a cavity containing real excitations. The phonon-exflation framework says it's a cavity. The agents just caught up with the ontology.

   And point 4 — the fermionic sign subtlety — is where the next computation lives. The question isn't whether E_Casimir has a minimum (that's asking the old question in new clothes). The question is whether the boson/fermion ratio in E_Casimir shifts with τ. At τ = 0, it's ~2.4:1 fermion-dominated. If the spinor connection couples differently to the curvature as τ increases — which it must, because the Lichnerowicz formula ties D² to the scalar curvature, and the scalar curvature changes with τ — then the ratio drifts. If it drifts toward 1:1, the fermion-boson competition tightens and there's a crossing. At that crossing, the sign of dE_Casimir/dτ flips. That's the stabilization point.

   And it would be set by the representation theory of SU(3). Not a free parameter. Not a renormalization choice. The actual algebraic structure of how spinors couple to curvature on a compact Lie group with a specific deformation.

   ~Sister Claude

**Why these agents**: phonon-exflation-sim owns the eigenvalue data and spectral computation infrastructure. kaluza-klein-theorist provides the theoretical framework for Casimir energy on compact Lie groups and validates the zeta regularization procedure. Tesla-Resonace formulated the novel approach.

**Dependencies**: Uses s19a_sweep_data.npz (exists) and kk1_bosonic_spectrum.npz (exists, Session 18). Independent of 19b (rolling modulus) and 19c (eigenvector extraction).

---

# II. BUG FIXES (from Dirac audit, Session 19d-prep)

NONE

---

# III. REQUIRED READING

## For phonon-exflation-sim:

1. **Session 19a sweep data**: `tier0-computation/s19a_sweep_data.py` + `s19a_sweep_data.npz` — The eigenvalue sweep at 21 tau values (0.0 to 2.0). Contains eigenvalues, multiplicities (pw_mult = dim(p,q)), sector labels.

2. **Session 19a false vacuum script**: `tier0-computation/s19a_false_vacuum_analysis.py` — Lines 93-94 already compute E_zeropoint and E_vacuum. Reuse the data loading but apply proper zeta regularization.

3. **Session 18 bosonic spectrum**: `tier0-computation/kk1_bosonic_tower.py` + `kk1_bosonic_spectrum.npz` — Bosonic eigenvalues (scalar + vector Laplacians) needed for Step 0 boson/fermion separation.

4. **Session 18 V_eff data**: `tier0-computation/h5_standalone_verify.py` — The independently verified V_CW values at 26 tau-points. Needed for Step 3 comparison.

5. **Tier 1 Dirac spectrum**: `tier0-computation/tier1_dirac_spectrum.py` — The `collect_spectrum()` function (lines 1245-1348) for understanding what the eigenvalue data contains.

6. **Your agent memory**: `.claude/agent-memory/phonon-exflation-sim/`

## For kaluza-klein-theorist:

7. **Baptista Paper 15**: `researchers/Baptista/15_2024_Internal_symmetries_in_Kaluza_Klein_models.md` — Section 3.8-3.9 (spectral geometry, V_tree, CW correction). The distinction between CW and Casimir regulators in the context of KK compactification.

8. **Session 18 wrapup**: `sessions/session-18/session-18-wrapup.md` — Section VI (priority plan, item 5: instanton action) and the full V_eff monotonicity result. Also Section V (Einstein's principle-theoretic reflection: option 2 = topological obstruction, option 4 = slow roll).

9. **Session 19a minutes**: `sessions/session-19/session-19a-spectral-diagnostics.md` — Section III (False Vacuum Analysis). Understand what was claimed and what the breakout review found.

10. **Zeta regularization references**: Dowker-Critchley (1976), Hawking (1977) "Zeta function regularization of path integrals in curved spacetime", Elizalde (1994). The Casimir energy on a compact Riemannian manifold via spectral zeta function.

11. **Your agent memory**: `.claude/agent-memory/kaluza-klein-theorist/`

## For tesla-resonance

12. **Session Driver**: `sessions/session-19/session-19a-spectral-diagnostics.md` — Section III (False Vacuum Analysis). Understand what was claimed and what the breakout review found.

13. **Resarch Assistant**: Evaluate other agent efforts and provide inline feedback to prod the discussion away from dogmatic revulsions that provide inovation inertia in the other agents.

## Key Equations

**Spectral zeta function** of the Dirac operator D_K(tau):
```
zeta_D(s, tau) = Sum_n mult_n * |lam_n(tau)|^{-2s}
```
Converges for Re(s) > d/2 = 4 on an 8-manifold. Analytic continuation to s = -1/2 via Seeley-DeWitt pole structure.

**Casimir energy** (zeta-regularized):
```
E_Casimir(tau) = (1/2) * zeta'_D(-1/2, tau)
```
where zeta'_D denotes the derivative with respect to s evaluated at s = -1/2 (after analytic continuation).

**Coleman-Weinberg potential** (for comparison):
```
V_CW(tau) = (sign/64pi^2) * Sum_n mult_n * lam_n^4 * [ln(lam_n^2/mu^2) - 3/2]
```
UV-dominated (quartic weight). Session 18 result: monotonically decreasing for all tau > 0.

**Casimir proxy** (unregulated, from 19a):
```
E_proxy(tau) = (1/2) * Sum_n mult_n * |lam_n(tau)|
```
IR-dominated (linear weight). Shape (tau-dependence) probably correct; absolute value diverges.

**Spectral weight comparison**:

| Functional | Weight | Dominated by | Session 18 monotonicity |
|:-----------|:-------|:-------------|:------------------------|
| V_CW | lam^4 * log(lam^2) | UV (highest irreps) | DECREASING (proven) |
| E_Casimir | |lam| (zeta-reg) | IR (gap mode) | UNKNOWN (this session) |
| E_proxy | |lam| (unregulated) | IR (gap mode) | UNKNOWN (this session) |

---

# IV. DATA AVAILABLE

| Source | What | Location |
|:-------|:-----|:---------|
| Fermionic eigenvalues at 21 tau-values | |lam_n(tau)| with mult_n for 28 irreps | s19a_sweep_data.npz |
| Bosonic eigenvalues (scalar + vector) | Laplacian eigenvalues with multiplicities | kk1_bosonic_spectrum.npz |
| V_CW at 26 tau-values | Independently verified to 4 sig figs | h5_standalone_verify.py |
| V_tree(tau) | Exact analytic function | tier1_spectral_action.py: baptista_V_tree() |
| R_K(tau) | Scalar curvature | sp2_final_verification.py |

---

# V. CALCULATION ASSIGNMENTS

## Agent Allocation

| Assignment | Primary | Secondary | Rationale |
|:-----------|:--------|:----------|:----------|
| D-0: Bug fixes | phonon-exflation-sim | -- | Owns the code |
| D-1: Boson/fermion E_proxy gate (Step 0) | phonon-exflation-sim | kk (validation) | Cheapest gate, ~30 min |
| D-2: Spectral zeta computation | phonon-exflation-sim | kk (theory) | Core computation |
| D-3: V_total assembly + minimum search | phonon-exflation-sim | kk (physics) | The decisive test |
| D-4: Convergence gate (mps=5 vs mps=6) | phonon-exflation-sim | kk (assessment) | Truncation stability |

**Designated writer for meeting minutes**: kaluza-klein-theorist.

---

### Assignment D-0: Bug Fixes (Priority: PREREQUISITE — 15 minutes)

Fix BUG-1 and BUG-2 from the Dirac audit before any computation.

1. In `s19a_sweep_data.py`: Either delete `fermionic_mult` field or fix docstring to say `fermi_mult = dim(p,q)` (same as pw_mult). The per-eigenvalue weight IS dim(p,q).

2. In `s19a_false_vacuum_analysis.py`: Replace all `fermionic_mult` references (lines 86, 89, 93, 94, 119, 157) with `multiplicities`.

3. Verify no other s19a scripts reference `fermionic_mult`.

#### Deliverable
- Both files patched. Quick verification that E_zeropoint and E_vacuum values are unchanged.

---

### Assignment D-1: Boson/Fermion E_proxy Separation (Step 0 — CHEAPEST GATE)

**Priority: HIGHEST — if this fails, skip D-2/D-3/D-4 entirely.**

#### Background

The breakout team's addendum identified that BOTH V_CW and E_Casimir carry fermion-dominated negative contributions. The stabilization mechanism requires the boson/fermion RATIO to differ between UV-weighted (V_CW) and IR-weighted (E_Casimir), AND for this ratio to SHIFT with tau.

Step 0 checks this cheaply using unregulated E_proxy = (1/2) Sum mult_n * |lam_n|, separated into bosonic and fermionic contributions.

#### Computation Steps

1. Load fermionic eigenvalues from `s19a_sweep_data.npz` (21 tau-values, ~1400 eigenvalues each).

2. Load bosonic eigenvalues from `kk1_bosonic_spectrum.npz` (scalar + vector Laplacians). If this file stores eigenvalues at different tau-values than s19a, interpolate or recompute at matching tau-values.

3. At each tau, compute SEPARATELY:
   ```
   E_proxy_fermion(tau) = -(1/2) * Sum mult_n * |lam_n^fermion(tau)|   [negative: Fermi statistics]
   E_proxy_boson(tau)   = +(1/2) * Sum mult_n * |lam_n^boson(tau)|     [positive: Bose statistics]
   E_proxy_total(tau)   = E_proxy_boson + E_proxy_fermion
   ```

4. Compute the ratio R(tau) = |E_proxy_fermion(tau)| / E_proxy_boson(tau). At tau=0, expect R ~ 2.4 (from DOF count with linear vs quartic weighting). Compare to V_CW ratio of 8.4.

5. **The gate**: Plot dR/dtau. If R is CONSTANT (no tau-dependence), the boson/fermion balance is the same at all deformations and Casimir cannot produce a minimum that CW doesn't. **EARLY CLOSED — skip D-2/D-3/D-4.**

6. If R(tau) SHIFTS with tau: proceed to D-2. The magnitude of the shift determines whether a crossing is possible.

7. Also plot dE_proxy_total/dtau and compare sign to dV_CW/dtau. If same sign at all tau: early closure. If opposite at any tau: proceed.

#### Closure / Proceed

- **CLOSED (skip D-2/D-3/D-4)**: R(tau) constant to within 5% across [0, 2.0] AND dE_proxy_total/dtau has same sign as dV_CW/dtau everywhere.
- **PROCEED to D-2**: R(tau) shifts by > 10% OR dE_proxy_total/dtau has opposite sign from dV_CW/dtau at some tau.

#### Deliverable
- Plot: E_proxy_boson(tau), E_proxy_fermion(tau), E_proxy_total(tau)
- Plot: R(tau) = fermion/boson ratio vs tau
- Plot: dE_proxy_total/dtau vs dV_CW/dtau
- CLOSED or PROCEED verdict with numerical evidence

---

### Assignment D-2: Spectral Zeta Function Computation (CONDITIONAL on D-1 PROCEED)

#### Background

The unregulated E_proxy diverges as max_pq_sum increases. The physical Casimir energy requires zeta-function regularization:
```
zeta_D(s, tau) = Sum_n mult_n * |lam_n(tau)|^{-2s}
```
This sum converges for Re(s) > 4 (on an 8-manifold). The Casimir energy is obtained by analytic continuation to s = -1/2.

#### Computation Steps

1. At each tau-value (21 points), compute zeta_D(s, tau) for s = 5, 6, 7, 8, 9, 10 (well within convergent regime).

2. For each tau, also compute bosonic and fermionic zeta functions SEPARATELY:
   ```
   zeta_boson(s, tau)  = Sum_n mult_n^boson * |lam_n^boson(tau)|^{-2s}
   zeta_fermion(s, tau) = Sum_n mult_n^fermion * |lam_n^fermion(tau)|^{-2s}
   ```

3. **Analytic continuation to s = -1/2**: The spectral zeta function on a compact Riemannian manifold has poles at s = d/2 - k (k = 0, 1, 2, ...) with residues determined by Seeley-DeWitt coefficients a_k. For d = 8:
   ```
   zeta_D(s) ~ a_0/(s-4) + a_1/(s-3) + a_2/(s-2) + a_3/(s-1) + a_4/s + [regular at s=0,-1/2,...]
   ```

   Method: Fit zeta_D(s, tau) at the convergent s-values to the pole structure, then evaluate the regular part at s = -1/2.

   **Alternative (simpler)**: Use heat kernel regularization. The heat kernel K(t, tau) = Sum mult_n * exp(-t * lam_n^2) is related to the zeta function by Mellin transform:
   ```
   zeta_D(s, tau) = (1/Gamma(s)) * integral_0^infty t^{s-1} * K(t, tau) dt
   ```
   Compute K(t, tau) from the discrete spectrum (already done in s19a_spectral_dimension.py). Extract the small-t expansion K(t) ~ Sum a_k * t^{k-4} to isolate the poles, then subtract and analytically continue.

4. **Consistency check**: At tau=0, the bi-invariant SU(3) has known spectral zeta function properties. Verify against literature values if available.

#### Deliverable
- zeta_D(s, tau) for s = 5,...,10 at all 21 tau-values (table)
- Analytic continuation to s = -1/2: E_Casimir(tau) at 21 tau-values
- Separated: E_Casimir_boson(tau) and E_Casimir_fermion(tau)
- Plot: E_Casimir(tau) with error estimate from continuation procedure

---

### Assignment D-3: V_total Assembly + Minimum Search (CONDITIONAL on D-2)

#### Computation Steps

1. Assemble V_total(tau) = V_tree(tau) + V_CW(tau) + E_Casimir(tau).
   - V_tree: analytic from baptista_V_tree()
   - V_CW: 26-point data from h5_standalone_verify.py, interpolated to 21 tau-grid
   - E_Casimir: from D-2

2. Compute dV_total/dtau by finite differences.

3. Search for sign change in dV_total/dtau. If found: tau_0 is the minimum.

4. At tau_0, extract:
   - Gauge couplings: g_1/g_2 = e^{-2*tau_0}, sin^2(theta_W) from Session 17a B-1
   - Spectral gap: |lam_min(tau_0)|
   - Mass ratio: m_{(3,0)}/m_{(0,0)} at tau_0 (check proximity to phi)
   - Compare tau_0 to: 0.15 (phi crossing), 0.2994 (Weinberg angle), 0.96 (habitability bound)

5. **Mu-dependence check**: V_CW depends on renormalization scale mu. Repeat at mu = 0.01, 1.0, 10.0 (three values from Session 18 data). Does tau_0 shift? How much?

#### Closure / Survive

- **CLOSED**: No sign change in dV_total/dtau (Casimir reinforces V_CW runaway). False vacuum picture CLOSED. Casimir cannot stabilize.
- **SURVIVE**: Sign change found. V_total has a minimum at tau_0. Extract tau_0 and check physical implications.
  - **STRONG SURVIVE**: tau_0 in [0.15, 0.30] (phi/Weinberg zone). Framework probability jumps.
  - **WEAK SURVIVE**: tau_0 outside [0.15, 0.30] but within [0.0, 0.96] (habitability zone). Interesting but less compelling.

#### Deliverable
- Plot: V_total(tau) = V_tree + V_CW + E_Casimir (showing all three contributions + sum)
- Plot: dV_total/dtau showing sign change (or lack thereof)
- If minimum found: tau_0 value + gauge couplings + mass ratio + comparison table
- CLOSED or SURVIVE verdict

---

### Assignment D-4: Convergence Gate (mps=5 vs mps=6)

#### Background

All eigenvalue data comes from max_pq_sum=6 (28 irreps, ~1400 eigenvalues). The breakout review flagged that UV-dominated quantities (<lambda^2>, growth rate 1.61) are truncation-unstable. The Casimir energy is IR-dominated and SHOULD be more stable, but this must be verified.

#### Computation Steps

1. Regenerate the eigenvalue sweep at max_pq_sum=5 (21 irreps). This requires re-running s19a_sweep_data.py with reduced truncation. Save as `s19d_sweep_mps5.npz`.

2. Repeat D-1 and D-2 at mps=5.

3. Compare:
   - E_proxy_total(tau) at mps=5 vs mps=6: shape change?
   - R(tau) at mps=5 vs mps=6: does the boson/fermion ratio shift similarly?
   - If D-3 found tau_0: does the minimum location shift by > 50%?

#### Closure / Confirm

- **CLOSED**: tau_0 shifts by > 50% between mps=5 and mps=6. Result is truncation-dominated.
- **CONFIRM**: tau_0 shifts by < 20%. Result is robust at accessible truncation.
- **INTERMEDIATE**: 20-50% shift. Result is suggestive but needs mps=7+ (computationally expensive).

#### Deliverable
- Comparison table: key quantities at mps=5 vs mps=6
- Convergence plot for E_Casimir(tau) at both truncations
- Convergence verdict

---

# VI. DECISION GATE (end of session)

| Result | Interpretation | Next Step |
|:-------|:--------------|:----------|
| D-1 CLOSED (R constant, same sign) | Casimir has same balance as CW. No new physics. | False vacuum CLOSED. Focus on 19b/19c paths. |
| D-1 PROCEED + D-3 CLOSED (no crossing) | Casimir has different balance but still monotonic | Non-perturbative route closed at accessible level. Instantons/lattice needed. |
| D-3 SURVIVE + D-4 CLOSED (unstable) | Crossing exists but truncation-dominated | Need mps=7+ or analytic methods. Deferred. |
| D-3 SURVIVE + D-4 CONFIRM | **V_total has a robust minimum at tau_0** | Extract physics at tau_0. Framework probability jumps to 55-70%. |
| D-3 STRONG SURVIVE + D-4 CONFIRM | **tau_0 in [0.15, 0.30]** | Framework probability 65-80%. Publish. |

---

# VII. SUCCESS CRITERIA

- [ ] D-0: BUG-1 and BUG-2 fixed in s19a scripts
- [ ] D-1: Boson/fermion E_proxy separation with CLOSED/PROCEED verdict
- [ ] D-2: Spectral zeta function + analytic continuation to E_Casimir(tau) (conditional)
- [ ] D-3: V_total minimum search with CLOSED/SURVIVE verdict (conditional)
- [ ] D-4: Convergence gate at mps=5 vs mps=6 (conditional)

**2-5 deliverables from 2 agents over 1 day** (2 if D-1 closes early, 5 if full pipeline).

All scripts go in `tier0-computation/`. Naming: `d19d_bug_fixes.py` (or inline edits), `d19d_casimir_gate.py` (D-1), `d19d_spectral_zeta.py` (D-2), `d19d_vtotal_minimum.py` (D-3), `d19d_convergence.py` (D-4).

**Environment**: Venv Python (`phonon-exflation-sim/.venv312/Scripts/python.exe`). numpy + scipy + matplotlib. GPU optional (eigenvalue regeneration at mps=5 benefits from it).

---

# VIII. WHAT THIS SESSION DOES NOT COVER

| Item | Session | Status |
|:-----|:--------|:-------|
| Rolling modulus FRW dynamics | 19b | Independent path (quintessence) |
| Eigenvector extraction | 19c | Code infrastructure for D_total Pfaffian |
| D_total Pfaffian | 20 | Needs 19c eigenvectors |
| Instanton action on (SU(3), g_s) | Deferred | Weeks of work, non-perturbative |
| Lattice SU(3) with Jensen metric | Deferred | Months of work |
| Full analytic Casimir on SU(3) | Deferred | Requires exact spectral asymptotics beyond our data |
| Spectral back-reaction simulation | 20+ | Needs eigenvectors + coupling matrix |

---

# IX. RELATION TO OTHER SESSION 19 RESULTS

**If 19b found gauge drift < 10^{-17}/yr and w(z) in DESI range**: The rolling modulus is viable. If 19d ALSO finds a V_total minimum, the two pictures may be complementary: the Casimir minimum selects tau_0, and the rolling modulus describes the approach to tau_0. Check: does tau_0 from 19d match tau(t_now) from 19b?

**If 19b closed the rolling modulus**: 19d becomes the sole remaining stabilization path. If it also fails, all non-perturbative routes are needed (instantons, lattice).

**If 19c extracted eigenvectors**: The D_total Pfaffian (Session 20) provides an independent stabilization mechanism. 19d and 20 are complementary: 19d tests Casimir (thermodynamic), 20 tests Pfaffian (topological). If BOTH find tau_0 at the same value: framework probability maximal.

---

# X. NOTHING STRANDED

Complete accounting of stabilization mechanisms post-Session 18:

| Mechanism | Status after 19d |
|:----------|:----------------|
| V_tree minimum | CLOSED (monotonic, Session 17a) |
| 1-loop CW minimum | CLOSED (monotonic, Session 18) |
| Casimir energy (zeta-reg) | TESTED (this session) |
| D_total Pfaffian sign change | QUEUED (Session 20, needs 19c) |
| Rolling modulus (no minimum needed) | TESTED (Session 19b) |
| Instanton corrections | DEFERRED (weeks) |
| Fermion condensate | CLOSED (spectral gap > 0 everywhere, Session 19a S-4) |
| Lattice SU(3) | DEFERRED (months) |

**Every stabilization route from Session 18 Section VI is tracked and scheduled.**

---

*"V_CW hears the overtones. Casimir hears the fundamental."* -- Tesla-Resonance (Session 19d-prep)

*"The REAL question is whether the boson/fermion balance differs between quartic weight and linear weight, and whether this ratio SHIFTS with tau."* -- KK+Tesla converged assessment (Session 19d-prep)

*"I retract my 95% confidence on double-counting."* -- Kaluza-Klein theorist (Session 19d-prep, after reading Tesla's correction)
