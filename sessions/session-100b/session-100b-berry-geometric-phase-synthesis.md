# Session 100b Synthesis: Band-Selective Schur Rigidity — Stage-0 Theorem Candidate, Honest FAIL(a) Scope, and the Two-Differential Declaration

**Date**: 2026-06-07
**Agent**: berry-geometric-phase-theorist (Berry)
**Source Documents**:
- `sessions/session-100b/session-100b-w6-workingpaper.md` (§W6-1, §W6-2, §W6-3 + Wave 6 Synthesis; W6-2 witnesses e1–e3, d1–d4, CC-1–CC-3)
- `sessions/session-plan/session-100b-plan-w6.md` (§W6-2 pre-registration: operator clauses, FAIL-arm discrimination, dual priors, machinery pins, substitution chain)
- `.claude/agent-memory/berry-geometric-phase-theorist/MEMORY.md` + `s100b-band-selective-rigidity.md` (agent memory)
- Verified on disk: `computations/session-100b/s100b_gate_verdicts.txt` lines 92–98 (canonical W6-2 line + dual-SHA companion + schema-v2 3-tuple + UNTRUSTED-UPSTREAM extra-row at line 95 + gauge-pin + anatomy rows); `sessions/session-100b/session-100b-housekeeping.md` §A19 (dispatch-with-caveat triage, trigger audit `bea5401ae1ac3c4d`)

Gate verdicts cited here are authoritative as emitted; nothing in this synthesis re-adjudicates them. The W6-2 record is `S100b-NONABELIAN-METRIC-FRACTION: FAIL [FAIL-a-JPH-protected-B2-carries-CKH]`, schema-v2 3-tuple `sign=PASS / magnitude=FAIL / regime=VALID`, `audit_sha256=4a03497c43a97335144bad80f60e16d00097829ca4310f25315dfe4c9c926818`.

---

## I. Session Outcome

Wave 6 hardened the §VII.AF.1.OP-PROJ bridge on both of its structural axes and, in doing so, produced this wave's deepest single result as the *informative arm of a FAIL*: on the U(2)-invariant (τ,μ) TT moduli surface, the (0,0)-block D_K eigenbundle is **band-selectively rigid** — the B1 pair and B3 triplets are frozen isotypic slots (max ‖ΔP‖_F ~ 1e-14, base-direction QGT ≡ 0), the B2 quadruplets are the sole moving carrier (‖ΔP‖_F = 0.228, defect-excluded I_NA(B2) = 2.59e-2), and the B2 invariant band-matrix is Schur-scalar (∝ 1₄ to ~1e-13) — so Abelian-vs-non-Abelian band structure is **symmetry-undecidable on any U(2)-invariant base** (W6-2 FAIL, reading (a), audit `4a03497c…`). This synthesis formalizes that no-go as a Stage-0-ready theorem candidate (§II.2), scopes the FAIL(a) record honestly (what is certified vs what remains undecidable, §II.3), writes down the Level-1/Level-2 two-differential declaration that reconciles W6-1's *nonzero* algebra-direction pairing with W6-2's *frozen* base-direction QGT on the *same* B1 pair (§II.4), and hands the S101 isotropy-breaking gate its dual-prior and threshold rationale (§V.1). W6-1 (PASS, Δ_disc = 0.341976 = 342× floor) and W6-3 (PASS, class-(iii) χ-transportable decay channels empty) are carried as context.

---

## II. Key Results

### II.1 The geometric picture first

**Classification: GEOMETRIC.**

The substrate IS the D_K eigenbundle over its own modulus space. The base is the 2-parameter Ad-U(2)-invariant volume-preserving TT surface in log-metric coordinates, l(τ,μ) = τ·v_J + (μ/|v_μ|)·v_μ with v_J = (2,−2,1), v_μ = (11,7,−8), |v_μ|² = 234, both orthogonal to the volume normal n = (1,3,4) and to each other (S96 pins; μ = 0 IS the Jensen line; the fold τ_fold = 0.19 is enclosed). The fiber is the 16-dimensional (0,0) Peter-Weyl singlet spinor block of D_K — exact at every L_max by block-diagonality (S22b, PROVEN for any left-invariant metric). Its signed spectrum at every node is particle-hole/chiral symmetric with the layout

```
[ −B3 ×3 | −B2 ×4 | −B1 | +B1 | +B2 ×4 | +B3 ×3 ]        (PH pairing witness max|λ₇+λ₈| = 2.4e-15)
```

Eigenvalues are quoted in M_KK units; the base coordinates (τ,μ) are dimensionless log-metric coordinates, so every QGT component, metric trace, and integrated quantity below is dimensionless.

The geometry of this fiber bundle is decided by symmetry before any number is computed: the deformation family commutes with a *fixed* unitary representation of the U(2) isotropy at every base point. Schur's lemma then partitions the bands into (i) multiplicity-locked slots whose eigenbundles cannot rotate at all (frozen — zero connection, zero metric, zero curvature along the base) and (ii) moving slots whose only invariant band-geometry datum is a scalar. Everything W6-2 measured is the numerical shadow of this partition. The theorem below states it once, precisely, so no future quantum-geometry gate on a symmetric base has to rediscover it.

### II.2 Stage-0-Ready Theorem Candidate — Band-Selective Schur Rigidity and Symmetry-Undecidability of Band Geometry

**Result**: theorem-candidate text, Stage-0-ready per `joint-theorem-promotion.md` §Stage 0. **Classification: GEOMETRIC.**

