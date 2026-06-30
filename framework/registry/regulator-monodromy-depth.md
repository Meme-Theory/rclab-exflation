# Regulator-Monodromy Depth (substrate observable)

**Status**: NEEDS-DECISION (T10-38: standalone observable file vs deferred to spectral-moment-identities.md) → **STANDALONE FILE INSTALLED** 2026-04-27 (S86 Level-10 housekeeping T10-38).
**Source**: S86 W-12 workshop `_housekeeping-extract-w12.md` OTHER-W12-2 (lines 259-263) + EMERGENCE E-2 line 1643-1645 (R3-volovik final round) + REG-W12-1 line 8-11 + workshop §"What Changed" (i) line 1715-1716.
**Recommending agent**: gen-physicist (extract); connes + volovik (workshop sponsors).
**Cross-references**: `sessions/framework/registry/spectral-moment-identities.md` (existing curated framework note; OTHER-W12-1 housing for V_4 parallelogram + (Z_2)^d hypercube identity); `sessions/framework/registry/elimination-bulletins.md` Bulletin #5 (BULLETIN-4A; T10-39 install); REGULATOR-MONODROMY-AXIS-DECOMPOSITION 5-step methodology (RULE-W12-3).

This entry defines the **regulator-monodromy depth** of the substrate as a structural observable. The depth measures how many INDEPENDENT regulator-class boundaries the substrate's mode content respects without overlap, and is the spectral analog of S60 inheritance framework's "correspondence count."

---

## §1 — Definition

**Regulator-monodromy depth of substrate** (per OTHER-W12-2):

```
depth(substrate) := max d for which the (Z_2)^d hypercube-vertex character identity
                   holds with EXACT residual on bottom-N modes at saturated L_max.
```

Where the (Z_2)^d hypercube-vertex character identity (per OTHER-W12-1, S86 W-12 R3-A line 1385-1430 + Sage-verified d ∈ {2, 3, 4, 5}) is:

```
Σ_{ε ∈ {0,1}^d} (-1)^|ε| · A_n^(ε) = 2^d · Σ_{i: σ_j(i) = -1 ∀j} n_i · w(x_i) · x_i^n
```

with prefactor `+2^d` (Sage-verified d ∈ {2, 3, 4}; d = 5 deferred to S87 carry-forward `S87-HYPERCUBE-VERTEX-IDENTITY-LANDING`).

**Interpretation**: depth measures how many INDEPENDENT regulator-class boundaries the substrate's mode content respects without overlap. Each independent boundary corresponds to a sign convention or class selector (LOCAL UV / heat-kernel-coefficient sign OR GLOBAL IR / asymptotic-completion topology) the regulator picks up when crossed.

---

## §2 — Substrate's depth at τ_fold (current status)

| Layer | Pre-S86 status | S86 W-12 status | Post-S87 status |
|:------|:---------------|:----------------|:------------------|
| **Bare-eigenvalue layer** | Z_2 (Mellin reversal only) | Z_2 (PASS-nonbimodal) | depth = 1 (Mellin reversal axis only) |
| **Moment-integral layer** | Pre-registered hypothesis: Z_4 cyclic monodromy | V_4 = Z_2(Mellin local-residue at s = -1) × Z_2(W6-3 global-asymptotic-topology) | depth ≥ 2 (V_4 confirmed candidate via S87) |
| **Atlas-extended layer** | Not probed | Not yet probed | depth = 2 (exactly) vs higher is S87+ atlas-extension question |

The substrate's regulator-monodromy depth at τ_fold is therefore **depth ≥ 2** at S86 close, with the V_4 = (Z_2)² Klein-four monodromy at moment-integral layer the confirmed candidate (Sage-verified non-cyclic via element orders V_4 = [1, 2, 2, 2] vs Z_4 = [1, 2, 4, 4]; R2-A line 798-840). Depth promotion to a definite integer requires S87 carry-forward `S87-MONODROMY-V_4-EXPLICIT` (CF-66) PASS.

---

## §3 — Z_2 axis decomposition

The two confirmed Z_2 axes at moment-integral layer are STRUCTURALLY INDEPENDENT (R2-A E-3 line 918-955; R3-A C-4 line 1280):

