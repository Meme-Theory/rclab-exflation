# Session 16, Round 3a: Computational Action Items (Executable Specifications)
## KK-Theorist + Sim-Specialist Joint Specification
## Date: 2026-02-13
## Status: FINAL (both agents converged on all points)

---

## EXECUTIVE SUMMARY

This document converts all Round 2 proposals (2a: V_eff, 2b: D_K+generations, 2c: corrected Paasch, 2d-i/ii: Giants evaluation) into executable specifications with binding pass/fail criteria. Seven computational items are ranked by decisiveness, with full code-level specifications, dependency graphs, and hardware requirements.

**Key architectural decision**: Items #1 (V_eff) and #2 (Z_3+U(2)) execute in PARALLEL on separate code tracks with zero dependencies. Both complete in ~2 days. Day 3 integrates results via Items #3 (gauge couplings) and #4 (corrected Paasch). Items #5-#7 are diagnostics/scoping with flexible scheduling.

**Total new code**: ~900 lines across 3 new files + ~25 modified lines in existing code.
**Total compute**: ~90 minutes at p+q<=6 on Ryzen 32-core (8.7s/point benchmark from Session 14; eigenvalue caching amortizes across all sweeps).
**Hardware**: Single machine, 128GB RAM, 32-core CPU. No GPU required.

### Key API Decision (Converged, backward-compatibility verified)
The `collect_spectrum()` function in `tier1_dirac_spectrum.py` gets a new kwarg `store_eigenvectors=False`:
- `False` (default): Uses `eigvalsh(1j*D)` -- fastest, eigenvalues only. Returns `(all_evals, eval_data)` as before.
- `True`: Uses `eigh(1j*D)` -- returns eigenvectors as a THIRD return value. Returns `(all_evals, eval_data, evec_data)`.

**BACKWARD COMPATIBILITY**: 9 call sites across 3 files do `for p, q, evals in eval_data:` tuple unpacking (`tier1_spectral_action.py` lines 173/392/433/469/851/1137/1827, `extended_phi_analysis.py` line 155, `tier1_phi_analysis.py` line 175). The `eval_data` tuples MUST remain 3-element `(p, q, evals)`. Eigenvectors are returned in a SEPARATE parallel list `evec_data` of `(p, q, evecs)` tuples. When `store_eigenvectors=False`, the return count is 2 (unchanged); when `True`, it is 3. Zero changes needed to any existing caller.

### Key Runtime Correction
Session 14 benchmarks show 8.7s per s-value at pq=6 (not the initially estimated 30s). With the `eigvalsh` switch, expected ~5-6s per s-value. Total eigenvalue cache for 200 points: **~17-30 minutes** (not hours).

---

## 1. FULL BOSON+FERMION COLEMAN-WEINBERG V_eff

- **Type**: Formula + Computation
- **Specification**: Compute the 1-loop effective potential for the Jensen shape modulus s:

```
V_eff(s) = V_tree(s) + V_CW^boson(s) + V_CW^fermion(s)

V_tree(s)     = baptista_V_potential(0, s)                              [eq 3.80, existing code]
V_CW^boson(s) = +n_b/(64*pi^2) * m_C2^4(s) * [ln(m_C2^2(s)/mu^2) - c_b]  [4 C^2 modes, eq 3.84/3.87]
V_CW^fermion(s) = -n_f/(64*pi^2) * SUM_{(p,q)} dim(p,q) * SUM_j |lam_j^{(p,q)}(s)|^4 * [ln(|lam_j|^2/mu^2) - 3/2]
```

where:
  - `n_b = 12` (4 C^2 directions x 3 massive vector DOF)
  - `n_f` = {1, 4} (DOF envelope: 1 = per-eigenvalue minimal, 4 = 4D Dirac)
  - `c_b = 5/6` (MS-bar for vectors) or `3/2` (MS-bar for scalars) -- run BOTH
  - `m_C2^2(s)` from `gauge_boson_masses_baptista(0, s)` [existing code, line 660 of tier1_spectral_action.py]
  - `lam_j^{(p,q)}(s)` from `collect_spectrum(s, ..., max_pq_sum=6)` [existing code, line 1245 of tier1_dirac_spectrum.py]
  - `dim(p,q)` = Peter-Weyl multiplicity [existing code, `dim_su3_irrep()` in tier1_spectral_action.py]
  - `mu` = renormalization scale, swept over {0.1, 0.3, 1.0, 3.0, 10.0}

  **Two computation regimes** (from Round 2a Section X):
  - **CW regime** (standard): lam^4 * ln(lam^2) weighting
  - **High-T regime**: lam^2 weighting only: V_highT = -n_f/(12) * SUM d_n * |lam_n(s)|^2 / mu^2

  **Thermodynamic diagnostics** (from Round 2a-Hawking, adopted):
  - D1: U(s) = (1/64pi^2) * SUM d_n * |lam_n|^4;  TS(s) = (1/64pi^2) * SUM d_n * |lam_n|^4 * ln(|lam_n|^2)
  - D2: Spectral entropy S_spectral(s) = -SUM p_n * ln(p_n) with p_n = d_n * exp(-|lam_n|^2/Lambda^2) / Z
  - D3: Phase transition scan -- sweep Lambda over [0.01, 100], track s_0(Lambda)
  - D4: Specific heat sign -- d^2V_CW/d(mu^2)^2 at s_0

