# Session 47 Way Forward → Session 48 Planning

## Purpose

Exhaustive extraction of all recommendations, collaborative suggestions, open questions, and pre-registered gates from Sessions 46 and 47 that remain unexecuted. Items already completed in S47 are marked DONE. Everything else is a carry-forward candidate for S48.

---

## Part A: S47 Pre-Registered Gates for S48

These gates were explicitly named and pre-registered in S47 documents with full computation specs.

### A-1. GOLDSTONE-MASS-48
- **Source**: `session-47-texture-framework.md` §6.1
- **What**: Compute mass of U(1)_7 Goldstone mode from spectral action second derivative
- **Method**: D_K(phi) = exp(i*phi*K_7) * D_K * exp(-i*phi*K_7). Compute m_G^2 = (1/rho_s) * d^2 S / dphi^2 at phi=0
- **Input**: s44_dos_tau.npz, s34 K_7 matrix, s44_cutoff_f.npz, rho_s(C^2)=7.962 (s47_rhos_tensor.npz)
- **Gate**: PASS if m_G/M_KK in [10^{-60}, 10^{-50}]; INFO if computable but outside; FAIL if d^2S/dphi^2 = 0 identically
- **Expected**: FAIL ([iK_7, D_K] = 0 makes D_K(phi) = D_K for all phi, so d^2S/dphi^2 = 0)
- **Agent**: Landau or Spectral-Geometer
- **Priority**: HIGH — confirms Goldstone is exactly massless in spectral action, forces mass origin elsewhere

### A-2. ANISO-OZ-48
- **Source**: `session-47-texture-framework.md` §6.2
- **What**: Full anisotropic Ornstein-Zernike power spectrum on 3D tessellation (4x4x2 = 32 cells) with direction-dependent Josephson coupling and Goldstone mass as free parameter
- **Input**: J_C2 = 0.933, J_su2 = 0.059, T_acoustic = 0.112. Mass m scanned over [10^{-3}, 10^{3}] in units of J_C2
- **Gate**: PASS if exists m/J with n_s(K_pivot, m) = 0.965 ± 0.01 AND physically reasonable origin; INFO if trivially achievable; FAIL if 3D geometry prevents n_s = 0.965
- **Expected**: INFO (O-Z trivially gives n_s = 0.965 at some m; non-trivial question is 3D anisotropic corrections)
- **Agent**: Landau
- **Priority**: HIGH — the current n_s mechanism lives here

### A-3. CHI-Q-PHASE-48
- **Source**: `session-47-texture-framework.md` §6.3
- **What**: q-theory susceptibility decomposed into phase (Goldstone) and amplitude (Higgs-like) contributions
- **Method**: rho_vac(tau, phi). Compute chi_q = d^2 rho_vac/dtau^2 and chi_phi = d^2 rho_vac/dphi^2 independently
- **Input**: s44_dos_tau.npz, s46_qtheory_selfconsistent.npz, s34 K_7 matrix
- **Gate**: PASS if chi_phi/chi_q > 0.1; INFO if measurable but < 0.1; FAIL if chi_phi = 0
- **Expected**: FAIL (same [iK_7, D_K] = 0 argument)
- **Agent**: Volovik
- **Priority**: MEDIUM — closes the q-theory phase channel

### A-4. ANISO-GAP-48
- **Source**: `session-47-ns-reassessment.md` §6
- **What**: Effective BCS gap as seen by modes in each Lie algebra direction (C^2, su(2), u(1)), using rho_s anisotropy as weighting
- **Input**: s47_rhos_tensor.npz, s46_qtheory_selfconsistent.npz, s44_dos_tau.npz
- **Method**: For each mode k, Delta_eff(k) = Sum_a |<k|J_a|k'>|^2 * Delta_{sector(k')} * f(rho_s^{aa})
- **Gate**: PASS if n_s in [0.80, 1.10]; FAIL if outside; INFO if [0.50, 0.80]
- **Expected**: FAIL (sqrt(24) ~ 4.9x anisotropy insufficient)
- **Agent**: Volovik or Landau
- **Priority**: MEDIUM — formally closes k-dependent gap path

