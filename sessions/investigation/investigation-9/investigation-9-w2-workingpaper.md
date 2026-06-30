# Investigation 9 Wave 2 — String Cross-Framework Walls / Mechanism Imports (Results Working Paper)

**Investigation**: 9 | **Wave**: 2 | **Plan**: investigation-9-plan-w2.md | **Track**: investigation | **Theme**: "the wall tells us what cement to pour" — import string mechanisms (Sen-tachyon K-theory descent, dS-entropy species-count) as substrate-fillers + refresh the swampland audit against 2018–2025 conjectures. Gate-type mix: compute × 2 + review × 1.

**Verdict-file (compute gates only)**: `computations/investigation-9/inv9_gate_verdicts.txt` — emit via `emit_verdict(session=9, track="investigation", ...)` per `.claude/rules/gate-verdicts.md §"Investigation-Track Canonical Path"`. The review gate (W2-3) has NO verdict line; it closes by artifact-existence-with-content.

## Gate Sections

### §W2-1. INV9-W2-1-SEN-TACHYON-K-THEORY-DESCENT (string-theory-theorist)

**Status**: COMPLETED
**Gate ID**: `INV9-W2-1-SEN-TACHYON-K-THEORY-DESCENT`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (K_0(A_F) class change under the supersonic transit)
**Agent**: `string-theory-theorist` (+ connes-ncg-theorist co-option for the Chern-character / Wedderburn-rank K_0 evaluation)
**Hypothesis**: The supersonic transit realizes a Sen-type tachyon condensation — the K_0(A_F) class (rank-3, ch-matrix diag(1,1,3)) of the post-transit projector differs from the pre-transit class, giving the framework a unitary, information-preserving dynamics.
**Plan reference**: `sessions/investigation/investigation-9/investigation-9-plan-w2.md` §W2-1 (machinery pin, substitution chain, K_0(A_F)=ℤ^3 rank-triple source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/investigation-9/inv9_w2_sen_tachyon_k_theory_descent.py` — EXISTS (26830 bytes). `grep -cE "from canonical_constants import"` → **3**; `grep -cE "print_verdict_payload"` → **3** (both must_contain patterns PRESENT).
- **data** `computations/investigation-9/inv9_w2_sen_tachyon_k_theory_descent.npz` — EXISTS (4927 bytes; 23 keys incl. `ch0_pre=[1 2 3]`, `ch0_post=[1 2 3]`, `k0_class_change=False`, `band0_spread`, `invariance_t0/t1/t2`, dual-SHA).
- **plot** `computations/investigation-9/inv9_w2_sen_tachyon_k_theory_descent.png` — EXISTS (179404 bytes; 3 panels: rank-triple pre-vs-post, per-triality-class sector partition vs L_max, band-0 ground-|λ| deformation scatter).
- **verdict_line** `computations/investigation-9/inv9_gate_verdicts.txt` — `^INV9-W2-1-SEN-TACHYON-K-THEORY-DESCENT:.* audit_sha256=[a-f0-9]{64}` MATCHES (`audit_sha256=1b82dc76…fb6c0`); dual-SHA companion comment row PRESENT. No `[SIGN]` 3-tuple row (`schema_v2_3tuple_required: false`).
- **wp_section** this §W2-1 — carries `Status: COMPLETED`, `Verdict: FAIL`, `Output Artifacts`, `MCP Pre-Compute Audit` (all four must_contain markers present).

**Verdict-line closure** (compute gate):
Emitted via `emit_verdict(session=9, track="investigation", ...)` (race-safe, lock-serialized; sig_5-unique). Canonical line:
```
INV9-W2-1-SEN-TACHYON-K-THEORY-DESCENT: FAIL -- value='K0_class_change=False;ch0_pre=(1,2,3);ch0_post=(1,2,3);K0_rank=3;Wedderburn_ranks_over_C=(1, 2, 3);n_tachyonic=279;band0_spread=2.312678;rank_structure_invariant=True' scheme=K-theory-Chern-character-ch0 convention=Wedderburn-rank-triple-K0-AF-ZZ3 L_max=12 audit_sha256=1b82dc76e502d19823afa848d1179ca28b8f4ed7c6bc44923a99b8c2b9cfb6c0 content_sha256=c84f9b982966e537e6bd93a7a5da1342316cb2369655b166b321834548b9bab9 schema_version=S84+
```
- `audit_sha256` = `1b82dc76e502d19823afa848d1179ca28b8f4ed7c6bc44923a99b8c2b9cfb6c0` (script+canonical+pinmap)
- `content_sha256` = `c84f9b982966e537e6bd93a7a5da1342316cb2369655b166b321834548b9bab9` (script only)

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; query-first discipline):
- `search_knowledge("TRANSIT-279 tachyon condensation Sen K_0 Chern character")` → confirmed `ch_matrix = diag(1,1,3)` + `ch^0([1_ℂ])=(1,0,0)/ch^0([1_ℍ])=(0,2,0)/ch^0([1_M3])=(0,0,3)` (S84 W10); `s48_qa_tachyon.py --feeds_into--> gates:TRANSIT-279`.
- `query_entity(theorems, proven_1437)` → returns T7 (GGE relic, PROVEN S58); the plan's `proven_1437` label maps to the T-series — the TRANSIT-279 tachyon STRUCTURE is anchored via the S84-W10 / S46 equation hits, not this theorem ID. Noted; not load-bearing for the K_0 computation.
- `search_knowledge("chi prime faithful image rank 1+2 Wedderburn S91-W2")` → `rank(image χ') = rank(ℂ)+rank(ℍ) = 1+2 = 3`; faithful image is ℂ⊕ℍ (M_3 killed, ker rank 9); K_0-rank-mass-fraction 3/6.
- `search_knowledge("S84 W10 K_0 A_F rank-3 ch0 ... HP0 projector class")` → `session-84-w10-workingpaper.md`: `ch_matrix = diag(1,1,3)`; `session-86-1b-s12-connes.md` PROVEN theorem: `EXP_K0_RANK=3, EXP_K0_TORSION=0`, A_F=ℂ⊕ℍ⊕M_3(ℂ) Wedderburn-3-summand.
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42); `get_constant("M_KK")` → 7.4287e16; `canonical_constants.rank_exclusion` → 3 (S84 W10a-117 rank-3 lattice). **Not PRE-CLOSED** — the *transit-change* of the K_0 class is FRESH (no prior gate evaluated whether the tachyonic flow jumps the K_0 class; the S84/S86 results pin the STATIC pre-transit class only).

**Verdict**: **FAIL** — `ch⁰(P_post) = ch⁰(P_pre) = (1, 2, 3)`; the K_0(A_F)=ℤ³ class is **INVARIANT** under the supersonic transit. Per the plan `dual_prior` discriminator (FAIL → 0.9 to Track B): the tachyonic direction is a fluctuation **within a fixed K-theory class**, NOT a brane-charge-changing condensation. The Sen analogy is structural-only — the framework HAS a tachyon, but its condensation does NOT carry a K-theoretic charge change. This is a categorical boundary result: the framework's tachyon is unlike Sen's at the K-theory level.

**Results**:

| Quantity | Value | Source |
|:---------|:------|:-------|
| `A_F` | ℂ ⊕ ℍ ⊕ M₃(ℂ) | KO-dim=6 finite spectral triple (canonical) |
| `K_0(A_F)` | ℤ³ (Wedderburn 3-summand) | S86-1b PROVEN `EXP_K0_RANK=3, EXP_K0_TORSION=0` |
| `ch⁰(P_pre)` = `(n_ℂ, n_ℍ, n_M3)` | **(1, 2, 3)** | = ch⁰(1_ℂ)+ch⁰(1_ℍ)+ch⁰(1_M3); S84 W10 eq II.2-5/6/7 |
| `ch⁰(P_post)` | **(1, 2, 3)** | inner-fluctuation endpoint; `A_F` fixed ⇒ same minimal central idempotents |
| `K0_class_change` (post ≠ pre, component-wise) | **False** | discrete ℤ³ integer-triple comparison |
| K_0 rank (occupied summands) | 3 | matches canonical `rank_exclusion = 3` |
| `n_tachyonic` (TRANSIT-279) | 279 | `s48_qa_tachyon.npz` `tr_n_tachyonic` (proven structure, S46) |
| band-0 ground \|λ\| spread (L≤10) | **2.312678** M_KK | deformation is NONTRIVIAL (spectrum moves) yet class is rigid |
| `rank_structure_invariant` (triality partition stable across L_max∈{8..12}) | True | per-class sector counts: t0/t1/t2 = (14,15,15)→(30,30,30) as L_max 8→12 |
| `L_max_plan` / `L_max_operational` | 12 / 10 | cache stored at L=12; Friedrich-Bär-saturated observable at L=10 |

**Substitution chain** (pins the K_0 invariant identity; per `math-scripts.md` the chain pins the discrete-class structure rather than a directional sign):
```
Def 1: A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)                          [finite spectral-triple algebra; KO-dim=6, canonical]
Def 2: K_0(M_n(ℂ)) = ℤ, generated by [minimal proj]   [rank-1/C for ℂ, rank-2 for ℍ→ℂ, rank-3 for M_3(ℂ)]
Def 3: K_0(A ⊕ B) = K_0(A) ⊕ K_0(B)                    [K-theory additive over direct sums]
Def 4: ch⁰: K_0(A_F)→HP⁰(A_F);  ch⁰([1_ℂ])=(1,0,0), ch⁰([1_ℍ])=(0,2,0), ch⁰([1_M3])=(0,0,3)
                                                       [S84 W10, eq II.2-5/6/7; ch_matrix=diag(1,1,3)]
Substitute: K_0(A_F) = K_0(ℂ)⊕K_0(ℍ)⊕K_0(M_3(ℂ)) = ℤ⊕ℤ⊕ℤ = ℤ³
Simplify:   class of a configuration = rank-triple (n_ℂ,n_ℍ,n_M3) ∈ ℤ³
            ch⁰(P_pre)  = ch⁰(1_ℂ)+ch⁰(1_ℍ)+ch⁰(1_M3) = (1,0,0)+(0,2,0)+(0,0,3) = (1,2,3)
            ch⁰(P_post) = (1,2,3)  [the 279 tachyonic dirs are INNER FLUCTUATIONS
                                    D_K → D_K + A + JAJ⁻¹, A = Σ aᵢ[D_K,bᵢ], aᵢ,bᵢ ∈ A_F (Connes);
                                    they deform D_K WITHIN A_F; Wedderburn minimal central
                                    idempotents of a semisimple algebra are UNIQUE ⇒ rigid]
Canonical form: K0_class_change ⟺ (n_ℂ,n_ℍ,n_M3)_post ≠ (…)_pre
Read off:   (1,2,3) = (1,2,3) component-wise  ⇒  K0_class_change = FALSE
Conclusion: NO Sen-type descent. The supersonic transit does NOT carry a K-theoretic charge change;
            the tachyon is a fluctuation within a fixed K_0 class. G-1 stays open.
```

**Why the transit cannot jump the class (structural core)**: a Sen condensation in Witten's picture changes `K⁰(X)` because the brane *bundle* changes while spacetime `X` is fixed. The framework's analog of "spacetime" is the algebra `A_F`, which is FIXED by the NCG axioms; the analog of "the bundle" is the minimal-central-idempotent decomposition — but that is RIGID (Wedderburn-Artin: the minimal central idempotents of a semisimple algebra are unique). The transit `D_K(τ)` is a continuous deformation of the *Dirac/metric data* (inner fluctuations), not of `A_F`; by K-theory homotopy invariance a projector's K_0 class is constant under such deformation. The numerical witness confirms this: the band-0 ground spectrum spreads by 2.31 M_KK across the sectors (the deformation is large and real), yet the per-triality-class Wedderburn sector partition is structurally invariant across every L_max ∈ {8,9,10,11,12} truncation — the eigenvalues move, the class does not.

**Substrate framing** (phononic-framing.md): GEOMETRIC. Explanation flows substrate-first — σ(D_K) → the 279 tachyonic inner fluctuations (the substrate's own unstable directions at the fold) → the tachyonic-flow endpoint → the K_0(A_F) class of that endpoint → whether a Sen descent occurred. The substrate IS the spectral triple (A_F, H_K, D_K); the K_0 class is an INTRINSIC substrate-IS invariant, NOT a property the substrate has IN a 10d brane background. Sen condensation is a string WALL-measurement (string theory = walls, substrate = interior): we read the substrate's own transit dynamics through the K-theory wall and find it does NOT exhibit the charge-changing signature. **Cross-framework note**: the relevant K-theory is `K_0(A_F)=ℤ³` (Wedderburn rank-triple on the finite NCG algebra), NOT Witten's `K⁰(X)=ℤ` (rank-1, 10d spacetime) — a genuinely different mathematical object (SU(3) is not Calabi-Yau; the framework is not a string compactification). **Solution-space consequence**: the SUM-vs-NO-SUM "different road" the framework takes for ∫Dg is NOT a Sen flow; gap G-1 (a notion of dynamical configuration-change without ∫Dg) stays open, and the Ordered-Veil information-completeness mechanism (C-1) is NOT imported from string K-theory — it must be sought elsewhere. This narrows the candidate space: the framework's tachyon condensation is categorically distinct from the string-theoretic one at the K-theory layer.

---

### §W2-2. INV9-W2-2-DS-ENTROPY-SUBSTRATE-SPECIES-COUNT (string-theory-theorist)

**Status**: COMPLETED
**Gate ID**: `INV9-W2-2-DS-ENTROPY-SUBSTRATE-SPECIES-COUNT`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (dS entropy as a finite substrate species-count)
**Agent**: `string-theory-theorist` (+ hawking-theorist methodological anchor for the Gibbons-Hawking S_dS horizon-thermodynamics side)
**Hypothesis**: The de Sitter (Gibbons-Hawking) entropy is reproduced to O(1) by a finite substrate species-count — log(number of D_K eigenvalues in the species shell [M_KK, 2.06 M_KK] at the fold) ≈ S_dS = 3π/(Λ ℓ_P²) with Λ from the a₀^ζ moment — supplying the entropic CC mechanism (C-2) via a non-holographic bulk mode count.
**Plan reference**: `sessions/investigation/investigation-9/investigation-9-plan-w2.md` §W2-2 (machinery pin, MANDATORY substitution chain, `regulator_pin=a_0^{ζ}`, Λ-scale crux).

**Verdict**: **INFO** (composite). `r = |S_count − S_dS|/S_dS = 3.41` falls in the pre-registered INFO band (1.0, 10.0] — **order-right, but NOT a clean O(1) match**. 3-tuple: `sign_verdict=N/A` (magnitude-agreement gate, no signed directional prediction), `magnitude_verdict=INFO`, `regime_verdict=MARGINAL` (the species shell is L_max-SATURATED — VALID on that axis — but the substrate-scale Λ FORM is ambiguous at the OOM level, the marginal axis). Composite collapse: `magnitude=INFO ⇒ INFO`.

**Output Artifacts** (closure-verification checklist; all on disk, content-verified):
- **script** `computations/investigation-9/inv9_w2_ds_entropy_species_count.py` (28083 B) — contains `from canonical_constants import` (Section 1) + `print_verdict_payload` (Section 6). VERIFIED.
- **data** `computations/investigation-9/inv9_w2_ds_entropy_species_count.npz` (11259 B) — N_shell, S_count, S_dS (substrate/alt/observed), r, L_max-invariance flags, all canonical pins. VERIFIED.
- **plot** `computations/investigation-9/inv9_w2_ds_entropy_species_count.png` (124318 B) — entropy ladder (substrate-scale vs observed-Λ contrast, log axis) + verdict-numbers panel. VERIFIED.
- **verdict line** `computations/investigation-9/inv9_gate_verdicts.txt` — `INV9-W2-2-DS-ENTROPY-SUBSTRATE-SPECIES-COUNT: INFO -- value='3.4135870628092553' ... audit_sha256=fe4240bc910a87d1d5440b244a9836978a9e6d6f931800d7fff8a6761da73cde content_sha256=254e4698cf3bd50efee684967eac83e617ddb64dc562e834b01226189bde3e86 schema_version=S84+` + dual-SHA companion row + schema-v2 3-tuple row (`sign=N/A magnitude=INFO regime=MARGINAL`) + 5 companion `#`-rows (regulator_pin, publication_precision, WHICH_Λ, Λ-form-ambiguity, shell-L_max-invariance). Emitted race-safe via `emit_verdict(session=9, track="investigation")`. VERIFIED.

**Verdict-line closure** (compute gate, `[SIGN]` trigger): dual-SHA computed in-script (`audit_sha256` over [script ‖ canonical_constants.py ‖ pinmap_json]; `content_sha256` over script bytes). The script PRINTED the payload via `print_verdict_payload`; emitted via the `emit_verdict` MCP tool (no raw `open("a")`). The schema-v2 3-tuple companion row is present (`[SIGN]` requirement). `regulator_pin=a_0^{ζ}` + `publication_precision=3` carried as `extra_rows`.

**MCP Pre-Compute Audit** (query-first discipline, executed before writing the script):
- `search_knowledge("de Sitter entropy species count Gibbons-Hawking")` → `S_dS = 3π/(Λℓ_P²) = A/4G` (s43_cc_113_workshop, Paper 07); S=N_species·A/(4G_N) species-counting framing (session-17d); S61 `s61_bekenstein_desitter` computes `S_dS = 3.263e122 nats` at the OBSERVED Λ (the ~10^122 CC problem — the WRONG Λ for this gate). NOT pre-closed; the species-count functional is FRESH.
- `search_knowledge("species scale Lambda_sp M_KK 2.06 EFT breakdown shell")` → `Lambda_sp_over_M_KK = 2.06` (gate S63-SPECIES-36/SCALE-63; THIN EFT-breakdown shell [M_KK, 2.06 M_KK]); W6-SPECIES-36 THIN PASS.
- `get_constant("a_0_FW_zeta")` → 6440.0 (S88-A-N-FW-CANONICALIZATION; ζ-regulated zeroth Seeley-DeWitt moment, `a_0 = ζ_{D_K}(0) = Tr(1)`). **This is the regulator-pinned Λ source — NOT the raw 155984 degeneracy count.**
- `get_constant("Lambda_sp_over_M_KK")` → 2.06 (S96; source `s63_species_scale.npz`).
- `get_constant("M_KK")` → 7.428660036284456e16 GeV (CONST-FREEZE-42; gravity route alias).
- `get_constant("M_Pl_reduced")` → 2.435e18 GeV (CODATA 2018).
- `get_constant("f_0_sharp")` → 1.0; `get_constant("f_2_default")` → 2.34 (S62 W1 / S72; spectral-functional f-moments for the `(2 f_0/f_2)·a_0` vacuum-energy prefactor).
- `search_knowledge("Lambda_cc = (2 f_0/f_2) a_0 spectral action vacuum energy")` → `Lambda_cc = (2 f_0/f_2)·a_0` (session-39-naz-hawking-workshop); `Lambda_SA = (f_0/f_2)·(a_0/a_2)·M_KK²` (session-64, the DIMENSIONAL form supplying the M_KK² scale factor). **PRE-CLOSED on the Λ-path identity; FRESH on the species-count↔dS-entropy comparison.**

**Results** (numbers first; 3 sig figs published per `publication_precision=3`):

| Quantity | Value | Source / definition |
|:--|:--|:--|
| species shell [lo, hi] | [1.00, 2.06] M_KK | `Lambda_sp_over_M_KK = 2.06` (S63-SPECIES-36) |
| **N_shell** (unique-per-sector) | **3360** | `#{stored |λ| ∈ [1.0, 2.06]}` over Peter-Weyl sectors p+q≤10 |
| N_shell (dim-weighted, alt) | 79938 | SU(3)-multiplicity-weighted shell count |
| shell L_max-INVARIANT | **True** (N@L10 = N@L12 = 3360) | Friedrich-Bär saturation: shell fully resolved at L_max=10 |
| total cardinality (unique) | 78080 | matches canonical `phononic-framing.md` 78,080-unique figure (read-correctness check) |
| **S_count = log(N_shell)** | **8.12** | substrate species-count entropy (canonical) |
| S_count (dim-weighted) | 11.3 | alt reading |
| moment prefactor (2 f₀/f₂)·a₀^ζ | 5504 | dimensionless |
| Λ_substrate = pref·M_KK² | 3.04e37 GeV² | substrate-scale CC |
| Λ·ℓ_P² (ℓ_P²=1/M_Pl,red²) | 5.12 | dimensionless |
| **S_dS (substrate-scale)** | **1.84** | `3π/(Λ ℓ_P²)` — genuinely O(1) |
| S_dS (alt a₀/a₂ form, X-check) | 1.02e4 | `(f₀/f₂)(a₀/a₂)M_KK²` — Λ-form ambiguity |
| S_dS (OBSERVED Λ, X-check) | 8.98e120 | `Λ=3H₀²` — the ~10^122 CC problem (WRONG Λ) |
| **r = \|S_count − S_dS\|/S_dS** | **3.41** | canonical gate value |
| r (dim-weighted N_shell) | 5.14 | alt reading |
| 3-tuple | sign=N/A, magnitude=INFO, regime=MARGINAL | |

**MANDATORY substitution chain** (per `math-scripts.md §"Double-Check Logic Before Compute"`; the [SIGN] magnitude claim "log(count) matches S_dS to O(1)"):

```
Claim: "log(#{|λ| ∈ [M_KK, 2.06 M_KK]}) matches Gibbons-Hawking S_dS to O(1)."

Step 1  N_shell = #{ |λ| ∈ spec(D_K) : 1.0 ≤ |λ|/M_KK ≤ 2.06 }   [shell cardinality; Lambda_sp_over_M_KK=2.06]
        = 3360 (unique-per-sector, L_max=10; L_max-INVARIANT vs L_max=12 by Friedrich-Bär saturation)
Step 2  S_count = log(N_shell) = log(3360) = 8.1197         [substrate species-count entropy, B-4]
Step 3  a_0^ζ = 6440.0                                       [ζ-regulated zeroth Seeley-DeWitt moment; regulator_pin=a_0^{ζ}]
Step 4  Λ = (2 f_0/f_2)·a_0^ζ · M_KK²                        [spectral-action vacuum-energy path; session-39 prefactor × session-64 M_KK² scale]
        = (2·1.0/2.34)·6440·M_KK² = 5504.27·M_KK² = 3.0375e37 GeV²   [SUBSTRATE-SCALE, NOT observed-DE]
Step 5  ℓ_P² = 1/M_Pl,red² = 1/(2.435e18)² = 1.6866e-37 GeV⁻²   [REDUCED-Planck convention, declared in convention field]
        Λ·ℓ_P² = 3.0375e37 · 1.6866e-37 = 5.1230   (dimensionless ✓)
Step 6  S_dS = 3π/(Λ ℓ_P²) = 3π/5.1230 = 1.8397       [Gibbons-Hawking; A/4G with H²=Λ/3]
Step 7  r = |S_count − S_dS|/S_dS = |8.1197 − 1.8397|/1.8397 = 3.4136

Direction: NO directional sign pre-registered — the claim is a MAGNITUDE agreement |·| ≤ O(1);
           sign_verdict = N/A. The PASS/INFO/FAIL band is on |r|: PASS r≤1.0; INFO 1.0<r≤10.0; FAIL r>10.0.
Read-off:  r = 3.41 ∈ (1.0, 10.0]  ⇒  magnitude_verdict = INFO (order-right, not O(1)).
Conclusion: S_count (8.12) and the SUBSTRATE-SCALE S_dS (1.84) are the SAME ORDER (a handful of nats each),
           in stark contrast to the OBSERVED-Λ S_dS ≈ 9e120. The species-count is the right ORDER for the
           substrate-scale dS entropy, but the strict O(1) match is not clean. B-4 does NOT close in this
           naive bare-shell-cardinality form; it is order-right.
```

**The load-bearing regulator-class separation** (why `regulator_pin=a_0^{ζ}` is MANDATORY): `S_count = log(N_shell)` is an **algebra-INVARIANT spectrum-only functional** — a cardinality of the eigenvalue set, **regulator-INDEPENDENT** (counting eigenvalues does not invoke a UV regulator). `S_dS` depends on Λ, which is **regulator-DEPENDENT** through `a_0^ζ` (the ζ-regulated moment; a different regulator gives a different a_0 hence a different Λ). The two sides of the comparison live on DIFFERENT regulator-sensitivity axes. The raw degeneracy-weighted count **155984 = a₀ raw is NOT used for Λ** — only the shell subset N_shell feeds S_count, and `a_0^ζ = 6440` feeds Λ. Using 155984 for both would be a `UV_REGULARIZATION_CONFLATION` error. ✓ disclosed in the verdict `extra_rows`.

**The WHICH-Λ crux** (orchestrator override; the plan's pre-registered crux): the O(1) match is a **SUBSTRATE-SCALE** statement. At the substrate scale, `Λ = (2 f₀/f₂)·a₀^ζ·M_KK² ≈ 5504·M_KK²`, giving `S_dS ≈ 1.84` (O(1)). At the **observed** dark-energy scale, `Λ = 3H₀² ≈ 6.2e-84 GeV²`, giving `S_dS ≈ 9e120` — the ~10^122 CC problem that **DILUTION-CC** (closed S66, 114-OOM via the Volovik tracking vacuum) already addresses, a **DIFFERENT** question. The `convention=...-SUBSTRATE-SCALE` field declares the choice; the observed-Λ value is computed in-script purely as the auditable contrast. The `regime_verdict=MARGINAL` flags the residual Λ-FORM ambiguity: the plan-pinned `(2 f₀/f₂)·a₀^ζ` prefactor (5504) and the dimensionally-cleaner session-64 `(f₀/f₂)·(a₀/a₂)·M_KK²` form (prefactor 0.99, dividing by `a₂≈2776`) differ by ~a₂ ≈ 5552×, inflating S_dS from 1.84 to ~1.02e4. The O(1) headline holds ONLY for the plan-pinned prefactor form.

**L_max discipline**: `L_max_plan = 12` (cache `s84_spectrum_cache_L12_tau019.npz` stored at L_max=12) / `L_max_operational = 10` (Friedrich-Bär saturation truncation, p+q≤10). The species shell `[M_KK, 2.06 M_KK]` is **fully resolved at L_max=10**: N_shell = 3360 at BOTH L_max=10 and L_max=12 (the shell is populated only by low-(p,q) sectors; higher L_max adds modes ABOVE the shell). This makes the operational truncation rigorous and the regime VALID on the saturation axis.

**Substrate framing** (per `phononic-framing.md`): PHONONIC. The species-count is a count of the substrate's accessible **vibrational modes** below the species scale — the D_K eigenvalues in `[M_KK, 2.06 M_KK]` ARE the substrate excitations that can be populated before the EFT breaks. Explanation flows substrate-first: `σ(D_K) → N_shell (the substrate's own finite mode count) → S_count = log(N_shell) → comparison to S_dS`. The substrate IS the spectral content; the dS entropy is NOT something the substrate has IN a de Sitter container — the de Sitter horizon is an **emergent acoustic surface** (the acoustic white hole / supersonic transit), and its entropy is read off the substrate's intrinsic mode count, NOT a boundary central charge. This is the B-4 bridge: where AdS holography reads entropy off a boundary CFT central charge (WRONG sign, infinite), the framework reads it off a **finite, non-holographic bulk species-count** (right sign, finite). **Cross-framework note** (string-theoretic pedigree): Dvali's species-scale argument (`Λ_sp ~ M_Pl/N^{1/(d−2)}`, arXiv:0706.2050) ties the gravitational cutoff to the species number, and the Bekenstein-Hawking entropy of a species-scale region COUNTS the species — but the natural string-side relation is `S_horizon ~ N` (extensive, area-law, LINEAR in N), whereas the gate's `S_count = log(N)` is the **Boltzmann/microcanonical** count (entropy of a system that can occupy any of N states). These are **different functionals of N**; the INFO verdict's "order-right but not O(1)" is precisely the signature that the framework's finite mode-count is dS-entropy-LIKE but not the same functional — exactly the FAIL/INFO branch the plan anticipated ("the count may need a different shell, a degeneracy weighting, or a different entropy functional").

**Solution-space consequence** (constraint-map update; per `epistemic-discipline.md`): this is a **boundary result**, not a closure. The corridor it constrains: the **bare-shell-cardinality `log(N_shell)`** form of the B-4 species-counting entropic-CC mechanism does NOT produce a clean O(1) match to the substrate-scale Gibbons-Hawking entropy (r=3.41, INFO). What SURVIVES: (i) the substrate-scale dS entropy IS O(1) (1.84) — the framework does NOT inherit the ~10^122 catastrophe at the substrate scale (consistent with DILUTION-CC handling the observed-Λ leg separately); (ii) the species shell is a genuine, FINITE, regulator-INVARIANT, L_max-saturated mode count (3360) — a well-defined non-holographic bulk object (consistent with A-3 as-constructed non-holography). What this PRUNES forward: the entropic-CC mechanism, IF it exists, needs either the LINEAR-in-N (extensive area-law `S ~ N`) functional rather than `log N`, or a different shell / degeneracy weighting. The Λ-form ambiguity (factor ~a₂) is a SEPARATE compute carry-forward (pin the substrate-scale Λ form: `(2 f₀/f₂)·a₀^ζ·M_KK²` vs `(f₀/f₂)·(a₀/a₂)·M_KK²`). **All of this is internal-consistency mapping, NOT a prediction of the framework** (swampland/species-scale comparisons are wall-measurements of the substrate interior per my standing methodology rule).

**Dual prior update** (plan pre-registered): `magnitude_verdict=INFO ⇒ unchanged, route to a Λ-scale-pinning CF` (the plan's INFO discriminator). Track A (0.4, entropic mechanism found) / Track B (0.6, numerical near-miss) — the INFO leaves the prior unchanged and routes the Λ-scale + entropy-functional refinement as carry-forward; it does NOT shift mass to either track. (Probability/confidence weighting is Skeptic's domain; recorded here only as the pre-registered discriminator outcome.)

**Carry-forward** (4-field, genuine future compute): (1) **What**: recompute S_dS with the LINEAR species-count `S ~ N_species·A/(4G)` (extensive area-law) instead of `log(N_shell)`, AND disambiguate the substrate-scale Λ form. (2) **Inputs**: `inv9_w2_ds_entropy_species_count.npz` (N_shell=3360, both Λ forms), `a_0_FW_zeta`, `a_2_FW_zeta`, `f_0_sharp`, `f_2_default`. (3) **Gate**: `|S_extensive − S_dS|/S_dS ≤ 1.0` for the extensive reading; separately, pin which `(f₀,f₂,a₀,a₂)` combination is the substrate-natural Λ via a Λ-form-selection workshop. (4) **Effort**: 1 session (the npz + canonical pins are on disk; the recompute is a closed-form re-evaluation). Session-promotion required for any permanent landing (investigation track-local boundary).

---

### §W2-3. INV9-W2-3-MODERN-SWAMPLAND-REFRESH (string-theory-theorist)

**Status**: LANDED (2026-06-16) — review gate; closes by artifact-existence-with-content (NO verdict line, per `gate-verdicts.md §"Investigation-Track Canonical Path"`). Deliverable: `investigation-9-swampland-refresh-synthesis.md` (30,474 B; all 9 `must_contain` markers present). **Headline:** the 38-closure pre-2018 swampland audit SURVIVES the 2018–2025 refresh — refined dS / sharpened Distance / Dvali species scale all CONSISTENT, Emergent String classified (τ→0 decompactification, large-τ emergent-string candidate by-analogy). No new structural TENSION; R-3 library gap closed for this sub-domain. Sharpest fresh claim: the large-τ emergent-string leg (decider = WORLDSHEET-BOUNDARY-62 critical dim, CF-INV9-W2-WORLDSHEET-DIM).
**Gate ID**: `INV9-W2-3-MODERN-SWAMPLAND-REFRESH`
**Trigger**: `[VERIFY]`
**Classification**: **NON-PHONONIC** (methodology / cross-framework swampland audit)
**Agent**: `string-theory-theorist` (review executor, solo per the review block; NOT a numerical-compute executor)
**Hypothesis**: The framework's pre-2018 swampland audit (38 closures, all CONSISTENT) remains CONSISTENT (or develops a specific named TENSION) against the 2018–2025 conjectures — refined dS (OPSV-2018), sharpened Distance, Emergent String (LLW-2019), Dvali species scale — and the infinite-distance τ-limits classify cleanly under the Emergent-String dichotomy.
**Plan reference**: `sessions/investigation/investigation-9/investigation-9-plan-w2.md` §W2-3 (review block: sources, paper-search FETCH targets, per-conjecture audit spec).

**Closure type**: **artifact-existence-with-content** — review gate, **NO verdict line** (per `gate-verdicts.md §"Investigation-Track Canonical Path"`: only compute/solo gates emit verdict lines; review gates close on the synthesis md, same closure semantic as a METHODOLOGY-class wave per `wave-classification.md §M1`).

**Output Artifacts** (artifact-existence checklist; the deliverable IS the synthesis md):
*(pending — confirm the synthesis md exists (`ls "sessions/investigation/investigation-9/investigation-9-swampland-refresh-synthesis.md"`) AND paste `grep -E '<must_contain>' <path>` output for every plan `must_contain` marker: `## ` (≥1 section header); `Refined de Sitter` (conjecture 1 tagged); `Distance Conjecture` (conjecture 2 tagged); `Emergent String` (conjecture 3 — the dichotomy classification); `species scale` (conjecture 4 — Dvali species scale); `(CONSISTENT|TENSION|classified)` (per-conjecture verdict present); `(decompactification|emergent-string)` (Emergent-String dichotomy verdict on the τ-limits); `τ→0|tau->0|τ → 0` (the τ→0 limit classified); `large-τ|large-tau|large τ` (the large-τ limit classified). A LANDED close requires the md to exist with ALL markers present. A partial primary-source fetch is NOT a NOT-LANDED state IF the affected conjecture is tagged `classified-from-survey-structure-pending-primary-fetch` (LANDED-with-disclosed-gap). NO verdict-file line; NO byte/line targets — content-presence only. If a marker is absent → NOT LANDED → orchestrator SendMessage write-only continuation to the same agentId.)*

**MCP Pre-Compute Audit** (review-gate analog — knowledge-MCP "check-if-known" pre-step BEFORE the paper-search fetch):
*(pending — list the `mcp__knowledge__*` queries executed before the paper-search fetch + write, with one-line salient return each; mark PRE-CLOSED if a closure already covers a conjecture's status. Per `.claude/rules/knowledge-index-usage.md`. Suggested: `search_knowledge("swampland conjecture de Sitter distance emergent string")`, `trace_entity("swampland status")`, `get_constant("w0_FW")`, `get_constant("Lambda_sp_over_M_KK")`, `get_constant("delta_tau_crit_pos")`. THEN the paper-search fetch (OPSV-2018 arXiv:1810.05506, LLW-2019 arXiv:1910.01135, Dvali species-scale arXiv:0706.2050) via `search_arxiv` + `download_arxiv`/`read_arxiv_paper` — avoid `search_google_scholar` per the shared-IP rate-limit note; discovery via `search_arxiv` + WebSearch.)*

**Verdict**:
*(pending agent execution — review gates close LANDED / NOT-LANDED by artifact-existence, NOT PASS/FAIL/INFO)*

**Results** (the synthesis md is the deliverable):
*(pending — include: the synthesis at `sessions/investigation/investigation-9/investigation-9-swampland-refresh-synthesis.md` carrying, for EACH of the four modern conjectures, a CONSISTENT/TENSION/classified verdict + the specific deciding substrate quantity — (1) refined dS OPSV-2018 vs |S'|/S ≥ 0.23, w0_FW = −0.918, gradients c=3.52 cutoff / c~6.6 zeta vs the c~O(1) bound, the tachyonic-φ min(V'')<0 clause; (2) sharpened Distance vs Δφ/M_Pl = 0.170 [SEED-AUTHOR survey value, NOT a canonical pin — flag provenance; closest canonical delta_tau_crit_pos = 0.175]; (3) Emergent String LLW-2019 dichotomy verdict on BOTH τ→0 (cold-big-bang unstable maximum) and large-τ infinite-distance limits (decompactification vs emergent-string); (4) Dvali species scale vs Λ_sp/M_KK = 2.06 THIN, internal-consistency check against N_shell from W2-2; the per-conjecture primary-source status (fetched vs `classified-from-survey-structure-pending-primary-fetch`); substrate-first framing — swampland conjectures are WALL-MEASUREMENTS, a CONSISTENT tag is internal-consistency confirmation NOT a prediction)*

---

## Wave 2 Synthesis (team-lead)

Two compute gates closed FAIL / INFO; the review gate LANDED. Gate-type mix honored: W2-1/W2-2 carry verdict lines + dual-SHA; W2-3 closed by artifact-existence (no verdict line).

- **INV9-W2-1 (Sen-tachyon-K-theory-descent) — FAIL.** `ch⁰(P_post)=ch⁰(P_pre)=(1,2,3)`; K₀(A_F)=ℤ³ **invariant** under the supersonic transit (band-0 |λ| spreads 2.31 M_KK — the deformation is large/real — yet the per-triality Wedderburn partition is invariant across L_max∈{8..12}). *Structural reason:* the transit is an inner fluctuation (D_K→D_K+A+JAJ⁻¹, A∈A_F) that deforms the metric/connection within A_F; A_F is fixed by the NCG axioms and its minimal central idempotents are Wedderburn-rigid ⇒ K-theory homotopy invariance forbids a class jump. *Constraint-map:* the framework's tachyon is categorically **unlike** Sen's at the K-theory level (K₀(A_F)=ℤ³ ≠ Witten K⁰(X)=ℤ); the ∫Dg substitute is **not** a Sen flow; gap G-1 stays open. Direct evidence for the W3-1 adjudication (a Sen flow cannot defend a SUM reading).
- **INV9-W2-2 (dS-entropy-species-count) — INFO.** `r = |S_count − S_dS|/S_dS = 3.41`, in the pre-registered INFO band (1.0, 10.0] — order-right, **not** a clean O(1) match. 3-tuple `sign=N/A` (magnitude-agreement gate), `magnitude=INFO`, `regime=MARGINAL` (species shell is L_max-SATURATED — VALID on that axis — but the substrate-scale Λ FORM is OOM-ambiguous, the marginal axis). Load-bearing regulator discipline honored: `N_shell` (regulator-INVARIANT cardinality) vs Λ from `a_0^{ζ}` (regulator-DEPENDENT) kept un-conflated. *Constraint-map:* species-count is the **right order** for dS entropy at the substrate scale but the O(1) match is not clean — the non-holographic species-counting CC mechanism (C-2) is plausible-but-unconfirmed pending Λ-scale pinning.
- **INV9-W2-3 (modern-swampland-refresh) — LANDED.** 30,474-byte synthesis; all four 2018–2025 conjectures fetched in full (OPSV-2018, OOSV-2018, LLW-2019, Dvali-Redi). Verdicts: refined dS **CONSISTENT** (reaches clause-3 via the same η-problem mechanism OPSV invoke — derivation-level rhyme); sharpened Distance **CONSISTENT** (Δφ/M_Pl=0.170 sub-Planckian 5.9×, provenance-flagged as seed-author not canonical); Emergent String **classified** (τ→0 ↦ decompactification, large-τ ↦ emergent-string *candidate*, classified-by-ANALOGY since SU(3)≠Calabi-Yau); Dvali species scale **CONSISTENT** + scale-type-pin caveat. *Headline:* the 38-closure pre-2018 audit **survives** the modern refresh — no new structural TENSION; the 7-year swampland-library gap (R-3) is closed for this sub-domain. The **large-τ emergent-string leg** is the framework's sharpest falsifiable swampland-side claim (stands/falls on WORLDSHEET-BOUNDARY-62 critical dimension).

**Wave 2 → Wave 3 branching (as it resolved):** W2-1 FAIL (K₀ invariant) → W3-1 weighting of string's no-sum reading (a Sen flow is not the ∫Dg substitute); W2-2 INFO → the finite-trace mechanism is order-right but unconfirmed; W2-3's Emergent-String classification informs the broader cross-framework-character discussion (W3-2 lens).

## Carry-Forward Computations

### CF-INV9-W2-LAMBDA-SCALE — dS-entropy Λ-scale pinning + shell refinement
| Field | Value |
|:--|:--|
| What | Pin the substrate-scale Λ form (a_0^ζ-derived vs alternative moment paths) and refine the species shell; re-test `|S_count − S_dS|/S_dS` for an O(1) match |
| Inputs | `s84_spectrum_cache_L12_tau019.npz` N_shell; `a_0_FW_zeta=6440.0`; the W2-2 `.npz` (r=3.41 baseline); cc-path-a Λ_cc machinery |
| Gate | `r ≤ 1.0` (O(1) PASS) at a pinned substrate-scale Λ |
| Effort | ~1 session |

### CF-INV9-W2-WORLDSHEET-DIM — WORLDSHEET-BOUNDARY-62 critical-dimension (emergent-string-leg decider)
| Field | Value |
|:--|:--|
| What | Compute the Voronoi-boundary Nambu-Goto effective central charge / critical dimension; decide whether the large-τ limit is a genuine LLW-2019 emergent-string limit or only an analogy |
| Inputs | WORLDSHEET-BOUNDARY-62 apparatus; the W2-3 synthesis §Emergent-String; `c_eff` machinery |
| Gate | `c_eff` matches a critical-string value (emergent-string CONFIRMED) vs not (analogy-only) |
| Effort | ~1–2 sessions |

### CF-INV9-W2-DVALI-PIN — Dvali species scale-type consistency (ratio-vs-cutoff)
| Field | Value |
|:--|:--|
| What | Pin the Dvali scale-type (ratio vs cutoff) and check the framework N reproduces Λ_sp/M_KK=2.06 via the Dvali formula |
| Inputs | W2-2 `N_shell`; `Lambda_sp_over_M_KK=2.06`; Dvali `Λ_sp ~ M_Pl/N^{1/(d-2)}` |
| Gate | Dvali-formula N consistent with 2.06 within O(1) |
| Effort | ~0.5 session |

**Session-promotion non-math** (designated-writer / track-local boundary): the substrate-first Δφ/M_Pl re-pin (W2-3 V.1) and any swampland-falsifier-inventory row (mack sole-writer) are recorded in `investigation-9-housekeeping.md §B/§D`. W2-1's refined-endpoint-construction is a possible but low-priority CF (the FAIL is fairly decisive) — not promoted.

## Constraint-Map Updates
| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-06-16 | Sen-tachyon K-theory descent (W2-1) | untested (transit-as-Sen-flow) | CLOSED — K₀ invariant | inner fluctuation deforms D_K not A_F; Wedderburn-rigid; G-1 open |
| 2026-06-16 | dS-entropy species-count / C-2 (W2-2) | untested entropic CC mechanism | order-right, O(1) unconfirmed (INFO) | r=3.41; regime=MARGINAL on Λ-scale form |
| 2026-06-16 | Swampland audit vs 2018–2025 (W2-3) | pre-2018, 38 closures | SURVIVES refresh, no new TENSION | 4 modern conjectures CONSISTENT/classified; R-3 gap closed |
| 2026-06-16 | Large-τ emergent-string leg (W2-3) | unstated | sharpest falsifiable swampland claim; decider = WORLDSHEET-BOUNDARY-62 | LLW-2019 dichotomy classified-by-analogy |

## Files Produced
| Gate | Script | Data | Plot | Synthesis md | Verdict-line |
|:--|:--|:--|:--|:--|:--|
| INV9-W2-1 | `inv9_w2_sen_tachyon_k_theory_descent.py` | `.npz` | `.png` | — | FAIL (audit `1b82dc76…`) |
| INV9-W2-2 | `inv9_w2_ds_entropy_species_count.py` | `.npz` | `.png` | — | INFO (audit `fe4240bc…`) |
| INV9-W2-3 | — (review) | — | — | `investigation-9-swampland-refresh-synthesis.md` (30,474 B) | none (artifact-existence) |
