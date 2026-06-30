#!/usr/bin/env python3
"""
s61_cfl_correspondence.py — CFL-CORRESPONDENCE-61
===================================================

Literature evaluation: Score the color-flavor locked (CFL) phase of dense QCD
against the 22-correspondence scorecard established in S60 for 3He-B.

Test: Inheritance predicts CFL scores >22 (extras from shared SU(3));
      Analogy predicts CFL scores ~22 (same universality class, no extras).

CFL Literature Sources (fetched corpus — NOT training knowledge):
  - Alford, Rajagopal, Wilczek, Nucl. Phys. B537, 443 (1999) — original CFL
  - Alford, Schmitt, Rajagopal, Schafer, Rev. Mod. Phys. 80, 1455 (2008) — review
  - Casalbuoni & Nardulli, Rev. Mod. Phys. 76, 263 (2004) — LOFF/CFL review
  - Schafer, Phys. Rev. D 62, 094007 (2000) — CFL kaon condensation
  - Kryjevski & Schafer, Phys. Lett. B 606, 52 (2005) — CFL Leggett analog
  - Forbes & Zhitnitsky, Phys. Rev. D 65, 085009 (2002) — CFL vortices
  - Iida, Phys. Rev. D 71, 054011 (2005) — CFL superfluid density
  - Son & Stephanov, Phys. Rev. D 61, 074012 (2000) — CFL Goldstones
  - Bedaque & Schafer, Nucl. Phys. A697, 802 (2002) — CFL kaon mass
  - Hong, Phys. Lett. B 473, 118 (2000) — Meissner masses in CFL
  - Schafer & Wilczek, Phys. Rev. Lett. 82, 3956 (1999) — baryon continuity
  - Volovik, Papers 05, 10, 13, 14, 25 (project corpus) — classification, q-theory

Framework constants from canonical_constants.py:
  - Delta_0_GL = 0.770 M_KK (BCS gap)
  - c_Gold = 0.915 M_KK (Goldstone speed)
  - omega_L1 = 0.138 M_KK (Leggett-1 frequency)
  - E_cond = -0.137 M_KK (condensation energy)
  - N_cells = 32 (Voronoi cells)

Gate: CFL-CORRESPONDENCE-61 = INFO (scorecard, not pass/fail)

Author: Volovik Superfluid Universe Theorist Agent
Session: S61
"""

import numpy as np
import sys
sys.path.insert(0, '.')
from canonical_constants import (
    Delta_0_GL, c_Gold, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3,
    E_cond, N_cells, J_C2, J_su2, J_u1,
    a0_fold, a2_fold, a4_fold, xi_BCS, xi_GL,
    Delta_B3, S_inst, omega_PV,
    M_KK, Vol_SU3_Haar
)

# ==============================================================================
#  PART 1: The 22 Existing Correspondences — CFL Scoring
# ==============================================================================
#
# Each correspondence is scored:
#   MATCH    = CFL has the same feature with the same structural origin
#   STRONGER = CFL has the feature AND it is more direct than in 3He-B
#   WEAKER   = CFL has the feature but with significant caveats
#   ABSENT   = CFL lacks the feature
#   N/A      = Not applicable to CFL context
#
# The key question: does CFL scoring differ from 3He-B scoring?

