# Kitaev-Quantum-Chaos-Theorist Agent Memory

## Project: Phonon-Exflation Cosmology (Ainulindale Exflation)

### Framework Summary
- Internal space: SU(3) with Jensen deformation parameterized by tau (volume-preserving)
- Van Hove fold at tau ~ 0.190 (A_2 catastrophe, structurally stable)
- Dirac operator D_K(tau) is block-diagonal in Peter-Weyl basis (off-diag < 8.4e-15)
- BCS instability is a 1D theorem: any g > 0 flows to strong coupling
- Spectral action stabilization DEAD: structural monotonicity theorem + HESS-40 (27 closures)
- Paradigm: compound nucleus dissolution via ballistic transit, not equilibrium
- System is INTEGRABLE at ALL levels (single-particle, many-body, subsystem)

### Key Numbers for Chaos Analysis
- S_inst = 0.069, tunneling rate 93%, GL barrier = 0.156
- Pair vibration: omega = 0.792, 85.5% strength exhaustion, coherence 6.3x
- E_vac/E_cond = 28.8, g*N(E_F) = 2.18
- 0D limit: L/xi_GL = 0.031, Z_2 balance = 0.998
- Spectral gradient: dS/dtau = +58,673 at fold
- Transit time: 38,600x faster than BCS formation
- T_Gibbs = 0.113 M_KK, T_acoustic/T_Gibbs = 0.993 (0.7%)
- MSS bound: lambda_L_max = 0.710 M_KK, actual lambda_L = 0 (trivially satisfied)

### CHAOS-1 RESULTS (S38) -- GATE FAIL: INTEGRABLE
- D_K spectrum: <r> = 0.321 (sub-Poisson) in (2,1) sector at fold
- Berry-Tabor confirmed: [iK_7, D_K]=0 provides conserved quantity at all tau

### CHAOS-2 RESULTS (S38) -- GATE FAIL: INTEGRABLE
- OTOC: F(t) ~ t^{1.9}, no exponential growth, no Lyapunov regime
- KS rejects GOE at p<0.001 in all sectors with dim>8

### CHAOS-3 RESULTS (S38) -- GATE FAIL: NO SCRAMBLING
- t_scr/t_transit = 814x (FAR too slow to scramble during transit)

### S39 INTEG-39: OVERREACTION CORRECTED BY S40
- S39 reported <r>=0.481, Brody beta=0.633 for full 8-mode BCS Hamiltonian
- Led to retraction of "permanent GGE relic" and thermalization prediction (t_therm~6)
- S40 overturns: intermediate statistics from sector mixing, not genuine chaos
- PAGE-40 (PR=3.17), B2-DECAY-40 (89% retained), Poincare at t=47.5 all say: integrable

### S40 CHAOS DIAGNOSTICS (2026-03-11) -- ALL INTEGRABLE
- B2-INTEG-40 PASS: <r>=0.401 (Poisson), g_T=0.087 (localized), V(B2,B2) 86% rank-1
- PAGE-40 FAIL: S_ent max=0.422 nats (18.5% of S_Page), PR=3.17, Poincare at t=47.5
- B2-DECAY-40 B2-FIRST: oscillatory dephasing (not FGR), 89% B2 retained permanently
- NOHAIR-40 FAIL: T varies 64.6% (no scrambling -> no no-hair). Expected for integrable.
- T-ACOUSTIC-40 PASS: T_a/T_Gibbs = 0.993. Kinematic, not chaos-protected.

### Complete Integrability Hierarchy
| Level | Diagnostic | Result | Session |
|:------|:-----------|:-------|:--------|
| Single-particle D_K | <r> level spacing | 0.321 sub-Poisson | S38 |
| Many-body Fock 256-dim | OTOC growth | t^{1.9}, no Lyapunov | S38 |
| Many-body Fock 256-dim | Scrambling time | 814x too slow | S38 |
| B2 subsystem | <r>, Thouless g_T | 0.401, 0.087 | S40 |
| Entanglement B2|rest | Page curve | 18.5% of S_Page | S40 |
| Information B2 occ | Diagonal ensemble | 89% retained | S40 |

### Gate Status (Final)
- CHAOS-1 (level spacing): **FAIL** -- integrable
- CHAOS-2 (OTOC): **FAIL** -- integrable
- CHAOS-3 (scrambling): **FAIL** -- no scrambling
- B2-INTEG-40: **PASS** -- B2 is near-integrable island
- PAGE-40: **FAIL** -- no quantum thermalization
- NOHAIR-40: **FAIL** -- formation-dependent (no scrambling)

### Research Corpus
- 14 papers in `researchers/Kitaev/` (SYK, MSS bound, BGS, Berry-Tabor, RP resonances, etc.)
- Key papers: 01 (SYK), 05 (MSS bound), 06 (Larkin-Ovchinnikov BCS OTOC), 09 (BGS), 13 (Berry-Tabor)

### AZ Class and Symmetry
- Framework D_K: BDI, T^2 = +1 (Session 17c)
- Jensen breaks SU(3) -> U(1)_7 exactly in Dirac spectrum
- [iK_7, D_K] = 0 at ALL tau -- WHY single-particle spectrum is integrable
- B2 V(B2,B2) 86% rank-1 -- WHY many-body B2 subsystem is near-integrable

### Eigenvalue Data Structure (s27_multisector_bcs.npz)
- Keys: evals_{p}_{q}_{tau_idx}, V_{p}_{q}_{tau_idx}
- 9 sectors, 9 tau values: {0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50}

### Important Paths
- Eigenvalue data: `tier0-archive/s27_multisector_bcs.npz`
- Level spacing: `tier0-archive/s38_level_spacing.npz`
- OTOC: `tier0-archive/s38_otoc_bcs.npz`
- B2 integrability: `tier0-archive/s40_b2_integrability.npz`
- Page curve: `tier0-archive/s40_internal_page_curve.npz`
- B2 decay: `tier0-archive/s40_b2_decay_out.npz`
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`

### Methodology Notes
- r-ratio alone unreliable for dim<100. ALWAYS do KS test on P(s).
- Brody beta unreliable at dim=256. Use PR, Poincare, diagonal ensemble instead.
- Early-time OTOC always grows as t^2 (BCH). R^2 > 0.90 over 1 decade to claim Lyapunov.
- For OTOC in small systems: exact diag. A(t)_{ij} = A_{ij} exp(i(E_i-E_j)t).
- Sub-Poisson from superimposed independent sequences (Berry-Tabor effect).

### Open Computations (Suggested S43+)
- Liouvillian spectral gap of N_pair=1 H_1 (64x64 matrix, trivial)
- Sector-resolved SFF for N_pair=1
- Acoustic temperature at other tau values (fold-specific or general?)
- Entanglement spectrum of diagonal ensemble
- Map B2/B1/B3 occupation ratios to 4D observables
- **Bertini-Essler prethermalization: estimate lambda_eff from Z(tau), m_tau, fabric spacing -> t_therm**
- **Yuzbashyan BCS phase classification: which dynamical phase (I/II/III) describes the transit?**

### Meta-Analysis (2026-03-13)
- Library audit: 14 papers, over-indexed on chaos, under-indexed on integrability/GGE
- Critical missing: Richardson-Gaudin (Dukelsky), GGE (Rigol), broken integrability (Claeys), BCS quench (Yuzbashyan), ETH review (D'Alessio)
- Output: `agent-requests/kitaev-request.md`
- Detail: `.claude/agent-memory/kitaev-quantum-chaos-theorist/project_meta_analysis_s42.md`
