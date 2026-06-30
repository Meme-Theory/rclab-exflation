# Session X Wave W2 — Comprehensive Expansion of Phononic-Substrate-Geometry.md (Results Working Paper)

**Session**: X | **Wave**: W2 | **Plan**: session-x-plan-w2.md | **Theme**: Substrate-geometry-as-resonator — SU(3) topology, spectral triple, Peter-Weyl/Casimir/Dirac spectrum, Seeley-DeWitt a_n moments, spectral-action variational principle, cross-pillar geometry bridges; expand Phononic-Substrate-Geometry.md to S93-era whole-project view.

## Gate Sections

### §W2-1. WX-W2-1-AGGREGATE-DOMAIN-SURVEY (tesla-resonance)

**Status**: COMPLETED
**Gate ID**: `WX-W2-1-AGGREGATE-DOMAIN-SURVEY`
**Trigger**: `[AUDIT]`
**Classification**: **GEOMETRIC** (whole-domain survey of substrate-geometry across ~93 sessions)
**Agent**: `tesla-resonance`
**Hypothesis**: The whole-project (S93-era) substrate-geometry domain — SU(3) topology, the spectral triple (A_F, H_K, D_K), Jensen moduli geometry, Peter-Weyl/Casimir/Dirac spectrum, Seeley-DeWitt a_n moments, the spectral-action variational principle, and the §VII geometry bridges — can be mapped across the pertinent KB entity classes, and the GAP between what the project knows in this domain and what Phononic-Substrate-Geometry.md (post-S84) covers can be enumerated with a KB citation per gap row.
**Plan reference**: `sessions/session-plan/session-x-plan-w2.md` §W2-1 (machinery pin, PASS/FAIL rubric, seven sub-domains a–g, gap-taxonomy).

**Output Artifacts** (closure-verification checklist):
- (1) script `computations/session-x/sx_w2_aggregate_domain_survey.py` — PRESENT (19,654 B). `grep -E 'from canonical_constants import|append_verdict'` → `from canonical_constants import *`, `from canonical_constants import (`, `def append_verdict(...)`, `append_verdict(verdict, value_str, ...)`. ✓
- (2) data `computations/session-x/sx_w2_aggregate_domain_survey.npz` — PRESENT (11,387 B; subdomains + gap-rows + constant-currency snapshot for G2 hand-off). ✓
- (3) plot `.png` — N/A (optional; survey/enumeration gate, no numerical plot).
- (4) verdict line in `computations/session-x/sx_gate_verdicts.txt` matching `^WX-W2-1-AGGREGATE-DOMAIN-SURVEY:.* audit_sha256=[a-f0-9]{64}` → PRESENT, `audit_sha256=79efcbeb79015f5390db4c8bfad4ea7b163273d66c5cd13ec67228378ac70952`, `content_sha256=1a4f9b9df575ecc3a858c73518bf021cb6f5e42748ba5327dc93694e9292cf8a`; companion dual-SHA comment row PRESENT. ✓
- (5) this WP §W2-1 section — `**Status**: COMPLETED`, `**Verdict**` + `**Output Artifacts**` + `**MCP Pre-Compute Audit**` blocks populated. ✓

**MCP Pre-Compute Audit** (~24 distinct knowledge-MCP queries fired across the seven sub-domains a–g; one-line salient return each):

