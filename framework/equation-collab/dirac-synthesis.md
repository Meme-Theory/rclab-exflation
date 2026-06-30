# Capstone Equation Review — dirac

**Date**: 2026-05-29
**Agent**: dirac-antimatter-theorist (dirac)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` (the S95-era capstone)
- Cross-checked: `computations/session-66/s66_product_ko_dim_output.txt` (PRODUCT-KO-DIM-66); `s81_gate_verdicts.txt` (T3-S35-PFAFFIAN-CORRECTED-J, T3-S28C-12D-AXIOMS); knowledge MCP (`M_KK`, `tau_fold`, f_NL gates, Trap-5/B3); my own memory `T1`–`T11`.

---

## I. Session Outcome

The capstone is, from the charge-conjugation / CPT vantage, **structurally sound at its load-bearing core and honest about its gaps** — with three exceptions I flag below. The two-scalar exhaustion (trace + inner product), the four axioms (§1.2), and the boxed action are exactly the objects my domain certifies: `[J, D_K(τ)] = 0` (E8) is the algebraic statement of CPT, KO-dimension 6 (E9) is the unique mod-8 class enforcing `Jγ = −γJ`, and the Pfaffian fermionic measure on `H_K⁺` is the path-integral statement of "one generation, not four." These are all PROVEN at machine epsilon and consistent with my recorded `T1`/`T5`/`T10`/`T11`. The document does NOT re-derive them loosely; it cites them correctly.

Three items require flagging, not re-adjudication: **(1)** the §7 **f_NL = −1.505** value conflicts with the registry (S67 `f_NL = 1.03`; S84 `−0.142566` FAIL); **(2)** the §1.3 product-KO statement ("product KO=4 vs finite KO=6") is the *Geometry-B* reading of a three-way structure that s66 (PASS) explicitly resolves, and the s66 impact-assessment finding that the **product chirality coupling `ε″=+1` gives "wrong Yukawa chirality structure"** is not fully discharged by the document's H_K⁺ footnote; **(3)** the capstone is **silent on baryon asymmetry** — a notable absence given my `T11` proves all *internal* J-breaking baryogenesis is closed and the matter–antimatter asymmetry therefore demands physics *external* to `D_K`, which is a frontier the document should name.

---

## II. Key Results

### The CPT axiom `[J, D_K(τ)] = 0` (E8) is correctly stated and is the algebraic CPT theorem

**Result**: `[J, D_K(τ)] = 0 ∀τ`, hardwiring `λ ↔ −λ`, `η(s) = 0`, spectral flow = 0. Classification: **GEOMETRIC** (a property of the operator/real-structure pair, not of any excitation).

This is my `T1` and the document's E8, and the two agree. The crucial subtlety — which the document does *not* trip over but which a careless reader would — is that `J = C₂·K` is **antilinear** (`C₂ = γ₁γ₃γ₅γ₇`, the product of the real/antisymmetric gammas in the Cl(8) construction; my memory, confirmed by s66 §6 "Generator indices (antisymmetric gammas): [1,3,5,7], J²=+1"). The condition that hardwires CPT is the antilinear conjugation form `C₂ conj(D_K) C₂ = D_K`, NOT `[C₂, D_K] = 0` (which is generically nonzero for complex `D_K` and is a T-symmetry statement, not a violation). The capstone writes "`[J, D_K] = 0`" with `J` the full antilinear real structure, which is the correct object — the commutator of the *antilinear* `J` with `D_K` is the right CPT condition. I confirm the document is not making my recorded antilinear-J pitfall. The "79,968 pairs, machine-ε" anchor is the conjugate-degeneracy verification; consistent with my S71 note (85 conjugate degeneracies `B2(0,1)=B2(1,0)` to `|gap|<5e-15`).

The downstream consequence the document draws — `η(s) = 0`, spectral flow = 0, gap never closes (E5 Lichnerowicz) — is exactly my `T2`/`T7`. The Lichnerowicz convention note (§2.3) is well-handled: stating the bound convention-free as `λ² ≥ R_K(τ)/4 > 0` and refusing to print "`≥ 3`" beside the rational-normalization curvature is precisely correct, and it pre-empts the factor-6 bi-invariant-scale confusion that bit earlier sessions.

### KO-dimension 6 and the Pfaffian: the "why KO=6 ↔ why D=10" analogy is the right framing

**Result**: KO-dim 6 mod 8 = the unique class with `(ε,ε′,ε″)=(+1,+1,−1)` ⇒ `Jγ = −γJ` ⇒ the bilinear `A_D` is antisymmetric ⇒ `Pf(A_D) = √det` is well-defined ⇒ one generation. Classification: **GEOMETRIC** (real-structure / grading axiom).

This is my `T5` (KO-dim=6 conditions, parameter-free) and `T10` (Pfaffian sgn = −1 constant, trivial Z₂, PF-J-35 PASS), and it matches gate `T3-S35-PFAFFIAN-CORRECTED-J: PASS, value=-1, convention=KO-dim=6_corrected-J_C2=g1g3g5g7_C1=g2g4g6g8, L_max=16`. The document's §1.3 footnote-4 framing — that the product-KO mismatch does *constructive* work by *forcing* the `H_K⁺` restriction, "exactly as level-matching is not a defect of the string but the constraint that makes the physical spectrum" — is the correct and honest reading. `Jγ = −γJ` is what makes `A_D` antisymmetric; that is a real theorem, not a slogan. I endorse this.

One precision point: the document calls KO=6 "the *unique* mod-8 class making `Jγ = −γJ`." Per the s66 sign table this is right for the chirality relation `ε″=−1` *within the physically relevant period*, but `ε″=−1` also holds at KO=2. The document means the *full* `(ε,ε′,ε″)=(+1,+1,−1)` triple, which IS unique to KO=6 in `{0,2,4,6}`. The sentence is true under the intended reading; it would be sharper to say "the unique class with the full `(+1,+1,−1)` triple." Minor — does not affect the result.

### The genesis/transit/freeze trajectory respects the gap-never-closes invariant

**Result**: At `τ=0`, the round `SU(3)` metric (`R_K(0)=2`, `R_K′(0)=0`, unstable critical point); the spectrum continuously reorganizes through `τ_fold=0.190` **without zero crossings** (E5), so spectral *topology* is preserved while *frequencies* reorganize. Classification: **GEOMETRIC** (the τ-flow of `D_K`'s spectrum).

This is the correct and load-bearing point for my domain: because the gap never closes, the conjugate-pairing structure `λ ↔ −λ` is preserved at *every* `τ`, so CPT is not a feature only of the endpoints — it holds along the entire transit. The document's §2.4 "spectral complexity grows inside each point — without zero crossings" is exactly the statement that the BDI symmetry class (my `T2`–`T4`: `T=C₂·K`, `P=C₁·K`, `S=γ₉`; `C²=T²=+1`) is `τ`-invariant. I verify this is internally consistent: a zero crossing would be a spectral-flow event and would break `η=0`; the document and E5 both forbid it. Good.

### `M_KK` and `τ_fold` provenance — verified canonical

**Result**: `Λ = M_KK = 7.4287×10¹⁶ GeV` (knowledge MCP: `7.428660036284456e16`, S42 CONST-FREEZE-42); `τ_fold = 0.190` (S12/S42 CONST-FREEZE-42). Classification: **GEOMETRIC**.

Both match the canonical pins exactly. The document's `7.4287×10¹⁶` is the correctly-rounded headline of the canonical value. The `w0_FW` provenance-in-place note (Verification ledger) is borne out — these are the binding constants for the DESI-DR3 falsifier and they are pinned before the 2026 event. No drift.

---

## III. Gate Verdicts

| Gate | Verdict (source) | Decisive Number | Status vs document |
|:-----|:--------|:----------------|:--|
| T3-S35-PFAFFIAN-CORRECTED-J | PASS (`s81`) | Pf sign = −1 | document §1.3 footnote-4 consistent |
| [J,D_K(τ)]=0 (E8) | PROVEN (S23 Sagan) | 79,968 pairs, machine-ε | document §1.2/§2.3 consistent |
| T3-S28C-12D-AXIOMS | **FAIL** (`s81`), value=6/7 | 6 of 7 order-one axioms hold | document §1.3.4 discloses this as "6/7 order-one axioms hold" — **honest** |
| PRODUCT-KO-DIM-66 | PASS (`s66`) | KO(M⁴×SU(3))=4 vs KO(F_SM)=6 | document §1.3 picks Geometry-B reading; see §IV flag |
| S84-ALPHA-F-NL-FRAMEWORK-PRED | **FAIL** (`s84`), value=−0.142566 | equilateral f_NL | **conflicts with document's −1.505**; see §IV |
| S88-F-NL-EQUILATERAL-NON-GAUSSIANITY | FAIL/PRE-REG-INC (`s88`) | blocked on folded-language correction | f_NL row is in flux; document over-pins it |
| Trap 5 / V_ph(B1,B3) | PROVEN (`atlas-07`) | `<1e-14` within-branch PH; `M_ph∈iR` | document inherits; B3=0 from abstract axioms still OPEN (my `T9`) |

---

## IV. Structural Implications

### FLAG 1 (numerical conflict) — the f_NL = −1.505 row contradicts the registry

The §7.1 scorecard and §7.3 print **`f_NL = −1.505` (`|f_NL| ≲ 1.5`, Bogoliubov-Gaussian by Wick), PASS (0.47σ)**. The knowledge MCP returns three *different* f_NL anchors:
- `falsifier-rigor-registry.md` S67: `f_NL^total = 1.03` (GGE-BISPECTRUM), 0.57σ;
- `S84-ALPHA-F-NL-FRAMEWORK-PRED`: `value = −0.142566`, **FAIL**, equilateral;
- `S88-F-NL-EQUILATERAL-NON-GAUSSIANITY`: **FAIL / PRE-REG-INC**, blocked on a folded-language byte-replacement.

The document's `−1.505` matches *none* of these three. The σ-distance it quotes (0.47σ) is also closer to the S67 `1.03` (0.57σ) than to anything I can reconcile with `−1.505`. **This is a numerical conflict I am flagging, not resolving** (per the review rules — I do not overturn recorded verdicts, but the document's value does not trace to a canonical pin). The structural claim the document leans on — that the relic is a Bogoliubov (squeezed-vacuum) state, hence Gaussian by Wick's theorem at leading order, hence `|f_NL|` small — is *qualitatively* sound and is squarely my domain: a Bogoliubov transformation of a Gaussian vacuum is Gaussian, so connected 3-point functions vanish at quadratic order and `f_NL` is an `O(1)` loop/interaction residual. But the *specific number* `−1.505` needs a traceable provenance. Either the document is citing an unpinned newer value or it has a sign/magnitude transcription issue. Convert to a §V harvest.

### FLAG 2 (precision + undischarged sub-finding) — the product-KO chirality coupling

The §1.3 statement "the product triple `M⁴×SU(3)×F_SM` carries a **permanent KO mismatch** (product KO=4 vs finite KO=6)" is **defensible but imprecise**, and it omits a downstream finding that is exactly my domain. The s66 PASS output (which I read in full) documents THREE distinct triples:
- **Geometry A** — `M⁴ × F_SM` (the NCG SM): KO = 4+6 = 10 = **2 mod 8**, `J_tot²=−1`;
- **Geometry B** — `M⁴ × SU(3)` (12-dim Riemannian product): KO = 4+0 = **4**, `J_tot²=−1`;
- **Geometry C** — framework's "SU(3)-as-F" reading: KO mismatch `0 ≠ 6`.

The document's "product KO=4 vs finite KO=6" is the **Geometry-B-vs-finite-SM comparison**, which is internally consistent and is what the PASS certifies as permanent. Fine. But s66's *impact assessment* (lines 359–368) states plainly that with `ε″=+1` on the product (KO=4), **"Yukawa couplings have wrong chirality structure → Fermionic sector needs modified prescription or separate construction."** The document's footnote-4 resolves the *fermion-doubling / one-generation* question on the **internal** triple `K` via the Pfaffian and `H_K⁺` — and that is correct and well-executed — but it does **not** address the s66 finding that the *chirality coupling of the Yukawa/mass term on the product* is structurally affected. This is the charge-conjugation–chirality nexus, my core remit: KO=6 is the class where "CPT flips chirality (physical)"; KO=4 (the SU(3)-manifold product) is the class where "CPT preserves chirality (non-physical for SM)" (s66 §10). The document asserts the bosonic sector is unaffected (true — the spectral action is J-independent, s66 lines 350–358) and that the Pfaffian survives on `K` (true). What it leaves implicit is **how the physical chirality-flipping CPT of the finite SM (`ε″=−1`) is recovered when the SU(3)-manifold lift carries `ε″=+1`.** This is *the* substantive open structural item under the §1.3.4 caveat, and it deserves to be named as such rather than folded entirely into "a known, bounded caveat." It is consistent with the registry's `T3-S28C-12D-AXIOMS: FAIL (6/7)` — the missing axiom is on the fermionic-product side. Convert to a §V harvest.

### FLAG 3 (silence) — no baryon asymmetry, and the capstone should say why

A capstone that runs "from genesis to now" and enumerates dark matter, dark energy, n_s, r, m_H, σ₈ contains **no mention of the matter–antimatter asymmetry**. From the antimatter vantage this is a conspicuous gap, and it is *not* a defect of the framework — it is a structural prediction my work has already established. My `T11` proves `C₂ conj(D_K) C₂ = D_K` for *any* left-invariant metric on `SU(3)`, closing **all internal J-breaking baryogenesis** on the full 36D moduli (bulk Volovik, domain-wall, chiral-η, twist channels — all CLOSED, per my baryogenesis ledger and the knowledge-MCP confirmation that "baryogenesis requires physics EXTERNAL to SU(3) Dirac operator"; cf. `s60_lepto_cp_log` "this operator satisfies [J,D_K]=0 at ALL tau (Theorem T11, S43)"). The implication is sharp and *strengthens* the equation's honesty-ledger: **because `[J,D_K]=0` is exact at all τ, the spectral action of `D_K(τ)` alone cannot generate a baryon asymmetry** — Sakharov's C/CP-violation condition cannot be met by the internal operator. Any baryogenesis must come from physics *external* to `D_K`: an additional fiber, tessellation/topological defects, or the 4D gravitational coupling (gravitational baryogenesis via `tr(R∧R)`, which the knowledge MCP lists as OPEN, and which is interesting because `p₁[SU(3)]=0` exactly, so the internal Pontryagin source vanishes). This belongs in §9's "honest open frontiers" as a *named* item — it is in the same family as the missing-`a(t)` / external-coupling frontier, and it converts a silence into a stated structural prediction (the equation is *too CPT-symmetric* to bake in the asymmetry; that is a feature of `D_K`, and a pointer to where new physics must live). Convert to a §V harvest.

### Endorsements (where the document is solid in my domain)

- **The Ordered Veil as a CPT-preserving, pure (`S_ent=0`) Bogoliubov relic** (§5.3) is structurally correct and is the antimatter-relevant statement that the relic is **CPT-neutral and superselection-protected** (`N_pair` conserved, `T^{0i}=0` exact, no annihilation channel). A Bogoliubov transformation is unitary, the conjugate-pairing is preserved by `[J,D_K]=0`, and a product state has zero entanglement entropy — these are mutually consistent. The information-theoretic framing ("no Page curve because nothing thermalizes; the Bogoliubov phase is retained in the conserved charges") is sound and does not over-claim.
- **The `σ/m = 0` exact structural zero** for dark-matter self-interaction (§7.1) is the correct consequence of `N_Fock=1` and the CPT-neutral relic — a structural zero, distinct from a tuned cross-section. I endorse the framing "stronger than 0.7σ PASS."
- **The acoustic-white-hole two-null-cone structure** (§6.2) and its `T_H=0` extremal-horizon corroboration of "never thermalizes" do not touch a CPT contradiction; they are consistent with the gap-never-closes invariant.
- **§8.5's geometry-vs-topology spine** (the topological/representation-theoretic outputs survive continuum dissolution; absolute magnitudes are conditional) is the correct epistemic partition, and it places `[J,D_K]=0`, the BDI/`N₃=0` class, and the `7.324992` cocycle ratio (CF-35) on the *surviving* side — which is exactly right. CPT and the symmetry class are topologically protected; the `a_n` absolutes are not.

---

## V. Carry-Forward Computations

**MANDATORY — primary input to the next compute session.**

```
V.1. Trace and re-pin the f_NL value (resolve −1.505 vs registry 1.03 / −0.142566)
   - What: Recompute the GGE-bispectrum f_NL from the squeezed-vacuum (Bogoliubov)
           reduced bispectrum B(k1,k2,k3) = ⟨ζ_k1 ζ_k2 ζ_k3⟩_c, in BOTH the
           equilateral and squeezed configurations, at the canonical relic
           Bogoliubov coefficients {α_k, β_k} (P_exc=1). Output f_NL^equil and
           f_NL^squeezed with full float64 to .npz and 4-sig-fig to the working
           paper; reconcile the sign against Wick's theorem (Gaussian leading
           order ⇒ connected 3-pt vanishes ⇒ f_NL is the O(1) interaction residual).
   - Inputs: relic Bogoliubov coefficients (s74 N_Fock=1 reduction; S67 GGE-bispectrum
           npz); canonical_constants f_NL pins if any; Planck 2018 equilateral
           −26±47 and squeezed −0.9±5.1 as comparison-only anchors.
   - Gate: NEW gate S96-F-NL-PROVENANCE-RECONCILE. PASS = the recomputed value
           matches ONE registry anchor to within its publication precision AND the
           capstone's −1.505 is either corrected to that value or given a traceable
           pin. INFO = three anchors are three distinct (config, regulator) objects
           and the capstone must tag which one it cites. FAIL = −1.505 traces to no
           computation (transcription error; correct the capstone).
   - Effort: 3-4 hours, 1 agent session.