---

## Part B: S47 Open Computations (Crystal Geometry)

From `session-47-crystal-geometry.md` §6 (Tesla-Resonance, O-1 through O-5).

### B-1. O-1: Soft-pairing anti-correlation across tau
- **What**: Compute V(B2,B2)(tau) and K_soft(tau) across [0, 0.50]. Check whether dV/dtau and dK/dtau have opposite signs at every tau
- **If confirmed**: promotes observation to structural result
- **Overlaps**: Nazarewicz 3.2 (curvature-gap correlation function)
- **Priority**: MEDIUM

### B-2. O-2: 1/e^2 radius convergence test
- **What**: Compute condensate 1/e^2 radius at max_pq_sum = 4, 5, 6. Does it converge to pi/4?
- **Why**: Tests the 0.7% near-miss between 1/e^2 radius (0.78 rad) and K_7 eigenvalue q_7 = 1/4
- **Priority**: LOW (likely coincidence given COHERENCE-RESPONSE-47 ARTIFACT verdict)

### B-3. O-3: Condensate density along soft vs hard geodesics
- **What**: Compute condensate profile along geodesic in soft su(2)-C^2 directions starting from identity. Check whether condensate decays slower in soft than hard directions
- **Priority**: MEDIUM (probes spatial structure of order parameter)

### B-4. O-4: Curvature-weighted spectral sum (Sakharov functional)
- **What**: S(tau) = sum_a K_a * rho_a(tau). Check for minimum; if so, selects emergent G_N at fold
- **Cross-ref**: Volovik collab 3.5 (Sakharov induced gravity interpretation)
- **Note**: Volovik coherence response assessed as "INSUFFICIENT as self-coherence probe but correct as G_N computation"
- **Priority**: MEDIUM-HIGH — directly tests whether curvature anatomy improves the 0.36 OOM G_N discrepancy from RUNNING-GN-45

### B-5. O-5: TT 2-tensor Lichnerowicz computation ← NEXT DECISIVE COMPUTATION
- **What**: Implement Delta_L h = -nabla^2 h - 2 R_{acbd} h^{cd} + 2 R_{(a}^c h_{b)c} in Peter-Weyl basis using S47 curvature anatomy data
- **Why**: "The curvature anatomy computed here provides exactly the Riemann tensor components needed"
- **Prediction**: TT modes in hard su(2)-su(2) sector should behave differently from soft su(2)-C^2 sector
- **Priority**: HIGH — explicitly flagged as "the next decisive computation"

### B-6. Dirac eigenvector retention and analysis
- **Source**: crystal-geometry §"What Would Complete the Picture", Nazarewicz 5.5, Landau closing
- **What**: Modify `collect_spectrum` in `tier1_dirac_spectrum.py` to retain eigenvectors
- **Sub-questions**: (a) Where on SU(3) do B2 modes concentrate? (b) Do pi-phase states have distinctive Chladni patterns? (c) Do soft-sector modes have larger spatial extent?
- **Priority**: MEDIUM-HIGH — "would close the loop between spectral landscape and condensate structure"

---

## Part C: S47 Collaborative Suggestions (by agent)

### C-1. Landau Suggestions (from crystal-geometry-landau-collab.md)

| ID | Suggestion | Priority | S47 Status |
|:---|:-----------|:---------|:-----------|
| S-1 | Explicit GL free energy F_GL(tau) using s44_dos_tau.npz + corrected V matrix. Plot S_spectral + F_GL for local extrema | — | NOT DONE |
| S-2 | Leggett mode frequency from inter-sector BdG coupling (B2/B3). If omega_L < 2*Delta_B3 = 0.168, sharp resonance. May reach zero at critical tau → new instability | — | NOT DONE |
| S-3 | Z_3 domain wall energy. Width set by 1/e^2 radius. Order parameter manifold U(1) x Z_3 with pi_0 = Z_3, pi_1 = Z | — | NOT DONE |
| S-4 | Full rho_s tensor via Peotta-Torma formula | — | **DONE** (RHOS-TENSOR-47) |
| S-5 | Anisotropic Kibble-Zurek defect production: n_soft ~ (tau_Q)^{-12nu/(12nu+z)} vs n_hard ~ (tau_Q)^{-3nu/(3nu+z)} | — | NOT DONE |

