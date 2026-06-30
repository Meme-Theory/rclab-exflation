# S79 — Phononic Length & Substrate-c Consolidation Synthesis

**Author**: phonon-first-cosmologist (solo synthesis)
**Date**: 2026-04-16
**Format**: /rclab-review condensed — single-author
**Scope**: Consolidate the QA excursion on "phononic length" as a term-of-art and the substrate-c hierarchy, producing an S80 carry-forward with pre-registered canonicalization gates.

## Header

### Source documents (primary)
- QA excursion report: *Phononic Length & Substrate c — Consolidated Current-State Report* (delivered inline, S79)
- `computations/canonical_constants.py` (current live state, verified S79)
- `C:/Users/ryan/.claude/projects/C--sandbox-Ainulindale-Exflation/memory/project_substrate-not-c-limited.md` (user-articulated doctrine, 2026-04-11)
- `sessions/archive/session-79/workshops/p1-3-w1b-iteration-audit.md` (PRU Class-8 formalization, Nazarewicz + gen-physicist)
- `sessions/archive/session-79/workshops/p4-d-ratios-vs-absolutes-meta.md` (ratio/absolute meta-pattern, referenced)
- `sessions/archive/session-79/workshops/p4-c-w2d-fstar-outside-cluster.md` (sibling class, referenced)
- `sessions/archive/session-79/workshops/p4-a-w3k-rank-universality.md` (rank-universality, referenced)
- `computations/s42_gradient_stiffness.py:1017-1020` (c_fabric derivation)
- `sessions/archive/session-52/session-52-phonon-workshop.md:86-135` (c_Gold, omega_L, K*)
- `sessions/archive/session-67/session-67-transit-phonon-first-workshop.md:93-110` (c_BLV derivation)

### Scope statement
This synthesis consolidates two parallel but distinct physical categories — (i) the length scale(s) that deserve the term-of-art "phononic length" and (ii) the velocity hierarchy of fabric vs phononic modes — that have been using ad-hoc provenance throughout S22–S78. It diagnoses the omission as a Class-8 PRU (per `p1-3`), pre-registers the S80 canonicalization wave, and maps cross-connections to the active S79 workshops P4-A / P4-C / P4-D.

### Substrate-first framing
The fabric is D_K on Jensen-deformed SU(3). "Phononic length" is not a propagation distance. It is a **geometric invariant of D_K** — the inverse wavenumber at which the low-momentum Goldstone branch ceases to be a coherent phonon and Landau-damps into pair-breaking continuum. It is a spectral property of the fabric, not a distance traveled by anything.

---

## Section 1 — Current State Map

### 1a. Length-scale ledger (PHONONIC candidates)

Units M_KK^{-1}; physical conversion l_KK = hbar*c / M_KK with M_KK = 7.4287e16 GeV gives l_KK = 2.6563e-33 m (verified S79, Python).

| # | Name | Value (M_KK^{-1}) | Physical (m) | Origin | Canonical entry | Provenance status |
|:--|:-----|:-----------------:|:------------:|:-------|:----------------|:-------------------|
| L1 | l_KK (fiber Compton) | 1.000 | 2.6563e-33 | hbar*c / M_KK | implicit via M_KK | OK (fundamental) |
| L2 | xi_BCS (BCS coherence) | 0.808347 | 2.1472e-33 | S37 BCS gap | `canonical_constants.py:192` | CANONICAL |
| L3 | xi_GL (GL coherence) | 0.976321 | 2.5934e-33 | S37 GL functional | `canonical_constants.py:193` | CANONICAL |
| L4 | lambda_Bragg/2 (tau-space) | pi/2 | n/a (tau-dimensional) | `s22a_delta_T_profile.py` | none | Topical only (NOT a physical length) |
| L5 | **l_phonon (proposed)** | **5.4054 = 1/K*** | **1.4358e-32 m** | GL-JOSEPHSON-52 Goldstone-to-continuum crossover | **MISSING** | **PRU omission** |

