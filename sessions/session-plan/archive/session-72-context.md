# Session 72 Context Package: BCS and Friends

**Assembled**: 2026-04-10
**Topic**: BCS and Friends
**Planner**: landau-condensed-matter-theorist

---

## Framework Status (from MEMORY.md)

### PROVEN (16 results, machine epsilon)
KO-dim=6 | SM quantum numbers | [J,D_K]=0 CPT | g1/g2=e^{-2tau} | 67/67 Baptista | Volume-preserving TT | Riemann 147/147 | TT stability | phi_paasch=1.531580 | AZ class BDI | D_K block-diagonal | Trap 3 | Perturbative Exhaustion | DNP instability | Pomeranchuk | Clock constraint

### Current State
- 25 CLOSED mechanisms (all perturbative + instanton averaging)
- PARADIGM: Transit physics, not equilibrium. Instanton gas, not potential well
- THE ORDERED VEIL: integrable, not chaotic. GGE relic, never thermalizes
- Mechanism chain UNCONDITIONAL (S35): I-1, RPA, Turing, WALL, BCS all PASS
- Open: FRIEDMANN-BCS-38 (coupled dynamics, shortfall 38,600x)

### Session History
- S66: CC reframe, spectral functional crisis, EVOI table established
- S68: BCS-dressed modes (delta_As=11.2%, PASS), ISW correction
- S69: phi_eff=0.558*pi (cos=-0.181), KK-Higgs PASS (127.5 GeV)
- S70: Leggett vacuum (0.267 OOM gap), Meissner PASS, 46/46 computations
- S71: 20 computations (6 PASS, 11 INFO, 3 FAIL). Spectral zeta, A_s overcorrection, scheme hierarchy

---

## S71 Gate Verdicts (20 gates)

### CRITICAL (4)
- SPECTRAL-ZETA-THRESHOLD-71: **INFO** — S_inf=2.353 (in range), truncation 10.2% (INFO band)
- HIGHER-ORDER-CCM-71: **PASS (formal)** — delta=26.9% but anti-correlation PERSISTS. Scheme-dependent (0% zeta, 27% cutoff).
- INTER-SITE-ENTANGLE-71: **INFO** — S_vN=1.999 bits vs 0.876 predicted, ratio 2.28. 4-mode transmon.
- DECOHERENCE-BAND-71: **PASS** — SU(1,1) exact (8e-15). BCS alone overcorrects 7.7x.

### HIGH (4)
- NON-TRIVIAL-FIBRATION-CSQUARED-71: **INFO** — c_s^2 safe (4.26e-4), alpha_s 4.2% of needed 781%
- WEYL-TWO-LOOP-71: **FAIL (marginal)** — delta_2=1.003e-3. All-orders bound 1.16e-3.
- BH-THIRD-LAW-71: **FAIL** — ratio=0.01. Category error (fiber vs fabric).
- THREE-CELL-GSL-71: **PASS** — S_gen monotone all 4 stages. Frustration reduces S_GGE by 48%.

### MEDIUM (7)
- R-SPATIAL-SCAN-71: **INFO** — r_spatial_critical DNE. BCS dominates 7.7x.
- CHIRP-UNIVERSALITY-71: **PASS** — geometric invariant to machine precision. PERMANENT.
- ENTRY-HORIZON-SPECTRUM-71: **INFO** — N_crossings=0. Entry kinematic.
- CAUSAL-MOMENT-MAP-71: **INFO** — a_0>a_2>a_4 hierarchy FROZEN at all tau.
- DESI-DR3-SCENARIO-B-71: **INFO** — FW 2.88σ. w_a sole discriminant.
- 21CM-ISW-PREREGISTRATION-71: **INFO** — +4.0% enhancement. SNR=4.16 ideal.
- DISCRETE-RW-UNIVERSALITY-71: **INFO** — partial universality in S_4 family.

### LOW (5)
- ALPHA-S-BAYESIAN-SHADOW-71: **INFO** — Pantheon+ 17.7%, spectral zeta 10.2% tighter.
- CORRELATED-SENSITIVITY-71: **INFO** — omega_L robust (sensitivity -0.44).
- CC-FROM-GGE-RESIDUAL-71: **FAIL** — 110 OOM. Direct GGE-CC CLOSED. Q-theory sole.
- BCS-BACKREACTION-a4-71: **PASS** — delta=2.02e-8. Gauge safe.
- GGE-HAWKING-ANALOG-71: **INFO** — C_V suppression 430x. BEC accessible.

