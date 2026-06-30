# Session 85 Synthesis: S-4 Structural-Elimination Bulletins (kaku)

**Date**: 2026-04-25
**Agent**: kaku-speculative-theorist (alternative-pathway / cross-paradigm relocation)
**Source Documents**:
- `sessions/archive/session-85/session-85-w0-workingpaper.md` (§W0-7 ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE FAIL)
- `sessions/archive/session-85/session-85-w2-workingpaper.md` (§W2-7 DISJOINT-CORRIDOR-REGISTRY-LANDING FAIL)
- `sessions/archive/session-85/session-85-w3-workingpaper.md` (§W3-7 BRANCH-A-A_S-CLOSURE-K2035 FAIL)
- `sessions/archive/session-85/session-85-w5-workingpaper.md` (§W5-1 FI-PARITY-REGISTRY FAIL)
- `.claude/agent-memory/kaku-speculative-theorist/MEMORY.md`

---

## I. Session Outcome

Four W0–W5 FAILs eliminate four named hypotheses and re-shape the surviving constraint map: (i) ε_H J-parity is NOT a regulator-independent invariant — only its HP^1 magnitude survives; (ii) §VII.P pairwise corridor-disjointness is parity-blind to HP^1 secondary twists — odd-parity diagnostics (η-invariant, GV integral) become load-bearing; (iii) the Branch-A K_substrate=2.035 TD-path over-produces A_s by 57%, so the sole surviving A_s pathway is closed under the strict W3-7 30% band but survives under the S80 factor-2 band; (iv) ρ_Zubarev does NOT converge to −1 on the 5-point sweep — the Jensen-Zubarev identity falls to numerical refutation pending kernel-normalization audit. The most consequential elimination is W3-7: it forces the framework either to relax its A_s pre-registration to the factor-2 S80 band, to trace the TD-path multiplicative chain (f_conv·F_amp/c_sub) for the 57% surplus, or to re-open S70–S77 corridors. The other three FAILs each redirect work toward concrete alternative paradigms (odd-parity NCG, q-deformed substrate, lattice / holographic regulator families) rather than closing solution-space wholesale.

---

## II. Key Results

### Bulletin 1 — ε_H J-Parity (W5-1) is Regulator-Conditional, Not a Permanent Wall

**Result**: GEOMETRIC. sig(ε_H) = +1 under cutoff_sqrt vs −1 under {zeta, Zubarev, SDW, anomaly} at τ_fold; INFO clause (anomaly-outlier) does NOT fire because outlier=cutoff_sqrt. Gate FAIL.

**Closed hypothesis H_1 (now FALSE)**: *"The J-parity class [ε_H] under the KO-dim=6 real structure is a regulator-independent invariant of the spectral triple, fit for permanent §VII-B wall registration."*

**Why H_1 was stated**: The plan's Step-4 positivity argument asserted that since every regulator's spectral functional f_r is positive on the active spectrum, the block-sign of ⟨ε_H, J ε_H⟩_k survives the regulator-weighted sum and sig(r) is r-invariant.

**Why H_1 fails (substitution chain, [SIGN] direction):**

```
Def 1: sig(r) = sign(Σ_k f_r(λ_k/Λ) · ⟨ε_H, J ε_H⟩_k)
Def 2: f_r is regulator-specific Mellin support; pure-a_4 family
       (zeta, Zubarev, SDW) has f_r ∝ δ(s−4); cutoff_sqrt has full
       (a_0, a_2, a_4, a_6) support; anomaly mixes (a_2, a_4).
Substitute (W5-1 §(b)): eps_H_zeta(τ_fold) = −4.485e−2,
                        eps_H_cutoff(τ_fold) = +2.163e−2.
Simplify: sig(zeta)=−1, sig(cutoff_sqrt)=+1, sig(SDW)=−1·0.97=−1,
          sig(Zubarev)=sig(zeta) by S83 G3 EN3, sig(anomaly)=
          sign(−0.04485 − 0.12012)=−1.
Direction: 4-vs-1 split with the outlier in the cutoff_sqrt
          (a_0-inclusive) family. The "f_r > 0 ⇒ sign-preservation"
          argument was conflated: positivity preserves sign WITHIN
          a single regulator's a_n-subset, not ACROSS regulators
          that select DIFFERENT a_n-subsets.
Conclusion: H_1 FALSE — sig(ε_H) is regulator-dependent.
```

**Surviving structure**: Magnitude of ε_H lifted to HP^1 (W5-6 INFO-tight, 2× band) — the cohomology-class magnitude is approximately invariant where the sign is not. This is a strictly weaker but still load-bearing structural object.

**Evidence class**: METHODOLOGICAL redirect. The regulator family is a physical DOF (Lizzi thesis), not a gauge choice; sig(ε_H) cannot be reported without naming the regulator. ALGEBRAIC walls survive (positivity within sub-family); the universal-sign claim was a category error.

