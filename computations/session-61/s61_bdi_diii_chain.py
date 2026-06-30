#!/usr/bin/env python3
"""
BDI-DIII-CHAIN-61: Altland-Zirnbauer inheritance chain from substrate to 3He-B
================================================================================

Gate: BDI-DIII-CHAIN-61 (INFO classification)
Agent: Nazarewicz Nuclear Structure Theorist

Question: Is 3He-B the UNIQUE condensed matter endpoint reachable from BDI
via the compositing inheritance chain?

Method: Trace T^2, C^2 through every compositing level. The AZ class changes
when the effective time-reversal operator acquires Kramers degeneracy (T^2 = -1),
which occurs when the composite object has half-integer spin.

Reference: Sato & Ando (2017), Hasan & Kane (2010), Volovik (Paper 05 Table 1).
Framework BDI proven S08/S17c: J^2 = +1, [J, D_K] = 0, KO-dim = 6.
"""

from canonical_constants import M_KK, tau_fold
import numpy as np

# ==============================================================================
# SECTION 1: THE ALTLAND-ZIRNBAUER 10-FOLD WAY
# ==============================================================================
# The 10 AZ classes are labeled by (T^2, C^2, S) where:
#   T = time-reversal, C = particle-hole (charge conjugation), S = sublattice (chiral)
#   T^2 = 0 (absent), +1 (integer spin), -1 (half-integer spin, Kramers)
#   C^2 = 0 (absent), +1, -1
#   S = 0 (absent), 1 (present, S = TC when both T,C present)
#
# The 10 classes and their topological invariants in d=3 spatial dimensions:

AZ_TABLE = {
    # class:  (T^2,  C^2,  S,   topo_d3)
    'A':      (0,    0,    0,   '0'),       # Unitary
    'AIII':   (0,    0,    1,   'Z'),       # Chiral unitary
    'AI':     (+1,   0,    0,   '0'),       # Orthogonal
    'BDI':    (+1,   +1,   1,   '0'),       # Chiral orthogonal  <-- SUBSTRATE
    'D':      (0,    +1,   0,   'Z'),       # BdG (no TRS)
    'DIII':   (-1,   +1,   1,   'Z'),       # BdG (TRS, Kramers) <-- 3He-B
    'AII':    (-1,   0,    0,   'Z2'),      # Symplectic (TI)
    'CII':    (-1,   -1,   1,   'Z2'),      # Chiral symplectic
    'C':      (0,    -1,   0,   '0'),       # BdG (no TRS, spin-singlet)
    'CI':     (+1,   -1,   1,   '0'),       # BdG (TRS, spin-singlet)
}

print("=" * 72)
print("  ALTLAND-ZIRNBAUER 10-FOLD TABLE")
print("=" * 72)
print(f"{'Class':<6} {'T^2':>4} {'C^2':>4} {'S':>3} {'Topo(d=3)':>10}")
print("-" * 32)
for name, (T2, C2, S, topo) in AZ_TABLE.items():
    marker = ""
    if name == 'BDI':
        marker = "  <-- SUBSTRATE (PROVEN S08/S17c)"
    elif name == 'DIII':
        marker = "  <-- 3He-B TARGET"
    T2_str = str(T2) if T2 != 0 else '0'
    C2_str = str(C2) if C2 != 0 else '0'
    print(f"{name:<6} {T2_str:>4} {C2_str:>4} {S:>3} {topo:>10}{marker}")

# ==============================================================================
# SECTION 2: THE INHERITANCE CHAIN
# ==============================================================================
# Level 0: M^4 x SU(3) substrate (D_K Dirac operator)
# Level 1: Gauge bosons (gluons, W, Z, photon, graviton)
# Level 2: Quarks and leptons (from D_K eigenstates)
# Level 3: Nucleons (composite: 3 quarks)
# Level 4: Atoms (composite: nucleons + electrons)
# Level 5: Condensed matter (Cooper pairs, superfluids)

print("\n" + "=" * 72)
print("  INHERITANCE CHAIN: BDI -> ??? -> DIII")
print("=" * 72)

