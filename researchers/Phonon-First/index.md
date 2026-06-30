# Phonon-First Paper Index

**Collection**: Cross-Domain Foundations for Phonon-Exflation Cosmology
**Papers**: 32 (1976-2026)
**From PDF**: 20 | **Journal-only stubs**: 12
**Primary domain**: Acoustic/analogue gravity, superfluid cosmology, NCG spectral action, flat-band BCS, Josephson arrays, topological solitons, spectral dimension, KK geometry
**Project relevance**: The 8-pillar foundational reading list spanning all domains that intersect the phonon-exflation mechanism chain (instanton → RPA → Turing → van Hove → BCS) and the acoustic cosmology pivot
**Rebuilt**: 2026-03-27 from arXiv source PDFs

---

## Dependency Graph

```
PILLAR I: ACOUSTIC / ANALOGUE GRAVITY (BLV metric backbone)
  21 (Unruh 1981) --> 03 (Visser 1998) --> 01 (BLV Review 2005)
                       03 --> 02 (BLV FRW 2003) --> 04 (Viermann Exp 2022)
                       |
  [Cross to Pillar II]  |
                       v
PILLAR II: SUPERFLUID COSMOLOGY (Volovik program)
  22 (Volovik Monograph) <-- 21 (Unruh: acoustic horizon idea)
  05 (Volovik Review 2000) -- condensed themes from 22
  22 --> 06 (Jacobson-Volovik DW 1998) --> 07 (Volovik Lifshitz 2017)
  22 --> 17 (Volovik Flat Band 2019)
         |                                    |
  [Cross to Pillar IV]                [Cross to Pillar IV]
         v                                    v
PILLAR IV: FLAT BANDS, VAN HOVE, BCS
  17 --> 12 (Luo Kagome 2025)
  17 --> 24 (Markiewicz Cuprates 2023)
  07 --> 13 (Wu 3D vHs 2024)
  17 --> 14 (Peotta-Torma Flat Band SF 2015)
         |
  [Cross to Pillar V]
         v
PILLAR V: JOSEPHSON ARRAYS & MOTT (N_pair=1)
  15 (Fazio-vdZant Review 2001)
  25 (Bradley-Doniach 1984) --> 26 (Haviland 1D QPT 2001)
  16 (Greiner Mott 2002)
         |
  [Cross to Pillar VI via phase-slip / soliton duality]
         v
PILLAR VI: TOPOLOGICAL SOLITONS & DOMAIN WALLS
  27 (Manton-Sutcliffe 2004) <-- independent (monograph)
  28 (Jackiw-Rebbi 1976) <-- independent (foundational)
  29 (Vachaspati 2006) <-- 28 (Jackiw-Rebbi: zero modes at walls)
  29 <-- 27 (Manton-Sutcliffe: BPS bounds, moduli space)
         |
  [Cross to Pillar VII via Kibble-Zurek defect formation]
         v
PILLAR VII: SPECTRAL DIMENSION FLOW
  20 (AJL CDT 2005) --> 18 (Carlip Review 2017)
  19 (COT Discrete Flow 2015) --> 18 (Carlip Review 2017)
         |
  [Cross to Pillar VIII via discrete-to-continuum emergence]
         v
PILLAR VIII: KALUZA-KLEIN ON LIE GROUPS (Jensen geometry)
  31 (Ziller 1982) --> 30 (Baptista 2005)
  30 uses 31's Einstein metric classification for SU(3)

NCG BACKBONE (Pillar III):
  08 (CC Spectral Action 1997) --> 09 (CCM Gravity+SM 2007)
  09 --> 23 (vS Textbook 2015)
  08 --> 10 (CC Resilience 2012)
  08 --> 11 (Boyle-Farnsworth Division Algebras 2014)
  08 --> 32 (Martinetti Twisted SM 2026)
  23 --> [finite-density BdG extension links to Pillars IV-V]

MAJOR CROSS-PILLAR BRIDGES:
  05 (Volovik review) bridges I <-> II (acoustic metric in superfluid)
  06 (Jacobson-Volovik) bridges II <-> VI (domain wall Hawking radiation)
  07 (Volovik Lifshitz) bridges II <-> IV (Lifshitz transition = vHs)
  17 (Volovik Flat Band) bridges II <-> IV (flat band BCS from superfluid)
  23 (vS textbook Ch.16) bridges III <-> IV (finite-density NCG = BCS)
  25 (Bradley-Doniach) bridges V <-> VI (phase-slip / soliton duality)
  29 (Vachaspati) bridges VI <-> VII (Kibble-Zurek defect counting)
  30 (Baptista) bridges VIII <-> III (KK geometry feeds spectral action)
  04 (Viermann) bridges I <-> IV (experimental BEC pair creation)
  14 (Peotta-Torma) bridges IV <-> V (geometric superfluidity)
```

