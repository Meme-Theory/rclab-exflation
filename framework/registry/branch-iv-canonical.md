# BRANCH-IV Canonical Formulation (S86 P4 commit)

**Status**: LANDED via S86-BRANCH-IV-FORMULATION-COMMIT (W4-1, 2B path-(c)).
**Plan**: `sessions/session-plan/session-86-plan-w4.md` §W4-1.
**Working paper**: `sessions/archive/session-86/session-86-w4-workingpaper.md` §W4-1.
**Verification script**: `computations/s86_w4_p4_branch_iv_commit.py`.
**Verdict file**: `computations/s86_gate_verdicts.txt` (canonical path per `.claude/rules/gate-verdicts.md`).

**Substrate framing (mandatory per `.claude/rules/phononic-framing.md`)**: BRANCH-IV
IS the substrate's transit pathway through the van-Hove fold at `tau_fold = 0.190`.
The eigenvalue spectrum of the Dirac operator `D_K` on Jensen-deformed `SU(3)`
reorganizes at the fold; the GGE relic IS the substrate's residual coherence
pattern post-fold. `R_JK` and `xi_E_GGE_inv` are spectral functionals OF the
substrate (moments of `D_K`), NOT external probes IN spacetime. Use IS-not-IN
language throughout — `R_JK` IS the K-functional moment of `D_K` at distance-2
(NOT "lives in the K-corridor of substrate space"). The 3He-B coherence-length
spectroscopy is a parent->child inheritance (NOT an analogy) per
`.claude/agent-memory/transit-dynamics-theorist/project_3heb-inheritance.md`.

---

## §1. R_JE Retirement

**Decision**: The single-tag `R_JE` formulation is RETIRED in favor of two
distance-tagged spectral diagnostics — `R_JK` (distance-2) and `xi_E_GGE_inv`
(distance-1). The retirement is a registry-write CHANGE operation (not a
magnitude claim); no quantitative tolerance band applies.

**Rationale**: The S85-2A epsilon-pivot first-principles audit and the S85-2B
BRANCH-IV-asymmetry audit (both in `sessions/archive/session-85/`) identified
single-name conflation between distance-1 and distance-2 spectral tags inside
the prior `R_JE` formulation. `R_JE := xi_J / xi_E_GGE` (E-coupled,
GGE-energy-weighted) was a single-distance-tag ratio that conflated the
K-functional structure (distance-2 / Newton-constant slot) with the
GGE-coherence-length structure (distance-1 / s=-1 Mellin residue).

**S85 evidence (anchor SHAs from `computations/s85_gate_verdicts.txt`)**:

| S85 verdict | Evidence | content_sha256 (first 16) | audit_sha256 (first 16) |
|:------------|:---------|:--------------------------|:------------------------|
| `S85-W12-ELIM-1: PASS` | BRANCH-IV reaudit L_max trajectory `D_iv8=-0.988704, D_iv10=-0.991965, D_iv12=-0.994010`; signs `(-1, -1, -1)`. R_JK `[0.01129619, 0.00803461, 0.00598992]` at L_max in {8, 10, 12}. Inverted Josephson dominance proven on Jensen-deformed SU(3) Dirac. | `dad2afb06775af65` | `08cf848edcce08ba` |
| `S85-W12-ELIM-3: FAIL` | Catalog-extension equivalence-class disjoint check: 1 of 0.089286 (FAIL — single-name-conflation witness). | `c37eee4d02688c03` | `e77860d65a2cfb32` |
| `S85-W12-ELIM-6: FAIL` | Plan-layer PRDR four-valued predicate `(6248, 14, 0, 0)`: FAIL — two further single-name-conflation rows landed. | `c7b54124f8f2c50d` | `6a009c7b3c5fb528` |
| `S85-W12-ELIM-8: PASS` | Regulator-invariance taxonomy across the 5-regulator atlas W0: `(n_a=13, n_b=0, n_c=0, n_d=3)`. Confirms BRANCH-IV diagnostics survive the regulator-class scan. | `8221f24ff998c296` | `d9c4bc06ee2d5154` |

S85 W12-ELIM-1 PASS provides the L_max-trajectory anchor. S85 W12-ELIM-3
FAIL + W12-ELIM-6 FAIL document the single-name-conflation pattern that
necessitates the 2B path-(c) commit. `R_JE` therefore retires; downstream
references should cite `R_JK` (distance-2) or `xi_E_GGE_inv` (distance-1)
explicitly, never the legacy single-tag.