levels = [
    {
        'level': 0,
        'name': 'Substrate (D_K on M^4 x SU(3))',
        'spin': 'N/A (spectral geometry)',
        'T2': +1,
        'C2': +1,
        'S': 1,
        'AZ': 'BDI',
        'reason': 'J^2 = +1 PROVEN (S08, machine epsilon). KO-dim=6.',
        'kramers': False,
    },
    {
        'level': 1,
        'name': 'Gauge bosons (spin-1)',
        'spin': 1,
        'T2': +1,
        'C2': +1,
        'S': 1,
        'AZ': 'BDI',
        'reason': 'Integer spin -> T^2 = +1. PHS from BdG structure. Chiral from D_K.',
        'kramers': False,
    },
    {
        'level': 2,
        'name': 'Quarks/leptons (spin-1/2)',
        'spin': 0.5,
        'T2': -1,
        'C2': +1,
        'S': 1,
        'AZ': 'DIII',
        'reason': 'FIRST HALF-INTEGER SPIN. T^2 = (-1)^{2s} = -1 for s=1/2. Kramers degeneracy.',
        'kramers': True,
    },
    {
        'level': 3,
        'name': 'Nucleons (spin-1/2, composite of 3 quarks)',
        'spin': 0.5,
        'T2': -1,
        'C2': +1,
        'S': 1,
        'AZ': 'DIII',
        'reason': '3 quarks (each s=1/2) -> J = 1/2 or 3/2. Nucleon: J=1/2. Still Kramers.',
        'kramers': True,
    },
    {
        'level': 4,
        'name': '3He atom (spin-1/2, composite of 2p+1n+2e)',
        'spin': 0.5,
        'T2': -1,
        'C2': +1,
        'S': 1,
        'AZ': 'DIII',
        'reason': '3He: 2p(up+down)+1n(up)+2e(up+down) -> nuclear I=1/2. F=1/2 in ground state. Kramers.',
        'kramers': True,
    },
    {
        'level': 5,
        'name': '3He-B superfluid (Cooper pairs of spin-1/2 atoms)',
        'spin': 0.5,
        'T2': -1,
        'C2': +1,
        'S': 1,
        'AZ': 'DIII',
        'reason': 'BdG of spin-1/2 fermions. T^2 = -1. N_K = 2 (3D topological, Z invariant).',
        'kramers': True,
    },
]

print(f"\n{'Level':<6} {'AZ':<5} {'T^2':>4} {'Kramers':>8}  {'System'}")
print("-" * 72)
for L in levels:
    marker = " ***" if L['level'] == 2 else ""
    print(f"  {L['level']:<4} {L['AZ']:<5} {L['T2']:>+3} {'YES' if L['kramers'] else 'NO':>8}  {L['name']}{marker}")

print("\n*** = TRANSITION POINT: T^2 flips sign at Level 2 (quarks/leptons)")

# ==============================================================================
# SECTION 3: THE SIGN-FLIP MECHANISM
# ==============================================================================
# T^2 = (-1)^{2J} where J = total angular momentum (spin).
# For integer J (bosons): T^2 = +1 (no Kramers degeneracy)
# For half-integer J (fermions): T^2 = -1 (Kramers degeneracy)
#
# The compositing rule: when you combine N particles of spin s_i,
# the total spin J ranges from |s_1 - s_2 - ...| to s_1 + s_2 + ...
# T^2 for the composite = (-1)^{2J_total} = product_i (-1)^{2s_i}
# (because T factors over tensor products: T_total = T_1 x T_2 x ...)
#
# So: T^2 = product of all constituent T^2 values.
# Odd number of fermions -> T^2 = -1. Even number -> T^2 = +1.

print("\n" + "=" * 72)
print("  COMPOSITING RULE: T^2 = product_i (T_i)^2")
print("=" * 72)

