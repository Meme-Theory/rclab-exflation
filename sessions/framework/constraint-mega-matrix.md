# Phonon-Exflation Constraint Mega-Matrix

**Generated**: 2026-03-02 (original S7-S31) | **Updated**: 2026-03-20 (S32-S51 appendix)
**Source**: Sessions 7-31Ba syntheses + Atlas D02/D05/D07 (sessions/framework/Atlas/)
**Purpose**: Comprehensive cross-reference of every gate, wall, closure, pass, and surviving channel
**NOTE**: For the definitive S1-S51 accounting, see the Project Atlas:
  - `sessions/framework/Atlas/atlas-02-mechanism-lifecycle.md` (58 closures, 6 eras)
  - `sessions/framework/Atlas/atlas-05-walls-doors-windows.md` (10 walls, 8 doors, 5 windows)
  - `sessions/framework/Atlas/atlas-07-permanent-results.md` (36 publishable + 33 machine-epsilon)

---

## I. STRUCTURAL WALLS (Inescapable by Any Static Mechanism)

These are proven mathematical facts about the geometry. No parameter choice, no coupling adjustment, no static potential evaluation can circumvent them.

| Wall | Statement | Source | Scope | What Escapes It |
|:-----|:---------|:-------|:------|:----------------|
| **W1: F/B Asymptotic Trap** | F/B ratio → 0.55 (UV), set by dim ratio 16/44. Weyl's law. tau-independent. | S18, S20b, S21a | Full spectrum (N → ∞) | Low-mode regime (N < 200): AC corrections O(N^{-1/8}) ~ 50-60%. BCS operates in AC regime. |
| **W2: Block-Diagonality** | D_K exactly block-diagonal in Peter-Weyl. ANY left-invariant metric on compact Lie group. | S22b (8.4e-15) | All sectors | Nothing — this is exact. Cross-sector coupling is zero. |
| **W3: Spectral Gap** | D_K has gap lambda_min > 0 at all tau. D_total gap min = 0.790 at tau=0.27. Never closes on Jensen. | S17a, S30Ab | Jensen curve + U(2)-invariant | Off-Jensen U(2)-breaking (Interior Mixing Theorem breaks when Killing decomposition changes). Full 5D landscape untested. |
| **W4: Static Monotonicity** | V_spec, V_FR, F_total, S_can, all positive spectral functionals: monotonically increasing from round metric on Jensen AND 3D U(2)-invariant surface. | S20-24 (Jensen), S30Ba (U(2)), S31Aa (3-form) | Jensen + U(2)-inv + 3-form sector | Dynamical (Kapitza time-averaging), non-perturbative (instantons), full 5D landscape. |
| **W5: Pfaffian Triviality** | sgn Pf(Xi · D_total) = +1 at ALL 75 tau in [0, 2.5], ALL 6 sectors. Interior Mixing Theorem: gap-edge perturbation suppressed 15-22x. | S30Ab | Jensen curve at N_max=2 | Off-Jensen (Killing decomposition change), higher N_max (dilutes further, makes it harder), full 5D landscape. |
| **W6: NCG-KK Irreconcilability** | Lambda_SA/M_KK = 10^6 at tau=0.21, 10^15 at tau=0.57. Irreconcilable at all tested tau for M_KK = 10^16 GeV. | S30Bb, S31Ba | All tested tau on Jensen | Abandon NCG identification (pure KK), threshold corrections, non-standard M_KK. |

---

## II. CLOSED MECHANISMS (22+ Total)

Mechanisms tested and proven unable to stabilize the modulus or produce the required dynamics.

### II.A Perturbative Potential (14 closures, Sessions 17-22)