**Landau Open Questions:**
- Q-1: C^2 isotropization endpoint — does C^2-C^2 curvature reach 1.0 at some tau_iso? Emergent SO(4)?
- Q-2: Pomeranchuk instability in curvature channel — spontaneous distortion beyond Jensen family? (S29b found 2/4 negative Hessian eigenvalues)
- Q-3: Condensate contribution to CC — Delta_B2^4 ~ M_KK^4, GGE destroys condensate, residual = |E_cond|?
- Q-4: Protected chain q_7^2 = K = 1/16 survival when summed over all PW sectors

### C-2. Nazarewicz Suggestions (from crystal-geometry-nazarewicz-collab.md)

| ID | Suggestion | Priority | S47 Status |
|:---|:-----------|:---------|:-----------|
| 3.1 | Self-consistent HFB gap equation in Peter-Weyl basis (sector-resolved Delta) | 1 | NOT DONE |
| 3.2 | Curvature-gap correlation function r(tau) across 26 tau values. Structural if r < -0.9 at all tau | 2 | NOT DONE |
| 3.3 | Collective pair rotation coupling matrix along soft vs hard geodesics | 3 | NOT DONE |
| 3.4 | Bayesian assessment: sample 100 random left-invariant metrics, test K(u(1),C^2) = 1/16 universality | 4 | NOT DONE |
| 3.5 | Nilsson diagram analog: track curvature branch separations as f(tau), identify level crossings | 5 | NOT DONE |

**Nazarewicz Open Questions:**
- 5.1: Is the pairing field self-consistent on SU(3)? (→ 3.1)
- 5.2: Does protected chain survive beyond Jensen? (same as Landau Q-4)
- 5.3: 0D limit physical status — PBCS vs BCS, 36% gap reduction effect on contrast ratio
- 5.4: Curvature anisotropy growth bounded? Does soft branch → K=0 at some tau_critical? (decompactification instability) — compute to tau=1.0
- 5.5: Chladni patterns from Dirac eigenvectors (same as B-6)

### C-3. Volovik Suggestions (from crystal-geometry-volovik-collab.md)

| ID | Suggestion | Priority | S47 Status |
|:---|:-----------|:---------|:-----------|
| 3.1 | Akama-Diakonov emergent metric from condensate profile on T^2. Check for analog horizon | — | NOT DONE |
| 3.2 | Q-theory vacuum energy using Haar-weighted condensate geometry (not just (0,0) solution) | — | NOT DONE (Q-THEORY-BCS-45 tau*=0.209 exists but needs Haar correction) |
| 3.3 | Homotopy classification of order parameter manifold on T^2 — vortex support | — | NOT DONE |
| 3.4a | Lab analog: shell structure in cold atoms on SU(3) optical lattice | — | NOT DONE (theoretical) |
| 3.4b | Lab analog: protected K in twisted trilayer graphene | — | NOT DONE (theoretical) |
| 3.4c | Lab analog: soft-pairing anti-correlation in iron pnictides | — | NOT DONE (theoretical) |
| 3.5 | Sakharov curvature-weighted functional at fold (same as B-4) | — | NOT DONE |

**Volovik Open Questions:**
- 1: Is Haar-weighted shell a laboratory observable? What is the SU(3) analog of 3He NMR frequency shift?
- 2: C^2 isotropization = Lifshitz transition? (same as Landau Q-1)
- 3: What is q-theory vacuum variable? q ~ |Delta|_avg (shell-peak, not identity value). Does d(rho)/dq = 0 select fold?
- 4: Analog Hawking effect from condensate gradient? Compute analog surface gravity
- 5: R_B2 = 1.494 ↔ superfluid fraction? (0.494 excess = normal-fluid fraction analog?)

### C-4. N_s Reassessment Paths (from session-47-ns-reassessment.md)