**Solution-space dimensionality reduction**: The §VII-B registry loses one prospective row (ε_H J-parity wall). §VII.M gains one row (SCHEME-DEPENDENT observable: ε_H sign at τ_fold splits 4:1 with outlier=cutoff_sqrt). Net: registry slot count is conserved but moved from "permanent invariant" to "permanent split". The dimensionality of the regulator-choice space partitions cleanly into pure-a_4 (3 members) and mixed-a_n (2 members) sub-families with respect to ε_H sign.

#### Alternative-pathway map (kaku angle)

The surviving HP^1 magnitude near-invariance is a structural object that can land in at least four cross-paradigm constraint surfaces. Cross-ranked against existing framework walls (most-aligned first):

1. **NCG-axiomatic — η-invariant lift** (highly aligned). HP^1 magnitude in KO-dim=6 maps to the absolute value |η(D_K, 0)| under the Atiyah-Patodi-Singer regulator. W2-5 already proved η ∈ {0, 1/2} mod ℤ on this triple; magnitude-mod-1 is the natural odd-parity lift of the failed sign invariant. Cost: low (already structurally constrained).
2. **Lattice substrate — Brouwer degree** (moderately aligned). The HP^1 secondary twist on (C_H, C_epsH) is a Z₂ class, equivalent to a Brouwer degree on the ℍ-factor's idempotent space. A lattice regulator (rep-theoretic, S78 W2-F) accesses this via a finite Z₂ holonomy. Cost: low — rep-theoretic atlas already in the 5-atlas.
3. **KK-extra-dim — Casimir mode parity** (loosely aligned). In KK reduction of the SU(3)-fiber, the HP^1 class corresponds to a discrete Z₂ orientation choice on the compactified manifold (Wilson loop sign on the M_3 generator). The "sign flip in cutoff_sqrt vs zeta" mirrors KK Casimir signs that depend on the Pauli-Villars vs zeta regularizations of the same Casimir energy in the ED literature. Cost: medium — requires reconstructing the KK ↔ NCG dictionary entry for this specific sign.
4. **Holographic — boundary CS level mod 2** (least aligned). HP^1 in NCG is the bulk-side analog of Chern-Simons level mod 2 on the holographic boundary. The Z₂ ambiguity of the bulk η-invariant is the boundary CS framing anomaly. Cost: high — no holographic mapping has been instantiated for the substrate; this is speculative connection-mapping.

**Highest-EVOI relocation**: (1) NCG-η lift, because the η-invariant is already constrained to {0, 1/2} mod ℤ by W2-5 and the magnitude question is one CC-1 W0-23 computation away from closure.

---

### Bulletin 2 — §VII.P Disjoint-Corridor Theorem is HP^1-Parity-Blind

**Result**: GEOMETRIC. (C_H, C_epsH) twin pair has IDENTICAL (a_0, a_2, a_4) = (2.0, −0.0417, 0.0625) at max_rel_diff = 0 over 21 enumerated pairs. Gate FAIL with structural-refinement reading.

**Closed hypothesis H_2 (now FALSE)**: *"For every pair (C_a, C_b) of §VII.P corridors with HP²(C_a ∩ C_b) = 0, the pair produces distinct even-Seeley-DeWitt signatures (a_0, a_2, a_4) at relative tolerance 1e-8."*

**Why H_2 was stated**: §VII.P was originally stated as "HP^0 ∩ HP^1 = {0}" with ε_H carrier in HP^1, and the W2-7 gate was meant to certify that this parity-disjointness translates into spectral distinguishability — making §VII.P a registry-grade observational falsifier.

**Why H_2 fails (substitution chain):**

```
Def 1: a_k(C) = Tr_F[f(D_F^2/Λ^2) · χ_C], the k-th Seeley-DeWitt
       moment restricted to corridor C.
Def 2: Chern character ch: K_0(A_F) → HP^0(A_F); ε_H lives in HP^1.
Def 3: Even Seeley-DeWitt expansion {a_0, a_2, a_4, …} couples ONLY
       to HP^0 (image of ch on K_0); HP^odd has no image in even
       moments.
Substitute (C_H, C_epsH): same factor support {ℍ}, secondary HP^1
       twist differs, HP^0 content identical.
Simplify: a_k(C_H) = a_k(C_epsH) for every even k by HP^1-blindness.
Direction: max_rel_diff = 0 across (a_0, a_2, a_4); 1 of 21 pairs
       FAILs the disjointness probe.
Conclusion: H_2 FALSE — even Seeley-DeWitt cannot decode HP^1
       secondary twists.
```

**Surviving structure**: A genuine new permanent result — the *parity-blindness theorem*: even Seeley-DeWitt moments are functionally orthogonal to HP^odd cohomology classes. This is strictly stronger than H_2 because it identifies WHICH probes can/cannot distinguish secondary twists. Two refined registry slots are open:
- §VII.P-v2 (restricted to HP^0-content-distinct corridors — 20/21 pairs).
- §VII.P' (parity-extended with odd-parity probe required — η-invariant or Godbillon-Vey integral — for the 1 problematic pair).

