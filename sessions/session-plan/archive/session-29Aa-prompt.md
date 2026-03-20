# Session 29Aa: KC-3 Closure + Entropy Balance

**Date**: 2026-02-28
**Author**: Hawking (hawking-theorist), dissected by team-lead
**Depends on**: Session 28 (all sub-sessions: 28a KC-1 PASS, 28b self-consistent tau-T, 28c phonon T-matrix + van Hove BCS + Luttinger + steady-state mu)
**Input data**:
- `tier0-computation/s28a_bogoliubov_coefficients.npz` (B_k(tau) for all sectors)
- `tier0-computation/s28c_phonon_tmatrix.npz` (T-matrix at tau = 0.15, 0.35)
- `tier0-computation/s28c_bcs_van_hove.npz` (Van Hove BCS gap Delta(tau))
- `tier0-computation/s28c_luttinger.npz` (Luttinger K(tau) per sector)
- `tier0-computation/s28c_steady_state_mu.npz` (n_gap(tau, d(tau)/dt))
- `tier0-computation/s28a_spectral_action_comparison.npz` (I_E(tau) for D_K and D_can)
- `tier0-computation/s28b_self_consistent_tau_T.npz` (F_total(tau, mu) landscape)
- `tier0-computation/s23a_eigenvectors_extended.npz` (D_K eigenvectors for all sectors)
- Session 25 spectral entropy data (`s25_hawking_computations.py` outputs)

## Motivation

Session 28 produced the first mechanism to survive computation: the Constraint Chain (KC-1/2/4/5 PASS, KC-3 CONDITIONAL). Two independent team syntheses converged unanimously on the same priorities: **KC-3 closure + backreaction self-consistency**. Session 29Aa tackles the first half: does KC-3 PASS or FAIL, and is the tau evolution thermodynamically permitted?

The guiding question: **is the BCS phase transition at tau = 0.35 a self-consistent cosmological event?**

### The CMB-as-Horizon Provocation (Background Context)

Session 29A is organized around Hawking's evaluation of three structural claims:

- **Claim A** (partial): The CMB surface of last scattering is the 4D image of the internal BCS phase boundary. The internal Gibbons-Hawking temperature T_GH^{internal}(tau) = e^{-2tau}/pi at the transition, redshifted to today, should equal 2.725 K. Testable once the tau-to-cosmic-time mapping is computed (Session 29Ab-29Ac).

- **Claim B** (weakest): The Big Bang singularity IS the BCS phase transition — a spacelike surface from which all geodesics emerge. Requires spatially homogeneous tau(t) or rapid bubble percolation (beta/H >> 1). Natural if tau is a function of cosmic time only (FRW background).

- **Claim C** (strongest): The mono-decreasing Euclidean action I_E(tau) is structurally identical to black hole evaporation with negative specific heat (Gibbons-Hawking 1977). The BCS first-order transition IS the Hawking-Page transition of the internal geometry (Synthesis B C-7: cascade of transitions across sectors).

**Where the isomorphism breaks**: The CMB is a phase boundary, not a causal horizon. Information beyond it is accessible in principle. Einstein's correction (Synthesis B C-6): no horizon on SU(3), so the GSL does not apply in strict form — use the ordinary second law instead.

**Four testable consequences** (all require backreaction from 29Ab):
- T-1: T_GH^{internal}(tau_transition) redshifted to today = 2.725 K
- T-2: BCS transition imprints a feature in P(k) at k_transition
- T-3: Spectral index break across the transition
- T-4: Multi-peaked stochastic GW background from L-9 cubic invariant

All four require the backreaction computation (29Ab). This sub-session produces the KC-3 verdict and entropy balance that GATE whether 29Ab proceeds.

---

# 0. OPERATIONAL RULES

## COMPUTATION DISCIPLINE

