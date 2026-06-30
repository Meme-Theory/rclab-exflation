# W11-C5 + W11-C6 Lab-Falsifier Protocol Pre-Registration

**Status**: NEEDS-DECISION (UD-14: NEW file vs extend existing W11 framework artifact) → **NEW FILE INSTALLED** 2026-04-27 (S86 Level-10 housekeeping T10-21).
**Source**: S86 W-5 workshop `_housekeeping-extract-w5.md` OTHER-3 (lines 251-254) + COMPUTE-CF-2 (lines 268-273) + COMPUTE-CF-3 (lines 275-280) + workshop L1393-1418 (R2-A EMERGENCE #3 binding chain) + L2243-2247 (Q4-FINAL gate-structure) + L2649-2659 (CF-2/CF-3 specs).
**Recommending agent**: gen-physicist (extract); volovik PRIMARY + connes CO-AUTHOR (workshop sponsors).
**Cross-references**: §VII.P-v2 HP^1-content-distinct recast (S87 carry-forward CF-34); `sessions/framework/correspondence/3HeB-inheritance-canonical.md`; `sessions/framework/registry/elimination-bulletins.md` Bulletin #2.

This entry is the four-gate falsifier protocol pre-registration for the W11-C5 (3He-B vortex-core spectroscopy at Lancaster MCT-3 / RHUL) + W11-C6 (3He-A µSR) laboratory experiments. F1-FIRST priority is enforced; cross-cocycle ratio `7.3250 ± 0.1%` is the cohomology-asymmetry test alongside row-wise NULL prediction (kernel-signature test); both tests are pre-registered to prevent post-hoc test-class selection.

---

## §1 — Protocol scope

W11-C5 and W11-C6 are TWO laboratory falsifier programs proposed at S86 W-5 to test the substrate's prediction that 3He-B (vortex-core spectroscopy) and 3He-A (µSR) measurements should produce ROW-WISE NULL signal on five inheritance-arrow image rows (F1, F2, F3, F4, F5) AND a cohomology-asymmetry cross-cocycle ratio of `‖φ_67‖ / ‖φ_88‖ = 7.3250 ± 0.1%` on any non-NULL detection (which would be an inheritance-arrow violation requiring framework re-evaluation).

| Protocol | Lab platform | Phase | Geometry | Probe |
|:---------|:--------------|:-------|:----------|:-------|
| **W11-C5** | Lancaster MCT-3 (PRIMARY) or RHUL (alternative) | 3He-B | Vortex-core | Spectroscopy (Caroli-Matricon ladder splitting; φ_67 cocycle-clean) |
| **W11-C6** | Helsinki ROTA / TKK-µSR or equivalent | 3He-A | Chiral A-phase | µSR (muon-spin rotation) |

Both protocols adopt the same four-gate structure (§2). Lab-conversion factors differ between B-phase and A-phase (chirality conventions, observable inventory); substrate ratios (substrate-derived predictions for cocycle ratios) are IDENTICAL across the two protocols at value `7.3250` per the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 EMERGENCE #2 R2-A; Sage-verified machine-precision residual `0.0e+00`).

---

## §2 — Four-gate structure (per L2243-2247)

Each protocol is pre-registered as a four-gate falsifier suite:

### Gate 1 — Row-wise NULL on F1 + F2 + F5 (kernel-signature test)

**Pre-registered prediction**: substrate predicts NULL signal on rows F1 (Caroli-Matricon ladder splitting), F2 (φ_67 cocycle-related observable), F5 (chirality-flip rate). The lab measurement on each row should produce signal-to-noise ratio (S/N) `≤ 1` (i.e., at or below detector noise floor).

**PASS criterion**: row-wise NULL detection on all three rows (F1, F2, F5); per-row S/N `≤ 1` at lab-detector precision.

**FAIL criterion**: any row produces statistically significant signal (S/N `> 3`); inheritance-arrow image is violated; framework-level re-evaluation triggered.

**INFO criterion**: 1 ≤ S/N ≤ 3 on any row; defer to multi-pressure scan or repeat measurement (Gate 4).

### Gate 2 — Cross-cocycle ratio `7.3250 ± 0.1%` (cohomology-asymmetry test)

**Pre-registered prediction**: on any NON-NULL detection at any row (F1-F5), the substrate predicts the cross-cocycle ratio `‖φ_67‖ / ‖φ_88‖ = 7.3250 ± 0.1%` per the (Δ_B/Δ_A)^p cancellation theorem.

**Operational form (per S86 W-5 (Δ_B/Δ_A)^p cancellation theorem, DONE-5)**:

```
For two rows F_i and F_j with common p_i = p_j = p:
   lab(F_i) / lab(F_j) = ‖φ_a‖ / ‖φ_b‖ × (f_i / f_j)
                       = 7.3250 × (lab-conversion-ratio)

where f_i, f_j are the lab-conversion factors (phase-dependent: differ between B-phase
and A-phase, identical structurally for substrate ratio).
```

**PASS criterion**: cross-cocycle ratio at any non-NULL detection matches predicted `7.3250 ± 0.1%` value at lab-detector precision (modulo lab-conversion factors).

**FAIL criterion**: cross-cocycle ratio differs from `7.3250` by `> 0.1%` or shows phase-dependent substrate ratio (which would falsify the cancellation theorem).

### Gate 3 — Row-wise NULL on F3 + F4 (kernel-signature test, supporting rows)

**Pre-registered prediction**: substrate predicts NULL signal on rows F3 (Andreev-bound-state echo) and F4 (multi-pressure slope analysis observable).

**PASS criterion**: row-wise NULL detection on F3 and F4; per-row S/N `≤ 1` at lab-detector precision.

**FAIL criterion**: F3 or F4 produces statistically significant signal (S/N `> 3`); inheritance-arrow image violated.

**INFO criterion**: 1 ≤ S/N ≤ 3 on F3 or F4; defer to F4 multi-pressure scan (Gate 4).

### Gate 4 — F4 multi-pressure slope analysis (lifeline for INFO-level results)

**Pre-registered prediction**: F4 multi-pressure scan (across 3-5 distinct pressures within `0 < p < p_melt`) tests whether any F4 INFO signal scales with pressure as expected from substrate's BdG sector OR is an instrumental artifact.

**Operational form**: substrate's F4 prediction is structurally pressure-INDEPENDENT (per S86 W-5 R2-A DISSENT #2 Sage-verification; F4 Jacobi-cubic vs φ_88-linear ratio = 0.385 at canonical (τ_fold=0.19, Δ_B/Δ_A=0.85), independent of pressure within `0 < p < p_melt`).

**PASS criterion**: F4 scan shows pressure-INDEPENDENT signal (slope `= 0` within scan precision); confirms substrate prediction; reclassifies F4 from INFO to NULL.

**FAIL criterion**: F4 scan shows pressure-DEPENDENT signal (non-zero slope at scan precision); falsifies substrate's pressure-independence prediction; promotes F4 to FAIL classification.

**Helsinki ROTA F4 multi-pressure protocol commitment**: Gate 4 commitment within S87-S88 window per W-5 CF-2 sub-gate.

---

## §3 — F1-FIRST priority enforcement

Per workshop L1393-1418 binding chain + R3-13 doubly-decisive cost-benefit analysis, the F1 row is prioritized for primary measurement because:

1. **F1 is the φ_67 cocycle-clean row** — Caroli-Matricon ladder splitting in 3He-B vortex cores measures `φ_67` (the chiral-pair Hochschild cocycle) directly without contamination from `φ_88` (the conjugate chiral-pair cocycle). The cocycle-clean property minimizes substrate-side adjudication ambiguity.

2. **F1 has the largest substrate-derived predicted lab S/N margin** — per workshop volovik R1 V3 5-row table, F1 has the largest predicted S/N margin among the 5 rows under expected lab conditions, making it the most likely row to produce a decisive PASS or FAIL outcome at first measurement.

3. **F1 is doubly-decisive** — a PASS at F1 confirms BOTH the inheritance-arrow image (Gate 1 NULL) AND the cocycle-clean cohomology structure (Gate 2 ratio `7.3250`). A FAIL at F1 would simultaneously falsify both tests, which is the cleanest possible falsifier outcome.

**Enforcement rule**: any W11-C5 / W11-C6 spec submission that does NOT enforce F1-FIRST priority FAILs the protocol pre-registration step. F1 measurements MUST precede F2-F5 measurements in the experimental program.

---

## §4 — Substrate-derived predictions (cited verbatim)

| Row | Substrate prediction | Phase-dependence | Source |
|:----|:----------------------|:------------------|:--------|
| **F1** (Caroli-Matricon ladder splitting) | NULL (kernel signature); cocycle weight `‖φ_67‖ = 0.793346` if non-NULL | B-phase + A-phase identical structurally; lab-conversion factor differs | Workshop CF-2 input pin; canonical_constants.py `cocycle_norm_phi67` (UD-6 promotion candidate) |
| **F2** (φ_67-related observable) | NULL (kernel signature); cross-cocycle ratio `7.3250` with F1 if non-NULL | Same | Workshop CF-2 input pin |
| **F3** (Andreev-bound-state echo) | NULL (kernel signature) | Same | Workshop CF-2 input pin |
| **F4** (multi-pressure observable) | NULL (kernel signature); pressure-INDEPENDENT slope `= 0` | F4 Jacobi-cubic vs φ_88-linear ratio = 0.385 at canonical | Workshop DONE-3 (Sage-verified within workshop) |
| **F5** (chirality-flip rate) | NULL (kernel signature); cocycle weight `‖φ_88‖ = 0.108296` if non-NULL | Same | Workshop CF-2 input pin |

**Cross-cocycle ratio** (Sage-exact): `‖φ_67‖ / ‖φ_88‖ = 0.793346 / 0.108296 = 7.324992` (Sage-verified 0.0001% match to 4-sig-fig form `7.3250`).

---

## §5 — Cross-references

- **3He-B inheritance canonical**: `sessions/framework/correspondence/3HeB-inheritance-canonical.md` — substrate-physical pre-conditions for the inheritance-arrow morphism χ : C ⊕ H ⊕ M_3(C) → M_2(C); the (τ, k)-mixed Provost-Vallée connection 2-form block characterization of ker(ι_*).
- **§VII.P-v2 HP^1-content-distinct recast**: S87 carry-forward CF-34 (`S87-VII-P-V2-HP1-CONTENT-DISTINCT-RECAST`); registry-landing for §VII.P-v2 strict 7-class drop.
- **(Δ_B/Δ_A)^p cancellation theorem**: S86 W-5 EMERGENCE #2 (R2-A); Sage-verified machine-precision residual `0.0e+00`; operational form `lab(F_i)/lab(F_j) = ‖φ_a‖/‖φ_b‖ × (f_i/f_j)` for common `p_i = p_j = p`.
- **`cocycle_norm_phi67` and `cocycle_norm_phi88`**: pending UD-6 promotion to `computations/canonical_constants.py`; values pinned at `cocycle_norm_phi67 = 0.793346` (substrate magnitude annotation per S86 W-5 C2) and `cocycle_norm_phi88 = 0.108296`.
- **Bulletin #2 (`(C_H, C_epsH) shares (a_0, a_2, a_4)`)**: `sessions/framework/registry/elimination-bulletins.md` Bulletin #2; cross-link to §VII.P-v2 HP^1-distinct recast (T10-20 install).
- **F1-FIRST priority**: workshop L1393-1418 (R2-A EMERGENCE #3 binding chain) + R3-13 doubly-decisive cost-benefit; workshop volovik R1 V3 5-row table for predicted S/N margins.
- **Helsinki ROTA F4 multi-pressure protocol**: Gate 4 commitment within S87-S88 window per W-5 CF-2 sub-gate.
- **CF-2 (W11-C5 lab-falsifier)**: S87 carry-forward CF-32 in `_housekeeping-install-queue.md`; effort: 1 dispatch + 1 follow-up; ~2h S87 plan-freeze.
- **CF-3 (W11-C6 µSR-falsifier)**: S87 carry-forward CF-33 in `_housekeeping-install-queue.md`; effort: 1 dispatch; ~2h.
- **Cohomology-asymmetry test classification (W-5 CF-6)**: forward-looking pre-registration template for any future ker(ι_*) characterization with rank ≥ 2; W-5 CF-6 spec.
- **R-protection structural protection of α_s**: `sessions/framework/registry/alpha-s-structural-protection.md` (T10-4 install) — parent registry entry citing W11-C5/C6 as the lab-falsifier protocol for α_s alternative test routes.

---

## §6 — Open user decisions (BLOCKERS)

- **UD-14**: Create new file `W11-C5-C6-falsifier-protocol.md` (Option a, this install) vs extend existing W11 framework artifact (Option b)? Until UD-14 is decided, this file is the standalone canonical artifact for the W11-C5/C6 protocol; if UD-14 chooses Option b, the file content here is migrated to the existing W11 file and this file is closed.
- **UD-6**: Promote `cocycle_norm_phi67`, `cocycle_norm_phi88`, `R_universal_HP1_strict_F4`, `lam_min_over_max_jensen_fold` to `computations/canonical_constants.py`? Workshop notes "downstream-cited enough to canonicalize" condition. W11-C5/C6 lab spec (CF-2/CF-3) depends on `cocycle_norm_phi67/88` canonicalization.

---

## §7 — Closing

The W11-C5 + W11-C6 four-gate falsifier protocol is the substrate's primary laboratory falsifier program for the inheritance-arrow image structure. Both kernel-signature (Gate 1, Gate 3) and cohomology-asymmetry (Gate 2) tests are pre-registered to prevent post-hoc test-class selection; F1-FIRST priority is enforced for substrate-side adjudication clarity. Substrate ratios are IDENTICAL across B-phase (Lancaster) and A-phase (Helsinki) protocols at value `7.3250` per the (Δ_B/Δ_A)^p cancellation theorem (Sage-verified machine-precision); lab-conversion factors differ between phases. The protocol is ready for S87 plan-freeze submission to platform liaisons; CF-2 + CF-3 are S87 carry-forwards CF-32 + CF-33 with `~2h` effort each at S87 plan-freeze.
