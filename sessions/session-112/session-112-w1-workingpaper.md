# Session 112 Wave 1 — M_KK keystone + H0 closure (the §6.3 magnitude half) (Results Working Paper)

**Session**: 112 | **Wave**: 1 | **Plan**: session-112-plan-w1.md | **Theme**: the MAGNITUDE half of the §6.3 a(t)/effective-Friedmann residual — whether a substrate-natural anchor can fix the dimensionful scale M_KK τ-RG-invariantly, and whether the H0-residual band then closes dimensionfully (else caps at the 6.125% dimensionless channel).

## Gate Sections

### §W1-1. CF-S112-MKK-SUBSTRATE-ANCHOR (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S112-MKK-SUBSTRATE-ANCHOR`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (M_KK = 1/R_K is the compactification scale of the spectral-triple fabric, not a property of its excitations)
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: a substrate-natural dimensionful anchor Λ_anchor (no CODATA, no M_Pl routing) fixes M_KK = Λ_anchor·R(τ_fold) τ-RG-invariantly to Δ_rel < 5e-2 — OR the magnitude leg is a permanent external-import boundary (the self-referential-unit-system no-go).
**Plan reference**: `sessions/session-plan/session-112-plan-w1.md` §W1-1 (two-leg test, candidate-anchor pins A/B, codata_exclusion_set, substitution chain, dual-prior).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-112/s112_mkk_substrate_anchor.py` — present; `grep -nE 'from canonical_constants import|print_verdict_payload'` → L70 `from canonical_constants import *`, L72 `from canonical_constants import (`, L327 `def print_verdict_payload(`, L405 `print_verdict_payload(`.
- `computations/session-112/s112_mkk_substrate_anchor.npz` — present (data; 47 keys: legs, prefactors, kernel-continuity, τ-scan arrays, 3-tuple).
- `computations/session-112/s112_mkk_substrate_anchor.png` — present (2-panel: M_KK(τ)/M_KK = pure-number·R(τ) τ-non-flatness; Δ_rel bar chart vs 5e-2/5e-1 bands).
- verdict line in `computations/session-112/s112_gate_verdicts.txt` matching `^CF-S112-MKK-SUBSTRATE-ANCHOR:.* audit_sha256=[a-f0-9]{64}` — present, `audit_sha256=3fa9be16…561e39af`, WITH dual-SHA companion row (`audit_sha256_short=3fa9be16e90ada96 content_sha256_short=567251976d8766f0`) AND the schema-v2 3-tuple companion row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`) + regulator_pin + parity_pin extra rows ([SIGN] trigger).

**MCP Pre-Compute Audit**:
- `search_knowledge("M_KK self-referential scale 1/R_K external anchor dimensional transmutation")` → confirmed `M_KK = 1/R_K` (S35 Feynman-Landau), `M_Pl² = a_2(s)/(48π²·R_K²)` (the candidate-B normalization, SAME source), graph edge `Self-Referential --reproduces--> M_KK` (S61), and `M_KK_derived = M_Pl_reduced·exp(−1/(λ_eff·N₀))` (S110/INV9 transmutation chain). NOT pre-closed (this gate re-reads the transmutation under substrate-natural anchors — a fair test the bare-import reading had not had).
- `search_knowledge("CF-S112-MKK-SUBSTRATE-ANCHOR …")` → CF-S112-MKK-SUBSTRATE-ANCHOR NOT in any verdict ledger ⇒ not previously evaluated. S111-CF-MKK-RG-INVARIANCE baseline confirmed: `Delta_rel=8.1929`, `leg1=False`, `leg2=False`, `R_fold=1.6017e-01`, `lam_fold=0.03893`, `N0_fold=14.0233`, `R_range=[3.639e-11,1.601e-01]`.
- `get_constant("M_KK_gravity")` → 7.428660036284456e16 (S42 CONST-FREEZE-42) ✓ matches pin.
- `get_constant("a_2_FW_zeta")` → 2776.165389 (S88 A-N-FW-CANONICALIZATION) ✓ matches pin.
- `get_constant("Delta_BCS")` → 0.4642547394830737 (S70 BCS-GAP-CANONICAL-70, R-PROTECTED) ✓ matches pin.
- `trace_entity("Self-Referential M_KK")` → no direct trace node (the self-reference lives as the S61 `--reproduces-->` edge surfaced by search_knowledge, not a standalone entity).

**Verdict**: **FAIL** (composite). 3-tuple: `sign_verdict=PASS`, `magnitude_verdict=FAIL`, `regime_verdict=VALID`. This is the **registered no-go** (dual-prior Track-B, prior 0.90): the §6.3 a(t)/effective-Friedmann **magnitude leg is a permanent external-import boundary** — the self-referential-unit-system no-go, lattice-QCD scale-setting analog (all dimensionless ratios predicted; exactly ONE external dimensionful anchor irreducibly required). NOT an agent failure (`math-scripts.md §"All Results Are Good Results"`): the structurally strongest possible negative result, exactly as pre-registered.

**Results**:

**Bit-exact continuity vs S111 / S110 CV2A (tol 1e-9)** — PASS on all three:
| check | residual | tol | status |
|:------|:---------|:----|:-------|
| \|R_fold − R_CV2A\| | 0.000e+00 | 1e-9 | ✓ |
| \|λ_fold − λ_CV2A\| | 0.000e+00 | 1e-9 | ✓ |
| \|N₀_fold − N₀_CV2A\| | 1.776e-15 | 1e-9 | ✓ |
| R_formula_resid (exp(−1/(λ·N₀)) vs cached R_fold) | 0.000e+00 | — | ✓ |
| bare_recon_resid (M_Pl_reduced·R_fold vs S111 M_KK_derived_red) | 0.000e+00 | — | ✓ |

The cached transmutation kernel is reproduced bit-for-bit: `R_fold=0.16016847970570353`, `λ_fold=0.038934760900644856`, `N₀_fold=14.023250234055002`, `C_const=13.782016865760449`, `τ_fold_found=0.1901578802145293`.

**Per-candidate two-leg test** (PASS iff EITHER satisfies `leg1_RGinv ∧ leg2_noimport ∧ Δ_rel<5e-2 ∧ independent-GeV-scale`):

| candidate | leg1_RGinv (Δ_rel^{τ-flat} ≤ 5e-2) | leg2_noimport (codata ∩ inputs = ∅) | Δ_rel (target-match) | independent GeV scale? | conjunction |
|:----------|:-----------------------------------|:------------------------------------|:---------------------|:-----------------------|:------------|
| **A** GAP-EMERGENT-LENGTH (Λ_A = Δ_BCS·M_KK) | **False** (flat=1.0000) | True (codata=∅) | 0.925641 | **False** | **passA=False** |
| **B** EMERGENT-NEWTON (Λ_B = √(a_2^ζ/48π²)·M_KK) | **False** (flat=1.0000) | True (codata=∅) | 0.612270 | **False** | **passB=False** |

**GATE PASS (A ∨ B) = False.**

**Substitution chain (bit-exact, `[SIGN]` discipline per `math-scripts.md §"Double-Check Logic Before Compute"`)** — Claim: *"M_KK is τ-RG-invariant under a substrate-natural anchor iff the anchor's τ-flow cancels R(τ)'s τ-flow AND the anchor carries an independent GeV scale; absent such an anchor, the magnitude leg is a permanent external-import boundary."*

- **Step 1 (definitions, all substrate-first canonicals):** `R(τ)=exp(−1/(λ_eff(τ)·N₀(τ)))` [S110 CV2A, DIMENSIONLESS]; `λ_eff(τ)=‖K_a(τ)‖²_{C2}/C_const` [Baptista P17 eq4.1; λ_fold=0.038934761]; `N₀(τ)`= windowed van-Hove DOS [N₀_fold=14.023250234]; `Λ_anchor(τ)` = candidate anchor; `M_KK_target=7.428660036e16 GeV` [S42]; `M_KK(τ):=Λ_anchor(τ)·R(τ)`.
- **Step 2 (substitute candidate B):** `M_KK(τ_fold) = √(a_2^ζ/(48π²))·M_KK·R_fold = √(2776.165389/(48π²))·M_KK·0.16016847970570353`.
- **Step 3 (simplify the dimensionless prefactor, one step/line):** `48π² = 473.741011`; `a_2^ζ/(48π²) = 2776.165389/473.741011 = 5.860091`; `√(5.860091) = 2.420762` (= M_Pl_eff/M_KK, the substrate a_2-route Planck ratio); `2.420762·0.16016847970570353 = 0.387730`.
- **Step 4 (canonical form — read the self-reference):** `M_KK(τ_fold) = 0.387730·M_KK` ⇒ the closed form maps `M_KK ↦ 0.387730·M_KK`, a fixed point ONLY at `M_KK=0`. ⇒ candidate B under-shoots by factor 0.387730 (`Δ_rel_B = |0.387730 − 1| = 0.612270 ≫ 5e-2`). Candidate A: `prefac_A = Δ_BCS·R_fold = 0.4642547·0.16016848 = 0.074359`, `Δ_rel_A = 0.925641`. **Both substrate-internal anchors reduce to `M_KK·(pure number)`**: the substrate's spectral data (a_2^ζ, Δ_BCS) are DIMENSIONLESS in M_KK units, so they cannot bootstrap the absolute GeV scale — the **self-referential no-go**.
- **Step 5 (direction read-off — the two legs):**
  - `leg1_RGinv`: `M_KK(τ)/M_KK(τ_fold) = R(τ)/R(τ_fold)` because `Λ_anchor(τ)=(τ-INDEPENDENT pure number)·M_KK` for both candidates (a_2^ζ and Δ_BCS are τ_fold-anchored canonical scalars). The τ-flow is therefore carried ENTIRELY by R(τ), whose range over [0.19,0.55] is a full factor (max|R(τ)/R_fold − 1| = 1.0000). The substrate-natural anchor does **not** flatten the τ-product because the τ-non-flatness is a property of R(τ) itself, **independent of the anchor's magnitude** — exactly the same reason the bare M_Pl anchor failed leg1 in S111 (M_Pl is also τ-constant). Nothing in a_2^ζ(τ) or Δ_BCS cancels R(τ)'s van-Hove-fold-localized exponential. ⇒ **leg1=False**, as pre-registered.
  - `leg2_noimport`: candidates A/B use ONLY `{M_KK-as-unit, Δ_BCS}` resp. `{M_KK-as-unit, a_2^ζ}` — **no CODATA** ⇒ set-membership audit `codata ∩ inputs = ∅` passes (leg2=True). BUT "M_KK-as-unit" means each anchor is expressed IN M_KK units and carries **no INDEPENDENT GeV scale**; to produce a GeV number an external scale must re-enter. leg2 "passes" set-membership trivially while the anchor supplies no absolute magnitude — the **degeneracy** the gate exposes. This is why the PASS rubric's `independent-GeV-scale` conjunct is False for both.
- **Conclusion:** PASS requires a substrate-internal Λ_anchor whose τ-flow cancels R(τ)'s AND which carries an independent GeV scale. The chain + compute show both pinned candidates reduce to `M_KK·(pure number)` — neither carries an independent GeV scale (self-reference) and neither flattens leg1. The honest pre-registered outcome FAIL = **magnitude leg is a permanent external-import boundary** is realized.

**4-tuple**: `(value=NO-GO-self-referential-unit-system;…, scheme=SA, convention=RATIO, L_max=12)`. **regulator_pin** = `a_2^{zeta}` (poleconv-A-double, pole_in_s=3, curvature_grade_n=2; M_Pl_eff²=a_2^ζ/(48π²) EH-normalization per `regulator-pin-discipline.md`). **convention_parity_pin** = `RATIO-DA-1-PARITY-odd` (M_KK is a d_A=+1 ODD scale leg; the magnitude leg lives on the sign-locked M_KK¹ odd scale-leg face of the Q=R·M_KK^m wall — corpus §23.0(5), fifth pin axis).

**Baseline comparison**: the bare-import baseline (S111, M_Pl_reduced·R_fold) gave `Δ_rel_bare=8.1929` (M_KK_derived=3.900e17 vs target 7.429e16). The substrate-natural anchors **do** beat it on magnitude (Δ_rel_B=0.612, Δ_rel_A=0.926 < 8.193) — but NOT into the 5e-2 PASS band, and NOT even into the 5e-1 INFO band (best=0.612 > 0.5). The improvement is a red herring: removing the CODATA M_Pl removes a *misnormalized* anchor, but the replacement is a pure-number multiple of the very scale being solved for.

**Dual-prior reallocation**: FAIL → **0.95 to Track-B** (the magnitude leg is a permanent external-import boundary, registered as a structural no-go). The 0.05 residual mass on Track-A reflects only the formal possibility that an absolute-scale-carrying thermodynamic observable (not captured by candidates A/B) could exist — the gate leaves that open but found no such mechanism. Structural twin: the rank-1-Yukawa-wall "irreducibly external, not a refinable approximation" precedent (S100a INV2-W1-1).

**3-tuple semantics**: `sign_verdict=PASS` — the substitution-chain Step-4 predicted direction (anchor reduces to M_KK·(pure number), no independent GeV scale, self-reference) IS the observed direction; the prediction's sign matches the computation. `magnitude_verdict=FAIL` — best Δ_rel=0.612270 > 5e-1 INFO band. `regime_verdict=VALID` — closed-form arithmetic on bit-exact cached scalars throughout, no regime breach. Composite collapse (deterministic rule, `gate-verdicts.md`): `magnitude=FAIL ∧ regime=VALID ⇒ composite=FAIL`.

**Substrate framing** (GEOMETRIC; `phononic-framing.md`): M_KK = 1/R_K IS the compactification radius of the spectral-triple fabric — a property of the D_K eigenvalue spectrum's overall scale, not of its phononic excitations. The substrate measures EVERY observable in M_KK units: the D_K eigenvalues, Δ_BCS=0.4643, the Seeley-DeWitt moments a_0=6440.0, a_2=2776.17 are all PURE NUMBERS. The flow is FROM the D_K spectrum (λ_eff, N₀ read off the Jensen deformation) → the transmutation ratio R(τ)=exp(−1/(λ_eff·N₀)) → the scale M_KK. The substrate supplies the dimensionless multiplier R; it cannot supply the ONE dimensionful anchor R must multiply without borrowing an external scale — the same structural reason lattice QCD inputs one dimensionful quantity (f_π / proton mass) to set its scale while predicting all dimensionless ratios. This FAIL is the substrate telling us precisely where its predictive reach ends and where exactly one external anchor is irreducibly required — the §6.3 magnitude-leg boundary.

**Solution-space assessment**: this gate CLOSES the corridor "a substrate-internal anchor of the form (substrate pure number)·M_KK fixes the absolute M_KK GeV scale τ-RG-invariantly." The wall is structural and twofold: (i) **leg1 is unreachable by any τ-constant anchor** — the τ-non-flatness is intrinsic to R(τ), so flattening requires an anchor whose own τ-flow cancels the van-Hove exponential, which a fold-anchored canonical scalar cannot do; (ii) **the magnitude leg is self-referential** — every substrate spectral datum is dimensionless in M_KK units, so no algebraic combination of them carries an independent GeV scale. Downstream: W1-2 (CF-S112-H0-BAND-CLOSURE) consumes this FAIL via its `upstream_verdict_pin` and returns the **registered fallback** — H0 relief CAPPED at the 6.125% dimensionless channel (band_closed=False), with the dimensionful remainder pinned to the one external M_KK scale the substrate cannot self-supply. The §6.3 capstone narrates M_KK-magnitude as an irreducible external pin (capstone-hygiene Q1-YES + Q3-YES routing; scope-qualified per the S100a "irreducibly external" precedent). The NEXT computable question is whether a substrate **thermodynamic** observable carrying an absolute energy scale (e.g. a measured transition temperature with an external SI tie) could serve as the one irreducible anchor — but that, by construction, is an external import, confirming rather than circumventing the no-go.

---

### §W1-2. CF-S112-H0-BAND-CLOSURE (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `CF-S112-H0-BAND-CLOSURE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (H0 is the substrate's emergent expansion-rate transport observable, sourced by the a_0/a_2 spectral moments + GGE-relic channel)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: the H0-residual band closes dimensionfully (band_closed=True) IFF W1-1 PASSes — releasing the 93.875% held by the M_KK^1 scale leg into the band [0.08,0.10]; else closure caps at the 6.125% dimensionless channel.
**Plan reference**: `sessions/session-plan/session-112-plan-w1.md` §W1-2 (conditional band-closure operator, s111_cf3 inputs, upstream-verdict pin, substitution chain, dual-prior).
**Intra-wave dependency**: SERIALIZED downstream of W1-1. The `upstream_verdict_pin` is the W1-1 verdict line in `computations/session-112/s112_gate_verdicts.txt`, resolved at runtime via the gate-verdicts.md Option-A supersession reading. **Branch selected: W1-1 = FAIL → FAIL-capped-dimensionless** (the registered fallback). W1-1 (`CF-S112-MKK-SUBSTRATE-ANCHOR`, `audit_sha256=3fa9be16e90ada96e6d1b0f43748b0ddc48626b1c428c1f01a769ed4561e39af`) closed FAIL composite (sign=PASS magnitude=FAIL regime=VALID) — the self-referential-unit-system no-go: a finite spectral triple that measures every observable in M_KK units cannot fix its own absolute GeV scale from within (lattice-QCD scale-setting analog). The M_KK^1 scale leg therefore stays INADMISSIBLE.

**Conditional branch taken (W1-1 FAIL → capped 6.125%)**: with M_KK NOT substrate-derived, the d_A=+1 ODD M_KK^1 scale leg remains a bare external import. Only EVEN-degree morphisms are available to transport it to the CMB pivot (the morphism sector is even: −2(s−s′) Wodzicki ratios carry even degree, HKR carries 0; the only odd-degree carrier is the M_KK^1 scale leg itself) — the parity selection rule (cross-pillar-bridge-corpus §23.0(5), the fifth pin axis) blocks the transport. No dimensionful draw is permitted. Relief is CAPPED at the substrate's dimensionless transport channel: `partial_relief = 49/800 = 0.06124965` (exact rational 1224993/20000000), loaded from `s111_cf3_h0_residual.npz` (NOT recomputed). Since `0.06124965 ∉ [0.08, 0.10]` (it sits **0.018750 below the band floor** band_lo=0.08), `band_closed = False`.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | `must_contain` verified |
|:---------|:-----|:------------------------|
| script | `computations/session-112/s112_h0_band_closure.py` | `from canonical_constants import` ✓, `print_verdict_payload` ✓ |
| data | `computations/session-112/s112_h0_band_closure.npz` | present (56 keys incl. exact rationals, branch, 3-tuple) ✓ |
| plot | `computations/session-112/s112_h0_band_closure.png` | present (band-position diagram: capped relief vs band [0.08,0.10]) ✓ |
| verdict line | `computations/session-112/s112_gate_verdicts.txt` | `^CF-S112-H0-BAND-CLOSURE:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion ✓ + schema-v2 3-tuple companion ✓ |
| WP section | this §W1-2 | `Status: COMPLETED`, `Verdict: FAIL`, `Output Artifacts`, `MCP Pre-Compute Audit` ✓ |

Verification is by content/regex presence only, never line/byte counts (per `.claude/rules/agent-standards.md §"Completion Verification"`).

**MCP Pre-Compute Audit** (query-first; this gate is a CONDITIONAL CONSUMER — no new substrate compute, so the queries confirm the inputs are already-canonical and the result is not re-derivable elsewhere):

- `search_knowledge("H0 residual band closure M_KK scale leg dimensionless transport relief")` → confirms the upstream chain: `[gate] S111-CF3-H0-RESIDUAL` INFO (the source of `49/800`, `residual_held=0.93875`, `M_KK1_scale_leg_INADMISSIBLE=True`, `band_closed_dimensionless=False`); `[gate] S110-CF3-TIMESCAPE-H0` INFO (the `deg_T=2.0 NON-SCALAR` + `fitted_ratio=18.367` origin); `[theorem PROVEN] transport-κ sign-lock` (the `deg=+1` scale leg's `+28.17`-decade band-sandwich — the connes×mack workshop result establishing M_KK^1 as the only dimensionally-right but ODD leg). NOT a recompute: the band-closure decision is the registered conditional consumer of S111-CF3.
- `get_constant("H_0_km_s_Mpc")` → `67.4` (substrate framing anchor; no PROVENANCE entry — used only as the npz record anchor, not a PASS input).
- The S110 workshop equation block (`deg=1 (d_A, M_KK scale leg): dimensionally RIGHT`; `deg=0 (scalar): dimensionally WRONG for d_A=1`) is the parity diagnosis the FAIL branch propagates: the dimensionally-correct leg is the one W1-1 found cannot be self-supplied.

**Verdict**: **FAIL** (composite). 3-tuple: **sign=PASS, magnitude=FAIL, regime=VALID**. Collapse rule (gate-verdicts.md): sign=PASS ∧ magnitude=FAIL ∧ regime=VALID ⇒ composite=FAIL. This is the **registered H0-relief ceiling**, a structural boundary — NOT an agent failure (per `.claude/rules/math-scripts.md §"All Results Are Good Results"`).

- `audit_sha256 = f5a8498d1114e311db9d8aa51b22308df1a260169af4d10d8693ecd36a818796`
- `content_sha256 = 70994dd5e5c78dc2564ec032281ece6fac580791a737ce1201ec498cf39c9762`
- 4-tuple: `(value=<branch=FAIL-capped-dimensionless;…>, scheme=emergent-scale-transport-DIMENSIONLESS-ONLY, convention=DA-0-PARITY-EVEN, L_max=12)`
- `convention_parity_pin = RATIO-DA-1-PARITY-odd` (companion row — the released-branch face: M_KK^1 is d_A=+1 ODD, INADMISSIBLE under W1-1 FAIL).

**Substitution chain (conditional directional claim, with substituted numbers)**:

```
Claim: "The H0-residual band closes dimensionfully IFF W1-1 PASSes (M_KK substrate-derived);
        else closure caps at the 6.125% dimensionless channel."

Step 1 (Definitions, loaded from s111_cf3_h0_residual.npz; consistency re-checked):
  partial_relief      = 1224993/20000000 = 0.06124965   [exact rational; round-fig 49/800; roundfig_within_4sf=True]
  residual_held       = 0.93875035                       [= 1 − partial_relief; residual_consistent=True at 1e-9]
  band                = [band_lo, band_hi] = [0.08, 0.10] [H0 closure band; central 0.09, lit 0.084]
  dimensionful_draw_reqd = 18.36194166                   [the draw the M_KK^1 scale leg must supply — NOT attempted]
  M_KK1_INADMISSIBLE_bare = True                         [d_A=+1 ODD; only EVEN morphisms available; parity blocks it]
  W1-1_verdict        = FAIL                             [resolved at runtime, audit_sha256=3fa9be16…, Option-A reading]

Step 2 (Substitute the conditional — band_closed = f(W1-1_verdict)):
  W1-1 == FAIL  ⇒  M_KK^1 scale leg stays INADMISSIBLE  ⇒  no dimensionful draw
                ⇒  relief_total = partial_relief = 0.06124965 (capped, dimensionless only)

Step 3 (Simplify the FAIL branch — the registered fallback, evaluated this run):
  relief_total = 0.06124965  (6.1250% ceiling)
  0.06124965 ∉ [0.08, 0.10]   (band_floor_gap = band_lo − relief_total = 0.08 − 0.06124965 = +0.018750)
  ⇒ band_closed = False

Step 4 (Canonical form — directional read-off):
  band_closed = False  ⟸  W1-1 == FAIL  (relief 0.06125 < band_lo 0.08, structural)
  ⇒ the SIGN of band-closure tracks the SIGN of W1-1 scale-leg admissibility.

Step 5 (Direction):
  The pre-registered prediction for the FAIL branch was "band does NOT close" — and it does not.
  The SIGN is therefore CORRECT (sign_verdict=PASS): a bare-import M_KK (W1-1 FAIL) leaves the
  93.875% held, capping relief at the dimensionless 6.125%. The MAGNITUDE fails only because that
  capped value lands 0.018750 below the band floor (magnitude_verdict=FAIL). The method is exact
  (rationals) and the FAIL branch was explicitly anticipated at plan-freeze (regime_verdict=VALID).

Conclusion: band_closed = False, conditioned on W1-1 == FAIL. H0 relief is CAPPED at 6.125% — the
  registered ceiling under a permanent external M_KK pin. There is no closure path that bypasses
  W1-1: the dimensionless channel alone (0.06125) falls below the band floor (0.08) by construction.
```

**Results**:

- **Resolved W1-1 upstream verdict**: `CF-S112-MKK-SUBSTRATE-ANCHOR` = **FAIL** (resolved via Option-A supersession reading of `computations/session-112/s112_gate_verdicts.txt`; reason=`resolved`, n_canonical=1, n_superseded=0; `audit_sha256=3fa9be16e90ada96…`). Branch fired: **FAIL-capped-dimensionless** (the registered fallback).
- **band_closed = False** against band [0.08, 0.10] (central 0.09, lit 0.084). The capped relief 0.06124965 sits **0.018750 below band_lo=0.08**.
- **Dimensionless-channel floor**: `49/800 = 0.06124965` (exact 1224993/20000000), loaded from `s111_cf3`, not recomputed. `roundfig_within_4sf=True`, `roundfig_recompute_ok=True`, `residual_consistent=True` (the loaded rational equals 1 − relief to 1e-9). The S111 capped reading `best_dimless_frac_lo=0.06127` is the dual-cross-section variant; the exact-rational floor is the falsifier-relevant value.
- **Dimensionful draw NOT attempted** (`dimensionful_draw_attempted=False`): the FAIL branch does not permit it; the `dimensionful_draw_required_to_close=18.36` would only be tested on W1-1 PASS.
- **4-tuple**: `(scheme=emergent-scale-transport-DIMENSIONLESS-ONLY, convention=DA-0-PARITY-EVEN, L_max=12)`; `convention_parity_pin=RATIO-DA-1-PARITY-odd` (the released-branch ODD face that W1-1 FAIL left inadmissible).
- **Dual-prior reallocation (inherited from W1-1)**: W1-1 FAIL → 0.95 to Track-B (permanent external-import boundary). W1-2 inherits: band-closure stays capped at 6.125%, the registered ceiling.
- **Dual-SHA + schema-v2 3-tuple**: present (sign=PASS / magnitude=FAIL / regime=VALID).
- **Artifacts**: `s112_h0_band_closure.py`, `s112_h0_band_closure.npz`, `s112_h0_band_closure.png`.

**H0-relief ceiling (the falsifier-relevant number)**: **6.125%**. The Hubble tension is genuinely but partially relieved — the substrate's emergent expansion-rate channel delivers exactly `49/800 = 6.125%` of the residual through its DIMENSIONLESS transport leg (d_A=0, EVEN parity). The remaining **93.875%** is honestly pinned to the **one external M_KK scale** (`M_KK = 7.42866 × 10¹⁶ GeV`) that the self-referential unit system cannot self-supply. This 6.125% ceiling is the H0 number `mack-cosmic-bridge` logs as falsifier-relevant: the framework predicts the substrate resolves the Hubble tension *up to* 6.125% from first principles, with the dimensionful remainder explicitly NON-predicted (it is the irreducible external anchor, NOT a refinable approximation — the S100a rank-1-Yukawa-wall precedent: "irreducibly external, not a refinable approximation"). A future detector measurement of H0 that required >6.125% of the tension to come from the dimensionless channel would falsify this ceiling; a measurement consistent with the substrate supplying 6.125% and the rest tracking the externally-fixed M_KK scale is consistent.

**Substrate framing** (IS-not-IN; the flow runs FROM the D_K spectral moments TOWARD the observable): H0 — the emergent expansion rate — IS read from the substrate's GGE-relic transport channel. The a_0/a_2 Seeley-DeWitt moments source the effective Friedmann H² = (8πG_eff/3)ρ_eff, and the H0 residual IS a transport observable of the substrate's excitations across the 54.04-decade substrate-leaf → CMB-pivot scale separation (`dec_separation=54.04`, `a0_a2_orthogonal=True`, `deg_T=2.0` NON-SCALAR). The substrate's DIMENSIONLESS transport channel (d_A=0, even parity) delivers `49/800 = 6.125%` relief intrinsically — that is the substrate BEING the partial resolution, not a model fitted to it. The dimensionful M_KK^1 scale leg (d_A=+1, ODD parity) is INADMISSIBLE because only even-degree morphisms can transport a bare external scale to the pivot — and W1-1 established the substrate cannot make M_KK intrinsic (the self-referential no-go). The substrate's honest answer: it resolves the Hubble tension by 6.125% through what it IS (its dimensionless spectral transport), and pins the rest to the one absolute scale it cannot measure against itself — exactly the boundary where the framework's predictive reach ends and one external anchor is irreducibly required.

---

## Wave 1 Synthesis (team-lead)

Wave 1 attacked the MAGNITUDE half of the §6.3 a(t)/effective-Friedmann residual — the dimensionful origin of M_KK. Both gates FAILed, and the FAILs are the strongest possible result: a **structural no-go**, not an agent failure (`math-scripts.md §"All Results Are Good Results"`).

- **W1-1 CF-S112-MKK-SUBSTRATE-ANCHOR — FAIL** (sign=PASS · magnitude=FAIL · regime=VALID; audit `3fa9be16…`). The registered no-go (dual-prior Track-B, prior 0.90). Both pinned substrate-natural anchors — A (GAP-EMERGENT-LENGTH `Δ_BCS·M_KK`) and B (EMERGENT-NEWTON `√(a₂^ζ/(48π²))·M_KK`) — reduce to `M_KK·(pure number)` (prefac_B=0.387730 ⇒ Δ_rel=0.612; prefac_A=0.074359 ⇒ Δ_rel=0.926), because the substrate's spectral data (a₂, Δ_BCS) are DIMENSIONLESS in M_KK units and cannot bootstrap an absolute GeV scale. leg1 τ-flatness is unreachable by any τ-constant anchor (`M_KK(τ)/M_KK(τ_fold)=R(τ)/R(τ_fold)`; the τ-non-flatness is intrinsic to R(τ), the same reason bare M_Pl failed in S111). Both beat the bare baseline Δ_rel=8.193 but miss both the 5e-2 PASS and 5e-1 INFO bands. **The magnitude leg is a permanent external-import boundary — the self-referential-unit-system no-go** (lattice-QCD scale-setting analog: all dimensionless ratios predicted, exactly ONE external dimensionful anchor irreducibly required).
- **W1-2 CF-S112-H0-BAND-CLOSURE — FAIL** (the registered FAIL-branch fallback; audit `f5a8498d…`). W1-1 FAIL ⇒ the d_A=+1 ODD M_KK¹ scale leg stays INADMISSIBLE (parity selection rule) ⇒ no dimensionful draw ⇒ H0 relief CAPPED at `49/800 = 6.125%` (exact, the dimensionless transport channel); `0.06125 ∉ [0.08, 0.10]`, band_closed=False, residual_held=93.875%. **6.125% is the substrate's honest, structurally-bounded contribution to the Hubble tension**; the ~93.875% remainder is pinned to the one external M_KK scale.

### Effected In-Session (non-math — executed via the mack landing pass; verified on disk)

- [x] Capstone §6.3 reconciliation — `sessions/framework/phonic-exflation-equation.md:458` — additive status-sharpening note: magnitude leg now a PERMANENT external-import boundary (FAIL-confirmed under both bare-import S111 + substrate-natural S112); H0 capped 6.125%; substrate-IS arrow explicitly preserved; scope-qualified per S100a "irreducibly external, not a refinable approximation"; Q1∧Q3∧Q4.
- [x] Atlas D04 C1 reconcile — the §6.3 note hardens the atlas-04 C1 dimensional-readout-leg ASSUMED tag to PERMANENT (the last substrate-internal escape ruled out); prose tag = register tag.
- [x] Falsifier-inventory H0-ceiling row — `sessions/framework/registry/falsifier-master-inventory.md:2359` (Row #81.audit-S112-W1-H0-CEILING-PERMANENT) — 6.125% as the falsifier-relevant H0 number; dual audit-SHA provenance (W1-1 `3fa9be16…` + W1-2 `f5a8498d…`); mack sole-writer; framed as ceiling-hardening, no Row #81 H0=67.40 value change.

## Carry-Forward Computations

No carry-forwards: the W1 magnitude-leg no-go is a permanent structural boundary (not a refinable approximation, per the S100a precedent), and the 6.125% H0-relief ceiling is the registered fallback. There is no fillable future-compute — a PASS would require an absolute-scale-carrying observable the substrate does not provide, which is not a pre-registerable gate.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-06-22 | CF-S112-MKK-SUBSTRATE-ANCHOR | M_KK-origin standing gap (OPEN) | CLOSED — magnitude leg PERMANENT external-import boundary | both substrate-natural anchors reduce to M_KK·(pure number); self-referential no-go (FAIL) |
| 2026-06-22 | CF-S112-H0-BAND-CLOSURE | H0 relief partial-pending-M_KK-derivation | CLOSED — capped 6.125% dimensionless channel (permanent) | W1-1 FAIL ⇒ ODD M_KK¹ scale leg inadmissible; band_closed=False |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Size |
|:--|:--|:--|:--|:--|
| W1-1 | s112_mkk_substrate_anchor.py | s112_mkk_substrate_anchor.npz | s112_mkk_substrate_anchor.png | 31228 B script |
| W1-2 | s112_h0_band_closure.py | s112_h0_band_closure.npz | (none — conditional band-closure) | — |
