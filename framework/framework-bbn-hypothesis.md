# Framework BBN Hypothesis: Scale-Dependent Tau and the Phonon Cascade

**Date**: 2026-03-08
**Source**: Session 36 discussion (post-W4-A/W4-B needle hole results)
**Status**: HYPOTHESIS (pre-computational, conceptual framework)
**Prerequisite computations**: CUTOFF-SA-37, saddle-structure mapping

---

## I. Core Claim

The Jensen deformation parameter tau is not a free modulus rolling in a static potential. It is **dynamically linked to the dominant phonon wavelength** at each cosmological epoch. The exflation process is a cascade of phonon fragmentations, each corresponding to a wall collapse at a specific tau value. The spectral action at any epoch involves only modes at the current phonon scale — not all KK levels simultaneously.

---

## II. The Phonon Scale Hierarchy

### Early Universe (BBN epoch, T ~ 1 MeV)

The dominant phonon mode spans the Hubble volume. The internal geometry is maximally deformed (high tau ~ 0.34-0.54) because the phonon IS the universe at that scale. The domain walls — which ARE the gauge fields in the 4D effective theory — sit at the false vacuum saddle points corresponding to that scale.

At this epoch:
- tau is at a saddle, not the fold
- The BCS pairing window [0.175, 0.205] has not been reached
- No fold-scale condensate exists
- The relevant physics is saddle-scale wall structure
- delta_H/H from BCS is identically zero (no condensate during BBN)

### Intermediate Epochs (cascade)

As exflation proceeds, the universe-scale phonon fragments into smaller phonons. Each fragmentation event is:
1. A domain wall collapse at the current tau saddle
2. Energy release into 4D expansion (the "whirlpool in reverse")
3. A downward step in the effective tau toward the next saddle
4. The walls migrate inward through tau-space

This is not one particle rolling down a hill. It is a sequence of symmetry-breaking events, each preparing the landscape for the next. The cascade picture:

```
tau ~ 0.54  (universe-scale phonon, earliest saddle)
    ↓ wall collapse → expansion burst
tau ~ 0.34  (next saddle, galaxy-cluster-scale phonons)
    ↓ wall collapse → expansion burst
tau ~ 0.24  (approaching fold, galactic-scale phonons)
    ↓ wall collapse → expansion burst
tau ~ 0.190 (van Hove fold, final fragmentation, particle-scale phonons)
    ↓ BCS condensation → Standard Model physics
tau → 0     (round SU(3), ground state, far future?)
```

Each step has its own:
- Pairing window (or lack thereof)
- Wall structure and collapse dynamics
- Phonon burst spectrum
- Contribution to 4D expansion history

### Present Day (tau ~ 0.190)

Present-day particle physics lives at the fold because we ARE the final-scale phonons. The van Hove singularity at the fold is the density-of-states peak for the smallest-scale fragmentation. The BCS condensate at the fold produces the domain walls whose excitations are SM particles.

---

## III. Resolution of the Needle Hole

### Why the Linear Spectral Action Gives the Wrong Answer

The Session 36 W4-A/W4-B computations found:
- Static: dS/dtau / |E_BCS| = 376,000 (gradient overwhelms condensation)
- Dynamic: tau_BCS / tau_dwell = 38,600 (trajectory too fast for condensation)
- Level 3 KK modes contribute 91.4% of the gradient

The linear sum S = Sigma |lambda_k| treats all KK levels simultaneously and equally. But physically, the high KK levels (Level 3 = 91% of gradient) correspond to phonon modes that have ALREADY fragmented at earlier epochs. They should not contribute to the dynamics at the fold scale.

### The Cutoff Function IS the Scale Separation

The Connes spectral action Tr f(D^2/Lambda^2) uses a smooth cutoff f that suppresses eigenvalues above Lambda. This is not an arbitrary mathematical choice — it is the physical statement that **the spectral action at any epoch only involves modes at the current phonon scale**.

At the fold epoch (tau ~ 0.190):
- Lambda should be set at or near the fold-scale eigenvalues
- Level 3 modes (91% of linear gradient) are above Lambda and suppressed
- The remaining dynamics is dominated by the singlet fold structure
- The singlet-only shortfall is 177x (dynamic) or 10.4x with BCS friction
- The fold curvature in the cutoff-modified spectral action may close this gap

The needle hole becomes: **does the cutoff-modified spectral action S_f(tau) have the right structure at the fold scale?** This is CUTOFF-SA-37.

### The 91% Suppression Is Not Fine-Tuning

Suppressing Level 3 by 99.7% sounds like fine-tuning. But it is not:
- Level 3 eigenvalues are ~10x larger than Level 0 eigenvalues
- A smooth cutoff f(x) that falls from 1 to 0 over one decade naturally achieves this
- The scale Lambda is set by the physics (the KK mass scale at the current epoch)
- No parameter is tuned — the cutoff follows from the cascade dynamics