| # | Mechanism | Why It Fails | Session |
|:--|:---------|:-------------|:--------|
| 1 | V_tree minimum | No tree-level minimum in Dirac spectrum functional | S17a SP-4 |
| 2 | 1-loop Coleman-Weinberg | F/B = 8.4:1 fermionic dominance, monotonic | S18 |
| 3 | Casimir scalar + vector | Monotonically increasing | S19d D-1 |
| 4 | Casimir with TT 2-tensors | Constant-ratio trap (W1) | S20b L-3/L-4 |
| 5 | Seeley-DeWitt a_2/a_4 balance | a_4/a_2 = 1000:1 at tau=0, R^2 always dominates | S20a SD-1 |
| 6 | Spectral back-reaction (scalar+vec) | Monotonic | S19d |
| 7 | Fermion condensate (perturbative) | Can't overcome gap | S19a S-4 |
| 8 | D_K Pfaffian Z_2 transition | No sign change on Jensen (W5) | S17c D-2, S30Ab |
| 9 | Single-field slow-roll | No minimum to slow-roll around | S19b R-1 |
| 10 | V''_total spinodal | V'' > 0 everywhere, no spinodal | S21a Landau |
| 11 | Connes 8-cutoff positive spectral sums | ALL monotonic, AM-GM inequality proof | S21a |
| 12 | S_signed gauge-threshold | Monotonic | S22a |
| 13 | Coupled delta_T crossing (PB-3) | D_K block-diagonal → coupled = block-diagonal exactly | S22b |
| 14 | Coupled V_IR minimum (PB-2) | Same cause as PB-3 | S22b |

### II.B Post-Perturbative Closures (Sessions 22-31)

| # | Mechanism | Why It Fails | Session |
|:--|:---------|:-------------|:--------|
| 15 | Higgs-sigma portal | Trap 3: e/(a·c) = 1/16 = 1/dim(spinor), exactly constant | S22c C-1 |
| 16 | Rolling modulus quintessence | Clock closure: dalpha/alpha = -3.08·tau_dot, 15,000x violation | S22d E-3 |
| 17 | Kosmann-BCS condensate (mu=0) | BdG M_max = 0.077-0.149, needs > 1.0. Factor 7-13x below. | S23a K-1e |
| 18 | Gap-edge self-coupling | V(gap,gap) = 0 EXACTLY (selection rule) | S23a |
| 19 | V_spec(tau; rho) monotone | Monotonically increasing ALL rho in [0.001, 0.5] | S24a V-1 |
| 20 | Eigenvalue ratio phi in singlet | Zero phi crossings in (0,0) singlet | S24a |
| 21 | V_total on 3D U(2)-inv surface | V_spec/F_BCS = 8000x at rho=0.01, no minimum | S30Ba B-30min |
| 22 | Freund-Rubin 3-form stabilization | |omega_3|^2 monotonically increasing, cooperates with V_spec, grows 6x faster | S31Aa BA-31-fr |

### II.C Retracted / Superseded

| Claim | Status | Session |
|:------|:-------|:--------|
| Session 21b "4-5x coupling" | RETRACTED — within-sector Kosmann norm, not inter-sector matrix elements | S22b |
| Tesla g·N(0) ~ 8-10 | RETRACTED — corrected to 3.24 | S22c |

---

## III. GATE VERDICTS (All Sessions, Organized by Outcome)

### III.A HARD CLOSES FIRED (Framework-Damaging)

| Gate | Verdict | Decisive Number | Session |
|:-----|:--------|:----------------|:--------|
| B-30a | Pfaffian trivial on Jensen | Pf = +1 at ALL 75 tau, ALL 6 sectors | S30Ab |
| B-30min | No V_total minimum on U(2)-inv surface | V_spec/F_BCS = 8000x | S30Ba |
| B-30nck | NCG-KK irreconcilable at tau~0.57 | Lambda_SA/M_KK ~ 10^15 | S30Bb |
| B-31nck | NCG-KK irreconcilable at tau~0.21 | Lambda_SA/M_KK ~ 10^6 | S31Ba |
| K-1e | BCS at mu=0 DECISIVE CLOSURE | M_max = 0.077-0.149, needs > 1.0 | S23a |
| V-1 | V_spec monotone | Increasing all rho | S24a |
| L-1 | Thermal spectral action | Monotonic | S19b |