| # | Query | Salient return |
|:--|:------|:---------------|
| 1 | `search_knowledge("tau_fold uniqueness van Hove cusp theorem")` | §VII.M.W10-3 PERMANENT (theorem `proven_1504`); gate `S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM` PASS (value='promoted', scheme=van-Hove-cusp-non-stationarity) |
| 2 | `search_knowledge("spectral dimension flow d_s CDT return probability heat kernel")` | S92 workshop `s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md`; `d_s(σ)=−2 d ln P/d ln σ`; σ_*=1.4005 M_KK⁻² windowed ≠ σ→0; impedance `Z(E)=ρ_E·v_g` cancellation; eqs 6590-6595 |
| 3 | `search_knowledge("composite bridge map dimensional class Wodzicki HKR VII.BA")` | §VII.BA workshop S92 (connes+mack, CONVERGED); `GV_APS_L12=GV_CS_L12=−1.2081580929e+08` float64-exact; T1-T5 taxonomy; Wodzicki deg −2s vs HKR deg 0 |
| 4 | `search_knowledge("Mellin cone substrate-distance pole residue Wodzicki s=3 s=4")` | pole(s=3)=substrate-distance-1; pole(s=4)=substrate-distance-2; pole(s=−1)=IC slot; `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` INFO |
| 5 | `search_knowledge("Jensen deformation moduli space tau asymmetry stratum coalescence VII.AE")` | §VII.AE PERMANENT (δ_τ_crit_neg=−0.0750±0.005 anticrossing-swap; δ_τ_crit_pos=+0.175±0.05 stratum-coalescence; 2.33× asymmetry); §VII.AD/AJ V_4 cluster |
| 6 | `search_knowledge("Seeley-DeWitt moment regulator FI RD MIXED spectral functional a_2 a_4")` | S82 42-row taxonomy FI=30/RD=4/MIXED=8 (FI-identity subset 3); two functors M_lizzi + M_connes; a_0=155984/a_2=64308.24/a_4=29086.18 (L_max=10) |
| 7 | `search_knowledge("Friedrich-Bar saturation Casimir bound L_max truncation bottom-K eigenvalue")` | S87 W11-2/W11-3 saturation theorem; η_FB=0.547≥0.40; bottom-K saturated ∀ L≥10; CF-47 Taylor analogue (S90); unified S92 W9-3 |
| 8 | `search_knowledge("LQG loop quantum gravity comparison phonon exflation bounce CDT de Sitter")` | curated doc `sessions/framework/correspondence/loop-quantum-gravity-phonon-exflation-comparison.md` (S92); eqs 18046-18057 |
| 9 | `search_knowledge("cross-pillar bridge VII.AF.1 first registered Connes-Karoubi K-theory Level-3 Level-2")` | §VII.AF.1.OP-PROJ first LANDED bridge (S87 W5-1, Pillar III↔IV; 0.0095% F_4 at L_max=10; L⁻³ envelope; Level-3/Level-2=0.0950); Door-S86-CPB |
| 10 | `search_knowledge("A_F Birkhoff uniqueness theorem Wedderburn 3907 verdict value 16")` | gate `S84-AF-BIRKHOFF-UNIQUENESS-PROOF` FAIL value=16 (Witten integral, scheme=Wedderburn-Artin); PASS-THEOREM W8-87b rel_err=1.23e-15; §VII.W-3.ALGEBRAIC STAGE-3-PERMANENT (S88 W4a-17, N7, Door-S88-WedderburnFrobenius) |
| 11 | `search_knowledge("155984 eigenvalues 78080 unique L_max 10 Peter-Weyl card spectrum")` | `N_DK_eigenvalues=155984=card(spectrum L_max=10)` total; 78,080 unique; index `max(p,q)≤L_max` (NOT `p+q≤L_max/2`); a_0=155984=total mode count |
| 12 | `search_knowledge("alpha_s substrate-distance-1 -0.08587279 scale separation pivot goldstone 54 decades transport degree")` | `alpha_s_substrate_distance_1=−0.08587279` (Mellin s=3, in BZ) SCALE-SEPARATED 54.04 decades from `alpha_s_pivot_goldstone≈0`; S93 W7-1 deg(T_BZ→pivot)=+2 NON-SCALAR PASS |
| 13 | `search_knowledge("SU(3) principal bundle S5 instanton winding pi_3 pi_4 Weyl A_2 root system")` | π_3(SU(3))=ℤ instantons; π_1(SU(3))=0 (no vortices); A_2 root hexagon; a_2 via Gilkey 20R/3·Vol; D_K=⊕_{(p,q)} D_K^{(p,q)} block-diagonal |
| 14 | `search_knowledge("Higgs mass framework tree 97 GeV 125 KK threshold Aitken-Kasparov m_H")` | m_H=127.5–131.8 GeV Aitken-Gaussian (S62-S66; canonical class=131.8); filter-independent tree m_H=134 (A10); 97 GeV = S83 gear-machine tree; ACCOMMODATION-FLAGGED (falsifier-rigor-registry) |
| 15 | `search_knowledge("Baptista SU(3) Dirac spectrum heat kernel collab Peter-Weyl Casimir 56 60 61")` | HEAT-KERNEL-A2-61 (S60/S61): a_2=(4π)⁻⁴·(20R/3)·Vol (Lichnerowicz fix of 38-session error; vs naive 8R/3); a_2=(4π)⁴·Res_{s=3} ζ_{D_K²}(s) Mellin route; session-56-dirac-collab |
| 16 | `search_knowledge("four-speed hierarchy c_mod c_BLV c_BA c_L 3He-B inheritance")` | c_mod=1.000, c_BLV=0.485, c_BA=0.399, c_L=[0.019,0.032] (mid 0.0255); SOUND-SPEED-64 PASS (all causal); Ma_BLV=17.1/Ma_BA=20.7/Ma_Leggett=331 |
| 17 | `search_knowledge("rank-6 partition 53 identities biographical framing audit 78%")` | `S84-BIOGRAPHICAL-FRAMING-AUDIT` value=0.7778 INFO; rank(M)∈[5,7] central 6 PROVISIONAL; 53 identities → 5 layers {ALGEBRAIC 35, TOPOL 3, CAUSAL 3, ENERGETIC 7, TEMPORAL} (§W8-91 PROVEN) |
| 18 | `search_knowledge("d_s windowed spectral dimension fold value 8 manifold Weyl gamma_E impedance Z")` | `S93-W7-3-FOLD-ENERGY-WINDOWED-DS-GATE` INFO: min_ds=7.7953, ds_σ_*=8.4851, γ_E_central=0.4807; σ→0 d_s=8 robust (S31a/S34/S44/S52/S89 slope_A(L=14)=15.734≈2·8); `min d_s<3` van-Hove criterion RETIRED (S93 W7-3) |
| 19 | `get_constant("M_KK")` | 7.428660036284456e+16 (default = gravity route; NO PROVENANCE supersession) |
| 20 | `get_constant("M_KK_kerner")` | 5.041679838376001e+17 (S42 CONST-FREEZE-42; gauge-metric route; Superseded=False) — resolves Q2 (§13 "~5×10^17" is the Kerner route, not an error) |
| 21 | `get_constant("tau_fold")` | 0.19 (S12/S42 CONST-FREEZE-42; Superseded=False) |
| 22 | `get_constant("Delta_BCS")` | 0.4642547394830737 (S70 BCS-GAP-CANONICAL-70; R-Protected=YES) |
| 23 | `trace_entity("spectral dimension d_s flow CDT same-functional fair comparison")` | No trace (concept lives in S92 workshop + S93 W7-3 gate; not a named registry entity — confirms it is NEW geometry the doc must absorb) |
| 24 | (canonical_constants.py grep cross-checks) | dS_fold=58672.80241, d2S_fold=317862.84898, S_fold=250360.67696, E_cond=−0.13685 (8-mode ED), n_s_framework=0.9561 (T6) ≠ planck_ns=0.9649 (observational) |

PRE-CLOSED status: NONE — this is a survey/expansion gate, not a recomputation of a closed mechanism. The survey MINES closed/permanent results read-only as inputs; it does not re-gate them.

**Verdict**: **INFO** — `value='seven_subdomains_swept=True;E_gaps=12;Q_gaps=7;all_rows_KB_cited=True;kb_query_count~24;reconcile_items_for_G2=Q1_AF_verdict_vs_theorem+Q6_cube3_open'`. The survey is complete and fully cited (PASS predicate satisfied: all seven sub-domains a–g swept; every gap row carries a KB citation + where-it-belongs line). The INFO (vs PASS) flags TWO structurally-ambiguous reconciliation items for G2's QA layer per the plan's INFO_meaning: Q1 (A_F-Birkhoff verdict-vs-theorem split — the literal value-16 FAIL gate vs the W8-87b PASS-THEOREM now STAGE-3-PERMANENT) and Q6 (cube-3 "12" still genuinely OPEN, heat-kernel route FAILed at S85). These must be reconciled-in-text by G2, not silently flipped.

**Results** — STATE-OF-DOMAIN MAP + GAP ANALYSIS:

#### STATE-OF-DOMAIN MAP (substrate-geometry, S93-era, organized by seven sub-domains)