| Path | Description | Status |
|:-----|:-----------|:-------|
| A | k-dependent Delta(k) ~ k^{-alpha}. Need alpha ~ 0.76 for n_s = 0.965. Rho_s anisotropy provides mechanism but in wrong space | → ANISO-GAP-48 |
| B | Topological defect correlations (outside Bogoliubov paradigm). Power-law from universality class | NOT ATTEMPTED |
| C | Adiabatic spectral flow through q-theory potential. N_3=0 blocks direct route | OPEN |
| C' | **Fabric-level power spectrum** from inter-cell coupling across tessellation — "no session has attempted this" | **DONE** (TEXTURE-CORR-48 in W5) |

### C-5. Q-Theory Goldstone Self-Tuning (from texture-framework §7.4)
- **What**: Specify how rho_s enters q-theory self-tuning for Goldstone sector. Compute predicted mass
- **Preliminary estimate**: m ~ T^2/sqrt(rho_s * M_KK^2) ~ 10^{-39} GeV (within OOM of required 2.4e-39 GeV)
- **Gate potential**: If q-theory self-tuning operates on Goldstone sector, mass determined by d(rho_vac)/d(m^2) = 0
- **Priority**: HIGH — directly addresses mass problem

### C-6. Goldstone Mass Origin Candidates (from texture-framework §3.3)
- **(a)** Spectral action on-site potential: m^2 = (a_2/rho_s) * (d^2 lambda/dphi^2)_avg
- **(b)** Finite correlation length in disordered su(2)/u(1) directions introduces effective mass into C^2 phase field
- Both need computation in S48

---

## Part D: S46 Carry-Forwards (NOT executed in S47)

These were recommended in S46 collab documents and NOT found in S47 gate verdicts or computation scripts.

### D-1. CRITICAL (gates CC mechanism)

