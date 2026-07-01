---
name: Sessions S55-S59 Consolidated
description: S55-S59 results — fabric discovery (E_J=7.042), BA spectrum, Leggett dispersion, Josephson dominance, squeezing, epsilon hierarchy, DM channel
type: project
---

## S55 (Fabric Discovery)
- FABRIC-COUPLING: E_J=7.042 per bond. E_J/E_c=194. SUPERFLUID all tau. omega_J=0.715.
- PHONON-DISP: c_eff=0.338 (37% of c_Gold). 127% tau-variation. 18 Z_2-even, 14 Z_2-odd branches.
- ZETA MONOTONE: zeta'_D(0) monotone increasing (collective, 26/31 individually non-monotone).
- EUCLID-CONTINUUM FAIL: "Mode count wins" for non-interacting cells. E_J/E_c=194 violates this.
- |A_coset|^2 = 3/2 + (3/2)e^{-4tau} (O'Neill A-tensor, PROVEN algebraic).
- Z_fabric != Z_single^N. Phase coherence changes effective mode count. PERMANENT.

## S56 (BA Spectrum + Leggett Fabric + Collab)
**BA-SPECTRUM-56**: F_BA minimum at tau=0.306 (global min=-7.08). c_BA=0.399.
- Fold: omega_1=0.209, T_GH=0.590, 7/31 modes thermal, F_BA=7.02.
- THERMAL regime (omega_1/T_GH=0.35). Not quantum.

**LEGGETT-FABRIC-56**: Two-speed hierarchy confirmed.
- c_BA=0.399 (fast, massless) vs c_L=0.019-0.032 (slow, massive). Ratio 0.048-0.080.
- Leggett STRONGLY DISPERSIVE at all tau. Gap thermally populated.

**Collab permanent results**:
- Josephson dominance: F_J/F_BA ~ N_bonds*E_J/(N_modes*omega_mean) ~ 14. PERMANENT.
- N_eff=41.5. BKT maintained (T_GH/T_BKT<0.17).
- Two-adiabaticity: Josephson gap=13.04 (adiabatic), Leggett gap=0.070-0.138 (non-adiabatic).
  P_exc(Josephson)=6.6e-4, P_LZ(Leggett)~0.996. Transit selectively excites Leggett.

## S57 (Squeezing + DM)
**My computations**: Channel energy budget (E_L/E_matter=26.4%), Bogoliubov squeezing (f_DM=0.119 exc, 0.440 total), omega_L sweep (monotone, deeply diabatic).

**Key session results**: Gap-scaling PASS (Delta_N~N^{-1.84}). CC-SIGN PASS (Lambda_eff=+1.709).
DM-ABUNDANCE PASS (Omega_DM h^2 in [0.017,0.188]). FLOQUET CLOSED (mu_F=0).
Mode-independent BA theorem: |beta|^2=1.015 for ALL 31 modes (f(tau)*sqrt(lambda_n) factorization).
Desert inert at Mach 2700. CC = phonon lifetime = integrability.

**Lessons**: Leggett = harmonic oscillators, NOT two-level (use squeezing not LZ).
epsilon (50% uncertain) = THE bottleneck. CC = zero phonon-phonon scattering.

## S58 (Epsilon + Anharmonicity)
**EPSILON-DIRECT-58 PASS**: eps_direct=0.00143 +/- 39%. V_bare vs V_constrained are DIFFERENT MODELS.
- V_bare: Trap 1 (V[B1,B1]=0) + selection rule (V[B1,B3]=0) respected.
- V_constrained violates both. Ratios 0.07x-6.6x (NOT rescaling).
- Dominant uncertainty: within-band V_B2B3 CoV=36.3%.

**ANHARMONIC-LEGGETT-58**: Harmonic SAFE by 1.7e4x. Gamma*dt=6e-5.
- Cubic=0 exact (cos even, unfrustrated). Quartic max=7e-4. J_L=eps*E_J=0.017.
- phi_RMS(fold)=2.04 rad but J_L weakness suppresses scattering.
- Leggett modes on C2 sub-graph (50 bonds). J_L/J_C2 ~ 1/400.

## S59 (Canonical Epsilon)
**EPSILON-CANONICAL-59 PASS**: eps_canonical=0.00374. Matches eps_implied(0.00369) to 1.6%.
- eps_bare(0.00143) is microscopic matrix element. eps_S49(0.00248) from wrong V. Both SUPERSEDED.
- Full 3-band eigenvalue: omega_L1(V_bare)=0.04923, omega_L2=0.08733.
- 2-band partition formula underpredicts by 18-56%. Must use full 3-band.
- f_DM shifts +35% to 0.161 (lower gap dominates over higher J_L for squeezing).
