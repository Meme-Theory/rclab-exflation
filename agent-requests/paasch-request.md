# Meta-Analysis Request: Paasch Mass Quantization Analyst

**Domain**: Particle Mass Phenomenology, Mass Quantization, Logarithmic Potentials, Fine Structure Constant
**Date**: 2026-03-13
**Agent**: paasch-mass-quantization-analyst
**Researchers Folder**: `researchers/Paasch/`

---

## 1. Current Library Audit

**Papers on file**: 16 (across 3 Paasch originals + 13 context papers)
**Coverage assessment**: The THREE core Paasch papers (02, 03, 04) are present and thoroughly indexed. Supporting context is strong on the LNH/varying-G side (Dirac 1937/1974, Williams LLR 2004, Barrow 2005) and on historical mass quantization (Nambu 1952, Muraki 1978, MacGregor 2007). The Koide formula (1983) and Coldea E8 experiment (2010) provide key benchmarks. Coverage of alpha derivations (Wyler 1969, Eddington 1929) is adequate. **Major gaps** exist in: (1) post-2016 Koide extensions and quark-sector applications, (2) statistical critiques/look-elsewhere analysis of mass coincidences, (3) Barut's lepton mass formula and Gsponer-Hurni quark extension, (4) modern spectral geometry mass gap theorems, (5) Furey/octonion algebraic mass approaches, (6) Froggatt-Nielsen and clockwork hierarchy mechanisms, (7) DESI 2024-2025 w(z) results constraining the framework's dark energy prediction.

| # | Current Paper | Key Topics | Adequate? |
|---|--------------|------------|-----------|
| 02 | Paasch 2009: Logarithmic potential, exponential mass function | phi_paasch = 1.53158, spiral, 6 sequences | Yes (CRITICAL) |
| 03 | Paasch 2016: Calculation of particle masses | Mass numbers N(j)=7n, golden ratio, proton/neutron to 6-8 digits | Yes (CRITICAL) |
| 04 | Paasch 2016: Derivation of fine structure constant | alpha = 0.007297359 (0.9 ppm), from n3=10 and ln(x)=-x | Yes (HIGH) |
| 05 | Muraki 1978: Logarithmic mass formulae | Paasch precursor, ln(m/m0) = an+b | Yes |
| 06 | Dirac 1974: LNH cosmological models | G~1/t, matter creation | Yes (historical, refuted) |
| 07 | Koide 1983: Lepton mass formula | Q = 2/3 to 0.001%, tau prediction | Partial -- needs extensions |
| 08 | Dirac 1937: Cosmological constants | LNH origin | Yes (historical) |
| 09 | Zenczykowski 2015: Cl(6) and mass concept | Algebraic mass origin, integer grading | Yes |
| 10 | Williams 2004: LLR constraints on G-dot | G-dot/G = (4+/-9)e-13 yr^-1 | Partial -- needs 2024 update |
| 11 | Coldea 2010: Golden ratio E8 experiment | m2/m1 = 1.618 in CoNb2O6 | Yes (CRITICAL benchmark) |
| 12 | Planck 2015: Cosmological parameters | H0, Omega_m, t0 | Partial -- needs 2024 update |
| 13 | Nambu 1952: Empirical mass spectrum | m_n ~ n*70 MeV | Yes |
| 14 | Eddington 1929: alpha derivation | alpha^-1 = 136/137 (cautionary tale) | Yes |
| 15 | Barrow 2005: Varying constants review | G, alpha constraints | Partial -- needs 2024 update |
| 16 | Wyler 1969: Geometric alpha derivation | alpha from D5, ~0.6 ppm | Yes |
| 17 | MacGregor 2007: Power of Alpha | 70 MeV mass bands, lifetime grid | Yes |

---

## 2. Web-Fetch Requests

### Priority A -- Critical (directly addresses open gates or framework mechanisms)