> **Stage-0 authorship and Stage-2 exclusion (stated up front, per the S99 E1 lesson).** This section constitutes Stage-0 authorship of the candidate by `berry-geometric-phase-theorist`. Per `joint-theorem-promotion.md` §Stage 2 (cross-reviewers must NOT be the original authoring agents, with downstream-inheritance reach extending to successor spawns whose memory inherits the reading path) and the S99 E1 Stage-0-authorship reviewer-exclusion hardening, **berry-geometric-phase-theorist is EXCLUDED from any later Stage-2 cross-review of this candidate** — including future berry spawns, whose agent memory (`s100b-band-selective-rigidity.md`) already inherits this workshop's reading path and therefore fires the downstream-inheritance test. Stage-2 reviewer selection is the future orchestrator's task under the Axis-B Selection Protocol; the structural constraint pinned here is only the exclusion.

---

#### Candidate statement (frozen text for Stage-1 registration at S101)

**Title**: *Band-Selective Schur Rigidity and the Symmetry-Undecidability of Abelian-vs-Non-Abelian Band Geometry on G-Invariant Deformation Families.*

**Setting and definitions.**

Let V be a finite-dimensional complex Hilbert space (the fiber), G a compact group, and ρ : G → U(V) a **fixed** (base-independent) unitary representation. Decompose V into isotypic components,

$$V \;=\; \bigoplus_\alpha V_\alpha \otimes \mathbb{C}^{m_\alpha}, \qquad E_\alpha := d_\alpha \int_G \overline{\chi_\alpha(g)}\,\rho(g)\,dg \quad \text{(isotypic projector; } b\text{-independent)}, \tag{E1}$$

where V_α runs over the distinct irreducibles appearing, m_α their multiplicities, and E_α is fixed by ρ alone. Let B be a smooth connected manifold (the moduli base) and b ↦ H(b) a smooth family of Hermitian operators on V. For an isolated band with spectral projector P(b) of constant rank, define the band quantum-geometric tensor (QGT) along base directions a, b ∈ T_bB through the **gauge-free projector form**

$$Q_{ab}(b) \;=\; \mathrm{Tr}\!\left[(\partial_a P)(1-P)(\partial_b P)\right], \qquad M_{ab}(b) \;=\; P\,(\partial_a P)(1-P)(\partial_b P)\,P \quad \text{(band-matrix)}. \tag{E2}$$

**Hypotheses.**

- **(H1) Fixed fiber representation.** ρ is independent of b ∈ B. *(Substrate realization: V = ℂ¹⁶, the (0,0) Peter-Weyl singlet spinor fiber of D_K; G = U(2) ⊂ SU(3) the isotropy group with its spin-lift ρ; fiber fixed because the Peter-Weyl block structure is metric-independent — S22b block-diagonality, PROVEN, cited as input.)*
- **(H2) G-invariant deformation family.** [ρ(g), H(b)] = 0 for all g ∈ G and all b ∈ B. *(Realization: H(τ,μ) = D_K(τ,μ)|₍₀,₀₎ on the U(2)-invariant volume-preserving TT surface.)*
- **(H3) Band α-purity at the evaluation point.** The band's eigenspace lies inside a single isotypic component. Generic on B; it fails only at symmetry-allowed crossings between *different* isotypic characters (von Neumann–Wigner: no level repulsion between distinct symmetry types), which are excluded from the theorem's domain and handled operationally by the defect-exclusion discipline. *(Realization: the B1/B2 crossing clipping the (0.10, +0.10) window corner is exactly such a point.)*
- **(H4) (for T2) Irreducible moving slot.** The band corresponds to a simple eigenvalue ν(b) of the reduced m_α × m_α block h_α(b), so the band spans 1_{V_α} ⊗ w(b), dim = d_α, with m_α ≥ 2.
- **(H5) (for sub-lemma P) Chirality pairing.** A constant Hermitian unitary γ with {γ, H(b)} = 0 for all b, pairing two multiplicity-one slots u₋ ↦ u₊. *(Realization: γ₉, the normalized Cl(8) gamma product; measured max|{H, γ₉}| = 0.0 exactly, |⟨u₊|γ₉|u₋⟩| = 1.000000000.)*
- **(H6) (for sub-lemma P) Reality structure.** A b-independent antiunitary reality structure making H(b) real-symmetric in a fixed basis, with eigenvectors of simple (within-slot) eigenvalues real. *(Realization: the substrate J / Kosmann-reality mechanism class of the S25 Ω = 0 theorem; compatibility with γ₉ is confirmed empirically by the witnesses below.)*

**Lemma L0 (gauge-free band QGT; evaluator identity).** For any smooth rank-r projector family P(b) with orthonormal band frame {u_n(b)},

$$\sum_{n \in \mathrm{band}} \langle \partial_a u_n |(1-P)| \partial_b u_n \rangle \;=\; \mathrm{Tr}\!\left[(\partial_a P)(1-P)(\partial_b P)\right]. \tag{E3}$$

*Proof.* P = Σₙ|uₙ⟩⟨uₙ| ⇒ ∂ₐP = Σₙ(|∂ₐuₙ⟩⟨uₙ| + |uₙ⟩⟨∂ₐuₙ|). Right-multiplying by (1−P) kills the first sum's right factor ⟨uₙ|(1−P) = 0, so (∂ₐP)(1−P) = Σₙ|uₙ⟩⟨∂ₐuₙ|(1−P); symmetrically (1−P)(∂_bP) = Σₘ(1−P)|∂_buₘ⟩⟨uₘ|. Multiply and trace; orthonormality collapses the double sum to the diagonal. ∎ The right side involves only P: basis-free, phase-free. *(This is the script-header LEMMA of `s100b_nonabelian_metric_fraction.py`, verdict-file gauge-pin row; it is what makes every PASS-clause quantity immune to the π-jumps of the largest-component phase pin.)*

**Theorem part T1 (multiplicity-locked slots are frozen eigenbundles).** Assume (H1), (H2). If on a connected open U ⊆ B a band's eigenspace equals a full isotypic component with m_α = 1, then

$$P_{\mathrm{band}}(b) = E_\alpha \;\; \text{for all } b \in U \quad\Longrightarrow\quad \partial P_{\mathrm{band}} \equiv 0 \;\Longrightarrow\; Q_{ab} \equiv 0 \text{ on } U. \tag{E4}$$