| Axis | Type | Source | Independence |
|:------|:-----|:--------|:--------------|
| **Axis_M (Mellin local-residue at `s = -1`)** | LOCAL UV / heat-kernel-coefficient sign convention | Wodzicki-residue / `a_4` locality argument (S82 W2-5 MP-Exclusion theorem) | LOCAL data does NOT fix GLOBAL data |
| **Axis_C (W6-3 conformal-end / global-asymptotic-topology)** | GLOBAL IR / asymptotic-completion topology selector (ℐ⁺ class, flat ℝ × S² ↔ dS S³) | Connes-Marcolli (2007) §1.17 | GLOBAL data does NOT fix LOCAL data |

The two axes are STRUCTURALLY INDEPENDENT (verified via R2-A D-2 substitution chain, line 842-864): a regulator using Mellin-cone residue reads off the SAME `a_4` regardless of whether asymptotic ℐ⁺ is flat (`Λ_eff = 0`) or dS (`Λ_eff > 0`). Conformal-end choice (Axis_C) determines downstream interpretation as CC contribution but does not change residue value itself.

**Substrate-physical depth-2 reading**: substrate at τ_fold has `depth = m + k = 1 + 1 = 2` where `m = 1` (one LOCAL axis: Mellin local-residue) + `k = 1` (one GLOBAL axis: W6-3 conformal-end) + 0 further independent axes.

---

## §4 — Depth extension question (S87+)

The depth extension question: is `depth = 2` exact at substrate τ_fold, or does it extend to `depth > 2` under atlas extension?

**S87 carry-forward `S87-MONODROMY-DEPTH-EXTENSION`** (CF-71 in `_housekeeping-install-queue.md`; W-12 CF-W12-6 latent):

- **What**: Test whether substrate's regulator-monodromy depth `d = 2` is exact, or extends to `d > 2` under atlas extension. Add candidate axes (e.g., Pauli-Villars's `κ_PV` as third LOCAL axis OR topological-sector selector as second GLOBAL axis); test (Z_2)^3 hypercube-identity at extended atlas.
- **Inputs**: S87 V_4 confirmation (CF-66 `S87-MONODROMY-V_4-EXPLICIT` PASS); candidate third-axis enumeration (Pauli-Villars `κ_PV` LOCAL OR topological-sector selector GLOBAL); spectral moments `A_n^(g)` for `n ∈ {0, 2, 4}` at τ_fold under three-axis cosets.
- **Gate**: PASS = (Z_2)^3 hypercube-identity holds with EXACT residual on bottom-N modes at saturated L_max; depth ≥ 3. INFO = identity holds approximately but residual exceeds parallelogram-EXACT threshold; further axis-independence verification needed. FAIL = identity violated; depth = 2 exactly.
- **Effort**: ~6-10 hours.

---

## §5 — Cross-domain analog: S60 inheritance "correspondence count"

The regulator-monodromy depth is the spectral analog of S60 inheritance framework's "correspondence count":

| Substrate observable | Spectral analog | Inheritance-framework analog |
|:---------------------|:----------------|:------------------------------|
| **Regulator-monodromy depth** `d` | Number of independent regulator-class boundaries respected | Number of structural correspondences between substrate and 3He-B (S60 framework: 22 correspondences mapped) |
| **(Z_2)^d hypercube-identity exact** | Disjoint-support condition holds at depth `d` | Substrate-substrate / substrate-laboratory correspondence is structurally protected |
| **Depth extension under atlas extension** | New axis axis creates new (Z_2) factor | New laboratory analog adds new correspondence row |

**Direction**: The substrate's regulator-monodromy depth is a STRUCTURAL OBSERVABLE that measures how many independent regulator-class boundaries the substrate's mode content respects. It is the spectral analog of inheritance-correspondence count, not a free parameter; depth promotion from `d ≥ 2` to a definite integer is gated on S87 carry-forward verification.

---

## §6 — Observable life-cycle

The observable transits through five life-cycle states:

