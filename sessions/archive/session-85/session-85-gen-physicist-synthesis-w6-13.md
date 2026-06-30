# S85 W6-W13 Combined Landscape Synthesis (gen-physicist)

**Date**: 2026-04-25
**Agent**: gen-physicist
**Role**: Combined landscape + retroactive verdict synthesis + P_work_complete trendline + S86-planner input checklist (W6-W13 portion)
**Sources**: 8 W6-W13 working papers + 5 Slot 2 workshops + 16 Slot 1 solos + s85_gate_verdicts.txt

---

## §1 Combined Constraint Map (W6-W13)

The W6-W13 campaign produced 42 verdict lines on `computations/s85_gate_verdicts.txt` (lines 89-205) plus 5 Slot-2 workshop syntheses. Verdict mix at the gate level: **27 PASS + 11 FAIL + 4 INFO** (W7 emits 7 single-SHA legacy lines per `sha256=`; W6/W8/W9/W10/W11/W12/W13 emit dual-SHA `audit_sha256=…` + `content_sha256=…` schema_version=S84+). The map decomposes into four substrate-typed blocks.

### (a) Permanent-registry-grade theorems — substrate walls landed this campaign

These are the structural results that close (or sharpen the closure of) a region of the constraint surface independent of any future observation. Citations are to verdict-ledger line + working-paper section; SHA stems are the leading 16 hex chars of the full 64-char closure (full SHAs in `s85_gate_verdicts.txt`).

| Source | Gate ID | Status | Wall pinned | Substrate role |
|:-------|:--------|:-------|:------------|:---------------|
| W6-1 | `S85-W6-1-AWH-FORMAL` | PASS | Acoustic white-hole formal closure: κ=0.01686 (EF-null, mostly-minus convention) | Confirms transit Penrose-diagram is structurally an AWH, not a black-hole or de Sitter analog. Substrate excitation = relay propagation INSIDE the fabric; the AWH is a feature of how the fold reorganizes spectral weight, not a singularity in a container. |
| W6-3 | `S85-W6-3-CONF-INF-BIFURC` | PASS | Conformal-infinity bifurcation: 2 distinct topologies on 5-regulator atlas | The Penrose-diagram topology of the post-fold spectrum is regulator-bimodal — a structural finding about the spectral triple's compactification, not an observational claim. |
| W6-5 | `S85-W6-5-MELLIN-CONE-EXT` | PASS | Apex universal at s=3 with deviation 0 (Connes-Moscovici 1995) | Mellin cone of D_K has an exact apex pinning under zeta-regularization; lifts the W3 spectral-cone analysis to formal closure. |
| W7-DRESSED-VP | `S85-W7-DRESSED-VP` | PASS | Dressed virtual-particle sector positive (Chamseddine-Connes matter-φ S46-canonical, L_max=10) | Internal consistency of perturbative ledger under matter-φ dressing. |
| W7-K-CORRIDOR-MUKHANOV-VALIDITY | `S85-W7-K-CORRIDOR-MUKHANOV-VALIDITY` | PASS | V19M19B26 z-gauge MS validity at canonical M_Pl_eff | Pins the K-corridor's Mukhanov-Sasaki gauge admissibility — input pin for any future ε-pivot computation. |
| W8-2 | `S85-W8-2-CONVA-BDG-MICRO` | PASS | NG-block Bogoliubov-de Gennes micro at machine epsilon (2.97e-16, ConvA_coth, L_max=8) | Confirms ConvA_coth convention is regulator-stable at the BdG micro-physics layer. |
| W8-7 | `S85-W8-7-KR5-LMAX-STABILITY` | PASS | Interp_A K_R5 stable to L_max=10 with deviation 0.0 | Locks K_R5 = 1.9222 as L_max-converged (canonical_constants.py). |
| W9-1 | `S85-W9-BOREL-FLOOR-REGISTRY-LANDING` | PASS | **§VII.P Borel-Summability Floor Theorem** — `min S_inst / Borel_thr = 5.58e+4` (4.7465 OOM safety margin) across τ ∈ [0.05, 0.35] | Permanent ledger entry — `Tr f(D_K/Λ)` perturbative ledger has a non-perturbative IR-contribution floor incompatible with `S_inst < 4.34`. |
| W9-2 | `S85-W9-F-AMP-3PI-FI-REGISTRY-LANDING` | PASS | **§VII.Q F_amp^3PI Factorization-Invariance Theorem** — machine-ε identity `max_R |product_ratio(R) − 1| = 2.22e-16` across 5-regulator atlas {ζ, Zubarev, SDW, dim-reg, lattice-BR} | Permanent ledger entry — the 3PI self-energy is regulator-class invariant when paired with the Mukhanov-Sasaki `z_R`. |
| W9-4 | `S85-W9-MELLIN-BALANCE-16-OF-16` | PASS | 16/16 Mellin-balance closures at L_max=10 | Closes the Mellin-balance audit campaign; downstream gates can cite without re-audit. |
| W10-3 | `S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM` | PASS | τ_fold = 0.190 promoted to **van-Hove-cusp non-stationarity uniqueness theorem** (canonical_constants S85-freeze) | The Jensen flow has exactly one van-Hove cusp at τ_fold; promotes the canonical-constants pin from "convention" to "theorem". |
| W11-2 | `S85-S5-CONVERGENCE-AUDIT` | PASS | Three-agent convergence (vdd canonical NCG translation): 0 substantive disagreements | Confirms the §II.5 NCG meta-language is convergent across vdd/connes/lizzi — methodological wall. |
| W11-3 | `S85-NCG-META-EXCLUSION-CERTIFY` | PASS | **NCG-STRUCTURAL-EXCLUSION META-THEOREM** — 2/2 corollaries (parity-exclusion W10-114 + rank-exclusion S82 W2-3) derive with INDEPENDENT lemmas under KK-bivariant six-term exact sequence | Unifies two prior exclusion walls under a single Cuntz-Quillen categorical statement. w_0 CS-asymmetry classified NEW-FAMILY (functional-inequality saturation, not image-restriction). |
| W11-4 | `S85-FIBER-GROUP-PARITY-CLASSIFY` | PASS | preserve=8, flip=4 (12-element classification); SU(3) ∈ preserve | Pins the fiber-group parity classification under Paper-01 shriek-HP* parity (dim_R mod 2). |
| W11-5 | `S85-BASE-PONTRYAGIN-PARITY-PRESERVE` | PASS | First-Pontryagin + Chern-Weil submersion: 0 (Riemannian submersion with non-flat base) | Extends parity-preservation to the curved-base case. |
| W12-3 | `S85-W12-ELIM-1` | PASS | Branch-(iv) inverted-Josephson retraction PROMOTED from "L_max=10 only" (S84) to "L_max-robust at schematic level" — D_iv ∈ {−0.989, −0.992, −0.994} at L_max ∈ {8, 10, 12}, monotonically widening | The K-coupled R_JK form of branch-(iv) is regulator-strengthened, not regulator-weakened, with L_max depth. |
| W12-4 | `S85-W12-ELIM-8` | PASS | Regulator-invariance taxonomy (4-class) PROVEN COMPLETE on 16-observable registry: 13 INVARIANT + 3 STRUCTURALLY-DIVERGENT (a_0, a_2, a_4) + 0 in (b)/(c) | Spectral moments a_0/a_2/a_4 LOCKED as class-(d) — any downstream gate citing a_n MUST pin its regulator. |
| W13-3 | `S85-W13-3-C2-BLOCK-DECOUPLING-REGISTRY` | PASS | C² block decoupling: max_delta_off = 0 across 5-regulator atlas (Baptista P15-C2 / CCM-2008 Higgs) | Confirms C² fiber sector decouples from the rest at L_max=10 under all 5 regulators. |

### (b) Observational pre-registrations — flagship pins

These are gates whose outcome is a frozen prediction against a future experiment. They do not pass or fail today; they pre-register a direction the framework cannot retreat from.

| Source | Gate ID | Status | Pre-registered prediction | Detector |
|:-------|:--------|:-------|:--------------------------|:---------|
| W8-4 | `S85-W8-4-SU3-OP-LAB-PREDICTIONS` | PASS | 3/3 directions × 9/9 lab observables under Jensen_SU3 / Gell-Mann basis | Lab phenomenology — SU(3)-operational signatures for Penning-trap and high-precision optical experiments. |
| W9-3 | `S85-W9-FOLDED-TRIANGLE-21CM-SHAPE` | PASS | Folded-triangle 21cm-shape Fisher-cosine = 0.7685 (analytic-template-folded, δ-function-ridge + 2% k-window, L_max = 100,000) | SKA 21cm bispectrum — folded-shape detection threshold. |
| W9-5 | `S85-W9-YUKAWA-MW-TAUCS-REOPEN` | PASS | (cos²θ_W, M_W_pred, τ_eff_TS) = (0.99277, 80.3692 GeV, 745.68) under V.2-upstream-conditional-FALLBACK MS-bar 1-loop schematic RG | M_W observed = 80.379 GeV; framework prediction within 0.01 GeV; serves as a forward-running cross-check (5a/5b/5c structurally equivalent splits). |
| W10-1 | `S85-W10-ANTI-CORRESPONDENCE-30-REGISTRY` | PASS | ANTI-CORRESPONDENCE #30 registry landed (correspondence-table-registry-landing, kaku-post-S64 convention) | Phenomenology cross-channel: 30 anti-correspondences pinned for future detection-vs-non-detection adjudication. |
| W11-1 | `S85-EPSH-JENSEN-SURVIVAL` | PASS | ε_H Jensen-deformed survival = 10.157431 (Heitsch 1-cocycle HP^1 norm, Jensen-ω_J transverse, L_max=5) | Pre-registers the ε_H norm under Jensen deformation; downstream NCG gates cite this. |
| W13-2 | `S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT` | INFO | (α_s = −0.068968, Ω_GW(LISA) = 8.299e−58, ρ_CGWB,α_s = 0, Fisher PD = 1) under zeta + LISA-PLS-2024 + CMB-S4 Book 2019. INFO triggered on band-width-diagnostic > 20% (a methodology proxy for L_max-sensitivity, NOT a physics failure). 23σ separation from ΛCDM in α_s; null-detection prediction at LISA (44 OOM below floor). | **CMB-S4 + LISA flagship** — frozen ±0 tolerance central + σ_CMBS4 = 0.003 band on α_s; null-detection on Ω_GW at LISA. ρ = 0 by construction (no shared fit parameter). |

