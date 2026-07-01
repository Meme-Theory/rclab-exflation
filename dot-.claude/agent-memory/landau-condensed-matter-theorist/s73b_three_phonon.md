---
name: S73B Three-Phonon Beliaev (L=3 + L=7 confirmation)
description: Beliaev vertex B2->B1+B1 FAIL, particle-hole protection STRUCTURAL, L_max-invariant
type: project
---

## S73B THREE-PHONON: FAIL CONFIRMED-STRUCTURAL

Gamma/H_fold = 7.77e-7 at L_max ∈ {3, 5, 7} (identical to 6+ decimals). Beliaev channel B2 -> B1 + B1 STRUCTURALLY INOPERATIVE.

### Why
V_3 = V_eff * (u_B1^2 v_B2 - v_B1^2 u_B2) STRUCTURALLY SUPPRESSED by particle-hole symmetry. B1 (xi=0, Fermi surface) and B2 (xi=0.026) both have u ≈ v; coherence factor coh = -0.020 (18x suppression). Even with stimulated enhancement (n_B2=53, factor 2998x), 6 OOM below threshold.

### L_max-Invariance Proof
1. (0,0) trivial irrep: 8 positive eigenvalues fixed by Kosmann singlet on Cl(8); L_max adds higher irreps but does NOT alter (0,0) eigenvalues.
2. B1 = absolute global min of positive spectrum at every L_max. Non-trivial sectors start at E_min > 0.8359 > E_B1=0.8197 (rep-theoretic gap).
3. Therefore mu=E_B1 exactly; xi_B1=0 exactly; (u_B1, v_B1)=(1/sqrt(2), 1/sqrt(2)); B2 (u,v) depend only on Delta_BCS (canonical) and E_B2 (L-invariant); V_eff[B1,B2] L-invariant; C_Beliaev L-invariant; V_3 L-invariant; Gamma L-invariant.

### Numbers (L_max=3,5,7 — all identical)
- E_B1 = 0.81974111 M_KK; (0,1)/(1,0) E_min = 0.83589
- u_B2=0.72622, v_B2=0.68747 (xi_B2/Delta=0.0549)
- C_Beliaev = -0.01938; V_3^Bog = 0.00820 M_KK
- Gamma_stim/H_fold = 7.77e-7

### Closure
- CLOSES CF4 PERMANENTLY (deferred since S46, 26 sessions).
- B2 decay must proceed via Josephson transfer, GGE thermalization, or direct transit friction.
- Resonance condition perfectly satisfied (transit broadening 46,570x > mismatch); failure purely from vertex suppression.
- QRPA frequencies omega_B1=1.632, omega_B2=3.245 (S40 convention). Direct 8-mode QRPA at L=7 gives 0.678, 0.725 (different convention); coherence-factor suppression dominant either way.

### Files
- `computations/s73b_three_phonon.{py,npz,png}`
- `computations/s73b_three_phonon_lmax7.{py,npz,png}`