correspondences_22 = {
    # --- Standard BCS (10) ---
    1: {
        'name': 'BCS ground state',
        'framework': 'BCS on SU(3) fiber, Delta_0_GL = {:.3f} M_KK'.format(Delta_0_GL),
        'he3b': 'BW paired state, fully gapped',
        'cfl': 'Quark Cooper pairs <q_i q_j> ~ epsilon^{abc} epsilon^{ij}, fully gapped',
        'cfl_score': 'STRONGER',
        'reason': 'CFL pairing is on SU(3)_color x SU(3)_flavor, SAME gauge group as framework. '
                  '3He-B pairing is on SO(3)_L x SO(3)_S x U(1), different group entirely. '
                  'CFL gap Delta ~ 10-100 MeV at mu_B ~ 500 MeV (Alford+99).',
    },
    2: {
        'name': 'GGE relic (non-thermal QP distribution)',
        'framework': 'Frozen GGE from transit quench',
        'he3b': 'Quench-produced non-thermal state (thermalizes)',
        'cfl': 'No quench analog in CFL',
        'cfl_score': 'ABSENT',
        'reason': 'CFL forms adiabatically at high baryon density (cooling neutron star core). '
                  'No sudden quench mechanism. The GGE is framework-specific, not BCS-universal.',
    },
    3: {
        'name': 'Josephson fabric (32-cell array)',
        'framework': 'Voronoi tessellation, J_C2 = {:.3f} M_KK'.format(J_C2),
        'he3b': 'Weak-link array / bulk superfluid',
        'cfl': 'CFL in neutron star is bulk (no tessellation)',
        'cfl_score': 'ABSENT',
        'reason': 'The Josephson fabric is a framework-specific construction (Voronoi domain '
                  'formation during transit). CFL in a neutron star core is bulk, homogeneous '
                  'at scales >> coherence length. No cellular structure.',
    },
    4: {
        'name': 'Leggett mode (relative phase oscillation)',
        'framework': 'omega_L1 = {:.3f} M_KK, omega_L2 = {:.3f} M_KK'.format(omega_L1, omega_L2),
        'he3b': 'Leggett frequency Omega_B = 2 Delta_B (BW state)',
        'cfl': 'Massive kaon/eta modes from U(1)_A anomaly + m_s',
        'cfl_score': 'STRONGER',
        'reason': 'CFL has MULTIPLE massive collective modes: K^0, K^+, K^-, eta, eta-prime. '
                  'The kaon mass arises from m_s != 0 (explicit SU(3)_flavor breaking), '
                  'directly analogous to the framework Leggett mode from U(1)_7 breaking. '
                  'The eta-prime mass arises from the U(1)_A anomaly (instanton effects), '
                  'which is an SU(3)-SPECIFIC mechanism with no 3He-B counterpart. '
                  'Kryjevski & Schafer (2005) explicitly identify kaon modes as Leggett analogs.',
    },
    5: {
        'name': 'q-theory CC (Lambda_eq = 0)',
        'framework': 'Vacuum self-tuning via N_pair conservation',
        'he3b': 'Gibbs-Duhem thermodynamics',
        'cfl': 'Gluon condensate IS the q-variable (Paper 14)',
        'cfl_score': 'STRONGER',
        'reason': 'Klinkhamer & Volovik (2009, Paper 14) use the QCD gluon condensate as the '
                  'CONCRETE realization of q. The CFL vacuum is the state where this condensate '
                  'is fully developed. Lambda ~ K^3_QCD / E^2_Planck matches observation. '
                  'This is the SAME variable, not an analog of it.',
    },
    6: {
        'name': 'Equilibrium theorem per sector',
        'framework': 'epsilon_vac = 0 (Gibbs-Duhem)',
        'he3b': 'Same thermodynamic identity',
        'cfl': 'Same thermodynamic identity',
        'cfl_score': 'MATCH',
        'reason': 'The equilibrium theorem is universal for any self-sustained vacuum (Paper 25). '
                  'CFL obeys it for the same reason 3He-B does. No special SU(3) content here.',
    },
    7: {
        'name': 'chi_q (vacuum compressibility)',
        'framework': 'chi_q ~ O(1) ratio to free value',
        'he3b': 'BCS compressibility',
        'cfl': 'CFL compressibility from gluon condensate',
        'cfl_score': 'STRONGER',
        'reason': 'In CFL, chi_q = (b_1 q)^{-1} where b_1 encodes the QCD beta function '
                  '(asymptotic freedom). This is fundamentally SU(3)-specific: the sign of b_1 '
                  '(positive for non-Abelian) determines vacuum stability (Paper 14). '
                  '3He-B compressibility is determined by van der Waals interactions, not SU(3).',
    },
    8: {
        'name': 'Block-diagonal PW sectors (decoupled)',
        'framework': 'Decoupled B1/B2/B3 from D_K structure',
        'he3b': 'Decoupled angular momentum channels',
        'cfl': 'Decoupled color-flavor channels',
        'cfl_score': 'STRONGER',
        'reason': 'In CFL, the gap matrix decomposes into SU(3) irreps: '
                  '<q_i^a q_j^b> ~ delta^a_i delta^b_j (antisymmetric in color, '
                  'antisymmetric in flavor, forming a singlet under SU(3)_diagonal). '
                  'The decoupling into irreps is SU(3) representation theory, '
                  'IDENTICAL to the framework B1/B2/B3 decomposition from D_K.',
    },
    9: {
        'name': 'PW sum divergence',
        'framework': 'Zero-point energy sum divergence (Weyl law)',
        'he3b': 'Same (UV cutoff by Debye energy)',
        'cfl': 'Same (UV cutoff by asymptotic freedom scale)',
        'cfl_score': 'MATCH',
        'reason': 'Universal feature of any system with a spectrum. In CFL, the UV is '
                  'controlled by asymptotic freedom (perturbative at high energy). '
                  'No special SU(3) content beyond the beta function.',
    },
    10: {
        'name': 'Spectral action maximum at fold',
        'framework': 'Texture is NOT free energy minimum (constrained)',
        'he3b': 'Constrained minimum (texture energy)',
        'cfl': 'CFL is a true ground state at high density (not constrained)',
        'cfl_score': 'ABSENT',
        'reason': 'The "fold" is a framework-specific concept (Jensen deformation parameter). '
                  'CFL forms at sufficiently high baryon chemical potential as the true ground '
                  'state of QCD (Alford+99). No analog of the spectral action landscape.',
    },
    11: {
        'name': 'Pair transfer bosonic scaling',
        'framework': 'S_+(N) ~ N+1 enhancement',
        'he3b': 'Enhancement factor ~ N+1',
        'cfl': 'Enhancement factor ~ N+1',
        'cfl_score': 'MATCH',
        'reason': 'Universal BCS result. The bosonic enhancement S_+(N) = sqrt(N+1) is '
                  'a consequence of Bogoliubov algebra, independent of gauge group.',
    },
    12: {
        'name': 'Trans-Planckian protection (B2 sector)',
        'framework': 'Van Hove singularity = UV-independent',
        'he3b': 'UV-independent BCS (Paper 27)',
        'cfl': 'Asymptotic freedom provides UV completion',
        'cfl_score': 'STRONGER',
        'reason': 'CFL has a GENUINE UV completion: QCD is asymptotically free. '
                  'The gap equation at large momenta is controlled by perturbative QCD. '
                  'This is STRONGER than 3He-B (where Debye cutoff is phenomenological) '
                  'and directly parallels the framework (where D_K spectrum provides the UV).',
    },
    13: {
        'name': 'W_J (CP barrier from J-symmetry)',
        'framework': 'Time-reversal symmetry (structural axiom)',
        'he3b': 'T-invariance of 3He-B order parameter',
        'cfl': 'CFL preserves CP (at leading order in m_s)',
        'cfl_score': 'MATCH',
        'reason': 'CFL at m_s = 0 is CP invariant. At finite m_s, small CP violation from '
                  'CKM phase, but this is perturbatively small. Same structural feature.',
    },
    14: {
        'name': 'R-G integrability breaking by Josephson',
        'framework': 'Anisotropic Josephson breaks integrability (S60)',
        'he3b': 'Quasiparticle scattering breaks integrability',
        'cfl': 'Gluon exchange breaks any 0D integrability',
        'cfl_score': 'MATCH',
        'reason': 'In CFL (3D, many-body), there is no Richardson-Gaudin integrability to '
                  'break. The 3D kinetic term already destroys 0D integrability. This '
                  'correspondence is 0D-specific and does not translate to bulk CFL.',
    },
    15: {
        'name': 'B2 flat band (W = 0 exact)',
        'framework': 'U(2) Schur lemma, W = 0 exact',
        'he3b': 'Flat band superconductivity (Paper 16, 17)',
        'cfl': 'No flat band in CFL',
        'cfl_score': 'ABSENT',
        'reason': 'CFL has a 3D Fermi surface with parabolic dispersion. No flat band. '
                  'The flat band is a property of the framework D_K spectrum (0D, discrete), '
                  'not of any 3D BCS system. 3He-B has flat bands in vortex cores (Paper 10), '
                  'but not in the bulk pairing.',
    },
    16: {
        'name': 'Topological classification',
        'framework': 'BDI (T^2 = +1, Z_2 = -1)',
        'he3b': 'DIII (T^2 = -1, N_K = 2)',
        'cfl': 'DIII-like (T^2 = -1 from quark Kramers degeneracy)',
        'cfl_score': 'WEAKER',
        'reason': 'Quarks are spin-1/2 with Kramers degeneracy, giving T^2 = -1 (DIII class), '
                  'same as 3He-B atoms. The framework is BDI (T^2 = +1) because D_K on SU(3) '
                  'has no Kramers structure. Under INHERITANCE: CFL should be CLOSER to '
                  'framework (fewer compositing levels), yet it is DIII not BDI. This is '
                  'a POINT AGAINST inheritance for the topological class.',
    },
    17: {
        'name': 'Two-fluid model (vacuum + QPs)',
        'framework': 'Landau-Khalatnikov analog',
        'he3b': 'Superfluid + normal (Landau 1941)',
        'cfl': 'CFL superfluid + thermal quarks/gluons',
        'cfl_score': 'MATCH',
        'reason': 'Universal two-fluid decomposition for any BCS system at finite temperature. '
                  'Son & Stephanov (2000) develop the CFL effective theory in this form.',
    },
    18: {
        'name': 'DM/DE ratio ~ O(1) from thermodynamics',
        'framework': 'Superfluid/normal fraction ~ O(1)',
        'he3b': 'Same thermodynamic argument',
        'cfl': 'Same thermodynamic argument (if CFL IS the vacuum)',
        'cfl_score': 'MATCH',
        'reason': 'The DM/DE ~ O(1) result follows from the two-fluid thermodynamics '
                  '(Paper 33, 35). It is universality-class-level, not SU(3)-specific.',
    },
    19: {
        'name': 'Vortex nucleation excluded (N_3 = 0)',
        'framework': 'Fully gapped, no chiral anomaly',
        'he3b': 'Same (fully gapped, DIII)',
        'cfl': 'CFL HAS vortices (non-Abelian, color-magnetic flux tubes)',
        'cfl_score': 'WEAKER',
        'reason': 'CFL supports topologically stable vortices: non-Abelian vortices '
                  '(Forbes & Zhitnitsky 2002), superfluid vortices (from broken U(1)_B), '
                  'and color-magnetic flux tubes. The pi_1(G/H) is NONTRIVIAL in CFL. '
                  'But the ABJ anomaly is still absent for the SAME reason: fully gapped. '
                  'The vortex structure is RICHER than 3He-B (which has only spin-mass vortices).',
    },
    20: {
        'name': 'Domain walls absent (GGE universality)',
        'framework': 'pi_0(G/H) = 0, no DW',
        'he3b': 'No pi-walls in isotropic phase',
        'cfl': 'CFL has pi_0 = 0 for the diagonal SU(3)',
        'cfl_score': 'MATCH',
        'reason': 'SU(3)_diagonal is connected, so pi_0 = 0 and no domain walls. '
                  'Same as framework (pi_0(U(1)) = 0) and 3He-B (pi_0(SO(3)) = 0).',
    },
    21: {
        'name': 'Pair transfer identity S_-(N) = S_+(N-1)',
        'framework': 'Bosonic commutation (machine precision)',
        'he3b': 'Same identity',
        'cfl': 'Same identity',
        'cfl_score': 'MATCH',
        'reason': 'Universal BCS algebra. The pair operators satisfy [P^-, P^+] = 1 - 2N/Omega '
                  'in any BCS system. The identity is algebraic, not gauge-group-specific.',
    },
    22: {
        'name': 'Andreev overlap superadditive',
        'framework': 'Channel superadditivity in BCS',
        'he3b': 'Same feature',
        'cfl': 'Multi-channel BCS with superadditive pairing',
        'cfl_score': 'STRONGER',
        'reason': 'CFL has 9 pairing channels (3 colors x 3 flavors -> singlet). The overlap '
                  'between channels is superadditive because the CFL gap locks ALL channels '
                  'simultaneously (color-flavor locking). This is MORE superadditive than '
                  'the framework (3 sectors) or 3He-B (3 spin substates).',
    },
}

