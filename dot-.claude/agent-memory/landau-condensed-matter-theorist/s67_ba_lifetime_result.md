---
name: S67 BA-LIFETIME-FABRIC-67 Results
description: Beliaev decay rates for all 256 BA modes on 32-cell CG(24) fabric — PASS with 53 OOM margin
type: project
---

## S67 BA-LIFETIME-FABRIC-67: Beliaev-Associative Phonon Thermalization

Gate: **PASS**. min(Gamma_BA / H(z_eq)) = 8.83 x 10^{52} >> 10. All 256 BA modes decay 53 OOM before z_eq.

**Why:** The Leggett-only DM scenario requires all BA (Bogoliubov-Anderson) phonon modes to thermalize before matter-radiation equality so that only Leggett modes survive as DM relics. This computation verifies that requirement.

**How to apply:** The Leggett-only DM picture (Omega_DM h^2 = 0.120, 0.6% from Planck) is now self-consistent from the thermalization side. BA modes are overdamped (Q < 2), Leggett modes are underdamped (Q = 18.6). Use this in any future DM discussion.

### Key Numbers
- Gamma_BA range: [0.268, 2.343] M_KK = [3.03e40, 2.64e41] s^{-1}
- tau_BA range: [3.78e-42, 3.30e-41] s (QA estimated 3.1e-37, we get 4-5 OOM shorter)
- H(z_eq) = 3.43e-13 s^{-1}
- Q_BA: 0.10 (B2[0]) to 1.30 (B2[3]). All overdamped.
- Landau damping suppressed 62x (n_th = 0.016 at T_acoustic)
- Classification: FUNCTIONAL-INDEPENDENT (set by J_eff and BCS gap, both structural)

### Physics
- BA modes are collective phase oscillations of the Josephson condensate on CG(24)
- In the strong-coupling regime (E_J/Delta = 73.2), phase fluctuations are large -> short lifetimes
- Leggett mode is inter-band coherence oscillation, protected by gap between pairing channels
- Standard Landau quasiparticle criterion (Paper 11): Gamma << omega for stability. BA fails, Leggett passes.

### Files
- `computations/s67_ba_lifetime.{py,npz}`
