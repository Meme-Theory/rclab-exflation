# Correspondence-Table Registry (parallel to permanent-results §VII)

> **Provenance**: project-level registry created by S86 W15-1
> (`S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY`) per
> `sessions/session-plan/session-86-plan-w15.md` §W15-1. Owner agent:
> `kaku-speculative-theorist`. The registry mirrors the
> `permanent-results-registry.md` §VII row schema for ANTI-CORRESPONDENCE
> entries but lives in `sessions/framework/` so that future cross-paradigm
> structural-exclusion arguments route through this single canonical
> ledger rather than re-deriving the case each time.

## Substrate-framing convention (MANDATORY for all entries)

Every entry in this registry pins a structural-EXCLUSION wall in the
SUBSTRATE solution space. The string-paradigm (or other contrast-anchor)
column is a CONTRAST ANCHOR, NOT a reference frame. Direction of
explanation: substrate spectral triple -> its own structural invariants
-> comparison FROM that structure outward to the contrast paradigm. Do
NOT write "the substrate looks like the contrast paradigm except for
these N corrections" -- that inverts the explanatory direction. The
substrate is logically prior; the contrast paradigm is the anchor.

Per `.claude/rules/phononic-framing.md`: this is a structural wall, not
a "things the substrate has that look like the string scheme" ledger.

## Schema (one row per entry)

  ## Entry #<N> -- <substrate aspect> vs <contrast paradigm>

  Source verdict: <gate ID> (S<N>), audit_sha256=<full 64-char>
  Sibling cluster: <list of sibling entry IDs forming the bloc>

  <N>-OBSTRUCTION VECTOR:
  | axis | substrate | <contrast paradigm> |
  |:-----|:----------|:--------------------|
  ...

  Substrate-side derivation pointers:
  ...

  Contrast-side anchor:
  ...


## Entry #30 -- Substrate vs Witten 1998 K-theoretic D-brane scheme

Source verdict: W10-1 (S85), audit_sha256=e034e19f7fbc3d9642997559ed8fd77c070e98331d07dddbf04405b2c464fddc
Sibling cluster: #19_no-T-duality, #20_no-S-duality, #21_no-Hagedorn
                 -- together, this 4-entry cluster forms the
                 string-paradigm-exclusion bloc inside this registry.

4-OBSTRUCTION VECTOR:

| axis                  | substrate              | Witten 1998       |
|:----------------------|:-----------------------|:------------------|
| rank                  | 3                      | 1                 |
| K_0                   | torsion-free           | Z/2               |
| Witten integral       | 16.0                   | 1.0               |
| Bott-period residue   | != 1                   | 1                 |

Each axis is a structural disagreement, NOT a numerical epsilon-deviation.
ALL FOUR must hold simultaneously for entry #30 to apply; absence of
any single component invalidates the registry write.

Substrate-side derivation pointers (substrate spectral triple is logically prior):
 - rank = 3: from the SU(3) gauge factor of D_K (Connes spectral-triple-rank
   theorem; the substrate's internal algebra A_F = C + H + M_3(C) gives
   K_0(A_F) rank = 3 from three Wedderburn-simple summands -- see §VII.R
   3-axis disjointness in `permanent-results-registry.md`).
 - K_0 torsion-free: from the SU(3) representation lattice of the Connes
   spectral triple (no Z/2 torsion appears in the substrate's K_0 group;
   the substrate's representation theory is over a noncommutative algebra
   of finite type, not a real KO-theory class).
 - Witten integral = 16.0: third spectral moment of D_K, computed as
   ch_0 * A-roof(TM^4) with the substrate's own characteristic-class data
   (16 distinct relay-pattern equivalence classes).
 - Bott-period residue != 1: 8-periodicity of real KO-theory is broken on
   the Jensen-deformed substrate by the tau_fold-localized parity flip
   (16 mod 8 = 0, 16 mod 2 = 0; neither congruence class hits 1).

Contrast-side anchor (string-paradigm reference, NOT a reference frame):
 - Witten, "D-Branes and K-Theory", JHEP 12 (1998) 019.
   Witten's K-theoretic D-brane classification scheme assigns single-brane
   K^0(X) = Z (rank 1), KO^6(pt) = Z/2 torsion, single-brane Witten
   integral = 1, and 8-periodic KO theory with residue 1. The substrate
   fails to match any of these four invariants.

Entry semantics: this is a structural EXCLUSION wall. The substrate's
spectral triple is genuinely DISTINCT from Witten's K-theoretic D-brane
classification along four independent axes. The four axes are not
small-correction perturbations of a shared structure -- they are
algebraically independent K-theoretic invariants. The registry write
documents the boundary the substrate's structural identity does not
cross under the Witten 1998 candidate parent.

Provenance chain (per S85 W10-1 patch):
 - Source gate: S84-DET-P-K-THEORY (W7-74); homotopy_level = 1
 - Source closure SHA-256: def5d0cdb8a39d16017820a602cb8821fefcbbc8720700f3eb6e5b095d4af1d2
 - Landing gate: S85-W10-ANTI-CORRESPONDENCE-30-REGISTRY (PASS)
 - Landing audit_sha256: e034e19f7fbc3d9642997559ed8fd77c070e98331d07dddbf04405b2c464fddc
 - Landing content_sha256: 5e5f6f0dcb6cbefcbfe146aa9ecc056f55b653469308a487308518ef36042138
 - Project-registry landing gate: S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY (this entry)


## Candidate-parent ledger

> **Provenance**: structural map produced by S86 slot 1b S-12 (connes-ncg-theorist
> synthesis at `sessions/archive/session-86/session-86-1b-s12-connes.md`). NOT a verdict
> gate; NOT a new ANTI-CORRESPONDENCE entry. Each row is a structural classification
> against the existing 4-obstruction vector (rank=3, K_0=torsion-free,
> Witten-integral=16.0, Bott-period residue ≠ 1) inherited from S85 W10-1 / S86 W15-1.
> New exclusion entries require their own pre-registered gates per the registry's
> substrate-framing convention; the S87 candidate gates are V.4, V.5, V.6.

### Eliminated by existing 4-vector (no new gate required, structural)

| Candidate K-theoretic scheme | Rank axis | K_0 torsion axis | Bott-residue axis | Eliminator source |
|:-----------------------------|:----------|:-----------------|:-------------------|:------------------|
| Witten 1998 IIB D-brane K | rank 1 ≠ 3 (FAIL) | Z/2 ≠ torsion-free (FAIL) | residue 1 (FAIL) | Entry #30 (S85 W10-1) |
| Heterotic E_8 × E_8 worldsheet | rank ≥ 16 ≠ 3 (FAIL) | torsion-free in low deg; matches substrate-side BUT FAILs W10-5 W-side test that expects Z/2 (mirror-axis convention; net FAIL) | mod 8 = 0 ≠ 1 (FAIL) | S85 W10-5 candidate A |
| M-theory C-field DMW | rank 1 ≠ 3 (FAIL) | Z (integer-charge); torsion-free at primary class but content ≠ A_F Wedderburn (FAIL on content) | 16 mod 8 = 0 ≠ 1 (FAIL) | S85 W10-5 candidate B |
| Twisted K with H-flux | rank depends on (X, H), generic ≠ 3 (FAIL) | Z/2 only under fine-tuning, generically not torsion-free (FAIL generically) | 16 mod 2 = 0 ≠ 1 (FAIL) | S85 W10-5 candidate C |
| Orientifold KR-theory | rank 1 generically (FAIL) | KR carries Z/2 torsion via KO^6(pt) inheritance (FAIL on torsion-free) | residue 1 natural under unbroken 8-periodicity (FAIL) | S86 1b S-12 §II.3a; needs S87 V.4 |
| F-theory K-theory (12-dim elliptic) | rank ∼ Hodge ≫ 3 (FAIL) | Mordell-Weil torsion generically nontrivial (FAIL) | dim 12 ≡ 4 mod 8; KO^4(pt) = Z gives residue 0, axis FAIL or mute by convention | S86 1b S-12 §II.3b; needs S87 V.5 |
| Equivariant KU_G generic | rank = \|Irr(G)\| ≠ 3 generically (FAIL) | torsion-free for compact connected G; FAILs for finite G with extensions; in any case content ≠ A_F (FAIL on content) | residue 1 natural under unbroken 8-periodicity (FAIL) | S86 1b S-12 §II.3c; needs S87 V.6 |

