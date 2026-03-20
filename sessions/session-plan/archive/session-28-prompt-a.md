# Session 28a: Zero-Cost Diagnostics + Torsionful BCS

**Date**: 2026-02-27
**Depends on**: Session 27 (T-1 PASS, multi-sector BCS), Session 19a (sweep data), Session 25 (spectral action data)
**Input data**:
- `tier0-computation/s19a_sweep_data.npz` (21 tau, 11424 modes -- Bogoliubov source)
- `tier0-computation/s27_torsion_gap_gate.npz` (D_can vs D_K gaps, 21 tau, 4 sectors)
- `tier0-computation/s27_multisector_bcs.npz` (9 sectors, 9 tau, 12 mu)
- `tier0-computation/s23a_kosmann_singlet.npz` (Kosmann matrices, eigenvalues)
- `tier0-computation/s25_landau_results.npz`, `s25_connes_results.npz` (thermal spectral action data)

## Motivation

Session 28a opens with six zero-cost post-processing computations that extract maximum information from existing .npz files, then tackles the single highest-priority new computation identified by the collab review: torsionful BCS. The zero-cost items include the Constraint Chain gateway (KC-1: do Bogoliubov coefficients from the evolving spectrum generate phonon injection?) and five diagnostics that map the landscape before the main computation runs. The torsionful BCS (merged E-4/S-1/L-4) is the computation that 3/4 reviewers independently identified as #1: does the D_can eigenbasis produce M_max > 1 at mu = 0?

---

# 0. OPERATIONAL RULES

## COMPUTATION DISCIPLINE