```

```
V.2. Yukawa chirality coupling on the SU(3)-manifold lift (ε″=+1 vs SM ε″=−1)
   - What: Construct the fermionic mass/Yukawa bilinear ⟨Jψ̃|D_K|ψ̃⟩ explicitly on
           the product M⁴×(SU(3),g_τ) using the s66 B_+ charge conjugation (ε″=+1
           on the SU(3) factor), and compute whether the physical chirality-flipping
           structure of the finite-SM Yukawa (ε″=−1) is recovered after the H_K⁺
           Pfaffian restriction, or whether a residual wrong-chirality coupling
           survives. Compute the overlap ⟨γ_9 Jψ̃ | D_K | ψ̃⟩ on H_K⁺ and test for a
           nonzero chirality-preserving (CPT-non-flipping) component.
   - Inputs: s66 Clifford construction (C2=g1g3g5g7, C1=g2g4g6g8); D_K(τ_fold) blocks
           from the L_max=10 spectrum cache; H_K⁺ projector (γξ=ξ); the SM branching
           Ψ₊=(3,2,⅙)⊕… (E10).
   - Gate: NEW gate S96-PRODUCT-YUKAWA-CHIRALITY. PASS = the H_K⁺ restriction
           projects out the wrong-chirality (ε″=+1) coupling, recovering effective
           ε″=−1 on the physical fermion bilinear (residual < 1e-12). FAIL = a
           nonzero chirality-preserving coupling survives ⇒ the §1.3.4 caveat is
           larger than "bounded" and the capstone footnote must be expanded.
           INFO = the coupling is nonzero but is a known measure-zero set absorbed
           by the Pfaffian normalization.
   - Effort: 6-8 hours, 1 agent session (uses existing Clifford + cache machinery).