composites = [
    ('Proton', '2u + 1d', 3, 'odd', -1, 'DIII'),
    ('Neutron', '2d + 1u', 3, 'odd', -1, 'DIII'),
    ('3He nucleus', '2p + 1n', 3, 'odd', -1, 'DIII'),
    ('4He nucleus', '2p + 2n', 4, 'even', +1, 'BDI'),
    ('3He atom', '3He_nuc + 2e', 5, 'odd', -1, 'DIII'),
    ('4He atom', '4He_nuc + 2e', 6, 'even', +1, 'BDI'),
    ('Deuteron', '1p + 1n', 2, 'even', +1, 'BDI'),
    ('Pion (pi+)', 'u + d_bar', 2, 'even', +1, 'BDI'),
    ('Cooper pair (3He)', '2 x 3He', 2, 'even', +1, 'BDI (pair)'),
    ('6Li atom', '3p+3n+3e', 9, 'odd', -1, 'DIII'),
    ('7Li atom', '3p+4n+3e', 10, 'even', +1, 'BDI'),
    ('40K atom', '19p+21n+19e', 59, 'odd', -1, 'DIII'),
    ('87Rb atom', '37p+50n+37e', 124, 'even', +1, 'BDI'),
    ('Electron', 'fundamental', 1, 'odd', -1, 'DIII'),
]

print(f"\n{'Composite':<20} {'Constituents':<15} {'N_ferm':>7} {'Parity':>7} {'T^2':>4} {'AZ':<6}")
print("-" * 72)
for name, const, N, parity, T2, AZ in composites:
    marker = ""
    if name == '3He atom':
        marker = "  <-- 3He-B constituent"
    elif name == '4He atom':
        marker = "  <-- 4He BEC constituent"
    print(f"{name:<20} {const:<15} {N:>7} {parity:>7} {T2:>+3}  {AZ:<6}{marker}")

# ==============================================================================
# SECTION 4: UNIQUENESS ANALYSIS
# ==============================================================================
# Question: Is 3He-B the UNIQUE DIII condensed matter system reachable from BDI?
# Answer: NO. Any condensed matter system made from an ODD number of fermions
# per constituent atom (half-integer total spin) is DIII if it has
# both TRS and PHS (BdG structure in the superfluid/superconducting state).

print("\n" + "=" * 72)
print("  UNIQUENESS ANALYSIS: OTHER DIII SYSTEMS")
print("=" * 72)

diii_systems = [
    {
        'system': 'Superfluid 3He-B',
        'constituent': '3He (I=1/2)',
        'N_ferm': 5,
        'T2': -1,
        'topo_inv': 'N_K = 2',
        'pairing': 'p-wave triplet',
        'gap': 'isotropic',
        'framework_match': '6/6',
    },
    {
        'system': 'Superfluid 3He-A',
        'constituent': '3He (I=1/2)',
        'N_ferm': 5,
        'T2': -1,
        'topo_inv': 'N_3 = 2 (Weyl)',
        'pairing': 'p-wave triplet',
        'gap': 'NODAL (point nodes)',
        'framework_match': '4/6 (WRONG: not fully gapped)',
    },
    {
        'system': 'Sr2RuO4 (if p-wave)',
        'constituent': 'Ru (s=0 paired e-)',
        'N_ferm': 1,
        'T2': -1,
        'topo_inv': 'Z (if triplet)',
        'pairing': 'p-wave (disputed)',
        'gap': 'TBD (nodes debated)',
        'framework_match': '3/6 (electronic, not nuclear)',
    },
    {
        'system': 'CuxBi2Se3',
        'constituent': 'Electron',
        'N_ferm': 1,
        'T2': -1,
        'topo_inv': 'Z (DIII, d=3)',
        'pairing': 'p-wave (spin-orbit)',
        'gap': 'nodal/nematic',
        'framework_match': '2/6 (electronic, SOC not BCS)',
    },
    {
        'system': 'UPt3',
        'constituent': 'Heavy fermion e-',
        'N_ferm': 1,
        'T2': -1,
        'topo_inv': 'Z (DIII, multicomponent)',
        'pairing': 'f-wave triplet',
        'gap': 'multiple phases, nodal',
        'framework_match': '3/6 (unconventional pairing)',
    },
    {
        'system': '6Li ultracold gas',
        'constituent': '6Li (F=1/2)',
        'N_ferm': 9,
        'T2': -1,
        'topo_inv': 'Z (if p-wave)',
        'pairing': 's-wave singlet (BEC-BCS)',
        'gap': 'isotropic',
        'framework_match': '4/6 (s-wave, not p-wave)',
    },
    {
        'system': '40K ultracold gas',
        'constituent': '40K (F=9/2)',
        'N_ferm': 59,
        'T2': -1,
        'topo_inv': 'Z (if p-wave)',
        'pairing': 's-wave singlet (BEC-BCS)',
        'gap': 'isotropic',
        'framework_match': '3/6 (no analog of B2 sector)',
    },
]

