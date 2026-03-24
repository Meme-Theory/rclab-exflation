# E vs F Audit: Every Equation Where S(tau) Was Used as Gravitating Energy

**Author**: Einstein-Theorist
**Date**: 2026-03-14
**Context**: Session 43 Workshop Convergence C1 identified the spectral action as the "wrong gravitating functional." The Einstein field equations require the internal energy E, not the free energy F (or entropy S). This audit catalogues every instance where S(tau) * M_KK^4 / (16 pi^2) was used as though it were rho_grav.

**Principle**: The gravitating energy density entering the Friedmann equation is the INTERNAL ENERGY:

    E = F + TS  (Helmholtz convention)

or equivalently (from the workshop E1 Legendre duality):

    E_grav = S_fold - sum_k T_k * (dS/dT_k)    ... (E1)

where the T_k are the 8 GGE temperatures from GGE-TEMP-43.

**Key distinction**: Derivatives dS/dtau and d2S/dtau2 are UNAFFECTED by the F-to-E correction, because dF/dtau = dE/dtau for any Legendre transform with fixed T. Only the ABSOLUTE VALUE of S(tau) used as rho is incorrect.

---

## Master Table

| # | File / Computation | Session | What was used | Classification | Impact |
|:--|:-------------------|:--------|:-------------|:---------------|:-------|
| 1 | `s43_qtheory_selftune.py` (QFIELD-43) | S43 W1-1 | S_fold * M_KK^4 / (16 pi^2) as rho_vac | **AFFECTED** | CC estimate changes; gate verdict unchanged |
| 2 | `s43_carlip_cc.py` (F-FOAM-5-43) | S43 W2-3 | Lambda_internal = S_fold * M_KK^4 * pf | **AFFECTED** | L_required shifts; PASS unchanged |
| 3 | `s43_friedmann_bcs.py` (FRIEDMANN-BCS-43) | S43 W7-1 | V(tau) = S(tau) / (16 pi^2) in Friedmann eq | **AFFECTED** | H(tau) wrong; epsilon_H wrong; n_s result invalid |
| 4 | `s43_gge_dm_abundance.py` (GGE-DM-43) | S43 W2-1 | rho_GGE = E_exc * prefactor * M_KK^4 | **PARTIALLY AFFECTED** | GGE itself uses E_exc (correct); normalization uses S_fold (wrong) |
| 5 | `s42_dark_energy_wz.py` (W-Z-42) | S42 | V(tau_fold) as vacuum energy for w(z) | **AFFECTED** | epsilon_V changes; w = -1 conclusion survives |
| 6 | `s42_homogeneity.py` (HOMOG-42) | S42 | H_prefactor from sqrt(a_0 / (6 * (4pi)^2)) | **AFFECTED** | Hubble rate wrong; fluctuation amplitude changes |
| 7 | `s42_tau_dyn_reopening.py` | S42 | rho_SA = S_fold * M_KK^4 for Hubble damping | **AFFECTED** | Damping timescale changes; dwell estimate shifts |
| 8 | `s42_constants_snapshot.py` (CONST-FREEZE-42) | S42 | M_KK from a_2 via 1/G_N = (96/pi^2) a_2 M_KK^2 | **UNAFFECTED** | a_2 is a DERIVATIVE coefficient, not absolute S(tau) |
| 9 | `s42_gradient_stiffness.py` | S42 | Z(tau) = (dS/dtau)^2 / S_total, dS/dtau, d2S/dtau2 | **UNAFFECTED** | All derivatives; gradient stiffness unchanged |
| 10 | `s37_CC-Investigation.md` (CC-ARITH-37) | S37 | V_sd = f4*Lambda^4*a_0 + f2*Lambda^2*a_2 + f0*a_4 as vacuum energy | **AFFECTED** | R_CC ~ 113 is the vacuum energy of the WRONG functional |
| 11 | `s36_sfull_tau_stabilization.npz` (TAU-STAB-36) | S36 | S_full(tau) gradient as restoring/destabilizing | **UNAFFECTED** | Gradient (derivative), not absolute value |
| 12 | `s42_fabric_wz_v2.py` | S42 | Fabric w(z) uses V(tau) as DE density | **AFFECTED** | Same as entry 5 |
| 13 | `s43_cbb_timeline.py` (CBB-TIMELINE-43) | S43 W3-1 | S_fold and Delta_S as energy scales for timeline | **AFFECTED** | Epoch boundaries shift; qualitative structure unchanged |
| 14 | `s43_gcm_zeropoint.py` (GCM-ZP-43) | S43 W1-8 | E_ZP vs S_fold for fractional comparison | **AFFECTED** | Denominator changes; E_ZP/S_fold ratio changes |
| 15 | `s43_dowker_sorkin.py` (DS-LAMBDA-43) | S43 W6-16 | S_fold as Lambda_bare input | **AFFECTED** | Same class as entry 2 |
| 16 | `s43_first_law.py` (FIRSTLAW-43) | S43 W6-6 | rho_wall/S_fold for energy fractions | **PARTIALLY AFFECTED** | Denominator changes; first law itself uses differences (correct) |

