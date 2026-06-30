# S103 Review — `papers/monotonicity/main.tex`

**Paper**: "Monotonicity of the Spectral Action Under Volume-Preserving Deformations of SU(3)"
**Authors (paper)**: MemeTheory & Claude Opus 4.6
**Paper era**: ~March 2026 (framework ~S50–S53; the *physics* is the S17a–S45 spectral-action lineage)
**Review date**: 2026-06-12 (framework post-S103)
**Reviewer**: Spectral-Geometer
**Sources consulted**: knowledge MCP (`search_knowledge`, `trace_entity`, `get_constant`); `sessions/framework/ARCHIVE/spectral-post-mortem.md` (the canonical lineage post-mortem, ARCHIVED 2026-05-10 — its *content* survives, see §4); `sessions/framework/phonic-exflation-equation.md §1.3a / §5.1` (capstone E7); `sessions/framework/Atlas/atlas-07-permanent-results.md` (A2/E7/Chebyshev); `sessions/framework/Atlas/atlas-09-retractions.md` (Items 4, 35, 44, 45); `sessions/permanent-results-registry.md`; `computations/_shared/canonical_constants.py` (via `get_constant`); legacy paper memory `papers/cmpp-classification/.claude/agent-memory/spectral-geometer/`.

---

## Orientation: the one structural fact that governs this review

The theorem is **alive and PERMANENT**. What has drifted is the **interpretive frame**. The paper was written when the project still hoped the spectral action would *select* τ at the fold (a moduli-stabilization minimum). The post-mortem (`spectral-post-mortem.md §10`, "The Framing Error: There Is No 'Now'") and the S37 paradigm shift killed that frame: the substrate **transits** through the fold; it is never trapped. The current canon (capstone §1.3a, §5.1) reads the *same monotonicity theorem* as the **engine of transit** — `e^{−S(τ)}` is monotone ⇒ `Z` has no interior saddle in τ ⇒ boundary-dominated path integral ⇒ the universe transits rather than settling. The math is identical; the conclusion's sign of intent is inverted (no-well-to-roll-into → monotone-ramp-that-drives-transit).

The paper's §1 (Intro), §3 (SD coefficients), §4 (Structural theorem) are sound mathematics that survive almost verbatim. The casualties are concentrated in **§5 (Consequences) and §6 (Conclusion outlook)**, which frame the result as a *moduli-stabilization* result and ask "what additional structure stabilizes τ" — a question the register now answers (nothing does; it transits, and that is by design, not a deficiency).

A second, subtler obligation: the paper sits on top of a sign-convention split (`S_f` decreasing for UV-suppressing `f` vs the canonical `dS/dτ = +58,673` for the linear/increasing-`f` reading). The paper is internally sign-coherent, but the rewrite must state the convention explicitly so a reader does not collide the paper's "monotonically decreasing `S_f`" against the registry's "`dS/dτ > 0`". See §1 row [S-CONV] and §3.

---

## §1 Claim-audit table

Status legend: **CURRENT** (matches register) · **DRIFTED** (numerically/notation off, fixable) · **SUPERSEDED** (frame/claim replaced by a later result) · **RETRACTED** (register marks it broken) · **STILL-OPEN** (open in register, paper may over- or under-claim).