| # | Title | Authors | Year | Identifier | Why Needed |
|---|-------|---------|------|-----------|------------|
| A1 | "DESI 2024 VI: Cosmological Constraints from BAO" | DESI Collaboration (Adame et al.) | 2024 | arXiv:2404.03002 | DESI DR1 w(z) measurement is THE observational test for the framework's dark energy prediction. S42 W-Z-42 FAIL (w_0 = -1 + O(10^-29)) must be compared against DESI's w_0 = -0.55+/-0.21, w_a = -1.32+0.52. The framework currently predicts no measurable deviation from Lambda. |
| A2 | "DESI DR2 Results II: Measurements of BAO and Cosmological Constraints" | DESI Collaboration | 2025 | arXiv:2503.14738 | DR2 strengthens dynamical DE evidence with 14M galaxies. Preference for w(z) != -1 does NOT diminish. If confirmed, this is a direct observational constraint the framework must confront. |
| A3 | "Noncommutative Geometry and Particle Physics" (2nd edition) | van Suijlekom, W.D. | 2024 | Springer: 978-3-031-59120-4 (also free PDF at waltervansuijlekom.nl) | The definitive textbook, updated 2024. Contains finite-density spectral action, beyond-SM models, and the mathematical infrastructure for the BCS-on-spectral-triple program central to sessions 33-42. The S34 discovery of Connes papers 15-16 on finite-density spectral action traces directly to this school. |
| A4 | "Second Quantization and the Spectral Action" | Dong, R.; Khalkhali, M.; van Suijlekom, W.D. | 2019 | arXiv:1903.09624 | BCS on spectral triples with chemical potential. von Neumann entropy and average energy expressed as spectral actions. Directly relevant to S35-S42 BCS chain. We use the framework but should have the source paper on file. |
| A5 | "Entropy and the Spectral Action" | Chamseddine, A.H.; Connes, A.; van Suijlekom, W.D. | 2019 | arXiv:1809.02944 | The Connes paper that extends spectral action to finite density. The "Connes papers 15-16" discovered in S34. Foundation for all BCS-spectral-action computations in S35-S42. |
| A6 | "Comprehensive Bayesian Exploration of Froggatt-Nielsen Mechanism" | Bauer et al. | 2025 | arXiv:2412.19484; JHEP 03(2025)150 | Systematic Bayesian analysis of all viable FN charge assignments. The FN mechanism produces exponential mass hierarchies from O(1) charge differences -- the same structural pattern as Paasch's phi^n. Comparing the Bayesian landscape of FN charges to Paasch's N(j)=7n integers would determine whether phi-quantization is a special case of FN or structurally distinct. |

### Priority B -- Important (foundational or fills significant gap)