---

## Topic Map

### Pillar I: Acoustic / Analogue Gravity
Papers: 01, 02, 03, 04, 21
The BLV (Barcelo-Liberati-Visser) acoustic metric framework: phonons in moving fluids propagate on an effective curved spacetime. Establishes the mathematical machinery (effective metric, surface gravity, Hawking temperature) that the framework transports from laboratory fluids to the BCS condensate on SU(3). Paper 04 (Viermann 2022) provides the first direct experimental observation of cosmological pair creation in an expanding BEC — the proof-of-concept for the phonon-exflation mechanism.

### Pillar II: Superfluid Cosmology & Emergent Spacetime
Papers: 05, 06, 07, 17, 22
Volovik's program: the universe as a superfluid vacuum. Paper 22 is the monograph establishing that Weyl fermions, gauge fields, and spacetime all emerge from p-wave superfluid order-parameter texture. Paper 05 is a condensed review. Papers 06-07 extend to domain-wall horizons and Lifshitz transitions. Paper 17 connects flat bands to Planckian metals. This pillar provides the conceptual parent of phonon-exflation — the framework is Volovik's program applied to BCS on SU(3).

### Pillar III: Noncommutative Geometry & Spectral Action
Papers: 08, 09, 10, 11, 23, 32
The Chamseddine-Connes spectral action principle: the Standard Model Lagrangian emerges from Tr f(D²/Λ²) on the product geometry M⁴ × F with KO-dimension 6. Paper 23 (van Suijlekom textbook) extends to finite-density (chemical potential, BdG structure). Paper 10 resolves the Higgs mass discrepancy via the sigma field. Paper 11 (Boyle-Farnsworth) reformulates using division algebras. Paper 32 (Martinetti 2026) explores twisted spectral triples and Krein structure. This pillar provides the mathematical backbone: the spectral triple, the heat kernel expansion, and the Seeley-DeWitt coefficients.

### Pillar IV: Flat Bands, Van Hove Singularities & BCS
Papers: 12, 13, 14, 17, 24
The condensed-matter backbone for the BCS instability mechanism. Van Hove singularities (divergent DOS at saddle points) drive strong-coupling physics even from weak initial interactions. Paper 12 (Luo 2025) observes vHs-driven flat bands in kagome superconductors. Paper 24 (Markiewicz 2023) shows T_c is maximized at vHs crossing. Paper 13 (Wu 2024) extends to 3D. Paper 14 (Peotta-Torma 2015) proves flat-band superfluidity is controlled by the quantum metric, not kinetic energy. Paper 17 (Volovik) connects to Planckian metals.

### Pillar V: Josephson Arrays, Mott Insulators & Quantum Walkers
Papers: 15, 16, 25, 26
The N_pair=1 regime: quantum phase transitions in coupled-pair systems. Paper 15 (Fazio-vdZant review) maps the full phase diagram of JJ arrays (superconductor-insulator, BKT, Mott). Paper 16 (Greiner 2002) provides the first direct observation of the superfluid-to-Mott transition in optical lattices. Papers 25-26 establish the phase-slip / charge-soliton duality and the BKT critical exponent in 1D.

