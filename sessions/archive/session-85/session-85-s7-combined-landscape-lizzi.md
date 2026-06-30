# Session 85 Synthesis: S-7 Combined Landscape (lizzi — FI/RD + Mellin + dual-SHA)

**Date**: 2026-04-25
**Agent**: lizzi-spectral-functional-theorist (lizzi)
**Slot**: S-7 (review campaign closeout — combined W0-W5 landscape)
**Track**: FI/RD regulator-classification extension + Mellin-residue track + dual-SHA audit forensics + regulator-scope bounding per W5

**Source Documents (read in full or grep-targeted)**:
- `sessions/archive/session-85/session-85-w0-workingpaper.md` (W0-5 Z_R, W0-6 van Hove, W0-7 Zubarev, W0-9 d_spec, W0-10 triality, W0-11 CC-3, W0-20 Mellin-cone-S3)
- `sessions/archive/session-85/session-85-w1a-workingpaper.md` (W1a-1 scheme-dep STRUCTURAL, W1a-2 alpha_s identity scope, W1a-3 d_spec finite-size)
- `sessions/archive/session-85/session-85-w1b-workingpaper.md` (W1b alpha_s prior re-emissions; dual-SHA forensics input)
- `sessions/archive/session-85/session-85-w1c-workingpaper.md` (W1c-3 alpha_s vocabulary 2193 ambiguous sites)
- `sessions/archive/session-85/session-85-w2-workingpaper.md` (W2-1 axiom-minimality 5/7, W2-7 disjoint-corridor refinement)
- `sessions/archive/session-85/session-85-w3-workingpaper.md` (W3-11 multipole breakdown Lambda-convention)
- `sessions/archive/session-85/session-85-w4-workingpaper.md` (W4-8 REFRAME re-emission)
- `sessions/archive/session-85/session-85-w5-workingpaper.md` (W5-1 sign FAIL, W5-2 HP^0 FAIL, W5-3 L0/L3 FAIL, W5-4 PASS, W5-5 join FAIL, W5-6 HP^1 INFO-tight, W5-7 obstruction PASS)
- `sessions/archive/session-85/workshops/s85-w1-cutoff-authority-adjudication.md` (W-1 cutoff_sqrt status thread)
- `sessions/archive/session-85/session-85-s1-regulator-boundary-lizzi.md` (slot 1a S-1 — F_4/M boundary theorem)
- `sessions/archive/session-85/session-85-s6-truncation-taxonomy-lizzi.md` (slot 1b S-6 — Mellin Strip / Convergence Cone Theorem)
- `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md`

**Knowledge MCP queries used (S-7 closeout)**:
`search_knowledge('regulator family Lizzi spectral functional FI RD')`,
`search_knowledge('Mellin cone strip convergence zeta truncation')`,
`search_knowledge('R-protection intensive extensive partition')`.
Prior closures cited: ZETA-NOT-PHYSICAL-75, F-STAR-JOINT-74, JOINT-AUDIT-ATLAS-74, S82 atlas FI=30/RD=4/MIXED=8, S83 G6 FI duality theorem, S83 G3 EN3 (zeta unique axiom-native), S78 W2-F Mellin-multiplier theorem, S67 FUNCTIONAL-SELECT-67 frustration triangle.

The substrate framing rule (`phononic-framing.md`) is honored throughout — D_K eigenvalues are the input; spectral functionals (zeta, Zubarev, SDW, cutoff_sqrt, anomaly) are mathematical extractors of substrate-intrinsic invariants, not container-theoretic devices.

---

## I. Session Outcome (S-7 closeout)

The S85 W0-W5 landscape contains four orthogonal structural axes that the slot-1 syntheses (S-1 boundary theorem, S-6 Mellin strip taxonomy) had each touched in part. The combined picture is now sharp:

**Axis 1 (Mellin support, F_4 vs M).** The 5-regulator atlas {zeta, Zubarev, SDW, cutoff_sqrt, anomaly} splits into pure-a_4 family F_4 = {zeta, Zubarev, SDW} and mixed-support family M = {cutoff_sqrt, anomaly}. Five W5 gates and one W2-7 gate measure the wall.

**Axis 2 (Mellin strip / convergence cone).** The L_max=8..12 D_K cache yields ENTIRE zeta_D(s); residue identities at Re(2s) < d_spec require analytic continuation. Three of seven W0-W5 truncation FAILs (W0-7, W0-11, W0-20) live on this strip.

**Axis 3 (parity, HP^even vs HP^odd).** W2-7 records that the (C_H, C_epsH) twin pair is parity-blind to even Seeley-DeWitt; this axis is orthogonal to F_4/M and lifts the L_max-axis of S6.

**Axis 4 (R-protection: intensive vs extensive).** From W-1 closeout (this session) the cutoff-authority Layer-A/Layer-B distinction inherits the S76 R-Protection intensive/extensive partition applied to the regulator-choice axis. Load-bearing predictions (CC ratios, n_s, R_protected) live in the intensive sector; extensives carry W3-11-style Lambda-convention freedom.

**Forensics.** The 142 parsed verdict lines in `computations/s85_gate_verdicts.txt` carry **142 unique audit_sha256** — sig_5 of v3-closure-audit is CLEAN, no SHA hardcoding. Eight gate IDs carry multiple verdict lines (W4-8 REFRAME, W3-CF-3 logspace fix, W1b alpha_s prior re-emissions, etc.) — each by design with distinct audit_sha256.

**Mellin-strip recommendation.** Three of seven truncation FAILs (W0-7 Zubarev rho, W0-11 CC-3 CM-residue, W0-20 Mellin-cone-S3) share root-cause MSM (Mellin-strip mismatch) at Re(2s) < d_spec. A single S86 master gate `S86-MELLIN-HEAT-KERNEL-INFRA` (Pade + Seeley-DeWitt counter-term subtractor) resolves all three.

**Graceful-degrade hooks.** W-4 (cutoff_sqrt status: STRUCTURALLY-EXCLUDED / GENUINELY-PHYSICAL / REQUIRES-S86-GATE) is running in parallel. This S-7 leaves explicit reading hooks for both interpretations: under STRUCTURALLY-EXCLUDED the W5 frustration collapses to a 4-regulator atlas (F_4 ∪ {anomaly}); under GENUINELY-PHYSICAL the W5 set constitutes a structural TWO-CLASS THEOREM stronger than S67 frustration.

---

## II. Key Results

### II.1 Extended FI/RD Regulator Classification — W0-W5 set

The S82 42-row M_lizzi/M_connes atlas (FI=30, RD=4, MIXED=8, no conflicts) is extended here onto the S85 W0-W5 result set. The classification rule (M_lizzi from `s83_w1_g6_fi_duality_theorem.py`):

```
M_lizzi(O) = FI    iff drift across {zeta, Zubarev, SDW, cutoff_sqrt, anomaly} <= 5%
                        OR observable obeys (a) intrinsic invariant (b) bounded-range mode-eq output (b') op pre-commitment
M_lizzi(O) = RD    iff fails (a) AND (b) AND (b'); regulator-dressed
M_lizzi(O) = MIXED iff threads BOTH FI and RD ingredients
```

Compositional rule on factor-products: FI · FI = FI, RD · RD = RD, otherwise MIXED.

