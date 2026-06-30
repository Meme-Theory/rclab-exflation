---
ARCHIVED: 2026-05-10
Last meaningful session: S66
Superseded by: sessions/permanent-results-registry.md + sessions/framework/Atlas/atlas-07-permanent-results.md
Reason: S66-era baseline findings snapshot; superseded by permanent-results-registry.md (~17000 lines) + atlas-07 §XVI registry slot inventory (S88 atlas-uplift)
---

# Baseline Framework Findings: Comprehensive Cross-Session Inventory

**Scope**: Sessions 1–66 (December 2024 — April 2026)
**Generated**: 2026-04-04
**Sources**: Permanent results registry, Atlas D01–D10, session working papers S52–S66, constraint mega-matrix, EVOI framework, observational avenues, CC budget, workshop syntheses
**Purpose**: Single authoritative document reflecting the full state of knowledge across 66 sessions, ~1,200 computation scripts, 170+ computations (S63–S66), and the S66 CC reframe

---

## Section 1: Proven Mathematics (Publishable Standalone)

These survive regardless of the framework's physical fate. Organized by discovery era.

### 1A. Permanent Results Registry (S7–S28): 12 Results

| # | Result | Session | Precision | Journal Target |
|:--|:-------|:--------|:----------|:---------------|
| 1 | D_K Block-Diagonality Universality — exact in Peter-Weyl for ANY left-invariant metric on ANY compact semisimple Lie group. Three proofs. | S22b | 8.4e-15 | JGP/CMP |
| 2 | Spectral Action Monotonicity Theorem — a_{2k} monotone for k=0,1,2,3. Periodic orbit corrections bounded at 10^{-39}. | S24a+S28c | 10^{-39} | JGP/CMP |
| 3 | Three Algebraic Traps — F/B=4/11, b_1/b_2=4/9, e/(ac)=1/16. All from tensor product structure. | S20b–S22c | Exact | CMP |
| 4 | LZ Retraction / Codimension Classification — BCS on compact manifold is codim-1, not codim-2. LZ inapplicable. | S28 | Exact | JMP |
| 5 | Van Hove Zero-Critical-Coupling on Compact Manifolds — 1D band structures give BCS with no threshold. 43–51x enhancement. | S28c | Exact | CMP/PRL |
| 6 | Cl(8) Three-Way Bridge — Berry γ/π~1, NCG 6/7 axioms, order-one violation 2^{1+k/2} all trace to Spin(8) on C^16. | S28 | — | JMP |
| 7 | Berry Curvature Vanishing on Compact Lie Groups — K_a anti-Hermitian ⟹ Ω=0 identically, all eigenstates, all sectors, all τ. | S25 | 1.12e-16 | JGP/CMP |
| 8 | Spectral Bianchi Identity — gauge invariance constrains sector-weighted spectral derivatives. Analog of ∇_μ G^{μν}=0. | S25 | Theoretical | CMP |
| 9 | 8D Petrov Classification of Jensen-Deformed SU(3) — Type D at τ=0, algebraically general at τ>0. Stable multiplicity {3,4,1,2,4,3,3,8}. | S25 | Machine ε | GRG |
| 10 | Spectral Flow = 0 Theorem — R_K(τ)≥12>0 for all τ. Lichnerowicz bound λ²≥3. No zero crossings. Five confirmations. | S25 | Exact | JGP |
| 11 | Grading Theorem — Tr(γ_9·f(D_K²/Λ²))=0 identically for all f, all τ. 8 independent confirmations. | S25 | Exact | JMP/CMP |
| 12 | Perturbative Exhaustion Theorem — If H1–H5 hold (all verified), F_pert is not true free energy. First-order transition. | S22c | H1–H5 verified | — |

### 1B. Atlas D07 Additions (S29–S62): 28 Additional Publishable Results

| # | Result | Session | Status |
|:--|:-------|:--------|:-------|
| 13 | Structural Monotonicity Theorem — ⟨λ²⟩(τ) increases monotonically. 9,600 individual checks (10 cutoffs × 6 Λ × 16 τ × 10 sectors). | S37 | Machine ε |
| 14 | Lorentzian CMPP Type D — corrects Riemannian artifact. Schwarzschild/Kerr class, permanent across all τ. | S50 | Exact |
| 15 | α_s = n_s² − 1 Structural Theorem — for ANY K² propagator on compact Josephson lattice with broken U(1). Five proofs. | S50 | Exact |
| 16 | Anderson-Higgs Impossibility for U(1)_7 — [D_K, K_7]=0 at all orders. Three proofs: commutant, categorical, numerical. | S51 | Exact |
| 17 | CF-9 Triple Identity — Berry curvature = NCG inner fluctuation = KK A-tensor. |A_coset|²=3/2+(3/2)e^{-4τ}. | S62 | 2e-14 |
| 18 | Cauchy-Schwarz Spectral Moment Bound — f_4·f_0/f_2² ≥ 1. Gaussian is unique saturating cutoff. | S62 | Exact proof |
| 19 | CC = Integrability (Monotonicity Theorem) — dE_ZP/dq > 0 for all q. No interior q-theory equilibrium. | S62 | Exact proof |
| 20 | Filter-Independence Theorem — m_H = 134 GeV tree-level for ALL 6 cutoff families. Structural from CCM. | S62 | Structural |
| 21 | Mode-Independent Occupation Theorem — n_s independent of Bogoliubov |β|². Tilt from geometry only. | S57/S62 | Proven |
| 22 | N_e Saturation Theorem — N_e = 0.1734, independent of initial conditions. | S52 | Structural |
| 23 | Rank-1 Josephson Identity — J_12/J_23 = 19.52, algebraically constant. | S52 | Exact |
| 24 | Gibbons-Hawking Thermodynamic Stabilization — F minimum at τ=0.220, 29% barrier. Parameter-free. | S55 | Proven |
| 25 | Gap Scaling Theorem — Δ_N ~ N^{-1.84} on compact manifold. | S57 | Verified |
| 26 | GGE Universality — all cells identical post-transit, E_DW=0, no domain walls. | S57 | Proven |
| 27 | Volovik Partition — F_Josephson = −336.6 M_KK (95.9% → vacuum); F_BCS+F_BA+F_Leggett = 14.411 M_KK (→ matter). | S58 | Proven |
| 28 | Fold Hessian Signature — S(α) = α·a₂ + a₄ transitions at α_crit=55. Physical regime: fold is SA maximum. | S60 | Proven |
| 29 | Leggett Adiabaticity — P_exc > 0.999 at transit. Deeply diabatic. | S57 | Verified |
| 30–40 | *Additional machine-epsilon infrastructure: KO-dim=6, SM quantum numbers (6 multiplets), [J,D_K]=0 (79,968 pairs), g_1/g_2=e^{-2τ}, Baptista 67/67, D_K 39/39, Riemann 147/147, volume-preserving TT, AZ class BDI, Pfaffian Z_2=+1 throughout, NCG verification chain 7/7 (S61)* | S7–S61 | Machine ε |

