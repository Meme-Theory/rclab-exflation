# Convergence Rollup — Yukawa hierarchy / Milnor moduli / modular flavor (CV-8)

**Synthesizer:** van-den-dungen-bridge-theorist.  **Date:** 2026-06-20.  **Digests netted:** inv-2, inv-9.

**Register-status verification (knowledge MCP, 2026-06-20).** Investigation/agent docs are point-in-time, not authoritative; every load-bearing claim below was re-checked against the live graph. Confirmed: **Trap 4 (Schur orthogonality)** PROVEN, `V_eff(B_i,B_j)=0 < 1e-55`, automatic from U(2) rep theory; **Rank-1 Yukawa** PROVEN (S62), `J_12/J_23=19.52` algebraically constant + rank-deficient; **Yukawa tree-level mass generation** PROVEN (S62, "tree-level Yukawa vanishes by PW orthogonality"); **§VII.BL Generation-Blindness Obstruction** STAGE-3-PERMANENT (S99 W3-1, Stage-2 PASS-AND audit `0f0c4f65`, `R_cross=1.019704`); **(W2) Homogeneity wall** PROVEN ("left-invariance ⇒ multiplicity-scalar; `ε_LX` MUST BREAK left-invariance on the multiplicity space"); **Corollary/design rule** PROVEN ("any mechanism discharging the hierarchy to its observed nonzero value MUST be an external non-LI fibre connection breaking W2 while PRESERVING reality"); **`S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN`** existence-PASS (value=0.0, scheme `NCG-INNER-FLUCT-EXTERNAL-NONLI`, L_max=12); **`S97-YUKAWA-FAMILY-DERIVE`** FAIL (`R_cross=1.0197`). This rollup is netted against THESE statuses, not against the S108/S109-plateau survey wording inv-1 was authored at.

---

## 1. The convergence (inv-1 framing)

**CV-8 as inv-1 stated it** (`investigation-1/_synthesis.md` §1, ranked the *strongest single convergence in the survey* — "3 agents, two converging on the SAME tool"):

> `baptista`: every "off-Jensen" result is a 5D U(2)-invariant projection; the framework's own Schur theorem says the **Yukawa hierarchy can ONLY live in the unexplored 23D complement** (the rank-1 "wall" tests for a hierarchy in the one region the theorem forbids it). Then **`string-theory` and `kaku` *independently* arrive at the same specific fix: modular flavor symmetry (Dedekind-η), already latent in the framework's threshold corrections** — closing the rank-1 Yukawa wall AND supplying a principled τ↔K e-fold map from one structure.

**The claim, decomposed into its two arms:**
- **Arm-G (geometric / Milnor-complement)**: the rank-1 wall is a *Schur-lemma artifact of staying on the U(2)-invariant slice*; the hierarchy lives in the 23D off-U(2) complement, where a transverse modulus should LIFT it. inv-1 prior leaned ~0.65 (plan dual_prior Track A) that the wall is a Schur artifact and a lift would appear off-surface.
- **Arm-M (modular flavor)**: a Dedekind-η modular form in (τ−τ_fold), weighted by the Casimir C₂(p,q), is the mechanism — and the SAME structure supplies the τ↔K e-fold map (a cross-bind to CV-3).

**Bridge B-3** (inv-1 §2 table): "Modular flavor symmetry — D_K(τ) near the fold as a Dedekind-η modular form," anchored to Feruglio 1706.08749, cost "1 structural workshop," proposed by string-theory + kaku independently. inv-1 §6 named it "the most beautiful 'mirror darkly' springboard."

**The prior in one line:** inv-1 expected CV-8 to be BOLSTERED — a lift would appear off-surface (Arm-G), and Arm-M (Dedekind-η) would be the validated tool that produces it.

---

## 2. Per-route ledger

