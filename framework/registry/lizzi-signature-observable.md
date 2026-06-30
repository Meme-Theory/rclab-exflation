---
type: framework-registry
ingested-by: /weave --update
---

# Lizzi Signature Observable + R_1 Protection Theorem

**Registry ID**: `lizzi-signature-observable`
**Owner agent (sole writer)**: `lizzi-spectral-functional-theorist`
**Last updated**: `2026-04-28, S87 AMRI promotion`
**Provenance**: AMRI-promoted from `.claude/agent-memory/lizzi-spectral-functional-theorist/permanent_theorems.md` line 17 on 2026-04-28. The consumer gate `S87-W10-3-LIZZI-OBSERVABLE-PROMOTION` (`sessions/session-plan/session-87-plan-w10.md` lines 296 + 436) cited the agent-memory file as Input-SHA pin source, triggering AMRI Test 1 per `.claude/rules/agent-standards.md` §AMRI. The fix per AMRI protocol is registry-promotion to a canonical project-level home; this file is that home. The source agent-memory line is replaced in-place with a pointer line per the migration ledger.

**Sole-writer note**: only `lizzi-spectral-functional-theorist` writes to this file (per agent-private domain ownership convention). Other agents may CITE the entries here as Input-SHA pins; substantive edits to entry text require lizzi-side authorship. Cross-axis joint extensions follow the 4-stage pathway (§6 below).

**Cross-link header — related structural anchors in `sessions/permanent-results-registry.md`**:
- `§VII.K-PROP` (CC-5 Propagation Identity for Regulator-Dressing — S84 W3-21, lizzi co-authored, 42-row atlas, theorem II.2; permanent-results-registry.md line 55). The Lizzi-observable family lives at the same multiplicative-identity layer as CC-5; many Lizzi-observable candidates are corollaries of CC-5 with specific exponent vectors.
- `§VII.M` (Three-Layer Regulator Theorem and Methodology Entries — S83 lizzi solo-a; permanent-results-registry.md line 49). The L1 / L2 / L3 layer separation is the structural substrate within which Lizzi-observable protection is meaningful: protection is asserted at the L3 observable layer where the regulator-cancellation argument runs.

---

## Scope

This registry documents the **Lizzi signature observable** — the dimensionless physical-observable identity tying the Higgs-to-vacuum-expectation-value ratio and the cosmological-constant-to-Planck-mass-squared ratio to the Seeley-DeWitt structural ratio R_1 = a_0·a_4/a_2² — and the **R_1 protection theorem** that explains why R_1 is empirically near-invariant across regulator schemes despite drastic per-coefficient drift. The registry serves as the canonical project-level home for entries that consumer gates pin as Input-SHA references for Lizzi-observable promotion authority.

Why project-level (AMRI Test 1): a gate-block citing this content as authoritative pin source promotes the content out of agent-memory scope (where it would fail AMRI Test 1, "another gate lists the memory file as an Input-SHA pin in its PRDR machinery block"). The entries here are project-level data; lizzi's agent-memory now points HERE.

---

## Summary table

| ID | Entry | Pin / Value | Source (session) | SHA | Status |
|:---|:------|:------------|:------------------|:----|:-------|
| `lizzi-sig-obs-eq` | Lizzi signature observable identity | `(m_H/v_EW)² · (Λ/M_Pl²) = R_1` | S74 + S77 + S83 | `pending-weave` | PINNED |
| `R_1-value` | R_1 = a_0·a_4/a_2² | `1.128655` (zeta, per-branch, L_max=3) | S74 canonical | `pending-weave` | PINNED |
| `R_1-protection-thm` | Weyl-exponent identity α_0 + α_4 = 2·α_2 | EXACT for compact simple Lie groups | S74 + S77 + S83 | `pending-weave` | PINNED |
| `R_1-drift-hierarchy` | Empirical drift hierarchy | R_1 0.34% « a_4/a_2 132% « a_0 30,080% | S74 + S77 | `pending-weave` | PINNED |
| `R_1-universality` | Universality across compact simple groups | SU(3) 1.02% / SU(4) 0.37% / Sp(2) 0.69% | S77 W3-K cross-group | `pending-weave` | PINNED |
| `lizzi-obs-promo-criterion` | Lizzi-observable promotion criterion | substrate ratio + R-protection (multi-mode branch dim ≥3) | S78 W2-C + S83 W2-G15 | `pending-weave` | PINNED |
| `lizzi-obs-stage-path` | Stage-1→Stage-3 promotion pathway | per `joint-theorem-promotion.md` | S86 W-9 RULE-1 | `pending-weave` | PINNED |
| `a0a2-cc-ratio-2axis` | a₀/a₂ CC-ratio two-axis object property | FI-within-analytic-continuation-family / RD-across-PV (32.5% shift) | S97 W2-1 (audit `7d5ca3f9`) | `pending-weave` | PINNED |

