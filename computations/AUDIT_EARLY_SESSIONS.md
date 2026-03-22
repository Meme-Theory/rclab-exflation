# Early Sessions Audit (S7-S24)

Audit date: 2026-03-15
Auditor: Claude Opus 4.6 (automated code review)
Scope: All scripts prefixed s7_-s24_, kk1_, tier1_, session11_, a5_, b_, c1_, d_, phase25_, sp_, sd_, l20_, r20a_

---

## Scripts Inventoried

**137 scripts** in the S7-S24 range (counting all prefixes: kk1_, tier1_, session11_, a5_, b_, c1_, d_, phase25_, sp_, sd_, l20_, r20a_, s19a_, s21_, s22_, s23_, s24_).

### Library scripts (no .npz, imported by others)
- `tier1_dirac_spectrum.py` — THE bedrock. Dirac operator on Jensen-deformed SU(3). 1900+ lines.
- `branching_computation.py` — Gell-Mann matrices, SU(3) branching rules.
- `b6_scalar_vector_laplacian.py` — Laplacian infrastructure, Ricci tensor.

### ROOT data producers (produce .npz without loading any .npz)
- `kk1_bosonic_tower.py` -> `kk1_bosonic_spectrum.npz` (12 downstream consumers)
- `r20a_riemann_tensor.py` -> `r20a_riemann_tensor.npz` (20 downstream consumers)
- `l20_lichnerowicz.py` -> `l20_TT_spectrum.npz` (5 downstream), `l20_vtotal_minimum.npz` (9 downstream)
- `s19a_sweep_data.py` -> `s19a_sweep_data.npz` (34 downstream consumers)
- `s22b_eigenvector_extraction.py` -> `s22b_eigenvectors.npz` (6 downstream consumers)
- `s23a_kosmann_singlet.py` -> `s23a_kosmann_singlet.npz` (**63 downstream consumers** — MOST CONSUMED FILE)
- `s21c_neutrino_fine_grid.py` -> `s21c_neutrino_fine_grid.npz` (2 downstream)
- `s22a_dnp_bound.py` -> `s22a_dnp_bound.npz` (0 downstream)
- `s22c_higgs_sigma.py` -> `s22c_higgs_sigma.npz` (0 downstream)

### Intermediate data producers (load one .npz, produce another)
- `s21c_V_IR.py`: loads s19a_sweep_data + kk1_bosonic_spectrum -> `s21c_V_IR.npz`
- `s22b_block_diagonal_results.py`: loads s19a_sweep_data -> `s22b_block_diagonal_results.npz`
- `s22b_kosmann_matrix.py`: loads s22b_eigenvectors -> `s22b_kosmann_matrix.npz`
- `s23a_bcs_gap_equation.py`: loads s23a_kosmann_singlet -> `s23a_gap_equation.npz`
- `s23a_eigenvector_extended.py`: loads s22b data -> `s23a_eigenvectors_extended.npz`
- `s23c_fiber_integrals.py`: loads r20a_riemann_tensor -> `s23c_fiber_integrals.npz`
- `s24a_vspec.py`: loads s23c_fiber_integrals -> `s24a_vspec.npz`

---

## Root Data Files (no upstream dependencies)

These scripts compute everything from scratch (SU(3) generators + Jensen metric) without loading any .npz:

| Script | Output .npz | Downstream Count | Description |
|:-------|:-----------|:-----------------|:------------|
| `tier1_dirac_spectrum.py` | (library) | ALL scripts import it | Dirac operator D_K on (SU(3), g_tau) |
| `s19a_sweep_data.py` | `s19a_sweep_data.npz` | 34 | Eigenvalue sweep at 21 tau values, max_pq_sum=6 |
| `s23a_kosmann_singlet.py` | `s23a_kosmann_singlet.npz` | **63** | Kosmann matrix elements in (0,0) singlet |
| `r20a_riemann_tensor.py` | `r20a_riemann_tensor.npz` | 20 | Full 8x8x8x8 Riemann tensor at 21 tau |
| `kk1_bosonic_tower.py` | `kk1_bosonic_spectrum.npz` | 12 | Bosonic KK tower (scalar + vector) |
| `l20_lichnerowicz.py` | `l20_TT_spectrum.npz`, `l20_vtotal_minimum.npz` | 14 | TT spectrum + Casimir/CW energies |
| `s22b_eigenvector_extraction.py` | `s22b_eigenvectors.npz` | 6 | Dirac eigenvectors at 9 tau values |