### 1C. NEW Since Atlas — S63 Permanent Theorems (T1–T17)

| # | Theorem | Statement | Source |
|:--|:--------|:----------|:-------|
| T1 | Zero First-Order Tensor | Homogeneous transit on M⁴×K produces π_ij=0 | VdD-Hawking |
| T2 | Breathing Mode Exclusion | δg_ab^K = h(x)g_ab^K projects to 4D scalar, not tensor | VdD-Hawking |
| T3 | Scalar-Tensor Kasparov Decoupling | U_total = 1_M ⊗ U_K ⟹ β_T=0 exactly at linear order | VdD-Hawking |
| T4 | Exflation Tensor Theorem | r depends on exactly 3 numbers: ε(0.0216), c_s(0.485), N_e | VdD-Hawking E5 |
| T5 | Volume-Preserving No-Trapping | θ_int=0 identically. Penrose singularity theorem inapplicable | W6-14 |
| T6 | Constant-Epsilon Theorem | n_s = (1−3ε)/(1−ε) for power-law with constant ε, c_s | W4-01 |
| T7 | n_s Gauge Invariance | ε_BLV = 2 − 1/ε_SA (exact). BLV and SA give identical n_s | W1-05 |
| T8 | Hessian Cluster Structure | 10-cluster = Ad(U(2)) decomposition of Sym²(su(3)). By Schur's lemma | W2-06 |
| T9 | Mixed B-F q-theory Exclusion | Same-spectrum B/F has at most one critical point (maximum). 9th CC closure | W3-06 |
| T10 | Cartan Trace Identity | T_{SU(3)}(p,q) = T_{SU(2)}(q,p) = T_{U(1)}(q,p)/12 for ALL (p,q) | W5-07 |
| T11 | Nonlocal Form Factor Inheritance | Analyticity class of F(p²) = analyticity class of f''(z). IDG CC CLOSED | W6-01 |
| T12 | Transfer Function Factorization | T(k_4D|k_KK) = T_proj·T_evo. n_s is cutoff-independent | W6-03 |
| T13 | MaxEnt Gaussian Uniqueness | Gaussian cutoff is unique max entropy solution. Strict concavity + KL divergence | W6-21 |
| T14 | Kinetic Normalization Identity | K_DeWitt = 5.0 exact, τ-independent | W6-25 |
| T15 | Casimir Sigma Scaling | E_Cas(σ) = σ^{-1/8}·E_Cas(1) to machine ε. Pure power-law | W5-03 |
| T16 | S_3 Subgroup Edge-Weight | Josephson anisotropy max/min = 11.80, from S_3 ⊂ S_4 | W3-08 |
| T17 | Proton Decay Tree-Level Zero | Exactly zero by PW orthogonality on SU(3). τ_p = 6.26×10³⁹ yr | W4-04 |

### 1D. NEW Since Atlas — S64–S66 Structural Results

| Result | Session | Status |
|:-------|:--------|:-------|
| R-monotonicity on Jensen (AM-GM exact): dR/dτ ≥ 0 | S64 W1-A | PERMANENT |
| Fermi-surface lock: v²(B2[0]) = 1/2 identically | S64 W2-C | PERMANENT |
| a_0/a_2 trap (off-Jensen): decreasing a_2 INCREASES a_0/a_2 | S64 W2-A | PERMANENT |
| Spectral moment decoupling: F_{−1}(CC) vs F_{+1}(NEC) are different moments | S64 W5-B | PERMANENT |
| H2 theorem: π_{ij}=0 from DeWitt tracelessness (volume-preserving) | S64 W3-A | PERMANENT |
| Chirality antisymmetry: {γ_9, dD_K/dτ}=0. Chiral pairs ADD, not cancel | S64 W6-B | PERMANENT |
| BdG Heat Kernel Factorization — K_BdG(t) = exp(−Δ²t)·K_bare(t) | S64 W3-B / S65 | PERMANENT |
| CC Ratio from Scalar Curvature Only — d(a_0/a_2)/ds = −(a_0/a_2)/R·dR/ds | S65 W1-B | PERMANENT |
| B/F Spectral Asymmetry = 0 — |A|=0 EXACTLY on pure Riemannian triple | S65 W1-C | PERMANENT |
| Bogoliubov Gaussianity Preservation — f_NL = O(ε) regardless of squeezing | S65 W5-D | PERMANENT |
| EIH Casimir Monotonicity — local a_0/a_2 increases with C_2(p,q) | S65 W6-A | PERMANENT |
| Volovik Gibbs-Duhem relaxation — ρ_vac = ε(q)−μq → 0 as q adjusts | S66 W1-A | FUNCTIONAL-INDEPENDENT |
| Chebyshev monotonicity theorem — Q^eff ≥ Q^bare for all UV-suppressing cutoffs | S66 Workshop 1 | PERMANENT |
| BCS-Sakharov decoupling — a_2, a_4 orthogonal projections. r_2=0.892 | S66 Workshop 1 | PERMANENT |
| Anomaly one-parameter family — c_k(φ) = (−1)^k φ^k/k at one loop | S66 Workshop 2 | STRUCTURAL |
| Heat kernel bridge — Spectral action ↔ heat kernel ↔ S-matrix via Bernstein's theorem | S66 Workshop 5 | STRUCTURAL |
| eps_H sign reversal between cutoff families — SCHEME-DEPENDENT at the sign level | S66 W2-A | PERMANENT (negative result) |
| KO-dimension degeneracy at d=8 — B_+/B_- give identical KO signs | S66 W8-A | PERMANENT |

**Total proven mathematical results: 77+ publishable (Atlas D07) + 17 (S63) + 18 (S64–S66) = 112+**

---

## Section 2: Structural Walls (Updated Through S66)

| Wall | Name | Statement | Closures | Sessions |
|:-----|:-----|:----------|:---------|:---------|
| W1 | Weyl Asymptotic F/B | F/B=16/44=0.364, τ-independent by Weyl's law | 6 | S18–S22c |
| W2 | Peter-Weyl Block-Diagonality | D_K exactly block-diagonal. ANY left-invariant metric, ANY compact Lie group | 3 | S22b |
| W3 | Spectral Gap at μ=0 | λ_min>0 at all τ on Jensen. No Fermi surface | 5 | S17a–S34 |
| W4 | Spectral Action Monotonicity | ⟨λ²⟩(τ) monotone. ALL monotone f, ALL Λ, ALL sectors. 9,600 checks | 13+ | S17a–S45 |
| W5 | Berry Curvature Vanishing | K_a anti-Hermitian ⟹ Ω=0 identically. All eigenstates | 0 (preemptive) | S25 |
| W6 | NCG-KK Irreconcilability | Λ_SA/M_KK = 10⁶–10¹⁵ at all tested τ | 0 (interpretive) | S30–S31 |
| W7 | α_s = n_s²−1 Identity | Structural for ANY K² propagator on compact Josephson lattice. 5 proofs | 3 | S50 |
| W8 | Anderson-Higgs Impossibility | K_7 is diffeomorphism, not gauge. [D_K,K_7]=0 at all orders | 1 | S51 |
| W9 | Convex Combination Theorem | n_s of additive mixture bounded. At K_pivot=2.0: max n_s=0.15 | 1 | S51 |
| W10 | Zero-Mode Protection on T² | Goldstone KK n=0 mode. ⟨0|V|n⟩=0 to all orders in Born series | 2 | S50–S51 |