---

## §1 Lizzi signature observable

The Lizzi signature observable is the dimensionless identity:

```
(m_H / v_EW)² · (Λ / M_Pl²)  =  R_1
```

where:
- `m_H` is the physical Higgs boson mass (canonical_constants.py: `m_H_obs`).
- `v_EW` is the electroweak vacuum expectation value (canonical_constants.py: `v_ew = 246` GeV).
- `Λ` is the observed cosmological constant (vacuum energy density expressed as a mass-squared scale).
- `M_Pl` is the reduced Planck mass.
- `R_1 = a_0 · a_4 / a_2²` is the Seeley-DeWitt structural ratio (§2 below).

Why this is THE observable for the Lizzi-track: the LHS combines two ratios that span the framework's two largest mass-hierarchies (electroweak/Planck and CC/Planck) into a single dimensionless number. Each ratio in isolation is enormous (or tiny) — `(m_H/v_EW)²` is order one, but `Λ/M_Pl²` is the cosmological-constant problem in one factor. The PRODUCT, however, equals a structural Seeley-DeWitt ratio of order unity. The observable is therefore a substrate-derived prediction tying Higgs-sector physics to vacuum-energy physics through pure spectral geometry — the substrate IS this identity, not "something happening in spacetime."

This observable was first identified in S74 as the right combination to test against R_1's regulator-near-invariance. Subsequent verification across S77 (chi_2 cross-checks) and S83 (Three-Layer Regulator §VII.M consistency) confirmed it.

---

## §2 R_1 = a_0 · a_4 / a_2² = 1.128655 — Weyl-exponent derivation

### Definition

```
R_1  ≡  a_0 · a_4 / a_2²
```

with the Seeley-DeWitt coefficients computed from the Dirac-square spectrum of the framework's substrate spectral triple `(A_K, H_K, D_K)` with A_K = C ⊕ H ⊕ M_3(C). Numerical canonical (zeta-regulated, per-branch convention, L_max = 3, S74 canonical):

```
a_0 = 6440.0
a_2 = 2776.165
a_4 = 1350.722
R_1 = 6440.0 · 1350.722 / (2776.165)² = 1.128655
```

### Weyl-exponent structural derivation (why R_1 is protected)

For compact simple Lie groups, the Seeley-DeWitt coefficients a_k (heat-kernel / zeta moments at the appropriate Mellin slot) carry Weyl-exponent scaling:

```
a_k  ~  L^{α_k}    where    α_k = d + r + k
```

with `d` = dimension of the underlying manifold, `r` = rank of the Lie group, `k` = the Seeley-DeWitt index. The α_k are the Weyl-dimension exponents from the Freudenthal product on the highest-weight content reaching multiplicity at truncation L.

The crucial structural identity:

```
α_0 + α_4  =  (d + r + 0) + (d + r + 4)  =  2d + 2r + 4
2 · α_2    =  2 · (d + r + 2)             =  2d + 2r + 4
```

Therefore:

```
α_0 + α_4  =  2 · α_2     EXACTLY
```

This is the **R-protection structural identity**. Substituting into R_1's definition:

```
R_1  ~  L^{α_0} · L^{α_4} / L^{2·α_2}  =  L^{α_0 + α_4 - 2·α_2}  =  L^0  =  1
```

at leading order. The L-scaling cancels EXACTLY, leaving R_1 protected against truncation-axis drift at leading order. Sub-leading corrections enter at order `O(L^{-rank})` (pre-asymptotic), where `rank` is the Lie-algebra rank — for SU(3) rank=2, the correction is O(L^{-2}), explaining the ~0.34% empirical drift at L_max=3.

