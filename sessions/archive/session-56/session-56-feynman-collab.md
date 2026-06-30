# Session 56 Collaborative Review: Feynman-Theorist

**Session**: S56 — Z Warriors Assemble: The Fabric Partition Function
**Reviewer**: Feynman-Theorist (path integrals, QFT, renormalization, Feynman diagrams)
**Source**: `session-56-results-workingpaper.md` (20 computations, 4 waves)
**Date**: 2026-03-22

---

## 1. What Was Computed and What It Means

S56 asked the right question: is Z_fabric different from Z_cell^N, and does the difference break the single-cell monotonicity that killed 46+ stabilization attempts? The answer is: Z_fabric IS structurally different (N_eff = 41.5 at fold, not 992; BA phonon free energy is non-monotone; BKT order persists), but the difference does NOT produce a free energy minimum. The Josephson stiffness term F_J = -N_bonds * E_J * m dominates at every tau and is monotonically decreasing, because E_J(tau) ~ J_C2(tau)^2 decreases monotonically as the C2 coset direction stretches.

This is what I would call a "clean structural FAIL." The computation was correctly set up, the question was well-posed, and the answer is definitive. No tuning of parameters or approximation scheme will change F_fabric's monotonicity while E_J/E_c >> 1. The system is 14 sigma above the superfluid-insulator transition. The only escape is physics that changes E_J(tau) non-monotonically or drives E_J/E_c toward unity -- neither is present.

The CC QUESTION posed to me is: what does Z_fabric look like as a path integral? What are the 1-loop corrections to the W1-1 mean-field saddle? Does adiabatic suppression survive beyond mean-field? What are the Feynman diagrams for quasiparticle tunneling?

Let me compute.

---

## 2. The Fabric Partition Function as a Path Integral

### 2.1 The Action

The fabric partition function, written as a Euclidean path integral, is:

```
Z_fabric = integral D[phi_i] D[psi_k^(i)] exp(-S_E[phi, psi])
```

where i = 1,...,32 labels cells, phi_i is the U(1)_7 condensate phase on cell i, and psi_k^(i) are the 8 BCS-active fermionic (pair) modes on cell i. The Euclidean action decomposes as:

```
S_E = S_phase + S_BCS + S_Josephson + S_QP
```

**S_phase** (quantum rotor on each cell):
```
S_phase = (E_c/2) sum_i integral_0^beta d(tau_E) (d(phi_i)/d(tau_E))^2
```
This is the charging energy cost of phase fluctuations. E_c = 0.0363 M_KK at the fold. Each phi_i lives on S^1. The path integral over phi_i is an integral over winding-number sectors plus fluctuations.

**S_BCS** (intra-cell pairing, already integrated to give determinant):
```
S_BCS = -sum_i log det(G_BdG^(i))
```
where G_BdG is the Bogoliubov-de Gennes Green's function in Nambu space. At the mean-field level this gives -sum_i [sum_k log(2 cosh(beta E_qp_k / 2))] plus the condensation energy. The S55 EFT-RULES-55 Feynman rules encode the propagators and vertices from this sector: G_k(omega) = 1/(omega - eps_k + i*eta), anomalous F_k with Delta_k, vertex -iV_kl.

**S_Josephson** (inter-cell Cooper pair tunneling):
```
S_Josephson = -E_J sum_{<ij>} integral_0^beta d(tau_E) cos(phi_i - phi_j)
```
This is the XY model coupling. E_J = 7.042 M_KK per C2 bond, 50 bonds. The cosine interaction generates ALL orders of phase-difference vertices. W1-1 evaluated this at mean-field (saddle point: phi_i = phi_0 for all i, m = <cos(phi_i - phi_j)> = 0.986).

**S_QP** (quasiparticle tunneling -- the integrability-breaking channel):
```
S_QP = -sum_{<ij>,k} t_k integral_0^beta d(tau_E) [gamma_k^(i)^dag gamma_k^(j) + h.c.]
```
where gamma_k is the Bogoliubov quasiparticle operator on mode k, and t_k is the MODE-DEPENDENT tunneling amplitude. This is the term W1-2 identified as the surviving integrability-breaking channel: the isotropic Josephson (S_Josephson) preserves Richardson-Gaudin, but the anisotropic quasiparticle hopping (S_QP) does not.

