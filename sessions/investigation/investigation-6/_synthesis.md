# investigation-6 — Distillation Digest

**Reviewer:** kaku-speculative-theorist (neutral; not an inv-6 author — seed authors were dirac, kaluza-klein, feynman).  **Date:** 2026-06-20.
**Topic:** The KK scale-bracket (M_KK), the framework's own quantum-loop gravity sector, baryogenesis η_B, and the Parker-Bogoliubov A_s route — read back against CV-2 (M_KK 6.79× bracket / B-2 dimensional transmutation), the quantum-loop side of the gravity sector, η_B (B-6), and CV-1 (one of six A_s routes).
**inv-1 convergences/bridges executed:** CV-2 (M_KK bracket), CV-1 (A_s, Parker-Bogoliubov leg), B-2 (dimensional transmutation), B-6 (baryogenesis bottleneck); plus the gravity-sector quantum-loop face (Γ[τ] one-loop, graviton finiteness, d_s, emergent Lorentz).
**Gate tally:** 14 gates — **2 PASS / 6 FAIL / 5 INFO + 1 workshop-LANDED** (the 6/5 split counts W4-1 separately as a workshop). FAIL/INFO are constraint-map results, not failures (`math-scripts.md §"All Results Are Good Results"`). Artifacts verified on disk: all 13 compute gates carry dual-SHA verdict lines in `computations/investigation-6/inv6_gate_verdicts.txt` (W1-4 carries a clean Option-A supersession: prior `9fa1fcf6` superseded by canonical `de92408b`); the W4 workshop closed by artifact-existence (`workshops/m-kk-determination-route-reconciliation.md`, all 6 must_contain markers present). **No missing artifacts.**

**Substrate-first reading frame** (applied to every verb tag): the substrate IS the spectral triple `(A_K, H_K, D_K(τ))`; explanation flows `D_K eigenvalues → spectral moments (a₀/a₂/a₄/a₆, ζ'_D(0,τ), heat-trace P(σ)) → emergent physics → measurement`. Several inv-6 FAILs are *substrate-confirmations in disguise*: the FAIL falsifies a container-thinking hypothesis (metric inflation; finite-QG-by-summing-geometries) while the substrate mechanism (spectral complexification; Wilsonian-EFT-with-cutoff) survives. These are tagged CHALLENGED-corridor-closed, NOT MUDDLED — the constraint map sharpens.

---

## 1. Per-gate ledger

