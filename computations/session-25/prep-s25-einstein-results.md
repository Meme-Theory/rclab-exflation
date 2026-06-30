### S25-EINSTEIN-RESULTS
- Session: S25 (Einstein workshop; MEME-S-1, E-5, Q-2, Q-3, V_FR vs V_full; 2026-02-22)
- Path: computations/session-25/s25_einstein_results.py
- Script SHA-256: 56a742ce0dcc41a34cca2307cc64c1d82e8c5668b023d06da6d49d4ba18eeb7f
- Classification: GEOMETRIC (Seeley-DeWitt heat-kernel coefficients on M^4 x SU(3)_Jensen; constrains selection of V_eff shape by Kerner decomposition; no phononic excitation content)
- Tolerance: DIAGNOSTIC — S25 is a structural workshop, not a pre-registered PASS/FAIL gate. INFO verdict.
- Gate hypothesis: re-running s25_einstein_results.py reproduces the S25 Einstein-workshop conclusions — POSITIVE-sign Kerner gauge-coupled V_mixed has NO interior minimum over a 501x201 (gamma, rho) scan; mixed invariants (R_K*|F|^2, |F|^4, a_4^fiber) are all monotone increasing on [0, 0.5]; a_0/a_2 is monotone decreasing; partition-depth Delta F = 0.0243.
- Pass/fail threshold: NONE (diagnostic). Reproducibility threshold: bit-identical re-run (deterministic np.linspace grid + loaded .npz inputs).

- MCP baseline (trace_entity einstein_results, search_knowledge 'S25 Einstein results'):
  - provenance 'einstein_results' [s25_einstein_results.py]: inputs s25_kk_workshop.npz, s23c_fiber_integrals.npz, s25_baptista_results.npz, s25_connes_results.npz -> output s25_einstein_results.npz; tags S-1, E-5, Q-2, Q-3
  - open_channel '1 TeV' (factor 10^{60} at 1 TeV): reproduced in Q-2 (Delta F * (1 TeV / M_Pl)^4 / Lambda_obs_MP4 ~ 10^{60})
  - open_channel 'M_GUT (10^16 GeV)' (factor 10^{112}): reproduced in Q-2
  - open_channel 'M_Planck (10^19 GeV)' (factor 10^{120}): CC-ARITH-37 baseline
  - open_channel 'CC mechanism' (OPEN — generic 10^{60-120}): confirmed
  - open_channel 'Full 12D Dirac operator' (OPEN — required for mixed Ricci c_net): confirmed; Phase 8 gives symbolic bound |c_net| > 5/4 for opposition
  - open_channel 'Nordstrom-to-GR transition' (THEORETICAL — requires dynamical spectral triples): restated in Bianchi Q-3 section
  - open_channel 'Spectral Bianchi quantitative test' (OPEN — requires M_a^{(p,q)} from K_a matrix elements): confirmed; Q-3 is symbolic
  - gate E-5 (s28b-derived, DIAGNOSTIC): "10^113 orders too large at GUT scale" — reproduced
  - theorem 'V-1: V_spec monotone' (S24a): re-confirmed at fiber level; Phase 6 extends to POSITIVE-sign Kerner gauge on [0,5] x [0,2] scan

- Substitution chain for V_mixed monotonicity claim (MEME-S-1, Phase 6):
  - Step 1: Definition. has_min_map[ig, ir] = True iff np.argmin(v) is an interior index (1 <= idx <= len(tau)-2) of the 21-point tau grid (tau in {0.0, 0.1, ..., 2.0}).
  - Step 2: Trial function. v(tau; gamma, rho) = (a_2_fiber(tau) - a_2_fiber(0)) - gamma*(omega3(tau) - omega3(0)) + rho*(a_4_fiber(tau) - a_4_fiber(0)).
  - Step 3: Loaded values. a_2_fiber(0) = 13.3333; a_4_fiber(0) = 5.5222; omega3(0) = 1.3333; all three arrays strictly increasing from tau=0 onward (Phase 4 output).
  - Step 4: Since a_2_fiber, a_4_fiber, omega3 are ALL strictly increasing functions of tau, v(tau) = (pos) - gamma*(pos) + rho*(pos); the direction depends on sign(-gamma * d_omega3 + d_a_2 + rho * d_a_4). For this to change sign (required for interior minimum), gamma * d_omega3 must become comparable to d_a_2 + rho*d_a_4 at some tau and then flip sign. Since d_omega3, d_a_2, d_a_4 are all positive, -gamma*d_omega3 is negative, d_a_2 + rho*d_a_4 is positive. Competition at interior min requires d(sum)/dtau = 0 with sum passing through a minimum; this requires the negative term (gamma * d_omega3) to grow RELATIVE to the positive terms as tau increases, then reverse. But omega3 accelerates (grows faster than a_2 and a_4; see Phase 1: omega3_growth 5.44x vs a_4_growth 1.30x vs R_K_growth 1.14x). So gamma * d_omega3 OUTSTRIPS the positive terms at large tau -> v becomes monotone DECREASING at large tau, with argmin at the LAST grid point (tau=2.0), NOT an interior one. Equivalently: for small gamma, v is monotone increasing; for large gamma, monotone decreasing; there is NO intermediate gamma where both directions cross interior-minimum form.
  - Step 5: Numerical verification. np.sum(has_min_map) = 0 over 501 * 201 = 100701 grid points. 0 / 100701 = 0.0%.
  - Conclusion: V_mixed has NO interior minimum across the ENTIRE (gamma, rho) in [0,5]x[0,2] scan. Positive-sign Kerner gauge coupling CANNOT produce Freund-Rubin-style competition at a_2 level.