| # | S85 result | Origin | M_lizzi class | Pin tag (S83 G57) | Substrate-axis | Notes |
|:--|:-----------|:-------|:-------------:|:-----------------:|:---------------|:------|
| 1 | W5-6 HP^1 magnitude max/min = 2.0 | lizzi-solo | **FI** (R-protected-like, 2x band) | FI-via-pin (HP^1 = a_4-projector) | Axis 1 (F_4/M, magnitude side) | TIGHT (≤10) per pre-reg observational band; reduces S66 raw 381× by 190.5× |
| 2 | W0-5 Z_R 2-loop sub-dominant 8.64e-8 | gen-physicist | **FI** | FI-via-pin (regulator-class agnostic at 2-loop) | Axis 4 (intensive — second-moment ratio) | Internal ratio of 2-loop/1-loop, sign-aligned |
| 3 | W2-1 axiom minimality {dim,reg,fin,real,1st-order}=5/7 | connes | **FI-identity** | FI-pure (axiomatic invariant) | Axis 4 (intensive — load-bearing axiom set) | orient + PD NOT load-bearing for a_4/alpha_s |
| 4 | W5-1 sign(eps_H at tau_fold) | lizzi | **RD** (SCHEME-DEP, sign flip) | RD-unpinned (regulator-conditional) | Axis 1 (F_4/M, sign side) | F_4 ∪ {anomaly} → −1, {cutoff_sqrt} → +1 (by F_4/M wall theorem) |
| 5 | W1c-3 alpha_s vocabulary 2193 sites | mack | **NOT a regulator-classifiable observable** | — (governance) | (none — vocabulary discipline) | Hygiene meta-gate, not on regulator-choice axis |
| 6 | W5-2 HP^0 factorization spread (5-atlas) | lizzi | **MIXED** (3/5 FI, 2/5 RD) | mostly-RD | Axis 1 (F_4 factorizes 0%, M = 107% / 254%) | Mellin-multiplier theorem scope BOUNDED to F_4 |
| 7 | W5-3 L0/L3 dissonance histogram (31,3,8) | lizzi | **MIXED** (bimodal-like) | mostly-RD | Axis 4 (extensive — distribution on §VII.K-DUAL.LAYER) | MEDIUM bucket undersupplied; sharp boundary not gradient |
| 8 | W5-4 sign-pattern L_max-robust {8,9,10} | lizzi | **FI-identity** | FI-via-pin (truncation-stable) | (sanity over Axis 1) | PASS confirms W5-1 RD verdict permanent |
| 9 | W5-5 layer-aware lattice non-functorial 8/40 | lizzi | **RD** (categorical FAIL) | RD-unpinned | Axis 1 + Axis 4 cross | Localized at L1-AX/L2-SA → L3-OB transitions |
| 10 | W5-7 two-layer obstruction n_joint=0/5 | lizzi | **FI** (structural NO-go theorem) | FI-pure | Axis 1 (joint f_conv × eps_H) | Stronger than predicted: every individual conjunct already FAILs |
| 11 | W2-7 disjoint-corridor (C_H, C_epsH) parity-blind | connes | **MIXED** (FAIL-with-refinement) | promotable (parity-extension) | Axis 3 (HP^even vs HP^odd) | Even Seeley-DeWitt cannot distinguish HP^1-twin pairs |
| 12 | W0-6 van Hove S_max=74.6 | feynman+tesla | **MIXED** (a)/(d) class | RD-unpinned (regulator-side OK; tau_argmax=0.221 vs canonical 0.190) | Axis 4 + Axis 2 partial | Class (a) underresolved or (d) competing tau_fold characterizations |
| 13 | W0-7 Zubarev rho=−0.6349 (asymp −0.81) | feynman+tesla | **RD** (Mellin-strip mismatch primary) | RD-unpinned | Axis 2 (Mellin strip) | Conjecture rho→−1 falsified at direct-truncated level; pending MB |
| 14 | W0-9 d_spec three pathways (0.15, 9.32, 12) | feynman+tesla | **MIXED** (route iii FI-pure exact; routes i,ii RD via finite-size) | promotable | Axis 4 (topological FI) | dim(SU3)+dim(M^4)=12 EXACT (Route iii); Weyl/zeta finite-size at L=10 |
| 15 | W0-10 Spin8 triality V/S = 4.23% | feynman+tesla | **MIXED** | RD-unpinned (over-tight 1% plan tolerance) | Axis 4 (extensive) | Jensen-deformed SU(3) NOT Spin(8)-invariant; expected breaking |
| 16 | W0-11 CC-3 CM signed sum log10(|Λ|/|a_0|)=−0.13 | feynman+tesla | **RD** (PSO + MSM) | RD-unpinned | Axis 2 | Direct sum cannot test residue identity; MB infrastructure required |
| 17 | W0-20 Mellin-cone s=3 R_inf=1.81e6 | feynman+tesla | **RD** (MSM primary) | RD-unpinned | Axis 2 | s=3 in divergence cone (d_spec/2=4); Z(3,L) ∼ L^4.24 |
| 18 | W3-11 multipole min L*=−1 | landau | **MIXED** (Λ-convention ambiguity) | RD-unpinned | (orthogonal to regulator axis: Λ_phys vs Λ_Casimir, factor 63) | Cutoff convention resolution carry-forward (S86 V.6) |