---

## S71 Workshop Emergent Findings (cross-workshop convergence)

### K-Theoretic vs Spectral Partition (WS1 + WS3)
ALL predictions partition into:
- **K-theoretic (permanent)**: KO-dim, quantum numbers, chirality, BDI, c_s²=0, w_a=0
- **Spectral (scheme-dependent)**: w_0, alpha_s, m_H, CC
- **Spectral-robust (ratios)**: g_1/g_2, n_s, omega_L, sin²(θ_W), m_H/m_W

### w_0 ≤ -0.908 Theorem (WS1)
Cauchy-Schwarz on spectral moment ratios proves w_0 ≤ -0.908 for all smooth functionals. Gaussian saturates at -0.918. One-sided attractor toward ΛCDM.

### w_a = 0.066 RETIRED (WS1)
Canonical prediction: (w_0 = -0.918 ± 0.05, w_a = 0).

### Decoherence = Exit Horizon Causal Disconnection (WS2)
Physical mechanism: partial trace over supersonic interior modes at exit sonic horizon. Dual-timescale: BCS fast at exit, spatial/Leggett slow post-exit.

### Self-Consistent Gap Curvature κ_Δ is THE Bottleneck (WS3)
Landau-Khalatnikov formula could close A_s budget with zero free parameters — but requires κ_Δ (gap curvature at fold), not κ_n (eigenvalue curvature from W2-B).

### Vol=1 Master Stability Theorem (WS3)
Baptista volume-preserving property → a_0 constant, moment hierarchy frozen, Jensen is valley minimum in 35D moduli space.

---

## EVOI Framework (S66, needs updating to S72)

### Level 1 CRITICAL (EVOI > 10%)
- P1: TRANSIT-PS-67 — Full Bogoliubov power spectrum. EVOI=22.5%
- P2: LEGGETT-GRAV-DECAY-67 — Gravitational decay vertex. EVOI=17.4%
- P3: FUNCTIONAL-SELECT-67 — Physical spectral functional. EVOI=13.2%
- P4: BBN-VOLOVIK-67 — Tracking EOS at T_BBN. EVOI=14.0%

### Mechanism Chain: 9/11 links at 9/9 PASS
- Open: Spectral functional selection, Leggett DM stability (grav decay uncomputed)

---

## Landau Agent Memory (key entries)

### S71 Workshop R1-R2 Results
- Decoherence = transit phase diffusion (Landau-Khalatnikov, computable from van Hove kappa)
- S_vN = log2(dim(coset)) = 2 bits (zero-parameter prediction)
- Scheme-independent set = {g1/g2, n_s, omega_L, sin²(theta_W)}
- Skin fraction = N_BCS/N_total with d_eff=0
- sin²(θ_W) and van Hove kappa identified as top priorities

### S71 Key Results
- INTER-SITE-ENTANGLE: INFO, S_vN=1.999 bits, 4-state Schmidt, Josephson-dominated
- phi_eff = 0.558*pi, cos(phi_eff) = -0.181
- BCS-BACKREACTION-a4: PASS, delta=2.02e-8
- BCS-DRESSED-MODE-68: PASS, net A_s shift +11.2%

---

## Carry-Forward Computations (from structured wrap-ups)

**Sources**: 3 workshop wrap-ups (Mack×VdD, PF×Hawking, Landau×Baptista)

### CRITICAL / HIGH PRIORITY

