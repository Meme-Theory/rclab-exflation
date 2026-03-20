# GPE Simulation Review (D/H Analysis)

## Core Verdict: FIT, NOT PREDICTION
- 4-5 free params (tau_exp, gamma0, R_freeze, freeze_mode, d_pair_factor), 1 observable (D/H=2.737e-5)
- Standard BBN: 1 param (eta) predicts D/H, He-4, He-3, Li-7 simultaneously
- R_freeze=3.0 CHOSEN to produce D/H~2.5e-5 (not derived from physics)
- D/H monotonically decreasing at t=100, no plateau demonstrated

## Phase 2B Code Review: 2 Critical Issues
1. **Self-consistent freeze-out design flaw**: SC mode uses step function in gamma; breakthrough used smooth sigmoid. Not apples-to-apples comparison.
2. **Soft pairing sign error**: E_bind = pi*n0*ln(d/xi_eff) gives E_bind<0 for d<xi (most tightly bound pairs). Code rejects close pairs instead of accepting them. D/H~10^-5 from healing-length-exceeds-separation mechanism, NOT binding-energy-vs-kinetic-energy as described.

## Moderate Issues
- Convergence test does not check time-convergence of D/H (still decreasing at end)
- Sensitivity scan uses single seed (42) for all parameter variations
- Ensemble aggregate D/H uses binary pair count, not soft weights

## Hidden Parameters (not listed as "free" but affect result)
- Sigmoid width: 0.1*R_freeze (hardcoded, expansion.py line 94)
- IC healing steps: 150, KZ quench steps: 1000
- Pair regularization: d=max(dist,0.5), xi_eff=max(xi,0.5)
- L = 64*N/256 (box size scaling)

## Kinetic Energy Normalization Bug
- Code uses dx^2/N^2, correct is dx^4 (off by 1/L^2)
- Only affects absolute energy values, NOT relative drift or D/H (non-critical)

## Key Prediction: CV is the decisive diagnostic
- CV<50%: soft pairing statistically stable, worth deeper investigation
- CV>100%: result is noise