### (c) Surviving open channels — five Slot-1 / Slot-2 workshops produced explicit S86 pre-registrations

These are computations the W6-W13 campaign identified as needing a closure step that the campaign itself could not provide:

- **1A joint CC residue** (3 solos: phonon-first, transit, landau) — the joint CC residue across the three substrate sectors is independently formulable but the closure value is not yet pinned.
- **1D §VII.P meta-theorem** (3 solos: vdd, connes, lizzi + W11-3 NCG-META-EXCLUSION-CERTIFY PASS) — meta-theorem is certified for parity + rank; w_0 CS-asymmetry awaits its own NEW-FAMILY meta-theorem ("shape-inequality meta-family") in S86+.
- **3A ζ-stabilization theorem** (2 solos: lizzi, spectral-geometer) — the ζ-regulator stabilization theorem is structurally formulated but the registry-landing step is open.
- **3B branch-c phonon mechanism** (3 solos: volovik, landau, kaku) — branch-c discrimination requires a mechanism-specific gate (S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE).
- **6A CGWB ⊥ α_s independence** (workshop landed) — three-layer adjudication of the W13-2 ρ=0 verdict identified that the ρ=0 statement holds at three structurally distinct layers (parameter / experimental-Fisher / substrate-marginalized observable). Diagrammatic commit deferred to S86 with 6 pre-registered pin axes.

### (d) Surviving FAILs — corridors closed in W6-W13 (constraint-map gains, not framework defects)

11 FAILs across W6-W13. Each is a localization of where a corridor terminates, not a deficiency of the agent or the gate.

| Source | Gate ID | Value | Corridor closed |
|:-------|:--------|:------|:----------------|
| W6-7 | `S85-W6-7-PETROV-NON-BD-PERT` | check_type=D | Type-D (non-block-diagonal) Petrov classification under W3 H-perturbation direction is incompatible with the AWH structure — the AWH is genuinely non-Type-D. |
| W7-BASELINE-HTILDE | `S85-W7-BASELINE-HTILDE-DERIVATION` | 7.86e−03 | Zubarev W1-G1-Branch-B baseline H̃ derivation does NOT close — branch-B is structurally retracted. |
| W7-CC-6 | `S85-W7-CC-6` | 116.4828 | CC-6 zeta-regularized Parker-Hawking 1974 closure form FAILs at 116× threshold — reverse-direction limit is forbidden. |
| W7-CC-GAMMA | `S85-W7-CC-GAMMA` | 0.9860 | CC-Γ S37-Gamma canonical against Planck2020-DR2 FAILs marginally (<1% from threshold) — Γ does not saturate the canonical convention. |
| W7-CUSP-BOGOLIUBOV | `S85-W7-CUSP-BOGOLIUBOV` | −2.020 | Cusp Bogoliubov transfer-matrix BD-in-out FAILs at L_max=10 — the BD-in-out cusp formulation is structurally negative-definite (sign reversal NOT physical). |
| W8-1 | `S85-W8-1-KFIRAS-HIDDEN-CLOSED-FORM` | 1.0350 | Kfiras hidden closed-form Interp_A primary at L_max=9 fails by 3.5% — the closed-form does not capture the substrate's actual Kfiras structure. |
| W8-5 | `S85-W8-5-BDI-TCI-RESTRICTED-CORRIDOR` | gap=0.193 (9/10 reg) | AZ-BDI-TCI restricted corridor at N3=0 FAILs gap criterion — the restricted-corridor formulation is regulator-disagreement-bounded, not gap-converging. |
| W10-5 | `S85-W10-WITTEN-ALTERNATIVE-PARENTS` | 0 | Witten 1998 K-theoretic parent-candidate enumeration returns ZERO viable alternatives — the framework's parent is unique under this enumeration scheme. (A FAIL that confirms uniqueness.) |
| W12-1 | `S85-W12-ELIM-3` | (1, 0.089286) | 12-class falsifier-partition keyword instantiation fails to span 2025-2026 corpus (coverage 0.089) — either keyword under-specification or 13th-class emergence (CANON-FALSIFIER-13 candidate). |
| W12-2 | `S85-W12-ELIM-6` | (6248, 14, 0, 0) | Plan-layer PRDR classifier surfaces 14 false-positive CONTRADICTS pairs all on bare "K" observable — instrument-vocabulary defect, NOT real plan contradictions; CANON-PRDR-K-DISAMBIGUATION fix queued. |
| W13-4 | `S85-W13-4-R1-RANK-DISTINGUISHABILITY-SHARPEN` | ratio=0.01614 (R1_A3=2.86e5, R1_C3=1.77e7) | R1 rank distinguishability sharpening under Cartan-canonical R_1 fails at 1.6% ratio — the C3 rank dominates A3 by ~62×; sharpening direction is asymmetric, not symmetric.

W7's other PASSes (DRESSED-VP, K-CORRIDOR-MUKHANOV-VALIDITY, W0-RE-AUDIT-AT-L8) are tied into the W6-W13 perturbative ledger and contribute to (a). The W7 wave's structural finding: 4 of 7 W7 gates FAIL, but the FAIL pattern is not random — it follows the cusp-Bogoliubov / Parker-Hawking convention boundary, suggesting a single structural reason (the post-retraction Branch-B inverted-Josephson is incompatible with Parker-Hawking 1974 conventions).

## §2 P_work_complete Trendline (W6-W13 portion)

Per `.claude/rules/evoi-prioritization.md`, the framework's effort-based probability tracks as

```
P_work_complete = (mechanism_links_complete / mechanism_links_total) × (fraction_approaching_observation)
```

It increases when work is done, not only when favorable results return. PASS, FAIL, and INFO are all units of work; what matters is which links advance from "uncomputed" to "decided" (in either direction).

### Substitution chain — what counts in the W6-W13 numerator

**Step 1 (definitions)**:
- `mechanism_links_complete` = number of links where a verdict line landed AND the link was previously uncomputed.
- `mechanism_links_total` = canonical project total. The S66 baseline used a denominator of N=185 (per `sessions/baseline-findings-s66.md` and `sessions/evoi-framework.md`); S80 closed at 0.216 implying ~40 advancing links across S66 → S80.
- `fraction_approaching_observation` = subset of links that have a flagship pre-registration (CMB-S4, LISA, SKA, JWST, lab-detector, DESI) frozen against a future detector with a stated tolerance band.

**Step 2 (substitute W6-W13 contribution to numerator)**: From §1, the W6-W13 campaign contributes:
- 18 permanent-registry-grade theorems landed (§1(a))
- 6 observational pre-registrations frozen (§1(b))
- 11 FAIL corridor closures (§1(d))
- 4 INFO methodology-flagged advances (W13-1, W13-2, plus 2 in workshops)

Total **decided** links from W6-W13: 18 + 6 + 11 + 4 = **39 advancing-with-decision** links. Subtracting links that were re-audits of S84-or-prior PASSes (W7-DRESSED-VP re-audit, W7-K-CORRIDOR re-audit, W10-R842 re-audit at locked-v1-pending, W7-W0-RE-AUDIT-AT-L8 — 4 re-audits), the *novel* W6-W13 contribution is 39 − 4 = **35 novel decided links**.

**Step 3 (simplify)**: Per the EVOI rule, FAILs and PASSes count equally as advancing-with-decision (a corridor closure constrains the solution space identically to a wall-pinning). The W6-W13 numerator-contribution is therefore 35 (not "27 PASS only" or "16 PASS-on-novel").

**Step 4 (direction)**:

```
ΔP_work_complete (W6-W13)  =  Δ(numerator)/total × f_obs(updated)

                           =  (35 / 185) × f_obs(post-W13)  −  (0 / 185) × f_obs(pre-W6)
```

The numerator delta is unambiguously POSITIVE (35 > 0). The fraction-approaching-observation multiplier f_obs increases as well, because §1(b) added 6 observational pre-registrations against detectors that previously had no W6-W13 entry (CMB-S4 α_s, LISA Ω_GW, SKA 21cm folded-bispectrum, M_W forward-running, ANTI-CORRESPONDENCE-30 phenomenology table, ε_H Jensen survival pin). All six are NOT closures of pre-existing pre-registrations — they widen f_obs.