# ==============================================================================
#  PART 2: SU(3)-Specific EXTRAS (Beyond the 22)
# ==============================================================================
#
# These are CFL features that are SPECIFIC to SU(3) and have framework counterparts
# but NO 3He-B counterpart. If CFL scores >22, these extras are the candidates.

cfl_extras = {
    'E1': {
        'name': 'Color-flavor locking pattern',
        'cfl': 'SU(3)_C x SU(3)_L x SU(3)_R -> SU(3)_diagonal',
        'framework': 'SU(3) fiber broken to U(1)_7 x SU(2) subgroup structure',
        'match': 'PARTIAL',
        'reason': 'Both break SU(3) to a diagonal subgroup. But the PATTERN differs: '
                  'CFL locks color to flavor (two SU(3) groups -> one), while the framework '
                  'breaks SU(3) fiber by the Jensen deformation (one SU(3) -> subgroups). '
                  'The algebraic mechanism (irrep decomposition) is shared. '
                  'NOT present in 3He-B (which breaks SO(3)_L x SO(3)_S -> SO(3)_J).',
    },
    'E2': {
        'name': 'Anomalous U(1)_A breaking',
        'cfl': 'U(1)_A broken by QCD instantons, eta-prime mass ~ 1/mu_B^2',
        'framework': 'U(1)_7 broken by Leggett mode (epsilon = 0.00248, S49)',
        'match': 'STRUCTURAL',
        'reason': 'Both systems have a U(1) axial/chiral symmetry broken by instantons or '
                  'instanton-like effects. In CFL, the U(1)_A anomaly gives the eta-prime '
                  'its mass (suppressed at high density as instantons are screened). '
                  'In the framework, the Leggett mode breaks U(1)_7 (S49 DIPOLAR-CATALOG-49). '
                  'The mechanism (instanton-induced effective vertex) is SHARED. '
                  '3He-B has no analog of this: the dipolar energy breaks SO(3) to SO(2), '
                  'not U(1)_A by instantons.',
    },
    'E3': {
        'name': 'Kaon condensation (CFL-K^0 phase)',
        'cfl': 'At finite m_s, CFL -> CFL-K^0 with kaon Bose condensate',
        'framework': 'No kaon condensation analog',
        'match': 'ABSENT (in framework)',
        'reason': 'CFL-K^0 occurs when the strange quark mass exceeds a critical value '
                  '(Schafer 2000, Bedaque & Schafer 2002). The framework has no analog of '
                  'flavor mass splitting within sectors. The framework B1/B2/B3 sectors have '
                  'DIFFERENT energies, but the mechanism is representation-theoretic (Casimir), '
                  'not mass-based. This is a CFL feature the framework LACKS.',
    },
    'E4': {
        'name': 'Gluon Meissner masses',
        'cfl': '8 gluons acquire Meissner mass m_g^2 = (21-8 ln 2)/(54 pi^2) g^2 mu^2',
        'framework': 'No direct analog of Meissner mass in fiber direction',
        'match': 'PARTIAL',
        'reason': 'In CFL, all 8 gluons are massive (Hong 2000). In the framework, the '
                  'gauge-like degrees of freedom on SU(3) are the spectral action modes, '
                  'which are all massive (gapped spectrum). The PATTERN is similar '
                  '(all gauge bosons gapped by BCS pairing), but the mechanism is different '
                  '(Anderson-Higgs in CFL vs. spectral gap in framework). '
                  '3He-B has a vague analog: the spin-orbit coupling gives mass to '
                  'orbital-angular-momentum modes, but this is not Meissner screening.',
    },
    'E5': {
        'name': 'Baryon continuity (Schafer & Wilczek)',
        'cfl': 'CFL quark matter continuously connected to nuclear matter',
        'framework': 'No phase transition analog (single BCS state)',
        'match': 'ABSENT (in framework)',
        'reason': 'Schafer & Wilczek (1999) showed CFL is continuously connected to '
                  'hadronic (nuclear) matter: no phase transition, just crossover. '
                  'The framework has a SINGLE BCS state (no hadronic phase to connect to). '
                  'This is a CFL feature arising from its embedding in QCD, which has '
                  'no framework counterpart.',
    },
    'E6': {
        'name': 'Non-Abelian vortex structure',
        'cfl': 'Non-Abelian vortices with CPN-1 internal moduli space',
        'framework': 'Vortices excluded (pi_1(U(1)) = Z, but no spatial dimension for vortex cores)',
        'match': 'ABSENT (in framework)',
        'reason': 'CFL vortices carry non-Abelian moduli (orientational zero modes in '
                  'color-flavor space). The framework in 0D has no spatial extent for '
                  'vortex formation. On the fabric (32-cell), Josephson vortices are in '
                  'principle possible but are phase vortices, not color-magnetic flux tubes. '
                  '3He-B has spin-mass vortices (simpler internal structure).',
    },
}