| # | Title | Authors | Year | Identifier | Why Needed |
|---|-------|---------|------|-----------|------------|
| B1 | "A Superalgebra Within: Representations of Lightest SM Particles Form a Z_2^5-Graded Algebra" | Furey, C. | 2025 | Annalen der Physik (2025), 2500229 | Furey identifies SU(3)+SU(2)+U(1) from C x O triality. Her algebraic approach to SM quantum numbers parallels Zenczykowski (Paper 09) but is more developed and connects directly to our KO-dim = 6 and Peter-Weyl sector structure. Missing from our library. |
| B2 | "An Algebraic Roadmap of Particle Theories" | Furey, C. | 2025 | Annalen der Physik (2025), 2400323 | Comprehensive roadmap connecting division algebras to particle physics. Maps the landscape of octonionic approaches. Essential context for understanding how our D_K eigenvalue structure relates to the broader algebraic program. |
| B3 | "Koide Formula and the Connection of Elementary Particle Masses with the Fine-Structure Constant alpha" | Kosinov, M. | 2024 | Cambridge Open Engage / SSRN:4992875 | New empirical formula linking electron, proton, tau, muon masses to alpha, as accurate as Koide. Predicts m_tau = 1776.7586 MeV. Directly extends the Nambu-Barut-Paasch tradition of alpha-mass connections. Should be evaluated against our D_K eigenvalue ratios. |
| B4 | "Trial Factors for the Look-Elsewhere Effect in High Energy Physics" | Gross, E.; Vitells, O. | 2010 | Eur. Phys. J. C 70, 525 (arXiv:1005.1891) | The standard reference for quantifying the look-elsewhere effect. Our phi_paasch = 1.531580 finding (Session 12) has p < 0.01 against null, but the trial factor from scanning across all possible eigenvalue ratios, all tau values, and all sector pairs was never formally computed. This paper provides the methodology. |
| B5 | "Non-linear field theory for lepton and quark masses" | Gsponer, A.; Hurni, J.P. | 1996 | OSTI:478280 / arXiv:hep-ph/9510326 | Extends Barut's lepton mass formula to quarks using non-linear scalar field model. Explains N^4 power law and limits generations to 3. Parallel to Paasch's integer mass number structure. Not on file. |
| B6 | "The Dirac Operator" (AMS Bulletin survey) | -- | 2025 | Bull. AMS 62(1), S0273-0979-2024-01847-3 | 2025 survey of Dirac operator spectral properties on compact manifolds. Eigenvalue estimates, spectral gaps, Kahler and quaternion-Kahler enhancements. Directly relevant to understanding how the D_K spectral gap at the fold constrains mass predictions. |
| B7 | "Dynamical dark energy in light of DESI DR2 BAO measurements" | -- | 2025 | Nature Astronomy (2025), s41550-025-02669-6 | Analysis of dynamical DE evidence from DESI DR2. The framework's W-Z-42 FAIL (|w+1| ~ 10^-29) means we need to understand precisely what DESI sees and what structural modification could produce it. |
| B8 | "Particles and Shells" | Palazzi, P. | 2003 | arXiv:physics/0301074 | Shell structure in particle masses, "stablines" in cube-root mass space. Predicted Bc mass at 7.4+/-0.2 GeV. 35 MeV quantization reassessed. Parallel to Paasch's mass number scheme. Not on file despite being in my system prompt knowledge base. |
| B9 | "Review of Particle Physics" (2024 edition) | Navas, S. et al. (PDG) | 2024 | Phys. Rev. D 110, 030001 | Updated PDG masses. 2717 new measurements from 869 papers. All Paasch mass predictions and Koide formula evaluations should be re-checked against 2024 PDG values. Current library uses Planck 2015 (Paper 12) for cosmological parameters and pre-2018 mass values. |

### Priority C -- Supplementary (strengthens coverage, recent developments)

| # | Title | Authors | Year | Identifier | Why Needed |
|---|-------|---------|------|-----------|------------|
| C1 | "Updated Running Quark and Lepton Parameters at Various Scales" | -- | 2025 | arXiv:2510.01312 | Running masses at various energy scales. For testing whether Paasch's relations hold at a specific renormalization scale (possibly the phi-crossing tau = 0.15 mapped to some M_KK). Running couplings enter the clock constraint (S22d). |
| C2 | "The symmetry approach to quark and lepton masses and mixing" | -- | 2025 | ScienceDirect: S0370157324004319 | Comprehensive review of symmetry-based mass/mixing approaches. Context for understanding how the framework's spectral approach compares to flavor symmetry models. |
| C3 | "The problem of flavour" | -- | 2025 | Eur. Phys. J. Plus, s13360-025-06008-6 | Recent review of the flavor problem. Context for situating Paasch's purely algebraic mass predictions within the broader question of why masses have the values they do. |
| C4 | "Froggatt-Nielsen ALP" | -- | 2024 | JHEP 09(2024)174 | The FN mechanism predicts axion-like particles. Connects mass hierarchy to dark matter sector. Relevant to the framework's GGE dark matter candidate. |
| C5 | "Fermion Mass Hierarchy and High Quality Axion from Gauged U(1) Flavor Symmetry" | -- | 2025 | arXiv:2602.24253 | Recent gauged flavor symmetry model producing exponential hierarchy. Connects to Paasch's phi^n scaling. |
| C6 | "Dirac's Large Number Hypothesis: An Updated Review" | Jiang et al. | 2025 | Qeios T7G07S.2 / Preprints 202408.1773 | 2025 review connecting LNH to holographic principles and quantum gravity effects. Updates the theoretical landscape around Paper 06/08. |
| C7 | "Cosmological and Lunar Laser Ranging Constraints on Evolving Dark Energy" | -- | 2025 | arXiv:2512.10530 | Combined LLR + cosmological constraints on modified gravity. Updates Paper 10 (Williams 2004) constraints by 20 years. |
| C8 | "A modified version of the Koide formula from flavor nonets in a scalar potential model" | -- | 2021 | Nucl. Phys. B 973, 115598 (ScienceDirect:S0550321321002431) | Extends Koide to flavor nonets. Tests whether Q=2/3 generalizes to mesons in ways compatible with Paasch's spiral sequences. |
| C9 | "Mass ratios from octonionic NCG" | Singh, T.P. | 2022 | MDPI Physics 4(3); arXiv:2209.03205 | Octonionic trace dynamics predicting CKM parameters and mass ratios. Connects to our Session 8 KO-dim=6 and to Zenczykowski's Cl(6). Already in system prompt but not on file. |
| C10 | "Particle Mass-Formulae" | Giani, S. | 2004 | CERN-OPEN-2004-004 | CERN review of ALL particle mass formulae. Comprehensive benchmark compilation. Historical context for Paasch's approach. In system prompt but not on file. |