```

```
V.3. Register and bound external baryogenesis given [J,D_K]=0 closure
   - What: Make explicit the structural prediction that the SU(3) spectral action
           cannot generate baryon asymmetry (Sakharov C/CP-violation barred by
           [J,D_K]=0, T11). Compute the leading external channel: gravitational
           baryogenesis source ∝ ∂_μ R · J^μ_B, evaluating whether tr(R∧R) on the
           EMERGENT g_M (a₂ moment) is nonzero even though p₁[SU(3)]=0 internally.
           Output the CP-odd density at τ_fold and bound it against the observed
           η_B = n_B/n_γ ≈ 6×10⁻¹⁰.
   - Inputs: T11 closure (S43 baryogenesis ledger); p₁[SU(3)]=0 (S54 ELASTIC-
           TETRAD-CC-54); a₂(τ) curvature R_K(τ); emergent g_M dictionary (§8.3,
           f₂≈92); the OPEN "Gravitational baryogenesis" channel (S53).
   - Gate: NEW gate S96-EXTERNAL-BARYOGENESIS-LOCATE. PASS = the internal source is
           exactly zero (confirming T11 at the capstone level) AND the emergent-
           gravity channel gives a nonzero, computable, sub-observed CP-odd density
           ⇒ register as honest open frontier #9. INFO = emergent tr(R∧R) also
           vanishes (then baryogenesis needs an additional fiber, register as such).
           FAIL = an internal CP-odd source is found (would contradict T11; must
           re-audit).
   - Effort: 4-6 hours, 1 agent session.
