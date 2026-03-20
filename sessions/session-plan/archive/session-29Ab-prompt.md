# Session 29Ab: Backreaction + Free Energy Comparison

**Date**: 2026-02-28
**Author**: Hawking (hawking-theorist), dissected by team-lead
**Depends on**: Session 29Aa (KC-3 PASS required, entropy balance PASS required, derived drive rate from 29a-2)
**Prerequisite**: 29Aa must complete with KC-3 PASS AND entropy PASS. If either fires a hard close (K-29a or K-29b), this sub-session does not run.
**Input data**:
- `tier0-computation/s29a_derived_drive_rate.npz` (E_total range, d(tau)/dt profile) — FROM 29Aa
- `tier0-computation/s29a_inter_sector_coupling.npz` (J_perp / Delta_BCS) — FROM 29Aa
- `tier0-computation/s28a_spectral_action_comparison.npz` (I_E(tau) for D_K and D_can, V_eff)
- `tier0-computation/s28b_self_consistent_tau_T.npz` (F_total(tau, mu) landscape)
- `tier0-computation/s28b_hessian.npz` (Hessian eigenvalues at minima)
- `tier0-computation/s28c_bcs_van_hove.npz` (Van Hove BCS gap Delta(tau))

## Motivation

Session 29Aa delivered the KC-3 verdict and entropy balance. If both PASSED, the Constraint Chain is complete (KC-1 through KC-5 all PASS) and the tau evolution is thermodynamically permitted. Session 29Ab now asks: **what does the tau(t) trajectory actually look like?**

This sub-session contains the FULL backreaction computation — the coupled modulus equation of motion with Friedmann constraint. This is the universal priority identified by both Session 28 team syntheses. Every observational prediction in 29Ac depends on the outputs of this computation.

The three computations here answer three questions:
1. **29b-1**: Does BCS condensation become energetically favorable? (Free energy crossing)
2. **29b-2**: What is the cosmic time trajectory tau(t)? (Modulus EOM)
3. **29b-3**: Does the one-loop correction destroy the mean-field BCS minimum? (Gaussian fluctuations)

---

# 0. OPERATIONAL RULES

## COMPUTATION DISCIPLINE