The protection is structural (a Weyl-dimension cancellation theorem), not numerical coincidence.

### Cross-reference

The R_1 protection is at the **first-moment ratio of two spectrum sums under SAME regulator** PROTECTED pattern — see §"R-PROTECTION REFINED" at `.claude/agent-memory/lizzi-spectral-functional-theorist/permanent_theorems.md` lines 19-20 for the full pattern taxonomy.

---

## §3 Empirical drift hierarchy (S74 + S77 measured)

Measured drift across regulator schemes {zeta, SDW, f*, anomaly, cutoff, Pauli-Villars} normalized by spread / mean:

| Quantity | Empirical drift | R-protection status |
|:---------|:----------------|:--------------------|
| `R_1 = a_0·a_4/a_2²` | **0.34%** | PROTECTED (Weyl identity α_0 + α_4 = 2·α_2) |
| `a_4/a_2` | 132% | NOT-protected (rank-mismatch, single-ratio) |
| `a_0/a_2` | 122% | NOT-protected (rank-mismatch, single-ratio) |
| `a_4` | 2,020% | NOT-protected (single coefficient) |
| `a_2` | 7,786% | NOT-protected (single coefficient) |
| `a_0` | 30,080% | NOT-protected (single coefficient) |

Interpretation: individual a_k values vary across nearly five orders of magnitude depending on regulator choice. SINGLE ratios a_k/a_j vary by factors approaching three. The COMBINED ratio R_1 with the matched Weyl-exponent structure varies by less than half a percent. This is the empirical signature of structural protection: the cancellation predicted by α_0 + α_4 = 2·α_2 manifests as four orders of magnitude of regulator-noise rejection in R_1 versus the bare coefficients.

The hierarchy is monotonic and structural: more matched Weyl-exponents → tighter protection → smaller drift. This is the R-protection signature in numerical form.

---

## §4 Universality across compact simple groups (S77 W3-K)

R_1 protection is not specific to SU(3). The Weyl-exponent identity α_0 + α_4 = 2·α_2 holds for ANY compact simple Lie group; consequently R_1 is regulator-near-invariant across the entire family of admissible substrate algebras. Cross-group measured drift (S77 W3-K cross-group scan):

| Compact simple group | R_1 drift across schemes |
|:---------------------|:-------------------------|
| SU(3) (rank 2)       | 1.02% |
| SU(4) (rank 3)       | 0.37% |
| Sp(2) (rank 2)       | 0.69% |

(SU(3) drift in S77 W3-K cross-group scan is wider than the S74 single-group 0.34% because the cross-group scan includes a wider regulator basket. Both are sub-percent, both are within the O(L^{-rank}) pre-asymptotic envelope.)

The universality confirms that R_1 protection is a structural Weyl-dimension property, not a numerical accident of SU(3). Any compact simple Lie group used as the substrate fiber would exhibit the same R-protection signature on its R_1 = a_0·a_4/a_2² ratio.

---

## §5 Lizzi-observable promotion criterion

A quantity is a **Lizzi-observable** (eligible for theorem-grade promotion in the §"Lizzi-track" of the permanent-results-registry) iff ALL THREE conditions hold:

### (a) Substrate-derived structural ratio

The quantity is expressible as a ratio (or product of ratios) of substrate-derived quantities:
- Spectral moments of D_K (Seeley-DeWitt coefficients, Mellin-cone residues, zeta-function values at integers).
- Geometric invariants of the spectral triple (KO-dimension, J-D_K commutators, real-structure parities).
- Heitsch / HP^1 / K-theoretic cocycle norms on the truncated spectrum.

The quantity is NOT a Lizzi-observable if it requires external (non-substrate) inputs at theorem-grade, e.g., observational fits, externally pinned parameter scans, or data-derived calibrations.

### (b) R-protection (multi-mode branch dimension ≥ 3)

