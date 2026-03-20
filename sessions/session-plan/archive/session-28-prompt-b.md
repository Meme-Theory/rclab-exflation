# Session 28b: Landau Diagnostics + NCG Axiom Gates

**Date**: 2026-02-27
**Depends on**: Session 28a (torsionful BCS verdict, KC-1 verdict, thermal spectral action), Session 27 (multi-sector BCS data)
**Input data**:
- `tier0-computation/s27_multisector_bcs.npz` (9 sectors, 9 tau, 12 mu -- M_max, F_cond, Delta)
- `tier0-computation/s27_torsion_gap_gate.npz` (D_can and D_K eigenvalues, eigenvectors)
- `tier0-computation/s28a_torsionful_bcs.npz` (torsionful BCS results, if 28a produced them)
- `tier0-computation/s28a_thermal_spectral_action.npz` (thermal F(tau; T), from 28a L-1)
- `tier0-computation/tier1_dirac_spectrum.py` (geometry and operator infrastructure)
- Session 8 J matrix data (real structure operator, from `tier0-computation/`)

## Motivation

Session 28b conducts the deep diagnostics that characterize the BCS phase structure and test whether the torsionful Dirac operator satisfies the NCG axiom framework. The Landau diagnostics (L-3, L-5, L-6, L-9) probe the condensed matter physics of the multi-sector system: relaxation times, Pomeranchuk instabilities, quasiparticle renormalization, and first-order transition signatures. The NCG gate (C-3) tests whether the algebraic part of D_can satisfies the order-one condition -- the structural prerequisite for building a full noncommutative geometry from the torsionful operator. The self-consistent (tau, T) minimization (L-7) is the combined thermal+BCS computation that Landau's two-transition scenario requires. Together, these determine whether the torsionful BCS system has the right condensed matter and algebraic properties to serve as a physical mechanism.

---

# 0. OPERATIONAL RULES

## CONDITIONAL ROUTING

The priority ordering within 28b depends on 28a results:

- **If E-4/S-1/L-4 gave MAJOR PASS** (D_can BCS works at mu=0): All Landau diagnostics (L-3 through L-9) run on D_can spectrum. C-3 becomes critical -- if D_can satisfies the order-one condition, the full NCG + BCS package is viable.
- **If E-4/S-1/L-4 gave MINOR PASS or CLOSED**: Landau diagnostics run on D_K spectrum (existing s27 data). C-3 is still computed but becomes less urgent.
- **If L-1 gave PASS** (thermal minimum exists): L-7 becomes top priority. The two-transition scenario (thermal condensation at high T, BCS at low T) requires the self-consistent (tau, T) map.
- **If L-1 gave CLOSED**: L-7 runs in reduced form (BCS-only at T=0, no thermal channel).

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s28b_`

## REQUIRED READING

ALL agents:
1. **Session 28a synthesis**: `sessions/session-28/session-28a-synthesis.md` -- gate verdicts from 28a.
2. **Session 27 wrapup, Section 3**: Multi-sector BCS results, phase transition sequence, Baptista addenda.
3. **Landau collab**: `sessions/session-27/session-27-landau-collab.md` -- Two-transition scenario, relaxation times, quasiparticle weight, self-consistent (tau, T).
4. **Connes collab**: `sessions/session-27/session-27-connes-collab.md` -- Order-one condition, structural monotonicity, 12D axiom framework.
5. **MathVariables**: `sessions/framework/MathVariables.md` -- Sections 2 (Dirac operators), 4 (BCS variables), 11 (walls and traps).

---

# I. COMPUTATIONS

### 28b-1: C-3 Order-One Condition for D_can

**What**: Test whether M_Lie (the algebraic/Lie-derivative part of D_can) satisfies the NCG order-one condition: [[M_Lie, a_F], J b_F J^{-1}] = 0 for all a_F, b_F in the finite algebra A_F. This is the structural prerequisite for D_can to define a valid noncommutative geometry. If it holds, the entire NCG apparatus (spectral action, Connes distance formula, gauge invariance) applies to the torsionful operator.

**Input**: Session 8 J matrix (real structure operator), M_Lie from `s27_torsion_gap_gate.py` infrastructure, A_F generators.

**Script**: `s28b_order_one_condition.py`

**Method**:
1. Load (or reconstruct) the real structure operator J from Session 8 data.
2. Construct M_Lie at tau = 0, 0.15, 0.30 in the (0,0) singlet sector.
3. The finite algebra A_F acts on Psi_+ = C^16 (the positive chirality subspace). Generators: a_F = {1, lambda_a} (identity + 8 Gell-Mann matrices).
4. For each pair (a_F, b_F) in the algebra:
   - Compute [M_Lie, a_F] (the commutator).
   - Compute J * b_F * J^{-1} (the J-conjugated element).
   - Compute the double commutator [[M_Lie, a_F], J b_F J^{-1}].
   - Record the Frobenius norm.
5. Gate criterion: maximum norm across all pairs.

**Output**: `s28b_order_one.npz`, `s28b_order_one.txt`

**Gate C-3**:
- PASS: ||[[M_Lie, a_F], J b_F J^{-1}]|| < 10^{-10} for all pairs -- order-one condition satisfied at machine precision
- FAIL: Maximum norm > 0.01 -- order-one condition violated
- MARGINAL: Maximum norm in [10^{-10}, 0.01] -- approximate satisfaction

**Closure Audit Context (Baptista)**: Block-diagonality is UNIVERSAL — the proof depends on left-invariance, not connection choice. Both D_K and D_can are block-diagonal. C-3 therefore tests a genuinely NEW question: whether M_Lie satisfies the NCG order-one axiom, not a rehash of D_K results. If PASS, the entire NCG apparatus (spectral action, Connes distance formula, gauge invariance) applies to D_can — this is the algebraic prerequisite for the torsionful spectral action (28a-4) to have physical meaning.

**Agent**: phonon-exflation-sim

---

### 28b-2: L-3 Landau-Khalatnikov Relaxation Times

**What**: Compute the relaxation time tau_LK for the BCS order parameter in each sector as a function of the Jensen parameter tau. In Landau-Khalatnikov theory, the relaxation time diverges at a second-order phase transition (critical slowing down) and is finite elsewhere. If the (2,0) sector shows re-entrant behavior (supercritical -> subcritical -> supercritical, as found in S27), the relaxation time should show two divergences, trapping the modulus between them.

**Input**: `tier0-computation/s27_multisector_bcs.npz` (M_max per sector per tau)

**Script**: `s28b_relaxation_times.py`

**Method**:
1. Load M_max(sector, tau, mu) from s27 data.
2. Near the BCS transition (M_max = 1), the relaxation time scales as:
   ```
   tau_LK ~ 1 / |M_max - 1|
   ```
   (mean-field critical exponent z*nu = 1 for BCS).
3. For each sector at mu = lambda_min: compute tau_LK(tau) by interpolating M_max(tau).
4. Identify divergences (where M_max crosses 1). These are the sector-specific critical tau values.
5. **Key diagnostic**: The (2,0) sector shows re-entrant behavior (S27 addendum: supercritical at tau=0, subcritical for tau in [0.10, 0.40], supercritical at tau=0.50). Verify the two critical tau values where M_max crosses 1.
6. If torsionful BCS data is available (28a-7): repeat with D_can M_max values.

**Output**: `s28b_relaxation_times.npz`, `s28b_relaxation_times.png`

**Gate L-3**: Diagnostic. Re-entrant (2,0) sector with two relaxation-time divergences indicates a dynamical tau-trapping window between the two transitions.

**Closure Audit Context (Baptista)**: This diagnostic does not directly retest a specific closure but relates to **Closure 14 (clock closure, Session 22d)**: any non-zero tau_dot violates the atomic clock bound by 15,000x, so any stabilization mechanism must freeze tau exactly (tau_dot = 0). The Landau-Khalatnikov relaxation time tau_LK diverges at second-order BCS transitions (critical slowing down), producing tau_dot → 0 naturally at the transition — consistent with the clock constraint. If re-entrant behavior in (2,0) is confirmed, two divergences would bracket a tau-trapping window. If torsionful BCS data (28a-7) is available, repeating with D_can values tests whether re-entrant behavior is connection-dependent.

**Agent**: phonon-exflation-sim

---

### 28b-3: L-5 Per-Sector Pomeranchuk Map

**What**: Compute the Pomeranchuk stability parameter f_l for each sector as a function of tau. Session 22c found f(0,0) = -4.687 < -3 in the singlet, confirming BCS prerequisites. This extends the analysis to all 9 sectors, identifying which sector has the deepest instability and whether the instability pattern correlates with the BCS phase structure.

**Input**: `tier0-computation/s27_multisector_bcs.npz` (V_max, eigenvalue spectra per sector)

**Script**: `s28b_pomeranchuk_map.py`

**Method**:
1. For each sector (p,q) at each tau:
   ```
   f_l^{(p,q)}(tau) = -N^{(p,q)}(0) * V_max^{(p,q)}(tau)
   ```
   where N(0) is the effective density of states at the gap edge and V_max is the maximum Kosmann coupling.
2. The Pomeranchuk instability condition: f_l < -(2l+1) for angular momentum channel l.
   For l=0 (s-wave): f_0 < -1.
3. Tabulate f_0(tau) for all sectors. Plot as a heatmap: sector vs tau.
4. Identify the sector with the deepest instability (most negative f_0) at each tau.
5. Compare the instability map to the BCS phase diagram from S27 P3 (sector on/off table in S27 addendum).

**Output**: `s28b_pomeranchuk.npz`, `s28b_pomeranchuk.png`

**Gate L-5**: Diagnostic. Deepest instability in (3,0)+(0,3) sectors at tau ~ 0.30-0.35 would be consistent with the interior minimum location. Deepest instability in (2,1) would indicate the high-multiplicity sector drives the physics despite weak per-mode coupling.

**Closure Audit Context (Baptista)**: This diagnostic extends the Pomeranchuk instability from the (0,0) singlet (Session 22c: f(0,0) = -4.687) to all 9 sectors. It provides context for **Closure 7 (perturbative fermion condensate, Session 19a)**, which was closed by the spectral gap. The non-perturbative BCS successor operates in the Pomeranchuk-unstable regime. The Baptista audit notes the constant-ratio trap is "UV-robust but IR-uncertain" (audit §3) — the Pomeranchuk parameter f_0 is an IR quantity that could differ between D_K and D_can in ways that UV-controlled sums cannot.

**Agent**: phonon-exflation-sim

---

### 28b-4: L-6 Quasiparticle Weight Z(tau)

**What**: Compute the quasiparticle renormalization factor Z(tau) = |<psi_can|psi_LC>|^2, the overlap between D_can and D_K eigenvectors for the gap-edge states. Z = 1 means the torsionful and torsion-free eigenstates are identical; Z << 1 means torsion strongly mixes the states. The tau value where Z is minimized identifies the most strongly interacting regime.

**Input**: `tier0-computation/s27_torsion_gap_gate.npz` (D_can and D_K eigenvectors)

**Script**: `s28b_quasiparticle_weight.py`

**Method**:
1. Load D_can and D_K eigenvectors at each tau, per sector.
2. Identify the gap-edge eigenvectors (lowest |eigenvalue| pair) in each basis.
3. Compute Z(tau) = max_m |<psi_1^{can}|psi_m^{LC}>|^2 (maximum overlap of the D_can gap-edge state with any D_K eigenstate).
4. Plot Z(tau) per sector.
5. Z_min identifies the tau value where torsion has maximal effect on the gap-edge wavefunction.
6. **Connection to BCS**: If Z << 1 at some tau, the Kosmann coupling matrix V_nm^{can} will be drastically different from V_nm^{LC} at that tau -- the torsionful BCS kernel sees an entirely different pairing landscape.

**Output**: `s28b_quasiparticle_weight.npz`, `s28b_quasiparticle_weight.png`

**Gate L-6**: Diagnostic. Z_min < 0.5 at any tau would indicate strong torsion mixing, making the D_can BCS result qualitatively different from the D_K result.

**Closure Audit Context (Baptista)**: The constant-ratio trap (F/B = 0.55) is UV-robust but IR-uncertain. Weyl's law controls UV for both connections, but 28b's diagnostics (L-3 relaxation, L-5 Pomeranchuk, L-6 quasiparticle weight) all probe IR physics where connection choice matters. Z_min quantifies exactly HOW MUCH the D_can eigenbasis differs from D_K at the gap edge — the regime where Closure 17 (K-1e) and Closure 18 (selection rule) were computed.

**Agent**: phonon-exflation-sim

---

### 28b-5: L-9 Cubic Invariant / First-Order Transition Test

**What**: Test whether the BCS free energy F_total(tau, mu) has cubic invariants (cusps, non-analyticities) at sector boundary transitions. In Landau theory, a cubic term in the order parameter drives first-order transitions. The multi-sector F_total from S27 showed sector on/off transitions -- are these smooth crossovers or sharp (first-order) transitions?

**Input**: `tier0-computation/s27_multisector_bcs.npz` (F_cond per sector per tau per mu)

**Script**: `s28b_cubic_invariant.py`

**Method**:
1. Load F_total(tau, mu) from s27 data.
2. At mu/lambda_min = 1.20 (where the interior minimum exists): compute dF_total/dtau and d^2F_total/dtau^2 via finite differences.
3. Identify tau values where d^2F/dtau^2 has discontinuities (sign changes in d^3F/dtau^3).
4. At each sector boundary (where a sector transitions from subcritical to supercritical):
   - Does F_total have a cusp (non-analytic point)? Measure |d^3F/dtau^3| left and right.
   - A jump in d^3F/dtau^3 indicates a third-order (or first-order-like in Landau sense) phase transition.
5. Compute the Landau cubic invariant: expand F_cond near the transition as F ~ a*(M_max-1) + b*(M_max-1)^2 + c*(M_max-1)^3. Extract c. If c != 0: first-order transition.

**Output**: `s28b_cubic_invariant.npz`, `s28b_cubic_invariant.png`

**Gate L-9**: Diagnostic. Cusps at sector boundaries confirm first-order (discontinuous) BCS transitions, making the multi-sector system structurally different from a smooth potential minimum.

**Closure Audit Context (Baptista)**: This diagnostic does not directly retest a specific closure but provides an alternative to **Closure 9 (single-field slow-roll, Session 19b)**: eta >> 1 closes slow-roll, but a first-order BCS transition stabilizes the modulus via discontinuous jump, not continuous rolling. If sector boundaries show cubic invariants (cusps in F_total), this supports multi-sector BCS as a non-perturbative mechanism qualitatively distinct from all 15 CONFIRMED CLOSED perturbative closes. The Baptista audit confirms all perturbative mechanisms are closed regardless of connection; first-order BCS transitions are the class of mechanism that perturbation theory cannot access.

**Agent**: phonon-exflation-sim

---

### 28b-6: L-7 Self-Consistent (tau, T) Minimization

**What**: Find the simultaneous minimum of F_total(tau, T) = F_thermal(tau, T) + F_BCS(tau, T). This is the Landau two-transition scenario: at high T, the thermal spectral action dominates and may stabilize tau; at low T, the BCS condensation energy takes over. The combined free energy landscape in (tau, T) space determines whether a non-trivial self-consistent solution exists.

**Input**:
- `tier0-computation/s28a_thermal_spectral_action.npz` (F_thermal(tau; T) from 28a L-1)
- `tier0-computation/s27_multisector_bcs.npz` (F_BCS(tau; mu) from S27)

**Script**: `s28b_self_consistent_tau_T.py`

**Method**:
1. Load F_thermal(tau, T) from 28a L-1.
2. Load F_BCS(tau, mu) from S27.
3. The combined free energy:
   ```
   F_total(tau, T) = F_thermal(tau, T) + sum_{(p,q)} mult(p,q) * F_cond^{(p,q)}(tau, mu_eff(T))
   ```
   where mu_eff(T) encodes the temperature-dependent effective chemical potential (in the simplest model: mu_eff ~ T for thermally activated, or mu_eff = 0 at all T for spectral action self-consistency).
4. Scan the (tau, T) plane: tau in [0, 0.50] (21 points), T in [0.01, 5.0] (20 points).
5. At each grid point: evaluate F_total. Find global and local minima.
6. Plot the phase diagram in (tau, T) space. Mark regions of BCS condensation (Delta > 0) and thermal stabilization.
7. **Key question**: Does a non-trivial minimum exist at (tau > 0, T > 0) that is self-consistent?

**Output**: `s28b_self_consistent_tau_T.npz`, `s28b_self_consistent_tau_T.png`

**Gate L-7**:
- PASS: Non-trivial minimum at (tau_0, T_0) with tau_0 in (0, 0.5) -- two-transition scenario works
- CLOSED: Minimum at (tau=0, T) for all T -- no thermal stabilization
- INCONCLUSIVE: Saddle point but no true minimum

**Closure Audit Context (Baptista)**: The gauge coupling identity g_1/g_2 = e^{-2tau} derives from metric scale factors, NOT the Dirac operator. Closure 14 (clock) and Closure 15 (DESI) are permanently closed regardless of connection — any tau-stabilizing condensate must freeze tau EXACTLY (tau_dot = 0). L-7's self-consistent minimum, if it exists, must produce an exactly frozen modulus, not a slowly rolling one. The Baptista L_tilde coupling (Paper 18) represents a third unexplored option beyond D_K and D_can for future sessions.

**Agent**: phonon-exflation-sim

---

### 28b-7: S-3 Hessian of F_total at Interior Minimum

**What**: Compute the full Hessian matrix of F_total at the interior minimum tau=0.35 (mu/lambda_min=1.20) from S27 P3. A true minimum requires both eigenvalues of the Hessian to be positive. If one eigenvalue is negative, the point is a saddle.

**Input**: `tier0-computation/s27_multisector_bcs.npz`

**Script**: `s28b_hessian.py`

**Method**:
1. Extract F_total(tau, mu) at mu/lambda_min = 1.20 from s27 data.
2. At tau = 0.35: compute the 2x2 Hessian:
   ```
   H = [[d^2F/dtau^2,  d^2F/dtau dmu],
        [d^2F/dmu dtau, d^2F/dmu^2]]
   ```
   using finite differences from the s27 grid (9 tau, 12 mu points).
3. Diagonalize H. Report both eigenvalues.
4. If both positive: true minimum. If one negative: saddle. If both negative: maximum.
5. Repeat at other candidate minima if they exist.

**Output**: `s28b_hessian.npz`, `s28b_hessian.txt`

**Gate S-3**:
- PASS: Both Hessian eigenvalues positive -- genuine minimum
- FAIL: One or both eigenvalues negative -- saddle or maximum

**Closure Audit Context (Baptista)**: This gate validates the S27 interior minimum at tau=0.35. It does not retest a specific numbered closure but is a prerequisite for all BCS-based stabilization to work. Relates to **Closure 14 (clock closure, Session 22d)**: a true minimum with positive Hessian eigenvalues naturally produces tau_dot = 0, satisfying the clock constraint. A saddle point does not — the modulus rolls along the unstable direction, violating the atomic clock bound. The Hessian is computed from D_K BCS data (s27); if 28a-7 shows MAJOR PASS for D_can BCS, the D_can Hessian is the physically relevant one.

**Agent**: phonon-exflation-sim

---

### 28b-8: E-5 Cosmological Constant from Condensation Energy

**What**: Estimate Lambda_eff from the BCS condensation energy at the interior minimum. If condensation provides a negative contribution to the vacuum energy, this constrains the cosmological constant problem.

**Input**: `tier0-computation/s27_multisector_bcs.npz` (F_total at interior min)

**Script**: `s28b_lambda_eff.py`

**Method**:
1. F_total at the interior minimum (tau=0.35, mu/lambda_min=1.20) from S27: F_total = -18.56.
2. Convert to physical units: Lambda_eff = F_total * M_KK^4 / (8*pi*G) where M_KK ~ 10^16 GeV.
3. Compare to observed Lambda ~ (2 meV)^4 ~ 10^{-47} GeV^4.
4. Report the ratio Lambda_eff / Lambda_observed.
5. This is an order-of-magnitude estimate -- the F_total is in code units and the conversion depends on assumptions about the compactification scale.

**Output**: `s28b_lambda_eff.txt`

**Gate E-5**: Diagnostic. The order-of-magnitude comparison constrains whether the BCS mechanism is even remotely compatible with the observed vacuum energy. If Lambda_eff exceeds Lambda_observed by more than 60 orders of magnitude (the standard cosmological constant problem), the framework inherits the standard problem. If Lambda_eff is closer, that would be unexpected and significant.

**Closure Audit Context (Baptista)**: Closure 2 (Coleman-Weinberg, Session 18) is flagged NEEDS REVIEW at low priority. The CW potential for D_can has not been computed. Weyl's law almost certainly closes it in UV, but IR contribution could differ. If time permits, a zero-cost CW recomputation from existing s27 D_can eigenvalues would resolve Closure 2 as a byproduct alongside this E-5 estimate.

**Agent**: phonon-exflation-sim

---

# II. EXECUTION ORDER

```
Independent (run in parallel):
  28b-1 (C-3)  ── order-one condition (requires J matrix + M_Lie)
  28b-2 (L-3)  ── relaxation times (requires s27 M_max interpolation)
  28b-3 (L-5)  ── Pomeranchuk map (requires s27 V_max + eigenvalues)
  28b-5 (L-9)  ── cubic invariant (requires s27 F_total)
  28b-7 (S-3)  ── Hessian (requires s27 F_total grid)
  28b-8 (E-5)  ── Lambda_eff (requires s27 interior min)