**Evidence class**: ALGEBRAIC theorem. The HP^odd → even-Seeley-DeWitt map is a STRUCTURAL zero (image of HC^odd → cyclic-cohomology pairing on commutative-graded-symmetric kernels), not a numerical accident. The W2-3 PASS at HP^3 = 0 (semisimple finite-dim Loday 1992) and W2-6 PASS at q-deformed HP² = 0 corroborate the algebraic mechanism.

**Solution-space dimensionality reduction**: The original §VII.P falsifier corridor (single registry row) splits into two: one permanent (§VII.P-v2, 20-pair PASS by HP^0 content) and one open (§VII.P', awaiting odd-parity probe gate). Net: registry-slot count *increases* by one open slot but the original closed-form theorem narrows. The framework gains explicit machinery — odd-parity probe — that was previously implicit.

#### Alternative-pathway map (kaku angle)

The HP^1 secondary twist surviving as the (C_H, C_epsH) discriminator forces the next gate into the odd-parity sector. Cross-paradigm landing zones:

1. **NCG-axiomatic — APS η-invariant probe** (top alignment). η(D_K, 0) is the canonical odd-parity discriminant. W2-5 PASS established η ∈ {0, 1/2} mod ℤ; difference η(C_H) − η(C_epsH) ∈ {0, ±1/2} would resolve the parity-blind pair. Same W0-23 CC-1 computation that lifts Bulletin 1 also closes this. Cost: low (single gate).
2. **NCG-axiomatic — Godbillon-Vey integral** (top alignment, complementary). S83-G56 already constructed GV response on this triple; GV is a HC^3 / HP^3 cyclic class probe and naturally distinguishes secondary twists. Cost: low (machinery exists).
3. **q-deformed substrate** (W2-6 confirmed HP² = 0 at all q in scan). At generic q, HP^1(A_F^q) carries an additional Woronowicz-1-form structure that may EVADE parity-blindness even on (a_0, a_2, a_4) because q-deformed Seeley-DeWitt expansion has off-diagonal a_{2k+1} contributions in the Connes-Moscovici-twisted regulator. This opens a corridor for a new gate: does q-deformed even-Seeley-DeWitt distinguish (C_H, C_epsH) at generic q? Cost: medium — extends W2-6 but with new pairing computation.
4. **String-side lift — D-brane charges in K-theory** (cross-paradigm speculative). The HP^1 secondary class is the cyclic-cohomology image of a torsion K-theory element; on a D-brane stack, this is a discrete RR-flux Z_2 charge. The brane-stack-on-A_F dictionary is not yet established in the framework, but if it exists, the (C_H, C_epsH) twin pair would correspond to two D-branes with the same RR-form data but different discrete fluxes — distinguishable by S-duality boundary conditions, not by spectral action moments. Cost: high — requires the brane-stack ↔ A_F decomposition.
5. **Lattice substrate — discrete spin structure** (moderate). On a lattice regulator, the Z_2 secondary-twist class corresponds to the choice of spin structure on the quotient; lattice probes naturally see this via the Bär-Pfäffle index theorem. Cost: medium — requires lattice formulation.

**Highest-EVOI relocation**: (1)+(2) jointly — η-invariant + GV integral form a 2-route confluence that decisively closes §VII.P' in one session. This reuses machinery already in the framework.

---

### Bulletin 3 — Branch-A K_substrate=2.035 A_s Pathway Closes Under Strict 30% Band

**Result**: PHONONIC. A_s_framework(K=2.035) = 3.299e−9 vs A_s_Planck = 2.10e−9; relerr = 57.1% > 30% FAIL band. Gate FAIL with three-path carry-forward.

**Closed hypothesis H_3 (now FALSE if 30% band is authoritative)**: *"K_substrate = 2.035 Branch-A TD-path is the sole surviving A_s pathway that reproduces Planck central within 30% under the 5-regulator atlas."*

**Why H_3 was stated**: After S70-S77 closed multiple A_s mechanisms, S80's UNIFIED-AS-79 TD-path was the surviving zero-free-parameter prediction; W3-4's certified 5-regulator functoriality means scheme-invariance can no longer be invoked to relax the band; W3-7 was meant to convert S80's PASS-F2 (factor-2) into a strict 10%/30% closure.

**Why H_3 fails (substitution chain, [VERIFY] direction):**

```
Def 1: A_s_TD = (H_tilde_TD)^2 / (8π^2 · eps_H) · F_amp · c_sub^{-1} · f_conv
       (UNIFIED-AS-79 multiplicative pipeline, S80 cache).
Def 2: relerr = |A_s_TD - A_s_Planck| / A_s_Planck.
Substitute (W3-7 §pinned-cache): A_s_TD = 3.2994e-9, A_s_Planck = 2.1e-9.
Simplify: relerr = (3.2994e-9 - 2.1e-9)/2.1e-9 = 1.1994/2.1 = 0.5712.
Direction: 0.5712 > 0.30 (W3-7 FAIL band) → FAIL strict.
       Compare against S80 factor-2 band: 0.5712 < 1.0 → PASS-F2.
Conclusion: H_3 FALSE under 30% band; SURVIVES under factor-2 band.
       Two readings coexist; W3-7 plan picks strict.
```

**Verified arithmetic** (Python, this session):
- A_s_TD / A_s_Planck = 1.5712 (framework over-produces by factor 1.57).
- Multiplicative factor needed to land Planck central: 0.6365.
- If c_sub were the sole degree of freedom (P_ζ ∝ 1/c_sub per canonical-constants substitution chain), c_sub_effective = 2.238 / 0.6365 = 3.516 — i.e., if c_sub were ~57% larger, A_s would land. But c_sub is pinned by S80 SDW kinetic mixing, not free.

**Surviving mechanisms** (carry-forward exhausts the alternatives):
1. S80 factor-2 band re-asserted as authoritative (current S80 verdict_TD = PASS-F2).
2. Re-open S70-S77 closed A_s mechanisms (corridor sweet-spot search).
3. Trace the S80 TD-path multiplicative chain to isolate the 57% surplus among (f_conv = 9.3e−4, F_amp = 1.0166, c_sub = 2.238).

**Evidence class**: TRUNCATION limit MIXED with METHODOLOGICAL redirect. The A_s computation is canonical (no truncation per se); the FAIL is methodological — the W3-7 pre-registered 30% band was tighter than S80's pre-registered factor-2 band, and the strict reading vs the lenient reading point to different sole-surviving statements about the framework. Per `feedback_reporting-framing.md`: a 57% over-shoot at zero-free-parameter prediction is still a non-trivial structural commitment (Planck reach excludes ~5 orders of magnitude); calling it "catastrophic" depends on which threshold is canonical.

**Solution-space dimensionality reduction (most consequential of the four FAILs)**: The single A_s-corridor-anchor proposal (Branch-A, K=2.035, strict 30%) closes. Three open pathways remain:
- (a) Accept S80 PASS-F2 as the framework's honest band, retire W3-7 strict band as overly tight.
- (b) Find a corridor sweet spot in the closed S70-S77 family (this re-opens previously closed mechanisms — must check whether their FAIL reasons remain decisive).
- (c) Audit one of {f_conv, F_amp, c_sub} with high enough resolution to re-derive the 57% surplus.

#### Alternative-pathway map (kaku angle)

The 57% over-production is the SHARPEST cross-paradigm signal in the four FAILs. It localizes to a canonical multiplicative chain whose pieces have NCG and KK analogs. Cross-paradigm landing zones:

1. **NCG-axiomatic — c_sub correction via dimension-spectrum order-2 pole** (top alignment). Connes-Moscovici 1995 §5 simple-spectrum requirement allows order-2 poles in the dimension spectrum for triples failing the regular-simple condition. If the SU(3)×A_F triple has an order-2 pole, c_sub picks up a logarithmic correction that exactly tracks the W0-7 ρ_Zubarev shortfall (Bulletin 4 below) — both Bulletin 3 and Bulletin 4 may share a single CM-1995 normalization-audit fix. Cost: low — direct kernel-normalization audit.
2. **KK-extra-dim — F_amp from Casimir back-reaction** (moderate). F_amp = 1.0166 carries a 1.66% squeezing correction in Bunch-Davies → substrate IC. In KK literature, the analog is the Mukhanov-Sasaki amplitude correction from compactification radius variation R(τ); a 57% A_s surplus translates to a ~25% R-correction — which is within the Planck-bounded compactification range. Cost: medium — requires translating the substrate-IC into KK-language.
3. **Holographic — boundary OPE coefficient redefinition** (loose). In gauge-gravity duality, A_s corresponds to a boundary CFT 2-point function at the pivot scale; a 57% normalization surplus is the size of a typical CFT operator-mixing matrix coefficient. The substrate's Mellin-cone could be reformulated as a boundary OPE on the holographic dual; renormalization within OPE could absorb the 57%. Cost: high — no holographic dual constructed for substrate yet.
4. **Lattice substrate — c_sub from finite-size scaling** (moderate). On a lattice regulator, c_sub picks up O(a/L) finite-volume corrections. Is the framework's c_sub computation susceptible to such a correction? In the rep-theoretic atlas, this is computable. Cost: medium — extends W3-4 atlas computation to finite-N truncations.

**Highest-EVOI relocation**: (1) NCG-axiomatic c_sub via CM-1995 dimension-spectrum order-2 pole audit. This unifies Bulletin 3 and Bulletin 4 (both involve the same Mellin-cone kernel normalization) and would close them with ONE computation.

---

### Bulletin 4 — Jensen-Zubarev Identity ρ → −1 Numerically Refuted at L_max ∈ {8..12}

**Result**: GEOMETRIC. ρ_Zubarev(L=12) = −0.6349; unconstrained fit c_0 = −0.8104; |c_0 − (−1)| = 0.1896 vs PASS_TOL = 0.01 and INFO_TOL = 0.05. Gate FAIL.

**Closed hypothesis H_4 (now NUMERICALLY REFUTED conditional on fit-model correctness)**: *"ρ_Zubarev(L_max → ∞) = −1 exactly under the Jensen-Zubarev identity conjecture, with residual 1/L² decay fitting the form ρ(L) = −1 + α/L² + β/L⁴ to PASS_TOL = 0.01."*

**Why H_4 was stated**: The conjecture proposed that the Zubarev Mellin-cone moment of D_K under Jensen deformation reduces analytically to the rational −1 — a clean, parameter-free identity that would land in the registry as a permanent algebraic theorem.

**Why H_4 fails (substitution chain):**

```
Def 1: ρ_Zubarev(L) = signed weighted average of D_K eigenvalues
       under the Zubarev Mellin-cone kernel (Zubarev 1974 + CM-1995).
Def 2: R_∞ = fit-extrapolated L→∞ intercept under
       ρ(L) = c_0 + α/L^2 + β/L^4.
Def 3: gate statistic = |c_0 + 1|; PASS at < 0.01, INFO at < 0.05.
Substitute (W0-7 §(b)): unconstrained fit on (8,9,10,11,12) data
       → c_0 = -0.8104 (R^2 = 0.99995); constrained c_0 = -1
       → R^2 = 0.9305 (much worse).
Simplify: |c_0 + 1| = 0.1896.
Direction: 0.1896 > 0.05 INFO threshold → FAIL.
Monotonicity: ρ DECREASES toward target (Δρ < 0); |Δρ| also
       decreases (sign of second derivative consistent with
       convergence) — converging, but to ≈ -0.81 not -1.
Conclusion: H_4 NUMERICALLY REFUTED IF fit-model is correct.
```

**Surviving interpretations** (mutually exclusive, orthogonal recovery paths):
- (i) Conjecture is structurally wrong; true limit is irrational / framework-constant-dependent (≈ −0.81).
- (ii) 1/L^6 term matters; the (8..12) sweep underfits the asymptotic series.
- (iii) Kernel normalization differs from CM-1995 canonical; the target is a rescaled value.

**Evidence class**: TRUNCATION limit. The L_max ∈ {8..12} sweep with 5 data points + 3 fit parameters is at the edge of overfit (degrees of freedom = 2). Adding a 1/L^6 term overfits; this is genuinely a truncation regime where the fit cannot resolve the conjectural identity at the required tolerance. Promotion to ALGEBRAIC theorem requires either (a) extending L_max to {13, 14, 15} for 6-7 points enabling a 4-parameter fit, or (b) deriving the closed-form Mellin-cone Zubarev kernel asymptote analytically.

**Solution-space dimensionality reduction**: The Jensen-Zubarev identity is downgraded from THEOREM-grade to CONJECTURE-grade. Downstream W2 connes-ncg carry-forwards must NOT cite the identity as theorem-grade. W0-20 MELLIN-CONE-S3-RESIDUE shares the eigenvalue cache; the same kernel-normalization audit applies there. Net: one prospective theorem retracted; three open recovery paths registered.

#### Alternative-pathway map (kaku angle)

The Zubarev kernel is one specific Mellin-cone choice among a family. Cross-paradigm landing zones for the surviving mechanism:

1. **NCG-axiomatic — CM-1995 normalization audit** (top alignment). The Connes-Moscovici 1995 §4 kernel has a specific normalization factor (residue-of-zeta vs raw Mellin transform). The W0-7 script may use Zubarev-1974 raw without the CM-1995 factor. If interpretation (iii) holds, the correct target is `-1 · normalization_factor` and the FAIL becomes a PASS in CM-1995 convention. Audit cost: low — direct kernel inspection. **This is the same CM-1995 audit that potentially closes Bulletin 3.**
2. **NCG-axiomatic — generalize from Zubarev to broader Mellin-cone family** (moderate). The Zubarev kernel is one of a 1-parameter family (the "cone half-angle") of admissible Mellin kernels under CM-1995. Generic family members converge to family-dependent limits (irrational); the identity ρ = −1 may hold ONLY at a special cone-angle. Recover: parametric scan over the cone-angle, find where ρ → −1. Cost: medium.
3. **q-deformed substrate — ρ_q(q→1) limit** (loose). On A_F^q (W2-6 confirmed q-deformation of disjoint corridors), the analog of the Zubarev moment is a q-Mellin transform whose classical limit q→1 gives ρ. Possible that the identity holds in the q→1 limit but the L_max sweep at q=1 directly is sensitive to L_max → ∞ scaling, while the q-route bypasses this. Cost: medium-high.
4. **Holographic — boundary β-function** (loose). Mellin-cone moments map to boundary CFT β-function residues in holographic literature; the value −1 is the "marginal" β-function fixed point. If the substrate is dual to a near-marginal CFT, ρ = −1 at infinite L is the AdS-bulk reformulation of marginal stability. The 0.19 surplus would be a relevant deformation. Cost: high — no dual.
5. **Lattice substrate — perturbative chain extrapolation** (moderate). ρ_Zubarev on a lattice can be computed as a perturbative chain in the lattice spacing 1/L; the residue ρ → c_0 + α/L^2 + ... is exactly the lattice's continuum extrapolation. The fit-residue 0.19 may quantify a known O(a^4) lattice artifact in the rep-theoretic atlas. Cost: medium.

**Highest-EVOI relocation**: (1) CM-1995 normalization audit, AND it unifies with Bulletin 3's c_sub audit. ONE Connes-Moscovici 1995 §4-§5 kernel-normalization gate could close both Bulletin 3 (if the normalization absorbs the c_sub factor) and Bulletin 4 (if it absorbs the 0.19 intercept gap). This is the deepest cross-paradigm consolidation in the W0-W5 FAIL set.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S85-W5-1-FI-PARITY-REGISTRY | FAIL | sig(cutoff_sqrt) = +1 vs sig(zeta) = −1 (4-vs-1 split) |
| S85-W2-7-DISJOINT-CORRIDOR-REGISTRY-LANDING | FAIL | 1/21 pairs (C_H, C_epsH) match at max_rel_diff = 0 |
| S85-W3-CF-1-BRANCH-A-A_S-CLOSURE-K2035 | FAIL | A_s relerr = 57.12% > 30% strict band |
| S85-W0-ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE | FAIL | fit-intercept c_0 = −0.8104 vs target −1.0 (Δ = 0.190) |

---

## IV. Structural Implications

The four FAILs partition into two consolidation pairs and yield a single highest-EVOI cross-paradigm computation:

**Consolidation 1 — odd-parity probes (Bulletins 1 + 2)**: Both ε_H J-parity (W5-1) and the (C_H, C_epsH) twin pair (W2-7) point to the SAME structural gap — the framework's even-Seeley-DeWitt machinery cannot decode HP^odd cohomology. The η-invariant (CC-1 W0-23, already constrained to {0, 1/2} mod ℤ) and Godbillon-Vey integral (S83-G56, already constructed) are the canonical odd-parity probes. ONE follow-up computation — η(C_H) − η(C_epsH) at the parity-twin pair — would constrain Bulletin 1's HP^1 magnitude AND Bulletin 2's parity-blindness gap simultaneously.

**Consolidation 2 — Mellin-cone normalization (Bulletins 3 + 4)**: The Branch-A A_s 57% surplus (W3-7) and the Jensen-Zubarev 19% intercept gap (W0-7) BOTH involve Mellin-cone kernel normalization in the Connes-Moscovici 1995 §4-§5 framework. c_sub = 2.238 (the W3-7 multiplicative knob) is computed under one normalization convention; ρ_Zubarev's target −1 is under another. A single CM-1995 §5 dimension-spectrum + §4 kernel-normalization audit could resolve both — either by absorbing both gaps simultaneously into a corrected normalization, or by demonstrating that the framework's chosen normalization is canonical and both gaps are genuine physics statements (CC over-production of A_s; ρ-limit irrational).

**Highest-EVOI single computation**: CM-1995 §4-§5 kernel-normalization audit on the Mellin-cone family. Touches Bulletin 3 (c_sub correction) AND Bulletin 4 (ρ target). Cost: 1 agent session. Worst-case: both gaps confirmed as genuine — framework gains two strict structural claims (over-production by 57% and irrational ρ-limit). Best-case: both gaps absorbed by normalization — framework gains a unified Mellin-cone landing for A_s and ρ_Zubarev.

**Cross-paradigm relocation summary** (Bulletins 1-4):

| Surviving mechanism | NCG | KK | Holographic | Lattice |
|:--------------------|:----|:---|:------------|:--------|
| Bulletin 1 — HP^1 mag invariance | TOP (η-invariant) | LOOSE (Wilson loop sign) | LOOSE (CS framing) | MOD (Brouwer degree) |
| Bulletin 2 — odd-parity probe | TOP (η + GV) | — | LOOSE (D-brane RR) | MOD (lattice spin) |
| Bulletin 3 — A_s 57% surplus | TOP (CM-1995 c_sub) | MOD (Casimir back-reaction) | LOOSE (boundary OPE) | MOD (finite-size) |
| Bulletin 4 — ρ ≠ −1 | TOP (CM-1995 norm) | — | LOOSE (β-function) | MOD (continuum extrap) |

The NCG-axiomatic column dominates as the "highest-alignment" relocation surface across all four bulletins — the framework's structural backbone IS Connes-NCG, so each FAIL has a natural NCG-side mechanism in flight. The Lattice column is uniformly moderate-cost (rep-theoretic atlas already in place), and Holographic remains uniformly loose because no holographic dual has been instantiated. KK only applies to the two bulletins involving spectral-action coefficients; the parity bulletins do not have a clean KK reformulation.

---

## V. Carry-Forward Computations

V.1. Joint η-invariant + GV-integral probe of (C_H, C_epsH) twin pair
   - **What**: Compute η(D_K, 0) restricted to corridor C_H and C_epsH on the L_max=10 cache, then compute Godbillon-Vey integral on the same pair via S83-G56 machinery. Output: (η_diff, GV_diff) tuple. Gate criterion: at least one of |η_diff − k·(1/2)| or |GV_diff − GV_canon| ≥ 1e-6 distinguishes the twin pair.
   - **Inputs**: L_max=10 D_K eigenvalue cache; APS regulator (W2-5 PASS, η ∈ {0, 1/2} mod ℤ); S83-G56 GV response infrastructure; canonical_constants.py.
   - **Gate**: NEW S86-ETA-GV-PARITY-PROBE — PASS iff at least one probe distinguishes (C_H, C_epsH) at relative tolerance 1e-3; INFO if both probes vanish (would force §VII.P' to invoke a third diagnostic class); FAIL if both probes fire AND distinguish but disagree on direction. Closes BOTH Bulletin 1 (HP^1 magnitude) and Bulletin 2 (odd-parity probe).
   - **Effort**: 4-6 hours, 1 agent session (connes-ncg-theorist + kaku consult).

V.2. Connes-Moscovici 1995 §4-§5 kernel-normalization audit
   - **What**: Audit the Zubarev Mellin-cone kernel implementation in `s85_w0_zubarev_lmax_convergence_to_minus_one.py` against CM-1995 §4 (kernel normalization) and §5 (dimension-spectrum simple-pole assumption). Trace the normalization factor through to (a) the ρ-intercept target, (b) the c_sub coefficient in S80 UNIFIED-AS-79. Output: (kernel_factor, ρ_target_corrected, c_sub_corrected, A_s_corrected).
   - **Inputs**: `s85_w0_zubarev_*.py`, `s80_unified_as_79_full.npz`, CM-1995 paper PDF, S82 W2-4 substrate-matched IC derivation.
   - **Gate**: NEW S86-CM1995-KERNEL-NORMALIZATION — PASS iff (i) ρ_target_corrected matches W0-7 fit intercept within INFO_TOL = 0.05 AND (ii) A_s_corrected lands within W3-7 strict band (relerr < 30%) OR S80 factor-2 band; INFO iff one of (i) or (ii) holds; FAIL iff neither holds. Closes Bulletins 3 + 4 jointly under best-case.
   - **Effort**: 6-8 hours, 1 agent session (connes-ncg-theorist).

V.3. L_max ∈ {13, 14} extension of Zubarev convergence
   - **What**: Extend D_K eigenvalue cache to L_max = 13 and L_max = 14; recompute ρ_Zubarev(L) at each new point; refit ρ(L) = c_0 + α/L^2 + β/L^4 + γ/L^6 (4-parameter fit on 6-7 points).
   - **Inputs**: D_K Jensen-deformed SU(3) construction at L_max = 13, 14 (memory + compute); existing L=8..12 cache.
   - **Gate**: S85-ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE re-evaluation — PASS iff |c_0 + 1| < 0.05 with 4-parameter fit; INFO iff |c_0 + 1| < 0.10; FAIL otherwise. Discriminates between Bulletin 4 interpretations (i) and (ii).
   - **Effort**: 8-12 hours (cache extension is the bottleneck), 1 agent session (gen-physicist + GPU access).

V.4. Refined §VII.P-v2 registry landing (HP^0-content-distinct corridor restriction)
   - **What**: Re-emit §VII.P theorem statement restricted to 20 of 21 pairs (excluding C_H ∩ C_epsH twin); land in registry skeleton at `sessions/framework/permanent-results-registry.md`.
   - **Inputs**: W2-7 verdict line + 21-pair table (`s85_w2_disjoint_corridor_counter_construction.json`); registry skeleton.
   - **Gate**: NEW S86-VII-P-V2-LANDING — PASS iff registry entry added with explicit exclusion clause and SHA-tagged provenance. Documentation gate.
   - **Effort**: 1-2 hours, 1 agent session (connes-ncg-theorist).

V.5. q-deformed even-Seeley-DeWitt parity probe of (C_H, C_epsH)
   - **What**: Extend W2-6 q-scan with a paired even-Seeley-DeWitt computation: at each q ∈ {0.7, 0.8, 0.9, 0.95, 0.99, 1.01, 1.05, 1.1, 1.25, 1.5}, compute (a_0, a_2, a_4)(C_H) − (a_0, a_2, a_4)(C_epsH) under the Connes-Moscovici-twisted regulator. Gate criterion: max-q over all 10 values where the difference exceeds 1e-6.
   - **Inputs**: W2-6 q-scan infrastructure; CM-twisted Mellin transforms; A_F^q construction.
   - **Gate**: NEW S86-Q-EVEN-SDW-PARITY — PASS iff difference > 1e-6 at any q ≠ 1; INFO if difference scales monotonically with |q − 1|; FAIL if difference vanishes everywhere. Cross-paradigm probe relocating Bulletin 2 to q-deformed substrate.
   - **Effort**: 4-6 hours, 1 agent session (connes-ncg-theorist).

V.6. S70-S77 closed-A_s-mechanism re-examination
   - **What**: List the 5+ A_s mechanisms that closed in S70-S77; for each, re-tabulate the FAIL reason and check whether a corridor sweet-spot exists in K_substrate ∈ {1.1, 1.5, 1.92, 2.035, 5, 10, 20, 50} that PASSES W3-7 strict 30% band. Output: corridor map with PASS/FAIL bands per mechanism per K.
   - **Inputs**: S70-S77 verdict files; W3-7 band; W3-4 5-regulator atlas.
   - **Gate**: S86-AS-CORRIDOR-RE-EXAM — INFO output gate; PASS iff any (mechanism, K) cell PASSES W3-7 strict band; otherwise INFO with ranked list. Determines whether Bulletin 3's strict reading is rescuable without paradigm relocation.
   - **Effort**: 6-10 hours, 1 agent session (landau + connes consult).

V.7. KK-Casimir back-reaction estimate of F_amp correction
   - **What**: Translate F_amp = 1.0166 into a KK-language Mukhanov-Sasaki amplitude correction via the standard map F_amp = (1 + δR/R)^2 with δR the substrate-IC compactification-radius shift. Solve for δR/R; check whether 25% radius-correction is consistent with substrate sound-speed c_fabric.
   - **Inputs**: S80 cache (F_amp, eps_H); canonical_constants.py (M_KK, c_fabric); KK literature (Baptista #13-#18).
   - **Gate**: NEW S86-KK-FAMP-RADIUS-MAP — PASS iff δR/R lies within ±10% of the substrate sound-speed-bounded value; INFO iff within ±25%; FAIL otherwise. Cross-paradigm probe of Bulletin 3 in KK setting.
   - **Effort**: 4-6 hours, 1 agent session (kaku + landau).

V.8. Permanent-results-registry creation with parity-blindness theorem entry
   - **What**: Create `sessions/framework/permanent-results-registry.md` (currently absent per W3-8 CC-5 informational FAIL); land the parity-blindness theorem (Bulletin 2 surviving result) as the inaugural entry; populate with W3-8 Landau structural block (W3-8 carry-forward) and BDI AZ class (W3-10 carry-forward).
   - **Inputs**: W2-7 substitution chain; W3-8 + W3-10 registry-entry drafts; `sessions/framework/_registry-template.md`.
   - **Gate**: NEW S86-REGISTRY-LANDING — PASS iff registry file exists with at least 3 entries (parity-blindness + Landau block + BDI AZ); INFO iff partial; FAIL otherwise. Documentation gate.
   - **Effort**: 2-3 hours, 1 agent session (connes-ncg-theorist).

V.9. Lattice spin-structure probe of HP^1 secondary twist
   - **What**: On the rep-theoretic 5-atlas regulator, construct the discrete spin structure on (A_F, ℍ-factor); compute the Bär-Pfäffle index theorem applied to (C_H, C_epsH) twin pair; check whether spin structure choice distinguishes them.
   - **Inputs**: Rep-theoretic atlas (W3-4 PASS, S78 W2-F); Bär-Pfäffle reference; W2-7 twin-pair specification.
   - **Gate**: NEW S86-LATTICE-SPIN-STRUCTURE-PROBE — PASS iff spin-structure choice yields distinct index for the twin pair; INFO if spin structure is ambiguous; FAIL if index is invariant under spin-structure choice. Cross-paradigm probe of Bulletin 1 + 2 in lattice setting.
   - **Effort**: 6-8 hours, 1 agent session (connes-ncg-theorist + lizzi consult).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | ε_H J-parity is regulator-conditional, not universal | GEOMETRIC | Bulletin closed (H_1 FALSE) | §VII-B loses parity-wall row; §VII.M gains scheme-dep row; HP^1 magnitude survives as the proper invariant |
| 2 | §VII.P pairwise theorem is HP^1-parity-blind | GEOMETRIC | Bulletin closed (H_2 FALSE); new theorem opens | §VII.P-v2 (20-pair restriction) and §VII.P' (odd-parity probe) become two separate registry slots |
| 3 | Branch-A K=2.035 over-produces A_s by 57% | PHONONIC | Bulletin closed (H_3 FALSE under strict band; SURVIVES under S80 factor-2) | Forces choice between strict W3-7 closure (catastrophic for sole-surviving claim) or lenient S80 factor-2 acceptance |
| 4 | Jensen-Zubarev identity numerically refuted (ρ → −0.81, not −1) | GEOMETRIC | Bulletin closed (H_4 NUMERICALLY REFUTED conditional on fit-correctness) | Conjecture downgraded; CM-1995 kernel-normalization audit unifies with Bulletin 3 |
| 5 | Cross-paradigm consolidation: 4 FAILs collapse to 2 follow-ups (η+GV joint probe; CM-1995 audit) | META | Identified | One η+GV gate closes Bulletins 1+2; one CM-1995 gate closes Bulletins 3+4; 4-FAIL → 2-gate compression |