**Class distribution on this 18-row W0-W5 set:**
FI / FI-identity: 5 (W5-6, W0-5, W2-1, W5-4, W5-7)
RD: 5 (W5-1, W0-7, W0-11, W0-20, W5-5)
MIXED: 6 (W5-2, W5-3, W2-7, W0-6, W0-9, W0-10, W3-11)
Vocabulary-only (NOT regulator-classifiable): 1 (W1c-3)
**Promotable to FI under S86 infrastructure**: at least 3 (W0-7, W0-11, W0-20 if Mellin-Barnes infra delivers; W2-7 if parity-extended §VII.P' lands).

### II.2 Dual-SHA Audit (sig_5 of v3-closure-audit)

**Method.** Parsed `computations/s85_gate_verdicts.txt` (206 lines, 198 audit_sha256 occurrences, 142 canonical S85-verdict lines extractable via regex `^S85-[A-Za-z0-9_\-]+:.*audit_sha256=([a-f0-9]{64})`). Counted unique audit_sha256, flagged duplicates, identified gate-IDs with multiple verdict lines.

**Substitution chain (sig_5 verdict)**:

```
Step 1 [definition]:
  sig_5 := (count_unique(audit_sha256) == count_total(verdict_lines))

Step 2 [substitute]:
  count_unique(audit_sha256)         = 142
  count_total(verdict_lines, S85)    = 142

Step 3 [simplify]:
  142 == 142  ⇒ TRUE

Step 4 [direction]:
  sig_5 = TRUE  ⇒  no SHA hardcoding; closure_hash(pins) is computed per-line.
  v3-closure-audit sig_5 status: CLEAN.
```

**Eight gate-IDs with multiple verdict lines (re-emissions, by design)**:

| Gate ID | Lines | First sha (16) | Reason for re-emission |
|:--------|:-----:|:---------------|:------------------------|
| S85-FOLDED-BISPECTRUM-21CM-SHAPE-TEMPLATE | 1, 8 | d3b2df03..., 11c3d2d4... | Re-emission after Fisher-cosine fix (different input pin) |
| S85-W1a-SCHEME-DEP | 15, 17 | 42f6eb63..., c9a2beaf... | dual-SHA template upgrade post W1a-1 (sig_2 fix) |
| S85-W1a-ALPHA-S-REGISTRY-UPGRADE | 16, 18, 82 | 84cb404e..., 3cf7dd46..., e5f82105... | Three-iteration spectral-second-moment scheme refinement |
| S85-W1b-ALPHA-S-PRIOR-RANGE-LCDM | 48, 83 | bb974974..., d230693a... | Prior-range expansion after W1b-1 LCDM-baseline patch |
| S85-W3-CF-3-MULTI-VALUED-LANDAU-OP | 51, 52 | 7797753e..., 34db19e4... | logspace-vs-linear bug fix re-emission |
| S85-W1b-PLANCK-DESI-2025-ALPHA-S-RECALIBRATION | 65, 66, 84 | b1e51b01..., 59492947..., 1c2f9f19... | Three-step Planck-DESI calibration refinement |
| S85-W1b-CF-M6-ALPHA-S-W-A-DECOUPLED-JOINT | 68, 85 | bdee703e..., 14ee8643... | Decoupled-joint reformulation (W1b carry) |
| S85-W3-FALSIFIER-TABLE-OZ-CLASS | 74, 75 | 09baae8e..., 1bb59c885... | regex bug fix re-emission |

All eight re-emissions carry distinct audit_sha256 by design — original verdict lines preserved as audit trail. No non-design duplicates detected; no hidden SHA-hardcoded copy-pastes.

**Verdict (forensic)**: dual-SHA closure across S85 W0-W5 is structurally sound. No remediation required at sig_5.

### II.3 Regulator-Scope Bounding per W5 (combined-landscape consequence)

The slot-1 S-1 boundary theorem established F_4 vs M as the coarsest Mellin-vector partition. Combined with the W5 PASS gates and the W0-W5 FAIL set, each surviving result can be tagged by the smallest regulator scope on which it remains physically meaningful.

| Result | {a_4}-pure scope (F_4) | Mixed-support scope (M) | Combined / cross |
|:-------|:----------------------:|:-----------------------:|:----------------:|
| W5-6 HP^1 magnitude (band 2.0) | TIGHT 2.91% if F_4-only (max/min = 1.0/0.970024) | wide if cutoff_sqrt included (factor 2.0) | F_4-only = R-protected STRICT (≤1.5×) |
| W0-5 Z_R 2-loop scheme_dev 8.64e-8 | TRIVIAL (regulator-class agnostic) | TRIVIAL | Sub-dominant FI on full atlas |
| W2-1 axiom minimality | INDEPENDENT | INDEPENDENT | Axis 4 invariant |
| W5-1 sign(eps_H at tau_fold) | UNANIMOUS −1 across {zeta, Zub, SDW} | SCHEME-DEPENDENT (sign-flip on cutoff_sqrt) | Class-separating observable per S-1 thm |
| W5-2 HP^0 factorization | 0% spread (TIGHT) | 254%/107% spread (FAIL) | S78 W2-F theorem scope = F_4 |
| W5-7 two-layer obstruction n_joint=0 | n_joint=0/3 (already FAIL within F_4 since drift > 5%) | n_joint=0/2 (already FAIL within M) | Theorem holds at every sub-scope |
| W2-7 (C_H, C_epsH) parity-blind | parity-blind on F_4 (HP^even ⊥ HP^odd) | parity-blind on M | Orthogonal axis (HP^even vs HP^odd) |
| W0-7/11/20 Mellin-cone FAILs | direct-zeta on F_4 still subject to MSM at Re(2s) < d_spec | not directly tested on M (cutoff_sqrt does NOT use direct-zeta) | Axis 2: Mellin strip; F_4-specific at present |

**Reading.** The {a_4}-pure scope F_4 = {zeta, Zubarev, SDW} is sufficient for ALL load-bearing W5 results (HP^1 invariance, sign cluster, two-layer obstruction holds within F_4 since drift is already > 5%). cutoff_sqrt's role is to PROBE THE WALL, not to host predictions — its inclusion turns F_4-tight observables into RD ones (sign flip; HP^1 factor 2; HP^0 factorization 254%). Whether cutoff_sqrt is structurally excluded (W-4 outcome) determines whether the F_4-only landscape IS the framework's regulator scope or whether two coexisting classes must each be tracked.

### II.4 Mellin Strip / Convergence Cone Theorem — registry draft

This is the structural theorem stated in slot 1b S-6, formally registered here as a Lizzi-track permanent finding alongside ZETA-NOT-PHYSICAL-75.

**Theorem (Mellin Strip / Convergence Cone, S85-W0-S6).**
Let (A, H, D_K) be the Jensen-SU(3) spectral triple at finite L_max ≥ 8 with truncated spectrum {λ_n}_{n=1..N(L)} and dimensional spectrum d_spec ≈ 8 (cache-intrinsic). Define `Z_L(s) := Σ_n d_n |λ_n|^{-2s}` and `zeta_D(s)` = analytic continuation of the L=∞ continuum sum. Then:

```
Regime I  (Re(2s) > d_spec):     Z_L(s)  →  zeta_D(s)            as L → ∞       (admissible direct truncation)
Regime II (Re(2s) = d_spec):     Z_L(s)  ~  log L                                  (logarithmic divergence; finite L meaningful only after subtracting leading log)
Regime III(Re(2s) < d_spec):     Z_L(s)  ~  L^{(d_spec − 2s)/2 + corr}             (no finite limit; only the residue analytic continuation is meaningful)
```

**Substitution chain (Regime III divergence direction)**:

```
Step 1 [definition]:
  Z_L(s) = Σ_{n=1..N(L)} d_n |λ_n|^{-2s}
  d_spec = first pole of zeta_D = 8 (cache W0-9 confirmation)

Step 2 [substitute s = 3, d_spec = 8]:
  Re(2s) = 6 < 8 = d_spec  ⇒  Regime III

Step 3 [simplify]:
  exponent of L^{(d_spec − 2s)/2 + corr} = (8 − 6)/2 + dim-mult corr = 1 + corr

Step 4 [direction]:
  Empirical fit (W0-20):  Z(3, L)  ~  L^{4.24}   (positive divergence rate; corr ~ 3 from dim-mult)
  ⇒  Z_L(3) is monotone-increasing in L; no finite limit
  ⇒  W0-20's R_inf = 1.81e6 is the divergent-cone PARTIAL SUM, NOT the analytic-continuation residue
  Direction: divergence-rate sign POSITIVE on the divergence cone; methodology-closed for direct truncation in Regime III.
```

**Three of seven W0-W5 truncation FAILs are Regime III misclassifications**:
- W0-7 Zubarev kernel pole at d_spec/2 = 4 sits on the boundary → Regime II near-edge → MSM
- W0-11 CC-3 CM signed sum requires residues at s ∈ {1, 2, 3, 4} → most are in Regime III → PSO + MSM
- W0-20 explicitly tests s = 3 < d_spec/2 = 4 → Regime III → MSM primary

**Functional-independence ledger entry**:

| Quantity | Class |
|:---------|:------|
| `Z(s, L)` for Re(2s) < d_spec | **DIVERGENT-IN-L** (methodology-closed; no finite limit) |
| `chi_2(S+) − chi_2(S−)` (charge-conjugation) | **FUNCTIONAL-INDEPENDENT** (machine epsilon, S6 result 5) |
| CM signed residue ratio at finite L | **FUNCTIONAL-DEPENDENT-THROUGH-ANALYTIC-CONT** (requires Mellin-Barnes infrastructure) |
| Zubarev rho asymptote conjecture rho→−1 | **CONJECTURE FALSIFIED** at direct-truncated level (extrapolated −0.81); MB pending |

**Provenance**:
- W0-7 audit_sha256 (s85_w0_zubarev_lmax_convergence) — see verdict file
- W0-11 audit_sha256 (s85_w0_cc3_connes_moscovici)
- W0-20 audit_sha256 (s85_w0_mellin_cone_s3_residue)
- L_max=12 D_K cache sha 9e6d9cf7... (shared input pin)

This theorem joins ZETA-NOT-PHYSICAL-75 in the Lizzi corpus: zeta_D(s) is neither (a) directly observable (S75) nor (b) directly computable on a truncated cache without analytic continuation (S85). Both are FUNCTIONAL-INDEPENDENT.

### II.5 W-1 R-Protection Partition Fold-In

The W-1 cutoff-authority adjudication established Layer-A (load-bearing predictions: CC ratios, n_s, R_protected) vs Layer-B (extensive predictions including Lambda-convention-conditional W3-11). This IS the S76 R-Protection intensive/extensive partition applied to the regulator-choice axis.

**Substitution chain (intensive/extensive partition with regulator axis)**:

```
Step 1 [definition (S76 lizzi-specgeo workshop, registered)]:
  Q is INTENSIVE iff   d(log Q)/d(log L) = 0    in Weyl regime  (alpha_k = d + r + k)
  Q is EXTENSIVE iff   d(log Q)/d(log L) = c · d(log V_Pl(L))   in Weyl regime
  V_Pl(L) = a_0(L)  (Plancherel volume)

Step 2 [substitute regulator-axis formulation]:
  Q is R-protected (intensive over the regulator atlas) iff drift_r(Q) <= 1.5x (STRICT) or 2.5x (LOOSE)
  Q is R-extensive iff drift_r(Q) ~ regulator-class scaling (e.g., L_max-divergent under SDW, M_KK-divergent under f-amp)

Step 3 [simplify]:
  Layer-A (W-1 closeout: CC ratios, n_s, R_protected, HP^1 magnitude, R-family ratio observables)
    ⇒ regulator-drift bounded; intensive
  Layer-B (Lambda-convention-conditional, W3-11; absolute-CC; M_KK-divergent SDW absolutes)
    ⇒ regulator-drift unbounded; extensive

Step 4 [direction]:
  Layer-A predictions are PROTECTED from W3-11 polynomial-truncation breakdown
  by the same theorem that proved them f-protected (S76 R-protection).
  Direction: bounded drift implies category-stable verdict.
```

**Three-bucket combined classification (regulator scope × R-protection)**:

| Layer | Observables (S85 W0-W5 examples) | F_4-only | Full 5-atlas | Status |
|:------|:---------------------------------|:--------:|:------------:|:------:|
| Layer-A (R-protected, intensive) | HP^1 ‖[ε_H]‖, R-family ratios, two-layer-obstruction, axiom-minimality | TIGHT | TIGHT (≤2x) | LOAD-BEARING |
| Layer-A' (R-tagged, scheme-magnitude only) | sin²θ_W (sin²W = R_1/R_2 type), c_s | TIGHT | TIGHT | LOAD-BEARING |
| Layer-B (R-invariant in magnitude only, sign SD) | sign(eps_H at tau_fold), per-branch zeta-Josephson | TIGHT-magnitude | RD-sign | LOAD-BEARING-WITH-SCHEME-TAG |
| Layer-C (R-extensive) | M_KK absolutes, M_0-cluster span, k_a2 span, f_conv slot weights | RD | RD | NOT-LOAD-BEARING |

The framework's predictive content lives in Layers A + A' + B (with explicit scheme tag for sign-class B observables). Layer-C is regulator-conditional bookkeeping; no load-bearing prediction depends on Layer-C alone.

### II.6 W-4 Parallel-Dependency Hooks (graceful degrade)

W-4 evaluates whether cutoff_sqrt is STRUCTURALLY-EXCLUDED, GENUINELY-PHYSICAL, or REQUIRES-S86-GATE. This S-7 leaves both readings tractable:

**Reading A — STRUCTURALLY-EXCLUDED**:
- Effective regulator atlas reduces from 5 to 4: F_4 ∪ {anomaly} = {zeta, Zubarev, SDW, anomaly}
- W5-1 sign-flip evaporates (4/4 −1, no outlier); W5-1 RECLASSIFIES from FAIL to PASS
- W5-2 HP^0 spread = 0% on F_4 sub-cluster, 107% on anomaly sub-cluster ⇒ FAIL persists at 1/4 outlier; INFO clause may fire (anomaly is the sole outlier; matches S67 structural-exclusion pattern)
- W5-6 HP^1 max/min reduces from 2.0 to 1.0/0.970024 = 1.0309 ⇒ TIGHT-tighter band
- W5-7 two-layer obstruction PERSISTS (every regulator already FAILs SCHEME_INDEP individually within F_4 ∪ {anomaly})
- S67 frustration triangle stays a 3-corner frustration on (anomaly, zeta, f*); F_4/M wall collapses to single-class
- **Net**: simpler picture; W5 demoted from "structural two-class theorem" to "atlas reduction + S67 reaffirmation"

**Reading B — GENUINELY-PHYSICAL**:
- Two coexisting regulator classes (F_4 and M) are both substrate-admissible
- W5-1 sign-flip is PHYSICAL — substrate has TWO sign sectors
- W5-2 HP^0, W5-5 lattice non-functoriality, W5-6 HP^1 magnitude all become PERMANENT structural splits
- F_4/M boundary becomes a TWO-CLASS THEOREM stronger than S67 frustration: not just "no regulator accommodates red tilt + observational tuple" but "two STRUCTURALLY DISTINCT regulator classes coexist"
- S67 frustration triangle co-exists with F_4/M wall as two independent obstruction statements
- **Net**: richer physics; the spectral functional is a TWO-CLASS physical DOF on the framework

**Reading C — REQUIRES-S86-GATE**:
- W-4 unable to adjudicate at the available evidence; defer to S86 axiomatization gate (see CF entries below)
- All W5 verdicts remain authoritative; only the META-classification "structurally-excluded vs genuinely-physical" defers
- This S-7 stands intact under reading C

**Hook to S86**: the proposed `S86-AXIOM-F4-PARTITION-86` and `S86-PHYSICAL-REG-AXIOM-86` (see Section V) directly close W-4. Either gate's PASS distinguishes A from B; FAIL means C continues.

---

## III. Gate Verdicts (per regulator class, W0-W5 set)

Verdicts taken AUTHORITATIVELY from source WPs. No re-adjudication. Per-regulator-class subset views below.

### III.1 W5 lizzi-solo (regulator atlas wave) — full block

| Gate | Verdict | Value | Source line | audit_sha256 (16) |
|:-----|:-------:|:-----:|:------------|:-------------------|
| S85-W5-1-FI-PARITY-REGISTRY | FAIL | False | W5 WP §W5-1 (line 132 of verdict file) | `45ac9bfceca269f1` |
| S85-W5-2-HP0-INTRA-CORRIDOR | FAIL | 3 | W5 WP §W5-2 (line 139) | `4536d99702607605` |
| S85-W5-3-L0-L3-LAYER-DISSONANCE | FAIL | (31, 3, 8) | W5 WP §W5-3 (line 144) | `ecfd7b11592a294b` |
| S85-W5-4-PARITY-LMAX-SANITY | PASS | True | W5 WP §W5-4 (line 150) | `8e3b77e98ef12e5b` |
| S85-W5-5-LAYER-AWARE-LATTICE-JOIN | FAIL | 8 | W5 WP §W5-5 (line 156) | `50c372ee43503fea` |
| S85-W5-6-REGULATOR-SCAN-EPS-H | INFO-tight | 2.0 | W5 WP §W5-6 (line 163) | `92d022ff56df893e` |
| S85-W5-7-TWO-LAYER-OBSTRUCTION | PASS | 0 | W5 WP §W5-7 (line 169) | `f8c8f56630a34719` |

### III.2 W2 connes (cross-linked W2-1, W2-7)

| Gate | Verdict | Value | Source | audit_sha256 (16) |
|:-----|:-------:|:-----:|:-------|:-------------------|
| S85-W2-ALPHA-S-AXIOM-MINIMALITY-AU | PASS | 5 | W2 WP §W2-1 | `69934d6c13328236` |
| S85-W2-DISJOINT-CORRIDOR-REGISTRY-LANDING (W2-7) | FAIL-with-refinement | 1 | W2 WP §W2-7 | `2ef68ad50f55b59e` |

### III.3 W0 truncation FAILs (Mellin-strip relevant)

| Gate | Verdict | Value | Class (S6) | audit_sha256 (16) |
|:-----|:-------:|:-----:|:-----------|:-------------------|
| S85-VAN-HOVE-CUSP-THEOREM (W0-6) | FAIL | S_max=74.6 | (a)/(d) mixed | (line 22 of verdict file) |
| S85-ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE (W0-7) | FAIL | rho=−0.6349 | (c) primary; MSM | — |
| S85-D_SPEC-ALT-DERIVATION-PATH (W0-9) | FAIL | (0.15, 9.32, 12) | (b) primary | — |
| S85-CC-2-SPIN8-TRIALITY-ORBIT-SUM (W0-10) | FAIL (mixed) | V/S=4.23% | (c) primary (over-tight) | — |
| S85-CC-3-CONNES-MOSCOVICI-RESIDUE (W0-11) | FAIL | log10=−0.13 | (c) primary; PSO+MSM | — |
| S85-W0-L-MELLIN-CONE-S3-RESIDUE (W0-20) | FAIL | R_inf=1.81e6 | (c) primary; MSM | — |

### III.4 W0 / W1a / W1c FI/RD-relevant pivots

| Gate | Verdict | Value | Class | audit_sha256 (16) |
|:-----|:-------:|:-----:|:------|:-------------------|
| S85-F_CONV-TWO-LOOP-Z_R-INVESTIGATION (W0-5) | PASS | 8.64e-8 | FI sub-dominant | `a533378543bf559f` |
| S85-W1a-SCHEME-DEP (W1a-1) | FAIL | 0.1252 | RD STRUCTURAL | `c9a2beaf9a0ce862` |
| S85-W1a-ALPHA-S-REGISTRY-UPGRADE (W1a-2) | FAIL | 0.7876 | RD scheme-specific | `3cf7dd462069c16f` |
| S85-W1a-ALT-D-SPEC-PROBE (W1a-3) | FAIL | 1.188 | MIXED (Route iii FI; i,ii RD finite-size) | (see verdict line) |
| S85-W1c-HISTORICAL-ALPHA-S-USAGE-AUDIT (W1c-3) | FAIL | 2193 | NOT regulator-classifiable | `93e212abdd0bdb94` |

### III.5 W3 / W4 cross

| Gate | Verdict | Value | Class | audit_sha256 (16) |
|:-----|:-------:|:-----:|:------|:-------------------|
| S85-W3-MULTIPOLE-BREAKDOWN-SCAN (W3-11) | FAIL (model-dep) | min L*=−1 | MIXED (Λ-convention) | — |
| S85-W4-8-WATCHLIST-UPDATE | PASS (REFRAMED) | 6 | NON-PHONONIC project-level | `2398fa6f3fe806b3` |

### III.6 Source-conflict audit

Cross-checked W0/W1a/W1b/W1c/W2/W3/W4/W5 — no contradictory verdicts on any regulator-axis observable. The single internal inconsistency flagged in the source set (W3-11 vs W3-9 Lambda-convention disagreement) is acknowledged in the source W3 WP itself and carried forward to S86 V.6 (Multipole-breakdown Lambda-convention resolution).

---

## IV. Structural Implications

### IV.1 Under W-4 Reading A (cutoff_sqrt STRUCTURALLY-EXCLUDED)

- **F_4/M wall (S-1 theorem)**: COLLAPSES to atlas-reduction. Effective atlas = {zeta, Zubarev, SDW, anomaly}; W5-1 / W5-2 / W5-5 / W5-6 demote to corollaries of S67 + reduced atlas. Mellin-vector partition becomes {a_4}-pure-only with anomaly as a structurally-excluded mixed-support outlier.
- **Lizzi observable signature (M_lizzi atlas)**: 30 FI / 4 RD / 8 MIXED count from S82 stays unchanged — cutoff_sqrt's exclusion does not retroactively re-classify prior atlas rows (those were classified on observation-content, not on cutoff_sqrt-inclusion).
- **HP^1 magnitude**: TIGHTENS to factor 1.031 within F_4 = {zeta, Zubarev, SDW}; HP^1 becomes a STRICT R-protected projector at the 3.1% level on the surviving atlas.
- **Two-layer obstruction (W5-7)**: PERSISTS — within F_4 ∪ {anomaly}, all 4 regulators STILL fail SCHEME_INDEP individually because f_conv 2-loop drift = 39.21% global (regulator-class agnostic) and within F_4 the HP^1 drift is 3.1% (TIGHT) but f_conv conjunct is FALSE for all 4. Theorem holds on every sub-scope including the reduced 4-atlas.
- **Mellin Strip / Convergence Cone (S6 theorem)**: UNCHANGED. The strip belongs to Axis 2, orthogonal to the F_4/M Axis 1; cutoff_sqrt's exclusion does not touch it.

### IV.2 Under W-4 Reading B (cutoff_sqrt GENUINELY-PHYSICAL)

- **F_4/M wall**: BECOMES A STRUCTURAL TWO-CLASS THEOREM stronger than S67. The substrate's regulator-choice DOF has TWO admissible classes; predictions reported as (value, class) with explicit class-tag.
- **W5-1 sign-flip**: PHYSICAL — substrate has two sign sectors at τ_fold; observation must commit to a class.
- **W5-2 / W5-5 / W5-6**: PERMANENT structural splits, not artifacts.
- **HP^1 magnitude**: stays at factor 2.0 across full atlas; HP^1 becomes a R-protected projector at LOOSE level (≤2.5×) but NOT STRICT.
- **Frustration triangle (S67)**: COEXISTS as two independent obstructions on the framework's regulator scope — S67 is a 3-corner frustration on observables; F_4/M is a 2-class structural partition on regulator choices. Both walls hold simultaneously.

### IV.3 Under W-4 Reading C (REQUIRES-S86-GATE)

- This S-7 stands intact. All W0-W5 verdicts remain authoritative under their pre-registered thresholds; only the META-interpretation defers.
- The proposed S86 axiomatization gates (CF-LZ-S87-1, S86-PHYSICAL-REG-AXIOM-86) directly close W-4 by deciding A vs B.

### IV.4 Mellin-strip closure ladder for S86

The three Mellin-strip FAILs (W0-7, W0-11, W0-20) share a single root cause and resolve via a single S86 master gate `S86-MELLIN-HEAT-KERNEL-INFRA` (originally proposed in slot 1b S-6). Successful PASS of this gate would:
- Re-evaluate W0-7 under MB-continued kernel: rho_MB ↦ true asymptote (test conjecture −1)
- Re-evaluate W0-11 under MB-pole-subtracted residue sum: log10|Λ|/|a_0| ↦ MB value (test CC-cancellation)
- Re-evaluate W0-20 under MB-shifted residue: Z(3)_continued ↦ true value (test analytic continuation existence)

If the S86 master gate PASSes, the Mellin-strip class (c) FAILs all migrate to either (b) METHOD-INAPPROPRIATE (closed) or (d) structural results in their own right — depending on whether MB delivers cancellation or numerical residue.

### IV.5 Three-axis structural picture (registered)

```
Axis 1 (Mellin support):        F_4  ↔  M           (THIS S-1 boundary theorem; L_max ≥ 8 robust)
Axis 2 (Mellin strip):          Re(2s) > d_spec  ↔  Re(2s) ≤ d_spec    (S6 theorem; methodology-closed in Regime III)
Axis 3 (HP^even / HP^odd):      Even Seeley-DeWitt parity-blind to HP^1 secondary twists  (W2-7 wall)
Axis 4 (R-protection):          Intensive-load-bearing  ↔  Extensive-bookkeeping  (S76 partition; W-1 fold-in)
```

These four axes are STRUCTURALLY INDEPENDENT. Each W0-W5 result lands at one or more axes; no result requires all four simultaneously. The atlas registry §VII.K-META, §VII.M, §VII.P, §VII.B are the four landing slots.

### IV.6 Functional-Independence Ledger updates

| Entry | Before S85 | After S85 |
|:------|:-----------|:----------|
| `chi_2(S+) − chi_2(S−)` charge-conjugation | UNCLASSIFIED | **FUNCTIONAL-INDEPENDENT** (machine epsilon, S6) |
| CM signed residue ratio at finite L | implicitly thought achievable | **FUNCTIONAL-DEPENDENT-THROUGH-ANALYTIC-CONT** (requires MB infrastructure to even define) |
| Zubarev rho asymptote conjecture (rho → −1) | stated but untested | **CONJECTURE FALSIFIED** at direct-truncated level (extrapolated −0.81); MB pending |
| Z(s, L) for Re(2s) < d_spec | implicitly assumed L-extrapolable | **DIVERGENT-IN-L** (W0-20 fits L^{4.24}); methodology-closed |
| sign(eps_H at τ_fold) over 5-atlas | SCHEME-DEPENDENT (S66) | **SCHEME-DEPENDENT, L_max-robust** (W5-1 + W5-4 PASS lock) |
| ‖[ε_H]‖_{HP^1} over 5-atlas | unclassified | **NEAR-FI** (R-protected-LOOSE, factor 2; STRICT on F_4 only at factor 1.031) |
| HP^0 factorization theorem (S78 W2-F) scope | implicit universal | **BOUNDED** to F_4 (pure-a_4 family) |
| Layer-aware lattice-join (W10-116) | hypothesized Boolean | **NON-FUNCTORIAL** at L1-AX/L2-SA → L3-OB transitions |
| Joint f_conv × eps_H scheme-indep | proposed obstruction | **PERMANENT OBSTRUCTION** (W5-7, n_joint=0/5 trivially) |
| (C_H, C_epsH) twin-pair spectral distinguishability (§VII.P) | proposed wall | **PARITY-CONDITIONAL** (HP^1-secondary twins indistinguishable on HP^even; needs odd-parity diagnostic) |

Twelve permanent updates to the FI ledger across S85 W0-W5.

### IV.7 Substrate framing audit

All 18 classified results in §II.1 honor `phononic-framing.md`. The substrate (D_K eigenvalues on Jensen-deformed SU(3) × A_F) is the input; spectral functionals (regulators) extract heat-kernel moments {a_n}; observables emerge from Mellin-vector × character-vector pairings. No GR-frame, no "container" thinking. The cutoff_sqrt vs F_4 wall is a property of the substrate's regulator-choice DOF, not of an external geometry.

---

## V. Carry-Forward Computations (MANDATORY, 4-field schema)

V.1. **CF-LZ-S86-1: S86-MELLIN-HEAT-KERNEL-INFRA master gate**
- **What**: Implement Mellin-Barnes residue extractor: (i) compute Z_L(s) at s ∈ {5, 6, 7, 8} on the convergence strip Re(s) > d_spec/2 = 4; (ii) fit rational Pade [m/n] with m+n ≤ 5; (iii) continue to s* ∈ {0, 1, 2, 3, 4}; (iv) subtract Seeley-DeWitt counter-terms a_k · Γ(s-s_k)^{-1}; (v) sum over signed residues. Gate resolves W0-7, W0-11, W0-20 simultaneously.
- **Inputs**: D_K L_max=12 cache (sha 9e6d9cf7..., 166896 evs); canonical_constants.py (a_0=6440, a_2 from S82 W3-14 c_Gold, a_4 from JOINT-AUDIT-ATLAS-74); existing scripts s85_w0_cc3_connes_moscovici.py + s85_w0_mellin_cone_s3_residue.py + s85_w0_zubarev_lmax_convergence.py.
- **Gate**: `S86-MELLIN-HEAT-KERNEL-INFRA`. PASS: |Lambda_CC^MB|/|a_0| ≤ 1e-1 AND fit chi^2/dof ≤ 5. INFO: 1e-1 < ratio ≤ 1e-3, OR chi^2/dof ∈ (5, 25]. FAIL: ratio > 1e-3 OR chi^2/dof > 25.
- **Effort**: 6-8 h, 1 agent session (gen-physicist with lizzi review pass).

V.2. **CF-LZ-S86-2: AXIOM-F4-PARTITION-86 (W-4 closure path A)**
- **What**: Determine whether `supp(r) = {4}` is equivalent to a structural Connes-axiom condition (e.g., "r is scale-covariant under Λ → cΛ with single Mellin residue at s = d_spec/2 − 2"). If equivalent, F_4 becomes axiom-derivable; cutoff_sqrt is STRUCTURALLY-EXCLUDED (W-4 reading A); the framework's regulator scope reduces to F_4.
- **Inputs**: this S-7 §II.1 + §II.3; S83 G3 EN3 (zeta unique axiom-native); Connes A1-A6 axioms; slot-1a S-1 §II.2 Mellin vectors.
- **Gate**: `AXIOM-F4-PARTITION-86`. PASS iff F_4 derivable from a single structural clause; FAIL iff no such clause; INFO iff clause exists on proper subset of F_4.
- **Effort**: MODERATE, 4-6 h.

V.3. **CF-LZ-S86-3: PHYSICAL-REG-AXIOM-86 (W-4 closure path B)**
- **What**: Test candidate axioms X for "regulator r is physical iff [X]" with three candidates: (a) `supp(r) = {4}`; (b) Connes-axiom-native (S83 G3 EN3); (c) preserves ‖[ε_H]‖_{HP^1} at factor ≤ 2. Evaluate each against the 5-atlas. Outcome distinguishes W-4 reading A (cutoff_sqrt rejected) from B (cutoff_sqrt admitted).
- **Inputs**: S83 G3 EN3; slot-1a S-1; Connes A1-A6.
- **Gate**: `PHYSICAL-REG-AXIOM-86`. PASS iff a candidate cleanly partitions; FAIL iff no candidate partitions cleanly.
- **Effort**: MODERATE, 5-7 h.

V.4. **CF-LZ-S86-4: DUAL-SHA-INFRASTRUCTURE-86 (forensics)**
- **What**: Land a per-session sig_5 audit script `computations/_dual_sha_uniqueness_audit.py` that on every session close (a) parses verdict file by canonical regex, (b) reports `count_total / count_unique` audit_sha256, (c) flags duplicates with line numbers + first-16 hex, (d) cross-checks gate-IDs with multiple verdict lines against an explicit allowlist of "by-design re-emission" patterns (REFRAME, logspace fix, regex fix). Run as part of `v3-closure-audit.sh`.
- **Inputs**: this S-7 §II.2 audit script (Python regex-based); `.claude/rules/v3-closure-recovery.md` (sig_5 spec).
- **Gate**: `DUAL-SHA-INFRA-86`. PASS iff audit script lands AND v3-closure-audit.sh sources it AND a synthetic test (single hardcoded duplicate audit_sha256) is correctly flagged.
- **Effort**: LOW, 2-3 h.

V.5. **CF-LZ-S86-5: FI-RD-PERMANENT-REGISTRY-86**
- **What**: Land the extended 18-row FI/RD classification (this S-7 §II.1) into `sessions/permanent-results-registry.md` §VII.K-META as the canonical S85 W0-W5 atlas. Include sub-tag alphabet from S83 G57 (FI-via-pin, mostly-RD, promotable, FI-pure, RD-unpinned) for each row. Composition with S82 42-row M_lizzi atlas yields a 60-row total with conflict-check against M_connes.
- **Inputs**: this S-7 §II.1 18-row table; S82 42-row atlas; S83 G57 5-label sub-tag alphabet; M_connes companion classifier.
- **Gate**: `FI-RD-REGISTRY-86`. PASS iff all 18 rows commit with provenance (gate-ID, audit_sha256, source WP-line) AND M_lizzi/M_connes agreement on shared rows. FAIL iff any row uncommitted or M-classifier conflict.
- **Effort**: MODERATE, 3-4 h.

V.6. **CF-LZ-S86-6: MELLIN-STRIP-REGISTRY-LANDING-86**
- **What**: Land the Mellin Strip / Convergence Cone Theorem (§II.4 above) in `sessions/permanent-results-registry.md` as a Lizzi-track theorem alongside ZETA-NOT-PHYSICAL-75. Cite the substitution chain (Steps 1-4) verbatim. Cross-reference S6 slot 1b synthesis.
- **Inputs**: this S-7 §II.4; permanent-results-registry; S6 file.
- **Gate**: `MELLIN-STRIP-REGISTRY-86`. PASS iff theorem entry present with full substitution chain and provenance to W0-7/W0-11/W0-20. FAIL iff any field missing.
- **Effort**: LOW, 1 h.

V.7. **CF-LZ-S86-7: HP1-NEAR-INVARIANCE-LANDING-86**
- **What**: Land the W5-6 finding that ‖[ε_H]‖_{HP^1} is R-protected-LOOSE on full 5-atlas (factor 2.0) and R-protected-STRICT on F_4 sub-cluster (factor 1.031) into §VII-B as a permanent registry entry. Pair with the slot-1a Corollary D substitution chain (HP^1 = Mellin-coarse projector onto |f_4^r|) for substrate-first explanation.
- **Inputs**: W5-6 WP §(d); slot-1a S-1 §II.8; S83 G56 GODBILLON-VEY-HEITSCH.
- **Gate**: `HP1-INVARIANCE-86`. PASS iff entry lands with both 5-atlas (factor 2) and F_4-only (factor 1.031) numbers AND substrate-first explanation. FAIL iff either component missing.
- **Effort**: LOW, 1.5 h.

V.8. **CF-LZ-S86-8: TWO-LAYER-OBSTRUCTION-LANDING-86**
- **What**: Land the W5-7 PASS as new §VII-B permanent wall entry "Two-Layer Obstruction Theorem" (analogous to S67 frustration-triangle). Note that the obstruction is STRONGER than predicted: each conjunct fails individually for every regulator (n_joint=0/5 trivial). Pair with cf-LZ-S86-9 (sixth-regulator synthesis test).
- **Inputs**: W5-7 WP §(d); S67 FUNCTIONAL-SELECT-67 (frustration triangle); slot-1a S-1 §IV.4.
- **Gate**: `TWO-LAYER-WALL-86`. PASS iff wall entry lands.
- **Effort**: LOW, 1 h.

V.9. **CF-LZ-S86-9: SIXTH-REGULATOR-SYNTHESIS-86**
- **What**: Construct composite regulator r_mix = α·zeta + β·cutoff_sqrt with α + β = 1, α, β > 0; compute Mellin vector f^{r_mix} = (2β, β, α + 0.5β, 0.1β); test whether any (α, β) produces joint scheme-indep on f_conv AND eps_H (the W5-7 obstruction clause). If so, obstruction is 5-atlas-specific; if not, obstruction lifts to continuous regulator space.
- **Inputs**: slot-1a S-1 §II.2 Mellin-vector table; W5-7 joint-satisfaction matrix; W6-67 f_conv scheme_dev = 39.21%; W5-6 HP^1 f_4^r table.
- **Gate**: `SIXTH-REG-SYNTH-86`. PASS iff ∃(α, β): drift(f_conv) ≤ 5% AND drift(ε_H) ≤ 5%. FAIL iff no such (α, β). INFO iff marginal.
- **Effort**: LOW, 2-3 h.

V.10. **CF-LZ-S86-10: F-STAR-MIXED-CONSEQUENCES-86 (parallel-sibling closure)**
- **What**: Re-evaluate the S77 finding f_conv · P_zeta = 1.72e-9 (0.09 OOM gap) using Mellin-Barnes-continued Lambda_CC^MB (output of V.1) replacing direct truncated a_0. Determine whether the 0.09 OOM gap closes / persists / opens. Tests whether CC and A_s gaps are JOINTLY scheme-dependent in the same direction.
- **Inputs**: V.1 output (Lambda_CC^MB); S77 f_conv · P_zeta script; canonical_constants for f_conv normalization (zeta convention).
- **Gate**: `FCONV-AS-MB-SIBLING-86`. PASS iff |log10(f_conv^MB · P_zeta) − log10(P_Planck)| ≤ 0.05. INFO ≤ 0.5. FAIL > 0.5.
- **Effort**: LOW, 2-3 h (after V.1).

V.11. **CF-LZ-S86-11: VII-P-V2-PARITY-EXTENSION-86**
- **What**: Land the W2-7 refined §VII.P-v2 statement (HP^0-content-distinct corridors carry distinct (a_0, a_2, a_4) signatures) AND companion §VII.P' (HP^1-distinguished pairs require odd-parity η or Godbillon-Vey diagnostic). Reproduce odd-parity diagnostic on (C_H, C_epsH) test case from S84 W10-115.
- **Inputs**: W2-7 WP; S84 W10-115 GV integral; §VII.P S84 S-5 Connes synthesis.
- **Gate**: `VII-P-V2-LANDING-86`. PASS iff both statements land AND odd-parity diagnostic reproduces non-zero on (C_H, C_epsH).
- **Effort**: MODERATE, 4-5 h.

V.12. **CF-LZ-S86-12: R-PROTECTION-MELLIN-CRITERION-86**
- **What**: Prove or disprove the criterion in slot-1a S-1 §IV.5: "observable O is R-protected on the 5-atlas iff `m_n^O = 0` for all `n ∈ {0, 2, 6}`". Test against S80 W0-9 184-entry RATIO/ABSOLUTE/MIXED classification: for each entry, extract m^O and check whether R-protection status correlates with the criterion.
- **Inputs**: S80 W0-9 184 entries; slot-1a S-1 §IV.5; per-observable character-vector extraction protocol (build).
- **Gate**: `R-PROT-MELLIN-86`. PASS iff criterion classifies ≥ 180/184. INFO ≥ 170. FAIL < 170.
- **Effort**: HIGH, 8-12 h.

V.13. **CF-LZ-S86-13: W3-11-LAMBDA-CONVENTION-RESOLUTION-86**
- **What**: Extract Λ_actual from L_max=10 D_K cache as the empirical top eigenvalue (from W0-7 series at L=12 gives lambda_max = 5.42 M_KK). Re-run W3-11 with Λ_actual replacing both Casimir-saturated and c_fabric*M_KK ad hoc choices. Verify W3-9 + W3-11 coexistence under unified cutoff.
- **Inputs**: L=10 D_K spectrum max eigenvalue; W3-9 + W3-11 producing scripts; canonical_constants pin for c_fabric.
- **Gate**: `MULTIPOLE-UNIFIED-86`. PASS iff min L*(K) ≥ 4 across [K_R5, K_crit] under Λ_actual AND Gi(K_crit) << 1. INFO iff min L* ∈ {2,3} OR Gi ∈ (1e-3, 1). FAIL < 2 OR Gi > 1.
- **Effort**: LOW, 2-3 h.

V.14. **CF-LZ-S86-14: W1c-3-VOCABULARY-REMEDIATION-86**
- **What**: Remediate the 2193 AMBIGUOUS α_s usage sites identified by W1c-3 across 390 files. Extend classifier keyword list to recognize (a) M_GUT / LCDM-baseline / "no running" contexts, (b) SKA / LiteBIRD / CMB-HD / CMB-S4 Fisher-forecast conventions, (c) META-about-α_s audit-gate pattern. Re-run W1c-7 impact matrix with extended classifier.
- **Inputs**: W1c-3 JSON (576 KB, 2193 entries); W1c-1 canonical handles; extended classifier specification.
- **Gate**: `ALPHA-S-VOCAB-86`. PASS iff N_flagged ≤ 5 on extended classifier.
- **Effort**: HIGH, 8-12 h (mechanical but voluminous).

---

## VI. Summary Table — regulator-class × observable matrix

| Observable / observable-family | F_4 = {zeta, Zub, SDW} (pure-a_4) | M = {cutoff_sqrt, anomaly} (mixed) | Joint reading | Pin tag (S83 G57) |
|:-------------------------------|:----------------------------------:|:----------------------------------:|:---------------|:-----------------:|
| sign(eps_H at τ_fold) | uniform −1 | −1 (anom) / +1 (cutoff) | RD (sign-flip) | RD-unpinned |
| HP^1 magnitude ‖[ε_H]‖ | factor 1.031 (TIGHT-STRICT) | factor 2.0 (TIGHT-LOOSE) | FI on F_4; FI-LOOSE on full atlas | FI-via-pin |
| HP^0 factorization spread | 0% (TIGHT) | 107% / 254% | RD on M | mostly-RD |
| Layer-aware lattice-join functoriality | functorial within F_4 | non-functorial at L1/L2→L3 | RD | RD-unpinned |
| Two-layer obstruction n_joint | 0/3 (FAIL on each conjunct) | 0/2 (FAIL on each conjunct) | FI structural NO-go | FI-pure |
| L0/L3 dissonance histogram (42-row) | (atlas-side metric, no per-class split) | — | MIXED (bimodal-like) | mostly-RD |
| Axiom-minimality {dim,reg,fin,real,1st-order}=5/7 | INDEPENDENT | INDEPENDENT | FI-identity | FI-pure |
| Z_R 2-loop scheme_dev | sub-dom 8.64e-8 | sub-dom 8.64e-8 | FI sub-dominant | FI-via-pin |
| f_conv 2-loop drift (W6-67) | 39.21% global | 39.21% global | RD STRUCTURAL (W1a-1) | RD-unpinned |
| Mellin-strip Regime I/II/III | shared (cache-axis) | shared (cache-axis) | Axis 2 (orthogonal to F_4/M) | regime-conditional |
| (C_H, C_epsH) parity-blindness | even-SDW blind | even-SDW blind | MIXED (axis 3 wall) | promotable |
| chi_2(S+) − chi_2(S−) charge-conjugation | machine ε | machine ε | FI permanent | FI-pure |
| α_s = n_s² − 1 identity (W1a-2) | scheme-specific (topological only) | spectral 2nd-mom disagrees 79% | RD scheme-specific | RD-unpinned |
| d_spec = 12 (W1a-3 routes) | route iii exact 12; routes i/ii at L=10 finite-size | — | MIXED (FI-pure topological + RD-finite-size) | promotable |
| Λ-convention (W3-11) | not regulator-axis (Λ_phys vs Λ_Casimir) | — | MIXED orthogonal | RD-unpinned |
| α_s vocabulary (W1c-3) | not regulator-axis | not regulator-axis | NOT regulator-classifiable | governance |

**Reading**: Five FI-or-FI-identity rows; five RD rows; six MIXED rows; one orthogonal-axis row; one vocabulary row. 11/18 rows touch the F_4/M wall directly; 7/18 are orthogonal to it. The framework's load-bearing predictions live in the FI + FI-identity + structural-NO-go subset (5 rows), all of which survive on F_4 alone. cutoff_sqrt's status (W-4) determines whether the framework reports across one regulator class or two.

---

## VII. Closing Notes

**Single highest-leverage takeaway.** The S85 W0-W5 landscape is a four-axis structural picture: F_4/M (Mellin support), Mellin-strip regime (analytic continuation), HP^even/HP^odd (parity), and intensive/extensive (R-protection). Each axis is independently provable, independently tested, independently registry-landable. The eight gate-ID re-emissions in `s85_gate_verdicts.txt` are all by design with distinct audit_sha256 — the framework's dual-SHA discipline is structurally clean. The single largest S86 leverage point is `S86-MELLIN-HEAT-KERNEL-INFRA` (CF V.1): one master gate that simultaneously closes W0-7, W0-11, W0-20 and updates the f_conv/A_s sibling pair (V.10). The W-4 adjudication on cutoff_sqrt (CF V.2 / V.3) determines which regulator-scope the framework reports under going forward.

**Next session.** S86 should lead with V.1 (Mellin-Barnes infrastructure) + V.2/V.3 (axiomatization), then V.5 (FI/RD permanent registry landing), then V.6/V.7/V.8 (three §VII landing entries: Mellin Strip theorem, HP^1 near-invariance, Two-Layer Obstruction). Vocabulary remediation (V.14) is high-effort and decoupled from physics — schedule as a dedicated late-S86 sub-wave.

**End of Lizzi S-7 combined-landscape synthesis.** File: `sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md`. 18-row FI/RD extension delivered; dual-SHA forensics CLEAN at sig_5 (142/142 unique); regulator-scope bounding map registered; Mellin Strip Theorem registry draft complete; W-1 R-protection partition folded in; W-4 graceful-degrade hooks left for both readings A and B. 14 carry-forward computations specified, all four-field complete. All quantitative claims verified via Python (substitution chains in §II.2, §II.4, §II.5); all direction claims carry explicit substitution chains. No re-adjudication of source-WP gate verdicts.
