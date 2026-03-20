# S45 Pre-Registered Gate: OCC-SPEC-45

## Occupied-State Spectral Action Minimum Search

**Gate ID**: OCC-SPEC-45
**Priority**: CRITICAL (sole surviving tau-stabilization route within spectral action framework)
**Source**: Connes S44 collab review, Section 3.6 + Q3. Paper 16 (Dong-Khalkhali-van Suijlekom 2022).
**Convergence**: Novel — not proposed by any other S44 reviewer. Connes identifies it as "the single surviving route."

---

## Background

The S37 monotonicity theorem (CUTOFF-SA-37) proved:

> For any monotone decreasing f, S(tau) = Tr f(D_K(tau)^2 / Lambda^2) is monotone increasing.

This closed tau-stabilization through the vacuum spectral action. S44 W4-4 (F-FOAM-2) closed foam-modified non-monotone f. Every attempt to find a minimum in the spectral action has failed across Sessions 37-44.

**The loophole**: the S37 theorem sums over ALL modes equally. Paper 16 (Connes/16) extends the spectral action to finite density:

S_occ(tau) = sum_k n_k(tau) * f(lambda_k(tau)^2 / Lambda^2)

where n_k(tau) are the BCS Bogoliubov occupation numbers. The occupation numbers n_k depend on the spectrum through the self-consistent gap equation, and the spectrum depends on tau. The n_k are NOT monotone in tau — they depend on the van Hove singularity structure which changes during the transit (S44 W6-8: 9 singularities at tau=0, 12 at tau>0, near-crossing at tau=0.19).

**Why this might work**: Near the fold, van Hove singularities enhance pairing for specific modes, causing their n_k to spike. If those modes' eigenvalues are simultaneously increasing (stiffening), the product n_k * f(lambda_k^2) could DECREASE — creating a turning point in S_occ that the vacuum S cannot have. This is the inverted Born-Oppenheimer regime (S38): geometry fast, pairing slow.

---

## Pre-Registered Gate

**OCC-SPEC-45**:
- **PASS**: S_occ(tau) has a local minimum at tau_min in [0.10, 0.25] with barrier height > 0.01 * S_occ(tau_min)
- **FAIL**: S_occ(tau) is monotone at all Lambda and all tau in [0.00, 0.50]
- **INFO**: Minimum exists but barrier height < 0.01 (too shallow for dynamical trapping)
- **BONUS**: If tau_min is within 10% of tau_fold = 0.190 (self-consistent fold selection)

---

## Computation Specification

### Agent: connes-ncg-theorist (primary), nazarewicz-nuclear-structure-theorist (cross-check)
### Model: opus
### Cost: HIGH (BCS self-consistent gap at 20 tau values × 992 modes)

### Steps

1. **Load spectrum**: eigenvalues lambda_k(tau) from `tier0-computation/s41_spectral_refinement.npz` (multiple tau) and `tier0-computation/s36_sfull_tau_stabilization.npz`. PW degeneracies from standard dim(p,q) formula.

2. **BCS gap equation at each tau**: For tau = 0.00, 0.02, 0.05, 0.08, 0.10, 0.12, 0.14, 0.16, 0.17, 0.18, 0.185, 0.190, 0.195, 0.20, 0.22, 0.25, 0.30, 0.35, 0.40, 0.50:
   - Compute DOS N(E, tau) from eigenvalues
   - Solve self-consistent BCS gap equation: 1/g = sum_k 1/(2*E_k) where E_k = sqrt(xi_k^2 + Delta^2)
   - Use the BCS coupling from S35/S38: V_eff from the B2 pairing interaction
   - Obtain Delta(tau) and the Bogoliubov amplitudes u_k(tau), v_k(tau)
   - Compute occupation numbers: n_k(tau) = v_k(tau)^2 = (1/2)(1 - xi_k/E_k)

3. **Occupied-state spectral action**: For each tau, compute:

   S_occ(tau) = sum_k d_k * n_k(tau) * f(lambda_k(tau)^2 / Lambda^2)

   with f(x) = exp(-x) (standard exponential cutoff) and Lambda = M_KK.

   Also compute with f(x) = theta(1-x) and f(x) = (1+x)^{-3} for cutoff robustness.

4. **Vacuum spectral action comparison**: Compute S_vac(tau) = sum_k d_k * f(lambda_k^2/Lambda^2) at same tau points. Verify monotonicity (S37 theorem cross-check).