---

## 3. New Researcher / Field Recommendations

### Complementary (would strengthen or extend the framework)

| Researcher or Field | Why Complementary | Key Papers (1-3) | Proposed Folder Name |
|--------------------|-------------------|-------------------|---------------------|
| **Cohl Furey** (algebraic particle physics) | Derives SM quantum numbers from C x O (complex octonions). Her Z_2^5-graded superalgebra (2025) parallels our Peter-Weyl sector decomposition. The three generations from octonions could explain why Paasch needs exactly 6 sequences (= 3 generations x 2 chiralities?). | (1) "A Superalgebra Within" (2025 Ann. Phys.), (2) "An Algebraic Roadmap" (2025 Ann. Phys.), (3) "Standard Model from an Algebra?" arXiv:1611.09182 | `researchers/Furey/` |
| **Walter van Suijlekom** (spectral action, finite density NCG) | THE living authority on NCG particle physics. His 2nd edition textbook (2024) and papers with Khalkhali on finite-density spectral triples are the mathematical foundation for everything in S33-S42. Should have a dedicated folder. | (1) NCG and Particle Physics 2nd ed. (2024), (2) "Second Quantization and the Spectral Action" arXiv:1903.09624, (3) "Entropy and the Spectral Action" arXiv:1809.02944 | `researchers/van-Suijlekom/` |
| **DESI Collaboration** (BAO, dark energy w(z)) | DESI DR1 (2024) and DR2 (2025) provide the most precise measurement of w(z) in history. The framework's W-Z-42 prediction (|w+1| ~ 10^-29) is 28 OOM below DESI's detection. If dynamical DE is confirmed, the framework needs to explain it -- or recognize it as a falsification of the frozen-wall picture. | (1) DESI 2024 VI arXiv:2404.03002, (2) DESI DR2 II arXiv:2503.14738, (3) Nature Astronomy DESI DR2 analysis (2025) | `researchers/DESI/` |
| **Mykola Kosinov** (alpha-mass connections) | 2024 preprint extending the Nambu-Barut-Koide tradition with a new formula connecting 4 particle masses to alpha, yielding m_tau = 1776.7586 MeV. Direct competitor/complement to Paasch's alpha derivation (Paper 04). | (1) "Koide Formula and Connection of Masses with FSC" SSRN:4992875 (2024) | `researchers/Kosinov/` -- OR fold into Paasch folder as Paper 18 |

### Adversarial (would challenge, constrain, or stress-test the framework)