Verified arithmetic (Python, S79):
- l_phonon = 1 / K* = 1 / 0.185 = 5.4054 M_KK^{-1}
- l_phonon(physical) = 5.4054 * 2.6563e-33 m = 1.4358e-32 m
- l_phonon / l_KK = 5.4054 (l_phonon is longer than the fiber by factor ~5.4)
- l_phonon / xi_BCS = 6.687 (Goldstone wavelength spans ~7 BCS coherence lengths before damping)

### 1b. Substrate-c ledger (SPEEDS)

Two categorical objects. Category (i) is fabric dynamics; category (ii) is propagation on the emergent 4-metric g_M. These are not on the same scale.

**Category 2a — Fabric dynamics (NOT c-bounded)**

| Name | Value (M_KK units) | Provenance | Canonical entry | Status |
|:-----|:------------------:|:-----------|:----------------|:-------|
| c_fabric | 209.97368021 | `computations/s42_gradient_stiffness.py:1017-1020` (S42) | `canonical_constants.py:250` | CANONICAL |

Derivation (for audit trail): c_fabric = sqrt(Z_fold / M_ATDHFB) = sqrt(74730.76 / 1.695) = sqrt(44088.36) = 210.0 M_KK (verified via the two canonical entries Z_fold = 74730.76411846, M_ATDHFB = 1.695 at `canonical_constants.py:246, 245`). Substrate-framing: this is the propagation speed of spectral deformations of the modulus tau itself — it is how fast the fabric reorganizes its own internal description, not a signal speed on g_M. By the film analogy (`project_substrate-not-c-limited.md`), c_fabric is the editing speed of the film; c is the frame rate of what plays on it.

**Category 2b — Phononic acoustic speeds on emergent g_M (c-bounded by construction)**

| Name | Value | Provenance | Canonical entry | Status |
|:-----|:-----:|:-----------|:----------------|:-------|
| c_Gold | 0.915 | S52 W1-F GL-JOSEPHSON-52; `s52_gl_josephson.npz` | `canonical_constants.py:307` | Entry exists, NO session/source/gate provenance in MCP |
| c_BLV | 0.485 | `sessions/archive/session-67/session-67-transit-phonon-first-workshop.md:93-110` (BLV scalar-mode transit) | **MISSING** | PRU omission |
| c_BA | 0.399 | `computations/s56_cba_sound.py` (S59); re-derived `s63_sound_speed.py`, `s64_sound_speed.py` | **MISSING** | PRU omission |
| c_L | 0.025 | Leggett phase mode; agent memory S59+, `s70_leggett_*.py` | **MISSING** | PRU omission |
| c_mod | 1.000 | Emergent photon on g_M = c_light by construction; memory S75+ | **MISSING** | PRU omission |

Verified arithmetic (Python, S79) — substitution chain for the c_fabric/c_Gold ratio:
- Step 1: definition — c_fabric = 209.97368021 M_KK (from `canonical_constants.py:250`); c_Gold = 0.915 M_KK (from `canonical_constants.py:307`).
- Step 2: substitute — ratio = c_fabric / c_Gold = 209.97368021 / 0.915.
- Step 3: simplify — ratio = 229.4794.
- Step 4: inverse — c_Gold / c_fabric = 1 / 229.4794 = 0.004358; the canonical entry `c_Gold_over_c_fabric = 0.00436` at line 308 matches to 3 sig figs.
- Direction read-off: c_fabric > c_Gold by factor 229.48 (fabric dynamics is 2.3 orders of magnitude faster than the fastest phononic signal on g_M).

**Ordering (all on emergent g_M, units of c_light):** c_L = 0.025 < c_BA = 0.399 < c_BLV = 0.485 < c_Gold = 0.915 < c_mod = 1.000. All < 1 on g_M as required by construction (emergent photon saturates the bound). c_fabric = 229.48 × c_Gold lives in the orthogonal fabric-dynamics category and is NOT on this ordering.

### 1c. Canonical vs PRU omission summary