Every result classified against its pre-registered gate BEFORE any interpretation. Report the number first. Classify second. Interpret third.

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s29b_`

## 29Aa GATE CHECK (MANDATORY FIRST ACTION)

Before any computation, read `tier0-computation/s29a_gate_verdicts.txt` and verify:
1. KC-3 verdict = PASS (K-29a did not fire)
2. Entropy balance = PASS (K-29b did not fire)

If EITHER is FAIL or CLOSED, **this sub-session does not proceed**. Report the closure and skip to Session 29A final synthesis.

Also load the drive rate profile from `s29a_derived_drive_rate.npz` — the E_total range that satisfies KC-3 is the input for 29b-2.

## COMPLETION SIGNAL

Session ends ONLY when user approves shutdown explicitly. Idle agents are not finished agents.

---

# I. REQUIRED READING

## ALL agents (MANDATORY):

1. **Session 29Aa synthesis**: `sessions/session-29/session-29Aa-synthesis.md` — KC-3 verdict, entropy balance, drive rate, J_perp results.
2. **Session 28 fusion synthesis**: `sessions/session-28/session-28-fusion-synthesis.md` — Section III (Constraint Chain), Section V (modulus-space narrative).
3. **Session 28 team synthesis A**: `sessions/session-28/session-28-team-synthesis-a.md` — Backreaction (U-5), free energy comparison (CP-1), Gaussian correction (T-2).
4. **Session 28 team synthesis B**: `sessions/session-28/session-28-team-synthesis-b.md` — Free energy comparison (CP-1), no-boundary initial conditions (U-4).
5. **MathVariables**: `sessions/framework/MathVariables.md` — Section 4 (BCS variables), Section 2 (Dirac operator).
6. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## Agent-specific required reading:

| Agent | Additional Reading |
|:------|:-------------------|
| phonon-exflation-sim | `tier0-computation/s28b_self_consistent_tau_T.py` (F_total infrastructure), `tier0-computation/s28c_bcs_van_hove.py` (BCS gap solver) |
| einstein-theorist | `researchers/Einstein/index.md` — Friedmann equation context. Baptista Paper 15 eq 1.2 (KK ansatz), G_{tau,tau} = 5 derivation |
| landau-condensed-matter-theorist | `researchers/Landau/index.md` — BCS fluctuation theory, Ginzburg criterion |
| coordinator | This prompt Section IV (pre-registered Constraint Gates). Memorize ALL thresholds before first computation completes |

---

# II. COMPUTATIONS

## 29b-1: Free Energy Comparison at First-Order Transition (CP-1) [CRITICAL]

**What**: The first-order BCS transition (L-9 PASS) simplifies the backreaction to a free energy comparison (Synthesis B, CP-1). Compare:

$$F_{condensed}(\tau = 0.35, \mu = \mu_{eff}) \quad \text{vs.} \quad F_{normal}(\tau, \mu = 0) \tag{29b.1}$$

The transition occurs when F_condensed < F_normal. The critical tau at which this crossing occurs, combined with the drive rate from 29a-2, gives the cosmic time t_BCS of the transition.

**Key question**: Does the first-order transition occur BEFORE the modulus reaches tau = 0.35 from the DNP-unstable initial state at tau = 0? If the modulus is driven past tau = 0.35 without the transition occurring (because KC-3 has not filled the gap yet), the BCS mechanism fails.

**Input**: `s28b_self_consistent_tau_T.npz` (F_total landscape), `s28a_spectral_action_comparison.npz` (F_normal = spectral action).

**Script**: `s29b_free_energy_comparison.py`

**Method**:
1. Load F_total(tau, mu) landscape from Session 28b data.
2. Extract F_condensed(tau) = F_total(tau, mu_eff) at the self-consistent mu for each tau.
3. Extract F_normal(tau) = spectral action (no condensation, mu = 0).
4. Find tau_cross where F_condensed(tau_cross) = F_normal(tau_cross).
5. Plot both curves with crossing point marked.
6. Check: is tau_cross in [0.20, 0.50]?

**Output**: `s29b_free_energy_comparison.npz`, `s29b_free_energy_comparison.png`

**Computational cost**: Interpolation of existing data. < 1 min.

**Agent**: phonon-exflation-sim or einstein-theorist

---

## 29b-2: Modulus Equation of Motion (Synthesis A U-5, Synthesis B Priority 3) [CRITICAL]

**What**: Solve the coupled modulus equation of motion:

$$\ddot{\tau} + 3H\dot{\tau} + \frac{1}{G_{\tau\tau}} \frac{dV_{eff}}{d\tau} = 0 \tag{29b.2}$$

with the Friedmann constraint:

$$H^2 = \frac{1}{3M_P^2}\left[\frac{1}{2}G_{\tau\tau}\dot{\tau}^2 + V_{eff}(\tau)\right] \tag{29b.3}$$

This is the FULL backreaction computation. V_eff(tau) includes the bare spectral action (monotonically decreasing, from C-1/L-1) and the BCS condensation energy (from S-3 interior minima). G_{tau,tau} = 5 (Baptista Paper 15).

The system is a two-variable ODE (tau(t), H(t)) with one free parameter M_KK (the compactification scale). Initial conditions from the no-boundary proposal + WCH (Synthesis A, U-4): tau(0) = 0, d(tau)/dt(0) = epsilon (small perturbation from DNP instability).

**Outputs** (ALL required for 29Ac):
1. **tau(t) trajectory** — the cosmic time evolution of the modulus
2. **t_BCS** — the cosmic time of the BCS transition (from 29b-1 free energy crossing)
3. **H(t_BCS)** — the Hubble rate at the transition
4. **d(tau)/dt at all t** — confirms whether KC-3 drive rate requirement is met dynamically

**Input**: `s28a_spectral_action_comparison.npz`, `s28b_self_consistent_tau_T.npz`, `s29a_derived_drive_rate.npz` (E_total range from 29Aa). M_KK as parameter.

**Script**: `s29b_modulus_eom.py`

**Method**:
1. Construct V_eff(tau) by interpolating spectral action + BCS condensation energy data.
2. Set up the 2nd-order ODE as a system of two 1st-order ODEs:
   - y1 = tau, y2 = d(tau)/dt
   - dy1/dt = y2
   - dy2/dt = -3*H*y2 - (1/G_{tau,tau}) * dV_eff/d(tau)
   - H = sqrt((1/3*M_P^2) * (0.5*G_{tau,tau}*y2^2 + V_eff(y1)))
3. Integrate from t=0 to t=t_max for M_KK in {10^14, 10^15, 10^16, 10^17, 10^18} GeV.
4. For each M_KK: record tau(t), t_BCS, H(t_BCS), d(tau)/dt(t_BCS).
5. Plot tau(t) trajectory for each M_KK. Mark t_BCS on each curve.

**Output**: `s29b_modulus_eom.npz`, `s29b_modulus_eom.png`

**Computational cost**: ODE integration. < 5 min.

**Agent**: phonon-exflation-sim for numerics, einstein-theorist for the Friedmann equation setup.

---

## 29b-3: Gaussian Fluctuation Correction (Synthesis A Priority 4, T-2) [MEDIUM]

**What**: Compute the one-loop determinant det(M[Delta]) around the BCS saddle point. The Ginzburg criterion for N ~ 16 modes in the singlet sector gives delta T_c / T_c ~ O(1) (Synthesis A, T-2). The BCS coherence length xi ~ v_F/Delta ~ 1.25, compared to the injectivity radius r_inj ~ 2.44, gives xi/r_inj ~ 0.51 (Synthesis A, X-2) — Cooper pairs span half the internal manifold, making finite-size corrections order unity.

Diagonalize the 2N x 2N BdG Hamiltonian at the saddle point, compute det(M) = product of eigenvalues, and evaluate the Gaussian correction to the free energy:

$$F_{1-loop} = F_{MF} + \frac{1}{2}\sum_n \ln(\omega_n^2 + E_n^2) \tag{29b.4}$$

where E_n are the BdG quasiparticle energies and omega_n are Matsubara frequencies.

**Input**: `s28c_bcs_van_hove.npz`, `s28b_hessian.npz`.

**Script**: `s29b_gaussian_correction.py`

**Method**:
1. Load BdG Hamiltonian from van Hove BCS data at the saddle point (tau = 0.35, mu = mu_eff).
2. Diagonalize the 2N x 2N BdG matrix (N ~ 16 for singlet sector → 32x32 matrix).
3. Extract quasiparticle energies E_n.
4. Evaluate F_1-loop at T = 0 (zero Matsubara frequency contribution only).
5. Compare: is |F_1-loop - F_MF| / |F_MF| < 1? (Ginzburg criterion)
6. Check: does F_1-loop change the sign of F_condensed - F_normal?

**Output**: `s29b_gaussian_correction.npz`, `s29b_gaussian_correction.txt`

**Computational cost**: BdG diagonalization (~32x32 matrix), Matsubara sum. < 5 min.

**Note**: This computation can run in parallel with 29b-1 and 29b-2 — it is independent of the backreaction trajectory.

**Agent**: landau-condensed-matter-theorist (BCS fluctuation expertise)

---

# III. EXECUTION ORDER

```
29b-3 (Gaussian correction) ──── independent, run immediately
                                  (does not depend on 29b-1 or 29b-2)