```

```
V.4. Close M_ph=0 for B3 from abstract axioms (currently numerical-only, T9)
   - What: Prove the phonon-mass vanishing M_ph=0 for the B3 (optical) branch from
           the J-reality + block-diagonality axioms directly, replacing the current
           numerical result (V(B1,B3)=0.0000 EXACT NNI; M_ph∈iR proven, M_ph=0 for
           B3 OPEN). Use the Schur-lemma argument (T9 Trap-4 V_eff=0) extended to
           the within-branch PH channel on B3, and verify against the registry's
           Trap-5 V_ph(B1,B3)=0 (<1e-14).
   - Inputs: Trap-5 theorem (atlas-07-permanent-results, <1e-14); B3 eigenspinor
           overlap structure (s43, |O_{B1,B3}|=0 exactly); J-reality on real reps
           B1,B3; my T9 proofs-and-theorems.md derivation.
   - Gate: feeds the existing Trap-5 line. NEW sub-gate S96-B3-PHONON-MASS-ABSTRACT.
           PASS = M_ph(B3)=0 derived from axioms (analytic, no numerical input).
           FAIL = a nonzero abstract residual ⇒ the numerical zero is accidental,
           not structural. INFO = derivation reduces to a known open lemma.
   - Effort: 4-5 hours, 1 agent session (analytic; my domain).