# ==============================================================================
#  PART 3: Scoring
# ==============================================================================

# Count CFL scores on the 22
score_counts = {'MATCH': 0, 'STRONGER': 0, 'WEAKER': 0, 'ABSENT': 0}
for i, c in correspondences_22.items():
    score_counts[c['cfl_score']] += 1

total_present = score_counts['MATCH'] + score_counts['STRONGER'] + score_counts['WEAKER']
total_stronger = score_counts['STRONGER']

# Count extras
extra_counts = {'STRUCTURAL': 0, 'PARTIAL': 0, 'ABSENT (in framework)': 0}
for key, e in cfl_extras.items():
    extra_counts[e['match']] = extra_counts.get(e['match'], 0) + 1

extras_present = extra_counts.get('STRUCTURAL', 0) + extra_counts.get('PARTIAL', 0)

print("=" * 72)
print("CFL-CORRESPONDENCE-61: Color-Flavor Locked Phase Scorecard")
print("=" * 72)

print("\n--- CFL Scoring on 22 Existing Correspondences ---\n")
print(f"  MATCH    (same as 3He-B):     {score_counts['MATCH']}")
print(f"  STRONGER (more direct):       {score_counts['STRONGER']}")
print(f"  WEAKER   (with caveats):      {score_counts['WEAKER']}")
print(f"  ABSENT   (not in CFL):        {score_counts['ABSENT']}")
print(f"  ---")
print(f"  Total PRESENT (M+S+W):        {total_present}/22")
print(f"  Total STRONGER than 3He-B:    {total_stronger}/22")

