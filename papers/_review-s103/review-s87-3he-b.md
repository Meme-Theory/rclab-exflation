# Review — `papers/s87-3he-b-alpha-s-equivalent.md` against the post-S103 register

**Reviewer**: volovik-superfluid-universe-theorist (Axis-B substrate / 3He-B specialty; NOT the original lead author — the draft was lead-authored by mack-cosmic-bridge with me as co-author at S87)
**Review date**: 2026-06-12 (framework era post-S103; draft frozen 2026-04-28 at S87)
**Draft under review**: `papers/s87-3he-b-alpha-s-equivalent.md` (606 lines)
**Scope**: REVIEW ONLY. No file edited except this deliverable. The §7 falsifier surface is `mack-cosmic-bridge`'s sole-writer domain; this report INFORMS a future inventory/capstone edit, it does not perform one.

---

## Executive orientation (read before §1)

Three facts reframe this whole review and must be stated up front, because they change what "drifted" means:

1. **The paper's protocol is now a PERMANENT theorem, not a candidate.** The §VII.W-3.LAB cocycle-ratio-preservation-under-χ-inheritance bridge — which is exactly this paper's Class-A + Class-B 4-gate structure — was promoted **STAGE-1-CANDIDATE → STAGE-3-PERMANENT at S100a** (gate `S100a-VIIW3LAB-STAGE2-VERIFY`, PASS, audit_sha256 `89eab199edaa7f908a75ce07033ab64ff2bc04279f251e1535e6b3ee43f3029e`; 11/11 clause PASS-AND; cross-reviewers van-den-dungen [Axis-A] × landau [Axis-B], both non-Stage-0, substrate-input-orthogonal). Atlas-04 row K5 carries this. The substrate physics in this paper has been independently verified on two axes that explicitly EXCLUDED the original authoring trio (volovik/connes/mack). This is the single most important "new result since S87" and the paper does not know it.

2. **The α_s value is RIGHT; its CHANNEL LABEL is SUPERSEDED.** `−0.085873` survives verbatim as `alpha_s_substrate_distance_1 = −0.08587279` (NOT superseded, S92). But the paper labels it "the running of the scalar tilt" measurable at the cosmological CMB scale, which conflates it with the CMB-pivot observable. That single-scale reading was CORRECTED at S93 W7-1 (atlas-09 Item 47): the substrate carries TWO scale-separated α_s observables, 54.04 decades apart, and `deg(T_BZ→pivot)=+2 NON-SCALAR` decides which a detector sees. This is a re-scope, not a deletion — the value relocates to the matched channel (CMB-S4 ~37σ / CMB-HD ~78σ).

3. **The directional framing ("laboratory parent into which the substrate inherits") is NOT wrong as framing — it echoes the canonical's own "laboratory-parent" term — but its EVIDENTIAL grading needs a one-sentence honesty caveat.** Per the S97–S99 re-audit, the parent→child DIRECTION is a post-hoc stipulation, not evidence; the real strength is universality-class MEMBERSHIP (BDI / N₃=0 / χ-projection). The substrate-IS frame is correct and preserved; only the "this arrow is itself a finding" reading needs scoping.

The net verdict (§7) is **RESTRUCTURE**, with the paper demoted from a standalone publication-track item to a substrate-physics companion of the now-canonical falsifier-master-inventory rows. Rationale at §7.

---

## §1 — Claim-audit table