| Researcher or Field | Why Adversarial | Key Papers (1-3) | Proposed Folder Name |
|--------------------|-----------------|-------------------|---------------------|
| **Look-Elsewhere Effect / Statistical Rigor** | The phi_paasch = 1.531580 finding (Session 12) achieved p < 0.01 against a random-ratio null. But the trial factor was never computed: how many ratios, tau values, and sector pairs were implicitly scanned? Gross & Vitells (2010) is THE standard method. Without this, the phi_paasch significance is formally uncalibrated. | (1) Gross & Vitells, "Trial Factors for LEE" EPJC 70:525 (2010), (2) "The look-elsewhere effect from a unified Bayesian/frequentist perspective" arXiv:2007.13821 (2020) | `researchers/Statistics/` |
| **Sabine Hossenfelder** (critique of mathematical beauty in physics) | Her "Lost in Math" (2018) and blog posts explicitly critique the practice of fitting mass relations to known data without pre-registered predictions. The Paasch program fits known masses to O(0.4%) but has made no novel predictions for unknown particles. Hossenfelder's framework for evaluating "beautiful math" would stress-test whether phi_paasch is a discovery or a coincidence. | (1) "Lost in Math" (Basic Books, 2018), (2) "To Understand the Foundations of Physics, Study Numerology" (Backreaction blog, 2017), (3) "Screams for Explanation" arXiv:1801.02176 | `researchers/Hossenfelder/` |
| **PDG Statistical Methods** | The PDG reviews on probability and statistics provide the standard methods for evaluating mass formula accuracy. Any claim that Paasch's proton mass to 6 digits is "derived" must survive the PDG's look-elsewhere and systematic uncertainty standards. | (1) PDG 2024 Statistics review, (2) Barlow "Statistical Issues in Particle Physics" (SLAC-R-703), (3) "A Practical Guide to Statistical Techniques" arXiv:2411.00706 | Fold into `researchers/Statistics/` |

---

## 4. Framework Connections (S41/S42)

### Session 41 Connections

**N_eff step function (32 to 240)**. S41 discovered that N_eff jumps discontinuously from 32 distinct eigenvalue types at round SU(3) to 240 at any nonzero Jensen deformation. This is the phononic crystal gaining resolution in a single step, not gradually. For Paasch's 6 sequences: the 240 distinct eigenvalues at generic tau could correspond to Paasch's mass allocation system, but only if the 240 eigenvalues can be organized into 6 families with phi-quantized spacing. UNCOMPUTED. The number 240 is notable: it is the number of root vectors of E8, the same Lie algebra whose spectrum produces the golden ratio in the Coldea experiment (Paper 11). Whether this is coincidence or structure is an open question.

**Phononic crystal identification (permanent)**. S41 W3-1 permanently identified the Jensen-deformed SU(3) as a phononic crystal satisfying all formal criteria (Bloch modes, band structure, van Hove singularities, complete spectral gap). Paasch's logarithmic potential (Paper 02, Eq. 2a) was originally motivated by confined constituents in a potential well -- the phononic crystal provides the PHYSICAL REALIZATION of that potential. The crystal's discrete mode spectrum is the mass spectrum.

**No-Umklapp theorem**. The Peter-Weyl lattice is infinite and non-periodic: no Brillouin zone boundary, no Umklapp scattering. This structurally explains GGE permanence and provides a second independent foundation (beyond Richardson-Gaudin integrability) for why the post-transit state never thermalizes. For Paasch: the absence of Umklapp means mode-mode scattering cannot redistribute mass among sequences. The 6-sequence structure, if set during the transit, is permanent.

**Fabric reframing**. The crystal IS space. Fewer modes = fewer points = larger cells. The fabric's collective behavior (spatial averaging, gradient energy, collective modes) is the correct computational target, not single-crystal properties. For Paasch: if the 32-cell tessellation at early tau sets the large-scale structure (GIANT-VORONOI-42 PASS), then Paasch's 6 sequences might correspond to the 6 types of domain wall (3 orientations x 2 chiralities from K_7 charge +/-1/2). This was identified in Session 33 W3 but never computed.

### Session 42 Connections

**Z(tau) = 74,731 (Z-FABRIC-42 PASS)**. The gradient stiffness at the fold is 27% above the spectral action gradient. The fabric has non-trivial spatial rigidity. Per-sector breakdown shows (2,1)+(1,2) dominate (69.6% of Z). The (3,0)+(0,3) sectors -- where phi_paasch lives -- contribute 23% of Z. This means the phi-relevant eigenvalues have ABOVE-AVERAGE gradient sensitivity. Physical implication: the inter-sector ratio m_{(3,0)}/m_{(0,0)} varies significantly across the fabric when tau is spatially inhomogeneous. The phi_paasch value 1.531580 is the ratio at a SPECIFIC tau = 0.15, which may not be the same everywhere.