### III.B GATES CLEARED (Framework Survived)

| Gate | Verdict | What Was Tested | Session |
|:-----|:--------|:---------------|:--------|
| B-30b | D_F construction succeeds | Anti-Hermitian, block-diagonal, D_F(0) = 6.89e-15 | S30Aa |
| B-30w | Weinberg angle accessible | sin^2 range [0.080, 0.510] covers [0.15, 0.30] | S30Ba |
| B-30phi | phi accessible | phi_30 range [1.288, 1.550], 263/441 in [1.45, 1.65] | S30Ba |
| OoO-3a | Chirality preserved | max ||{D_F, gamma_F}|| = 5.59e-14 | S30Aa |
| BA-31-or | Orientation insensitive | Max eigenvalue diff < 6.0e-14 (machine epsilon) | S31Aa |
| AC-1 | g1/g2 = 0.549 consistent | Known identity, does not close | S24a |
| T-1 | Fermionic gap weakening | PASS | S28/S29 |
| KC-1 | BCS injection rate | Gamma_inject = 29,643 at tau=0.40 | S29 |
| KC-2 | BCS scattering width | W/Gamma = 0.52 at tau=0.15 | S29 |
| KC-4 | Luttinger attractive | K < 1 in 21/24 combinations | S29 |
| KC-5 | BCS gap size | Delta/lambda_min = 0.84 (large) | S29 |
| B-1 | g1/g2 = e^{-2tau} structural | PASS then weakened | S17a |

### III.C GATES FAILED / DO NOT FIRE (Predictions Not Met)

| Gate | Verdict | What Failed | Session |
|:-----|:--------|:-----------|:--------|
| K-1 | DOES NOT FIRE (physical freq) | V_Kapitza monotonic at T3/T4. Modes 1.7x too stiff. | S31Ba |
| R-1 | FAIL | Neutrino R ~ 10^14, needs [17, 66] | S24a |
| V-3 | FAIL | No minimum anywhere | S24a |
| P-30pmns | FAIL | sin^2(theta_13) = 0.403 (18x too large) | S30Bb |
| P-30golden | FAIL | phi_30 max = 1.550, golden ratio 1.618 not accessible | S30Bb |
| P-30b | CANNOT FIRE | RGE-A FAIL at tau~0.57, P-30w FAIL at tau~0.21 | S30Bb |
| P-30a (compound) | CANNOT FIRE | phi + sin^2_B anti-correlated | S30Bb |
| P-30w | DOES NOT FIRE | No minimum to evaluate | S30Ba |
| RGE-A | FAIL/REFRAMED | sin^2(M_Z) in [0.134, 0.172] at tau~0.57; PASS at tau~0.21 under reframing | S30Bb |
| L-8 | FAIL | BCS condensation energy too small | S22d |
| C-3 | FAIL | Various coupling predictions | S28c |
| C-6 | FAIL | Order-one violation 4.000 | S28c |
| B-30r | DOES NOT FIRE | | S30 |
| B-30p | DOES NOT FIRE (prelim) | N_max=3 | S30 |

### III.D STRUCTURAL / DIAGNOSTIC PASSES

| Gate | Verdict | What Passed | Session |
|:-----|:--------|:-----------|:--------|
| **I-1** | **PASSES** (5/6 coupling ratios) | Gamma_inst/omega_tau > 3, peak 9.64 at tau=0.181 | S31Ba |
| KO-dim=6 | PROVEN | Parameter-free, machine epsilon | S7-S8 |
| CPT [J, D_K] = 0 | PROVEN | Hardwired, identically zero | S17a |
| Block-diagonal D_K | PROVEN | 8.4e-15 | S22b |
| 67/67 Baptista geometry | PROVEN | Machine epsilon | S17b |
| 147/147 Riemann tensor | PROVEN | Machine epsilon | S20a |
| phi_paasch = 1.531580 | PROVEN | At tau=0.15 (z=3.65) | S12, S22a |
| AZ class BDI, T^2=+1 | PROVEN | Correct symmetry class | S17c |
| Perturbative Exhaustion | PROVEN | H1-H5 verified | S22c |
| DOS-1 at Cand1 | PASS | 62 vs 46 (35% enhancement, Pomeranchuk confirmed) | S30Bb |
| P-30phi at Cand1 | PASS | phi_30 = 1.5206 in [1.52, 1.54] | S30Bb |

