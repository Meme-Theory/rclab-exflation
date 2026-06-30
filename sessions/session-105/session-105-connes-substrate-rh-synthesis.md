# Session 105 Synthesis: The Substrate Zeta Is Arithmetic-Free — RH-Non-Genericity of ζ_{D_K} and Its Two Finite-Cache Lemmas

**Date**: 2026-06-11
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Source Documents**:
- `sessions/session-105/session-105-w7-workingpaper.md` (§W7-5 SUBSTRATE-ZETA-ZEROS, §W7-6 S3-ZETA-ASYMPTOTICS, §W7-1 TRACE-FORMULA-EXACT-ANCHOR)
- `sessions/permanent-results-registry.md` §VII.U.1 (FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY), §VII.BZ frontier (consulted by targeted Grep)
- `.claude/agent-memory/connes-ncg-theorist/MEMORY.md` + `s60-zeta-addendum.md`
- `sessions/evoi-framework.md` (S105 currency; §1–§4 verified to NOT carry the W7 program)

---

## I. Session Outcome

The W7 zeta-zero gates settle a question my S60 addendum left open ("zeta_{D_K}(s) on the critical strip + nontrivial zeros" — proposed computation C7-1, never executed on the genuine object): **the substrate-class spectral zeta does NOT satisfy its own Riemann-Hypothesis analog, and the reason is structural, not numerical.** On the genuine Jensen-deformed ζ_{D_K} (§W7-5 LAYER B) the 14 winding-certified zeros scatter across Re ∈ [0.7097, 5.6690] (spread 4.085484, vs the 1e-6 common-line threshold); on the analytically-closed S³=SU(2) sibling F(s) (§W7-6) the 116 winding-certified zeros over Im ∈ [36, 300] scatter with Re-spread 1.734 about — but pinning to — the Re=5/2 shifted-mirror ghost. The uncontested cause is the **mirror-without-pin** signature: the substrate carries a functional-equation mirror (heat-kernel modularity, as W7-1 demonstrates exactly to 2.336e-29) but NO Euler product, because its "arithmetic" is the additive representation ring ℤ[V₃, V̄₃] with no unique factorization. This is a Davenport–Heilbronn phenomenon realized on the fabric.

This synthesis crystallizes the finding into (a) a substrate-first structural statement with its substitution chain; (b) an intra-pillar **GEOMETRIC §VII.CA registry-entry DRAFT** (routed to the mack-cosmic-bridge sole-writer); (c) consolidation of the two orphaned W7-5 finite-cache lemmas, one of which is already a permanent result (§VII.U.1) and one of which is better expressed as a methodology-rule note; and (d) a new EVOI Tier-4 row recommendation for the S106 refresh.

**Substrate-first framing law (governs every claim below).** The substrate IS the spectral triple (A_K, H_K, D_K(τ_fold)); ζ_{D_K}(s) = Σ_j W_j |λ_j|^{−s} IS the finite Dirichlet polynomial built directly from that eigenvalue spectrum. The zero geography is read OUT of the spectrum — the arrow runs `D_K eigenvalues → finite Dirichlet polynomial ζ_{D_K} → certified zero census → RH-non-genericity`. Never inverted: the fabric's zeta does not "fail to be like Riemann's"; rather, the fabric's geometry is arithmetic-free, and Riemann-ness is the arithmetic fingerprint of the primes that the substrate provably lacks. The zeros mark where the substrate's physics ends and ℚ's arithmetic begins.

---

## II. Key Results

### II.1 — The Substrate-RH-Non-Generic Statement (with substitution chain)