### Pillar VI: Topological Solitons & Domain Walls
Papers: 27, 28, 29
The topological protection mechanism. Paper 27 (Manton-Sutcliffe) provides the mathematical framework: kinks, BPS bounds, moduli space geometry, instanton classification. Paper 28 (Jackiw-Rebbi 1976) proves that fermion zero modes at kink cores carry fractional quantum number ½ — the mechanism by which K₇ charges emerge from Cooper pair disruption. Paper 29 (Vachaspati 2006) develops Kibble-Zurek defect formation dynamics.

### Pillar VII: Spectral Dimension Flow
Papers: 18, 19, 20
UV-IR dimensional reduction in quantum gravity. Paper 20 (AJL 2005) discovers d_s: 4 → 2 flow in CDT. Paper 19 (COT 2015) confirms this in discrete quantum geometry superpositions. Paper 18 (Carlip 2017) reviews the universality of this flow across CDT, asymptotic safety, LQG, Horava-Lifshitz, and causal sets.

### Pillar VIII: Kaluza-Klein on Lie Groups & Jensen Geometry
Papers: 30, 31
The internal-space geometry. Paper 31 (Ziller 1982) classifies all Einstein metrics on compact Lie groups. Paper 30 (Baptista 2005) develops the Jensen deformation on SU(3), proves volume preservation, and formulates the null-geodesic hypothesis. These define the geometric arena where phonon-exflation operates.

---

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| Acoustic metric / BLV formalism | 01, 03, 21 | CRITICAL |
| Hawking radiation from defects | 03, 06, 21 | CRITICAL |
| FRW cosmology from BEC expansion | 02, 04 | HIGH |
| Experimental pair creation in BEC | 04 | HIGH |
| Volovik superfluid universe program | 05, 06, 07, 17, 22 | CRITICAL |
| Lifshitz transitions / Fermi surface topology | 07, 13 | HIGH |
| Spectral action / NCG foundations | 08, 09, 23 | CRITICAL |
| Finite-density NCG / BdG spectral action | 23 | CRITICAL |
| Higgs from geometry / sigma field | 10, 11 | HIGH |
| Twisted spectral triples / Krein space | 32 | MEDIUM |
| Van Hove singularity / flat-band BCS | 12, 13, 14, 17, 24 | CRITICAL |
| Quantum metric / geometric superfluidity | 14 | CRITICAL |
| Josephson array phase transitions | 15, 25, 26 | HIGH |
| Superfluid-Mott transition / Bose-Hubbard | 16 | HIGH |
| Phase-slip / charge-soliton duality | 25, 26 | HIGH |
| Topological solitons / BPS bounds | 27 | MEDIUM |
| Fractional fermion number / zero modes | 28 | CRITICAL |
| Kibble-Zurek defect formation | 29 | CRITICAL |
| Spectral dimension flow / d_s: 4→2 | 18, 19, 20 | HIGH |
| Jensen deformation on SU(3) | 30, 31 | CRITICAL |
| Einstein metrics on Lie groups | 31 | HIGH |
| K₇ charge emergence mechanism | 06, 28, 29 | CRITICAL |
| GGE permanence / integrability | 04, 05, 28, 29 | HIGH |
| Flat band Planckian / SYK connection | 17 | CRITICAL |

---

## Paper Entries

### Paper 01: Analogue Gravity (BLV Review) [CRITICAL]
- **File**: `01_2005_Barcelo_Liberati_Visser_Analogue_Gravity.md`
- **arXiv**: gr-qc/0505065
- **Year**: 2005
- **Authors**: C. Barcelo, S. Liberati, M. Visser
- **Relevance**: CRITICAL
- **Tags**: acoustic metric, Hawking radiation, effective spacetime, BEC, universality
- **Pillar**: I

