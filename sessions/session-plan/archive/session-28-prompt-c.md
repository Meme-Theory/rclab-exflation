# Session 28c: Constraint Chain Completion + Structural Gates

**Date**: 2026-02-27
**Depends on**: Session 28a (KC-1 verdict, torsionful BCS), Session 28b (C-3 order-one, L-7 self-consistent tau-T, S-3 Hessian)
**Input data**:
- `tier0-computation/s28a_bogoliubov_coefficients.npz` (KC-1 output: |beta_k|^2)
- `tier0-computation/s23a_eigenvectors_extended.npz` (D_K eigenvectors for mode overlaps)
- `tier0-computation/s23a_kosmann_singlet.npz` (Kosmann coupling data)
- `tier0-computation/s27_torsion_gap_gate.npz` (D_can eigenvalues)
- `tier0-computation/s27_multisector_bcs.npz` (multi-sector BCS data)
- `tier0-computation/s28a_torsionful_bcs.npz` (torsionful BCS, if available)
- `tier0-computation/s28b_order_one.npz` (C-3 result, for C-6 gating)
- `tier0-computation/r20a_riemann_tensor.npz` (Riemann tensor for geodesic computation)
- `tier0-computation/tier1_dirac_spectrum.py` (geometry infrastructure)

## Motivation

Session 28c completes the Constraint Chain (KC-2 through KC-5) if KC-1 passed, and executes structural gates that probe the deep mathematical infrastructure of the framework. KC-2 (the 1D phonon-phonon T-matrix) is the first genuinely new computation in the phonon collision program: it computes 4-point mode function overlaps on SU(3) to determine whether phonon-phonon scattering establishes a thermalization bottleneck. The structural gates -- 12D spectral triple axioms (C-6), Duistermaat-Guillemin periodic orbits (E-3), Berry curvature at sector transitions (S-4), and sector count convergence (L-8) -- are independent of the Constraint Chain and can run regardless of KC-1 outcome.

# 0. OPERATIONAL RULES

## CONDITIONAL BRANCHING

The Constraint Chain computations KC-2 through KC-5 are strictly conditional:

- **If KC-1 PASSED**: KC-2 is the top priority. KC-3 through KC-5 follow if KC-2 passes.
- **If KC-1 CLOSED**: Drop all KC computations. Session 28c becomes structural gates only (C-6, E-3, S-4, L-8).
- **If KC-1 INCONCLUSIVE**: KC-2 runs but with reduced priority (structural gates first).

Similarly, C-6 (12D axiom verification) is gated by C-3 (order-one condition from 28b):