Every result classified against its pre-registered gate BEFORE any interpretation. Report the number first. Classify second. Interpret third.

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s29a_`

## PRE-SESSION GATE

Before any computation proceeds, verify that all Session 28 data files listed above are intact and accessible. Load each .npz, verify key names, print array shapes. If ANY file is missing or corrupted, STOP and report.

## COMPLETION SIGNAL

Session ends ONLY when user approves shutdown explicitly. Idle agents are not finished agents.

---

# I. REQUIRED READING

## ALL agents (MANDATORY):

1. **Session 28 fusion synthesis**: `sessions/session-28/session-28-fusion-synthesis.md` — Section III (Constraint Chain status), Section IV (cross-synthesis discoveries XS-1 through XS-8), Section VIII (unified priorities).
2. **Session 28 team synthesis A**: `sessions/session-28/session-28-team-synthesis-a.md` — Sections on KC-3, T-matrix extension (U-2, X-1), drive rate (C-3), entropy balance (H-13).
3. **Session 28 team synthesis B**: `sessions/session-28/session-28-team-synthesis-b.md` — Sections on free energy comparison (CP-1), Mermin-Wagner (C-4), entropy balance (CP-4).
4. **Session 28c results**: `sessions/session-28/session-28c-results.md` — T-matrix data, van Hove BCS, Luttinger K, steady-state mu.
5. **MathVariables**: `sessions/framework/MathVariables.md` — Sections 2.1 (D_can vs D_K), 4 (BCS variables).
6. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## Agent-specific required reading:

| Agent | Additional Reading |
|:------|:-------------------|
| phonon-exflation-sim | `tier0-computation/s28c_phonon_tmatrix.py` (T-matrix infrastructure to extend), `tier0-computation/s28c_steady_state_mu.py` (n_gap interpolation) |
| hawking-theorist | `researchers/Hawking/index.md` Papers 03 (Four Laws), 07 (Gibbons-Hawking), 11 (Bekenstein Entropy). `s25_hawking_computations.py` (spectral entropy data) |
| coordinator | This prompt Section V (pre-registered Constraint Gates). Memorize ALL thresholds before first computation completes |

---

# II. COMPUTATIONS

## 29a-1: T-Matrix Extension to tau = 0.40, 0.45, 0.50 [CRITICAL]

**What**: Extend the KC-2 phonon-phonon T-matrix from the currently validated range (tau <= 0.35) to the KC-3-required range (tau >= 0.50). Solve the non-perturbative Lippmann-Schwinger equation:

$$T = V_{J\text{-even}} (1 - G_0 V_{J\text{-even}})^{-1} \tag{29a.1}$$

where V_{J-even} is the J-projected pairing interaction and G_0 is the free propagator (Synthesis A, U-2, X-1).

**Input**: `s28c_phonon_tmatrix.py` (adapt tau scan range), `s23a_eigenvectors_extended.npz` (mode functions).

**Script**: `s29a_tmatrix_extension.py`

**Method**:
1. Load existing T-matrix infrastructure from `s28c_phonon_tmatrix.py`.
2. Extend tau scan to {0.40, 0.45, 0.50} (currently stops at 0.35).
3. At each new tau: construct V_{J-even} from J-projected pairing interaction, build G_0, solve Lippmann-Schwinger.
4. Compute W = Im(T) (scattering rate) and Gamma_inject from existing B_k data.
5. Report W/Gamma_inject ratio at each new tau value.

**Output**: `s29a_tmatrix_extension.npz`, `s29a_tmatrix_extension.png`

**Computational cost**: ~200x200 matrix inversion per tau value (after J-projection halves dimension from ~400). Estimated: < 5 min on 32-core.

**Agent**: phonon-exflation-sim

---

## 29a-2: Self-Consistent KC-3 with Derived Drive Rate [CRITICAL]

**What**: Replace the scanned drive rate d(tau)/dt ~ 1-8 with a derived value from the modulus equation of motion:

$$\frac{d\tau}{dt} = \sqrt{\frac{2}{G_{\tau\tau}} [E_{total} - V_{eff}(\tau)]} \tag{29a.2}$$

where G_{tau,tau} = 5 (Baptista Paper 15), V_eff is the spectral action plus BCS condensation energy, and E_total is the one free parameter (Synthesis A, C-3).

Using the DNP instability result (SP-5: the round metric is repulsive), the modulus starts at tau ~ 0 with d(tau)/dt ~ 0 and accelerates. The maximum drive rate is determined by E_total.

**Input**: `s28a_spectral_action_comparison.npz` (V_eff), `s28b_self_consistent_tau_T.npz` (BCS condensation energy), `s28c_steady_state_mu.npz` (n_gap interpolation).

**Script**: `s29a_derived_drive_rate.py`

**Method**:
1. Load V_eff(tau) from spectral action data.
2. Load BCS condensation energy from self-consistent tau-T landscape.
3. For E_total in range [V_eff(0)*1.01, V_eff(0)*1.1, V_eff(0)*2, V_eff(0)*10, V_eff(0)*100]:
   - Integrate d(tau)/dt = sqrt(2/5 * [E_total - V_eff(tau)]) from tau=0 to tau=0.50.
   - Record d(tau)/dt at tau = 0.50.
4. Interpolate n_gap from `s28c_steady_state_mu.npz` at derived drive rate.
5. Check: does n_gap > 20 (KC-3 threshold) at tau = 0.50 for any natural E_total?

**Output**: `s29a_derived_drive_rate.npz`, `s29a_derived_drive_rate.png`

**Computational cost**: ODE integration + interpolation. < 1 min.

**Agent**: phonon-exflation-sim

---

## 29a-3: Entropy Balance (H-13 / CP-4) [HIGH]

**What**: Compute the GSL-analog balance sheet explicitly:

$$\frac{dS_{particles}}{d\tau} \geq \left|\frac{dS_{spec}}{d\tau}\right| \tag{29a.3}$$

The particle entropy production rate uses KC-1 data (Gamma_inject = 29,643 at tau = 0.40, B_k(gap) = 0.023):

$$\frac{dS_{particles}}{d\tau} \sim \Gamma_{inject} \cdot \ln(1/B_k) \sim 112{,}000 \tag{29a.4}$$

The spectral entropy decrease rate |dS_spec/d(tau)| uses Session 25 data (H-2 computation).

**Important framing** (Einstein's correction from Synthesis B): There is no horizon on SU(3), so the GSL does not apply in its strict form. The ordinary second law applies: total entropy must increase. This is a WEAKER constraint than the GSL but still non-negotiable.

**Input**: `s28a_bogoliubov_coefficients.npz`, Session 25 spectral entropy data (`s25_hawking_computations.py` outputs).

**Script**: `s29a_entropy_balance.py`

**Method**:
1. Load B_k(tau) and Gamma_inject(tau) from Bogoliubov data.
2. Compute dS_particles/d(tau) = sum_k Gamma_k * ln(1/B_k) at each tau in [0, 0.50].
3. Load spectral entropy S_spec(tau) from Session 25 data. Compute |dS_spec/d(tau)| via finite differences.
4. Plot both derivatives vs tau. Shade regions where entropy balance is satisfied vs violated.
5. Report: at which tau values (if any) does dS_particles/d(tau) < |dS_spec/d(tau)|?

**Output**: `s29a_entropy_balance.npz`, `s29a_entropy_balance.png`

**Computational cost**: Existing data, one derivative calculation. < 1 min.

**Agent**: hawking-theorist or phonon-exflation-sim

---

## 29a-4: Inter-Sector Coupling J_perp (Mermin-Wagner) [MEDIUM]

**What**: Quantify the inter-sector coupling J_perp that determines whether the effective dimensionality exceeds 1 (Synthesis B, C-4). If J_perp > Delta_BCS, mean-field BCS holds and the gap is a true gap. If J_perp < Delta_BCS, the system is effectively 1D and the gap is a pseudogap (Luttinger liquid).

The block-diagonality theorem (Session 22b) says the D_K off-diagonal blocks are EXACTLY zero. But the 4-point interaction V_{abcd} is NOT block-diagonal in general — it couples different sectors through 4-mode overlap integrals. The relevant J_perp is the inter-sector matrix element of the BCS pairing interaction.

**Input**: `s23a_eigenvectors_extended.npz` (mode functions from multiple sectors), `s28c_phonon_tmatrix.py` (adapt to compute inter-sector matrix elements).

**Script**: `s29a_inter_sector_coupling.py`

**Method**:
1. Load eigenvectors from at least 2 sectors (e.g., (0,0) singlet and (1,0) fundamental).
2. Compute 4-point overlap integrals between modes in different sectors:
   V_{abcd}^{inter} = integral over SU(3) of psi_a^{(0,0)*} psi_b^{(0,0)} psi_c^{(1,0)*} psi_d^{(1,0)} dvol
3. Extract the largest inter-sector matrix element: J_perp = max |V_{abcd}^{inter}|.
4. Compare to Delta_BCS from `s28c_bcs_van_hove.npz` at tau = 0.35.
5. Report J_perp / Delta_BCS.

**Output**: `s29a_inter_sector_coupling.npz`, `s29a_inter_sector_coupling.png`

**Computational cost**: 4-point overlap integrals. Moderate. Estimated: 10-30 min on 32-core.

**Agent**: phonon-exflation-sim

---

# III. EXECUTION ORDER

```
29a-1 (T-matrix extension)  ──┐
29a-2 (drive rate)           ──┤── independent, can run in parallel
29a-3 (entropy balance)      ──┤
29a-4 (J_perp)              ──┘