**Substrate-IS-language statement**: The retirement IS canonical splitting in
the substrate's spectral-functional ledger — TWO distance-tagged moments of
`D_K` REPLACE the conflated single-tag ratio. The substrate's transit pathway
through the fold is unchanged; only the diagnostic cardinality at
distance-resolved level has been corrected from 1 to 2.

---

## §2. R_JK (K-functional, distance-2)

**Canonical name**: `R_JK` (Python identifier in
`computations/canonical_constants.py` SECTION E.B). NOT `R_JE`. NOT
`R_JK_corridor`.

**Numerical anchor** (at L_max = 10, S85-W12-ELIM-1 PASS, full float64):
```
R_JK = 0.00803460529503449     (dimensionless ratio, M_KK-natural units)
```
Cross-check identity (loaded-vs-anchor) tolerance: rel_tol = 1e-12 per
`.claude/rules/epistemic-discipline.md` §"Publication-Precision Pre-Registration"
(pub_sig_figs = 15).

**Formula** (per gen-physicist 9A §4.6 substitution chain):

```
R_JK := Tr_F( chi_K(D_K) * D_K^{-2} )                 (general)
      = (sigma_J * |Delta_BCS|^2) / (sigma_K * K_base) (substrate-natural reduction)
      = (a_4 / a_2) * (|Delta_BCS|^2 / K_base)
```

where:

| Symbol | Definition | Value | Unit |
|:-------|:-----------|:------|:-----|
| `sigma_J` | `Tr[D_K^{-4}] / Vol_SU3` (= a_4 spectral moment) | 0.01199366 (L_max=10) | M_KK^{-4} |
| `sigma_K` | `Tr[D_K^{-2}] / Vol_SU3` (= a_2 spectral moment) | 0.15810134 (L_max=10) | M_KK^{-2} |
| `Delta_BCS` | Canonical BCS gap (R-protected, S70 BCS-GAP-CANONICAL-70) | 0.4642547394830737 | dimensionless |
| `K_base` | R3 band-weighted squeezing anchor (= K_corridor; S82 W2-4) | 2.035 | dimensionless |
| `Vol_SU3` | Weyl-Haar SU(3) integration volume | 1349.7399583199533 | dimensionless |
| `chi_K` | K-functional character (corridor-localized weighting at K = K_corridor) | (functional) | dimensionless |

**L_max-INDEPENDENT prefactor**: `|Delta_BCS|^2 / K_base = 0.10591275829606715`
(Delta_BCS and K_base are pinned canonical constants, not regulator-truncated
moments).

**Distance tag**: 2 (the K-functional `R_JK` enters the spectral-action ledger
at the second moment a_2; substrate-distance-2 corresponds to the
Newton-constant slot in the Seeley-DeWitt expansion).

**Substrate-IS-language statement**: `R_JK` IS the K-functional moment of
`D_K` at distance-2. The K-functional character `chi_K` IS the
corridor-localized weighting of the spectral action at `K = K_corridor`
(= `K_base` = 2.035). `R_JK` does NOT live "in" a K-corridor of substrate
space; rather, the K-corridor IS the locus where `chi_K` weights the
spectral content.

**L_max trajectory** (from `computations/session-85/s85_w12_elim1_D_K_Lmax_moments.npz`; path corrected from the stale `computations/artifacts/` citation 2026-06-07 per S100b W1-4 §A housekeeping flag — artifacts copy verified ABSENT, session-85 copy is the on-disk canonical):

| L_max | a_2 | a_4 | R_JK | D_iv = R_JK − 1 | sign |
|:------|:----|:----|:-----|:----------------|:-----|
| 8 | 0.0950613 | 0.01013882 | 0.01129619 | -0.98870381 | -1 |
| 10 | 0.15810134 | 0.01199366 | **0.00803461** | -0.99196539 | -1 |
| 12 | 0.24437807 | 0.01382087 | 0.00598992 | -0.99401008 | -1 |

The L_max=10 anchor (`R_JK = 0.00803461`) is the canonical landing value;
L_max=8 and L_max=12 entries document the trajectory's monotone decrease
(`R_JK` decreases as `L_max` increases), with `D_iv := R_JK − 1` strictly
bounded below 0 across the trajectory.

**Cross-cite**: connes-ncg-theorist for the Seeley-DeWitt a_4/a_2 spectral-
action moment derivation (Connes-Chamseddine spectral-action convention;
distance-2 corresponds to the second moment in the heat-kernel Mellin
expansion).

---