---

## IV. SURVIVING CHANNELS (What's Left)

### IV.A Dynamical Vacuum Routes

| Channel | Status | Key Evidence | Next Test | Expected Cost |
|:--------|:-------|:-------------|:----------|:-------------|
| **Instanton-driven Kapitza** | OPEN — I-1 PASSES, K-1 redirected | Gamma_inst/omega_tau = 5.98-9.64 at tau=0.181. S_inst < 0 on SU(3). Instanton frequency in soft-mode range (omega^2 < 5-8 where K-1 showed minima form). | Compute V_Kapitza with omega_eff = Gamma_inst (replace T3/T4 with instanton rate) | **~Zero** (existing data) |
| **Full 5D moduli landscape** | UNTESTED | T4 instability at boundary (eigenvalue -9.9 at tau=0.60, eps=+0.15). Interior Mixing Theorem breaks when Killing decomposition changes. 3 unconstrained directions with unknown eigenvalues. | Full 5D Hessian at tau~0.18 | ~1 hr |
| **Off-Jensen Pfaffian** | UNTESTED | W5 (Pfaffian trivial) proven only on Jensen. Interior Mixing suppression breaks under U(2)-breaking. Gap minimum 0.790 at tau=0.27 — closest approach. | D_F + Pfaffian at T4-unstable direction | ~2-5 hr |

### IV.B Structural Escapes (Parameter Adjustments)

| Channel | Status | What It Requires | Plausibility |
|:--------|:-------|:----------------|:-------------|
| **Threshold corrections for NCG-KK** | THEORETICAL | Modify RGE running by 6 orders at M_KK via heavy KK mode contributions | Unprecedented in standard GUT. Theoretically possible but never demonstrated. |
| **Pure KK interpretation** | AVAILABLE | Abandon NCG spectral action identification. Use D_K eigenvalues + KK geometry only. Treat spectral action as effective potential. | Removes Wall 6 entirely. Sacrifices NCG classification theorem. |
| **Finite-density spectral action (P2b)** | THEORETICAL | mu ≠ 0 in spectral action. New NCG theory required. | No existing formalism. BF 5-15 unchanged. EV ~ 0.5. |
| **Non-standard M_KK** | THEORETICAL | M_KK ≠ 10^16 GeV. Would fix NCG-KK but conflicts with GUT phenomenology. | Disfavored by proton lifetime constraints. |

---

## V. CONVERGENCE MAP: The tau = 0.15-0.21 Window

Three independent constraints converge on the same narrow tau window. This is the single most structurally suggestive feature of 31 sessions.

| Constraint | Source | tau Value | Independent? |
|:-----------|:-------|:----------|:-------------|
| phi_30 = 1.532 (Paasch target) | S12, S30Bb | tau = 0.15-0.20 | YES (eigenvalue ratio) |
| RGE-evolved sin^2(M_Z) = 0.231 | S30Bb (einstein) | tau ~ 0.21 | YES (gauge coupling running) |
| Peak instanton rate | S31Ba I-1 | tau = 0.181 | YES (curvature-dependent tunneling) |
| Gradient-balance point (V_spec vs F_BCS) | S30Ba | tau = 0.180 | Partially (derived from V_spec) |
| Instanton action minimum | S22c Part 7 | tau ~ 0.10-0.31 | YES (topology of instanton moduli) |

**Physical picture**: The framework's *kinematics* work at tau ~ 0.15-0.21. Every coupling, every mass ratio, every observable points here. The sole missing piece is *dynamics* — a mechanism that stabilizes the modulus at this tau.

---

## VI. THE GAP ANALYSIS: Where New Physics Lives