| Gate | Verdict | Substrate reading (class) | Framework claim touched (cite) | Verb | Magnitude |
|:-----|:--------|:--------------------------|:-------------------------------|:-----|:----------|
| INV6-W1-1 M-KK-BRACKET-PROPAGATE | INFO | GEOMETRIC — M_KK two-route bracket on a₀/a₂ magnitude bands | CV-2 / B-2 6.79× bracket; AMPLITUDE-NORM-66 A_s gap re-scope | CLARIFIED | ratio=6.7868 (0.832 dec) EXACT; a₂-band 1.663 OOM, a₀-band 3.327 OOM; A_s gap ⊂ a₀-band, ⊄ a₂-band |
| INV6-W1-2 KK-CASIMIR-VOLUME | INFO | PHONONIC→GEOMETRIC — graded Casimir along breathing/volume mode | atlas-04 G6 (det g=1 ASSUMED); §VII.BS rank-1 (STAGE-3-PERMANENT) | BOLSTERED (§VII.BS) / CHALLENGED-closed (3rd M_KK route) | ζ_graded(−½)=−4.30e7; 0 interior stationary points; monotone EXACT (conformal-power identity) |
| INV6-W1-3 KK-THRESHOLD-RUNNING | FAIL | PARTICLE — 3-coupling KK-tower running M_KK→m_Z | R-KK1 (KK gauge unification); m_H route-band; Cartan Trace Identity T10 (PROVEN) | CHALLENGED-closed | best-common max_rel=1.123, 0/3 within 2%; Cartan T_eig identity 8.68e-16 EXACT (intact); m_H=131.8±2.15 (+5.36%) |
| INV6-W1-4 KK-SOLITON-COMPACT-OBJECT | INFO | PHONONIC — Z₂ BCS-amplitude domain wall | Domain-wall GW (PROVEN S77); G-KK3/S106 first compact-object occupant | BOLSTERED | kink σ=2.594, M_wall=290.6 M_KK, C=1.177; Derrick 3D-lump FORBIDDEN; bimetric fork (c_acoustic>c_tensor sign-robust) |
| INV6-W2-1 GAMMA-TAU-ONELOOP-TRAJECTORY | PASS | GEOMETRIC — one-loop modulus action Γ[τ]=−½ζ'_D(0,τ) | atlas-04 S3 (S_cl IS modulus action, ASSUMED); Sakharov 1/G_N∝a₂; W4 no-well wall | BOLSTERED | dΓ/dτ\|_fold=+88,149 retains+steepens tree +58,673 (ratio +1.498); Λ_ind=+1350.7>0; root_count=1=M_KK_gravity (1 ULP) |
| INV6-W2-2 TRANSIT-PS-PARKER-BOGOLIUBOV | FAIL | PHONONIC — Parker-Bogoliubov P_ζ(k) through fold | CV-1 A_s (4th route); AMPLITUDE-NORM-66; K_pivot gap (atlas-04 C2 BROKEN) | CHALLENGED-constructive | A_s=5.99e-8 (+1.455 OOM, moved DOWN 1.695); K_pivot=0.975 M_KK derived; REGIME=BREAKDOWN (adiab valid 49.25%<50%) |
| INV6-W2-3 GRAVITON-LOOP-FINITENESS | FAIL | GEOMETRIC — graviton (a₂-fluctuation) R³ Goroff-Sagnotti coefficient | C-F1 ("UV-complete substrate" assumed); emergent-gravity UV status | CHALLENGED-closed | β(a₆,R³)=1.748>0 (UV-power-divergent); control β(a₁₀)=0.309 saturates; emergent gravity = Wilsonian EFT cutoff M_KK |
| INV6-W2-4 EMERGENT-LORENTZ-REALGATE | PASS | PHONONIC — emergent dispersion + SME on κ=3 crystalline substrate | T3-BATCH-S75-EMERGENT-LORENTZ (was INFO/MIGRATED/no-run); T1 [J,D_K]=0 (PROVEN); C-F3/A-F5 | BOLSTERED | ξ₂=−1/16 EXACT both modes (sub-luminal, isotropic to O(k⁴)); CPT-odd SME=0 EXACT by [J,D_K]=0; E_QG2=2.97e17 GeV (6.5 OOM above floor) |
| INV6-W2-5 GRAVITON-SPECTRAL-FUNCTION-DS | INFO | GEOMETRIC — graviton ρ(ω) UV spectral dimension | d_s→8 Weyl asymptotic (PROVEN, Phononic-Investigation.md); AS/CDT/Hořava d_s→2 | BOLSTERED | d_s(σ_*)=8.457 (L≤10), 8.460 (L≤12); graviton-ρ Weyl d=8.59; dist_to_8=0.457≪dist_to_2=6.457 (NO reduction, 2 independent measures) |
| INV6-W3-1 ETA-B-GGE-RESCATTERING | FAIL | PHONONIC — inter-branch GGE strong-rescattering phase | CV-related / B-6 η_B; C6 baryogenesis (CONDITIONAL) | CHALLENGED-closed | R_enh=0.99922≤1.0 EXACT at φ_CP=π/2 (cos-ceiling); R_required=13.55× NOT supplied |
| INV6-W3-2 J-BREAKING-DEFORMATION-ENUM | INFO | GEOMETRIC — J-breaking deformation classification (BF/BS) | LBA-1 (δA "φ_88 unique"); C6 "unique CP source" tag | CLARIFIED (+ forecloses a rescue) | \|S_admissible\|=2 basis dirs BUT independent-CP-source rank=1=span{λ₈}=φ_88 (off(2,7) residual proj_Y=2.78e-17 EXACT) |
| INV6-W3-3 ETA-B-ACOUSTIC-SCHWINGER | FAIL | PHONONIC — acoustic-Schwinger pair production, Mach-13.75 transit | B-6 η_B; field-strength rescue corridor; S43 Schwinger | CHALLENGED-closed | exp(−S_canon)=0.9322 (93% of ceiling); E→∞ boost ×1.073 only; band-low needs exp(−S)=6.19 IMPOSSIBLE |
| INV6-W3-4 ANTIMATTER-DOMAIN-HORIZON | FAIL | PHONONIC — pre-transit acoustic sound horizon vs c/H_0 | Single-domain antimatter (Fermi-LAT <1e-5); white-hole disconnect (PROVEN S85); exflation≠inflation | CHALLENGED-closed (corridor) + BOLSTERED (substrate frame) | R_horizon=8.89e-32 (31 dex short, 71.4 e-fold deficit); single-domain SURVIVES via τ-simultaneity (distinct mechanism) |
| INV6-W4-1 M_KK route-reconciliation | LANDED (workshop) | GEOMETRIC — 3-route M_KK adjudication | CV-2 #1 standing gap; §VII.BS rank-1 (STAGE-3-PERMANENT, S102/S103) | CLARIFIED | STRUCTURAL VERDICT: ONE-ROUTE-DOMINATES (gravity-a₂, 7.4287e16); Question-A rank=1 PROVEN; OVER-DETERMINED jointly REJECTED |

---

## 2. Convergence read-back

### CV-2 (M_KK as a frozen 6.79× gauge-vs-gravity bracket, B-2 dimensional transmutation) → **RELOCATED + structurally sharpened, NOT dissolved**

inv-6 attacked CV-2 with four gates + the W4 workshop, and the bracket did NOT collapse — but its *epistemic type* changed cleanly:

- **W1-1** confirmed the bracket is REAL (ratio=6.7868 EXACT, subsumption=False) and propagated it into a₂-magnitude (1.663 OOM) and a₀-magnitude (3.327 OOM) bands.
- **W1-2** closed the *one KK-native mechanism* that could have broken it from inside (Casimir-volume stabilization): no interior minimum exists, by an EXACT conformal-power identity (`E_Cas(v)=v^{−1/8}·C`, C=−4.30e7≠0). This is the live finding — the breathing modulus IS §VII.BS's multiplicative weight `w=M_KK` wearing a Casimir hat.
- **W2-1** is intra-sector gravity self-consistency (root_count=1=M_KK_gravity) — one channel solved twice, conceded NOT to be over-determination.
- **W4-1** adjudicated all three into **ONE-ROUTE-DOMINATES (gravity-a₂ canonical)** on landed evidence, with the §VII.BS rank-1 single-import status PROVEN at session-track (S102/S103, register-verified: STAGE-3-PERMANENT) and the canonical VALUE held pending the gauge-a₄ loop gate.

**Net read-back**: CV-2 is RELOCATED from "a frozen-since-S42 bracket of unknown status" to a clean two-question decomposition — Question A (rank of import = ONE, PROVEN) vs Question B (canonical value = gravity-a₂, pending one named gate). The "frozen bracket" framing of CV-2 is superseded; the bracket is now a *fixed dimensionless offset between two tree dictionaries on the one weight `w`*, with its physics-vs-tree-artifact status isolated to a single pre-registered compute (CF-INV6-W4-A).

### Quantum-loop side of the gravity sector → **CONFIRMED as a coherent UV package (the wave's deepest structural output)**

This was the convergence inv-6 was most distinctively spawned to fill (inv-1 noted the gravity sector is thorough on its a₂ tree side, almost untouched on its quantum-loop side). Two gates close it as ONE physics:

- **W2-3** (FAIL): emergent graviton R³ Goroff-Sagnotti coefficient is 1/ε-divergent (β(a₆)=1.748>0, a₆ channel below the Weyl threshold 2n>d=8) ⇒ emergent gravity is a Wilsonian EFT cut off at M_KK, NOT finite QG. Closes contradiction C-F1.
- **W2-5** (INFO): d_s→8 in the UV on two independent measures (heat-trace 8.46 + graviton-ρ Weyl 8.59), antipodal to AS/CDT/Hořava d_s→2.

**These are the same UV-structure seen twice**: the a₆ channel diverges *because* d=8 (not 2); a d_s→2 reduction would have softened the UV (the AS mechanism), but the substrate keeps the full SU(3) fiber dimension. CONFIRMED, and now ownable as a falsifiable contrarian prediction.

### B-6 / baryogenesis η_B → **CONFIRMED as a localized open problem (deficit pinned, two rescue corridors closed)**

inv-6 did NOT close the η_B 1.1-OOM shortfall, but it sharpened the constraint map decisively:

- **W3-1** (FAIL) + **W3-3** (FAIL) are *independent* enhancement mechanisms that BOTH cap at ≈1 (R_enh≤1 by cos-ceiling; exp(−S)≤1 by Schwinger-exponent ceiling, fold already at 93%). They converge on the SAME conclusion: the deficit lives in the CP-bias × fiber-volume suppression σ_supp, NOT the production count.
- **W3-2** (INFO) proves the CP source is rank-1 (φ_88), which *forecloses* the natural "source-multiplicity enlarges η_B" rescue.

Three gates triangulate the same residual locus (σ_supp). This is the structural strength of a FAIL cluster: the surviving open problem is now a single, named, computable quantity. **CV-related: the inv-1 "baryogenesis is the sole bottleneck" reading is confirmed and localized.**

### CV-1 (A_s normalization, Parker-Bogoliubov leg of the 6-route hub) → **CONFIRMED direction, REGIME-bounded; one of six routes, now characterized**

**W2-2** (FAIL) is the 4th independent A_s route. It is direction-correct (adiabatic counterterm moved A_s DOWN 1.695 OOM, from +3.15 to +1.455, sign-definite-negative) but neither magnitude-closes (1.455 OOM short of band) nor regime-validates (Parker UV-subtraction valid over only 49.25% of the subhorizon window). The convergence with W1-1 is the headline: the AMPLITUDE-NORM-66 3.15-OOM A_s gap is contained by the a₀-band but EXCEEDS the a₂-band — A_s is an a₂-magnitude observable, so the M_KK bracket explains ≤1.66 of the 3.15 OOM, leaving a residual ~1.49 OOM. CV-1's A_s route is one of six; inv-6 characterizes its regime boundary and feeds a 4-route triangulation.

---

## 3. Four-verb classification

### BOLSTERED

