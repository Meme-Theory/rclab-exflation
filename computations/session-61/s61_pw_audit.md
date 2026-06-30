# S61 BAP-5: PW Data Audit — (1,2) Irrep Contamination Scope

**Gate**: PW-AUDIT-61 (INFO)
**Author**: baptista-spacetime-analyst
**Date**: 2026-03-28
**Verdict**: INFO — 41 contaminated scripts identified, 122 safe, 10 utility

## 1. Background

Session 44 script `s44_dos_tau.py` computes the multiplicity-weighted phonon DOS across 5 tau values, drawing eigenvalue data from `s27_multisector_bcs.npz` and `s36_sfull_tau_stabilization.npz`. The sector list used:

```
(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1)
```

This is 9 sectors with p+q <= 3. The **10th sector** satisfying p+q <= 3 is **(1,2)**, which is the CPT-conjugate of (2,1). It has dim(1,2) = 15, dim^2 = 225, spinor_dim = 240.

The upstream source `s27_multisector_bcs.py` correctly documents this omission (line 35: "(1,2) is conjugate to (2,1): skip and double (2,1) contribution") and defines `MULT_21_EFFECTIVE = 450` for its internal F_total computation. **However, s44_dos_tau.py does NOT propagate this doubling.** The stored dim2 arrays assign weight 225 to (2,1) modes instead of the correct 450.

## 2. Quantitative Impact

| Quantity | Current (wrong) | Corrected | Error |
|:---------|:----------------|:----------|:------|
| n_physical (total modes) | 101,984 | 155,984 | **-34.6%** (or +52.95% correction) |
| (2,1) sector weight | 240 x 225 = 54,000 | 240 x 450 = 108,000 | **factor 2** |
| Missing modes | 0 | 54,000 | — |
| Fraction of total | 53.0% of current | 34.6% of corrected | — |

The correction magnitude for any specific quantity depends on the (2,1) sector's eigenvalue distribution relative to the full spectrum. For total counts (a_0, n_physical), the correction is exactly 52.95%. For weighted averages (mean_omega, omega_rms), the correction is smaller (~5-15%) because the (2,1) eigenvalues are distributed across the same range as other high-multiplicity sectors. For spectral action coefficients (a_2, a_4), the correction depends on the (2,1) eigenvalue positions relative to the weighting function.

**Key point**: Since (1,2) is CPT-conjugate to (2,1), its eigenvalues are **identical**. The correction is therefore exactly equivalent to doubling the (2,1) weight from 225 to 450 in all dim2 arrays. No recomputation of eigenvalues is needed.

## 3. Contamination Classification

### 3.1 CONTAMINATED Scripts (41 total)

Scripts that use dim2-weighted cross-sector sums from s44_dos_tau.npz data. Results from these scripts require recomputation or post-hoc correction.