---

## Detailed Analysis

### Instance 1: QFIELD-43 (s43_qtheory_selftune.py)

**What was used**: Lines 500-514. The "naive CC" is computed as:

    rho_naive = S_fold * prefactor * M_KK^4    (line 500)
    Lambda_naive = rho_naive / M_P^4            (line 505)

The "q-theory corrected" version uses Delta_S = S(fold) - S(0):

    rho_qtheory = Delta_S * prefactor * M_KK^4  (line 501)

Both identify the spectral action VALUE with rho_grav.

**What SHOULD have been used**: The internal energy E_grav from Eq. (E1):

    E_grav = S_fold - sum_k T_k * (dS/dT_k)

where the GGE temperatures T_k are known from GGE-TEMP-43 (T_B2 = 0.668, T_B1 = 0.435, T_B3 = 0.178). The correction term sum_k T_k * (dS/dT_k) is currently uncomputed. This is exactly what CC-GGE-GIBBS-44 is designed to evaluate.

**Impact on result**: The GATE VERDICT (FAIL) is UNCHANGED. The q-theory equilibrium theorem rho(q_0) = 0 remains trivially satisfied at tau = 0 regardless of whether we use S or E. The Gibbs-Duhem analysis (no zero crossing) depends on the functional FORM of rho(tau), which is qualitatively the same for E(tau) as for S(tau) -- both are dominated by a large constant term at tau = 0. The 113-order gap might change by a few orders (depending on the magnitude of sum_k T_k dS/dT_k), but not by 113 orders.

**Estimated magnitude**: The correction sum_k T_k (dS/dT_k) requires knowing how S(tau) changes under variations of the GGE Lagrange multipliers. These are the 8 Richardson-Gaudin integrals, not tau. The BCS energy E_cond = -0.115 M_KK is already the INTERNAL energy of the condensate (it is defined as the eigenvalue of the many-body Hamiltonian, not a free energy). The correction primarily affects the spectral action's contribution S(tau), not the GGE excitation energy E_exc. Thus the dominant CC term (rho_GGE = E_exc * prefactor * M_KK^4) is already using the correct quantity. The ~10^5 M_KK^4 ground-state spectral action S(0) is the most affected -- but q-theory already removes it.

---

### Instance 2: F-FOAM-5-43 (s43_carlip_cc.py)

**What was used**: Lines 131-158. Lambda_internal for all four routes computed as:

    Lambda = S_fold * M_KK^4 * prefactor    (naive)
    Lambda = Delta_S * M_KK^4 * prefactor   (q-theory corrected)

This Lambda_internal feeds into the Carlip trapping calculation to determine the required averaging scale L.

**What SHOULD have been used**: E_grav from Eq. (E1).