Every result classified against its pre-registered gate BEFORE any interpretation. Report the number first. Classify second. Interpret third.

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s28a_`

## REQUIRED READING

ALL agents:
1. **Session 27 wrapup**: `sessions/session-27/session-27-wrapup.md` -- T-1 PASS details, multi-sector BCS phase structure, Baptista addenda.
2. **Master collab**: `sessions/session-27/session-27-master-collab.md` -- Sections II (convergent themes), III (Constraint Chain), IV (computation roster).
3. **MathVariables**: `sessions/framework/MathVariables.md` -- Sections 1.4 (contorsion), 2.1 (D_can vs D_K), 4 (BCS variables).
4. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

---

# I. COMPUTATIONS

## Phase 1: Zero-Cost Post-Processing (~30 min total)

### 28a-1: KC-1 Parametric Injection Rate (Bogoliubov Coefficients)

**What**: Compute |beta_k|^2 from the rate of change of Dirac eigenvalues d(lambda_k)/d(tau). This is the Parker particle creation rate on the internal space -- the mechanism by which an evolving Jensen deformation generates phononic excitations. If |beta_k|^2 ~ 0 for all modes, the 1D phonon mechanism has no drive and is CLOSED.

**Input**: `tier0-computation/s19a_sweep_data.npz` -- eigenvalues lambda_k(tau) at 21 tau values for 11424 modes.

**Script**: `s28a_bogoliubov_coefficients.py`

**Method**:
1. Load eigenvalues lambda_k(tau_i) at 21 tau values.
2. Compute omega_k(tau) = |lambda_k(tau)| (mode frequency).
3. Numerical derivative: d(omega_k)/d(tau) via 3-point central difference.
4. Bogoliubov coefficient (adiabatic approximation):
   ```
   |beta_k|^2 ~ (1/(4 * omega_k^2)) * |d(omega_k)/d(tau)|^2 * (d(tau)/dt)^2
   ```
   Report the tau-independent part: B_k(tau) = (1/(4*omega_k^2)) * (d(omega_k)/d(tau))^2.
5. Identify modes with largest B_k. Plot B_k vs omega_k at tau = 0.15, 0.25, 0.35.
6. Compute the total injection rate: Gamma_inject = sum_k B_k(tau) * (multiplicity).

**Output**: `s28a_bogoliubov_coefficients.npz`, `s28a_bogoliubov_coefficients.png`

**Gate KC-1**:
- PASS: B_k > 0.01 for modes near the gap edge at any tau in [0.10, 0.40]
- CLOSED: B_k < 10^{-4} for ALL modes at ALL tau -- no parametric amplification
- INCONCLUSIVE: B_k in [10^{-4}, 0.01] -- marginal injection

**Closure Audit Context (Baptista)**: The Constraint Chain (KC-1 through KC-5) is orthogonal to the connection ambiguity — it tests phonon injection from parametric amplification, not spectral action stabilization. This computation does not directly retest any of the 21 closed mechanisms; it probes a NOVEL mechanism (Parker particle creation on the internal space). The Bogoliubov coefficients B_k depend on d(omega_k)/d(tau) from D_K eigenvalues (s19a data). If 28a-7 shows MAJOR PASS for D_can BCS, KC-1 should be recomputed with D_can eigenvalues since the parametric amplification that matters is in the spectrum where condensation occurs. The eigenvalue evolution rate d(omega)/d(tau) could differ between connections.

**Agent**: phonon-exflation-sim

---

### 28a-2: L-1 Thermal Spectral Action

**What**: Evaluate the finite-temperature spectral action F(tau; beta) = -T * ln Tr exp(-beta * D_K^2 / Lambda^2) using existing eigenvalue data. The perturbative spectral action S[D, f, Lambda] is T=0. The thermal version introduces a Boltzmann weight that suppresses high modes, potentially breaking the Seeley-DeWitt monotonicity and generating a tau minimum.

**Input**: s25 and s27 eigenvalue data. Specifically, the D_K eigenvalues from `s27_multisector_bcs.npz` (which stores eigenvalues per sector) and the full spectrum from `s19a_sweep_data.npz`.

**Script**: `s28a_thermal_spectral_action.py`

**Method**:
1. Load D_K eigenvalues lambda_n(tau) across sectors.
2. For each tau and each temperature T in {0.1, 0.5, 1.0, 2.0, 5.0} (in units of lambda_min(0)):
   ```
   F(tau; T) = -T * sum_n ln(1 + exp(-|lambda_n(tau)|/T))
   ```
   (fermionic partition function for Dirac spectrum).
3. Plot F(tau; T) vs tau at each temperature.
4. Check for non-monotonicity: does F(tau; T) have a minimum at tau > 0 for any T?
5. If minimum found: record tau_min(T), F_min(T), curvature F''(tau_min).

**Output**: `s28a_thermal_spectral_action.npz`, `s28a_thermal_spectral_action.png`

**Gate L-1**:
- PASS: F(tau; T) has a minimum at tau > 0 for some T -- thermal stabilization exists
- CLOSED: F(tau; T) monotonically decreasing at all T -- thermal correction does not help
- INCONCLUSIVE: Minimum exists but is shallow (F'' < 0.01)

**Closure Audit Context (Baptista)**: This computation retests **Closure 19 (V-1: V_spec monotone, Session 24a)** in a fundamentally new way: by adding finite temperature. The T=0 spectral action is monotonically increasing (Closure 19). The thermal Boltzmann suppression of high modes weights the IR spectrum more heavily — exactly the regime where the Baptista audit flags connection-dependence as uncertain (audit §3: "The constant-ratio trap is UV-robust but IR-uncertain"). Also relates to **Closure 5 (Seeley-DeWitt a_2/a_4, Session 20a)**: the Seeley-DeWitt expansion is a T=0 asymptotic series, and thermal corrections introduce new terms not captured by the a_{2k} coefficients. This computation uses D_K eigenvalues; if non-monotonicity is found, repeating with D_can eigenvalues (weaker IR gaps) is the immediate follow-up.

**Agent**: phonon-exflation-sim

---

### 28a-3: E-1 Lichnerowicz Gap Decomposition

**What**: Decompose the spectral gap ratio gap_T/gap_K from Session 27 into the Lichnerowicz components. On a compact Riemannian manifold, D^2 = nabla*nabla + R/4. For D_can (flat connection, nabla_can has zero curvature), D_can^2 = nabla_can*nabla_can. The gap ratio quantifies how much of the Levi-Civita gap comes from the curvature endomorphism R/4.

**Input**: `tier0-computation/s27_torsion_gap_gate.npz`

**Script**: `s28a_lichnerowicz_decomposition.py`

**Method**:
1. Load gap_K(tau) and gap_T(tau) per sector from s27 data.
2. The Lichnerowicz formula gives: gap_K^2 >= R_K/4 (for the LC Dirac).
3. For D_can (flat connection): gap_T = gap from M_Lie alone (no curvature endomorphism).
4. Define: R_contribution(tau) = gap_K^2(tau) - gap_T^2(tau). This isolates the curvature's role.
5. Plot R_contribution(tau) / gap_K^2(tau) per sector -- fraction of gap due to curvature.
6. Cross-check: at tau=0, D_can = M_Lie should give gap_T from pure algebra. Verify against known M_Lie eigenvalues.

**Output**: `s28a_lichnerowicz.npz`, `s28a_lichnerowicz.png`

**Gate**: Diagnostic only. Quantifies how much easier BCS becomes when curvature endomorphism is absent.

**Closure Audit Context (Baptista)**: This diagnostic does not directly retest any specific closure but provides structural context for **Closure 17 (K-1e: BCS at mu=0, Session 23a)** and the torsionful BCS (28a-7). The Lichnerowicz formula D_K^2 = nabla*nabla + R/4 shows the D_K gap has a curvature contribution. For D_can, R/4 is absent (canonical connection is flat): D_can^2 = nabla_can*nabla_can (Casimir). The decomposition quantifies how much of the D_K gap is "curvature padding" that D_can lacks — directly explaining the 33-78% gap weakening from Session 27 T-1. This is the structural reason why Closure 17's 7-13x M_max shortfall might be partially remedied in the torsionful basis.

**Agent**: phonon-exflation-sim

---

### 28a-4: C-1 Spectral Action S_can vs S_LC

**What**: Compute the spectral action Tr f(D_can^2 / Lambda^2) using D_can eigenvalues and compare to Tr f(D_K^2 / Lambda^2). This isolates the torsion contribution to the spectral action at all tau values.

**Input**: `tier0-computation/s27_torsion_gap_gate.npz` (D_can and D_K eigenvalues per sector)

**Script**: `s28a_spectral_action_comparison.py`

**Method**:
1. Load D_can and D_K eigenvalues at 21 tau values, per sector.
2. Compute S_can(tau; Lambda) = sum_n f(lambda_can_n^2 / Lambda^2) with f = step function (count eigenvalues below Lambda).
3. Compute S_LC(tau; Lambda) = sum_n f(lambda_K_n^2 / Lambda^2).
4. Evaluate at Lambda = {1, 2, 5, 10} (in spectral units).
5. Plot S_can(tau) and S_LC(tau) at each Lambda. Compute the difference Delta_S = S_can - S_LC.
6. Key question: is Delta_S(tau) monotonic? Or does it have structure (minimum/maximum)?

**Output**: `s28a_spectral_action_comparison.npz`, `s28a_spectral_action_comparison.png`

**Gate C-1**: Diagnostic. If Delta_S has a minimum at tau > 0, torsion introduces spectral action structure that the LC operator does not have.

**Closure Audit Context (Baptista)**: This computation directly retests **Closure 19 (V-1: V_spec monotone, Session 24a)** and **Closure 5 (Seeley-DeWitt a_2/a_4, Session 20a)**. Both closes used D_K exclusively. The canonical connection is FLAT — the Gilkey curvature-squared terms that produce a_4/a_2 = 1000:1 for D_K are absent for D_can. D_can^2 is not of standard Laplace type (no spin connection contribution), so the Seeley-DeWitt expansion is a different series. If S_can(tau) is non-monotonic, both V-1 and SD-1 closes do NOT transfer to the torsionful sector, and the framework's native stabilization mechanism reopens through a door invisible for 27 sessions. If S_can is also monotonic, both closes are confirmed for both connections and spectral action stabilization is permanently closed. **This is the single most important number Session 28 can produce.**

**Agent**: phonon-exflation-sim

---

### 28a-5: C-4 Spectral Correlation R_2(s)

**What**: Compute the two-point spectral correlation function R_2(s) = <rho(E) rho(E+s)> for the D_can and D_K spectra across sectors. Wigner-Dyson statistics (GUE/GOE) indicate spectral rigidity from quantum chaos; Poisson statistics indicate integrability. A transition between the two as tau varies would signal a spectral phase transition.

**Input**: `tier0-computation/s27_multisector_bcs.npz` (eigenvalues per sector at 9 tau), `tier0-computation/s27_torsion_gap_gate.npz` (D_can eigenvalues)

**Script**: `s28a_spectral_correlations.py`

**Method**:
1. For each sector and each tau: extract the unfolded eigenvalue sequence (subtract smooth part).
2. Compute the nearest-neighbor spacing distribution P(s) and the number variance Sigma^2(L).
3. Fit P(s) to the Brody distribution: P(s) = A * s^q * exp(-c * s^(q+1)). Report q.
4. Compare D_can vs D_K statistics at each tau.
5. Plot P(s) at tau = 0, 0.15, 0.30, 0.50 for both operators.

**Output**: `s28a_spectral_correlations.npz`, `s28a_spectral_correlations.png`

**Gate C-4**: Diagnostic. Wigner-Dyson in D_can but Poisson in D_K at the same tau would indicate torsion induces spectral chaos -- relevant for random matrix theory approaches to NCG.

**Closure Audit Context (Baptista)**: This diagnostic does not directly retest any specific closure. It classifies the spectral statistics (Poisson vs GUE/GOE) for both D_can and D_K, providing structural context for the block-diagonality theorem (Closes 10, 11, 16). The Baptista audit confirms block-diagonality is universal (both connections): inter-sector crossings are always exact. Intra-sector level statistics could differ between connections and reveal whether D_can has stronger eigenvalue repulsion (GUE → avoided crossings, larger Berry curvature) than D_K within sectors, which would affect the BCS coupling landscape.

**Agent**: phonon-exflation-sim

---

### 28a-6: S-2 M_max vs C_2 Dispersion Relation

**What**: Plot the BCS maximum kernel eigenvalue M_max as a function of the quadratic Casimir C_2(p,q) across all 9 sectors, at fixed mu/lambda_min values. This maps the "dispersion relation" of the BCS instability across representations.

**Input**: `tier0-computation/s27_multisector_bcs.npz`

**Script**: `s28a_mmax_dispersion.py`

**Method**:
1. Load M_max(sector, tau, mu) from s27 data.
2. For each sector (p,q), compute C_2 = (p^2 + q^2 + pq + 3p + 3q)/3.
3. At fixed tau = {0.15, 0.30, 0.50} and mu/lambda_min = {0, 0.5, 1.0, 1.2}:
   plot M_max vs C_2 for all 9 sectors.
4. Identify: is M_max monotonically decreasing with C_2? Is there a phonon-like dispersion omega ~ sqrt(C_2)?
5. Mark the M_max = 1 threshold. Which sectors are above/below at each (tau, mu)?

**Output**: `s28a_mmax_dispersion.npz`, `s28a_mmax_dispersion.png`

**Gate S-2**: Diagnostic. A phonon-like dispersion (M_max decreasing with C_2) indicates the BCS instability is strongest for the lowest representations, consistent with the phonon interpretation. An acoustic branch (M_max ~ sqrt(C_2) for small C_2) would be direct evidence of phononic structure.

**Closure Audit Context (Baptista)**: This diagnostic does not directly retest any specific closure but provides structural context for **Closure 17 (K-1e: BCS at mu=0, Session 23a)** by mapping M_max across representations. The quadratic Casimir C_2(p,q) controls the low-lying eigenvalues of D_can (since D_can^2 ~ Casimir), so the dispersion M_max(C_2) in the D_K basis may differ qualitatively from D_can. A phonon-like acoustic branch (M_max decreasing with C_2) would connect the BCS instability to the Constraint Chain's phonon interpretation (KC-1 through KC-5).

**Agent**: phonon-exflation-sim

---

## Phase 2: Torsionful BCS (The Main Event)

### 28a-7: E-4/S-1/L-4 Torsionful BCS Kernel (Merged)

**What**: Redo the BCS gap equation using D_can (canonical/torsionful Dirac operator) eigenvalues instead of D_K (Levi-Civita). Session 27 T-1 showed gap_T / gap_K ranges from 0.22 to 0.67 -- the torsionful gap is 33-78% weaker. This directly increases M_max = V / (2 * delta_lambda) because delta_lambda is smaller. The decisive question: does M_max cross 1 at mu = 0 in any sector?

**Input**:
- `tier0-computation/s27_torsion_gap_gate.npz` (D_can eigenvalues per sector)
- `tier0-computation/s27_multisector_bcs.py` (BCS solver infrastructure, reuse)
- `tier0-computation/tier1_dirac_spectrum.py` (geometry infrastructure)

**Script**: `s28a_torsionful_bcs.py`

**Method**:
1. Extract D_can eigenvalues from s27 data at all 21 tau values, for sectors (0,0), (1,0), (0,1), (1,1).
2. **Compute Kosmann matrices in the D_can eigenbasis**: The Kosmann operator K_a is defined with respect to the Levi-Civita connection. For D_can, the relevant pairing matrix becomes:
   ```
   V_nm^{can} = sum_{a in C^2} |<psi_n^{can}|K_a|psi_m^{can}>|^2
   ```
   where |psi_n^{can}> are D_can eigenvectors (NOT D_K eigenvectors). This requires diagonalizing D_can to get its eigenvectors, then rotating K_a into that basis.
3. Build the linearized BCS kernel in D_can eigenbasis:
   ```
   M_{nm} = V_nm^{can} / (2 * |lambda_n^{can} - mu| * |lambda_m^{can} - mu|)^{1/2}
   ```
4. Compute M_max at mu = 0 for each sector and tau.
5. **The decisive test**: if M_max(mu=0) > 1 in ANY sector at ANY tau, the mu obstruction is resolved by connection choice alone. BCS condensation occurs without requiring an external chemical potential.
6. Also compute M_max at mu = {0.5, 0.8, 1.0, 1.2} * lambda_min_can for comparison.
7. If M_max(mu=0) > 1: compute self-consistent Delta and F_cond in that sector.

**Output**: `s28a_torsionful_bcs.npz`, `s28a_torsionful_bcs.png`

**Gate (merged E-4/S-1/L-4)**:
- **MAJOR PASS**: M_max(mu=0) > 1 in any D_can sector -- torsion resolves the mu obstruction. Framework probability climbs substantially.
- **MINOR PASS**: M_max(mu=0) remains below 1, but M_max(mu=lambda_min_can) is significantly larger than in D_K basis (ratio > 2) -- torsion helps but does not fully resolve.
- **CLOSED**: M_max in D_can basis is comparable to or worse than D_K basis at all mu -- torsion does not help BCS.

**Agent**: phonon-exflation-sim (primary), coordinator (gate classification)

**Critical implementation note**: The Kosmann operator K_a is defined using the Levi-Civita connection coefficients (antisymmetric part A^a_{rs}). For the torsionful BCS, the pairing vertex is still the Kosmann coupling -- it is the SPECTRUM that changes (D_can eigenbasis vs D_K eigenbasis), not the interaction. The interaction vertex V_nm changes because the basis states change, but the K_a operator itself is the same object. Verify this by checking V_nm^{can} != V_nm^{LC} even though K_a is the same operator.

**Closure Audit Context (Baptista)**: This computation directly retests **Closure 17 (K-1e: Kosmann-BCS at mu=0, Session 23a)** and **Closure 18 (Gap-edge self-coupling V(gap,gap)=0, Session 23a)**. Both closes used D_K eigenstates exclusively. For D_can: (1) the spectral gap is 33-78% weaker (Session 27 T-1), directly reducing the BCS denominator; (2) the eigenstates are DIFFERENT (D_can = M_Lie, not M_Lie + Omega_LC), so V_nm^{can} != V_nm^{LC} even though K_a is the same operator; (3) the V(gap,gap)=0 selection rule is basis-dependent and may not hold in the D_can eigenbasis. The 7-13x M_max shortfall from K-1e was computed for D_K — a 33% gap reduction alone gives M_max ~ 0.1-0.2 (still below 1), so the D_can eigenbasis must also produce larger Kosmann matrix elements for a MAJOR PASS. The Baptista audit rates Closure 17 as CRITICAL priority and Closure 18 as HIGH (resolved as byproduct of Closure 17 test).

---

# II. EXECUTION ORDER

```
Phase 1 (parallel, ~30 min):
  28a-1 (KC-1)  ──┐
  28a-2 (L-1)   ──┤
  28a-3 (E-1)   ──┤── all independent, run simultaneously
  28a-4 (C-1)   ──┤
  28a-5 (C-4)   ──┤
  28a-6 (S-2)   ──┘