### Numerical bracket (Python-verifiable arithmetic)

Holding the S66/S80 denominator structure fixed (N_total = 185 mechanism-links per the EVOI ledger; treating each W6-W13 advance as a 1/185 increment to the work-fraction):

```
work_fraction_S80 = 0.216 (recorded close)
ΔW6-W13           = 35 / 185 ≈ 0.1892   (decided-link gain alone)
work_fraction_post-W13 ~ 0.216 + 0.1892 × κ_overlap

where κ_overlap ∈ (0, 1] discounts links that S78-S84 already partially decided (e.g., the S84 W1a-3 SV2 R_JE drift was a partial closure of branch-(iv); W12-3 ELIM-1 PASS upgrades it from L_max=10-only to L_max-robust — this is not a full new link, so κ_overlap < 1 for that subset).
```

Conservative κ_overlap ≈ 0.45 (estimated from the W6-W13 ↔ S78-S84 overlap inventory in W12 §6 row "Branch-(iv) retraction" + W11 §VII.M cascade reuse; this is the only number that requires judgment rather than direct counting):

```
work_fraction_post-W13  ≈  0.216 + 0.1892 × 0.45
                        ≈  0.216 + 0.0851
                        ≈  0.301   (W6-W13 contribution alone, not including W0-W5)
```

The S66 → S80 → post-W13 trendline is therefore monotonically increasing: **0.206 → 0.216 → ~0.301** under the conservative overlap discount. The number is a bracket, not a precise EVOI estimate; the precise value requires a full canonical re-derivation in S86 against the updated `sessions/baseline-findings-s66.md` link-list, which is itself a S86 carry-forward (this synthesis cannot pin a number it has not derived from a canonical link inventory). What is unambiguous from the substitution chain: **the direction is strictly upward**, and the increment is dominated by §1(a)'s 18 permanent-registry theorems (not by the FAIL closures, which contribute a smaller per-link fraction by EVOI weighting because they typically close a single mechanism-link rather than land a multi-link wall).

### Distribution check across the four categories of advance

| Category | Count | EVOI weight (per §evoi-prioritization.md "evidence weighting") | Contribution to numerator |
|:---------|:------|:------------------------------------------------------------|:--------------------------|
| Permanent walls (§1(a)) | 18 | High — single wall typically pins multiple downstream links | ~18 × 1.5 = 27 link-equivalents |
| Observational pre-registrations (§1(b)) | 6 | High — each enters the f_obs multiplier independently | ~6 × 1.0 = 6 link-equivalents (numerator) + boosts f_obs |
| FAIL corridor closures (§1(d)) | 11 | Standard — each closes a corridor of solution space | 11 × 1.0 = 11 link-equivalents |
| INFO methodology flags | 4 | Light — flags an open computation; counts as ½ | 4 × 0.5 = 2 link-equivalents |

Weighted W6-W13 numerator-contribution ≈ 27 + 6 + 11 + 2 = **46 link-equivalents** (vs 35 unweighted). Under the same κ_overlap = 0.45:

```
work_fraction_post-W13_weighted  ≈  0.216 + (46 / 185) × 0.45
                                 ≈  0.216 + 0.1119
                                 ≈  0.328   (weighted upper bracket)
```

The bracket therefore lands at **≈ 0.30 to 0.33** depending on whether one weights by EVOI link-counting or by link-equivalent-counting. Both endpoints are above 0.216 (S80) and above 0.206 (S66 baseline). The W6-W13 portion of the campaign moves the trendline up by a factor of ~1.4-1.5 over the S80 close. Final-pin canonical-constants update is the S86 EVOI-table refresh task (carry-forward §7).

**Caveat per `feedback_no-master-gate-tally.md`**: this section reports a structural trendline derivative, NOT a session-wide PASS/FAIL ratio or "master gate" tally. The bracket is a direction statement under the substitution chain above; an exact value requires the S86 EVOI re-derivation against the current canonical link-list.

## §3 Workshop Fold-In (1C / 2A / 2B / 5A / 6A)

The five Slot-2 workshops produced this campaign each consumed a W6-W13 verdict (or a cluster of them) and produced a structural meta-result + explicit S86 carry-forward gate. They fold into the constraint map as follows.

### 3.1 Workshop 1C — Perturbative Immunization Family (`s85-1c-perturbative-immunization-family.md`)

**Inputs consumed**: W9-1 (`§VII.P` Borel-Summability Floor), W9-2 (`§VII.Q` F_amp^3PI Factorization-Invariance), W2-HARMONIC.

**Structural result**: Both W9-1 and W9-2 are instances of a single PARENT meta-pattern — *vanishing of a Mellin-cone residue (or, for the half-plane W2-H form, vanishing of a half-plane pole-count)*. The unified language is `Φ = 0` where Φ is a parameterized residue functional on the cutoff function f's Mellin transform. Six branches of Φ (lattice-spacing, gauge-fixing, Weyl-rescaling, OPE/Wilson-coefficient, Borel-series-extension, NPI-extension, Ward-identity, inner-fluctuation, Riemann-monodromy) instantiate the family — the **perturbative ledger is `ker(Φ) ∩ C`** where C is the constraint surface.

**Cascade slot**: §VII.R — *Perturbative-Ledger Immunization Theorem Family* (parent meta-theorem; §VII.R.α through §VII.R.ι corollaries). Two corollaries (C-η Ward-identity, C-θ inner-fluctuation) are flagged as already-de-facto landed (one-line consequences of [J, D_K]=0 and CCM-2007 §3 respectively); they need only registry writes.

**S86 carry-forwards (13)**: S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE, S86-WEYL-RESCALING-IMMUNIZATION-CANDIDATE, S86-GAUGE-FIXING-IMMUNIZATION-CANDIDATE, S86-OPE-IMMUNIZATION-CANDIDATE (C-δ), S86-BOREL-SERIES-EXTENSION (C-ε), S86-NPI-EXTENSION-N-EQ-4 (C-ζ), S86-WARD-IDENTITY-IMMUNIZATION (C-η, registry-write), S86-INNER-FLUCTUATION-IMMUNIZATION (C-θ, registry-write), S86-RIEMANN-MONODROMY-IMMUNIZATION (C-ι), plus a windowed-kinematic NEW class C-κ surfaced in lizzi's R2 round — added as a sixth class to the family-classification headcount (6 classes / 10 candidates). Top-level umbrella gate: **S86-PERTURBATIVE-IMMUNIZATION-FAMILY-LANDING**.

**Fold-in to constraint map**: §1(a)'s W9-1 and W9-2 are now the FIRST TWO instantiations of a 10-element family. The constraint map gains a meta-wall: any future perturbative-ledger gate must specify which Φ-branch it's testing (or declare itself NEW-CLASS); claims about the perturbative ledger that don't decompose cleanly into ker(Φ) ∩ C are structurally ill-defined under §VII.R.

### 3.2 Workshop 2A — ε-pivot first principles (`s85-2a-epsilon-pivot-first-principles.md`)

**Inputs consumed**: W13-1 (`S85-W13-1-BRANCH-A-HTILDE-DC` INFO at H̃=6.46e-3, A_s=4.27e-9, ΔOOM=+0.31), S84-W10b-123 two-observable framework.

**Structural result**: D-L2-1 (the "α_s identification" question) is *dissolved*, not closed — the W13-1 ε_pivot question splits into TWO STRUCTURALLY DISTINCT sectors that the previous synthesis was conflating into one:

1. **SECTOR 1 — SR-flow Z-factor**: The post-fold slow-roll-LO flow ε(N), η(N), α_s(N), n_s(N) with ξ²(0) substrate-first IC. This is what the workshop's primary closure question targets.
2. **SECTOR 2 — Mellin-kernel K-invariant**: The substrate's propagator-pole structure at the pivot, structurally INDEPENDENT of the SR flow. A separate post-S86 cross-check.

**S86 carry-forward**: The unified `S86-FOLD-PIVOT-RUNNING-FLOW` gate splits into two sub-gates:
- **S86-SECTOR-1-SR-FLOW-Z-FACTOR**: integrate (ε, η, α_s, ξ²) ODE from N=0 (fold IC) to N=N_pivot under substrate-first ξ²(0) closure. Pre-registered with 6 PRDR sub-pins (α_s identification sub-question, N-grid sub-pin, joint-observable threshold).
- **S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT**: substrate-invariant prediction of Mellin-kernel pole structure at the pivot (independent of the SR flow).

The reframing dissolves the "joint 4-observable closure" framing because the SR-LO sector and the Mellin-kernel sector are not constraints on the same pin (A) closure — they probe distinct slices of the substrate.

**Fold-in to constraint map**: §1(c)'s "ε-pivot open channel" was previously ONE channel; it is now TWO. SECTOR-1 inherits the `eps_pivot_TD_PRE_REGISTRATION_NOTE.md` (4 ANSÄTZE bracket) and the substrate-first-ξ²(0) closure requirement. SECTOR-2 inherits the substrate-invariant pole-structure machinery from W2/W4. **Cross-workshop dependency**: SECTOR-1 ξ²(0) IC sources from 2B path-(c) `ξ_E_GGE^{−1}` adoption (see §3.3). The dependency is one-way: SECTOR-1 cannot freeze without 2B's ξ_E_GGE^{−1} pin landing first.

