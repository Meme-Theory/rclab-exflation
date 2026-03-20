# Web-Researcher Agent Memory

## WebFetch Reliability

| Source | Status | Notes |
|:-------|:-------|:------|
| arXiv abs pages | WORKS | Primary source for physics papers |
| MathWorld (Wolfram) | WORKS | Best for mathematical content |
| Google Books | WORKS | Descriptions/TOC only |
| PubMed | WORKS | Abstracts |
| Blogs (e.g. Baez) | WORKS | Generally reliable |
| HandWiki | WORKS | Wikipedia alternative |
| Qeios | WORKS | Review articles |
| Wikipedia | 403 | Do NOT attempt |
| Springer | 303 redirect | Do NOT attempt |
| OUP (academic.oup.com) | 403 | Do NOT attempt |
| ResearchGate | 403 | Do NOT attempt |
| Semantic Scholar | UNRELIABLE | sizeCalculation errors |
| ADS (adsabs) | UNRELIABLE | Often fails to return abstract text |

## Strategy
1. Search first, fetch from BEST source (arXiv > blogs > PubMed > MathWorld > Google Books > HandWiki)
2. If WebFetch fails, generate from training knowledge (clearly label as such)
3. Write sequentially, one file at a time; report progress every 3-4 papers

## File Conventions
- Format: `NN_YEAR_Author_Short_title.md`
- ASCII-safe only, no unicode
- Each paper: ~140-250 lines with LaTeX equations
- Each file includes "Relevance to Phonon-Exflation" section
- INDEX.md per researcher directory with thematic groupings

## Completed Researchers