5. **Search for minimum**: Plot S_occ(tau). Check:
   - Is there a local minimum? (dS_occ/dtau = 0 with d^2S_occ/dtau^2 > 0)
   - Where? (tau_min)
   - How deep? (barrier = S_occ(tau_shoulder) - S_occ(tau_min))
   - Cutoff-robust? (does it survive all three f choices?)

6. **Decompose the mechanism**: If minimum found, identify which modes drive it:
   - Compute dS_occ/dtau = sum_k d_k [dn_k/dtau * f + n_k * df/dtau * 2*lambda_k * dlambda_k/dtau / Lambda^2]
   - The first term (occupation change) competes with the second term (eigenvalue change)
   - Which sectors (B1, B2, B3) contribute to each?
   - Is the van Hove near-crossing at tau=0.19 (W6-8 T3-T5, delta=0.0008) the driver?

7. **Barrier dynamics**: If minimum exists, compute:
   - Barrier height in M_KK^4 units
   - Oscillation frequency at the minimum: omega_osc = sqrt(d^2S_occ/dtau^2 * Z_tau)
   - Dwell time: t_dwell ~ 1/omega_osc
   - Does dwell time exceed H^{-1}? (tau-stabilization criterion)

### Input Files
- `tier0-computation/s41_spectral_refinement.npz`
- `tier0-computation/s36_sfull_tau_stabilization.npz`
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s38_cc_instanton.npz` (BCS coupling, Delta_0)
- `tier0-computation/s36_mmax_authoritative.npz`
- `tier0-computation/s44_dos_tau.npz` (van Hove tracking)
- `tier0-computation/s44_vanhove_track.npz`
- `tier0-computation/tier1_dirac_spectrum.py` (if new tau values needed)
- `researchers/Connes/16_2022_Dong_Khalkhali_van_Suijlekom_Second_quantization_spectral_action.md`

### Output Files
- Script: `tier0-computation/s45_occ_spectral.py`
- Data: `tier0-computation/s45_occ_spectral.npz`
- Plot: `tier0-computation/s45_occ_spectral.png`

---

## Why This Might Fail (Adversarial Pre-Assessment)

1. **Occupation numbers may be too smooth.** If n_k(tau) varies slowly compared to lambda_k(tau), the weighting doesn't change the monotonicity structure enough. The BCS gap equation is a mean-field smoothing that may wash out van Hove spikes.

2. **The gap may vanish before the fold.** If Delta(tau) → 0 before tau reaches 0.19, then n_k → theta(mu - lambda_k) (step function), and S_occ reduces to a sum over occupied states with monotone eigenvalues — still monotone.

3. **The near-crossing at tau=0.19 may be too weak.** W6-8 found delta = 0.0008 between T3 and T5 — close but not crossing. If they don't cross, the van Hove enhancement may be insufficient.

4. **Wrong functional.** Even if S_occ has a minimum, it may not be the GRAVITATING functional. The CC gap audit showed the spectral action is wrong for the CC; the occupied-state version might also be wrong.

5. **Truncation artifact.** The 992-mode spectrum at max_pq_sum = 6 may not have enough resolution near van Hove points. The dissolution scaling (W6-7: epsilon_c ~ 1/sqrt(N)) suggests the fine structure is truncation-dependent.

## Why It Might Work

1. **Inverted Born-Oppenheimer.** S38 proved geometry is fast, pairing is slow. The occupation numbers LAG the eigenvalue evolution. This lag creates a phase difference between n_k and lambda_k that can produce constructive interference (minimum) at specific tau.

2. **Van Hove singularities are real.** W5-3 and W6-8 confirmed 12 singularities with specific tau-trajectories. Near a van Hove point, the DOS diverges logarithmically, spiking the pairing strength and driving n_k non-monotonically.

3. **The BCS instability is a theorem.** S35 RG-BCS-35: any g > 0 flows to strong coupling. This guarantees Delta(tau) > 0 for all tau where a van Hove singularity exists — the gap doesn't vanish prematurely.

4. **Paper 16 is rigorous.** The occupied-state spectral action is mathematically well-defined (Theorem 4: KO-dimension preserved). It's not an ad-hoc modification — it's the canonical finite-density extension of Connes' program.

5. **S_occ encodes different physics.** The vacuum S counts all modes equally (geometric). S_occ weights by many-body state (physical). The distinction is precisely where the S37 theorem's loophole lives.