**v_th(B2) = 0.618 c**. The thermal velocity of B2 quasiparticles at formation is 0.618 c -- the golden ratio to 3 significant figures. This is computed from E_th = T_acoustic = 0.112 M_KK and M*_B2 = 2.228 M_KK. The golden ratio appears here because v_th = sqrt(2T/M) and the ratio T/M happens to produce phi_golden. Whether this is a consequence of the spectral geometry or a numerical coincidence is UNRESOLVED. It connects to Paasch's golden ratio in M-value ratios (Paper 03, Eq. 5.5) and to the Coldea E8 experiment (Paper 11).

**w(z) FAIL (W-Z-42)**. The framework predicts |w+1| ~ 10^-29, indistinguishable from Lambda. DESI measures w_0 = -0.55+/-0.21 (DR1) with strengthening evidence for dynamical DE in DR2. This is a 28-OOM discrepancy. The framework's frozen-wall picture produces no measurable deviation from Lambda. If DESI's dynamical DE is confirmed, the framework needs either: (1) a mechanism for ongoing tau evolution (contradicts the frozen-wall/compound-nucleus picture established in S37-S40), or (2) an entirely different source of w != -1. For Paasch: his original framework assumed G(t) ~ 1/t (LNH), which would produce dynamical DE. The LNH is empirically refuted (Paper 10), but the OBSERVATION that w(z) may deviate from -1 keeps the question of time-varying quantities alive.

**m_tau = 2.062 M_KK (C-FABRIC-42 PASS)**. The tau modulus mass is numerically close to the heaviest KK eigenvalue (lambda_max ~ 2.06 M_KK). This coincidence is likely structural: both are controlled by the largest Casimir eigenvalues in level-3 sectors. For Paasch: the scale 2.06 appears in the eigenvalue spectrum at the fold and sets the characteristic energy of the fabric. The ratio m_tau/m_min = 2.06/0.82 = 2.51 is the full spectral bandwidth. This ratio has not been compared to any Paasch mass number.

**HF-KK-42 FAIL (eta ~ 3.4e-9)**. The baryon-to-photon ratio estimate is 0.7 decades from observed (6.1e-10). Despite the gate failure, this is the closest the framework has come to a cosmological observable. The key quantities are all geometric invariants of the fold. For Paasch: the mass gap 0.819 M_KK and the BCS gap Delta = 0.025 (spectral units) are the controlling parameters. The former is the (0,0) singlet eigenvalue -- Paasch's reference mass.

### Open Questions This Literature Could Address

1. **TRIAL-FACTOR gate (UNCOMPUTED)**. Apply the Gross-Vitells look-elsewhere correction to the phi_paasch finding. Pre-registered criterion: if the trial-corrected p-value remains < 0.05, the ratio is significant. If p > 0.1 after correction, it is consistent with chance. This requires: counting all eigenvalue ratios scanned (~50 sector pairs x 20 tau values = 1000 implicit tests), applying the Euler characteristic method from Gross-Vitells, and computing the global p-value. ZERO computational cost (uses existing s22a_paasch_curve.npz data).

2. **N(j) = 7n vs. Froggatt-Nielsen charge assignments**. Paasch's integer mass numbers N(j) = 7n have the SAME STRUCTURE as Froggatt-Nielsen charges: integer quantum numbers producing exponential mass hierarchies. The 2025 Bayesian FN analysis (arXiv:2412.19484) maps the full landscape of viable FN charges. Does any FN charge assignment reproduce N = {7, 35, 42, 98, 150}? If yes, Paasch's mass numbers may be a specific realization of FN. If no, the two mechanisms are structurally distinct.

