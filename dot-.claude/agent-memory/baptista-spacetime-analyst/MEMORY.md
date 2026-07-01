# Baptista Spacetime Analyst Memory

KK geometry on SU(3): Jensen deformation, fiber integration, Dirac operator D_K. Baptista corpus at `researchers/Baptista/` (papers #13-#18 critical KK; full index at `researchers/Baptista/index.md`).

## Active Context

- Cross-session gate verdict ledger lives in `computations/s{N}_gate_verdicts.txt` (CANONICAL — do not duplicate here).
- Canonical numerical constants live in `computations/_shared/canonical_constants.py` (query via `mcp__knowledge__.get_constant`).
- Project-level registries (falsifier-master-inventory, permanent-results, alpha-s-protection, branch-iv-canonical, w0-primary-decision-rule, etc.) live in `sessions/framework/registry/`.
- Working papers + per-session synthesis live in `sessions/session-{N}/`.

## Reference Index

- [permanent-results.md](permanent-results.md) — 16 proven theorems (machine epsilon), permanent spectral results, selection rules, J/gamma_9/CPT decomposition, constraint landscape, Baptista-Berry conjecture
- [paper-index-and-conventions.md](paper-index-and-conventions.md) — Baptista paper groupings, KK arXiv IDs, key equation references, 5D moduli parameterization, infrastructure notes, workflow lessons
- [open-problems.md](open-problems.md) — alpha_s tension, Weinberg angle, metric positivity, CC, A_s, observational status table, active workshop insights, S76 carry-forward. STALE SNAPSHOT (≤S76): its status table (e.g. alpha_s "FAIL", Weinberg "FAIL") is SUPERSEDED by later verdicts (alpha_s resolved S93 W7-1) — cross-check source/MCP before citing, per [[memory-is-stale-snapshot]]
- [feedback_memory-is-stale-snapshot.md](feedback_memory-is-stale-snapshot.md) — memory is a snapshot; recorded session verdicts + knowledge MCP win on conflict (user correction S95-era)
- [early-sessions.md](early-sessions.md) — Compressed S3-S51: foundations, NCG phases, D_phys, PMNS, mechanism chain, atlas
- [s80_w0_15_branch_shortfall.md](s80_w0_15_branch_shortfall.md) — Most recent unique substrate-side correction (refutation of phonon-first 1D-K-cut diagnosis; rank-universality slot map)
- [sx_w8_crystal_geometry_viz.md](sx_w8_crystal_geometry_viz.md) — Crystal-geometry viz expansion S47→S93: curvature-convention quartet (D8), dead-import findings, 4 figure-warranted post-S47 results (E1-E4), D6 supersession-orphan
- [fermion-hierarchy-fiber-overlap.md](fermion-hierarchy-fiber-overlap.md) — S99 panel + S100a W2-1 PASS + W2-2 INFO: dual-Z₃ {1/9,1/3,1/3}; overlap COMPUTED — hierarchy exponent is LAPLACIAN-graded, not Dirac-floor-graded (floors crowd = S97 wall; scalar channel carries 9/5); |w|=1/√6 all φ, arg(w)=Z₃ phase exact; center-Z₃ selection rules; plan-label traps (cache min/max, band-edge inversion)
- [tau0-operator-is-levi-civita.md](tau0-operator-is-levi-civita.md) — S100b W3-2 FAIL(STRUCTURED): D_K(τ=0) is LC t=1/2, NOT Kostant cubic; t=1/2 closed form verified 9e-15; cubic point has a₂=a₄=a₆≡0; n/36 derived; Lai-Teh row-8 erratum
- [inv2-w1-1-rank1-wall-genuine.md](inv2-w1-1-rank1-wall-genuine.md) — INV2-W1-1 FAIL: rank-1 Yukawa wall is GENUINE (not Schur artifact) under minimal su(2)-split modulus; gen degeneracy protected deeper than U(2); su(2)-split lifts ISOSPIN (22→30) not generation; method trap (gen copies ≠ smallest signed evals; project onto fixed same-sign degenerate multiplet); deformed_su2_split_metric helper; CF=C²-anisotropy modulus
- [s114_w2_1_kpivot_edge_transfer_deg0_samepole.md](s114_w2_1_kpivot_edge_transfer_deg0_samepole.md) — S114 W2-1 INFO: BZ-edge→K* transfer degree EXTRACTED = 0 (SAME-pole, EVEN); α_s/d_s +2 is a DIFFERENT (two-pole) observable, NOT importable onto a scale-ratio (dedup-flag-iii); deg-0 trivial-on-ratio (cancellation thm) ⇒ 1.6625-dec contraction unaccounted; same-pole-vs-cross-pole flow discriminator
- [s117_w3_4_offjensen_u2_sharing.md](s117_w3_4_offjensen_u2_sharing.md) — S117 W3-4 PASS-RESOLVED: off-Jensen U(2) moduli dim=1+k_coset=5; phi_88 (lambda_8 U(2)-CENTER singlet) INDEPENDENT of eps_LX (CP^2 coset doublet) ⇒ K7-transit survives real eps_LX. Reusable: U(2)-isotropy IRREP-TYPE (singlet vs doublet) is the moduli-sharing discriminator, NOT generator commutators
- [s116-branch-iv-l15-fb-scope.md](s116-branch-iv-l15-fb-scope.md) — S116 W9 INFO + TERMINAL WORKSHOP RESOLVED: branch-(iv) w0_FW DR3 at p+q=15 (spread_CAC{13,14,15}=0.039290). FB-saturation SCOPE caveat (bottom-K + bulk low-|λ| ⊥ λ_max-driven w0 Zubarev moment — do NOT cite FB to claim w0 DR3 "saturated"); GT bosonic-ladder bit-exact vs Casimir-projection cache at p=15 (sentinel 0.0); INV13 cross-track full-window match. W9 fork RESOLVED as EXACT decomp ρ_B=mean_Z/λ_max−1 (numerator⊥denominator; both canonical, observable-DEPENDENT redundancy; channel split 100.081%/−0.081%; law |d|=μb/λ_max² Sage-ratio 1.00081) + Weyl-FORCED anchor-fidelity gap w0_cac→−1.340827 (separate Level-3 ≠ Level-2 L_max-stability; fix=de-reference-the-edge per reading-(B); →CF-S117-W0-ANCHOR-FIDELITY + CF-S117-BRANCH-IV-L16)
- [branch-iv-lambda-max-driven.md](branch-iv-lambda-max-driven.md) — METHOD TRAP (S117 W7-3 builds s116's forward CF-S117-BRANCH-IV-L16): branch-iv ρ_B=mean_Z/λ_max−1 is λ_max-DRIVEN not bottom-K-driven; FB bottom-K saturation does NOT freeze it at high L (INV13 conflated → SET ρ_B(16)≡ρ_B(15), WRONG by 0.016460). Built p+q=16 shell INFO: ρ_B(16)=−0.712635, λ_max(16)=6.917603@GT-pure(0,16), mean_Z frozen 8.9e-07, decel+narrow confirmed. Shell-build technique: conj-CPT halving, Casimir-ordered λ_max from GT-pure, stdout block-buffering blind spot (key waiter on npz not log)

## Key Constants & Equations (Quick Reference)

Always cross-check against `canonical_constants.py` before citation; values below are agent operational pins.

| Quantity | Value | Origin |
|---|---|---|
| tau_fold | 0.190 | S42 |
| G_DeWitt | 5.0 (exact) | S42 |
| m_tau | 2.062 M_KK | S42 |
| dS/dtau at fold | +58,673 | S36 |
| S_fold | 250,361 | S36 |
| sin^2(theta_W)\|M_KK | 0.5839 (3 methods, machine eps) | S33a, S75 |
| sin^2 cubic accidental | 0.2348 (1.6% from PDG, no derivation) | S75 |
| R(fold) | 2.018 | S33a, Paper 15 eq 3.70 |
| m_H (BCS-dressed) | 127.51 GeV | S69 |
| N_eff | 3.1744 | S74 W4-R |
| R_protected_fold | 1.1287 | S73B |
| w_0 (Noether) | -0.918 | S73B |
| alpha_s(M_Z) | 0.022 (5.4x tension) | S69 |
| g1/g2 | e^{-2tau} (67/67 Baptista verified) | S33a |
| a_0/a_2 (left-inv) | 6/R (PERMANENT) | S65 |
| a_2^bos / a_2^Dirac | 61/20 = 3.05 exact | S44 |
| f_conv | pi^4/(9216*a_0^2) | S76 W2-A |
| Y on U(2)-invariant | lambda * I_4 (Schur) | S66 |
| Lefschetz dominant winding | n* = 60 = N_pair | S74 W3-N |
| (n_b, n_f) Sym^2(su(3)*) | (20, 16) unique under U(2) | S74 W4-R |
| L_R Dynkin ratio | delta_1/delta_3 = 20/9 (perm obstruction) | S73a |

## Debugging Notes

- Gate-verdict file format: `s{N}_gate_verdicts.txt` lines have dual-SHA closure (audit_sha256 + content_sha256). NEVER edit verdict lines manually.
- "a_k" name collision: spectral zeta (S41/S42) != power sums (S60) != Gilkey heat-kernel coefficients. Disambiguate when reading old work.
- NEVER use `d^2(Tr D_K)/dtau^2` — vanishes by tracelessness. Use sum|lambda| or f(D^2) instead.
- NEVER use A_antisym (frame indices) for K_a_matrix (spinor indices). V MATRIX LESSON, S34a.
- ALWAYS sum over ALL generators, not just a subalgebra (K-1e lesson).
- Eq 3.65 in Paper 15: OCR garbled — DO NOT USE; use eq 3.70 for R(s).
- Wigner-Eckart on abstract rep theory can be TOO STRONG for Dirac — Clifford correlations need verification.
- NumPy 2.x: use `np.trapezoid` (not `np.trapz`).
- Python interpreter: `phonon-exflation-sim/.venv312/Scripts/python.exe`.

## Memory Discipline

- This file is agent-private; project registries belong in `sessions/framework/registry/` (see `.claude/rules/agent-standards.md` §AMRI).
- Detail files for individual gates were collapsed 2026-04-28; per-gate detail is reproducible from `sessions/session-{N}/session-{N}-results-workingpaper.md` + verdict files.
- When citing a verdict, link to the verdict file (`computations/s{N}_gate_verdicts.txt`), not to a memory artifact.