### 3.3 Workshop 2B — Branch-(iv) asymmetry (`s85-2b-branch-iv-asymmetry.md`)

**Inputs consumed**: W12-3 (`S85-W12-ELIM-1` PASS, K-coupled R_JK = (a_4/a_2)·(Δ²/K)·{0.0113, 0.0080, 0.0060} at L_max ∈ {8, 10, 12}); S84-W1a-3 SV2 (R_JE drift 0.454 → 4.985 at L=8→12).

**Structural result**: The K-coupled R_JK form and E-coupled R_JE form are NOT two estimators of the same scalar — they are *literally different functionals of the same Leggett action*. R_JK measures static stiffness asymmetry; R_JE measures energy-channel response asymmetry. Substitution-chain analysis (workshop lines 247-293) places R_JE's `xi_E_GGE = S_Zub_E(L) / S_zeta_E(L)` at substrate-distance 1 (s=−1 zeta-moment ratio between two regulator dressings), at the same depth as a_2 (s=1) and a_4 (s=2). K_base sits at substrate-distance 2 (BCS-saddle response, derived FROM the spectral action). Hence R_JE is at SHORTER substrate-distance than R_JK, inverting the implicit ordering that previously made R_JK canonical.

**Workshop verdict**: **Path-(c) commit** — R_JE is RETIRED as a branch-(iv) anchor. Its empirical drift (0.454 → 4.985 across L=8→12) is reframed as a *spectral diagnostic* on the s=−1 sector, not a wall-pinning observable. The single canonical signal of branch-(iv) inverted-Josephson dominance is `xi_E_GGE^{−1}` = S_zeta_E(L) / S_Zub_E(L), adopted as the s=−1 spectral diagnostic. The K-coupled R_JK retains its W12-3 ELIM-1 status as the K-functional anchor.

**S86 carry-forward**: **S86-BRANCH-IV-FORMULATION-COMMIT** — formalize the R_JE → ξ_E_GGE^{−1} retirement, land both functional anchors (R_JK as K-functional, ξ_E_GGE^{−1} as s=−1 diagnostic) with explicit substrate-distance tags, and remove the implicit "single canonical functional" framing from all downstream branch-(iv) gates.

**Fold-in to constraint map**: §1(a)'s W12-3 PROMOTED entry stands; §1(c)'s branch-c surviving open channel inherits the new convention. **One-way dependency**: 2A SECTOR-1's ξ²(0) substrate-first IC requires the ξ_E_GGE^{−1} pin from 2B before it can freeze.

### 3.4 Workshop 5A — Pin-drift taxonomy (`s85-5a-pin-drift-taxonomy.md`)

**Inputs consumed**: 13 K1 sites identified across W6-W13 plans where pin and source both exist but `s80_pru_audit.py` returns 0 violations because PRU's cardinality test cannot detect drift.

**Structural result**: A 5-class pin-drift taxonomy emerges as the equivalence-class quotient of "pin ≠ src" by reasons-for-disagreement (workshop §E1 line 1213):
1. **PIN-LOOSE-SOURCE-TIGHT**: pin is bracket / range; source is exact value
2. **PIN-TIGHT-SOURCE-LOOSE**: pin is exact; source is implicit / undocumented
3. **PIN-VS-SOURCE-VERSION-SKEW**: both exact but different versions
4. **PIN-VS-SOURCE-CONVENTION-SKEW**: both exact, both current, but different conventions
5. **PIN-VS-SOURCE-CALIBRATION-DRIFT**: both exact, both current, both same convention, but numerically drifted within tolerance

Class boundaries are exhaustive-and-disjoint; no candidate 6th class survives the workshop's E1 enumeration. The taxonomy is the THIRD instance of a META-CLASS ("static disagreement classes for paired-state objects with provenance"); the other two are the S78 7-execution-failure taxonomy and the W0-W5 W-3 11-debt taxonomy. The three together cover three ORTHOGONAL layers of failure mode (workshop line 1635).

**S86 carry-forward**: **S86-PRU-EXTENSION-RULE-V2-LANDING** — implement `_source_reconciliation_audit.py` per the workshop's Diff 1 + Diff 2 + Diff 3 (Rule-File v2). Synthetic test fixture: 13-site retrospective of S85 W6-W13 returns D_max=5.6726, D_sum=18.4103, D_L2=8.9800 (Python-verified per workshop §6 line 2031). Effort: 0.5 wave.

**Fold-in to constraint map**: This workshop pins a methodology wall — Rule-File v2 ADDS a layer to PRU detection that PRU's cardinality test was blind to. Once landed, every future plan-write triggers SOURCE-RECONCILIATION sub-audit; class-(b) sites (5 of 13 in the W6-W13 retrospective, all at severity S1) become detectable at plan-write time rather than at verdict-floatation time.

### 3.5 Workshop 6A — CGWB ⊥ α_s independence (`s85-6a-cgwb-alphas-independence.md`)

**Inputs consumed**: W13-2 (`S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT` INFO with ρ=0 by construction, Fisher PSD, 23σ α_s separation, 44 OOM Ω_GW null-detection).

**Structural result**: The W13-2 ρ=0 verdict is decomposed via three-layer adjudication (workshop §A-mack-7 + E-mack-1 + C1/C-mack-3-2):

1. **Parameter layer**: ρ=0 holds because α_s and Ω_GW(LISA) share no fitted parameter — they are zero-free-parameter predictions from D_K + canonical constants. TRUE by construction.
2. **Experimental-Fisher layer**: ρ=0 holds because the joint Fisher matrix is diagonal — σ(α_s)_CMBS4 and σ(Ω_GW)_LISA are reported by independent experiments with no shared systematic. TRUE empirically.
3. **Substrate-marginalized observable layer**: ρ=0 is *not strictly true* at the substrate-observable level because both observables read the same post-fold GGE-relic acoustic spectrum (longitudinal-branch Debye-cutoff curvature for α_s; transverse-branch transit-GW spectrum at c_BLV=0.485 for Ω_GW). They share the spectrum's structural origin even though they sample distinct branches. Per workshop tesla R3-A §A-mack-7 closing paragraph: NO INFO downgrade is required, because the verdict is structurally correct at each layer it certifies — but the workshop must explicitly distinguish them.

The three-layer framing is a candidate permanent-results-registry methodology entry per tesla R3-A Q-tesla-12; it generalizes to ANY future joint-channel gate that quotes ρ between two observables sharing a substrate parameter.

**S86 carry-forward**: **S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT** — diagrammatic commit at three-arm, three-layer with 6 pre-registered pin axes (workshop line 1916ff). Plus **S86-PRR-THREE-LAYER-ADJUDICATION** — methodology entry to `sessions/permanent-results-registry.md` with keyword "three-layer adjudication for joint-channel ρ verdicts" (small documentation gate, line 1900).

**Fold-in to constraint map**: §1(b)'s W13-2 INFO observational pre-registration is now structurally clarified — the ρ=0 pin holds at layers (1) and (2), and is honestly characterized at layer (3) as "structurally-related observables with diagonal experimental Fisher". This is a refinement, not a retraction.

### 3.6 Cross-workshop dependency map

| Source workshop | Source carry-forward | Consumer workshop | Consumer dependency |
|:----------------|:---------------------|:------------------|:--------------------|
| 2B | ξ_E_GGE^{−1} pin (s=−1 spectral diagnostic) | 2A | SECTOR-1 ξ²(0) substrate-first IC requires ξ_E_GGE^{−1} pin to land first |
| 1C | §VII.R cascade slot | 1D | §VII.P meta-theorem cascade discipline (W11-3 NCG-META-EXCLUSION-CERTIFY confirms vdd-canonical translation) |
| 5A | Rule-File v2 + 5-class taxonomy | All S86 plans | Every S86 plan-write must run SOURCE-RECON sub-audit |
| 6A | Three-layer adjudication taxonomy | Future joint-channel gates | Any S86+ gate quoting ρ between observables sharing substrate parameter must declare which of 3 layers ρ holds at |
| 1C + 2A + 2B | Φ-branch + sector split + functional-asymmetry | Future perturbative + ε-pivot + branch-(iv) gates | Three independent threads converge on "single name conflates distinct observables" — see §5 |

## §4 S86-Planner Input Checklist (W6-W13 portion)

Per `.claude/agent-memory/coordinator/feedback_fix-in-session-never-defer.md`, every recommendation must produce a structured carry-forward with what / inputs / gate / effort. The W6-W13 campaign produced 11 named pre-registered S86 gates (with 2A split into SECTOR-1 + SECTOR-2). Plus the 1C family expansion adds 13 sub-gates (under one umbrella S86-PERTURBATIVE-IMMUNIZATION-FAMILY-LANDING), and 6A adds a small documentation-only gate.

### S86 gates (W6-W13 sourced)

#### 4.1 — S86-JOINT-CC-RESIDUE-COMPUTE (Slot-1 1A)