- **§VII.BS rank-1 NNU single-import structure** — before: STAGE-3-PERMANENT (S102 max\|Corr\|=1.0 EXACT, S103 second_rel_sv=1.07e-17; register-verified this review). after: independently CORROBORATED from a new direction (W1-2 Casimir-volume null is the dynamical demonstration that the volume mode is the pure multiplicative weight `w=v^{−1/8}`, never Casimir-stabilized). magnitude: structural (exact conformal-power identity, regulator-independent). citation: §VII.BS (permanent-results-registry); W1-2 (audit 8aec20dd). *This is the cleanest cross-domain bridge of the wave: the same `O=w·Ô` factorization that §VII.BS lives on shows up in the breathing-mode Casimir as `w∝v^{−1/d}`.*
- **Γ[τ]=−½ζ'_D(0,τ) as the correct one-loop modulus action** — before: atlas-04 S3 "S_cl IS the modulus action" ASSUMED. after: the explicit one-loop Γ[τ] retains AND steepens the tree τ-gradient (ratio +1.498, sign retained), induced Λ is de Sitter-positive, and Sakharov↔spectral-zeta over-determines M_KK *within the gravity sector* (root_count=1=M_KK_gravity, 1 ULP). magnitude: PASS (the strongest pre-registered outcome). citation: W2-1 (audit b8cc01fc); generalizes the S95-closed NO-WELL-ONE-LOOP from the *correct* functional.
- **Emergent Lorentz invariance — INFO/MIGRATED → real PASS** — before: T3-BATCH-S75-EMERGENT-LORENTZ = INFO/value=MIGRATED/convention=no-run-no-gate (register-verified: a hygiene migration, never computed). after: a genuine PASS — ξ₂=−1/16 EXACT for BOTH Goldstone and graviton-zero-mode (same hexagonal point group ⇒ shared light cone by symmetry, A-F5 resolved structurally), CPT-odd SME=0 EXACT by [J,D_K]=0, E_QG2=2.97e17 GeV (6.5 OOM above the detectable floor). magnitude: structural (Sage-exact −1/16; algebraic-zero CPT-odd). citation: W2-4 (audit 4b079da0). *Upgrades a no-run-no-gate placeholder to a forced prediction against the most precise CPT test in physics (neutral-meson 1e-18).*
- **d_s→8 (no UV dimensional reduction)** — before: PROVEN as the σ→0 Weyl asymptotic (Phononic-Investigation.md, register-verified). after: CONFIRMED on the canonical cache AND given a SECOND independent measure (graviton ρ(ω) Weyl counting d=8.59), and re-framed as an ownable falsifiable contrarian signature (antipodal to AS/CDT/Hořava d_s→2). magnitude: INFO (8.46 overshoots the strict ≤0.2 band — an overshoot of 8, NOT a drift toward 2). citation: W2-5 (audit 05382117). *Consistent with the established result that spectral-dim-flow-as-a-string/CDT-bridge is dead; inv-6 sharpens it into a positive prediction.*
- **Z₂ BCS-amplitude domain wall as first compact-object-like structure** — before: Domain-wall GW PROVEN (S77); G-KK3/S106 occupant slot open. after: the first explicit super-compact wall patch (C=1.177>Buchdahl 4/9), Derrick 3D-lump FORBIDDEN (genuine content is a Z₂ wall, not a Q-ball), with a bimetric fork (c_acoustic>c_tensor sign-robust at the core). magnitude: structural (existence + characterization). citation: W1-4 (audit de92408b, Option-A canonical).

### CHALLENGED

- **C-F1 "UV-complete substrate ⇒ finite emergent gravity"** — before: silent favorable assumption (UV-completeness inherited). after: CLOSED against finiteness — emergent gravity is a Wilsonian EFT with explicit higher-curvature counterterms cut off at M_KK (R³ a₆ channel 1/ε-divergent, β=1.748>0). magnitude: structural (power-counting + numerical β; the finite trace at fixed L_max ≠ loop-finiteness in the L_max→∞ continuum). citation: W2-3 (audit 45f4f96a). **Corridor-closed; constructive — converts a slogan into a documented theorem.**
- **R-KK1 (KK-tower reproduces SM couplings from a single α_unif at M_KK)** — before: untested phenomenological bridge. after: FAIL by ~2 OOM (best-common max_rel=1.123, 0/3 within 2%); the Cartan Trace Identity itself is UNSCATHED (T_eig identity 8.68e-16 EXACT) — what fails is the bridge, because the fiber Peter-Weyl tower is the wrong spectrum (= S96 isometry≠SM / C-KK1). magnitude: structural (112% floor, not a precision near-miss). citation: W1-3 (audit 6c2fb858). **Corridor-closed; the FAIL diagnoses *which* object is wrong (spectrum, not scale) — this is precisely the feynman-side R1 argument in the W4 workshop.**
- **η_B GGE-rescattering enhancement corridor** — before: candidate ~13.5× source (LHCb-2025 baryon-CP analog). after: CLOSED — R_enh≤1.0 EXACT at the substrate's maximal weak phase φ_CP=π/2 (cos-ceiling); LHCb's boost needs *non-maximal* phases. magnitude: structural (exact ceiling identity). citation: W3-1 (audit d08cffd9). **Corridor-closed.**
- **η_B acoustic-Schwinger field-strength corridor** — before: candidate Mach/field-strength source. after: CLOSED — exp(−S)≤1 and the fold sits at 93% of the production ceiling (S_canon=0.0702), so the entire E→∞ headroom is ×1.073; band-low needs the impossible exp(−S)=6.19. magnitude: structural (Schwinger-exponent ceiling, anchor-robust to the OES gap). citation: W3-3 (audit 97960ac4). **Corridor-closed; W3-1 ∧ W3-3 convergently localize the deficit to σ_supp.**
- **Single-domain antimatter via a super-Hubble acoustic horizon** — before: candidate metric-causal-patch hypothesis (plan track_A, prior 0.80). after: FAIL by 31 dex / 71.4 e-folds (R_horizon=8.89e-32) — the substrate's own integrated expansion history (N_e^total=2.92 ≪ 60) forbids it. **BUT the conclusion (single-domain, Fermi-LAT <1e-5 consistent) SURVIVES via a structurally distinct substrate mechanism: τ-simultaneity (one Jensen slice).** magnitude: structural (dual-pathway agreement on R≪1). citation: W3-4 (audit 198255d7). **Corridor-closed for the metric hypothesis; substrate-confirming — the FAIL is the substrate refusing container-thinking (exflation = spectral complexification, NOT metric inflation), with the physical conclusion preserved by a fiber-internal mechanism.**