The W1-2 cross-check with random inter-cell coupling gave <r> = 0.543 (GOE), confirming the diagnostic works. The anisotropic Josephson ensemble gave <r> = 0.446 -- transitional. The physical quasiparticle tunneling amplitude is:

```
t_k ~ J_C2 * (u_k^(i) * u_k^(j) - v_k^(i) * v_k^(j))
```

For identical cells: t_k ~ J_C2 * (u_k^2 - v_k^2) = J_C2 * (eps_k / E_qp_k). This is mode-dependent (ranges from 0 for eps_k = 0 to J_C2 for eps_k >> Delta). The suppression factor for modes near the Fermi surface is exp(-Delta/T_GH). W1-2 computed Delta/T_GH = 0.79 at the fold, giving exp(-0.79) = 0.45. NOT exponentially suppressed. This is the open channel.

### 2.2 The Mean-Field Saddle Point

W1-1 evaluated Z_fabric at the saddle point of S_phase + S_Josephson, obtaining the self-consistent XY mean-field. The saddle is:

```
phi_i = phi_0 (uniform)      =>     S_Josephson^(0) = -beta * N_bonds * E_J * m
m = I_1(z*E_J*m/T) / I_0(z*E_J*m/T)    =>    m = 0.986
```

The saddle-point free energy is F^(0) = F_cells + F_Josephson = -392.08 M_KK at the fold. This is the number that is monotonically increasing with tau.

### 2.3 One-Loop Corrections

The 1-loop correction is the Gaussian integral over fluctuations delta_phi_i around the saddle. Expand:

```
S_E = S^(0) + (1/2) sum_{ij} delta_phi_i * M_{ij} * delta_phi_j + O(delta_phi^3)
```

The fluctuation operator is:

```
M_{ij}(omega_n) = [E_c * omega_n^2 + z_i * E_J * m] * delta_{ij} - E_J * m * A_{ij}
```

where omega_n = 2*pi*n*T are bosonic Matsubara frequencies, z_i is the coordination of cell i, and A_{ij} is the adjacency matrix of the C2 graph.

The 1-loop correction to the free energy is:

```
F^(1) = (T/2) sum_n log det M(omega_n) = (1/2) sum_{n=1}^{31} [omega_n^BA + T*log(1 - exp(-omega_n^BA/T))]
```

where omega_n^BA = sqrt(E_c * E_J * m * lambda_n) are exactly the Bogoliubov-Anderson frequencies computed in W0-1. The 1-loop correction IS the BA phonon free energy F_BA.

W0-1 found F_BA = +7.02 M_KK at the fold (positive: zero-point energy dominates over thermal). The minimum of F_BA at tau = 0.306 has depth -7.08 M_KK. This means the 1-loop correction IS non-monotone. But it is a 1.8% perturbation on the saddle-point value |F^(0)| = 392 M_KK.

**The adiabatic suppression (P_exc = 6.6e-4 on 2 cells) IS a beyond-mean-field result.** It comes from the exact diagonalization of the coupled 2-cell Hamiltonian in W3-6. The mean-field saddle gives the thermodynamics (free energy landscape), but the excitation probability comes from the OVERLAP of the ground state at tau_initial with eigenstates at tau_final -- a quantum-mechanical quantity that requires the full spectrum.

The gap that produces adiabatic suppression is Delta_J = 13.04 M_KK (2-cell bonding-antibonding splitting). In the path integral language, this gap appears as the inverse correlation length of the phase fluctuations:

```
<delta_phi(tau_E) * delta_phi(0)> ~ exp(-Delta_J * tau_E)
```

The quench rate d(tau)/d(tau_E) must exceed Delta_J to produce excitations. In the Landau-Zener framework: P_exc ~ exp(-pi * Delta_J^2 / (2 * |dE/dt|)). With Delta_J = 13.04 and the spectral flow rate |dM/dtau| = 353 (W3-8), the LZ parameter is pi * 13.04^2 / (2 * 353) = 0.76. This gives P_exc ~ exp(-0.76) = 0.47, which is parametrically larger than the exact result 6.6e-4. The discrepancy means the LZ single-crossing formula does not apply here -- the system has 120 states and the adiabatic regime is better than LZ predicts. The exact P_exc = 6.6e-4 is the definitive number.