Phase 2 (sequential after Phase 1, ~2 hrs):
  28a-7 (Torsionful BCS) ── depends on D_can eigenvectors from s27 data

Gate classification: immediately after each computation completes.
```

KC-1 is the Constraint Chain gateway. If KC-1 CLOSES, Session 28c drops the phonon collision computations (KC-2 through KC-5) and redirects to structural gates only.

---

# III. SESSION VERDICT CRITERIA

Results from 28a that feed into 28b and 28c:

| Result | Feeds Into | Condition |
|:-------|:-----------|:----------|
| KC-1 verdict | 28c (KC-2 through KC-5) | KC-1 PASS required to proceed |
| L-1 thermal minimum | 28b (L-7 self-consistent tau-T) | If L-1 PASS, L-7 becomes high priority |
| E-4/S-1/L-4 torsionful M_max | 28b (L-3, L-5, L-6 diagnostics) | If MAJOR PASS, all Landau diagnostics run on D_can spectrum |
| C-1 spectral action difference | 28b (C-3 order-one condition) | Informs whether torsion modifies NCG axioms |
| S-2 dispersion relation | 28c (KC-2 T-matrix) | Phonon-like dispersion supports the 1D collision model |

**28a is successful if it produces definitive gate verdicts for KC-1 and the torsionful BCS (E-4/S-1/L-4).** Everything else is diagnostic context.

---

# IV. OUTPUT FILES

| File | Computation | Producer |
|:-----|:-----------|:---------|
| `tier0-computation/s28a_bogoliubov_coefficients.py` | KC-1 | phonon-sim |
| `tier0-computation/s28a_bogoliubov_coefficients.npz` | KC-1 data | phonon-sim |
| `tier0-computation/s28a_bogoliubov_coefficients.png` | KC-1 plot | phonon-sim |
| `tier0-computation/s28a_thermal_spectral_action.py` | L-1 | phonon-sim |
| `tier0-computation/s28a_thermal_spectral_action.npz` | L-1 data | phonon-sim |
| `tier0-computation/s28a_thermal_spectral_action.png` | L-1 plot | phonon-sim |
| `tier0-computation/s28a_lichnerowicz.py` | E-1 | phonon-sim |
| `tier0-computation/s28a_lichnerowicz.npz` | E-1 data | phonon-sim |
| `tier0-computation/s28a_lichnerowicz.png` | E-1 plot | phonon-sim |
| `tier0-computation/s28a_spectral_action_comparison.py` | C-1 | phonon-sim |
| `tier0-computation/s28a_spectral_action_comparison.npz` | C-1 data | phonon-sim |
| `tier0-computation/s28a_spectral_action_comparison.png` | C-1 plot | phonon-sim |
| `tier0-computation/s28a_spectral_correlations.py` | C-4 | phonon-sim |
| `tier0-computation/s28a_spectral_correlations.npz` | C-4 data | phonon-sim |
| `tier0-computation/s28a_spectral_correlations.png` | C-4 plot | phonon-sim |
| `tier0-computation/s28a_mmax_dispersion.py` | S-2 | phonon-sim |
| `tier0-computation/s28a_mmax_dispersion.npz` | S-2 data | phonon-sim |
| `tier0-computation/s28a_mmax_dispersion.png` | S-2 plot | phonon-sim |
| `tier0-computation/s28a_torsionful_bcs.py` | E-4/S-1/L-4 | phonon-sim |
| `tier0-computation/s28a_torsionful_bcs.npz` | E-4/S-1/L-4 data | phonon-sim |
| `tier0-computation/s28a_torsionful_bcs.png` | E-4/S-1/L-4 plot | phonon-sim |
| `tier0-computation/s28a_gate_verdicts.txt` | All gate verdicts | coordinator |
| `sessions/session-28/session-28a-synthesis.md` | Synthesis | coordinator |