29b-1 (free energy comparison) ──┐
                                  ├── 29b-2 uses tau_cross from 29b-1
29b-2 (modulus EOM)           ────┘   but can start setup in parallel

Outputs of 29b-1 + 29b-2:
  → t_BCS (cosmic time of BCS transition)
  → H(t_BCS) (Hubble rate at transition)
  → tau(t) trajectory
  → These feed ALL of 29Ac
```

**Critical path**: 29b-1 → 29b-2 → 29Ac. The free energy crossing point tau_cross is needed by 29b-2 to identify t_BCS on the tau(t) trajectory.

---

# IV. PRE-REGISTERED CONSTRAINT GATES

## Hard Closes (any one terminates Session 29A)

| ID | Condition | Computation | Consequence |
|:---|:----------|:------------|:------------|
| K-29c | F_condensed > F_normal at ALL tau in [0, 2.0] | 29b-1 | BCS condensation never energetically favored. Mechanism closed by thermodynamics. |
| K-29d | One-loop correction reverses sign of F_condensed - F_normal | 29b-3 | Mean-field BCS is artifact. Gap is pseudogap. |

## Soft Gates

| ID | Condition | Computation | Consequence |
|:---|:----------|:------------|:------------|
| G-29c | t_BCS from tau(t) trajectory requires M_KK > 10^{18} GeV or t_BCS > 13.8 Gyr | 29b-2 | Transition time requires extreme compactification scale or exceeds universe age. Fine-tuning concern. |

## Positive Signals

| ID | Condition | Computation | Consequence |
|:---|:----------|:------------|:------------|
| P-29e | F_condensed < F_normal crossing at tau_cross in [0.20, 0.50] | 29b-1 | BCS energetically favored in the physical window. |
| P-29f | tau(t) trajectory reaches tau_cross in t_BCS ~ 10^{-36} to 10^{-10} s for natural M_KK | 29b-2 | GUT/EW-scale transition with natural parameters. |
| P-29g | |F_1-loop - F_MF| / |F_MF| < 0.5 | 29b-3 | Mean-field BCS is quantitatively reliable. |

---

# V. SESSION VERDICT CRITERIA

Results from 29Ab that feed into 29Ac:

| Result | Feeds Into | Required |
|:-------|:-----------|:---------|
| tau_cross (free energy crossing point) | 29Ac-1 (T_GH), 29Ac-2 (k_transition) | YES |
| tau(t) trajectory | 29Ac-2 (k_transition), 29Ac-3 (CDL), 29Ac-4 (GW) | YES |
| t_BCS, H(t_BCS) | 29Ac-2 (k_transition), 29Ac-4 (GW spectrum) | YES |
| F_1-loop assessment | 29Ac interpretation (reliability of mean-field) | Advisory |

**29Ab is successful if it produces**:
1. A definitive free energy crossing verdict (crossing exists or does not)
2. A tau(t) trajectory with t_BCS and H(t_BCS) for a range of M_KK
3. A Gaussian correction assessment (mean-field reliable or artifact)

**Early termination conditions**:
- K-29c fires (no free energy crossing) → Backreaction computation is moot. Report closure, skip 29Ac.
- K-29d fires (one-loop destroys minimum) → Mean-field BCS is artifact. Report closure, skip 29Ac.

---

# VI. AGENT ASSIGNMENTS

| Agent | Role | Computations |
|:------|:-----|:-------------|
| **phonon-exflation-sim** | Primary computation | 29b-1, 29b-2 |
| **einstein-theorist** | Friedmann equation setup | 29b-2 (ODE formulation, M_KK interpretation) |
| **landau-condensed-matter-theorist** | BCS fluctuations | 29b-3 (Gaussian correction, Ginzburg criterion) |
| **coordinator** | Gate classification + documentation | Classify EACH result in real time. Assemble gate verdicts. |

**Recommended team size**: 4 agents (phonon-sim + einstein + landau + coordinator). Minimum viable: phonon-sim + coordinator.

---

# VII. OUTPUT FILES

| File | Computation | Producer |
|:-----|:-----------|:---------|
| `tier0-computation/s29b_free_energy_comparison.py` | 29b-1 | phonon-sim |
| `tier0-computation/s29b_free_energy_comparison.npz` | 29b-1 data | phonon-sim |
| `tier0-computation/s29b_free_energy_comparison.png` | 29b-1 plot | phonon-sim |
| `tier0-computation/s29b_modulus_eom.py` | 29b-2 | phonon-sim |
| `tier0-computation/s29b_modulus_eom.npz` | 29b-2 data | phonon-sim |
| `tier0-computation/s29b_modulus_eom.png` | 29b-2 plot | phonon-sim |
| `tier0-computation/s29b_gaussian_correction.py` | 29b-3 | landau |
| `tier0-computation/s29b_gaussian_correction.npz` | 29b-3 data | landau |
| `tier0-computation/s29b_gaussian_correction.txt` | 29b-3 verdict | landau |
| `tier0-computation/s29b_gate_verdicts.txt` | All gate verdicts | coordinator |
| `sessions/session-29/session-29Ab-synthesis.md` | Synthesis | coordinator |

---

# VIII. CONDITIONAL PROBABILITY (POST-29Ab)

Assumes 29Aa delivered KC-3 PASS + entropy PASS (probability updated to 10-14% panel entering this phase).

| Scenario | Free Energy | One-Loop | Posterior (panel) | Path Forward |
|:---------|:------------|:---------|:-----------------|:-------------|
| **Full PASS** (crossing + survives 1-loop) | crossing exists | survives | **15-22%** | Proceed to 29Ac |
| **Crossing only** (1-loop marginal) | crossing exists | marginal (ratio > 0.5) | 12-16% | Proceed to 29Ac with caveats |
| **No crossing** (K-29c fires) | no crossing | -- | 3-5% | Session 29A terminates |
| **1-loop destroys** (K-29d fires) | crossing exists | reverses sign | 3-5% | Session 29A terminates |

The dramatic upward pathway through 29Ac requires: crossing exists + 1-loop survives + natural M_KK.

---

*Session 29Ab prompt dissected from Session 29A plan (Hawking, 2026-02-28). This sub-session contains the full backreaction computation — the single universal priority from both Session 28 syntheses. Three computations, total runtime < 15 min. All outputs feed directly into 29Ac observational predictions. If free energy crossing does not exist or one-loop destroys it, Session 29A terminates early.*