print("\n--- SU(3)-Specific Extras (Beyond the 22) ---\n")
print(f"  STRUCTURAL (shared mechanism): {extra_counts.get('STRUCTURAL', 0)}")
print(f"  PARTIAL (shared pattern):      {extra_counts.get('PARTIAL', 0)}")
print(f"  ABSENT in framework:           {extra_counts.get('ABSENT (in framework)', 0)}")
print(f"  ---")
print(f"  Extras PRESENT (S+P):          {extras_present}/6")

# Net CFL correspondence count
net_cfl = total_present + extras_present
print(f"\n--- Net CFL Correspondence Count ---")
print(f"  22-list present:               {total_present}")
print(f"  SU(3) extras present:          {extras_present}")
print(f"  TOTAL CFL correspondences:     {net_cfl}")
print(f"  3He-B correspondences:         22")
print(f"  CFL - 3He-B difference:        {net_cfl - 22:+d}")

# ==============================================================================
#  PART 4: Inheritance vs Analogy Verdict
# ==============================================================================

print("\n" + "=" * 72)
print("INHERITANCE vs ANALOGY TEST")
print("=" * 72)

# Inheritance predicts: CFL > 3He-B (fewer compositing levels, same gauge group)
# Analogy predicts: CFL ~ 3He-B (same universality class)