| Item | Source | Description | S47 Status |
|:-----|:-------|:-----------|:-----------|
| N-PAIR-FULL-47 | Volovik, Hawking, Dirac, String, quicklook | Physical pair number from 992-mode (or 16-mode singlet) spectrum. PASS if N >= 2 | **NOT DONE** — no s47_npair script found |
| V-TAU-SWEEP-47 | Volovik, String, quicklook | V_{kk'}(tau) sweep for Delta_B3 > 0.13 at any tau | **PARTIALLY** — scale-bridge FAIL addresses related question but not the V matrix sweep itself |

### D-2. HIGH (gates n_s mechanism)

| Item | Source | Description | S47 Status |
|:-----|:-------|:-----------|:-----------|
| NONSINGLET-SELFCONSIST-47 | Volovik, Hawking, QA | Self-consistent LZ with negative feedback. Iterate v_transit, update beta_k, converge | **DONE** (ACOUSTIC-HORIZON-48 FAIL — Planck-scale) |
| Three-phonon vertex omega_B2 ~ 2*omega_B1 | QA | Resonant friction enhancement from 0.6% detuning near-resonance | NOT DONE |
| Block-resolved n_s via 3-band structure | QA, working paper | Full KK projection per band, not per wavenumber | NOT DONE |

### D-3. MEDIUM (topological characterization)

| Item | Source | Description | S47 Status |
|:-----|:-------|:-----------|:-----------|
| WILSON-LOOP-47 | Berry addendum, Volovik, Dirac, Hawking | Non-Abelian Berry phase for 492 degenerate multiplets. Total pi-count in [13,50] | NOT DONE |
| DISSOLUTION-BERRY-47 | Berry addendum, Hawking | 13 pi-phase survival at eps = 0.5*eps_c | NOT DONE |
| CLOSED-LOOP-47 | Berry addendum, Dirac | Round-trip Berry phase tau: 0→0.19→0. Gamma=0 consistency with S25 | NOT DONE |
| Sector-resolved R(p,q) BCS pair ratio | Dirac | Check |R(p,q) - R(q,p)|/R(p,q) < 0.1 for all conjugate pairs | NOT DONE |
| (3,0)/(0,3) pi-phase gauge-independence test | Dirac | Closed-loop distinguishes gauge-dependent from physical asymmetry | NOT DONE |
| (2,1) pi-phase count = 5 derivation | Dirac, Berry addendum | Topology of (2,1) eigenvector bundle in BO(1)^240 | NOT DONE |

### D-4. MEDIUM-LOW (DM/DE and mass ratios)

| Item | Source | Description | S47 Status |
|:-----|:-------|:-----------|:-----------|
| GIBBS-DUHEM-GGE-47 | Volovik | Generalized Gibbs-Duhem with multiple T_k. Resolve Zubarev/Keldysh 20% discrepancy | NOT DONE |
| DESI-UPDATED-47 | Volovik | Update w_0/w_a with corrected alpha range [0.7, 1.2] | NOT DONE |
| Keldysh sigma with pair-pair interactions | Hawking, working paper | May shift alpha closer to 0.388 observed | NOT DONE |

### D-5. Paasch Computations (all from paasch-collab, NONE executed in S47)

| Item | Description | Status |
|:-----|:-----------|:-------|
| PHI-GOLDEN-22-47 | Tau sweep of m_{(2,2)}/m_{(0,0)} ratio toward golden ratio 1.618 | NOT DONE |
| FN-CENTROID-47 | Pair-transfer centroids recomputed with exact V_phys (alpha* = 0.775) | NOT DONE |
| LOG-SIGNED-40 | Signed boson-fermion log sum on 2912 eigenvalues (UNCOMPUTED since S40) | NOT DONE |
| TRIAL-FACTOR | Look-elsewhere correction for phi_paasch significance | NOT DONE (explicitly flagged UNCOMPUTED) |
| n3 = dim(3,0) = 10 | Algebraic derivation of Paasch's n3 from SU(3) representation theory | NOT DONE (priority list since S40) |
| Six-sequence test | Place 2912 eigenvalues on Paasch logarithmic spiral. Zero-cost computation | NOT DONE |
| Phi under non-singlet BCS | E_qp(3,0)/E_qp(0,0) with self-consistent gaps across tau | NOT DONE |

### D-6. String Theory Suggestions (all from string-collab, NONE executed in S47)

| Item | Description | Status |
|:-----|:-----------|:-------|
| Swampland c(tau) profile | de Sitter conjecture check on q-theory potential. c = |eps'|/eps vs O(1) threshold | NOT DONE |
| Poisson-Lie T-duality | Jensen deformation T-dual on SU(3)/SU(2,1). Monotonicity may break in dual frame | NOT DONE (flagged "more urgent" after S46 SU(2,1) result) |
| SU(2,1) discrete series / compact quotient | Rescue compact resolvent axiom at d=8 | NOT DONE |
| WZW vs spectral action Strutinsky benchmark | Reliability check near fold. 95-99% standard from nuclear physics | NOT DONE |
| 13 pi phases ↔ WZW winding mod 2 | pi_5(SU(3)) = Z connection. 13 mod 2 = 1 matches nontrivial Z_2 | NOT DONE |

### D-7. Quantum Acoustics Suggestions (from qa-collab, NONE executed in S47)

| Item | Description | Status |
|:-----|:-----------|:-------|
| Berry phase edge states at tessellation boundaries | Topological edge modes at 32-cell domain walls for inter-domain energy transfer | NOT DONE |
| Dissolution-driven GOE transition | Spectral form factor ramp onset at what epsilon? Probes crystal breakdown | NOT DONE |
| B2 van Hove protection at higher-order scattering | Does it extend beyond single-particle Bogoliubov? | NOT DONE |
| B3 repulsive channel in post-transit GGE | V_B3B3 = -0.072. Population inversion? | NOT DONE |
| 13 pi-phases ↔ van Hove singularity energies | E = [1.075, 1.819]. Double enhancement if coincident | NOT DONE |
| Jahn-Teller connection to 2D saddle | Formal theorem question | NOT DONE |

### D-8. Tachyonic Transit Open Items (from s46_addendum_tachyonic_transit.md)

| Item | Description | Status |
|:-----|:-----------|:-------|
| Transit velocity through 279-mode tachyonic landscape | Driving/resistance ratio as slow-roll analog | NOT DONE |
| GGE distribution across tachyonic modes | 279-channel occupation pattern | NOT DONE |
| Self-consistent Delta(tau) coupled to q-theory crossing | Does tau* = 0.209 lock onto fold? | PARTIALLY (q-theory data from S46 exists, self-consistency not closed) |
| CCS 2013 extra 169 gauge-type channels | Role in transit dynamics | NOT DONE |

### D-9. S46 Corrections Requiring Propagation

| Correction | Detail | S47 Status |
|:-----------|:-------|:-----------|
| alpha* = 3.91 → 0.775 | All W1-2, W2-2, W3-1 used retracted value. Centroid ratios need recomputation | NOT PROPAGATED (FN-CENTROID-47 unexecuted) |
| alpha_eff = 0.410 → [0.70, 1.15] | DM/DE ratio, w_0/w_a downstream uses need update | NOT PROPAGATED (DESI-UPDATED-47 unexecuted) |
| CHAOS-1 <r> = 0.321 → 0.439 | Sub-Poisson reclassification (88% zero-spacings from degeneracies) | ACKNOWLEDGED in S47 SPECTRAL-LANDSCAPE-47 but no formal recomputation |

---

## Part E: S47 Scale-Bridge and Acoustic-Horizon Results (constrain S48 directions)

These S47 W5 results CLOSED specific paths and constrain what S48 can pursue:

| Gate | Verdict | Implication for S48 |
|:-----|:--------|:-------------------|
| TEXTURE-CORR-48 | **PASS** | K^{-2} Goldstone spectrum confirmed. n_s from gradient coupling = 1.0 (Harrison-Zel'dovich, 8.3 sigma from Planck). **Mass is required** → gates A-1, A-2 |
| SCALE-BRIDGE-48 | **FAIL** | Josephson coupling → BAO: acoustic velocity / physical distance FAIL by 56 decades. No direct causal bridge from internal BCS to ~150 Mpc structure |
| ACOUSTIC-HORIZON-48 | **FAIL** | Transit acoustic horizon is Planck-scale (~10^{-35} m). Even comoving stretch gives ~10^{-6} m. Route CLOSED by 60 OOM (physical) or 31 OOM (comoving) |

**Implication**: The n_s mechanism MUST go through fabric-level texture with a mass gap (A-1/A-2), not through causal propagation during transit.

---

## Part F: Algebra Error to Propagate

From `session-47-scale-bridge.md`: The xi_texture = 151 Mpc value in `sessions/session-plan/session-47-wave5-texture.md` line 225 is **WRONG**. Correct value is **xi = 2.67 Mpc**. The near-coincidence with BAO peak (147 Mpc) was an artifact of the error. All S48 work must use xi = 2.67 Mpc.

---

## Part G: Prioritized S48 Computation List

### Tier 1 — Pre-Registered Gates (must execute)

1. **GOLDSTONE-MASS-48** (A-1) — confirms Goldstone exactly massless in spectral action
2. **ANISO-OZ-48** (A-2) — 3D anisotropic power spectrum with mass parameter scan
3. **CHI-Q-PHASE-48** (A-3) — q-theory phase susceptibility
4. **ANISO-GAP-48** (A-4) — k-dependent gap from rho_s anisotropy
5. **N-PAIR-FULL** (D-1) — physical pair number from full spectrum. CRITICAL for CC crossing

### Tier 2 — High-Priority Carry-Forwards

6. **TT 2-tensor Lichnerowicz** (B-5) — "the next decisive computation"
7. **Q-theory Goldstone self-tuning** (C-5) — mass ~ 10^{-39} GeV estimate needs rigorous computation
8. **Self-consistent HFB on SU(3)** (Naz 3.1) — sector-resolved gap equation, PRIORITY 1 from Nazarewicz
9. **Curvature-gap correlation function** (B-1 / Naz 3.2) — V(B2,B2)(tau) vs K_soft(tau), structural if r < -0.9
10. **Sakharov curvature-weighted sum** (B-4 / Volovik 3.5) — S(tau) for G_N improvement

### Tier 3 — Topological and Berry Phase (from S46, all unexecuted)

11. **WILSON-LOOP-47** (D-3) — non-Abelian Berry phase for 492 degenerate states
12. **DISSOLUTION-BERRY-47** (D-3) — topological skeleton survival test
13. **CLOSED-LOOP-47** (D-3) — round-trip Berry phase consistency with S25
14. **Sector-resolved R(p,q)** (D-3) — CPT pair symmetry test

### Tier 4 — DM/DE Refinement

15. **GIBBS-DUHEM-GGE** (D-4) — multi-temperature Gibbs-Duhem for GGE
16. **DESI-UPDATED** (D-4) — w_0/w_a at corrected alpha [0.7, 1.2]
17. **Keldysh sigma with pair-pair interactions** (D-4)

### Tier 5 — Paasch, String, QA (unexecuted S46 backlog)

18. **LOG-SIGNED-40** — uncomputed since S40, signed boson-fermion log sum
19. **PHI-GOLDEN-22** — tau sweep of (2,2)/(0,0) ratio toward golden ratio
20. **Six-sequence test** — zero-cost computation on existing 2912 eigenvalues
21. **n3 = dim(3,0)** — algebraic derivation, in priority list since S40
22. **Swampland c(tau)** — de Sitter conjecture on q-theory potential
23. **Berry edge states at tessellation** — topological edge modes at domain walls
24. **Three-phonon vertex** — resonant friction from omega_B2 ~ 2*omega_B1

### Tier 6 — Deeper Investigations (longer-term)

25. **Dirac eigenvector retention** (B-6) — modify tier1 code, Chladni patterns
26. **Curvature anisotropy to tau=1.0** (Naz 5.4) — decompactification instability?
27. **C^2 isotropization / Lifshitz transition** (Landau Q-1 / Volovik Q-2)
28. **Leggett mode** (Landau S-2) — inter-sector collective mode
29. **Z_3 domain wall energy** (Landau S-3)
30. **Anisotropic KZ defect production** (Landau S-5)
31. **Akama-Diakonov emergent metric** (Volovik 3.1) — analog horizon
32. **Poisson-Lie T-duality** (String) — monotonicity in dual frame
33. **Topological defect correlations** (NS Path B) — outside Bogoliubov paradigm
34. **279-mode tachyonic transit velocity** (Tachyon addendum)
35. **Self-consistent Delta(tau) + q-theory** — locks tau* onto fold?

---

## Part H: Cross-Cutting Themes for S48

### Theme 1: The Mass Problem
TEXTURE-CORR-48 PASSED with K^{-2} spectrum but n_s = 1.0 (massless Goldstone). The ENTIRE n_s mechanism now depends on finding a Goldstone mass. Three candidates: (a) spectral action on-site (A-1, expected FAIL), (b) disordered-direction correlation length (C-6b), (c) q-theory self-tuning (C-5). S48's central question: **where does the mass come from?**

### Theme 2: Physical Pair Number
N-PAIR-FULL was CRITICAL in S46 and never executed. With N=1 from 8-mode ED, the q-theory CC crossing at tau*=0.170 requires N >= 2. The 992-mode spectrum exists. This is computable and decisive.

### Theme 3: Self-Consistency
Three levels of self-consistency remain open: (a) sector-resolved HFB (Naz 3.1), (b) condensate back-reaction on geometry (substrate reframe §4.2), (c) q-theory potential coupled to BCS (tachyon addendum). Each progressively harder.

### Theme 4: Topological Layer 2
The non-Abelian Berry phase for 492 degenerate states (WILSON-LOOP-47) has been deferred twice. The total pi-count may change from 13 to something closer to 16 (SM particle count). This is a zero-cost computation with existing code infrastructure.

### Theme 5: Fabric vs Internal
S47 definitively closed causal propagation paths (60 OOM gap). All surviving mechanisms are fabric-level: tessellation phase correlations with mass gap. The framework's observational signatures come from the 32-cell tessellation, not from the internal SU(3) BCS.