### CLARIFIED

- **AMPLITUDE-NORM-66 A_s "exclusion" re-scope** — before: FAIL (marginal), 3.15 OOM, "right ratios, wrong amplitudes" (register-verified: still FAIL, still open). after: truth value UNCHANGED (still a failing amplitude), but the FAILURE is now *decomposed*: A_s is an a₂-magnitude observable; the M_KK bracket injects only 1.663 OOM on a₂ (3.327 on a₀), so the gap is "un-normalizable pending M_KK (≤1.66 OOM, a₂-band) PLUS a residual ~1.49-OOM a₂-channel shortfall." magnitude: precision (Sage-exact band decomposition). citation: W1-1 (audit fb920648) + W2-2 (Parker route moved it down 1.695). **A clean re-scope from "clean data-miss" to "scale-normalization ambiguity + budgeted residual" — register-status (FAIL) preserved.**
- **LBA-1 δA "φ_88 unique" → rank-1 CP-source subspace** — before: "φ_88 is the unique J-breaking CP source" (a basis-direction claim). after: truth value SHARPENED — \|S_admissible\|=2 *basis directions* survive the literal filter, but the independent-CP-source RANK is 1 = span{λ₈} = φ_88 (the second survivor off(2,7) is collinear in hypercharge projection, residual proj_Y=2.78e-17 EXACT). magnitude: structural (epistemic-type promotion: "unique direction" → "rank-1 source subspace"). citation: W3-2 (audit ca1fd44a). **CLARIFIED — and load-bearing: it forecloses the source-multiplicity η_B rescue (eps_CP_naive_basis_sum is NOT a physical sum).**
- **M_KK #1 standing gap → Question-A/Question-B decomposition** — before: "3 routes, canonicity disputed." after: truth value UNCHANGED (M_KK remains imported), but the disputed structure is resolved into orthogonal axes — Question A (rank=1, PROVEN at session-track) vs Question B (canonical value=gravity-a₂, held pending one gate). magnitude: structural (category decomposition dissolves the kk-vs-feynman conflict). citation: W4-1 workshop (LANDED). **CLARIFIED — the adjudication dissolved an apparent contradiction by separating two questions, both correctly answered.**

### MUDDLED

- **C6 baryogenesis register-anchor discrepancy** (register-vs-investigation, surfaced this review) — atlas-04 C6 reads CONDITIONAL with **"η ~ 3.4e-9 (0.75 decades from observed 6.1e-10), requires exactly 2 pair breaks during transit"**, while the S98 canonical AND every inv-6 W3 gate anchor on **η_B = 4.517492e-11 (≈1.13 decades short)**. These are *different numbers for the same gap* (3.4e-9 vs 4.5e-11, ~1.9 OOM apart) and a *different mechanism count* ("exactly 2 pair breaks" vs the ε_nLI=ε_K7²/n_pairs σ_supp normalization). before: register tension latent. after: inv-6's three convergent W3 gates make the η_B=4.5e-11 anchor (and the σ_supp-locus deficit) the active reading, but they did NOT reconcile it against the atlas-04 "3.4e-9 / 2-pair-breaks" prose — a register-status incoherence the digest must surface. magnitude: ~1.9 OOM register-vs-investigation, structural (two distinct normalization stories). citation: atlas-04 C6 vs S98-W3-2 (3be22b8a) vs W3-1/W3-3. **This is the one genuine MUDDLE inv-6 leaves — NOT internal to inv-6 (its three gates are mutually coherent), but between inv-6's anchor and the standing C6 register prose. The σ_supp recompute (CF-INV6-W3-A) is the compute that would resolve which normalization is canonical, and the EVOI/atlas-04 reconciliation (CF-INV6-W3-B / HY1) is the register fix.**