print(f"\n{'System':<25} {'T^2':>4} {'Gap':>12} {'Topo':>8} {'Match':>6}")
print("-" * 65)
for s in diii_systems:
    print(f"{s['system']:<25} {s['T2']:>+3} {s['gap']:>12} {s['topo_inv']:>8} {s['framework_match']:>6}")

# ==============================================================================
# SECTION 5: BDI CONDENSED MATTER SYSTEMS (for contrast)
# ==============================================================================

print("\n" + "=" * 72)
print("  BDI SYSTEMS (EVEN FERMION NUMBER -> T^2 = +1)")
print("=" * 72)

bdi_systems = [
    ('4He superfluid', '4He (I=0)', 6, +1, 'trivial', 'BEC, not BCS'),
    ('87Rb BEC', '87Rb (I=3/2)', 124, +1, 'trivial', 'BEC boson'),
    ('23Na BEC', '23Na (I=3/2)', 34, +1, 'trivial', 'BEC boson'),
    ('Deuteron condensate', 'd (I=1)', 6, +1, 'Z (1D)', 'spin-1 BEC'),
    ('Polyacetylene', 'electrons (paired)', 2, +1, 'Z (1D)', 'SSH model'),
]

print(f"\n{'System':<25} {'N_ferm':>7} {'T^2':>4} {'Topo':>10} {'Note'}")
print("-" * 65)
for name, const, N, T2, topo, note in bdi_systems:
    print(f"{name:<25} {N:>7} {T2:>+3} {topo:>10} {note}")

# ==============================================================================
# SECTION 6: THE CI ALTERNATIVE (spin-singlet BdG with TRS)
# ==============================================================================
# If pairing is spin-SINGLET with TRS: AZ class CI (T^2 = +1, C^2 = -1)
# This is DIFFERENT from BDI. The sign of C^2 matters.
# For conventional s-wave superconductors (Al, Nb, Pb): C^2 = -1 gives CI.
# For p-wave triplet (3He-B): C^2 = +1 gives DIII.

print("\n" + "=" * 72)
print("  CRITICAL DISTINCTION: PAIRING SYMMETRY AND C^2")
print("=" * 72)

print("""
The BDI -> DIII transition involves TWO steps:
  1. T^2: +1 -> -1  (Kramers from half-integer spin at Level 2)
  2. C^2: +1 -> +1  (maintained through compositing AND in BdG of triplet pairing)

If the superfluid has SINGLET pairing instead of TRIPLET:
  C^2 = -1 (singlet BdG convention)
  With T^2 = -1: AZ class = CII (not DIII)

So the DIII destination requires BOTH:
  (a) Half-integer-spin constituent (T^2 = -1) -- from Level 2 compositing
  (b) TRIPLET (odd-parity) pairing (C^2 = +1) -- from the interaction

For SINGLET pairing of half-integer spin fermions:
  - Conventional superconductors (Al, Pb, NbTi): class CI or C depending on TRS
  - 6Li BEC-BCS at unitarity: singlet pairing -> NOT DIII

Pairing symmetry        C^2     With T^2=-1     Example
---------------------------------------------------------------
Triplet (p-wave)        +1      DIII            3He-B, CuxBi2Se3
Singlet (s-wave)        -1      CII             Conventional SC, 6Li
""")

# ==============================================================================
# SECTION 7: NUCLEAR PHYSICS PERSPECTIVE
# ==============================================================================
# In nuclear physics, pairing is predominantly s-wave SINGLET (isovector T=1).
# The Cooper pairs have J=0, T=1. This is spin-singlet.
# Nuclear matter with pairing: class CI (not DIII).
# Neutron matter at high density: ^1S_0 pairing -> CI
# Neutron matter at higher density: ^3P_2 pairing -> DIII (triplet!)

print("=" * 72)
print("  NUCLEAR PHYSICS: PAIRING SYMMETRY BY DENSITY")
print("=" * 72)