| # | Computation | Source (count) | Input | Gate | Effort |
|:--|:-----------|:---------------|:------|:-----|:-------|
| 1 | Self-consistent gap curvature κ_Δ | WS3-CF1 (1) | D_K trajectories, BCS pairing matrix | A_S-DECOHERENCE-72 | Medium |
| 2 | DUAL-DECOHERENCE-72 | WS2-CF1 (1) | W1-D compound, W2-C horizons, W2-D gradient | delta_OOM in [0.15,0.40] | Medium |
| 3 | sin²(θ_W) at M_KK + RG to M_Z | WS3-CF4 (2: WS3+WS1 both mention) | D_K spectrum, PW tower | WEINBERG-ANGLE-72 | Medium |
| 4 | W1-B gate re-evaluation (Gilkey ratio) | WS3-CF3 (1) | Existing W1-B data | HIGHER-ORDER-CCM-71 re-eval | Low |
| 5 | Spectral zeta ratio convergence scan | WS3-CF2 (1) | S64 L_max=10 eigenvalues | ZETA-RATIO-CONVERGENCE-72 | Low |
| 6 | CAUCHY-SCHWARZ-W0-BOUND verification | WS1-CF6 (1) | S66 f-moment database | w_0 ≤ -0.908 for all families | Low |
| 7 | SPECTRAL-FUNCTIONAL-FIT-72 | WS1-CF2 (1) | S66 cutoffs, S64 n_s, S71 A_s | Consistent f(x) existence | High |
| 8 | INSTANTON-KAPPA-72 | WS1-CF1 (1) | ADHM moduli, Jensen fiber | kappa vs 0.586 bound | Medium |

### MEDIUM PRIORITY

| # | Computation | Source | Input | Gate | Effort |
|:--|:-----------|:-------|:------|:-----|:-------|
| 9 | ASYMPTOTIC-TRUNCATION-72 (a_8) | WS1-CF3 | D_K eigenvalues L≥8 | SDW convergence | Medium |
| 10 | BCS-DRESSED-SA (eps_H^BCS) | WS1-CF4 | K_BdG, D_K spectrum | n_s correction | High |
| 11 | BLUESHIFT-TILT-72 | WS2-CF5 | T_entry=72.8, Bogoliubov | |delta_ns|>0.001 | Medium |
| 12 | tau_today equilibrium | WS3-CF5 | S(tau), E_BCS(tau) | TAU-EQUILIBRIUM-72 | Medium |
| 13 | Three-way tau_fold consistency | WS3-CF6 | Existing results | TAU-OVERCLOSURE-72 | Low |
| 14 | MODULAR-CHIRP-72 | WS2-CF3 | S64 GGE-KMS, W2-B chirp | agreement <10⁻⁸ | Medium |

### LOW PRIORITY / HIGH EFFORT

| # | Computation | Source | Input | Gate | Effort |
|:--|:-----------|:-------|:------|:-----|:-------|
| 15 | DECOHERENCE-BISPECTRUM | WS1-CF5 | Bogoliubov, decoherence | f_NL consistency | Medium |
| 16 | C_V-SCALING-72 | WS2-CF4 | GGE thermodynamics | alpha>0 | Low |
| 17 | FRUSTRATION-SCHMIDT-72 | WS2-CF6 | W1-C junction, W1-H frustration | K(frustration) | Low |
| 18 | ISLAND-GRAPH-72 | WS2-CF2 | W1-C, W1-H, CG(24) | Area law, Page curve | High |
| 19 | CG24-GGE-ENTROPY | WS2-CF7 | W1-H, CG(24) chromatic | S_cell on full fabric | High |
| 20 | a_2-a_4-CONSTANCY-G2 | WS1-CF7 | G_2 Dirac spectrum (new) | SU(3)-specificity | High |

---

## Existing Data Files (inputs available)

- D_K eigenvalue database: `computations/s64_dk_eigenvalues_lmax10.npz` (L_max=10, 155,984 eigenvalues)
- BCS pairing matrix: `computations/s58_bcs_pairing.npz`
- S66 cutoff families: `computations/s66_*.npz`
- S71 compound squeeze: `computations/s71_decoherence_band.npz`
- S71 chirp data: `computations/s71_chirp_universality.npz`
- S71 entry horizon: `computations/s71_entry_horizon_spectrum.npz`
- S71 spectral zeta: `computations/s71_spectral_zeta_threshold.npz`
- S71 inter-site entangle: `computations/s71_inter_site_entangle.npz`
- S70 Leggett vacuum: `computations/s70_leggett_vacuum.npz`
- S69 phi_eff: `computations/s69_phi_eff.npz`
- Canonical constants: `computations/canonical_constants.py`

## Computation Environment

- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- Output: `computations/`
- Script prefix: `s72_`
- GPU: AMD RX 9070 XT (17.1 GB VRAM, ROCm)
- CPU: AMD Ryzen 32-core, 128GB RAM