| # | Load-bearing claim (paper) | Paper's version | Current canonical (+ source) | Status |
|:--|:--------------------------|:----------------|:-----------------------------|:-------|
| C1 | Scalar curvature `R(τ)` monotone increasing; `dR/dτ = x^{-2}(x³−1)² ≥ 0` | Prop. 4.4 (analytic proof) | E3 capstone L199 `R_K(τ)=−¼e⁻⁴ᵗ+2e⁻ᵗ−¼+½e²ᵗ`, R-monotonicity PROVEN (S64, AM-GM); `dR/dτ>0` | **CURRENT** |
| C2 | `R(0)=2`, `R(0.19)=2.018`; `\|Ric\|²(0)=½`, `\|Riem\|²(0)=½`; Einstein `Ric=¼g` at τ=0 | §3.3 + appendix | `R_scalar(g_biinv)=2.0`; capstone L199 `R_K(0.19)=2.018`; 147/147 Riemann checks | **CURRENT** |
| C3 | `a_0(τ)` constant (volume-preserving); `da_0/dτ=0` | Thm 5.1(i) | Volume-preserving TT exact, `det g_τ=3⁸=6561 ∀τ` (capstone L184, Sage) | **CURRENT** |
| C4 | `a_2(τ) ∝ R(τ)` monotone increasing | Thm 5.1(ii) | E7 chain `a_{2k} monotone`; atlas-07 A2; geometric `a_2^{SD}(fold)=0.728235` (Gilkey exact) | **CURRENT** |
| C5 | `a_0…a_6` individually monotone; "all a_{2n}" NOT claimed | Contributions §1; Thm 5.1 | atlas-09 **Item 4 (CORRECTION, S27)**: only a_0–a_6 proven; beyond a_6 is conjecture | **CURRENT** (paper correctly scopes) |
| C6 | Effective `â_2` decreasing, `â_4` increasing(→0⁻), `â_6` decreasing (truncated p+q≤3) | Thm 5.1(iv), Table 1, Fig 1 | These are *spectral-sum* effective coeffs, distinct object from geometric Gilkey `a_n` (Remark 5.6) | **CURRENT** but see [F-EFF] below |
| C7 | `ζ_D(1)=Σ d_k/λ_k² = 2776.17` at fold; ratio to geometric `a_2^{SD}=0.728` is 3812 (pole at s=1, d=8) | Remark 5.6 | `a_2_FW_zeta = 2776.17` (S88); my-memory: "spectral a_2"=ζ_D(1)=2776.17 ≠ SD a_2=0.728 (factor 3812; pole s=1 d=8) | **CURRENT** (exact match incl. mechanism) |
| C8 | `⟨λ²⟩(τ)` strictly increasing: 2.495 (τ=0) → 3.471 (τ=0.5); 2.623 at fold | Thm 5.8(i) | Post-mortem §4(i) table identical; S102 `dM²/dτ>0` strict τ>0, =0 at τ=0, L-uniform CLOSED-FORM (SIGN-PROVEN); S103 landing §VII.BW | **CURRENT** |
| C9 | All 10 Peter–Weyl sectors (p+q≤3) individually monotone; no inter-sector cancellation | Thm 5.8(i) | Block-diagonality 8.4e-15 (S22b) + sector-by-sector (post-mortem §7.5) | **CURRENT** |
| C10 | `S_f(τ)` monotone **decreasing** for all **completely monotone** `f` (Bernstein) | Thm 5.8(ii) | See [S-CONV]; the *register's* canonical statement is "monotone, no well, all monotone `f`" — orientation depends on `f` | **CURRENT** (convention must be stated) |
| [S-CONV] | Sign of `dS_f/dτ` | Paper: `S_f` DECREASES (UV-suppressing `f`); cross-check reports "+60,267 (linear sum)" (L875) | `dS_fold=+58,672.8` (canonical, **linear/increasing-`f`**); post-mortem §4(ii)/(iii): decreasing-`f`→`S_f`↓, increasing-`f`→`S_f`↑ | **CURRENT** (paper internally coherent; rewrite must pin convention) |
| C11 | 9,600 monotonicity checks (10 cutoffs × 6 Λ × 16 τ × 10 sectors), all pass | Thm 5.8(iii) | E7 "9,600/9,600" (capstone L341; atlas-07; CUTOFF-SA-37) | **CURRENT** |
| C12 | **No minimum** of `S_f` on Jensen curve for any monotone `f` | Thm 5.8(iv), §6.1 | CUTOFF-SA-37 + **S95 W2-3 NO-WELL-ONE-LOOP PASS** (one-loop-robust) | **CURRENT** (and now strengthened, see §4) |
| C13 | Periodic-orbit corrections `≤ 7.9×10⁻³⁹` of leading SD term (Duistermaat–Guillemin); exact to ≥19 dp at τ=0.5 | Prop 5.9, Table 2, Fig 2 | No registry contradiction; geodesic-integrability (Berry–Tabor) PROVEN. Standalone spectral-geometry result. | **CURRENT** (no register conflict; novel-to-paper) |
| C14 | `L_min(τ)=4π√3·e⁻ᵗ` shortest closed geodesic | Prop 5.9 proof | Not separately registered; consistent with su(2) Cartan period + `L_2=e⁻²ᵗ`. Plausible; reviewer did not independently re-derive the `4π√3` prefactor. | **STILL-OPEN** (verify prefactor in rewrite) |
| C15 | SU(2)×SU(2) Berger: `d²S/ds²=−3.42`; SU(3) `d²S/dτ²=+20.42`; sign from complex reps | Prop 5.12 | atlas-07 **B5** "SU(3) Anomalously Curved vs SU(2)×SU(2) — opposite-sign spectral action curvature; root cause: complex representations" | **CURRENT** (registered structural result) |
| C16 | Connes 2019 open problem (metric deformations); paper gives "partial results, one family, one manifold" | Abstract, §6.3 | `Connes2019` = "NCG, the Spectral Standpoint" arXiv:1910.10407 — real. Scope-honest framing already applied (legacy memory). | **CURRENT** |
| C17 | All 22 transverse Hessian eigenvalues positive (min +1572); Jensen curve = transverse valley floor, longitudinal slope/saddle | §6.3, §6 Conclusion | Capstone L341 "HESS-40 found all 22 transverse Hessian eigenvalues positive; moduli constraint surface is zero-dimensional" | **CURRENT** (number "+1572" is paper's; register states "all 22 positive" without the min value — verify min in rewrite) |
| C18 | Moduli space dim: 28-dim (left-invariant) → 27 (volume-preserving) → 22 transverse | §6.3 | Capstone: U(2)-invariant metric space is 5D; full left-invariant is higher. "28→27→22" arithmetic is the full-left-invariant counting (35? — see note). | **DRIFTED** (dimension bookkeeping inconsistent — §3 [D-DIM]) |
| C19 | The fold is a van Hove singularity, A_2 catastrophe, structurally stable | §6.1 corollary, §6.3 | τ_fold=0.190 unique non-stationary van Hove cusp (S85 W10-3); A_2 catastrophe (post-mortem §1) | **CURRENT** |
| C20 | "The spectral action provides **no mechanism to stabilize** τ … moduli stabilization … what additional structure is required?" | §5.1, §6 Conclusion | **SUPERSEDED frame**: the canon is transit physics (post-mortem §10; capstone §5.1). Not "missing stabilizer" but "monotone ramp drives transit by design." | **SUPERSEDED** (primary casualty — §3 [FRAME]) |
| C21 | "spectral action prefers the round metric τ=0 over any deformed metric" | §5.1 | True as a statement about `S_f` (decreasing-`f`), but the *physical* reading "prefers / is trapped at" is container/equilibrium thinking. Substrate genesis IS at τ=0 (cold big bang, unstable extremum) and **transits away**. | **SUPERSEDED frame** (§3 [FRAME]) |
| C22 | Outlook: "functionals beyond the spectral action (Fock-space energy of fermionic many-body states) may be needed to capture the physics of the internal space" | §6 Conclusion | Post-mortem §5/§8: the right object is **transit dynamics** (Kibble–Zurek quench, GGE relic), not a different static functional. F.5 one-loop BdG shift is **wrong-sign anti-trapping** — a *different static functional won't help either*. | **SUPERSEDED** (§3 [FRAME], §4) |
| C23 | "Hessian … local minimum in transverse directions but a saddle point in the longitudinal (Jensen) direction" / "tilted valley with no minimum" | §6.3, §6 | Consistent with HESS-40 + monotonicity. The geometry is correct; only the *moduli-stabilization* gloss around it is stale. | **CURRENT** (geometry) / frame-adjacent |
| B1 | `Slebarski1985`: "The Dirac Operator on Homogeneous Spaces and Representations of Reductive Lie Groups", Proc. AMS, 1985 | references.bib | **WRONG**: real = "Dirac operators on a compact Lie group", Bull. London Math. Soc. **17** (1985) 579–583 (MR813743) | **DRIFTED** (cited L146/L505 — must fix, §5) |
| B2 | `ConnesInnerFluctuations` keyed/cited for "inner fluctuations … well understood" but titled "On the Spectral Characterization of Manifolds" | references.bib L221, cited L117 | Title is the *reconstruction* paper (MR3032810, real). The inner-fluctuations content needs Chamseddine–Connes–van Suijlekom 2013 (J. Geom. Phys. 73, 222) or Connes' original | **DRIFTED** (key/title/context mismatch — §5) |
| B3 | `GordonSchuethSutton`: 3 authors, Math. Ann. 353 (2012) 1383–1410 | references.bib (orphan) | **WRONG**: real = Gordon & **Sutton** (2 authors), Math. **Z.** 266 (2010) 979–995 (MR2729300). Schueth not an author of this paper. | **DRIFTED** (orphan — remove or fix, §5) |
| B4 | `GilkeySurvey2004`: Duke Math. J. 47, year 2004 | references.bib (orphan) | **WRONG YEAR**: Duke Math. J. 47 (**1980**) 511–528 (MR587163) | **DRIFTED** (orphan — remove or fix year, §5) |
| B5 | `Jensen1973`, `Fegan1987`, `Bar1992`, `Connes2019`, `Chamseddine1997`, `ChamseddineConnesMarcolli2007` | references.bib | All verified REAL and matching (MR353209, MR914927, MR1166019; arXiv:1910.10407; CMP 186:731; ATMP 11:991) | **CURRENT** |

---

## §2 What survives (the theorem core)

The following are PERMANENT in the register and require **no change** beyond convention-pinning and citation repair. They are the paper's spine and they hold:

1. **Geometric monotonicity (Prop 4.4 / Thm 5.1(i)–(iii))**. `R(τ)` increasing via the exact factorization `dR/dτ = x⁻²(x³−1)² ≥ 0` (x=e⁻ᵗ) is a clean analytic proof, registered as R-monotonicity (S64, AM-GM on volume-preserving Jensen). `a_0` constant, `a_2 ∝ R` increasing. **[C1–C5]**

2. **Structural monotonicity of `⟨λ²⟩(τ)` (Thm 5.8(i))**. Strictly increasing 2.495→3.471, sector-by-sector across all 10 p+q≤3 sectors, no inter-sector cancellation (block-diagonality 8.4e-15). This is now *strengthened* to a closed-form sign proof: **S102 TRD2-MONOTONICITY-ANALYTIC** proves `dM²/dτ>0` strict for τ>0, =0 at τ=0, **L-uniform** (Weitzenböck–Lichnerowicz, symbolic Sage-QQ) — i.e. the paper's 16-point numerical monotonicity is now a *theorem at all L*. **[C8, C9]**

3. **Completely-monotone-`f` extension via Bernstein (Thm 5.8(ii))**. The Laplace-transform argument — `f` completely monotone ⇒ `f(x)=∫e⁻ˢˣdμ(s)`, μ≥0 ⇒ `S_f` inherits the sign of the heat trace — is correct and is the mathematically respectable core of the "all monotone `f`" register claim. The paper's restriction to *completely* monotone (vs all monotone) is **more honest than the register's loose "all monotone `f`" phrasing** and should be kept (it is the legacy peer-review fix; 23.4% of bare eigenvalues decrease individually, so the naïve "all monotone" proof was a gap). **[C10, Remark 5.7]**

4. **No interior minimum (Thm 5.8(iv))**. Now *one-loop-robust*: **S95 W2-3 NO-WELL-ONE-LOOP PASS** (200-point grid, three routes) confirms `dΓ/dτ` keeps a fixed sign with zero interior sign-changes when the `½Tr ln(D²/Λ²)` loop is added. The paper proved it at tree level; the register has since closed the one-loop question in the paper's favor. **[C12]**

5. **SU(3) specificity vs SU(2)×SU(2) (Prop 5.12)**. Registered as atlas-07 **B5** (opposite-sign spectral action curvature; complex-representation root cause). The paper's `+20.42` vs `−3.42` and the three-part structural explanation (complex reps / product factorization / fold curvature) are sound. **[C15]**

6. **Periodic-orbit suppression (Prop 5.9)**. The Duistermaat–Guillemin bound `≤10⁻³⁹` is a genuine standalone spectral-geometry contribution with no register conflict; it certifies the heat-kernel (Seeley–DeWitt) expansion as effectively exact on the Jensen curve. Consistent with the framework's geodesic-integrability (Berry–Tabor) result. **[C13]** (Verify the `4π√3` prefactor and the `L_min²Λ²/4` Gaussian-FT exponent algebra in rewrite — C14.)

7. **Seeley–DeWitt hierarchy + `a_4(K)=0` at the Einstein point**. The hierarchy and the vanishing of the gauge-kinetic coefficient at τ=0 (gauge kinetics *emerge* from the deformation) are permanent results (post-mortem §7.1–7.2, S33a). The paper carries the hierarchy implicitly (gradient decomposition §5.2); the rewrite could add `a_4(K)=0` explicitly as it is a clean, citable result.

**Net**: the abstract's four enumerated results (geometric `a_2` increasing; `⟨λ²⟩` increasing + sector-wise; effective `â_2k` monotone; completely-monotone-`f` `S_f` monotone; periodic-orbit `10⁻³⁹`; SU(3)/SU(2)² sign contrast; no minimum) are **all CURRENT**. The theorem does not move.

---

## §3 What must change

### [FRAME] (HIGHEST PRIORITY) — τ-selection / moduli-stabilization framing is SUPERSEDED

The paper repeatedly frames the no-minimum result as a *deficiency* of the spectral action as a **moduli-stabilization** mechanism and asks what *additional structure* could stabilize τ. The current canon inverts this: the monotone ramp is **the transit engine**, and the absence of a well is the *point*, not a gap. Every such passage must be reframed substrate-first.

Offending passages and required reframes (substrate-first, per `phononic-framing.md`):

- **Abstract L79–80**: "establish that no minimum of the spectral action exists along the Jensen curve." → Keep the *fact*, but the surrounding "partial progress toward [stabilization]" gloss must not imply stabilization was the goal. Reframe: the monotonicity is *why the substrate transits* — a monotone `e^{−S(τ)}` weight has no interior saddle, so the partition function is genesis-boundary-dominated.

- **§5.1 (L994–999)**: "the spectral action provides no mechanism to stabilize the deformation parameter τ at a finite positive value." → This is container/equilibrium thinking ("a mechanism to stabilize a modulus inside a moduli space"). Substrate-first: *τ is the substrate's intrinsic deformation parameter; the monotone spectral-action gradient drives it through the fold — transit, not trapping.* Cite post-mortem §10 and capstone §1.3a/§5.1.

- **§5.1 L989–992**: "spectral action prefers the round metric τ=0." → Genesis IS at τ=0 (the cold big bang, an *unstable* extremum); the substrate does not "prefer" to sit there — it is the starting configuration from which the monotone gradient drives the transit. Replace "prefers" with the unstable-extremum/transit language.

- **§5.1 Corollary (L1001–1007)**: "the spectral fold … is invisible to any completely monotone spectral action functional … No such functional can detect or stabilize the fold." → The *fact* is CURRENT (post-mortem §6, §10: the fold is invisible to integrated spectral moments). But "stabilize the fold" presumes the stabilization frame. Reframe: the fold is a *van Hove feature in the DOS* — a measure-zero, IR feature — invisible to UV-dominated integrated moments; *the fold's physics is dynamical (BCS/Kibble–Zurek during transit), not a stationary point of `S_f`.* This is the post-mortem's central lesson ("the dot and the ink were never separate", §Addendum).

- **§6 Conclusion (L1192–1199)**: "if the spectral action alone cannot stabilize the internal geometry, what additional structure is required? … functionals beyond the spectral action (Fock-space energy …) may be needed." → **SUPERSEDED and partly wrong.** (a) The framing presumes stabilization is owed. (b) The specific suggestion (a different *static* functional, e.g. Fock-space energy) is *closed*: post-mortem F.5 shows the one-loop BdG shift is **wrong-sign anti-trapping** (`δS_BdG=+12.76`, penalizes pairing), so a Fock-space static functional does not produce a well either. Replace the entire outlook with the **transit-dynamics** picture: the relevant question is the *Kibble–Zurek defect density / GGE relic produced during transit through the fold* (post-mortem §10, §8), not which static functional has a minimum.

**Reframe principle (mandatory)**: every reframed passage keeps the substrate logically prior — `D_K eigenvalues → spectral moments → emergent physics`. Do **not** explain the substrate result by appealing to "moduli stabilization in KK compactification" as if the moduli space were a pre-existing container the substrate lives in (`phononic-framing.md §"IS Space, Not IN Space"`, Level-2 moduli-deformation substrate-IS). The moduli-space of Jensen deformations **IS** a substrate-IS object (the substrate's own deformation parameter), not a meta-container.

### [S-CONV] — pin the `dS/dτ` sign convention explicitly

The paper says `S_f` is monotone **decreasing** (for UV-suppressing `f`); the register's headline number is `dS_fold = +58,672.8 > 0` (the **linear sum / increasing-`f`** reading, `f(x)=x` so `S=Σ|λ|`). Both are correct and the paper's own cross-check (L875: "+60,267 (linear sum)") shows it knows this. But an external mathematical-physics reader will collide "Thm 5.8(ii): `S_f` decreasing" against any framework citation of "`dS/dτ>0`". **Add one sentence** (in Thm 5.8 or §5.2) stating the orientation rule explicitly: *for monotonically decreasing (UV-suppressing) `f`, `S_f` decreases; for monotonically increasing `f` (e.g. the linear sum `Σ|λ|` or `x^α`), `S_f` increases; in both cases `S_f` is strictly monotone with no interior extremum.* This is post-mortem §4(ii)/(iii) verbatim and removes the only genuine reader-confusion hazard. The capstone E7 statement (`dS/dτ>0`) and the paper (`S_f↓`) are the same theorem read with opposite `f`-orientation.

### [F-EFF] — Figure 1 / Table 1 caption: effective vs geometric `a_4`

`fig_sd_coefficients.pdf` and Table 1 show the **effective** `â_2k` from the truncated (p+q≤3) spectral sum: `â_4 < 0` (−330 → −303, increasing toward zero). A reader may collide this against the canonical **geometric** `a_4_FW_zeta = +1350.72 > 0` (S75; a_4 > 0 established S73A W2-D) and conclude an error. There is none — these are different objects (effective spectral-sum fit vs full-L Gilkey curvature-polynomial moment), and Remark 5.6 correctly distinguishes them for `a_2`. **Required**: extend the same explicit disclaimer to `a_4`/`a_6` in the Figure 1 caption and Table 1 caption: *these are effective coefficients from the p+q≤3 truncated spectral sum, NOT the geometric Gilkey Seeley–DeWitt moments; the sign of `â_4` (negative) does not contradict the positive geometric `a_4`.* Without this, the figure is a cross-citation trap. (Per `regulator-pin-discipline.md`, the geometric `a_n` must also carry a regulator tag — see §6 [BIB/NOTATION].)

### [D-DIM] — moduli-space dimension bookkeeping (C18)

§6.3 states "28-dimensional moduli space of left-invariant metrics → 27 (volume-preserving) → 22 transverse." The number of left-invariant metrics on a Lie group of dim 8 is the space of positive-definite symmetric bilinear forms = `8·9/2 = 36`, modulo nothing (or modulo isometry). "28" is not obviously this count, and "22 transverse" needs the 1 (Jensen longitudinal) + the isotropy-fixed directions accounted. The capstone treats the U(2)-invariant subspace as 5D. **The paper's dimension arithmetic (28→27→22) is internally unexplained and likely wrong.** Either (a) derive it explicitly (state which group action is quotiented), or (b) restrict the claim to the count that HESS-40 actually computed (the register says "all 22 transverse Hessian eigenvalues positive" — so 22 is the HESS-40 number; the "28→27" preamble should be reconciled or dropped). Flag for the rewrite author to pin against HESS-40's actual setup.

### [SCOPE] — Connes open-problem phrasing already conservative; keep it

The legacy peer-review fix already weakened "address the open problem" → "provide partial results toward the open problem, for one specific deformation family on one manifold." This is CURRENT and appropriately humble. **No change** beyond ensuring the §6.3 and Abstract phrasings remain matched. (Mathematical-physics referees will appreciate the restraint; do not let a rewrite re-inflate it.)

---

## §4 New results since the paper's era that belong in it

These are register results *after* the paper's S50–53 era (or contemporaneous but not cited) that materially strengthen or correctly reframe the paper. A rewrite should fold them in.

1. **The S77 re-derivation lineage → cite the post-mortem.** The bare spectral action monotonicity was *proven S37* (CUTOFF-SA-37) and **independently re-derived S77** (the canonical example of the "query-first" lesson; `sessions/framework/registry/spectral-post-mortem.md`, ARCHIVED but content-permanent per atlas-09 Item 45). For a *publication*, the relevant move is not to cite internal session IDs but to note that the monotonicity has been verified by multiple independent computations and is now a **closed-form sign theorem** (S102, item 2 below). The post-mortem is the lineage-of-record; the paper's "20 sessions" framing (if any survives) should be replaced by the clean theorem statement.

2. **S102 closed-form sign proof (strengthens Thm 5.8(i)).** `TRD2-MONOTONICITY-ANALYTIC`: `dM²/dτ > 0` strict for τ>0, `=0` at τ=0, **L-uniform** (Weitzenböck–Lichnerowicz, symbolic Sage-QQ, machine-eps). This upgrades the paper's 16-point numerical `⟨λ²⟩` monotonicity to an *analytic theorem valid at all truncation levels L* — directly answering Remark 4.7's worry ("it remains logically possible that some higher sector could exhibit a different pattern"). **This should replace or supplement Remark 4.7**: the L-uniform closed-form proof closes the "higher sectors might differ" loophole for `⟨λ²⟩`. (The completely-monotone-`f` `S_f` extension still rests on the heat-trace-dominance argument, which is honest to keep.)

3. **S95 one-loop closures as honest scope statements.** Two S95 PASSes belong in the Consequences section as the *correct* modern framing:
   - **NO-WELL-ONE-LOOP (S95 W2-3, PASS)**: no interior well survives adding the one-loop `½Tr ln(D²/Λ²)` term (200-point grid, 3 routes). → strengthens C12 from tree-level to one-loop-robust.
   - **T-STAR-ONELOOP-ORIGIN (S95 W2-1, FAIL)**: the corridor "the one-loop threshold coefficient *is* the empirical admixture `t*`" is CLOSED — `Γ_1loop ≈ 26%` is ~3× too large to be `t*=0.0883`. → This is the register's statement that **the spectral-action landscape does NOT select τ**; the route is now MECHANISM-CHAIN dynamical relaxation or τ_fold is empirical. *The paper's outlook must be rewritten to reflect that one-loop spectral-action τ-selection is a closed corridor, not an open hope.*

4. **Sign-wall role for `α_s` (the load-bearing downstream cross-link).** The monotonicity SIGN-WALLS the substrate-distance-1 strong-coupling running: `alpha_s_substrate_distance_1 = −0.08587279` (S92, NOT superseded). The mechanism: `dR/dτ>0` ⇒ `a_2′(τ)>0` is the *R-monotone obstruction sign* (S64 W1-A) that fixes the sign of downstream observables. A mathematical-physics paper need not carry the cosmology, but **a one-paragraph "Downstream consequence" remark** noting that the monotonicity sign is not idle — it propagates to a definite-sign prediction for an emergent running coupling — would (a) motivate why the *sign* (not just monotonicity) matters, and (b) connect to the framework's predictive surface without over-claiming. Optional but valuable; mark PRELIMINARY if included.

5. **Instanton-gas / transit paradigm (replaces the stabilization outlook).** The post-mortem §10 + capstone §5 give the canonical replacement for the paper's "what stabilizes τ" outlook: the substrate transits the fold diabatically (Mach 13.75), BCS condensation and Kibble–Zurek defect formation happen *during* transit, the GGE relic forms (`⟨Q⟩_GGE=59.8`, `P_exc=1`, the Ordered Veil = transit-timescale diabatic freeze-out, `S_ent=0`, S95 W5). The paper's Conclusion should point here rather than to "a different static functional." (Keep the depth appropriate to a spectral-geometry venue — one paragraph, cited — not a cosmology excursion.)

6. **`a_2^{SD}(fold) = 0.728235` exact anchor.** The geometric Gilkey `a_2` at the fold is a clean exact number (my-memory / Gilkey closed form) the paper can cite as the geometric counterpart to its `ζ_D(1)=2776.17` (Remark 5.6 already does this with `0.728` — confirm it carries the regulator tag, §6).

---

## §5 Bibliography audit

**Verified REAL and matching (no change):**
- `Jensen1973` — MR353209, exact match (J. Diff. Geom. 8 (1973) 599–614). ✓
- `Fegan1987` — MR914927 (Simon Stevin 61 (1987) 97–108). ✓ (author "Howard Fegan"; the "D." middle initial in the bib is harmless.)
- `Bar1992` — MR1166019 (Arch. Math. 59 (1992) 65–79), exact. ✓ (legacy Bar1996→Bar1992 fix confirmed applied.)
- `Connes2019` — arXiv:1910.10407 "NCG, the Spectral Standpoint", real. ✓ (note: "New Spaces in Mathematics" is the volume; fine.)
- `Chamseddine1997` — CMP 186 (1997) 731–750, real. ✓
- `ChamseddineConnesMarcolli2007` — ATMP 11 (2007) 991–1089, real. ✓
- `Gilkey1995`, `Vassilevich2003`, `BerlineGetzlerVergne2004`, `Connes1994`, `LawsonMichelsohn1989`, `Lichnerowicz1963`, `DuistermaatGuillemin1975`, `Arnold1966`, `vanSuijlekom2015`, `Witten1981`, `DuffNilssonPope`, `Ivrii2016`, `Baptista2024` — standard, no red flags. (`Baptista2024` = arXiv:2306.01049 "Kaluza–Klein Spectrometry from Exceptional Deformations" — the project's KK source; verify the arXiv number resolves to the intended Baptista paper, as the project corpus uses Baptista #13–#18.)

**ERRORS requiring fix (CITED entries — these render):**

- **`Slebarski1985` [B1] — WRONG title + journal + pages.** Bib has "The Dirac Operator on Homogeneous Spaces and Representations of Reductive Lie Groups, Proc. AMS, 1985." The real Slebarski 1985 is **"Dirac operators on a compact Lie group", Bull. London Math. Soc. 17 (1985) 579–583** (MR813743, MRreviewer H. D. Fegan). Cited at L146 and L505 (block-diagonality / homogeneous-space Dirac). Replace the entry with the MR813743 BibTeX. *(There exist later Slebarski papers on reductive groups — J. Reine Angew. Math. — but the cited Proc. AMS combination does not match any single record; the block-diagonality citation is correctly served by the Bull. LMS paper.)*

- **`ConnesInnerFluctuations` [B2] — key/title/context mismatch.** Entry title is "On the Spectral Characterization of Manifolds" (= the reconstruction theorem, MR3032810, J. Noncommut. Geom. 7 (2013) 1–82, real) but the key and the L117 citation context are "inner fluctuations of the Dirac operator … well understood." Two clean fixes: (a) if the intended reference is inner fluctuations, replace with **Chamseddine–Connes–van Suijlekom, "Inner fluctuations in NCG without the first-order condition", J. Geom. Phys. 73 (2013) 222–234** (or Connes' "Gravity coupled with matter…", CMP 182 (1996) 155); (b) if the L117 sentence actually wants the reconstruction theorem, rename the key to `ConnesReconstruction2013` and keep MR3032810. Recommend (a) — the sentence is explicitly about inner fluctuations.

**ERRORS in ORPHAN entries (defined, never `\cite`d — harmless to render but submission-hygiene):**

- **`GordonSchuethSutton` [B3]** — WRONG: real is Gordon & Sutton (2 authors), Math. Z. 266 (2010) 979–995 (MR2729300); Schueth is not an author, journal/volume/year/pages all wrong. **Remove** (orphan) or fix + cite (it is relevant to the spectral-rigidity context — a `\cite` in §2 background on isospectrality would be apt, and would also let the paper note that the Jensen *deformation* explicitly breaks naturally-reductive isospectral-isolation, a nice contextual point).
- **`GilkeySurvey2004` [B4]** — WRONG YEAR: Duke Math. J. 47 is **1980** not 2004 (MR587163). **Remove** (orphan) or fix year if used.
- **`BoldtLauret2018`** — orphan; arXiv:1811.09637 is real (inverse Dirac spectral problem, 3-dim Lie groups) but MRef did not resolve a journal version cleanly. **Remove** (orphan) or verify the published venue (Ann. Global Anal. Geom.) before citing.

**Hygiene summary**: 2 cited-entry fixes (Slebarski, ConnesInnerFluctuations) are MANDATORY (they render incorrectly). 3 orphan fixes are submission-cleanliness (remove or repair). No fully-hallucinated authors of *cited* works were found — the errors are wrong-metadata on real papers, consistent with legacy-model authorship that grabbed approximately-right citations. The math-content citations (Gilkey, Vassilevich, Bär, Fegan, Jensen, Chamseddine–Connes) are sound.

---

## §6 Rewrite plan (section-by-section, mechanically executable)

**Verdict-bearing principle**: this is a REWRITE-IN-PLACE (see §7), not a restructure. The skeleton, theorem statements, proofs, figures, and ~85% of prose are kept. Edits are surgical: reframe §5–§6, pin one convention sentence, repair 2+3 bib entries, add 3 caption disclaimers, fold in 3 register strengthenings.

### Abstract (L42–81)
- KEEP all four enumerated results and the numbers (CURRENT per §1).
- L79–80: keep "no minimum … exists along the Jensen curve" but adjust the surrounding clause so it does not imply moduli-stabilization was the objective. Add a half-sentence: *"the monotonicity is the structural reason the deformation parameter flows rather than settling"* (substrate-first, transit framing).
- No re-inflation of the Connes-open-problem scope (keep "partial results, one family, one manifold").

### §1 Introduction (L84–204)
- KEEP §1 essentially verbatim — the spectral-action background, Connes-2019 open-problem motivation, Jensen-deformation setup, Peter–Weyl block-diagonality, and Contributions list are all CURRENT.
- L107–119: the moduli-stabilization motivation ("if the geometry of K is to be determined dynamically — as a modulus stabilized at a minimum of `S_f`") is the *honest historical motivation* and may stay AS MOTIVATION, but add a forward-pointer sentence: *"As we show, no such minimum exists; §5 discusses why this is structurally expected and what it implies (a flowing, not stabilized, modulus)."* This sets up the reframed §5 without rewriting §1's logic.
- L117: fix `\cite{ConnesInnerFluctuations}` per §5 [B2].
- L146, L505: fix `Slebarski1985` per §5 [B1].

### §2 Preliminaries (L207–317)
- KEEP. The Lichnerowicz bound check (L314–317: `λ₁²=0.672 ≥ R/4 = 0.504`, ratio 1.33) is CURRENT and a nice rigor anchor. *(Cross-check against the framework's tighter Friedrich–Kirchberg bound `5R/16=0.631` if a sharper statement is wanted — actual `λ₁²=0.672`, tightness 1.065; optional.)*
- L255–283 (the `a_0`/`a_2`/`a_4` Gilkey formulas + spinor-rank footnote): KEEP; the convention footnote is careful and correct. **Add regulator tag**: per `regulator-pin-discipline.md`, the geometric `a_n` used downstream should be tagged (these are the Gilkey/heat-kernel — i.e. `ζ`-scheme-compatible — coefficients). For an external venue the superscript may be relegated to a footnote, but the internal-consistency requirement is: every numerical `a_n` the paper reports (0.728 geometric; 2776.17 spectral-sum; the effective `â`s) must be unambiguously labelled which object/scheme it is. Add a one-line "Conventions" note.

### §3 Jensen Deformation (L321–529)
- KEEP entirely. Curvature invariants (L404–423), Dirac operator construction, Peter–Weyl decomposition, block-diagonality lemma all CURRENT.
- **Remark 4.7 (L519–529)**: AUGMENT with the S102 closed-form result (§4 item 2). Replace "this has not been proven in general: it remains logically possible that some higher sector could exhibit a qualitatively different monotonicity pattern" with the stronger true statement: the `⟨λ²⟩` monotonicity is now proven **L-uniformly in closed form** (Weitzenböck–Lichnerowicz), so the higher-sector loophole is closed *for `⟨λ²⟩`*; the residual open item is only the general (non-completely-monotone) `f` case (Remark 5.7). This is a strict strengthening and removes a self-identified weakness.

### §4 (paper's §"Monotonicity of Seeley–DeWitt Coefficients", L533–711)
- KEEP. Prop 4.4 (R-monotone) proof is clean. Thm 5.1 holds.
- **Table 1 + Fig 1 caption (L683–704)**: add the effective-vs-geometric `a_4` disclaimer per §3 [F-EFF]. One sentence in each caption.
- Remark 5.6 (L636–651): KEEP — it already correctly distinguishes geometric `a_2`=0.728 from spectral-sum `ζ_D(1)`=2776.17 (factor 3812, pole at s=1). Confirm the regulator/object tags are explicit.

### §5 Structural Monotonicity Theorem (L715–975)
- KEEP Thm 5.8, all proofs, the 9,600-check verification, the periodic-orbit Prop 5.9.
- **Add the [S-CONV] convention sentence** (§3 [S-CONV]) immediately after Thm 5.8(ii) or in §5.2: state the decreasing-`f`→`S_f`↓ / increasing-`f`→`S_f`↑ orientation rule explicitly, with the `+58,673` linear-sum value named as the increasing-`f` representative.
- Remark 5.7 (general-monotone conjecture, L772–783): KEEP — it is honest and correct (23.4% bare eigenvalues decrease). This is the register's *only* genuinely open sub-item for this theorem.
- Prop 5.9 / C14: verify the `L_min=4π√3 e⁻ᵗ` prefactor and the Gaussian-FT exponent `e^{−L²Λ²/4}` algebra (the proof at L928–944 asserts `ĥ(ξ)=e^{−ξ²/4}` and `e^{−18.73²/4}=e^{−87.7}` — check `18.73²/4 = 87.7` ✓; check the `4π√3` against the su(2) Cartan period independently).

### §6 Consequences (L979–1153) — PRIMARY REWRITE TARGET
- **§5.1 (L982–1019)**: reframe per §3 [FRAME]. Keep the *mathematical facts* (no minimum; fold invisible to integrated moments). Replace the moduli-stabilization gloss with the transit reading. Specifically:
  - L989–992 "prefers the round metric": → unstable-extremum/genesis + transit language.
  - L994–999 "provides no mechanism to stabilize": → "the monotone gradient drives the modulus through the fold (transit), consistent with a genesis-boundary-dominated `Z=Σe^{−S}`."
  - Corollary L1001–1007: keep "fold invisible to integrated spectral moments"; reframe "stabilize the fold" → "the fold's physics is dynamical (occurs during transit), not a stationary point of `S_f`."
- **§5.2 Gradient decomposition (L1022–1051)**: KEEP — the hierarchy `|da_6/dτ|≫|da_4/dτ|≫|da_2/dτ|≫|da_0/dτ|` and the `a_6`-domination at the fold are correct and useful. (These use the *effective* `â` gradients from Table 1; ensure the object-label is consistent with §3 [F-EFF].)
- **§5.3 Connes' open problem (L1053–1082)**: KEEP the scope-honest framing. The transverse-Hessian sentence (L1077–1082, "all 22 transverse directions positive, min +1572") is CURRENT (HESS-40) — verify the "+1572" min against HESS-40's actual output, and reconcile the "27-dimensional" preamble with §3 [D-DIM]. Add the S95 one-loop-robustness note (§4 item 3).
- **§5.4 SU(2)×SU(2) comparison (L1085–1153)**: KEEP — registered as atlas-07 B5.

### §6 Conclusion (L1157–1199)
- KEEP the first two paragraphs (theorem summary; SU(3) specificity).
- **Rewrite the outlook (L1182–1199)** per §3 [FRAME] + §4 item 5:
  - Keep "extension to the full moduli space" and "other Lie groups (Sp(2), G_2)" — these are legitimate open spectral-geometry directions.
  - **Delete/replace** "if the spectral action alone cannot stabilize the internal geometry, what additional structure is required? … functionals beyond the spectral action (Fock-space energy …)." Reason: (a) presumes the stabilization frame; (b) the Fock-space-functional suggestion is *closed wrong-sign* (post-mortem F.5, δS_BdG=+12.76 anti-trapping). Replace with: the monotonicity is the **transit engine** — the physically relevant question is the dynamics *during* transit (Kibble–Zurek quench through the van Hove fold, GGE relic formation), a *dynamical* question, not a search for a static functional with a minimum. One paragraph, cited to the transit-dynamics result; keep venue-appropriate brevity.
- Optionally add the §4 item 4 "Downstream consequence" remark (sign-wall for an emergent running coupling), marked PRELIMINARY.

### Appendix (L1203–1298)
- KEEP. Validation cross-checks (bi-invariant `λ²=n/36`; spectral symmetry 5.5e-15; `[J,D_K]=0` 3.3e-13; Riemann 147/147; block-diagonal 8.4e-15) are all CURRENT and are the paper's rigor backbone. The `λ²=n/36` τ=0 anchor is a genuine canonical anchor (confirmed). Software/data-availability section is fine.

### references.bib
- Fix `Slebarski1985` (→ MR813743 BibTeX, Bull. LMS 17 (1985) 579–583).
- Fix `ConnesInnerFluctuations` (→ inner-fluctuations paper, or rename key to reconstruction).
- Remove or repair the 3 orphans (`GordonSchuethSutton`→MR2729300; `GilkeySurvey2004`→year 1980; `BoldtLauret2018`→verify venue). Recommendation: cite `GordonSchuethSutton` (corrected) in §2 as spectral-rigidity context; remove the other two orphans.

---

## §7 Verdict

**REWRITE-IN-PLACE.**

The theorem is PERMANENT and the paper's mathematical spine — geometric `a_2` monotonicity (analytic), `⟨λ²⟩` structural monotonicity (now closed-form L-uniform), the Bernstein completely-monotone-`f` extension, the no-minimum result (now one-loop-robust), SU(3)/SU(2)² specificity, and the `10⁻³⁹` periodic-orbit bound — is entirely CURRENT and in several places has been *strengthened* by post-paper register results (S102 closed-form sign proof; S95 NO-WELL-ONE-LOOP). Nothing in the core requires retraction or restructuring. The damage is confined to (i) the §5–§6 *moduli-stabilization* framing, which the S37 paradigm shift and the spectral post-mortem §10 superseded with the transit-physics reading (the monotone ramp is the transit *engine*, not a failed stabilizer), (ii) a single unstated `dS/dτ` sign-convention that must be pinned so the paper's "`S_f` decreasing" does not collide with the framework's "`dS/dτ>0`", (iii) two cited bibliography entries with wrong metadata on real papers (Slebarski, inner-fluctuations) plus three orphan entries, and (iv) a figure-caption trap (effective vs geometric `a_4` sign) and a moduli-dimension bookkeeping slip. All four are surgical edits against a sound skeleton. A focused pass — reframe §5–§6 substrate-first, add one convention sentence, repair five bib entries, add three caption disclaimers, and fold in the three register strengthenings — yields a publication-ready spectral-geometry paper whose results are fully reconciled with the post-S103 register. RESTRUCTURE is unwarranted (the architecture is fine); RETIRE-AND-REPLACE is wrong (the theorem is one of the framework's permanent results).
