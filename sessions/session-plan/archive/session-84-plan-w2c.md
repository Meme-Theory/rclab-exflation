# Session 84 Plan -- Wave 2c: Layer Transport + UNPINNED Stress + L_max Extrapolation + G Pinning Audit (4 gates)

**Session**: 84
**Wave**: 2c (parallel-independent with W2a and W2b)
**Scope**: §4.B items 18, 19, 20 from session-84-context.md -- the operational-mechanics audits of the three-layer regulator theorem
**Planner**: gen-physicist
**Date**: 2026-04-18
**Dispatch mode**: parallel-independent (no cross-agent handoff within W2c)

---

## W2c Summary

W2c stress-tests the operational mechanics of the three-layer regulator theorem (L1 axiomatic / L2 substrate-action / L3 observable) registered in W2a-11. Where W2a lands the theorem statements, W2b audits the framework-target projections, and W2c audits **how the theorem is actually used** when observables are evaluated. Three orthogonal stress tests:

1. **W2c-18 (LAYER-TRANSPORT)**: For each MIXED row in the §VII.K atlas, compute the explicit Mellin transport T_{L2->L3} that converts Layer-2 substrate-action minimum into Layer-3 observable-level span. Without an explicit transport table, MIXED rows are only informally classified -- this gate formalizes the L2->L3 step per row.

2. **W2c-19 (UNPINNED-L2-AUDIT)**: The 5 UNPINNED rows in §VII.K-META (r_max, w_0 under Zubarev and zeta branches, a_2-cluster, mu_eff Lindblad-Keldysh) are by construction unpinned under L1. Audit whether L2 Zubarev canonicalization pins them. If yes, they promote to L2-pinned; if no, they are genuinely scheme-unpinned and inform the §VII.K-META structural completeness claim.

3. **W2c-20 (L_MAX-EXTRAPOLATION)**: The W1-G1 3-criterion intersection (Zubarev-unique substrate-action minimum, zeta-unique Dixmier-axiom regulator) is numerically validated at L_max=5 only. Extrapolate to L_max=7 and L_max=9 using GPU torch.linalg.eigvals on the full D_K spectrum. If either uniqueness inverts, W1-G1 PASS is a truncation artifact.

All three gates are AUDIT-class -- they re-examine operational use of a prior PASS verdict (W1-G1 and S83-G58 META) rather than producing new structural claims. Together they determine whether the three-layer theorem is a structural truth or a L_max=5 coincidence.

---

## W2c Decision Point Prerequisites

**Preconditions for W2c dispatch**:
- W2a-11 (S84-THREE-LAYER-REG-LANDING) must be dispatched in parallel (same wave) to provide the theorem-statement anchor; W2c gates cite the L1/L2/L3 definitions from W2a-11 but do not require its PASS before executing.
- S83-G53 HP-EVEN-COMPLETENESS-AUDIT-VII (PASS) provides the 53-row §VII.K atlas -- input SHA must be pinned from W3-G54 output.
- S83-G54 FI-REGISTRY-VII-K-LANDING (PASS) provides the MIXED / FI / GV / CM 4-bucket classification with per-row sub-tags.
- S83-G61 MIXED-SUB-TAG-PER-ROW (PASS, 8/8 valid) provides the FI-pin / mostly-RD / promotable sub-tag partition.
- Canonical S_zeta/S_Zubarev = 42.03 anchor at L_max=5, tau=0.19 (from W1-G1 numerical sanity, Connes synthesis Appendix A §VII.M).

**Fallback on precondition failure**: If S83 SHA ledger is unavailable at dispatch time, W2c gates run in diagnostic mode (INFO-only verdicts), and re-dispatch is queued for W3.

---

## §W2c-18. S84-LAYER-TRANSPORT-AUDIT

**Gate ID**: S84-LAYER-TRANSPORT-AUDIT

**Trigger**: `[AUDIT]`

**Classification**: META

**Agent type**: van-den-dungen-bridge-theorist

**Hypothesis**: For each MIXED row in the §VII.K 42-row atlas, there exists a well-defined Mellin transport map T_{L2->L3} : (substrate-action minimum at L2) -> (observable-level span at L3) that produces a finite, row-specific layer-shift factor sigma_row = |span_L3(row) / Δ_L2(row)|. The MIXED classification is structurally complete iff every MIXED row yields a finite sigma_row under the transport, and degenerate iff any row produces an undefined or diverging transport.

**Method** (full self-contained dispatch prompt for van-den-dungen-bridge-theorist):

> You are a van-den-dungen-bridge-theorist dispatch for S84-LAYER-TRANSPORT-AUDIT.
>
> **SUBSTRATE FRAMING (mandatory)**: The substrate is phononic. Every observable is a spectral moment of D_K on Jensen-deformed SU(3). Layer-2 Zubarev action is a substrate-action functional whose minimum selects the substrate's preferred regulator; Layer-3 span is the range of observable values under scheme variation. The transport T_{L2->L3} is NOT a GR-style coordinate transformation -- it is a Kasparov-style factorization of the observable through the substrate-action layer.
>
> **Task**: Build an explicit T_{L2->L3} transport table for the 10 MIXED rows identified in S83 W3-G54 audit (from the 42-row §VII.K atlas). For each row:
>
> 1. Identify the observable's Mellin slot(s) via its CC-5 decomposition O = prod_i F_i^|p_i|.
> 2. Compute Delta_L2(row) = |S_Zubarev(regulator_row) - S_Zubarev(canonical)| at tau=0.19, L_max=5, where canonical is the Zubarev unique minimum from W1-G1 (S_Zubarev = 3.806e+3).
> 3. Compute span_L3(row) = max_{reg in 5} O(reg) - min_{reg in 5} O(reg) across the 5-regulator atlas {zeta, Zubarev, SDW, dim-reg, lattice-BR}.
> 4. Define sigma_row = span_L3(row) / Delta_L2(row) (dimensionless layer-shift factor -- the rate of transport).
> 5. Tabulate sigma_row for all 10 MIXED rows.
>
> **Canonical constants (MANDATORY)**:
> ```python
> from canonical_constants import *
> # tau_fold = 0.19, M_KK, Delta_BCS = 0.4642, S_fold, dS_fold, d2S_fold
> # H_TD = 5.9076e-3, eps_H = 0.02163
> ```
> Every derived intermediate tagged with `# (local)`.
>
> **Input SHA-256 pins**:
> - `s83_w3_g54_hp_even_completeness_audit_vii.npz` (§VII.K atlas, 53 rows) -- `<computed-at-runtime>`
> - `s83_w1_g1_zubarev_unique.npz` (S_Zubarev canonical at L_max=5) -- `<computed-at-runtime>`
> - `s83_g61_mixed_sub_tag.npz` (MIXED sub-tag partition 8/8) -- `<computed-at-runtime>`
> - `canonical_constants.py` (live import) -- `<computed-at-runtime>`
>
> **Numerical procedure**:
> - Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
> - GPU path: NOT required (transport is row-by-row scalar arithmetic; the 10 MIXED rows yield a 10-entry table). OMP cap 8 for CPU safety.
> - For each MIXED row, load its regulator-sweep output from the §VII.K atlas file. If not present, recompute using the 5-regulator suite at L_max=5, tau=0.19.
> - Record per-row: (observable_name, Mellin_slots, p_exponents, Delta_L2, span_L3, sigma_row, sub_tag).
>
> **Cross-checks**:
> 1. CC-5 identity: span_L3(row) must equal prod_i span(F_i)^|p_i| at <0.02% residual (from S83-G34 CC-5 theorem).
> 2. Layer ordering: if sigma_row << 1, the row is L2-dominated (Layer-2 variation amplifies to L3 weakly); if sigma_row >> 1, L3-dominated (observable-layer variation exceeds substrate-action variation). MIXED-FI-pin rows should cluster at sigma_row in [0.8, 1.5]; MIXED-mostly-RD should cluster at sigma_row < 0.5; MIXED-promotable should cluster at sigma_row > 2.
> 3. Signed-transport sanity: sign(sigma_row) = sign(d span_L3 / d Delta_L2) must be +1 (monotonic transport). Negative sigma indicates anti-correlation -- flag as structural anomaly.
>
> **Output file names**:
> - `computations/s84_w2c_layer_transport_audit.py` (script)
> - `computations/s84_w2c_layer_transport_audit.npz` (data: 10-row sigma table)
> - `computations/s84_w2c_layer_transport_audit.md` (working-paper section §VII.M-TRANSPORT)
>
> **Verdict-line target**: `computations/s84_gate_verdicts.txt` appended with:
> ```
> S84-LAYER-TRANSPORT-AUDIT: PASS|FAIL|INFO -- value=<max_sigma> scheme=Zubarev-L2 convention=CC5 L_max=5 sha256=<closure>
> ```