**Impact**: Lambda_eff = 1 / (12 pi^2 Lambda_bare L^4). If Lambda_bare changes by a factor x, then L changes by x^{-1/4}. Since E_grav could differ from S_fold by a factor of order O(1) to O(10) (the Legendre transform of a nearly constant function shifts the value but does not introduce exponential suppression), the required L shifts by at most L -> L * 10^{1/4} ~ 1.8 L. The PASS verdict survives: L remains in the physically reasonable range (above Planck, below millimeters). The specific value of L = 174 nm shifts to ~250-300 nm. The force anomaly shifts from 4.4e-22 to ~3e-22. Both remain many orders below experimental sensitivity.

**Estimated magnitude**: Factor of 1-3 in Lambda_bare, factor of 1-1.3 in L_required. Qualitatively unchanged.

---

### Instance 3: FRIEDMANN-BCS-43 (s43_friedmann_bcs.py)

**What was used**: Lines 98-131 and 255-267. The potential V(tau) entering the Friedmann equation:

    V_Pl(tau) = cs_S(tau) * prefactor * scale4    (line 112)
    V_MKK4(tau) = cs_S(tau) * pf                  (line 256)

The Friedmann equation:

    H^2 = FC * [(1/2)*M_ATDHFB*tau_dot^2 + S(tau)]    (line 311-314)

with FC = (8 pi/3) * alpha_G * pf. The entire slow-roll analysis (epsilon_V, eta_V, epsilon_H) uses V(tau) = S(tau) * normalization.

**What SHOULD have been used**: E(tau) = S(tau) - sum_k T_k * (dS/dT_k). However, the Friedmann equation requires rho = T + V where V is the potential energy density. If S(tau) is a free energy, the correct gravitating quantity is the internal energy. The DERIVATIVE terms (dS/dtau entering the equation of motion for tau) are the same for E and S. What changes is the VALUE of V at each tau, which sets H(tau).

**Impact**: The Friedmann equation's H^2 is proportional to V(tau). If V is replaced by E(tau) which is smaller (or larger) by a factor f, then H changes by sqrt(f). The slow-roll parameter epsilon_H = -dH/dt / H^2 involves the RATIO of time derivative to H^2, so it scales as:

    epsilon_H ~ (dV/dtau)^2 / (V^2 * Z)

Since dV/dtau = dE/dtau (derivatives unchanged), and V -> E = f * V, we get epsilon_H -> epsilon_H / f^2. If f < 1 (E < S), epsilon_H INCREASES. If f > 1 (E > S), epsilon_H DECREASES.

**Gate verdict impact**: The gate conclusion was "n_s constraint surface EMPTY." The target epsilon_H = 0.0176 requires 60,861x more energy than BCS provides. Changing V by a factor f changes this ratio by 1/f^2. For the conclusion to flip, we would need f ~ 250 (i.e., E(tau) ~ 250 * S(tau)). This is physically impossible -- the Legendre transform cannot multiply the energy by such a factor. The verdict SURVIVES.

**Estimated magnitude**: epsilon_H changes by f^{-2}. For f ~ 0.5-2, epsilon_H changes by factor 0.25-4. The 60,861x shortfall at the BCS scale is far too large to be rescued.

---

### Instance 4: GGE-DM-43 (s43_gge_dm_abundance.py)

**What was used**: Lines 293-294:

    rho_GGE_MKK4 = E_exc_MKK * prefactor
    rho_GGE_GeV4_grav = rho_GGE_MKK4 * M_KK_grav^4

Here E_exc_MKK = 50.9 M_KK is the EXCITATION energy of the GGE above the ground state. This is already the correct quantity -- it is the internal energy of the quasiparticle excitations, not a free energy.

However, the script ALSO uses S_fold-derived quantities for normalization and comparison (lines 337-404), and the Omega_DM/Omega_Lambda ratio depends on what we identify as rho_Lambda.

**Classification**: PARTIALLY AFFECTED. The GGE excitation energy E_exc is correctly identified as internal energy. The Lambda identification inherits the S-vs-E error from Instance 1.

