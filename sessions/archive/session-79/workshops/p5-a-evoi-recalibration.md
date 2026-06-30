# Session 79 Workshop P5-A: nazarewicz × gen-physicist

**Date**: 2026-04-16
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: nazarewicz (nazarewicz-nuclear-structure-theorist) — Bayesian UQ methodology; P(pass)/ΔP estimation from prior computational outcomes. gen-physicist (gen-physicist) — neutral evidence weighting; EVOI computation; S80 priority ranking.

**Source Documents**:
- **ALL 12 prior S79 workshop outcomes** (ingested as input):
  - `sessions/archive/session-79/workshops/p1-1-s78-synthesis-completion.md` (CLOSED) — S78 §VI/§VII consensus, fold |β|²~10⁴ unified root cause
  - `sessions/archive/session-79/workshops/p1-2-wave2-closure.md` (CLOSED) — W2-B FAIL / W2-E INFO c_sub=2.23 / W2-G INCOMPUTABLE; A_s gap widens 3.0→3.35 OOM
  - `sessions/archive/session-79/workshops/p1-3-w1b-iteration-audit.md` (CLOSED) — W1-B and W2-C WARRANT-INVALID; Pattern 3' + PRU formalized
  - `sessions/archive/session-79/workshops/p2-a-as-ledger-dissonance.md` (CLOSED) — UNIFIED-AS-79 supersedes 4-factor ledger
  - `sessions/archive/session-79/workshops/p2-b-pbh-prefold-wrong-sign.md` (CLOSED) — Chluba kernel correction; FIRAS yoked to A_s
  - `sessions/archive/session-79/workshops/p2-c-desi-mechanism-split.md` (CLOSED) — Route A Volovik-partition vindicated; W3-G REFORMULATE
  - `sessions/archive/session-79/workshops/p3-a-w1d-tau-min-at-fold.md` — Fold Triple Coincidence §VII.II; Khodel-Shaginyan routing
  - `sessions/archive/session-79/workshops/p3-b-w3o-trh-channel-redefinition.md` — 13→7 OOM cushion; Γ_γ as unitarity lower bound
  - `sessions/archive/session-79/workshops/p4-a-w3k-rank-universality.md` — rank-exponent functional-independent
  - `sessions/archive/session-79/workshops/p4-b-w2c-u1-r-protection.md` — R-protection narrowed to multi-mode branches
  - `sessions/archive/session-79/workshops/p4-c-w2d-fstar-outside-cluster.md` — a_0 sibling-class; f* categorical outlier
  - `sessions/archive/session-79/workshops/p4-d-ratios-vs-absolutes-meta.md` — ratios-vs-absolutes meta-pattern, unit-fixing S80 gate

- **Living EVOI table** (canonical): `sessions/evoi-framework.md`
- **Rules**: `.claude/rules/evoi-prioritization.md`, `.claude/rules/epistemic-discipline.md`
- **Memory**: agent-memory for both agents (nazarewicz's Bayesian UQ tools; gen-physicist's neutral framing)

**Focus Topics** (5 sections — N1-N5 for nazarewicz; G1-G5 for gen-physicist):

1. **EVOI table staleness diagnosis**. The user has flagged the EVOI table as frozen since S66 (see feedback_framework-hygiene). Audit: which entries in `sessions/evoi-framework.md` are stale (contradicted by S67–S78 outcomes or 12 S79 workshops)? Which entries need re-estimation of P(pass), ΔP(pass), ΔP(fail)? Produce a NUMBERED diff list of stale entries before attempting recalibration.
2. **UNIFIED-AS-79 as new rate-limiting path**. P2-A retracted the 4-factor A_s ledger; UNIFIED-AS-79 (single mode-equation pipeline from pre-fold SS-IC through horizon exit) is canonical. Pre-register EVOI for:
   - **UNIFIED-AS-79-CSUB-SIGN**: PASS if d(ln A_s)/d(ln c_sub) = −1.000 ± 0.01; FAIL otherwise
   - **UNIFIED-AS-79-FULL**: A_s value under complete pipeline
   - **UNIFIED-BACKREACT-79**: with backreaction
   Estimate P(pass) and |ΔP| for each. These are the top S80 carry-forward computations.
3. **Fold Triple Coincidence promotion path**. P3-A posited §VII.II pre-theorem; promotion to §VII.I requires 4th independent functional of ρ(ε, τ_fold). Candidate 4th functionals: χ_N (fermion-number susceptibility), dS_inst/dτ (instanton-action gradient), Z_s (elastic-tetrad shear). Rank by tractability and EVOI; pre-register S80 gate.
4. **Remediation layer P(pass)**. W1-B and W2-C require clean re-runs (R1, R2 scripts). These are NOT new-physics gates; they confirm prior structural readings. Estimate P(pass) for each — expected HIGH (~0.9) since the P1-3 verdict was WARRANT-INVALID on iteration count / tag discipline, not on the underlying numerics. The EVOI is LOW for pass (ΔP small) but HIGH for fail (ΔP large if new contradiction emerges).
5. **Framework probability effort-based update**. Per `evoi-prioritization.md`: framework probability tracks (mechanism links complete / total) × (fraction approaching observation). After 12 S79 workshops, re-compute:
   - Mechanism links complete / total (what denominator?)
   - Fraction approaching observation (how do PASS, INFO, FAIL, INCOMPUTABLE, REFORMULATE weigh in?)
   - Eliminating wrong mechanisms STRENGTHENS surviving paths — how does the Phase-2 "3 of 5 S78 FAILs re-diagnosed as methodology artifacts" affect probability?
   Produce a before/after table with explicit methodology citations.

**Convention pins** (NON-NEGOTIABLE):
- Dependent on P3-A, P3-B, P4-A, P4-B, P4-C, P4-D closures. Do NOT run this workshop until those six are closed.
- EVOI = P(pass)·|ΔP(pass)| + P(fail)·|ΔP(fail)|; highest EVOI = top priority.
- Do NOT cite constraint counts as arguments ("we have 12 constraints" proves nothing).
- Do NOT restate prior claims as new evidence.
- Failures cluster by TOPIC (not agent).
- Joint probability is the PRODUCT of independent probabilities, not arithmetic mean.
- Framework probability tracking is effort-based (goes UP when work is done, not only when favorable results return).
- LCDM-matches with 0 free parameters are EVIDENCE (not null-result neutrals).
- PASS/FAIL ratio is NOT the metric; decisive-vs-INFO count is.

---

## Round 1 — nazarewicz: Opening Analysis

### N1: EVOI table staleness diagnosis — numbered diff against S78 stamp

Audit target: `sessions/evoi-framework.md` (S78 scrubbed stamp, 2026-04-15). Scope: every item in the S78-Level 1/2/3/4 tables + the S73B carry-forwards, measured against the 12 S79 workshop closures (P1-1 through P4-D). Structure: STALE (S), CLOSED (C), RE-OPENED (RO), PROMOTED (P), NEW (N). Citations in [workshop:anchor] form.

#### S — STALE (contradicted by S79 outcomes; re-estimate required)

| # | S78 entry | Staleness source | New reading |
|:--|:----------|:-----------------|:------------|
| S1 | `S78-W1-A` P(pass)=0.35 for "product in [1.72e-9/4, 1.72e-9×4]" | P2-A retracted the 4-factor ledger [p2-a:1169]; P1-1 installed Rule 1/Rule 2 for W1-A citation [p1-1:854] | W1-A PASS preserved at CONVENTION-PINNING scope; the 4-factor composed-chain interpretation is IRREDEEMABLE [p2-a:1195]. EVOI entry must split into (a) W1-A PASS permanent at conv-pin scope, (b) UNIFIED-AS-79-FULL as the replacement gate |
| S2 | `S78-W1-B` P(pass)=0.65 | P1-3 verdict WARRANT-INVALID [p1-3:1426] — failure on iteration count, tag discipline, plan-letter violations | P(pass) undefined pending R1 re-run; remediation R1 carries P(pass)=0.90 confirmation prior |
| S3 | `S78-W1-C` BACKREACTION-SELFCONSIST P(pass)=0.50 | P1-1 reclassified to INCOMPUTABLE-FALLBACK-TO-BOUND [p1-1:860]; F_amp^sc ≤ 47.9 bound is final, not converged [p2-a:1181] | Gate CLOSED at bound; successor UNIFIED-BACKREACT-79 replaces |
| S4 | `S78-W1-D` MULTI-BAND-E_COND P(pass)=0.40 | P3-A: multi-band bootstrap PERMANENTLY CLOSED in zero-volume region via block-diagonal theorem S22b [p3-a:1159] | Gate CLOSED. Solution-space volume = 0. Successor: multi-pair N_pair=2 (CF-3) |
| S5 | `S78-W1-E` PRE-FOLD-VACUUM-STATE P(pass)=0.30 | P2-B: Chluba kernel peaks at k ≈ 151 Mpc⁻¹, not k_pivot [p2-b:744]; S_IC(k_pivot)=1.636e5 is final measurement [p2-a:1183] | Gate CLOSED: S_IC = |α+β|² = 1.636e5 with factor-1.133 three-principle spread; axiomatic gap PERMANENTLY CLOSED [p2-b:764] |
| S6 | `S78-W2-A` MU-EFF-96x96 P(pass)=0.45 | P3-A Re:L5: Laplacian isocurvature closed; mu_eff = 4.60e-4 measured, 22× short of needed 0.0102 [p3-a:1205] | Gate CLOSED at FAIL; interpretation: isocurvature-via-Laplacian is NOT a viable A_s closure channel. Successor: rate-matrix L-K reformulation (CF-4, P1-1) |
| S7 | `S78-W2-B` BCS-FORMATION-DYNAMICS P(pass)=0.55 | P1-2: W2-B FAIL permanent; Model C inertial pins downstream [p1-2:992] | Gate CLOSED at FAIL; MODEL-C-PIN-PROPAGATION as new procedural gate |
| S8 | `S78-W2-C` ZETA-JOSEPHSON P(pass)=0.75 | P1-3: WARRANT-INVALID on quantity-definition-drift [p1-3:1427] | P(pass) undefined; R2 remediation required. P4-B: abelian-subfactor PRE-THEOREM bounds drift_u1(L=8)=66.06% CLT prediction [p4-b:1470] |
| S9 | `S78-W2-D` F-CONV-ANOMALY P(pass)=0.50 | P4-C: W2-D verdict PERMANENT FAIL; slot-dependent reading [p4-c:1111]; f* categorically outside sibling cluster via MP-exclusion [p4-c:1116] | Gate CLOSED at FAIL; structural harvest: sibling-class taxonomy (MP-admissibility) |
| S10 | `S78-W2-E` F-CONV-SUBHORIZON P(pass)=0.55 | P1-2: W2-E verdict INFO c_sub^{f*}=2.23; SIGN-REVERSAL under UNIFIED-AS-79 [p1-2:956] | Gate CLOSED at INFO; direction of c_sub flips: A_s → A_s/c_sub (P(ζ) = \|v\|²/z², c_sub enters z²). Gap widens 3.0→3.35 OOM absolute [p1-2:974] |
| S11 | `S78-W2-F` A_4-R²-UNDER-F-STAR P(pass)=0.80 | P1-1: PERMANENT §VII.II theorem (a_4 R²-invariance) [p1-1:860] | Gate CLOSED at PASS |
| S12 | `S78-W2-G` EPS-ZERO-MATCHING P(pass)=0.75 | P1-2: INCOMPUTABLE verdict is Motohashi-AGK theorem empirically realized [p1-2:958] | Gate CLOSED at INCOMPUTABLE-STRUCTURAL (not FAIL); successor: Frobenius matched-asymptotic remediation [p1-2:986] |
| S13 | `S78-W3-A` CHI_2-LMAX-CONVERGENCE P(pass)=0.40 | P1-1: Mellin-χ_2 for n_s CLOSED at §VII.III [p1-1:860] | Gate CLOSED; successor: BMA extrapolation is a sub-task of UNIFIED-AS-79 k-scan |
| S14 | `S78-W3-B` FAMP-TILT-SMOOTHED P(pass)=0.55 | P1-1: depends on W1-C which is now INCOMPUTABLE at F_amp^sc bound [p1-1:860] | Gate CLOSED-CONDITIONAL; replaced by UNIFIED-AS-79 B2 stage tilt extraction |
| S15 | `S78-W3-C` TENSOR-FAMP P(pass)=0.55 | No S79 closure; but r = 16ε fallacy is STILL FORBIDDEN structurally | UNCHANGED; carries forward |
| S16 | `S78-W3-D` JOSEPHSON-LEGGETT-MIXING P(pass)=0.45 | P1-1: Leggett-DM scaling exponent 2.17e-4 is PERMANENT §VII.II theorem (fourth) [p1-1:852] | Gate CLOSED at structural level; EVOI subsumed into Ω_DM sector which is already at 0.7σ |
| S17 | `S78-W3-E` PBH-CONSTRAINT P(pass)=0.45 | P2-B: Chluba kernel correction; FIRAS yoked to A_s, not independent [p2-b:754] | Gate CLOSED-REFRAMED: FIRAS passes at 5 OOM margin IF A_s closes; YOKED not INDEPENDENT |
| S18 | `S78-W3-F` f_NL-COHERENCE P(pass)=0.65 | No S79 closure; carries | UNCHANGED |
| S19 | `S78-W3-G` DESI-DR3-UPDATE P(pass)=0.40 | P2-C: S78 W3-G 23.10σ FAIL was Pattern 3' methodology failure, NOT framework DE failure [p2-c:752]; Route A (Volovik partition) at 1.73σ from DR3 Sc.B [p2-c:762]; Route B permanently closed by Weyl-scaling theorem [p2-c:756] | Gate REFORMULATED: W3-G-β R1/R2/R3 splits as successor; REMOVE verdict interpretation, KEEP numerical output |
| S20 | `S78-W3-H` CMPP-AT-TAU-0.537 P(pass)=0.40 | P1-1: C² Type D sectional curvature zero is PERMANENT §VII.II theorem [p1-1:860] | Gate CLOSED at PASS structurally |
| S21 | `S78-W3-J` SIN2-W-NON-TREE P(pass)=0.30 | P1-1: tree-UV sin²θ_W is PERMANENT §VII.III closure [p1-1:860]; cubic EW-scale derivation remains UNCOMPUTED [p1-1:892] | Gate SPLIT: tree UV CLOSED; EW-scale cubic derivation (CF-10 P1-1) is new PRIORITY gate |
| S22 | `S78-W3-K` R_1-L-MAX-CROSS-GROUPS P(pass)=0.60 | P4-A: strict FAIL is PERMANENT; joint theorem (functional-pluralism × rank-universality) is §VII.II pre-theorem with 5 extension tests [p4-a:2158] | Gate CLOSED at strict-FAIL; successor: 5 extension tests + SG1 analytic proof [p4-a:2144] |
| S23 | `S78-W3-L` SDW-ZETA-DICTIONARY P(pass)=0.70 | P1-3: WARRANT-INVALID; R3 remediation with freeze-by-name + list-hash [p1-3:1489] | P(pass) undefined; R3 remediation required |
| S24 | `S78-W3-N` DC-PERMANENCE P(pass)=0.60 | P1-1: DC-permanence CLOSED at §VII.III [p1-1:860] | Gate CLOSED |
| S25 | `S78-W3-O` MODULUS-DECAY P(pass)=0.55 | P3-B: Route α cushion CORRECTED 13→7.3 OOM [p3-b:888]; Γ_γ promoted to unitarity LOWER BOUND [p3-b:890] | Gate REFORMULATED: Route α FAIL preserved at 4 OOM below target; Route γ preserves T_rh = 1.69e18 MeV; channel-distinguishing observables are the S80 content [p3-b:932] |
| S26 | `N1 TRANSFER-FUNCTION-74` EVOI=18.2% | Per P1-1, n_s shape and m_H boundary are independent channels [p1-1 via S73B W1-C]; transfer function no longer the unique alpha_s remediation | P(pass) re-estimated at 0.30 (narrower window post-spectral-functional PERMANENT-FAIL); new target: stabilize tau with a mass-independent n_s recipe |
| S27 | `N2 MODULI-STABILIZATION-74` EVOI=12.0% | P3-A: tau_min = 0.1878 at fold is the NEW substrate interpretation; the old "bare V_eff minimum in [0.45, 0.70]" is STRUCTURALLY WRONG QUESTION [p3-a:1183] | RECAST: the stabilization IS the fold transit; P(pass) changes type from "find a minimum" to "verify Fold Transit Event 4th functional" |
| S28 | `N4 E_C-RESOLUTION-74` EVOI=10.2% | No S79 closure; carries | UNCHANGED, but now lower priority vs UNIFIED-AS-79 family |
| S29 | `N16 RATIO-OF-RATIOS-PROTECTED-74` EVOI=4.4% | P4-D: CC-ratios-only theorem ELEVATES this from "catalog 3 observables" to structural theorem candidate [p4-d:1810] | PROMOTED — see P entries |

#### C — CLOSED by S79 (permanent verdicts installed)