### VI.1 What Has NOT Been Tested

| Test | Why It Matters | Cost | Priority |
|:-----|:-------------|:-----|:---------|
| **Instanton-driven V_Kapitza** | I-1 shows instanton frequency in soft-mode range where K-1 demonstrated minima form. This is THE combination test. | ~Zero (existing data) | **CRITICAL** |
| **Full 5D Hessian at tau~0.18** | 3 directions with unknown eigenvalues. If ANY has omega^2 < 5, Hessian-Kapitza fires. | ~1 hr | HIGH |
| **Off-Jensen Dirac spectrum at T4-unstable point** | Interior Mixing Theorem breaks, gap could close, Pfaffian could flip. Entirely uncharted. | ~2-5 hr | HIGH |
| **AZ class at off-Jensen points** | BDI proven only on Jensen. Off-Jensen classification unknown. Required before any off-Jensen Pfaffian. | ~1 hr | MEDIUM |
| **Instanton gas on 2D U(2)-inv grid** | Maps Gamma_inst across 2D surface, finds if soft-mode range extends off-Jensen. | ~30 min | MEDIUM |
| **Proper neutrino sector at tau~0.21** | R-1 FAIL used full-spectrum H_eff. Sector-restricted computation untried. | ~30 min | LOW |
| **Eigenvector-dependent orientation test** | Pfaffian and Kosmann elements under reversed orientation. Eigenvalues safe, eigenvectors unknown. | ~2 hr | LOW |
| **Off-Jensen 3-form norm** | BA-31-fr closed FR on Jensen. U(2)-invariant and T4-unstable directions untested. | ~30 min | LOW |

### VI.2 Logical Implications Tree

```
Current state: 22 closures, 6 walls, all static mechanisms exhausted
                |
                v
    ┌──────────────────────────────────────┐
    │ Does instanton-driven V_Kapitza      │
    │ have an interior minimum?            │
    │ (omega_eff = Gamma_inst)             │
    └─────────┬──────────────┬─────────────┘
              │YES           │NO
              v              v
    ┌─────────────┐  ┌─────────────────────┐
    │ FIRST       │  │ Does full 5D Hessian │
    │ POSITIVE    │  │ have omega^2 < 5?    │
    │ SIGNAL      │  └──────┬─────────┬─────┘
    │             │         │YES      │NO
    │ tau_* near  │         v         v
    │ 0.15-0.21?  │  ┌──────────┐  ┌───────────────┐
    │ → MAJOR     │  │ Hessian-  │  │ OFF-JENSEN    │
    │ probability │  │ Kapitza   │  │ landscape:    │
    │ revision    │  │ fires     │  │ full 5D Dirac │
    │ upward      │  │ → test    │  │ + Pfaffian    │
    └─────────────┘  │ at that   │  │ required      │
                     │ tau       │  └───────────────┘
                     └──────────┘
```

### VI.3 Physics Hunches — Where Surprises Could Hide

Based on 31 sessions of constraint analysis, here are the directions most likely to yield genuinely new physics:

**1. Instanton-Condensate Duality (Highest Ceiling)**
Tesla's identification: instantons ARE nonlinear phonons under KK reduction. The wall between "perturbative oscillations" and "instanton tunneling" is false — both are excitations at different amplitudes. S_inst < 0 on positively-curved SU(3) means instantons are ENHANCED, not suppressed. This is the structural inversion that no flat-space intuition would predict. The instanton gas at tau ~ 0.18 is dense, not dilute.

**2. The U(2)-Breaking Frontier (Widest Unexplored Territory)**
T4 eigenvalue = -9.9 at the boundary means the U(2)-invariant surface is itself unstable. The landscape FUNNELS toward full 5D. The Interior Mixing Theorem's suppression — which protects the gap and trivializes the Pfaffian — breaks when the Killing/non-Killing decomposition changes. This is the one place where W3 and W5 could simultaneously fail.