**(a) SU(3) cavity topology** — 8-dim compact Lie manifold; principal SU(2)-bundle over S⁵ (`π_4(S³)=ℤ/2` classifies the two bundles, SU(3) is the nontrivial one); A_2 root system (hexagonal, Weyl `S_3`, rank 2, center `Z_3`); `π_1=0` (topological censorship — no vortices), `π_3(SU(3))=ℤ` (instanton winding, S36-S38 Ordered Veil stabilization); weight-lattice charges label every Peter-Weyl `(p,q)` sector. **Stable since S7-S18; no S85→S93 revision.**

**(b) Wave-guide algebra** — `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` (24-dim real; `K_0=ℤ³`); KO-dim=6 mod 8; `J²=+1`, `[J,D_K]=0` (CPT); bimodule multiplicity 3 (generations). **MAJOR S88 UPGRADE**: the A_F uniqueness was PROMOTED to STAGE-3-PERMANENT as §VII.W-3.ALGEBRAIC "Wedderburn-Artin Frobenius Rescue Class" (S88 W4a-17, connes+volovik; N7, Door-S88-WedderburnFrobenius). The literal `value=16` FAIL gate is the Witten-integral check (`EXP_WITTEN_INTEGRAL=16.0`), NOT the candidate-count; the W8-87b proof (rel_err=1.23e-15) is the PASS-THEOREM. The doc's "1/3,907" framing is now backed by a permanent cross-axis theorem, STRONGER than at authorship.

**(c) Jensen moduli geometry** — volume-preserving TT, `L_1=e^{+2τ}/L_2=e^{−2τ}/L_3=e^{+τ}`, `L_1·L_2³·L_3⁴=1`. **NEW S88 STRUCTURE**: the substrate-IS picture now operates at TWO levels (`phononic-framing.md §"Single-τ-slice vs moduli-deformation"`): Level-1 single-τ-slice (eigenvalues, cardinality at fixed τ) and Level-2 moduli-deformation (the moduli-space of τ-deformations IS substrate-IS). §VII.AE (PERMANENT) maps the breakdown geometry on either side of the fold: negative-side anticrossing-swap at δ_τ_crit_neg=−0.0750±0.005; positive-side stratum-coalescence at δ_τ_crit_pos=+0.175±0.05; 2.33× negative/positive asymmetry. §VII.AD Δ_0 localization + §VII.AJ partition-stability bot-20 cardinality (2,4,8,6) + V_4 stratum-coalescence cluster (S88 PERMANENT).