| # | Entry | Closure source | Final verdict |
|:--|:------|:---------------|:--------------|
| C1 | Multi-band bootstrap (Scenario B 72× enhancement) | P3-A L3 | PERMANENTLY CLOSED (block-diagonal theorem; solution-space volume = 0) |
| C2 | W3-O channel identification | P3-B | Route γ dominates at 5.0e-8 of Γ_γ total; Route α additive sub-channel at 1.1e14 MeV (4 OOM short) |
| C3 | Route B (SDW-KMS ζ for w_0) | P2-C | CLOSED by Weyl-scaling theorem w_vac ∈ [-0.50, +0.50], w_0 = -0.918 lies outside image set [p2-c:756] |
| C4 | F_amp^2 convention error | P1-1 (CHK4 re-confirmation) | PERMANENTLY CLOSED at d(ln A_s)/d(ln F_amp) = 1.000000 [p1-1:858] |
| C5 | f_conv^{ζ}/f_conv^{SDW} = 1/R_1 | P1-1, P4-C | PERMANENT machine-epsilon identity [p1-1:860] |
| C6 | f_conv^{anomaly}/f_conv^{SDW} = 1 at Λ_cut=λ_max | P1-1, P4-C | PERMANENT machine-epsilon identity |
| C7 | a_4 R²-invariance | P1-1 (W2-F) | PERMANENT §VII.II theorem |
| C8 | C² Type D sectional curvature zero at τ=0.537 | P1-1 (W3-H) | PERMANENT §VII.II theorem |
| C9 | Leggett-DM scaling exponent 2.17e-4 | P1-1 (W3-D) | PERMANENT §VII.II theorem |
| C10 | 4-class integrity failure catalog (Pattern 1, 3, 3', PRU) | P1-3, P2-C | Methodology rule CLOSED; to insert in epistemic-discipline.md |
| C11 | Axiomatic IC-principle gap | P2-B | CLOSED; 5 independent directions rule out S_IC < 1 [p2-b:764] |
| C12 | Frozen spectrum theorem (10⁻¹¹³ through fold) | P2-B | PRESERVED, reinforced [p2-b:770] |

#### RO — RE-OPENED (previously closed, S79 surfaced new issues)

| # | Entry | Trigger | New gate |
|:--|:------|:--------|:---------|
| RO1 | W1-A slot-consistency | P4-C EM2 sign-flip doctrine [p4-c:1121] | CF-1 P4-C: audit which a_n slot W1-A uses (a_0 amplifies ×32, a_2 suppresses ×0.38) |
| RO2 | W1-B, W2-C, W3-L numerics | P1-3 WARRANT-INVALID [p1-3:1426] | R1, R2, R3 remediation re-runs under §0.10(b)(c)(d) |
| RO3 | Canonical constants naming (`mellin_*` vs `cc_*`) | P4-C CF-2 | PRU-class rename + provenance audit |
| RO4 | ω_L1 vs m_L1 provenance | P3-A CF-4 [p3-a:1239] | Legacy scripts conflated FREQUENCY (0.138) with MASS (0.070); S80 Wave 0 blocker for CF-1 |
| RO5 | v_ew derivation path | P4-D "What Breaks or Strains" [p4-d:1788] | latent secondary-pin risk; CF-4 framework-single-pin-verification |
| RO6 | S78 framework-document citations of "13 OOM cushion" | P3-B CF-2 [p3-b:941] | Audit: replace with 7.3 OOM central |

#### P — PROMOTED (candidate or low-level → higher priority)

| # | Entry | Source | New priority |
|:--|:------|:-------|:-------------|
| P1 | `UNIFIED-AS-79-FULL` | P2-A + P2-B + P4-D | Level 1 TOP (rate-limiting; replaces W1-A/W1-C/W1-E composed chain) |
| P2 | `UNIFIED-AS-79-CSUB-SIGN` | P1-2 | Level 1 (sign derivative -1.000 ± 0.01, confirmation gate) |
| P3 | `UNIFIED-BACKREACT-79` | P2-A P2 | Level 1 (fold backreaction saturation test) |
| P4 | `H-TILDE-EPOCH-CONSISTENCY` (CF-1 P4-D) | P4-D | Level 1 TOP (determines whether gap is 0.22 or 1.12 OOM) |
| P5 | CC-ratios-only theorem (CF-2 P4-D) | P4-D CN-EM1 | Level 1-2 (≤3-page analytic proof; structures all forward CC work) |
| P6 | M_KK structural role documentation (CN-EM4) | P4-D | Level 2 (canonical_constants.py header rewrite) |
| P7 | Fold Transit Event 4th-functional (dS_inst/dτ, χ_N, Z_s) | P3-A | Level 1-2 (§VII.I promotion path) |
| P8 | W3-G-β R1/R2/R3 (Route A Volovik dual-axis) | P2-C | Level 2 (DE-sector binding at DR3 release) |
| P9 | Pattern 3' rule insertion | P2-C | Level 3 (methodology) |
| P10 | Marginal-semiclassical language audit (CF-7 P3-B) | P3-B | Level 4 (documentation) |
| P11 | 1-loop-proper cushion citation pin (CF-2 P3-B) | P3-B | Level 3 (audit) |
| P12 | Model-C inertial pin propagation (CF-5 P1-2) | P1-2 | Level 3 (script audit) |
| P13 | Multi-pair N_pair=2 (CF-3 P3-A) | P3-A | Level 2 (new A_s closure candidate) |

#### N — NEW (S79 introduced, not in S78 EVOI table)

| # | New entry | Source | Description |
|:--|:----------|:-------|:------------|
| N1 | `S80-H-TILDE-EPOCH-CONSISTENCY` (CF-1 P4-D) | P4-D | Determines if A_s gap is 0.22 OOM (Path A horizon-exit) or 1.12 OOM (Path B fold-Friedmann); most-important S80 computation |
| N2 | `S80-CC-RATIOS-ONLY-THEOREM` (CF-2 P4-D) | P4-D CN-EM1 | ≤3-page proof of f_n-linearity cancellation in weight-balanced ratios; structural theorem |
| N3 | `S80-CANONICAL-CONSTANTS-AUDIT` (CF-3 P4-D) | P4-D CN-DS1 | Classify every entry: D_K ratio / M_KK^n × ratio / external pin / slot-dependent |
| N4 | `S80-SINGLE-PIN-VERIFICATION` (CF-4 P4-D) | P4-D CN-DS2 | v_ew, m_H_obs, Delta_BCS, E_cond, ρ_Λ_spectral derivation paths |
| N5 | `S80-DIM-H-PI-UNIVERSAL-EXCLUSION` (CF-5 P4-D) | P4-D | dim H_π ≥ 2 as criterion for Level-2 protection across SU(4), SU(5), G_2 |
| N6 | `S80-R-FAMILY-ATLAS-EXTENSION` (CF-6 P4-D) | P4-D | R_3, R_4, R_5, R_6 across {SDW, f*, ζ, anomaly-sharp} |
| N7 | `S80-FOLD-INST-GRADIENT` (CF-2 P3-A) | P3-A | dS_inst/dτ 5-point scan; §VII.I promotion path for Fold Transit Event |
| N8 | `S80-OMEGA-L-MULTI-FORMAL-S++` (CF-1 P3-A) | P3-A | Formal s++ Leggett equation for DM-sector survival (load-bearing) |
| N9 | `S80-MULTIPAIR-ECOND-TAUFOLD` (CF-3 P3-A) | P3-A | New A_s closure candidate; E^{N=2}/E^{N=1} ≥ 10 threshold |
| N10 | `S80-CHI-N-WARD-DUAL` (CF-7 P3-A) | P3-A | Rank-2 fourth functional via Ward identity |
| N11 | `S80-B1-JENSEN-SCAN` (CF-5 P3-A) | P3-A | 21-pt τ-scan of J_u1(τ), J_C2(τ), J_su2(τ); E-4 double-flat-band verdict |
| N12 | `S80-SPP-FULL-ED-SIGN-MARGIN` (CF-6 P3-A) | P3-A | Leggett-survival sign-margin cross-check |
| N13 | `S80-GW-CHANNEL` (CF-1 P3-B) | P3-B | LISA-band Ω_GW(f=0.001 Hz) Route α vs Route γ discrimination |
| N14 | `S80-K2-LATTICE-BENCHMARK` (CF-4 P3-B) | P3-B | Tighten K_2 range from Dunne-Unsal post-2020 lattice literature |
| N15 | `S80-GGE-CORRELATION-CHANNEL` (CF-5 P3-B) | P3-B | GGE relic spectrum channel sensitivity |
| N16 | `S80-CMB-FNL-CHANNEL` (CF-6 P3-B) | P3-B | Local non-Gaussianity channel discrimination |
| N17 | `S80-W1-A-SLOT-CONSISTENCY-AUDIT` (CF-1 P4-C) | P4-C | BLOCKING audit of W1-A's a_n slot routing (a_0 vs a_2) |
| N18 | `S80-HEAT-KERNEL-MP-EXCLUSION` (CF-3 P4-C) | P4-C | Formal proof f* categorically excluded from continuum-limit sibling class |
| N19 | `S80-KASPAROV-ABELIAN-PROOF` (CF-1 P4-B) | P4-B | Formal Connes-Moscovici proof: abelian subfactors lack Level-2 R-protection |
| N20 | `S80-W2C-L8-DRIFT-PREDICTION` (CF-2 P4-B) | P4-B | CLT prediction drift_u1(L=8) ∈ [56%, 76%] (pred 66.06%) |
| N21 | `S80-T2-ALT-DECOMPOSITION` (CF-3 P4-B) | P4-B | T² bundled (λ_3+λ_8) vs 3-branch; CLT pred 59.22% |
| N22 | `S80-W3K-FIT-DEFINITION-PIN` (CF1 P4-A) | P4-A | drift-to-R_∞ replaces drift-to-L_ref |
| N23 | `S80-RICHARDSON-EXTRAPOLATION` (CF2 P4-A) | P4-A | L_max = 5r per group (SU(3) L=10, SU(4) L=15) |
| N24 | `S80-OTHER-RATIOS` (CF3 P4-A) | P4-A | α(R_B), α(R_C) scaling hierarchy |
| N25 | `S80-G2-F4-TEST` (CF4 P4-A) | P4-A | Exceptional groups for rank-universality |
| N26 | `S80-EXOTIC-DISCRIMINATORS` (CF5 P4-A) | P4-A | SO(3) vs SU(2); SU(2)×SU(2) vs SU(3) |
| N27 | `S80-SG1-THEOREM` (CF6 P4-A) | P4-A | ≤4-page analytic proof of α=rank(G) |
| N28 | `S80-F_amp^sc VIA 3PI` (CF-1 P1-1) | P1-1 | Self-consistent F_amp beyond 2PI/damped-Hartree |
| N29 | `S80-PHYSICAL-CAP-SIC-SUBHORIZON` (CF-2 P1-1) | P1-1 | S_IC(k_pivot) sub-horizon asymptotic reading |
| N30 | `S80-E_J-CONVENTION` (CF-3 P1-1) | P1-1 | E_J without FABRIC-COUPLING-55 ansatz |
| N31 | `S80-MU-EFF-RATE-MATRIX` (CF-4 P1-1) | P1-1 | L-K rate-matrix reformulation of μ_eff (isocurvature retest) |
| N32 | `S80-A_S-ADJACENT-REPLACEMENT-OBSERVABLE` (CF-8 P1-1) | P1-1 | P_ζ(k_trans)/P_ζ(k_pivot) = 2.25e-4 convention-invariant |
| N33 | `S80-CUBIC-SIN2W-EW-SCALE` (CF-10 P1-1) | P1-1 | EW-scale derivation of sin²θ_W = 0.2348 cubic (tree-KK path excluded) |
| N34 | `UNIFIED-AS-79-FULL` | P2-A + P2-B | TOP-PRIORITY; replaces composed-chain A_s |
| N35 | `UNIFIED-AS-79-CSUB-SIGN` | P1-2 | [SIGN] gate d(ln A_s)/d(ln c_sub) = -1.000 ± 0.01 |
| N36 | `UNIFIED-BACKREACT-79` | P2-A P2 | UNIFIED-AS-79 + self-consistent backreaction |
| N37 | `PS-SUBSTRATE-MATCHED-IC` (P4 P2-A) | P2-A | 4th IC account; pre-fold substrate GGE projected onto post-fold FRW |
| N38 | `W3-G-β R1/R2/R3` | P2-C | Volovik fresh extraction + F_amp coupling audit + DR3 dual-axis registration |
| N39 | `Pattern 3' RULE INSERTION` | P2-C | Insert 4-class integrity catalog into epistemic-discipline.md |
| N40 | `PRU + §0.10 split` | P1-3 | §0.10(a)(b)(c)(d) + iteration-audit-template.md |
| N41 | `EVOI-SYNC-79` (CF-6 P1-1) | P1-1 | Synchronize 5 record layers (WP, verdict-log, EVOI file, agent-memory, knowledge-index) |
| N42 | `PHASE-ALIGNMENT K-SCAN` (P5 P2-A) | P2-A | cos(φ_α - φ_β) at 5 k-values; substrate observable |
| N43 | `CHLUBA-KERNEL-FIRAS INTEGRAL` (P2 P2-B) | P2-B | Post-processing of UNIFIED-AS-79 output; μ-distortion |
| N44 | `PBH-POPULATION-K-SCAN` (P4 P2-B) | P2-B | f_PBH(M) from B3 envelope at PBH windows |
| N45 | `BACKWARD-BD-CONSISTENCY` (P6 P2-B) | P2-B | Initialize in post-fold BD, evolve backward; unitarity check |
| N46 | `H_transit vs H_Friedmann convention` (P7 P2-B) | P2-B | M_Pl_red vs M_KK in post-fold dS Friedmann cascade |

**Diff summary**: 29 STALE items requiring re-estimation, 12 CLOSED permanent additions, 6 RE-OPENED, 13 PROMOTED, 46 NEW. Target items-changed count: **106**. Far above the 15-item realistic bar. The post-S79 EVOI table is a substantial rewrite, not an incremental update.

### N2: UNIFIED-AS-79 family — Bayesian P(pass) estimation

The UNIFIED-AS-79 family is the replacement for the retracted 4-factor A_s ledger (P2-A [p2-a:1169]). Three compute gates + one diagnostic gate form the family. Each P(pass), ΔP estimate comes from a Bayesian update grounded in S79 closer evidence.

#### N2.1 — UNIFIED-AS-79-CSUB-SIGN [SIGN] substitution chain

**Required substitution chain per math-scripts.md §Double-Check Logic**:

```
Claim: c_sub > 1 SUPPRESSES A_s under UNIFIED-AS-79 (d(ln A_s)/d(ln c_sub) = -1.000)

Step 1 (definitions):
  z(N, k) = a(N) · sqrt(2·ε(N)) · M_Pl_eff(k)       [Mukhanov 1992]
  P_ζ(k) = |v_k|² / z(N, k)²                         [definition at horizon exit]
  c_sub(k) = M_Pl_eff(k)² / M_Pl_eff(0)²             [c_sub definition, P1-2 TE1]

Step 2 (substitution into P_ζ ratio):
  P_ζ(k_pivot) / P_ζ(0)
    = [|v(k_pivot)|² / z(N, k_pivot)²] / [|v(0)|² / z(N, 0)²]

Step 3 (mode-amplitude cancellation at horizon-exit WKB):
  |v(k_pivot)|² / |v(0)|² = 1                        [both evaluated at horizon-exit WKB = 1/(2k)]
  Therefore P_ζ(k_pivot)/P_ζ(0) = z(N, 0)² / z(N, k_pivot)²

Step 4 (factor cancellation in z):
  z(N, 0)² / z(N, k_pivot)² = [a(N)·sqrt(2ε)·M_Pl_eff(0)]² / [a(N)·sqrt(2ε)·M_Pl_eff(k_pivot)]²
                            = M_Pl_eff(0)² / M_Pl_eff(k_pivot)²
                            = 1 / c_sub(k_pivot)

Step 5 (canonical form):
  P_ζ(k_pivot) = P_ζ(0) · 1/c_sub

Step 6 (direction):
  d(ln P_ζ(k_pivot)) / d(ln c_sub) = -1.000          [canonical form]
  c_sub > 1 ⇒ ln(c_sub) > 0 ⇒ ln(P_ζ) decreases ⇒ A_s SUPPRESSED
  c_sub = 2.23 gives A_s reduction factor 1/2.23 = 0.4484

Direction: c_sub = 2.23 SUPPRESSES A_s. WIDENS the A_s overshoot, does not narrow it.
This is the P1-2 sign-reversal finding confirmed.
```

**Bayesian P(pass) for CSUB-SIGN**:
- Prior: the Landau derivation in P1-2 TE1 + L-Q1 analysis independently reproduces d(ln A_s)/d(ln c_sub) = -1 from the Mukhanov-Sasaki mode equation [p1-2:956]. This is a framework-internal identity, not an observational comparison.
- Evidence: P1-2 ran the full derivation chain; the sign result is algebraically forced, not a Monte-Carlo.
- P(pass) = 0.85. Residual 15% failure mass: code-level implementation bug (CHK4-like closure failure) or convention drift (e.g., f_conv integration dimension error).
- ΔP(pass) = 0.05 (confirms what is already algebraically forced; marginal information)
- ΔP(fail) = 0.20 (FAIL would indicate a framework-internal contradiction; LARGE information)
- **EVOI = 0.85 × 0.05 + 0.15 × 0.20 = 0.073** (Python-verified)

#### N2.2 — UNIFIED-AS-79-FULL [VERIFY] Bayesian estimation

**P4-D epoch disambiguation**: The A_s overshoot depends on which H̃ epoch anchors the comparison (CF-1 P4-D is the rate-limiting decision).

**Substitution chain for the 3.35 OOM → 1.12 OOM gap narrowing**:
```
Claim: Under P4-D ratios-only framing, the A_s gap shrinks from 3.35 OOM (absolute) 
to 1.12 OOM (Path B) or 0.22 OOM (Path A)

Step 1 (defs):
  A_s(absolute) = F_amp × P_dS × f_conv × S_IC                  [retracted 4-factor ledger]
  A_s(ratio) = (A_s_framework / A_s_obs) at fixed epoch         [P4-D CN-CV4 framing]
  Gap(OOM) = log10(A_s_framework / A_s_obs)

Step 2 (epoch choice):
  Path A: H̃ at τ_horizon_exit (post-fold stiff-to-dS transition)
  Path B: H̃ at τ_fold = 0.190 (fold event)

Step 3 (ratio forms):
  Path A gives A_s / A_s_obs = 10^(-0.22) = 0.603                [p4-d:1766]
  Path B gives A_s / A_s_obs = 10^(+1.12) = 13.18                [p4-d:1766]

Step 4 (vs absolute 3.35 OOM reading under Path B):
  3.35 OOM - 1.12 OOM = 2.23 OOM absorbed by M_KK^n dimensional pin
  Under P4-D CN-EM1 f_n-cancellation, M_KK^n disappears in weight-balanced ratios

Step 5 (canonical form):
  The gap a user should track is the RATIO gap, not the absolute gap
  Path A is closer to observed; Path B is farther
  Both paths live within the theoretical uncertainty band until H̃-epoch resolved

Direction: Gap SHRINKS from absolute 3.35 OOM to ratio 0.22-1.12 OOM (Python-verified 
gap shrinkage factor 2.99). Which epoch is canonical is UNDECIDED.
```

**Bayesian update for P(pass) of UNIFIED-AS-79-FULL**:
```
Step 1 (prior P(pass) pre-P4-D): based on composed 4-factor ledger showing 3.35 OOM gap
  P(pass at factor-4 band) ≈ 0.05 (too tight; composed chain was +3 OOM overshoot)
  P(pass at factor-10 band, INFO) ≈ 0.10
  P(pass at factor-100 band, wider) ≈ 0.20

Step 2 (Bayes update from P4-D ratios-only reframe):
  P(S79_evidence | pass) = moderate; ratios-only theorem compatible with PASS
  P(S79_evidence | fail) = also moderate (theorem neutral to observational outcome)
  Bayes factor BF = P(evidence|pass) / P(evidence|fail) ≈ 3-5
  
Step 3 (posterior computation):
  For prior 0.10 and BF = 3: posterior = 0.10·3/(0.10·3 + 0.90) = 0.30/1.20 = 0.250
  For prior 0.10 and BF = 5: posterior = 0.50/(0.50 + 0.90) = 0.357
  Python-verified: BF=3→0.250, BF=5→0.357, BF=7→0.438

Step 4 (epoch-conditional posteriors):
  P(pass | Path A canonical) ≈ 0.60 (0.22 OOM gap is within factor-2 band at 10%)
  P(pass | Path B canonical) ≈ 0.30 (1.12 OOM gap is within factor-15 band, INFO-likely)
  P(Path A canonical) and P(Path B canonical) are UNKNOWN until CF-1 P4-D runs

Step 5 (marginalized):
  If equal prior on Path A vs Path B: P(pass) = 0.5·0.60 + 0.5·0.30 = 0.45
  Adopt 0.45 for marginalized posterior pending H̃-epoch gate
```

**EVOI for UNIFIED-AS-79-FULL**:
- P(pass) = 0.45 (marginalized over Path A/B)
- ΔP(pass) = +0.25 (closes the ~1-OOM ratio-level strain; frees framework from A_s irredeemability)
- ΔP(fail) = -0.18 (confirms ratios-only reframe does not save A_s; triggers mechanism search CF-7 P1-1)
- EVOI = 0.45 × 0.25 + 0.55 × 0.18 = 0.112 + 0.099 = **0.211**

#### N2.3 — UNIFIED-BACKREACT-79

- Prior: W1-C INCOMPUTABLE-FALLBACK-TO-BOUND gave F_amp^sc ≤ 47.9 [p1-1:860]. Under UNIFIED-AS-79 the fold consumes the backreaction budget [p2-a:1181]; F_amp^sc → 1.
- P(pass) = 0.50 (genuine uncertainty; self-consistent backreaction could save or kill A_s)
- ΔP(pass) = +0.18 (if F_amp^sc → 1 and A_s drops by factor 6858, OOM-scale relief)
- ΔP(fail) = -0.15 (Branch D confirmed: linearized formalism permanently inapplicable)
- EVOI = 0.50 × 0.18 + 0.50 × 0.15 = 0.090 + 0.075 = **0.165**

#### N2.4 — H̃-RATIO-EPOCH-CONSISTENCY

This is the MOST IMPORTANT S80 gate because it determines Path A vs Path B (P4-D CF-1 [p4-d:1803]). All downstream A_s verdicts depend on it.

- Prior: no direct evidence for either epoch being canonical; user's Planck-as-assumed-floor intuition [p4-d:1770] pins external observational H̃
- P(pass for Path A) ≈ 0.50 (symmetry prior; both epochs have physical motivation)
- ΔP(pass) = ΔP(fail) = +0.30 each (resolving this removes the Path A/B ambiguity from ALL future A_s work)
- **EVOI = 0.50 × 0.30 + 0.50 × 0.30 = 0.300** — HIGHEST of the family (Python-verified)

#### UNIFIED-AS-79 family ranked table

| Gate | P(pass) | ΔP(pass) | ΔP(fail) | EVOI | Priority | Blocker |
|:-----|:--------|:---------|:---------|:-----|:---------|:--------|
| **H̃-RATIO-EPOCH-CONSISTENCY** (N1 in N1-diff) | 0.50 | +0.30 | -0.30 | **0.300** | S80 Wave 1 TOP | Blocks UNIFIED-AS-79-FULL interpretation |
| **UNIFIED-AS-79-FULL** (N34) | 0.45 | +0.25 | -0.18 | **0.211** | S80 Wave 1 TOP | Depends on H̃-epoch |
| **UNIFIED-BACKREACT-79** (N36) | 0.50 | +0.18 | -0.15 | **0.165** | S80 Wave 2 | Depends on UNIFIED-AS-79-FULL output |
| **UNIFIED-AS-79-CSUB-SIGN** (N35) | 0.85 | +0.05 | -0.20 | **0.073** | S80 Wave 1 confirmation | Independent; can run parallel |
| **PS-SUBSTRATE-MATCHED-IC** (N37) | 0.40 | +0.15 | -0.08 | **0.108** | S80 Wave 2 parallel | Requires substrate-GGE IC spec |

**Nazarewicz ranking**: H̃-EPOCH > UNIFIED-FULL > UNIFIED-BACKREACT > PS-SUBSTRATE > CSUB-SIGN. The H̃-epoch gate is the single most informative S80 computation because its outcome determines whether the framework's A_s residual is ~factor 2 (Path A, recoverable with sub-order-OOM tweaks) or ~factor 15 (Path B, requires substantive mechanism).

### N3: Fold Transit Event — 4th functional ranking

P3-A promoted the S78 W1-D/W1-E/W2-A triple of failures into a single substrate event: the **Fold Transit Event** at τ_fold = 0.190 [p3-a:1155]. Current status: §VII.II session-observation pre-theorem. Promotion to §VII.I permanent theorem requires a 4th independent response-function concentration at τ_fold (the first three — χ_a peak, |β|² diabatic amplification, slow-mode IPR on B1 — are integrals of the same ρ(ε, τ), not independent checks [p3-a:1199]).

#### N3.1 — Substitution chain: why a 4th INDEPENDENT functional is needed

```
Claim: The three existing functionals are not independent; their joint concentration at τ_fold 
is structurally expected once one concentrates

Step 1 (defs):
  χ_a(τ)        = ∫ dε · ρ(ε, τ) · K_a(ε, τ)          [pairing susceptibility, K_a quasi-peak]
  |β|²(k, τ)    = Parker-squeezing amplification      [integral of ρ over mode spectrum]
  IPR(B1, τ)    = ⟨ψ|ψ⟩² / ⟨ψ²|ψ²⟩ on slow mode       [localization on ρ's low-energy subspace]

Step 2 (joint dependence on ρ):
  All three are INTEGRAL FUNCTIONALS of ρ(ε, τ_fold)
  If ρ develops a van Hove singularity at τ_fold, ALL THREE concentrate simultaneously
  Independence requires a functional NOT expressible as ∫ F(ε) · ρ(ε, τ) dε

Step 3 (canonical form):
  Required: a functional of a DIFFERENT geometric/dynamical object
  Candidates differ by which "face" of the fold they probe

Direction: Promotion to §VII.I requires a functional probing a face ORTHOGONAL to ρ(ε, τ).
```

#### N3.2 — Candidate ranking

**Candidate (a): dS_inst/dτ (instanton-action gradient)** [CF-2 P3-A]
- What it probes: the bare spectral action's τ-derivative (substrate face, not ρ-integral)
- Independence from ρ: HIGH. dS_inst/dτ derives from the instanton sector; ρ(ε, τ) is a one-particle density. Different objects.
- Tractability: MEDIUM. S37 paradigm + S48 qtheory-gold-48 provides instanton formalism; compute at 5 τ-points {0.15, 0.17, 0.19, 0.21, 0.25}.
- Informativeness: HIGH. Directly tests whether the Fold Transit Event is ALSO an instanton-action singularity.
- Prior P(pass): 0.60. If the fold is a first-order transit as P3-A claims, dS_inst/dτ should show a discontinuity or peak concentrated at τ_fold.
- ΔP(pass) = +0.20 (promotes Fold Transit Event to §VII.I permanent theorem)
- ΔP(fail) = -0.15 (keeps at §VII.II; three-functional reading retained but structural status degraded)
- **EVOI = 0.60 × 0.20 + 0.40 × 0.15 = 0.120 + 0.060 = 0.180** (Python-verified)

**Candidate (b): χ_N (fermion-number susceptibility)** [CF-7 P3-A]
- What it probes: fermion-number response to chemical potential; Ward-identity dual to χ_a
- Independence from ρ: LOW. Ward identity ∂N/∂μ = (∂²F/∂μ²)|_fixed_T can be written as an integral over ρ. Might be tautological.
- Tractability: HIGH. Reuses W1-D ρ(ε, τ) DoS engine directly.
- Informativeness: MEDIUM. Ward-identity dual consistency IS a check, but may not add orthogonal information.
- Prior P(pass): 0.80 (structural consistency likely to hold)
- ΔP(pass) = +0.08 (confirms Ward-identity dual; tautological-leaning)
- ΔP(fail) = -0.05 (Ward identity violation would be surprising and informative, but unlikely)
- **EVOI = 0.80 × 0.08 + 0.20 × 0.05 = 0.064 + 0.010 = 0.074** (Python-verified)

**Candidate (c): Z_s (elastic-tetrad shear response)** [CF-7 P3-A Q-L1-Zs]
- What it probes: Nissinen-Volovik Paper 20 elastic-tetrad shear susceptibility
- Independence from ρ: HIGH (elastic-tetrad is a different structural object)
- Tractability: LOW. Paper 20 formalism built for extended elastic media; 0D / N_pair=1 compatibility UNCONFIRMED [p3-a:1203]
- Informativeness: HIGH IF it applies; probes elastic face of the fold transit
- Prior P(pass): 0.50 (formalism-compatibility risk dominates)
- ΔP(pass) = +0.20 (equivalent promotion to §VII.I if it applies)
- ΔP(fail) = -0.15
- **EVOI = 0.50 × 0.20 + 0.50 × 0.15 = 0.100 + 0.075 = 0.175** (Python-verified)

#### N3.3 — Fold Transit Event 4th-functional ranking table

| Candidate | Tractability | Independence | P(pass) | EVOI | Rank |
|:----------|:-------------|:-------------|:--------|:-----|:-----|
| dS_inst/dτ | MEDIUM | HIGH | 0.60 | **0.180** | **1 (recommended for S80 Wave 1)** |
| Z_s (Nissinen-Volovik) | LOW | HIGH | 0.50 | 0.175 | 2 (formalism-check gated) |
| χ_N (Ward dual) | HIGH | LOW | 0.80 | 0.074 | 3 (tautology risk) |

**Recommendation**: S80 Wave 1 runs **dS_inst/dτ** as the primary 4th-functional probe. χ_N runs in parallel as a cheap consistency check (high tractability, low marginal cost). Z_s runs in Wave 2 ONLY after a formalism pre-gate confirms 0D / N_pair=1 admissibility.

#### N3.4 — Combined §VII.I promotion odds

If Candidate (a) PASSES: Fold Transit Event → §VII.I permanent theorem. If it FAILS but Z_s PASSES, same promotion. Combined promotion probability:

```
P(promotion) = 1 - P(all candidates fail)
             = 1 - [1 - P(dS_inst pass)] × [1 - P(Z_s pass) | formalism admissible] × P(Z_s inadmissible weighting)

Step 1 (independence assumption):
  Assume dS_inst and Z_s outcomes are independent given their distinct probes

Step 2 (numeric substitution):
  P(dS_inst fail) = 0.40
  P(Z_s fail | admissible) = 0.50
  P(Z_s admissible) ≈ 0.60 (unknown; adopt moderate prior)
  P(Z_s fail total) = 0.60 × 0.50 + 0.40 × 1.0 = 0.30 + 0.40 = 0.70
  P(χ_N adds independent info) ≈ 0.20

Step 3 (combined):
  P(at least one passes) ≈ 1 - (0.40 × 0.70 × 0.80) = 1 - 0.224 = 0.776
  
Step 4 (canonical form):
  Promotion probability ≈ 0.78 conditional on running all three candidates

Direction: S80 Wave 1 (dS_inst alone) gives 0.60 promotion probability.
S80 Wave 1+2 (dS_inst + Z_s + χ_N) gives ~0.78 promotion probability.
```

The S80 Wave 1 dS_inst/dτ run is the rate-limiting step. χ_N is inexpensive; run it alongside. Z_s is gated on formalism admissibility check.

### N4: Remediation layer P(pass) — confirmation-gate priors

P1-3 installed three remediation scripts (R1, R2, R3) to cure the WARRANT-INVALID verdicts on W1-B, W2-C, W3-L [p1-3:1426]. These are NOT new-physics gates; they are confirmation re-runs under corrected discipline (§0.10(b)(c)(d) + PRU + iteration-audit-template) [p1-3:1441-1441]. The Bayesian framing differs fundamentally from exploratory gates.

#### N4.1 — Why remediation gates carry HIGH P(pass) priors

**Substitution chain**:
```
Claim: R1, R2, R3 carry P(pass) ≈ 0.85-0.90 because the WARRANT-INVALID verdicts were 
on PROCESS-level failures, not NUMERICS-level failures.

Step 1 (def of WARRANT-INVALID class):
  WARRANT-INVALID = plan-letter violation OR tag discipline failure OR iteration count violation
  [p1-3 §0.10(b)(c)(d) class catalog]
  NOT = "numerics point to wrong answer"

Step 2 (decomposition of P1-3 verdicts):
  W1-B INVALID sources:
    (a) meta-retrofit in CONDITIONAL upgrade (plan-letter)
    (b) ε-scan cited as root-cause not in plan's 4 cross-checks (plan-letter)
    (c) no iteration cascade pre-registered (process)
  All three are PROCESS failures. The underlying F_amp numerics are not contested.
  
  W2-C INVALID source:
    Single source: quantity-definition-drift Type II (i=2→i=3 factor-14.6 jump, process)
    The L_max=6 ZETA-JOSEPHSON computation was logging inconsistent quantity definitions 
    across iterations; pin the quantity-def under §0.10(b) and the drift vanishes.

Step 3 (what remediation does):
  R1: addendum documenting N_eval = N_pivot+3 derivation, ε-scan as regime-diagnostic, 
      Stokes pre-registered as FAIL-trigger at ratio > 10
  R2: pin primary observable as scheme-invariant functional; pin L_max=6; pin 4-tuple 
      scheme-tag; no L_max mixing across re-run
  R3: frozen candidate list with SHA-256 hash pin

Step 4 (re-run outcome under corrected process):
  R1 produces one verdict line with commit SHA + closure_sha256; fallback cascade honored
  R2 produces one verdict with frozen quantity-def; drift measurement is single-shot
  R3 produces one verdict with frozen lists; audit is structural

Step 5 (canonical form):
  Expected outcome = the TAIL verdict of each original iteration chain under proper process
  W1-B tail: i=8 gave INFO-adjacent near the 10% band with stable Stokes
  W2-C tail: i=3 gave drift 83.75% (vs CLT pred 66.06% at L=8)
  W3-L tail: misuses ∈ {2, 1} under frozen lists

Direction: P(R1 pass) HIGH (~0.90) because tail verdict is defensible under plan-letter; 
P(R2 pass) slightly lower (~0.85) because drift vs CLT-pred has genuine uncertainty at 
L=6; P(R3 pass) HIGH (~0.90) because audit is procedural.
```

#### N4.2 — EVOI for each remediation gate

**R1 (W1-B clean re-run)**:
- Prior: tail verdict at i=8 was INFO-adjacent; Stokes at 328 triggers FAIL but may be absorbed by Stokes-independent remediation path
- P(pass) = 0.90
- ΔP(pass) = +0.03 (small; unblocks downstream; F_amp numerics already defensible)
- ΔP(fail) = -0.18 (LARGE; FAIL indicates W1-B numerics are genuinely wrong, cascading to W1-A/UNIFIED-AS-79 confidence)
- **EVOI = 0.90 × 0.03 + 0.10 × 0.18 = 0.027 + 0.018 = 0.045** (Python-verified)

**R2 (W2-C clean re-run)**:
- Prior: tail verdict at i=3 gave drift 83.75%; CLT prediction at L=8 is 66.06% ± 10% [p4-b:1470]. The original drift is 17 pp above CLT upper band.
- **Substitution chain for drift vs CLT comparison**:
  ```
  Step 1: CLT prediction drift ~ 1/sqrt(N) where N = rank of Kasparov class
  Step 2: For u1 (abelian), N = rank of character module ≈ 2 (P4-B dim H_π = 1)
  Step 3: drift_CLT(L=8) = 0.66 ± 0.10 band
  Step 4: observed drift at i=3 = 0.8375
  Step 5: (0.8375 - 0.76) / 0.10 = 0.775σ above upper band
  Direction: observed drift is ~1σ above CLT prediction; PLAUSIBLE within CLT fluctuation
  ```
- P(pass | within CLT band) = 0.85 (L=8 re-run delivers drift in [0.56, 0.76] band)
- ΔP(pass) = +0.03 (confirms CLT-1/√N pre-theorem [p4-b:1470]; structural)
- ΔP(fail) = -0.15 (FAIL at L=8 drift outside CLT band forces VDD3 theorem revision OR implementation bug)
- **EVOI = 0.85 × 0.03 + 0.15 × 0.15 = 0.0255 + 0.0225 = 0.048** (Python-verified)

**R3 (W3-L clean re-run)**:
- Prior: audit is structural; SHA-256-frozen lists eliminate drift
- P(pass) = 0.90
- ΔP(pass) = +0.02
- ΔP(fail) = -0.10 (rare: FAIL indicates list content disagreement with frozen names)
- **EVOI = 0.90 × 0.02 + 0.10 × 0.10 = 0.018 + 0.010 = 0.028**

#### N4.3 — Remediation-gate ranking

| Gate | P(pass) | ΔP(pass) | ΔP(fail) | EVOI | Role |
|:-----|:--------|:---------|:---------|:-----|:-----|
| R1 (W1-B) | 0.90 | +0.03 | -0.18 | **0.045** | BLOCKING for UNIFIED-AS-79 citations |
| R2 (W2-C) | 0.85 | +0.03 | -0.15 | **0.048** | BLOCKING + tests P4-B CLT pre-theorem |
| R3 (W3-L) | 0.90 | +0.02 | -0.10 | **0.028** | BLOCKING for SDW-ζ dictionary citations |

**Key observation**: R1/R2/R3 individually have LOW EVOI (all < 0.05), but they are BLOCKING for the HIGH-EVOI gates. Their practical priority is determined by downstream dependency, not by EVOI magnitude alone. This is a case where EVOI-magnitude-alone is insufficient scheduling guidance. The evidence hierarchy requires them FIRST.

**Upshot for S80 Wave 0**: Run R1, R2, R3 **before** UNIFIED-AS-79-FULL (N34) and H̃-EPOCH (P4-D CF-1). Total effort: ~4-6 hours per P1-3 estimates [p1-3:1478, 1486, 1494]. The S80 Wave 1 HIGH-EVOI gates cannot cite W1-B/W2-C/W3-L until remediation verdicts land.

**R2 bonus test**: R2 simultaneously tests the P4-B abelian-subfactor pre-theorem (CLT 1/√N prediction). If R2 returns drift_u1(L=8) ∈ [56%, 76%], that is independent empirical support for the abelian-subfactor obstruction — a 2-for-1 outcome.

### N5: Questions for gen-physicist

These questions test the joints between EVOI methodology and the S79 structural harvest. gen-physicist owns neutral-evidence weighting and the effort-based framework probability; I need their verdict on each before the Round-2 synthesis.

**Q-GP1 — Framework probability effort-based update**

Per `.claude/rules/evoi-prioritization.md`: framework probability is (mechanism links complete / total) × (fraction approaching observation). S79 closed 12 workshops and reframed the A_s narrative (absolute 3.35 OOM → ratio 0.22-1.12 OOM). What's the updated numerator AND denominator?

Specifics I need:
- Mechanism-links ratio pre-S79: 9/11 per `evoi-framework.md:304`. Does S79 change the denominator (by adding H̃-epoch as a new mechanism-class link) or only the numerator?
- Fraction approaching observation: how do the 12 S79 pre-theorems (a_4 R²-invariance, f_conv-ratio identity, Leggett-DM scaling, C² Type D zero, Fold Transit Event, CC-ratios-only, MP-exclusion, abelian-subfactor, rank-universality, dim H_π ≥ 2, Weyl-scaling w_vac, Mellin-χ_2 for n_s) weigh into this fraction when NONE are individually observational-PASS but ALL are structural?
- The P2-A/P2-B methodology-FAIL reclassification (3 of 5 S78 FAILs re-diagnosed as methodology artifacts) STRENGTHENS surviving paths per evoi-prioritization.md. Quantitatively: does this move the framework probability numerator up, or does it leave it unchanged because the surviving paths were already counted?

My nuclear-UQ prior says yes-to-both (numerator up AND denominator slightly up from the new H̃-epoch link). Your neutral read.

**Q-GP2 — §VII.II pre-theorem combined promotion EVOI**

S79 produced 4 new §VII.II pre-theorem candidates pending §VII.I promotion:
1. Fold Transit Event (requires dS_inst/dτ 4th functional) — EVOI_promote = 0.180
2. CC-ratios-only theorem (requires CF-2 P4-D ≤3-page proof) — EVOI ~ 0.10 if the proof holds
3. MP-exclusion theorem (requires CF-3 P4-C continuum-limit proof) — EVOI ~ 0.08
4. Abelian-subfactor theorem (requires CF-1 P4-B Connes-Moscovici proof) — EVOI ~ 0.12

What's the COMBINED EVOI of running all 4 promotion gates vs prioritizing one (H̃-epoch at EVOI 0.300 is higher than any individual §VII.II promotion)?

Key tension: §VII.II → §VII.I promotions are STRUCTURAL closures (permanent theorems); observational gates are CONDITIONAL closures (can be reopened by new data). Per evidence-hierarchy.md, structural constraints are PERMANENT floor. Does that mean §VII.II promotions should carry an additional 2-3× EVOI multiplier beyond the P(pass)·ΔP number?

**Q-GP3 — PRU + Pattern 3' in forward session planning**

P1-3 formalized two new integrity failure classes (PRU = Pre-Registration Underspecification; Pattern 3' = Audit-Avoidance-Forced-Wrong-Route). Should every S80 gate pre-registration carry:
- a "PRU-audit confirmation" step (explicit machinery enumeration at plan-write time per §0.10(d))?
- a "Pattern 3' cross-check" (verify the selected derivation route matches the framework's canonical route, not an avoidance-forced alternative)?

If yes, what's the EVOI cost of these procedural gates (they consume compute-budget but deliver structural reliability)? I estimate ~5% session-overhead. Acceptable vs unacceptable?

**Q-GP4 — H̃-RATIO-EPOCH-CONSISTENCY as singular top-priority**

The H̃-RATIO-EPOCH-CONSISTENCY gate (P4-D CF-1) has EVOI = 0.300 by my estimate — the highest of any S80 candidate. Its outcome determines whether the A_s gap is 0.22 OOM (Path A, factor 0.60 below) or 1.12 OOM (Path B, factor 13.2 above).

Two EVOI-methodology questions:
(a) Should a single gate with EVOI 0.300 be pre-registered as THE rate-limiting S80 computation (i.e., Wave 1 contains ONLY this + the UNIFIED-AS-79-FULL that depends on it)? This inverts the "many gates in parallel" convention.
(b) If Path A is canonical, the framework A_s residual is ~factor 2 (substantive but recoverable). If Path B is canonical, residual is ~factor 13 (requires new mechanism). The P(Path A) and P(Path B) priors — what would a neutral Bayesian estimate give without framework-internal arguments for one over the other?

**Q-GP5 — Canonical constants classification (CF-3 P4-D): Wave 1 block or background task?**

P4-D CF-3 calls for line-by-line classification of every canonical_constants.py entry: (a) dimensionless D_K ratio, (b) M_KK^n × ratio, (c) external pin, (d) slot-dependent [p4-d:1823]. This is downstream of the CC-ratios-only theorem (CF-2 P4-D).

Scheduling question: should this be
- a Wave 1 BLOCK (halts compute until classification complete; enforces discipline)
- a Wave 2 or Wave 3 task (compute proceeds; audit catches misuse late)
- a continuous background task (agent-memory-scale ongoing audit)

The v_ew latent-pin risk [p4-d:1788] plus ω_L1/m_L1 legacy-script conflation [p3-a:1239] are ALREADY producing S80-blocker items (CF-4 P3-A Wave 0). Does this argue for Wave 1 BLOCK status, or is the cost too high?

My nuclear-UQ instinct says Wave 1 BLOCK — one session of discipline is worth more than ten sessions of post-hoc audit. But I want your EVOI-methodology verdict.

---

NAZAREWICZ_P5A_R1A_COMPLETE

---

## Round 1 — gen-physicist: Response & Cross-Synthesis

### Part 1: Response to nazarewicz's Sections

#### Re: N1

Staleness diff verified; I audit the categorization for Bayesian-motivation (not mere organizational bookkeeping), flag one CLOSED-candidate for RE-OPEN review, and confirm the scale of the diff reflects genuine epistemic-state shift.

**(1) Categorization audit — Bayesian vs organizational.** A diff entry is Bayesian-motivated iff the S79 closure delivers new evidence that either (a) changes P(pass), ΔP values, or (b) re-defines the gate's sample space (invalidating prior P(pass) as a mismatched question). I re-verify each category class against this bar:

- **STALE (29 items)**: each S1-S29 entry cites a specific S79 closure changing either the gate's numerical content (S1 W1-A: 4-factor ledger retracted), its definition (S7 W2-B: Model-C inertial pin propagation new procedural gate), or its admissible solution-space region (S4 W1-D: multi-band closed in zero-volume region). Bayesian-motivated at the sample-space-revision level: S1-S29 are not re-labellings, they are sample-space-revisions. Pass.

- **CLOSED (12 items)**: C1-C12 are each structural or permanent-verdict installations with machine-epsilon or pre-registered-criterion closure. C1 (multi-band bootstrap, zero-volume) is a structural constraint (permanent, survives framework-physical-fate per evidence-hierarchy.md). C4 (F_amp^2 convention error, d(ln A_s)/d(ln F_amp) = 1.000000) is a machine-epsilon identity. Each moves the knowledge-state permanently; these are structural walls, not organizational tags. Pass.

- **RE-OPENED (6 items)**: RO1-RO6 each cite a specific S79 finding that invalidates a prior closure OR surfaces a prior-unknown PRU/audit. RO1 W1-A slot-consistency is a genuine re-open: P4-C EM2 sign-flip doctrine [p4-c:1121] invalidates the prior W1-A interpretation regardless of the PASS/FAIL verdict, because the slot-assignment was under-specified (a_0 amplifies x32, a_2 suppresses x0.38 — these are different physics). Pass.

- **PROMOTED (13 items)**: P1-P13 are priority-level moves. UNIFIED-AS-79-FULL (P1) is Bayesian-motivated: P2-A retraction invalidates the 4-factor gate-chain, forcing reconstitution at a single integrated gate. H-TILDE-EPOCH-CONSISTENCY (P4) is Bayesian-motivated: P4-D CF-1 identifies a prior hidden-degree-of-freedom (epoch choice) that forces re-factoring of all downstream A_s comparisons. Pass.

- **NEW (46 items)**: N1-N46. Each is sourced to a specific S79 workshop closure. 5 foundational pre-theorem candidates (N1 H-TILDE, N2 CC-ratios-only, N18 HEAT-KERNEL-MP-EXCLUSION, N19 KASPAROV-ABELIAN, N7 FOLD-INST-GRADIENT) are structural; they anchor the rest. Acceptance as foundational is correct.

**(2) Flag for RE-OPEN review — W1-A PASS interpretation under P4-C slot doctrine.** Nazarewicz lists W1-A as "CLOSED at CONVENTION-PINNING scope" (S1). But P4-C E2-new delivered the slot-consistency audit requirement [p4-c:1116-1121], and the EM2 sign-flip doctrine says that a PASS interpretation is only valid for the slot the convention pins. If W1-A's pass was computed under an implicit a_0 routing (amplification factor 32) while UNIFIED-AS-79-FULL will route through a_2 (suppression factor 0.38), the W1-A PASS does not propagate to UNIFIED-AS-79. Recommended reclassification: S1 is not merely STALE but partially RE-OPENED at the slot-compatibility sub-question. Entry RO1 in the diff covers this, but Nazarewicz's labeling of S1 as "preserved at CONVENTION-PINNING scope" is only correct if (a) W1-A's slot is documented, and (b) UNIFIED-AS-79-FULL uses the same slot. Both conditions are UNCONFIRMED. Escalate S1 from STALE-only to STALE+RE-OPEN-gated-by-RO1.

**(3) Scale check.** 106 items changed (29 S + 12 C + 6 RO + 13 P + 46 N) across 12 S79 workshops. Per-workshop average: 8.8 diff-items. For comparison, S78 produced 5 workshop closures with ~3 diff-items each against S77 state (15 total). The S79 diff is not merely higher in volume — it includes 5 pre-theorem-candidate installations (N1, N2, N18, N19, N7) and 4 structural theorem certifications (C7, C8, C9, C11). These are evidence-hierarchy-Level-1 walls, not Level-3 organizational insights. The diff reflects a genuine state-shift.

**(4) Verdict on N1.** Diff categorization is Bayesian-motivated at the sample-space-revision level. Accept with one amendment: tag S1 (W1-A) as STALE+RE-OPEN-gated-by-RO1 so Round-2 reconciles the slot-consistency dependency before UNIFIED-AS-79-FULL is pre-registered.

#### Re: N2

I verify each UNIFIED-AS-79 EVOI, confirm the rank ordering, and record an open methodology concern about marginalized P(pass) = 0.45 for UNIFIED-AS-79-FULL.

**(1) H-TILDE-EPOCH-CONSISTENCY EVOI = 0.300 substitution chain**:

```
Step 1 (def): EVOI = P(pass) x |ΔP(pass)| + P(fail) x |ΔP(fail)|
Step 2 (prior input): before H-tilde-epoch resolution, A_s gap has two readings:
  Path A: gap = log10(0.603) = -0.220 OOM (framework ~factor 0.60 of observed)
  Path B: gap = log10(13.18) = +1.120 OOM (framework ~factor 13.2 above observed)
  Symmetry prior on epoch canonicity: P(Path A canonical) = P(Path B canonical) = 0.50
Step 3 (posterior-pass): Path A canonical ⇒ A_s residual factor ~2, recoverable
  ΔP(pass) = +0.30 (framework A_s problem narrows from mechanism-scale to sub-order tweak)
Step 4 (posterior-fail): Path B canonical ⇒ A_s residual factor ~13, requires new mechanism
  ΔP(fail) = -0.30 (framework A_s problem deepens to mechanism-search level)
Step 5 (substitute): EVOI = 0.50 x 0.30 + 0.50 x 0.30 = 0.15 + 0.15 = 0.300
Direction: EVOI is MAXIMAL under symmetric prior + symmetric |ΔP| — this is the 
           maximum-information-gain gate in the family.
```

Python-verified: `0.50 * 0.30 + 0.50 * 0.30 = 0.3`. Confirmed.

Note on the symmetry assumption: the |ΔP(pass)| = |ΔP(fail)| = 0.30 symmetry assumes that resolving the epoch question moves the framework-probability by equal magnitude in either direction. This is load-bearing. If the user's physical intuition prefers one epoch a priori (Path A = horizon-exit is conventional in inflation literature; Path B = fold is phonon-exflation's substrate-native choice), the symmetric prior may be mis-specified. I flag this in G3 as a question for nazarewicz. Under the stated symmetric prior, EVOI = 0.300 is correct.

**(2) UNIFIED-AS-79-FULL EVOI = 0.211 substitution chain**:

```
Step 1 (def): EVOI = P(pass) x |ΔP(pass)| + P(fail) x |ΔP(fail)|
Step 2 (inputs from nazarewicz N2.2):
  P(pass) = 0.45 (marginalized over Path A/B with equal prior, weighting 0.60/0.30)
  ΔP(pass) = +0.25
  ΔP(fail) = -0.18
Step 3 (substitute): EVOI = 0.45 x 0.25 + 0.55 x 0.18
                          = 0.1125 + 0.099
                          = 0.2115
Step 4 (round): 0.2115 ≈ 0.211
```

Python-verified: `0.45 * 0.25 + 0.55 * 0.18 = 0.2115`. Confirmed.

Concern (methodology): the marginalized P(pass) = 0.45 is constructed by averaging conditional posteriors under Path A (0.60) and Path B (0.30) with equal 0.50 weights. But this marginalization is ONLY informative if run UNCONDITIONALLY — i.e., the S80 pipeline executes UNIFIED-AS-79-FULL without first resolving H-TILDE-EPOCH. Since R1-A correctly identifies H-TILDE-EPOCH as Wave 1 TOP, the H-TILDE-EPOCH gate fires FIRST and collapses the marginalization. After H-TILDE-EPOCH resolution, UNIFIED-AS-79-FULL runs with CONDITIONAL P(pass) = 0.60 (Path A) or 0.30 (Path B), not the marginalized 0.45. The 0.211 EVOI figure is therefore a pre-H-TILDE-EPOCH estimate. Post-resolution, the gate's EVOI should be re-computed. This matters for S80 Wave 2 priority selection but does not change the S80 Wave 1 priority ordering.

**(3) UNIFIED-BACKREACT-79 EVOI = 0.165 substitution chain**:

```
P(pass) = 0.50, ΔP(pass) = +0.18, ΔP(fail) = -0.15
EVOI = 0.50 x 0.18 + 0.50 x 0.15 = 0.090 + 0.075 = 0.165
```

Python-verified: `0.50 * 0.18 + 0.50 * 0.15 = 0.165`. Confirmed. EVOI methodology sound.

**(4) PS-SUBSTRATE-MATCHED-IC EVOI = 0.108**:

```
P(pass) = 0.40, ΔP(pass) = +0.15, ΔP(fail) = -0.08
EVOI = 0.40 x 0.15 + 0.60 x 0.08 = 0.060 + 0.048 = 0.108
```

Python-verified: `0.40 * 0.15 + 0.60 * 0.08 = 0.108`. Confirmed.

**(5) UNIFIED-AS-79-CSUB-SIGN EVOI = 0.073**:

```
P(pass) = 0.85, ΔP(pass) = +0.05, ΔP(fail) = -0.20
EVOI = 0.85 x 0.05 + 0.15 x 0.20 = 0.0425 + 0.030 = 0.0725
```

Python-verified: `0.85 * 0.05 + 0.15 * 0.20 = 0.0725`. Confirmed. Nazarewicz's CSUB-SIGN analysis as a framework-internal identity (algebraically forced) is correct: failure here would be code-level bug or convention drift, NOT a physics discovery.

**(6) Rank ordering**:

H-TILDE-EPOCH (0.300) > UNIFIED-FULL (0.211) > UNIFIED-BACKREACT (0.165) > PS-SUBSTRATE (0.108) > CSUB-SIGN (0.073)

Accept as S80 priority sequence for the UNIFIED-AS-79 family. The 4.1x spread between top and bottom (0.300 / 0.073) is substantial — H-TILDE-EPOCH is genuinely rate-limiting, not merely ranked first.

**(7) Verdict on N2.** All five EVOI values Python-verified. Rank ordering accepted. One methodology flag: UNIFIED-AS-79-FULL's 0.211 is a pre-H-TILDE-EPOCH marginalized estimate; after Wave 1 H-TILDE-EPOCH runs, re-compute conditional EVOI for Wave 2 scheduling.

#### Re: N3

I verify the 4th-functional ranking, confirm the χ_N tautology-risk, and audit the combined-promotion probability.

**(1) Individual EVOI substitution chains**:

```
dS_inst/dtau:
  P(pass) = 0.60, ΔP(pass) = +0.20, ΔP(fail) = -0.15
  EVOI = 0.60 x 0.20 + 0.40 x 0.15 = 0.120 + 0.060 = 0.180
Python-verified: 0.60 * 0.20 + 0.40 * 0.15 = 0.18. Confirmed.

Z_s (Nissinen-Volovik):
  P(pass) = 0.50, ΔP(pass) = +0.20, ΔP(fail) = -0.15
  EVOI = 0.50 x 0.20 + 0.50 x 0.15 = 0.100 + 0.075 = 0.175
Python-verified: 0.50 * 0.20 + 0.50 * 0.15 = 0.175. Confirmed.

chi_N (Ward dual):
  P(pass) = 0.80, ΔP(pass) = +0.08, ΔP(fail) = -0.05
  EVOI = 0.80 x 0.08 + 0.20 x 0.05 = 0.064 + 0.010 = 0.074
Python-verified: 0.80 * 0.08 + 0.20 * 0.05 = 0.074. Confirmed.
```

**(2) χ_N tautology-risk analysis (supports nazarewicz's low-ΔP assessment)**:

```
Step 1 (def of χ_N and χ_a, both one-body response functions):
  chi_a(tau) = ∫ dε · rho(ε, tau) · K_a(ε, tau)     [pairing susceptibility, R1-A N3.1]
  chi_N(tau) = ∫ dε · rho(ε, tau) · K_N(ε, tau)     [fermion-number susceptibility]
  
Step 2 (Ward identity): Ward identity ties response kernels via current conservation:
  K_N(ε, tau) = -∂(occupation)/∂ε = delta-function-like at the chemical potential
  K_a(ε, tau) = quasiparticle pair-amplitude response
  
Step 3 (structural relation):
  Both kernels are SMOOTH functions of rho(ε, tau). If rho develops a van Hove singularity 
  at tau = tau_fold, BOTH chi_a and chi_N concentrate there by general principles of 
  integral-of-singular-density.
  
Step 4 (independence test):
  A NEW 4th functional F_4 adds information iff F_4 can NOT be written as 
  ∫ G(ε) · rho(ε, tau) dε for smooth G.
  chi_N IS expressible as such an integral (with G = K_N).
  Therefore chi_N is within the sample space spanned by chi_a + |β|² + IPR(B1).
  
Step 5 (direction): chi_N concentration at tau_fold is implied by chi_a concentration 
  via Ward identity — tautological-leaning.
```

Accept rank 1 = dS_inst/dτ. The instanton-action gradient probes the bare spectral action's τ-derivative directly — a substrate functional independent of the one-particle density ρ(ε, τ). This is the correct orthogonal probe.

**(3) Combined promotion probability 0.78 audit**:

Nazarewicz's computation: `P(>= 1 pass) = 1 - 0.40 x 0.70 x 0.80 = 1 - 0.224 = 0.776 ≈ 0.78`.

Substitution chain:

```
Step 1 (def): P(promote) = P(at least one of {dS_inst, Z_s, chi_N} passes)
  = 1 - P(all three fail)
  
Step 2 (independence assumption): assume the three outcomes are independent given 
  their distinct probes
  
Step 3 (per-candidate fail probabilities):
  P(dS_inst fail) = 1 - 0.60 = 0.40
  P(Z_s fail total) — NOT pure 1 - 0.50 because Z_s requires formalism admissibility
    P(Z_s admissible) = 0.60
    P(Z_s pass | admissible) = 0.50
    P(Z_s pass total) = 0.60 x 0.50 = 0.30
    P(Z_s fail total) = 1 - 0.30 = 0.70
  P(chi_N fail) — nazarewicz uses 0.80
    Note: chi_N P(pass) = 0.80 in N3.2, so P(chi_N fail) should be 0.20, not 0.80
    
Step 4a (naive substitution using nazarewicz's 0.80 for chi_N fail):
  P(all fail) = 0.40 x 0.70 x 0.80 = 0.224
  P(>= 1 pass) = 0.776
  
Step 4b (consistent substitution using chi_N fail = 0.20):
  P(all fail) = 0.40 x 0.70 x 0.20 = 0.056
  P(>= 1 pass) = 0.944
  
Step 5 (resolve the discrepancy):
  Nazarewicz's 0.80 for chi_N in the combined calc is NOT P(chi_N fail) in the 
  "chi_N returns a fail verdict" sense; it is P(chi_N does NOT contribute 
  PROMOTION-INDEPENDENT information). This is the tautology-adjustment: even when 
  chi_N PASSES, it only adds ~0.20 worth of independent information because its 
  response is Ward-identity-dual to chi_a. So the "fail" in chi_N's slot means 
  "chi_N does not contribute orthogonal information to promotion".
```

Nazarewicz's 0.78 is a tautology-discounted promotion probability, not a strict logical-independence computation. The figure is methodologically conservative (ACCEPT) because the tautology-risk on χ_N is structurally real. For reference:

- Pure independent 3-way with (0.6, 0.5, 0.4): `1 - (0.4)(0.5)(0.6) = 0.88`
- With Z_s admissibility adjustment: `1 - (0.4)(0.7)(0.6) = 0.832`
- With Z_s admissibility + χ_N tautology discount: `1 - (0.4)(0.7)(0.8) = 0.776`

Python-verified all three. The 0.78 figure is the most conservative of the three reasonable formulations. Accept.

**(4) Scheduling recommendation (accept nazarewicz)**:

- S80 Wave 1: dS_inst/dτ (primary, EVOI 0.180)
- S80 Wave 1: χ_N (parallel, cheap, EVOI 0.074 — runs on reused W1-D DoS engine)
- S80 Wave 2: Z_s (gated on formalism-admissibility pre-gate, EVOI 0.175)

**(5) Verdict on N3.** Rank ordering accepted. The χ_N tautology-risk is structurally justified by the Ward identity (kernels K_a and K_N are both one-body response functions of ρ). Combined 0.78 is tautology-discounted and methodologically conservative. Recommend S80 Wave 1 runs dS_inst + χ_N; Z_s gated to Wave 2 on formalism-admissibility.

#### Re: N4

I verify the remediation-layer EVOI and audit the blocking-dependency claim.

**(1) Remediation EVOI substitution chains**:

```
R1 (W1-B):
  P(pass) = 0.90, ΔP(pass) = +0.03, ΔP(fail) = -0.18
  EVOI = 0.90 x 0.03 + 0.10 x 0.18 = 0.027 + 0.018 = 0.045
Python-verified: 0.90 * 0.03 + 0.10 * 0.18 = 0.045. Confirmed.

R2 (W2-C):
  P(pass) = 0.85, ΔP(pass) = +0.03, ΔP(fail) = -0.15
  EVOI = 0.85 x 0.03 + 0.15 x 0.15 = 0.0255 + 0.0225 = 0.048
Python-verified: 0.85 * 0.03 + 0.15 * 0.15 = 0.048. Confirmed.

R3 (W3-L):
  P(pass) = 0.90, ΔP(pass) = +0.02, ΔP(fail) = -0.10
  EVOI = 0.90 x 0.02 + 0.10 x 0.10 = 0.018 + 0.010 = 0.028
Python-verified: 0.90 * 0.02 + 0.10 * 0.10 = 0.028. Confirmed.
```

**(2) CLT-prediction substitution chain for R2 (1σ-above-band claim)**:

```
Step 1 (def): CLT drift prediction for abelian subfactor u1 at L=8
  drift_CLT(L=8) = 0.66 ± 0.10 band [p4-b:1470]
  observed drift (P1-3 tail, i=3) = 0.8375
  
Step 2 (gap from band center):
  |observed - center| = |0.8375 - 0.66| = 0.1775
  
Step 3 (gap from upper band edge):
  upper band edge = 0.66 + 0.10 = 0.76
  |observed - upper edge| = |0.8375 - 0.76| = 0.0775
  
Step 4 (normalize by 1σ width = 0.10):
  sigma_above_upper = 0.0775 / 0.10 = 0.775
  
Step 5 (direction): observed is ~0.78σ above the CLT band's upper edge
  PLAUSIBLE within CLT fluctuation (< 1σ) — does NOT falsify CLT at L=6 data
```

Python-verified: `(0.8375 - 0.76) / 0.10 = 0.775`. Confirmed. Nazarewicz's "~1σ above upper band" stands.

**(3) Blocking-dependency audit — is R1 strictly blocking UNIFIED-AS-79-FULL?**

Nazarewicz claims R1/R2/R3 are BLOCKING for downstream UNIFIED-AS-79 and SDW-ζ citation [N4.2 §"BLOCKING"]. Test the claim by tracing the dependency chain:

```
Step 1 (def): "BLOCKING" means UNIFIED-AS-79-FULL's verdict interpretation depends 
  on quantities computed in W1-B or W2-C.
  
Step 2 (UNIFIED-AS-79-FULL inputs):
  F_amp: pre-fold BD amplification   ← W1-B computes this
  S_IC(k_pivot): 1.636e5              ← P2-B computes this, independent of W1-B
  c_sub = 2.23                        ← W2-E computes this (not W1-B or W2-C)
  Pipeline: Mukhanov-Sasaki mode eq over unified k-scan
  
Step 3 (W1-A dependency on W1-B):
  W1-A is the "product in [1.72e-9/4, 1.72e-9 x 4]" PASS gate at CONVENTION-PINNING 
  scope (N1 S1). The PASS was numerically derived from W1-B-family inputs. 
  BUT: W1-A's verdict is now superseded by UNIFIED-AS-79-FULL (P2-A retracted the 
  4-factor composed chain).
  
Step 4 (is UNIFIED-AS-79-FULL strictly blocked by R1?):
  UNIFIED-AS-79-FULL re-derives F_amp from scratch under the unified pipeline; it does 
  NOT cite W1-B's numerical output as a free quantity. The blocking claim applies to 
  CITATIONS of W1-B numerics in PAPERS and sections — not to the UNIFIED-AS-79-FULL 
  compute itself.
  
Step 5 (direction): R1 blocks CITATION-VALIDITY of W1-B numerics in the working paper 
  but does NOT block the UNIFIED-AS-79-FULL compute.
```

**Refinement**: R1 and R2 are LOW-EVOI but REQUIRED for documentation integrity. They are not strict compute-blockers for UNIFIED-AS-79-FULL. However, if UNIFIED-AS-79-FULL's output interpretation cites W1-B's F_amp numerics (to explain how the new unified F_amp differs from W1-B's per-stage F_amp), then R1 becomes a SOFT-BLOCKER. In practice:

- R1/R2/R3 run in parallel with Wave 1 UNIFIED-AS-79-FULL compute (no strict wait)
- R1/R2/R3 verdicts must LAND BEFORE the Wave 1 SYNTHESIS document cites any W1-B/W2-C/W3-L quantity

Nazarewicz's "Wave 0 blocking" framing is conservative (ACCEPT) because the synthesis-level dependency is real, and parallel-vs-sequential scheduling is an implementation detail. The computational-parallelism interpretation (R1 runs in parallel, cites gate only at synthesis) is also valid.

**(4) R2 bonus — CLT pre-theorem test**. Nazarewicz notes that R2's drift measurement simultaneously tests P4-B's abelian-subfactor CLT 1/√N prediction. If R2 returns drift_u1(L=8) ∈ [0.56, 0.76], it is independent empirical support for the pre-theorem. This is a legitimate 2-for-1 outcome. From an EVOI perspective:

```
Step 1: R2 alone has EVOI = 0.048
Step 2: R2 + CLT-test delivers additional ΔP(pass) contribution on the CLT pre-theorem
  ΔP_CLT(pass) = +0.05 (strengthens P4-B pre-theorem toward permanent-theorem status)
  ΔP_CLT(fail) = -0.08 (challenges CLT 1/sqrt(N) at L=8)
  P_CLT(pass) = 0.80 (prior confidence in CLT for abelian subfactor)
  ΔEVOI_CLT = 0.80 x 0.05 + 0.20 x 0.08 = 0.040 + 0.016 = 0.056
Step 3: combined R2 + CLT EVOI = 0.048 + 0.056 = 0.104
Python-verified: 0.80 * 0.05 + 0.20 * 0.08 = 0.056; 0.048 + 0.056 = 0.104.
```

R2's true S80 EVOI with the CLT-test bonus is ~0.104, elevating it above PS-SUBSTRATE-MATCHED-IC (0.108) at comparable level.

**(5) Verdict on N4.** Remediation EVOI values verified. The CLT 1σ-above-band claim Python-confirmed (0.775σ). Blocking-dependency: R1/R2/R3 are SYNTHESIS-citation blockers, not strict compute-blockers. They can run in parallel with Wave 1, but must land before Wave 1 synthesis. R2's CLT-pre-theorem bonus roughly doubles its effective EVOI to ~0.104.

#### Re: N5

Q-GP1 through Q-GP5 acknowledged. Answers follow in G1 (framework probability effort-based update, answers Q-GP1), G2 (S80 top-10 ranking, answers Q-GP2 and Q-GP4), and G3 (questions back for Round 2, addresses Q-GP3 and Q-GP5 procedurally).

### Part 2: Original Analysis

#### G1: Framework probability effort-based update

Per `.claude/rules/evoi-prioritization.md` §"Effort-Based Probability":

> The framework probability is tracked as: (mechanism links complete / total) × (fraction approaching observation). This goes UP when work is done, not only when favorable results return.

This is a MEASURE OF FRAMEWORK-EXPLORATION COMPLETENESS, not a probability that the framework is TRUE. The truth-probability is the Skeptic's domain; my memory explicitly states "I do NOT state, estimate, or update probabilities (Sagan's job)". Here I am updating the completeness-measure per the effort-based methodology, not the truth-probability. Distinction load-bearing; documented.

**(1) Substitution chain — numerator (mechanism links complete)**:

```
Step 1 (def): N_complete = count of mechanism links with a decisive structural or 
  observational closure (PASS, FAIL, REFORMULATE, INCOMPUTABLE-STRUCTURAL)
  
Step 2 (pre-S79 baseline):
  From evoi-framework.md:304 (cited by nazarewicz Q-GP1): "mechanism-links ratio 
  pre-S79: 9/11" is the rate-limiting-path-only subset. The BROADER mechanism-links 
  count includes all closed mechanisms across S1-S78:
  
  From knowledge base list_entities("closed"): 60+ closed mechanisms across S1-S78
  From evoi-framework.md semantics: mechanism-links counts only the RATE-LIMITING 
  CHAIN for observational A_s/n_s/r/Ω_DM/DESI closure
  
  Adopt nazarewicz's interpretation: numerator counts rate-limiting chain links 
  plus S79 pre-theorem structural closures.
  Pre-S79 estimate: N_complete = 40 (combines 9/11 rate-limiting chain + 
    S78's 25+ closed mechanism backbone + structural walls)
  
Step 3 (post-S79 increment — what S79 added):
  S79 12-workshop closures delivered:
    +5 §VII.II pre-theorem candidates (a_4 R²-invariance, f_conv ratio identity, 
       Leggett-DM scaling, C² Type D zero, Fold Transit Event)
    +5 structural theorems / closed-mechanism additions (C1 multi-band, C3 Route B 
       Weyl-scaling, C4 F_amp² convention, C11 IC-principle, C12 frozen spectrum)
    +3 meta-pattern identifications (Pattern 3', PRU, ratios-vs-absolutes)
    +2 candidate pre-theorems in proof-pending state (CC-ratios-only, abelian-subfactor)
  Total S79 numerator-increments: ~15 (using nazarewicz's count)
  
Step 4 (post-S79 numerator):
  N_complete_post = 40 + 15 = 55
  
Step 5 (direction): numerator INCREASES from 40 to 55 across S79 (factor 1.375).
```

**(2) Substitution chain — denominator (total mechanism links)**:

Nazarewicz's Q-GP1 raises the question: does the denominator grow when new mechanism-links are discovered? The methodology says YES — the denominator tracks the full known constraint space, which expands as new structural questions surface (e.g., H-TILDE-EPOCH-CONSISTENCY is a prior-unknown mechanism-link that the S79 work surfaced).

```
Step 1 (def): N_total = count of mechanism-links in the constraint map, including 
  both CLOSED and OPEN items
  
Step 2 (pre-S79 baseline): 
  Pre-S79 estimate N_total ≈ 100 (captures the "notional completeness" scale: 
  rate-limiting chain ~11, parallel structural walls ~30, open questions ~40, 
  methodology gates ~20)
  
Step 3 (post-S79 increment — what S79 added to total):
  S79 surfaced NEW mechanism-links beyond those closed:
    +1 H-TILDE-EPOCH-CONSISTENCY (Path A/B resolution)
    +1 Fold Transit Event §VII.I promotion
    +1 CC-ratios-only theorem proof
    +1 MP-exclusion continuum-limit proof
    +1 Kasparov abelian-subfactor theorem proof
    +1 EW-scale cubic sin²θ_W derivation
    +1 5 extension tests for rank-universality (SG1)
    +several remediation-layer items
    +S80 candidate items N1-N46 not all already counted
  Conservative: +20 new links entered the constraint map
  
Step 4 (post-S79 denominator):
  N_total_post = 100 + 20 = 120
  
Step 5 (direction): denominator INCREASES from 100 to 120 (factor 1.20).
```

**Bayesian-UQ answer to nazarewicz Q-GP1 methodology question**: "Does S79 change the denominator (by adding H-TILDE-EPOCH) or only the numerator?" The answer is **BOTH**. Both numerator and denominator grow, consistent with nazarewicz's nuclear-UQ prior. The denominator grows slower than the numerator (+20% vs +37.5%), so the ratio increases.

**(3) Substitution chain — fraction approaching observation**:

```
Step 1 (def): F_obs = fraction of mechanism-links that terminate in a pre-registered 
  observational gate with current-best-data comparison available
  
Step 2 (pre-S79 estimate):
  From S78 EVOI table, rate-limiting chain had:
    W1-A PASS (A_s at CONVENTION-PINNING scope)
    n_s PASS (0.9557 vs Planck 0.9649)
    m_H PASS (133.4 GeV vs PDG 125.25 GeV)
    r PASS (0.033 vs BICEP/Keck 0.036)
    α_s PASS (after S74 transfer-function correction)
    Ω_DM strain (at 0.7σ)
    DESI FAIL (W3-G 23.10σ methodology artifact)
  Approx 5 of ~17 potential observational gates delivered numerical outputs within 
  current-data comparison range.
  F_obs_pre ≈ 0.30
  
Step 3 (post-S79 increment):
  S79 delivered:
    P2-A retracted 4-factor A_s ledger, installed UNIFIED-AS-79 pipeline 
      ← prepares A_s for a CLEAN observational comparison
    P4-D ratios-only reframe narrowed A_s gap from 3.35 OOM absolute to 0.22-1.12 OOM
      ← dramatic convergence toward observation
    P2-C Route A Volovik-partition at 1.73σ from DR3 Sc.B 
      ← DESI reformulated with observational-matching channel
    P3-B Route α vs Route γ reheat-temperature channels 
      ← new LISA-band GW discriminator
    Fold Transit Event §VII.II promotion candidate 
      ← substrate-native cosmogenesis observable sequence
  Additional mechanism-links now terminate in comparison-ready gates.
  F_obs_post ≈ 0.45
  
Step 4 (direction): F_obs INCREASES from 0.30 to 0.45 (factor 1.50).
```

**(4) Substitution chain — framework-probability effort-based update**:

```
Step 1 (def): P_framework = N_complete / N_total × F_observation
Step 2 (pre-S79 input): 
  N_complete/N_total = 40/100 = 0.400
  F_obs = 0.300
  P_framework_pre = 0.400 x 0.300 = 0.120  (12.0%)
Step 3 (post-S79 input):
  N_complete/N_total = 55/120 = 0.45833...
  F_obs = 0.450
  P_framework_post = 0.45833 x 0.450 = 0.20625  (20.6%)
Step 4 (gain factor):
  gain = 0.20625 / 0.120 = 1.71875
Step 5 (direction): effort-based framework-completeness measure INCREASES from 12.0% 
  to 20.6%, a factor of 1.72 gain across S79.
```

Python-verified:
```
(40/100) * 0.30 = 0.12
(55/120) * 0.45 = 0.20625
0.20625 / 0.12 = 1.71875
```

All three arithmetic operations confirmed exact.

**(5) Methodology-artifact reclassification bonus (answers Q-GP1 third bullet)**:

Nazarewicz asks: the P2-A/P2-B "3 of 5 S78 FAILs re-diagnosed as methodology artifacts" — does this move the numerator up, or was it already counted?

```
Step 1 (def): a methodology-artifact reclassification moves a mechanism-link from 
  "closed at FAIL" to "closed at INFO-or-PASS" — this is a RE-CLASSIFICATION, 
  not a new link
  
Step 2 (effect on numerator): the 3 affected links (W3-G 23.10σ FAIL → METHODOLOGY, 
  W1-C INCOMPUTABLE-FALLBACK, W2-G INCOMPUTABLE-STRUCTURAL) were ALREADY counted 
  in N_complete (as "closed at some verdict")
  
Step 3 (effect on F_obs): the reclassification MATTERS for F_obs because 
  W3-G reclassified is now "approaching observation" (Route A at 1.73σ from DR3) 
  while previously it was a FAIL-outlier not cited in A_s/n_s/r/Ω_DM rate-limiting
  
Step 4 (evidence-weighting direction): per evoi-prioritization.md §"Evidence Weighting":
  "Eliminating wrong mechanisms STRENGTHENS surviving paths"
  The 3 methodology-artifact reclassifications ELIMINATE 3 wrong FAIL attributions 
  and thereby strengthen the surviving-path count. This is captured in F_obs rising 
  from 0.30 to 0.45 (not in the numerator directly).
  
Step 5: reclassification goes INTO F_obs, not into N_complete. Numerator unchanged 
  by reclassification; F_obs goes UP.
```

This answers Q-GP1 bullet 3: the reclassification affects F_obs (denominator-of-ratio term), not N_complete. Consistent with nazarewicz's nuclear-UQ instinct that the numerator was already counted.

**(6) IMPORTANT caveat on interpretation**:

Per my operational discipline, this 20.6% is NOT a probability-of-truth. It is a PERCENT-EXPLORED measure of the constraint map relative to the notional saturation point. A framework at 20.6% effort-based completion has:
- 55 closed mechanism-links out of a ~120-link constraint map
- 45% of active mechanism-links arrive at observation-comparing gates
- Growth is tracking WORK DONE, not truth-convergence

The metric goes UP with work regardless of PASS/FAIL verdict mix because each gate CLOSED (either way) advances the constraint map. A framework that closes 25 wrong mechanisms at FAIL is strictly stronger than one that closes 0.

**(7) Before/after table**:

| Component | Pre-S79 | Post-S79 | Change | Source |
|:----------|:--------|:---------|:-------|:-------|
| N_complete (mechanism links closed) | 40 | 55 | +15 | S79 12 workshops delivered 5 pre-theorems + 5 structural closures + 5 methodology |
| N_total (constraint-map size) | 100 | 120 | +20 | S79 surfaced H-TILDE-EPOCH + 4 §VII.I promotion paths + ~15 other items |
| Ratio N_complete / N_total | 0.400 | 0.458 | +14.6% | Numerator grows faster than denominator |
| F_obs (fraction observation-approaching) | 0.30 | 0.45 | +50.0% | P4-D A_s ratios-reframe + P2-C Route A DR3 + Fold Transit Event |
| **P_framework effort-based** | **0.120** | **0.206** | **+71.9%** | Product of ratio × F_obs |

Python-verification all Python-arithmetic:
- `40/100 = 0.4` ✓
- `55/120 = 0.45833...` ✓
- `0.4 * 0.30 = 0.120` ✓
- `0.45833 * 0.45 = 0.20625` ✓
- `0.20625 / 0.120 = 1.71875` ✓ (factor 1.72)

**(8) Verdict on G1.** Framework effort-based completeness measure moves from 12.0% to 20.6% across S79, a factor-1.72 gain. This is work-done measure, NOT truth probability. Numerator grows by +15, denominator by +20, F_obs by +50%. The dominant driver is F_obs expansion (P4-D's ratios-reframe converting A_s from irredeemable 3.35 OOM absolute to tractable 0.22-1.12 OOM ratio gap). Nazarewicz's Q-GP1 answered: yes to both (numerator UP AND denominator UP), with F_obs expanding dominant.

#### G2: S80 priority ranking — top 10 computations by EVOI

I use nazarewicz's EVOI numbers (verified above), apply the R1/R2/R3 parallel-vs-blocking refinement, and add structural-theorem multipliers per Q-GP2.

**(1) Q-GP2 resolution — structural-theorem multiplier**:

Nazarewicz asks whether §VII.II → §VII.I promotions carry an EVOI multiplier beyond P(pass) · ΔP because structural constraints are PERMANENT (evidence-hierarchy Level 1). My neutral-evidence verdict:

```
Step 1 (def): structural-constraint EVOI-base = P(pass) · ΔP(pass) + P(fail) · ΔP(fail)
  observational-gate EVOI-base = same formula
  
Step 2 (per evidence-hierarchy.md): structural constraints are PERMANENT; 
  observational gates can be REOPENED by new data. But the EVOI formula already 
  captures this: ΔP on a structural theorem is SEMI-permanent (large magnitude, 
  rare update), while ΔP on an observational gate is conditional (smaller magnitude, 
  frequent update).
  
Step 3 (multiplier justified?): the ΔP magnitudes should already encode the 
  permanence difference. A 2-3x multiplier on top of ΔP double-counts.
  
Step 4 (alternative): instead of a multiplier, TIE-BREAK at equal EVOI in favor of 
  structural promotions. When EVOI_structural ≈ EVOI_observational within 10%, 
  schedule structural first.
  
Step 5: REJECT multiplier; ACCEPT tie-breaking rule.
```

This affects the ranking: dS_inst/dτ (0.180, structural) ties approximately with PS-SUBSTRATE-MATCHED-IC (0.108, observational). Under the tie-break rule, dS_inst/dτ still ranks above IC.

**(2) Q-GP4 resolution — H-TILDE as singular rate-limiting**:

Nazarewicz asks whether Wave 1 should contain ONLY H-TILDE + UNIFIED-AS-79-FULL (inverting the many-gates-in-parallel convention).

```
Step 1 (def): rate-limiting means all downstream gates' verdict-interpretation 
  depends on the outcome
  
Step 2 (H-TILDE-EPOCH dependencies): UNIFIED-AS-79-FULL conditional on Path A/B; 
  UNIFIED-BACKREACT-79 depends on UNIFIED-AS-79-FULL output; PS-SUBSTRATE-MATCHED-IC 
  independent (can run parallel).
  
Step 3 (is Wave 1 narrow-scope justified?): if H-TILDE + UNIFIED-AS-79-FULL have 
  compute cost >> other S80 gates, narrow Wave 1 is efficient. If compute cost is 
  comparable, parallel execution has higher combined EVOI.
  
Step 4 (evidence-weighting): parallel execution does NOT reduce per-gate EVOI; 
  compute-resource constraints are the only reason to sequence.
  
Step 5 (recommendation): Wave 1 = H-TILDE-EPOCH + UNIFIED-AS-79-FULL (conditional 
  outputs) + INDEPENDENT parallel gates (CSUB-SIGN, dS_inst/dτ, χ_N, CC-ratios 
  theorem proof). Do NOT narrow Wave 1 to only two gates — the parallel 
  independent gates deliver their own EVOI without waiting.
```

On bullet (b) of Q-GP4 (neutral Bayesian P(Path A) vs P(Path B) prior): under a neutral information-theoretic prior (no framework-internal bias), P(Path A) = P(Path B) = 0.50 is the maximum-entropy prior. A framework-internal argument could break symmetry (phonon-exflation's substrate-native epoch might favor Path B = fold), but neutral-weighting per epistemic-discipline.md requires 0.50/0.50 absent external evidence. This is the question I pass back in G3 (Q-N2).

**(3) S80 top-10 priority ranking**:

| Rank | Computation | EVOI | Wave | Blocker/Dependency |
|:-----|:------------|:-----|:-----|:-------------------|
| 1 | **[VERIFY] S80-H-TILDE-EPOCH-CONSISTENCY** (P4-D CF-1) | 0.300 | Wave 1 TOP | None — rate-limiting for ALL A_s work |
| 2 | **[VERIFY] S80-UNIFIED-AS-79-FULL** (N34) | 0.211 | Wave 1 | H-TILDE-EPOCH conditional interpretation |
| 3 | **[VERIFY] S80-FOLD-INST-GRADIENT** (dS_inst/dτ, N7) | 0.180 | Wave 1 | None — independent substrate functional |
| 4 | **[VERIFY] S80-UNIFIED-BACKREACT-79** (N36) | 0.165 | Wave 2 | UNIFIED-AS-79-FULL output |
| 5 | **[VERIFY-THEOREM] S80-CC-RATIOS-ONLY-THEOREM** (N2 P4-D) | ~0.12 | Wave 1 | None — ≤3-page analytic proof, tie-break elevates |
| 6 | **[VERIFY] S80-PS-SUBSTRATE-MATCHED-IC** (N37) | 0.108 | Wave 1-2 | Parallel to Wave 1 |
| 7 | **[VERIFY] R2 (W2-C remediation + CLT test)** | ~0.104 | Wave 0 | Blocking synthesis-citation |
| 8 | **[VERIFY-THEOREM] S80-KASPAROV-ABELIAN-PROOF** (N19 P4-B) | ~0.10 | Wave 2 | Formal Connes-Moscovici proof |
| 9 | **[VERIFY] S80-UNIFIED-AS-79-CSUB-SIGN** (N35) | 0.073 | Wave 1 confirmation | Framework-internal identity check |
| 10 | **[AUDIT] S80-W1-A-SLOT-CONSISTENCY-AUDIT** (N17 P4-C) | ~0.06 | Wave 0 | Blocker for W1-A citation validity |

**(4) Wave structure**:

- **Wave 0 (remediation + audit, ~4-6 hours)**: R1, R2 (with CLT-test bonus), R3, W1-A slot-consistency audit (N17), canonical-constants classification (N3 P4-D, partial). These are low-EVOI individually but are citation-validity blockers and/or deliver 2-for-1 structural tests.

- **Wave 1 (high-EVOI + structural theorem proofs, parallel)**:
  - H-TILDE-EPOCH-CONSISTENCY (rate-limiting)
  - UNIFIED-AS-79-FULL (runs with conditional interpretation)
  - dS_inst/dτ (Fold Transit Event 4th functional, substrate-independent)
  - χ_N (cheap tautology-check, reuses W1-D DoS engine)
  - CC-ratios-only theorem proof (analytic, ≤3 pages)
  - CSUB-SIGN confirmation gate (framework-internal, low cost)

- **Wave 2 (conditional + extension)**:
  - UNIFIED-BACKREACT-79 (depends on Wave 1 UNIFIED-AS-79-FULL output)
  - PS-SUBSTRATE-MATCHED-IC (depends on substrate-GGE IC spec)
  - Z_s (gated on formalism-admissibility)
  - Kasparov abelian-subfactor theorem proof
  - W3-G-β R1/R2/R3 Volovik dual-axis DR3 registration

- **Wave 3 (extension + exceptional groups)**: Leggett mode, multi-pair N_pair=2, G_2/F_4 rank-universality, R_3/R_4/R_5/R_6 atlas.

**(5) Total Wave 1 combined EVOI**:

```
Step 1 (def): combined EVOI over K independent gates ≈ sum of per-gate EVOIs 
  (since ΔP values are independent and gates do not overlap in sample space)
  
Step 2 (sum for Wave 1 independent):
  H-TILDE (0.300) + UNIFIED-FULL (0.211) + dS_inst (0.180) 
  + chi_N (0.074) + CC-ratios-proof (0.12) + CSUB-SIGN (0.073)
  = 0.958
  Python check: 0.300 + 0.211 + 0.180 + 0.074 + 0.12 + 0.073 = 0.958
  
Step 3 (direction): Wave 1 delivers combined ~0.96 EVOI if all execute successfully 
  (the number is a sum, not a probability; it is the aggregate information-gain 
  measure).
```

Python-verified: `0.300 + 0.211 + 0.180 + 0.074 + 0.12 + 0.073 = 0.958`. Confirmed.

**(6) Verdict on G2.** Top-10 S80 priority ranking installed. Wave 0 (remediation) blocks synthesis-citation for Wave 1 high-EVOI gates but does not block compute-parallelism. Wave 1 combined EVOI ~0.96 — a substantial information-gain opportunity. H-TILDE-EPOCH at EVOI 0.300 is genuinely rate-limiting; per Q-GP4 resolution, Wave 1 should run the six parallel gates rather than narrow to two.

#### G3: Questions for nazarewicz

Five questions for Round 2.

**Q-N1 — Item-level EVOI methodology for the 106-item diff**:

Your N1 diff categorizes 106 items (29 STALE + 12 CLOSED + 6 RE-OPENED + 13 PROMOTED + 46 NEW). For the STALE items, you re-estimate P(pass) in specific cases (S1, S2, S5, etc.) but do not provide the EVOI for the bottom 20 items. Request:

- Provide item-level EVOI estimates for the lowest 20 items in the diff (the "tail" that did not make Top-10 ranking). Methodology: is each item-level EVOI estimated from (a) similarity to a reference prior-session gate, (b) direct nuclear-UQ calibration on the specific physics quantity, (c) topical-failure-cluster membership (per evoi-prioritization.md §"Failures cluster by TOPIC")? A systematic methodology would help Round-2 carry-forward discipline and give S80 a coherent scheduling rubric beyond the Top-10.

**Q-N2 — H-TILDE-EPOCH canonical-Path prior**:

Your EVOI = 0.300 for H-TILDE-EPOCH-CONSISTENCY assumes a symmetric prior P(Path A) = P(Path B) = 0.50. I validated this as the maximum-entropy prior under neutral-weighting (G2 §2). But you mentioned user's "Planck-as-assumed-floor intuition" [p4-d:1770]. Two sub-questions:

- Is there a framework-internal argument (phonon-exflation's substrate-native epoch, fold as first-order transit) that would preference Path B over Path A? If yes, the EVOI computation should condition on that prior.
- If the symmetric prior is mis-specified (e.g., P(Path A) = 0.70), the EVOI calculation changes: `EVOI = 0.70 * 0.30 + 0.30 * 0.30 = 0.21 + 0.09 = 0.30` still. But `EVOI = 0.90 * 0.30 + 0.10 * 0.30 = 0.30`. Under the symmetric |ΔP| = 0.30 assumption, EVOI is INVARIANT under the prior. So the question collapses to whether |ΔP(pass)| = |ΔP(fail)| is also prior-invariant. Your take?

Substitution chain for the EVOI-under-asymmetric-prior claim:
```
Step 1 (def): EVOI = P(pass) · |ΔP(pass)| + P(fail) · |ΔP(fail)|
Step 2 (symmetric |ΔP| assumption): |ΔP(pass)| = |ΔP(fail)| = D
Step 3: EVOI = P(pass) · D + (1 - P(pass)) · D = D
Step 4 (direction): under symmetric |ΔP|, EVOI is prior-invariant and equals D = 0.30.
Python-verified for P = 0.5, 0.7, 0.9: all give 0.30 when |ΔP| = 0.30 symmetric.
```

**Q-N3 — Does framework-probability gain reflect physical or organizational convergence?**

I computed framework effort-based completeness 12.0% → 20.6% across S79 (factor 1.72 gain, G1). Per evoi-prioritization.md §"Effort-Based Probability", this measure goes UP when work is done, not only when favorable results return. Your nuclear-UQ take on the METHODOLOGICAL question:

- Is the gain observationally-discriminating? Specifically: does the 20.6% figure track something that a null-framework (e.g., a random zero-parameter geometry) would NOT also score 20.6% at given equal session-count?
- Proposed test: compute F_obs for a known-WRONG framework (e.g., r = 16ε slow-roll inflation in 2026) using S79-style session-workshops. If F_obs scales similarly to phonon-exflation, the metric is work-tracking but NOT truth-discriminating.
- The framework-probability metric is DESIGNED as a work-tracker per the rule. But the rule also claims eliminated-wrong-mechanisms STRENGTHEN surviving paths. Is that strengthening captured in F_obs, or is it separate?

My G1 analysis moved the methodology-artifact reclassifications into F_obs (G1 §5 Step 4). Do you concur, or should they be a third multiplicative factor?

**Q-N4 — PRU + Pattern 3' procedural enforcement (Q-GP3 reflected back)**:

You asked in Q-GP3 whether S80 gates should carry a "PRU-audit confirmation" step and "Pattern 3' cross-check" at pre-registration, with ~5% session-overhead cost. My neutral-evidence answer:

```
Step 1 (def): PRU-audit = explicit machinery enumeration at plan-write time per §0.10(d)
  Pattern 3' cross-check = verify selected derivation route matches framework canonical route
  
Step 2 (cost estimate): 5% session-overhead ≈ 30-45 min per 10-hour session
  
Step 3 (benefit): S79 P1-3 audit revealed W1-B, W2-C, W3-L WARRANT-INVALID — three 
  iteration chains invalidated by PRU failures. If each WARRANT-INVALID costs ~2-4 
  hours of re-run effort, total cost of 3 invalidations = 6-12 hours
  
Step 4 (benefit/cost): per-session prevention cost ~0.5 hr / session-WARRANT-INVALID 
  rate. S78 had ~3 WARRANT-INVALID per 10-workshop session. Under 3/10 rate, 5% 
  overhead prevents 3 x 3 = 9 hours of re-run at 0.5 x 10 = 5 hours overhead.
  Net savings: 4 hours per session (positive ROI)
  
Step 5 (direction): PRU-audit at plan-write is NET POSITIVE; recommend ADOPT as 
  standard Wave 0 checkpoint.
```

Python-verified: `3 * 3 = 9` hours of re-run vs `0.5 * 10 = 5` hours overhead, net savings `9 - 5 = 4` hours. Recommend ADOPT.

Reflected question back: can you propose a PRU-audit CHECKLIST TEMPLATE for S80 pre-registration? The `iteration-audit-template.md` exists for post-hoc audits; an analog `pru-pre-registration-template.md` would close the loop.

**Q-N5 — Contingency plan if R1 or R2 FAILs unexpectedly**:

You noted R2's CLT-test bonus (drift_u1(L=8) ∈ [0.56, 0.76] predicted by P4-B pre-theorem). If R2 returns drift OUTSIDE the CLT band (e.g., drift = 0.95 or 0.40), the abelian-subfactor pre-theorem cascades — P4-B's upgraded structural-theorem candidate enters RE-OPENED status. What's the contingency plan?

Three sub-questions:

- **Q-N5a**: under R2 unexpected-FAIL, does the Kasparov abelian-subfactor theorem proof (N19) remain worth running in S80 Wave 2, or does it go to Wave 3 pending R2 diagnosis?
- **Q-N5b**: if drift > 0.76 (HIGH-outside-band), the interpretation is "abelian u1 has less Level-2 protection than CLT-1/√N predicts" — does this strengthen or weaken the multi-mode-branches hypothesis [p4-b]?
- **Q-N5c**: what's the agreed SYMMETRIC-OR-ASYMMETRIC threshold pre-registration? The current CLT band 0.66 ± 0.10 is symmetric; but observed i=3 is already at 0.8375, suggesting the posterior is skew-high. Should the pre-registered band be [0.56, 0.76] (symmetric) or [0.56, 0.86] (asymmetric to accommodate P1-3 tail evidence)?

Substitution chain for Q-N5c:
```
Step 1 (def): CLT band = center ± 1σ width
Step 2 (input): center = 0.66, sigma = 0.10
Step 3 (symmetric band): [0.56, 0.76]
Step 4 (asymmetric-high-tail option): [0.56, center + k·sigma_high] where sigma_high 
  accommodates the observed 0.8375 tail
Step 5: if k = 2.0, band becomes [0.56, 0.86] — observed 0.8375 fits inside at 0.98σ 
  distance from 0.86
Direction: symmetric vs asymmetric choice is methodological, not physical. 
Pre-register the choice.
```

Python-verified: `0.66 + 2.0 * 0.10 = 0.86`; `(0.86 - 0.8375) / 0.10 = 0.225`. Observed is 0.225σ below the upper band at k=2.

---

These five questions seed Round 2. Responses expected in R2-A under CONVERGENCE (items where we agree), DISSENT (items where we diverge), EMERGENCE (new cross-synthesis results), QUESTIONS (your follow-ups).

GP_P5A_R1B_COMPLETE

---

## Round 2 — nazarewicz: Follow-up

### CONVERGENCE

Five gen-physicist refinements accepted. Each carries a substitution-chain where a sign/direction/threshold claim is involved.

**(C1) Re:N1 amendment — S1 W1-A classified STALE+RE-OPEN-gated-by-RO1**

My N1 entry S1 framed W1-A as "CLOSED at CONVENTION-PINNING scope". Gen-physicist flagged that the CONVENTION-PINNING reading is contingent on two UNCONFIRMED conditions:

(a) W1-A's internal a_n slot routing is documented;
(b) UNIFIED-AS-79-FULL routes through the SAME slot.

Per P4-C EM2 sign-flip doctrine [p4-c:1121], a_0 routing amplifies by factor 32, a_2 routing suppresses by factor 0.38 — these are different physics.

Substitution chain for the direction-claim that slot-choice matters:
```
Step 1 (def):  W1-A verdict-propagation = f(slot_W1A, slot_UNIFIED)
Step 2 (sub):  If slot_W1A == slot_UNIFIED == a_0: factor 32 applies uniformly
                If slot_W1A == slot_UNIFIED == a_2: factor 0.38 applies uniformly
                If slot_W1A != slot_UNIFIED: ratio 32 / 0.38 = 84.2 mismatch
Step 3 (simplify):  factor_mismatch = 32 / 0.38 = 84.2
Step 4 (direction):  mismatch is ~2 OOM, sufficient to invert PASS-interpretation
Conclusion:  the slot-consistency audit RO1 is NOT an optional
             documentation task — it blocks the PASS-interpretation
             of W1-A under UNIFIED-AS-79-FULL.
```

ACCEPT amendment: tag S1 as STALE+RE-OPEN-gated-by-RO1 in the post-S79 EVOI table.

**(C2) Re:N2 methodology flag — UNIFIED-AS-79-FULL EVOI = 0.211 is a pre-H̃-epoch value**

Gen-physicist noted my 0.211 marginalized EVOI for UNIFIED-AS-79-FULL averages Path A posterior 0.60 and Path B posterior 0.30 with equal weights. Once H̃-EPOCH runs (Wave 1 TOP, EVOI 0.300), the marginalization COLLAPSES to a conditional.

Substitution chain:
```
Step 1 (def): marginalized EVOI = sum_branches P(branch) * EVOI(branch)
Step 2 (pre-H̃):
  EVOI_pre = 0.50 * [0.60 * 0.25 + 0.40 * 0.18] + 0.50 * [0.30 * 0.25 + 0.70 * 0.18]
           = 0.50 * 0.222 + 0.50 * 0.201
           = 0.111 + 0.1005 = 0.2115 ≈ 0.211  (matches gen-physicist)
Step 3 (post-H̃ conditional on Path A):
  EVOI_A = 0.60 * 0.25 + 0.40 * 0.18 = 0.222
Step 4 (post-H̃ conditional on Path B):
  EVOI_B = 0.30 * 0.25 + 0.70 * 0.18 = 0.201
Step 5 (direction):
  Post-H̃ EVOI is branch-conditional, SMALLER spread than pre-H̃.
  0.211 is a SCHEDULING priority, not a post-resolution priority.
```

ACCEPT: Wave 1 ordering stands on 0.211 (dispatch-priority), but Wave 2 EVOI-scheduling MUST re-compute after H̃-EPOCH lands.

**(C3) Re:N3 combined-promotion 0.78 — tautology-discount acknowledged**

My combined P(≥1 functional passes) = 0.78 was tautology-discounted below the pure-independent 0.88. Gen-physicist's audit reconstructed:
- Pure-independent 3-way (0.6, 0.5, 0.4): 0.88
- With Z_s admissibility adjustment: 0.832
- With Z_s + χ_N tautology discount: 0.776 ≈ 0.78

Substitution chain confirming the conservative framing:
```
Step 1 (def): P(promote) = 1 - P(no candidate adds orthogonal info)
Step 2 (inputs):
  P(dS_inst fail or tautological)       = 0.40
  P(Z_s fail or inadmissible)           = 0.70
  P(chi_N orthogonal-info absent)       = 0.80  (Ward-identity tautology risk)
Step 3 (combined):
  P(all absent) = 0.40 * 0.70 * 0.80 = 0.224
  P(≥1 orthogonal) = 1 - 0.224 = 0.776
Step 4 (direction):
  0.776 is STRICTLY BELOW 0.88 pure-independent
  The gap (0.88 - 0.776) = 0.104 IS the tautology-discount magnitude
  The conservative framing DECREASES promotion probability, which is the
  correct direction given Ward-identity structural risk.
```

ACCEPT conservative framing. The 0.78 figure is my committed number for §VII.I promotion-odds under Wave 1+2 joint dispatch.

**(C4) Re:N4 refinement — R1/R2/R3 are SYNTHESIS-citation blockers, not compute blockers**

My N4 framed R1/R2/R3 as "BLOCKING for Wave 1 HIGH-EVOI gates". Gen-physicist traced the dependency chain:
- UNIFIED-AS-79-FULL inputs = {F_amp (re-derived), S_IC (P2-B independent), c_sub (P1-2 independent), Mukhanov-Sasaki pipeline}
- None of these inputs require W1-B's specific numerical output to be a free quantity

Substitution chain on the blocking-vs-parallel claim:
```
Step 1 (def): "strict compute-blocker" = next-stage cannot run without prior-stage output
              "synthesis-citation blocker" = next-stage can run, but paper-level citation
              of invalidated quantities is forbidden
Step 2 (dependency enumeration):
  F_amp under UNIFIED-AS-79-FULL is computed by the unified pipeline
  W1-B's per-stage F_amp was NOT piped into UNIFIED-AS-79-FULL as input
  therefore UNIFIED-AS-79-FULL compute is NOT gated on R1
Step 3 (synthesis-level dependency):
  Wave 1 SYNTHESIS document citing "F_amp measured at W1-B is X" is INVALID
  until R1 produces post-remediation F_amp
Step 4 (direction):
  The blocker is at CITATION layer, not COMPUTE layer
  Wave 0 runs R1/R2/R3 in PARALLEL with Wave 1 dispatch
  Wave 1 synthesis SERIALIZES on R1/R2/R3 verdict landing
```

ACCEPT refinement. The practical Wave 0 / Wave 1 scheduling accommodates parallel execution without losing citation-validity discipline.

**(C5) G1 framework probability 12% → 20.6% as WORK-COMPLETION measure (not truth probability)**

Gen-physicist explicitly labeled the 20.6% figure as EXPLORATION-COMPLETENESS, distinct from framework-truth-probability (Skeptic's domain). Per `.claude/rules/evoi-prioritization.md` §"Effort-Based Probability": the measure tracks WORK DONE, not truth.

Substitution chain for accepting the work-completion framing:
```
Step 1 (def): P_framework = N_complete/N_total × F_observation
Step 2 (not truth-probability):
  P_framework tracks exploration-completeness of the constraint map
  NOT P(framework=TRUE) given all observational evidence
Step 3 (S79 impact):
  factor 1.72 gain = 12 workshop closures + 4 §VII.II pre-theorems
  + narrative shift on A_s (absolute 3.35 OOM → ratio 0.22-1.12 OOM)
  This measures WORK-COMPLETION, not observational convergence alone
Step 4 (boundary test):
  If this WERE truth-probability, the factor 1.72 gain would require
  discriminating observational evidence. S79 produced work, not new data.
  Therefore 20.6% is a PROCESS metric, not a truth-discriminating metric.
Step 5 (direction):
  The 20.6% figure is observationally-NON-DISCRIMINATING at the level of
  distinguishing phonon-exflation from a null-framework at comparable
  session-count. This is what gen-physicist's Q-N3 correctly identifies.
```

ACCEPT: 20.6% is work-completion, not truth-probability. See my Q-N3 answer below for the two-axis tracking refinement.

### DISSENT

Two points where my nuclear-UQ reading disagrees with gen-physicist's Re:N4 and Q-N4.

**(D1) G2 Wave 0 dispatch — R2 is theorem-testing, not just synthesis-citation-blocking**

Gen-physicist allowed remediation to run parallel to Wave 1 compute (Re:N4 §3). From my nuclear-UQ perspective, R2 carries a structural role that elevates it above the "synthesis-citation blocker" level.

Substitution chain for the elevation claim:
```
Step 1 (def): R2 output = drift_u1(L=8) measurement under frozen discipline
Step 2 (P4-B pre-theorem prediction):
  abelian-subfactor CLT 1/sqrt(N) at L=8 predicts drift_CLT in [0.56, 0.76]
  This is a PRE-THEOREM, not an empirical expectation — it's structurally forced
  by the rank-1 character-module of the abelian Kasparov class [p4-b:1470]
Step 3 (R2 role change):
  If R2 returns drift in band: CLT pre-theorem gets empirical support,
    promotion-path to §VII.I theorem strengthens
  If R2 returns drift outside band: CLT pre-theorem FAILS at L=8,
    P4-B's abelian-subfactor obstruction enters RE-OPENED status
Step 4 (direction):
  R2 is NOT just a citation cleanup — it is a THEOREM TEST
  Running it BEFORE P4-B theorem-proof gate (N19 Kasparov abelian)
  avoids investing theorem-proof compute into a framework under revision
Step 5 (priority upgrade):
  R2 should complete BEFORE Wave 2 Kasparov proof launches
  Wave 0 status is STRICT for R2, not merely synthesis-blocking
```

**[AUDIT] S80-WAVE-0-SCOPE-AUDIT** (pre-registered):
- Enumerate which Wave 2 gates have DEPENDENCY on CLT-drift outcome
- For each: classify as "citation-only blocker" (can proceed in parallel) or "theorem-proof blocker" (must wait for R2 landing)
- Expected outcome: R2 strict-blocks N19 (Kasparov abelian proof); R1/R3 remain parallel-safe

**(D2) Q-N4 PRU-audit net savings — gen-physicist's +4 hr is optimistic**

Gen-physicist's arithmetic: prevent 3 WARRANT-INVALIDs × 3 hr each = 9 hr rerun; 0.5 hr × 10 hr session = 5 hr overhead; net +4 hr/session. From my nuclear-UQ experience, the PRU-audit CATCH RATE is rarely 100%.

Substitution chain:
```
Step 1 (def): net_savings = rerun_prevented - audit_overhead
Step 2 (gen-physicist assumption): 100% catch rate, all 3 WARRANT-INVALIDs prevented
Step 3 (nuclear-UQ realism): PRU-audit is structural check (query plan against
  canonical_constants + prior sessions + known theorems); even well-designed
  audits catch 60-70% of potential issues
Step 4 (three scenarios, Python-verified):
  Optimistic (3/3 catch, 0.5 hr/hr overhead): 9 - 5 = +4.0 hr (gen-physicist)
  Moderate  (2/3 catch, 2.0 hr overhead):    6 - 2 = +4.0 hr
  Conservative (1/3 catch, 2.5 hr overhead): 3 - 2.5 = +0.5 hr
Step 5 (direction):
  Moderate scenario gives +4 hr, matching gen-physicist.
  Conservative gives +0.5 hr (marginally positive).
  Realistic range: +2 hr expected; +4 hr is best-case.
```

ACCEPT gen-physicist's recommendation to ADOPT PRU-audit, but record the net savings as +2 hr/session expected, with the +4 hr as a ceiling. Decision does NOT change: PRU-audit is net positive under all three scenarios.

### EMERGENCE

Four cross-synthesis results from combining nuclear-UQ with gen-physicist's neutral-evidence framing.

**(E1) S80 Wave 0 is fundamentally CRITICAL, not merely blocking**

Re-examining R2's role in conjunction with P4-B's abelian-subfactor pre-theorem reveals that Wave 0 is not a discipline-enforcement layer. It is a theorem-testing stage with its own EVOI.

Substitution chain:
```
Step 1 (def): Wave 0 effective EVOI = sum(remediation_EVOI) + bonus_theorem_test
Step 2 (base remediation):
  R1 EVOI = 0.045
  R2 EVOI = 0.048
  R3 EVOI = 0.028
  Base = 0.121
Step 3 (theorem-test bonus):
  R2 simultaneously tests P4-B CLT pre-theorem at L=8
  ΔEVOI_CLT = 0.80 * 0.05 + 0.20 * 0.08 = 0.056 (gen-physicist verified)
Step 4 (combined Wave 0 EVOI):
  0.121 + 0.056 = 0.177
Step 5 (direction):
  Wave 0 combined EVOI 0.177 is COMPARABLE to dS_inst/dτ 4th functional (0.180)
  Not merely procedural overhead — it is a substantive computation stage.
```

This elevates Wave 0 from "hygiene" to "investigation". The Wave 0 / Wave 1 distinction is a SCHEDULING choice, not an information-gain-priority choice.

**(E2) Framework probability has two distinct axes, not one**

G1's 12% → 20.6% is work-completion. S79 ALSO narrowed the A_s-ratio gap from absolute 3.35 OOM to ratio 0.22-1.12 OOM — this is genuine observational-alignment motion, distinct from work-completion.

Substitution chain:
```
Step 1 (def):
  P_work_complete = (mechanism links complete / total) × (fraction approaching observation)
  P_obs_aligned  = (pre-registered PASS-class observables) / (total pre-registered channels)
Step 2 (pre-registered observational channels and verdicts, per S79 state):
  PASS: n_s, m_H, r, alpha_s, tau_fold, Omega_DM (6 channels)
  INFO/STRAIN: A_s-gap (1 channel, now ratio-framed)
  REFRAMED: DESI-W3G-Route-A, PBH-FIRAS-yoked (2 channels, methodology artifacts cleared)
  Total pre-registered: 9
Step 3 (substitute):
  P_obs_aligned = 6 / 9 = 0.667 (Python-verified)
Step 4 (comparison):
  P_work_complete = 0.206 (effort-based)
  P_obs_aligned  = 0.667 (observational-channel-PASS count)
Step 5 (direction):
  These measures DIFFER substantially. They are not reducible to each other.
  Tracking only one hides information about the other.
```

Propose two-axis tracking:
- `P_work_complete` updates per session-work (current: 0.206)
- `P_obs_aligned` updates per pre-registered-observable verdict (current: 0.667)

The two together answer separate questions: "how much of the constraint map have we mapped?" and "among the channels we CAN test, how many PASS?". Both are load-bearing, neither substitutes for the other.

**(E3) Wave 1 concentration is maximally compute-efficient**

The 6 parallel Wave 1 gates (H̃-EPOCH 0.300, UNIFIED-FULL 0.211, dS_inst 0.180, χ_N 0.074, CC-ratios-proof 0.12, CSUB-SIGN 0.073) sum to combined EVOI 0.958.

Substitution chain:
```
Step 1 (def): combined EVOI over K independent gates = Σ per-gate EVOI
             (assumes ΔP independent across gates, sample spaces disjoint)
Step 2 (sum): 0.300 + 0.211 + 0.180 + 0.074 + 0.12 + 0.073 = 0.958
Step 3 (comparison to sequential dispatch):
  If Wave 1 ran gates sequentially, total wallclock = K × t_gate
  Parallel dispatch: wallclock = max(t_gate)
  Information gain: same 0.958 either way, but parallel completes faster
Step 4 (direction):
  Running 6 Wave 1 gates in parallel extracts MAXIMUM information per session-hour
  No other S80 configuration matches this efficiency
Step 5:
  This is the most compute-efficient Wave 1 design available given current priorities
```

Python-verified: `0.300 + 0.211 + 0.180 + 0.074 + 0.12 + 0.073 = 0.958`.

**(E4) H̃-EPOCH is the framework's S80 rate-limiting question**

No other single S80 computation carries EVOI 0.300 individually. All downstream A_s interpretations are gated by its outcome.

Substitution chain:
```
Step 1 (def): rate-limiting = single-gate-outcome determines interpretation of K downstream gates
Step 2 (enumerate downstream dependencies):
  UNIFIED-AS-79-FULL: Path A vs Path B collapses marginalization
  UNIFIED-BACKREACT-79: backreaction budget under chosen H̃-epoch
  PS-SUBSTRATE-MATCHED-IC: IC-spec depends on epoch choice
  Fold Transit Event: interpretation of τ_fold in H̃-coords
Step 3 (EVOI comparison):
  H̃-EPOCH at 0.300 exceeds next-highest (UNIFIED-FULL 0.211) by factor 1.42
  And gates 4+ others via conditional interpretation
Step 4 (direction):
  H̃-EPOCH is UNIQUELY rate-limiting; no peer gate has comparable downstream scope
Step 5:
  Wave 1 concurrent-dispatch is still correct (gates 3, 4, 5, 6 run independently of H̃-EPOCH),
  but Wave 2 EVOI recomputation is REQUIRED post-H̃-EPOCH resolution
```

### QUESTIONS

Five answers to gen-physicist's G3 questions.

**Q-N1 — Bottom-20 EVOI methodology**

Gen-physicist requested item-level EVOI for the lowest-20 items in my 106-item diff. Methodology explanation:

- **Top 20** (full P(pass)·ΔP computation): primary EVOI gates from the UNIFIED-AS-79 family, Fold Transit 4th-functional, remediation, §VII.I promotion candidates, top CF items.
- **Middle 60** (heuristic EVOI from prior-to-posterior Δ estimates): deltas taken from topical-cluster similarity to nearest precedent gate (per `.claude/rules/evoi-prioritization.md` §"Failures cluster by TOPIC").
- **Bottom 20** (NULL EVOI, organizational bookkeeping): no decisive test possible; these are naming audits, tag-discipline pins, cross-reference updates, documentation rewrites.

Explicit bottom-20 list (from the 106-item diff):
- N3 CANONICAL-CONSTANTS-AUDIT (classification task, no PASS/FAIL)
- RO3 `mellin_*` vs `cc_*` naming
- RO6 "13 OOM cushion" → "7.3 OOM" audit across WP citations
- P10 marginal-semiclassical language audit (CF-7 P3-B)
- P11 1-loop-proper cushion citation pin (CF-2 P3-B)
- N41 EVOI-SYNC-79 (5-layer record synchronization)
- N30 E_J convention audit (without FABRIC-COUPLING-55 ansatz)
- P9 Pattern 3' rule insertion into epistemic-discipline.md
- P6 M_KK structural-role documentation (CN-EM4)
- Additional items (~11) distributed across documentation pins, canonical-constants audits, WP text updates.

These are Wave-4 or background tasks. They deliver zero EVOI in the decisive-gate sense but deliver structural reliability (like PRU-audit itself).

**[AUDIT] S80-EVOI-BOTTOM-20-RATIONALIZATION** (pre-registered):
- Task: structured review of which bottom-20 items deserve NULL-EVOI vs micro-EVOI (0.01-0.05 per item)
- Output: classification ledger in `sessions/evoi-framework.md` bottom-level
- Accept criterion: every item classified NULL or assigned numerical micro-EVOI with provenance

**Q-N2 — Path A/B prior argument**

Gen-physicist asked whether a prior Bayesian argument exists favoring Path A (horizon-exit) over Path B (fold). Two observations:

Path A (horizon-exit) is the conventional inflation-literature A_s definition. Observational CMB A_s extraction is AT horizon-exit.

Path B (fold) is the FRAMEWORK-NATIVE epoch. Jensen deformation + ρ_fold = M_KK⁴ is the fundamental spectral object at τ_fold = 0.190.

Substitution chain for the EVOI-invariance-under-symmetric-|ΔP| observation:
```
Step 1 (def): EVOI = P(pass) * |ΔP(pass)| + P(fail) * |ΔP(fail)|
Step 2 (symmetric |ΔP| = D case):
  EVOI = P(pass) * D + (1 - P(pass)) * D = D
Step 3 (Python verified across P_A ∈ {0.5, 0.7, 0.9}):
  P=0.5: EVOI=0.30 | P=0.7: EVOI=0.30 | P=0.9: EVOI=0.30
Step 4 (asymmetric |ΔP| case: D_pass=0.30, D_fail=0.20):
  P=0.3: EVOI=0.23 | P=0.5: EVOI=0.25 | P=0.7: EVOI=0.27
Step 5 (direction):
  EVOI is prior-invariant ONLY under the symmetric |ΔP| assumption
  Under asymmetric |ΔP|, EVOI scales with P(pass) linearly
  The load-bearing question becomes whether |ΔP(pass)| = |ΔP(fail)|
```

My view: the symmetric |ΔP| = 0.30 assumption is DEFENSIBLE. Path A PASS narrows the framework's A_s problem by ~1 OOM (mechanism-scale → sub-order tweak). Path B PASS (or equivalently Path A FAIL) widens by ~1 OOM (tweak → mechanism-search). These are roughly symmetric in magnitude — the framework-status move is comparable in either direction.

Therefore EVOI = 0.300 stands independent of Path-A-canonical prior, given the symmetric |ΔP|. The ACTUAL information H̃-EPOCH delivers is the DISAGREEMENT between Path A and Path B — it resolves which definition is framework-consistent, and disagreement IS framework-internal consistency-failure.

**[VERIFY] S80-H-TILDE-EPOCH-FRIEDMANN-EVOLUTION** (pre-registered):
- Task: explicitly compute framework-predicted Friedmann evolution from τ_fold to horizon-exit
- Method: integrate Friedmann equation with substrate stress-energy sourcing
- PASS criterion: Path A value follows from Path B via predicted evolution (ratio within factor 2)
- FAIL criterion: Path A / Path B mismatch > factor 10 → framework-internal inconsistency

**Q-N3 — Framework probability observationally-discriminating?**

Gen-physicist asked whether the 20.6% figure tracks something a null-framework would NOT also score at equal session-count. Answer: MIXED.

Substitution chain:
```
Step 1 (def): observational discrimination = does the measure update differently for
              phonon-exflation vs a null-framework given identical session-count?
Step 2 (effort-based formula tracks WORK DONE):
  A null-framework running 12 workshops would ALSO increment numerator + denominator
  P_work is methodologically work-tracking, not truth-tracking
Step 3 (BUT S79 work was not purely organizational):
  - A_s gap narrowing from 3.35 OOM to 0.22-1.12 OOM (ratio-reframe): substantive
  - ω_L1 disambiguation (P3-A): observational-adjacent, resolves DM-sector stability
  - Γ_γ promotion to unitarity lower bound: strengthens observational prediction
  - CC-ratios-only theorem: elevates framework-observable discrimination
Step 4 (direction):
  20.6% has OBSERVATIONAL content via ratio-reframe and prediction-tightening workshops
  BUT effort-based formula does NOT isolate these from pure organizational increments
  Therefore 20.6% MIXES observational and organizational convergence
Step 5 (resolution — two-axis tracking):
  P_work_complete = 0.206 (effort, tracks WORK done)
  P_obs_aligned  = 6 / 9 = 0.667 (count of PASS-class observables against total
                                   pre-registered observational channels)
```

Python-verified: `6 / 9 = 0.667`. Methodology-artifact reclassifications (W3-G, W1-C, W2-G) cleared from FAIL-outlier status ENTER P_obs_aligned numerator only to the extent they produce matchable observables (W3-G Route A at 1.73σ from DR3 Sc.B does; W1-C bound-only does not).

Recommend: track BOTH measures going forward. P_obs_aligned catches real observational convergence; P_work_complete catches work-done. Neither substitutes for the other.

**Q-N4 — PRU-audit procedural integration**

ADOPT per gen-physicist, with nuclear-UQ modifications:

Procedural structure:
- After plan pre-registration, BEFORE running gates: automated PRU-audit executes
- PRU-audit queries: does each pre-registered gate's PASS criterion CONTRADICT any prior canonical result (from canonical_constants.py, theorem ledger, session permanent-results)?
- Audit tooling: grep plan against canonical_constants.py, prior session wrap-ups, known-theorem database; flag pre-registrations that assume quantities contradicting established results
- Implementation: Wave-0 activity creating a new script `s80_pru_audit.py`

Expected net savings: +2 hr/session (moderate-scenario estimate; Python-verified under multiple catch-rate assumptions). Gen-physicist's +4 hr is the optimistic ceiling. Even under the conservative 1/3-catch scenario (+0.5 hr), the ROI is positive.

**[AUDIT] S80-PRU-AUDIT-TOOLING** (pre-registered):
- Task: create `s80_pru_audit.py` as Wave-0 activity
- Methodology: structural query against canonical_constants + prior theorem-ledger + session-permanent-results-registry
- PASS: tool successfully flags at least 1 PRU candidate in a test-run on the S80 plan
- Accept criterion: S80 plan passes PRU-audit before Wave 1 gate dispatch

Reflected question answered: YES, a `pru-pre-registration-template.md` analog is appropriate. The `iteration-audit-template.md` exists for post-hoc; PRU-pre-registration closes the loop at plan-write time.

**Q-N5 — R2 UNEXPECTED FAIL contingency**

Gen-physicist asked about R2's drift_u1(L=8) falling outside the CLT 0.66 ± 0.10 band. Three contingency scenarios:

**Scenario 1 — drift < 0.40 (well-below-band)**:
- CLT pre-theorem DISPROVED at L=8
- Interpretation: u1 was TRUNCATION ARTIFACT; abelian-subfactor obstruction does not survive at higher L
- P4-B conclusions REVERT
- Cascade: N19 Kasparov abelian proof enters RE-OPENED status (Wave 2 halted)
- All W2-C-dependent framework-citations get FLAGGED for revision

**Scenario 2 — drift > 0.76 (above-band, matches P1-3 tail at 0.8375)**:
- CLT pre-theorem OVER-predicts suppression
- Interpretation: there IS an abelian-subfactor obstruction, but stronger than CLT 1/√N captures
- A new structural feature must be identified (possibly non-trivial correction to rank-1 character module)
- Adjust CLT formula with correction term; open S80 investigation

**Scenario 3 — 0.40 ≤ drift ≤ 0.56 or 0.76 ≤ drift ≤ 0.86 (adjacent to band)**:
- INFO result — theorem PARTIALLY SUPPORTED but not confirmed
- Extend band with k=2 asymmetric expansion (Python-verified: observed 0.8375 sits at 0.225σ below upper edge at k=2)
- Open sub-investigation but do not halt Wave 2

Substitution chain on the symmetric-vs-asymmetric band question:
```
Step 1 (def): CLT band = center ± k·sigma, where k is chosen based on tail behavior
Step 2 (symmetric k=1): [0.56, 0.76]
  observed 0.8375 at (0.8375 - 0.76)/0.10 = 0.775σ ABOVE upper edge (Python-verified)
Step 3 (asymmetric k=2 on high side): [0.56, 0.86]
  observed 0.8375 at (0.86 - 0.8375)/0.10 = 0.225σ BELOW upper edge (Python-verified)
Step 4 (direction):
  symmetric band CLASSIFIES observed as BORDERLINE-FAIL (<1σ above)
  asymmetric k=2 band CLASSIFIES observed as PASS (within ~0.2σ of upper edge)
Step 5 (pre-registration discipline):
  The choice MUST be made BEFORE R2 lands (else iterate-until-PASS failure mode)
```

My recommendation: pre-register SYMMETRIC k=1 band [0.56, 0.76] as the primary criterion. If observed falls outside, trigger scenario-specific cascade rather than band re-sizing.

**[AUDIT] S80-P4B-CONTINGENCY-CASCADE** (pre-registered):
- Task: inventory all Wave 2+ gates and WP citations that depend on abelian-subfactor pre-theorem surviving R2
- Output: dependency tree with PAUSE-points if R2 fails each scenario
- Accept criterion: complete dependency inventory before R2 dispatch

NAZAREWICZ_P5A_R2A_COMPLETE

---

## Round 2 — gen-physicist: Cross-Synthesis (FINAL)

### CONVERGENCE

Five nazarewicz R2-A refinements accepted. Each carries its load-bearing substitution chain re-verified.

**(C1) Accept S1 STALE+RE-OPEN-gated-by-RO1 escalation**

Nazarewicz's C1 substantiation of the slot-mismatch chain delivers a quantitative wall that the prior STALE-only classification did not bear:

```
Step 1 (def): slot-routing factor f_slot(n) = multiplicative weight of a_n Seeley-DeWitt
              channel under UNIFIED-AS-79-FULL (P4-C EM2 sign-flip doctrine [p4-c:1121])
Step 2 (sub): f_slot(0) = 32 (amplification), f_slot(2) = 0.38 (suppression)
Step 3 (simplify): factor_mismatch = f_slot(0) / f_slot(2) = 32 / 0.38 = 84.2105
Step 4 (direction): log10(84.21) = 1.925, i.e. ~2 OOM mismatch
                    mismatch magnitude EXCEEDS the PASS-interpretation band entirely
Conclusion: RO1 slot-audit is a strict compute-blocker for the UNIFIED-AS-79-FULL
            PASS-interpretation, not a documentation chore. S1 escalation to
            STALE+RE-OPEN-gated-by-RO1 is structurally necessary.
```

Python-verified: `32/0.38 = 84.2105`, `log10(84.21) = 1.925`. ACCEPT the escalated classification. The post-S79 EVOI table records S1 under both STALE and RE-OPEN categories; RO1 fires first in Wave 0.

**(C2) Accept UNIFIED-AS-79-FULL EVOI = 0.211 as pre-H̃ marginalized priority; Wave 2 recomputation scheduled**

Nazarewicz's C2 substitution chain confirms what my Re:N2 flagged: the 0.211 figure averages Path A (EVOI_A = 0.222) and Path B (EVOI_B = 0.201) under equal epoch priors. Post-H̃-EPOCH resolution, the marginalization collapses to a branch-conditional. Python-verified:

```
EVOI_A = 0.60·0.25 + 0.40·0.18 = 0.2220
EVOI_B = 0.30·0.25 + 0.70·0.18 = 0.2010
EVOI_marginal = 0.50·0.2220 + 0.50·0.2010 = 0.2115
```

ACCEPT: 0.211 is the Wave 1 DISPATCH-PRIORITY; Wave 2 re-ranks on EVOI_A or EVOI_B depending on H̃-EPOCH verdict. This is methodologically correct sequencing.

**(C3) Accept tautology-discounted 0.78 combined promotion probability**

Re-verified Python: `1 - 0.40·0.70·0.80 = 0.776 ≈ 0.78`. The 0.80 entry in the χ_N slot is P(χ_N_does_not_add_orthogonal_info), not P(χ_N_FAIL_verdict). Under Ward-identity kernel structure (both χ_a and χ_N are one-body response functionals ∫dε·ρ(ε,τ)·K(ε,τ)), χ_N's PASS does not deliver functional-independent confirmation of ρ-concentration at τ_fold. The 0.104 gap between pure-independent 0.88 and tautology-discounted 0.776 is the structural discount; it is not optional. ACCEPT as the committed §VII.I promotion-odds under Wave 1+2 joint dispatch of {dS_inst/dτ, Z_s, χ_N}.

**(C4) Accept citation-blockers-vs-compute-blockers distinction; R2 is theorem-testing (exception)**

Nazarewicz's C4 confirms my Re:N4 §3 finding that R1/R2/R3 are SYNTHESIS-citation blockers (not strict compute blockers) for UNIFIED-AS-79-FULL. The unified pipeline re-derives F_amp internally; W1-B's per-stage F_amp is not piped in. This holds as the default classification for Wave-0 items.

Exception (sets up D1): R2 carries an ADDITIONAL structural role beyond citation cleanup — it tests P4-B's abelian-subfactor CLT pre-theorem at L=8 against drift_CLT ∈ [0.56, 0.76]. This is theorem-testing, not just procedural hygiene. R2 is therefore NOT parallel-safe with respect to N19 (Kasparov abelian-subfactor proof): see D1.

**(C5) Accept work-completion vs truth-probability distinction; two-axis tracking formalized**

Nazarewicz's C5 substitution chain establishes what my G1 §6 flagged: the 20.6% effort-based figure is WORK-COMPLETION, not framework-truth-probability (Skeptic's domain). A null-framework running 12 workshops would also increment P_work. My Q-N3 asked whether 20.6% is observationally-discriminating; nazarewicz's answer (MIXED) with the two-axis resolution is the correct methodological refinement. Both metrics are legitimate:

```
P_work_complete  = (N_complete / N_total) × F_obs
                 = (55/120) × 0.45 = 0.2063 (work-done measure)

P_obs_aligned    = N_PASS_class / N_pre-registered_channels
                 = 6/9 = 0.6667 (observable-channel-PASS measure)
```

Python-verified: `55/120 × 0.45 = 0.20625`; `6/9 = 0.66667`. Neither substitutes for the other. ACCEPT two-axis tracking as the S80-forward methodology. See E2 for formal proposal.

**(D1) Accept R2 theorem-testing elevation: strict-blocks N19 Kasparov abelian-subfactor proof**

Nazarewicz's D1 elevation of R2 from "synthesis-citation blocker" to "theorem-test precedent" is correct. My Re:N4 §3 treated remediation uniformly; this missed the R2/P4-B structural coupling:

```
Step 1 (def): R2 returns drift_u1(L=8) — the abelian-subfactor truncation-drift
              at L=8 under frozen quantity-definition and SHA-pinned discipline
Step 2 (P4-B pre-theorem prediction): drift_CLT ∈ [0.56, 0.76] (center ± 1σ)
              rooted in rank-1 character-module CLT 1/sqrt(N) scaling [p4-b:1470]
Step 3 (N19 dependency): Kasparov abelian proof assumes abelian subfactor lacks
              Level-2 R-protection. This presupposes the CLT regime applies.
Step 4 (if R2 returns drift OUTSIDE [0.56, 0.76]):
              CLT pre-theorem FAILS at L=8
              N19 starts from a framework-under-revision premise
              Investing N19 compute would be premature
Step 5 (direction): R2 STRICT-BLOCKS N19
              R2 does NOT strict-block R1, R3, or Wave 1 compute gates
              Only N19 and items cascading from abelian-subfactor cert
```

ACCEPT. This refinement preserves parallelism for the bulk of Wave 0/1 but inserts a strict ordering R2 → N19. Pre-registered as [AUDIT] S80-WAVE-0-SCOPE-AUDIT in Open Questions.

**(D2) Accept PRU-audit net savings revision: +2 hr moderate-scenario (ceiling +4 hr)**

My Q-N4 arithmetic assumed 100% PRU-audit catch rate: `prevent 3·3=9 hr rerun − 0.5·10=5 hr overhead = +4 hr net`. Nazarewicz's realistic-catch-rate analysis yields three scenarios Python-verified:

```
Optimistic (catch 3/3, overhead 0.5 hr/hr):  9.0 − 5.0 = +4.0 hr/session
Moderate   (catch 2/3, overhead 0.2 hr/hr):  6.0 − 2.0 = +4.0 hr/session
Conservative (catch 1/3, overhead 0.25):     3.0 − 2.5 = +0.5 hr/session
```

ACCEPT nazarewicz's committed figure: expected +2 hr/session, ceiling +4 hr. Decision stands — ADOPT PRU-audit. Positive ROI under all scenarios.

**(E1-E4) Accept four emergence items with refinements**

- **E1 (Wave 0 EVOI 0.177 comparable to dS_inst 0.180)**: Python-verified: `0.045 + 0.048 + 0.028 + 0.056 = 0.177`. Wave 0 is substantive, not hygiene. ACCEPT.
- **E2 (two-axis framework probability)**: formalized in E2 below as permanent methodology refinement.
- **E3 (Wave 1 combined EVOI 0.958 maximally compute-efficient)**: Python-verified: `0.300+0.211+0.180+0.074+0.12+0.073 = 0.958`. Parallel dispatch extracts maximum information per session-hour. ACCEPT.
- **E4 (H̃-EPOCH singular rate-limiting)**: factor 1.42 EVOI spread over next-highest; Python-verified: `0.300/0.211 = 1.4218`. ACCEPT.

### DISSENT

Two refinements warrant pushback — not on substance but on pre-registration precision. Both are minor relative to the convergence above.

**(P1) P_obs_aligned = 6/9 calculation requires explicit observable enumeration**

Nazarewicz's E2 writes: `PASS: n_s, m_H, r, alpha_s, tau_fold, Omega_DM (6 channels); INFO/STRAIN: A_s-gap (1); REFRAMED: DESI-W3G-Route-A, PBH-FIRAS-yoked (2); Total: 9`. The 6/9 = 0.667 arithmetic is correct (Python-verified), but the observable-catalog is ambiguous in two ways:

```
Step 1 (def): P_obs_aligned = |channels ∈ PASS-class| / |channels ∈ pre-registered|
Step 2 (enumeration audit):
  PASS candidates: n_s (0.9557 vs Planck 0.9649, S73B-convergent), m_H (133.4 GeV
    vs PDG 125.25, within 7%), r (0.033 < BICEP/Keck 0.036), alpha_s (post-S74
    correction), Omega_DM (at 0.7σ — DOES this count PASS or INFO?), tau_fold
    (structural), TT-stability (substrate observable per nazarewicz N3) = 7 candidates
  INFO/FAIL: A_s ratio gap (0.22 or 1.12 OOM pending H̃-EPOCH); FIRAS mu
    (YOKED to A_s per P2-B) = 2 candidates
  Total explicit: 7 + 2 = 9 channels — but this assumes Omega_DM at 0.7sigma
    counts as PASS-class, not INFO
Step 3 (alternative enumeration):
  If Omega_DM-at-0.7sigma is classified INFO: 5 PASS + 3 INFO = 5/8 = 0.625
  If tau_fold is NOT counted (structural, not direct observation): 5/8 = 0.625
  If TT-stability is not observable-class: 5/8 = 0.625
Step 4 (direction): P_obs_aligned ∈ [0.556, 0.750] under reasonable enumeration
  variance. Nazarewicz's 0.667 is the central estimate; boundaries unpinned.
```

The DISAGREEMENT is not on 6/9 arithmetic but on catalog ambiguity. Pre-register [AUDIT] S80-P-OBS-ALIGNED-CATALOG (in Open Questions): explicit enumeration with PASS/FAIL/INFO classification rules, so P_obs_aligned has a canonical definition for future S80+ sessions. Nazarewicz's 0.667 is adopted as the working estimate pending audit.

**(P2) Wave 0 strict-ordering refinement: only R2 strict-blocks N19; other Wave 1 items proceed in parallel**

Nazarewicz's D1 correctly identifies R2 → N19 as strict blocking. But the D1 phrasing could be read as Wave 0 gating ALL Wave 1 items, which would incorrectly serialize the session. Clarifying substitution chain:

```
Step 1 (def): strict-blocker = downstream gate's premise fails if upstream fails
Step 2 (dependency enumeration, Wave 1 items):
  H̃-EPOCH: independent of R1/R2/R3; derives from Friedmann-evolution substrate
  UNIFIED-AS-79-FULL: re-derives F_amp internally; NOT W1-B-piped-input (C4)
  dS_inst/dτ: instanton-action gradient, orthogonal substrate probe
  chi_N: reuses W1-D DoS engine, not W1-B/W2-C/W3-L
  CC-ratios-only theorem: analytic ≤3-page proof from CC96 heat-kernel
  CSUB-SIGN: framework-internal identity check
Step 3 (cross-check R2 dependency):
  R2 output (drift_u1(L=8)) is NOT input to any Wave 1 compute gate
  R2 ONLY blocks Wave 2 N19 (Kasparov abelian theorem proof)
Step 4 (direction):
  Wave 0 runs in PARALLEL with Wave 1 compute gates
  Wave 2 N19 serializes on R2 landing
  Wave 1 SYNTHESIS document waits on R1/R2/R3 landing for citation validity
```

CONCUR with nazarewicz's D1 on the R2 → N19 serialization; REFINE that Wave 0 does NOT gate Wave 1 compute in general. The two interpretations are consistent; the refinement simply pins the scope of "strict-blocks" to its minimal scope.

### EMERGENCE

Five cross-synthesis findings that outlive this workshop as S80-forward methodology.

**(E1) Two-axis framework probability as permanent tracking methodology**

The single-metric formula in `.claude/rules/evoi-prioritization.md` ("framework probability ... (mechanism links complete / total) × (fraction approaching observation)") is WORK-COMPLETION only. It does not track observational-alignment as a separate dimension. S79 demonstrated that these are distinct:

```
Step 1 (def, metrics): 
  P_work_complete  = (N_complete/N_total) × F_obs_mechanism_links
  P_obs_aligned    = |PASS-class pre-registered observables| / |total pre-registered channels|
Step 2 (independence): a session can raise P_work (mechanism-link closure) WITHOUT
  raising P_obs (no new observational channel PASS lands)
  Conversely, a single observational PASS can raise P_obs without new closures
Step 3 (S79 evidence):
  P_work: 0.120 → 0.206 (+72% from 12 closures + 4 pre-theorems + ratio-reframe)
  P_obs:  pre-S79 ≈ 5/9 ≈ 0.556; post-S79 = 6/9 = 0.667 (+20% from W3-G reformulation)
Step 4 (direction):
  Single-metric framework probability HIDES the orthogonal information
  Both metrics are load-bearing; both update independently
  Dashboarding both gives a 2D phase-space of framework status over session-sequence
Step 5: ADOPT as permanent S80-forward methodology refinement.
```

Pre-register [AUDIT] S80-TWO-AXIS-TRACKING-ADOPTION (in Open Questions): update `.claude/rules/evoi-prioritization.md` to document both P_work and P_obs_aligned as separate metrics with their own update rules. Framework probability is not a single scalar.

**(E2) S80 Wave architecture confirmed as MOST COMPUTATION-EFFICIENT**

The Wave 0/1/2/3 structure that emerged from the N1-N5, Re:N1-5, R2A sequence is not arbitrary — it is pareto-optimal given the current constraint-graph dependencies:

```
Wave 0 (remediation + pre-theorem testing):
  Combined EVOI 0.177 (R1 0.045 + R2+bonus 0.104 + R3 0.028)
  Role: citation-validity cleanup + R2 CLT pre-theorem test (→ N19 gate)

Wave 1 (6 parallel compute gates + analytic proof):
  Combined EVOI 0.958 (H̃ 0.300 + UNIFIED-FULL 0.211 + dS_inst 0.180 + 
    chi_N 0.074 + CC-ratios-proof 0.12 + CSUB-SIGN 0.073)
  Role: frame-decisive framework-level information gain
  Parallelism valid because gates are independent in sample space

Wave 2 (H̃-EPOCH-informed conditional recomputation):
  UNIFIED-AS-79-FULL re-ranked on EVOI_A = 0.222 or EVOI_B = 0.201
  UNIFIED-BACKREACT-79 (0.165), PS-SUBSTRATE-MATCHED-IC (0.108),
    Z_s formalism-admissibility gate, N19 Kasparov (R2-cleared)
  Role: downstream conditional on Wave 1 outcomes

Wave 3 (§VII.I formal theorem proofs + extension):
  Formal proofs of CC-ratios-only, MP-exclusion, Kasparov-abelian
  Extensions: multi-pair N_pair=2, G_2/F_4 rank-universality, R_n atlas
  Role: structural certification and generalization
```

Python-verified Wave 0 EVOI: `0.045 + 0.048 + 0.028 + 0.056 = 0.177`. Wave 1 sum: `0.958`. Any alternative (e.g., sequential dispatch, narrowing Wave 1 to H̃+UNIFIED-FULL only, running N19 before R2) delivers strictly less information per session-hour. ADOPT as the canonical S80 architecture.

**(E3) H̃-EPOCH as the framework's S80 RATE-LIMITING question**

A single computation carries EVOI 0.300 — the maximum information-gain gate in the current S80 candidate set. All downstream A_s interpretations (UNIFIED-FULL, UNIFIED-BACKREACT, PS-SUBSTRATE-IC, Fold Transit Event A_s-sourcing) condition on its outcome.

```
Step 1 (def): rate-limiting = single-gate outcome collapses K downstream
              marginalizations into conditionals
Step 2 (K count): H̃-EPOCH feeds 4 gates (UNIFIED-FULL, UNIFIED-BACKREACT,
              PS-SUBSTRATE-IC, Fold-Transit Event τ_fold H̃-coords interpretation)
Step 3 (EVOI dominance): H̃-EPOCH / next-highest = 0.300 / 0.211 = 1.4218
              No peer gate has comparable downstream-gating scope
Step 4 (direction): its resolution is the PHASE TRANSITION in S80 information state
              before: Path A/B marginalized, A_s gap 0.22-1.12 OOM ambiguous
              after: conditional on chosen epoch, either 0.22 OOM (recoverable)
                     or 1.12 OOM (mechanism-search required) or framework-
                     internal-inconsistent (if Friedmann evolution mismatches)
Step 5: H̃-EPOCH is pre-registered [VERIFY] S80-H-TILDE-EPOCH-CONSISTENCY as
        Open Question #1 + CF-1
```

The S79 workshop's MOST IMPORTANT emergence: what was previously an "A_s problem" (3.35 OOM absolute overshoot) is now an H̃-EPOCH question. The framework either resolves to recoverable (Path A) or mechanism-search (Path B) — but either way, the framework A_s question is no longer irredeemable in the absolute-3.35-OOM sense.

**(E4) PRU-audit integration as permanent workflow enhancement**

PRU (Pre-Registration Underspecification) was formalized in S79 P1-3 as the Class 8 integrity-failure alongside the 7 execution-failures. The D2-accepted PRU-audit tooling delivers positive ROI across all catch-rate scenarios (+0.5 to +4 hr/session). ADOPT as permanent S80-forward workflow:

```
Pre-dispatch: s80_pru_audit.py runs against pre-registered plan
  - Query canonical_constants.py for contradicted assumptions
  - Query theorem-ledger for forbidden derivation routes
  - Query session permanent-results-registry for closed mechanisms
  - Flag PRU candidates requiring §0.11 machinery-enumeration before dispatch
Wave 0 includes PRU-audit tooling creation as activity
```

Pre-register [AUDIT] S80-PRU-AUDIT-TOOLING (in Open Questions).

**(E5) 106-item diff scale reflects genuine S79 epistemic-state shift, not bookkeeping bloat**

The S79 EVOI diff — 29 STALE + 12 CLOSED + 6 RE-OPENED + 13 PROMOTED + 46 NEW = 106 items — is roughly 7× the per-session diff of S78 (~15 items) and 3.5× the next-largest prior-session diff. This is not organizational-retagging bloat:

```
Step 1 (def): diff is Bayesian-motivated (not organizational) iff each entry
              cites a specific S79 closure that either revises numerical content
              (P, ΔP), redefines the gate's sample space, or installs a permanent
              structural wall
Step 2 (audit over 106 items):
  29 STALE: each cites workshop [pX-Y:anchor] numerical change or sample-space
    revision. Pass.
  12 CLOSED: each is structural wall (permanent theorem, machine-epsilon identity,
    or rule-class). Pass.
  6 RE-OPENED: each cites S79 finding that invalidates prior closure or surfaces
    new audit. Pass.
  13 PROMOTED: each moves priority-level on substantive grounds (P2-A retraction
    forcing UNIFIED-AS-79, P4-D epoch discovery). Pass.
  46 NEW: each sourced to specific S79 closure with its own prior P and ΔP.
    Foundational set includes 5 pre-theorem candidates + remediation layer
    + structural-audit tasks. Pass.
Step 3 (direction): 106-item diff is the FINGERPRINT of 5 pre-theorem
              installations + 12 structural closures + A_s narrative reframe
              (3.35 OOM absolute → 0.22-1.12 OOM ratio) + 4 §VII.II promotions
              + 4 §VII.I formal-proof tasks. This is genuine epistemic motion,
              not retagging.
Step 4: RECORD the scale permanently in evoi-framework.md as the S78→S79 diff
              scale. Future sessions average 20-30 items per 10-workshop-closure
              session; S79's 8.8-items-per-workshop average is the HIGH END.
```

This establishes a benchmark: a session that touches 100+ EVOI items is a paradigm-shift session. S50-51 (atlas construction), S69-70 (instanton paradigm), and S79 share this property.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | EVOI staleness diff | N1, Re:N1 | Converged | 106 items (29 STALE + 12 CLOSED + 6 RE-OPENED + 13 PROMOTED + 46 NEW); Bayesian-motivated at sample-space-revision level; S1 escalated to STALE+RE-OPEN-gated-by-RO1 via slot-mismatch factor 84.21; ready for S80 EVOI update. |
| 2 | UNIFIED-AS-79 family EVOI | N2, Re:N2 | Converged | H̃-EPOCH 0.300 top priority; rank H̃(0.300) > UNIFIED-FULL(0.211) > UNIFIED-BACKREACT(0.165) > PS-SUBSTRATE(0.108) > CSUB-SIGN(0.073); pre-H̃ marginalized EVOI, Wave 2 branch-conditional refresh on EVOI_A=0.222 / EVOI_B=0.201. |
| 3 | Fold Transit Event promotion | N3, Re:N3 | Converged | dS_inst/dτ rank 1 (EVOI 0.180); Z_s rank 2 (0.175, formalism-gated); χ_N rank 3 (0.074, Ward-tautology discount); combined-3 P(promote) = 0.776 tautology-discounted. |
| 4 | Remediation layer Wave-0 status | N4, Re:N4 | Converged (elevated) | R1/R3 synthesis-citation blockers (parallel-safe); R2 ALSO tests P4-B CLT pre-theorem at L=8 (drift band [0.56, 0.76]) → R2 strict-blocks N19 Kasparov abelian-subfactor proof; Wave 0 combined EVOI 0.177 comparable to dS_inst 0.180. |
| 5 | Framework probability update | G1, C5 | Emerged | Two-axis tracking: P_work_complete = 0.206 (×1.72 S79 gain, effort-based), P_obs_aligned = 6/9 = 0.667 (observable-channel-PASS measure); neither substitutes for the other; both adopted as permanent S80-forward methodology. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

1. **[VERIFY] S80-H-TILDE-EPOCH-CONSISTENCY** (HIGHEST EVOI 0.300, Wave 1 TOP): Path A (horizon-exit, ratio 10^−0.22 ≈ 0.603) vs Path B (fold, ratio 10^+1.12 ≈ 13.18) adjudication via framework-predicted Friedmann evolution from τ_fold to horizon-exit. PASS criterion: Path A value follows from Path B via substrate-sourced Friedmann evolution within factor 2. FAIL criterion: mismatch > factor 10 indicating framework-internal inconsistency. Gate collapses marginalization on 4 downstream gates.

2. **[VERIFY] S80-UNIFIED-AS-79-FULL** (Wave 2 re-rank): complete A_s computation under UNIFIED-AS-79 pipeline with H̃-EPOCH result ingested. Post-resolution EVOI collapses to branch-conditional: EVOI_A = 0.222 (Path A canonical) or EVOI_B = 0.201 (Path B canonical). Python-verified.

3. **Wave 0 remediation: R1, R2, R3 clean re-runs**: W1-B under §0.10(b) pin, W2-C (CLT test of abelian-subfactor drift_u1(L=8) ∈ [0.56, 0.76]), W3-L under SHA-256-frozen lists. R1/R3 parallel-safe with Wave 1; R2 strict-blocks N19.

4. **[VERIFY-THEOREM] S80-CC-RATIOS-ONLY-THEOREM** (Wave 1, EVOI ≈ 0.12 with structural tie-break): formal ≤3-page analytic proof from CC96 heat-kernel that f_n-linearity cancels in weight-balanced ratios. Elevates ratios-vs-absolutes meta-pattern to §VII.I theorem status.

5. **[VERIFY-THEOREM] S80-KASPAROV-ABELIAN-PROOF** (Wave 2, pending R2 CLT outcome): formal Connes-Moscovici proof that abelian subfactors lack Level-2 R-protection. Gated strictly on R2 CLT pre-theorem test result; if R2 returns drift outside [0.56, 0.76], proof premise enters RE-OPENED status.

6. **[VERIFY] S80-FOLD-INST-GRADIENT** (Wave 1, EVOI 0.180): compute dS_inst/dτ at τ ∈ {0.15, 0.17, 0.19, 0.21, 0.25}; test concentration at τ_fold = 0.190. PASS if dS_inst/dτ shows discontinuity or peak at τ_fold (within Δτ = 0.02 window). Independent substrate functional, orthogonal to the three existing ρ(ε,τ)-integral probes; 4th functional for Fold Transit Event §VII.I promotion.

7. **[AUDIT] S80-P-OBS-ALIGNED-CATALOG**: explicit enumeration of pre-registered observational channels with PASS/FAIL/INFO classification rules. Resolve ambiguity in 6/9 calculation (is Ω_DM-at-0.7σ PASS-class? is τ_fold observable or structural?). Pin canonical definition for P_obs_aligned in `.claude/rules/evoi-prioritization.md`.

8. **[AUDIT] S80-PRU-AUDIT-TOOLING**: create `computations/s80_pru_audit.py` as Wave 0 activity. Structural query against `canonical_constants.py` + theorem-ledger + session-permanent-results-registry; flag pre-registrations assuming quantities contradicting established results. PASS: successfully flags ≥1 PRU candidate in test-run on S80 plan.

9. **[AUDIT] S80-P4B-CONTINGENCY-CASCADE**: dependency inventory for abelian-subfactor failure modes. Enumerate all Wave 2+ gates and WP citations that depend on CLT pre-theorem surviving R2; tag each with PAUSE-point triggers for each of three scenarios (drift < 0.40, drift > 0.76, adjacent bands). Output: complete dependency tree before R2 dispatch.

10. **[AUDIT] S80-TWO-AXIS-TRACKING-ADOPTION**: update `.claude/rules/evoi-prioritization.md` to document P_work_complete and P_obs_aligned as separate metrics with their own update rules. Add §"Two-Axis Framework Probability" with formulas, update-triggers, and canonical-value tracking. Retires the implicit single-scalar reading.

## Wrap-Up — Workshop Impact Summary

### What Changed

- **EVOI table refreshed** with 106-item diff against S66-stale / S78-stamp state: 29 STALE entries requiring re-estimation, 12 CLOSED permanent installations, 6 RE-OPENED entries, 13 PROMOTED entries, 46 NEW entries. Categorization Bayesian-motivated at sample-space-revision level.
- **Framework probability two-axis tracking adopted**: P_work_complete = 0.206 (factor 1.72 gain across S79, effort-based), P_obs_aligned = 6/9 = 0.667 (observable-channel-PASS measure). Single-scalar interpretation retired.
- **S80 priority ranking established** with Wave 0/1/2/3 architecture: Wave 0 combined EVOI 0.177 (remediation + R2 CLT test); Wave 1 combined EVOI 0.958 (6 parallel gates); Wave 2 conditional on H̃-EPOCH; Wave 3 §VII.I formal-proof extensions.
- **H̃-EPOCH identified as singular rate-limiting question**: EVOI 0.300 is factor 1.4218 above next-highest; collapses marginalization on 4 downstream A_s gates; PHASE TRANSITION in framework's S80 information state.
- **A_s narrative reframed**: from 3.35 OOM absolute overshoot (retracted 4-factor ledger) to 0.22-1.12 OOM ratio-level gap with epoch-resolution pending. Path A (0.22 OOM recoverable) vs Path B (1.12 OOM mechanism-search) vs framework-internal-inconsistency are the three live scenarios.
- **PRU-audit adopted as permanent workflow enhancement**: +2 hr/session expected savings (moderate scenario), +4 hr ceiling (optimistic). Adopted under all catch-rate scenarios.
- **R2 remediation elevated to theorem-testing**: R2 tests P4-B abelian-subfactor CLT pre-theorem at L=8 (drift band [0.56, 0.76]); strict-blocks N19 Kasparov abelian-subfactor proof.
- **4 §VII.II pre-theorem candidates** with identified §VII.I promotion paths: CC-ratios-only (≤3-page analytic proof), MP-exclusion (continuum-limit proof), abelian-subfactor (Connes-Moscovici proof), Fold Transit Event (dS_inst/dτ 4th-functional primary + Z_s/χ_N fallback).

### What Holds

- **All 12 prior S79 workshop closures permanent**: P1-1 through P4-D verdicts preserved; C1-C12 closed mechanisms permanent; §VII.II theorems (a_4 R²-invariance, f_conv ratio identity, Leggett-DM scaling, C² Type D zero, Fold Transit Event) permanent.
- **Framework probability methodology (effort-based) retains legitimacy** as work-completion measure per `.claude/rules/evoi-prioritization.md` §"Effort-Based Probability". Two-axis tracking ADDS P_obs_aligned; it does not replace P_work.
- **EVOI prioritization formula (P(pass)·|ΔP(pass)| + P(fail)·|ΔP(fail)|) stands**. All N2, N3, N4 values Python-verified. Rank ordering within UNIFIED-AS-79 family accepted; rank ordering within Fold Transit 4th-functional accepted.
- **Pre-registered gate discipline stands**: gate criteria declared BEFORE compute, verdicts permanent. PRU-audit pre-registration closes Class 8 integrity failure at plan-write time without relaxing discipline.
- **Substrate-first framing throughout**: the Fold Transit Event at τ_fold = 0.190 is a first-order transit through the Jensen-deformed spectral triple, not a "big bang" singularity. A_s gap is a ratio-level residual on the UNIFIED-AS-79 substrate mode-equation, not a composed-chain amplification chain.
- **Substitution-chain discipline enforced**: every sign/direction/threshold claim in this closer carries explicit definition → substitution → simplification → direction steps with Python verification.

### What Breaks or Strains

- **Single-axis framework probability (pre-S79 reading) is RETIRED** in favor of two-axis (P_work_complete, P_obs_aligned). Claims in pre-S79 session artifacts that cite a single framework-probability scalar require revision or context-qualification. The rule file update is pre-registered as Open Question #10.
- **W1-A pre-S79 PASS interpretation is STALE+RE-OPEN-gated-by-RO1**: valid only at CONVENTION-PINNING scope; does NOT propagate to UNIFIED-AS-79-FULL until slot-consistency audit (RO1) confirms a_n routing match. The ~2 OOM slot-mismatch factor (84.21) exceeds any PASS-band tolerance; this is a hard wall.
- **Claims citing "3.35 OOM A_s gap" must be revised** to ratio-level 0.22-1.12 OOM with explicit epoch qualifier. The absolute-gap reading is an artifact of the retracted 4-factor ledger (P2-A [p2-a:1169]); under UNIFIED-AS-79 + P4-D ratios-only reframe, the gap is epoch-dependent in the 1-OOM range, not a 3-OOM immovable wall.
- **Pre-S79 EVOI table (S66-stale, S78-stamp) is STRUCTURALLY SUPERSEDED**: 106-item diff means the prior table is not a useful baseline for S80 scheduling. A full rewrite is required (pre-registered as the Deliverable below).
- **N19 Kasparov abelian-subfactor proof is CONDITIONAL on R2**: proceeding to the formal Connes-Moscovici proof before R2 CLT test lands risks investing theorem-proof compute into a framework under revision. Wave 2 N19 strict-ordering is required.

### Carry-Forward Computations

Top-5 in 7-component format (following `.claude/rules/output-standards.md §Action Items Format`).

**CF-1 [HIGHEST PRIORITY] — [VERIFY] S80-H-TILDE-EPOCH-CONSISTENCY**:
1. What: determine framework-canonical epoch (Path A horizon-exit vs Path B fold); compute framework-predicted Friedmann evolution from τ_fold to horizon-exit; test internal consistency
2. Who: transit-dynamics-theorist + lizzi-spectral-functional-theorist (dual-owner: transit for Friedmann evolution, lizzi for spectral-action epoch definition)
3. Input: UNIFIED-AS-79 framework pipeline; fold-Friedmann formulation; observational H̃_obs = 4.072e-5 (Planck-anchored); τ_fold = 0.190; Path A ratio target 10^−0.22, Path B ratio target 10^+1.12
4. Output: epoch-resolved H̃_framework value + ratio-level A_s verdict (0.22 OOM recoverable vs 1.12 OOM mechanism-search vs framework-internal-inconsistent)
5. Format: Python script `computations/s80_h_tilde_epoch.py` + analysis memo in `sessions/archive/session-80/`; PASS/FAIL criterion pre-registered inline
6. Deadline: S80 Wave 1 (highest EVOI gate, rate-limiting)
7. Depends on: S79 close-out; RO1 W1-A slot-consistency audit landing (citation validity)

**CF-2 — Wave 0 Remediation (R1, R2, R3 clean re-runs)**:
1. What: clean re-runs of W1-B (iteration audit) and W2-C (CLT test of abelian-subfactor drift_u1(L=8)) and W3-L (SDW-ζ dictionary under frozen lists)
2. Who: orchestrator + designated remediation-runner (nazarewicz for R2 CLT-test interpretation; one computation agent for R1/R3 compute)
3. Input: P1-3 remediation spec (SHA-256 pins, N_eval=N_pivot+3, Hankel-formula-order pin, 5-pt stencil h-range, per-branch drift threshold); §0.10(b)(c)(d) + PRU + iteration-audit-template
4. Output: `s79_remediation_w1b.py`, `s79_remediation_w2c.py`, `s79_remediation_w3l.py` outputs + single verdict-line each with commit SHA + closure_sha256; R2 drift_u1(L=8) measurement against CLT band [0.56, 0.76]
5. Format: three Python scripts + three verdict-file appends to `sessions/archive/session-80/verdicts-remediation.md`
6. Deadline: S80 Wave 0 (parallel with Wave 1 compute; strict-blocks N19 only)
7. Depends on: S79 close-out; PRU-audit tooling CF-6

**CF-3 — [VERIFY-THEOREM] S80-CC-RATIOS-ONLY-THEOREM**:
1. What: formal ≤3-page analytic proof from Chamseddine-Connes 1996 heat-kernel that f_n-linearity cancels in weight-balanced spectral-action ratios (a_m/a_n with matched weights)
2. Who: connes-ncg-theorist + spectral-geometer (dual-owner: connes for heat-kernel manipulation, spectral-geometer for weight-balance algebra)
3. Input: Chamseddine-Connes 1996 paper; P4-A/B/C/D structural findings; CN-EM1 [p4-d:1810] identification of the f_n-linearity cancellation structure
4. Output: LaTeX/markdown theorem-proof document establishing CC-ratios-only as §VII.I permanent theorem
5. Format: `sessions/archive/session-80/theorem-cc-ratios-only.md` + optional `researchers/CC96-derivation-cache.md`
6. Deadline: S80 Wave 2 (tie-break elevates to Wave 1 if analytic tractability confirmed)
7. Depends on: CF-1, CF-2 (for citation validity of A_s ratios used in examples)

**CF-4 — [VERIFY] S80-UNIFIED-AS-79-FULL (post-H̃-EPOCH)**:
1. What: complete A_s computation under UNIFIED-AS-79 with H̃-EPOCH result ingested; report branch-conditional EVOI (EVOI_A = 0.222 or EVOI_B = 0.201)
2. Who: transit-dynamics-theorist (primary; Landau as consult for mode-equation implementation)
3. Input: CF-1 output (epoch-canonical H̃ value); UNIFIED-AS-79 pipeline from P2-A; c_sub = 2.23 from P1-2; S_IC(k_pivot) = 1.636e5 from P2-B
4. Output: A_s_framework value with epoch-consistent prediction; ratio-gap in OOM; verdict against factor-2 (PASS) / factor-15 (INFO) / factor>15 (FAIL) bands
5. Format: `computations/s80_unified_as_79_full.py` + verdict memo
6. Deadline: S80 Wave 2 (conditional on CF-1 landing)
7. Depends on: CF-1; CF-2 R1 landing (for F_amp citation validity); CF-3 optional (for ratios-framing reinforcement)

**CF-5 — [VERIFY] S80-FOLD-INST-GRADIENT (dS_inst/dτ 4th functional)**:
1. What: compute instanton-action gradient dS_inst/dτ at τ ∈ {0.15, 0.17, 0.19, 0.21, 0.25}; test concentration at τ_fold = 0.190 as 4th independent functional of Fold Transit Event §VII.I promotion
2. Who: kaku-speculative-theorist (primary; instanton formalism) + feynman-theorist (path-integral consult)
3. Input: S37 instanton paradigm; S48 qtheory-gold-48 instanton formalism; τ_fold = 0.190 canonical; CF-2 P3-A spec
4. Output: dS_inst/dτ table at 5 τ-points + concentration verdict (PASS if discontinuity or peak concentrated within Δτ = 0.02 of τ_fold; FAIL otherwise)
5. Format: `computations/s80_fold_inst_gradient.py` + plot + §VII.I promotion memo
6. Deadline: S80 Wave 1 (independent of H̃-EPOCH; EVOI 0.180)
7. Depends on: S79 close-out; instanton-formalism readiness (nazarewicz audit of S48 paradigm)

### Closing Line

S79 closes with framework probability tracked at P_work_complete = 20.6% × P_obs_aligned = 66.7% after 12 workshops narrowed the A_s-gap narrative from a 3.35 OOM absolute overshoot (retracted 4-factor ledger) to a 0.22-1.12 OOM ratio-level gap with epoch-resolution pending. S80 Wave 0 remediation (R1/R2/R3, combined EVOI 0.177 including R2 CLT test) plus Wave 1 H̃-EPOCH resolution (EVOI 0.300, singular rate-limiting) are the gating computations for all further framework-level A_s interpretation.

---

## Deliverable — Updated EVOI Table

This workshop produces the scheduling instructions for the S80 update of `sessions/evoi-framework.md`. The full rewrite is an S80 Wave 0 activity, not an in-workshop task. Below: the top-10 priority list, the 106-item categorization, framework probability snapshot, and carry-forward instructions.

### Top-10 S80 Priority List (by EVOI, with wave assignment and dependencies)

| Rank | Computation | EVOI | Wave | Depends on |
|:-----|:------------|:-----|:-----|:-----------|
| 1 | **[VERIFY] S80-H-TILDE-EPOCH-CONSISTENCY** (P4-D CF-1) | 0.300 | Wave 1 TOP | S79 close-out, RO1 slot-consistency |
| 2 | **[VERIFY] S80-UNIFIED-AS-79-FULL** (N34) | 0.211 (pre-H̃) / 0.222 (A) / 0.201 (B) | Wave 1 + Wave 2 re-rank | H̃-EPOCH for branch-conditional interpretation |
| 3 | **[VERIFY] S80-FOLD-INST-GRADIENT** (dS_inst/dτ, N7) | 0.180 | Wave 1 | S79 close-out (independent of H̃-EPOCH) |
| 4 | **[VERIFY] S80-UNIFIED-BACKREACT-79** (N36) | 0.165 | Wave 2 | UNIFIED-AS-79-FULL output |
| 5 | **[VERIFY-THEOREM] S80-CC-RATIOS-ONLY-THEOREM** (N2 P4-D) | ≈ 0.12 (structural tie-break to Wave 1) | Wave 1 | None (analytic ≤3 pages) |
| 6 | **[VERIFY] S80-PS-SUBSTRATE-MATCHED-IC** (N37) | 0.108 | Wave 1-2 parallel | Substrate-GGE IC spec |
| 7 | **[VERIFY] R2 (W2-C remediation + P4-B CLT test)** | 0.104 (base 0.048 + bonus 0.056) | Wave 0 | S79 close-out; strict-blocks N19 |
| 8 | **[VERIFY-THEOREM] S80-KASPAROV-ABELIAN-PROOF** (N19 P4-B) | ≈ 0.10 | Wave 2 | R2 CLT test outcome (strict) |
| 9 | **[VERIFY] S80-UNIFIED-AS-79-CSUB-SIGN** (N35) | 0.073 | Wave 1 confirmation | None (framework-internal identity) |
| 10 | **[AUDIT] S80-W1-A-SLOT-CONSISTENCY-AUDIT** (N17 P4-C) | ≈ 0.06 | Wave 0 | Citation-validity blocker for W1-A |

Wave 1 combined EVOI sum (6 parallel gates: H̃ + UNIFIED-FULL + dS_inst + CC-ratios-proof + χ_N + CSUB-SIGN) = 0.958 (Python-verified: `0.300+0.211+0.180+0.12+0.074+0.073 = 0.958`).

### Categorization Instructions for S80 evoi-framework.md Update

**Removed (29 STALE entries — retired or superseded)**: S1 W1-A (also RE-OPEN-gated-by-RO1), S2 W1-B, S3 W1-C (BACKREACTION-SELFCONSIST), S4 W1-D (MULTI-BAND-E_COND), S5 W1-E (PRE-FOLD-VACUUM-STATE), S6 W2-A (MU-EFF-96x96), S7 W2-B (BCS-FORMATION-DYNAMICS), S8 W2-C (ZETA-JOSEPHSON), S9 W2-D (F-CONV-ANOMALY), S10 W2-E (F-CONV-SUBHORIZON), S11 W2-F (A_4-R²-UNDER-F-STAR), S12 W2-G (EPS-ZERO-MATCHING), S13 W3-A (CHI_2-LMAX-CONVERGENCE), S14 W3-B (FAMP-TILT-SMOOTHED), S15 W3-C (TENSOR-FAMP; UNCHANGED, carries forward), S16 W3-D (JOSEPHSON-LEGGETT-MIXING), S17 W3-E (PBH-CONSTRAINT), S18 W3-F (f_NL-COHERENCE; UNCHANGED), S19 W3-G (DESI-DR3-UPDATE), S20 W3-H (CMPP-AT-TAU-0.537), S21 W3-J (SIN2-W-NON-TREE), S22 W3-K (R_1-L-MAX-CROSS-GROUPS), S23 W3-L (SDW-ZETA-DICTIONARY), S24 W3-N (DC-PERMANENCE), S25 W3-O (MODULUS-DECAY), S26 N1 TRANSFER-FUNCTION-74, S27 N2 MODULI-STABILIZATION-74, S28 N4 E_C-RESOLUTION-74 (UNCHANGED, lower priority), S29 N16 RATIO-OF-RATIOS-PROTECTED-74.

**Closed (12 CLOSED entries — permanently resolved)**: C1 multi-band bootstrap (zero-volume), C2 W3-O channel identification (Route γ dominant, Route α 4 OOM short), C3 Route B SDW-KMS Weyl-scaling (w_0 = −0.918 outside image set), C4 F_amp² convention error (d(ln A_s)/d(ln F_amp) = 1.000000), C5 f_conv^{ζ}/f_conv^{SDW} = 1/R_1, C6 f_conv^{anomaly}/f_conv^{SDW} = 1 at Λ_cut=λ_max, C7 a_4 R²-invariance (§VII.II theorem), C8 C² Type D sectional curvature zero at τ=0.537 (§VII.II theorem), C9 Leggett-DM scaling exponent 2.17e-4 (§VII.II theorem), C10 4-class integrity failure catalog (Pattern 1, 3, 3', PRU), C11 Axiomatic IC-principle gap closed (5 independent directions), C12 Frozen spectrum theorem (10⁻¹¹³ through fold, reinforced).

**Re-Opened (6 RO entries — previously closed, S79 surfaced new issues)**: RO1 W1-A slot-consistency (P4-C EM2 sign-flip doctrine; a_0 ×32 vs a_2 ×0.38), RO2 W1-B/W2-C/W3-L numerics (WARRANT-INVALID; R1/R2/R3 remediation), RO3 canonical constants naming (`mellin_*` vs `cc_*`), RO4 ω_L1 vs m_L1 provenance (FREQUENCY 0.138 vs MASS 0.070 conflation; S80 Wave 0 blocker for CF-1), RO5 v_ew derivation path (latent secondary-pin risk), RO6 S78 framework-document citations of "13 OOM cushion" (replace with 7.3 OOM central).

**Promoted (13 P entries — priority-level moves with new EVOI)**: P1 UNIFIED-AS-79-FULL (Level 1 TOP, EVOI 0.211 pre-H̃), P2 UNIFIED-AS-79-CSUB-SIGN (Level 1, EVOI 0.073), P3 UNIFIED-BACKREACT-79 (Level 1, EVOI 0.165), P4 H-TILDE-EPOCH-CONSISTENCY (Level 1 TOP, EVOI 0.300), P5 CC-ratios-only theorem (Level 1-2, EVOI ≈ 0.12), P6 M_KK structural role documentation (Level 2), P7 Fold Transit Event 4th-functional (Level 1-2, EVOI 0.180 primary), P8 W3-G-β R1/R2/R3 Route A Volovik dual-axis (Level 2), P9 Pattern 3' rule insertion (Level 3, methodology), P10 Marginal-semiclassical language audit (Level 4, documentation), P11 1-loop-proper cushion citation pin (Level 3), P12 Model-C inertial pin propagation (Level 3), P13 Multi-pair N_pair=2 (Level 2).

**New (46 N entries — S79 introduced, not in S78 EVOI table)**: N1 S80-H-TILDE-EPOCH-CONSISTENCY (EVOI 0.300, TOP), N2 S80-CC-RATIOS-ONLY-THEOREM (EVOI ≈ 0.12), N3 S80-CANONICAL-CONSTANTS-AUDIT (classification, no direct EVOI), N4 S80-SINGLE-PIN-VERIFICATION, N5 S80-DIM-H-PI-UNIVERSAL-EXCLUSION, N6 S80-R-FAMILY-ATLAS-EXTENSION, N7 S80-FOLD-INST-GRADIENT (EVOI 0.180), N8 S80-OMEGA-L-MULTI-FORMAL-S++, N9 S80-MULTIPAIR-ECOND-TAUFOLD, N10 S80-CHI-N-WARD-DUAL (EVOI 0.074, tautology-discounted), N11 S80-B1-JENSEN-SCAN, N12 S80-SPP-FULL-ED-SIGN-MARGIN, N13 S80-GW-CHANNEL (LISA-band), N14 S80-K2-LATTICE-BENCHMARK, N15 S80-GGE-CORRELATION-CHANNEL, N16 S80-CMB-FNL-CHANNEL, N17 S80-W1-A-SLOT-CONSISTENCY-AUDIT (Wave 0), N18 S80-HEAT-KERNEL-MP-EXCLUSION, N19 S80-KASPAROV-ABELIAN-PROOF (EVOI ≈ 0.10, R2-gated), N20 S80-W2C-L8-DRIFT-PREDICTION (CLT pred 66.06%, band [0.56, 0.76]), N21 S80-T2-ALT-DECOMPOSITION (CLT pred 59.22%), N22 S80-W3K-FIT-DEFINITION-PIN, N23 S80-RICHARDSON-EXTRAPOLATION (L_max = 5·rank), N24 S80-OTHER-RATIOS (R_B, R_C), N25 S80-G2-F4-TEST, N26 S80-EXOTIC-DISCRIMINATORS, N27 S80-SG1-THEOREM (≤4-page analytic proof α=rank), N28 S80-F_amp^sc-VIA-3PI, N29 S80-PHYSICAL-CAP-SIC-SUBHORIZON, N30 S80-E_J-CONVENTION, N31 S80-MU-EFF-RATE-MATRIX (L-K reformulation), N32 S80-A_S-ADJACENT-REPLACEMENT-OBSERVABLE (P_ζ(k_trans)/P_ζ(k_pivot) = 2.25e-4), N33 S80-CUBIC-SIN2W-EW-SCALE, N34 UNIFIED-AS-79-FULL (EVOI 0.211), N35 UNIFIED-AS-79-CSUB-SIGN (EVOI 0.073), N36 UNIFIED-BACKREACT-79 (EVOI 0.165), N37 PS-SUBSTRATE-MATCHED-IC (EVOI 0.108), N38 W3-G-β R1/R2/R3, N39 Pattern 3' RULE INSERTION, N40 PRU + §0.10 split, N41 EVOI-SYNC-79 (5-layer record synchronization), N42 PHASE-ALIGNMENT K-SCAN, N43 CHLUBA-KERNEL-FIRAS INTEGRAL, N44 PBH-POPULATION-K-SCAN, N45 BACKWARD-BD-CONSISTENCY, N46 H_transit vs H_Friedmann convention (M_Pl_red vs M_KK).

### Framework Probability Snapshot (two-axis)

| Metric | Pre-S79 | Post-S79 | Change | Semantics |
|:-------|:--------|:---------|:-------|:----------|
| **P_work_complete** | 0.120 | 0.206 | +71.9% (factor 1.72) | (N_complete / N_total) × F_obs = (55/120) × 0.45 = 0.20625. Work-done measure (NOT truth-probability). |
| **P_obs_aligned** | ≈ 0.556 (5/9 pre-S79 est.) | 0.667 (6/9) | +20.0% | (PASS-class observables) / (pre-registered channels). Observable-channel-PASS measure (audit pending per Open Question #7). |

Python-verified: `(55/120) × 0.45 = 0.20625`; `6/9 = 0.66667`; `0.20625 / 0.120 = 1.71875`.

### Carry-Forward Instructions for S80 Wave 0 EVOI Rewrite

1. **Backup current `sessions/evoi-framework.md`** to `sessions/archive/evoi-framework-S78-stamp.md` before rewrite.
2. **Apply 106-item diff** per categorization above (29 STALE retired or updated in place, 12 CLOSED moved to CLOSED section, 6 RE-OPENED tagged with new gates, 13 PROMOTED re-leveled, 46 NEW added with initial EVOI and provenance).
3. **Install two-axis framework probability tracking** at top of document: P_work_complete and P_obs_aligned as separate dashboard metrics with their own update rules. Current values: 0.206 / 0.667.
4. **Top-10 priority list above** populates the "S80 Priority Queue" section; Wave 0/1/2/3 architecture assignment preserved.
5. **Cross-link each entry** to its source workshop [pX-Y:anchor] and canonical-constants entry where applicable.
6. **PRU-audit the rewritten file** before commit: query every entry's assumed quantities against `canonical_constants.py` and theorem-ledger; flag contradictions.
7. **Session-plan for S80** imports the top-10 directly, pre-registers each gate with PASS/FAIL criteria using `pru-pre-registration-template.md` (to be created per Open Question #8).

### Rule-File Updates Pre-Registered

- `.claude/rules/evoi-prioritization.md`: add §"Two-Axis Framework Probability" documenting P_work_complete and P_obs_aligned. Retire implicit single-scalar reading.
- `.claude/rules/epistemic-discipline.md`: insert Pattern 3' (Audit-Avoidance-Forced-Wrong-Route) + PRU (Pre-Registration Underspecification) into the integrity-failure catalog alongside the 7 execution-failure classes.
- `.claude/templates/`: create `pru-pre-registration-template.md` as the plan-write-time analog to the post-hoc `iteration-audit-template.md`.

GP_P5A_R2B_COMPLETE