## §3. xi_E_GGE^{-1} (s=-1 spectral diagnostic, distance-1)

**Canonical name**: `xi_E_GGE_inv` (Python identifier in
`computations/canonical_constants.py` SECTION E.B). This is the
identifier-safe ASCII form of `ξ_E_GGE^{-1}`.

**Numerical anchor** (substrate-natural, full float64):
```
xi_E_GGE_inv = 13.642473425595973     (in M_KK units; intensive)
             = N_pair_GGE * Delta_BCS / K_base
             = 59.8 * 0.4642547394830737 / 2.035
```
Cross-check identity (loaded-vs-anchor) tolerance: rel_tol = 1e-12 per
`.claude/rules/epistemic-discipline.md` §"Publication-Precision Pre-Registration"
(pub_sig_figs = 15).

**Formula** (per lizzi 9A §2.2 / Mellin-strip convention):

```
xi_E_GGE^{-1} := lim_{s -> -1} zeta_{D_K^(GGE)}(s)
              = (analytic continuation) Sum_n lambda_n^(GGE)
```

where `D_K^(GGE)` is the post-fold GGE-restricted Dirac operator — `D_K`
projected to the 59.8-pair Parker-production sector per the S38 GGE
permanence theorem. The Mellin-strip convention is Connes-Chamseddine
spectral-action with analytic continuation past s = -1; the s = -1 residue
is the first non-trivial Mellin-strip residue below s = 0 (hence
**distance-1** tag).

**Substrate-natural anchor decomposition**:

| Symbol | Definition | Value | Unit |
|:-------|:-----------|:------|:-----|
| `N_pair_GGE` | Parker-pair production count (S38 GGE permanence theorem) | 59.8 | dimensionless count |
| `Delta_BCS` | Canonical BCS gap (S70 BCS-GAP-CANONICAL-70, R-protected) | 0.4642547394830737 | M_KK (eigenvalue) |
| `K_base` | R3 band-weighted squeezing anchor (corridor-localized weighting) | 2.035 | dimensionless |
| `lambda_GGE_avg` | GGE-weighted average eigenvalue (= Delta_BCS / K_base) | 0.22813 | M_KK |
| `xi_E_GGE_inv` | s=-1 zeta residue (= N_pair_GGE * lambda_GGE_avg) | 13.640957 | M_KK |

The dominant contribution to the s = -1 residue is the GGE-weighted sum over
the 59.8-pair sector, yielding `xi_E_GGE_inv ≈ N_pair_GGE * <lambda_GGE>`
where `<lambda_GGE> = Delta_BCS / K_base` is the substrate-natural mean
eigenvalue (BCS gap weighted by the corridor-localized K_base). This
substrate-natural anchor is the canonical S86-W4-1 P4 commit value; future
work that performs full GGE eigenvalue diagonalization may refine this
anchor (the canonical entry is overwritable via `update_constant` MCP if
that refinement lands).

**Distance tag**: 1 (first non-trivial Mellin-strip residue below s = 0;
substrate-distance-1 corresponds to the s = -1 slice of the spectral zeta
function).

**3He-B parent->child inheritance** (per
`.claude/agent-memory/transit-dynamics-theorist/project_3heb-inheritance.md`):
The 3He-B coherence-length-inverse spectroscopy (Volovik QFL Fig. 5.3) is
NOT an analogy. It is the parent of the substrate's `xi_E_GGE_inv` via the
universality-class inheritance map. The 3He-B order parameter sources the
parent coherence-length spectrum; the substrate's GGE-projected zeta residue
inherits as the child via the parent->child correspondence. The lab system
provides the observational template; the substrate provides the underlying
spectral-triple structure that is logically prior.

**Substrate-IS-language statement**: `xi_E_GGE_inv` IS the s=-1 spectral
residue moment OF the GGE-projected `D_K`. The GGE relic IS the substrate's
residual coherence pattern post-fold (NOT an excitation IN a vacuum).
`xi_E_GGE_inv` is one moment of that pattern at the s=-1 Mellin slice.

**Cross-cite**: volovik-superfluid-universe-theorist for the 3He-B
parent->child inheritance template (Volovik QFL Ch. 5; coherence-length-
inverse spectroscopy as the lab observational anchor for the substrate's
s=-1 spectral diagnostic).

---

## §4. Provenance + Cross-cite Ledger

### Plan + workshop sources
- `sessions/session-plan/session-86-plan-w4.md` §W4-1 (machinery pin,
  thresholds, 5 CC, framework-file edits, canonical-constants registration).