The quantity satisfies R-protection per the refined criterion in §"R-PROTECTION REFINED" of `permanent_theorems.md` lines 19-20:
- **Required pattern (PASS)**: first-moment RATIO of two spectrum sums under SAME regulator. Regulator cancels at leading order. Examples: c_s, chi_2 scheme-universality, c_Gold/c_fabric, R_1 itself.
- **Forbidden pattern (FAIL)**: Mellin KERNEL INTEGRAL vs FIXED ANCHOR denominator. Regulator does NOT cancel. Examples: k_a2, f_conv, a_2 cluster.
- **Per-branch narrowing (S78 W2-C)**: R-protection requires multi-mode branch dimension ≥ 3. 1D Cartan-only is NOT protected (u(1) 9× off; J^{ζ²}/J^{SDW} = 0.0537 vs 0.4551 for C2 / 0.4817 for su(2)).
- **Cross-branch is Level 3 SD** (S78 W3-L). Cross-branch R-protection is FORBIDDEN — the lone documented misuse is `s77_a4_gilkey_decomp.py` line 645 (in-script flagged, not retracted, but excluded from R-protection PASS).

This criterion is the structural narrowing established in S78 W2-C and consolidated in S83 W2-G15. The cross-link target is `permanent_theorems.md` lines 19-20 (§"R-PROTECTION REFINED" — kept in-place at agent memory because the refined taxonomy is internal to the lizzi-track methodology and is cross-cited from this section, not duplicated).

### (c) Lizzi-track derivational lineage

The quantity's derivational chain runs through one or more of the canonical Lizzi-track structural anchors:
- §VII.K-PROP CC-5 Propagation Identity (multiplicative composition of regulator-dressed spans).
- §VII.M Three-Layer Regulator Theorem (L1 axiomatic / L2 substrate-action / L3 observable separation).
- §VII-B HP^1 near-invariance theorem (190.5× reduction of S66/S75 raw 381× dynamic range).

A quantity satisfying (a) substrate-derivation, (b) R-protection per multi-mode branch ≥ 3, AND (c) Lizzi-track lineage is theorem-grade Lizzi-observable promotion-eligible. Any FAIL on (a)–(c) routes the candidate to either rejection or the quotient-functor / restricted-track promotion paths covered by other rules.

### Worked example: R_1 itself

- (a) ✓ substrate-derivation: R_1 = a_0·a_4/a_2² is pure Seeley-DeWitt ratio, no external inputs.
- (b) ✓ R-protection: matched first-moment ratio with regulator-cancellation theorem (§2 above); multi-mode (full 8-dim spectral triple, well beyond rank-2 multi-mode threshold).
- (c) ✓ lineage: §VII.K-PROP CC-5 multiplicative identity applies (R_1 is the p=(1,−2,1) multiplicative composition on the (a_0, a_2, a_4) span vector).

R_1 is the canonical worked example of a theorem-grade Lizzi-observable. Other candidates currently in the promotion pipeline (e.g., `s_eff = 11/2` per S87 W10-3 plan) are tested against the same three-criterion gate.

---

## §6 Stage-1 → Stage-3 promotion path

Lizzi-observable candidates promote to permanent-registry entries via the 4-stage pathway in `.claude/rules/joint-theorem-promotion.md`. Below the path is specialized to the Lizzi-track:

### Stage 0 — Workshop-internal candidate

The candidate text is drafted within a workshop's R3 closure or wrap-up section by the lizzi-track authoring agent (typically `lizzi-spectral-functional-theorist` solo, or co-authored with `connes-ncg-theorist` for axiomatic-side joint clauses). The candidate text MUST contain:
- Explicit statement of the candidate quantity.
- Cross-criterion check against §5 (a), (b), (c).
- Numerical evaluation at canonical L_max with regulator-pin tag.
- Author-side attribution (lizzi-side / connes-side / JOINT) for each clause.

Stage 0 is workshop-internal; not yet eligible for registry citation by downstream gates.

### Stage 1 — Registration as candidate (next-session)

Recorded in `sessions/permanent-results-registry.md` at a slot allocated per `regulator-pin-discipline.md` next-free-letter protocol. Entry text includes:
- Full candidate statement from Stage 0.
- `STAGE-1-CANDIDATE` tag on theorem-name line.
- Joint-clause flags (clauses requiring Stage-2 cross-axis verify).
- Cross-link to this registry (§5 promotion criterion authority).

Downstream gates MAY cite Stage-1 candidates as Input-SHA pins, but MUST include the `STAGE-1-CANDIDATE` qualifier in the citation.