**3. Effective Frequency from Multi-Mode Coupling**
K-1 tested transverse oscillation in a SINGLE mode (T3 or T4). Real dynamics couples ALL transverse modes. The effective frequency of the coupled system could be softer than any individual mode. This is standard in nonlinear dynamics (frequency pulling, parametric resonance). The threshold is omega^2 ~ 5: the individual modes are at 8.3 and 9.9. Two modes coupling could produce an effective omega^2 ~ 4-6 via sum/difference frequencies.

**4. The CC Connection (Deepest Question)**
BA-31-cc found a_0/a_2 = 0.494 (O(1), no suppression). But the Kapitza mechanism, if it works, produces a TIME-AVERAGED vacuum energy, not a static one. The time-averaged CC from Kapitza oscillation is V_Kapitza(tau_*) — which could be exponentially smaller than V_spec at any fixed tau. The Kapitza mechanism doesn't just stabilize the modulus — it could be the CC suppression mechanism itself.

**5. The BCS-at-Finite-Temperature Regime**
All BCS computations assumed T=0 (ground state). At finite temperature, the spectral gap is thermally populated. K-1e (BCS closure) used mu=0. At T ~ lambda_min (the gap), the occupation changes qualitatively. The partition function F(tau; beta) at beta ~ 1/lambda_min has never been computed.

---

## VII. PROBABILITY STATE

| Session | Panel | Sagan | Key Event |
|:--------|:------|:------|:----------|
| Pre-22 | 40% | — | Before traps discovered |
| 22a | 46% | — | Pomeranchuk pass |
| 22b | 38% | — | Block-diagonal theorem |
| 22c | 44% | — | Perturbative Exhaustion |
| 22d | 40% | 27% | Clock closure, DESI closed |
| 23a | 6-10% | 4-8% | **Venus: K-1e fires** |
| 24a | 5-7% | 2-3% | V-1 fires |
| 24b | 5% (4-7%) | 3% (2-4%) | Combined BF = 0.31 |
| 28 | 7-10% | 4-7% | KC-1 through KC-5 PASS (BCS chain) |
| 30 | ~5% | ~3% | B-30a, B-30min, B-30nck fire. 0 positive signals. |
| 31Aa | ~4-5% | ~2-3% | BA-31-fr closes FR. B-31nck FAIL. 0 positive. |
| 31Ba | **TBD** | **TBD** | K-1 DOES NOT FIRE (physical). **I-1 PASSES** (5/6). |

**Net I-1 PASS effect**: First structural positive signal in a pre-registered gate since KC-1-5 (S29). The instanton-Kapitza mechanism is mathematically viable. No probability weight until the instanton-driven V_Kapitza is computed.

---

## VIII. CLOSED vs OPEN SCORECARD

| Category | Count | Examples |
|:---------|:------|:--------|
| **Structural walls** | 6 | W1-W6 |
| **Closed mechanisms** | 22+ | All perturbative, BCS at mu=0, FR, rolling quintessence |
| **Hard closes fired** | 7 | B-30a, B-30min, B-30nck, B-31nck, K-1e, V-1, L-1 |
| **Gates PASSED** | ~15 | KO-dim, CPT, block-diag, phi, BCS chain (KC-1-5), D_F construction, I-1 |
| **Gates FAILED / NOT FIRE** | ~14 | K-1, R-1, V-3, P-30pmns, P-30golden, etc. |
| **Surviving dynamic channels** | 3 | Instanton-Kapitza, full 5D landscape, off-Jensen Pfaffian |
| **Surviving structural escapes** | 4 | Threshold corrections, pure KK, P2b, non-standard M_KK |
| **UNCOMPUTED decisive tests** | 3 | Instanton-driven V_Kapitza, 5D Hessian, off-Jensen D_F |

**Closure-to-pass ratio**: ~22:15 (1.5:1). When including hard closes vs structural passes: 7:15 for hard closes, but closed mechanisms dominate 22:15 overall.

---