- **If C-3 PASSED**: C-6 is high priority -- the full 12D spectral triple may be valid.
- **If C-3 FAILED**: C-6 is informational only -- the 12D triple fails at the algebra level.

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s28c_`

## REQUIRED READING

ALL agents:
1. **Session 28a synthesis**: `sessions/session-28/session-28a-synthesis.md` -- KC-1 verdict, torsionful BCS verdict.
2. **Session 28b synthesis**: `sessions/session-28/session-28b-synthesis.md` -- C-3, L-7, S-3 verdicts.
3. **Master collab, Section III**: Constraint Chain definition (KC-1 through KC-5), Constraint Conditions, critical caveats.
4. **Einstein collab**: `sessions/session-27/session-27-einstein-collab.md` -- Duistermaat-Guillemin periodic orbits, EIH coupling.
5. **MathVariables**: `sessions/framework/MathVariables.md` -- Sections 1.2-1.4 (Jensen deformation, connection), 6 (KK reduction), 8 (topological invariants).

---

# I. COMPUTATIONS: Constraint Chain (CONDITIONAL ON KC-1 PASS)

### 28c-1: KC-2 1D Phonon-Phonon T-Matrix

**What**: Compute the 4-point overlap integrals of SU(3) Dirac mode functions that determine the phonon-phonon scattering amplitude in the 1D effective theory. The 1D phonon collision mechanism requires that phonon-phonon scattering is efficient enough to establish a thermalization bottleneck (scattering rate W comparable to or exceeding the decay rate Gamma). If W << Gamma, phonons decay before they can scatter and the bottleneck mechanism fails.

**Input**:
- `tier0-computation/s23a_eigenvectors_extended.npz` (D_K eigenvectors per mode)
- Spectral action a_4 coefficient for the quartic vertex
- `tier0-computation/tier1_dirac_spectrum.py` (mode functions)

**Script**: `s28c_phonon_tmatrix.py`

**Method**:
1. The 1D effective interaction arises from integrating the 4D spectral action vertex over the internal SU(3):
   ```
   V_{1234} = integral_{SU(3)} psi_1^*(x) psi_2^*(x) psi_3(x) psi_4(x) dvol
   ```
   where psi_k(x) are Dirac mode functions on SU(3) at fixed tau.
2. Load eigenvectors from s23a data (or recompute for D_can if 28a-7 showed MAJOR PASS).
3. The 4-point overlap factorizes in Peter-Weyl: psi_k in sector (p_k, q_k) gives selection rules from the Clebsch-Gordan decomposition of (p_1,q_1) x (p_2,q_2) x (p_3*,q_3*) x (p_4*,q_4*).
4. Compute V_{1234} for the 20 lowest modes at tau = 0.15, 0.25, 0.35.
5. The T-matrix element:
   ```
   T_{12->34} = V_{1234} + sum_n V_{12n} * G_n * V_{n34}  (Born approximation + 1-loop)
   ```
   where G_n = 1/(E_1 + E_2 - E_n + i*epsilon) is the intermediate propagator.
6. Compute the scattering rate:
   ```
   W = (2*pi) * sum_{3,4} |T_{12->34}|^2 * delta(E_1+E_2-E_3-E_4) * n_3 * n_4
   ```
   using phase space from the 1D density of states.
7. Compare W to the decay rate Gamma (from single-particle spectral width, if computable from the eigenvalue data).

**Output**: `s28c_phonon_tmatrix.npz`, `s28c_phonon_tmatrix.png`

**Gate KC-2**:
- PASS: W > 0.1 * Gamma -- scattering rate sufficient for bottleneck
- CLOSED: W < 0.01 * Gamma -- phonons decay before scattering, no bottleneck
- INCONCLUSIVE: W in [0.01, 0.1] * Gamma

**Agent**: phonon-exflation-sim

**Implementation note**: The 4-point overlap integral on SU(3) can be computed analytically using the Peter-Weyl decomposition and SU(3) Clebsch-Gordan coefficients. For modes in sectors (p_1,q_1) and (p_2,q_2), the product decomposes via the tensor product:
```
(p_1,q_1) x (p_2,q_2) = direct sum of (p,q) with known multiplicities
```
The overlap is nonzero only if (p_3,q_3) x (p_4,q_4) contains a component in the same decomposition. This provides strong selection rules that limit the number of nonzero V_{1234}.

**Closure Audit Context (Baptista)**: The Constraint Chain (KC-1 through KC-5) is ORTHOGONAL to the connection ambiguity. It tests whether parametric amplification creates phonons, whether they scatter to form a bottleneck, and whether mu_eff fills the spectral gap. These questions apply regardless of which Dirac operator is used — though the spectral gap to be filled IS connection-dependent (weaker for D_can). If 28a-7 showed MAJOR PASS for D_can BCS, the T-matrix should be computed in the D_can eigenbasis since that's the spectrum where condensation occurs.

---

### 28c-2: KC-3 Steady-State mu_eff (Conditional on KC-2 PASS)

**What**: Solve the kinetic equation balancing phonon injection (from KC-1), phonon-phonon scattering (from KC-2), and phonon decay to determine the steady-state effective chemical potential mu_eff. If mu_eff < lambda_min, the spectral gap is not filled and BCS condensation cannot occur.

**Input**: KC-1 output (injection rates |beta_k|^2), KC-2 output (scattering rates W)

**Script**: `s28c_steady_state_mu.py`

**Method**:
1. Kinetic equation for the phonon occupation number n_k:
   ```
   dn_k/dt = Gamma_inject(k) - Gamma_decay(k) * n_k + C_scatter[n](k)
   ```
   where C_scatter is the collision integral from KC-2.
2. Steady state: dn_k/dt = 0. Solve for n_k.
3. The effective chemical potential: mu_eff defined by n_k = 1/(exp((E_k - mu_eff)/T_eff) - 1) fitted to the steady-state distribution.
4. Report mu_eff as a function of the drive strength (dtau/dt).

**Output**: `s28c_steady_state_mu.npz`, `s28c_steady_state_mu.txt`

**Gate KC-3**:
- PASS: mu_eff > lambda_min for physically reasonable drive rates
- CLOSED: mu_eff < 0.5 * lambda_min even at maximum drive

**Closure Audit Context (Baptista)**: This Constraint Chain computation determines whether dynamically generated mu_eff exceeds the spectral gap. It directly addresses the mu=0 obstruction that powered **Closure 17 (K-1e: BCS at mu=0, Session 23a)**: M_max(mu=0) = 0.077-0.149 but M_max(mu=lambda_min) ~ 11. The Constraint Chain exists to bypass Closure 17 by filling the gap dynamically rather than by changing the operator. The spectral gap lambda_min is connection-dependent (33-78% weaker for D_can), so KC-3 should use lambda_min appropriate to whichever operator showed BCS promise. If D_can is the active channel, the weaker gap means mu_eff needs to be correspondingly smaller to trigger condensation.

**Agent**: phonon-exflation-sim

---

### 28c-3: KC-4 Luttinger Parameter K (Conditional on KC-2 PASS)

**What**: Compute the Luttinger liquid parameter K for the 1D phonon system. K < 1 indicates attractive interactions (fermionization toward Tonks-Girardeau regime). K = 1 is non-interacting. K >> 1 indicates weak repulsive interactions (no Fermi surface, BCS blocked).

**Input**: 1D density and scattering length from KC-2

**Script**: `s28c_luttinger.py`

**Method**:
1. The Luttinger parameter:
   ```
   K = pi / sqrt(1 + 4/(n_1D * a_1D))
   ```
   where n_1D is the 1D phonon density and a_1D is the effective 1D scattering length.
2. n_1D: from the steady-state occupation at mu_eff (or estimated from injection rates).
3. a_1D: from the s-wave scattering amplitude of KC-2 T-matrix, reduced to 1D.
4. Compute K as a function of the drive strength.

**Output**: `s28c_luttinger.txt`

**Gate KC-4**:
- PASS: K < 1 (attractive, fermionization possible)
- CLOSED: K > 3 (weakly repulsive, no Fermi surface)

**Closure Audit Context (Baptista)**: This Constraint Chain computation tests whether the 1D phonon system supports a Fermi surface (K < 1, attractive). It is a novel mechanism test with no specific closure to retest. The Luttinger parameter depends on scattering amplitudes from KC-2 and phonon density from KC-1/KC-3 — both derived from the eigenvalue spectrum and therefore connection-dependent. The Baptista audit's framework observation §4 ("torsion affects spectral action but not gauge couplings") means the 1D effective theory inherits connection-dependence through the mode functions and spectral gap, but not through the gauge coupling structure.

**Agent**: phonon-exflation-sim

---

### 28c-4: KC-5 BCS Gap with van Hove DOS (Conditional on KC-3 + KC-4 PASS)

**What**: Solve the BCS gap equation with the 1D density of states g(omega) ~ 1/sqrt(omega - omega_min) (van Hove singularity at the band edge). The enhanced DOS at the van Hove point amplifies Cooper pairing relative to the flat-DOS estimate used in S23a.

**Input**: KC-3 mu_eff, KC-4 Fermi surface, Kosmann coupling from s23a

**Script**: `s28c_bcs_van_hove.py`

**Method**:
1. The 1D BCS gap equation with van Hove DOS:
   ```
   1 = V * integral_0^omega_D g(omega) / (2*sqrt((omega-mu)^2 + Delta^2)) d(omega)
   ```
   where g(omega) = 1/sqrt(omega - omega_min) * theta(omega - omega_min).
2. V: effective pairing from Kosmann coupling projected onto the 1D Fermi surface.
3. Solve self-consistently for Delta.
4. Compare to the flat-DOS result from S23a.

**Output**: `s28c_bcs_van_hove.npz`, `s28c_bcs_van_hove.txt`

**Gate KC-5**:
- PASS: Delta > 0 (pairing occurs with van Hove enhancement)
- CLOSED: Delta = 0 (pairing too weak even with enhanced DOS)

**Closure Audit Context (Baptista)**: This is the terminal Constraint Chain gate, retesting **Closure 17 (K-1e: BCS at mu=0, Session 23a)** in a fundamentally different regime — with dynamically generated mu from the Constraint Chain and van Hove-enhanced 1D density of states. The van Hove singularity g(omega) ~ 1/sqrt(omega - omega_min) provides logarithmic amplification of Cooper pairing at the band edge, exceeding the flat-DOS estimate in Session 23a. If KC-5 passes, Closure 17 is circumvented through a complete physical mechanism chain (parametric amplification → thermalization → gap filling → BCS) rather than by operator substitution. This mechanism is connection-dependent only through the spectral gap and mode functions.

**Agent**: phonon-exflation-sim

---

# II. COMPUTATIONS: STRUCTURAL GATES (UNCONDITIONAL)

### 28c-5: C-6 12D Spectral Triple Axiom Verification

**What**: Verify the 7 axioms of a spectral triple for the product geometry M^4 x (SU(3), g_tau, D_can). This is the gate DP-1: if all 7 axioms hold, the 12D geometry defines a valid noncommutative space in the sense of Connes.

**Input**: `tier0-computation/r20a_riemann_tensor.npz` (metrics), Session 8 J matrix, D_can from s27

**Script**: `s28c_12d_axioms.py`

**Method**: Verify each axiom at tau = 0, 0.15, 0.30:
1. **Dimension** (axiom 1): The spectral dimension from the Weyl asymptotics of D = D_M + D_can is 4 + 8 = 12.
2. **Regularity** (axiom 2): A and [D, A] are bounded operators on the domain of D. Check for a set of generators.
3. **Finiteness** (axiom 3): The space of smooth vectors is a finitely generated projective A-module.
4. **Reality** (axiom 4): J D = epsilon D J, J gamma = epsilon'' gamma J, J^2 = epsilon' I. Check KO-dimension signs for dim=12 (mod 8 = 4).
5. **First order** (axiom 5): [[D, a], J b J^{-1}] = 0 for all a, b in A. This is C-3 extended to the full 12D operator.
6. **Orientation** (axiom 6): Existence of a Hochschild cycle c such that pi(c) = gamma.
7. **Poincare duality** (axiom 7): The intersection form is non-degenerate.

For axioms 4-5, numerical verification at machine precision. For axioms 1-3, 6-7, structural/algebraic arguments supplemented by numerical checks.

**Output**: `s28c_12d_axioms.npz`, `s28c_12d_axioms.txt`

**Gate C-6 (= DP-1)**:
- PASS: All 7 axioms verified -- 12D spectral triple is valid
- FAIL: Any axiom violated -- 12D geometry is not a spectral triple

**Closure Audit Context (Baptista)**: The product spectral triple axioms are algebraic — they hold or fail regardless of connection. Closure 8 (Pfaffian Z_2, Session 17c) is flagged NEEDS REVIEW at low priority: D_can has accidental zero modes in trivial sector (rho=0, not topological). The Pfaffian of D_can has not been computed. If C-6 is verified, the Pfaffian check is a natural zero-cost byproduct — include it. 15/21 closes are CONFIRMED CLOSED regardless of connection (block-diag, Weyl, metric identities, Clifford traces). No computation in 28c can or should attempt to revive inter-sector coupling, rolling quintessence, or Higgs-sigma portal.

**Agent**: phonon-exflation-sim

---

### 28c-6: E-3 Duistermaat-Guillemin Periodic Orbits

**What**: Compute the lengths of closed geodesics on (SU(3), g_tau) and their contribution to the spectral action via the Duistermaat-Guillemin trace formula. If the non-perturbative (periodic orbit) corrections exceed 4% of the perturbative (Seeley-DeWitt) spectral action at the KK scale, they cannot be neglected and may provide the non-perturbative minimum that perturbation theory cannot.

**Input**: Jensen metric g_tau from `tier0-computation/tier1_dirac_spectrum.py`

**Script**: `s28c_periodic_orbits.py`

**Method**:
1. The geodesics on (SU(3), g_tau) are governed by the geodesic equation:
   ```
   d^2x^a/ds^2 + Gamma^a_{bc}(tau) dx^b/ds dx^c/ds = 0
   ```
2. For the bi-invariant metric (tau=0): all geodesics are group translations exp(tX), with period 2*pi/|X| for unit X. The closed geodesic lengths are 2*pi*n for integer n.
3. For tau > 0: the metric is left-invariant but not bi-invariant. Geodesics are NOT group translations. Use the Euler-Arnold equations on su(3)* (the dual Lie algebra, with the coadjoint action).
4. Numerically integrate the Euler-Arnold equations to find periodic orbits at tau = 0.15, 0.25, 0.35.
5. Compute the Maslov index and the determinant of the stability matrix for each orbit.
6. The Duistermaat-Guillemin contribution to the trace of the wave operator:
   ```
   Tr cos(t*sqrt(-Delta)) ~ sum_{gamma} A_gamma * delta(t - L_gamma)
   ```
   where L_gamma is the geodesic length and A_gamma encodes the stability.
7. Estimate the ratio of the periodic orbit correction to the Seeley-DeWitt smooth part at Lambda = M_KK.

**Output**: `s28c_periodic_orbits.npz`, `s28c_periodic_orbits.png`

**Gate E-3**: Diagnostic. Non-perturbative correction > 4% at KK scale indicates periodic orbits matter.

**Closure Audit Context (Baptista)**: This structural gate probes non-perturbative corrections from closed geodesics, relating to **Closure 5 (Seeley-DeWitt a_2/a_4, Session 20a)** and **Closure 19 (V-1: V_spec monotone, Session 24a)** — both perturbative closes from the smooth heat kernel expansion. The Duistermaat-Guillemin formula captures OSCILLATORY corrections that the Seeley-DeWitt expansion misses. The Baptista audit flags both Closure 5 and Closure 19 as NEEDS REVIEW for D_can. For D_K specifically, periodic orbit corrections could introduce non-monotonic structure even in the LC spectral action, potentially reopening Closure 19 non-perturbatively. Geodesics are determined by the Levi-Civita connection; the D_can analog would involve heat kernel corrections from the Casimir operator, which is a different computation.

**Agent**: phonon-exflation-sim

---

### 28c-7: S-4 Berry Curvature at Sector Transitions

**What**: Compute the Berry curvature of the BCS ground state wavefunction at the sector boundary transitions identified in S27 (where sectors switch from subcritical to supercritical). A quantized Berry phase (pi or 2*pi) at a transition would indicate topological protection of the BCS phase.

**Input**: BCS solutions from s27 or s28a (depending on which basis), sector transition tau values from S27 addendum

**Script**: `s28c_berry_bcs.py`

**Method**:
1. At each sector transition (where M_max crosses 1):
   - Parameterize the BCS ground state |Psi(tau)> along a path in tau through the transition.
   - Compute the Berry connection: A(tau) = -i * <Psi(tau)|d/dtau|Psi(tau)>.
   - Integrate: gamma = integral A(tau) dtau over a closed loop around the transition point.
2. Use the self-consistent Delta(tau) from s27 (or s28a torsionful BCS if available).
3. For the re-entrant (2,0) sector: compute the Berry phase around the full re-entrant cycle (in -> out -> in transition).
4. A quantized Berry phase gamma = pi (mod 2*pi) indicates a Z_2 topological transition.

**Output**: `s28c_berry_bcs.npz`, `s28c_berry_bcs.png`

**Gate S-4**: Diagnostic. Quantized Berry phase at sector transitions indicates topological protection, distinguishing the multi-sector BCS system from a smooth crossover.

**Closure Audit Context (Baptista)**: Berry phase of the BCS ground state depends on eigenvalue flow, which IS connection-dependent. If 28a computed D_can BCS, S-4 should use D_can results — the Berry curvature at sector transitions may be quantitatively different in the torsionful eigenbasis.

**Agent**: phonon-exflation-sim

---

### 28c-8: L-8 Sector Count Convergence at p+q <= 4

**What**: Extend the multi-sector BCS computation from S27 (p+q <= 3, 9 sectors) to p+q <= 4 (adding (4,0), (0,4), (3,1), (1,3), (2,2) = 5 new sectors, 14 total). Verify that the F_total profile converges: if higher sectors contribute negligibly, the physical sector count is 9 and the S27 result is definitive. If higher sectors change the qualitative picture, p+q <= 3 was insufficient.

**Input**: `tier0-computation/s27_multisector_bcs.py` (BCS solver, extend sector list), `tier0-computation/tier1_dirac_spectrum.py`

**Script**: `s28c_sector_convergence.py`

**Method**:
1. For each new sector (4,0), (0,4), (3,1), (1,3), (2,2):
   - Mode counts: dim(4,0) = 35, dim(3,1) = 24, dim(2,2) = 27.
   - Multiplicities: mult(4,0) = 35^2 = 1225, mult(3,1) = 24^2 = 576, mult(2,2) = 27^2 = 729.
   - NOTE: (2,2) has mult = 729, comparable to (2,1) at 450. This sector could matter.
2. Compute D_K eigenvalues, Kosmann matrices K_a, and V_nm pairing matrix for each new sector.
3. Run BCS at mu = {0, 0.5, 1.0, 1.2} * lambda_min, tau = {0, 0.15, 0.25, 0.35, 0.50}.
4. Compute M_max per sector. Check: are new sectors above or below threshold?
5. Update F_total with new sectors. Compare to S27 F_total.
6. Convergence criterion: |F_total(p+q<=4) - F_total(p+q<=3)| / |F_total(p+q<=3)| < 0.10 at the interior minimum.

**Output**: `s28c_sector_convergence.npz`, `s28c_sector_convergence.png`

**Gate L-8**:
- PASS (converged): New sectors contribute < 10% correction to F_total -- S27 result is robust
- FAIL (not converged): New sectors change F_total qualitatively (new minimum, shifted location)

**Closure Audit Context (Baptista)**: Higher-sector M_max depends on the operator used. If 28a used D_can for the torsionful BCS and showed qualitatively different results, L-8 should extend D_can (not D_K) to p+q <= 4 for consistency. The convergence question is: do the 5 new sectors change the D_can BCS picture, not the D_K picture that S27 already established.

**Agent**: phonon-exflation-sim

---

# III. EXECUTION ORDER

```
Unconditional (run immediately, in parallel):
  28c-5 (C-6)  ── 12D axiom verification
  28c-6 (E-3)  ── periodic orbits
  28c-7 (S-4)  ── Berry curvature at transitions
  28c-8 (L-8)  ── sector convergence