**(d) Eigenmode census** — 155,984 eigenvalues = `card(spectrum at L_max=10)` (TOTAL, with multiplicity); 78,080 UNIQUE; index convention `max(p,q) ≤ L_max` (the doc's §5.1 `p+q ≤ L_max/2` is WRONG). B1 acoustic (1 mode, V=0 Trap 1, 2Δ=0.744), B2 flat (4 modes, v²=1/2 lock, V=0.256, 90.7% pairing, 2Δ=1.464), B3 optical (3 modes, V=0.003, 2Δ=0.168). Seven-frequency comb {0.070, 0.107, 0.168, 0.744, 1.430, 1.464, 8.27}. **NEW S87/S92**: Friedrich-Bär saturation certifies bottom-K invariance ∀ L≥10 (η_FB=0.547). **NEW S92/S93**: spectral dimension `d_s(σ)=−2 d ln P/d ln σ` — σ→0 Weyl limit = 8 = dim SU(3) (robust S31a→S89); windowed `d_s(σ_*≈1.40 M_KK⁻²)=8.4851` at the fold (S93 W7-3) is a DISTINCT functional; the `min d_s<3` van-Hove criterion was RETIRED (S93 W7-3 — graph-Laplacian Φ ≠ heat-trace Φ); discriminator moved to the energy-axis DOS exponent γ_E.

**(e) Spectral action** — `S=Tr f(D_K²/Λ²)`; `a_0/a_2/a_4` = CC/gravity/gauge (a_0=155984=total mode count, a_2=64308.24, a_4=29086.18 at L_max=10). dS/dτ|_fold=+58672.8 (>0), d²S/dτ²=+317862.8 (>0, convex), S(τ_fold)=250360.7 (speed bump). **NEW S82**: FI/RD/MIXED 42-row regulator-dressing taxonomy (FI=30/RD=4/MIXED=8; FI-identity subset 3) with TWO independent characterization functors M_lizzi + M_connes; algebra-INVARIANT vs algebra-DEPENDENT 4-corner classification (§VII.U.2). **DEEPENED via Baptista S60/S61**: a_2=(4π)⁻⁴·(20R/3)·Vol (Gilkey/Lichnerowicz, HEAT-KERNEL-A2-61, fixing a 38-session 8R/3 vs 20R/3 error) = (4π)⁴·Res_{s=3} ζ_{D_K²}(s) (Mellin route); MG-0 Mellin first-moment cone FI theorem.

**(f) Geometry bridges** — **ENTIRELY NEW since S84** (the §VII registry build-out is S86-S93). §VII.AF.1.OP-PROJ first LANDED cross-pillar bridge (S87 W5-1; Pillar III↔IV; HKR-image; 0.0095% F_4 at L_max=10; L⁻³ envelope; Level-3/Level-2=0.0950, 10× inside envelope). 5-anatomy (substrate-IS / lab-IN / bridge-map / envelope / anchor) + 3-level ladder MANDATORY at K=3 (Door-S86-CPB). §VII.BA composite bridge-map dimensional-class (S92): T1-T5 taxonomy; Wodzicki-trace deg −2s vs HKR cohomology-ratio deg 0; two-axis admissibility (homogeneity + substrate-natural-binding); `Δ_scheme→0` across APS-1975/Cheeger-Simons/Bismut-Cheeger (GV_APS=GV_CS=−1.2081580929e+08, machine-zero). Mellin-cone per-pole substrate-distance structure: s=3 (substrate-distance-1), s=4 (substrate-distance-2), s=−1 (IC slot).

**(g) Open structural questions** — τ_fold axiomaticity: **RESOLVED** by the van-Hove-cusp non-stationarity UNIQUENESS theorem §VII.M.W10-3 PERMANENT (S85 W10-3) — τ_fold=0.190 is no longer "the last empirical anchor" but a uniqueness-theorem-pinned value. L_max→∞: **RESOLVED structurally** by Friedrich-Bär saturation (bottom-K certified ∀ L≥10). cube-3 exponent "12": **STILL OPEN** (ζ-probe heat-kernel route §W9b-105 FAILed, d_spec=4.895/no two of d_a=0.153/d_b=9.32/d_c=12 agree; geometric su(2) geodesic-ball candidate at `s83-mu_BC-geometric-derivation.md`). rank-6: PROVISIONAL (78% biographical-framing survival; the 53 identities also partition into 5 canonical layers, §W8-91 PROVEN). A_F→SM coupling values + HP4 CC factor-3: still open. **NEW open axis**: α_s now carries TWO scale-separated substrate-IS observables (substrate-distance-1=−0.08587279 inside the BZ vs pivot-Goldstone≈0 at the CMB pivot, 54.04 decades apart; deg(T_BZ→pivot)=+2 NON-SCALAR resolved S93 W7-1).

#### GAP ANALYSIS — EXPANSION (E) gaps (the deliverable for G2)

| # | Domain gap (project knows; doc does NOT cover) | KB citation | Where it belongs |
|:--|:------------------------------------------------|:------------|:-----------------|
| E1 | τ_fold van-Hove-cusp UNIQUENESS theorem | §VII.M.W10-3 PERMANENT; gate `S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM` PASS | §4 + §12.1 (recast τ_fold from "last empirical anchor" → theorem-pinned) |
| E2 | Spectral-dimension d_s(σ) flow vs CDT | S92 `s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md`; S93 W7-3 gate (min_ds=7.7953, ds_σ_*=8.4851) | NEW §5.5 |
| E3 | Composite bridge-map dimensional-class theorem | §VII.BA S92; `GV_APS=GV_CS=−1.2081580929e+08` | NEW §7.6 |
| E4 | Mellin-cone per-pole substrate-distance structure | pole s=3/s=4/s=−1 (S85-S92); `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` INFO | DEEPEN §7.2 (MG-0) |
| E5 | Moduli-deformation substrate-IS geometry (Level-2) | §VII.AE/AD/AJ PERMANENT; 2.33× τ-asymmetry | NEW §3.4 |
| E6 | FI/RD/MIXED regulator-dressing taxonomy | S82 42-row (FI=30/RD=4/MIXED=8); M_lizzi+M_connes functors | DEEPEN §6 + §7.3/7.4 |
| E7 | Friedrich-Bär saturation theorem | S87 W11-2/W11-3; η_FB=0.547; CF-47 (S90); S92 W9-3 | DEEPEN §12.2 |
| E8 | LQG/CDT cross-framework comparison | `loop-quantum-gravity-phonon-exflation-comparison.md` (S92) | NEW §11.7/§12-xref |
| E9 | First LANDED cross-pillar bridges (§VII.AF.1+) | §VII.AF.1.OP-PROJ (S87 W5-1); Door-S86-CPB | NEW §7.6 (with E3) |
| E10 | α_s TWO scale-separated observables | `alpha_s_substrate_distance_1=−0.08587279` vs `alpha_s_pivot_goldstone≈0`; S93 W7-1 deg=+2 | DEEPEN §7.5 + §10.2 (the doc has ONE α_s; project now has two + the n_s²−1 identity form) |
| E11 | a_2 heat-kernel Gilkey 20R/3 (Lichnerowicz) | HEAT-KERNEL-A2-61 (S60/S61, Baptista-domain); a_2=(4π)⁻⁴·(20R/3)·Vol = (4π)⁴·Res_{s=3} ζ | DEEPEN §11.1 + §6 |
| E12 | 53 identities → 5 canonical layers | §W8-91 PROVEN {ALGEBRAIC 35, TOPOL 3, CAUSAL 3, ENERGETIC 7, TEMPORAL} | DEEPEN §7.1 or §12.4 (the rank-6 layer substrate) |

#### GAP ANALYSIS — QA-DRIFT (Q) gaps (the embedded QA pass for G2)

| # | Claim (as written) | Reconciliation | Class |
|:--|:-------------------|:---------------|:------|
| Q1 | A_F-Birkhoff "S84 §W8-87b PASS-THEOREM, 1/3,907" | The `value=16 FAIL` gate is the Witten-integral check; the PASS-THEOREM is W8-87b (rel_err=1.23e-15), NOW STAGE-3-PERMANENT (§VII.W-3.ALGEBRAIC, S88 W4a-17). Cite both; do not flip. | RECONCILE (the doc is correct; strengthen + disambiguate gate-ID) |
| Q2 | §13 "Proton decay at M_KK ~ 5 × 10¹⁷ GeV" vs §4 M_KK=7.43e16 | `M_KK_kerner=5.0417e17` is a DISTINCT canonical route (gauge-metric, Superseded=False); the default `M_KK=7.4287e16` is the gravity route. The §13 "~5×10^17" is NOT an error — disambiguate the two routes in-text. | DISAMBIGUATE (not a drift-fix; both routes canonical) |
| Q3 | "84 sessions / 1,600+ scripts / 112+ results" | Authorship-time (S84) snapshot; project is now S93-era. | REFRESH to S93-era |
| Q4 | τ-quartet (0.190/0.15/0.22/0.2117/...) | `tau_fold=0.19` canonical (NOT superseded); the others are DISTINCT quantities (horizon-τ, white-hole interior). | DISAMBIGUATE (verify each is the correct distinct quantity) |
| Q5 | 155,984 eigenvalues; "p+q ≤ L_max/2" | 155,984 = TOTAL (CORROBORATED `=card(spectrum L_max=10)`); 78,080 UNIQUE; correct index is `max(p,q) ≤ L_max`. | DISAMBIGUATE + add 78,080-unique note + fix index convention |
| Q6 | §8.3 cube-3 "12" exponent | STILL genuinely OPEN S93; heat-kernel ζ-probe route FAILed at S85 (d_spec=4.895). | UPDATE-OPEN (failed-route record + geometric candidate) |
| Q7 | §11.x cosmology values (CC, Ω_DM, f_NL, w_0, r) | Cosmology-domain; W3 (`Phononic-to-Cosmos.md`) owns the comprehensive treatment. | SCOPE-OUT to W3 (verify one-liners current; cross-reference) |

**Additional Q-find surfaced by survey** (folds into G2 QA): the Higgs §8.2 "tree 97 GeV → 125 GeV, residual 2.41 GeV" mixes three KB values — 97 (S83 gear-machine tree), 134 (filter-independent tree, A10), 127.5–131.8 (Aitken-Gaussian framework central, S62-S66). The Higgs is ACCOMMODATION-FLAGGED (falsifier-rigor-registry), not a clean prediction. G2 must reconcile §8.2 to the framework central 131.8 GeV with the accommodation caveat. Tagged **Q8 (Higgs reconcile)**.

---

### §W2-2. WX-W2-2-COMPREHENSIVE-EXPANSION (tesla-resonance)

**Status**: COMPLETED
**Gate ID**: `WX-W2-2-COMPREHENSIVE-EXPANSION`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (the deliverable: integrate post-S84 geometry into Phononic-Substrate-Geometry.md in authorial voice)
**Agent**: `tesla-resonance`
**Hypothesis**: Phononic-Substrate-Geometry.md can be substantially expanded — in Tesla-Resonance's authorial voice, with the IS-not-IN direction restored — so that every material EXPANSION gap row from G1 is integrated (new geometry sections for post-S84 results; deepened spectral-triple/moment treatment; new bridges) OR explicitly scoped-out with a one-line reason, and the document reads as a current (S93-era) comprehensive synthesis of the whole-project substrate-geometry domain.
**Plan reference**: `sessions/session-plan/session-x-plan-w2.md` §W2-2 (gap-integration target, comprehensive floor ≥4 new + ≥3 deepened + ≥3 recast/QA, two worked substitution chains, PASS/FAIL rubric).

**Output Artifacts** (closure-verification checklist):
- (1) script `computations/session-x/sx_w2_comprehensive_expansion.py` — PRESENT. `grep -E 'from canonical_constants import|append_verdict'` → `from canonical_constants import *`, `from canonical_constants import (`, `def append_verdict(...)`, `append_verdict(verdict, value_str, ...)`. ✓
- (2) data `computations/session-x/sx_w2_comprehensive_expansion.npz` — PRESENT (integration ledger + floor counts). ✓
- (3) plot `.png` — N/A (optional; expansion gate).
- (4) verdict line `^WX-W2-2-COMPREHENSIVE-EXPANSION:.* audit_sha256=[a-f0-9]{64}` → PRESENT, `audit_sha256=6d9c2edad34f009cdcdaf99e0cfa1f8e133e3b6225c3e53ff81a818a4d689852`, `content_sha256=ec79a25f52aaf1a6a6afbf4618c4ab81d302dc5e5ff9b86273b4578f13c069cb`; companion dual-SHA comment row PRESENT. ✓
- (5) EXPANDED DOCUMENT `sessions/framework/Phononic-Substrate-Geometry.md` — must_contain `5.5`, `7.6`, `spectral dimension`, `Friedrich-B` all PRESENT (19 marker matches); grew 62,470 B → 100,450 B (+37,980 B, +61%). ✓
- (6) this WP §W2-2 section — `**Status**: COMPLETED`, all blocks populated. ✓

**MCP Pre-Compute Audit**: The full ~24-query knowledge-MCP manifest was fired at G1 (§W2-1) and is the binding source-of-truth for every gap row's citation. At G2 integration time each gap row's KB citation was re-resolved from the G1 state-of-domain map (carried in `sx_w2_aggregate_domain_survey.npz`): E1→§VII.M.W10-3 PASS (gate `S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM`); E2→`s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md` + S93 W7-3 gate; E3+E9→§VII.BA + §VII.AF.1; E4→Mellin pole s=3/s=4/s=−1; E5→§VII.AE/AD/AJ; E6→S82 42-row; E7→S87 W11-2/W11-3 + S92 W9-3; E8→`loop-quantum-gravity-phonon-exflation-comparison.md`; E10→`alpha_s_substrate_distance_1` vs `alpha_s_pivot_goldstone` + S93 W7-1; E11→HEAT-KERNEL-A2-61 (S60/S61); E12→§W8-91. Constant currency re-verified at write-time via `get_constant`: M_KK=7.4287e16, M_KK_kerner=5.0417e17, tau_fold=0.19, alpha_s_substrate_distance_1=−0.08587279, alpha_s_pivot_goldstone=0.0. Two substitution chains Sage-confirmed exact (see below). PRE-CLOSED: NONE (expansion gate; mines closed results read-only, does not re-gate).

**Verdict**: **INFO** — `value='new_sections=4;deepened=5;recast_QA=9;chains=2;doc_pre_B=62470;doc_post_B=100450;floor_met=True;chains_met=True;scoped_out_to_W3=Q7_cosmology'`. The comprehensive floor is met decisively (4 NEW ≥ 4, 5 DEEPENED ≥ 3, 9 RECAST/QA ≥ 3, both substitution chains present), the document grew +61%, and the deliverable is realized — the doc is no longer a post-S84 snapshot but a whole-project S93-era geometry synthesis. The INFO (vs PASS) records the single bounded scope-out per the plan's INFO_meaning: Q7 (comprehensive cosmology) is forward-pointed to W3 `Phononic-to-Cosmos.md` with current one-liners retained + a §11 scope note (NOT integrated comprehensively here, by design — cosmology-observable detail is W3's document).