**NEW since Atlas (S63–S66 — not yet numbered as walls but structural):**

| Candidate | Statement | Session |
|:----------|:----------|:--------|
| R-monotonicity | dR/dτ≥0 by AM-GM on volume-preserving Jensen. a_2 diverges exponentially | S64 |
| a_0/a_2 trap | Decreasing R (off-Jensen) INCREASES a_0/a_2. CC worsens on descent | S64 |
| Frustration triangle | No single spectral centroid η satisfies n_s(red) + CC(small) + Mott(accessible) | S66 |

---

## Section 3: Complete Gate Verdict Registry

### 3A. Cumulative Gate Statistics

| Source | Period | Total | PASS | FAIL | INFO | CLOSED | CONDITIONAL |
|:-------|:-------|:------|:-----|:-----|:-----|:-------|:------------|
| Permanent registry | S7–S28 | ~30 | 12 | 5 | — | 8 | 1 (KC-3) |
| Mega-matrix | S29–S31 | ~20 | 6 | 6 | — | 5 | — |
| Sessions S52–S60 | S52–S60 | ~50 | 15 | 20 | 15 | — | — |
| Session 61 | S61 | 91 comps | — | — | — | — | — |
| Session 62 | S62 | 21 | 11 | 1 | 6 | — | — |
| Session 63 | S63 | 69 | 31 | 7 | 31 | — | — |
| Session 64 | S64 | 33 | 8 | 9 | 16 | — | — |
| Session 65 | S65 | 37 | 11 | 11 | 12 | — | 1 (DESI DR3) |
| Session 66 | S66 | 40+ | 12+ | 12+ | 16+ | — | — |

### 3B. Landmark Gate Verdicts (Framework-Defining)

| Gate | Verdict | Decisive Number | Session | Impact |
|:-----|:--------|:----------------|:--------|:-------|
| K-1e | DECISIVE CLOSURE | M_max 6.5–12.9x below threshold | S23a | Venus Moment: 44%→8% |
| V-1 | CLOSED | V_spec monotone ALL ρ | S24a | Framework nadir |
| KC-1–KC-5 | 5/5 PASS | Bogoliubov, T-matrix, mu_eff, Luttinger, BCS gap | S28–S29 | BCS chain complete |
| CUTOFF-SA-37 | STRUCTURAL CLOSURE | All monotone f, all Λ, all sectors | S37 | Paradigm shift to transit |
| KZ-NS-62 | CONDITIONAL PASS | n_s = 0.9567 (1.9σ from Planck) | S62 | First viable n_s |
| DILUTION-CC-66 | PASS (Scenario B) | ρ_vac(today)/ρ_obs = 1.032 (0.01 OOM) | S66 | CC reframe |
| ZETA-SA-66 | INFO | ε_H sign reversal (cutoff +0.022 vs zeta −0.045) | S66 | Spectral functional crisis |
| AMPLITUDE-NORM-66 | FAIL (marginal) | A_s gap 3.15 OOM (Route A) | S66 | Normalization crisis |
| QTHEORY-NPAIR-66 | FAIL | min|P_vac|=2.34e-7 M_Pl⁴ (113.5 OOM) | S66 | Discrete self-tuning fails |

---

## Section 4: Mechanism Closures (Complete Tally)

### 4A. Cumulative Closure Count

| Era | Sessions | Closures | Running Total |
|:----|:---------|:---------|:-------------|
| I: Perturbative Potential | S17–S22 | 16 | 16 |
| II: Post-Perturbative | S23–S31 | 10 | 26 |
| III: BCS Chain & Instanton | S35–S38 | 7 | 33 |
| IV: Transit & Cosmology | S39–S46 | 15 | 48 |
| V: n_s Crisis & Fabric | S46–S49 | 7 | 55 |
| VI: O-Z Investigation | S50–S51 | 20 | 75 |
| VII: Spectral Action Triad | S61–S62 | 8 | 83 |
| S52–S60 (fabric-scale) | S52–S60 | 33+ | 116+ |
| S63 (spectral ops precursor) | S63 | 9+ | 125+ |
| S64 (CC combo) | S64 | 8 | 133+ |
| S65 (CC budget) | S65 | 8 | 141+ |
| S66 (spectral ops) | S66 | — (refinements) | 141+ |

### 4B. Sagan 4-Topic Grouping

All closures reduce to 4 independent structural topics (S25 Redux correction):

| Topic | Root Cause | Closure Count | Key Wall |
|:------|:-----------|:-------------|:---------|
| A: Perturbative potential | Spectral action monotonicity + Weyl F/B ratio | ~40 | W1, W4 |
| B: Inter-sector coupling | Block-diagonality theorem | ~10 | W2 |
| C: BCS at μ=0 | Spectral gap, particle-hole symmetry | ~8 | W3 |
| D: Dynamic/fabric-scale | Various specific mechanisms | ~80+ | Various |

### 4C. Key Individual Closures Not in Atlas (S52–S66)

| Mechanism | Session | Kill Shot |
|:----------|:--------|:----------|
| E-fold mapping (N_e=0.1734, IC-independent) | S52 | Structural theorem |
| BCS baryogenesis (φ_CP=0 identically) | S52 | Algebraic |
| Lattice ED stabilization | S54 | d²E_0/dτ²=0.33, 193x below threshold |
| Gauge frustration | S56 | <3.5% flux quantum |
| Unimodular gravity for CC | S60 | Volume preservation ≠ CC suppression |
| CC staircase | S60 | |Λ_res| oscillates, no convergence |
| Leptogenesis (real M_R) | S60 | No CP phase |
| Fiber skyrmion baryogenesis | S64 | M_skyrm = 1.27e5 M_KK (22 OOM above proton) |
| CC Path C (Jensen transit) | S64 | R(τ) monotone by AM-GM |
| CC Path B (Gaudin integrability) | S64 | 94.6% ρ_ZP outside Gaudin space |
| B/F spectral asymmetry for CC | S65 | |A|=0 EXACTLY on Riemannian triple |
| Theta-vacuum CC scanning | S65 | a_3=0 by Gilkey's theorem |
| EIH effacement for CC | S65 | Monotonic with C_2 (wrong direction) |
| Nonlocal SA for CC | S65 | All nonlocal filters INCREASE a_0/a_2 |
| Mott transition CC | S65 | E_J/E_C=194 (571x above critical) |