### Surviving candidate set (NCG-internal; require S87 gates)

| Candidate | Rank axis | K_0 torsion axis | Witten-integral axis | Bott-residue axis | S87 carry-forward |
|:----------|:----------|:-----------------|:----------------------|:-------------------|:-------------------|
| Karoubi K_*(A_F = C ⊕ H ⊕ M_3(C)) | Z^3 (PASS by construction) | torsion-free (PASS by construction) | mute (algebraic K does not carry D_K data) | mute (no topological grading) | V.1 (S87-KAROUBI-PARENT-OF-A_F): trivial-identity classification or non-trivial Karoubi superalgebra |
| Operator K_*(A_F^q) Hopf-deformed | Z^3 likely preserved at generic q (PASS) | depends on q being root-of-unity | depends on q-shift of third spectral moment | depends on q-preservation of τ_fold parity flip | V.2 (S87-Q-DEFORMED-K-PARENT) |
| Kasparov KK(A_F, B) ambient | Z^3 (PASS for B = C) | torsion-free (PASS) | substrate's [D_F] index pairing = 16 (likely PASS) | mute (KK is the framework's own K-homology category, not a contrast parent) | V.3 (S87-KK-PARENT-DISAMBIGUATION) — KK is a category, not a comparative parent |

### Disambiguation: parent vs. ambient category

- **Parent** (registry sense): a *contrast paradigm* whose K-theoretic invariants the substrate's spectral triple either *matches* (CORRESPONDENCE) or *fails to match* (ANTI-CORRESPONDENCE) — a comparative identity outside the framework.
- **Ambient category** (Pillar VIII sense): the K-theoretic *category* in which the substrate's K-homology class `[D_F]` is naturally constructed (Kasparov KK; Karoubi K of A_F by definition). NOT a comparative parent.