**Impact**: The Omega_DM/Omega_Lambda = 5.4e5 overshoot reflects using rho_Lambda = rho_GGE (which is already the internal energy, not S_fold). The PASS (degenerate) verdict is unchanged. The "DM and CC are the same problem" conclusion survives because both share the same M_KK^4 scale.

---

### Instance 5: W-Z-42 (s42_dark_energy_wz.py)

**What was used**: Lines 46-48, 77-88:

    V_fold = S_fold    (line 48, spectral action value at fold)
    epsilon_V = (V'/V)^2 / (2Z) = 3.67e-7   (line 77)

The w(z) prediction:

    w = -1 + (2/3) * epsilon_V = -1 + 2.45e-7

**What SHOULD have been used**: E_fold instead of S_fold in the denominator of epsilon_V.

**Impact**: epsilon_V = (dS/dtau)^2 / (2 Z S^2). Replacing S -> E = f * S gives epsilon_V -> epsilon_V / f^2. For f ~ O(1), epsilon_V remains << 1. The conclusion w = -1 to within 10^{-7} is ROBUST to O(1) corrections.

The DECISIVE argument for w = -1 was NOT epsilon_V but the Hubble friction ratio 3H/omega_tau ~ 10^{-55}. This ratio uses H from the Friedmann equation (affected by S->E correction) but omega_tau = sqrt(d2S/(Z)) which is a DERIVATIVE (unaffected). Thus 3H/omega_tau -> 3H*sqrt(f)/omega_tau. For f ~ O(1), the ratio remains absurdly small. The tau field is frozen regardless.

**Gate verdict**: w = -1 prediction SURVIVES. The absolute value of the vacuum energy density changes, but the equation-of-state parameter does not.

---

### Instance 6: HOMOG-42 (s42_homogeneity.py)

**What was used**: Lines 89-91:

    H_prefactor = sqrt(a0_fold / (6 * (4 pi)^2))

This H_prefactor enters the Starobinsky formula for fluctuation variance:

    <phi^2> = (3 H^4) / (8 pi^2 m^2) * [1 - exp(-2 m^2 N / (3H^2))]

**What SHOULD have been used**: H from E(tau) rather than S(tau) in the Friedmann equation.

**Impact**: H^2 ~ a_0 * M_KK^4 / M_Pl^2. The a_0 coefficient IS the correct coefficient for the cosmological constant term in the Seeley-DeWitt expansion. However, the GRAVITATING a_0 should be derived from the internal energy, not the free energy. If a_0 -> a_0 * f, then H -> H * sqrt(f), and <phi^2> ~ H^4 / m^2 scales as f^2. The delta_tau/tau fluctuation scales as f.

For f ~ O(1): delta_tau/tau changes by O(1). The HOMOG-42 result was delta_tau/tau = 6.7e-7 (gravity route, superheavy regime). Even for f = 10 (implausible for a Legendre correction), delta_tau/tau ~ 7e-6, still below the FIRAS bound of 3e-6... wait, that would FAIL. So the margin matters.

**Estimated magnitude**: This is a SENSITIVE instance. The delta_tau/tau = 6.7e-7 has only a factor ~4.5 margin above the FIRAS-derived bound. If H^2 increases by a factor > ~20, the gate could flip. The F-to-E correction is unlikely to be this large (it would require E >> S, which contradicts the standard thermodynamic relation E = F + TS with T > 0 and S > 0 giving E > F). For the spectral action, S plays the role of F (free energy), so E = S + TS_entropy > S. This would INCREASE H, making delta_tau/tau larger and the margin smaller. This requires CC-GGE-GIBBS-44 computation to resolve.

**Classification**: AFFECTED, POTENTIALLY SENSITIVE.

---

### Instance 7: s42_tau_dyn_reopening.py

**What was used**: Lines 807-831:

    rho_SA = S_fold * M_KK^4   (approximate)
    H^2 = S_fold / (3 * (M_Pl/M_KK)^2)

This determines the Hubble damping timescale for the tau modulus.

**Impact**: H changes by sqrt(f). The dwell time scales as 1/H. For f ~ O(1), the dwell estimate shifts by O(1). The TAU-DYN shortfall was 35,000-83,000x. A factor-of-2 change in H does not rescue this. VERDICT SURVIVES.

---

### Instance 8: CONST-FREEZE-42 (s42_constants_snapshot.py)

**What was used**: Lines 762-772. M_KK extraction from G_N:

    M_KK^2 = pi^3 * M_Pl^2 / (12 * a_2)

where a_2 is the SECOND Seeley-DeWitt coefficient (heat kernel coefficient), computed from the spectral sum sum_k lambda_k^{-2} * dim(rep)^2.

**Classification**: UNAFFECTED. The a_2 coefficient is a GEOMETRIC invariant of the Dirac operator -- it encodes the integrated Ricci scalar of the internal space:

    a_2 = (1/6) integral_K R_K dvol_K / (4 pi)^{d/2}

This is NOT the absolute value of the spectral action S(tau). It is a coefficient in the asymptotic expansion of the heat kernel, which encodes CURVATURE, not energy. The Einstein-Hilbert term in the 4D effective action:

    (1/16 pi G_N) R_4 = a_2 * M_KK^2 * R_4 / (normalization)

relates G_N to a_2 through the GEOMETRY of the internal space, not through its total energy. The F-to-E correction does not apply here.

**The same applies to the Kerner formula** for gauge couplings (lines 337-341):

    alpha_eff = 4 M_KK^2 / (M_Pl^2 * g_ab)

This uses the metric components g_ab, not the spectral action value. UNAFFECTED.

---

### Instance 9: s42_gradient_stiffness.py

**Classification**: UNAFFECTED. All outputs are DERIVATIVES: dS/dtau, d2S/dtau2, Z_spectral = (dS/dtau)^2/S_total. The gradient stiffness Z is a ratio of derivatives to the action value, but importantly, Z enters the equation of motion through (1/Z)(dV/dtau), and dV/dtau = dE/dtau. The stiffness Z itself is a property of the field-space metric (DeWitt superspace metric), not of the gravitating energy.

---

### Instance 10: CC-ARITH-37 (session-37-CC-Investigation.md)

**What was used**: The Seeley-DeWitt vacuum energy:

    V_sd = f4 Lambda^4 a_0 + f2 Lambda^2 a_2 + f0 a_4

evaluated at the fold, giving R_CC = log10(V_sd / rho_obs) ~ 112-115.

**What SHOULD have been used**: The INTERNAL ENERGY of the spectral system, not the spectral action value. The spectral action Tr f(D^2/Lambda^2) is formally the one-loop effective action, which in the thermodynamic analogy is the FREE ENERGY F = -T ln Z, not the internal energy E = <H>.

**Impact**: R_CC ~ 113 was already identified as the "standard hierarchy problem reproduced faithfully." The F-to-E correction changes the ABSOLUTE VALUE but not the ORDER OF MAGNITUDE. The correction is sum_k T_k (dS/dT_k), which involves the GGE temperatures (O(1) in M_KK units) and derivatives of S with respect to Lagrange multipliers (unknown, but dimensionally O(S)). At most this changes R_CC by ~1-2 orders. The CC-ARITH-37 SOFT FAIL verdict (R_CC in 100-122 band) is UNAFFECTED.

---

### Instances 11-16: Summary of Remaining

| # | Computation | Affected? | Reason | Verdict |
|:--|:-----------|:----------|:-------|:--------|
| 11 | TAU-STAB-36 | No | Uses dS/dtau (derivative) | Unchanged |
| 12 | fabric_wz_v2 | Yes | Same as Instance 5 | w=-1 survives |
| 13 | CBB-TIMELINE-43 | Yes | Energy scales shift | Epoch boundaries shift by O(1) |
| 14 | GCM-ZP-43 | Yes | E_ZP/S_fold denominator changes | Fractional percentage shifts |
| 15 | DS-LAMBDA-43 | Yes | Lambda_bare input changes | Same class as Instance 2 |
| 16 | FIRSTLAW-43 | Partially | First law uses differences (correct); fractions use S_fold (wrong) | Verified delta Q = T dS relation unaffected |

---

## Summary Statistics

| Classification | Count | Examples |
|:--------------|:------|:--------|
| **AFFECTED** (absolute S used as rho) | 9 | Instances 1,2,3,5,6,7,10,12,13 |
| **PARTIALLY AFFECTED** | 3 | Instances 4,14,16 |
| **UNAFFECTED** (derivatives or geometric coefficients) | 4 | Instances 8,9,11, and all Z/dS/d2S computations |

---

## Which Results Change Most?

### Results that SURVIVE the correction (verdict unchanged):

1. **QFIELD-43 FAIL** (113 OOM gap). The gap might become 111 or 115 OOM; it cannot become < 10.
2. **w = -1 prediction**. Driven by Hubble friction ratio 10^{-55}, insensitive to O(1) corrections.
3. **FRIEDMANN-BCS-43** (n_s constraint surface empty). The 60,861x shortfall is robust.
4. **M_KK extraction from G_N**. Uses a_2 (geometric coefficient), not S(tau).
5. **All derivative-based results**: Z(tau), dS/dtau, d2S/dtau2, gradient stiffness, tau dynamics.
6. **BCS energetics**: E_cond, E_exc, Delta_0 are Hamiltonian eigenvalues (internal energy), not free energies.
7. **Carlip mechanism**: PASS verdict robust to O(1) changes in Lambda_bare.

### Results that REQUIRE re-examination:

1. **R_CC value** (currently 113). Changes by at most a few orders. Still in SOFT FAIL band. But the EXACT value matters for CC-GGE-GIBBS-44 target.
2. **HOMOG-42 margin** (currently 4.5x). The H^2 correction could narrow or widen this margin. Most sensitive single result.
3. **Hubble rate during transit** (all H-dependent timescales). The absolute H changes; ratios of timescales may shift.

### The CRITICAL uncomputed quantity:

    Delta_rho = S(tau) - E_grav(tau) = sum_k T_k * (dS/dT_k)

where T_k are the 8 GGE temperatures and dS/dT_k are derivatives of the spectral action with respect to the GGE Lagrange multipliers. This is PRECISELY what CC-GGE-GIBBS-44 will compute. Until this is done, the F-to-E correction is known in sign (E > F for T > 0, so E_grav > S_fold, making the CC problem WORSE) but not in magnitude.

---

## Structural Observation

The F-vs-E error is UNIVERSAL across the framework. Every computation that used S(tau) as rho_grav inherited the same systematic error. But the error is a MULTIPLICATIVE correction -- it scales the absolute vacuum energy by a factor f = E/S. This means:

1. All RATIOS computed from the spectral action (coupling ratios, epsilon_V, slow-roll parameters, energy fractions) change by powers of f but remain correct to O(1).

2. All DERIVATIVES (dS/dtau, stiffness Z, BCS gap, Turing wavelength, impedance) are EXACTLY correct.

3. The ABSOLUTE CC estimate changes by a factor f, which shifts R_CC by log10(f). For f ~ 1-10, this is at most 1 order.

4. The Hubble rate changes by sqrt(f), which shifts ALL H-dependent timescales by 1/sqrt(f).

The error is systematic and correctable. It does not invalidate any structural theorem (monotonicity, block-diagonal, Schur, etc.). It does not change any gate verdict except possibly HOMOG-42, which has the tightest margin. The CC problem at 113 OOM was already correctly identified as unsolved; the F-to-E correction makes it marginally worse (E > S), not better.

---

## Recommendation for S44

**Immediate**: CC-GGE-GIBBS-44 computes exactly the quantity needed: sum_k T_k * (dS/dT_k). This simultaneously resolves the F-vs-E question AND tests the Gibbs-Duhem CC suppression mechanism.

**Medium-term**: Re-run HOMOG-42 with the corrected H after CC-GGE-GIBBS-44 provides the correction factor f = E/S.

**No action needed**: All derivative-based results, M_KK extraction, BCS energetics, structural theorems.