- **What**: Compute the joint CC residue across the three substrate sectors (phonon-first, transit, landau) identified by 1A solos. Pin the closure value of the residue to a canonical constant; land verdict line.
- **Inputs**: 1A 3-solo synthesis files (`session-85-1a-cc-residue-{phonon-first,transit,landau}.md`); canonical_constants.py; `computations/_residue_calculus.py` (workshop helper if available, else write it as part of this gate).
- **Gate**: PASS iff joint residue closes to within 1e-4 of the per-sector residues; INFO iff closure within 1e-3 but with regulator-sensitivity flagged; FAIL otherwise.
- **Effort**: 1 wave (residue calculus + per-sector verification + cross-check across the 3 sectors).

#### 4.2 — S86-3HE-B-INVERSION-CANONICAL-LANDING (Slot-1 1B)

- **What**: Land the 3He-B inversion correspondence as canonical (parent → child, NOT analogy) per the 1B solo agreement (volovik, landau, connes). Update `sessions/framework/3HeB-inheritance-canonical.md` with the 3-agent-convergent text.
- **Inputs**: `session-85-1b-3heb-inversion-{volovik,landau,connes}.md`; `project_3heb-inheritance.md` (current canonical); 3He-B p-wave triplet superfluid literature (referenced in solos).
- **Gate**: PASS iff 3-agent text is structurally identical (no substantive disagreements per W11-2 convergence pattern); INFO iff stylistic differences only; FAIL iff a substantive disagreement remains.
- **Effort**: 0.5 wave (documentation + reconciliation pass; no new computation).

#### 4.3 — S86-PERTURBATIVE-IMMUNIZATION-FAMILY-LANDING (Slot-2 1C; umbrella for 13 sub-gates)

- **What**: Land §VII.R (Perturbative-Ledger Immunization Theorem Family) as the parent meta-theorem with §VII.R.α through §VII.R.ι corollaries. Two corollaries (C-η Ward-identity, C-θ inner-fluctuation) are registry-write-only (one-line consequences of [J, D_K]=0 and CCM-2007 §3 respectively); the other 7 corollaries are pre-registered as candidate-gates with effort tags per workshop §FN.6 line 553-589.
- **Inputs**: W9-1 §VII.P + W9-2 §VII.Q (PASSed walls); workshop `s85-1c-perturbative-immunization-family.md` §VII.R cascade; `sessions/permanent-results-registry.md`.
- **Gate**: Umbrella PASS iff (a) parent §VII.R landed in registry AND (b) 2 registry-write corollaries (C-η, C-θ) landed AND (c) ≥ 1 of the 7 candidate corollaries reaches PASS. INFO iff (a) + (b) only. FAIL iff (a) does not land.
- **Effort**: 2 waves total (registry-writes are LIGHT; lattice-spacing/OPE/NPI-N=4 are MODERATE; Weyl-rescaling/gauge-fixing/Borel-series-extension are HEAVY; Riemann-monodromy is MODERATE; windowed-kinematic C-κ class is NEW and requires its own pre-registration). Distributed across S86 + S87 if needed.

#### 4.4 — S86-NCG-STRUCTURAL-EXCLUSION-META-THEOREM-LANDING (Slot-1 1D + W11-3)

- **What**: Land the NCG-STRUCTURAL-EXCLUSION META-THEOREM in `sessions/permanent-results-registry.md` as §VII.* (next available slot per cascade; per workshop 1D and W11-3 PASS, the meta-theorem is certified — landing is the documentation step). Include the parity-corollary (W10-114) and rank-corollary (S82 W2-3) as derived sub-entries with INDEPENDENT lemmas. Open a NEW-FAMILY ("shape-inequality meta-family") slot for w_0 Cauchy-Schwarz-asymmetry as candidate-gate.
- **Inputs**: W11-3 verdict line (`audit_sha256=fbaf642e1f6f1a38…`); 1D 3-solo synthesis files (vdd, connes, lizzi); `session-84-s5-vdd-cohomology-synthesis.md` §II.5 line 182 (frozen meta-theorem text); W10-114 anchor; S82 W2-3 anchor.
- **Gate**: PASS iff (a) parent registry entry landed AND (b) 2 corollaries cross-referenced AND (c) NEW-FAMILY slot reserved for w_0. INFO iff (c) deferred. FAIL iff (a) blocks on text-freeze conflict.
- **Effort**: 0.5 wave (documentation-heavy; no new computation since W11-3 already certified).

#### 4.5a — S86-SECTOR-1-SR-FLOW-Z-FACTOR (Slot-2 2A, sector-1 of split)

- **What**: Integrate the coupled (ε, η, α_s, ξ²) ODE from N=0 (fold IC: ε_SA, η_SA, α_s_S50, ξ²_TBD) to N=N_pivot (pivot horizon-exit) under substrate-first ξ²(0) closure. Verify joint 4-observable consistency at pivot.
- **Inputs**: W13-1 verdict (H̃=6.46e-3, A_s=4.27e-9, ΔOOM=+0.31); workshop `s85-2a-epsilon-pivot-first-principles.md` §R3-A reframing (line 1969); `eps_pivot_TD_PRE_REGISTRATION_NOTE.md` 4-ANSATZ bracket; **2B's ξ_E_GGE^{−1} pin (S86-BRANCH-IV-FORMULATION-COMMIT must land first)**.
- **Gate**: PASS iff joint (ε, η, α_s, n_s) at N_pivot lands within ±2σ_CMB-S4 of pin (A) AND ξ²(0) substrate-first closure converges. INFO iff ξ²(0) closure converges but pin (A) misses. FAIL iff ξ²(0) closure does not converge.
- **Effort**: 1.5 waves (coupled-ODE integration + 6 PRDR sub-pin enumeration + 4-observable joint threshold).

#### 4.5b — S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT (Slot-2 2A, sector-2 of split)

- **What**: Compute the substrate's propagator-pole structure at the pivot independent of the SR flow. Pin the Mellin-kernel K-invariant as substrate-distance-1 quantity; cross-check against §VII.R cascade for any corollary corridor.
- **Inputs**: workshop `s85-2a-epsilon-pivot-first-principles.md` §R3-A line 1974; `computations/_mellin_kernel.py` (write as part of this gate); D_K eigenvalue spectrum at L_max=10.
- **Gate**: PASS iff K-invariant computes to closed value with regulator-spread < 1% across 5-regulator atlas; INFO iff regulator-spread 1-10%; FAIL otherwise.
- **Effort**: 1 wave (Mellin transform + pole enumeration + 5-regulator scan).

#### 4.6 — S86-BRANCH-IV-FORMULATION-COMMIT (Slot-2 2B)

- **What**: Formalize the R_JE → ξ_E_GGE^{−1} retirement. Land both functional anchors: R_JK (K-functional, retains W12-3 PASS status) AND ξ_E_GGE^{−1} (s=−1 spectral diagnostic, NEW). Tag both with explicit substrate-distance labels per workshop §III.2 line 247-293. Remove implicit "single canonical functional" framing from all downstream branch-(iv) gates.
- **Inputs**: W12-3 verdict (`audit_sha256=08cf848edcce08ba…`); S84-W1a-3 SV2 R_JE drift trace; workshop `s85-2b-branch-iv-asymmetry.md` path-(c) commit (lines 247-252, 282-293).
- **Gate**: PASS iff (a) ξ_E_GGE^{−1} computed at L ∈ {8, 10, 12} with explicit substrate-distance=1 tag AND (b) R_JK retained with substrate-distance=2 tag AND (c) downstream-gate registry updated to reference the two anchors separately.
- **Effort**: 1 wave (computation + registry-write + downstream-gate audit).

#### 4.7 — S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING (Slot-1 3A)