Depends on 28a-7 output:
  28b-4 (L-6)  ── quasiparticle weight (requires D_can AND D_K eigenvectors)

Depends on 28a-2 output:
  28b-6 (L-7)  ── self-consistent (tau, T) (requires thermal spectral action from L-1)
```

---

# III. SESSION VERDICT CRITERIA

Results from 28b that feed into 28c:

| Result | Feeds Into | Condition |
|:-------|:-----------|:----------|
| C-3 PASS (order-one) | 28c C-6 (12D axiom verification) | If C-3 PASS, C-6 becomes high priority |
| L-7 PASS (thermal min) | 28c Constraint Chain | Self-consistent mu_eff from thermal channel feeds KC-3 |
| L-3 re-entrant (2,0) | 28c S-4 (Berry curvature) | Re-entrant transitions are sector boundary transitions |
| S-3 PASS (true minimum) | 28c KC-3 (steady-state mu) | Validates the interior minimum as a target for dynamical locking |

**28b is successful if it establishes (a) whether D_can satisfies the NCG axioms (C-3), (b) whether the multi-sector BCS interior minimum is a true minimum or a saddle (S-3), and (c) whether a self-consistent (tau, T) solution exists (L-7).**

---

# IV. OUTPUT FILES

| File | Computation | Producer |
|:-----|:-----------|:---------|
| `tier0-computation/s28b_order_one.py` | C-3 | phonon-sim |
| `tier0-computation/s28b_order_one.npz` | C-3 data | phonon-sim |
| `tier0-computation/s28b_order_one.txt` | C-3 verdict | phonon-sim |
| `tier0-computation/s28b_relaxation_times.py` | L-3 | phonon-sim |
| `tier0-computation/s28b_relaxation_times.npz` | L-3 data | phonon-sim |
| `tier0-computation/s28b_relaxation_times.png` | L-3 plot | phonon-sim |
| `tier0-computation/s28b_pomeranchuk.py` | L-5 | phonon-sim |
| `tier0-computation/s28b_pomeranchuk.npz` | L-5 data | phonon-sim |
| `tier0-computation/s28b_pomeranchuk.png` | L-5 plot | phonon-sim |
| `tier0-computation/s28b_quasiparticle_weight.py` | L-6 | phonon-sim |
| `tier0-computation/s28b_quasiparticle_weight.npz` | L-6 data | phonon-sim |
| `tier0-computation/s28b_quasiparticle_weight.png` | L-6 plot | phonon-sim |
| `tier0-computation/s28b_cubic_invariant.py` | L-9 | phonon-sim |
| `tier0-computation/s28b_cubic_invariant.npz` | L-9 data | phonon-sim |
| `tier0-computation/s28b_cubic_invariant.png` | L-9 plot | phonon-sim |
| `tier0-computation/s28b_self_consistent_tau_T.py` | L-7 | phonon-sim |
| `tier0-computation/s28b_self_consistent_tau_T.npz` | L-7 data | phonon-sim |
| `tier0-computation/s28b_self_consistent_tau_T.png` | L-7 plot | phonon-sim |
| `tier0-computation/s28b_hessian.py` | S-3 | phonon-sim |
| `tier0-computation/s28b_hessian.npz` | S-3 data | phonon-sim |
| `tier0-computation/s28b_hessian.txt` | S-3 verdict | phonon-sim |
| `tier0-computation/s28b_lambda_eff.py` | E-5 | phonon-sim |
| `tier0-computation/s28b_lambda_eff.txt` | E-5 estimate | phonon-sim |
| `sessions/session-28/session-28b-synthesis.md` | Synthesis | coordinator |