- **IS canonical**: xi_BCS, xi_GL, c_fabric, c_Gold (value only, provenance incomplete).
- **SHOULD BE canonical but isn't**: l_phonon, c_BLV, c_BA, c_L, c_mod. Five entries with session-level authority but no canonical home — each has appeared in 3+ scripts or synthesis documents yet is rediscovered case-by-case.
- **Zero matches** for any of `l_phonon | phonon_length | lambda_phonon | c_BLV | c_BA | c_L` in `canonical_constants.py` (verified S79 Grep).

---

## Section 2 — Substrate Framing Doctrine

### 2a. "Phononic length" is a geometric invariant of D_K

The framing trap agents default into: "phononic length = distance a phonon travels in one coherence time." This is backwards.

In the substrate picture:
- D_K eigenvalues define the Goldstone branch dispersion omega_G(K) at small K.
- Above K* the dispersion bends into pair-breaking continuum and the mode is no longer a coherent phonon — Landau damping.
- l_phonon = 1/K* is the **longest wavelength at which the fabric can sustain phonon-like excitations**. It is a boundary in spectral phase space, not a distance.

Formally: l_phonon ∈ spec(D_K) as a derived quantity of the low-lying eigenvalue structure. It is the inverse of the wavenumber K* at which im(omega_G(K)) starts to exceed re(omega_G(K)) (decoherence onset). This is **geometric** — it's determined by the fiber's spectral structure before any phonon exists. Nothing propagates to define it.

Correspondingly, xi_BCS = 0.808 M_KK^{-1} is the length over which pair correlations decohere — also a spectral invariant, not a traveled distance. The two lengths classify DIFFERENT spectral regimes:
- xi_BCS: pair correlation scale (fermion-pair level, set by Delta_BCS).
- l_phonon: Goldstone-mode coherence scale (collective level, set by K*).
- l_KK: fiber Compton scale (single-eigenvalue spacing, set by M_KK).

All three are "phononic" only in the sense that they are properties of the fabric's mode spectrum. None is a propagation distance.

### 2b. Why c_fabric > c_Gold does not violate relativity

The c_fabric / c_Gold = 229.48 ratio is a frequent trigger for the "but this violates c!" reaction. It does not.

From `project_substrate-not-c-limited.md` (2026-04-11):
- c is the speed limit for propagation ACROSS the substrate — things moving through the emergent metric g_M.
- c is NOT a limit on the substrate's own dynamics: fold transit, instanton events, Jensen deformation evolution, spectral reorganization.

c_fabric is a spectral-deformation rate — how fast the modulus tau can reorganize the fiber's internal description. It is not a signal propagation. By the user's film analogy: c is the frame rate at which the movie plays; the substrate is the film itself. Editing the film (splicing, reorganizing, running a transit) is not bound by frame rate.