1. **CANDIDATE-OBSERVABLE** — current state at S86 close. Definition is registered; depth ≥ 2 at τ_fold; exact value pending S87 V_4 verification.
2. **DEPTH-CONFIRMED-d=2** — `S87-MONODROMY-V_4-EXPLICIT` PASS-parallelogram-exact; depth = 2 confirmed at saturated L_max for moment-integral layer.
3. **DEPTH-EXTENDED-d>2** — `S87-MONODROMY-DEPTH-EXTENSION` PASS at (Z_2)^3 hypercube-identity; depth ≥ 3 confirmed; new axis added to atlas.
4. **DEPTH-LOCKED-EXACT** — extension test at depth `d + 1` FAILs; depth = `d` is exact at substrate τ_fold for the current atlas.
5. **CANONICALIZED** — depth value promoted to `computations/canonical_constants.py` as `regulator_monodromy_depth_substrate_tau_fold = d`; provenance pinned.

The observable is currently in state 1 (CANDIDATE-OBSERVABLE) at S86 close.

---

## §7 — Cross-references

- **Companion identity registry**: `sessions/framework/registry/spectral-moment-identities.md` (curated framework note housing V_4 parallelogram identity at d = 2 + (Z_2)^d hypercube-vertex character identity general form with prefactor `+2^d` + disjoint-support condition; OTHER-W12-1 housing).
- **REGULATOR-MONODROMY-AXIS-DECOMPOSITION 5-step methodology**: S86 W-12 RULE-W12-3 (workshop EMERGENCE E-2 R2-B line 1207-1228 + R3-A C-4 line 1278-1283).
- **V_4 monodromy candidate registry entry** (REG-W12-1): candidate observable for `sessions/permanent-results-registry.md` after S87-MONODROMY-V_4-EXPLICIT PASS-parallelogram-exact; gated on S87 carry-forward CF-66.
- **Bulletin #5 (BULLETIN-4A) V_4 coset interpretation**: `sessions/framework/registry/elimination-bulletins.md` Bulletin #5 update via T10-39 (W-12 OTHER-W12-3); moment-integral V_4 coset cardinality 8 + 1 + 1 + 1 = 11.
- **Wodzicki-residue / `a_4` locality**: S82 W2-5 MP-Exclusion theorem; supplies locality argument for Axis_M classification as LOCAL.
- **Connes-Marcolli (2007) §1.17 separation**: `sessions/framework/correspondence/correspondence-table-registry.md` CORR-W12-3 (T10-7 install via parallel agent); supplies separation of local spectral-action computation from global asymptotic completion (Axis_C classification as GLOBAL).
- **S60 inheritance framework correspondence count**: `sessions/framework/framework-3heb-comparison.md` (22-correspondence ledger; T10-23 install).
- **`S87-MONODROMY-V_4-EXPLICIT`** (CF-66): V_4 verification at τ_fold + 4 cosets + 3 spectral moments (n ∈ {0, 2, 4}); ~6 hours; PASS confirms depth = 2.
- **`S87-HYPERCUBE-VERTEX-IDENTITY-LANDING`** (CF-69): formalize (Z_2)^d hypercube-vertex character identity at d ∈ {2, 3, 4, 5} with Sage-verification; ~2 hours; PASS pins prefactor `+2^d`.
- **`S87-MONODROMY-DEPTH-EXTENSION`** (CF-71 latent): depth extension test under atlas extension; ~6-10 hours.

---

## §8 — Closing

The regulator-monodromy depth of the substrate is a structural observable measuring how many INDEPENDENT regulator-class boundaries the substrate's mode content respects without overlap. Substrate at τ_fold has `depth ≥ 2` at S86 close, with the V_4 = Z_2(Mellin local-residue) × Z_2(W6-3 global-asymptotic-topology) Klein-four monodromy at moment-integral layer the confirmed candidate (Sage-verified non-cyclic). Depth promotion from `d ≥ 2` to a definite integer is gated on S87 carry-forwards CF-66 (V_4 explicit verification), CF-69 (hypercube-identity landing), and CF-71 (depth-extension test). The observable is the spectral analog of S60 inheritance framework's "correspondence count" — a STRUCTURAL OBSERVABLE, not a free parameter.