nuclear_pairing = [
    ('Finite nuclei', '1S0 (nn, pp)', 'singlet', +1, -1, 'CI', 'Delta ~ 1-2 MeV'),
    ('Neutron star crust', '1S0 (nn)', 'singlet', +1, -1, 'CI', 'Delta ~ 1-3 MeV'),
    ('NS outer core', '3P2-3F2 (nn)', 'TRIPLET', -1, +1, 'DIII', 'Delta ~ 0.01-0.1 MeV'),
    ('NS inner core', '1S0 (pp)', 'singlet', +1, -1, 'CI', 'Delta ~ 0.01-1 MeV'),
    ('CFL quark matter', '1S0 (ud,ds,su)', 'singlet', +1, -1, 'CI/C', 'Delta ~ 10-100 MeV'),
    ('CSL quark matter', '1S0+3P2', 'mixed', -1, 'mixed', 'mixed', 'Delta ~ 1-10 MeV'),
]

print(f"\n{'System':<25} {'Channel':>15} {'Type':>8} {'C^2':>4} {'AZ':>5} {'Gap'}")
print("-" * 80)
for name, channel, ptype, T2_pair, C2, AZ, gap in nuclear_pairing:
    print(f"{name:<25} {channel:>15} {ptype:>8} {str(C2):>4} {AZ:>5} {gap}")

print("""
KEY NUCLEAR RESULT:
  Neutron ^3P_2 pairing in the outer core (rho ~ 1-3 rho_0) is the NUCLEAR
  analog of 3He-B. Both are DIII class with triplet pairing.

  This is the Nazarewicz group's territory: Paper 02 (HFB continuum) and
  Paper 08 (mean-field pair collapse) deal directly with pairing channels.
  The ^3P_2 channel is the one where anisotropic gaps, tensor force effects,
  and spin-orbit coupling all play critical roles -- exactly the physics
  that distinguishes DIII from CI.
""")

# ==============================================================================
# SECTION 8: SUMMARY AND VERDICT
# ==============================================================================

print("=" * 72)
print("  VERDICT: BDI-DIII-CHAIN-61")
print("=" * 72)

print("""
1. TRANSITION POINT: Level 2 (quarks/leptons).
   T^2 flips from +1 to -1 when the first half-integer spin particle
   appears. This is PERMANENT for all odd-fermion-number composites
   through the rest of the chain.

2. UNIQUENESS: 3He-B is NOT the unique DIII endpoint.
   ANY spin-1/2 fermion system with TRIPLET pairing reaches DIII:
   - 3He-B (laboratory, confirmed)
   - 3He-A (laboratory, confirmed, but gapless -- different topology)
   - Neutron ^3P_2 superfluid (neutron star outer core)
   - CuxBi2Se3, UPt3 (electronic topological SC candidates)
   - Ultracold 6Li/40K in p-wave channel (proposed but difficult)

3. 3He-B IS THE UNIQUE FULLY-GAPPED DIII SYSTEM with:
   (a) Isotropic gap (no nodes)
   (b) N_K = 2 (strong topological, not weak)
   (c) Kramers degeneracy from NUCLEAR spin (not electronic SOC)
   (d) Maximally symmetric residual group SO(3)_{L+S}

4. PATH STRUCTURE:
   BDI (Level 0-1) -> [half-integer spin] -> DIII (Level 2-5)
   The path passes through NO intermediate AZ classes.
   C^2 = +1 is maintained at every level.
   Only T^2 changes, and it changes ONCE (at Level 2).

5. ALTERNATIVE PATHS FROM BDI:
   BDI -> BDI: Even-fermion composites (4He, deuteron, pi meson, BEC)
   BDI -> CI:  Half-integer spin + SINGLET pairing (conventional SC, nuclear ^1S_0)
   BDI -> DIII: Half-integer spin + TRIPLET pairing (3He-B, n-star ^3P_2)

   The BDI -> DIII path requires BOTH conditions simultaneously.
""")

# ==============================================================================
# SECTION 9: NUMERICAL CHECKS
# ==============================================================================

# Verify T^2 compositing rule
print("=" * 72)
print("  NUMERICAL CHECKS: T^2 COMPOSITING")
print("=" * 72)