**Results** — EXPANSION INTEGRATION LEDGER:

#### Comprehensive-floor verification (all markers grepped on-disk in doc_post)

| Floor category | Required | Achieved | Members (all PRESENT on-disk) |
|:---------------|:---------|:---------|:------------------------------|
| NEW sections | ≥ 4 | **4** | §3.4 (E5 moduli geometry), §5.5 (E2 d_s flow), §7.6 (E3+E9 bridge maps), §11.7 (E8 LQG/CDT) |
| DEEPENED sections | ≥ 3 | **5** | §7.2 (E4 per-pole), §6/§11.2/§7.3 (E6 FI/RD/MIXED), §6 (E11 a_2 Gilkey 20R/3), §12.2 (E7 Friedrich-Bär), §12.4 (E12 5-layer partition) |
| RECAST/QA edits | ≥ 3 | **9** | §12.1 (E1 τ_fold resolved), §3.1 (Q1 A_F), §4 (Q2 M_KK two-route), §0/§14 (Q3 counts), §5.1/§1.1 (Q5 index+78,080), §12.3 (Q6 cube-3), §11/§7.5 (Q7 cosmology scope), §8.2 (Q8 Higgs accommodation), §7.5 (E10 α_s two-observable) |
| Substitution chains | 2 | **2** | EXAMPLE A (d_s σ→0=8), EXAMPLE B (Wodzicki/HKR degree) |