The band is a constant (frozen) eigenbundle: zero base-direction connection, zero quantum metric, zero curvature; its Chen–Karki–Hosur (CKH) non-additivity is 0/0-vacuous on this base.

*Derivation, every step.* (1) By (H2), H(b) preserves each isotypic component, and by Schur's lemma its restriction to a multiplicity-one component is scalar: H(b)E_α = ν_α(b)E_α with ν_α(b) ∈ ℝ. (2) The eigenSPACE is therefore the isotypic component itself, which by (E1) is built from ρ alone — b-independent — even while the eigenVALUE ν_α(b) moves. (3) Differentiating H(b)E_α = ν_α(b)E_α along the base (E_α constant): (∂H)E_α = (∂ν_α)E_α — first-order perturbations cannot leak out of the slot; this is the pointwise witness dH|u⟩ = (dλ)|u⟩ recorded in W6-2 e2. (4) ∂P = ∂E_α = 0, and L0 gives Q_ab ≡ 0. (5) Crossings with *other* isotypic characters move only the |λ|-ordering label, never the slot projector: the corner defect is a tracking artifact of sorted labels, not of the geometry. ∎

**Theorem part T2 (the moving slot's invariant band-matrix is Schur-scalar).** Assume (H1)–(H4). Then for every base-direction pair (a,b),

$$M_{ab}(b)\big|_{\mathrm{ran}\,P} \;=\; c_{ab}(b)\,\mathbf{1}_{d_\alpha}, \qquad c_{ab}(b) = \langle w |(\partial_a \pi)(1-\pi)(\partial_b \pi)| w \rangle, \tag{E5}$$

where π(b) = |w(b)⟩⟨w(b)| is the rank-1 reduced eigenprojection in the multiplicity space ℂ^{m_α}. All G-invariant band-geometry data of the moving slot reduce to the eigenvalue ν(b) and the scalar 2-tensor c_{ab}(b) — a multiplicity-space (Fubini–Study-type) metric with **no band-index anisotropy**.

*Derivation, every step.* (1) P(b) is a spectral projector of H(b) (functional calculus on an isolated eigenvalue), so [ρ(g), H(b)] = 0 ⇒ [ρ(g), P(b)] = 0. (2) Differentiate along the base; ρ(g) is constant by (H1) — this is exactly where G-invariance of the *family* enters — so [ρ(g), ∂ₐP] = 0. (3) Hence every factor of M_ab commutes with ρ(g): [ρ(g), M_ab] = 0, and M_ab maps ran P → ran P. (4) ran P ≅ V_α irreducible (H4), so M_ab|_{ran P} is a G-equivariant endomorphism of an irreducible representation: by Schur's lemma it lies in the commutant End_G(V_α). For complex-type V_α this is ℂ·1, giving (E5) directly. (5) The explicit mechanism (tensor route): P = 1_{V_α} ⊗ π with π rank-1, so ∂P = 1_{V_α} ⊗ ∂π and M_ab = 1_{V_α} ⊗ [π(∂_aπ)(1−π)(∂_bπ)π] = c_{ab}·(1_{V_α} ⊗ π) — the rank-1 sandwich is the scalar c_ab of (E5); cross-terms into other isotypic components vanish because all factors are block-diagonal in (E1). ∎

*Commutant remark (rigor honesty).* For real- or quaternionic-type V_α, or for a band that is a sum of two distinct irreps each effectively multiplicity-one within the band, Schur weakens "scalar" to "commutant-valued" (block-scalar diag(c·1, c′·1) with equivariance killing the cross-blocks). The measured B2 witness — ‖M_ab − (Tr M_ab/4)P‖/‖M_ab‖ ≈ 1e-13 at interior nodes, both ττ and μμ (W6-2 e3) — certifies *full* scalarity on the quadruplet to thirteen decades, i.e. the slot behaves as a single complex-type irreducible (or carries an additional lock equating the block scalars). Every reading preserves the corollary below, since the commutant data carry no member-frame anisotropy in any case.

**Sub-lemma P (double protection of the chirality pair).** Assume (H1), (H2), (H5), (H6). For the γ-paired multiplicity-one slots, the cross-band (Wilczek–Zee) coupling m_a := ⟨u₊|∂_aH|u₋⟩ vanishes identically:

$$\{\gamma, H(b)\} = 0 \;\forall b \;\Rightarrow\; \{\gamma, \partial_a H\} = 0 \;\Rightarrow\; m_a = -\,m_a^{*} \;\;(\text{purely imaginary}); \qquad \text{(H6)} \Rightarrow m_a \in \mathbb{R}; \qquad \therefore\; m_a = 0. \tag{E6}$$

*Derivation, every step.* (1) γ is constant, so differentiating the anticommutator along the base gives {γ, ∂ₐH} = 0. (2) With u₊ = γu₋ (phase fixed real-positive; |⟨u₊|γ|u₋⟩| = 1): m_a = ⟨γu₋|∂ₐH|u₋⟩ = ⟨u₋|γ∂ₐH|u₋⟩ = −⟨u₋|(∂ₐH)γ|u₋⟩ = −⟨u₋|∂ₐH|u₊⟩ = −m_a* — the γ channel forces m_a imaginary-only. (3) The reality structure (H6) makes ∂ₐH real-symmetric and u± real in the fixed basis, so m_a is real. (4) A number both purely imaginary and real is zero. ∎ The pair's first-order inter-band channel is killed **twice**, by two independent structures; its QGT cross-content and CKH numerator sit at the float floor with no fine-tuning.

**Corollary U (symmetry-undecidability of Abelian-vs-non-Abelian band structure).** Assume (H1)–(H4). On a G-invariant base, *no G-invariant functional of the band geometry can distinguish a genuinely non-Abelian (Wilczek–Zee) band from a direct sum of d_α identical Abelian channels.*

*Derivation.* The CKH discriminator requires either (i) invariant band-matrix anisotropy — excluded by T2, M_ab ∝ 1; or (ii) a canonical band-member frame against which per-member Abelian metrics are defined — excluded because the band is an irreducible G-space: no G-invariant frame exists, any frame choice is gauge, and inside an exactly degenerate eigenspace per-member projectors are not even finite-difference-stable (W6-2 d1: the Abelian sum spans a 670× range over the U(2) gauge orbit while the non-Abelian trace is invariant to 1.67e-16; d2/d3: pinned-frame I_Ab(B2) = 5.77e+03 is an artifact of eigh's arbitrary intra-eigenspace rotations). Every invariant therefore factors through {ν(b), c_{ab}(b)} — which is *exactly* the invariant data of d_α independent Abelian bands with identical metric c_{ab}. The two models are observationally identical on this base. ∎

**Release condition R (regime of validity).** T1, T2, U hold exactly on, and only on, G-invariant families. Under a deformation H(b) + ε·δH with [ρ(g), δH] ≠ 0 for some g (isotropy-breaking), step (2) of T2 fails for the broken generators; M_ab is constrained only by the residual stabilizer Stab(δH) ⊊ G, and for generic δH the band-matrix develops anisotropy at O(ε) **iff** genuine within-band Wilczek–Zee structure exists. Simultaneously the T1 multiplicity locks release: the frozen slots acquire O(ε) base motion. Isotropy-breaking deformations are therefore both the *release condition* of the no-go and the *discriminator* the no-go licenses (forward gate CF-S101-B2-ISOTROPY-BREAKING, §V.1). The natural deformation candidates are off-block log-metric directions keyed to the C² coset generators λ₄..λ₇ — precisely the algebra directions that carry 94.8% of the Level-1 metric content in W6-1's d3 anatomy (final pin at S101 plan-freeze).

**Numerical witnesses (substrate realization; S100b W6-2, audit `4a03497c43a97335…`; all values LC-lineage-conditional per the caveat below).**

| Clause | Witness | Value |
|:-------|:--------|:------|
| T1 (B1 pair frozen) | max pairwise ‖ΔP‖_F over well-separated non-defect nodes | 7.94e-14 |
| T1 (B3∓/B3± frozen) | same | 1.44e-14 / 1.57e-14 |
| T1 (moving comparator) | B2∓/B2± ‖ΔP‖_F | 2.279e-01 / 2.279e-01 |
| T1 (frozen-slot QGT) | defect-excluded I_NA (pair) | 2.602e-24 (projector-FD round-off floor; interior integrand ceiling 1.64e-21) |
| T2 (Schur-scalar) | ‖M_ab − (Tr M_ab/4)P‖/‖M_ab‖ on B2, interior nodes, ττ and μμ | ≈ 1e-13 |
| T2 (moving-slot content) | defect-excluded I_NA(B2) | 2.591e-02 (22 OOM above the pair floor) |
| P (chirality lock) | max\|{H, γ₉}\|; \|⟨u₊\|γ₉\|u₋⟩\| | 0.0 exactly; 1.000000000 |
| P (double protection) | median \|A^WZ_{+−,a}\| = \|m_a\|/(λ₋−λ₊), denominator ≈ 1.64 M_KK | 1.297e-17 (99.96% of 2601 nodes < 1e-12) |
| P (CKH numerator at floor) | f_nonAb(pair) = \|I_Ab − I_NA\|/I_NA | 2.960595e-15 (numerator −4.44e-15 = 20·ε float-cancellation floor) |
| U (frame-dependence of the Abelian sum) | I_Ab over 8-sample Haar U(2) orbit vs I_NA invariance | 141.9 → 1006.9 (≈670× I_NA) vs ‖P_M(rot) − P_M‖ = 1.67e-16 |
| H3 boundary (corner defect) | pinned-mesh I_NA carried by 3 FD-defect nodes; spike anatomy | 1.5 = 100.00% (node value 2.5e+05 = 4/Δ², Δ = 0.004); C_FHS = −0.5 from a single π-plaquette, 2499/2500 plaquettes \|F\| < 1e-6 |
| Metric-not-curvature companion | Im_int = ∫ Im Tr_band Q_{[τ,μ]} | 6.124613e-18 < 1e-12 (pointwise max 1.53e-12, localized at the defect) |

**Lineage caveat (MANDATORY; carried verbatim into any Stage-1 registration).** W6-2 carries the UNTRUSTED-UPSTREAM caveat (housekeeping §A19; verdict-file extra-row, `s100b_gate_verdicts.txt` line 95): the consumed s84 spectrum-cache lineage sits at the Levi-Civita torsion point t = 1/2 of the Lai–Teh family, with operator CANONICITY under Q1-workshop adjudication (numerical validity is control-verified; the eigensolver is correct at machine epsilon). The split this theorem text must preserve — and both Wave-6 working papers state it explicitly — is: **the gauge-free projector Lemma L0, the trace identity, and the Schur/isotropy arguments (T1, T2, P, U, R) are operator-independent**: they use only (E1)-equivariance, functional calculus, the constant involution γ, and the reality structure, none of which reference the torsion point — they transfer as-is under *either* branch of the τ = 0 canonicity adjudication. **The specific eigenbundle NUMBERS** (which slots are multiplicity-one, the signed layout, ‖ΔP‖ values, I_NA(B2) = 2.59e-2, the corner-crossing location) **are LC-lineage-conditional** and would be recomputed under a re-adjudicated operator.

**Clause attribution (Stage-0 form).** (a) L0 — berry-side (operator-independent algebra). (b) T1 — berry-side representation theory; cites S22b block-diagonality (PROVEN, spectral/NCG-side input) for the fiber realization. (c) T2 + commutant remark — berry-side. (d) P — berry-side; cites the S25 reality-mechanism class (berry-side prior PROVEN result) + the measured γ₉ witnesses. (e) U — berry-side. (f) R — berry-side; forward gate S101. (g) Numerical witness clauses — berry-side compute (S100b W6-2), LC-lineage-conditional. The candidate is thus single-axis (geometric) with cited cross-axis PROVEN inputs; it may route at Stage-1 either as a standard structural-theorem registration or as a joint theorem if an NCG-side co-author lands the (H1)/(H2) spectral-triple realization clauses independently. Under **both** routes, Stage-2 independent verification applies with the berry exclusion stated at the head of this section.

### II.3 Corrected interpretive scope of the W6-2 FAIL(a) record

**Result**: scope paragraph for the permanent record. **Classification: GEOMETRIC.**

The verdict line stands as emitted (FAIL, reading (a), `sign=PASS/magnitude=FAIL/regime=VALID`, audit `4a03497c…`); what follows scopes its *interpretation*, which the plan's FAIL-arm rubric routed to interpretation without registry regression.

**What FAIL(a) certifies** (numbers LC-lineage-conditional; structure operator-independent):

1. **The lowest (J/PH pair) multiplet is doubly protected and is not a CKH carrier on this base.** γ₉ forces the cross-WZ channel imaginary-only; substrate J reality kills the remainder (sub-lemma P): median |A^WZ| = 1.3e-17; f_nonAb(pair) = 2.96e-15 = the 20·ε float-cancellation floor. This is a *derivation-backed zero*, not a null measurement.
2. **Band-selective rigidity.** The B1 pair and B3 triplets are frozen eigenbundles over the entire surface (‖ΔP‖_F ~ 1e-14; multiplicity-locked isotypic slots; base QGT ≡ 0); the B2 quadruplets are the **sole moving geometric carrier** (‖ΔP‖_F = 0.228; defect-excluded I_NA(B2) = 2.59e-2, twenty-two orders of magnitude above the pair-channel defect-excluded floor 2.602e-24).
3. **Metric-not-curvature re-confirmed.** Im_int = 6.1e-18 < 1e-12; the punctured-surface F-field is trivial (2499/2500 plaquettes |F| < 1e-6); the 12-invariant topological-triviality chain stands.
4. **The anomaly class is reconciled.** The exact-rational values I_NA = 1.5 and C_FHS = −0.5 are FD corner-defect artifacts of sorted-label tracking at the symmetry-allowed B1/B2 crossing (3 nodes; spike anatomy 4/Δ²; single π-plaquette) — not substrate topology (§II.5).

**What FAIL(a) does NOT certify — the honest boundary:**

The literal B2-arm discriminator that *triggered* reading (a), f_nonAb(B2) = 7.44e+03 > 1e-10, is **frame-artifact-dominated** per the gate's own d2/d3 attribution: its Abelian leg I_Ab(B2, pinned frame) = 5.77e+03 is produced by eigh's arbitrary intra-eigenspace rotations inside the exactly degenerate quadruplet, where per-member rank-1 projectors are frame-dependent *by construction* and not even FD-stable (the sharpened CKH point); 96.66% of the pinned I_NA(B2) = 0.776 is likewise carried by the 3 corner-defect nodes. The *sound* B2 evidence is the defect-excluded, gauge-free I_NA_excl(B2) = 2.59e-2 — which certifies that B2 **moves** and carries the only genuine metric content on this base. But by Corollary U (e3 witness: the B2 invariant band-matrix is Schur-scalar, ∝ 1₄ to 1e-13), whether that moving content is **non-Abelian (Wilczek–Zee) or an isotropic Abelian direct sum is UNDECIDABLE on any U(2)-invariant base** — the symmetry forces the only invariant to the exact form an Abelian model would produce.

**Therefore the FAIL(a) label "B2-carries-CKH" is to be read as: "the pair is doubly protected, and B2 is the sole moving carrier of band geometry on this base" — NOT as "B2 content is verified non-Abelian."** The affirmative non-Abelian question transfers, whole, to the isotropy-breaking gate (CF-S101-B2-ISOTROPY-BREAKING), whose honest dual-prior and thresholds are handed in §V.1. The plan's Track-B-variant routing ("protection specific to the PH doublet, NOT Abelian reduction of the algebra") is unchanged by this scoping: the algebra-correctness reading of the §VII.AF.1.OP-PROJ trace object survives untouched, because W6-2's zero is now *explained* by symmetry forcing rather than weighing against the algebra reading.

### II.4 Level-1/Level-2 two-differential declaration (W6-1 ↔ W6-2 on the same B1 pair)

**Result**: declaration per `phononic-framing.md` §"Single-τ-slice vs moduli-deformation substrate-IS levels". **Classification: GEOMETRIC.**

Wave 6 evaluated **two different differentials of the same projector field**, and a future reader who conflates them will manufacture a contradiction that does not exist:

- **W6-1 (Level-1, single-τ-slice substrate-IS)** differentiates along **ALGEBRA directions** at the fixed slice τ_fold = 0.19: the φ_g^sym cocycle legs are commutators [P, J_a] with J_a = iK_a the Kosmann spin-lifts of the Gell-Mann generators — su(3) Ad-orbit transport of the band-0 projector at fixed base point. The B1-pair algebra-direction metric trace is **NONZERO**: Σ_a (1/16)‖(1−P)J_aP‖²_F = 0.0417715, with the content loss under the normal-state swap localized to the order-parameter-gated C² coset directions (0.0396 → 0.0128, a 3.1× loss; 94.8% of the BdG metric content in λ₄..λ₇; λ₈ machine-zero = the proven wall [iK₇, D_K] = 0 manifest in the metric trace). Audit `06206dbbd1f6ec38…` (PASS).
- **W6-2 (Level-2, moduli-deformation substrate-IS)** differentiates along **MODULI-BASE directions**: ∂_τ, ∂_μ on the U(2)-invariant TT surface. For the same B1 pair the eigenbundle is **base-FROZEN**: ∂P ≡ 0 to ‖ΔP‖_F = 7.9e-14, base QGT ≡ 0 (Theorem T1). Audit `4a03497c…` (FAIL(a)).

**No contradiction.** The two differentials probe complementary direction sets, and symmetry decides both with the same Schur skeleton: the U(2)-invariant base moves only along isotropy-preserving directions, against which the multiplicity-locked B1 slot is rigid (T1); the Level-1 algebra legs move along the su(3) coset, where the same slot is maximally responsive — and that response is order-parameter-gated (it requires τ > 0; it is 94.8% C²-coset). In bundle language: the B1 eigenbundle over the moduli base is a *flat, constant* bundle (zero base connection), while its fixed fiber carries a *nonzero Ad(SU(3))-orbit quantum metric* — the W6-1 pairing is a slice of the S61 metric reservoir (g = 982.5 full-surface; the dimensional-reduction reframe: the metric-rich content lives in su(3)/Kosmann directions, not the moduli base). The declaration to write into any registry text touching either result: **W6-1's pairing is a Level-1 algebra-direction observable; W6-2's QGT is a Level-2 base-direction observable; on the B1 pair the first is 0.0417715 and the second is identically zero, and both follow from the same U(2)-isotypic structure.** The two levels are structurally orthogonal per the algebra-axis orthogonality discipline (`cross-pillar-bridge-anatomy.md`), and the level tag is a structural pin, not commentary.

The closure is tight in one further respect: the isotropy-*breaking* moduli directions that release the W6-2 no-go (condition R) are the Level-1 coset directions λ₄..λ₇ *promoted to base directions* — the S101 gate will deform the base along exactly the directions in which W6-1 measured the pair's metric content to live.

### II.5 Lineage: the Schur skeleton, the S96-class anomaly reconciliations, metric-not-curvature

**Result**: ancestry + resolved context. **Classification: GEOMETRIC.**

**The Schur skeleton is inherited, one layer up.** The candidate of §II.2 is the same structural argument as the permanent **off-Jensen-gradient = 0** closure — U(2) invariance of the Jensen line forcing the transverse spectral-action gradient to vanish (S62-era U(2)-invariance mechanism per the dimensional-reduction work; PROVEN closure "W1-E + W5-G: the off-Jensen direction is closed; the spectral action is effectively one-dimensional (τ only)"; computational witness GRAD-69 / `s69_off_jensen_gradient.py`; constraint-mega-matrix W3 row "Jensen curve + U(2)-invariant") — **lifted from the spectral-action-gradient layer to the eigenbundle/QGT layer**. At the scalar layer, invariance forces a *functional's gradient* to vanish at the symmetric locus; at the operator layer, the same invariance forces *projectors* constant (T1) and *band-matrices* scalar (T2). One symmetry, two floors of the same building: Pillar VIII Jensen geometry ↔ Pillar IV quantum-metric bridge mechanism, now connected at the eigenbundle level.

**S96-class anomaly reconciliations (resolved context).** The suspicious exact-rational pair flagged against the S96 scaffold baseline — I_NA = 1.5 *exact* and C_FHS = −0.5 — is fully reconciled by W6-2's corner anatomy as FD corner-defect artifacts: the symmetry-allowed B1/B2 crossing (von Neumann–Wigner; distinct isotropy characters) clips the (0.10, +0.10) window corner; sorted/signed-label tracking jumps to an orthogonal subspace there, injecting exact-rational FD spikes (node (0,50): 2.5e+05 = 4/Δ², weight×value = 1.000000; nodes (0,49)/(1,50): 3.125e+04, 0.250000 each — totalling 1.5 = 100.00% of the pinned I_NA), and a single corner π-plaquette produces C_FHS = −0.5 while 2499/2500 plaquettes carry |F| < 1e-6. Not topology; a tracking-artifact class. One labeling-precision note, flagged per the conflict rule: the Wave-6 synthesis constraint-map row words these as "S96 anomalies", while §W6-2 CC-3 records that S96's *emitted* baseline was the trivial C_FHS = 9.78e-15 — its |λ|-argsort blocks fell *below* the det-link guard at the defect (identity links), masking the class that W6-2's signed tracking exposed. Both sources agree on the physics (artifact, not substrate topology; S96's PASS-TRIVIAL stands); the row's label names the anomaly *class*, not an emitted S96 value.

**Metric-not-curvature, re-confirmed.** Im_int = 6.1e-18 (raw integrated antisymmetric part; bound 1e-12), the punctured-surface F-field trivial, and the S25/S61/S96 chain (Berry curvature ≡ 0 on SU(3); 12 independent zero invariants; off-Jensen Chern trivial) unbroken. The substrate remains in its signature regime: metrically structured where symmetry permits motion (B2), topologically trivial everywhere.

---

## III. Gate Verdicts

Verdicts are quoted from the sources; authoritative as emitted.

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| §W6-1 `S100b-VII-AF1-BDG-PROJECTOR-CONFIRM` | **PASS** (sign=PASS/mag=PASS/regime=VALID) | Δ_disc = 0.341976 = 342× the 1e-3 Level-2 floor; C² coset content 0.0396 → 0.0128 (3.1×); audit `06206dbbd1f6ec3858e8fc1469d87d24e52164e72bd1f70ad05cbbd02b172783` |
| §W6-2 `S100b-NONABELIAN-METRIC-FRACTION` | **FAIL** `[FAIL-a-JPH-protected-B2-carries-CKH]` (sign=PASS/mag=FAIL/regime=VALID; breach fraction 1.38%) | f_nonAb(pair) = 2.960595e-15 ≤ 1e-10; Im_int = 6.12e-18 < 1e-12 (companion PASS); B2-arm literal 7.44e+03 (frame-artifact-dominated, §II.3); audit `4a03497c43a97335144bad80f60e16d00097829ca4310f25315dfe4c9c926818` |
| §W6-3 `S100b-LEGGETT-DAMPING-INHERITANCE` | **PASS** (Option-A canonical; supersedes `cd5b0bc3…`) | class-(iii) χ-transportable decay channels EMPTY; x_L1 = 0.148625 < 1; x_DM = 5.985 Z₂-protected; audit `bce1ed8010a6a023…` |

W6-1 and W6-2 both carry the UNTRUSTED-UPSTREAM caveat (housekeeping §A19; W6-2 verdict-file extra-row at line 95); W6-3 is not a cache consumer and is correctly uncaveated.

---

## IV. Structural Implications

1. **A new wall, candidate-grade: symmetry-undecidability on invariant bases.** Corollary U is a no-go of the same epistemic kind as the framework's permanent walls — it eliminates a *class of measurements* (all G-invariant band-geometry functionals on G-invariant deformation families) as discriminators of Abelian-vs-non-Abelian band structure. Every future quantum-geometry gate on a symmetric base must be designed against it: the discriminating content must be sourced either from isotropy-breaking deformations (condition R) or from non-invariant observables declared as such. The constraint-map row already landed by the Wave-6 synthesis ("Abelian-vs-non-Abelian SYMMETRY-UNDECIDABLE on U(2)-invariant bases") acquires, through §II.2, a first-principles derivation rather than a numerical observation.

2. **The W6-2 FAIL strengthens, not weakens, the §VII.AF.1.OP-PROJ algebra reading.** The pair-channel zero is now *derived* (sub-lemma P: γ₉ + J, double protection), so it carries no evidential weight against the CKH algebra-correctness of the bridge's trace object; the bridge object itself (quantum METRIC, Re QGT) and the metric-not-curvature regime are re-confirmed. The registered entry is untouched (correct branch of the pre-registered routing).

3. **Band-geometry topology of the (0,0) fiber is now mapped.** Frozen slots (B1, B3) ↔ multiplicity-one isotypic components; moving slot (B2) ↔ multiplicity ≥ 2; the only invariant moving-slot datum is a scalar base-metric c_ab(b). This is the complete classification of what the U(2)-invariant moduli base can see of the singlet fiber — the geometric skeleton for any future gate on this base.

4. **The two-differential declaration (§II.4) is a conflation guard with registry consequences.** Any future registry or capstone text citing "the quantum metric of the B1 pair" MUST carry the Level-1 (algebra-direction, 0.0417715) vs Level-2 (base-direction, ≡ 0) tag; the bare phrase is ambiguous between a nonzero and an identically-zero quantity.

5. **Evaluator discipline propagates.** The gauge-free projector identity (L0) is the *only* safe evaluator inside exactly degenerate fibers (phase pins π-jump; per-member decompositions are not FD-stable); corner crossings between isotypic characters must be gap-mapped and defect-excluded; sign floors at the canonical 1e-14 (Class 8.3 item 4). These are now standing design rules, recorded in agent memory and embodied in the S101 spec below.

6. **Lineage hygiene.** All structural conclusions are operator-independent and survive either branch of the τ = 0 canonicity adjudication; all specific numbers are LC-lineage-conditional (§A19). Any Stage-1 registration must carry the caveat verbatim.

---

## V. Carry-Forward Computations

**V.1 CF-S101-B2-ISOTROPY-BREAKING — enrichment: honest dual-prior + threshold rationale (the handoff this synthesis owes the S101 plan author).**
- **What**: evaluate the B2 quadruplet's band-matrix anisotropy and non-Abelian fraction on an isotropy-BROKEN deformation family (pre-registered at S101 plan-freeze; natural candidates: off-block log-metric directions keyed to the C² coset generators λ₄..λ₇, per §II.4's closure), with three pre-registered witnesses: (i) **release positive-control** — frozen-slot motion ‖ΔP(B1)‖_F and ‖ΔP(B3)‖_F must exceed 1e-10 (visibly above the 1e-14 frozen floor) on the broken base, else the deformation failed to break the isotropy at the fiber level and the gate is vacuous (Class-8.7-adjacent pre-flight; this control is MANDATORY before the discriminator is read); (ii) **anisotropy discriminator** — A(b) := ‖M_ab − (Tr_band M_ab/4)·P‖_F/‖M_ab‖_F at interior defect-excluded nodes, PASS floor A > 1e-10 (three decades above the measured 1e-13 Schur-scalar floor, same machine-zero-discriminator philosophy as W6-2's f_nonAb floor) AND first-order scaling verified by a ≥3-point ε_break-scan (fitted slope d log A/d log ε = 1.0 ± 0.3 — distinguishes a genuine Schur release, generically O(ε), from floor noise); (iii) **defect-excluded f_nonAb(B2, deformed)** via the gauge-free L0 evaluator with gap-mapping and defect-excluded companions, sign floor 1e-14. **Baseline anchoring, honest**: the W6-2 B2-arm literal 7.44e+03 anchors the *artifact-channel scale only* (eigh intra-eigenspace rotations; §II.3) — it is NOT a physics target, and any claimed f_nonAb must demonstrate frame-invariance (d1-style orbit spread below a pre-registered ceiling) before counting as evidence. **Recommended dual-prior pre-registration block** (per `epistemic-discipline.md` §"Dual-prior pre-registration"; this is plan-freeze machinery, not a framework-probability assessment): Track A — genuine within-band WZ structure, symmetry-masked on the invariant base; anisotropy releases at O(ε) — prior 0.6 (the W6-2 plan's 0.75 algebra prior, tempered by the substrate's repeated Schur-triviality record: L0–L7 chain, 12 zero invariants, off-Jensen gradient = 0 — the same skeleton has so far always landed trivial when tested). Track B — the B2 content is structurally Abelian-isotropic beyond the symmetry forcing (a residual protection — e.g. Stab(δH) ⊇ SU(2), or J-reality on the real form — keeps M_ab scalar off-symmetry) — prior 0.4. Discriminator: PASS (control (i) ∧ A > 1e-10 ∧ linear ε-scaling) → 0.9 Track A; FAIL (control (i) passed, A at floor) → 0.85 Track B; INFO (control (i) failed, or ε-scaling indeterminate) → priors unchanged, deformation family re-pinned. Crucially, W6-2's FAIL(a) itself carries **zero** prior weight against Track A (Corollary U: the invariant base could not have seen the difference).
- **Inputs**: `computations/session-100b/s100b_nonabelian_metric_fraction.{py,npz}` (B2 eigenbundle, I_NA_excl(B2) = 2.59e-2 baseline, e3 Schur-scalar floor 1e-13, d1 frame diagnostics, gauge-free L0 machinery — operator-independent per the §A19 caveat split); `computations/_shared/dirac_spectrum.py`; deformation-family pin (S101 plan-freeze); `tau_fold` from canonical_constants.
- **Gate**: `S101-B2-ISOTROPY-BREAKING` (extends the WP CF block's spec with the witnesses, floors, control, and dual-prior above; pre-registration at S101 plan-freeze; carries the UNTRUSTED-UPSTREAM caveat until the τ = 0 canonicity adjudication lands).
- **Effort**: 1 compute gate, ≤ half a session (small-matrix eigenbundle sweep + ε-scan; GPU optional).

**V.2 Stage-1 registration + Stage-2 two-agent independent verification of the §II.2 candidate.**
- **What**: land the §II.2 frozen text as a `STAGE-1-CANDIDATE` registry entry (next-free §VII slot; designated writer per registry discipline; LC-lineage caveat carried verbatim; clause attribution as written), then dispatch the Stage-2 EXTENDED-THEOREM-INDEPENDENT-VERIFY gate: two parallel cross-reviewers re-derive L0/T1/T2/P/U from the registered text alone and independently re-verify the numerical witness table against `s100b_nonabelian_metric_fraction.npz` (witness re-check is a compute: re-evaluate ‖ΔP‖ tables, the e3 scalarity ratio, and the A^WZ median from the npz arrays without consuming this synthesis).
- **Inputs**: §II.2 of this synthesis (frozen candidate text); `s100b_nonabelian_metric_fraction.npz`; `joint-theorem-promotion.md` (4-stage pathway + Axis-B Selection Protocol); `_joint_theorem_independent_verify_audit.py`.
- **Gate**: `S101-SCHUR-RIGIDITY-STAGE2-VERIFY` — PASS iff both reviewers independently PASS every clause (a)–(g), with joint clauses PASS-AND'd; reviewer constraint pinned: **berry-geometric-phase-theorist (and successor berry spawns) EXCLUDED** per Stage-0 authorship + the S99 E1 reviewer-exclusion hardening + the downstream-inheritance reach (berry memory `s100b-band-selective-rigidity.md` inherits the reading path); reviewers must also clear the audit-machinery self-authorship check (audit item 6).
- **Effort**: 1 registration dispatch + 2 parallel review agents, ≤ half a session combined.

No other MATH follow-ups: the Mode-A absolute-reproduction item (CF-W6-1) is already specified in the WP CF block and belongs to landau's thread; the Level-1/Level-2 declaration (§II.4) and FAIL(a) scope paragraph (§II.3) are text artifacts consumed by the S101 plan author and the registry writer, not computations.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Band-Selective Schur Rigidity theorem candidate (L0 + T1 + T2 + P + U + R), §II.2 | GEOMETRIC | Stage-0-ready (frozen text; berry = Stage-0 author, EXCLUDED from Stage-2) | Symmetry-undecidability no-go: G-invariant functionals on G-invariant bases cannot discriminate Abelian vs non-Abelian band structure; release = isotropy breaking |
| 2 | FAIL(a) honest scope: certified = {pair doubly protected; B2 sole moving carrier; metric-not-curvature; anomaly class reconciled}; NOT certified = {B2 non-Abelian character} | GEOMETRIC | Scope paragraph final (§II.3); verdict line untouched | B2-arm literal 7.44e+03 = artifact-channel scale only; affirmative question transfers whole to S101 |
| 3 | Two-differential declaration: B1 pair Level-1 algebra-direction pairing 0.0417715 ≠ 0 (W6-1) vs Level-2 base-direction QGT ≡ 0 (W6-2) — no contradiction | GEOMETRIC | Declared (§II.4); registry conflation guard | Level-1/Level-2 tag mandatory on any future "B1-pair quantum metric" citation |
| 4 | Lineage: off-Jensen-gradient = 0 (U(2) Schur skeleton) lifted scalar-layer → eigenbundle-layer; S96-class anomalies (1.5 exact, −0.5) reconciled as FD corner artifacts; Im_int = 6.1e-18 | GEOMETRIC | Resolved context (§II.5) | One Schur skeleton spans Pillar VIII Jensen geometry ↔ Pillar IV quantum-metric bridge; topological triviality chain unbroken |
| 5 | S101 handoff: dual-prior 0.6/0.4 (A/B), positive control (lock release > 1e-10), anisotropy floor A > 1e-10 + linear ε-scaling, frame-invariance requirement | GEOMETRIC | Handed (§V.1) | W6-2 FAIL carries zero prior weight against Track A; gate design immune to the artifact channels W6-2 mapped |
| 6 | UNTRUSTED-UPSTREAM split: structure (L0/T1/T2/P/U/R) operator-independent; numbers LC-lineage-conditional | GEOMETRIC | Caveat carried (§A19; verdict line 95) | Theorem text transfers as-is under either τ = 0 canonicity branch; witness table recomputes under re-adjudication |