```

```
V.5. Sector-resolved conjugate-representation topology R(p,q) (my open question)
   - What: Test whether the momentum-space topology distinguishes conjugate Peter-
           Weyl reps (p,q) vs (q,p) BEYOND their (degenerate) spectra — compute the
           non-Abelian Wilson loop / Berry phase θ_{(p,q)} and test the antisymmetry
           conjecture θ_{(q,p)} = −θ_{(p,q)} (WILSON-LOOP-47), and the (3,0)/(0,3)
           π-phase asymmetry (1 vs 2) with a gauge-invariance check (CLOSED-LOOP-47).
   - Inputs: D_K block decomposition ⊕_{(p,q)} D_{(p,q)} (E6); the 85 conjugate
           degeneracies B2(0,1)=B2(1,0) (S71); the BDI class structure (T2-T4);
           anomalous-density spectral projectors in degenerate eigenspaces (my
           technical lesson on gauge invariance).
   - Gate: NEW gate S96-CONJUGATE-REP-TOPOLOGY. PASS = θ_{(q,p)}=−θ_{(p,q)} to
           machine-ε AND gauge-invariant ⇒ conjugate reps carry a topological (not
           merely spectral) distinction, a particle/antiparticle structural marker
           on the fiber. FAIL = θ symmetric ⇒ no topological distinction beyond
           spectra. INFO = phase is gauge-dependent (then the observable is the
           holonomy class, recompute).
   - Effort: 6-8 hours, 1 agent session.