#### Per-gap integration ledger

| Gap | Disposition | §-anchor | KB citation |
|:----|:------------|:---------|:------------|
| E1 | INTEGRATED (recast) | §4, §12.1, §14, App.A/B | §VII.M.W10-3 PERMANENT (proven_1504) |
| E2 | INTEGRATED (new §5.5) | §5.5 | S92 d_s workshop + S93 W7-3 gate |
| E3 | INTEGRATED (new §7.6) | §7.6 | §VII.BA; GV_APS=GV_CS=−1.2081580929e8 |
| E4 | INTEGRATED (deepen §7.2) | §7.2 | Mellin pole s=3/s=4/s=−1; S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE |
| E5 | INTEGRATED (new §3.4) | §3.4 | §VII.AE/AD/AJ PERMANENT; 2.33× asymmetry |
| E6 | INTEGRATED (deepen §6+§7.3+§11.2) | §6, §7.3, §11.2 | S82 42-row FI=30/RD=4/MIXED=8 |
| E7 | INTEGRATED (recast §12.2) | §12.2 | S87 W11-2/W11-3; η_FB=0.547; S92 W9-3 |
| E8 | INTEGRATED (new §11.7) | §11.7 | `loop-quantum-gravity-phonon-exflation-comparison.md` |
| E9 | INTEGRATED (new §7.6) | §7.6 | §VII.AF.1.OP-PROJ (S87 W5-1); Door-S86-CPB |
| E10 | INTEGRATED (deepen §7.5) | §7.5, App.A | `alpha_s_substrate_distance_1` vs `_pivot_goldstone`; S93 W7-1 |
| E11 | INTEGRATED (deepen §6) | §6 | HEAT-KERNEL-A2-61 (S60/S61, Baptista cross-consult); 20R/3 Lichnerowicz |
| E12 | INTEGRATED (deepen §12.4) | §12.4 | §W8-91 5-layer partition PROVEN |
| Q1 | RECONCILED | §3.1, App.A | value=16 FAIL gate vs W8-87b PASS-THEOREM; §VII.W-3 STAGE-3-PERMANENT (S88) |
| Q2 | DISAMBIGUATED | §4, §13, App.A | M_KK_gravity=7.4287e16 vs M_KK_kerner=5.0417e17 (both canonical) |
| Q3 | REFRESHED | §0, §14 | ~93 sessions / 1,800+ scripts / 1,500+ results (proven_1500+) |
| Q4 | DISAMBIGUATED | §4 | tau_fold=0.19 canonical (NOT superseded); quartet are distinct quantities |
| Q5 | DISAMBIGUATED | §5.1, §1.1, §14, App.A | 155,984 total / 78,080 unique; `max(p,q)≤L_max` (index fixed) |
| Q6 | UPDATE-OPEN | §8.3, §12.3, §11.7 | cube-3 "12" STILL OPEN; ζ-route FAILed d_spec=4.895; geometric candidate |
| Q7 | SCOPED-OUT → W3 | §11 scope note, §7.5 | cosmology-observable detail is W3 `Phononic-to-Cosmos.md` |
| Q8 | RECONCILED (Higgs) | §8.2 | m_H=131.8 framework central; ACCOMMODATION-FLAGGED; filter-indep tree 134 |

#### SUBSTITUTION CHAIN — EXAMPLE A (d_s spectral dimension σ→0 = manifold dimension; §5.5; Sage-exact)

```
Def 1: P(σ→0) ~ C σ^{−d/2}                 [Weyl asymptotic; C const, d = manifold dimension]
Def 2: d_s(σ) = −2 d ln P / d ln σ           [spectral dimension]
Substitute: ln P = ln C − (d/2) ln σ;  d ln P/d ln σ = σ·d(ln P)/dσ = −d/2   [Sage simplify_full → −d/2]
Simplify:  d_s(σ) = −2·(−d/2) = d            [Sage simplify_full → d]
Canonical: d_s(σ→0) = d = dim(SU(3)) = 3²−1 = 8
Direction: σ→0 Weyl spectral dim = manifold dim 8; windowed d_s(σ_*)=8.485 is a DISTINCT functional
Conclusion: cavity reads 8-dimensional to a sharp heat-kernel probe; CDT comparison MUST use the SAME
            functional Φ at the SAME scale-type (phononic-framing.md fair-comparison rule). [Sage-confirmed]
```

#### SUBSTITUTION CHAIN — EXAMPLE B (Wodzicki vs HKR homogeneity degree → composite bridge admissibility; §7.6; Sage-exact)

```
Def 1: deg(Wodzicki-trace factor at pole s) = −2s    [Wodzicki uniqueness; Connes 1994 §2.3]
Def 2: deg(HKR cohomology-class ratio)      = 0       [orientability axiom + Chern character]
Substitute: composite B = f⊙g admissible iff deg(B) = d_A   [d_A = Level-3 anchor homogeneity]
Simplify:  Wodzicki carries −2s (≠0 ∀ s>0: Sage at s=1,2,3,4 → −2,−4,−6,−8); HKR carries 0
Direction: T1 (trace×ratio, deg −2s) FORBIDDEN at deg-0 anchor; T3 (ratio/ratio, deg 0) ADMISSIBLE;
           T4 (Wodzicki/Wodzicki s≠s', deg 2(s′−s)) ADMISSIBLE, T4|_{s=s'} ≡1 VACUOUS
Conclusion: bridge degree must match anchor by a substrate-natural NON-SCALAR morphism; a canonical-import
            scalar is VACUOUS. Operational test: Δ_scheme→0 across APS/CS/BC (GV_APS=GV_CS, machine-zero).
            [Sage-confirmed]
```

α_s two-observable check (§7.5; Sage-exact, bit-confirmed): Planck pivot n_s=0.9649 → α_s=n_s²−1 = −6896799/100000000 = −0.068968; substrate-distance-1 a_4/a_2=0.9561 → −8587279/100000000 = −0.08587279 (9561²=91412721 perfect square). Same X²−1 polynomial, two scales 54.04 decades apart; deg(T_BZ→pivot)=+2 NON-SCALAR (S93 W7-1).

---