**Machinery pin (PRDR)**:
- L_max = 5 (matches W1-G1 numerical sanity anchor)
- scan_range: 10 MIXED rows from §VII.K-META sub-tag partition (no free scan -- row-set is fixed by S83-G61)
- tolerance: sigma_row reported to 4 significant figures; transport-identity CC-5 residual < 0.02% (matches S83-G34 PASS threshold)
- scheme: Zubarev as L2 canonical (W1-G1 anchor)
- convention: CC-5 Mellin decomposition (§VII.K-PROP S83-G34)
- random_seed: N/A (deterministic table construction)
- GPU path: CPU-only (scalar arithmetic across 10 rows), OMP_NUM_THREADS=8

**Expected output 4-tuple**: `(value=<max sigma_row across 10 MIXED rows>, scheme=Zubarev-L2, convention=CC5, L_max=5)`

**PASS / FAIL / INFO thresholds**:
- **PASS**: All 10 MIXED rows yield finite sigma_row with sign(sigma_row) = +1 AND sub-tag clustering matches prediction (FI-pin [0.8, 1.5], mostly-RD < 0.5, promotable > 2) within factor-1.5 band. Tolerance rule: RATIO (factor-1.5 around sub-tag centroid).
- **FAIL**: Any row yields sigma_row undefined (Delta_L2 = 0, division by zero) OR any row produces sign(sigma_row) = -1 (anti-correlated transport indicates MIXED classification is structurally broken). Tolerance rule: ABSOLUTE (presence of any anomaly).
- **INFO**: 1-2 rows deviate from sub-tag centroid prediction by factor 1.5-3 (classification is structurally valid but sub-tag partition may need refinement). Tolerance rule: RATIO (factor-1.5 to factor-3 band).

**Substitution chain** (mandatory for [AUDIT] trigger):

1. **Definition** (canonical): Layer-2 substrate-action functional is S_L2(reg) = integral over Jensen-SU(3) of (heat-kernel trace weighted by Zubarev cutoff). S_L2(canonical) = S_Zubarev = 3.806e+3 at L_max=5, tau=0.19 [from W1-G1].
2. **Definition** (canonical): Layer-3 observable span is span_L3(O) = max(O_reg) - min(O_reg) over the 5-regulator atlas {zeta, Zubarev, SDW, dim-reg, lattice-BR}.
3. **Definition** (new, for this gate): Layer-transport factor is sigma_row = span_L3(row) / Delta_L2(row) where Delta_L2(row) = |S_L2(regulator_row) - S_L2(canonical)|.
4. **Substitute** (row-by-row): For each row in {10 MIXED rows}, plug (Delta_L2, span_L3) into sigma definition -- explicit per-row arithmetic, no simplification yet.
5. **Simplify** (canonical form): sigma_row = span_L3(row) / Delta_L2(row), with units cancellation (both are action-scaled variations).
6. **Read direction** (from canonical form): sigma_row > 1 <=> observable-layer dominates substrate-action layer (L3-dominated transport); sigma_row < 1 <=> substrate-action dominates (L2-dominated transport); sigma_row ~ 1 <=> balanced transport (MIXED in the strict sense).
7. **Conclusion**: Per-row transport factor classifies MIXED-sub-tag correctly iff sigma_row centroid aligns with {FI-pin [0.8, 1.5], mostly-RD < 0.5, promotable > 2}.

**What PASSES / FAILS MEAN for solution space**:
- **PASS**: The three-layer theorem has an explicit, finite, monotonic transport map. MIXED classification is structurally complete -- every MIXED observable factors uniquely through (L2 substrate-action, L3 observable) with row-specific transport rate. This confirms the §VII.M landing as a structural result rather than a nomenclature.
- **FAIL**: If any MIXED row produces undefined or sign-reversed transport, the MIXED classification is degenerate on at least one row -- the three-layer theorem's operational mechanics require extension (e.g., non-linear transport, higher-order Mellin slot structure). W2a-11 registration would need to scope-restrict to {FI, GV, CM} buckets only, dropping MIXED as a uniform bucket.
- **INFO**: Sub-tag centroids partially align; the MIXED bucket is structurally valid but the 3-sub-tag partition (FI-pin/mostly-RD/promotable) may need refinement. Feeds into W3 FI-sub-tag-registry proposal.

**Effort estimate**: 1 session, MEDIUM. The computation is row-by-row scalar arithmetic (no GPU eigendecomposition needed) -- the dominant cost is loading and parsing the 53-row §VII.K atlas. van-den-dungen-bridge-theorist is the natural agent for transport audits because the Kasparov factorization machinery is the source of the layered decomposition.

**Substrate-framing reminder in agent dispatch prompt**: The transport map T_{L2->L3} is a Kasparov-style factorization, NOT a coordinate transformation on an external spacetime. L2 is the substrate-action layer (functional minimum on Jensen-SU(3)); L3 is the observable layer (spectral moments). The direction of explanation is D_K -> S_L2 -> span_L3 -> observable -- never invert. A MIXED row that fails the transport audit is a structural anomaly at the substrate level, not a breakdown of a coordinate chart.

---

## §W2c-19. S84-UNPINNED-L2-AUDIT

**Gate ID**: S84-UNPINNED-L2-AUDIT

**Trigger**: `[AUDIT]`

**Classification**: META

**Agent type**: lizzi-spectral-functional-theorist

**Hypothesis**: The 5 UNPINNED rows in the §VII.K-META atlas (S83 Lizzi synthesis §II.4 Python-validated) are L1-unpinned by construction. Under L2 Zubarev canonicalization (W1-G1 substrate-action choice), each UNPINNED row either (a) shifts by factor < 1.5 relative to its L1 reading -- indicating L2 provides the missing pin, promoting the row to L2-pinned; or (b) shifts by factor > 3 -- indicating the row is genuinely unpinned by either layer, and represents a structural degeneracy of the §VII.K-META classification.

**Method** (full self-contained dispatch prompt for lizzi-spectral-functional-theorist):