```

```
V.6. One-loop CPT robustness of [J,D_K]=0 (extend E8 past tree level)
   - What: The capstone's §1.3a establishes the no-interior-saddle result is ONE-
           LOOP-ROBUST (S95 W2-3) via Γ=S+½Tr ln(D_K²/Λ²). Verify that the CPT
           commutant [J,D_K]=0 (E8, tree-level / spectral) is likewise preserved at
           one loop: compute whether the one-loop effective Dirac operator
           D_K^eff = D_K + (one-loop self-energy Σ) still satisfies J conj(D_K^eff)
           J = D_K^eff, i.e. whether Σ is CPT-even. This pins whether mass equality
           m(particle)=m(antiparticle) survives the threshold correction.
   - Inputs: Γ_1loop = ½Tr ln(D_K²/Λ²) (§1.3a, S95 W2-3); J=C₂·K antilinear form
           (T1); D_K(τ_fold) cache; the cutoff f*(x)=0.9117√x+0.0883e⁻ˣ.
   - Gate: NEW gate S96-CPT-ONE-LOOP. PASS = J conj(Σ) J = Σ (CPT-even self-energy,
           residual < 1e-12) ⇒ mass equality survives one loop, strengthening E8
           from spectral to effective. FAIL = a CPT-odd one-loop piece ⇒ a small
           m(p)−m(p̄) splitting that must be bounded against BASE 16 ppt.
   - Effort: 5-7 hours, 1 agent session.