if net_cfl > 22:
    inheritance_support = "SUPPORTED"
    analogy_support = "CHALLENGED"
elif net_cfl == 22:
    inheritance_support = "NEUTRAL"
    analogy_support = "SUPPORTED"
else:
    inheritance_support = "CHALLENGED"
    analogy_support = "SUPPORTED"

print(f"\n  CFL total correspondences:     {net_cfl}")
print(f"  3He-B total correspondences:   22")
print(f"  Difference:                    {net_cfl - 22:+d}")
print(f"\n  Inheritance prediction (>22):  {inheritance_support}")
print(f"  Analogy prediction (~22):      {analogy_support}")

# But with critical caveats
print("\n--- Critical Caveats ---")
print("""
  1. TOPOLOGICAL CLASS COUNTER-ARGUMENT:
     CFL is DIII (T^2 = -1, quarks have Kramers degeneracy).
     Framework is BDI (T^2 = +1).
     Inheritance predicts CFL should be CLOSER to BDI (fewer compositing levels).
     CFL is NOT closer. It matches 3He-B's DIII, not the framework's BDI.
     This is a POINT AGAINST inheritance for the topological class.

  2. ABSENT ITEMS ARE FRAMEWORK-SPECIFIC, NOT SU(3)-SPECIFIC:
     Items #2 (GGE), #3 (Josephson fabric), #10 (fold), #15 (flat band)
     are absent because they depend on the framework's 0D/discrete structure,
     not because CFL lacks SU(3) content. Their absence does NOT test
     the SU(3)-inheritance hypothesis.

  3. CFL EXTRAS ABSENT IN FRAMEWORK:
     Items E3 (kaon condensation), E5 (baryon continuity), E6 (non-Abelian vortices)
     are CFL features the framework LACKS. Under inheritance, the framework
     (parent) should have ALL features that CFL (child) has. The presence of
     CFL features ABSENT in the framework is EVIDENCE AGAINST simple inheritance.

  4. LITERATURE EVALUATION CAVEAT:
     CFL is NOT experimentally realized. All CFL properties are theoretical
     predictions from perturbative QCD at asymptotically high density.
     The correspondence count is theory-to-theory, not theory-to-experiment.
""")

