# Capstone Citation Anchors — companion registry (the corpus)

Companion registry for `S96-CONSOL-CITATION-ANCHOR` (S96 W8-6). Carries the FULL bibliographic detail (arXiv/DOI) for every primary-literature anchor inserted inline in the capstone `sessions/framework/phonic-exflation-equation.md`. The capstone carries the minimal inline anchors `[CITE-N]` + the INHERITED/NOVEL tag; this registry carries the arXiv IDs, DOIs, and the per-anchor INHERITED-vs-NOVEL rationale.

**Source of the citation sets**: `deep-research-report.md §"Suggested citations for the capstone"` (a closed external recommendation table). Citation content is from the cited sources only (`feedback_research-corpus.md`); no training-knowledge invention. An uncertain inherited-vs-novel status is recorded as a dual annotation (INFO), not forced to a single tag.

**Gate**: `S96-CONSOL-CITATION-ANCHOR` | **Session**: S96 | **Class**: NON-PHONONIC (METHODOLOGY-class)
**Mandatory citation sets covered**: 8/8
**audit_sha256**: `c8b7f7cc99a81afd981eace1699450dc2bc14ef9a6c3be894a8a61943dfa555f`
**content_sha256**: `63aaef3bce35db1f60de0f7977e479bef0736a576ac80416a2a61b12308a978e`

**Plan-text-drift note** (`substrate-first-canonical-sourcing.md §(ii.B)`): the plan pins
`canonical_constants.py` and the capstone at plan-freeze SHAs; both drifted at runtime
(W1/W2/W3 canonical edits; W7 + W8-2 capstone edits) — EXPECTED per the gate CONTEXT.
Resolved to runtime ground-truth; plan-pinned values preserved in the JSON sidecar.

---

## Citation-anchor table (per capstone location)