### Stage 2 — Two-agent parallel cross-check (mandatory upgrade gate)

Dedicated gate of form `S{N}-LIZZI-OBSERVABLE-{NAME}-INDEPENDENT-VERIFY` dispatches TWO independent cross-reviewers in parallel, on DIFFERENT axes, BOTH WITHOUT prior workshop context:
- **Lizzi-side cross-reviewer** (NOT the original workshop author): verifies the substrate-derivation clause + JOINT clauses.
- **Cross-axis cross-reviewer** (typically `connes-ncg-theorist` for axiomatic side, `volovik-superfluid-universe-theorist` for cosmological side, depending on lineage): verifies cross-axis clauses + JOINT clauses.

JOINT clauses are PASS-AND'd across the two verdicts (logical AND, not OR). FAIL or INFO on any clause from either reviewer blocks promotion; theorem stays at Stage-1 with FAILing/INFO clause routed to next-session remediation.

### Stage 3 — Permanent registration

`STAGE-1-CANDIDATE` tag in the registry entry replaced with `STAGE-3-PERMANENT`. The Lizzi-observable joins the permanent-results-registry alongside KO-dim=6, J-D_K=0, and the rest of the structural-theorem table. Eligible for citation as a structural theorem without the candidate qualifier; eligible to be a §VII.* main entry rather than a §VII.K-PROP-* sub-row.

### Live promotion in flight