The substitution chain that makes this precise:
- Step 1: c_fabric^2 = Z_fold / M_ATDHFB (definition, S42 gradient-stiffness derivation).
- Step 2: Z_fold has units [action / moduli-space-metric] = [energy × (dtau)^{-2}]; M_ATDHFB has units [energy × time^2 / (dtau)^2] by ATDHFB construction.
- Step 3: c_fabric^2 has units [1/time^2] — it IS a rate, but a rate of spectral-variable change, not a rate of position change.
- Step 4: Because tau is not a spatial coordinate on g_M (it's a modulus of the fiber), no "thing" is moving at c_fabric. Nothing propagates. There is no signal to superluminally race a photon.
- Direction read-off: c_fabric is a fabric-internal reorganization rate; no relativistic constraint applies.

c_Gold, c_BLV, c_BA, c_L, c_mod all live on g_M and ARE bounded by c by construction (emergent c_mod = c_light saturates the bound). They are propagation modes. The ordering at §1b is physical.

### 2c. Why l_phonon is a length and not a distance

l_phonon shows up in length units (M_KK^{-1}, or meters after conversion) but it is not a distance between two points. It is a cut-off in K-space promoted to length-space by inversion. This is the same species of "length" as the de Broglie wavelength of a bound state: a spectral property expressed in units of length, not a separation in a coordinate chart.

Consequence: questions like "what is between point A at distance l_phonon and point A at distance 2*l_phonon?" are not well-formed. l_phonon classifies a regime in the spectrum, not a location in space. This is the same mistake as asking where a Brillouin zone "is."

---

## Section 3 — PRU Diagnosis

Applying the Class-8 PRU definition from `sessions/archive/session-79/workshops/p1-3-w1b-iteration-audit.md:668`:

> "Class 8: Pre-Registration Underspecification (PRU). A gate's plan leaves one or more pieces of gate-relevant machinery unpinned, such that execution-time machinery choices are not authorized by the plan."

The length/speed ledger exhibits the exact pathology at the `canonical_constants.py` level rather than at a gate level. Five entries with de-facto authority (they appear in 3+ scripts or registry entries) have no canonical home — each consumer script rediscovers or hardcodes them. This is the infrastructure-level analog of gate PRU: the canonical-constants module is the machinery enumeration, and it has gaps.

### Named PRU omissions (S79 audit)

| # | Omitted constant | Appearances outside canonical | Severity |
|:--|:-----------------|:------------------------------|:---------|
| P1 | **l_phonon** | 0 explicit, but K* = 0.185 appears in s52 outputs and 6 synthesis docs | NEW (never canonicalized) |
| P2 | **c_BLV** | `permanent-results-registry.md:469, 856`; `session-67-transit-phonon-first-workshop.md:93-110`; 7+ sessions | HIGH — load-bearing for BLV transit gates |
| P3 | **c_BA** | `s56_cba_sound.py`, `s63_sound_speed.py`, `s64_sound_speed.py`; 4+ sessions | HIGH — Bogoliubov-Anderson derivations |
| P4 | **c_L** | `s70_leggett_*.py`; agent memory S59, S66, S68; S70 Hawking workshop | HIGH — load-bearing for Leggett decay / DM |
| P5 | **c_mod** | Memory S75+; substrate-framing derivations | MEDIUM (bound is by-construction, value trivial) |

### Provenance scatter for existing entries

- **c_fabric (line 250)**: has derivation comment "(S42 s42_gradient_stiffness)" in-line. Adequate.
- **c_Gold (line 307)**: has in-line comment "(M_KK units)" but `mcp__knowledge__get_constant("c_Gold")` returns **no session/source/gate provenance** per QA's audit (§3 bullet 3). This is a provenance repair, not a value repair.
- **c_Gold_over_c_fabric (line 308)**: has an extensive provenance comment ("R-PROTECTED — 229x hierarchy; eigenvalue gradient ratio, bypasses Seeley-DeWitt expansion. STRUCTURAL, drift 0.00% (S74 W4-F #20)"). Gold standard for what other entries should look like.
- **xi_BCS, xi_GL (lines 192-193)**: have in-line attribution "(s37_instanton_mc, high precision)" — adequate but not MCP-level.

### Why PRU matters here

The PRU remediation prescription from `p1-3:927` is:
> "Every gate's §W-X block must include a structured subsection `Enumerated free parameters: [p_1 = v_1, p_2 = v_2, ...]` where each p_i is a free parameter identified by dry-running the script."

Transposed to the infrastructure level: every quantity that appears as a numerical literal in 3+ computation scripts is a de-facto framework constant, and MUST be enumerated in `canonical_constants.py` with (session, source-script, gate-ID, drift-status) provenance. The five omissions above violate this at the infrastructure layer.

---

## Section 4 — S80 "Phononic Length Canonicalization" Wave Pre-Registration

Four gates. Each tagged with its compliance requirement.

### [AUDIT] S80-PHONON-LENGTH-CANONICALIZATION

**Hypothesis**: The five PRU-omitted constants (l_phonon, c_BLV, c_BA, c_L, c_mod) can be canonicalized with full (session, source-script, gate-ID, drift-status) provenance without re-derivation — they already have originating computations in computation and need only transplanting.

**Action**: Add to `canonical_constants.py` Section E2 (Phonon & Structural Results) the following entries, each with a provenance comment matching the c_Gold_over_c_fabric gold-standard format:

```python
l_phonon = 1.0 / K_star_goldstone    # Phononic length = 5.4054 M_KK^-1 = 1.4358e-32 m
                                      # Goldstone-to-continuum crossover (GL-JOSEPHSON-52 PASS,
                                      # s52_gl_josephson.npz, K_star_goldstone = 0.185 M_KK)
c_BLV = 0.485                         # BLV scalar-mode transit speed (permanent-results-registry S62+,
                                      # s67_transit.py; session-67-transit-phonon-first-workshop.md:93-110)
c_BA = 0.399                          # Bogoliubov-Anderson sound speed at fold (s56_cba_sound.py S59,
                                      # re-derived s63/s64_sound_speed.py; used in transit dynamics)
c_L = 0.025                           # Leggett phase-mode speed (s70_leggett_*.py, agent memory S66/S68;
                                      # R-protected per LEGGETT-PARTITION-57/58)
c_mod = 1.000                         # Emergent photon on g_M (construction; c_light by definition,
                                      # memory S75+; substrate-not-c-limited doctrine)
K_star_goldstone = 0.185              # Goldstone-continuum crossover wavenumber (M_KK units;
                                      # GL-JOSEPHSON-52, s52_gl_josephson.npz)
```

Pass/fail criterion: all five entries land in `canonical_constants.py` with inline provenance referencing (a) originating session, (b) originating script or workshop document, (c) governing gate ID, (d) drift status where known. `/weave --update` canonical-constants audit reports **Potential = 0** after the update.

**Verdict rule**: PASS if 5/5 entries transplanted with complete provenance and audit clean; FAIL if any entry remains PRU-compliant.

### [VERIFY] S80-L-PHONON-DERIVATION

**Hypothesis**: The Goldstone-to-continuum crossover K* = 0.185 M_KK is reproducible from the S52 artifact `s52_gl_josephson.npz` by re-running the dispersion analysis (locate K at which im(omega_G) first exceeds re(omega_G) / 10).

**Protocol**:
1. Write `computations/s80_phononic_length.py` that loads `s52_gl_josephson.npz`, extracts the omega_G(K) branch, and computes K* by the Landau-damping-onset criterion (im(omega_G(K*)) / re(omega_G(K*)) = 0.1, the conventional decoherence threshold).
2. Compute l_phonon = 1/K* in M_KK^{-1} and in physical meters.
3. Pre-register band: 0.175 <= K* <= 0.195 (QA-reported 0.185 M_KK ± 0.01 = ±5%).

**Pass/fail criterion**:
- PASS: K* ∈ [0.175, 0.195] M_KK, and l_phonon ∈ [5.13, 5.71] M_KK^{-1}.
- FAIL: K* outside this band (indicates the QA report value is not reproducible, forcing either value update or classification downgrade).
- INCOMPUTABLE: s52_gl_josephson.npz does not contain the data required to extract omega_G(K) with imaginary part (requires re-run of GL-JOSEPHSON-52 with extended diagnostics).

### [VERIFY] S80-FOUR-SPEED-PROVENANCE-PIN

**Hypothesis**: Each of c_BLV, c_BA, c_L is reproducible from its originating script to at least 3 significant figures. Reproducibility confirms canonical transplant is safe.

**Protocol**: Re-run the three originating scripts (or their nearest extant analogs):
- c_BLV: re-derive from `session-67-transit-phonon-first-workshop.md` dispersion; if no live script, write a minimal re-derivation from the S67 transit Hamiltonian.
- c_BA: re-run `computations/s56_cba_sound.py` if exists, else nearest sibling in s63/s64.
- c_L: re-run the Leggett dispersion from `s70_leggett_*.py` or nearest extant.

Record each as a 4-tuple tag: (canonical_value, reproduced_value, source_script_SHA, session_ID).

**Pass/fail criterion**:
- PASS: all three reproduced values within 0.5% of canonical value; 4-tuple tags recorded.
- FAIL: any value drift exceeds 0.5% (forces canonicalization at the drifted value, with drift noted).
- INCOMPUTABLE: any originating script missing or uncallable without major refactor (triggers S80 re-derivation sub-task).

### [AUDIT] S80-C-GOLD-PROVENANCE-REPAIR

**Hypothesis**: The `c_Gold` entry in the knowledge MCP currently returns no session/source/gate metadata (per QA §3 bullet 3). Repairing this to the c_Gold_over_c_fabric standard is a mechanical update.

**Protocol**:
1. `mcp__knowledge__update_constant("c_Gold", 0.915, "S52", "s52_gl_josephson.npz / GL-JOSEPHSON-52", "S52 W1-F Goldstone phonon; R-protected partner of c_fabric at 229x hierarchy")`.
2. Confirm via `mcp__knowledge__get_constant("c_Gold")` that session, source, and gate metadata are now present.

**Pass/fail criterion**: PASS if the MCP returns complete metadata; FAIL if any of session/source/gate field remains blank after the update.

### [VERIFY] S80-XI-BCS-VS-L-PHONON-CLASSIFICATION

**Hypothesis**: xi_BCS (0.808 M_KK^{-1}) and l_phonon (5.405 M_KK^{-1}) classify different physical regimes — specifically, xi_BCS is the pair-correlation scale and l_phonon is the Goldstone-continuum crossover. They are NOT the same length under different names.

**Protocol**:
1. Derive xi_BCS from Delta_BCS and the BCS gap equation: xi_BCS = hbar * v_F / (pi * Delta_BCS), at the fold value.
2. Derive l_phonon from the Goldstone branch of s52_gl_josephson.npz.
3. Test whether they scale coherently or independently under tau-variation (tau in [0.15, 0.25] around tau_fold = 0.190).

**Pass/fail criterion**:
- PASS: the two lengths have distinct tau-dependence (e.g., xi_BCS scales as 1/Delta_BCS(tau), l_phonon scales as 1/K*(tau) with different functional form); correlation coefficient |r| < 0.9 over the tau-window.
- FAIL: the two lengths are proportional in tau (|r| > 0.9), indicating they are the same physical scale expressed in two derivations. This would collapse one onto the other and simplify the canonical ledger.
- INCOMPUTABLE: tau-swept dispersion data unavailable (triggers additional tau-scan in S80 Wave 2).

---

## Section 5 — Cross-Connections to S79 Workshops

### 5a. P4-D (ratios vs absolutes meta-pattern)

Question for S80: **is l_phonon an absolute or a ratio?**

Substitution chain:
- Step 1: definition — l_phonon = 1/K* where K* is a wavenumber with units M_KK.
- Step 2: substitute — l_phonon = 1/K* with K* = k_star [dimensionless] × M_KK.
- Step 3: simplify — l_phonon = (1/k_star) × M_KK^{-1}.
- Step 4: physical length — l_phonon(m) = (1/k_star) × (hbar c / M_KK).
- Direction read-off: l_phonon = (1/k_star) × l_KK. The quantity (1/k_star) is dimensionless. l_phonon is therefore a dimensionless ratio l_phonon/l_KK = 1/k_star = 5.4054 multiplied by the fundamental scale l_KK.

**P4-D classification**: l_phonon is an **absolute** because its physical-meter value depends on the fundamental scale M_KK, which is not itself a dimensionless ratio. Only the ratio l_phonon/l_KK = 5.4054 is a pure framework observable (dimensionless, R-class candidate).

Carry-forward for S80: add `l_phonon_over_l_KK = 5.4054` as a candidate R-protected ratio. Check whether 1/K* is preserved under Seeley-DeWitt expansion rank (as c_Gold/c_fabric = 0.00436 is, per S74 W4-F #20). If yes, it joins the small family of structurally protected dimensionless observables.

### 5b. P4-C (sibling class: a_0 vs a_2)

Question for S80: **does l_phonon derive from an a_0 or an a_2 slot?**

The dispersion omega_G(K) at small K is controlled by the quadratic-in-K term in the collective-mode expansion of the spectral action. This is an a_2-slot quantity (the a_2 Seeley-DeWitt coefficient generates gradient terms in the effective action).

Substitution chain:
- Step 1: definition — a_2 coefficient contains terms proportional to K^2 in the effective Lagrangian for collective modes.
- Step 2: substitute — the Goldstone kinetic term has coefficient ∝ a_2; the pair-breaking onset is governed by eigenvalue spacing ∝ M_KK.
- Step 3: simplify — K* where kinetic ~ pair-breaking threshold: (a_2 contribution) × K*^2 ~ Delta_BCS. Thus K*^2 ∝ Delta_BCS / a_2 contribution.
- Step 4: direction read-off — K* (and hence l_phonon) is an **a_2-slot** quantity, same sibling class as c_Gold, c_BLV, c_BA, and xi_BCS.

**Classification**: l_phonon joins the a_2 sibling class. This is consistent with the substrate picture — all phononic velocities and coherence lengths are a_2 quantities because they are dynamical (K^2, R, omega^2 terms). a_0 quantities are static (volumes, CC, Higgs potential extrema).

Carry-forward for S80: confirm via Seeley-DeWitt heat-kernel expansion that dl_phonon/dLambda vanishes at same order as dc_Gold/dLambda (both are a_2 ratios-of-moments and should regulator-cancel). If confirmed, l_phonon joins the R-protected family; if not, it is regulator-dependent and classifies as a "soft" phononic observable.

### 5c. P4-A (rank-universality)

Question for S80: **SU(3) has 8 generators → how many phonon branches, and do they scale with rank(G)?**

SU(3): rank 2, 8 generators, 6 coset directions (8 - 2 stabilizer-U(1)^2) for the broken U(1)_7 Goldstone, plus additional branches from the Jensen deformation's Z_3 structure.

Branch count in current canonical ledger: c_Gold (1), c_BLV (1), c_BA (1), c_L (1, Leggett relative phase), c_mod (1, emergent photon). Five branches — NOT 8, NOT 6. The gap between branches-counted-as-speeds and generators-counted-as-directions is a concrete rank-universality question.

Carry-forward for S80: enumerate all modes of the GL-Josephson Lagrangian on SU(3)/(U(1))^2 quotient. If rank-universality holds, the expected count at SU(N) should be (N^2 - 1) - 2*(N-1) Goldstones plus (N-1) moduli modes plus 1 photon, yielding a specific N-scaling. For SU(3): 8 - 4 + 2 + 1 = 7, off-by-2 from the currently identified 5. This discrepancy should be resolved BEFORE the canonical transplant (so the S80 canonical entries are not built on a miscounted branch list).

Recommended pre-audit: QA to enumerate all dispersing modes in `s52_gl_josephson.npz` and confirm the 5-branch count before S80-PHONON-LENGTH-CANONICALIZATION freezes values. If hidden branches (e.g., transverse Higgs partners) emerge, add them with provenance.

---

## Section 6 — Next-Session Dispatch (S80 Wave 1)

Two action items in 7-component format, plus one blocking prerequisite.

### Prerequisite (must run before Item 1)

**PREREQ-1: `/weave --update` on current state.**
- WHAT: run `/weave --update` to baseline the current canonical-constants audit state.
- WHO: orchestrator.
- INPUT: current `computations/canonical_constants.py`.
- OUTPUT: current Violations and Potential counts, for diff against post-S80.
- FORMAT: `/weave --update` command output logged to `sessions/archive/session-80/weave-baseline.txt`.
- DEADLINE: S80 Wave 1, before Item 1 dispatch.
- DEPENDS ON: nothing.

### Action Item 1 — Phononic-length canonicalization

- **WHAT**: `computations/s80_phononic_length.py` script that extracts K* from s52 data, computes l_phonon, and emits the canonical-constants additions as an update patch. Plus direct MCP updates for c_Gold / c_BLV / c_BA / c_L / c_mod provenance.
- **WHO**: quantum-acoustics-theorist (primary, owns s52 artifact), lizzi-spectral-functional-theorist (secondary, verifies a_2-slot classification and R-protection via Mellin-weight argument).
- **INPUT**:
  - `computations/canonical_constants.py` current state (post-PREREQ-1 baseline).
  - `s52_gl_josephson.npz` (omega_G(K) branch).
  - Originating scripts for c_BLV, c_BA, c_L (S80-FOUR-SPEED-PROVENANCE-PIN).
  - PRU diagnosis (this synthesis, §3).
- **OUTPUT**:
  - Five new canonical entries (l_phonon, c_BLV, c_BA, c_L, c_mod) + K_star_goldstone.
  - Provenance repair for c_Gold in MCP.
  - One-paragraph framework-status note for `summary/` documenting the canonicalization.
  - Verdicts for gates S80-PHONON-LENGTH-CANONICALIZATION, S80-L-PHONON-DERIVATION, S80-FOUR-SPEED-PROVENANCE-PIN, S80-C-GOLD-PROVENANCE-REPAIR, S80-XI-BCS-VS-L-PHONON-CLASSIFICATION.
- **FORMAT**: Python script at `computations/s80_phononic_length.py`; canonical constants update via `update_constant` MCP calls AND direct edits to `canonical_constants.py` Section E2; framework-status paragraph at `summary/s80-phonon-canonicalization-note.md`.
- **DEADLINE**: S80 Wave 1.
- **DEPENDS ON**: PREREQ-1 (weave baseline) complete; P4-A branch-enumeration pre-audit (§5c) complete or explicitly deferred.

### Action Item 2 — Rank-universality branch-count pre-audit

- **WHAT**: enumerate all dispersing collective modes in `s52_gl_josephson.npz` — acoustic, Leggett, Higgs, quantum-metric, CP-diagonal — and confirm the 5-speed canonical list is complete. Flag any hidden branch for addition.
- **WHO**: quantum-acoustics-theorist (solo — this is s52-internal).
- **INPUT**: `s52_gl_josephson.npz`, `session-52-phonon-workshop.md:86-135` (omega table), P4-A workshop state.
- **OUTPUT**: branch-count tally with (name, rest-frequency, sound-speed-if-dispersing, canonical-entry-status) per branch.
- **FORMAT**: `sessions/archive/session-80/s80-branch-count.md` + short response summary.
- **DEADLINE**: S80 Wave 1, BEFORE Item 1 execution.
- **DEPENDS ON**: nothing.

### Out-of-band note (not an action item, but record it)

The proposed l_phonon = 1/K* definition is TENTATIVE. If S80-L-PHONON-DERIVATION reveals the Landau-damping-onset criterion is sensitive to the 0.1 threshold choice (e.g., 0.05 gives K* = 0.12, 0.2 gives K* = 0.25), then l_phonon inherits that threshold as a PRU-risk and must be pinned in-line. Alternative definitions to test if the dispersion criterion drifts: (a) K at which group velocity vanishes (turning point), (b) K at which the Goldstone branch first intersects the pair-breaking gap, (c) K at which phase coherence time equals inverse temperature. Each gives a different numerical l_phonon and constitutes a distinct physical scale.

---

## Section 7 — Closing Line

The phononic-length question has been sitting as an implicit Class-8 PRU across 27+ sessions — five canonical entries with de-facto authority, zero canonical homes. The substrate doctrine resolves the framing trap cleanly: l_phonon is a geometric invariant of D_K, not a distance; c_fabric > c_Gold by 229× is a fabric-dynamics fact, not a relativity violation. S80 Wave 1 closes the PRU omission with four pre-registered gates and delivers a clean canonicalized ledger for the velocity hierarchy on g_M and the length hierarchy in the fiber spectrum.

PHONON_FIRST_LENGTH_SYNTHESIS_COMPLETE