| Investigation | Route / gate | Verdict | Digest verb | Magnitude |
|:--------------|:-------------|:--------|:------------|:----------|
| inv-2 (van-den-dungen) | **INV2-W1-1** off-U(2) Dirac+Yukawa, minimal su(2)-block split modulus δ (Arm-G, the *geometric* transverse test) | **FAIL** (sign=F/mag=F/regime=VALID) | **CHALLENGED** (closes the su(2)-split sub-corridor; STRENGTHENS the wall) | structural; lift indicator `|dY₁₂/dδ|₀=1.94e-15 ≪ eps_lift=1e-3` (9 OOM below floor); cubic null `d³S/dδ³₀=5.6e-10`; rigid shift 0.84086→0.85439; det-ratio=1.0 exact |
| inv-2 (van-den-dungen) | **INV2-W1-2** orbit-volume fiber measure `(det g_K)^{1/2}` → Weinberg cubic (the CV-2/CV-8 shared-root "Bridge-1=Bridge-2" test) | **FAIL** (sign=F/mag=F/regime=VALID) | **CLARIFIED** (accommodation tag now derivation-confirmed accidental) | exact; measure gives n=1 (−4τ), reproduces M_KK Jensen `sin²θ_W=0.58385339` bit-for-bit; cubic 0.23480 near-hit is accidental |
| inv-2 (van-den-dungen) | **INV2-W1-4** χ-as-Kasparov-shriek faithfulness (N3/N7 χ-rescue) | **LANDED** workshop (converged, no verdict line) | **MUDDLED → resolved-in-workshop** | structural; χ is NOT the M⁴×SU(3) shriek (category-mismatch + Connes-Karoubi zero-map `(0,0,0)∈ℤ³`); peripheral to CV-8 (it is the N3/N7 axis — see §6) |
| inv-9 (hawking) | **INV9-W1-1** MODULAR-FLAVOR-FORM — is gen-graded D_K(τ) a Dedekind-η modular form under any of 3 ε-maps? (Arm-M, the *modular* test, B-3 direct) | **FAIL** (sign=PASS/mag=FAIL) | **CHALLENGED** (corridor CLOSED on the substrate) | structural; min_R²=0.258 ≪ 0.95; R_direct=1.49 vs target O(1e5); grading_dev=1.437 (weights ~0, NOT Casimir-graded); τ-flat across [0.15,0.25] |
| inv-9 (hawking) | **INV9-W1-3** BCS-DIMENSIONAL-TRANSMUTATION (CV-2 facet; inter-sector coupling check) | **FAIL** (sign=PASS/mag=FAIL) | **CHALLENGED** (unit-fixity-yes / dynamics-no) | inter-sector Kosmann coupling = 0.0 EXACT (PA-2) — independent confirmation that generations do not mix under the deformation; Var_λ=0 EXACT geometry-fixity |
| inv-9 (hawking) | **CF-INV9-W1-MODULAR-WIDE** (routed, not run) | n/a (LOW-priority confirmatory CF) | (→COMPUTE-CF, near-closed) | corridor near-closed by W1-1; confirmatory only |

**Cross-gate (inv-2 wave headline):** "**Bridge-1 = Bridge-2**" — the survey's flagship bet that ONE off-U(2) geometric root (the orbit-volume measure) underlies BOTH the Yukawa hierarchy AND the Weinberg angle — **FALSIFIED on both arms** (INV2-W1-1 ∧ INV2-W1-2). The two oldest tensions are structurally INDEPENDENT through the orbit-volume measure.

---

## 3. NET framework verdict