### 2.4 Does Adiabatic Suppression Survive Beyond Mean-Field?

The question is whether higher-loop corrections to Z_fabric can break the adiabatic protection. The answer is structured:

**2-loop (anharmonic phase fluctuations):** The O(delta_phi^4) term in the cosine expansion gives a phi^4 self-interaction with coupling lambda_4 = E_J * m / 24. The 2-loop sunset diagram contributes:

```
F^(2) ~ lambda_4^2 * T^2 * sum_{n,n'} G_BA(omega_n) * G_BA(omega_n') * G_BA(omega_n + omega_n')
```

Dimensional analysis: F^(2) ~ (E_J*m)^2 * T^2 / omega_BA^5. At the fold: ~ (7*0.99)^2 * 0.59^2 / 0.79^5 ~ 50 / 0.31 ~ 160 M_KK. This is LARGE -- comparable to F^(0). But this estimate is misleading. The expansion parameter is T/omega_BA ~ 0.59/0.79 = 0.75 (intermediate, not small). The Gaussian approximation W0-1 used is already suspect at this temperature.

However, the real test is whether the 2-loop correction has different tau-dependence than 1-loop. Since both involve the same set of BA frequencies omega_n^BA(tau) which all decrease monotonically (they track sqrt(E_J) ~ J_C2), the higher-loop terms inherit the SAME monotonicity structure. The n-loop correction scales as (E_J)^n * f(T/omega_BA), and E_J is monotonically decreasing. Each loop correction contributes an independently monotonic function of tau.

**Conclusion: adiabatic suppression survives at all loop orders in the phase-fluctuation expansion.** The protection comes from the gap structure Delta_J ~ E_J * sqrt(lambda_1), which is monotonically decreasing with tau. The gap closes as tau increases, but it remains parametrically large (13 M_KK at fold, dropping to ~1 M_KK at tau = 0.5). The excitation probability increases with tau but the 2-cell exact diagonalization (W3-6) shows P_exc = 6.6e-4 even for the sudden quench -- the maximum possible excitation. Adiabatic evolution (slow transit) produces even less excitation.

The mean-field is a saddle-point approximation. The 1-loop correction (BA phonons) is non-monotone but 1.8% of the saddle. Higher loops inherit the same E_J-monotonicity. The adiabatic protection is structural.

---

## 3. Feynman Diagram Structure for Quasiparticle Tunneling

This is the computation I want to do. The isotropic Josephson preserves integrability (W1-2 FAIL with <r> = 0.367). The surviving integrability-breaking channel is ANISOTROPIC quasiparticle tunneling -- mode-dependent single-particle hopping between cells. Let me draw the diagrams.

### 3.1 Propagators

**Bogoliubov quasiparticle** (mode k, cell i):
```
       k,i
  ---------> = G_k(omega) = 1/(omega - E_qp_k + i*eta)
```
E_qp_k = sqrt(eps_k^2 + Delta^2). At the fold: E_qp ranges from 0.464 (mode at Fermi surface) to 2.5 M_KK.