---

## Section 5: Observational Scorecard

### 5A. Framework Predictions vs Observation (S66 State)

#### CMB Sector

| Observable | Framework | Observed | Tension | Verdict | Classification |
|:-----------|:----------|:---------|:--------|:--------|:---------------|
| n_s | 0.9567 (Hubble SA) | 0.9649±0.0042 | 1.9σ | CONDITIONAL PASS | SCHEME-DEPENDENT |
| n_s (BCS+CW) | 0.9595 | same | 1.3σ | INFO | SCHEME-DEPENDENT |
| dn_s/d ln k | +0.000715 | −0.0045±0.0067 | 0.78σ | PASS | — |
| α_s (slow-roll, L=4) | −0.038 | −0.0045±0.0067 | 5.0σ | FAIL (formula suspect) | — |
| α_s (acoustic, CMB) | ~0 | same | CONSISTENT | Pending TRANSIT-PS-67 | — |
| r (second-order) | 0.024–0.033 | <0.036 | — | PASS | FUNCTIONAL-INDEPENDENT |
| ΔN_eff | 0.027 | 0.15±0.23 | 0.5σ | PASS | FUNCTIONAL-INDEPENDENT |
| A_s (Route A) | 8.73e-2 | 2.1e-9 | 7.62 OOM | FAIL | — |
| A_s (Route B, PW) | gap 3.15 OOM | same | 3.15 OOM | FAIL (marginal) | — |

#### Particle Physics

| Observable | Framework | Observed | Tension | Verdict |
|:-----------|:----------|:---------|:--------|:--------|
| m_H (Gaussian, L=6) | 131.8 GeV | 125.1 GeV | 5.4% | CONDITIONAL PASS |
| m_H (Richardson extrap.) | 129.0 GeV | 125.1 GeV | 3.1% | INFO |
| m_H (Aitken, S66) | 127.5 GeV | 125.1 GeV | 1.9% | CONVERGING |
| sin²θ_W | 0.2307 | 0.2312 | 0.2% | PASS |
| M_W | 80.41 GeV | 80.38 GeV | 0.05% | PASS |
| τ_p | 6.26×10³⁹ yr | >1.6×10³⁴ yr | 5 OOM margin | PASS |
| Yukawa rank | 2 | 3 | rank deficient | OPEN |

#### Dark Matter

| Observable | Framework | Observed | Tension | Verdict |
|:-----------|:----------|:---------|:--------|:--------|
| Ω_DM h² (Leggett-only) | 0.120 | 0.1186±0.0020 | 0.7σ | PASS |
| z_eq (Leggett) | 3425 | 3402±26 | 0.88σ | PASS |
| σ/m | 0 | <1.25 cm²/g | — | PASS |
| Direct detection | 0 | null | — | PASS |
| Annihilation | 0 | null | — | PASS |
| λ_fs (WDM) | 9.85e-23 Mpc | <0.1 Mpc | 22 OOM safe | PASS |

#### Dark Energy / CC

| Observable | Framework | Observed | Tension | Verdict |
|:-----------|:----------|:---------|:--------|:--------|
| w_0 | −0.918 | −0.752±0.057 (DESI DR2) | 2.9σ | TENSION |
| w_a | ~0 | −0.73±0.25 (DESI DR2) | 2.9σ | TENSION |
| CC (Volovik Scenario B) | ρ_obs × 1.032 | ρ_obs | 0.01 OOM | PASS |
| CC (conservative stackable) | 107.7 OOM gap | — | — | FAIL |

#### Non-Gaussianity (S66 Predictions)

| Observable | Framework | Observed | Status |
|:-----------|:----------|:---------|:-------|
| f_NL^{equil} (c_s<1) | ~1.12 | −26±47 | CONSISTENT, CMB-S4 testable |
| f_NL^{GGE diagonal} | ~0.13 | — | Prediction |
| f_NL shape | Folded triangles (k_1+k_2=k_3) | — | Unique to GGE (not single-field) |

### 5B. Observational Programs Cross-Reference (56 catalogued)

Key discriminants (from observational avenues document):

| Program | Test | Framework Status | Timeline |
|:--------|:-----|:----------------|:---------|
| DESI DR3 | w_0, w_a joint constraint | 2.9σ tension; pre-registered decision rules | 2026–2027 |
| CMB-S4 | r, α_s, f_NL | r=0.024–0.033 testable; α_s decisive | 2028+ |
| JUNO | Mass ordering | Normal ordering predicted | 2026–2028 |
| BICEP/Keck | r<0.036 | PASS at current limit | Ongoing |
| Euclid | f·σ_8, lensing | 2.96σ reach; σ_8=0.799 discriminant | 2027+ |
| ALPHA-g | Antimatter gravity | a_g=g exactly ([J,D_K]=0) | 2026–2028 |

---

## Section 6: The CC Budget (S66 State)

### 6A. Raw Gap and Stackable Corrections

```
RAW GAP (q-theory, gravity route):              114.0 OOM
                                                ──────────
CLASS A: Structural stackable corrections
  A1  Sakharov G_N factor (2.3x)                 −0.36
  A2  BCS occupation (7.5%)                       −1.12
  A3  N_cells Voronoi (32 cells)                  −1.51
  A4  Gravitational backreaction (α_G)            −3.58
  A5  Sakharov BdG (31% of target)                −0.16
  A6  Volume R-max                                −0.03
  A7  Orbifold Z₃×Z₃                             −0.08
  A8  Inhomogeneous O'Neill                       −0.004
                                        Subtotal  −6.84

CLASS C: Wrong-direction corrections
  C1  BCS dressing ratio                          +0.05
  C2-5 Orbifold Z₃, U(1), EIH, nonlocal          +0.49
                                        Subtotal  +0.54

CLASS B: Zeta functional (scheme change)
  B1  a_0 eliminated, β₁M⁴                       −5.0 (ESTIMATED)

                                                ──────────
AFTER ALL COMPUTED CORRECTIONS:                 102.7 OOM remaining
                                                ──────────
```

### 6B. The S66 Paradigm Shift: Volovik Relaxation

**DILUTION-CC-66 PASS (Scenario B)**:
- Volovik q-theory relaxation: ρ_vac ~ M_Pl²·H²
- Landing: ρ_vac(today)/ρ_obs = 1.032 (0.01 OOM from observation)
- The 114 OOM is NOT a problem to solve — it IS exflation (the expansion history)
- Standard inflation carries equivalent ~111 OOM gap