- gen-physicist 9A §4.6 — `R_JK` formula source (K-functional substitution
  chain at distance-2; Newton-constant slot identification).
- lizzi 9A §2.2 — `xi_E_GGE_inv` formula source (s=-1 Mellin-strip residue
  convention; substrate-distance-1 tag rationale).

### Canonical constants used (from `computations/canonical_constants.py`)
- `M_KK = 7.428660036284456e+16` (gravity route; S42 KK-CANONICAL).
- `Delta_BCS = 0.4642547394830737` (S70 BCS-GAP-CANONICAL-70; R-protected).
- `K_base = 2.035` (S82 W2-4 PS-SUBSTRATE-MATCHED-IC R3 band-weighted
  squeezing anchor; identified with `K_corridor` at the substrate's
  K-corridor locus).
- `Vol_SU3 = 1349.7399583199533` (Weyl-Haar SU(3) integration volume).
- `tau_fold = 0.190` (van Hove fold position).

### Anchor cache
- `computations/session-85/s85_w12_elim1_D_K_Lmax_moments.npz` — S85
  W12 BRANCH-IV reaudit moments cache. Provides L_max-trajectory anchor
  for `R_JK` and Delta_BCS / K_base ratio for `xi_E_GGE_inv`.
  (Path corrected 2026-06-07 from the stale `computations/artifacts/`
  citation per the S100b W1-4 §A housekeeping flag: artifacts copy
  verified ABSENT on disk; `computations/session-85/` is the canonical.)

### S85 verdict-file SHAs (from `computations/s85_gate_verdicts.txt`)
- W12-ELIM-1 PASS: content `dad2afb06775af65`, audit `08cf848edcce08ba`.
- W12-ELIM-3 FAIL: content `c37eee4d02688c03`, audit `e77860d65a2cfb32`.
- W12-ELIM-6 FAIL: content `c7b54124f8f2c50d`, audit `6a009c7b3c5fb528`.
- W12-ELIM-8 PASS: content `8221f24ff998c296`, audit `d9c4bc06ee2d5154`.

### Cross-cited specialists
- **transit-dynamics-theorist** (primary for this commit): BRANCH-IV is the
  substrate's transit pathway through the van-Hove fold; specialist's home
  domain (Bogoliubov coefficients, mode equations in time-dependent
  backgrounds, GGE formation post-quench).
- **volovik-superfluid-universe-theorist** (cross-cite for `xi_E_GGE_inv`):
  3He-B parent->child inheritance template (Volovik QFL Fig. 5.3
  coherence-length-inverse spectroscopy).
- **lizzi-spectral-functional-theorist** (Mellin-strip convention author):
  s=-1 residue extraction convention (W2 C9/C10 Mellin-cone work; ZETA-NOT-
  PHYSICAL-75 closure).
- **connes-ncg-theorist** (Seeley-DeWitt a_4/a_2 author): K-functional
  spectral-action moment (distance-2 / Newton-constant slot identification).

### Project memory cross-cites
- `project_3heb-inheritance.md` — correspondence is parent->child, not
  analogy.
- `project_volovik-convergence.md` — framework independently rediscovered
  Volovik's program; 3He-B is the canonical lab anchor.
- `feedback_agent-roster.md` — weight Volovik's reviews
  highest.

### Downstream unlock
- **W5a P3** (`S86-SECTOR-1-SR-FLOW-Z-FACTOR`): becomes runnable on PASS.
  Per partition §3 sequencing row "W4 (P4) -> W5 (P3 SECTOR-1 xi^2(0) IC)":
  Sector-1 `xi^2(0)` initial condition sources from `xi_E_GGE_inv` (the
  registry-pinned substrate-distance-1 diagnostic). P3 cannot integrate the
  (epsilon, eta, alpha_s, xi^2) ODE from N=0 fold IC until xi^2(0) is
  sourced from a registry-pinned diagnostic; this commit provides that
  pin.

---

## §S86 P4 Commit Audit Trail

This section is appended on every successful re-commit (idempotent; the
verification script appends a new audit row to the verdict file but does
NOT overwrite this framework file).

- **2026-04-26**: Initial S86-W4-1 P4 commit. Verdict line + dual-SHA in
  `computations/s86_gate_verdicts.txt`. R_JE retired; R_JK + xi_E_GGE_inv
  landed at SECTION E.B in `canonical_constants.py`. Verification script:
  `computations/s86_w4_p4_branch_iv_commit.py`.