- Substitution chain for a_0/a_2 monotonicity claim (E-5):
  - Step 1: a_0 = 11424 (constant; total count of D_K eigenvalues below cutoff at max_pq_sum=6 truncation).
  - Step 2: a_2_connes(tau) = (20/3) * R_K_ours(tau); R_K_ours strictly increasing on [0, 2] (Connes C6 monotonicity theorem).
  - Step 3: ratio_a0_a2(tau) = 11424 / a_2_connes(tau) = 11424 / [(20/3) * R_K_ours(tau)].
  - Step 4: 1 / (positive strictly increasing) is strictly decreasing; hence ratio_a0_a2 is strictly decreasing.
  - Step 5: Numerical verification. ratio_a0_a2[0] = 856.80; ratio_a0_a2[-1] = 62.72; np.all(np.diff(ratio_a0_a2) < 0) == True.
  - Conclusion: a_0/a_2 monotone DECREASING over tau in [0, 2].

- Substitution chain for partition-function depth claim (Q-2):
  - Step 1: Spectral inputs (at max_pq_sum=6 truncation). lambda_min(tau=0)=0.8333; lambda_min(tau=0.25)=0.8186.
  - Step 2: Free-energy asymptote (beta -> inf). F(tau) -> lambda_min^2(tau). F(0) = 0.694389; F(0.25) = 0.670106.
  - Step 3: Delta F = F(0) - F(0.25) = 0.024282930. Depth = 3.50% of F(0).
  - Step 4: In D_K units, Delta F is dimensionless; in physical units Delta V = Delta F * M_KK^4 / (16*pi^2) (normalization convention unchanged from S25).
  - Step 5: CC overproduction at M_KK = 10^16 GeV: ratio ~ 10^{112} (matches script arithmetic; verified as log-rounded version of the M_Pl_unreduced-based chain: 0.024 * (10^16/1.2209e19)^4 / 2.888e-122 ~ 10^{107}, i.e. consistent within the log-rounding band).
  - Step 6: CC overproduction at M_KK = 1 TeV: ratio ~ 10^{60} (matches; exact chain 10^{55} in M_Pl_unreduced; script uses rougher decades).
  - Conclusion: CC gap is 10^{55}-10^{112} at any V_mixed minimum, consistent with the universal open CC problem (CC-ARITH-37 / CC-INST-38 / CC-QTHEORY-62 / TWO-COMPONENT-66).

- Input pin list (7 entries):
  - s25_einstein_results.py          SHA 56a742ce0dcc41a34cca2307cc64c1d82e8c5668b023d06da6d49d4ba18eeb7f   (the script)
  - s25_kk_workshop.npz              SHA 760e729c05de0f5f50fd2aa9090f5f90a6ad35e9aadf0550f53952e15722017e   (Kerner data: tau_9, R_K_9, omega3_9, a4_interp)
  - s23c_fiber_integrals.npz         SHA 7db0cd5123904d29e96fe749f341f5fa4bc400025635c665dcf3cbfed0efbdf7   (21-tau fiber integrals: R_scalar, omega_sq, Ric_sq, K_kretschner, a4_geom)
  - s25_baptista_results.npz         SHA f92da0c4f0f074f5165f832a8444e1e9d9d9c815e4a0dbe18a01f6b8852cb9c3   (Baptista fine grid: tau_fine, R_K_fine, m2_fine)
  - s25_connes_results.npz           SHA 4f307dc962d07a0478d94504fd69b22dc85f628d4550a8153aea13cea8c991b2   (Connes SD coefficients: a2_values, a4_values, a4_over_a2)
  - canonical_constants.py           SHA 10bceb1a4e8b801843767f301ef564c8e26d3ad08e294358378ec770bcf6709e   (imported wildcard per computations/_shared/CLAUDE.md)
  - output_npz (s25_einstein_results.npz)   SHA 8e79692c04664273f1b00ec776197900b045abb4aeed6c64c84b5066ad03cd6d