---

## Hardcoded Constants Found

All early-session scripts (S7-S24) work in **pure geometric units** on SU(3). There are NO hardcoded physical constants (G_N, hbar, c, alpha, M_Planck) in any root-level script. This is by design: the Dirac spectrum, Riemann tensor, Kosmann matrix elements, and KK masses are all dimensionless geometric quantities.

Physical constants only appear in later sessions (S22d+) when computing cosmological observables. The key early-session constants are geometric:

| Script | Constant | Value | Correct? |
|:-------|:---------|:------|:---------|
| `tier1_dirac_spectrum.py` | Jensen scale factors | L1=e^{2s}, L2=e^{-2s}, L3=e^s | **CORRECT** (volume-preserving: L1*L2^3*L3^4=1) |
| `tier1_dirac_spectrum.py` | Killing form normalization | B_{ab} = -3 delta_{ab} | **CORRECT** for su(3) with Tr(e_a e_b) = -1/2 delta_{ab} |
| `tier1_dirac_spectrum.py` | Spinor dimension | 2^4 = 16 | **CORRECT** for Cliff(R^8) |
| `r20a_riemann_tensor.py` | R(s) formula | -0.25e^{-4s} + 2e^{-s} - 0.25 + 0.5e^{2s} | **CORRECT** (matches b6 and Baptista eq 3.70) |
| `r20a_riemann_tensor.py` | K(s) formula | (23/96)e^{-8s} - e^{-5s} + (5/16)e^{-4s} + (11/6)e^{-2s} - (3/2)e^{-s} + 17/32 + (1/12)e^{4s} | **CORRECT** (verified at machine epsilon against SP-2) |
| `s19a_sweep_data.py` | SU(3) dim formula | (p+1)(q+1)(p+q+2)/2 | **CORRECT** |
| `s22a_paasch_curve.py` | phi_paasch | 1.531580 | **CORRECT** (solution to x = e^{-x^2}) |
| `s23a_kosmann_singlet.py` | Kosmann formula | K_a = (1/8) sum_{r,s} [Gamma^s_{ra} - Gamma^r_{sa}] gamma_r gamma_s | **CORRECT** (antisymmetric part, Baptista Paper 17 eq 4.1) |

---

## Stale Values Found

### 1. M_max = 2.062 (RETRACTED Session 34)
- **Origin**: `s33b_trap1_wall_bcs.py` (TRAP-33b)
- **Retracted because**: Used wrong V matrix (symmetric metric Lie derivative instead of antisymmetric Kosmann)
- **Still referenced in print statements**: `s35a_mu_physical_basis.py`, `s35a_vh_impedance_arbiter.py`
- **NOT used in any computation after S34**: All post-S34 scripts use M_max = 1.674 (MMAX-AUTH-36) or recompute
- **RISK**: NONE (retraction is clean, print statements are historical context)

### 2. M_max = 1.445 (S34 workshop estimate)
- **Referenced**: `s35_thouless_multiband.py`, `s35_ed_corrected_dos.py`
- **Superseded by**: M_max = 1.674 (8x8 multi-band, MMAX-AUTH-36)
- **RISK**: LOW (these scripts produced intermediate results that were superseded)

### 3. No stale values in root scripts
All root-level scripts (tier1, s19a, r20a, kk1, l20, s23a_kosmann) compute from first principles and do not hardcode any values that were later corrected. The Session 34 corrections (J operator, V matrix) affected how downstream scripts _used_ the data, not the data files themselves.

---

## Dependency Chains

### Chain 1: Dirac Spectrum (THE TRUNK)
```
tier1_dirac_spectrum.py (library)
  -> s19a_sweep_data.npz (21 tau, 28 irreps, 11424 eigenvalues each)
       -> s21c_V_IR.py, s22a_*.py, s22b_block_diagonal, s22c_bcs_channel_scan
       -> a5_*.py (phonon analysis)
       -> d19d_casimir_gate.py
  -> s22b_eigenvectors.npz (9 tau, eigenvectors for p+q<=3)
       -> s22b_kosmann_matrix.npz
       -> s22c_bcs_channel_scan.npz
       -> s23a_eigenvectors_extended.npz (17 downstream)
       -> s44_n3_bdg.py (tau_values only — safe)
  -> s23a_kosmann_singlet.npz (9 tau, Kosmann operators + singlet eigensystem)
       -> 63 downstream scripts (S24-S44)
       -> s23a_gap_equation.npz (12 downstream, but NONE after S32)
```