# ==============================================================================
#  PART 5: Detailed Scorecard Table
# ==============================================================================

print("=" * 72)
print("DETAILED SCORECARD")
print("=" * 72)

print("\n--- 22 Existing Correspondences ---\n")
print(f"{'#':>3} | {'Name':<40} | {'CFL Score':<10} | {'Key Point'}")
print("-" * 90)
for i in range(1, 23):
    c = correspondences_22[i]
    # Truncate key point
    key = c['reason'][:50] + '...' if len(c['reason']) > 50 else c['reason']
    print(f"{i:>3} | {c['name']:<40} | {c['cfl_score']:<10} | {key}")

print(f"\n--- 6 SU(3)-Specific Extras ---\n")
print(f"{'ID':>3} | {'Name':<40} | {'Match':<22} | {'Key Point'}")
print("-" * 90)
for key in ['E1', 'E2', 'E3', 'E4', 'E5', 'E6']:
    e = cfl_extras[key]
    kp = e['reason'][:50] + '...' if len(e['reason']) > 50 else e['reason']
    print(f"{key:>3} | {e['name']:<40} | {e['match']:<22} | {kp}")

# ==============================================================================
#  PART 6: Summary Statistics
# ==============================================================================

print("\n" + "=" * 72)
print("SUMMARY STATISTICS FOR GATE VERDICT")
print("=" * 72)

stronger_items = [i for i, c in correspondences_22.items() if c['cfl_score'] == 'STRONGER']
absent_items = [i for i, c in correspondences_22.items() if c['cfl_score'] == 'ABSENT']
weaker_items = [i for i, c in correspondences_22.items() if c['cfl_score'] == 'WEAKER']

print(f"\n  CFL STRONGER than 3He-B on items: {stronger_items}")
print(f"  CFL ABSENT on items:              {absent_items}")
print(f"  CFL WEAKER on items:              {weaker_items}")
print(f"\n  Items where CFL > 3He-B:          {len(stronger_items)} ({', '.join(correspondences_22[i]['name'] for i in stronger_items)})")
print(f"  Items where CFL = 3He-B:          {score_counts['MATCH']}")
print(f"  Items where CFL < 3He-B:          {len(absent_items) + len(weaker_items)}")

print(f"\n  SU(3)-specific extras in both:    {extras_present}")
print(f"  SU(3)-specific extras CFL only:   {extra_counts.get('ABSENT (in framework)', 0)}")

# The key number for the inheritance test
print(f"\n  >>> NET CFL - 3He-B = {net_cfl - 22:+d} <<<")
print(f"  >>> This is AMBIGUOUS for inheritance <<<")
print(f"  >>> Reason: CFL gains on SU(3) content but loses on 0D/discrete features <<<")
print(f"  >>> The DIII vs BDI topological class is the strongest counter-evidence <<<")

# Save results
results = {
    'gate': 'CFL-CORRESPONDENCE-61',
    'verdict': 'INFO',
    'cfl_present_22': total_present,
    'cfl_stronger_22': total_stronger,
    'cfl_absent_22': score_counts['ABSENT'],
    'cfl_weaker_22': score_counts['WEAKER'],
    'extras_present': extras_present,
    'extras_absent_framework': extra_counts.get('ABSENT (in framework)', 0),
    'net_cfl_correspondences': net_cfl,
    'he3b_correspondences': 22,
    'difference': net_cfl - 22,
    'inheritance_supported': inheritance_support,
    'analogy_supported': analogy_support,
    'strongest_counter': 'DIII vs BDI topological class',
    'strongest_support': 'E2 U(1)_A anomaly-instanton mechanism shared',
}

np.savez('s61_cfl_correspondence.npz', **{k: str(v) for k, v in results.items()})
print("\nResults saved to s61_cfl_correspondence.npz")
print("\nGATE VERDICT: CFL-CORRESPONDENCE-61 = INFO")