**Three scenarios mapped:**

| Scenario | Mechanism | CC Residual | Status |
|:---------|:----------|:------------|:-------|
| A: Constant w=−1 + GGE dilutes | GGE dilution only | 113.6 OOM | FAIL |
| B: Volovik ρ~H² | Thermodynamic tracking | 0.01 OOM | PASS |
| B2: Uniform w=−0.918 | DESI equation of state | 106.7 OOM | FAIL |

### 6C. Remaining Structural Issue

The **a_0 topological obstruction**: a_0=6440 is an integer (mode count) that cannot relax continuously. The zeta action avoids this by excluding a_0 (from noncommutative integral projection onto leading zeta pole). This is the sole remaining structural issue for the Volovik mechanism.

**BBN constraint**: ρ_vac/ρ_rad=0.67 at nucleosynthesis in Scenario B. Transit (Workshop 4) argues vacuum enters Friedmann as G renormalization, not additional species. QA derives tracking margin Γ_β/H_BBN ~ 10¹¹. **BBN-VOLOVIK-67** is a CRITICAL S67 gate.

---

## Section 7: The Three Crises

### 7A. Spectral Functional Crisis

**The problem**: ε_H changes SIGN between cutoff families.
- sqrt(x): ε_H = +0.02163 → n_s = 0.9567 (RED tilt, Planck-compatible)
- Zeta/exponential: ε_H < 0 → n_s > 1 (BLUE tilt, excluded)
- n_s spread across functionals: 0.164 (39× Planck error bar)

**Resolution path**: Anomaly + conservation hierarchy → one-parameter dilaton family c_k(φ)=(−1)^k φ^k/k. Bayesian evidence collapses model space: exp(−x) excluded at 15.5σ, compact at 36.9σ. Only sqrt(x) and anomaly(φ) survive. Higgs mass discriminant: m_H^{zeta}~174 GeV vs m_H^{cutoff}~127.5 GeV. Observation at 125.1 GeV selects cutoff at percent level.

**Status**: FUNCTIONAL-SELECT-67 is a CRITICAL S67 gate.

### 7B. Amplitude Normalization Crisis

**The problem**: A_s gap 3.15 OOM. "Right universe, wrong volume."
- All spectral-geometric RATIOS match observation (n_s, sin²θ_W, M_W, Ω_DM)
- All absolute AMPLITUDES fail (A_s, CC, H₀)
- S_fold (vacuum spectral action) used where S_occ (occupied-state) needed

**Status**: TRANSIT-PS-67 may resolve simultaneously with α_s.

### 7C. Alpha_s Falsification Threat

**The problem**: α_s = −0.038 at 5.0σ from Planck.
- Slow-roll formula inapplicable at Mach 13.8
- ATDHFB calibration (nuclear fission): factor 2–5× reduction, saturates at deeply diabatic limit
- Acoustic prediction (QA): α_s(CMB)~0 from 56 OOM scale hierarchy (sinc² spectral envelope)
- Pre-registered range: [−0.019, −0.008] (ATDHFB) or ~0 (acoustic limit at CMB scale)

**Status**: TRANSIT-PS-67 must deliver α_s as function of k. CRITICAL.

---

## Section 8: Retractions & Corrections (Complete Log)

### 8A. Through S51 (Atlas D09): 25 Items

| # | Type | Claim | Session Made→Corrected | Impact |
|:--|:-----|:------|:-----------------------|:-------|
| 1 | CORRECTION | AZ class DIII→BDI | S17c | Low |
| 2 | RETRACTION | "4-5x inter-sector coupling" | S21b→S22b | Moderate |
| 3 | ERRATUM | Berry curvature 982.5 → quantum metric | S24a→S25 | Low |
| 4 | CORRECTION | a_6 "all a_{2n} monotone" → conjecture beyond a_6 | S24a→S27 | Low |
| 5 | RETRACTION | P_LZ=0.97 (LZ inapplicable, codim-1) | S28 | Moderate |
| 6 | CORRECTION | φ_paasch: prediction→mathematical property | S12→S28 | Moderate |
| 7 | CORRECTION | Tesla g*N(0): 8–10→3.24 | S22c | Low |
| 8–10 | RETRACTION chain | K-1e→TRAP-33b→corrected V | S23a→S33b→S34 | HIGH (triple) |
| 11–12 | CORRECTIONS | J operator, V matrix | S34 | Low |
| 13 | CORRECTION | Kapitza ratio 5.98→0.030 | S31→S38 | Low |
| 14 | RETRACTION | "Liberated NG mode" | S38 W3 R1→R2 | Low |
| 15 | RETRACTION | Schwinger-instanton duality (numerology) | S38→S39 | Moderate |
| 16 | RETRACTION | GGE permanence (V_phys 13% non-separable) | S38→S39 | HIGH |
| 17 | RETRACTION | CDM λ_fs=3e-48 Mpc→89 Mpc (wrong velocity) | S42→S43 | HIGH |
| 18–19 | RETRACTIONS | S42 eta, S43 DM/DE overshoot | S42–S44 | Moderate |
| 20 | CORRECTION | CUTOFF-F-44 framing | S44 | Low |
| 21 | RETRACTION | S45 α=0.41 (entropy mismatch) | S45→S46 | Moderate |
| 22 | RETRACTION | Analog horizons (no superflow) | S48→S49 | Moderate |
| 23 | CORRECTION | CMPP Type II→Type D (Riemannian artifact) | S49→S50 | Low |
| 24 | CORRECTION | σ_8 shift "21% excluded" (14x overestimate) | S49→S50 | Moderate |
| 25 | CORRECTION | B_1D=20.9 (compared derived param, not raw BAO) | S49→S50 | HIGH |

### 8B. S52–S60 Retractions

| # | Type | Claim | Session Made→Corrected | Impact |
|:--|:-----|:------|:-----------------------|:-------|
| 26 | RETRACTION | H₀=68.8 km/s/Mpc (S59) | S59→S60 | HIGH ((1,2) irrep data bug) |
| 27 | DOWNGRADE | GGE permanence→conditional on Josephson isolation | S38→S60 | Moderate |
| 28 | DOWNGRADE | PENROSE-ACCESS-59→INFO (P=0.574) | S59→S60 | Moderate |

### 8C. S63 Retractions (4)

| # | Type | Claim | Corrected To |
|:--|:-----|:------|:-------------|
| 29 | RETRACTION | S62 "strong coupling" S_1loop/S_b=0.52 | Species-counting effect (g=0.003) |
| 30 | CORRECTION | S62 "Λ=0 via Jacobson" | Entropy conflation corrected |
| 31 | RETRACTION | S57 dynamical exponent z=3.68 | Compound artifact; true z=2.00 |
| 32 | RETRACTION | S62 "44.7% quantum depletion" | True occupation depletion=5.12% |