---

## 4. Routing (pre-routed; orchestrator finalizes Stage 3)

### →WORKSHOP (Q1 — math/physics adjudication of competing readings)

- **None NEW from inv-6's own substance.** The one genuine adversarial adjudication inv-6 contained (M_KK route-reconciliation) was ALREADY executed as the W4-1 workshop and LANDED a converged STRUCTURAL VERDICT — it is not a re-runnable workshop, it is a finished one whose verdict-candidate routes to compute/registry (CF-INV6-W4-A/B). Per `Investigating-Workshops.md §"No workshops is a valid output"`, inv-6's substance is dominated by clean FAIL/INFO corridor-closures + one finished workshop; honest count of NEW workshop seeds = **0**.
  - *One latent candidate flagged, NOT promoted*: the **C6 η_B register-anchor discrepancy** (MUDDLED above, 3.4e-9-vs-4.5e-11) is a genuine ledger-dissonance — but it is a Q2 register-reconciliation (which normalization is canonical) resolvable by the σ_supp compute + an atlas-04 down-tag, NOT a two-reading first-principles physics adjudication. It routes to COMPUTE-CF + HOUSEKEEPING, not a workshop. (If the σ_supp recompute were to show the two anchors are *both* defensible under different assumptions that cannot both hold, it would PROMOTE to a Q1 workshop — flagged for Stage-2 rollup against inv-3's M_KK-derivability and any other η_B-touching investigation.)

### →COMPUTE-CF (4-field + EVOI)

1. **CF-INV6-W4-A — `INV{n+1}-MKK-GAUGE-LOOP-SELFCONSISTENCY`** (the decisive M_KK gate; leading next-session compute). **What**: the a₄-channel analog of W2-1 — compute `1/g²(M_KK)` from the same Γ_1loop=−½ζ'_D(0,τ), projected onto the Yang-Mills `Tr F²` coefficient *through the SU(A_K) inner-fluctuation algebra* (NOT the fiber Peter-Weyl tower — the W1-3 error / S96 isometry≠SM). **Inputs**: inv6_w2_1 npz (b8cc01fc); L12 cache (canonical 9e6d9cf7); the C-KK1/S96-route-A inner-fluctuation gauge projector onto A_F=ℂ⊕ℍ⊕M₃(ℂ); observed (α_em,sin²θ_W,α_s) at m_Z; M_KK_gravity=7.4287e16, M_KK_kerner=5.0417e17 as fork targets. **Gate**: 3-way fork — root at 7.43e16 ±2% → cross-sector OVER-DETERMINED (M_KK derived); root at 5.04e17 → UNDER-DETERMINED/§VII.BS rank-1 with fixed internal structure; ill-defined/scheme-dependent → ONE-ROUTE confirmed. Scheme pin: ζ-regulated, Λ_UV=μ=M_KK, L_max=12 (PRU Class-8 guard). **Effort**: ~1–2 compute (joint feynman+kk). **EVOI**: HIGHEST of the inv-6 carry-forwards — it is the single gate that resolves the framework's #1 standing gap (M_KK) and discriminates all three M_KK verdict-classes; both W4 advocates name it identically.
2. **CF-INV6-W3-A — σ_supp normalization recompute** (the localized η_B deficit + the MUDDLE resolver). **What**: compute the CP-bias × fiber-volume suppression σ_supp=ε_nLI²·geom·fbar directly, to test whether the ~13.5× η_B deficit is a σ_supp normalization error vs a structural production shortfall — AND to reconcile the inv-6 anchor (4.5e-11) against the atlas-04 C6 prose (3.4e-9). **Inputs**: inv6_w3_1 (d08cffd9), inv6_w3_3 (97960ac4), inv6_w3_2 rank-1 φ_88 (ca1fd44a); S98-W3-2 (3be22b8a); atlas-04 C6 "2-pair-break" derivation. **Gate**: \|η_B(σ_supp-recomputed)/6.12e-10 − 1\| ≤ info_band PASS / FAIL; pre-register the band; AND a side-criterion reconciling 4.5e-11 vs 3.4e-9 (which normalization the substrate selects). **Effort**: ~1 compute. **EVOI**: HIGH — resolves both the localized open problem AND the MUDDLED register discrepancy.
3. **CF-INV6-W2-A — 4-route A_s triangulation + atlas-08 EFT self-classification**. **What**: triangulate the 4 independent A_s routes (inv-3 near-floor-DOS, inv-4 exit-greybody, inv-5 impulse-quench, inv-6 Parker-Bogoliubov +1.455 OOM) into a single A_s constraint + converged regime-of-validity; promote W2-3+W2-5 (Wilsonian EFT, no d_s reduction) into atlas-08. **Inputs**: inv6_w2_2 npz + 3 prior-inv A_s npz; inv6_w2_3/w2_5 npz; atlas-08. **Gate**: triangulation PASS = regime-valid windows mutually consistent on A_s central value (pre-register tolerance); EFT-classification = artifact-existence. **Effort**: ~1 compute + 1 atlas landing. **EVOI**: MEDIUM — closes the cross-investigation A_s envelope and lands the coherent UV self-classification.

### →HOUSEKEEPING (register cell + fix; mostly session-track promotions of investigation-track results)

- **§VII.BS rank-1 corroboration from W1-2** — no register edit OWED (the rank-1 hardening is already STAGE-3-PERMANENT at S102/S103); cite W1-2 as independent dynamical corroboration if/when inv-6 is promoted. (HOUSEKEEPING-cite, not a write.)
- **T3-BATCH-S75-EMERGENT-LORENTZ INFO/MIGRATED → PASS** — register cell: the s81 batch-hygiene migration. On session-promotion of W2-4, upgrade the no-run-no-gate INFO to the real PASS (ξ₂=−1/16, CPT-odd structural null). [CF-INV6-W2-B mirror; mack/designated-writer per the falsifier surface for the LIV/CPT-even row.]
- **C6 baryogenesis EVOI Rank-8 CLOSED→CONDITIONAL down-tag (HY1)** — register cell: EVOI table + atlas-04 C6. Reconcile the "3.4e-9 / 2-pair-breaks" prose against the S98 4.5e-11 anchor (the MUDDLE). [CF-INV6-W3-B; gated on CF-INV6-W3-A's σ_supp verdict.]
- **C6 "unique CP source" tag re-word (HY-W3-2)** — register cell: atlas-04 C6 / EVOI Rank-8. Re-word "unique CP source" → "rank-1 CP-source subspace = span{λ₈} (φ_88-hypercharge)" per W3-2. [CF-INV6-W3-B mirror.]
- **m_H single-number collapse (131.8±2.15) for capstone m_H-prose hygiene** — register cell: capstone m_H prose. The W1-3 route-band collapse is available; +5.36% from obs (outside 2%). [CF-INV6-W1-A mirror; capstone-hygiene 5-question gate Q4 already fired YES in inv-6 housekeeping.]
- **Seed hygiene HY4/HY5/HY6** — HY4 (corpus paper-32 a_g prose), HY5 (capstone §0/§2.4 gauge-from-NCG-algebra reconciliation — directly relevant to the W1-3 / C-KK1 isometry≠SM finding), HY6 (alpha_GUT canonical-constants registration). All session-track; route to investigation-close.

### →CLOSED (corridor closed; constraint-map update, recorded not carried)

- **Casimir-volume route to a 3rd M_KK determination** — CLOSED by exact conformal-power identity (W1-2). The breathing modulus cannot stabilize; volume-preservation (atlas-04 G6) stays IMPOSED. Note: the only surviving thin leg is a non-conformal combined direction off the det g=6561 surface, predicted monotone (off-Jensen 35D Hessian ridge-confined, S76 HESS-61).
- **C-F1 "finite emergent gravity"** — CLOSED against finiteness (W2-3); emergent gravity = Wilsonian EFT cutoff M_KK. Constraint-map: atlas-08 should record EFT-with-explicit-higher-curvature-counterterms, NOT finite QG.
- **η_B GGE-rescattering enhancement** — CLOSED (W3-1, R_enh≤1 at φ_CP=π/2).
- **η_B acoustic-Schwinger field-strength enhancement** — CLOSED (W3-3, exp(−S)≤1, fold at 93% ceiling).
- **Single-domain antimatter via super-Hubble metric acoustic horizon** — CLOSED (W3-4); the conclusion survives via τ-simultaneity (a distinct, NON-metric mechanism), so the corridor is closed but the physical claim is preserved.
- **OVER-DETERMINED M_KK verdict-class** — jointly REJECTED in the W4 workshop (no two structurally-independent channels select one value on landed evidence).

---

## 5. Cross-investigation hooks (for Stage-2 rollup)

- **CV-2 / M_KK** — inv-3 (CV-2 M_KK / B-2; reviewer kitaev) ran the complementary **M_KK derivability-in-principle** half; the W4-1 workshop explicitly cross-cites it ("do not merge — the two halves of the #1 standing gap"). inv-11 (reviewer landau) ran **M_KK BCS dimensional-transmutation (B-2)** and an mkk-gap-vs-integer-scheme workshop. **Stage-2 must roll inv-3 + inv-6 + inv-11 into a single net CV-2 verdict** — all three touch the same import-rank/value question; inv-6's Question-A/Question-B decomposition + the gauge-a₄ gate (CF-INV6-W4-A) is the discriminating frame.
- **C6 / η_B (B-6)** — inv-6 is the primary η_B-mechanism investigation. Check whether any other investigation touches baryogenesis or the σ_supp normalization for the MUDDLE rollup; the atlas-04 C6 "3.4e-9 / 2-pair-breaks" prose is the standing register anchor that ALL η_B-touching investigations should be reconciled against in Stage-2.
- **CV-1 / A_s (6-route hub)** — inv-3 (near-floor-DOS), inv-4 (exit-greybody), inv-5 (impulse-quench), inv-6 (Parker-Bogoliubov), inv-12 (A_s wall / 6-route hub, reviewer connes), inv-10 (A_s normalization, reviewer transit-dynamics). **Six routes across six investigations** — Stage-2 must build the single A_s normalization envelope (CF-INV6-W2-A is inv-6's contribution to it). inv-12's "is Tr f(D²) the right functional" (CV-4 SA≠free energy) connects to inv-6 W2-1's Γ[τ] (the correct one-loop functional) — a direct hook.
- **Quantum-loop gravity / d_s / EFT** — inv-9 (cross-framework QG, swampland; reviewer hawking) is the natural Stage-2 partner for W2-3 (EFT) + W2-5 (d_s→8). The d_s→8 contrarian signature and the Wilsonian-EFT verdict are cross-framework claims (vs AS/CDT/Hořava/LQG) that inv-9's QG-character lens should roll up alongside.
- **Emergent Lorentz / CPT** — W2-4's CPT-odd structural null ([J,D_K]=0) connects to any CPT/antimatter investigation; the LIV E_QG2=2.97e17 GeV prediction is a falsifier-inventory candidate (mack sole-writer).
- **§VII.BS rank-1** — touched by inv-3, inv-11, inv-12 (FI/RD ledger), inv-6. The S102/S103 hardening is the shared session-track anchor; Stage-2 should confirm no investigation contradicts the rank-1 PROVEN status.

---

## 6. Stranded hygiene (rescue list — HY items inv-6 routed OUT targeting session-track registers, never applied)

All inv-6 hygiene is correctly track-local (an investigation CANNOT mutate session-track curated registers per `gate-verdicts.md §"Investigation-Track Canonical Path"`). The following target session-track registers and remain UNAPPLIED — they must be lifted into a session-mode `/rclab-plan` (Stage-4) or they are lost:

- **HY1** — EVOI Rank-8 baryogenesis CLOSED→CONDITIONAL down-tag (EVOI table + atlas-04 C6). Carries the MUDDLE: reconcile the atlas-04 "η~3.4e-9 / 2-pair-breaks" prose against the S98/inv-6 anchor (4.5e-11). [in CF-INV6-W3-B]
- **HY2** — η_B falsifier-row mint (falsifier-master-inventory.md, **mack sole-writer**). [in CF-INV6-W3-B]
- **HY3** — δ_CP^PMNS falsifier-row (falsifier-master-inventory.md, mack sole-writer); note W3-1 did NOT structurally derive the lepton/baryon CP orthogonality — δ_CP^PMNS=0 (S99) stands on its own derivation. [in CF-INV6-W3-B]
- **HY-W3-2** — atlas-04 C6 / EVOI "unique CP source" → "rank-1 CP-source subspace = span{λ₈}" re-word. [in CF-INV6-W3-B]
- **HY-W2 (atlas-08 EFT self-classification)** — record emergent gravity as Wilsonian EFT (cutoff M_KK, explicit higher-curvature counterterms) + d_s→8 no-reduction in atlas-08. [in CF-INV6-W2-A/B]
- **HY-W2-4 (T3-BATCH-S75-EMERGENT-LORENTZ upgrade)** — INFO/MIGRATED/no-run-no-gate → real PASS on session-promotion. [in CF-INV6-W2-B]
- **HY-W4 (§VII.BS clause-(b) caveat retirement)** — ALREADY landed at session-track (S102/S103, register-verified: clause-(b) RESOLVED per atlas-08-freshness-S103). No edit owed — cited, not stranded. (Listed for completeness so Stage-2 does not re-mint it.)
- **HY4** — corpus paper-32 a_g prose correction (session-track corpus).
- **HY5** — capstone §0/§2.4 gauge-from-NCG-algebra reconciliation (capstone prose; directly relevant to the W1-3 isometry≠SM / C-KK1 finding). [capstone-hygiene Q4 fired YES]
- **HY6** — alpha_GUT canonical-constants registration (canonical_constants.py).

**Rescue priority**: HY1 + HY-W3-2 (the C6 MUDDLE pair) and HY-W4 (already done — do not re-mint) are the highest-signal; HY5 connects the W1-3/C-KK1 finding to the capstone. None are applicable until inv-6 is promoted into a session.

---

*End of investigation-6 distillation digest. Reviewer: kaku-speculative-theorist (neutral). Register status verified against knowledge MCP this review (§VII.BS STAGE-3-PERMANENT S102/S103; AMPLITUDE-NORM-66 FAIL; C6 CONDITIONAL with the 3.4e-9-vs-4.5e-11 discrepancy; d_s→8 PROVEN; T3-BATCH-S75-EMERGENT-LORENTZ INFO/MIGRATED; M_KK constants S42 superseded=False).*