**Dominant tag: CHALLENGED (corridor-closing), with a CLARIFIED facet (the hierarchy's home is RELOCATED and now register-PINNED).** CV-8 is **NOT BOLSTERED** — and forcing it would be dishonest. Both arms of the inv-1 convergence were attacked head-on and both failed; what survives is a sharper, register-confirmed picture of where the hierarchy lives.

**The honest reconciliation of the two digests (the load-bearing net).** inv-2's digest reports CV-8 "confirmed-and-narrowed: minimal su(2)-split sub-corridor closed; **B-3 modular-flavor untouched and still live**; C²-coset the surviving probe." That "still live" is TRUE *only within inv-2's scope* — inv-2 tested Arm-G (geometric su(2)-split) and did not touch Arm-M. **inv-9 tested Arm-M directly and CLOSED it on the substrate** (INV9-W1-1). Per the rubric's "latest synthesis wins" and the source-authority hierarchy (gate verdict > investigation digest narration), inv-9's closure of B-3 GOVERNS. The netted status of B-3 is **CLOSED on the substrate, not "still live."** inv-2's "untouched" was a statement about inv-2's coverage, not a register fact.

**Why Arm-M is closed — one structural reason, both digests + register agree.** The **(W2) homogeneity wall** (PROVEN) is decisive: a left-invariant Jensen TT-deformation `D_K(τ)` acts as a **multiplicity-scalar** at every τ — it multiplies all generations inside a Peter-Weyl (p,q) sector by the same factor. A Dedekind-η modular form in (τ−τ_fold) is still a function of the single scalar τ, so it inherits the multiplicity-scalar property and **cannot generate inter-generation structure**. inv-9 W1-1 made this empirical (matrix elements τ-INVARIANT, weights ~0 not Casimir-graded, R_direct=1.49 τ-flat across the full moduli window); inv-9 W1-3 confirmed it from the orthogonal BCS channel (inter-sector Kosmann coupling = 0.0 EXACT). This is the Kasparov-faithful reading: **the hierarchy is an off-fibre connection datum, not an internal-fibre deformation datum** — no amount of deforming the SU(3) fibre metric (which is what τ does) can split what Schur orthogonality protects inside the fibre.

**Where the hierarchy's home now stands — RELOCATED and PINNED.** The inv-1 prior ("any transverse direction lifts it; Dedekind-η is the tool") is replaced by a register-confirmed three-part localization:
1. **NOT on-U(2)** (Trap 4 / rank-1 wall, PROVEN — the original wall).
2. **NOT a τ-modulus** (Arm-M closed by inv-9 W1-1 via W2; NOT the su(2)-split off-U(2) modulus either, by inv-2 W1-1 — 9 OOM below the lift floor).
3. **IS an external non-left-invariant fibre connection** `ε_LX` (`A_nLI = A_homog + δA`) — this is the PROVEN **design-rule corollary** ("any mechanism discharging the hierarchy MUST be an external non-LI fibre connection breaking W2 while preserving reality") and it already carries an **existence-PASS** (`S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN`, scheme `NCG-INNER-FLUCT-EXTERNAL-NONLI`, L_max=12). The C²-coset direction (`J_C2=0.9330 M_KK`, 4 bonds) — inv-2's surviving CF-1 probe — is precisely the geometric direction `ε_LX` would live along.

**Facets (each cited):**
- **(CHALLENGED, structural)** Arm-G minimal su(2)-split: the rank-1 wall is PROVEN-genuine off-surface for the su(2) direction, not merely a Schur artifact of the U(2) slice (inv-2 W1-1; dual_prior reallocated 0.65 Track A → 0.90 Track B). The inv-1 §3 Contradiction-1 ("rank-1 wall vs hierarchy-REQUIRES-off-Jensen") **resolves in favor of the wall** for su(2) — and the "REQUIRES off-Jensen" theorem is honored, not refuted: the off-Jensen requirement is satisfied by the *external* `ε_LX` (off-fibre), not by an *internal* transverse Jensen modulus. **The generic question — does ANY internal transverse modulus lift it? — is the surviving open seam (§4).**
- **(CHALLENGED → CLOSED, structural)** Arm-M modular flavor: B-3 closed on the substrate (inv-9 W1-1). STRENGTHENS §VII.BL Generation-Blindness from τ_fold to the full window [0.15,0.25].
- **(CHALLENGED, structural)** "Bridge-1 = Bridge-2": falsified (inv-2 W1-1 ∧ W1-2) — the survey's flagship cross-convergence does not hold; Yukawa and Weinberg do not share the orbit-volume root.
- **(CLARIFIED)** the home is no longer "the unexplored 23D complement, somewhere" — it is pinned to the external non-LI connection class, with a PASS existence proof and one untested geometric probe (C²-coset).

**Net four-verb verdict: CHALLENGED-with-RELOCATION.** The inv-1 BOLSTERED expectation is refuted on both arms; the durable output is a corridor-closing + a register-confirmed relocation of the hierarchy's home from "Dedekind-η τ-modulus / generic off-U(2)" to "external non-LI fibre connection `ε_LX`." The framework is *stronger* for it (a flagship convergence eliminated, the surviving mechanism already existence-PROVEN) but CV-8 itself, as inv-1 framed it, did not survive.

---

## 4. Adversarial tensions (→ WORKSHOP, Q1)

Applying the `Investigating-Workshops.md` 3-question discriminator. A workshop requires TWO+ agents with competing FIRST-PRINCIPLES readings of a substrate-physics observable, unresolved, whose resolution is a structural verdict (not bookkeeping, not a queued compute).

**WS-1 (Q1, GENUINE) — Is the rank-1 wall genuinely off-Jensen for ALL internal transverse moduli, or only for the su(2)-split?** This is inv-2 §3 Contradiction-1 generalized — the one piece inv-2 explicitly left open ("the off-Jensen requirement may still be satisfied by a *different* modulus — that is now the open question, not a contradiction").
- **Reading A (baptista / geometric):** the rank-1 wall is still a *projection artifact* — it is genuine only along the su(2)-block and the orbit-volume measure (both tested), but the C²-coset direction (L3·I₄ split, the one that DIRECTLY touches the generation/fermion sector, `J_C2=0.9330`) *will* lift the per-generation degeneracy at first order, because that direction carries the inter-generation anisotropy the su(2)-block does not. CV-8 Arm-G survives.
- **Reading B (van-den-dungen / connes — NCG-axiomatic):** the wall is PROTECTED by Schur orthogonality + the W2 homogeneity structure for *every* left-invariant-on-the-base transverse deformation; the C²-coset is just another internal Jensen modulus and inherits the multiplicity-scalar property; only the EXTERNAL `ε_LX` (off-fibre, W2-breaking) can lift it — so the C²-coset compute will FAIL like su(2). CV-8 Arm-G is dead; the hierarchy is exclusively external.
- **Why this is Q1, not a compute-CF:** the readings invoke DIFFERENT machinery (Baptista's orbit-volume / O'Neill-tensor anisotropy on the U(2)-coset vs the NCG W2 multiplicity-scalar theorem) and they cannot both be right — they make OPPOSITE predictions for the SAME C²-coset gate. The workshop's job is to derive, from first principles, whether the C²-coset is "internal-Jensen-like" (Reading B) or "anisotropy-carrying-unlike-su(2)" (Reading A) BEFORE the compute, so the gate's outcome is interpreted correctly. The compute (CF-1, §5) is the discriminator the workshop pre-registers; the *adjudication of which reading the geometry supports* is the structural verdict. Agents: **baptista** (Riemannian-submersion / O'Neill-tensor side) ↔ **van-den-dungen / connes** (W2 multiplicity-scalar / Kasparov-shriek side).
- **Caveat (honest):** borderline Q1/Q3 — like inv-2's WS-A, it carries a definite PASS/FAIL gate. I route it →WORKSHOP because the two readings genuinely diverge on which machinery decides the SIGN of `dY₁₂/dδ` for the C²-coset, and the outcome flips the status of CV-8 Arm-G (workshop-output marker). A planner may legitimately fold it into CF-1 as a dual-prior-pre-registered compute — flagging the ambiguity, not forcing it.

**WS-2 (Q1, GENUINE, INHERITED from inv-2 — the M1 internal-shriek intertwiner).** Peripheral to the Yukawa-hierarchy core but it lives in this cluster's N3/N7 arm and inv-2 routed it here. Does χ (M₃(ℂ)→0) factor as the Kasparov shriek `π_!^{CP²}` of the internal submersion SU(3)→CP²?
- **Reading A (van-den-dungen):** χ is a *faithful internal fibre-integration* (Paper 02, 1405.5368 almost-commutative machinery as the type-bridge expressing "delete the M₃ summand of the fibre algebra" as a shriek) → discharges LBA-5, flips the χ-rescue to faithful, N7-(ii)→unconditional.
- **Reading B (connes):** the Q10 W4 Connes-Karoubi zero-map (`[φ_cd]=(0,0,0)∈ℤ³`, gate S93-W2-1) is positive evidence χ acts as *deletion* (a faithful shriek retains its fibre as a NON-trivial integrated class; a zero-image is deletion) → LBA-5 permanently undischargeable, "extrinsic restriction" PERMANENT.
- Both agents converged the expected outcome is FAIL (Reading B) but recorded it as a live, non-trivial question on which they could differ (different machinery — Kasparov shriek vs K-theory boundary). Construct-or-obstruct the intertwiner `χ = (type-bridge) ∘ π_!^{CP²}` to a machine-checkable commuting square. Agents: **van-den-dungen** ↔ **connes**.
- **Note:** this is the SAME tension inv-2 routed as its WS-A (mirror CF-INV2-W1-4-M1); it is NOT double-counted — it is carried into this rollup because the N3/N7 χ-faithfulness arm was part of inv-2's CV-8-adjacent charge. It belongs to the **N3/N7 cluster** for Stage-3 de-duplication (see §6); listed here so the cluster-net does not lose it.

**Workshop count surfaced: 2** (WS-1 the C²-coset wall-genuineness adjudication [genuinely new]; WS-2 the M1 intertwiner [inherited from inv-2, belongs to the N3/N7 cluster]). Arm-M (modular flavor) generates **0 workshops** — inv-9 closed it with a structural verdict; it is a result, not a seed.

---

## 5. Validated forward bridges (→ COMPUTE-CF)

EVOI-ordered. "Validated" is used in the rubric sense (CHALLENGED-with-constructive-next-step / a corridor with a register-confirmed surviving mechanism). Note the honest status of B-3 below.

**CF-1 — C²-coset anisotropy off-U(2) Yukawa test** (= inv-2 CF-INV2-W1-1-C2COSET; the discriminator WS-1 pre-registers).
1. **What:** build the C²-coset anisotropy transverse modulus (split L3·I₄, `J_C2=0.9330 M_KK`, the direction DIRECTLY touching the generation/fermion sector, transverse to U(2)); re-run the off-U(2) Dirac + Yukawa-overlap test on the d=2 generation multiplet. Does THIS direction lift the per-generation degeneracy at first order where the su(2)-split (INV2-W1-1) could not?
2. **Inputs:** `computations/investigation-2/inv2_w1_off_u2_dirac_yukawa.py` (the `deformed_*_split_metric` + `Y_ij(δ)` + fixed-δ=0-multiplet machinery); `dirac_spectrum.py`; `canonical_constants` (`tau_fold`, L3=e^τ, `J_C2`); INV2-W1-1's su(2)-split-null baseline.
3. **Gate:** `|dY₁₂/dδ|₀ > eps_lift=1e-3` AND rank(Y_ij) 1→≥2 for δ∈(0,0.20] (same pre-reg as INV2-W1-1). **Dual-prior pre-registration (per WS-1):** PASS → 0.9 mass to Reading A (geometric, CV-8 Arm-G survives, hierarchy lives in C²-coset); FAIL → 0.9 to Reading B (W2-protected, hierarchy exclusively external `ε_LX`).
4. **Effort:** 1 session (machinery in hand; swap the split block).
- **EVOI: HIGH.** The direct generation-sector modulus and the natural successor to INV2-W1-1 FAIL; the SOLE surviving probe of CV-8 Arm-G; discriminates "hierarchy lives off-U(2) somewhere internal" vs "protected in ALL internal transverse directions → exclusively external." Highest-leverage single compute on the off-U(2) hierarchy corridor.

**CF-2 — `ε_LX` between-generation hierarchy MAGNITUDE derivation** (the register-confirmed surviving route; promotes the S98-W3-1 existence-PASS toward a value).
1. **What:** the existence of an external non-LI `ε_LX` connection splitting generations is PROVEN (`S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN` PASS) and is the design-rule-MANDATED mechanism (PROVEN corollary). The open question is the HIERARCHY VALUE: does the PDG-pole-anchored `ε_LX` between-generation multiplicity deformation reproduce the observed `m_t : m_c : m_u` (and `J_12/J_23` lifted off 19.52-rank-1)? Run the `EPS-LX-BETWEEN-GENERATION-MULTIPLICITY-PDG-POLE` form at L_max=12 and read off the generated hierarchy ratios.
2. **Inputs:** the `S98-W3-1` `ε_LX` form (scheme `NCG-INNER-FLUCT-EXTERNAL-NONLI`; `A_nLI = A_homog + δA` posit from `session-97-plan-w3.md`); `S97-YUKAWA-FAMILY-DERIVE` FAIL baseline (`R_cross=1.0197`); s84 L12 cache; PDG masses; `J_C2`. (Note: `session-100a-plan-w4.md` already pre-registered this branch — check for a landed S100a verdict before re-running.)
3. **Gate:** generated `J_12/J_23` departs from 19.52 (rank lifted) AND the three-generation ratio matches PDG within a pre-registered band; INFO if rank lifts but magnitude off.
4. **Effort:** 1 session (S98-W3-1 machinery exists; this is the magnitude follow-on).
- **EVOI: HIGH.** This is the register's OWN surviving mechanism — the only route that the PROVEN design-rule corollary admits. A magnitude PASS would be the first DERIVED fermion hierarchy; it is independent of CF-1's geometric question (CF-1 asks whether an *internal* modulus can do it; CF-2 develops the *external* one that provably can exist). **Depends on:** S100a-W4 landing status (verify on disk first).

**B-3 (modular flavor / Dedekind-η) — NOT a validated forward bridge.** Honest disposition: **CLOSED on the substrate** (inv-9 W1-1), not carried as a compute-CF. The W2 homogeneity wall is the structural obstruction (a τ-modulus is multiplicity-scalar; a modular form in the single scalar τ inherits this and cannot generate inter-generation structure). The only residual is `CF-INV9-W1-MODULAR-WIDE` (wider-N/τ multi-map confirmatory check) — **LOW EVOI, confirmatory only**, the corridor is near-closed by W1-1; I do NOT promote it as a validated bridge. Recording it here so Stage-3 sees it adjacent and does not mistake B-3's inv-1 "strongest convergence" billing for a live route.

**Down-stream cross-link:** CF-1 and CF-2 are complementary, not redundant — CF-1 tests whether the hierarchy can live in an *internal* C²-coset Jensen modulus (WS-1 Reading A); CF-2 develops the *external* `ε_LX` connection (WS-1 Reading B, the register-MANDATED mechanism). If CF-1 FAILs (Reading B confirmed), CF-2 becomes the sole hierarchy route and its priority rises further.

---

## 6. Cross-links to other convergences

- **inv-2 ↔ inv-9 internal reconciliation (the headline cross-link):** the two digests' apparent disagreement on B-3 ("still live" vs "CLOSED") is resolved in favor of inv-9 (latest gate verdict on the modular arm governs; inv-2 never tested Arm-M). The two digests are otherwise CONCORDANT on the relocation: inv-2 closes the su(2)-split + names C²-coset as the surviving GEOMETRIC probe; inv-9 closes the MODULAR arm + names `ε_LX` (external non-LI) as the surviving mechanism. Netted: both point at the C²-coset / `ε_LX` external-connection corridor — the register-PINNED home.

- **N3 / N7 / χ-faithfulness / LBA-5 cluster (→ inv-12, inv-5):** inv-2's INV2-W1-4 (χ-as-shriek) + WS-2 (M1 intertwiner) belong to the spectral-triple-axioms cluster, NOT the Yukawa-hierarchy core. inv-12 (connes-ncg-theorist reviewer; seed authors lizzi/van-den-dungen/transit) attacks "is Tr f(D²) the right functional/signature" + CV-4 "SA ≠ free energy" + FI/RD ledger; inv-5 (lizzi reviewer; CV-4 CC a₄, two-effective-actions) touches the same axioms cluster. The N7-(i) d-singleton (§VII.O) and KO-dim=6 are upstream of both. **Stage-3 action:** route WS-2 + the HY-B1..B4 register-application obligation (atlas-04 N7 two-leg split, LBA-5 registration, atlas-08 Q10 scoping, §VII.W-3 verdict-name) to the N3/N7 cluster-net, NOT this Yukawa cluster. inv-2's §6 stranded-hygiene (HY-B1..B5) lands there.

- **CV-2 / M_KK keystone (→ inv-3, inv-6, inv-11):** inv-2 W1-2 REMOVES the Weinberg-cubic facet from the CV-2 "one root, several walls" bundle (orbit-volume gives n=1, not the cubic — the near-hit is accidental). inv-9 W1-3 confirms `Δ_BCS/M_KK` geometry-fixity (Var_λ=0 EXACT) + inter-sector Kosmann coupling=0.0 EXACT. **Stage-3 action:** the CV-2 net must NOT double-count the Weinberg arm as an open M_KK facet (corridor CLOSED), and should fold inv-9's inter-sector-decoupling=0 result as independent support for the generation-blindness picture (generations do not mix under the deformation — the same fact that closes Arm-M).

- **§VII.BL Generation-Blindness (the strengthened survivor):** both inv-2 (geometric su(2)-null) and inv-9 (modular-null + Kosmann=0) STRENGTHEN the STAGE-3-PERMANENT §VII.BL from τ_fold to the full moduli window [0.15,0.25] across BOTH the geometric and modular attack axes. This is the cluster's net BOLSTERING-of-a-survivor (recorded as CHALLENGED-strengthening per the rubric, not as an independent BOLSTER).

- **CV-9 compact-object (→ inv-4, inv-7, inv-13):** orthogonal to the Yukawa core; inv-2 W1-3 (static-soliton FAIL → dynamical-only) is netted in the compact-object cluster rollup, not here. Flagged only because inv-2 carried it; the off-U(2) compact-object soliton CF-2 (dynamical τ(t,r)) belongs to that cluster.

- **CV-3 a(t) / τ↔K e-fold map (the lost B-3 cross-bind):** inv-1 billed B-3 as supplying BOTH the Yukawa fix AND the τ↔K e-fold map "from one structure." With Arm-M closed (inv-9 W1-1), that cross-bind is SEVERED — the e-fold map does NOT come from a Dedekind-η flavor structure. **Stage-3 action:** the CV-3 net must not cite B-3 as a route to the τ↔t map; that map remains imported (CV-3's own #1-frontier status, inv-4/inv-7/inv-9 W3-2 LQC-import ruling).