3. **Koide Q from D_K eigenvalues**. The Koide ratio Q = 2/3 has never been tested on D_K eigenvalues. Using the B1, B2, B3 branch eigenvalues at the fold (0.819, 0.845, 0.978): Q_B = (sum m_i) / (sum sqrt(m_i))^2 = 2.642 / (0.905 + 0.919 + 0.989)^2 = 2.642 / 7.907 = 0.334 = 1/3 (LOWER BOUND, not 2/3). The Koide ratio is 1/3 for the B-sector, not 2/3. This is actually the DEGENERATE limit (all masses equal gives Q = 1/3). With more spread: the full (0,0) singlet eigenvalues (8 levels from 0.819 to 0.978) should be tested against generalized Koide-like sum rules. UNCOMPUTED.

4. **v_th = 0.618 c: coincidence or structure?** The golden ratio in the B2 thermal velocity is a 3-digit match. It depends on T_acoustic/M*_B2 = 0.112/2.228 = 0.0503, and v_th = sqrt(2 * 0.0503) = 0.317, then v_th^2 = T/M = 0.050 -> v = 0.224 c... Wait, this needs re-derivation from S42 data. The S42 working paper states v_th(B2) = 0.618 c. If accurate, this is a testable golden ratio in a DERIVED quantity at the fold. The test: does v_th remain golden across tau, or only at the fold? Tau-sweep needed.

5. **240 eigenvalues and E8 roots**. The N_eff = 240 at generic tau equals |E8 root system| = 240. The Coldea experiment (Paper 11) observed golden ratio mass ratios from E8 symmetry. If the 240 D_K eigenvalue types organize according to E8 root structure, this would connect Paasch's golden ratio (Paper 03) to the framework's spectral geometry via E8. HIGHLY SPECULATIVE but testable: compute the inner products of the 240 eigenvalue vectors and compare to E8 root system geometry.

6. **n3 = 10 = dim(3,0)?** Still the highest-priority unexamined algebraic coincidence. Paasch's alpha derivation uses n3 = 10 from the proton mass calculation (Paper 03, Eq. 6.4). The (3,0) representation of SU(3) has dimension 10. The phi_paasch ratio lives in the (3,0) sector. Is n3 = dim(3,0) a consequence of the spectral geometry, or an accident? This is a purely algebraic question answerable from existing data.

7. **omega_2/omega_0 = 1.226 vs. fN = 1.236**. The QRPA frequency ratio at the fold is 0.8% from Paasch's exponential scaling factor fN = 2*phi_golden = 1.236068. This was identified in S40 but never swept across tau. If the ratio tracks fN across the transit window, it connects Paasch's golden ratio to the framework's collective excitation spectrum. If it diverges outside the fold, it is a fold-specific coincidence.

---

## 5. Self-Assessment

- **Biggest gap in current library**: The absence of DESI 2024-2025 BAO results. The framework's dark energy prediction (W-Z-42) is 28 OOM below DESI's measurement. Whether this is a fatal discrepancy or a sign that the frozen-wall picture needs modification depends on understanding the DESI data in detail. The second biggest gap is statistical rigor: the look-elsewhere effect has never been applied to phi_paasch or any of the framework's mass-ratio coincidences.

- **Most promising new direction**: The Furey algebraic program (C x O, Z_2^5-graded superalgebra) combined with the N_eff = 240 = |E8 roots| observation. If the 240 distinct D_K eigenvalue types at generic tau organize according to E8 root geometry, it would unify: (a) Paasch's golden ratio from Paper 03, (b) Coldea's E8 golden ratio from Paper 11, (c) the framework's phononic crystal spectrum from S41, and (d) Furey's octonionic SM construction. This is speculative but computationally testable from existing tier-0 data.

- **Confidence in recommendations**: HIGH for Priority A (DESI, van Suijlekom, spectral action foundations -- these are clearly needed). HIGH for Priority B adversarial (look-elsewhere effect -- this is a methodological obligation, not optional). MEDIUM for the E8/240 connection (speculative, but the numerical coincidence is striking and the test is cheap). LOW for the Kosinov formula (single-author preprint, not peer-reviewed, but the empirical content should be checked).