### 8D. S64–S66 Corrections

| # | Type | Claim | Session |
|:--|:-----|:------|:--------|
| 33 | RETRACTION | S64 subsonic transit claim | S64 (corrected within session: Mach 13.8) |
| 34 | CORRECTION | S66 w_a=+1.121 (CPL structurally inadequate) | S66 W4-C |

**Total retractions/corrections: 34 through S66**

---

## Section 9: S67 Priority Queue

From S66 Workshop Master Synthesis Section VI, with all 10 reviewer computation tables consolidated.

### 9A. CRITICAL Priority (4 computations)

| ID | Computation | Workshops | Pre-Registered Gate |
|:---|:-----------|:----------|:-------------------|
| TRANSIT-PS-67 | Full Bogoliubov power spectrum through fold | 4/5 | PASS: |α_s(k_CMB)|<0.015; FAIL: >0.019 |
| LEGGETT-GRAV-DECAY-67 | Gravitational decay vertex ⟨g,g|H_grav|L⟩ | 1/5 (critical) | PASS: Γ_grav<H_0; FAIL: Γ_grav>H_0 |
| FUNCTIONAL-SELECT-67 | Dilaton φ along anomaly family; n_s∩m_H | 2/5 | PASS: unique φ with n_s∈[0.955,0.975] AND m_H∈[122,130] |
| BBN-VOLOVIK-67 | Volovik tracking EOS at T_BBN=1 MeV | 3/5 | PASS: |w_vac−1/3|<0.03; FAIL: >0.10 |

### 9B. HIGH Priority (5 computations)

| ID | Computation | Pre-Registered Gate |
|:---|:-----------|:-------------------|
| BA-LIFETIME-FABRIC-67 | BA phonon thermalization on CG(24) | PASS: Γ_BA/H(z_eq)>10; FAIL: <0.1 |
| JOINT-FALSIFICATION-67 | Multi-channel test across functionals | PASS: ≥1 f satisfies all 4 channels |
| BAYESIAN-FUNCTIONAL-67 | Planck evidence Z_i for surviving functionals | PASS: posterior n_s within 2σ AND Ω_DM within 10% |
| GGE-BISPECTRUM-67 | f_NL from in-in formalism on GGE relic | Prediction: f_NL^{equil}~1.12 |
| PROJECTED-MOMENTS-67 | a_0,a_2,a_4 from RG exact occupations | PASS: |δa_2/a_2|<10% at N_pair=4 |

### 9C. MEDIUM Priority (10 computations)

FINITE-SIZE-SCALING-67, VHS-CLASSIFY-67, HIGGS-ZETA-67, WGC-SATURATION-67, MULTIFIELD-DELTA-N-67, ISOCURVATURE-67, SPECTRAL-ENDPOINT-67, CONSERVATION-HIERARCHY-TEST-67, CHEUNG-NS-CORRECTION-67, COMPACTION-WA-SIGN-67

### 9D. LOW Priority (12 computations)

FUNCTIONAL-FIXED-POINT-67, FABRIC-PROJECTED-MOMENTS-67, GGE-TWO-FLUID-67, VOLOVIK-Q-A0-67, GGE-VOLOVIK-RELAX-67, FOLD-CURVATURE-RATIO-67, SUB-GAP-FUNCTIONAL-SCAN-67, DESI-VOLOVIK-67, FEATURE-AMPLITUDE-67, BCS-4PT-WILSON-67, LEGGETT-SPECTRAL-DIM-67, OEE-FILLING-SCAN-67

---

## Section 10: Framework Document Readiness Assessment

### 10A. Document Staleness

| Document | Current Through | Sessions Behind | Needed Updates |
|:---------|:---------------|:---------------|:---------------|
| Atlas D01–D10 | S62 | 4 (S63–S66) | 170+ comps, 17 theorems, CC reframe, functional crisis, Volovik PASS |
| Permanent results registry | S28 | 38 (S29–S66) | ~100 new theorems, ~100 new closures, ~20 new walls/gates |
| Session finals | S62 (atlas-produced) | S63–S66 missing clean finals | 4 session finals needed |
| EVOI framework | S61 | 5 | S66 reframe changes all priorities |
| Constraint mega-matrix | S31 (+S51 appendix) | 15+ | S52–S66 closures not in matrix |
| Observational avenues | S28 | 38 | Major updates: n_s recovery, CC reframe, DM Leggett, r prediction |

### 10B. Publication Candidates

**Ready for journal submission (standalone math):**
1. Block-diagonality universality theorem (JGP/CMP)
2. Spectral action monotonicity + structural monotonicity (JGP/CMP)
3. 8D Petrov classification on Jensen-deformed SU(3) (GRG)
4. Van Hove zero-critical-coupling on compact manifolds (CMP/PRL)
5. α_s = n_s²−1 structural identity (CMP/PRD)
6. CF-9 triple identity Berry=NCG=KK (JGP/CMP)
7. Filter-independence theorem for Higgs mass (PRD/CMP)

**Near-ready (need one more verification):**
8. Anderson-Higgs impossibility for Kosmann-derived U(1) (JGP)
9. CC = integrability monotonicity theorem (CMP/PRD)
10. Cauchy-Schwarz spectral moment bound with Gaussian uniqueness (JGP)

**Require S67 computation results:**
- n_s from transit Bogoliubov (needs TRANSIT-PS-67)
- Leggett DM observational paper (needs LEGGETT-GRAV-DECAY-67)
- CC via Volovik relaxation (needs BBN-VOLOVIK-67)

### 10C. What S67 Must Deliver

Three computations determine the framework's observational future:

1. **TRANSIT-PS-67** — resolves α_s (falsification threat), A_s (normalization gap), n_s(k) simultaneously
2. **LEGGETT-GRAV-DECAY-67** — if FAIL, DM sector collapses entirely (Ω_DM h²=0.120 meaningless)
3. **FUNCTIONAL-SELECT-67** — determines whether n_s is a prediction or accommodation

The framework's structural skeleton is proven. Its observational contact requires these three computations.

---

## Appendix: Key Constants and Numbers

| Quantity | Value | Source |
|:---------|:------|:-------|
| τ_fold | 0.190 | Van Hove singularity |
| S_fold | 250,361 | Spectral action at fold |
| dS/dτ | +58,673 | Gradient at fold |
| d²S/dτ² | +317,863 | Curvature at fold |
| ε_H | 0.02163 | Hubble slow-roll parameter |
| c_BLV | 0.485 | Fabric sound speed |
| Mach number | 13.75 | Transit speed / sound speed |
| N_e | 3.73e-3 | Physical transit e-folds (S64) |
| M_KK | 7.429×10¹⁶ GeV | Gravity-route extraction |
| a_0 | 6440 | Mode count (τ-independent) |
| a_2(fold) | 2776.17 | Second Seeley-DeWitt coefficient |
| a_4(fold) | 1350.72 | Fourth Seeley-DeWitt coefficient |
| Δ_B3 | 0.370 M_KK | BCS gap at fold |
| ω_L1 | 0.138 M_KK | Leggett mode frequency |
| Q_Leggett | 18.6 | Quality factor |
| E_J/E_C | 8.57 (zeta a_4) | Josephson ratio |
| φ_paasch | 1.531580 | Eigenvalue ratio at τ=0.15 |
| 155,984 | — | D_K eigenvalues at L_max=10 |
| 32 | — | Tessellation cells (CG(24)) |