*Matrix assembled from: session-30-master-synthesis.md, session-31Aa-synthesis.md, session-31Ba-synthesis.md, all gate verdict files (s24a through s31Ba), MEMORY.md framework status. All numbers from source computations, not re-derived. This document is a reference matrix, not a synthesis — it does not adjudicate or interpret, only cross-references.*

---

## VII. SESSIONS 32-51 UPDATE (From Project Atlas)

**Source**: `sessions/framework/Atlas/atlas-02-mechanism-lifecycle.md`, `atlas-05-walls-doors-windows.md`

### VII.A New Walls (S37-S51)

| Wall | Statement | Source | Closures |
|:-----|:---------|:-------|:---------|
| **W7: alpha_s = n_s²-1 Structural Theorem** | For ANY equilibrium propagator with K² dispersion on a compact Josephson lattice with broken U(1). 5 independent proofs. | S50 (W1-A, W1-F, W1-H, W2-A, W2-B) | 7+ |
| **W8: Anderson-Higgs Impossibility** | K_7 is a Kosmann derivative (diffeomorphism), not an inner automorphism (gauge). [iK_7, D_K] = 0 at all orders. Categorical. | S51 W1-C | 1 (permanent) |
| **W9: Convex Combination Theorem** | n_s of any additive correlator mixture bounded by individual n_s values. At K_pivot = 2.0: max n_s = 0.15 << 0.965. | S51 W2-A | 1 |
| **W10: Zero-Mode Protection on T²** | Goldstone is KK n=0 mode, wavefunction constant on T². <V> = 0 exactly. Extends to full Born series Re(Sigma). | S50 W1-H, S51 W1-B | 2 |

### VII.B Additional Closures (S32-S51: 36 new, total 58)

| Era | Sessions | Count | Key Closures |
|:----|:---------|:------|:-------------|
| BCS Chain + Instanton | S35-S38 | 7 | Cutoff SA (structural monotonicity), one-loop RPA self-trapping (wrong sign), (B1,B3,G1) PMNS triad (algebraic), CC-through-instanton (76x margin) |
| Transit + Cosmology | S39-S46 | 15 | Friedmann-BCS (38,600x), self-tuning runaway, Zak phase retracted, acoustic horizon retracted |
| Fabric + n_s | S46-S49 | 7 | O-Z Friedmann mass (115 OOM), Bragg gap (KK scale), Leggett transit (destroyed post-transit) |
| O-Z Investigation | S50-S51 | 20 | 3-pole propagator, Bogoliubov imprint, running mass, eikonal, anomalous dispersion, fabric RPA, spatial KZ, w_a (4 mechanisms), Anderson-Higgs, polariton, local resonance, critical scaling |

### VII.C Updated Surviving Channels (Post-S51)

The S7-S31 surviving channels (Section IV) are now resolved:

| Channel (S31) | S51 Status |
|:--------------|:-----------|
| Instanton-driven Kapitza | CLOSED (S37 CUTOFF-SA-37: structural monotonicity) |
| Full 5D moduli landscape | OPEN (never computed, atlas D08 structural question Q9) |
| Off-Jensen Pfaffian | OPEN (atlas D08, S52 W3-C) |

**New surviving channels (S51)**:
1. **SA-Goldstone mixing at K < K*** — n_s = 0.965 achievable. CONDITIONAL on K_pivot mapping (EFOLD-MAPPING-52).
2. **12D submersion decomposition** — THE missing computation. 23/23 atlas reviewers converge.
3. **Q-theory CC crossing at fabric level** — Conditional on N_pair >= 2 (S52 W1-I).

### VII.D Current Decision Tree (replaces VI.2)

```
S51 state: 58 closures, 10 walls, 3 conditional surviving channels
              |
              v
    EFOLD-MAPPING-52 (12D submersion decomposition)
              |
       ┌──────┴──────┐
       |PASS         |FAIL
       v              v
  K_pivot < K*     K_pivot > K*
  SA mixing viable  Cosmology closed
  → n_s, sigma_8    → Publish math
  → Test vs CMB-S4  → 36 theorems
```