### Chain 2: Riemann Tensor
```
tier1_dirac_spectrum.py (geometry functions)
  -> r20a_riemann_tensor.npz (21 tau, full 8x8x8x8 Riemann)
       -> s21c_gb_debug*.py (Gauss-Bonnet checks)
       -> s22a_weyl_curvature.npz -> s22c_instanton_action.npz
       -> s23c_fiber_integrals.npz (10 downstream)
             -> s24a_vspec.npz
             -> s25_baptista_results, s25_einstein_results, s25_sp_results
             -> s26_baptista_bridge
             -> s31Ba_instanton_kapitza
```

### Chain 3: Bosonic Spectrum
```
kk1_bosonic_tower.py
  -> kk1_bosonic_spectrum.npz
       -> a5_*.py (phonon analysis, 7 scripts)
       -> s21c_V_IR.py
       -> s23a_precheck_3b.py
       -> d19d_casimir_gate.py (via s19a_sweep_data + kk1)
```

### Chain 4: Lichnerowicz / CW Potential
```
l20_lichnerowicz.py (also imports tier1 + r20a functions)
  -> l20_TT_spectrum.npz
       -> a5_4sector_lowmode, s22a_euclidean_action, l20_phonon_band_structure (3+)
  -> l20_vtotal_minimum.npz
       -> a5_*.py, s22a_slow_roll, s22c_landau_classification (9 total)
```

---

## Red Flags

### RED FLAG 1: E_cond Triple Inconsistency (HIGH RISK)
Three different values for BCS condensation energy used interchangeably across S35-S44:
- **-0.115**: S35 multi-sector ED (5 modes, 32 Fock states)
- **-0.137**: S36 full 8-mode ED (ED-CONV-36, converged)
- **-0.156**: GL/gap-equation derived (instanton calculations, S37-S38)

This directly contaminates:
- E_exc = 443 * |E_cond| -> 50.9 vs 60.7 vs 69.1 M_KK
- Dark matter abundance calculations
- Cosmological constant comparisons
- Friedmann equation computations

See `AUDIT_HARDCODED_CONSTANTS.md` Section 3 for full script-level tracking.

### RED FLAG 2: s23a_gap_equation.npz Used Pre-Correction (LOW RISK)
The V matrix stored in `s23a_gap_equation.npz` was computed from K_a (antisymmetric Kosmann), which is CORRECT. The Session 34 retraction was about `s22b_kosmann_matrix.npz` using the SYMMETRIC metric Lie derivative operator — a different file. The s23a gap equation was always correct.

However, 6 scripts (s31Ca, s31Cb, s31Cf, s32a x2) load this file. They pre-date the S34 correction session but their V matrices are from the correct Kosmann formula. No action needed.

### RED FLAG 3: Orphan Data Files (NEGLIGIBLE)
Two .npz files have no consumers:
- `s19a_omega.npz` — likely an intermediate computation artifact
- `s19a_R_reg.npz` — likely a regularized spectral sum

These don't affect anything downstream.

### RED FLAG 4: s22b_eigenvectors.npz vs s23a_kosmann_singlet.npz (LOW RISK)
`s22b_eigenvectors.npz` contains eigenvectors computed at the SAME tau values and with the SAME Dirac operator as `s23a_kosmann_singlet.npz`. The difference is:
- s22b: Stores eigenvectors for ALL sectors (p+q <= 3), 1232 modes per tau
- s23a_kosmann: Stores eigenvectors only for (0,0) singlet (16 modes) + Kosmann matrices

One S44 script (`s44_n3_bdg.py`) loads s22b_eigenvectors.npz, but only uses the `tau_values` array (grid coordinates). The eigenvectors themselves are not referenced from this file. SAFE.