### §W2-3. WX-W2-3-RECONCILE-VERIFY (tesla-resonance)

**Status**: COMPLETED
**Gate ID**: `WX-W2-3-RECONCILE-VERIFY`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (QA over expanded document: DEFECT_SET = {stale ∪ unframed ∪ untraced ∪ untagged}, PASS = empty)
**Agent**: `tesla-resonance`
**Hypothesis**: After the G2 expansion, every claim in Phononic-Substrate-Geometry.md (retained + newly added) is current (matches canonical_constants / permanent theorems / closed mechanisms / gate verdicts), framing-compliant (IS-not-IN per phononic-framing.md), provenance-traced (each quantitative claim sourced to a canonical-constants entry / permanent theorem / closed mechanism / gate verdict), and a_n^{regulator}-tagged where a Seeley-DeWitt coefficient is cited.
**Plan reference**: `sessions/session-plan/session-x-plan-w2.md` §W2-3 (4-axis verification, DEFECT_SET operator, tolerance rule rel_tol ≥ 10^(−sig_figs), α_s belt-drive re-verification substitution chain, PASS/FAIL rubric).

**Output Artifacts** (closure-verification checklist):
- (1) script `computations/session-x/sx_w2_reconcile_verify.py` — PRESENT. `grep -E 'from canonical_constants import|append_verdict'` → `from canonical_constants import *`, `from canonical_constants import (`, `def append_verdict(...)`, `append_verdict(verdict, value_str, ...)`. ✓
- (2) data `computations/session-x/sx_w2_reconcile_verify.npz` — PRESENT (4-axis pass flags + DEFECT_SET cardinality + legit-open items). ✓
- (3) plot `.png` — N/A (optional; verification gate).
- (4) verdict line `^WX-W2-3-RECONCILE-VERIFY:.* audit_sha256=[a-f0-9]{64}` → PRESENT, `audit_sha256=bbde8552ee1c05df6f7b568cf8f236981f8ffd7b7f94b7368b3e8395ea441e57`, `content_sha256=aa376ac6440f53a1ac3afa00f597a936e0017442b7aac0b2a27e12a32a0c314d`; companion dual-SHA comment row PRESENT. ✓
- (5) this WP §W2-3 section — `**Status**: COMPLETED`, all blocks populated. ✓

**MCP Pre-Compute Audit**: QA cross-checks were run against the canonical-constants snapshot (the binding currency source) and the G1 query manifest (§W2-1). Per-axis salient returns: `get_constant("M_KK")` → 7.4287e16 (§4/§13 current); `get_constant("M_KK_kerner")` → 5.0417e17 (§13 proton-decay scale, distinct route); `get_constant("tau_fold")` → 0.19 (§4 current; theorem-pinned §VII.M.W10-3); `get_constant("Delta_BCS")` → 0.4642547 (§4 current); `get_constant("dS_fold")` → 58672.80 (§6.3 current); `get_constant("alpha_s_substrate_distance_1")` → −0.08587279 (§7.5 current); `get_constant("alpha_s_pivot_goldstone")` → 0.0 (§7.5 current); `get_constant("planck_ns")` → 0.9649, `get_constant("n_s_framework")` → 0.9561 (§10.2 distinction verified); α_s belt-drive identity re-verified Sage-exact (chain below); `trace_entity("A_F Birkhoff uniqueness")` → verdict-vs-theorem disambiguation present in §3.1 doc_post. PRE-CLOSED: NONE.