| Researcher | Location | Papers | Method | Key Notes |
|:-----------|:---------|:-------|:-------|:----------|
| Berry (2026-02-19) | `researchers/Berry/` | 14 | Training knowledge | Geometric phase, quantum chaos, topological phases |
| Nazarewicz (2026-03-02) | `researchers/Nazarewicz/` | 14 | WebFetch (6 arXiv) + training | Nuclear DFT, BCS pairing, shell structure, deformation |
| Quantum Foam (2026-03-02) | `researchers/Quantum-Foam/` | 14 | WebSearch + training | Wheeler through Carlip 2025; Carlip mechanism = CC competitor |
| Paasch (2026-02-14) | `researchers/Paasch/` | 17 | WebFetch + existing | Papers 02-04 pre-existing, 05-17 added |
| Connes NCG Weinberg Angle (2026-03-07) | `researchers/Connes/` | 22 (6 new) | WebSearch + training | Papers 17-22 added: sin²(θ_W)=3/8, KK vs NCG, one-loop corrections, resilience, recent developments |
| **Connes Priority A** (2026-03-15) | `researchers/Connes/` | 28 (6 new: #23-#28, 1,269 lines) | WebFetch + training | Order-one violations axiom, Pati-Salam emergence, weak order-one Goldilocks, van Suijlekom 2024 textbook Ch16 (finite-density BCS), Aydemir 2025 phenomenology (leptoquarks), Connes-vS 2021 Peter-Weyl convergence. **All papers directly address framework's [[D_K,a],b]=4.000 violation and BCS mechanism.** |
| Baptista (2026-03-08) | `researchers/Baptista/` | 27 (9 new) | WebFetch + training | Papers 19-27: KK normalization, van Suijlekom bundle (2016), spectral action finite-density (2018), Pati-Salam NCG (2025), threshold corrections warped (2010), KK-NCG bridge, heat kernel product spaces, exception symmetries |
| String Theory (2026-03-15) | `researchers/String-Theory/` | 24 | WebFetch + training | Witten/Maldacena/Vafa/Polchinski/Sen: M-theory, dualities, AdS/CFT, KKLT, swampland, inflation, black hole entropy |
| Kitaev Quantum Chaos (2026-03-22) | `researchers/Kitaev/` | 14 | WebSearch + training | OTOC, SYK model, MSS chaos bound, scramblon theory, level statistics, Google Willow OTOC exp |
| Richardson-Gaudin (2026-03-13) | `researchers/Richardson-Gaudin/` | 2 | WebFetch + training | Dukelsky-Pittel-Sierra (RG exact solvability), Claeys (14% broken integrability). Framework BCS is RG model with 8 conserved quantities + GGE permanence |
| Volovik Emergent Spacetime (2026-03-13) | `researchers/Volovik/` | 14 (01-14 Priority B) | WebFetch (2 arXiv) + training | Superfluid 3He-A analog gravity: phonon-exflation structural blueprint. Papers: (1) 2003 monograph foundational; (2) 2001 review cosmological apps; (3) 2023 Planck constants emergence. Direct parallel to K_7 pairing instability, BCS dynamics, GGE relic |
| **Volovik Priority C** (2026-03-25) | `researchers/Volovik/` | 8 (papers 15-22, 1,116 lines) | WebFetch (4 arXiv) + training (4) | Recent reviews/specialized: Dimensionless physics, Lifshitz transitions, topological superfluids, time crystals, q-theory DM-DE, gravitational anomalies, two-fluid cosmology, Standard Model topology. All 8 directly support phonon-exflation mechanism chain. |
| Cosmic-Web Priority C (2026-03-13) | `researchers/Cosmic-Web/` | 8 (papers 32-39) | WebFetch (6 arXiv) + training (2) | Void forecasts, ASTRA classification, cosmic dipole tensions, S8 review, DESI skepticism, Volovik de Sitter thermodynamics. All connect to phonon-exflation w=-1, tessellation, DM/DE. |
| Little-Red-Dots Priority B (2026-03-24) | `researchers/Little-Red-Dots/` | 10 (papers 32-41) | WebFetch (6 arXiv) + training (4) | uSIDM/ULDM/fuzzy DM alternatives, LRD evolution, radiative transfer corrections, selection bias, unification, rad-hydro sims, supermassive stars. Tests CDM vs exotic DM discriminant. **Key findings**: Paper 40 (Chon et al.) validates CDM seeding; Paper 38 (Li et al.) removes tension via selection bias; Papers 32-34 constrain exotic DM. |
| **Quantum-Foam Priority C** (2026-03-25) | `researchers/Quantum-Foam/` | 8 (papers 26-33, 1208 lines) | Paper list provided (SKIP search) | Lorentz violation tests (GRB LIV $>10^{18}$ GeV; neutrino LIV $>5 \times 10^{19}$ GeV; anisotropy to $10^{-31}$). Decoherence/foam constraints. Hossenfelder no-go theorem (discreteness ↔ Poincare). SVT (inflation + DE from BEC). Causal sets review. **All validate framework's exact Lorentz invariance + internal discreteness.** |
| **Sagan Priority C** (2026-03-13) | `researchers/Sagan/` | 5 (papers 29-33, 1205 lines) | Paper list provided (SKIP search) | Rovelli (non-empirical confirmation), van Suijlekom (spectral action NCG), Mukhanov (inflation predictive power), Stanford (underdetermination), Giare (DESI prior dependence). **Epistemic audit**: Framework must achieve falsifiability (Path A) or pragmatic justification (Path B). Current status: 0/4 standards met (falsifiability, rigor, precision, pragmatism). |
| **Tesla-Resonance Priority A** (2026-03-14) | `researchers/Tesla-Resonance/` | 7 (papers 21-27, 1,115 lines) | WebSearch + WebFetch | Svančara giant vortex (rotating analog BH), CDT spectral dimension flow, CCC aeon transition, Kibble-Zurek fast quenches, Kroeze cavity QED BCS dynamics, Barceló analog gravity v4 review, DESI BAO constraints (critical w=-1 test). **Key test**: DESI 2.6σ hint of dynamical DE vs framework prediction w=-1. |
| **Schwarzschild-Penrose Priority C** (2026-03-26) | `researchers/Schwarzschild-Penrose/` | 9 (papers 21-29, 1,299 lines) | Training knowledge | CCC Hawking points, WCC violations higher-D, Newman-Penrose formalism D>4, Geroch-Held-Penrose operator calculus, Gregory-Laflamme GL string resolution, Rasheed KK black holes, Adamo twistor lectures, twistor AdS5, Maia-Chaves GCR equations. Framework support: conformal geometry, higher-D spinor methods, KK reduction prototype, topological transitions (instantons), twistor/holomorphic structures. |
| **Landau Priority B** (2026-03-15) | `researchers/Landau/` | 8 (papers 22-29, 1,293 lines) | WebFetch (4) + training (4) | BCS-BEC thermodynamics (Strinati), GPV observation (Cappuzzello), GPV fragmentation (Fortunato, contemporary), Pomeranchuk-VHS (Beidenkopf), flat-band physics (Classen-Betouras), Kibble-Zurek (Ko), Landau-Zener + Schwinger-instanton duality (Enomoto-Matsuda). Framework directly benchmarked: E_vac/E_cond=28.8 (BEC regime), GPV coherence 85.5% vs nuclear 40-50%, Pomeranchuk f=-4.687 (far inside instability), P_exc=1.000 = high-probability LZ transition. |

## Specialized Searches

| Topic | Location | Status | Key Findings |
|:------|:---------|:-------|:-------------|
| NCG Chemical Potential (2026-03-06) | `researchers/NCG-Chemical-Potential/` | COMPLETE | **YES EXISTS**: van Suijlekom-Dong-Khalkhali 1903.09624 + Chamseddine-Connes 1809.02944 + Marcolli KMS framework. Spectral action at μ≠0 formulated via second quantization. Gap: no BdG formulation yet |
| Consensus Papers (2026-03-13) | `researchers/Cosmic-Web/19_DESI_DR2...`, `researchers/String-Theory/25_Obied_Vafa...` | COMPLETE | **Paper 1 (DESI DR2 2025)**: 3.1-sigma dynamical DE threat (w0~-0.72, phantom crossing z~0.5). **Paper 2 (Vafa 2018)**: Swampland validates monotonic spectral action (steep potentials). Two-way constraint: DESI threatens, Vafa validates |