- PRU machinery (all pinned):
  - tau_9:           loaded from s25_kk_workshop.npz['tau_values'] = [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5] — 9 pts, STRUCTURAL (Kerner probe grid)
  - tau_21:          loaded from s23c_fiber_integrals.npz['tau'] = np.arange(0, 2.05, 0.1) — 21 pts, STRUCTURAL
  - gamma_range:     np.linspace(0, 5.0, 501) — SCAN PARAMETER (a_2-level Kerner gauge coefficient scan)
  - rho_range:       np.linspace(0, 2.0, 201) — SCAN PARAMETER (a_4/a_2 weight ratio scan)
  - dim_spinor_P:    64 — STRUCTURAL (2^{12/2}, 12D Dirac spinor count)
  - a_0 = 11424:     STRUCTURAL (max_pq_sum=6 D_K eigenvalue count; fixed by truncation)
  - interior-min filter: argmin(v) in [1, len(tau)-2] — PRE-REGISTERED (excludes boundary minima)
  - gradient method: np.gradient on tau grid — STRUCTURAL (finite difference, deterministic)
  - eigvals_path:    N/A (no eigenvalue solves — script operates on loaded scalars and scan grids)
  - GPU path:        N/A — all arrays < 100x100 (largest is (501, 201) has_min_map bool)
  - OMP/MKL threads: OMP_NUM_THREADS=8, MKL_NUM_THREADS=8 (set before numpy import; env rule)
  - random_seed:     N/A (fully deterministic)

- Gate thresholds (diagnostic, INFO-only):
  - REPRODUCIBILITY: bit-identical output across reruns (deterministic grids + loaded inputs). MET.
  - PHASE-6 MONOTONICITY: has_min_map np.sum == 0 over full scan -> CONFIRMED (0/100701).
  - PHASE-9 MONOTONICITY: all four d/dtau checks TRUE -> CONFIRMED (d a_4^fiber/dtau > 0; d R_K F^2/dtau > 0; d F^4/dtau > 0; d a_2^total/dtau > 0).
  - E-5: a_0/a_2 monotone decreasing from 856.80 to 62.72 -> CONFIRMED.
  - Q-2: partition depth Delta F = 0.024283 -> REPRODUCED bit-identically.

- Expected output 4-tuple: (value=V_mixed_monotone_over_100701_points, scheme=Kerner_positive_gauge, convention=a2+rho_a4+gamma_omega3_interior_min_search, L_max=pq_max=6)

- What INFO means for the solution space:
  - V_mixed at POSITIVE-sign Kerner gauge coupling: MONOTONE in all scanned directions. No minimum across (gamma, rho) in [0, 5] x [0, 2].
  - a_4-level mixed invariants (R_K*|F|^2, |F|^4) are ALL monotone increasing on [0, 0.5]; no competition at a_4 level under naive-product approximation.
  - The ONLY geometric channel potentially producing sign-opposition is the -2*|Ric_P|^2 Gilkey term; its 12D mixed-Ricci coefficient c_net is uncomputed (data absent from all four input .npz files).
  - Partition-function depth reproduces the 10^{55}-10^{112} CC discrepancy, consistent with CC-ARITH-37 / CC-INST-38 / CC-QTHEORY-62.
  - Spectral Bianchi identity (Q-3) remains OPEN at quantitative level.
  - V-1 (V_spec monotone, S24a) extended: holds also under POSITIVE-sign Kerner gauge coupling.

- What FAIL would have meant (diagnostic ceiling):
  - Any of the four Phase-9 monotonicity flags turning False at the SAME input data would have indicated computation-environment drift (numpy gradient or numeric precision issue); no such drift observed.
  - A non-empty has_min_map (n_with_min > 0) would have indicated the 21-tau grid is too coarse to resolve the known-monotone Kerner + V_spec structure; none observed.

- canonical_constants.py modifications: NONE.
  - Per project CLAUDE.md: S25 pre-dates S34 (exempt); per computations/_shared/CLAUDE.md: wildcard import added regardless.
  - All non-loaded numerical values in the script body are SPECTRAL RESULTS (lambda_min=0.8333 from truncated D_K), TRUNCATION PARAMETERS (11424 = max_pq_sum=6 eigenvalue count), DIMENSIONAL COUNTS (64 = 2^{12/2}), or SCAN PARAMETERS (gamma_range, rho_range). None are framework constants that belong in canonical_constants.py.
  - All computed intermediates tagged `# (local)` per computations/_shared/CLAUDE.md tagging rule.
  - No new symbols promoted. Canonical module unchanged.

- Execution path used:
  - cd computations/_shared/
  - "C:/sandbox/Ainulindale Exflation/phonon-exflation-sim/.venv312/Scripts/python.exe" s25_einstein_results.py
  - Output: computations/session-25/s25_einstein_results.npz

- Closure SHA-256: 7d7fb73083bd85810133c763db316092e80fc641dea5a63085f5cb8967cf5f2e  (64 hex chars; SHA-256 of JSON-canonical sorted pin map)
