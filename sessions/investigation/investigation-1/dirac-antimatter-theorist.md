# Investigation-1 — Antimatter / CPT / J-Operator Vantage

**Agent**: dirac-antimatter-theorist (Workhorse-Antimatter)
**Domain**: Dirac equation, CPT symmetry, charge conjugation, the NCG real structure J, BDI topological classification, baryon asymmetry, precision antimatter constraints.
**Vantage**: I follow the Clifford algebra and the real structure J wherever they lead, and I take every solution seriously — including the under-produced ones. My job here is to test the framework's antimatter-sector self-assessment at the equation level and find where the algebra has been over-extended, under-explored, or quietly contradicted.

**What I actually read** (this session, not from memory):
- Framework narrative: `atlas-00-index.md`, `atlas-04-assumptions.md` (full §I-§IX), `atlas-08-open-questions.md` (Q1-Q20 + S97-S107 freshness bullets), `atlas-08-freshness-S107.md`.
- Registries: `falsifier-master-inventory.md` (Rows #66, #67, #80, #81, #82 + structure), `evoi-framework.md` (Tier-1/Tier-2, esp. Rank-8 BARYOGEN, Rank-3/9b neutrino), `open-channel-ledger.md §C` (row B2).
- Knowledge MCP: `search_knowledge` on baryogenesis / leptogenesis / CPT-Lorentz / fermion-doubling / δ_CP-PMNS / positronium; `trace_entity` baryogenesis + transit-baryogenesis; `get_constant` on `phi_CP_K7_transit`, `phi_CP`, `epsilon_K7`, `delta_CP_PMNS_substrate`, `eta_BBN_obs`, `M_KK`; `list_constants` on the CP/baryo family.
- Antimatter corpus: papers 14 (open questions), 21 (LHCb 2025 baryon CP), 32 (Villata ALPHA-g), and my own memory (T1-T11, S96 W4-3/W4-5 Majorana + Yukawa-chirality, S71).

**Headline correction to my own memory**: My MEMORY.md still records "Baryogenesis Status (S43): ALL internal J-breaking CLOSED" and lists "external baryogenesis mechanism" as an *open question*. That is stale. Post-S43, the framework (S97 W3-2 → S98 W3-2) **sourced** an external baryogenesis mechanism (a φ_88-Cartan non-left-invariant deformation δA) and now carries η_B as a substrate-FIXED, zero-free-CP-parameter prediction — but one that **under-produces the observed value by ~1.1 OOM**. The EVOI table marks this "CLOSED-SOURCED-UNIQUE → §5"; atlas-04 C6 carries it "CONDITIONAL." That gap between the two self-assessments is the single most important thing in this report. I have re-derived the relevant chain and cite it faithfully below.

A note on epistemic types throughout: I tag **PROVEN** (machine-ε structural / NCG-axiomatic), **CONDITIONAL**, **BROKEN/RETRACTED**, and **SPECULATIVE**. A negative result is a boundary, not a failure.

---

## 1. BIGGEST GAPS

### G-1. The η_B under-production: a "closed" result that misses observation by 13.5×

This is the largest gap in my domain and it is partly hidden by inconsistent status-tagging.

The framework's own three exact substrate nulls — all of which I proved or co-proved — are:
1. η_B(D_K) = 0 by `[J, D_K] = 0` (T1; PROVEN, machine-ε; `atlas-04` G8 at 79,968 pairs, dev 3.29e-13).
2. BDI winding ν = 0 / no protected CP-odd zero mode (T4; PROVEN; `atlas-04` B5).
3. φ_CP ≡ 0 intrinsic (`canonical_constants.py: phi_CP = 0`; PROVEN, algebraic — "BCS baryogenesis (φ_CP=0 identically)" closed S52, knowledge.db `closed_regv_eraVII_77`).

Given those three nulls, the substrate **cannot** baryogenerate from any internal left-invariant structure. T11 sealed this: `C2·conj(D_K)·C2 = D_K` for ANY left-invariant metric on SU(3) (PROVEN; extends to the full 36D moduli). So a baryon asymmetry **requires** physics external to the SU(3) Dirac operator. That is correct and I stand behind it.

The S98 resolution (`S98-W3-2-BARYOGEN-UNIQUENESS` PASS, audit `3be22b8a`; `atlas-04` C6) introduces exactly such an external object: a **non-left-invariant deformation `δA` in the φ_88-Cartan direction**, with `ε_nLI = ε_K7²/n_pairs` and `φ_CP = π/2` declared "substrate-FIXED, not scanned." It yields a UNIQUE in-window `η_B = 4.52e-11`, and identifies φ_88-Cartan as the unique non-leptophilic CP source (`ε_CP(φ_67) = ε_CP(λ_3) = 0` EXACT).

I re-derived the amplitude chain as a sanity check (math-scripts substitution discipline):
- `ε_nLI = ε_K7² / n_pairs = (0.00248)² / 59.8 = 6.1504e-6 / 59.8 = 1.0285e-7` (using `epsilon_K7 = 0.00248` and the T4 pair count `n_pairs = 59.8`).
- C6 reports the scan representative `ε* = 6.31e-8` — same order of magnitude as my `ε_nLI`, factor ~1.6 apart (consistent; the difference is the in-window solve vs the closed-form ratio).
- Under-production: `η_B(pred)/η_B(obs) = 4.52e-11 / 6.12e-10 = 0.0739` → **a factor of 13.5, i.e. 1.13 OOM short**. This matches `open-channel-ledger §C` B2 ("~1.1 OOM") exactly.

**The gap, stated plainly**: a prediction that is (a) one order of magnitude below observation and (b) sourced by a hand-introduced deformation whose amplitude and phase are *posited* ("substrate-FIXED" by the posit `ε_nLI = ε_K7²/n_pairs`, not derived from a variational principle on the substrate) is **not a closure** in the sense the EVOI table's "CLOSED-SOURCED-UNIQUE" tag implies. It is an existence proof with the right sign (η_B > 0, baryon excess — good) and the wrong magnitude. The δA object lives *outside* the proven structure precisely because the proven structure forbids the effect; its specific form (φ_88-Cartan, that ε_nLI relation) is a choice, not a derivation. Two things are underived: (i) *why* δA points along φ_88-Cartan rather than any of the other 7 broken generators, and (ii) *why* `ε_nLI = ε_K7²/n_pairs` rather than some other power. C6 is honest about this ("PASS is of EXISTENCE, NOT uniqueness" at S97; the S98 "uniqueness" is uniqueness-given-the-posit). The EVOI tag is not honest about it.

### G-2. No baryogenesis falsifier row in the master inventory

`falsifier-master-inventory.md` has rows for n_PBH (#65/#66), BAO two-speed (#67), 0νββ m_ββ (#80), H₀ (#81), β_pivot (#82) — but **no η_B row**. The single most consequential antimatter-sector number the framework produces (4.52e-11, 1.1 OOM from the most precisely known cosmological baryon-asymmetry datum `eta_BBN_obs = 6.12e-10 ± 4e-12`) is not in the falsifier surface at all; it lives only as an assumptions-registry cell (C6). This is a structural gap: a prediction that misses a 0.65%-precision observation by 13.5× should be the framework's loudest live falsifier, with the δA-posit explicitly flagged as the failure locus.

### G-3. No compact-object / antimatter-annihilation-domain sector at all

`atlas-08` S106 bullet records a NEW "CORPUS-EXCEEDS open question": the framework has no compact-object sector (no mass-radius, formation channel, compactness bound, QNM-echo spectrum). I add the antimatter face of this: the framework has **no treatment of the cosmological matter-antimatter domain structure** (Antimatter paper 14 Q7: antimatter fraction < 10⁻⁵ within ~10 Mpc from Fermi-LAT annihilation-line non-detection). The framework's transit produces a CPT-symmetric GGE relic; the asymmetry is then injected by δA at a single value. There is no account of *spatial* domain formation, no prediction for the annihilation-boundary gamma flux, and therefore no engagement with one of the seven great antimatter questions. GEOMETRIC/PHONONIC status: this is genuinely untraveled (see §5, UB-2).

### G-4. M_KK enters the η_B prediction as "undetermined" while being a frozen canonical constant

C6 states "M_KK undetermined" as a caveat on the η_B precision. But `M_KK` IS a canonical constant: `get_constant("M_KK") = 7.4287e16 GeV` (alias of `M_KK_gravity`, frozen S42 CONST-FREEZE-42). The resolution is that the η_B mechanism's M_KK-sensitivity is a *different* scale-readout than the gravity-anchored alias — the same `O = w·Ô` rank-1 normalization non-universality (§VII.BS, S102) that scopes the a(t) gap. This is not a contradiction, but it IS an unstated coupling: the baryon asymmetry's absolute normalization inherits the framework's single un-derived dimensional scale. Until M_KK is derived (the standing "M_KK-DERIVATION" gap, EVOI §6), the η_B magnitude carries that same irreducible external input *on top of* the δA posit. The 1.1-OOM miss could in principle be a wrong M_KK as easily as a wrong δA — and the framework cannot currently separate the two. That degeneracy is a gap.

---

## 2. CRITICAL CONTRADICTIONS

### C-1. EVOI "CLOSED" vs atlas-04 "CONDITIONAL" on baryogenesis (status contradiction)

- `evoi-framework.md §2` Rank-8: "**CLOSED-SOURCED-UNIQUE → §5** … matter-sector frontier #9 closes at zero free CP parameters."
- `atlas-04` C6: "Status **HELD CONDITIONAL** — the sourced η_B is sharpened to a single substrate-forced value but is still under-produced vs observed 6.12e-10 by ~1.1 OOM (prediction tightened, observation not yet matched)."
- `open-channel-ledger §C` B2: "**CLOSED at uniqueness** (zero free CP params). Residual: η_B under-produced … by ~1.1 OOM."

Three curated registers, three different framings of the same result. The EVOI tag retiring the row "to §5" (resolved) directly contradicts the assumptions register holding it CONDITIONAL with an un-matched observation. This is exactly the kind of capstone-hygiene drift the `capstone-hygiene-gate.md` Q3 discipline exists to catch. **Resolution direction**: the assumptions register is correct (CONDITIONAL); the EVOI "CLOSED" is over-confident. A 1.1-OOM miss with a posited source is not closure — it is a sourced-but-failing prediction whose §5 retirement removes it from the priority queue prematurely. Recommend down-tagging the EVOI row to CONDITIONAL and minting the η_B falsifier row (G-2).

### C-2. The Villata corpus document's "α_g ~ 0.1-1% from BCS asymmetry" contradicts my proven a_g = g (PROVEN vs SPECULATIVE-in-corpus)

`researchers/Antimatter/32_2024_Villata` §"Connection to Phonon-Exflation Framework" asserts (as a framework prediction): "phonon-exflation predicts α_g ~ 0.1-1% from emergent BCS asymmetry … the BCS substrate has intrinsic particle-antiparticle asymmetry in pairing structure, leading to ~1% correction to effective gravitational mass ratio. If blind reanalysis confirms α_g > 0.3, phonon-exflation requires exotic BCS phase."

This is **wrong** and contradicts the proven structure. My S42 result (and memory line 54, S36 physical content): the BCS condensate is **J-even**, and a J-even condensate gives `a_g = g` **exactly** (`atlas-04` would carry this under the WEP-structural reading; the J-even parity is the proven object). The condensate is a same-sign K_7 pairing within the B2 singlet sector — it is **not** a particle-antiparticle asymmetry (memory line 52: "Cooper pairs: same-sign K_7 pairing … NOT particle-antiparticle"). There is no intrinsic particle/antiparticle gap asymmetry in the proven framework. The corpus paper (written before the S43 closures matured) projected a percent-level a_g deviation that the framework's own algebra forbids: `[J, D_K] = 0` ⟹ spectrum is `(λ, -λ)`-paired ⟹ gravity (which couples to eigenvalues / a_2 moment) cannot distinguish particle from antiparticle, and the J-even condensate preserves this. The ALPHA-g central value α_g = 0.75 ± 0.29 is, in the proven framework, a **systematic to be scattered to zero by AEgIS/GBAR**, NOT a 1% BCS signal.

This is a genuine contradiction between a corpus-document framework-connection note and the proven theorem set. It should be corrected in the corpus (the paper-connection prose, not the falsifier registry, which correctly carries no α_g BCS-deviation row). I flag it as adversarial honesty: the proven answer is `a_g = g` to all orders the framework can compute, and any future ALPHA-g/AEgIS deviation at the 10⁻³-10⁻⁴ level would be a *falsifier* of the framework, not a confirmation of an "exotic BCS phase."

### C-3. δ_CP^PMNS = {0, π} (lepton sector CP-conserving) vs φ_CP^K7 = π/2 (baryon sector maximally CP-violating) — a structural tension the framework treats as resolved-by-sector-split

`canonical_constants.py`: `delta_CP_PMNS_substrate = 0.0` (discrete set {0, π}, "substrate-forced," `S99-W3-SEESAW-SUMMNU`; Jarlskog J = 0 EXACT, certified `S101-Z3-PHASE-REPHASING-INVARIANCE`). Simultaneously `phi_CP_K7_transit = π/2` (maximal, `S98-W3-2`). So the framework predicts **zero leptonic Dirac CP violation** but **maximal baryogenesis CP violation**, from two different generators (φ_88-Cartan for baryons; the leptonic phase rephased away). The framework frames this as a clean sector-split (the Z₃ phase "relocates to the Majorana column," Row #80 annotation), so it is not a logical contradiction. But it is a structural *tension* that the framework has not stress-tested: in essentially every standard baryogenesis-via-leptogenesis scenario, the leptonic CP phase and the baryon asymmetry are linked. Here they are decreed orthogonal. If DUNE/T2HK/Hyper-K measure δ_CP^PMNS ≠ {0, π} at high significance (current global fits already mildly prefer δ_CP ≈ 1.5π, ~2.5σ from CP-conservation), the framework's leptonic prediction fails AND the claimed orthogonality of the lepton/baryon CP sectors comes under pressure — because then *both* sectors carry CP violation and the "φ_88-Cartan is the unique CP source" claim needs the leptonic phase explained, not rephased. The framework currently has δ_CP^PMNS = {0,π} as a **falsifiable zero-parameter prediction** (good!) but has not engaged what its failure would do to C6. This is a contradiction-in-waiting, sharpened by data trending against it.

---

## 3. UNSUPPORTED LOAD-BEARING ASSUMPTIONS

### LBA-1. The δA = φ_88-Cartan deformation: form, direction, and amplitude all posited

(Detailed in G-1.) The entire baryogenesis closure rests on a single externally-introduced object whose three defining choices are unsupported by derivation:
- **Direction**: why φ_88 (Cartan hypercharge) and not one of the other broken generators? The claim "φ_88-Cartan is the UNIQUE non-leptophilic CP source" is supported by `ε_CP(φ_67) = ε_CP(λ_3) = 0` EXACT — but that only shows φ_67 and λ_3 give zero; it does not show φ_88 is forced, only that it is the survivor among a tested few. This is a uniqueness-by-elimination over an incompletely-enumerated set.
- **Amplitude relation**: `ε_nLI = ε_K7²/n_pairs` is a posited functional form. Why ε_K7-squared? Why divided by the pair count? No variational or symmetry argument is cited for this specific combination.
- **Phase**: φ_CP = π/2 "substrate-FIXED" — but the framework simultaneously rephases the leptonic δ_CP to {0,π}. Why is the baryon-sector deformation locked at maximal while the lepton-sector phase is removable? Both are "substrate-forced" by fiat.

This is the load-bearing assumption that the entire matter-sector frontier-#9 closure depends on, and it is structurally the weakest link in the framework's antimatter sector. It is the analog, in my domain, of the K_pivot = 2.0 M_KK assumption (C2, BROKEN) in the cosmology sector: a number that the framework needs but cannot derive.

### LBA-2. n_pairs = 59.8 and the "exactly 2 pair-breaks during transit" requirement

C6's *original* S42 mechanism required "exactly 2 pair breaks during transit and specific M_KK." The pair count `n_pairs = 59.8` (T4, PROVEN from the sudden-quench Bogoliubov calc, `atlas-04` T4) is solid, but the "exactly 2 break" requirement that converts the relic into an asymmetry is an assumption about the transit microphysics that has never been derived from the GGE dynamics. The S98 mechanism re-routes through δA rather than pair-breaking, but the n_pairs = 59.8 still enters the amplitude (`ε_nLI = ε_K7²/n_pairs`), so the pair-count is doing load-bearing work in the magnitude. If the effective pair count relevant to the CP-violating amplitude differs from 59.8 (e.g. only the B2-fraction, 93%, or only the singlet sub-sector participates), the η_B normalization shifts.

### LBA-3. "J-even condensate ⟹ a_g = g exactly" assumes loop/many-body corrections preserve J-parity

This one is MOSTLY proven and I want to be precise about where the support ends. `[J, D_K] = 0` is PROVEN at tree level for any left-invariant metric (T1/T11). The BCS condensate being J-even is PROVEN at the mean-field level (S36, S46; `Delta_{J-odd}/Delta < 10^{-12}`). What is *assumed* is that no higher-loop or non-perturbative effect introduces a J-odd condensate component. The corpus paper 32 (C-2 above) actually probes this seam — it claims loops *do* break it. The proven framework says they don't (the Gram-matrix PSD theorem and the BDI Pfaffian protection are structural, S46), but a fully non-perturbative proof that the condensate parity is J-even to all orders is not in hand. This is a genuine, if narrow, load-bearing assumption: the framework's `a_g = g` prediction (and hence its consistency with ALPHA-g) rests on J-parity surviving beyond mean-field. I rate the support strong but not complete.

### LBA-4. The lepton δ_CP rephasing assumes the Z₃ phase has no physical Majorana imprint beyond m_ββ

`delta_CP_PMNS_substrate = {0,π}` is justified by "the Z₃ generation-map phase is rephasing-REMOVABLE on both substrate-pinned legs, Jarlskog J = 0 EXACT." The phase "relocates to the Majorana column" (Row #80). This is internally consistent, but it assumes the only physical residue of the Z₃ phase is in the Majorana sector (m_ββ band [1.516, 3.695] meV). If there is any process sensitive to the Dirac phase that the framework has not enumerated, the rephasing argument leaks. The assumption that the rephasing is *complete* (J = 0 EXACT covers all observables) is load-bearing for the δ_CP^PMNS = {0,π} prediction.

---

## 4. AREAS NEEDING REFINEMENT

### R-1. Mint the η_B falsifier row and reconcile the three status tags

Concrete: `mack-cosmic-bridge` (sole writer of `falsifier-master-inventory.md`) should land an η_B row carrying: prediction 4.52e-11; observation `eta_BBN_obs = 6.12e-10 ± 4e-12`; **σ-distance ≈ 1.1 OOM (a ~135σ tension if taken at face value against the 0.65%-precision BBN datum)**; the δA-posit explicitly named as the failure locus; falsifier function = "any first-principles derivation of δA that does NOT recover ε_nLI = ε_K7²/n_pairs at φ_CP = π/2 falsifies the closure; the magnitude is already failing." Then reconcile C1: down-tag the EVOI Rank-8 from CLOSED to CONDITIONAL.

### R-2. Sharpen the δ_CP^PMNS = {0,π} prediction into a dated DUNE/Hyper-K live-watch

This is a *good* zero-parameter prediction (`delta_CP_PMNS_substrate`, Jarlskog J = 0 exact) and it deserves promotion from a buried Row-#80 annotation to a first-class falsifier row with a detector horizon. DUNE (first beam ~2029-2031) and Hyper-Kamiokande will measure δ_CP to ~±15-20° within the decade. Current T2K+NOvA global fits prefer δ_CP ≈ 1.5π at ~2.5σ from {0,π}. This is one of the framework's sharpest near-term falsifiable predictions and it is currently invisible in the falsifier surface. PARTICLE classification.

### R-3. Re-examine whether δA must be φ_88-Cartan via complete generator enumeration

LBA-1's uniqueness-by-elimination is incomplete. A refinement gate: enumerate ALL non-left-invariant deformation directions (the off-Jensen 35D moduli are characterized, S76 W2-J; the CP-odd subset is finite) and compute `ε_CP` for each. If φ_88 is genuinely the unique nonzero CP source over the *complete* set, the uniqueness claim is earned. If others contribute, the "unique CP source" claim must be retracted and the η_B prediction becomes a sum (likely larger — which would help the 1.1-OOM miss). This is a tractable, well-posed computation on existing infrastructure.

### R-4. Correct the corpus paper-32 framework-connection prose (a_g)

`researchers/Antimatter/32_2024_Villata` §"Connection" should be corrected to reflect the proven `a_g = g` (J-even condensate), not the speculative "α_g ~ 0.1-1% from BCS asymmetry." The framework's actual prediction is that ALPHA-g's central value scatters to zero; a confirmed nonzero α_g would *falsify* the framework, not confirm an exotic phase. (This is a documentation-hygiene refinement, not a physics gate.)

### R-5. State the M_KK-degeneracy in the η_B magnitude explicitly

Per G-4: the η_B absolute normalization inherits the single un-derived dimensional scale M_KK via the §VII.BS rank-1 normalization non-universality. C6's "M_KK undetermined" caveat should be linked explicitly to the §VII.BS theorem and the M_KK-DERIVATION standing gap, so the 1.1-OOM miss is correctly attributed: it could be δA-form OR M_KK, and the framework cannot yet separate them. This is a precision-of-attribution refinement.

---

## 5. UNTRAVELED BRIDGES (most important)

These are known results / open mysteries in my domain that the framework has **not** engaged and that could become springboards — with explicit sketches of how the substrate (D_K spectrum, spectral moments, GGE relic, supersonic transit, Jensen deformation) fills the cement, and how each bridges two of the gaps/contradictions above.

### UB-1. LHCb 2025: percent-level CP violation in baryon decays from strong-phase rescattering → a substrate mechanism for the missing OOM in η_B

**The result** (`researchers/Antimatter/21_2025_LHCb`, arXiv:2504.15008, Nature Physics): first observation of CP violation in baryon decays — Λ_b⁰ → pK⁻π⁺π⁻ with A_CP = (2.45 ± 0.46)% global (5.2σ), (5.4 ± 0.9)% local (6.0σ). Crucially, the asymmetry is **localized to the π⁺π⁻ resonance region** (ρ(770), σ/f₀(500), f₀(1370)) and is driven by **final-state strong-interaction rescattering phases**, not by the weak penguin loops that dominate meson CP violation. The interference is `A_i e^{iδ_i}` (weak × strong phase). N-pion rescattering models predict 5.6-5.9%; observation is 5.4%.

**Why this is untraveled**: The framework's baryogenesis (C6) is built entirely on a *weak* CP phase (φ_CP = π/2 in the δA deformation). It has never engaged the possibility that the baryon-sector CP violation relevant to baryogenesis is dominated by **strong final-state phases** — exactly the lesson LHCb just delivered. The framework's transit produces a dense instanton gas (`S_inst = 0.069`, B8) and a strongly-interacting GGE relic; this is precisely the regime where strong rescattering phases are large.

**How the substrate fills the cement**: The strong-interaction phase δ_i in the LHCb amplitude has a natural substrate analog: the **scattering phase of post-transit GGE quasiparticles re-overlapping at a fiber** (the substrate picture of "two relay patterns overlap at a single fiber" — `phononic-framing.md`). The B2 condensate sector carries the K_7 charge and the φ_88 CP-source; the *gapped-branch scattering phases* between the 7 gapped GGE branches (whose Layer-1/Layer-2 two-speed splits are already computed, Row #67) are the substrate's "final-state interaction phases." Concretely: the CP-violating amplitude that sources η_B should be `Im[A_weak(φ_88) · A_strong(GGE-rescattering)]`, where the strong piece is the inter-branch overlap phase — currently set to zero implicitly in C6. **A non-zero GGE-rescattering phase would multiply the η_B amplitude and could supply the missing factor 13.5** (1.1 OOM). LHCb shows baryon-sector CP enhancement of ~percent from rescattering vs ~per-mille from weak phases alone — a factor ~10-30 enhancement, which is the right size to close G-1.

**Bridge**: This bridges **G-1 (η_B under-production)** and **C-3 (lepton/baryon CP tension)**. It supplies the missing OOM via a substrate-native strong phase (G-1), AND it explains C-3 structurally: the lepton sector has no strong final-state rescattering (leptons don't QCD-rescatter), so δ_CP^PMNS = {0,π} (CP-conserving) while the baryon sector gets large CP from rescattering — the orthogonality of the two CP sectors becomes *derived* (strong-phase presence) rather than decreed. Concrete gate: compute the inter-branch GGE scattering phase at τ_fold from the existing 8-branch spectrum (Row #67 infrastructure) and insert it into the C6 amplitude.

### UB-2. Cosmic antimatter-domain bounds (Fermi-LAT) → a supersonic-transit prediction for the acoustic white hole's causal-disconnection scale

**The mystery** (`researchers/Antimatter/14` Q7): no antimatter stars/galaxies/domains observed; antimatter fraction < 10⁻⁵ within ~10 Mpc; annihilation-boundary MeV gamma flux not seen by Fermi-LAT. Standard cosmology has no clean account of *why* the universe is single-domain rather than a matter/antimatter patchwork.

**Why untraveled**: The framework has the η_B *amplitude* (C6) but says nothing about the *spatial structure* of the asymmetry — whether it is global (single domain) or domain-walled. This is the antimatter face of the S106 "CORPUS-EXCEEDS compact-object gap" (G-3).

**How the substrate fills the cement**: The framework's transit is a **supersonic passage through the van Hove fold at Mach 13.75**, producing an **acoustic white hole** (`phononic-framing.md`: "pre/post-transit causally disconnected by supersonic flow"). The δA deformation that sources η_B acts *during* this transit. If δA is **spatially uniform across the causally-connected pre-transit region**, the asymmetry is single-domain by construction — the acoustic white hole's causal horizon sets the domain size, and it is super-horizon (the whole observable universe was inside one causally-connected pre-transit patch). This is the substrate's natural answer to Q7: **the universe is single-domain because the baryogenesis-sourcing δA was imprinted on a single causally-connected acoustic patch before supersonic transit disconnected it from any other patch** — exactly the mechanism inflation invokes for the horizon problem, but here it is the acoustic white hole (a proven structural feature, not an added field). Prediction: zero annihilation-boundary gamma flux within the acoustic horizon (consistent with Fermi-LAT), with the domain scale = the pre-transit sound-horizon.

**Bridge**: This bridges **G-3 (no antimatter-domain sector)** and **LBA-1 (δA posit)**. It gives the δA deformation a *spatial* characterization (uniform on the pre-transit acoustic patch) that both fills the missing antimatter-domain sector AND constrains the δA posit (it must be coherent across the causal patch, which is a real physical constraint, not a free choice). Concrete: compute the pre-transit acoustic sound-horizon from the Mach-13.75 transit and check it exceeds the present Hubble scale (it should, by the same white-hole argument that solves the horizon problem).

### UB-3. Kostelecky SME data tables (2026) + neutral-meson CPT → a Jensen-deformation bound on emergent Lorentz/CPT violation

**The result** (`researchers/Antimatter/18_2026_Kostelecky` data tables; `26_2024_Roberts` neutral-meson CPT review): the Standard Model Extension catalogs ~hundreds of Lorentz/CPT-violating coefficients with experimental bounds; neutral-meson oscillations (K⁰, B⁰, D⁰) bound CPT-violating mass differences to extraordinary precision (e.g. |m_{K⁰} − m_{K̄⁰}|/m_K < 10⁻¹⁸).

**Why untraveled**: The framework proves CPT exact at the *static* level (`[J, D_K] = 0`, T1). It has NOT computed whether the **Jensen deformation dynamics** (the `tau`-flow that IS cosmic time, C1) induces any *effective* Lorentz/CPT-violating SME coefficient at the emergent 4D level. The S75 `S75-K1-EMERGENT-LORENTZ` gate touched emergent Lorentz invariance but I find no SME-coefficient computation.

**How the substrate fills the cement**: The framework already has the clock-violation bound `dα/α = -3.08·τ̇` ⟹ `|τ̇| < 5e-18/yr` (my memory; Rolling-modulus closure, S22d). A time-dependent τ is *exactly* a candidate source of an effective SME coefficient — a slowly-varying background that picks out a preferred frame (cosmic time). The substrate prediction: the leading SME coefficient is `∝ τ̇ · (spectral moment)`, and the existing `|τ̇| < 5e-18/yr` bound translates directly into an SME-coefficient bound. Because `[J, D_K] = 0` is exact at every τ-slice (T11), the *CPT-odd* SME coefficients vanish identically (the framework predicts ZERO CPT violation — consistent with all neutral-meson bounds, and a structural prediction, not a fit), while the *Lorentz-violating-but-CPT-even* coefficients are bounded by τ̇. This is a clean, computable bridge: map the framework's τ-dynamics onto the SME coefficient basis.

**Bridge**: This bridges **LBA-3 (J-parity beyond mean-field)** and **C-2 (a_g contradiction)**. The neutral-meson CPT bounds (|m_K − m_K̄| < 10⁻¹⁸) are the most stringent test of `[J, D_K] = 0` available — far tighter than antiproton q/m (16 ppt). If the framework's J-parity survives to the loop level (LBA-3), it must produce zero CPT-odd SME coefficients; the neutral-meson bounds then *constrain the loop corrections* (UB-3 turns LBA-3 from an assumption into a bounded quantity). And it resolves C-2: the same J-evenness that gives `a_g = g` gives zero CPT-odd SME coefficients — so the corpus paper's "1% BCS asymmetry" is doubly excluded (it would show up in neutral-meson CPT tests at a level already ruled out by ~14 orders of magnitude).

### UB-4. AEgIS/ALPHA positronium & antihydrogen BEC + the J(e⁻e⁺) = e⁺e⁻ self-conjugacy → a substrate test of the GGE relic's CPT-neutrality

**The result** (`researchers/Antimatter/11_AEgIS` positronium laser cooling 2024; paper 14: positronium BEC targeted < 10 K, "transformative"; `17_2024_ALPHA` hyperfine 1S-2S): positronium (e⁻e⁺) is its own antiparticle under C, `J(e⁻e⁺) = e⁺e⁻ = e⁻e⁺` (corpus framework-discussion S-6). A positronium BEC would be a macroscopic, CPT-self-conjugate condensate.

**Why untraveled**: The framework's dark-matter candidate is the **Leggett-channel GGE quasiparticle: "CPT-neutral, non-annihilating"** (`phononic-framing.md`; LEGGETT-MOMENT-70, Ω_DM h² = 0.120, 0.6% from Planck). The CPT-neutrality of the GGE relic is *asserted* (from J-symmetry) but has no laboratory analog test. Positronium BEC is the natural one: a J-self-conjugate condensate is exactly the structure the GGE relic claims to be.

**How the substrate fills the cement**: The GGE relic is a product state (`S_ent = 0`, T2) of Bogoliubov pairs that is J-invariant (S42: "GGE J-symmetric: DM prediction CPT-exact"). A positronium BEC is a J-self-conjugate macroscopic condensate. The substrate prediction maps onto a measurable property: the **collective-mode spectrum of a J-self-conjugate condensate is itself `(λ, -λ)`-paired** (the same BDI pairing, T3). AEgIS/ALPHA Ps-BEC collective excitations should show this pairing if the substrate analogy holds. More concretely, the framework's claim that the Leggett-channel relic is "non-annihilating despite being CPT-neutral" (the resolution of why DM doesn't self-annihilate) has a direct Ps-BEC test: Ps normally self-annihilates (τ ~ 142 ns for ortho-Ps), but the framework's mechanism (the Leggett mode is *inter-band coherence*, off the annihilation channel by `[iK_7, D_K] = 0` selection) predicts a *protected* sub-channel. Whether a Ps-BEC can be stabilized against annihilation in a specific collective mode is a laboratory probe of the substrate's "non-annihilating CPT-neutral" claim.

**Bridge**: This bridges **G-3 (no compact-object/annihilation sector)** and the DM identity. It gives the GGE-relic CPT-neutrality claim its first laboratory analog (Ps-BEC), and it connects the annihilation-domain gap (G-3, UB-2) to the DM sector through a single structural object: the J-self-conjugate, BDI-paired, annihilation-protected condensate. The substrate says matter-antimatter domains annihilate (Q7) BUT the CPT-neutral GGE relic does not (DM) — and Ps-BEC is where that distinction can be tested.

### UB-5. The Boyle-Farnsworth / Bochniak-Sitarz algebraic-SM and fermion-doubling line → a derivation route for the δA direction (closing LBA-1)

**The result** (`researchers/Antimatter/29_2018_Boyle_Farnsworth` algebraic structure of the SM; `22_2020` / `19_2024 Bochniak_Sitarz` fermion doubling and fermion integrals in spectral triples): these works characterize *which* finite spectral triples avoid fermion-doubling and *what* the admissible real-structure-compatible deformations are. Bochniak-Sitarz (paper 19) is already cited in the S100a seesaw adjudication, but only for the fermion-integral normalization — NOT for the deformation-classification content.

**Why untraveled**: LBA-1's central weakness is that δA = φ_88-Cartan is posited, with uniqueness only by incomplete elimination. The Boyle-Farnsworth / Bochniak-Sitarz framework provides exactly the missing tool: a *classification* of real-structure-compatible (J-compatible) deformations of a finite spectral triple. The δA deformation is, by construction, J-*incompatible* (it must break the `C2·conj(D_K)·C2 = D_K` identity to source CP violation — that is the whole point). So the question "which δA?" is precisely "which minimal J-breaking deformation is admissible under the remaining axioms (order-zero, the Frobenius rescue class N3/N7)?"

**How the substrate fills the cement**: Use the Boyle-Farnsworth algebraic constraints + the Bochniak-Sitarz fermion-doubling-avoidance conditions to *enumerate the admissible J-breaking deformations* of `A_F = ℂ ⊕ ℍ ⊕ M₃(ℂ)`. The φ_88-Cartan direction should emerge (or not) as the unique minimal J-breaking deformation that (a) preserves the Frobenius rescue class (N7, the unique 7-axiom algebra), (b) avoids fermion doubling, and (c) is non-leptophilic. If it emerges uniquely, **LBA-1 is closed and the η_B closure becomes a genuine derivation**. If a different direction emerges, the η_B prediction changes (and possibly the magnitude with it — bridging G-1).

**Bridge**: This bridges **LBA-1 (δA posit)** and **G-1 (η_B magnitude)**. It is the route to turn the framework's weakest antimatter assumption (the posited δA) into a derived object, and a different derived δA could simultaneously fix the 1.1-OOM miss. This is the highest-value *structural* bridge because it attacks the load-bearing assumption directly with tools (NCG deformation classification) the framework already has in its corpus but has not applied to baryogenesis.

---

## Highest-Leverage Next Steps (3-5 concrete items)

1. **Reconcile the baryogenesis status tags and mint the η_B falsifier row** (closes C-1, G-2). Down-tag EVOI Rank-8 from CLOSED-SOURCED-UNIQUE to CONDITIONAL; have `mack-cosmic-bridge` land an η_B row in `falsifier-master-inventory.md` (prediction 4.52e-11; obs `eta_BBN_obs = 6.12e-10 ± 4e-12`; ~1.1 OOM / ~135σ under-production; δA-posit named as failure locus). Pure hygiene + honesty; no new physics required. **Effort: one designated-writer dispatch.**

2. **Compute the GGE inter-branch strong-rescattering phase and insert it into the C6 η_B amplitude** (closes/relieves G-1, bridges to C-3 via UB-1). Use the existing 8-branch spectrum and Row #67 two-speed infrastructure to get the inter-branch overlap phase at τ_fold; test whether `Im[A_weak(φ_88)·A_strong(GGE)]` supplies the missing factor ~13.5. Pre-registered threshold: PASS if the rescattering-enhanced η_B lands in [3e-10, 1.2e-9]. **Effort: one compute gate on existing infrastructure.** This is the single highest-EVOI item in my domain — it could convert a failing prediction into a matching one via a substrate-native mechanism that LHCb 2025 just validated experimentally.

3. **Enumerate the admissible J-breaking deformations via the Boyle-Farnsworth / Bochniak-Sitarz classification** (closes LBA-1, bridges to G-1 via UB-5). Apply the NCG deformation-classification tools (already in corpus papers 19/22/29) to `A_F = ℂ ⊕ ℍ ⊕ M₃(ℂ)` under the Frobenius rescue class. PASS if φ_88-Cartan emerges as the unique minimal non-leptophilic J-breaking deformation; INFO if a finite admissible set emerges (then η_B becomes a sum). **Effort: one structural workshop (connes-ncg + me).**

4. **Promote δ_CP^PMNS = {0,π} to a first-class dated falsifier row** (R-2, addresses C-3). Land it with DUNE/Hyper-K horizons (~2029-2031) and the current ~2.5σ T2K+NOvA tension against {0,π}. This is one of the framework's sharpest zero-parameter near-term predictions and it is currently invisible. **Effort: one mack-cosmic-bridge dispatch.**

5. **Correct the corpus paper-32 a_g prose** (R-4, closes C-2). Replace the speculative "α_g ~ 0.1-1% from BCS asymmetry" with the proven `a_g = g` (J-even condensate); state that a confirmed nonzero α_g at 10⁻³-10⁻⁴ would *falsify* the framework. Cross-link UB-3: the same J-evenness gives zero CPT-odd SME coefficients (neutral-meson bound 10⁻¹⁸). **Effort: documentation-hygiene edit.**

---

*Adversarial-honesty summary*: The framework's static CPT structure (`[J,D_K]=0`, KO-dim 6, BDI, T11) is genuinely PROVEN and is the strongest part of the antimatter sector — I stand fully behind it. The framework's *dynamical* baryogenesis is its weakest part and is over-tagged as closed: a hand-posited δA deformation yielding a prediction 13.5× below observation is a sourced-but-failing prediction, not a closure. The most promising untraveled bridge — and the reason I'd spend the next compute cycle there — is that LHCb's 2025 discovery of large strong-phase-driven baryon CP violation supplies exactly the substrate-native enhancement (GGE inter-branch rescattering phase) the framework needs to close the 1.1-OOM gap, and it would *derive* the lepton/baryon CP-sector orthogonality the framework currently decrees.