**Summary**: Definitive review of analogue gravity. Derives acoustic metric theorem, Hawking temperature from surface gravity, and catalogs realizations across superfluids, BECs, photonic media. Establishes that spacetime emergence is a general principle.

---

### Paper 02: Analogue Models for FRW Cosmologies [HIGH]
- **File**: `02_2003_Barcelo_Liberati_Visser_Analogue_FRW.md`
- **arXiv**: gr-qc/0305061
- **Year**: 2003
- **Authors**: C. Barcelo, S. Liberati, M. Visser
- **Relevance**: HIGH
- **Tags**: FRW cosmology, BEC expansion, Feshbach resonance, particle creation
- **Pillar**: I

**Summary**: Two routes to analogue FRW: explosion geometry and varying speed of sound via Feshbach resonance. Derives particle creation window and timescale requirements.

---

### Paper 03: Acoustic Black Holes [CRITICAL]
- **File**: `03_1998_Visser_Acoustic_Black_Holes.md`
- **arXiv**: gr-qc/9712010
- **Year**: 1998
- **Authors**: M. Visser
- **Relevance**: CRITICAL
- **Tags**: acoustic metric, Painleve-Gullstrand, vortex geometry, surface gravity
- **Pillar**: I

**Summary**: Rigorous derivation of acoustic metric from fluid mechanics. Establishes Painleve-Gullstrand connection, vortex (draining bathtub) geometry, and position-dependent speed-of-sound surface gravity formula.

---

### Paper 04: Quantum Field Simulator for Dynamics in Curved Spacetime [HIGH]
- **File**: `04_2022_Viermann_Quantum_Field_Simulator.md`
- **arXiv**: 2202.10399
- **Year**: 2022
- **Authors**: C. Viermann et al.
- **Relevance**: HIGH
- **Tags**: BEC experiment, pair creation, curved spacetime, Sakharov oscillations
- **Pillar**: I

**Summary**: First experimental confirmation of cosmological particle pair production in expanding BEC. Demonstrates positive and negative curvature spacetimes and Sakharov oscillations. Proof-of-concept for phonon-exflation.

---

### Paper 05: Superfluid Analogies of Cosmological Phenomena [CRITICAL]
- **File**: `05_2000_Volovik_Superfluid_Analogies.md`
- **arXiv**: gr-qc/0005091
- **Year**: 2000
- **Authors**: G. E. Volovik
- **Relevance**: CRITICAL
- **Tags**: superfluid vacuum, anti-grand-unification, vacuum energy, Fermi point, universality
- **Pillar**: II

**Summary**: Condensed review of Volovik's universe-as-superfluid program. Anti-grand-unification paradigm, two-fluid hydrodynamics as effective gravity, vacuum energy nullification (ε̃ = 0), three universality classes (Fermi surface/gapped/Fermi point), SM as Fermi point class.

---

### Paper 06: Event Horizons and Ergoregions in ³He [HIGH]
- **File**: `06_1998_Jacobson_Volovik_Event_Horizons_3He.md`
- **arXiv**: cond-mat/9801308
- **Year**: 1998
- **Authors**: T. A. Jacobson, G. E. Volovik
- **Relevance**: HIGH
- **Tags**: domain wall horizon, Schwinger radiation, ergoregion, ³He-A, charged BH analog
- **Pillar**: II

**Summary**: Moving ³He-A soliton as charged rotating BH analogue. Predicts Hawking radiation at T_H ≈ 5 μK, Schwinger pair creation from effective electromagnetic field, and ergoregion instability.

---

### Paper 07: Exotic Lifshitz Transitions in Topological Materials [HIGH]
- **File**: `07_2017_Volovik_Exotic_Lifshitz_Transitions.md`
- **arXiv**: 1701.06435
- **Year**: 2017
- **Authors**: G. E. Volovik
- **Relevance**: HIGH
- **Tags**: Lifshitz transition, topological invariants, Weyl points, flat band, hierarchy problem
- **Pillar**: II