- **Pass/Fail** (11-point consolidated, Round 2a Section XI):

  **Tier 1 (BLOCKING):**
  1. V_eff(s) has a local minimum at s_0 > 0 (not at boundary s=0 or s=2.5)
  2. F(s_0) < F(0) -- broken phase wins
  3. d^2F/ds^2 > 0 at s_0 -- genuine minimum, not saddle

  **Tier 2 (ROBUSTNESS):**
  4. |s_0(pq=6) - s_0(pq=5)| < 0.1 -- truncation convergence
  5. s_0(n_f=1) and s_0(n_f=4) agree within 0.2 -- DOF robustness
  6. s_0 stable under mu variation by factor 2 (shift < 0.3)
  7. CW regime and high-T regime give qualitatively same s_0

  **Tier 3 (SIGNIFICANCE):**
  8. Mass ratios m_{(p,q)}/m_{(p',q')} at s_0 compared to SM
  9. Gauge couplings g_i(s_0) vs SM values (see Item #3)
  10. Spectral entropy max correlates with s_0 (|s_max - s_0| < 0.3)
  11. C_V sign at s_0

  **Six binding consistency checks** (Hawking, Round 2a-Hawking):
  At every candidate s_0: F(s_0) < F(0), d^2F/ds^2 > 0, C_s finite, Bekenstein bound, species bound, GSL.

- **Feasibility**: GREEN
- **Timeline**: Day 1: code + test at pq=3 (~4h). Day 2: production at pq=6 + sweeps (~12h compute, can run overnight).
- **Owner**: sim-specialist (code), kk-theorist (formula verification)
- **Decisiveness**: 8/10 (determines s_0, but DOF inversion weakens to INDICATIVE not definitive)
- **Dependencies**: All eigenvalue infrastructure exists. No new operators needed.
- **Code**:

  | File | Function | Lines | Runtime | Status |
  |------|----------|-------|---------|--------|
  | `tier0-computation/tier1_veff_full.py` (NEW) | `collect_spectrum_cached()` | ~40 | 8.7s first, 50ms cached | I/O wrapper |
  | `tier0-computation/tier1_veff_full.py` | `compute_veff_cw()` | ~70 | 10ms/point | Core formula |
  | `tier0-computation/tier1_veff_full.py` | `scalar_laplacian_on_irrep()` | ~15 | <1ms/sector | Bosonic tower (Version C) |
  | `tier0-computation/tier1_veff_full.py` | `veff_sweep()` | ~50 | 30 min first, 2 min cached | Production |
  | `tier0-computation/tier1_veff_full.py` | `convergence_test()` | ~35 | ~43 min (all pq levels) | Quality check |
  | `tier0-computation/tier1_veff_full.py` | `veff_diagnostics()` | ~60 | <1 min | Hawking thermo |
  | `tier0-computation/tier1_veff_full.py` | `high_T_veff()` | ~30 | <1 min | Cross-check |
  | `tier0-computation/run_veff.py` (NEW) | `main()` | ~100 | Orchestrates above | Driver |
  | **Total** | | **~400** | **~30 min first, 5 min repeat** | |

  **Pseudocode for core function:**
  ```python
  def compute_veff_cw(s, cached_spectrum, mu=1.0, n_f=4, c_b=5/6):
      """
      V_eff(s) = V_tree + V_boson + V_fermion from cached eigenvalue data.

      cached_spectrum: dict {(p,q): array_of_|lam|} at this s-value
      """
      V_tree = baptista_V_potential(0.0, s)

      m2_C2, _ = gauge_boson_masses_baptista(0.0, s)
      n_b = 12  # 4 directions x 3 polarizations
      V_boson = 0.0
      if m2_C2 > 1e-30:
          V_boson = n_b / (64 * np.pi**2) * m2_C2**2 * (np.log(m2_C2 / mu**2) - c_b)

      V_fermion = 0.0
      for (p, q), lam_abs in cached_spectrum.items():
          d_pq = dim_su3_irrep(p, q)
          for lam in lam_abs:
              if lam < 1e-12: continue  # skip zero modes
              lam2 = lam**2
              V_fermion -= n_f * d_pq / (64 * np.pi**2) * lam2**2 * (np.log(lam2 / mu**2) - 1.5)

      return V_tree + V_boson + V_fermion, V_tree, V_boson, V_fermion
  ```

  **Eigenvalue caching strategy:**
  ```python
  def cache_eigenvalues(s_values, gens, f_abc, gammas, max_pq_sum=6):
      """
      Compute and cache |lam| for all sectors at all s-values.
      Store to disk as .npz for restart capability.
      Returns: dict[s] -> dict[(p,q)] -> array_of_|lam|
      """
      cache = {}
      for s in s_values:
          all_evals, eval_data = collect_spectrum(s, gens, f_abc, gammas,
                                                  max_pq_sum=max_pq_sum, verbose=False)
          cache[s] = {}
          for (p, q, evals) in eval_data:
              cache[s][(p, q)] = np.abs(evals)
          np.savez(f'veff_cache_s{s:.4f}.npz', **{f'{p}_{q}': v for (p,q),v in cache[s].items()})
      return cache
  ```

  **Sweep grid:**
  - s-values: np.linspace(0.01, 2.5, 200) for production; np.linspace(0.01, 1.5, 50) for testing
  - mu-values: {0.1, 0.3, 1.0, 3.0, 10.0}
  - n_f values: {1, 4}
  - c_b values: {5/6, 3/2}
  - max_pq levels: {3, 4, 5, 6} for convergence test

- **Risk Factors**:

  | Risk | Severity | Mitigation |
  |------|----------|------------|
  | UV dominance: fermion CW ~30,000x boson at pq=6 | CRITICAL | Work with normalized V_eff(s) - V_eff(s_ref); use dV/ds for minimum |
  | mu sensitivity of s_0 | MODERATE | Sweep mu, report s_0(mu) curve |
  | DOF inversion (45:16 boson:fermion asymptotic) | HIGH | n_f envelope + flag as "Version C-modified, INDICATIVE" |
  | Zero mode ln(0) divergence | LOW | Skip |lam| < 1e-12 |
  | Numerical cancellation in large sums | MODERATE | Double precision (15 digits); finite-difference dV/ds cross-check |
  | MINGW eigensolver on 1024x1024 | LOW | eigh more stable than eigvals; try/except fallback to eigvals |

- **Hardware Requirements**:
  - Memory: ~200 MB peak (eigenvalue cache + working matrices)
  - CPU: Eigenvalue computation uses BLAS threading; ~8.7s per s-value at pq=6 (Session 14 benchmark), ~5-6s with eigvalsh switch
  - Disk: ~50 MB for eigenvalue cache (200 s-values)
  - Total compute: ~30 min for eigenvalue cache (once); ~10 min for all CW sweeps (reuses cache)
  - With convergence test (pq=3,4,5,6): ~43 min total (pq=3 ~30s, pq=4 ~2min, pq=5 ~10min, pq=6 ~30min)

---

## 2. Z_3 + U(2) QUANTUM NUMBER LABELING

- **Type**: Formula + Computation
- **Specification**: For each eigenvector of D_{(p,q)} on (SU(3), g_s), assign:
  - Z_3 generation = (p - q) mod 3
  - U(2) quantum numbers (Y, j) from total hypercharge and isospin operators
  - Particle type from SM map (eq 2.66)
  - Inter-generation mass ratios at candidate s_0 values

  **Mathematical details:**

  The Dirac block D_{(p,q)} has size `dim(p,q) * 16`. Each eigenvector lives in `V_{(p,q)} tensor C^16`.

  U(2) generators on the total space:
  ```
  Y_total = rho_{(p,q)}(e_8) tensor I_16 + I_{dim} tensor Y_spinor
  T_a = rho_{(p,q)}(e_a) tensor I_16 + I_{dim} tensor T_spinor_a   (a = 0, 1, 2)
  C2_SU2 = sum_a T_a^2
  ```

  where `rho_{(p,q)}(e_a)` is the representation matrix from `get_irrep()` (indices 0,1,2 for SU(2), index 7 for U(1)), and `Y_spinor`, `T_spinor_a` are the U(2) generators in the 16-dim spinor representation.

  **Source for spinor U(2) generators**: Two equivalent constructions:

  1. **From branching_computation.py** (line 387, `compute_u2_casimirs()`): Returns `Y_gen, C2_su2, T1, T2, T3` acting on C^16 via `LR_action_matrix()` (combined L+R action on Psi_+). These are the operators that decompose the 16-dim spinor into SM particle types (Session 7).

  2. **From spin connection** (sim-specialist derivation): The su(3) generators in the 16-dim spinor representation are:
  ```
  S_a = (1/4) * sum_{b,c} f_{abc} * gamma_b @ gamma_c   (a = 0..7)
  ```
  The U(2) subset uses a = {0,1,2} (SU(2)) and a = {7} (U(1)). This is the standard formula from the adjoint action on Cliff(R^8) restricted to the spin representation.

  Both constructions give the same operators (cross-validation required). The spinor part determines WHICH SM particle type; the representation part from `rho_{(p,q)}` determines WHICH KK level.

  For each eigenvector psi:
  ```
  Y_val = <psi | Y_total | psi>   (expectation value)
  j(j+1) = <psi | C2_SU2 | psi>   (Casimir expectation)
  ```

  **CRITICAL CODE CHANGE** -- modify `collect_spectrum()` (line 1245 of `tier1_dirac_spectrum.py`):

  New signature:
  ```python
  def collect_spectrum(s, gens, f_abc, gammas, max_pq_sum=3, verbose=True, store_eigenvectors=False):
  ```

  At line 1328:
  ```python
  # OLD:
  evals_pi = np.linalg.eigvals(D_pi)

  # NEW (when store_eigenvectors=False -- DEFAULT, fastest):
  iD_pi = 1j * D_pi
  iD_pi = (iD_pi + iD_pi.conj().T) / 2  # enforce exact Hermiticity (hazard H5)
  evals_h = np.linalg.eigvalsh(iD_pi)
  evals_pi = -1j * evals_h

  # NEW (when store_eigenvectors=True -- for Track B):
  iD_pi = 1j * D_pi
  iD_pi = (iD_pi + iD_pi.conj().T) / 2  # enforce exact Hermiticity
  evals_h, evecs_h = np.linalg.eigh(iD_pi)
  evals_pi = -1j * evals_h
  evecs_pi = evecs_h
  ```

  `eval_data` tuples extend to `(p, q, evals_array, evecs_array)` when `store_eigenvectors=True`, else remain `(p, q, evals_array)`. Backward compatible: all existing callers that index `eval_data[i][2]` for eigenvalues continue to work.

  Performance: `eigvalsh` is ~5x faster than `eigvals`; `eigh` is ~3x faster. At pq=6: ~5s/point (eigvalsh) vs ~8.7s/point (current eigvals). Net speedup for Track A.

  **Memory management**: For Track B, eigenvectors at (3,3) = 1024x1024 complex = 16 MB per sector. Total ~200 MB per s-value across 28 sectors. Analyze quantum numbers at each s-value immediately, then discard eigenvectors before the next s-value. Do NOT cache eigenvectors across the sweep.

  **Generation assignment** (trivial, from Z_3 center of SU(3)):
  ```python
  generation = (p - q) % 3  # 0, 1, or 2
  ```

  **Particle type map** (from SM quantum numbers, Baptista eq 2.66):
  ```
  (Y ~  0,   j = 0)   -> nu_R
  (Y ~ -1,   j = 0)   -> e_R
  (Y ~ +1/6, j = 1/2) -> (u_L, d_L) doublet
  (Y ~ +2/3, j = 0)   -> u_R
  (Y ~ -1/3, j = 0)   -> d_R
  (Y ~ -1/2, j = 1/2) -> (nu_L, e_L) doublet
  ```
  (Actual Y values depend on normalization convention; relative structure is invariant.)

- **Pass/Fail**:

  | Criterion | Condition | Verdict |
  |-----------|-----------|---------|
  | THREE generations | Each Z_3 sector has same set of (Y, j) particle types | STRUCTURAL PASS (expected by construction) |
  | Mass hierarchy exists | For at least one (Y, j), lightest masses across 3 Z_3 sectors are NOT degenerate | Z_3 splitting works |
  | Hierarchy ratio > 10 | At least one inter-generation ratio > 10 at s_0 or s = 0.30 | Nontrivial hierarchy |
  | OOM match | Charged lepton e_R ratio within factor 10 of m_mu/m_e = 207 | Quantitative test |
  | FAIL | Z_3 sectors have different (Y, j) content | Generation mechanism closed |

- **Feasibility**: GREEN
- **Timeline**: Day 1: eigenvector storage + U(2) generators (~4h). Day 2: quantum numbers + Z_3 + generation analysis (~4h). Day 2 evening: run at s = {0, 0.15, 0.30, 0.60, 1.14} (~2h).
- **Owner**: kk-theorist (math specification), sim-specialist (implementation)
- **Decisiveness**: 9/10 (parameter-free, representation-theoretic, independent of V_eff and DOF uncertainty)
- **Dependencies**: Requires eigenvectors from modified collect_spectrum(). Independent of V_eff.
- **Code**:

  | File | Function | Lines | Status |
  |------|----------|-------|--------|
  | `tier0-computation/tier1_dirac_spectrum.py` | Modified `collect_spectrum()` (eigh + evecs) | ~20 modified | CRITICAL |
  | `tier0-computation/tier1_u2_projection.py` (NEW) | `u2_generators_in_irrep()` | ~50 | New |
  | `tier0-computation/tier1_u2_projection.py` | `assign_quantum_numbers()` | ~40 | New |
  | `tier0-computation/tier1_u2_projection.py` | `z3_generation_label()` | ~5 | New |
  | `tier0-computation/tier1_u2_projection.py` | `analyze_generations()` | ~60 | New |
  | `tier0-computation/tier1_u2_projection.py` | `test_phi_in_generations()` | ~30 | New |
  | `tier0-computation/tier1_u2_projection.py` | `particle_type_map()` | ~20 | New |
  | `tier0-computation/tier1_u2_projection.py` | `u2_spinor_embedding()` | ~40 | New |
  | `tier0-computation/tier1_u2_projection.py` | `resolve_degenerate_subspaces()` | ~40 | New |
  | `tier0-computation/tier1_u2_projection.py` | `main() / driver` | ~50 | New |
  | `tier0-computation/run_z3_u2.py` (NEW) | Driver script | ~80 | New |
  | **Total** | | **~375 new + ~25 modified** | |

  **CRITICAL HAZARD: Degenerate eigenvector quantum numbers** (from sim-specialist review):
  When `eigh` returns eigenvectors for degenerate eigenvalues, the eigenvectors span the correct subspace but are NOT necessarily U(2) eigenstates. The Y and C2 expectation values may not be cleanly quantized. Resolution: within each group of degenerate eigenvalues (|lam_i - lam_j| < 1e-8), diagonalize Y_total restricted to that subspace to obtain the correct U(2) basis. This is the standard "good quantum number" technique. Implementation: `resolve_degenerate_subspaces()` function, ~40 lines, ~2s per sector.

  **Quantization check**: Round Y to nearest multiple of 1/6 (smallest Y quantum in SM). Round j to nearest half-integer. Flag any eigenvector where the rounded value differs from the raw value by more than 0.05.

- **Risk Factors**:

  | Risk | Severity | Mitigation |
  |------|----------|------------|
  | Eigenvector memory at (3,3): 1024x1024 complex = 16 MB | LOW | Store only at target s values (5 points) |
  | U(2) quantum numbers not cleanly quantized | MEDIUM | Round to nearest physical value; cross-validate vs Tier 0 branching |
  | Spinor U(2) embedding wrong normalization | MEDIUM | Cross-validate against branching_computation.py Session 7 results |
  | MINGW eigh on 1024x1024 complex | LOW | eigh is more stable than eigvals; add fallback |

- **Hardware Requirements**:
  - Memory: ~500 MB peak (eigenvectors at largest sector + U(2) operators)
  - CPU: ~15s per s-value at pq=6 with eigh (faster than current ~30s with eigvals)
  - Total compute: ~5 s-values * 15s = ~75s for eigenvalues; ~2 min for U(2) projection per s-value

---

## 3. GAUGE COUPLING TEST AT s_0

- **Type**: Test
- **Specification**: At the stabilized Jensen parameter s_0 (from Item #1), compute:

  ```
  g_1/g_2 = e^{-2*s_0}
  ```

  Compare to measured value: g_1/g_2 ~ 0.55 (from sin^2(theta_W) ~ 0.231 at M_Z).

  **Derivation**: The Jensen metric scales u(1) by e^{2s} and su(2) by e^{-2s}. Gauge couplings are proportional to the inverse metric on the gauge directions:
  ```
  g_1^2 ~ 1/g_{u(1)} = e^{-2s}
  g_2^2 ~ 1/g_{su(2)} = e^{2s}
  ```
  Therefore g_1/g_2 = e^{-2s}.

  **RG running caveat** (from Round 2d-ii Section IV): This formula gives g_1/g_2 at the compactification scale (~M_Pl). At M_Z: g_1 increases ~35%, g_2 decreases ~20%. Net systematic uncertainty: 10-15%. The 20% pass window absorbs this.

  **Backup protocol** (from Round 2d-ii, Sagan): If V_eff is monotonic (no s_0 from Item #1), use the gauge-coupling-derived value s_0 = 0.30 (from e^{-0.60} = 0.549 ~ 0.55). Evaluate ALL mass ratios and Z_3 structure at this backup s_0. This is weaker (s_0 imposed, not derived) but still informative.

  **Diagnostic value of s_0** (from Round 2d-ii):
  ```
  s_0 = 0.15: e^{-0.30} = 0.741 --> marginal FAIL (35% above)
  s_0 = 0.30: e^{-0.60} = 0.549 --> STRONG PASS (0.2% match)
  s_0 = 0.50: e^{-1.00} = 0.368 --> FAIL (33% below)
  s_0 = 1.14: e^{-2.28} = 0.102 --> catastrophic FAIL
  ```

  **Physically viable window**: s_0 in [0.15, 0.50] for consistency. Sweet spot: s_0 ~ 0.30.

- **Pass/Fail**:

  | Criterion | Condition | Verdict |
  |-----------|-----------|---------|
  | STRONG PASS | e^{-2*s_0} in [0.45, 0.60] | Tight match even before RG |
  | PASS | e^{-2*s_0} in [0.4, 0.7] | Consistent after plausible RG corrections |
  | FAIL | e^{-2*s_0} outside [0.2, 0.8] | No RG running can save it |

- **Feasibility**: GREEN (trivial computation once s_0 known)
- **Timeline**: Minutes once s_0 is available from Item #1 (or immediately using backup s_0 = 0.30)
- **Owner**: kk-theorist
- **Decisiveness**: 7/10 (FIRST Level 3 test against instrument measurement; BUT if using backup s_0, reduced to 5/10 since s_0 is imposed not derived)
- **Dependencies**: Item #1 (V_eff) for derived s_0. Can run with backup s_0 = 0.30 independently.
- **Code**: ~10 lines (formula evaluation). Can be inline in the analysis script.

  ```python
  def gauge_coupling_test(s_0):
      """FIRST Level 3 test against measurement."""
      g1_over_g2 = np.exp(-2 * s_0)
      measured = 0.55
      deviation = abs(g1_over_g2 - measured) / measured * 100
      strong_pass = 0.45 <= g1_over_g2 <= 0.60
      pass_ = 0.4 <= g1_over_g2 <= 0.7
      fail = g1_over_g2 < 0.2 or g1_over_g2 > 0.8
      return g1_over_g2, deviation, strong_pass, pass_, fail
  ```

---

## 4. CORRECTED PAASCH PHI^{3/2} TEST

- **Type**: Test
- **Specification**: Paasch's mass numbers satisfy N(j) = (m_j/m_e)^{2/3}. Since D_K eigenvalues ARE masses (Paper 17, Corollary 3.4), the spectral test for the Paasch signature ratio is:

  ```
  lambda_p / lambda_K = m_p / m_K = (N(p)/N(K))^{3/2} = phi_paasch^{3/2} = 1.8985
  ```

  **Pre-registered target**: 1.8985 (stated before computation in Round 2c).

  **Empirical check**: m_p/m_K = 938.272/493.677 = 1.9006. phi_paasch^{3/2} = 1.53158^{1.5} = 1.8954. Agreement: 0.27%.

  **Implementation**: After Z_3+U(2) labeling (Item #2), identify which (p,q) sector + U(2) quantum numbers correspond to the proton and kaon. Then extract the eigenvalue ratio at s_0 (from Item #1 or backup s_0 = 0.30).

  **IMPORTANT**: The sector-to-particle identification requires the U(2) quantum numbers from Item #2. The proton is a baryon (three quarks), so the relevant eigenvalue is for the u_R or d_R type in a specific Z_3 sector. The kaon is a meson. The identification is non-trivial and depends on the full particle map.

  **Additional phi_paasch targets** (from Round 2c):
  - f_N vs sqrt(7/3): 0.022% (algebraic invariant of D(SU(3)))
  - f_M = 2/phi_golden = 1.236 vs [sqrt(58/31)]^{2/3}: 0.32% (late amendment from Round 2d-i Section V)

- **Pass/Fail**:

  | Criterion | Condition | Verdict |
  |-----------|-----------|---------|
  | STRONG PASS | lambda_p/lambda_K within 1% of 1.8985, sector ID from U(2) (not fitted) | Paasch connection established |
  | PASS | Within 5% of 1.8985 after sector identification | Paasch connection suggestive |
  | FAIL | No mass ratio within 10% of 1.8985 at s_0, for any sector ID | Paasch connection severed |

- **Feasibility**: GREEN (nearly free once Item #2 labeling exists)
- **Timeline**: Hours (after Item #2 complete). Runs as analysis on labeled eigenvalue catalog.
- **Owner**: kk-theorist (sector identification logic), sim-specialist (automation)
- **Decisiveness**: 6/10 (pre-registered test of specific algebraic prediction; weakened by dependence on sector identification which may be ambiguous)
- **Dependencies**: Item #2 (Z_3+U(2) labeling). Item #1 (V_eff) for s_0 or backup s_0.
- **Code**: ~50 lines added to `tier1_u2_projection.py` analysis section.

---

## 5. SEELEY-DEWITT CONVERGENCE DIAGNOSTIC

- **Type**: Test (diagnostic)
- **Specification**: Test whether the V_eff minimum s_0 converges as the truncation level max_pq_sum increases. Compute:

  ```
  s_0(max_pq = 3), s_0(max_pq = 4), s_0(max_pq = 5), s_0(max_pq = 6)
  ```

  Also compute the Seeley-DeWitt coefficient a_2(s) (proportional to scalar curvature) at each truncation level. The a_2 is:
  ```
  a_2(s) = SUM_{(p,q)} dim(p,q)^2 * SUM_j |lam_j^{(p,q)}(s)|^2
  ```
  weighted appropriately for the heat kernel expansion.

  **Physical content**: If s_0 changes by < 0.1 from pq=5 to pq=6, the truncation is reliable. If it changes by > 0.5, higher irreps are needed.

  **Implementation**: Reuses eigenvalue cache from Item #1. Each pq level is a strict subset of the next. No recomputation needed -- just truncate the sum.

- **Pass/Fail**:

  | Criterion | Condition | Verdict |
  |-----------|-----------|---------|
  | PASS | |s_0(6) - s_0(5)| < 0.1 | Truncation reliable |
  | MARGINAL | 0.1 < |s_0(6) - s_0(5)| < 0.5 | Indicative but not conclusive |
  | FAIL | |s_0(6) - s_0(5)| > 0.5 | Need higher pq (7+), timeline extends |

- **Feasibility**: GREEN (reuses cached data)
- **Timeline**: ~30 min analysis once eigenvalue cache from Item #1 exists.
- **Owner**: sim-specialist
- **Decisiveness**: 4/10 (diagnostic that validates Item #1, not independently decisive)
- **Dependencies**: Item #1 eigenvalue cache
- **Code**: ~30 lines in `tier1_veff_full.py`

  ```python
  def convergence_test(cache, s_values, mu=1.0, n_f=4, pq_levels=[3, 4, 5, 6]):
      """Test s_0 convergence with truncation level."""
      results = {}
      for max_pq in pq_levels:
          # Filter cache to sectors with p+q <= max_pq
          V_eff_arr = []
          for s in s_values:
              truncated = {k: v for k, v in cache[s].items() if k[0]+k[1] <= max_pq}
              V, _, _, _ = compute_veff_cw(s, truncated, mu=mu, n_f=n_f)
              V_eff_arr.append(V)
          idx_min = np.argmin(V_eff_arr)
          results[max_pq] = s_values[idx_min]
      return results
  ```

---

## 6. BOSONIC KK TOWER SCOPING (Feasibility Study)

- **Type**: Formula (scoping study, NOT full computation)
- **Specification**: Assess the feasibility and level-of-effort for computing the MISSING bosonic KK tower eigenvalues, to address the DOF inversion (45:16 boson:fermion asymptotic ratio, Round 2d-i Section III).

  Three bosonic operators on (SU(3), g_s):

  | Operator | Fiber DOF | Peter-Weyl block size | Existing code? |
  |----------|-----------|----------------------|----------------|
  | Scalar Laplacian Delta_0 | 1 | dim(p,q) | NO |
  | Hodge Laplacian Delta_1 on 1-forms | 8 | dim(p,q) * 8 | NO |
  | Lichnerowicz Laplacian Delta_2 on sym 2-tensors | 36 | dim(p,q) * 36 | NO |

  **Scalar Laplacian**: Peter-Weyl decomposition gives `Delta_0^{(p,q)}` as a `dim(p,q) x dim(p,q)` matrix (no spinor factor). The construction uses the same representation matrices `rho_{(p,q)}(e_a)` and metric infrastructure. Formula:
  ```
  Delta_0^{(p,q)} = -SUM_{a,b} g^{ab}(s) * rho_{(p,q)}(e_a) * rho_{(p,q)}(e_b)
  ```
  where g^{ab}(s) is the inverse Jensen metric: g^{u(1)} = e^{-2s}/g_0, g^{su(2)} = e^{2s}/g_0, g^{C^2} = e^{-s}/g_0. The metric is block-diagonal (tier1_dirac_spectrum.py line 111-151), so g^{ab} is trivially computed. This is the quadratic Casimir for the deformed metric. ~30 lines new code. Eigenvalues are REAL and non-negative (Laplacian is self-adjoint, non-negative).

  **Hodge Laplacian**: More complex. The 1-form bundle on SU(3) is 8-dimensional. Peter-Weyl block size: `dim(p,q) * 8`. The Hodge Laplacian includes the connection Laplacian PLUS curvature terms (Weitzenbock formula):
  ```
  Delta_1 = nabla^* nabla + Ric
  ```
  Requires the Ricci tensor on (SU(3), g_s). ~100-150 lines. Eigenvalues real.

  **Lichnerowicz**: Symmetric 2-tensor bundle is 36-dimensional. Block size: `dim(p,q) * 36`. Most complex. ~200+ lines. Eigenvalues real.

  **Deliverable**: For each operator, report:
  1. Block size at p+q=6 (largest matrix to diagonalize)
  2. New code estimate (lines)
  3. New mathematical ingredients needed
  4. Compute time estimate
  5. Whether existing infrastructure (metric, connection, representation matrices) suffices

  **THIS IS A SCOPING STUDY ONLY.** The full computation is Tier 2+.

- **Pass/Fail**: N/A (feasibility study). Output is a table of LOE estimates.
- **Feasibility**: GREEN for scoping; YELLOW for full computation
- **Timeline**: ~4 hours for the scoping document. Full scalar Laplacian: ~1 day. Full Hodge: ~3-5 days. Full Lichnerowicz: ~1-2 weeks.
- **Owner**: kk-theorist (mathematical specification), sim-specialist (LOE estimate)
- **Decisiveness**: 3/10 (scoping only; but the FULL computation would be 8/10 as it resolves the DOF inversion)
- **Dependencies**: None (uses existing infrastructure knowledge)
- **Code**: ~20 lines for scalar Laplacian prototype (in scoping doc). Full computation deferred.

  **Scalar Laplacian prototype** (for scoping):
  ```python
  def scalar_laplacian_on_irrep(rho_pq, g_inv_s):
      """Quadratic Casimir for deformed metric = scalar Laplacian."""
      dim_pq = rho_pq[0].shape[0]
      Delta = np.zeros((dim_pq, dim_pq), dtype=complex)
      for a in range(8):
          for b in range(8):
              Delta -= g_inv_s[a, b] * rho_pq[a] @ rho_pq[b]
      return Delta  # Hermitian, eigenvalues are real >= 0
  ```

  **Block sizes at p+q=6:**
  - Scalar: max dim(3,3) = 64. Eigenvalue problem: 64x64. Trivial.
  - Hodge: max 64*8 = 512. Eigenvalue problem: 512x512. Manageable.
  - Lichnerowicz: max 64*36 = 2304. Eigenvalue problem: 2304x2304. Heavy but feasible.

---

## 7. PFAFFIAN PREREQUISITES

- **Type**: Computation (prerequisites for topological test)
- **Specification**: Begin constructing the finite Dirac operator D_F on C^32 from the D_K eigenvectors, to enable the Pfaffian sign test:

  ```
  sgn(Pf(J * D_F(s)))
  ```

  **The Pfaffian Override Principle** (Round 1d, unanimous Giants): If the Z_2 topological invariant changes sign at ANY s_c in [0, 2], it supersedes all other priorities. Topology trumps dynamics.

  **Prerequisites** (from Round 2d-i):
  1. Store D_K eigenvectors (from Item #2 eigenvector modification)
  2. Select the 16 lightest positive eigenvalues at each s (truncated spectrum)
  3. Construct D_F as the 32x32 matrix with these eigenvalues (16 positive + 16 negative from chirality)
  4. Verify J-compatibility: J * D_F = D_F * J (where J is real structure from Session 8)
  5. Compute Pf(J * D_F) at ~50 s-values in [0, 2]
  6. Report sign changes

  **Mathematical detail**: The finite Dirac operator D_F in the Connes spectral triple is a 32x32 matrix acting on H_F = C^32. In the phonon-exflation framework, D_F is constructed from D_K eigenvalues (Paper 17, Corollary 3.4). The Pfaffian is:

  ```
  Pf(A) = defined for 2n x 2n antisymmetric matrix A
  J * D_F is antisymmetric if J^2 = -1 (KO-dim 6 condition, verified Session 8)
  sgn(Pf(J * D_F)) = product of signs of eigenvalues of J * D_F
  ```

  **Truncation at p+q <= 1**: Use only (0,0), (1,0), (0,1) sectors. Total eigenvalues: 16 + 48 + 48 = 112. Select lightest 16 positive eigenvalues. This gives a "truncated Pfaffian" that may differ from the full result but provides an early indicator.

  **Spectral gap condition**: For the truncation to be reliable, the 16th eigenvalue must be well-separated from the 17th. If the gap is < 10% of the 16th eigenvalue, truncation is unreliable.

- **Pass/Fail**:

  | Criterion | Condition | Verdict |
  |-----------|-----------|---------|
  | SIGN CHANGE | sgn(Pf(J * D_F(s))) flips at some s_c in [0, 2] | TOPOLOGICAL TRANSITION -- overrides everything |
  | CONSTANT | Pfaffian sign unchanged for all s in [0, 2] | Topological route closed; V_eff must work |
  | INCONCLUSIVE | Spectral gap < 10% at all s | Truncation unreliable; need more sectors |

- **Feasibility**: YELLOW (prerequisites ~3-5 days; full version ~3 weeks)
- **Timeline**: Days 4-5 of one-week plan (after Items #1 and #2)
- **Owner**: kk-theorist (D_F construction math), sim-specialist (Pfaffian numerics)
- **Decisiveness**: 10/10 (binary, zero parameters, topological -- IF sign changes)
- **Dependencies**: Item #2 (eigenvectors). Session 8 J matrix. Session 11 gamma_F.
- **Code**: ~150-200 lines new (D_F construction + Pfaffian computation)

  | File | Function | Lines | Status |
  |------|----------|-------|--------|
  | `tier0-computation/pfaffian_test.py` (NEW) | `construct_D_F_truncated()` | ~60 | New |
  | `tier0-computation/pfaffian_test.py` | `compute_pfaffian_sign()` | ~30 | New |
  | `tier0-computation/pfaffian_test.py` | `spectral_gap_check()` | ~20 | New |
  | `tier0-computation/pfaffian_test.py` | `pfaffian_sweep()` | ~40 | New |
  | `tier0-computation/pfaffian_test.py` | `main()` | ~50 | New |
  | **Total** | | **~200** | |

- **Risk Factors**:

  | Risk | Severity | Mitigation |
  |------|----------|------------|
  | D_F construction from truncated spectrum may not be J-compatible | HIGH | Verify J*D_F=D_F*J at each s; if fails, construction is wrong |
  | Spectral gap too small at truncation boundary | MEDIUM | Check gap; if <10%, extend to p+q<=2 |
  | Pfaffian computation numerically unstable for near-zero determinant | LOW | Use scipy.linalg.pfaffian or compute via eigenvalues |
  | Full D_F requires all 16 Weyl fermion quantum numbers matched to eigenvectors | HIGH | This is the ~3 week part; truncated version avoids it |

---

## DEPENDENCY GRAPH

```
                    [EXISTING INFRASTRUCTURE]
                    gens, f_abc, gammas, Clifford, etc.
                           |
           +---------------+---------------+
           |                               |
   [ITEM #1: V_eff]              [ITEM #2: Z_3 + U(2)]
   tier1_veff_full.py         tier1_u2_projection.py
   ~365 lines new                ~315 lines new + 20 modified
   Days 1-2                      Days 1-2
           |                               |
           +------+------+      +----------+----------+
                  |       |      |          |          |
         [ITEM #5]  [ITEM #3]  [ITEM #4]  [ITEM #7]
         SD conv    Gauge      Paasch     Pfaffian
         ~30 lines  ~10 lines  ~50 lines  ~200 lines
         Day 3      Day 3      Day 3      Days 4-5
                       |
                  [ITEM #6: Bosonic KK Scoping]
                  ~20 lines prototype
                  Day 3 (analysis only)
```

**Critical path**: Items #1 and #2 are PARALLEL (zero code dependencies). Day 3 integrates both via Items #3, #4, #5. Items #6 and #7 are independent and can run anytime after Day 2.

---

## HARDWARE REQUIREMENTS

| Resource | Requirement | Available | Status |
|----------|------------|-----------|--------|
| CPU | 32-core recommended for parallelism | Ryzen 32-core | OK |
| RAM | ~500 MB peak (eigenvectors at largest sector) | 128 GB | OK |
| Disk | ~50 MB eigenvalue cache | Ample | OK |
| GPU | Not required (numpy CPU only) | AMD (no CUDA) | N/A |
| Python | numpy, scipy | Installed | OK |
| Runtime | ~4-6 hours total compute (eigenvalue cache dominates) | Overnight OK | OK |

**Performance estimates** (Session 14 benchmarks, Ryzen 32-core):
- Eigenvalue cache at pq=6, 200 s-values: ~30 min first run with eigvals, ~17 min with eigvalsh (bottleneck)
- V_eff sweep (5 mu x 2 n_f x 2 c_b = 20 combos): ~4 min (uses cache, pure arithmetic)
- Convergence test (pq=3,4,5,6): ~43 min total (pq=3 ~30s, pq=4 ~2min, pq=5 ~10min, pq=6 ~30min)
- Z_3+U(2) at 5 s-values with eigenvectors: ~5 min (eigh, ~50s per point + ~10s analysis)
- Gauge coupling: seconds
- Paasch test: seconds
- Pfaffian at 50 s-values: ~30 min (small matrices, p+q<=1)

**Total**: ~90 minutes compute. Fits within a single work session. No overnight run needed.

---

## COMBINED SCHEDULE

| Day | Track A (V_eff) | Track B (Z_3+U(2)) | Integration |
|-----|-----------------|--------------------|----|
| **Day 1** | Code tier1_veff_full.py. Test at pq=3. | Modify collect_spectrum() for eigh+evecs. Code U(2) generators. | -- |
| **Day 2** | Production run: eigenvalue cache at pq=6, 200 s-points. Start CW sweeps. | Code quantum number assignment, Z_3 labeling, generation analysis. Run at 5 s-values. | -- |
| **Day 3** | Identify s_0 (or "monotonic"). Convergence test. | Particle type map. Inter-generation ratios. | **Gauge coupling test. Corrected Paasch test. Integration of both tracks.** |
| **Day 4** | Thermodynamic diagnostics (D1-D4). Bosonic KK scoping. | phi_paasch^{3/2} detailed analysis. | Begin Pfaffian prerequisites. |
| **Day 5** | Documentation. | Documentation. | Pfaffian sweep (if prerequisites met). |

---

## THE GAUGE-COUPLING BACKUP s_0 = 0.30 (from Round 2d-ii)

**Scenario**: V_eff is monotonic (no minimum). Item #1 returns FAIL.

**Protocol**:
1. Set s_0 = 0.30 (the value where g_1/g_2 = e^{-0.60} = 0.549 ~ measured 0.55)
2. At s = 0.30, evaluate:
   - All Z_3 inter-generation mass ratios (from Item #2)
   - Corrected Paasch phi_paasch^{3/2} (from Item #4)
   - Mass hierarchy assessment
3. Report as "gauge-coupling-imposed s_0 = 0.30" (weaker than V_eff-derived s_0)

**Interpretation**: If the geometry at gauge-consistent s also gives reasonable mass ratios, the framework has structural coherence even without perturbative V_eff support. If it gives wrong masses, a fundamental tension exists.

This backup is endorsed by all four Giants (Round 2d-i + 2d-ii).

---

## CONSOLIDATED NUMERICAL HAZARDS (KK-theorist + sim-specialist)

| ID | Hazard | Severity | Location | Mitigation |
|----|--------|----------|----------|------------|
| H1 | UV dominance (lam^4 weighting) | CRITICAL | compute_veff_full | Normalize: V(s) - V(s_ref). Report dV/ds. |
| H2 | mu sensitivity of s_0 | MODERATE | compute_veff_full | Sweep mu over {0.1, 0.3, 1.0, 3.0, 10.0}, report s_0(mu) |
| H3 | Zero mode log divergence | LOW | compute_veff_full | Skip |lam| < 1e-12 |
| H4 | Numerical cancellation in dV/ds | MODERATE | veff_sweep | Finite difference check: h=1e-5, 1e-6, 1e-7 |
| H5 | eigh symmetry assumption | LOW | collect_spectrum | Symmetrize: iD = (iD + iD.conj().T)/2 before eigh/eigvalsh |
| H6 | Degenerate eigenvectors not U(2) eigenstates | MEDIUM | assign_quantum_numbers | Diagonalize U(2) within degenerate subspace (~40 lines) |
| H7 | Spectral entropy underflow | LOW | veff_diagnostics | Log-sum-exp trick for exp(-lam^2/Lambda^2) |
| H8 | _irrep_cache cleared in driver scripts | LOW (NOT a library bug) | run_*.py | Populate cache at start, never clear. Helper: precompute_irreps() |

---

## OVERALL RISK MATRIX

| Risk Factor | Probability | Impact | Items Affected | Mitigation |
|------------|------------|--------|----------------|------------|
| DOF inversion invalidates V_eff minimum | 35-40% | HIGH (V_eff becomes indicative only) | #1, #3, #5 | n_f envelope + "Version C-modified" flag; Items #2,#4,#7 unaffected |
| V_eff monotonic at all natural params | 35-40% | MEDIUM (perturbative route closed) | #1, #3 | Backup s_0=0.30; Pfaffian becomes essential (#7) |
| MINGW eigensolver instability | 5% | LOW (fallback exists) | #1, #2 | try/except with eigvals fallback; limit matrix size |
| Z_3 sectors have different (Y,j) content | 2% | HIGH (generation mechanism closed) | #2 | Expected to pass by construction (rep theory); would be a bug |
| Spectral gap too small for Pfaffian truncation | 30% | MEDIUM (need more sectors) | #7 | Extend to p+q<=2; timeline extends by ~1 day |
| U(2) quantum numbers not cleanly quantized | 15% | MEDIUM (particle ID ambiguous) | #2, #4 | Round to nearest physical value; cross-validate |

---

## CONVERGED API DECISIONS (KK-theorist + sim-specialist)

### 1. collect_spectrum() Modification
```python
# New signature (backward compatible):
def collect_spectrum(s, gens, f_abc, gammas, max_pq_sum=3, verbose=True, store_eigenvectors=False):
    # store_eigenvectors=False (default): uses eigvalsh(1j*D), fastest, eigenvalues only
    # store_eigenvectors=True: uses eigh(1j*D), returns evecs in extended tuples
```
- `eval_data` entries: `(p, q, evals)` when `store_eigenvectors=False`, `(p, q, evals, evecs)` when `True`.
- All existing callers unaffected (index `[2]` for eigenvalues still correct).

### 2. File Naming Convention
- `tier1_veff_full.py`: V_eff Track A (matches existing `tier1_dirac_spectrum.py`, `tier1_spectral_action.py`)
- `tier1_u2_projection.py`: Z_3+U(2) Track B
- `pfaffian_test.py`: Pfaffian Item #7
- `run_veff.py`, `run_z3_u2.py`: Driver scripts

### 3. Scalar Laplacian Placement
In `tier1_veff_full.py` (bosonic operator, conceptually part of V_eff, no eigenvector dependency).

### 4. _irrep_cache Management
```python
def precompute_irreps(gens, f_abc, max_pq_sum=6):
    """Populate _irrep_cache for all sectors. Call ONCE at script start."""
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            try:
                get_irrep(p, q, gens, f_abc)
            except NotImplementedError:
                pass
```
Both driver scripts call this at initialization. Never clear the cache during s-sweeps.

### 5. Memory Strategy
- Track A (V_eff): `store_eigenvectors=False`. Cache eigenVALUES to disk (.npz per s-value). ~50 MB total.
- Track B (Z_3+U(2)): `store_eigenvectors=True` at each of 5 target s-values. Analyze quantum numbers immediately, discard eigenvectors before next s-value. Peak ~200 MB.

---

## SUMMARY TABLE

| Rank | Item | Type | Timeline | Owner | Decisiveness | Feasibility | New Code | Key Caveat |
|------|------|------|----------|-------|-------------|-------------|----------|------------|
| **1** | V_eff full CW | Formula+Computation | 2 days | sim-specialist | 8/10 | GREEN | ~400 lines | DOF inversion: INDICATIVE not definitive |
| **1** | Z_3+U(2) labeling | Formula+Computation | 2 days | kk-theorist+sim | 9/10 | GREEN | ~375+25 mod | Parameter-free, representation-theoretic |
| **2** | Gauge coupling test | Test | Minutes | kk-theorist | 7/10 | GREEN | ~10 lines | FIRST Level 3 test; backup s_0=0.30 |
| **3** | Corrected Paasch phi_paasch^{3/2} | Test | Hours | both | 6/10 | GREEN | ~50 lines | Pre-registered; depends on sector ID |
| **4** | Seeley-DeWitt convergence | Test | 30 min | sim-specialist | 4/10 | GREEN | ~30 lines | Diagnostic for #1 |
| **5** | Bosonic KK scoping | Formula | 4 hours | kk-theorist | 3/10 | GREEN | ~20 lines | Scoping only; full computation ~weeks |
| **6** | Pfaffian prerequisites | Computation | 3-5 days | both | 10/10 | YELLOW | ~200 lines | Binary topological; IF sign changes, overrides all |

---

*"Compute. Report everything. Null results are science." -- Feynman*
*"The universe does not care about our comfort. Follow the mathematics." -- Hawking*