| Anchor | Capstone location | Mandatory set | Claim type | Citation set | INHERITED / NOVEL-BEYOND |
|:--|:--|:--|:--|:--|:--|
| **CITE-1** | §0 opening; §1 master equation | `spectral-action` | Spectral action & geometry-from-spectrum (the master functional Tr f(D^2/Lambda^2) + Connes reconstruction) | Chamseddine & Connes 1996; Chamseddine-Connes-Marcolli 2007; Connes 2006 / almost-commutative review | **INHERITED** |
| **CITE-2** | §1.1 gauge/Higgs emergence | `spectral-action` | Inner fluctuations -> SM gauge structure + Higgs; the SU(3)-manifold specialization D_K IS the finite Dirac operator D_F | Chamseddine-Connes-Marcolli 2007 §2.5; Lizzi NCG review (Devastato-Lizzi 2014 lineage) | **NOVEL-BEYOND** |
| **CITE-3** | §2.x / §8.2 a_n convention table; §8.2a R_K firewall | `a_n-heat-kernel` | Heat-kernel coefficients / local invariants / zeta-regularized spectral quantities; the 'two a_n objects, never conflated' firewall | Vassilevich 2003 (Heat kernel expansion: user's manual) | **INHERITED** |
| **CITE-4** | §0 arrow; §6.2 white hole; §6.3 'Jacobson reading made microscopic' | `emergent-gravity` | Emergent / thermodynamic / analog gravity and their limits (gravity is the a_2 moment; Einstein eqns as equations of state) | Jacobson 1995; Barcelo-Liberati-Visser 2005; Belenchia-Liberati-Mohd 2014; Volovik 2005/2007 | **INHERITED-genre/NOVEL-same-object** |
| **CITE-5** | §5.3 GGE-relic formation (transit / defect production) | `KZM-transit` | Kibble-Zurek / non-equilibrium defect formation; the diabatic sudden-quench P_exc -> 1 | del Campo & Zurek 2014 (Universality of phase transition dynamics) | **NOVEL-BEYOND** |
| **CITE-6** | §7.1 CC closure row; §7 CC caveat box; 'Substrate readings' (q-theory / vacuum relaxation) | `q-theory-CC` | Vacuum relaxation & q-theory cosmological-constant relaxation | Klinkhamer & Volovik 2008; Visser 2002; Volovik 2005 | **NOVEL-BEYOND** |
| **CITE-7** | §7.1 m_H row; §7 'Open gaps' (m_H route-dependence); §8.3 Higgs dictionary | `NCG-Higgs` | NCG Higgs phenomenology & compatibility with m_H ~ 125 GeV | Chamseddine-Connes-Marcolli 2007; Devastato-Lizzi-Martinetti 2014; ATLAS/CMS Higgs-mass (PDG 125.25 +/- 0.17 GeV) | **NOVEL-BEYOND** |
| **CITE-8** | §7.1 observational table + dark-energy anchor provenance note (‡); §7.2 falsifier anchors | `cosmological-data` | Numerical comparison anchors (the observational data the phenomenology contacts) | Planck 2018; BICEP/Keck 2024; Popovic et al. 2025 (DES-Dovekie, arXiv:2511.07517v3); DES Y3 2021 | **INHERITED** |
| **CITE-9** | §5.3 / §6.2 / §6.3 status-reconciliation clauses; §7.1 / §7.3 status notes; §0 'no seesaw' (any corrected/downgraded claim) | `retraction-aware` | Retraction-aware narrative (visible scholarly self-correction) | the repo's own retraction log (Atlas D09) + assumptions status (Atlas D04) | **INHERITED** |

---

## Per-anchor INHERITED-vs-NOVEL rationale

The NOVEL-BEYOND rows are the *citations-for-restraint* the report emphasizes: the cited work is the lineage, but the capstone claim steps beyond it into genuinely novel, still-contested territory. The single INFO row (CITE-4, analog-gravity) carries the dual annotation the report flags as the exact calibration question.

### CITE-1 — spectral-action (INHERITED)

- **Capstone location**: §0 opening; §1 master equation
- **Claim type**: Spectral action & geometry-from-spectrum (the master functional Tr f(D^2/Lambda^2) + Connes reconstruction)
- **Citation set**: Chamseddine & Connes 1996; Chamseddine-Connes-Marcolli 2007; Connes 2006 / almost-commutative review
- **Tag**: INHERITED
- **Rationale**: The master functional is canonical NCG; the framework inherits the spectral-action principle wholesale. NOVEL-BEYOND content (the SU(3)-manifold same-object D_K = D_F move) is tagged separately at CITE-2.

### CITE-2 — spectral-action (NOVEL-BEYOND)

- **Capstone location**: §1.1 gauge/Higgs emergence
- **Claim type**: Inner fluctuations -> SM gauge structure + Higgs; the SU(3)-manifold specialization D_K IS the finite Dirac operator D_F
- **Citation set**: Chamseddine-Connes-Marcolli 2007 §2.5; Lizzi NCG review (Devastato-Lizzi 2014 lineage)
- **Tag**: NOVEL-BEYOND
- **Rationale**: INHERITED: SU(A_K) = U(1)xSU(2)xSU(3) gauge group + inner-fluctuation Higgs is standard CCM. NOVEL-BEYOND: the internal factor is the MANIFOLD SU(3) (not a finite F), so D_K itself IS D_F (Baptista P18 eq 7.5) and the Higgs is an inner fluctuation of D_K — the framework departs from the product-geometry D = d_M (x) 1 + gamma_5 (x) D_F reflex.

### CITE-3 — a_n-heat-kernel (INHERITED)

- **Capstone location**: §2.x / §8.2 a_n convention table; §8.2a R_K firewall
- **Claim type**: Heat-kernel coefficients / local invariants / zeta-regularized spectral quantities; the 'two a_n objects, never conflated' firewall
- **Citation set**: Vassilevich 2003 (Heat kernel expansion: user's manual)
- **Tag**: INHERITED
- **Rationale**: The Seeley-DeWitt / Gilkey-zeta a_n machinery and the raw-mode-count-vs-curvature-integral distinction are the canonical heat-kernel/zeta literature; the §8.2 firewall IS the standard discipline applied. No novelty claimed in the a_n machinery itself.

### CITE-4 — emergent-gravity (INHERITED-genre/NOVEL-same-object)

- **Capstone location**: §0 arrow; §6.2 white hole; §6.3 'Jacobson reading made microscopic'
- **Claim type**: Emergent / thermodynamic / analog gravity and their limits (gravity is the a_2 moment; Einstein eqns as equations of state)
- **Citation set**: Jacobson 1995; Barcelo-Liberati-Visser 2005; Belenchia-Liberati-Mohd 2014; Volovik 2005/2007
- **Tag**: INHERITED-genre/NOVEL-same-object
- **Rationale**: INFO — the report flags this as the exact calibration question. INHERITED genre: emergent/thermodynamic/analog gravity (Jacobson eq-of-state; BLV analog-gravity limits; Volovik superfluid vacuum). NOVEL-BEYOND (contested): the substrate white hole is claimed as the SAME OBJECT as the SU(3)-substrate transit (substrate IS, not same-genre-analogy) — the dual annotation is the honest INFO tag, not a forced single label.

### CITE-5 — KZM-transit (NOVEL-BEYOND)

- **Capstone location**: §5.3 GGE-relic formation (transit / defect production)
- **Claim type**: Kibble-Zurek / non-equilibrium defect formation; the diabatic sudden-quench P_exc -> 1
- **Citation set**: del Campo & Zurek 2014 (Universality of phase transition dynamics)
- **Tag**: NOVEL-BEYOND
- **Rationale**: INHERITED: the quench/defect-production framing (KZM impulse-matching, Bogoliubov sudden-quench) is standard. NOVEL-BEYOND (contested per report): the jump from KZM-style defect production to a concrete GGE relic that explains CMB structure, dark matter, and horizon resolution is the framework's speculative extension — a productive analogy + mathematics, not a demonstrated cosmological mechanism.

### CITE-6 — q-theory-CC (NOVEL-BEYOND)

- **Capstone location**: §7.1 CC closure row; §7 CC caveat box; 'Substrate readings' (q-theory / vacuum relaxation)
- **Claim type**: Vacuum relaxation & q-theory cosmological-constant relaxation
- **Citation set**: Klinkhamer & Volovik 2008; Visser 2002; Volovik 2005
- **Tag**: NOVEL-BEYOND
- **Rationale**: INHERITED: the q-theory vacuum-relaxation picture (Gibbs-Duhem equilibrium identity rho_Lambda=0; tracking vacuum) is the right anchor. NOVEL-BEYOND: the Volovik-PARTITION + effacement-residual (Gamma_eff = 0.99970) mechanism closing 114 OOM to rho_vac/rho_obs = 1.032 (DILUTION-CC-66, w0_FW = -0.918) is the framework's specific extension — and it is DOUBLY CONDITIONAL on C10 + external H(t).

### CITE-7 — NCG-Higgs (NOVEL-BEYOND)

- **Capstone location**: §7.1 m_H row; §7 'Open gaps' (m_H route-dependence); §8.3 Higgs dictionary
- **Claim type**: NCG Higgs phenomenology & compatibility with m_H ~ 125 GeV
- **Citation set**: Chamseddine-Connes-Marcolli 2007; Devastato-Lizzi-Martinetti 2014; ATLAS/CMS Higgs-mass (PDG 125.25 +/- 0.17 GeV)
- **Tag**: NOVEL-BEYOND
- **Rationale**: INHERITED: the NCG-Higgs tradition (filter-independent tree-level lambda_h = (4/3)g_3^2(M_KK); A10 PROVEN). NOVEL-BEYOND: the KK-threshold band route (127.5-131.8 GeV at the ~2% theory budget) is the framework's specific prediction; the zeta route (138.5 GeV) is EXCLUDED and mu_BC (188 GeV) is an ACCOMMODATION, not a prediction.

### CITE-8 — cosmological-data (INHERITED)

- **Capstone location**: §7.1 observational table + dark-energy anchor provenance note (‡); §7.2 falsifier anchors
- **Claim type**: Numerical comparison anchors (the observational data the phenomenology contacts)
- **Citation set**: Planck 2018; BICEP/Keck 2024; Popovic et al. 2025 (DES-Dovekie, arXiv:2511.07517v3); DES Y3 2021
- **Tag**: INHERITED
- **Rationale**: These are external data anchors (no framework novelty claimed) — they prevent the phenomenology section from feeling internally self-referential. The (w0, wa) pair is the Popovic/DES-Dovekie joint posterior; sigma8 = 0.811 is the Planck anchor (W8-2 fix); Omega_GW Companion-null = 8.299e-58 is the Sage-exact regulator-class value.

### CITE-9 — retraction-aware (INHERITED)

- **Capstone location**: §5.3 / §6.2 / §6.3 status-reconciliation clauses; §7.1 / §7.3 status notes; §0 'no seesaw' (any corrected/downgraded claim)
- **Claim type**: Retraction-aware narrative (visible scholarly self-correction)
- **Citation set**: the repo's own retraction log (Atlas D09) + assumptions status (Atlas D04)
- **Tag**: INHERITED
- **Rationale**: INHERITED self-citation — turns the self-correction culture into a visible methodological strength. Each capstone clause narrating a BROKEN/CONDITIONAL/RETRACTED claim (T3 BROKEN, retraction items 16/22/25/27/34, C1/C2/C4/C5/C12) cites the register tag alongside the main text, so the prose confidence equals the register status (capstone-hygiene-gate.md).

---

## Full bibliography (arXiv / DOI)

- **Chamseddine & Connes 1996** — A. H. Chamseddine, A. Connes, 'The Spectral Action Principle', Commun. Math. Phys. 186 (1997) 731-750. arXiv:hep-th/9606001. DOI:10.1007/s002200050126.
- **Chamseddine-Connes-Marcolli 2007** — A. H. Chamseddine, A. Connes, M. Marcolli, 'Gravity and the standard model with neutrino mixing', Adv. Theor. Math. Phys. 11 (2007) 991-1089. arXiv:hep-th/0610241. DOI:10.4310/ATMP.2007.v11.n6.a3.
- **Connes 2006 / almost-commutative review** — A. Connes, 'Noncommutative geometry and the standard model with neutrino mixing', JHEP 0611 (2006) 081. arXiv:hep-th/0608226. DOI:10.1088/1126-6708/2006/11/081.
- **Vassilevich 2003** — D. V. Vassilevich, 'Heat kernel expansion: user's manual', Phys. Rept. 388 (2003) 279-360. arXiv:hep-th/0306138. DOI:10.1016/j.physrep.2003.09.002.
- **Jacobson 1995** — T. Jacobson, 'Thermodynamics of Spacetime: The Einstein Equation of State', Phys. Rev. Lett. 75 (1995) 1260-1263. arXiv:gr-qc/9504004. DOI:10.1103/PhysRevLett.75.1260.
- **Barcelo-Liberati-Visser 2005** — C. Barcelo, S. Liberati, M. Visser, 'Analogue Gravity', Living Rev. Rel. 8 (2005) 12; updated 14 (2011) 3. arXiv:gr-qc/0505065. DOI:10.12942/lrr-2005-12.
- **Belenchia-Liberati-Mohd 2014** — A. Belenchia, S. Liberati, A. Mohd, 'Emergent gravitational dynamics in a relativistic Bose-Einstein condensate', Phys. Rev. D 90 (2014) 104015. arXiv:1407.7896. DOI:10.1103/PhysRevD.90.104015.
- **Volovik 2005/2007** — G. E. Volovik, 'The Universe in a Helium Droplet', Oxford Univ. Press (2003/2009); 'Vacuum energy: quantum hydrodynamics vs quantum gravity', JETP Lett. 82 (2005) 319. arXiv:gr-qc/0505104; 'Cosmological constant and vacuum energy', Annalen Phys. 14 (2005) 165. arXiv:gr-qc/0405012.
- **del Campo & Zurek 2014** — A. del Campo, W. H. Zurek, 'Universality of phase transition dynamics: Topological defects from symmetry breaking', Int. J. Mod. Phys. A 29 (2014) 1430018. arXiv:1310.1600. DOI:10.1142/S0217751X1430018X.
- **Klinkhamer & Volovik 2008** — F. R. Klinkhamer, G. E. Volovik, 'Dynamic vacuum variable and equilibrium approach in cosmology', Phys. Rev. D 78 (2008) 063528. arXiv:0806.2805. DOI:10.1103/PhysRevD.78.063528.
- **Visser 2002** — M. Visser, 'Sakharov's induced gravity: a modern perspective', Mod. Phys. Lett. A 17 (2002) 977-992. arXiv:gr-qc/0204062. DOI:10.1142/S0217732302006886.
- **Devastato-Lizzi-Martinetti 2014** — A. Devastato, F. Lizzi, P. Martinetti, 'Higgs mass in noncommutative geometry', Fortsch. Phys. 62 (2014) 863-868. arXiv:1403.7567. DOI:10.1002/prop.201400013.
- **ATLAS/CMS Higgs-mass** — Particle Data Group, R. L. Workman et al., 'Review of Particle Physics' (Higgs boson mass m_H = 125.25 +/- 0.17 GeV), Prog. Theor. Exp. Phys. 2022 (2022) 083C01. DOI:10.1093/ptep/ptac097. (ATLAS+CMS combination.)
- **Planck 2018** — Planck Collaboration, N. Aghanim et al., 'Planck 2018 results. VI. Cosmological parameters', Astron. Astrophys. 641 (2020) A6. arXiv:1807.06209. DOI:10.1051/0004-6361/201833910.
- **BICEP/Keck 2024** — BICEP/Keck Collaboration, 'Improved Constraints on Primordial Gravitational Waves using Planck, WMAP, and BICEP/Keck Observations through the 2018 Observing Season', Phys. Rev. Lett. 127 (2021) 151301; 2024 update. arXiv:2110.00483. DOI:10.1103/PhysRevLett.127.151301.
- **Popovic et al. 2025 (DES-Dovekie)** — B. Popovic et al. (DES Collaboration), 'DES-Dovekie' joint w0waCDM analysis (DES-Dovekie SN + DESI DR2 BAO + Planck 2018 + ACT-DR6 + SPT-3G), arXiv:2511.07517v3 (2025). w0 = -0.803 +/- 0.054, wa = -0.72 +/- 0.21, rho(w0,wa) ~ -0.85.
- **DES Y3 2021** — DES Collaboration, T. M. C. Abbott et al., 'Dark Energy Survey Year 3 Results: Cosmological Constraints from Galaxy Clustering and Weak Lensing', Phys. Rev. D 105 (2022) 023520. arXiv:2105.13549. DOI:10.1103/PhysRevD.105.023520.
- **Repo retraction log (Atlas D09) + assumptions status (Atlas D04)** — sessions/framework/Atlas/atlas-09-retractions.md (retraction log) + sessions/framework/Atlas/atlas-04-assumptions.md (assumptions/conditional status). Internal self-citation — the framework's own visible self-correction record (capstone-hygiene-gate.md).

---

## Substrate-first framing preservation

The INHERITED/NOVEL tagging does NOT invert any explanation direction. The arrow `D_K eigenvalues -> spectral-action moments -> emergent physics -> measurement` is unchanged. The citation anchoring signals which pillars the substrate-first derivation stands ON (INHERITED: spectral action, heat-kernel a_n discipline, q-theory, KZM, emergent-gravity genre) and which it EXTENDS (NOVEL-BEYOND: the SU(3)-manifold same-object move CITE-2, the GGE-relic-IS-CMB CITE-5, the Volovik-partition CC residual CITE-6, the KK-threshold Higgs band CITE-7). The framework claims novelty exactly where it derives substrate-IS physics the inherited pillars do not, and inherits exactly where the machinery is canonical NCG / emergent-gravity.

## Cross-references

- **Capstone (inline anchors)**: `sessions/framework/phonic-exflation-equation.md §"Citation anchors"`.
- **Source recommendation**: `deep-research-report.md §"Suggested citations for the capstone"`.
- **Curated-doc discipline**: `.claude/rules/capstone-hygiene-gate.md` (Q5 citation add/invalidate); `feedback_framework-hygiene.md` (designated-writer reviewed patch, no bulk append).
- **Research-corpus discipline**: `feedback_research-corpus.md` (citation content from cited sources only).
