# Review — "Running of the Spectral Index for Ornstein-Zernike Propagators: An Exact Algebraic Identity and Its Implications"

**Reviewer**: mack-cosmic-bridge (sole writer of this file)
**Target paper**: `papers/alpha-s-ns/main.tex` (456 lines) + `papers/alpha-s-ns/references.bib`
**Paper era**: ~March 2026, framework ~S50–S53
**Review epoch**: post-S103 (2026-06-12)
**Scope**: REVIEW ONLY. No edits to the paper or any other file.

---

## Executive orientation (read first)

The paper has **two cleanly separable layers** and they have aged in opposite directions:

1. **The exact algebra** (`α_s = n_s² − 1` for O-Z propagators, its `K^a` generalization, the five suppression proofs as statements about the O-Z *sector*). This is **untouched and has been STRENGTHENED** — at the framework's own substrate n_s = 9561/10000 the identity is now a **bit-exact rational** (`α_s = −8587279/100000000` EXACTLY in ℚ; 9561² = 91412721 is a perfect square). The mathematical spine is publishable as-is, modulo a small rounding correction (§2 below).

2. **The physical confrontation** ("5.0–6.0σ tension at lattice-scale identification, conditional on a ~10⁻⁵⁷ scale mapping", "α_eff = 1.21 SA-correlator as identity-breaker", the mass problem, the scale-mapping-as-open-problem framing). This layer is **SUPERSEDED at the structural level** by the S92–S94 transport-degree resolution. The paper's "load-bearing assumption I cannot derive" (`K_pivot ∼ M_KK` vs `K_pivot ∼ 10⁻⁵⁷ M_KK`, a 57-decade ambiguity it leaves OPEN) has since been **RESOLVED**: the substrate carries **TWO scale-separated α_s observables**, and *which* a detector measures is set by a single **computable, derived** transport degree `deg(T_{BZ→pivot}) = +2` (NON-SCALAR), now **STAGE-3-PERMANENT** (S94 W1-1). The 54.04-decade separation is the canonical replacement for the paper's hand-estimated `10⁻⁵⁷`.

The paper's intellectual honesty is its saving grace: it *explicitly* flagged the scale mapping as "the decisive open problem" and labelled the tension "conditional." The framework has since closed exactly that open problem. So the rewrite is not a retraction — it is **the resolution the paper itself called for**. The "−12σ-class tension" did not vanish: it **relocated** to a matched channel (CMB-S4/CMB-HD substrate-sensitivity, ~34σ reach) as a **live future falsifier**, while the **CMB pivot image is +0.67σ — CONSISTENT** with Planck.

**One caveat for an external paper**: nearly all of the load-bearing resolution lives in internal artifacts (gate `S93-W7-1`, registry §VII.BA/§VII.BG, atlas-09 Item 47, `cross-pillar-bridge-corpus.md §23`). A public paper cannot cite these; the transport-degree mechanism must be **re-derived self-contained** or the paper must be **explicitly scoped to the pure mathematics + a conditional-physics appendix**. This is the central rewrite decision (§7).

---

## §1 Claim-Audit Table

Status legend: CURRENT = still canonical; DRIFTED = value/number changed but claim-type intact; SUPERSEDED = replaced by a newer structural result; RETRACTED = claim was wrong; STILL-OPEN = genuinely open then and now.