**Summary**: Classification of Lifshitz transitions by topological invariants (N₁, N₂, N₃). Shows flat bands enhance T_c, BH horizon as type-I/type-II Weyl transition surface, and hierarchy problem from topological proximity to flat-band transition.

---

### Paper 08: The Spectral Action Principle [CRITICAL]
- **File**: `08_1997_Chamseddine_Connes_Spectral_Action.md`
- **arXiv**: hep-th/9606001
- **Year**: 1997
- **Authors**: A. H. Chamseddine, A. Connes
- **Relevance**: CRITICAL
- **Tags**: spectral action, heat kernel, Seeley-DeWitt, GUT, Higgs, conformal coupling
- **Pillar**: III

**Summary**: Foundational paper proposing Tr χ(D/Λ) + ⟨ψ, Dψ⟩. Full heat kernel expansion with a₀, a₂, a₄ coefficients. GUT coupling unification g₃² = g₂² = (5/3)g₁², conformal coupling ξ₀ = 1/6.

---

### Paper 09: Gravity and the Standard Model with Neutrino Mixing [CRITICAL]
- **File**: `09_2007_Chamseddine_Connes_Marcolli_Gravity_SM.md`
- **arXiv**: hep-th/0610241
- **Year**: 2007
- **Authors**: A. H. Chamseddine, A. Connes, M. Marcolli
- **Relevance**: CRITICAL
- **Tags**: spectral triple, KO-dimension 6, neutrino mixing, see-saw, gauge unification
- **Pillar**: III

**Summary**: Definitive 71-page construction. Left-right symmetric algebra, unique subalgebra selection, KO-dimension 6, bimodule classification, full normalized SM action, Pfaffian fermion doubling, see-saw mechanism.

---

### Paper 10: Resilience of the Spectral Standard Model [HIGH]
- **File**: `10_2012_Chamseddine_Connes_Resilience_Spectral_SM.md`
- **arXiv**: 1208.1030
- **Year**: 2012
- **Authors**: A. H. Chamseddine, A. Connes
- **Relevance**: HIGH
- **Tags**: Higgs mass, sigma field, quartic couplings, RG evolution
- **Pillar**: III

**Summary**: Resolves Higgs mass crisis post-LHC. Introduces Higgs-singlet potential from spectral action with mass reduction factor √(1 - λ²_{hσ}/(λ_h λ_σ)) ≈ 0.78, yielding m_H ≈ 125.5 GeV.

---

### Paper 11: Non-Commutative Geometry, Non-Associative Geometry and the Standard Model [HIGH]
- **File**: `11_2014_Boyle_Farnsworth_Division_Algebras.md`
- **arXiv**: 1401.5083
- **Year**: 2014
- **Authors**: L. Boyle, S. Farnsworth
- **Relevance**: HIGH
- **Tags**: division algebras, order-two constraint, Yukawa reduction, J reinterpretation
- **Pillar**: III

**Summary**: Reformulates NCG SM via algebra B = ΩA ⊕ H. New order-two constraint [[D, L_a], [D, R_b]] = 0 eliminates 7 unwanted parameters. J reinterpreted as anti-automorphism.

---

### Paper 12: Van Hove Singularity-Driven Flat Bands in Kagome Superconductors [HIGH]
- **File**: `12_2025_Luo_Van_Hove_Flat_Bands_Kagome.md`
- **arXiv**: 2403.06085
- **Year**: 2024
- **Authors**: H. Luo et al.
- **Relevance**: HIGH
- **Tags**: kagome, van Hove, flat band, AV₃Sb₅, ARPES
- **Pillar**: IV