> You are a lizzi-spectral-functional-theorist dispatch for S84-UNPINNED-L2-AUDIT.
>
> **SUBSTRATE FRAMING (mandatory)**: The substrate picks its own scheme at two strata (S83-MASTER theorem): L1 axiomatic (zeta unique under Dixmier axioms A1-A6) and L2 substrate-action (Zubarev unique at local-min in spectral-action functional). UNPINNED rows are observables whose substrate-derivable scheme is ambiguous at L1 -- the Dixmier axioms do not select a unique regulator for these observables. The L2 audit asks whether the substrate-action layer removes the ambiguity.
>
> **Task**: For each of the 5 UNPINNED rows in §VII.K-META (Lizzi synthesis §II.4):
>   - #13: r_max (backreaction ratio, W2-2 FAIL at 1.33e+4)
>   - #17: w_0 under Zubarev (G51 branch (iv))
>   - #18: w_0 under zeta (G51 branch (iii))
>   - #24: a_2-cluster (W2-8 S82 FAIL at 60.35% var)
>   - #38: mu_eff Lindblad-Keldysh (S82 INFO at 8.58e-4)
>
> recompute the observable value under L2 Zubarev canonicalization (i.e., using S_Zubarev minimum as the regulator-selection rule, which fixes the cutoff scheme to Lambda_Z with matching prescription matched to the Zubarev entropy-maximization local minimum). Then:
>
> 1. Obtain the L1 reading O_L1(row) from the original S82/S83 FAIL/INFO record.
> 2. Compute O_L2(row) under L2 Zubarev canonicalization at L_max=5, tau=0.19.
> 3. Compute shift_factor(row) = max(O_L1, O_L2) / min(|O_L1|, |O_L2|).
> 4. Classify: PROMOTE-L2 if shift_factor < 1.5; GENUINE-UNPINNED if shift_factor > 3; BORDERLINE if 1.5-3.
>
> **Canonical constants (MANDATORY)**:
> ```python
> from canonical_constants import *
> # tau_fold=0.19, Delta_BCS=0.4642, E_cond=-0.1369, Vol_SU3,
> # H_TD=5.9076e-3, eps_H=0.02163, w0_FW,
> # J_C2, omega_L1, S_fold, dS_fold, d2S_fold
> ```
> Every derived intermediate tagged with `# (local)`.
>
> **Input SHA-256 pins**:
> - `s82_w2_g2_unified_backreact_79.npz` (row #13 r_max input) -- `<computed-at-runtime>`
> - `s83_w3_g51_w0_regulator.npz` (rows #17 and #18 w_0 branches) -- `<computed-at-runtime>`
> - `s82_w2_g8_a2_cluster.npz` (row #24 a_2-cluster) -- `<computed-at-runtime>`
> - `s82_mu_eff_lindblad_keldysh.npz` (row #38 mu_eff LK) -- `<computed-at-runtime>`
> - `s83_w1_g1_zubarev_unique.npz` (L2 canonicalization anchor) -- `<computed-at-runtime>`
> - `canonical_constants.py` (live import) -- `<computed-at-runtime>`
>
> **Numerical procedure**:
> - Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
> - GPU path: Recommended for row #24 a_2-cluster (requires full D_K spectrum reload at L_max=5 for 5-regulator cross-check). Use `torch.linalg.eigvals` on Jensen-deformed D_K matrix (expected dimension ~10^4 at L_max=5). For rows #13, #17, #18, #38, scalar arithmetic suffices -- OMP_NUM_THREADS=8 CPU path.
> - Per-row procedure:
>   - Row #13 (r_max): Recompute backreaction ratio r_max = (Delta rho) / rho_total using Zubarev cutoff Lambda_Z in place of zeta-regulator cutoff. Compare to S82 W2-2 FAIL value 1.33e+4.
>   - Row #17 (w_0 Zubarev): Already at L2 Zubarev branch (G51 iv). Report O_L2 = -0.998 directly; compute shift vs L1 reading (w0_FW = -0.918, mixed-scheme).
>   - Row #18 (w_0 zeta): Compute O_L2 = w_0 under Zubarev canonicalization starting from zeta-branch initial data. Compare to L1 zeta reading.
>   - Row #24 (a_2-cluster): Recompute cluster span at L2 Zubarev (drop the 4 non-Zubarev regulators from the 5-regulator atlas). Compare to S82 W2-8 60.35% var.
>   - Row #38 (mu_eff LK): Recompute Lindblad-Keldysh mu_eff under Zubarev temporal cutoff in place of exponential Lindblad kernel. Compare to S82 INFO 8.58e-4.
>
> **Cross-checks**:
> 1. Layer-selection rule: The §VII.K-META meta-principle (R-protected <= 1.5 / NOT-R-protected >= 2.5, S83-G58 PASS) predicts that UNPINNED rows should ALL be NOT-R-protected -- verify by computing the Mellin balance status of each UNPINNED row.
> 2. CC-5 propagation: If row is composable (O = prod F_i^|p_i|), verify CC-5 identity span_L2(O) = prod span_L2(F_i)^|p_i| at <0.02% residual.
> 3. Consistency with G51 FAIL: The w_0 rows #17 and #18 failed canonical-choice audit at S83-G51 (-0.998 vs -0.918). Verify that the L2-canonicalization shift factor aligns with the G51 magnitude (0.998/0.918 = 1.087 shift, below PROMOTE-L2 threshold 1.5 -- so w_0 Zubarev is expected to PROMOTE-L2).
>
> **Output file names**:
> - `computations/s84_w2c_unpinned_l2_audit.py` (script)
> - `computations/s84_w2c_unpinned_l2_audit.npz` (data: 5-row shift-factor table)
> - `computations/s84_w2c_unpinned_l2_audit.md` (working-paper section §VII.M-UNPINNED)
>
> **Verdict-line target**: `computations/s84_gate_verdicts.txt` appended with:
> ```
> S84-UNPINNED-L2-AUDIT: PASS|FAIL|INFO -- value=<max shift_factor> scheme=Zubarev-L2 convention=CC5 L_max=5 sha256=<closure>
> ```

**Machinery pin (PRDR)**:
- L_max = 5 (matches W1-G1 anchor and the L1 readings from S82/S83)
- scan_range: 5 UNPINNED rows from §VII.K-META (fixed row-set per Lizzi synthesis §II.4, no free scan)
- tolerance: shift_factor reported to 3 significant figures; CC-5 residual < 0.02% where applicable
- scheme: Zubarev-L2 canonicalization (Lambda_Z cutoff matched to Zubarev entropy-max local min)
- convention: CC-5 Mellin decomposition for composable rows; direct observable reading for non-composable
- random_seed: N/A (deterministic per-row arithmetic except for row #24, which uses deterministic seed=42 for the 5-regulator atlas shuffle consistency)
- GPU path: torch.linalg.eigvals for row #24 (D_K spectrum at L_max=5, ~10^4 eigenvalues); CPU OMP=8 for rows #13, #17, #18, #38

**Expected output 4-tuple**: `(value=<max shift_factor across 5 UNPINNED rows>, scheme=Zubarev-L2, convention=CC5, L_max=5)`

**PASS / FAIL / INFO thresholds**:
- **PASS**: All 5 UNPINNED rows yield shift_factor < 1.5 (L2 is ALSO a valid pin for each; UNPINNED is redundant with L2-pinned, suggesting §VII.K-META should collapse UNPINNED -> L2-pinned sub-bucket). Tolerance rule: RATIO (factor-1.5 uniform band).
- **FAIL**: Any row's L2 shift factor exceeds 3 (that row is genuinely unpinned by either layer -- §VII.K-META structural gap, not a labeling artifact). Tolerance rule: RATIO (factor-3 threshold per row).
- **INFO**: 1-2 rows in the 1.5-3 factor range (borderline; sub-classification UNPINNED-L2-PARTIAL). Tolerance rule: RATIO (factor-1.5 to factor-3 band).

**Substitution chain** (mandatory for [AUDIT] trigger):

1. **Definition** (canonical, L1): L1 reading O_L1(row) = observable value under axiomatic Dixmier-unique zeta regulator (S83-G3 PASS). UNPINNED rows are defined as rows where L1 ambiguity persists despite A1-A6 axiom enforcement.
2. **Definition** (canonical, L2): L2 reading O_L2(row) = observable value under Zubarev substrate-action local-minimum regulator (S83-G1 PASS).
3. **Definition** (new, for this gate): shift_factor(row) = max(|O_L1|, |O_L2|) / min(|O_L1|, |O_L2|). Dimensionless; always >= 1.
4. **Substitute** (row-by-row): For each of 5 UNPINNED rows, plug (O_L1 from S82/S83 record, O_L2 from L2 canonicalization) into shift_factor definition.
5. **Simplify**: shift_factor = max / min directly; no algebraic simplification needed.
6. **Read direction**: shift_factor < 1.5 <=> L1 and L2 agree within factor-1.5 (L2 is a valid alternative pin); shift_factor > 3 <=> L1 and L2 disagree strongly (row is unpinned by either layer); 1.5-3 <=> borderline.
7. **Conclusion**: PROMOTE-L2 iff shift_factor < 1.5; GENUINE-UNPINNED iff shift_factor > 3; BORDERLINE iff 1.5-3.

**What PASSES / FAILS MEAN for solution space**:
- **PASS**: All 5 UNPINNED rows promote to L2-pinned. The §VII.K-META UNPINNED bucket is redundant -- collapses to L2-pinned sub-bucket. This STRENGTHENS the three-layer theorem: every observable in the 42-row atlas pins to one of {L0-INT, L1-AX, L2-SA, L3-OB} with NONE genuinely unpinned. W2a-13 predicted distribution 26/2/1/8/5 revises to 26/2/1/13/0 (pins into L3-OB sub-bucket).
- **FAIL**: If any UNPINNED row fails to pin at L2, the three-layer theorem has a structural gap. W2a-11 registration must scope-restrict to "applies to 42-minus-N rows" or introduce a fourth layer. Each GENUINE-UNPINNED row becomes a target for new structural work.
- **INFO**: Partial promotion (3-4 of 5 rows promote). §VII.K-META UNPINNED bucket is partially redundant; W3 follow-up to classify the borderline rows.

**Effort estimate**: 1-2 sessions, MEDIUM. Row #24 requires D_K spectrum reload at L_max=5 (GPU eigendecomposition); rows #13, #17, #18, #38 are scalar arithmetic. lizzi-spectral-functional-theorist is the natural agent because the substrate-action functional analysis (L2 Zubarev canonicalization) is within Lizzi's regulator-uniqueness proof toolkit.

**Substrate-framing reminder in agent dispatch prompt**: UNPINNED rows are substrate-level ambiguities, not observer-frame ambiguities. The L2 Zubarev canonicalization is the substrate's entropy-maximizing choice -- it is NOT an external scheme imposed on a pre-existing observable. The direction of explanation is: D_K spectrum -> S_Zubarev local-min -> regulator choice -> observable value. If a row fails to pin at L2, it means the substrate itself is ambiguous on that observable, not that we lack a coordinate system.

---

## §W2c-20. S84-LAYER-UNIQUENESS-LMAX-EXTRAPOLATION

**Gate ID**: S84-LAYER-UNIQUENESS-LMAX-EXTRAPOLATION

**Trigger**: `[VERIFY-THEOREM]`

**Classification**: GEOMETRIC

**Agent type**: connes-ncg-theorist

**Hypothesis**: The W1-G1 3-criterion intersection (which selects Zubarev as the unique substrate-action minimum at L2 and zeta as the unique Dixmier-axiom regulator at L1) is a structural property of the Jensen-deformed SU(3) spectral triple, NOT a truncation artifact at L_max=5. Specifically: (i) Zubarev remains the unique local-min of S_substrate-action at L_max=7 and L_max=9; (ii) zeta remains the unique A1-A6-compliant regulator at L_max=7 and L_max=9; (iii) no alternative regulator in the 5-element atlas {zeta, Zubarev, SDW, dim-reg, lattice-BR} satisfies both L1 and L2 uniqueness at any L_max.

**Method** (full self-contained dispatch prompt for connes-ncg-theorist):

> You are a connes-ncg-theorist dispatch for S84-LAYER-UNIQUENESS-LMAX-EXTRAPOLATION.
>
> **SUBSTRATE FRAMING (mandatory)**: The substrate self-determines at two strata -- axiomatic (L1 Dixmier-trace class, zeta-unique under A1-A6) and substrate-action (L2 spectral-action-functional local-min, Zubarev-unique). The W1-G1 PASS at L_max=5 is the first-principles numerical sanity check. This gate extrapolates to higher truncation to verify the uniqueness is structural, not a coincidence of truncation level. NEVER explain the L_max=5 anchor via GR or QFT. The direction of explanation is D_K spectrum at L_max -> S_functional at L_max -> uniqueness classification at L_max.
>
> **Task**: Recompute the W1-G1 3-criterion intersection at L_max=7 and L_max=9. The three criteria (from Connes synthesis Appendix A §VII.M):
>   - **Criterion A (Dixmier-trace class)**: regulator satisfies A1-A6 axioms. passes[zeta]=True; passes[Zubarev]=True; passes[SDW]=True; passes[dim-reg]=False; passes[lattice-BR]=False (L1 uniqueness: only zeta survives all axioms; Zubarev and SDW fail A6).
>   - **Criterion B (chi_KK = +1 sign)**: regulator yields correct KK-sector sign. passes[zeta]=True; passes[Zubarev]=True; passes[SDW]=False; passes[dim-reg]=(TBD); passes[lattice-BR]=(TBD).
>   - **Criterion C (S_functional has local minimum, curv > 0)**: passes[zeta]=False (curv_zeta = 0 structurally; no local minimum); passes[Zubarev]=True (curv_Zubarev = +1.16e+5 at L_max=5); passes[SDW]=True.
>
> For each L_max in {7, 9}:
>
> 1. Load or build D_K spectrum on Jensen-deformed SU(3) at tau=0.19. At L_max=7, expected ~10^5 eigenvalues; at L_max=9, expected ~10^6 eigenvalues (GPU MANDATORY).
> 2. For each of 5 regulators {zeta, Zubarev, SDW, dim-reg, lattice-BR}:
>    - Compute S_functional(regulator, L_max) = spectral-action evaluated at tau=0.19.
>    - Compute curv(regulator, L_max) = d^2 S_functional / d tau^2 at tau=tau_fold (central difference).
>    - Compute chi_KK(regulator, L_max) = sign of KK-sector parity invariant.
>    - Test A1-A6 axiom compliance (Dixmier-trace class).
> 3. Build the 3-criterion intersection truth table at each L_max:
>    ```
>    L_max | regulator    | A | B | C | intersect
>    7     | zeta         | T | T | F | False (Criterion C fails)
>    7     | Zubarev      | T | T | T | True  (unique L2 min if only row)
>    7     | SDW          | T | F | T | False (Criterion B fails)
>    ...
>    ```
> 4. Record S_zeta / S_Zubarev at L_max=7 and L_max=9 (sanity-anchor ratio; at L_max=5 this is 42.03 per Connes synthesis Appendix A).
> 5. Extrapolation ansatz: curv_Zubarev(L_max) ~ L_max^alpha with alpha ~ 2 expected from Seeley-DeWitt trace structure; test log-log fit and report alpha.
>
> **Canonical constants (MANDATORY)**:
> ```python
> from canonical_constants import *
> # tau_fold=0.19, M_KK, Delta_BCS=0.4642, E_cond=-0.1369,
> # Vol_SU3, J_C2, omega_L1, dS_fold, d2S_fold, S_fold,
> # H_TD=5.9076e-3, eps_H=0.02163
> ```
> Every derived intermediate tagged with `# (local)`.
>
> **Input SHA-256 pins**:
> - `D_K_spectrum_L5.npz` (reference spectrum at L_max=5) -- `<computed-at-runtime>`
> - `D_K_spectrum_L7.npz` (if pre-built; else regenerate) -- `<computed-at-runtime>`
> - `D_K_spectrum_L9.npz` (if pre-built; else regenerate) -- `<computed-at-runtime>`
> - `s83_w1_g1_zubarev_unique.npz` (L_max=5 reference values) -- `<computed-at-runtime>`
> - `canonical_constants.py` (live import) -- `<computed-at-runtime>`
>
> **Numerical procedure**:
> - Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
> - GPU path MANDATORY: `torch.linalg.eigvals` for D_K matrix construction at L_max=7 (~10^5 eigenvalues) and L_max=9 (~10^6 eigenvalues). AMD RX 9070 XT (17.1 GB VRAM, ROCm 7.2) -- the L_max=9 spectrum is near VRAM limit; use chunked diagonalization (block by SU(3) irrep with p+q <= 9) if full-matrix eigendecomposition OOMs.
> - Seeley-DeWitt trace: compute S_functional via truncated heat-kernel expansion, using the D_K eigenvalue spectrum summed over Peter-Weyl blocks.
> - Curvature computation: d^2 S / d tau^2 via 5-point central difference with step tau = 1e-4.
> - Sign of chi_KK: product of sign(eigenvalue) over KK-tower levels, weighted by gauge-module degeneracy.
>
> **Cross-checks**:
> 1. L_max=5 reproduction: Recompute S_functional, curv, chi_KK at L_max=5 and verify match with W1-G1 anchors (curv_Zubarev = +1.16e+5; chi_KK[Zubarev] = +1; S_zeta/S_Zubarev = 42.03). Tolerance: relative error < 1%.
> 2. Monotonic extrapolation: Expect curv_Zubarev(L_max) to grow monotonically in L_max (Seeley-DeWitt trace is positive-definite and truncation-sensitive). If curv_Zubarev(7) or curv_Zubarev(9) is non-monotonic or < curv_Zubarev(5), flag as numerical artifact (cross-check GPU precision).
> 3. Alpha extrapolation: Log-log fit curv_Zubarev ~ L_max^alpha across {5, 7, 9}. Expected alpha ~ 2 from Seeley-DeWitt a_2 scaling. If alpha < 0, FAIL (curv diverges in wrong direction); if |alpha - 2| > 0.5, INFO (scaling exponent off but sign correct).
> 4. Ratio stability: S_zeta / S_Zubarev at L_max=7 and L_max=9. If ratio drifts by factor > 3 from L_max=5 anchor (42.03), flag as L_max-sensitive (the ratio itself may be an artifact). Expected drift factor <= 1.5 if truly structural.
>
> **Output file names**:
> - `computations/s84_w2c_layer_uniqueness_lmax_extrapolation.py` (script)
> - `computations/s84_w2c_layer_uniqueness_lmax_extrapolation.npz` (data: 3-criterion truth tables at L_max={5, 7, 9})
> - `computations/s84_w2c_layer_uniqueness_lmax_extrapolation.md` (working-paper section §VII.M-LMAX)
>
> **Verdict-line target**: `computations/s84_gate_verdicts.txt` appended with:
> ```
> S84-LAYER-UNIQUENESS-LMAX-EXTRAPOLATION: PASS|FAIL|INFO -- value=<alpha> scheme=multi-regulator convention=3-criterion L_max=9 sha256=<closure>
> ```

**Machinery pin (PRDR)**:
- L_max grid: {5 (reference anchor), 7, 9} -- 3-point extrapolation; fixed grid, no free scan
- scan_range: 5 regulators {zeta, Zubarev, SDW, dim-reg, lattice-BR} x 3 L_max values x 3 criteria = 45 truth-table entries
- tolerance: curv to 3 significant figures; chi_KK exact sign; S_zeta/S_Zubarev to 4 significant figures; alpha fit via scipy log-log linear regression (R^2 > 0.95 required for decisive alpha extraction)
- scheme: 5-regulator atlas (all regulators evaluated; no scheme-selection during the audit)
- convention: CC-5 Mellin decomposition for trace computation; Peter-Weyl block-diagonal D_K (uses proven S27 block-diagonality, off-diag 8.4e-15 machine epsilon)
- random_seed: 42 (deterministic for any Monte Carlo sub-components if added later; current path is deterministic)
- GPU path: torch.linalg.eigvals on AMD RX 9070 XT ROCm 7.2; dtype=float64; chunked by SU(3) irrep blocks (p+q) if L_max=9 full-matrix OOMs VRAM (17.1 GB cap)

**Expected output 4-tuple**: `(value=<alpha scaling exponent of curv_Zubarev ~ L_max^alpha>, scheme=multi-regulator, convention=3-criterion-intersection, L_max=9)`

**PASS / FAIL / INFO thresholds**:
- **PASS**: Zubarev remains the unique row with (A=T AND B=T AND C=T) at both L_max=7 and L_max=9 AND zeta remains the unique row satisfying criterion A at both L_max=7 and L_max=9 AND alpha in [1.5, 2.5] (Seeley-DeWitt scaling confirmed). Tolerance rule: THEOREM (exact truth-table match at L_max=7 and L_max=9 for the intersection; RATIO factor-1.25 for alpha).
- **FAIL**: Either (a) Zubarev loses uniqueness at L_max=7 or L_max=9 (another regulator gains C=T), OR (b) zeta loses A1-A6 compliance at higher L_max (another regulator also satisfies A), OR (c) alpha < 0 (curv_Zubarev shrinks as L_max grows, inverting Seeley-DeWitt scaling). Any of these means W1-G1 PASS at L_max=5 is a truncation artifact. Tolerance rule: ABSOLUTE (presence of uniqueness inversion).
- **INFO**: Alpha in [0.5, 1.5] or [2.5, 4] -- scaling exponent off but sign correct, uniqueness preserved. OR S_zeta/S_Zubarev ratio drifts by factor > 1.5 at L_max=7 or L_max=9 while uniqueness is preserved (ratio is not structural, but theorem holds). Tolerance rule: RATIO (factor-1.5 ratio drift; factor-2 alpha window).

**Substitution chain** (mandatory for [VERIFY-THEOREM] trigger):

1. **Definition** (W1-G1 at L_max=5): A (Dixmier-trace): passes[regulator] is a boolean per regulator, computed from A1-A6 axiom compliance. B (chi_KK=+1): passes[regulator] = (sign(chi_KK[regulator]) == +1). C (curv>0): passes[regulator] = (curv_Sfunctional[regulator] > 0).
2. **Definition** (3-criterion intersection): PASS[regulator] = A[regulator] AND B[regulator] AND C[regulator]. Uniqueness-at-intersection: exactly one regulator has PASS[regulator] = True.
3. **Anchor values** (L_max=5 from W1-G1): PASS[zeta] = T AND T AND F = False (curv_zeta = 0 structurally). PASS[Zubarev] = T AND T AND T = True (curv_Zubarev = +1.16e+5; chi_KK=+1; S_Zubarev=3.806e+3). PASS[SDW] = T AND F AND T = False (chi_SDW = sign(cos(pi S_SDW / (2 N_modes))) = -1 fails B).
4. **Extrapolation definition**: PASS[regulator, L_max] = A[regulator, L_max] AND B[regulator, L_max] AND C[regulator, L_max]. Uniqueness-at-intersection at L_max=L: exactly one regulator has PASS[regulator, L_max=L] = True.
5. **Substitute** (L_max=7): Compute (A, B, C) for each of 5 regulators at L_max=7 from GPU eigendecomposition. Build truth table. Check uniqueness-at-intersection.
6. **Substitute** (L_max=9): Same, at L_max=9.
7. **Scaling law substitution**: curv_Zubarev(L_max) expected to satisfy curv(L_max) = C_0 * L_max^alpha + O(L_max^{alpha-1}). Fit log(curv) vs log(L_max) over {5, 7, 9}; extract alpha.
8. **Simplify**: uniqueness-at-intersection at L_max=7 AND at L_max=9 AND alpha in [1.5, 2.5] => theorem PASS.
9. **Read direction**: If uniqueness is preserved, W1-G1 extends to higher L_max and the three-layer theorem is structural. If inverted, W1-G1 is truncation-artifactual and theorem-scope must be qualified as "structurally valid at finite L_max only".
10. **Conclusion**: PASS iff (Zubarev unique L2 at L_max in {7, 9}) AND (zeta unique L1 at L_max in {7, 9}) AND (alpha in [1.5, 2.5]).

**What PASSES / FAILS MEAN for solution space**:
- **PASS**: The three-layer regulator theorem is structurally anchored at all computable L_max. W1-G1 PASS is structural, not truncation-dependent. Registers as permanent theorem candidate with "L_max-independent" tag. W2a-11 (§VII.M landing) proceeds with full-scope claim.
- **FAIL**: W1-G1 PASS at L_max=5 falsifies its own scope at higher L_max. The three-layer theorem is structurally valid ONLY at truncated L_max, not in the asymptotic limit. W2a-11 must register with "L_max=5 truncation-artifactual" qualifier. This is a significant scope restriction: the theorem becomes a numerical coincidence of the L_max=5 spectrum rather than an axiomatic truth. Downstream: every S83 gate that cited W1-G1 PASS as a structural anchor (G3, G58 META, G61 MIXED sub-tags, G51 canonical choice) requires re-audit.
- **INFO**: Theorem holds but scaling exponent alpha deviates from Seeley-DeWitt prediction. Uniqueness is structural but the quantitative extrapolation law requires refinement. Feeds into W3 scaling-law audit.

**Effort estimate**: 2-3 sessions, HIGH. L_max=9 is near the VRAM limit of the AMD RX 9070 XT (17.1 GB); may require chunked diagonalization by SU(3) irrep blocks. L_max=7 eigendecomposition is ~10^5 eigenvalues -- 1-2 hours on GPU. L_max=9 eigendecomposition is ~10^6 eigenvalues -- several hours with chunking. connes-ncg-theorist is the natural agent because the spectral-action-functional-minimum uniqueness proof and Dixmier-axiom compliance proof are within the Connes-NCG toolkit.

**Substrate-framing reminder in agent dispatch prompt**: Criteria A, B, C are substrate-level structural properties, NOT external axiom checks imposed on D_K. A1-A6 Dixmier axioms are the substrate's own admissibility conditions for a regulator; chi_KK sign is the substrate's own KK-parity invariant; S_functional local-min is the substrate's own entropy-maximization condition. The L_max extrapolation audits whether these substrate-level properties are stable under increased spectral-triple truncation -- if they are NOT, the substrate's self-determination (S83-MASTER theorem) is itself a truncation effect. Never frame this audit as "does the theorem hold in higher resolution" -- frame it as "does the substrate continue to self-determine as more of its spectral structure is resolved".

---

## W2c -> W2a / W2b Parallel Dispatch Note

W2c runs in parallel with W2a (11-17) and W2b (other three-layer items) under the concurrent-dispatch cap of ~8 agents per session. All three sub-waves (W2a, W2b, W2c) share the same three-layer theorem anchor (W1-G1 PASS at L_max=5) but test orthogonal aspects:

- **W2a**: theorem-statement landing + cross-KO-dim falsifier + per-row pin registry + L1-vs-L2 projection
- **W2b**: MP admissibility across regulators + pin-derivation census for NOT-R-protected + cocycle L1/L2/MIXED classification
- **W2c**: transport mechanics (MIXED rows) + UNPINNED L2 stress + L_max extrapolation

**Cross-wave input dependencies**: W2c does NOT depend on W2a or W2b outputs within the same session. However, W2a-13 (LAYER-PIN-REGISTRY-LANDING) predicts a 26/2/1/8/5 distribution; W2c-19 (UNPINNED-L2-AUDIT) verifies or falsifies the "5 UNPINNED" sub-bucket. If W2c-19 PASSES (all 5 promote to L2-pinned), W2a-13 predicted distribution revises to 26/2/1/13/0 in the W3 write-up.

**Dispatch coordination**: All three sub-waves dispatch simultaneously; no cross-talk during computation. Results assembled in W3 decision point.

---

## W2c -> W3 Decision Point

After W2c completes, W3 convenes the three-layer theorem synthesis based on combined W2a + W2b + W2c outputs.

**Decision rules**:

1. **W1-G1 structural anchor**: If W2c-20 PASSES (uniqueness preserved at L_max=7 and L_max=9 with alpha in [1.5, 2.5]), the three-layer theorem is registered as permanent with "L_max-independent" tag. If W2c-20 FAILS, theorem is registered with "L_max=5 truncation-artifactual" qualifier and downstream S83 gates re-audit queue in W3.

2. **MIXED classification structural completeness**: If W2c-18 PASSES (all 10 MIXED rows yield finite sigma_row with correct sub-tag centroid alignment), the MIXED bucket is structurally complete and §VII.K-META 4-bucket classification is final. If FAIL, MIXED classification needs sub-structure refinement in W3.

3. **UNPINNED bucket redundancy**: If W2c-19 PASSES (all 5 UNPINNED rows promote to L2-pinned), the UNPINNED bucket is redundant and collapses into L2-SA sub-bucket in the final §VII.K-DUAL atlas. W2a-13 predicted distribution 26/2/1/8/5 revises to 26/2/1/13/0. If FAIL, UNPINNED rows require structural work in W3 or a fourth layer in the theorem.

4. **Joint scope of the theorem**: If all three W2c gates PASS, the three-layer theorem achieves **operational closure**: statement (W2a-11) + explicit transport (W2c-18) + bucket completeness (W2c-19) + L_max invariance (W2c-20). Promotes to permanent-results-registry alongside §VII.N (IKKT anti-correspondence + 11-dim exclusion). If any W2c gate FAILS or returns INFO, the theorem lands with scope-qualifier and the specific gap becomes a W3 target.

**W3 targets conditional on W2c outcomes**:
- W2c-18 FAIL -> W3-MIXED-REFINEMENT (new sub-bucket partition)
- W2c-19 FAIL -> W3-UNPINNED-STRUCTURAL (either new layer or genuine-unpinned acceptance)
- W2c-20 FAIL -> W3-LMAX-ARTIFACT (scope-restriction re-audit across all S83 gates citing W1-G1)
- All three PASS -> W3-THEOREM-LANDING (formal §VII.M registry entry + permanent-results-registry promotion)

---

## W2c Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, all gate-relevant machinery parameters are pinned below to prevent PRU (Pre-Registration Underspecification, Class 8 plan-property failure). This §0.11 block is the PRDR (Pre-Registration Dry-Run) output for W2c.

### Common (all three W2c gates)

| Parameter | Value | Source / Note |
|:----------|:------|:--------------|
| `tau_fold` | 0.19 | canonical_constants.py |
| `Delta_BCS` | 0.4642 | canonical_constants.py |
| `E_cond` | -0.1369 | canonical_constants.py |
| `Vol_SU3` | canonical | canonical_constants.py |
| `H_TD` | 5.9076e-3 | canonical_constants.py |
| `eps_H` | 0.02163 | canonical_constants.py |
| `S_Zubarev` at L=5 | 3.806e+3 | W1-G1 PASS anchor |
| `S_zeta / S_Zubarev` at L=5 | 42.03 | W1-G1 numerical sanity |
| `curv_Zubarev` at L=5 | +1.16e+5 | W1-G1 local-min curvature |
| `chi_KK[Zubarev]` at L=5 | +1 | W1-G1 sign |
| Python env | `"phonon-exflation-sim/.venv312/Scripts/python.exe"` | mandatory (GPU ROCm) |
| OMP cap (CPU paths) | 8 | OMP_NUM_THREADS=8 |
| Hardware | AMD RX 9070 XT 17.1 GB VRAM ROCm 7.2 | torch.linalg GPU path |
| Random seed | 42 | all stochastic sub-components (if added) |
| SHA closure | 64-char hexdigest | S81+ canonical verdict format |
| Verdict file | `computations/s84_gate_verdicts.txt` | S84 canonical |

### W2c-18 specific

| Parameter | Value | Source / Note |
|:----------|:------|:--------------|
| L_max | 5 (fixed) | matches W1-G1 anchor |
| Row-set | 10 MIXED rows from §VII.K | S83-G54 PASS + G61 sub-tag partition |
| Transport definition | sigma_row = span_L3 / Delta_L2 | gate-defined |
| CC-5 residual tolerance | < 0.02% | S83-G34 PASS threshold |
| Sub-tag centroid bands | FI-pin [0.8, 1.5]; mostly-RD < 0.5; promotable > 2 | predicted |
| GPU path | CPU (scalar arithmetic) | no eigendecomposition needed |
| Output shape | 10-row sigma table | (row_id, Mellin_slots, p, Delta_L2, span_L3, sigma, sub_tag) |

### W2c-19 specific

| Parameter | Value | Source / Note |
|:----------|:------|:--------------|
| L_max | 5 (fixed) | matches S82/S83 UNPINNED records |
| Row-set | 5 UNPINNED rows | Lizzi synthesis §II.4 Python-validated |
| L2 canonicalization | Zubarev Lambda_Z cutoff | from W1-G1 |
| shift_factor definition | max(\|O_L1\|, \|O_L2\|) / min(\|O_L1\|, \|O_L2\|) | gate-defined |
| PROMOTE-L2 threshold | shift_factor < 1.5 | gate-defined |
| GENUINE-UNPINNED threshold | shift_factor > 3 | gate-defined |
| BORDERLINE band | 1.5 - 3 | gate-defined |
| GPU path | torch.linalg for row #24 (D_K reload); CPU for rows #13, #17, #18, #38 | mixed |

### W2c-20 specific

| Parameter | Value | Source / Note |
|:----------|:------|:--------------|
| L_max grid | {5, 7, 9} | fixed extrapolation points |
| Regulator atlas | 5 regulators {zeta, Zubarev, SDW, dim-reg, lattice-BR} | from §VII.K-META |
| Criterion A | A1-A6 Dixmier-trace class | S83-G3 axioms |
| Criterion B | chi_KK = +1 | KK-parity sign |
| Criterion C | d^2 S_functional / d tau^2 > 0 at tau_fold | local-min test |
| Curvature step size | tau = 1e-4 | 5-point central difference |
| Extrapolation ansatz | curv_Zubarev(L_max) ~ L_max^alpha | Seeley-DeWitt a_2 |
| Expected alpha | ~ 2 | Seeley-DeWitt trace scaling |
| Alpha PASS band | [1.5, 2.5] | factor-1.25 around 2 |
| R^2 fit quality | > 0.95 | log-log linear regression |
| GPU path | torch.linalg.eigvals MANDATORY | L_max=7 ~10^5 eig; L_max=9 ~10^6 eig |
| VRAM budget | 17.1 GB (AMD RX 9070 XT) | chunked diag if L_max=9 OOMs |
| Chunking strategy | Peter-Weyl block-diagonal by SU(3) irrep (p,q) with p+q <= L_max | proven S27 block-diagonality (off-diag 8.4e-15) |
| dtype | float64 | precision for small-curvature discrimination |

---

## W2c Input-SHA Ledger

All inputs hashed at runtime via SHA-256 and recorded in the closure SHA for each verdict line. S84+ dual-SHA schema: both `audit_sha256` (machinery pin hash) and `content_sha256` (input-file hash) emitted.

### Static inputs (hash at dispatch time, verified in script)

| Gate | Input | SHA status |
|:-----|:------|:-----------|
| W2c-18 | `canonical_constants.py` | `<computed-at-runtime>` |
| W2c-18 | `s83_w3_g54_hp_even_completeness_audit_vii.npz` | `<computed-at-runtime>` |
| W2c-18 | `s83_w1_g1_zubarev_unique.npz` | `<computed-at-runtime>` |
| W2c-18 | `s83_g61_mixed_sub_tag.npz` | `<computed-at-runtime>` |
| W2c-19 | `canonical_constants.py` | `<computed-at-runtime>` |
| W2c-19 | `s82_w2_g2_unified_backreact_79.npz` | `<computed-at-runtime>` |
| W2c-19 | `s83_w3_g51_w0_regulator.npz` | `<computed-at-runtime>` |
| W2c-19 | `s82_w2_g8_a2_cluster.npz` | `<computed-at-runtime>` |
| W2c-19 | `s82_mu_eff_lindblad_keldysh.npz` | `<computed-at-runtime>` |
| W2c-19 | `s83_w1_g1_zubarev_unique.npz` | `<computed-at-runtime>` |
| W2c-20 | `canonical_constants.py` | `<computed-at-runtime>` |
| W2c-20 | `D_K_spectrum_L5.npz` | `<computed-at-runtime>` |
| W2c-20 | `D_K_spectrum_L7.npz` (if pre-built; regenerate otherwise) | `<computed-at-runtime>` |
| W2c-20 | `D_K_spectrum_L9.npz` (if pre-built; regenerate otherwise) | `<computed-at-runtime>` |
| W2c-20 | `s83_w1_g1_zubarev_unique.npz` | `<computed-at-runtime>` |

### Dynamic inputs (generated during W2c)

| Gate | Output | SHA status |
|:-----|:-------|:-----------|
| W2c-18 | `s84_w2c_layer_transport_audit.npz` (transport table) | emitted as closure |
| W2c-19 | `s84_w2c_unpinned_l2_audit.npz` (shift-factor table) | emitted as closure |
| W2c-20 | `s84_w2c_layer_uniqueness_lmax_extrapolation.npz` (truth tables + alpha fit) | emitted as closure |

### S83 SHA cross-collision audit

Per S83-G55 FAIL (1/3 S82 SHAs collided), all W2c verdict SHAs are checked against the S83 verdict ledger and S82 W1-1-TD/W2-13/W3-7 regenerated SHAs (S84-SHA-COLLISION-REGEN is the parent repair gate). If any W2c SHA matches a prior verdict SHA, the script is flagged for copy-paste-or-hardcode error per `.claude/rules/gate-verdicts.md`.

---

**End of W2c plan. 4 gates, all pre-registered. W2c dispatches in parallel with W2a and W2b under the concurrent cap. S84-G-AUDIT appended as the final gate by orchestrator directive; not a W2c-native gate (einstein-theorist owned).**

---

## §W2c-G-AUDIT. S84-G-AUDIT -- Newton Constant Observational-Pinning Audit

**Gate ID**: S84-G-AUDIT

**Classification**: GEOMETRIC (second Seeley-DeWitt moment -> Einstein-Hilbert coefficient)

**Trigger**: `[VERIFY]` + `[SIGN]`

**Owner**: einstein-theorist (appended to W2c by orchestrator directive; not a W2c-native gate)

**Hypothesis tested**: Can G be observationally pinned to a single (f_2 scheme x M_KK route) combination via NIST-BIPM 2026 G = 6.67387(38) x 10^-11 m^3 kg^-1 s^-2 at 5.7 x 10^-5 relative precision, following the S67 HIGGS-ZETA-67 observational-exclusion pattern that pinned m_H?

**Master equation (Eq A, SA canonical, s44 derivation from Connes-Chamseddine 2007)**:
```
1/(16 pi G_N) = (6 / pi^3) * f_2 * a_2 * M_KK^2
=> G_N = pi^2 / (96 * f_2 * a_2 * M_KK^2)
```

**Substitution chain (directions)**:
- d(ln G_N) / d(ln f_2)   = -1  -> f_2 up  => G_N down
- d(ln G_N) / d(ln a_2)   = -1  -> a_2 up  => G_N down
- d(ln G_N) / d(ln M_KK)  = -2  -> M_KK up => G_N down

**Machinery pin (PRDR)**:
- Master-eq convention: Eq A (SA canonical, s44)
- a_2 normalization: PW-weighted spectral zeta (CONST-FREEZE-42)
- L_max: 10 (S75 a2_full_L10 = 64308.24); NOTE -- a_2(L=3) = 2776 vs a_2(L=10) = 64308 gives factor 23.16x swing, a_2 is NOT converged to 5.7 x 10^-5
- BCS dressing: INCLUDED (s76 delta_a_2 = -4.5006, 0.16% correction)
- f_2 schemes: {sharp: 1, Gaussian: 2.34 (canonical f_2_default), SDW-L^2: 2/3, f*: 214.97}
- M_KK routes: {gravity (7.43 x 10^16 GeV, CIRCULAR -- excluded from verdict), Kerner (5.04 x 10^17 GeV, INDEPENDENT)}
- Vol(SU(3)): 8 sqrt(3) pi^4 = 1349.74 (Haar/Weyl)
- Eigenvalue cutoff: lambda_min > 0.01 (S41 convention)
- GPU backend: torch.linalg on ROCm for any a_2 recomputation

**Input SHA-256 pins (computed)**:
- `d49412402ad9e732a7a7270ee042e857e6899bdbc191de8237b7b96762fb28ec` canonical_constants.py
- `aec4fb985e8e861675f8e4c850288f15e0d23f17f2493c31f477d6d77b8c1cae` s61_heat_kernel_a2.npz
- `34b9b457a0a8f4bbba152f447c154d1ec031a9f44e128e20d5820d06a966df08` s76_bcs_dressing_a2.npz
- `39f613507950979327f0d9b7473bd73f7b0a7ea2d9d0c5507f6b8b939909f80b` s42_constants_snapshot.npz
- `125d57375989a15ad8c41a69b0434001f3b1e3e7073dda19f6c031d9e254cca6` s82_w2_5_heat_kernel_mp.npz
- `db2958043020a8235eafcd225039defc2daca511fc44e3c140d87633feba9024` s83_w3_g57_pinning_audit.py
- `7bebad7da7c57b4d2706fd4e123cfbb762fa63c0244e143d597068fb7a574fb4` s83_gate_verdicts.txt

**Pre-registered verdict criteria**:
- **PASS (FI-via-pinning)**: exactly one Kerner-route x f_2-scheme combination under Eq A at the L_max-converged a_2 delivers |G_pred / G_obs - 1| < 5.7 x 10^-5. Gravity-route matches DO NOT count (circular). G becomes fifth FI_pin observable.
- **INFO-promotable-to-FI**: multiple combinations within 5.7 x 10^-5; secondary constraint needed (LLR, nucleosynthesis G(z=10^9) / G_0 bound, or third independent M_KK route).
- **INFO-mostly-RD**: no combination within 5.7 x 10^-5 but at least one Kerner combination within 1%. G joins w_0, H_0 in mostly-RD.
- **FAIL**: no Kerner combination within 1% after L_max convergence. Master equation structurally wrong; points at Eq A prefactor error, missing dressing term, or obstruction requiring third M_KK route.
- **PRE-REG-INCOMPLETE (PRU Class 8, most likely outcome)**: L_max-convergence of a_2 to 5.7 x 10^-5 precision not demonstrated at L_max=10. Factor-23 swing L=3 -> L=10 means required L_max ~ O(100) or a resummation certificate. Gate returns PRE-REG-INCOMPLETE until Richardson extrapolation or asymptotic-form proof is supplied.

**Numerical pre-verification (Python executed, L_max=3 spot check)**:
```
Route                   Scheme                         G_pred / G_obs
gravity (CIRCULAR)      sharp (f_2=1)                  1.000   (calibrated, excluded)
gravity (CIRCULAR)      Gaussian (f_2=2.34)            0.427
Kerner (INDEP)          sharp (f_2=1)                  0.0217
Kerner (INDEP)          Gaussian (f_2=2.34)            0.00928
Kerner (INDEP)          SDW L^2 (f_2=2/3)              0.0326
Kerner (INDEP)          f* (f_2=215)                   1.01e-4
```
At L_max=10, divide ratios by ~23. All Kerner ratios fall to ~10^-3 to ~10^-6. None within 1% without further structural input -> FAIL expected unless PRE-REG-INCOMPLETE takes precedence.

**Expected outcome (EVOI)**: PRE-REG-INCOMPLETE dominant; FAIL secondary; INFO-mostly-RD tertiary; PASS and INFO-promotable both unlikely. Information gain under all branches; PRE-REG-INCOMPLETE branch identifies specific S85 unblocker (a_2 L_max convergence).

**Carry-forward (contingent)**:
- PASS -> unlocks LLR / MICROSCOPE / PPN calibration; collapses M_KK degeneracy
- INFO-promotable -> compute nucleosynthesis bound + third M_KK route
- INFO-mostly-RD -> update S83 pinning atlas; G becomes 3rd mostly-RD
- FAIL -> sign-analysis of Eq A terms; S85 derivation audit
- PRE-REG-INCOMPLETE -> S85 a_2 Richardson extrapolation at L_max >= 15 (GPU-heavy on RX 9070 XT, ~10^6 eigenvalues)

**Output 4-tuple (pre-registration placeholder)**:
```
S84-G-AUDIT: {PASS|INFO|FAIL|PRE-REG-INCOMPLETE} -- value=<G_pred_winner_or_null> scheme=<sharp|Gaussian|SDW-L2|f*|null> convention=Eq-A-SA-canonical L_max=10 sha256=f4655ca286a1486b9644cbf42a8d155c158ae5f5f366fdfdbf8f5da3c2100699
```