---

## IV. Implications for BBN

### Standard BBN in the Cascade Picture

During BBN (T ~ 1 MeV, z ~ 10^9):
- tau is at a high saddle (tau ~ 0.34-0.54)
- The internal geometry is in its pre-fragmentation configuration
- No BCS condensate exists at the fold scale
- The expansion rate H(T_BBN) is determined by the saddle-scale spectral action, not the fold-scale

### The Lithium Problem

The BBN-LITHIUM-36 computation (Feynman, Session 36 W2-F) found delta_H/H = -6.6e-5 at the fold. This is the wrong computation:
1. During BBN, tau is not at the fold
2. There is no BCS condensate during BBN
3. The relevant modification to H is from the saddle-scale spectral action coefficients, not from D_BdG vs D_K at the fold

The correct BBN computation would:
1. Identify which saddle tau occupies during BBN
2. Compute the spectral action at that saddle (not the fold)
3. Compare the expansion rate at the saddle to standard GR
4. Assess whether the saddle-scale wall structure modifies H(T_BBN) in the lithium-resolving window [-0.15, -0.03]

This requires:
- Mapping the saddle structure of S_f(tau) with the physical cutoff (CUTOFF-SA-37)
- Computing the tau(t) trajectory through the cascade (CASCADE-DYN-37)
- Evaluating a_0, a_2 at the saddle tau, not the fold tau

### Level 4 Candidacy

If the cascade dynamics determines:
1. Which saddle tau occupies during BBN (from the tau(t) trajectory)
2. The spectral action coefficients at that saddle (from the cutoff computation)
3. The resulting delta_H/H falls in [-0.15, -0.03]

...then the lithium prediction follows from the same geometry that gives the gauge couplings, with no free parameters. This would be a genuine Level 4 novel prediction.

---

## V. Testable Predictions of the Cascade Picture

### Expansion History

The cascade produces a STAIRCASE expansion history, not smooth inflation:
- Each wall collapse → burst of expansion
- Between collapses → slower expansion (or deceleration)
- The "e-folds" of inflation are distributed across multiple cascade steps
- Each step has a characteristic energy scale set by the saddle eigenvalues

### Preferred Scales

If the saddles are at specific tau values (0.54, 0.34, 0.24, 0.190), each produces a wall collapse at a specific energy scale. These scales may appear as:
- Preferred BAO-like features in the matter power spectrum
- Characteristic scales in void statistics
- Steps in the dark energy equation of state w(z)

These are testable against DESI, Euclid, and SDSS data (Level 4 candidates if confirmed).

### CMB Signatures

The staircase expansion may produce:
- Oscillatory features in the primordial power spectrum (from discrete cascade steps)
- Non-Gaussianity correlated with the saddle scales
- A modified spectral index n_s that varies with wavenumber k

---

## VI. Computational Prerequisites

| Gate | Computation | What it resolves |
|:-----|:-----------|:----------------|
| CUTOFF-SA-37 | S_f(tau) with physical cutoff | Does fold minimum emerge? Saddle structure? |
| CASCADE-DYN-37 | tau(t) trajectory with scale-dependent cutoff | Which saddle during BBN? Dwell times? |
| SADDLE-BBN-37 | a_0, a_2 at saddle tau with saddle-scale cutoff | delta_H/H at BBN from saddle physics |
| K7-G1-37 | q_7 of G1 mode in (1,0) | PMNS route (independent, but same session) |

CUTOFF-SA-37 is the prerequisite for everything else. If S_f(tau) has no fold minimum for any physical cutoff, the cascade picture remains conceptual. If it does, the entire program follows.

---

## VII. Relationship to Existing Framework Results

### What Survives Unchanged
- All pure math results: KO-dim=6, anomaly-free, second-order, vibrational, Schur's lemma
- BCS instability theorem (any g > 0 flows to strong coupling in 1D)
- Mass hierarchy R = 27.2 and normal ordering
- ED convergence (enhanced, B1 catalyst)
- W6 resolution (species scale)

### What Is Reframed
- SC-HFB-36 "FAIL": not a failure — the static equilibrium question was wrong. The system rolls, it doesn't sit.
- TAU-STAB-36 "FAIL": the linear spectral action is the wrong computation. The cutoff-modified S_f is the physical one.
- TAU-DYN-36 "FAST ROLL": the trajectory is too fast because it includes all KK levels. Scale-separated dynamics may be much slower at the fold scale.
- BBN-LITHIUM-36 "FAIL": computed at wrong tau. The cascade places BBN at a saddle, not the fold.

### What Is New
- Tau linked to phonon wavelength (not a free modulus)
- Cascade = sequence of wall collapses (not single roll)
- Cutoff = scale separation (not arbitrary suppression)
- BBN at saddle, not fold
- Staircase expansion, not smooth inflation