| # | Load-bearing claim (paper) | Paper's version | Current canonical (value + source) | Status |
|:--|:--|:--|:--|:--|
| 1 | Core identity `α_s = n_s² − 1` for O-Z `P=T/(JK²+m²)`, K-indep params | exact, parameter-free | UNCHANGED; now **bit-exact in ℚ** at framework n_s: `n_s_FW_exact = Fraction(9561,10000)` ⇒ `α_s = −8587279/100000000` EXACTLY (`canonical_constants.py:2405`; §VII.AN-CORRIGENDUM; Sage-verified this review) | **CURRENT** (upgraded) |
| 2 | Generalization `α_s = −(a−1+n_s)(1−n_s)` for `K^a`; a=2 recovers core | exact | UNCHANGED; Sage-verified a=2 reduces to `n_s²−1` exactly | **CURRENT** |
| 3 | Five suppression proofs (multi-pole, running mass, zero-mode, RPA, Goldstone) as bounds *within the O-Z sector* | `|δα_s|` ≤ 1.3×10⁻³ | Statements about the O-Z *sector* are intact (they are framework-parameter computations at S50–S51 values). NOTE the explicit disclaimer "do not establish CMB ∈ O-Z sector" is **exactly right** and should be retained verbatim | **CURRENT** (as sector-bounds) |
| 4 | n_s value used to make the prediction | Planck-extended `0.9625 ± 0.0048` | Three distinct n_s now exist; see #5–#7. The Planck value is an **observational anchor**, NOT the framework prediction | **SUPERSEDED** (role re-cast) |
| 5 | Framework predicted-n_s (implicit: O-Z m-fit to 0.965) | fitted via `m_* = 11.87 M_KK` | `n_s_framework = 0.9561` (const-ε gauge-invariant, S84 T6 / S85 W9-3) and committed `n_s_FW_sqrt_cutoff = 0.9590` (S103 W5-2, √x BCS+1-loop, 1.40σ Planck). NOT obtained by fitting an O-Z mass | **SUPERSEDED** |
| 6 | Predicted running `α_s = −0.0734 ± 0.0092` at n_s=0.9625 | central −0.0734 | **Arithmetic slip**: at n_s=0.9625 the exact value is `−471/6400 = −0.07359375` ≈ **−0.0736**, not −0.0734 (Sage-verified). σ = 0.00924 ✓. More importantly the VALUE is now re-homed: see #8/#9 | **DRIFTED** (+ rounding error) |
| 7 | "−0.073 at the lattice scale, factor-16 above Planck" tension | 5.0–6.0σ | **SUPERSEDED**: relocated by scale/channel. The single-pivot comparison was atlas-09 **Item 47** "first multi-sigma falsifier (−12.146σ Planck / −13.99σ Aiola)" → **CORRECTED** S93 W7-1 to a SCALE-MISMATCH, not a falsification | **SUPERSEDED** |
| 8 | Goldstone-pivot running (the value a CMB detector at pivot sees) | implicitly the −0.073 | `alpha_s_pivot_goldstone = 0.0` (S92 AH-TR-1; Goldstone-protected, \|α_s\|≤5e-3; **+0.67σ vs Planck**, machine-zero 8.4e-15 at S74) | **SUPERSEDED→NEW** |
| 9 | Substrate-distance running (inside-BZ value) | conflated with the pivot value | `alpha_s_substrate_distance_1 = −0.08587279` (S92 AH-TR-1; Mellin pole s=3; FI-class regulator-invariant over 5-regulator atlas; **sign-walled negative**; frozen-now, cannot drift to meet CMB-S4) | **SUPERSEDED→NEW** |
| 10 | Scale mapping `K_pivot ∼ M_KK` "not derived; 5–6σ conditional on it" | OPEN, the decisive problem | **RESOLVED**: `deg(T_{BZ→pivot}) = +2` NON-SCALAR (gate `S93-W7-1`, PASS; `factorization_holds=False`, `formulation=T4-non-scalar`). The transport degree IS the physics deciding pivot-vs-substrate; STAGE-3-PERMANENT §VII.BA(h)/§VII.BG (S94 W1-1) | **SUPERSEDED** (open→closed) |
| 11 | Scale separation magnitude | `K_pivot ∼ 10⁻⁵⁷ M_KK` (naive `k_*/M_KK`) | Canonical: **54.04 decades** of k between transit/substrate and CMB pivot (`phononic-framing.md §"Scale-and-channel-tagging"`; the per-observable transport map, not a naive ratio) | **DRIFTED** (10⁻⁵⁷ → 54.04-decade transport) |
| 12 | α_eff = 1.21 SA-correlator as identity-breaking candidate | the open compute that "could rescue" | SA-correlator (S50, atlas-10 #12) + SA-Goldstone mixing (S51, atlas-10 #13) remain PROVEN-as-registered but the mixing gate `T3-BATCH-S51-SA-GOLDSTONE-MIXING` is **INFO/MIGRATED** — no post-S88 advance. The transport-degree mechanism (#10) **supersedes SA-mixing as the explanation** for pivot≈0 vs substrate=−0.0859 | **SUPERSEDED** (as mechanism) / STILL-OPEN (as a distinct correlator computation) |
| 13 | The mass problem `m_* = 11.87 M_KK` (170× Leggett mass) | unsolved, entangled with α_s | Artifact of the O-Z-fit framing (#5). With n_s now a *spectral-geometry* output (a₂/Goldstone), there is no O-Z mass to fit, so the "mass problem" **dissolves** rather than persists. NOT a current open item | **SUPERSEDED** (dissolved by re-framing) |
| 14 | CMB-S4 decisive: `σ(α_s) ∼ 0.003` → 8σ / >20σ | conditional on lattice ID | CURRENT in *kind* (CMB-S4 IS the decisive instrument) but the figure is re-homed: substrate value is a **~34σ-reach** CMB-S4(2030)/CMB-HD(2035) falsifier of the s=3 Mellin identity at the **matched channel** (falsifier-master-inventory Row #3; capstone §7.2 Row #3) | **DRIFTED** (re-homed to matched channel) |
| 15 | Planck base ΛCDM `n_s=0.9649, α_s=−0.0045±0.0067` | quoted as consistency-with-zero anchor | CURRENT (`planck_ns=0.9649`, `planck_alpha_s=−0.0045`). NOTE the framework's **own** canonical α_s pin updated to Aiola+2020 `+0.0023±0.0063` (`alpha_s_canon_2020`, S86 W13) for internal gates — but Planck-2018 is the right anchor for a *paper* quoting the 2018 release | **CURRENT** |
| 16 | r = 0 (paper's tensor entry in Table 1) | r=0, "consistent <0.06" | Framework r is **0.033** (dual-pathway Path-H 0.00745 / Path-C 0.0117), PASS within 2σ of BICEP/Keck <0.036 (capstone §7.1). The paper's "r=0" is wrong for the framework | **RETRACTED** (r≠0) |
| 17 | "α_s = n_s²−1 absent from literature" prior-art claim | no prior statement found | Plausibly still true for this exact functional form, but the paper should distinguish the *kinematic O-Z* statement (likely novel) from generic *single-pole rational propagator* running (well known in stat-mech). Unverifiable as an absolute negative; soften | **STILL-OPEN** (claim un-auditable) |
| 18 | "α_s linear in tilt vs slow-roll quadratic" distinguishing signature | `α_s ≈ −2ε` vs `O(ε²)` | CURRENT as a mathematical contrast. But note: the *framework's* CMB-pivot prediction is **≈0** (Goldstone), i.e. it looks slow-roll-like at pivot; the −2ε behavior lives at the substrate/BZ leaf. The "signature" statement must be channel-tagged | **DRIFTED** (channel-dependent) |

---

## §2 What Survives (the exact algebra)

**The mathematics is intact and was independently re-derived inside the framework.** Verification this review (Sage QQ):

- `n_s = 9561/10000` ⇒ `n_s² − 1 = −8587279/100000000 = −0.08587279` **EXACTLY** (no rounding). `9561² = 91412721` confirmed perfect square. This is the **bit-exact ℚ upgrade** the prompt flagged — the identity is not merely numerically close, it is an *exact rational identity* at the framework's substrate tilt. (Registry home: §VII.AN-CORRIGENDUM, lines 17181–17192; `canonical_constants.py:2405`.)
- Generalized `a=2` form `−(a−1+n_s)(1−n_s)` reduces to `n_s²−1` exactly. ✓
- Proposition 1 derivation (the Möbius-transformation-composed-with-log-derivative argument, eq. 116–140) is correct as written.

**What this means for the paper**: Proposition 1, Corollary 1 (Ka generalization), and the three Remarks are publishable verbatim. They are *kinematic* facts about O-Z correlators, true independent of any framework. The framework's contribution is that its substrate n_s happens to make the identity bit-exact — a striking but **secondary** observation that belongs in a remark, not the headline.

**One correction inside the surviving math** (claim #6): the paper's "−0.0734 at n_s=0.9625" is an arithmetic slip. The exact value is `−471/6400 = −0.07359375 ≈ −0.0736`. The σ=0.0092 is correct. If the rewrite keeps any n_s=0.9625 evaluation it must read −0.0736.

**The five proofs survive AS SECTOR-BOUNDS.** Crucially, the paper *already* states (lines 183, 443) that the five proofs bound corrections *within the O-Z sector* and explicitly do NOT establish that the CMB belongs to that sector. This disclaimer is exactly the right epistemic move and is **more important now than when written**, because the transport-degree resolution shows the CMB-pivot observable is precisely the Goldstone leaf where the O-Z-sector value does NOT apply. Retain the disclaimer; it ages into a strength.

---

## §3 What Must Change

### 3a. Stale values / numbers
- **−0.0734 → −0.0736** (arithmetic, claim #6).
- **`K_pivot ∼ 10⁻⁵⁷ M_KK` → 54.04-decade transport map** (claim #11). The naive `k_*/M_KK` ratio is superseded by the per-observable transport degree; the IR scale separation is canonically **54.04 decades**, not a hand-estimated 10⁻⁵⁷.
- **"r = 0" → r = 0.033** (claim #16) in Table 1, or drop the r row (it is not this paper's observable and the value is wrong).
- **n_s role**: 0.9625 is an *anchor*, not the prediction. The framework prediction is 0.9561 (const-ε) / committed 0.9590 (√x). Do not present 0.9625 as "the framework's n_s."

### 3b. Superseded narrative (the central rewrite)
The entire "5.0–6.0σ tension, conditional on an underived `K_pivot ∼ M_KK`" arc (§4.3–§4.4, §5.4) is **the pre-resolution framing**. It must be replaced by the **dual-observable / transport-degree** picture:
- There are **two** substrate α_s observables, not one ambiguously-scaled one.
- `deg(T_{BZ→pivot}) = +2` (NON-SCALAR, derived) decides which a detector measures. This is the answer to the paper's own "decisive open problem."
- At the **CMB pivot**: framework α_s ≈ 0, **+0.67σ vs Planck — CONSISTENT**.
- At the **substrate/BZ leaf**: α_s = −0.08587279, a **live ~34σ-reach CMB-S4/CMB-HD falsifier** at the matched substrate-sensitivity channel.
- The "−12σ tension" is a **scale-mismatch artifact** (comparing a BZ-scale running against the CMB-pivot datum), **not a falsification**. It relocated; it did not vanish.

### 3c. Framing violations vs `phononic-framing.md`

The paper is written in **container/inflation vocabulary throughout** — understandable for an external O-Z/stat-mech audience, but several passages invert the substrate-first direction and one mandatory standing rule is now violated:

1. **SCALE-AND-CHANNEL-TAGGING (standing rule, `phononic-framing.md §"Scale-and-channel-tagging for running/tilt observables"`)**: *every* running/tilt observable MUST declare its matched (scale, channel) pair. The paper presents a single un-tagged α_s and asks "which scale?" as an open question. A post-S103 rewrite MUST comply: tag the pivot value (Planck/CMB channel) and the substrate value (CMB-S4/CMB-HD substrate-sensitivity channel) explicitly. This is the single hardest compliance requirement.
2. **"If the CMB power spectrum is identified with an O-Z propagator at lattice scale…"** (abstract, §4.3): container-thinking framing — it treats the CMB as a thing that *might live in* the O-Z sector. Substrate-first: the substrate IS the spectral content; the CMB-pivot running is the Goldstone-leaf image of the substrate's spectral moments under the transport map. The "identification" is not a free modelling choice — the transport degree fixes it.
3. **"57 orders of magnitude" / "compresses 57 orders" (§4.4, §5.4)**: the naive expansion-history ratio. The substrate-first object is the transport map `T_{BZ→pivot}`, whose degree (+2) is the physics; the 54.04-decade k-separation is its scale.
4. **Lattice/crystal vocabulary** ("32-cell lattice", "Josephson tunneling", "tessellation"): per atlas-09 Item 39/43, the crystal-layer organizing picture is SUPERSEDED by the resonator picture (`Phononic-Substrate-Geometry.md`, S84). The constructive content survives, but a current paper should at minimum note that the lattice is a *projection* of the spectral-triple substrate, not the fundamental object. **The substrate IS the resonator; the O-Z correlator is a low-energy Goldstone-sector image.**

Note: none of these are fatal for an *external* paper — the lattice/Josephson language is legitimate as the laboratory-IN projection. But the (scale, channel) tagging is non-negotiable, and the "open scale-mapping problem" narrative is simply false post-S93.

---

## §4 New Results Since the Paper's Era (that belong in it)

These are the post-S53 developments the rewrite must fold in. All are internal artifacts — see §7 for how to surface them to an external audience.

1. **Dual-observable resolution (S92 AH-TR-1)**. Two scale-separated α_s: `alpha_s_pivot_goldstone = 0.0` (CMB pivot, Goldstone-protected) and `alpha_s_substrate_distance_1 = −0.08587279` (inside-BZ, Mellin pole s=3). Source: `canonical_constants.py:1568,1571`; `s92-adhoc-alpha-s-transfer-map-identity.md`.
2. **Transport degree (S93 W7-1, STAGE-3-PERMANENT S94 W1-1)**. `deg(T_{BZ→pivot}) = +2`, NON-SCALAR, `factorization_holds=False`. The composite bridge map `T5 = HKR ∘ Connes-Karoubi K₀-pairing` is the unique admissible Element-3 at the coupling's home pole; `|deg(a4/a2)| = 2 = |d_A|`. Registry: §VII.BA(h), §VII.BG (lines 20164, 20802–20805). This is the **derived** answer to the paper's open scale-mapping problem.
3. **FI-class regulator invariance**. The −0.08587279 substrate running is FI (Functional-Invariant) across the 5-regulator atlas {ζ, SDW, Pauli-Villars, Mellin, lattice} — regulator-invariant, frozen-now. It *cannot* drift to meet CMB-S4 (this is what makes it a clean falsifier). Source: `alpha_s_substrate_distance_1` provenance (orig S88 W4 P5; S91 W9 5-regulator).
4. **Sign-wall**. The substrate α_s is SIGN-WALLED negative by spectral-action monotonicity (the [SIGN] sub-check at §VII.BG: `t5_image_signed = −1.493993 < 0`, GV-Heitsch odd-grading negative). The red-tilt sign is structural, not fitted.
5. **Bit-exact rational (S88 W-15)**. `α_s = −8587279/100000000` EXACTLY at `n_s_FW_exact = Fraction(9561,10000)`. Replaces the scheme-dependent floats.
6. **S103 commit branch (S103 W5-2)**. `n_s_FW_sqrt_cutoff = 0.9590` COMMITTED under the Chamseddine-Connes √x generating functional (Row #85 HELD→COMMITTED-LIVE, 1.4048σ vs Planck; A₅→A₆ atlas-cardinality robust). This is the framework's committed CMB-pivot tilt; the O-Z-fit n_s (paper's 0.965-via-m_*) is not how the framework gets n_s.
7. **Atlas-09 Item 47** is the formal register-of-record for the whole α_s rescoping (the single most useful internal anchor for the rewrite): "the multi-σ reading RELOCATES to the matched channel as a live prediction — a strength, not a defined-away tension."

**Net effect on the paper's thesis**: the paper framed itself as "an exact identity that predicts a 5–6σ tension, IF an underived scale mapping holds." The honest post-S103 thesis is: "an exact identity whose two scale-separated images are (a) **consistent** with Planck at the pivot and (b) a **live future falsifier** at the substrate channel, with the scale mapping now derived (deg=+2)." This is a **stronger and more honest** paper — it trades a conditional tension for a resolved mechanism plus a concrete future test.

---

## §5 Bibliography Audit

Ten `needed:` keys. Verified-existing candidates are marked ✓ (checked via paper-search MCP this review); others are standard references whose existence I assert from the bib metadata but did NOT fetch — marked accordingly. **No fabricated references.**

| Key | Paper's placeholder | Proposed real reference | Verification |
|:--|:--|:--|:--|
| `needed:Planck2018` | Planck 2018 VI | **Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters", A&A 641, A6 (2020), arXiv:1807.06209** | ✓ fetched (arXiv 1807.06209v4); the .bib entry is already correct — just drop `needed:` prefix |
| `needed:Liddle-Lyth` | slow-roll α_s ~ O((1−n_s)²) | **Liddle & Lyth, *Cosmological Inflation and Large-Scale Structure*, CUP (2000)** | NOT fetched (book; metadata in .bib is standard and correct). Alternatively cite Kosowsky & Turner, PRD 52, R1739 (1995) for the slow-roll running formula specifically |
| `needed:Ornstein-Zernike` | O-Z correlator | **Ornstein & Zernike, Proc. Acad. Sci. Amsterdam 17, 793 (1914)** | NOT fetched (1914, pre-arXiv; the .bib entry is the standard citation). Consider adding a modern textbook anchor: Chaikin & Lubensky, *Principles of Condensed Matter Physics*, CUP (1995), §2.4 |
| `needed:phonon-exflation` | the framework paper | **Self-citation to the companion `Phonon-Exflation Cosmology` paper** (in prep). Keep as `@misc{...,note={In preparation}}` until the companion has a DOI/arXiv id | internal; cannot verify externally |
| `needed:S47-texture` | Josephson lattice stiffness | Internal computation S47. **External paper cannot cite a session script.** Either (a) move the stiffness-tensor derivation into an appendix self-contained, or (b) cite it via the companion framework paper §(stiffness). Mark as internal-artifact-not-citable | internal |
| `needed:S49-bayes` | MC posterior for α_s | Internal S49 (`s49_alpha_s_bayes.npz`). Same issue — the MC is trivial (Gaussian propagation through 2n_s·σ); **inline the one-line error propagation** instead of citing a script. No external ref needed | internal |
| `needed:S50-leggett-prop` | 3-pole Leggett propagator | Internal S50. The 3-pole numbers (m_base²=140.5, σ_max=0.072) are framework-specific; cite via companion paper or appendix. Mark internal | internal |
| `needed:S50-crossdomain` | SA-correlator identity-breaker | Internal S50 (atlas-10 #12). **This thread is superseded as a mechanism (§1 #12)** — if the SA-correlator stays in the rewrite, cite it as the companion-paper cross-domain result, NOT as a live rescue | internal |
| `needed:S51-ward` | Ward identity zero-mode transparency | Internal S51. The Goldstone Ward-identity argument is standard QFT — **cite a textbook** (Weinberg QFT Vol. II §19, or Watanabe-Murayama on NG counting) rather than the session script | partially externalizable |
| `needed:S51-mixing` | convex combination theorem | Internal S51 (atlas-10 #13). Cite via companion paper; mark internal | internal |

**Additional references the rewrite SHOULD add** (the paper currently under-cites the observational/forecast landscape):
- **CMB-S4 forecast**: CMB-S4 Collaboration, arXiv:2008.12619 (✓ fetched) — for the "CMB-S4 decisive" claim, gives the real σ(r); for σ(α_s) the canonical is the CMB-S4 Science Book (arXiv:1610.02743, NOT fetched — verify before citing).
- **ACT DR4 α_s anchor**: Aiola et al. 2020 (ACT DR4) — the framework's own canonical α_s pin (`alpha_s_canon_2020 = +0.0023±0.0063`). If the paper quotes a post-2018 α_s, this is the source.
- For the bit-exact rational identity, no external citation is needed — it is elementary arithmetic.

**Bibliography verdict**: 2 of 10 are clean external references already correctly formatted (just strip `needed:`); 2 more are standard textbook/historical citations (Liddle-Lyth, O-Z) that should be kept; 1 (Ward identity) should be re-pointed to a QFT textbook; the remaining 5 are **internal session artifacts that an external paper cannot cite** and must be either inlined (the trivial ones: S49 MC) or routed through the companion framework paper (the framework-specific ones: S47/S50/S51). The biggest bibliographic liability is the **5 internal-artifact citations** masquerading as references — a referee will flag every `Session N computation. Scripts: sN_*.py` entry.

---

## §6 Rewrite Plan (section-by-section, mechanically executable)

> Goal: preserve the exact algebra; replace the pre-resolution physics with the dual-observable/transport-degree picture; comply with SCALE-AND-CHANNEL-TAGGING; de-internalize the bibliography.

**Abstract** — Replace the "5.0–6.0σ tension conditional on a 10⁻⁵⁷ mapping" sentence-pair. New thrust: *exact identity (now bit-exact in ℚ at the framework tilt) → two scale-separated images → pivot consistent (+0.67σ), substrate a live ~34σ CMB-S4 falsifier → scale mapping is derived (transport degree +2, non-scalar), not assumed.* Drop "α_eff = 1.21 as identity-breaker" from the abstract (demote to a discussion remark). Keep the four-line-algebra and Ka-generalization claims verbatim.

**§1 Introduction** — Keep the "no α_s=f(n_s) in slow-roll" motivation (it's correct and well-framed). Replace the closing paragraph (lines 61–63) "factor 16, tension depends on scale mapping" with the dual-observable framing. Fix `needed:Planck2018`, `needed:Liddle-Lyth`.

**§2 Setup** — Keep the O-Z propagator derivation. ADD a paragraph (or footnote) clarifying the lattice is the **laboratory-IN projection of the spectral-triple substrate** (substrate-first compliance, atlas-09 Item 39). De-internalize `needed:S47-texture` (inline the stiffness numbers or route to companion paper). The `m_*=11.87 M_KK` "mass problem" subsection (§2.3 + §5.3) should be **cut or heavily demoted** — it is an artifact of the O-Z-fit-to-0.965 framing that the framework no longer uses (claim #13).

**§3 Derivation** — **Keep verbatim.** This is the crown jewel and is exactly right. ADD a remark recording the **bit-exact ℚ identity** at `n_s = 9561/10000` (α_s = −8587279/100000000 exactly; perfect-square 9561²). Fix the −0.0734 → −0.0736 if any 0.9625 evaluation is retained (better: evaluate at the framework's own 0.9590/0.9561 with the channel caveat).

**§4 Robustness (5 proofs)** — **Keep the five proofs**, but reframe the section preamble: these bound corrections *within the O-Z/Goldstone sector*, which is now identified as the **CMB-pivot leaf where α_s ≈ 0**. Retain the disclaimer "do not establish CMB ∈ O-Z sector" (lines 183, 443) — it is now load-bearing in the right way. De-internalize S49/S50/S51 citations per §5.

**§4 (was "Comparison to Observation") → rename "The Two Scale-Separated Running Observables"** — This is the **most-rewritten section**. Structure:
  - §4.1 The transport degree decides the channel. State `deg(T_{BZ→pivot}) = +2` NON-SCALAR. **Self-contained derivation required** (external audience): show the `w(L_max)·κ(k)` factorization fails (`factorization_holds=False`), i.e. the BZ→pivot transport is a genuine re-weighting, not a scalar unit conversion. This is the keystone — without it the paper has no right to claim the scale mapping is derived.
  - §4.2 Pivot image: α_s ≈ 0, **+0.67σ vs Planck −0.0045±0.0067 — CONSISTENT**.
  - §4.3 Substrate image: α_s = −0.08587279, FI-class (regulator-invariant), sign-walled negative, **frozen-now**. A **~34σ-reach CMB-S4(2030)/CMB-HD(2035) falsifier** at the matched substrate-sensitivity channel.
  - §4.4 The historical single-pivot −12σ reading was a **scale-mismatch artifact** (BZ-scale value vs CMB-pivot datum), now resolved. Cite atlas-09 Item 47 framing in spirit (the falsifier *relocated*, it did not vanish).
  - Replace Table 1: keep n_s row; α_s row becomes DUAL (pivot ≈0 / substrate −0.0859) with explicit (scale, channel) tags; **fix or drop the r=0 row** (framework r=0.033).

**§5 Discussion** — Cut §5.3 (mass problem, dissolved) and §5.4 (scale-mapping-as-open-problem, resolved). Keep §5.1 (regime of validity — correct), §5.7 (no prior art — soften per #17), §5.8 (slow-roll comparison — but channel-tag it per #18: the −2ε behavior is the *substrate-leaf* signature; the *pivot* prediction is ≈0). For §5.2 (SA-correlator): demote to "a distinct correlator that also breaks the identity at the BZ scale; superseded as the pivot-vs-substrate *mechanism* by the transport degree" — do NOT present α_eff=1.21 as the rescue of a tension that no longer exists.

**§6 Conclusion** — Rewrite to match the new thesis. Drop "5–6σ tension conditional on lattice ID." New close: the identity is exact (bit-exact in ℚ at the framework tilt); the two images are pivot-consistent and substrate-falsifiable; the scale mapping is derived (deg=+2). Keep the final sentence (Möbius-composition is framework-independent) — it's a good closer.

**References** — Per §5: strip `needed:` on the 2 clean externals; keep the 2 textbook/historical; re-point the Ward-identity to a QFT text; inline the trivial S49 MC; route the 5 framework-specific internals through the companion paper or appendices. Add CMB-S4 (2008.12619) and the CMB-S4 Science Book (verify 1610.02743 before citing).

---

## §7 Verdict

**RESTRUCTURE.**

Rationale: The exact-algebra core (§3, Prop 1 + Cor 1 + Remarks, and the five sector-bounds of §4) is **correct, survives intact, and is upgraded to a bit-exact rational identity** — it needs only a one-character arithmetic fix and a new remark. That is a REWRITE-IN-PLACE-grade core. But the paper's **physical spine — its central confrontation with data — is built on a question the framework has since answered**: the "load-bearing, underived scale mapping `K_pivot ∼ M_KK`" that the paper honestly flagged as "the decisive open problem" is now RESOLVED (transport degree +2, NON-SCALAR, STAGE-3-PERMANENT). The "5–6σ tension" is no longer the result; the result is a **dual-observable resolution** (pivot consistent at +0.67σ; substrate a live ~34σ CMB-S4 falsifier). This is not a value-tweak — it changes the *epistemic type* of the paper's headline from "conditional tension" to "resolved mechanism + future test," which forces a section-level rebuild of §4–§6 (and the abstract/intro framing), plus mandatory SCALE-AND-CHANNEL-TAGGING compliance and de-internalization of five non-citable session-artifact references. That is more than in-place editing and less than discard-and-replace: the skeleton (identity → robustness → confrontation → discussion) stays; the confrontation half is rebuilt around the post-S93 physics. Hence RESTRUCTURE, not REWRITE-IN-PLACE (the physics narrative is too stale for line-edits) and not RETIRE-AND-REPLACE (the mathematical core is genuinely durable and worth preserving). The restructured paper is **stronger and more honest** than the original — it presents a flagship result (an exact identity whose scale-separated images are simultaneously Planck-consistent and CMB-S4-falsifiable) with the scale ambiguity *resolved* rather than *flagged*.

---

### Appendix: artifacts consulted (for traceability)
- `canonical_constants.py` lines 511, 1239–1249, 1568–1582, 1957, 2269–2300, 2404–2405 (α_s/n_s pins + provenance)
- Knowledge MCP: `alpha_s_pivot_goldstone`, `alpha_s_substrate_distance_1`, `alpha_s_inflation_framework` (SUPERSEDED), `n_s_framework`, `n_s_FW_sqrt_cutoff`; gate `S93-W7-1-...DEG-TRANSPORT-BZ-PIVOT` (PASS)
- `sessions/framework/Atlas/atlas-09-retractions.md` Item 47 (alpha_s transport-degree, register-of-record), Items 36/39/43/48/49
- `sessions/framework/phonic-exflation-equation.md` §7.1 (Register B α_s row line 502; flat-table line 527), §7.2 (Row #3 line 556), the α_s "most-misread row" box (line 544)
- `sessions/framework/registry/cross-pillar-bridge-corpus.md §23` (transport-degree K-counter, SCALE-AND-CHANNEL-TAGGING)
- `sessions/permanent-results-registry.md` §VII.AN/AN-CORRIGENDUM/AO (lines 17123–17240), §VII.BA(h)/§VII.BG (lines 20164, 20800–20827)
- `.claude/rules/phononic-framing.md §"Scale-and-channel-tagging for running/tilt observables"` (standing rule)
- Sage QQ verification (bit-exact ℚ identity; −0.0734→−0.0736 arithmetic slip; a=2 reduction)
- arXiv (paper-search MCP, existence-verified): 1807.06209v4 (Planck 2018 VI); 2008.12619v1 (CMB-S4 forecast)
