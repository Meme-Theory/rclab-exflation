# Session 38 W1: GPV-as-Phonon Workshop Detail

## Workshop File
`sessions/archive/session-38/session-38-naz-qa-workshop.md`

## Key Results

### GPV Classification (RESOLVED)
- GPV is NOT a phonon. It is a **pair vibration** (pair-transfer mode, Delta_N = +/-2)
- Correct classification: "collective pair vibration of B2 flat optical sector"
- Also identifiable as amplitude (Higgs) mode of BCS condensate
- Nuclear analog: ^210Pb GPV seen via ^208Pb(t,p), coherent enhancement 5-10x
- Framework's B_plus = 9.94, coherent/incoherent = 6.32 matches nuclear GPV systematics
- omega_PV/(2*Delta_OES) = 0.854 -- BELOW pair-breaking threshold (anomalous: nuclei always above)
- This means GPV is a BOUND pair vibration, not continuum resonance. Consequence of B2 flatness.

### Post-Quench Survival (CONFIRMED with caveats)
- GPV pole survives 443x quench because:
  1. Pole is property of Hamiltonian (V + E_8), not ground state
  2. System is integrable (r=0.321, no Lyapunov) -- does NOT thermalize
  3. K_7 quantum number provides IAS-like protection
- Nuclear comparison: GDR dissolves at T ~ 3-4 MeV (Gamma/E ~ 1). GPV dissolves at T ~ 0.7*Delta.
  At 443x, nuclear system would be completely dissolved. Survival is ANOMALOUS -- only possible because integrable.
- Caveats: (a) 50-70% strength retention, (b) <7.3% frequency shift, (c) integrability untested for 73K modes

### 443x Energy Dump (Nuclear Context)
- Nuclear analog: ^6He at 443 MeV -- completely unbound (E*/B = 15x)
- NOT a compound nucleus. Complete disassembly into free particles.
- But single-particle spectrum E_8 unchanged (geometric property of D_K)
- Compound nucleus analogy BREAKS because system does not thermalize

### Parametric Amplification (KILLED)
- omega_att/omega_PV = 1.81 (near 2:1) is STATIC geometric relationship
- Kinematically unrealizable: tau_Q/T_att ~ 2.6e-4 (fewer than one pump cycle)
- Nuclear backbending analog: omega_c/omega_GPV ~ 0.5 in A~160-170 confirms frequency relationship
- But requires sustained interaction (>10 cycles) to develop parametric amplification

### Post-Fold Spectrum Prediction
| omega | Mode | Strength | Q-factor | Nuclear Analog |
|:------|:-----|:---------|:---------|:---------------|
| 0.137 | Pair removal | 5.63 | High | ^210Pb -> ^208Pb |
| 0.792 | GPV | 5-7 (post-quench) | >5 | ^208Pb(t,p) GPV |
| 0.928 | 2-QP threshold | continuum | -- | 2*Delta |
| 1.337 | omega_split | 1.55 | Moderate | Higher GPV |
| 1.883 | Double-pair | 1.55 | Broad | 2-phonon GPV |

### GPE Simulation Recommendation
- Use BdG equations (NOT scalar GPE) -- pair amplitude Delta(t) is the dynamical variable
- 4-mode minimum (B2 quartet), 8-mode full with V_8x8
- Time-dependent linear quench: epsilon(t) = epsilon_0 + v*t, v = 26.5
- Track FT of |Delta(t)|^2 post-quench for GPV peak
- Do NOT add dissipation (integrable system)
- Do NOT represent as classical phonon field
- Run >= 10 * T_OTOC = 67 time units post-quench

### Nuclear Benchmarks for Simulation
| Observable | Nuclear | Framework |
|:-----------|:--------|:----------|
| Coherent enhancement | 5-10x | 6.32x |
| omega_GPV/(2*Delta) | 1.5-2.5 | 0.854 (below threshold) |
| Strength in GPV | 60-80% | 85.5% |
| Post-quench survival | No (thermalize) | Yes (integrable) |
| Q-factor | 2-5 | >5 (prediction) |

## New Analogies Established
- ^210Pb GPV <-> B2 pair vibration (coherent enhancement, pair-transfer channel)
- IAS (isospin-protected) <-> GPV (K_7-protected, integrability-protected)
- Nuclear backbending <-> 2:1 frequency ratio (same physics, opposite direction)
- ^6He at extreme E* <-> post-fold disassembly (N_pair=1, few-body)
- Ericson fluctuations (many overlapping resonances) <-> NOT applicable (N_eff=4 too small)