---

*Compiled from: permanent-results-registry.md, Atlas D01–D10, session working papers S52–S66, constraint-mega-matrix.md, evoi-framework.md, observational_avenues.md, CC-budget.md, session-66-workshop-master-synthesis.md, session-66-inflation-exflation-synthesis.md. All numbers from source computations, not re-derived.*

## FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030

**Source**: S86 W-2 A_s Band-Authority workshop (closed 2026-04-25) + mack S-7 §V.2 carry-forward (S85). Landed by gate `S86-FROZEN-COMMIT-LANDING` (S86 W13-P1, mack-cosmic-bridge).

**Window**: 2026-04-25 → 2030-12-31 (4-year external-clock window covering BK-Array 2026 → DESI DR3 2027 → CMB-S4 2028 → PIXIE 2029+ → LiteBIRD 2030).

**Discipline**: NO re-pin of any framework prediction during this window unless EITHER:
1. external observational data forces a reversibility trigger PRE-REGISTERED at landing time (e.g., DR3 R_842 reversibility for w_0 per S84-W1b-9), OR
2. the pre-registration itself is structurally incomplete (PRU Class 8) and the plan author re-files via PRDR (per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness).

**Frozen predictions covered (canonical-source pinned)**:

| Observable | Frozen value | Canonical-constants name | Source pin |
|:-----------|:-------------|:-------------------------|:-----------|
| `n_s` | 0.9649 | `planck_ns` | Planck 2018 TT,TE,EE+lowE+lensing; S65 / S85 W1c-1 |
| `r` (Path-C, substrate-compaction) | 0.0117 (canonical 0.0117315222) | `r_CMB_framework` | S83 G46 TENSOR-TRANSFER PASS |
| `r` (Path-H, transverse fiber-osc) | 0.00745 | (Path-H derivation; W-2 workshop) | S86 W-2 closure 2026-04-25 |
| `w_0` PRIMARY | -0.918 | `w0_FW` | Volovik vacuum + effacement (S58); §W13-3 P9 adjudication |
| `α_s_inflation_framework` | -0.068968 | `alpha_s_inflation_framework` | S50-51 identity α_s = n_s² − 1; UNCHANGED across canonical update of P12 §W13-5 (the framework prediction is frozen; only the reference observational canon moved) |
| `f_NL_folded` | 3 pathways | (per §W13-2 P10 registry) | GGE-equilateral 0.0547 (S82) / GGE-folded 0.129 (S67) / analytic-template-folded 0.7685 (S85 W9-3) |
| `A_s` | 3.11e-09 → 4.27e-09 | (ε-range) | ε ∈ [0.02, 0.02163] per W14 W5 |

**Reversibility triggers** (per landed prediction; the ONLY conditions under which a frozen pin may be updated within the 2026-2030 window):

- `w_0`: DR3 publication. Trigger event = R_842 rectangle lockout per S84-W1b-9 (`content_sha256=9cc7f47e…79d9f`). Window opens 2026-04-23.
- `r`: TWO-step trigger chain:
  1. BK-Array publication (BICEP/Keck 2026, per S84-W4-42 4-branch tree, `content_sha256=e2ca24d6…882d3`),
  2. AND LiteBIRD publication (2030, per §W13-7 P2 SEQUENCED detector chain).
  Both legs of Both-Pathways (Path-H + Path-C) carry parallel reversibility under the SAME trigger chain.
- `α_s`: CMB-S4 publication (2028+). Per S86 C36 quarterly poll for explicit σ(α_s) forecast availability; pin is updatable on canon drift via `update_constant("alpha_s_inflation_framework", ...)` only.

**Citation discipline**: every downstream gate citing "the framework's <X> prediction" MUST reference the frozen value via the canonical-constants name (NOT a copy-pasted literal); `audit_sha256` closure REQUIRED on any verdict line that cites a frozen pin.

**What this discipline IS** (per phononic framing): this is the **substrate's commitment to its own predictions for the duration of the active detector window**. It is NOT a confidence claim; it is a refusal to engage in convention-shopping (S78 Class 1) under post-data pressure. Each frozen pin is a substrate-channel observable; the discipline is the substrate's self-restraint against post-hoc data-fitting.


## 4-Level Unit-Class Taxonomy (S86 W-2 workshop landing)

**Source**: S86 W-2 A_s Band-Authority workshop (closed 2026-04-25). Precursor: `.claude/agent-memory/mack-cosmic-bridge/project_s73a_mack_vdd_workshop_r2.md` (4-level sub-derivation layer split). Landed by gate `S86-FROZEN-COMMIT-LANDING` (S86 W13-P1).

**Purpose**: partition substrate-prediction OBJECTS by which sub-derivation layer they live in, and assign each level a per-level edit-discipline. The taxonomy prevents convention-shopping at the framework level by making the editable-versus-frozen status of each sub-layer explicit.