| Script | Location | Session | Usage | Estimated Correction |
|:-------|:---------|:--------|:------|:--------------------|
| `s43_phonon_dos.py` | archive | S43 | rho_w, hist_w, n_physical (42 PW ops) | 53% (total count) |
| `s44_dos_tau.py` | archive | S44 | **ROOT CAUSE** — rho_w, mean_omega, all outputs (56 ops) | 53% |
| `s44_bayesian_f.py` | archive | S44 | n_physical count (6 ops) | 53% |
| `s44_lifshitz_eta.py` | archive | S44 | vh_rho (1 op) | up to 53% |
| `s44_vanhove_track.py` | archive | S44 | rho_smooth, all_dim2 histograms (8 ops) | ~53% in (2,1) bins |
| `s45_acoustic_ns.py` | archive | S45 | n_physical per sector (2 ops) | 53% |
| `s45_debye_waller.py` | archive | S45 | dim2-weighted averages (3 ops) | ~5-15% |
| `s45_fwd_bwd_ns.py` | archive | S45 | dim2 * P_total, weighted sums (18 ops) | ~53% |
| `s45_kz_ns.py` | archive | S45 | dim2 * beta2 particle number (21 ops) | ~53% |
| `s45_kz_ns_crosscheck.py` | archive | S45 | dim2 * beta2 weighted (24 ops) | ~53% |
| `s45_kz_ns_kmap.py` | archive | S45 | dim2 * beta2 EIH-weighted (12 ops) | ~53% |
| `s45_occ_spectral_crosscheck.py` | archive | S45 | rho_smooth, dim2-weighted shell (8 ops) | ~53% |
| `s45_truncated_torsion.py` | archive | S45 | dim2_fold.sum (2 ops) | up to 53% |
| `s46_anomalous_dispersion.py` | archive | S46 | dim2 mode counts (4 ops) | up to 53% |
| `s46_fwd_bwd_ns.py` | archive | S46 | dim2 * P weighted (2 ops) | up to 53% |
| `s46_landau_zener_ns.py` | archive | S46 | dim2 * P_k particle number (9 ops) | ~53% |
| `s46_nonsinglet_dissipation.py` | archive | S46 | dim2 * v_k^2 coupling, dissipation (26 ops) | up to 53% |
| `s46_spectral_flow_ns.py` | archive | S46 | dim2 * P_total spectral flow (6 ops) | up to 53% |
| `s47_spectral_flow_ns.py` | archive | S47 | dim2 spectral flow (2 ops) | up to 53% |
| `s47_spectral_landscape.py` | archive | S47 | dim2 sector totals (6 ops) | up to 53% |
| `s48_berry_complete.py` | archive | S48 | rho_smooth, vh_rho (8 ops) | ~53% |
| `s48_curv_extend.py` | archive | S48 | mean_omega_vs_tau (1 op) | ~5-15% |
| `s48_paasch_backlog.py` | archive | S48 | dim2 sum check (2 ops) | up to 53% |
| `s48_volovik_string.py` | archive | S48 | dim2 histograms, spectral heat (7 ops) | up to 53% |
| `s51_cutoff_conv.py` | archive | S51 | dim2 cutoff weights (2 ops) | up to 53% |
| `s51_strutinsky.py` | archive | S51 | dim2 Strutinsky smoothing (9 ops) | up to 53% |
| `s42_fabric_wz.py` | archive | S42 | rho_smooth (2 ops) | ~53% |
| `s42_fabric_wz_v2.py` | archive | S42 | rho_smooth (10 ops) | ~53% |
| `s52_ddg_mkk.py` | computation | S52 | dim2 mode labeling + count (2 ops) | minor (label use) |
| `s52_wdavg_ds.py` | computation | S52 | dim2-weighted spectral sums (6 ops) | 53% |
| `s54_sft_cutoff.py` | computation | S54 | dim2-weighted a_0, a_2, a_4 (37 ops) | 53% for a_0 |
| `s54_threshold.py` | computation | S54 | dim2 sector counts (2 ops) | up to 53% |
| `s55_bogoliubov_992.py` | computation | S55 | dim2 * beta_sq particle number (4 ops) | 53% |
| `s55_erich_continuum.py` | computation | S55 | rho_smooth, dim2 continuum (2 ops) | ~53% |
| `s55_euclid_continuum.py` | computation | S55 | dim2 * ln_terms partition function (14 ops) | up to 53% |
| `s55_ladder_test.py` | computation | S55 | dim2 weighted sums (8 ops) | up to 53% |
| `s55_self_consistent.py` | computation | S55 | dim2-weighted partition (4 ops) | 53% |
| `s55_sf_sign.py` | computation | S55 | dim2 * n_k * lambda occupation (13 ops) | up to 53% |
| `s59_spinor_norm.py`* | computation | S59 | += d2 * w Seeley-DeWitt sums (per sector) | 53% for totals |
| `s60_a4_trace.py`* | computation | S60 | += d2 * w Seeley-DeWitt sums (per sector) | 53% for totals |

\* Scanner initially classified as SAFE; manual review revealed `+= d2 * w` contamination pattern.

Note: `s61_pw_audit.py` (this scanner) is a false positive — it contains contamination pattern strings in its own source code.

### 3.2 SAFE Scripts (122 total)

Scripts that use only eigenvalue positions (gaps, extrema, ranges), per-sector calculations without cross-sector PW summation, eigenvalue metadata, or dim2 only as a sector label/mask.

Key safe categories:
- **S27-S29 BCS scripts** (20 scripts): Use s27 eigenvalues directly, work per-sector. s27 correctly handles (1,2) doubling internally.
- **S33-S43 pre-DOS scripts** (25 scripts): Use eigenvalue positions, per-sector BCS, or metadata only.
- **S44 analysis scripts** (12 scripts): Use eigenvalue positions (gaps, induced_g, sakharov, etc.) not weighted sums.
- **S45-S51 per-sector scripts** (25 scripts): Berry phase, analytic torsion, qtheory, sigma select — per-sector.
- **S52 structure scripts** (10 scripts): casimir_josephson, eta_b, log_signed, msw_transit, etc.
- **S53-S60 eigenvalue scripts** (10 scripts): b1_soft_mode, brody_parameter, eliashberg_sector, strutinsky_992.
- **S60 PW convergence** (1 script): `s60_pw_h0_conv.py` computes its own eigenvalues from scratch for ALL irreps including (1,2) — independently correct.