**Verdict**: **PASS** — `value='defect_set_cardinality=0;CURRENT=True;FRAMED=True;TRACED=True;TAGGED=True;legit_open_stated_as_open=3(cube3+couplings+HP4)'`. The expanded document carries zero stale claims, zero container-thinking violations, zero untraced quantitative claims, and zero bare-a_n Seeley-DeWitt VALUE citations. The QA layer over the deliverable is closed. (The three legitimately-OPEN items — cube-3 "12", A_F→SM coupling values, HP4 CC factor-3 — are correctly stated AS open in doc_post, which is framing-compliant-OPEN per the plan's INFO_meaning, NOT a defect; hence PASS rather than INFO.)

**Results** — PER-CLAIM DEFECT-SET LEDGER:

#### AXIS 1 — CURRENT (canonical-value match; 11/11 PASS, 0 stale)

| Claim | doc value | canonical | tolerance (Class-8.3) | CURRENT |
|:------|:----------|:----------|:----------------------|:--------|
| M_KK (gravity) | 7.43 × 10¹⁶ | 7.4287e16 | 3 sig figs (rel_tol 1e-3) | Y |
| M_KK_kerner | 5.0417 × 10¹⁷ | 5.0417e17 | 5 sig figs | Y |
| τ_fold | 0.190 | 0.19 | exact | Y |
| Δ_BCS | 0.4643 | 0.4642547 | 4 sig figs | Y |
| dS/dτ\|fold | +58,673 | 58672.80 | 5 sig figs | Y |
| α_s^{substrate} | −0.08587279 | −0.08587279 | bit-exact | Y |
| α_s^{pivot} (n_s²−1) | −0.068968 | −0.06896799 | bit-exact | Y |
| n_s_FW | 0.9561 | 0.9561 | exact | Y |
| planck_ns | 0.9649 | 0.9649 | exact | Y |
| eigenvalues total | 155,984 | 155984 | exact | Y |
| eigenvalues unique | 78,080 | 78080 | exact | Y |

Stale-claim scan: `97→125 residual 2.41 GeV` (0 live), `S85 5.8 pending` (0 live), `last remaining empirical anchor as live assertion` (0 live). The historical "at authorship this was called…" references in §12.1/§4-update are framing-compliant (describing what the framework USED to say before stating the resolution), NOT live stale claims.

#### AXIS 2 — FRAMED (IS-not-IN; 0 container-thinking violations, 5/5 positive markers)

Container-assertion scan: `substrate lives/sits in spacetime` (0), `fields on K asserted` (0), `BEC IS the substrate` (0), `particles created in curved spacetime` (0). The one near-match (§5.5 "not a property of an ambient container the substrate sits in") is in the CORRECTIVE direction — it is the IS-not-IN reframe, framing-compliant. Positive markers present 5/5: "IS, Not IN", "substrate IS the resonator", "IS-not-IN", "not a property of an ambient container", "Substrate (Pillar A) IS". Every new section flows substrate → emergent physics.

#### AXIS 3 — TRACED (12/12 provenance pointers present)

§VII.M.W10-3 (τ_fold thm) ✓ | §VII.W-3.ALGEBRAIC (A_F STAGE-3) ✓ | S93 W7-3 (d_s gate) ✓ | §VII.BA (composite bridge) ✓ | §VII.AF.1 (first bridge) ✓ | §VII.AE (moduli asymmetry) ✓ | S87 W11-2/W11-3 (Friedrich-Bär) ✓ | S82 42-row (FI/RD/MIXED) ✓ | HEAT-KERNEL-A2-61 (a_2 Gilkey) ✓ | §W8-91 (5-layer) ✓ | S93 W7-1 (α_s degree) ✓ | loop-quantum-gravity-phonon-exflation-comparison.md (LQG doc) ✓.

#### AXIS 4 — TAGGED (5/5 regulator-tag markers; bare-a_n VALUE citations resolved)

`a_2^{ζ}` ✓ | `a_4^{ζ}` ✓ | §6.2 "Regulator-class note, per regulator-pin-discipline.md" disclosure ✓ | MG-0 first-moment-cone FI-INVARIANT note ✓ | "a_0 = total mode count, a count rather than a regulated value" ✓. The object-reference a_n symbols (§6.2 moments table, §11.1 headers, proportionalities) are covered by the §6.2 regulator-class disclosure; the only NUMERICAL Seeley-DeWitt VALUE citations (§6.1) carry explicit ζ tags; the load-bearing `a_4/a_2` ratio is noted FI-class regulator-INVARIANT.

#### SUBSTITUTION CHAIN re-verification — α_s belt-drive (Sage-exact, bit-confirmed)

```
Def 1: u = m²/(J K²)                              [Ornstein-Zernike single-pole]
Def 2: P(K) = T/[J K² + m²]                       [scalar power spectrum]
Substitute: n_s − 1 = d ln(K³P)/d ln K = −2/(1+u)
Simplify:   α_s = d(n_s−1)/d ln K = −4u/(1+u)²
Canonical:  (n_s−1)(n_s+1) = α_s = n_s² − 1        [identically, n_aux=0]
Direction:  at Planck pivot n_s=0.9649 ⇒ α_s = 0.9649²−1 = −6896799/100000000 = −0.068968  [Sage-exact]
            at substrate s=3 a_4/a_2=0.9561 ⇒ α_s = 0.9561²−1 = −8587279/100000000 = −0.08587279
                                                  (9561²=91412721 perfect square; bit-exact)  [Sage-exact]
Conclusion: identity current S93 (S84 §W8-86 PASS-THEOREM, §W10-123 n_aux=0); doc "−0.068968"/"−0.069"
            matches n_s²−1 to publication precision; the SECOND substrate-distance-1 reading −0.08587279
            is the distinct in-BZ observable, 54.04 decades away (S93 W7-1 deg=+2 NON-SCALAR).
```

The two G2-added directional chains (EXAMPLE A d_s σ→0=8; EXAMPLE B Wodzicki deg −2s vs HKR deg 0) were re-verified against the §5.5 / §7.6 inline chains and the Sage runs at G2 — both consistent.

#### DEFECT_SET

```
stale            = []
unframed         = []
untraced         = []
untagged         = []
current_missing  = []
|DEFECT_SET|     = 0
```

QA-layer remediations applied during this gate (fix-in-session, NOT iterate-until-PASS — each was an enumerated defect, fixed, re-verified): (i) §4 intro "one remains empirical pending S85 5.8" → "S85 W10-3 closed that gap" (last live stale τ_fold-pending claim); (ii) §10.2 "n_s=0.9649 (matching Planck)" → distinguished n_s_FW=0.9561 (framework) from planck_ns=0.9649 (observational) + cross-ref to §7.5 two-observable structure; (iii) §6.2 added explicit regulator-class disclosure note covering the object-reference a_n symbols. Legitimately-OPEN items correctly stated as open (not defects): cube-3 "12" (§12.3), A_F→SM coupling values (§12.5), HP4 CC factor-3 (§12.6).

---

## Wave W2 Synthesis (team-lead)

*(Written after all 3 gates complete. Structure per `sessions/archive/session-84/session-84-w1-workingpaper.md:1040–1095`. Sections: process observations (closed in-session) | constraint-map updates (state changes from this wave's verdicts) | carry-forward computations (genuine future-work items with 4-field specs).)*

## Carry-Forward Computations

*(Written at wave close. One `### {CF-ID} — {one-line title}` sub-heading per genuine future-work item, each with a 4-field-spec table (What / Inputs / Gate / Effort). Per `CLAUDE.md §"No Technical Debt"` + `feedback_fix-in-session-never-defer.md`: hygiene observations on already-correct artifacts are NOT carry-forwards. Empty is acceptable if the wave produced zero genuine future-work items.)*

## Constraint-Map Updates

*(One row per state change. Columns: Date | Mechanism/gate | Prior state | New state | Reason.)*

| Date | Mechanism / Gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| *(pending)* | *(pending)* | *(pending)* | *(pending)* | *(pending)* |

## Files Produced

*(One row per artifact. Columns: Gate | Script | Data (.npz) | Plot (.png) | Document | Note.)*

| Gate | Script | Data (.npz) | Plot (.png) | Document / Other | Note |
|:-----|:-------|:------------|:------------|:-----------------|:-----|
| `WX-W2-1-AGGREGATE-DOMAIN-SURVEY` | `computations/session-x/sx_w2_aggregate_domain_survey.py` | `computations/session-x/sx_w2_aggregate_domain_survey.npz` (optional) | — | — | Survey + gap-analysis artifact; intra-wave G2 input |
| `WX-W2-2-COMPREHENSIVE-EXPANSION` | `computations/session-x/sx_w2_comprehensive_expansion.py` | `computations/session-x/sx_w2_comprehensive_expansion.npz` (optional) | — | `sessions/framework/Phononic-Substrate-Geometry.md` (EXPANDED) | The deliverable |
| `WX-W2-3-RECONCILE-VERIFY` | `computations/session-x/sx_w2_reconcile_verify.py` | `computations/session-x/sx_w2_reconcile_verify.npz` (optional) | — | — | Per-claim defect-set ledger in WP §W2-3 |