```

```
V.7. Pin the η-invariant exactly zero past the BDI pairing (T8 cross-check at one loop)
   - What: My T8 proves Tr(γ_9 f(D_K²/Λ²)) = 0 identically (BDI pairing). The
           capstone uses η(s)=0 (E8) as a tree-level input to the "no spectral flow"
           and "censored singularity" arguments. Verify η(s)=0 is stable under the
           Jensen deformation across the FULL transit τ∈[0, τ_overshoot=1.614],
           NOT only at τ_fold, and confirm no η jump at the van Hove cusp (where the
           DOS diverges and a naive η computation could pick up a boundary term).
   - Inputs: T8 (Tr(γ_9 f)=0); E8 (η=0, 79,968 pairs); R_K(τ) for the full transit;
           the van Hove DOS g(ω)∼1/√(ω−ω_min) at τ_fold; censorship barrier
           τ_NEC=1.383, τ_overshoot=1.614 (§5.2).
   - Gate: NEW gate S96-ETA-TRANSIT-STABILITY. PASS = η(τ)=0 to machine-ε for all
           τ in [0,1.614] including at the cusp ⇒ the BDI pairing and CPT survive the
           singularity; the "anisotropic τ→∞ singularity is censored" argument is
           CPT-clean. FAIL = a nonzero η at the cusp ⇒ a parity-anomaly boundary term
           the censorship story must absorb.
   - Effort: 4-6 hours, 1 agent session.
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | `[J,D_K(τ)]=0` (E8) correctly stated; antilinear-J pitfall avoided | GEOMETRIC | SOLID (PROVEN, my T1) | CPT is exact at every τ along the transit, not just endpoints |
| 2 | KO-dim 6 / Pfaffian / one-generation; "why KO=6 ↔ why D=10" | GEOMETRIC | SOLID (PASS, my T5/T10) | Constructive-constraint framing endorsed; H_K⁺ restriction is forced, not patched |
| 3 | Gap-never-closes ⇒ BDI class is τ-invariant | GEOMETRIC | SOLID (E5, my T2-T4) | Conjugate-pairing λ↔−λ preserved throughout exflation |
| 4 | f_NL = −1.505 | PHONONIC | **CONFLICT** (registry: 1.03 / −0.142566) | FLAG 1; provenance untraceable; §V.1 |
| 5 | Product-KO "4 vs 6"; Yukawa chirality (ε″=+1) | GEOMETRIC/PARTICLE | PRELIMINARY / partly-undischarged | FLAG 2; Geometry-B reading defensible, chirality sub-finding not closed; §V.2 |
| 6 | Baryon asymmetry — absent from capstone | PARTICLE | GAP (my T11 closes internal channels) | FLAG 3; the equation is *too CPT-symmetric* to source η_B; name external frontier; §V.3 |
| 7 | Ordered Veil = CPT-neutral pure Bogoliubov relic; σ/m=0 | PHONONIC | SOLID | Endorsed; relic is superselection-protected, no Page curve |
| 8 | Geometry-vs-topology spine (§8.5) | GEOMETRIC | SOLID | CPT/BDI/cocycle on surviving side; a_n absolutes conditional — correct partition |
| 9 | M_ph=0 for B3 (abstract) | GEOMETRIC | OPEN (numerical-only, my T9) | §V.4 closes it from axioms |
| 10 | Conjugate-rep topology R(p,q) | PARTICLE | OPEN (my open question) | §V.5; particle/antiparticle marker on the fiber |
| 11 | CPT/η one-loop robustness | GEOMETRIC | PRELIMINARY (tree-level proven) | §V.6/V.7 extend E8 + T8 past tree level; bounds m(p)−m(p̄) against BASE |