### 3.3 Secondary Contamination Path

One archive script (`s45_dos_fine_scan.py`) independently recomputes eigenvalues from the Dirac operator but uses the same 9-sector list with (1,2) missing. This is contaminated through the **sector list**, not through s44_dos_tau.npz. This secondary path may affect other scripts that compute their own eigenvalues using hardcoded sector lists copied from s27/s44.

## 4. Impact on PROVEN Results

Cross-referencing the 16 PROVEN results from the framework status:

| PROVEN Result | Affected? | Reason |
|:-------------|:----------|:-------|
| KO-dim=6 | NO | Representation theory, not eigenvalue sums |
| SM quantum numbers | NO | Per-irrep assignment |
| [J,D_K]=0 CPT | NO | Algebraic identity |
| g1/g2=e^{-2tau} | NO | Coupling ratio, not PW sums |
| 67/67 Baptista | NO | Reproduces Baptista's results exactly |
| Volume-preserving TT | NO | Geometric constraint |
| Riemann 147/147 | NO | Curvature components |
| TT stability | NO | Per-sector eigenvalue analysis |
| phi_paasch=1.531580 | NO | Single-sector (B2) computation |
| AZ class BDI | NO | Symmetry classification |
| D_K block-diagonal | NO | Matrix structure |
| Trap 3 | NO | Conceptual/geometric |
| Perturbative Exhaustion | NO | Theorem about mechanisms |
| DNP instability | NO | Dynamical nucleation |
| Pomeranchuk | NO | Per-sector analysis |
| Clock constraint | NO | Geometric |

**None of the 16 PROVEN results are contaminated.** They all concern algebraic structure, per-sector properties, or geometric constraints that do not involve cross-sector PW-weighted sums.

## 5. Impact on Gate Verdicts

The contamination primarily affects:
1. **Total particle number estimates** (S45-S46 KZ/Bogoliubov): These report n_pair values that are ~53% too low.
2. **Spectral action coefficients** (S54 SFT): a_0 undercount by 53%, a_2/a_4 similarly affected.
3. **DOS-derived quantities**: weighted means, rms, Strutinsky corrections.
4. **Partition function computations** (S55): thermodynamic quantities scaled by wrong total.

Most of these were used as diagnostic/exploratory computations, not as decisive gate verdicts. The critical mechanism chain results (BCS gap, Pomeranchuk, instanton gas) are per-sector or use only eigenvalue positions, and are unaffected.

## 6. Correction Strategy

**Recommended: Post-hoc correction (Option B)**

Since (1,2) eigenvalues are identical to (2,1) eigenvalues by CPT, the correction for any s44-derived quantity is:
```
For all dim2 arrays: replace entries where dim2 == 225 with dim2 = 450
```
This is equivalent to doubling the Peter-Weyl multiplicity of the (2,1)/(1,2) combined sector.

No upstream eigenvalue recomputation is needed. Downstream scripts can be corrected by:
1. Loading s44_dos_tau.npz
2. Replacing `dim2[dim2 == 225] = 450`
3. Recomputing all weighted sums

Priority for recomputation:
- **HIGH**: s54_sft_cutoff.py (spectral action), s55_bogoliubov_992.py (particle number), s55_euclid_continuum.py (partition function)
- **MEDIUM**: s45_kz_ns*.py (Kibble-Zurek), s51_strutinsky.py (shell corrections)
- **LOW**: Archive-only scripts no longer in the active computation chain

## 7. Summary Statistics

- **Total scripts scanned**: 173 (referencing s44 data)
- **CONTAMINATED**: 41 (including 2 manual reclassifications)
- **SAFE**: 122
- **UTILITY**: 10 (inspection/debug, no physics output)
- **PROVEN results affected**: 0 / 16
- **Correction magnitude**: 52.95% increase in total PW weight (54,000 / 101,984)
- **Data files**: `computations/session-61/s61_pw_audit.py` (scanner), this report

**Gate verdict: PW-AUDIT-61 INFO** — contamination scope mapped; no PROVEN results affected; 41 scripts flagged for correction; post-hoc fix available.