**Summary**: ARPES observation of vHs-driven flat band emergence in kagome superconductors AV₃Sb₅. Multiple vHs pinned to Fermi level drive electronic instabilities and superconductivity.

---

### Paper 13: The Discovery of Three-Dimensional Van Hove Singularity [HIGH]
- **File**: `13_2024_Wu_3D_Van_Hove_Singularity.md`
- **arXiv**: 2304.07043
- **Year**: 2024
- **Authors**: W. Wu et al.
- **Relevance**: HIGH
- **Tags**: 3D VHS, EuCd₂As₂, Weyl semimetal, magneto-infrared, topological
- **Pillar**: IV

**Summary**: First observation of 3D Van Hove singularity in topological magnet EuCd₂As₂ via magneto-infrared spectroscopy. Magnetic field tunes Weyl bands to form 3D VHS.

---

### Paper 14: Superfluidity in Topologically Nontrivial Flat Bands [CRITICAL]
- **File**: `14_2015_Peotta_Torma_Superfluidity_Flat_Bands.md`
- **arXiv**: 1506.02815
- **Year**: 2015
- **Authors**: S. Peotta, P. Törmä
- **Relevance**: CRITICAL
- **Tags**: flat band, quantum metric, Chern number, superfluid weight, Harper-Hubbard
- **Pillar**: IV

**Summary**: Proves flat-band superfluidity controlled by quantum metric, not kinetic energy. Bound D_s ≥ |C| from Chern number. Even a completely flat band carries finite superfluid current if topologically nontrivial.

---

### Paper 15: Quantum Phase Transitions and Vortex Dynamics in Superconducting Networks [HIGH]
- **File**: `15_2001_Fazio_van_der_Zant_JJ_Arrays.md`
- **arXiv**: cond-mat/0011152
- **Year**: 2001
- **Authors**: R. Fazio, H. van der Zant
- **Relevance**: HIGH
- **Tags**: Josephson arrays, QPT, BKT, vortex dynamics, superconductor-insulator
- **Pillar**: V

**Summary**: Comprehensive review of quantum phase transitions in JJ arrays. Full phase diagram including SI transition, BKT, vortex dynamics, charge-vortex duality, and dissipation effects.

---

### Paper 16: Quantum Phase Transition from Superfluid to Mott Insulator [HIGH]
- **File**: `16_2002_Greiner_Superfluid_Mott_Transition.md`
- **arXiv**: 2506.21303
- **Year**: 2002
- **Authors**: M. Greiner, O. Mandel, T. Esslinger, T. W. Hänsch, I. Bloch
- **Relevance**: HIGH
- **Tags**: Mott insulator, BEC, optical lattice, quantum phase transition, Bose-Hubbard
- **Pillar**: V

**Summary**: First direct observation of superfluid-to-Mott insulator transition in 3D optical lattice. Reversible transition driven by lattice depth, with gap in excitation spectrum.

---

### Paper 17: Flat Band and Planckian Metal [CRITICAL]
- **File**: `17_2019_Volovik_Flat_Band_Planckian.md`
- **arXiv**: 1907.11515
- **Year**: 2019
- **Authors**: G. E. Volovik
- **Relevance**: CRITICAL
- **Tags**: flat band, Planckian metal, SYK model, Khodel fermion condensate, T-linear resistivity
- **Pillar**: II/IV (bridge)

**Summary**: Connects flat bands to Planckian dissipation via SYK model. Flat band produces Khodel fermion condensate and T-linear resistivity. Bridges superfluid cosmology to condensed matter BCS.

---

### Paper 18: Spontaneous Dimensional Reduction in Quantum Gravity [HIGH]
- **File**: `18_2017_Carlip_Dimensional_Reduction_QG.md`
- **arXiv**: 1605.05694
- **Year**: 2016
- **Authors**: S. Carlip
- **Relevance**: HIGH
- **Tags**: dimensional reduction, spectral dimension, d_s 4→2, asymptotic safety, BKL
- **Pillar**: VII

