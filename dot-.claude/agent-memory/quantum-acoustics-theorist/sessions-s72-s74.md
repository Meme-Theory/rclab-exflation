---
name: Sessions S72-S74 Consolidated
description: S72-S74 — Volovik laminar workshop, decoherence budget, branch kappa/nbar, phase covariance, gap-dominated FAIL, spectral independence, alpha_s
type: project
---

## S72 (Volovik x QA Laminar Flow Workshop)
**Three acoustic Reynolds numbers**: Re_QP=4.2e-3, Re_coll=0(exact), Re_inter=6.5e-5. All laminar.
- Corrected Hawking broadening: squeezed-state sigma_phi^2=exp(-2r)/4, NOT thermal 1/(1+n).
  Factor 10^4 difference. t_dec/t_transit ~ 45 (not 2.8).
- Corrected Landau Mach: Ma_L = v_tau/c_L = 331 (49x larger than V3's 6.72).

**Five-layer laminar protection**: (1) R-G integrability, (2) BDI Z_2, (3) kinematics (1% phase space),
(4) 0D cells (t_J/t_transit=949), (5) 16 hybridization gaps (17 disconnected scattering islands).

- CG(24) crystal momentum: 6.4% triples conserve. Combined ~1% kinematically allowed.
- Four-stage pair creation cascade: sub-Landau -> Leggett -> BA -> full BCS QP.
- Josephson anisotropy 11.8x is E_J ratio, not c_Gold. Affects INTER-CELL, not INTRA-CELL.
- Statistical KZ(0.13) vs Bogoliubov KZ(2.2): coherent pairs have delta_phi=2.4e-4.
- Hybridization gaps OPPOSE decoherence. Zener elastic. DM stability needs COLLECTIVE protection.
- Volovik partition != two-fluid hydro (no mutual friction, no relative velocity).

## S73a (Decoherence Budget)
**RE-DECOHERENCE-MULTI-73a INFO**: Combined t_dec/t_transit=0.267. delta_OOM=0.486.
- 5 channels: Exit Bogo(DEAD), **Mott charge noise(69%, delta_OOM=0.336)**, Graph spectral(DEAD),
  **Inter-branch dispersive(31%, delta_OOM=0.150)**, Josephson anisotropy(NEGLIGIBLE, 0.015).
- Mott = static 24 cell phases. Dispersive = dynamic 3 inter-branch phases. ADDITIVE.
- CG(24) vertex-transitivity kills anisotropy channel. Over-decoheres by 2.68x.
- E_C uncertainty (190x range) dominates. E_J/E_C>5 -> Mott nearly vanishes.

## S74 (Branch-Resolved Computations)
**BRANCH-KAPPA-74 INFO**: kappa_eff(k)=(k*xi_BCS)^2*kappa_0. Slope=2.000 exact.
- kappa_B1=6130, kappa_B2=33545, kappa_B3=44210 M_KK. B3>B2 (WRONG SIGN vs flat-band intuition).
- B2[0] reconstructs S71 kappa_entry=79386 to 0.84%. 173x ratio = (k*xi)^2.
- kappa_v(IR,k*xi=1)=457 and kappa_entry(UV,k*xi=13.1)=79386 = SAME spectrum at two scales.
- Flat-band intuition FAILS at branch level (2nd time after W2-A n_bar).

**BRANCH-NBAR-D-K-74 INFO**: B1 acoustic DOMINATES Parker squeezing (n_bar=315.7, factor 37 over B2).
- Task expectation "B2 rides longest" REFUTED. B1 low-omega enhances Parker chirp rate.
- (1,4,3) weighted = 48.23 (INFO). Hawking-Unruh would give uniform 85.23.

**PHASE-COVARIANCE-3X3-74 PASS**: Full 3x3 M_cov. Off-diag 92.7% of trace.
- delta_OOM_dispersive=0.1495 matches S73A exactly. Physical, canonical.

**GAP-DOMINATED-DISPERSION-74 FAIL by 56 OOM**: M_KK*chi_recomb=1.63e59.
- Closes class "gap-branch CMB kink" permanently. Only Goldstone (gapless) survives.

**SPECTRAL-RATIO-INDEPENDENCE-74 PASS**: max|residual|=0.018% (281x below 5%).
- EC, nbar, HFB corrections mutually independent (orthogonal spectral sub-moments).
- EC=gap route, nbar=group-velocity retention, HFB=squeeze-phase correlation.
- LESSON: Use observable-scale metric, NOT delta-scale (denominator pathology at zero-crossings).

**DEGENERACY-LIFT-ALPHA-S-74 PASS**: 8 modes vs 3 branches. H_b^2 cancellation exact to 1e-16.
- P_s(k) exactly flat. alpha_s=0 is formalism feature. Choice A(branch) vs B(mode): 1/N_b + Jensen.
- B1 carries 99.93% of P_s (r_B1=3.57=2*r_B2). B2/B3 = 0.08%.