**Anomalous (Gor'kov)** propagator:
```
       k,i
  ---<<----- = F_k(omega) = Delta_k / (omega^2 - E_qp_k^2 + i*eta)
```
The double arrow denotes pair creation/annihilation.

**BA phonon** (graph mode n):
```
       n
  ~~~~~~~~ = D_n(omega) = 2*omega_n / (omega^2 - omega_n^2 + i*eta)
```
omega_n = sqrt(E_c * E_J * lambda_n). At the fold: omega ranges from 0.209 to 1.368 M_KK.

### 3.2 Vertices

**Quasiparticle tunneling** (the integrability-breaking vertex):
```
    k,i           k,j
  ----->---[t_k]----->---
```
Vertex factor: -i * t_k * A_{ij}, where t_k = J_C2 * (u_k^2 - v_k^2) = J_C2 * eps_k/E_qp_k.

Mode-dependence of t_k at the fold (using S55 EFT data, eps_k from s54_ed_sweep):
- Mode 0 (near Fermi surface): t_0 ~ J_C2 * 0.74 = 0.68 M_KK
- Mode 3 (far from FS): t_3 ~ J_C2 * 0.99 = 0.91 M_KK
- Mode 4 (universal coupler): t_4 ~ J_C2 * 0.87 = 0.80 M_KK

The mode-dependence ratio t_max/t_min ~ 0.91/0.68 = 1.34 at the fold. This is the ANISOTROPY that breaks integrability. Compare to the isotropic Josephson where all modes couple with equal amplitude -- there the ratio is exactly 1.

**QP-phonon vertex** (Andreev process at cell boundary):
```
    k,i                k,j
  ----->---            ----->---
            \  n     /
             ~~~~~~~~
```
This is the process where a quasiparticle on cell i scatters into cell j by emitting/absorbing a BA phonon. The vertex factor involves the anomalous Green's function:

```
V_{Andreev} = t_k * v_k * u_k / sqrt(2*omega_n)
```

At the fold: v_k * u_k ~ 0.34 (S52 BOGOLIUBOV-AMP data), giving V_Andreev ~ 0.68 * 0.34 / sqrt(0.42) ~ 0.36 M_KK.

### 3.3 The Leading Integrability-Breaking Process

The process that breaks integrability is quasiparticle tunneling with mode-dependent amplitudes. The tree-level T-matrix element for QP(k,cell_1) -> QP(l,cell_2) is:

```
    k,1           l,2
  ----->---[t_k]----->---[V_kl]----->---
```

But this is already elastic (k=l) at leading order. The first INELASTIC process is at 1-loop:

```
    k,1           m,1          l,2
  ----->---[V_km]----->---[t_m]----->---
              |
          m',1 |  (virtual pair fluctuation)
              |
  -----<---[V_km']----<------
```

This is the process computed in S52 BOGOLIUBOV-AMP: QP scattering mediated by virtual pair fluctuations. The S52 result was that the M-matrix is DIAGONAL (only elastic forward scattering, inelastic QP-QP = 0) for a SINGLE cell. On the fabric, the quasiparticle tunneling vertices t_k introduce mode-dependence that can generate inelastic scattering between cells.

The inelastic amplitude for QP(k, cell 1) -> QP(l, cell 2) at 1-loop on the fabric is:

```
M_fabric(k->l) = sum_m t_m * V_km * G_m(E_k) * t_m * V_ml / (E_k - E_m + i*eta)
```

Since t_m is mode-dependent (anisotropic), this is generically nonzero even when the intra-cell M is diagonal. The anisotropy ratio t_max/t_min = 1.34 provides a ~34% deviation from the isotropic (integrable) limit.

### 3.4 Suppression Factor

The quasiparticle tunneling rate is thermally suppressed by the BCS gap:

```
Gamma_QP ~ t_k^2 * N(E_F) * exp(-Delta / T_GH)
```

At the fold: Delta/T_GH = 0.464/0.590 = 0.787, so exp(-0.787) = 0.455. This is ORDER-ONE suppression, not exponential. The quasiparticle tunneling channel is OPEN.

However, the total rate must be compared to the transit rate dtau/dt. From S40 (SELF-CONSIST-40), the transit timescale is t_transit ~ 1/H ~ 1/(2*pi*T_GH) ~ 0.27 M_KK^{-1}. The quasiparticle scattering rate is Gamma_QP ~ t_k^2 * 0.455 / (bandwidth) ~ 0.68^2 * 0.455 / 6.6 ~ 0.032 M_KK.

The ratio Gamma_QP / H = 0.032 / 3.7 = 0.009. Quasiparticle tunneling is 100x slower than expansion. This means thermalization through this channel does NOT complete during transit. The GGE survives.

---

## 4. The CC = exp(-Delta_fabric * N/T) Formula

The CC QUESTION states: closures are self-tuning sectors, CC = exp(-Delta_fabric * N/T), P_exc = 6.6e-4 on 2 cells. Let me evaluate this path-integral formula.

In the Euclidean path integral, the probability of excitation above the ground state scales as:

```
P_exc ~ exp(-Delta * beta_eff) = exp(-Delta / T_eff)
```

where Delta is the gap and T_eff is the effective temperature of the quench. For the fabric:

- Delta_fabric(N_cell) scales with N_cell through the Josephson bonding. For 2 cells: Delta = 13.04 M_KK. For 32 cells: Delta ~ E_J * sqrt(lambda_max) ~ 7 * sqrt(7.3) ~ 19 M_KK (upper estimate from the top of the BA band).
- T_eff = T_GH = 0.590 M_KK at the fold.
- N = 2 cells: Delta/T = 13.04/0.59 = 22.1. Predicted P_exc ~ exp(-22.1) = 2.5e-10. Actual: 6.6e-4. The formula OVERESTIMATES the suppression by 6 orders.

The discrepancy reveals that the WKB tunneling formula does not apply. The actual excitation comes not from thermal activation over the gap but from the SUDDEN QUENCH overlap |<GS(tau_fold)|GS(tau_0)>|^2. The path-integral computation is:

```
P_exc = 1 - |<0_fold|0_initial>|^2 = 1 - |det(U^dag V)|^2
```

where U,V are the Bogoliubov transformation matrices connecting the two vacua. For 2 cells, W3-6 gives |<0|0>|^2 = 0.9993, so P_exc = 7e-4. This is a matrix element, not a Boltzmann factor.

For 32 cells with N_pair >> 1, the scaling is:

```
P_exc(N_cell) = 1 - |<0_fold|0_initial>|^2 ~ 1 - exp(-N_cell * d_overlap)
```

where d_overlap is the per-cell overlap distance. From the 2-cell data: d_overlap = -log(0.9993) = 7e-4. For 32 cells: P_exc ~ 1 - exp(-32 * 7e-4) = 1 - exp(-0.022) = 0.022. This is 33x LARGER than the 2-cell value, not smaller. More cells means MORE excitation (each cell contributes independently to the overlap deficit).

**The fabric does NOT suppress excitation. It amplifies it.** Each additional cell is an additional source of overlap deficit. The formula CC = exp(-Delta_fabric * N/T) assumes thermal equilibrium activation, but the actual mechanism is quantum-mechanical overlap in Fock space.

However, P_exc = 0.022 for 32 cells is still small. The GGE is nearly the ground state. The non-thermal relic that constitutes dark matter/dark energy in the single-cell picture (S38: P_exc = 1.000) requires a VIOLENT quench that the fabric's gap structure prevents. The CC problem is the ADIABATICITY problem: the fabric is too stiff to produce the non-equilibrium excitations that the framework needs.

---

## 5. Assessment: What the Constraint Surface Looks Like

### 5.1 Structural Walls (Permanent)

**Wall W_Josephson (NEW, S56):** In any superfluid Josephson array where E_J(tau) is monotonically decreasing and E_J/E_c >> 1, the mean-field free energy F_fabric is monotonically increasing. This wall is independent of N_cell, graph topology, or temperature (as long as T << T_c). The proof is W1-1: F_Josephson = -N_bonds * E_J * m dominates, E_J ~ J_C2^2 decreases, m is saturated. 1-loop corrections (F_BA) and chemical potential corrections (W2-1) are 0.8% and 0.2% respectively.

**Wall W_integ_Josephson (NEW, S56):** Isotropic Josephson coupling preserves Richardson-Gaudin integrability. <r> = 0.367 (Poisson) at physical coupling, confirmed by random-coupling control (<r> = 0.543, GOE). The algebraic structure is the rank-1 form H_J = -(E_J/2)(B_1^dag B_2 + h.c.) -- coupling through the TOTAL pair operator, which is the central element of the Gaudin algebra.

**Wall W_Strutinsky_fabric (NEW, S56):** Shell corrections on the fabric have gradient ratio R = 0.051, which is 14x SMALLER than the single-cell value (0.71). The Josephson ground-state energy inflates the smooth background gradient. Strutinsky stabilization is CLOSED on the fabric.

### 5.2 Surviving Channel

The sole surviving integrability-breaking channel is **anisotropic quasiparticle tunneling** (S_QP in the action). The Feynman diagram analysis in Section 3 shows:

- Mode-dependent tunneling t_k = J_C2 * eps_k/E_qp_k with anisotropy ratio 1.34
- Thermal suppression exp(-Delta/T_GH) = 0.455 (ORDER ONE, not exponential)
- Tunneling rate Gamma_QP / H = 0.009 (100x too slow for thermalization during transit)

This channel is OPEN but SLOW. It does not thermalize the GGE during transit. It might thermalize on longer timescales (post-transit, when H drops and Gamma_QP/H increases). The post-transit coherence analysis (W3-2) shows E_J/H recovers above 1 only at tau > 0.49, suggesting a late-time window where Josephson dynamics dominate expansion.

### 5.3 The Adiabaticity Problem

The deepest structural result of S56 is that the fabric's Josephson gap (13 M_KK for 2 cells, scaling upward with N_cell) protects the ground state during transit. P_exc = 6.6e-4 on 2 cells. The S38 non-thermal GGE relic (P_exc = 1.000 on 1 cell with sudden quench) requires VIOLENT symmetry breaking that the fabric suppresses.

In path integral language: the saddle-point configuration of Z_fabric at the fold is the SAME state as at tau = 0 (the ground state of the coupled system), because the gap prevents level crossing. The path integral is dominated by a single saddle with no instanton tunneling between vacua. The instanton action for crossing the Josephson gap is S_inst ~ Delta_J / T_GH ~ 22, giving a tunneling rate P ~ exp(-22) ~ 10^{-10} per cell. This is the quantitative statement that the fabric does not produce cosmological particle creation.

### 5.4 Forward Program

Three computations that would advance the constraint surface:

**F1: Quasiparticle tunneling rate on 2-cell ED.** Compute the anisotropic tunneling Hamiltonian H_QP = -sum_k t_k * gamma_k^(1)^dag * gamma_k^(2) in the same 120-dim Fock space as W1-2. Measure <r> with H = H_BCS^(1) + H_BCS^(2) + H_J + alpha_QP * H_QP. This tests whether the 1.34 anisotropy ratio is sufficient to break integrability at the fabric level. Pre-registered gate: <r> > 0.48 at alpha_QP = 1.

**F2: Finite-rate transit on 2-cell fabric.** The sudden quench (P_exc = 6.6e-4) is the UPPER BOUND on excitation. Compute the time-dependent Schrodinger equation with tau(t) evolving at the physical transit rate. If the transit is adiabatic (P_exc << 6.6e-4), the framework's non-thermal relic is suppressed on the fabric. If non-adiabatic (P_exc >> 6.6e-4 from avoided crossings), the relic survives.

**F3: N_cell scaling of Delta_J and P_exc.** Extrapolate the 2-cell gap (13.04 M_KK) to N_cell = 4, 8, 16, 32 using the known graph Laplacian eigenvalues. If Delta_J ~ sqrt(N_cell) * E_J, the gap grows and the adiabatic protection strengthens. If Delta_J saturates (due to disorder or frustration), there may be a critical N_cell where P_exc ~ O(1).

---

## Closing

The path integral perspective makes the S56 result clean. The fabric partition function Z_fabric has a well-defined saddle (uniform phase, XY mean-field), well-defined 1-loop corrections (BA phonons = Gaussian fluctuations of delta_phi around the saddle), and a definitive structural result: the saddle-point free energy is monotonically increasing because E_J(tau) is monotonically decreasing.

The 1-loop correction F_BA is the first genuinely non-monotone contribution in 56 sessions. Its minimum at tau = 0.306 is real physics -- the competition between zero-point energy and thermal entropy of 31 collective modes on a 32-cell graph. It is also energetically irrelevant: 7 M_KK against a 350 M_KK Josephson background.

The discovery that the Josephson gap (13 M_KK on 2 cells) adiabatically protects the ground state (P_exc = 6.6e-4) reframes the CC problem. It is no longer "how do we stabilize tau?" It is: "how does the fabric produce the non-equilibrium excitations that the cosmological constant requires?" The quasiparticle tunneling channel is the answer -- it is anisotropic (breaks integrability), thermally unsuppressed (exp(-0.79) = 0.45), but SLOW (Gamma/H = 0.009). Whether it thermalizes post-transit, when H drops and the ratio inverts, is the decisive next computation.

The fabric is a superfluid that does not want to be excited. The universe requires excitation. The tension between these two facts is the constraint surface of the CC problem. S56 has measured the walls of that surface with quantitative precision.