**Summary**: Reviews universal d_s: 4→2 flow across 10+ independent QG approaches. Two proposed mechanisms: UV scale invariance (asymptotic safety) and asymptotic silence (BKL behavior).

---

### Paper 19: Dimensional Flow in Discrete Quantum Geometries [HIGH]
- **File**: `19_2015_Calcagni_Oriti_Thurigen_Dimensional_Flow.md`
- **arXiv**: 1412.8390
- **Year**: 2015
- **Authors**: G. Calcagni, D. Oriti, J. Thürigen
- **Relevance**: HIGH
- **Tags**: spectral dimension, discrete geometry, quantum superposition, walk dimension
- **Pillar**: VII

**Summary**: Individual lattice states show NO genuine dimensional flow (only artifacts). Quantum superpositions over different complexes produce true flow. Walk dimension d_w = 2 universally. True fractal at α = 1 reproducing d_S ≈ 2.

---

### Paper 20: Spectral Dimension of the Universe [HIGH]
- **File**: `20_2005_Ambjorn_Jurkiewicz_Loll_Spectral_Dimension.md`
- **arXiv**: hep-th/0505113
- **Year**: 2005
- **Authors**: J. Ambjorn, J. Jurkiewicz, R. Loll
- **Relevance**: HIGH
- **Tags**: CDT, spectral dimension, Monte Carlo, dimensional reduction, self-renormalization
- **Pillar**: VII

**Summary**: Original discovery of scale-dependent spectral dimension in CDT Monte Carlo. D_S(∞) = 4.02 ± 0.1, D_S(0) = 1.80 ± 0.25. Fit: D_S(σ) = 4.02 - 119/(54+σ).

---

### Paper 21: Experimental Black-Hole Evaporation? [CRITICAL] — STUB
- **File**: `21_1981_Unruh_Experimental_Black_Hole_Evaporation.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1981
- **Authors**: W. G. Unruh
- **Relevance**: CRITICAL
- **Tags**: sonic horizon, Hawking radiation, founding paper, acoustic metric
- **Pillar**: I (founding)
- **Status**: Journal-only (PRL 46:1351)

---

### Paper 22: The Universe in a Helium Droplet [CRITICAL] — STUB
- **File**: `22_2003_Volovik_Universe_Helium_Droplet.md`
- **arXiv**: N/A (OUP monograph, ISBN 978-0198507826)
- **Year**: 2003
- **Authors**: G. E. Volovik
- **Relevance**: CRITICAL
- **Tags**: superfluid vacuum, emergent gravity, Weyl fermions, cosmological constant
- **Pillar**: II (founding)
- **Status**: Book. Partial coverage via paper 05 (gr-qc/0005091)

---

### Paper 23: Noncommutative Geometry and Particle Physics [CRITICAL] — STUB
- **File**: `23_2015_van_Suijlekom_NCG_Particle_Physics.md`
- **arXiv**: N/A (Springer textbook, ISBN 978-9401791618)
- **Year**: 2015
- **Authors**: W. D. van Suijlekom
- **Relevance**: CRITICAL
- **Tags**: spectral triple, KO-dimension, heat kernel, BdG extension, Ch.16
- **Pillar**: III
- **Status**: Book. Key results covered by papers 08-11

---

### Paper 24: Cuprates Van Hove Flat Band [HIGH] — STUB
- **File**: `24_2023_Markiewicz_Cuprates_Van_Hove_Flat_Band.md`
- **arXiv**: N/A (journal-only)
- **Year**: 2023
- **Authors**: R. S. Markiewicz et al.
- **Relevance**: HIGH
- **Tags**: cuprates, van Hove, T_c, flat band
- **Pillar**: IV
- **Status**: Journal-only (Commun. Phys. 6:268)

---

### Paper 25: Quantum Fluctuations in Chains of Josephson Junctions [HIGH] — STUB
- **File**: `25_1984_Bradley_Doniach_JJ_Chain_Fluctuations.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1984
- **Authors**: R. M. Bradley, S. Doniach
- **Relevance**: HIGH
- **Tags**: JJ chain, phase-slip, charge-soliton duality, quantum fluctuations
- **Pillar**: V
- **Status**: Journal-only (PRB 30:1138)