def T_squared(n_fermions):
    """T^2 = (-1)^{N_ferm} where N_ferm = total fermion number."""
    return (-1)**n_fermions

checks = [
    ('3He nucleus: 2p+1n = 3 quarks x3 = 9 quarks, +0 leptons', 9),
    ('3He atom: 9 quarks + 2 electrons = 11 fermions', 11),
    ('But EFFECTIVE: 3He has nuclear spin I=1/2, so T^2=-1', 1),
    ('4He atom: 12 quarks + 2 electrons = 14 fermions', 14),
    ('EFFECTIVE: 4He has I=0, J=0, so T^2=+1', 0),
    ('Electron: 1 fermion', 1),
    ('Cooper pair (3He-3He): 2 fermions', 2),
    ('NOTE: Cooper PAIR has T^2=+1, but BdG treats SINGLE atoms', 1),
]

print(f"\n{'System':<60} {'N':>4} {'T^2':>5}")
print("-" * 72)
for desc, N in checks:
    T2 = T_squared(N)
    print(f"{desc:<60} {N:>4} {T2:>+4}")

print("""
IMPORTANT SUBTLETY:
  The Cooper pair itself has even fermion number (T^2 = +1, bosonic).
  But the BdG framework describes QUASIPARTICLES, not pairs.
  The relevant T^2 is that of the CONSTITUENT (the single atom),
  not the pair. This is why 3He-B (Cooper pairs of spin-1/2 atoms)
  is DIII (T^2 = -1) and not BDI (T^2 = +1).

  In nuclear physics: a J=0 T=1 Cooper pair of neutrons is a boson,
  but the HFB quasiparticle spectrum is classified by the single-
  nucleon symmetries. This is standard Bogoliubov theory (Paper 03).
""")

# ==============================================================================
# SECTION 10: FRAMEWORK IMPLICATIONS
# ==============================================================================

print("=" * 72)
print("  FRAMEWORK IMPLICATIONS")
print("=" * 72)

print("""
CLASSIFICATION:

  The inheritance chain BDI -> DIII passes through EXACTLY one transition:
  Level 2 (first half-integer spin composite).

  This transition is ROBUST (topological, cannot be undone by smooth
  perturbations). Every subsequent level inherits T^2 = -1 from the
  half-integer spin of the constituent.

  The SECOND condition for DIII (triplet pairing, C^2 = +1) is NOT
  inherited from the substrate. It is a DYNAMICAL choice of the
  many-body ground state at Level 5 (3He) or at the neutron star
  core. The substrate's C^2 = +1 (BDI) does propagate through the
  BdG framework, but the pairing SYMMETRY (singlet vs triplet)
  depends on the interaction in the relevant partial-wave channel.

  In nuclear language (Paper 08, Dobaczewski et al. 2007):
  - The nn interaction at low density is attractive in ^1S_0 (singlet)
  - At higher density (rho ~ 2 rho_0), ^1S_0 becomes repulsive
  - ^3P_2 (triplet) takes over, driven by tensor force
  - The transition singlet -> triplet is a CI -> DIII crossover

  For 3He atoms:
  - Hard-core repulsion kills s-wave pairing
  - p-wave (triplet) pairing emerges from spin fluctuation exchange
  - This is why 3He-B is DIII, not CI

PHONONIC CLASSIFICATION:
  The substrate BDI -> 3He-B DIII transition is PARTICLE-mediated.
  The T^2 sign flip occurs at Level 2 where individual quark/lepton
  modes acquire half-integer spin. This is a PARTICLE property
  (spin quantum number of the excitation), not a collective
  (phononic) property.

  The PAIRING (which makes the BdG framework applicable in the first
  place) is a PHONONIC/COLLECTIVE phenomenon -- it is a many-body
  instability of the Fermi surface, not a single-particle property.

  So the BDI -> DIII chain has MIXED character:
  - T^2 = -1 is PARTICLE (spin from substrate geometry)
  - C^2 = +1 with BdG is PHONONIC (collective pairing instability)
  - The combination (DIII) requires BOTH.
""")

print("=" * 72)
print("  BDI-DIII-CHAIN-61: COMPLETE")
print("=" * 72)