### RED FLAG 5: Numerical Coincidence m_tau = 2.062 = retracted M_max (NEGLIGIBLE)
The tau modulus mass m_tau = 2.062 M_KK (computed in S42 from V''/Z = 317863/74731) numerically equals the retracted M_max = 2.062 (S33b). This is a pure coincidence — different physical quantities from independent computations. No downstream confusion was found: scripts use m_tau contextually (mass) not as a Thouless eigenvalue.

---

## Mathematical Correctness of Root Scripts

### tier1_dirac_spectrum.py — CORRECT
- Clifford algebra: Standard inductive construction. `{gamma_a, gamma_b} = 2 delta_{ab}` validated.
- Jensen metric: Volume-preserving (L1*L2^3*L3^4 = e^0 = 1). Correct decomposition su(3) = u(1) + su(2) + C^2.
- Orthonormal frame: E = inv(cholesky(g_s)). Correct: E @ g_s @ E^T = I.
- Connection: Koszul formula `2 Gamma_{cab} = ft_{abc} - ft_{bca} + ft_{cab}`. Correct.
- Metric compatibility: Gamma^c_{ab} + Gamma^b_{ac} = 0 validated numerically.
- Spin connection: Omega = (1/4) sum_{a,b,c} Gamma^b_{ac} gamma_a gamma_b gamma_c. Correct.
- Dirac operator: D_pi = sum_{a,b} E_{ab} (rho(X_b) tensor gamma_a) + I tensor Omega. Correct.
- Peter-Weyl multiplicity: dim(p,q) applied per eigenvalue. Correct.

### r20a_riemann_tensor.py — CORRECT
- Riemann formula: R^d_{abc} = Gamma^e_{bc} Gamma^d_{ae} - Gamma^e_{ac} Gamma^d_{be} - ft^e_{ab} Gamma^d_{ec}. Standard for left-invariant metrics on Lie groups.
- Validation: 7 tests at all 21 tau values (antisymmetry, pair exchange, Bianchi, Ricci, scalar curvature, Kretschner). All pass to machine epsilon.
- Scalar curvature matches analytic formula from SP-2.
- Kretschner matches analytic formula from SP-2.

### s23a_kosmann_singlet.py — CORRECT
- Kosmann formula: K_a = (1/8) sum_{r,s} [Gamma[s,r,a] - Gamma[r,s,a]] gamma_r gamma_s.
- Correct distinction from metric Lie derivative (symmetric part) used erroneously in S22b.
- Extensive derivation in docstring working through the conventions carefully.
- Killing directions (U(2)) have nonzero K_a (expected: Kosmann correction for Killing vectors is the spin connection term, not zero). Non-Killing directions (C^2) also have nonzero K_a.

### kk1_bosonic_tower.py — CORRECT
- Scalar Laplacian on SU(3) via Peter-Weyl: verified against Casimir at s=0.
- Vector Laplacian via Weitzenbock: Delta_1 = nabla*nabla + Ric.
- Bosonic spectrum at s=0 matches known Casimir values: C_2(p,q) = (p^2+q^2+pq+3p+3q)/3.

---

## Summary

**Verdict: The foundational S7-S24 scripts are CLEAN.**

1. **No physical constant errors**: Root scripts work entirely in dimensionless geometric units on SU(3). No G_N, hbar, or M_Planck to get wrong.

2. **Mathematical constructions verified**: Dirac operator, Riemann tensor, Kosmann correction, and KK spectrum all implement the correct formulas with extensive validation suites.

3. **No stale values in roots**: The S34 corrections (J operator, V matrix) affected how downstream scripts _interpreted_ the data, not the root data itself. The root .npz files are computed from scratch and remain correct.

4. **The main contamination risk is E_cond (downstream, S35+)**: Three different values (-0.115, -0.137, -0.156) are used inconsistently across active scripts. This is NOT a root-level problem — it comes from different ED computations in S35-S37, each legitimate but at different truncation levels. However, scripts that hardcode one value while citing a different session as source are error-prone.

5. **Dependency structure is sound**: The 63 scripts that load `s23a_kosmann_singlet.npz` all use the CORRECT (antisymmetric Kosmann) data. No script after S34 loads the retracted `s23a_gap_equation.npz`.

6. **Key numerical values are stable**:
   - tau_fold = 0.190 (consistent everywhere)
   - phi_paasch = 1.531580 (never changed)
   - M_max = 1.674 (authoritative since S36, used consistently in S37+)
   - S_inst = 0.069 (consistent everywhere)