Conditional on KC-1 PASS (from 28a):
  28c-1 (KC-2) ── phonon T-matrix (top priority if KC-1 passed)

Conditional on KC-2 PASS:
  28c-2 (KC-3) ── steady-state mu_eff
  28c-3 (KC-4) ── Luttinger parameter K

Conditional on KC-3 + KC-4 PASS:
  28c-4 (KC-5) ── BCS gap with van Hove DOS

Dependency chain:
  KC-1 (28a) --> KC-2 (28c) --> KC-3 (28c) --> KC-5 (28c)
                            \--> KC-4 (28c) --/
```

---

# IV. SESSION VERDICT CRITERIA

### Constraint Chain Outcome Table

| Scenario | KC-1 | KC-2 | KC-3 | KC-4 | KC-5 | Verdict |
|:---------|:-----|:-----|:-----|:-----|:-----|:--------|
| Full pass | PASS | PASS | PASS | PASS | PASS | 1D phonon mechanism viable. Framework reopens. |
| Drive exists, no scattering | PASS | CLOSED | -- | -- | -- | Phonons created but cannot thermalize. mechanism closed. |
| Scattering but no mu | PASS | PASS | CLOSED | -- | -- | Bottleneck exists but mu_eff too low. Marginal. |
| Fermionization fails | PASS | PASS | -- | CLOSED | -- | No Fermi surface. BCS blocked despite mu. |
| Pairing too weak | PASS | PASS | PASS | PASS | CLOSED | All prerequisites met but coupling insufficient. |
| No drive at all | CLOSED | -- | -- | -- | -- | Parametric amplification absent. Drop mechanism. |

### Structural Gate Outcomes

| Gate | PASS consequence | FAIL consequence |
|:-----|:----------------|:-----------------|
| C-6 (12D axioms) | Full NCG framework applies to D_can on M^4 x SU(3) | D_can does not define a valid spectral triple |
| E-3 (periodic orbits) | Non-perturbative corrections significant at KK scale | Perturbative approach adequate |
| S-4 (Berry phase) | Topological protection of BCS transitions | Smooth crossover, no protection |
| L-8 (convergence) | S27 multi-sector result is robust | Higher sectors change the picture |

**28c is successful if it either (a) completes the Constraint Chain through KC-5 with a definitive verdict, or (b) establishes that the structural gates (C-6, L-8) confirm or refute the existing computational picture.**

---

# V. OUTPUT FILES

| File | Computation | Producer |
|:-----|:-----------|:---------|
| `tier0-computation/s28c_phonon_tmatrix.py` | KC-2 | phonon-sim |
| `tier0-computation/s28c_phonon_tmatrix.npz` | KC-2 data | phonon-sim |
| `tier0-computation/s28c_phonon_tmatrix.png` | KC-2 plot | phonon-sim |
| `tier0-computation/s28c_steady_state_mu.py` | KC-3 | phonon-sim |
| `tier0-computation/s28c_steady_state_mu.npz` | KC-3 data | phonon-sim |
| `tier0-computation/s28c_steady_state_mu.txt` | KC-3 verdict | phonon-sim |
| `tier0-computation/s28c_luttinger.py` | KC-4 | phonon-sim |
| `tier0-computation/s28c_luttinger.txt` | KC-4 verdict | phonon-sim |
| `tier0-computation/s28c_bcs_van_hove.py` | KC-5 | phonon-sim |
| `tier0-computation/s28c_bcs_van_hove.npz` | KC-5 data | phonon-sim |
| `tier0-computation/s28c_bcs_van_hove.txt` | KC-5 verdict | phonon-sim |
| `tier0-computation/s28c_12d_axioms.py` | C-6 | phonon-sim |
| `tier0-computation/s28c_12d_axioms.npz` | C-6 data | phonon-sim |
| `tier0-computation/s28c_12d_axioms.txt` | C-6 verdict | phonon-sim |
| `tier0-computation/s28c_periodic_orbits.py` | E-3 | phonon-sim |
| `tier0-computation/s28c_periodic_orbits.npz` | E-3 data | phonon-sim |
| `tier0-computation/s28c_periodic_orbits.png` | E-3 plot | phonon-sim |
| `tier0-computation/s28c_berry_bcs.py` | S-4 | phonon-sim |
| `tier0-computation/s28c_berry_bcs.npz` | S-4 data | phonon-sim |
| `tier0-computation/s28c_berry_bcs.png` | S-4 plot | phonon-sim |
| `tier0-computation/s28c_sector_convergence.py` | L-8 | phonon-sim |
| `tier0-computation/s28c_sector_convergence.npz` | L-8 data | phonon-sim |
| `tier0-computation/s28c_sector_convergence.png` | L-8 plot | phonon-sim |
| `tier0-computation/s28c_gate_verdicts.txt` | All gate verdicts | coordinator |
| `sessions/session-28/session-28c-synthesis.md` | Final synthesis | coordinator |