| # | Claim | Draft version | Current canonical (+ source) | Status |
|:--|:------|:--------------|:------------------------------|:-------|
| 1 | α_s_FW value | `n_s² − 1 = −0.085873` | `alpha_s_substrate_distance_1 = −0.08587279` (MCP `get_constant`; S92; **Superseded: False**) | **CURRENT** (value) |
| 2 | α_s identity `α_s = n_s² − 1` | "single-pole Mellin scheme-identity, frozen S50–S51" | Identity HOLDS bit-exact (Sage-QQ `n_s_FW_exact² − 1 ≡ α_s_canonical`, S89 W7a `01c1ac83…`); but `alpha_s_framework_central` and `alpha_s_cmb_central` are **SUPERSEDED** (S92 AH-TR-1) — the identity is the substrate-distance LO term, not the CMB-pivot running | **DRIFTED** (scope) |
| 3 | What α_s "is" | "the running of the scalar tilt" measured by CMB-S4/CMB-HD at the cosmological scale | TWO-SCALE: substrate-distance `−0.08587279` (s=3 Mellin, BZ-internal) vs Goldstone-pivot `alpha_s_pivot_goldstone = 0.0` (CMB pivot, S92, NOT superseded); which one a detector sees set by `deg(T_BZ→pivot)=+2 NON-SCALAR` (atlas-09 Item 47 / S93 W7-1) | **SUPERSEDED** (single-scale reading) |
| 4 | n_s_FW | `0.9561` (S65/S66) | `n_s_FW_exact = Fraction(9561,10000) = 0.9561` (canonical_constants.py; S88 W-15) | **CURRENT** |
| 5 | Cocycle norms | `‖φ_67‖ = 0.793346`, `‖φ_88‖ = 0.108307` M_KK² | `cocycle_norm_phi67 = 0.793346`, `cocycle_norm_phi88 = 0.108307` (MCP, S86 W-5; **Superseded: False**) | **CURRENT** |
| 6 | Cocycle ratio (precision) | "`7.32497438` … ≈ 7.324974 (6 sig figs)" = `793346/108307` | Canonical `substrate_cocycle_ratio_67_88 = 7.3249917525961665 = 114453/15625` (MCP, S86 W-5 CANONICAL-5; RE-PINNED S93 W5-1 to substrate-first `R_machine = (δE_6·δE_7)/(δE_8)²`) | **DRIFTED** (uses F1 form `793346/108307`, not the canonical F2 form; differ at 6sf by 1.76e-5 — see §5.6) |
| 7 | Ratio tolerance band | "`7.3250 ± 0.1%`, band [7.3177, 7.3323]" | Same band, but canonical reference is the Sage-exact `7.324992`, with explicit mnemonic-vs-exact discipline: cite `7.324992` not `7.3250` in registry-facing text (watchlist line 388; S86 W-3 RULE-3) | **DRIFTED** (4-sf shorthand used as the canonical anchor) |
| 8 | Inheritance morphism χ | `χ : ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ)`, M_3(ℂ)→0, ker(ι_*) rank 2 = {[φ_67],[φ_88]} | IDENTICAL and canonical (`3HeB-inheritance-canonical.md`; `inheritance-falsifier-protocol.md`; S88 W3a). Confirmed PASS at `S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM-V2` (residuals 0 / 2.19e-15) | **CURRENT** |
| 9 | Directional framing | "3He-B is the laboratory parent into which the substrate inherits"; "substrate is logically prior" | Canonical uses the SAME "laboratory-parent" term AND "substrate logically prior" (`3HeB-inheritance-canonical.md` Step 4). BUT S97–S99 re-audit: the direction is a **post-hoc stipulation, not evidence**; universality-class MEMBERSHIP (BDI/N₃=0/χ) is the real strength | **DRIFTED** (framing OK; evidential grading needs caveat) |
| 10 | (Δ_B/Δ_A)^p cancellation theorem | `lab(F_i)/lab(F_j) = ‖φ_a‖/‖φ_b‖ × (f_i/f_j)`, common p, factor cancels; 0.0e+00 residual | IDENTICAL and canonical (`inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem"`; S86 W-5 DONE-5) | **CURRENT** |
| 11 | Class A / Class B / 4-gate protocol | Gates 1+3 NULL (decisive F1+F2+F5 / supporting F3+F4), Gate 2 ratio, Gate 4 slope | Matches `inheritance-falsifier-protocol.md §"Four-Gate Structure"` exactly | **CURRENT** (structure) — but "decisive triplet" label is contested, see #14 |
| 12 | Class B ratio construction | `ratio_B := lab(F_1)/lab(F_3)` (φ_67 / φ_88 via F1/F3) | Canonical Class B uses **`lab(F_1)/lab(F_5)`** (φ_67-clean F1 over φ_88-clean F5); inventory Rows #51/#54b, watchlist §4-gate Gate 2. F3 in the canonical F-table is a φ_67 SUPPORTING row (HQV splitting), NOT the φ_88 denominator | **DRIFTED** (wrong cross-row pairing) |
| 13 | F-row physical assignments | F2 = "hyperfine longitudinal-relaxation"; F3 = "spin-rotation chiral-pair sum (φ_88)"; F5 = "spin-orbit precession (φ_67)" | Canonical (inventory #47–#51 + watchlist): F1 = Caroli-Matricon ladder (φ_67); F2 = SABS axial-equatorial (φ_67); F3 = HQV splitting (φ_67 supporting); F4 = hypercharge Larmor (φ_88, cocycle-degenerate); F5 = acoustic-mode Jensen quench (φ_88-clean) | **SUPERSEDED** (draft's per-row physics + cocycle assignments do not match the landed F-table; in particular F5 is φ_88-clean in canon, φ_67 in draft) |
| 14 | "decisive triplet" status | F1+F2+F5 are the decisive triplet (firm) | W11-5 §VII.AJ REGISTRY-FAIL (S87 W5, `e1aef7ce…`): under the (S2) kernel-rank-invalid scenario the "decisive triplet" REBRANDS to "candidate" pending rank re-derivation; carry-forward `S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY`. The bridge-map and ratio are PRESERVED; only the spectral-excess-observable construction FAILed | **DRIFTED** (status-qualifier needed) |
| 15 | Protocol registry status | Paper pre-registers a protocol; implicitly novel/candidate | §VII.W-3.LAB now **STAGE-3-PERMANENT** (S100a, `89eab199…`; 11/11 PASS-AND, vdd × landau). Rows #47–#54b are STAGE-3-anchored laboratory predictions; the empirical Level-3 anchor stays DEFERRED-but-pre-registered (2027–2030 lab cycle) | **DRIFTED** (paper understates: this is now permanent) |
| 16 | Inventory rows #45/#46 | "pre-registers two new rows … landed by the W2-1 audit script" | Rows #45/#46 DID land (inventory lines 946–947); BUT the fuller B-phase suite #47–#51 (S87 W5-2) + A-phase #52–#54b (S87 W5-3) supersede them as the operative falsifier set. #45's Row-text uses `lab(F1)/lab(F3)`-style; #46 carries the 4-sf `7.3250` | **DRIFTED** (rows exist but are now the thin version of a richer landed suite) |
| 17 | Polycritical point values | `p ≈ 21.22 bar, T ≈ 0.7 mK` | Watchlist/protocol: `P_pc ≈ 21.22 bar, T_pc ≈ 2.273 mK` (`aalto-ltl-multi-session-protocol.md`). Draft's `T ≈ 0.7 mK` is inconsistent with the canonical `2.273 mK` | **DRIFTED** (T_pc value wrong) |
| 18 | §6 "α_s-equivalent at 3He-B" = NMR spin-tilt running | `alpha_s^lab := d²(ln ω_L)/d(ln p_eff)²` inherits `α_s_FW = −0.085873` modulo `(Δ_B/Δ_A)²`; predicted ≈ −0.0859 at ≈9σ | This is the paper's most speculative original construction. NOT independently landed in any register; the landed falsifier surface is the cocycle-ratio (Class B) + kernel-NULL (Class A), NOT an NMR running-of-running. No `alpha_s^lab` constant exists in canonical_constants | **STILL-OPEN** (paper-original, unverified, not in register) |
| 19 | Carry-forward #4 `S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM` | pre-registered for S88 | DISCHARGED: `S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM-V2` PASS (χ_M3 residual 0; homom 2.19e-15; AZ-BDI-DIII inheritance confirmed) | **CURRENT** (done — update paper to cite the PASS) |
| 20 | Carry-forwards #1/#2/#3/#5 (lab dispatch, ratio precision, Δ-ratio calibration, α_s extraction protocol) | pre-registered for S88 | Absorbed into the S90 `S90-3HE-B-LIAISON-WATCHLIST-LANDING` (CF-35) liaison schedule (5-element pre-registration; Q4-2026 first-contact, 2026–2029 program) | **DRIFTED** (superseded by the CF-35 liaison schedule) |

---

## §2 — What survives (verified against current rule text)

These are the load-bearing structural results in the paper that hold today. I verified each against the current canonical, not against the S87 state.

**S2.1 — The algebra-projection kernel structure (§3.1). SURVIVES, canonical.**
`χ : ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ)` sending M_3(ℂ)→0, with `ker(ι_*) = span{[φ_67],[φ_88]}` rank 2, is verbatim the canonical inheritance morphism (`3HeB-inheritance-canonical.md` §"Substitution chain"; `inheritance-falsifier-protocol.md` line 5). It was independently re-confirmed PASS at `S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM-V2` (BDI↔DIII compatibility, χ_M3 max residual 0.0, homomorphism residual 2.19e-15). The rank-2 kernel is exact: `rk K_*(A_K) − rk K_*(A_He) = 4 − 2 = 2` (Hodgkin on SU(3) vs S³). **Keep §3.1 essentially as-is.** One refinement: the draft attaches [φ_67] to "λ_6/λ_7 Gell-Mann directions" and [φ_88] to "λ_8 second Cartan element" — this matches the canonical W8-4 framework-unique directions {λ_6, λ_7, λ_8}; correct.

**S2.2 — The (Δ_B/Δ_A)^p cancellation theorem (§4). SURVIVES, canonical, operationally verified.**
The identity `lab(F_i)/lab(F_j) = ‖φ_a‖/‖φ_b‖ × (f_i/f_j)` with common exponent p, the factor cancelling exactly, is the canonical `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem"` (machine-precision 0.0e+00 residual, S86 W-5 DONE-5). This is the high-leverage discipline the rule itself flags (line 71: "Pre-registration of Gate 2 (cohomology-asymmetry) is the high-leverage discipline"). **Keep §4 in full** — it is the paper's strongest substrate-physics content. The cancellation is what makes the Class-B ratio substrate-falsifying rather than lab-conversion-dependent, and that argument is correct and still load-bearing.

**S2.3 — The 4-gate protocol structure (§5). SURVIVES as structure; verified against the current rule.**
Gates 1/2/3/4 (decisive-NULL / cohomology-ratio / supporting-NULL / slope-discrimination) map one-to-one onto `inheritance-falsifier-protocol.md §"Four-Gate Structure"` (lines 53–58). Both test classes (A kernel-signature, B cohomology-asymmetry) are pre-registered, satisfying the "Why both classes are required" mandate (rule lines 25–35). The "either alone is structurally insufficient" framing is correct. **Keep the 4-gate scaffold.** Caveat: the SPECIFIC per-row assignments and the Class-B cross-row pairing have drifted (§5.5, §5.6 below) and must be corrected to the landed F-table.

**S2.4 — Substrate-IS framing / direction of explanation (§6.4, §8, §10). SURVIVES.**
Every explanation flows substrate → bridge → laboratory. The 5-anatomy IS-not-IN block (§8.1) and the 3-level ladder (§8.2) are present with explicit values. This satisfies `phononic-framing.md §"IS Space, Not IN Space"` and the cross-pillar-bridge anatomy. The substrate-IS frame is NOT the problem — do not let the §3 fix touch it. (The fix at §3 is purely the evidential-grading caveat of S2.5 / §3.1-review, not a frame inversion.)

**S2.5 — Universality-class membership as the real substrate anchor. SURVIVES and is STRENGTHENED post-S87.**
The paper leans on BDI-protected inheritance throughout. Post-S97–S99, this is exactly the right thing to lean on: universality-class membership (BDI symmetry class, N₃=0, the χ-projection) is the durable claim. The S100a Stage-2 PASS-AND (vdd × landau) verified precisely the cocycle-ratio-preservation-under-χ structure. So the membership content the paper rests on is now the most independently-corroborated part of the whole 3He-B program. **This should be promoted to the paper's headline** (see §3).

---

## §3 — What must change

**S3.1 — Directional-inheritance framing → universality-class membership (evidential grading).**

The draft's abstract (lines 31–38) and §6.4 / §3 say "3He-B … is the laboratory parent into which the substrate inherits." This phrasing is NOT wrong — the canonical `3HeB-inheritance-canonical.md` Step 4 uses the identical "laboratory-parent" term and "substrate is logically prior." So do NOT rewrite it as "3He-B is an analog" (that is the FORBIDDEN framing per the canonical, and per my own memory rule the "analogy" framing for 3He-B is forbidden since S86 W1b-T8).

What must change is the EVIDENTIAL weight the direction carries. Per the S97–S99 re-audit (recorded in `project_3heb-inheritance.md` / the project memory: "the DIRECTION is a post-hoc stipulation, not evidence … universality-class membership (BDI/N₃=0/χ) is the real strength"), the paper must add a one-paragraph honesty caveat distinguishing two things:

- **Structural fact (keep, strong):** the inheritance morphism ι is a well-defined Kasparov-KK projection with non-trivial rank-2 kernel. This is a theorem (S88 W3a; CARTESIAN-CONFIRM-V2 PASS), and as of S100a the cocycle-ratio-preservation it implies is STAGE-3-PERMANENT.
- **Evidential scoping (add, honest):** the *choice* of arrow-direction (substrate as parent vs 3He-B as parent) is a post-hoc stipulation that organizes the correspondence; it is NOT itself observational evidence for the framework. The observational content is (i) the universality-class MEMBERSHIP (BDI / N₃=0 / χ), shared by substrate and 3He-B as a structural fact, and (ii) the lab-measurable cocycle-asymmetry ratio. The paper should say the arrow is a framing convention and the falsifiable physics is the membership + the ratio, not the arrow.

This is a substrate-first-preserving correction: the substrate stays logically prior; we simply stop letting "the direction" do evidential work it cannot do.

**S3.2 — α_s scale-and-channel tagging (the single largest content fix).**

The draft (abstract line 16; §2.1; §6) presents `−0.085873` as "the running of the scalar tilt" measurable on the cosmological scale by CMB-S4/CMB-HD. Per `phononic-framing.md §"Scale-and-channel-tagging"` (SUGGESTION at K=2) and atlas-09 Item 47, this single-scale reading is SUPERSEDED. The fix:

- Re-label `−0.08587279` as the **substrate-distance running** `alpha_s_substrate_distance_1` (s=3 Mellin pole, BZ-internal). Cite it as the substrate-IS observable.
- State that the CMB-PIVOT running is a DIFFERENT observable: `alpha_s_pivot_goldstone ≈ 0` (Goldstone-protected, S92, NOT superseded).
- State the two are 54.04 decades apart and that `deg(T_BZ→pivot) = +2 NON-SCALAR` (S93 W7-1, atlas-09 Item 47) is what decides which a detector measures — the substrate value is detector-facing at CMB-S4/CMB-HD, NOT at the Planck pivot.
- Mark `alpha_s = n_s² − 1` as the substrate-distance LO identity (which holds bit-exact, Sage-QQ S89 W7a `01c1ac83…`), NOT as "the CMB running." The constants `alpha_s_framework_central` and `alpha_s_cmb_central` are SUPERSEDED (S92 AH-TR-1) and must not be cited.

CRITICAL nuance for the rewrite agent: this is a re-SCOPE, not a retraction. The multi-σ falsifier did not vanish — it RELOCATED to the matched channel (CMB-S4 ~37σ / CMB-HD ~78σ reach; 13.99σ vs the current Aiola+2020 ACT-DR4+Planck anchor). Frame it as a strengthening (a sharper, channel-matched prediction), per `feedback_reporting-framing.md` (record where the falsifier MOVED, never that it was defined away).

**S3.3 — The §6 "α_s^lab NMR running-of-running" construction is paper-original and unverified — demote it.**

§6 builds `alpha_s^lab := d²(ln ω_L)/d(ln p_eff)²` and claims it inherits `−0.085873` at ≈9σ Aalto-LTL precision. This construction appears NOWHERE in the register. No `alpha_s^lab` canonical constant exists; the LANDED 3He-B falsifier surface is the cocycle-ratio (Class B) + kernel-NULL (Class A), not an NMR running-of-running. Moreover §6 inherits the superseded single-scale α_s reading. The rewrite must either (a) drop §6's quantitative ≈9σ claim entirely and replace it with the actual landed Class-A/Class-B predictions, or (b) explicitly tag the entire §6 NMR-running construction as SPECULATIVE-PAPER-ORIGINAL / not-in-register / pending a substrate-side derivation gate. I recommend (a): the paper does not need §6's invented observable, because the landed inventory rows already give it a falsifier surface that survived Stage-2.

**S3.4 — Class-B cross-row pairing: F1/F3 → F1/F5.**

§5.2 and §4.2 use `ratio_B := lab(F_1)/lab(F_3)`. The canonical Class-B ratio is `lab(F_1)/lab(F_5)` (φ_67-clean F1 over φ_88-clean F5; inventory Rows #51/#54b; watchlist Gate 2). In the landed F-table, F3 is a φ_67 SUPPORTING row (HQV splitting), so F1/F3 is a φ_67/φ_67 ratio — it does NOT yield the cross-cocycle 7.3250. Correct every F1/F3 to F1/F5.

**S3.5 — Per-row F-table physics must match the landed table.**

§4.2 / §5 assign F2 = hyperfine longitudinal-relaxation, F3 = spin-rotation chiral-pair sum (φ_88), F5 = spin-orbit precession (φ_67). The landed canonical (inventory #47–#51 + watchlist) is: F1 = Caroli-Matricon ladder (φ_67); F2 = SABS axial-equatorial pair correlation (φ_67); F3 = HQV splitting in restricted geometry (φ_67 supporting); F4 = hypercharge-twist Larmor anomaly (φ_88, cocycle-degenerate, Gate-4 slope); F5 = acoustic-mode dispersion under Jensen-modulus quench (φ_88-clean). Note the inversion: in the canon **F5 is φ_88-clean** (it is the ratio DENOMINATOR), whereas the draft calls F5 a φ_67 row. Replace the draft's F-row block wholesale with the landed assignments.

**S3.6 — Cocycle-ratio precision + mnemonic discipline.**

§3.2 cites `793346/108307 = 7.32497438 ≈ 7.324974 (6 sig figs)`. This is the F1 form. The CANONICAL constant is `substrate_cocycle_ratio_67_88 = 114453/15625 = 7.3249917526` (the F2 / R_machine form, re-pinned S93 W5-1 to `(δE_6·δE_7)/(δE_8)²`). Sage-verified: `793346/108307 = 7.3249743784` vs `114453/15625 = 7.324992`, differing at 6sf by `1.76e-5` — they AGREE only to 5sf (7.3250). The S92 §VII.AY workshop adjudicated F1-vs-F2 exactly this way (agree at 5sf, disagree at 6sf). Per `regulator-pin-discipline.md` mnemonic-vs-exact discipline + the watchlist's explicit instruction (line 388), registry-facing text must cite `7.324992` (Sage-exact), with `7.3250` as a 4-sf shorthand only. Fix: change all canonical citations to `7.324992` (114453/15625); keep `7.3250 ± 0.1%` only as the band-center shorthand with the Sage-exact form named.

**S3.7 — Status qualifiers the rewrite must carry.**

- The "decisive triplet" label (§5.1) must carry the W11-5 §VII.AJ REGISTRY-FAIL caveat: under the kernel-rank-invalid scenario it rebrands to "candidate" pending `S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY`. The bridge-map and ratio are PRESERVED (the FAIL is observable-construction-specific, not bridge-map-defective).
- The protocol must be stated as STAGE-3-PERMANENT (§VII.W-3.LAB, S100a), with the empirical Level-3 lab anchor DEFERRED-but-pre-registered (2027–2030).

**S3.8 — Polycritical T_pc: 0.7 mK → 2.273 mK.** §4.2 / §6 say `T ≈ 0.7 mK`. Canonical is `T_pc ≈ 2.273 mK` (`aalto-ltl-multi-session-protocol.md`; watchlist line 336). Correct it.

---

## §4 — New results since S87 that belong in the paper

1. **§VII.W-3.LAB STAGE-3-PERMANENT (S100a).** The cocycle-ratio-preservation-under-χ-inheritance bridge — this paper's exact Class-A+B structure — passed 2-agent Stage-2 cross-axis verification (`S100a-VIIW3LAB-STAGE2-VERIFY`, audit `89eab199…`, 11/11 clause PASS-AND; reviewers van-den-dungen × landau; both non-Stage-0; substrate-input-orthogonal: s87.npz→landau only, s89.npz→vdd only). This is the keystone update: the paper's protocol is now permanent, independently of its authors. (Atlas-04 K5; falsifier-master-inventory lines 1133–1139.)

2. **The full landed falsifier suite (S87 W5-2 + W5-3), which supersedes the paper's own #45/#46.** Rows #47–#51 (3He-B B-phase, gate `S87-W11-C5-LAB-FALSIFIER` PASS, value 7.324992, audit `d40a8d26…`) and Rows #52–#54b (3He-A A-phase, gate `S87-W11-C6-MUSR-FALSIFIER` PASS, audit `3e8a066e…`), with the cross-platform identical-ratio test (B-phase and A-phase both predict F1/F5 = 7.3250 ± 0.1% identically; disagreement forces re-anatomy). The A-phase chirality correction `χ_A = Δ_B²/⟨|Δ_A|²⟩_FS = 3/2 EXACT` (Volovik 2003 §3.4) is a clean substrate-derived result the paper should cite.

3. **CF-35 liaison schedule (S90 `S90-3HE-B-LIAISON-WATCHLIST-LANDING`).** A 5-element pre-registered Aalto LTL liaison schedule (Q4-2026 first contact; 2026–2029 program; Krusius+Tuoriniemi+Eltsov groups; substrate ratio 7.324992 ± 0.1%) now exists. The paper's §9 carry-forwards #1–#3/#5 are absorbed into it. CF-35 status: STILL-OPEN (forward-falsifier, liaison-state poll cadence). Important caveat the rewrite must surface: per the project memory, **CF-35's 7.324992 is post-hoc — it is a genuine falsifier ONLY if its observable is unmeasured.** The paper's "± 0.1% pre-registration" is sound precisely because no lab datum yet exists; the rewrite should state this explicitly (the ratio is a pre-registered prediction on an unmeasured observable, not a fit to existing 3He-B data).

4. **`S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM-V2` PASS** discharges the paper's §9 carry-forward #4 (BDI↔DIII compatibility; χ_M3 residual 0, homomorphism residual 2.19e-15).

5. **α_s two-scale resolution (S92 AH-TR-1 / S93 W7-1; atlas-09 Item 47).** The substrate-distance vs Goldstone-pivot separation and `deg(T_BZ→pivot)=+2 NON-SCALAR`. This is the content fix of §3.2.

6. **The α_s surviving-route rank table (S87 W9a-2), `(iii) ≻ (iv) ≻ (i) ≻ (ii)`.** The paper's single-pole Mellin route (i) is ranked THIRD of four; the more robust routes are (iii) GGE-relic Bogoliubov occupation-variance and (iv) BdG K-running near K_sat. If the paper keeps any α_s-route framing, it should acknowledge route (i) is not the most substrate-robust route. (Inventory lines 984–991.)

---

## §5 — Reference / anchor audit

| Draft citation | Exists? | Says what the draft claims? |
|:---------------|:--------|:----------------------------|
| Gate `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT` PASS | YES | YES — verdict line present, audit `1f38f9888538011c…`, content `bde3ad80…`, value `paper_artifact_present_with_substrate_IS_prediction`, scheme `single-pole-Mellin-substrate-distance-1`, convention `inheritance-morphism-3He-B-BdG-canonical`. Paper is a verified PASS artifact. |
| `papers/s87-3he-b-alpha-s-equivalent.md` audit script | YES | `computations/session-87/s87_w2_3he_b_alpha_s_paper_audit.py` exists (MCP provenance). Note: draft §12 cites it as `computations/s87_w2_…` (no session subdir) — minor path drift; canonical lives under `session-87/`. |
| Inventory Rows #45 + #46 | YES (landed) | PARTIALLY — they landed (lines 946–947) but #46 uses 4-sf `7.3250` and the suite was superseded by #47–#54b. The draft's claim "extending the suite from 9 atomic predictions to 11" (§7.2) is the S87-era bookkeeping; the inventory is now far larger. |
| `inheritance-falsifier-protocol.md` 4-gate + cancellation | YES | YES — draft's protocol matches the rule's Four-Gate Structure and cancellation theorem verbatim. |
| `cross-pillar-bridge-anatomy.md` 5-anatomy + 3-level | YES | MOSTLY — anatomy present; but the rule has since grown a large directive index (Level-2 binding/non-binding sub-class, OE-form discipline, etc.). The draft's §8 5-anatomy block predates the OE-form MANDATORY discipline (Element-2 must be operator-expression form); a re-anchor should check Element-2 OE-form compliance. |
| `n_s_framework = 0.9561` | YES | YES — `n_s_FW_exact = Fraction(9561,10000)`, canonical. |
| `cocycle_norm_phi67 = 0.793346`, `phi88 = 0.108307` | YES | YES — both canonical, not superseded. |
| `substrate_cocycle_ratio_67_88` | YES | DRIFTED — canonical is `7.3249917526` (114453/15625), NOT the draft's `7.32497438` (793346/108307). See §3.6. |
| `Delta_BCS = 0.4642547394830737` | YES | Canonical pin exists; value consistent with my memory (`Delta_BCS = 0.464`). |
| `tau_fold = 0.19` | YES | Canonical `tau_fold = 0.190`. (Draft writes `0.19`; equivalent.) |
| "S50–S51 atlas single-pole Mellin `α_s = n_s² − 1`" | PARTIALLY | The identity holds bit-exact (S89 W7a); but `alpha_s_cmb_central`'s S50 identity@observed-pivot is SUPERSEDED (S92). The draft cites it as the live CMB reading — wrong scope. |
| Plan `sessions/session-plan/session-87-plan-w2.md §W2-1` | LIKELY (archived) | Session-87 plans are archived; the gate provenance confirms the plan existed. Not independently re-verified on disk this pass (low-leverage). |
| "S86 W-5 W11-C5/C6 calibration corpus" | YES | YES — `inheritance-falsifier-protocol.md §"Canonical lab platforms (3He-B)"` carries W11-C5 (vortex-core) + W11-C6 (3He-A µSR). |
| Aalto LTL / Lancaster MCT-3 / Helsinki ROTA platforms | YES | MOSTLY — platforms match the canonical lab-platform list. But the draft's specific F-row→platform→physics mapping drifted (§3.5). The current inventory wording (Rows #47–#54b) is the authority; `mack-cosmic-bridge` is sole writer of that surface. |

No fabricated anchors found. The paper's citations are real; the drift is in VALUES (ratio precision, T_pc), SCOPE (α_s channel), and STATUS (the protocol is now permanent, the suite is now larger).

---

## §6 — Rewrite plan (section-by-section, mechanically executable)

A rewrite agent can execute the following in order. Each item names the section, the action, and the canonical source to pull from.

- **§1 Abstract.**
  - Replace "the running of the scalar tilt" (line 16) with "the substrate-distance running of the scalar tilt (`alpha_s_substrate_distance_1`, s=3 Mellin pole, BZ-internal)." Add one clause: "distinct from the Goldstone-pivot running `alpha_s_pivot_goldstone ≈ 0` at the CMB pivot; the two are 54.04 decades apart, `deg(T_BZ→pivot)=+2 NON-SCALAR` (S93 W7-1)."
  - Replace `7.3250 ± 0.1%` canonical citation with `7.324992 ± 0.1%` (Sage-exact 114453/15625), keeping 7.3250 as the 4-sf shorthand.
  - Add one sentence: "The Class-A+B protocol registered here is, as of S100a, STAGE-3-PERMANENT (§VII.W-3.LAB, Stage-2 PASS-AND `89eab199…`)."
  - Keep the "3He-B is the laboratory parent" sentence (it is canonical) but add the §3.1 evidential caveat (one sentence: the arrow is a framing convention; the falsifiable physics is universality-class membership + the cocycle ratio).

- **§2 (α_s prediction).**
  - §2.1: keep the value `−0.08587279`. Re-tag it `alpha_s_substrate_distance_1`. Replace "the identity holds at the scheme-identity level" framing's CMB conflation: state explicitly this is the substrate-distance LO term (bit-exact Sage-QQ, S89 W7a), NOT the CMB-pivot running.
  - §2.3: rewrite the "Falsifying it requires (i) a direct CMB-S4 measurement of α_s on the cosmological scale" — re-scope to: the substrate-distance value is detector-facing at CMB-S4/CMB-HD via the +2 transport degree (13.99σ vs current anchor); the pivot leaf (≈0) is the matched-channel Planck reading. Pull exact framing from atlas-09 Item 47 + watchlist `α_s` row.
  - Add a short subsection citing the S87 W9a-2 surviving-route rank `(iii)≻(iv)≻(i)≻(ii)`; note that this paper's single-pole route is route (i), ranked 3rd.

- **§3 (inheritance morphism).** Keep §3.1 (canonical). In §3.2: change the ratio to the canonical `114453/15625 = 7.324992` form; explain the F1-vs-F2 distinction (S92 §VII.AY: agree 5sf, disagree 6sf) and cite the S93 W5-1 re-pin to `R_machine = (δE_6·δE_7)/(δE_8)²`. Add the S3.1 evidential caveat paragraph here (direction = stipulation; membership = evidence). Cite `S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM-V2` PASS as the morphism's independent confirmation.

- **§4 (cancellation theorem).** Keep in full (strongest content). Fix T_pc to 2.273 mK. Fix the F-row physics block to the landed F-table (§3.5). Change the Class-B example pairing from F1/F3 to F1/F5.

- **§5 (Class A + B protocol).** Replace the per-row F-table (F1–F5 assignments) with the landed canonical (inventory Rows #47–#51). Add the W11-5 §VII.AJ "decisive triplet → candidate" status caveat to §5.1. Change §5.2 Class-B ratio to F1/F5. State the protocol is STAGE-3-PERMANENT.

- **§6 (NMR α_s^lab running).** RECOMMENDED: delete the quantitative ≈9σ NMR-running-of-running construction (paper-original, not in register, inherits superseded single-scale α_s). Replace with a short statement of the actual landed lab predictions: Class-A NULL on F1+F2+F5 (decisive) + F3+F4 (supporting); Class-B ratio 7.324992 ± 0.1% on F1/F5; Gate-4 multi-pressure slope on F4 (Jacobi-cubic vs φ_88-linear, 0–34 bar). If kept, tag the whole §6 SPECULATIVE-PAPER-ORIGINAL with an explicit "not in register; pending substrate-side derivation gate" banner. Keep §6.4 (direction of explanation) verbatim.

- **§7 (inventory rows).** Update: rows #45/#46 DID land but are now the thin precursor of the richer #47–#54b suite; cite the S100a STAGE-3-PERMANENT promotion. Note `mack-cosmic-bridge` is the sole writer of the inventory surface — the paper documents, it does not author rows. Update "9 → 11 predictions" to reflect that the operative suite is now #47–#54b (5 B-phase + A-phase cross-platform).

- **§8 (cross-pillar anatomy).** Re-anchor the ratio numbers to `7.324992`. Check Element-2 OE-form compliance against the current `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"` (MANDATORY since the draft was written). The Level-3/Level-2 numbers use the F1 ratio `7.32497438` — re-state against `7.324992`.

- **§9 (carry-forwards).** Mark #4 DISCHARGED (CARTESIAN-CONFIRM-V2 PASS). Mark #1/#2/#3/#5 absorbed into the CF-35 liaison schedule. Add the CF-35 post-hoc caveat (ratio is a falsifier only because the observable is unmeasured).

- **§10/§11/§12.** Update §11 references: replace the `substrate_cocycle_ratio` citation with the canonical 114453/15625 form; mark `alpha_s = n_s² − 1` as the substrate-distance LO identity (not CMB). Fix §12 audit-script path to `computations/session-87/s87_w2_3he_b_alpha_s_paper_audit.py`.

---

## §7 — Verdict

**RESTRUCTURE.** Not REWRITE-IN-PLACE (the α_s channel re-scope, the F-table replacement, and the §6 deletion are structural, not line-edits). Not RETIRE-AND-REPLACE (the core substrate physics — kernel structure, cancellation theorem, 4-gate protocol — survives and has in fact been PROMOTED to permanent since the draft was written; there is real, now-corroborated content to preserve).

**Publication-track vs falsifier-master-inventory as canonical home — recommendation: DEMOTE from standalone publication-track to a substrate-physics companion of the inventory rows.**

Rationale:
- The FALSIFIABLE content of this paper (Class-A NULL predictions, Class-B cocycle ratio, Gate-4 slope, the lab platforms and horizons) now lives canonically and more completely in `falsifier-master-inventory.md` Rows #47–#54b + the CF-35 liaison schedule + the §VII.W-3.LAB STAGE-3-PERMANENT theorem. The inventory is the live, sole-writer-maintained, register-current home; it superseded this paper's #45/#46 within the same session (S87 W5-2/W5-3) and has been promoted to permanent since.
- A standalone paper that re-states a now-permanent theorem's falsifier rows, while carrying superseded α_s channel framing and a paper-original unverified NMR observable, is a version-synchronization liability: it will drift from the inventory every session unless someone maintains it, and it is not the register anyone cites.
- What the paper uniquely offers that the inventory does NOT is (a) the substrate-physics EXPOSITION of WHY the cancellation theorem makes the ratio substrate-falsifying, and (b) the direction-of-explanation pedagogy. That is companion/exposition value, not primary-register value.

Therefore: keep the paper as a **substrate-physics exposition companion** (a readable derivation of the cancellation theorem + the inheritance-morphism kernel structure, pointing to the inventory rows as the canonical falsifier surface), OR fold its surviving exposition into the §VII.W-3.LAB registry entry's prose. Do NOT maintain it as a parallel canonical falsifier surface — the inventory is that surface, and `mack-cosmic-bridge` is its sole writer. If kept in `papers/`, the header must carry a "register-of-record: falsifier-master-inventory Rows #47–#54b + §VII.W-3.LAB (STAGE-3-PERMANENT)" pointer so no future reader treats the paper's numbers as canonical.

One concrete next computable question, if the paper is retained and someone wants to upgrade it past exposition: derive (or refute) the §6 `alpha_s^lab := d²(ln ω_L)/d(ln p_eff)²` NMR running-of-running from the substrate side as an actual gate (substrate-derived prediction + pre-registered threshold), so that §6 either becomes a real landed falsifier or is honestly retired. As written it is neither.

---

## Appendix — Sage verification (cocycle-ratio precision)

```
phi67/phi88 (draft F1 form) = 793346/108307 = 7.3249743783873615
canonical const (F2 form)   = 114453/15625  = 7.324992
equal? False ; difference = 1.7621612638148965e-05  (agree to 5sf, disagree at 6sf)
```
Confirms §3.6: the draft's "7.324974 (6 sig figs)" is the F1 ratio of the published cocycle norms, NOT the canonical `substrate_cocycle_ratio_67_88 = 7.324992` (114453/15625, S86 W-5 CANONICAL-5, re-pinned S93 W5-1). Registry-facing text must cite the canonical form.