All four feed into the KC-3 VERDICT:
  29a-1 provides: W/Gamma_inject at tau = 0.50
  29a-2 provides: whether drive rate is dynamically natural
  29a-3 provides: whether tau evolution is thermodynamically permitted
  29a-4 provides: whether mean-field BCS is justified (Mermin-Wagner)

KC-3 VERDICT = 29a-1 gate condition satisfied
                AND 29a-3 entropy balance satisfied
```

**Critical path**: 29a-1 is the primary gate. If 29a-1 CLOSES (W/Gamma_inject < 0.1 at tau >= 0.50), KC-3 FAILS and Session 29Ab is unnecessary — terminate early.

---

# IV. SESSION VERDICT CRITERIA

Results from 29Aa that feed into 29Ab:

| Result | Feeds Into | Condition |
|:-------|:-----------|:----------|
| KC-3 verdict (29a-1) | 29Ab (all computations) | KC-3 PASS required to proceed to 29Ab |
| Entropy balance (29a-3) | 29Ab (backreaction) | Entropy PASS required — second law is non-negotiable |
| Drive rate (29a-2) | 29Ab-2 (modulus EOM) | Provides d(tau)/dt initial conditions and E_total range |
| J_perp / Delta_BCS (29a-4) | 29Ab interpretation | Mermin-Wagner verdict determines whether BCS or Luttinger liquid |

**29Aa is successful if it produces**:
1. A definitive KC-3 verdict (PASS or FAIL)
2. A definitive entropy balance verdict (permitted or forbidden)
3. A derived drive rate with E_total dependence
4. A J_perp / Delta_BCS ratio (Mermin-Wagner assessment)

**Early termination conditions**:
- K-29a fires (KC-3 FAIL) → Session 29A terminates. Report verdict, skip 29Ab/29Ac.
- K-29b fires (entropy violation) → Session 29A terminates. Report verdict, skip 29Ab/29Ac.

---

# V. PRE-REGISTERED CONSTRAINT GATES

## Hard Closes (any one terminates Session 29A)

| ID | Condition | Computation | Consequence |
|:---|:----------|:------------|:------------|
| K-29a | W/Gamma_inject < 0.1 at tau >= 0.50 | 29a-1 | KC-3 FAIL. Constraint Chain closed. Framework drops to 3%. |
| K-29b | dS_particles < \|dS_spec\| at any tau in [0, 0.50] | 29a-3 | Tau evolution thermodynamically forbidden. All mechanisms closed. |

## Soft Gates (constrain but do not close)

| ID | Condition | Computation | Consequence |
|:---|:----------|:------------|:------------|
| G-29a | d(tau)/dt < 1 at tau = 0.50 for E_total in natural range | 29a-2 | Drive rate requires fine-tuning. Mechanism weakened but not closed. |
| G-29b | J_perp / Delta_BCS < 1 | 29a-4 | Mermin-Wagner applies. Gap is pseudogap. Quantitative predictions unreliable but qualitative picture may survive. |

## Positive Signals (increase probability)

| ID | Condition | Computation | Consequence |
|:---|:----------|:------------|:------------|
| P-29a | W/Gamma_inject > 0.5 at tau = 0.50 | 29a-1 | KC-3 PASSES with comfortable margin. Constraint Chain complete. |
| P-29b | Self-consistent d(tau)/dt reaches KC-3 threshold | 29a-2 | Drive rate is dynamically natural. No fine-tuning. |

---

# VI. AGENT ASSIGNMENTS

| Agent | Role | Computations |
|:------|:-----|:-------------|
| **phonon-exflation-sim** | Primary computation | 29a-1, 29a-2, 29a-4, optionally 29a-3 |
| **hawking-theorist** | Thermodynamic evaluation | 29a-3 (entropy balance, Gibbons-Hawking expertise) |
| **coordinator** | Gate classification + documentation | Classify EACH result in real time. Assemble gate verdicts. |

**Recommended team size**: 3 agents (phonon-sim + hawking + coordinator). Minimum viable: phonon-sim + coordinator.

---

# VII. OUTPUT FILES

| File | Computation | Producer |
|:-----|:-----------|:---------|
| `tier0-computation/s29a_tmatrix_extension.py` | 29a-1 | phonon-sim |
| `tier0-computation/s29a_tmatrix_extension.npz` | 29a-1 data | phonon-sim |
| `tier0-computation/s29a_tmatrix_extension.png` | 29a-1 plot | phonon-sim |
| `tier0-computation/s29a_derived_drive_rate.py` | 29a-2 | phonon-sim |
| `tier0-computation/s29a_derived_drive_rate.npz` | 29a-2 data | phonon-sim |
| `tier0-computation/s29a_derived_drive_rate.png` | 29a-2 plot | phonon-sim |
| `tier0-computation/s29a_entropy_balance.py` | 29a-3 | hawking or phonon-sim |
| `tier0-computation/s29a_entropy_balance.npz` | 29a-3 data | hawking or phonon-sim |
| `tier0-computation/s29a_entropy_balance.png` | 29a-3 plot | hawking or phonon-sim |
| `tier0-computation/s29a_inter_sector_coupling.py` | 29a-4 | phonon-sim |
| `tier0-computation/s29a_inter_sector_coupling.npz` | 29a-4 data | phonon-sim |
| `tier0-computation/s29a_inter_sector_coupling.png` | 29a-4 plot | phonon-sim |
| `tier0-computation/s29a_gate_verdicts.txt` | All gate verdicts | coordinator |
| `sessions/session-29/session-29Aa-synthesis.md` | Synthesis | coordinator |

---

# VIII. CONDITIONAL PROBABILITY (POST-29Aa)

Pre-Session 29A probability: **7-8% panel / 4-5% Sagan** (Synthesis B consensus).

| Scenario | KC-3 | Entropy | Posterior (panel) | Path Forward |
|:---------|:------|:--------|:-----------------|:-------------|
| **KC-3 PASS + entropy PASS** | PASS | PASS | 10-14% | Proceed to 29Ab (backreaction) |
| **KC-3 PASS + entropy FAIL** | PASS | FAIL | 2-3% | Thermodynamic veto. Session 29A terminates. |
| **KC-3 FAIL** | FAIL | -- | 3% (structural floor) | Session 29A terminates. |

---

*Session 29Aa prompt dissected from Session 29A plan (Hawking, 2026-02-28). This is the gateway sub-session: KC-3 and entropy balance determine whether Session 29Ab/29Ac proceed. All four computations can run in parallel. Total estimated runtime: < 30 min. If KC-3 or entropy CLOSES, Session 29A terminates early with a definitive verdict.*