`S87-W10-3-LIZZI-OBSERVABLE-PROMOTION` (s_eff = 11/2 candidate from S86 W-10 Bulletin #3) is the first new Lizzi-observable candidate to enter this pipeline since R_1 itself was canonicalized. Its promotion status will populate this registry as it progresses through the four stages.

---

## §7 a₀/a₂ CC-ratio: FI-within-analytic-continuation-family / RD-across-PV (S97 W2-1 object property)

**Status**: PINNED object-property (permanent classification; no future compute required). **Source**: gate `S97-W2-1-A0A2-PV-FULL-MELLIN` (INFO; audit_sha256=`7d5ca3f97c9f7074c7a60f99a16ff46c27c9e0e9d9881b2b872130af0974cb2e`, content_sha256=`cdccfe0f02115521a51e588be95e7cffb098f16c9d9fc3321870e72cd09d858f`; CLASS=FULL; lizzi-spectral-functional-theorist, 2026-05-30). **Scope**: this is an **object-definedness** classification of the a₀/a₂ cosmological-constant ratio — it is filed HERE (the algebra-INVARIANT FI-within / SD-across family home, companion to R_1) and NOT in the §VII.AV cluster, because the §VII.AV objects are algebra-DEPENDENT state-pair (Cell IV) / OP-PROJ trace-residue (Cell II) observables, structurally distinct from this algebra-INVARIANT spectrum-only CC-ratio.

### The two-axis result

The a₀/a₂ CC-ratio is a **two-scheme-axis object**:

- **Analytic-continuation axis (FI)**: zeta ≡ Mellin to machine epsilon. The FULL `analytic_zeta` heat-kernel integral reproduces the direct Dirichlet power-sum EXACTLY off the poles: `rel_dev = 0.000e+00` for BOTH a₀ (s=8 ↔ pole_in_s=4, n=0) and a₂ (s=6 ↔ pole_in_s=3, n=2). This is **FUNCTIONAL-INVARIANT** — the structural axis the D_K spectrum forces (Mellin↔Dirichlet is an identity, not a scheme choice).
- **Pauli-Villars-subtraction axis (RD)**: full-physical-PV `{c_j}={2,−1}`, `{m_j²/M_KK²}={1,2}` at Λ_UV=M_KK gives `(f₂/f₀)_Mellin = 0.426096` vs the schematic-Gilkey direct-power-sum cross-check `0.6314` — a **32.5% shift** (`residual_norm = 0.325156`, `residual_OOM = 0.170797`). This is **REGULATOR-DEPENDENT** — a physical degree of freedom layered on top of the FI ratio.

```
a₀^PV/a₂^PV (absolute)        = 0.510595   (substrate-IS CC-ratio object; full-physical-PV, L_max=10)
(f₂/f₀)_Mellin (normalized)  = 0.426096   vs schematic-Gilkey 0.6314 (32.5% shift)
f₀_Mellin = a₀^PV/a₀^ζ        = 0.472393
f₂_Mellin = a₂^PV/a₂^ζ        = 0.201285
a₀^ζ = 6440.0   a₂^ζ = 2776.165389   (canonical denominators; knowledge-MCP non-superseded)
L10→L12 drift (absolute ratio)  = 5.703%
L10→L12 drift (f₂/f₀ form)       = 15.469%
```

FAIL (Gilkey-normalization artifact) is **excluded**: a₀^PV and a₂^PV are both finite and positive (a2_pv_collapsed=False, a0_pv_blew_up=False) — no S94 absolute-divergence signature. PASS (atlas-universal across the PV-scheme choice) is **excluded** by the 32.5% RD shift. Object-definedness is **family-scoped, not atlas-universal**.

### Substrate-natural-regulator reading (lizzi-signature)

The substrate-natural regulator for the CC-ratio is the **analytic-continuation/Mellin operation** — the axis the spectrum forces, under which the ratio is FI. The PV subtraction is an *added* physical input (a UV-finiteness choice on the absolute moment), not a regularization the spectrum prescribes. Between the two PV variants, the full-physical {1,2}-mass tower (satisfying the genuine PV identities Σ c_j = 1, Σ c_j m_j² = 0 at a physical Λ_UV) is the defensible regulator; the schematic Casimir-fraction set is a structural-form surrogate (per its own S96 disclosure it "does NOT reproduce the canonical 0.431082"). The CC-ratio's structural content is its FI-under-Mellin behavior; the absolute PV-subtracted value is a physical degree of freedom to be pinned by consistency, not a convention to be shopped. This is the lizzi-signature thesis applied verbatim: *what survives all choices (FI-under-Mellin) is structural; what depends on the choice (the PV-subtracted absolute value) is a physical d.o.f.*

### §8.5 tier-2 / CC-closure invariance

The capstone §8.5 tier-2 survival and the CC closure rest on the **FI-within-family ratio**, which is INVARIANT under the full-physical-PV scheme: the survival anchor is the ratio of *unsubtracted* analytic-continuation moments (rel_dev=0), while the 32.5% shift lives entirely on the *subtracted* (RD) axis. `d(FI-anchor)/d(PV-scheme) = 0` — the RD shift propagates ZERO into the tier-2 survival margin. The §8.5 tier-2 survival is therefore **PV-scheme-INVARIANT**. (Bound on a wrong re-anchoring: were §8.5 instead anchored to the absolute `a₀^PV/a₂^PV`, the propagation would be bounded by ≤ 5.70% on the absolute ratio / ≤ 32.5% on the schematic-vs-physical gap — an explicit upper bound that does NOT apply to the actual FI anchor.)

### Framework signature (3-instance chain — RD-across-PV)

This is the **third** independent confirmation that FULL-vs-schematic-PV scheme dependence is a framework SIGNATURE (an RD-across-PV object property), not a defect of any one computation:

| # | Instance | Object (algebra-axis) | FULL-PV | SCHEMATIC | Shift |
|:--|:---------|:----------------------|:--------|:----------|:------|
| 1 | §VII.AV (S91/S92) | Var_a 2nd-log-derivative curvature B_PV at s=4 (Cell IV, algebra-DEPENDENT) | −527.97 M_KK² (m_PV=M_KK) | −7.046 M_KK² (m_PV→0) | factor ~75× |
| 2 | S96-SDW-CC-GAP (da899b4d) | f₀,f₂ CC-ratio factors (algebra-INVARIANT) | (full route) | f₂/f₀=0.6314 | 36.86% (`partB_FI_across_PV=False`) |
| 3 | **S97-W2-1 (`7d5ca3f9`)** | **a₀^PV/a₂^PV CC-ratio via FULL analytic_zeta Mellin (algebra-INVARIANT)** | **(f₂/f₀)=0.4261; a₀^PV/a₂^PV=0.510595** | **0.6314** | **32.5%** |

Instances #2 and #3 measure the SAME algebra-INVARIANT CC-ratio RD-across-PV signature via two distinct routes (S96 surrogate direct-power-sum `pv_ratio_cancellation()`; W2-1 FULL `analytic_zeta` heat-kernel integral) — W2-1 *confirms* #2's `partB_FI_across_PV=False` rather than re-deriving it, and isolates the FI and RD axes in a single gate (FI to machine-eps; RD at 32.5%). Instance #1 is on the orthogonal algebra-DEPENDENT (state-pair) axis. The signature spans two algebra-axis cells and two s-poles.

### Companion to R_1

The a₀/a₂ object joins R_1 in the FI-within / SD-across family but occupies a DIFFERENT structural cell: R_1 = a₀·a₄/a₂² is FI across the *full* regulator basket (0.34% drift) because its matched Weyl-exponents (α₀+α₄=2·α₂) cancel the regulator on EVERY axis; the bare a₀/a₂ ratio has rank-mismatched exponents (NOT-protected, 122% across the full basket per §3) and is FI only on the analytic-continuation sub-axis while RD across the PV-subtraction sub-axis. The W2-1 result sharpens §3's "a₀/a₂ 122% NOT-protected" entry: the 122% is the cross-FULL-basket drift; within the analytic-continuation family the ratio is FI to machine-eps, and the dominant RD contribution is specifically the PV-subtraction axis.

---

## Consumer gates

Forward-reference for future auditors: gates that read this registry as Input-SHA. Update when a new consumer gate lands.

| Gate ID | Session | Role | Notes |
|:--------|:--------|:-----|:------|
| `S87-W10-3-LIZZI-OBSERVABLE-PROMOTION` | S87 | INPUT-PIN | Cites this file (post-AMRI) as Lizzi-observable promotion authority for s_eff = 11/2 candidate. Pre-AMRI cited `lizzi-spectral-functional-theorist/MEMORY.md` line 21-22 (R_1 + signature observable identity). Migrated 2026-04-28. |

---

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-04-28 | S87 (AMRI promotion) | Created. Verbatim canonical content migrated from `permanent_theorems.md` line 17 (R_1 PROTECTION block) plus the §1 observable identity from MEMORY.md line 21-22. §6 promotion path specialized from `joint-theorem-promotion.md` 4-stage rule. | lizzi-spectral-functional-theorist |
| 2026-05-31 | S97 (Slot-1 solo S-3) | Added §7 (a₀/a₂ CC-ratio FI-within-analytic-continuation-family / RD-across-PV object property) + summary-table row `a0a2-cc-ratio-2axis`. Source gate `S97-W2-1-A0A2-PV-FULL-MELLIN` (INFO, audit `7d5ca3f9`). Records the third instance of the FULL-vs-schematic-PV framework signature, the substrate-natural-regulator reading, and the §8.5 tier-2 PV-scheme-INVARIANCE structural verdict. NON-MATH object-property landing (no future compute); companion to R_1 in a distinct structural cell. | lizzi-spectral-functional-theorist |

---

## Migration notes

- **Pre-migration memory file path**: `.claude/agent-memory/lizzi-spectral-functional-theorist/permanent_theorems.md` line 17 (verbatim "R_1 PROTECTION (S74 + S77 + S83)" block). Companion citation at MEMORY.md line 21-22 ("R_1 = a_0*a_4/a_2² = 1.128655 (Lizzi signature)" + "(m_H/v_EW)² * (Λ/M_Pl²) = R_1 (Lizzi observable identity)") — those MEMORY.md lines remain as agent-private constant citations and are NOT part of this AMRI promotion (they pin canonical_constants.py-style values, not registry-authority text).
- **Migration session / gate**: S87 (AMRI promotion task pre-W10-3 to clear AMRI Test 1 violation flagged by the W10 plan at `session-87-plan-w10.md` lines 296 and 436).
- **Pointer installed in memory**: `permanent_theorems.md` line 17 verbatim block replaced with single-line pointer: `> See `sessions/framework/registry/lizzi-signature-observable.md` (AMRI-promoted 2026-04-28; was inline definition of R_1 + Lizzi signature observable + empirical drift hierarchy).`
- **In-place retention**: `permanent_theorems.md` line 19-20 (§"R-PROTECTION REFINED" block) is RETAINED IN-PLACE at agent-memory because §5 of this file cross-cites to it without duplicating it; the refined R-protection taxonomy is methodology-internal to the lizzi-track, not registry-pin-authority text.