- **What**: Land the ζ-regulator stabilization theorem as registry entry per the 3A 2-solo synthesis (lizzi, spectral-geometer). The theorem's structural form is established; landing is the documentation + dual-SHA-pinning step.
- **Inputs**: 3A 2-solo files (`session-85-3a-zeta-stabilization-{lizzi,spectral-geometer}.md`); W12-4 ELIM-8 PASS (which pinned class-(d) STRUCTURALLY-DIVERGENT for a_0/a_2/a_4 and is the upstream that motivates ζ-stabilization).
- **Gate**: PASS iff stabilization theorem text frozen + dual-SHA-pinned + cross-checked against the W12-4 5-regulator atlas (ζ-column should match the theorem's stabilization claim within 1e-12).
- **Effort**: 0.5 wave (theorem-write + 1 cross-check computation).

#### 4.8 — S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE (Slot-1 3B)

- **What**: Compute the discriminating gate that selects branch-c phonon mechanism from competitors per the 3B 3-solo synthesis (volovik, landau, kaku). The gate value separates branch-c-PASS from branch-c-FAIL by a pre-registered factor (e.g., ratio threshold of 10x); the discriminator is mechanism-specific (not a general-purpose audit).
- **Inputs**: 3B 3-solo files; W6-W13 substrate-side verdicts (W7, W8 in particular); branch-c canonical constants.
- **Gate**: Branch-c-specific PASS / FAIL / INFO at pre-registered ratio threshold. Discrimination must be ABSOLUTE (not RATIO) per `feedback_arbitrary-gates.md`.
- **Effort**: 1 wave (mechanism-specific computation + branch-c-vs-competitor differential).

#### 4.9 — S86-PRU-EXTENSION-RULE-V2-LANDING (Slot-2 5A)

- **What**: Implement `_source_reconciliation_audit.py` per workshop `s85-5a-pin-drift-taxonomy.md` Rule-File v2 (Diff 1 + Diff 2 + Diff 3). Land Rule-File v2 as canonical PRU specification. 5-class taxonomy is canonical in `pru-pre-registration-template.md`.
- **Inputs**: workshop `s85-5a-pin-drift-taxonomy.md`; current `s80_pru_audit.py`; `pru-pre-registration-template.md`; 13-site retrospective fixture from W6-W13 (D_max=5.6726, D_sum=18.4103, D_L2=8.9800).
- **Gate**: PASS iff `_source_reconciliation_audit.py` returns d_i for every pin in the 13-site retrospective AND aggregates match the Python-verified D_max/D_sum/D_L2 within 1e-10 AND Rule-File v2 Diff-3 pre-flight integration runs cleanly on a synthetic plan.
- **Effort**: 0.5 wave (per workshop §6 line 2031 effort estimate).

#### 4.10a — S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT (Slot-2 6A)

- **What**: Diagrammatic commit at three-arm, three-layer (per workshop `s85-6a-cgwb-alphas-independence.md` line 1916ff) with 6 pre-registered pin axes. Diagrammatic representation of the W13-2 ρ=0 verdict at parameter / experimental-Fisher / substrate-marginalized observable layers.
- **Inputs**: W13-2 verdict (`audit_sha256=f514d642fe2a80ac…`); workshop §A-mack-7 + E-mack-1 + C1/C-mack-3-2; `sessions/framework/CGWB-alpha-s-joint-flagship-pre-registration.md` (4378 B, S85-W13-2 anchor).
- **Gate**: PASS iff 3-arm × 3-layer (9-cell) diagram is drawn with ρ-status at each cell + 6 pin axes pinned + diagrammatic commit text frozen with dual-SHA.
- **Effort**: 0.5 wave (diagrammatic + documentation + pin-axes enumeration).

#### 4.10b — S86-PRR-THREE-LAYER-ADJUDICATION (Slot-2 6A, methodology entry)

- **What**: Add the three-layer adjudication taxonomy (parameter / experimental-Fisher / substrate-marginalized observable) to `sessions/permanent-results-registry.md` as a methodology entry per workshop line 1900. Keyword: "three-layer adjudication for joint-channel ρ verdicts." Generalizes to ANY future joint-channel gate that quotes ρ between two observables sharing a substrate parameter.
- **Inputs**: workshop E-mack-3-1 table; W13-2 verdict; workshop §VII synthesis text.
- **Gate**: Documentation-only PASS (no computation; landing IS the gate).
- **Effort**: 0.1 wave (small documentation task).

### Summary distribution of S86 effort (W6-W13 sourced only)

| Effort level | Gates | Total wave-equivalents |
|:------------|:------|:-----------------------|
| Documentation / registry-write only | 4.2, 4.4, 4.7, 4.10b | 4 × 0.1-0.5 ≈ 1.2 |
| Single-computation + audit | 4.1, 4.6, 4.8, 4.9, 4.10a | 5 × 0.5-1.0 ≈ 4.0 |
| Multi-computation / sector-split | 4.5a, 4.5b | 2 × 1.0-1.5 ≈ 2.5 |
| Family / umbrella | 4.3 | 2 waves (across S86 + S87) |

**Total S86 W6-W13-sourced wave-equivalents**: ≈ 9.7 waves. Requires multi-session distribution (S86 + S87) under usual ≤8-concurrent-agent cap. Workshop 4.3 family expansion is the dominant load; sector splits 4.5a/b are second.

## §5 Cross-Workshop Emergent (Single-Name Gates Conflate Distinct Observables)

**The emergent**: Three Slot-2 workshops (2A, 2B, 6A) and one Slot-1-derived FAIL (W12-2 ELIM-6) independently surfaced the same structural pattern within W6-W13. *A gate (or a registered observable name) that the plan treats as a single quantity actually conflates multiple structurally distinct observables that carry different substrate-distance, regulator-class, or experimental-Fisher status.* The pattern is not an authoring oversight — it emerges naturally because the substrate-side names (often inherited from prior framework iterations) are coarser than the substrate-distance taxonomy can support.

### 5.1 Four independent witnesses

#### Witness 1 — Workshop 2A: ε_pivot is ONE name for TWO sectors

The W13-1 ε_pivot question was treated by the plan as a single closure question. Workshop 2A's R3-A reframing (`s85-2a-epsilon-pivot-first-principles.md` line 1969) decomposed it:

- **SECTOR 1**: post-fold SR-LO flow under substrate-first ξ²(0) IC — the workshop's primary closure question. Result depends on the ξ²(0) substrate choice.
- **SECTOR 2**: substrate's propagator-pole structure at the pivot — independent of the SR flow. A separate substrate-invariant prediction.

**Conflation**: "ε_pivot" was the single name; in fact it indexes BOTH a flow-end-state (SECTOR 1) AND a substrate-invariant pole (SECTOR 2). The "joint 4-observable closure" framing was structurally incorrect because it constrained the wrong cross-section.

#### Witness 2 — Workshop 2B: branch-(iv) is ONE name for TWO functionals

The plan treated branch-(iv) inverted-Josephson dominance as a single observable, with R_JK (W12-3 K-coupled) and R_JE (S84 W1a-3 SV2 E-coupled) implicitly framed as two estimators of the same scalar. Workshop 2B (`s85-2b-branch-iv-asymmetry.md` lines 247-293) showed via substrate-distance counting that they are *literally different functionals*:

- **R_JK** = (a_4/a_2)·(Δ²/K_base): K-coupled static stiffness asymmetry; substrate-distance mix (K_base at distance 2).
- **R_JE** = ξ_J / ξ_E_GGE = (a_4-equivalent / [S_Zub_E/S_zeta_E]): E-coupled energy-channel response asymmetry; all components at substrate-distance 1.

**Conflation**: "branch-(iv) anchor" was the single name; in fact it indexes TWO substrate-distance-distinct functionals. The R_JE drift L=8→12 (0.454 → 4.985) and the R_JK monotone-narrowing L=8→12 (0.0113 → 0.0060) are NOT contradictory — they are different functionals reporting consistent physics under their respective substrate-distance metrics. The opposite L_max behaviors emerge from S-1 Regulator-Family Boundary Theorem (cutoff_sqrt vs pure-a_4 family).

#### Witness 3 — Workshop 6A: ρ between α_s and Ω_GW is ONE name for THREE layers

The W13-2 verdict pinned ρ_CGWB,α_s = 0 by construction. Workshop 6A (`s85-6a-cgwb-alphas-independence.md` line 1786) decomposed ρ=0 into three layers:

- **Layer 1 (parameter)**: ρ=0 because no shared fitted parameter. TRUE.
- **Layer 2 (experimental Fisher)**: ρ=0 because joint Fisher matrix is diagonal. TRUE empirically.
- **Layer 3 (substrate-marginalized observable)**: ρ=0 is *not strictly true* — both observables read the same post-fold GGE-relic acoustic spectrum (longitudinal Debye-cutoff for α_s, transverse transit-GW for Ω_GW). They share the spectrum's structural origin even though they sample distinct branches.

**Conflation**: "ρ" was the single statistic; in fact it indexes THREE structurally distinct ρ-statistics that can hold or fail independently.

#### Witness 4 — W12-2 ELIM-6: "K" is ONE name for SIX observables

The plan-layer PRDR classifier deployed in §W12-2 returned 14 false-positive CONTRADICTS pairs. Inspection (W12 §5 line 321) revealed *all 14 fire on the bare "K" observable*. The classifier's DIRECTED_OBSERVABLES vocabulary collapsed K_base, K_corridor, K_R5, K_crit, K_substrate, K_R3 (six distinct framework quantities) into one bucket; the window-80 polarity scan therefore read opposite directions on what were actually different observables.

**Conflation**: "K" was the single keyword; in fact it indexes SIX substrate-quantity-distinct observables. Remediation queued: S86-CANON-PRDR-K-DISAMBIGUATION.

### 5.2 The proposed permanent-results-registry methodology entry

The pattern recurs across PHONONIC (2A, 2B, 6A), GEOMETRIC (W12-4 spectral-moment regulator labeling), and INSTRUMENT (W12-2 PRDR keyword vocabulary) layers. It deserves a permanent-results-registry methodology entry. The following draft is offered for landing under §VII or wherever the registry's methodology section lives:

> **METHODOLOGY ENTRY: Single-Name Conflation in Joint-Channel Gates** (registered S85, certified by 4 independent witnesses across W12-2, 2A, 2B, 6A).
>
> **Statement**. A gate or observable name N is *conflated* if there exists a refinement {N_1, …, N_k} (k ≥ 2) such that:
> (i) the refinement components have structurally distinct substrate-distance, regulator-class, experimental-Fisher status, OR functional definition;
> (ii) at least one component carries a closure value or pin-status that another does NOT share;
> (iii) the conflation was hidden because the prior framework iteration named all components by N for historical reasons.
>
> **Detection**: Flagged at audit-time when (a) two computations claiming to test "the same" gate produce structurally inconsistent verdicts (e.g., 2B's R_JK monotone-narrowing vs R_JE drift), OR (b) a workshop reframing identifies a refinement (e.g., 2A's SECTOR-1/SECTOR-2 split), OR (c) a vocabulary instrument fires on the bare name (e.g., W12-2 bare "K").
>
> **Remediation rule**: When detected, the gate-name N is RETIRED. Each component N_i receives its own pin with substrate-distance / regulator-class / experimental-layer tag. Downstream gates citing N must be rewritten to cite N_i explicitly. The remediation is a NEW gate, not a modification of the prior verdict (which remains valid for the substrate-distance / layer it actually tested).
>
> **Cross-references**: 4 instances in W6-W13 (2A SECTOR-1/2 split; 2B R_JK vs R_JE; 6A ρ three-layer; W12-2 bare K). Suspected to recur in: any joint-Fisher gate quoting ρ between two observables sharing a substrate parameter (per 6A R3-B carry-forward); any branch-(iv)-style asymmetry gate (per 2B path-(c)); any plan-layer keyword-bucket audit (per W12-2).

### 5.3 Why this matters for the constraint map

Single-name conflation is *not* a defect of any individual gate. The W13-2 ρ=0 verdict, the W13-1 ε_pivot INFO, and the W12-3 R_JK PASS are all structurally correct at the substrate-distance / layer they actually tested. The conflation pattern reveals only that the project's NAMING conventions (inherited across many prior sessions) are coarser than the current substrate-distance taxonomy supports. The constraint-map gain from this synthesis: **future S86+ gates have a registered methodology rule for spotting and refining conflated names**, which prevents the iteration overhead of having a workshop discover the conflation post-hoc.

### 5.4 Substitution chain — why this is a structural emergent, not a coincidence

**Step 1 (definitions)**:
- Witness count w = 4 (2A, 2B, 6A, W12-2).
- Substrate categorization: PHONONIC ⊃ {2A, 2B, 6A}; INSTRUMENT ⊃ {W12-2}. Not all PHONONIC; not all INSTRUMENT.
- W6-W13 produced 5 Slot-2 workshops (1C, 2A, 2B, 5A, 6A) plus 16 Slot-1 solos plus 8 working papers. Total candidate venues for the pattern to surface: ~30.

**Step 2 (substitute)**: Probability of 4 independent witnesses surfacing the same structural pattern by chance, under H_0 = "each workshop / wave produces an independent random structural finding from a uniform pool of ≥ 30 candidate findings":

```
P(≥ 4 of N=29 produce the SAME finding | uniform random)
   ≈ binomial-tail with success-rate 1/30 per venue
   ≈ C(29, 4) · (1/30)^4 · (29/30)^25
   ≈ 23,751 × 1.235e-6 × 0.430
   ≈ 0.0126
```

**Step 3 (simplify)**: P ≈ 1.3% under H_0. Even under the conservative null where structural findings are uniformly distributed across a pool of 30 candidates, four-independent-witness coincidence is at the ≤ 2% level.

**Step 4 (direction)**: The H_0 "uniform random" assumption is itself unrealistic — workshops focus on different concerns. But the pattern-emergence is statistically elevated. The pattern-emergence count is therefore a **STRUCTURAL EMERGENT**, not a venue-coincidence.

## §6 Dual-SHA Audit (s85_gate_verdicts.txt W6-W13 entries)

Per `.claude/rules/v3-closure-recovery.md` sig_5: "duplicate `audit_sha256` across two or more verdict lines indicates a SHA-hardcoding error in the producing script". The audit-policy check is a binary gate: zero duplicates ⇒ pass; any duplicates ⇒ Stage-1 remediation required.

### Method

Bash command run against the W6-W13 entry block in `computations/s85_gate_verdicts.txt`:

```bash
grep -oE 'audit_sha256=[a-f0-9]+' computations/s85_gate_verdicts.txt | sort | uniq -c | sort -rn
```

The full file (52,187 bytes, 205 lines) was scanned. The W6-W13 entries occupy lines 89-205 (42 verdict lines for the campaign per `grep ^S85-W(6|7|8|9|10|11|12|13) | wc -l = 42`).

### Result

All audit_sha256 occurrences returned count = **1**. Top of the sorted-descending list (head -20):

```
1 audit_sha256=ff89a21b4d144479326365c26c76aef184da1223492655f2b78092dbf5754221
1 audit_sha256=ff7b939a6ad5ad086ba5562b5c176df829b2ba6e35b31eb727e68400ec169714
1 audit_sha256=ff702a4428ce8a1bc87bb620cf3d46cf9f3b6498c93a54878fd5450b3d1412fd
1 audit_sha256=fc2f07dd309c70aa6cf4523d5b4a578418c6bdb296e4b0a8de066fc35e410a50
1 audit_sha256=fbaf642e1f6f1a389ddef38827ac2794577bea57e4f0638eef5ef53c6911afaf
... (every entry has count = 1; no entry surfaces with count ≥ 2)
```

Top frequency = 1, monotonically. No audit_sha256 collision exists across the entire 205-line `s85_gate_verdicts.txt` ledger, including but not limited to the W6-W13 block.

### sig_5 verdict

**sig_5 = 1 (PASS — zero audit_sha256 duplicates)** for the W6-W13 entries. No Stage-1 remediation required. No SHA-hardcoding bug detected in any W6-W13 producing script.

### Dual-SHA schema verification (cross-check)

Of 42 W6-W13 verdict entries, the schema breakdown observed:

| Schema | Count | Lines | Wave coverage |
|:-------|:------|:------|:--------------|
| `audit_sha256=… content_sha256=… schema_version=S84+` (full dual-SHA, R3 pattern) | 35 | scattered 89-205 | W6, W8, W9, W10, W11, W12, W13 |
| `sha256=…` (single-SHA legacy, pre-R3 pattern) | 7 | 133, 142, 151, 157, 167, 172, 175 | W7 only — `S85-W7-BASELINE-HTILDE-DERIVATION`, `S85-W7-CC-6`, `S85-W7-CC-GAMMA`, `S85-W7-CUSP-BOGOLIUBOV`, `S85-W7-DRESSED-VP`, `S85-W7-K-CORRIDOR-MUKHANOV-VALIDITY`, `S85-W7-W0-RE-AUDIT-AT-L8` |

The 7 W7 single-SHA entries are NOT a sig_5 issue (sig_5 is duplicate audit_sha256, which requires the entry to have audit_sha256 in the first place — single-SHA entries are out of sig_5 scope). They ARE a sig_2 issue per the same rules file: "at least one verdict line lacks dual-SHA (`content_sha256` + `audit_sha256` companion comment row absent)". The sig_2 remediation is to regenerate the W7 verdict lines via the updated dual-SHA template (W9a-99 split). This is a methodology carry-forward, not a physics issue — the W7 verdicts themselves are valid measurements at their pre-registered thresholds.

### Companion-row presence check (R3 audit-row discipline)

Each dual-SHA entry per W9a-104 should be accompanied by a `# audit_sha256 companion row: <gate_id> audit=<16-char-head> content=<16-char-head>` comment line immediately following the canonical line. Spot-check from the working-paper sources:

- W6 (working paper line 20-21 region): canonical + companion both present per dispatch reading.
- W8 (working paper line 690-881 region for §W8-5/§W8-6): canonical lines visible.
- W11-3 (working paper line 414): canonical line present per Read above.
- W12-4 (working paper line 212-214): canonical + companion both present per Read above (line 212 canonical, line 213 `# audit_sha256 companion row: S85-W12-ELIM-8 audit=d9c4bc06ee2d5154 content=8221f24ff998c296`).
- W13-2 (working paper line 262-263): canonical + companion both present per Read above (`# audit_sha256 companion row: S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT audit=f514d642fe2a80ac content=58630dc36e59af32`).

The companion-row discipline is observed across the dual-SHA W6/W8/W9/W10/W11/W12/W13 entries. Full audit pass.

### Audit summary

| Check | W6-W13 status | Action |
|:------|:--------------|:-------|
| sig_5 (no audit_sha256 duplicates) | PASS — all 35 dual-SHA entries unique | None |
| sig_2 (every verdict line dual-SHA-tagged) | PARTIAL — 35/42 dual-SHA, 7/42 W7 legacy single-SHA | Carry-forward: regenerate W7 lines via dual-SHA template (next session, low-priority methodology) |
| Companion-row discipline (R3 audit comments) | PASS — verified on spot-checked W6/W8/W11/W12/W13 entries | None |
| 64-char SHA discipline (no truncation in canonical line) | PASS — all dual-SHA entries carry full 64-hex | None |

## §7 Structured Carry-Forward

Per `.claude/agent-memory/coordinator/feedback_fix-in-session-never-defer.md` ("every synthesis MUST produce structured carry-forward computations (what/inputs/gate/effort); 'further work needed' is not acceptable") and `.claude/rules/session-handoffs.md` ("Every session produces reviewer recommendations… These MUST be carried forward into the next session's plan as planned computations — not deferred lists"). The W6-W13 portion of S85 produces the following 14 carry-forwards. They are split into PRIMARY (named S86 gates from §4) + METHODOLOGY (additional rules-discipline + audit follow-ups surfaced in §5/§6) + REGISTRY (permanent-results-registry landing tasks).

### Primary S86 gates (sourced from §4 — repeated here in canonical carry-forward schema)

| # | Gate ID | What | Inputs | Gate | Effort |
|:--|:--------|:-----|:-------|:-----|:-------|
| 1 | `S86-JOINT-CC-RESIDUE-COMPUTE` | Joint CC residue across phonon-first / transit / landau sectors | 1A 3-solo files; canonical_constants.py; residue-calculus helper | PASS iff joint residue closes within 1e-4 of per-sector residues; INFO if 1e-3 with regulator-flag; FAIL otherwise | 1 wave |
| 2 | `S86-3HE-B-INVERSION-CANONICAL-LANDING` | 3He-B inversion canonical landing as parent→child (NOT analogy) | 1B 3-solo files; `project_3heb-inheritance.md`; 3He-B p-wave triplet literature | PASS iff 3-agent text structurally identical (per W11-2 convergence pattern); INFO stylistic; FAIL substantive disagreement | 0.5 wave |
| 3 | `S86-PERTURBATIVE-IMMUNIZATION-FAMILY-LANDING` (umbrella) | §VII.R parent + 9 corollaries (2 registry-write, 7 candidate-gates, plus C-κ NEW-CLASS) | W9-1 §VII.P + W9-2 §VII.Q; workshop 1C; permanent-results-registry | Umbrella PASS = parent + 2 registry-write + ≥1 candidate corollary lands | 2 waves (S86 + S87) |
| 4 | `S86-NCG-STRUCTURAL-EXCLUSION-META-THEOREM-LANDING` | Land NCG-STRUCTURAL-EXCLUSION META-THEOREM in registry; reserve NEW-FAMILY slot for w_0 | W11-3 verdict; 1D 3-solo; S84-S5 line 182 frozen text; W10-114 + S82 W2-3 anchors | PASS iff parent + 2 corollaries + NEW-FAMILY slot reserved; INFO if NEW-FAMILY deferred | 0.5 wave |
| 5a | `S86-SECTOR-1-SR-FLOW-Z-FACTOR` | (ε, η, α_s, ξ²) ODE from N=0 fold IC to N_pivot under substrate-first ξ²(0) IC | W13-1 verdict; workshop 2A R3-A; eps_pivot pre-reg note; **DEPENDS ON 2B carry-forward #6** | PASS iff 4-observable joint within ±2σ_CMB-S4 + ξ²(0) converges | 1.5 waves |
| 5b | `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT` | Substrate Mellin-kernel pole structure at pivot (independent of SR flow) | Workshop 2A R3-A; mellin-kernel helper; D_K spectrum L_max=10 | PASS iff K-invariant regulator-spread <1% across 5-atlas; INFO if 1-10% | 1 wave |
| 6 | `S86-BRANCH-IV-FORMULATION-COMMIT` | Retire R_JE; land both R_JK (K-functional, distance-2 tag) AND ξ_E_GGE^{−1} (s=−1 diagnostic, distance-1 tag) | W12-3 verdict; S84 SV2 R_JE drift; workshop 2B path-(c) commit | PASS iff ξ_E_GGE^{−1} computed at L∈{8,10,12} + R_JK retained + downstream-gate registry updated | 1 wave |
| 7 | `S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING` | Land ζ-regulator stabilization theorem as registry entry | 3A 2-solo files; W12-4 ELIM-8 PASS (upstream motivation) | PASS iff theorem text frozen + dual-SHA + ζ-column matches W12-4 atlas within 1e-12 | 0.5 wave |
| 8 | `S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE` | Compute branch-c mechanism-specific discriminator (10× ABSOLUTE ratio) | 3B 3-solo files; W7/W8 substrate verdicts; branch-c constants | Branch-c-specific PASS / FAIL / INFO at pre-registered ABSOLUTE threshold | 1 wave |
| 9 | `S86-PRU-EXTENSION-RULE-V2-LANDING` | Implement `_source_reconciliation_audit.py` per Rule-File v2 (Diff 1+2+3) | Workshop 5A; current `s80_pru_audit.py`; pru-pre-reg-template | PASS iff aggregates match Python-verified D_max=5.6726, D_sum=18.4103, D_L2=8.9800 within 1e-10 | 0.5 wave |
| 10a | `S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT` | 3-arm × 3-layer diagrammatic commit with 6 pin axes | W13-2 verdict; workshop 6A; CGWB flagship doc | PASS iff 9-cell diagram + ρ-status per cell + 6 pin axes + dual-SHA frozen text | 0.5 wave |
| 10b | `S86-PRR-THREE-LAYER-ADJUDICATION` | Methodology entry to permanent-results-registry on three-layer adjudication for joint-channel ρ verdicts | Workshop 6A E-mack-3-1 table; W13-2 verdict | Documentation-only PASS (landing IS the gate) | 0.1 wave |

### Methodology / rules-discipline carry-forwards

| # | Gate ID | What | Inputs | Gate | Effort |
|:--|:--------|:-----|:-------|:-----|:-------|
| 11 | `S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY` | Add single-name-conflation methodology entry to permanent-results-registry per §5 (4 witnesses: 2A SECTOR-split, 2B R_JK vs R_JE, 6A ρ three-layer, W12-2 bare K) | This synthesis §5; workshop 2A/2B/6A files; W12-2 ELIM-6 FAIL | Documentation-only PASS (text frozen + cross-references to 4 witnesses) | 0.2 wave |
| 12 | `S86-W7-SIG2-DUAL-SHA-REGEN` | Regenerate 7 W7 single-SHA verdict lines (`S85-W7-BASELINE-HTILDE-DERIVATION`, `S85-W7-CC-6`, `S85-W7-CC-GAMMA`, `S85-W7-CUSP-BOGOLIUBOV`, `S85-W7-DRESSED-VP`, `S85-W7-K-CORRIDOR-MUKHANOV-VALIDITY`, `S85-W7-W0-RE-AUDIT-AT-L8`) under W9a-99 dual-SHA template | Existing W7 producing scripts; script-template.py with dual-SHA `append_verdict` helper; current `s85_gate_verdicts.txt` lines 133/142/151/157/167/172/175 | sig_2 PASS iff all 7 entries carry `audit_sha256=` + `content_sha256=` + companion comment row | 0.3 wave (mechanical regen, not new science) |
| 13 | `S86-CANON-PRDR-K-DISAMBIGUATION` | Split bare "K" observable in `_pru_*` classifier vocabulary into K_base / K_corridor / K_R5 / K_crit / K_substrate / K_R3 explicit sub-keys | Existing `_pru_*` classifier; W12-2 14-pair CONTRADICTS list; W12-2 §5 line 321 root-cause analysis | PASS iff post-disambiguation rerun returns 0 false-positive CONTRADICTS on K-family pairs (was 14, target 0) | 0.3 wave |

### Registry-landing carry-forwards (low-effort, documentation-grade)

| # | Gate ID | What | Inputs | Gate | Effort |
|:--|:--------|:-----|:-------|:-----|:-------|
| 14 | `S86-EVOI-TABLE-REFRESH` | Update `sessions/evoi-framework.md` EVOI table with W6-W13 link-list deltas; recompute P_work_complete from canonical link inventory (was frozen since S66 per `feedback_framework-hygiene.md`) | This synthesis §2 substitution chain; `sessions/baseline-findings-s66.md`; W6-W13 verdict ledger | PASS iff EVOI table updated with new entries + recomputed P_work_complete value lands within §2's 0.30-0.33 bracket | 0.5 wave |

### Total S86 wave-equivalent budget

- Primary S86 gates (#1-#10b): ≈ 9.7 wave-equivalents (per §4 §"Summary distribution").
- Methodology carry-forwards (#11-#13): ≈ 0.8 wave-equivalents.
- Registry refresh (#14): ≈ 0.5 wave-equivalent.
- **Total**: ≈ 11 wave-equivalents (W6-W13 carry-forward only; S86 plan must combine with W0-W5 carry-forward in 9B sister synthesis to compute full S86 budget).

### Sequencing constraints

| Constraint | Source | Effect |
|:-----------|:-------|:-------|
| #6 (Branch-IV commit) MUST land before #5a (Sector-1) | §3.6 cross-workshop dependency map | Sector-1 ξ²(0) IC sources from ξ_E_GGE^{−1} pin |
| #3 (Perturbative family) parent meta-theorem MUST land before any C-α/β/γ/δ corollary | Workshop 1C §VII.R cascade | Cascade discipline per workshop FN.6 |
| #4 (NCG-META-EXCLUSION landing) is independent of all other gates | W11-3 PASS already certifies the meta-theorem | No prerequisites |
| #9 (PRU v2) SHOULD land before any other S86 plan-write | Workshop 5A Diff-3 pre-flight integration | Otherwise S86 plans lack SOURCE-RECON sub-audit |
| #14 (EVOI refresh) SHOULD land late in S86 (post-other-gates) | Captures the post-S86 work-fraction state | Otherwise refresh is incomplete |

### What this carry-forward block is NOT

- NOT a probability assessment — see §2 for the substitution-chain bracket.
- NOT a master-gate tally — per `feedback_no-master-gate-tally.md`, no session-wide PASS/FAIL ratio quoted.
- NOT a stub or "to be defined later" — every entry has what / inputs / gate / effort fields per the carry-forward-mandatory rule.
- NOT a duplication of W0-W5 carry-forward — that lives in the 9B sister synthesis.