| Level | Layer | Examples | Edit-discipline (2026-2030) |
|:-----|:------|:---------|:----------------------------|
| **Priority 1** | **Fold structural-floor** — substrate eigenvalue structure at the fold; non-negotiable | `L_max = 10` D_K spectral cache; M_KK gravity scale; `tau_fold = 0.190`; Δ_BCS gap; `S_fold = 250,361`; the 155,984 D_K eigenvalues | **NEVER edit** during 2026-2030. A change at Level 1 invalidates the entire downstream cascade — every Level 2/3/4 prediction inherits from this layer. |
| **Priority 2** | **Pre-fold convention-pin** — substrate-internal convention choices that fix the gauge BEFORE the fold but admit alternative fixings | regulator class (zeta / Pauli-Villars / Mellin / lattice / cutoff per `.claude/rules/regulator-pin-discipline.md`); scheme convention; normalization factors; cluster-span span-2/span-3 metric choice | Edit ONLY via PRDR sub-diff at plan-freeze (NOT post-hoc). A Level 2 edit requires a `pre-registration-update:` log entry on the producing gate; iteration-until-PASS is forbidden (S78 Class 6 / `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS). |
| **Priority 3** | **Observational boundary** — the post-fold substrate-to-observable map | transfer functions (e.g., `T(k)` for the tensor sector); Fisher convolutions (CMB-S4, LiteBIRD, DESI DR3 σ matrices); detector response models | Edit ONLY via documented detector-data update — e.g., a new Fisher PDF SHA-pinned per S86 C32 / W4-3 / W4-6. Updates land as additive Fisher-pin entries, never as silent overwrites. |
| **Priority 4** | **Observational prediction** — the final number that lands in `falsifier-master-inventory.md` | `r = 0.01173` (Path-C) / `r = 0.00745` (Path-H); `n_s = 0.9590` framework / `n_s = 0.9649` Planck canon; `w_0 = -0.918`; `α_s = -0.068968`; CGWB ρ_AC | Edit ONLY via reversibility trigger (per FROZEN-PREDICTION-DISCIPLINE-COMMIT) AND re-derivation through Levels 1-3. Level 4 cannot be edited in isolation; an upstream-level change is required. |

**Key load-bearing level per observable**:

- `A_s` band-authority (W3-7 / W-2): Level 2 12.5% scheme-floor flag is load-bearing; Level 3 30% severity-band is load-bearing for severity reporting; Level 4 factor-2 (PASS-F2) is load-bearing for the closure decision. Each band corresponds to a different Level; collapsing them into a single number was the W3-7 confusion now retired.
- `r` (Both-Pathways): Level 2 scheme-floor flag is 12.5%; Path-H vs Path-C split is 36.5% > 12.5% → registered as a Level 4 DUAL-PATHWAY observable, NOT a scheme artifact (per Element 3 below).
- `w_0`: Level 4 PRIMARY = -0.918 (per §W13-3 P9 adjudication); branch (iv) -0.842454 retracted to single-branch (iv) per S83 R3 audit.
- `α_s`: Level 4 framework = -0.068968 (S50 identity), UNCHANGED across the canonical update of P12 §W13-5 — that update is a Level 3 boundary edit (Aiola 2020 ACT DR4 +1σ drift in the Planck canon `n_s_canon`), NOT a Level 4 framework prediction edit.

**What this taxonomy IS** (per phononic framing): the 4-level partition is **substrate self-knowledge** — it tells the framework which of its own internal layers it is allowed to revisit and which are frozen for the detector window. It is NOT a hierarchy of confidence; it is a hierarchy of editability. Level 1 is fixed by the substrate's own eigenvalue structure; Level 2 is fixed by convention choice; Level 3 is fixed by external instrumentation; Level 4 is the substrate's emitted prediction.


## r Both-Pathways Registration (S86 W-2 workshop landing)

**Source**: S86 W-2 A_s Band-Authority workshop (closed 2026-04-25). Cross-references §W13-7 P2 (`falsifier-master-inventory.md` extension). Landed by gate `S86-FROZEN-COMMIT-LANDING` (S86 W13-P1). Detailed schema row produced by gate `S86-R-BOTH-PATHWAYS-WATCHLIST-LANDING` (S86 W13-P2, volovik-superfluid-universe-theorist).

**Statement**: the substrate's tensor-to-scalar ratio has TWO sub-channel projections — transverse fiber-oscillation (Path-H) and substrate-compaction (Path-C) — that test the substrate's tensor-mode generation mechanism via TWO complementary detectors at TWO times. This is NOT "the framework predicts two numbers"; it is a dual-registration discipline for ONE observable derived through TWO methodologically-distinct projections.

| Pathway | r | n_T (consistency relation) | scheme | source_gate |
|:--------|:--|:---------------------------|:-------|:------------|
| **Path-H** (Hawking pathway: transverse fiber-oscillation) | 0.00745 | -0.000931 (n_T = -r/8) | transverse-fiber-mode-derivation | W-2 workshop derivation |
| **Path-C** (Connes pathway: substrate-compaction) | 0.0117315222 (reported 0.0117) | -0.001466 (n_T = -r/8) | tensor-transfer-G46 | S83 W3-G46 TENSOR-TRANSFER PASS |

**Split (3-way documentation per §W13-7 P2)**:

- Raw ratio: `r_PathC / r_PathH = 1.5747`
- Path-H-relative split: `(r_PathC − r_PathH) / r_PathH = 0.5747` (≈ 57.5%)
- **Path-C-relative split: `(r_PathC − r_PathH) / r_PathC = 0.3650` (≈ 36.5%; the registered "split" per plan §W13-6 EDIT SPEC; matches §W13-7 P2 ≈36.3%)**
- The plan's ≈36.3% citation in §W13-7 P2 is the same Path-C-relative form within rounding; the registered split for downstream live-watch use is **36.5%**.

**Scheme-floor flag**: 12.5% (per S86 C27 W3-7 PASS-clause re-pin; this is the Level 2 floor below which a split is considered convention noise rather than a substrate observable).

**Registration verdict**: 36.5% > 12.5% → registered as **DUAL-PATHWAY observable**, NOT scheme artifact. r is therefore the substrate's TWO-channel prediction for the tensor-to-scalar ratio; downstream gates citing r MUST select Path-H or Path-C explicitly (or carry both rows side-by-side under Both-Pathways framing).

**SEQUENCED detector chain** (per §W13-7 P2 + S84 W4-42):

1. **BK-Array 2026** (BICEP/Keck) — first detector window. 4-branch decision tree pre-registered per S84 W4-42 (`content_sha256=e2ca24d6…882d3`). Both pathways' r values fall inside the same upper-leg branch under any r ≲ 0.020 detection; first separation point arrives only with sub-percent σ(r).
2. **LiteBIRD 2030** — second detector window. σ(r) ~ 0.001 forecast. Path-H vs Path-C separation becomes statistically discriminable at LiteBIRD precision. Cross-reference S84 W4-41 LiteBIRD n_T STRUCTURAL-FLOOR (54-decade separation) for the n_T side of the joint discriminant.
3. n_T consistency: n_T = -r / 8 holds for BOTH pathways (slow-roll-equivalent at the substrate layer; verified at S84 W4-39 N_T-CMB-TRANSFER PASS).

**Reversibility scope under FROZEN-PREDICTION-DISCIPLINE-COMMIT**: r is reversibly editable ONLY after BOTH BK-Array 2026 AND LiteBIRD 2030 have published. A single-detector publication (e.g., BK-Array 2026 alone) does NOT trigger r re-pin; it triggers a BRANCH-ASSIGNMENT update on the 4-branch decision tree.

**What Both-Pathways IS** (per phononic framing): the dual registration is **substrate self-test** — the substrate emits one tensor-to-scalar ratio through two of its own internal projection channels (transverse fiber oscillation = B2 transverse modes; substrate compaction = B1 longitudinal acoustic modes through the G46 transfer). The two projections must agree to within their joint scheme-floor; if Path-H/Path-C separation exceeds the Level 2 floor, that excess IS a substrate observable, not a derivation flaw.