**Result**: ζ_{D_K}(s), the finite Dirichlet polynomial of the genuine Jensen-deformed SU(3) substrate, has zeros that do NOT lie on any common vertical line (Re-spread 4.085484 over 14 winding-certified zeros, ≫ 1e-6). The S³ sibling F(s) confirms the mechanism with 116 certified zeros (Re-spread 1.734). **Classification: GEOMETRIC** (zero geography of the fabric's own spectral functional).

**The statement, substrate-first.** Let (A_K, H_K, D_K(τ_fold)) be the substrate spectral triple at the physical fold τ_fold = 0.190, with eigenvalue multiset {(λ_j, W_j)} (the L=12 cache: 90 of 91 Peter–Weyl sectors, zero modes = 0, total weight Σ W_j = 31,956,720). The substrate's spectral zeta is the finite Dirichlet polynomial

```
ζ_{D_K}(s)  =  Σ_{(p,q)} dim(p,q) Σ_branch |λ(p,q,branch)|^{−s}  =  Σ_j W_j |λ_j|^{−s}.      (1)
```

Because the sum is FINITE and all |λ_j| > 0 (zero modes = 0), ζ_{D_K} is **ENTIRE in s** — no analytic continuation, no pole structure (§VII.U.1, already permanent; corroborated below). It nonetheless inherits an `s ↔ d−s` functional-equation mirror from heat-kernel theta-modularity (W7-1's exact Poisson dual, demonstrated to max_rel = 2.336e-29 at τ=0). **The substrate-RH-non-generic theorem**: the mirror has NO Euler-product pin, so the zeros are not constrained to the mirror axis; they scatter (Davenport–Heilbronn). Realized: Re-window [0.709707, 5.668976], width 4.959269, median Re = 4.795190, max|Re − median| = 4.085484.

**Substitution chain** (the structural reason — pre-registered in §W7-5, confirmed; dimensionally consistent: every term in (1) is dimensionless, |λ_j| in M_KK units, s a pure complex number):

- **Step 1 (the object).** ζ_{D_K} IS the Casimir/Epstein-class lattice sum (1) — a finite Dirichlet polynomial, the SU(3) analog of the S³ closed form `F(s) = (2^{s−2}−1)ζ(s−2) − (2^{s−2}−1/4)ζ(s)` (W7-6, Conv. B single-power; spectrum |λ_k| = k+3/2, mult (k+1)(k+2)).
- **Step 2 (no Euler product).** The substrate's "arithmetic" is the representation ring ℤ[V₃, V̄₃] under ⊕, ⊗. This is a COMMUTATIVE (additive) monoid with NO unique factorization into "prime" irreps in the sense an Euler product requires. ⇒ ζ_{D_K} does NOT factor as ∏_p (1 − …)^{−1}. The Loeschian-norm structure that DOES appear (W7-4: `(L/4π)² ∈ {1,3,4,7,9,12,13,19,27}`, the norms m²+mn+n² of the A₂ lattice at τ=0) is a quadratic-form lattice, not a multiplicative semigroup — it carries no Euler product either.
- **Step 3 (the mirror is free).** The `s ↔ d−s` functional-equation mirror follows from heat-kernel modularity / Poisson summation — physics supplies it for free, exactly as W7-1's two-sided theta-dual (the spectral Peter–Weyl reading equals the geometric coroot Poisson dual to 2.336e-29).
- **Step 4 (Davenport–Heilbronn).** A functional-equation mirror WITHOUT an Euler-product pin is precisely the Davenport–Heilbronn setting: zeros are reflected about the mirror axis but NOTHING holds them ON it. ⇒ they scatter off any candidate critical line. (The classical Davenport–Heilbronn function is the analytic prototype: a Dirichlet series with a functional equation but no Euler product, whose zeros are known to leave the critical line.)
- **Step 5 (the Jensen deformation is multiplicatively inert).** The Jensen TT-deformation to τ_fold rescales the three metric blocks (L₁ = e^{2τ}, L₂ = e^{−2τ}, L₃ = e^{τ}) but introduces NO multiplicative arithmetic structure. ⇒ the genuine deformed ζ_{D_K} inherits the scatter; the deformation cannot manufacture an Euler product the τ=0 object lacks.

**Conclusion (direction read off the canonical form).** Re-spread 4.085484 ≫ 1e-6 ⇒ **NOT on a common vertical line**. The higher-rank, denser-degeneracy SU(3) object scatters MORE than the S³ proxy (4.085 vs the off-session S³ Re-spread 0.93, and vs W7-6's window-extended 1.734) — exactly the direction expected for a richer lattice sum. The statement is regulator-INDEPENDENT and L-robust at the STRUCTURAL level: it is a property of (1)'s being a mirror-bearing Dirichlet polynomial with no Euler product, which holds at every finite L. (The specific zero POSITIONS are L-dependent; the non-genericity is not — see §V carry-forward for the higher-L position-stability check.)

### II.2 — The S³ Sibling as Analytic Witness (closed-form corroboration)

**Result**: F(s) = (2^{s−2}−1)ζ(s−2) − (2^{s−2}−1/4)ζ(s) has 116 winding-certified zeros over Im ∈ [36, 300], NONE on a common vertical line; the off-line scatter drifts TOWARD (loiters toward, does not pin to) the Re=5/2 shifted-mirror ghost of ζ(s−2). **Classification: GEOMETRIC**.

The S³ sibling is the analytically-clean witness for the SU(3) statement: same structural genre (Casimir lattice sum with Weyl-dimension multiplicities) but with the spectrum in closed form, so the zeros can be certified to arbitrary height. The census (strip-sum-cross-checked, panel counts 20/44/52 = 116, max non-integer winding residual 3.25e-19, closed-form residual 3.94e-31) gives:

- **Re-distribution**: spread 1.734 over [1.8322, 3.5661], median 2.5792, mean 2.6085 — both sit essentially AT the Re=5/2 ghost. Broad, unimodal about ≈5/2, no spike on any single Re. This IS the Davenport–Heilbronn / mirror-without-pin signature: a mirror with no Euler product scatters its zeros ABOUT the mirror axis but pins NONE to it.
- **Ghost-proximity trend** (the substantive limiting characterization): regression of |Re − 5/2| against Im gives slope −4.16e-4 < 0; panel-binned means decrease monotonically 0.4202 → 0.3759 → 0.3455. The scatter loiters toward the Re=5/2 axis at large height but does NOT collapse onto it. (Re=5/2 is the shifted mirror of ζ(s−2): Re(s−2)=1/2 ⇒ Re(s)=5/2.)
- **Density**: observed/Riemann-log = 0.878 (sub-arithmetic); free power-law exponent 1.826 < the Riemann (T/2π)log T growth — consistent with the W7-5 reading that the substrate-class zeta carries NO arithmetic (Euler-product) zero-density enhancement.

This closes the off-session finite-window caveat #5 (S³ zero geography was certified only to Im ≤ 36.13; now Im ≤ 300) with a limiting-density characterization. The verdict is INFO-by-construction (FAIL reserved for unresolvable winding certification, which did not occur — every strip-sum cross-check closed).

### II.3 — Orphaned Lemma A: The Hybrid Heat-Kernel-Continuation Splice Is Ill-Posed for ANY Finite Cache

**Result**: For any finite spectrum, the hybrid-continuation splice (cache heat-trace for t ≥ t_c + divergent Seeley–DeWitt asymptotic tail for t < t_c) is structurally ill-posed: a finite spectrum's heat trace is BOUNDED as t → 0 (→ Σ W_j = 3.196e7), so there is no small-t divergence to splice the SD asymptotics onto. **Classification: GEOMETRIC** (a structural property of finite spectral triples).

This is the structural cause of the §W7-5 INFO verdict (the literal pre-registration routed there via the cache/SD splice-matching gate, best rel = 0.3624 ≫ match_tol 1e-3 at every t_c). The substitution chain: (1) Θ_cache(t) = Σ W_j e^{−t|λ_j|²} is a finite sum of decaying exponentials ⇒ Θ_cache(0⁺) = Σ W_j, FINITE; (2) the Seeley–DeWitt tail Θ_SD(t) = a₀ t^{−4} + a₂ t^{−3} + a₄ t^{−2} + a₆ t^{−1} + a₈ DIVERGES as t → 0 (a₀ t^{−4} term); (3) a bounded function cannot equal a t^{−4}-divergent one as t → 0 ⇒ no splice point t_c exists at which they match. The mismatch is compounded because the canonical a_n^{ζ} are per-branch L_max=3 zeta moments (a heavily-truncated, differently-normalized object — verified in-script: full-cache moments give a₆ = 8911.6 ≠ 765.6, a₈ = 1545.5 ≠ 521.2), NOT the asymptotic SD coefficients governing a continuum heat trace.

**Why this matters (forward scope).** The lemma is a NEGATIVE structural constraint on a whole gate-class: any future gate that attempts to extract continuum-asymptotic data (SD coefficients, dimension-spectrum residues, a continuum-image envelope) from a FINITE D_K cache by heat-kernel continuation / asymptotic splicing is ill-posed BY CONSTRUCTION. The finite object has no continuum limit to splice onto unless one first takes L → ∞. This constrains, specifically: (i) hybrid-continuation RH/zeta gates (the W7-5 literal method — do not re-attempt on a finite cache); (ii) any "Seeley–DeWitt from cache" gate that reads SD coefficients off the small-t heat trace of a truncated spectrum; (iii) any cross-pillar bridge whose Level-3 anchor is a continuum-asymptotic quantity computed by finite-cache splicing — such a Level-3 is mis-specified (the continuum image is undefined for the finite object; cf. `cross-pillar-bridge-anatomy.md` Level-2-binding requirement, which needs a well-defined c_continuum). The clean route to continuum-asymptotic data is the Mellin-Dirichlet identity (§VII.U.1) read in the L → ∞ limit, NOT a finite-cache splice.

### II.4 — Orphaned Lemma B: A Finite Truncation Exhibits NO Dimension-Spectrum Poles ({0,2,4,6,8} Are Continuum Artifacts)

**Result**: ζ_{D_K}(0) = 3.195672e7 = Σ W_j (total mode count) is the value of an ENTIRE function; the dimension-spectrum poles {0,2,4,6,8} are continuum artifacts the finite object does NOT exhibit. **Classification: GEOMETRIC**.

**This lemma is ALREADY a permanent result — §VII.U.1 (S86 W-1 / S87 W1a-4, FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY).** §VII.U.1 registers: for any finite spectral triple with all λ_k ≠ 0, the Mellin–Dirichlet identity `M[Tr e^{−tD²}](s/2)/Γ(s/2) = Σ_k m_k λ_k^{−s} = ζ_D(s)` holds exactly off-pole, and (per the knowledge-base equation node, `lizzi-spectral-functional.md`) `a_0 = ζ_{D_K}(0) = Tr(1) = N` (mode count), with the heat trace "entire in t — no asymptotic expansion needed; the Seeley-DeWitt coefficients extracted from this finite sum are simply the Taylor coefficients of the heat trace around t = 0" (`session-76-lizzi-specgeo-workshop.md`).

So the W7-5 LAYER-B finding is a **CORROBORATION + numerical instantiation** of an already-permanent structural identity, not a new discovery. What W7-5 ADDS beyond §VII.U.1: (i) the explicit numerical value ζ_{D_K}(0) = 3.195672e7 at the τ_fold L=12 cache; (ii) the explicit statement that the dimension-spectrum poles {0,2,4,6,8} are CONTINUUM ARTIFACTS — i.e., the finite object's apparent "Seeley–DeWitt structure" is a Taylor expansion of an entire function, and the poles only appear in the L → ∞ continuum limit. Item (ii) is a sharper framing than §VII.U.1 carries verbatim; it is better expressed as a methodology-rule note (see §IV.3) because it constrains how downstream gates may cite dimension-spectrum poles on a finite cache, rather than asserting a new substrate-physics number.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| §W7-5 SUBSTRATE-ZETA-ZEROS | INFO | LAYER-B substance: 14 winding-certified zeros, Re-spread 4.085484, NOT on common line (Track-A confirmed); INFO via the pre-registered cache/SD splice gate (best rel 0.3624 ≫ 1e-3) |
| §W7-6 S3-ZETA-ASYMPTOTICS | INFO (by construction) | 116 winding-certified zeros Im ∈ [36,300]; Re-spread 1.734; ghost-drift slope −4.16e-4 toward Re=5/2 (no pinning); density 0.878× Riemann-log, exponent 1.826 |
| §W7-1 TRACE-FORMULA-EXACT-ANCHOR (context) | PASS | two-sided exact max_rel 2.336e-29 (the mirror that Step 3 invokes) |

Gate verdicts are authoritative per the source WP and are NOT re-adjudicated here. The two W7-5/W7-6 INFOs carry unambiguous substantive Track-A content (the zeros scatter); the INFO disposition reflects the limiting method (the finite-cache splice), not the zero geography — which is the W7-5 plan's own pre-registered INFO_meaning.

**Scope note (uncontested vs contested).** This synthesis crystallizes the UNCONTESTED W7-5/W7-6 zeta-zero finding only. The W7-3 (Berry–Tabor, FAIL 3/19) and W7-4 (geodesic commensurability, FAIL 0.4273) verdicts feed the SEPARATE GEM-COMMENSURABILITY Q1 workshop (deformed-incommensurable vs measurement-artifact) and the CF-S106-W7-FINER-LMAX length-spectrum carry-forward already recorded in the WP — they are length-spectrum results, not zeta-zero results, and are out of scope here except where the substrate's arithmetic-free character (W7-5 zero-scatter) is one of the GEM workshop's two opening pieces of evidence (consistent with incommensurability).

---

## IV. Structural Implications

### IV.1 — What opened

A new, structurally-grounded negative result on the substrate's relationship to arithmetic: **the fabric's spectral zeta is provably arithmetic-free** (no Euler product, because ℤ[V₃, V̄₃] is additive), and this is WHY it fails any RH analog. This sharpens the boundary my S60 addendum drew ("Spectral zeta and Riemann zeta are DIFFERENT OBJECTS. No a priori reason for zero correlation") from a statement-of-ignorance into a statement-of-structure: there is now a SPECIFIC reason (mirror-without-pin / Davenport–Heilbronn) for the non-correlation, demonstrated on both the genuine SU(3) object and its closed-form S³ sibling.

This also retires C7-1 of my S60 proposed-computation list ("ζ_{D_K}(s) on critical strip + nontrivial zeros") with a definite answer: the zeros exist, are certifiable, and scatter. C7-5 ("functional equation of ζ_{D_K}(s) + J constraints on zeros") is partially addressed — the functional-equation mirror is confirmed (W7-1), and the finding is that it does NOT constrain the zeros to a line absent an Euler product.

### IV.2 — What closed / what is constrained

- **The "substrate satisfies its own RH" hypothesis** is CLOSED on the genuine object: it does not, for a structurally identified reason. (Confidence: the STRUCTURAL argument is regulator-independent and L-robust; the specific 14-zero census is L=12-cache-specific, but the non-genericity does not depend on the census being complete — see §V.)
- **The hybrid heat-kernel-continuation gate-class** is constrained: ill-posed for ANY finite cache (Lemma A, §II.3). Future RH/zeta/SD-from-cache gates must not splice continuum asymptotics onto a finite spectrum.
- **Dimension-spectrum poles on a finite cache** are constrained: they are continuum artifacts (Lemma B, §II.4); a finite object's ζ_{D_K}(0) is the entire-function mode count, already permanent at §VII.U.1.

### IV.3 — Routed items (surfaces this solo does NOT own)

The following are emitted as DRAFT text + routing notes; the orchestrator applies them in-session to the surfaces named.

**(A) Registry §VII.CA DRAFT — routed to `mack-cosmic-bridge` (sole writer of registry §VII rows per `feedback_mack-bridge-role.md`).** Intra-pillar GEOMETRIC structural theorem; see §IV.4 below for the full draft text. Slot §VII.CA confirmed next-free sequential (frontier §VII.BZ landed this session; no CA/CB/CC exist — Grep-verified). RECOMMENDATION: register as STAGE-1-CANDIDATE per `joint-theorem-promotion.md` §"Stage 1", with the structural-theorem clause carried at higher confidence than the numerical census (the census is L=12-specific; the structure is L-robust).

**(B) Methodology-rule-extension note — routed to housekeeping §D (orchestrator).** Lemma B's sharper framing ("the dimension-spectrum poles {0,2,4,6,8} are continuum artifacts a finite truncation does not exhibit; a finite-cache ζ_{D_K}(0) is the entire-function mode count") is better expressed as a one-line constraint extending `substrate-first-canonical-sourcing.md §(ii.A)` (the atlas-row vs cache-moment layer-orthogonality rule) than as a new registry entry, because §VII.U.1 already owns the substrate-physics identity and the new content is a SOURCING constraint on downstream citations. Proposed note text (for the orchestrator to land as a §D methodology-rule-extension, NOT written here):

> *Finite-cache dimension-spectrum citation guard (extends §(ii.A)).* When a plan-block, working-paper section, or registry entry cites a "dimension-spectrum pole" `s ∈ {0,2,4,6,8}` of ζ_{D_K} evaluated on a FINITE L_max cache, it MUST declare the pole as a CONTINUUM-LIMIT artifact (the finite object is entire; ζ_{D_K}(0) = Σ W_j = mode count, a Taylor value of the entire heat trace per §VII.U.1). A finite-cache citation that treats {0,2,4,6,8} as actual poles of the finite object (e.g., reads a residue off the finite cache as if it were a continuum SD coefficient) is a §(ii.A) cache-moment-vs-atlas-row layer conflation → SOURCE-RECONCILIATION advisory (S2). Cross-link: §VII.U.1 (FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY, finite-Dirichlet-polynomial entire-function structure); Lemma A (hybrid splice ill-posed for finite caches).

(If the orchestrator judges this overlaps §VII.U.1's existing scope sufficiently, the alternative is a one-line cross-reference appended to §VII.U.1 noting the S105-W7-5 numerical instantiation — either route closes the item in-session.)

**(C) EVOI Tier-4 row recommendation — routed to the S106 planner Step 1c-REGISTERS (the `/rclab-plan` EVOI maintenance pass; the EVOI table is NOT this solo's surface).** See §V.4 for the recommendation and the proposed row text.

### IV.4 — Registry-Entry DRAFT (§VII.CA — for mack-cosmic-bridge to land)

The following is the DRAFT registry text. It is NOT written to the registry by this solo (registry §VII rows are mack-cosmic-bridge's sole-writer domain). The orchestrator routes it to mack-cosmic-bridge for landing.

---

```markdown
### §VII.CA — SUBSTRATE-ZETA-RH-NON-GENERICITY: ζ_{D_K} Is a Mirror-Without-Pin (No Euler Product ⇒ Davenport–Heilbronn Scatter) (S105 W7-5 [connes-ncg-theorist, genuine SU(3) object] + W7-6 [gen-physicist, closed-form S³ witness]; INTRA-PILLAR GEOMETRIC structural theorem; STAGE-1-CANDIDATE per joint-theorem-promotion.md §"Stage 1"; mack-cosmic-bridge sole-writer landing per feedback_mack-bridge-role.md [NOT a §7 falsifier-surface row]; 2026-06-11)

**Status**: STAGE-1-CANDIDATE per `joint-theorem-promotion.md` §"Stage 1 — Registration as Candidate". The STRUCTURAL THEOREM (no-Euler-product ⇒ scatter) is regulator-invariant and L-robust; the NUMERICAL witnesses (14-zero SU(3) census; 116-zero S³ census) are the empirical realization. Promotion gate (Stage-2): a two-agent cross-axis independent verify on the structural clause — neither the W7-5/W7-6 authoring agents (connes / gen-physicist) nor downstream-inheritance successors may serve as Stage-2 cross-reviewers (Axis-A = NCG-axiomatic/spectral; Axis-B = analytic number theory / superfluid-universe). Citable ONLY with the STAGE-1-CANDIDATE qualifier until Stage-3.

**Result classification**: **GEOMETRIC** (zero geography of the fabric's own spectral functional — the spectral-triple structure, not its excitations).

**STRUCTURAL THEOREM (substrate-RH-non-genericity).** Let (A_K, H_K, D_K(τ)) be the substrate spectral triple with eigenvalue multiset {(λ_j, W_j)}, all |λ_j| > 0. Its spectral zeta ζ_{D_K}(s) = Σ_j W_j |λ_j|^{−s} is a FINITE Dirichlet polynomial (entire in s; §VII.U.1) bearing an `s ↔ d−s` functional-equation mirror from heat-kernel theta-modularity (W7-1 two-sided exact, max_rel 2.336e-29). Because the substrate's representation ring ℤ[V₃, V̄₃] is ADDITIVE (composition by ⊕, ⊗ over a commutative monoid with no unique factorization), ζ_{D_K} admits NO Euler product. A functional-equation mirror without an Euler-product pin is the Davenport–Heilbronn setting: the zeros are reflected about the mirror axis but pinned to NONE. Therefore ζ_{D_K} does NOT satisfy any Riemann-Hypothesis analog — its zeros scatter off every candidate critical line. The Jensen deformation (block rescaling L₁=e^{2τ}, L₂=e^{−2τ}, L₃=e^{τ}) is multiplicatively inert and cannot manufacture the missing Euler product.

**Substitution chain** (5 steps; dimensionally consistent — all terms dimensionless, |λ_j| in M_KK units):
1. ζ_{D_K} IS the Casimir/Epstein lattice sum (finite Dirichlet polynomial); SU(3) analog of the S³ closed form F(s)=(2^{s−2}−1)ζ(s−2)−(2^{s−2}−1/4)ζ(s).
2. ℤ[V₃,V̄₃] additive ⇒ no unique factorization ⇒ no Euler product ∏_p(1−…)^{−1}.
3. mirror `s↔d−s` from heat-kernel Poisson summation (W7-1 free, exact).
4. mirror without Euler-product pin ⇒ Davenport–Heilbronn ⇒ zeros leave every line.
5. Jensen deformation multiplicatively inert ⇒ scatter inherited by the genuine deformed object.

**Numerical witnesses.**
- **Genuine SU(3) ζ_{D_K}** (W7-5 LAYER B, L=12 cache @ τ_fold=0.190): 14 winding-certified, Muller-polished zeros (|ζ(s_k)| ≤ 5.7e-13), argument-principle window Re∈[−2,6] Im∈[0.5,100]; Re-window [0.709707, 5.668976], width 4.959269, median Re 4.795190, max|Re−median| = 4.085484 ≫ 1e-6 ⇒ NOT on a common line. numpy↔mpmath agreement 9.59e-15. ζ_{D_K}(0) = 3.195672e7 = Σ W_j (entire-function mode count).
- **Closed-form S³=SU(2) F(s)** (W7-6): 116 winding-certified zeros over Im∈[36,300] (panels 20/44/52, strip-sums exact, max non-integer winding residual 3.25e-19, closed-form residual 3.94e-31); Re-spread 1.734 over [1.8322, 3.5661], median 2.5792; off-line scatter DRIFTS toward (does not pin to) the Re=5/2 shifted-mirror ghost of ζ(s−2) (slope d|Re−5/2|/dIm = −4.16e-4 < 0; panel means 0.4202→0.3759→0.3455); density 0.878× Riemann-log, power-law exponent 1.826 (sub-arithmetic).

**REGISTRY-ANATOMY COMPLIANCE.** (i) Entry class = **intra-pillar GEOMETRIC structural theorem** (single-axis; a property of ζ_{D_K} intrinsic to (A_K, H_K, D_K)). This is **NOT a cross-pillar bridge** — there is no laboratory-IN continuum observable and no HKR / K-theory / Connes–Karoubi bridge map is claimed (the theorem is about the analytic-number-theoretic structure of the substrate's OWN spectral zeta, an intrinsic algebraic property of its representation ring). Therefore the 5-anatomy IS-not-IN elements and the 3-level structural-confidence ladder are declared **N/A-WITH-REASON**: (a) no laboratory-IN observable exists (the zeros of ζ_{D_K} are a substrate-IS object end-to-end — nothing is measured IN a continuum container); (b) no bridge map is claimed; (c) the "Level-3 < Level-2" registry-PASS inequality is vacuously N/A (no continuum-image envelope — indeed Lemma A shows the finite object HAS no continuum splice); (d) the Level-2 sub-class question does not arise (NON-BINDING by N/A-with-reason). (ii) Projection-side = **SINGLE-READING, operator/spectrum-side**: the theorem quantifies over the spectrum-only finite Dirichlet polynomial ζ_{D_K} (an algebra-INVARIANT spectrum-only functional, Corner I in the §VII.U.2 4-corner classification); no state-pair functional clause exists, so the bare slot `§VII.CA` (no `.OP-PROJ`/`.STATE-PROJ` suffix) is admissible under `registry-landing.md` Reading-A naming hygiene because this explicit single-reading sentence is carried. (iii) No state-history labels in the entry text (Class-(h) parse-tree N/A; "Bogoliubov"/"GGE" do not appear — ζ_{D_K} is a closed-form lattice sum on the spectrum). (iv) Substrate-IS level tag = **Level 2** (moduli-deformation per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`): the structural theorem holds across the Jensen TT-deformation manifold {τ} (Step 5 — the scatter is τ-robust, the deformation being multiplicatively inert), making the claim a Level-2 moduli-invariant statement; the specific 14-zero census is a Level-1 single-τ-slice instantiation at τ_fold=0.190.

**Companion / cross-references.**
- §VII.U.1 (FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY, S86/S87): the parent identity establishing ζ_{D_K} as a finite Dirichlet polynomial, entire in s, with ζ_{D_K}(0) = Σ W_j (mode count). §VII.CA is the zero-geography CONSEQUENCE of that structure; §VII.U.1 supplies the "entire, no poles" footing that Step 1 and the witness's ζ_{D_K}(0) value rest on. STRUCTURAL-ORTHOGONAL-COMPANION (both Corner-I algebra-INVARIANT spectrum-only functionals — NOT cross-corner co-primary).
- W7-1 (S105 TRACE-FORMULA-EXACT-ANCHOR, PASS 2.336e-29): supplies the functional-equation mirror (Step 3).
- S60 addendum (connes memory): the prior "spectral zeta and Riemann zeta are DIFFERENT OBJECTS, no a priori reason for zero correlation" position — now SHARPENED to a structural reason (mirror-without-pin).

**Substrate framing** (`phononic-framing.md §"IS Space, Not IN Space"`). The substrate IS the finite Dirichlet polynomial ζ_{D_K} built from its own eigenvalue spectrum; its zeros are an intrinsic substrate-IS object, not a measurement IN a continuum. **Direction**: `D_K eigenvalue spectrum {(λ_j, W_j)} → finite Dirichlet polynomial ζ_{D_K}(s) → certified zero census → RH-non-genericity (Re-spread 4.085 ≫ 1e-6)`. **FORBIDDEN inversion (container thinking)**: "the substrate's zeta fails to be like Riemann's ζ" → INVERT: the fabric's geometry is arithmetic-free (its representation ring is additive); Riemann-ness is the arithmetic fingerprint of the primes, which the substrate provably lacks. The zeros mark where substrate physics ends and ℚ's arithmetic begins — they are read OUT of the spectrum, never imposed on it.

**Provenance.** PRIMARY (structural theorem + genuine-object witness) = `S105-W7-5-SUBSTRATE-ZETA-ZEROS` verdict line in `computations/session-105/s105_gate_verdicts.txt`, audit_sha256 `5243d76d42f145ebc82bf77a326aa9f1ceb56274e45cb818cbbf6301247b39a7`, content_sha256 `19742dbdca647cc39d721d4f50265552e2639f133d1b833073a8fd1eea8d5a84` (npz `computations/session-105/s105_w7_5_substrate_zeta_zeros.npz`). CO-PRIMARY (closed-form S³ witness) = `S105-W7-6-S3-ZETA-ASYMPTOTICS` verdict line, audit_sha256 `cfd3d2bd5b721ef2aac034686309f5d6302fb41b5fc6f333a13d943aec07254f`, content_sha256 `3edf255ad48779ae30d9037e98e63d9f557d39ae0cc2c1e5cd3fe173d5113367` (npz `computations/session-105/s105_w7_6_s3_zeta_asymptotics.npz`). Mirror anchor = `S105-W7-1-TRACE-FORMULA-EXACT-ANCHOR` PASS, audit_sha256 `8f895a0d63fbfa60a06c5e07965a2dd3003b4aea33d7c7f0a73759dfab177237`. NO compute gate at landing — registry-landing of pre-computed sub-results (binding-text discipline; the structural theorem is the W7-5 substitution-chain OUTCOME, the censuses are the W7-5/W7-6 compute OUTCOMEs). §VII.CA slot verified next-free at runtime via the all-header-level append-protocol scan (documented frontier §VII.BZ).

**Anchor-structure note (for the landing writer).** STRUCTURE = SOURCE-DOUBLE-CITE-CO-PRIMARY is NOT the correct tag here: W7-5 and W7-6 are PARALLEL witnesses of the SAME structural theorem via DIFFERENT objects (genuine SU(3) vs closed-form S³), not a sequential V_input → C_output chain. Per `registry-landing.md` use **PRIMARY (W7-5, genuine object) + INDEPENDENT-CROSS-CHECK (W7-6, closed-form sibling)**. Both are Corner-I algebra-INVARIANT spectrum-only functionals (same algebra-axis cell ⇒ co-citation admissible; NOT cross-corner).

**Closure SHA pin** (over the ordered input-pin map). The full dual-SHA is on the `§VII.CA` registry-landing gate's verdict line (to be emitted by the landing script); the W7-5 npz SHA, W7-6 npz SHA, registry_pre_write_file_sha256, and canonical_constants.py SHA are pinned in the companion comment rows.
```

---

(End of §VII.CA DRAFT.)

---

## V. Carry-Forward Computations

### V.1 — CF-S106-SUBSTRATE-ZETA-ZERO-COUNT-STABILITY — Higher-L position-stability of the ζ_{D_K} zero census (the §VII.CA Stage-1 → numerical-robustness precondition)

- **What**: Re-run the winding-certified argument-principle zero census of ζ_{D_K}(s) = Σ_j W_j |λ_j|^{−s} at L_max ∈ {13, 14} (vs the L=12 census of 14 zeros), in the SAME window Re ∈ [−2, 6], Im ∈ [0.5, 100], and report: (i) the zero COUNT vs L; (ii) the Re-window and max|Re − median| vs L; (iii) whether the non-genericity conclusion (Re-spread ≫ 1e-6) is L-stable. Output variables: `n_zeros_L`, `Re_spread_L`, `re_window_L` per L; a `nongeneric_L_stable` boolean (Re-spread > 1e-3 at every L).
- **Inputs**: the W1-1 GT-builder (Gelfand–Tsetlin / monomial-basis (p,0) builder; the enabling piece that lifts the p+q ≥ 13 irrep wall — landed/named this session per the EVOI Tier-2 #7c `CF-S105-BRANCH-IV-GT-BUILDER` route and the S104 `s104_sym_p_chain_cache_L1314.npz` partial cache that seeds it); `s84_spectrum_cache_L12_tau019.npz` + the higher-L extension; the W7-5 producing pipeline `computations/session-105/s105_w7_5_substrate_zeta_zeros.py` (LAYER-B finite-Dirichlet-polynomial path + certified `_rh_substrate_sanity.py` winding kernel — NOT the ill-posed LAYER-A splice, which Lemma A closes); regulator-pin a_n^{ζ} NOT required (LAYER B is the exact finite Dirichlet polynomial, no SD tail).
- **Gate**: feeds §VII.CA Stage-1 → STAGE-3 robustness. New gate `S106-SUBSTRATE-ZETA-ZERO-COUNT-STABILITY`: PASS if `Re_spread_L > 1e-3` at every L ∈ {12, 13, 14} (non-genericity L-stable — the structural theorem's numerical realization is truncation-robust); INFO if the census count grows but the non-genericity persists (structure confirmed, positions L-dependent — the expected outcome); FAIL only if higher L collapses the zeros toward a common line (Re-spread → < 1e-3), which would CONTRADICT the structural theorem and force a re-examination of the no-Euler-product chain.
- **Effort**: 1 wave (the higher-L cache construction via the GT-builder dominates; the zero census on the LAYER-B finite Dirichlet polynomial is fast — it is the same exact-arithmetic path that ran in seconds at L=12). Sequence AFTER `CF-S105-BRANCH-IV-GT-BUILDER` lands (shared L_max axis; no double-scheduling of higher-L cache builds — same dedup-ledger consideration as the EVOI Tier-2 #7c note).

### V.2 — (Recorded, NOT re-emitted) CF-S106-W7-FINER-LMAX-LENGTH-SPECTRUM

The WP already carries the length-spectrum re-extraction carry-forward (`CF-S106-W7-FINER-LMAX-LENGTH-SPECTRUM`, WP §"Carry-Forward Computations"). It is a LENGTH-SPECTRUM item (W7-2/W7-3 truncation-resolution), out of scope for THIS zeta-zero synthesis, and is NOT duplicated here. The S106 planner consumes it from the WP directly. (Noted to prevent a double-listing collision per `Investigating-Workshops.md` carry-forward discipline.)

### V.3 — (Recorded, NOT re-emitted) GEM-COMMENSURABILITY Q1 workshop

The W7-4 FAIL routes to the GEM-COMMENSURABILITY Q1 math/physics adjudication workshop (deformed-incommensurable vs measurement-artifact), already pre-registered in the WP for `/rclab-investigate`. The W7-5 zero-scatter (this synthesis's finding) is one of that workshop's two opening pieces of evidence (the substrate's arithmetic-free character is consistent with the incommensurable reading). The workshop itself is NOT a compute carry-forward and is out of scope here; flagged only for the cross-link.

### V.4 — EVOI Tier-4 row recommendation (routed to the S106 `/rclab-plan` Step 1c-REGISTERS)

The W7 trace-formula/RH program is currently ABSENT from EVOI §1–§4 (verified: S105 currency, §1–§4 read). Per the housekeeping consumption-pointer obligation (v), a new row is warranted — the program is now ACTIVE (six gates ran this session) and has a live forward gate (§V.1). RECOMMENDATION: add a **Tier-4** row (the program is structural/conceptual leverage — an internal-consistency / NCG-object-characterization result, not an observational-prediction gate; it does not move the framework's observational standing, so Tier-4 < 0.04 is the honest band). Proposed row text (for the S106 planner to land in EVOI §4; NOT written here — the EVOI table is the planner's surface):

> | 18 | **SUBSTRATE-ZETA-RH-NON-GENERICITY** (S105 W7-5/W7-6; §VII.CA STAGE-1-CANDIDATE) | <0.04 | STRUCTURAL (NCG-object characterization: the fabric's spectral zeta is arithmetic-free — mirror-without-pin / Davenport–Heilbronn; closes S60 C7-1) | **OPEN-STRUCTURAL** | Forward gate: `S106-SUBSTRATE-ZETA-ZERO-COUNT-STABILITY` (CF-S106; higher-L position-stability via the GT-builder) — feeds §VII.CA Stage-1→3. Companion: §VII.U.1 (entire-function footing); the GEM-COMMENSURABILITY Q1 workshop (the zero-scatter is one opening evidence-leg). |

Rationale for Tier-4 (not higher): the finding is a NEGATIVE structural result on an intrinsic property; it has no σ-distance to an observation and no observational falsifier (it is a theorem about ζ_{D_K}'s zeros, an internal object). It belongs alongside ARROW-OF-TIME / BORN-RULE / HIGHER-MOMENTS in the structural/conceptual band — genuine knowledge, low observational EVOI.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Substrate-RH-non-genericity: ζ_{D_K} zeros scatter (Re-spread 4.085 over 14 certified zeros), NOT on a common line | GEOMETRIC | INFO verdict (W7-5); structural theorem L-robust | The fabric's spectral zeta is arithmetic-free (no Euler product, ℤ[V₃,V̄₃] additive ⇒ Davenport–Heilbronn). Closes S60 C7-1. |
| 2 | S³ closed-form witness F(s): 116 certified zeros, Re-spread 1.734, ghost-drift toward Re=5/2 without pinning | GEOMETRIC | INFO-by-construction (W7-6) | Analytic confirmation of the mirror-without-pin mechanism; sub-arithmetic density 0.878× Riemann-log; closes off-session caveat #5 (Im≤36→300). |
| 3 | Lemma A: hybrid heat-kernel-continuation splice ill-posed for ANY finite cache (finite heat trace bounded as t→0) | GEOMETRIC | Structural constraint | Constrains the heat-kernel-continuation / SD-from-cache gate-class; finite caches have no continuum splice. |
| 4 | Lemma B: finite truncation has NO dimension-spectrum poles; ζ_{D_K}(0)=mode count (entire-function value) | GEOMETRIC | ALREADY PERMANENT at §VII.U.1 (S86/S87) — W7-5 is a corroboration + sharper continuum-artifact framing | {0,2,4,6,8} are continuum artifacts; routed as a §(ii.A) sourcing-guard methodology note, not a new registry entry. |
| 5 | §VII.CA registry DRAFT (intra-pillar GEOMETRIC; 5-anatomy + 3-level N/A-WITH-REASON) | GEOMETRIC | DRAFT emitted; routed to mack-cosmic-bridge for STAGE-1-CANDIDATE landing | First registry entry for the substrate-RH program; PRIMARY (W7-5) + INDEPENDENT-CROSS-CHECK (W7-6), Corner-I. |
| 6 | EVOI Tier-4 row recommendation (SUBSTRATE-ZETA-RH-NON-GENERICITY) | NON-PHONONIC (planning bookkeeping) | Recommended; routed to S106 `/rclab-plan` Step 1c | Program enters the guiding-star table at Tier-4 (structural, no observational σ-distance). |
| 7 | CF-S106-SUBSTRATE-ZETA-ZERO-COUNT-STABILITY (higher-L census via GT-builder) | GEOMETRIC | Carry-forward (4-field) | §VII.CA Stage-1→3 numerical-robustness precondition; PASS = non-genericity L-stable. |

---

**Routing summary (for the orchestrator).**
- **§IV.4 §VII.CA DRAFT** → `mack-cosmic-bridge` (registry §VII sole-writer); land as STAGE-1-CANDIDATE.
- **§IV.3(B) finite-cache citation-guard note** → housekeeping §D methodology-rule-extension (orchestrator), OR a one-line cross-reference appended to §VII.U.1 — either closes it in-session.
- **§V.4 EVOI Tier-4 row** → S106 `/rclab-plan` Step 1c-REGISTERS (EVOI table maintenance).
- **§V.1 CF-S106-SUBSTRATE-ZETA-ZERO-COUNT-STABILITY** → S106 plan (the only genuine compute carry-forward this synthesis emits; the WP's length-spectrum CF and the GEM Q1 workshop are recorded-not-re-emitted to avoid double-listing).