---

### Paper 26: 1D Josephson Junction Quantum Phase Transition [HIGH] — STUB
- **File**: `26_2001_Haviland_1D_JJ_QPT.md`
- **arXiv**: N/A (journal-only)
- **Year**: 2001
- **Authors**: D. B. Haviland et al.
- **Relevance**: HIGH
- **Tags**: 1D JJ, BKT, superconductor-insulator, critical exponent
- **Pillar**: V
- **Status**: Journal-only (Physica C 352:55)

---

### Paper 27: Topological Solitons [MEDIUM] — STUB
- **File**: `27_2004_Manton_Sutcliffe_Topological_Solitons.md`
- **arXiv**: N/A (CUP monograph)
- **Year**: 2004
- **Authors**: N. S. Manton, P. M. Sutcliffe
- **Relevance**: MEDIUM
- **Tags**: kinks, BPS bounds, moduli space, instanton, Skyrmion
- **Pillar**: VI
- **Status**: Book

---

### Paper 28: Solitons with Fermion Number ½ [CRITICAL] — STUB
- **File**: `28_1976_Jackiw_Rebbi_Solitons_Fermion_Half.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1976
- **Authors**: R. Jackiw, C. Rebbi
- **Relevance**: CRITICAL
- **Tags**: fermion zero modes, fractional charge, index theorem, kink, topological protection
- **Pillar**: VI (founding)
- **Status**: Journal-only (PRD 13:3398)

---

### Paper 29: Kinks and Domain Walls [CRITICAL] — STUB
- **File**: `29_2006_Vachaspati_Kinks_Domain_Walls.md`
- **arXiv**: N/A (CUP monograph)
- **Year**: 2006
- **Authors**: T. Vachaspati
- **Relevance**: CRITICAL
- **Tags**: Kibble-Zurek, domain wall, instanton tunneling, defect formation
- **Pillar**: VI
- **Status**: Book

---

### Paper 30: Special Metrics and Group Actions in Geometry [CRITICAL] — STUB
- **File**: `30_2005_Baptista_Special_Geometry_Dim_Six.md`
- **arXiv**: N/A (doctoral thesis, Universidade de Lisboa)
- **Year**: 2005
- **Authors**: J. M. Baptista
- **Relevance**: CRITICAL
- **Tags**: Jensen deformation, SU(3), volume preservation, null geodesic, KK geometry
- **Pillar**: VIII
- **Status**: Thesis (not on arXiv). Key results in researchers/Baptista/ papers

---

### Paper 31: Homogeneous Einstein Metrics [HIGH] — STUB
- **File**: `31_1982_Ziller_Homogeneous_Einstein_Metrics.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1982
- **Authors**: W. Ziller
- **Relevance**: HIGH
- **Tags**: Einstein metrics, Lie groups, SU(3) moduli space, 28-dimensional
- **Pillar**: VIII
- **Status**: Journal-only (Math. Ann. 259:351)

---

### Paper 32: Twisted Standard Model and Krein Structure [MEDIUM]
- **File**: `32_2026_Martinetti_Twisted_SM_Krein.md`
- **arXiv**: 2603.03216
- **Year**: 2026
- **Authors**: P. Martinetti
- **Relevance**: MEDIUM
- **Tags**: twisted spectral triple, Krein space, twistor symmetry, NCG SM
- **Pillar**: III

**Summary**: Multiple minimal twists of the SM spectral triple exist. Twist-induced inner product converts Hilbert space to Krein space. Twisted unitary group contains twistor symmetry as subgroup.