The string-paradigm exclusion bloc (#19/#20/#21/#30 + W10-5 cousins A/B/C + S87 V.4/V.5/V.6 candidates) is a *parent* exclusion. Karoubi K of A_F and Kasparov KK are *ambient categories*; classifying them as ANTI-CORRESPONDENCE entries is a category error and would invert the substrate-framing direction. The S87 V.7 carry-forward (CORRESPONDENCE-TABLE-CLASSIFICATION) extends the registry to support both polarities cleanly.

### Surviving set cardinality

After the structural sieve (eliminations + ambient-category reclassifications):

- **Topological-K parent space**: EMPTY (Witten + heterotic + M-theory + twisted K + orientifold KR + F-theory + equivariant KU_G all carry ≥ 2 of 3 obstructions structurally).
- **Algebraic-K parent space**: SINGLETON {operator K_*(A_F^q)} after Karoubi K and KK are reclassified as ambient categories.
- **Ambient categories** (not parents): {Karoubi K_*(A_F), Kasparov KK(A_F, ·)}.

The substrate's K-theoretic parent question therefore reduces to a single open computational gate: does the Hopf q-deformation of A_F preserve the 4-vector? If yes (V.2 PASS), the substrate's K-theoretic identity is q-stable. If no (V.2 FAIL), the parent space is fully empty and the substrate's K-theoretic identity is intrinsic to the undeformed spectral triple alone.


## Entry #31 — Substrate (BDI gap protection via Leggett dipolar) ↔ NCG-axiomatic (KO-dim 6 + AZ symmetry algebra TRS-PHS-chiral)

Source: S86 W-2 R3-B EMERGENCE (i) (mack+volovik), workshop file `session-86-w2-workingpaper.md` L1465-1494
Anchors: A4-V5 L830-842 + R2-B CONVERGENCE L938 + R3-B EMERGENCE (i) L1465-1494 + Verdict row 11 L1579
Substrate-side derivation pointers:
 - Substrate input: BDI gap protection via Leggett dipolar coupling at the substrate pivot (3He-B-inherited universality class, lab-anchor `lab-si-translation-86-result.md` ν_Δ = 34.146 MHz at Δ/k_B·T_c ≈ 1.96)
 - NCG identity: KO-dim 6 spectral triple + AZ symmetry algebra (TRS · PHS · chiral) selects the BDI representative in the ten-fold-way
 - Direction (substrate-IS-prior): the BDI universality is a SUBSTRATE STRUCTURAL fact; the C1 identity α_s = n_s² − 1 at the substrate pivot is then a JOINT consequence of (i) NCG-axiom uniqueness and (ii) BDI-universality theorem — i.e., the protection theorem is "NCG-axiom + BDI-universality theorem", NOT pure NCG-axiom theorem
Bridge: the C1 identity carries simultaneous single-pole equivalence + K-homogeneity at the pivot u_pivot = 19649/351 because both protections derive from the same BDI universality class.
Status: STRUCTURAL CORRESPONDENCE (not exclusion); registered as a substrate-anchor for the §VII.M three-layer regulator theorem.

## Entry #32 — §VII.M three-layer regulator theorem ↔ Path-H/Path-C two-pathway r ↔ LiteBIRD outcomes

Source: S86 W-2 R3-B EMERGENCE (iv) (mack+connes), workshop `session-86-w2-workingpaper.md` L1547-1563 + Verdict row 11 L1579
Anchors: R2-B CONVERGENCE L885-908 + R3 CONVERGENCE L1135 + R3-B EMERGENCE (iv) L1547-1563
3-LAYER ↔ 2-PATHWAY ↔ 5-OUTCOME MAPPING:

| §VII.M layer | r-pathway | LiteBIRD outcome |
|:-------------|:----------|:-----------------|
| L1 zeta closure | Path-H (transverse-fiber Mellin, c_T = 1) | Outcome 1: r ≈ 0.00745 ± 1σ |
| L3 per-Q span closure | Path-C (longitudinal-compaction Mellin, c_S = c_sub = 2.238) | Outcome 2: r ≈ 0.0117 ± 1σ |
| L2 Zubarev (or third regulator) | path-interpolation | Outcome 3: r between Path-H and Path-C |

Substrate-side derivation pointers:
 - Substrate input: spectral-action regulator choice → pivot-evaluated r amplitude (regulator-non-uniqueness at NLO is a SUBSTRATE STRUCTURAL feature, not an arbitrary scheme choice)
 - n_T = -r/8 invariant in BOTH pathways (single-field substrate consistency); LiteBIRD measurement decides regulator class
Direction (substrate-IS-prior): regulator class is a SUBSTRATE-STRUCTURAL three-fold partition of A_5 at NLO; LiteBIRD is the detector that resolves which of the three the substrate sits in.
Status: STRUCTURAL CORRESPONDENCE (3-element regulator atlas projects onto 5-element observation atlas).


## Entry #33 — 3He-B Volovik 2003 §7-8 dipolar-Leggett ↔ Substrate GGE-acoustic Goldstone universality class

Source: S86 W-2 R3-B EMERGENCE (ii) (mack+volovik), `session-86-w2-workingpaper.md` L1496-1519
Anchors: Re:C1 EMERGES L414 + V3 Q4.3 answer L518 + R3 Q4-C3 L1187 + R3-B EMERGENCE (ii) L1496-1519 + Carry-Forward Priority 1 L1651
Lab anchor: agent-memory `lab-si-translation-86-result.md` — 3He-B at Δ/k_B·T_c ≈ 1.96 with ν_Δ = 34.146 MHz, ratio match 1.13% to substrate K_*

Substrate-side derivation pointers (substrate inheritance from 3He-B universality class is parent → child):
 - 3He-B BDI gap protection ↔ Substrate Goldstone branch K-homogeneity
 - 3He-B spin-tilt running of dipolar excitation ↔ Substrate α_s spectral running at substrate pivot
 - Direction (substrate-IS-prior; lab-anchor reads): the SUBSTRATE inherits the BDI universality class; the lab-anchor is the LABORATORY image of the substrate's BDI structure (parent → child; not analogy)
 - Falsifier: Aalto LTL spin-tilt running measurement at ε² = 0.001 precision (CMB-HD-equivalent) is a lab-analog falsifier of the substrate's universality assignment; failure to find n_s_lab to single-pole precision falsifies BDI inheritance more fundamentally than CMB-S4 sign-test (which only falsifies C1 identity at substrate pivot)
Status: STRUCTURAL CORRESPONDENCE (parent universality class transmitted parent → child via Volovik 2003 §7-8 dipolar-Leggett mechanism).

## Entry #34 — K-homogeneity ODE family `f(u) = 2A/(u-A)` ↔ propagator-class taxonomy I-V

Source: S86 W-2 R3-EMERGENCE-(ii) + R3-FINAL CONVERGENCE Sage-symbolic + Verdict row 10 (mack+connes)
Anchors: `session-86-w2-workingpaper.md` L1219-1239 + L1342-1376 + L1578

5-CLASS PROPAGATOR TAXONOMY (substrate single-effective-pole equivalence at u_pivot):

| Class | ODE-family parameter | Propagator structure | C1 identity status |
|:------|:---------------------|:---------------------|:-------------------|
| I     | A = -1 (single-pole) | literal Goldstone propagator | EXACT (residue ≡ 0 symbolically) |
| II    | degenerate (multi-pole shared (J, m²)) | shared mass + shared coupling | EXACT (residue ≡ 0 symbolically) |
| III   | A ≠ -1                | mathematical-only K-homogeneity ODE solutions | identity holds for any A |
| IV    | independent multi-pole | distinct (J, m²) per pole | identity-breaking at order w_2 · asymmetry; residue = (16/840123) · w_2 leading order at substrate-physical test point |
| V     | running-mass m²(K)    | scale-running propagator | identity-breaking at order γ · u/(1 + u); substrate γ_pivot ~ 4.4e-5 |

Substrate-side derivation pointers:
 - The K-homogeneity ODE `f(u) = 2A/(u-A)` parametrizes a one-parameter ODE family; the SUBSTRATE single-effective-pole equivalence class (Class I/II) is the actual structural anchor at the substrate pivot — Class III is mathematical-only (no substrate physics realizes A ≠ -1 single-effective-pole)
 - R3 EXPLICITLY RETRACTS the R2-A "K-homogeneity ODE family protects identity universally" framing; single-effective-pole equivalence (I+II) is what the substrate physically occupies; Classes IV and V are pre-registered breakage shapes
Direction (substrate-IS-prior): the substrate occupies Class I/II by BDI-protection; Classes III/IV/V are the falsifier-shape inventory.
Status: STRUCTURAL CORRESPONDENCE (taxonomy, not exclusion); 5 classes pre-registered with explicit residue formulas for falsifier-design.

## Entry #35 — Trend-test ↔ Sign-test ↔ Magnitude-test all unified through C1 identity (Closing-Line statement)

Source: S86 W-2 R3-B EMERGENCE (iii) + Closing Line (mack), `session-86-w2-workingpaper.md` L1521-1545 + L1687
3-TEST UNIFICATION (observational sufficiency triad through one structural identity):

| Test type | Detector / data | C1 identity probe |
|:----------|:----------------|:------------------|
| Trend-test | Fairbairn+ data inclusions (ACT+P → ACT+P+SPT → ACT+P+SPT+eBOSS) | direction of α_s drift |
| Sign-test  | CMB-S4 (2028+), σ(α_s) ≈ 2.1e-3 | sign of central value (substrate ceiling 25× below 1σ resolution) |
| Magnitude-test | CMB-HD (2034+), σ(α_s) ≈ 1.1e-3 | magnitude of central + first detection of NLO ε² piece (1.12σ at CMB-HD) |

Substrate-side derivation pointers:
 - All three tests probe the SAME C1 identity α_s = n_s² − 1 at the substrate pivot u_pivot = 19649/351
 - Sign-AND-magnitude lock through C1 identity (no upgrade pathway; same lock); under sign=magnitude lock at the substrate pivot, magnitude-test resolves SIMULTANEOUSLY with sign-test
Direction (substrate-IS-prior): C1 is one substrate identity; trend / sign / magnitude are three independent observational windows ON that identity (closing-line statement: "sign-test, magnitude-test, trend-test resolve simultaneously through one structural identity").
Status: STRUCTURAL CORRESPONDENCE (observational triad unified by single substrate identity).


## Entry #36 — 3He-B → substrate Path-H/Path-C inheritance dictionary (4-row extension to 22-correspondence ledger)

Source: S86 W-3 §V1 + Re:V1 + R2-A DISSENT + R2-B Convergence #1 + R3-B Convergence #2 (gen-physicist)
Anchors: `session-86-w3-workingpaper.md` L41-127 + L428-525 + L1530-1593 + L1984-2027 + L2840-2879
Lab-MCP confirmation: `s44_bcs_tensor_r.py` knowledge-MCP — "Longitudinal sound = phonon = scalar perturbation"; "Transverse sound = order parameter collective mode = tensor"

5-ROW PATH-H/PATH-C INHERITANCE DICTIONARY (extends existing 22-correspondence framework-3heb-comparison.md ledger):

| 3He-B (parent) | Substrate (child; inheritance arrow) | Pathway label |
|:---------------|:--------------------------------------|:--------------|
| 3He-B longitudinal δρ_s/ρ_s (BDI J=0 condensate, first sound c_1) | substrate B1 eigenvalue cluster, c_S = c_sub = 2.238 | Path-C (longitudinal-compaction Mellin) |
| 3He-B transverse OP collective mode (second sound c_2) | substrate B2 eigenvalue cluster, c_T = 1 | Path-H (transverse-fiber Mellin) |
| 3He-B SU(2)_J quench at T_c | substrate SU(3) → BCS-on-SU(3) quench at fold | both pathways' parent transition |
| 3He-B BDI symmetry class | substrate BDI symmetry class (preserved per S60 framework-3heb-comparison.md) | both pathways inherit BDI |
| Lab-MCP confirmation row | s44_bcs_tensor_r.py mapping: longitudinal=phonon=scalar; transverse=OP-collective=tensor | bidirectional confirmation |

Substrate-side derivation pointers (parent → child inheritance, NOT analogy):
 - 3He-B is the parent universality class; the substrate's two pathway labels (Path-H, Path-C) are CHILD images of the 3He-B first-sound / second-sound channel split
 - The lab-MCP confirmation row is bidirectional: 3He-B confirms substrate pathway labeling; substrate's spectral-action moments give back the BCS-tensor-r structure to 3He-B at the universality-class level
Direction (substrate-IS-prior in registry semantics): the SUBSTRATE structure is what is registered; 3He-B is the lab-anchor that mirrors it under the parent → child inheritance arrow
Status: STRUCTURAL CORRESPONDENCE (4-row + 1-confirmation extension; brings ledger to 26 correspondences total).

## Entry #37 — K_7 + Mermin-Ho compound analog (Pillar III refined; 4-row compound block)

Source: S86 W-3 §V3 + Re:V3 + R2-A Q-CN-5 + Workshop Verdict row 3 (gen-physicist)
Anchors: `session-86-w3-workingpaper.md` L232-316 + L628-766 + L1905-1916 + L3171

4-ROW COMPOUND-ANALOG BLOCK (Pillar III dual-projection refined; supplies SHAPE+LABELING for the Path-H/Path-C dual-valuedness):

| 3He-A | Substrate analog | Channel role |
|:------|:------------------|:-------------|
| 3He-A K_7 invariant (orbital `l̂`, K_7-charged) | K_7-charged BCS-on-SU(3) condensate (per `dipolar-catalog-49-result.md`, 7/8 generators K_7-charged) | parent quantum number |
| 3He-A transverse `l̂` projection (orbital vorticity) | substrate B2 transverse-fiber projection | Path-H |
| 3He-A longitudinal `l̂` projection (spin-vector vorticity) | substrate B1 longitudinal-compaction projection | Path-C |
| 3He-A Mermin-Ho relation ∇ × v_s ∝ l̂ · (∇l̂ × ∇l̂) | substrate spectral-action partition (∂a_4/∂h^TT)_α=1,2 | identity at L_max=10 |

Substrate-side derivation pointers:
 - The K_7 + Mermin-Ho compound is the lab-projection of the SUBSTRATE's intrinsic dual-projection structure ∂a_4/∂h^TT at α=1 vs α=2
 - 7/8 of the SU(3) generators carry K_7 charge per the `dipolar-catalog-49-result.md` registry; the unique K_7-zero generator is the Cartan-hypercharge channel
Direction (substrate-IS-prior): the substrate's spectral-action partition produces the K_7 + Mermin-Ho compound at the lab projection; 3He-A is the laboratory mirror.
Status: STRUCTURAL CORRESPONDENCE (compound 4-row, refining Pillar III row of `framework-3heb-comparison.md`).

## Entry #38 — Cross-pillar ranking refinement table (Pillar I/II/III/IV substrate-analog quality)

Source: S86 W-3 §V3 + Re:V3 + R2-A Convergence #3 (gen-physicist)
Anchors: `session-86-w3-workingpaper.md` L304 + L758-766 + L1523

4-PILLAR CROSS-CHECK RANKING (refined statuses):

| Pillar | 3He-A observable | Multi-valuedness type | Substrate analog quality |
|:-------|:------------------|:----------------------|:--------------------------|
| I      | 3He-A chiral anomaly N_3 | integer (topological) | EXCLUDED — BDI 0D class, N_3 = 0 per S44 |
| II     | Hopf charge π_3(SU(2)) | integer (topological) | INFORMATIVE on what r LACKS — no integer winding in r |
| III    | Mermin-Ho / K_7 texture | continuous (spectral-block) | CLEANEST ANALOG — matches B1/B2; K_7+Mermin-Ho compound supplies SHAPE+LABELING (see Entry #37) |
| IV     | Peotta-Törmä flat-band g_FS | quantum-metric (Berry) | NEUTRAL — S64 PROVEN inapplicable to CC; same closure here for r |

Substrate-side derivation pointers:
 - Pillar III is the CLEANEST analog because the spectral-block multi-valuedness shape matches the substrate's B1/B2 dual cluster, which is the IMAGE of the substrate spectral-action's dual-projection structure
 - Pillar I excluded by S44 BDI 0D class constraint; Pillar IV blocked by S64 cross-domain closure (g_FS uniqueness on Bloch fiber bundle does NOT constrain D_K^2 block decomposition under NCG axioms)
Direction (substrate-IS-prior): the substrate's structural identity assigns each pillar a quality grade; the table is read FROM substrate OUTWARD (not as "the substrate looks like Pillar III").
Status: STRUCTURAL CORRESPONDENCE (cross-pillar ranking; canonical ledger for r-prediction analog quality).


## Entry #39 — Cross-pillar 3-channel taxonomy correspondence (NEEDS-ORCHESTRATOR-FOLLOWUP)

Source: S86 W-4 §L3 BCS-channel taxonomy block + §A5 + Wrap-Up §"What Holds" (connes+lizzi)
Anchors: `session-86-w4-workingpaper.md` L547-608 + L807 + L1616
Status pending: STRUCTURAL or GENUINE pending Level 1 theorem proof closure (S87-CROSS-PILLAR-3-CHANNEL-THEOREM-PROOF, ~1 session)

3-CHANNEL CROSS-DOMAIN TAXONOMY (Bogoliubov-pair-conservation kinematics produces a 3-channel invariant across pillars):

| Channel | Pillar III BCS | Pillar II f_NL_folded | Pillar IV Leggett |
|:--------|:---------------|:----------------------|:------------------|
| 1       | Cooperon-vertex (3-pt-connected) | Pathway A (in-in formalism, L_J-Laplacian-dressed) | scalar Leggett channel |
| 2       | Bogoliubov-cumulant (pair-cumulant) | Pathway B (Type-S co-coordinate on N_pair_eff) | scalar Leggett channel |
| 3       | Andreev-template (2-pt-separable) | Pathway C (Type-S co-coordinate on N_pair_eff, Mellin-cone-protected) | scalar Leggett channel |

Substrate-side derivation pointers (substrate-IS-prior cross-domain bridge):
 - The substrate's Bogoliubov-pair-conservation kinematics is what produces the 3-channel invariant; the channels are SUBSTRATE STRUCTURAL, not pillar-specific accidents
 - The cross-pillar invariance is pre-registered as a Level-1 theorem candidate; PASS criterion: 3-sector basis matrix in A_F⊗A_M has rank=3 to machine precision at L_max=10
 - INFO outcomes: rank=2 (degeneracy) or rank≥4 (additional sectors)

(NEEDS-ORCHESTRATOR-FOLLOWUP) Classification — STRUCTURAL vs GENUINE — depends on the S87 Level-1 theorem closure outcome. If the rank=3 condition holds, the entry promotes to GENUINE; if rank=2 or rank≥4, the entry classification is REVISED. Registry slot reserved; status to be updated post-S87 CF-1 verdict.

## Entry #40 — In-in formalism / Schwinger-Keldysh closed-time-path correspondence (NEEDS-ORCHESTRATOR-FOLLOWUP)

Source: S86 W-4 §R2-B EMERGENCE #3 cross-citation + §R3-A CONVERGENCE #6 (connes+lizzi)
Anchors: `session-86-w4-workingpaper.md` L1042-1048 + L1175-1197

Substrate-side derivation pointers (substrate IS-prior; in-in is canonical for the substrate, not chosen):
 - The substrate has NO asymptotic free state — there is no in/out vacuum to define an in-out S-matrix; permanent non-equilibrium is a SUBSTRATE STRUCTURAL property of the GGE relic
 - The Schwinger-Keldysh closed-time-path canonical formalism is forced ON the substrate by the absence of asymptotic spacetime; it is not chosen for convenience
 - The substrate-IS-space picture forces in-in canonical formalism by NCG axioms (R3-A CONVERGENCE #6 line 1175); this is the formalism-class axis of the rank-2 product detector orthogonality

Bridge: substrate's permanent non-equilibrium parallels Schwinger-Keldysh canonical formalism for non-equilibrium QFT — formalism-class shared, not analogy.

(NEEDS-ORCHESTRATOR-FOLLOWUP) Likely STRUCTURAL classification (formalism-class shared with Schwinger-Keldysh by NCG-axiom force, not by analogy). Final classification depends on whether the substrate-IS-canonical axis of §VII.O / §VII.O.1 / §VII.O.0 entry trio lands in S87 (Level 1 theorem closure dependency).

## Entry #41 — Substrate-vs-detector projection asymmetry pattern (TWO-DIRECTION dual; NEEDS-ORCHESTRATOR-FOLLOWUP)

Source: S86 W-4 §R3-B EMERGENCE #4 cross-citation (connes+lizzi)
Anchors: `session-86-w4-workingpaper.md` L1567-1570

TWO-DIRECTION DUAL (cross-cutting framework architecture pattern):

| Direction | Substrate side | Detector side |
|:----------|:---------------|:--------------|
| (A) detector defines canonical | substrate is coarse-grained relative to detector channel structure | S77 r_AB pattern: detector-canonical observable splits into substrate-coarse projections |
| (B) substrate richer than detector resolves | substrate has structural axes (e.g. Type-F per-mode {phi_a}) detector cannot read | S86-W4 Type-F invisibility: per-mode phase information detector-invisible on current horizon |

Substrate-side derivation pointers (substrate-IS-prior in BOTH directions of the dual):
 - Direction (A): the substrate is the same in both pictures; the detector channel structure is a coarse-graining function ON the substrate (substrate-IS-prior; detector is the projection)
 - Direction (B): the substrate carries structural axes (per-mode {phi_a}, formalism-class, regulator-class) the detector cannot resolve at finite precision; Type-F observables are detector-invisible-on-current-horizon, NOT substrate-invisible
 - Both directions preserve substrate-IS-prior; the asymmetry is between substrate's intrinsic structure and detector's projection capability

(NEEDS-ORCHESTRATOR-FOLLOWUP) Cross-cutting framework architecture pattern; classification (STRUCTURAL vs PARADIGMATIC) depends on whether the §VII.P Type-F/Type-S Cross-Pillar Atlas lands in S87 (Level-4 carry-forward, post-Level-1).


## Entry #42 — Pillar III HP^1 cohomology ↔ Pillar IV Peotta-Törmä quantum-metric trace (cross-pillar bridge theorem)

Source: S86 W-5 V4 bridge theorem statement + Re:V4 EMERGES + Closing Line (volovik+connes)
Anchors: `session-86-w5-workingpaper.md` L319-322 + L723-725 + L2671
Provenance: T6 anchor at `session-86-w1b-workingpaper.md:151`; W5-6 INFO-tight verdict `s85_gate_verdicts.txt:163`; CF-1 registry-landing
Status: PASS-UNCONDITIONAL (three-level ladder: Level 1 cohomology-class identity / Level 2 L^{-3} envelope at d=4 / Level 3 empirical 0.0095% F_4 strict 10× inside envelope)

CROSS-PILLAR BRIDGE:

| Side | Observable | Spectral-triple location |
|:-----|:-----------|:-------------------------|
| Pillar III (LEFT) | `‖[ε_H]‖_{HP^1, r}` (HP^1 cohomology norm, regulator r ∈ Atlas_5) | substrate finite-L Hochschild pairing |
| Pillar IV (RIGHT) | `R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k` (Peotta-Törmä quantum-metric trace on Jensen-deformed band-0) | continuum BZ-trace via L → ∞ HKR image |

Bridge identity: `‖[ε_H]‖_{HP^1, r} = |f_4^r| · R_universal` where R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩ is the regulator-invariant Connes-Karoubi pairing.

Substrate-side derivation pointers:
 - Substrate IS the finite-L Hochschild pairing; the laboratory IS the continuum BZ-trace via L → ∞ HKR (Hochschild-Kostant-Rosenberg) image
 - The bridge identity is regulator-CONDITIONAL via |f_4^r|; R_universal is regulator-INVARIANT
 - three-level verification ladder: Level 1 cohomology-class identity (algebraic), Level 2 L^{-3} envelope at d=4 (asymptotic), Level 3 empirical 0.0095% F_4 strict (10× inside envelope)
Direction (substrate-IS-prior): the substrate's finite-L Hochschild pairing is structurally prior; the BZ-trace is the laboratory image at L → ∞.
Status: STRUCTURAL CORRESPONDENCE (PASS-UNCONDITIONAL three-level).

## Entry #43 — Substrate ker(ι_*) HP^* generators ↔ 3He-B BdG-sector NULL falsifiers (5-row × 4-gate)

Source: S86 W-5 V3 5-row table + C2 confirmation + R3-7 decisive triplet + Q4-FINAL gate-structure (volovik+connes)
Anchors: `session-86-w5-workingpaper.md` L293-300 + L976-986 + L2027-2029 + L2243-2247
Provenance: §V3 + §C2 + §R3-C; CF-2 + CF-3 lab-falsifier pre-registrations

KER(ι_*) HP^* GENERATORS ↔ 3He-B BdG-SECTOR ABSENCES (5-row × 4-gate structure):

| Substrate ker(ι_*) HP^2 generator | 3He-B BdG-sector observable | Substrate prediction | Falsifier signature |
|:-----------------------------------|:-----------------------------|:---------------------|:--------------------|
| [φ_67] (chiral pair, Hochschild cocycle) | F1: vortex-core Caroli-Matricon ladder asymmetry | NULL | φ_67-style Im/Re Bogoliubov off-diagonal |
| [φ_67] (chiral pair) | F2: SABS axial-equatorial off-diagonal | NULL | φ_67 cocycle-clean signature |
| [φ_67] (chiral pair) | F3: HQV splitting in restricted geometry | NULL | φ_67 supporting |
| [φ_88] (Cartan hypercharge, Jensen-rate-limited) | F4: hypercharge-twist Larmor anomaly | NULL | φ_88 supporting (cocycle-degenerate at fixed (p,T)) |
| [φ_88] (Cartan hypercharge) | F5: acoustic-mode dispersion offset under Jensen-modulus quench | NULL | φ_88 cocycle-clean signature |

Bridge: ι : (A_He, H_He, D_BdG) → (A_K, H_K, D_K); χ : C ⊕ H ⊕ M_3(C) → M_2(C) sending M_3(C) → 0; ker(ι_*) = full (τ, k)-mixed block.

Substrate-side derivation pointers (substrate-first reading per R3-8):
 - 3He-B carries NO Jensen-direction degree of freedom; the substrate's ker(ι_*) HP^2 generators are SUBSTRATE STRUCTURAL features the lab cannot natively read
 - Substrate prediction is NULL on all 5 F-rows (kernel signature) — i.e., 3He-B should NOT exhibit the substrate-internal HP^2 cocycle structure
 - Cross-cocycle ratio prediction = 7.3250 ± 0.1% on any non-NULL detection (cohomology-asymmetry test); pre-registered via W11-C5/C6 four-gate structure
Direction (substrate-IS-prior): the substrate's HP^2 cohomology is structurally prior; 3He-B is the lab platform that PROBES the kernel signature by attempting to detect what is structurally absent.
Status: STRUCTURAL CORRESPONDENCE (5-row falsifier table; substrate prediction is NULL; non-NULL detection would carry cross-cocycle ratio 7.3250).


## Entry #44 — T6 ↔ T7 ↔ S67 joint spectroscopic identity (three-wall correspondence; dual-hex Josephson plaquette structure)

Source: S86 W-6 §E-L-R3-1 + §C-V-R3-2 + Wrap-Up §"What Changed" (lizzi+volovik)
Anchors: `session-86-w6-workingpaper.md` L1700-1740 + L1900-1936 + L2188

THREE-WALL CORRESPONDENCE:

| Source | Spectroscopic face | Substrate amplitude / count |
|:-------|:-------------------|:----------------------------|
| T6 (HP^1 Near-Invariance, §VII-B, S86 W1b) | AMPLITUDE | r_HP1 = k_link × (1 − δ_SDW) |
| T7 (Two-Layer Obstruction, §VII-B, S86 W1b) | COUNT | n_joint = frustrated-cycle count |
| S67 (Frustration Triangle, `proven_1738`, S66) | HALF-QUANTUM | n_p = 1/2 per S_3-orbit corner |

Underlying substrate object: dual-hex Josephson-array plaquette-cycle structure with cluster-restricted Mellin support (triangular tile k_link=3 for F_4; hexagonal tile k_link=6 for M).
Quotient operator: cyclic fold (acts identically on all three faces; 6-link hexagonal → 3-link triangular for amplitude, 6-conjunct categorical → 3-axis for count, 3 Z_2-corners → Z_3 cyclic gauge sector for half-quantum).

Substrate-side derivation pointers:
 - The substrate IS the dual-hex Josephson plaquette structure; T6, T7, S67 are three spectroscopic projections of the same substrate object
 - Cyclic-fold quotient acts identically across all three faces — this is the structural reason the three walls converge at quotient-isomorphism
 - Status: PASS-quotient-isomorphism, residual 0.0095% on Python-verified anchor
Direction (substrate-IS-prior): the substrate's plaquette-cycle structure is the primary object; T6/T7/S67 are three lab-spectroscopic windows on it.
Status: STRUCTURAL CORRESPONDENCE (three-wall converged at quotient-isomorphism residual 0.0095%).

## Entry #45 — F_4 ↔ triangular tiling, M ↔ hexagonal tiling, C28 ↔ tile-decomposition invariance

Source: S86 W-6 §V3 + §C4 (lizzi convergence) + Wrap-Up Verdict row 6 (lizzi+volovik)
Anchors: `session-86-w6-workingpaper.md` L746-882 + L964-967 + L2157
Cross-anchor: registry §VII-B L2939-2945

REGULATOR-CLASS ↔ TILING CORRESPONDENCE:

| Regulator class | Tiling | k_link | Mellin support |
|:----------------|:-------|:-------|:----------------|
| F_4 = {ζ, Zubarev, SDW} | triangular tiling of dual-hex | 3 | pure-a_4 |
| M = {cutoff_sqrt, anomaly} | hexagonal tiling | 6 | mixed-Mellin {a_0, a_2, a_4, a_6} |
| C28-invariance signature | wall persists across F_4 alone OR M alone | — | tile-decomposition invariant |

C28-invariance ↔ topological-quantization signature under tile-decomposition (analog of Chern-number tile-independence in lattice gauge theory).
Decomposition: n_joint = 0/5 = (0/3 triangular) + (0/2 hexagonal).

Substrate-side derivation pointers:
 - The regulator atlas A_5 partitions structurally into F_4 and M by tile geometry (triangular vs hexagonal)
 - The C28-invariance signature is the substrate's tile-decomposition invariance — analogous to Chern-number tile-independence but at the regulator-class level
 - Mellin support is determined by tile geometry: triangular tiles support pure-a_4; hexagonal tiles support mixed {a_0, a_2, a_4, a_6}
Direction (substrate-IS-prior): the substrate's plaquette tile geometry is what classifies the regulators; the regulator atlas A_5 = F_4 ∪ M is the lab-projection of the tile classification.
Status: STRUCTURAL CORRESPONDENCE (regulator-tile classification; cited in registry §VII-B L2939-2945).


## Entry #46 — Class-protected Bogoliubov ledger principle ↔ Bogoliubov coefficient unitarity (|α|² − |β|² = 1)

Source: S86 W-9 §Re:L4 §1 + §A-T4.4 (mack+lizzi)
Anchors: `session-86-w9-workingpaper.md` L612-620 + L1184-1189

CROSS-AXIS BRIDGE (spectral-functional ↔ transit-dynamics):

| Side | Object | Conservation form |
|:-----|:-------|:------------------|
| Spectral-functional moment ledger | A_s = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub^{-1}·f_conv | per-branch class-protected multiplicative ledger |
| Transit-dynamics Bogoliubov | (α, β) coefficients | unitarity |α|² − |β|² = 1 |

Substrate-side derivation pointers:
 - The substrate's per-branch protection in the multiplicative A_s ledger is the SPECTRAL-FUNCTIONAL ANALOG of the unitary conservation law for transit Bogoliubov coefficients
 - Each multiplicative factor (H̃²/8π², 1/ε_H, F_amp, c_sub^{-1}, f_conv) is class-protected on its own branch — the ledger structure mirrors the per-mode |α|² − |β|² = 1 invariance
 - Both invariants are cosmological: they constrain how transit physics couples to the observable scalar amplitude
Direction (substrate-IS-prior): the substrate's spectral-functional ledger is structurally prior; Bogoliubov-unitarity is the transit-dynamics image at the lab projection.
Status: STRUCTURAL OR GENUINE entry (cross-axis bridge: spectral-functional moment ledger ↔ transit-dynamics Bogoliubov coefficient framework).

## Entry #47 — Mellin residue at substrate-distance-1 pole ↔ Bogoliubov backreaction-onset N (per-R)

Source: S86 W-9 §T-CR2.5 (transit+mack)
Anchors: `session-86-w9-workingpaper.md` L1387-1430

PROJECTION MAPPING:

| Side | Object | Truncation level |
|:-----|:-------|:------------------|
| Spectral-class | Mellin residue at substrate-distance-1 pole | finite-L Mellin moment |
| Dynamical-class | per-R Bogoliubov backreaction-onset N_back,R | per-regulator backreaction-onset N |

Substrate-side derivation pointers:
 - The new observable N_breakdown_observable(R) per E-R2.1 IS the SR-LO image of N_back,R, projected through the SR-LO truncation
 - The mapping is per-R (regulator-resolved): each regulator class in A_5 maps to a separate Mellin residue → Bogoliubov backreaction-onset pair
 - E-R2.1 N_breakdown_observable IS the SR-LO image (not similar to, not analogous to) — projection identity at the SR-LO truncation level
Direction (substrate-IS-prior): the substrate's Mellin residue is structurally prior; the backreaction-onset N is the transit-dynamics projection through SR-LO truncation.
Status: STRUCTURAL CORRESPONDENCE (spectral-class projection ↔ dynamical-class projection mapping).

## Entry #48 — Spectral 3-class partition ↔ Dynamical 4-class breakdown anti-correlation at s=3

Source: S86 W-9 §Re:L2 + §C-R2.3 + §T-CR2.2 (lizzi+transit)
Anchors: `session-86-w9-workingpaper.md` L503-532 + L968-1004 + L1249-1289
Pole-scoping: s=3 SPECIFIC (NOT general); resolution-scoping: 4-class A_5 projection (NOT 5-class atlas)

POLE-SPECIFIC SPECTRAL-DYNAMICAL DUALITY:

| Side | Partition | Cardinality |
|:-----|:----------|:------------|
| Spectral | A_5 regulator atlas at s=3 pole | 3-class partition |
| Dynamical | A_5 breakdown classification at 4-class projection | 4-class breakdown |

Anti-correlation: rank-monotonic at the 4-class projection of A_5; Spearman |ρ_S| = 1.0 EXACT.

Substrate-side derivation pointers (pole-scoping and resolution-scoping MANDATORY per source):
 - The 3-class spectral partition exists ONLY at the s=3 pole; other poles in the Mellin strip do NOT exhibit this partition
 - The 4-class dynamical projection is at the A_5 atlas resolution; 5-class (full atlas) projection does NOT preserve the EXACT |ρ_S| = 1.0
 - Anti-correlation is rank-monotonic (Spearman, not Pearson) — the spectral and dynamical orderings of A_5 regulators are EXACTLY reversed at this pole-resolution combination
Direction (substrate-IS-prior): the substrate's Mellin pole structure carries the spectral 3-class partition; the dynamical 4-class breakdown is the transit-projection at the same A_5 resolution.
Status: STRUCTURAL CORRESPONDENCE (pole-specific s=3, resolution-specific 4-class; |ρ_S| = 1.0 EXACT only at this projection).


## Entry #49 — ρ_∞^{Zubarev} ↔ eta-invariant signature density correspondence

Source: S86 W-10 Re:L2 closing + R2-B DISSENT item 2 + R3-A CONVERGENCE #5 + R3-B EMERGENCE E1 (connes+lizzi)
Anchors: `session-86-w10-workingpaper.md` L565-566 + L1402-1433 + L1742 + L2131-2183
Cross-references: existing `eta_invariant` constant (`s60_eta_invariant.py` provenance) and `w0_cc1_eta_invariant` constant (`s85_w0_cc1_eta_invariant.py` provenance)

CORRESPONDENCE:

| Side | Observable | Spectral location |
|:-----|:-----------|:-------------------|
| L2 emission (substrate) | ρ_∞^{Zubarev} ≈ −0.8104 | s = −1 (fermionic-signed-residue) |
| Eta-invariant analog | eta-invariant signature density at Jensen-fold slice (chiral-anomaly density) | s = −1 (KO-dim 6 mod 8) |

Substrate-side derivation pointers (both are spectral observables of D_K at the SAME location):
 - Both observables sit at s = −1 in the Mellin strip; KO-dim 6 mod 8 selects the fermionic-signed-residue location
 - ρ_Zubarev evaluates the L2 weighted ratio at this location
 - eta-invariant analog evaluates the L1 zeta-regularized signed Mellin moment at the same location
 - The numerical alignment (ρ_∞^{Zubarev} ≈ −0.8104) is a substrate fact pinned by W10 workshop, not a coincidence
Direction (substrate-IS-prior): the substrate's D_K spectrum at s = −1 produces both observables; ρ_Zubarev and eta-invariant signature density are two regulator-class projections of the same substrate location.
Status: STRUCTURAL CORRESPONDENCE (READY-TO-INSTALL; same-location observable-pair at s = −1 fermionic residue).

## Entry #50 — Bosonic L3-composite ↔ Fermionic L2-direct sectoral duality (KO-dim 6 mod 8 mediated)

Source: S86 W-10 R3-B EMERGENCE E1 (connes+lizzi)
Anchors: `session-86-w10-workingpaper.md` L2131-2183

KO-DIM 6 MOD 8 BOSONIC-FERMIONIC SECTORAL DUALITY (across the corridor):

| Sector | Pathway | Emission character | Companion structure |
|:-------|:--------|:--------------------|:---------------------|
| Bosonic L3-composite | A_s | RATIONAL (with Γ(integer)/Γ(half-integer) candidates) | composite Mellin moments |
| Fermionic L2-direct | ρ | IRRATIONAL (with eta-invariant analog at s = −1) | direct Mellin signed-residue |

Mediation: KO-dim 6 mod 8 mediates via:
 - Sd_bos integer-poles (bosonic spectral data set)
 - Sd_ferm signed-residue locations (fermionic spectral data set)
 - half-integer Mellin moments at s_eff = (KO-dim − 1)/2 · 2 = 11/2 as bridge

Substrate-side derivation pointers:
 - The substrate's KO-dim 6 mod 8 structure is what produces the bosonic-fermionic sectoral split
 - Bosonic emission is RATIONAL because composite Mellin moments at integer poles compose rationally; fermionic emission is IRRATIONAL because the signed residue picks up half-integer Mellin moment companions
 - The bridge at s_eff = 11/2 connects the two sectors via the half-integer Mellin location pre-registered in §VII.M
Direction (substrate-IS-prior): the KO-dim 6 mod 8 structure is the substrate's structural feature; the bosonic-fermionic emission split is the lab-projection of this structural duality.
Status: STRUCTURAL CORRESPONDENCE (structural pattern recognition; not new mechanism; pattern emerges from KO-dim 6 mod 8 mediation).


## Entry #51 — HP^*(A_F) parity grading ↔ NCG-classical-gravity correspondence (canonical NCG echo of even Chern/Pontryagin classes blind to torsion)

Source: S86 W-11 §"What Holds" item 1 + §4 item 1 + §"Cross-paradigm parallel" (gen-physicist)
Anchors: `session-86-w11-workingpaper.md` L237 + L171 + L176 (citing `elimination-bulletins.md:75`)

PARITY-GRADING CORRESPONDENCE (HP^* on cyclic cohomology RESPECTED by D_K on Jensen-deformed SU(3) at L_max=10):

| HP^* parity | Substrate coupling | NCG-classical-gravity analog |
|:------------|:--------------------|:------------------------------|
| Even cyclic cocycles | even Seeley-DeWitt moments + η (s=0 residue of even-grading Mellin moment) | even Chern / Pontryagin classes (blind to torsion) |
| Odd cyclic cocycles | GV (transgression of first Pontryagin class on the foliation) | odd-degree secondary classes (η-Cheeger-Simons, Godbillon-Vey) recover torsion / secondary information |

Substrate-side derivation pointers:
 - W-11 establishes the HP^* parity grading on cyclic cohomology is RESPECTED by D_K on Jensen-deformed SU(3) at L_max=10 in the strongest sense — no parity violations across the substrate's spectrum
 - Even cocycles couple to even Seeley-DeWitt moments + the η contribution from the even-grading Mellin moment at s=0
 - Odd cocycles couple to GV (Godbillon-Vey transgression of first Pontryagin class on the foliation)
 - This is the canonical NCG echo of the classical fact that even Chern/Pontryagin classes are blind to torsion / secondary information that odd-degree secondary classes (η-Cheeger-Simons, Godbillon-Vey) recover
Direction (substrate-IS-prior): the substrate's HP^* parity grading on cyclic cohomology is structurally prior; the classical-bundle even/odd Chern-Pontryagin/secondary-class structure is the lab-image of this NCG-cohomological parity.
Status: STRUCTURAL CORRESPONDENCE (canonical NCG echo of even Chern/Pontryagin classes' torsion-blindness; HP^* parity ↔ classical-bundle even/odd structure).


## Entry #52 — 3He-B at first-order Bogoliubov cusp ↔ Substrate D_K at τ_fold (universality-class match, refined; layered classification)

Source: S86 W-12 V1 + Q1 R1-volovik response + "Workshop Verdict" topic 4 (connes+volovik)
Anchors: `session-86-w12-workingpaper.md` L602-610 + L391-393 + L1686
Cross-anchor: `framework-3heb-comparison.md` (one of 22 inheritance correspondences per S60)

REFINED 5-ROW UNIVERSALITY-CLASS MATCH (sharpening of existing 3He-B inheritance correspondence):

| Superfluid (3He-B at first-order) | Substrate (D_K at τ_fold) | Status |
|:----------------------------------|:--------------------------|:------:|
| BdG dispersion branch cut at gap edge | Mellin-cone residue strip (Axis_M) | STRUCTURAL |
| Gauge-rotation Z_2 (Δ → -Δ) | W6-3 conformal-end Z_2 (flat ↔ dS) | STRUCTURAL |
| Maxwell-construction phase coexistence | V_4 coset partition of regulator atlas | STRUCTURAL |
| Andreev bound states between gap and 2Δ | Bottom-20 strata in [x_gap, x_PV] = [0.2155, 1.0] | STRUCTURAL |
| 4-stratum Andreev multiplicity (BdG-doubled) | (2, 4, 8, 6) bare-stratum cardinality | STRUCTURAL (universality match, NOT representation-theoretic) |

Anti-correspondence (per R1-volovik response Q1 L391-393):
 - Multiplicity 4 in 3He-B emerges from chirality × parity (different group-theoretic origin)
 - Substrate's 4 emerges from SU(3) Casimir branching
 - Same cardinality (4 strata), different group-theoretic origin — universality-class match (4-stratum discrete Andreev structure at first-order cusp), NOT representation-theoretic identity

Substrate-side derivation pointers:
 - The substrate's D_K at τ_fold sits at a first-order Bogoliubov-cusp universality class (5-row match across BdG/gauge/Maxwell/Andreev/multiplicity dimensions)
 - The match is UNIVERSALITY-CLASS level, not representation-theoretic — the cardinality alignment (4 = 4) is forced by the universality class but the group-theoretic origins are distinct
Direction (substrate-IS-prior): the substrate's spectral-triple structure at τ_fold is structurally prior; the 3He-B first-order cusp is the lab analog at the same universality class.
Status: STRUCTURAL CORRESPONDENCE (refined 5-row + 1-anti-correspondence row; layered classification required to maintain the universality-vs-representation distinction).

## Entry #53 — BdG-Nambu doubling ↔ NCG Axiom 5 reality structure `[J,D_K]=0`

Source: S86 W-12 Re:C1 (R1-volovik) + CONVERGENCE 1 (R2-connes) + "What Holds" (connes+volovik)
Anchors: `session-86-w12-workingpaper.md` L359-361 + L776-777 + L1737

EQUIVALENCE:

| Side | Structure | Spectral signature |
|:-----|:----------|:-------------------|
| BdG-Nambu doubling | H_BdG = τ_3 ⊗ H_normal + τ_1 ⊗ Δ | spectrum {±E_k} symmetric about zero; every excitation level above gap edge appears in pairs |
| NCG Axiom 5 reality structure | J implements particle-hole conjugation; `[J, D_K] = 0` | every λ has J-conjugate −λ; bottom-20 |λ|-strata come in even multiplicities |

Substrate-side derivation pointers:
 - The strict evenness of the (2, 4, 8, 6) bare-stratum cardinality is the BdG-Nambu doubling signature, NOT coincidence
 - This is a CONSEQUENCE of the S43 PROVEN result `[J, D_K] = 0` applied to the Jensen-deformed SU(3) Dirac operator
 - The substrate-superfluid identification is FORCED by NCG-axiom 5 reality, not chosen as a tunable analogy
Direction (substrate-IS-prior): the NCG Axiom 5 reality structure is the substrate-axiomatic prior; BdG-Nambu doubling is the lab-side image of `[J, D_K] = 0`.
Status: GENUINE / FORCED CORRESPONDENCE (substrate-superfluid identification is a CONSEQUENCE of NCG-axiom 5 reality, not a tunable analogy).

## Entry #54 — Local-vs-global axis decomposition ↔ Connes-Marcolli (2007) §1.17 separation

Source: S86 W-12 EMERGENCE E-3 (R2-A) + CONVERGENCE C-4 (R3-A) (connes+volovik)
Anchors: `session-86-w12-workingpaper.md` L918-955 + L1280

V_4 = Z_2(LOCAL) × Z_2(GLOBAL) ABELIAN PRODUCT DECOMPOSITION:

| Axis | Z_2 sector | Spectral content |
|:-----|:------------|:------------------|
| Axis_M | LOCAL UV / heat-kernel-coefficient sign convention | Wodzicki-residue / a_4 contribution |
| Axis_C | GLOBAL IR / asymptotic-completion topology selector | ℐ⁺ class |

Structural independence: local data does NOT fix global completion; global completion does NOT fix local data — the two axes are structurally orthogonal.

Substrate-side derivation pointers:
 - V_4 is the abelian product of one local + one global involution (Klein-four group structure)
 - Connes-Marcolli (2007) §1.17 separates local spectral-action computation (Seeley-DeWitt expansion) from global completion (choice of asymptotic regime); the W-12 5-step REGULATOR-MONODROMY-AXIS-DECOMPOSITION methodology IS that separation applied to regulator-monodromy enumeration
 - This methodology-bridge entry registers the local/global structural independence as a NEW correspondence (not an existing 3He-B inheritance row)
Direction (substrate-IS-prior in the methodology-bridge sense): the substrate's V_4 = Z_2(local) × Z_2(global) decomposition is the substrate-structural prior; the Connes-Marcolli separation is the methodology-bridge image at the spectral-action / asymptotic-completion level.
Status: STRUCTURAL CORRESPONDENCE (methodology-bridge entry; new addition to registry; classifies the W-12 5-step regulator-monodromy-axis-decomposition methodology as the application of Connes-Marcolli §1.17 to monodromy enumeration).


## Entry #55 — Substrate ↔ methodology layer-functor F (10-mapping enumeration)

Source: S86 W-13 §C2-EM-2 + §C3-CONN-DIS-1 (connes+lizzi)
Anchors: `session-86-w13-workingpaper.md` L1396-1397 + L2185-2186
Cross-reference: `epistemic-discipline.md §"Layer-Decomposition"` (RULE-2)

LAYER-FUNCTOR F (substrate ↔ methodology pair, 5 mappings; methodology ↔ audit pair, 5 mappings):

| F-image domain | F-image codomain | Mapping count |
|:----------------|:-------------------|:---------------|
| substrate | methodology | 5 mappings (5-mapping enumeration at substrate ↔ methodology pair) |
| methodology | audit | 5 mappings (5-mapping enumeration at methodology ↔ audit pair) |

Substrate-side derivation pointers:
 - The substrate is the categorical-source object; methodology is the F-image codomain (5 distinct mappings F: substrate → methodology pinned in source)
 - Methodology is itself the source for a downstream F-image to audit (5 distinct mappings F: methodology → audit pinned in source)
 - The triplet (substrate, methodology, audit) is canonical; the F functor is the shared structural map across both pairs
 - Cross-reference RULE-2 in `epistemic-discipline.md §"Layer-Decomposition"` (registers the layer-decomposition principle that justifies the F-functor architecture)
Direction (substrate-IS-prior in the layer-functor sense): the substrate occupies the categorical source; methodology and audit are F-images at successive layers; F preserves the structural skeleton across the chain.
Status: STRUCTURAL CORRESPONDENCE (READY-TO-INSTALL; content fully specified by C2-EM-2 + C3-CONN-DIS-1; source-pin: workshop SHA at R3 closure).

## Entry #56 — Substrate spectral-action ↔ methodology rule-architecture Φ correspondence (graded ring isomorphism)

Source: S86 W-13 §C3-CONV-1 + §C3-CONN-EM-1 (connes+lizzi)
Anchors: `session-86-w13-workingpaper.md` L1450-1490 + L2027-2034

GRADED RING ISOMORPHISM Φ (substrate Seeley-DeWitt moment a_2n ↔ methodology rule-architecture stratum Σ_n):

| Substrate moment | Φ-image stratum | Weight | Physical content |
|:------------------|:------------------|:--------|:------------------|
| a_0^{ζ}            | Σ_1 | 0 | perimeter / cosmological term |
| a_2^{ζ}            | Σ_2 | 2 | Einstein-Hilbert kinematic skeleton |
| a_4^{ζ}            | Σ_3 | 4 | Yang-Mills + Higgs quartic load-bearing |

Substrate-side derivation pointers:
 - The substrate's Seeley-DeWitt expansion provides the graded-ring source: a_0, a_2, a_4 carry weights 0, 2, 4 respectively
 - Φ maps each substrate moment to the corresponding methodology rule-architecture stratum: Σ_1 (cosmological/perimeter rule layer), Σ_2 (kinematic-skeleton rule layer), Σ_3 (load-bearing rule layer)
 - The isomorphism preserves the graded-ring structure: weight-0 ↔ Σ_1, weight-2 ↔ Σ_2, weight-4 ↔ Σ_3
 - Per `regulator-pin-discipline.md`, Seeley-DeWitt coefficients carry explicit regulator tags: a_0^{ζ}, a_2^{ζ}, a_4^{ζ} (zeta-regulated; the Φ correspondence inherits the regulator tag from the source moment)
Direction (substrate-IS-prior): the substrate's spectral-action graded-ring is structurally prior; the methodology rule-architecture is the Φ-image at the methodology layer.
Status: STRUCTURAL CORRESPONDENCE (READY-TO-INSTALL; content fully specified; graded ring isomorphism Φ(a_2n) = Σ_n with explicit weight preservation; source-pin: workshop SHA).

